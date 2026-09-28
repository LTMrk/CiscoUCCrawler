---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-be6000-releasenotes-15-business-edition-6000-software-load-summary-expo-fc163ecb35
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/BE6000/releasenotes/15/business-edition-6000-software-load-summary-export-restricted-version-14x15x-k9-16-and-unrestricted-version-14x15x-xu-16/cucm_m_business-edition-6000-software-load-version-14x15x-k9-16-and-unrestricted-version-14x15x-xu-16.html
retrieved_at: 2026-08-21T21:39:14.564565+00:00
---

Business Edition 6000 and 7000 Software Load Summary (Export Restricted 14X15X-K9-16 and Export Unrestricted 14X15X-XU-16)

# Business Edition 6000 and 7000 Software Load Summary (Export Restricted 14X15X-K9-16 and Export Unrestricted 14X15X-XU-16)

Book Contents

- Book Title Page

- Business Edition 6000 and 7000 Software Load Summary

Find Matches in This Book

## Results

Updated: December 1, 2025

Chapter: Business Edition 6000 and 7000 Software Load Summary

## Chapter: Business Edition 6000 and 7000 Software Load Summary

# Business Edition 6000 and 7000 Software Load Summary

## Introduction to Software Load Summary

The document identifies the software that is preloaded on the appliance model of this product for your convenience.

We attempt to keep the software versions in this build as up-to-date as possible; however, newer code may have been released
                              after this product was manufactured.

Before using this software, please ensure that you have the latest maintenance updates, available either from Cisco Software Center (CSC), or using Cisco Electronic Software Delivery (ESD). We provide details on how to use Electronic Software Delivery in an email to you when you order licenses for your
                                          chosen applications. Table 1 lists the files that are included and indicates where you can go online to download the files.

## New and Changed Information

The following table provides an overview of the significant changes to the features in this guide up to this current release.
                              The table does not provide an exhaustive list of all changes made to the guide or of the new features up to this release.

Feature or Change

Description

See

Date

Initial Release of Document for Preloads Version 14X15X-K9/XU-16 on M6 Appliances

Preload application files for CSR 14 and 15 versions (drop all files for version12.x)

Revised preload file list (drop all skip-install-OVAs [now in UC media kits], drop all locales)

Preloaded ESXi version to 7.0 U3i (ships unlicensed, license required but is sold separately or customer-provided)

BE6000M, BE7000M, BE7000H (M6) appliance hardware

—

April 15, 2024

## Types of Factory—loaded Software

Business Edition 6000/7000 appliance hardware is loaded with the latest supported BIOS, firmware, and drivers from Cisco’s UCS Hardware and Software Compatibility Tool at the time of factory build. At time of installation, consult this tool to see if any items must be refreshed.

Business Edition 6000/7000 appliances are loaded with a variety of files for virtualization software and application software
                              to assist you with expediting installation and first-time-setup. At the time of install, check myvmware.com, Cisco Software
                              Center, and Cisco Electronic Software Delivery to see if newer maintenance updates are available.

For normal installations, do not erase the factory-loaded software. If you do erase you will lose all the files and any factory-loaded
                              embedded virtualization software license.

Files need to be manually re-downloaded from myvmware.com and cisco.com, and any embedded virtualization licenses to be applied
                                    manually.

If the factory-loaded software is erased (example due to hardware replacement/migration, disks reformat, RAID rebuild, virtualization
                                    software reinstall, or upgrade, so on), see the Business Edition 6000/7000 or 14 or 15 Installation Guide for appliance rebuild instructions.

See below for a summary of factory-loaded file types for virtualization software and applications. Table 1 contains a detailed
                              list of what specific files are factory-loaded. These files are stored in the virtualization software’s datastore.

Cisco custom image for VMware vSphere ESXi Install CD : The installation media from vmware.com for the indicated version used to factory-install ESXi. Factory-loaded ESXi is unlicensed,
                                    entitlement sold separately or customer-provided.

Base OVA : Open Virtual Archive file containing “empty” virtual machine (VM) configurations using specs and settings that are supported
                                    by the applications.

Bootable installer image for base release : ISO application installer for indicated base release (example 12.5 base release) that must be used along with an “empty”
                                    virtual machine that is deployed from the Base OVA.

Non-bootable upgrade-only image for Service Update : ISO application file that applies maintenance updates (example SU2) on top of an existing install of a base release (example
                                    applying SU2 on top of 12.5 base release). Follow application upgrade guides for how to use these files.

Recovery software image: ISO file used with Cisco TAC when an application virtual machine has suffered data corruption or is unable to start.

## Preloaded Virtualization and Application Software - Business Edition 6000 and 7000

The hypervisor datastore on the appliance includes installation files for Collaboration System Release 14 and 15 Unified Communications (UC) applications. These applications include Cisco Unified Communications Manager, Cisco Unity Connection,
                              and Cisco Unified Communications Manager Instant Messaging and Presence Server. You may install any of the other preloaded
                              applications with either of these UC releases. For release sets of compatible application versions, see Cisco Collaboration
                              Systems Release documents at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-system/tsd-products-support-series-home.html

The following table details the files included in the datastore and indicates which to use for a version 14 or 15 Unified Communications solution.

Application or File

Filename for appliances with Cisco Product ID's:

BE6K-M6-K9 / BE6K-M6-XU

BE7M-M6-K9 / BE7M-M6-XU

BE7H-M6-K9 / BE7H-M6-XU

Access

Virtualization Software

VMware vSphere ESXi 7.0 U3i

CISCO Custom Image for ESXi 7.0 U1 Install CD

VMware-ESXi-7.0.3i-20842708-Custom-Cisco-4.2.2-a.iso

VMware

Virtualization License

License sold separately or customer-provided.

A license for VMware vSphere ESXi is required to operate, but is not included with, shipped with or factory-loaded on M6 appliances.

N/A

Calling, Messaging & Edge Applications

Cisco Unified Communications Manager 14 and 15

Preloaded bootable application installer image for base release

Export Restricted:

Bootable_UCSInstall_UCOS_14.0.1.10000-20.sha512.iso

Bootable_UCSInstall_UCOS_15.0.1.10000-32.sha512.iso

Export Unrestricted:

Bootable_UCSInstall_UCOS_UNRST_14.0.1.10000-20.sha512.iso

Bootable_UCSInstall_UCOS_UNRST_15.0.1.10000-32.sha512.iso

Cisco License Central

Preloaded non-bootable application upgrade-only image for Service Update (SU)

Export Restricted:

UCSInstall_UCOS_14.0.1.10000-20.sha512.iso

UCSInstall_UCOS_15.0.1.10000-32.sha512.iso

Export Unrestricted:

UCSInstall_UCOS_UNRST_14.0.1.10000-20.sha512.iso

UCSInstall_UCOS_UNRST_15.0.1.10000-32.sha512.iso

Software Download

Preloaded recovery software image

14.0.1.10000-20-recovery.iso

15.0.1.10000-32-recovery.iso

Software Download

Preloaded base OVA for Virtual Machine configurations

cucm_14.0_vmv13_v1.1.ova

cucm_15.0_vmv17_v1.1.sha512.ova

Software Download

Cisco Unified Communications Manager - IM &Presence Service 14 and 15

Preloaded bootable application installer image for base release

Export Restricted:

Bootable_UCSInstall_CUP_14.0.1.10000-16.sha512.iso

Bootable_UCSInstall_CUP_15.0.1.10000-10.sha512.iso

Export Unrestricted:

Bootable_UCSInstall_CUP_UNRST_14.0.1.10000-16.sha512.iso

Bootable_UCSInstall_CUP_UNRST_15.0.1.10000-10.sha512.iso

Cisco License Central

Preloaded non-bootable application upgrade-only image for Service Update (SU)

Export Restricted:

UCSInstall_CUP_14.0.1.10000-16.sha512.iso

UCSInstall_CUP_15.0.1.10000-10.sha512.iso

Export Unrestricted:

UCSInstall_CUP_UNRST_14.0.1.10000-16.sha512.iso

UCSInstall_CUP_UNRST_15.0.1.10000-10.sha512.iso

Preloaded recovery software image

14.0.1.10000-16-recovery.iso

15.0.1.10000-10-recovery.iso

Software Download

Preloaded base OVA for Virtual Machine configurations

cucm_im_p_14.0_vmv13_v1.0.ova

cucm_im_p_15.0_vmv17_v1.0.sha512.ova

Software Download

Cisco Unity Connection 14 and 15

Preloaded bootable application installer image for base release

Export Restricted:

Bootable_UCSInstall_CUC_14.0.1.10000-19.sha512.iso

Bootable_UCSInstall_CUC_15.0.1.10000-24.sha512.iso

Export Unrestricted:

Bootable_UCSInstall_CUC_UNRST_14.0.1.10000-19.sha512.iso

Bootable_UCSInstall_CUC_UNRST_15.0.1.10000-24.sha512.iso

Cisco License Central

Preloaded non-bootable application upgrade-only image for Service Update (SU)

Export Restricted:

UCSInstall_CUC_14.0.1.10000-19.sha512.iso

UCSInstall_CUC_15.0.1.10000-24.sha512.iso

Export Unrestricted:

UCSInstall_CUC_UNRST_14.0.1.10000-19.sha512.iso

UCSInstall_CUC_UNRST_15.0.1.10000-24.sha512.iso

Software Download

Preloaded recovery software image

14.0.1.10000-19-recovery.iso

15.0.1.10000-24-recovery.iso

Software Download

Preloaded base OVA for Virtual Machine configurations

CUC_14.0_v1.1.ova

CUC_15.0_v1.1.sha512.ova

Software Download

Cisco Emergency Responder 14 and 15

Preloaded bootable application installer image for base release

Bootable_UCSInstall_CER_14.0.1.10000-7.sha512.iso

Bootable_UCSInstall_CER_15.0.1.10000-34.sha512.iso

Cisco License Central

Preloaded non-bootable application upgrade-only image for Service Update (SU)

UCSInstall_CER_14.0.1.10000-7.sha512.iso

UCSInstall_CER_15.0.1.10000-34.sha512.iso

Software Download

Preloaded recovery software image

14.0.1.10000-7-recovery.iso

15.0.1.10000-34-recovery.iso

Cisco License Central

Preloaded base OVA for Virtual Machine configurations

cer_14.0_vmv13_v1.0.ova

cer_15.0_vmv17_v1.0.sha512.ova

Software Download

Cisco Expressway X14 and X15

Deployed OVA containing preinstalled application (Small VM configuration)

s42700x14_0_0_v6.5.ova

s42700x15_0_0.ova

Software Download

Cisco Paging Server 14.4.2

Deployed OVA containing preinstalled application (Standard VM configuration)

Bootable-CiscoPagingServer_14.4.2.ova

Software Download

Contact Center Applications

Cisco Unified Contact Center Express 12.5

Preloaded bootable application installer image for base release

UCSInstall_UCCX_12_5_1_UCOS_12.5.1.10000-31.sgn.iso

Cisco License Central

Preloaded base OVA for Virtual Machine configurations

UCCX_12.5_vmv13_v2.7.ova

Software Download

Management Applications

Cisco Prime Collaboration Deployment 15

Deployed OVA containing preinstalled application (Default VM configuration)

pcd_vApp_UCOS_15.0.1.10000-10_vmv17_v1.2.sha512.ova

Cisco License Central

| Note | Before using this software, please ensure that you have the latest maintenance updates, available either from Cisco Software Center (CSC), or using Cisco Electronic Software Delivery (ESD). We provide details on how to use Electronic Software Delivery in an email to you when you order licenses for your
                                          chosen applications. Table 1 lists the files that are included and indicates where you can go online to download the files. |
|---|---|

| Feature or Change | Description | See | Date |
|---|---|---|---|
| Initial Release of Document for Preloads Version 14X15X-K9/XU-16 on M6 Appliances | Preload application files for CSR 14 and 15 versions (drop all files for version12.x) Revised preload file list (drop all skip-install-OVAs [now in UC media kits], drop all locales) Preloaded ESXi version to 7.0 U3i (ships unlicensed, license required but is sold separately or customer-provided) BE6000M, BE7000M, BE7000H (M6) appliance hardware | — | April 15, 2024 |

| Application or File | Filename for appliances with Cisco Product ID's: BE6K-M6-K9 / BE6K-M6-XU BE7M-M6-K9 / BE7M-M6-XU BE7H-M6-K9 / BE7H-M6-XU | Access |
|---|---|---|
| Virtualization Software |
| VMware vSphere ESXi 7.0 U3i |
| CISCO Custom Image for ESXi 7.0 U1 Install CD | VMware-ESXi-7.0.3i-20842708-Custom-Cisco-4.2.2-a.iso | VMware |
| Virtualization License |
| License sold separately or customer-provided. | A license for VMware vSphere ESXi is required to operate, but is not included with, shipped with or factory-loaded on M6 appliances. | N/A |
| Calling, Messaging & Edge Applications |
| Cisco Unified Communications Manager 14 and 15 |
| Preloaded bootable application installer image for base release | Export Restricted: Bootable_UCSInstall_UCOS_14.0.1.10000-20.sha512.iso Bootable_UCSInstall_UCOS_15.0.1.10000-32.sha512.iso Export Unrestricted: Bootable_UCSInstall_UCOS_UNRST_14.0.1.10000-20.sha512.iso Bootable_UCSInstall_UCOS_UNRST_15.0.1.10000-32.sha512.iso | Cisco License Central |
| Preloaded non-bootable application upgrade-only image for Service Update (SU) | Export Restricted: UCSInstall_UCOS_14.0.1.10000-20.sha512.iso UCSInstall_UCOS_15.0.1.10000-32.sha512.iso Export Unrestricted: UCSInstall_UCOS_UNRST_14.0.1.10000-20.sha512.iso UCSInstall_UCOS_UNRST_15.0.1.10000-32.sha512.iso | Software Download |
| Preloaded recovery software image | 14.0.1.10000-20-recovery.iso 15.0.1.10000-32-recovery.iso | Software Download |
| Preloaded base OVA for Virtual Machine configurations | cucm_14.0_vmv13_v1.1.ova cucm_15.0_vmv17_v1.1.sha512.ova | Software Download |
| Cisco Unified Communications Manager - IM &Presence Service 14 and 15 |
| Preloaded bootable application installer image for base release | Export Restricted: Bootable_UCSInstall_CUP_14.0.1.10000-16.sha512.iso Bootable_UCSInstall_CUP_15.0.1.10000-10.sha512.iso Export Unrestricted: Bootable_UCSInstall_CUP_UNRST_14.0.1.10000-16.sha512.iso Bootable_UCSInstall_CUP_UNRST_15.0.1.10000-10.sha512.iso | Cisco License Central |
| Preloaded non-bootable application upgrade-only image for Service Update (SU) | Export Restricted: UCSInstall_CUP_14.0.1.10000-16.sha512.iso UCSInstall_CUP_15.0.1.10000-10.sha512.iso Export Unrestricted: UCSInstall_CUP_UNRST_14.0.1.10000-16.sha512.iso UCSInstall_CUP_UNRST_15.0.1.10000-10.sha512.iso | Software Download |
| Preloaded recovery software image | 14.0.1.10000-16-recovery.iso 15.0.1.10000-10-recovery.iso | Software Download |
| Preloaded base OVA for Virtual Machine configurations | cucm_im_p_14.0_vmv13_v1.0.ova cucm_im_p_15.0_vmv17_v1.0.sha512.ova | Software Download |
| Cisco Unity Connection 14 and 15 |
| Preloaded bootable application installer image for base release | Export Restricted: Bootable_UCSInstall_CUC_14.0.1.10000-19.sha512.iso Bootable_UCSInstall_CUC_15.0.1.10000-24.sha512.iso Export Unrestricted: Bootable_UCSInstall_CUC_UNRST_14.0.1.10000-19.sha512.iso Bootable_UCSInstall_CUC_UNRST_15.0.1.10000-24.sha512.iso | Cisco License Central |
| Preloaded non-bootable application upgrade-only image for Service Update (SU) | Export Restricted: UCSInstall_CUC_14.0.1.10000-19.sha512.iso UCSInstall_CUC_15.0.1.10000-24.sha512.iso Export Unrestricted: UCSInstall_CUC_UNRST_14.0.1.10000-19.sha512.iso UCSInstall_CUC_UNRST_15.0.1.10000-24.sha512.iso | Software Download |
| Preloaded recovery software image | 14.0.1.10000-19-recovery.iso 15.0.1.10000-24-recovery.iso | Software Download |
| Preloaded base OVA for Virtual Machine configurations | CUC_14.0_v1.1.ova CUC_15.0_v1.1.sha512.ova | Software Download |
| Cisco Emergency Responder 14 and 15 |
| Preloaded bootable application installer image for base release | Bootable_UCSInstall_CER_14.0.1.10000-7.sha512.iso Bootable_UCSInstall_CER_15.0.1.10000-34.sha512.iso | Cisco License Central |
| Preloaded non-bootable application upgrade-only image for Service Update (SU) | UCSInstall_CER_14.0.1.10000-7.sha512.iso UCSInstall_CER_15.0.1.10000-34.sha512.iso | Software Download |
| Preloaded recovery software image | 14.0.1.10000-7-recovery.iso 15.0.1.10000-34-recovery.iso | Cisco License Central |
| Preloaded base OVA for Virtual Machine configurations | cer_14.0_vmv13_v1.0.ova cer_15.0_vmv17_v1.0.sha512.ova | Software Download |
| Cisco Expressway X14 and X15 |
| Deployed OVA containing preinstalled application (Small VM configuration) | s42700x14_0_0_v6.5.ova s42700x15_0_0.ova | Software Download |
| Cisco Paging Server 14.4.2 |
| Deployed OVA containing preinstalled application (Standard VM configuration) | Bootable-CiscoPagingServer_14.4.2.ova | Software Download |
| Contact Center Applications |
| Cisco Unified Contact Center Express 12.5 |
| Preloaded bootable application installer image for base release | UCSInstall_UCCX_12_5_1_UCOS_12.5.1.10000-31.sgn.iso | Cisco License Central |
| Preloaded base OVA for Virtual Machine configurations | UCCX_12.5_vmv13_v2.7.ova | Software Download |
| Management Applications |
| Cisco Prime Collaboration Deployment 15 |
| Deployed OVA containing preinstalled application (Default VM configuration) | pcd_vApp_UCOS_15.0.1.10000-10_vmv17_v1.2.sha512.ova | Cisco License Central |