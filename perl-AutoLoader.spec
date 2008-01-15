%define module AutoLoader

Name:		perl-%{module}
Version:	5.64
Release:	%mkrel 2
License:	GPLv2+
Group:		Development/Perl
Summary:	Load subroutines only on demand
Url:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The AutoLoader module works with the AutoSplit module and the __END__ token to
defer the loading of some subroutines until they are used rather than loading
them all at once.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL -n INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std
mv %{buildroot}%{_mandir}/man3/AutoLoader.3pm \
   %{buildroot}%{_mandir}/man3/AutoLoader-%{version}.3pm

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/AutoLoader.pm
%{perl_vendorlib}/AutoSplit.pm
