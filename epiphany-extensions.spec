%define		basever	2.26
Summary:	Collection of extensions for Epiphany
Summary(pl.UTF-8):	Zbiór rozszerzeń dla Epiphany
Name:		epiphany-extensions
Version:	2.26.1
Release:	5
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/epiphany-extensions/2.26/%{name}-%{version}.tar.bz2
# Source0-md5:	bc3044148e915312654f8c82a575e58e
Patch0:		%{name}-libxul.patch
URL:		http://www.gnome.org/projects/epiphany/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	epiphany-devel >= 2.26.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	opensp-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-devel >= 2.22.0
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	sed >= 4.0
BuildRequires:	xulrunner-devel >= 1.9-5
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
%requires_eq_to	epiphany epiphany-devel
%requires_eq_to	xulrunner xulrunner-devel
Provides:	epiphany-plugins
Obsoletes:	epiphany-plugins <= 0.1.2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# can be provided by mozilla or mozilla-embedded
%define		_noautoreqdep	libgtkembedmoz.so libgtksuperwin.so libxpcom.so
%define		_noautoreq	libxpcom.so

%description
Epiphany Extensions is a collection of extensions for Epiphany.

%description -l pl.UTF-8
Epiphany Extensions jest zbiorem rozszerzeń dla Epiphany.

%prep
%setup -q
%patch0 -p1

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

%find_lang %{name} --with-gnome --with-omf --all-name

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

%files -f %{name}.lang
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
%{_sysconfdir}/gconf/schemas/epilicious.schemas
%{_sysconfdir}/gconf/schemas/smart-bookmarks.schemas
