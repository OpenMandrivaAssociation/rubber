%define name rubber
%define version 1.1
%define release %mkrel 2

Name:		%name
Summary:	An automated system for building LaTeX documents
Version:	%version
Release:	%release
Source:		%name-%version.tar.bz2
URL:		http://www.pps.jussieu.fr/~beffara/soft/rubber/
License:	GPL
Group:		Publishing
Requires:	python, tetex
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel
BuildRequires:  texinfo
BuildArchitectures: noarch

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
%configure
%make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
%defattr(-,root,root)
%doc COPYING NEWS README
%{_bindir}/rubber
%{_bindir}/rubber-pipe
%{_bindir}/rubber-info
%{_libdir}/python*/site-packages/rubber
%{_datadir}/rubber
%lang(fr) %{_mandir}/fr/man1/rubber-info.1*
%lang(fr) %{_mandir}/fr/man1/rubber-pipe.1*
%lang(fr) %{_mandir}/fr/man1/rubber.1*
%doc %{_mandir}/man1/rubber-info.1*
%doc %{_mandir}/man1/rubber-pipe.1*
%doc %{_mandir}/man1/rubber.1*
%doc %{_infodir}/rubber.info.bz2
