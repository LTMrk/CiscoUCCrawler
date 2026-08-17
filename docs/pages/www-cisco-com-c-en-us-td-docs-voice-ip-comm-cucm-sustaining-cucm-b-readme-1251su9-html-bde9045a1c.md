---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-sustaining-cucm-b-readme-1251su9-html-bde9045a1c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/sustaining/cucm_b_readme-1251su9.html
retrieved_at: 2026-08-16T23:51:36.514074+00:00
---

ReadMe for Cisco Unified Communications Manager Release 12.5(1)SU9

# ReadMe for Cisco Unified Communications Manager Release 12.5(1)SU9

### Download Options

Updated: July 25, 2024

First Published: July 25, 2024

# Revision History

Date

Revision

July 23, 2024

Initial publication

## Introduction

To view the release notes for previous versions of Cisco Unified Communications Manager, choose the Cisco Unified Communications
                                 Manager version from the following URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_release_notes_list.html

Please review all sections in this document pertaining to installation before you install this Service Update (SU). Failure
                                 to install this SU as described may result in inconsistent Cisco Unified Communications Manager behavior.

This 12.5(1)SU9 ReadMe file contains important information about installation procedures and resolved caveats for Cisco Unified Communications
                     Manager release 12.5(1)SU9 . This SU can be applied to Cisco Unified Communications Manager and Session Management Edition.

Before you install Cisco Unified Communications Manager, Cisco recommends that you review the Important Notes for information about issues that may affect your system.

## System Requirements

The following sections comprise the system requirements for this release.

### Server Support

In this release, you cannot install or run Cisco Unified Communications Manager on server hardware; you must run these applications
                     on virtual machines. Please refer to the “Hardware” section of the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1) for additional details:

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/12_5_1/cucm_b_upgrade-migration-guide-125x.html

### Uninterruptible Power Supply

Ensure that you connect each node to an uninterruptible power supply (UPS) to provide backup power and protect your system.

Caution

Failure to connect the Cisco Unified Communication Manager nodes to a UPS may result in damage to physical media and require
                                 a new installation of Cisco Unified CM.

## Version and Description

This SU is a cumulative update that incorporates all of the fixes and changes from Cisco Unified Communications Manager 12.5(1) through 12.5(1)SU8(a) along with additional changes that are specific to this SU.

You can only install this SU on Cisco Unified Communications Manager Release 8.6(x) through 11.x, 12.0(1x), 12.5(1) through 12.5(1)SU8(a) , or any 12.5(1) ES from 12.5.1.11001-1 to 12.5.1.19211-1 . Upgrades from any earlier supported versions require a PCD migration. If you are upgrading from a version prior to 12.x,
                                 ensure you have the proper licensing prior to doing the upgrade.

For a list of all supported upgrade paths and the supported upgrade method, please see the Compatibility Matrix at:

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-device-support-tables-list.html

Caution

Please note that if you install an SU it may contain fixes that are not included in the newer Unified CM releases. For example,
                                 a fix in an 11.5(1)SU, 11.5(1)SU6, may not be included in 12.0(1) because the fix was not available prior to the release of
                                 12.0(1). In this example, an SU or ES on the 12.0(1) branch may be required to retain the same fixes.

## New to this Release

For details about the features included in this release, refer to Release Notes for Cisco Unified Communications Manager and
                     IM & Presence Service, Release 12.5(1) at:

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-release-notes-list.html

### In addition to the features listed in the Release Notes, the following changes were introduced in 12.5(1)SU7:

Log4j upgrade to 2.17.2

### In addition to the features listed in the Release Notes, the following changes were introduced in 12.5(1)SU4:

Upgrade to JDK8

Upgrade to Tomcat9

## Important Notes

Compatibility between collaboration products is detailed at the following link. You must insure your versions are compatible
                     before beginning your upgrade:

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/CSR-Compatibility-Matrix-InteractiveHTML.html

Cisco provides the following guidance to help you successfully upgrade Cisco Unified Communications Manager software:

To minimize call-processing interruptions during the upgrade process, register all devices to servers that are running the
                           same version of Cisco Unified Communications Manager software. Make sure that you register all devices to the backup Cisco
                           Unified Communications Manager server or to the primary Cisco Unified Communications Manager server, but not to both the backup
                           and primary servers.

## Related Documentation

To view documentation that supports Cisco Unified CM Release 12.5(x), go to:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-documentation-roadmaps-list.html

## Before You Begin

Before you upgrade the software version of Cisco Unified Communications Manager, verify your current software version.

To do that, open Cisco Unified Communications Manager Administration. The following information displays:

Cisco Unified CM Administration System version: x.x.x

## Installation Instructions

Apply this SU to all of your Cisco Unified Communications Manager servers, beginning with the publisher server and TFTP server

Refer to the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 12.5(1) for detailed information about doing this upgrade:

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/12_5_1/cucm_b_upgrade-migration-guide-125x.html

Because the 12.5.1.21900-29 build is a non-bootable ISO, it proves useful only for upgrades. You cannot use it for new installations. You may however
                                 install with the base version 12.5.1.10000-22 and apply 12.5.1.21900-29 as a patch during the installation.

Release 12.5(1)SU9 is available in both restricted (which is the release type that has always been available from Cisco) and unrestricted versions
                     of software to comply with import / export restrictions to various countries. The unrestricted version is available in limited
                     markets. Please refer to the “Export Restricted and Export Unrestricted Software” section in the Understanding Upgrades and Migrations chapter, of the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1) referenced above, for a more detailed description.

Once installed, UNRST releases can never be converted or upgraded to releases which support full encryption capabilities

The file names and hash values you will use for this upgrade are:

ISO Name:

MD5:

SHA512:

ISO Name:

MD5:

SHA512:

## Reverting to a Previous Version

Revert the SU on all servers in the cluster in the same order in which you performed the installation.

Refer to the “Switch to Previous Version” section in the Upgrade Procedures chapter at Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 12.5(1) for detailed instructions on “Reverting to a Previous Version.”

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/12_5_1/cucm_b_upgrade-migration-guide-125x.html

## Caveats

Caveats describe unexpected behavior on a Cisco Unified Communications server. The following sections contain lists and descriptions
                     of resolved and open caveats in this release.

### Resolved Caveats

Resolved Caveats for Cisco Unified Communications Manager Release 12.5(1)SU9 describes possible unexpected behaviors in previous Cisco Unified Communications Manager 12.5(1) releases.

Resolved CUCM Caveats in 12.5(1)SU9 (everything fixed in SU9 since SU8(a)) Click Here for the list

Cumulative Resolved CUCM Caveats (everything fixed in all SU's since base 12.5(1)) Click Here for the list

### Open Caveats

Open Caveats for Cisco Unified Communications Manager Release 12.5(1)SU9 describes a few of the possible unexpected behaviors still remaining in Cisco Unified Communications Manager Release 12.5(1)SU9 .

### CUCM Caveats 12.5.1 Complete List

For a complete list of caveats applicable to 12.5.1, use the following Bug Search Tool link:

https://bst.cloudapps.cisco.com/bugsearch?pf=prdNm&sb=afr&kw=*&bt=custV&prdNam=Cisco%20Unified%20Communications%20Manager%20(CallManager)&rls=12.5(1.1

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

Filter String for 12.5.1SU9:

For Mac: Table.SelectRows(#"Changed column type", each not Text.Contains([Known Fixed Releases], "CCM.012.005(001.10000.022)")
                     and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.11900.146)") and not Text.Contains([Known Fixed Releases],
                     "CCM.012.005(001.12900.115)") and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.13900.152)") and not Text.Contains([Known
                     Fixed Releases], "CCM.012.005(001.14900.063)") and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.15900.066)")
                     and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.16900.048)") and not Text.Contains([Known Fixed Releases],
                     "CCM.012.005(001.17900.064)") and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.18100.014)") and not Text.Contains([Known
                     Fixed Releases], "CCM.012.005(001.18900.040)") and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.18901.001)")
                     and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.21900.029)") and not Text.StartsWith([Known Fixed Releases],
                     "UCMAP") and Text.Contains([#"Product - Series"], "CallManager") or [Known Fixed Releases] = null) For Windows: = Table.SelectRows(#"Changed Type", each not Text.Contains([Known Fixed Releases], "CCM.012.005(001.10000.022)") and not Text.Contains([Known
                     Fixed Releases], "CCM.012.005(001.11900.146)") and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.12900.115)")
                     and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.13900.152)") and not Text.Contains([Known Fixed Releases],
                     "CCM.012.005(001.14900.063)") and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.15900.066)") and not Text.Contains([Known
                     Fixed Releases], "CCM.012.005(001.16900.048)") and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.17900.064)")
                     and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.18100.014)") and not Text.Contains([Known Fixed Releases],
                     "CCM.012.005(001.18900.040)") and not Text.Contains([Known Fixed Releases], "CCM.012.005(001.18901.001)") and not Text.Contains([Known
                     Fixed Releases], "CCM.012.005(001.21900.029)") and not Text.StartsWith([Known Fixed Releases], "UCMAP") and Text.Contains([#"Product
                     - Series"], "CallManager") or [Known Fixed Releases] = null)

Security Advisory Caveats: To get a list of caveats that are applicable to Security Advisories or other security related issues, after filtering for
                     a specific release using the examples above, an additional filter for the keyword PSIRT can be applied to the Release Note
                     Enclosure column.

## Firmware Versions

SUs contain firmware loads, however, Cisco recommends that you always download the latest firmware load from the Software
                     Download Center.

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
----------------------------------------  ------------------------------  ----------3905                                      3905.9-4-1SR4-2                 9.4(1SR4.2)
3911_3951-sip                             3911_3951-sip.8-1-4a            8.1(4.0)  
6608                                      6608-4.0.0.32-mgcp              4.0(0.32) 
6608cfb                                   6608cfb-4.0.0.03-sccp           4.0(0.3)  
6608mtp                                   6608mtp-4.0.0.06-sccp           4.0(0.6)  
6624                                      6624-4.0.0.13-mgcp              4.0(0.13) 
6901-sccp                                 6901-sccp.9-3-1-SR3-1           9.3(1.0)  
6901-sip                                  6901-sip.9-3-1-SR3-1            9.3(1.0)  
6911-sccp                                 6911-sccp.9-3-1-SR2-3           9.3(1.0)  
6911-sip                                  6911-sip.9-3-1-SR2-4            9.3(1.0)  
6945-SCCP                                 6945-SCCP-9-4-1-3SR3            9.4(1.3)  
6945-SIP                                  6945-SIP-9-4-1-3SR3             9.4(1.3)  
69xx-SCCP                                 69xx-SCCP-9-4-1-3SR3            9.4(1.3)  
69xx-SIP                                  69xx-SIP-9-4-1-3SR3             9.4(1.3)  
7832-sip                                  7832-sip.14-2-1-0201-40.k4      14.2.1(0201.40)
78xx                                      78xx.14-2-1-0201-40.k4          14.2.1(0201.40)
7911_7906-sccp                            7911_7906-sccp.9-4-2SR3-1       9.4(2SR3.1)
7911_7906-sip                             7911_7906-sip.9-4-2SR3-1        9.4(2SR3.1)
7914-sccp                                 7914-sccp.5-0-4                 5.0(4.0)  
7915                                      7915.1-0-4-2                    1.0(4.2)  
7916                                      7916.1-0-4-2                    1.0(4.2)  
7925-sccp                                 7925-sccp.1-4-8SR1-5.k3         1.4(8SR1.5)
7926-sccp                                 7926-sccp.1-4-8SR1-5.k3         1.4(8SR1.5)
7931-sccp                                 7931-sccp.9-4-2SR2-2            9.4(2SR2.2)
7931-sip                                  7931-sip.9-4-2SR2-2             9.4(2SR2.2)
7936-sccp                                 7936-sccp.3-3-21                3.3(21.0) 
7937                                      7937-1-4-5-7-SCCP               1.4(5.7)  
7940-7960                                 7940-7960-8.12.00-sip           8.12(00.0)
7940-7960-sccp                            7940-7960-sccp.8-1-2SR2         8.1(2SR2.0)
7941_7961-sccp                            7941_7961-sccp.9-4-2SR3-1       9.4(2SR3.1)
7941_7961-sip                             7941_7961-sip.9-4-2SR3-1        9.4(2SR3.1)
7942_7962-sccp                            7942_7962-sccp.9-4-2SR3-1       9.4(2SR3.1)
7942_7962-sip                             7942_7962-sip.9-4-2SR3-1        9.4(2SR3.1)
7945_7965-sccp                            7945_7965-sccp.9-4-2SR4         9.4(2SR4.0)
7945_7965-sip                             7945_7965-sip.9-4-2SR4-3        9.4(2SR4.3)
7975-sccp                                 7975-sccp.9-4-2SR4              9.4(2SR4.0)
7975-sip                                  7975-sip.9-4-2SR4               9.4(2SR4.0)
7985                                      7985-4-1-7-0-sccp               4.1(7.0)  
8821-sip                                  8821-sip.11-0-6SR5-5.k4         11.0(6SR5.5)
8831-sip                                  8831-sip.10-3-1SR7-2            10.3(1SR7.2)
8832-sip                                  8832-sip.14-2-1-0201-40.k4      14.2.1(0201.40)
8845_65-sip                               8845_65-sip.14-2-1-0201-40.k4   14.2.1(0201.40)
88xx-sip                                  88xx-sip.14-2-1-0201-40.k4      14.2.1(0201.40)
894x-sccp                                 894x-sccp.9-4-2SR3-1            9.4(2SR3.1)
894x-sip                                  894x-sip.9-4-2SR3-1             9.4(2SR3.1)
8961                                      8961.9-4-2SR4-1.k3              9.4(2SR4.1)
9951                                      9951.9-4-2SR4-1.k3              9.4(2SR4.1)
9971                                      9971.9-4-2SR4-1.k3              9.4(2SR4.1)
ata                                       ata-3.2.4-sccp                  3.2(4.0)  
ata187                                    ata187.9-2-3-1                  9.2(3.1)  
ata190                                    ata190.1-2-2-003                1.2(2.3)  
ATA191                                    ATA191.12-0-2-0001-011          12.0.2(0001.11)
headset-builtin                           headset-builtin.3-2-0001-1.k4   3.2(0001.1)
PHONEOS-8875                              PHONEOS-8875.2-3-1-0001-26      2.3.1(0001.26)

Plug-in Report
------------------------------------------
cm-rtmt-client-plugin-12.5.0.0-0.i386.rpm
cm-ctlc-plugin-6.0.0.1-1.i386.rpm
cm-taps-plugin-7.0.2.0-1.i386.rpm
cm-jtapi-plugin-12.5.1.21900-1.i386.rpm
cm-axlsqltoolkit-plugin-1.1.0.0-1.i386.rpm
cm-tsp-plugin-12.5.2.4-0.i386.rpm

TZDATA file                               Version
----------------------------------------  ----------
platform-tzdata-2023c-1.el7.noarch.rpm    2023-c
```

| Date | Revision |
|---|---|
| July 23, 2024 | Initial publication |

| Note | To view the release notes for previous versions of Cisco Unified Communications Manager, choose the Cisco Unified Communications
                                 Manager version from the following URL: http://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_release_notes_list.html |
|---|---|

| Note | Please review all sections in this document pertaining to installation before you install this Service Update (SU). Failure
                                 to install this SU as described may result in inconsistent Cisco Unified Communications Manager behavior. |
|---|---|

| Note | Before you install Cisco Unified Communications Manager, Cisco recommends that you review the Important Notes for information about issues that may affect your system. |
|---|---|

| Caution | Failure to connect the Cisco Unified Communication Manager nodes to a UPS may result in damage to physical media and require
                                 a new installation of Cisco Unified CM. |
|---|---|

| Note | You can only install this SU on Cisco Unified Communications Manager Release 8.6(x) through 11.x, 12.0(1x), 12.5(1) through 12.5(1)SU8(a) , or any 12.5(1) ES from 12.5.1.11001-1 to 12.5.1.19211-1 . Upgrades from any earlier supported versions require a PCD migration. If you are upgrading from a version prior to 12.x,
                                 ensure you have the proper licensing prior to doing the upgrade. |
|---|---|

| Caution | Please note that if you install an SU it may contain fixes that are not included in the newer Unified CM releases. For example,
                                 a fix in an 11.5(1)SU, 11.5(1)SU6, may not be included in 12.0(1) because the fix was not available prior to the release of
                                 12.0(1). In this example, an SU or ES on the 12.0(1) branch may be required to retain the same fixes. |
|---|---|

| Note | Apply this SU to all of your Cisco Unified Communications Manager servers, beginning with the publisher server and TFTP server |
|---|---|

| Note | Because the 12.5.1.21900-29 build is a non-bootable ISO, it proves useful only for upgrades. You cannot use it for new installations. You may however
                                 install with the base version 12.5.1.10000-22 and apply 12.5.1.21900-29 as a patch during the installation. |
|---|---|

| Note | Once installed, UNRST releases can never be converted or upgraded to releases which support full encryption capabilities |
|---|---|

| ISO Name: | UCSInstall_UCOS_12.5.1.21900-29.sha512.iso |
|---|---|
| MD5: | 8433423a7d3b1be224eb4b5db5183f64 |
| SHA512: | d1f94be2c25145153c3d30486550afdd0ce40d4d68c188fd3d8038f9ac7b33c43e2207caa6ededb00abdd1ee088339742f7 9efa5b2f55ea99c389906e95a85c1 |

| ISO Name: | UCSInstall_UCOS_UNRST_12.5.1.21900-29.sha512.iso |
|---|---|
| MD5: | acd5a52a449a4c378a6ddc544bd08907 |
| SHA512: | cddbf55cd7b341b09f2e29d0289996db914a7b4e2f07973945f402f2f5ac0d5e4cf4db0afed80c37c5072a7d78ded4b53855a 1a7e5d58418309ea15a86c40e5b |

| Note | Revert the SU on all servers in the cluster in the same order in which you performed the installation. |
|---|---|