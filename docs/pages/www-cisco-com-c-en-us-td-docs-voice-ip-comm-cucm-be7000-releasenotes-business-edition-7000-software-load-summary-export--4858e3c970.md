---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be7000-releasenotes-business-edition-7000-software-load-summary-export--4858e3c970
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE7000/releasenotes/business-edition-7000-software-load-summary-export-restricted-version-12x14x-k9-14/cucm_m_business-edition-7000-software-load.html
retrieved_at: 2026-08-21T21:40:25.808340+00:00
---

Business Edition 7000 Software Load Summary Export Restricted Version 12X14X-K9-14

# Business Edition 7000 Software Load Summary Export Restricted Version 12X14X-K9-14

Book Contents

- Book Title Page

- Business Edition 7000 Software Load Summary

Find Matches in This Book

## Results

Updated: December 1, 2025

Chapter: Business Edition 7000 Software Load Summary

## Chapter: Business Edition 7000 Software Load Summary

# Business Edition 7000 Software Load Summary

## Introduction to Software Load Summary

The document identifies the software that is preloaded on the appliance's module of this product for your convenience.

We attempt to keep the software versions in this build as up-to-date as possible; however, newer code may have been released
                              after this product was manufactured.

Before using this software, please ensure that you have the latest maintenance updates, available either from Cisco Software Center (CSC), or using Cisco Electronic Software Delivery (ESD). We provide details on how to use Electronic Software Delivery in an email to you when you order licenses for your
                                          chosen applications. Table 1 lists the files that are included and indicates where you can go online to download the files.

## Types of Factory-loaded Software

Business Edition 7000 appliance hardware is loaded with the latest supported BIOS, firmware, and drivers from Cisco’s UCS Hardware and Software Compatibility Tool at the time of factory build. At time of installation, consult this tool to see if any items must be refreshed.

Business Edition 7000 appliances are loaded with a variety of files for virtualization software and application software to
                              assist you with expediting installation and first-time-setup. At the time of install, check myvmware.com, Cisco Software Center,
                              and Cisco Electronic Software Delivery to see if newer maintenance updates are available.

For normal installations, do not erase the factory-loaded software. If you do erase you will lose all the files and any factory-loaded
                              embedded virtualization software license.

Files need to be manually re-downloaded from myvmware.com and cisco.com, and any embedded virtualization licenses to be applied
                                    manually.

If the factory-loaded software is erased (example due to hardware replacement/migration, disks reformat, RAID rebuild, virtualization
                                    software reinstall, or upgrade, so on), see the Business Edition 7000 12.5 Installation Guide for appliance rebuild instructions.

See below for a summary of factory-loaded file types for virtualization software and applications. Table 1 contains a detailed
                              list of what specific files are factory-loaded. These files are stored in the virtualization software’s datastore.

Cisco custom image for VMware vSphere ESXi Install CD : The installation media from vmware.com for the indicated version used to factory-install ESXi. Factory-install will also
                                    be factory-licensed if you ordered the appliance with an embedded virtualization license. If you overwrite this factory install
                                    with your reinstall or upgrade, the embedded virtualization license will be erased and must be manually re-applied.

Deployed OVA containing preinstalled application : Open Virtual Archive file containing a fully installed, ready-to-run application. Deploy to the appliance, then power on
                                    to enter application first-time-setup.

Partial (skip) installed OVA: Open Virtual Archive file containing an application that is installed up to the “skip” configuration point, where the application
                                    is ready to accept the configuration and complete installation. Deploy to the appliance, then power on to complete application
                                    install and enter first-time-setup through either the system wizard through the virtual machine console or through unattended/touchless
                                    install with a platformConfig.xml configuration file. Refer to the Business Edition 7000 12.5  Installation Guide for further information.

Base OVA : Open Virtual Archive file containing “empty” virtual machine (VM) configurations using specs and settings that are supported
                                    by the applications.

Bootable installer image for base release : ISO application installer for indicated base release (example 12.5 base release) that must be used along with an “empty”
                                    virtual machine that is deployed from the Base OVA.

Non-bootable upgrade-only image for Service Update : ISO application file that applies maintenance updates (example SU2) on top of an existing install of a base release (example
                                    applying SU2 on top of 12.5 base release). Follow application upgrade guides for how to use these files.

Cisco Options Pack (COP) : various patches and updates, such as Locale files, that are distributed in ISO installer format. Follow application install/upgrade
                                    guides for how to use these files.

Recovery software image: ISO file used with Cisco TAC when an application virtual machine has suffered data corruption or is unable to start.

## Preloaded Virtualization and Application Software - Business Edition 7000

The hypervisor datastore on the appliance includes installation files for Collaboration System Release 12 Unified Communications (UC) applications. These applications include Cisco Unified Communications Manager, Cisco Unity Connection,
                              and Cisco Unified Communications Manager Instant Messaging and Presence Server. You may install any of the other preloaded
                              applications with either of these UC releases. For release sets of compatible application versions, see Cisco Collaboration
                              Systems Release documents at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/tsd-products-support-series-home.html .

The following table details the files included in the datastore and indicates which to use for a version 12.x Unified Communications solution.

Application or File

Filename for appliances with Cisco Product ID's:

BE7M-M5-K9

BE7H-M5-K9

Access

Virtualization Software

VMware vSphere ESXi 7.0 GA

CISCO Custom Image for ESXi 7.0 GA Install CD

VMware_ESXi_7.0.0_15843807_Custom_Cisco_4.1.1a.iso

VMware

Cisco Business Edition Embedded Virtualization License

If ordered with option BE6K-VIRT-LIC-NONE

No license is factory-loaded; sold separately / customer must provide. ESXi 7.0 will enter "evaluation mode" until a license
                                          is provided (see vmware.com for details)

Cisco License Central

If ordered with option BE6/7K-VIRTBASP-7X

License for Cisco Business Edition Embedded Virt. Basic Plus 7x is factory-loaded. See Cisco Business Edition 7000 Installation
                                          Guide for details.

Cisco License Central

If ordered with option BE6/7K-VIRTENH-7X

License for Cisco Business Edition Embedded Virt. Enhanced 7x is factory-loaded. See Cisco Business Edition 7000 Installation
                                          Guide for details.

Cisco License Central

Calling, Messaging & Edge Applications

Cisco Unified Communications Manager 12.5(1) SU2

Partial (skip) installed application OVA (7500 user VM configuration)

UCSInstall_UCOS_12.5.1.10000-22_110_vmv13_v1.0.ova

Factory preload only

Preloaded bootable application installer image for base release

Bootable_UCSInstall_UCOS_12.5.1.10000-22.sgn.iso

Cisco License Central

Preloaded non-bootable application upgrade-only image for Service Update (SU)

UCSInstall_UCOS_12.5.1.12900-115.sgn.iso

Software Download

Locale files

CUCM_12.5.1.10000-22_Locale.iso

Software Download

Preloaded recovery software image

12.5.1.10000-22-recovery.iso

Software Download

Preloaded base OVA for Virtual Machine configurations

cucm_12.5_vmv13_v1.0.ova

Software Download

Cisco Unified Communications Manager - IM &Presence Service 12.5(1) SU2

Partial (skip) installed application OVA (5000 user VM configuration)

UCSInstall_CUP_12.5.1.10000-22_80d_vmv13_v1.0.ova

Factory preloaded only

Preloaded bootable application installer image for base release

Bootable_UCSInstall_CUP_12.5.1.10000-22.sgn.iso

Cisco License Central

Preloaded non-bootable application upgrade-only image for Service Update (SU)

UCSInstall_CUP_12.5.1.12900-25.sgn.iso

Locale files

IMP_Locale_12.5.iso

Preloaded recovery software image

12.5.1.10000-22-recovery.iso

Software Download

Preloaded base OVA for Virtual Machine configurations

cucm_im_p_12.5_vmv13_v1.0.ova

Software Download

Cisco Unity Connection 12.5(1) SU2

Partial (skip) installed application OVA (5000 user VM configuration)

UCSInstall_CUC_12.5.1.10000-23_200_v1.0.ova

Factory preload only

Preloaded bootable application installer image for base release

Bootable_UCSInstall_CUC_12.5.1.10000-23.sgn.iso

Cisco License Central

Preloaded non-bootable application upgrade-only image for Service Update (SU)

UCSInstall_CUC_12.5.1.12900-56.sgn.iso

Software Download

Locale files

cuc_locale_12.5.iso

cuc_locale1_12.5.iso

Software Download

Preloaded recovery software image

12.5.1.10000-23-recovery.iso

Software Download

Preloaded base OVA for Virtual Machine configurations

CUC_12.5_v1.0.ova

Software Download

Cisco Emergency Responder 12.5(1) SU2

Preloaded bootable application installer image for base release

Bootable_UCSInstall_CER_12.5.1.10000-7.sgn.iso

Cisco License Central

Preloaded non-bootable application upgrade-only image for Service Update (SU)

UCSInstall_CER_12.5.1.21900-35.sgn.iso

Software Download

Preloaded recovery software image

12.5.1.10000-7-recovery.iso

Cisco License Central

Preloaded base OVA for Virtual Machine configurations

cer_12.5_vmv13_v1.0.ova

Software Download

Cisco Expressway X12.6.2

Deployed OVA containing preinstalled application (Medium VM configuration)

s42700x12_6_2.ova

s42700x12_7_1_v6.5.ova

s42700x14_0_0_v6.5.ova

Software Download

Cisco Paging Server 12.5.1

Deployed OVA containing preinstalled application (Standard VM configuration)

Bootable-CiscoPagingServer_12.5.1.ova

Software Download

Meetings Applications

Cisco TelePresence Management Suite

Preloaded TMS installer

Not preloaded at this time

Cisco License Central

Preloaded TMSXE installer

Not preloaded at this time

Cisco License Central

Preloaded TMSPE installer

Not preloaded at this time

Cisco License Central

Contact Center Applications

Cisco Unified Contact Center Express 12.5

Partial (skip) installed application OVA (400 agent VM configuration)

Not preloaded at this time

Cisco License Central

Preloaded bootable application installer image for base release

UCSInstall_UCCX_12_5_1_UCOS_12.5.1.10000-31.sgn.iso

Cisco License Central

Language pack

uccx-language-pack_26-12.5.1.10000-22.cop

Software Download

Preloaded base OVA for Virtual Machine configurations

UCCX_12.5_vmv13_v2.7.ova

Software Download

Management Applications

Cisco Prime Collaboration Provisioning 12.6 SU2

Deployed OVA containing preinstalled application (Medium VM configuration)

cpc-provisioning-12.6.0.3039-medium.ova_v6.5_signed

Cisco License Central

Cisco Prime Collaboration Deployment 12.6(1)

Deployed OVA containing preinstalled application (Default VM configuration)

pcd_vApp_UCOS_12.6.1.10000-21_vmv8_v1.2.ova

Cisco License Central

| Note | Before using this software, please ensure that you have the latest maintenance updates, available either from Cisco Software Center (CSC), or using Cisco Electronic Software Delivery (ESD). We provide details on how to use Electronic Software Delivery in an email to you when you order licenses for your
                                          chosen applications. Table 1 lists the files that are included and indicates where you can go online to download the files. |
|---|---|

| Application or File | Filename for appliances with Cisco Product ID's: BE7M-M5-K9 BE7H-M5-K9 | Access |
|---|---|---|
| Virtualization Software |
| VMware vSphere ESXi 7.0 GA |
| CISCO Custom Image for ESXi 7.0 GA Install CD | VMware_ESXi_7.0.0_15843807_Custom_Cisco_4.1.1a.iso | VMware |
| Cisco Business Edition Embedded Virtualization License |
| If ordered with option BE6K-VIRT-LIC-NONE | No license is factory-loaded; sold separately / customer must provide. ESXi 7.0 will enter "evaluation mode" until a license
                                          is provided (see vmware.com for details) | Cisco License Central |
| If ordered with option BE6/7K-VIRTBASP-7X | License for Cisco Business Edition Embedded Virt. Basic Plus 7x is factory-loaded. See Cisco Business Edition 7000 Installation
                                          Guide for details. | Cisco License Central |
| If ordered with option BE6/7K-VIRTENH-7X | License for Cisco Business Edition Embedded Virt. Enhanced 7x is factory-loaded. See Cisco Business Edition 7000 Installation
                                          Guide for details. | Cisco License Central |
| Calling, Messaging & Edge Applications |
| Cisco Unified Communications Manager 12.5(1) SU2 |
| Partial (skip) installed application OVA (7500 user VM configuration) | UCSInstall_UCOS_12.5.1.10000-22_110_vmv13_v1.0.ova | Factory preload only |
| Preloaded bootable application installer image for base release | Bootable_UCSInstall_UCOS_12.5.1.10000-22.sgn.iso | Cisco License Central |
| Preloaded non-bootable application upgrade-only image for Service Update (SU) | UCSInstall_UCOS_12.5.1.12900-115.sgn.iso | Software Download |
| Locale files | CUCM_12.5.1.10000-22_Locale.iso | Software Download |
| Preloaded recovery software image | 12.5.1.10000-22-recovery.iso | Software Download |
| Preloaded base OVA for Virtual Machine configurations | cucm_12.5_vmv13_v1.0.ova | Software Download |
| Cisco Unified Communications Manager - IM &Presence Service 12.5(1) SU2 |
| Partial (skip) installed application OVA (5000 user VM configuration) | UCSInstall_CUP_12.5.1.10000-22_80d_vmv13_v1.0.ova | Factory preloaded only |
| Preloaded bootable application installer image for base release | Bootable_UCSInstall_CUP_12.5.1.10000-22.sgn.iso | Cisco License Central |
| Preloaded non-bootable application upgrade-only image for Service Update (SU) | UCSInstall_CUP_12.5.1.12900-25.sgn.iso | Software Download |
| Locale files | IMP_Locale_12.5.iso | Software Download |
| Preloaded recovery software image | 12.5.1.10000-22-recovery.iso | Software Download |
| Preloaded base OVA for Virtual Machine configurations | cucm_im_p_12.5_vmv13_v1.0.ova | Software Download |
| Cisco Unity Connection 12.5(1) SU2 |
| Partial (skip) installed application OVA (5000 user VM configuration) | UCSInstall_CUC_12.5.1.10000-23_200_v1.0.ova | Factory preload only |
| Preloaded bootable application installer image for base release | Bootable_UCSInstall_CUC_12.5.1.10000-23.sgn.iso | Cisco License Central |
| Preloaded non-bootable application upgrade-only image for Service Update (SU) | UCSInstall_CUC_12.5.1.12900-56.sgn.iso | Software Download |
| Locale files | cuc_locale_12.5.iso cuc_locale1_12.5.iso | Software Download |
| Preloaded recovery software image | 12.5.1.10000-23-recovery.iso | Software Download |
| Preloaded base OVA for Virtual Machine configurations | CUC_12.5_v1.0.ova | Software Download |
| Cisco Emergency Responder 12.5(1) SU2 |
| Preloaded bootable application installer image for base release | Bootable_UCSInstall_CER_12.5.1.10000-7.sgn.iso | Cisco License Central |
| Preloaded non-bootable application upgrade-only image for Service Update (SU) | UCSInstall_CER_12.5.1.21900-35.sgn.iso | Software Download |
| Preloaded recovery software image | 12.5.1.10000-7-recovery.iso | Cisco License Central |
| Preloaded base OVA for Virtual Machine configurations | cer_12.5_vmv13_v1.0.ova | Software Download |
| Cisco Expressway X12.6.2 |
| Deployed OVA containing preinstalled application (Medium VM configuration) | s42700x12_6_2.ova s42700x12_7_1_v6.5.ova s42700x14_0_0_v6.5.ova | Software Download |
| Cisco Paging Server 12.5.1 |
| Deployed OVA containing preinstalled application (Standard VM configuration) | Bootable-CiscoPagingServer_12.5.1.ova | Software Download |
| Meetings Applications |
| Cisco TelePresence Management Suite |
| Preloaded TMS installer | Not preloaded at this time | Cisco License Central |
| Preloaded TMSXE installer | Not preloaded at this time | Cisco License Central |
| Preloaded TMSPE installer | Not preloaded at this time | Cisco License Central |
| Contact Center Applications |
| Cisco Unified Contact Center Express 12.5 |
| Partial (skip) installed application OVA (400 agent VM configuration) | Not preloaded at this time | Cisco License Central |
| Preloaded bootable application installer image for base release | UCSInstall_UCCX_12_5_1_UCOS_12.5.1.10000-31.sgn.iso | Cisco License Central |
| Language pack | uccx-language-pack_26-12.5.1.10000-22.cop | Software Download |
| Preloaded base OVA for Virtual Machine configurations | UCCX_12.5_vmv13_v2.7.ova | Software Download |
| Management Applications |
| Cisco Prime Collaboration Provisioning 12.6 SU2 |
| Deployed OVA containing preinstalled application (Medium VM configuration) | cpc-provisioning-12.6.0.3039-medium.ova_v6.5_signed | Cisco License Central |
| Cisco Prime Collaboration Deployment 12.6(1) |
| Deployed OVA containing preinstalled application (Default VM configuration) | pcd_vApp_UCOS_12.6.1.10000-21_vmv8_v1.2.ova | Cisco License Central |