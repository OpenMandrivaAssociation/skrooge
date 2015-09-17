Summary:	Personal Finance Management Tool
Name:		skrooge
Version:	1.12.5
Release:	0.1
License:	GPLv3+
Group:		Office
Url:		http://skrooge.org
Source0:	http://skrooge.org/files/%{name}-%{version}.tar.xz
BuildRequires:	grantlee
BuildRequires:	grantlee-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepim4-devel
BuildRequires:	pkgconfig(libkactivities)
BuildRequires:	pkgconfig(libofx)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(sqlite3)
Requires:	qt4-database-plugin-sqlite
Requires:	qca2-plugin-openssl
Requires:	grantlee

%description
Skrooge is a personal finance management tool for KDE4, with the aim of
being highly intuitive, while providing powerful functions such as
graphics, persistent Undo/Redo, infinite category levels, and much more...

%files -f %{name}.lang
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*.so
%{_kde_libdir}/kde4/plugins/grantlee
%{_kde_appsdir}/*
%{_kde_applicationsdir}/*.desktop
%{_kde_datadir}/config.kcfg/*.kcfg
%{_kde_configdir}/*.knsrc
%{_kde_iconsdir}/*/*/*/*
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/akonadi/agents/skroogeakonadiresource.desktop
%{_datadir}/appdata/skrooge.appdata.xml

#-----------------------------------------------------------------------------

%define libskgbankgui_major 1
%define libskgbankgui %mklibname skgbankgui %{libskgbankgui_major}

%package -n %{libskgbankgui}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libskgbankgui}
%{name} library.

%files -n %{libskgbankgui}
%{_kde_libdir}/libskgbankgui.so.%{libskgbankgui_major}*

#-----------------------------------------------------------------------------

%define libskgbankmodeler_major 1
%define libskgbankmodeler %mklibname skgbankmodeler %{libskgbankmodeler_major}

%package -n %{libskgbankmodeler}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libskgbankmodeler}
%{name} library.

%files -n %{libskgbankmodeler}
%{_kde_libdir}/libskgbankmodeler.so.%{libskgbankmodeler_major}*

#-----------------------------------------------------------------------------

%define libskgbasegui_major 1
%define libskgbasegui %mklibname skgbasegui %{libskgbasegui_major}

%package -n %{libskgbasegui}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libskgbasegui}
%{name} library.

%files -n %{libskgbasegui}
%{_kde_libdir}/libskgbasegui.so.%{libskgbasegui_major}*

#-----------------------------------------------------------------------------

%define libskgbasemodeler_major 1
%define libskgbasemodeler %mklibname skgbasemodeler %{libskgbasemodeler_major}

%package -n %{libskgbasemodeler}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libskgbasemodeler}
%{name} library.

%files -n %{libskgbasemodeler}
%{_kde_libdir}/libskgbasemodeler.so.%{libskgbasegui_major}*

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
%{_kde_libdir}/*.so

#--------------------------------------------------------------------

%prep
%setup -q

%build
#need bespoke pkg path due to qt4/5 split
export PKG_CONFIG_PATH=%{_libdir}/qt4/pkgconfig
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-html

