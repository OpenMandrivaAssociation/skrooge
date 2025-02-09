%ifarch %{arm} %{armx}
# /usr/bin/ld: error: /usr/lib64/libqca-qt5.so.2.1.3: bad symbol name offset 111989914 at 0
%global optflags %{optflags} -fuse-ld=bfd
%endif

%define __noautoprovfiles designer\/libskg.*gui.so*

Summary:	Personal Finance Management Tool
Name:		skrooge
Version:	25.1.0
Release:	2
License:	GPLv3+
Group:		Office
Url:		https://skrooge.org
Source0:	https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Runner)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6StatusNotifierItem)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(PlasmaActivities)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	pkgconfig(libofx)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(sqlcipher)
BuildRequires:	shared-mime-info
Requires:	qt6-qtbase-sql-sqlite
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
%{_kde5_datadir}/%{name}
%{_kde5_xmlguidir}/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/metainfo/org.kde.skrooge.appdata.xml
%{_libdir}/qt6/plugins/kf6/ktexttemplate/grantlee_skgfilters.so
%{_libdir}/qt6/plugins/skg_gui/
%{_libdir}/qt6/plugins/sqldrivers/*.so
%{_libdir}/qt6/plugins/skrooge_import/
%{_datadir}/knotifications6/*
%{_datadir}/knsrcfiles/skrooge_monthly.knsrc
%{_datadir}/knsrcfiles/skrooge_unit.knsrc
%{_datadir}/skrooge_import_backend/
%{_datadir}/skrooge_source/

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
#--------------------------------------------------------------------

%prep
%autosetup -p1
%cmake -DQT_MAJOR_VERSION=6 -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-html

