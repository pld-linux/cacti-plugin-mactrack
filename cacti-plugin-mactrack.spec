%define		namesrc	mactrack	
%include	/usr/lib/rpm/macros.perl
Summary:	MacTrack - Cacti plugin to track device MAC/IP addresses and ports
Summary(pl):	MacTrack - wtyczka Cacti do ¶ledzenia adresów MAC/IP i portów urz±dzeñ
Name:		cacti-plugin-mactrack
Version:	r170
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
#Source0:	http://download.cactiusers.org/downloads/%{namesrc}-%{version}.tar.gz
# $ svn export -r 170 svn://svn.cacti.net/var/svnroot/mactrack/trunk/plugin/mactrack; tar -czf mactrack-r170.tar.gz ./mactrack
# $ svn export -r 170 svn://svn.cacti.net/var/svnroot/mactrack/trunk/native/mactrack; tar -czf mactrack-native-r170.tar.gz ./mactrack
# is plugin and native version
# Source0-md5:	
URL:		http://cactiusers.org/wiki/MacTrackDocs
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
MacTrack - Cacti plugin to track device MAC/IP addresses and ports.

%description -l pl
MacTrack - wtyczka Cacti do ¶ledzenia adresów MAC/IP i portów
urz±dzeñ.

%prep
%setup -q -n %{namesrc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{webcactipluginroot}/docs/*
%{webcactipluginroot}
