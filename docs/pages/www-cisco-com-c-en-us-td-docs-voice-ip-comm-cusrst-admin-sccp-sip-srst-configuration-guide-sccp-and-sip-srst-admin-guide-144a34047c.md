---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-144a34047c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_roadmap.html
retrieved_at: 2026-08-21T02:48:47.584651+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Cisco Unified Survivable Remote Site Telephony Feature Roadmap

## Chapter: Cisco Unified Survivable Remote Site Telephony Feature Roadmap

# Cisco Unified Survivable Remote Site Telephony Feature Roadmap

This chapter contains a list of Cisco Unified Survivable Remote Site Telephony (Cisco Unified SRST) features and the location
                        of feature documentation.

Use Cisco Feature Navigator to find information about platform support and Cisco IOS software image support. Access Cisco
                        Feature Navigator at http://www.cisco.com/go/fn . You must have an account on Cisco.com. If you do not have an account or have forgotten your username or password, click Cancel at the login dialog box and follow the instructions that appear.

## Documentation Organization

This document consists of the following chapters or appendixes as shown in the following table.

Chapter or Appendix

Description

Cisco Unified SRST Feature Overview

Gives a brief description of Cisco Unified SRST and provides information on the supported platforms and Cisco Unified IP Phones.
                                       In addition, it describes any prerequisites or restrictions that should be addressed before Cisco Unified SIP SRST is configured.

Setting Up the Network

Describes how to set up a Cisco Unified SRST system to communicate with your network.

Enhanced SRST

Describes how to configure the Cisco Unified Enhanced SRST feature in your network.

Cisco Unified SIP SRST

Describes the features for Cisco Unified SIP SRST Version 4.1 and provides the associated configuration procedures.

Setting Up Cisco Unified IP Phones using SCCP

Describes how to set up the basic Cisco Unified SRST phone configuration.

Setting Up Cisco Unified IP Phones using SIP

Describes features available in Version 3.0 that are also necessary for Version 3.4. Features include instructions on how
                                       to provide a backup to an external SIP call control (IP-PBX) by providing basic registrar services. These services are used
                                       by a SIP IP phone in the event of a WAN connection outage when the SIP phone is unable to communicate with its primary SIP
                                       proxy.

Configuring Call Handling

Describes how to configure incoming and outgoing calls.

Configure Secure SRST for SCCP and SIP

Describes the Secure SRST security functionality to the Cisco Unified SRST.

Integrating Voice Mail with Cisco Unified SRST

Describes how to set up voicemail.

Setting Video Parameters

Describes how to set up video parameters.

Monitoring and Maintaining Cisco Unified SRST

Provides a list of useful show commands for monitoring and maintaining Cisco Unified SRST.

Appendix A: Configuring Cisco Unified SIP SRST Features Using Redirect Mode

Describes features using redirect mode, which applies to version 3.0 only.

Appendix B: Integrating Cisco Unified Communications Manager and Cisco Unified SRST to Use Cisco Unified SRST as a Multicast
                                          MOH Resource

Describes how to configure Cisco Unified CM and Cisco Unified SRST to enable multicast music-on-hold (MOH).

## Feature Roadmap

The following table provides a feature history summary of Unified SRST features.

Cisco Unified SRST

Cisco IOS Release

Enhancements or Modifications

Version 15.0

Cisco IOS XE 26.1.1

Advanced TLS security compliance and control. See Configure Secure SRST for SCCP and SIP .

Support for Cisco Desk Phone 9800 Series, and Cisco Desk Phone 9811 Series. See Unified SRST/E-SRST 15.0 Supported Firmware, Platforms, Memory, and Voice Products .

Version 15.0

Cisco IOS XE 17.18.2

SRST support on C8375-E-G2 router platform with virtual DSP (vDSP) enabled. See Unified SRST/E-SRST 15.0 Supported Firmware, Platforms, Memory, and Voice Products .

Security warnings for usage of legacy TLS and associated weaker ciphers. See Signaling Security on Unified SRST - TLS .

Version 15.0

Cisco IOS XE 17.18.1a

Cisco Smart Licensing reports flex subscription entitlement tag for SRST platforms. To maintain the continued support and
                                             entitlements to the future application versions, purchase a Collaboration Flex subscription. See Smart License Operation .

Support for Cisco Desk Phone 9861 (DP-9861), and Cisco Desk Phone 9871 (DP-9871). See Unified SRST/E-SRST 15.0 Supported Firmware, Platforms, Memory, and Voice Products .

Version 14.5

Cisco IOS XE 17.15.1a

Support for Cisco Desk Phone 9841 (DP-9841), and Cisco Desk Phone 9851 (DP-9851). See Unified SRST/E-SRST 14.5 Supported Firmware, Platforms, Memory, and Voice Products .

Version 14.4

Cisco IOS XE 17.14.1a

TLS version 1.3 support —TLS version 1.3 and associated ciphers support for secure SIP and SCCP SRST:

AES128_GCM_SHA256

AES256_GCM_SHA384

CHACHA20_POLY1305_SHA256

Version 14.3

Cisco IOS XE Dublin
                                             17.11.1a

Cisco IOS XE Cupertino 17.9.3a

Webex Survivability Gateway Mode —Webex Survivability Gateway mode now supports survivability for Webex Calling endpoints and Unified SRST-based survivability
                                       for on-premises endpoints that register to Cisco Unified Communications Manager.

Site Survivability for Webex Calling —Configure a Webex Survivability Gateway to provide a calling fallback service for Webex Calling endpoints.

Version 14.3

YANG model enhancements for Unified SRST:

Programmability Guide for Cisco
                                          IOS XE Unified Communications VoIP Products

https://www.cisco.com/c/en/us/td/docs/routers/sdwan/command/sdwan-cr-book.html

Version 14.3

Cisco IOS XE Cupertino
                                             17.9.1a

Introduced the following commands as part of Cisco Webex Calling Branch Survivability:

mode webex-sgw

voice register webex-sgw sync

show voice register webex-sgw users

Modified the following command as part of Cisco Webex Calling Branch Survivability:

id (voice register pool) modified to include phone-number e164-number and extension-number extension-number

Version 14.3

Cisco IOS XE Cupertino
                                             17.9.1a

CDR Accounting Overview

Configuring File Accounting

gw-accounting

Version 14.2

Cisco IOS XE Cupertino
                                             17.8.1a

SHA2-Cipher-Only Mode for Unified Secure SRST

Version 14.2

SIP OAuth Client Registration for Unified Secure SRST

Version 14.1

Cisco IOS XE Bengaluru 17.6.1a

Programmability Guide for Cisco IOS XE Unified Communications VoIP Products

Version 14.1

Cisco IOS XE Bengaluru 17.5.1a Release

Support for Unified SRST on Cisco 1100 Integrated Services Router

Support for Unified SRST and E-SRST on Cisco 8200L Catalyst Series Edge Platforms

Version 14.1

Cisco IOS XE Bengaluru 17.4.1a Release

Support for Unified SRST and E-SRST on Cisco 8200 Catalyst Series Edge Platforms

Smart Licensing Using Policy— Cisco Smart Licensing for Unified SRST

Smart Licensing Using Policy— Cisco Smart Licensing for Unified E-SRST

Version 14.1

Cisco IOS XE Amsterdam 17.3.2 Release

Support for Unified SRST and E-SRST on Cisco 8300 Catalyst Series Edge Platforms

Smart Licensing Using Policy— Cisco Smart Licensing for Unified SRST

Smart Licensing Using Policy— Cisco Smart Licensing for Unified E-SRST

Version 12.8

Cisco IOS XE Amsterdam 17.2.1r

Cisco Jabber with Unified SRST

VRF Support for Unified SRST

Support for YANG Models in Unified SRST

Version 12.7

Cisco IOS XE Amsterdam

17.1.1

Support for maximum number of devices in Cisco 4451 and 4461 Integrated Services Routers was increased from 1500 to 2000

Version 12.6

Cisco IOS XE Gibraltar 16.11.1a

Simple Network Management Protocol (SNMP) Support for Unified SRST

Toll Fraud Prevention for SIP Line Side on Unified SRST

Unified SRST, Unified E-SRST, and Unified Secure SRST Password Policy

Version 12.5

Cisco IOS XE Gibraltar 16.10.1a

Support for Unified SRST on Cisco 4461 Integrated Services Routers

Version 12.3

Cisco IOS XE Fuji 16.9.1

Secure SCCP SRST on Cisco 4000 Series Integrated Services Router

Version 12.2

Cisco IOS XE Fuji 16.8.1

Unified E-SRST with Support for Voice Hunt Group

Version 12.1

Cisco IOS XE Fuji 16.7.1

Licensing

Secure SCCP SRST on Cisco 4000 Series Integrated Services Router

Unified SRST and Unified Border Element Co-location

Version 12.0

Cisco IOS XE Everest 16.6.1

IPv6 Support for Unified SRST SIP IP Phones

Version 11.0

15.6(1)T

Support for Cisco IP Phone 7811

Support for Cisco IP Phones 8811, 8831, 8841, 8845, 8865, 8851, 8851NR, 8861

Support for Cisco ATA-190 Phones

Version 10.5

15.4(3)M

Version 10.0

15.3(3)M

Cisco Jabber for Windows

SIP: Configure Unified E-SRST

Version 9.5

15.3(2)T

Version 9.1

15.2(4)M

KEM Support for Cisco Unified SIP IP Phones

Enhancement in Speed-Dial Support

Voice Hunt Group Support

Version 9.0

15.2(2)T

Version 8.8

15.2(1)T

Support for Cisco Unified 6945, 8941, and 8945 SCCP IP Phones

Version 8.6

15.1(4)M

Support for Cisco Unified 8941 and 8945 SCCP IP Phones were introduced. For more information, see Configuring Cisco Unified 8941 and 8945 SCCP IP Phones .

Version 8.0

15.1(1)T

Beginning with Cisco IP Phone firmware 8.5(3) and Cisco IOS Release 15.1(1)T, Cisco SRST supports SIP signaling over UDP,
                                       TCP, and TLS connections, providing both RTP and SRTP media connections based on the security settings of the IP phone. For
                                       more information, see the following sections:

Signaling Security on Unified SRST - TLS

Media Security on Unified SRST - SRTP

Configuring Secure SIP Call Signaling and SRTP Media with Cisco SRST

Version 7.0/4.3

See Cisco Feature Navigator for compatibility.

Configuring Eight Calls per Button (Octo-Line)

Configuring Consultative Transfer

Version 4.2(1)

See Cisco Feature Navigator for compatibility.

Enhanced 911 Services .

The following new features are included:

Assigning ERLs to zones to enable routing to the PSAP that is closest to the caller.

Customizing E911 by defining a default ELIN, identifying a designated number if the 911 caller cannot be reached on callback,
                                             specifying the expiry time for data in the Last Caller table, and enabling syslog messages that announce all emergency calls.

Expanding the E911 location information to include name and address.

Adding new permanent call detail records.

Version 4.1

12.4(15)T

Version 4.0

12.4(4)XC

Version 3.4

12.4(4)T

Cisco SIP SRST 3.4

Configuring Cisco Unified SIP SRST Features Using Redirect Mode

Configuring Call Handling (see Back-to-Back User Agent Mode)

Version 3.3

Secure SRST

Cisco Unified IP Phone 7970G and Cisco Unified 7971G-GE Support

Enhancement to the show ephone Command

Version 3.2

12.3(11)T

Version 3.1

12.3(7)T

Cisco Unified IP Phone 7920 Support

Cisco Unified IP Phone 7936 Support

Version 3.0

12.2(15)ZJ 12.3(4)T

Version 2.1

Version 2.02

Cisco Unified IP Phone Conference Station 7935 Support

Increase in Directory Numbers

Cisco Unity Voicemail Integration Using In-Band DTMF Signaling Across the PSTN and BRI/PRI

Cisco Unified SRST was implemented on the Cisco Catalyst 4500 access gateway module and Cisco 7200 routers (NPE-225, NPE-300,
                                             and NPE400).

Support was removed for the Cisco MC3810-V3 concentrator.

Version 2.01

Cisco Unified SRST was implemented on the Cisco 1760 routers, and support for the Cisco 1750 was removed.

Support was added for additional connected Cisco IP phones.

Support was added for additional directory numbers or virtual voice ports on Cisco IP phones.

Version 2.0

Cisco Unified SRST was implemented on the Cisco 2600XM and Cisco 2691 routers.

Cisco Unified SRST was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 3725 and Cisco 3745 routers
                                             and the Cisco MC3810-V3 concentrators.

Cisco Unified SRST was implemented on the Cisco 1750 and Cisco 1751 routers.

Huntstop support.

Class of restriction (COR).

Translation rule support.

MOH and tone on hold.

Distinctive ringing.

Forward to a central voicemail or auto-attendant (AA) through PSTN during Cisco Unified Communications Manager fallback.

Phone number alias support during Cisco Unified Communications Manager fallback: enhanced default destination support.

List-based call restrictions for Cisco Unified Communications Manager fallback.

Version 1.0

Support was added for 144 Cisco IP phones on the Cisco 3660 multiservice routers.

Cisco Unified SRST introduced on the Cisco 2600 series and Cisco 3600 series multiservice routers and the Cisco IAD2420 series
                                             integrated access devices.

Cisco IP phones able to establish a connection with an SRST router in the event of a WAN link to Cisco Unified Communications
                                             Manager failure.

Dimming of all Cisco Unified IP Phone function keys that are not supported during Cisco Unified SRST operation.

Extension-to-extension dialing.

Direct Inward Dialing (DID).

Direct Outward Dialing (DOD).

Calling party ID (Caller ID/ANI) display.

Last number redial.

Preservation of local extension-to-extension calls when WAN link fails.

Preservation of local extension to PSTN calls when WAN link fails.

Preservation of calls in progress when failed WAN link is re-established.

Blind transfer of calls within IP network.

Multiple lines per Cisco IP phone.

Multiple-line appearance across telephones.

Call hold (shared lines).

Analog Foreign Exchange Station (FXS) and Foreign Exchange Office (FXO) ports.

BRI support for EuroISDN.

PRI support for NET5 switch type.

## Information About New Features in Cisco Unified SRST

### New Features for Cisco Unified SRST Version 15.0

Cisco Unified SRST 15.0 release ( Cisco IOS XE 26.1.1 )

Advanced TLS security compliance and control.

See Configure Secure SRST for SCCP and SIP .

This release introduces support for the following phone devices:

Cisco Desk Phone 9800 Series

Cisco Desk Phone 9811 Series

See Unified SRST/E-SRST 15.0 Supported Firmware, Platforms, Memory, and Voice Products .

Cisco Unified SRST 15.0 release ( Cisco IOS XE 17.18.2 )

Security warnings for usage of legacy TLS and associated weaker ciphers.

See Unified SRST/E-SRST 15.0 Supported Firmware, Platforms, Memory, and Voice Products

SRST support on C8375-E-G2 router platform with virtual DSP (vDSP) enabled.

See Unified SRST/E-SRST 15.0 Supported Firmware, Platforms, Memory, and Voice Products .

Cisco Unified SRST 15.0 release ( Cisco IOS XE 17.18.1a )

Cisco Smart Licensing reports flex subscription entitlement tag for SRST platforms. To maintain the continued support and
                                          entitlements to the future application versions, purchase a Collaboration Flex subscription. See Smart License Operation .

This release introduces support for the following phone devices:

Cisco Desk Phone 9861 (DP-9861)

Cisco Desk Phone 9871 (DP-9871)

See Unified SRST/E-SRST 15.0 Supported Firmware, Platforms, Memory, and Voice Products .

The smart licensing functionality remains unchanged. For ongoing requirements and continued support, purchase Collaboration
                                                      Flex subscription.

### New Features for Cisco Unified SRST Version 14.5

Cisco Unified SRST 14.5 release introduces support for the following phone devices:

Cisco Desk Phone 9841 (DP-9841)

Cisco Desk Phone 9851 (DP-9851)

See Unified SRST/E-SRST 14.5 Supported Firmware, Platforms, Memory, and Voice Products .

### New Features for Cisco Unified SRST Version 14.4

Cisco Unified SRST 14.4 Release introduces support for the following new features:

Secure SIP SRST and Secure SCCP SRST supports TLS version 1.3 ciphers.

SHA2 ciphers support with TLS version 1.3 for secure SCCP SRST.

Only SCCP Analog Voice Gateways support TLS version 1.3. The SCCP IP phone endpoints do not support TLS version 1.3.

For configuration information, see Configure Secure SRST for SCCP and SIP .

### New Features for Cisco Unified SRST Version 14.3

Cisco Unified SRST 14.3 Release introduces support for the following new features:

Webex Survivability Gateway—From Cisco IOS XE 17.9.3 and Cisco IOS XE Dublin
                                          17.11.1a onward, configure a Webex Survivability Gateway to provide an on-site calling fallback service for Webex Calling endpoints.
                                    This feature also supports the colocation of a Webex Calling survivability configuration and a Unified SRST configuration
                                    on the same router.

For general information, see Webex Survivability Gateway Mode .

To configure a Survivability Gateway, see Site Survivability for Webex Calling .

SFTP CDR Transfer for File Accounting — Allows transfer of SRST CDRs using SFTP. See Configuring File Accounting .

### New Features for Cisco Unified SRST Version 14.2

Cisco Unified SRST 14.2 Release introduces support for the following new features:

Restrict Secure SIP SRST and Secure SCCP SRST to only using TLS 1.2 SHA2 Cipher Suites— SHA2-Cipher-Only Mode for Unified Secure SRST

SIP OAuth Support for Secure SRST— SIP OAuth Client Registration for Unified Secure SRST

### New Features for Unified SRST Version 14.1

Unified SRST 14.1 Release introduces support for the following new features:

Voice: Class of Restriction YANG Configuration Model— Programmability Guide for Cisco IOS XE Unified Communications VoIP Products

Smart Licensing Using Policy— Cisco Smart Licensing for Unified SRST

Smart Licensing Using Policy— Cisco Smart Licensing for Unified E-SRST

### New Features for Unified SRST Version 12.7

Unified SRST 12.7 Release introduces support for the following new feature:

Support for maximum number of devices in Cisco 4451 and 4461 Integrated Services Routers was increased from 1500 to 2000.

### New Features for Cisco Unified SRST Version 12.6

Cisco Unified SRST 12.6 Release introduces support for the following new features:

Simple Network Management Protocol (SNMP) Support for Cisco Unified SRST

Toll Fraud Prevention for SIP Line Side on Cisco Unified SRST

Cisco Unified SRST, Unified E-SRST, and Unified Secure SRST Password Policy

### New Features for Cisco Unified SRST Version 12.3

Cisco Unified SRST 12.3 Release introduces support for Secure SCCP SRST on Cisco 4000 Series Integrated Services Router .

### New Features for Cisco Unified SRST Version 12.2

Cisco Unified SRST 12.2 Release introduces support for Unified E-SRST with Support for Voice Hunt Group .

### New Features for Cisco Unified SRST Version 12.1

Cisco Unified SRST 12.1 introduces support for the following new features:

Licensing

Secure SIP SRST Support on Cisco 4000 Series Integrated Services Router

Cisco Unified SRST and Cisco Unified Border Element co-location

### New Feature for Cisco Unified SRST Version 12.0

Cisco Unified SRST 12.0 introduces support for IPv6 protocols on SIP IP Phones. For more information on IPv6 Support introduced
                              for Cisco Unified SRST, see IPv6 Support for Cisco Unified SRST SIP IP Phones .

### New Features for Cisco Unified SRST Version 11.0

Cisco Unified SRST 11.0 supports the following new Cisco IP phones and adapters:

Support for Cisco IP Phone 7811

Support for Cisco IP Phones 8811, 8831, 841, 8851, 8851NR, 8861

Support for Cisco ATA-190

For information on the phones supported in Cisco Unified SRST 11.0, see Phone Feature Support Guide for Cisco Unified Communications Manager Express, Cisco Unified SRST, Unified E-SRST, and Unified
                                 Secure SRST .

### New Features for Cisco Unified SRST Version 10.5

Cisco Unified SRST 10.5 supports the following features:

Where to Go Next, Setting Up the Network

For more information on the Cisco Unified SRST 10.5 supported feature, see the SCCP: Configure Unified E-SRST .

Cisco Unified SRST 10.5 supports the following new Cisco Unified SIP IP phones:

Support for Cisco Unified DX650 SIP IP Phones

Support for Cisco Unified 78xx SIP IP Phones

#### Support for Cisco Unified DX650 SIP IP Phones

For information on feature support for the Cisco Unified DX650 SIP IP Phones in Cisco Unified SRST 10.5, see Phone Feature Support Guide for Unified CME, Unified SRST, Unified E-SRST, and Unified Secure SRST .

#### Support for Cisco Unified 78xx SIP IP Phones

For information on feature support for the Cisco Unified 78xx SIP IP Phones in Cisco Unified SRST 10.5, see Phone Feature Support Guide for Unified CME, Unified SRST, Unified E-SRST, and Unified Secure SRST .

### New Features in Cisco Unified SRST Version 10.0

Cisco Unified SRST 10.0 supports the following new features:

Cisco Jabber for Windows

SIP: Configure Unified E-SRST

To obtain an account on Cisco.com, go to www.cisco.com and click Register at the top of the screen.

#### Cisco Jabber for Windows

Cisco Jabber for Windows client is supported from Cisco Unified CME Release 10 onwards.Cisco Jabber for Windows supports the
                                 visual voicemail functionality integrated with the Cisco Unity connection. Cisco Jabber for Windows is a SIP-based soft client
                                 with integrated Instant Messaging and presence functionality, and uses the new Client Services Framework 2nd Generation (CSF2G)
                                 architecture.

CSF is a unified communications engine that is reused by multiple Cisco PC-based clients. The Cisco Jabber client has to be
                                 registered with a presence server such as cloud-based Cisco Webex server, or Cisco Unified Presence server to avail the standard
                                 XMPP-based instant messaging functionalities. The client is identified by a device ID name that can be configured under the
                                 voice register pool in Cisco Unified CME. You should configure the username and password under voice register pool to identify
                                 the user logging into Cisco Unified CME through Cisco Jabber for Windows client. The device discovery process uses HTTPS connection.
                                 Therefore, you should configure the secure HTTP on Cisco Unified CME. A new phone type, Jabber-Win has been added to configure
                                 the voice register pool for Cisco Jabber for Windows client.

##### Restrictions

The Cisco Jabber for Windows client version should be version 9.1.0 and later version.

The Cisco Jabber for Windows client should register with a presence server such as cloud-based Webex server, or a Cisco Unified
                                          Presence server to enable the telephony features on the Jabber client.

The Cisco Jabber for Windows client supports only the visual voicemail functionality using Internet Message Access Protocol
                                          (IMAP) on the Cisco Unity Connection.

The Cisco Jabber for Windows client does not support software-based conferencing and supports only the softphone mode with
                                          Cisco Unified CME.

Desk phone models are not supported.

For configuration information, see the “Cisco Jabber for Windows” section of Cisco Unified Communications Manager Administration Guide .

#### Version Negotiation for Cisco Unified SIP IP Phones

The version negotiation for Cisco Unified SIP IP Phones was introduced in Cisco Unified SRST 10.0 release. For more information
                                 on the Cisco Unified SRST 10.0 supported features, see the SIP: Configure Unified E-SRST section.

### New Features in Cisco Unified SRST Version 9.5

### After-hour Pattern Blocking Support for Regular Expressions

In Cisco Unified SRST 9.5, support for afterhours pattern blocking is extended to regular expression patterns for dial plans
                              on Cisco Unified SIP and Cisco Unified SCCP IP phones. With this support, users can add a combination of fixed dial plans
                              and regular expression-based dial plans.

When a call is initiated after hours, the dialed number is matched against a combination of dial plans. If a match is found,
                              the call is blocked.

To enable regular expression patterns to be included when configuring afterhours pattern blocking, the after-hours block pattern command is modified to include regular expressions as a value for the pattern argument in the following command syntax:

after-hours block pattern pattern-tag  pattern

This command is available in the following configuration modes:

telephony-service—For both SCCP and SIP Phones.

ephone-template—For SCCP phones only.

The maximum length of a regular expression pattern is 32 for both Cisco Unified SIP and Cisco Unified SCCP IP phones.

If calls to the following numbers are to be blocked after hours:

numbers beginning with ‘0’ and ‘00’

numbers beginning with 1800, followed by four digits

numbers 9876512340 to 9876512345

then the following configurations can be used:

after-hours block pattern 1 0*

after-hours block pattern 2 00*

after-hours block pattern 3 1800….

after-hours block pattern 4 987651234[0-5]

There is no change in the number of afterhours patterns that can be added. The maximum number is still 100.

For more information on configuration examples, see the “Configuring Afterhours Block Patterns of Regular Expressions: Example”
                              section of Cisco Unified Communications Manager Administration Guide .

For a summary of the basic Cisco IOS regular expression characters and their functions, see the Cisco Regular Expression Pattern Matching Characters section of Terminal Services Configuration Guide .

### Call Park Recall Enhancement

Before Cisco Unified CME 9.5, a parked call could not be recalled by or transferred to the phone that put the call in park
                              or the original phone that transferred the call when the destination phone was offhook or ringing.

In Cisco Unified CME 9.5, the recall force keyword is added to the call-park system command in telephony-service configuration mode to allow a user to force the recall or transfer of a parked call to the
                              phone that put the call in park or the phone with the reserved-for number as its primary DN when the destination phone is
                              available to answer the call.

In Cisco Unified CME 10.5, a new ring tone is introduced for park recall to assist the phone user to distinctly identify the
                              type of call.

This feature is supported on all phone families for SCCP endpoints and on 89XX and 99XX phone families for SIP endpoints.
                              No configurations are required to activate this feature.

The following example configures the Call Park Recall:

```
Router# configure terminal
Router(config)# telephony-service
Router(config)# srst mode auto-provision all
Router(config-telephony)# call-park system ? recall Configure parameters for recall
Router(config-telephony)# call-park system recall ? force Force recall for busy call park
initiator
Router(config-telephony)# call-park system recall force
```

### Park Monitor

In Cisco Unified CME 8.5 and later versions, the park monitor feature allows you to park a call and monitor the status of
                              the parked call until the parked call is retrieved or abandoned. When a Cisco Unified SIP IP Phone 8961, 9951, or 9971 parks
                              a call using the park soft key, the park monitoring feature monitors the status of the parked call. The park monitoring call
                              bubble is not cleared until the parked call gets retrieved or is abandoned by the parkee. This parked call can be retrieved
                              using the same call bubble on the parker’s phone to monitor the status of the parked call.

Once a call is parked, Cisco Unified CME sends a SIP NOTIFY message to the parker phone indicating the “parked” event along
                              with the park slot number so that the parker phone can display the park slot number as long as the call remains parked.

When a parked call is retrieved, Cisco Unified CME sends another SIP NOTIFY message to the parker phone indicating the “retrieved”
                              event so that the phone can clear the call bubble. When a parked call is disconnected by the parkee, Cisco Unified CME sends
                              a SIP NOTIFY message to the parker phone indicating the “abandoned” event and the parker phone clears the call bubble upon
                              cancellation of the parked call.

When a parked call is recalled or transferred, Cisco Unified CME sends a SIP NOTIFY message to the parker phone indicating
                              the “forwarded” event so that parker phone can clear the call bubble during park, recall, and transfer. You can also retrieve
                              a parked call from the parker phone by directly selecting the call bubble or pressing the resume soft key on the phone.

#### Display Support for Name of Called Voice Hunt Groups

A voice hunt group is associated with a pilot number. But because there is no association with the name of the voice hunt
                                 group when calls are forwarded from the voice hunt group to the final number, the forwarding number is sent without the name
                                 of the forwarding party. The final number can be in the form of a voicemail, a Basic Automatic Call Distribution (BACD) script,
                                 or another extension.

In Cisco Unified SRST 9.5, the display of the name of the called voice-hunt-group pilot is supported by configuring the following
                                 command in voice hunt-group or ephone-hunt configuration mode:

[ no ] name "primary pilot name" [ secondary "secondary pilot name" ]

The secondary name is optional and when the secondary pilot name is not explicitly configured, the primary pilot name is applicable
                                 to both pilot numbers.

For configuration information, see the “Associating a Name with a Called Voice Hunt Group” section of Cisco Unified Communications Manager Administration Guide .

For configuration examples, see the “Example: Associating a Name with a Called Voice Hunt Group” section of Cisco Unified Communications Manager Administration Guide .

Restrictions

Display support applies to Cisco Unified SCCP IP phones in voice hunt-group and ephone-hunt configuration modes but are not
                                       supported in Cisco Unified SIP IP phones.

Called name and called number information displayed on the caller’s phone follows existing behavior, where the called names
                                       and called numbers are updated so that a sequential hunt reflects the name and number of the ringing phone.

The following example configures the primary pilot name for both the primary and secondary pilot numbers:

```
name SALES
```

The following example configures different names for the primary and secondary pilot numbers:

```
name SALES secondary SALES-SECONDARY
```

Use quotes (") when input strings have spaces in between as shown in the next three examples.

The following example associates a two-word name for the primary pilot number and a one-word name for the secondary pilot
                                    number:

```
name “CUSTOMER SERVICE” secondary CS
```

The following example associates a one-word name for the primary pilot number and a two-word name for the secondary pilot
                                    number:

```
name FINANCE secondary “INTERNAL ACCOUNTING”
```

The following example associates two-word names for the primary and secondary pilot numbers:

```
name “INTERNAL LLER” secondary “EXTERNAL LLER”
```

#### Preventing Local-Call Forwarding to Final Agent in Voice Hunt Groups

Local or internal calls are calls originating from a Cisco Unified SIP or Cisco Unified SCCP IP phone in the same Cisco Unified
                                 CME system.

Before Cisco Unified CME 9.5, the no forward local-calls command was configured in ephone-hunt group to prevent a local call from being forwarded to the next agent.

In Cisco Unified CME 9.5, local calls are prevented from being forwarded to the final destination using the no forward local-calls to-final command in parallel or sequential voice hunt-group configuration mode.

When the no forward local-calls to-final command is configured in sequential voice hunt-group configuration mode, local calls to the hunt-group pilot number are
                                 sent sequentially only to the list of members of the group using the rotary-hunt technique. In case all the group members
                                 of the voice hunt group are busy, the caller hears a busy tone. If any of the group members are available but do not answer,
                                 the caller hears a ringback tone and is eventually disconnected after the specified timeout. The call is not forwarded to
                                 the final number.

When the no forward local-calls to-final command is configured in parallel voice hunt-group configuration mode, local calls to the hunt-group pilot number are sent
                                 simultaneously to the list of members of the group using the blast technique. In case all the group members of the voice hunt
                                 group are busy, the caller hears a busy tone. If any of the group members are available but do not answer, the caller hears
                                 a ringback tone and is eventually disconnected after the specified timeout.The call is not forwarded to the final number.
                                 or configuration examples, see the “Preventing Local-Call Forwarding to Final Agent in Voice Hunt Groups” section of” section
                                 of Cisco Unified Communications Manager Administration Guide .

#### Trunk-to-Trunk Transfer Blocking for Toll Fraud Prevention on Cisco Unified SIP IP Phones

In Cisco Unified Survivable Remote Site Telephony (SRST) 4.0, trunk-to-trunk transfer blocking for toll bypass fraud prevention
                                 is supported on Cisco Unified Skinny Client Control Protocol (SCCP) IP phones.

The following table lists the transfer-blocking commands and the appropriate configuration modes for Cisco Unified CME and
                                 Cisco Unified SRST.

Commands

Cisco Unified SRST

transfer-pattern

call-manager-fallback

transfer max-length

voice register pool

transfer-pattern blocked

voice register pool

conference transfer-pattern

call-manager-fallback

voice register pool or voice register template

voice register pool or voice register template

The call transfer and conference restrictions apply when transfers or conferences are initiated toward external parties, like
                                             a PSTN trunk, a SIP trunk, or an H.323 trunk. The restrictions do not apply to transfers and conferences to local extensions.

### Transfer-Pattern

The transfer-pattern command for Cisco Unified SIP IP phones functions like the transfer-pattern command for Cisco Unified SCCP IP phones by allowing all, not just local, transfers to take place.

The transfer-pattern command specifies the directory numbers for Call Transfer. The command can be configured up to 32 times using the following
                              command syntax: transfer-pattern transfer-pattern [ blind ].

The blind keyword in the transfer-pattern command applies only to Cisco Unified SCCP IP phones and does not apply to Cisco Unified SIP IP phones.

With the transfer-pattern command configured, only Call Transfers to numbers that match the configured transfer pattern are allowed to take place.
                              With the transfer pattern configured, all or a subset of transfer numbers can be dialed and the transfer to a remote party
                              can be initiated.

The following are examples of configurable transfer patterns:

.T—This configuration allows Call Transfers to any destinations with one or more digits, like 123, 877656, or 76548765.

919........—This configuration only allows Call Transfers to remote numbers beginning with “919” and followed by eight digits,
                                    like 91912345678. However, Call Transfers to 9191234 or 919123456789 are not allowed.

### Backward Compatibility

To maintain backward compatibility, all Call Transfers from Cisco Unified SIP IP phones to any number (local or over the trunk)
                              are allowed when no transfer patterns are configured through the transfer-pattern , transfer-pattern blocked , or transfer max-length commands.

For Cisco Unified SCCP IP phones, if you do not configure transfer patterns, Call Transfers over the trunk are blocked.

#### Dial Plans

Whatever dial plan is used for external calls, the same numbers should be configured as specific numbers using the transfer-pattern command.

If a dial plan requires “9” to be dialed before making an external call, then prefix “9” to the transfer-pattern number. For
                                 example, if 12345678 is an external number that requires “9” to be dialed before making the external call, then the transfer-pattern
                                 number is 912345678.

### Transfer Max-Length

The transfer max-length command is used to indicate the maximum length of the number being dialed for Call Transfer. When only a specific number
                              of digits are allowed during a Call Transfer, value from 3 through 16 is configured. When the number dialed exceeds the maximum
                              length, then the Call Transfer is blocked.

For example, if you configure 5 as the maximum length, Call Transfers from Cisco Unified SIP IP phones allows up to a five-digit
                              directory number. All Call Transfers to directory numbers with more than five digits are blocked.

If only transfer max length is configured and conference max-length is not configured, then transfer max length takes effect for transfers and conferences.

### Transfer-Pattern Blocked

When the transfer-pattern blocked command is configured for a specific phone, no Call Transfers are allowed from that phone over the trunk.

This feature forces unconditional blocking of all Call Transfers from the specific phone to any other nonlocal numbers (external
                              calls from one trunk to another trunk). No Call Transfers from this specific phone are possible even when a transfer pattern
                              matches the dialed digits for transfer.

The following table compares the behaviors of Cisco Unified SCCP and SIP IP phones for specific configurations.

Configuration

Cisco Unified SCCP IP Phones

Cisco Unified SIP IP Phones

No transfer patterns are configured.

Blocks all nonlocal Call Transfers.

Allows all nonlocal Call Transfers for backward compatibility.

Specific transfer patterns are configured.

Allows Call Transfers to specific external entities.

Allows Call Transfers to specific external entities.

The transfer-pattern blocked command is configured.

Blocks all nonlocal Call Transfers are blocked.

The configuration reverts to the default, where no transfer patterns are configured.

All nonlocal Call Transfers are blocked.

The configuration unconditionally blocks all nonlocal Call Transfers. It does not return to the default, where all nonlocal
                                                      Call Transfers are allowed.

### Conference-Pattern Blocked

The conference-pattern blocked command is used to prevent extensions on a voice register Pool from initiating conferences.

The following table summarizes the behavior of the conference-pattern blocked command in relation to no conference-pattern blocked , conference max-length , no conference max-length , and transfer max-length commands.

Conference max-length

No conference max-length

No conference-pattern blocked (default case)

Allowing/Blocking of conference call depends on configured conference max-length.

Allowing/Blocking of conference call depends on configured transfer max-length.

Conference-pattern blocked

Conference calls are not allowed on SIP and SCCP phones.

Max-length <= allowed max-length

Max-length > allowed max-length

Transfer

Conference

Transfer

Conference

Transfer max-length +

No Conference max-length (use transfer max-length for conference cases too, as conference max-length not configured)

Y

Y

N

N

No transfer max-length + Conference max-length (conference max-length has precedence over transfer max-length for conference)

Y

Y

Y

N

No transfer max-length + Conference max-length (conference max-length has precedence over transfer max-length for conference)

Y

Y

N

N

No transfer max-length + No conference max-length

All transfer and conference calls are allowed.

### Configuring the Maximum Number of Digits for a Conference Call

#### Before you begin

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag OR ephone phone-tag

- conference max-length value

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice register pool pool-tag OR ephone phone-tag

#### Example:

```
Router(config)# voice register pool 25
```

Enters voice register Pool configuration mode and creates a Pool configuration for a Cisco Unified SIP IP phone in Cisco Unified
                                             Communications Manager Express or for a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST.

pool-tag : Unique number assigned to the Pool. Range is 1–100.

Enters voice register template configuration mode and defines a template of common parameters for Cisco Unified SIP IP phones.

template-tag : Declares a template tag. Range is 1–10.

Enters ephone configuration mode.

phone-tag : Unique sequence number that identifies this ephone during configuration tasks. The maximum number of ephones is version
                                                   and platform-specific. Type? To display range.

Step 4

conference max-length value

#### Example:

```
Router(config-telephony)# conference
max-lenght 6
```

Allows the conference of calls from Cisco IP phones to specified directory numbers of phones other than Cisco IP phones.

conference max-length Allows conference call depending on the configured conference max-length. Range is 3–16.

Step 5

end

#### Example:

```
Router(config-telephony)# end
```

Exits telephony-service configuration mode and enter privileged EXEC mode.

### Configuring Conference Blocking Options for Phones

#### Before you begin

Use Cisco Unified SRST 10.5 or a later version.

Configure the transfer-pattern command.

Configure the conference transfer-pattern command.

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag OR ephone phone-tag

- conference-pattern blocked

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router# enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice register pool pool-tag OR ephone phone-tag

#### Example:

```
Router(config)# voice register pool 25
```

Enters voice register Pool configuration mode and creates a Pool configuration for a Cisco Unified SIP IP phone in Cisco Unified
                                             Communications Manager Express or for a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST.

pool-tag : Unique number assigned to the Pool. Range is 1–100.

Enters voice register template configuration mode and defines a template of common parameters for Cisco Unified SIP IP phones.

template-tag : Declares a template tag. Range is 1–10.

Enters ephone configuration mode.

phone-tag : Unique sequence number that identifies this ephone during configuration tasks. The maximum number of ephones is version
                                                   and platform-specific. Type? To display range.

Step 4

conference-pattern blocked

#### Example:

```
Router(config-telephony)# conference-pattern
blocked
```

Allows the conference of calls from Cisco IP phones to specified directory numbers of phones other than Cisco IP phones.

conference-pattern blocked No conference calls are allowed.

Step 5

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits telephony-service configuration mode and enter global configuration mode.

### Transfer-Pattern Blocked

When the transfer-pattern blocked command is configured for a specific phone, no Call Transfers are allowed from that phone over the trunk.

This feature forces unconditional blocking of all Call Transfers from the specific phone to any other nonlocal numbers (external
                              calls from one trunk to another trunk). No Call Transfers from this specific phone are possible even when a transfer pattern
                              matches the dialed digits for transfer.

The following table compares the behaviors of Cisco Unified SCCP and SIP IP phones for specific configurations.

Configuration

Cisco Unified SCCP IP Phones

Cisco Unified SIP IP Phones

No transfer patterns are configured.

Blocks all nonlocal Call Transfers.

Allows all nonlocal Call Transfers for backward compatibility.

Specific transfer patterns are configured.

Allows Call Transfers to specific external entities.

Allows Call Transfers to specific external entities.

The transfer-pattern blocked command is configured.

Blocks all nonlocal Call Transfers are blocked.

The configuration reverts to the default, where no transfer patterns are configured.

All nonlocal Call Transfers are blocked.

The configuration unconditionally blocks all nonlocal Call Transfers. It does not return to the default, where all nonlocal
                                                      Call Transfers are allowed.

### Conference Transfer-Pattern

When both the transfer-pattern and conference transfer-pattern commands are configured and dialed digits match the configured transfer pattern, conference calls are allowed. However, when
                              the dialed digits do not match the configured transfer pattern, the conference call is blocked.

For information on provisioning Cisco Unified IP phones for secure access to web content using HTTPS, see the HTTPS Provisioning for Cisco Unified IP Phones section of Cisco Unified Communications Manager Express System Administrator Guide.

For configuration examples, see the Configuring HTTPS Support for Cisco Unified Communications Manager Express: Example section
                              of Cisco Unified Communications Manager Administration Guide .

### New Features in Cisco Unified SRST Version 9.1

Cisco Unified SRST 9.1 supports the following new features:

KEM Support for Cisco Unified SIP IP Phones

Enhancement in Speed-Dial Support

Voice Hunt Group Support

If you have older routers, such as the VG26nn and VG37nn platforms and Cisco Integrated Services Router (ISR) Generation 1
                                          platforms (Cisco ISR 1861, 2800, and 3800 Series), you must upgrade to Cisco ISR 881, 886VA, 887VA, 888, 888E, 1861E, 2900,
                                          3900, and 3900E Series platforms to utilize these new features.

#### Key Expansion Module Support for Cisco Unified SIP IP Phones

Cisco Unified IP Key Expansion Modules (KEMs) are supported on Cisco Unified 8851/51NR, 8861, 8961, 9951, and 9971 SIP IP
                                 phones from Cisco Unified SIP SRST 9.1.

For information on KEMs support for Cisco Unified 8851/51NR, 8861, 8961, 9951, and 971 SIP IP phones, see Phone Feature Support Guide for Cisco Unified Communications Manager Express, Cisco Unified SRST, Unified E-SRST, and Unified
                                    Secure SRST .

Restrictions

Bulk registration is not supported for KEMs in Cisco Unified SRST. Phones do not send bulk Registration Requests but always
                                       use the UDP port for registration.

KEMs is not supported for Cisco Unified SCCP IP Phones and Cisco Unified SIP IP Phones other than the Cisco Unified 8851/51NR,
                                       8861, 8961, 9951, and 9971 SIP IP phones.

Features configured on keys are disabled when supported Cisco Unified SIP IP phones are in Cisco Unified SIP SRST.

All Cisco Unified 8851/51NR, 8861,8961, 9951, and 9971 SIP IP phone restrictions and limitations apply to KEMs.

All Cisco Unified SIP SRST feature restrictions and limitations apply to KEMs.

For more information on how the blf-speed-dial , number , and speed-dial commands, in voice register Pool configuration mode, have been modified, see Cisco Unified Communications Manager Express Command Reference .

For information on installing KEMs on Cisco Unified IP Phone, see the Installing a Key Expansion Module on the Cisco Unified IP Phone section of Cisco Unified IP Phone 8961, 9951, and 9971 Administration Guide for Cisco Unified Communications Manager 7.1
                                 (3) (SIP).

For information on installing KEMs on Cisco Unified 8811, 8841, 8851, 8851NR, and 8861 Phones, see the Cisco IP Phone Key Expansion Module section of Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861 Administration Guide for Cisco Unified Communications Manager.

#### Enhancement in Speed-Dial Support

Cisco Unified SRST 9.1 ignores the “,” or comma (pause indicator) to avoid break-in speed-dial support.

Because the pause speed-dial feature (supported in Cisco Unified Communications Manager or Cisco Unified Communications Manager)
                                 is not supported in Cisco Unified SRST, Cisco Unified Communications Manager and phones (Cisco Unified SCCP IP phones and
                                 Cisco Unified SIP IP phones) registered in Cisco Unified SRST maintain backward compatibility in Cisco Unified SRST mode.
                                 When phones failover to the Cisco Unified SRST router during WAN outages and Cisco Unified Communications Manager fails, the
                                 phones only send the speed-dial numbers when the pause speed-dial buttons are pressed. The comma pause indicator is ignored
                                 and the preconfigured FAC, PIN, and DTMF are not sent.

For information on configuring speed-dial in Cisco Unified Communications Manager, see the “Device setup” chapter of Cisco Unified Communications Manager Administration Guide .

#### Voice Hunt Group Support

Cisco Unified SIP SRST 9.1 supports voice hunt groups. Voice hunt groups allow call placed to a single (pilot) number to contact
                                 multiple destinations.

There are three different types of voice hunt groups. Each type uses a different strategy to determine the first number that
                                 rings for successive calls to the pilot number until a number answers.

Parallel Hunt Groups—Allows an incoming call to simultaneously ring all the numbers in the hunt group member list.

Sequential Hunt Groups—Allows an incoming call to ring all the numbers in the left-to-right order in which they were listed
                                       while defining the hunt group. The first number in the list is always the first number tried when the pilot number is called.
                                       Maximum number of hops is not a configurable parameter for sequential hunt groups.

Longest-idle Hunt Groups—Allows an incoming call to first go to the number that has been idle the longest for the number of
                                       hops specified when the hunt group was defined. The longest-idle time is determined from the last time that a phone registered,
                                       reregistered, or went on-hook.

Cisco Unified SCCP IP phones support only ephone hunt groups whereas a voice hunt group supports Cisco Unified SCCP IP phones,
                                 Cisco Unified SIP IP phones. In addition, it also supports a mixture of Cisco Unified SCCP IP phones and Cisco Unified SIP
                                 IP phones.

With the voice hunt group feature preconfigured in the Cisco Unified SIP SRST router, voice hunt groups continue to be supported
                                 after phones fallback from Cisco Unified Communications Manager to the Cisco Unified SIP SRST router.

Restrictions

Hunt group statistics is not supported for voice hunt groups in Cisco Unified SRST.

Hunt group nesting or setting the final number of one hunt groups as the pilot of another hunt group is not supported.

### New Features in Cisco Unified SRST Version 9.0

### Support for Cisco Unified 6901 and 6911 SIP IP Phones

For information on feature support for the Cisco Unified 6901 and 6911SIP IP Phones in Cisco Unified SRST, see Phone Feature Support Guide for Cisco Unified Communications Manager Express, Cisco Unified SRST, Unified E-SRST, and Unified
                                 Secure SRST .

### Support for Cisco Unified 6921, 6941, 6945, and 6961 SIP IP Phones

For information on feature support for the Cisco Unified 6921, 6941, 6945, and 6961 SIP IP Phones in Cisco Unified SRST, see Phone Feature Support Guide for Cisco Unified Communications Manager Express, Cisco Unified SRST, Unified E-SRST, and Unified
                                 Secure SRST .

### Support for Cisco Unified 8941 and 8945 SIP IP Phones

For information on feature support for the Cisco Unified 8941 and 8945 SIP IP Phones in Cisco Unified SRST, see Phone Feature Support Guide for Cisco Unified Communications Manager Express, Cisco Unified SRST, Unified E-SRST, and Unified
                                 Secure SRST .

### Multiple Calls Per Line

Cisco Unified SRST 9.0 supports the Multiple Calls Per Line (MCPL) feature on Cisco Unified 6921, 6941, 6945, and 6961 SIP
                              IP phones. In addition, it supports Cisco Unified 8941, 8945 SCCP, and SIP IP phones.

Before Cisco Unified SRST 9.0, supports only two calls for every directory number (DN) on Cisco Unified 8941 and 8945 SCCP
                              IP phones.

With Cisco Unified SRST 9.0, the MCPL feature overcomes the limitation on the maximum number of calls per line.

Cisco Unified SRST 9.0 does not support the MCPL feature on Cisco Unified 6921, 6941, 6945, and 6961 SCCP IP phones. Allows
                              only two calls on these phones whereas allows only one call on octo-line directory numbers on these phones before activating
                              Call Forward Busy or busy tone.

### Cisco Unified 8941 and 8945 SCCP IP Phones

Before Cisco Unified SRST 9.0, the values for the max-dn and timeouts busy commands were hardcoded for Cisco Unified 8941 and 8945 SCCP IP phones.

In Cisco Unified SRST 9.0, you can configure the max-dn and timeouts busy commands in call-manager-fallback configuration mode. Use the max-dn command to set the maximum number of DNs that can be supported by the router and enable dual-line mode, octo-line mode, or
                              both modes. Use the timeouts busy command to set the timeout value for Call Transfers to busy destinations.

For configuration information, see Configuring the Maximum Number of Calls .

### Cisco Unified 6921, 6941, 6945, 6961, 8941, and 8945 SIP IP Phones

In Cisco Unified SRST 9.0, the maximum number of calls for Cisco Unified 6921, 6941, 6945, 6961, 8941, and 8945 SIP IP phones
                              is controlled by the phones.

Prerequisites

Cisco Unified SRST 9.0 and later versions.

Correct firmware is installed:

9.2(1) or a later version for Cisco Unified 6921, 6941, 6945 and 6961 SIP IP phones.

9.2(2) or a later version for Cisco Unified 8941 and 8945 SIP IP phones.

### Voice and Fax Support on Cisco ATA-187

Cisco ATA-187 is a SIP-based analog phone adapter that turns traditional phone devices into IP devices. Cisco ATA-187 can
                              connect with a regular analog FXS phone or fax machine on one end, while the other end is an IP side that uses SIP for signaling
                              and registers as a Cisco Unified SIP IP phone.

Cisco ATA-187 functions as a Cisco Unified SIP IP phone that supports T.38 fax relay and fax pass-through, enabling the real-time
                              transmission of fax over IP networks. The fax rate is from 7.2 to 14.4 kbps.

For information on feature support for the Cisco ATA-187 in Cisco Unified SRST, see Phone Feature Support Guide for Cisco Unified Communications Manager Express, Cisco Unified SRST, Unified E-SRST, and Unified
                                 Secure SRST .

For more information on Cisco ATA-187, see Cisco ATA 187 Analog Telephone Adaptor Administration Guide for SIP .

### New Features in Cisco Unified SRST Version 8.8

Cisco Unified SRST 8.8 supports the following new Cisco Unified SCCP IP phones:

Cisco Unified 6945 SCCP IP Phones

Cisco Unified 8941 SCCP IP Phones

Cisco Unified 8945 SCCP IP Phones

#### Support for Cisco Unified 6945, 8941, and 8945 SCCP IP Phones

For information on feature support for the Cisco Unified 6945, 8941, and 8945 SCCP IP Phones in Cisco Unified SRST, see Phone Feature Support Guide for Cisco Unified Communications Manager Express, Cisco Unified SRST, Unified E-SRST, and Unified
                                    Secure SRST .

For information on the Cisco Unified 6945 SCCP IP Phone, see Cisco Unified IP Phone 6945 User Guide for Cisco Unified Communications Manager Express Version 8.8 (SCCP) .

For information on the Cisco Unified 8941 and 8945 SCCP IP Phones, see Cisco Unified IP Phone 8941 and 8945 User Guide for Cisco Unified Communications Manager Express Version 8.8 (SCCP) .

### New Features in Cisco Unified SRST Version 8.0

Beginning with Cisco IP Phone firmware 8.5(3) and Cisco IOS Release 15.1(1)T, Cisco Unified SRST supports SIP signaling over
                              UDP, TCP, and TLS connections, providing both RTP and SRTP media connections based on the security settings of the IP phone.

### New Features in Cisco Unified SRST Version 7.0/4.3

Cisco Unified SRST 7.0/4.3 supports the following new features:

Configuring Eight Calls per Button (Octo-Line)

Configuring Consultative Transfer

### New Features in Cisco Unified SRST Version 4.2(1)

Cisco Unified SRST Version 4.2(1) introduces the new feature enhancements for Enhanced 911 Services .

### New Features in Cisco Unified SRST Version 4.1

Cisco Unified SRST Version 4.1 introduces the following new feature:

Enhanced 911 Services

### New Features in Cisco Unified SRST Version 4.0

### Additional Cisco Unified IP Phone Support

The following IP phones are supported with Cisco Unified SRST systems:

Cisco Unified IP Phone 7911G

Cisco Unified IP Phone 7941G and Cisco Unified IP Phone 7941G-GE

Cisco Unified IP Phone 7960G

Cisco Unified IP Phone 7961G and Cisco Unified IP Phone 7961G-GE

In addition, the Cisco Unified IP Phone 7914 Expansion Module can attach to the Cisco 7941G-GE and Cisco 7961G-GE. The Cisco
                              7914 Expansion Module adds additional features, such as adding 14 line appearances or speed-dial numbers to your phone. You
                              can attach one or two expansion modules to your IP phone. When you use two expansion modules, you have 28 additional line
                              appearances or speed-dial numbers, or a total of 34 line appearances or speed-dial numbers. For more information, see Cisco IP Phone 7914 Expansion Module Quick Start Guide .

No additional SRST configuration is required for these phones.

The show ephone command is enhanced to display the configuration and status of the new Cisco IP Phones added to SRST Version 4.0. For more
                              information, see the show ephone command in Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions) .

To determine compatible firmware, platforms, memory, and additional voice products that are associated with Cisco Unified
                              SRST 4.0, see Cisco Unified SRST 4.3 Supported Firmware, Platforms, Memory, and Voice Products .

### Cisco IP Communicator Support

Cisco IP Communicator is a software-based application that delivers enhanced telephony support on personal computers. This
                              SCCP-based application allows computers to function as IP phones, providing high-quality voice calls on the road, in the office,
                              or from wherever users may have access to the corporate network. Cisco IP Communicator appears on a user's computer monitor
                              as a graphical, display-based IP phone with a color screen, a key pad, feature buttons, and soft keys.

### Fax Pass-through using SCCP and ATAs Support

Fax pass-through mode is now supported using Cisco VG 224 voice gateways, Analog Telephone Adaptors (ATA), and SCCP. ATAs
                              ship with SIP firmware, so SCCP firmware must be loaded before this feature can be used.

For ATAs that are registered to a Cisco Unified SRST system to participate in FAX calls, they must have their ConnectMode
                                          parameter set to use the “standard payload type 0/8” as the RTP payload type in FAX pass-through mode. For ATAs used with
                                          Cisco Unified SRST 4.0 and higher versions, this is done by setting bit 2 of the ConnectMode parameter to 1 on the ATA. For
                                          more information, see the “Parameters and Defaults” chapter in Cisco ATA 186 and Cisco ATA 188 Analog Telephone Adaptor Administrator's Guide for SCCP .

### H.323 VoIP Call Preservation Enhancements for WAN Link Failures for SCCP Phones

H.323 VoIP call preservation enhancements for WAN link failures sustains connectivity for H.323 topologies where signaling
                              is handled by an entity, such as Cisco Unified Communications Manager, that is different from the other endpoint and brokers
                              signaling between the two connected parties.

Call preservation is useful when a gateway and the other endpoint (typically a Cisco Unified IP phone) are collocated at the
                              same site and the call agent is remote and therefore more likely to experience connectivity failures. H.323 VoIP call preservation
                              enhancements does not support SIP Phones.

For configuration information see the “Configuring H.323 Gateways” chapter in Cisco IOS H.323 Configuration Guide .

### Video Support

This feature allows you to set video parameters for the Cisco Unified SRST to maintain close feature parity with Cisco Unified
                              CM. When the Cisco Unified SRST is enabled, Cisco Unified IP Phones do not have to be reconfigured for video capabilities
                              because all ephones retain the same configuration used with Cisco Unified CM. However, you must enter call-manager-fallback
                              configuration mode to set video parameters for Cisco Unified SRST. The feature set for video is the same as that for Cisco Unified
                              SRST audio calls.

For more information, see Setting Video Parameters .

### New Features in Cisco Unified SRST Version 3.4

### Cisco SIP SRST 3.4

Cisco SIP SRST Version 3.4 describes SRST functionality for Session Initiation Protocol (SIP) networks. Cisco SIP SRST Version
                              3.4 provides backup to an external SIP call control (IP-PBX) by providing basic registrar and back-to-back user agent (B2BUA)
                              services. These services are used by a SIP IP phone in the event of a WAN connection outage when the SIP phone is unable to
                              communicate with its primary SIP proxy.

Cisco SIP SRST Version 3.4 can support SIP phones with standard RFC 3261 feature support locally and across SIP WAN networks.
                              With Cisco SIP SRST Version 3.4, SIP phones can place calls across SIP networks in the same way as Skinny Client Control Protocol
                              (SCCP) phones. For full information about SIP SRST, Version 3.4, see Cisco SIP SRST Version 3.4 System Administrator Guide .

### New Features in Cisco SRST Version 3.3

### Secure SRST

Secure Cisco IP phones that are located at remote sites and that are attached to gateway
                              routers can communicate securely with Cisco Unified Communications Manager using the
                              WAN. But if the WAN link or Cisco Unified Communications Manager goes down, all
                              communication through the remote phones becomes nonsecure. To overcome this situation,
                              gateway routers can now function in secure SRST mode, which activates when the WAN link
                              or Cisco Unified Communications Manager goes down. When the WAN link or Cisco Unified
                              Communications Manager is restored, Cisco Unified Communications Manager resumes secure
                              call-handling capabilities.

Secure SRST provides new SRST security features such as authentication, integrity, and media encryption. Authentication provides
                              assurance to one party that another party is whom it claims to be. Integrity provides assurance that the given data has not
                              been altered between the entities. Encryption implies confidentiality; that is, that no one can read the data except the intended
                              recipient. These security features allow privacy for SRST voice calls and protect against voice security violations and identity
                              theft. For more information, see Configure Secure SRST for SCCP and SIP .

### Cisco Unified IP Phone 7970G and Cisco Unified 7971G-GE Support

The Cisco Unified IP Phones 7970G and 7971G-GE are full-featured telephones that provide voice communication over an IP network.
                              They function much like a traditional analog telephones, allowing you to place and receive phone calls and to access features
                              such as mute, hold, transfer, speed dial, call forward, and more. In addition, because the phones are connected to your data
                              network, they offer enhanced IP telephony features, including access to network information and services, and customizable
                              features and services. The phones also support security features that include file authentication, device authentication,
                              signaling encryption, and media encryption.

The Cisco Unified IP Phones 7970G and 7971G-GE also provide a color touchscreen, support for up to eight line or speed-dial
                              numbers, context-sensitive online help for buttons and feature, and a variety of other sophisticated functions. No configurations
                              specific to SRST are necessary.

For more information, see the Cisco Unified IP Phone 7900 Series documentation index .

The Cisco Unified IP Phone 7914 Expansion Module can attach to your Cisco Unified IP Phones 7970G and 7971G-GE. See the Cisco Unified IP Phone Expansion Module 7914 Support section for more information.

### Enhancement to the show ephone Command

The show ephone command is enhanced to display the configuration and status of the Cisco Unified IP Phone 7970G and Cisco Unified IP Phone
                              7971G-GE. For more information, see the show ephone command in Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions) .

### New Features in Cisco SRST Version 3.2

### Enhancement to the alias Command

The alias command is enhanced as follows:

The cfw keyword was added, providing call forward no-answer/busy capabilities.

The maximum number of alias commands used for creating calls to telephone numbers that are unavailable during Cisco Unified Communications Manager fallback
                                    was increased to 50.

The alternate-number argument can be used in multiple alias commands.

For more information, see the alias command in Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions) .

### Enhancement to the cor Command

The maximum number of cor lists has increased to 20.

For more information, see the cor command in Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions) .

### Enhancement to the pickup Command

The pickup command was introduced to enable the PickUp soft key on all Cisco Unified IP Phones, allowing an external Direct Inward Dialing
                              (DID) call coming into one extension to be picked up from another extension during SRST.

For more information, see the pickup command in Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions) .

### Enhancement to the user-locale Command

The user-locale command is enhanced to display the Japanese Katakana country code. Japanese Katakana is available in Cisco Unified Communications
                              Manager V4.0 or later versions.

For more information, see the user-locale command in the Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions) .

### Increased the Number of Cisco Unified IP Phones Supported on the Cisco 3845

The Cisco 3845 now supports 720 phones and up to 960 ephone-dns or virtual voice ports.

### MOH Live-Feed Support

Cisco Unified SRST is enhanced with the new moh-live command. The moh-live command provides live-feed MOH streams from an audio device connected to an E&M or FXO port to Cisco IP phones in SRST mode.
                              If an FXO port is used for a live feed, the port must be supplied with an external third-party adaptor to provide a battery
                              feed. Music from a live feed is obtained from a fixed source and is continuously fed into the MOH playout buffer instead of
                              being read from a flash file. Live-feed MOH can also be multicast to Cisco IP phones. See the Integrating Cisco Unified Communications Manager and Cisco Unified SRST to Use Cisco Unified SRST as a Multicast MOH Resource section for configuration instructions.

### No Timeout for Call Preservation

To preserve existing H.323 calls on the branch in the event of an outage, disable the H.225 keepalive timer by entering the no h225 timeout keepalive command. This feature is supported in Cisco IOS Releases 12.3(7)T1 and higher versions. See the Cisco Unified SRST Feature Overview section for more information.

H.323 is not supported with SIP phones.

### RFC 2833 DTMF Relay Support

Cisco Skinny Client Control Protocol (SCCP) phones, such as those used with Cisco SRST systems, provide only out-of-band DTMF
                              digit indications. To enable SCCP phones to send digit information to remote SIP-based IVR and voice-mail applications, Cisco
                              SRST 3.2 and later versions provide conversion from the out-of-band SCCP digit indication to the SIP standard for DTMF relay,
                              which is RFC 2833. You select this method in the SIP VoIP dial peer using the dtmf-relay rtp-nte command. See the How to Configure DTMF Relay for SIP Applications and Voicemail section for configuration instructions.

To use voicemail on a SIP network that connects to a Cisco Unity Express system, use a nonstandard SIP Notify format. To configure
                              the Notify format, use the sip-notify keyword with the dtmf-relay command. Using the sip-notify keyword may be required for backward compatibility with Cisco SRST Versions 3.0 and 3.1.

### Translation Profile Support

Cisco SRST 3.2 and later versions support translation profiles. Translation profiles allow you to group translation rules
                              together and to associate translation rules with the following:

Called numbers

Calling numbers

Redirected called numbers

See the Enabling Translation Profiles section for more configuration information. For more information on the translation-profile command, see Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions) .

### New Features in Cisco Unified SRST Version 3.1

Cisco Unified SRST V3.1 introduced the new features described in the following sections:

Cisco Unified IP Phone 7920 Support

Cisco Unified IP Phone 7936 Support

For information about Cisco Unified IP phones, see the Cisco Unified IP Phone 7900 Series documentation.

#### Cisco Unified IP Phone 7920 Support

The Cisco Unified Wireless IP Phone 7920 is an easy-to-use IEEE 802.11b wireless IP phone that provides comprehensive voice
                                 communications in conjunction with Cisco Unified CM and Cisco Aironet 1200, 1100, 350, and 340 Series of Wi-Fi (IEEE 802.11b)
                                 access points. As a key part of the Cisco AVVID Wireless Solution, the Cisco Unified Wireless IP Phone 7920 delivers seamless
                                 intelligent services, such as security, mobility, quality of service (QoS), and management, across an end-to-end Cisco network.

No configuration is necessary.

#### Cisco Unified IP Phone 7936 Support

The Cisco Unified IP Conference Station 7936 is an IP-based, hands-free conference room station that uses VoIP technology.
                                 The IP Conference Station replaces a traditional analog conferencing unit by providing business conferencing features—such
                                 as call hold, call resume, call transfer, call release, redial, mute, and conference—over an IP network.

No configuration is necessary.

### New Features in Cisco SRST Version 3.0

### Additional Language Options for IP Phone Display

Displays for the Cisco Unified IP Phone 7940G and Cisco Unified IP Phone 7960G can be configured with extra ISO-3166 codes
                              for German, Danish, Spanish, French, Italian, Japanese, Dutch, Norwegian, Portuguese, Russian, Swedish, United States.

This feature is available only for Cisco Unified SRST running under Cisco Unified Communications Manager V3.2.

### Consultative Call Transfer and Forward Using H.450.2 and H.450.3 for SCCP Phones

Cisco Unified SRST V1.0, Cisco Unified SRST V2.0, and Cisco Unified SRST V2.1 allow blind Call Transfers and blind call forwarding.
                              Blind calls do not give transferring and forwarding parties the ability to announce or consult with destination parties. These
                              three versions of Cisco Unified SRST use a Cisco Unified SRST proprietary mechanism to perform blind transfers. Cisco Unified
                              SRST V3.0 adds the ability to perform Call Transfers with consultation using the ITU-T H.450.2 (H.450.2) standard and call
                              forwarding using the ITU-T H.450.3 (H.450.3) standard for H.323 calls.

Cisco Unified SRST V3.0 provides support for IP phones to initiate Call Transfer and forwarding with H.450.2 and H.450.3 by
                              using the default session application. The built-in H.450.2 and H.450.3 support that is provided by the default session application
                              applies to Call Transfers and call forwarding initiated by IP phones, regardless of the PSTN interface type.

All voice gateway routers in the VoIP network must support H.450. For H.450 support, routers with Cisco Unified SRST must
                                          run either Cisco Unified SRST V3.0 and higher versions or Cisco IOS Release 12.2(15)ZJ and later releases. Routers without
                                          Cisco Unified SRST must run either Cisco Unified SRST V2.1 and higher versions or Cisco IOS Release 12.2(11)YT and later releases.
                                          SIP phones do not support this feature.

For more information about the default session application, see the Default Session Application Enhancements Guide .

For configuration information, see the Enabling Consultative Call Transfer and Forward Using H.450.2 and H.450.3 with Cisco Unified SRST 3.0 section.

### Customized System Message for Cisco Unified IP Phones

The display message that appears on Cisco Unified IP Phone 7905G, Cisco Unified IP Phone 7940G, Cisco Unified IP Phone 7960G,
                              and Cisco Unified IP Phone 7910 units when they are in fallback mode can be customized. The new system message command allows
                              you to edit these display messages on a per-router basis. The custom system message feature supports English only.

For further information, see the Configuring Customized System Messages for Cisco Unified IP Phones section.

### Dual-Line Mode

A new keyword that was added to the max-dn command allows you to set IP phones to dual-line mode. Each dual-line IP phone must have one voice port and two channels
                              to handle two independent calls. This mode enables call waiting, Call Transfer, and conference functions on a single ephone-dn
                              (ephone directory number). There is a maximum number of DNs available during Cisco Unified SRST fallback. The max-dn command affects all IP phones on a Cisco Unified SRST router.

For configuration information, see the Configuring Dual-Line Phones section.

### E1 R2 Signaling Support

Cisco Unified SRST V3.0 supports E1 R2 signaling. R2 signaling is an international signaling standard that is common to channelized
                              E1 networks; however, there is no single signaling standard for R2. The ITU-T Q.400-Q.490 recommendation defines R2, but several
                              countries and geographic regions implement R2 in entirely different ways. Cisco addresses this challenge by supporting many
                              localized implementations of R2 signaling in its Cisco IOS Software.

The Cisco E1 R2 signaling default is ITU, which supports the following countries: Denmark, Finland, Germany, Russia (ITU variant),
                              Hong Kong (ITU variant), and South Africa (ITU variant). The expression “ITU variant” means that there are multiple R2 signaling
                              types in the specified country, but Cisco supports the ITU variant.

Cisco also supports specific local variants of E1 R2 signaling in the following regions, countries, and corporations:

Argentina

Australia

Bolivia

Brazil

Bulgaria

China

Colombia

Costa Rica

East Europe (includes Croatia, Russia, and Slovak Republic)

Ecuador (ITU)

Ecuador (LME)

Greece

Guatemala

Hong Kong (uses the China variant)

Indonesia

Israel

Korea

Laos

Malaysia

Malta

New Zealand

Paraguay

Peru

Philippines

Saudi Arabia

Singapore

South Africa (Panaftel variant)

Telmex Corporation (Mexico)

Telnor Corporation (Mexico)

Thailand

Uruguay

Venezuela

Vietnam

### European Date Formats

The date format on a Cisco IP phone display can be configured with the following two extra formats:

yy-mm-dd (year-month-day)

yy-dd-mm (year-day-month)

For configuration information, see the Configuring IP Phone Clock, Date, and Time Formats section.

### Huntstop for Dual-Line Mode

A new keyword was added to the huntstop command. The channel keyword causes hunting to skip the secondary channel in dual-line configuration if the primary line is busy or does not answer.

For configuration information, see the Configuring Dial-Peer and Channel Hunting section.

### Music On Hold for Multicast from Flash Files

You can configure Cisco Unified SRST to support continuous multicast output of MOH from a flash MOH file in flash memory.

For more information, see the Defining XML API Schema section.

### Ringing Timeout Default

A ringing timeout default can be configured for extensions on which no-answer call forwarding has not been enabled. Expiration
                              of the timeout causes incoming calls to return a disconnect code to the caller. This mechanism provides protection against
                              hung calls for inbound calls received over interfaces such as Foreign Exchange Office (FXO) that do not have forward-disconnect
                              supervision. For more information, see the Configuring the Ringing Timeout Default section.

### Secondary Dial Tone

Secondary dial tone is available for Cisco Unified IP Phones running Cisco Unified SRST. The secondary dial tone is generated
                              when you dial a predefined PSTN access prefix. For example, you would hear different dial tone when a designated number is
                              pressed to reach an outside line.

The secondary dial tone is created through the secondary dial tone command. For more information, see the Configuring a Secondary Dial Tone section.

### Enhancement to the Show ephone Command

The show ephone command is enhanced to display the following:

Configuration and status of additional phones (new keywords: 7905, 7914, 7935, ATA )

Status of all phones with the call-forwarding all (CFA) feature enabled on at least one of their DNs (new keyword: cfa )

For more information, see the show ephone command in Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions) .

### System Log Messages for Phone Registrations

Diagnostic messages are added to the system log whenever a phone registers or unregisters from Cisco Unified SRST.

### Three-Party G.711 Ad Hoc Conferencing

Cisco Unified SRST supports three-party instant meeting conferencing using the G.711 coding technique. For conferencing to
                              be available, connect two lines to one or more buttons of an IP phone.

For more information, see the Enabling Three-Party G.711 Ad Hoc Conferencing section.

### Support for Cisco VG248 Analog Phone Gateway 1.2(1) and Higher Versions

The Cisco VG248 Analog Phone Gateway is a mixed-environment solution, enabled by Cisco Unified Communications system. It allows
                              organizations to support their legacy analog devices while taking advantage of the new opportunities afforded by using IP
                              telephony. The Cisco VG248 is a high-density gateway for using analog phones, fax machines, modems, voicemail systems, and
                              speakerphones within an enterprise voice system based on Cisco Unified Communications Manager.

During Cisco Unified Communications Manager fallback, Cisco Unified SRST considers the Cisco VG248 to be a group of Cisco
                              Unified IP Phones. Cisco Unified SRST counts each of the 48 ports on the Cisco VG248 as a separate Cisco Unified IP Phone.
                              Support for Cisco VG248 Version 1.2(1) and higher versions is also available in Cisco Unified SRST Version 2.1.

For more information, see Cisco VG248 Analog Phone Gateway Data Sheet and Cisco VG248 Analog Phone Gateway Version 1.2(1) Release Notes .

### New Features in Cisco SRST Version 2.1

Cisco SRST V2.1 introduced the new features described in the following sections:

For information about Cisco Unified IP phones, see the Cisco Unified IP Phone 7900 Series documentation.

#### Additional Language Options for IP Phone Display

Displays for the Cisco Unified IP Phone 7940G and Cisco Unified IP Phone 7960G can be configured with ISO-3166 codes for the
                                 following countries:

France

Germany

Italy

Portugal

Spain

United States

This feature is available only in Cisco Unified SRST running under Cisco Unified Communications Manager V3.2.

For configuration information, see the Configuring IP Phone Language Display section.

#### Cisco Unified SRST Aggregation

For systems running Cisco Unified Communications Manager 3.3(2) and later versions, the restriction of running Cisco Unified
                                 SRST on a default gateway was removed. Multiple SRST routers can be used to support more phones. Carefully plan and configure
                                 the dial peers and dial plans for Call Transfer and forwarding to work properly.

#### Cisco ATA 186 and ATA 188 Support

The Cisco ATA analog phone adapters are handset-to-Ethernet adapters that allow regular analog phones to operate on IP-based
                                 telephony networks. Cisco ATAs support two voice ports, each with an independent phone number. The Cisco ATA 188 also has
                                 an RJ-45 10/100BASE-T data port. Cisco Unified SRST supports Cisco ATA 186 and Cisco ATA 188 using Skinny Client Control Protocol
                                 (SCCP) for the voice calls only.

#### Cisco Unified IP Phone 7902G Support

The Cisco Unified IP Phone 7902G is an entry-level IP phone that addresses the voice communications needs of a lobby, laboratory,
                                 manufacturing floor, hallway, or other area where only basic calling capability is required.

The Cisco Unified IP Phone 7902G is a single-line IP phone with fixed feature keys that provide one-touch access to the redial,
                                 transfer, conference, and voicemail access features. Consistent with other Cisco IP phones, the Cisco Unified IP Phone 7902G
                                 supports inline power, which allows the phone to receive power over the LAN. This capability gives the network administrator
                                 centralized power control and thus greater network availability.

#### Cisco Unified IP Phone 7905G Support

The Cisco Unified IP Phone 7905G is a basic IP phone that provides a core set of business features. It provides single-line
                                 access and four interactive softkeys that guide a user through call features and functions via the pixel-based LCD. The graphic
                                 capability of the display presents calling information, intuitive access to features, and language localization in future
                                 firmware releases. The Cisco Unified IP Phone 7905G supports inline power, which allows the phone to receive power over the
                                 LAN.

No configuration is necessary.

#### Cisco Unified IP Phone 7912G Support

The Cisco Unified IP Phone 7912G provides core business features and addresses the communication needs of a cubicle worker
                                 who conducts low to medium phone traffic. Four dynamic softkeys provide access to call features and functions. The graphic
                                 display shows calling information and allows access to features.

The Cisco Unified IP Phone 7912G supports an integrated Ethernet switch, providing LAN connectivity to a local PC. In addition,
                                 the Cisco Unified IP Phone 7912G supports inline power, which allows the phone to receive power over the LAN. This capability
                                 gives the network administrator centralized power control and thus greater network availability. The combination of inline
                                 power and Ethernet switch support reduces cabling needs from a single wire to the desktop.

#### Cisco Unified IP Phone Expansion Module 7914 Support

The Cisco Unified IP Phone 7914 Expansion Module attaches to your Cisco Unified IP Phone 7960G, adding 14 line appearances
                                 or speed-dial numbers to your phone. You can attach one or two expansion modules to your IP phone. When you use two expansion
                                 modules, you have 28 additional line appearances or speed-dial numbers or a total of 34 line appearances or speed-dial numbers.

#### Enhancement to the Dial Plan-Pattern Command

A new keyword was added to the dialplan-pattern command. The extension-pattern keyword sets an extension number’s leading digit pattern when it is different from the E.164
                                 phone number’s leading digits defined in the pattern variable. This enhancement allows manipulation of IP phone abbreviated extension number prefix digits. See the dialplan-pattern command in Cisco Unified SRST and Cisco Unified SIP SRST Command Reference (All Versions) .

### New Features in Cisco SRST Version 2.02

### Cisco Unified IP Phone Conference Station 7935 Support

The Cisco IP Conference Station 7935 is an IP-based, full-duplex hands-free conference station for use on desktops and offices
                              and in small-to-medium-sized conference rooms. This device attaches a Cisco Catalyst 10/100 Ethernet switch port with a simple
                              RJ-45 connection and dynamically configures itself to the IP network via the DHCP. Other than connecting the Cisco 7935 to
                              an Ethernet switch port, no further administration is necessary. The Cisco 7935 dynamically registers to Cisco Unified CM
                              for connection services and receives the appropriate endpoint phone number and any software enhancements or personalized settings,
                              which are preloaded within Cisco Unified CM.

The Cisco Unified IP Phone 7935 provides three soft keys and menu navigation keys that guide a user through call features
                              and functions. The Cisco Unified IP Phone 7935 also features a pixel-based LCD display. The display provides features such
                              as date and time, calling party name, calling party number, digits dialed, and feature and line status. No configuration is
                              necessary.

### Increase in Directory Numbers

The following table shows the increases in directory numbers.

Cisco Router

Maximum Phones

Increase in Maximum Directory Number

From

To

Cisco 1751

24

96

120

Cisco 1760

24

96

120

Cisco 2600XM

24

96

120

Cisco 2691

72

216

288

Cisco 3640

72

216

288

Cisco 3660

240

720

960

Cisco 3725

144

432

576

Cisco 3745

240

720

960

### Cisco Unity Voicemail Integration Using In-Band DTMF Signaling Across the PSTN and BRI/PRI

Cisco Unity voicemail and other voicemail systems can be integrated with Cisco Unified SRST. Voicemail integration introduces
                              six new commands:

| Chapter or Appendix | Description |
|---|---|
| Cisco Unified SRST Feature Overview | Gives a brief description of Cisco Unified SRST and provides information on the supported platforms and Cisco Unified IP Phones.
                                       In addition, it describes any prerequisites or restrictions that should be addressed before Cisco Unified SIP SRST is configured. |
| Setting Up the Network | Describes how to set up a Cisco Unified SRST system to communicate with your network. |
| Enhanced SRST | Describes how to configure the Cisco Unified Enhanced SRST feature in your network. |
| Cisco Unified SIP SRST | Describes the features for Cisco Unified SIP SRST Version 4.1 and provides the associated configuration procedures. |
| Setting Up Cisco Unified IP Phones using SCCP | Describes how to set up the basic Cisco Unified SRST phone configuration. |
| Setting Up Cisco Unified IP Phones using SIP | Describes features available in Version 3.0 that are also necessary for Version 3.4. Features include instructions on how
                                       to provide a backup to an external SIP call control (IP-PBX) by providing basic registrar services. These services are used
                                       by a SIP IP phone in the event of a WAN connection outage when the SIP phone is unable to communicate with its primary SIP
                                       proxy. |
| Configuring Call Handling | Describes how to configure incoming and outgoing calls. |
| Configure Secure SRST for SCCP and SIP | Describes the Secure SRST security functionality to the Cisco Unified SRST. |
| Integrating Voice Mail with Cisco Unified SRST | Describes how to set up voicemail. |
| Setting Video Parameters | Describes how to set up video parameters. |
| Monitoring and Maintaining Cisco Unified SRST | Provides a list of useful show commands for monitoring and maintaining Cisco Unified SRST. |
| Appendix A: Configuring Cisco Unified SIP SRST Features Using Redirect Mode | Describes features using redirect mode, which applies to version 3.0 only. |
| Appendix B: Integrating Cisco Unified Communications Manager and Cisco Unified SRST to Use Cisco Unified SRST as a Multicast
                                          MOH Resource | Describes how to configure Cisco Unified CM and Cisco Unified SRST to enable multicast music-on-hold (MOH). |

| Cisco Unified SRST | Cisco IOS Release | Enhancements or Modifications |
|---|---|---|
| Version 15.0 | Cisco IOS XE 26.1.1 | Advanced TLS security compliance and control. See Configure Secure SRST for SCCP and SIP . Support for Cisco Desk Phone 9800 Series, and Cisco Desk Phone 9811 Series. See Unified SRST/E-SRST 15.0 Supported Firmware, Platforms, Memory, and Voice Products . |
| Version 15.0 | Cisco IOS XE 17.18.2 | SRST support on C8375-E-G2 router platform with virtual DSP (vDSP) enabled. See Unified SRST/E-SRST 15.0 Supported Firmware, Platforms, Memory, and Voice Products . Security warnings for usage of legacy TLS and associated weaker ciphers. See Signaling Security on Unified SRST - TLS . |
| Version 15.0 | Cisco IOS XE 17.18.1a | Cisco Smart Licensing reports flex subscription entitlement tag for SRST platforms. To maintain the continued support and
                                             entitlements to the future application versions, purchase a Collaboration Flex subscription. See Smart License Operation . Support for Cisco Desk Phone 9861 (DP-9861), and Cisco Desk Phone 9871 (DP-9871). See Unified SRST/E-SRST 15.0 Supported Firmware, Platforms, Memory, and Voice Products . |
| Version 14.5 | Cisco IOS XE 17.15.1a | Support for Cisco Desk Phone 9841 (DP-9841), and Cisco Desk Phone 9851 (DP-9851). See Unified SRST/E-SRST 14.5 Supported Firmware, Platforms, Memory, and Voice Products . |
| Version 14.4 | Cisco IOS XE 17.14.1a | TLS version 1.3 support —TLS version 1.3 and associated ciphers support for secure SIP and SCCP SRST: AES128_GCM_SHA256 AES256_GCM_SHA384 CHACHA20_POLY1305_SHA256 |
| Version 14.3 | Cisco IOS XE Dublin
                                             17.11.1a Cisco IOS XE Cupertino 17.9.3a | Webex Survivability Gateway Mode —Webex Survivability Gateway mode now supports survivability for Webex Calling endpoints and Unified SRST-based survivability
                                       for on-premises endpoints that register to Cisco Unified Communications Manager. Site Survivability for Webex Calling —Configure a Webex Survivability Gateway to provide a calling fallback service for Webex Calling endpoints. |
| Version 14.3 | Cisco IOS XE Dublin
                                          17.10.1a | YANG model enhancements for Unified SRST: Programmability Guide for Cisco
                                          IOS XE Unified Communications VoIP Products https://www.cisco.com/c/en/us/td/docs/routers/sdwan/command/sdwan-cr-book.html |
| Version 14.3 | Cisco IOS XE Cupertino
                                             17.9.1a | Webex Managed Gateway Command Reference Introduced the following commands as part of Cisco Webex Calling Branch Survivability: mode webex-sgw voice register webex-sgw sync show voice register webex-sgw users Modified the following command as part of Cisco Webex Calling Branch Survivability: id (voice register pool) modified to include phone-number e164-number and extension-number extension-number |
| Version 14.3 | Cisco IOS XE Cupertino
                                             17.9.1a | CDR Accounting Overview Configuring File Accounting gw-accounting |
| Version 14.2 | Cisco IOS XE Cupertino
                                             17.8.1a | SHA2-Cipher-Only Mode for Unified Secure SRST |
| Version 14.2 | Cisco IOS XE Cupertino
                                          17.8.1a | SIP OAuth Client Registration for Unified Secure SRST |
| Version 14.1 | Cisco IOS XE Bengaluru 17.6.1a | Programmability Guide for Cisco IOS XE Unified Communications VoIP Products |
| Version 14.1 | Cisco IOS XE Bengaluru 17.5.1a Release | Support for Unified SRST on Cisco 1100 Integrated Services Router Support for Unified SRST and E-SRST on Cisco 8200L Catalyst Series Edge Platforms |
| Version 14.1 | Cisco IOS XE Bengaluru 17.4.1a Release | Support for Unified SRST and E-SRST on Cisco 8200 Catalyst Series Edge Platforms Smart Licensing Using Policy— Cisco Smart Licensing for Unified SRST Smart Licensing Using Policy— Cisco Smart Licensing for Unified E-SRST |
| Version 14.1 | Cisco IOS XE Amsterdam 17.3.2 Release | Support for Unified SRST and E-SRST on Cisco 8300 Catalyst Series Edge Platforms Smart Licensing Using Policy— Cisco Smart Licensing for Unified SRST Smart Licensing Using Policy— Cisco Smart Licensing for Unified E-SRST |
| Version 12.8 | Cisco IOS XE Amsterdam 17.2.1r | Cisco Jabber with Unified SRST VRF Support for Unified SRST Support for YANG Models in Unified SRST |
| Version 12.7 | Cisco IOS XE Amsterdam 17.1.1 | Support for maximum number of devices in Cisco 4451 and 4461 Integrated Services Routers was increased from 1500 to 2000 |
| Version 12.6 | Cisco IOS XE Gibraltar 16.11.1a | Simple Network Management Protocol (SNMP) Support for Unified SRST Toll Fraud Prevention for SIP Line Side on Unified SRST Unified SRST, Unified E-SRST, and Unified Secure SRST Password Policy |
| Version 12.5 | Cisco IOS XE Gibraltar 16.10.1a | Support for Unified SRST on Cisco 4461 Integrated Services Routers |
| Version 12.3 | Cisco IOS XE Fuji 16.9.1 | Secure SCCP SRST on Cisco 4000 Series Integrated Services Router |
| Version 12.2 | Cisco IOS XE Fuji 16.8.1 | Unified E-SRST with Support for Voice Hunt Group |
| Version 12.1 | Cisco IOS XE Fuji 16.7.1 | Licensing Secure SCCP SRST on Cisco 4000 Series Integrated Services Router Unified SRST and Unified Border Element Co-location |
| Version 12.0 | Cisco IOS XE Everest 16.6.1 | IPv6 Support for Unified SRST SIP IP Phones |
| Version 11.0 | 15.6(1)T | Support for Cisco IP Phone 7811 Support for Cisco IP Phones 8811, 8831, 8841, 8845, 8865, 8851, 8851NR, 8861 Support for Cisco ATA-190 Phones |
| Version 10.5 | 15.4(3)M |  |
| Version 10.0 | 15.3(3)M | Cisco Jabber for Windows SIP: Configure Unified E-SRST |
| Version 9.5 | 15.3(2)T |  |
| Version 9.1 | 15.2(4)M | KEM Support for Cisco Unified SIP IP Phones Enhancement in Speed-Dial Support Voice Hunt Group Support |
| Version 9.0 | 15.2(2)T |  |
| Version 8.8 | 15.2(1)T | Support for Cisco Unified 6945, 8941, and 8945 SCCP IP Phones |
| Version 8.6 | 15.1(4)M | Support for Cisco Unified 8941 and 8945 SCCP IP Phones were introduced. For more information, see Configuring Cisco Unified 8941 and 8945 SCCP IP Phones . |
| Version 8.0 | 15.1(1)T | Beginning with Cisco IP Phone firmware 8.5(3) and Cisco IOS Release 15.1(1)T, Cisco SRST supports SIP signaling over UDP,
                                       TCP, and TLS connections, providing both RTP and SRTP media connections based on the security settings of the IP phone. For
                                       more information, see the following sections: Signaling Security on Unified SRST - TLS Media Security on Unified SRST - SRTP Configuring Secure SIP Call Signaling and SRTP Media with Cisco SRST |
| Version 7.0/4.3 | See Cisco Feature Navigator for compatibility. | Configuring Eight Calls per Button (Octo-Line) Configuring Consultative Transfer |
| Version 4.2(1) | See Cisco Feature Navigator for compatibility. | Enhanced 911 Services . The following new features are included: Assigning ERLs to zones to enable routing to the PSAP that is closest to the caller. Customizing E911 by defining a default ELIN, identifying a designated number if the 911 caller cannot be reached on callback,
                                             specifying the expiry time for data in the Last Caller table, and enabling syslog messages that announce all emergency calls. Expanding the E911 location information to include name and address. Adding new permanent call detail records. |
| Version 4.1 | 12.4(15)T |  |
| Version 4.0 | 12.4(4)XC |  |
| Version 3.4 | 12.4(4)T | Cisco SIP SRST 3.4 Configuring Cisco Unified SIP SRST Features Using Redirect Mode Configuring Call Handling (see Back-to-Back User Agent Mode) |
| Version 3.3 |  | Secure SRST Cisco Unified IP Phone 7970G and Cisco Unified 7971G-GE Support Enhancement to the show ephone Command |
| Version 3.2 | 12.3(11)T |  |
| Version 3.1 | 12.3(7)T | Cisco Unified IP Phone 7920 Support Cisco Unified IP Phone 7936 Support |
| Version 3.0 | 12.2(15)ZJ 12.3(4)T |  |
| Version 2.1 |  |  |
| Version 2.02 |  | Cisco Unified IP Phone Conference Station 7935 Support Increase in Directory Numbers Cisco Unity Voicemail Integration Using In-Band DTMF Signaling Across the PSTN and BRI/PRI Cisco Unified SRST was implemented on the Cisco Catalyst 4500 access gateway module and Cisco 7200 routers (NPE-225, NPE-300,
                                             and NPE400). Support was removed for the Cisco MC3810-V3 concentrator. |
| Version 2.01 |  | Cisco Unified SRST was implemented on the Cisco 1760 routers, and support for the Cisco 1750 was removed. Support was added for additional connected Cisco IP phones. Support was added for additional directory numbers or virtual voice ports on Cisco IP phones. |
| Version 2.0 |  | Cisco Unified SRST was implemented on the Cisco 2600XM and Cisco 2691 routers. Cisco Unified SRST was integrated into Cisco IOS Release 12.2(8)T and implemented on the Cisco 3725 and Cisco 3745 routers
                                             and the Cisco MC3810-V3 concentrators. Cisco Unified SRST was implemented on the Cisco 1750 and Cisco 1751 routers. Huntstop support. Class of restriction (COR). Translation rule support. MOH and tone on hold. Distinctive ringing. Forward to a central voicemail or auto-attendant (AA) through PSTN during Cisco Unified Communications Manager fallback. Phone number alias support during Cisco Unified Communications Manager fallback: enhanced default destination support. List-based call restrictions for Cisco Unified Communications Manager fallback. |
| Version 1.0 |  | Support was added for 144 Cisco IP phones on the Cisco 3660 multiservice routers. Cisco Unified SRST introduced on the Cisco 2600 series and Cisco 3600 series multiservice routers and the Cisco IAD2420 series
                                             integrated access devices. Cisco IP phones able to establish a connection with an SRST router in the event of a WAN link to Cisco Unified Communications
                                             Manager failure. Dimming of all Cisco Unified IP Phone function keys that are not supported during Cisco Unified SRST operation. Extension-to-extension dialing. Direct Inward Dialing (DID). Direct Outward Dialing (DOD). Calling party ID (Caller ID/ANI) display. Last number redial. Preservation of local extension-to-extension calls when WAN link fails. Preservation of local extension to PSTN calls when WAN link fails. Preservation of calls in progress when failed WAN link is re-established. Blind transfer of calls within IP network. Multiple lines per Cisco IP phone. Multiple-line appearance across telephones. Call hold (shared lines). Analog Foreign Exchange Station (FXS) and Foreign Exchange Office (FXO) ports. BRI support for EuroISDN. PRI support for NET5 switch type. |

| Note | The smart licensing functionality remains unchanged. For ongoing requirements and continued support, purchase Collaboration
                                                      Flex subscription. |
|---|---|

| Note | Only SCCP Analog Voice Gateways support TLS version 1.3. The SCCP IP phone endpoints do not support TLS version 1.3. |
|---|---|

| Note | The maximum length of a regular expression pattern is 32 for both Cisco Unified SIP and Cisco Unified SCCP IP phones. |
|---|---|

| Note | There is no change in the number of afterhours patterns that can be added. The maximum number is still 100. |
|---|---|

| Note | Use quotes (") when input strings have spaces in between as shown in the next three examples. |
|---|---|

| Commands | Cisco Unified SRST |
|---|---|
| transfer-pattern | call-manager-fallback |
| transfer max-length | voice register pool |
| transfer-pattern blocked | voice register pool |
| conference transfer-pattern | call-manager-fallback |
| conference max-length | voice register pool or voice register template |
| conference-pattern blocked | voice register pool or voice register template |

| Note | The call transfer and conference restrictions apply when transfers or conferences are initiated toward external parties, like
                                             a PSTN trunk, a SIP trunk, or an H.323 trunk. The restrictions do not apply to transfers and conferences to local extensions. |
|---|---|

| Note | The blind keyword in the transfer-pattern command applies only to Cisco Unified SCCP IP phones and does not apply to Cisco Unified SIP IP phones. |
|---|---|

| Note | If only transfer max length is configured and conference max-length is not configured, then transfer max length takes effect for transfers and conferences. |
|---|---|

| Configuration | Cisco Unified SCCP IP Phones | Cisco Unified SIP IP Phones |
|---|---|---|
| No transfer patterns are configured. | Blocks all nonlocal Call Transfers. | Allows all nonlocal Call Transfers for backward compatibility. |
| Specific transfer patterns are configured. | Allows Call Transfers to specific external entities. | Allows Call Transfers to specific external entities. |
| The transfer-pattern blocked command is configured. | Blocks all nonlocal Call Transfers are blocked. Note The configuration reverts to the default, where no transfer patterns are configured. | Note | The configuration reverts to the default, where no transfer patterns are configured. | All nonlocal Call Transfers are blocked. Note The configuration unconditionally blocks all nonlocal Call Transfers. It does not return to the default, where all nonlocal
                                                      Call Transfers are allowed. | Note | The configuration unconditionally blocks all nonlocal Call Transfers. It does not return to the default, where all nonlocal
                                                      Call Transfers are allowed. |
| Note | The configuration reverts to the default, where no transfer patterns are configured. |
| Note | The configuration unconditionally blocks all nonlocal Call Transfers. It does not return to the default, where all nonlocal
                                                      Call Transfers are allowed. |

| Note | The configuration reverts to the default, where no transfer patterns are configured. |
|---|---|

| Note | The configuration unconditionally blocks all nonlocal Call Transfers. It does not return to the default, where all nonlocal
                                                      Call Transfers are allowed. |
|---|---|

|  | Conference max-length | No conference max-length |
|---|---|---|
| No conference-pattern blocked (default case) | Allowing/Blocking of conference call depends on configured conference max-length. | Allowing/Blocking of conference call depends on configured transfer max-length. |
| Conference-pattern blocked | Conference calls are not allowed on SIP and SCCP phones. |

|  | Max-length <= allowed max-length | Max-length > allowed max-length |
|---|---|---|
|  | Transfer | Conference | Transfer | Conference |
| Transfer max-length + No Conference max-length (use transfer max-length for conference cases too, as conference max-length not configured) | Y | Y | N | N |
| No transfer max-length + Conference max-length (conference max-length has precedence over transfer max-length for conference) | Y | Y | Y | N |
| No transfer max-length + Conference max-length (conference max-length has precedence over transfer max-length for conference) | Y | Y | N | N |
| No transfer max-length + No conference max-length | All transfer and conference calls are allowed. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register pool pool-tag OR ephone phone-tag Example: Router(config)# voice register pool 25 | Enters voice register Pool configuration mode and creates a Pool configuration for a Cisco Unified SIP IP phone in Cisco Unified
                                             Communications Manager Express or for a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST. pool-tag : Unique number assigned to the Pool. Range is 1–100. OR Enters voice register template configuration mode and defines a template of common parameters for Cisco Unified SIP IP phones. template-tag : Declares a template tag. Range is 1–10. OR Enters ephone configuration mode. phone-tag : Unique sequence number that identifies this ephone during configuration tasks. The maximum number of ephones is version
                                                   and platform-specific. Type? To display range. |
| Step 4 | conference max-length value Example: Router(config-telephony)# conference
max-lenght 6 | Allows the conference of calls from Cisco IP phones to specified directory numbers of phones other than Cisco IP phones. conference max-length Allows conference call depending on the configured conference max-length. Range is 3–16. |
| Step 5 | end Example: Router(config-telephony)# end | Exits telephony-service configuration mode and enter privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register pool pool-tag OR ephone phone-tag Example: Router(config)# voice register pool 25 | Enters voice register Pool configuration mode and creates a Pool configuration for a Cisco Unified SIP IP phone in Cisco Unified
                                             Communications Manager Express or for a set of Cisco Unified SIP IP phones in Cisco Unified SIP SRST. pool-tag : Unique number assigned to the Pool. Range is 1–100. OR Enters voice register template configuration mode and defines a template of common parameters for Cisco Unified SIP IP phones. template-tag : Declares a template tag. Range is 1–10. OR Enters ephone configuration mode. phone-tag : Unique sequence number that identifies this ephone during configuration tasks. The maximum number of ephones is version
                                                   and platform-specific. Type? To display range. |
| Step 4 | conference-pattern blocked Example: Router(config-telephony)# conference-pattern
blocked | Allows the conference of calls from Cisco IP phones to specified directory numbers of phones other than Cisco IP phones. conference-pattern blocked No conference calls are allowed. |
| Step 5 | exit Example: Router(config-telephony)# exit | Exits telephony-service configuration mode and enter global configuration mode. |

| Configuration | Cisco Unified SCCP IP Phones | Cisco Unified SIP IP Phones |
|---|---|---|
| No transfer patterns are configured. | Blocks all nonlocal Call Transfers. | Allows all nonlocal Call Transfers for backward compatibility. |
| Specific transfer patterns are configured. | Allows Call Transfers to specific external entities. | Allows Call Transfers to specific external entities. |
| The transfer-pattern blocked command is configured. | Blocks all nonlocal Call Transfers are blocked. Note The configuration reverts to the default, where no transfer patterns are configured. | Note | The configuration reverts to the default, where no transfer patterns are configured. | All nonlocal Call Transfers are blocked. Note The configuration unconditionally blocks all nonlocal Call Transfers. It does not return to the default, where all nonlocal
                                                      Call Transfers are allowed. | Note | The configuration unconditionally blocks all nonlocal Call Transfers. It does not return to the default, where all nonlocal
                                                      Call Transfers are allowed. |
| Note | The configuration reverts to the default, where no transfer patterns are configured. |
| Note | The configuration unconditionally blocks all nonlocal Call Transfers. It does not return to the default, where all nonlocal
                                                      Call Transfers are allowed. |

| Note | The configuration reverts to the default, where no transfer patterns are configured. |
|---|---|

| Note | The configuration unconditionally blocks all nonlocal Call Transfers. It does not return to the default, where all nonlocal
                                                      Call Transfers are allowed. |
|---|---|

| Note | If you have older routers, such as the VG26nn and VG37nn platforms and Cisco Integrated Services Router (ISR) Generation 1
                                          platforms (Cisco ISR 1861, 2800, and 3800 Series), you must upgrade to Cisco ISR 881, 886VA, 887VA, 888, 888E, 1861E, 2900,
                                          3900, and 3900E Series platforms to utilize these new features. |
|---|---|

| Note | For ATAs that are registered to a Cisco Unified SRST system to participate in FAX calls, they must have their ConnectMode
                                          parameter set to use the “standard payload type 0/8” as the RTP payload type in FAX pass-through mode. For ATAs used with
                                          Cisco Unified SRST 4.0 and higher versions, this is done by setting bit 2 of the ConnectMode parameter to 1 on the ATA. For
                                          more information, see the “Parameters and Defaults” chapter in Cisco ATA 186 and Cisco ATA 188 Analog Telephone Adaptor Administrator's Guide for SCCP . |
|---|---|

| Note | The Cisco Unified IP Phone 7914 Expansion Module can attach to your Cisco Unified IP Phones 7970G and 7971G-GE. See the Cisco Unified IP Phone Expansion Module 7914 Support section for more information. |
|---|---|

| Note | For information about Cisco Unified IP phones, see the Cisco Unified IP Phone 7900 Series documentation. |
|---|---|

| Note | This feature is available only for Cisco Unified SRST running under Cisco Unified Communications Manager V3.2. |
|---|---|

| Note | All voice gateway routers in the VoIP network must support H.450. For H.450 support, routers with Cisco Unified SRST must
                                          run either Cisco Unified SRST V3.0 and higher versions or Cisco IOS Release 12.2(15)ZJ and later releases. Routers without
                                          Cisco Unified SRST must run either Cisco Unified SRST V2.1 and higher versions or Cisco IOS Release 12.2(11)YT and later releases.
                                          SIP phones do not support this feature. |
|---|---|

| Note | For information about Cisco Unified IP phones, see the Cisco Unified IP Phone 7900 Series documentation. |
|---|---|

| Note | This feature is available only in Cisco Unified SRST running under Cisco Unified Communications Manager V3.2. |
|---|---|

| Cisco Router | Maximum Phones | Increase in Maximum Directory Number |
|---|---|---|
| From | To |
| Cisco 1751 | 24 | 96 | 120 |
| Cisco 1760 | 24 | 96 | 120 |
| Cisco 2600XM | 24 | 96 | 120 |
| Cisco 2691 | 72 | 216 | 288 |
| Cisco 3640 | 72 | 216 | 288 |
| Cisco 3660 | 240 | 720 | 960 |
| Cisco 3725 | 144 | 432 | 576 |
| Cisco 3745 | 240 | 720 | 960 |