%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Cracklib
Summary:	Crypt::Cracklib Perl module - Perl interface to Cracklib
Summary(pl):	Modu³ Perla Crypt::Cracklib - perlowy interfejs do biblioteki Cracklib
Name:		perl-Crypt-Cracklib
Version:	0.01
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	cracklib-devel
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple interface to Alec Muffett's Crack library.

%description -l pl
Modu³ Crypt::Cracklib jest prostym interfejsem do biblioteki Crack
Aleca Muffetta.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo -e '/usr/include\n/usr/lib' | perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Crypt/Cracklib.pm
%dir %{perl_vendorarch}/auto/Crypt/Cracklib
%{perl_vendorarch}/auto/Crypt/Cracklib/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Cracklib/*.so
%{_mandir}/man3/*
