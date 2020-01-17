%define name		CharLS
%define gzname		charls
%define major		2
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:           %{name}
Version:        2.1.0
Release:        1
License:        BSD
Summary:        A JPEG-LS library
Url:            https://github.com/team-charls/charls
Group:          System/Libraries
Source0:        https://github.com/team-charls/charls/archive/%{gzname}-%{version}.tar.gz

BuildRequires:	cmake

%description
An optimized implementation of the JPEG-LS standard for lossless and
near-lossless image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

%package -n %{develname}
Summary:        Libraries and headers for CharLS
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:	CharLS-devel

%description -n %{develname}
This package contains libraries and headers for CharLS.

%package -n %{libname}
Summary:        A JPEG-LS library
Group:          System/Libraries

%description -n %{libname}
An optimized implementation of the JPEG-LS standard for lossless and
near-lossless image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

%prep
%setup -n %{gzname}-%{version}

%build
%cmake \
 -Dcharls_BUILD_SHARED_LIBS=ON \
 -DBUILD_TESTING=ON \
 -DCMAKE_BUILD_TYPE=release
%make VERBOSE=1

%install
pushd build
%makeinstall_std
popd

%check
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:.
ctest .

%files -n %{develname}
%doc LICENSE.md README.md SECURITY.md
%{_includedir}/charls/
%{_libdir}/*.so

%files -n %{libname}
%{_libdir}/libcharls.so.%{major}*


