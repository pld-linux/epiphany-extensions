Summary:	Collection of extensions for Epiphany
Summary(pl):	Zbi�r rozszerze� dla Epiphany
Name:		epiphany-extensions
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	e8c38a481b8d3b4a70fa1016dbffe7cf
Patch0:		%{name}-locale-names.patch
URL:		http://epiphany.mozdev.org/
BuildRequires:	autoconf
Buildrequires:	automake
BuildRequires:	epiphany-devel >= 1.1.8
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel >= 2.3.2
BuildRequires:	intltool >= 0.29
BuildRequires:	libglade2-devel >= 2.3.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.0
Requires:	epiphany >= 1.1.8
Obsoletes:	epiphany-plugins <= 0.1.2
Provides:	epiphany-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Epiphany Extensions is a collection of extensions for Epiphany.

%description -l pl
Epiphany Extensions jest zbiorem rozszerze� dla Epiphany.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal} -I %{_aclocaldir}/gnome2-macros
%{__autoconf}
%{__automake}
%configure \
	--with-extensions=all

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}-1.0

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-1.0.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/epiphany/extensions/*.so*
%{_libdir}/epiphany/extensions/*.la
%{_datadir}/%{name}