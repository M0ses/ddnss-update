#
# spec file for package ddnss-update
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           ddnss-update
Version:	0.0.1
Release:	0.0
License:	GPL
Summary:	Update script for ddnss.de
Url:		https://github.com/M0ses/ddnss-update
Group:		Productivity/Networking/DNS/Utilities
Source:		%{name}-%{version}.tar.xz
#Patch:
#BuildRequires:
#PreReq:
#Provides:
Requires:	curl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires: shadow
Requires: shadow
BuildRequires: systemd-rpm-macros
%{?systemd_requires}

%description
update script for ddnss.de 

%prep
%setup -q

%build

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}

%pre
id ddnss 2>/dev/null || useradd -r -m -d /var/lib/ddnss -c "User for updating ddnss.de records" -s /bin/bash ddnss
%service_add_pre ddnss-update.timer

%post
%service_add_post ddnss-update.timer

%preun
%service_del_preun ddnss-update.timer

%postun
%service_del_postun ddnss-update.timer

%files
%defattr(-,root,root)
%doc README.md LICENSE
%dir /etc/ddnss/
%config (noreplace) /etc/ddnss/ddnss-update.rc
/usr/bin/ddnss-update
%dir %attr(0755,ddnss,users) %ghost /var/lib/ddnss
%ghost /var/lib/ddnss/last.ip
%ghost /var/log/ddnss-update.log
%{_unitdir}/ddnss-update.service
%{_unitdir}/ddnss-update.timer
