# The `deno` tool is not packaged in Fedora so we are not running
# the tests for now
%bcond_without check

Name: gleam
Version: 1.1.0
Release: %autorelease
Summary: A friendly language for building type-safe, scalable systems!

# TODO
# SourceLicense:

License: Apache-2.0
URL: https://github.com/gleam-lang/gleam
Source: %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cargo-rpm-macros >= 24
# BuildRequires: cargo
%if %{with check}
BuildRequires: clippy
%endif
Requires: erlang


%description
Gleam is a general-purpose, concurrent, functional high-level programming
language that compiles to Erlang or JavaScript source code. Gleam is
a statically-typed language, which is different from the most popular languages
that run on Erlang’s virtual machine BEAM, Erlang and Elixir.


%prep
%autosetup
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires


%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies


%install
%cargo_install
# mkdir -p %{buildroot}/%{_bindir}/
# cp -a target/release/%{name} %{buildroot}/%{_bindir}/


%if %{with check}
%check
%cargo_test
%endif


%files
%license LICENCE
%license compiler-cli/LICENCE
%license compiler-core/LICENCE
%license compiler-wasm/LICENCE
%license test-package-compiler/LICENCE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc README.md
%{_bindir}/gleam


%changelog
%autochangelog
