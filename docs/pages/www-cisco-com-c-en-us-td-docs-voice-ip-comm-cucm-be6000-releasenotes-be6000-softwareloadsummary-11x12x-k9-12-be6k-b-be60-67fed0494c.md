---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-releasenotes-be6000-softwareloadsummary-11x12x-k9-12-be6k-b-be60-67fed0494c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/releasenotes/BE6000_SoftwareLoadSummary-11X12X-K9-12/be6k_b_be6000-load-restricted-12x13x-k9-12_chapter_00.html
retrieved_at: 2026-08-21T21:39:44.031890+00:00
---

Business Edition 6000 Software Load Summary Export Restricted Version 11X12X-K9-12

# Business Edition 6000 Software Load Summary Export Restricted Version 11X12X-K9-12

Book Contents

- Book Title Page

- Business Edition 6000 Software Load Summary

- Index

Find Matches in This Book

## Results

Updated: March 6, 2019

Chapter: Business Edition 6000 Software Load Summary

## Chapter: Business Edition 6000 Software Load Summary

# Business Edition 6000 Software Load Summary

## Introduction to
                        	 Software Load Summary

The document
                              		  identifies the software that is preloaded on the appliance's module of this
                              		  product for your convenience.

We attempt to keep
                              		  the software versions in this build as up-to-date as possible; however, newer
                              		  code may have been released after this product was manufactured.

Before using
                                          			 this software, please ensure that you have the latest versions, available
                                          			 either from Cisco Software Center (CSC), or using Cisco
                                             				Electronic Software Delivery (ESD). We provide details on how to use
                                          			 Electronic Software Delivery in an email to you when you order licenses for
                                          			 your chosen applications. Table 2 lists the files that are included and
                                          			 indicates where you can go online to download the files.

## Installed Applications - Business Edition

Business Edition 6000 appliance are shipped with preinstalled application virtual machines. These application virtual machines
                              simplify your system deployment because Unified Communications applications are installed to the “skip” configuration point.
                              When they are started, they are ready to accept configuration and complete the installation.

Use the system wizard through the virtual machine console, or provide a platformConfig.xml configuration file to configure the “skip” installed applications. Refer to the Business Edition 6000 Installation Guide for further information. The following table summarizes the installed applications for this build. New and updated software
                              is highlighted in BOLD .

Application

Version

Install Option

Pre-installation Method

Cisco Unified Communications Manager

(UCSInstall_UCOS_12.5.1.10000-22_80_vmv13_v1.0.ova)

12.5

1000 users

Partial (skip) installed application

Cisco Unified Communications Manager IM & Presence

(UCSInstall_CUP_12.5.1.10000-22_80_vmv13_v1.0.ova)

12.5

1000 users

Partial (skip) installed application

Cisco Unity Connection

(UCSInstall_CUC_12.5.1.10000-23_160_v1.0.ova)

12.5

1000 users

Partial (skip) installed application

Cisco Paging Server

(Bootable-CiscoPagingServer_12.5.1.ova)

12.5

Standard

Deployed Application OVA

Cisco Unified Contact Center Express

(UCCX_12_0_100Agent_VM11_OVA.ova)

12.0

100 Agents

Partial (skip) installed application

Cisco Prime Collaboration Provisioning

(cpc-provisioning-12.6.0.2283-small_v6.5_signed.ova)

12.6

Small

Deployed Application OVA

Cisco Prime Collaboration Deployment

(pcd_vApp_UCOS_12.5.1.10000-18_vmv8_v1.2.ova)

12.5

Deployed Application OVA

## Preloaded Applications - Business Edition 6000

The hypervisor datastore on the appliance's module includes installation files for Collaboration Solution Release 11 and 12
                              Unified Communications (UC) applications. These applications include Cisco Unified Communications Manager, Cisco Unity Connection,
                              and Cisco Unified Communications Manager Instant Messaging and Presence Server. You may install any of the other preloaded applications with either of these UC releases. Unified Communications Version 11 or 12 applications must be used together.

The following table details the files included in the datastore and indicates which to use for either a version 11 or 12 Unified
                              Communications solution.  New and updated software is shown in ITALICS .

Application or File

Filename

Access

Version 11 Solution

Version 12 Solution

- Application image

VMware-ESXi-6.5.0-8294253-Custom-Cisco-6.5.2.1.ova

VMware

—

Cisco Unified Communications Manager & Cisco Unity Connection 1

- Common version 11.5(1) SU3 UCM application image

Bootable_UCSInstall_UCOS_11.5.1.10000-6.sgn.iso

ESD

—

- 12.5 application image

ESD

—

- Version 11.5(1) recovery image

11.5.1.13900-52-recovery.iso

CSC

—

- Version 12.5 recovery image

CSC

—

- Version 12.5

CSC

—

- Version 11.5(1) Service Update 3

UCSInstall_UCOS_11.5.1.13901-3.sgn.iso

CSC

—

- Version 11.5 UCM virtual machine template

cucm_11.5_vmv8_v1.1.ova

CSC

—

- Version 11.5 CUC virtual machine template

CUC_11.5_v1.1.ova

CSC

—

- Version 11.5(1) UCM locale files

UCM-Locales-11.5.1.3000-1.iso

CSC

—

- Version 11.5(1) CUC locale files

UCN-Locales-11.5.0.1-1000-ar-SA-el-GR.iso

UCN-Locales-11.5.0.1-1000-en-AU-fr-CA.iso

UCN-Locales-11.5.0.1-1000-he-IL-nl-NL.iso

UCN-Locales-11.5.0.1-1000-pl-PL-sv-SE.iso

UCN-Locales-11.5.0.1-1000-tr-TR-zh-TW.iso

UCN-Locales-11.5.0.1-1000-ja-JP.iso

CSC

—

- Version 11.5(1) SU3 application

UCSInstall_CUP_11.5.1.13900-57.sgn.iso

ESD

—

- Version 11.5(1) SU3 recovery image

11.5.1.13900-57-recovery.iso

CSC

—

-Version 11.5 virtual machine template

cucm_im_p_11.5_vmv8_v1.4.ova

CSC

—

CSC

—

CSC

—

CSC

—

CSC

—

CSC

—

CUCM_12.5.1.10000-22_Locale.iso

CSC

—

CSC

—

CSC

—

CSC

—

CSC

—

CSC

—

CSC

—

ESD

—

ESD

—

CSC

—

CSC

—

- Application image

UCSInstall_UCCX_12_0_1_UCOS_12.0.1.10000-24.sgn.iso

ESD

Yes

—

- Virtual machine template

UCCX_12.0_vmv11_v2.6.ova

CSC

Yes

—

- Language pack

CCX-Locales-12.0.1.10000-32.iso

CSC

Yes

—

CSC

—

Yes

CSC

—

Yes

CSC

—

Yes

- TMSPE Installer

CSC

—

Yes

## Patch File

If patches and updates for the latest software are available when the manufacturing image is built, they are included in the
                              datastore for your convenience. For UC applications, patch files (also known as COP files) are bundled in iso format and stored
                              in the /OVA-ISO/App_Patches/ datastore directory. To use these files, connect the appropriate iso image to your UC virtual
                              machine, then follow your application's documentation to install the patches from “DVD.”

Check http://software.cisco.com/ for patches or updates that are released after this document was issued.

The following table details the patches included in this release. Please check release information for each patch before applying.
                              Usually, patches should be applied immediately after the application install process is completed.

Application Patches and Updates

Cisco Unified Communications Manager 11.5 (UCM11_COP_Files.iso)

Cisco Unified Presence 11 (CUP11_COP_Files.iso)

Cisco Emergency Responder 11.5 (CER11_COP_Files.iso)

COP file to address: CSCvb27600, CSCvb27859, CSCva98951, CSCva98954, CSCvb57494 and CSCvb7765

## Locale
                        	 Files

For your convenience, software preloads now include locale files for
                              		  Unified Communications Manager, IM & Presence Server, Cisco Unity
                              		  Connection, and Contact
                                 			 Center Express . Locale files are packaged in DVD images. This allows the
                              		  locale files to be installed directly from local media by the applications.
                              		  Connect the ISO DVD image to your virtual machine using vSphere client prior to
                              		  installing the locale.

## Software Not Included

Entitlement and Requirements

Cisco WebEx Meeting Server

Available with CUWL Pro licensing. Requires separate hardware and virtualization software. See the Cisco WebEx Meeting Server Ordering Guide .

ESD

Cisco Prime Collaboration Assurance

Standard Edition license included with all Unified CM deployments. Business and Advanced Editions require separate licenses.

CSC

Cisco TelePresence Conductor

Available with CUWL Pro / Personal Multiparty licensing

/ ESD

Cisco TelePresence Server

Available with CUWL Pro / Personal Multiparty licensing

/ ESD

| Note | Before using
                                          			 this software, please ensure that you have the latest versions, available
                                          			 either from Cisco Software Center (CSC), or using Cisco
                                             				Electronic Software Delivery (ESD). We provide details on how to use
                                          			 Electronic Software Delivery in an email to you when you order licenses for
                                          			 your chosen applications. Table 2 lists the files that are included and
                                          			 indicates where you can go online to download the files. |
|---|---|

| Application | Version | Install Option | Pre-installation Method |
|---|---|---|---|
| Cisco Unified Communications Manager (UCSInstall_UCOS_12.5.1.10000-22_80_vmv13_v1.0.ova) | 12.5 | 1000 users | Partial (skip) installed application |
| Cisco Unified Communications Manager IM & Presence (UCSInstall_CUP_12.5.1.10000-22_80_vmv13_v1.0.ova) | 12.5 | 1000 users | Partial (skip) installed application |
| Cisco Unity Connection (UCSInstall_CUC_12.5.1.10000-23_160_v1.0.ova) | 12.5 | 1000 users | Partial (skip) installed application |
| Cisco Paging Server (Bootable-CiscoPagingServer_12.5.1.ova) | 12.5 | Standard | Deployed Application OVA |
| Cisco Unified Contact Center Express (UCCX_12_0_100Agent_VM11_OVA.ova) | 12.0 | 100 Agents | Partial (skip) installed application |
| Cisco Prime Collaboration Provisioning (cpc-provisioning-12.6.0.2283-small_v6.5_signed.ova) | 12.6 | Small | Deployed Application OVA |
| Cisco Prime Collaboration Deployment (pcd_vApp_UCOS_12.5.1.10000-18_vmv8_v1.2.ova) | 12.5 |  | Deployed Application OVA |

| Application or File | Filename | Access | Version 11 Solution | Version 12 Solution |
|---|---|---|---|---|
| Virtualization Software |
| - Application image | VMware-ESXi-6.5.0-8294253-Custom-Cisco-6.5.2.1.ova | VMware | — | Yes |
| Cisco Unified Communications Manager & Cisco Unity Connection 1 |
| - Common version 11.5(1) SU3 UCM application image | Bootable_UCSInstall_UCOS_11.5.1.10000-6.sgn.iso | ESD | Yes | — |
| - 12.5 application image | Bootable_UCSInstall_UCOS_12.5.1.10000-22.sgn.iso | ESD | — | Yes |
| - Version 11.5(1) recovery image | 11.5.1.13900-52-recovery.iso | CSC | Yes | — |
| - Version 12.5 recovery image | 12.5.1.10000-22-recovery.iso | CSC | — | Yes |
| - Version 12.5 | UCSInstall_UCOS_12.5.1.10000-22.sgn.iso | CSC | — | Yes |
| - Version 11.5(1) Service Update 3 | UCSInstall_UCOS_11.5.1.13901-3.sgn.iso | CSC | Yes | — |
| - Version 11.5 UCM virtual machine template | cucm_11.5_vmv8_v1.1.ova | CSC | Yes | — |
| - Version 11.5 CUC virtual machine template | CUC_11.5_v1.1.ova | CSC | Yes | — |
| - Version 11.5(1) UCM locale files | UCM-Locales-11.5.1.3000-1.iso | CSC | Yes | — |
| - Version 11.5(1) CUC locale files | UCN-Locales-11.5.0.1-1000-ar-SA-el-GR.iso UCN-Locales-11.5.0.1-1000-en-AU-fr-CA.iso UCN-Locales-11.5.0.1-1000-he-IL-nl-NL.iso UCN-Locales-11.5.0.1-1000-pl-PL-sv-SE.iso UCN-Locales-11.5.0.1-1000-tr-TR-zh-TW.iso UCN-Locales-11.5.0.1-1000-ja-JP.iso | CSC | Yes | — |
| Cisco Unified Communications Manager IM and Presence |
| - Version 11.5(1) SU3 application | UCSInstall_CUP_11.5.1.13900-57.sgn.iso | ESD | Yes | — |
| - Version 11.5(1) SU3 recovery image | 11.5.1.13900-57-recovery.iso | CSC | Yes | — |
| -Version 11.5 virtual machine template | cucm_im_p_11.5_vmv8_v1.4.ova | CSC | Yes | — |
| - Version 12.5 image Bootable | Bootable_UCSInstall_CUP_12.5.1.10000-22.sgn.iso | CSC | — | Yes |
| -Version 12.5 recovery image | 12.5.1.10000-22-recovery.iso | CSC | — | Yes |
| -Version 12.5 IMP locale files | IMP_Locale_12.5.iso | CSC | — | Yes |
| -Version virtual machine template | cucm_im_p_12.5_vmv13_v1.0.ova | CSC | — | Yes |
| Cisco Unified Communications Manager |
| - Version 12.5 UCM virtual machine template | cucm_12.5_vmv13_v1.0.ova | CSC | — | Yes |
| - Version 12.5 UCM locale files | CUCM_12.5.1.10000-22_Locale.iso | CSC | — | Yes |
| Cisco Unity Connection |
| - 12.5 application image | Bootable_UCSInstall_CUC_12.5.1.10000-23.sgn.iso | CSC | — | Yes |
| -Version 12.5 recovery image | 12.5.1.10000-23-recovery.iso | CSC | — | Yes |
| -Version 12.5 | UCSInstall_CUC_12.5.1.10000-23.sgn.iso | CSC | — | Yes |
| -Version 12.5 CUC virtual machine template for 6K | CUC_12.5_v1.0.ova | CSC | — | Yes |
| -Version 12.5 UCM locale files | cuc_locale_12.5.iso | CSC | — | Yes |
| -Version 12.5 UCM locale files | cuc_locale1_12.5.iso | CSC | — | Yes |
| Cisco Emergency Responder |
| - Application image | Bootable_UCSInstall_CER_12.5.1.10000-7.sgn.iso | ESD | — | Yes |
| - Recovery image | 12.5.1.10000-7-recovery.iso | ESD | — | Yes |
| - Virtual machine template | cer_12.5_vmv13_v1.0.ova | CSC | — | Yes |
| - Version 12.5 | UCSInstall_CER_12.5.1.10000-7.sgn.iso | CSC | — | Yes |
| Cisco Unified Contact Center Express |
| - Application image | UCSInstall_UCCX_12_0_1_UCOS_12.0.1.10000-24.sgn.iso | ESD | Yes | — |
| - Virtual machine template | UCCX_12.0_vmv11_v2.6.ova | CSC | Yes | — |
| - Language pack | CCX-Locales-12.0.1.10000-32.iso | CSC | Yes | — |
| Cisco Expressway |
| - Virtual application installer | s42700x12_5_0_v6.5.ova | CSC | — | Yes |
| Cisco TelePresence Management Suite |
| - TMS installer | Cisco_TMS_15.8.0.zip | CSC | — | Yes |
| - TMSXE Installer | Cisco_TMSXE_5.8.zip | CSC | — | Yes |
| - TMSPE Installer | Cisco_TMSPE_1.14.0.zip | CSC | — | Yes |

| Note | Check http://software.cisco.com/ for patches or updates that are released after this document was issued. |
|---|---|

| Application Patches and Updates |
|---|
| Cisco Unified Communications Manager 11.5 (UCM11_COP_Files.iso) |  |
| Cisco Unified Presence 11 (CUP11_COP_Files.iso) |  |
| Cisco Emergency Responder 11.5 (CER11_COP_Files.iso) COP file to address: CSCvb27600, CSCvb27859, CSCva98951, CSCva98954, CSCvb57494 and CSCvb7765 |  |

| Application | Entitlement and Requirements | Access |
|---|---|---|
| Cisco WebEx Meeting Server | Available with CUWL Pro licensing. Requires separate hardware and virtualization software. See the Cisco WebEx Meeting Server Ordering Guide . | ESD |
| Cisco Prime Collaboration Assurance | Standard Edition license included with all Unified CM deployments. Business and Advanced Editions require separate licenses. | CSC |
| Cisco TelePresence Conductor | Available with CUWL Pro / Personal Multiparty licensing | / ESD |
| Cisco TelePresence Server | Available with CUWL Pro / Personal Multiparty licensing | / ESD |