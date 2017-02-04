Summary:	A JDBC driver for PostgreSQL
Name:		pgjdbc-ng
Version:	0.6
Release:	1
License:	BSD
Group:		Development/Java
URL:		https://github.com/impossibl/%{name}
Source0:	https://github.com/impossibl/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	jpackage-utils
BuildRequires:	java-headless
BuildRequires:	maven-local
BuildRequires:	mvn(io.netty:netty-common)
BuildRequires:	mvn(io.netty:netty-buffer)
BuildRequires:	mvn(io.netty:netty-codec)
BuildRequires:	mvn(io.netty:netty-handler)
BuildRequires:	mvn(io.netty:netty-transport)
BuildRequires:	mvn(org.apache.maven.plugins:maven-checkstyle-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-shade-plugin)
# The following is required for tests only
BuildRequires:	mvn(junit:junit)

Requires:	java-headless
Requires:	jpackage-utils

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
%doc license.txt

#----------------------------------------------------------------------------

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%files javadoc -f .mfiles-javadoc
%doc license.txt

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{name}-%{version}

# Delete prebuild binaries
find . -name "*.jar" -delete
find . -name "*.class" -delete

# Fix Jar name
%mvn_file :%{name} %{name}-%{version} %{name}

%build
%mvn_build

%install
%mvn_install
