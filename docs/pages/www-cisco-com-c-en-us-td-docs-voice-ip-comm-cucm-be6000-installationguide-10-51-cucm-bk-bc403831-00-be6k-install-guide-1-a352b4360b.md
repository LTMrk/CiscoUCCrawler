---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-installationguide-10-51-cucm-bk-bc403831-00-be6k-install-guide-1-a352b4360b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/InstallationGuide/10_51/CUCM_BK_BC403831_00_be6k-install-guide-1051/CUCM_BK_BC403831_00_be6k-install-guide-1051_chapter_011.html
retrieved_at: 2026-08-21T22:55:14.465974+00:00
---

Cisco Business Edition 6000 Installation Guide, Release 10.5(1)

# Cisco Business Edition 6000 Installation Guide, Release 10.5(1)

Updated: June 6, 2014

Chapter: Initial Configuration

## Chapter: Initial Configuration

Contents

# Initial Configuration

## Browse, Setup, and Apply Licenses

Follow these steps to access each application, perform first-time setup for some applications, and apply the licenses.

- Paging Server: Collect information about the application URL from the virtual machine console. The default first-time username and password are admin and changeMe .

- Cisco Prime Collaboration Provisioning: Browse to the IP address and use globaladmin as the username.

- Cisco Prime Collaboration: Download the license, tool and readme file from datastore.    Use the instructions in the readme file to apply the license (a permanent license with no expiration).

- Cisco Unified Contact Center Express: Demo licenses have a 30 day evaluation period. You must extract the demo license files from the ISO file. After you have demo license files on your PC, browse to the ESXi portal of Unified Contact Center Express and follow the instructions to apply the demo license.

- Prime Collaboration Provisioning: No PAK is needed because the product comes with a permanent license that needs to be installed.

- Paging Server: No PAK is needed because the product comes with a permanent license for basic paging.

Cisco Prime License Manager (ELM) is automatically installed as part of the Unified Communications manager installation.

- Cisco VCS, Expressway, TS, and Conductor: After registering the PAK for VCS, the customer receives two keys (Release key and Option key). In the administration portal, select Maintenance > Option keys . Apply the Release key first, and then apply the Option key.

A valid UCCS subscription is required to use the PUT to download upgrade images.

## Where To Go From Here

After you verify successful installation, see the Prime Collaboration Provisioning Guide for Cisco Business Edition 6000 in the Cisco Business Edition 6000 Support Documents. Use this guide to start the initial configuration of Unified Communications Manager, Cisco Unity Connection and IM and Presence Service applications.

# Initial Configuration

## Browse, Setup, and Apply Licenses

Follow these steps to access each application, perform first-time setup for some applications, and apply the licenses.

- Paging Server: Collect information about the application URL from the virtual machine console. The default first-time username and password are admin and changeMe .

- Cisco Prime Collaboration Provisioning: Browse to the IP address and use globaladmin as the username.

- Cisco Prime Collaboration: Download the license, tool and readme file from datastore.    Use the instructions in the readme file to apply the license (a permanent license with no expiration).

- Cisco Unified Contact Center Express: Demo licenses have a 30 day evaluation period. You must extract the demo license files from the ISO file. After you have demo license files on your PC, browse to the ESXi portal of Unified Contact Center Express and follow the instructions to apply the demo license.

- Prime Collaboration Provisioning: No PAK is needed because the product comes with a permanent license that needs to be installed.

- Paging Server: No PAK is needed because the product comes with a permanent license for basic paging.

Cisco Prime License Manager (ELM) is automatically installed as part of the Unified Communications manager installation.

- Cisco VCS, Expressway, TS, and Conductor: After registering the PAK for VCS, the customer receives two keys (Release key and Option key). In the administration portal, select Maintenance > Option keys . Apply the Release key first, and then apply the Option key.

A valid UCCS subscription is required to use the PUT to download upgrade images.

Product License Registration

Cisco Product Upgrade Tool (PUT)

## Where To Go From Here

After you verify successful installation, see the Prime Collaboration Provisioning Guide for Cisco Business Edition 6000 in the Cisco Business Edition 6000 Support Documents. Use this guide to start the initial configuration of Unified Communications Manager, Cisco Unity Connection and IM and Presence Service applications.

| Step 1 | To access the administration portal for each individual application, browse to the IP address of application. Consider the following information: Paging Server: Collect information about the application URL from the virtual machine console. The default first-time username and password are admin and changeMe . Cisco Prime Collaboration Provisioning: Browse to the IP address and use globaladmin as the username. |
|---|---|
| Step 2 | Some applications come with a preinstalled demo license for a 60 day evaluation period. Two applications have the following exceptions: Cisco Prime Collaboration: Download the license, tool and readme file from datastore.    Use the instructions in the readme file to apply the license (a permanent license with no expiration). Cisco Unified Contact Center Express: Demo licenses have a 30 day evaluation period. You must extract the demo license files from the ISO file. After you have demo license files on your PC, browse to the ESXi portal of Unified Contact Center Express and follow the instructions to apply the demo license. |
| Step 3 | After purchasing the license, you should  receive the Product Authorization Key (PAK) through email from Cisco. The PAK should then be registered to "Product License Registration" to receive license key in form of a software file. |
| Step 4 | Apply license keys in the application using the administration portal: Prime Collaboration Provisioning: No PAK is needed because the product comes with a permanent license that needs to be installed. Paging Server: No PAK is needed because the product comes with a permanent license for basic paging. Unified Communications Manager and Cisco Unity Connection: Browse the IP Address of Unified Communications Manager and click Cisco Prime License Manager . Select License > Install License File and follow instructions. Note Cisco Prime License Manager (ELM) is automatically installed as part of the Unified Communications manager installation. Cisco VCS, Expressway, TS, and Conductor: After registering the PAK for VCS, the customer receives two keys (Release key and Option key). In the administration portal, select Maintenance > Option keys . Apply the Release key first, and then apply the Option key. | Note | Cisco Prime License Manager (ELM) is automatically installed as part of the Unified Communications manager installation. |
| Note | Cisco Prime License Manager (ELM) is automatically installed as part of the Unified Communications manager installation. |
| Step 5 | When you need to upgrade the software version, use the Cisco Product Upgrade Tool (PUT). Note A valid UCCS subscription is required to use the PUT to download upgrade images. | Note | A valid UCCS subscription is required to use the PUT to download upgrade images. |
| Note | A valid UCCS subscription is required to use the PUT to download upgrade images. |

| Note | Cisco Prime License Manager (ELM) is automatically installed as part of the Unified Communications manager installation. |
|---|---|

| Note | A valid UCCS subscription is required to use the PUT to download upgrade images. |
|---|---|

| Step 1 | To access the administration portal for each individual application, browse to the IP address of application. Consider the following information: Paging Server: Collect information about the application URL from the virtual machine console. The default first-time username and password are admin and changeMe . Cisco Prime Collaboration Provisioning: Browse to the IP address and use globaladmin as the username. |
|---|---|
| Step 2 | Some applications come with a preinstalled demo license for a 60 day evaluation period. Two applications have the following exceptions: Cisco Prime Collaboration: Download the license, tool and readme file from datastore.    Use the instructions in the readme file to apply the license (a permanent license with no expiration). Cisco Unified Contact Center Express: Demo licenses have a 30 day evaluation period. You must extract the demo license files from the ISO file. After you have demo license files on your PC, browse to the ESXi portal of Unified Contact Center Express and follow the instructions to apply the demo license. |
| Step 3 | After purchasing the license, you should  receive the Product Authorization Key (PAK) through email from Cisco. The PAK should then be registered to "Product License Registration" to receive license key in form of a software file. |
| Step 4 | Apply license keys in the application using the administration portal: Prime Collaboration Provisioning: No PAK is needed because the product comes with a permanent license that needs to be installed. Paging Server: No PAK is needed because the product comes with a permanent license for basic paging. Unified Communications Manager and Cisco Unity Connection: Browse the IP Address of Unified Communications Manager and click Cisco Prime License Manager . Select License > Install License File and follow instructions. Note Cisco Prime License Manager (ELM) is automatically installed as part of the Unified Communications manager installation. Cisco VCS, Expressway, TS, and Conductor: After registering the PAK for VCS, the customer receives two keys (Release key and Option key). In the administration portal, select Maintenance > Option keys . Apply the Release key first, and then apply the Option key. | Note | Cisco Prime License Manager (ELM) is automatically installed as part of the Unified Communications manager installation. |
| Note | Cisco Prime License Manager (ELM) is automatically installed as part of the Unified Communications manager installation. |
| Step 5 | When you need to upgrade the software version, use the Cisco Product Upgrade Tool (PUT). Note A valid UCCS subscription is required to use the PUT to download upgrade images. | Note | A valid UCCS subscription is required to use the PUT to download upgrade images. |
| Note | A valid UCCS subscription is required to use the PUT to download upgrade images. |

| Note | Cisco Prime License Manager (ELM) is automatically installed as part of the Unified Communications manager installation. |
|---|---|

| Note | A valid UCCS subscription is required to use the PUT to download upgrade images. |
|---|---|