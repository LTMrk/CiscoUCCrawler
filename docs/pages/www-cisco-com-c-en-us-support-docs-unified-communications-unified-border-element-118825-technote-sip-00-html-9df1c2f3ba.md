---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-border-element-118825-technote-sip-00-html-9df1c2f3ba
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-border-element/118825-technote-sip-00.html
retrieved_at: 2026-08-16T15:56:40.689184+00:00
---

Use SIP Profiles on CUBE Enterprise Common Use Cases

# Use SIP Profiles on CUBE Enterprise Common Use Cases

### Download Options

Updated: September 5, 2024

Document ID: 118825

Contents

## Contents

## Introduction

This document describes how to use the Session Initiation Protocol (SIP) Profile Test Tool that is available for use on Cisco.com.

## Prerequisites

### Requirements

The information in this document is based on ISR platforms running Cisco IOS® and Cisco IOS® XE software.

### Components Used

Cisco recommends that you have knowledge of these topics:

- Navigation through Cisco IOS ®

- SIP message format and transactions

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

SIP Profiles are used in order to manipulate header information in the SIP messages. They can also be used to make changes in the Session Description Protocol (SDP), which is used to negotiate media.

## Common SIP Message Normalization Scenarios

This section provides several SIP message normalization scenarios that have been seen frequently. Each scenario includes the configuration required on Cisco IOS for your reference and a screenshot from the SIP Profile Test Tool that is mentioned in the Introduction.

These scenarios can be used as references for other manipulation required on the SIP messages.

### Copy Value from Diversion Header to the From Header

```
voice class sip-profiles 1 request INVITE sip-header Diversion copy "<sip:(.*)@.*" u01 request INVITE sip-header From copy ".*<sip:(.*)@.*" u02 request INVITE sip-header From modify "(.*)<sip:.*@(.*)" "\1<sip:\u01@\2" request INVITE sip-header From modify "<sip:@" "<sip:\u02@"
```

### Copy Number from To Header in an Incoming Invite to the REQ-URI Parameter (Prior to Cisco IOS Version 15.4)

Copy the number in the To header in an inbound Invite message and modify the outgoing INVITE:

```
voice class sip-copylist 1 sip-header TO voice class sip-profiles 2 request INVITE peer-header sip TO copy "sip:(.*)@" u01 request INVITE sip-header SIP-Req-URI modify ".*@(.*)" "INVITE sip:\u01@\1"
```

### Copy Number from To Header in an Incoming Invite to the REQ-URI Parameter (with Inbound SIP Profiles)

```
voice class sip-profiles 1 request INVITE sip-header TO copy "sip:(.*)@" u01 request INVITE sip-header SIP-Req-URI modify ".*@(.*)" "INVITE sip:\u01@\1" voice service voip sip sip-profiles inbound sip-profiles 1 inbound
```

### One-way / No-way Audio Interoperability Issues with Provider

```
voice class sip-profiles 200 request ANY sdp-header Audio-Attribute modify "a=inactive" "a=sendrecv" request ANY sdp-header Audio-Connection-Info modify "0.0.0.0" "CUBE’s IP"
```

### Remove the UPDATE Method Support to Avoid Interoperability Issues

```
voice class sip-profiles 200 request ANY sip-header Allow-Header modify ", UPDATE" ""
```

### IP Address to Domain Name Conversion

```
voice class sip-profiles 1 request ANY sip-header SIP-Req-URI modify "10.67.138.241:5060" "sipp.cisco.com"
```

### Add a Prefix in the Diversion Header

```
voice class sip-profiles 1 request ANY sip-header Diversion modify "sip:(.*)@" "sip:704264\1@"
```

### Set DID Number in Diversion Header

```
voice class sip-profiles 1 request INVITE sip-header Diversion modify "sip:(.*)@" "sip:7042642614@"
```

### Remove Diversion Header

```
voice class sip-profiles 1 request INVITE sip-header Diversion remove
```

### Copy Location Number for Caller ID in Local Gateway (Webex Calling Deployments in United States, Canada, and Puerto Rico)

```
voice service voip sip sip-profile inbound voice class sip-profiles 201 rule 1 request INVITE sip-header From copy "<sip:(.*)@" u01 rule 2 request INVITE sip-header P-Asserted-Identity modify "<sip:.*@(.*)>" "<sip:\u01@\1>" voice class tenant 200 sip-profiles 201 inbound
```

## Possible Issues

Here are some possible issues you can encounter.

- After Cisco IOS Version 15.4, the SIP profile feature is introduced to modify inbound SIP messages as well.

- Cisco IOS Versions 15.3 and earlier only support SIP profiles in the outbound direction.

## Related Information

In Depth Explanation of Cisco IOS and IOS-XE Call Routing

Understanding Inbound and Outbound Dial Peers Matching on IOS Platforms

### Revision History

3.0

05-Sep-2024

Formatting, headers, alt-text

2.0

09-May-2023

Updated Title, Introduction, Branding Requirements, Gerunds, Machine Translation, Style Requirements, Alt Text and Formatting.

1.0

23-Jul-2021

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 3.0 | 05-Sep-2024 | Formatting, headers, alt-text |
| 2.0 | 09-May-2023 | Updated Title, Introduction, Branding Requirements, Gerunds, Machine Translation, Style Requirements, Alt Text and Formatting. |
| 1.0 | 23-Jul-2021 | Initial Release |