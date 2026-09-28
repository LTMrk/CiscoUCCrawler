---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-rel-notes-15-su2-cucm-b-release-notes-for-cucm-imp-15su2-html-b8aa770ae6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/15/SU2/cucm_b_release-notes-for-cucm-imp-15su2.html
retrieved_at: 2026-09-01T15:33:48.674016+00:00
---

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service Release 15SU2

# Release Notes for Cisco Unified Communications Manager and the IM and Presence Service Release 15SU2

- 15SU2

- 15

### Download Options

Updated: December 4, 2024

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service Release 15SU2

First Published: October 1, 2024

Last Updated: December 4, 2024

# About Release Notes

This release describes new features, restrictions, and caveats for Cisco Unified Communications Manager ( Unified Communications Manager ) and Cisco Unified Communications Manager IM and Presence Service ( IM and Presence Service ) . The release notes are updated for every maintenance release but not for patches or hot fixes.

## Supported Versions

The following software versions apply to:

Unified Communications Manager : 15.0.1.12900-234

IM and Presence Service : 15.0.1.12900-10

### Version Compatibility Between Unified CM and the IM and Presence Service

Version compatibility depends on the IM and Presence Service deployment type. The following table outlines the options and whether a release mismatch is supported between the telephony
                        deployment and the IM and Presence Service deployment. A release mismatch, if it is supported, would let you deploy your Unified Communications Manager telephony deployment and your IM and Presence Service deployment using different releases.

Any respin or ES that is produced between Cisco.com releases is considered part of the previous release. For example, a Unified Communications Manager ES with a build number
                                 of 15.0.1.14[0-2]xx would be considered part of the 15SU1 (15.0.1.11900-x) release.

Deployment Type

Release Mismatch

Description

Standard Deployment of IM and Presence Service

Not supported

Unified Communications Manager and the IM and Presence Service are in the same cluster and must run on the same release—a release mismatch is not supported.

Centralized Deployment of IM and Presence Service

Supported

The IM and Presence Service deployment and the telephony deployment are in different clusters and can run on different releases—a release mismatch is
                                    supported.

The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning. This non-telephony
                                             node must run on the same release as the IM and Presence Service .

Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onwards.

## Documentation for this Release

For a complete list of the documentation that is available for this release, see the Documentation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 15 .

## Installation Procedures

For information on how to install your system, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service .

## Upgrade Procedures

For information on how to upgrade to this release, see the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 15 .

## New and Changed Features

### Centralized Call History for Webex App

Webex App users, while using Unified Communications Manager for Calling, can only access the local call history. This creates inconsistency across devices in the shared line case when
                     the users are not logged into the App. One of the concerns is that users cannot receive missed call notifications in such
                     situations and must check different devices to find the call history and call back.

With this release, we are enabling the Webex App to use a centralized call history. This eliminates the previously mentioned
                     inconsistencies and provides a better user experience. This feature is supported from Webex 44.11 onwards.

To use this feature, you must onboard the Unified Communications Manager node through Webex Cloud-Connected UC. For more information, see Set up Webex Cloud-Connected UC for on-premises devices .

### Unified CM Enhancements To Optimize MTP Insertion in IPv4/IPv6 SME Case

From Release 15SU2 onwards, the IP Addressing Mode Preference for Media enterprise parameter is overridden when calls are
                     made over an SME cluster to a dual-stack supported device. The destination cluster sends both the IP addresses (IPv4 and IPv6)
                     for all media lines in its offer SDP to the subsequent Unified CM servers. This reduces the chances of MTP allocation due
                     to IP mode mismatch.

For more information, see the 'Configure IP Addressing Preference for Cluster' section in the "Configure IPv6 Stack" chapter
                     of the System Configuration Guide for Cisco Unified Communications Manager .

### Enhanced Accessibility and Usability in User Interfaces

As an ongoing effort to improve accessibility improvements, the Self Care Portal is enhanced with the following for this release:

Introduction to sitemap helps users to navigate to the pages and files that are important in the Self Care Portal. Sitemap
                           provides links to the main phone functionalities in the portal for easy navigation.

Fixing of critical issues that are related to keyboard navigation and screen reader announcements.

### External Database Clean-up Utility Revamp

The External Database Clean-up Utility interface in the IM and Presence Service is enhanced for easier and more productive
                     use by administrators. The enhancements include a new landing page for easier access to the clean-up jobs and a clear division
                     between manual and automatic clean-up jobs. In addition, it includes the capability to individually configure and track the
                     life cycle of the automatic clean-up job for the IM and Presence Service clusters.

For more information, see the Online Help and Database Setup Guide for the IM and Presence Service, Release 15 and SUs .

### Inclusive Language Improvements

As part of this release, improvements have been made to the user interfaces to use inclusive language. For more information
                     on Inclusive Language policies and considerations throughout for any Cisco products see, Inclusive Language policies and considerations throughout for any Cisco products .

### Multi Line Support for Webex App on Mobile

The multi line support feature for UCM Calling allows administrators to configure multiple phone numbers for a single user.
                     You can assign these numbers to the user’s Webex App and devices, with each number independently being able to make and receive
                     calls. Currently, the maximum number of phone numbers that can be assigned to a mobile Webex application is eight. This capability
                     enables users to manage multiple calls simultaneously, thus enhancing efficiency, and productivity. This feature is supported
                     from Webex 44.12 onwards.

Previously, we supported this feature exclusively on the desktop version of the Webex App. With the latest release, we are
                     extending support to the mobile version as well. Mobility is a crucial aspect of enterprise calling because it ensures that
                     users remain connected and productive while on the move.

The maximum number of phone numbers that can be assigned to a desktop Webex application is enhanced from eight to ten. Download
                                 and install the cmterm-webex-desktop-10-Lines-241115.k4.cop.sha512 COP file from CCO to use this enhancement.

Mobile users having Mobile Identity (MI) configured cannot place or receive calls. Install the ciscocm.V15SU2_CSCwm77174-multiline_v1.zip file from CCO to use this feature.

### Presence Gateway Integration with Office 365

From this release, IM and Presence Service's Calendar Integration with Office 365 feature is enhanced to allow configurable AD Authentication Endpoint and Resource URI values. This is achieved through the AD Authentication Endpoint and Resource URI fields which are introduced in the Presence
                     Gateway Configuration page. These fields are auto populated with default values which can be modified as required.

For more information, see the ‘Configure a Presence Gateway’ section of the Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 15 and SUs .

### Single Sign-On Service Provider Enhancements

With this release, Unified Communications Manager has mandated that you can enable or disable SAML SSO only if the DB services
                     are up and running across all the nodes in the cluster.

Run the utils service list administrative command (A Cisco DB) that retrieves the list of all services to check the DB status.

### Smart Receiver Transport

From this release, Call Home as a transport mode for smart licensing is deprecated. Smart Transport mode, the new transport
                     mode, is introduced for smart licensing. All freshly installed Unified Communications Manager nodes support only Smart Transport.

Post upgrade or migration, Unified Communications Manager automatically switches to Smart Transport if connection to the endpoints
                     “smartreceiver.cisco.com” is successful. In case of connection failure, Unified CM falls back to the Call Home mode.

For more information, see the System Configuration Guide for Cisco Unified Communications Manager .

### Support for Tertiary CTI Manager and Fallback

Before this release, Cisco TSP enabled you to configure only a primary and secondary CTI Manager. From this release onwards,
                     Cisco TSP enables you to configure a tertiary CTI Manager. When the tertiary CTI Manager is configured, it is treated as the
                     least priority server. Cisco TSP connects to it only when connectivity to both the primary and secondary CTI Managers is lost.
                     The TSP remains connected to tertiary by default unless you have explicitly enabled and configured a valid choice for fallback
                     settings.

For more information, see the ‘Support for Tertiary CTI Manager and Fallback’ section in the "Overview" chapter of the Cisco Unified TAPI Developers Guide for Cisco Unified Communications Manager Release .

### Support for Transport Layer Security (TLS) 1.3

TLS 1.3 is the highest version of the Transport Layer Security (TLS) protocol supported from this release onwards.

TLS 1.3 is faster and more secure than older versions of TLS. One of the key improvements in TLS 1.3 is the reduction in handshake
                     latency. It significantly enhances the performance of time-sensitive applications. Moreover, TLS 1.3 also reduces round-trip
                     times (RTT), by further optimizing the connection establishment process. TLS 1.3 has dropped support for older and less secure
                     cryptographic algorithms.

For more information about the TLS 1.3 support limitations on IM and Presence Service, see the 'Set Minimum TLS Version' section
                     in the "TLS 1.3 Setup" chapter of the Security Guide for Cisco Unified Communications Manager, Release 15 and SUs .

## Important Notes

### Cisco Desk Phone 9800 Series Requirements

Cisco Unified Communications Manager (Unified Communications Manager) requirements for the Cisco Desk Phone 9800 Series include:

Unified Communications Manager 12.5(1)SU9, 14SU4 and later, or 15SU2 and later (To be FCSed around October 2024).

Installation of the following Cisco Options Package (COP) files on Unified Communications Manager: Phone firmware —Firmware for the Cisco Desk Phone 9800 Series phones is not bundled with Unified Communications Manager. A firmware update
                           may be required to enable the new features. The phone firmware COP files can be downloaded from Cisco.com .

For information on the list of supported features for the Cisco Desk Phone 9800 Series, see the Release Notes for Cisco Desk Phone 9800 Series .

### Interoperability Issues Between LBM Interclusters

Location Bandwidth Manager (LBM) running on Unified Communication Manager version 15 cannot communicate with Unified CM versions
                     with a newer version of Release 15 (for example, Release 15 SU1 or later). Hence, we recommend that you do the following if
                     you are using LBM across multiple clusters:

Ensure that you install the ciscocm.V15FCS_CSCwi82830-lbm_C0211-1.cop.sha512 COP file on Unified Communications Manager Release 15 to interoperate with LBM running on Unified Communication Manager versions
                           15SU1 or later.

### Deprecation of Remote Call Control with Microsoft Lync Server for IM and Presence Service

Unified Communications Manager Release 15 does not support Remote Call Control with Microsoft Lync Server for IM and Presence Service . If you are using this feature currently in your deployment and you are trying to upgrade to Release 15, you cannot use this
                     feature after the upgrade.

This feature continues to be supported in Releases 12.5.x and 14 and SUs until their EOL/EOS.

For more information, see Deprecation of Remote Call Control with Microsoft Lync Server for IM and Presence Service on Cisco Unified Communications
                        Manager, Release 15 .

### Remove Deprecated Device Firmware from ISO

Starting with Release 15 onwards, phone firmware that is end of support will no longer be included in the Unified Communications Manager ISO. These endpoints will still be allowed to register, unless they have been officially deprecated, but the firmware will
                     not be present in the TFTP directory following a fresh install. For more details, see the ReadMe for Cisco Unified Communications Manager .

### New 2021 Signing Key

Attention

Release 14SU1 and onwards is signed with a new 2021 signing key. It is possible that you may need to install the ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn
                                 COP file first if upgrading from Unified Communications Manager versions prior to Release 14. See the COP file readme for
                                 specifics.

This release also removes support for the previous signing key. If you are installing phone firmware, ensure that you use
                                 the files with k4.cop.sha512 in the name, as these files are also signed with the new signing key. Installing files signed
                                 with the previous signing key results in a "The selected file is not valid." error during installation.

### Secure SIP Line Support for Cisco VG410 Analog Voice Gateway

From this release onwards, Unified Communications Manager supports secure SIP Lines for Cisco VG410 Analog Voice Gateway that
                     are running on Cisco IOS XE 17.15.1 or above version.

### Simplifying Release Number Scheme

From Release 14 onwards, Cisco Unified Communications Manager has adopted the single number release plan. There will be no
                        (dot) releases like (dot five) in the past release versions. Service Update releases will be published on top of the main
                        major release 14 through the regular Software Maintenance cycle.

### New Cisco Gateway Support

New releases of Unified Communications Manager have introduced support for the following Cisco gateways:

Cisco VG400 Analog Voice Gateway

Cisco VG410 Analog Voice Gateway (Using only the Gateway Configuration window from Cisco Unified Communications Manager Administration Graphical User Interface)

Cisco VG420 Analog Voice Gateway

Cisco VG450 Analog Voice Gateway

Cisco 4461 Integrated Services Router

The following table lists supported gateway models and the initial release, by release category, where support was introduced.
                        Within each release category (for example, 11.5(x) and 12.5(x)), support for the gateway model is added as of the specified
                        release, along with later releases in that category. For these releases, you can select the gateway in the Gateway Configuration window of Unified Communications Manager .

Gateway Model

11.5(x) Releases

12.5(x) Releases

14(x) Releases

15(x) Releases

Cisco VG 202, 202 XM, 204, 204 XM, 310, 320, 350 Analog Voice Gateway

11.5(1) and later

12.5(1) and later

14 and later

15 and later

Cisco VG400 Analog Voice Gateway

11.5(1)SU7 and later

12.5(1) and later

14 and later

15 and later

Cisco VG410 Analog Voice Gateway

Not supported

Not supported

14SU3 and later

15 and later

Cisco VG420 Analog Voice Gateway

Not supported

12.5(1)SU4 and later

14SU1 and later

15 and later

Cisco VG450 Analog Voice Gateway

11.5(1)SU6 and later

12.5(1) and later

14 and later

15 and later

Cisco 4321, 4331 4351, 4431, 4451 Integrated Services Router

11.5(1) and later

12.5(1) and later

14 and later

15 and later

Cisco 4461 Integrated Services Router

11.5(1)SU6 and later

12.5(1) and later

14 and later

15 and later

Cisco Catalyst 8300 Series Edge Platforms

—

12.5(1)SU4 and later

14 and later

15 and later

#### Cisco Analog Telephone Adapters

Cisco Analog Telephone Adapters connect analog devices, such as an analog phone or fax machine, to your network. These devices
                        can be configured via the Phone Configuration window. The following table highlights model support for the ATA series.

ATA Adapter

11.5(x) Releases

12.5(x) Releases

14(x) Releases

15(x) Releases

Cisco ATA 191 Analog Telephone Adapter

11.5(1)SU4 and later

12.5(1) and later

14 and later

15 and later

Cisco ATA 190 Analog Telephone Adapter is EOS/EOL Notice .

## Caveats

### Bug Search Tool

The system grades known problems (bugs) per severity level. These release notes contain descriptions of the following bug
                     levels:

All severity level 1 or 2 bugs

Significant severity level 3 bugs

All customer-found bugs

You can search for open and resolved caveats of any severity for any release using the Cisco Bug Search tool, an online tool
                     available for customers to query defects according to their own needs.

To access the Cisco Bug Search tool, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Follow these steps to use Cisco Bug Search tool:

Access the Cisco Bug Search tool: https://bst.cloudapps.cisco.com/bugsearch .

Log in with your Cisco.com user ID and password.

If you are looking for information about a specific problem, enter the bug ID number in the Search for: field and click Go .

Tip

Click Help on the Bug Search page for information about how to search for bugs, create saved searches, and create bug groups.

### Caveats for 15SU2

You can search for defects in the Bug Search Tool at https://bst.cloudapps.cisco.com/bugsearch/ .

For a list of Open Caveats and Resolved Caveats, see the respective Readme files:

ReadMe for Cisco Unified Communications Manager, Release 15SU2

ReadMe for Cisco Unified IM and Presence, Release 15SU2

| Note | Any respin or ES that is produced between Cisco.com releases is considered part of the previous release. For example, a Unified Communications Manager ES with a build number
                                 of 15.0.1.14[0-2]xx would be considered part of the 15SU1 (15.0.1.11900-x) release. |
|---|---|

| Deployment Type | Release Mismatch | Description |
|---|---|---|
| Standard Deployment of IM and Presence Service | Not supported | Unified Communications Manager and the IM and Presence Service are in the same cluster and must run on the same release—a release mismatch is not supported. |
| Centralized Deployment of IM and Presence Service | Supported | The IM and Presence Service deployment and the telephony deployment are in different clusters and can run on different releases—a release mismatch is
                                    supported. Note The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning. This non-telephony
                                             node must run on the same release as the IM and Presence Service . Note Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onwards. | Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning. This non-telephony
                                             node must run on the same release as the IM and Presence Service . | Note | Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onwards. |
| Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning. This non-telephony
                                             node must run on the same release as the IM and Presence Service . |
| Note | Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onwards. |

| Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning. This non-telephony
                                             node must run on the same release as the IM and Presence Service . |
|---|---|

| Note | Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onwards. |
|---|---|

| Note | The maximum number of phone numbers that can be assigned to a desktop Webex application is enhanced from eight to ten. Download
                                 and install the cmterm-webex-desktop-10-Lines-241115.k4.cop.sha512 COP file from CCO to use this enhancement. Mobile users having Mobile Identity (MI) configured cannot place or receive calls. Install the ciscocm.V15SU2_CSCwm77174-multiline_v1.zip file from CCO to use this feature. |
|---|---|

| Note | This feature continues to be supported in Releases 12.5.x and 14 and SUs until their EOL/EOS. |
|---|---|

| Attention | Release 14SU1 and onwards is signed with a new 2021 signing key. It is possible that you may need to install the ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn
                                 COP file first if upgrading from Unified Communications Manager versions prior to Release 14. See the COP file readme for
                                 specifics. This release also removes support for the previous signing key. If you are installing phone firmware, ensure that you use
                                 the files with k4.cop.sha512 in the name, as these files are also signed with the new signing key. Installing files signed
                                 with the previous signing key results in a "The selected file is not valid." error during installation. |
|---|---|

| Gateway Model | 11.5(x) Releases | 12.5(x) Releases | 14(x) Releases | 15(x) Releases |
|---|---|---|---|---|
| Cisco VG 202, 202 XM, 204, 204 XM, 310, 320, 350 Analog Voice Gateway | 11.5(1) and later | 12.5(1) and later | 14 and later | 15 and later |
| Cisco VG400 Analog Voice Gateway | 11.5(1)SU7 and later | 12.5(1) and later | 14 and later | 15 and later |
| Cisco VG410 Analog Voice Gateway | Not supported | Not supported | 14SU3 and later | 15 and later |
| Cisco VG420 Analog Voice Gateway | Not supported | 12.5(1)SU4 and later | 14SU1 and later | 15 and later |
| Cisco VG450 Analog Voice Gateway | 11.5(1)SU6 and later | 12.5(1) and later | 14 and later | 15 and later |
| Cisco 4321, 4331 4351, 4431, 4451 Integrated Services Router | 11.5(1) and later | 12.5(1) and later | 14 and later | 15 and later |
| Cisco 4461 Integrated Services Router | 11.5(1)SU6 and later | 12.5(1) and later | 14 and later | 15 and later |
| Cisco Catalyst 8300 Series Edge Platforms | — | 12.5(1)SU4 and later | 14 and later | 15 and later |

| ATA Adapter | 11.5(x) Releases | 12.5(x) Releases | 14(x) Releases | 15(x) Releases |
|---|---|---|---|---|
| Cisco ATA 191 Analog Telephone Adapter | 11.5(1)SU4 and later | 12.5(1) and later | 14 and later | 15 and later |

| Note | Cisco ATA 190 Analog Telephone Adapter is EOS/EOL Notice . |
|---|---|

| Tip | Click Help on the Bug Search page for information about how to search for bugs, create saved searches, and create bug groups. |
|---|---|