Summary:	Platform independent hotkey handling for Gtk+ applications
Name:		gtkhotkey
Version:	0.2.1
Release:	0.1
License:	LGPL v3+
Group:		Libraries
Source0:	https://launchpad.net/gtkhotkey/0.2/0.2.1/+download/%{name}-%{version}.tar.gz
# Source0-md5:	bfdc73e68e9adbe0d506d31a25862914
URL:		https://launchpad.net/gtkhotkey
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Platform independent hotkey handling for Gtk+ applications.

%package devel
Summary:	Gtk Hotkey library header files for development
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Gtk Hotkey library header files for development.

%package static
Summary:	Static Gtk Hotkey library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static Gtk Hotkey library.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libgtkhotkey.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkhotkey.so.1

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/*.pc
#%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkhotkey.a
