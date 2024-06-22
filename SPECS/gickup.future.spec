%global debug_package %{nil}

# This specfile is written according to the Fedora Golang Packaging Guidelines
# but it doesn't work because of missing dependencies. I don't know how to fix
# it, so I am going to use a different specfile which would never pass the
# Fedora review process.

# https://github.com/cooperspencer/gickup
%global goipath         github.com/cooperspencer/gickup
%global forgeurl        https://github.com/cooperspencer/gickup
Version:                0.10.30

%gometa

%global common_description %{expand:
Gickup is a tool that allows you to clone/mirror repositories from one hoster to
another. This is useful if you want to have a backup of your repositories on
another hoster or to a local server.}

%global golicenses    LICENSE
%global godocs        *.md

%global godevelheader %{expand:
Requires:  %{name} = %{version}-%{release}
}

Name:           %{goname}
Release:        1%{?dist}
Summary:        Mirror repositories from one git forge to another
License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

BuildRequires: git
BuildRequires: golang(github.com/alecthomas/kong)
BuildRequires: golang(github.com/go-git/go-git/v5)
BuildRequires: golang(github.com/robfig/cron/v3)
BuildRequires: golang(github.com/rs/zerolog)
BuildRequires: golang(github.com/shurcooL/githubv4)
BuildRequires: golang(github.com/xanzy/go-gitlab)
BuildRequires: golang(golang.org/x/oauth2)
BuildRequires: golang(gopkg.in/natefinch/lumberjack.v2)
BuildRequires: golang(gopkg.in/yaml.v3)

# Not packaged yet:
# BuildRequires: golang(code.gitea.io/sdk/gitea)
# BuildRequires: golang(github.com/cooperspencer/onedev)
# BuildRequires: golang(github.com/gogs/go-gogs-client)
# BuildRequires: golang(github.com/google/go-cmp)
# BuildRequires: golang(github.com/google/go-github/v41)
# BuildRequires: golang(github.com/gookit/color)
# BuildRequires: golang(github.com/ktrysmt/go-bitbucket)
# BuildRequires: golang(github.com/melbahja/goph)
# BuildRequires: golang(github.com/prometheus/client_golang)
# BuildRequires: golang(golang.org/x/crypto)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
# go get $goipath
# Not all gickup dependencies are packaged in Fedora.
# According to the Fedora Go Packaging Guidelines:
#
# > At the moment golang projects packaged in Fedora SHOULD be unbundled by
# > default. It means projects are built from dependencies packaged in Fedora.
# > For some project it can be reasonable to build from bundled dependencies.
# > Every bundling needs a proper justification.
#
# Which makes a perfect sense but they don't tell us how to bundle some
# dependencies. So instead of the standard
# we are simply going to run `go build` manually.

go build -o %{gobuilddir}/bin/gickup
# %%gobuild -o %{gobuilddir}/bin/gickup

%install
%gopkginstall
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/gickup %{buildroot}%{_bindir}/

%check
%gocheck

%files
%license %{golicenses}
%doc %{godocs}
%{_bindir}/gickup

%gopkgfiles

%changelog
* Fri Jun 21 2024 Jakub Kadlcik <frostyx@email.cz>
- Initial package
