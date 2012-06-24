Summary:	Random signature generator
Summary(pl):	Generator losowych sygnaturek
Name:		gensig
Version:	2.2
Release:	2
Group:		Applications/Mail
Group(pt):	Aplica��es/Correio Eletr�nico
Group(pl):	Aplikacje/Poczta
License:	GPL
Source0:	http://www.geeks.com/~robf/gensig/%{name}-%{version}.tar.gz
URL:		http://www.geeks.com/~robf/gensig/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gensig is a random signature/tagline generator. It turns your
~/.signature into a FIFO, and every time it's read, it has a dif-
ferent tagline in your signature. It is very configurable and doesn't
load the whole taglines list into memory. It also reloads the taglines
list automatically if it has changed on disk and is capable of
handling multiple input files for taglines.

%description -l pl
gensig jest generatorem losowych sygnaturek pocztowych. Zmienia tw�j
plik ~/.signature w FIFO, w efekcie czego przy ka�dym jego czytaniu
otrzymywana jest nowa sygnaturka. Jest mocno konfigurowalny, nie
�aduje wszytkich sygnatur do pami�ci, prze�a� dowuje automatycznie
list� etykiet za ka�dym razem gdy ulegnie ona zmianie, a tak�e
umo�liwia prac� z wieloma plikami zawieraj�- cymi linie z
sygnaturkami.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS"
LDFLAGS="-s"
export CFLAGS LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README ChangeLog AUTHORS CREDITS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,README,ChangeLog,CREDITS,TODO}.gz
%attr(755,root,root) %{_bindir}/*

%{_datadir}/gensig
%{_mandir}/man1/*
