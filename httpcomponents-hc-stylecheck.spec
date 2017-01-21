%define bname httpcomponents
%define module hc-stylecheck

Summary:	Apache HttpComponents Stylecheck Plugin Configuration
Name:		%{bname}-%{module}
Version:	1
Release:	1
License:	ASL 2.0
Group:		Development/Java
URL:		https://hc.apache.org/
# svn export https://svn.apache.org/repos/asf/httpcomponents/hc-stylecheck/tags/%{version}/ %{name}-%{version}
# tar -cJf %{name}-%{version}.tar.xz %{name}-%{version}
Source:		%{name}-%{version}.tar.xz
BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	java
BuildRequires:	maven-local

%description
Shared stylecheck plugin configuration for HC projects.

%files -f .mfiles

#----------------------------------------------------------------------------

%prep
%setup -q

# fix jar-not-indexed warning
%pom_add_plugin :maven-jar-plugin . "<configuration>
	<archive>
		<index>true</index>
	</archive>
</configuration>"

# fix Jar name
%mvn_file :%{module} %{bname}/%{module}

%build
%mvn_build

%install
%mvn_install

