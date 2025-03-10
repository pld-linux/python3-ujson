#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Ultra fast JSON encoder and decoder for Python
Summary(pl.UTF-8):	Ultraszybki koder i dekoder formatu JSON dla Pythona
Name:		python3-ujson
Version:	3.0.0
Release:	6
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ujson/
Source0:	https://files.pythonhosted.org/packages/source/u/ujson/ujson-%{version}.tar.gz
# Source0-md5:	1c13a485776a2a0dfa1795d101bb3d57
URL:		https://pypi.org/project/ujson/
BuildRequires:	libstdc++-devel
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UltraJSON is an ultra fast JSON encoder and decoder written in pure C
with bindings for Python 3.5+.

%description -l pl.UTF-8
UltraJSON to ultraszybki koder i dekoder formatu JSON, napisany w
czystym C z wiązaniami do Pythona 3.5+.

%prep
%setup -q -n ujson-%{version}

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(readlink -f build-3/lib.*) \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%attr(755,root,root) %{py3_sitedir}/ujson.cpython-*.so
%{py3_sitedir}/ujson-%{version}-py*.egg-info
