Summary:	An fdisk-like partitioning tool for GPT disks
Name:		gptfdisk
Version:	1.0.7
Release:	1
License:	GPLv2+
Group:		System/Configuration/Hardware
Url:		http://www.rodsbooks.com/gdisk
Source0:	http://download.sourceforge.net/project/gptfdisk/gptfdisk/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(icu-io)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(uuid)
Provides:	gdisk = %{EVRD}
Provides:	gdisk = 1.0.0
Obsoletes:	gdisk < 1.0.0

%description
An fdisk-like partitioning tool for GPT disks. GPT
fdisk features a command-line interface, fairly direct
manipulation of partition table structures, recovery
tools to help you deal with corrupt partition tables,
and the ability to convert MBR disks to GPT format.

#----------------------------------------------------------------------------

%prep
%autosetup -n gptfdisk-%{version} -p1

%build
%setup_compile_flags
%make_build CC=%{__cc} CXX=%{__cxx}

%install
mkdir -p %{buildroot}%{_sbindir}
install -Dp -m0755 gdisk %{buildroot}%{_sbindir}
install -Dp -m0755 cgdisk %{buildroot}%{_sbindir}
install -Dp -m0755 sgdisk %{buildroot}%{_sbindir}
install -Dp -m0755 fixparts %{buildroot}%{_sbindir}
install -Dp -m0644 gdisk.8 %{buildroot}%{_mandir}/man8/gdisk.8
install -Dp -m0644 cgdisk.8 %{buildroot}%{_mandir}/man8/sgdisk.8
install -Dp -m0644 sgdisk.8 %{buildroot}%{_mandir}/man8/cgdisk.8
install -Dp -m0644 fixparts.8 %{buildroot}%{_mandir}/man8/fixparts.8

%files
%doc NEWS COPYING README
%{_sbindir}/gdisk
%{_sbindir}/cgdisk
%{_sbindir}/sgdisk
%{_sbindir}/fixparts
%doc %{_mandir}/man8/*
