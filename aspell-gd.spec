Summary:	Scottish Gaelic dictionary for aspell
Summary(pl):	S³ownik szkocki gaelicki dla aspella
Name:		aspell-gd
Version:	0.1.1
%define	subv	1
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/gd/aspell5-gd-%{version}-%{subv}.tar.bz2
# Source0-md5:	171673ec92270f58f945c4317286220b
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scottish Gaelic dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik szklocki gaelicki (lista s³ów) dla aspella.

%prep
%setup -q -n aspell5-gd-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README doc/Crawler.txt
%{_libdir}/aspell/*
%{_datadir}/aspell/*
