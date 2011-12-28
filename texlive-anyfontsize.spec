# revision 17050
# category Package
# catalog-ctan /macros/latex/contrib/anyfontsize
# catalog-date 2010-02-15 00:07:58 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-anyfontsize
Version:	20100215
Release:	1
Summary:	Select any font size in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/anyfontsize
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anyfontsize.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anyfontsize.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the to user select any font size (via e.g.
\fontsize{...}{...}\selectfont), even those sizes that are not
listed in the .fd file. If such a size is requested, LaTeX will
search for and select the nearest listed size; anyfontsize will
then scale the font to the size actually requested. Similar
functionality is available for the CM family, for the EC
family, or for either computer modern encoding; the present
package generalises the facility.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/anyfontsize/anyfontsize.sty
%doc %{_texmfdistdir}/doc/latex/anyfontsize/README
%doc %{_texmfdistdir}/doc/latex/anyfontsize/anyfontsize.pdf
%doc %{_texmfdistdir}/doc/latex/anyfontsize/anyfontsize.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
