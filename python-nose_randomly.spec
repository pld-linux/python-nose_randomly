#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Nose plugin to randomly order tests and control random.seed
Summary(pl.UTF-8):	Wtyczka nose do losowania kolejności testów oraz sterowania random.seed
Name:		python-nose_randomly
Version:	1.2.6
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/nose-randomly/
Source0:	https://files.pythonhosted.org/packages/source/n/nose-randomly/nose-randomly-%{version}.tar.gz
# Source0-md5:	e358c97da4be4514b8505c27ca8e8a5d
URL:		https://pypi.org/project/nose-randomly/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nose plugin to randomly order tests and control random.seed.

%description -l pl.UTF-8
Wtyczka nose do losowania kolejności testów oraz sterowania
random.seed.

%package -n python3-nose_randomly
Summary:	Nose plugin to randomly order tests and control random.seed
Summary(pl.UTF-8):	Wtyczka nose do losowania kolejności testów oraz sterowania random.seed
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-nose_randomly
Nose plugin to randomly order tests and control random.seed.

%description -n python3-nose_randomly -l pl.UTF-8
Wtyczka nose do losowania kolejności testów oraz sterowania
random.seed.

%prep
%setup -q -n nose-randomly-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m nose tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m nose tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%{py_sitescriptdir}/nose_randomly.py[co]
%{py_sitescriptdir}/nose_randomly-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-nose_randomly
%defattr(644,root,root,755)
%doc AUTHORS.rst HISTORY.rst LICENSE README.rst
%{py3_sitescriptdir}/nose_randomly.py
%{py3_sitescriptdir}/__pycache__/nose_randomly.cpython-*.py[co]
%{py3_sitescriptdir}/nose_randomly-%{version}-py*.egg-info
%endif
