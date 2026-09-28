---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-installation-guide-pcce-b-1262--4a99b72421
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/installation/guide/pcce_b_1262_cisco_pcce_installationandupgrade_guide/pcce_b_cisco_pcce_installationandupgrade_guide_12_5_2_appendix_01001.html
retrieved_at: 2026-08-21T04:51:05.587732+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

Updated: March 9, 2026

Chapter: Security Considerations

## Chapter: Security Considerations

# Security Considerations

## Java Upgrades

During installations and upgrades, Unified CCE installs the base required Java version.

You can apply Java updates to your contact center as follows:

Apply Java updates for the latest 32-bit Java 8 minor version.

For the most current Java support information, see the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

You can download and install the OpenJDK Java updates from the OpenLogic website.

Modify the Windows CCE_JAVA_HOME environment variable to point to the new OpenJDK Java Runtime Environment (JRE) location if it has changed.

AppDynamics machine agent that is packaged with Unified ICM and Unified CVP uses a separate copy of OpenJDK. Any vulnerability
                                       fix for OpenJDK requires an upgrade of the AppDynamics machine agent. This update is delivered through an engineering special
                                       (ES) for Unified ICM and Unified CVP.

## Upgrade OpenJDKUtility

The Cisco Upgrade OpenJDKUtility:

Upgrades OpenJDK JRE to latest release.

Supports upgrade for both MSI and Zip file formats.

Automatically sets the CCE_JAVA_HOME environment variable to updated version so that Unified CCE applications can employ the
                                 latest OpenJDK version as the Java runtime.

Before using the tool:

Download the OpenJDK installer from the OpenLogic OpenJDK website: https://www.openlogic.com/openjdk . (Both msi and zip formats are supported).

Copy the downloaded file into the Unified CCE component VMs. For Example C:\UpgradeOpenJDKTool .

Download the utility from https://software.cisco.com/download/home/284360381/type/284416107/release/12.6(2) and unzip OpenJdkUpgradeTool.zip to any local folder. For example: Download and Unzip under C:\UpgradeOpenJDKTool .

Run openJDKUtility.exe from unziped folder For all the supported commands and for more details, refer to the Readme.html (which is available as part of the OpenJdkUpgradeTool.zip ).

Once the installation is successful, CCE_JAVA_HOME is updated and does not trigger the system reboot.

## Upgrade Tomcat
                        	 Utility

Use the optional
                           		Cisco Upgrade Tomcat Utility to:

Upgrade Tomcat to version 9.0 build releases. (That
                                 					is, only version 9.0 build releases work
                                 					with this tool.) You may choose to upgrade to newer builds of Tomcat release 9.0 to keep up with the
                                 					latest security fixes.

Tomcat uses the following release numbering scheme: Major.minor.build. For example, you can upgrade from 9.0.22 to 9.0.69 . You cannot use this tool for major or minor version upgrades.

Before using the
                           		tool:

Download the Tomcat installer (apache-tomcat-version.exe) from the Tomcat website: http://archive.apache.org/dist/tomcat/tomcat-9/ . Copy the installer onto the Unified CCE component VMs. For Example
                                 					C:\UpgradeTomcatTool.

Download the utility zip file, extract it, and run the batch file to upgrade Tomcat.

Download link:

- <ICM install directory>:\icm\tomcat\logs

- <ICM install directory>:\icm\debug.txt

### Install Tomcat

For detailed information on the results from each step, see the ../UpgradeTomcatResults/UpgradeTomcat.log file.

Stop Unified CCE services on the VM before using the Tomcat Utility.

Step 1

From the command line, navigate to the directory where you copied the Upgrade Tomcat Utility.

Step 2

Enter this command to run the tool: tomcatutility.bat .

Step 3

When prompted, enter the full pathname of the Tomcat installer version you want
                                          to use.

```
c:\tomcatInstaller\apache-tomcat-9.0.69.exe
```

Step 4

When prompted, enter yes to continue with the install.

Step 5

Repeat these steps for all unified CCE component VMs.

## Enable Secure Communication Between CCE Components

This section describes how to enable TLS 1.2-based secure communication over existing TCP connections between Cisco Contact
                           Center Enterprise (CCE) components. When enabled, inter-component traffic—including MDS messaging, state transfer, data recovery,
                           replication, and real-time distribution—is encrypted using TLS 1.2.

### Overview

By default, TCP connections between CCE components (Router, Logger, Peripheral Gateway, AW-HDS, Dialer) carry unencrypted
                              traffic. Enabling secure communication wraps these connections with TLS 1.2, protecting data in transit across both private
                              (intra-data-center) and public (inter-data-center) network interfaces.

Secure communication is configured per component through the Cisco Web Setup tool (for Router, Logger, and AW) and Peripheral
                              Gateway Setup (for PG and Dialer). Each component can operate in mixed mode, accepting both secure and non-secure connections,
                              or in secure-only mode where non-secure connections are rejected.

### Secured Connection Path

The following inter-component connections are secured when this feature is enabled:

Connection

Interface Type

Description

### Prerequisites

#### Software Requirements

Secure communication requires the following minimum software versions on each CCE component:

Component

Minimum Version

#### Certificate Requirements

TLS requires certificates to be exchanged between all communicating CCE nodes. Before enabling secure communication:

Deploy a certificate on every CCE node (Router Side A and B, Logger Side A and B, all PGs, all AW servers).

Install each server's trust certificate on the peer nodes that connect to it. For example, Router Side A must trust Router
                                       Side B's certificate, and PG must trust the Router's certificate.

Use the CiscoCertUtil utility to create self-signed certificates and to import trust certificates.

For the Admin Client, create and install the certificate on the Admin Client machine, on all AW Distributors, and on the CCE
                                       Router.

For more information about certificate management, see the Certificate Management for Secured Connections chapter in the Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/configuration/guide/ucce_b_security-guide-for-cisco-unified-icm_contact_center_-enterprise_release_1262.html

### Enable Secure Communication on the CCE Router

To enable secure communication on both Router Side A and Router Side B, perform the following steps:

Step 1

Open Web Setup on the Router server.

Step 2

Edit the Router component.

Step 3

Navigate to the Router Security tab.

Step 4

Select the following options:

Enable secure connection between Router and its Peer and Logger.

Enable secure connection between Router and Peripheral Gateways

Enable secure connection between Router and AW Distributors

Step 5

(Optional) To enforce secure-only mode, select the Enable secure-only connection check box.

For the mixed mode, deselect secure connection to allows both secure and non-secure clients.

Step 6

Click Save and apply the configuration.

Step 7

Repeat the above steps on Router Side B.

Step 8

Restart the Router service on both sides.

### Enable Secure Communication on the CCE Logger

Perform the following steps on both Logger Side A and Logger Side B.

Step 1

Open Web Setup on the Logger server.

Step 2

Edit the Logger component.

Step 3

Navigate to the Logger Security tab.

Step 4

Select the following options:

Enable secure connection between Logger and Router

Enable secure data recovery between Logger and Logger

Enable secure data replication between Logger and AW-HDS-DDS

Enable secure connection between Campaign Manager and Dialer (Outbound Option)

Step 5

(Optional) To enforce secure-only mode, select the Enable secure-only connection check box.

Step 6

Click Save and apply the configuration.

Step 7

On the Logger Side B, perform the above Step 1 to Step 6.

Step 8

Restart the Logger service on both sides.

### Enable Secure Communication on the Peripheral Gateway

#### Peripheral Gateway Network Interfaces

To enable secure connection on every PG on both Side A and Side B, perform the following steps.

##### Before you begin

Ensure that ICM12.6.2_ES103 is installed and secure communication is enabled on the CCE Router before proceeding.

Step 1

Open Peripheral Gateway Setup on the PG server.

Step 2

Edit the PG.

For example, edit PG as PG1.

Step 3

Navigate to Peripheral Gateway Network Interfaces.

Step 4

From the Private Interfaces section, select the Enable secure connection check box.

Step 5

From the Visible Interfaces section, select the Enable secure connection check boc.

Step 6

Repeat Step 1 to Step 5 for all PGs on the server.

Step 7

Apply the configuration on both Side A and Side B.

Step 8

Restart the CCE PG Service on both sides.

#### Dialer (Outbound Option)

To enable secure connection for every Dialer on both Side A and Side B, perform the following steps:

##### Before you begin

Ensure that ICM12.6.2_ES103 is installed and secure communication is enabled on the CCE Logger before proceeding.

Step 1

Open Peripheral Gateway Setup on the PG server.

Step 2

Edit the Dialer component.

Step 3

Navigate to Outbound Option Dialer Properties.

Step 4

From the Campaign Manager Connections section, select Enable secure connection .

Step 5

Repeat Step 1 to Step 4 for all Dialers on the server.

Step 6

Apply the configuration on both Side A and Side B.

Step 7

Restart the CCE PG Service on both sides.

### Enable Secure Communication on the AW-HDS

To enable secure connection on every AW-HDS and AW-HDS-DDS server, perform the following steps:

#### Before you begin

Ensure that ICM12.6.2_ES103 is installed and secure communication is enabled on the CCE Logger before proceeding.

Step 1

Open Web Setup on the AW-HDS server.

Step 2

Edit the Administration & Data Server component.

Step 3

Navigate to the AW Security tab.

Step 4

Select the following options:

Enable secure data replication from Logger database to AW-HDS database

Enable secure connection between Distributor and AW Clients

Enable secure connection to CCE Router for configuration updates

Step 5

(Optional) To enforce secure-only mode, select Enable secure-only connection .

Step 6

Click Save and apply the configuration.

Step 7

Perform Step 1 to Step 6 on all AW-HDS and AW-HDS-DDS servers.

Step 8

Restart the Distributor service.

### Administration Client

#### Before you begin

Ensure that ICM12.6.2_ES103 is enabled on the Logger and ICM12.6.2_ES102 is enabled on the AW-HDS before enabling secure mode on the Administration Client.

Step 1

Open Admin Client Setup.

Step 2

Select Enable Secure Mode .

Step 3

Click Save .

### Recommended Enablement Order

Enable secure communication in the following order to avoid connectivity issues:

CCE Router (both Side A and Side B)

CCE Logger (both Side A and Side B)

CCE Peripheral Gateway (all PGs, both sides)

CCE Dialer (all Dialers, both sides)

CCE AW-HDS and AW-HDS-DDS (all servers)

CCE Administration Client (all Admin Client machines)

During the initial rollout, use mixed mode (do not enable secure-only) to maintain communication for components pending updatese.
                                          Once all components are upgraded and secure communication is verified across all links, you may optionally switch each component
                                          to secure-only mode.

### Configuration Summary

The following table has all the CCE components and its configuration summary:

Component

Secure connection to Peer and Logger

Secure connection to PGs

Secure connection to AW Distributors

Secure-only connection (optional)

Secure connection to Router

Secure data recovery (Logger-Logger)

Secure data replication (Logger-AW)

Secure connection to Dialer

Secure-only connection (optional)

Enable secure connection (Private Interfaces)

Enable secure connection (Visible Interfaces)

• Enable secure connection (Campaign Manager Connections)

Secure replication from Logger to AW-HDS

Secure connection (Distributor-AW Clients)

Secure connection to Router

Secure-only connection (optional)

• Enable Secure Mode

#### Verification

After enabling secure communication, verify that TLS connections are established:

Check the EMS process logs on each component for TLS handshake success messages.

Ensure that MDS traffic between Router Side A and Side B is operational and data is flowing.

Verify Logger-to-Logger recovery is functional by inspecting the recovery process logs.

Confirm that data replication from Logger to AW-HDS is working by checking the Distributor logs.

For Outbound Option, confirm that the Dialer connects to Campaign Manager and campaigns are operational.

Verify Admin Client connectivity to the AW Distributor.

### Disable Secure Communication

Disabling secure communication removes TLS encryption from inter-component traffic. Perform this action only during a maintenance
                                          window and only if required.

To disable secure communication, perform the following steps for each component:

For Router, uncheck all options under Router Security in Web Setup. Apply on both side A and B.

For Logger, uncheck all options under Logger Security in Web Setup. Apply on both side A and B.

For Peripheral Gateway, uncheck Enable secure connection under Private and Visible Interfaces in PG Setup. Cycle the CCE PG
                                    Service.

For Dialer, uncheck Enable secure connection under Campaign Manager Connections. Cycle the CCE PG Service.

For AW-HDS, uncheck all options under AW Security in Web Setup. Apply on all AW servers.

For Admin Client, uncheck Enable Secure Mode in Admin Client Setup.

### Troubleshooting

The following table provides the symptoms and resolution to troubleshoot secure communication for CCE components:

Symptom

Resolution

| Note | AppDynamics machine agent that is packaged with Unified ICM and Unified CVP uses a separate copy of OpenJDK. Any vulnerability
                                       fix for OpenJDK requires an upgrade of the AppDynamics machine agent. This update is delivered through an engineering special
                                       (ES) for Unified ICM and Unified CVP. |
|---|---|

| Note | Stop Unified CCE services on the VM before using the Tomcat Utility. |
|---|---|

| Step 1 | From the command line, navigate to the directory where you copied the Upgrade Tomcat Utility. |
|---|---|
| Step 2 | Enter this command to run the tool: tomcatutility.bat . |
| Step 3 | When prompted, enter the full pathname of the Tomcat installer version you want
                                          to use. For example: c:\tomcatInstaller\apache-tomcat-9.0.69.exe |
| Step 4 | When prompted, enter yes to continue with the install. |
| Step 5 | Repeat these steps for all unified CCE component VMs. Note If the latest installed Tomcat does not work properly, install the previous working version using the Tomcat utility by following
                                                      the above-mentioned steps. | Note | If the latest installed Tomcat does not work properly, install the previous working version using the Tomcat utility by following
                                                      the above-mentioned steps. |
| Note | If the latest installed Tomcat does not work properly, install the previous working version using the Tomcat utility by following
                                                      the above-mentioned steps. |

| Note | If the latest installed Tomcat does not work properly, install the previous working version using the Tomcat utility by following
                                                      the above-mentioned steps. |
|---|---|

| Connection | Interface Type | Description |
|---|---|---|
| Router ↔ Router | Private | High, medium, and low priority MDS traffic and state transfer between Router Side A and Side B. |
| PG ↔ PG | Private | MDS traffic and state transfer between Peripheral Gateway Side A and Side B. |
| PG Agent ↔ CC Agent | Public | Communication between PG Agent on the Peripheral Gateway and CC Agent on the CCE Router. |
| Logger ↔ Logger | Private | Data recovery process between Logger Side A (rcv) and Logger Side B (rcv). |
| Logger ↔ Router | Private | Node Manager, Campaign Manager, recovery, replication, and ConfigLogger on Logger as MDS clients to mdsproc on Router. |
| Logger ↔ AW-HDS / AW-HDS-DDS | Public | Data replication between Logger and the Administration & Data Server (AW-HDS or AW-HDS-DDS). |
| Campaign Manager ↔ Dialer | Public | Campaign Manager on Logger to BaDialer on the Agent PG (Outbound Option). |
| Router ↔ AW-HDS | Public | Real-Time Server on Router to Real-Time Distributor on the AW-HDS. |

| Component | Minimum Version |
|---|---|
| CCE AW-HDS, AW-HDS-DDS, and Admin Client | Release 12.6(2) with ICM12.6.2_ES102 or later |
| CCE Router and Logger (Rogger) | Release 12.6(2) with ICM12.6.2_ES103 or later |
| CCE Peripheral Gateway | Release 12.6(2) with ICM12.6.2_ES108 or later |

| Step 1 | Open Web Setup on the Router server. |
|---|---|
| Step 2 | Edit the Router component. |
| Step 3 | Navigate to the Router Security tab. |
| Step 4 | Select the following options: Enable secure connection between Router and its Peer and Logger. Enable secure connection between Router and Peripheral Gateways Enable secure connection between Router and AW Distributors |
| Step 5 | (Optional) To enforce secure-only mode, select the Enable secure-only connection check box. For the mixed mode, deselect secure connection to allows both secure and non-secure clients. |
| Step 6 | Click Save and apply the configuration. |
| Step 7 | Repeat the above steps on Router Side B. |
| Step 8 | Restart the Router service on both sides. |

| Step 1 | Open Web Setup on the Logger server. |
|---|---|
| Step 2 | Edit the Logger component. |
| Step 3 | Navigate to the Logger Security tab. |
| Step 4 | Select the following options: Enable secure connection between Logger and Router Enable secure data recovery between Logger and Logger Enable secure data replication between Logger and AW-HDS-DDS Enable secure connection between Campaign Manager and Dialer (Outbound Option) |
| Step 5 | (Optional) To enforce secure-only mode, select the Enable secure-only connection check box. |
| Step 6 | Click Save and apply the configuration. |
| Step 7 | On the Logger Side B, perform the above Step 1 to Step 6. |
| Step 8 | Restart the Logger service on both sides. |

| Step 1 | Open Peripheral Gateway Setup on the PG server. |
|---|---|
| Step 2 | Edit the PG. For example, edit PG as PG1. |
| Step 3 | Navigate to Peripheral Gateway Network Interfaces. |
| Step 4 | From the Private Interfaces section, select the Enable secure connection check box. |
| Step 5 | From the Visible Interfaces section, select the Enable secure connection check boc. |
| Step 6 | Repeat Step 1 to Step 5 for all PGs on the server. |
| Step 7 | Apply the configuration on both Side A and Side B. |
| Step 8 | Restart the CCE PG Service on both sides. |

| Step 1 | Open Peripheral Gateway Setup on the PG server. |
|---|---|
| Step 2 | Edit the Dialer component. |
| Step 3 | Navigate to Outbound Option Dialer Properties. |
| Step 4 | From the Campaign Manager Connections section, select Enable secure connection . |
| Step 5 | Repeat Step 1 to Step 4 for all Dialers on the server. |
| Step 6 | Apply the configuration on both Side A and Side B. |
| Step 7 | Restart the CCE PG Service on both sides. |

| Step 1 | Open Web Setup on the AW-HDS server. |
|---|---|
| Step 2 | Edit the Administration & Data Server component. |
| Step 3 | Navigate to the AW Security tab. |
| Step 4 | Select the following options: Enable secure data replication from Logger database to AW-HDS database Enable secure connection between Distributor and AW Clients Enable secure connection to CCE Router for configuration updates |
| Step 5 | (Optional) To enforce secure-only mode, select Enable secure-only connection . |
| Step 6 | Click Save and apply the configuration. |
| Step 7 | Perform Step 1 to Step 6 on all AW-HDS and AW-HDS-DDS servers. |
| Step 8 | Restart the Distributor service. |

| Step 1 | Open Admin Client Setup. |
|---|---|
| Step 2 | Select Enable Secure Mode . |
| Step 3 | Click Save . |

| Note | During the initial rollout, use mixed mode (do not enable secure-only) to maintain communication for components pending updatese.
                                          Once all components are upgraded and secure communication is verified across all links, you may optionally switch each component
                                          to secure-only mode. |
|---|---|

| Component | Configuration Location | Options |
|---|---|---|
| Router | Web Setup → Router Security | Secure connection to Peer and Logger Secure connection to PGs Secure connection to AW Distributors Secure-only connection (optional) |
| Logger | Web Setup → Logger Security | Secure connection to Router Secure data recovery (Logger-Logger) Secure data replication (Logger-AW) Secure connection to Dialer Secure-only connection (optional) |
| Peripheral Gateway | PG Setup → Network Interfaces | Enable secure connection (Private Interfaces) Enable secure connection (Visible Interfaces) |
| Dialer | PG Setup → Outbound Option Dialer Properties | • Enable secure connection (Campaign Manager Connections) |
| AW-HDS / AW-HDS-DDS | Web Setup → AW Security | Secure replication from Logger to AW-HDS Secure connection (Distributor-AW Clients) Secure connection to Router Secure-only connection (optional) |
| Admin Client | Admin Client Setup | • Enable Secure Mode |

| Note | Disabling secure communication removes TLS encryption from inter-component traffic. Perform this action only during a maintenance
                                          window and only if required. |
|---|---|

| Symptom | Resolution |
|---|---|
| Component fails to connect after enabling TLS | Verify that the peer component also has secure communication enabled and that certificates are correctly installed on both
                                       nodes. |
| Certificate error in process logs | Re-create the certificate using CiscoCertUtil and re-import the trust certificate on the peer node. |
| Mixed-mode clients cannot connect | Confirm that Enable secure-only connection is not enabled. Mixed mode must be used until all components are upgraded. |
| Dialer cannot connect to Campaign Manager | Ensure that ICM12.6.2_ES103 is installed on the Logger and Logger Security. From Logger Security, enable secure connection between Campaign Manager and
                                       Dialer. |