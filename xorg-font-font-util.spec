Summary:	Font utilities
Summary(pl):	Narzêdzia do czcionek
Name:		xorg-font-font-util
Version:	0.99.2
Release:	0.1
License:	BSD
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/font/font-util-%{version}.tar.bz2
# Source0-md5:	035da3fb58569c21fafc855d0dd3b906
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
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
