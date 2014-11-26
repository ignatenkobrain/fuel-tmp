Name:           multistrap
Version:        2.2.0
Release:        2%{?dist}
Summary:        multiple repository bootstrap based on apt

License:        GPLv3
URL:            http://www.emdebian.org/multistrap/
Source0:        http://ftp.debian.org/debian/pool/main/m/multistrap/%{name}_%{version}.tar.gz

BuildRequires:  po4a
Requires:       perl(Config::IniFiles) apt dpkg

%description
A debootstrap replacement with multiple repository support,
using apt to handle all dependency issues and conflicts.

Multistrap includes support for native and foreign architecture
bootstrap environments. Foreign bootstraps only need minimal
configuration on the final device. Also supports cleaning up the
generated bootstrap filesystem to remove downloaded packages and
hooks to modify the files in the bootstrap filesystem after the
packages have been unpacked but before being configured.

Unlike debootstrap, multistrap relies on working versions of
dpkg and apt outside the final filesystem. If dpkg supports
MultiArch, foreign architecture libraries can be installed,
where available.

Multistrap supercedes emdebian-rootfs and replaces the previous
support for preparing root filesystems for specific machines and
variants. Multistrap includes the previous emdebian-rootfs support
for customisation of package selection and of files created
within the root filesystem.

%prep
%setup -q
echo "#!/bin/sh" > ./configure
chmod +x ./configure

%build
%configure
make

%install
%make_install
mkdir -p %{buildroot}%{_sbindir}/
mkdir -p %{buildroot}%{_sysconfdir}/bash_completion.d/
mkdir -p %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{_mandir}

install -Dpm 0755 %{name} %{buildroot}%{_sbindir}/
cp -pr doc/multistrap/man/* %{buildroot}%{_mandir}/
install -Dpm 0644 bash/%{name} %{buildroot}%{_sysconfdir}/bash_completion.d/
install -Dpm 0755 check-deps.sh %{buildroot}%{_datadir}/%{name}/
install -Dpm 0644 device-table.pl %{buildroot}%{_datadir}/%{name}/
install -Dpm 0644 update-rc.d %{buildroot}%{_datadir}/%{name}/
install -Dpm 0644 cross/*.conf %{buildroot}%{_datadir}/%{name}/
install -Dpm 0644 cross/test.c %{buildroot}%{_datadir}/%{name}/
install -Dpm 0755 cross/setcrossarch.sh %{buildroot}%{_datadir}/%{name}/

%files
%doc examples/
%{_sbindir}/%{name}
%{_datadir}/%{name}
%{_sysconfdir}/bash_completion.d/%{name}
%{_mandir}/*/%{name}.*
%{_mandir}/*/*/%{name}.*
%{_mandir}/*/device-table.*
%{_mandir}/*/*/device-table.*

%changelog
* Wed Nov 26 2014 Igor Gnatenko <ignatenko@mirantis.com> - 2.2.0-2
- dpkg as requires

* Tue Nov 25 2014 Igor Gnatenko <ignatenko@mirantis.com> - 2.2.0-1
- Initial package
