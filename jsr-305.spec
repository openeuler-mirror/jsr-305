Name:           jsr-305
Version:        0
Release:        0.25
Summary:        Correctness annotations for Java code
License:        BSD and CC-BY
URL:            https://github.com/amaembo/jsr-305
BuildArch:      noarch
Source0:        https://github.com/amaembo/%{name}/archive/fdeb2abc16865fdd13f205c8f8afb7a34272e93e/%{name}.tar.gz
Source1:        NOTICE-CC-BY.txt
BuildRequires:  maven-local

%description
This package contains reference implementations, test cases, and other
documents for Java Specification Request 305: Annotations for Software Defect
Detection.

%package javadoc
Summary:        Javadoc documentation for jsr-305

%description javadoc
This package contains the API documentation for jsr-305.

%prep
%autosetup -n jsr-305-fdeb2abc16865fdd13f205c8f8afb7a34272e93e -p1
cp %{SOURCE1} NOTICE-CC-BY

%mvn_file :ri jsr-305
%mvn_alias :ri com.google.code.findbugs:jsr305
%mvn_package ":{proposedAnnotations,tcl}" __noinstall

%pom_disable_module sampleUses

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc ri/LICENSE NOTICE-CC-BY sampleUses

%files javadoc -f .mfiles-javadoc
%doc ri/LICENSE NOTICE-CC-BY

%changelog
* Tue Jan 21 2020 Jiangping Hu <hujp1985@foxmail.com> - 0-0.25
- Package init
