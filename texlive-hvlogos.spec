Name:		texlive-hvlogos
Version:	72538
Release:	1
Summary:	Print TeX-related names as logo
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hvlogos
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvlogos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvlogos.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is more or less an extension to Heiko Oberdiek's
package hologo. It prints TeX-related names as logos. The
package requires fetamont, hologo, dantelogo, and xspace.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/hvlogos
%doc %{_texmfdistdir}/doc/latex/hvlogos

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
