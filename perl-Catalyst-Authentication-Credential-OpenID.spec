%define upstream_name    Catalyst-Authentication-Credential-OpenID
%define upstream_version 0.16

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    OpenID credential for Catalyst::Plugin::Authentication framework
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Cache::FastMmap)
BuildRequires: perl(Catalyst)
BuildRequires: perl(Catalyst::Authentication::User::Hash)
BuildRequires: perl(Catalyst::Devel)
BuildRequires: perl(Catalyst::Engine::HTTP)
BuildRequires: perl(Catalyst::Plugin::Session::State::Cookie)
BuildRequires: perl(Catalyst::Plugin::Session::Store::FastMmap)
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Parser)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Net::OpenID::Consumer)
BuildRequires: perl(Test::More)
BuildRequires: perl(parent)
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


