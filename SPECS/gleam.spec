%global debug_package %{nil}

Name: gleam
Version: 1.2.1
Release: 1%{?dist}
Summary: A friendly language for building type-safe, scalable systems!

License: Apache-2.0
URL: https://github.com/gleam-lang/gleam
Source: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cargo
BuildRequires: clippy
Requires: erlang


%description
Gleam is a general-purpose, concurrent, functional high-level programming
language that compiles to Erlang or JavaScript source code. Gleam is
a statically-typed language, which is different from the most popular languages
that run on Erlang’s virtual machine BEAM, Erlang and Elixir.


%prep
%autosetup


%build
%make_build


%install
%make_install
mkdir -p %{buildroot}/%{_bindir}/
cp -a target/release/%{name} %{buildroot}/%{_bindir}/


%check
# The `deno` tool is not packaged in Fedora so we are not running
# the tests for now
# make test


%files
%license LICENCE
%doc README.md
%doc CHANGELOG.md
%{_bindir}/%{name}


%changelog
* Fri May 31 2024 Jakub Kadlcik <frostyx@email.cz> - 1.2.1-1
- New upstream version

* Mon May 27 2024 Jakub Kadlcik <frostyx@email.cz> - 1.2.0-1
- New upstream version

* Wed Apr 17 2024 Jakub Kadlcik <frostyx@email.cz> - 1.1.0-1
- New upstream version

* Sat Apr 13 2024 Jakub Kadlcik <frostyx@email.cz> 1.0.0-1
- Initial package
