Name:		skrooge
Version:	0.9.0
Release:	4
Summary:	Personal Finance Management Tool
License:	GPLv3+
Group:		Office
Url:		http://skrooge.org
Source0:	http://skrooge.org/files/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	qca2-devel
BuildRequires:	kdesdk4-scripts
BuildRequires:	sqlite3-devel
BuildRequires:	libofx-devel
BuildRequires:  desktop-file-utils
Requires:	qt4-database-plugin-sqlite
Requires:	qca2-plugin-openssl
Conflicts:	%{_lib}skrooge1 < 0.6.1-0.1100688.2


%description
Skrooge is a personal finance management tool for KDE4, with the aim of
being highly intuitive, while providing powerful functions such as
graphics, persistent Undo/Redo, infinite category levels, and much more...

%files -f %name.lang
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*.so
%{_kde_datadir}/applications/kde4/*.desktop
%{_datadir}/mime/packages/*.xml
%{_kde_datadir}/config.kcfg/*.kcfg
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop
%{_kde_appsdir}/*
%{_kde_iconsdir}/*/*/*/*

#-----------------------------------------------------------------------------

%define libskgbankgui_major 0
%define libskgbankgui %mklibname skgbankgui %{libskgbankgui_major}

%package -n %{libskgbankgui}
Summary:    %name library
Group:      System/Libraries
Obsoletes:  %{_lib}skrooge1 < 0.6.1-0.1100688.2
Conflicts:  %{name} < 0.6.1-0.1100688.5

%description -n %{libskgbankgui}
%{name} library.

%files -n %{libskgbankgui}
%{_kde_libdir}/libskgbankgui.so.%{libskgbankgui_major}*
%{_kde_libdir}/kde4/plugins/designer/libskgbankgui.so.%{libskgbankgui_major}*

#-----------------------------------------------------------------------------

%define libskgbankmodeler_major 0
%define libskgbankmodeler %mklibname skgbankmodeler %{libskgbankmodeler_major}

%package -n %{libskgbankmodeler}
Summary:	%{name} library
Group:		System/Libraries
Conflicts:	%{_lib}skrooge1 < 0.6.1-0.1100688.2

%description -n %{libskgbankmodeler}
%{name} library.

%files -n %{libskgbankmodeler}
%{_kde_libdir}/libskgbankmodeler.so.%{libskgbankmodeler_major}*

#-----------------------------------------------------------------------------

%define libskgbasegui_major 0
%define libskgbasegui %mklibname skgbasegui %{libskgbasegui_major}

%package -n %{libskgbasegui}
Summary:	%{name} library
Group:		System/Libraries
Conflicts:	%{_lib}skrooge1 < 0.6.1-0.1100688.2
Conflicts:	%{name} < 0.6.1-0.1100688.5

%description -n %{libskgbasegui}
%{name} library.

%files -n %{libskgbasegui}
%{_kde_libdir}/libskgbasegui.so.%{libskgbasegui_major}*
%{_kde_libdir}/kde4/plugins/designer/libskgbasegui.so.%{libskgbasegui_major}*

#-----------------------------------------------------------------------------

%define libskgbasemodeler_major 0
%define libskgbasemodeler %mklibname skgbasemodeler %{libskgbasemodeler_major}

%package -n %{libskgbasemodeler}
Summary:	%{name} library
Group:		System/Libraries
Conflicts:	%{_lib}skrooge1 < 0.6.1-0.1100688.2

%description -n %{libskgbasemodeler}
%{name} library.

%files -n %{libskgbasemodeler}
%{_kde_libdir}/libskgbasemodeler.so.%{libskgbasegui_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Skrooge development files
Group:		Development/KDE and Qt
Requires:	%{libskgbasemodeler} = %{version}-%{release}
Requires:	%{libskgbasegui} = %{version}-%{release}
Requires:	%{libskgbankmodeler} = %{version}-%{release}
Requires:	%{libskgbankgui} = %{version}-%{release}
Conflicts:	%{name} < 0.2.3

%description devel
This package contains header files needed if you wish to build applications
based on skrooge.

%files devel
%{_kde_libdir}/*.so
%{_kde_plugindir}/designer/*.so

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%check
for f in %{buildroot}%{_kde_datadir}/applications/kde4/*.desktop ; do
     desktop-file-validate $f
done 

%find_lang %{name} --with-html

%changelog
* Thu Jun 09 2011 Funda Wang <fwang@mandriva.org> 0.9.0-1mdv2011.0
+ Revision: 683512
- new version 0.9.0

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.1-2
+ Revision: 669984
- mass rebuild

  + Funda Wang <fwang@mandriva.org>
    - new version 0.8.1

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 0.8.0-1
+ Revision: 633989
- update to new version 0.8.0

* Tue Sep 07 2010 Funda Wang <fwang@mandriva.org> 0.7.3-1mdv2011.0
+ Revision: 576560
- update to new version 0.7.3

* Fri Aug 06 2010 Jerome Martin <jmartin@mandriva.org> 0.7.2-1mdv2011.0
+ Revision: 566669
- Release 0.7.2

  + John Balcaen <mikala@mandriva.org>
    - Add qca2-plugin-openssl as Requires (it's needed on runtime)

* Sun Jul 11 2010 Funda Wang <fwang@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 550639
- update to new version 0.7.1

* Fri Apr 09 2010 Funda Wang <fwang@mandriva.org> 0.7.0-1mdv2010.1
+ Revision: 533496
- New version 0.7.0

* Sat Apr 03 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.1-0.1100688.5mdv2010.1
+ Revision: 530882
- Fix file list
  Add conflicts to ease upgrade
- Fix regarding new kde packaging policy

* Thu Mar 18 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.1-0.1100688.4mdv2010.1
+ Revision: 524903
- Fix update

* Tue Mar 16 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.1-0.1100688.3mdv2010.1
+ Revision: 521075
- Fix conflicts versionnate

* Tue Mar 16 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.1-0.1100688.2mdv2010.1
+ Revision: 520682
- Add patch0 to fix soname
  Use major macros in file lists
- Fix lib package to follow KDE packaging std

* Mon Mar 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.1-0.1100688.1mdv2010.1
+ Revision: 515787
- Update to svn snapshot ( add KMymoney import/export )

* Sat Feb 06 2010 Jerome Martin <jmartin@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 501387
- Version 0.6.0

* Mon Jan 18 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.5.5-2mdv2010.1
+ Revision: 493136
- Add missing icons in hicolor

* Tue Dec 01 2009 Funda Wang <fwang@mandriva.org> 0.5.5-1mdv2010.1
+ Revision: 472294
- new version 0.5.5

* Tue Nov 24 2009 Funda Wang <fwang@mandriva.org> 0.5.4-1mdv2010.1
+ Revision: 469411
- new version 0.5.4

* Fri Nov 06 2009 Funda Wang <fwang@mandriva.org> 0.5.3-1mdv2010.1
+ Revision: 460549
- New version 0.5.3

* Thu Oct 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.5.2-2mdv2010.0
+ Revision: 457523
- Obsolete KMymoney2 for the moment ( this will be removed when we will have it back )

* Fri Oct 09 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.2-1mdv2010.0
+ Revision: 456416
- Update to new version 0.5.2

* Tue Sep 22 2009 Funda Wang <fwang@mandriva.org> 0.5.1-1mdv2010.0
+ Revision: 447105
- New version 0.5.1

  + Thierry Vignaud <tv@mandriva.org>
    - fix file list

* Wed Sep 09 2009 Funda Wang <fwang@mandriva.org> 0.5.0-1mdv2010.0
+ Revision: 435256
- fix doc installation

* Wed Jun 03 2009 Funda Wang <fwang@mandriva.org> 0.2.9-1mdv2010.0
+ Revision: 382448
- fix desktop installation
- New version 0.2.9

* Tue May 05 2009 Funda Wang <fwang@mandriva.org> 0.2.8-1mdv2010.0
+ Revision: 372038
- New version 0.2.8

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 0.2.7-1mdv2010.0
+ Revision: 369672
- New version 0.2.7

* Fri Mar 20 2009 Funda Wang <fwang@mandriva.org> 0.2.5-1mdv2009.1
+ Revision: 358276
- New version 0.2.5

* Wed Mar 04 2009 Funda Wang <fwang@mandriva.org> 0.2.4-1mdv2009.1
+ Revision: 348414
- BR ofx
- New version 0.2.4

* Wed Feb 25 2009 Funda Wang <fwang@mandriva.org> 0.2.3-1mdv2009.1
+ Revision: 344625
- New version 0.2.3

* Fri Feb 13 2009 Funda Wang <fwang@mandriva.org> 0.2.2-1mdv2009.1
+ Revision: 340165
- new version 0.2.2

* Mon Feb 02 2009 Funda Wang <fwang@mandriva.org> 0.2.1-1mdv2009.1
+ Revision: 336323
- BR qca2
- New version 0.2.1

* Wed Jan 21 2009 Funda Wang <fwang@mandriva.org> 0.2.0-2mdv2009.1
+ Revision: 332301
- add requires

* Mon Jan 19 2009 Funda Wang <fwang@mandriva.org> 0.2.0-1mdv2009.1
+ Revision: 331080
- New version 0.2.0

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 0.1.9-1mdv2009.1
+ Revision: 324714
- fix file list
- New verison 0.1.9

* Tue Dec 23 2008 Funda Wang <fwang@mandriva.org> 0.1.8-1mdv2009.1
+ Revision: 317759
- drop wrong desktop file
- new version 0.1.8

* Tue Dec 16 2008 Funda Wang <fwang@mandriva.org> 0.1.7-1mdv2009.1
+ Revision: 314710
- New version 0.1.7

* Tue Dec 02 2008 Funda Wang <fwang@mandriva.org> 0.1.6-1mdv2009.1
+ Revision: 308955
- new version 0.1.6

* Tue Nov 25 2008 Funda Wang <fwang@mandriva.org> 0.1.5-1mdv2009.1
+ Revision: 306525
- fix url
- import skrooge


