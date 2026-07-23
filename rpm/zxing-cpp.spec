%if 0%{?sailfishos_version} < 50200
ExclusiveArch: none
%endif

Name:       zxing-cpp20
Summary:    ZXing port to C++ (2.0)
Version:    2.0.0+git1
Release:    1
License:    ASL 2.0
URL:        https://github.com/sailfishos/zxing
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.10

# Sailfishos 5.1 has 2.0, 5.2 has 3.x
Conflicts: zxing-cpp < 3.0.0
BuildRequires:  sailfish-version >= 5.2.0
Requires:       sailfish-version > 5.2.0

%package devel
Summary: Development files for the %{name} package
Requires: %{name} = %{version}-%{release}

# Sailfishos 5.1 has 2.0, 5.2 has 3.x
Conflicts: zxing-cpp-devel < 3.0.0
BuildRequires:  sailfish-version >= 5.2.0
Requires:       sailfish-version > 5.2.0

%description
ZXing-C++ ("zebra crossing") is an open-source, multi-format 1D/2D barcode image processing library implemented in C++.

%description devel
%{summary}.

%prep
%autosetup -n %{name}-%{version}/zxing-cpp

%build
%cmake -DBUILD_EXAMPLES=false
%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE
%{_libdir}/libZXing.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/ZXing/*
%{_libdir}/libZXing.so
%{_libdir}/pkgconfig/zxing.pc
%{_libdir}/cmake/ZXing/*.cmake
