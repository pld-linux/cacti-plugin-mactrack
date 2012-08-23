# TODO
# - use system jquery
%define		plugin mactrack
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	End Device Port Tracker and General Network Toolkit
Summary(pl.UTF-8):	MacTrack - wtyczka Cacti do śledzenia adresów MAC/IP i portów urządzeń
Name:		cacti-plugin-%{plugin}
Version:	2.9
Release:	6
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/plugin:mactrack-v%{version}-1.tgz
# Source0-md5:	397e91c4c2059068f39abfb5b84b24ca
URL:		http://docs.cacti.net/plugin:mactrack
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	cacti
Requires:	cacti(pia) >= 2.0
Requires:	php(core) >= %{php_min_version}
Requires:	php(pcre)
Requires:	php-date
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
MacTrack - Cacti plugin to track device MAC/IP addresses and ports.

%description -l pl.UTF-8
MacTrack - wtyczka Cacti do śledzenia adresów MAC/IP i portów
urządzeń.

%prep
%setup -qc
mv %{plugin}/{LICENSE,README,docs} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/CHANGELOG
%{plugindir}
