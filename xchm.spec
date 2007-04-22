%define	name	xchm
%define version	1.13
%define docversion 1.10
%define	release	%mkrel 3

%define	section	Office/Publishing
%define	title	Xchm

%define	Summary	CHM viewer for UNIX

Name:		%name
Version:	%version
Release:	%release
Summary:	%Summary
License:	GPL
Group:		Publishing
URL:		http://xchm.sourceforge.net
Source:		%name-%version.tar.bz2
Source1:	%name-%docversion-doc.tar.bz2
Source2:	%name-16.png
Source3:	%name-32.png
Source4:	%name-48.png
BuildRequires:	libchm-devel
BuildRequires:	libtiff
BuildRequires:	wxGTK-devel >= 2.6
BuildRequires:	wxGTK-devel < 2.7
BuildRequires:	ghostscript
Buildrequires:	tetex-latex
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
xCHM - the CHM viewer for UNIX

%prep
%setup -q -a 1

%build
%configure --with-wx-config=%{_bindir}/wx-config-ansi
%make

%install
rm -rf %buildroot
%makeinstall_std

mkdir -p %buildroot{%_miconsdir,%_iconsdir,%_liconsdir}
%__install -m 644 %SOURCE2 %buildroot%_miconsdir/%name.png
%__install -m 644 %SOURCE3 %buildroot%_iconsdir/%name.png
%__install -m 644 %SOURCE4 %buildroot%_liconsdir/%name.png

# menu
%__mkdir_p %buildroot%_menudir
cat > %buildroot%_menudir/%name << EOF
?package(%name): \
command="%_bindir/%name" \
needs="x11" \
icon="%name.png" \
section="%section" \
title="%title" \
longtitle="%Summary"
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

%post
%update_menus

%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%doc %name-%docversion-doc/html
%doc %name-%docversion-doc/latex/*.dvi
%_bindir/%name
%_menudir/%name
%_liconsdir/%name.png
%_iconsdir/%name.png
%_miconsdir/%name.png
%_datadir/pixmaps/*.xpm


