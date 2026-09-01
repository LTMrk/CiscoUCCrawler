---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-compat-14-x-cucm-b-compatibility-matrix-cucm-imp-14x-html-d65ce141c3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/14_x/cucm_b_compatibility-matrix-cucm-imp-14x.html
retrieved_at: 2026-09-01T19:40:44.418828+00:00
---

Compatibility Matrix for Cisco Unified Communications Manager and the IM and Presence Service, Release 14x

# Compatibility Matrix for Cisco Unified Communications Manager and the IM and Presence Service, Release 14x

### Download Options

Updated: August 26, 2026

# Compatibility Matrix for Cisco Unified Communications Manager and the IM and Presence Service

## Revision History

Date

Revision

March 18, 2026

Initial guide publication for 14SU6.

March 18, 2026

Updated version support for 14SU6.

March 18, 2026

Added support for Cisco Desk Phone 9811.

March 18, 2026

Updated API and Secure Connection Packages information.

December 02, 2025

Updated the "Calendar Integration with Microsoft Outlook" section to include support for Exchange Server Subscription Edition
                              (SE).

October 14, 2025

Initial guide publication for 14SU5.

October 14, 2025

Updated version support for 14SU5.

October 14, 2025

Updated Web Browsers supported.

October 14, 2025

Updated ciphers list for Unified CM and IM and Presence Service.

October 14, 2025

Removed support for Active Directory 2016 with Windows Server 2016 from the "Calendar Integration with Microsoft Outlook"
                              section.

March 17, 2025

Added support for Cisco Board Pro 55 G2 and Cisco Board Pro 75 G2 from Release 14SU4 onwards.

June 10, 2024

Updated support version for Unified CM Release 14SU4a.

May 30, 2024

Initial guide publication for 14SU4.

May 30, 2024

Updated version support for 14SU4.

May 30, 2024

Added support for Cisco Desk Phone 9800 Series.

May 30, 2024

Updated ciphers list for Unified CM.

May 30, 2024

Removed 'Active Directory 2012 with Windows Server 2012' support from Calendar Integration with Microsoft Outlook section.

July 03, 2023

Removed Intercluster Peering Support for IM and Presence Service Release 10.x.

May 18, 2023

Initial guide publication for 14SU3.

May 18, 2023

Updated version support for 14SU3.

May 18, 2023

Added support for Cisco Video Phone 8875.

May 18, 2023

Updated ciphers list for Unified CM and IM and Presence Service.

May 18, 2023

Added support for Microsoft Active Directory on Windows Server 2022.

May 18, 2023

Added support for Cisco Headset 320 Series and Cisco Headset 720 Series.

June 16, 2022

Initial guide publication for 14SU2.

June 16, 2022

Updated version support for 14SU2.

June 16, 2022

Webex Desk Camera is rebranded to Cisco Desk Camera 4K.

June 16, 2022

Added support for Cisco Desk Camera 1080p.

July 05, 2022

Updated Unified IM and Presence Service release version support to 14SU2a.

October 27, 2021

Initial guide publication for 14SU1.

October 27, 2021

Changed title of the guide to 14x.

October 27, 2021

Updated upgrade paths and version support for 14SU1.

March 31, 2021

Initial guide publication for 14.

April 28, 2021

Added support for Ciphers for Application and OS End Users.

## Purpose of this Document

This document contains compatibility information for 14x releases of Cisco Unified Communications Manager and the IM and Presence
                  Service. This will include subsequent SU releases as well, unless indicated otherwise.

## Supported Upgrade and Migration Paths with COP Files

The following table highlights supported upgrade paths to upgrade to Release 14 and later of Cisco Unified Communications
                     Manager and the IM and Presence Service. It also lists the upgrade paths that require COP files. You must install COP files
                     on each node before you begin an upgrade using the Cisco Unified OS Admin interface, or before you begin an upgrade or migration
                     using the Prime Collaboration Deployment (PCD) tool. If you are using PCD, you can perform a bulk installation of the COP
                     files before you begin the upgrade.

Unless indicated otherwise, each release category includes the SU releases within that category.

You can download COP files for Cisco Unified Communications Manager and the IM and Presence Service at https://software.cisco.com/download/home/268439621 . After you select the destination version for the upgrade, choose Unified Communications Manager Utilities to see the list of COP files.

Although it is not mandatory, we strongly recommend that you run the Upgrade Readiness COP file prior to the upgrade in order
                              to maximize upgrade success. Cisco TAC may require that you run this COP file to provide effective technical support.

If the source is in FIPS mode and/or PCD in FIPS mode, see https://www.cisco.com/web/software/286319173/139477/ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop-ReadMe.pdf for information on the COP file ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop . This document details the pre-requisites required for direct upgrade or direct migration to the 14SU2 destination versions.

If the source is Release 14 or above and the upgrade path is direct standard, see the "Clusterwide Upgrade Task Flow (Direct
                                 Standard)" procedure that details Cluster Upgrade via Unified CM publisher using Unified OS Admin upgrade or CLI upgrade that
                                 will upgrade all cluster nodes in the Unified CM publisher node.

If you are planning to upgrade your source node-by-node or using a single-node only using the local Unified OS Admin upgrade
                                 or CLI upgrade, see the "Upgrade Cluster Nodes (Direct Refresh or Direct Standard" section.

For more information on the procedures, see the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service .

Source

Destination

Mechanism

Pre-requisites

Version Switching* (Source to Destination and Vice Versa)

11.5

14

Direct Refresh Upgrade

Via OS Admin or CLI

Run pre-upgrade-check COP file.

If the Unified CM source is older than 11.5.1.22900-28, then install the following COP file: cop ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

If the IM and Presence Service source is older than 11.5.1.22900-6, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

If you want to upgrade IM and Presence Service from release 11.5.1.18900-15 to 14, use the following COP file: ciscocm.V11.5.1_CSCvv25961_add_diffie_C0085-1.cop.sgn.

Supported

Direct Refresh Upgrade

Via PCD Upgrade Task

Run pre-upgrade-check COP file.

If the Unified CM source is older than 11.5.1.22900-28, then install the following COP file: cop ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

If the IM and Presence Service source is older than 11.5.1.22900-6, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

If you want to upgrade IM and Presence Service from release 11.5.1.18900-15 to 14, use the following COP file: ciscocm.V11.5.1_CSCvv25961_add_diffie_C0085-1.cop.sgn.

If the destination version is 14 SU2 or above and the source version 11.5 is in FIPS mode, then either:

PCD must be in (or placed in) non-FIPS mode.

Use Fresh Install with Data Import instead of using the PCD Upgrade Task.

Supported

PCD 14 Migration Task (V2V)

Run pre-upgrade-check COP file.

If the destination version is 14 SU2 or above and the source version 11.5 is in FIPS mode, then either:

PCD must be in (or placed in) non-FIPS mode.

Use Fresh Install with Data Import instead of using the PCD Migration Task.

Not supported

Fresh Install with Data Import (V2V)

Run pre-upgrade-check COP file.

ciscocm.DataExport_v1.0.cop.sgn

Not supported

12.0

14

Direct Refresh Upgrade

Via OS Admin or CLI

Run pre-upgrade-check COP file.

If the Unified CM source is older than 12.0.1.24900-19, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

If the IM and Presence Service source is older than 12.0.1.21000-34, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

Supported

Direct Refresh Upgrade

Via PCD Upgrade Task

Run pre-upgrade-check COP file.

If the Unified CM source is older than 12.0.1.24900-19, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

If the IM and Presence Service source is older than 12.0.1.21000-34, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

Supported

PCD 14 Migration Task (V2V)

Run pre-upgrade-check COP file.

If the source version is Release 12.0(1) of Unified Communications Manager (12.0.1.10000-10), then you must install the following
                                 COP file: ciscocm-slm-migration.k3.cop.sgn. This is not required if the source version is higher, for example, Release 12.0(1)SU1.

Not supported

Fresh Install with Data Import (V2V)

Run pre-upgrade-check COP file.

ciscocm.DataExport_v1.0.cop.sgn

Not supported

12.5

14

Direct Standard Upgrade (simple upgrades)

Via OS Admin or CLI

Run pre-upgrade-check COP file.

If the Unified CM source is older than 12.5.1.14900-63, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

If the IM and Presence Service source is older than 12.5.1.14900-4, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

Supported

Direct Standard Upgrade

Via PCD Upgrade Task

Run pre-upgrade-check COP file.

If the Unified CM source is older than 12.5.1.14900-63, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

If the IM and Presence Service source is older than 12.5.1.14900-4, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn.

If the destination version is 14 SU2 or above and the source version 12.5 is in FIPS mode, then either:

PCD must be in (or placed in) non-FIPS mode.

Use Fresh Install with Data Import instead of using the PCD Upgrade Task.

Supported

PCD 14 Migration Task (V2V)

Run pre-upgrade-check COP file.

If the destination version is 14 SU2 or above and the source version 12.5 is in FIPS mode, then either:

PCD must be in (or placed in) non-FIPS mode.

Use Fresh Install with Data Import instead of using the PCD Migration Task.

Not supported

Fresh Install with Data Import (V2V)

Run pre-upgrade-check COP file.

ciscocm.DataExport_v1.0.cop.sgn

Not supported

14 or 14SU1

14SU2 and later

Direct Standard Upgrade (simple upgrades)

Via OS Admin or CLI

Run pre-upgrade-check COP file.

Supported

Direct Standard Upgrade

Via PCD Upgrade Task

Run pre-upgrade-check COP file.

If the destination version is 14 SU2 or above and the source version is 14 or 14SU1 in FIPS mode, then either:

PCD must be in (or placed in) non-FIPS mode.

Use Fresh Install with Data Import instead of using the PCD Upgrade Task.

* Version switching refers to the ability to install the new version as an inactive version and switch to the new version,
                     and revert to the old version, whenever you want. This capability is supported with most direct upgrades, but not with migrations.

PCD Upgrades and Migrations—Use Cisco Prime Collaboration Deployment Release 14SU2 for all PCD tasks.

## Supported Versions

The following table outlines which Unified Communications Manager and IM and Presence Service versions are supported with
                     each release:

For this Release...

The Following Versions are Supported...

14

Cisco Unified Communications Manager 14.0.1.10000-20

IM and Presence Service 14.0.1.10000-16

14SU1

Cisco Unified Communications Manager 14.0.1.11900-132

IM and Presence Service 14.0.1.11900-9

14SU2

Cisco Unified Communications Manager 14.0.1.12900-161

14SU2a

IM and Presence Service 14.0.1.12901-1

14SU3

Cisco Unified Communications Manager 14.0.1.13900-155

IM and Presence Service 14.0.1.13900-8

14SU4

Cisco Unified Communications Manager 14.0.1.14901-1

IM and Presence Service 14.0.1.14900-4

14SU5

Cisco Unified Communications Manager 14.0.1.15900-24

IM and Presence Service 14.0.15900-3

14SU6

Cisco Unified Communications Manager 14.0.1.16900-4

IM and Presence Service 14.0.16900-3

### Version Compatibility Between Unified CM and the IM and Presence Service

Version compatibility depends on the IM and Presence Service deployment type. The following table outlines the options and
                        whether a release mismatch is supported between the telephony deployment and the IM and Presence Service deployment. A release
                        mismatch, if it is supported, would let you deploy your Unified Communications Manager telephony deployment and your IM and
                        Presence Service deployment using different releases.

Any respin or ES that is produced between Cisco.com releases is considered part of the previous release. For example, a Unified Communications Manager ES with a build number
                                 of 14.0.1.14[0-2]xx would be considered part of the 14SU4 (14.0.1.14900-x) release.

Deployment Type

Release Mismatch

Description

Standard Deployment of IM and Presence Service

Not supported

Unified Communications Manager and the IM and Presence Service are in the same cluster and must run the same release—a release
                                    mismatch is not supported.

Centralized Deployment of IM and Presence Service

Supported

The IM and Presence Service deployment and the telephony deployment are in different clusters and can run different releases—a
                                    release mismatch is supported.

The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                             This non-telephony node must run the same release as the IM and Presence Service.

## Unified Communications Manager Compatibility Information

### Cisco Collaboration System Applications

This release of Cisco Unified Communications Manager and the IM and Presence Service is a part of the Cisco Collaboration
                        Systems Release 14 and is compatible with the other Cisco Collaboration applications and versions in Cisco Collaboration Systems
                        Release 14.

For a full list of Cisco Collaboration applications that are a part of Cisco Collaboration Systems Release 14, and the supported
                        versions for each, see the Cisco Collaboration Systems Release Compatibility Matrix at: https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/CSR-Compatibility-Matrix-InteractiveHTML.html .

### Android Push Notifications Compatibility Recommendations

Android Push Notification feature is supported from the following software versions:

Unified Communications Manager 12.5(1)SU3

IM and Presence Service 12.5(1)SU3

Cisco Jabber 12.9.1

Cisco Expressway X12.6.2

This compatibility information isn't applicable for Cisco Webex.

Unified Communications Manager and IM and Presence Service Version

Expressway Version

Unified Communications Mobile and Remote Access

On-Premises Deployments

All clusters on:

11.5(1)SU8 or earlier

12.5(1)SU2 or earlier

X12.6.2

Android Push Notification is not supported

Android Push Notification is not supported

All clusters on:

12.5(1)SU3 OR 14 (and higher)

X12.6.2

Enable Android Push Notification using the CLI xConfiguration XCP Config FcmService: On on Expressway for messaging only

Android Push Notification is supported

Cluster with mixed versions [11.5(1)SU8 or earlier, OR 12.5(1)SU2 or earlier, and 12.5(1)SU3 OR 14 (and higher)]

X12.6.2

Android Push Notification for Messaging is not supported

VOIP is supported from Release 12.5(1)SU3 OR 14 (and higher)

Android Push Notification is supported from Release 12.5(1)SU3 OR 14 (and higher)

#### IM and Presence Stream Features/Services Advertisement Compatibility Recommendations

IM and Presence Service supports the advertisement of XMPP stream features/services to the clients connecting over Cisco Expressway's
                        Mobile and Remote Access.

Depending on your current IM and Presence Service version mix, you may need to enable or disable push notifications feature
                        using FCM service flag on the Expressway as per the information given in the following table:

```
xConfiguration XCP Config FcmService: On/Off
```

Apple Push Notification Service (APNS) is not affected by the FCM service flag status.

Mixed Versions IM and Presence Clusters

Expected Status of FCM Flag on Expressway X12.7

Comment

Any 11.5(1)SU with

12.5(1)SU2 and lower

OFF

Android Push (FCM) NOT supported.

11.5(1)SU8 (and lower) OR 12.5(1)SU2 (and lower) with 12.5(1)SU3 OR 14

OFF

Android push (FCM) NOT supported

11.5(1)SU8 (and lower) OR 12.5(1)SU2 (and lower) with 12.5(1)SU4 (and higher) OR 14SU1 (and higher)

OFF

Android push (FCM) supported on 12.5(1)SU4 OR 14 (or newer) versions

11.5(1)SU9 (and higher) OR 12.5(1)SU4 (and higher) with 12.5(1)SU3 OR 14 (and higher)

ON

Android push (FCM) supported on version 12.5(1)SU3 OR 14 (and higher)

11.5(1)SU9 (and higher) with 12.5(1)SU4 (and higher) OR 14SU1 (and higher)

Flag not required

(Expressway 12.7 relies fully on the new discovery mechanism)

Android push (FCM) supported on 12.5(1)SU4 OR 14 (or newer) versions

### Cisco Endpoint Support

All end of Life and End of Sale announcements are listed here: https://www.cisco.com/c/en/us/products/eos-eol-listing.html .

#### Supported Cisco Endpoints

The following table lists Cisco endpoints that are supported with this release of Cisco Unified Communications Manager. For
                        endpoints that have reached End of Sale (EOS), or End of Software Maintenance, click the EOS link to view support details.

Cisco will not issue bug fixes or security enhancements for endpoints that have reached End of Software Maintenance or End
                                    of Support status, regardless of whether those endpoints are deprecated or not deprecated. Cisco will not test Unified Communications
                                    Manager with End of Life phones. Nor will we fix Unified Communications Manager bugs that are related to End of Life phones
                                    unless the issue can be replicated on a phone that is not End of Life.

Device Series

Device Model

Cisco Unified SIP Phone 3900 Series

Cisco Unified SIP Phone 3905

Cisco Unified IP Phone 6900 Series

Cisco Unified IP Phone 6901

Cisco IP Phone 7800 Series

Cisco IP Phone 7811

Cisco IP Phone 7821

Cisco IP Phone 7841

Cisco IP Phone 7861

Cisco IP Conference Phone 7832

Cisco Unified IP Phone 7900 Series

Cisco Unified IP Phone Expansion Module 7915— EOS Notice

Cisco Unified IP Phone Expansion Module 7916— EOS Notice

Cisco Unified IP Phone 7942G— EOS Notice

Cisco Unified IP Phone 7945G— EOS Notice

Cisco Unified IP Phone 7962G— EOS Notice

Cisco Unified IP Phone 7965G— EOS Notice

Cisco Unified IP Phone 7975G— EOS Notice

Cisco IP Phone 8800 Series

Cisco IP Phone 8811, 8831, 8841, 8845, 8851, 8851NR, 8861, 8865, 8865NR

Cisco Wireless IP Phone 8821, 8821-EX— EOL Notice

Cisco Unified IP Conference Phone 8831— EOS Notice

Cisco IP Conference Phone 8832

Cisco Video Phone 8875

Cisco Video Phone 8875NR

Cisco Unified IP Phone 8900 Series

Cisco Unified IP Phone 8945— EOS Notice

Cisco Unified IP Phone 8961— EOS Notice

Cisco Unified IP Phone 9900 Series

Cisco Unified IP Phone 9951— EOS Notice

Cisco Unified IP Phone 9971— EOS Notice

Cisco Desk Phone 9800 Series

Cisco Desk Phone 9811

Cisco Desk Phone 9841

Cisco Desk Phone 9851

Cisco Desk Phone 9861

Cisco Desk Phone 9871

In Unified Communications Manager Release 14 systems running Device Pack 14.0.1.16076-1, the Cisco 9871 phone icon will not
                                                display correctly in the Cisco Unified CM Administration interface.

Cisco Desk Phone 9800 Key Expansion Module (KEM)

Cisco Jabber

Cisco Jabber for Android

Cisco Jabber for iPhone and iPad

Cisco Jabber for Mac

Cisco Jabber for Windows

Cisco Jabber Softphone for VDI - Windows (formerly Cisco Virtualization Experience Media Edition for Windows)

Cisco Jabber Guest

Cisco Jabber Software Development Kit

Cisco Jabber for Tablet

Cisco Headset Series

Cisco Headset 320

Cisco Headset 520

Cisco Headset 530

Cisco Headset 560

Cisco Headset 720

Cisco Headset 730

Cisco IP Communicator

Cisco IP Communicator— EOS Notice

Webex

Webex App

Webex Room Phone

Webex Desk

Cisco Desk Camera 4K

Cisco Desk Camera 1080p

Webex Desk Hub

Webex Desk Pro

Webex Desk Limited Edition

Webex Share— EOS Notice

Board 55, 55S, 70, 70S, 85, 85S

Board Pro 55 G2 and 75 G2

Webex Room Panorama

Webex Room 70 Panorama

Webex Room 70 Panorama Upgrade

Room 70

Room 70 G2

Room 55

Room 55 Dual

Room Kit Pro

Room Kit Plus

Room Kit

Room Kit Mini

Webex Room USB

Webex Wireless Phone 800 Series

Webex Wireless Phone 840

Webex Wireless Phone 860

Webex Meetings

Webex Meetings for iPad and iPhone

Webex Meetings for Android

Cisco Analog Telephony Adapters

Cisco ATA 190 Series Analog Telephone Adapters— EOS/EOL Notice

Cisco ATA 191 Series Analog Telephone Adapters

Cisco DX Series

Cisco Webex DX70— EOS Notice

Cisco Webex DX80— EOS Notice

Cisco DX650— EOS Notice

Cisco TelePresence IX5000

Cisco TelePresence IX5000

Cisco TelePresence EX Series

Cisco TelePresence System EX90— EOS Notice

Cisco TelePresence MX Series

Cisco TelePresence MX200 G2— EOS Notice

Cisco TelePresence MX300 G2— EOS Notice

Cisco TelePresence MX700D— EOS Notice

Cisco TelePresence MX800S— EOS Notice

Cisco TelePresence MX800D— EOS Notice

Cisco TelePresence SX Series

Cisco TelePresence SX10— EOS Notice

Cisco TelePresence SX20— EOS Notice

Cisco TelePresence SX80— EOS Notice

For a list of firmware versions that are used for each Cisco endpoint, see the Cisco Collaboration Systems Release Compatibility Matrix at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/CSR-Compatibility-Matrix.html .

For information about Device Pack compatibility to support the phones, see the Cisco Unified Communications Manager Device Package Compatibility Matrix at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix.html .

#### End of Support

The following table lists Cisco endpoints that have reached the End of Support date, but which are not yet deprecated. Unlike
                        deprecated endpoints, you can still deploy these endpoints in the latest release, but they are not supported actively, are
                        not tested, and may not work.

Click the links to view support announcements for each endpoint.

For information on all of the End of Support and End-of-Life products, see https://www.cisco.com/c/en_ca/products/eos-eol-listing.html .

Cisco Endpoints at End of Support

Cisco Unified SIP Phone 3911 , 3951

Cisco Unified IP Phone 6911 , 6921 , 6941 , 6945 , 6961 , 7906G , 7911G , 7931G , 7940G , 7945 , 7941G , 7960G , 7965 , 7961G , 8941

Cisco Unified IP Phone Expansion Module 7925G , 7925G-EX , 7926G

Cisco Unified IP Conference Station 7935 , 7936 , 7937G

Cisco TelePresence EX60

Cisco TelePresence MX200-G1 , MX200-G2 , MX300-G1 , MX300-G2

Cisco TelePresence 500-32 , 500-37 , 1000 MXP , 1100 , 1300-65 , 1300-47 , 3000 Series

Cisco ATA 190 Series Analog Telephone Adapters

#### Deprecated Phone Models

The following table lists all the phone models that are deprecated for this release of Unified Communications Manager , along with the Unified CM release where the phone model first became deprecated. For example, a phone model that was first
                           deprecated in Release 11.5(1) is deprecated for all later releases, including all 12.x releases.

If you are upgrading to the current release of Unified Communications Manager and you have any of these phone models deployed, the phone will not work after the upgrade.

Deprecated Phone Models for this Release

First Deprecated as of Unified CM...

Cisco Unified Wireless IP Phone 7921

Cisco Unified IP Phone 7970

Cisco Unified IP Phone 7971

12.0(1) and later releases

Cisco IP Phone 12 S

Cisco IP Phone 12 SP

Cisco IP Phone 12 SP+

Cisco IP Phone 30 SP+

Cisco IP Phone 30 VIP

Cisco Unified IP Phone 7902G

Cisco Unified IP Phone 7905G

Cisco Unified IP Phone 7910

Cisco Unified IP Phone 7910G

Cisco Unified IP Phone 7910+SW

Cisco Unified IP Phone 7910G+SW

Cisco Unified IP Phone 7912G

Cisco Unified Wireless IP Phone 7920

Cisco Unified IP Conference Station 7935

11.5(1) and later releases

For additional information refer to the Field Notice: Cisco Unified Communications Manager Release 14 does not support some deprecated phone models at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/trouble/14_0_1/fieldNotices/cucm_b_deprecated-phones-14.html .

##### Upgrades that
                           		  Involve Deprecated Phones

If you are using
                           		  any of these phones on an earlier release and you want to upgrade to this
                           		  release, do the following:

Confirm
                                 				whether the phones in your network will be supported in this release.

Identify any
                                 				non-supported phones.

For any
                                 				non-supported phones, power down the phone and disconnect the phone from the
                                 				network.

Provision a supported phone for the phone user. You can use the following methods to migrate from older model to newer model
                                 phones:

Native Phone Migration using IVR and Phone Services

Migration FX tool

Once all the
                                 				phones in your network are supported by this release, upgrade your system.

Deprecated phones can also be removed after the upgrade. When the administrator logs in to Unified Communications Manager
                                       after completing the upgrade, the system displays a warning message notifying the administrator of the deprecated phones.

##### Licensing

You do not need to purchase a new device license to replace a deprecated phone with a supported phone. The device license
                           becomes available for a new phone when you either remove the deprecated phone from the system, or when you switch to the new Unified Communications Manager version, and the deprecated phone fails to register.

### Virtualization Requirements

This release of Unified Communications Manager and the IM and Presence Service supports virtualized deployments only. Deployments
                        on bare-metal servers are not supported. For more information, see http://www.cisco.com/go/virtualized-collaboration .

See the following table for virtualization requirements.

Virtualization Requirements for...

For information, go to...

Unified Communications Manager and IM and Presence Service

For information on the virtualization requirements, go to the Cisco Virtualization Guide for Cisco On-premises Calling Applications .

Cisco Business Edition Deployments

For information on the virtualization requirements for Unified Communications Manager in a collaboration solution deployment
                                    such as Cisco Business Edition, go to the following:

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html

Cisco Business Edition 7000

Cisco Business Edition 6000

### Supported LDAP Directories

The following LDAP directories are supported:

Microsoft Active Directory on Windows Server 2012 R1/ R2

Microsoft Active Directory on Windows Server 2016

Microsoft Active Directory on Windows Server 2019—Supported for 11.5(1)SU7, 12.5(1)SU2, and later releases

Microsoft Active Directory on Windows Server 2022—Supported for 14SU3 and later releases

Microsoft Lightweight Directory Services 2012 R1/ R2

Microsoft Lightweight Directory Services 2019—Supported for 11.5(1)SU7, 12.5(1)SU2, and later releases

Oracle Directory Services Enterprise Edition 11gR1 (11.1.1.7.x or newer)

Oracle Unified Directory 12cPS3 (12.2.1.3.0)

Open LDAP 2.4.44 or later

Other LDAPv3 Compliant Directories—Unified Communications Manager uses standard LDAPv3 for accessing the user's data. Ensure
                              that the supportedcontrol attribute is configured in the LDAPv3 compliant directory servers to be used with DirSync. (The
                              supportedcontrol attribute may return the pagecontrolsupport and persistentcontrolsupport sub attributes, if configured.)

### Supported Web Browsers

The following web browsers are supported:

Firefox with Windows 11 (64 bit)

Chrome with Windows 11 (64 bit)

Microsoft Edge browser with Windows 11 (64 bit)

Chrome, Firefox, and Safari with MacOS (15.5)

We recommend that you use the latest version for all the web browsers supported.

### SFTP Server Support

For internal testing, we use the SFTP Server on Cisco Prime Collaboration Deployment (PCD) which is provided by Cisco, and
                        which is supported by Cisco TAC. Refer to the following table for a summary of the SFTP server options:

SFTP Server

Support Description

SFTP Server on Cisco Prime Collaboration Deployment

This server is the only SFTP server that is provided and tested by Cisco, and fully supported by Cisco TAC.

Version compatibility depends on your version of Unified Communications Manager and Cisco Prime Collaboration Deployment.
                                    See the Cisco Prime Collaboration Deployment Administration Guide before you upgrade its version (SFTP) or Unified Communications Manager to ensure that the versions are compatible.

SFTP Server from a Technology Partner

These SFTP servers from a technology partner are third-party provided and third-party tested. Version compatibility depends
                                    on the third party test. See the Technology Partner page if you upgrade their SFTP product and/or upgrade Unified Communications
                                    Manager for which versions are compatible.

SFTP Server from another Third Party

These SFTP servers are provided by a third party and are not officially supported by Cisco TAC.

Version compatibility is on a best effort basis to establish compatible SFTP versions and Unified Communications Manager versions.

These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                             For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner.

### SAML SSO Support

Although Cisco Collaboration infrastructure may prove to be compatible with other IdPs claiming SAML 2.0 compliance, only
                        the following IdPs have been tested with Cisco Collaboration solutions:

Microsoft ® Active Directory ® Federation Services 2.0 , 3.0, 4.0, and 5.0

Microsoft Entra ID

Okta 2017.38

OpenAM 10.0.1

PingFederate ® 6.10.0.4

F5 BIG-IP 11.6.0

For additional information on SAML SSO, see the SAML SSO Deployment Guide for Cisco Unified Communications Applications .

### API and Secure Connection Packages

The following table provides information on the API Development and secure connection packages that are supported with this
                        release.

Package Type

Details

API Development

Cisco Unified Communications Manager and the IM and Presence Service support OpenJDK for application development.

Release 14 use OpenJDK version 1.8.0.262.

Release 14SU1 use OpenJDK version 1.8.0.262.b10-0.

Release 14SU2 of Unified CM and Release 14SU2a of IM and Presence Service use OpenJDK version 1.8.0.262.b10-0.

Release 14SU3 use OpenJDK version 1.8.0.332.b09-1.

Release 14SU4 use OpenJDK version 1.8.0.372.b07-1.

Release 14SU5 use OpenJDK version 1.8.0.372.b07-1.

Release 14SU6 use OpenJDK version 1.8.0.372.b07-1.

SSL Connections

For Secure Sockets Layer (SSL) connections, these releases support either OpenSSL or Cisco SSL. You can use either of the
                                    following for your respective versions:

Release 14 uses OpenSSL 1.0.2u.6.2.374 and CiscoSSL 1.0.2u.6.2.374.

Release 14SU1 uses OpenSSL  1.0.2y.6.2.403 and CiscoSSL  1.0.2y.6.2.403.

Release 14SU2 of Unified CM and Release 14SU2a of IM and Presence Service uses OpenSSL 1.0.2zd.6.2.480 and CiscoSSL 1.1.1n.7.2.390.

Release 14SU3 uses OpenSSL 1.0.2zd.6.2.480 and CiscoSSL 1.1.1n.7.2.390.

Release 14SU4 uses OpenSSL 1.0.2zd.6.2.480 and CiscoSSL 1.1.1w.7.2.555.

Release 14SU5 uses OpenSSL 1.0.2zd.6.2.480 and CiscoSSL 1.1.1v.7.2.539.

Release 14SU6 uses OpenSSL 1.0.2zd.6.2.480 and CiscoSSL 1.1.1v.7.2.539.

SSH Clients

Release 14 supports OpenSSH client version 7.5.14i.1.5.18 for SSH connections.

Release 14SU1 supports OpenSSH client version  7.5.14i.1.5.18 for SSH connections.

Release 14SU2 of Unified CM and Release 14SU2a of IM and Presence Service supports CiscoSSH client version 1.9.29.18 for SSH
                                          connections.

Release 14SU3 supports OpenSSH client version 1.9.29.18 for SSH connections.

Release 14SU4 supports OpenSSH client version 1.11.34.3 for SSH connections.

Release 14SU5 supports OpenSSH client version 1.13.48.11 for SSH connections.

Release 14SU6 supports OpenSSH client version 1.13.48.11 for SSH connections.

For additional information on the packages that are installed on your system, run the show packages active CLI command. See the Command Line Interface Reference Guide for Cisco Unified Communications Solutions for more information about this command and its options.

#### TLS 1.2 Support

Unified Communications Manager and the IM and Presence Service support the use of TLS 1.2. For detailed information on TLS
                        1.2 support, see the TLS 1.2 Compatibility Matrix for Cisco Collaboration Products .

### Supported Ciphers for Unified Communications Manager

The following ciphers are supported by Unified Communications Manager:

Application / Process

Protocol

Port

Supported Ciphers

Cisco CallManager

TCP / TLS

2443

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
AES256-GCM-SHA384:
AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
AES128-GCM-SHA256:
AES128-SHA256:AES128-SHA: ECDHE-RSA-AES256-SHA:
```

DRS

TCP / TLS

4040

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
AES256-GCM-SHA384:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
AES128-GCM-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Cisco Tomcat

TCP / TLS

8443 / 443

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
DHE-RSA-AES256-GCM-SHA384:
DHE-RSA-AES256-SHA256:
DHE-RSA-AES256-SHA:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
DHE-RSA-AES128-GCM-SHA256:
DHE-RSA-AES128-SHA256:
DHE-RSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: 
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Cisco CallManager

TCP / TLS

5061

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384 
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384: 
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA 
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Cisco Certificate Authority Proxy Function

TCP / TLS

3804

```
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA
```

CTIManager

TCP / TLS

2749

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Cisco Trust Verification Service

TCP / TLS

2445

```
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256
```

Cisco Intercluster Lookup Service

TCP / TLS

7501

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
AES256-GCM-SHA384:
AES256-SHA256:AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Secure Configuration download (HAPROXY)

TCP / TLS

6971, 6972

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Authenticated Contact Search

TCP / TLS

9443

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA: ECDHE-RSA-AES256-SHA:
```

### Supported Ciphers for SSH

The following ciphers are supported by SSH:

Service

Ciphers/Algorithms

SSH Server

Ciphers

```
aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com
```

MAC algorithms:

```
hmac-sha2-256
hmac-sha2-512
hmac-sha1
```

Kex algorithms:

```
ecdh-sha2-nistp521
ecdh-sha2-nistp384
ecdh-sha2-nistp256
diffie-hellman-group14-sha1
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512
```

Host Key algorithms in non-FIPS mode:

```
rsa-sha2-256
rsa-sha2-512
ssh-rsa
```

Host Key algorithms in FIPS mode:

```
rsa-sha2-256
rsa-sha2-512
```

SSH Client

Ciphers:

```
aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com
```

MAC algorithms:

```
hmac-sha2-256
hmac-sha2-512
hmac-sha1
```

Kex algorithms:

```
ecdh-sha2-nistp521
ecdh-sha2-nistp384
ecdh-sha2-nistp256
diffie-hellman-group14-sha1
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512
```

Host Key algorithms in non-FIPS mode:

```
rsa-sha2-256
rsa-sha2-512
ssh-rsa
```

Host Key algorithms in FIPS mode:

```
rsa-sha2-256
rsa-sha2-512
```

DRS Client

Ciphers:

```
aes256-ctr
aes128-ctr
aes192-ctr
```

MAC algorithms:

```
hmac-sha2-256
hmac-sha1
```

```
ecdh-sha2-nistp256
ecdh-sha2-nistp384
ecdh-sha2-nistp521
diffie-hellman-group14-sha1
```

The Kex algorithms diffie-hellman-group-exchange-sha256, diffie-hellman-group-exchange-sha1, and diffie-hellman-group1-sha1
                                                   are not supported from Release 12.5(1)SU4 if you have configured Cipher Management functionality in your Unified CM server.
                                                   If the ciphers are not configured, DRS Client uses these algorithms.

SFTP client

Ciphers:

```
aes128-ctr
aes192-ctr 
aes256-ctr
```

MAC algorithms:

```
hmac-sha2-256 
hmac-sha1
```

Kex algorithms:

```
ecdh-sha2-nistp521 
ecdh-sha2-nistp384 
diffie-hellman-group14-sha1 
diffie-hellman-group1-sha1 
diffie-hellman-group-exchange-sha256 
diffie-hellman-group-exchange-sha1
```

End Users

```
hmac-sha512
```

```
SHA-512 – Hashing (salted)
```

DRS Backups / RTMT SFTPs

```
AES-128 – Encryption
```

Application Users

```
AES-256 – Encryption
```

## IM and Presence Service Compatibility Information

### Platform Compatibility

The IM and Presence Service shares a platform with Unified Communications Manager. Many of the compatibility topics for Unified
                        Communications Manager double as support topics for the IM and Presence Service. You can refer to the Unified Communications
                        Manager compatibility chapter for information on the following items:

Secure Connections

Virtualization Requirements

Supported LDAP Directories

Supported Web Browsers

### External Database Support

Many IM and Presence Service features such as Persistent Chat, High Availability for Persistent Chat, Message Archiver, and
                        Managed File Transfer require that you deploy an external database. For information on database support, see the Database Setup Guide for the IM and Presence Service .

### Federation Support

#### SIP Federation/SIP Open Federation Support

Cisco IM and Presence Service supports real-time communication between enterprises that use SIP/SIMPLE standards to deliver
                        instant messaging and presence information. Current IM and Presence Service releases offer backward compatibility with retired
                        Microsoft SIP/SIMPLE-based on-premises communication platforms.

#### Supported XMPP Federations

This release of IM and Presence Service supports XMPP Federation with the following systems:

Cisco Webex Messenger

IM and Presence Service Release 14

Any other XMPP-compliant system

### Intercluster Peering Support

This release of the IM and Presence Service supports intercluster peering with the following IM and Presence Service releases:

Release 14 and SUs

### Calendar Integration with Microsoft Outlook

The IM and Presence Service supports Microsoft Outlook Calendar integration with both on-premises Exchange Server and cloud-hosted
                        Exchange Online. For details on supported configurations, see the following table below:

Component

Install Compatible Version

Calendar Server

Exchange Server Subscription Edition (SE)

Exchange Online in Microsoft 365 (formerly Office 365)

Certificate Server

Built-in Microsoft Certificate Server in Windows Server

Third-party CA servers

Microsoft Exchange integration with IM and Presence Service supports certificates using RSA 1024 or 2048 bit keys and SHA1
                                                and SHA256 signature algorithms.

### Remote Call Control with Microsoft Lync

Microsoft
                        		  Remote Call Control (RCC) allows enterprise users to control their Cisco Unified IP
                           			 Phone or Cisco IP
                           			 Communicator Phone through Microsoft Lync, a third-party desktop
                        		  instant-messaging (IM) application. When a user signs in to the Microsoft Lync
                        		  client, the Lync server sends instructions, through the IM and Presence
                           			 Service node, to the Cisco Unified Communications
                           			 Manager to set up, tear down and maintain calling features based on a
                        		  user's action at the Lync client.

SIP federation and Remote Call Control (RCC) do not work together on
                                    			 the same IM and Presence Service cluster. This is because for SIP federation a
                                    			 user cannot be licensed for both Cisco IM and Presence Service and Microsoft
                                    			 Lync/OCS, but for RCC a user must be licensed for Cisco IM and Presence Service
                                    			 and Microsoft Lync/OCS at the same time.

An IM and Presence Service cluster that is used for RCC does not support Jabber or other IM and Presence Service functionality.

#### Software Requirements

The
                        		  following software is required for integrating IM and Presence Service with Microsoft Lync Server :

IM and Presence Service , current release

IM and Presence Service Lync Remote Call
                              				Control Plug-in

Cisco Unified Communications Manager , current release

(Optional) Upgraded Skype for Business 2015 Client

(Optional) Cisco CSS 11500 Content
                                 				  Services Switch

Microsoft Domain
                              				Controller

Microsoft Active
                              				Directory

DNS

Certificate
                              				Authority

#### Configuration

For additional details, including configuration information, see Remote Call Control with Microsoft Lync Server for the IM and Presence Service at https://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-installation-and-configuration-guides-list.html .

### Supported Ciphers for the IM and Presence Service

IM and Presence Service supports the following ciphers:

Application / Process

Protocol

Port

Supported Ciphers

Cisco SIP Proxy

TCP / TLS

5061

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:
AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Cisco SIP Proxy

TCP / TLS

5062

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:
AES256-SHA256:AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Cisco SIP Proxy

TCP / TLS

8083

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Cisco Tomcat

TCP / TLS

8443, 443

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
DHE-RSA-AES256-GCM-SHA384:
DHE-RSA-AES256-SHA256:
DHE-RSA-AES256-SHA:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
DHE-RSA-AES128-GCM-SHA256:
DHE-RSA-AES128-SHA256:
DHE-RSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: 
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA: ECDHE-RSA-AES256-SHA:
```

Cisco XCP XMPP Federation Connection Manager

TCP /TLS

5269

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:
```

Cisco XCP Client Connection Manager

TCP / TLS

5222

```
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:
```

| Date | Revision |
|---|---|
| March 18, 2026 | Initial guide publication for 14SU6. |
| March 18, 2026 | Updated version support for 14SU6. |
| March 18, 2026 | Added support for Cisco Desk Phone 9811. |
| March 18, 2026 | Updated API and Secure Connection Packages information. |
| December 02, 2025 | Updated the "Calendar Integration with Microsoft Outlook" section to include support for Exchange Server Subscription Edition
                              (SE). |
| October 14, 2025 | Initial guide publication for 14SU5. |
| October 14, 2025 | Updated version support for 14SU5. |
| October 14, 2025 | Updated Web Browsers supported. |
| October 14, 2025 | Updated ciphers list for Unified CM and IM and Presence Service. |
| October 14, 2025 | Removed support for Active Directory 2016 with Windows Server 2016 from the "Calendar Integration with Microsoft Outlook"
                              section. |
| March 17, 2025 | Added support for Cisco Board Pro 55 G2 and Cisco Board Pro 75 G2 from Release 14SU4 onwards. |
| June 10, 2024 | Updated support version for Unified CM Release 14SU4a. |
| May 30, 2024 | Initial guide publication for 14SU4. |
| May 30, 2024 | Updated version support for 14SU4. |
| May 30, 2024 | Added support for Cisco Desk Phone 9800 Series. |
| May 30, 2024 | Updated ciphers list for Unified CM. |
| May 30, 2024 | Removed 'Active Directory 2012 with Windows Server 2012' support from Calendar Integration with Microsoft Outlook section. |
| July 03, 2023 | Removed Intercluster Peering Support for IM and Presence Service Release 10.x. |
| May 18, 2023 | Initial guide publication for 14SU3. |
| May 18, 2023 | Updated version support for 14SU3. |
| May 18, 2023 | Added support for Cisco Video Phone 8875. |
| May 18, 2023 | Updated ciphers list for Unified CM and IM and Presence Service. |
| May 18, 2023 | Added support for Microsoft Active Directory on Windows Server 2022. |
| May 18, 2023 | Added support for Cisco Headset 320 Series and Cisco Headset 720 Series. |
| June 16, 2022 | Initial guide publication for 14SU2. |
| June 16, 2022 | Updated version support for 14SU2. |
| June 16, 2022 | Webex Desk Camera is rebranded to Cisco Desk Camera 4K. |
| June 16, 2022 | Added support for Cisco Desk Camera 1080p. |
| July 05, 2022 | Updated Unified IM and Presence Service release version support to 14SU2a. |
| October 27, 2021 | Initial guide publication for 14SU1. |
| October 27, 2021 | Changed title of the guide to 14x. |
| October 27, 2021 | Updated upgrade paths and version support for 14SU1. |
| March 31, 2021 | Initial guide publication for 14. |
| April 28, 2021 | Added support for Ciphers for Application and OS End Users. |

| Note | Unless indicated otherwise, each release category includes the SU releases within that category. |
|---|---|

| Note | Although it is not mandatory, we strongly recommend that you run the Upgrade Readiness COP file prior to the upgrade in order
                              to maximize upgrade success. Cisco TAC may require that you run this COP file to provide effective technical support. |
|---|---|

| Note | If the source is in FIPS mode and/or PCD in FIPS mode, see https://www.cisco.com/web/software/286319173/139477/ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop-ReadMe.pdf for information on the COP file ciscocm.ciscossl7_upgrade_CSCwa48315_CSCwa77974_v1.0.k4.cop . This document details the pre-requisites required for direct upgrade or direct migration to the 14SU2 destination versions. |
|---|---|

| Note | If the source is Release 14 or above and the upgrade path is direct standard, see the "Clusterwide Upgrade Task Flow (Direct
                                 Standard)" procedure that details Cluster Upgrade via Unified CM publisher using Unified OS Admin upgrade or CLI upgrade that
                                 will upgrade all cluster nodes in the Unified CM publisher node. If you are planning to upgrade your source node-by-node or using a single-node only using the local Unified OS Admin upgrade
                                 or CLI upgrade, see the "Upgrade Cluster Nodes (Direct Refresh or Direct Standard" section. For more information on the procedures, see the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service . |
|---|---|

| Source | Destination | Mechanism | Pre-requisites | Version Switching* (Source to Destination and Vice Versa) |
|---|---|---|---|---|
| 11.5 | 14 | Direct Refresh Upgrade | Via OS Admin or CLI | Run pre-upgrade-check COP file. If the Unified CM source is older than 11.5.1.22900-28, then install the following COP file: cop ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn. If the IM and Presence Service source is older than 11.5.1.22900-6, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn. If you want to upgrade IM and Presence Service from release 11.5.1.18900-15 to 14, use the following COP file: ciscocm.V11.5.1_CSCvv25961_add_diffie_C0085-1.cop.sgn. | Supported |
| Direct Refresh Upgrade | Via PCD Upgrade Task | Run pre-upgrade-check COP file. If the Unified CM source is older than 11.5.1.22900-28, then install the following COP file: cop ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn. If the IM and Presence Service source is older than 11.5.1.22900-6, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn. If you want to upgrade IM and Presence Service from release 11.5.1.18900-15 to 14, use the following COP file: ciscocm.V11.5.1_CSCvv25961_add_diffie_C0085-1.cop.sgn. If the destination version is 14 SU2 or above and the source version 11.5 is in FIPS mode, then either: PCD must be in (or placed in) non-FIPS mode. Use Fresh Install with Data Import instead of using the PCD Upgrade Task. | Supported |
| PCD 14 Migration Task (V2V) | Run pre-upgrade-check COP file. If the destination version is 14 SU2 or above and the source version 11.5 is in FIPS mode, then either: PCD must be in (or placed in) non-FIPS mode. Use Fresh Install with Data Import instead of using the PCD Migration Task. | Not supported |
| Fresh Install with Data Import (V2V) | Run pre-upgrade-check COP file. ciscocm.DataExport_v1.0.cop.sgn | Not supported |
| 12.0 | 14 | Direct Refresh Upgrade | Via OS Admin or CLI | Run pre-upgrade-check COP file. If the Unified CM source is older than 12.0.1.24900-19, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn. If the IM and Presence Service source is older than 12.0.1.21000-34, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn. | Supported |
| Direct Refresh Upgrade | Via PCD Upgrade Task | Run pre-upgrade-check COP file. If the Unified CM source is older than 12.0.1.24900-19, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn. If the IM and Presence Service source is older than 12.0.1.21000-34, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn. | Supported |
| PCD 14 Migration Task (V2V) | Run pre-upgrade-check COP file. If the source version is Release 12.0(1) of Unified Communications Manager (12.0.1.10000-10), then you must install the following
                                 COP file: ciscocm-slm-migration.k3.cop.sgn. This is not required if the source version is higher, for example, Release 12.0(1)SU1. | Not supported |
| Fresh Install with Data Import (V2V) | Run pre-upgrade-check COP file. ciscocm.DataExport_v1.0.cop.sgn | Not supported |
| 12.5 | 14 | Direct Standard Upgrade (simple upgrades) | Via OS Admin or CLI | Run pre-upgrade-check COP file. If the Unified CM source is older than 12.5.1.14900-63, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn. If the IM and Presence Service source is older than 12.5.1.14900-4, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn. | Supported |
| Direct Standard Upgrade | Via PCD Upgrade Task | Run pre-upgrade-check COP file. If the Unified CM source is older than 12.5.1.14900-63, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn. If the IM and Presence Service source is older than 12.5.1.14900-4, then install the following COP file: ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn. If the destination version is 14 SU2 or above and the source version 12.5 is in FIPS mode, then either: PCD must be in (or placed in) non-FIPS mode. Use Fresh Install with Data Import instead of using the PCD Upgrade Task. | Supported |
| PCD 14 Migration Task (V2V) | Run pre-upgrade-check COP file. If the destination version is 14 SU2 or above and the source version 12.5 is in FIPS mode, then either: PCD must be in (or placed in) non-FIPS mode. Use Fresh Install with Data Import instead of using the PCD Migration Task. | Not supported |
| Fresh Install with Data Import (V2V) | Run pre-upgrade-check COP file. ciscocm.DataExport_v1.0.cop.sgn | Not supported |
| 14 or 14SU1 | 14SU2 and later | Direct Standard Upgrade (simple upgrades) | Via OS Admin or CLI | Run pre-upgrade-check COP file. | Supported |
| Direct Standard Upgrade | Via PCD Upgrade Task | Run pre-upgrade-check COP file. If the destination version is 14 SU2 or above and the source version is 14 or 14SU1 in FIPS mode, then either: PCD must be in (or placed in) non-FIPS mode. Use Fresh Install with Data Import instead of using the PCD Upgrade Task. |

| Note | PCD Upgrades and Migrations—Use Cisco Prime Collaboration Deployment Release 14SU2 for all PCD tasks. |
|---|---|

| For this Release... | The Following Versions are Supported... |
|---|---|
| 14 | Cisco Unified Communications Manager 14.0.1.10000-20 IM and Presence Service 14.0.1.10000-16 |
| 14SU1 | Cisco Unified Communications Manager 14.0.1.11900-132 IM and Presence Service 14.0.1.11900-9 |
| 14SU2 | Cisco Unified Communications Manager 14.0.1.12900-161 |
| 14SU2a | IM and Presence Service 14.0.1.12901-1 |
| 14SU3 | Cisco Unified Communications Manager 14.0.1.13900-155 IM and Presence Service 14.0.1.13900-8 |
| 14SU4 | Cisco Unified Communications Manager 14.0.1.14901-1 IM and Presence Service 14.0.1.14900-4 |
| 14SU5 | Cisco Unified Communications Manager 14.0.1.15900-24 IM and Presence Service 14.0.15900-3 |
| 14SU6 | Cisco Unified Communications Manager 14.0.1.16900-4 IM and Presence Service 14.0.16900-3 |

| Note | Any respin or ES that is produced between Cisco.com releases is considered part of the previous release. For example, a Unified Communications Manager ES with a build number
                                 of 14.0.1.14[0-2]xx would be considered part of the 14SU4 (14.0.1.14900-x) release. |
|---|---|

| Deployment Type | Release Mismatch | Description |
|---|---|---|
| Standard Deployment of IM and Presence Service | Not supported | Unified Communications Manager and the IM and Presence Service are in the same cluster and must run the same release—a release
                                    mismatch is not supported. |
| Centralized Deployment of IM and Presence Service | Supported | The IM and Presence Service deployment and the telephony deployment are in different clusters and can run different releases—a
                                    release mismatch is supported. Note The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                             This non-telephony node must run the same release as the IM and Presence Service. | Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                             This non-telephony node must run the same release as the IM and Presence Service. |
| Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                             This non-telephony node must run the same release as the IM and Presence Service. |

| Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                             This non-telephony node must run the same release as the IM and Presence Service. |
|---|---|

| Note | This compatibility information isn't applicable for Cisco Webex. |
|---|---|

| Unified Communications Manager and IM and Presence Service Version | Expressway Version | Unified Communications Mobile and Remote Access | On-Premises Deployments |
|---|---|---|---|
| All clusters on: 11.5(1)SU8 or earlier 12.5(1)SU2 or earlier | X12.6.2 | Android Push Notification is not supported | Android Push Notification is not supported |
| All clusters on: 12.5(1)SU3 OR 14 (and higher) | X12.6.2 | Enable Android Push Notification using the CLI xConfiguration XCP Config FcmService: On on Expressway for messaging only | Android Push Notification is supported |
| Cluster with mixed versions [11.5(1)SU8 or earlier, OR 12.5(1)SU2 or earlier, and 12.5(1)SU3 OR 14 (and higher)] | X12.6.2 | Android Push Notification for Messaging is not supported VOIP is supported from Release 12.5(1)SU3 OR 14 (and higher) | Android Push Notification is supported from Release 12.5(1)SU3 OR 14 (and higher) |

| Note | Apple Push Notification Service (APNS) is not affected by the FCM service flag status. |
|---|---|

| Mixed Versions IM and Presence Clusters | Expected Status of FCM Flag on Expressway X12.7 | Comment |
|---|---|---|
| Any 11.5(1)SU with 12.5(1)SU2 and lower | OFF | Android Push (FCM) NOT supported. |
| 11.5(1)SU8 (and lower) OR 12.5(1)SU2 (and lower) with 12.5(1)SU3 OR 14 | OFF | Android push (FCM) NOT supported |
| 11.5(1)SU8 (and lower) OR 12.5(1)SU2 (and lower) with 12.5(1)SU4 (and higher) OR 14SU1 (and higher) | OFF | Android push (FCM) supported on 12.5(1)SU4 OR 14 (or newer) versions |
| 11.5(1)SU9 (and higher) OR 12.5(1)SU4 (and higher) with 12.5(1)SU3 OR 14 (and higher) | ON | Android push (FCM) supported on version 12.5(1)SU3 OR 14 (and higher) |
| 11.5(1)SU9 (and higher) with 12.5(1)SU4 (and higher) OR 14SU1 (and higher) | Flag not required (Expressway 12.7 relies fully on the new discovery mechanism) | Android push (FCM) supported on 12.5(1)SU4 OR 14 (or newer) versions |

| Note | Cisco will not issue bug fixes or security enhancements for endpoints that have reached End of Software Maintenance or End
                                    of Support status, regardless of whether those endpoints are deprecated or not deprecated. Cisco will not test Unified Communications
                                    Manager with End of Life phones. Nor will we fix Unified Communications Manager bugs that are related to End of Life phones
                                    unless the issue can be replicated on a phone that is not End of Life. |
|---|---|

| Device Series | Device Model |
|---|---|
| Cisco Unified SIP Phone 3900 Series | Cisco Unified SIP Phone 3905 |
| Cisco Unified IP Phone 6900 Series | Cisco Unified IP Phone 6901 |
| Cisco IP Phone 7800 Series | Cisco IP Phone 7811 Cisco IP Phone 7821 Cisco IP Phone 7841 Cisco IP Phone 7861 Cisco IP Conference Phone 7832 |
| Cisco Unified IP Phone 7900 Series | Cisco Unified IP Phone Expansion Module 7915— EOS Notice Cisco Unified IP Phone Expansion Module 7916— EOS Notice Cisco Unified IP Phone 7942G— EOS Notice Cisco Unified IP Phone 7945G— EOS Notice Cisco Unified IP Phone 7962G— EOS Notice Cisco Unified IP Phone 7965G— EOS Notice Cisco Unified IP Phone 7975G— EOS Notice |
| Cisco IP Phone 8800 Series | Cisco IP Phone 8811, 8831, 8841, 8845, 8851, 8851NR, 8861, 8865, 8865NR Cisco Wireless IP Phone 8821, 8821-EX— EOL Notice Cisco Unified IP Conference Phone 8831— EOS Notice Cisco IP Conference Phone 8832 Cisco Video Phone 8875 Cisco Video Phone 8875NR |
| Cisco Unified IP Phone 8900 Series | Cisco Unified IP Phone 8945— EOS Notice Cisco Unified IP Phone 8961— EOS Notice |
| Cisco Unified IP Phone 9900 Series | Cisco Unified IP Phone 9951— EOS Notice Cisco Unified IP Phone 9971— EOS Notice |
| Cisco Desk Phone 9800 Series | Cisco Desk Phone 9811 Cisco Desk Phone 9841 Cisco Desk Phone 9851 Cisco Desk Phone 9861 Cisco Desk Phone 9871 Note In Unified Communications Manager Release 14 systems running Device Pack 14.0.1.16076-1, the Cisco 9871 phone icon will not
                                                display correctly in the Cisco Unified CM Administration interface. Cisco Desk Phone 9800 Key Expansion Module (KEM) | Note | In Unified Communications Manager Release 14 systems running Device Pack 14.0.1.16076-1, the Cisco 9871 phone icon will not
                                                display correctly in the Cisco Unified CM Administration interface. |
| Note | In Unified Communications Manager Release 14 systems running Device Pack 14.0.1.16076-1, the Cisco 9871 phone icon will not
                                                display correctly in the Cisco Unified CM Administration interface. |
| Cisco Jabber | Cisco Jabber for Android Cisco Jabber for iPhone and iPad Cisco Jabber for Mac Cisco Jabber for Windows Cisco Jabber Softphone for VDI - Windows (formerly Cisco Virtualization Experience Media Edition for Windows) Cisco Jabber Guest Cisco Jabber Software Development Kit Cisco Jabber for Tablet |
| Cisco Headset Series | Cisco Headset 320 Cisco Headset 520 Cisco Headset 530 Cisco Headset 560 Cisco Headset 720 Cisco Headset 730 |
| Cisco IP Communicator | Cisco IP Communicator— EOS Notice |
| Webex | Webex App Webex Room Phone Webex Desk Cisco Desk Camera 4K Cisco Desk Camera 1080p Webex Desk Hub Webex Desk Pro Webex Desk Limited Edition Webex Share— EOS Notice Board 55, 55S, 70, 70S, 85, 85S Board Pro 55 G2 and 75 G2 Webex Room Panorama Webex Room 70 Panorama Webex Room 70 Panorama Upgrade Room 70 Room 70 G2 Room 55 Room 55 Dual Room Kit Pro Room Kit Plus Room Kit Room Kit Mini Webex Room USB |
| Webex Wireless Phone 800 Series | Webex Wireless Phone 840 Webex Wireless Phone 860 |
| Webex Meetings | Webex Meetings for iPad and iPhone Webex Meetings for Android |
| Cisco Analog Telephony Adapters | Cisco ATA 190 Series Analog Telephone Adapters— EOS/EOL Notice Cisco ATA 191 Series Analog Telephone Adapters |
| Cisco DX Series | Cisco Webex DX70— EOS Notice Cisco Webex DX80— EOS Notice Cisco DX650— EOS Notice |
| Cisco TelePresence IX5000 | Cisco TelePresence IX5000 |
| Cisco TelePresence EX Series | Cisco TelePresence System EX90— EOS Notice |
| Cisco TelePresence MX Series | Cisco TelePresence MX200 G2— EOS Notice Cisco TelePresence MX300 G2— EOS Notice Cisco TelePresence MX700D— EOS Notice Cisco TelePresence MX800S— EOS Notice Cisco TelePresence MX800D— EOS Notice |
| Cisco TelePresence SX Series | Cisco TelePresence SX10— EOS Notice Cisco TelePresence SX20— EOS Notice Cisco TelePresence SX80— EOS Notice |

| Note | In Unified Communications Manager Release 14 systems running Device Pack 14.0.1.16076-1, the Cisco 9871 phone icon will not
                                                display correctly in the Cisco Unified CM Administration interface. |
|---|---|

| Cisco Endpoints at End of Support |
|---|
| Cisco Unified SIP Phone 3911 , 3951 Cisco Unified IP Phone 6911 , 6921 , 6941 , 6945 , 6961 , 7906G , 7911G , 7931G , 7940G , 7945 , 7941G , 7960G , 7965 , 7961G , 8941 Cisco Unified IP Phone Expansion Module 7925G , 7925G-EX , 7926G Cisco Unified IP Conference Station 7935 , 7936 , 7937G Cisco TelePresence EX60 Cisco TelePresence MX200-G1 , MX200-G2 , MX300-G1 , MX300-G2 Cisco TelePresence 500-32 , 500-37 , 1000 MXP , 1100 , 1300-65 , 1300-47 , 3000 Series Cisco ATA 190 Series Analog Telephone Adapters |

| Deprecated Phone Models for this Release | First Deprecated as of Unified CM... |
|---|---|
| Cisco Unified Wireless IP Phone 7921 Cisco Unified IP Phone 7970 Cisco Unified IP Phone 7971 | 12.0(1) and later releases |
| Cisco IP Phone 12 S Cisco IP Phone 12 SP Cisco IP Phone 12 SP+ Cisco IP Phone 30 SP+ Cisco IP Phone 30 VIP Cisco Unified IP Phone 7902G Cisco Unified IP Phone 7905G Cisco Unified IP Phone 7910 Cisco Unified IP Phone 7910G Cisco Unified IP Phone 7910+SW Cisco Unified IP Phone 7910G+SW Cisco Unified IP Phone 7912G Cisco Unified Wireless IP Phone 7920 Cisco Unified IP Conference Station 7935 | 11.5(1) and later releases |

| Note | Deprecated phones can also be removed after the upgrade. When the administrator logs in to Unified Communications Manager
                                       after completing the upgrade, the system displays a warning message notifying the administrator of the deprecated phones. |
|---|---|

| Virtualization Requirements for... | For information, go to... |
|---|---|
| Unified Communications Manager and IM and Presence Service | For information on the virtualization requirements, go to the Cisco Virtualization Guide for Cisco On-premises Calling Applications . |
| Cisco Business Edition Deployments | For information on the virtualization requirements for Unified Communications Manager in a collaboration solution deployment
                                    such as Cisco Business Edition, go to the following: https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html Cisco Business Edition 7000 Cisco Business Edition 6000 |

| Note | We recommend that you use the latest version for all the web browsers supported. |
|---|---|

| SFTP Server | Support Description |
|---|---|
| SFTP Server on Cisco Prime Collaboration Deployment | This server is the only SFTP server that is provided and tested by Cisco, and fully supported by Cisco TAC. Version compatibility depends on your version of Unified Communications Manager and Cisco Prime Collaboration Deployment.
                                    See the Cisco Prime Collaboration Deployment Administration Guide before you upgrade its version (SFTP) or Unified Communications Manager to ensure that the versions are compatible. |
| SFTP Server from a Technology Partner | These SFTP servers from a technology partner are third-party provided and third-party tested. Version compatibility depends
                                    on the third party test. See the Technology Partner page if you upgrade their SFTP product and/or upgrade Unified Communications
                                    Manager for which versions are compatible. |
| SFTP Server from another Third Party | These SFTP servers are provided by a third party and are not officially supported by Cisco TAC. Version compatibility is on a best effort basis to establish compatible SFTP versions and Unified Communications Manager versions. Note These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                             For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. | Note | These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                             For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. |
| Note | These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                             For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. |

| Note | These products have not been tested by Cisco and we cannot guarantee functionality. Cisco TAC does not support these products.
                                             For a fully tested and supported SFTP solution, use Cisco Prime Collaboration Deployment or a Technology Partner. |
|---|---|

| Package Type | Details |
|---|---|
| API Development | Cisco Unified Communications Manager and the IM and Presence Service support OpenJDK for application development. Release 14 use OpenJDK version 1.8.0.262. Release 14SU1 use OpenJDK version 1.8.0.262.b10-0. Release 14SU2 of Unified CM and Release 14SU2a of IM and Presence Service use OpenJDK version 1.8.0.262.b10-0. Release 14SU3 use OpenJDK version 1.8.0.332.b09-1. Release 14SU4 use OpenJDK version 1.8.0.372.b07-1. Release 14SU5 use OpenJDK version 1.8.0.372.b07-1. Release 14SU6 use OpenJDK version 1.8.0.372.b07-1. |
| SSL Connections | For Secure Sockets Layer (SSL) connections, these releases support either OpenSSL or Cisco SSL. You can use either of the
                                    following for your respective versions: Release 14 uses OpenSSL 1.0.2u.6.2.374 and CiscoSSL 1.0.2u.6.2.374. Release 14SU1 uses OpenSSL  1.0.2y.6.2.403 and CiscoSSL  1.0.2y.6.2.403. Release 14SU2 of Unified CM and Release 14SU2a of IM and Presence Service uses OpenSSL 1.0.2zd.6.2.480 and CiscoSSL 1.1.1n.7.2.390. Release 14SU3 uses OpenSSL 1.0.2zd.6.2.480 and CiscoSSL 1.1.1n.7.2.390. Release 14SU4 uses OpenSSL 1.0.2zd.6.2.480 and CiscoSSL 1.1.1w.7.2.555. Release 14SU5 uses OpenSSL 1.0.2zd.6.2.480 and CiscoSSL 1.1.1v.7.2.539. Release 14SU6 uses OpenSSL 1.0.2zd.6.2.480 and CiscoSSL 1.1.1v.7.2.539. |
| SSH Clients | Release 14 supports OpenSSH client version 7.5.14i.1.5.18 for SSH connections. Release 14SU1 supports OpenSSH client version  7.5.14i.1.5.18 for SSH connections. Release 14SU2 of Unified CM and Release 14SU2a of IM and Presence Service supports CiscoSSH client version 1.9.29.18 for SSH
                                          connections. Release 14SU3 supports OpenSSH client version 1.9.29.18 for SSH connections. Release 14SU4 supports OpenSSH client version 1.11.34.3 for SSH connections. Release 14SU5 supports OpenSSH client version 1.13.48.11 for SSH connections. Release 14SU6 supports OpenSSH client version 1.13.48.11 for SSH connections. |

| Note | For additional information on the packages that are installed on your system, run the show packages active CLI command. See the Command Line Interface Reference Guide for Cisco Unified Communications Solutions for more information about this command and its options. |
|---|---|

| Application / Process | Protocol | Port | Supported Ciphers |
|---|---|---|---|
| Cisco CallManager | TCP / TLS | 2443 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
AES256-GCM-SHA384:
AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
AES128-GCM-SHA256:
AES128-SHA256:AES128-SHA: ECDHE-RSA-AES256-SHA: |
| DRS | TCP / TLS | 4040 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
AES256-GCM-SHA384:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
AES128-GCM-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Cisco Tomcat | TCP / TLS | 8443 / 443 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
DHE-RSA-AES256-GCM-SHA384:
DHE-RSA-AES256-SHA256:
DHE-RSA-AES256-SHA:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
DHE-RSA-AES128-GCM-SHA256:
DHE-RSA-AES128-SHA256:
DHE-RSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: 
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Cisco CallManager | TCP / TLS | 5061 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384 
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384: 
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA 
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Cisco Certificate Authority Proxy Function | TCP / TLS | 3804 | AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA |
| CTIManager | TCP / TLS | 2749 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Cisco Trust Verification Service | TCP / TLS | 2445 | AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:
ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES256-SHA384:
ECDHE-RSA-AES128-SHA256 |
| Cisco Intercluster Lookup Service | TCP / TLS | 7501 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
AES256-GCM-SHA384:
AES256-SHA256:AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Secure Configuration download (HAPROXY) | TCP / TLS | 6971, 6972 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Authenticated Contact Search | TCP / TLS | 9443 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA: ECDHE-RSA-AES256-SHA: |

| Service | Ciphers/Algorithms |
|---|---|
| SSH Server | Ciphers aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com MAC algorithms: hmac-sha2-256
hmac-sha2-512
hmac-sha1 Kex algorithms: ecdh-sha2-nistp521
ecdh-sha2-nistp384
ecdh-sha2-nistp256
diffie-hellman-group14-sha1
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512 Host Key algorithms in non-FIPS mode: rsa-sha2-256
rsa-sha2-512
ssh-rsa Host Key algorithms in FIPS mode: rsa-sha2-256
rsa-sha2-512 |
| SSH Client | Ciphers: aes128-ctr
aes192-ctr
aes256-ctr
aes128-gcm@openssh.com
aes256-gcm@openssh.com MAC algorithms: hmac-sha2-256
hmac-sha2-512
hmac-sha1 Kex algorithms: ecdh-sha2-nistp521
ecdh-sha2-nistp384
ecdh-sha2-nistp256
diffie-hellman-group14-sha1
diffie-hellman-group14-sha256
diffie-hellman-group16-sha512 Host Key algorithms in non-FIPS mode: rsa-sha2-256
rsa-sha2-512
ssh-rsa Host Key algorithms in FIPS mode: rsa-sha2-256
rsa-sha2-512 |
| DRS Client | Ciphers: aes256-ctr
aes128-ctr
aes192-ctr MAC algorithms: hmac-sha2-256
hmac-sha1 Kex algorithms: ecdh-sha2-nistp256
ecdh-sha2-nistp384
ecdh-sha2-nistp521
diffie-hellman-group14-sha1 Note The Kex algorithms diffie-hellman-group-exchange-sha256, diffie-hellman-group-exchange-sha1, and diffie-hellman-group1-sha1
                                                   are not supported from Release 12.5(1)SU4 if you have configured Cipher Management functionality in your Unified CM server.
                                                   If the ciphers are not configured, DRS Client uses these algorithms. | Note | The Kex algorithms diffie-hellman-group-exchange-sha256, diffie-hellman-group-exchange-sha1, and diffie-hellman-group1-sha1
                                                   are not supported from Release 12.5(1)SU4 if you have configured Cipher Management functionality in your Unified CM server.
                                                   If the ciphers are not configured, DRS Client uses these algorithms. |
| Note | The Kex algorithms diffie-hellman-group-exchange-sha256, diffie-hellman-group-exchange-sha1, and diffie-hellman-group1-sha1
                                                   are not supported from Release 12.5(1)SU4 if you have configured Cipher Management functionality in your Unified CM server.
                                                   If the ciphers are not configured, DRS Client uses these algorithms. |
| SFTP client | Ciphers: aes128-ctr
aes192-ctr 
aes256-ctr MAC algorithms: hmac-sha2-256 
hmac-sha1 Kex algorithms: ecdh-sha2-nistp521 
ecdh-sha2-nistp384 
diffie-hellman-group14-sha1 
diffie-hellman-group1-sha1 
diffie-hellman-group-exchange-sha256 
diffie-hellman-group-exchange-sha1 |
| End Users | hmac-sha512 SHA-512 – Hashing (salted) |
| DRS Backups / RTMT SFTPs | AES-128 – Encryption |
| Application Users | AES-256 – Encryption |

| Note | The Kex algorithms diffie-hellman-group-exchange-sha256, diffie-hellman-group-exchange-sha1, and diffie-hellman-group1-sha1
                                                   are not supported from Release 12.5(1)SU4 if you have configured Cipher Management functionality in your Unified CM server.
                                                   If the ciphers are not configured, DRS Client uses these algorithms. |
|---|---|

| Component | Install Compatible Version |
|---|---|
| Calendar Server | Exchange Server Subscription Edition (SE) Exchange Online in Microsoft 365 (formerly Office 365) |
| Certificate Server | Built-in Microsoft Certificate Server in Windows Server Third-party CA servers Note Microsoft Exchange integration with IM and Presence Service supports certificates using RSA 1024 or 2048 bit keys and SHA1
                                                and SHA256 signature algorithms. | Note | Microsoft Exchange integration with IM and Presence Service supports certificates using RSA 1024 or 2048 bit keys and SHA1
                                                and SHA256 signature algorithms. |
| Note | Microsoft Exchange integration with IM and Presence Service supports certificates using RSA 1024 or 2048 bit keys and SHA1
                                                and SHA256 signature algorithms. |

| Note | Microsoft Exchange integration with IM and Presence Service supports certificates using RSA 1024 or 2048 bit keys and SHA1
                                                and SHA256 signature algorithms. |
|---|---|

| Note | SIP federation and Remote Call Control (RCC) do not work together on
                                    			 the same IM and Presence Service cluster. This is because for SIP federation a
                                    			 user cannot be licensed for both Cisco IM and Presence Service and Microsoft
                                    			 Lync/OCS, but for RCC a user must be licensed for Cisco IM and Presence Service
                                    			 and Microsoft Lync/OCS at the same time. |
|---|---|

| Note | An IM and Presence Service cluster that is used for RCC does not support Jabber or other IM and Presence Service functionality. |
|---|---|

| Application / Process | Protocol | Port | Supported Ciphers |
|---|---|---|---|
| Cisco SIP Proxy | TCP / TLS | 5061 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:
AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Cisco SIP Proxy | TCP / TLS | 5062 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:
AES256-SHA256:AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Cisco SIP Proxy | TCP / TLS | 8083 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Cisco Tomcat | TCP / TLS | 8443, 443 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
DHE-RSA-AES256-GCM-SHA384:
DHE-RSA-AES256-SHA256:
DHE-RSA-AES256-SHA:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
DHE-RSA-AES128-GCM-SHA256:
DHE-RSA-AES128-SHA256:
DHE-RSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: 
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-SHA384:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA: ECDHE-RSA-AES256-SHA: |
| Cisco XCP XMPP Federation Connection Manager | TCP /TLS | 5269 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: |
| Cisco XCP Client Connection Manager | TCP / TLS | 5222 | ECDHE-RSA-AES256-GCM-SHA384:
ECDHE-ECDSA-AES256-GCM-SHA384:
ECDHE-RSA-AES256-SHA384:
ECDHE-ECDSA-AES256-SHA384:
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:
ECDHE-RSA-AES128-GCM-SHA256:
ECDHE-ECDSA-AES128-GCM-SHA256:
ECDHE-RSA-AES128-SHA256:
ECDHE-ECDSA-AES128-SHA256:
ECDHE-RSA-AES128-SHA:
ECDHE-ECDSA-AES128-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA: |