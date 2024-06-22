Name: qtile-extras
Version: 0.26.0
Release: 1%{?dist}
Summary: A collection of mods for Qtile.

License: MIT
URL: https://github.com/elParaguayo/qtile-extras
Source0: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pytest
BuildRequires: python3-requests
BuildRequires: python3-pip
BuildRequires: python3-wheel
BuildRequires: qtile = %{version}
BuildRequires: pango-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: python3-pytest-lazy-fixture
BuildRequires: python3-dbus-next

# The tarball is missing .git directory, we need to create it during build
BuildRequires: git

Requires: qtile = %{version}


%description
A collection of third-party widgets, toolkits, wallpapers, and other extras for
Qtile.

For more, please read
https://qtile-extras.readthedocs.io/


%generate_buildrequires
%pyproject_buildrequires


%prep
%autosetup -n %{name}-%{version}
git init
%py3_shebang_fix .

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
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files qtile_extras

rm -rf %{buildroot}%{python3_sitelib}/test


%check
# %%pytest -vv --backend x11


%files -n qtile-extras -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
* Thu May 23 2024 Jakub Kadlcik <frostyx@email.cz> - 0.26.0-1
- New upstream version

* Sun Nov 05 2023 Jakub Kadlcik <frostyx@email.cz> - 0.23.0-1
- New upstream version

* Thu Sep 22 2022 Jakub Kadlcik <frostyx@email.cz> - 0.22.1-1
- Upgrade to the new upstream version

* Wed Jan 05 2022 Jakub Kadlcik <frostyx@email.cz>
- Initial package
