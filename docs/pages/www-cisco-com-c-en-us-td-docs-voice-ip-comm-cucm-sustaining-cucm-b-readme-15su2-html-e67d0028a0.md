---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-sustaining-cucm-b-readme-15su2-html-e67d0028a0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/sustaining/cucm_b_readme-15su2.html
retrieved_at: 2026-08-16T23:51:01.438428+00:00
---

ReadMe for Cisco Unified Communications Manager Release 15SU2

# ReadMe for Cisco Unified Communications Manager Release 15SU2

### Download Options

Updated: October 1, 2024

First Published: October 1, 2024

# Revision History

Date

Revision

October 01, 2024

Initial publication

## Introduction

To view the release notes for previous versions of Cisco Unified Communications Manager, choose the Cisco Unified Communications
                                 Manager version from the following URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_release_notes_list.html

Please review all sections in this document pertaining to installation before you install this version. Failure to install
                                 this version as described may result in inconsistent Cisco Unified Communications Manager behavior.

This 15SU2 ReadMe file contains important information about installation procedures and resolved caveats for Cisco Unified Communications
                     Manager release 15SU2 . This version can be applied to Cisco Unified Communications Manager and Session Management Edition.

Before you install Cisco Unified Communications Manager, Cisco recommends that you review the Important Notes for information about issues that may affect your system.

## System Requirements

The following sections comprise the system requirements for this release.

### Server Support

In this release, you cannot install or run Cisco Unified Communications Manager on server hardware; you must run these applications
                     on virtual machines. Please refer to the “Hardware” section of the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 15 for additional details:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

### Uninterruptible Power Supply

Ensure that you connect each node to an uninterruptible power supply (UPS) to provide backup power and protect your system.

Caution

Failure to connect the Cisco Unified Communication Manager nodes to a UPS may result in damage to physical media and require
                                 a new installation of Cisco Unified CM.

## Version and Description

This SU is a cumulative update that incorporates all of the fixes and changes from Cisco Unified Communications Manager 15 through 15SU1 along with additional changes that are specific to this SU.

You can only install this SU on Cisco Unified Communications Manager Release 12.5(1), 14, 15 through 15SU1 , or any 15 ES from 15.0.1.11001-3 to 15.0.1.12008-1 . Upgrades from any earlier supported versions require a PCD migration. If you are upgrading from a version prior to 14, ensure
                                 you have the proper licensing prior to doing the upgrade.

For a list of all supported upgrade paths and the supported upgrade method, please see the Compatibility Matrix at:

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-device-support-tables-list.html

Caution

Please note that if you install an SU it may contain fixes that are not included in the newer Unified CM releases. For example,
                                 a fix in an 12.5(1)SU, 12.5(1)SU5, may not be included in 14 because the fix was not available prior to the release of 14.
                                 In this example, an SU or ES on the 14 branch may be required to retain the same fixes.

## New to this Release

For details about the features included in this release, refer to Release Notes for Cisco Unified Communications Manager and
                     IM & Presence Service, Release 15 at:

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-release-notes-list.html

## Important Notes

Compatibility between collaboration products is detailed at the following link. You must insure your versions are compatible
                     before beginning your upgrade:

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/CSR-Compatibility-Matrix-InteractiveHTML.html

Cisco provides the following guidance to help you successfully upgrade Cisco Unified Communications Manager software:

To minimize call-processing interruptions during the upgrade process, register all devices to servers that are running the
                           same version of Cisco Unified Communications Manager software. Make sure that you register all devices to the backup Cisco
                           Unified Communications Manager server or to the primary Cisco Unified Communications Manager server, but not to both the backup
                           and primary servers.

### End of Support Firmware Files Removed

Warning

Beginning with CUCM 15, phone firmware that is end of support will no longer be included in the CUCM ISO. These endpoints
                                 will still be allowed to register, unless they have been officially deprecated, but the firmware will not be present in the
                                 TFTP directory following a fresh install. The phones should still register even without the firmware present, but the cmterm-eol_endpoint- 15.0.1.10000-32 .cop.sha512 can be used to install the firmware on the system if needed. See the COP file readme for the list of firmware
                                 that is no longer included by default.

This change only impacts fresh installs and migrations. If you are direct upgrading from a previous version, the firmware
                                 will carry over to the new version.

## Related Documentation

To view documentation that supports Cisco Unified CM Release 15 , go to:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-documentation-roadmaps-list.html

## Before You Begin

Before upgrading, review the Upgrade and Migration Guide > Upgrade Planning for details on:

Supported Upgrade Paths

Upgrade options - There are multiple upgrade options available: Direct Upgrade, Cluster Upgrade, Fresh Install with Data Import,
                           PCD. Detailed instructions for each may be found in the Installation Guide

Hardware, Software, Network, and VM requirements. Open VMWare Tools now default for new installations of version 12.5 and
                           higher, and is recommended for upgrades from earlier versions.

Deprecated Phone Models

Compatibility information can be found in the Compatibility Matrix

## Installation Instructions

Apply this SU to all of your Cisco Unified Communications Manager servers, beginning with the publisher server and TFTP server

Refer to the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 14 for detailed information about doing this upgrade:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

Because the 15.0.1.12900-234 build is a non-bootable ISO, it proves useful only for upgrades. You cannot use it for new installations. You may however
                                 install with the base version 15.0.1.10000-32 and apply 15.0.1.12900-234 as a patch during the installation.

Release 15SU2 is available in both restricted (which is the release type that has always been available from Cisco) and unrestricted versions
                     of software to comply with import / export restrictions to various countries. The unrestricted version is available in limited
                     markets. Please refer to the “Export Restricted and Export Unrestricted Software” section in the Understanding Upgrades and Migrations chapter, of the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 14 referenced above, for a more detailed description.

Once installed, UNRST releases can never be converted or upgraded to releases which support full encryption capabilities

The file names and hash values you will use for this upgrade are:

ISO Name:

MD5:

SHA512:

ISO Name:

MD5:

SHA512:

## Reverting to a Previous Version

Revert to the previous version on all servers in the cluster in the same order in which you performed the upgrade.

Refer to the “Switch to Previous Version” section in the Upgrade Procedures chapter at Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 15 for detailed instructions on “Reverting to a Previous Version.”

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

## Caveats

Caveats describe unexpected behavior on a Cisco Unified Communications server. The following sections contain lists and descriptions
                     of resolved and open caveats in this release.

### Resolved Caveats

Resolved Caveats for Cisco Unified Communications Manager Release 15SU2 describes possible unexpected behaviors in Cisco Unified Communications Manager 15 releases.

Resolved CUCM Caveats in 15SU2 (everything fixed in SU3 since SU2) Click Here for the list

Cumulative Resolved CUCM Caveats (everything fixed in all SU's since base 15) Click Here for the list

### Open Caveats

Open Caveats for Cisco Unified Communications Manager Release 15SU2 describes a few of the possible unexpected behaviors still remaining in Cisco Unified Communications Manager Release 15SU2 .

Open CUCM Caveats in all 15 releases: CSCwi52160: Direct Migration fails from pre-15 to 15 with upgrade history from pre-10.0

### CUCM Caveats 15 Complete List

For a complete list of caveats applicable to 15 , use the following Bug Search Tool link:

https://bst.cloudapps.cisco.com/bugsearch?pf=prdNm&sb=afr&kw=*&bt=custV&prdNam=Cisco%20Unified%20Communications%20Manager%20(CallManager)&rls=15.0(1.1

To determine the caveats that were open for a specific release, use the following steps (the screenshots below are from Excel
                     for Mac, the Excel for Windows options are a little different but follow the same basic flow):

Click on the "Export Results to Excel" link

Open the downloaded file in Excel and Save As a .xlsx file

Open a blank Excel workbook

Click on Data --> Get Data (Power Query)

Choose "Excel workbook" as the source.

Click "Browse", select the .xlsx file saved previously, and click Next

Click the checkbox next to the Tab name (by default it will be Search Results)

Click on the "Transform Data" button

Click on the fx button to insert a new step

In the text box next to the fx button, paste the desired filter string (see below)

Click the check mark to apply the changes

Click the "Close and load" button

The results that are loaded into the Excel workbook will be all of the Open Caveats for that specific release

Security Advisory Caveats: To get a list of caveats that are applicable to Security Advisories or other security related issues, after filtering for
                     a specific release using the examples above, an additional filter for the keyword PSIRT can be applied to the Release Note
                     Enclosure column.

## Firmware Versions

SUs contain firmware loads, however, Cisco recommends that you always download the latest firmware load from the Software
                     Download Center.

### End of Support Firmware Files Removed

Warning

Beginning with CUCM 15, phone firmware that is end of support will no longer be included in the CUCM ISO. These endpoints
                                 will still be allowed to register, unless they have been officially deprecated, but the firmware will not be present in the
                                 TFTP directory following a fresh install. The phones should still register even without the firmware present, but the cmterm-eol_endpoint- 15.0.1.10000-32 .cop.sha512 can be used to install the firmware on the system if needed. See the COP file readme for the list of firmware
                                 that is no longer included by default.

This change only impacts fresh installs and migrations. If you are direct upgrading from a previous version, the firmware
                                 will carry over to the new version.

### Phone Firmware

To download phone firmware, follow this procedure:

Go to https://software.cisco.com/download/home

Click on Browse All

Click on Collaboration Endpoints

Choose the desired Endpoint Type

Choose the desired Endpoint Model

### Device Packages

To download phone firmware, follow this procedure:

Go to https://software.cisco.com/download/home

Click on Browse All

Click on Unified Communications

Click on Call Control

Click on Unified Communications Manager (CallManager)

Choose the desired UCM version

Click on the Device Packages link

### Firmware Versions in this Release

```
Device type                               Load name                       Version
----------------------------------------  ------------------------------  ----------
Device type                               Load name                       Version
----------------------------------------  ------------------------------  ----------
3905                                      3905.9-4-1SR4-2                 9.4(1SR4.2)
6901-sccp                                 6901-sccp.9-3-1-SR3-1           9.3(1.0)  
6901-sip                                  6901-sip.9-3-1-SR3-1            9.3(1.0)  
7832-sip                                  7832-sip.14-3-1-0001-60.k4      14.3.1(0001.60)
78xx                                      78xx.14-3-1-0001-60.k4          14.3.1(0001.60)
8821-sip                                  8821-sip.11-0-6SR5-5.k4         11.0(6SR5.5)
8832-sip                                  8832-sip.14-3-1-0001-60.k4      14.3.1(0001.60)
8845_65-sip                               8845_65-sip.14-3-1-0001-60.k4   14.3.1(0001.60)
88xx-sip                                  88xx-sip.14-3-1-0001-60.k4      14.3.1(0001.60)
ATA191                                    ATA191.12-0-2-0001-011          12.0.2(0001.11)
headset-builtin                           headset-builtin.3-2-0001-1.k4   3.2(0001.1)
PHONEOS-8875                              PHONEOS-8875.2-3-1-0001-26      2.3.1(0001.26)

Plug-in Report
------------------------------------------
cm-jtapi-plugin-15.0.1.12900-5.x86_64.rpm
cm-taps-plugin-7.0.2.0-1.x86_64.rpm
cm-tsp-plugin-15.0.0.7-0.x86_64.rpm
cm-axlsqltoolkit-plugin-1.1.0.0-1.x86_64.rpm
cm-rtmt-client-plugin-15.0.0.0-0.x86_64.rpm

TZDATA file                               Version
----------------------------------------  ----------
platform-tzdata-2024a-1.el8.noarch.rpm    2024-a
```

| Date | Revision |
|---|---|
| October 01, 2024 | Initial publication |

| Note | To view the release notes for previous versions of Cisco Unified Communications Manager, choose the Cisco Unified Communications
                                 Manager version from the following URL: http://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_release_notes_list.html |
|---|---|

| Note | Please review all sections in this document pertaining to installation before you install this version. Failure to install
                                 this version as described may result in inconsistent Cisco Unified Communications Manager behavior. |
|---|---|

| Note | Before you install Cisco Unified Communications Manager, Cisco recommends that you review the Important Notes for information about issues that may affect your system. |
|---|---|

| Caution | Failure to connect the Cisco Unified Communication Manager nodes to a UPS may result in damage to physical media and require
                                 a new installation of Cisco Unified CM. |
|---|---|

| Note | You can only install this SU on Cisco Unified Communications Manager Release 12.5(1), 14, 15 through 15SU1 , or any 15 ES from 15.0.1.11001-3 to 15.0.1.12008-1 . Upgrades from any earlier supported versions require a PCD migration. If you are upgrading from a version prior to 14, ensure
                                 you have the proper licensing prior to doing the upgrade. |
|---|---|

| Caution | Please note that if you install an SU it may contain fixes that are not included in the newer Unified CM releases. For example,
                                 a fix in an 12.5(1)SU, 12.5(1)SU5, may not be included in 14 because the fix was not available prior to the release of 14.
                                 In this example, an SU or ES on the 14 branch may be required to retain the same fixes. |
|---|---|

| Warning | Beginning with CUCM 15, phone firmware that is end of support will no longer be included in the CUCM ISO. These endpoints
                                 will still be allowed to register, unless they have been officially deprecated, but the firmware will not be present in the
                                 TFTP directory following a fresh install. The phones should still register even without the firmware present, but the cmterm-eol_endpoint- 15.0.1.10000-32 .cop.sha512 can be used to install the firmware on the system if needed. See the COP file readme for the list of firmware
                                 that is no longer included by default. This change only impacts fresh installs and migrations. If you are direct upgrading from a previous version, the firmware
                                 will carry over to the new version. |
|---|---|

| Note | Apply this SU to all of your Cisco Unified Communications Manager servers, beginning with the publisher server and TFTP server |
|---|---|

| Note | Because the 15.0.1.12900-234 build is a non-bootable ISO, it proves useful only for upgrades. You cannot use it for new installations. You may however
                                 install with the base version 15.0.1.10000-32 and apply 15.0.1.12900-234 as a patch during the installation. |
|---|---|

| Note | Once installed, UNRST releases can never be converted or upgraded to releases which support full encryption capabilities |
|---|---|

| ISO Name: | UCSInstall_UCOS_15.0.1.12900-234.sha512.iso |
|---|---|
| MD5: | b0879dd991b6db1cf023c7191b0cac6e |
| SHA512: | 191faa31079fbc72e97f791339fab1e7d5a09ba445879bc916527ee136c98e5fd881dfa650f7b4 ab76c95e073d251a1b99be1477117f8cfa517a476c11c65eb5 |

| ISO Name: | UCSInstall_UCOS_UNRST_15.0.1.12900-234.sha512.iso |
|---|---|
| MD5: | e7f0fda4112cad5c0b80f9257d31b686 |
| SHA512: | ee3c9b52d5219527c825ccc3b3af44e90751e7e61f0d258286ec87b29a9b1e62b7c0882907bd 5ca91776d17cccf58c762b27668d4d3f02b905af6a4056f3fe85 |

| Note | Revert to the previous version on all servers in the cluster in the same order in which you performed the upgrade. |
|---|---|

| Warning | Beginning with CUCM 15, phone firmware that is end of support will no longer be included in the CUCM ISO. These endpoints
                                 will still be allowed to register, unless they have been officially deprecated, but the firmware will not be present in the
                                 TFTP directory following a fresh install. The phones should still register even without the firmware present, but the cmterm-eol_endpoint- 15.0.1.10000-32 .cop.sha512 can be used to install the firmware on the system if needed. See the COP file readme for the list of firmware
                                 that is no longer included by default. This change only impacts fresh installs and migrations. If you are direct upgrading from a previous version, the firmware
                                 will carry over to the new version. |
|---|---|