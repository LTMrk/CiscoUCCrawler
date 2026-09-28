---
doc_id: www-cisco-com-c-en-us-support-docs-voice-call-routing-dial-plans-98582-index-html-21169dfa0e
source_url: https://www.cisco.com/c/en/us/support/docs/voice/call-routing-dial-plans/98582-index.html
retrieved_at: 2026-08-16T19:23:25.495950+00:00
---

IOS Voice XML Gateway to CVP Call Flow Using MRCPv2 ASR / TTS

# IOS Voice XML Gateway to CVP Call Flow Using MRCPv2 ASR / TTS

### Download Options

Updated: September 19, 2007

Document ID: 98582

Contents

## Contents

## Introduction

Voice Extensible Markup Language (VXML) is a standard defined by the World Wide Web Consortium (W3C). It is designed to create audio dialogs that provide synthesized speech, recognition of spoken words, recognition of DTMF digits, and recorded spoken audio. The VXML server and clients use the well known HTTP protocol to exchange VXML documents / pages.

Cisco Voice Portal (CVP) delivers intelligent and interactive voice response (IVR) applications that can be accessed over phone. There are three types of CVP deployments:

Standalone Service

CVP Call Control

Call Queue and Transfer

Synthesized speech and the recognition of spoken words / DTMF digits functionalities are provided by Text-to-Speech (TTS) and Automatic Speech Recognition Servers (ASR). The IOS ® VXML Gateway communicates with the TTS / ASR server through the Media Resource Control protocol (MRCP). There are two versions of MRCP (RFC 4463), namely MRCPv1 (MRCP over RTSP) and MRCPv2 (MRCP over SIP).

This document describes the call flow of an IOS Voice XML Gateway to CVP call in a standalone service deployment that uses MRCPv2 TTS / ASR servers. A sample pharmacy application was deployed at the CVP VXML server.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

The information in this document is based on these software and hardware versions:

IOS VXML Gateway: Cisco AS5400XM, IOS 12.4(15)T1

VXML server: CVP 4.0

ASR / TTS Server: Loquendo Speech Suite 7.0

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

### Conventions

Refer to Cisco Technical Tips Conventions for more information on document conventions.

## Configure

In this section, you are presented with the information to configure the features described in this document.

Note: Use the Command Lookup Tool ( registered customers only) to obtain more information on the commands used in this section.

### Network Diagram

This document uses this network setup:

### Configurations

This document uses these configurations:

```
!--- Define Hostname to IP Address !---- mapping for ASR and TTS servers ip host asr-en-us 172.18.110.76
ip host tts-en-us 172.18.110.76 !--- Define the Voice class URI to match !---- the SIP URI of ASR Server in the dial-peer voice class uri  TTS sip
 pattern tts@172.18.110.76 !--- Define the Voice class URI to match !---- the SIP URI of TTS server in the dial-peer voice class uri  ASR sip
 pattern asr@172.18.110.76 !--- Define the amount of maximum memory !---- to used for downloaded prompts ivr prompt memory 15000 !--- Define the SIP URI of ASR !---- and TTS Server ivr asr-server sip:asr@172.18.110.76
ivr tts-server sip:tts@172.18.110.76 !--- Configure an application service for !---- CVP VXML CVPSelfServiceBootstrap.vxml application
 service CVPSelfService flash:
CVPSelfServiceBootstrap.vxml
  paramspace english language en
  paramspace english index 0
  paramspace english location flash:
  paramspace english prefix en !--- Configure an application service for !---- CVP VXML CVPSelfService.tcl Script !--- CVPSelfService-app parameter specifies !---- the name of the VXML Application !--- CVPPrimary parameter specifies the !---- IP address of the VXML server service Pharmacy flash:CVPSelfService.tcl
  paramspace english index 0
  paramspace english language en
  paramspace english location flash:
  param CVPSelfService-port 7000
  param CVPSelfService-app 
GoodPrescriptionRefillApp7
  paramspace english prefix en
  param CVPPrimaryVXMLServer 172.18.110.75 !--- Specifies the Gateway’s RTP !---- stream to the ASR / TTS to go around the !---- Content Service Switch !---- instead of through the CSS. mrcp client rtpsetup enable !--- Specify the maximum memory size !---- for the HTTP Client Cache http client cache memory pool 15000 !--- Specify the maximum number of file !---- that can be stored in the !---- HTTP Client Cache http client cache memory file 500 !--- Disable Persistent !---- HTTP Connections no http client connection persistent !--- Configure the T1 PRI controller T1 3/0
 framing esf
 linecode b8zs
 pri-group timeslots 1-24 !--- Configure the ISDN switch !---- type and incoming-voice !---- under the D-channel interface interface Serial3/0:23
 no ip address
 encapsulation hdlc
 isdn switch-type primary-net5
 isdn incoming-voice modem
 no cdp enable ! --- Configure a POTS !---- dial-peer that will be used !---- as inbound dial-peer for calls coming ! --- in across the T1 PRI line. !---- The “pharmacy”service !---- is applied under this dial-peer. dial-peer voice 1 pots
 service pharmacy
 destination-pattern 5555
 direct-inward-dial
 port 3/0:D
 forward-digits all !--- Configure a SIP Voip !---- dial-peer that will be used !---- as an outbound dial-peer when the !---Gateway initiates a MRCP overc SIP !---- session to the ASR server. !---- Codec = G711ulaw, DTMF-Relay !---- = RTP-NTE, No Vad dial-peer voice 5 voip
 session protocol sipv2
 destination uri ASR
 dtmf-relay rtp-nte
 codec g711ulaw
 no vad !--- Configure a SIP Voip !---- dial-peer that will be used !---- as an outbound dial-peer when the !---Gateway initiates a MRCP !---- overc SIP session to the TTS server !--- Codec = G711ulaw, DTMF-Relay = RTP-NTE, !---- No Vad dial-peer voice 6 voip
 session protocol sipv2
 destination uri TTS
 dtmf-relay rtp-nte
 codec g711ulaw
 no vad
```

### Call Flow Example

This section describes the call flow that results from this configuration example.

An ISDN call arrives at the PSTN / VXML Gateway across T1 PRI 3/0.

The IOS Gateway matches POTS dial-peer 1 as the inbound dial-peer for this call.

The IOS Gateway hands off the call control to the Pharmacy service that is associated to dial-peer 1.

The CVP VXML / TCL script associated with the Pharmacy service sends a HTTP GET request to the VXML server.

The VXML server returns 200 OK response. This response contains a VXML document / page.

The IOS Gateway executes the VXML document.

If the VXML document specifies a URL for an audio prompt, the IOS Gateway downloads the Audio file and plays the prompt.

If the VXML document specifies a text for an audio prompt, the IOS Gateway establishes a SIP session with tts@172.18.110.76 (TTS Server) using dial-peer 5. After the SIP session is established, it opens a TCP connection to the TTS Server using the TCP port number provided in the SDP of 200 OK response of the SIP INVITE. This TCP connection is used to exchange MRCP messages such as SPEAK, SPEAK-COMPLETE between the IOS Gateway and TTS Server.

The TTS Server sends the G.711ulaw RTP audio stream to the IP address and UDP port number provided by the Gateway in the SDP of the SIP INVITE.

If the VXML document specifies the gateway to recognize DTMF digits and / or spoken words, the IOS Gateway establishes a SIP session with asr@172.18.110.76 (ASR server) with dial-peer 6. After the SIP session is established, it opens a TCP connection to the ASR Server using the TCP port number provided in the SDP of 200 OK response of the SIP INVITE. This TCP connection is used to exchange MRCP messages such as DEFINE GRAMMAR, COMPLETE, RECOGNIZE, and RECOGNITION-COMPLETE between the IOS Gateway and ASR Server.

The IOS VXML Gateway sends the G.711ulaw RTP audio stream to the IP address and UDP port number provided by the ASR in the SDP of the SIP 200 OK response. The IOS VXML Gateway sends the digits entered by the PSTN user as RTP-NTE events to the ASR server.

After the execution of the VXML document, the gateway sends an HTTP POST request (with a set of parameters) as specified in the <submit> tag of the VXML document / page.

Steps 6 – 10 occur for each VXML document sent by the server.

When the VXML Application finishes the service provided to the caller, it sends a VXML document with just a <exit/> tag within the <form> element.

The IOS Gateway disconnects the MRCPv2 sessions established with the TTS and ASR servers.

The IOS Gateway disconnects the call on the ISDN side.

## Verify

Use this section to confirm that your configuration works properly.

The Output Interpreter Tool ( registered customers only) (OIT) supports certain show commands. Use the OIT to view an analysis of show command output.

Show call active voice brief

```
11F8 : 160 333356110ms.
   1 +10 pid:1 Answer 5555 active
 dur 00:00:54 tx:1740/300598 rx:364/85472
 Tele 3/0:D (160) [3/0.1] 
   tx:15145/15145/0ms None noise:-52 
   acom:6  i/0:-32/-64 dBm 

Telephony call-legs: 1
SIP call-legs: 0
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
Multicast call-legs: 0
Media call-legs: 0
Total call-legs: 1
```

Show call active media brief

```
11F8 : 163 333360880ms.1 
   +60 pid:6 Originate 
   sip:tts@172.18.110.76:5060 active
 dur 00:00:44 tx:0/0 rx:2212/353545
 IP 172.18.110.76:10000 SRTP: 
   off rtt:0ms pl:
   4485/0ms lost:0/1/0 delay:65/65/65ms 
   g711ulaw TextRelay: off
 media inactive detected:n 
   media contrl rcvd:
   n/a timestamp:n/a
 long duration call detected:n 
   long duration 
   call duration:n/a timestamp:n/a11F8 : 
   164 333360890ms.1 +20 pid:5 Originate 
   sip:asr@172.18.110.76:5060 active

 dur 00:00:44 tx:1687/297152 rx:0/0
 IP 172.18.110.76:10002 SRTP: 
   off rtt:0ms 
   pl:6550/30ms lost:0/2/0 delay:65/65/65ms 
   g711ulaw TextRelay: off
 media inactive detected:n media contrl 
   rcvd:n/a timestamp:n/a
 long duration call detected:n 
   long duration 
   call duration:n/a timestamp:n/a 

Telephony call-legs: 0
SIP call-legs: 0
H323 call-legs: 0
Call agent controlled call-legs: 0
SCCP call-legs: 0
Multicast call-legs: 0
Media call-legs: 2
Total call-legs: 2
```

Show mrcp client session active detail

```
No Of Active MRCP Sessions: 1 

Call-ID: 0xA0 same: 0
--------------------------------------------
Resource Type: Synthesizer            
   URL: sip:tts@172.18.110.76
 Method In Progress: SPEAK                
   State: S_SYNTH_SPEAKING 

 Associated CallID: 0xA3
 MRCP version: 2.0
 Control Protocol: TCP Server IP Address: 
   172.18.110.76  Port: 51000 

  Data Protocol: RTP Server IP Address: 
   172.18.110.76  Port: 10000
  Signalling URL: sip:tts@172.18.110.76:5060 

  Packets Transmitted: 0 (0 bytes)
  Packets Received: 2265 (361968 bytes)
  ReceiveDelay: 65     LostPackets: 0
--------------------------------------------
--------------------------------------------

Resource Type: Recognizer             
   URL: sip:asr@172.18.110.76
 Method In Progress: RECOGNIZE            
   State: S_RECOG_RECOGNIZING 

Associated CallID: 0xA4
MRCP version: 2.0
Control Protocol: TCP Server IP Address: 
   172.18.110.76  Port: 51001 

Data Protocol: RTP Server IP Address: 
   172.18.110.76  Port: 10002 

Packets Transmitted: 1791 (313792 bytes)
Packets Received: 0 (0 bytes)
ReceiveDelay: 60     LostPackets: 0
```

Show voip rtp connections

```
VoIP RTP active connections :
No. CallId     dstCallId  LocalRTP 
   RmtRTP LocalIP         
   RemoteIP
1   163        160        18964    
   10000  14.1.16.25      
   172.18.110.76
2   164        160        23072    
   10002  14.1.16.25      
   172.18.110.76
Found 2 active RTP connections
```

Show http client cache

```
HTTP Client cached information
==============================
Maximum memory pool allowed for 
   HTTP Client caching 
   = 15000 K-bytes
Maximum file size allowed for caching 
   = 500 K-bytes
Total memory used up for Cache 
   = 410 Bytes
Message response timeout = 10 secs
Total cached entries     = 1
Total non-cached entries = 0 

           Cached entries
           ============== 

entry 114,  1 entries
Ref   FreshTime   Age          Size        
   context
---   ---------   ---          ----        
   -------
1     86400       48           1505        
   0 
url: http://172.18.110.75/Welcome-1.wav
```

## Troubleshoot

This section provides information you can use to troubleshoot your configuration.

### Debug Commands

Configure the IOS Gateway to log the debugs in its logging buffer and disable “logging console”.

Note: Refer to Important Information on Debug Commands before you use debug commands.

Note: These are the commands used to configure the Gateway in order to store the debugs in the Gateway's logging buffer:

service timestamps debug datetime msec

service sequence

no logging console

logging buffered 5000000 debug

clear log

The following are the debug commands used to troubleshoot the configuration:

debug isdn q931

debug voip ccapi inout

debug voip application vxml default

debug voip application vxml dump

debug ccsip message

debug mrcp detail

debug http client all

debug voip rtp session nte named-event

### Debug Outputs

This section provides debug outputs for this sample call flow:

#### Inbound Call from PSTN

```
*Jan 18 03:34:52.735: ISDN Se3/0:23 
   Q931: RX <- SETUP pd = 8  callref = 0x005A
        Bearer Capability i = 0x8090A2 
                Standard = CCITT 
                Transfer Capability = Speech  
                Transfer Mode = Circuit 
                Transfer Rate = 64 kbit/s 
        Channel ID i = 0xA98381 
                Exclusive, Channel 1 
        Called Party Number i = 0x81, '5555' 
                Plan:ISDN, Type:Unknown
*Jan 18 03:34:52.735: //-1/2AEE8C2A801C/
   CCAPI/cc_api_display_ie_subfields:
   cc_api_call_setup_ind_common:
   cisco-username=
   ----- ccCallInfo IE subfields -----
   cisco-ani=
   cisco-anitype=0
   cisco-aniplan=0
   cisco-anipi=0
   cisco-anisi=0
   dest=5555
   cisco-desttype=0
   cisco-destplan=1
   cisco-rdie=FFFFFFFF
   cisco-rdn=
   cisco-rdntype=-1
   cisco-rdnplan=-1
   cisco-rdnpi=-1
   cisco-rdnsi=-1
   cisco-redirectreason=-1   fwd_final_type =0
   final_redirectNumber =
   hunt_group_timeout =0
```

#### Inbound Dial-Peer 1 is Matched

```
*Jan 18 03:34:52.735: 
   //-1/2AEE8C2A801C/
   CCAPI/cc_api_call_setup_ind_common:
   Interface=0x664B4BA4, Call Info(
   Calling Number=,(Calling Name=)(TON=Unknown, 
   NPI=Unknown, Screening=Not Screened, 
   Presentation=Allowed),
   Called Number=5555(TON=Unknown, NPI=ISDN),
   Calling Translated=FALSE, Subscriber 
   Type Str=RegularLine, 
   FinalDestinationFlag=TRUE,
   Incoming Dial-peer=1, Progress 
   Indication=NULL(0), 
   Calling IE Present=FALSE,
   Source Trkgrp Route Label=, 
   Target Trkgrp Route Label=, 
   CLID Transparent=FALSE), 
   Call Id=-1
```

#### Call is Handed off to Pharmacy Service

```
*Jan 18 03:34:52.739: 
   //127/2AEE8C2A801C/CCAPI
   /cc_process_call_setup_ind:
   >>>>CCAPI handed cid 127 with tag 1 to app 
   "_ManagedAppProcess_Pharmacy"
*Jan 18 03:34:52.739: 
   //127/2AEE8C2A801C/CCAPI/ccCallSetupAck:
   Call Id=127
```

#### Call gets Connected on the ISDN Side

```
*Jan 18 03:34:52.739: 
   ISDN Se3/0:23 Q931: TX -> 
   CONNECT pd = 8  callref = 
   0x805A
*Jan 18 03:34:52.739: 
   //127/2AEE8C2A801C/CCAPI/ccCallHandoff:
   Silent=FALSE, Application=0x663106C4, 
   Conference Id=0xFFFFFFFF
*Jan 18 03:34:52.743: //127//VXML:/Open_CallHandoff:
```

#### Gateway Starts the Execution of the CVPSelfServiceBootstrap.vxml VoiceXML Script

```
*Jan 18 03:34:52.755: 
   //127/2AEE8C2A801C/VXML:
   /vxml_vxml_proc:
<vxml> 
   URI(abs):flash:
   CVPSelfServiceBootstrap.vxml 
   scheme=flash 
   path=CVPSelfServiceBootstrap.vxml 
   base= 
   URI(abs):flash:
   CVPSelfServiceBootstrap.vxml 
   scheme=flash 
   path=CVPSelfServiceBootstrap.vxml 
   lang=none version=2.0 
<script>:
*Jan 18 03:34:52.799: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval: 
*Jan 18 03:34:52.863: //127/2AEE8C2A801C/VXML
   :/vxml_jse_global_switch:  
   switch to scope(application) 
<var>: namep=handoffstring 
   expr=session.handoff_string
*Jan 18 03:34:52.867: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval:  
   expr=(var handoffstring=session.
   handoff_string) 
<var>: namep=application expr=getValue('APP')
*Jan 18 03:34:52.867: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval:  
   expr=(var application=getValue('APP')) 
<var>: namep=port expr=getValue('PORT')
*Jan 18 03:34:52.867: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval: 
   expr=(var port=getValue('PORT')) 
<var>: namep=callid expr=getValue('CALLID')
*Jan 18 03:34:52.867: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval:  
   expr=(var callid=getValue('CALLID')) 
<var>: namep=servername expr=getValue('PRIMARY')
*Jan 18 03:34:52.867: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval:  
   expr=(var servername=getValue('PRIMARY')) 
<var>: namep=var1 expr=getValue('var1')
*Jan 18 03:34:52.867: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval:  
   expr=(var var1=getValue('var1')) 
<var>: namep=var2 expr=getValue('var2')
*Jan 18 03:34:52.867: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval: 
   expr=(var var2=getValue('var2')) 
<var>: namep=var3 expr=getValue('var3')
*Jan 18 03:34:52.867: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval:  
   expr=(var var3=getValue('var3')) 
<var>: namep=var4 expr=getValue('var4')
*Jan 18 03:34:52.867: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval: 
   expr=(var var4=getValue('var4')) 
<var>: namep=var5 expr=getValue('var5')
*Jan 18 03:34:52.867: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval: 
   expr=(var var5=getValue('var5')) 
<var>: namep=status expr=getValue('status')
*Jan 18 03:34:52.867: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval:  
   expr=(var status=getValue('status')) 
<var>: namep=prevapp expr=getValue('prevapp')
*Jan 18 03:34:52.871: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval:
   expr=(var prevapp=getValue('prevapp')) 
<var>: namep=survive expr=getValue('survive')
*Jan 18 03:34:52.871: //127/2AEE8C2A801C/VXML
   :/vxml_expr_eval:  
   expr=(var survive=getValue('survive')) 
<var>: namep=handoffExit
```

#### Gateway Sends an HTTP GET Request to the VXML Server

```
*Jan 18 03:34:52.875: 
   //127//HTTPC:/httpc_write_stream: 
   Client write buffer fd(3):
GET /CVP/Server?application=
   GoodPrescriptionRefillApp7&callid=
   2AEE8C2A-0AFB11D6-801C0013-
   803E8C8E&session.connection.remote.uri=555
5&session.connection.local.uri=5555 HTTP/1.1
Host: 172.18.110.75:7000
Content-Type: application/x-www-form-urlencoded
Connection: close
Accept: text/vxml, text/x-vxml, application/vxml, 
   application/x-vxml, application/voicexml, 
   application/x-voicexml, text/plain, tex
t/html, audio/basic, audio/wav, 
   multipart/form-data, 
   application/octet-stream
User-Agent: Cisco-IOS-C5400/12.4
```

#### Gateway Receives a 200 OK message from the VXML Server

The message body of this response contains a VXML document (1). The VXML document tells the Gateway play media file called Welcome-1.wav located in a Media Server.

```
*Jan 18 03:34:52.883: processing server 
   rsp msg: msg(67CA63A8)
   URL:http://172.18.110.75:7000/CVP/
   Server?application=GoodPrescription
RefillApp7&callid=2AEE8C2A-0AFB11D6-801C0013
   -803E8C8E&session.connection.
   remote.uri=5555&session.connection.local.
   uri=5555, fd(3):
*Jan 18 03:34:52.883: Request msg: 
   GET /CVP/Server?application=
   GoodPrescriptionRefillApp7&callid=
   2AEE8C2A-0AFB11D6-801C0013-803E8C8
E&session.connection.remote.
   uri=5555&session
   .connection.local.uri=5555 HTTP/1.1
*Jan 18 03:34:52.883: 
   Message Response Code: 200
*Jan 18 03:34:52.883: 
   Message Rsp Decoded Headers:
*Jan 18 03:34:52.883: 
   Date:Mon, 30 Apr 2007 16:58:39 GMT
*Jan 18 03:34:52.883: 
   Content-Type:text/xml;
   charset=ISO-8859-1
*Jan 18 03:34:52.883: 
   Connection:close
*Jan 18 03:34:52.883: 
   Set-Cookie:JSESSIONID=
   BBCE0F948ADFDB720497F587A7997538; 
   Path=/CVP 

*Jan 18 03:34:52.883: headers:
*Jan 18 03:34:52.883: HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Set-Cookie: JSESSIONID=BBCE0F948ADF
   DB720497F587A7997538; Path=/CVP
Content-Type: text/xml;charset=ISO-8859-1
Date: Mon, 30 Apr 2007 16:58:39 GMT
Connection: close
 

*Jan 18 03:34:52.883: body:
*Jan 18 03:34:52.883: <?xml version="1.0" 
   encoding="UTF-8"?>
<vxml version="2.0" application=
   "/CVP/Server?audium_root=true&amp;
   calling_into=GoodPrescriptionRefillApp7" 
   xml:lang="en-us">
  <form id="audium_start_form">
    <block>
      <assign name="audium_vxmlLog" expr="''" />
      <assign name="audium_element
   _start_time_millisecs" 
   expr="new Date().getTime()" />
      <goto next="#start" />
    </block>
  </form>
  <form id="start">
    <block>
      <prompt bargein="true">
        <audio src="http://172.18.110.75/
   Welcome-1.wav" />
      </prompt>
      <assign name="audium_vxmlLog" 
   expr="audium_vxmlLog 
   + '|||audio_group$$$' + 'initial_audio_group' 
   + '^^^' 
   + application.getEla
psedTime(audium_element_start_time_millisecs)" />
      <submit next="/CVP/Server" method="post" 
   namelist=" audium_vxmlLog" />
    </block>
  </form>
</vxml>
```

#### Gateway Sends a HTTP GET Request to the Media Server to Download the Welcome-1.wav File

```
GET /Welcome-1.wav HTTP/1.1
Host: 172.18.110.75
Content-Type: 
   application/x-www-form-urlencoded
Connection: close
Accept: text/vxml, 
   text/x-vxml, application/vxml, 
   application/x-vxml, 
   application/voicexml, 
   application/x-voicexml, 
   text/plain, tex
t/html, audio/basic, audio/wav, 
   multipart/form-data, 
   application/octet-stream
User-Agent: Cisco-IOS-C5400/12.4
```

#### Gateway Receives a 200 OK from the Media Server and Receives the Contents of the Welcome-1.wav in the HTTP Message Body

```
*Jan 18 03:34:55.647: 
   //127//HTTPC:/httpc_socket_read: 
*Jan 18 03:34:55.647: 
   read data from the socket 3 
   : first 400 bytes of data: 
HTTP/1.1 200 OK
Content-Length: 26450
Content-Type: audio/wav
Last-Modified: 
   Mon, 30 Apr 2007 15:36:51 GMT
Accept-Ranges: bytes
ETag: "e0c1445f3d8bc71:2d6"
Server: Microsoft-IIS/6.0
Date: Mon, 30 Apr 2007 16:58:42 GMT
Connection: close

RIFFJg(Unprintable char...)
   0057415645666D7420120001010401
   F00401F00108000666163744000176700
   64617461176700FFFFFF807
   FFFFFFF80FFFFFF80F
(other hex information not shown).
```

#### Gateway Sends a POST HTTP Request to the Server as Defined in the "Submit" Option of VXML Document (1)

```
POST /CVP/Server HTTP/1.1
Host: 172.18.110.75:7000
Content-Length: 67
Content-Type: 
   application/x-www-form-urlencoded
Cookie: $Version=0; JSESSIONID=BBCE0F948
   ADFDB720497F587A7997538; $Path=/CVP
Connection: close
Accept: text/vxml, text/x-vxml, 
   application/vxml, 
   application/x-vxml, 
   application/voicexml, 
   application/x-voicexml, 
   text/plain, tex
t/html, audio/basic, audio/wav, 
   multipart/form-data, 
   application/octet-stream
User-Agent: Cisco-IOS-C5400/12.4
```

#### Gateway Receives a 200 OK for its POST HTTP Request

The message body contains VXML document (2). The VXML document tells the Gateway to play "Thank you for calling Audium pharmacy." Note that this prompt needs to be synthesized by a Text to Speech Server.

```
*Jan 18 03:34:55.651: 
   processing server rsp msg: 
   msg(67CA6960)URL:
   http://172.18.110.75:
   7000/CVP/Server, fd(4):
*Jan 18 03:34:55.651: Request msg: 
   POST /CVP/Server HTTP/1.1
*Jan 18 03:34:55.651: 
   Message Response Code: 200
*Jan 18 03:34:55.651: 
   Message Rsp Decoded Headers:
*Jan 18 03:34:55.651: 
   Date:Mon, 30 Apr 2007 16:58:42 GMT
*Jan 18 03:34:55.651: 
   Content-Type:text/xml;
   charset=ISO-8859-1
*Jan 18 03:34:55.651: Connection:close
*Jan 18 03:34:55.651: headers:
*Jan 18 03:34:55.651: HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Content-Type: text/xml;charset=ISO-8859-1
Date: Mon, 30 Apr 2007 16:58:42 GMT
Connection: close
 

*Jan 18 03:34:55.655: body:
*Jan 18 03:34:55.655: <?xml version="1.0" 
   encoding="UTF-8"?>
<vxml version="2.0" application=
   "/CVP/Server?audium_root=true&amp;
   calling_into=GoodPrescriptionRefillApp7" 
   xml:lang="en-us">
  <form id="audium_start_form">
    <block>
      <assign name="audium_vxmlLog" expr="''" />
      <assign name="audium_element
   _start_time_millisecs" 
   expr="new Date().getTime()" />
      <goto next="#start" />
    </block>
  </form>
  <form id="start">
    <block>
      <prompt bargein="true">
   Thank you for calling Audium pharmacy.
   </prompt>
      <assign name="audium_vxmlLog" expr=
   "audium_vxmlLog + '|||audio_group$$$' 
   + 'initial_audio_group' 
   + '^^^' + application.getEla
psedTime(audium_element_start_time_millisecs)" />
      <submit next="/CVP/Server" method="post" 
   namelist=" audium_vxmlLog" />
    </block>
  </form>
</vxml>
```

#### Gateway Sends a HTTP POST Request as Defined in the Submit Option of VXML Document (2)

```
*Jan 18 03:34:55.667: 
   //127//HTTPC:/httpc_write_stream: 
   Client write buffer fd(4):
POST /CVP/Server HTTP/1.1
Host: 172.18.110.75:7000
Content-Length: 67
Content-Type: 
   application/x-www-form-urlencoded
Cookie: $Version=0; JSESSIONID=
   BBCE0F948ADFDB720497F587A7997538; 
   $Path=/CVP
Connection: close
Accept: text/vxml, text/x-vxml, 
    application/vxml, 
   application/x-vxml, application/voicexml, 
   application/x-voicexml, text/plain, tex
t/html, audio/basic, audio/wav, 
   multipart/form-data, 
   application/octet-stream
User-Agent: Cisco-IOS-C5400/12.4
```

#### Gateway Receives a 200 OK Response for the HTTP POST Request

The message body contains VXML document (3). This VXML document defines a menu prompts that tells the caller to enter 1 or say Refill, or to enter 2 or say pharmacist. The prompts are synthesized by a Text-to-Speech Server. The inputs (speech / DTMF) are recognized with a Automatic Speech Recognizer.

```
*Jan 18 03:34:57.499: 
   processing server rsp msg: 
   msg(67CA6B48)URL:
   http://172.18.110.75:7000/CVP/Server, fd(4):
*Jan 18 03:34:57.499: Request msg: 
   POST /CVP/Server HTTP/1.1
*Jan 18 03:34:57.499: 
   Message Response Code: 200
*Jan 18 03:34:57.499: 
   Message Rsp Decoded Headers:
*Jan 18 03:34:57.499: 
   Date:Mon, 30 Apr 2007 16:58:42 GMT
*Jan 18 03:34:57.499: 
   Content-Type:text/xml;charset=ISO-8859-1
*Jan 18 03:34:57.499: Connection:close
*Jan 18 03:34:57.499: headers:
*Jan 18 03:34:57.499: HTTP/1.1 200 OK
Server: Apache-Coyote/1.1
Content-Type: text/xml;charset=ISO-8859-1
Date: Mon, 30 Apr 2007 16:58:42 GMT
Connection: close
 

*Jan 18 03:34:57.499: body:
*Jan 18 03:34:57.499: ... Buffer too large 
   - truncated to (4096) len.
*Jan 18 03:34:57.499: <?xml version="1.0" 
   encoding="UTF-8"?>
<vxml version="2.0" application=
   "/CVP/Server?audium_root=true&amp;
   calling_into=GoodPrescriptionRefillApp7" 
   xml:lang="en-us">
  <property name="timeout" value="60s" />
  <property name="confidencelevel" value="0.40" />
  <form id="audium_start_form">
    <block>
      <assign name="audium_vxmlLog" expr="''" />
      <assign name="audium_element
   _start_time_millisecs" 
   expr="new Date().getTime()" />
      <goto next="#start" />
    </block>
  </form>
  <form id="start">
    <block>
      <assign name="audium_vxmlLog" 
   expr="audium_vxmlLog 
   + '|||audio_group$$$' + 'initial_audio_group' + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
      <goto nextitem="choice_fld" />
    </block>
    <field name="choice_fld" modal="false">
      <property name="inputmodes" value="dtmf voice" />
      <prompt bargein="true">Say refills or press 1. 

Or. 

Say pharmacist or press 2.</prompt>
      <catch event="nomatch">
        <prompt bargein="true">Sorry. 

I did not understand that.  

Say refills or press 1. 

Say pharmacist or press 2.</prompt>
        <assign name="audium_vxmlLog" 
    expr="audium_vxmlLog 
   + '|||nomatch$$$' + '1' + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
        <assign name="audium_vxmlLog" 
    expr="audium_vxmlLog 
   + '|||audio_group$$$' + 'nomatch_audio_group' 
   + '^^^' + application.getElapsedTime(
   audium_element_start_time_millisecs)" />
      </catch>
      <catch event="nomatch" count="2">
        <prompt bargein="true">
   Sorry, I still did not get that. 

If you are using a speaker phone. 

Please use the phone keypad to make 
   your selection. 

Press 1 for refills.

Press 2 to speak to a pharmacist.</prompt>
        <assign name="audium_vxmlLog" 
   expr="audium_vxmlLog 
   + '|||nomatch$$$' + '2' + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
        <assign name="audium_vxmlLog" 
    expr="audium_vxmlLog 
   + '|||audio_group$$$' + 'nomatch_audio_group' 
   + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
      </catch>
      <catch event="nomatch" count="3">
        <prompt bargein="true">Gee.
 

Looks like we are having some trouble.</prompt>
        <assign name="audium_vxmlLog" 
    expr="audium_vxmlLog 
   + '|||nomatch$$$' + '3' + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
        <assign name="audium_vxmlLog" 
    expr="audium_vxmlLog 
   + '|||audio_group$$$' + 'nomatch_audio_group' 
    + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
        <var name="maxNoMatch" expr="'yes'" />
        <submit next="/CVP/Server" method="post" 
    namelist=" 
   audium_vxmlLog maxNoMatch" />
      </catch>
      <catch event="noinput">
        <prompt bargein="true">Sorry.  

I did not hear that.  

Say refills or press 1. 

Say pharmacist or press 2.</prompt>
        <assign name="audium_vxmlLog" 
    expr="audium_vxmlLog 
   + '|||noinput$$$' + '1' + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
        <assign name="audium_vxmlLog" 
     expr="audium_vxmlLog 
   + '|||audio_group$$$' + 'noinput_audio_group' 
   + '^^^' + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
      </catch>
      <catch event="noinput" count="2">
        <prompt bargein="true">I am sorry. 

I still did not hear that.

If you are using a speaker phone. 

Please use the phone keypad 
   to make your selection. 

Press 1 for refills. 

Press 2 to speak to a pharmacist.</prompt>
        <assign name="audium_vxmlLog" 
   expr="audium_vxmlLog 
   + '|||noinput$$$' + '2' + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
        <assign name="audium_vxmlLog" 
   expr="audium_vxmlLog 
   + '|||audio_group$$$' + 'noinput_
   audio_group' + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
      </catch>
      <catch event="noinput" count="3">
        <prompt bargein="true">Gee. 

Looks like we are having some trouble.</prompt>
        <assign name="audium_vxmlLog" 
   expr="audium_vxmlLog 
   + '|||noinput$$$' + '3' + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
        <assign name="audium_vxmlLog" 
   expr="audium_vxmlLog 
   + '|||audio_group$$$' + 'noinput_
   audio_group' + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
        <var name="maxNoInput" expr="'yes'" />
        <submit next="/CVP/Server" method="post" 
   namelist=" audium_vxmlLog maxNoInput" />
      </catch>
      <option value="refills" dtmf="1">
   prescription</option>
      <option value="refills">refills</option>
      <option value="refills">
   prescription refills</option>
      <option value="refills">
   refill my prescription</option>
      <option value="refills">
   I want to refill my prescription</option>
      <option value="refills">
   refills please</option>
      <option value="Pharmacist" 
   dtmf="2">Pharmacist</option>
      <option value="Pharmacist">
   I want to speak to a pharmacist</option>
      <option value="Pharmacist">
   pharmacist please</option>
      <filled>
        <assign name="audium_vxmlLog" 
   expr="audium_vxmlLog 
   + '|||utterance$$$' + choice_fld$.
   utterance + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
        <assign name="audium_vxmlLog" 
   expr="audium_vxmlLog 
   + '|||inputmode$$$' + choice_fld$.
   inputmode + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
        <assign name="audium_vxmlLog" 
   expr="audium_vxmlLog 
   + '|||interpretation$$$' + choice_fld + '^^^' 
   + application.getElapsedTim
   (audium_element_start_time_millisecs)" />
        <assign name="audium_vxmlLog" 
   expr="audium_vxmlLog 
   + '|||confidence$$$' + choice_fld$.
   confidence + '^^^' 
   + application.getElapsedTime
   (audium_element_start_time_millisecs)" />
        <var name="confidence" 
   expr="choice_fld$.confidence" />
        <submit next="/CVP/Server" method="post" 
   namelist=" audium_vxmlLog confidence choice_fld" />
      </filled>
    </field>
  </form>
</vxml>
```

#### Gateway Creates the Grammars to be Used for DTMF / Speech Recognition

These grammars are then sent to the ASR server once the Gateway establishes a session with the ASR server.

```
*Jan 18 03:34:57.523: 
   //127//AFW_:/vapp_asr_change_server:  
   asr_server=sip:asr@172.18.110.76
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   grammar_id=session:option485@field.grammar
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   xml_lang=en-us
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" encoding="UTF-8"?>
   <grammar version="1.0" xm
lns="http://www.w3.org/2001/06/grammar" 
   xml:lang="en-us" 
   root="root"><rule id="root" scope="public"> 
    prescription</rule></grammar>
*Jan 18 03:34:57.523: //-1//MRCP:/mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, Count=339, 
   Event=0x63ACCCF0
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   grammar_id=session:option486@field.grammar
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" 
   encoding="UTF-8"?>
    <grammar version="1.0" xm
lns="http://www.w3.org/2001/06/grammar" 
   mode="dtmf" root=
   "root"><rule id="root" scope=
   "public">1</rule></grammar>
*Jan 18 03:34:57.523: //-1//MRCP:
   /mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, Count=340, 
   Event=0x63ACCAE8
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   grammar_id=session:option487@field.grammar
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   xml_lang=en-us
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" 
   encoding="UTF-8"?>
   <grammar version="1.0" xm
lns="http://www.w3.org/2001/06/grammar" 
   xml:lang="en-us" 
   root="root"><rule id="root" scope="public"> 
    refills</rule></grammar>
*Jan 18 03:34:57.523: //-1//MRCP
   :/mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, Count=341, 
   Event=0x63ACBC88
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   grammar_id=session:option488@field.grammar
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   xml_lang=en-us
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" encoding="UTF-8"?>
   <grammar version="1.0" xm
lns="http://www.w3.org/2001/06/grammar" 
   xml:lang="en-us" 
   root="root"><rule id="root" scope="public"> 
   prescription refills</rule></grammar>
*Jan 18 03:34:57.523: //-1//MRCP:/mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, Count=342,
   Event=0x63ACBCB0
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   grammar_id=session:option489@field.grammar
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   xml_lang=en-us
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" 
   encoding="UTF-8"?>
   <grammar version="1.0" xm
lns="http://www.w3.org/2001/06/grammar" xml:
   lang="en-us" root="root">
   <rule id="root" scope="public"> 
    refill my prescription</rule><
/grammar>
*Jan 18 03:34:57.523: //-1//MRCP:/mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, 
   Count=343, Event=0x63ACBCD8
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   grammar_id=session:option490@field.grammar
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   xml_lang=en-us
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" encoding="UTF-8"?>
   <grammar version="1.0" xm
lns="http://www.w3.org/2001/06/grammar" 
    xml:lang="en-us" root="root">
   <rule id="root" scope="public"> 
    I want to refill my prescription
   </rule></grammar>
*Jan 18 03:34:57.523: //-1//MRCP:/mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, Count=344, 
   Event=0x63ACBD00
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   grammar_id=session:option491@field.grammar
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   xml_lang=en-us
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" encoding="UTF-8"?>
   <grammar version="1.0" xm
lns="http://www.w3.org/2001/06/grammar" 
  xml:lang="en-us" 
   root="root"><rule id="root" scope="public"> 
   refills please</rule></grammar
> 
*Jan 18 03:34:57.523: //-1//MRCP:/mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, Count=345, 
   Event=0x63ACBD28
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   grammar_id=session:option492@field.grammar
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   xml_lang=en-us
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" 
   encoding="UTF-8"?>
   <grammar version="1.0" xm
lns="http://www.w3.org/2001/06/grammar" 
   xml:lang="en-us" 
   root="root"><rule id="root" 
   scope="public"> Pharmacist
   </rule></grammar>
*Jan 18 03:34:57.523: //-1//MRCP:/mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, Count=346, 
   Event=0x63ACBB20
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   grammar_id=session:option493@field.grammar
*Jan 18 03:34:57.523: 
   //127//AFW_:/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.523: 
   //127//AFW_:/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.523: 
   //127//AFW_:/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" 
   encoding="UTF-8"?>
   <grammar version="1.0" xm
lns="http://www.w3.org/2001/06/grammar" 
   mode="dtmf" root="root">
   <rule id="root" scope=
   "public">2</rule></grammar>
*Jan 18 03:34:57.523: //-1//MRCP:/mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, 
   Count=347, Event=0x63ACBD50
*Jan 18 03:34:57.523: 
   //127//AFW_:/vapp_asr_define_grammar: 
*Jan 18 03:34:57.523: 
   //127//AFW_:/vapp_asr_define_grammar:  
   grammar_id=session:
   option494@field.grammar
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   xml_lang=en-us
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" 
   encoding="UTF-8"?>
   <grammar version="1.0" xm
lns="http://www.w3.org/2001/06/grammar" 
   xml:lang="en-us" 
   root="root"><rule id="root" scope="public"> 
   I want to speak to a pharmacist
   </rule></grammar>
*Jan 18 03:34:57.523: //-1//MRCP:/mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, 
   Count=348, Event=0x63ACBFF8
*Jan 18 03:34:57.523: //127//AFW_
   :/vapp_asr_define_grammar: 
*Jan 18 03:34:57.527: //127//AFW_
   :/vapp_asr_define_grammar:  
   grammar_id=session:option495@field.grammar
*Jan 18 03:34:57.527: //127//AFW_
   :/vapp_asr_define_grammar:  
   xml_lang=en-us
*Jan 18 03:34:57.527: //127//AFW_
   :/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.527: //127//AFW_
   :/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.527: //127//AFW_
   :/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" 
   encoding="UTF-8"?>
   <grammar version="1.0" xm
lns="http://www.w3.org/2001/06/grammar" 
   xml:lang="en-us" 
   root="root"><rule id="root" scope="public"> 
   pharmacist please
   </rule></grammar>

*Jan 18 03:34:57.527: 
   //-1//MRCP:/mrcp_get_ev:

   ****>Caller PC=0x61BE1F94, 
   Count=349, Event=0x63ACC048
*Jan 18 03:34:57.527: //127//AFW_
   :/vapp_asr_define_grammar: 
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar:  
   grammar_id=session:link496@document.grammar
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar:  
   xml_lang=en-us
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" 
   encoding="UTF-8"?>
   <grammar xmlns="http://ww
w.w3.org/2001/06/grammar" mode="voice" 
   version="1.0" 
   root="Hotlink_02_VOICE" xml:lang="en-us">
      <rule id="Hotlink_02_VOICE" scope="public">
        <one-of>
          <item>operator</item>
          <item>agent</item>
          <item>pharmacist</item>
        </one-of>
      </rule>
    </grammar>
*Jan 18 03:34:57.527: //-1//MRCP:/mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, Count=350, 
   Event=0x63ACC098
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar:
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar:  
   grammar_id=session:link497@document.grammar
*Jan 18 03:34:57.527:
   //127//AFW_:/vapp_asr_define_grammar:  
   xml_lang=en-us
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar:  
   remoteupdate=0
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" encoding="UTF-8"?>
   <grammar xmlns="http://ww
w.w3.org/2001/06/grammar" mode="voice" version="1.0" 
   root="Hotlink_01_VOICE" xml:lang="en-us">
      <rule id="Hotlink_01_VOICE" scope="public">
        <one-of>
          <item>operator</item>
          <item>agent</item>
          <item>pharmacist</item>
        </one-of>
      </rule>
    </grammar>
*Jan 18 03:34:57.527: 
   //-1//MRCP:/mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, Count=351, 
   Event=0x63ACC0C0
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar: 
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar:  
   grammar_id=session:help@grammar
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar:  
   xml_lang=en-us
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar:  
   encoding_name=UTF-8
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar:  
   remoteupdate=1
*Jan 18 03:34:57.527: 
   //127//AFW_:/vapp_asr_define_grammar: 
   grammar=<?xml version="1.0" 
   encoding="UTF-8"?>
   <grammar version="1.0" xm
lns="http://www.w3.org/2001/06/grammar" 
   xml:lang="en-us" 
   root="root"><rule id="root" 
   scope="public">
   help</rule></grammar>
*Jan 18 03:34:57.527: 
   //-1//MRCP:/mrcp_get_ev:
   ****>Caller PC=0x61BE1F94, Count=352, 
   Event=0x63ACBEE0
*Jan 18 03:34:57.527: //127//AFW_:/vapp_asr: 
   grammar_id=session:option485@field.grammar
grammar_id=session:option486@field.grammar
grammar_id=session:option487@field.grammar
grammar_id=session:option488@field.grammar
grammar_id=session:option489@field.grammar
grammar_id=session:option490@field.grammar
grammar_id=session:option491@field.grammar
grammar_id=session:option492@field.grammar
grammar_id=session:option493@field.grammar
grammar_id=session:option494@field.grammar
grammar_id=session:option495@field.grammar
grammar_id=session:link496@document.grammar
grammar_id=session:link497@document.grammar
grammar_id=session:help@grammar
```

#### Gateway Performs a Dial-Peer Lookup to Setup a SIP Session with the Text-to-Speech Server

The outbound dial-peer 6 is matched.

```
*Jan 18 03:34:57.527: 
   //-1/xxxxxxxxxxxx/CCAPI/ccCallSetupRequest:

   Destination Pattern=, 
   Called Number=sip:tts@172.18.110.76, 
   Digit Strip=FALSE

*Jan 18 03:34:57.527: 
   //-1/xxxxxxxxxxxx/CCAPI/ccCallSetupRequest:

   Calling Number=5555(TON=Unknown, NPI=Unknown, 
   Screening=Not Screened, 

   Presentation=Allowed),

   Called Number=sip:tts@172.18.110.76(TON=Unknown, 
   NPI=ISDN),

   Redirect Number=, Display Info=

   Account Number=, Final Destination Flag=TRUE,

   Guid=2AEE8C2A-0AFB-11D6-801C-0013803E8C8E, 
   Outgoing Dial-peer=6

*Jan 18 03:34:57.531: 
   //-1/xxxxxxxxxxxx/CCAPI/cc
   _api_display_ie_subfields:

   ccCallSetupRequest:

   cisco-username=

   ----- ccCallInfo IE subfields -----

   cisco-ani=5555

   cisco-anitype=0

   cisco-aniplan=0

   cisco-anipi=0

   cisco-anisi=0

   dest=sip:tts@172.18.110.76

   cisco-desttype=0

   cisco-destplan=1

   cisco-rdie=FFFFFFFF

   cisco-rdn=

   cisco-rdntype=-1

   cisco-rdnplan=-1

   cisco-rdnpi=-1

   cisco-rdnsi=-1

   cisco-redirectreason=-1   fwd_final_type =0

   final_redirectNumber =

   hunt_group_timeout =0

 

*Jan 18 03:34:57.531: 
    //-1/xxxxxxxxxxxx/CCAPI/
   ccIFCallSetupRequestPrivate:

   Interface=0x662CE538, Interface Type=3, 
   Destination=, Mode=0x0,

   Call Params(Calling Number=5555,
   (Calling Name=)(TON=Unknown, 
   NPI=Unknown, Screening=Not Screened, 
   Presentation=Allowed),

   Called Number=sip:tts@172.18.110.76
   (TON=Unknown, NPI=ISDN), 
   Calling Translated=FALSE,

   Subscriber Type Str=RegularLine, 
   FinalDestinationFlag=TRUE, 
   Outgoing Dial-peer=6, Call Count On=FALSE,

   Source Trkgrp Route Label=, 
   Target Trkgrp Route Label=, 
   tg_label_flag=0, Application Call Id=)
```

#### Gateway Sends a SIP INVITE to the TTS Server

The SDP of the INVITE message contains media information for the Audio stream and MRCPv2 application (speechsynth channel).

```
*Jan 18 03:34:57.531: 
   //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:

Sent: 

INVITE sip:tts@172.18.110.76:5060 SIP/2.0

Via: SIP/2.0/UDP 14.1.16.25:
   5060;branch=z9hG4bK931F1D

Remote-Party-ID: <sip:5555@14.1.16.25>;
   party=calling;screen=no;privacy=off

From: <sip:5555@14.1.16.25>
   ;tag=E54D43C-1EC4

To: sip:tts@172.18.110.76

Date: Fri, 18 Jan 2002 03:34:57 GMT

Call-ID: 2DCA5BEF-AFB11D6-80D3DC30
   -3585E95A@14.1.16.25

Supported: 100rel,timer,
   resource-priority,replaces

Min-SE:  1800

Cisco-Guid: 720276522-184226262
   -2149318675-2151582862

User-Agent: Cisco-SIPGateway/IOS-12.x

Allow: INVITE, OPTIONS, BYE, 
   CANCEL, ACK, PRACK, UPDATE, 
   REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER

CSeq: 101 INVITE

Max-Forwards: 70

Timestamp: 1011324897

Contact: <sip:5555@14.1.16.25:5060>

Expires: 180

Allow-Events: telephone-event

Content-Type: application/sdp

Content-Disposition: 
   session;handling=required

Content-Length: 358

 

v=0

o=CiscoSystemsSIP-GW-UserAgent 
   6021 4611 IN IP4 14.1.16.25

s=SIP Call

c=IN IP4 14.1.16.25

t=0 0

m=audio 16984 RTP/AVP 0 101

c=IN IP4 14.1.16.25

a=rtpmap:0 PCMU/8000

a=rtpmap:101 telephone-event/8000

a=fmtp:101 0-16

a=ptime:20

a=recvonly

a=mid:1

m=application 9 TCP/MRCPv2

a=setup:active

a=connection:new

a=resource:speechsynth

a=cmid:1
```

#### Gateway Performs a Dial-Peer Lookup to Set up a SIP Session with the ASR Server

The outbound dial-peer 5 is matched.

```
*Jan 18 03:34:57.531: 
   //-1/xxxxxxxxxxxx/CCAPI/ccCallSetupRequest:

   Destination Pattern=, 
    Called Number=sip:asr@172.18.110.76, 
   Digit Strip=FALSE

*Jan 18 03:34:57.531: 
   //-1/xxxxxxxxxxxx/CCAPI/ccCallSetupRequest:

   Calling Number=5555(TON=Unknown, NPI=Unknown, 
   Screening=Not Screened, Presentation=Allowed),

   Called Number=sip:asr@172.18.110.76
   (TON=Unknown, NPI=ISDN),

   Redirect Number=, Display Info=

   Account Number=, Final Destination Flag=TRUE,

   Guid=2AEE8C2A-0AFB-11D6-801C-0013803E8C8E, 
   Outgoing Dial-peer=5

*Jan 18 03:34:57.531: 
    //-1/xxxxxxxxxxxx/CCAPI/cc_api
   _display_ie_subfields:

   ccCallSetupRequest:

   cisco-username=

   ----- ccCallInfo IE subfields -----

   cisco-ani=5555

   cisco-anitype=0

   cisco-aniplan=0

   cisco-anipi=0

   cisco-anisi=0

   dest=sip:asr@172.18.110.76

   cisco-desttype=0

   cisco-destplan=1

   cisco-rdie=FFFFFFFF

   cisco-rdn=

   cisco-rdntype=-1

   cisco-rdnplan=-1

   cisco-rdnpi=-1

   cisco-rdnsi=-1

   cisco-redirectreason=-1   
   fwd_final_type =0

   final_redirectNumber =

   hunt_group_timeout =0

 

*Jan 18 03:34:57.535: 
    //-1/xxxxxxxxxxxx/CCAPI
   /ccIFCallSetupRequestPrivate:

   Interface=0x662CE538, Interface Type=3, 
   Destination=, Mode=0x0,

   Call Params(Calling Number=5555,
   (Calling Name=)(TON=Unknown, 
   NPI=Unknown, Screening=Not Screened, 
   Presentation=Allowed),

   Called Number=sip:asr@172.18.110.76
   (TON=Unknown, NPI=ISDN), 
   Calling Translated=FALSE,

   Subscriber Type Str=RegularLine, 
   FinalDestinationFlag=TRUE, 
   Outgoing Dial-peer=5, Call Count On=FALSE,

   Source Trkgrp Route Label=, 
   Target Trkgrp Route Label=, 
   tg_label_flag=0, Application Call Id=)
```

#### Gateways Sends a SIP INVITE to ASR Server

The SDP contains the media information for the audio stream, DTMF relay. and MRCPv2 Application (speechrecog channel).

```
*Jan 18 03:34:57.535: 
    //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:

Sent: 

INVITE sip:asr@172.18.110.76:5060 SIP/2.0

Via: SIP/2.0/UDP 
   14.1.16.25:5060;branch=z9hG4bK94C0B

Remote-Party-ID: <sip:5555@14.1.16.25>;
    party=calling;screen=no;privacy=off

From: <sip:5555@14.1.16.25>;tag=E54D440-1CDB

To: sip:asr@172.18.110.76

Date: Fri, 18 Jan 2002 03:34:57 GMT

Call-ID: 2DCAF817-AFB11D6
   -80D5DC30-3585E95A@14.1.16.25

Supported: 100rel,timer,
   resource-priority,replaces

Min-SE:  1800

Cisco-Guid: 720276522-184226262-
   2149318675-2151582862

User-Agent: Cisco-SIPGateway/IOS-12.x

Allow: INVITE, OPTIONS, BYE, CANCEL, 
   ACK, PRACK, UPDATE, 
   REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER

CSeq: 101 INVITE

Max-Forwards: 70

Timestamp: 1011324897

Contact: <sip:5555@14.1.16.25:5060>

Expires: 180

Allow-Events: telephone-event

Content-Type: application/sdp

Content-Disposition: 
   session;handling=required

Content-Length: 358

 

v=0

o=CiscoSystemsSIP-GW-UserAgent 
   6805 2057 IN IP4 14.1.16.25

s=SIP Call

c=IN IP4 14.1.16.25

t=0 0

m=audio 19994 RTP/AVP 0 101

c=IN IP4 14.1.16.25

a=rtpmap:0 PCMU/8000

a=rtpmap:101 telephone-event/8000

a=fmtp:101 0-16

a=ptime:20

a=sendonly

a=mid:1

m=application 9 TCP/MRCPv2

a=setup:active

a=connection:new

a=resource:speechrecog

a=cmid:1
```

#### Gateway Receives a 200 OK Response (for the SIP INVITE) from the ASR Server

G711ulaw codec, IP address and RTP port numbers for the audio stream.

The direction attribute of this RTP stream is "recvonly".

RTP-NTE based DTMF Relay.

TCP Port number (51001) to be used by the Gateway to establish a MRCPv2 session with ASR server.

```
*Jan 18 03:34:57.559: 
   //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:

Received: 

SIP/2.0 200 OK

Via: SIP/2.0/UDP 14.1.16.25:5060;
   branch=z9hG4bK94C0B

To: <sip:asr@172.18.110.76>;tag=a99d0500

From: <sip:5555@14.1.16.25>;tag=E54D440-1CDB

Call-ID: 2DCAF817-AFB11D6-80D5DC30-
   3585E95A@14.1.16.25

CSeq: 101 INVITE

Contact: <sip:172.18.110.76:5060>

Content-Type: application/sdp

Content-Length: 342

 

v=0

o=MRCPv2Server 3386937590 3386937590 
   IN IP4 172.18.110.76

s=SIP Call

c=IN IP4 172.18.110.76

t=3386937590 0

m=audio 10002 RTP/AVP 0 101

a=rtpmap:0 PCMU/8000

a=rtpmap:101 telephone-event/8000

a=recvonly

m=application 51001 TCP/MRCPv2 

a=connection:new

a=setup:passive

a=model:besteffort

a=channel:000023B846361276@speechrecog
```

#### Gateway Sends SIP ACK to the ASR Server

The SIP session for the ASR gets established between the Gateway and the ASR server.

```
*Jan 18 03:34:57.563: 
   //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:

Sent: 

ACK sip:172.18.110.76:5060 SIP/2.0

Via: SIP/2.0/UDP 14.1.16.25:5060;branch=z9hG4bK9520FA

From: <sip:5555@14.1.16.25>;tag=E54D440-1CDB

To: <sip:asr@172.18.110.76>;tag=a99d0500

Date: Fri, 18 Jan 2002 03:34:57 GMT

Call-ID: 2DCAF817-AFB11D6-80D5DC30-3585E95A@14.1.16.25

Max-Forwards: 70

CSeq: 101 ACK

Allow-Events: telephone-event

Content-Length: 0
```

#### Gateway Sends "DEFINE-GRAMMER" MRCP Request to ASR Server

Just one request is shown here.

```
MRCP/2.0 446      DEFINE-GRAMMAR  1

Channel-Identifier: 000023B846361276@speechrecog

:

Speech-Language: en-us

Content-Base: http://172.18.110.75:7000/CVP/

:

Content-Type: application/srgs+xml

Content-Id: option485@field.grammar

Content-Length: 193

 

:

<?xml version="1.0" encoding="UTF-8"?>
   <grammar version="1.0" 
   mlns="http://www.w3.org/2001/06/grammar" 
   xml:lang="en-us" root="root"

><rule id="root" scope="public"> 
   prescription</rule></grammar>
```

#### Gateway Receives a 200 COMPLETE Response for its DEFINE-GRAMMAR Request

```
*Jan 18 03:34:57.587: //-1//MRCP:/hash_get:

   Table=mrcpv2_socket_connect_table, Key=0:

MRCP/2.0 80 1 200 COMPLETE

Channel-Identifier: 000023B846361276@speechrecog
```

#### Gateway Receives a 200 OK Response (for the SIP INVITE) from the TTS Server

The SDP of the SIP INVITE message specifies these:

G711ulaw codec, IP address and RTP port numbers for the audio stream.

The direction attribute of this RTP stream is "sendonly".

RTP-NTE based DTMF Relay

TCP Port number (51000) to be used by the Gateway to establish a MRCPv2 session with TTS server.

```
*Jan 18 03:34:57.591: 
   //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:

Received: 

SIP/2.0 200 OK

Via: SIP/2.0/UDP 14.1.16.25:5060;
   branch=z9hG4bK931F1D

To: <sip:tts@172.18.110.76>;tag=c1160600

From: <sip:5555@14.1.16.25>;tag=E54D43C-1EC4

Call-ID: 2DCA5BEF-AFB11D6-80D3DC30-
   3585E95A@14.1.16.25

CSeq: 101 INVITE

Contact: <sip:172.18.110.76:5060>

Content-Type: application/sdp

Content-Length: 342

 

v=0

o=MRCPv2Server 3386937590 3386937590 
   IN IP4 172.18.110.76

s=SIP Call

c=IN IP4 172.18.110.76

t=3386937590 0

m=audio 10000 RTP/AVP 0 101

a=rtpmap:0 PCMU/8000

a=rtpmap:101 telephone-event/8000

a=sendonly

m=application 51000 TCP/MRCPv2 

a=connection:new

a=setup:passive

a=model:besteffort

a=channel:000023EC46361276@speechsynth
```

#### Gateway Sends SIP ACK to the TTS Server

The SIP session for the Text-to-Speech gets established between the Gateway and the TTS server.

```
*Jan 18 03:34:57.595: 
   //-1/xxxxxxxxxxxx/SIP/
   Msg/ccsipDisplayMsg:

Sent: 

ACK sip:172.18.110.76:5060 SIP/2.0

Via: SIP/2.0/UDP 14.1.16.25:5060;
   branch=z9hG4bK9626BC

From: <sip:5555@14.1.16.25>;tag=E54D43C-1EC4

To: <sip:tts@172.18.110.76>;tag=c1160600

Date: Fri, 18 Jan 2002 03:34:57 GMT

Call-ID: 2DCA5BEF-AFB11D6-80D3DC30
   -3585E95A@14.1.16.25

Max-Forwards: 70

CSeq: 101 ACK

Allow-Events: telephone-event

Content-Length: 0
```

#### Gateway Sends "RECOGNIZE" MRCP Request to ASR Server

```
MRCP/2.0 987      
   RECOGNIZE  15

Channel-Identifier: 
   000023B846361276@speechrecog

:

Speech-Language: en-us

Confidence-Threshold: 0.40

Sensitivity-Level: 0.50

Speed-Vs-Accuracy: 0.50

Cancel-If-Queue: false

Dtmf-Interdigit-Timeout: 10000

Dtmf-Term-Timeout: 0

Dtmf-Term-Char: #

No-Input-Timeout: 60000

N-Best-List-Length: 1

Logging-Tag: 127:127

Accept-Charset: charset: utf-8

Content-Base: 
   http://172.18.110.75:7000/CVP/

Media-Type: audio/basic

Start-Input-Timers: false

:

Content-Type: text/uri-list

Content-Length: 453

 

:

session:option485@field.grammar

session:option486@field.grammar

session:option487@field.grammar

session:option488@field.grammar

session:option489@field.grammar

session:option490@field.grammar

session:option491@field.grammar

session:option492@field.grammar

session:option493@field.grammar

session:option494@field.grammar

session:option495@field.grammar

session:link496@document.grammar

session:link497@document.grammar

session:help@grammar
```

#### ASR Server Sends "IN PROGRESS" Response (for RECOGNISE Request) to the Gateway

```
MRCP/2.0 84 15 200 IN-PROGRESS

Channel-Identifier: 
   000023B846361276@speechrecog
```

#### Gateway Finishes the Download of the Welcome-1.wav Media File

It stores it in the cache and plays the prompt to the caller.

```
*Jan 18 03:35:04.335: 
   //127//HTTPC:/httpc_is_cached: 
   HTTPC_FILE_IS_CACHED

*Jan 18 03:35:04.335: //-1//HTTPC:
   /httpc_set_cache_revoke_cb: 
   Registering revoke_callback(0x61CDD948)
   +pcontext(0x63A7AAA8) for cach

ep(0x68734930)

*Jan 18 03:35:04.335: //127//AFW_:/vapp_driver: 
   evtID: 146 vapp record state: 0

 

*Jan 18 03:35:04.335: //127//AFW_:/vapp_play_done: 
   evID=146 reason=17, 
   protocol=5, status_code=0, dur=3291, rate=0

*Jan 18 03:35:04.335: //127/2AEE8C2A801C/VXML:
   /vxml_media_done:
```

#### Gateway Sends the "SPEAK" MRCP Request to the TTS Server to Play the Thank-You Prompt

```
MRCP/2.0 376      SPEAK  1

Channel-Identifier: 
   000023EC46361276@speechsynth

:

Kill-On-Barge-In: true

Speech-Language: en-us

Logging-Tag: 127:127

Content-Base: 
   http://172.18.110.75:7000/CVP/

:

Content-Type: application/ssml+xml

Content-Length: 123

 

:

<?xml version="1.0" encoding="UTF-8"?>
   <speak version="1.0" xml:lang="en-us"> 
   Thank you for calling Audium pharmacy.</speak>
```

#### The TTS Server sends the "IN-PROGRESS"Response for the SPEAK Request

```
MRCP/2.0 83 1 200 IN-PROGRESS

Channel-Identifier: 
   000023EC46361276@speechsynth
```

#### The TTS Server Sends the "SPEAK-COMPLETE" Message After it has Spoken the Thank-You Prompt

```
MRCP/2.0 141 SPEAK-COMPLETE 1 COMPLETE

Channel-Identifier: 
   000023EC46361276@speechsynth

Completion-Cause: 000 normal

Speech-Marker: ""
```

#### The PSTN Caller Enters “1” to Choose Refill

Gateway sends this digit as a RTP-NTE event to the ASR server.

```
*Jan 18 03:35:12.583:          
   s=DSP d=VoIP payload 0x65 ssrc 
   0x15 sequence 0x1E9B timestamp 0x2FADCC60

*Jan 18 03:35:12.583:          Pt:101    Evt:1       
   Pkt:03 00 00  <Snd>>>

*Jan 18 03:35:12.587:          
   s=DSP d=VoIP payload 0x65 ssrc 
   0x15 sequence 0x1E9C timestamp 0x2FADCC60

*Jan 18 03:35:12.587:          Pt:101    Evt:1       
   Pkt:03 00 00  <Snd>>>

*Jan 18 03:35:12.631:          
   s=DSP d=VoIP payload 0x65 ssrc 
   0x15 sequence 0x1E9E timestamp 0x2FADCC60

*Jan 18 03:35:12.631:          Pt:101    Evt:1       
    Pkt:03 01 90  <Snd>>>

*Jan 18 03:35:12.683:          
   s=DSP d=VoIP payload 0x65 ssrc 
   0x15 sequence 0x1E9F timestamp 0x2FADCC60

*Jan 18 03:35:12.683:          Pt:101    Evt:1       
   Pkt:03 03 20  <Snd>>>

*Jan 18 03:35:12.703:          
   s=DSP d=VoIP payload 0x65 ssrc 
   0x15 sequence 0x1EA0 timestamp 0x2FADCC60

*Jan 18 03:35:12.703:          Pt:101    Evt:1       
   Pkt:83 03 38  <Snd>>>

*Jan 18 03:35:12.707:          s=DSP d=VoIP payload 
   0x65 ssrc 0x15 sequence 0x1EA1 timestamp 0x2FADCC60

*Jan 18 03:35:12.707:          Pt:101    Evt:1       
   Pkt:83 03 38  <Snd>>>

*Jan 18 03:35:12.711:          s=DSP d=VoIP payload 
   0x65 ssrc 0x15 sequence 
   0x1EA2 timestamp 0x2FADCC60

*Jan 18 03:35:12.711:          Pt:101    Evt:1       
   Pkt:83 03 38  <Snd>>>
```

#### ASR Server Sends a "RECOGNITION-COMPLETE" Message to the Gateway

This notifies the gateway that it has recognized one of the requested events (in this case digit 1).

```
MRCP/2.0 513 
   RECOGNITION-COMPLETE 15 COMPLETE

Channel-Identifier: 
   000023B846361276@speechrecog

Proxy-Sync-Id: 0B82553000000027

Completion-Cause: 000 success

Content-Type: application/nlsml+xml

Content-Length: 292

 

<?xml version="1.0" encoding="UTF-8"?>

<result grammar="session:option486@field.grammar">

        <interpretation grammar=
   "session:option486@field.grammar" 
   confidence="0.000000">

                <instance>

                        1

                </instance>

                <input mode="dtmf" 
   confidence="1.000000">

                        1

                </input>

        </interpretation>

</result>
```

#### The VXML Gateway Receives a Successful Recognition Notification from the ASR Server

After the receipt of this notification, the VXML Gateway sends a HTTP POST request as specified in the SUBMIT tag of VXML document (3). This POST request informs the VXML server that digit 1 was entered by the PSTN caller.

```
*Jan 18 03:35:12.863: 
   //127/2AEE8C2A801C/VXML:/vxml_vapp_bgpost:  

   url http://172.18.110.75:7000/CVP/Server 
   cachable 1 timeout 
   0 body audium_vxmlLog=%7C%7C%7Caudio
   _group$$$initial_audio_group%5E%

5E%5E4%7C%7C%7Cutterance$$$1%5E%5E%5E153
   40%7C%7C%7Cinputmode
   $$$dtmf%5E%5E%5E15344%7C%7C%7C
   interpretation$$$refills%5E%5E%5E15344%7C

%7C%7Cconfidence$$$0%5E%5E%5E15344&confidence=
   0&choice_fld=refills 
   len 258maxage -1 maxstale -1

*Jan 18 03:35:12.863: //127//AFW_:/vapp_bgpost: 
   url=http://172.18.110.75:7000/CVP/Server; 
   mime_type=application/x-www-form-urlencod

ed; len=258; iov_base=audium_vxmlLog=%7C%7C%7Caudio_
   group$$$initial_audio_group
   %5E%5E%5E4%7C%7C%7Cutterance
   $$$1%5E%5E%5E15340%7C%7C

%7Cinputmode$$$dtmf%5E%5E%5E15344%
   7C%7C%7Cinterpretation$$$refills
   %5E%5E%5E15344%7C%7C%7Cconfidence$$$0
   %5E%5E%5E15344&confidence=0&

choice_fld=refills

 

*Jan 18 03:35:12.931: 
   about to send data to the socket 3 
   : first 400 bytes of data: 

POST /CVP/Server HTTP/1.1

Host: 172.18.110.75:7000

Content-Length: 258

Content-Type: application/x-www-form-urlencoded

Cookie: $Version=0; JSESSIONID=
   BBCE0F948ADFDB720497F587A7997538; 
   $Path=/CVP

Connection: close

Accept: text/vxml, text/x-vxml, application/vxml, 
   application/x-vxml, 
   application/voicexml, application/x-voicexml, 
   text/plain, tex

t/html, audio/basic, audio/wav, multipart/form-dat
```

#### The ASR Recognizes the 4-digit Prescription Number

The ASR sends a RECOGNITION-COMPLETE MRCP message to the IOS VXML Gateway.

```
MRCP/2.0 533 
   RECOGNITION-COMPLETE 21 COMPLETE

Channel-Identifier: 
   000023B846361276@speechrecog

Proxy-Sync-Id: 0B82553000000028

Completion-Cause: 000 success

Content-Type: application/nlsml+xml

Content-Length: 312

 

<?xml version="1.0" encoding="UTF-8"?>

<result grammar=
   "session:field498@field.grammar">

        <interpretation grammar=
   "session:field498@field.grammar" 
   confidence="0.738968">

                <instance>

                        1234

                </instance>

                <input mode="speech" 
   confidence="0.752155">

                        one two three four

                </input>

        </interpretation>

</result>

 

    The final VXML document sent by the 
   VXML server contains just the 
   <exit\> tag in the <form>

    This tells the Gateway to
   terminate the VXML session
```

#### The Last VXML Document Sent by the VXML Server Contains Just the Exit Tag in the Form

This tells the Gateway to terminate the VXML session

```
*Jan 18 03:36:07.159: 
   processing server rsp msg: 
   msg(67CA85F8)URL:
   http://172.18.110.75:7000/CVP/Server, fd(3):

*Jan 18 03:36:07.159: Request msg: 
   POST /CVP/Server HTTP/1.1

*Jan 18 03:36:07.159: 
   Message Response Code: 200

*Jan 18 03:36:07.159: 
   Message Rsp Decoded Headers:

*Jan 18 03:36:07.159: D
   ate:Mon, 30 Apr 2007 16:59:53 GMT

*Jan 18 03:36:07.159: 
   Content-Type:text/xml;charset=ISO-8859-1

*Jan 18 03:36:07.159: Connection:close

*Jan 18 03:36:07.159: Set-Cookie:
   JSESSIONID=NULL; 
   Expires=Thu, 01-Jan-1970 
   00:00:10 GMT; Path=/CVP

*Jan 18 03:36:07.159: headers:

*Jan 18 03:36:07.159: HTTP/1.1 200 OK

Server: Apache-Coyote/1.1

Set-Cookie: JSESSIONID=NULL; Expires=Thu, 
   01-Jan-1970 00:00:10 GMT; Path=/CVP

Content-Type: text/xml;charset=ISO-8859-1

Date: Mon, 30 Apr 2007 16:59:53 GMT

Connection: close

 

 

*Jan 18 03:36:07.159: body:

*Jan 18 03:36:07.159: <?xml version="1.0" 
   encoding="UTF-8"?>

<vxml version="2.0" xml:lang="en-us">

  <catch event="vxml.session.error">

    <exit />

  </catch>

  <catch event="telephone.disconnect.hangup">

    <exit />

  </catch>

  <catch event="telephone.disconnect">

    <exit />

  </catch>

  <catch event="error.unsupported.object">

    <exit />

  </catch>

  <catch event="error.unsupported.language">

    <exit />

  </catch>

  <catch event="error.unsupported.format">

    <exit />

  </catch>

  <catch event="error.unsupported.element">

    <exit />

  </catch>

  <catch event="error.unsupported.builtin">

    <exit />

  </catch>

  <catch event="error.unsupported">

    <exit />

  </catch>

  <catch event="error.semantic">

    <exit />

  </catch>

  <catch event="error.noresource">

    <exit />

  </catch>

  <catch event="error.noauthorization">

    <exit />

  </catch>

  <catch event="error.eventhandler.notfound">

    <exit />

  </catch>

  <catch event="error.connection.noroute">

    <exit />

  </catch>

  <catch event="error.connection.noresource">

    <exit />

  </catch>

  <catch event="error.connection.nolicense">

    <exit />

  </catch>

  <catch event="error.connection.noauthorization">

    <exit />

  </catch>

  <catch event="error.connection.baddestination">

    <exit />

  </catch>

  <catch event="error.condition.baddestination">

    <exit />

  </catch>

  <catch event="error.com.cisco.
   media.resource.unavailable">

    <exit />

  </catch>

  <catch event=
   "error.com.cisco.handoff.failure">

    <exit />

  </catch>

  <catch event=
   "error.com.cisco.callhandoff.failure">

    <exit />

  </catch>

  <catch event=
   "error.com.cisco.aaa.authorize.failure">

    <exit />

  </catch>

  <catch event=
   "error.com.cisco.aaa.authenticate.failure">

    <exit />

  </catch>

  <catch event="error.badfetch.https">

    <exit />

  </catch>

  <catch event="error.badfetch.http">

    <exit />

  </catch>

  <catch event="error.badfetch">

    <exit />

  </catch>

  <catch event="error">

    <exit />

  </catch>

  <catch event="disconnect.com.cisco.handoff">

    <exit />

  </catch>

  <catch event="connection.disconnect.hangup">

    <exit />

  </catch>

  <catch event="connection.disconnect">

    <exit />

  </catch>

  <form>

    <block>

      <exit />

    </block>

  </form>

</vxml>
```

#### Gateway Terminates the VXML Application

```
*Jan 18 03:36:14.155: 
   //127/2AEE8C2A801C/VXML:/vxml_vapp_terminate:  

   vapp_status=0 ref_count 0

*Jan 18 03:36:14.155: 
   //127//AFW_:/vapp_terminate: 

*Jan 18 03:36:14.155: //127//AFW_
   :/vapp_session_exit_event_name: 
   Exit Event vxml.session.complete

*Jan 18 03:36:14.155: 
    //127//AFW_:/AFW_M_VxmlModule_Terminate: 

*Jan 18 03:36:14.155: 
    //131/2AEE8C2A801C/CCAPI/ccCallDisconnect:

   Cause Value=16, Tag=0x0, Call Entry
   (Previous Disconnect Cause=0, 
   Disconnect Cause=0)

*Jan 18 03:36:14.155: 
    //131/2AEE8C2A801C/CCAPI/ccCallDisconnect:

   Cause Value=16, Call Entry(Responsed=TRUE, 
   Cause Value=16)
```

#### Gateway Disconnects the SIP Session Established with the ASR Server

```
*Jan 18 03:36:14.159: 
   //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:

Sent: 

BYE sip:172.18.110.76:5060 SIP/2.0

Via: SIP/2.0/UDP 14.1.16.25:
   5060;branch=z9hG4bK971131

From: <sip:5555@14.1.16.25>;tag=E54D440-1CDB

To: <sip:asr@172.18.110.76>;tag=a99d0500

Date: Fri, 18 Jan 2002 03:34:57 GMT

Call-ID: 2DCAF817-AFB11D6-80D5DC30-
   3585E95A@14.1.16.25

User-Agent: Cisco-SIPGateway/IOS-12.x

Max-Forwards: 70

Timestamp: 1011324974

CSeq: 102 BYE

Reason: Q.850;cause=16

Content-Length: 0

 

*Jan 18 03:36:14.607: 
   //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:

Received: 

SIP/2.0 200 OK

Via: SIP/2.0/UDP 14.1.16.25:
   5060;branch=z9hG4bK971131

To: <sip:asr@172.18.110.76>;tag=a99d0500

From: <sip:5555@14.1.16.25>;tag=E54D440-1CDB

Call-ID: 2DCAF817-AFB11D6-80D5DC30-
   3585E95A@14.1.16.25

CSeq: 102 BYE

Contact: <sip:172.18.110.76:5060>

Content-Length: 0
```

#### Gateway Disconnects the SIP Session Established with the TTS Server

```
*Jan 18 03:36:14.159: 
   //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:

Sent: 

BYE sip:172.18.110.76:5060 SIP/2.0

Via: SIP/2.0/UDP 14.1.16.25:5060;branch=z9hG4bK981487

From: <sip:5555@14.1.16.25>;tag=E54D43C-1EC4

To: <sip:tts@172.18.110.76>;tag=c1160600

Date: Fri, 18 Jan 2002 03:34:57 GMT

Call-ID: 2DCA5BEF-AFB11D6-
   80D3DC30-3585E95A@14.1.16.25

User-Agent: Cisco-SIPGateway/IOS-12.x

Max-Forwards: 70

Timestamp: 1011324974

CSeq: 102 BYE

Reason: Q.850;cause=16

Content-Length: 0

 

*Jan 18 03:36:14.215: 
   //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:

Received: 

SIP/2.0 200 OK

Via: SIP/2.0/UDP 
   14.1.16.25:5060;branch=z9hG4bK981487

To: <sip:tts@172.18.110.76>;tag=c1160600

From: <sip:5555@14.1.16.25>;tag=E54D43C-1EC4

Call-ID:
   2DCA5BEF-AFB11D6-80D3DC30-3585E95A@14.1.16.25

CSeq: 102 BYE

Contact: <sip:172.18.110.76:5060>

Content-Length: 0
```

#### Gateway Disconnects the Call on the ISDN Side

```
*Jan 18 03:36:14.611: ISDN Se3/0:23 Q931: TX -> 
   DISCONNECT pd = 8  callref = 0x805A 

        Cause i = 0x8090 - Normal call clearing

*Jan 18 03:36:14.623: ISDN Se3/0:23 Q931: 
   RX <- RELEASE pd = 8  callref = 0x005A

*Jan 18 03:36:14.623: ISDN Se3/0:23 Q931: 
   TX -> RELEASE_COMP pd = 8  callref = 0x805A
```

## Related Information

### This Document Applies to These Products

- Call Routing / Dial Plans

- Unified Customer Voice Portal

| VXML Gateway Configuration |
|---|
| !--- Define Hostname to IP Address !---- mapping for ASR and TTS servers ip host asr-en-us 172.18.110.76
ip host tts-en-us 172.18.110.76 !--- Define the Voice class URI to match !---- the SIP URI of ASR Server in the dial-peer voice class uri  TTS sip
 pattern tts@172.18.110.76 !--- Define the Voice class URI to match !---- the SIP URI of TTS server in the dial-peer voice class uri  ASR sip
 pattern asr@172.18.110.76 !--- Define the amount of maximum memory !---- to used for downloaded prompts ivr prompt memory 15000 !--- Define the SIP URI of ASR !---- and TTS Server ivr asr-server sip:asr@172.18.110.76
ivr tts-server sip:tts@172.18.110.76 !--- Configure an application service for !---- CVP VXML CVPSelfServiceBootstrap.vxml application
 service CVPSelfService flash:
CVPSelfServiceBootstrap.vxml
  paramspace english language en
  paramspace english index 0
  paramspace english location flash:
  paramspace english prefix en !--- Configure an application service for !---- CVP VXML CVPSelfService.tcl Script !--- CVPSelfService-app parameter specifies !---- the name of the VXML Application !--- CVPPrimary parameter specifies the !---- IP address of the VXML server service Pharmacy flash:CVPSelfService.tcl
  paramspace english index 0
  paramspace english language en
  paramspace english location flash:
  param CVPSelfService-port 7000
  param CVPSelfService-app 
GoodPrescriptionRefillApp7
  paramspace english prefix en
  param CVPPrimaryVXMLServer 172.18.110.75 !--- Specifies the Gateway’s RTP !---- stream to the ASR / TTS to go around the !---- Content Service Switch !---- instead of through the CSS. mrcp client rtpsetup enable !--- Specify the maximum memory size !---- for the HTTP Client Cache http client cache memory pool 15000 !--- Specify the maximum number of file !---- that can be stored in the !---- HTTP Client Cache http client cache memory file 500 !--- Disable Persistent !---- HTTP Connections no http client connection persistent !--- Configure the T1 PRI controller T1 3/0
 framing esf
 linecode b8zs
 pri-group timeslots 1-24 !--- Configure the ISDN switch !---- type and incoming-voice !---- under the D-channel interface interface Serial3/0:23
 no ip address
 encapsulation hdlc
 isdn switch-type primary-net5
 isdn incoming-voice modem
 no cdp enable ! --- Configure a POTS !---- dial-peer that will be used !---- as inbound dial-peer for calls coming ! --- in across the T1 PRI line. !---- The “pharmacy”service !---- is applied under this dial-peer. dial-peer voice 1 pots
 service pharmacy
 destination-pattern 5555
 direct-inward-dial
 port 3/0:D
 forward-digits all !--- Configure a SIP Voip !---- dial-peer that will be used !---- as an outbound dial-peer when the !---Gateway initiates a MRCP overc SIP !---- session to the ASR server. !---- Codec = G711ulaw, DTMF-Relay !---- = RTP-NTE, No Vad dial-peer voice 5 voip
 session protocol sipv2
 destination uri ASR
 dtmf-relay rtp-nte
 codec g711ulaw
 no vad !--- Configure a SIP Voip !---- dial-peer that will be used !---- as an outbound dial-peer when the !---Gateway initiates a MRCP !---- overc SIP session to the TTS server !--- Codec = G711ulaw, DTMF-Relay = RTP-NTE, !---- No Vad dial-peer voice 6 voip
 session protocol sipv2
 destination uri TTS
 dtmf-relay rtp-nte
 codec g711ulaw
 no vad |