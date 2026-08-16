---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-border-element-213843-troubleshoot-session-refresh-on--e2a6772de5
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-border-element/213843-troubleshoot-session-refresh-on-cube.html
retrieved_at: 2026-08-16T15:56:48.999305+00:00
---

Troubleshoot Session Refresh on CUBE

# Troubleshoot Session Refresh on CUBE

### Download Options

Updated: October 18, 2018

Document ID: 213843

Contents

## Contents

## Introduction

This document describes how to Troubleshoot Session Initiation Protocol (SIP) Session Refresh issues on Cisco Unified Border Element (CUBE).

Contributed by Andres Salgado, Technical Marketing Engineer CUBE.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CUBE

- TCP

- SIP

- UDP

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Overview on SIP Session Refresh

T he Session Initiation Protocol (SIP) Session Timer Support feature adds the capability to periodically refresh SIP sessions with repeated INVITE requests. The repeated INVITE requests, or Re-INVITEs, are sent on an active call leg to allow User Agents (UAs) or proxies to determine the status of a SIP session. Without this keepalive mechanism, proxies that remember incoming and outgoing requests (stateful proxies) can continue to retain the call state needlessly. If a UA fails to send a BYE message at the end of a session or if the BYE message is lost because of network problems, a stateful proxy does not know that the session has ended. The Re-INVITES ensure that active sessions stay active and completed sessions are terminated.

## Interoperability and Compatibility

### Interoperability

This feature provides a periodic refresh of SIP sessions. The periodic refresh allows user agents and proxies to monitor the status of a SIP session, in order to prevent hung network resources when network failures occur.

### Compatibility

Only one of the two user agent or proxy participants in a call needs to implemented the SIP Session Timer Support feature. This feature is easily compatible with older SIP networks. The SIP Session Timer Support feature also adds two new general headers that are used to negotiate the value of the refresh interval.

#### Role of User Agents

The initial INVITE request establishes the duration of the session and can include a Session-Expires header and a Min-SE header. These headers indicate the session timer value required by the User Agent Client (UAC). A receiving User Agent Server (UAS) or proxy can lower the session timer value, but not lower than the value of the Min-SE header. If the session timer duration is lower than the configured minimum, the proxy or UAS can also send out a 422 response message. If the UAS or proxy finds that the session timer value is acceptable, it copies the Session-Expires header into the 2 xx class response.

A UAS or proxy can insert a Session-Expires header in the INVITE if the UAC did not include one. Thus a UAC can receive a Session-Expires header in a response even if none was present in the request.

In the 2 xx response, therefresherparameter in the Session-Expires header indicates who performs the re-INVITES. For example, if the parameter contains the valueUAC, the UAC performs the refreshes. For compatibility issues, only one of the two user agents needs to support the session timer feature, and in that case, the UA that supports the feature performs the refreshes. The other UA interprets the refreshes as repetitive INVITEs and ignores them.

Re-INVITEs are processed identically to INVITE requests, but go out in predetermined session intervals. Re-INVITEs carry the new session expiration time. The UA responsible for re-INVITE requests sends a re-INVITE out before the session expires. If there is no response, the UA sends a BYE request to terminate the call before session expiration. If a re-INVITE is not sent before the session expiration, either the UAC or the UAS can send a BYE.

If the 2 xx response does not contain a Session-Expires header, there is no session expiration and re-INVITES do not need to be sent.

#### Session-Expires Header

The Session-Expires header conveys the session interval for a SIP call. It is placed in an INVITE request and is allowed in any 2 xx class response to an INVITE. Its presence indicates that the UAC wants to use the session timer for this call. Unlike the SIP-Expires header, it can contain only a delta-time, which is the current time, plus the session interval from the response.

For example, if a UAS generates a 200 OK response to a re-INVITE that contained a Session-Expires header with a value of 1800 seconds (30 minutes), the UAS computes the session expiration as 30 minutes after the time when the 200 OK response was sent. For each proxy, the session expiration is 30 minutes after the time when the 2xx was received or sent. For the UAC, the expiration time is 30 minutes after the receipt of the final response.

The recommended value for the Session-Expires header is 1800 seconds.

The syntax of the Session-Expires header is:

```
Session-Expires  =  ("Session-Expires" | "x" ) ":" delta-seconds
```

```
[refresher]
```

```
refresher        =  ";" "refresher" "=" "UAS"|"UAC"
```

Therefresherparameter is optional in the initial INVITE, although the UAC can set it toUACto indicate that it is the one to initiate Session Refresh. The 200 OK response must have the refresher parameter set.

#### Min-SE Header

Because of the processing load of INVITE requests you can configure a minimum timer value that the proxy, UAC, and UAS can accept. The proxy, UAC, and UAS. The min-se command sets the minimum timer, and it is conveyed in the Min-SE header in the initial INVITE request.

When a call is made, the presence of the Min-SE header informs the UAS and any proxies of the minimum value that the UAC accepts for the session timer duration, in seconds. The default value is 1800 seconds (30 minutes). It is recomended to not reduce the session timer below the value set, the UAS and proxies prevent the 422 error generation by UAC. Once set, the min-se command value affects all calls originated by the router. If the Min-SE header is not present, the UA accepts any value.

The syntax of the Min-SE header is:

```
Min-SE  =  "Min-SE" ":" delta-seconds
```

#### 422 Response Message

If the value of the Session-Expires header is too small, the UAS or proxy rejects the call with a 422 Session Timer Too Small response message. With the 422 response message, the proxy or UAS includes a Min-SE header which indicates the minimum session value it can accept. The UAC can then retry the call with a larger session timer value.

If a 422 response message is received after an INVITE request, the UAC can retry the INVITE.

#### Supported and Require Headers

The presence of the timer argument in the Supported header indicates that the UA supports the SIP session timer. The presence of the timer argument in the Require header indicates that the opposite UA must support the SIP session timer for the call to be successful.

- In the 2xx response, the refresherparameter in the Session-Expires header indicates who performs the Re-INVITES

- If the 2xx response does not contain a Session-Expires header, there is no session expiration and Re-INVITES do not need to be sent

- The refresher parameter is optional in the initial INVITE. The 200 OK response must have the refresher parameter set

- Min-SE header informs the UAS and any proxies of the minimum value that the UAC accepts for the session timer duration, in seconds. The default value is 1800 seconds (30 minutes)

## Example Call Flows

Inbound call from SIP provider, response is set to UAC, therefore 15 minutes after the 200 OK, UAC (SIP provider) sends a session refresh (Re-Invite);

Cisco Unified Communications Manager (CUCM) sends a session refresh after 86400 seconds;

Session expires CUCM sends default value is 1800 , but can be increased to a maximum of 86400.

## Avoid Interoperability Issues with Update Refresh

1. CUBE can disable update for session refresh with SIP profiles.

```
voice class sip-profiles 200 request ANY sip-header Allow-Header modify ", UPDATE" "“ Response ANY sip-header Allow-Header modify ", UPDATE" "“ Voice service voip sip sip-profiles 200
```

2. The session refresh command under SIP in voice service voip adds a session expires to the outbound INVITE if there wasn't a header present in the inbound leg.

3. Set session refresh to Invite instead of update, CUCM 10.x onwards.

Session Refresh method under SIP profile in CUCM.

### Consumption of Mid-Call RE-INVITE/UPDATE

Avoids un-necessary Re-Invites/UPDATE sent by the network and consumes them locally to avoid any inter-operatability issues. Session refresh is passed across only if there is a media change.

Midcall-reinvite Cosumption

CUBE consumes reinvite with midcall-signaling passthru media-change. CUBE handles each leg independently. After 15 minutes you see the session refresh.

Midcall-reinvite Cosumption example with Session Expires headers.

## Related Information

- Session Timers in SIP

- SIP RFC

- Technical Support & Documentation - Cisco Systems