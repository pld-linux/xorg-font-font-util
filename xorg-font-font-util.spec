Summary:	BDF font utilities (bdftruncate, ucs2any)
Summary(pl.UTF-8):	Narzędzia do fontów BDF (bdftruncate, ucs2any)
Name:		xorg-font-font-util
Version:	1.1.0
Release:	1
License:	BSD
Group:		X11/Development/Tools
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-util-%{version}.tar.bz2
# Source0-md5:	9538043de60d685fc4253b0dc2924d58
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	X11-fonts-utils < 1:7.0.0
Obsoletes:	XFree86-fonts-utils < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BDF font utilities:
- bdftruncate generates truncated BDF font from ISO 10646-1-encoded
  BDF font
- ucs2any generates BDF fonts containing subsets of ISO 10646-1 codepoints

%description -l pl.UTF-8
Narzędzia do fontów BDF:
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
