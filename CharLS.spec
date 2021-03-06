%define name		CharLS
%define gzname		charls
%define major		1
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} %{major} -d

Name:           %{name}
Version:        1.1.0
Release:        1
License:        BSD
Summary:        A JPEG-LS library
Url:            https://github.com/team-charls/charls
Group:          System/Libraries
Source0:        https://github.com/team-charls/%{gzname}/releases/tag/%{gzname}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE charls_add_cmake_install_target.patch asterios.dramis@gmail.com -- Add a cmake install target for CharLS header files
#Patch0:         CharLS-1.0-suse-add_cmake_install_target.patch
# PATCH-FIX-OPENSUSE charls_add_sharedlib_soname.patch asterios.dramis@gmail.com -- Add soname to generated shared lib and install libCharLS.so
#Patch1:         CharLS-1.0-suse-add_sharedlib_soname.patch
# PATCH-FIX-OPENSUSE charls_fix_tests.patch asterios.dramis@gmail.com -- Fix tests
#Patch2:         CharLS-1.0-suse-fix_tests.patch
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
Provides:	CharLS-devel%{major}

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
#dos2unix *.h *.c* *.txt
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

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
%doc README.md
%{_includedir}/CharLS/
%{_libdir}/*.so

%files -n %{libname}
%{_libdir}/libCharLS.so.%{major}*


%changelog
* Tue Jan 10 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.0-2
+ Revision: 759512
- fixed mistake in previous commit
- release bump
- add provides foe -devel package
- BR cmake
- imported package CharLS

