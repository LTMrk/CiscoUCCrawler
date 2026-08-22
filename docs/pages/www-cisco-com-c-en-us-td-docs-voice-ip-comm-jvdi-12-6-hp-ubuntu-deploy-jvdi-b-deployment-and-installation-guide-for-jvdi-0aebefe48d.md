---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-6-hp-ubuntu-deploy-jvdi-b-deployment-and-installation-guide-for-jvdi-0aebefe48d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_6/hp_ubuntu/deploy/jvdi_b_deployment-and-installation-guide-for-jvdi-hp-ubuntu-12-6/jvdi_b_deployment-and-installation-guide-for-jvdi-hp-ubuntu-12-6_chapter_0100.html
retrieved_at: 2026-08-22T00:34:31.867293+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.6

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.6

Updated: April 9, 2019

Chapter: Upgrade

## Chapter: Upgrade

# Upgrade

## Upgrade Notes

For assistance obtaining the required downloads from HP, contact HP support.

The following upgrade paths are supported:

From Cisco Jabber Softphone for VDI —HP Thin Pro and Ubuntu Release 12.0 to Cisco Jabber Softphone for VDI —Thin Pro and Ubuntu Release 12.6

From Cisco Jabber Softphone for VDI —HP Thin Pro and Ubuntu Release 12.1 to Cisco Jabber Softphone for VDI —Thin Pro and Ubuntu Release 12.6

From Cisco Jabber Softphone for VDI —HP Thin Pro and Ubuntu Release 12.5 to Cisco Jabber Softphone for VDI —Thin Pro and Ubuntu Release 12.6

The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. However, the JVDI Client version can be the
                              same, or up to two releases earlier (N-2 support). For example, the following version combinations are supported:

Cisco Jabber for Windows Release 12.6, Cisco JVDI Agent Release 12.6, and Cisco JVDI Client Release 12.6

Cisco Jabber for Windows Release 12.6, Cisco JVDI Agent Release 12.6, and Cisco JVDI Client Release 12.5

Cisco Jabber for Windows Release 12.6, Cisco JVDI Agent Release 12.6, and Cisco JVDI Client Release 12.1

The limitations and restrictions for the earlier JVDI Client release apply. The available features are limited to those available
                                          for the earlier release. For more information, see the Release Notes for Cisco Jabber Softphone—HP Thin Pro and Ubuntu , for the earlier release. For example, if your JVDI Client Release is 12.1, see the release notes document for Release 12.1.

## Upgrade Workflow

To enable the Unified Communications features, upgrade all the following components:

The platform image on the thin client

Cisco Jabber Softphone for VDI — Cisco JVDI Client (thin client) and Cisco JVDI Agent (HVD)

Cisco Unified Communications software on the hosted virtual desktop (HVD)

Read the Release Notes document for your release of Cisco Jabber Softphone for VDI , available from http://www.cisco.com/c/en/us/support/collaboration-endpoints/virtualization-experience-media-edition/products-release-notes-list.html .

Review the important notes for information about limitations or restrictions that may affect your deployment.

See Requirements .

Review the system requirements to confirm that all required hardware and software meet them. Failure to meet all requirements
                                          can result in a nonfunctional deployment.

Have all users log out of the hosted virtual desktops.

Install the Cisco Jabber Softphone for VDI components on the thin clients and hosted virtual desktops.

See the workflow for the corresponding platform: Install the Components Workflow—HP Thin Pro or Install the Components Workflow—Ubuntu .

## Upgrade Cisco Jabber for Windows

Use this procedure to upgrade to a supported maintenance release of Cisco Jabber for Windows. For supported Cisco Jabber versions, see the "System Requirements" section in the Release Notes for Cisco Jabber Softphone for HP Thin Pro and Ubuntu for your release.

Close Cisco Jabber and ensure that it is not running on the HVD.

If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization.

Install Cisco Jabber .

| Note | For assistance obtaining the required downloads from HP, contact HP support. |
|---|---|

| Important | The limitations and restrictions for the earlier JVDI Client release apply. The available features are limited to those available
                                          for the earlier release. For more information, see the Release Notes for Cisco Jabber Softphone—HP Thin Pro and Ubuntu , for the earlier release. For example, if your JVDI Client Release is 12.1, see the release notes document for Release 12.1. |
|---|---|

| Important | To enable the Unified Communications features, upgrade all the following components: The platform image on the thin client Cisco Jabber Softphone for VDI — Cisco JVDI Client (thin client) and Cisco JVDI Agent (HVD) Cisco Unified Communications software on the hosted virtual desktop (HVD) |
|---|---|

| Step 1 | Read the Release Notes document for your release of Cisco Jabber Softphone for VDI , available from http://www.cisco.com/c/en/us/support/collaboration-endpoints/virtualization-experience-media-edition/products-release-notes-list.html . Review the important notes for information about limitations or restrictions that may affect your deployment. |
|---|---|
| Step 2 | See Requirements . Review the system requirements to confirm that all required hardware and software meet them. Failure to meet all requirements
                                          can result in a nonfunctional deployment. |
| Step 3 | Have all users log out of the hosted virtual desktops. |
| Step 4 | Install the Cisco Jabber Softphone for VDI components on the thin clients and hosted virtual desktops. See the workflow for the corresponding platform: Install the Components Workflow—HP Thin Pro or Install the Components Workflow—Ubuntu . |

| Step 1 | Close Cisco Jabber and ensure that it is not running on the HVD. Important If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. | Important | If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. |
|---|---|---|---|
| Important | If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. |
| Step 2 | Install Cisco Jabber . |

| Important | If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. |
|---|---|