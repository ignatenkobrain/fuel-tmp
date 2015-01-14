%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%global with_python3 1

%define upstream_name lockfile

Name:           python-%{upstream_name}
Version:        0.10.2
Release:        1%{?dist}
Epoch:          1
Summary:        A platform-independent file locking module

Group:          Development/Languages
License:        MIT
URL:            https://github.com/openstack/pylockfile
Source0:        https://pypi.python.org/packages/source/l/lockfile/%{upstream_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-pbr

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-pbr
%endif # with_python3

%description
The lockfile module exports a FileLock class which provides a simple API for
locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms. The
lock mechanism relies on the atomic nature of the link (on Unix) and mkdir (on
Windows) system calls.

%if 0%{?with_python3}
%package -n python3-lockfile
Summary:        A platform-independent file locking module
Group:          Development/Languages

%description -n python3-lockfile
The lockfile module exports a FileLock class which provides a simple API for
locking files. Unlike the Windows msvcrt.locking function, the Unix
fcntl.flock, fcntl.lockf and the deprecated posixfile module, the API is
identical across both Unix (including Linux and Mac) and Windows platforms. The
lock mechanism relies on the atomic nature of the link (on Unix) and mkdir (on
Windows) system calls.
This is a Python 3 build of lockfile package.
%endif # with_python3

%prep
%setup -q -n %{upstream_name}-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
popd
%endif # with_python3

%check
nosetests

%if 0%{?with_python3}
pushd %{py3dir}
PYTHONPATH=$(pwd) nosetests-%{python3_version}
popd
%endif # with_python3

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ACKS AUTHORS LICENSE PKG-INFO README RELEASE-NOTES doc/
%{python_sitelib}/%{upstream_name}
%{python_sitelib}/%{upstream_name}-%{version}-*.egg-info

%if 0%{?with_python3}
%files -n python3-lockfile
%defattr(-,root,root,-)
%doc ACKS AUTHORS LICENSE PKG-INFO README RELEASE-NOTES doc/
%{python3_sitelib}/%{upstream_name}
%{python3_sitelib}/%{upstream_name}-%{version}-*.egg-info
%endif # with_python3

%changelog
* Tue Dec 09 2014 Slavek Kabrda <bkabrda@redhat.com> - 1:0.10.2-1
- Update to 0.10.2
- Drop patches merged upstream
- Update URL and Source to point to new upstream

* Fri Jun 20 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1:0.9.1-8
- Properly list files for python3-lockfile subpackage.

* Fri Jun 20 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1:0.9.1-7
- Added python3-lockfile subpackage.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 24 2011 Silas Sewell <silas@sewell.org> - 1:0.9.1-1
- Update to 0.9.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 03 2010 Silas Sewell <silas@sewell.ch> - 1:0.8-1
- Update to 0.8, increase epoch

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 06 2010 Silas Sewell <silas@sewell.ch> - 0.9-1
- Update to 0.9

* Tue Jul 06 2010 Silas Sewell <silas@sewell.ch> - 0.8-2
- Bump for EL6 build

* Thu Jul 23 2009 Silas Sewell <silas@sewell.ch> - 0.8-1
- Initial build
