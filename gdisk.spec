Summary:	An fdisk-like partitioning tool for GPT disks
Name:		gdisk
Version:	0.8.10
Release:	1
License:	GPLv2+
Group:		System/Configuration/Hardware
Url:		http://www.rodsbooks.com/gdisk
Source0:	http://www.rodsbooks.com/%{name}/gptfdisk-%{version}.tar.gz
BuildRequires:	pkgconfig(icu-io)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(ncursesw)
Buildrequires:	pkgconfig(popt)
Buildrequires:	pkgconfig(uuid)

%description
An fdisk-like partitioning tool for GPT disks. GPT
fdisk features a command-line interface, fairly direct
manipulation of partition table structures, recovery
tools to help you deal with corrupt partition tables,
and the ability to convert MBR disks to GPT format.

%files
%doc NEWS COPYING README
%{_sbindir}/gdisk
%{_sbindir}/sgdisk
%doc %{_mandir}/man8/*

#----------------------------------------------------------------------------

%prep
%setup -qn gptfdisk-%{version}

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" %make

%install
mkdir -p %{buildroot}%{_sbindir}
install -Dp -m0755 gdisk %{buildroot}%{_sbindir}
install -Dp -m0755 sgdisk %{buildroot}%{_sbindir}
install -Dp -m0644 gdisk.8 %{buildroot}%{_mandir}/man8/gdisk.8
install -Dp -m0644 sgdisk.8 %{buildroot}%{_mandir}/man8/sgdisk.8


