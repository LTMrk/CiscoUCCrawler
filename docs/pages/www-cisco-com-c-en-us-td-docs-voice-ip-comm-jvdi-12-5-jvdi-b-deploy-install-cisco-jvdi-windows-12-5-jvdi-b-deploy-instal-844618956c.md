---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-5-jvdi-b-deploy-install-cisco-jvdi-windows-12-5-jvdi-b-deploy-instal-844618956c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_5/jvdi_b_deploy-install-cisco-jvdi-windows-12-5/jvdi_b_deploy-install-cisco-jvdi-windows-12-5_chapter_0100.html
retrieved_at: 2026-08-22T00:41:20.812524+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone—VDI Windows Release 12.5

# Deployment and Installation Guide for Cisco Jabber Softphone—VDI Windows Release 12.5

Updated: November 29, 2018

Chapter: Upgrade

## Chapter: Upgrade

# Upgrade

## Upgrade Workflow

To enable the Unified Communications features, upgrade all the following components:

The platform image on the thin client

Cisco Jabber Softphone for VDI — Cisco JVDI Client (thin client) and Cisco JVDI Agent (HVD)

Cisco Unified Communications software on the hosted virtual desktop (HVD)

The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same.

The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. The Cisco JVDI Client version can be the same, or up to two
                                          releases earlier. The available feature set is determined by the earlier software version.

Read the Release Notes document for your release of Cisco Jabber Softphone for VDI , available from http://www.cisco.com/c/en/us/support/collaboration-endpoints/virtualization-experience-media-edition/products-release-notes-list.html .

Review the important notes for information about limitations or restrictions that may affect your deployment.

See Requirements .

Review the system requirements to confirm that all required hardware and software meet them. Failure to meet all requirements
                                          can result in a nonfunctional deployment.

Have all users log out of the hosted virtual desktops.

If Cisco Virtualization Experience Media Edition is installed, uninstall it.

Install the Cisco Jabber Softphone for VDI components on the thin clients and hosted virtual desktops.

See Install the Components Workflow .

## Upgrade Cisco Jabber for Windows

Use this procedure to upgrade to a supported maintenance release of Cisco Jabber for Windows. For supported Cisco Jabber versions, see the "System Requirements" section in the Release Notes for Cisco Jabber Softphone for Windows for your release.

The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same.

The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. The Cisco JVDI Client version can be the same, or up to two
                                          releases earlier. The available feature set is determined by the earlier software version.

Close Cisco Jabber and ensure that it is not running on the HVD.

If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization.

Install Cisco Jabber .

## Upgrade the Citrix Receiver or the VMware Client

Perform this procedure to upgrade the Citrix Receiver or the VMware Horizon Client, with Cisco Jabber Softphone for VDI already installed. This procedure repairs Cisco JVDI Client .

Upgrade the Citrix Receiver or the VMware Horizon Client.

See the documentation for your Citrix or VMware product.

Use one of the following methods to install Cisco JVDI Client :

Run the Microsoft Installer

Use the Command Line

Use the Group Policy Editor

## Change the Hosted Virtual Desktop Connection Type

If you change the hosted virtual desktop connection type, you can use this procedure to repair Cisco Jabber Softphone for VDI .

You can change your connection type as follows:

Citrix Receiver to VMware Horizon Client

VMware Horizon Client to Citrix Receiver

Install the software for the new connection type, either Citrix Receiver or VMware Horizon Client.

Double click the CiscoJVDISetup.msi file.

To open the executable file, select OK .

If the Open File–Security Warning appears, select Run .

In the Welcome window, select Next .

In the Program Maintenance window, select Modify and then Next .

In the Custom setup window, select Citrix Client Support or VMware Client Support depending on which you installed and select Next .

To proceed with modifying the installation, select Install .

During the modification of Cisco JVDI Client only components that were installed with the previous version are reinstalled.

To complete the installation, select Finish .

| Important | To enable the Unified Communications features, upgrade all the following components: The platform image on the thin client Cisco Jabber Softphone for VDI — Cisco JVDI Client (thin client) and Cisco JVDI Agent (HVD) Cisco Unified Communications software on the hosted virtual desktop (HVD) The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same. The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. The Cisco JVDI Client version can be the same, or up to two
                                          releases earlier. The available feature set is determined by the earlier software version. |
|---|---|

| Step 1 | Read the Release Notes document for your release of Cisco Jabber Softphone for VDI , available from http://www.cisco.com/c/en/us/support/collaboration-endpoints/virtualization-experience-media-edition/products-release-notes-list.html . Review the important notes for information about limitations or restrictions that may affect your deployment. |
|---|---|
| Step 2 | See Requirements . Review the system requirements to confirm that all required hardware and software meet them. Failure to meet all requirements
                                          can result in a nonfunctional deployment. |
| Step 3 | Have all users log out of the hosted virtual desktops. |
| Step 4 | If Cisco Virtualization Experience Media Edition is installed, uninstall it. |
| Step 5 | Install the Cisco Jabber Softphone for VDI components on the thin clients and hosted virtual desktops. See Install the Components Workflow . |

| Important | The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same. The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. The Cisco JVDI Client version can be the same, or up to two
                                          releases earlier. The available feature set is determined by the earlier software version. |
|---|---|

| Step 1 | Close Cisco Jabber and ensure that it is not running on the HVD. Important If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. | Important | If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. |
|---|---|---|---|
| Important | If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. |
| Step 2 | Install Cisco Jabber . |

| Important | If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. |
|---|---|

| Step 1 | Upgrade the Citrix Receiver or the VMware Horizon Client. See the documentation for your Citrix or VMware product. |
|---|---|
| Step 2 | Use one of the following methods to install Cisco JVDI Client : Run the Microsoft Installer Use the Command Line Use the Group Policy Editor |

| Step 1 | Install the software for the new connection type, either Citrix Receiver or VMware Horizon Client. |
|---|---|
| Step 2 | Double click the CiscoJVDISetup.msi file. |
| Step 3 | To open the executable file, select OK . |
| Step 4 | If the Open File–Security Warning appears, select Run . |
| Step 5 | In the Welcome window, select Next . |
| Step 6 | In the Program Maintenance window, select Modify and then Next . |
| Step 7 | In the Custom setup window, select Citrix Client Support or VMware Client Support depending on which you installed and select Next . |
| Step 8 |  |
| Step 9 | To proceed with modifying the installation, select Install . Note During the modification of Cisco JVDI Client only components that were installed with the previous version are reinstalled. | Note | During the modification of Cisco JVDI Client only components that were installed with the previous version are reinstalled. |
| Note | During the modification of Cisco JVDI Client only components that were installed with the previous version are reinstalled. |
| Step 10 | To complete the installation, select Finish . |

| Note | During the modification of Cisco JVDI Client only components that were installed with the previous version are reinstalled. |
|---|---|