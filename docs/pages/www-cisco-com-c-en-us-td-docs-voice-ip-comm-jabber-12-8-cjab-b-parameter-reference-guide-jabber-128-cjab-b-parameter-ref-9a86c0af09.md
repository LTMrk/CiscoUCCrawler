---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-8-cjab-b-parameter-reference-guide-jabber-128-cjab-b-parameter-ref-9a86c0af09
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_8/cjab_b_parameter-reference-guide-jabber-128/cjab_b_parameter-reference-guide-jabber-128_chapter_01000.html
retrieved_at: 2026-08-21T05:22:33.194454+00:00
---

Parameters Reference Guide for Cisco Jabber 12.8

# Parameters Reference Guide for Cisco Jabber 12.8

Updated: January 21, 2020

Chapter: Presence

## Chapter: Presence

# Presence

## CalendarWebExMeetingPresence

Applies to Cisco Jabber for Windows.

Enables users' presence to change to "In a Webex meeting" even if they do not join the Cisco Webex session link but the meeting is in their Microsoft Outlook calendar.

true - Users' presence changes to "In a Webex meeting" even if they do not join the Cisco Webex session link.

false (default) - Users must join the Cisco Webex session link for their presence to change to "In a Webex meeting". Otherwise, their presence remains "Available", even if
                                    the meeting is in their Microsoft Outlook calendar.

Example: <CalendarWebExMeetingPresence>true</CalendarWebExMeetingPresence>

## DomainsForOutlookPresence

Specifies that if you configure a domain with this key, you'll be able to see presence information for people only within
                              the specified domain. If not configured, you'll be able to see presence information for all the contacts (domains).

This key supports multiple whitelisted domains which are separated by comma. For example <DomainsForOutlookPresence>cisco.com,
                              cisco.cn</DomainsForOutlookPresence>.

It supports simple wildcard match. For example, *.cisco.com or *cisco.com.

Example: <DomainsForOutlookPresence>cisco.com</DomainsForOutlookPresence>

## EnableOutlookPresenceIntegration

Applies to Cisco Jabber for Mac

Prerequisite: Microsoft Outlook 15.34.0

True (default)—Users' presence in Cisco Jabber is integrated with Microsoft Outlook.

False—Users' presence in Cisco Jabber is not integrated with Microsoft Outlook.

## HVDDisconnectSignout

Applies to Cisco Jabber Softphone for VDI —Windows

This parameter controls how Cisco Jabber for Windows handles presence status when users disconnect from their HVDs.

True—When a user signs out or otherwise disconnects from their HVD, Cisco Jabber automatically signs out and presence status updates to Offline , within 10 seconds.

False (default)—When a user signs out, or otherwise disconnects from their HVD, Cisco Jabber remains signed in, and their presence status shows as Available .

Example:

```
<HVDDisconnectSignout>False</HVDDisconnectSignout>
```

## LoginResource

Applies to all the Cisco Jabber clients.

multiResource
                                       				(default)—Users can sign in to multiple instances of the client at the same
                                       				time.

wbxconnect—Users can sign in to one instance of the client at a time. 
                                       			 This option applies to cloud and hybrid deployments only.

The client appends the wbxconnect suffix to the user's JID. Users cannot sign in to any other Cisco Jabber client that uses the wbxconnect suffix.

mutualExclusion—Users can sign in to one instance of the client at a time. This option applies to all deployment types (on-premises,
                                       cloud, and hybrid). New sign ins automatically sign out users from older instances of the client.

Example: <LoginResource>mutualExclusion</LoginResource>

## meetingservice_supportmultimeeting

Applies to Cisco Jabber for Windows.

Specifies if Jabber is allowed to start multiple Webex Meetings .

true (default)—Enable multiple meetings

false—Diable multiple meetings

Example: <meetingservice_supportmultimeeting>true</meetingservice_supportmultimeeting>

## OutlookContactResolveMode

Applies to Cisco Jabber for Windows and Mac

Specifies how Jabber resolves the presence of a contact in Outlook.

Auto (default)—When you configure the proxyaddress attribute with SIP:user@cupdomain , then Jabber uses user@cupdomain as a Jabber ID. If you configure the proxyaddress attribute without SIP, Jabber uses an email address to resolve the presence of a contact in Outlook.

Email —When you configure the proxyaddress attribute with SIP:user@cupdomain , then Jabber uses user@cupdomain as an email address. If you configure the proxyaddress attribute without SIP, Jabber uses an email address to resolve the presence of a contact in Outlook.

Example: <OutlookContactResolveMode>Email</OutlookContactResolveMode>

## PresenceServerAddress

Hostname
                                       				( hostname )

IP address
                                       				( 123.45.254.1 )

FQDN ( hostname.domain.com )

Example: <PresenceServerAddress> hostname </PresenceServerAddress>

## PresenceServerURL

Specifies the Central Authentication Service (CAS) URL for the Cisco Webex Messenger service.

Example: <PresenceServerURL> https://loginp.webexconnect.com/cas/sso/ ex_org /orgadmin.app </PresenceServerURL>