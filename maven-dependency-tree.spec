%{?_javapackages_macros:%_javapackages_macros}
Name:          maven-dependency-tree
Version:       2.1
Release:       2.2
Summary:       Maven dependency tree artifact
Group:	Development/Java
License:       ASL 2.0
Url:           https://maven.apache.org/
Source0:       http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildArch:     noarch

Patch0001:     0001-Port-to-Maven-3.1.0-and-Eclipse-Aether.patch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-plugin-testing-harness)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-util)

Provides:      maven-shared-dependency-tree = %{version}-%{release}
Obsoletes:     maven-shared-dependency-tree < %{version}-%{release}

%description
Apache Maven dependency tree artifact. Originally part of maven-shared.

%package javadoc

Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0001 -p1
%pom_add_dep org.apache.maven:maven-compat:3.1.0
%pom_add_dep org.apache.maven:maven-artifact:2.2.1

%build
# we have no jmock yet
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-1
- Remove dependency on Sonatype Aether
- Resolves: rhbz#985704

* Mon Jul 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-1
- Update to upstream version 2.1

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.0-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 10 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.0-2
- Build with xmvn

* Wed Oct 24 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-1
- Initial package
