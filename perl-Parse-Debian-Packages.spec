Name:           perl-Parse-Debian-Packages
Version:        0.03
Release:        1%{?dist}
Summary:        Parse the data from a debian Packages.gz
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Parse-Debian-Packages/
Source0:        http://www.cpan.org/authors/id/R/RC/RCLAMP/Parse-Debian-Packages-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module parses the Packages files used by the debian package
management tools.

%prep
%setup -q -n Parse-Debian-Packages-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes sample
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Nov 26 2014 Igor Gnatenko <ignatenko@mirantis.com> - 0.03-1
- Initial package
