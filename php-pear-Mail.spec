%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_pearname	%{_class}
Summary:	%{_class} - Class that provides multiple interfaces for sending emails
Summary(pl):	%{_class} - Klasa daj±ca interfejsy do wysy³ania poczty
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR's Mail:: interface, defines the interface for implementing
mailers under the PEAR hierarchy, and provides supporting functions
useful in multiple mailer backends. Currently supported are native PHP
mail() function, sendmail and SMTP. This package also provides a RFC
822 Email address list validation utility class.

%description -l pl

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install *.php			$RPM_BUILD_ROOT%{php_pear_dir}/
install %{_class}/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
