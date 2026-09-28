---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cumi-api-b-cumi-api-b-cumi-api-chapter-01010-html-5e4b5feb5c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUMI_API/b_CUMI-API/b_CUMI-API_chapter_01010.html
retrieved_at: 2026-08-21T08:06:48.282698+00:00
---

Cisco Unity Connection Messaging Interface (CUMI) API

# Cisco Unity Connection Messaging Interface (CUMI) API

Updated: December 23, 2018

Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API -- HTTP Samples

## Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API -- HTTP Samples

- Cisco Unity Connection Messaging                              	 Interface (CUMI) API -- HTTP Samples

- Send Message                              	 (Audio Data on Client)

- Send Message                              	 (Audio Data Recorded Via CUTI on Server)

# Cisco Unity Connection Messaging
                     	 Interface (CUMI) API -- HTTP Samples

## Send Message
                        	 (Audio Data on Client)

Note that the audio data portion
                              		  of the message is truncated after the first few bytes:

```
Hypertext Transfer Protocol 
 POST /vmrest/messages?userobjectid=b81bc5e4-e4c5-4743-9d84-34a401a5ba28 HTTP/1.1\r\n 
 Content-Type: multipart/form-data;boundary=Boundary_1_18607473_1256039585421\r\n 
 Accept: application/json\r\n 
 User-Agent: Java/1.6.0_11\r\n 
 Host: cuc-install-67.cisco.com\r\n 
 Connection: keep-alive\r\n 
 Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==\r\n 
 Credentials: ccmadministrator:ecsbulab 
 Content-Length: 8001\r\n 
 [Content length: 8001] 
 \r\n
 No. Time Source Destination Protocol Info 
 48 1.510814 10.93.225.254 10.93.230.219 HTTP Continuation or non-HTTP traffic
 Frame 48 (1514 bytes on wire, 1514 bytes captured)
 Ethernet II, Src: Ibm_71:6a:c6 (00:1a:64:71:6a:c6), Dst: Cisco_1e:d9:00 (00:23:04:1e:d9:00)
 Internet Protocol, Src: 10.93.225.254 (10.93.225.254), Dst: 10.93.230.219 (10.93.230.219)
 Transmission Control Protocol, Src Port: lumimgrd (4741), Dst Port: http (80), Seq: 905, Ack: 2488, Len: 1460
 Hypertext Transfer Protocol 
 \r\n
  Data (1458 bytes)
 0000 2d 2d 42 6f 75 6e 64 61 72 79 5f 31 5f 31 38 36 --Boundary_1_186
 0010 30 37 34 37 33 5f 31 32 35 36 30 33 39 35 38 35 07473_1256039585
 0020 34 32 31 0d 0a 43 6f 6e 74 65 6e 74 2d 54 79 70 421..Content-Typ
 0030 65 3a 20 61 70 70 6c 69 63 61 74 69 6f 6e 2f 6a e: application/j
 0040 73 6f 6e 0d 0a 0d 0a 7b 22 53 75 62 6a 65 63 74 son....{"Subject
 0050 22 3a 22 6d 75 6c 74 69 70 6c 65 20 72 65 63 69 ":"multiple reci
 0060 70 69 65 6e 74 73 20 73 65 6e 64 20 6d 65 73 73 pients send mess
 0070 61 67 65 20 74 65 73 74 22 2c 22 41 72 72 69 76 age test","Arriv
 0080 61 6c 54 69 6d 65 22 3a 22 30 22 2c 22 46 72 6f alTime":"0","Fro
 0090 6d 53 75 62 22 3a 22 66 61 6c 73 65 22 2c 22 46 mSub":"false","F
 00a0 72 6f 6d 56 6d 49 6e 74 53 75 62 22 3a 22 66 61 romVmIntSub":"fa
 00b0 6c 73 65 22 7d 0d 0a 2d 2d 42 6f 75 6e 64 61 72 lse"}..--Boundar
 00c0 79 5f 31 5f 31 38 36 30 37 34 37 33 5f 31 32 35 y_1_18607473_125
 00d0 36 30 33 39 35 38 35 34 32 31 0d 0a 43 6f 6e 74 6039585421..Cont
 00e0 65 6e 74 2d 54 79 70 65 3a 20 61 70 70 6c 69 63 ent-Type: applic
 00f0 61 74 69 6f 6e 2f 6a 73 6f 6e 0d 0a 0d 0a 7b 22 ation/json....{"
 0100 52 65 63 69 70 69 65 6e 74 22 3a 5b 7b 22 54 79 Recipient":[{"Ty
 0110 70 65 22 3a 22 54 4f 22 2c 22 41 64 64 72 65 73 pe":"TO","Addres
 0120 73 22 3a 7b 22 55 73 65 72 47 75 69 64 22 3a 22 s":{"UserGuid":"
 0130 62 38 31 62 63 35 65 34 2d 65 34 63 35 2d 34 37 b81bc5e4-e4c5-47
 0140 34 33 2d 39 64 38 34 2d 33 34 61 34 30 31 61 35 43-9d84-34a401a5
 0150 62 61 32 38 22 7d 7d 2c 7b 22 54 79 70 65 22 3a ba28"}},{"Type":
 0160 22 42 43 43 22 2c 22 41 64 64 72 65 73 73 22 3a "BCC","Address":
 0170 7b 22 53 6d 74 70 41 64 64 72 65 73 73 22 3a 22 {"SmtpAddress":"
 0180 6f 70 65 72 61 74 6f 72 40 63 75 63 2d 69 6e 73 operator@cuc-ins
 0190 74 61 6c 6c 2d 36 37 2e 63 69 73 63 6f 2e 63 6f tall-67.cisco.co
 01a0 6d 22 7d 7d 2c 7b 22 54 79 70 65 22 3a 22 43 43 m"}},{"Type":"CC
 01b0 22 2c 22 41 64 64 72 65 73 73 22 3a 7b 22 4f 62 ","Address":{"Ob
 01c0 6a 65 63 74 49 64 22 3a 22 31 61 62 61 38 64 39 jectId":"1aba8d9
 01d0 39 2d 39 31 37 62 2d 34 31 35 38 2d 38 33 31 39 9-917b-4158-8319
 01e0 2d 66 30 35 33 63 30 64 31 39 35 66 65 22 2c 22 -f053c0d195fe","
 01f0 54 79 70 65 22 3a 22 44 49 53 54 52 49 42 55 54 Type":"DISTRIBUT
 0200 49 4f 4e 4c 49 53 54 22 7d 7d 5d 7d 0d 0a 2d 2d IONLIST"}}]}..--
 0210 42 6f 75 6e 64 61 72 79 5f 31 5f 31 38 36 30 37 Boundary_1_18607
 0220 34 37 33 5f 31 32 35 36 30 33 39 35 38 35 34 32 473_125603958542
 0230 31 0d 0a 43 6f 6e 74 65 6e 74 2d 54 79 70 65 3a 1..Content-Type:
 0240 20 61 75 64 69 6f 2f 77 61 76 0d 0a 0d 0a 52 49 audio/wav....RI
 0250 46 46 c0 1c 00 00 57 41 56 45 66 6d 74 20 10 00 FF....WAVEfmt ..
 0260 00 00 07 00 01 00 40 1f 00 00 40 1f 00 00 01 00 ......@...@.....
 0270 08 00 66 61 63 74 04 00 00 00 8f 1c 00 00 64 61 ..fact........da
 0280 74 61 90 1c 00 00 ff ff ff ff ff ff ff ff ff ff ta..............
 0290 ff ff 7e 7e 7e 7e ff fe fd fd fd fe fe 7e 7e 7e ..22:49
```

## Send Message
                        	 (Audio Data Recorded Via CUTI on Server)

```
No. Time Source Destination Protocol Info
 61 9.984028 10.93.225.254 10.93.230.219 HTTP POST /vmrest/messages?userobjectid=b81bc5e4-e4c5-4743-9d84-34a401a5ba28 HTTP/1.1
 Frame 61 (405 bytes on wire, 405 bytes captured)
 Ethernet II, Src: Ibm_71:6a:c6 (00:1a:64:71:6a:c6), Dst: Cisco_1e:d9:00 (00:23:04:1e:d9:00)
 Internet Protocol, Src: 10.93.225.254 (10.93.225.254), Dst: 10.93.230.219 (10.93.230.219) 
 Transmission Control Protocol, Src Port: taurus-wh (1610), Dst Port: http (80), Seq: 2279, Ack: 4485, Len: 351
 Hypertext Transfer Protocol
 POST /vmrest/messages?userobjectid=b81bc5e4-e4c5-4743-9d84-34a401a5ba28 HTTP/1.1\r\n
 Content-Type: multipart/form-data;boundary=Boundary_1_28113457_1256068997078\r\n
 Accept: application/json\r\n
 User-Agent: Java/1.6.0_11\r\n
 Host: cuc-install-67.cisco.com\r\n
 Connection: keep-alive\r\n
 Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==\r\n
 Credentials: ccmadministrator:ecsbulab
 Content-Length: 754\r\n
 [Content length: 754]
 \r\n
 0000 00 23 04 1e d9 00 00 1a 64 71 6a c6 08 00 45 00 .#......dqj...E.
 0010 01 87 5a a3 40 00 80 06 c1 39 0a 5d e1 fe 0a 5d ..Z.@....9.]...]
 0020 e6 db 06 4a 00 50 23 1f 44 2a 2b c4 79 ff 50 18 ...J.P#.D*+.y.P.
 0030 fb 26 df 0d 00 00 50 4f 53 54 20 2f 76 6d 72 65 .&....POST /vmrm
 0040 73 74 2f 6d 65 73 73 61 67 65 73 3f 75 73 65 72 st/messages?user
 0050 6f 62 6a 65 63 74 69 64 3d 62 38 31 62 63 35 65 objectid=b81bc5e
 0060 34 2d 65 34 63 35 2d 34 37 34 33 2d 39 64 38 34 4-e4c5-4743-9d84
 0070 2d 33 34 61 34 30 31 61 35 62 61 32 38 20 48 54 -34a401a5ba28 HT
 0080 54 50 2f 31 2e 31 0d 0a 43 6f 6e 74 65 6e 74 2d TP/1.1..Content-
 0090 54 79 70 65 3a 20 6d 75 6c 74 69 70 61 72 74 2f Type: multipart/
 00a0 66 6f 72 6d 2d 64 61 74 61 3b 62 6f 75 6e 64 61 form-data;bounda
 00b0 72 79 3d 42 6f 75 6e 64 61 72 79 5f 31 5f 32 38 ry=Boundary_1_28
 00c0 31 31 33 34 35 37 5f 31 32 35 36 30 36 38 39 39 113457_125606899
 00d0 37 30 37 38 0d 0a 41 63 63 65 70 74 3a 20 61 70 7078..Accept: ap
 00e0 70 6c 69 63 61 74 69 6f 6e 2f 6a 73 6f 6e 0d 0a plication/json..
 00f0 55 73 65 72 2d 41 67 65 6e 74 3a 20 4a 61 76 61 User-Agent: Java
 0100 2f 31 2e 36 2e 30 5f 31 31 0d 0a 48 6f 73 74 3a /1.6.0_11..Host:
 0110 20 63 75 63 2d 69 6e 73 74 61 6c 6c 2d 36 37 2e cuc-install-67.
 0120 63 69 73 63 6f 2e 63 6f 6d 0d 0a 43 6f 6e 6e 65 cisco.com..Conne
 0130 63 74 69 6f 6e 3a 20 6b 65 65 70 2d 61 6c 69 76 ction: keep-aliv
 0140 65 0d 0a 41 75 74 68 6f 72 69 7a 61 74 69 6f 6e e..Authorization
 0150 3a 20 42 61 73 69 63 20 59 32 4e 74 59 57 52 74 : Basic Y2NtYWRt
 0160 61 57 35 70 63 33 52 79 59 58 52 76 63 6a 70 6c aW5pc3RyYXRvcjpl
 0170 59 33 4e 69 64 57 78 68 59 67 3d 3d 0d 0a 43 6f Y3NidWxhYg==..Co
 0180 6e 74 65 6e 74 2d 4c 65 6e 67 74 68 3a 20 37 35 ntent-Length: 75
 0190 34 0d 0a 0d 0a 4....
 No. Time Source Destination Protocol Info
 62 9.984053 10.93.225.254 10.93.230.219 HTTP Continuation or non-HTTP traffic
 Frame 62 (808 bytes on wire, 808 bytes captured)
 Ethernet II, Src: Ibm_71:6a:c6 (00:1a:64:71:6a:c6), Dst: Cisco_1e:d9:00 (00:23:04:1e:d9:00)
 Internet Protocol, Src: 10.93.225.254 (10.93.225.254), Dst: 10.93.230.219 (10.93.230.219)
 Transmission Control Protocol, Src Port: taurus-wh (1610), Dst Port: http (80), Seq: 2630, Ack: 4485, Len: 754
 Hypertext Transfer Protocol
 \r\n
 Data (752 bytes)
 Data: 2D2D426F756E646172795F315F32383131333435375F3132...
 0000 00 23 04 1e d9 00 00 1a 64 71 6a c6 08 00 45 00 .#......dqj...E.
 0010 03 1a 5a a4 40 00 80 06 bf a5 0a 5d e1 fe 0a 5d ..Z.@......]...]
 0020 e6 db 06 4a 00 50 23 1f 45 89 2b c4 79 ff 50 18 ...J.P#.E.+.y.P.
 0030 fb 26 e0 a0 00 00 0d 0a 2d 2d 42 6f 75 6e 64 61 .&......--Bounda
 0040 72 79 5f 31 5f 32 38 31 31 33 34 35 37 5f 31 32 ry_1_28113457_12
 0050 35 36 30 36 38 39 39 37 30 37 38 0d 0a 43 6f 6e 56068997078..Con
 0060 74 65 6e 74 2d 54 79 70 65 3a 20 61 70 70 6c 69 tent-Type: appli
 0070 63 61 74 69 6f 6e 2f 6a 73 6f 6e 0d 0a 0d 0a 7b cation/json....{
 0080 22 53 75 62 6a 65 63 74 22 3a 22 73 65 6e 64 20 "Subject":"send
 0090 6d 65 73 73 61 67 65 20 74 65 73 74 22 2c 22 41 message test","A
 00a0 72 72 69 76 61 6c 54 69 6d 65 22 3a 22 30 22 2c rrivalTime":"0",
 00b0 22 46 72 6f 6d 53 75 62 22 3a 22 66 61 6c 73 65 "FromSub":"false
 00c0 22 2c 22 46 72 6f 6d 56 6d 49 6e 74 53 75 62 22 ","FromVmIntSub"
 00d0 3a 22 66 61 6c 73 65 22 7d 0d 0a 2d 2d 42 6f 75 :"false"}..--Bou
 00e0 6e 64 61 72 79 5f 31 5f 32 38 31 31 33 34 35 37 ndary_1_28113457
 00f0 5f 31 32 35 36 30 36 38 39 39 37 30 37 38 0d 0a _1256068997078..
 0100 43 6f 6e 74 65 6e 74 2d 54 79 70 65 3a 20 61 70 Content-Type: ap
 0110 70 6c 69 63 61 74 69 6f 6e 2f 6a 73 6f 6e 0d 0a plication/json..
 0120 0d 0a 7b 22 52 65 63 69 70 69 65 6e 74 22 3a 7b ..{"Recipient":{
 0130 22 54 79 70 65 22 3a 22 54 4f 22 2c 22 41 64 64 "Type":"TO","Add
 0140 72 65 73 73 22 3a 7b 22 55 73 65 72 47 75 69 64 ress":{"UserGuid
 0150 22 3a 22 62 38 31 62 63 35 65 34 2d 65 34 63 35 ":"b81bc5e4-e4c5
 0160 2d 34 37 34 33 2d 39 64 38 34 2d 33 34 61 34 30 -4743-9d84-34a40
 0170 31 61 35 62 61 32 38 22 2c 22 44 69 73 70 6c 61 1a5ba28","Displa
 0180 79 4e 61 6d 65 22 3a 22 4f 70 65 72 61 74 6f 72 yName":"Operator
 0190 22 7d 7d 7d 0d 0a 2d 2d 42 6f 75 6e 64 61 72 79 "}}}..--Boundary
 01a0 5f 31 5f 32 38 31 31 33 34 35 37 5f 31 32 35 36 _1_28113457_1256
 01b0 30 36 38 39 39 37 30 37 38 0d 0a 43 6f 6e 74 65 068997078..Conte
 01c0 6e 74 2d 54 79 70 65 3a 20 61 70 70 6c 69 63 61 nt-Type: applica
 01d0 74 69 6f 6e 2f 78 6d 6c 0d 0a 0d 0a 3c 3f 78 6d tion/xml....<?xm
 01e0 6c 20 76 65 72 73 69 6f 6e 3d 22 31 2e 30 22 20 l version="1.0"
 01f0 65 6e 63 6f 64 69 6e 67 3d 22 55 54 46 2d 38 22 encoding="UTF-8"
 0200 20 73 74 61 6e 64 61 6c 6f 6e 65 3d 22 79 65 73 standalone="yes
 0210 22 3f 3e 3c 43 61 6c 6c 43 6f 6e 74 72 6f 6c 3e "?><CallControl>
 0220 3c 6f 70 3e 50 4c 41 59 3c 2f 6f 70 3e 3c 72 65 <op>PLAY</op><re
 0230 73 6f 75 72 63 65 54 79 70 65 3e 53 54 52 45 41 sourceType>STREA
 0240 4d 3c 2f 72 65 73 6f 75 72 63 65 54 79 70 65 3e M</resourceType>
 0250 3c 72 65 73 6f 75 72 63 65 49 64 3e 38 36 61 61 <resourceId>86aa
 0260 66 31 65 32 2d 63 34 64 62 2d 34 65 30 38 2d 61 f1e2-c4db-4e08-a
 0270 36 65 39 2d 38 32 65 31 37 30 36 61 37 39 66 34 6e9-82e1706a79f4
 0280 2e 77 61 76 3c 2f 72 65 73 6f 75 72 63 65 49 64 .wav</resourceId
 0290 3e 3c 6c 61 73 74 52 65 73 75 6c 74 3e 30 3c 2f ><lastResult>0</
 02a0 6c 61 73 74 52 65 73 75 6c 74 3e 3c 73 70 65 65 lastResult><spee
 02b0 64 3e 31 30 30 3c 2f 73 70 65 65 64 3e 3c 76 6f d>100</speed><vo
 02c0 6c 75 6d 65 3e 31 30 30 3c 2f 76 6f 6c 75 6d 65 lume>100</volume
 02d0 3e 3c 73 74 61 72 74 50 6f 73 69 74 69 6f 6e 3e ><startPosition>
 02e0 30 3c 2f 73 74 61 72 74 50 6f 73 69 74 69 6f 6e 0</startPosition
 02f0 3e 3c 2f 43 61 6c 6c 43 6f 6e 74 72 6f 6c 3e 0d ></CallControl>.
 0300 0a 2d 2d 42 6f 75 6e 64 61 72 79 5f 31 5f 32 38 .--Boundary_1_28
 0310 31 31 33 34 35 37 5f 31 32 35 36 30 36 38 39 39 113457_125606899
 0320 37 30 37 38 2d 2d 0d 0a 7078--..
```

| Hypertext Transfer Protocol 
 POST /vmrest/messages?userobjectid=b81bc5e4-e4c5-4743-9d84-34a401a5ba28 HTTP/1.1\r\n 
 Content-Type: multipart/form-data;boundary=Boundary_1_18607473_1256039585421\r\n 
 Accept: application/json\r\n 
 User-Agent: Java/1.6.0_11\r\n 
 Host: cuc-install-67.cisco.com\r\n 
 Connection: keep-alive\r\n 
 Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==\r\n 
 Credentials: ccmadministrator:ecsbulab 
 Content-Length: 8001\r\n 
 [Content length: 8001] 
 \r\n
 No. Time Source Destination Protocol Info 
 48 1.510814 10.93.225.254 10.93.230.219 HTTP Continuation or non-HTTP traffic
 Frame 48 (1514 bytes on wire, 1514 bytes captured)
 Ethernet II, Src: Ibm_71:6a:c6 (00:1a:64:71:6a:c6), Dst: Cisco_1e:d9:00 (00:23:04:1e:d9:00)
 Internet Protocol, Src: 10.93.225.254 (10.93.225.254), Dst: 10.93.230.219 (10.93.230.219)
 Transmission Control Protocol, Src Port: lumimgrd (4741), Dst Port: http (80), Seq: 905, Ack: 2488, Len: 1460
 Hypertext Transfer Protocol 
 \r\n
  Data (1458 bytes)
 0000 2d 2d 42 6f 75 6e 64 61 72 79 5f 31 5f 31 38 36 --Boundary_1_186
 0010 30 37 34 37 33 5f 31 32 35 36 30 33 39 35 38 35 07473_1256039585
 0020 34 32 31 0d 0a 43 6f 6e 74 65 6e 74 2d 54 79 70 421..Content-Typ
 0030 65 3a 20 61 70 70 6c 69 63 61 74 69 6f 6e 2f 6a e: application/j
 0040 73 6f 6e 0d 0a 0d 0a 7b 22 53 75 62 6a 65 63 74 son....{"Subject
 0050 22 3a 22 6d 75 6c 74 69 70 6c 65 20 72 65 63 69 ":"multiple reci
 0060 70 69 65 6e 74 73 20 73 65 6e 64 20 6d 65 73 73 pients send mess
 0070 61 67 65 20 74 65 73 74 22 2c 22 41 72 72 69 76 age test","Arriv
 0080 61 6c 54 69 6d 65 22 3a 22 30 22 2c 22 46 72 6f alTime":"0","Fro
 0090 6d 53 75 62 22 3a 22 66 61 6c 73 65 22 2c 22 46 mSub":"false","F
 00a0 72 6f 6d 56 6d 49 6e 74 53 75 62 22 3a 22 66 61 romVmIntSub":"fa
 00b0 6c 73 65 22 7d 0d 0a 2d 2d 42 6f 75 6e 64 61 72 lse"}..--Boundar
 00c0 79 5f 31 5f 31 38 36 30 37 34 37 33 5f 31 32 35 y_1_18607473_125
 00d0 36 30 33 39 35 38 35 34 32 31 0d 0a 43 6f 6e 74 6039585421..Cont
 00e0 65 6e 74 2d 54 79 70 65 3a 20 61 70 70 6c 69 63 ent-Type: applic
 00f0 61 74 69 6f 6e 2f 6a 73 6f 6e 0d 0a 0d 0a 7b 22 ation/json....{"
 0100 52 65 63 69 70 69 65 6e 74 22 3a 5b 7b 22 54 79 Recipient":[{"Ty
 0110 70 65 22 3a 22 54 4f 22 2c 22 41 64 64 72 65 73 pe":"TO","Addres
 0120 73 22 3a 7b 22 55 73 65 72 47 75 69 64 22 3a 22 s":{"UserGuid":"
 0130 62 38 31 62 63 35 65 34 2d 65 34 63 35 2d 34 37 b81bc5e4-e4c5-47
 0140 34 33 2d 39 64 38 34 2d 33 34 61 34 30 31 61 35 43-9d84-34a401a5
 0150 62 61 32 38 22 7d 7d 2c 7b 22 54 79 70 65 22 3a ba28"}},{"Type":
 0160 22 42 43 43 22 2c 22 41 64 64 72 65 73 73 22 3a "BCC","Address":
 0170 7b 22 53 6d 74 70 41 64 64 72 65 73 73 22 3a 22 {"SmtpAddress":"
 0180 6f 70 65 72 61 74 6f 72 40 63 75 63 2d 69 6e 73 operator@cuc-ins
 0190 74 61 6c 6c 2d 36 37 2e 63 69 73 63 6f 2e 63 6f tall-67.cisco.co
 01a0 6d 22 7d 7d 2c 7b 22 54 79 70 65 22 3a 22 43 43 m"}},{"Type":"CC
 01b0 22 2c 22 41 64 64 72 65 73 73 22 3a 7b 22 4f 62 ","Address":{"Ob
 01c0 6a 65 63 74 49 64 22 3a 22 31 61 62 61 38 64 39 jectId":"1aba8d9
 01d0 39 2d 39 31 37 62 2d 34 31 35 38 2d 38 33 31 39 9-917b-4158-8319
 01e0 2d 66 30 35 33 63 30 64 31 39 35 66 65 22 2c 22 -f053c0d195fe","
 01f0 54 79 70 65 22 3a 22 44 49 53 54 52 49 42 55 54 Type":"DISTRIBUT
 0200 49 4f 4e 4c 49 53 54 22 7d 7d 5d 7d 0d 0a 2d 2d IONLIST"}}]}..--
 0210 42 6f 75 6e 64 61 72 79 5f 31 5f 31 38 36 30 37 Boundary_1_18607
 0220 34 37 33 5f 31 32 35 36 30 33 39 35 38 35 34 32 473_125603958542
 0230 31 0d 0a 43 6f 6e 74 65 6e 74 2d 54 79 70 65 3a 1..Content-Type:
 0240 20 61 75 64 69 6f 2f 77 61 76 0d 0a 0d 0a 52 49 audio/wav....RI
 0250 46 46 c0 1c 00 00 57 41 56 45 66 6d 74 20 10 00 FF....WAVEfmt ..
 0260 00 00 07 00 01 00 40 1f 00 00 40 1f 00 00 01 00 ......@...@.....
 0270 08 00 66 61 63 74 04 00 00 00 8f 1c 00 00 64 61 ..fact........da
 0280 74 61 90 1c 00 00 ff ff ff ff ff ff ff ff ff ff ta..............
 0290 ff ff 7e 7e 7e 7e ff fe fd fd fd fe fe 7e 7e 7e ..22:49 |
|---|

| No. Time Source Destination Protocol Info
 61 9.984028 10.93.225.254 10.93.230.219 HTTP POST /vmrest/messages?userobjectid=b81bc5e4-e4c5-4743-9d84-34a401a5ba28 HTTP/1.1
 Frame 61 (405 bytes on wire, 405 bytes captured)
 Ethernet II, Src: Ibm_71:6a:c6 (00:1a:64:71:6a:c6), Dst: Cisco_1e:d9:00 (00:23:04:1e:d9:00)
 Internet Protocol, Src: 10.93.225.254 (10.93.225.254), Dst: 10.93.230.219 (10.93.230.219) 
 Transmission Control Protocol, Src Port: taurus-wh (1610), Dst Port: http (80), Seq: 2279, Ack: 4485, Len: 351
 Hypertext Transfer Protocol
 POST /vmrest/messages?userobjectid=b81bc5e4-e4c5-4743-9d84-34a401a5ba28 HTTP/1.1\r\n
 Content-Type: multipart/form-data;boundary=Boundary_1_28113457_1256068997078\r\n
 Accept: application/json\r\n
 User-Agent: Java/1.6.0_11\r\n
 Host: cuc-install-67.cisco.com\r\n
 Connection: keep-alive\r\n
 Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==\r\n
 Credentials: ccmadministrator:ecsbulab
 Content-Length: 754\r\n
 [Content length: 754]
 \r\n
 0000 00 23 04 1e d9 00 00 1a 64 71 6a c6 08 00 45 00 .#......dqj...E.
 0010 01 87 5a a3 40 00 80 06 c1 39 0a 5d e1 fe 0a 5d ..Z.@....9.]...]
 0020 e6 db 06 4a 00 50 23 1f 44 2a 2b c4 79 ff 50 18 ...J.P#.D*+.y.P.
 0030 fb 26 df 0d 00 00 50 4f 53 54 20 2f 76 6d 72 65 .&....POST /vmrm
 0040 73 74 2f 6d 65 73 73 61 67 65 73 3f 75 73 65 72 st/messages?user
 0050 6f 62 6a 65 63 74 69 64 3d 62 38 31 62 63 35 65 objectid=b81bc5e
 0060 34 2d 65 34 63 35 2d 34 37 34 33 2d 39 64 38 34 4-e4c5-4743-9d84
 0070 2d 33 34 61 34 30 31 61 35 62 61 32 38 20 48 54 -34a401a5ba28 HT
 0080 54 50 2f 31 2e 31 0d 0a 43 6f 6e 74 65 6e 74 2d TP/1.1..Content-
 0090 54 79 70 65 3a 20 6d 75 6c 74 69 70 61 72 74 2f Type: multipart/
 00a0 66 6f 72 6d 2d 64 61 74 61 3b 62 6f 75 6e 64 61 form-data;bounda
 00b0 72 79 3d 42 6f 75 6e 64 61 72 79 5f 31 5f 32 38 ry=Boundary_1_28
 00c0 31 31 33 34 35 37 5f 31 32 35 36 30 36 38 39 39 113457_125606899
 00d0 37 30 37 38 0d 0a 41 63 63 65 70 74 3a 20 61 70 7078..Accept: ap
 00e0 70 6c 69 63 61 74 69 6f 6e 2f 6a 73 6f 6e 0d 0a plication/json..
 00f0 55 73 65 72 2d 41 67 65 6e 74 3a 20 4a 61 76 61 User-Agent: Java
 0100 2f 31 2e 36 2e 30 5f 31 31 0d 0a 48 6f 73 74 3a /1.6.0_11..Host:
 0110 20 63 75 63 2d 69 6e 73 74 61 6c 6c 2d 36 37 2e cuc-install-67.
 0120 63 69 73 63 6f 2e 63 6f 6d 0d 0a 43 6f 6e 6e 65 cisco.com..Conne
 0130 63 74 69 6f 6e 3a 20 6b 65 65 70 2d 61 6c 69 76 ction: keep-aliv
 0140 65 0d 0a 41 75 74 68 6f 72 69 7a 61 74 69 6f 6e e..Authorization
 0150 3a 20 42 61 73 69 63 20 59 32 4e 74 59 57 52 74 : Basic Y2NtYWRt
 0160 61 57 35 70 63 33 52 79 59 58 52 76 63 6a 70 6c aW5pc3RyYXRvcjpl
 0170 59 33 4e 69 64 57 78 68 59 67 3d 3d 0d 0a 43 6f Y3NidWxhYg==..Co
 0180 6e 74 65 6e 74 2d 4c 65 6e 67 74 68 3a 20 37 35 ntent-Length: 75
 0190 34 0d 0a 0d 0a 4....
 No. Time Source Destination Protocol Info
 62 9.984053 10.93.225.254 10.93.230.219 HTTP Continuation or non-HTTP traffic
 Frame 62 (808 bytes on wire, 808 bytes captured)
 Ethernet II, Src: Ibm_71:6a:c6 (00:1a:64:71:6a:c6), Dst: Cisco_1e:d9:00 (00:23:04:1e:d9:00)
 Internet Protocol, Src: 10.93.225.254 (10.93.225.254), Dst: 10.93.230.219 (10.93.230.219)
 Transmission Control Protocol, Src Port: taurus-wh (1610), Dst Port: http (80), Seq: 2630, Ack: 4485, Len: 754
 Hypertext Transfer Protocol
 \r\n
 Data (752 bytes)
 Data: 2D2D426F756E646172795F315F32383131333435375F3132...
 0000 00 23 04 1e d9 00 00 1a 64 71 6a c6 08 00 45 00 .#......dqj...E.
 0010 03 1a 5a a4 40 00 80 06 bf a5 0a 5d e1 fe 0a 5d ..Z.@......]...]
 0020 e6 db 06 4a 00 50 23 1f 45 89 2b c4 79 ff 50 18 ...J.P#.E.+.y.P.
 0030 fb 26 e0 a0 00 00 0d 0a 2d 2d 42 6f 75 6e 64 61 .&......--Bounda
 0040 72 79 5f 31 5f 32 38 31 31 33 34 35 37 5f 31 32 ry_1_28113457_12
 0050 35 36 30 36 38 39 39 37 30 37 38 0d 0a 43 6f 6e 56068997078..Con
 0060 74 65 6e 74 2d 54 79 70 65 3a 20 61 70 70 6c 69 tent-Type: appli
 0070 63 61 74 69 6f 6e 2f 6a 73 6f 6e 0d 0a 0d 0a 7b cation/json....{
 0080 22 53 75 62 6a 65 63 74 22 3a 22 73 65 6e 64 20 "Subject":"send
 0090 6d 65 73 73 61 67 65 20 74 65 73 74 22 2c 22 41 message test","A
 00a0 72 72 69 76 61 6c 54 69 6d 65 22 3a 22 30 22 2c rrivalTime":"0",
 00b0 22 46 72 6f 6d 53 75 62 22 3a 22 66 61 6c 73 65 "FromSub":"false
 00c0 22 2c 22 46 72 6f 6d 56 6d 49 6e 74 53 75 62 22 ","FromVmIntSub"
 00d0 3a 22 66 61 6c 73 65 22 7d 0d 0a 2d 2d 42 6f 75 :"false"}..--Bou
 00e0 6e 64 61 72 79 5f 31 5f 32 38 31 31 33 34 35 37 ndary_1_28113457
 00f0 5f 31 32 35 36 30 36 38 39 39 37 30 37 38 0d 0a _1256068997078..
 0100 43 6f 6e 74 65 6e 74 2d 54 79 70 65 3a 20 61 70 Content-Type: ap
 0110 70 6c 69 63 61 74 69 6f 6e 2f 6a 73 6f 6e 0d 0a plication/json..
 0120 0d 0a 7b 22 52 65 63 69 70 69 65 6e 74 22 3a 7b ..{"Recipient":{
 0130 22 54 79 70 65 22 3a 22 54 4f 22 2c 22 41 64 64 "Type":"TO","Add
 0140 72 65 73 73 22 3a 7b 22 55 73 65 72 47 75 69 64 ress":{"UserGuid
 0150 22 3a 22 62 38 31 62 63 35 65 34 2d 65 34 63 35 ":"b81bc5e4-e4c5
 0160 2d 34 37 34 33 2d 39 64 38 34 2d 33 34 61 34 30 -4743-9d84-34a40
 0170 31 61 35 62 61 32 38 22 2c 22 44 69 73 70 6c 61 1a5ba28","Displa
 0180 79 4e 61 6d 65 22 3a 22 4f 70 65 72 61 74 6f 72 yName":"Operator
 0190 22 7d 7d 7d 0d 0a 2d 2d 42 6f 75 6e 64 61 72 79 "}}}..--Boundary
 01a0 5f 31 5f 32 38 31 31 33 34 35 37 5f 31 32 35 36 _1_28113457_1256
 01b0 30 36 38 39 39 37 30 37 38 0d 0a 43 6f 6e 74 65 068997078..Conte
 01c0 6e 74 2d 54 79 70 65 3a 20 61 70 70 6c 69 63 61 nt-Type: applica
 01d0 74 69 6f 6e 2f 78 6d 6c 0d 0a 0d 0a 3c 3f 78 6d tion/xml....<?xm
 01e0 6c 20 76 65 72 73 69 6f 6e 3d 22 31 2e 30 22 20 l version="1.0"
 01f0 65 6e 63 6f 64 69 6e 67 3d 22 55 54 46 2d 38 22 encoding="UTF-8"
 0200 20 73 74 61 6e 64 61 6c 6f 6e 65 3d 22 79 65 73 standalone="yes
 0210 22 3f 3e 3c 43 61 6c 6c 43 6f 6e 74 72 6f 6c 3e "?><CallControl>
 0220 3c 6f 70 3e 50 4c 41 59 3c 2f 6f 70 3e 3c 72 65 <op>PLAY</op><re
 0230 73 6f 75 72 63 65 54 79 70 65 3e 53 54 52 45 41 sourceType>STREA
 0240 4d 3c 2f 72 65 73 6f 75 72 63 65 54 79 70 65 3e M</resourceType>
 0250 3c 72 65 73 6f 75 72 63 65 49 64 3e 38 36 61 61 <resourceId>86aa
 0260 66 31 65 32 2d 63 34 64 62 2d 34 65 30 38 2d 61 f1e2-c4db-4e08-a
 0270 36 65 39 2d 38 32 65 31 37 30 36 61 37 39 66 34 6e9-82e1706a79f4
 0280 2e 77 61 76 3c 2f 72 65 73 6f 75 72 63 65 49 64 .wav</resourceId
 0290 3e 3c 6c 61 73 74 52 65 73 75 6c 74 3e 30 3c 2f ><lastResult>0</
 02a0 6c 61 73 74 52 65 73 75 6c 74 3e 3c 73 70 65 65 lastResult><spee
 02b0 64 3e 31 30 30 3c 2f 73 70 65 65 64 3e 3c 76 6f d>100</speed><vo
 02c0 6c 75 6d 65 3e 31 30 30 3c 2f 76 6f 6c 75 6d 65 lume>100</volume
 02d0 3e 3c 73 74 61 72 74 50 6f 73 69 74 69 6f 6e 3e ><startPosition>
 02e0 30 3c 2f 73 74 61 72 74 50 6f 73 69 74 69 6f 6e 0</startPosition
 02f0 3e 3c 2f 43 61 6c 6c 43 6f 6e 74 72 6f 6c 3e 0d ></CallControl>.
 0300 0a 2d 2d 42 6f 75 6e 64 61 72 79 5f 31 5f 32 38 .--Boundary_1_28
 0310 31 31 33 34 35 37 5f 31 32 35 36 30 36 38 39 39 113457_125606899
 0320 37 30 37 38 2d 2d 0d 0a 7078--.. |
|---|