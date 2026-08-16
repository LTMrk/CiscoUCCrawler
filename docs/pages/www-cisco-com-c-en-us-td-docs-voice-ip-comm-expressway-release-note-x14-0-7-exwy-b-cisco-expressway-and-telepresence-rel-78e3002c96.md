---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-release-note-x14-0-7-exwy-b-cisco-expressway-and-telepresence-rel-78e3002c96
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/release_note/X14-0-7/exwy_b_cisco-expressway-and-telepresence-release-note-x1407.html
retrieved_at: 2026-08-16T22:08:27.741963+00:00
---

Cisco Expressway and Cisco TelePresence Video Communication Server Release Note (X14.0.7)

# Cisco Expressway and Cisco TelePresence Video Communication Server Release Note (X14.0.7)

### Download Options

Updated: May 25, 2022

First Published: May 25, 2022

# About the Documentation

## Change History

Date

Change

Reason

May 2022

First publication for X14.0.7

X14.0.7 release

March 2022

First publication for X14.0.6

X14.0.6 release

February 2022

First publication for X14.0.5

X14.0.5 release

December 2021

First publication for X14.0.4

X14.0.4 release

August 2021

First publication for X14.0.3.

X14.0.3 release

August 2021

Added a new item on Traffic Server Enforces Certificate Verification in the section "Other Changes in this Release."

X14.0.2 release - Republished

July 2021

First publication for X14.0.2.

X14.0.2 release

June 2021

First publication for X14.0.1.

X14.0.1 release

May 2021

Included a limitation in MRA Limitations section.

X14.0 release - Republished

April 2021

First publication for X14.0.

X14.0 release

December 2020

First publication for X12.7.

X12.7 release

August 2020

Updates for maintenance release.

X12.6.2 release

July 2020

Remove misleading section about issues with software downgrade (which is not supported).

Document correction

July 2020

Updates for maintenance release. Also, clarification on endpoint requirements for OAuth token authorization.

X12.6.1 release

June 2020

First publication for X12.6.

X12.6 release

## Supported Platforms

Platform name

Serial Numbers

Scope of software version support

Small VM (OVA)

(Auto-generated)

X8.1 onwards

Medium VM (OVA)

(Auto-generated)

X8.1 onwards

Large VM (OVA)

(Auto-generated)

X8.1 onwards

CE1200 Hardware Revision 2 (pre-installed on UCS C220 M5L)

52E1####

X12.5.5 onwards

CE1200 Hardware Revision 1 (pre-installed on UCS C220 M5L)

52E0####

X8.11.1 onwards

CE1100 (Expressway pre-installed on UCS C220 M4L)

52D#####

Not supported (after X12.5.x) except limited support with X12.6.x versions for maintenance and bug fixing purposes only. Vulnerability/Security
                              support is extended until November 30, 2023.

CE1000 (Expressway pre-installed on UCS C220 M3L)

52B#####

Not supported (after X8.10.x)

CE500 (Expressway pre-installed on UCS C220 M3L)

52C#####

Not supported (after X8.10.x)

### Notices Relating to Deploying OVA with VMware 7.0 U2

This is a known issue in the current release. Deploying X14.0.7 OVA shows "Invalid Certificate" on vCenter 7.0 U2 version of VMware, though it shows "Trusted Certificate" in older versions. Refer to Knowledge Article for more information about the issue.

### Notices Relating to VCS Product Support

Cisco has announced end-of-sale and end-of-life dates for the Cisco TelePresence Video Communication Server (VCS) product. Details are available at the following link .

Issues resolved in this software release are available to Cisco Expressway and Cisco TelePresence Video Communication Server
                        users, however, new features added in this release are not supported on the Cisco TelePresence Video Communication Server
                        (VCS) product .

This notice does not affect the Cisco Expressway Series product.

### Notices Relating to Hardware Support for CE1200, CE1100, CE1000, and CE500 Appliances

This section applies to hardware support services only.

CE1200 Appliance

Supply issues with components used in the Expressway CE1200 are delaying orders. In light of the supply issues, we are extending
                                 the end of Vulnerability/Security support until November 30, 2023.

Please ignore the warning " unsupported hardware " in the User Interface.

CE1100 Appliance - End-of-Life and Advance Notice of hardware service support withdraw

In light of ongoing issues with component shortages that are affecting the timely supply of new Expressway appliances, to
                     support those customers still using Cisco Expressway CE1100 appliances, Cisco has taken the decision to extend the End of
                     Vulnerability/Security Support from November 14, 2021 (as per the original End-of-Life announcement ) to November 30, 2023, in line with the last date of support, for those customers with a valid service contract.

Although customers may run this release of software on the Expressway CE1100 and benefit from security improvements/vulnerability
                                 fixes, many new features require newer, more powerful hardware and as a result, new features/functionality added in this release
                                 of the Expressway software are not supported for use on the CE1100 platform.

CE500 and CE1000 Appliances - End-of-Sale Notice

The Cisco Expressway CE500 and CE1000 appliance hardware platforms are no longer supported by Cisco. See the End-of-sale announcement for more details.

## Interoperability and Compatibility

### Product Compatibility Information

#### Detailed matrices

Cisco Expressway is standards-based and interoperates with standards-based SIP and H.323 equipment both from Cisco and third
                        parties. For specific device interoperability questions, contact your Cisco representative.

#### Mobile and Remote Access (MRA)

Information about compatible products for MRA specifically, is provided in version tables for endpoints and infrastructure
                        products in the Mobile and Remote Access Through Cisco Expressway Deployment Guide .

For MRA, to access the latest features and functionality, it's recommended that Expressway is deployed in conjunction with
                        the latest version of UCM. However, Expressway is backwards compatible with earlier UCM releases as well.

### Which Expressway Services Can Run Together?

The Cisco Expressway Administrator Guide details which Expressway services can coexist on the same Expressway system or cluster. See the table " Services That Can be Hosted Together " in the Introduction chapter. For example, if you want to know if MRA can coexist with CMR Cloud (it can) the table will tell you.

## Feature Summary for X14.0.7

Feature / Change

Status

RedSky E911 Location Services

Supported from X14.0.4

Service Select Wizard

Supported from X14.0.3

Ban/Unban an IP Address

Supported from X14.0.3

Exempt an IP Address

Supported from X14.0.3

Call Detail Record (CDR) Configuration

Supported from X14.0.3

Multiple Admin Accounts and Groups can have CLI access.

Supported from X14.0.1

Ability to configure SNMP details in the new RAML REST API.

Supported from X14.0.1

Ability to view and acknowledge the alarms using command interface

Supported from X14.0.1

Redirect URI support for SSO/OAuth sign-in

Supported from X14.0

AV1 Support

Supported from X14.0

XCP support for "Jabber Zero Downtime"

Supported from X14.0

Escalation from P2P to Meeting

Supported from X14.0

Expressway Cluster load balancing not applicable to SIP Federation

Supported from X14.0

MRA SIP Registration Failover for Cisco Jabber

Supported from X14.0

Hardware Security Module (HSM) Support

Preview

MRA Mobile Application Management clients

Preview

Android Push Notifications for IM&P

Preview (disabled by default from X12.6.2)

Headset Capabilities for Cisco Contact Center

Preview

## Withdrawn or Deprecated Features and Software

The Expressway product set is under continuous review and features are sometimes withdrawn from the product or deprecated
                  to indicate that support for them will be withdrawn in a subsequent release. This table lists the features that are currently
                  in deprecated status or have been withdrawn since X12.5.

Feature / Software

Status

Support for Microsoft Internet Explorer browser

Deprecated from X14.0.2

VMware ESXi 6.0 (VM-based deployments)

Deprecated

Cisco Jabber Video for TelePresence (Movi)

Relates to Cisco Jabber Video for TelePresence (works in conjunction with Cisco Expressway for video communication) and not
                                          to the Cisco Jabber soft client that works with Unified CM.

Deprecated

FindMe device/location provisioning service - Cisco TelePresence FindMe/Cisco TelePresence Management Suite Provisioning Extension
                              (Cisco TMSPE)

Deprecated

Expressway Starter Pack

Deprecated

Smart Call Home preview feature

Withdrawn X12.6.2

Expressway built-in forward proxy

Withdrawn X12.6.2

Cisco Advanced Media Gateway

Withdrawn X12.6

VMware ESXi 5.x (VM-based deployments)

Withdrawn X12.5

## No Support for Ray Baum's Act

Expressway is not an MLTS (Multiline Telephone System). Customers that need to comply with the requirements of Ray Baum’s Act should use Cisco Unified Communication Manager in conjunction with Cisco Emergency Responder.

## Related Documentation

Support videos

Videos provided by Cisco TAC engineers about certain common Expressway configuration procedures are available on the Expressway/VCS Screencast Video List page (search for "Expressway videos" ).

Installation - virtual machines

Cisco Expressway Virtual Machine Installation Guide on the Expressway Installation Guides page.

Installation - physical appliances

Cisco Expressway CE1200 Appliance Installation Guide on the Expressway Installation Guides page.

Basic configuration for single-box systems

Cisco Expressway Registrar Deployment Guide on the Expressway Configuration Guides page.

Basic configuration for paired-box systems (firewall traversal)

Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide on the Expressway Configuration Guides page.

Administration and maintenance

Cisco Expressway Administrator Guid e on the Expressway Maintain and Operate Guides page (includes Serviceability information).

Clustering

Cisco Expressway Cluster Creation and Maintenance Deployment Guide on the Expressway Configuration Guides page.

Certificates

Cisco Expressway Certificate Creation and Use Deployment Guide on the Expressway Configuration Guides page.

Ports

Cisco Expressway IP Port Usage Configuration Guide on the Expressway Configuration Guides page.

Mobile and Remote Access

Mobile and Remote Access Through Cisco Expressway Deployment Guide on the Expressway Configuration Guides page.

Cisco Meeting Server

Cisco Meeting Server with Cisco Expressway Deployment Guide on the Expressway Configuration Guides page.

Cisco Meeting Server API Reference Guide on the Cisco Meeting Server Programming Guides page.

Other Cisco Meeting Server Guides are available on the Cisco Meeting Server Configuration Guides page.

Cisco Webex Hybrid Services

Hybrid services knowledge base

Cisco Hosted Collaboration Solution (HCS)

HCS customer documentation

Microsoft infrastructure

Cisco Expressway with Microsoft Infrastructure Deployment Guide on the Expressway Configuration Guides page.

Cisco Jabber and Microsoft Skype for Business Infrastructure Configuration Cheatsheet on the Expressway Configuration Guides page.

Rest API

Cisco Expressway REST API Summary Guide on the Expressway Configuration Guides page (high-level information only as the API is self-documented).

Multiway Conferencing

Cisco TelePresence Multiway Deployment Guide on the Expressway Configuration Guides page.

## Features and Changes in X14.0.7

We aim to provide new Expressway features as promptly as possible. Sometimes it is not possible to officially support a new
                     feature because it may require updates to other Cisco products which are not yet available.

There are no new functional enhancements or changes for this release.

### Preview Features

Some features in this release are provided in "preview" status only, because they have known limitations or incomplete software dependencies. Cisco reserves the right to disable
                     preview features at any time without notice.

Preview features should not be relied on in your production environment. Cisco Technical Support will provide limited assistance
                     (Severity 4) to customers who want to use preview features.

#### (Preview) Hardware Security Module (HSM) Support

From X12.6 release, Expressway supports HSM functionality, on a Preview basis only. HSM safeguards and manages digital keys
                           for strong authentication, and provides crypto-processing for critical functions such as encryption, decryption and authentication
                           for the use of applications, identities, and databases. An HSM device comes as a plug-in card or an external device that attaches
                           directly to your computer or network server. It prevents hardware and software tampering—by raising alarms or by making the
                           HSM inoperable.

A new Maintenance > Security > HSM configuration page is added to the Expressway web user interface.

Expressway currently only supports the nShield Connect XC from Entrust as an HSM provider (on a Preview basis).

The "SafeNet Luna" network device from Gemalto is also referenced in the Expressway user interface but, this device is not currently supported by Expressway .

#### (Preview) Headset Capabilities for Cisco Contact Center – MRA Deployments

This feature applies if you deploy Expressway with Mobile and Remote Access. It is currently provided in Preview status only.

New demonstration software now provides some Cisco Contact Center functions on compatible Cisco headsets. From X12.6, Expressway
                           automatically supports these new headset capabilities as a preview feature, if the involved endpoint, headset, and Unified
                           CM are running the necessary software versions. The feature is enabled from the Unified CM interface and you do not need to
                           configure anything on Expressway.

More information is available in the white paper Cisco Headset and Finesse Integration for Contact Center .

#### (Preview) Push Notifications with Mobile Application Management clients - MRA Deployments

This feature applies if you deploy Expressway with Mobile and Remote Access. It is currently provided in Preview status only.

With this feature, push notification support over Mobile and Remote Access now includes support for Mobile Application Management
                           (MAM) clients like Jabber Intune and Jabber BlackBerry. As a result, the push notification service is available for all devices
                           that are running Jabber Intune and Jabber BlackBerry clients.

#### (Preview) Push Notifications with Android Devices – MRA Deployments

This feature applies if you deploy Expressway with MRA. In X12.6 it was introduced in Preview status only, due to external
                           product version dependencies.

In X12.6.2, the feature was switched off by default due to a known issue (bug ID CSCvv12541 refers).

In X12.7, bug ID CSCvv12541 was fixed. However, this feature remains in Preview status for now, due to pending software dependencies.

##### How to enable push notifications for Android devices

This feature is enabled through the Expressway command line interface. Only do this if all IM and Presence Service nodes that service Android users are also running a supported release .

The CLI command is: xConfiguration XCP Config FcmService: On

IM and Presence services for users who are currently signed in over MRA will be disrupted when this command is used, so those
                                       users will need to sign in again.

#### (Preview) KEM Support for Compatible Phones - MRA Deployments

We have not officially tested and verified support over MRA for the Key Expansion Module (KEM) accessory for Cisco IP Phone
                           8800 Series devices. However, we have observed under lab conditions that KEMs with multiple DNs work satisfactorily over MRA.
                           These are not official tests, but in view of the COVID-19 crisis, this may be useful information for customers who are willing to use an
                           unsupported preview feature.

SIP path headers must be enabled on Expressway, and you need a Unified CM software version that supports path headers (release
                           11.5(1)SU4 or later is recommended).

### REST API Changes

The REST API for Expressway is available to simplify remote configuration. For example, by third party systems such as Cisco
                        Prime Collaboration Provisioning. We add REST API access to configuration, commands, and status information as new features
                        are added, and also selectively retrofit the REST API to some features that were added in earlier versions of Expressway.

The API is self-documented using RAML, and you can access the RAML definitions at https://< ipaddress >/api/raml .

Configuration APIs

API Introduced In Version

Service Select Wizard

X14.0.3

Ability to acknowledge active Alarms

X14.0.3

Ban/Unban an IP Address

X14.0.3

Exempt an IP Address

X14.0.3

Call Detail Record (CDR) Configuration

X14.0.3

Status - fail2banbannedaddress

X14.0.2

SNMP Configuration

X14.0.1

Alarms - view and acknowledge

X14.0.1

Dedicated Management Interface (DMI)

X12.7

Diagnostic Logging

X12.6.3

Smart Licensing

X12.6

Clustering

X8.11

Smart Call Home

X8.11

Microsoft Interoperability

X8.11

B2BUA TURN Servers

X8.10

Admin account

X8.10

Firewall rules

X8.10

SIP configuration

X8.10

Domain certificates for Server Name Identification

X8.10

MRA expansion

X8.9

Business to business calling

X8.9

MRA

X8.8

### Other Changes in this Release

#### X14.0.7 release

The following are the changes in this release.

#### Expressway processes SIP messages in a different order than they are received

A new CLI command is added that specifies the maximum delay of a SIP BIB invite message (ensure SIP message proceeds in order)
                        that the server must handle (in milliseconds).

Recommend adjusting delay between 500-1000 milliseconds.

The CLI command is: xConfiguration SIP Advanced BibInviteDelay: <1..5000>

#### ssh removal from backup and restore

We are removing the client ssh public key and server ssh key pair from the backup and restore.

As ssh keys will not part of backup, after restoring the system ssh may not work without password. So, to login, add both
                        client and server keys manually.

#### X14.0.2 release

The following are the changes in this release.

#### CE Zone Status Change from "Active" to "Address Resolvable"

Prior to X14.0.2, CE zone showed a status of Active where the Zone Profile had Monitor Peer status / Neighbor Monitor set to No - since the Expressway is not monitoring the peer status for the CE zones, the more accurate status of Address Resolvable is indicated.

Auto-created UC zones and associated Unified Communications zone profile are not customizable and Neighbor Monitor set to No is by design.

Auto-created CE (tcp/tls/OAuth) Zone destined for the UC node will show status as Address Resolvable as per a fix for CSCup29823 .

#### Traffic Server Enforces Certificate Verification

Before upgrading from pre-X14.0.2 release to X14.0.7, make sure the following certificate requirement is met.

Due to improvements in the traffic server service in Expressway, beginning in X14.0.2, the following must be in place for
                        MRA.

Requirement - Upload the Complete Certificate Authority (CA) chain of trust including any Certificate Authority provided intermediate
                        certificates to the Tomcat -trust and CallManager -trust list of Cisco Unified Communications Manager (UCM), even if the UCM is in non-secure mode. And restart the following services on CUCM side:

TFTP

Tomcat Service

CallManager Service

HA Proxy Service (if using TLS on Tomcat)

Reason - The traffic server service in Expressway sends its certificate whenever a server (UCM) requests it. These requests are
                        for services running on ports other than 8443 (for example, ports 6971, 6972, and so on). This enforces certificate verification
                        even if UCM is in non-secure mode.

For more information, see Mobile and Remote Access Through Expressway Deployment Guide .

## Limitations

We aim to provide new Expressway features as speedily as possible. Sometimes it is not possible to officially support a new
                  feature because it may require updates to other Cisco products which are not yet available, or known issues or limitations
                  affect some deployments of the feature. If customers might still benefit from using the feature, we mark it as “preview” in
                  the release notes. Preview features may be used, but you should not rely on them in production environments (see Preview Features Disclaimer ). Occasionally we may recommend that a feature is not used until further updates are made to Expressway or other products.

## Open and Resolved Issues

## Using the Bug Search Tool

The Bug Search Tool contains information about open and resolved issues for this release and previous releases, including
                     descriptions of the problems and available workarounds. The identifiers listed in these release notes will take you directly
                     to a description of each issue.

To look for information about a specific problem mentioned in this document:

Using a web browser, go to the Bug Search Tool .

Sign in with a cisco.com username and password.

Enter the bug identifier in the Search field and click Search .

To look for information when you do not know the identifier:

Type the product name in the Search field and click Search .

From the list of bugs that appears, use the Filter drop-down list to filter on either Keyword , Modified Date , Severity , Status , or Technology .

Use Advanced Search on the Bug Search Tool home page to search on a specific software version.

The Bug Search Tool help pages have further information on using the Bug Search Tool.

## Obtaining Documentation and Submitting a Service Request

Use the Cisco Notification Service to create customized flexible notification alerts to be sent to you via email or by RSS feed.

For information on obtaining documentation, using the Cisco Bug Search Tool (BST), submitting a service request, and gathering
                  additional information, see What's New in Cisco Product Documentation .

To receive new and revised Cisco technical content directly to your desktop, you can subscribe to the What's New in Cisco Product Documentation RSS feed . The RSS feeds are a free service.

### This Document Applies to These Products

- Expressway Series

| Date | Change | Reason |
|---|---|---|
| May 2022 | First publication for X14.0.7 | X14.0.7 release |
| March 2022 | First publication for X14.0.6 | X14.0.6 release |
| February 2022 | First publication for X14.0.5 | X14.0.5 release |
| December 2021 | First publication for X14.0.4 | X14.0.4 release |
| August 2021 | First publication for X14.0.3. | X14.0.3 release |
| August 2021 | Added a new item on Traffic Server Enforces Certificate Verification in the section "Other Changes in this Release." | X14.0.2 release - Republished |
| July 2021 | First publication for X14.0.2. | X14.0.2 release |
| June 2021 | First publication for X14.0.1. | X14.0.1 release |
| May 2021 | Included a limitation in MRA Limitations section. | X14.0 release - Republished |
| April 2021 | First publication for X14.0. | X14.0 release |
| December 2020 | First publication for X12.7. | X12.7 release |
| August 2020 | Updates for maintenance release. | X12.6.2 release |
| July 2020 | Remove misleading section about issues with software downgrade (which is not supported). | Document correction |
| July 2020 | Updates for maintenance release. Also, clarification on endpoint requirements for OAuth token authorization. | X12.6.1 release |
| June 2020 | First publication for X12.6. | X12.6 release |

| Platform name | Serial Numbers | Scope of software version support |
|---|---|---|
| Small VM (OVA) | (Auto-generated) | X8.1 onwards |
| Medium VM (OVA) | (Auto-generated) | X8.1 onwards |
| Large VM (OVA) | (Auto-generated) | X8.1 onwards |
| CE1200 Hardware Revision 2 (pre-installed on UCS C220 M5L) | 52E1#### | X12.5.5 onwards |
| CE1200 Hardware Revision 1 (pre-installed on UCS C220 M5L) | 52E0#### | X8.11.1 onwards |
| CE1100 (Expressway pre-installed on UCS C220 M4L) | 52D##### | Not supported (after X12.5.x) except limited support with X12.6.x versions for maintenance and bug fixing purposes only. Vulnerability/Security
                              support is extended until November 30, 2023. |
| CE1000 (Expressway pre-installed on UCS C220 M3L) | 52B##### | Not supported (after X8.10.x) |
| CE500 (Expressway pre-installed on UCS C220 M3L) | 52C##### | Not supported (after X8.10.x) |

| Note | This is a known issue in the current release. Deploying X14.0.7 OVA shows "Invalid Certificate" on vCenter 7.0 U2 version of VMware, though it shows "Trusted Certificate" in older versions. Refer to Knowledge Article for more information about the issue. |
|---|---|

| Important | Supply issues with components used in the Expressway CE1200 are delaying orders. In light of the supply issues, we are extending
                                 the end of Vulnerability/Security support until November 30, 2023. Please ignore the warning " unsupported hardware " in the User Interface. |
|---|---|

| Note | Although customers may run this release of software on the Expressway CE1100 and benefit from security improvements/vulnerability
                                 fixes, many new features require newer, more powerful hardware and as a result, new features/functionality added in this release
                                 of the Expressway software are not supported for use on the CE1100 platform. |
|---|---|

| Feature / Change | Status |
|---|---|
| RedSky E911 Location Services | Supported from X14.0.4 |
| Service Select Wizard | Supported from X14.0.3 |
| Ban/Unban an IP Address | Supported from X14.0.3 |
| Exempt an IP Address | Supported from X14.0.3 |
| Call Detail Record (CDR) Configuration | Supported from X14.0.3 |
| Multiple Admin Accounts and Groups can have CLI access. | Supported from X14.0.1 |
| Ability to configure SNMP details in the new RAML REST API. | Supported from X14.0.1 |
| Ability to view and acknowledge the alarms using command interface | Supported from X14.0.1 |
| Redirect URI support for SSO/OAuth sign-in | Supported from X14.0 |
| AV1 Support | Supported from X14.0 |
| XCP support for "Jabber Zero Downtime" | Supported from X14.0 |
| Escalation from P2P to Meeting | Supported from X14.0 |
| Expressway Cluster load balancing not applicable to SIP Federation | Supported from X14.0 |
| MRA SIP Registration Failover for Cisco Jabber | Supported from X14.0 |
| Hardware Security Module (HSM) Support | Preview |
| MRA Mobile Application Management clients | Preview |
| Android Push Notifications for IM&P | Preview (disabled by default from X12.6.2) |
| Headset Capabilities for Cisco Contact Center | Preview |

| Feature / Software | Status |
|---|---|
| Support for Microsoft Internet Explorer browser | Deprecated from X14.0.2 |
| VMware ESXi 6.0 (VM-based deployments) | Deprecated |
| Cisco Jabber Video for TelePresence (Movi) Note Relates to Cisco Jabber Video for TelePresence (works in conjunction with Cisco Expressway for video communication) and not
                                          to the Cisco Jabber soft client that works with Unified CM. | Note | Relates to Cisco Jabber Video for TelePresence (works in conjunction with Cisco Expressway for video communication) and not
                                          to the Cisco Jabber soft client that works with Unified CM. | Deprecated |
| Note | Relates to Cisco Jabber Video for TelePresence (works in conjunction with Cisco Expressway for video communication) and not
                                          to the Cisco Jabber soft client that works with Unified CM. |
| FindMe device/location provisioning service - Cisco TelePresence FindMe/Cisco TelePresence Management Suite Provisioning Extension
                              (Cisco TMSPE) | Deprecated |
| Expressway Starter Pack | Deprecated |
| Smart Call Home preview feature | Withdrawn X12.6.2 |
| Expressway built-in forward proxy | Withdrawn X12.6.2 |
| Cisco Advanced Media Gateway | Withdrawn X12.6 |
| VMware ESXi 5.x (VM-based deployments) | Withdrawn X12.5 |

| Note | Relates to Cisco Jabber Video for TelePresence (works in conjunction with Cisco Expressway for video communication) and not
                                          to the Cisco Jabber soft client that works with Unified CM. |
|---|---|

| Support videos | Videos provided by Cisco TAC engineers about certain common Expressway configuration procedures are available on the Expressway/VCS Screencast Video List page (search for "Expressway videos" ). |
|---|---|
| Installation - virtual machines | Cisco Expressway Virtual Machine Installation Guide on the Expressway Installation Guides page. |
| Installation - physical appliances | Cisco Expressway CE1200 Appliance Installation Guide on the Expressway Installation Guides page. |
| Basic configuration for single-box systems | Cisco Expressway Registrar Deployment Guide on the Expressway Configuration Guides page. |
| Basic configuration for paired-box systems (firewall traversal) | Cisco Expressway-E and Expressway-C Basic Configuration Deployment Guide on the Expressway Configuration Guides page. |
| Administration and maintenance | Cisco Expressway Administrator Guid e on the Expressway Maintain and Operate Guides page (includes Serviceability information). |
| Clustering | Cisco Expressway Cluster Creation and Maintenance Deployment Guide on the Expressway Configuration Guides page. |
| Certificates | Cisco Expressway Certificate Creation and Use Deployment Guide on the Expressway Configuration Guides page. |
| Ports | Cisco Expressway IP Port Usage Configuration Guide on the Expressway Configuration Guides page. |
| Mobile and Remote Access | Mobile and Remote Access Through Cisco Expressway Deployment Guide on the Expressway Configuration Guides page. |
| Cisco Meeting Server | Cisco Meeting Server with Cisco Expressway Deployment Guide on the Expressway Configuration Guides page. Cisco Meeting Server API Reference Guide on the Cisco Meeting Server Programming Guides page. Other Cisco Meeting Server Guides are available on the Cisco Meeting Server Configuration Guides page. |
| Cisco Webex Hybrid Services | Hybrid services knowledge base |
| Cisco Hosted Collaboration Solution (HCS) | HCS customer documentation |
| Microsoft infrastructure | Cisco Expressway with Microsoft Infrastructure Deployment Guide on the Expressway Configuration Guides page. Cisco Jabber and Microsoft Skype for Business Infrastructure Configuration Cheatsheet on the Expressway Configuration Guides page. |
| Rest API | Cisco Expressway REST API Summary Guide on the Expressway Configuration Guides page (high-level information only as the API is self-documented). |
| Multiway Conferencing | Cisco TelePresence Multiway Deployment Guide on the Expressway Configuration Guides page. |

| Important | The "SafeNet Luna" network device from Gemalto is also referenced in the Expressway user interface but, this device is not currently supported by Expressway . |
|---|---|

| Note | IM and Presence services for users who are currently signed in over MRA will be disrupted when this command is used, so those
                                       users will need to sign in again. |
|---|---|

| Configuration APIs | API Introduced In Version |
|---|---|
| Service Select Wizard | X14.0.3 |
| Ability to acknowledge active Alarms | X14.0.3 |
| Ban/Unban an IP Address | X14.0.3 |
| Exempt an IP Address | X14.0.3 |
| Call Detail Record (CDR) Configuration | X14.0.3 |
| Status - fail2banbannedaddress | X14.0.2 |
| SNMP Configuration | X14.0.1 |
| Alarms - view and acknowledge | X14.0.1 |
| Dedicated Management Interface (DMI) | X12.7 |
| Diagnostic Logging | X12.6.3 |
| Smart Licensing | X12.6 |
| Clustering | X8.11 |
| Smart Call Home | X8.11 |
| Microsoft Interoperability | X8.11 |
| B2BUA TURN Servers | X8.10 |
| Admin account | X8.10 |
| Firewall rules | X8.10 |
| SIP configuration | X8.10 |
| Domain certificates for Server Name Identification | X8.10 |
| MRA expansion | X8.9 |
| Business to business calling | X8.9 |
| MRA | X8.8 |

| Important | Before upgrading from pre-X14.0.2 release to X14.0.7, make sure the following certificate requirement is met. |
|---|---|