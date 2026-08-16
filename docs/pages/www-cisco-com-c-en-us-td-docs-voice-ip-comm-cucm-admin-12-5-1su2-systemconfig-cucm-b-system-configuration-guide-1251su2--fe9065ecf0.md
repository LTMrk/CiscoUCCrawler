---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su2-systemconfig-cucm-b-system-configuration-guide-1251su2--fe9065ecf0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU2/systemConfig/cucm_b_system-configuration-guide-1251su2/cucm_b_system-configuration-guide-for-cisco-1251su2_chapter_01100.html
retrieved_at: 2026-08-16T17:44:07.963336+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: July 31, 2025

Chapter: Configure Conference Bridges

## Chapter: Configure Conference Bridges

# Configure Conference Bridges

## Conference Bridges
                        	 Overview

Conference bridge
                              		  for Cisco Unified Communications Manager is a software or hardware application
                              		  that is designed to allow both ad hoc and meet-me voice conferencing.
                              		  Additional conference bridge types support other types of conferences,
                              		  including video conferences. Each conference bridge can host several
                              		  simultaneous, multiparty conferences. Both hardware and software conference
                              		  bridges can be active at the same time. Software and hardware conference
                              		  bridges differ in the number of streams and the types of codec that they
                              		  support. When you add a new server, the system automatically adds software
                              		  conference bridges.

When Cisco Unified Communications Manager server is
                                          			 created, the Conference Bridge Software is also created automatically and it
                                          			 cannot be deleted. You cannot add Conference Bridge Software to Cisco Unified Communications Manager Administration.

## Conference Bridge
                        	 Types

The
                              		  following conference bridge types are available in Cisco Unified
                                 			 Communications Manager Administration .

Conference
                                          					 Bridge Type

Description

Cisco
                                          					 Conference Bridge Hardware

This type
                                          					 supports the Cisco Catalyst 4000 and 6000 Voice Gateway Modules and the
                                          					 following number of conference sessions:

G.711 or G.729a conference - 32 participants per port; six participants maximum per conference; 256 total participants per
                                                      module; 10 bridges with three participants.

GSM - 24 participants per port; six participants maximum per conference; 192 total participants per module.

G.711 conference only - 24 conference participants; maximum of
                                                							 four conferences with six participants each.

Cisco
                                          					 Conference Bridge Software

Software
                                          					 conference devices support G.711 codecs by default.

The maximum number of callers for this type equals 256. With a setting of 256, the software conference bridge can support
                                          64 conference sessions of 4 parties each. The maximum number of caller parties in a conference session is specified via the Maximum Ad Hoc Conference and Maximum MeetMe Conference Unicast service parameters.

Caution

This type of conference bridge (SW Conference Bridge) is a simplified implementation. It does not identify parties that are
                                                      silent and uses a simple summing algorithm that may cause audio quality and low volume levels for the conference when there
                                                      is a large number of participants.

Cisco IOS
                                          					 Conference Bridge

Uses the NM-HDV or NM-HDV-FARM network modules.

G.711 a/mu-law, G.729, G.729a, G.729b, and G.729ab participants can join in a single conference call

Up to six parties can join in a single conference call

Cisco Unified Communications Manager assigns
                                          					 conference resources to calls on a dynamic basis.

For more
                                          					 information about Cisco IOS Conferencing and Transcoding for Voice Gateway
                                          					 Routers, see the Cisco IOS documentation that you received with this product.

Cisco IOS
                                          					 Enhanced Bridges

Uses the onboard Cisco Packet Voice/Fax Digital Signal Processor Modules (PVDM2) on the Cisco 2800 and 3800 series voice gateway
                                                routers or uses the NM-HD or NM-HDV2 network modules.

G.711 a-law/mu-law, G.729, G.729a, G.729b, G.729ab, GSM FR, and GSM EFR participants can join in a single conference

Up to eight parties can join in a single call.

With ISR4000 router and any of the SM-X-PVDM-3000/ SM-X-PVDM-2000/ SM-X-PVDM-1000/ SM-X-PVDM-500, each Conference Bridge Profile
                                                      can register up to a maximum of 512 sessions, due to the Unified Communications Manager 4096 maximum stream limitation.

Cisco Unified Communications Manager assigns
                                          					 conference resources to calls on a dynamic basis.

For more
                                          					 information about Cisco IOS Enhanced Conferencing and Transcoding for Voice
                                          					 Gateway Routers, see the Cisco IOS documentation that you received with this
                                          					 product.

This conference bridge type supports SRTP media encryption with
                                          AES_CM_128_HMAC_SHA1_80 for supported SIP phones where an ISR 4000 series gateway is deployed. SCCP phones and
                                          non-supported SIP phones fall back to AES_CM_128_HMAC_SHA1_32
                                          encryption.

Make sure that the gateway load supports the cipher. Please
                                                      review your gateway documentation for support details.

Cisco
                                          					 Conference Bridge (WS-SVC-CMM)

This
                                          					 conference bridge type supports the Cisco Catalyst 6500 series and Cisco 7600
                                          					 series Communication Media Module (CMM).

It supports up to eight parties per conference and up to 64 conferences per port adapter. This conference bridge type supports
                                          the following codecs: This conference bridge type supports on demand conferencing.

G.711 a-law/mu-law

G.729 annex A and annex B

G.723.1

Cisco
                                          					 Video Conference Bridge (IPVC-35xx)

The Cisco
                                          					 Video Conference Bridge provides audio and video conferencing functions for
                                          					 Cisco IP video phones, H.323 endpoints, and audio-only Cisco Unified IP
                                             						Phone s. The Cisco Video Conference Bridge supports the H.261, H.263,
                                          					 and H.264 codecs for video.

Cisco
                                          					 TelePresence MCU

Cisco
                                          					 TelePresence MCU is a set of hardware conference bridges for Cisco Unified
                                             						Communications Manager .

The
                                          					 Cisco TelePresence MCU is a high-definition (HD) multipoint video conferencing
                                          					 bridge. It delivers up to 1080p at 30 frames per second, full continuous
                                          					 presence for all conferences, full transcoding, and is ideal for mixed HD
                                          					 endpoint environments.

The Cisco TelePresence MCU supports SIP as the signaling call control protocol. It has a built-in Web Server that allows for
                                          complete configuration, control, and monitoring of the system and conferences. The Cisco TelePresence MCU provides an XML
                                          management API over HTTP.

Cisco TelePresence MCU allows both on demand and meet-me voice and video conferencing. Each conference bridge can host several
                                          simultaneous, multiparty conferences.

Cisco
                                             						Unified Communications Manager supports presentation sharing with the
                                          					 Binary Floor Control Protocol (BFCP) between Unified Communications
                                             						Manager and a Cisco TelePresence MCU.

Cisco
                                          					 TelePresence MCU must be configured in Port Reservation mode. For more
                                          					 information, consult the Cisco TelePresence MCU Configuration Guide .

Cisco
                                                      						TelePresence MCU does not support a common out-of-band DTMF method. Under the
                                                      						default setting, Cisco Unified
                                                         						  Communications Manager will not require a Media Termination Point
                                                      						(MTP). However, if the Media Termination Point Required check box is checked, Cisco Unified
                                                         						  Communications Manager will allocate an MTP and the SIP trunk will
                                                      						negotiate DTMF according to RFC 2833.

Cisco
                                          					 TelePresence Conductor

Cisco TelePresence Conductor provides intelligent conference administrative controls and is scalable, supporting device clustering
                                          for load balancing across MCUs and multiple device availabilities. Administrators can implement the Cisco TelePresence Conductor
                                          as either an appliance or a virtualized application on VMware with support for Cisco Unified Computing System (Cisco UCS)
                                          platforms or third-party-based platforms.

Cisco TelePresence Conductor dynamically selects the most appropriate Cisco TelePresence resource for each new conference.
                                          On demand, "MeetMe" , and scheduled voice and video conferences can dynamically grow and exceed the capacity of individual MCUs. Up to three Cisco
                                          TelePresence Conductor appliances or virtualized applications may be clustered to provide greater resilience. One Cisco TelePresence
                                          Conductor appliance or Cisco TelePresence Conductor cluster has a system capacity of 30 MCUs or 2400 MCU ports.

Cisco Meeting Server

The Cisco Meeting Server conference bridge solution allows Ad Hoc, Meet-Me, Conference Now, and Rendezvous conferences. This
                                          conference bridge offers premises-based audio, video, and web conferencing, and works with third-party on-premises infrastructure.
                                          It scales for small or large deployments. You can add capacity incrementally as needed, to ensure that you can support the
                                          current and future needs of your organization. This conference bridge provides advanced interoperability. Any number of participants
                                          can create and join meetings from:

Cisco or third-party room or desktop video systems

Cisco Jabber Client

Cisco Meeting App (can be native or with a WebRTC compatible browser)

Skype for Business

A minimum release of Cisco Meeting Server 2.0 is required to use the Cisco Meeting Server conference bridge.

The Cisco Meeting Server supports SIP as the signaling call control protocol. It has a built-in Web Server that allows for
                                          complete configuration, control, and monitoring of the system and conferences. The Cisco Meeting Server provides an XML management
                                          API over HTTP.

Cisco Meeting Server does not support H.265 video codec and Far End camera Control.

## Conference Bridge
                        	 Configuration Task Flow

Step 1

Configure Conference Bridges

Configure a
                                          				hardware or software conference bridge to allow ad hoc and meet-me voice
                                          				conferencing.

Step 2

Configure Service Parameters for Conference Bridges

Perform this
                                          				procedure when your network includes both Cisco IOS Conference Bridge and Cisco
                                          				IOS Enhanced Conference Bridge.

Step 3

Configure SIP Trunk Connection to Conference Bridge

Perform this procedure to configure a SIP trunk connection to your conference bridge.

### Configure
                           	 Conference Bridges

You must configure a hardware or software conference bridge to allow
                                 		  ad hoc and meet-me voice conferencing.

Step 1

From Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Conference Bridge .

Step 2

Click Add
                                             				New .

Step 3

Configure the
                                          			 fields in the Conference Bridge Configuration window. For detailed
                                          			 field descriptions, refer to the online help.

Step 4

Click Save .

#### What to do next

If your network
                                 		  includes both Cisco IOS Conference Bridge and Cisco IOS Enhanced Conference
                                 		  Bridge, Configure Service Parameters for Conference Bridges .

### Configure Service
                           	 Parameters for Conference Bridges

Perform this procedure when your network includes both Cisco IOS
                                 		  Conference Bridge and Cisco IOS Enhanced Conference Bridge.

Step 1

From Cisco Unified CM
                                          			 Administration, choose System > Service
                                                				  Parameters .

Step 2

In the Service Parameter Configuration window, choose a server
                                          			 and choose the Cisco CallManager service.

Step 3

In the Clusterwide Parameters (Features - Conference) section, set
                                          			 the following parameters to 6:

- Maximum Ad Hoc
                                             				Conference

- Maximum MeetMe
                                             				Conference Unicast

Step 4

Click Save .

### Configure SIP
                           	 Trunk Connection to Conference Bridge

Step 1

From Cisco
                                          			 Unified CM Administration, choose Device > Trunk

Step 2

Complete one
                                          			 of the following steps:

- To create a new SIP trunk,
                                             				click Add
                                                				  New .

- To add the connection to an
                                             				existing trunk, click Find and select the appropriate trunk.

Step 3

Select the Device
                                             				Protocol as SIP .

Step 4

Select the Trunk
                                             				Service Type as None .

Step 5

Create an
                                          			 entry for the conference bridge in the Destination area by adding the IP address or
                                          			 hostname for the conference bridge. If you need a new line, you can
                                          			 click (+) to add it.

Step 6

From the Normalization Script drop-down list box, select a
                                          			 normalization script. For example, the following scripts are mandatory

- cisco-telepresence-conductor-interop – select this
                                             				script if you are connecting this trunk to a Cisco TelePresence Conductor.

- cisco-telepresence-mcu-ts-direct-interop – select
                                             				this script if you are connecting this trunk to a Cisco TelePresence MCU.

- cisco-meeting-server-interop – select this script if
                                             				you are connecting this trunk to a Cisco Meeting Server.

Step 7

Complete any
                                          			 remaining fields in the Trunk Configuration window. For help with the fields
                                          			 and their settings, refer to the online help.

Step 8

Click Save.

| Note | When Cisco Unified Communications Manager server is
                                          			 created, the Conference Bridge Software is also created automatically and it
                                          			 cannot be deleted. You cannot add Conference Bridge Software to Cisco Unified Communications Manager Administration. |
|---|---|

| Conference
                                          					 Bridge Type | Description |
|---|---|
| Cisco
                                          					 Conference Bridge Hardware | This type
                                          					 supports the Cisco Catalyst 4000 and 6000 Voice Gateway Modules and the
                                          					 following number of conference sessions: Cisco
                                             						  Catalyst 6000 G.711 or G.729a conference - 32 participants per port; six participants maximum per conference; 256 total participants per
                                                      module; 10 bridges with three participants. GSM - 24 participants per port; six participants maximum per conference; 192 total participants per module. Cisco
                                             						  Catalyst 4000 G.711 conference only - 24 conference participants; maximum of
                                                							 four conferences with six participants each. |
| Cisco
                                          					 Conference Bridge Software | Software
                                          					 conference devices support G.711 codecs by default. The maximum number of callers for this type equals 256. With a setting of 256, the software conference bridge can support
                                          64 conference sessions of 4 parties each. The maximum number of caller parties in a conference session is specified via the Maximum Ad Hoc Conference and Maximum MeetMe Conference Unicast service parameters. Caution This type of conference bridge (SW Conference Bridge) is a simplified implementation. It does not identify parties that are
                                                      silent and uses a simple summing algorithm that may cause audio quality and low volume levels for the conference when there
                                                      is a large number of participants. | Caution | This type of conference bridge (SW Conference Bridge) is a simplified implementation. It does not identify parties that are
                                                      silent and uses a simple summing algorithm that may cause audio quality and low volume levels for the conference when there
                                                      is a large number of participants. |
| Caution | This type of conference bridge (SW Conference Bridge) is a simplified implementation. It does not identify parties that are
                                                      silent and uses a simple summing algorithm that may cause audio quality and low volume levels for the conference when there
                                                      is a large number of participants. |
| Cisco IOS
                                          					 Conference Bridge | Uses the NM-HDV or NM-HDV-FARM network modules. G.711 a/mu-law, G.729, G.729a, G.729b, and G.729ab participants can join in a single conference call Up to six parties can join in a single conference call Cisco Unified Communications Manager assigns
                                          					 conference resources to calls on a dynamic basis. For more
                                          					 information about Cisco IOS Conferencing and Transcoding for Voice Gateway
                                          					 Routers, see the Cisco IOS documentation that you received with this product. |
| Cisco IOS
                                          					 Enhanced Bridges | Uses the onboard Cisco Packet Voice/Fax Digital Signal Processor Modules (PVDM2) on the Cisco 2800 and 3800 series voice gateway
                                                routers or uses the NM-HD or NM-HDV2 network modules. G.711 a-law/mu-law, G.729, G.729a, G.729b, G.729ab, GSM FR, and GSM EFR participants can join in a single conference Up to eight parties can join in a single call. Note With ISR4000 router and any of the SM-X-PVDM-3000/ SM-X-PVDM-2000/ SM-X-PVDM-1000/ SM-X-PVDM-500, each Conference Bridge Profile
                                                      can register up to a maximum of 512 sessions, due to the Unified Communications Manager 4096 maximum stream limitation. Cisco Unified Communications Manager assigns
                                          					 conference resources to calls on a dynamic basis. For more
                                          					 information about Cisco IOS Enhanced Conferencing and Transcoding for Voice
                                          					 Gateway Routers, see the Cisco IOS documentation that you received with this
                                          					 product. This conference bridge type supports SRTP media encryption with
                                          AES_CM_128_HMAC_SHA1_80 for supported SIP phones where an ISR 4000 series gateway is deployed. SCCP phones and
                                          non-supported SIP phones fall back to AES_CM_128_HMAC_SHA1_32
                                          encryption. Note Make sure that the gateway load supports the cipher. Please
                                                      review your gateway documentation for support details. | Note | With ISR4000 router and any of the SM-X-PVDM-3000/ SM-X-PVDM-2000/ SM-X-PVDM-1000/ SM-X-PVDM-500, each Conference Bridge Profile
                                                      can register up to a maximum of 512 sessions, due to the Unified Communications Manager 4096 maximum stream limitation. | Note | Make sure that the gateway load supports the cipher. Please
                                                      review your gateway documentation for support details. |
| Note | With ISR4000 router and any of the SM-X-PVDM-3000/ SM-X-PVDM-2000/ SM-X-PVDM-1000/ SM-X-PVDM-500, each Conference Bridge Profile
                                                      can register up to a maximum of 512 sessions, due to the Unified Communications Manager 4096 maximum stream limitation. |
| Note | Make sure that the gateway load supports the cipher. Please
                                                      review your gateway documentation for support details. |
| Cisco
                                          					 Conference Bridge (WS-SVC-CMM) | This
                                          					 conference bridge type supports the Cisco Catalyst 6500 series and Cisco 7600
                                          					 series Communication Media Module (CMM). It supports up to eight parties per conference and up to 64 conferences per port adapter. This conference bridge type supports
                                          the following codecs: This conference bridge type supports on demand conferencing. G.711 a-law/mu-law G.729 annex A and annex B G.723.1 |
| Cisco
                                          					 Video Conference Bridge (IPVC-35xx) | The Cisco
                                          					 Video Conference Bridge provides audio and video conferencing functions for
                                          					 Cisco IP video phones, H.323 endpoints, and audio-only Cisco Unified IP
                                             						Phone s. The Cisco Video Conference Bridge supports the H.261, H.263,
                                          					 and H.264 codecs for video. |
| Cisco
                                          					 TelePresence MCU | Cisco
                                          					 TelePresence MCU is a set of hardware conference bridges for Cisco Unified
                                             						Communications Manager . The
                                          					 Cisco TelePresence MCU is a high-definition (HD) multipoint video conferencing
                                          					 bridge. It delivers up to 1080p at 30 frames per second, full continuous
                                          					 presence for all conferences, full transcoding, and is ideal for mixed HD
                                          					 endpoint environments. The Cisco TelePresence MCU supports SIP as the signaling call control protocol. It has a built-in Web Server that allows for
                                          complete configuration, control, and monitoring of the system and conferences. The Cisco TelePresence MCU provides an XML
                                          management API over HTTP. Cisco TelePresence MCU allows both on demand and meet-me voice and video conferencing. Each conference bridge can host several
                                          simultaneous, multiparty conferences. Cisco
                                             						Unified Communications Manager supports presentation sharing with the
                                          					 Binary Floor Control Protocol (BFCP) between Unified Communications
                                             						Manager and a Cisco TelePresence MCU. Cisco
                                          					 TelePresence MCU must be configured in Port Reservation mode. For more
                                          					 information, consult the Cisco TelePresence MCU Configuration Guide . Note Cisco
                                                      						TelePresence MCU does not support a common out-of-band DTMF method. Under the
                                                      						default setting, Cisco Unified
                                                         						  Communications Manager will not require a Media Termination Point
                                                      						(MTP). However, if the Media Termination Point Required check box is checked, Cisco Unified
                                                         						  Communications Manager will allocate an MTP and the SIP trunk will
                                                      						negotiate DTMF according to RFC 2833. | Note | Cisco
                                                      						TelePresence MCU does not support a common out-of-band DTMF method. Under the
                                                      						default setting, Cisco Unified
                                                         						  Communications Manager will not require a Media Termination Point
                                                      						(MTP). However, if the Media Termination Point Required check box is checked, Cisco Unified
                                                         						  Communications Manager will allocate an MTP and the SIP trunk will
                                                      						negotiate DTMF according to RFC 2833. |
| Note | Cisco
                                                      						TelePresence MCU does not support a common out-of-band DTMF method. Under the
                                                      						default setting, Cisco Unified
                                                         						  Communications Manager will not require a Media Termination Point
                                                      						(MTP). However, if the Media Termination Point Required check box is checked, Cisco Unified
                                                         						  Communications Manager will allocate an MTP and the SIP trunk will
                                                      						negotiate DTMF according to RFC 2833. |
| Cisco
                                          					 TelePresence Conductor | Cisco TelePresence Conductor provides intelligent conference administrative controls and is scalable, supporting device clustering
                                          for load balancing across MCUs and multiple device availabilities. Administrators can implement the Cisco TelePresence Conductor
                                          as either an appliance or a virtualized application on VMware with support for Cisco Unified Computing System (Cisco UCS)
                                          platforms or third-party-based platforms. Cisco TelePresence Conductor dynamically selects the most appropriate Cisco TelePresence resource for each new conference.
                                          On demand, "MeetMe" , and scheduled voice and video conferences can dynamically grow and exceed the capacity of individual MCUs. Up to three Cisco
                                          TelePresence Conductor appliances or virtualized applications may be clustered to provide greater resilience. One Cisco TelePresence
                                          Conductor appliance or Cisco TelePresence Conductor cluster has a system capacity of 30 MCUs or 2400 MCU ports. |
| Cisco Meeting Server | The Cisco Meeting Server conference bridge solution allows Ad Hoc, Meet-Me, Conference Now, and Rendezvous conferences. This
                                          conference bridge offers premises-based audio, video, and web conferencing, and works with third-party on-premises infrastructure.
                                          It scales for small or large deployments. You can add capacity incrementally as needed, to ensure that you can support the
                                          current and future needs of your organization. This conference bridge provides advanced interoperability. Any number of participants
                                          can create and join meetings from: Cisco or third-party room or desktop video systems Cisco Jabber Client Cisco Meeting App (can be native or with a WebRTC compatible browser) Skype for Business A minimum release of Cisco Meeting Server 2.0 is required to use the Cisco Meeting Server conference bridge. The Cisco Meeting Server supports SIP as the signaling call control protocol. It has a built-in Web Server that allows for
                                          complete configuration, control, and monitoring of the system and conferences. The Cisco Meeting Server provides an XML management
                                          API over HTTP. Note Cisco Meeting Server does not support H.265 video codec and Far End camera Control. | Note | Cisco Meeting Server does not support H.265 video codec and Far End camera Control. |
| Note | Cisco Meeting Server does not support H.265 video codec and Far End camera Control. |

| Caution | This type of conference bridge (SW Conference Bridge) is a simplified implementation. It does not identify parties that are
                                                      silent and uses a simple summing algorithm that may cause audio quality and low volume levels for the conference when there
                                                      is a large number of participants. |
|---|---|

| Note | With ISR4000 router and any of the SM-X-PVDM-3000/ SM-X-PVDM-2000/ SM-X-PVDM-1000/ SM-X-PVDM-500, each Conference Bridge Profile
                                                      can register up to a maximum of 512 sessions, due to the Unified Communications Manager 4096 maximum stream limitation. |
|---|---|

| Note | Make sure that the gateway load supports the cipher. Please
                                                      review your gateway documentation for support details. |
|---|---|

| Note | Cisco
                                                      						TelePresence MCU does not support a common out-of-band DTMF method. Under the
                                                      						default setting, Cisco Unified
                                                         						  Communications Manager will not require a Media Termination Point
                                                      						(MTP). However, if the Media Termination Point Required check box is checked, Cisco Unified
                                                         						  Communications Manager will allocate an MTP and the SIP trunk will
                                                      						negotiate DTMF according to RFC 2833. |
|---|---|

| Note | Cisco Meeting Server does not support H.265 video codec and Far End camera Control. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Conference Bridges | Configure a
                                          				hardware or software conference bridge to allow ad hoc and meet-me voice
                                          				conferencing. |
| Step 2 | Configure Service Parameters for Conference Bridges | Perform this
                                          				procedure when your network includes both Cisco IOS Conference Bridge and Cisco
                                          				IOS Enhanced Conference Bridge. |
| Step 3 | Configure SIP Trunk Connection to Conference Bridge | Perform this procedure to configure a SIP trunk connection to your conference bridge. |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Media
                                                				  Resources > Conference Bridge . |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | Configure the
                                          			 fields in the Conference Bridge Configuration window. For detailed
                                          			 field descriptions, refer to the online help. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM
                                          			 Administration, choose System > Service
                                                				  Parameters . |
|---|---|
| Step 2 | In the Service Parameter Configuration window, choose a server
                                          			 and choose the Cisco CallManager service. |
| Step 3 | In the Clusterwide Parameters (Features - Conference) section, set
                                          			 the following parameters to 6: Maximum Ad Hoc
                                             				Conference Maximum MeetMe
                                             				Conference Unicast |
| Step 4 | Click Save . |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose Device > Trunk |
|---|---|
| Step 2 | Complete one
                                          			 of the following steps: To create a new SIP trunk,
                                             				click Add
                                                				  New . To add the connection to an
                                             				existing trunk, click Find and select the appropriate trunk. |
| Step 3 | Select the Device
                                             				Protocol as SIP . |
| Step 4 | Select the Trunk
                                             				Service Type as None . |
| Step 5 | Create an
                                          			 entry for the conference bridge in the Destination area by adding the IP address or
                                          			 hostname for the conference bridge. If you need a new line, you can
                                          			 click (+) to add it. |
| Step 6 | From the Normalization Script drop-down list box, select a
                                          			 normalization script. For example, the following scripts are mandatory cisco-telepresence-conductor-interop – select this
                                             				script if you are connecting this trunk to a Cisco TelePresence Conductor. cisco-telepresence-mcu-ts-direct-interop – select
                                             				this script if you are connecting this trunk to a Cisco TelePresence MCU. cisco-meeting-server-interop – select this script if
                                             				you are connecting this trunk to a Cisco Meeting Server. |
| Step 7 | Complete any
                                          			 remaining fields in the Trunk Configuration window. For help with the fields
                                          			 and their settings, refer to the online help. |
| Step 8 | Click Save. |