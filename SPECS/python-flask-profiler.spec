Name:           python-flask-profiler
Version:        1.8
Release:        %autorelease
Summary:        API endpoint profiler for Flask framework

License:        MIT
URL:            https://github.com/muatik/flask-profiler
Source:         %{pypi_source flask_profiler}
Source:         %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pymongo
BuildRequires:  python3-sqlalchemy


%global _description %{expand:
Flask-profiler measures endpoints defined in your flask application; and
provides you fine-grained report through a web interface. It gives answers to
these questions:

- Where are the bottlenecks in my application?
- Which endpoints are the slowest in my application?
- Which are the most frequently called endpoints?
- What causes my slow endpoints? In which context, with what args and kwargs are
  they slow?
- How much time did a specific request take?

In short, if you are curious about what your endpoints are doing and what
requests they are receiving, give a try to flask-profiler.

With flask-profiler's web interface, you can monitor all your endpoints'
performance and investigate endpoints and received requests by drilling down
through filters.}

%description %_description

%package -n     python3-flask-profiler
Summary:        %{summary}

%description -n python3-flask-profiler %_description


%prep
%autosetup -p1 -n flask_profiler-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files 'flask_profiler' +auto


%check
%pyproject_check_import

# The project has unit tests but we are not running them because they require
# Flask-Testing which is not packaged into RPM yet
# https://pypi.org/project/Flask-Testing/
# See upstream .travis.yml on how to run tests


%files -n python3-flask-profiler -f %{pyproject_files}


%changelog
%autochangelog
