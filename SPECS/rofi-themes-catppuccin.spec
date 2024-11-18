%global commit b636a00fd40a7899a8206195464ae8b7f0450a6d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: rofi-themes-catppuccin
Version: 20240620.%{shortcommit}
Release: 1%{?dist}
Summary: Catppuccin themes for rofi
BuildArch: noarch

License: MIT
URL: https://github.com/catppuccin/rofi
Source:  %{URL}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Requires: rofi
Requires: rofi-themes


%description
Soothing pastel theme for Rofi


%prep
%global forgesetupargs -n rofi-%{commit}
%forgesetup


%build


%install
mkdir -p %{buildroot}/%{_datadir}/rofi/themes
cp -rp basic/.local/share/rofi/themes/*.rasi %{buildroot}/%{_datadir}/rofi/themes


%files
%license LICENSE
%doc README.md
%{_datadir}/rofi/themes/catppuccin-*.rasi


%changelog
* Mon Nov 18 2024 Jakub Kadlcik <frostyx@email.cz>
- Initial package
