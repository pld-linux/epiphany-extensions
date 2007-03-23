%define		basever	2.18
Summary:	Collection of extensions for Epiphany
Summary(pl.UTF-8):	Zbiór rozszerzeń dla Epiphany
Name:		epiphany-extensions
Version:	2.18.0
Release:	2
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/gnome/sources/epiphany-extensions/2.18/%{name}-%{version}.tar.bz2
# Source0-md5:	c0a6218b6a8506f204891a0769ac9553
URL:		http://www.gnome.org/projects/epiphany/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	epiphany-devel >= 2.18.0
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	gtk+2-devel >= 2:2.10.9
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.18.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	opensp-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-devel >= 2.17.92
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	xulrunner-devel >= 1.8.0.4
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
%requires_eq_to	epiphany epiphany-devel
%requires_eq	xulrunner
Provides:	epiphany-plugins
Obsoletes:	epiphany-plugins <= 0.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# can be provided by mozilla or mozilla-embedded
%define		_noautoreqdep	libgtkembedmoz.so libgtksuperwin.so libxpcom.so

%description
Epiphany Extensions is a collection of extensions for Epiphany.

%description -l pl.UTF-8
Epiphany Extensions jest zbiorem rozszerzeń dla Epiphany.

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

rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany/%{basever}/extensions/{,libepilicious/}*.{la,py}

%find_lang %{name}-%{basever}
%find_lang %{name} --with-gnome
cat %{name}.lang >> %{name}-%{basever}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install epilicious.schemas
%gconf_schema_install smart-bookmarks.schemas

%preun
%gconf_schema_uninstall epilicious.schemas
%gconf_schema_uninstall smart-bookmarks.schemas

%postun
%scrollkeeper_update_postun

%files -f %{name}-%{basever}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/*.so*
%{_libdir}/epiphany/%{basever}/extensions/*.ephy-extension
%{_libdir}/epiphany/%{basever}/extensions/*.py[co]
%dir %{_libdir}/epiphany/%{basever}/extensions/libepilicious
%{_libdir}/epiphany/%{basever}/extensions/libepilicious/*.py[co]
%{_datadir}/%{name}
%{_datadir}/epiphany/icons/hicolor/*/*/*.png
%{_datadir}/epiphany/icons/hicolor/*/*/*.svg
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/epilicious.schemas
%{_sysconfdir}/gconf/schemas/smart-bookmarks.schemas
