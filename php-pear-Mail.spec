%define		pearname Mail
Summary:	%{pearname} - Class that provides multiple interfaces for sending emails
Summary(pl.UTF-8):	%{pearname} - Klasa dająca interfejsy do wysyłania poczty
Name:		php-pear-%{pearname}
Version:	1.4.1
Release:	1
License:	PHP/BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	23dd52d1323485d1e5f81c0816cd06cc
URL:		http://pear.php.net/package/Mail/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php-pear >= 4:1.3-6
Suggests:	php-pear-Net_SMTP
Obsoletes:	php-pear-Mail-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq_pear Net/SMTP.*

%description
The PEAR's Mail:: interface, defines the interface for implementing
mailers under the PEAR hierarchy, and provides supporting functions
useful in multiple mailer backends. Currently supported are native PHP
mail() function, sendmail and SMTP. This package also provides a RFC
822 Email address list validation utility class.

%description -l pl.UTF-8
Klasa Mail:: definiuje w hierarchii PEAR interfejs do implementowania
wysyłania poczty oraz udostępnia funkcje pomocnicze przydatne w wielu
backendach do obsługi poczty. Aktualnie obsługiwane sposoby to natywna
dla PHP funkcja mail(), sendmail oraz SMTP. Ten pakiet zawiera także
klasę sprawdzającą zgodność list adresów z RFC 822.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Mail.php
%{php_pear_dir}/Mail/*
