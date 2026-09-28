---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-10-3-1-english-adminguide-cs38-bk-ad57597a-00-adminguide-8831-cs-406dd41996
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/10_3_1/english/AdminGuide/CS38_BK_AD57597A_00_adminguide-8831/CS38_BK_AD57597A_00_adminguide-8831_chapter_0111.html
retrieved_at: 2026-08-21T13:38:14.043460+00:00
---

Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

# Cisco Unified IP Conference Phone 8831 and 8831NR Administration Guide

Updated: November 17, 2014

Chapter: Model Information,
	 Status, and Statistics

## Chapter: Model Information,
	 Status, and Statistics

# Model Information,
                     	 Status, and Statistics

## Model Information,
                        	 Status, and Statistics Overview

This chapter describes how to use the following menus and screens on the
                           		Cisco Unified IP Conference Phone to view conference station information
                           		such as model, device, and network information:

Model Information screen: Displays hardware and software information
                                 			 about the conference phone.

Status menu: Provides access to screens that display network and
                                 			 call statistics and device information.

You can use the information on these screens to monitor the operation of
                           		a conference phone and to assist with troubleshooting.

You can also obtain much of this information, and obtain other related
                           		information, remotely through the conference phone web page. For more
                           		information, see Remote Monitoring .

For more information about troubleshooting the conference phone, see Troubleshooting and Maintenance .

There are certain options on the Network Configuration menu, Device
                                       		  Configuration menu, and Security Configuration menu that are for display only.
                                       		  These options are described in Cisco Unified IP Conference Phone Settings .

## Model Information
                        	 Screen

Model Number:
                                       				Model number of the conference phone.

MAC Address:
                                       				Media Access Control (MAC) address of the conference phone.

Software
                                       				Version: Version of the firmware running on the conference phone.

BootROM
                                       				Version: Identifier of the factory-installed load running on the conference
                                       				phone.

App Load ID:
                                       				Identifies the firmware running on the conference phone.

Active
                                       				load:xxx: Current active firmware running on the conference phone.

Inactive
                                       				load: xxx: Inactive firmware kept on the conference phone.

Last Upgrade:
                                       				<time date>: Time and date for last firmware upgrade

Active
                                       				Server: xxx: Current active server.

Stand-by-Server:xxx: Current stand by server.

Mic 1: (xx)
                                       				connected/disconnected: Mic connection state

Mic 2: (xx)
                                       				connected/disconnected: Mic connection state

Wireless Mic
                                       				1ID: Mic ID

Wireless Mic
                                       				2ID: Mic ID

System
                                       				ID:xxx: System ID

Linked Mode:
                                       				ON/OFF: Linked mode state

Backlight On
                                       				Time: <time>: Back light on time

Backlight On
                                       				Duration: <time>: Back light on duration

Days
                                       				Backlight Not Active: <days>: Days of the week when backlight is inactive

### Display Model Information Screen

To display the Model Information screen, press the Settings button and then select Model Information .

To exit the Model Information screen, press Exit .

## Status
                        	 Menu

Network
                                    			 Statistics: Displays the Network Statistics screen, which shows Ethernet
                                    			 traffic statistics.

Call Statistics:
                                    			 Displays information about the last call on the conference phone.

Device
                                    			 Information: Displays device settings and related information for the
                                    			 conference phone.

The Status menu
                                       		  also contains a Ping menu that allows you to test network connectivity to
                                       		  another conference phone.

### Display Status Menu

Press Apps .

Select Admin Settings > Status
                                                				  Menu .

### Network Statistics
                           	 Screen

The Network
                              		Statistics screen displays information about the conference phone and network
                              		performance.

The following table
                              		describes the information that appears in this screen.

Item

Description

Rx Frames

Number of
                                          				packets received by the conference phone.

Rx Broadcasts

Number of
                                          				broadcast packets received by the conference phone.

Rx Unicast

Total number
                                          				of unicast packets received by the conference phone.

Tx Frames

Number of
                                          				packets transmitted by the conference phone.

Tx
                                          				Broadcasts

Tx Unicast

CDP
                                          				Neighbor Device ID

CDP
                                          				Neighbor IP Address

CDP
                                          				Neighbor Port

Restart
                                          				Cause

Displays the
                                          				cause of a restart, for example: Port X 100 Full .

IPv4

Displays the
                                          				message: DHCP DISABLED or DHCP ENABLED .

#### Display Network Statistics Screen

To display the Network Statistics screen, perform  these
                                    		  steps:

Press Applications .

Select Settings .

Select Status .

Select Network Statistics .

To reset the Rx Frames, Tx Frames, and Rx Broadcasts statistics to
                                             			 0, press Clear .

### Call Statistics
                           	 Screen

The Call Statistics
                              		screen displays information about the last call on the conference phone.

You can remotely
                                          		  view the call statistics information by using a web browser to access the
                                          		  Streaming Statistics web page. For more information about remote monitoring,
                                          		  see Remote Monitoring .

A single call can
                              		have multiple voice streams, but data is captured for only the last voice
                              		stream. A voice stream is a packet stream between two endpoints. If one
                              		endpoint is put on hold, the voice stream stops even though the call is still
                              		connected. When the call resumes, a new voice packet stream begins, and the new
                              		call data overwrites the former call data.

#### Call Statistics
                              	 Information

The following table
                                 		describes the information displayed on the screen.

Item

Description

Receiver Codec
                                             				Type (Rcvr Codec)

Type of voice
                                             				stream received (RTP streaming audio): G.729, G.711 u-law, G.711 A-law, G.722,
                                             				G.722.1, or Lin16k.

Sender Codec
                                             				Type

Type of voice
                                             				stream transmitted (RTP streaming audio): G.729, G.711 u-law, G.711 A-law,
                                             				G.722, or Lin16k.

Receiver Size
                                             				(Rcvr Size)

Number of
                                             				bytes of voice packets received since voice stream was opened.

Sender Size

Number of
                                             				bytes of voice packets sent since voice stream was opened.

Rcvr Packets

Number of RTP
                                             				voice packets received since voice stream was opened.

This number
                                                         				  is not necessarily identical to the number of RTP voice packets received since
                                                         				  the call began because the call might have been placed on hold.

Sender Packets

Number of RTP
                                             				voice packets transmitted since voice stream was opened.

This number
                                                         				  is not necessarily identical to the number of RTP voice packets transmitted
                                                         				  since the call began because the call might have been placed on hold.

Avg Jitter

Estimated
                                             				average RTP packet jitter (dynamic delay that a packet encounters when going
                                             				through the network) observed since the receiving voice stream was opened.

Max Jitter

Maximum jitter
                                             				observed since the receiving voice stream was opened.

Rcvr Discarded

Number of RTP
                                             				packets discarded by the receiver.

Rcvr Lost
                                             				Packets

Missing RTP
                                             				packets (lost in transit).

Voice Quality Metrics

MOS LQK

Score that is
                                             				an objective estimate of the mean opinion score (MOS) for listening quality
                                             				(LQK) that rates from 5 (excellent) to 1 (bad). This score is based on audible
                                             				concealment events due to frame loss in the preceding 8-second interval of the
                                             				voice stream.

Avg MOS LQK

Average MOS
                                             				LQK score observed for the entire voice stream.

Min MOS LQK

Lowest MOS
                                             				LQK score observed from start of the voice stream.

Max MOS LQK

Baseline or
                                             				highest MOS LQK score observed from start of the voice stream.

Cumulative
                                             				Conceal Ratio

Total number
                                             				of concealment frames divided by total number of speech frames received from
                                             				start of the voice stream.

Max Conceal
                                             				Ratio

Maximum
                                             				concealment ratio that is observed during the call.

Conceal Secs

Number of
                                             				seconds that have concealment events (lost frames) from the start of the voice
                                             				stream (includes severely concealed seconds).

Severely
                                             				Conceal Secs

Number of
                                             				seconds that have more than 5 percent concealment events (lost frames) from the
                                             				start of the voice stream.

Latency

Estimate of
                                             				the network latency, expressed in milliseconds. Represents a running average of
                                             				the round-trip delay, measured when RTCP receiver report blocks are received.

#### Display Call Statistics Screen

To display the Call Statistics screen for information about
                                    		  the last voice stream, follow these steps:

Press Settings .

Select Status .

Select Call Statistics .

| Note | There are certain options on the Network Configuration menu, Device
                                       		  Configuration menu, and Security Configuration menu that are for display only.
                                       		  These options are described in Cisco Unified IP Conference Phone Settings . |
|---|---|

| Step 1 | To display the Model Information screen, press the Settings button and then select Model Information . |
|---|---|
| Step 2 | To exit the Model Information screen, press Exit . |

| Note | The Status menu
                                       		  also contains a Ping menu that allows you to test network connectivity to
                                       		  another conference phone. |
|---|---|

| Step 1 | Press Apps . |
|---|---|
| Step 2 | Select Admin Settings > Status
                                                				  Menu . |

| Item | Description |
|---|---|
| Rx Frames | Number of
                                          				packets received by the conference phone. |
| Rx Broadcasts | Number of
                                          				broadcast packets received by the conference phone. |
| Rx Unicast | Total number
                                          				of unicast packets received by the conference phone. |
| Tx Frames | Number of
                                          				packets transmitted by the conference phone. |
| Tx
                                          				Broadcasts |  |
| Tx Unicast |  |
| CDP
                                          				Neighbor Device ID |  |
| CDP
                                          				Neighbor IP Address |  |
| CDP
                                          				Neighbor Port |  |
| Restart
                                          				Cause | Displays the
                                          				cause of a restart, for example: Port X 100 Full . |
| IPv4 | Displays the
                                          				message: DHCP DISABLED or DHCP ENABLED . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Settings . |
| Step 3 | Select Status . |
| Step 4 | Select Network Statistics . |
| Step 5 | To reset the Rx Frames, Tx Frames, and Rx Broadcasts statistics to
                                             			 0, press Clear . |

| Note | You can remotely
                                          		  view the call statistics information by using a web browser to access the
                                          		  Streaming Statistics web page. For more information about remote monitoring,
                                          		  see Remote Monitoring . |
|---|---|

| Item | Description |
|---|---|
| Receiver Codec
                                             				Type (Rcvr Codec) | Type of voice
                                             				stream received (RTP streaming audio): G.729, G.711 u-law, G.711 A-law, G.722,
                                             				G.722.1, or Lin16k. |
| Sender Codec
                                             				Type | Type of voice
                                             				stream transmitted (RTP streaming audio): G.729, G.711 u-law, G.711 A-law,
                                             				G.722, or Lin16k. |
| Receiver Size
                                             				(Rcvr Size) | Number of
                                             				bytes of voice packets received since voice stream was opened. |
| Sender Size | Number of
                                             				bytes of voice packets sent since voice stream was opened. |
| Rcvr Packets | Number of RTP
                                             				voice packets received since voice stream was opened. Note This number
                                                         				  is not necessarily identical to the number of RTP voice packets received since
                                                         				  the call began because the call might have been placed on hold. | Note | This number
                                                         				  is not necessarily identical to the number of RTP voice packets received since
                                                         				  the call began because the call might have been placed on hold. |
| Note | This number
                                                         				  is not necessarily identical to the number of RTP voice packets received since
                                                         				  the call began because the call might have been placed on hold. |
| Sender Packets | Number of RTP
                                             				voice packets transmitted since voice stream was opened. Note This number
                                                         				  is not necessarily identical to the number of RTP voice packets transmitted
                                                         				  since the call began because the call might have been placed on hold. | Note | This number
                                                         				  is not necessarily identical to the number of RTP voice packets transmitted
                                                         				  since the call began because the call might have been placed on hold. |
| Note | This number
                                                         				  is not necessarily identical to the number of RTP voice packets transmitted
                                                         				  since the call began because the call might have been placed on hold. |
| Avg Jitter | Estimated
                                             				average RTP packet jitter (dynamic delay that a packet encounters when going
                                             				through the network) observed since the receiving voice stream was opened. |
| Max Jitter | Maximum jitter
                                             				observed since the receiving voice stream was opened. |
| Rcvr Discarded | Number of RTP
                                             				packets discarded by the receiver. |
| Rcvr Lost
                                             				Packets | Missing RTP
                                             				packets (lost in transit). |
| Voice Quality Metrics |
| MOS LQK | Score that is
                                             				an objective estimate of the mean opinion score (MOS) for listening quality
                                             				(LQK) that rates from 5 (excellent) to 1 (bad). This score is based on audible
                                             				concealment events due to frame loss in the preceding 8-second interval of the
                                             				voice stream. |
| Avg MOS LQK | Average MOS
                                             				LQK score observed for the entire voice stream. |
| Min MOS LQK | Lowest MOS
                                             				LQK score observed from start of the voice stream. |
| Max MOS LQK | Baseline or
                                             				highest MOS LQK score observed from start of the voice stream. |
| Cumulative
                                             				Conceal Ratio | Total number
                                             				of concealment frames divided by total number of speech frames received from
                                             				start of the voice stream. |
| Max Conceal
                                             				Ratio | Maximum
                                             				concealment ratio that is observed during the call. |
| Conceal Secs | Number of
                                             				seconds that have concealment events (lost frames) from the start of the voice
                                             				stream (includes severely concealed seconds). |
| Severely
                                             				Conceal Secs | Number of
                                             				seconds that have more than 5 percent concealment events (lost frames) from the
                                             				start of the voice stream. |
| Latency | Estimate of
                                             				the network latency, expressed in milliseconds. Represents a running average of
                                             				the round-trip delay, measured when RTCP receiver report blocks are received. |

| Note | This number
                                                         				  is not necessarily identical to the number of RTP voice packets received since
                                                         				  the call began because the call might have been placed on hold. |
|---|---|

| Note | This number
                                                         				  is not necessarily identical to the number of RTP voice packets transmitted
                                                         				  since the call began because the call might have been placed on hold. |
|---|---|

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Select Status . |
| Step 3 | Select Call Statistics . |