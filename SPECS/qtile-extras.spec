%global commit f3ea5b91f6c29b91b1e7860f9bf6d39e7751b602
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshot 20220105%{shortcommit}

Name: qtile-extras
Version: 0^%{snapshot}
Release: 1%{?dist}
Summary: A collection of mods for Qtile.

License: MIT
URL: https://github.com/elParaguayo/qtile-extras
Source0: %{URL}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytest
BuildRequires: python3-requests
BuildRequires: qtile >= 0.19.0
BuildRequires: pango-devel
BuildRequires: gdk-pixbuf2-devel

Requires: qtile >= 0.19.0


%description
A collection of third-party widgets, toolkits, wallpapers, and other extras for
Qtile.

For more, please read
https://qtile-extras.readthedocs.io/


%prep
%autosetup -n %{name}-%{commit}

# The stravalib isn't packaged for Fedora yet
# https://pypi.org/project/stravalib/
rm -rf qtile_extras/widget/strava.py
rm -rf qtile_extras/resources/stravadata
rm -rf test/widget/test_strava.py

# The iwlib isn't packaged for Fedora anymore
# https://pypi.org/project/iwlib/
rm -rf qtile_extras/widget/network.py
rm -rf test/widget/test_network.py


%build
%py3_build


%check
%{python3} setup.py test


%install
%py3_install

rm -rf %{buildroot}%{python3_sitelib}/test


%files
%license LICENSE
%doc README.md
%{python3_sitelib}/qtile_extras
%{python3_sitelib}/qtile_extras-*.egg-info


%changelog
* Wed Jan 05 2022 Jakub Kadlcik <frostyx@email.cz>
- Initial package
