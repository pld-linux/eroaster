%include        /usr/lib/rpm/macros.python
Summary:	ECLiPt Roaster
Summary(pl):	Jeszcze jedna nak³adka tworz±ca kombajn do nagrywania CD pod Xem
Name:		eroaster
Version:	2.1.0
Release:	0.1
License:	GPL
Group:		Applications/Archiving
URL:		http://eclipt.uni-klu.ac.at
Source0:	http://prdownloads.sourceforge.net/eroaster/eroaster-2.1.0.tar.gz
BuildRequires:	python
BuildRequires:	python-pygnome
BuildRequires:	sox
BuildRequires:	mpg123
BuildRequires:	xmms
BuildRequires:	cdrtools
BuildRequires:	cdrtools-utils
BuildRequires:	cdrtools-mkisofs
BuildRequires:	cdrtools-cdda2wav
BuildRequires:  rpm-pythonprov
%pyrequires_eq	python
Requires:	python-pygnome
Requires:	sox
Requires:	mpg123
Requires:	xmms
Requires:	cdrtools
Requires:	cdrtools-utils
Requires:	cdrtools-mkisofs
Requires:	cdrtools-cdda2wav
Requires:	cdrtools-readcd
Requires:	normalize
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ECLiPt Roaster is a frontend to cdrecord and mkisofs written in python
using the python-gnome bindings.

%description -l pl
Roaster jest nak³adk± na cdrecorda i inne cdrtoolsy. Napisany w
pythonie korzysta z bibilotek gnomowych. Bardzo przyjazny i mi³o
wygl±daj±cy.

%package applet
Summary:	ECLiPt Roaster GNOME Applet
Summary(pl):	Kombajn do nagrywania p³yt CD - GNOME Applet
Group:		Applications/Archiving
Requires:	python-pygnome-applet
Requires:	%{name}

%description applet
Gnome applet - small icon to add it to "quick lunch" menubar.

%description applet -l pl
Aplecik do gnoma - pozwala na "szybkie uruchomienie" eroastera.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT/%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT/%{_sysconfdir} \
	appletdir=$RPM_BUILD_ROOT%{_applnkdir}/Utilities/CD-RW \
	deskpixdir=$RPM_BUILD_ROOT%{_pixmapsdir}

%py_ocomp $RPM_BUILD_ROOT%{_libdir}/%{name}
%py_comp $RPM_BUILD_ROOT%{_libdir}/%{name}

rm -f doc/COPYING
gzip -9nf doc/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.gz
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/eroaster
%{_datadir}/%{name}
%{_libdir}/%{name}/*.py[co]
%{_libdir}/%{name}/ecat.py
%{_libdir}/%{name}/*.shortcuts
%{_pixmapsdir}/*.xpm
%{_applnkdir}/Utilities/CD-RW/*.desktop

%files applet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eroaster-applet
%{_sysconfdir}/CORBA/servers/eroaster.gnorba
