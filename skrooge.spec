Summary:	Personal Finance Management Tool
Name:		skrooge
Version: 	0.1.7
Release: 	%mkrel 1
Source0: 	http://downloads.sourceforge.net/skrooge/%name-%version.tar.gz
License: 	GPLv2+
Group: 		Office
Url: 		http://skrooge.sourceforge.net/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	kdelibs4-devel
BuildRequires:	kdesdk4-scripts
BuildRequires:	sqlite3-devel

%description
Skrooge is a personal finance management tool for KDE4, with the aim of
being highly intuitive, while providing powerful functions such as
graphics, persistent Undo/Redo, infinite category levels, and much more...

%if %mdkversion < 200900
%post
%update_menus

%postun
%update_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_libdir}/*.so
%{_kde_libdir}/kde4/*.so
%{_kde_plugindir}/designer/*.so
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_datadir}/config.kcfg/*.kcfg
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop
%{_kde_datadir}/mimelnk/application/skg.desktop
%{_kde_appsdir}/*
%{_kde_iconsdir}/*/*/*/*

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
chmod a+x po/*.sh
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
