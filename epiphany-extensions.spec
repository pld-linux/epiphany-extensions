Summary:	Collection of extensions for Epiphany
Summary(pl):	Zbiór rozszerzeñ dla Epiphany
Name:		epiphany-extensions
Version:	0.6
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	eb28e6834aad362da1ae07e76ed153f6
URL:		http://epiphany.mozdev.org/
BuildRequires:	epiphany-devel >= 1.1.2
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libxml2-devel
Requires:	epiphany >= 1.1.2
Obsoletes:	epiphany-plugins <= 0.1.2
Provides:	epiphany-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Epiphany Extensions is a collection of extensions for Epiphany.

%description -l pl
Epiphany Extensions jest zbiorem rozszerzeñ dla Epiphany.

%prep
%setup -q

%build
%configure \
	--with-extensions=all
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/epiphany/extensions/*.so*
%{_libdir}/epiphany/extensions/*.la
%{_datadir}/%{name}
