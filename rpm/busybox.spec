Summary: Single binary providing simplified versions of system commands
Name: busybox
Version: 1.31.0
Release: 1
License: GPLv2
Source0: http://www.busybox.net/downloads/%{name}-%{version}.tar.bz2
Source1: rpm/udhcpd.service
Source2: busybox-static.config
Source3: busybox-sailfish.config
Patch0:  0001-Copy-extended-attributes-if-p-flag-is-provided-to-cp.patch
Patch1:  0002-applets-Busybox-in-usr-bin-instead-of-bin.patch
URL: https://git.sailfishos.org/mer-core/busybox
BuildRequires: glibc-static
BuildRequires: libselinux-static libsepol-static
BuildRequires: pcre-static

Obsoletes: time <= 1.7
Provides: time > 1.7

# Providing only part of iputils, but should be enough for us. 
Obsoletes: iputils <= 20101006
Provides: iputils > 20101006

%define debug_package %{nil}

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes: %{name}-docs

%description doc
Busybox user guide.

%package static
Summary: Statically linked version of busybox

%description static
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This package provides
a statically linked version of Busybox.

%package symlinks-dosfstools
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacements for dosfstools

%description symlinks-dosfstools
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This
is the symlinks implementing part of dosfstools.

%package symlinks-gzip
Requires: %{name} = %{version}-%{release}
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
Summary: Busybox dhcp utilities

%description symlinks-dhcp
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This contains
the symlinks implementing the dhcp utilities (udhcpc/udhcpcd).

%package symlinks-diffutils
Requires: %{name} = %{version}-%{release}
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
Summary: Busybox replacements for grep
Provides: grep = %{version}
Provides: /bin/grep
Conflicts: gnu-grep

%description symlinks-grep
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This
is the symlinks implementing grep, egrep and fgrep replacements.

%package symlinks-cpio
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacements for cpio
Provides: cpio
Conflicts: gnu-cpio

%description symlinks-cpio
Busybox is a single binary which includes versions of a large number
of system commands, including a shell. This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This contains
the symlinks implementing cpio replacements.

%package symlinks-tar
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacements for tar
Provides: tar = %{version}
Conflicts: gnu-tar

%description symlinks-tar
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This
is the symlink implementing tar replacement.

%package symlinks-which
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacements for which
Provides: which = %{version}
Conflicts: util-linux <= 2.33+git1

%description symlinks-which
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.  This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This
is the symlink implementing which replacement.

%prep
%setup -q -n %{name}-%{version}/upstream
%patch0 -p1
%patch1 -p1

%build
# TODO: This config should be synced with the dynamic config at some point
# currently the features differ quite a bit
cp %{SOURCE2} .config
yes "" | make oldconfig
make %{?_smp_mflags}
cp busybox busybox-static

# clean any leftovers from static build
make clean
make distclean

# Build dynamic version
cp %{SOURCE3} .config

yes "" | make oldconfig
make %{_smp_mflags}
make busybox.links
# /bin links are legacy, use /usr/bin whenever you can
cat >> busybox.links << EOF
/bin/busybox
%{_bindir}/ping
%{_bindir}/ping6
%{_sbindir}/mkdosfs
%{_sbindir}/mkfs.vfat
%{_bindir}/gzip
%{_bindir}/gunzip
%{_bindir}/zcat
%{_sbindir}/udhcpc
/bin/find
%{_bindir}/grep
%{_bindir}/egrep
%{_bindir}/fgrep
%{_bindir}/cpio
%{_bindir}/tar
EOF

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}/usr/bin
install -m 755 busybox %{buildroot}/usr/bin/busybox
install -m 644 -D %{SOURCE1} %{buildroot}/lib/systemd/system/udhcpd.service
applets/install.sh %{buildroot} --symlinks
rm -f %{buildroot}/sbin/udhcpc

install -m 755 busybox-static %{buildroot}/usr/bin/busybox-static
ln -s ../usr/bin/busybox-static %{buildroot}/bin/busybox-static
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 644 -t %{buildroot}/%{_docdir}/%{name}-%{version} \
        docs/BusyBox.html docs/BusyBox.txt

%files
%defattr(-,root,root,-)
%license LICENSE
/bin/busybox
%{_bindir}/busybox
/bin/ping
%{_bindir}/ping
/bin/ping6
%{_bindir}/ping6
%{_bindir}/time
%{_bindir}/traceroute
%{_bindir}/traceroute6
%{_sbindir}/arping

%files static
%defattr(-,root,root,-)
/bin/busybox-static
%{_bindir}/busybox-static

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}

%files symlinks-dosfstools
%defattr(-,root,root,-)
/sbin/mkdosfs
%{_sbindir}/mkdosfs
/sbin/mkfs.vfat
%{_sbindir}/mkfs.vfat

%files symlinks-gzip
%defattr(-,root,root,-)
/bin/gunzip
%{_bindir}/gunzip
/bin/gzip
%{_bindir}/gzip
/bin/zcat
%{_bindir}/zcat

%files symlinks-dhcp
%defattr(-,root,root,-)
%{_sbindir}/udhcpc
%{_sbindir}/udhcpd
/lib/systemd/system/udhcpd.service

%files symlinks-diffutils
%defattr(-,root,root,-)
%{_bindir}/diff
%{_bindir}/cmp

%files symlinks-findutils
%defattr(-,root,root,-)
/bin/find
%{_bindir}/find
%{_bindir}/xargs

%files symlinks-grep
%defattr(-,root,root,-)
/bin/grep
%{_bindir}/grep
/bin/egrep
%{_bindir}/egrep
/bin/fgrep
%{_bindir}/fgrep

%files symlinks-cpio
%defattr(-,root,root,-)
/bin/cpio
%{_bindir}/cpio

%files symlinks-tar
%defattr(-,root,root,-)
/bin/tar
%{_bindir}/tar

%files symlinks-which
%defattr(-,root,root,-)
%{_bindir}/which
