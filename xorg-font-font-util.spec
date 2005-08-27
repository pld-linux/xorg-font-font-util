Summary:	Font utilities
Summary(pl):	Narzêdzia do czcionek
Name:		xorg-font-font-util
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-util-%{version}.tar.bz2
# Source0-md5:	fecdf7a03dac02b8b103492f55537b32
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_datadir	/usr/share

%description
Font utilities.

%description -l pl
Narzêdzia do czcionek.

%prep
%setup -q -n font-util-%{version}

sed -i -e 's:^mapdir.*:mapdir=\"\$datadir/fonts/util\":g' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_fontsdir}/util
%{_mandir}/man1/*.1*
%{_pkgconfigdir}/fontutil.pc
