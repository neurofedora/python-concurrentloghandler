%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%define modname ConcurrentLogHandler

Name:           python-concurrentloghandler
Version:        0.8.4
Release:        2%{?dist}
Summary:        Concurrent logging handler (drop-in replacement for RotatingFileHandler)

Group:          Development/Languages
License:        ASL 2.0
URL:            http://pypi.python.org/pypi/ConcurrentLogHandler/
Source0:        http://pypi.python.org/packages/source/C/%{modname}/%{modname}-%{version}.tar.gz
Patch0:         %modname-0.8.4-testpath.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel >= 0.6.11

%description
This module provides an additional log handler for Python's standard logging
package (PEP 282). This handler will write log events to log file which is
rotated when the log file reaches a certain size. Multiple processes can safely
write to the same log file concurrently.


%prep
%setup -q -n %{modname}-%{version}
%patch0


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README LICENSE
%{python_sitelib}/*


%changelog
* Tue Oct 04 2011 Dan Callaghan <dcallagh@redhat.com> - 0.8.4-2
- clean up spec a little

* Tue Dec 14 2010 Bill Peck <bpeck@redhat.com> - 0.8.4-1
- initial version
