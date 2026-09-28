---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-admin-guide-x14-0-1-exwy-b-cisco-expressway-administrator-guide-x-8f4648d1eb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X14-0-1/exwy_b_cisco-expressway-administrator-guide-x14-0-1/exwy_m_managing-licensing.html
retrieved_at: 2026-08-16T22:41:33.455860+00:00
---

Cisco Expressway Administrator Guide (X14.0.1)

# Cisco Expressway Administrator Guide (X14.0.1)

Updated: June 2, 2021

Chapter: Managing Licensing

## Chapter: Managing Licensing

# Managing Licensing

This section describes the licensing options that are available for Cisco Expressway, and how to manage them. Note that Smart
                        Licensing mode is not supported for the Cisco VCS product, only for the Cisco Expressway Series.

## Smart Licensing and PAK Licensing (Option Keys) Compared

Cisco Expressway supports either of these two licensing modes:

PAK-based licensing . The classic, traditional method uses option keys (also known as Product Activation Keys) to install licenses on Expressway.
                                    Note that option keys are not just used for licenses, but also to enable certain features and services.

Smart Licensing . The newer licensing method is available for Expressway from X12.6. This method is typically managed with our cloud-based
                                    Cisco Smart Software Manager (CSSM). Alternatively, deployments that need an on premises approach can use the Smart Software
                                    Manager On-Prem product (formerly known as "Smart Software Manager satellite" ).

Only one licensing mode is supported at any time.

Expressway is set to PAK-based licensing by default. You can switch to Smart Licensing from the web interface ( Maintenance > Smart licensing ) although be aware that switching back to PAK needs a factory reset .

Smart Licensing is not available with features that use option keys . Some Expressway features are enabled by option keys. Because option keys are incompatible with Smart Licensing, if you need
                              any features that require option keys, you must use PAK-based licensing and not Smart Licensing.

## Managing Option Keys

This section applies if the Expressway uses classic PAK-based licensing mode, rather than Smart Licensing . In PAK mode, option keys (also known as Product Activation Keys) are used to add additional features or licenses to Expressway.
                              Option keys can be valid for a fixed time period or for an unlimited duration.

If Smart Licensing is enabled on the Expressway then you cannot use any option keys and they have no effect on the system.

The Option keys page ( Maintenance > Option keys ) lists options currently installed on the Expressway and lets you add new ones. The System information section summarizes the existing features installed on the Expressway and displays the validity period of each installed key.

We are phasing out option keys, and from version X12.6 or for any CE1200-based appliance or later, only these keys are valid
                              for (PAK-based) Expressway systems:

Rich Media Sessions : Determines the number of non-Unified Communications calls allowed on the Expressway (or Expressway cluster) at any one time.
                                    See the Call Types and Licensing section for more information.

TelePresence Desktop Systems : Adds to the number of desktop systems that may register to the Expressway.

TelePresence Room Systems : Adds to the number of room systems that may register to the Expressway.

HSM : Enables Hardware Security Module support on Expressway. HSM functionality may be Preview status only depending on the Expressway software version; please check the release notes for your Expressway version before you use HSM.

Advanced Account Security: Enables advanced security features and restrictions for high-security installations.

Microsoft Interoperability : Enables encrypted calls to and from Microsoft Lync 2010 Server (for both native SIP calls and calls interworked from H.323).
                                    Also required by the Lync B2BUA when establishing ICE calls to Lync 2010 clients. Required for all types of communication with Lync 2013.

Expressways running older software may also use some or all of the following option keys, depending on the software version:

Expressway Series : Identifies and configures the product for Expressway Series system functionality.

Traversal Server : Enables the Expressway to work as a firewall traversal server.

Encryption : Indicates that AES encryption is supported by this software build.

H.323 to SIP Interworking gateway : Enables H.323 calls to be translated to SIP and vice versa.

### Adding Keys

This task only applies if you use PAK-based licensing, as option keys are invalid with Smart Licensing. You can add option
                                 keys through the web UI or the CLI.

As well as these instructions, a video demonstration of the process - provided by Cisco TAC engineers - is available on the Expressway/VCS Screencast Video List page.

65 option key limit

If you try to add more than 65 option keys (licenses), they appear as normal on the Option keys page. However, only the first 65 keys take effect. Additional keys from 66 onwards appear to be added, but actually the Expressway
                                 does not process them. CDETS CSCvf78728 refers.

#### Before you start

Have the option keys available.

Remove any demo option keys you already have on the system for the options in question, and restart the system. Otherwise
                                       the feature may stop working when the time-limited demo key expires.

#### Adding option keys using the web UI

In the Add option key field, enter the key for the option you want to add.

Click Add option .

Some option keys need a system restart before they take effect, including:

Traversal Server

Expressway Series

Advanced Account Security (if moved into FIPS mode)

If a restart is required, you get an alarm on the web interface, which remains as a notification until you restart. You can
                                 continue to use and configure the Expressway in the meantime.

#### Adding option keys using the CLI

To return the indexes of all the option keys that are already installed on your system:

To add a new option key to your system:

When using the CLI to add an extra option key, use any unused option index. To see which indexes are currently in use, type xConfiguration option . If you choose an existing option index, it will get overwritten and the functionality provided by that option key will no
                                             longer exist.

## Call Types and Licensing

### Call Types

Expressway distinguishes between the following types of call:

Registered. That is, room and desktop registrations

Rich Media Sessions (RMS)

#### Registered

Calls between locally registered endpoints (registered to Unified CM or Expressway) do not consume licenses, as that entitlement
                                 is included within the registration. The call entitlement within the registration license includes the following scenarios:

Calls to other endpoints registered to Unified CM or Expressway within the same network, when the call is routed through a
                                       neighbor or traversal zone.

Unified CM remote sessions. These are Mobile and Remote Access (MRA) calls – video or audio calls from devices located outside
                                       the enterprise that are routed via the Expressway firewall traversal solution to endpoints registered to Unified CM.

Calls to Cisco conferencing resources (CMR, TelePresence Server/ TelePresence Conductor, or Acano servers).

These calls are still counted against the physical limit of the box.

Expressway does not support ICE candidates in the SDP of a 1xx Provisional Message

#### RMS

These calls consume RMS licenses and consist of every other type of video or audio call that is routed through the Expressway.
                                 RMS licenses are consumed on the exit node of the Expressway in the following scenarios:

B2B

Jabber Guest

Interworked or gatewayed calls to third-party solutions (If the third-party endpoint is not registered to Cisco infrastructure)

Expressway may take the media or just the signaling.

Audio-only SIP calls are treated distinctly from video SIP calls. Each RMS license allows either 1 video call or 2 audio only
                                 SIP calls. So for example, a 100 RMS license would allow 90 video and 20 SIP audio-only simultaneous calls. Any other type
                                 of audio-only call uses an RMS license.

Expressway defines an "audio-only" SIP call as one that was negotiated with a single "m=" line in the SDP. For example, if a person makes a "telephone" call but the SIP UA includes an additional m= line in the SDP, the call will use a video call license.

While an "audio-only" SIP call is being established, it is treated (licensed) as a video call. It only becomes licensed as "audio-only" when the call setup has completed. This means that if your system approaches its maximum licensed limit, you may be unable
                                                   to connect some "audio-only" calls if they are made simultaneously.

The Expressway does not support midcall license optimization.

For deployments with TelePresence Conductor, license consumption is only applicable when TelePresence Conductor is deployed
                                                   with a B2BUA base configuration and not in a policy server base deployment.

SIP to H.323 interworking uses an RMS license (if any of the endpoints are not registered to cisco infrastructure) on the
                                                   node where interworking takes place.

### Room and Desktop Registrations on Expressway

If Expressway is configured as a SIP registrar or H.323 Gatekeeper, it needs to be licensed for concurrent systems (the Unified
                                 CM model) and not for concurrent calls.

For SIP deployments, you do this by adding either or both of the following license types to the Cisco Expressway-C or Cisco
                                 Expressway-E:

TelePresence Room System License

Desktop System License

The following SIP devices register as desktop systems; all other devices are considered room systems:

Cisco TelePresence EX60

Cisco TelePresence EX90

Cisco Webex DX70

Cisco Webex DX80

If you use Cisco Jabber Video for TelePresence (Movi) soft clients (now end-of-sale), they also register to Expressway as
                                       desktop systems.

To register as desktop systems (for SIP), DX systems must be running version CE8.2 or later, and EX systems must be running
                                             TC7.3.6 or later. DX and EX systems running earlier versions still register for SIP, but will consume a room system license.

For H.323 deployments, all endpoints consume a TelePresence Room System License. This is due to a limitation in H.323, which
                                 does not determine the difference between desktop and room type endpoints. We therefore recommend SIP as the preferred signaling
                                 protocol, although H.323 is available as a fall back for endpoints that do not support SIP.

#### Licensing considerations when Expressway is the SIP registrar / H.323 Gatekeeper

Option keys containing licenses for local registrations are installed on the Cisco Expressway-C and/or the Cisco Expressway-E
                                       depending on where the endpoints are registered. These licenses are pooled in a cluster, which means that Expressway peers
                                       can use each others' licenses. However, rooms cannot use desktop licenses, and desktop systems cannot use room licenses.

Registrations from outside the network are proxied to Expressway-C by the Expressway-E. The same domain cannot also be used
                                       for direct Expressway-E registrations.

If you have existing licenses on the Expressway-C and want to register some or all of your existing licensed endpoints to
                                       the Expressway-E, manually delete the relevant licenses from the Expressway-C and reload them on the Expressway-E.

The Large VM and the CE1200 and CE1100 appliances can support up to 5000 registrations, subject to the appropriate licensing.
                                       For MRA registrations (proxied to CUCM) the limits are 5000 for the CE1200, and 2500 for the Large VM and the CE1100. Local
                                       registrations, proxy registrations (via Expressway-E) and MRA registrations all count towards the registration limit.

Proxy registration is possible with SIP endpoints only and does not apply to H.323 endpoints.

FindMe device provisioning is supported with Cisco TMSPE (although this support is deprecated from Expressway version X12.5).

#### Licensing considerations if device registers as both SIP and H.323

Be aware that multiple licenses are consumed if the same device registers to Expressway both as SIP and as H.323. For example,
                                 say a DX80 is registered on Expressway-C as a SIP user agent, and also as an H.323 endpoint (with the same or different URL/DN).
                                 A Desktop System License will be consumed for the SIP registration, and a TelePresence Room System License will be consumed
                                 for the H.323 endpoint registration. The same dual license usage would apply, for example, if a Cisco Webex Room similarly
                                 registers for both SIP and H.323.

#### RMS license usage

The licensing model reduces the usage of Rich Media Session (RMS) licenses in the following scenarios:

If you have already paid for a registration license, RMS licenses are not used for the following call types:

Calls between registered systems. Here, "registered systems" means systems registered directly to the Expressway, by proxy to the Expressway-C through the Expressway-E, or by proxy through
                                             the Expressway pair (MRA) to neighbored Unified CMs.

Calls from registered systems (as above) to Cisco infrastructure. Currently, this extends only to Cisco Meeting Server, and
                                             to CiscoTelePresence Server and TelePresence MCUs that are managed by TelePresence Conductor. However, calls from MCUs that
                                             are not managed by Conductor do use RMS licenses.

Calls from registered systems (as above) to Cisco Collaboration Cloud.

Calls from registered systems to all other systems use one RMS license. Including, but not limited to, the following call
                                       types:

Business to business calls. Require one RMS license on Expressway-E.

Business to consumer calls (Jabber Guest). Require one RMS license on the Expressway-E.

Interoperability gateway calls, including Microsoft Lync / Skype for Business and third-party call control servers require
                                             one RMS license on the Expressway-C.

### License Usage for Device Registrations

Devices that are directly registered on Expressway (Cisco Expressway-C or Cisco Expressway-E) consume licenses as follows:

SIP. Cisco TelePresence EX60, Cisco TelePresence EX90, Cisco DX70, and Cisco DX80 endpoints consume a desktop license. Other
                                    SIP endpoints consume a room system license.

H.323. Each registered H.323 endpoint consumes a room system license.

SIP proxy registrations on the Cisco Expressway-C consume the same licenses as for direct SIP registrations. SIP proxy registrations
                              on the Cisco Expressway-E do not consume licenses.

Registrations are counted per alias , not per device (IP address). So a registration request with multiple aliases, like an MCU, consumes multiple room licenses
                                          even if only a single device is registered on Expressway.

### RMS License Consumption Table

This table lists the scenarios in which Expressway consumes RMS licenses. References to "Third-party Gatekeeper" mean the gatekeeper is connected to Expressway-C; references to "External" mean the gatekeeper is connected to Expressway-E.

Calling endpoint registered to ...

Called endpoint registered to...

Expressway-C

Expressway-E

Unified CM

Expressway-C (Lync)

1 Expressway-C (Lync Gateway)

0

Unified CM

External

0

1

Unified CM

Third-party Gatekeeper

1

0

Expressway-C

External

0

1

Expressway-C (Remote [SIP] - proxy)

External

0

1

Expressway-C (SIP)

Third-party Gatekeeper

1

0

Expressway-C (H323)

Third-party Gatekeeper

1

0

Expressway-C (Remote [SIP]) - proxy

Third-party Gatekeeper

1

0

Expressway-C

Expressway-C (Lync)

0

1 Expressway-C (Lync Gateway)

Expressway-C (Remote)

Expressway-C (Lync)

0

1 Expressway-C (Lync Gateway)

Expressway-C (SIP)

Third-party SIP server

1

0

Expressway-C (H323)

Third-party SIP server

1

0

Expressway-E (SIP)

External

-

1

Expressway-E (H.323)

External

-

1

### License Bypass for Calls to Collaboration Meeting Rooms (CMRs)

The Expressway no longer requires rich media session licenses for calls to and from cloud-based CMRs. This includes SIP/ H.323
                                 calls between Collaboration Cloud and the CMR Hybrid solution.

This only applies when the dialed string does not need transformation on the Expressway (for example, user@sitename.webex.com).

Although untransformed SIP calls to cloud-based CMRs do not use licenses, they do use resources and may not progress if the
                                 Expressway is at full capacity.

There is no license bypass for CMR Premises calls. H.323 calls to cloud-based CMRs consume CMR licenses but not RMS licenses.

## License Usage for Clustered Systems

### PAK-based Licenses

For classic (PAK-based) licensing these license types are pooled for use by any peer in a cluster, irrespective of which peer
                              the licenses are installed on:

RMS licenses

TURN relay licenses (systems running pre-X8.11 software)

We recommend where possible to distribute licenses evenly across all of the peers in a cluster. To see a summary of the licenses
                              installed on each cluster peer, go to the Option keys page and scroll to Current licenses .

If a cluster peer becomes unavailable, the shareable licenses installed on that peer remain available to the rest of the cluster
                              peers for two weeks from the time the cluster lost contact with the peer. This temporarily retains the overall license capacity
                              of the cluster (although note that each peer is limited by its physical capacity). After the two week period the licenses
                              associated with the unavailable peer are removed from the cluster. If you need to maintain the same capacity for the cluster
                              and the unavailable peer can't be fixed, you'll need to install new option keys on another peer.

## Intracluster Calls

License usage when endpoints are registered to different peers in the same cluster, depends on call media traversal across
                              the cluster:

If call media does not traverse the cluster peers, a call between the endpoints does not use any RMS licenses (it's a "Registered" call).

If any of the endpoint is not registered to Cisco infrastructure then calls will use RMS license.

If call media does traverse the cluster peers, a call between the endpoints uses an RMS license on the Expressway where the
                                    B2BUA is engaged.

If both the endpoints are registered to Cisco infrastructure then call will not use RMS license.

### Usage Limits

Usage limits have two aspects: physical capacity and licensing. The physical constraints of the Expressway cluster determine
                                 the ultimate limits, and within that the capacity available to the system is determined by its licensing.

#### Physical capacity limits

The maximum number of licenses that each Expressway peer can actually use depends on the physical capacity of the appliance
                                 or VM. For example, the maximum capacity supported by a large Expressway VM is 500 concurrent video calls.

Capacity alarms are raised if either of the following usage thresholds are reached:

Number of concurrent calls reaches 90% of the capacity of the cluster.

Number of concurrent calls on any one unit reaches 90% of the physical capacity of the unit.

#### License limits

The licensed capacity of a cluster will depend on whether the system uses classic PAK-based licensing, or smart licensing.
                                 For PAK-based, for example, if two large VMs are clustered and each has 300 RMS licenses installed, the effective capacity
                                 of the cluster is 600 concurrent video calls. If one peer is removed from the cluster, the remaining peer retains all 600
                                 RMS licenses for 14 days, but only supports up to 500 concurrent video calls.

For smart licensed systems, the licensed capacity depends on the license pool that's assigned to your organization's registered
                                 account with the Cisco Smart Software Manager.

## About Smart Licensing

This section applies if you use Smart Licensing for Expressway Series systems, available from version X12.6. (Smart Licensing
                           is not supported on Cisco VCS systems.) If you use PAK licensing, see Managing Option Keys instead.

### How Smart Licensing Works

Cisco Smart Software Licensing (Smart Licensing) is a new approach to licensing which is enabled across Cisco products. It
                                 simplifies licensing and makes license ownership and consumption clearer. Devices self-register and report license consumption,
                                 which removes the need to use option keys (Product Activation Keys). License entitlements are pooled in a single account.
                                 You can use a license on any compatible device owned by your company and move them around to meet the needs of your organization.

You use Smart Licensing to register Expressway with the Cisco Smart Software Manager--or the Cisco Smart Software Manager
                                 On-Prem (see below). From there you can manage licenses and monitor smart license usage.

#### On-premises option - using Smart Software Manager On-Prem

If you do not want to manage Cisco products directly using Cisco Smart Software Manager, either for policy or network availability
                                 reasons, you can instead use Smart Software Manager On-Prem. This is an on-premises component of Cisco Smart Licensing and
                                 products register and report license consumption to it in the same way as with Cisco Smart Software Manager.

Smart Software Manager On-Prem can be deployed in either Connected or Disconnected mode, depending on whether the satellite
                                 can connect directly to cisco.com.

Connected . Used when there is direct connectivity to cisco.com. Smart account synchronization occurs automatically.

Disconnected . Used when there is no direct connectivity to cisco.com. Smart Account synchronization must be manually uploaded and downloaded.

#### More information

For detailed product information about the Cisco Smart Software Manager, see Cisco Smart Software Manager . Or for information about the on-prem manager, see Smart Software Manager On-Prem .

## Before You Enable Smart Licensing

This section has some caveats to be aware of before you implement Smart Licensing on Expressway.

After Smart Licensing is enabled, the only way to revert to PAK-based licensing (or to convert an Expressway system to a Cisco
                                          VCS system) is with a factory reset. Because a factory reset reinstalls the software image and resets the Expressway configuration
                                          to the default, we strongly advise you to backup the Expressway data before you enable Smart Licensing.

### Product Instance Evaluation Mode

After enabling Smart Licensing, Expressway runs under a 90-day evaluation period. During the evaluation period Expressway
                              does not allow any cluster-related configuration. After the evaluation period, if Expressway is not registered with either
                              CSSM or Smart Software Manager On-Prem, the product moves to Unauthorized state and does not allow new device registrations
                              until the product is registered.

After Smart Licensing is enabled, you cannot use option keys on the Expressway. So if you want to use any Expressway functions
                              that still require option keys, you need to use PAK-based licensing.

We recommend that you review the general Expressway licensing information in Call Types and Licensing .

You need to set up Smart and Virtual accounts. For details, see Cisco Smart Accounts .

## Smart Licensing Settings

This section describes how to use the Smart Licensing settings in the Expressway web interface to do the following:

Enable Smart Licensing.

Register and deregister the Expressway with CSSM or Smart Software Manager On-Prem.

Manually renew the registration and license authorization.

View system license usage information as it is reported to CSSM or Smart Software Manager On-Prem. (Licenses are assigned
                                    to your organization's Smart Account and are not locked to a device.)

This section describes the web interface. For information about CLI commands for Smart Licensing, see the Command Reference section of this guide.

Field

Description

Smart licensing mode

Enables Smart Licensing on this Expressway product instance. Before you select this option, review the Smart Licensing Settings section.

Transport settings

Determines how this Expressway product instance communicates with CSSM to send and receive usage information.

If the Expressway product instance is already registered, you must first deregister it if you want to change transport settings
                                                      from Direct (CSSM) to On-Prem, or the other way round.

Direct : Expressway sends usage information directly over the internet and no additional components are needed. This is the default
                                          setting.

To use the Direct option, you must configure DNS settings on Expressway so that it can resolve cisco.com .

If you choose not to configure the domain and DNS on Expressway, you can instead select Smart Software Manager On-Prem or
                                          proxy server. If you choose not to use the DNS server in your deployment and not to connect to the internet, you can select
                                          the Smart Software Manager On-Prem with manual synchronization in disconnected mode.

Smart Software Manager On-Prem : Expressway sends usage information to an on-premise CSSM. Periodic information exchange keeps the databases in sync between
                                          Smart Software Manager On-Prem and CSSM.

In the URL field, be sure to enter the exact Smart Transport URL of Smart Software Manager On-Prem . Enter the protocol and FQDN of the satellite server prefixed to " SmartTransport " . This is an example of a valid transport URL: https://example.com/SmartTransport

For more information about installing or configuring Smart Software Manager On-Prem, see https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager.html .

Proxy Server : Optionally you can use this setting to have Expressway send usage information over the internet through a proxy server.
                                          Enter the following details:

Proxy address IPv4 address or FQDN of the proxy server.

Port Port on which the proxy server is listening for requests.

Username Username for authorizing requests at the proxy server.

Password Password for authenticating the authorized user.

Do not share my hostname or IP address with Cisco

Check this check box if the hostname and IP address of this Expressway product instance must not be exchanged with CSSM or
                                          Cisco Smart Software Manager On-Prem

Additional operations

The Additional operations drop-down list is activated after a successful registration.

Renew authorization now : Perform this operation if automatic authorization status renewal fails due to network connectivity issues with CSSM.

Renew registration now : Perform this operation if automatic registration renewal fails due to network connectivity issues with CSSM.

Deregister : The product reverts to Unregistered mode. All license entitlements used for the product are released immediately to the
                                                virtual account and are available for other product instances to use it. If the evaluation period has not expired, the product
                                                reverts to evaluation mode.

Product Instance Registration token

Enter the Product Instance Registration token that you generated from CSSM or Smart Software Manager On-Prem to register the
                                          product.

Reregister this product instance if it is already registered

Check this check box to reregister this Expressway product instance to a different virtual account.

Register

Click Register to register the Expressway with CSSM or Smart Software Manager On-Prem. (Changes to Reregister after successful registration.)

Licensing status

Registration status

Displays the registration status of this Expressway product instance:

Registered : Product is registered.

Unregistered : Product is not registered.

Unregistered : Registration Expired : Registration has expired for this product.

Unregistered : Registration Pending : Registration is in progress.

Unregistered : Registration Failed : Product registration failed because the token is invalid or expired.

License authorization status

Displays the license authorization status of this Expressway product instance.

Authorized : Product is authorized and in compliance state.

Authorization Expired : Authorization has expired. This usually happens if the product has not communicated with Cisco for 90 continuous days.

Out-of-compliance : Status for this product is out-of-compliance, due to insufficient licenses.

No Licenses in Use : No licenses are being consumed by the product.

Evaluation Mode : Product is in evaluation mode and not yet registered with Cisco.

Evaluation Expired : Evaluation period has expired.

Not Applicable : Product is unable to determine the current registration status.

Smart account

Displays information about the customer's Smart Account with Cisco. The Smart Account is created from the Request Smart Account option under the Administration section of Cisco Software Central .

Virtual account

A self-defined element to reflect the company organization. Licenses and Product instances can be distributed across virtual
                                          accounts. Created and maintained by an administrator on CSSM or Smart Software Manager On-Prem. The administrator needs full
                                          visibility to company assets.

Export-Controlled Functionality

Displays one of the following states:

Allowed : Export-controlled functionality is enabled in the token with which this product was registered.

Not Allowed : Export-controlled functionality is not enabled in the token with which this product was registered.

The Allow export-controlled functionality on the products registered with this token check box is not displayed for Smart Accounts that are not allowed to use Export-Controlled functionality.

License usage

Update usage details

License usage provides summary and detailed information on system license usage as it's reported to CSSM or Smart Software
                                          Manager On-Prem. The information is auto-updated every 6 hours.

Optionally you can manually update the usage details by clicking Update usage details . However, this is a resource intensive operation and we don't recommend using it frequently. It may take upwards of a minute
                                          depending on the size of the system.

License type

Lists the license types—rich media session or room/desktop registrations.

Current usage

Shows current license usage by license type. If a license type is not in use (being consumed) it is not displayed here.

Status

Displays the status of each license type.

Authorization Expired : Authorized period has expired.

Evaluation Mode : The agent is using the evaluation period for this entitlement.

Evaluation Expired : Evaluation period has expired.

Authorized : In compliance (authorized).

Invalid : Error condition state.

Invalid-tag : The entitlement tag is invalid.

Not Authorized : Enforcement mode is not applicable.

Out of compliance : Out of compliance.

Waiting : The initial state after an entitlement request while waiting for the authorization request response.

## Configure Smart Licensing

This section describes the tasks required to configure Smart Licensing.

### Before You Start

Review the cautions and other information in Before you Enable Smart Licensing .

The following additional configuration caveats apply:

The only supported transport protocol is HTTPS between Expressway and CSSM / Smart Software Manager On-Prem.

If a communication issue occurs with the registration server when you register the Expressway product instance, the registration
                                       fails with this message: The last attempt to renew smart software licensing registration is in progress because of the following reason: HTTP Server
                                          Error 200: Operation timed out .

The product instance reattempts to register at 15-minute intervals. Refresh the page on your browser after each reattempt,
                                       to check current registration status. If the communication issue is resolved during the reattempts, the product will be registered.
                                       If the product is not registered after multiple reattempts, verify if there is any communication issue with the registration
                                       server and manually reregister the product instance.

When you restore a system, the Smart Licensing settings that are restored depends on whether you restore the backup onto the
                                       same system or on a different system.

If you restore on the same system, Smart Licensing will be enabled and the registration settings are restored on the restored
                                             system.

If you restore on a different system, Smart Licensing will be enabled on the restored system but you must register the product
                                             again with a registration key.

If you are configuring Smart Software Manager On-Prem, be sure to enter the exact URL of the Smart Transport component (details
                                       and an example are provided in Smart Licensing Settings ).

### Process Summary

### Task 1: Obtain the Product Instance Registration Token

Log in to your smart account in CSSM or Smart Software Manager On-Prem.

Navigate to the virtual account that you want to associate with the Expressway.

Generate a Product Instance Registration Token.

Select the Allow export-controlled functionality on the products registered with this token check box to enable export-controlled functionality on the products registered with this token.

Use this option only if you are compliant with the export-controlled functionality.

By checking this check box and accepting the terms, you enable higher levels of product encryption for products registered
                                             with this Registration Token. By default, this check box is selected. You can uncheck this check box to disallow Export-Controlled
                                             functionality on a product.

The Allow export-controlled functionality on the products registered with this token check box is not displayed for Smart Accounts that are not permitted to use the Export-Controlled functionality.

Copy the token or save it to another location.

### Task 2: Enable Smart Licensing on Expressway

In the Expressway web interface, go to Maintenance > Smart licensing .

In the Configuration section, set Smart licensing mode to On (default is Off ).

Click Save .

### Task 3: Configure Transport Settings on Expressway

In the Expressway web interface, go to Maintenance > Smart licensing .

Navigate to Transport settings and select one of the following transport options:

Direct Expressway sends usage information directly over the internet and no additional components are needed. This is the default.

Smart Software Manager On-Prem Expressway sends usage information to an on-premise CSSM.

Proxy Server Expressway sends usage information over the internet through a proxy server.

Details about the transport settings are provided in Smart Licensing Settings . Remember that if the Expressway product instance is already registered, you must first deregister it if you want to change
                                             transport settings from Direct (CSSM) to On-Prem, or the other way round.

If the hostname and IP address of this product instance must not be exchanged with CSSM or Cisco Smart Software Manager On-Prem,
                                          check the setting Do not share my hostname or IP address with Cisco .

Click Save .

### Task 4: Register with Cisco Smart Software Manager

In the Expressway web interface, go to Maintenance > Smart licensing .

In the Registration section, paste the Product Instance Registration Token that you previously generated using CSSM or Smart Software Manager
                                          On-Prem.

Click Register to complete the registration process. (After successful registration the button changes to Reregister .)

In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system.

The configuration for Smart Licensing is now complete.

The following section describes how to manage Smart Licensing registrations and authorizations, including what to do if the
                                             Expressway hostname is changed in future, or if you decide to permanently shut it down.

## Manage Smart Licensing Registrations and Authorizations

This section describes Smart Licensing operations, including:

Renew Authorization : Use to manually renew the License authorization status for all the licenses listed under the License type. The license authorization
                                    is renewed automatically every 30 days. The authorization status will expire after 90 days if it is not connected to CSSM
                                    or Smart Software Manager On-Prem.

Renew Registration : Use to renew the registration information manually. The initial registration is valid for one year. Renewal of registration
                                    is automatically done every six months provided the product is connected to CSSM or Smart Software Manager On-Prem.

Deregister : Use to disconnect the Expressway from CSSM or Smart Software Manager On-Prem. The product reverts to evaluation mode as
                                    long as the evaluation period is not expired. All license entitlements used for the product are immediately released back
                                    to the virtual account and are available for other product instances to use it.

Reregister License with Cisco Smart Software Manager : Use to reregister Expressway with CSSM or Smart Software Manager On-Prem. The product may migrate to a different virtual
                                    account by reregistering with a token from a new virtual account.

### Renew Authorization

Use this procedure to manually renew the License authorization status for all the licenses listed under the License type . This process assumes that the product is registered with CSSM or Smart Software Manager On-Prem.

In the Expressway web interface, go to Maintenance > Smart licensing .

In the Action section, from the Additional operations drop-down list, choose Renew authorization now .

Click Save .

Expressway sends a request to Cisco Smart Software Manager or Smart Software Manager On-Prem to check the "License Authorization Status" and Cisco Smart Software Manager or Smart Software Manager On-Prem reports back the status to Cisco Expressway.

In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system.

### Renew Registration

During product registration to Cisco Smart Software Manager or Smart Software Manager On-Prem, a security association is used
                                 to identify the product and is anchored by the registration certificate, which has a lifetime of one year (the registration
                                 period). This is different from the registration token ID expiration, which has the time limit for the token to be active.
                                 This registration period is automatically renewed every 6 months. However, if there is an issue, you can manually renew this
                                 registration period.

This process assumes that the product is registered with CSSM or Smart Software Manager On-Prem.

In the Expressway web interface, go to Maintenance > Smart licensing .

In the Action section, from the Additional operations drop-down list, choose Renew registration now .

Click Save .

Expressway sends a request to CSSM or Smart Software Manager On-Prem to check the "Registration Status" and CSSM / Smart Software Manager On-Prem reports the status to Cisco Unified Communications Manager.

In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system.

### Deregister

Use this procedure to unregister an Expressway from CSSM or Smart Software Manager On-Prem and release all the licenses from
                                 the current virtual account. This procedure also disconnects the Expressway from CSSM / Smart Software Manager On-Prem. All
                                 license entitlements used for the product are released back to the virtual account and are available for other product instances
                                 to use.

If Expressway is unable to connect with CSSM or Smart Software Manager On-Prem, and the product is still deregistered, a warning
                                 message displays. The message notifies you to remove the product manually from CSSM / Smart Software Manager On-Prem to free
                                 up licenses.

In the Expressway web interface, go to Maintenance > Smart licensing .

In the Action section, from the Additional operations drop-down list, choose Deregister .

Click Save .

In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system.

### Reregister with Cisco Smart Software Manager

Use this procedure to reregister the Expressway with CSSM or Smart Software Manager On-Prem. You need the Product Instance
                                 Registration Token (see Manage Smart Licensing Registrations and Authorizations ).

From the web interface, choose Maintenance > Smart licensing .

In the Registration section, paste the "Registration Token Key" that you generated using the CSSM or Smart Software Manager On-Prem.

Click Reregister to complete the reregistration process.

In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system.

### How to Register a Change to the Expressway Hostname

If the Expressway hostname is changed, to reflect the change in CSSM, go to the Expressway Smart Licensing web page and click " Renew Registration Now " .

### Deregister First if Expressway is Permanently Shutdown

We recommend that if you plan to shutdown an Expressway machine permanently, you first deregister the product instance from
                                 the Expressway Smart Licensing web page. This is to avoid leaving unused product instances in CSSM.

In case you forget to do so, there is an alternate approach to remove the Expressway product instance from the CSSM portal.

This step is not needed for restarts or temporary shutdowns.

## Convert PAK-Based Licenses to Smart Licenses

If you currently use PAK-based licensing, this section explains how to convert to Smart Licensing. You can do the license
                              conversion in the License Registration Portal , or you can use Cisco Smart Software Manager if you have an active Cisco Software Support Service contract. You can convert a PAK-based license only when there is an
                              equivalent Smart License available for the PAK.

### Converting Unfulfilled or Partially Fulfilled PAKs

#### Using the License Registration Portal

Log in to License Registration Portal .

Click the PAKs or Tokens tab.

From the Virtual Account drop-down list, select the virtual account with the PAK licenses to be converted.

Check the check boxes next to the unfulfilled or partially fulfilled PAKs that you want to convert.

Click the blue arrow icon and select Covert to Smart Licensing from the drop-down list.

If the licenses are not assigned to a virtual account, select the virtual account from the Virtual Account drop-down list.

In the Quantity to Convert column, enter the number of licenses to covert and click Submit .

At the confirmation message The selected features have been successfully converted to Smart Entitlements , click Close .

Verify the status of the licenses in the Status column. This shows Converted for a complete conversion and Partially for a partial conversion.

#### Using Cisco Smart Software Manager

Log in to Cisco Smart Software Manager .

Click the Convert to Smart Licensing > Converts PAKs tab.

Locate the PAKs to convert and click the Convert to Smart Licensing link in the Actions column.

From the Destination Virtual Account drop-down list, select the destination virtual account.

In the SKUs section, check the SKU/PAK and enter the number of licenses to convert in the Quantity to convert column. If partial fulfillment is not allowed for the SKU, you must convert all licenses in the SKU.

Click Next .

Review the details and click Convert Licenses .

To verify that the PAK licenses are converted successfully, click Inventory > Licenses .

### Converting PAKs Register to Device or Product

#### Using the License Registration Portal

Log in to License Registration Portal .

Click the Devices tab.

From the Virtual Account drop-down list, select the virtual account that is associated to your device or product.

Select the devices that contains the licenses that you want to convert.

Click the blue arrow icon and click Covert licenses to Smart Licensing . The Convert to Smart Entitlements dialog box appears.

If any PAK licenses are not eligible for conversion, the Ineligible status is displayed in the Quantity to Covert column.

Select the virtual account from the Virtual Account drop-down list.

Select the SKUs and select the number of licenses that you want to convert.

Click Submit .

After the license conversion is complete, the Smart Entitlements (licenses) are reflected in your Smart Account in CSSM.

#### Using Cisco Smart Software Manager

Log in to Cisco Smart Software Manager .

Click Convert to Smart Licensing > Convert Licenses .

Select the device that contains the licenses that you want to convert and click the Convert to Smart Licensing link in the Actions column.

From the Destination Virtual Account field, select the destination virtual account. The Convert to Smart Entitlements dialog box appears.

If any PAK licenses are not eligible for conversion, the Ineligible status is displayed in the Quantity to Covert column.

Select the SKUs and enter the number of licenses to convert in the Quantity to Convert column.

Click Next .

Review the details and click Convert Licenses .

To verify that the PAK licenses are converted successfully, click Inventory > Licenses .

| Note | If Smart Licensing is enabled on the Expressway then you cannot use any option keys and they have no effect on the system. |
|---|---|

| Note | When using the CLI to add an extra option key, use any unused option index. To see which indexes are currently in use, type xConfiguration option . If you choose an existing option index, it will get overwritten and the functionality provided by that option key will no
                                             longer exist. |
|---|---|

| Note | These calls are still counted against the physical limit of the box. Expressway does not support ICE candidates in the SDP of a 1xx Provisional Message |
|---|---|

| Note | Expressway defines an "audio-only" SIP call as one that was negotiated with a single "m=" line in the SDP. For example, if a person makes a "telephone" call but the SIP UA includes an additional m= line in the SDP, the call will use a video call license. While an "audio-only" SIP call is being established, it is treated (licensed) as a video call. It only becomes licensed as "audio-only" when the call setup has completed. This means that if your system approaches its maximum licensed limit, you may be unable
                                                   to connect some "audio-only" calls if they are made simultaneously. The Expressway does not support midcall license optimization. For deployments with TelePresence Conductor, license consumption is only applicable when TelePresence Conductor is deployed
                                                   with a B2BUA base configuration and not in a policy server base deployment. SIP to H.323 interworking uses an RMS license (if any of the endpoints are not registered to cisco infrastructure) on the
                                                   node where interworking takes place. |
|---|---|

| Note | To register as desktop systems (for SIP), DX systems must be running version CE8.2 or later, and EX systems must be running
                                             TC7.3.6 or later. DX and EX systems running earlier versions still register for SIP, but will consume a room system license. |
|---|---|

| Note | Registrations are counted per alias , not per device (IP address). So a registration request with multiple aliases, like an MCU, consumes multiple room licenses
                                          even if only a single device is registered on Expressway. |
|---|---|

| Calling endpoint registered to ... | Called endpoint registered to... | Expressway-C | Expressway-E |
|---|---|---|---|
| Unified CM | Expressway-C (Lync) | 1 Expressway-C (Lync Gateway) | 0 |
| Unified CM | External | 0 | 1 |
| Unified CM | Third-party Gatekeeper | 1 | 0 |
| Expressway-C | External | 0 | 1 |
| Expressway-C (Remote [SIP] - proxy) | External | 0 | 1 |
| Expressway-C (SIP) | Third-party Gatekeeper | 1 | 0 |
| Expressway-C (H323) | Third-party Gatekeeper | 1 | 0 |
| Expressway-C (Remote [SIP]) - proxy | Third-party Gatekeeper | 1 | 0 |
| Expressway-C | Expressway-C (Lync) | 0 | 1 Expressway-C (Lync Gateway) |
| Expressway-C (Remote) | Expressway-C (Lync) | 0 | 1 Expressway-C (Lync Gateway) |
| Expressway-C (SIP) | Third-party SIP server | 1 | 0 |
| Expressway-C (H323) | Third-party SIP server | 1 | 0 |
| Expressway-E (SIP) | External | - | 1 |
| Expressway-E (H.323) | External | - | 1 |

| Note | This only applies when the dialed string does not need transformation on the Expressway (for example, user@sitename.webex.com). |
|---|---|

| Caution | After Smart Licensing is enabled, the only way to revert to PAK-based licensing (or to convert an Expressway system to a Cisco
                                          VCS system) is with a factory reset. Because a factory reset reinstalls the software image and resets the Expressway configuration
                                          to the default, we strongly advise you to backup the Expressway data before you enable Smart Licensing. |
|---|---|

| Note | This section describes the web interface. For information about CLI commands for Smart Licensing, see the Command Reference section of this guide. |
|---|---|

| Field | Description |
|---|---|
| Smart licensing mode | Enables Smart Licensing on this Expressway product instance. Before you select this option, review the Smart Licensing Settings section. |
| Transport settings | Determines how this Expressway product instance communicates with CSSM to send and receive usage information. Caution If the Expressway product instance is already registered, you must first deregister it if you want to change transport settings
                                                      from Direct (CSSM) to On-Prem, or the other way round. Direct : Expressway sends usage information directly over the internet and no additional components are needed. This is the default
                                          setting. To use the Direct option, you must configure DNS settings on Expressway so that it can resolve cisco.com . If you choose not to configure the domain and DNS on Expressway, you can instead select Smart Software Manager On-Prem or
                                          proxy server. If you choose not to use the DNS server in your deployment and not to connect to the internet, you can select
                                          the Smart Software Manager On-Prem with manual synchronization in disconnected mode. Smart Software Manager On-Prem : Expressway sends usage information to an on-premise CSSM. Periodic information exchange keeps the databases in sync between
                                          Smart Software Manager On-Prem and CSSM. In the URL field, be sure to enter the exact Smart Transport URL of Smart Software Manager On-Prem . Enter the protocol and FQDN of the satellite server prefixed to " SmartTransport " . This is an example of a valid transport URL: https://example.com/SmartTransport For more information about installing or configuring Smart Software Manager On-Prem, see https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager.html . Proxy Server : Optionally you can use this setting to have Expressway send usage information over the internet through a proxy server.
                                          Enter the following details: Proxy address IPv4 address or FQDN of the proxy server. Port Port on which the proxy server is listening for requests. Username Username for authorizing requests at the proxy server. Password Password for authenticating the authorized user. | Caution | If the Expressway product instance is already registered, you must first deregister it if you want to change transport settings
                                                      from Direct (CSSM) to On-Prem, or the other way round. |
| Caution | If the Expressway product instance is already registered, you must first deregister it if you want to change transport settings
                                                      from Direct (CSSM) to On-Prem, or the other way round. |
| Do not share my hostname or IP address with Cisco | Check this check box if the hostname and IP address of this Expressway product instance must not be exchanged with CSSM or
                                          Cisco Smart Software Manager On-Prem |
| Additional operations | The Additional operations drop-down list is activated after a successful registration. Renew authorization now : Perform this operation if automatic authorization status renewal fails due to network connectivity issues with CSSM. Renew registration now : Perform this operation if automatic registration renewal fails due to network connectivity issues with CSSM. Deregister : The product reverts to Unregistered mode. All license entitlements used for the product are released immediately to the
                                                virtual account and are available for other product instances to use it. If the evaluation period has not expired, the product
                                                reverts to evaluation mode. |
| Product Instance Registration token | Enter the Product Instance Registration token that you generated from CSSM or Smart Software Manager On-Prem to register the
                                          product. |
| Reregister this product instance if it is already registered | Check this check box to reregister this Expressway product instance to a different virtual account. |
| Register | Click Register to register the Expressway with CSSM or Smart Software Manager On-Prem. (Changes to Reregister after successful registration.) |
| Licensing status |
| Registration status | Displays the registration status of this Expressway product instance: Registered : Product is registered. Unregistered : Product is not registered. Unregistered : Registration Expired : Registration has expired for this product. Unregistered : Registration Pending : Registration is in progress. Unregistered : Registration Failed : Product registration failed because the token is invalid or expired. |
| License authorization status | Displays the license authorization status of this Expressway product instance. Authorized : Product is authorized and in compliance state. Authorization Expired : Authorization has expired. This usually happens if the product has not communicated with Cisco for 90 continuous days. Out-of-compliance : Status for this product is out-of-compliance, due to insufficient licenses. No Licenses in Use : No licenses are being consumed by the product. Evaluation Mode : Product is in evaluation mode and not yet registered with Cisco. Evaluation Expired : Evaluation period has expired. Not Applicable : Product is unable to determine the current registration status. |
| Smart account | Displays information about the customer's Smart Account with Cisco. The Smart Account is created from the Request Smart Account option under the Administration section of Cisco Software Central . |
| Virtual account | A self-defined element to reflect the company organization. Licenses and Product instances can be distributed across virtual
                                          accounts. Created and maintained by an administrator on CSSM or Smart Software Manager On-Prem. The administrator needs full
                                          visibility to company assets. |
| Export-Controlled Functionality | Displays one of the following states: Allowed : Export-controlled functionality is enabled in the token with which this product was registered. Not Allowed : Export-controlled functionality is not enabled in the token with which this product was registered. The Allow export-controlled functionality on the products registered with this token check box is not displayed for Smart Accounts that are not allowed to use Export-Controlled functionality. |
| License usage |
| Update usage details | License usage provides summary and detailed information on system license usage as it's reported to CSSM or Smart Software
                                          Manager On-Prem. The information is auto-updated every 6 hours. Optionally you can manually update the usage details by clicking Update usage details . However, this is a resource intensive operation and we don't recommend using it frequently. It may take upwards of a minute
                                          depending on the size of the system. |
| License type | Lists the license types—rich media session or room/desktop registrations. |
| Current usage | Shows current license usage by license type. If a license type is not in use (being consumed) it is not displayed here. |
| Status | Displays the status of each license type. Authorization Expired : Authorized period has expired. Evaluation Mode : The agent is using the evaluation period for this entitlement. Evaluation Expired : Evaluation period has expired. Authorized : In compliance (authorized). Invalid : Error condition state. Invalid-tag : The entitlement tag is invalid. Not Authorized : Enforcement mode is not applicable. Out of compliance : Out of compliance. Waiting : The initial state after an entitlement request while waiting for the authorization request response. |

| Caution | If the Expressway product instance is already registered, you must first deregister it if you want to change transport settings
                                                      from Direct (CSSM) to On-Prem, or the other way round. |
|---|---|

| Step 1 | Log in to your smart account in CSSM or Smart Software Manager On-Prem. |
|---|---|
| Step 2 | Navigate to the virtual account that you want to associate with the Expressway. |
| Step 3 | Generate a Product Instance Registration Token. |
| Step 4 | Select the Allow export-controlled functionality on the products registered with this token check box to enable export-controlled functionality on the products registered with this token. Caution Use this option only if you are compliant with the export-controlled functionality. By checking this check box and accepting the terms, you enable higher levels of product encryption for products registered
                                             with this Registration Token. By default, this check box is selected. You can uncheck this check box to disallow Export-Controlled
                                             functionality on a product. The Allow export-controlled functionality on the products registered with this token check box is not displayed for Smart Accounts that are not permitted to use the Export-Controlled functionality. | Caution | Use this option only if you are compliant with the export-controlled functionality. |
| Caution | Use this option only if you are compliant with the export-controlled functionality. |
| Step 5 | Copy the token or save it to another location. |

| Caution | Use this option only if you are compliant with the export-controlled functionality. |
|---|---|

| Step 1 | In the Expressway web interface, go to Maintenance > Smart licensing . |
|---|---|
| Step 2 | In the Configuration section, set Smart licensing mode to On (default is Off ). |
| Step 3 | Click Save . |

| Step 1 | In the Expressway web interface, go to Maintenance > Smart licensing . |
|---|---|
| Step 2 | Navigate to Transport settings and select one of the following transport options: Direct Expressway sends usage information directly over the internet and no additional components are needed. This is the default. Smart Software Manager On-Prem Expressway sends usage information to an on-premise CSSM. Proxy Server Expressway sends usage information over the internet through a proxy server. Details about the transport settings are provided in Smart Licensing Settings . Remember that if the Expressway product instance is already registered, you must first deregister it if you want to change
                                             transport settings from Direct (CSSM) to On-Prem, or the other way round. |
| Step 3 | If the hostname and IP address of this product instance must not be exchanged with CSSM or Cisco Smart Software Manager On-Prem,
                                          check the setting Do not share my hostname or IP address with Cisco . |
| Step 4 | Click Save . |

| Step 1 | In the Expressway web interface, go to Maintenance > Smart licensing . |
|---|---|
| Step 2 | In the Registration section, paste the Product Instance Registration Token that you previously generated using CSSM or Smart Software Manager
                                          On-Prem. |
| Step 3 | Click Register to complete the registration process. (After successful registration the button changes to Reregister .) |
| Step 4 | In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system. The configuration for Smart Licensing is now complete. The following section describes how to manage Smart Licensing registrations and authorizations, including what to do if the
                                             Expressway hostname is changed in future, or if you decide to permanently shut it down. |

| Step 1 | In the Expressway web interface, go to Maintenance > Smart licensing . |
|---|---|
| Step 2 | In the Action section, from the Additional operations drop-down list, choose Renew authorization now . |
| Step 3 | Click Save . Expressway sends a request to Cisco Smart Software Manager or Smart Software Manager On-Prem to check the "License Authorization Status" and Cisco Smart Software Manager or Smart Software Manager On-Prem reports back the status to Cisco Expressway. |
| Step 4 | In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system. |

| Step 1 | In the Expressway web interface, go to Maintenance > Smart licensing . |
|---|---|
| Step 2 | In the Action section, from the Additional operations drop-down list, choose Renew registration now . |
| Step 3 | Click Save . Expressway sends a request to CSSM or Smart Software Manager On-Prem to check the "Registration Status" and CSSM / Smart Software Manager On-Prem reports the status to Cisco Unified Communications Manager. |
| Step 4 | In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system. |

| Step 1 | In the Expressway web interface, go to Maintenance > Smart licensing . |
|---|---|
| Step 2 | In the Action section, from the Additional operations drop-down list, choose Deregister . |
| Step 3 | Click Save . |
| Step 4 | In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system. |

| Step 1 | From the web interface, choose Maintenance > Smart licensing . The Smart licensing window appears. |
|---|---|
| Step 2 | In the Registration section, paste the "Registration Token Key" that you generated using the CSSM or Smart Software Manager On-Prem. |
| Step 3 | Click Reregister to complete the reregistration process. |
| Step 4 | In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system. |

| Step 1 | Log in to License Registration Portal . |
|---|---|
| Step 2 | Click the PAKs or Tokens tab. |
| Step 3 | From the Virtual Account drop-down list, select the virtual account with the PAK licenses to be converted. |
| Step 4 | Check the check boxes next to the unfulfilled or partially fulfilled PAKs that you want to convert. |
| Step 5 | Click the blue arrow icon and select Covert to Smart Licensing from the drop-down list. The Convert to Smart Entitlements dialog box appears. |
| Step 6 | If the licenses are not assigned to a virtual account, select the virtual account from the Virtual Account drop-down list. |
| Step 7 | In the Quantity to Convert column, enter the number of licenses to covert and click Submit . |
| Step 8 | At the confirmation message The selected features have been successfully converted to Smart Entitlements , click Close . |
| Step 9 | Verify the status of the licenses in the Status column. This shows Converted for a complete conversion and Partially for a partial conversion. |

| Step 1 | Log in to Cisco Smart Software Manager . |
|---|---|
| Step 2 | Click the Convert to Smart Licensing > Converts PAKs tab. |
| Step 3 | Locate the PAKs to convert and click the Convert to Smart Licensing link in the Actions column. The Convert to Smart Software Licenses dialog box appears. |
| Step 4 | From the Destination Virtual Account drop-down list, select the destination virtual account. |
| Step 5 | In the SKUs section, check the SKU/PAK and enter the number of licenses to convert in the Quantity to convert column. If partial fulfillment is not allowed for the SKU, you must convert all licenses in the SKU. |
| Step 6 | Click Next . |
| Step 7 | Review the details and click Convert Licenses . |
| Step 8 | To verify that the PAK licenses are converted successfully, click Inventory > Licenses . |

| Step 1 | Log in to License Registration Portal . |
|---|---|
| Step 2 | Click the Devices tab. |
| Step 3 | From the Virtual Account drop-down list, select the virtual account that is associated to your device or product. |
| Step 4 | Select the devices that contains the licenses that you want to convert. |
| Step 5 | Click the blue arrow icon and click Covert licenses to Smart Licensing . The Convert to Smart Entitlements dialog box appears. If any PAK licenses are not eligible for conversion, the Ineligible status is displayed in the Quantity to Covert column. |
| Step 6 | Select the virtual account from the Virtual Account drop-down list. |
| Step 7 | Select the SKUs and select the number of licenses that you want to convert. |
| Step 8 | Click Submit . After the license conversion is complete, the Smart Entitlements (licenses) are reflected in your Smart Account in CSSM. |

| Step 1 | Log in to Cisco Smart Software Manager . |
|---|---|
| Step 2 | Click Convert to Smart Licensing > Convert Licenses . |
| Step 3 | Select the device that contains the licenses that you want to convert and click the Convert to Smart Licensing link in the Actions column. |
| Step 4 | From the Destination Virtual Account field, select the destination virtual account. The Convert to Smart Entitlements dialog box appears. If any PAK licenses are not eligible for conversion, the Ineligible status is displayed in the Quantity to Covert column. |
| Step 5 | Select the SKUs and enter the number of licenses to convert in the Quantity to Convert column. |
| Step 6 | Click Next . |
| Step 7 | Review the details and click Convert Licenses . |
| Step 8 | To verify that the PAK licenses are converted successfully, click Inventory > Licenses . |