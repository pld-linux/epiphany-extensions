%define		minmozver	5:1.7
Summary:	Collection of extensions for Epiphany
Summary(pl):	Zbiór rozszerzeñ dla Epiphany
Name:		epiphany-extensions
Version:	1.4.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/1.4/%{name}-%{version}.tar.bz2
# Source0-md5:	4ae247cd350feb8e959ed63e22853f83
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-mozilla_includes.patch
URL:		http://www.gnome.org/projects/epiphany/
BuildRequires:	autoconf >= 2.57
Buildrequires:	automake
BuildRequires:	epiphany-devel >= 1.4.1
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	intltool >= 0.29
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.11
BuildRequires:	mozilla-devel >= %{minmozver}
BuildRequires:	opensp-devel
Requires:	epiphany = %(rpm -q --qf '%{EPOCH}:%{VERSION}' epiphany-devel)
Requires:	mozilla-embedded = %(rpm -q --qf '%{EPOCH}:%{VERSION}' --whatprovides mozilla-embedded)
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
%patch0 -p1
%patch1 -p1

mv po/{no,nb}.po

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-extensions=all

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/epiphany-*/extensions/*.la

%find_lang %{name}-1.4

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-1.4.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/epiphany-*/extensions/*.so*
%{_datadir}/%{name}
