---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-06b60d1e4f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_appendix_a_.html
retrieved_at: 2026-08-21T02:49:43.422378+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Appendix A: Configuring Cisco Unified SIP SRST Features Using Redirect Mode

## Chapter: Appendix A: Configuring Cisco Unified SIP SRST Features Using Redirect Mode

# Appendix A: Configuring Cisco Unified SIP SRST Features Using Redirect Mode

This chapter describes Cisco Unified Session Initiation Protocol (SIP) Survivable Remote Site Telephony (SRST) features using
                        redirect mode.

This chapter applies to version 3.0 only.

## Prerequisites for Cisco Unified SIP SRST Features Using Redirect Mode

Complete the prerequisites documented in the Cisco Unified SRST Feature Overview chapter.

## Restrictions for Cisco Unified SIP SRST Features Using Redirect Mode

See the restrictions documented in the Cisco Unified SRST Feature Overview chapter.

## Information About Cisco Unified SIP SRST Features Using Redirect Mode

Cisco Unified SIP SRST provides backup to an external SIP call control (IP-PBX) by providing basic registrar and redirect
                           services. These services are used by a SIP IP phone if a WAN connection outage when the SIP phone is unable to communicate
                           with its primary SIP proxy. The Cisco Unified SIP SRST device also provides PSTN gateway access for placing and receiving
                           PSTN calls.

To make maximum use of the Cisco Unified SIP SRST service, the local SIP IP phones should support dual (concurrent) registration
                           with both their primary SIP proxy or registrar and the Cisco Unified SIP SRST backup registrar. Cisco Unified SIP SRST works
                           for the following types of calls:

Local SIP IP phone to local SIP phone, if the main proxy is unavailable.

Other services like class of restriction (COR) for local SIP IP phones to the outgoing PSTN. For example, to block outgoing
                                 1-900 numbers.

### How to Configure Cisco Unified SIP SRST Features Using Redirect Mode

## Configuring Call Redirect Enhancements to Support Calls Between SIP IP Phones for Cisco Unified SIP SRST

The call redirect enhancement supports calls from a local SIP phone to another local SIP phone through the Cisco IOS voice
                           gateway. Before this enhancement, an attempt by a SIP phone to contact another local SIP phone using the Cisco IOS voice gateway
                           as if it were a SIP proxy or redirect server would fail. However, the Cisco IOS voice gateway can now act as a SIP redirect
                           server. The voice gateway responds to the originator with a SIP Redirect message, allowing the SIP phone that originated the
                           call to establish a call to its destination.

The redirect ip2ip (voice service) and redirect ip2ip (dial-peer) commands allow you to enable the SIP functionality, globally or on a specific inbound dial peer. The default
                           application on Cisco Unified SIP SRST supports IP-to-IP redirection.

### Configuring Audio and Video Codecs at the Dial Peer Level

When IP-to-IP redirection is configured in dial-peer configuration mode, the configuration for the specific dial peer takes
                                             precedence over the global configuration entered under voice service configuration mode.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- redirect ip2ip

- end

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

Enters voice service configuration mode.

Step 4

redirect ip2ip

#### Example:

```
Router(config-voi-srv)# redirect ip2ip
```

Configures a video codec at the dial peer level. Redirects SIP phone calls to SIP phone calls globally on a gateway using
                                             the Cisco IOS voice gateway.

Step 5

end

#### Example:

```
Router(config-voi-srv)# end
```

Returns to privileged EXEC mode.

### Configuring Call Redirect Enhancements to Support Calls On a Specific VoIP Dial Peer

To enable IP-to-IP call redirection for a specific VoIP dial peer, configure it on an inbound dial peer in dial-peer configuration
                                 mode. The default application on Cisco Unified SIP SRST supports IP-to-IP redirection.

When IP-to-IP redirection is configured in dial-peer configuration mode, the configuration for the specific dial peer takes
                                             precedence over the global configuration entered under voice service configuration mode.

#### Before you begin

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- application application-name

- redirect ip2ip

- end

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

dial-peer voice tag voip

#### Example:

```
Router(config)# dial-peer voice 25 voip
```

Enters dial-peer configuration mode.

tag : A number that uniquely identifies the dial peer (this number has local significance only).

VoIP: Indicates that this is a VoIP peer using voice encapsulation on the POTS network and is used for configuring redirect.

Step 4

application application-name

#### Example:

```
Router(config-dial-peer)# application session
```

Enables a specific application on a dial peer.

For SIP, the default Tool Command Language (Tcl) application (from the Cisco IOS image) is session and can be applied to both
                                                   VoIP and POTS dial peers.

The application must support IP-to-IP redirection.

Step 5

redirect ip2ip

#### Example:

```
Router(config-dial-peer)# redirect ip2ip
```

Redirects SIP phone calls to SIP phone calls on a specific VoIP dial peer using the Cisco IOS voice gateway.

Step 6

end

#### Example:

```
Router(config-dial-peer)# end
```

Returns to privileged EXEC mode.

## Configuring Sending 300 Multiple Choice Support

Before Cisco IOS Release 12.2(15)ZJ, when a call was redirected, the SIP gateway would send a 302 Moved Temporarily message.
                              The first longest match route on a gateway (dial-peer destination pattern) was used in the Contact header of the 302 message.
                              With Release 12.2(15)ZJ, if multiple routes to a destination exist for a redirected number (multiple dial peers are matched),
                              the SIP gateway sends a 300 Multiple Choice message, and the multiple routes in the Contact header are listed.

The configuration below allows users to choose the order in which the routes appear in the Contact header.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- redirect contact order [best-match | longestmatch]

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice service voip

### Example:

```
Router(config)# voice service voip
```

Enters voice service configuration mode.

Step 4

sip

### Example:

```
Router(config-voi-srv)# sip
```

Enters SIP configuration mode.

Step 5

redirect contact order [best-match | longestmatch]

### Example:

```
Router(conf-serv-sip)# redirect contact order
best-match
```

Sets the order of contacts in the 300 Multiple Choice message. The keywords are defined as follows:

best-match : Uses the current system configuration to set the order of contacts.

longestmatch : Sets the contact order by using the destination pattern longest match first, and then the second longest match, the third
                                                longest match, and so on. This is the default.

Step 6

end

### Example:

```
Router(config-serv-sip)# end
```

Returns to privileged EXEC mode.

## Configuration Examples for Cisco Unified SIP SRST Features Using Redirect Mode

This section provides the following configuration example:

### Cisco Unified SIP SRST: Example

This section provides a configuration example to match the configuration tasks in the previous sections.

```
!
! Sets up the registrar server and enables IP-to-IP redirection and 300
! Multiple Choice support.
!
voice service voip
redirect ip2ip
sip
registrar server expires max 600 min 60
redirect contact order best-match
!
! Configures the voice-class codec with G.711uLaw and G729 codecs. The codecs are
! applied to the voice register pools.
!
voice class codec 1
codec preference 1 g711ulaw
codec preference 2 g729br8
!
! The voice register pools define various pools that are used to match
! incoming REGISTER requests and create corresponding dial peers.
!
voice register pool 1
id mac 0030.94C2.A22A
preference 5
cor incoming call91 1 91011
translate-outgoing called 1
proxy 10.2.161.187 preference 1 monitor probe icmp-ping
alias 1 94... to 91011 preference 8
voice-class codec 1
!
voice register pool 2
id ip 192.168.0.3 mask 255.255.255.255
preference 5
cor outgoing call95 1 91021
proxy 10.2.161.187 preference 1
voice-class codec 1
!
voice register pool 3
id network 10.2.161.0 mask 255.255.255.0
number 1 95... preference 1
preference 5
cor incoming call95 1 95011
cor outgoing call95 1 95011
proxy 10.2.161.187 preference 1 monitor probe icmp-ping
max registrations 5
voice-class codec 1
!
voice register pool 4
id network 10.2.161.0 mask 255.255.255.0
number 1 94... preference 1
preference 5
cor incoming everywhere default
cor outgoing everywhere default
proxy 10.2.161.187 preference 1
max registrations 2
voice-class codec 1
!
! Configures translation rules to be applied in the voice register pools.
!
translation-rule 1
Rule 0 94 91
!
! Sets up proxy monitoring.
!
call fallback active
!
dial-peer cor custom
name 95
name 94
name 91
!
! Configures COR values to be applied to the voice register pool.
!
dial-peer cor list call95
member 95
!
dial-peer cor list call94
member 94
!
dial-peer cor list call91
member 91
!
dial-peer cor list everywhere
member 95
member 94
member 91
!
! Configures a voice port and a POTS dial peer for calls to and from the PSTN endpoints.
voice-port 1/0/0
!
dial-peer voice 91500 pots
corlist incoming call91
corlist outgoing call91
destination-pattern 91500
port 1/0/0
!
```

| Note | This chapter applies to version 3.0 only. |
|---|---|

| Note | When IP-to-IP redirection is configured in dial-peer configuration mode, the configuration for the specific dial peer takes
                                             precedence over the global configuration entered under voice service configuration mode. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service configuration mode. |
| Step 4 | redirect ip2ip Example: Router(config-voi-srv)# redirect ip2ip | Configures a video codec at the dial peer level. Redirects SIP phone calls to SIP phone calls globally on a gateway using
                                             the Cisco IOS voice gateway. |
| Step 5 | end Example: Router(config-voi-srv)# end | Returns to privileged EXEC mode. |

| Note | When IP-to-IP redirection is configured in dial-peer configuration mode, the configuration for the specific dial peer takes
                                             precedence over the global configuration entered under voice service configuration mode. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 25 voip | Enters dial-peer configuration mode. tag : A number that uniquely identifies the dial peer (this number has local significance only). VoIP: Indicates that this is a VoIP peer using voice encapsulation on the POTS network and is used for configuring redirect. |
| Step 4 | application application-name Example: Router(config-dial-peer)# application session | Enables a specific application on a dial peer. For SIP, the default Tool Command Language (Tcl) application (from the Cisco IOS image) is session and can be applied to both
                                                   VoIP and POTS dial peers. The application must support IP-to-IP redirection. |
| Step 5 | redirect ip2ip Example: Router(config-dial-peer)# redirect ip2ip | Redirects SIP phone calls to SIP phone calls on a specific VoIP dial peer using the Cisco IOS voice gateway. |
| Step 6 | end Example: Router(config-dial-peer)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service configuration mode. |
| Step 4 | sip Example: Router(config-voi-srv)# sip | Enters SIP configuration mode. |
| Step 5 | redirect contact order [best-match \| longestmatch] Example: Router(conf-serv-sip)# redirect contact order
best-match | Sets the order of contacts in the 300 Multiple Choice message. The keywords are defined as follows: best-match : Uses the current system configuration to set the order of contacts. longestmatch : Sets the contact order by using the destination pattern longest match first, and then the second longest match, the third
                                                longest match, and so on. This is the default. |
| Step 6 | end Example: Router(config-serv-sip)# end | Returns to privileged EXEC mode. |