Name:           jsr-305
Version:        3.0.2
Release:        1
Summary:        Correctness annotations for Java code
License:        BSD and CC-BY
URL:            https://code.google.com/p/jsr-305
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz
Source1:        NOTICE-CC-BY.txt
BuildRequires:  maven-local
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif

%description
This package contains reference implementations, test cases, and other
documents for Java Specification Request 305: Annotations for Software Defect
Detection.

%package javadoc
Summary:        Javadoc documentation for jsr-305

%description javadoc
This package contains the API documentation for jsr-305.

%prep
%autosetup -n jsr-305-3.0.2 -p1
cp %{SOURCE1} NOTICE-CC-BY
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/*" 1.6

sed -i 's|<groupId>com\.google\.code\.findbugs</groupId>|<groupId>org.jsr-305</groupId>|' ri/pom.xml
sed -i 's|<artifactId>jsr305</artifactId>|<artifactId>ri</artifactId>|' ri/pom.xml

%mvn_file :ri jsr-305
%mvn_alias :ri com.google.code.findbugs:jsr305
%mvn_package ":{proposedAnnotations,tcl}" __noinstall

%pom_disable_module sampleUses

%pom_remove_parent ri
%pom_add_parent org.jsr-305:jsr-305:0.1-SNAPSHOT ri

%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin ri
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin ri
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin ri
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin ri

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc ri/LICENSE NOTICE-CC-BY sampleUses

%files javadoc -f .mfiles-javadoc
%doc ri/LICENSE NOTICE-CC-BY

%changelog
* Fri Sep 3 2021 houyingchao <houyingchao@huawei.com> - 3.0.2-1
- Upgrade to 3.0.2

* Tue Jan 21 2020 Jiangping Hu <hujp1985@foxmail.com> - 0-0.25
- Package init
