
%define RELEASE 1.3.10.2
%define rel %{?CUSTOM_RELEASE}%{!?CUSTOM_RELEASE:%RELEASE}

Summary: OpenFabrics Alliance InfiniBand umad (user MAD) library
Name: libibumad
Version: 1.3.10.2
Release: %rel%{?dist}
License: GPLv2 or BSD
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source: http://www.openfabrics.org/downloads/management/libibumad-1.3.10.2.tar.gz
Url: http://openfabrics.org
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: libtool

%description
libibumad provides the user MAD library functions which sit on top of
the user MAD modules in the kernel. These are used by the IB diagnostic
and management tools, including OpenSM.

%package devel
Summary: Development files for the libibumad library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description devel
Development files for the libibumad library.

%package static
Summary: Static version of the libibumad library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description static
Static version of the libibumad library.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post devel -p /sbin/ldconfig
%postun devel -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libibumad*.so.*
%{_mandir}/man3/*
%doc AUTHORS COPYING ChangeLog

%files devel
%defattr(-,root,root)
%{_libdir}/libibumad.so
%{_includedir}/infiniband/*.h

%files static
%defattr(-,root,root)
%{_libdir}/libibumad.a
