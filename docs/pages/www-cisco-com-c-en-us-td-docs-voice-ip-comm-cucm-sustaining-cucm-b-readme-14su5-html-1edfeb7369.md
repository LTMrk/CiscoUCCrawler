---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-sustaining-cucm-b-readme-14su5-html-1edfeb7369
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/sustaining/cucm_b_readme-14su5.html
retrieved_at: 2026-08-16T23:41:15.562795+00:00
---

ReadMe for Cisco Unified Communications Manager Release 14SU5

# ReadMe for Cisco Unified Communications Manager Release 14SU5

### Download Options

Updated: October 14, 2025

First Published: October 14, 2025

# Revision History

Date

Revision

October 14, 2025

Initial publication

## Introduction

To view the release notes for previous versions of Cisco Unified Communications Manager, choose the Cisco Unified Communications
                                 Manager version from the following URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_release_notes_list.html

Please review all sections in this document pertaining to installation before you install this version. Failure to install
                                 this version as described may result in inconsistent Cisco Unified Communications Manager behavior.

This 14SU5 ReadMe file contains important information about installation procedures and resolved caveats for Cisco Unified Communications
                     Manager release 14SU5 . This version can be applied to Cisco Unified Communications Manager and Session Management Edition.

Before you install Cisco Unified Communications Manager, Cisco recommends that you review the Important Notes for information about issues that may affect your system.

## System Requirements

The following sections comprise the system requirements for this release.

### Server Support

In this release, you cannot install or run Cisco Unified Communications Manager on server hardware; you must run these applications
                     on virtual machines. Please refer to the “Hardware” section of the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 14 for additional details:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

### Uninterruptible Power Supply

Ensure that you connect each node to an uninterruptible power supply (UPS) to provide backup power and protect your system.

Caution

Failure to connect the Cisco Unified Communication Manager nodes to a UPS may result in damage to physical media and require
                                 a new installation of Cisco Unified CM.

## Version and Description

This SU is a cumulative update that incorporates all of the fixes and changes from Cisco Unified Communications Manager 14 through 14SU4a along with additional changes that are specific to this SU.

You can only install this SU on Cisco Unified Communications Manager Release 10.5 through 11.x, 12.0(1x), 12.5(1), 14 through 14SU4a , or any 14 ES from 14.0.1.11001-1 to 14.0.1.15072-1 . Upgrades from any earlier supported versions require a PCD migration. If you are upgrading from a version prior to 14, ensure
                                 you have the proper licensing prior to doing the upgrade.

For a list of all supported upgrade paths and the supported upgrade method, please see the Compatibility Matrix at:

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-device-support-tables-list.html

Caution

Please note that if you install an SU it may contain fixes that are not included in the newer Unified CM releases. For example,
                                 a fix in an 12.5(1)SU, 12.5(1)SU5, may not be included in 14 because the fix was not available prior to the release of 14.
                                 In this example, an SU or ES on the 14 branch may be required to retain the same fixes.

## New to this Release

For details about the features included in this release, refer to Release Notes for Cisco Unified Communications Manager and
                     IM & Presence Service, Release 14SU5 at:

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-release-notes-list.html

### In addition to the features listed in the Release Notes, the following changes were introduced in 14SU3:

Log4j upgrade to 2.19

### In addition to the features listed in the Release Notes, the following changes were introduced in 14SU1:

This release is signed with a new 2021 signing key. See the Important Notes section for more details.

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

Beginning with CUCM 14SU5, phone firmware that is end of support will no longer be included in the CUCM ISO. These endpoints
                                 will still be allowed to register, unless they have been officially deprecated, but the firmware will not be present in the
                                 TFTP directory following a fresh install. The phones should still register even without the firmware present, but the cmterm-eol_endpoint- 14.0.1.15900-24 .cop.sha512 can be used to install the firmware on the system if needed. See the COP file readme for the list of firmware
                                 that is no longer included by default.

This change only impacts fresh installs and migrations. If you are direct upgrading from a previous version, the firmware
                                 will carry over to the new version.

### Warning for Upgrades to 15

Warning

This SU adds support for Smart Receiver Transport for licensing. This feature is not found in the CUCM 15 base or 15SU1 releases,
                                 as those versions were released prior to development of this feature. Upgrades from this SU to any CUCM or IM&P 15 versions
                                 lower than 15SU2 are not allowed and will not be displayed as valid upgrade options. Customers upgrading from this SU should
                                 choose 15SU2 or higher as their target upgrade.

### Warning for Upgrades from 10.5(2)

Warning

Per the Supported Upgrade and Migration Paths in the Compatibility Matrix , direct upgrades from any 10.5.2 release to any 14 release are not supported (PCD Migration or Fresh Install with Data Import
                                 are the only supported upgrade options from 10.5.2). In previous releases of 14, this upgrade path was not blocked in the
                                 code even though it is not supported. Starting with 14SU2, upgrades from release 10.5.2 are now blocked in the code so a direct
                                 upgrade attempt will now fail as an usupported upgrade.

### Warning for Upgrades with FIPS Enabled

Warning

If you are upgrading with FIPS enabled and/or using PCD with FIPS enabled, see the CiscoSSL7 COP File Readme for information on the COP file ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop. This document details the pre-requisites
                                 required for direct upgrade or direct migration to the 14SU2 or higher destination versions when FIPS is enabled.

## Related Documentation

To view documentation that supports Cisco Unified CM Release 14, go to:

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

Because the 14.0.1.15900-24 build is a non-bootable ISO, it proves useful only for upgrades. You cannot use it for new installations. You may however
                                 install with the base version 14.0.1.10000-20 and apply 14.0.1.15900-24 as a patch during the installation.

Release 14SU5 is available in both restricted (which is the release type that has always been available from Cisco) and unrestricted versions
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

Refer to the “Switch to Previous Version” section in the Upgrade Procedures chapter at Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 14 for detailed instructions on “Reverting to a Previous Version.”

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html

## Caveats

Caveats describe unexpected behavior on a Cisco Unified Communications server. The following sections contain lists and descriptions
                     of resolved and open caveats in this release.

### Resolved Caveats

Resolved Caveats for Cisco Unified Communications Manager Release 14SU5 describes possible unexpected behaviors in Cisco Unified Communications Manager 14 releases.

Resolved CUCM Caveats in 14SU5 (everything fixed in SU5 since SU4/4a) Click Here for the list

Cumulative Resolved CUCM Caveats (everything fixed in all SU's since base 14) Click Here for the list

### Open Caveats

Open Caveats for Cisco Unified Communications Manager Release 14SU5 describes a few of the possible unexpected behaviors still remaining in Cisco Unified Communications Manager Release 14SU5 .

### CUCM Caveats 14 Complete List

For a complete list of caveats applicable to 14, use the following Bug Search Tool link:

https://bst.cloudapps.cisco.com/bugsearch?pf=prdNm&sb=afr&kw=*&bt=custV&prdNam=Cisco%20Unified%20Communications%20Manager%20(CallManager)&rls=14.0(1.1

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

Filter String for 14SU5:

For Mac: Table.SelectRows(#"Changed column type", each not Text.Contains([Known Fixed Releases], "CCM.014.000(001.10000.020)") and
                     not Text.Contains([Known Fixed Releases], "CCM.014.000(001.11900.132)") and not Text.Contains([Known Fixed Releases], "CCM.014.000(001.12900.161)")
                     and not Text.Contains([Known Fixed Releases], "CCM.014.000(001.13900.155)") and not Text.Contains([Known Fixed Releases],
                     "CCM.014.000(001.14900.094)") and not Text.Contains([Known Fixed Releases], "CCM.014.000(001.14901.001)") and not Text.Contains([Known
                     Fixed Releases], "CCM.014.000(001.15900.024)") and not Text.StartsWith([Known Fixed Releases], "UCMAP") and Text.Contains([#"Product
                     - Series"], "CallManager")) For Windows: = Table.SelectRows(#"Changed Type", each not Text.Contains([Known Fixed Releases], "CCM.014.000(001.10000.020)") and not Text.Contains([Known
                     Fixed Releases], "CCM.014.000(001.11900.132)") and not Text.Contains([Known Fixed Releases], "CCM.014.000(001.12900.161)")
                     and not Text.Contains([Known Fixed Releases], "CCM.014.000(001.13900.155)") and not Text.Contains([Known Fixed Releases],
                     "CCM.014.000(001.14900.094)") and not Text.Contains([Known Fixed Releases], "CCM.014.000(001.14901.001)") and not Text.Contains([Known
                     Fixed Releases], "CCM.014.000(001.15900.024)") and not Text.StartsWith([Known Fixed Releases], "UCMAP") and Text.Contains([#"Product
                     - Series"], "CallManager"))

Security Advisory Caveats: To get a list of caveats that are applicable to Security Advisories or other security related issues, after filtering for
                     a specific release using the examples above, an additional filter for the keyword PSIRT can be applied to the Release Note
                     Enclosure column.

## Firmware Versions

SUs contain firmware loads, however, Cisco recommends that you always download the latest firmware load from the Software
                     Download Center.

### End of Support Firmware Files Removed

Warning

Beginning with CUCM 14SU5, phone firmware that is end of support will no longer be included in the CUCM ISO. These endpoints
                                 will still be allowed to register, unless they have been officially deprecated, but the firmware will not be present in the
                                 TFTP directory following a fresh install. The phones should still register even without the firmware present, but the cmterm-eol_endpoint- 14.0.1.15900-24 .cop.sha512 can be used to install the firmware on the system if needed. See the COP file readme for the list of firmware
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
3905                                      3905.9-4-1SR4-2                 9.4(1SR4.2)
6901-sccp                                 6901-sccp.9-3-1-SR3-2.k4        9.3(1.0)  
6901-sip                                  6901-sip.9-3-1-SR3-2.k4         9.3(1.0)  
7832-sip.14                               7832-sip.14-3-1-0301-349.k4     3.1(0301.349)
78xx.14                                   78xx.14-3-1-0301-349.k4         3.1(0301.349)
8821-sip                                  8821-sip.11-0-6SR7-2.k4         11.0(6SR7.2)
8832-sip.14                               8832-sip.14-3-1-0301-349.k4     3.1(0301.349)
8845_65-sip.14                            8845_65-sip.14-3-1-0301-349.k4  3.1(0301.349)
88xx-sip.14                               88xx-sip.14-3-1-0301-349.k4     3.1(0301.349)
ATA191.12                                 ATA191.12-0-3-0001-139          0.3(0001.139)
headset-builtin                           headset-builtin.3-4-0001-1.k4   3.4(0001.1)
PHONEOS.3                                 PHONEOS.3-5-1-0102-59           5.1(0102.59)

Plug-in Report
------------------------------------------
cm-rtmt-client-plugin-14.0.0.0-0.i386.rpm
cm-ctlc-plugin-6.0.0.1-1.i386.rpm
cm-jtapi-plugin-14.0.1.15900-1.i386.rpm
cm-tsp-plugin-14.0.1.4-0.i386.rpm
cm-axlsqltoolkit-plugin-1.1.0.0-1.i386.rpm
cm-taps-plugin-7.0.2.0-1.i386.rpm

TZDATA file                               Version
----------------------------------------  ----------
platform-tzdata-2024a-1.el7.noarch.rpm    2024-a
```

| Date | Revision |
|---|---|
| October 14, 2025 | Initial publication |

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

| Note | You can only install this SU on Cisco Unified Communications Manager Release 10.5 through 11.x, 12.0(1x), 12.5(1), 14 through 14SU4a , or any 14 ES from 14.0.1.11001-1 to 14.0.1.15072-1 . Upgrades from any earlier supported versions require a PCD migration. If you are upgrading from a version prior to 14, ensure
                                 you have the proper licensing prior to doing the upgrade. |
|---|---|

| Caution | Please note that if you install an SU it may contain fixes that are not included in the newer Unified CM releases. For example,
                                 a fix in an 12.5(1)SU, 12.5(1)SU5, may not be included in 14 because the fix was not available prior to the release of 14.
                                 In this example, an SU or ES on the 14 branch may be required to retain the same fixes. |
|---|---|

| Warning | Beginning with CUCM 14SU5, phone firmware that is end of support will no longer be included in the CUCM ISO. These endpoints
                                 will still be allowed to register, unless they have been officially deprecated, but the firmware will not be present in the
                                 TFTP directory following a fresh install. The phones should still register even without the firmware present, but the cmterm-eol_endpoint- 14.0.1.15900-24 .cop.sha512 can be used to install the firmware on the system if needed. See the COP file readme for the list of firmware
                                 that is no longer included by default. This change only impacts fresh installs and migrations. If you are direct upgrading from a previous version, the firmware
                                 will carry over to the new version. |
|---|---|

| Warning | This SU adds support for Smart Receiver Transport for licensing. This feature is not found in the CUCM 15 base or 15SU1 releases,
                                 as those versions were released prior to development of this feature. Upgrades from this SU to any CUCM or IM&P 15 versions
                                 lower than 15SU2 are not allowed and will not be displayed as valid upgrade options. Customers upgrading from this SU should
                                 choose 15SU2 or higher as their target upgrade. |
|---|---|

| Warning | Per the Supported Upgrade and Migration Paths in the Compatibility Matrix , direct upgrades from any 10.5.2 release to any 14 release are not supported (PCD Migration or Fresh Install with Data Import
                                 are the only supported upgrade options from 10.5.2). In previous releases of 14, this upgrade path was not blocked in the
                                 code even though it is not supported. Starting with 14SU2, upgrades from release 10.5.2 are now blocked in the code so a direct
                                 upgrade attempt will now fail as an usupported upgrade. |
|---|---|

| Warning | If you are upgrading with FIPS enabled and/or using PCD with FIPS enabled, see the CiscoSSL7 COP File Readme for information on the COP file ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop. This document details the pre-requisites
                                 required for direct upgrade or direct migration to the 14SU2 or higher destination versions when FIPS is enabled. |
|---|---|

| Note | Apply this SU to all of your Cisco Unified Communications Manager servers, beginning with the publisher server and TFTP server |
|---|---|

| Note | Because the 14.0.1.15900-24 build is a non-bootable ISO, it proves useful only for upgrades. You cannot use it for new installations. You may however
                                 install with the base version 14.0.1.10000-20 and apply 14.0.1.15900-24 as a patch during the installation. |
|---|---|

| Note | Once installed, UNRST releases can never be converted or upgraded to releases which support full encryption capabilities |
|---|---|

| ISO Name: | UCSInstall_UCOS_14.0.1.15900-24.sha512.iso |
|---|---|
| MD5: | d463de42f26a3b93aafbc3fa371b4d9a |
| SHA512: | 82e66685e179fd5ade25349344e8dffafc51357549fb350e0b303eadfe598ed2e5defc85779f5 e8e0d77103891484fc946d237a9376f13f4a8f2a58bd31dcf5d |

| ISO Name: | UCSInstall_UCOS_UNRST_14.0.1.15900-24.sha512.iso |
|---|---|
| MD5: | a1147ea556b49e71db02b11c7f626aae |
| SHA512: | dc4b809bb9e0c85bc98f8d5c3625d23063cfb323356a0ceea18c6f2be548801e1e71b15370aec 47b47aac151efe6706dce9fd5aee3ef3fb680792a6f36482835 |

| Note | Revert to the previous version on all servers in the cluster in the same order in which you performed the upgrade. |
|---|---|

| Warning | Beginning with CUCM 14SU5, phone firmware that is end of support will no longer be included in the CUCM ISO. These endpoints
                                 will still be allowed to register, unless they have been officially deprecated, but the firmware will not be present in the
                                 TFTP directory following a fresh install. The phones should still register even without the firmware present, but the cmterm-eol_endpoint- 14.0.1.15900-24 .cop.sha512 can be used to install the firmware on the system if needed. See the COP file readme for the list of firmware
                                 that is no longer included by default. This change only impacts fresh installs and migrations. If you are direct upgrading from a previous version, the firmware
                                 will carry over to the new version. |
|---|---|