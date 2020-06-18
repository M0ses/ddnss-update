#
# spec file for package ddnss-update
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/

Name:           ddnss-update
Version:	0.0.4
Release:	0
License:	GPL-3.0-only
Summary:	Update script for ddnss.de
URL:		https://github.com/M0ses/ddnss-update
Group:		Productivity/Networking/DNS/Utilities
Source:		https://github.com/M0ses/ddnss-update/archive/%{version}/%{name}-%{version}.tar.gz
Source99:	%{name}-rpmlintrc
BuildRequires:	shadow
BuildRequires:	systemd-rpm-macros
Requires:	shadow
Requires:	perl(Config::General)
Requires:	perl(LWP::Protocol::https)
Requires:	perl(LWP::UserAgent)
BuildArch:	noarch

%{?systemd_requires}

%description
Script to update ddnss.de records.

%prep
%setup -q

%build

%install
%make_install
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcddnss-update

%pre
id ddnss 2>/dev/null || useradd -r -m -d %{_localstatedir}/lib/ddnss -c "User for updating ddnss.de records" -s /bin/bash ddnss
%service_add_pre ddnss-update.service
%service_add_pre ddnss-update.timer

%post
%service_add_post ddnss-update.service
%service_add_post ddnss-update.timer

%preun
%service_del_preun ddnss-update.service
%service_del_preun ddnss-update.timer

%postun
%service_del_postun ddnss-update.service
%service_del_postun ddnss-update.timer

%files
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/ddnss/
%config(noreplace) %{_sysconfdir}/ddnss/ddnss-update.rc
%{_bindir}/ddnss-update
%dir %attr(0755,ddnss,users) %ghost %{_localstatedir}/lib/ddnss
%ghost %{_localstatedir}/lib/ddnss/last.ip
%dir %attr(0755,ddnss,users) %{_localstatedir}/log/ddnss
%ghost %{_localstatedir}/log/ddnss/ddnss-update.log
%{_unitdir}/ddnss-update.service
%{_unitdir}/ddnss-update.timer
%{_sbindir}/rcddnss-update

%changelog
