---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-installation-guide-pcce-b-cisco-f930602ac9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/installation/guide/pcce_b_cisco-pcce-installationandupgrade-guide-12_5/pcce_b_cisco-pcce-installationandupgrade-guide-12_5_chapter_00001.html
retrieved_at: 2026-08-21T16:38:48.160277+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

Updated: April 3, 2021

Chapter: System Requirements

## Chapter: System Requirements

# System Requirements

Before proceeding with ICM application installation, ensure that you follow the antivirus guidelines specified in the Section,
                                    Antivirus Guidelines of the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

## Set up Active Directory

Ensure that you have a completed plan for your domain structure and Active Directory
                           implementation before you set up your network.

Warning

The Unified CCE servers should be in the same domain, and multiple domains are not supported.

For more information, see the Staging Guide for Cisco Unified ICM/Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

## Transport Layer
                        	 Security Version 1.2 Required

Contact center enterprise solutions require the use of TLS 1.2 only
                           		connections in this release. Our services accept incoming TLS connections only
                           		over TLS 1.2. All outgoing TLS connection use only TLS 1.2.

All clients that connect to either our web interfaces or databases must
                           		support TLS 1.2.

The older versions of the TLS/SSL are disabled by installer.

For more information see, Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

## Installation
                        	 Tools

During
                              		  installation, use one or all of the following tools, as required:

ICM-CCE-Installer—The main Unified CCE Installer copies all files into relevant folders, creates the base registries, and
                                       installs needed third-party software such as JRE and Apache Tomcat. It uses the Microsoft .NET Framework which is an integral
                                       software of Windows Server.

Optionally, you can update the JRE installed by the Unified CCE Installer with a later version of the JRE. See Java Upgrades .

If the ICM-CCE installer installs JRE on the Windows platform, the system retains only the Cisco approved CA certificates
                                                in the java certificate store, and removes all the unapproved certificates.

Do not run the installer remotely. Download the installer to a local machine for installation.

Cisco Unified
                                    				Intelligent Contact Management Database Administration (ICMDBA) Tool—Used to
                                    				create new databases, modify or delete existing databases, and perform limited
                                    				SQL Server configuration tasks.

Domain
                                    				Manager—Used to provision Active Directory.

Web Setup—Used to set up the Call Routers, Loggers, Network Gateways, Network Interface Controllers, and Administration &
                                    Data Servers.

Peripheral Gateway (PG) Setup—Used to set up MR PIMs and CG.

## VMware Hosting and
                        	 Hardware Support

See the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html for the supported specification based hardware, Cisco UCS C-Series servers for Packaged CCE fresh installs and upgrades,
                              and supported VMware vSphere ESXi versions.

## Software
                        	 Compatibility

See the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html

Endpoints for
                                    				agents and callers

Cisco gateway
                                    				hardware and software

Third-party
                                    				software

## Software
                        	 Licenses

The following table lists the Cisco components that comprise a Packaged CCE solution:

One server license for each of the voice applications.

One agent license for each concurrent user with different feature tiers.

You must register CVP instance with Cisco Smart
                                          									Licensing Server which includes CVP Call Server and VXML Server
                                          									in order to use the appropriate licenses.

For more information, see Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html .

Cisco Finesse

Cisco Finesse: User licenses included with selected tiers of Cisco Unified Contact Center Enterprise user licenses. One license
                                          for each server pair. One license for each Media Kit.

Packaged Contact Center Enterprise is enabled with Smart Licensing. For information on Smart Licensing, see the Packaged Contact
                                          Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Before you begin an installation or upgrade of any part of your contact center, confirm the following:

That you have all the required software products.

That all the software versions are compatible with each other.

That all software versions are also compatible with all hardware and VMware.

## Java Requirements

A new 12.5(1a) base installer is available for customers, which has OpenJDK JRE as the supporting Java run time for all the
                           CCE applications. Its predecessor the 12.5(1) installer employs Oracle JRE. Any installation done using the 12.5(1) installer
                           can continue to use Oracle JRE, and can receive Java security updates and fixes from the Oracle website.

However, if there is a need to apply an ES on 12.5(1) that mandates the installation of ES55 (mandatory OpenJDK ES), then
                           the Java updates would have to be downloaded and installed from the OpenLogic website.

CCE VMs installed using the 12.5(1a) installer would need the OpenJDK patches applied. You can verify the base installer version
                           to be 12.5(1a) from Control Panel > Programs > Programs and Features > Cisco Unified ICM/CCE 12.5.1a .

## Certificate Management Requirements

During installation of 12.5(2), Unified CCE installs the Java version 8 update 332. If your system has a Java version that
                              is lower than version 8 update 332, perform the following steps:

Step 1

Before you install 12.5(2):

Run the command at the command prompt: cd %CCE_JAVA_HOME%\bin .

Important

Export the certificates of all the components imported into the truststore.

The command to export the certificates is keytool -export -keystore <JRE path>\lib\security\cacerts -alias <alias of the component> -file <filepath>.cer

Enter the truststore password when prompted.

Step 2

After 12.5(2) installation is complete, perform the following steps:

Run the command at the command prompt: cd %CCE_JAVA_HOME%\bin .

Import the certificates for all the components that you previously exported from the truststore before you installed 12.5(2). The command to import certificates is keytool -import -keystore <JRE path>\lib\security\cacerts -file <filepath>.cer -alias <alias>.

Enter the truststore password when prompted.

Enter 'yes' when prompted to trust the certificate.

| Note | Before proceeding with ICM application installation, ensure that you follow the antivirus guidelines specified in the Section,
                                    Antivirus Guidelines of the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
|---|---|

| Warning | The Unified CCE servers should be in the same domain, and multiple domains are not supported. |
|---|---|

| Note | The older versions of the TLS/SSL are disabled by installer. |
|---|---|

| Note | Optionally, you can update the JRE installed by the Unified CCE Installer with a later version of the JRE. See Java Upgrades . If the ICM-CCE installer installs JRE on the Windows platform, the system retains only the Cisco approved CA certificates
                                                in the java certificate store, and removes all the unapproved certificates. |
|---|---|

| Components | License requirements |
|---|---|
| Cisco Packaged Contact Center Enterprise | One server license for each of the voice applications. One agent license for each concurrent user with different feature tiers. |
| Cisco Unified Communications Manager | One license for each Cisco Unified Communications Manager node, plus device licenses for connected devices. |
| Cisco Unified Customer Voice Portal (CVP) | You must register CVP instance with Cisco Smart
                                          									Licensing Server which includes CVP Call Server and VXML Server
                                          									in order to use the appropriate licenses. For more information, see Administration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/tsd-products-support-series-home.html . |
| Cisco Finesse | Cisco Finesse: User licenses included with selected tiers of Cisco Unified Contact Center Enterprise user licenses. One license
                                          for each server pair. One license for each Media Kit. |
| Cisco Customer Collaboration Platform | User license included with Packaged CCE Agent License. One server license for each Customer Collaboration Platform server. |

| Note | Packaged Contact Center Enterprise is enabled with Smart Licensing. For information on Smart Licensing, see the Packaged Contact
                                          Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
|---|---|

| Step 1 | Before you install 12.5(2): Run the command at the command prompt: cd %CCE_JAVA_HOME%\bin . Important Use %JAVA_HOME% if you are employing Oracle JRE. Export the certificates of all the components imported into the truststore. The command to export the certificates is keytool -export -keystore <JRE path>\lib\security\cacerts -alias <alias of the component> -file <filepath>.cer Enter the truststore password when prompted. | Important | Use %JAVA_HOME% if you are employing Oracle JRE. |
|---|---|---|---|
| Important | Use %JAVA_HOME% if you are employing Oracle JRE. |
| Step 2 | After 12.5(2) installation is complete, perform the following steps: Run the command at the command prompt: cd %CCE_JAVA_HOME%\bin . Import the certificates for all the components that you previously exported from the truststore before you installed 12.5(2). The command to import certificates is keytool -import -keystore <JRE path>\lib\security\cacerts -file <filepath>.cer -alias <alias>. Enter the truststore password when prompted. Enter 'yes' when prompted to trust the certificate. |

| Important | Use %JAVA_HOME% if you are employing Oracle JRE. |
|---|---|