Name: reach
Version: 0.1
release: 1
buildarch: noarch
packager: Paul Morgan <pmorgan@redhat.com>
License: GPL v3
URL: http://www.redhat.com
group: Admin
source: %{name}-%{version}.tgz
summary: Wrapper for the ping command
requires: /bin/ping
prereq: bash
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
Use reach instead of ping to simplify scripts.

%prep
%setup -q

%clean
rm -fr %{buildroot}

%build
# nothing to build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/{etc/reach,bin}
install -m755 reach %{buildroot}/bin/
install -m644 reach.conf %{buildroot}/etc/reach/

%files
/bin/reach
%config(noreplace) /etc/reach/reach.conf
%doc example_usage.txt

%changelog
* Thu Mar 18 2010 Paul Morgan <pmorgan@redhat.com>
- initial standalone package
