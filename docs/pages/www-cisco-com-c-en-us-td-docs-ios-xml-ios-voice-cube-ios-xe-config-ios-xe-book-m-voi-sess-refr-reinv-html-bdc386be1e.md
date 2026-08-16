---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-sess-refr-reinv-html-bdc386be1e
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-sess-refr-reinv.html
retrieved_at: 2026-08-16T15:45:25.668861+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Session Refresh with Reinvites

## Chapter: Session Refresh with Reinvites

# Session Refresh with Reinvites

## Feature Information for Session Refresh with Reinvites

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Session Refresh with Reinvites

Baseline Functionality

The Cisco Unified Border Element enhances its capability to control session refresh parameters and prevent session timeouts.

The following command was modified or introduced - midcall-signaling

## Prerequisites for Session Refresh with Reinvites

The allow-connections sip to sip command must be configured before you configure the Session refresh with Reinvites feature. For more information and configuration
                              steps see the "Configuring SIP-to-SIP Connections in a Cisco Unified Border Element" section.

Cisco Unified Border Element

Cisco IOS Release 12.4(20)T or a later release must be installed and running on your Cisco Unified Border Element.

Cisco Unified Border Element (Enterprise)

Cisco IOS XE Release 2.5 or a later release must be installed and running on your Cisco ASR 1000 Series Router.

## Information about Session Refresh with Reinvites

Configuring support for session refresh with reinvites expands the ability of the Cisco Unified Border Element to receive
                           a REINVITE message that contains either a session refresh parameter or a change in media via a new SDP and ensure the session
                           does not time out. The midcall-signaling command distinguishes between the way a Cisco Unified Communications Express and Cisco Unified Border Element releases signaling
                           messages. Most SIP-to-SIP video and SIP-to-SIP ReInvite-based supplementary services features require the Configuring Session
                           Refresh with Reinvites feature to be configured.

Cisco IOS Release 12.4(15)XZ and Earlier Releases

Session refresh support via OPTIONS method. For configuration information, see the "Enabling In-Dialog OPTIONS to Monitor
                           Active SIP Sessions" section.

Cisco IOS Release 12.4(15)XZ and Later Releases

Cisco Unified BE transparently passes other session refresh messages and parameters so that UAs and proxies can establish
                           keepalives on a call.

## How to Configure Session Refresh with Reinvites

### Configuring Session refresh with Reinvites

#### Before you begin

SIP-to-SIP video calls and SIP-to-SIP ReInvite-based supplementary services fail if the midcall-signaling command is not configured.

The following features function if the midcall-signaling command is not configured: session refresh, fax, and refer-based supplementary services.

Configuring Session Refresh with Reinvites is for SIP-to-SIP calls only. All other calls (H323-to-SIP, and H323-to-H323)
                                          do not require the midcall-signaling command be configured

Configuring the Session Refresh with Reinvites feature on a dial-peer basis is not supported.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- midcall-signaling passthru

- exit

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

Enters VoIP voice-service configuration mode.

Step 4

sip

#### Example:

```
Router(conf-voi-serv)# sip
```

Enters SIP configuration mode.

Step 5

midcall-signaling passthru

#### Example:

```
Router(conf-serv-sip)# midcall-signaling passthru
```

Passes SIP messages from one IP leg to another IP leg.

Step 6

exit

#### Example:

```
Router(conf-serv-sip)# exit
```

Exits the current mode.

Step 7

end

#### Example:

```
Router(conf-serv-sip) end
```

Returns to privileged EXEC mode.

| Feature Name | Releases | Feature Information |
|---|---|---|
| Session Refresh with Reinvites | Baseline Functionality | The Cisco Unified Border Element enhances its capability to control session refresh parameters and prevent session timeouts. The following command was modified or introduced - midcall-signaling |

| Note | SIP-to-SIP video calls and SIP-to-SIP ReInvite-based supplementary services fail if the midcall-signaling command is not configured. |
|---|---|

| Note | The following features function if the midcall-signaling command is not configured: session refresh, fax, and refer-based supplementary services. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters VoIP voice-service configuration mode. |
| Step 4 | sip Example: Router(conf-voi-serv)# sip | Enters SIP configuration mode. |
| Step 5 | midcall-signaling passthru Example: Router(conf-serv-sip)# midcall-signaling passthru | Passes SIP messages from one IP leg to another IP leg. |
| Step 6 | exit Example: Router(conf-serv-sip)# exit | Exits the current mode. |
| Step 7 | end Example: Router(conf-serv-sip) end | Returns to privileged EXEC mode. |