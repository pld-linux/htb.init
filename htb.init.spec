Summary:	Shell script for setting up HTB
Summary(pl.UTF-8):	Skrypt umożliwiający prostą konfigurację HTB
Name:		htb.init
Version:	0.8.5
Release:	4
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/htbinit/%{name}-v%{version}
# Source0-md5:	1713d9a4941120235cb0721ceba6493b
Source1:	http://dl.sourceforge.net/htbinit/htb-lartc.tar.gz
# Source1-md5:	1a6e6515abfe2a48744b36b7ff9af94d
Patch0:		%{name}-lsb.patch
Patch1:		%{name}-find.patch
URL:		http://www.sourceforge.net/projects/htbinit/
Requires(post,preun):	/sbin/chkconfig
Requires:	iproute2
Requires:	rc-scripts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTB.init is a shell script derived from CBQ.init that allows for easy
setup of HTB-based traffic control on Linux. HTB (Hierachical Token
Bucket) is a new queueing discipline which attempts to address the
weaknesses of current CBQ implementation.

%description -l pl.UTF-8
HTB.init jest prostym skryptem umożliwiającym łatwą konfigurację
kontroli ruchu HTB w Linuksie 2.4 i 2.6. HTB (Hierarchical Token
Bucket) to nowy algorytm kolejkowania próbujący wyeliminować słabości
aktualnej implementacji CBQ.

%prep
%setup -q -T -c -a1
install %{SOURCE0} .
%patch0 -p0
%patch1 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/rc.d/init.d,/etc/sysconfig/htb}

install %{name}-v%{version} $RPM_BUILD_ROOT/etc/rc.d/init.d/htb

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add htb

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del htb
fi

%files
%defattr(644,root,root,755)
%doc e*
%attr(754,root,root) /etc/rc.d/init.d/htb
%dir /etc/sysconfig/htb
