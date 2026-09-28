---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-12-5-jvdi-b-deploy-install-cisco-jvdi-elux-12-5-jvdi-b-deploy-install-c-55bfafb3f9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/12_5/jvdi_b_deploy-install-cisco-jvdi-elux-12-5/jvdi_b_deploy-install-cisco-jvdi-elux-12-5_chapter_0100.html
retrieved_at: 2026-08-22T00:37:15.377174+00:00
---

Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Unicon eLux Release 12.5

# Deployment and Installation Guide for Cisco Jabber Softphone for VDI—Unicon eLux Release 12.5

Updated: November 29, 2018

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

See Install the Components Workflow .

If your users do not require VPN access, you can skip the optional steps to install Cisco AnyConnect.

## Upgrade Cisco Jabber for Windows

Use this procedure to upgrade to a supported maintenance release of Cisco Jabber for Windows. For supported Cisco Jabber versions, see the "System Requirements" section in the Release Notes for Cisco Jabber Softphone for Unicon eLux for your release.

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
| Step 4 | Install the Cisco Jabber Softphone for VDI components on the thin clients and hosted virtual desktops. See Install the Components Workflow . If your users do not require VPN access, you can skip the optional steps to install Cisco AnyConnect. |

| Important | The Cisco Jabber for Windows version must match your Cisco Jabber Softphone for VDI version. The Cisco JVDI Agent and Cisco JVDI Client versions must be the same. The Cisco Jabber for Windows and Cisco JVDI Agent versions must always match. The Cisco JVDI Client version can be the same, or up to two
                                          releases earlier. The available feature set is determined by the earlier software version. |
|---|---|

| Step 1 | Close Cisco Jabber and ensure that it is not running on the HVD. Important If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. | Important | If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. |
|---|---|---|---|
| Important | If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. |
| Step 2 | Install Cisco Jabber . |

| Important | If Cisco Jabber is running during the installation, exit and restart Cisco Jabber to enable virtualization. |
|---|---|