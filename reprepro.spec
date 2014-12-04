Name:       reprepro
Version:    4.16.0
Release:    1%{?dist}
Summary:    Tool to handle local repositories of Debian packages
License:    GPLv2
URL:        http://mirrorer.alioth.debian.org/
Source0:    https://alioth.debian.org/frs/download.php/latestfile/464/%{name}_%{version}.orig.tar.gz
BuildRequires: libdb-devel
BuildRequires: zlib-devel
BuildRequires: gpgme-devel
BuildRequires: bzip2-devel
BuildRequires: libarchive-devel
BuildRequires: xz-devel

%description
reprepro is a tool to manage a repository of Debian packages (.deb).
It stores files either being injected manually or downloaded from some other 
repository (partially) mirrored into one pool/ hierarchy. 
Managed packages and files are stored in a Berkeley DB, so no database server is 
needed. Checking signatures of mirrored repositories and creating signatures of 
the generated Package indexes is supported. 

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc docs/ AUTHORS README NEWS COPYING
%{_mandir}/man1/changestool.1*
%{_mandir}/man1/reprepro.1*
%{_mandir}/man1/rredtool.1*
%{_bindir}/changestool
%{_bindir}/reprepro
%{_bindir}/rredtool

%changelog
* Thu Dec 04 2014 Igor Gnatenko <ignatenko@mirantis.com> - 4.16.0-1
- Rebase to latest version
- spec cleanup

* Wed Oct 31 2012 Sebastien Caps <sebastien.caps@guardis.com> - 4.12.3-6
- Fixed ifs blocks for fedora/rhel based on G Swift comments 

* Wed Oct 31 2012 Sebastien Caps <sebastien.caps@guardis.com> - 4.12.3-5
- Feedback on openssl patch, patched sha256 error for fc18

* Sun Oct 21 2012 Sebastien Caps <sebastien.caps@guardis.com> - 4.12.3-4
- Fix build dependencies usage on el6
- Switch to openssl md5 and sha because of sha256 errors on fc18

* Wed Aug 29 2012 Sebastien Caps <sebastien.caps@guardis.com> - 4.12.3-3
- Switch from db4-devel db.h to libdb-devel for fc18.

* Tue Aug 14 2012 Sebastien Caps <sebastien.caps@guardis.com> - 4.12.3-2
- Fix some spec file issue.

* Mon Jul 9 2012 Sebastien Caps <sebastien.caps@guardis.com> - 4.12.3-1
- Initial spec.
