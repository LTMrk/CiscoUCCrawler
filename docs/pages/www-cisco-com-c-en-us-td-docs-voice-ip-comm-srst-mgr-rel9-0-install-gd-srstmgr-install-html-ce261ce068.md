---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-srst-mgr-rel9-0-install-gd-srstmgr-install-html-ce261ce068
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/srst_mgr/rel9_0/install_gd/srstmgr_install.html
retrieved_at: 2026-08-21T21:29:30.546586+00:00
---

Installation and Upgrade Guide for Cisco Unified SRST Manager

# Installation and Upgrade Guide for Cisco Unified SRST Manager

### Download Options

Updated: August 17, 2015

## Table of Contents

Installation and Upgrade Guide for Cisco Unified SRST Manager

Overview of Cisco Unified SRST Manager Deployment

Overview of Installation Steps

Migrating and Upgrading

Selecting a Platform for Cisco Unified SRST Manager

Specifications-based Platforms

Tested Reference Configuration Platforms

VMware Requirements

Setting up the VMware ESXi Environment

VMWare Tools

Installing Cisco Unified SRST Manager

Downloading the Cisco Unified SRST Manager OVA Template

Deploying the OVA Template

Configuring Cisco Unified SRST Manager after Installation

Setting Up Communications with CUCM

Acquiring and Provisioning SRST Sites

Migration to Cisco Unified SRST Manager

Upgrading Cisco Unified SRST Manager

Cisco Unified SRST Manager Licensing

Related Documentation

First Published: August, 2012 Last updated: August 17, 2015

This document provides the technical information that you need to install Cisco Unified SRST Manager. This document contains the following topics:

## Overview of Cisco Unified SRST Manager Deployment

Cisco Unified SRST Manager operates within a VMware ESXi virtualized environment. The software is packaged as an OVA template for installation within the ESXi environment (4.1, 5.0, 5.1 or 5.5). To simplify the installation process, the OVA file includes the following:

- Virtual machine system settings preconfigured for Cisco Unified SRST Manager

- Cisco Unified SRST Manager software

For more information about the ESXi environment, see:

http://www.vmware.com/products/vsphere/esxi-and-esx/overview.html

### Overview of Installation Steps

The following steps provide an overview of how to set up Cisco Unified SRST Manager.

Step 1 Select and install a server on which to operate Cisco Unified SRST Manager.

See: Selecting a Platform for Cisco Unified SRST Manager

Step 2 Set up the VMWare ESXi environment on the server.

See: Setting up the VMware ESXi Environment

Step 3 Download the Cisco Unified SRST Manager OVA template from Cisco.com.

See: Downloading the Cisco Unified SRST Manager OVA Template

Step 4 Deploy the OVA on the server.

See: Deploying the OVA Template

Step 5 Configure the networking and other Cisco Unified SRST Manager settings, according to the details of your network.

See: Configuring Cisco Unified SRST Manager after Installation

Step 6 Set up communication between Cisco Unified SRST Manager and the communications manager.

See: Setting Up Communications with CUCM

Step 7 Acquire and provision remote sites and SRST references.

See: Acquiring and Provisioning SRST Sites

### Migrating and Upgrading

If you have a Cisco Unified Messaging Gateway (UMG) installation or an existing Cisco Unified SRST Manager installation, you can migrate the configuration data to a fresh installation of Cisco Unified SRST Manager. See Migration to Cisco Unified SRST Manager .

You can upgrade Cisco Unified SRST Manager when new releases become available. See Upgrading Cisco Unified SRST Manager .

## Selecting a Platform for Cisco Unified SRST Manager

There are two approaches to selecting a server for running Cisco Unified SRST Manager within a VMware ESXi environment.

### Specifications-based Platforms

This section provides information about specifications-based server platforms. See Table 1 for information about specifications-based server platforms.

Table 1 Specifications-based Server Platforms

For information on...

See...

Hardware requirements

UC Virtualization Supported Hardware

http://docwiki.cisco.com/wiki/UC_Virtualization_Supported_Hardware

VMware installation and configuration

Implementing Virtualization Deployments

http://docwiki.cisco.com/wiki/Implementing_Virtualization_Deployments

### Tested Reference Configuration Platforms

This section provides information about tested reference configuration (TRC) platforms. For extensive information about tested reference configurations, including details about specific server models, see:

UC Virtualization Supported Hardware

http://docwiki.cisco.com/wiki/UC_Virtualization_Supported_Hardware

Server Product Information

The following pages provide product information about specific TRC servers:

- Cisco UCS B-Series Blade Servers

http://www.cisco.com/en/US/products/ps10280/index.html

- Cisco UCS C200 M2 High-Density Rack Server

http://www.cisco.com/en/US/products/ps10891/index.html

- Cisco UCS C210 M2 General-Purpose Rack Server

http://www.cisco.com/en/US/products/ps10889/index.html

- Cisco UCS C260 M2 Rack Server

http://www.cisco.com/en/US/products/ps11588/index.html

## VMware Requirements

Cisco Unified SRST Manager requires VMware ESXi 4.1, 5.0, 5.1 or 5.5.

For details about VMware feature support, see Administration Guide for Cisco Unified SRST Manager.

### Setting up the VMware ESXi Environment

After configuring the server hardware, install VMware vSphere ESXi. For instructions, see:

Implementing Virtualization Deployments

http://software.cisco.com/download/navigator.html?a=a&i=rch

### VMWare Tools

VMware Tools are drivers installed in a guest operating system, providing support for a variety of system functions. The VMware Tools are included in the OVA template used for installing Cisco Unified SRST Manager.

Note The VMware Tools included in the Cisco Unified SRST Manager installation OVA template are the correct version for the Cisco Unified SRST Manager release. Do not upgrade the VMware Tools.

## Installing Cisco Unified SRST Manager

Perform the following steps to install Cisco Unified SRST Manager. These steps provide a high-level view of the installation and include links to individual sections for details.

Step 1 Download the Cisco Unified SRST Manager OVA template from Cisco.com.

See: Downloading the Cisco Unified SRST Manager OVA Template

Step 2 Deploy the OVA on the server.

See: Deploying the OVA Template

Step 3 Configure the networking and other Cisco Unified SRST Manager settings, according to the details of your network.

See: Configuring Cisco Unified SRST Manager after Installation

Step 4 Set up communication between Cisco Unified SRST Manager and the communications manager.

See: Setting Up Communications with CUCM

Step 5 Acquire and provision remote sites and SRST references.

See: Acquiring and Provisioning SRST Sites

### Downloading the Cisco Unified SRST Manager OVA Template

To download the Cisco Unified SRST Manager OVA template (virtual machine template), perform the following steps:

Step 1 Open the Cisco Unified Survivable Remote Site Telephony site: https://software.cisco.com/download/release.html?mdfid=268439627&softwareid=284490609&release=9.0.6&relind=AVAILABLE&rellifecycle=&reltype=latest&i=rm

Step 2 If prompted, log in, using your Cisco.com user name and password.

Step 3 Locate the OVA template in the “Download Software” section and download the file.

### Deploying the OVA Template

After downloading the Cisco Unified SRST Manager OVA template, use the following procedure to deploy the virtual machine template.

Prerequisites

The following are prerequisites for this procedure:

- Cisco Unified SRST Manager OVA template for installation.

- Server with VMware ESXi environment installed.

- VMware vCenter vSphere Client installed and operating.

Step 1 In the vCenter vSphere Client GUI, select File > Deploy OVF Template…

A dialog box opens for selecting a file.

Step 2 Browse to the downloaded Cisco Unified SRST Manager OVA template file. Click Open .

Step 3 In the Deploy OVF Template dialog box, click Next .

Step 4 In the Name field, enter a name for the device. This name determines how the device will appear in the left pane of the vCenter window.

Step 5 Click Next . The Deploy OVF Template dialog box displays the available server host(s) that are running ESXi.

Step 6 If there are multiple server hosts running ESXi, select the host on which you want Cisco Unified SRST Manager to run. Click Next .

The Deploy OVF Template dialog box displays disk format options.

Step 7 Select Thin provisioned format . This optimizes the data storage utilization.

Step 8 Click Next .

The Deploy OVF Template dialog box displays the available networks.

Step 9 In the Destination Networks column, select the network for Cisco Unified SRST Manager to use to communicate with Communications Manager and the remote sites.

Step 10 Click Next .

The Deploy OVF Template dialog box displays a summary of the options that you have configured.

Step 11 Click Finish to deploy Cisco Unified SRST Manager.

A dialog box indicates when the deployment is complete.

### Configuring Cisco Unified SRST Manager after Installation

After deploying the OVA template, perform the following procedure to configure Cisco Unified SRST Manager.

Prerequisites

The following are prerequisites for this procedure:

- VMware vCenter vSphere Client installed and operating.

- Cisco Unified SRST Manager OVA template deployed.

Step 1 In the vCenter vSphere Client GUI, in the left pane, select the Cisco Unified SRST Manager device. The name of the device is the name configured during installation. Example : “SRST-Manager”

Step 2 Open the console. To do this, click the Console icon in the vCenter toolbar. A console window appears for the SRST-Manager device.

Step 3 In the console window, click the Power On icon (appears as a green “Play” button).

The device boots, displaying the boot output in the console. When the start-up is complete, the console displays a message, prompting you to start configuration.

Step 4 At the prompt in the console window, confirm that you want to start the configuration process.

Step 5 To proceed, accept the license that is displayed in the console window.

By accepting the license you are acknowledging that you are using the E-SRST solution. Cisco Unified SRST Manager has no additional license fee.

Step 6 When prompted, enter the IP address of the device.

Step 7 When prompted, enter the netmask of the device.

Note Cisco Unified SRST Manager requires IP communication access to: • Cisco Unified Communications Manager • Remote sites

Step 8 When prompted, enter the default gateway address.

Step 9 Confirm that the configuration is correct.

Step 10 When prompted for the host name, enter the name by which Cisco Unified SRST Manager will appear within your network. Use a name that conforms to the fully qualified domain name (FQDN) rules. Example : SRSTMGR

Step 11 When prompted for a domain, enter a domain. Example : srtgme.com

Note Configuring DNS server is optional. If DNS server is not configured, Cisco Unified SRST Manager gets the mapping of IP address to hostname and vice-versa, from “Extension: SubjectAltName” section of CUCM certificate.

Step 12 When prompted regarding using DNS, enter “ y ” to configure Cisco Unified SRST Manager to use DNS.

Step 13 Enter the IP for the primary DNS server.

Step 14 Enter the IP for a secondary DNS server if one is available. Otherwise, press Enter .

Step 15 When prompted for the primary network time protocol (NTP) server, enter the server domain name or IP. In some cases, a default server IP appears automatically, and you can press Enter to accept it.

Note Cisco Unified SRST Manager requires a NTP server.

Step 16 When prompted for the secondary NTP server, enter the server domain name or IP if you have a secondary NTP. Otherwise, press Enter .

Step 17 When prompted for time zone information, use the menus to set your local time zone, and confirm when prompted.

Cisco Unified SRST Manager restarts.

Step 18 When prompted, enter an administrator user ID. Example : admin

Step 19 Enter a password for the account, and confirm.

When this procedure is complete, Cisco Unified SRST Manager indicates that the system is online and displays a command line prompt. Example : SYSTEM ONLINE

SRSTMGR#

### Setting Up Communications with CUCM

Perform the following procedures to configure communication between Cisco Unified SRST Manager and Cisco Unified Communications Manager (CUCM).

- Procedure 1: Transferring a Tomcat Certificate from CUCM to Cisco Unified SRST Manager

This procedure transfers an authentication certificate from Cisco Unified Communications Manager (CUCM) to Cisco Unified SRST Manager to enable secure communications with CUCM.

- Procedure 2: Configuring Communication between Cisco Unified SRST Manager and CUCM

This procedure completes the configuration of communications between Cisco Unified SRST Manager and Cisco Unified Communications Manager (CUCM).

Prerequisites

The following are prerequisites for this procedure.

- Cisco Unified Communications Manager (CUCM) is operating and available.

- SRST is operating and available.

Procedure 1: Transferring a Tomcat Certificate from CUCM to Cisco Unified SRST Manager

Step 1 Open Communications Manager and download the Tomcat certificate, as follows.

a. In a browser, open the CUCM interface.

b. In the Navigation menu at the top-right corner of the page, select Cisco Unified OS Administration , and click Go .

c. Enter a user name and password.

The Cisco Unified OS Administration page opens.

d. Select Security > Certificate Management .

The Certificate List page opens.

e. Display the certificates and locate the tomcat.der certificate. Click the hyperlinked name of the tomcat.der certificate. (Note: Do not select the tomcat.pem certificate.)

The Certificate Configuration page opens.

f. Click the Download button to download the certificate.

Step 2 In another browser tab or window, open Cisco Unified SRST Manager.

Step 3 Enter a user name and password to log in.

Step 4 Install the Tomcat certificate downloaded from CUCM, as follows.

a. In the System tab, select Trusted TLS Certificates . The TLS Certificates page opens.

b. Click the Add button.

The Add Trusted TLS Certificate page opens.

c. In the Label field, enter a name that describes the certificate. Example : CUCM

d. Click the Browse button to open the File Upload dialog box. Browse to the location of the certificate, select the certificate, and click Open .

e. On the Add Trusted TLS Certificate page, click the Update button.

The TLS Certificates page opens, showing the new certificate, identified by the label that you entered for it.

When this procedure is complete, the certificate is installed in Cisco Unified SRST Manager, enabling secure communication with CUCM.

Procedure 2: Configuring Communication between Cisco Unified SRST Manager and CUCM

Step 1 In Cisco Unified SRST Manager, open the Configure tab and click Central Call Agents .

The Central Call Agents page opens.

Step 2 Click the Add button to add CUCM.

The initial page of the Add Central Call Agent Wizard page opens.

Step 3 Click the Next button on the initial page.

Step 4 On the CUCM Hostname page, in the Hostname or IP Address field, enter the host name or IP address of CUCM.

Step 5 Click Next .

The CUCM AXL Interface page opens.

Step 6 Enter the user name and password of the AXL user on CUCM. For example, you can enter the default administrator user account created on CUCM.

Step 7 Click Next .

A confirmation dialog box indicates that Cisco Unified SRST Manager will contact CUCM to download the configured cluster nodes.

Step 8 Click OK in the dialog box.

The CUCM Cluster page opens. The page displays the CUCM primary node, which indicates that Cisco Unified SRST Manager has integrated successfully with CUCM.

Step 9 If the primary CUCM node is part of a cluster, the CUCM administrator may want to have a secondary node (a subscriber) available for Cisco Unified SRST Manager provisioning failover, in case the primary node (publisher) goes down. To configure a subscriber node, do the following:

a. Click Cluster Nodes > Retrieve Nodes .

b. In the Profile tab, select the subscriber server you want as the secondary node.

Step 10 Click Next .

The CUCM Schedule page opens. Using the scheduling fields on this page, you can configure automatic updates to the remote sites on the network. The default is daily at 12:00 AM.

Step 11 In the Call Agent Time Zone field, select the time zone of CUCM.

Step 12 Click Next .

The CUCM Enable page opens.

Step 13 Verify that provisioning is enabled.

Step 14 Click Finish .

The Central Call Agents page opens. A link for CUCM appears in the list.

When this procedure is complete, Cisco Unified SRST Manager communication with CUCM is fully configured.

### Acquiring and Provisioning SRST Sites

Perform the following procedure to discover and provision the SRST sites.

Prerequisites

The following are prerequisites for this procedure.

- Cisco Unified Communications Manager (CUCM) is operating and available.

- SRST is operating and available.

- Communication has been established between Cisco Unified SRST Manager and Cisco Unified Communications Manager (CUCM).

Step 1 In Cisco Unified SRST Manager, in the Central Call Agents page, click the link for CUCM.

The CUCM Profile page opens.

Step 2 Click the SRST References button to display the references.

Step 3 Click the Retrieve SRST References button.

Cisco Unified SRST Manager communicates with CUCM to retrieve information about remote sites and SRST References. The new SRST references appear in the list on the SRST References page.

Step 4 Provision the SRST references, as follows.

a. In Cisco Unified SRST Manager, open the Configure tab, and select Sites . The Sites page opens, displaying the available sites.

b. For each site that you want to provision, select the check box in the Filter column.

c. Click the Provision Selected Sites button.

Cisco Unified SRST Manager provisions the SRST sites.

## Migration to Cisco Unified SRST Manager

Migrating from an existing server to a VMware-based Cisco Unified SRST Manager utilizes backup and restore procedures to save configuration data from the existing installation and migrate the data to the new installation.

Step 1 On the existing installation, perform a manual backup. In the backup, include both of the following:

- Configuration

- Data

See the section about manually starting a backup in Administration Guide for Cisco Unified SRST Manager.

Step 2 Install Cisco Unified SRST Manager on a server, using an OVA template, as described in this guide.

Step 3 When the installation is complete, perform a restore to migrate the configuration and data from the previous installation.

See the section about manually restoring from a backup in Administration Guide for Cisco Unified SRST Manager .

## Upgrading Cisco Unified SRST Manager

The process of upgrading from an existing installation of Cisco Unified SRST Manager to a new version is similar to the migration procedure. The upgrade process is useful for maintenance releases and major releases. Upgrading utilizes backup and restore procedures to save configuration data from the existing installation and migrate the data to the new installation.

Step 1 On the existing installation, perform a manual backup. In the backup, include both of the following:

- Configuration

- Data

See the section about manually starting a backup in Administration Guide for Cisco Unified SRST Manager .

Step 2 Install the new version of Cisco Unified SRST Manager on a server, using an OVA template, as described in this guide.

Step 3 Power off the virtual machine operating the old Cisco Unified SRST Manager installation. This ensures that the IP address assignment for the new installation will not conflict with the IP address of the old installation.

Step 4 When the installation of the new system is complete, perform a restore to migrate the configuration and data from the previous installation.

See the section about manually restoring from a backup in Administration Guide for Cisco Unified SRST Manager .

Step 5 After confirming that the new version functions correctly, uninstall/remove the old version of Cisco Unified SRST Manager within the ESXi environment.

For information about uninstalling an OVA template, see the documentation for the ESXi client documentation.

## Cisco Unified SRST Manager Licensing

Cisco Unified SRST Manager is licensed software, provided without charge to Cisco customers, for use in the Enhanced Survivable Remote Site Telephony (E-SRST) solution. Installation requires acceptance of the terms of the license.

## Related Documentation

- Technical specifications of Cisco Unified Communications virtualized servers are available at the following URL:

http://www.cisco.com/en/US/prod/collateral/voicesw/ps6790/ps5748/ps378/solution_overview_c22-597556.html

- TCP and UDP ports for vCenter Server, ESX hosts, and other network components’ management access are listed in article 1012382 at the VMware Knowledge Base site, at the following URL:

http://kb.vmware.com

Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

### Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks . Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)

Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

### Any Internet Protocol (IP) addresses and phone numbers used in this document are not intended to be actual addresses and phone numbers. Any examples, command display output, network topology diagrams, and other figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses or phone numbers in illustrative content is unintentional and coincidental.

© 2005-2015 Cisco Systems, Inc. All rights reserved.

### © 2005-2015 Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- Unified Survivable Remote Site Telephony

| For information on... | See... |
|---|---|
| Hardware requirements | UC Virtualization Supported Hardware http://docwiki.cisco.com/wiki/UC_Virtualization_Supported_Hardware |
| VMware installation and configuration | Implementing Virtualization Deployments http://docwiki.cisco.com/wiki/Implementing_Virtualization_Deployments |