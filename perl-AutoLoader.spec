%define upstream_name    AutoLoader
%define upstream_version 5.74
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Load subroutines only on demand
License:	GPLv2+
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/AutoLoader-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The AutoLoader module works with the AutoSplit module and the __END__ token to
defer the loading of some subroutines until they are used rather than loading
them all at once.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL -n INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
mv %{buildroot}%{_mandir}/man3/AutoLoader.3pm \
   %{buildroot}%{_mandir}/man3/AutoLoader-%{version}.3pm

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/AutoLoader.pm
%{perl_vendorlib}/AutoSplit.pm

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 5.710.0-2mdv2011.0
+ Revision: 680485
- mass rebuild

* Sun Nov 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 5.710.0-1mdv2011.0
+ Revision: 599534
- update to new version 5.71

* Tue Sep 22 2009 Jérôme Quelin <jquelin@mandriva.org> 5.700.0-1mdv2011.0
+ Revision: 447132
- update to 5.70

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 5.690.0-2mdv2010.0
+ Revision: 420978
- rebuild

* Thu Aug 20 2009 Jérôme Quelin <jquelin@mandriva.org> 5.690.0-1mdv2010.0
+ Revision: 418637
- update to 5.69

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 5.680.0-1mdv2010.0
+ Revision: 402094
- rebuild using %%perl_convert_version

* Tue Jan 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.68-1mdv2009.1
+ Revision: 325286
- update to new version 5.68

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.67-1mdv2009.1
+ Revision: 292028
- update to new version 5.67

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 5.66-2mdv2009.0
+ Revision: 268370
- rebuild early 2009.0 package (before pixel changes)

* Sat May 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 5.66-1mdv2009.0
+ Revision: 208351
- update to new version 5.66

* Tue Jan 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 5.64-2mdv2008.1
+ Revision: 151978
- new license policy
- fix mixture of tabs and spaces
- rebuild for perl-5.10.0

* Fri Dec 28 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.64-1mdv2008.1
+ Revision: 138798
- new version

* Thu Dec 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.63-2mdv2008.1
+ Revision: 138320
- rename man page to avoid conflict with perl package
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.63-1mdv2008.1
+ Revision: 109592
- import perl-AutoLoader


* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.63-1mdv2008.1
- first mdv release 


