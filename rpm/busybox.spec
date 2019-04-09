Summary: Single binary providing simplified versions of system commands
Name: busybox
Version: 1.29.3
Release: 1
License: GPLv2
Group: System/Shells
Source0: http://www.busybox.net/downloads/%{name}-%{version}.tar.bz2
Source1: rpm/udhcpd.service
Source2: busybox-static.config
Source3: busybox-sailfish.config
Patch0:  0001-Copy-extended-attributes-if-p-flag-is-provided-to-cp.patch
URL: https://github.com/mer-packages/busybox 

Obsoletes: time <= 1.7
Provides: time > 1.7

# Providing only part of iputils, but should be enough for us. 
Obsoletes: iputils <= 20101006
Provides: iputils > 20101006

BuildRequires: glibc-static

%define debug_package %{nil}

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
Busybox user guide.

%package static
Group: System Environment/Shells
Summary: Statically linked version of busybox

%description static
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This package provides
a statically linked version of Busybox.

%package symlinks-dosfstools
Requires: %{name} = %{version}-%{release}
Group: System/Shells
Summary: Busybox replacements for dosfstools

%description symlinks-dosfstools
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This
is the symlinks implementing part of dosfstools.

%package symlinks-gzip
Requires: %{name} = %{version}-%{release}
Group: System/Shells
Summary: Busybox replacements for gzip
Provides: gzip = %{version}
Obsoletes: gzip <= 1.5

%description symlinks-gzip
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This
is the symlinks implementing gzip replacements.

%package symlinks-dhcp
Requires: %{name} = %{version}-%{release}
Group: System/Shells
Summary: Busybox dhcp utilities

%description symlinks-dhcp
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This contains
the symlinks implementing the dhcp utilities (udhcpc/udhcpcd).

%package symlinks-diffutils
Requires: %{name} = %{version}-%{release}
Group: System/Shells
Summary: Busybox replacements for diffutils
Provides: diffutils = %{version}
Conflicts: gnu-diffutils

%description symlinks-diffutils
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This
is the symlinks implementing part of diffutils replacements.

%package symlinks-findutils
Requires: %{name} = %{version}-%{release}
Group: System/Shells
Summary: Busybox replacements for findutils
Provides: findutils = %{version}
Conflicts: gnu-findutils

%description symlinks-findutils
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This
is the symlinks implementing findutils replacements.

%package symlinks-grep
Requires: %{name} = %{version}-%{release}
Group: System/Shells
Summary: Busybox replacements for grep
Provides: grep = %{version}
Conflicts: gnu-grep

%description symlinks-grep
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This
is the symlinks implementing grep, egrep and fgrep replacements.

%prep
%setup -q -n %{name}-%{version}/upstream
%patch0 -p1

%build
# TODO: This config should be synced with the dynamic config at some point
# currently the features differ quite a bit
cp %{SOURCE2} .config
yes "" | make oldconfig
make %{?jobs:-j%jobs}
cp busybox busybox-static

# clean any leftovers from static build
make clean
make distclean

# Build dynamic version
cp %{SOURCE3} .config
yes "" | make oldconfig
make %{_smp_mflags}
make busybox.links
cat >> busybox.links << EOF
/usr/bin/gzip
/usr/bin/gunzip
/usr/sbin/udhcpc
/bin/find
EOF

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/bin
install -m 755 busybox %{buildroot}/bin/busybox
install -m 644 -D %{SOURCE1} %{buildroot}/lib/systemd/system/udhcpd.service
applets/install.sh %{buildroot} --symlinks
rm -f %{buildroot}/sbin/udhcpc

install -m 755 busybox-static %{buildroot}/bin/busybox-static
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 644 -t %{buildroot}/%{_docdir}/%{name}-%{version} \
	docs/BusyBox.html docs/BusyBox.txt

%files
%defattr(-,root,root,-)
%license LICENSE
/bin/busybox
/bin/ping
/bin/ping6
/usr/bin/time
/usr/bin/traceroute
/usr/bin/traceroute6
/usr/sbin/arping

%files static
%defattr(-,root,root,-)
/bin/busybox-static

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}

%files symlinks-dosfstools
%defattr(-,root,root,-)
/sbin/mkdosfs
/sbin/mkfs.vfat

%files symlinks-gzip
%defattr(-,root,root,-)
/bin/gunzip
/usr/bin/gunzip
/bin/gzip
/usr/bin/gzip
/bin/zcat

%files symlinks-dhcp
%defattr(-,root,root,-)
/usr/sbin/udhcpc
/usr/sbin/udhcpd
/lib/systemd/system/udhcpd.service

%files symlinks-diffutils
%defattr(-,root,root,-)
/usr/bin/diff
/usr/bin/cmp

%files symlinks-findutils
%defattr(-,root,root,-)
/bin/find
/usr/bin/find
/usr/bin/xargs

%files symlinks-grep
%defattr(-,root,root,-)
/bin/grep
/bin/egrep
/bin/fgrep
