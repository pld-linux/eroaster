%include        /usr/lib/rpm/macros.python
Summary:	ECLiPt Roaster
Summary(pl):	Jeszcze jedna nak�adka tworz�ca kombajn do nagrywania CD pod Xem
Name:		eroaster
Version:	2.2.0
Release:	0.3
License:	GPL
Group:		Applications/Archiving
URL:		http://eclipt.uni-klu.ac.at/
Source0:	ftp://eclipt.uni-klu.ac.at/pub/projects/eroaster/snapshots/%{name}-%{version}-%{release}.tar.gz
# Source0-md5:	58b86d7a0a553445359cce2f9eec8061
BuildRequires:	cdrtools
BuildRequires:	cdrtools-cdda2wav
BuildRequires:	cdrtools-mkisofs
BuildRequires:	cdrtools-utils
BuildRequires:	mpg123
BuildRequires:	python
BuildRequires:	python-gnome-ui >= 1.99.15
BuildRequires:	python-pygtk
BuildRequires:	rpm-pythonprov
BuildRequires:	sox
BuildRequires:	xmms
Requires:	cdrtools
Requires:	cdrtools-cdda2wav
Requires:	cdrtools-mkisofs
Requires:	cdrtools-readcd
Requires:	cdrtools-utils
Requires:	mpg123
Requires:	normalize
%pyrequires_eq	python
Requires:	python-pygtk
Requires:	sox
Requires:	xmms
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ECLiPt Roaster is a frontend to cdrecord and mkisofs written in python
using the python-gnome bindings.

%description -l pl
Roaster jest nak�adk� na cdrecorda i inne cdrtoolsy. Napisany w
pythonie korzysta z bibilotek gnomowych. Bardzo przyjazny i mi�o
wygl�daj�cy.

%package applet
Summary:	ECLiPt Roaster GNOME Applet
Summary(pl):	Kombajn do nagrywania p�yt CD - GNOME Applet
Group:		Applications/Archiving
Requires:	python-pygtk
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
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir} \
	appletdir=$RPM_BUILD_ROOT%{_applnkdir}/Utilities/CD-RW \
	deskpixdir=$RPM_BUILD_ROOT%{_pixmapsdir}

%py_ocomp $RPM_BUILD_ROOT%{_libdir}/%{name}
%py_comp $RPM_BUILD_ROOT%{_libdir}/%{name}

rm -f doc/COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/eroaster
%{_datadir}/%{name}
%{_libdir}/%{name}/*.py[co]
%{_libdir}/%{name}/ecat.py
%{_libdir}/%{name}/*.shortcuts
%{_libdir}/%{name}/glade/*.glade
%{_libdir}/%{name}/xml/*.xml
%{_pixmapsdir}/*.xpm
%{_applnkdir}/Utilities/CD-RW/*.desktop

%files applet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eroaster-applet
%{_sysconfdir}/CORBA/servers/eroaster.gnorba
