Summary: Single binary providing simplified versions of system commands
Name: busybox
Version: 1.36.1
Release: 1
License: GPLv2
Source0: http://www.busybox.net/downloads/%{name}-%{version}.tar.bz2
Source1: rpm/udhcpd.service
Source2: busybox-static.config
Source3: busybox-sailfish.config
Source4: set_ps1.sh
Patch0:  0001-Copy-extended-attributes-if-p-flag-is-provided-to-cp.patch
Patch1:  0002-applets-Busybox-in-usr-bin-instead-of-bin.patch
Patch2:  0003-Align-watch-with-what-is-in-procps-ng.patch
Patch3:  0004-ash-Load-ENV-file-also-if-SSH_CLIENT-SSH2_CLIENT-is-.patch
Patch4:  0005-ash-job-option-to-restore-term-io-after-job-is-stopp.patch
Patch5:  0006-ash-Write-history-on-SIGHUP.patch
Patch6:  0007-shell-fix-SIGWINCH-and-SIGCHLD-in-hush-interrupting-.patch
Patch7:  0008-ash-disable-sleep-as-builtin-closes-15619.patch

URL: https://github.com/sailfishos/busybox
BuildRequires: glibc-static
BuildRequires: libselinux-static libsepol-static
BuildRequires: pcre-static
BuildRequires: pkgconfig(systemd)
BuildRequires: sed

Obsoletes: time <= 1.7
Provides: time > 1.7

# Providing only part of iputils, but should be enough for us. 
Obsoletes: iputils <= 20101006
Provides: iputils > 20101006

Obsoletes: busybox-symlinks-cpio <= 1.33.1+git2

%define debug_package %{nil}

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description doc
Busybox user guide.

%package static
Summary: Statically linked version of busybox

%description static
Busybox is a single binary which includes versions of a large number
of system commands, including a shell. This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This package
provides a statically linked version of Busybox.

%package symlinks-bash
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacement for bash
Conflicts: gnu-bash
Obsoletes: bash < 1:3.2.57+git1
Provides: bash = 1:3.2.57+git1

%description symlinks-bash
%{summary} as symlinks. Provides ash with sh and bash symlinks as
a mostly compatible alternative to GNU Bash.

%package symlinks-bc
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacement for bc
Conflicts: bc <= 1.06.95
Obsoletes: bc <= 1.06.95
Provides: bc = 1.06.95-1

%description symlinks-bc
%{summary} as symlinks. Provides bc and dc symlinks as
a mostly compatible alternative to GNU Bc.

%package symlinks-coreutils
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacements for coreutils
Conflicts: gnu-coreutils
Provides: coreutils = 1:6.9+git1
Obsoletes: coreutils < 1:6.9+git1
Provides: mktemp

%description symlinks-coreutils
%{summary} as symlinks.

%package symlinks-dosfstools
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacements for dosfstools

%description symlinks-dosfstools
%{summary} as symlinks.

%package symlinks-gzip
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacement for gzip
Conflicts: gnu-gzip
Provides: gzip = 1.9+git1
Obsoletes: gzip < 1.9+git1

%description symlinks-gzip
%{summary} as symlinks.

%package symlinks-dhcp
Requires: %{name} = %{version}-%{release}
Summary: Busybox dhcp utilities

%description symlinks-dhcp
%{summary} as symlinks (udhcpc/udhcpcd).

%package symlinks-diffutils
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacements for diffutils
Conflicts: gnu-diffutils
Provides: diffutils = 2.8.1+git1
Obsoletes: diffutils < 2.8.1+git1

%description symlinks-diffutils
%{summary} as symlinks.

%package symlinks-findutils
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacements for findutils
Conflicts: gnu-findutils
Provides: findutils = 4.6.0+git2
Obsoletes: findutils < 4.6.0+git2

%description symlinks-findutils
%{summary} as symlinks.

%package symlinks-grep
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacement for grep
Conflicts: gnu-grep
Provides: grep = 1:2.5.1a+git1
Provides: /bin/grep
Obsoletes: grep < 1:2.5.1a+git1

%description symlinks-grep
%{summary} as symlinks (grep, egrep, fgrep).

%package symlinks-cpio
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacement for cpio
Provides: cpio
Conflicts: gnu-cpio

%description symlinks-cpio
%{summary} as symlinks.

%package symlinks-procps
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacement for procps
Provides: procps = 3.3.15+git2
Obsoletes: procps < 3.3.15+git2
Conflicts: procps-ng

%description symlinks-procps
%{summary} as symlinks.

%package symlinks-sed
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacement for sed
Provides: sed = 1:4.1.5+git1
Obsoletes: sed < 1:4.1.5+git1
Conflicts: gnu-sed

%description symlinks-sed
%{summary} as symlinks.

%package symlinks-tar
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacement for tar
Conflicts: gnu-tar
Provides: tar = 1.32+git2
Obsoletes: tar < 1.32+git2

%description symlinks-tar
%{summary} as symlinks.

%package symlinks-vi
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacement for vi
Provides: vi
Conflicts: vim-minimal

%description symlinks-vi
%{summary} as symlinks.

%package symlinks-which
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacement for which
Provides: which
Conflicts: util-linux <= 2.33+git1

%description symlinks-which
%{summary} as symlinks.

%package symlinks-console-tools
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacement for console tools
Provides: console-tools
Conflicts: ncurses
Obsoletes: ncurses < 6.1+git2

%description symlinks-console-tools
%{summary} as symlinks.

%package symlinks-psmisc
Requires: %{name} = %{version}-%{release}
Summary: Busybox replacement for psmisc
Provides: psmisc = 22.13+git1
Conflicts: psmisc-tools
Obsoletes: psmisc < 22.13+git1

%description symlinks-psmisc
%{summary} as symlinks.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
# TODO: This config should be synced with the dynamic config at some point
# currently the features differ quite a bit
cp %{SOURCE2} .config
yes "" | make oldconfig
%make_build CRYPT_AVAILABLE=n
cp busybox busybox-static

# clean any leftovers from static build
make clean
make distclean

# Build dynamic version
cp %{SOURCE3} .config

yes "" | make oldconfig
%make_build
make busybox.links
# /bin links are legacy, use /usr/bin whenever you can
cat >> busybox.links << EOF
/bin/busybox
%{_bindir}/ping
%{_bindir}/ping6
%{_sbindir}/mkdosfs
%{_sbindir}/mkfs.vfat
%{_sbindir}/sysctl
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
%{_bindir}/vi
/bin/basename
/bin/bc
/bin/dc
/bin/cut
/bin/env
/bin/sort
%{_bindir}/base32
%{_bindir}/base64
%{_bindir}/cat
%{_bindir}/chgrp
%{_bindir}/chmod
%{_bindir}/chown
%{_bindir}/cp
%{_bindir}/date
%{_bindir}/dd
%{_bindir}/df
%{_bindir}/echo
%{_bindir}/false
%{_bindir}/link
%{_bindir}/ln
%{_bindir}/ls
%{_bindir}/mkdir
%{_bindir}/mknod
%{_bindir}/mktemp
%{_bindir}/mv
%{_bindir}/nice
%{_bindir}/printenv
%{_bindir}/ps
%{_bindir}/pwd
%{_bindir}/realpath
%{_bindir}/rm
%{_bindir}/rmdir
%{_bindir}/sed
%{_bindir}/sleep
%{_bindir}/stat
%{_bindir}/stty
%{_bindir}/sync
%{_bindir}/touch
%{_bindir}/true
%{_bindir}/uname
%{_bindir}/clear
%{_bindir}/reset
%{_bindir}/sh
%{_bindir}/ash
%{_bindir}/bash
/sbin/fuser
/sbin/pidof
%{_bindir}/pidof
EOF

%install
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}/usr/bin
install -m 755 busybox %{buildroot}/usr/bin/busybox
install -m 644 -D %{SOURCE1} %{buildroot}%{_unitdir}/udhcpd.service
applets/install.sh %{buildroot} --symlinks
# Cleanup some symlinks
rm -f %{buildroot}/sbin/udhcpc
rm -f %{buildroot}/bin/base32
rm -f %{buildroot}/bin/base64

install -m 644 -D %{SOURCE4} %{buildroot}/%{_sysconfdir}/profile.d/set_ps1.sh

install -m 755 busybox-static %{buildroot}/usr/bin/busybox-static
ln -s ../usr/bin/busybox-static %{buildroot}/bin/busybox-static
mkdir -p %{buildroot}/%{_docdir}/%{name}-%{version}
install -m 644 -t %{buildroot}/%{_docdir}/%{name}-%{version} \
        docs/BusyBox.html docs/BusyBox.txt

rm -f %{buildroot}/bin/pidof

%files
%defattr(-,root,root,-)
%license LICENSE
/bin/busybox
%{_bindir}/busybox
/bin/ash
%{_bindir}/ash
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

%files symlinks-bash
%defattr(-,root,root,-)
/bin/bash
/bin/sh
%{_bindir}/bash
%{_bindir}/sh
%{_sysconfdir}/profile.d/set_ps1.sh

%files symlinks-bc
%defattr(-,root,root,-)
/bin/bc
/bin/dc
%{_bindir}/bc
%{_bindir}/dc

%files symlinks-coreutils
%defattr(-,root,root,-)
/bin/basename
/bin/cat
/bin/chgrp
/bin/chmod
/bin/chown
/bin/cp
/bin/cut
/bin/date
/bin/dd
/bin/df
/bin/echo
/bin/env
/bin/false
/bin/link
/bin/ln
/bin/ls
/bin/mkdir
/bin/mknod
/bin/mktemp
/bin/mv
/bin/nice
/bin/printenv
/bin/pwd
/bin/rm
/bin/rmdir
/bin/sleep
/bin/sort
/bin/stat
/bin/stty
/bin/sync
/bin/touch
/bin/true
/bin/uname
%{_bindir}/[
%{_bindir}/[[
%{_bindir}/base32
%{_bindir}/base64
%{_bindir}/basename
%{_bindir}/cat
%{_bindir}/chgrp
%{_bindir}/chmod
%{_bindir}/chown
%{_bindir}/cksum
%{_bindir}/comm
%{_bindir}/cp
%{_bindir}/cut
%{_bindir}/date
%{_bindir}/dd
%{_bindir}/df
%{_bindir}/dirname
%{_bindir}/du
%{_bindir}/echo
%{_bindir}/env
%{_bindir}/expand
%{_bindir}/expr
%{_bindir}/factor
%{_bindir}/false
%{_bindir}/fold
%{_bindir}/groups
%{_bindir}/head
%{_bindir}/hostid
%{_bindir}/id
%{_bindir}/install
%{_bindir}/link
%{_bindir}/ln
%{_bindir}/logname
%{_bindir}/ls
%{_bindir}/md5sum
%{_bindir}/mkdir
%{_bindir}/mkfifo
%{_bindir}/mknod
%{_bindir}/mktemp
%{_bindir}/mv
%{_bindir}/nice
%{_bindir}/nl
%{_bindir}/nohup
%{_bindir}/od
%{_bindir}/paste
%{_bindir}/printenv
%{_bindir}/printf
%{_bindir}/pwd
%{_bindir}/readlink
%{_bindir}/realpath
%{_bindir}/rm
%{_bindir}/rmdir
%{_bindir}/seq
%{_bindir}/sha1sum
%{_bindir}/sha256sum
%{_bindir}/sha512sum
%{_bindir}/shred
%{_bindir}/shuf
%{_bindir}/sleep
%{_bindir}/sort
%{_bindir}/split
%{_bindir}/stat
%{_bindir}/stty
%{_bindir}/sum
%{_bindir}/sync
%{_bindir}/tac
%{_bindir}/tail
%{_bindir}/tee
%{_bindir}/test
%{_bindir}/touch
%{_bindir}/tr
%{_bindir}/true
%{_bindir}/tty
%{_bindir}/uname
%{_bindir}/unexpand
%{_bindir}/uniq
%{_bindir}/unlink
%{_bindir}/users
%{_bindir}/wc
%{_bindir}/who
%{_bindir}/whoami
%{_bindir}/yes
%{_sbindir}/chroot

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
%{_unitdir}/udhcpd.service

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
/bin/{,e,f}grep
%{_bindir}/{,e,f}grep

%files symlinks-cpio
%defattr(-,root,root,-)
/bin/cpio
%{_bindir}/cpio

%files symlinks-procps
%defattr(-,root,root,-)
/bin/ps
/sbin/sysctl
%{_bindir}/ps
%{_bindir}/watch
%{_sbindir}/sysctl
%{_bindir}/free
%{_bindir}/pgrep
%{_bindir}/pkill
%{_bindir}/pmap
%{_bindir}/pwdx
%{_bindir}/top
%{_bindir}/uptime
%{_bindir}/w

%files symlinks-sed
%defattr(-,root,root,-)
/bin/sed
%{_bindir}/sed

%files symlinks-tar
%defattr(-,root,root,-)
/bin/tar
%{_bindir}/tar

%files symlinks-vi
%defattr(-,root,root,-)
/bin/vi
%{_bindir}/vi

%files symlinks-which
%defattr(-,root,root,-)
%{_bindir}/which

%files symlinks-console-tools
%defattr(-,root,root,-)
%{_bindir}/clear
%{_bindir}/reset

%files symlinks-psmisc
%defattr(-,root,root,-)
/sbin/fuser
/sbin/pidof
%{_bindir}/fuser
%{_bindir}/pidof
%{_bindir}/killall
%{_bindir}/pstree
