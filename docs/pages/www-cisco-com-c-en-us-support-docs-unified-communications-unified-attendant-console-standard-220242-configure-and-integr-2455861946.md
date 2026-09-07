---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-attendant-console-standard-220242-configure-and-integr-2455861946
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-attendant-console-standard/220242-configure-and-integrate-cuac-standard-im.html
retrieved_at: 2026-09-07T15:48:37.584965+00:00
---

Configure and Integrate CUAC Standard IM and Presence Integration

# Configure and Integrate CUAC Standard IM and Presence Integration

### Download Options

Updated: February 17, 2023

Document ID: 220242

Contents

## Contents

## Introduction

This document describes how the CUAC Standard client integrates with the IM and Presence server for Jabber presence in the CUAC console.

## CUAC Standard IM and Presence Integration

### Configuration in the CUAC Standard Client

The Cisco Unified Attendant Console (CUAC) Standard client connects and integrates with the IM and Presence server for Jabber presence in the CUAC console for directory contacts. The configuration for this connection to presence is fairly simple in the CUAC Standard client. This information can either be supplied during the client installation or skipped and provided after installation.

To configure these settings in the client, choose File > Options > Operator Details .

In the Presence Details section, input the required information:

Server Address - IP Address, Hostname, or FQDN of the IM and Presence server

Port - 5222 (because the connection is an XMPP subscription)

Domain - The domain that is configured as the Default Domain in the IM and Presence server configuration.

User - Presence Enabled End Username

Password - End User Password

After these options are configured, the presence details are validated with the IM and Presence server when the Apply button is selected.

Note : When the connection is successful, the Apply button is not selectable. If there was a problem with the connection details, this error is displayed:

This error is presented in the event that there are connection issues with the server provided, bad username/password, or incorrect presence domain.

### Presence in the CUAC Client CUAC-Standard Client

Presence in the CUAC client is seen in the presence oval to the left of the user last name.  This is an example of an Available status.

Busy/On a call/Meeting presence is displayed as this:

DND is displayed as this:

### How does the CUAC Standard Client Pull Presence for Users

#### Default User@Proxy Domain IM Addressing Scheme

The CUAC client uses the end user account that is configured in the options to send presence subscriptions for users.

In the Contact Details for each user, the Directory URI field is used to populate the URI for the presence subscriptions.  For user firstname lastname above, we see this:

Because the user does not have a Directory URI configured in CUCM, apply the username only.

Use the Domain configured in the Presence Details to build the URI - firstinitiallastname@domain.net.

This URI is then used to send a XMPP presence subscription to IMP to get presence for the user.

#### Directory URI IM Addressing Scheme

CUAC Standard does support the Directory URI IM addressing scheme for presence subscriptions.

The process to subscribe to presence is the same, however, the client is provided with the full URI rather than just the username.

In this case the full URI is provided in the contact details:

Remember that the Administrator must provide the DEFAULT DOMAIN in the connection details whether the default IM address scheme or Directory URI is used in IMP.

### CUAC Standard Presence Integration Troubleshooting

It is important to ensure that the domain, username and password are correct in the Presence connection details.

In the logs we see this:

#### Incorrect Domain Configured in the CUAC Standard Client Connection Details

2016-05-24 15:51:19,799 [1] INFO XMPP - XMPPWrapper.IsValidLogin: Host:x.x.x.x,Port:5222, Domain:domain.ne , UserName:firstintiallastname@domain.ne . 2016-05-24 15:51:19,799 [1] INFO XMPP - XMPPWrapper.IsValidLogin: Log Event:Creating new instance of _xmppClient 2016-05-24 15:51:19,799 [1] INFO XMPP - XMPPWrapper.IsValidLogin: Log Event:New instance of _xmppClient created

In this instance, the Domain is configured as domain.ne rather than domain.net.  This is incorrect and leads to the incorrect user that attempts to authenticate, firstinitiallastname@domain.ne.

User Authorization failed to error:

2016-05-24 15:51:32,761 [33] INFO XMPP - XMPPWrapper.IsValidLogin: Log Event:RECV: <stream:features><mechanisms xmlns='urn:ietf:params:xml:ns:xmpp-sasl'><mechanism>PLAIN</mechanism><mechanism>CISCO-VTG-TOKEN</mechanism></mechanisms></stream:features> 2016-05-24 15:51:32,762 [33] INFO XMPP - XMPPWrapper.IsValidLogin: Log Event:SEND: <auth mechanism="PLAIN" xmlns="urn:ietf:params:xml:ns:xmpp-sasl">AGd3YXNoaW5ndG9uAFJUUCFhcHBz</auth> 2016-05-24 15:51:32,779 [33] INFO XMPP - XMPPWrapper.IsValidLogin: Log Event:RECV: <failure xmlns='urn:ietf:params:xml:ns:xmpp-sasl'><not-authorized/></failure>

Stop the connection and close the session to IMP for the user:

2016-05-24 15:51:32,780 [33] INFO XMPP - XMPPWrapper.IsValidLogin: Log Event:Firing OnLoginError() 2016-05-24 15:51:32,780 [33] INFO XMPP - XMPPWrapper.IsValidLogin: StatusChangeEvent:<Start xmlns="firstinitiallastname@domain.ne"> <Status id="403">&lt;failure xmlns="urn:ietf:params:xml:ns:xmpp-sasl"&gt;&lt;not-authorized /&gt;&lt;/failure&gt;</Status> </Start> 2016-05-24 15:51:32,780 [33] INFO XMPP - XMPPWrapper.IsValidLogin: Log Event:AUTH ERROR: <failure xmlns="urn:ietf:params:xml:ns:xmpp-sasl"><not-authorized /></failure> 2016-05-24 15:51:32,781 [33] INFO XMPP - XMPPWrapper.IsValidLogin: Log Event:RECV: </stream:stream> 2016-05-24 15:51:32,781 [33] INFO XMPP - XMPPWrapper.IsValidLogin: Log Event:------ Disconnected to firstinitiallastname@domain.ne ------ 2016-05-24 15:51:32,781 [33] INFO XMPP - XMPPWrapper.IsValidLogin: Log Event:Firing OnDisconnect() 2016-05-24 15:51:32,781 [33] INFO XMPP - XMPPWrapper.IsValidLogin: StatusChangeEvent:<Shutdown xmlns="firstinitiallastname@domain.ne"> <Status id="503">Connection to x.x.x.x has been lost</Status> </Shutdown>

Error is displayed in the client Window:

2016-05-24 15:51:34,299 [1] WARN  View - OperatorDetailsViewModel.DoSave. Presence Server connection test failed. Please check the connection details and try again. Host:x.x.x.x, Port:5222

To fix this issue, correct the domain.  The same errors are present in the event of an incorrect password or bad username.

#### Successful Presence Change Notification

2016-05-24 15:41:01,086 [3] DEBUG XMPP - XMPPWrapper: PresencePlugin Log:Firing OnPresenceNotification() 2016-05-24 15:41:01,086 [3] DEBUG XMPP - <PresenceNotify xmlns="firstinitiallastname@domain.net/jabber_9934"> <Show>available</Show> <State type="sub" /> <State type="phone"></State> </PresenceNotify> 2016-05-24 15:41:01,086 [3] INFO XMPP - XMPPWrapper: OnPresenceChange: URI:firstinitiallastname@domain.net, eventUID:available, subState:, PhoneSate:

In this presence update, user status changed to Available.

## Related Documents

Unified attendant consoles: eos eol notice listing

### Revision History

1.0

17-Feb-2023

Initial Release

### Contributed by Cisco Engineers

Josh Hammonds

Cisco TAC Engineer

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 17-Feb-2023 | Initial Release |