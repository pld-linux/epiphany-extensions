#
%define		basever	2.14
Summary:	Collection of extensions for Epiphany
Summary(pl):	Zbiór rozszerzeñ dla Epiphany
Name:		epiphany-extensions
Version:	2.14.1.1
Release:	19
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/gnome/sources/epiphany-extensions/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	3e807a83f068e41ce34c3c653a3353b6
URL:		http://www.gnome.org/projects/epiphany/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	epiphany-devel >= 2.14.1.1
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.8.3
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.22
BuildRequires:	xulrunner-devel >= 1.8.0.4
BuildRequires:	opensp-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-devel >= 2.12.0
Requires(post,postun):	scrollkeeper
Requires:	epiphany = %(rpm -q --qf '%{EPOCH}:%{VERSION}' epiphany-devel)
%requires_eq	xulrunner
Provides:	epiphany-plugins
Obsoletes:	epiphany-plugins <= 0.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# can be provided by mozilla or mozilla-embedded
%define		_noautoreqdep	libgtkembedmoz.so libgtksuperwin.so libxpcom.so

%description
Epiphany Extensions is a collection of extensions for Epiphany.

%description -l pl
Epiphany Extensions jest zbiorem rozszerzeñ dla Epiphany.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--with-extensions=really-all \
	--with-gecko=xulrunner \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany/%{basever}/extensions/*.{la,py}
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}-%{basever}
%find_lang %{name} --with-gnome
cat %{name}.lang >> %{name}-%{basever}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}-%{basever}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/*.so*
%{_libdir}/epiphany/%{basever}/extensions/[!l]*
%{_datadir}/%{name}
%{_omf_dest_dir}/%{name}
