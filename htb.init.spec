Summary:	Shell script for setting up HTB
Summary(pl):	Skrypt umożliwiający prostą konfigurację HTB
Name:		htb.init
Version:	0.8.5
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/htbinit/%{name}-v%{version}
# Source0-md5:	1713d9a4941120235cb0721ceba6493b
URL:		http://www.sourceforge.net/projects/htbinit/
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	iproute2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTB.init is a shell script derived from CBQ.init that allows for easy
setup of HTB-based traffic control on Linux. HTB (Hierachical Token
Bucket) is a new queueing discipline which attempts to address the
weaknesses of current CBQ implementation.

%description -l pl
HTB.init jest prostym skryptem umożliwiającym konfigurację HTB w
Linuksie 2.4 i 2.6.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d}

install %{SOURCE0} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add htb.init

%postun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del htb.init
fi

%files
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%dir /etc/sysconfig/htb
