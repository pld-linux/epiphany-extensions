%define		basever	2.15
Summary:	Collection of extensions for Epiphany
Summary(pl):	Zbi�r rozszerze� dla Epiphany
Name:		epiphany-extensions
Version:	2.15.2
Release:	3
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/gnome/sources/epiphany-extensions/2.15/%{name}-%{version}.tar.bz2
# Source0-md5:	2ec568adefdec0b59d42153d38b9357b
URL:		http://www.gnome.org/projects/epiphany/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.71-2
BuildRequires:	epiphany-devel >= 2.15.92
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.2
BuildRequires:	intltool >= 0.35
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.15.91
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	mozilla-firefox-devel >= 1.5.0.6
BuildRequires:	opensp-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-devel >= 2.15.91
Requires(post,postun):	scrollkeeper
Requires:	epiphany = %(rpm -q --qf '%{EPOCH}:%{VERSION}' epiphany-devel)
%requires_eq	mozilla-firefox
Provides:	epiphany-plugins
Obsoletes:	epiphany-plugins <= 0.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# can be provided by mozilla or mozilla-embedded
%define		_noautoreqdep	libgtkembedmoz.so libgtksuperwin.so libxpcom.so

%description
Epiphany Extensions is a collection of extensions for Epiphany.

%description -l pl
Epiphany Extensions jest zbiorem rozszerze� dla Epiphany.

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
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany/%{basever}/extensions/*.{la,py}

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
%{_libdir}/epiphany/%{basever}/extensions/*.ephy-extension
%{_libdir}/epiphany/%{basever}/extensions/*.py[co]
%{_datadir}/%{name}
%{_omf_dest_dir}/%{name}
