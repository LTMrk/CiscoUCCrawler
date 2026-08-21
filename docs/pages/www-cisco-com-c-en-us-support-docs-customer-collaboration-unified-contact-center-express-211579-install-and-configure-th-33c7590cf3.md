---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-contact-center-express-211579-install-and-configure-th-33c7590cf3
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-contact-center-express/211579-Install-and-Configure-the-OpenAM-Identit.html
retrieved_at: 2026-08-21T13:21:48.677305+00:00
---

Install and Configure the OpenAM Identity Provider (IdP) for Cisco Identity Service (IdS) to enable SSO

# Install and Configure the OpenAM Identity Provider (IdP) for Cisco Identity Service (IdS) to enable SSO

### Download Options

Updated: August 13, 2017

Document ID: 211579

Contents

## Contents

## Introduction

This document describes the configuration on the OpenAM Identity Provider (IdP) to enable Single Sign On (SSO).

Cisco IdS Deployment Models

Co-resident with CUIC and LD for 2k deployments.

Standalone for 4k and 12k deployments.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Contact Center Express (UCCX) Release 11.6 or Cisco Unified Contact Center Enterprise Release 11.6 or Packaged Contact Center Enterprise (PCCE) Release 11.6 as applicable.

Note : This document references the configuration with respect to the Cisco Identitify Service (IdS) and the Identity Provider (IdP). The document references UCCX in the screenshots and examples, however the configuration is similar with respect to the Cisco Identitify Service (UCCX/UCCE/PCCE) and the IdP.

### Components Used

This document is not restricted to specific software and hardware versions. The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Install

Note : This document references OpenAM release 10.0.1 as a part of the qualification with SSO

### System Requirements

### Operating Systems

### Java Environment

### Web Application Container Requirements

### Supported Browsers

### Data Store Requirements

### Minimum Hardware Requirements

- Microsoft Windows Server 2003, 2008 R2

- Linux 2.6, 3.0

- Oracle Solaris 10

- Apache Tomcat 6.0.x, 7.0.x

- GlassFish v2

- JBoss Enterprise Application Platform 4.x, 5.x

- JBoss Application Server 7.x

- Jetty 7

- Oracle WebLogic Server 11g

- Oracle WebLogic Server 12c

If you run as a non-root user, the web application container must be able to write to its own home directory, where OpenAM stores configuration files.

- Chrome and Chromium 16 and later

- Firefox 3.6 and later

- Internet Explorer (version 7 and higher)

- Safari 5 and later

- ForgeRock OpenDJ

- Microsoft Active Directory

- IBM Tivoli Directory Server

- OpenDS

- Oracle Directory Server Enterprise Edition

- 1GB free RAM for OpenAM

You can deploy OpenAM on any hardware supported for the combination of the software required.

### Install

#### Obtain OpenAM Software

- Download OpenAM 10.0.1 releases from https://backstage.forgerock.com/downloads/OpenAM/OpenAM%20Enterprise/10.0.1/OpenAM%2010.0.1/zip#list

- For each release of the OpenAM core services, you can download the entire package as a .zip archive, only the OpenAM .war file, only the administrative tools as a .zip archive

- After you unzip the archive of the entire package, you get an opensso directory with a README, a set of license files, and the directories

#### Pre-requisites

Ensure that you have the required pre-requisite software for OpenAM core services before installation,

- A Java 6 runtime environment

- Install Apache Tomcat as web application container

- OpenAM core services require a minimum Java Virtual Memory (JVM) heap size of 1 GB and a permanent generation size of 256 MB. Apply the JVM options when you set JAVA_OPTS in the catalina file before the start of the tomcat application server - -Xmx1024m -XX:MaxPermSize=256m

For example set JAVA_OPTS=%JAVA_OPTS% -Xmx1024m -XX:MaxPermSize=256m -Xms512m

- Install Microsoft Active Directory as a Data Store with few users.

#### Install OpenAM Web Application

The deployable-war/opensso.war file contains all OpenAM server components and samples under the opensso directory.

##### Deploy OpenAM on Tomcat Container

Copy the opensso.war file to the directory where tomcat web applications are stored. Rename the opensso.war file to openam.war. Restart the tomcat service.

Verify the initial configuration screen in your browser at http://<FQHN>:8080/openam

### Run OpenAM Service

Openam is a simple web application hosted in a tomcat server. So, simply launch your tomcat server and hence be able to access OpenAM web service.

## Configure

### OpenAM Configurator

The OpenAM custom configuration process allows lots of common configuration options to be set with ease, so with more effort before the configuration, it saves configuration steps required later.

##### General Settings

Click Create New Configuration option, and choose password for the default administrator account (amAdmin). The password needs to be at least 8 characters long.

Once a valid password has been entered twice, the next button appears and the configuration can proceed.

##### Server Settings

By default, the Server URL is the fully qualified domain name of the server.

Note : It is important that the user that runs Apache Tomcat has write access to the Configuration directory. As a result  ~/openam/config is appropriate for this purpose. Supported Platform Locales are en_US (English), de (German), es (Spanish), fr (French), ja (Japanese), zh_CN (Simplified Chinese), or zh_TW (Traditional Chinese).

##### Configuration Data Store Settings

For single server configuration, these settings need not be changed.

##### User Data Store Settings

The User Data Store Settings connect OpenAM to the Microsoft Active Directory data store.

- User Data Store Type : Active Directory with Host and Port

- SSL/TLS Enabled : Not enabled

- Directory Name : <Domain Name of AD Server>

- Port : 389

- Root Suffix : dc=cisco,dc=com

- Login ID : cn=<AD user name>,cn=users,dc=cisco,dc=com

- Password : <AD user password>

Note : The configurator does not provide an option to continue until all the settings have been correctly specified and it has successfully connected to the Active Directory instance.

##### Site Configuration

In the Site Configuration screen, you can set up OpenAM as part of a site where the load is balanced across multiple OpenAM servers. For the first OpenAM install, accept the defaults.

##### Agent Information

In the Agent Information screen, provide a password of at least 8 characters to be used by policy agents to connect to OpenAM.

##### Summary

Review the information and click Create Configuration

##### Configuration Progress

The Configuration Progress Screen displays the progress of the installation. All the output on this screen and errors, are written to the file: ~/openam/config/install.log.

##### Configuration Complete

### Configure OpenAM as IdP

- Click Proceed to Login or Access through URL http://<FQDN of OpenAM>:8080/openam, and then login as OpenAM administrator

- When you access OpenSSO Enterprise for the first time, you are directed to the Configurator to perform the OpenSSO Enterprise initial configuration

- Select Default Configuration

- You are required to configure the passwords for OpenAMserver

- Configure the passwords and login to OpemAM server UI

#### Circle of Trust Configuration

Navigate to Federation Tab and click on New button under Circle of Trust section

Create a circle of trust with an unique name for the IdP Circle of trust and Click OK

Note : Service Provider and IdP must be in same Circle of Trust(CoT) for SAML SSO to work.

#### Create Hosted Identity Provider

Navigate to Common Tasks Tab and click on Create hosted Identity Provider and create a hosted IdP (leave the default configured values and Save the settings).

The Circle of Trust created earlier is listed

#### Configure Signing Key

Navigate to Federation Tab and Click on hosted Identity Provider added under Entity Providers section. Navigate to Assertion Content section and configure Signing field value as test under Certificate Aliases section. This is the certificate that would be used to sign the SAML assertion.

#### Import Service Provider Entity

Navigate to Federation Tab and Click on Import Entity... button under Entity Providers section.

Upload the Service Provider's Entity file (sp.xml) and save the page.

#### Request/Response Signing

Click on the entity imported and enable signing for Request/Response

#### Attribute Mapping

Navigate to Assertion Processing and add a mapping attribute for uid and user_principal as per the Directory and OpenAM settings. Click on Save.

Note : Both the attributes uid and user_principal are mandatory – since Service Provider (SP) identifies the Identity of a Authenticated user with the help of these. Also, ensure that the attributes sAMAccountName and userPrincipalName are also mapped in the Attribute Editor of Active Directory User properties.

#### Edit Circle of Trust

Navigate to Federation Tab and click on Circle of Trust added and ensure that you move the IdP(OpenAm server) and Service Provider entity from Available to Selected sections under Entity Providers section. This assigns IdP and Service Provider to be in the same Circle of Trust.

### Download OpenAM IdP Metadata

You can download the IdPmetadatafile of OpenAM server with the url http://<FQDN of OpenAM>:8080/openam/saml2/jsp/exportmetadata.jsp?entityid=http://<FQDN of OpenAM>:8080/openam&realm=

##### Sample OpenAM Metadata XML

## Further Configuration for SSO:

This document describes the configuration from the IdP aspect for SSO to integrate with the Cisco Identity Service. For further details, refer to the individual product configuration guides:

- UCCX

- UCCE

- PCCE

### Contributed by Cisco Engineers

Arundeep Nagaraj

Cisco TAC

Jalander Ramagiri

Cisco Engineering

Venkatesh Vedurumudi

Cisco Engineering

### This Document Applies to These Products

- Unified Contact Center Express

| Product | Deployment |
|---|---|
| UCCX | Co-resident |
| PCCE | Co-resident with CUIC (Cisco Unified Intelligence Center) and LD (Live Data) |
| UCCE | Co-resident with CUIC and LD for 2k deployments. Standalone for 4k and 12k deployments. |

| Operating Systems | Java Environment | Web Application Container Requirements | Supported Browsers | Data Store Requirements | Minimum Hardware Requirements |
|---|---|---|---|---|---|
| Microsoft Windows Server 2003, 2008 R2 Linux 2.6, 3.0 Oracle Solaris 10 | Release 10.0.1 of OpenAM requires Java Development Kit 1.6, at least 1.6.0_10. ForgeRock recommends that you use at least version 1.6.0_27 due to security fixes. ForgeRock has tested this release of OpenAM primarily with Oracle Java SE JDK. OpenAM Java SDK supports Java Development Kit 1.5 or 1.6. | Apache Tomcat 6.0.x, 7.0.x GlassFish v2 JBoss Enterprise Application Platform 4.x, 5.x JBoss Application Server 7.x Jetty 7 Oracle WebLogic Server 11g Oracle WebLogic Server 12c If you run as a non-root user, the web application container must be able to write to its own home directory, where OpenAM stores configuration files. | Chrome and Chromium 16 and later Firefox 3.6 and later Internet Explorer (version 7 and higher) Safari 5 and later | ForgeRock OpenDJ Microsoft Active Directory IBM Tivoli Directory Server OpenDS Oracle Directory Server Enterprise Edition | 1GB free RAM for OpenAM You can deploy OpenAM on any hardware supported for the combination of the software required. |