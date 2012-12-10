%define name    ftpproxy
%define version 1.2.3
%define release %mkrel 7
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-7mdv2011.0
+ Revision: 618367
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.2.3-6mdv2010.0
+ Revision: 428964
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.2.3-5mdv2009.0
+ Revision: 245448
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2.3-3mdv2008.1
+ Revision: 140731
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import ftpproxy


* Tue May 16 2006 Lenny Cartier <lenny@mandriva.com> 1.2.3-3mdk
- rebuild

* Thu Feb 10 2005 Tibor Pittich <Tibor.Pittich@mandrake.org> 1.2.3-2mdk
- rebuild

* Tue Feb 8 2005 Tibor Pittich <Tibor.Pittich@mandrake.org> 1.2.3-1mdk
- 1.2.3

* Mon Jan 5 2003 Tibor Pittich <Tibor.Pittich@mandrake.org> 1.2.2-1mdk
- initial contrib import
