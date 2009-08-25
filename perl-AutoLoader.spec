%define upstream_name    AutoLoader
%define upstream_version 5.69

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	Load subroutines only on demand
License:	GPLv2+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The AutoLoader module works with the AutoSplit module and the __END__ token to
defer the loading of some subroutines until they are used rather than loading
them all at once.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
