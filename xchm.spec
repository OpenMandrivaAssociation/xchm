Name:		xchm
Version:	1.37
Release:	1
Summary:	CHM viewer for UNIX
License:	GPLv2+
Group:		Publishing
URL:		https://xchm.sourceforge.net
Source0:	https://github.com/rzvncj/xCHM/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:	xchm-1.37-link.patch
BuildRequires:	autoconf automake slibtool
BuildRequires:	zstd
BuildRequires:	chmlib-devel
BuildRequires:	libwxgtk3.2-devel

%description
xCHM - the CHM viewer for UNIX

%prep
%autosetup -p1

%conf
%configure --with-wx-config=%{_bindir}/wx-config-3.2

%build
%make_build

%install
%make_install

%find_lang %name

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}doc.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/xchm.appdata.xml
%{_mandir}/man1/xchm.1.zst
