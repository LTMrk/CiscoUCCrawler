---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-14-1-cjab-b-onprem-deployment-for-jabber141-cjab-b-deploy-jabber-on-p-96ccdf9d11
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/14_1/cjab_b_onprem-deployment-for-jabber141/cjab_b_deploy-jabber-on-premises-129_chapter_010010.html
retrieved_at: 2026-08-21T19:03:40.859252+00:00
---

On-Premises Deployment for Cisco Jabber 14.1

# On-Premises Deployment for Cisco Jabber 14.1

Updated: April 3, 2024

Chapter: Quality of Service

## Chapter: Quality of Service

# Quality of Service

## Quality of Service Options

Use the following options to configure the quality of service for Cisco Jabber:

Option

Description

Enable Media Assure

Configure Media Assure in Cisco Unified Communications Manager.

Supported Codecs

Review the supported Codecs for each client.

Define a port range on the SIP profile

Configure Port Ranges in Cisco Unified Communications Manager

Define a Port Range in Jabber-config.xml

Configure Port Ranges in the jabber-config.xml file.

Set DSCP Values

Configure Differentiated Services Code Point (DSCP) values.

## Enable Media Assure

Media Assure enhances the quality of real-time media on all network types so that your meetings aren't interrupted because
                              of poor media quality.

### Before you begin

Step 1

Open the Cisco Unified CM Administration interface.

Step 2

Select Device > Device Settings > Sip Profile .

Step 3

Select your profile from the available list.

Step 4

In the SDP Information section, select Pass all unknown SDP attributes value for SDP Transparency Profile .

Step 5

Select Apply Config.

## Supported Codecs

Type

Codec

Codec Type

Cisco Jabber for Android

Cisco Jabber for iPhone
                                             				  and iPad

Cisco Jabber for Mac

Cisco Jabber for
                                             				  Windows

Audio

G.711

A-law

Yes

Supports normal mode.

Yes

Yes

µ-law/Mu-law

Yes

Supports normal mode.

Yes

Yes

G.722

Yes

Yes

Yes

G.722.1

24 kb/s and 32 kb/s

Yes

Supports normal mode.

Yes

Yes

G.729

Does not support Visual Voicemail with G.729; however, you can access voice messages using G.729 and the Call Voicemail feature.

No

No

G.729a

Yes

Minimum requirement for low-bandwidth availability.

Only codec that supports low-bandwidth mode.

Supports normal mode.

Yes

Yes

Opus

Yes

Yes

Yes

Video

H.264/AVC

Baseline profile

Yes

Yes

Yes

High profile

No

Yes

Yes

Voicemail

G.711

A-law

Yes

Yes

Yes

µ-law / Mu-law (default)

Yes

Yes

Yes

PCM linear

Yes

Yes

Yes

If users have issues with voice quality when using Cisco Jabber for Android or Cisco Jabber for iPhone
                                 				  and iPad , they can turn low-bandwidth mode on and off in the client settings.

## Define a port range on the SIP profile

The client uses the port range to send RTP traffic across the network.
                              		  The client divides the port range equally and uses the lower half for audio
                              		  calls and the upper half for video calls. As a result of splitting the port
                              		  range for audio media and video media, the client creates identifiable media
                              		  streams. You can then classify and prioritize those media streams by setting
                              		  DSCP values in the IP packet headers.

Step 1

Open the Cisco Unified CM Administration interface.

Step 2

Select Device > Device
                                             				  Settings > SIP Profile .

Step 3

Find the appropriate SIP profile or create a new SIP profile.

The SIP Profile Configuration window opens.

Step 4

Specify whether you want common or separate port ranges for audio
                                       			 and video. If you are separating your audio and video port ranges, provide
                                       			 audio and video ports. Specify the port range in the following fields:

Start Media Port — Defines the start port for media streams. This field sets the lowest port in the range.

Stop Media Port — Defines the stop port for media streams. This field sets the highest port in the range.

Step 5

Select Apply Config and then OK .

## Define a Port Range in Jabber-config.xml

To specify a port range to use when users share their screen from a chat window in Cisco Jabber for
                                          				  Windows , see "SharePortRangeStart" in the Cisco Jabber Parameters Reference Guide .

## Set DSCP Values

Set Differentiated Services Code Point (DSCP) values in RTP media packet headers to prioritize Cisco Jabber traffic as it
                              traverses the network.

### Set DSCP Values on Cisco Unified Communications Manager

You can set DSCP values for audio media and video media on Cisco Unified Communications Manager. Cisco Jabber can then retrieve
                                 the DSCP values from the device configuration and apply them directly to the IP headers of RTP media packets.

Restriction

For later operating systems such as Microsoft Windows 7, Microsoft implements a security feature that prevents applications
                                                from setting DSCP values on IP packet headers. For this reason, you should use an alternate method for marking DSCP values,
                                                such as Microsoft Group Policy.

For more information on configuring flexible DSCP values, refer to Configure Flexible DSCP Marking and Video Promotion Service Parameters .

Step 1

Open the Cisco Unified CM Administration interface.

Step 2

Select System > Service Parameters .

The Service Parameter Configuration window opens.

Step 3

Select the appropriate server and then select the Cisco CallManager service.

Step 4

Locate the Clusterwide Parameters (System - QOS) section.

Step 5

Specify DSCP values as appropriate and then select Save .

### Set DSCP Values with Group Policy

If you deploy Cisco Jabber for Windows on a later operating system such as Microsoft Windows 7, you can use Microsoft Group Policy to apply DSCP values.

Complete the steps in the following Microsoft support article to create a group policy: http://technet.microsoft.com/en-us/library/cc771283%28v=ws.10%29.aspx

You should create separate policies for audio media and video media with the following attributes:

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

For some configurations, there is an option to enable differentiated services for calls in the Cisco Jabber for Mac client and Cisco Jabber for mobile clients .

Important

You can
                                                      					 hear or see other parties, but you cannot be heard or seen

You are
                                                      					 experiencing unexpected Wi-Fi disconnection issues

Disabling
                                                				differentiated service for calls may degrade audio and video quality.

If EnableDSCPPacketMarking is configured as true or false, then the user cannot see Enable Differentiated Service for Calls in the Cisco Jabber clients.

Step 1

In Cisco
                                          			 Jabber for Mac, go to Jabber
                                             				> Preferences > Calls > Advanced and select Enable
                                             				Differentiated Service for Calls .

Step 2

In Cisco Jabber for mobile clients, go to Jabber > Settings > Audio and Video and select Enable Differentiated Service for Calls .

### Set DSCP Values on
                           	 the Network

You can configure
                                 		  switches and routers to mark DSCP values in the IP headers of RTP media.

Audio
                                                   						media streams in ports from 16384 to 24574 as EF

Video
                                                   						media streams in ports from 24575 to 32766 as AF41

Signaling Streams—You can identify signaling between the client and servers based on the various ports required for SIP, CTI
                                          QBE, and XMPP. For example, SIP signaling between Cisco Jabber and Cisco Unified Communications Manager occurs through port
                                          5060.

You should mark signaling packets as AF31.

| Option | Description |
|---|---|
| Enable Media Assure | Configure Media Assure in Cisco Unified Communications Manager. |
| Supported Codecs | Review the supported Codecs for each client. |
| Define a port range on the SIP profile | Configure Port Ranges in Cisco Unified Communications Manager |
| Define a Port Range in Jabber-config.xml | Configure Port Ranges in the jabber-config.xml file. |
| Set DSCP Values | Configure Differentiated Services Code Point (DSCP) values. |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Device Settings > Sip Profile . |
| Step 3 | Select your profile from the available list. |
| Step 4 | In the SDP Information section, select Pass all unknown SDP attributes value for SDP Transparency Profile . |
| Step 5 | Select Apply Config. All SIP devices using this profile must restart before any changes are applied. |

| Type | Codec | Codec Type | Cisco Jabber for Android | Cisco Jabber for iPhone
                                             				  and iPad | Cisco Jabber for Mac | Cisco Jabber for
                                             				  Windows |
|---|---|---|---|---|---|---|
| Audio | G.711 | A-law | Yes Supports normal mode. | Yes | Yes |
| µ-law/Mu-law | Yes Supports normal mode. | Yes | Yes |
| G.722 |  | Yes | Yes | Yes |
| G.722.1 | 24 kb/s and 32 kb/s | Yes Supports normal mode. | Yes | Yes |
| G.729 |  | Does not support Visual Voicemail with G.729; however, you can access voice messages using G.729 and the Call Voicemail feature. | No | No |
| G.729a |  | Yes Minimum requirement for low-bandwidth availability. Only codec that supports low-bandwidth mode. Supports normal mode. | Yes | Yes |
| Opus |  | Yes | Yes | Yes |
| Video | H.264/AVC | Baseline profile | Yes | Yes | Yes |
| High profile | No | Yes | Yes |
| Voicemail | G.711 | A-law | Yes | Yes | Yes |
| µ-law / Mu-law (default) | Yes | Yes | Yes |
| PCM linear |  | Yes | Yes | Yes |

| Step 1 | Open the Cisco Unified CM Administration interface. |
|---|---|
| Step 2 | Select Device > Device
                                             				  Settings > SIP Profile . |
| Step 3 | Find the appropriate SIP profile or create a new SIP profile. The SIP Profile Configuration window opens. |
| Step 4 | Specify whether you want common or separate port ranges for audio
                                       			 and video. If you are separating your audio and video port ranges, provide
                                       			 audio and video ports. Specify the port range in the following fields: Start Media Port — Defines the start port for media streams. This field sets the lowest port in the range. Stop Media Port — Defines the stop port for media streams. This field sets the highest port in the range. |
| Step 5 | Select Apply Config and then OK . |

| To specify a port range to use when users share their screen from a chat window in Cisco Jabber for
                                          				  Windows , see "SharePortRangeStart" in the Cisco Jabber Parameters Reference Guide . |
|---|

| Restriction | For later operating systems such as Microsoft Windows 7, Microsoft implements a security feature that prevents applications
                                                from setting DSCP values on IP packet headers. For this reason, you should use an alternate method for marking DSCP values,
                                                such as Microsoft Group Policy. |
|---|---|

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

| Important | This option is enabled by default. Cisco recommends not
                                             			 disabling this option unless you are experiencing issues in the following
                                             			 scenarios: You can
                                                      					 hear or see other parties, but you cannot be heard or seen You are
                                                      					 experiencing unexpected Wi-Fi disconnection issues Disabling
                                                				differentiated service for calls may degrade audio and video quality. |
|---|---|

| Note | If EnableDSCPPacketMarking is configured as true or false, then the user cannot see Enable Differentiated Service for Calls in the Cisco Jabber clients. |
|---|---|

| Step 1 | In Cisco
                                          			 Jabber for Mac, go to Jabber
                                             				> Preferences > Calls > Advanced and select Enable
                                             				Differentiated Service for Calls . |
|---|---|
| Step 2 | In Cisco Jabber for mobile clients, go to Jabber > Settings > Audio and Video and select Enable Differentiated Service for Calls . |