#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pytest_cov
Version  : 3.0.0
Release  : 80
URL      : https://files.pythonhosted.org/packages/61/41/e046526849972555928a6d31c2068410e47a31fb5ab0a77f868596811329/pytest-cov-3.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/61/41/e046526849972555928a6d31c2068410e47a31fb5ab0a77f868596811329/pytest-cov-3.0.0.tar.gz
Summary  : Pytest plugin for measuring coverage.
Group    : Development/Tools
License  : MIT
Requires: pypi-pytest_cov-license = %{version}-%{release}
Requires: pypi-pytest_cov-python = %{version}-%{release}
Requires: pypi-pytest_cov-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(coverage)
BuildRequires : pypi(pip)
BuildRequires : pypi(py)
BuildRequires : pypi(pytest)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(six)
BuildRequires : pypi(virtualenv)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
Overview
        ========
        
        .. start-badges

%package license
Summary: license components for the pypi-pytest_cov package.
Group: Default

%description license
license components for the pypi-pytest_cov package.


%package python
Summary: python components for the pypi-pytest_cov package.
Group: Default
Requires: pypi-pytest_cov-python3 = %{version}-%{release}

%description python
python components for the pypi-pytest_cov package.


%package python3
Summary: python3 components for the pypi-pytest_cov package.
Group: Default
Requires: python3-core
Provides: pypi(pytest_cov)
Requires: pypi(coverage)
Requires: pypi(pytest)

%description python3
python3 components for the pypi-pytest_cov package.


%prep
%setup -q -n pytest-cov-3.0.0
cd %{_builddir}/pytest-cov-3.0.0
pushd ..
cp -a pytest-cov-3.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656400848
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytest_cov
cp %{_builddir}/pytest-cov-3.0.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytest_cov/07800edab5f4e77a7371e226f11ba91f963a11cf
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pytest_cov/07800edab5f4e77a7371e226f11ba91f963a11cf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
