%ifnarch %{riscv}
# (tpg) optimize it a bit
%global optflags %{optflags} -Oz --rtlib=compiler-rt
%endif

Summary:	An fdisk-like partitioning tool for GPT disks
Name:		gptfdisk
Version:	1.0.9
Release:	4
License:	GPLv2+
Group:		System/Configuration/Hardware
Url:		http://www.rodsbooks.com/gdisk
Source0:	http://download.sourceforge.net/project/gptfdisk/gptfdisk/%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Fix-failure-crash-of-sgdisk-when-compiled-with-lates.patch
Patch1:		0002-Updated-guid.cc-to-deal-with-minor-change-in-libuuid.patch
Patch2:		0003-Updated-URLs-in-man-pages-to-HTTPS-rather-than-HTTP.patch
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(uuid)
Provides:	gdisk = %{EVRD}
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
%set_build_flags
%make_build CC=%{__cc} CXX=%{__cxx}

%install
for f in gdisk sgdisk cgdisk fixparts ; do 
    install -D -p -m 0755 $f %{buildroot}%{_sbindir}/$f
    install -D -p -m 0644 $f.8 %{buildroot}%{_mandir}/man8/$f.8
done

%files
%doc NEWS COPYING README
%{_sbindir}/gdisk
%{_sbindir}/cgdisk
%{_sbindir}/sgdisk
%{_sbindir}/fixparts
%doc %{_mandir}/man8/*
