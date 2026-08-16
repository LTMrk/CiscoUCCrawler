---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su4-systemconfig-cucm-b-system-configuration-guide-1251su4--382ae1350a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU4/systemConfig/cucm_b_system-configuration-guide-1251su4/cucm_m_install-dial-and-national-numbering.html
retrieved_at: 2026-08-16T17:39:16.372357+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4 to 12.5(1)SU7

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU4 to 12.5(1)SU7

Updated: July 31, 2025

Chapter: Install a National Numbering Plan

## Chapter: Install a National Numbering Plan

# Install a National Numbering Plan

## National Numbering Plan Overview

Unified Communications Manager provides a default North American Numbering Plan (NANP). For countries with different dial
                              plan requirements, you can install a Cisco International Dial Plan and use it to create a unique numbering plan that is specific
                              to your requirements.

The numbering plan contains the Discard Digits Instructions (DDIs) and tags specific to that numbering plan. You can use these
                              items when configuring call routing to create routing rules that are applicable to the numbering plan.

This chapter describes how to install a National Numbering Plan. For more information about using a national numbering plan,
                              see the Unified Communications Manager Dial Plan Deployment Guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

## National Numbering Plan Prerequisites

If you are installing a National Numbering Plan for countries outside of North America, download the Cisco Option Package
                              (COP) file that contains the international dial plans for the current release. The COP file uses the naming convention IDP
                              v. x , and is available from the Cisco website:

https://software.cisco.com/download/navigator.html

Place the file on an external FTP or SFTP server that Unified Communications Manager can access.

## National Numbering  Plan Installation Task Flow

Step 1

Install the COP file

Optional . To install a numbering plan for countries outside of North America, download the Cisco Option Package (COP) file that contains
                                          the international dial plans for the current release.

Step 2

Install a National Numbering Plan

Install the national numbering plan on each Unified Communications Manager node in the cluster. Perform this procedure only if you are installing a National Numbering Plan for countries outside of
                                          North America.

Step 3

Restart the CallManager Service

The changes take effect after you restart the service.

### Install the COP file

Use this procedure to install a Cisco Option Package (COP)  file that contains international dial plans.

Step 1

Begin this procedure on the Unified Communications Manager publisher node. From Cisco Unified Communications OS Administration, choose Software Upgrades > Install .

Step 2

In the Source field, choose Remote File System .

Step 3

Configure the fields on the Software Installation/Upgrade window. See the Related Topics for more information about the fields and their configuration options.

Step 4

Click Next .

Step 5

From the Options/Upgrades drop-down list, choose the DP COP file and click Next .

Step 6

When the Checksum window appears, verify the checksum value against the checksum for the file that you downloaded.

Step 7

Click Next to proceed with the software upgrade.

Step 8

Click Install .

Step 9

Click Finish .

Step 10

Repeat this procedure on the Unified Communications Manager subscriber nodes. You must install the COP file on all the nodes in the cluster.

#### COP File Installation Fields

Field

Description

Directory

Enter the directory where the COP file is located.

Remote Server

Enter the host name or IP address of the server where COP file is located.

Remote User

Enter the user name for the remote server.

Remote Password

Enter the password for the remote server.

Transfer Protocol

Select a protocol to use when connecting with the remote server.

### Install a National Numbering Plan

Perform this procedure only if you are installing a national numbering plan for countries outside of  North America.

Install the national numbering plan on each Unified Communications Manager node in the cluster. Begin with the Unified Communications Manager publisher node.

Step 1

From Cisco
                                          			 Unified Communications Manager Administration, choose Call Routing > Dial Plan
                                                				  Installer .

Step 2

Enter search criteria and click Find .

Step 3

Choose the
                                          			 dial plan version that you want to install from the Available Version drop-down
                                          			 list.

Step 4

Click Install .

Step 5

Repeat this
                                          			 procedure for every subscriber node in the cluster.

### Restart the CallManager Service

Step 1

From the Cisco Unified Serviceability interface, choose Tools > Control Center - Feature Services .

Step 2

Choose the Unified Communications Manager server from the Servers drop-down list.

Step 3

Click the radio button that corresponds to the Cisco CallManager service.

Step 4

Click Restart .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Install the COP file | Optional . To install a numbering plan for countries outside of North America, download the Cisco Option Package (COP) file that contains
                                          the international dial plans for the current release. |
| Step 2 | Install a National Numbering Plan | Install the national numbering plan on each Unified Communications Manager node in the cluster. Perform this procedure only if you are installing a National Numbering Plan for countries outside of
                                          North America. |
| Step 3 | Restart the CallManager Service | The changes take effect after you restart the service. |

| Step 1 | Begin this procedure on the Unified Communications Manager publisher node. From Cisco Unified Communications OS Administration, choose Software Upgrades > Install . The Software Installation/Upgrade window appears. |
|---|---|
| Step 2 | In the Source field, choose Remote File System . |
| Step 3 | Configure the fields on the Software Installation/Upgrade window. See the Related Topics for more information about the fields and their configuration options. |
| Step 4 | Click Next . The window refreshes with a list of available software options and upgrades. |
| Step 5 | From the Options/Upgrades drop-down list, choose the DP COP file and click Next . The Installation File window opens and downloads the file from the FTP server. The window displays the progress of the download. |
| Step 6 | When the Checksum window appears, verify the checksum value against the checksum for the file that you downloaded. |
| Step 7 | Click Next to proceed with the software upgrade. A warning message displays the DP COP file that you selected to install. |
| Step 8 | Click Install . The Install Status window appears. |
| Step 9 | Click Finish . |
| Step 10 | Repeat this procedure on the Unified Communications Manager subscriber nodes. You must install the COP file on all the nodes in the cluster. |

| Field | Description |
|---|---|
| Directory | Enter the directory where the COP file is located. |
| Remote Server | Enter the host name or IP address of the server where COP file is located. |
| Remote User | Enter the user name for the remote server. |
| Remote Password | Enter the password for the remote server. |
| Transfer Protocol | Select a protocol to use when connecting with the remote server. |

| Step 1 | From Cisco
                                          			 Unified Communications Manager Administration, choose Call Routing > Dial Plan
                                                				  Installer . |
|---|---|
| Step 2 | Enter search criteria and click Find . |
| Step 3 | Choose the
                                          			 dial plan version that you want to install from the Available Version drop-down
                                          			 list. |
| Step 4 | Click Install . The
                                          			 Status displays that the dial plan has been installed. |
| Step 5 | Repeat this
                                          			 procedure for every subscriber node in the cluster. |

| Step 1 | From the Cisco Unified Serviceability interface, choose Tools > Control Center - Feature Services . |
|---|---|
| Step 2 | Choose the Unified Communications Manager server from the Servers drop-down list. In the CM Services area, Cisco CallManager displays in the Service Name column. |
| Step 3 | Click the radio button that corresponds to the Cisco CallManager service. |
| Step 4 | Click Restart . The service restarts and displays the message, Service Successfully Restarted . |