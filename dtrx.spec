Name: dtrx
Version: 7.1
Release: 13+mike1%{?dist}
Summary: Intelligent archive extractor

Group: Applications/Archiving
License: GPLv3+
URL: http://brettcsmith.org/2007/dtrx/
Source0: http://brettcsmith.org/2007/dtrx/%{name}-%{version}.tar.gz

BuildArch: noarch
#The following packages are needed for check section
BuildRequires:  lzma,ncompress,cabextract,p7zip-plugins,unshield,dpkg
BuildRequires:  %{__python2}

# The following packages are the backend tools for dtrx
Requires: bzip2
Requires: cpio
Requires: gzip
Requires: rpm
Requires: tar
Requires: lzma
Requires: ncompress
Requires: cabextract
Requires: xz
Requires: p7zip-plugins
Requires: unshield
Requires: dpkg
Requires: unzip

%description
dtrx extracts archives in a number of different formats; it currently
supports tar, zip (including self-extracting .exe files), cpio, rpm, deb,
gem, 7z, cab, rar (if unrar is installed), lhz (if lha is installed),
and InstallShield files.
It can also decompress files compressed with gzip, bzip2, lzma, xz,or compress.

In addition to providing one command to handle many different archive
types, dtrx also aids the user by extracting contents consistently.  By
default, everything will be written to a dedicated directory that's named
after the archive.  dtrx will also change the permissions to ensure that the
owner can read and write all those files.

%prep
%setup -q


%build

%install
%{__python2} setup.py install --prefix=%{buildroot}/%{_prefix}

%check
#%{__python2} tests/compare.py

%files
%{_bindir}/dtrx
%{python2_sitelib}/*
%doc NEWS README
%license COPYING


%changelog
* Mon Jun 15 2020 Mike Gerber <mike@sprachgewalt.de> - 7.1-13+mike1
- Do not run the tests (no more PyYAML for Python2 in Fedora 32)

* Thu Nov 28 2019 Mike Gerber <mike@sprachgewalt.de> - 7.1-13+mike0
- Rebuild for Fedora 31
- Depend on Python 2

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 02 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 7.1-10
- Add BR: %%{__python} (Fix F26FTBFS, RHBZ#1423343).
- Add %%license.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Sergio Belkin <sebelk@fedoraproject.org> - 7.1-2
- Removed lha dependency

* Sat Jun 23 2012 Sergio Belkin <sebelk@fedoraproject.org> - 7.1-1
- Update to 7.1
- Added support to LZH archives

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 16 2011 Sergio Belkin <sebelk@fedoraproject.org> 7.0-3
- Removed rpm and p7zip from BuildRequires according to Packaging Guidelines
- Added line between changelog entries

* Fri Mar 11 2011 Sergio Belkin <sebelk@fedoraproject.org> 7.0-2
- Removed mention to third party repository in description section

* Tue Mar 08 2011 Sergio Belkin <sebelk@fedoraproject.org> 7.0-1
- First dtrx RPM built for Fedora
