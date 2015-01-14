%{!?pyver: %define pyver %(%{__python} -c "import sys ; print sys.version[:3]")}

Name:           python-daemon
Version:        2.0.3
Release:        1%{?dist}
Summary:        Library to implement a well-behaved Unix daemon process

Group:          Development/Languages
License:        Python
URL:            http://pypi.python.org/pypi/python-daemon/
Source0:        http://pypi.python.org/packages/source/p/python-daemon/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools
BuildRequires:  python-nose python-testtools python-testscenarios
BuildRequires:  python-lockfile python-minimock
Requires:       python-lockfile >= 0.10

%description
This library implements the well-behaved daemon specification of PEP 3143,
"Standard daemon process library".

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
rm -fr %{buildroot}%{python_sitelib}/tests

# Test suite requires minimock and lockfile
%check
#PYTHONPATH=$(pwd) nosetests

%files
%license LICENSE.ASF-2
%{python_sitelib}/daemon/
%{python_sitelib}/python_daemon-%{version}-py%{pyver}.egg-info/

%changelog
* Wed Jan 14 2015 Igor Gnatenko <ignatenko@mirantis.com> - 2.0.3-1
- update to 2.0.3

* Mon Aug  4 2014 Thomas Spura <tomspur@fedoraproject.org> - 1.6-7
- enable tests again as lockfile was fixed

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Kushal Das <kushal@fedoraproject.org> - 1.6-1
- New release of source

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Dec 23 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.5.2-1
- add missing BR: python-nose
- also add lockfile as R (bug #513546)
- update to 1.5.2

* Wed Dec 23 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.5.1-2
- add missing BR: minimock and lockfile -> testsuite works again
- remove patch, use sed instead

* Wed Oct 07 2009 Luke Macken <lmacken@redhat.com> - 1.5.1-1
- Update to 1.5.1
- Remove conflicting files (#512760)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 24 2009 Kushal Das <kushal@fedoraproject.org> 1.4.6-1
- Initial release

