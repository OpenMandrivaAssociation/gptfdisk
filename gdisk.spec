%define name	gdisk
%define version 0.8.1
%define release	1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	An fdisk-like partitioning tool for GPT disks
License:	GPLv2
Group:		System/Configuration/Hardware
URL:		http://www.rodsbooks.com/gdisk
Source0:	http://www.rodsbooks.com/%{name}/gptfdisk-%{version}.tar.gz

BuildRequires:	icu-devel
Buildrequires: 	pkgconfig(uuid)
Buildrequires: 	popt-devel
BuildRequires:	ncurses-devel

%description
An fdisk-like partitioning tool for GPT disks. GPT
fdisk features a command-line interface, fairly direct
manipulation of partition table structures, recovery
tools to help you deal with corrupt partition tables,
and the ability to convert MBR disks to GPT format.


%prep
%setup -q -n gptfdisk-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_CXX_FLAGS" make

%install
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
install -Dp -m0755 gdisk $RPM_BUILD_ROOT/%{_sbindir}
install -Dp -m0755 sgdisk $RPM_BUILD_ROOT/%{_sbindir}
install -Dp -m0644 gdisk.8 $RPM_BUILD_ROOT/%{_mandir}/man8/gdisk.8
install -Dp -m0644 sgdisk.8 $RPM_BUILD_ROOT/%{_mandir}/man8/sgdisk.8

%files
%doc NEWS COPYING README
%{_sbindir}/gdisk
%{_sbindir}/sgdisk
%doc %{_mandir}/man8/*
