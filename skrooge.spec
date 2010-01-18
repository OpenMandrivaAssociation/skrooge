Name: skrooge
Version: 0.5.5
Release: %mkrel 2
Summary: Personal Finance Management Tool
Source0: http://websvn.kde.org/*checkout*/tags/skrooge/%{version}/%{name}-%{version}.tar.bz2
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

# We add this obsolete during the time we have not kmymoney2
Obsoletes: kmymoney2 < 1.0.0-0.1013464.2

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

#-------------------------------------------------------------------

%define major 1
%define libname %mklibname skrooge %major

%package -n %libname
Summary: skrooge library
Group: System/Libraries

%description -n %libname
Skrooge library.

%files -n %libname
%defattr(-,root,root)
%{_kde_libdir}/*.so.%{major}
%{_kde_libdir}/*.so.%{version}
%{_kde_plugindir}/designer/*.so.%{major}
%{_kde_plugindir}/designer/*.so.%{version}

#-------------------------------------------------------------------

%package devel
Summary: skrooge development files
Group: Development/KDE and Qt
Requires: %{libname} = %{version}-%{release}
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
%setup -q

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
    %__cp %buildroot%_kde_iconsdir/oxygen/${size}x${size}/apps/skrooge2.png %buildroot/%_datadir/icons/hicolor/${size}x${size}/apps
done

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
