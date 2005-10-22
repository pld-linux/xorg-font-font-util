Summary:	Font utilities
Summary(pl):	Narzêdzia do czcionek
Name:		xorg-font-font-util
Version:	0.99.1
Release:	0.1
License:	BSD
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/font/font-util-%{version}.tar.bz2
# Source0-md5:	006214458f6f419b12bcd7590c5e4b66
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
	appmandir=%{_mandir}/man1 \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/*
%{_fontsdir}/util
%{_mandir}/man1/*.1x*
%{_pkgconfigdir}/fontutil.pc
