%define name rubber
%define version 1.1
%define release %mkrel 7

Name:		%name
Summary:	An automated system for building LaTeX documents
Version:	%version
Release:	%release
Source:		http://ebeffara.free.fr/pub/%name-%version.tar.bz2
URL:		http://www.pps.jussieu.fr/~beffara/soft/rubber/
License:	GPL
Group:		Publishing
Requires:	tetex
%py_requires -d
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  texinfo
BuildArch: noarch

%description
This is a building system for LaTeX documents. It is based on a routine that
runs just as many compilations as necessary. The module system provides a
great flexibility that virtually allows support for any package with no user
intervention, as well as pre- and post-processing of the document. The
standard modules currently provide support for bibtex, dvips, dvipdfm, pdftex,
makeindex. A good number of standard packages are supported, including
graphics/graphicx (with automatic conversion between various formats and
Metapost compilation).

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --bindir=%{_bindir} --mandir=%{_mandir} --infodir=%{_infodir}
%make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT


%preun
%_remove_install_info %{name}.info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING NEWS README
%{_bindir}/*
%{python_sitelib}/rubber
%{python_sitelib}/*.egg-info
%{_datadir}/rubber
%lang(fr) %{_mandir}/fr/man1/*
%{_mandir}/man1/*
%{_infodir}/*


%changelog
* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 1.1-7mdv2011.0
+ Revision: 591342
- rebuild for py 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1-6mdv2010.0
+ Revision: 442768
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.1-5mdv2009.1
+ Revision: 326018
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.1-4mdv2009.0
+ Revision: 242567
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 27 2007 Funda Wang <fwang@mandriva.org> 1.1-2mdv2008.0
+ Revision: 71744
- fix file list on x86_64

  + Lenny Cartier <lenny@mandriva.org>
    - Rebuild for python
    - Import rubber



* Sun Mar 26 2006 Marc Lijour <mlijour@mandriva.com> 1.1-1mdk
- Update to version 1.1
- noarch works now

* Thu Dec 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.0-3mdk
- Don't build as noarch, since apparently python doesn't handle that

* Wed Dec 14 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.0-2mdk
- Fix BuildRequires

* Tue Dec 13 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.0-1mdk
- Initial MDV package
