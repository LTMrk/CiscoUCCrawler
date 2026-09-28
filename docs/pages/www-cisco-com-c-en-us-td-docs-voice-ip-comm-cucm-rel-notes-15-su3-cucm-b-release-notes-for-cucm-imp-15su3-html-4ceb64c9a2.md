---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-rel-notes-15-su3-cucm-b-release-notes-for-cucm-imp-15su3-html-4ceb64c9a2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/rel_notes/15/SU3/cucm_b_release-notes-for-cucm-imp-15su3.html
retrieved_at: 2026-08-16T17:52:01.034688+00:00
---

Release Notes for Cisco Unified Communications Manager Release 15SU3a and the IM and Presence Service Release 15SU3

# Release Notes for Cisco Unified Communications Manager Release 15SU3a and the IM and Presence Service Release 15SU3

### Download Options

Updated: August 14, 2025

Release Notes for Cisco Unified Communications Manager Release 15SU3a and the IM and Presence Service Release 15SU3

First Published: July 31, 2025

Last Updated: August 14, 2025

# Preview Features Disclaimer

Some features in this release are provided in "preview" status only, because they have known limitations or incomplete software
                  dependencies. Cisco reserves the right to disable preview features at any time without notice.

Preview features should not be relied on in your production environment. Cisco Technical Support will provide limited assistance
                  (Severity 4) to customers who want to use preview features.

## About Release Notes

This release describes new features, restrictions, and caveats for Cisco Unified Communications Manager ( Unified Communications Manager ) and Cisco Unified Communications Manager IM and Presence Service ( IM and Presence Service ) . The release notes are updated for every maintenance release but not for patches or hot fixes.

### Supported Versions

The following software versions apply to:

Unified Communications Manager : 15.0.1.13901-2

IM and Presence Service : 15.0.1.13900-6

#### Version Compatibility Between Unified CM and the IM and Presence Service

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

### Documentation for this Release

For a complete list of the documentation that is available for this release, see the Documentation Guide for Cisco Unified Communications Manager and the IM and Presence Service, Release 15 .

### Installation Procedures

For information on how to install your system, see the Installation Guide for Cisco Unified Communications Manager and the IM and Presence Service .

### Upgrade Procedures

For information on how to upgrade to this release, see the Upgrade and Migration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 15 .

### New and Changed Features

#### Certificate Management Changes

For this release, the certificate management changes are as follows:

The validity period for self-signed certificates has been updated, allowing you to select either one year or two years for
                              newly generated certificates, in addition to the existing options. The default validity period remains unchanged. For more
                              information, see the ‘Self-Signed Certificate Fields’ section in the “Certificates” chapter of the Security Guide for Cisco Unified Communications Manager .

For all self-signed certificates, the CA flag has been changed from CA:TRUE to CA:FALSE except for CAPF certificates. For
                              more information, see the ‘Generate Self-Signed Certificate’ section in the “Certificates” chapter of the Security Guide for Cisco Unified Communications Manager .

You can configure up to five distribution point URI settings to support multiple CRL file downloads (1 per Certificate Authority).
                              You can perform full-chain validation instead of leaf certificate validation by default. This option is available on both
                              publisher and subscriber nodes. For more information, see the ‘Certificate Revocation Configuration’ section in the “Certificates”
                              chapter of the Security Guide for Cisco Unified Communications Manager .

#### FIPS Compliance

From Release 15SU3 onwards:

The Unified Communications Manager and IM and Presence Service that is available is FIPS 140-3 compliant.

CiscoSSL has been upgraded to Cisco SSL 7.3, which is FIPS 140-3 compliant.

#### IPSec DH Group Changes

From Release 15SU3 onwards, DH groups 17 and 18 are no longer available on the IPSec Policy Configuration page. If your source
                        cluster uses policies based on DH groups 17 or 18, reconfigure the policies to exclude these groups before proceeding with
                        the upgrade. This applies to both FIPS and Non-FIPS mode.

For more information, see the ‘Upgrade Considerations with FIPS Mode’ and the ‘IPsec Requirements’ sections in the “Planning
                        the Upgrade" chapter of the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service .

#### Support for Blind Conference Calls When SNR Set to User Control Mode

From this release onwards, Unified Communications Manager has added support for conference calls and call transfers (redirection) when the Single Number Reach (SNR) voicemail policy
                        has been configured for User Control.

For more information, see the ‘CMC RD Feature Interaction’ section in the “Manage Phones" chapter of the Administration Guide for Cisco Unified Communications Manager .

#### Support for MLPP Notifications on Specific SIP Phone Models

Starting with this release, Unified CM supports precedence call originating related MLPP notifications on specific SIP phone
                        models when precedence call is placed using translation or route pattern. When you enable MLPP notifications on either the
                        Cisco Desk Phone 9841, Cisco Desk Phone 9851, Cisco Desk Phone 9861, Cisco Desk Phone 9871, or Cisco Video Phone 8875 (including
                        Non-Radio models), the phones receive notifications for precedence calls, before the call is connected. These notifications
                        include precedence ringback tones and display alerts.

For more information, see the ‘Multilevel Precedence and Preemption Restrictions’ section in the “Configure Multilevel Precedence
                        and Preemption” chapter of the Feature Configuration Guide for Cisco Unified Communications Manager .

#### Support for More than 126 Lines on KEM Modules with Cisco Desk Phone 9861 and Cisco Desk Phone 9871

From this release onwards, Unified Communications Manager will support 130 lines on KEM modules for the Cisco Desk Phone 9861 and Cisco Desk Phone 9871 models.

#### Support for SME  Busy Out

From this release onwards, the Cisco Session Manager Edition (SME) introduces a feature designed to enhance the upgrade process
                        by allowing administrators to manage the Busy Out state of the SME cluster. Using a new CLI command, administrators can enable
                        or disable this functionality.

When activated, the SME cluster responds to SIP OPTIONS ping requests with a 503 Service Unavailable message. This signals Unified Communications Manager Leaf clusters to stop routing new calls to the affected SME cluster. Importantly, ongoing calls on the SME cluster remain
                        unaffected. During this period, new calls from Unified Communications Manager Leaf clusters are automatically redirected to alternative SME clusters.

This feature ensures a seamless upgrade experience by maintaining service continuity and preventing call disruptions. Once
                        the upgrade is complete, the Busy Out state can be deactivated, restoring normal call routing operations.

For more information, see the "Set Commands" chapter in the Command Line Interface Reference Guide for Cisco Unified Communications Solutions .

#### (Preview-Non Production use only) Support of Hardware Gateway-based Conference Bridge in Unified CM in IPv6

From this release onwards, Unified CM provides a dual stack (IPv4 and IPv6) for a hardware conference bridge provided the
                        following conditions are fulfilled:

The Unified Communications Manager should be dual-stack (IPv4 and IPv6).

An IOS Gateway that has dual stack support (IPv4 and IPv6) should be used for registering hardware conference bridge to Unified Communications Manager .

For more information, see the ‘Conference Bridge Types’ section in the “Configure Conference Bridges” chapter of the System Configuration Guide for Cisco Unified Communications Manager .

#### Updates to Cipher Management Page

For SSH interface, you can configure SSH host key algorithm using the Cipher Management page. For more information, see the
                        ‘Recommended Ciphers’ section in the “Cipher Management” chapter of the Security Guide for Cisco Unified Communications Manager .

#### Minimum TLS Version Support for Calendaring Service

The minimum TLS version configuration is now enabled for the calendaring service in the IM and Presence Service.

#### TLS 1.3 Support for MSSQL Database

In this release, the IM and Presence Service adds support for TLS 1.3 connections with the MSSQL database.

### Important Notes

#### Cisco Desk Phone 9800 Series Requirements

Cisco Unified Communications Manager (Unified Communications Manager) requirements for the Cisco Desk Phone 9800 Series include:

Unified Communications Manager 12.5(1)SU9, 14SU4 and later.

Installation of the following Cisco Options Package (COP) files on Unified Communications Manager: Phone firmware —Firmware for the Cisco Desk Phone 9800 Series phones is not bundled with Unified Communications Manager. A firmware update
                              may be required to enable the new features. The phone firmware COP files can be downloaded from Cisco.com .

For information on the list of supported features for the Cisco Desk Phone 9800 Series, see the Release Notes for Cisco Desk Phone 9800 Series .

#### Interoperability Issues Between LBM Interclusters

Location Bandwidth Manager (LBM) running on Unified Communication Manager version 15 cannot communicate with Unified CM versions
                        with a newer version of Release 15 (for example, Release 15 SU1 or later). Hence, we recommend that you do the following if
                        you are using LBM across multiple clusters:

Ensure that you install the ciscocm.V15FCS_CSCwi82830-lbm_C0211-1.cop.sha512 COP file on Unified Communications Manager Release 15 to interoperate with LBM running on Unified Communication Manager versions
                              15SU1 or later.

#### Deprecation of Call Control Discovery via Service Advertisement Framework in Unified Communications Manager

Cisco Unified Communications Manager does not support Call Control Discovery via Service Advertisement Framework. Therefore,
                        we recommend that you migrate to Global Dial Plan Replication using the Intercluster Lookup Service (ILS). For more information,
                        see the following:

Deprecation of Call Control Discovery via Service Advertisement Framework in Cisco Unified Communications Manager

System Configuration Guide for Cisco Unified Communications Manager

#### Deprecation of Remote Call Control with Microsoft Lync Server for IM and Presence Service

Unified Communications Manager Release 15 does not support Remote Call Control with Microsoft Lync Server for IM and Presence Service . If you are using this feature currently in your deployment and you are trying to upgrade to Release 15, you cannot use this
                        feature after the upgrade.

This feature continues to be supported in Releases 12.5.x and 14 and SUs until their EOL/EOS.

For more information, see Deprecation of Remote Call Control with Microsoft Lync Server for IM and Presence Service on Cisco Unified Communications
                           Manager, Release 15 .

#### Remove Deprecated Device Firmware from ISO

Starting with Release 15 onwards, phone firmware that is end of support will no longer be included in the Unified Communications Manager ISO. These endpoints will still be allowed to register, unless they have been officially deprecated, but the firmware will
                        not be present in the TFTP directory following a fresh install. For more details, see the ReadMe for Cisco Unified Communications Manager .

#### New 2021 Signing Key

Attention

Release 14SU1 and onwards is signed with a new 2021 signing key. It is possible that you may need to install the ciscocm.enable-sha512sum-2021-signing-key-v1.0.cop.sgn
                                    COP file first if upgrading from Unified Communications Manager versions prior to Release 14. See the COP file readme for
                                    specifics.

This release also removes support for the previous signing key. If you are installing phone firmware, ensure that you use
                                    the files with k4.cop.sha512 in the name, as these files are also signed with the new signing key. Installing files signed
                                    with the previous signing key results in a "The selected file is not valid." error during installation.

#### Simplifying Release Number Scheme

From Release 14 onwards, Cisco Unified Communications Manager has adopted the single number release plan. There will be no
                           (dot) releases like (dot five) in the past release versions. Service Update releases will be published on top of the main
                           major release 14 through the regular Software Maintenance cycle.

#### RSA Cipher Considerations

Although the Cipher Management configuration page allows you to configure any number of ciphers, if you are using one of the following cipher that relies
                        on RSA for key exchange, ensure that you add at least one more strong cipher to maintain compatibility before upgrading from
                        pre-15SU3 releases:

AES128-GCM-SHA256

AES256-SHA256

AES128-SHA256

AES256-SHA

AES128-SHA

#### New Cisco Gateway Support

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

##### Cisco Analog Telephone Adapters

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

### Caveats

#### Bug Search Tool

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

#### Caveats

You can search for defects in the Bug Search Tool at https://bst.cloudapps.cisco.com/bugsearch/ .

For a list of Open Caveats and Resolved Caveats, see the respective Readme files:

ReadMe for Cisco Unified Communications Manager, Release 15SU3a

ReadMe for Cisco Unified IM and Presence, Release 15SU3

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