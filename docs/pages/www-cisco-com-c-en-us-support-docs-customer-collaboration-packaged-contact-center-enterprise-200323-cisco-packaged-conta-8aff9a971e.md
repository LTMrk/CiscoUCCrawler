---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-packaged-contact-center-enterprise-200323-cisco-packaged-conta-8aff9a971e
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/packaged-contact-center-enterprise/200323-Cisco-Packaged-Contact-Center-Enterprise.html
retrieved_at: 2026-08-16T19:22:15.761680+00:00
---

Configure PCCE Outbound Option - Disable Ringback When Transferred to Agent for SIP

# Configure PCCE Outbound Option - Disable Ringback When Transferred to Agent for SIP

Updated: May 30, 2017

Document ID: 200323

Contents

## Contents

## Introduction

The document describes a solution to a problem found when the same gateway is used for Public Switched Telephone Network (PSTN) and Outbound Dialer. This document is complementary to the Package Contact Center Enterprise (PCCE)  features guide, release 11.0(1) outbound option section.

Contributed by Ramiro Amaya and Mayur Vyas, Cisco TAC Engineers

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Unified Contact Center Enterprise (UCCE)

- PCCE

- Outbound Dialer

- Cisco Unified Communications Manager ( CUCM)

- Cisco IOS ® Voice Gateways (GW)

### Components Used

The information in this document is based on these software and hardware versions:

- CUCM Version 11

- Cisco IOS Voice Gateway: c2800nm-adventerprisek9_ivs-mz.151-2.T5

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

The voice gateway generates a ringback tone to the customer in specific call flows when the call is sent to the agent. In outbound dialer, this is something customers does not want end user to know that this is outbound call and they are being transferred

For dialer call flows, in order to prevent the generation of a ringback from gateway, Session Initiation Protocol (SIP) normalization script to the Unified Communications Manager SIP trunk.

In the scenario where the same gateway is used for outbound dialer and PSTN calls, the trunk for PSTN calls still needs a 180 RINGING SIP message for inbound calls in order to trigger the gateway to play ringback to the PSTN, but needs to be disabled for outbound dialer calls.

Here is an example of the two scenarios described:

Image 1. PSTN Calls

Image 2. Dialer Calls

## Configure

Since the SIP normalization script will be applied only to the Gateway trunk used for dialer calls, and the same gateway is used for Dialer and PSTN calls, an additional Gateway trunks needs to be created in CUCM. However, in CUCM you cannot add the same trunk twice unless the trunk uses a different incoming port. So in this scenario, the gateway trunk used for Dialer will have a different incoming port from the Gateway trunk used for the PSTN calls. It will be the same gateway, but with different incoming ports.

### CUCM

Step 1. Navigate to https:// <IP_address> :8443 where <IP_address> identifies the CUCM.

Step 2. Sign in to CUCM.

Step 3. In order to create a SIP trunk security profile in CUCM, choose Communications Manager GUI > System > Security > SIP Trunk Security Profile > [Add New] . The default port is 5060. Change the default port to 5065 or any SIP port available for the gateway and CUCM.

Image 3. SIP Security Profile

Step 4. Click Save .

Step 5. Create a new SIP trunk and add the new SIP Trunk Security Profile.

Image 4. Create a New SIP Trunk

Step 6. Click Save .

Step 7. Click Reset .

Step 8. In Communications Manager GUI > Devices > Device Settings > SIP Normalization Scripts > [Create New] , enter this SIP normalization script into the content field. All other values remain set to default.

M = {}

function M.outbound_180_INVITE(msg)

msg:setResponseCode(183, "Session in Progress")

end

return M

Image 5. Add Normalization Script

Step 9. Click Save .

Step 10. Associate the new normalization script with the SIP trunk.

Image 6. Associate Script with Trunk

### Voice Gateways

In addition to the gateway configuration described on the Cisco Packaged Contact Center Enterprise Features Guide, Release 11.0 , configure an outgoing Dial-peer for transferring call to the agent with the incoming port set on the CUCM SIP Trunk Security Profile (the port 5065 was used in the previous example).

Configure an Outgoing Dial-Peer to Transfer a Call to an Agent

This example shows this configuration in th gateway:

```
dial-peer voice 11000 voip
 destination-pattern 11T
 session protocol sipv2
 session target ipv4: 10.10.10.31:5065 (this is Call Manager's IP address and Security profile incoming port)
 voice-class codec 1
 voice-class sip rel1xx supported "100rel"
 dtmf-relay rtp-nte h245-signal h245-alphanumeric
 no vad
```

## Verify and Troubleshoot

When the dailer leg connects on the PSTN Integrated Services Digital Network ( ISDN) side, UCCE initiates a REFER transfer to the agent. In this case, the GW sends  an INVITE to the User Agent (UA) where the agent resides.  In the case of CUCM, the gateway receives back a 180 ringing on the transfer leg.  When gateway receive this, it  triggers the GW to play ringback out to the ISDN Primary Rate Interface (PRI) where the caller just answered  the call.  The end result is a caller answers and hears ringback.

Call connected

```
Dec  1 07:44:25.204 CST: ISDN Se0/0/1:23 Q931: RX <- CONNECT pd = 8  callref = 0xDCEF

Dec  1 07:44:25.206 CST: %ISDN-6-CONNECT: Interface Serial0/0/1:0 is now connected to 13098313400 N/A

Dec  1 07:44:25.206 CST: ISDN Se0/0/1:23 Q931: TX -> CONNECT_ACK pd = 8  callref = 0x5CEF

Dec  1 07:44:25.206 CST: //4767881/685BD1A2987C/CCAPI/cc_api_call_connected:  Interface=0x23E58B38, Data Bitmask=0x1, Progress Indication=NULL(0),  Connection Handle=0
```

Received REFER from Dialer

```
Dec  1 07:44:26.736 CST: //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:

Received:

REFER sip:001913098313400@10.185.3.134:5060 SIP/2.0

Via: SIP/2.0/UDP

192.168.237.130:58810;branch=z9hG4bK-d8754z-890f5b5e0352e84d-1---d8754z-;rport

Max-Forwards: 70

Contact: <sip:8805550@192.168.237.130:58810>

To: <sip:001913098313400@10.185.3.133>;tag=65A63E8C-1E9F

From: <sip:8805550@192.168.237.130>;tag=be521e41

Call-ID: b9312276-8412f240-434b1f08-a869d275

CSeq: 4 REFER

User-Agent: Cisco-SIPDialer/UCCE8.0

Refer-To: <sip:8814997@10.185.3.133>

Referred-By: <sip:8805550@192.168.237.130>

Content-Length: 0
```

After the Invite is sent to CUCM, CUCM sends 100 trying, 180 ringing to gateway.

```
Dec  1 07:44:26.926 CST: //4767885/685BD1A2987C/SIP/Msg/ccsipDisplayMsg:

Received:

SIP/2.0 180 Ringing

Via: SIP/2.0/UDP 10.185.3.134:5060;branch=z9hG4bK96E46B38

To: <sip:8814997@10.185.3.133>;tag=d2999f32-ed69-4535-a8bf-99298e16c176-97460839

From: <sip:13098313400@10.185.3.134>;tag=65A65296-507

Contact: <sip:8814997@10.184.60.3:5060>

Remote-Party-ID: "Wylie Test Agent"

<sip:8814997@10.184.60.3>;party=called;screen=yes;privacy=off

Call-ID: 6B7F9249-1B5911E1-9884C122-F70CF5@10.185.3.134

CSeq: 101 INVITE

Content-Length: 0

Date: Thu, 01 Dec 2011 13:44:26 GMT

Allow: INVITE, OPTIONS, INFO, BYE, CANCEL, ACK, PRACK, UPDATE, REFER,

SUBSCRIBE, NOTIFY

Allow-Events: presence

P-Asserted-Identity: "Wylie Test Agent" <sip:8814997@10.184.60.3>

Supported: X-cisco-srtp-fallback

Supported: Geolocation
```

Gateway plays ringback to PRI leg from the DSP.

```
Dec  1 07:44:26.926 CST: //4767885/685BD1A2987C/CCAPI/cc_api_call_alert:

  Interface=0x22667AD4, Progress Indication=NULL(0), Signal Indication=SIGNAL 

RINGBACK(1)

Dec  1 07:44:26.926 CST: //4767885/685BD1A2987C/CCAPI/cc_api_call_alert:

  Call Entry(Retry Count=0, Responsed=TRUE)

Dec  1 07:44:26.926 CST: //4767881/685BD1A2987C/CCAPI/ccGenerateToneInfo:

  Stop Tone On Digit=FALSE, Tone=Ring Back,

  Tone Direction=Network, Params=0x0, Call Id=4767881
```

After the SIP Trunk is configured as described in the Configure section, CUCM will send 183 session progress instead of 180 ringing for Outbound dialer call and this stops the gateway to generate ringback on ISDN PRI  leg.

### Revision History

1.0

21-Apr-2016

Initial Release

### Contributed by Cisco Engineers

Ramiro Amaya

Cisco TAC Engineer

Mayur Vyas

Cisco TAC Engineer

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 21-Apr-2016 | Initial Release |