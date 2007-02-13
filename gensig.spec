Summary:	Random signature generator
Summary(pl.UTF-8):	Generator losowych sygnaturek
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

%description -l pl.UTF-8
gensig jest generatorem losowych sygnaturek pocztowych. Zmienia twój
plik ~/.signature w FIFO, w efekcie czego przy każdym jego czytaniu
otrzymywana jest nowa sygnaturka. Jest mocno konfigurowalny, nie
ładuje wszystkich sygnatur do pamięci, przeładowuje automatycznie
listę etykiet za każdym razem gdy ulegnie ona zmianie, a także
umożliwia pracę z wieloma plikami zawierającymi linie z
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
