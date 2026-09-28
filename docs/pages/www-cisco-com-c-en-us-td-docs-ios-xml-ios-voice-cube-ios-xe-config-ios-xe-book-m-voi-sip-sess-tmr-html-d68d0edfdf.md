---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-sip-sess-tmr-html-d68d0edfdf
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-sip-sess-tmr.html
retrieved_at: 2026-08-16T15:46:49.721673+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: SIP  Session Timer Support

## Chapter: SIP  Session Timer Support

# SIP  Session Timer Support

The SIP Session Timer Support feature adds the capability to periodically refresh Session Initiation Protocol (SIP) sessions
                        by sending repeated INVITE requests. The repeated INVITE requests, or re-INVITEs, are sent during an active call leg to allow
                        user agents (UAs) or proxies to determine the status of a SIP session. Without this keepalive mechanism, proxies that remember
                        incoming and outgoing requests (stateful proxies) may continue to retain the call state needlessly. If a UA fails to send
                        a BYE message at the end of a session or if the BYE message is lost because of network problems, a stateful proxy does not
                        know that the session has ended. The re-INVITES ensure that active sessions stay active and completed sessions are terminated.

## Feature Information for SIP Session Timer Support

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

SIP - Session Timer Support

Baseline Functionality

The SIP Session Timer Support feature adds the capability to periodically refresh Session Initiation Protocol (SIP) sessions
                                       by sending repeated INVITE requests. The repeated INVITE requests, or re-INVITEs, are sent during an active call leg to allow
                                       user agents (UAs) or proxies to determine the status of a SIP session.

The following commands were introduced or modified: min-se (SIP) and show sip-ua min-se

## Information About SIP  Session Timer Support

To configure the Session Timer feature, you should understand the following concepts:

### Interoperability and Compatibility

Interoperability--This feature provides a periodic refresh of SIP sessions. The periodic refresh allows user agents and proxies
                                    to monitor the status of a SIP session, preventing hung network resources from pausing indefinitely when network failures
                                    occur.

Compatibility--Only one of the two user agent or proxy participants in a call needs to implemented the SIP Session Timer Support
                                    feature. This feature is easily compatible with older SIP networks. The SIP Session Timer Support feature also adds two new
                                    general headers that are used to negotiate the value of the refresh interval.

### Role of the User Agents

The initial INVITE request establishes the duration of the session and may include a Session-Expires header and a Min-SE header.
                              These headers indicate the session timer value required by the user agent client (UAC). A receiving user agent server (UAS)
                              or proxy can lower the session timer value, but not lower than the value of the Min-SE header. If the session timer duration
                              is lower than the configured minimum, the proxy or UAS can also send out a 422 response message. If the UAS or proxy finds
                              that the session timer value is acceptable, it copies the Session-Expires header into the 2 xx class response.

A UAS or proxy can insert a Session-Expires header in the INVITE if the UAC did not include one. Thus a UAC can receive a
                              Session-Expires header in a response even if none was present in the request.

In the 2 xx response, the refresher parameter in the Session-Expires header indicates who performs the re-INVITES. For example, if the parameter contains the
                              value UAC , the UAC performs the refreshes. For compatibility issues, only one of the two user agents needs to support the session timer
                              feature, and in that case, the UA that supports the feature performs the refreshes. The other UA interprets the refreshes
                              as repetitive INVITEs and ignores them.

Re-INVITEs are processed identically to INVITE requests, but go out in predetermined session intervals. Re-INVITEs carry the
                              new session expiration time. The UA responsible for generating re-INVITE requests sends a re-INVITE out before the session
                              expires. If there is no response, the UA sends a BYE request to terminate the call before session expiration. If a re-INVITE
                              is not sent before the session expiration, either the UAC or the UAS can send a BYE.

If the 2 xx response does not contain a Session-Expires header, there is no session expiration and re-INVITES do not need to be sent.

### Session-Expires Header

The Session-Expires header conveys the session interval for a SIP call. It is placed in an INVITE request and is allowed in
                              any 2 xx class response to an INVITE. Its presence indicates that the UAC wants to use the session timer for this call. Unlike the
                              SIP-Expires header, it can contain only a delta-time, which is the current time, plus the session interval from the response.

For example, if a UAS generates a 200 OK response to a re-INVITE that contained a Session-Expires header with a value of 1800
                              seconds (30 minutes), the UAS computes the session expiration as 30 minutes after the time when the 200 OK response was sent.
                              For each proxy, the session expiration is 30 minutes after the time when the 2 xx was received or sent. For the UAC, the expiration time is 30 minutes after the receipt of the final response.

The recommended value for the Session-Expires header is 1800 seconds.

The syntax of the Session-Expires header is:

```
Session-Expires  =  ("Session-Expires" | 
"x"
) ":" delta-seconds
                            [refresher]
refresher        =  ";" "refresher" "=" "UAS"|"UAC"
```

The refresher parameter is optional in the initial INVITE, although the UAC can set it to UAC to indicate that it will do the refreshes. The 200 OK response must have the refresher parameter set.

### Min-SE Header

Because of the processing load of INVITE requests you can configure a minimum timer value that the proxy, UAC, and UAS can
                              accept. The proxy, UAC, and UAS. The min-se command sets the minimum timer, and it is conveyed in the Min-SE header in the initial INVITE request.

When making a call, the presence of the Min-SE header informs the UAS and any proxies of the minimum value that the UAC accepts
                              for the session timer duration, in seconds. The default value is 1800 seconds (30 minutes). By not reducing the session timer
                              below the value set, the UAS and proxies prevent the UAC from having to reject a call with a 422 error. Once set, the min-se command value affects all calls originated by the router. If the Min-SE header is not present, the UA accepts any value.

The syntax of the Min-SE header is:

```
Min-SE  =  "Min-SE" ":" delta-seconds
```

### 422 Response Message

If the value of the Session-Expires header is too small, the UAS or proxy rejects the call with a 422 Session Timer Too Small response message. With the 422 response message, the proxy or UAS includes a Min-SE header indicating the minimum session
                              value it can accept. The UAC may then retry the call with a larger session timer value.

If a 422 response message is received after an INVITE request, the UAC can retry the INVITE.

### Supported and Require Headers

The presence of the timer argument in the Supported header indicates that the UA supports the SIP session timer. The presence of the timer argument in the Require header indicates that the opposite UA must support the SIP session timer for the call to be successful.

## How to Configure SIP Session Timer Support

### Prerequisites

Ensure that the gateway has voice functionality that is configurable for SIP.

Establish a working IP network.

Configure VoIP--Information about configuring VoIP in a SIP environment can be found here: http://www.cisco.com/en/US/tech/tk652/tk701/tech_configuration_guides_list.html .

### Restrictions

Cisco SIP gateways cannot initiate the use of SIP session timers, but do fully support session timers if another UA requests
                                    it.

The Min-SE value can be set only by using the min-se command in the configuration gateway. It cannot be set using the CISCO-SIP-UA-MIB.

### Configuring SIP Session Timer Support

To configure the SIP: Session Timer Support feature, complete this task.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- min-se seconds

- min-se exit

- min-se show sip-ua min-se

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
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

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters voice service VoIP configuration mode.

Step 4

sip

#### Example:

```
Router(conf-voi-serv)# sip
```

Enters SIP configuration mode.

Step 5

min-se seconds

#### Example:

```
Router(conf-serv-sip)# min-se 600
```

Sets the minimum session expires header value, in seconds, for all calls.

Range is 90 to 86,400 (one day). The default value is 1800 (30 minutes).

Step 6

min-se exit

#### Example:

```
Router(conf-serv-sip)# exit
```

Exits the current configuration mode.

Step 7

min-se show sip-ua min-se

#### Example:

```
Router(config)# show sip-ua min-se
```

Verifies the value of the Min-SE header.

#### Example

This example contains partial output from the show running-config command. It shows that the Min-SE value has been changed from its default value.

```
! 
voice service voip 
 sip 
  min-se 950 
!
```

## Troubleshooting Tips

To troubleshoot this feature, perform the following steps:

Make sure that you can make a voice call.

Use the debug ccsip all command to enable all SIP debugging capabilities, or use one of the following SIP debug commands:

debug ccsip calls

debug ccsip error

debug ccsip events

debug ccsip messages

debug ccsip states

| Feature Name | Releases | Feature Information |
|---|---|---|
| SIP - Session Timer Support | Baseline Functionality | The SIP Session Timer Support feature adds the capability to periodically refresh Session Initiation Protocol (SIP) sessions
                                       by sending repeated INVITE requests. The repeated INVITE requests, or re-INVITEs, are sent during an active call leg to allow
                                       user agents (UAs) or proxies to determine the status of a SIP session. The following commands were introduced or modified: min-se (SIP) and show sip-ua min-se |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service VoIP configuration mode. |
| Step 4 | sip Example: Router(conf-voi-serv)# sip | Enters SIP configuration mode. |
| Step 5 | min-se seconds Example: Router(conf-serv-sip)# min-se 600 | Sets the minimum session expires header value, in seconds, for all calls. Range is 90 to 86,400 (one day). The default value is 1800 (30 minutes). |
| Step 6 | min-se exit Example: Router(conf-serv-sip)# exit | Exits the current configuration mode. |
| Step 7 | min-se show sip-ua min-se Example: Router(config)# show sip-ua min-se | Verifies the value of the Min-SE header. |