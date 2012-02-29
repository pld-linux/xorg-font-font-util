Summary:	BDF font utilities (bdftruncate, ucs2any)
Summary(pl.UTF-8):	Narzędzia do fontów BDF (bdftruncate, ucs2any)
Name:		xorg-font-font-util
Version:	1.3.0
Release:	1
License:	BSD
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-util-%{version}.tar.bz2
# Source0-md5:	ddfc8a89d597651408369d940d03d06b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.8
Obsoletes:	X11-fonts-utils < 1:7.0.0
Obsoletes:	XFree86-fonts-utils < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org font package creation/installation utilities:
- bdftruncate generates truncated BDF font from ISO 10646-1-encoded
  BDF font
- ucs2any generates BDF fonts containing subsets of ISO 10646-1 codepoints

%description -l pl.UTF-8
Narzędzia do tworzenia i instalacji pakietów fontów X.org:
- bdftruncate generuje obcięte fonty BDF z fontów BDF w kodowaniu ISO
  10646-1
- ucs2any generuje fonty BDF zawierające podzbiory kodów ISO 10646-1

%prep
%setup -q -n font-util-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-mapdir=%{_fontsdir}/util \
	--with-fontrootdir=%{_fontsdir}

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/bdftruncate
%attr(755,root,root) %{_bindir}/ucs2any
%{_fontsdir}/util
%{_mandir}/man1/bdftruncate.1x*
%{_mandir}/man1/ucs2any.1x*
%{_aclocaldir}/fontutil.m4
%{_pkgconfigdir}/fontutil.pc
