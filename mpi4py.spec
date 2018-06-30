#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mpi4py
Version  : 3.0.0
Release  : 6
URL      : https://bitbucket.org/mpi4py/mpi4py/downloads/mpi4py-3.0.0.tar.gz
Source0  : https://bitbucket.org/mpi4py/mpi4py/downloads/mpi4py-3.0.0.tar.gz
Summary  : Python bindings for MPI
Group    : Development/Tools
License  : BSD-2-Clause
Requires: mpi4py-python3
Requires: mpi4py-license
Requires: mpi4py-python
BuildRequires : cmake
BuildRequires : openmpi-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==============
        
        This package provides Python bindings for the **Message Passing
        Interface** (MPI_) standard. It is implemented on top of the MPI-1/2/3
        specification and exposes an API which grounds on the standard MPI-2
        C++ bindings.

%package dev
Summary: dev components for the mpi4py package.
Group: Development
Provides: mpi4py-devel

%description dev
dev components for the mpi4py package.


%package license
Summary: license components for the mpi4py package.
Group: Default

%description license
license components for the mpi4py package.


%package python
Summary: python components for the mpi4py package.
Group: Default
Requires: mpi4py-python3

%description python
python components for the mpi4py package.


%package python3
Summary: python3 components for the mpi4py package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mpi4py package.


%prep
%setup -q -n mpi4py-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530377224
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/mpi4py
cp LICENSE.rst %{buildroot}/usr/share/doc/mpi4py/LICENSE.rst
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib/python3.7/site-packages/mpi4py/include/mpi4py/mpi4py.MPI.h
/usr/lib/python3.7/site-packages/mpi4py/include/mpi4py/mpi4py.MPI_api.h
/usr/lib/python3.7/site-packages/mpi4py/include/mpi4py/mpi4py.h

%files license
%defattr(-,root,root,-)
/usr/share/doc/mpi4py/LICENSE.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
