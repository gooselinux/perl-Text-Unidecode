Name:           perl-Text-Unidecode
Version:        0.04
Release:        7.1%{?dist}
Summary:        US-ASCII transliterations of Unicode text

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Text-Unidecode/
Source0:        http://www.cpan.org/modules/by-module/Text/Text-Unidecode-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description

Text::Unidecode provides a function, `unidecode(...)' that
takes Unicode data and tries to represent it in US-ASCII
characters (i.e., the universally displayable characters between
0x00 and 0x7F). The representation is almost always an attempt at
*transliteration* -- i.e., conveying, in Roman letters, the
pronunciation expressed by the text in some other writing
system. 


%prep
%setup -q -n Text-Unidecode-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README TODO.txt ChangeLog
%{perl_vendorlib}/Text/
%{_mandir}/man3/*.3*


%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.04-7.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.04-5
- rebuild for new perl

* Wed Oct 17 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 0.04-4.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Tue Aug 29 2006 Patrice Dumas <pertusus at free.fr> - 0.04-4
- rebuild for FC6

* Mon Jun 26 2006 Patrice Dumas <pertusus at free.fr> - 0.04-3
- rebuild for perl-5.8.8

* Fri Feb 17 2006 Patrice Dumas <pertusus at free.fr> - 0.04-2
- rebuild for fc5

* Sun Jan 29 2006 Patrice Dumas <pertusus at free.fr> - 0.04-1
- fedora extras submission
