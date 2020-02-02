Summary:	libc++abi - C++ standard library support from LLVM project
Summary(pl.UTF-8):	libc++abi - wsparcie dla biblioteki standardowej C++ z projektu LLVM
Name:		llvm-libcxxabi
Version:	9.0.1
Release:	1
License:	MIT or BSD-like
Group:		Libraries
#Source0Download: https://github.com/llvm/llvm-project/releases/
Source0:	https://github.com/llvm/llvm-project/releases/download/llvmorg-%{version}/libcxxabi-%{version}.src.tar.xz
# Source0-md5:	1395b30a937e28779cd9707c6357b801
URL:		http://libcxxabi.llvm.org/
BuildRequires:	cmake >= 3.4.3
BuildRequires:	clang >= %{version}
%ifarch %{arm}
BuildRequires:	libunwind-devel
%endif
BuildRequires:	llvm-devel >= %{version}
BuildRequires:	llvm-libcxx-devel >= 3.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libc++abi is a new implementation of low level support for a standard
C++ library.

%description -l pl.UTF-8
libc++abi to nowa implementacja niskopoziomowego wsparcia dla
biblioteki standardowej C++.

%package devel
Summary:	Development files for LLVM libc++abi library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki LLVM libc++abi
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for LLVM libc++abi library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki LLVM libc++abi.

%package static
Summary:	Static LLVM libc++abi library
Summary(pl.UTF-8):	Statyczna biblioteka LLVM libc++abi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LLVM libc++abi library.

%description static -l pl.UTF-8
Statyczna biblioteka LLVM libc++abi.

%prep
%setup -q -n libcxxabi-%{version}.src

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_C_COMPILER="clang" \
	-DCMAKE_CXX_COMPILER="clang++"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}/libcxxabi
cp -p include/*.h $RPM_BUILD_ROOT%{_includedir}/libcxxabi

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS.TXT LICENSE.TXT
%attr(755,root,root) %{_libdir}/libc++abi.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libc++abi.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libc++abi.so
%{_includedir}/libcxxabi

%files static
%defattr(644,root,root,755)
%{_libdir}/libc++abi.a
