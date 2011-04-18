%define upstream_name    Catalyst-Authentication-Credential-OpenID
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    OpenID credential for Catalyst::Plugin::Authentication framework
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Cache::FastMmap) >= 1.280.0
BuildRequires: perl(Catalyst) >= 5.700.0
BuildRequires: perl(Catalyst::Authentication::User::Hash)
BuildRequires: perl(Catalyst::Devel) >= 1.0.0
BuildRequires: perl(Catalyst::Engine::HTTP)
BuildRequires: perl(Catalyst::Plugin::Session::State::Cookie) >= 0.80.0
BuildRequires: perl(Catalyst::Plugin::Session::Store::FastMmap) >= 0.50.0
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Parser) >= 3.0.0
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Net::OpenID::Consumer) >= 1.30.0
BuildRequires: perl(Test::More)
BuildRequires: perl(parent) >= 0.200.0
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
D'er... testing. Has an OpenID provider to test the OpenID credential
against.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


