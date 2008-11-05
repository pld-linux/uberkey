#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	uberkey is a keylogger for x86 systems
#Summary(pl.UTF-8):	-
Name:		uberkey
Version:	1.2
Release:	1
License:	GPL
Group:		Applications
Source0:	http://gnu.ethz.ch/linuks.mine.nu/uberkey/%{name}-%{version}.tar.gz
# Source0-md5:	5724b911650ffe9cb32f16d01a96fe9a
URL:		http://gnu.ethz.ch/linuks.mine.nu/uberkey/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uberkey is a keylogger for x86 systems.

# %description -l pl.UTF-8

%prep
%setup -q

%build
%{__make} \
	CC=%{__cc} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D uberkey   $RPM_BUILD_ROOT%{_bindir}/uberkey
install -D uberkey.8 $RPM_BUILD_ROOT%{_mandir}/man8/uberkey.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
