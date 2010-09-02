Name: reach
summary: Wrapper for the ping command

Version: 0.2
release: 0%{?dist}
License: GPL v3
group: Applications/System

URL: http://github.com/jumanjiman/reach
source: %{name}-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
buildarch: noarch

requires: /bin/ping
requires: bash

%description
Use reach instead of ping to simplify scripts.

%prep
%setup -q

%clean
%{__rm} -rf %{buildroot}

%build
# nothing to build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/reach
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m755 src/reach %{buildroot}%{_bindir}
%{__install} -p -m644 src/reach.conf %{buildroot}%{_sysconfdir}/reach

%files
%defattr(-,root,root,-)
%{_bindir}/reach
%config(noreplace) %{_sysconfdir}/reach/reach.conf
%doc src/example_usage.txt

%changelog
* Wed Jul 07 2010 Paul Morgan <pmorgan@redhat.com> 0.1.1-1
- new package built with tito

* Thu Mar 18 2010 Paul Morgan <pmorgan@redhat.com>
- initial standalone package
