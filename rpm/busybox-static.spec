Summary: Statically linked version of busybox
Name: busybox-static

%include rpm/busybox-common.inc

%description
Busybox is a single binary which includes versions of a large number
of system commands, including a shell. This package can be very
useful for recovering from certain types of system failures,
particularly those involving broken shared libraries. This package
provides a statically linked version of Busybox.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%conf
# BusyBox uses a deprecated SELinux API
export CFLAGS="$CFLAGS -Wno-deprecated-declarations"

# Build static version
cp %{SOURCE2} .config
yes "" | make oldconfig

%build
# BusyBox uses a deprecated SELinux API
export CFLAGS="$CFLAGS -Wno-deprecated-declarations"
%make_build CRYPT_AVAILABLE=n

%install
mkdir -p %{buildroot}/bin
mkdir -p %{buildroot}/usr/bin
install -m 755 busybox %{buildroot}/usr/bin/busybox-static
ln -s ../usr/bin/busybox-static %{buildroot}/bin/busybox-static

%files
%license LICENSE
/bin/busybox-static
%{_bindir}/busybox-static
