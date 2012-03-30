%define		basever	3.4
Summary:	Collection of extensions for Epiphany
Summary(pl.UTF-8):	Zbiór rozszerzeń dla Epiphany
Name:		epiphany-extensions
Version:	3.4.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/epiphany-extensions/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	84eb15907ceb410030b00aacb6e5ff35
URL:		http://www.gnome.org/projects/epiphany/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-devel >= 0.34
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	docbook-dtd412-xml
BuildRequires:	epiphany-devel >= 3.4.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-webkit3-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	opensp-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.592
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	scrollkeeper
Requires:	epiphany >= 3.4.0
Provides:	epiphany-plugins
Obsoletes:	epiphany-plugins <= 0.1.2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
	--disable-silent-rules \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/epiphany/%{basever}/extensions/*.la

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%scrollkeeper_update_post

%postun
%glib_compile_schemas
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ui
%{_datadir}/glib-2.0/schemas/org.gnome.epiphanyextensions.gschema.xml
%{_datadir}/epiphany/icons

%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/libactionsextension.so
%{_libdir}/epiphany/%{basever}/extensions/actions.ephy-extension
%{_datadir}/%{name}/ui/action-properties.ui
%{_datadir}/%{name}/ui/actions-editor.ui

%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/libadblockextension.so
%{_libdir}/epiphany/%{basever}/extensions/adblock.ephy-extension
%{_datadir}/%{name}/ui/adblock.ui

%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/libautoreloadextension.so
%{_libdir}/epiphany/%{basever}/extensions/auto-reload.ephy-extension

%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/libextensionsmanageruiextension.so
%{_libdir}/epiphany/%{basever}/extensions/extensions-manager-ui.ephy-extension
%{_datadir}/%{name}/ui/extensions-manager-ui.ui

%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/libgesturesextension.so
%{_libdir}/epiphany/%{basever}/extensions/gestures.ephy-extension
%{_datadir}/%{name}/ephy-gestures.xml

%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/libgreasemonkeyextension.so
%{_libdir}/epiphany/%{basever}/extensions/greasemonkey.ephy-extension

%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/libhtml5tubeextension.so
%{_libdir}/epiphany/%{basever}/extensions/html5tube.ephy-extension

%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/libpushscrollerextension.so
%{_libdir}/epiphany/%{basever}/extensions/push-scroller.ephy-extension

%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/librssextension.so
%{_libdir}/epiphany/%{basever}/extensions/rss.ephy-extension
%{_datadir}/%{name}/ui/rss-ui.ui

%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/libsoupflyextension.so
%{_libdir}/epiphany/%{basever}/extensions/soup-fly.ephy-extension

%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/libtabkeytabnavigateextension.so
%{_libdir}/epiphany/%{basever}/extensions/tab-key-tab-navigate.ephy-extension

%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/libtabstatesextension.so
%{_libdir}/epiphany/%{basever}/extensions/tab-states.ephy-extension
