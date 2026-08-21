---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-feature-guide-srst71ft-html-2d0230ae44
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/feature/guide/srst71ft.html
retrieved_at: 2026-08-21T21:29:58.170670+00:00
---

Cisco Unified SRST 7.1 New Features

# Cisco Unified SRST 7.1 New Features

### Download Options

Updated: July 12, 2010

## Table Of Contents

Cisco Unified Survivable Remote Site Telephony 7.1 New Features

Finding Feature Information

Contents

Prerequisites for Cisco Unified SRST 7.1

Information About Cisco Unified SRST 7.1

DSCP

Voice Translation Rules and Profiles

How to Configure Cisco Unified SRST 7.1 New Features

Configuring DSCP for Cisco Unified SRST

Prerequisites

Restrictions

Examples

Applying Voice Translation Rules in Cisco Unified SRST 7.1 and Later

Prerequisites

Additional References

Related Documents

Standards

MIBs

RFCs

Technical Assistance

Command Reference

Feature Information for Cisco Unified SRST 7.1

## Cisco Unified Survivable Remote Site Telephony 7.1 New Features

First Published: January 20, 2009

This document describes the following new features introduced in Cisco Unified Survivable Remote Site Telephony 7.1 (Cisco Unified SRST):

• Differentiated Services Code Point (DSCP)

• Translation profiles for SIP phones and directory numbers

## Finding Feature Information

Your software release may not support all the features documented in this module. For the latest feature information and caveats, see the release notes for your platform and software release. To find information about the features documented in this module, and to see a list of the releases in which each feature is supported, see the "Feature Information for Cisco Unified SRST 7.1" section .

Use Cisco Feature Navigator to find information about platform support and Cisco IOS, Catalyst OS, and Cisco IOS XE software image support. To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn . An account on Cisco.com is not required.

## Contents

• Prerequisites for Cisco Unified SRST 7.1

• Information About Cisco Unified SRST 7.1

• How to Configure Cisco Unified SRST 7.1 New Features

• Additional References

• Command Reference

• Feature Information for Cisco Unified SRST 7.1

## Prerequisites for Cisco Unified SRST 7.1

• Cisco Unified SRST 7.1

• Cisco IOS Release 12.4(22)YB

## Information About Cisco Unified SRST 7.1

To configure Cisco Unified SRST 7.1 features, you should understand the following concepts:

• DSCP

• Voice Translation Rules and Profiles

### DSCP

Differentiated Services Code Point (DSCP) packet marking is used to specify the class of service for each packet. Cisco Unified IP Phones get their DSCP information from the configuration file that is downloaded to the device.

In Cisco Unified SRST 7.1 and later versions, you can configure the DSCP value for media packets in the configuration file for SCCP phones. Because Cisco Unified IP Phones get their DSCP information from the configuration file that is downloaded to the device, the DSCP value for other types of traffic is set by Cisco Unified Communications Manager in the configuration file it downloads to the phone.

For configuration information, see the "Configuring DSCP for Cisco Unified SRST" section .

### Voice Translation Rules and Profiles

Voice translation rules perform manipulations on telephone numbers. Voice translation profiles allow you to group voice translation rules together and use them to manipulate the calling number (ANI), called number (DNIS), or redirected called number for a voice call.

Translation rules are defined by using the voice translation-rule command. After you define a set of translation rules and assign them to a translation profile using the voice translation-profile command, you can apply the rules to all inbound or outbound calls to and from a specific SIP phone, or to individual inbound or outbound call legs according to the directory number.

For configuration information, see the "Applying Voice Translation Rules in Cisco Unified SRST 7.1 and Later" section .

## How to Configure Cisco Unified SRST 7.1 New Features

This section contains the following tasks.

• Configuring DSCP for Cisco Unified SRST

• Applying Voice Translation Rules in Cisco Unified SRST 7.1 and Later

### Configuring DSCP for Cisco Unified SRST

To set the differentiated services code point (DSCP) levels for phones, perform the following steps.

### Prerequisites

• Cisco Unified SRST 7.1 or a later version.

### Restrictions

• Cisco Unified IP Phones get their DSCP information from the configuration file that is downloaded to the device. Because Cisco Unified SRST does not download configuration files to phones during fallback, only the DSCP value set for media packets takes effect, and only for SCCP phones.

• If DSCP is configured for the gateway interface using the service-policy command or for the dial peer using the ip qos dscp command, the value set with those commands takes precedence over the DSCP value configured with this procedure.

### SUMMARY STEPS

1. enable

2. configure terminal

3. call-manager-fallback

4. ip qos dscp {{ number | af | cs | default | ef } { media | service | signaling | video }}

5. end

### DETAILED STEPS

Command or Action

Purpose

Step 1

enable

Example:

Router> enable

Enables privileged EXEC mode.

• Enter your password if prompted.

Step 2

configure terminal

Example:

Router# configure terminal

Enters global configuration mode.

Step 3

call-manager-fallback

Example:

Router(config)# call-manager-fallback

Enters call-manager-fallback configuration mode.

Step 4

ip qos dscp {{ number | af | cs | default | ef } { media | service | signaling | video }}

Example:

Router(config-cm-fallback)# ip qos dscp af11 media

Sets the DSCP priority levels for different types of traffic.

Note Only the media keyword is supported by Cisco Unified SRST.

Step 5

end

Example:

Router(config-cm-fallback)# end

Returns to privileged EXEC mode.

### Examples

The following example shows the DSCP value for media is set to af11.

call-manager-fallback

ip source-address 10.10.10.1 port 2000

max-ephones 100

max-dn 240

ip qos dscp af11 media

.

.

### Applying Voice Translation Rules in Cisco Unified SRST 7.1 and Later

To apply a voice translation profile for incoming or outgoing call legs to a directory number on a SIP phone, perform the following steps.

### Prerequisites

• Cisco Unified SRST 7.1 or a later version.

• Voice translation profile containing voice translation rules must be configured. See the Configuring a Translation Rule section in the VoIP Gateway Trunk and Carrier Based Routing Enhancements document.

### SUMMARY STEPS

1. enable

2. configure terminal

3. voice register dn dn - tag or voice register pool phone - tag

4. translation-profile { incoming | outgoing } name

5. end

### DETAILED STEPS

Command or Action

Purpose

Step 1

enable

Example:

Router> enable

Enables privileged EXEC mode.

• Enter your password if prompted.

Step 2

configure terminal

Example:

Router# configure terminal

Enters global configuration mode.

Step 3

voice register dn dn-tag

or

voice register pool phone-tag

Example:

Router(config)# voice register dn 1

or

Router(config)# voice register pool 10

Enters voice register dn configuration mode to define a directory number for a SIP phone.

Step 4

translation-profile { incoming | outgoing } name

Example:

Router(config-register-dn)# translation-profile incoming name1

or

Router(config-register-pool)# translation-profile incoming name1

Assigns a translation profile to incoming or outgoing call legs to this directory number or phone.

Step 5

```
end
```

Example:

Router(config-register-dn)# end

or

Router(config-register-pool)# end

Exits to privileged EXEC mode.

## Additional References

The following sections provide references related to Cisco Unified SRST.

### Related Documents

Related Topic

Document Title

Cisco Unified SRST configuration

• Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions)

• Cisco Unified SRST and SIP SRST Command Reference

Cisco IOS voice configuration

• Cisco IOS Voice Configuration Library

• Cisco IOS Voice Command Reference

### Standards

Standard

Title

No new or modified standards are supported by this feature, and support for existing standards has not been modified by this feature.

—

### MIBs

MIB

MIBs Link

No new or modified MIBs are supported by this feature, and support for existing MIBs has not been modified by this feature.

To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco MIB Locator found at the following URL:

http://www.cisco.com/go/mibs

### RFCs

RFC

Title

No new or modified RFCs are supported by this feature, and support for existing RFCs has not been modified by this feature.

—

### Technical Assistance

Description

Link

The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving technical issues with Cisco products and technologies.

To receive security and technical information about your products, you can subscribe to various services, such as the Product Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds.

Access to most tools on the Cisco Support website requires a Cisco.com user ID and password.

http://www.cisco.com/techsupport

## Command Reference

The following commands are introduced or modified in the features documented in this module. For information about these commands, see the Cisco Unified SRST and SIP SRST Command Reference at http://www.cisco.com/en/US/docs/voice_ip_comm/cusrst/command/reference/srstcr.html .

For information about all Cisco IOS commands, use the Command Lookup Tool at http://tools.cisco.com/Support/CLILookup or the Cisco IOS Master Command List, All Releases , at http://www.cisco.com/en/US/docs/ios/mcl/allreleasemcl/all_book.html .

• ip qos dscp (call-manager-fallback)

• translation-profile (voice register)

## Feature Information for Cisco Unified SRST 7.1

Table 1 lists the release history for this feature.

Not all commands may be available in your Cisco IOS software release. For release information about a specific command, see the command reference documentation.

Use Cisco Feature Navigator to find information about platform support and software image support. Cisco Feature Navigator enables you to determine which Cisco IOS software images support a specific software release, feature set, or platform. To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn . An account on Cisco.com is not required.

Note Table 1 lists only the Cisco IOS software release that introduced support for a given feature in a given Cisco IOS software release train. Unless noted otherwise, subsequent releases of that Cisco IOS software release train also support that feature.

Table 1 Feature Information for Cisco Unified SRST 7.1

Feature Name

Releases

Feature Information

Cisco Unified SRST 7.1

12.4(22)YB

• Adds DSCP packet marking for specifying the class of service for each packet.

• Adds translation profiles at the directory number and phone level.

### Cisco and the Cisco Logo are trademarks of Cisco Systems, Inc. and/or its affiliates in the U.S. and other countries. A listing of Cisco's trademarks can be found at www.cisco.com/go/trademarks . Third party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1005R)

### Any Internet Protocol (IP) addresses used in this document are not intended to be actual addresses. Any examples, command display output, and figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses in illustrative content is unintentional and coincidental. © 2009 Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- Unified Survivable Remote Site Telephony

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. • Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 4 | ip qos dscp {{ number \| af \| cs \| default \| ef } { media \| service \| signaling \| video }} Example: Router(config-cm-fallback)# ip qos dscp af11 media | Sets the DSCP priority levels for different types of traffic. Note Only the media keyword is supported by Cisco Unified SRST. |
| Step 5 | end Example: Router(config-cm-fallback)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. • Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register dn dn-tag or voice register pool phone-tag Example: Router(config)# voice register dn 1 or Router(config)# voice register pool 10 | Enters voice register dn configuration mode to define a directory number for a SIP phone. |
| Step 4 | translation-profile { incoming \| outgoing } name Example: Router(config-register-dn)# translation-profile incoming name1 or Router(config-register-pool)# translation-profile incoming name1 | Assigns a translation profile to incoming or outgoing call legs to this directory number or phone. |
| Step 5 | end Example: Router(config-register-dn)# end or Router(config-register-pool)# end | Exits to privileged EXEC mode. |

| Related Topic | Document Title |
|---|---|
| Cisco Unified SRST configuration | • Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) • Cisco Unified SRST and SIP SRST Command Reference |
| Cisco IOS voice configuration | • Cisco IOS Voice Configuration Library • Cisco IOS Voice Command Reference |

| Standard | Title |
|---|---|
| No new or modified standards are supported by this feature, and support for existing standards has not been modified by this feature. | — |

| MIB | MIBs Link |
|---|---|
| No new or modified MIBs are supported by this feature, and support for existing MIBs has not been modified by this feature. | To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco MIB Locator found at the following URL: http://www.cisco.com/go/mibs |

| RFC | Title |
|---|---|
| No new or modified RFCs are supported by this feature, and support for existing RFCs has not been modified by this feature. | — |

| Description | Link |
|---|---|
| The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving technical issues with Cisco products and technologies. To receive security and technical information about your products, you can subscribe to various services, such as the Product Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds. Access to most tools on the Cisco Support website requires a Cisco.com user ID and password. | http://www.cisco.com/techsupport |

| Feature Name | Releases | Feature Information |
|---|---|---|
| Cisco Unified SRST 7.1 | 12.4(22)YB | • Adds DSCP packet marking for specifying the class of service for each packet. • Adds translation profiles at the directory number and phone level. |