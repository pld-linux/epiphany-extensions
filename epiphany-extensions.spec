# Conditinal build:
%bcond_with	mozilla_firefox	# build with mozilla-firefox-devel
#
Summary:	Collection of extensions for Epiphany
Summary(pl):	Zbi�r rozszerze� dla Epiphany
Name:		epiphany-extensions
Version:	1.9.6
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/gnome/sources/epiphany-extensions/1.9/%{name}-%{version}.tar.bz2
# Source0-md5:	cbd527a45057da8d7e088d1cad721fae
Patch0:		%{name}-m4.patch
URL:		http://www.gnome.org/projects/epiphany/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1.9
BuildRequires:	dbus-glib-devel >= 0.34
BuildRequires:	epiphany-devel >= 1.9.
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.8.3
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.12.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.22
%if %{with mozilla_firefox}
BuildRequires:	mozilla-firefox-devel
%else
BuildRequires:	mozilla-devel >= 5:1.7
%endif
BuildRequires:	opensp-devel
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-devel >= 2.12.0
Requires:	epiphany = %(rpm -q --qf '%{EPOCH}:%{VERSION}' epiphany-devel)
%if %{with mozilla_firefox}
%requires_eq	mozilla-firefox
%else
Requires:	mozilla-embedded = %(rpm -q --qf '%{EPOCH}:%{VERSION}' --whatprovides mozilla-embedded)
%endif
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
%patch0 -p1

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--with-extensions=all
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany/1.9/extensions/*.{la,py}
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}-1.10

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-1.10.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/epiphany/1.9/extensions/*.so*
%{_libdir}/epiphany/1.9/extensions/[!l]*
%{_datadir}/%{name}
