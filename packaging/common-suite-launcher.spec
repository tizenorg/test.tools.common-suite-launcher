Name:		common-suite-launcher
Version:	1.0.0
Release:	0
License:	GPL-2.0
Summary:	Launcher of Tizen Common test suites
Group:		Development/Testing
Source:		%{name}-%{version}-%{release}.tar.gz
Source1001:	%{name}.manifest
Requires:	xmlstarlet
BuildArch:	noarch


%description

Common Suite Launcher is the Launcher of the test suites of the Tizen Common profile


%prep
%setup -q
cp %{SOURCE1001} .


%build


%install
install -d %{buildroot}/%{_bindir}
install -m 0755 src/%{name} %{buildroot}/%{_bindir}


%files
%manifest %{name}.manifest
%defattr(-,root,root)
%{_bindir}/common-suite-launcher
