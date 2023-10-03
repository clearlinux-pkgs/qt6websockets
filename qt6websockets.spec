#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : qt6websockets
Version  : 6.5.3
Release  : 1
URL      : https://download.qt.io/official_releases/qt/6.5/6.5.3/submodules/qtwebsockets-everywhere-src-6.5.3.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.5/6.5.3/submodules/qtwebsockets-everywhere-src-6.5.3.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6websockets-lib = %{version}-%{release}
Requires: qt6websockets-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
### Introduction
`QtWebSockets` is a pure Qt implementation of WebSockets - both client and server.
It is implemented as a Qt add-on module, that can easily be embedded into existing Qt projects. It has no other dependencies than Qt.

%package dev
Summary: dev components for the qt6websockets package.
Group: Development
Requires: qt6websockets-lib = %{version}-%{release}
Provides: qt6websockets-devel = %{version}-%{release}
Requires: qt6websockets = %{version}-%{release}

%description dev
dev components for the qt6websockets package.


%package lib
Summary: lib components for the qt6websockets package.
Group: Libraries
Requires: qt6websockets-license = %{version}-%{release}

%description lib
lib components for the qt6websockets package.


%package license
Summary: license components for the qt6websockets package.
Group: Default

%description license
license components for the qt6websockets package.


%prep
%setup -q -n qtwebsockets-everywhere-src-6.5.3
cd %{_builddir}/qtwebsockets-everywhere-src-6.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1696371930
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1696371930
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6websockets
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6websockets/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6websockets/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6websockets/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6websockets/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6websockets/f45ee1c765646813b442ca58de72e20a64a7ddba || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6websockets_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_websockets.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_websockets_private.pri
/usr/lib64/qt6/modules/WebSockets.json
/usr/lib64/qt6/qml/QtWebSockets/plugins.qmltypes
/usr/lib64/qt6/qml/QtWebSockets/qmldir

%files dev
%defattr(-,root,root,-)
/usr/include/QtWebSockets/6.5.3/QtWebSockets/private/qdefaultmaskgenerator_p.h
/usr/include/QtWebSockets/6.5.3/QtWebSockets/private/qwebsocket_p.h
/usr/include/QtWebSockets/6.5.3/QtWebSockets/private/qwebsocketcorsauthenticator_p.h
/usr/include/QtWebSockets/6.5.3/QtWebSockets/private/qwebsocketdataprocessor_p.h
/usr/include/QtWebSockets/6.5.3/QtWebSockets/private/qwebsocketframe_p.h
/usr/include/QtWebSockets/6.5.3/QtWebSockets/private/qwebsockethandshakeoptions_p.h
/usr/include/QtWebSockets/6.5.3/QtWebSockets/private/qwebsockethandshakerequest_p.h
/usr/include/QtWebSockets/6.5.3/QtWebSockets/private/qwebsockethandshakeresponse_p.h
/usr/include/QtWebSockets/6.5.3/QtWebSockets/private/qwebsocketprotocol_p.h
/usr/include/QtWebSockets/6.5.3/QtWebSockets/private/qwebsocketserver_p.h
/usr/include/QtWebSockets/QMaskGenerator
/usr/include/QtWebSockets/QWebSocket
/usr/include/QtWebSockets/QWebSocketCorsAuthenticator
/usr/include/QtWebSockets/QWebSocketHandshakeOptions
/usr/include/QtWebSockets/QWebSocketProtocol
/usr/include/QtWebSockets/QWebSocketServer
/usr/include/QtWebSockets/QtWebSockets
/usr/include/QtWebSockets/QtWebSocketsDepends
/usr/include/QtWebSockets/QtWebSocketsVersion
/usr/include/QtWebSockets/qmaskgenerator.h
/usr/include/QtWebSockets/qtwebsocketsexports.h
/usr/include/QtWebSockets/qtwebsocketsversion.h
/usr/include/QtWebSockets/qwebsocket.h
/usr/include/QtWebSockets/qwebsocketcorsauthenticator.h
/usr/include/QtWebSockets/qwebsockethandshakeoptions.h
/usr/include/QtWebSockets/qwebsocketprotocol.h
/usr/include/QtWebSockets/qwebsockets_global.h
/usr/include/QtWebSockets/qwebsocketserver.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtWebSocketsTestsConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qmlwebsocketsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qmlwebsocketsConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qmlwebsocketsConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qmlwebsocketsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qmlwebsocketsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qmlwebsocketsTargets.cmake
/usr/lib64/cmake/Qt6WebSockets/Qt6WebSocketsAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6WebSockets/Qt6WebSocketsConfig.cmake
/usr/lib64/cmake/Qt6WebSockets/Qt6WebSocketsConfigVersion.cmake
/usr/lib64/cmake/Qt6WebSockets/Qt6WebSocketsConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6WebSockets/Qt6WebSocketsDependencies.cmake
/usr/lib64/cmake/Qt6WebSockets/Qt6WebSocketsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6WebSockets/Qt6WebSocketsTargets.cmake
/usr/lib64/cmake/Qt6WebSockets/Qt6WebSocketsVersionlessTargets.cmake
/usr/lib64/libQt6WebSockets.prl
/usr/lib64/libQt6WebSockets.so
/usr/lib64/pkgconfig/Qt6WebSockets.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt6WebSockets.so.6
/usr/lib64/libQt6WebSockets.so.6.5.3
/usr/lib64/qt6/qml/QtWebSockets/libqmlwebsocketsplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6websockets/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/qt6websockets/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6websockets/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6websockets/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
/usr/share/package-licenses/qt6websockets/f45ee1c765646813b442ca58de72e20a64a7ddba