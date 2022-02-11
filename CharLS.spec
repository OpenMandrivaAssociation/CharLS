%define major		2
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} %{major} -d

%define lname		%(echo %name | tr [:upper:] [:lower:])

Summary:        A C++ JPEG-LS library implementation
Name:           CharLS
Version:        2.0.0
Release:        1
License:        BSD
Url:            https://github.com/team-charls/charls
Group:          System/Libraries
Source0:        https://github.com/team-charls/%{lname}/archive/%{version}/%{lname}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja

%description
An optimized implementation of the JPEG-LS standard for lossless and
near-lossless image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

#---------------------------------------------------------------------------

%package -n %{develname}
Summary:        Libraries and headers for CharLS
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:	CharLS-devel%{major}

%description -n %{develname}
This package contains libraries and headers for CharLS.

%files -n %{develname}
%doc README.md
%{_includedir}/CharLS/
%{_libdir}/*.so

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:        A JPEG-LS library
Group:          System/Libraries

%description -n %{libname}
An optimized implementation of the JPEG-LS standard for lossless and
near-lossless image compression. JPEG-LS is a low-complexity standard that
matches JPEG 2000 compression ratios. In terms of speed, CharLS outperforms
open source and commercial JPEG LS implementations.

%files -n %{libname}
%{_libdir}/libCharLS.so.%{major}*

#---------------------------------------------------------------------------

%prep
%autosetup -n %{lname}-%{version}
rm CharLS*.sln* -v

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DBUILD_TESTING:BOOL=ON \
	-G Ninja
%ninja_build	

%install
%ninja_install -C build

%check
pushd build
# Enter a key + enter to finish
echo "a" | ./charlstest
popd
