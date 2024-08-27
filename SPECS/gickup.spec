%global debug_package %{nil}

Name: gickup
Version: 0.10.32
Release: 1%{?dist}
Summary: Mirror repositories from one git forge to another

License: Apache-2.0
URL: https://github.com/cooperspencer/gickup
Source: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: golang
BuildRequires: git


%description
Gickup is a tool that allows you to clone/mirror repositories from one hoster to
another. This is useful if you want to have a backup of your repositories on
another hoster or to a local server.


%prep
%autosetup


%build
go build


%install
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp gickup %{buildroot}%{_bindir}/


%check
go test


%files
%license LICENSE
%doc README.md
%{_bindir}/gickup


%changelog
* Tue Aug 27 2024 Jakub Kadlcik <frostyx@email.cz> - 0.10.32-1
- New upstream version

* Thu Aug 01 2024 Jakub Kadlcik <frostyx@email.cz> - 0.10.31-1
- New upstream version

* Sat Jun 22 2024 Jakub Kadlcik <frostyx@email.cz>
- Initial package
