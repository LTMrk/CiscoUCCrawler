---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-compat-12-x-cucm-b-compatibility-matrix-cucm-imp-125x-html-e155bc0d95
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/12_x/cucm_b_compatibility-matrix-cucm-imp-125x.html
retrieved_at: 2026-08-16T17:51:10.729625+00:00
---

Compatibility Matrix for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(X)

# Compatibility Matrix for Cisco Unified Communications Manager and the IM and Presence Service, Release 12.5(X)

### Download Options

Updated: May 27, 2025

# Compatibility Matrix for Cisco Unified Communications Manager and the IM and Presence Service

## Revision History

Date

Revision

May 27, 2025

Updated the "Intercluster Peering Support" section.

March 17, 2025

Added support for Cisco Board Pro 55 G2 and Cisco Board Pro 75 G2.

July 23, 2024

Initial release version for 12.5(1)SU9.

July 23, 2024

Updated support versions for 12.5(1)SU9.

July 23, 2024

Added support for Cisco Desk Phone 9800 Series.

July 23, 2024

Removed support for Active Directory 2012 with Windows Server 2012 from the "Calendar Integration with Microsoft Outlook"
                              section.

August 30, 2023

Initial release version for 12.5(1)SU8a.

August 30, 2023

Updated support version for Unified CM Release 12.5(1)SU8a.

August 03, 2023

Initial release version for 12.5(1)SU8.

August 03, 2023

Updated support versions for 12.5(1)SU8.

August 03, 2023

Added support for Cisco Video Phone 8875 and Cisco Video Phone 8875NR.

January 31, 2023

Initial release version for 12.5(1)SU7a.

January 31, 2023

Updated support version for Unified CM Release 12.5(1)SU7a.

November 29, 2022

Initial release version for 12.5(1)SU7.

December 08, 2022

Updated upgrade paths and version support for 12.5(1)SU7.

December 08, 2022

Webex Desk Camera is rebranded to Cisco Desk Camera 4K.

December 08, 2022

Added support for Cisco Desk Camera 1080p.

December 08, 2022

Added support for Cisco Headset 320 Series and Cisco Headset 720 Series.

February 15, 2022

Initial release version for 12.5(1)SU6.

February 15, 2022

Updated upgrade paths and version support for 12.5(1)SU6.

February 15, 2022

Added support for Webex Desk Hub and Webex Wireless Phone 800 Series

May 05, 2022

Renamed some of the ROOM device names to remove Webex from them.

August 03, 2021

Initial release version for 12.5(1)SU5.

August 03, 2021

Updated upgrade paths and version support for 12.5(1)SU5.

August 03, 2021

Added Microsoft Exchange Server 2019 support for the IM and Presence Service Calendar Integration with Microsoft Outlook.

February 22, 2021

Initial release version for 12.5(1)SU4.

February 22, 2021

Updated upgrade paths and version support for 12.5(1)SU4.

February 22, 2021

Added IM and Presence Service support for the advertisement of XMPP stream features/services over Mobile and Remote Access.

February 22, 2021

Added support for Cisco VG420 Analog Voice Gateway and Cisco Catalyst 8300 Series Edge Platforms.

March 25, 2021

Fixed the 7941 G Series EOS URL.

April 28, 2021

Added support for Ciphers for Application and OS End Users.

August 13, 2020

Updated version support for 12.5(1)SU3.

August 13, 2020

Added support for Microsoft® Active Directory® Federation Services 3.0, 4.0, and 5.0, and Microsoft Azure.

October 19, 2020

Corrected list of Webex endpoints.

November 18, 2020

Corrected dates.

December 13, 2020

Renamed Cisco Webex Teams to Cisco Webex.

June 19, 2019

Added OpenJDK version for 12.5(1)SU1 release.

Updated for 12.5(1)SU1. Changed title to 12.5(x)

February 03, 2020

Updated upgrade paths, LDAP support, version support for 12.5(1)SU2.

February 20, 2020

Updated LDAPv3 Compliant Directories.

March 09, 2020

Updated Cisco Endpoint Support section.

March 11, 2020

Added Cisco Headsets to Endpoint Support.

April 06, 2020

Removed non-supported Cisco endpoints.

May 12, 2020

Added JTAPI Support information.

July 8, 2020

Updated SSL Connections and SSH Clients.

July 27, 2020

Updated supported ciphers list for IM and Presence Service.

## Purpose of this Document

This document contains compatibility information for 12.5(x) releases of Cisco Unified Communications Manager (Unified Communications
                     Manager) and the Cisco Unified Communications Manager IM and Presence Service (IM and Presence Service). This includes subsequent
                     SU releases as well, unless indicated otherwise.

## Supported Upgrade and Migration Paths

The following table highlights supported upgrade paths to upgrade to 12.5(x) releases of Unified Communications Manager and
                     the IM and Presence Service.

Unless indicated otherwise, each release category includes the SU releases within that category. For example, 12.5(x) includes
                              12.5(1)SU releases. In addition, releases like 10.5(x) and 11.x include any SU releases within those categories as well.

Source

Destination

Supported Upgrade Method

Version Switching* (Source to Destination and Vice Versa)

Cisco Unified Communications Manager Upgrade Paths

Unified CM 10.0(x)

12.5(x)

PCD Migration**

Version switching not supported

Unified CM 10.5(x), 11.x, 12.0(x)

12.5(x)

Unified OS Admin upgrade (direct refresh)

CLI upgrade (direct refresh)

PCD Upgrade (direct refresh)**

PCD Migration**

Fresh Install with Data Import only to destination 12.5(1)SU5 or later.

If the source release is 10.5(x) and the destination release is 12.5(1) through 12.5(1)SU5, PCD Upgrade Task is supported.

If the source release is 10.5(x) and the destination release is 12.5(1)SU6 and above, PCD Upgrade Task is not supported.

Version switching supported for upgrades, but not for migrations

Unified CM 12.5(x)

12.5(y)

Unified OS Admin upgrade (direct standard)

CLI upgrade (direct standard)

PCD Upgrade (direct standard)**

Fresh Install with Data Import only to destination 12.5(1)SU5 or later.

Version switching supported for upgrades, but not for migrations

IM and Presence Service Upgrade Paths

IM and Presence 10.0(x)

IM and Presence 12.5(x)

PCD Migration**

Version switching not supported

IM and Presence 10.5(x), 11.x or 12.0(x)

12.5(x)

Unified OS Admin upgrade (direct refresh)

CLI upgrade (direct refresh)

PCD upgrade (direct refresh)**

PCD Migration**

Fresh Install with Data Import only to destination 12.5(1)SU5 or later.

Version switching supported for upgrades, but not supported for migrations.

IM and Presence 12.5(x)

12.5(y)

Unified OS Admin upgrade (direct standard)

CLI upgrade (direct standard)

PCD upgrade (direct standard)**

Fresh Install with Data Import only to destination 12.5(1)SU5 or later.

Version switching supported for upgrades, but not supported for migrations.

* Version switching refers to the ability to install the new version as an inactive version and switch to the new version,
                     and revert to the old version, whenever you want. This capability is supported with most direct upgrades, but not with migrations.

** PCD Upgrades and Migrations—Use Cisco Prime Collaboration Deployment Release 12.6 or later for all PCD tasks. If you want
                     to upgrade or migrate to Unified CM Release 12.5(1)SU6 and above, ensure that you use the Release 14 version of the Cisco
                     Prime Collaboration Deployment.

### Required COP Files

The tables below lists the upgrade paths that require COP files. You must install COP files on each node before you begin
                        an upgrade using the Cisco Unified OS Administration interface, or before you begin an upgrade or migration using the Prime
                        Collaboration Deployment (PCD) tool. If you are using PCD, you can perform a bulk installation of the COP files before you
                        begin the upgrade.

You can download COP files for Cisco Unified Communications Manager and the IM and Presence Service at https://software.cisco.com/download/home/268439621 . After you select the destination version for the upgrade, choose Unified Communications Manager Utilities to see the list of COP files.

You should run the Upgrade Readiness COP file prior to the upgrade in order to maximize upgrade success. If you do not run
                                    this COP file, you increase the risk of an unsuccessful upgrade due to undetected issues on the source release. Cisco TAC
                                    may require that you run this COP file to provide effective technical support.

From

To

COP Files

Unified Communications Manager Upgrades

Unified CM 10.5(x), 11.0(x)

12.5(x)

Direct Refresh upgrade

Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information.

Unified CM 11.5(x)

12.5(x)

Direct Refresh upgrade; COP file is required to increase the disk space.

ciscocm.free_common_space_v<latest_version>.cop.sgn. To download the COP files and the Readme files, go to https://software.cisco.com , click Software Download link under Download & Upgrade section, and navigate to the Unified Communications > Call Control > Cisco Unified Communications Manager (CallManager) > <Version> > Unified Communications Manager/CallManager/Cisco Unity Connection Utilities .

Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information.

Unified CM 12.0(1)

12.5(x)

PCD Migrations require a COP file:

ciscocm-slm-migration.k3.cop.sgn

This requirement applies only for Prime Collaboration Deployment migrations from Release 12.0(1) of Unified Communications
                                                Manager (build 12.0.1.10000-10). If you are migrating from a higher release, such as Unified Communications Manager 12.0(1)SU1,
                                                you don't need to install the COP file.

Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information.

Unified CM 12.5(x)

12.5(y)

Direct Standard upgrade

Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information.

IM and Presence Service Upgrades

10.5(x), 11.x, 12.x

12.5(x)

No COP files required

## Supported Versions

The following table outlines which Unified Communications Manager and IM and Presence Service versions are supported with
                     each release:

For this Release...

The Following Versions are Supported...

12.5(1)

Unified Communications Manager 12.5.1.10000-22

IM and Presence Service 12.5.1.10000-22

12.5(1)SU1

Unified Communications Manager 12.5.1.11900-146

IM and Presence Service 12.5.1.11900-117

12.5(1)SU2

Unified Communications Manager 12.5.1.12900-115

IM and Presence Service 12.5.1.12900-25

12.5(1)SU3

Unified Communications Manager 12.5.1.13900-152

IM and Presence Service 12.5.1.13900-17

12.5(1)SU4

Unified Communications Manager 12.5.1.14900-63

IM and Presence Service 12.5.1.14900-4

12.5(1)SU5

Unified Communications Manager 12.5.1.15900-66

IM and Presence Service 12.5.1.15900-5

12.5(1)SU6

Unified Communications Manager 12.5.1.16900-48

IM and Presence Service 12.5.1.16900-3

12.5(1)SU7

Unified Communications Manager 12.5.1.17900-64

IM and Presence Service 12.5.1.17900-7

12.5(1)SU7a

Unified Communications Manager 12.5.1.18100-14

IM and Presence Service 12.5.1.17900-7

12.5(1)SU8

IM and Presence Service 12.5.1.18900-6

12.5(1)SU8a

Unified Communications Manager 12.5.1.18901-1

12.5(1)SU9

Unified Communications Manager 12.5.1.21900-29

IM and Presence Service 12.5.1.21900-3

## Unified Communications Manager Compatibility Information

### Cisco Collaboration System Applications

The 12.5.x release of Cisco Unified Communications Manager and the IM and Presence Service is a part of the Cisco Collaboration
                        Systems Release 12.5 through 12.8 and is compatible with the other Cisco Collaboration applications and versions in Cisco
                        Collaboration Systems Release 12.5.

Note that Release 12.5(1)SU3 is compatible with the 12.8 version of  the Cisco Collaboration Systems.

For a full list of Cisco Collaboration applications that are a part of Cisco Collaboration Systems Release 12.5(x), and the
                        supported versions for each, see the Cisco Collaboration Systems Release Compatibility Matrix at: https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/CSR-Compatibility-Matrix-InteractiveHTML.html .

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

12.5(1)SU3 and onwards

X12.6.2

Enable Android Push Notification using the CLI xConfiguration XCP Config FcmService: On on Expressway for messaging only

Android Push Notification is supported

Cluster with mixed versions (11.5(1)SU8 or earlier, OR 12.5(1)SU2 or earlier, AND 12.5(1)SU3 onwards)

X12.6.2

Android Push Notification for Messaging is not supported

VOIP is supported from  Release 12.5(1)SU3 onwards

Android Push Notification is supported from Release 12.5(1)SU3 onwards

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

11.5(1)SU8 (and lower) or 12.5(1)SU2 (and lower) with 12.5(1)SU3 or 14

OFF

Android push (FCM) NOT supported

11.5(1)SU8 (and lower) or 12.5(1)SU2 (and lower) with 12.5(1)SU4 (and higher) or 14SU1 (and higher)

OFF

Android push (FCM) supported on 12.5(1)SU4 (or newer) versions

11.5(1)SU9 (and higher) or 12.5(1)SU4 (and higher) with 12.5(1)SU3 or 14SU1 (and higher)

ON

Android push (FCM) supported on version 12.5(1)SU3 and higher

11.5(1)SU9 (and higher) with 12.5(1)SU4 (and higher) or 14SU1 (and higher)

Flag not required

(Expressway 12.7 relies fully on the new discovery mechanism)

Android push (FCM) supported on 12.5(1)SU4 (or newer) versions

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

Cisco Desk Phone 9841

Cisco Desk Phone 9851

Cisco Desk Phone 9861

Cisco Desk Phone 9871

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

For additional information, refer to Field Notice: Cisco Unified Communications Manager Release 11.5(x) does not support some deprecated phone models at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/11_5_1/fieldNotice/cucm_b_fn-deprecated-phone-models-1151.html .

For additional information refer to the Field Notice: Cisco Unified Communications Manager Release 12.0(x) does not support some deprecated phone models at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/12_0_1/deprecated_phones/cucm_b_deprecated-phone-models-for-1201.html .

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

Unified Communications Manager

For information about Unified Communications Manager virtualization requirements, go to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-communications-manager.html .

IM and Presence Service

For information about the IM and Presence Service virtualization requirements, go to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-ucm-im-presence.html .

Cisco Business Edition Deployments

For information on the virtualization requirements for Unified Communications Manager in a collaboration solution deployment
                                    such as Cisco Business Edition, go to the following:

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/cisco-collaboration-infrastructure.html

Cisco Business Edition 7000

Cisco Business Edition 6000

### Supported LDAP Directories 12.5(x)

The following LDAP directories are supported:

Microsoft Active Directory 2008 R1/ R2

Microsoft Active Directory 2012 R1/ R2

Microsoft Active Directory 2016

Microsoft Active Directory 2019—Supported for 12.5(1)SU2 and later

Microsoft Lightweight Directory Services 2008 R1/ R2

Microsoft Lightweight Directory Services 2012 R1/ R2

Microsoft Lightweight Directory Services 2019—Supported for 12.5(1)SU2 and later

Oracle Directory Services Enterprise Edition 11gR1 (11.1.1.7.x or newer)

Oracle Unified Directory 11gR2 (11.1.2.2.0 or 11.1.2.3.0)

Open LDAP 2.4.45 or later

Other LDAPv3 Compliant Directories—Unified Communications Manager uses standard LDAPv3 for accessing the user's data. Ensure
                              that the supportedcontrol attribute is configured in the LDAPv3 compliant directory servers to be used with DirSync. (The
                              supportedcontrol attribute may return the pagecontrolsupport and persistentcontrolsupport sub attributes, if configured.)

### Supported Web Browsers

The following web browsers are supported:

Chrome with Windows 10 (64 bit)

Firefox with Windows 10 (64 bit)

Internet Explorer 11 with Windows 7 (64 bit)

Internet Explorer 11 with Windows 10 (64 bit)

Microsoft Edge browser with Windows 10 (32 bit/64 bit)

Safari with MacOS (10.x)

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

### API Development

The following table provides information on the API Development package that is supported with this release.

Package Type

Details

API Development

Cisco Unified Communications Manager and the IM and Presence Service support OpenJDK for application development.

Release 12.5(1) uses OpenJDK version 1.7.0.191.

Release 12.5(1)SU1 uses OpenJDK version  1.7.0.201.

Release 12.5(1)SU4 uses OpenJDK version 1.8.0.262.

Release 12.5(1)SU5 uses OpenJDK version 1.8.0.262.

Release 12.5(1)SU6 uses OpenJDK version 1.8.0.262.

Release 12.5(1)SU7 uses OpenJDK version 1.8.0.262.

Release 12.5(1)SU8 uses OpenJDK version 1.8.0.262.

Release 12.5(1)SU9 uses OpenJDK version 1.8.0.262.

### Secure Connections

#### TLS 1.2 Support

Unified Communications Manager and the IM and Presence Service support the use of TLS 1.2. For detailed information on TLS
                        1.2 support, see the TLS 1.2 Compatibility Matrix for Cisco Collaboration Products .

#### SSL Connections

For Secure Sockets Layer (SSL) connections, this release supports both Cisco SSL and Cisco SSH:

Cisco OpenSSL 1.0.2zf.6.2.511 and CiscoSSL 1.0.2zd.6.2.48

Cisco OpenSSH client version 7.5.14i.1.5.18 and CiscoSSH 7.5.14i.1.5.18

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

Cisco CTL Provider

Cisco CTL Provider is not available from Release 14SU3 onwards.

TCP / TLS

2444

```
AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:CAMELLIA256-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:CAMELLIA128-SHA:
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
SHA-256 – Hashing (salted)
```

DRS Backups / RTMT SFTPs

```
AES-128 – Encryption
```

Application Users

```
AES-256 – Encryption
```

### Supported Platforms for Cisco Unified JTAPI and TAPI

#### Cisco Unified JTAPI

For a detailed breakdown of supported Windows, Linux, and VMware platforms for Cisco Unified JTAPI, see https://developer.cisco.com/site/jtapi/documents/cisco-unified-jtapi-supported-jvm-versions/ .

For additional information that is related to Cisco Unified JTAPI, see Cisco Unified JTAPI Developers Guide for Cisco Unified Communications Manager .

#### Cisco Unified TAPI

For a detailed breakdown of supported Windows platforms for Cisco Unified TAPI, see https://developer.cisco.com/site/tapi/documents/supported-windows-os/ .

For additional information that is related to Cisco Unified TAPI, see Cisco Unified TAPI Developers Guide for Cisco Unified Communications Manager .

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

### Supported LDAP Directories 12.5(x)

The following LDAP directories are supported:

Microsoft Active Directory 2008 R1/ R2

Microsoft Active Directory 2012 R1/ R2

Microsoft Active Directory 2016

Microsoft Active Directory 2019—Supported for 12.5(1)SU2 and later

Microsoft Lightweight Directory Services 2008 R1/ R2

Microsoft Lightweight Directory Services 2012 R1/ R2

Microsoft Lightweight Directory Services 2019—Supported for 12.5(1)SU2 and later

Oracle Directory Services Enterprise Edition 11gR1 (11.1.1.7.x or newer)

Oracle Unified Directory 11gR2 (11.1.2.2.0 or 11.1.2.3.0)

Open LDAP 2.4.45 or later

Other LDAPv3 Compliant Directories—Unified Communications Manager uses standard LDAPv3 for accessing the user's data. Ensure
                              that the supportedcontrol attribute is configured in the LDAPv3 compliant directory servers to be used with DirSync. (The
                              supportedcontrol attribute may return the pagecontrolsupport and persistentcontrolsupport sub attributes, if configured.)

### Federation Support

#### SIP Federation/SIP Open Federation  Support

SIP Open Federation is supported as of 12.5(1)SU3.

Cisco IM and Presence service supports SIP open federation for Cisco Jabber clients. As an administrator, you can configure
                        SIP open federation allowing Cisco Jabber users seamlessly federate with users from all available domains.

#### Supported XMPP Federations

This release of IM and Presence Service supports XMPP Federation with the following systems:

Cisco Webex Messenger

IM and Presence Service Release 10.x and up

Any other XMPP-compliant system

### Intercluster Peering Support

This release of the IM and Presence Service supports intercluster peering with the following IM and Presence Service releases:

Intercluster peering is not supported if the IM and Presence Service version has gone EOL/EOS.

Release 12.5(x)

Release 15 and SUs

### Calendar Integration with Microsoft Outlook

The IM and Presence Service supports Microsoft Outlook Calendar Integration with either an on-premise Exchange server or a
                        hosted Office 365 server. See the table below for support information:

For technical support on any third-party products, contact the respective organization.

Component

Install Compatible Version

Windows Server

Service Packs for Windows Server 2012 (Standard)

Windows Server 2016

Windows Server 2019—With 11.x releases, the minimum IM and Presence Service Release is 11.5(1)SU7. With 12.x releases, the minimum IM and Presence Service Release is 12.5(1)SU2.

Microsoft Exchange Server 2016

Microsoft Exchange 2016

Microsoft Exchange Server 2019

Microsoft Exchange 2019

Microsoft Office 365

See your Microsoft documentation for details on deploying a hosted Office 365 server.

As of October 2020, Microsoft is changing the authentication mechanism that is supported by Exchange Online to use OAuth-based
                                             authentication only. After the change, if you want to deploy calendar integration between the IM and Presence Service and
                                             Office 365, you will need to upgrade the IM and Presence Service to Release 12.5(1)SU2. This change will not affect integration
                                             with an on-premises Exchange server.

Active Directory

Active Directory 2016 with Windows Server 2016

User names configured in Active Directory must be identical to those names defined in Unified Communications Manager.

A Third-Party Certificate OR Certificate Server

One or the other of these are required to generate the certificates.

Microsoft Exchange integration with IM and Presence Service supports certificates using RSA 1024 or 2048-bit keys and SHA1
                                                and SHA256 signature algorithms.

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

| Date | Revision |
|---|---|
| May 27, 2025 | Updated the "Intercluster Peering Support" section. |
| March 17, 2025 | Added support for Cisco Board Pro 55 G2 and Cisco Board Pro 75 G2. |
| July 23, 2024 | Initial release version for 12.5(1)SU9. |
| July 23, 2024 | Updated support versions for 12.5(1)SU9. |
| July 23, 2024 | Added support for Cisco Desk Phone 9800 Series. |
| July 23, 2024 | Removed support for Active Directory 2012 with Windows Server 2012 from the "Calendar Integration with Microsoft Outlook"
                              section. |
| August 30, 2023 | Initial release version for 12.5(1)SU8a. |
| August 30, 2023 | Updated support version for Unified CM Release 12.5(1)SU8a. |
| August 03, 2023 | Initial release version for 12.5(1)SU8. |
| August 03, 2023 | Updated support versions for 12.5(1)SU8. |
| August 03, 2023 | Added support for Cisco Video Phone 8875 and Cisco Video Phone 8875NR. |
| January 31, 2023 | Initial release version for 12.5(1)SU7a. |
| January 31, 2023 | Updated support version for Unified CM Release 12.5(1)SU7a. |
| November 29, 2022 | Initial release version for 12.5(1)SU7. |
| December 08, 2022 | Updated upgrade paths and version support for 12.5(1)SU7. |
| December 08, 2022 | Webex Desk Camera is rebranded to Cisco Desk Camera 4K. |
| December 08, 2022 | Added support for Cisco Desk Camera 1080p. |
| December 08, 2022 | Added support for Cisco Headset 320 Series and Cisco Headset 720 Series. |
| February 15, 2022 | Initial release version for 12.5(1)SU6. |
| February 15, 2022 | Updated upgrade paths and version support for 12.5(1)SU6. |
| February 15, 2022 | Added support for Webex Desk Hub and Webex Wireless Phone 800 Series |
| May 05, 2022 | Renamed some of the ROOM device names to remove Webex from them. |
| August 03, 2021 | Initial release version for 12.5(1)SU5. |
| August 03, 2021 | Updated upgrade paths and version support for 12.5(1)SU5. |
| August 03, 2021 | Added Microsoft Exchange Server 2019 support for the IM and Presence Service Calendar Integration with Microsoft Outlook. |
| February 22, 2021 | Initial release version for 12.5(1)SU4. |
| February 22, 2021 | Updated upgrade paths and version support for 12.5(1)SU4. |
| February 22, 2021 | Added IM and Presence Service support for the advertisement of XMPP stream features/services over Mobile and Remote Access. |
| February 22, 2021 | Added support for Cisco VG420 Analog Voice Gateway and Cisco Catalyst 8300 Series Edge Platforms. |
| March 25, 2021 | Fixed the 7941 G Series EOS URL. |
| April 28, 2021 | Added support for Ciphers for Application and OS End Users. |
| August 13, 2020 | Updated version support for 12.5(1)SU3. |
| August 13, 2020 | Added support for Microsoft® Active Directory® Federation Services 3.0, 4.0, and 5.0, and Microsoft Azure. |
| October 19, 2020 | Corrected list of Webex endpoints. |
| November 18, 2020 | Corrected dates. |
| December 13, 2020 | Renamed Cisco Webex Teams to Cisco Webex. |
| June 19, 2019 | Added OpenJDK version for 12.5(1)SU1 release. |
| Updated for 12.5(1)SU1. Changed title to 12.5(x) |
| February 03, 2020 | Updated upgrade paths, LDAP support, version support for 12.5(1)SU2. |
| February 20, 2020 | Updated LDAPv3 Compliant Directories. |
| March 09, 2020 | Updated Cisco Endpoint Support section. |
| March 11, 2020 | Added Cisco Headsets to Endpoint Support. |
| April 06, 2020 | Removed non-supported Cisco endpoints. |
| May 12, 2020 | Added JTAPI Support information. |
| July 8, 2020 | Updated SSL Connections and SSH Clients. |
| July 27, 2020 | Updated supported ciphers list for IM and Presence Service. |

| Note | Unless indicated otherwise, each release category includes the SU releases within that category. For example, 12.5(x) includes
                              12.5(1)SU releases. In addition, releases like 10.5(x) and 11.x include any SU releases within those categories as well. |
|---|---|

| Source | Destination | Supported Upgrade Method | Version Switching* (Source to Destination and Vice Versa) |
|---|---|---|---|
| Cisco Unified Communications Manager Upgrade Paths |
| Unified CM 10.0(x) | 12.5(x) | PCD Migration** | Version switching not supported |
| Unified CM 10.5(x), 11.x, 12.0(x) | 12.5(x) | Unified OS Admin upgrade (direct refresh) CLI upgrade (direct refresh) PCD Upgrade (direct refresh)** PCD Migration** Fresh Install with Data Import only to destination 12.5(1)SU5 or later. Note If the source release is 10.5(x) and the destination release is 12.5(1) through 12.5(1)SU5, PCD Upgrade Task is supported. If the source release is 10.5(x) and the destination release is 12.5(1)SU6 and above, PCD Upgrade Task is not supported. | Note | If the source release is 10.5(x) and the destination release is 12.5(1) through 12.5(1)SU5, PCD Upgrade Task is supported. If the source release is 10.5(x) and the destination release is 12.5(1)SU6 and above, PCD Upgrade Task is not supported. | Version switching supported for upgrades, but not for migrations |
| Note | If the source release is 10.5(x) and the destination release is 12.5(1) through 12.5(1)SU5, PCD Upgrade Task is supported. If the source release is 10.5(x) and the destination release is 12.5(1)SU6 and above, PCD Upgrade Task is not supported. |
| Unified CM 12.5(x) | 12.5(y) | Unified OS Admin upgrade (direct standard) CLI upgrade (direct standard) PCD Upgrade (direct standard)** Fresh Install with Data Import only to destination 12.5(1)SU5 or later. | Version switching supported for upgrades, but not for migrations |
| IM and Presence Service Upgrade Paths |
| IM and Presence 10.0(x) | IM and Presence 12.5(x) | PCD Migration** | Version switching not supported |
| IM and Presence 10.5(x), 11.x or 12.0(x) | 12.5(x) | Unified OS Admin upgrade (direct refresh) CLI upgrade (direct refresh) PCD upgrade (direct refresh)** PCD Migration** Fresh Install with Data Import only to destination 12.5(1)SU5 or later. | Version switching supported for upgrades, but not supported for migrations. |
| IM and Presence 12.5(x) | 12.5(y) | Unified OS Admin upgrade (direct standard) CLI upgrade (direct standard) PCD upgrade (direct standard)** Fresh Install with Data Import only to destination 12.5(1)SU5 or later. | Version switching supported for upgrades, but not supported for migrations. |

| Note | If the source release is 10.5(x) and the destination release is 12.5(1) through 12.5(1)SU5, PCD Upgrade Task is supported. If the source release is 10.5(x) and the destination release is 12.5(1)SU6 and above, PCD Upgrade Task is not supported. |
|---|---|

| Note | You should run the Upgrade Readiness COP file prior to the upgrade in order to maximize upgrade success. If you do not run
                                    this COP file, you increase the risk of an unsuccessful upgrade due to undetected issues on the source release. Cisco TAC
                                    may require that you run this COP file to provide effective technical support. |
|---|---|

| From | To | COP Files |
|---|---|---|
| Unified Communications Manager Upgrades |
| Unified CM 10.5(x), 11.0(x) | 12.5(x) | Direct Refresh upgrade Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information. |
| Unified CM 11.5(x) | 12.5(x) | Direct Refresh upgrade; COP file is required to increase the disk space. ciscocm.free_common_space_v<latest_version>.cop.sgn. To download the COP files and the Readme files, go to https://software.cisco.com , click Software Download link under Download & Upgrade section, and navigate to the Unified Communications > Call Control > Cisco Unified Communications Manager (CallManager) > <Version> > Unified Communications Manager/CallManager/Cisco Unity Connection Utilities . Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information. |
| Unified CM 12.0(1) | 12.5(x) | PCD Migrations require a COP file: ciscocm-slm-migration.k3.cop.sgn Note This requirement applies only for Prime Collaboration Deployment migrations from Release 12.0(1) of Unified Communications
                                                Manager (build 12.0.1.10000-10). If you are migrating from a higher release, such as Unified Communications Manager 12.0(1)SU1,
                                                you don't need to install the COP file. Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information. | Note | This requirement applies only for Prime Collaboration Deployment migrations from Release 12.0(1) of Unified Communications
                                                Manager (build 12.0.1.10000-10). If you are migrating from a higher release, such as Unified Communications Manager 12.0(1)SU1,
                                                you don't need to install the COP file. |
| Note | This requirement applies only for Prime Collaboration Deployment migrations from Release 12.0(1) of Unified Communications
                                                Manager (build 12.0.1.10000-10). If you are migrating from a higher release, such as Unified Communications Manager 12.0(1)SU1,
                                                you don't need to install the COP file. |
| Unified CM 12.5(x) | 12.5(y) | Direct Standard upgrade Required COP file: ciscocm.enable-sha512sum-2021-signingkey-v1.0.cop.sgn. See the COP file for more information. |
| IM and Presence Service Upgrades |
| 10.5(x), 11.x, 12.x | 12.5(x) | No COP files required |

| Note | This requirement applies only for Prime Collaboration Deployment migrations from Release 12.0(1) of Unified Communications
                                                Manager (build 12.0.1.10000-10). If you are migrating from a higher release, such as Unified Communications Manager 12.0(1)SU1,
                                                you don't need to install the COP file. |
|---|---|

| For this Release... | The Following Versions are Supported... |
|---|---|
| 12.5(1) | Unified Communications Manager 12.5.1.10000-22 IM and Presence Service 12.5.1.10000-22 |
| 12.5(1)SU1 | Unified Communications Manager 12.5.1.11900-146 IM and Presence Service 12.5.1.11900-117 |
| 12.5(1)SU2 | Unified Communications Manager 12.5.1.12900-115 IM and Presence Service 12.5.1.12900-25 |
| 12.5(1)SU3 | Unified Communications Manager 12.5.1.13900-152 IM and Presence Service 12.5.1.13900-17 |
| 12.5(1)SU4 | Unified Communications Manager 12.5.1.14900-63 IM and Presence Service 12.5.1.14900-4 |
| 12.5(1)SU5 | Unified Communications Manager 12.5.1.15900-66 IM and Presence Service 12.5.1.15900-5 |
| 12.5(1)SU6 | Unified Communications Manager 12.5.1.16900-48 IM and Presence Service 12.5.1.16900-3 |
| 12.5(1)SU7 | Unified Communications Manager 12.5.1.17900-64 IM and Presence Service 12.5.1.17900-7 |
| 12.5(1)SU7a | Unified Communications Manager 12.5.1.18100-14 IM and Presence Service 12.5.1.17900-7 |
| 12.5(1)SU8 | IM and Presence Service 12.5.1.18900-6 |
| 12.5(1)SU8a | Unified Communications Manager 12.5.1.18901-1 |
| 12.5(1)SU9 | Unified Communications Manager 12.5.1.21900-29 IM and Presence Service 12.5.1.21900-3 |

| Note | Note that Release 12.5(1)SU3 is compatible with the 12.8 version of  the Cisco Collaboration Systems. |
|---|---|

| Note | This compatibility information isn't applicable for Cisco Webex. |
|---|---|

| Unified Communications Manager and IM and Presence Service Version | Expressway Version | Unified Communications Mobile and Remote Access | On-Premises Deployments |
|---|---|---|---|
| All clusters on: 11.5(1)SU8 or earlier 12.5(1)SU2 or earlier | X12.6.2 | Android Push Notification is not supported | Android Push Notification is not supported |
| All clusters on: 12.5(1)SU3 and onwards | X12.6.2 | Enable Android Push Notification using the CLI xConfiguration XCP Config FcmService: On on Expressway for messaging only | Android Push Notification is supported |
| Cluster with mixed versions (11.5(1)SU8 or earlier, OR 12.5(1)SU2 or earlier, AND 12.5(1)SU3 onwards) | X12.6.2 | Android Push Notification for Messaging is not supported VOIP is supported from  Release 12.5(1)SU3 onwards | Android Push Notification is supported from Release 12.5(1)SU3 onwards |

| Note | Apple Push Notification Service (APNS) is not affected by the FCM service flag status. |
|---|---|

| Mixed Versions IM and Presence Clusters | Expected Status of FCM Flag on Expressway X12.7 | Comment |
|---|---|---|
| Any 11.5(1)SU with 12.5(1)SU2 and lower | OFF | Android Push (FCM) NOT supported. |
| 11.5(1)SU8 (and lower) or 12.5(1)SU2 (and lower) with 12.5(1)SU3 or 14 | OFF | Android push (FCM) NOT supported |
| 11.5(1)SU8 (and lower) or 12.5(1)SU2 (and lower) with 12.5(1)SU4 (and higher) or 14SU1 (and higher) | OFF | Android push (FCM) supported on 12.5(1)SU4 (or newer) versions |
| 11.5(1)SU9 (and higher) or 12.5(1)SU4 (and higher) with 12.5(1)SU3 or 14SU1 (and higher) | ON | Android push (FCM) supported on version 12.5(1)SU3 and higher |
| 11.5(1)SU9 (and higher) with 12.5(1)SU4 (and higher) or 14SU1 (and higher) | Flag not required (Expressway 12.7 relies fully on the new discovery mechanism) | Android push (FCM) supported on 12.5(1)SU4 (or newer) versions |

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
| Cisco Desk Phone 9800 Series | Cisco Desk Phone 9841 Cisco Desk Phone 9851 Cisco Desk Phone 9861 Cisco Desk Phone 9871 Cisco Desk Phone 9800 Key Expansion Module (KEM) |
| Cisco Jabber | Cisco Jabber for Android Cisco Jabber for iPhone and iPad Cisco Jabber for Mac Cisco Jabber for Windows Cisco Jabber Softphone for VDI - Windows (formerly Cisco Virtualization Experience Media Edition for Windows) Cisco Jabber Guest Cisco Jabber Software Development Kit Cisco Jabber for Tablet |
| Cisco Headset Series | Cisco Headset 320 Cisco Headset 520 Cisco Headset 530 Cisco Headset 560 Cisco Headset 720 Cisco Headset 730 |
| Cisco IP Communicator | Cisco IP Communicator— EOS Notice |
| Webex | Webex App Webex Room Phone Webex Desk Webex Desk Hub Webex Desk Pro Webex Desk Limited Edition Webex Share— EOS Notice Board 55, 55S, 70, 70S, 85, 85S Board Pro 55 G2 and 75 G2 Webex Room Panorama Webex Room 70 Panorama Webex Room 70 Panorama Upgrade Room 70 Room 70 G2 Room 55 Room 55 Dual Room Kit Pro Room Kit Plus Room Kit Room Kit Mini Webex Room USB |
| Webex Wireless Phone 800 Series | Webex Wireless Phone 840 Webex Wireless Phone 860 |
| Webex Meetings | Webex Meetings for iPad and iPhone Webex Meetings for Android |
| Cisco Analog Telephony Adapters | Cisco ATA 190 Series Analog Telephone Adapters— EOS/EOL Notice Cisco ATA 191 Series Analog Telephone Adapters |
| Cisco DX Series | Cisco Webex DX70— EOS Notice Cisco Webex DX80— EOS Notice Cisco DX650— EOS Notice |
| Cisco TelePresence IX5000 | Cisco TelePresence IX5000 |
| Cisco TelePresence EX Series | Cisco TelePresence System EX90— EOS Notice |
| Cisco TelePresence MX Series | Cisco TelePresence MX200 G2— EOS Notice Cisco TelePresence MX300 G2— EOS Notice Cisco TelePresence MX700D— EOS Notice Cisco TelePresence MX800S— EOS Notice Cisco TelePresence MX800D— EOS Notice |
| Cisco TelePresence SX Series | Cisco TelePresence SX10— EOS Notice Cisco TelePresence SX20— EOS Notice Cisco TelePresence SX80— EOS Notice |

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
| Unified Communications Manager | For information about Unified Communications Manager virtualization requirements, go to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unified-communications-manager.html . |
| IM and Presence Service | For information about the IM and Presence Service virtualization requirements, go to https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-ucm-im-presence.html . |
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
| API Development | Cisco Unified Communications Manager and the IM and Presence Service support OpenJDK for application development. Release 12.5(1) uses OpenJDK version 1.7.0.191. Release 12.5(1)SU1 uses OpenJDK version  1.7.0.201. Release 12.5(1)SU4 uses OpenJDK version 1.8.0.262. Release 12.5(1)SU5 uses OpenJDK version 1.8.0.262. Release 12.5(1)SU6 uses OpenJDK version 1.8.0.262. Release 12.5(1)SU7 uses OpenJDK version 1.8.0.262. Release 12.5(1)SU8 uses OpenJDK version 1.8.0.262. Release 12.5(1)SU9 uses OpenJDK version 1.8.0.262. |

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
| Cisco CTL Provider Note Cisco CTL Provider is not available from Release 14SU3 onwards. | Note | Cisco CTL Provider is not available from Release 14SU3 onwards. | TCP / TLS | 2444 | AES256-GCM-SHA384:AES256-SHA256:
AES256-SHA:CAMELLIA256-SHA:
AES128-GCM-SHA256:AES128-SHA256:
AES128-SHA:CAMELLIA128-SHA: |
| Note | Cisco CTL Provider is not available from Release 14SU3 onwards. |
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

| Note | Cisco CTL Provider is not available from Release 14SU3 onwards. |
|---|---|

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
diffie-hellman-group16-sha512 |
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
diffie-hellman-group16-sha512 |
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
| End Users | hmac-sha512 SHA-256 – Hashing (salted) |
| DRS Backups / RTMT SFTPs | AES-128 – Encryption |
| Application Users | AES-256 – Encryption |

| Note | The Kex algorithms diffie-hellman-group-exchange-sha256, diffie-hellman-group-exchange-sha1, and diffie-hellman-group1-sha1
                                                   are not supported from Release 12.5(1)SU4 if you have configured Cipher Management functionality in your Unified CM server.
                                                   If the ciphers are not configured, DRS Client uses these algorithms. |
|---|---|

| Note | Intercluster peering is not supported if the IM and Presence Service version has gone EOL/EOS. |
|---|---|

| Note | For technical support on any third-party products, contact the respective organization. |
|---|---|

| Component | Install Compatible Version |
|---|---|
| Windows Server | Service Packs for Windows Server 2012 (Standard) Windows Server 2016 Windows Server 2019—With 11.x releases, the minimum IM and Presence Service Release is 11.5(1)SU7. With 12.x releases, the minimum IM and Presence Service Release is 12.5(1)SU2. |
| Microsoft Exchange Server 2016 | Microsoft Exchange 2016 |
| Microsoft Exchange Server 2019 | Microsoft Exchange 2019 |
| Microsoft Office 365 | See your Microsoft documentation for details on deploying a hosted Office 365 server. Note As of October 2020, Microsoft is changing the authentication mechanism that is supported by Exchange Online to use OAuth-based
                                             authentication only. After the change, if you want to deploy calendar integration between the IM and Presence Service and
                                             Office 365, you will need to upgrade the IM and Presence Service to Release 12.5(1)SU2. This change will not affect integration
                                             with an on-premises Exchange server. | Note | As of October 2020, Microsoft is changing the authentication mechanism that is supported by Exchange Online to use OAuth-based
                                             authentication only. After the change, if you want to deploy calendar integration between the IM and Presence Service and
                                             Office 365, you will need to upgrade the IM and Presence Service to Release 12.5(1)SU2. This change will not affect integration
                                             with an on-premises Exchange server. |
| Note | As of October 2020, Microsoft is changing the authentication mechanism that is supported by Exchange Online to use OAuth-based
                                             authentication only. After the change, if you want to deploy calendar integration between the IM and Presence Service and
                                             Office 365, you will need to upgrade the IM and Presence Service to Release 12.5(1)SU2. This change will not affect integration
                                             with an on-premises Exchange server. |
| Active Directory | Active Directory 2016 with Windows Server 2016 Note User names configured in Active Directory must be identical to those names defined in Unified Communications Manager. | Note | User names configured in Active Directory must be identical to those names defined in Unified Communications Manager. |
| Note | User names configured in Active Directory must be identical to those names defined in Unified Communications Manager. |
| A Third-Party Certificate OR Certificate Server | One or the other of these are required to generate the certificates. Note Microsoft Exchange integration with IM and Presence Service supports certificates using RSA 1024 or 2048-bit keys and SHA1
                                                and SHA256 signature algorithms. | Note | Microsoft Exchange integration with IM and Presence Service supports certificates using RSA 1024 or 2048-bit keys and SHA1
                                                and SHA256 signature algorithms. |
| Note | Microsoft Exchange integration with IM and Presence Service supports certificates using RSA 1024 or 2048-bit keys and SHA1
                                                and SHA256 signature algorithms. |

| Note | As of October 2020, Microsoft is changing the authentication mechanism that is supported by Exchange Online to use OAuth-based
                                             authentication only. After the change, if you want to deploy calendar integration between the IM and Presence Service and
                                             Office 365, you will need to upgrade the IM and Presence Service to Release 12.5(1)SU2. This change will not affect integration
                                             with an on-premises Exchange server. |
|---|---|

| Note | User names configured in Active Directory must be identical to those names defined in Unified Communications Manager. |
|---|---|

| Note | Microsoft Exchange integration with IM and Presence Service supports certificates using RSA 1024 or 2048-bit keys and SHA1
                                                and SHA256 signature algorithms. |
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

| Note | SIP federation and Remote Call Control (RCC) do not work together on
                                    			 the same IM and Presence Service cluster. This is because for SIP federation a
                                    			 user cannot be licensed for both Cisco IM and Presence Service and Microsoft
                                    			 Lync/OCS, but for RCC a user must be licensed for Cisco IM and Presence Service
                                    			 and Microsoft Lync/OCS at the same time. |
|---|---|

| Note | An IM and Presence Service cluster that is used for RCC does not support Jabber or other IM and Presence Service functionality. |
|---|---|