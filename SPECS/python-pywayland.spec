Name:           python-pywayland
Version:        0.4.14
Release:        1%{?dist}
Summary:        Python bindings for the libwayland library written in pure Python

License:        Apache2
URL:            https://github.com/flacjacket/pywayland/
Source:         %{pypi_source pywayland}

BuildRequires:  python3-devel
BuildRequires:  wayland-devel
BuildRequires:  gcc


%global _description %{expand:
PyWayland provides a wrapper to the libwayland library using the CFFI library
to provide access to the Wayland library calls and written in pure Python.}


%description %_description

%package -n     python3-pywayland
Summary:        %{summary}

%description -n python3-pywayland %_description


%prep
%autosetup -p1 -n pywayland-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files '*' +auto


%check
%pyproject_check_import -t


%files -n python3-pywayland -f %{pyproject_files}


%changelog
* Sun Jan 01 2023 Jakub Kadlcik <frostyx@email.cz> - 0.4.14-1
- New upstream version

* Tue Jun 14 2022 Jakub Kadlcik <frostyx@email.cz> - 0.4.12-1
- Initial package
