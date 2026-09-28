---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-7-cjab-b-deploy-jabber-on-premises-127-cjab-b-deploy-jabber-on-pre-05e7c0193f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_7/cjab_b_deploy-jabber-on-premises-127/cjab_b_deploy-jabber-on-premises-127_chapter_010011.html
retrieved_at: 2026-08-21T21:07:08.182155+00:00
---

On-Premises Deployment for Cisco Jabber 12.7

# On-Premises Deployment for Cisco Jabber 12.7

Updated: April 1, 2024

Chapter: Integrate Cisco Jabber with Applications

## Chapter: Integrate Cisco Jabber with Applications

# Integrate Cisco Jabber with Applications

## Configure Presence
                        	 in Microsoft SharePoint 2010 and 2013

If your
                              		  organization defines users' profiles where their IM address is different from
                              		  their email address, then additional configuration is required to enable
                              		  presence integration between the client and Microsoft SharePoint 2010 and 2013.

### Before you begin

For Cisco Jabber for Windows clients only.

Ensure that
                                    				all sites are in sync with Microsoft SharePoint Central Administration (CA).

Ensure that
                                    				synchronization between Microsoft SharePoint and Active Directory is set up.

Step 1

If you have
                                       			 Microsoft SharePoint 2013, update the SharePoint CA profile pages for users
                                       			 with the following information:

For the SIP Address profile field, leave it blank.

In the Work email profile field, enter the user profile.
                                             				  For example, john4mail@example.pst .

Step 2

If you have
                                       			 Microsoft SharePoint 2010, update the SharePoint CA profile pages for users
                                       			 with the following information:

For the SIP Address profile field, enter the user profile.
                                             				  For example, john4mail@example.pst

In the Work email profile field, leave it blank.

## Client
                        	 Availability

Users can define
                              		  whether their availability reflects their calendar events by setting an option
                              		  to let others know they are in a meeting from the Status tab of the Options window from the client. This option
                              		  synchronizes events in your calendar with your availability. The client only
                              		  displays In a
                                 			 meeting availability for supported integrated calendars.

Cisco Jabber for mobile clients support this meeting integration feature from Cisco Jabber 11.7 release.

Microsoft Exchange and Cisco Unified Communication Manager IM and Presence Integration — Applies to on-premises deployments.
                                       The Include Calendar information in my Presence Status field in Cisco Unified Presence is the same as the In a meeting option in the client. Both fields update the same value in the Cisco Unified Communication Manager IM and Presence database.

If users set both fields to different values, then the last field that the user sets takes priority. If users change the value
                                       of the Include Calendar information in my Presence Status field while the client is running, the users must restart the client for those changes to apply.

Cisco Jabber Client — Applies to on-premises and cloud-based deployments. You must disable Cisco Unified Communication Manager
                                       IM and Presence and Microsoft Exchange integration for the client to set the In a meeting availability. The client checks if integration between Cisco Unified Communication Manager IM and Presence and Microsoft
                                       Exchange is on or off. The client can only set availability if integration is off.

Deployment Scenario

You
                                             						select In a meeting (according to my calendar)

You do
                                             						not select In a meeting (according to my calendar)

You
                                             						enable integration between Cisco Unified Communication Manager IM and Presence
                                             						and Microsoft Exchange.

Cisco
                                             						Unified Communication Manager IM and Presence sets availability status

Availability status does not change

You do
                                             						not enable integration between Cisco Unified Communication Manager IM and
                                             						Presence and Microsoft Exchange.

Client
                                             						sets availability status

Availability status does not change

Cloud-based deployments

Client
                                             						sets availability status

Availability status does not change

Availability Enabled in the Client

Availability Enabled by Integrating Cisco Unified Communication
                                             						Manager IM and Presence with Microsoft Exchange

Offline in a meeting availability is not supported.

Offline in a meeting availability is supported.

In a meeting availability is supported for
                                             						non-calendar events.

In a meeting availability is not supported for
                                             						non-calendar events.

Offline in a meeting availability refers to when the user is not
                                                         						  logged in to the client but an event exists in the user's calendar.

Non-calendar events refer to events that do not appear in the
                                                         						  user's calendar, such as instant meetings, Offline , or On a call .

## Protocol
                           		Handlers

XMPP: 
                                       			 or XMPP://

Starts an
                                       				instant message and opens a chat window in Cisco Jabber .

IM: 
                                       			 or IM://

Starts an
                                       				instant message and opens a chat window in Cisco Jabber .

TEL: 
                                       			 or TEL://

Starts an
                                       				audio or video call with Cisco Jabber .

TEL is
                                                   				  registered by Apple native phone. It cannot be used to cross launch Cisco
                                                   				  Jabber for iPhone and iPad.

CISCOTEL: 
                                       			 or CISCOTEL://

Starts an
                                       				audio or video call with Cisco Jabber .

SIP: or SIP://

Starts an
                                       				audio or video call with Cisco Jabber .

Starts an audio or video call with Cisco Jabber .

### Registry Entries for Protocol Handlers

HKEY_CLASSES_ROOT\tel\shell\open\command

HKEY_CLASSES_ROOT\xmpp\shell\open\command

HKEY_CLASSES_ROOT\im\shell\open\command

### Protocol Handlers
                           	 on HTML Pages

You can add protocol handlers on HTML pages as part of the href attribute. When users click the hyperlinks that
                                 		  your HTML pages expose, the client performs the appropriate action for the
                                 		  protocol.

#### TEL and IM
                                 		  Protocol Handlers

Example of the TEL: and IM:
                                 		  protocol handlers on an HTML page:

```
<html>
  <body>
    <a href="TEL:1234">Call 1234</a><br/>
    <a href="IM:msmith@domain">Send an instant message to Mary Smith</a>
  </body>
</html>
```

In the preceding
                                 		  example, when users click the hyperlink to call 1234, the client starts an
                                 		  audio call to that phone number. When users click the hyperlink to send an
                                 		  instant message to Mary Smith, the client opens a chat window with Mary.

#### CISCOTEL and
                                 		  SIP Protocol Handlers

Example of the
                                 		  CISCOTEL and SIP protocol handlers on an HTML page:

```
<html>
  <body>
    <a href="CISCOTEL:1234">Call 1234</a><br/>
				<a href="SIP:msmith@domain">Call Mary</a><br/>
    <a href="CISCOTELCONF:msmith@domain;amckenzi@domain">Weekly conference call</a>
  </body>
</html>
```

In the preceding
                                 		  example, when users click the Call 1234 or Call Mary hyperlinks, the client starts an audio call to that phone number.

#### XMPP Protocol
                                 		  Handlers

Example of a group chat
                                 		  using the XMPP: protocol handler on an HTML page:

```
<html>
  <body>
    <a href="XMPP:msmith@domain;amckenzi@domain">Create a group chat with Mary Smith and Adam McKenzie</a>
  </body>
</html>
```

In the preceding
                                 		  example, when users click the hyperlink to create a group chat with Mary Smith
                                 		  and Adam McKenzie, the client opens a group chat window with Mary and Adam.

Tip

Add lists of contacts for
                                                				the XMPP: and IM: handlers to create group chats. Use a semi-colon to delimit
                                                				contacts, as in the following example:

```
XMPP:user_a@domain.com;user_b@domain.com;user_c@domain.com;user_d@domain.com
```

#### Add Subject Lines and Body Text

You can add subject lines and body text to any of the protocol handlers so that when users click on the hyperlink to create
                                 a person-to-person or group chat, the client opens a chat window with pre-populated subject line and body text.

Using any supported protocol handler for instant messaging on the client

For either person-to-person chats or for group chats

Including a subject and body text, or one or the other

```
xmpp:msmith@domain?message;subject=I.T.%20Desk
```

```
im:user_a@domain.com;user_b@domain.com;user_c@domain.com?message;subject=I.T%20Desk;body=Jabber%2010.5%20Query
```

### Protocol Handler Supported Parameters

#### Cross Launch for Mobile Clients

```
ciscotel://1234567?CrossLaunchBackSchema=SomeAppSchema&CrossLaunchBackAppName=SomeAppName
```

none (default)—No application in the dialog box.

app_name —The application name that is displayed in the dialog box.

none(default)—You stay in Cisco Jabber.

schema —The schema used to cross launch back the application.

#### Supported Separators

```
tel:123;123
```

```
im:participant1@example.com,participant2@example.com
```

### DTMF
                           	 Support

#### Enter DTMF in the IM Window

In the conversation window of the client, you can enter a protocol handler including DTMF digits and the client will create
                                 a link that participants can use. The supported protocols are TEL, CISCOTEL, SIP, CLICKTOCALL, CISCOIM, IM, and XMPP. The
                                 supported parameters are numbers or SIP URIs.

```
tel:1800123456,,,5678#
```

#### Enter DTMF in an Active Call

During a call, users can copy and paste DTMF digits into the call window of the client. Users can easily enter Meeting IDs,
                                 Attendee IDs, and PINs from their meeting invitation. If you enter alphanumeric strings during an active call, they are interpreted
                                 as the corresponding numbers on the keypad, and commas represent a one second pause between DTMF signals.

#### Supported DTMF Signals

If a user enters a DTMF signal that isn't supported by the system that Jabber is calling, then Jabber will not send the input
                                 from the user.

Cisco Jabber for Windows and mobiles support the following DTMF signals:

0 to 9

#

*

A to D

| Step 1 | If you have
                                       			 Microsoft SharePoint 2013, update the SharePoint CA profile pages for users
                                       			 with the following information: For the SIP Address profile field, leave it blank. In the Work email profile field, enter the user profile.
                                             				  For example, john4mail@example.pst . |
|---|---|
| Step 2 | If you have
                                       			 Microsoft SharePoint 2010, update the SharePoint CA profile pages for users
                                       			 with the following information: For the SIP Address profile field, enter the user profile.
                                             				  For example, john4mail@example.pst In the Work email profile field, leave it blank. |

| Note | Cisco Jabber for mobile clients support this meeting integration feature from Cisco Jabber 11.7 release. |
|---|---|

| Deployment Scenario | You
                                             						select In a meeting (according to my calendar) | You do
                                             						not select In a meeting (according to my calendar) |
|---|---|---|
| You
                                             						enable integration between Cisco Unified Communication Manager IM and Presence
                                             						and Microsoft Exchange. | Cisco
                                             						Unified Communication Manager IM and Presence sets availability status | Availability status does not change |
| You do
                                             						not enable integration between Cisco Unified Communication Manager IM and
                                             						Presence and Microsoft Exchange. | Client
                                             						sets availability status | Availability status does not change |
| Cloud-based deployments | Client
                                             						sets availability status | Availability status does not change |

| Availability Enabled in the Client | Availability Enabled by Integrating Cisco Unified Communication
                                             						Manager IM and Presence with Microsoft Exchange |
|---|---|
| Offline in a meeting availability is not supported. | Offline in a meeting availability is supported. |
| In a meeting availability is supported for
                                             						non-calendar events. | In a meeting availability is not supported for
                                             						non-calendar events. |
| Note Offline in a meeting availability refers to when the user is not
                                                         						  logged in to the client but an event exists in the user's calendar. Non-calendar events refer to events that do not appear in the
                                                         						  user's calendar, such as instant meetings, Offline , or On a call . | Note | Offline in a meeting availability refers to when the user is not
                                                         						  logged in to the client but an event exists in the user's calendar. Non-calendar events refer to events that do not appear in the
                                                         						  user's calendar, such as instant meetings, Offline , or On a call . |
| Note | Offline in a meeting availability refers to when the user is not
                                                         						  logged in to the client but an event exists in the user's calendar. Non-calendar events refer to events that do not appear in the
                                                         						  user's calendar, such as instant meetings, Offline , or On a call . |

| Note | Offline in a meeting availability refers to when the user is not
                                                         						  logged in to the client but an event exists in the user's calendar. Non-calendar events refer to events that do not appear in the
                                                         						  user's calendar, such as instant meetings, Offline , or On a call . |
|---|---|

| Note | TEL is
                                                   				  registered by Apple native phone. It cannot be used to cross launch Cisco
                                                   				  Jabber for iPhone and iPad. |
|---|---|

| Tip | Add lists of contacts for
                                                				the XMPP: and IM: handlers to create group chats. Use a semi-colon to delimit
                                                				contacts, as in the following example: XMPP:user_a@domain.com;user_b@domain.com;user_c@domain.com;user_d@domain.com |
|---|---|