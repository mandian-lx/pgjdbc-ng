%{?_javapackages_macros:%_javapackages_macros}

Summary:	A JDBC driver for PostgreSQL
Name:		pgjdbc-ng
Version:	0.6
Release:	1
License:	BSD
Group:		Development/Java
URL:		https://github.com/impossibl/%{name}
Source0:	https://github.com/impossibl/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:  maven-local
BuildRequires:  mvn(io.netty:netty)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)

%description
A new JDBC driver for PostgreSQL aimed at supporting the advanced features of
JDBC and Postgres.

Features:
 *  JDBC 4.1 target (with goal of complete conformance)
 *  UDT support through standard SQLData, SQLInput & SQLOutput
 *  Code Generator for UDTs (https://github.com/impossibl/pgjdbc-ng-udt)
 *  Support for JDBC custom type mappings
 *  Pluggable custom type serialization
 *  Compact binary format with text format fallback
 *  Database, ResultSet and Parameter meta data
 *  Transactions / Savepoints
 *  Blobs
 *  Updatable ResultSets
 *  Callable Statements
 *  Asynchronous Notifications
 *  SSL Authentication and Encrpytion
 *  DataSource / XADataSource

%files -f .mfiles
%doc LICENSE

#----------------------------------------------------------------------------

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%files javadoc -f .mfiles-javadoc
%doc README.md
%doc LICENSE

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{name}-%{version}

# Delete prebuild binaries
find . -name "*.jar" -delete
find . -name "*.class" -delete

# Remove unuseful plugins
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-shade-plugin
%pom_remove_plugin :maven-source-plugin

# Fix Jar name
%mvn_file :%{name} %{name}-%{version} %{name}

%build
# Tests require connection to localhost/127.0.0.1:5432
%mvn_build -f

%install
%mvn_install
