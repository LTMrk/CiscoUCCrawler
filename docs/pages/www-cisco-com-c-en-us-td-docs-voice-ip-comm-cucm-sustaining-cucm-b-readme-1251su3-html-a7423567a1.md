---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-sustaining-cucm-b-readme-1251su3-html-a7423567a1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/sustaining/cucm_b_readme-1251su3.html
retrieved_at: 2026-08-17T00:04:00.462947+00:00
---

ReadMe for Cisco Unified Communications Manager Release 12.5(1)SU3

# ReadMe for Cisco Unified Communications Manager Release 12.5(1)SU3

### Download Options

Updated: August 24, 2020

First Published: August 13, 2020

# Revision History

Date

Revision

August 13, 2020

Initial publication

## Introduction

To view the release notes for previous versions of Cisco Unified Communications Manager, choose the Cisco Unified Communications
                                 Manager version from the following URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps556/prod_release_notes_list.html

Please review all sections in this document pertaining to installation before you install this Service Update (SU). Failure
                                 to install this SU as described may result in inconsistent Cisco Unified Communications Manager behavior.

This 12.5(1)SU3 ReadMe file contains important information about installation procedures and resolved caveats for Cisco Unified Communications
                     Manager release 12.5(1)SU3 . This SU can be applied to Cisco Unified Communications Manager and Session Management Edition.

Before you install Cisco Unified Communications Manager, Cisco recommends that you review the Important Notes for information about issues that may affect your system.

## System Requirements

The following sections comprise the system requirements for this release.

### Server Support

In this release, you cannot install or run Cisco Unified Communications Manager on server hardware; you must run these applications
                     on virtual machines. Please refer to the “Hardware” section of the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(1) for additional details:

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/upgrade/12_5_1/cucm_b_upgrade-migration-guide-125x.html

### Uninterruptible Power Supply

Ensure that you connect each node to an uninterruptible power supply (UPS) to provide backup power and protect your system.

Failure to connect the Cisco Unified Communication Manager nodes to a UPS may result in damage to physical media and require
                                 a new installation of Cisco Unified CM.

## Version and Description

This SU is a cumulative update that incorporates all of the fixes and changes from Cisco Unified Communications Manager 12.5(1) through 12.5(1)SU2 along with additional changes that are specific to this SU.

You can only install this SU on Cisco Unified Communications Manager Release 8.6(x) through 11.x, 12.0(1x), 12.5(1) through 12.5(1)SU2 , or any 12.5(1) ES from 12.5.1.11001-1 to 12.5.1.13032-2 . Upgrades from any earlier supported versions require a PCD migration. If you are upgrading from a version prior to 12.x,
                                 ensure you have the proper licensing prior to doing the upgrade.

For a list of all supported upgrade paths and the supported upgrade method, please see the Compatibility Matrix at:

http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-device-support-tables-list.html

Please note that if you install an SU it may contain fixes that are not included in the newer Unified CM releases. For example,
                                 a fix in an 11.5(1)SU, 11.5(1)SU6, may not be included in 12.0(1) because the fix was not available prior to the release of
                                 12.0(1). In this example, an SU or ES on the 12.0(1) branch may be required to retain the same fixes.

## New to this Release

For details about the features included in this release, refer to Release Notes for Cisco Unified Communications Manager and
                     IM & Presence Service, Release 12.5(1) at:

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

### Warning for Upgrades from 12.5(1)

There is an open caveat in the Upgrade Enhancements feature in all 12.5(1) releases, where the source version is prior to SU2, which could cause cluster upgrades to newer 12.5(1)
                                 versions to fail. Use the Bug Search Toolkit link below for more details on the conditions that cause the issue and possible
                                 workarounds:

https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvq22312

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

Because the 12.5.1.13900-152 build is a non-bootable ISO, it proves useful only for upgrades. You cannot use it for new installations. You may however
                                 install with the base version 12.5.1.10000-22 and apply 12.5.1.13900-152 as a patch during the installation.

Release 12.5(1)SU3 is available in both restricted (which is the release type that has always been available from Cisco) and unrestricted versions
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

Resolved Caveats for Cisco Unified Communications Manager Release 12.5(1)SU3 describes possible unexpected behaviors in previous Cisco Unified Communications Manager 12.5(1) releases.

Resolved CUCM Caveats in 12.5(1)SU3 (everything fixed in SU3 since SU2) Click Here for the list

Resolved CUCM Caveats in 12.5(1)SU2 (everything fixed in SU2 since SU1) Click Here for the list

Resolved CUCM Caveats in 12.5(1)SU1 (everything fixed in SU1 since base 12.5(1)) Click Here for the list

Cumulative Resolved CUCM Caveats (everything fixed in all SU's since base 12.5(1)) Click Here for the list

### Open Caveats

Open Caveats for Cisco Unified Communications Manager Release 12.5(1)SU3 describes a few of the possible unexpected behaviors still remaining in Cisco Unified Communications Manager Release 12.5(1)SU3 .

Open CUCM Caveats in 12.5(1)SU3 CSCvv07486: Unable to sync Access Points in WLC due to SNMP requests too large CSCvv23885: Incorrect LDAP password caused JVM core dump and Tomcat service failure

### CUCM Caveats 12.5(1) Complete List

For a complete list of caveats applicable to 12.5(1), use the following Bug Search Tool link:

https://bst.cloudapps.cisco.com/bugsearch?kw=*&pf=prdNm&pfVal=268439621&rls=12.5(1.1&sb=afr&bt=null

To determine the caveats that were open for a specific release, download the results to Excel and use the Known Fixed Release
                     values above to filter out the applicable releases. The Known Fixed Release for base 12.5(1) is 12.5(1.10000.22). Once the
                     filters are applied, additional sorting / filtering can be applied for Bug Severity, Bug Status, and keywords. Here are some
                     examples of how to generate lists for a specific release:

All SU3 Unresolved Caveats: To get a list of caveats that are applicable to 12.5(1) but are not fixed in SU3, use an Advanced Filter in Excel with an
                     AND condition on the Known Fixed Releases column with the following values:

<>*CCM.12.5(1.10000.22)* <>*CCM.012.005(001.11900.146)* <>*CCM.012.005(001.12900.115)* <>*CCM.012.005(001.13900.152)*

All SU2 Unresolved Caveats: To get a list of caveats that are applicable to 12.5(1) but are not fixed in SU2, use an Advanced Filter in Excel with an
                     AND condition on the Known Fixed Releases column with the following values:

<>*CCM.012.005(001.10000.022)* <>*CCM.012.005(001.11900.146)* <>*CCM.012.005(001.12900.115)*

All SU1 Unresolved Caveats: To get a list of caveats that are applicable to 12.5(1) but are not fixed in SU1, use an Advanced Filter in Excel with an
                     AND condition on the Known Fixed Releases column with the following values:

<>*CCM.012.005(001.10000.022)* <>*CCM.012.005(001.11900.146)*

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
----------------------------------------  ------------------------------  ----------
3905                                      3905.9-4-1SR3                   9.4(1SR3.0)
3911_3951-sip                             3911_3951-sip.8-1-4a            8.1(4.0)  
6608                                      6608-4.0.0.32-mgcp              4.0(0.32) 
6608cfb                                   6608cfb-4.0.0.03-sccp           4.0(0.3)  
6608mtp                                   6608mtp-4.0.0.06-sccp           4.0(0.6)  
6624                                      6624-4.0.0.13-mgcp              4.0(0.13) 
6901-sccp                                 6901-sccp.9-3-1-SR2-2           9.3(1.0)  
6901-sip                                  6901-sip.9-3-1-SR2-3            9.3(1.0)  
6911-sccp                                 6911-sccp.9-3-1-SR2-3           9.3(1.0)  
6911-sip                                  6911-sip.9-3-1-SR2-4            9.3(1.0)  
6945-SCCP                                 6945-SCCP-9-4-1-3SR3            9.4(1.3)  
6945-SIP                                  6945-SIP-9-4-1-3SR3             9.4(1.3)  
69xx-SCCP                                 69xx-SCCP-9-4-1-3SR3            9.4(1.3)  
69xx-SIP                                  69xx-SIP-9-4-1-3SR3             9.4(1.3)  
7832-sip.12                               7832-sip.12-8-1-0001-455.k3     12.8(1)
78xx.12                                   78xx.12-8-1-0001-455.k3         12.8(1)
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
8821-sip                                  8821-sip.11-0-5SR1-4.k3         11.0(5SR1.4)
8821-sip                                  8821-sip.11-0-5SR3-2.k3         11.0(5SR3.2)
8831-sip                                  8831-sip.10-3-1SR6-4            10.3(1SR6.4)
8832-sip.12                               8832-sip.12-8-1-0001-455.k3     12.8(1)
8845_65-sip.12                            8845_65-sip.12-8-1-0001-455.k3  12.8(1)
88xx-sip.12                               88xx-sip.12-8-1-0001-455.k3     12.8(1)
894x-sccp                                 894x-sccp.9-4-2SR3-1            9.4(2SR3.1)
894x-sip                                  894x-sip.9-4-2SR3-1             9.4(2SR3.1)
8961                                      8961.9-4-2SR4-1.k3              9.4(2SR4.1)
9951                                      9951.9-4-2SR4-1.k3              9.4(2SR4.1)
9971                                      9971.9-4-2SR4-1.k3              9.4(2SR4.1)
ata                                       ata-3.2.4-sccp                  3.2(4.0)  
ata187                                    ata187.9-2-3-1                  9.2(3.1)  
ata190                                    ata190.1-2-2-003                1.2(2.3)  
ata191                                    ata191.12-0-1SR2-3              12.0(1SR2.3)
headset                                   headset.2-1-0002-2              2.1(0002.2)

Plug-in Report
------------------------------------------
cm-rtmt-client-plugin-12.5.0.0-0.i386.rpm
cm-tsp-plugin-12.5.1.6-0.i386.rpm
cm-jtapi-plugin-12.5.1.13900-2.i386.rpm
cm-ctlc-plugin-6.0.0.1-1.i386.rpm
cm-taps-plugin-7.0.2.0-1.i386.rpm
cm-axlsqltoolkit-plugin-1.1.0.0-1.i386.rpm

TZDATA file                               Version
----------------------------------------  ----------
platform-tzdata-2019b-1.el7.noarch.rpm    2019-b
```

## Obtaining Documentation and Submitting a Service Request

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/en/US/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application.
                     The RSS feeds are a free service and Cisco currently supports RSS version 2.0.

| Date | Revision |
|---|---|
| August 13, 2020 | Initial publication |

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

| Note | You can only install this SU on Cisco Unified Communications Manager Release 8.6(x) through 11.x, 12.0(1x), 12.5(1) through 12.5(1)SU2 , or any 12.5(1) ES from 12.5.1.11001-1 to 12.5.1.13032-2 . Upgrades from any earlier supported versions require a PCD migration. If you are upgrading from a version prior to 12.x,
                                 ensure you have the proper licensing prior to doing the upgrade. |
|---|---|

| Caution | Please note that if you install an SU it may contain fixes that are not included in the newer Unified CM releases. For example,
                                 a fix in an 11.5(1)SU, 11.5(1)SU6, may not be included in 12.0(1) because the fix was not available prior to the release of
                                 12.0(1). In this example, an SU or ES on the 12.0(1) branch may be required to retain the same fixes. |
|---|---|

| Warning | There is an open caveat in the Upgrade Enhancements feature in all 12.5(1) releases, where the source version is prior to SU2, which could cause cluster upgrades to newer 12.5(1)
                                 versions to fail. Use the Bug Search Toolkit link below for more details on the conditions that cause the issue and possible
                                 workarounds: https://bst.cloudapps.cisco.com/bugsearch/bug/CSCvq22312 |
|---|---|

| Note | Apply this SU to all of your Cisco Unified Communications Manager servers, beginning with the publisher server and TFTP server |
|---|---|

| Note | Because the 12.5.1.13900-152 build is a non-bootable ISO, it proves useful only for upgrades. You cannot use it for new installations. You may however
                                 install with the base version 12.5.1.10000-22 and apply 12.5.1.13900-152 as a patch during the installation. |
|---|---|

| Note | Once installed, UNRST releases can never be converted or upgraded to releases which support full encryption capabilities |
|---|---|

| ISO Name: | UCSInstall_UCOS_12.5.1.13900-152.sgn.iso |
|---|---|
| MD5: | 3f5f5b89be93289ec133cb972aed397c |
| SHA512: | 814fda098db38a86f87703dec200f5901c3b31c2a80743aa358773035bf260908ce827a44cf71aace398f3 84518be1710f131f4d880daf1b42a904debe31d6ee |

| ISO Name: | UCSInstall_UCOS_UNRST_12.5.1.13900-152.sgn.iso |
|---|---|
| MD5: | 10ee24e955926139721a31792c196b96 |
| SHA512: | ad33002fe053946096351794d4aeb405e4e683677350fff58feeb41bb195790f0f4612c88a496ff7c8189 90c89d0309e06d55a3feb253f255db743a2889ec97f |

| Note | Revert the SU on all servers in the cluster in the same order in which you performed the installation. |
|---|---|