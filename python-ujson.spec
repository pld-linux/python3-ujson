#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Ultra fast JSON encoder and decoder for Python
Summary(pl.UTF-8):	Ultraszybki koder i dekoder formatu JSON dla Pythona
Name:		python-ujson
Version:	2.0.3
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ujson/
Source0:	https://files.pythonhosted.org/packages/source/u/ujson/ujson-%{version}.tar.gz
# Source0-md5:	80d288c186dd02579e1561494b45aa41
URL:		https://pypi.org/project/ujson/
BuildRequires:	libstdc++-devel
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-pytest
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-six
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UltraJSON is an ultra fast JSON encoder and decoder written in pure C
with bindings for Python 2.7 and 3.5+.

%description -l pl.UTF-8
UltraJSON to ultraszybki koder i dekoder formatu JSON, napisany w
czystym C z wiązaniami do Pythona 2.7 oraz 3.5+.

%package -n python3-ujson
Summary:	Ultra fast JSON encoder and decoder for Python
Summary(pl.UTF-8):	Ultraszybki koder i dekoder formatu JSON dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-ujson
UltraJSON is an ultra fast JSON encoder and decoder written in pure C
with bindings for Python 2.7 and 3.5+.

%description -n python3-ujson -l pl.UTF-8
UltraJSON to ultraszybki koder i dekoder formatu JSON, napisany w
czystym C z wiązaniami do Pythona 2.7 oraz 3.5+.

%prep
%setup -q -n ujson-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(readlink -f build-2/lib.*) \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(readlink -f build-3/lib.*) \
%{__python3} -m pytest tests
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
%doc LICENSE.txt README.rst
%attr(755,root,root) %{py_sitedir}/ujson.so
%{py_sitedir}/ujson-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-ujson
%defattr(644,root,root,755)
%doc LICENSE.txt README.rst
%attr(755,root,root) %{py3_sitedir}/ujson.cpython-*.so
%{py3_sitedir}/ujson-%{version}-py*.egg-info
%endif
