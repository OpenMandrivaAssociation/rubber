Name:		rubber
Summary:	An automated system for building LaTeX documents
Version:	1.1
Release:	9
Source:		http://ebeffara.free.fr/pub/%{name}-%{version}.tar.bz2
URL:		http://www.pps.jussieu.fr/~beffara/soft/rubber/
License:	GPL
Group:		Publishing
Requires:	texlive
BuildRequires:  python-devel
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
python setup.py install --root=%{buildroot}

%clean

%files
%doc COPYING NEWS README
%{_bindir}/*
%{py_puresitedir}/rubber
%{py_puresitedir}/*.egg-info
%{_datadir}/rubber
%lang(fr) %{_mandir}/fr/man1/*
%{_mandir}/man1/*
%{_infodir}/*
