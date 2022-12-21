Name:           python-pywlroots
Version:        0.15.24
Release:        1%{?dist}
Summary:        Python binding to the wlroots library using cffi

License:        MIT
URL:            https://github.com/flacjacket/pywlroots
Source:         %{pypi_source pywlroots}

BuildRequires: python3-devel
BuildRequires: gcc
BuildRequires: wlroots-devel >= 0.15
BuildRequires: python3-pywayland
BuildRequires: python3-xkbcommon
BuildRequires: python3-pip
BuildRequires: python3-setuptools
BuildRequires: python3-build
BuildRequires: python3-wheel

Requires:  wlroots


%global _description %{expand:
A Python binding to the wlroots library using cffi. The library uses pywayland
to provide the Wayland bindings and python-xkbcommon to provide wlroots
keyboard functionality.}


%description %_description

%package -n     python3-pywlroots
Summary:        %{summary}

%description -n python3-pywlroots %_description


%prep
%autosetup -p1 -n pywlroots-%{version}


%generate_buildrequires

# We cant use %%pyproject_buildrequires because of
# https://bugzilla.redhat.com/show_bug.cgi?id=2097535
# Until it's resolved, the following line needs to be commented-out and the
# BuildRequires needs to be specified manually
# %%pyproject_buildrequires


%build
python3 wlroots/ffi_build.py
python3 -m build --wheel --no-isolation
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files '*' +auto


%check
%pyproject_check_import -t


%files -n python3-pywlroots -f %{pyproject_files}


%changelog
* Tue Dec 20 2022 Jakub Kadlcik <frostyx@email.cz> - 0.15.24-1
- New upstream version

* Tue Jun 14 2022 Jakub Kadlcik <frostyx@email.cz> - 0.15.17-1
- Initial package
