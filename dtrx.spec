Name:    dtrx
Version: 8.7.1
Release: 1+mike0%{?dist}
Summary: Intelligent archive extractor

# GitHub tag has no "v" prefix here
%global github_tag %{version}

Group: Applications/Archiving
License: GPLv3+
URL: http://brettcsmith.org/2007/dtrx/
Source0:  https://github.com/dtrx-py/dtrx/archive/%{github_tag}.tar.gz#/%{name}-%{version}.tar.gz


BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
# pyproject-rpm-macros needs EPEL on Rocky 8
BuildRequires: pyproject-rpm-macros

BuildRequires: python3-pyyaml
BuildRequires: yq
BuildRequires: lzma
BuildRequires: ncompress
BuildRequires: cabextract
BuildRequires: p7zip-plugins
BuildRequires: wget
BuildRequires: dpkg
BuildRequires: unrar
BuildRequires: arj
BuildRequires: lzip

# Not available on Rocky
#BuildRequires: brotli

# The following packages are the backend tools for dtrx
Requires: bzip2
Requires: cpio
Requires: gzip
Requires: rpm
Requires: tar
Requires: xz
Requires: unzip
Recommends: unrar
Recommends: lzma
Recommends: p7zip-plugins
Recommends: wget
Suggests: ncompress
Suggests: cabextract
Suggests: unshield
Suggests: dpkg
Suggests: arj
Suggests: lzip

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
%autosetup

# We don't have setuptools 75 on Rocky 8-10, so fingers crossed
sed -i 's/setuptools>=75/setuptools/' pyproject.toml

# Fix project.license for Rocky 8-10's build system
%if 0%{?rhel}
sed -i 's/license = "GPL-3.0-or-later"/license = { text = "GPL-3.0-or-later" }/' pyproject.toml
%endif

# Remove unsupported tests
yq -i 'del(.[] | select(.name == "brotli"))' tests/tests.yml
yq -i 'del(.[] | select(.name == "basic .lzh"))' tests/tests.yml
yq -i 'del(.[] | select(.name == "list contents of LZH"))' tests/tests.yml
yq -i 'del(.[] | select(.name == "basic .tar.lrz"))' tests/tests.yml
yq -i 'del(.[] | select(.name == "decompressing lrzip, not interactive"))' tests/tests.yml

# Fails. Why?
yq -i 'del(.[] | select(.name == "password rar noninteractive with password"))' tests/tests.yml
yq -i 'del(.[] | select(.name == "password zip noninteractive"))' tests/tests.yml
yq -i 'del(.[] | select(.name == "download and extract"))' tests/tests.yml

# Tests report DEVELOPMENT as --version, installed RPM is fine
yq -i 'del(.[] | select(.name == "--version"))' tests/tests.yml


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%{__python3} tests/compare.py

%files
%{_bindir}/dtrx
%{python3_sitelib}/*
%doc README.md
%license COPYING



%changelog
* Mon Sep 28 2026 Mike Gerber <mike@mike-gerber.de> - 8.7.1-1+mike0
- Update to 8.7.1
- Use Python 3
- Use pyproject RPM macros
- Remove unshield dependency, make it optional
- Change some Requires to Recommends/Suggests
- Patch pyproject.toml to make it build on Rocky 8-10
- Run tests again

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
