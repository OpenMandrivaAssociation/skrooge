Name:		skrooge
Version:	1.2.0
Release:	%mkrel 1
Summary:	Personal Finance Management Tool
Source0:	http://skrooge.org/files/%{name}-%{version}.tar.bz2
Source1:	%{name}.po
Patch0:		%{name}.po.patch
Patch1:		%{name}.desktop.patch
License:	GPLv3+
Group:		Office
Url:		http://skrooge.org
BuildRequires:	kdelibs4-devel
BuildRequires:	qca2-devel
BuildRequires:	kdesdk4-scripts
BuildRequires:	sqlite3-devel
BuildRequires:	libofx-devel
BuildRequires:	desktop-file-utils
BuildRequires:	grantlee-devel
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
%{_datadir}/config/*.knsrc
%{_kde_servicetypes}/*.desktop
%{_kde_appsdir}/*
%{_kde_iconsdir}/*/*/*/*

#-----------------------------------------------------------------------------

%define libskgbankgui_major 1
%define libskgbankgui %mklibname skgbankgui %{libskgbankgui_major}

%package -n %libskgbankgui
Summary:    %name library
Group:      System/Libraries
Obsoletes:  %{_lib}skrooge1 < 0.6.1-0.1100688.2
Conflicts:  %name < 0.6.1-0.1100688.5

%description -n %libskgbankgui
%name library.

%files -n %libskgbankgui
%_kde_libdir/libskgbankgui.so.%{libskgbankgui_major}*

#-----------------------------------------------------------------------------

%define libskgbankmodeler_major 1
%define libskgbankmodeler %mklibname skgbankmodeler %{libskgbankmodeler_major}

%package -n %libskgbankmodeler
Summary:    %name library
Group:      System/Libraries
Conflicts:  %{_lib}skrooge1 < 0.6.1-0.1100688.2

%description -n %libskgbankmodeler
%name library.

%files -n %libskgbankmodeler
%_kde_libdir/libskgbankmodeler.so.%{libskgbankmodeler_major}*

#-----------------------------------------------------------------------------

%define libskgbasegui_major 1
%define libskgbasegui %mklibname skgbasegui %{libskgbasegui_major}

%package -n %libskgbasegui
Summary:    %name library
Group:      System/Libraries
Conflicts:  %{_lib}skrooge1 < 0.6.1-0.1100688.2
Conflicts:  %name < 0.6.1-0.1100688.5

%description -n %libskgbasegui
%name library.

%files -n %libskgbasegui
%_kde_libdir/libskgbasegui.so.%{libskgbasegui_major}*

#-----------------------------------------------------------------------------

%define libskgbasemodeler_major 1
%define libskgbasemodeler %mklibname skgbasemodeler %{libskgbasemodeler_major}

%package -n %libskgbasemodeler
Summary:    %name library
Group:      System/Libraries
Conflicts:  %{_lib}skrooge1 < 0.6.1-0.1100688.2

%description -n %libskgbasemodeler
%name library.

%files -n %libskgbasemodeler
%_kde_libdir/libskgbasemodeler.so.%{libskgbasegui_major}*

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
%{_kde_libdir}/*.so
%{_libdir}/grantlee/0.2/grantlee_skroogefilters.so

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
%{makeinstall_std} -C build

%check
for f in %{buildroot}%{_kde_datadir}/applications/kde4/*.desktop ; do
     desktop-file-validate $f
done 

%find_lang %name --with-html
