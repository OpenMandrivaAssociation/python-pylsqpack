%define module pylsqpack

Name:		python-pylsqpack
Version:	0.3.24
Release:	1
Summary:	Python wrapper for the ls-qpack QPACK library
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/pylsqpack/
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description
Python wrapper for the ls-qpack QPACK library

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info

