%define		namesrc	mactrack	
%include	/usr/lib/rpm/macros.perl
Summary:	MacTrack - Cacti plugin to track device MAC/IP addresses and ports
Summary(pl.UTF-8):   MacTrack - wtyczka Cacti do śledzenia adresów MAC/IP i portów urządzeń
Name:		cacti-plugin-mactrack
Version:	0.0.1b
#this is Pre-BETA version
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://download.cactiusers.org/downloads/%{namesrc}.tar.gz
# Source0-md5:	b7cd45a9a27736d046205530dc200f96
URL:		http://cactiusers.org/wiki/MacTrackDocs
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
MacTrack - Cacti plugin to track device MAC/IP addresses and ports.

%description -l pl.UTF-8
MacTrack - wtyczka Cacti do śledzenia adresów MAC/IP i portów
urządzeń.

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
# remove patched files
rm -rdf "patched files"
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{webcactipluginroot}/docs/*
%{webcactipluginroot}
