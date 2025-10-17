%global srcname	vinyl
%define dev DeltaCopy
%define release_tag ${TAG} # this line gets updated automatically by Github Actions

# Build a git snapshot
URL:            https://github.com/%{dev}/%{srcname}-theme
Source0:        https://github.com/%{dev}/%{srcname}-theme/archive/refs/tags/%{version}.tar.gz

Name:           %{srcname}-theme
Version:        %{release_tag}
Release:        0
Summary:        A modern style for qt applications

License:        GPLv2+ and MIT

BuildRequires:  cmake
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(KWin)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  python3dist(cairosvg) 
BuildRequires:  python3dist(lxml) 
BuildRequires:  extra-cmake-modules >= 6.13.0
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  xcursorgen
BuildRequires:  unzip

Provides:       Plasma(ColorScheme-Vinyl-Dark)
Provides:       Plasma(ColorScheme-Vinyl-Light)
Provides:       Plasma(CursorTheme-Vinyl-Black)
Provides:       Plasma(CursorTheme-Vinyl-White)
Provides:       Plasma(DesktopTheme-Vinyl)
Provides:       Plasma(KonsoleTheme-Vinyl)
Provides:       Plasma(IconTheme-Vinyl)
Provides:       Plasma(MenuLauncher-Vinyl)
Provides:       Mozilla(FirefoxTheme-Vinyl-Dark)
Provides:       Mozilla(FirefoxTheme-Vinyl-Light)
Provides:       Plasma(SDDMTheme-Vinyl)
Provides:       Plasma(Splash-Vinyl)
Provides:       Plasma(WidgetStyle-Vinyl)
Provides:       Plasma(Wallpapers-Vinyl)
Provides:       Plasma(WindowDecoration-Vinyl)

# Prevent issue github #29 on Fedora
Requires:       qt6qml(org.kde.plasma.private.quicklaunch)

%description
Vinyl is a fork of Lightly (a Breeze fork) theme style that aims to be
visually modern and minimalistic.

%prep
%setup -n %{name}-%{version}

%cmake_kf6

pushd cursors
  cp AUTHORS ../AUTHORS.cursors
  cp COPYING ../COPYING.cursors
  cp LICENSE ../LICENSE.cursors
  cp README.md ../README.cursors.md
popd


%build
%cmake_build

%install
%cmake_install \
  --prefix %{_prefix}

for variant in Black White; do
    if [ -d cursors/Vinyl-${variant} ]; then
        %{__mkdir_p} %{buildroot}%{_datadir}/icons/Vinyl-${variant} && \
        %{__cp} -av cursors/Vinyl-${variant}/* \
            %{buildroot}%{_datadir}/icons/Vinyl-${variant}/
    fi
done

%files
%license LICENSES/
%doc AUTHORS.md COPYING.md README.md

# Application style
%{_bindir}/vinyl-settings6
#{_datadir}/applications/vinylstyleconfig.desktop
#{_datadir}/icons/hicolor/scalable/apps/vinyl-settings.svg*
%{_datadir}/kstyle/themes/vinyl.themerc
%{_qt6_plugindir}/kstyle_config/vinylstyleconfig.so
%{_qt6_plugindir}/styles/vinyl6.so
%{_libdir}/cmake/Vinyl/

# Window Decoration
%dir %{_kf6_qtplugindir}/org.kde.kdecoration3.kcm
%{_kf6_qtplugindir}/org.kde.kdecoration3.kcm/kcm_vinyldecoration.so

%dir %{_kf6_qtplugindir}/org.kde.kdecoration3
%{_kf6_qtplugindir}/org.kde.kdecoration3/org.kde.vinyl.so
%{_datadir}/applications/kcm_vinyldecoration.desktop

# Colors
%{_datadir}/color-schemes/Vinyl*Dark.colors
%{_datadir}/color-schemes/Vinyl*Light.colors

# Splash
%{_datadir}/locale/*/*/plasma_lookandfeel_*.vinyl-splash.mo
%{_datadir}/metainfo/*.vinyl-splash.appdata.xml
%{_datadir}/plasma/look-and-feel/*vinyl-splash/

# Launcher
%{_datadir}/locale/*/*/plasma_applet_*.vinyl-launcher.mo
%{_datadir}/metainfo/*.vinyl-launcher.appdata.xml
%{_datadir}/plasma/plasmoids/*vinyl-launcher/

# Cursors
%doc AUTHORS.cursors README.cursors.md
%license COPYING.cursors
%license LICENSE.cursors
%{_datadir}/icons/Vinyl-Black/index.theme
%{_datadir}/icons/Vinyl-Black/cursors/
%{_datadir}/icons/Vinyl-White/index.theme
%{_datadir}/icons/Vinyl-White/cursors/

# Icons
%{_datadir}/icons/Vinyl/

# Konsole
%{_datadir}/konsole/

# Desktop Theme
%{_datadir}/plasma/desktoptheme/*

# Layout Templates
%{_datadir}/plasma/layout-templates/*
%{_datadir}/metainfo/*.vinyl.desktop.bottomPanel.appdata.xml

# Global Themes
%{_datadir}/plasma/look-and-feel/*vinyl.desktop.*
%{_datadir}/metainfo/*.vinyl.desktop.dark.appdata.xml
%{_datadir}/metainfo/*.vinyl.desktop.light.appdata.xml

# Mozilla Firefox Themes
%if %{with mozilla}
%{_datadir}/mozilla/extensions/*
%endif


# SDDM Theme
%{_datadir}/locale/*/*/sddm_theme_*.vinyl-sddm.mo
%{_datadir}/sddm/themes/*

# Wallpapers
%{_datadir}/wallpapers/Vinyl*

%changelog
%autochangelog