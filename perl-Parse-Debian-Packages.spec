Name:           perl-Parse-Debian-Packages
Version:        0.03
Release:        2%{?dist}
Summary:        Parse the data from a Debian Packages.gz
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Parse-Debian-Packages/
Source0:        http://www.cpan.org/authors/id/R/RC/RCLAMP/Parse-Debian-Packages-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module parses the Packages files used by the Debian package
management tools.

%prep
%setup -q -n Parse-Debian-Packages-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes sample
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Nov 26 2014 Igor Gnatenko <ignatenko@mirantis.com> - 0.03-2
- fix missing BRs
- drop useless Rs
- fix descriptions by capitalizing "Debian"
- don't remove empty directories
- use DESTDIR instead of PERL_INSTALL_ROOT

* Wed Nov 26 2014 Igor Gnatenko <ignatenko@mirantis.com> - 0.03-1
- Initial package
