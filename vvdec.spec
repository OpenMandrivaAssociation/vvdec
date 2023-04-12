Name:           vvdec
Version:        1.6.0
Release:        0
Summary:        Fraunhofer Versatile Video Decoder (VVdeC)
License:        BSD-3-Clause-Clear
URL:            https://www.hhi.fraunhofer.de/en/departments/vca/technologies-and-solutions/h266-vvc.html
Source:         https://github.com/fraunhoferhhi/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.13

%description
A fast and efficient H.266/VVC decoder implementation.

%package -n %{lname}
Summary:        Fraunhofer Versatile Video Decoder (VVdeC)
Group:          System/Libraries

%description -n %{lname}
A fast and efficient H.266/VVC decoder implementation.

This package contains a library that can other apps use to utilize the
decoding capabilities.

%package devel
Summary:        Fraunhofer Versatile Video Decoder (VVdeC)
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
A fast and efficient H.266/VVC decoder implementation.

This package contains the development files.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_SKIP_RPATH=YES
%cmake_build

%install
%cmake_install

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/vvdecapp

%files -n %{lname}
%{_libdir}/*.so

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{lname}.pc
%{_libdir}/cmake/%{name}/
