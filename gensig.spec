Summary:	Random signature generator
Summary(pl):	Generator losowych sygnaturek
Name:		gensig
Version:	2.3
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.geekthing.com/~robf/gensig/%{name}-%{version}.tar.gz
# Source0-md5:	1b4a0b3713b8e377baeef606f584d539
URL:		http://www.geekthing.com/~robf/gensig/
BuildRequires:	autoconf >= 2.13
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gensig is a random signature/tagline generator. It turns your
~/.signature into a FIFO, and every time it's read, it has a dif-
ferent tagline in your signature. It is very configurable and doesn't
load the whole taglines list into memory. It also reloads the taglines
list automatically if it has changed on disk and is capable of
handling multiple input files for taglines.

%description -l pl
gensig jest generatorem losowych sygnaturek pocztowych. Zmienia twój
plik ~/.signature w FIFO, w efekcie czego przy ka¿dym jego czytaniu
otrzymywana jest nowa sygnaturka. Jest mocno konfigurowalny, nie
³aduje wszystkich sygnatur do pamiêci, prze³adowuje automatycznie
listê etykiet za ka¿dym razem gdy ulegnie ona zmianie, a tak¿e
umo¿liwia pracê z wieloma plikami zawieraj±cymi linie z
sygnaturkami.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS CREDITS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gensig
%{_mandir}/man1/*
