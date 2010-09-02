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
# convert manpages
/usr/bin/a2x -d manpage -f manpage doc/reach.1.asciidoc
/usr/bin/a2x -d manpage -f manpage doc/reach.conf.5.asciidoc


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/reach
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m755 src/reach %{buildroot}%{_bindir}
%{__install} -p -m644 src/reach.conf %{buildroot}%{_sysconfdir}/reach
# manpages
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__mkdir_p} %{buildroot}%{_mandir}/man5
%{__gzip} -c doc/reach.1 > %{buildroot}/%{_mandir}/man1/reach.1.gz
%{__gzip} -c doc/reach.conf.5 > %{buildroot}/%{_mandir}/man5/reach.conf.5.gz


%files
%defattr(-,root,root,-)
%{_bindir}/reach
%config(noreplace) %{_sysconfdir}/reach/reach.conf
%doc %{_mandir}/man1/reach.1.gz
%doc %{_mandir}/man5/reach.conf.5.gz
%doc doc/COPYING

%changelog
* Wed Jul 07 2010 Paul Morgan <pmorgan@redhat.com> 0.1.1-1
- new package built with tito

* Thu Mar 18 2010 Paul Morgan <pmorgan@redhat.com>
- initial standalone package
