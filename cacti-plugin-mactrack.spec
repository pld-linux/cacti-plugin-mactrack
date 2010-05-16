%define		plugin mactrack
%include	/usr/lib/rpm/macros.perl
Summary:	MacTrack - Cacti plugin to track device MAC/IP addresses and ports
Summary(pl.UTF-8):	MacTrack - wtyczka Cacti do śledzenia adresów MAC/IP i portów urządzeń
Name:		cacti-plugin-mactrack
Version:	1.1
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{plugin}-%{version}.zip
# Source0-md5:	635bb1df81bf9c0f28368438c4dcba42
URL:		http://cactiusers.org/wiki/MacTrackDocs
BuildRequires:	rpm-perlprov
BuildRequires:	unzip
Requires:	cacti
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{plugindir}/docs/*
%{plugindir}
