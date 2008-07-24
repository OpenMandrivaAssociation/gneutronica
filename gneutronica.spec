%define name	gneutronica
%define version 0.33
%define release %mkrel 5

Name: 	 	%{name}
Summary: 	A GNOME-based MIDI drum sequencer
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/gneutronica/%{name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/gneutronica/

License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libgnomecanvas2-devel ImageMagick libalsa-devel

%description
This program is MIDI drum machine software for linux with a gnome based user
interface to allow easy creation and play back of drum tracks to external MIDI
devices.

%prep
%setup -q
perl -p -i -e "s|gcc|gcc $RPM_OPT_FLAGS||g" Makefile

%build
make
					
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
cp %name %buildroot/%_bindir
mkdir -p %buildroot/%_datadir/%name
cp -r drumkits %buildroot/%_datadir/%name
mkdir -p %buildroot/%_mandir/man1
bzip2 < documentation/%name.1 > %buildroot/%_mandir/man1/%name.1.bz2
mkdir -p %buildroot/%_datadir/pixmaps
cp icons/*.png %buildroot/%_datadir/pixmaps

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Gneutronica
Comment=MIDI drum sequencer
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Midi;
Encoding=UTF-8
EOF


#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 icons/gneutronica_icon.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 icons/gneutronica_icon.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 icons/gneutronica_icon.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc BUGS CHANGES documentation/*.png documentation/*.html
%{_bindir}/%name
%{_mandir}/man1/*
%{_datadir}/pixmaps/*
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

