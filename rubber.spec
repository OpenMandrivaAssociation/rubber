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

%post
%_install_info %{name}.info

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
