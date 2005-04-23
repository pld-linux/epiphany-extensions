Summary:	Collection of extensions for Epiphany
Summary(pl):	Zbi�r rozszerze� dla Epiphany
Name:		epiphany-extensions
Version:	1.6.3
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/gnome/sources/epiphany-extensions/1.6/%{name}-%{version}.tar.bz2
# Source0-md5:	9e2573dcf57b7313160b19de878f0939
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}-mozilla_includes.patch
URL:		http://www.gnome.org/projects/epiphany/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	epiphany-devel >= 1.6.2
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gtk+2-devel >= 2:2.6.4
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	mozilla-devel >= 5:1.7
BuildRequires:	opensp-devel
BuildRequires:	pkgconfig
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
Epiphany Extensions jest zbiorem rozszerze� dla Epiphany.

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

%find_lang %{name}-1.6

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-1.6.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/epiphany-*/extensions/*.so*
%{_libdir}/epiphany-*/extensions/*.xml
%{_datadir}/%{name}
