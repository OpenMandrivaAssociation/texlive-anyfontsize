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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the to user select any font size (via e.g.
\fontsize{...}{...}\selectfont), even those sizes that are not listed in
the .fd file. If such a size is requested, LaTeX will search for and
select the nearest listed size; anyfontsize will then scale the font to
the size actually requested. Similar functionality is available for the
CM family, for the EC family, or for either computer modern encoding;
the present package generalises the facility.

