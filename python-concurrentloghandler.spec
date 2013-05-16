%global modname ConcurrentLogHandler

Name:           python-concurrentloghandler
Version:        0.8.4
Release:        9%{?dist}
Summary:        Concurrent logging handler (drop-in replacement for RotatingFileHandler)

Group:          Development/Languages
License:        ASL 2.0
URL:            http://pypi.python.org/pypi/ConcurrentLogHandler/
Source0:        http://pypi.python.org/packages/source/C/%{modname}/%{modname}-%{version}.tar.gz
# Upstream's setup.py tries to install tests and doc into /usr which is not what we want
Patch0:         %{modname}-0.8.4-testpath.patch
# RHBZ#858912: don't flush log file if already closed
Patch1:         %{modname}-0.8.4-flush-closed.patch
# RHBZ#952929: ensure stream lock is closed
Patch2:         %{modname}-0.8.4-close-stream-lock.patch
# RHBZ#858922: suppress exceptions in release
Patch3:         %{modname}-0.8.4-exceptions-in-release.patch

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
This module provides an additional log handler for Python's standard logging
package (PEP 282). This handler will write log events to log file which is
rotated when the log file reaches a certain size. Multiple processes can safely
write to the same log file concurrently.


%prep
%setup -q -n %{modname}-%{version}
%patch0
%patch1 -p1
%patch2 -p1
%patch3 -p1


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root=$RPM_BUILD_ROOT


%files
%doc README LICENSE
%{python_sitelib}/*


%changelog
* Thu May 16 2013 Dan Callaghan <dcallagh@redhat.com> - 0.8.4-9
- RHBZ#952929: ensure stream lock is closed
- RHBZ#858922: suppress exceptions in release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 20 2012 Dan Callaghan <dcallagh@redhat.com> - 0.8.4-7
- RHBZ#858912: dont't flush log file if already closed

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 13 2011 Dan Callaghan <dcallagh@redhat.com> - 0.8.4-4
- add a comment about why testpath.patch is needed

* Wed Oct 12 2011 Dan Callaghan <dcallagh@redhat.com> - 0.8.4-3
- clean up spec a little more
- drop version from setuptools dependency as it is not needed

* Tue Oct 04 2011 Dan Callaghan <dcallagh@redhat.com> - 0.8.4-2
- clean up spec a little

* Tue Dec 14 2010 Bill Peck <bpeck@redhat.com> - 0.8.4-1
- initial version
