---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmeover-html-4fc7128203
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmeover.html
retrieved_at: 2026-08-21T07:21:47.060718+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Cisco Unified CME
	 Overview

## Chapter: Cisco Unified CME
	 Overview

# Cisco Unified CME
                     	 Overview

## Important
                        	 Information about Cisco IOS XE 16 Denali

Effective Cisco IOS
                           		XE Release 3.7.0E (for Catalyst Switching) and Cisco IOS XE Release 3.17S (for
                           		Access and Edge Routing) the two releases evolve (merge) into a single version
                           		of converged release—the Cisco IOS XE 16 Denali—providing one release covering
                           		the extensive range of access and edge products in the Switching and Routing
                           		portfolio.

For migration
                           		information related to the Cisco IOS XE 16, see Cisco IOS XE Denali 16.2
                              		  Migration Guide for Access and Edge Routers .

## Unified CME Graphical User Interface Deprecation

From Unified CME Release 12.6 (Cisco IOS XE Gibraltar 16.11.1a Release), the Graphical User Interface (GUI) is no more supported
                           for Unified CME. Hence, the GUI files posted under the name cme-gui-.. , as part of the Unified CME software bundle, is not available for download for Unified CME 12.6 and later releases. We recommend
                           that you use the Command Line Interface (CLI) commands to configure Unified CME.

CME GUI allows configuration of essential SIP phone features.

All the CLI commands related to Unified CME GUI deployment are disabled for Unified CME 12.6 and later releases. The following
                           CLI commands related to Unified CME GUI are disabled:

web admin customer name username { password string | secret { 0 | 5 } string }

web admin system [ name username ] [ password string | secret { 0 | 5 } string ]

web customize load filename

time-webedit

dn webedit

show telephony-service admin

## CTI CSTA Protocol Suite Deprecation

From Unified CME Release 12.6 (Cisco IOS XE Gibraltar 16.11.1a), the Computer Telephony Integration (CTI) Computer Supported
                           Telecommunications Applications (CSTA) protocol suite is no more supported on Unified CME. All the CLI commands related to
                           CTI CSTA are disabled for Unified CME 12.6 and later releases.

The following CLI commands related to CTI CSTA that are configured under voice service voip configuration mode is disabled on Unified CME 12.6 and later releases:

cti shutdown

cti callmonitor

cti csta mode basic

cti message device-id suppress-conversion

cti timeout make-call-prompt

The following CLI commands related to CTI CSTA that are configured under ephone-dn and ephone-template configuration mode is disabled on Unified CME 12.6 and later releases:

cti notify

cti watch

The following CLI commands related to CTI CSTA that are configured under voice register session-server configuration mode are disabled on Unified CME 12.6 and later releases:

cti aware

The following CLI show commands related to CTI CSTA that are configured under show cti ? are disabled on Unified CME 12.6 and later releases:

show cti call

show cti gcid

show cti line-node

show cti session

## Simple Network Management Protocol (SNMP) Support for Unified CME

Unified CME supports Simple Network Management Protocol (SNMP) Management Information Base (MIBs) for monitoring the product
                           status. Unified CME Release 12.6 and later is SNMP Version 3 (SNMPv3) compliant. Unified CME supports the following main SNMP
                           MIB:

CISCO-CCME-MIB

For information on configuration of SNMP version 3 on Unified CME router, see SNMP Configuration Guide .

## Introduction

The Cisco Unified
                                       		  Communications Manager Express System Administrator Guide refers to a phone
                                       		  with SIP firmware as SIP Phone, SIP IP Phone, or Cisco Unified SIP IP phone. A
                                       		  phone with SCCP firmware is referred as SCCP Phone, SCCP IP Phone, or Cisco
                                       		  Unified SCCP IP phone.

It is mandatory to configure the command supplementary-service media-renegotiate under voice service voip configuration mode to enable the supplementary features supported on Unified CME.

It is mandatory to configure the CLI command call-park system application under telephony-service configuration mode to support SIP and mixed mode (SIP and SCCP) features such as Call Park and Call Pick-up in Unified CME.

Configure the CLI commands no supplementary-service sip refer , no supplementary-service sip moved-temporarily under voice service voip configuration mode for call transfer and call forward scenarios in Unified CME.

Cisco Unified
                           		Communications Manager Express (formerly known as Cisco Unified
                           		CallManager Express) is a call-processing application in Cisco IOS software
                           		that enables Cisco routers to deliver key-system or hybrid PBX functionality
                           		for enterprise branch offices or small businesses.

Cisco Unified CME is
                           		a feature-rich entry-level IP telephony solution that is integrated directly
                           		into Cisco IOS software. Cisco Unified CME allows small business customers and
                           		autonomous small enterprise branch offices to deploy voice, data, and IP
                           		telephony on a single platform for small offices, thereby streamlining
                           		operations and lowering network costs.

Cisco Unified CME is
                           		ideal for customers who have data connectivity requirements and also have a
                           		need for a telephony solution in the same office. Whether offered through a
                           		service provider’s managed services offering or purchased directly by a
                           		corporation, Cisco Unified CME offers most of the core telephony features
                           		required in the small office, and also many advanced features not available
                           		with traditional telephony solutions. The ability to deliver IP telephony and
                           		data routing by using a single converged solution allows customers to optimize
                           		their operations and maintenance costs, resulting in a very cost-effective
                           		solution that meets office needs.

A Cisco Unified CME
                           		system is extremely flexible because it is modular. A Cisco Unified CME system
                           		consists of a router that serves as a gateway and one or more VLANs that
                           		connect IP phones and phone devices to the router.

Cisco Unified CME for the Small- and Medium-Size
                              		  Office shows a typical deployment of Cisco Unified CME with several phones and devices
                           		connected to it. The Cisco Unified CME router is connected to the public
                           		switched telephone network (PSTN). The router can also connect to a gatekeeper
                           		and a RADIUS billing server in the same network.

Cisco Unified CME for Service Providers shows a branch office with several Cisco Unified IP phones connected to a
                           		Cisco IAD2430 series router with Cisco Unified CME. The Cisco IAD2430 router is
                           		connected to a multiservice router at a service provider office, which provides
                           		connection to the WAN and PSTN.

A Cisco Unified CME
                           		system uses the following basic building blocks:

Ephone or voice
                                 			 register pool—A software concept that usually represents a physical telephone,
                                 			 although it is also used to represent a port that connects to a voice-mail
                                 			 system, and provides the ability to configure a physical phone using Cisco IOS
                                 			 software. Each phone can have multiple extensions associated with it and a
                                 			 single extension can be assigned to multiple phones. Maximum number of ephones
                                 			 and voice register pools supported in a Cisco Unified CME system is equal to
                                 			 the maximum number of physical phones that can be connected to the system.

Directory
                                 			 number—A software concept that represents the line that connects a voice
                                 			 channel to a phone. A directory number represents a virtual voice port in the
                                 			 Cisco Unified CME system, so the maximum number of directory numbers supported
                                 			 in Cisco Unified CME is the maximum number of simultaneous call connections
                                 			 that can occur. This concept is different from the maximum number of physical
                                 			 lines in a traditional telephony system.

## Licensing

This section provides information on licensing of Cisco Unified Communications Manager Express (Unified CME).

### Cisco Smart Licensing

Cisco Smart Licensing is a software licensing model that provides visibility of ownership and usage through the Cisco Smart
                              Software Manager (CSSM) portal. CSSM is a central license repository that manages licenses across all Cisco products that
                              you own, including Cisco Unified Communications Manager Express (Unified CME). Devices send license usage to CSSM either directly
                              or use an on-premises satellite. Your Smart Account Administrator controls your access to CSSM. Use your Cisco credentials
                              to access the CSSM portal using htttp://software.cisco.com .

Smart Licensing applies to all platform technology (UCK9, Security) and Unified CME feature licenses that the router uses.
                              Unified CME requires one license entitlement (CME_EP) for each configured SIP or SCCP phone.

CSSM shows license usage across all devices that you register to a virtual account. A Virtual Account License Inventory displays
                              the quantity of licenses that you purchase, those licenses in use, and a balance. Alert Insufficient Licenses is displayed if the license balance is below 0.

For example, consider a smart account in CSSM with 50 CME_EP licenses. If you have a single registered Unified CME router
                              with 20 configured phones, the CSSM licenses page shows Purchased as 50, In Use as 20 and Balance as 30.

For more information on Smart Software Manager, see the Cisco Smart Software Manager User Guide .

The CME_EP license count includes all phones configured in the Unified CME, covering both ephones and voice register pools,
                                          regardless of their registration status. This count is updated once a phone type is configured under ephone or voice register
                                          pool configuration. To avoid unnecessary reporting while you configure Unified CME, license usage is reported three minutes
                                          after the last configuration change.

Unified CME Smart Licenses also provide RTU entitlement for routers that are not configured for Smart Licensing.

### Smart License Operation

#### Cisco IOS XE Everest 16.5.1 Release to Cisco IOS XE Fuji 16.9.1 Release

Cisco 4000 Series Integrated Services Router s support Smart Licensing as an alternative to Cisco Software RTU Licensing. Use the license smart enable command to enable Smart Licensing. To disable Smart Licensing, use the no form of the command and reaccept the EULA using the license accept end user agreement configuration command.

#### Cisco IOS XE Gibraltar 16.10.1 Release Onwards

The Cisco RTU Licensing and the CLI license smart enable command are deprecated. Smart Licensing is mandatory from this release.

#### Cisco IOS XE Everest 16.5.1 Release to Cisco IOS XE Amsterdam 17.3.1a Release

Routers configured to use Smart Licensing offer a 90-day evaluation period, during which you can use all the features without
                                 registering to CSSM. A Cisco Unified Communications Manager Express device is associated with CSSM using a registration token.
                                 You can obtain the registration token from the virtual CSSM account or from an on-premises satellite. Once registered, the
                                 evaluation period pauses and you can use the balance later. You cannot renew the evaluation period on its expiry.

Warning

Cisco Unified Communications Manager Express shuts down when the router is unregistered and allowed to pass into the Evaluation
                                             Expired state.

To register the Cisco Unified Communications Manager Express router with CSSM, use license smart register idtoken command. For information on registering the device with CSSM, see Software Activation Configuration Guide .

Upon successful registration, the device sends an authorization request to CSSM for the licenses in use. For each license
                                 type requested, if the Smart Account has sufficient licenses, CSSM responds with Authorized . If the Smart Account does not have sufficient licenses, CSSM responds with Out of Compliance .

Post successful authorization of the request, licenses are bound to the requesting device until the next authorization request
                                 submission.

An authorization request is sent every 30 days or when there is any change in license consumption, to maintain the registration
                                 with CSSM. The authorization expires if you do not update the license request for the router within 90 days. The certificate
                                 issued to identify the router at the time of registration is valid for one year and renewed every six months.

The router displays the License authorization as follows:

```
Router# show license summary
Smart Licensing is ENABLED
Registration:Status: REGISTERED
Smart Account: Call-Manager-Express
Virtual Account: CME Application
Export-Controlled Functionality: Not Allowed
Last Renewal Attempt: None
Next Renewal Attempt: Oct 07 12:08:10 2016 UTC
License Authorization:
Status: AUTHORIZED
Last Communication Attempt: SUCCESS
Next Communication Attempt: May 13 07:11:48 2016 UTC
License Usage:
License                 Entitlement tag            Count     Status
-----------------------------------------------------------------------------
ISR_4351_UnifiedComm... (ISR_4351_UnifiedCommun..)   1       AUTHORIZED
CME v12 Endpoint Lic... (CME_EP)                     4       AUTHORIZED
```

#### Cisco IOS XE Gibraltar 16.12.1 Release to Cisco IOS XE Amsterdam 17.3.1a Release

Specific License Reservation (SLR) is supported on Cisco 4000 Series Integrated Services Router s. SLR allows reservation and utilization of Cisco Smart Licenses without communicating the license information to CSSM. To
                                 reserve specific licenses for a device, generate request code from the device. Enter the request code in CSSM along with the
                                 required licenses and their quantity, and generate authorization code. Enter the authorization code on the device to map the
                                 license to the Unique Device Identifier (UDI).

If upgrading to Cisco IOS XE Amsterdam 17.3.1a with a license reservation in place, update the reservation to include version 14, rather than version 12 CME licenses. The
                                             reservation may be updated before or after the software upgrade.

#### Cisco IOS XE Amsterdam 17.3.2 Release Onwards

This release introduces a new paradigm for tracking license usage across your business. In earlier releases, license authorization
                                 was forward-looking, binding licenses to a device until the next authorization request. Actual license usage during the proceeding
                                 reporting period is now sent to CSSM, allowing you to plan ongoing license requirements based on historical usage data.

Initial device registration is no longer required to use most platform functionality and the evaluation period is deprecated.

License usage reports are submitted periodically according to a minimum reporting policy set for your account. Typically,
                                 this period could be once per year. However, you can generate reports more frequently if the use of licensed features varies
                                 over time. CSSM acknowledges each Resource Utilization Monitoring (RUM) report to ensure that the usage is recorded reliably.
                                 If the router does not receive an acknowledgment within the minimum reporting period, call processing is disabled. Call processing
                                 is resumed when a valid acknowledgment is received.

Reports can be submitted to CSSM directly or through a satellite. Cisco Smart Licensing Utility (CSLU) applications can also
                                 receive usage reports, providing you with more flexibility in managing your license usage. Also, when a device is not able
                                 to communicate directly with a licensing server, a signed usage report can be generated and manually uploaded to CSSM. You
                                 must upload the CSSM generated acknowledgment to the device within the license reporting policy period to ensure continued
                                 use.

As license reporting is now based on historical usage, the registration process that is used previously has been replaced
                                 with a trust association that also defines the reporting policy set in your account. Establishing trust with CSSM or Cisco
                                 Smart Software Manager Satellite uses an identity token similar to earlier registrations. Use the license smart trust idtoken token command to establish the trust relationship within the initial reporting period set for the device. The CLI license smart register command is deprecated from this release.

Warning

When using any of the following releases, Unified CME shuts down if the router does not receive a report acknowledgment from
                                             CSSM before the acknowledgment deadline set by the account policy: 17.3.2, 17.3.3, 17.3.4a, 17.6.1a, or any 17.4 or 17.5 release.
                                             Unified CME does not shut down in this way with later releases.

Smart License Reservation (SLR) for Unified CME licenses is not compatible with Cisco IOS XE Amsterdam 17.3.2 and later releases. Even if a reservation is in place when upgrading to one of these releases, license use reporting is still
                                                   required in accordance with the device policy.

The enhancements that are made for Cisco IOS XE Amsterdam 17.3.2 and Cisco IOS XE Bengaluru 17.4.1a are not available for Cisco CSR 1000V.

Current license usage for Cisco Unified Communications Manager Express is displayed using the show license summary command:

```
Router(config)#do sh license summary
License Usage:
License                 Entitlement tag               Count Status
appxk9                  (ISR_4400_Application)            1 IN USE
uck9                    (ISR_4400_UnifiedCommun...)       1 IN USE
securityk9              (ISR_4400_Security)               1 IN USE
CME_EP                  (CME_EP)                          2 IN USE
```

Cisco Unified Border Element (CUBE) session licenses are required along with CME license specifically for SIP trunking flows.

The following are the SIP trunk call flow examples that trigger CUBE session license reporting:

SIP/SCCP Unified CME registered IP phones making calls through a SIP dial-peer towards another Unified CME.

SIP/SCCP Unified CME registered IP phones making calls through a SIP dial-peer towards a CUCM.

SIP/SCCP Unified CME registered IP phones making calls through a SIP dial-peer towards a third-party IP PBX.

SIP/SCCP Unified CME registered IP phones making calls through a SIP dial-peer towards a SIP ITSP.

For purchasing CUBE license subscriptions, see Cisco Ordering Guide .

Use the show voice sip license stats command to verify the CUBE license usage status and license usage history:

The following example outputs are truncated to display 60-second and 60-minute tables only. Usage is recorded based on the
                                    peak value of concurrent calls for a defined interval of time.

```
Router# show voice sip license stats table 02:50:16 PM Wednesday Nov 13 2019 UTC

CUBE Trunk License Usage  (last 60 seconds)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50          0          0
51-55          0          0
56-60          0          0

CUBE Trunk License Usage  (last 60 minutes)
Period     Average       Max
----------------------------
 1-5           0          0
 6-10          0          0
11-15          0          0
16-20          0          0
21-25          0          0
26-30          0          0
31-35          0          0
36-40          0          0
41-45          0          0
46-50        324        900
51-55        343        899
56-60        292        600
```

For more license usage examples, refer to CUBE Smart Licensing .

## PBX or Keyswitch

When setting up a Cisco Unified CME system, you need to decide if call
                           		handling should be similar to that of a PBX, similar to that of a keyswitch, or
                           		a hybrid of both. Cisco Unified CME provides significant flexibility in this
                           		area, but you must have a clear understanding of the model that you choose.

### PBX Model

The simplest model
                              		is the PBX model, in which most of the IP phones in your system have a single
                              		unique extension number. Incoming PSTN calls are routed to a receptionist at an
                              		attendant console or to an automated attendant. Phone users may be in separate
                              		offices or be geographically separated and therefore often use the telephone to
                              		contact each other.

For this model, we
                              		recommend that you configure directory numbers as dual-lines so that each
                              		button that appears on an IP phone can handle two concurrent calls. The phone
                              		user toggles between calls using the blue navigation button on the phone.
                              		Dual-line directory numbers enable your configuration to support call waiting,
                              		call transfer with consultation, and three-party conferencing (G.711 only).

Incoming Call
                                 		  Using PBX Model shows a PSTN call that is received at the Cisco Unified CME router, which sends
                              		it to the designated receptionist or automated attendant (1), which then routes
                              		it to the requested extension (2).

For configuration
                              		information, see Configure Phones for a PBX System .

### Keyswitch
                           	 Model

In a keyswitch
                              		system, you can set up most of your phones to have a nearly identical
                              		configuration, in which each phone is able to answer any incoming PSTN call on
                              		any line. Phone users are generally close to each other and seldom need to use
                              		the telephone to contact each other.

For example, a 3x3
                              		keyswitch system has three PSTN lines shared across three telephones, such that
                              		all three PSTN lines appear on each of the three telephones. This permits an
                              		incoming call on any PSTN line to be directly answered by any telephone—without
                              		the aid of a receptionist, an auto-attendant service, or the use of (expensive)
                              		DID lines. Also, the lines act as shared lines—a call can be put on hold on one
                              		phone and resumed on another phone without invoking call transfer.

In the keyswitch
                              		model, the same directory numbers are assigned to all IP phones. When an
                              		incoming call arrives, it rings all available IP phones. When multiple calls
                              		are present within the system at the same time, each individual call (ringing
                              		or waiting on hold) is visible and can be directly selected by pressing the
                              		corresponding line button on an IP phone. In this model, calls can be moved
                              		between phones simply by putting the call on hold at one phone and selecting
                              		the call using the line button on another phone. In a keyswitch model, the
                              		dual-line option is rarely appropriate because the PSTN lines to which the
                              		directory numbers correspond do not themselves support dual-line configuration.
                              		Using the dual-line option also makes configuration of call-coverage (hunting)
                              		behaviors more complex.

You configure the
                              		keyswitch model by creating a set of directory numbers that correspond
                              		one-to-one with your PSTN lines. Then you configure your PSTN ports to route
                              		incoming calls to those ephone-dns. The maximum number of PSTN lines that you
                              		can assign in this model can be limited by the number of available buttons on
                              		your IP phones. If so, the overlay option may be useful for extending the
                              		number of lines that can be accessed by a phone.

Incoming PSTN
                                 		  Call Using Keyswitch Model shows an incoming call from the PSTN (1), which is routed to extension 1001 on
                              		all three phones (2).

For configuration
                              		information, see Configure Phones for a Key System .

### Hybrid
                           	 Model

PBX and keyswitch
                              		configurations can be mixed on the same IP phone and can include both unique
                              		per-phone extensions for PBX-style calling and shared lines for keyswitch-style
                              		call operations. Single-line and dual-line directory numbers can be combined on
                              		the same phone.

In the simplest
                              		keyswitch deployments, individual telephones do not have private extension
                              		numbers. Where key system telephones do have individual lines, the lines are
                              		sometimes referred to as intercoms rather than as extensions. The term
                              		“Intercom” is derived from “internal communication;” there is no assumption of
                              		the common “intercom press-to-talk” behavior of auto dial or auto answer in
                              		this context, although those options may exist.

For key systems that
                              		have individual intercom (extension) lines, PSTN calls can usually be
                              		transferred from one key system phone to another using the intercom (extension)
                              		line. When Call Transfer is invoked in the context of a connected PSTN line,
                              		the outbound consultation call is usually placed from the transferrer phone to
                              		the transfer-to phone using one of the phone’s intercom (extension) line
                              		buttons. When the transferred call is connected to the transfer-to phone and
                              		the transfer is committed (the transferrer hangs up), the intercom lines on
                              		both phones are normally released and the transfer-to call continues in the
                              		context of the original PSTN line button (all PSTN lines are directly available
                              		on all phones). The transferred call can be put on hold (on the PSTN line
                              		button) and then subsequently resumed from another phone that shares that PSTN
                              		line.

For example, you can
                              		design a 3x3 keyswitch system as shown in Incoming PSTN
                                 		  Call Using Keyswitch Model and then add another, unique extension on each phone ( Incoming PSTN
                                 		  Call Using Hybrid PBX-Keyswitch Model ).
                              		This setup will allow each phone to have a “private” line to use to call the
                              		other phones or to make outgoing calls.

## Call Detail
                        	 Records

The accounting
                           		process collects accounting data for each call leg created on the Cisco voice
                           		gateway. You can use this information for post-processing activities such as
                           		generating billing records and network analysis. Voice gateways capture
                           		accounting data in the form of call detail records (CDRs) containing attributes
                           		defined by Cisco. The gateway can send CDRs to a RADIUS server, syslog server,
                           		or to a file in .csv format for storing to flash or an FTP server. For
                           		information about generating CDRs, see CDR Accounting for Cisco IOS Voice Gateways .

## Additional
                        	 References

The following
                           		section provides references related to Cisco Unified CME.

Related
                                          					 Topic

Document
                                          					 Title

Cisco
                                          					 Unified CME configuration

Cisco Unified CME Command Reference

Cisco Unified CME Documentation Roadmap

Cisco IOS
                                          					 commands

Cisco IOS Voice Command Reference

Cisco IOS Software Releases 12.4T Command
                                             						References

Cisco IOS
                                          					 configuration

Cisco IOS Voice Configuration Library

Cisco IOS Software Releases 12.4T Configuration
                                             						Guides

Cisco IOS
                                          					 voice troubleshooting

Cisco IOS Voice Troubleshooting and Monitoring
                                             						Guide

Dial
                                          					 peers, DID, and other dialing issues

Dial Peer Configuration on Voice Gateway
                                             						Routers

Understanding One Stage and Two Stage Dialing
                                             						(technical note)

Understanding How Inbound and Outbound Dial
                                             						Peers Are Matched on Cisco IOS Platforms (technical note)

Using IOS Translation Rules - Creating Scalable
                                             						Dial Plans for VoIP Networks (sample configuration)

Dynamic
                                          					 Host Configuration Protocol (DHCP)

“DHCP”
                                          					 section of the Cisco IOS IP Addressing Services Configuration
                                             						Guide

Fax and
                                          					 modem configurations

Cisco Fax Services over IP Application
                                             						Guide

FXS ports

“Configuring Analog Voice Ports” section of the Cisco IOS Voice Port Configuration Guide

SCCP Controlled Analog (FXS) Ports with
                                             						Supplementary Features in Cisco IOS Gateways

Cisco VG 224 Analog Phone Gateway data
                                             						sheet

H.323

Cisco IOS H.323 Configuration Guide

Network
                                          					 Time Protocol (NTP)

“Performing Basic System Management” chapter of Cisco IOS Network Management Configuration
                                             						Guide

Phone
                                          					 documentation for Cisco Unified CME

User Documentation for Cisco Unified IP
                                             						Phones

Public key
                                          					 infrastructure (PKI)

“Part 5: Implementing
                                          					 and Managing a PKI” in the Cisco IOS Security Configuration Guide

SIP

Cisco IOS SIP Configuration Guide

TAPI and
                                          					 TSP documentation

Cisco Unified CME programming Guides

Tcl IVR
                                          					 and VoiceXML

Cisco IOS Tcl IVR and VoiceXML Application Guide
                                             						- 12.3(14)T and later

Cisco Voice XML Programmer’s Guide

VLAN
                                          					 class-of-service (COS) marking

Enterprise QoS Solution Reference Network Design
                                             						Guide

Voice-mail
                                          					 integration

Cisco Unified CallManager Express 3.0
                                             						Integration Guide for Cisco Unity 4.0

Integrating Cisco CallManager Express with
                                             						Cisco Unity Express

Call
                                          					 detail records (CDRs)

CDR Accounting for Cisco IOS Voice
                                             						Gateways

XML

XML Provisioning Guide for Cisco CME/SRST

Cisco IP Phone Services Application Development
                                             						Notes

### Management
                           	 Information Base

MIBs

MIBs Link

CISCO-CCME-MIB

MIB
                                          					 CISCO-VOICE-DIAL-CONTROL-MIB

To locate
                                          					 and download MIBs for selected platforms, Cisco IOS releases, and feature sets,
                                          					 use Cisco MIB Locator found at the following URL: http://www.cisco.com/go/mibs

| Note | CME GUI allows configuration of essential SIP phone features. |
|---|---|

| Note | The Cisco Unified
                                       		  Communications Manager Express System Administrator Guide refers to a phone
                                       		  with SIP firmware as SIP Phone, SIP IP Phone, or Cisco Unified SIP IP phone. A
                                       		  phone with SCCP firmware is referred as SCCP Phone, SCCP IP Phone, or Cisco
                                       		  Unified SCCP IP phone. |
|---|---|

| Note | It is mandatory to configure the command supplementary-service media-renegotiate under voice service voip configuration mode to enable the supplementary features supported on Unified CME. |
|---|---|

| Note | It is mandatory to configure the CLI command call-park system application under telephony-service configuration mode to support SIP and mixed mode (SIP and SCCP) features such as Call Park and Call Pick-up in Unified CME. |
|---|---|

| Note | Configure the CLI commands no supplementary-service sip refer , no supplementary-service sip moved-temporarily under voice service voip configuration mode for call transfer and call forward scenarios in Unified CME. |
|---|---|

| Note | The CME_EP license count includes all phones configured in the Unified CME, covering both ephones and voice register pools,
                                          regardless of their registration status. This count is updated once a phone type is configured under ephone or voice register
                                          pool configuration. To avoid unnecessary reporting while you configure Unified CME, license usage is reported three minutes
                                          after the last configuration change. |
|---|---|

| Note | Unified CME Smart Licenses also provide RTU entitlement for routers that are not configured for Smart Licensing. |
|---|---|

| Warning | Cisco Unified Communications Manager Express shuts down when the router is unregistered and allowed to pass into the Evaluation
                                             Expired state. |
|---|---|

| Note | If upgrading to Cisco IOS XE Amsterdam 17.3.1a with a license reservation in place, update the reservation to include version 14, rather than version 12 CME licenses. The
                                             reservation may be updated before or after the software upgrade. |
|---|---|

| Warning | When using any of the following releases, Unified CME shuts down if the router does not receive a report acknowledgment from
                                             CSSM before the acknowledgment deadline set by the account policy: 17.3.2, 17.3.3, 17.3.4a, 17.6.1a, or any 17.4 or 17.5 release.
                                             Unified CME does not shut down in this way with later releases. |
|---|---|

| Note | Smart License Reservation (SLR) for Unified CME licenses is not compatible with Cisco IOS XE Amsterdam 17.3.2 and later releases. Even if a reservation is in place when upgrading to one of these releases, license use reporting is still
                                                   required in accordance with the device policy. The enhancements that are made for Cisco IOS XE Amsterdam 17.3.2 and Cisco IOS XE Bengaluru 17.4.1a are not available for Cisco CSR 1000V. |
|---|---|

| Note | For purchasing CUBE license subscriptions, see Cisco Ordering Guide . |
|---|---|

| Related
                                          					 Topic | Document
                                          					 Title |
|---|---|
| Cisco
                                          					 Unified CME configuration | Cisco Unified CME Command Reference Cisco Unified CME Documentation Roadmap |
| Cisco IOS
                                          					 commands | Cisco IOS Voice Command Reference Cisco IOS Software Releases 12.4T Command
                                             						References |
| Cisco IOS
                                          					 configuration | Cisco IOS Voice Configuration Library Cisco IOS Software Releases 12.4T Configuration
                                             						Guides |
| Cisco IOS
                                          					 voice troubleshooting | Cisco IOS Voice Troubleshooting and Monitoring
                                             						Guide |
| Dial
                                          					 peers, DID, and other dialing issues | Dial Peer Configuration on Voice Gateway
                                             						Routers Understanding One Stage and Two Stage Dialing
                                             						(technical note) Understanding How Inbound and Outbound Dial
                                             						Peers Are Matched on Cisco IOS Platforms (technical note) Using IOS Translation Rules - Creating Scalable
                                             						Dial Plans for VoIP Networks (sample configuration) |
| Dynamic
                                          					 Host Configuration Protocol (DHCP) | “DHCP”
                                          					 section of the Cisco IOS IP Addressing Services Configuration
                                             						Guide |
| Fax and
                                          					 modem configurations | Cisco Fax Services over IP Application
                                             						Guide |
| FXS ports | FXS Ports in SCCP Mode on Cisco VG 224 Analog Phone
                                          					 Gateway “Configuring Analog Voice Ports” section of the Cisco IOS Voice Port Configuration Guide FXS Ports in SCCP Mode on Cisco VG 224 Analog Phone
                                          					 Gateway SCCP Controlled Analog (FXS) Ports with
                                             						Supplementary Features in Cisco IOS Gateways Cisco VG 224 Analog Phone Gateway data
                                             						sheet |
| H.323 | Cisco IOS H.323 Configuration Guide |
| Network
                                          					 Time Protocol (NTP) | “Performing Basic System Management” chapter of Cisco IOS Network Management Configuration
                                             						Guide |
| Phone
                                          					 documentation for Cisco Unified CME | User Documentation for Cisco Unified IP
                                             						Phones |
| Public key
                                          					 infrastructure (PKI) | “Part 5: Implementing
                                          					 and Managing a PKI” in the Cisco IOS Security Configuration Guide |
| SIP | Cisco IOS SIP Configuration Guide |
| TAPI and
                                          					 TSP documentation | Cisco Unified CME programming Guides |
| Tcl IVR
                                          					 and VoiceXML | Cisco IOS Tcl IVR and VoiceXML Application Guide
                                             						- 12.3(14)T and later Cisco Voice XML Programmer’s Guide |
| VLAN
                                          					 class-of-service (COS) marking | Enterprise QoS Solution Reference Network Design
                                             						Guide |
| Voice-mail
                                          					 integration | Cisco Unified CallManager Express 3.0
                                             						Integration Guide for Cisco Unity 4.0 Integrating Cisco CallManager Express with
                                             						Cisco Unity Express |
| Call
                                          					 detail records (CDRs) | CDR Accounting for Cisco IOS Voice
                                             						Gateways |
| XML | XML Provisioning Guide for Cisco CME/SRST Cisco IP Phone Services Application Development
                                             						Notes |

| MIBs | MIBs Link |
|---|---|
| CISCO-CCME-MIB MIB
                                          					 CISCO-VOICE-DIAL-CONTROL-MIB | To locate
                                          					 and download MIBs for selected platforms, Cisco IOS releases, and feature sets,
                                          					 use Cisco MIB Locator found at the following URL: http://www.cisco.com/go/mibs |