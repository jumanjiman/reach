Name: reach
Version: 0.1.1
release: 1
buildarch: noarch
packager: Paul Morgan <pmorgan@redhat.com>
License: GPL v3
URL: http://www.redhat.com
group: Admin
source: %{name}-%{version}.tar.gz
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
install -m755 src/reach %{buildroot}/bin/
install -m644 src/reach.conf %{buildroot}/etc/reach/

%files
/bin/reach
%config(noreplace) /etc/reach/reach.conf
%doc src/example_usage.txt

%changelog
* Wed Jul 07 2010 Paul Morgan <pmorgan@redhat.com> 0.1.1-1
- new package built with tito

* Thu Mar 18 2010 Paul Morgan <pmorgan@redhat.com>
- initial standalone package
