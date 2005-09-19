%include	/usr/lib/rpm/macros.php
%define		_class		Mail
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - Class that provides multiple interfaces for sending emails
Summary(pl):	%{_pearname} - Klasa daj±ca interfejsy do wysy³ania poczty
Name:		php-pear-%{_pearname}
Version:	1.1.9
Release:	1
License:	PHP/BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ce8dcb33a9ad9ea7072ca0175fd4ce8f
URL:		http://pear.php.net/package/Mail/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Net/SMTP.*)'

%description
The PEAR's Mail:: interface, defines the interface for implementing
mailers under the PEAR hierarchy, and provides supporting functions
useful in multiple mailer backends. Currently supported are native PHP
mail() function, sendmail and SMTP. This package also provides a RFC
822 Email address list validation utility class.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa Mail:: definiuje w hierarchii PEAR interfejs do implementowania
wysy³ania poczty oraz udostêpnia funkcje pomocnicze przydatne w wielu
backendach do obs³ugi poczty. Aktualnie obs³ugiwane sposoby to natywna
dla PHP funkcja mail(), sendmail oraz SMTP. Ten pakiet zawiera tak¿e
klasê sprawdzaj±c± zgodno¶æ list adresów z RFC 822.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%prep
%setup -q -c
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
