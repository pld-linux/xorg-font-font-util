Summary:	BDF font utilities (bdftruncate, ucs2any)
Summary(pl.UTF-8):	Narzędzia do fontów BDF (bdftruncate, ucs2any)
Name:		xorg-font-font-util
Version:	1.3.3
Release:	1
License:	BSD
Group:		X11/Development/Tools
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-util-%{version}.tar.xz
# Source0-md5:	d92913afdcd8ac008225a8bd06488702
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Obsoletes:	X11-fonts-utils < 1:7.0.0
Obsoletes:	XFree86-fonts-utils < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org font package creation/installation utilities:
- bdftruncate generates truncated BDF font from ISO 10646-1-encoded
  BDF font
- ucs2any generates BDF fonts containing subsets of ISO 10646-1
  codepoints

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/bdftruncate
%attr(755,root,root) %{_bindir}/ucs2any
%{_fontsdir}/util
%{_mandir}/man1/bdftruncate.1*
%{_mandir}/man1/ucs2any.1*
%{_aclocaldir}/fontutil.m4
%{_pkgconfigdir}/fontutil.pc
