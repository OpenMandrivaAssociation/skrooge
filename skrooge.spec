Name: skrooge
Version: 0.5.0
Release: %mkrel 1
Summary: Personal Finance Management Tool
Source0: %name-%version.tar.gz
Patch0: skrooge-0.5.0-fix-doc-installation.patch
License: GPLv2+
Group: Office
Url: http://skrooge.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: qca2-devel
BuildRequires: kdesdk4-scripts
BuildRequires: sqlite3-devel
BuildRequires: libofx-devel
Requires: qt4-database-plugin-sqlite

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
%_datadir/doc/HTML/en/doc/*

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
%patch0 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build


%find_lang %name --with-html

%clean
rm -rf %{buildroot}
