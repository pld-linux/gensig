Summary:	Random signature generator
Summary(pl):	Generator losowych sygnatur
Name:		gensig
Version:	2.0
Release:	1
Group:		Applications/Mail
Group(pl):	Aplikacje/Poczta
Copyright:	GPL
URL:		http://www.geeks.com/~robf/gensig/
Source:		http://www.geeks.com/~robf/gensig/%{name}-%{version}.tar.gz
BuildPrereq:	rpm >= 3.0.1-4
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
gensig  is  a  random  signature/tagline generator. It turns your
~/.signature into a FIFO, and every time it's read, it has a dif-
ferent  tagline  in  your  signature. It is very configurable and
doesn't load the whole taglines list into memory. It also reloads
the  taglines list automatically if it has changed on disk and is
capable of handling multiple input files for taglines.

%description -l pl
gensig  jest  generatorem  losowych sygnatur/doklejanych etykiet.
Zmienia twój plik ~/.signature  w  FIFO,  w  efekcie  czego  przy
ka¿dym  jego czytaniu otrzymywana jest nowa sygnatura. Jest mocno
konfigurowalny, nie ³aduje wszytkich sygnatur do pamiêci, prze³a­
dowuje automatycznie listê etykiet  za  ka¿dym  razem gdy ulegnie 
ona zmianie, a tak¿e umo¿liwia pracê z wieloma plikami zawieraj±-
cymi linie z sygnaturami.

%prep
%setup -q

%build
%configureS

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog AUTHORS CREDITS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,README,ChangeLog,CREDITS,TODO}.gz

%attr(755,root,root) /usr/bin/*
/usr/share/gensig

%changelog
* Thu Apr 28 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [2.0-1]
- initial RPM release for PLD.
