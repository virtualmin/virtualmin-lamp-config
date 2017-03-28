Name: virtualmin-lamp-config
Summary: Configuration tool for the Virtualmin LAMP stack
Version: 6.0.0
Release: 2%{?dist}
Distribution: Virtualmin
Vendor: Virtualmin, Inc.
License: GPLv3
Obsoletes: virtualmin-base
BuildArch: noarch
Requires: webmin >= 1.831 wbm-virtual-server perl(Net::SSLeay) perl(IO::Tty) 
Source: virtualmin-lamp-config-%{version}.tar.gz

%description
A configuration script for using Virtualmin with the LAMP stack. It is part of the
Virtualmin installation system. It expects all of the packages you plan to use to
be pre-installed (this is handled by the Virtualmin install.sh script).

%prep
%setup -q

%install
mkdir -p "$RPM_BUILD_ROOT/usr/libexec/webmin/virtual-server/"
cp virtualmin-lamp-config.pl "$RPM_BUILD_ROOT/usr/libexec/webmin/virtual-server/"

%files
%attr(0755, root, root) /usr/libexec/webmin/virtual-server/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Mar 28 2017 Joe Cooper <joe@virtualmin.com> - 6.0.0-2
- Initial RPM release


