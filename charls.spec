%define major		2
%define libname		%mklibname %{name}
%define devname		%mklibname %{name} -d
%define oldlibname	%mklibname %{name} 2
%define olddevname	%mklibname %{name} 2 -d

Summary:        A C++ JPEG-LS library implementation
Name:           charls
Version:        2.4.2
Release:        2
License:        BSD
Group:          System/Libraries
Url:            https://github.com/team-charls/charls
Source0:        https://github.com/team-charls/charls/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja

%description
An optimized implementation of the JPEG-LS standard for lossless and
near-lossless image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	A JPEG-LS library
Group:		System/Libraries
# Intentionally unversioned, because libname should not contain version number
Obsoletes:	%{oldlibname}

%description -n %{libname}
An optimized implementation of the JPEG-LS standard for lossless and
near-lossless image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:        Libraries and headers for CharLS
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:	CharLS-devel
# Intentionally unversioned, because libname should not contain version number
Obsoletes:	%{olddevname}

%description -n %{devname}
This package contains libraries and headers for CharLS.

%files -n %{devname}
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

#---------------------------------------------------------------------------

%prep
%autosetup -p1
rm CharLS*.sln* -v

%build
%cmake \
	-DCHARLS_BUILD_SAMPLES:BOOL=ON \
	-DCHARLS_BUILD_TESTS:BOOL=ON \
	-DCHARLS_PEDANTIC_WARNINGS:BOOL=ON \
	-G Ninja
%ninja_build	

%install
%ninja_install -C build

%check
echo "a" | LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH %ninja test -C build

