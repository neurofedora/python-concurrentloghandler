# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

%define modname ConcurrentLogHandler

Name:           python-concurrentloghandler
Version:        0.8.4
Release:        1%{?dist}
Summary:        Concurrent logging handler (drop-in replacement for RotatingFileHandler)

Group:          Development/Languages
License:        Apache Software License
URL:            http://pypi.python.org/packages/source/C/ConcurrentLogHandler
Source0:        %{modname}-%{version}.tar.bz2
Patch0:         %modname-0.8.4-testpath.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools-devel >= 0.6c11

%description
This module provides an additional log handler for Python's standard logging
package (PEP 282). This handler will write log events to log file which is
rotated when the log file reaches a certain size. Multiple processes can safely
write to the same log file concurrently.


%prep
%setup -q -n %{modname}-%{version}
%patch0


%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --install-data=%_defaultdocdir/%name

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README LICENSE
# For noarch packages: sitelib
%{python_sitelib}/*
# For arch-specific packages: sitearch
%{python_sitearch}/*


%changelog
