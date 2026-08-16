---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-rel-notes-14-0-1-su4-cucm-b-release-notes-for-cucm-imp-14su4-html-7a0aa57507
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/14_0_1/SU4/cucm_b_release-notes-for-cucm-imp-14su4.html
retrieved_at: 2026-08-16T17:52:34.323172+00:00
---

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service Release 14SU4a

# Release Notes for Cisco Unified Communications Manager and the IM and Presence Service Release 14SU4a

### Download Options

Updated: June 10, 2024

Release Notes for Cisco Unified Communications Manager and the IM and Presence Service Release 14SU4a

First Published: May 30, 2024

Last Updated: June 10, 2024

# About Release Notes

This release describes new features, restrictions, and caveats for Cisco Unified Communications Manager ( Unified Communications Manager ) and Cisco Unified Communications Manager IM and Presence Service ( IM and Presence Service ) . The release notes are updated for every maintenance release but not for patches or hot fixes.

## Supported Versions

The following software versions apply to:

Unified Communications Manager Release 14SU4a: 14.0.1.14901-1

IM and Presence Service Release 14SU4: 14.0.1.14900-4

### Version Compatibility Between Unified CM and the IM and Presence Service

Version compatibility depends on the IM and Presence Service deployment type. The following table outlines the options and
                        whether a release mismatch is supported between the telephony deployment and the IM and Presence Service deployment. A release
                        mismatch, if it is supported, would let you deploy your Unified Communications Manager telephony deployment and your IM and
                        Presence Service deployment using different releases.

Any respin or ES that is produced between Cisco.com releases is considered part of the previous release. For example, a Unified Communications Manager ES with a build number
                                 of 14.0.1.14[0-2]xx would be considered part of the 14SU4a (14.0.1.14901-x) release.

Deployment Type

Release Mismatch

Description

Standard Deployment of IM and Presence Service

Not supported

Unified Communications Manager and the IM and Presence Service are in the same cluster and must run the same release—a release
                                    mismatch is not supported.

Centralized Deployment of IM and Presence Service

Supported

The IM and Presence Service deployment and the telephony deployment are in different clusters and can run on different releases—a
                                    release mismatch is supported.

The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                             This non-telephony node must run on the same release as the IM and Presence Service.

Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onwards.

## Documentation for this Release

For a complete list of the documentation that is available for this release, see the Documentation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 14 .

## Installation Procedures

For information on how to install your system, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service .

## Upgrade Procedures

For information on how to upgrade to this release, see the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 14 .

## New and Changed Features

### Centralized Call History for Webex App

Webex App users, while using Unified Communications Manager for Calling, can only access the local call history. This creates inconsistency across devices in the shared line case when
                     the users are not logged into the App. One of the concerns is that users cannot receive missed call notifications in such
                     situations and must check different devices to find the call history and call back.

With this release, we are enabling the Webex App to use a centralized call history. This eliminates the previously mentioned
                     inconsistencies and provides a better user experience.

To use this feature, the Unified Communications Manager node must be onboarded through Webex Cloud-Connected UC. For more
                     information, see Set up Webex Cloud-Connected UC for on-premises devices .

### Smart Receiver Transport

From this release, Call Home as a transport mode for smart licensing is deprecated. Smart Transport mode, the new transport
                     mode, is introduced for smart licensing. All freshly installed Unified Communications Manager nodes support only Smart Transport.

Post upgrade or migration, Unified Communications Manager automatically switches to Smart Transport if connection to the endpoints
                     “smartreceiver.cisco.com” is successful. In case of connection failure, Unified CM falls back to the Call Home mode.

For more information, see the System Configuration Guide for Cisco Unified Communications Manager .

### Automatic Renewal of Refresh Token for Webex Clients

Unified Communications Manager supports the automatic renewal of refresh token for Webex clients. This feature introduces a new enterprise parameter ‘ Auto Renew Refresh Token ’ that is enabled by default.

For more information, see:

System Parameters Task Flow section of the 'Configure Enterprise Parameters and Services' chapter in the System Configuration Guide for Cisco Unified Communications Manager

OAuth Framework section of the 'Identity Management' chapter in the Security Guide for Cisco Unified Communications Manager

### Managed File Transfer User Authentication Enhancement

The IM and Presence Service SSH public key is extended from 2048 bits to 4096 bits, for enhanced security when establishing
                     connections with the External File Server.

For configuration information, see the "Configure Managed File Transfer" chapter in the Configuration and Administration of the IM and Presence Service Guide .

## Important Notes

### Simplifying Release Number Scheme

From Release 14 onwards, Cisco Unified Communications Manager has adopted the single number release plan. There will be no
                        (dot) releases like (dot five) in the past release versions. Service Update releases will be published on top of the main
                        major release 14 through the regular Software Maintenance cycle.

### SIP Secure Phone Registration

From 14SU2 release onwards, memory usage increases for SIP secure phone registrations although it does not impact the server
                        capacity in most of the deployments.

### New 2021 Signing Key

Attention

Release 14SU1 and onwards is signed with a new 2021 signing key. It is possible that you may need to install the ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn
                                 COP file first if upgrading from Unified Communications Manager versions prior to Release 14. See the COP file readme for
                                 specifics.

This release also removes support for the previous signing key. If you are installing phone firmware, ensure that you use
                                 the files with k4.cop.sha512 in the name, as these files are also signed with the new signing key. Installing files signed
                                 with the previous signing key results in a "The selected file is not valid." error during installation.

### New Cisco Gateway Support

New releases of Unified Communications Manager have introduced support for the following Cisco gateways:

Cisco VG400 Analog Voice Gateway

Cisco VG410 Analog Voice Gateway (Using only the Gateway Configuration window from Cisco Unified Communications Manager Administration Graphical User Interface)

Cisco VG420 Analog Voice Gateway

Cisco VG450 Analog Voice Gateway

Cisco 4461 Integrated Services Router

The following table lists supported gateway models and the initial release, by release category, where support was introduced.
                        Within each release category (for example, 11.5(x) and 12.5(x)), support for the gateway model is added as of the specified
                        release, along with later releases in that category. For these releases, you can select the gateway in the Gateway Configuration window of Unified Communications Manager.

Gateway Model

11.5(x) Releases

12.5(x) Releases

14(x) Releases

Cisco VG 202, 202 XM, 204, 204 XM, 310, 320, 350 Analog Voice Gateway

11.5(1) and later

12.5(1) and later

14 and later

Cisco VG400 Analog Voice Gateway

11.5(1)SU7 and later

12.5(1) and later

14 and later

Cisco VG410 Analog Voice Gateway

Not supported

Not supported

14SU3 and later

Cisco VG420 Analog Voice Gateway

Not supported

12.5(1)SU4 and later

14SU1 and later

Cisco VG450 Analog Voice Gateway

11.5(1)SU6 and later

12.5(1) and later

14 and later

Cisco 4321, 4331 4351, 4431, 4451 Integrated Services Router

11.5(1) and later

12.5(1) and later

14 and later

Cisco 4461 Integrated Services Router

11.5(1)SU6 and later

12.5(1) and later

14 and later

Cisco Catalyst 8300 Series Edge Platforms

—

12.5(1)SU4 and later

14 and later

#### Cisco Analog Telephone Adapters

Cisco Analog Telephone Adapters connect analog devices, such as an analog phone or fax machine, to your network. These devices
                        can be configured via the Phone Configuration window. The following table highlights model support for the ATA series.

ATA Adapter

11.5(x) Releases

12.5(x) Releases

14(x) Releases

Cisco ATA 190 Analog Telephone Adapter

11.5(1) and later

12.5(1) and later

14 and later

Cisco ATA 191 Analog Telephone Adapter

11.5(1)SU4 and later

12.5(1) and later

14 and later

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

### Caveats

You can search for defects in the Bug Search Tool at https://bst.cloudapps.cisco.com/bugsearch/ .

For a list of Open Caveats and Resolved Caveats, see the respective Readme files:

ReadMe for Cisco Unified Communications Manager, Release 14SU4a

ReadMe for Cisco Unified IM and Presence, Release 14SU4

| Note | Any respin or ES that is produced between Cisco.com releases is considered part of the previous release. For example, a Unified Communications Manager ES with a build number
                                 of 14.0.1.14[0-2]xx would be considered part of the 14SU4a (14.0.1.14901-x) release. |
|---|---|

| Deployment Type | Release Mismatch | Description |
|---|---|---|
| Standard Deployment of IM and Presence Service | Not supported | Unified Communications Manager and the IM and Presence Service are in the same cluster and must run the same release—a release
                                    mismatch is not supported. |
| Centralized Deployment of IM and Presence Service | Supported | The IM and Presence Service deployment and the telephony deployment are in different clusters and can run on different releases—a
                                    release mismatch is supported. Note The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                             This non-telephony node must run on the same release as the IM and Presence Service. Note Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onwards. | Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                             This non-telephony node must run on the same release as the IM and Presence Service. | Note | Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onwards. |
| Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                             This non-telephony node must run on the same release as the IM and Presence Service. |
| Note | Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onwards. |

| Note | The IM and Presence Service central cluster also includes a standalone Unified CM publisher node for database and user provisioning.
                                             This non-telephony node must run on the same release as the IM and Presence Service. |
|---|---|

| Note | Centralized Deployment is supported for the IM and Presence Service from Release 11.5(1)SU4 onwards. |
|---|---|

| Attention | Release 14SU1 and onwards is signed with a new 2021 signing key. It is possible that you may need to install the ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn
                                 COP file first if upgrading from Unified Communications Manager versions prior to Release 14. See the COP file readme for
                                 specifics. This release also removes support for the previous signing key. If you are installing phone firmware, ensure that you use
                                 the files with k4.cop.sha512 in the name, as these files are also signed with the new signing key. Installing files signed
                                 with the previous signing key results in a "The selected file is not valid." error during installation. |
|---|---|

| Gateway Model | 11.5(x) Releases | 12.5(x) Releases | 14(x) Releases |
|---|---|---|---|
| Cisco VG 202, 202 XM, 204, 204 XM, 310, 320, 350 Analog Voice Gateway | 11.5(1) and later | 12.5(1) and later | 14 and later |
| Cisco VG400 Analog Voice Gateway | 11.5(1)SU7 and later | 12.5(1) and later | 14 and later |
| Cisco VG410 Analog Voice Gateway | Not supported | Not supported | 14SU3 and later |
| Cisco VG420 Analog Voice Gateway | Not supported | 12.5(1)SU4 and later | 14SU1 and later |
| Cisco VG450 Analog Voice Gateway | 11.5(1)SU6 and later | 12.5(1) and later | 14 and later |
| Cisco 4321, 4331 4351, 4431, 4451 Integrated Services Router | 11.5(1) and later | 12.5(1) and later | 14 and later |
| Cisco 4461 Integrated Services Router | 11.5(1)SU6 and later | 12.5(1) and later | 14 and later |
| Cisco Catalyst 8300 Series Edge Platforms | — | 12.5(1)SU4 and later | 14 and later |

| ATA Adapter | 11.5(x) Releases | 12.5(x) Releases | 14(x) Releases |
|---|---|---|---|
| Cisco ATA 190 Analog Telephone Adapter | 11.5(1) and later | 12.5(1) and later | 14 and later |
| Cisco ATA 191 Analog Telephone Adapter | 11.5(1)SU4 and later | 12.5(1) and later | 14 and later |

| Tip | Click Help on the Bug Search page for information about how to search for bugs, create saved searches, and create bug groups. |
|---|---|