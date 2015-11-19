%define _prefix   /

Name:		lame_svirt-selinux	
Version:	1.0.0
Release:	1%{?dist}
Summary:	SELinux Policy for lame_svirt

Group:		System Environment/Base
BuildArch:	noarch
License:	GPLv2
Requires:		policycoreutils, libselinux-utils
Requires(post):		selinux-policy-base >= %{selinux_policyver}, selinux-policy-targeted >= %{selinux_policyver}, policycoreutils, policycoreutils-python
Requires(postun):	policycoreutils
BuildRequires:		selinux-policy selinux-policy-devel
Source0: 		./lame_svirt.pp


%description
SELinux Policy module for use with svirt to make it work with contrail 


%prep

%build

%install
install -D %{S:0} %{buildroot}%{_prefix}/usr/share/selinux/packages/lame_svirt/lame_svirt.pp


%files
%dir %attr(0700, root, root) /usr/share/selinux/packages/lame_svirt/
%attr(0600, root, root) /usr/share/selinux/packages/lame_svirt/lame_svirt.pp

%post
	/usr/sbin/semodule -i /usr/share/selinux/packages/lame_svirt/lame_svirt.pp 

%postun
if [ $1 -eq 0 ]; then
	/usr/sbin/semodule -r lame_svirt
fi


%changelog

