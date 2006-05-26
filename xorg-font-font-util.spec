Summary:	Font utilities
Summary(pl):	Narzêdzia do czcionek
Name:		xorg-font-font-util
Version:	1.0.1
Release:	1
License:	BSD
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-util-%{version}.tar.bz2
# Source0-md5:	b81535f78fe05732931f02841e5ca37b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	X11-fonts-utils
Obsoletes:	XFree86-fonts-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Font utilities.

%description -l pl
Narzêdzia do czcionek.

%prep
%setup -q -n font-util-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-mapdir=%{_fontsdir}/util

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/bdftruncate
%attr(755,root,root) %{_bindir}/ucs2any
%{_fontsdir}/util
%{_mandir}/man1/bdftruncate.1x*
%{_mandir}/man1/ucs2any.1x*
%{_aclocaldir}/fontutil.m4
%{_pkgconfigdir}/fontutil.pc
