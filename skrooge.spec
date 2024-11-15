%ifarch %{arm} %{armx}
# /usr/bin/ld: error: /usr/lib64/libqca-qt5.so.2.1.3: bad symbol name offset 111989914 at 0
%global optflags %{optflags} -fuse-ld=bfd
%endif

%define __noautoprovfiles designer\/libskg.*gui.so*

Summary:	Personal Finance Management Tool
Name:		skrooge
Version:	2.33.0
Release:	1
License:	GPLv3+
Group:		Office
Url:		https://skrooge.org
Source0:	https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5JobWidgets)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5DesignerPlugin)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:	cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Script)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Designer)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Concurrent)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Grantlee5)
BuildRequires:  cmake(Qt5XmlPatterns)
BuildRequires:	pkgconfig(libofx)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(sqlcipher)
BuildRequires:	shared-mime-info
Requires:	qt5-database-plugin-sqlite
Requires:	grantlee
# uses during version checking
Requires:	sqlcipher

%description
Skrooge is a personal finance management tool for KDE4, with the aim of
being highly intuitive, while providing powerful functions such as
graphics, persistent Undo/Redo, infinite category levels, and much more...

%files -f %{name}.lang
%{_kde5_bindir}/*
%{_kde5_applicationsdir}/*.desktop
%{_kde5_datadir}/config.kcfg/*.kcfg
%{_kde5_iconsdir}/*/*/*/*
%{_kde5_services}/*.desktop
%{_kde5_services}/sources/*.desktop
%{_kde5_servicetypes}/*.desktop
%{_kde5_datadir}/%{name}
%{_kde5_xmlguidir}/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/metainfo/org.kde.skrooge.appdata.xml
%{_qt5_plugindir}/grantlee/5.*/*.so
%{_qt5_plugindir}/skg_gui/
%{_qt5_plugindir}/skrooge/import/
%{_qt5_plugindir}/sqldrivers/*.so
%{_datadir}/knotifications5/*
%{_datadir}/knsrcfiles/skrooge_monthly.knsrc
%{_datadir}/knsrcfiles/skrooge_unit.knsrc

#-----------------------------------------------------------------------------

%define libskgbankgui_major 2
%define libskgbankgui %mklibname skgbankgui %{libskgbankgui_major}

%package -n %{libskgbankgui}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libskgbankgui}
%{name} library.

%files -n %{libskgbankgui}
%{_kde5_libdir}/libskgbankgui.so.%{libskgbankgui_major}*

#-----------------------------------------------------------------------------

%define libskgbankmodeler_major 2
%define libskgbankmodeler %mklibname skgbankmodeler %{libskgbankmodeler_major}

%package -n %{libskgbankmodeler}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libskgbankmodeler}
%{name} library.

%files -n %{libskgbankmodeler}
%{_kde5_libdir}/libskgbankmodeler.so.%{libskgbankmodeler_major}*

#-----------------------------------------------------------------------------

%define libskgbasegui_major 2
%define libskgbasegui %mklibname skgbasegui %{libskgbasegui_major}

%package -n %{libskgbasegui}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libskgbasegui}
%{name} library.

%files -n %{libskgbasegui}
%{_kde5_libdir}/libskgbasegui.so.%{libskgbasegui_major}*

#-----------------------------------------------------------------------------

%define libskgbasemodeler_major 2
%define libskgbasemodeler %mklibname skgbasemodeler %{libskgbasemodeler_major}

%package -n %{libskgbasemodeler}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libskgbasemodeler}
%{name} library.

%files -n %{libskgbasemodeler}
%{_kde5_libdir}/libskgbasemodeler.so.%{libskgbasegui_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Skrooge development files
Group:		Development/KDE and Qt
Requires:	%{libskgbasemodeler} = %{EVRD}
Requires:	%{libskgbasegui} = %{EVRD}
Requires:	%{libskgbankmodeler} = %{EVRD}
Requires:	%{libskgbankgui} = %{EVRD}

%description devel
This package contains header files needed if you wish to build applications
based on skrooge.

%files devel
%{_qt5_plugindir}/designer/*.so*
#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html

