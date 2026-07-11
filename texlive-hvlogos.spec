%global tl_name hvlogos
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.16
Release:	%{tl_revision}.1
Summary:	Print TeX-related names as logo
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hvlogos
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hvlogos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hvlogos.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is more or less an extension to Heiko Oberdiek's package
hologo. It prints TeX-related names as logos. The package requires
fetamont, hologo, dantelogo, and xspace.

