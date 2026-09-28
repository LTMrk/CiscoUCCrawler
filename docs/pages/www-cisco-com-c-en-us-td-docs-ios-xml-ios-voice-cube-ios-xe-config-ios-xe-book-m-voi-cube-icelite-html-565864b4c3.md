---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cube-icelite-html-565864b4c3
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cube-icelite.html
retrieved_at: 2026-08-16T15:51:19.664672+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: ICE-Lite Support

## Chapter: ICE-Lite Support

# ICE-Lite Support

## ICE-Lite Support
                        	 on CUBE

Interactive
                           		Connectivity Establishment (ICE) is a protocol for Network Address Translator
                           		(NAT) traversal for UDP-based multimedia sessions established with the
                           		offer-answer model. ICE makes use of the Session Traversal Utilities for NAT
                           		(STUN) protocol and its extension, Traversal Using Relay NAT (TURN), and can be
                           		used by any protocol utilizing the offer-answer model, such as the Session
                           		Initiation Protocol (SIP).

The ICE-Lite Support
                           		on CUBE feature enables the remote peers of CUBE (that may be behind a NAT and
                           		doing ICE) to use the ICE semantics in the session description protocol (SDP)
                           		and perform an offer-answer exchange of SDP messages. The CUBE can also
                           		interwork with endpoints that support or do not support ICE. ICE agents
                           		(devices) that are always attached to the public Internet have a special type
                           		of implementation called Lite. CUBE will be in ICE-lite mode only. CUBE
                           		supports the ICE-lite feature from Cisco IOS Release 15.5(2)S.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Releases

Feature
                                             					 Information

ICE-Lite
                                             					 Support on CUBE

Cisco IOS
                                             					 15.5(3)M

Cisco IOS
                                             					 XE 3.16S

The
                                             					 ICE-Lite Support on CUBE feature enables the remote peers of CUBE (that may be
                                             					 behind a NAT and doing ICE) to use the ICE semantics in the session description
                                             					 protocol (SDP) and perform an offer-answer exchange of SDP messages. The CUBE
                                             					 can also interwork with endpoints that support or do not support ICE. ICE
                                             					 agents (devices) that are always attached to the public Internet have a special
                                             					 type of implementation called Lite. CUBE will be in ICE-lite mode only.

The
                                             					 following commands were introduced or modified: debug voip
                                                   						  icelib , show voip ice
                                                   						  global-stats , show voip ice instance
                                                   						  call-id call-id , show voip ice
                                                   						  summary , and stun usage
                                                   						  ice

### Characteristics

The following are some of the key characteristics of ICE-lite.

A CLI configured for ICE-lite.

Support for ICE-lite in the contact header with a media-tag option of REGISTER message (as per RFC 5768).

ICE-lite feature is in compliance with section 4.2 of RFC 7584, with CUBE acting as ICE termination Back-to-Back UA.

CUBE accepts Full ICE Offer and responds in ICE-lite mode.

CUBE responds to mid call updates or early dialog updates with changes to SDP parameters, and which requires ICE to restart.

For outbound offer from CUBE, a Session Description Protocol (SDP) with ICE-lite semantics is sent.

ICE protocol verifies all types of media streams (audio, video, application media lines) and components (RTP, RTCP), wherever
                                    applicable.

### ICE
                           	 Candidate

To execute ICE, an agent has to
                              		identify all of its address candidates. A candidate is a transport address—a
                              		combination of IP address and port for a transport protocol, such as UDP. A
                              		candidate can be derived from physical or logical network interfaces, or
                              		discoverable using STUN and TURN. A viable candidate is a transport address
                              		obtained directly from a local interface; such a candidate is called a host
                              		candidate. The local interface could be ethernet or WiFi, or it could be one
                              		that is obtained through a tunnel mechanism, such as a Virtual Private Network
                              		(VPN) or Mobile IP (MIP). In all cases, such a network interface appears to the
                              		agent as a local interface from which ports (and thus candidates) can be
                              		allocated.

### ICE Lite

ICE agents (devices)
                              		that are always attached to the public Internet have a special type of
                              		implementation called Lite. For ICE to be used in a call, both the endpoints
                              		(agents) must support it. An ICE agent that supports Lite neither gathers ICE
                              		candidates nor triggers ICE connectivity checks; however, the agent responds to
                              		connectivity checks and includes only host candidates for any media stream. An
                              		ICE agent that supports the lite mode is called an ICE-lite endpoint.

### High Availability
                           	 Support with ICE

High availability (HA) is
                              		supported only for audio calls that use ICE. For video calls, as the size of
                              		SDP is larger, HA will not work. Some of the design considerations are the
                              		following:

No new checkpoint module for
                                    			 ICE instance.

ICE instance will be re-created on the standby device from SIP HA
                                    			 re-creation path by using source SDP, destination SDP, and configuration
                                    			 profile.

As no information related to ICE is checkpointed, in the standby
                                    			 device, the ICE valid list (created after connectivity checks are done) is
                                    			 populated from currently used media address.

## Restrictions for ICE-lite Support

The following
                           		features are not supported with ICE:

IPv6

Alternative
                                 			 Network Address Types (ANAT)

ANAT-ICE interworking

Media
                                 			 anti-trombone

High
                                 			 availability support for video calls

Codec
                                 			 Transparent

SDP passthrough

Media
                                 			 flow-around

Resource
                                 			 Reservation Protocol (RSVP)

SIP-to-TDM
                                 			 gateway support

A workaround option for ICE-lite based media optimization is to configure loopback dial-peer on a TDM gateway. Contact Account
                                             or TAC teams for further technical details.

Media
                                 			 Termination Point (MTP)

VXML and TCL
                                 			 Scripts

## Configure ICE-Lite

ICE lite can be configured under STUN, and the decision to use ICE for a session is based on the offer/answer. This configuration
                              is used for outbound dial-peers of CUBE to decide whether to offer ICE in SDP or not. For an incoming offer, the decision to do ICE is based on what the remote end
                              offers in SDP.

### SUMMARY STEPS

- enable

- configure terminal

- voice class stun-usage tag

- stun usage ice lite

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables
                                          				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

voice class stun-usage tag

### Example:

```
Device(config)# voice class stun-usage 5
```

Sets STUN
                                          				usage global parameters, and enters voice class configuration mode.

Step 4

stun usage ice lite

### Example:

```
Device(config-class)# stun usage ice lite
```

Configures ICE in ICE-Lite mode.

Step 5

end

### Example:

```
Device(config-class)# end
```

Returns to
                                          				privileged EXEC mode.

## Verify ICE-Lite (Success Flow Calls)

The following show commands
                              		  can be used to verify ICE for success flow calls. The show commands can be entered in any order.

### SUMMARY STEPS

- show call
                                    				  active video compact

- show voip
                                    				  rtp connections

- show voip
                                    				  ice instance call-id call-id-1

- show voip
                                    				  ice instance call-id call-id-2

- show voip
                                    				  ice summary

- show voip
                                    				  ice global-stats

### DETAILED STEPS

Step 1

show call
                                             				  active video compact

### Example:

```
Device# show call active video compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 4
        25 ANS     T189   H264       VOIP-VIDEO   P8181     72.163.212.137:2328
        30 ORG     T189   H264       VOIP-VIDEO   P9191         9.45.46.16:8028
        35 ANS     T189   H264       VOIP-VIDEO   P8181         9.45.46.16:8008
        36 ORG     T189   H264       VOIP-VIDEO   P9191     72.163.212.163:2328
```

Step 2

show voip
                                             				  rtp connections

The following
                                          				sample output displays the VoIP RTP usage information and RTP active
                                          				connections.

### Example:

```
Device# show voip rtp connections VoIP RTP Port Usage Information:
Max Ports Available: 19999, Ports Reserved: 101, Ports in Use: 20
                                        Min   Max   Ports     Ports     Ports
Media-Address Range                     Port  Port  Available Reserved  In-use
------------------------------------------------------------------------------
Global Media Pool                       8000  48198 19999     101       20
------------------------------------------------------------------------------
VoIP RTP active connections :
No. CallId dstCallLocalRTP RmtRTP   LocalIP             RemoteIP          MPSS
1   25     30     8000     2326     10.104.45.107       72.163.212.137    NO
2   26     31     8002     2328     10.104.45.107       72.163.212.137    NO
3   27     32     8036     2454     10.104.45.107       72.163.212.137    NO
4   28     33     8004     2330     10.104.45.107       72.163.212.137    NO
5   29     34     8038     2332     10.104.45.107       72.163.212.137    NO
6   30     25     8006     8016     9.45.46.16          9.45.46.16        NO
7   31     26     8008     8028     9.45.46.16          9.45.46.16        NO
8   32     27     8010     8030     9.45.46.16          9.45.46.16        NO
9   33     28     8012     8032     9.45.46.16          9.45.46.16        NO
10  34     29     8014     8034     9.45.46.16          9.45.46.16        NO
11  35     36     8016     8006     9.45.46.16          9.45.46.16        NO
12  36     35     8018     2326     10.104.45.107       72.163.212.163    NO
13  37     41     8020     2328     10.104.45.107       72.163.212.163    NO
14  38     42     8022     2454     10.104.45.107       72.163.212.163    NO
15  39     43     8024     2330     10.104.45.107       72.163.212.163    NO
16  40     44     8026     2332     10.104.45.107       72.163.212.163    NO
17  41     37     8028     8008     9.45.46.16          9.45.46.16        NO
18  42     38     8030     8010     9.45.46.16          9.45.46.16        NO
19  43     39     8032     8012     9.45.46.16          9.45.46.16        NO
20  44     40     8034     8014     9.45.46.16          9.45.46.16        NO
Found 20 active RTP connections
```

Step 3

show voip
                                             				  ice instance call-id call-id-1

The following
                                          				sample output displays the active ICE sessions on the ICE-full and the ICE-lite
                                          				legs where there are ICE negotiations.

### Example:

```
Device# show voip ice instance call-id 25 Interactive Connectivity Check(ICE) Instance details:
Call-ID is 25
Instance is 0x7FC617FC0508
Overall ICE-State is COMPLETED
LocalAgent's mode is ICE-CONTROLLED
RemoteAgent's mode is ICE-CONTROLLING
m-line:1
---------
ICE-State: ACTIVE
NominatedPairs:
LocalIP 10.104.45.107   port 8000  type host         RemoteIP 72.163.212.137  port 2326  type host

m-line:2
---------
ICE-State: ACTIVE
NominatedPairs:
LocalIP 10.104.45.107   port 8002  type host         RemoteIP 72.163.212.137  port 2328  type host
LocalIP 10.104.45.107   port 8003  type host         RemoteIP 72.163.212.137  port 2329  type host

m-line:3
---------
ICE-State: ACTIVE
NominatedPairs:
LocalIP 10.104.45.107   port 8036  type host         RemoteIP 72.163.212.137  port 2454  type host

m-line:4
---------
ICE-State: ACTIVE
NominatedPairs:
LocalIP 10.104.45.107   port 8004  type host         RemoteIP 72.163.212.137  port 2330  type host
LocalIP 10.104.45.107   port 8005  type host         RemoteIP 72.163.212.137  port 2331  type host

m-line:5
---------
ICE-State: ACTIVE
NominatedPairs:
LocalIP 10.104.45.107   port 8038  type host         RemoteIP 72.163.212.137  port 2332  type host

Total Rx STUN Bind Req 22
Total Tx STUN Bind Succ Resp 22
Total Tx STUN Bind failure resp 0
```

Step 4

show voip
                                             				  ice instance call-id call-id-2

The following
                                          				sample output displays the idle ICE sessions on the ICE-lite and the ICE-lite
                                          				legs where there are no ICE negotiations.

### Example:

```
Device# show voip ice instance call-id 30 Interactive Connectivity Check(ICE) Instance details:
Call-ID is 30
Instance is 0x7FC617FC03F8
Overall ICE-State is RUNNING
LocalAgent's mode is ICE-CONTROLLED
RemoteAgent's mode is ICE-CONTROLLING
m-line:1
---------
ICE-State: IDLE
No candidate has been nominated

m-line:2
---------
ICE-State: IDLE
No candidate has been nominated

m-line:3
---------
ICE-State: IDLE
No candidate has been nominated

m-line:4
---------
ICE-State: IDLE
No candidate has been nominated

m-line:5
---------
ICE-State: IDLE
No candidate has been nominated

Total Rx STUN Bind Req 0
Total Tx STUN Bind Succ Resp 0
Total Tx STUN Bind failure resp 0
```

Step 5

show voip
                                             				  ice summary

The following
                                          				sample output displays a summary of active ICE sessions.

### Example:

```
Device# show voip ice summary CALL-ID              ICE-STATE
------------------------------
25                   COMPLETED
30                   RUNNING
35                   RUNNING
36                   COMPLETED
```

Step 6

show voip
                                             				  ice global-stats

The following
                                          				sample output displays the global ICE statistics.

### Example:

```
Device# show voip ice global-stats Interactive Connectivity Establishment(ICE) global stats:
Total Rx Stun BindingRequests        : 43
Total Tx Stun BindingSuccessResponses: 43
Total Tx Stun BindingErrorResponses  : 0
```

## Error Flow Calls

The following are the show command sample outputs followed by the
                              		  system logs for error flow calls. The show commands can be entered in any order.

### SUMMARY STEPS

- show call active voice compact

- show voip rtp connections

- show voip ice instance call-id call-id

- show voip ice instance call-id call-id

- show voip ice summary

- show voip ice global-stats

### DETAILED STEPS

Step 1

show call active voice compact

### Example:

```
Device# show call active video compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 2
        57 ANS     T4     g711ulaw    VOIP        Padithyam     173.39.64.79:7078
        58 ORG     T4     g711ulaw    VOIP        P9191         72.163.212.163:2336
```

Step 2

show voip rtp connections

The following sample output displays the VoIP RTP usage
                                          				information and RTP active connections.

### Example:

```
Device# show voip rtp connections VoIP RTP Port Usage Information:
Max Ports Available: 19999, Ports Reserved: 101, Ports in Use: 2
                                        Min   Max   Ports     Ports     Ports
Media-Address Range                     Port  Port  Available Reserved  In-use
------------------------------------------------------------------------------
Global Media Pool                       8000  48198 19999     101       2
------------------------------------------------------------------------------
VoIP RTP active connections :
No. CallId dstCallLocalRTP RmtRTP   LocalIP             RemoteIP          MPSS
1   57     58     8040     7078     10.104.45.107       173.39.64.79      NO
2   58     57     8042     2336     10.104.45.107       72.163.212.163    NO
Found 2 active RTP connections
```

Step 3

show voip ice instance call-id call-id

The following sample output displays the ICE sessions.

### Example:

```
Device# show voip ice instance call-id 57 Interactive Connectivity Check(ICE) Instance details:
Call-ID is 57
Instance is 0x7FC617FC03F8
Overall ICE-State is RUNNING
LocalAgent's mode is ICE-CONTROLLED
RemoteAgent's mode is ICE-CONTROLLING
m-line:1
---------
ICE-State: IDLE
No candidate has been nominated

Total Rx STUN Bind Req 2
Total Tx STUN Bind Succ Resp 0
Total Tx STUN Bind failure resp 2
```

Step 4

show voip ice instance call-id call-id

The following sample output displays the ICE sessions.

### Example:

```
Device# show voip ice instance call-id 58 Interactive Connectivity Check(ICE) Instance details:
Call-ID is 58
Instance is 0x7FC617FC0508
Overall ICE-State is RUNNING
LocalAgent's mode is ICE-CONTROLLED
RemoteAgent's mode is ICE-CONTROLLING
m-line:1
---------
ICE-State: IDLE
No candidate has been nominated

Total Rx STUN Bind Req 2
Total Tx STUN Bind Succ Resp 0
Total Tx STUN Bind failure resp 2
```

Step 5

show voip ice summary

The following sample output displays a summary of active ICE
                                          				sessions.

### Example:

```
Device# show voip ice summary CALL-ID              ICE-STATE
------------------------------
57                   RUNNING
58                   RUNNING
Total number of sessions: 2
```

Step 6

show voip ice global-stats

The following sample output displays the global ICE statistics.

### Example:

```
Device# show voip ice global-stats Interactive Connectivity Establishment(ICE) global stats:
Total Rx Stun BindingRequests        : 47
Total Tx Stun BindingSuccessResponses: 43
Total Tx Stun BindingErrorResponses  : 4
```

The following are the sys logs for invalid message integrity and
                                          				for sending ICE-controlled parameter.

Sys Log for invalid message integrity:

```
004012: *Aug  8 14:25:30.876 IST: %CISCO_STUN-4-INVALID_MESSAGE_INTEGRITY: Invalid Message-Integrity attribute in the received STUN message on UDP IP address 10.104.45.107 port 8040 ###STUN Message structure start### Message Type                  : STUN_MSG_TYPE_BINDING_REQ Magic Cookie                  : 2112A442
Transaction ID                : 01CD61B24C077331EDC27A5B 
Mapped Address                : Not Set/Present
User Name                     : Not Set/Present
Error code not present  
Alternate Server              : Not Set/Present
Realm                         : Not Set/Present
nonce                         : Not Set/Present
Xormapped Address             : Not Set/Present
Server                        : Not Set/Present
ICE Priority                  : Not Set/Present
ICE Controlled                : Not Set/Present
ICE Controlling               : Not Set/Present
Cisco-flowdata                : 
cisco-flowdata is not present Message  Integrity            : Not Set/Present Finger Print                  : Not Set/Present
###STUN Message structure End###

004013: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/cisco_stun_process_event: Exit
004014: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Inout/cisco_stun_process_event: Entry with EventType:7
004015: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Inout/cisco_stun_process_send_msg_event: Entry
004016: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSendMsg: Entry
004017: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunGetMsgClass: Entry
004018: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunGetMsgClass: en_StunResp
004019: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSendMsg: dMsgClass:3
004020: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeMsg: Entry
004021: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunCalculateSize:      Length of ERROR-CODE = 20
004022: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunCalculateSize:      Length of MESSAGE-INTEGRITY = 24
004023: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsg: STUN Message Length = 64
004024: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeHdr: Entry
004025: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeHdr: Exit
004026: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeAttr: Entry
004027: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeAttr: Exit
004028: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsgIntegrity:  Original STUN Message Length = 44
004029: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsgIntegrity:  Adjusted STUN Message Length = 44
004030: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsgIntegrity: Successfully Encoded MI attribute. Exit
004031: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSetMsgIntegrityToStunMessage: Entry
004032: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSetMsgIntegrityToStunMessage: Exit with success
004033: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsg: Total length:64
004034: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeMsg: Exit
004035: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Inout/stunSendMsgToNetwork: Entry
004036: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Detail/stunSendMsgToNetwork: Message sending from, 10.104.45.107:8040, to 173.39.64.79:7078
004037: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Detail/stunSendMsgToNetwork: Stun Message: 0111002C2112A44201CD61B24C077331EDC27A5B0009000F0000040042616420526571756573740000080014D0E2E828944BF3D07CC5C06D026D8909B85EF3E9
004038: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Inout/stunSendMsgToNetwork: Exit
004039: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSendMsg: 
** Sent Stun Packet to Network **
###STUN Message structure start### Message Type                  : STUN_MSG_TYPE_BINDING_ERR_RESP Magic Cookie                  : 2112A442
Transaction ID                : 01CD61B24C077331EDC27A5B 
Mapped Address                : Not Set/Present
User Name                     : Not Set/Present Error Code                     : Number = 400 ,Reason = Bad Request Alternate Server              : Not Set/Present
Realm                         : Not Set/Present
nonce                         : Not Set/Present
Xormapped Address             : Not Set/Present
Server                        : Not Set/Present
ICE Priority                  : Not Set/Present
ICE Controlled                : Not Set/Present
ICE Controlling               : Not Set/Present
Cisco-flowdata                : 
cisco-flowdata is not present
Message  Integrity            : D0E2E828944BF3D07CC5C06D026D8909B85EF3E9
004040: *Aug  8 14:25:30.876 IST: Finger Print                  : Not Set/Present
###STUN Message structure End###

004041: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSendMsg: Sent Bind Response, Free the transaction
004042: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Detail/cisco_stun_process_send_msg_event: STUN message Sent
```

Sys Log for sending ICE-controlled parameter instead of
                                             				  ICE-controlling parameter:

```
004130: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunGetMsgClass: Entry
004131: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunGetMsgClass: en_StunReq 004132: *Aug  8 14:25:30.912 IST: %CISCO_STUN-4-ICE_ROLE_CONFLICT: Ice Role Conflcit detected in the received STUN message on UDP IP address 10.104.45.107 port 8042 004133: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSetErrorCodeToStunMessage: Entry
004134: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSetErrorCodeToStunMessage: reason:Role Conflcit, code:487
004135: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSetErrorCodeToStunMessage: Exit with success
004136: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stun_process_send_bind_response: Exit
004137: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stun_post_bind_request_ind_to_app: Post Message to Application
004138: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/cisco_stun_process_stun_pak_rcvd_event: Received New STUN message###STUN Message structure start### Message Type                  : STUN_MSG_TYPE_BINDING_REQ Message Length                : 80
Magic Cookie                  : 2112A442
Transaction ID                : F1CF84958CE76D15C83059D9 
Mapped Address                : Not Set/Present
User Name                     : GAah:4wWY
Error code not present  
Alternate Server              : Not Set/Present
Realm                         : Not Set/Present
nonce                         : Not Set/Present
Xormapped Address             : Not Set/Present
Server                        : Cisco
ICE Priority                  : 1862270975 ICE Controlled                : 11920035603547232620 ICE Controlling               : Not Set/Present Cisco-flowdata                : 
cisco-flowdata is not present
Message  Integrity            : 0AF4B8C2378CB90AB0B0A3806507D766BF5CD1DD
004139: *Aug  8 14:25:30.912 IST: Finger Print                  : 4235512547
###STUN Message structure End###

004140: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/cisco_stun_process_event: Exit
004141: *Aug  8 14:25:30.912 IST: //58/91300134802E/STUN/Inout/cisco_stun_process_event: Entry with EventType:7
004142: *Aug  8 14:25:30.912 IST: //58/91300134802E/STUN/Inout/cisco_stun_process_send_msg_event: Entry
004143: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSendMsg: Entry
004144: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunGetMsgClass: Entry
004145: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunGetMsgClass: en_StunResp
004146: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSendMsg: dMsgClass:3
004147: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeMsg: Entry
004148: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunCalculateSize:      Length of ERROR-CODE = 24
004149: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunCalculateSize:      Length of MESSAGE-INTEGRITY = 24
004150: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsg: STUN Message Length = 68
004151: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeHdr: Entry
004152: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeHdr: Exit
004153: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeAttr: Entry
004154: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeAttr: Exit
004155: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsgIntegrity:  Original STUN Message Length = 48
004156: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsgIntegrity:  Adjusted STUN Message Length = 48
004157: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsgIntegrity: Successfully Encoded MI attribute. Exit
004158: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSetMsgIntegrityToStunMessage: Entry
004159: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSetMsgIntegrityToStunMessage: Exit with success
004160: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsg: Total length:68
004161: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeMsg: Exit
004162: *Aug  8 14:25:30.912 IST: //58/91300134802E/STUN/Inout/stunSendMsgToNetwork: Entry
004163: *Aug  8 14:25:30.912 IST: //58/91300134802E/STUN/Detail/stunSendMsgToNetwork: Message sending from, 10.104.45.107:8042, to 72.163.212.163:2336
004164: *Aug  8 14:25:30.912 IST: //58/91300134802E/STUN/Detail/stunSendMsgToNetwork: Stun Message: 011100302112A442F1CF84958CE76D15C83059D90009001100000457526F6C6520436F6E666C6369740000000008001413402FC99C60296539026305739773476578806E
004165: *Aug  8 14:25:30.913 IST: //58/91300134802E/STUN/Inout/stunSendMsgToNetwork: Exit
004166: *Aug  8 14:25:30.913 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSendMsg: 
** Sent Stun Packet to Network **
###STUN Message structure start### Message Type                  : STUN_MSG_TYPE_BINDING_ERR_RESP Magic Cookie                  : 2112A442
Transaction ID                : F1CF84958CE76D15C83059D9 
Mapped Address                : Not Set/Present
User Name                     : Not Set/Present Error Code                     : Number = 487 ,Reason = Role Conflcit Alternate Server              : Not Set/Present
Realm                         : Not Set/Present
nonce                         : Not Set/Present
Xormapped Address             : Not Set/Present
Server                        : Not Set/Present
ICE Priority                  : Not Set/Present
ICE Controlled                : Not Set/Present
ICE Controlling               : Not Set/Present
Cisco-flowdata                : 
cisco-flowdata is not present
Message  Integrity            : 13402FC99C60296539026305739773476578806E
004167: *Aug  8 14:25:30.913 IST: Finger Print                  : Not Set/Present
###STUN Message structure End###

004168: *Aug  8 14:25:30.913 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSendMsg: Sent Bind Response, Free the transaction
004169: *Aug  8 14:25:30.913 IST: //58/91300134802E/STUN/Detail/cisco_stun_process_send_msg_event: STUN message Sent
```

## Configuration Example

The following is a sample loopback dial-peer configuration on TDM gateway to support ICE-lite based media optimization:

## Troubleshoot ICE-Lite Support

You can use the
                           		following debug commands
                           		to troubleshoot the ICE-lite support on CUBE feature. Use these commands to
                           		enable ICE debugs for each call.

debug voip icelib all

debug voip icelib default

debug voip icelib detail

debug voip icelib error

debug voip icelib event

debug voip icelib inout

debug voip stun all

debug voip stun default

debug voip stun detail

debug voip stun error

debug voip stun event

debug voip stun inout

debug voip stun message

debug voip stun packet

## Additional
                        	 References

### Standards and
                              		  RFCs

RFC 5389

Session Traversal Utilities
                                             						  for NAT (STUN)

RFC
                                          						5245

Interactive Connectivity
                                             						  Establishment (ICE): A Protocol for Network Address Translator (NAT) Traversal
                                             						  for Offer/Answer Protocols

RFC 5766

Traversal Using Relays
                                             						  around NAT (TURN): Relay Extensions to Session Traversal Utilities for NAT
                                             						  (STUN)

RFC 5768

Indicating Support for
                                             						  Interactive Connectivity Establishment (ICE) in the Session Initiation Protocol
                                             						  (SIP)

RFC 3840

Indicating User Agent
                                             						  Capabilities in the Session Initiation Protocol (SIP)

RFC 7584

Session Traversal Utilities for NAT (STUN) Message
                                             						  Handling for SIP Back-to-Back User Agents (B2BUAs)

### Technical
                              		  Assistance

The
                                          						Cisco Support website provides extensive online resources, including
                                          						documentation and tools for troubleshooting and resolving technical issues with
                                          						Cisco products and technologies.

To
                                          						receive security and technical information about your products, you can
                                          						subscribe to various services, such as the Product Alert Tool (accessed from
                                          						Field Notices), the Cisco Technical Services Newsletter, and Really Simple
                                          						Syndication (RSS) Feeds.

Access
                                          						to most tools on the Cisco Support website requires a Cisco.com user ID and
                                          						password.

http://www.cisco.com/support

| Feature
                                             					 Name | Releases | Feature
                                             					 Information |
|---|---|---|
| ICE-Lite
                                             					 Support on CUBE | Cisco IOS
                                             					 15.5(3)M Cisco IOS
                                             					 XE 3.16S | The
                                             					 ICE-Lite Support on CUBE feature enables the remote peers of CUBE (that may be
                                             					 behind a NAT and doing ICE) to use the ICE semantics in the session description
                                             					 protocol (SDP) and perform an offer-answer exchange of SDP messages. The CUBE
                                             					 can also interwork with endpoints that support or do not support ICE. ICE
                                             					 agents (devices) that are always attached to the public Internet have a special
                                             					 type of implementation called Lite. CUBE will be in ICE-lite mode only. The
                                             					 following commands were introduced or modified: debug voip
                                                   						  icelib , show voip ice
                                                   						  global-stats , show voip ice instance
                                                   						  call-id call-id , show voip ice
                                                   						  summary , and stun usage
                                                   						  ice |

| Note | Refer to RFC 5245 for more information about ICE candidates. |
|---|---|

| Note | Refer to RFC 5245 for more information about ICE-lite implementation and connectivity checks. |
|---|---|

| Note | A workaround option for ICE-lite based media optimization is to configure loopback dial-peer on a TDM gateway. Contact Account
                                             or TAC teams for further technical details. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | voice class stun-usage tag Example: Device(config)# voice class stun-usage 5 | Sets STUN
                                          				usage global parameters, and enters voice class configuration mode. |
| Step 4 | stun usage ice lite Example: Device(config-class)# stun usage ice lite | Configures ICE in ICE-Lite mode. |
| Step 5 | end Example: Device(config-class)# end | Returns to
                                          				privileged EXEC mode. |

| Step 1 | show call
                                             				  active video compact Example: Device# show call active video compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 4
        25 ANS     T189   H264       VOIP-VIDEO   P8181     72.163.212.137:2328
        30 ORG     T189   H264       VOIP-VIDEO   P9191         9.45.46.16:8028
        35 ANS     T189   H264       VOIP-VIDEO   P8181         9.45.46.16:8008
        36 ORG     T189   H264       VOIP-VIDEO   P9191     72.163.212.163:2328 |
|---|---|
| Step 2 | show voip
                                             				  rtp connections The following
                                          				sample output displays the VoIP RTP usage information and RTP active
                                          				connections. Example: Device# show voip rtp connections VoIP RTP Port Usage Information:
Max Ports Available: 19999, Ports Reserved: 101, Ports in Use: 20
                                        Min   Max   Ports     Ports     Ports
Media-Address Range                     Port  Port  Available Reserved  In-use
------------------------------------------------------------------------------
Global Media Pool                       8000  48198 19999     101       20
------------------------------------------------------------------------------
VoIP RTP active connections :
No. CallId dstCallLocalRTP RmtRTP   LocalIP             RemoteIP          MPSS
1   25     30     8000     2326     10.104.45.107       72.163.212.137    NO
2   26     31     8002     2328     10.104.45.107       72.163.212.137    NO
3   27     32     8036     2454     10.104.45.107       72.163.212.137    NO
4   28     33     8004     2330     10.104.45.107       72.163.212.137    NO
5   29     34     8038     2332     10.104.45.107       72.163.212.137    NO
6   30     25     8006     8016     9.45.46.16          9.45.46.16        NO
7   31     26     8008     8028     9.45.46.16          9.45.46.16        NO
8   32     27     8010     8030     9.45.46.16          9.45.46.16        NO
9   33     28     8012     8032     9.45.46.16          9.45.46.16        NO
10  34     29     8014     8034     9.45.46.16          9.45.46.16        NO
11  35     36     8016     8006     9.45.46.16          9.45.46.16        NO
12  36     35     8018     2326     10.104.45.107       72.163.212.163    NO
13  37     41     8020     2328     10.104.45.107       72.163.212.163    NO
14  38     42     8022     2454     10.104.45.107       72.163.212.163    NO
15  39     43     8024     2330     10.104.45.107       72.163.212.163    NO
16  40     44     8026     2332     10.104.45.107       72.163.212.163    NO
17  41     37     8028     8008     9.45.46.16          9.45.46.16        NO
18  42     38     8030     8010     9.45.46.16          9.45.46.16        NO
19  43     39     8032     8012     9.45.46.16          9.45.46.16        NO
20  44     40     8034     8014     9.45.46.16          9.45.46.16        NO
Found 20 active RTP connections |
| Step 3 | show voip
                                             				  ice instance call-id call-id-1 The following
                                          				sample output displays the active ICE sessions on the ICE-full and the ICE-lite
                                          				legs where there are ICE negotiations. Example: Device# show voip ice instance call-id 25 Interactive Connectivity Check(ICE) Instance details:
Call-ID is 25
Instance is 0x7FC617FC0508
Overall ICE-State is COMPLETED
LocalAgent's mode is ICE-CONTROLLED
RemoteAgent's mode is ICE-CONTROLLING
m-line:1
---------
ICE-State: ACTIVE
NominatedPairs:
LocalIP 10.104.45.107   port 8000  type host         RemoteIP 72.163.212.137  port 2326  type host

m-line:2
---------
ICE-State: ACTIVE
NominatedPairs:
LocalIP 10.104.45.107   port 8002  type host         RemoteIP 72.163.212.137  port 2328  type host
LocalIP 10.104.45.107   port 8003  type host         RemoteIP 72.163.212.137  port 2329  type host

m-line:3
---------
ICE-State: ACTIVE
NominatedPairs:
LocalIP 10.104.45.107   port 8036  type host         RemoteIP 72.163.212.137  port 2454  type host

m-line:4
---------
ICE-State: ACTIVE
NominatedPairs:
LocalIP 10.104.45.107   port 8004  type host         RemoteIP 72.163.212.137  port 2330  type host
LocalIP 10.104.45.107   port 8005  type host         RemoteIP 72.163.212.137  port 2331  type host

m-line:5
---------
ICE-State: ACTIVE
NominatedPairs:
LocalIP 10.104.45.107   port 8038  type host         RemoteIP 72.163.212.137  port 2332  type host

Total Rx STUN Bind Req 22
Total Tx STUN Bind Succ Resp 22
Total Tx STUN Bind failure resp 0 |
| Step 4 | show voip
                                             				  ice instance call-id call-id-2 The following
                                          				sample output displays the idle ICE sessions on the ICE-lite and the ICE-lite
                                          				legs where there are no ICE negotiations. Example: Device# show voip ice instance call-id 30 Interactive Connectivity Check(ICE) Instance details:
Call-ID is 30
Instance is 0x7FC617FC03F8
Overall ICE-State is RUNNING
LocalAgent's mode is ICE-CONTROLLED
RemoteAgent's mode is ICE-CONTROLLING
m-line:1
---------
ICE-State: IDLE
No candidate has been nominated

m-line:2
---------
ICE-State: IDLE
No candidate has been nominated

m-line:3
---------
ICE-State: IDLE
No candidate has been nominated

m-line:4
---------
ICE-State: IDLE
No candidate has been nominated

m-line:5
---------
ICE-State: IDLE
No candidate has been nominated

Total Rx STUN Bind Req 0
Total Tx STUN Bind Succ Resp 0
Total Tx STUN Bind failure resp 0 |
| Step 5 | show voip
                                             				  ice summary The following
                                          				sample output displays a summary of active ICE sessions. Example: Device# show voip ice summary CALL-ID              ICE-STATE
------------------------------
25                   COMPLETED
30                   RUNNING
35                   RUNNING
36                   COMPLETED |
| Step 6 | show voip
                                             				  ice global-stats The following
                                          				sample output displays the global ICE statistics. Example: Device# show voip ice global-stats Interactive Connectivity Establishment(ICE) global stats:
Total Rx Stun BindingRequests        : 43
Total Tx Stun BindingSuccessResponses: 43
Total Tx Stun BindingErrorResponses  : 0 |

| Step 1 | show call active voice compact Example: Device# show call active video compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 2
        57 ANS     T4     g711ulaw    VOIP        Padithyam     173.39.64.79:7078
        58 ORG     T4     g711ulaw    VOIP        P9191         72.163.212.163:2336 |
|---|---|
| Step 2 | show voip rtp connections The following sample output displays the VoIP RTP usage
                                          				information and RTP active connections. Example: Device# show voip rtp connections VoIP RTP Port Usage Information:
Max Ports Available: 19999, Ports Reserved: 101, Ports in Use: 2
                                        Min   Max   Ports     Ports     Ports
Media-Address Range                     Port  Port  Available Reserved  In-use
------------------------------------------------------------------------------
Global Media Pool                       8000  48198 19999     101       2
------------------------------------------------------------------------------
VoIP RTP active connections :
No. CallId dstCallLocalRTP RmtRTP   LocalIP             RemoteIP          MPSS
1   57     58     8040     7078     10.104.45.107       173.39.64.79      NO
2   58     57     8042     2336     10.104.45.107       72.163.212.163    NO
Found 2 active RTP connections |
| Step 3 | show voip ice instance call-id call-id The following sample output displays the ICE sessions. Example: Device# show voip ice instance call-id 57 Interactive Connectivity Check(ICE) Instance details:
Call-ID is 57
Instance is 0x7FC617FC03F8
Overall ICE-State is RUNNING
LocalAgent's mode is ICE-CONTROLLED
RemoteAgent's mode is ICE-CONTROLLING
m-line:1
---------
ICE-State: IDLE
No candidate has been nominated

Total Rx STUN Bind Req 2
Total Tx STUN Bind Succ Resp 0
Total Tx STUN Bind failure resp 2 |
| Step 4 | show voip ice instance call-id call-id The following sample output displays the ICE sessions. Example: Device# show voip ice instance call-id 58 Interactive Connectivity Check(ICE) Instance details:
Call-ID is 58
Instance is 0x7FC617FC0508
Overall ICE-State is RUNNING
LocalAgent's mode is ICE-CONTROLLED
RemoteAgent's mode is ICE-CONTROLLING
m-line:1
---------
ICE-State: IDLE
No candidate has been nominated

Total Rx STUN Bind Req 2
Total Tx STUN Bind Succ Resp 0
Total Tx STUN Bind failure resp 2 |
| Step 5 | show voip ice summary The following sample output displays a summary of active ICE
                                          				sessions. Example: Device# show voip ice summary CALL-ID              ICE-STATE
------------------------------
57                   RUNNING
58                   RUNNING
Total number of sessions: 2 |
| Step 6 | show voip ice global-stats The following sample output displays the global ICE statistics. Example: Device# show voip ice global-stats Interactive Connectivity Establishment(ICE) global stats:
Total Rx Stun BindingRequests        : 47
Total Tx Stun BindingSuccessResponses: 43
Total Tx Stun BindingErrorResponses  : 4 The following are the sys logs for invalid message integrity and
                                          				for sending ICE-controlled parameter. Sys Log for invalid message integrity: 004012: *Aug  8 14:25:30.876 IST: %CISCO_STUN-4-INVALID_MESSAGE_INTEGRITY: Invalid Message-Integrity attribute in the received STUN message on UDP IP address 10.104.45.107 port 8040 ###STUN Message structure start### Message Type                  : STUN_MSG_TYPE_BINDING_REQ Magic Cookie                  : 2112A442
Transaction ID                : 01CD61B24C077331EDC27A5B 
Mapped Address                : Not Set/Present
User Name                     : Not Set/Present
Error code not present  
Alternate Server              : Not Set/Present
Realm                         : Not Set/Present
nonce                         : Not Set/Present
Xormapped Address             : Not Set/Present
Server                        : Not Set/Present
ICE Priority                  : Not Set/Present
ICE Controlled                : Not Set/Present
ICE Controlling               : Not Set/Present
Cisco-flowdata                : 
cisco-flowdata is not present Message  Integrity            : Not Set/Present Finger Print                  : Not Set/Present
###STUN Message structure End###

004013: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/cisco_stun_process_event: Exit
004014: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Inout/cisco_stun_process_event: Entry with EventType:7
004015: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Inout/cisco_stun_process_send_msg_event: Entry
004016: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSendMsg: Entry
004017: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunGetMsgClass: Entry
004018: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunGetMsgClass: en_StunResp
004019: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSendMsg: dMsgClass:3
004020: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeMsg: Entry
004021: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunCalculateSize:      Length of ERROR-CODE = 20
004022: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunCalculateSize:      Length of MESSAGE-INTEGRITY = 24
004023: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsg: STUN Message Length = 64
004024: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeHdr: Entry
004025: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeHdr: Exit
004026: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeAttr: Entry
004027: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeAttr: Exit
004028: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsgIntegrity:  Original STUN Message Length = 44
004029: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsgIntegrity:  Adjusted STUN Message Length = 44
004030: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsgIntegrity: Successfully Encoded MI attribute. Exit
004031: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSetMsgIntegrityToStunMessage: Entry
004032: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSetMsgIntegrityToStunMessage: Exit with success
004033: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsg: Total length:64
004034: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeMsg: Exit
004035: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Inout/stunSendMsgToNetwork: Entry
004036: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Detail/stunSendMsgToNetwork: Message sending from, 10.104.45.107:8040, to 173.39.64.79:7078
004037: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Detail/stunSendMsgToNetwork: Stun Message: 0111002C2112A44201CD61B24C077331EDC27A5B0009000F0000040042616420526571756573740000080014D0E2E828944BF3D07CC5C06D026D8909B85EF3E9
004038: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Inout/stunSendMsgToNetwork: Exit
004039: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSendMsg: 
** Sent Stun Packet to Network **
###STUN Message structure start### Message Type                  : STUN_MSG_TYPE_BINDING_ERR_RESP Magic Cookie                  : 2112A442
Transaction ID                : 01CD61B24C077331EDC27A5B 
Mapped Address                : Not Set/Present
User Name                     : Not Set/Present Error Code                     : Number = 400 ,Reason = Bad Request Alternate Server              : Not Set/Present
Realm                         : Not Set/Present
nonce                         : Not Set/Present
Xormapped Address             : Not Set/Present
Server                        : Not Set/Present
ICE Priority                  : Not Set/Present
ICE Controlled                : Not Set/Present
ICE Controlling               : Not Set/Present
Cisco-flowdata                : 
cisco-flowdata is not present
Message  Integrity            : D0E2E828944BF3D07CC5C06D026D8909B85EF3E9
004040: *Aug  8 14:25:30.876 IST: Finger Print                  : Not Set/Present
###STUN Message structure End###

004041: *Aug  8 14:25:30.876 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSendMsg: Sent Bind Response, Free the transaction
004042: *Aug  8 14:25:30.876 IST: //57/91300134802E/STUN/Detail/cisco_stun_process_send_msg_event: STUN message Sent Sys Log for sending ICE-controlled parameter instead of
                                             				  ICE-controlling parameter: 004130: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunGetMsgClass: Entry
004131: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunGetMsgClass: en_StunReq 004132: *Aug  8 14:25:30.912 IST: %CISCO_STUN-4-ICE_ROLE_CONFLICT: Ice Role Conflcit detected in the received STUN message on UDP IP address 10.104.45.107 port 8042 004133: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSetErrorCodeToStunMessage: Entry
004134: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSetErrorCodeToStunMessage: reason:Role Conflcit, code:487
004135: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSetErrorCodeToStunMessage: Exit with success
004136: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stun_process_send_bind_response: Exit
004137: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stun_post_bind_request_ind_to_app: Post Message to Application
004138: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/cisco_stun_process_stun_pak_rcvd_event: Received New STUN message###STUN Message structure start### Message Type                  : STUN_MSG_TYPE_BINDING_REQ Message Length                : 80
Magic Cookie                  : 2112A442
Transaction ID                : F1CF84958CE76D15C83059D9 
Mapped Address                : Not Set/Present
User Name                     : GAah:4wWY
Error code not present  
Alternate Server              : Not Set/Present
Realm                         : Not Set/Present
nonce                         : Not Set/Present
Xormapped Address             : Not Set/Present
Server                        : Cisco
ICE Priority                  : 1862270975 ICE Controlled                : 11920035603547232620 ICE Controlling               : Not Set/Present Cisco-flowdata                : 
cisco-flowdata is not present
Message  Integrity            : 0AF4B8C2378CB90AB0B0A3806507D766BF5CD1DD
004139: *Aug  8 14:25:30.912 IST: Finger Print                  : 4235512547
###STUN Message structure End###

004140: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/cisco_stun_process_event: Exit
004141: *Aug  8 14:25:30.912 IST: //58/91300134802E/STUN/Inout/cisco_stun_process_event: Entry with EventType:7
004142: *Aug  8 14:25:30.912 IST: //58/91300134802E/STUN/Inout/cisco_stun_process_send_msg_event: Entry
004143: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSendMsg: Entry
004144: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunGetMsgClass: Entry
004145: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunGetMsgClass: en_StunResp
004146: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSendMsg: dMsgClass:3
004147: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeMsg: Entry
004148: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunCalculateSize:      Length of ERROR-CODE = 24
004149: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunCalculateSize:      Length of MESSAGE-INTEGRITY = 24
004150: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsg: STUN Message Length = 68
004151: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeHdr: Entry
004152: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeHdr: Exit
004153: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeAttr: Entry
004154: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeAttr: Exit
004155: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsgIntegrity:  Original STUN Message Length = 48
004156: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsgIntegrity:  Adjusted STUN Message Length = 48
004157: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsgIntegrity: Successfully Encoded MI attribute. Exit
004158: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSetMsgIntegrityToStunMessage: Entry
004159: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunSetMsgIntegrityToStunMessage: Exit with success
004160: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunEncodeMsg: Total length:68
004161: *Aug  8 14:25:30.912 IST: //-1/xxxxxxxxxxxx/STUN/Inout/stunEncodeMsg: Exit
004162: *Aug  8 14:25:30.912 IST: //58/91300134802E/STUN/Inout/stunSendMsgToNetwork: Entry
004163: *Aug  8 14:25:30.912 IST: //58/91300134802E/STUN/Detail/stunSendMsgToNetwork: Message sending from, 10.104.45.107:8042, to 72.163.212.163:2336
004164: *Aug  8 14:25:30.912 IST: //58/91300134802E/STUN/Detail/stunSendMsgToNetwork: Stun Message: 011100302112A442F1CF84958CE76D15C83059D90009001100000457526F6C6520436F6E666C6369740000000008001413402FC99C60296539026305739773476578806E
004165: *Aug  8 14:25:30.913 IST: //58/91300134802E/STUN/Inout/stunSendMsgToNetwork: Exit
004166: *Aug  8 14:25:30.913 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSendMsg: 
** Sent Stun Packet to Network **
###STUN Message structure start### Message Type                  : STUN_MSG_TYPE_BINDING_ERR_RESP Magic Cookie                  : 2112A442
Transaction ID                : F1CF84958CE76D15C83059D9 
Mapped Address                : Not Set/Present
User Name                     : Not Set/Present Error Code                     : Number = 487 ,Reason = Role Conflcit Alternate Server              : Not Set/Present
Realm                         : Not Set/Present
nonce                         : Not Set/Present
Xormapped Address             : Not Set/Present
Server                        : Not Set/Present
ICE Priority                  : Not Set/Present
ICE Controlled                : Not Set/Present
ICE Controlling               : Not Set/Present
Cisco-flowdata                : 
cisco-flowdata is not present
Message  Integrity            : 13402FC99C60296539026305739773476578806E
004167: *Aug  8 14:25:30.913 IST: Finger Print                  : Not Set/Present
###STUN Message structure End###

004168: *Aug  8 14:25:30.913 IST: //-1/xxxxxxxxxxxx/STUN/Detail/stunSendMsg: Sent Bind Response, Free the transaction
004169: *Aug  8 14:25:30.913 IST: //58/91300134802E/STUN/Detail/cisco_stun_process_send_msg_event: STUN message Sent |

| Standard/RFC | Title |
|---|---|
| RFC 5389 | Session Traversal Utilities
                                             						  for NAT (STUN) |
| RFC
                                          						5245 | Interactive Connectivity
                                             						  Establishment (ICE): A Protocol for Network Address Translator (NAT) Traversal
                                             						  for Offer/Answer Protocols |
| RFC 5766 | Traversal Using Relays
                                             						  around NAT (TURN): Relay Extensions to Session Traversal Utilities for NAT
                                             						  (STUN) |
| RFC 5768 | Indicating Support for
                                             						  Interactive Connectivity Establishment (ICE) in the Session Initiation Protocol
                                             						  (SIP) |
| RFC 3840 | Indicating User Agent
                                             						  Capabilities in the Session Initiation Protocol (SIP) |
| RFC 7584 | Session Traversal Utilities for NAT (STUN) Message
                                             						  Handling for SIP Back-to-Back User Agents (B2BUAs) |

| Description | Link |
|---|---|
| The
                                          						Cisco Support website provides extensive online resources, including
                                          						documentation and tools for troubleshooting and resolving technical issues with
                                          						Cisco products and technologies. To
                                          						receive security and technical information about your products, you can
                                          						subscribe to various services, such as the Product Alert Tool (accessed from
                                          						Field Notices), the Cisco Technical Services Newsletter, and Really Simple
                                          						Syndication (RSS) Feeds. Access
                                          						to most tools on the Cisco Support website requires a Cisco.com user ID and
                                          						password. | http://www.cisco.com/support |