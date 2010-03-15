%define svn 1100688

Name: skrooge
Version: 0.6.1
Release: %mkrel 0.%svn.1
Summary: Personal Finance Management Tool
Source0: http://websvn.kde.org/*checkout*/tags/skrooge/%{version}/%{name}-%{version}.%svn.tar.bz2
License: GPLv2+
Group: Office
Url: http://extragear.kde.org/apps/skrooge/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: qca2-devel
BuildRequires: kdesdk4-scripts
BuildRequires: sqlite3-devel
BuildRequires: libofx-devel
Requires: qt4-database-plugin-sqlite
Conflicts:  %{_lib}skrooge1 < 0.6.1

%description
Skrooge is a personal finance management tool for KDE4, with the aim of
being highly intuitive, while providing powerful functions such as
graphics, persistent Undo/Redo, infinite category levels, and much more...

%files -f %name.lang
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*.so
%{_kde_datadir}/applications/kde4/*.desktop
%{_datadir}/mime/packages/*.xml
%{_kde_datadir}/config.kcfg/*.kcfg
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop
%{_kde_appsdir}/*
%{_kde_iconsdir}/*/*/*/*
%{_kde_plugindir}/designer/*.so.*

#-----------------------------------------------------------------------------

%define libskgbankgui_major 0
%define libskgbankgui %mklibname skgbankgui %{libskgbankgui_major}

%package -n %libskgbankgui
Summary:    %name library
Group:      System/Libraries
Conflicts:  %{_lib}skrooge1 < 0.6.1

%description -n %libskgbankgui
%name library.

%files -n %libskgbankgui
%defattr(-,root,root,-)
%_kde_libdir/libskgbankgui.so.*

#-----------------------------------------------------------------------------

%define libskgbankmodeler_major 0
%define libskgbankmodeler %mklibname skgbankmodeler %{libskgbankmodeler_major}

%package -n %libskgbankmodeler
Summary:    %name library
Group:      System/Libraries
Conflicts:  %{_lib}skrooge1 < 0.6.1

%description -n %libskgbankmodeler
%name library.

%files -n %libskgbankmodeler
%defattr(-,root,root,-)
%_kde_libdir/libskgbankmodeler.so.*

#-----------------------------------------------------------------------------

%define libskgbasegui_major 0
%define libskgbasegui %mklibname skgbasegui %{libskgbasegui_major}

%package -n %libskgbasegui
Summary:    %name library
Group:      System/Libraries
Conflicts:  %{_lib}skrooge1 < 0.6.1

%description -n %libskgbasegui
%name library.

%files -n %libskgbasegui
%defattr(-,root,root,-)
%_kde_libdir/libskgbasegui.so.*

#-----------------------------------------------------------------------------

%define libskgbasemodeler_major 0
%define libskgbasemodeler %mklibname skgbasemodeler %{libskgbasemodeler_major}

%package -n %libskgbasemodeler
Summary:    %name library
Group:      System/Libraries
Conflicts:  %{_lib}skrooge1 < 0.6.1

%description -n %libskgbasemodeler
%name library.

%files -n %libskgbasemodeler
%defattr(-,root,root,-)
%_kde_libdir/libskgbasemodeler.so.*

#-----------------------------------------------------------------------------

%package devel
Summary: skrooge development files
Group: Development/KDE and Qt
Requires: %libskgbasemodeler = %{version}-%{release}
Requires: %libskgbasegui = %{version}-%{release}
Requires: %libskgbankmodeler = %{version}-%{release}
Requires: %libskgbankgui = %{version}-%{release}
Conflicts: %{name} < 0.2.3

%description devel
This package contains header files needed if you wish to build applications
based on skrooge.

%files devel
%defattr(-,root,root)
%{_kde_libdir}/*.so
%{_kde_plugindir}/designer/*.so

#--------------------------------------------------------------------

%prep
%setup -q -n %name

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build


# We copy some missing icons from oxygen to hicolor
for size in 16 22 32 48 64 128; do
    mkdir -p %buildroot/%_datadir/icons/hicolor/${size}x${size}/apps
    %__cp %buildroot%_kde_iconsdir/oxygen/${size}x${size}/apps/skrooge.png %buildroot/%_datadir/icons/hicolor/${size}x${size}/apps
done

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
