%global tl_name anyfontsize
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Select any font size in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/anyfontsize
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/anyfontsize.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/anyfontsize.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the to user select any font size (via e.g.
\fontsize{...}{...}\selectfont), even those sizes that are not listed in
the .fd file. If such a size is requested, LaTeX will search for and
select the nearest listed size; anyfontsize will then scale the font to
the size actually requested. Similar functionality is available for the
CM family, for the EC family, or for either computer modern encoding;
the present package generalises the facility.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/anyfontsize
%dir %{_datadir}/texmf-dist/tex/latex/anyfontsize
%doc %{_datadir}/texmf-dist/doc/latex/anyfontsize/README
%doc %{_datadir}/texmf-dist/doc/latex/anyfontsize/anyfontsize.pdf
%doc %{_datadir}/texmf-dist/doc/latex/anyfontsize/anyfontsize.tex
%{_datadir}/texmf-dist/tex/latex/anyfontsize/anyfontsize.sty
