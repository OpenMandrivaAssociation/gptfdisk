Name:		gdisk
Version:	0.8.1
Release:	2
Summary:	An fdisk-like partitioning tool for GPT disks
License:	GPLv2
Group:		System/Configuration/Hardware
URL:		http://www.rodsbooks.com/gdisk
Source0:	http://www.rodsbooks.com/%{name}/gptfdisk-%{version}.tar.gz
Patch0:		gptfdisk-0.8.1-gcc4.7.patch
BuildRequires:	icu-devel
Buildrequires:	pkgconfig(uuid)
Buildrequires:	popt-devel
BuildRequires:	pkgconfig(ncurses)

%description
An fdisk-like partitioning tool for GPT disks. GPT
fdisk features a command-line interface, fairly direct
manipulation of partition table structures, recovery
tools to help you deal with corrupt partition tables,
and the ability to convert MBR disks to GPT format.


%prep
%setup -q -n gptfdisk-%{version}
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_CXX_FLAGS" make

%install
mkdir -p %{buildroot}%{_sbindir}
install -Dp -m0755 gdisk %{buildroot}%{_sbindir}
install -Dp -m0755 sgdisk %{buildroot}%{_sbindir}
install -Dp -m0644 gdisk.8 %{buildroot}%{_mandir}/man8/gdisk.8
install -Dp -m0644 sgdisk.8 %{buildroot}%{_mandir}/man8/sgdisk.8

%files
%doc NEWS COPYING README
%{_sbindir}/gdisk
%{_sbindir}/sgdisk
%doc %{_mandir}/man8/*


%changelog
* Fri Apr 20 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.8.1-1
+ Revision: 792468
- imported package gdisk

