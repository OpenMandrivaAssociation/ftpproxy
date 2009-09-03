%define name    ftpproxy
%define version 1.2.3
%define release %mkrel 6
%define Summary Application level gateway for FTP

Summary:        %Summary
Name:           %name
Version:        %version
Release:        %release
License:        GPL
Group:          Networking/File transfer
URL:            http://www.ftpproxy.org/
Source0:        %name-%version.tar.bz2
BuildRoot:      %_tmppath/%name-buildroot

%description
ftp.proxy is an application level gateway for FTP. It sits between a client and
a server forwarding command and data streams supporting a subset of the file
transfer protocol as described in RFC 959.

Beside this basic function which makes the program useful on firewall or
masqueraders it offers fixing the FTP server (e.g. for connections into a
protected LAN) and proxy authentication.

%prep
%setup -q

%build
%make

%install
rm -rf %buildroot

%__mkdir_p %{buildroot}%{_bindir}
%__cp src/ftp.proxy %{buildroot}%{_bindir}

%clean
rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%_bindir/*
%defattr(0644,root,root,0755)
%doc HISTORY INSTALL LICENSE doc/rfc2389.txt doc/rfc959.txt
%doc samples/*

