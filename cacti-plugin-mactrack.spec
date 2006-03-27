%define		namesrc	mactrack	
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - MacTrack
Summary(pl):	Wtyczka do Cacti - MacTrack
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
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - 

%description -l pl
Wtyczka do Cacti - 

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
