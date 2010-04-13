%define		basever	2.28
Summary:	Collection of extensions for Epiphany
Summary(pl.UTF-8):	Zbiór rozszerzeń dla Epiphany
Name:		epiphany-extensions
Version:	2.30.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/epiphany-extensions/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	76dd4f6296a259d09554e693336187a2
URL:		http://www.gnome.org/projects/epiphany/
BuildRequires:	GConf2-devel >= 2.28.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	docbook-dtd412-xml
BuildRequires:	epiphany-devel >= 2.28.1
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel >= 2:2.16.0
BuildRequires:	gtk-webkit-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.28
BuildRequires:	opensp-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.198
Requires(post,postun):	scrollkeeper
%requires_eq_to	epiphany epiphany-devel
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
	--with-extensions=really-all \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany/%{basever}/extensions/*.la

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/epiphany/%{basever}/extensions/*.so*
%{_libdir}/epiphany/%{basever}/extensions/*.ephy-extension
%{_datadir}/%{name}
%{_datadir}/epiphany/icons/hicolor/*/*/*.png
%{_datadir}/epiphany/icons/hicolor/*/*/*.svg
