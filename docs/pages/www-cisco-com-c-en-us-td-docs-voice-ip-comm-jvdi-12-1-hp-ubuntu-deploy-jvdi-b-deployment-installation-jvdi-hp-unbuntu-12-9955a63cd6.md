---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-1-hp-ubuntu-deploy-jvdi-b-deployment-installation-jvdi-hp-unbuntu-12-9955a63cd6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_1/hp_ubuntu/deploy/jvdi_b_deployment-installation-jvdi-hp-unbuntu-12-1/jvdi_b_deployment-installation-jvdi-hp-unbuntu-12-1_chapter_0100.html
retrieved_at: 2026-08-22T00:35:30.237621+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.1

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—HP Thin Pro and Ubuntu Release 12.1

Updated: July 18, 2018

Chapter: Upgrade

## Chapter: Upgrade

- Upgrade

- Upgrade Workflow

- Upgrade Cisco Jabber for Windows

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

Install the Cisco Jabber Softphone for VDI components on the thin clients and hosted virtual desktops.

See the workflow for the corresponding platform: Install the Components Workflow—HP Thin Pro or Install the Components Workflow—Ubuntu .

## Upgrade Cisco Jabber for Windows

Use this procedure to upgrade to a supported maintenance release of Cisco Jabber for Windows. For supported Cisco Jabber versions, see the "System Requirements" section in the Release Notes for Cisco Jabber Softphone for HP Thin Pro and Ubuntu for your release.

The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same.

The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. The Cisco JVDI Client version can be the same, or up to two
                                          releases earlier. The available feature set is determined by the earlier software version.

Close Cisco Jabber and ensure that it is not running on the HVD.

If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization.

Install Cisco Jabber .

| Important | To enable the Unified Communications features, upgrade all the following components: The platform image on the thin client Cisco Jabber Softphone for VDI — Cisco JVDI Client (thin client) and Cisco JVDI Agent (HVD) Cisco Unified Communications software on the hosted virtual desktop (HVD) The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same. The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. The Cisco JVDI Client version can be the same, or up to two
                                          releases earlier. The available feature set is determined by the earlier software version. |
|---|---|

| Step 1 | Read the Release Notes document for your release of Cisco Jabber Softphone for VDI , available from http://www.cisco.com/c/en/us/support/collaboration-endpoints/virtualization-experience-media-edition/products-release-notes-list.html . Review the important notes for information about limitations or restrictions that may affect your deployment. |
|---|---|
| Step 2 | See Requirements . Review the system requirements to confirm that all required hardware and software meet them. Failure to meet all requirements
                                          can result in a nonfunctional deployment. |
| Step 3 | Have all users log out of the hosted virtual desktops. |
| Step 4 | Install the Cisco Jabber Softphone for VDI components on the thin clients and hosted virtual desktops. See the workflow for the corresponding platform: Install the Components Workflow—HP Thin Pro or Install the Components Workflow—Ubuntu . |

| Important | The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same. The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. The Cisco JVDI Client version can be the same, or up to two
                                          releases earlier. The available feature set is determined by the earlier software version. |
|---|---|

| Step 1 | Close Cisco Jabber and ensure that it is not running on the HVD. Important If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. | Important | If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. |
|---|---|---|---|
| Important | If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. |
| Step 2 | Install Cisco Jabber . |

| Important | If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. |
|---|---|