%define module pylsqpack

Name:		python-pylsqpack
Version:	0.3.19
Release:	1
Summary:	Python wrapper for the ls-qpack QPACK library
URL:		https://pypi.org/project/pylsqpack/
License:	BSD-3-Clause
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pylsqpack/%{module}-%{version}.tar.gz
BuildSystem:	python

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)


%description
Python wrapper for the ls-qpack QPACK library

%prep
%autosetup -n %{module}-%{version} -p1

%build
export CFLAGS="%{optflags}"
%py_build

%install
%py_install

%files
%{python3_sitearch}/%{module}
%{python3_sitearch}/%{module}-%{version}.dist-info
%license LICENSE
