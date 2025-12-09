Summary:	Manage Python errors with ease
Name:		python-crashtest
Version:	0.4.1
Release:	3
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/crashtest/
Source0:	https://files.pythonhosted.org/packages/source/c/crashtest/crashtest-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildArch:	noarch

%description
Crashtest is a Python library that makes exceptions handling and inspection easier.

%files
%doc README.md
%{py_sitedir}/crashtest
%{py_sitedir}/crashtest-*.*-info
