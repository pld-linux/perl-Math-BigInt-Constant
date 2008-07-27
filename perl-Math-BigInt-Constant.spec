#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	BigInt-Constant
Summary:	Math::BigInt::Constant - arbitrary sized constant integers
Summary(pl.UTF-8):	Math::BigInt::Constant - stałe całkowite o dowolnym rozmiarze
Name:		perl-Math-BigInt-Constant
Version:	1.06
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	03241d6b40f0dda51d00cf6103c156ff
BuildRequires:	perl-Math-BigInt >= 1.74
BuildRequires:	perl(Math::BigFloat) >= 1.26
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Math-BigInt >= 1.74
Requires:	perl(Math::BigFloat) >= 1.26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module lets you define constant BigInts on a per-object basis.
The usual "use Math::BigInt ':constant'" will catch all integer
constants in the script at compile time, but will not let you create
constant values on the fly, nor work for strings and/or floating point
constants like "1e5".

%description -l pl.UTF-8
Ten moduł pozwala definiować stałe BigInty dla każdego obiektu. Zwykłe
"use Math::BigInt ':constant'" wyłapie wszystkie stałe całkowite w
skrypcie w czasie kompilacji, ale nie pozwoli na tworzenie stałych
wartości w locie, ani nie będzie działać z łańcuchami czy stałymi
zmiennoprzecinkowymi typu "1e5".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES LICENSE NEW README TODO
%{perl_vendorlib}/Math/BigInt/Constant.pm
%{_mandir}/man3/*
