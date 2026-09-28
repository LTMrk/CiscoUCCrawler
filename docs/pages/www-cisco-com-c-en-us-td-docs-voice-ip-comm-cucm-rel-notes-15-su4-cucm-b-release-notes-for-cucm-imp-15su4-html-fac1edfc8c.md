---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-rel-notes-15-su4-cucm-b-release-notes-for-cucm-imp-15su4-html-fac1edfc8c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/15/SU4/cucm_b_release-notes-for-cucm-imp-15su4.html
retrieved_at: 2026-08-16T17:51:44.247660+00:00
---

Release Notes for Cisco Unified Communications Manager Release 15SU4a and the IM and Presence Service Release 15SU4

# Release Notes for Cisco Unified Communications Manager Release 15SU4a and the IM and Presence Service Release 15SU4

### Download Options

Updated: March 17, 2026

### Release Notes for Cisco Unified Communications Manager Release 15SU4a and the IM and Presence Service Release 15SU4

First Published: January 29, 2026

Last Updated: March 17, 2026

# About Release Notes

This release describes new features, restrictions, and caveats for Cisco Unified Communications Manager ( Unified Communications Manager ) and Cisco Unified Communications Manager IM and Presence Service ( IM and Presence Service ) . The release notes are updated for every maintenance release but not for patches or hot fixes.

## Supported Versions

The following software versions apply to:

Unified Communications Manager Release 15SU4a: 15.0.1.14901-2

IM and Presence Service Release 15SU4: 15.0.1.14900-8

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

### Enhanced Accessibility in User Interfaces

As an ongoing effort to improve accessibility improvements, the Cisco Unified CM Administration, Cisco Unified Reporting,
                     Cisco Unified Serviceability, Cisco Unified OS Admin, Disaster Recovery System, Cisco Unified IM and Presence Serviceability,
                     Cisco Unified IM and Presence OS Administration, Cisco Unified IM and Presence Reporting, and IM and Presence Disaster Recovery
                     System user interfaces are enhanced with the following functionality for this release:

Sitemap —Helps users navigate to important pages within each user interface. The Sitemap provides links to main functionalities for
                           easy navigation.

User Interface Menu —The menu opens only when you click it with a mouse or use the Enter or Spacebar keys on the keyboard; it does not open on
                           hover.

### Microsoft Office 365 Calendaring Integration with IM and Presence Service

Starting with Release 15SU4, Cisco Unified Communications Manager IM and Presence Service migrates from Exchange Web Services
                     (EWS) to Microsoft Graph APIs for Office 365 integration. This change ensures continued support for calendaring features,
                     which allow 'In a Meeting' and 'Out of Office' presence statuses.

During the upgrade, the IM and Presence Service automatically updates standard commercial and U.S. Government EWS endpoint
                     URLs to Microsoft Graph URLs.

The migration to Microsoft Graph API applies only to Microsoft Office 365; integration with on-premises Exchange Server continues
                                 to use EWS APIs for calendaring.

For more information, see the Microsoft Outlook Calendar Integration for the IM and Presence Service .

### New Hypervisor Support for On-premises Calling Solutions

Cisco Unified Communications Manager Release 15SU4 introduces support for additional virtualization options. In addition to
                     VMware vSphere ESXi, Release 15SU4 supports Cisco NFVIS-for-UC and Cisco Compute Hyperconverged with Nutanix (CCHN) for on-premises
                     calling deployments. These additions allow on-premises customers to choose between traditional VMware support, a Cisco-native
                     virtualization layer for appliances, or a robust hyperconverged infrastructure (HCI) solution.

Cisco NFVIS-for-UC (Network Function Virtualization Infrastructure Software for Unified Communications) —Cisco NFVIS is a limited-purpose virtualization product from the Cisco networking portfolio that supports hosting Virtual
                           Network Functions (VNFs) on select Cisco network and server hardware. Cisco NFVIS-for-UC is a specialized edition of NFVIS
                           that supports hosting core calling applications on select Cisco calling appliances.

Cisco NFVIS-for-UC is a special edition of NFVIS that introduces a new commercial offer with a separate product ID, distinct
                           pricing, new licensing, and a slightly different administrative GUI.

Cisco NFVIS-for-UC supports only select on-premises calling applications.

Cisco NFVIS-for-UC supports only select Cisco Calling Appliances.

Supported Applications : Cisco Unified Communications Manager, Dedicated Instance Enhanced Survivability Node (ESN), Cisco Unified Communications
                                 Manager Session Management Edition, Cisco Unified Communications Manager IM and Presence Service, Cisco Unity Connection,
                                 Cisco Emergency Responder, and Cisco Expressway. Other workloads (including the remainder of the Collaboration portfolio,
                                 other Cisco products, third-party applications, or homegrown applications) are not supported.

Supported Hardware : Cisco Business Edition 6000 (M5, M6, M7), Cisco Business Edition 7000 (M5, M6, M7), and Cisco Expressway CE1400V (M7).

Minimum Requirements : Release 15SU4 (or X15.4 for Expressway) running on Cisco NFVIS-for-UC version 4.18.2a.

Key Benefits : Provides a Cisco-on-Cisco, appliance-based solution tailored for collaboration-centric customer needs.

Cisco Compute Hyperconverged with Nutanix (CCHN) —Cisco Compute Hyperconverged with Nutanix (CCHN) is a joint solution that integrates Nutanix software with Cisco hardware.
                           This software-defined system integrates compute, storage, and networking into a single platform.

Supported Applications : Cisco Unified Communications Manager, Dedicated Instance Enhanced Survivability Node (ESN), Cisco Unified Communications
                                 Manager Session Management Edition, Cisco Unified Communications Manager IM and Presence Service, Cisco Unity Connection,
                                 Cisco Emergency Responder, and Cisco Expressway. Other workloads (including the remainder of the Collaboration portfolio,
                                 other Cisco products, third-party applications, or homegrown applications) are not supported.

Supported Hardware : Cisco HCI Nodes and Cisco Compute Nodes (integrated with Cisco HCI nodes) based on HCI, HCIX, and UCS hardware as described
                                 in the Cisco Compute Hyperconverged with Nutanix Data Sheets.

Minimum Requirements : Release 15SU4 (or X15.4 for Expressway) running on Nutanix Acropolis Hypervisor (AHV) 10.0 and Nutanix Acropolis OS (AOS)
                                 7.0.

Key Benefits : Provides a robust hyperconverged infrastructure platform for data center-centric customer needs.

VMware vSphere ESXi —VMware vSphere ESXi 8.0 continues to be supported. Note that ESXi 7.0 and earlier releases have reached the end of support
                           from VMware by Broadcom.

For more information, see:

Virtualization Guide : Cisco Virtualization Guide for Cisco On-premises Calling Applications

Installation Guides : Refer to the specific 'Installation Guides' for Cisco Unified Communications Manager, Dedicated Instance Enhanced Survivability
                           Node (ESN), Cisco Unified Communications Manager Session Management Edition, Cisco Unified Communications Manager IM and Presence
                           Service, Cisco Unity Connection, Cisco Emergency Responder, and Cisco Expressway.

All hypervisor and hardware support information for version 15 is located in the documents listed earlier, rather than at: http://www.cisco.com/go/virtualized-collaboration .

### Support for NSE-based Fax or Modem Passthrough for Secure SIP Lines

From Release 15SU4 onwards, the system sends fmtp parameters between endpoints during SIP calls with fax or modem negotiation.
                     Earlier, it used to remove these parameters. This change helps the endpoints choose the right codec, making fax or modem pass-through
                     work smoothly. The fix works for both early offer and delayed offer calls. It supports SIP to SIP calls and SCCP to SIP calls.
                     However, it does not support MTP and TRP call flows.

For more information, see the ‘NSE-based Fax or Modem Passthrough for Secure SIP Lines’ section in the “Configure Gateways”
                     chapter of the System Configuration Guide for Cisco Unified Communications Manager .

### Webex Calling Hybrid for Customer Assist

Webex Calling introduces support for hybrid deployment models with Customer Assist, giving organizations the flexibility to
                     combine cloud-based agent functionality with their current on-premises (Cisco Unified Communications Manager) telephony infrastructure.
                     This hybrid approach enables a smooth, phased transition to advanced customer experience features, allowing businesses to
                     leverage the benefits of the cloud while protecting their existing investments. With hybrid Customer Assist, you can onboard
                     agents to the cloud at your own pace, streamline operations, and enhance customer interactions—without the need for a full
                     telephony migration.

For more information, see Webex Calling Hybrid .

## Important Notes

### Cisco Desk Phone 9800 Series Requirements

Cisco Unified Communications Manager (Unified Communications Manager) requirements for the Cisco Desk Phone 9800 Series include:

Unified Communications Manager 12.5(1)SU9, 14SU4 and later , or 15SU2 and later (To be FCSed around October 2024) .

Installation of the following Cisco Options Package (COP) files on Unified Communications Manager: Phone firmware —Firmware for the Cisco Desk Phone 9800 Series phones is not bundled with Unified Communications Manager. A firmware update
                           may be required to enable the new features. The phone firmware COP files can be downloaded from Cisco.com .

For information on the list of supported features for the Cisco Desk Phone 9800 Series, see the Release Notes for Cisco Desk Phone 9800 Series .

### Interoperability Issues Between LBM Interclusters

Location Bandwidth Manager (LBM) running on Unified Communication Manager version 15 cannot communicate with Unified CM versions
                     with a newer version of Release 15 (for example, Release 15 SU1 or later). Hence, we recommend that you do the following if
                     you are using LBM across multiple clusters:

Ensure that you install the ciscocm.V15FCS_CSCwi82830-lbm_C0211-1.cop.sha512 COP file on Unified Communications Manager Release 15 to interoperate with LBM running on Unified Communication Manager versions
                           15SU1 or later.

### Deprecation of 32-Bit Windows Plugin Support for Cisco TAPI Service Provider

Cisco Unified Communications Manager does not support Cisco TAPI Service Provider (TSP) 32-bit Windows plugin. We encourage
                     you to migrate to the 64-bit plugin version of Cisco TAPI Service Provider (TSP) on supported Windows platforms.

For more information, see the following: Deprecation of 32-Bit Windows Plugin Support for Cisco TAPI Service Provider in Cisco Unified Communications Manager .

### Deprecation of Application Policy Infrastructure Controller Enterprise Module (APIC-EM) Integration

Cisco Unified Communications Manager does not support the Application Policy Infrastructure Controller Enterprise Module (APIC-EM)
                     Integration. We encourage you to use Unified Communication Manager-based Service Parameter–based DSCP QoS management instead
                     of APIC-EM.

Deprecation of Application Policy Infrastructure Controller Enterprise Module (APIC-EM) Integration with Cisco Unified Communications
                              Manager

### Deprecation of Call Control Discovery via Service Advertisement Framework in Unified Communications Manager

Cisco Unified Communications Manager does not support Call Control Discovery via Service Advertisement Framework. Therefore,
                     we recommend that you migrate to Global Dial Plan Replication using the Intercluster Lookup Service (ILS). For more information,
                     see the following:

Deprecation of Call Control Discovery via Service Advertisement Framework in Cisco Unified Communications Manager

System Configuration Guide for Cisco Unified Communications Manager

### Deprecation of Mobile Voice Access via H.323 and SIP VXML Gateways

Cisco Unified Communications Manager does not support Mobile Voice Access via H.323 and SIP VoiceXML (VXML) Gateways. We encourage
                     you to configure Unified Communications Manager with native Mobile Voice Access, which is supported starting from Unified
                     CM version 12.5 and later.

For more information, see: Deprecation of Mobile Voice Access via H.323 and SIP VXML Gateways in Cisco Unified Communications Manager .

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

### Simplifying Release Number Scheme

From Release 14 onwards, Cisco Unified Communications Manager has adopted the single number release plan. There will be no
                        (dot) releases like (dot five) in the past release versions. Service Update releases will be published on top of the main
                        major release 14 through the regular Software Maintenance cycle.

### RSA Cipher Considerations

Although the Cipher Management configuration page allows you to configure any number of ciphers, if you are using one of the following cipher that relies
                     on RSA for key exchange, ensure that you add at least one more strong cipher to maintain compatibility before upgrading from
                     pre-15SU3 releases:

AES128-GCM-SHA256

AES256-SHA256

AES128-SHA256

AES256-SHA

AES128-SHA

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

Cisco VG 202, 202 XM, 204, 204 XM, 224, 310, 320, 350 Analog Voice Gateway

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

### Caveats

You can search for defects in the Bug Search Tool at https://bst.cloudapps.cisco.com/bugsearch/ .

For a list of Open Caveats and Resolved Caveats, see the respective Readme files:

ReadMe for Cisco Unified Communications Manager, Release 15SU4a

ReadMe for Cisco Unified IM and Presence, Release 15SU4

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

| Note | The migration to Microsoft Graph API applies only to Microsoft Office 365; integration with on-premises Exchange Server continues
                                 to use EWS APIs for calendaring. |
|---|---|

| Note | All hypervisor and hardware support information for version 15 is located in the documents listed earlier, rather than at: http://www.cisco.com/go/virtualized-collaboration . |
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
| Cisco VG 202, 202 XM, 204, 204 XM, 224, 310, 320, 350 Analog Voice Gateway | 11.5(1) and later | 12.5(1) and later | 14 and later | 15 and later |
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