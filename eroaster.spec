Summary:	ECLiPt Roaster
Summary(pl):	Jeszcze jedna nak³adka tworz±ca kombajn do nagrywania CD pod Xem
Name:		eroaster
Version:	2.0.12
Release:	0.1
License:	GPL
Group:		Applications/Archiving
URL:		http://eclipt.uni-klu.ac.at
Source0:	ftp://eclipt.uni-klu.ac.at/pub/projects/%{name}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  python-pygnome
BuildRequires:  sox
BuildRequires:  mpg123
BuildRequires:  xmms
BuildRequires:	cdrtools-utils
BuildRequires:	cdrtools-mkisofs
BuildRequires:	cdrtools-cdda2wav
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ECLiPt Roaster is a frontend to cdrecord and mkisofs written in python
using the python-gnome bindings.

%description -l pl
Roaster jest nak³adk± na cdrecorda i inne cdrtoolsy. Napisany w pythonie
korzysta z bibilotek gnomowych. Bardzo przyjazny i mi³o wygl±daj±cy.

%package applet
Summary:	ECLiPt Roaster GNOME Applet
Group:		Applications/Archiving
Requires:	python-pygnome-applet
Requires:	%{name}

%description applet
Gnome applet

%description applet -l pl
Aplecik do gnoma

%prep

%setup -q
./configure --prefix=$RPM_BUILD_ROOT%{_prefix} --sysconfdir=%{_sysconfdir}

%build

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/%{_prefix} sysconfdir=$RPM_BUILD_ROOT/%{_sysconfdir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/eroaster
%{_datadir}/eroaster/pixmaps/*
%{_libdir}/eroaster/*

%files applet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/eroaster-applet
%{_datadir}/applets/Utility/eroaster.desktop
%{_datadir}/pixmaps/eroaster.xpm
%{_sysconfdir}/CORBA/servers/eroaster.gnorba
