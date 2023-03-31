Name:		texlive-context-layout
Version:	47085
Release:	2
Summary:	Show ConTeXt layouts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/context-layout
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-layout.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-layout.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Draws a representation of the layout of the current page and
displays the sizes of the widths and heights of the margins,
header, footer and text body.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/context/third/layout
%doc %{_texmfdistdir}/doc/context/third/layout

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
