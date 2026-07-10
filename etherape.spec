%global _hardened_build 1
Name:           etherape
Version:        0.9.22
Release:        1%{?dist}
Summary:        Graphical network monitor for Unix

License:        GPL-2.0-or-later
URL:            https://etherape.sourceforge.net/
ExclusiveArch:  x86_64 aarch64
Source0:        https://downloads.sourceforge.net/project/etherape/etherape/%{version}/%{name}-%{version}.tar.gz
Source1:        etherape.pam
Source2:        etherape.console

BuildRequires:  libpcap-devel, libglade2-devel
BuildRequires:  gettext, desktop-file-utils, libgnomeui-devel
BuildRequires:  gnome-doc-utils
BuildRequires:  scrollkeeper
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
EtherApe is a graphical network monitor modeled after etherman.

%prep
%autosetup -p1


%build
%configure --bindir=%{_sbindir}
%make_build


%install
%make_install

mkdir -p %{buildroot}/%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/pam.d/etherape
mkdir -p %{buildroot}/%{_sysconfdir}/security/console.apps
install -m 644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/security/console.apps/etherape
mkdir -p %{buildroot}/%{_bindir}
ln -s consolehelper %{buildroot}/%{_bindir}/etherape

%find_lang %{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/etherape.desktop

%files -f %{name}.lang
%license COPYING
%doc ABOUT-NLS AUTHORS ChangeLog FAQ NEWS OVERVIEW README README.bugs TODO


%{_bindir}/etherape
%{_sbindir}/etherape
#%%dir %%{_sysconfdir}/%%{name}
#%%config(noreplace) %%{_sysconfdir}/%%{name}/services
%config(noreplace) %{_sysconfdir}/pam.d/etherape
%config(noreplace) %{_sysconfdir}/security/console.apps/etherape
%dir %{_datadir}/%{name}
%{_datadir}/gnome/help/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/etherape.desktop
%{_datadir}/pixmaps/etherape.png
%dir %{_datadir}/omf/etherape
%{_datadir}/omf/etherape/etherape-C.omf
%{_mandir}/man1/*

%post
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :

%postun
scrollkeeper-update -q || :


%changelog
* Sat Jul 05 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 0.9.22-1
- Multi-distro audit: ExclusiveArch already correct, no noarch issue, no
  stray commented BuildArch line, no EL7 macro fallback needed
- Verified BuildRequires against openSUSE/SLES pkg repos: libpcap-devel,
  gettext, desktop-file-utils are identically named, no guard needed
- libglade2-devel, libgnomeui-devel, gnome-doc-utils, scrollkeeper are not
  simple SUSE renames — they are GNOME2-era packages that are EOL/dropped
  or architecturally replaced (rarian/rarian-scrollkeeper-compat) on modern
  distros generally, not a RHEL/Fedora-vs-SUSE naming divergence; a
  %%global name-swap guard cannot fix an availability/EOL problem, so left
  unguarded pending a real upstream EOL decision for this package

* Sat Jul 04 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 0.9.22-1
- Version: 0.9.18 → 0.9.22 (latest SourceForge release)
- Source0: http→https, fix SourceForge path to /project/etherape/etherape/%{version}/; verified 302→200
- URL: http→https
- SPDX: GPLv2+ → GPL-2.0-or-later; add ExclusiveArch: x86_64 aarch64
- %%autosetup -p1, %%make_build, %%make_install, %%license COPYING

* Fri May 22 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 0.9.18-1
- Fix spec violations: %global for constants, use %{buildroot}

* Fri Apr 24 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 0.9.18-1
- Update to 0.9.18

* Fri Apr 24 2026 CasjaysDev <rpm-devel@casjaysdev.pro> - 0.9.15-4
- Modernize spec for AlmaLinux 10: remove BuildRoot, %%clean, %%defattr, Group tag

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 06 2017 Jon Ciesla <limburgher@gmail.com> - 0.9.15-1
- 0.9.15, BZ 1429169.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 06 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.14-1
- 0.9.14, BZ 1305314.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.13-1
- 0.9.13, BZ 960395.

* Mon Feb 11 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.12-6
- Drop desktop vendor tag.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Jon Ciesla <limburgher@gmail.com> - 0.9.12-4
- Add hardened build.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.12-2
- Rebuild for new libpng

* Mon Jul 18 2011 Jan F. Chadima <jchadima@redhat.com> 0.9.12-1
- Upgrade to 0.9.12

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.9.7-9
- fix license tag

* Sat Apr 19 2008 Michael Rice <errr@errr-online.com> - 0.9.7-8
- fix ln -s

* Sat Apr 19 2008 Michael Rice <errr[AT]errr-online.com> - 0.9.7-7
- Fix #442131 problems running as non root

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9.7-6
- Autorebuild for GCC 4.3

* Wed Apr 11 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-5
- Rebuild to get all matching version from FC-5 .. devel

* Mon Feb 12 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-4
- Fix desktop file install

* Sat Feb 10 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-3
- Add scrollkeeper post and postun script snips
- Fix dir ownership or pixmaps and omf
- Fix .desktop X category

* Wed Jan 31 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-2
- Fix dup BR's
- add missing BR for libgnomeui-devel scrollkeeper
- removed %%{buildroot}. in choice of other

* Wed Jan 24 2007 Michael Rice <errr[AT]errr-online.com> - 0.9.7-1
- Initial RPM release
