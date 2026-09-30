Version: 1.38.0
Release: 1
License: GPLv2
URL: https://github.com/sailfishos/busybox

Source0: http://www.busybox.net/downloads/%{name}-%{version}.tar.bz2
Source1: rpm/udhcpd.service
# TODO: This config should be synced with the dynamic config at some point
# currently the features differ quite a bit
Source2: busybox-static.config
Source3: busybox-sailfish.config
Source4: set_ps1.sh

Patch0:  0001-Copy-extended-attributes-if-p-flag-is-provided-to-cp.patch
Patch1:  0002-applets-Busybox-in-usr-bin-instead-of-bin.patch
Patch2:  0003-Align-watch-with-what-is-in-procps-ng.patch
Patch3:  0004-ash-Load-ENV-file-also-if-SSH_CLIENT-SSH2_CLIENT-is-.patch
Patch4:  0005-ash-job-option-to-restore-term-io-after-job-is-stopp.patch
Patch5:  0006-ash-Write-history-on-SIGHUP.patch
Patch6:  0007-networking-Fix-build-without-cbq-support.patch

BuildRequires: glibc-static
BuildRequires: libselinux-static libsepol-static
BuildRequires: pcre2-static
BuildRequires: pkgconfig(systemd)
BuildRequires: sed

Obsoletes: time <= 1.7
Provides: time > 1.7

# Providing only part of iputils, but should be enough for us.
Obsoletes: iputils <= 20101006
Provides: iputils > 20101006

Obsoletes: busybox-symlinks-cpio <= 1.33.1+git2

%define debug_package %{nil}
