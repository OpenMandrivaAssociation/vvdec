%define libname %mklibname vvdec
%define devname %mklibname -d vvdec

Name:           vvdec
Version:        1.6.1
Release:        1
Summary:        Fraunhofer Versatile Video Decoder (VVdeC)
License:        BSD-3-Clause-Clear
URL:            https://www.hhi.fraunhofer.de/en/departments/vca/technologies-and-solutions/h266-vvc.html
Source:         https://github.com/fraunhoferhhi/vvdec/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake

%description
A fast and efficient H.266/VVC decoder implementation.

%package -n %{libname}
Summary:        Fraunhofer Versatile Video Decoder (VVdeC)
Group:          System/Libraries

%description -n %{libname}
A fast and efficient H.266/VVC decoder implementation.

This package contains a library that can other apps use to utilize the
decoding capabilities.

%package -n %{devname}
Summary:        Fraunhofer Versatile Video Decoder (VVdeC)
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description -n %{devname}
A fast and efficient H.266/VVC decoder implementation.

This package contains the development files.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_SKIP_RPATH=YES
%make_build

%install
%make_install -C build

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/vvdecapp

%files -n %{libname}
%{_libdir}/*.so

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{lname}.pc
%{_libdir}/cmake/%{name}/
