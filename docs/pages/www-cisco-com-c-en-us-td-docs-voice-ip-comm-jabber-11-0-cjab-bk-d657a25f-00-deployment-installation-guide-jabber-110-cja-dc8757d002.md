---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-11-0-cjab-bk-d657a25f-00-deployment-installation-guide-jabber-110-cja-dc8757d002
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/11_0/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110/CJAB_BK_D657A25F_00_deployment-installation-guide-jabber-110_chapter_01111.html
retrieved_at: 2026-08-25T21:46:57.263933+00:00
---

Cisco Jabber 11.0 Deployment and Installation Guide

# Cisco Jabber 11.0 Deployment and Installation Guide

Updated: June 25, 2015

Chapter: Cisco Jabber Reference Information

## Chapter: Cisco Jabber Reference Information

# Cisco Jabber Reference Information

## Client
	 Availability

Users can define
		  whether their availability reflects their calendar events by setting an option
		  to let others know they are in a meeting from the Status tab of the Options window from the client. This option
		  synchronizes events in your calendar with your availability. The client only
		  displays In a
			 meeting availability for supported integrated calendars.

Cisco Jabber
				for mobile clients don't support this meeting integration.

Microsoft
				Exchange and Cisco Unified Communication Manager IM and Presence Integration —
				Applies to on-premises deployments. The Include Calendar information in my Presence Status field in Cisco Unified Presence is the same as the In
				  a meeting option in the client. Both fields update the same value
				in the Cisco Unified Communication Manager IM and Presence database.

If users set
				both fields to different values, then the last field that the user sets takes
				priority. If users change the value of the Include Calendar information in my Presence Status field while the client is running, the users must restart the client for those
				changes to apply.

Cisco
				Jabber Client — Applies to on-premises and cloud-based deployments. You must
				disable Cisco Unified Communication Manager IM and Presence and Microsoft
				Exchange integration for the client to set the In
				  a meeting availability. The client checks if integration between
				Cisco Unified Communication Manager IM and Presence and Microsoft Exchange is
				on or off. The client can only set availability if integration is off.

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

Add lists of contacts for
				the XMPP: and IM: handlers to create group chats. Use a semi-colon to delimit
				contacts, as in the following example:

```
XMPP:user_a@domain.com;user_b@domain.com;user_c@domain.com;user_d@domain.com
```

#### Add Subject
		  Lines and Body Text

You can add
		  subject lines and body text to any of the protocol handlers so that when users
		  click on the hyperlink to create a person-to-person or group chat, the client
		  opens a chat window with pre-populated subject line and body text.

Using any
				supported protocol handler for instant messaging on the client

For either
				person-to-person chats or for group chats

Including a
				subject and body text, or one or the other

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

#### Enter DTMF in
		  the IM Window

```
tel:1800123456,,,5678#
```

#### Enter DTMF in
		  an Active Call

During a call,
		  users can copy and paste DTMF digits into the call window of the client. Users
		  can easily enter Meeting IDs, Attendee IDs, and PINs from their meetings
		  invite. If you enter alpha numeric strings during an active call they are
		  interpreted as the corresponding numbers on the keypad.

#### Supported DTMF
		  Strings

0 to 9

#

*

Comma—meaning
				a one second delay (multiple commas are supported)

a to z, A to
				Z—These characters are not supported when on an active call.

## Define a Port
	 Range on the SIP Profile

The client uses the port range to send RTP traffic across the network.
		  The client divides the port range equally and uses the lower half for audio
		  calls and the upper half for video calls. As a result of splitting the port
		  range for audio media and video media, the client creates identifiable media
		  streams. You can then classify and prioritize those media streams by setting
		  DSCP values in the IP packet headers.

The SIP Profile Configuration window opens.

Start Media Port — Defines the start
					 port for media streams. This field sets the lowest port in the range.

Stop Media Port — Defines the stop port
					 for media streams. This field sets the highest port in the range.

## Set DSCP Values

Set Differentiated Services Code Point (DSCP) values in RTP media packet headers to prioritize Cisco Jabber traffic as it traverses the network.

### Set DSCP Values on Cisco Unified Communications Manager

You can set DSCP values for audio media and video media on Cisco Unified Communications Manager. Cisco Jabber can then retrieve the DSCP values from the device configuration and apply them directly to the IP headers of RTP media packets.

For later operating systems such as Microsoft Windows 7, Microsoft implements a security feature that prevents applications from setting DSCP values on IP packet headers. For this reason, you should use an alternate method for marking DSCP values, such as Microsoft Group Policy.

For more information on configuring flexible DSCP values, refer to Configure Flexible DSCP Marking and Video Promotion Service Parameters .

The Service Parameter Configuration window opens.

### Set DSCP Values with Group Policy

If you deploy Cisco Jabber for Windows on a later operating system such as   Microsoft Windows 7, you can use Microsoft Group Policy to apply DSCP values.

Complete the steps in the following Microsoft support article to create a group policy: http:/​/​technet.microsoft.com/​en-us/​library/​cc771283%28v=ws.10%29.aspx

Attributes

Audio Policy

Video Policy

Signaling Policy

Application name

CiscoJabber.exe

CiscoJabber.exe

CiscoJabber.exe

Protocol

UDP

UDP

TCP

Port number or range

Corresponding port number or range from the SIP profile on Cisco Unified Communications Manager.

Corresponding port number or range from the SIP profile on Cisco Unified Communications Manager.

5060 for SIP

5061 for secure SIP

DSCP value

46

34

24

### Set DSCP Values on
	 the Client

For some
		  configurations, there is an option to enable differentiated services for calls
		  in the Cisco Jabber for Mac client and Cisco Jabber for
			 mobile clients .

You can
					 hear or see other parties, but you cannot be heard or seen

You are
					 experiencing unexpected Wi-Fi disconnection issues

Disabling
				differentiated service for calls may degrade audio and video quality.

If EnableDSCPPacketMarking is configured as true or
				false, then the user cannot see Enable Differentiated Service for Calls in the Cisco
				Jabber clients.

### Set DSCP Values on
	 the Network

You can configure
		  switches and routers to mark DSCP values in the IP headers of RTP media.

Audio
						media streams in ports from 16384 to 24574 as EF

Video
						media streams in ports from 24575 to 32766 as AF41

Signaling
				Streams
			  — You can
				  identify signaling between the client and servers based on the various ports
				  required for SIP, CTI QBE, and XMPP. For example, SIP signaling between 
				  Cisco Jabber
				  and 
				  Cisco Unified Communications Manager occurs through port 5060.

You should
				  mark signaling packets as AF31.

| Note | Cisco Jabber
				for mobile clients don't support this meeting integration. |
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

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Device
				  Settings > SIP Profile . |
| Step 3 | Find the appropriate SIP profile or create a new SIP profile. The SIP Profile Configuration window opens. |
| Step 4 | Specify whether you want common or separate port ranges for audio
			 and video. If you are separating your audio and video port ranges, provide
			 audio and video ports. Specify the port range in the following fields: Start Media Port — Defines the start
					 port for media streams. This field sets the lowest port in the range. Stop Media Port — Defines the stop port
					 for media streams. This field sets the highest port in the range. |
| Step 5 | Select Apply Config and then OK . |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select System > Service Parameters . The Service Parameter Configuration window opens. |
| Step 3 | Select the appropriate server and then select the Cisco CallManager service. |
| Step 4 | Locate the Clusterwide Parameters (System - QOS) section. |
| Step 5 | Specify DSCP values as appropriate and then select Save . |

| Attributes | Audio Policy | Video Policy | Signaling Policy |
|---|---|---|---|
| Application name | CiscoJabber.exe | CiscoJabber.exe | CiscoJabber.exe |
| Protocol | UDP | UDP | TCP |
| Port number or range | Corresponding port number or range from the SIP profile on Cisco Unified Communications Manager. | Corresponding port number or range from the SIP profile on Cisco Unified Communications Manager. | 5060 for SIP 5061 for secure SIP |
| DSCP value | 46 | 34 | 24 |

| Note | If EnableDSCPPacketMarking is configured as true or
				false, then the user cannot see Enable Differentiated Service for Calls in the Cisco
				Jabber clients. |
|---|---|

| Step 1 | In Cisco
			 Jabber for Mac, go to Jabber
				> Preferences > Calls > Advanced and select Enable
				Differentiated Service for Calls . |
|---|---|
| Step 2 | In Cisco
			 Jabber for mobile clients, go to Jabber > Settings > Audio and Video and select Enable
				Differentiated Service for Calls . |