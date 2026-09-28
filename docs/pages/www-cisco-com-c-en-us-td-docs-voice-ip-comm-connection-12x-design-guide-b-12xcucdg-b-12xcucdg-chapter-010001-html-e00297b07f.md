---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-design-guide-b-12xcucdg-b-12xcucdg-chapter-010001-html-e00297b07f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/design/guide/b_12xcucdg/b_12xcucdg_chapter_010001.html
retrieved_at: 2026-08-17T02:34:43.902761+00:00
---

Design Guide for Cisco Unity Connection 12.x

# Design Guide for Cisco Unity Connection 12.x

Updated: August 17, 2017

Chapter: Sizing and Scaling
	 Cisco Unity Connection Servers

## Chapter: Sizing and Scaling
	 Cisco Unity Connection Servers

# Sizing and Scaling
                     	 Cisco Unity Connection Servers

For a list of
                        		servers that meet Unity Connection specifications, see the Cisco Unity
                        		Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

## Audio Codecs

### Audio Codec Usage
                           	 for Call Connections and Recording

In Unity Connection, a call in any audio codec format
                              		supported by SCCP or SIP signaling—G.711 mu-law, G.711 a-law, G.722, G.729, and
                              		iLBC—are always transcoded to PCM linear. From PCM linear, the recording is
                              		encoded in the system-level recording audio codec—PCM linear, G.711 mu-law,
                              		G.711 a-law, G.729a, or G.726—a systemwide setting in Cisco Unity Connection
                              		Administration. G.711 mu-law is the default.

In this section, we refer to the audio codec that is negotiated
                              		between the calling device and Unity Connection as the “line codec,” and the
                              		audio codec that is set as the system-level recording audio codec as the
                              		“recording codec.”

Supported Line Codecs
                                 		  (Advertised Codecs)

G.711 mu-law

G.711 a-law

G.722

G.729

iLBC

Supported Recording Codecs
                                 		  (System-Level Recording Audio Codecs)

PCM linear

G.711 mu-law (default)

G.711 a-law

G.729a

G.726

GSM 6.10

Because transcoding occurs in
                              		every connection, there is little difference in system impact when the line
                              		codec differs from the recording codec. For example, using G.729a as the line
                              		codec and G.711 mu-law as the recording codec does not place a significant
                              		additional load on the Unity Connection server for transcoding. However, the
                              		iLBC or G.722 codecs require more computation to transcode, and therefore
                              		places a significant additional load on the Unity Connection server.
                              		Consequently, a Unity Connection server can support only half as many G.722 or
                              		iLBC connections as it can G.711 mu-law connections.

Generally, you should not change the system recording format
                              		from the default setting except in the following situations:

To address disk space considerations, consider using a low
                                    			 bit-rate codec such as G.729a or G.726. Note that a low bit-rate codec produces
                                    			 lower quality audio than a high bit-rate codec such as G.711 mu-law.

To improve the audio quality of recordings for endpoints that
                                    			 use G.722 as the line codec, consider using PCM linear. Note that PCM linear
                                    			 increases the disk space that is used.

There are additional possible reasons to change
                              		the recording codec or to choose only to advertise specific line codecs. Review
                              		the following information when making decisions on the system-level recording
                              		audio codec and the advertised codecs on the SCCP or SIP integration:

The audio codecs that are negotiated between the majority of the
                                    			 endpoints and Unity Connection. This information helps you decide the audio
                                    			 codecs that Unity Connection should advertise and the audio codecs that Unity
                                    			 Connection should not advertise. You can then decide when you need Cisco
                                    			 Unified Communications Manager to provide hardware transcoding resources rather
                                    			 than using Unity Connection to provide computationally significant native
                                    			 transcoding, such as when the configuration requires a number of clients to
                                    			 connect to Unity Connection using G.722 or iLBC.

The types of graphical user interface (GUI) clients that play
                                    			 the recordings (for example, web browsers, email clients, or media players) and
                                    			 the audio codecs that these GUI clients support.

The quality of the sound produced by the selected audio codec.
                                    			 Some audio codecs produce higher audio quality than other audio codecs. For
                                    			 example, G.711 produces a higher audio quality than G.729a and is a better
                                    			 choice when higher audio quality is necessary.

The amount of disk space that the audio codec takes up per
                                    			 second of recording time.

PCM linear produces the highest audio
                              		quality and is the most widely supported by media players, yet it uses the most
                              		disk space and bandwidth (16 KB/sec). G.711 (both a-law and mu-law) produces
                              		moderate audio quality compared to PCM linear and is also widely supported by
                              		media players, though it uses half as much disk space and bandwidth (8 KB/sec).
                              		G.729a produces the lowest audio quality of the four supported audio codecs and
                              		is poorly supported by media players because it requires a license for use. Yet
                              		this audio codec uses the least amount of disk space (1 KB/sec). G.726 produces
                              		moderate audio quality, is moderately supported by media players, and uses less
                              		disk space than most of the other codecs (3 KB/sec). This information is
                              		summarized in below table.

Recording Audio Codec

Audio Quality

Supportability

Disk Space Used

Sampling Rate

Channels

Sample Size

PCM linear

Highest

Widely supported

16 KB/sec

8 kHz/sec

1

16 bits

G.711 mu-law/a-law

Moderate

Widely supported

8 KB/sec

8 kHz/sec

1

8 bits

G726

Moderate

Moderately supported

4 KB/sec

8 kHz/sec

1

4 bits

GSM 6.10

Moderate

Poorly supported

1.63 KB/sec

8 kHz/sec

1

N/A

G.729a

Lowest

Poorly supported

1 KB/sec

8 kHz/sec

1

N/A

For details on changing the audio codec that is advertised by
                              		Unity Connection, or the system-level recording audio codec, see the “ Changing the Audio or Video
                                 		  Format of Recordings ” section of the “User Settings” chapter of the
                              		System Administration Guide for Cisco Unity Connection Release 11.x , at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/administration/guide/b_cucsag.html .

When modifying the advertised audio codecs, the choices are
                              		G.711 mu-law, G.711 a-law, G.722, G.729, and iLBC. In addition, you also
                              		indicate an order of preference for the chosen codecs.

For SCCP integrations, the order of the audio codecs is not
                              		important because Cisco Unified CM negotiates the audio codec based on the
                              		location of the port and the device in the negotiated call. However, for SIP
                              		integrations the order of the audio codecs is important. If one audio codec is
                              		preferred over another audio codec, Unity Connection advertises that it
                              		supports both audio codecs but prefers to use the one specified over the other.

In Web Inbox, the received voice messages are always played or downloaded in PCM linear whether any codec is selected to record
                                          the messages.

### Audio Codec
                           	 Considerations for VPIM Networking

If VPIM
                              		networking connects Unity Connection to another Unity Connection server, to a
                              		Cisco Unity server, or to a third-party voice-messaging system, you must choose
                              		a compatible audio codec.

Note the following audio codec considerations for Unity
                              		Connection VPIM networking:

For inbound messages, Unity Connection can do one of the
                                    			 following:

Convert voice messages to any audio format that Unity Connection
                                          				  supports.

Not convert the audio format of the voice message, keeping the
                                          				  voice message in its original audio format.

For outbound voice messages, Unity Connection can do one of the
                                    			 following:

Convert voice messages to the G.726 audio format.

Not convert the audio format of the voice message, keeping the
                                          				  voice message in its original audio format. Not converting is useful when you
                                          				  use VPIM networking to send voice messages between Unity Connection servers, or
                                          				  between Unity Connection and Cisco Unity servers.

For more information on VPIM Networking, see the VPIM Networking .

## Voice Messaging
                        	 Ports

The existing voice
                                    				messaging system -Evaluate how well the existing voice messaging system
                                 			 functions, if applicable. This evaluation may give you some idea how many ports
                                 			 are needed for taking voice messages, for turning message waiting indicators
                                 			 (MWIs) on and off, and for message notification.

- Use of the Web Inbox web
                                 			 client, or the Cisco Unity Connection ViewMail for Microsoft Outlook client -When users use the Web Inbox web client, the Messaging Inbox web client, or
                              		  the ViewMail for Outlook client, Unity Connection uses telephone record and
                              		  playback (TRAP) to allow users to play and record voice messages by phone
                              		  rather than using speakers and a microphone. This feature is especially useful
                              		  when users work in cubicles, where there is a lack of privacy. However, when a
                              		  user plays or records a message using TRAP, a port on the Unity Connection
                              		  server is used. (No port is used when a user uses speakers and a microphone to
                              		  play and record messages.) If the customer wants users to use TRAP,
                              		  calculations for the total number of voice ports required need to take this
                              		  into account.

- Unity Connection
                                 			 cluster -In some cases, an existing voice messaging system has more voice
                              		  messaging ports than Unity Connection supports. When configured as a Unity
                              		  Connection cluster (an active/active high availability Unity Connection server
                              		  pair), the Unity Connection system can support double the number of voice
                              		  messaging ports compared to a single-server deployment. For more information,
                              		  see the Cisco Unity Connection Clusters (Active/Active High Availability) chapter.

- Networking -The
                              		  customer can purchase additional Unity Connection servers or Unity Connection
                              		  cluster pairs and connect them using intrasite and/or intersite networking to
                              		  increase the number of voice ports supported. For more information, see the Networking chapter.

For additional
                           		information on the number of voice messaging ports, see the " Planning the Usage of Voice
                              		  Messaging Ports " section in the applicable Cisco Unity Connection
                           		integration guide at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/integration/guide/sip-csps/b_cuc12xintcsps.html .

## Storage Capacity
                        	 for Voice Messages

For
                           		Unity Connection systems that are configured to store voicemails only (no
                           		emails or faxes are stored on the server), base the server requirements on the
                           		total number of voice storage minutes required for each user. A supported Unity
                           		Connection server generally provides storage for at least 20 to 30 minutes of
                           		voice messages per user for the maximum number of users supported on that
                           		server. See the Cisco Unity Connection 12.x Supported Platforms List for the
                           		exact amount of voice-message storage supported for each server.

For Unity Connection systems that are configured to store faxes
                           		and email replies to voice messages in addition to voice messages, you cannot
                           		base server requirements on the total number of voice-storage minutes required
                           		for each user because the message store on the Unity Connection server also
                           		include faxes and possibly email. However, you can calculate the storage
                           		requirement for the desired number of voice-storage minutes and add that to the
                           		current mailbox limits.

For Unity Connection systems that are configured to store faxes
                           		and email replies to voice messages in addition to voice messages, start with
                           		the total number of voice-storage minutes required for each user, and add the
                           		amount of storage space that you want users to have for faxes. In general, the
                           		email stored in Unity Connection should not significantly affect storage
                           		capacity.

If the customer is replacing an existing voice-messaging system
                           		with Unity Connection, it may be possible to obtain information from the
                           		existing system on the average number of minutes of voice messages that users
                           		currently have. You can then multiply the average number of minutes by the
                           		recording size per minute—according to the codec that Unity Connection uses to
                           		record messages—to arrive at the average amount of disk space required for
                           		voice messages per user.

Start with a one-to-one correlation between the legacy
                           		voice-messaging system and Unity Connection. If the legacy system handles a
                           		larger capacity than the largest Unity Connection server, consider splitting
                           		the legacy user population onto more than one Unity Connection server.

## Users

For the maximum number of users supported for each supported
                           		server, planning, and selection of servers, take into account the possibility
                           		of adding users in the future. For more information, see the Cisco Unity Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

For information on moving users from one Cisco Unity Connection
                           		server to another, see the “ Moving or Migrating Users
                              		  Between Locations in Cisco Unity Connection ” section of the “Users”
                           		chapter of the System Administration Guide for Cisco Unity Connection, Release
                           		12.x, available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

## Simultaneous
                        	 TUI/VUI Sessions

To determine the maximum number of simultaneous TUI
                           		(touchtone conversation) and/or VUI (voice-recognition) sessions that Unity
                           		Connection can support, consider the following:

Unity Connection cluster —If a Unity Connection cluster
                                 			 server pair is configured (active/active high availability) instead of a
                                 			 standalone Unity Connection server, the maximum number of TUI and/or VUI
                                 			 sessions supported is doubled for each platform overlay. For the maximum number
                                 			 of sessions that Unity Connection can support for each platform overlay when a
                                 			 Unity Connection cluster is configured, see the Cisco Unity Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

Desktop Clients —When desktop clients (for example, the Web
                                 			 Inbox and IMAP) are deployed, the maximum number of TUI and/or VUI sessions
                                 			 that Unity Connection supports is reduced for Platform Overlay 1 servers. For
                                 			 more information, see the Cisco Unity Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

Note that some IMAP clients (for example, Cisco Unified Personal
                           		Communicator 7.0 and earlier) do not support the IMAP IDLE command. IMAP
                           		clients that do not support IMAP IDLE consume more system resources on a Unity
                           		Connection server. As a result, each active instance of each client that does
                           		not support IMAP Idle and is accessing Unity Connection voice messages counts
                           		as four active clients. See the “IMAP
                              		  Clients Used to Access Unity Connection Voice Messages” section for
                           		additional details.

G.722, iLBC or Opus Audio Codecs —Using G.722, iLBC or Opus
                                 			 audio codecs “on the line” or as advertised codecs reduces the maximum number
                                 			 of TUI and/or VUI sessions that Unity Connection supports for each platform
                                 			 overlay as compared to using the G.711 audio codec. For the maximum number of
                                 			 sessions that Unity Connection supports for each platform overlay when using
                                 			 the G.722, iLBC or Opus audio codec, see the Virtualization for Cisco Unity Connection (CUC) at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-unity-connection.html .
                                 			 For a discussion of supported system recording and advertised or “on the line”
                                 			 audio codecs with Unity Connection, see the “Audio
                                    				Codecs” section.

Media
                                    				Encryption and Authentication using Secure Real Time Protocol (SRTP) —Using
                                 			 SRTP for media encryption and authentication reduces the maximum number of TUI
                                 			 and/or VUI sessions that Unity Connection supports for each platform overlay
                                 			 upto 15 percent.

## IMAP Clients Used
                        	 to Access Unity Connection Voice Messages

Third-party IMAP clients such as email clients
                           		are supported for accessing voice messages from Unity Connection. Scalability
                           		of IMAP clients depends on whether they support IMAP Idle. Using clients that
                           		support IMAP Idle reduces the load on the Unity Connection server; a Unity
                           		Connection server can support four times as many IMAP Idle clients as it can
                           		non-IMAP Idle clients. (IMAP Idle, described in RFC 2177, allows a client to
                           		indicate to the server that it is ready to accept real-time notifications.)

Most third-party IMAP email clients, such as Microsoft Outlook
                           		and Lotus Notes, support IMAP Idle. Cisco Unified Personal Communicator (CUPC)
                           		version 8.0 and later supports IMAP idle. The Unity Connection Plug-in for IBM
                           		Lotus Sametime version 7.11 and later supports IMAP idle. Among the clients
                           		that do not support IMAP Idle are Cisco Unified Mobility Advantage and Cisco
                           		Unified Mobile Communicator. For information on whether a client supports IMAP
                           		Idle, see the documentation for the client. For information on the number of
                           		IMAP clients supported for each platform overlay (each grouping of comparable
                           		supported Unity Connection servers), see the Cisco Unity Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

You can mix IMAP Idle and non-IMAP Idle clients if necessary.
                           		However, to simplify sizing calculations, you should isolate IMAP Idle and
                           		non-IMAP Idle clients on separate Unity Connection servers or cluster server
                           		pairs (active/active high availability). If you must mix IMAP Idle and non-IMAP
                           		Idle clients on the same server or cluster server pair, count each non-IMAP
                           		Idle client as four IMAP Idle clients for sizing calculations. In addition, you
                           		may want to put users who use IMAP Idle clients and users who use non-IMAP Idle
                           		clients into separate classes of service so that you can run a report that
                           		tells you how many of each you have accessing voice messages on a given Unity
                           		Connection server.

Note that when you isolate IMAP Idle and non-IMAP Idle clients
                           		on separate servers or cluster server pairs, you should set up networking
                           		between the servers if they are not already networked. For more information on
                           		Unity Connection networking, see the Networking chapter.

## Visual Voicemail
                        	 Clients and Sessions

The maximum number of visual voicemail clients
                           		is equivalent to the maximum number of users supported by a Unity Connection
                           		server or a cluster (active/active high availability) server pair. For the
                           		maximum number of Visual Voicemail clients, sessions, or ports supported for
                           		each platform overlay, see the Cisco Unity Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

The maximum number of Visual Voicemail sessions is equivalent to
                           		the maximum number of ports available on a Unity Connection server or cluster
                           		(active/active high availability) server pair.

For supported versions of Cisco Unified Communications Manager
                           		and Cisco IP Phones with the Visual Voicemail feature, see System Requirements
                           		for Cisco Unity Connection Release 12.x at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html .

For system requirements, see the System Requirements for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/requirements/b_12xcucsysreqs.html .

For installation and configuration information, see the
                           		applicable Installation and Configuration Guide for Visual Voicemail
                              		  Release at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cupa/visual_voicemail/8-5/install/guide/vv_install.html .

For end-user information, see the Quick Start Guide: Visual Voicemail Release 8.5 at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cupa/visual_voicemail/8-5/quick_start/guide/Quick_Start_Guide_for_Visual_Voicemail_Release_8-5_chapter1.html .

## Simultaneous
                        	 Mobile Clients

Cisco Unified Mobility Advantage (CUMA) Release
                           		7.0 connects to the Unity Connection server using IMAP, so it is considered an
                           		IMAP client. Because the Cisco Unified Mobility Advantage IMAP connection is
                           		not an IMAP Idle connection, the maximum number of simultaneous mobile clients
                           		supported by Cisco Unified Mobility Advantage, Cisco Unified Mobile
                           		Communicator, and Unity Connection is reduced by approximately 70 percent. For
                           		the maximum number of Cisco Unified Mobility Advantage clients and Cisco
                           		Unified Mobile Communicator clients supported for each platform overlay, see
                           		the Cisco Unity Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

## Messaging
                        	 Assistant Clients

The maximum number of Messaging Assistant
                           		clients is equivalent to the maximum number of users supported by a Unity
                           		Connection server or a cluster (active/active high availability) server pair.
                           		For the maximum number of Messaging Assistant clients or users supported for
                           		each platform overlay, see the Cisco Unity Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

For information on using the Messaging Assistant, see the User
                           		Guide for the Cisco Unity Connection Personal Call Transfer Rules Web Tool (Release 12.x) at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/user/guide/pctr/b_12xcucugpctr.html .

## Web Inbox
                        	 Clients

For the maximum
                           		number of Web Inbox clients supported for each platform overlay, see the Cisco Unity Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

For information on using the Web Inbox, see the Quick Start
                           		Guide for the Cisco Unity Connection Web Inbox (Release 12.x) at http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/quick_start/guide/b_12xcucqsginbox.html .

## Cisco Unified
                        	 Personal Communicator Clients

The Cisco Unified Personal Communicator (CUPC)
                           		client does not support IMAP Idle, so the number of CUPC clients supported by a
                           		Unity Connection server or a cluster (active/active high availability) server
                           		pair is lower than the maximum number of users. For the maximum number of CUPC
                           		clients supported for each platform overlay, see the Cisco Unity Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

For information on using CUPC, see the applicable Cisco Unified
                           		Personal Communicator user guide at http://www.cisco.com/c/en/us/support/unified-communications/unified-personal-communicator/products-user-guide-list.html .

## IBM Lotus Sametime
                        	 Clients

The voice messaging plug-in for the IBM Lotus
                           		Sametime client does not support IMAP Idle, so the number of IBM Lotus Sametime
                           		clients supported by a Unity Connection server or a cluster (active/active high
                           		availability) server pair is lower than the maximum number of users. For the
                           		maximum number of IBM Lotus Sametime clients supported for each platform
                           		overlay, see the Cisco Unity Connection 12.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/supported_platforms/b_12xcucspl.html .

For information on the IBM Lotus Sametime client, see the
                           		applicable version of Release Notes for Cisco Unified Messaging with IBM Lotus
                              		  Sametime at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-release-notes-list.html .

## RSS Reader
                        	 Clients

The maximum
                           		number of RSS reader clients is equivalent to the maximum number of users
                           		supported by a Unity Connection server or a cluster (active/active high
                           		availability) server pair.

For more information on the RSS Feed feature and RSS reader
                           		clients, see the “ Configuring an RSS Reader to
                              		  View Voice Messages ” section of the “Advanced System Settings” chapter
                           		of the System Administration Guide for Cisco Unity Connection Release 12.x, at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/administration/guide/b_12xcucsag.html .

| Note | Use
                                       		of the G.722 or iLBC codec as line codecs or advertised codecs reduces the
                                       		number of voice ports that can be provisioned on the Unity Connection server.
                                       		For more information on the number of voice ports supported for each platform
                                       		overlay when using G.722 or iLBC codecs, see the Cisco Unity Connection 11.x Supported Platforms List at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/11x/supported_platforms/b_11xcucspl.html . |
|---|---|

| Recording Audio Codec | Audio Quality | Supportability | Disk Space Used | Sampling Rate | Channels | Sample Size |
|---|---|---|---|---|---|---|
| PCM linear | Highest | Widely supported | 16 KB/sec | 8 kHz/sec | 1 | 16 bits |
| G.711 mu-law/a-law | Moderate | Widely supported | 8 KB/sec | 8 kHz/sec | 1 | 8 bits |
| G726 | Moderate | Moderately supported | 4 KB/sec | 8 kHz/sec | 1 | 4 bits |
| GSM 6.10 | Moderate | Poorly supported | 1.63 KB/sec | 8 kHz/sec | 1 | N/A |
| G.729a | Lowest | Poorly supported | 1 KB/sec | 8 kHz/sec | 1 | N/A |

| Note | In Web Inbox, the received voice messages are always played or downloaded in PCM linear whether any codec is selected to record
                                          the messages. |
|---|---|

| Note | The
                                    		email stored in Unity Connection is only replies to or forwards of Unity
                                    		Connection voice messages, with or without the original voice message. This
                                    		email is not related to email in the email inbox of the user. |
|---|---|

| Note | Accessing voice messages from Unity Connection through IMAP
                                    		clients is supported with both the IPv4 and IPv6 addresses. However, sending
                                    		voice messages to Unity Connection using SMTP is only supported with the IPv4
                                    		addresses. |
|---|---|