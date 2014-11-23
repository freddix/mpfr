Summary:	Multiple-precision floating-point computations library
Name:		mpfr
Version:	3.1.2
Release:	4
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.mpfr.org/mpfr-current/%{name}-%{version}.tar.xz
# Source0-md5:	e3d203d188b8fe60bb6578dd3152e05c
# http://mpfr.loria.fr/mpfr-current/allpatches
Patch0:		allpatches
URL:		http://www.mpfr.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gmp-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MPFR library is a C library for multiple-precision floating-point
computations with exact rounding (also called correct rounding). It is
based on the GMP multiple-precision library. The main goal of MPFR is
to provide a library for multiple-precision floating-point computation
which is both efficient and has a well-defined semantics. It copies
the good ideas from the ANSI/IEEE-754 standard for double-precision
floating-point arithmetic (53-bit mantissa).

%package devel
Summary:	Header files for MPFR library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel

%description devel
Header files for MPFR library.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-static	\
	--enable-thread-safe	\
	--enable-shared
%{__make}

%check
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_infodir}/dir
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mpfr

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%post	devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO doc/FAQ.html
%attr(755,root,root) %ghost %{_libdir}/libmpfr.so.?
%attr(755,root,root) %{_libdir}/libmpfr.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpfr.so
%{_includedir}/mpfr.h
%{_includedir}/mpf2mpfr.h
%{_infodir}/mpfr.info*

