%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Cracklib
Summary:	Crypt::Cracklib - Perl interface to Cracklib
Summary(pl.UTF-8):	Crypt::Cracklib - perlowy interfejs do biblioteki Cracklib
Name:		perl-Crypt-Cracklib
Version:	1.7
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8179f32d7470780e001532bcb6cb4080
URL:		http://search.cpan.org/dist/Crypt-Cracklib/
BuildRequires:	cracklib-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple interface to Alec Muffett's Crack library.

%description -l pl.UTF-8
Moduł Crypt::Cracklib jest prostym interfejsem do biblioteki Crack
Aleca Muffetta.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

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
%{_mandir}/man3/Crypt::Cracklib.3pm*
