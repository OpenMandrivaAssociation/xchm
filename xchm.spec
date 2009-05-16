%define	name	xchm
%define version	1.16
%define docversion 1.10
%define	release	%mkrel 1

%define	Summary	CHM viewer for UNIX

Name:		%name
Version:	%version
Release:	%release
Summary:	%Summary
License:	GPLv2+
Group:		Publishing
URL:		http://xchm.sourceforge.net
Source:		http://ovh.dl.sourceforge.net/sourceforge/xchm/%name-%version.tar.gz
Source1:	%name-%docversion-doc.tar.bz2
Source2:	%name-16.png
Source3:	%name-32.png
Source4:	%name-48.png
BuildRequires:	libchm-devel
BuildRequires:	libtiff
BuildRequires:	wxgtku-devel
BuildRequires:	ghostscript
Buildrequires:	tetex-latex
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
xCHM - the CHM viewer for UNIX

%prep
%setup -q -a 1

%build
%configure2_5x --with-wx-config=%{_bindir}/wx-config-unicode
%make

%install
rm -rf %buildroot
%makeinstall_std

mkdir -p %buildroot%_iconsdir/hicolor/{16x16,32x32,48x48}/apps
%__install -m 644 %SOURCE2 %buildroot%_iconsdir/hicolor/16x16/apps/%name.png
%__install -m 644 %SOURCE3 %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
%__install -m 644 %SOURCE4 %buildroot%_iconsdir/hicolor/48x48/apps/%name.png

mkdir -p %buildroot%{_datadir}/applications
cat > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Xchm
Comment=CHM viewer for UNIX
Exec=xchm
Icon=xchm
Type=Application
Categories=GTK;Office;Viewer;
EOF

(
cd %name-%docversion-doc/latex/
make
)

# Doc are install elsewhere
rm -fr %buildroot/%_datadir/doc

%find_lang %name

%clean
rm -fr $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%doc %name-%docversion-doc/html
%doc %name-%docversion-doc/latex/*.dvi
%_bindir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/pixmaps/*.xpm
%_datadir/applications/*.desktop
