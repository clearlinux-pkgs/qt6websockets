#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v12
# autospec commit: f9eab48
#
Name     : qt6websockets
Version  : 6.7.2
Release  : 17
URL      : https://download.qt.io/official_releases/qt/6.7/6.7.2/submodules/qtwebsockets-everywhere-src-6.7.2.zip
Source0  : https://download.qt.io/official_releases/qt/6.7/6.7.2/submodules/qtwebsockets-everywhere-src-6.7.2.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6websockets-lib = %{version}-%{release}
Requires: qt6websockets-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
## Qt WebSockets
### Package Brief
`QtWebSockets` is a pure Qt implementation of WebSockets - both client and server.
It is implemented as a Qt add-on module that can easily be embedded into existing Qt projects.
Its only dependency is Qt.

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
%setup -q -n qtwebsockets-everywhere-src-6.7.2
cd %{_builddir}/qtwebsockets-everywhere-src-6.7.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1718937879
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
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
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
export SOURCE_DATE_EPOCH=1718937879
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6websockets
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6websockets/79453f55fa8ee32d7b95581473edcbfd043e088f || :
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6websockets/dc8f2e570bf431427dbc3bab9d4d551b53a60208 || :
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6websockets/7713a1753ce88f2c7e6b054ecc8e4c786df76300 || :
cp %{_builddir}/qtwebsockets-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6websockets/c70af14df11e3908dfc10397b1ba4b1f346661f3 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QtWebSockets/6.7.2/QtWebSockets/private/qdefaultmaskgenerator_p.h
/usr/include/QtWebSockets/6.7.2/QtWebSockets/private/qwebsocket_p.h
/usr/include/QtWebSockets/6.7.2/QtWebSockets/private/qwebsocketcorsauthenticator_p.h
/usr/include/QtWebSockets/6.7.2/QtWebSockets/private/qwebsocketdataprocessor_p.h
/usr/include/QtWebSockets/6.7.2/QtWebSockets/private/qwebsocketframe_p.h
/usr/include/QtWebSockets/6.7.2/QtWebSockets/private/qwebsockethandshakeoptions_p.h
/usr/include/QtWebSockets/6.7.2/QtWebSockets/private/qwebsockethandshakerequest_p.h
/usr/include/QtWebSockets/6.7.2/QtWebSockets/private/qwebsockethandshakeresponse_p.h
/usr/include/QtWebSockets/6.7.2/QtWebSockets/private/qwebsocketprotocol_p.h
/usr/include/QtWebSockets/6.7.2/QtWebSockets/private/qwebsocketserver_p.h
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
/usr/lib64/qt6/mkspecs/modules/qt_lib_websockets.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_websockets_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6WebSockets.so.6.7.2
/V3/usr/lib64/qt6/qml/QtWebSockets/libqmlwebsocketsplugin.so
/usr/lib64/libQt6WebSockets.so.6
/usr/lib64/libQt6WebSockets.so.6.7.2
/usr/lib64/qt6/metatypes/qt6websockets_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/WebSockets.json
/usr/lib64/qt6/qml/QtWebSockets/libqmlwebsocketsplugin.so
/usr/lib64/qt6/qml/QtWebSockets/plugins.qmltypes
/usr/lib64/qt6/qml/QtWebSockets/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6websockets/7713a1753ce88f2c7e6b054ecc8e4c786df76300
/usr/share/package-licenses/qt6websockets/79453f55fa8ee32d7b95581473edcbfd043e088f
/usr/share/package-licenses/qt6websockets/c70af14df11e3908dfc10397b1ba4b1f346661f3
/usr/share/package-licenses/qt6websockets/dc8f2e570bf431427dbc3bab9d4d551b53a60208
