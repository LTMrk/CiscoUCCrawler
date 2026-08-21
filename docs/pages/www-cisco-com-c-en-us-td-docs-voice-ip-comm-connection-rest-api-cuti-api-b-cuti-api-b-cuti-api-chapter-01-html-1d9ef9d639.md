---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cuti-api-b-cuti-api-b-cuti-api-chapter-01-html-1d9ef9d639
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUTI_API/b_CUTI_API/b_CUTI_API_chapter_01.html
retrieved_at: 2026-08-21T01:01:05.398730+00:00
---

Cisco Unity Connection Telephony Interface (CUTI) API

# Cisco Unity Connection Telephony Interface (CUTI) API

Updated: December 27, 2018

Chapter: Cisco Unity
	 Connection Telephony Interface (CUTI) API -- Using CUTI for Basic Call
	 Operations

## Chapter: Cisco Unity
	 Connection Telephony Interface (CUTI) API -- Using CUTI for Basic Call
	 Operations

# Cisco Unity
                     	 Connection Telephony Interface (CUTI) API -- Using CUTI for Basic Call
                     	 Operations

Links to Other API pages: Cisco_Unity_Connection_APIs

## About Basic Call
                        	 Operations

The basic call operations are making a call, checking call-connected
                           		status, and hanging up. The call object is used to convey information about a
                           		call (see API XSD's). Cisco Unity Connection 10.5(2) and later facilitates you
                           		to make a video call. A user will be able to establish a video call, if all the
                           		required pre-checks are satisfied, which are as follows:

- Mapping video service
                                 		  accounts: subscriber needs a video service configured with the video service
                                 		  account.

- Enabling Class of Service
                                 		  (COS) Settings for the subscriber

When making a call, the following fields are used:

- number : the only field that does not have a default value. Users
                                 		  with the system administrator role can call any number, but end users can call
                                 		  only those numbers that do not violate their associated restriction table,
                                 		  based on their class of service.

- maximumRings : defaults to 4.

- mediaSwitchObjectId : for end users, defaults to the phone system
                                 		  that is associated with the user. For users who do not have an associated phone
                                 		  system (for example, administrators), the phone system that is marked as the
                                 		  default TRAP phone system is used.

- calltype : indicates whether the call type is audio or video. If
                                 		  you do not specify the call type, then by default the call will be placed as an
                                 		  audio call only.

When a call has been placed, a client can get server information about
                           		the call, most importantly the connected status.

The following are HTTP commands for basic call operations:

```
POST http://<server>/calls:
Create a call (make a phone call) by using the information in a call object.
Returns a URI for the new call.
 
GET http://<server>/calls/<call id>: Get basic call information. Returns a call object.
 
DELETE http://<server>/calls/<call id>: Hangs up a call.
```

## Playing and
                        	 Recording by Using a Call

Files on the server can be played and recorded by phone (using the
                              		  call control operations) by using the CallControl object (see API XSD's).

Note: Video record and play do not support the pause and resume
                              		  operations.

Recording or Playing message can be paused and resumed (using the call
                              		  control operations).The fields of the CallControl object are described below:

- opType : PLAY, RECORD, PAUSE, RESUME or STOP

- resourceType : MESSAGE, BROADCASTMESSAGE, STREAM, HANDLER, or
                                    			 URI. STREAM is generally a temporary resource created by a record operation.

- resourceID : Can be a message identifier, a broadcast message
                                    			 identifier or a stream identifier depending on the resource type.

- Speed , volume and startPosition are all optional parameters. Speed and volume
                                    			 are a percentage and default to 100. The start position indicates a time in
                                    			 milliseconds and defaults to 0.

- lastResult : The result of the last call control operation.

- folderType : Reserved. Only messages in the inbox can be
                                    			 played.

- sessionId : This is a reference of the video recording on the
                                    			 MediaSense Server using Record API. MediaSense uniquely identifies the
                                    			 recording using the sessionId.

A call control object is passed to a call by using a POST to the
                              		  resource URI of the call:

```
POST http://<server>/vmrest/calls/<call id>
```

## Examples

The examples below
                              		  show how to: make a call, check call status, record by phone, play the
                              		  recording, pause and resume the recording, hang up, and send the recording as a
                              		  message. Each step is shown as the HTTP request and response.

Make the call

```
POST /vmrest/calls HTTP/1.1
Content-Type: application/json

Accept: application/json

User-Agent: Java/1.6.0_17

Host: cuc-install-67.cisco.com

Connection: keep-alive

Authorization: Basic
Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 36
 
{"number":"2119","maximumRings":"4"}
```

Response:

```
HTTP/1.1 201 Created
Set-Cookie:
JSESSIONIDSSO=CB2BE1D9771621DBEA24B479C1A9C10A; Path=/
Set-Cookie:
JSESSIONID=EB7C33B4DC0AAE91CB002D799C8734BA; Path=/vmrest
Location:
[http://cuc-install-67.cisco.com/vmrest/calls/vmrest/calls/1]
Content-Type: application/json
Transfer-Encoding: chunked

Date: Fri, 15 Jan 2010 15:14:11 GMT
Server:
```

Make the Video call

```
POST https://<connection-server>/vmrest/calls
```

```
<Call>
   <number>1096</number>
   <maximumRings>5</maximumRings>
   <callType>Video</callType>
</Call>
```

The following is
                              		  the response from the above *POST* request and the actual response will depend
                              		  upon the information given by you:

```
Response Code: 201
/vmrest/calls/66
CallType:video
```

JSON Example

```
POST /vmrest/calls HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic
Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 36
{"number":"1097","maximumRings":"4","callType":"video"}
```

Response:

```
HTTP/1.1 201 Created
Set-Cookie:
JSESSIONIDSSO=CB2BE1D9771621DBEA24B479C1A9C10A; Path=/
Set-Cookie:
JSESSIONID=EB7C33B4DC0AAE91CB002D799C8734BA; Path=/vmrest
Location:
[http://cuc-install-67.cisco.com/vmrest/calls/vmrest/calls/40/calltype:video]
Content-Type: application/json
```

Video Call Downgrade
                                 			 Scenarios

If a Video call
                              		  gets downgraded to audio, user receives the following response:

Scenario 1

If a user does not
                              		  have Video Service Account and try to make a video call, the following response
                              		  is received:

```
Response Code: 201
/vmrest/calls/66
CallType: Audio
CallDowngradeReason: Video Service Account does not exist
```

Scenario 2

If a user does not
                              		  have Video Service activated on Unity Connection and try to make a video call,
                              		  the following response is received:

```
Response Code: 201
/vmrest/calls/66
CallType: Audio
CallDowngradeReason: Video Service not found
```

Scenario 3

If a user does not
                              		  have Video enabled in Class of Service and try to make a video call, the
                              		  following response is received:

```
Response Code: 201
/vmrest/calls/66
CallType: Audio
CallDowngradeReason: Not allowed to Playback and Record Video Greetings
```

Check call status

```
GET /vmrest/calls/1 HTTP/1.1
Accept: application/json

User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com

Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
```

Response:

```
HTTP/1.1 200 OK
Pragma: No-cache
Cache-Control: no-cache
Expires: Wed, 31 Dec 1969 16:00:00 PST
Set-Cookie: JSESSIONIDSSO=849167D3D61D2F30BA278BBF949FDF0F; Path=/
Set-Cookie: JSESSIONID=28A69142E490EC63A56690F9811BDDF9; Path=/vmrest
Content-Type: application/json 
{"id":"1","connected":"true","nativeConnectionId":"2"}
```

Check Video call
                                 			 status

```
GET https://<connection-server>/vmrest/calls/<call-id>
```

The following is
                              		  the response from the above *GET* request and the actual response will depend
                              		  upon the information given by you:

```
Response Code: 200
```

```
<Call>
   <number>1007</number>
   <id>1105</id>
   <connected>true</connected>
   <callType>video</callType>
   <nativeConnectionId>16</nativeConnectionId>
</Call>
```

JSON
                                 			 Example

```
GET /vmrest/calls/1 HTTP/1.1
Accept: application/json

User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com

Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
```

Response:

```
HTTP/1.1 200 OK
Pragma: No-cache
Cache-Control: no-cache
Expires: Wed, 31 Dec 1969 16:00:00 PST
Set-Cookie: JSESSIONIDSSO=849167D3D61D2F30BA278BBF949FDF0F; Path=/
Set-Cookie: JSESSIONID=28A69142E490EC63A56690F9811BDDF9; Path=/vmrest
Content-Type: application/json
{"number":"1097","id":"40","connected":"true","callType":"video","nativeConnectionId":"45"}
```

Record by
                                 			 phone

```
POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 15
{"op":"RECORD"}
```

Response:

```
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=8279B639488165EFFAC8D330FD2A1281; Path=/
Set-Cookie: JSESSIONID=AA008CFCC9B329EA961CD1E660384785; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:13 GMT
Server:
{"op":"RECORD","resourceType":"STREAM","resourceId":"cf1cb014-6394- 4279-ab5a-74a6d680e440.wav",
"lastResult":"0","speed":"100","volume":"100","startPosition":"0"}
```

Video Recording by
                                 			 phone

```
POST https://<connection-server>/vmrest/calls/<call-id>
```

```
<CallControl>
<op>RECORD</op>
</CallControl>
```

The following is
                              		  the response from the above *POST* request and the actual response will depend
                              		  upon the information given by you:

```
Response Code: 200
```

```
<CallControl>
  <op>RECORD</op>
  <resourceType>STREAM</resourceType>
  <resourceId>9d59b180-6147-4796-9488-014ef73203a0.wav</resourceId>
  <sessionId>3514637e02b471</sessionId>
  <lastResult>0</lastResult>
</CallControl>
```

JSON
                                 			 Example

```
POST /vmrest/calls/<call-id> HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 15
{"op":"RECORD"}
```

Response:

```
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=8279B639488165EFFAC8D330FD2A1281; Path=/
Set-Cookie: JSESSIONID=AA008CFCC9B329EA961CD1E660384785; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:13 GMT
Server:
1({"op":"RECORD","resourceType":"STREAM","resourceId":"a899bac7-9ee2-4c75-b3a7-e6a2a5d6d2dc.wav","sessionId":"1e14628d9a9ac1","lastResult":"0"})
```

Pause the recording

```
POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: ucbu-aricent-vm5.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
{"op":"PAUSE"}
```

Response:

```
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=6A4C99C02E79D696A2DEC46C24A0B2DA; Path=/; Secure
Set-Cookie: JSESSIONID=1E642B010F5AD5630DE922B1378679DF; Path=/vmrest; Secure
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 01 Jun 2012 06:33:49 GMT
Server: 

{"op":"PAUSE","lastResult":"0","speed":"100","volume":"100","startPosition":"0"}
```

Resume the recording

```
POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: ucbu-aricent-vm5.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
{"op":"RESUME"}
```

Response:

```
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=687E20DEFCC984797342E37A656A1F32; Path=/; Secure
Set-Cookie: JSESSIONID=48D31DBFCBAEF586F2A9398AB11204CC; Path=/vmrest; Secure
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 01 Jun 2012 06:34:25 GMT
Server: 

{"op":"RESUME","lastResult":"0","speed":"100","volume":"100","startPosition":"0"}
```

Play the recording

```
POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 159

{"op":"PLAY","resourceType":"STREAM","resourceId":"cf1cb014-6394-4279-ab5a-74a6d680e440.wav",
"lastResult":"0","speed":"100","volume":"100","startPosition":"0"}
```

Response:

```
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=CD7B1064CEB9385B6FE9279ECBDB40E3; Path=/
Set-Cookie: JSESSIONID=201BD26E840AA2CEEC242A9CCD0FE8F6; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:

{"op":"PLAY","resourceType":"STREAM","resourceId":"cf1cb014-6394-4279-ab5a-74a6d680e440.wav",
"lastResult":"0","speed":"100","volume":"100","startPosition":"0"}
```

Play Video recording

In a video call,

- For STREAM or URI
                                    			 resource type, if the Session ID is available, then the video recording will be
                                    			 played, else the audio recording will be played from the Audio resource-ID
                                    			 along with an image.

- For Message or Broadcast
                                    			 Message resource type, the audio recording will be played from the Audio
                                    			 resource-ID along with an image.

- If both sessionID and
                                    			 resource ID are not available, an error message is send to the user.

```
POST https://<connection-server>/vmrest/calls/<call-id>
```

```
Request:
<CallControl>
   <op>PLAY</op>
   <resourceType>STREAM</resourceType>
   <resourceId>1218f93a-2ce2-4987-9589-f8e06bd54a14.wav</resourceId>
   <sessionId>2f61469411d7131</sessionId>
   <lastResult>0</lastResult>
</CallControl>
```

The following is
                              		  the response from the above *POST* request and the actual response will depend
                              		  upon the information given by you:

```
Response: 200 Ok
<CallControl>
   <op>PLAY</op>
   <resourceType>STREAM</resourceType>
   <resourceId>1218f93a-2ce2-4987-9589-f8e06bd54a14.wav</resourceId>
   <sessionId>2f61469411d7131</sessionId>
   <lastResult>0</lastResult>
</CallControl>
```

JSON
                                 			 Example

```
Request:
POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 159

{"op":"PLAY","resourceType":"STREAM","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","sessionId":"2f61469411d7131","lastResult":"0"}
```

```
Response:
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=CD7B1064CEB9385B6FE9279ECBDB40E3; Path=/
Set-Cookie: JSESSIONID=201BD26E840AA2CEEC242A9CCD0FE8F6; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:

1({"op":"PLAY","resourceType":"STREAM","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","sessionId":"2f61469411d7131","lastResult":"0"})
```

Hang up

```
DELETE /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Accept: text/html, image/gif, image/jpeg, \*; q=.2, \*/*; q=.2
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
```

Response:

```
HTTP/1.1 204 No Content
Pragma: No-cache
Cache-Control: no-cache
Expires: Wed, 31 Dec 1969 16:00:00 PST
Set-Cookie: JSESSIONIDSSO=93B286C6584533F9EE793A01E5804465; Path=/
Set-Cookie: JSESSIONID=0CCFFFCAD1C11A45EAD1E8F04B22D28D; Path=/vmrest
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:
```

Send the recording as a
                                 			 message

```
POST /vmrest/messages?userobjectid=84c14db9-7439-4326-a2e2-e516aa192dff HTTP/1.1
Content-Type: multipart/form-data;boundary=Boundary_1_16617866_1263568442453
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 731

\--Boundary_1_16617866_1263568442453
Content-Type: application/json
{"Subject":"send message test","ArrivalTime":"0","FromSub":"false"}
\--Boundary_1_16617866_1263568442453
Content-Type: application/json

{"Recipient":{"Type":"TO","Address":
{"UserGuid":"84c14db9-7439-4326-a2e2-e516aa192dff","DisplayName":"Operator"}
}}
\--Boundary_1_16617866_1263568442453
Content-Type: application/xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><CallControl><op>PLAY</op><resourceType>STREAM</resourceType><resourceId>cf1cb014-6394-4279-
ab5a-74a6d680e440.wav</resourceId><lastResult>0</lastResult><speed>100</speed><volume>100</volume><startPosition>0</startPosition></CallControl>

\--Boundary_1_16617866_1263568442453-\-
```

Response:

```
HTTP/1.1 202 Accepted
Set-Cookie: JSESSIONIDSSO=3D875CAE50B6B4947DEDCF5EDA119922; Path=/
Set-Cookie: JSESSIONID=842B1A6E53DAE329F6DA7525951668B4; Path=/vmrest
Content-Type: application/json
Content-Length: 0
Date: Fri, 15 Jan 2010 15:14:16 GMT
Server:
```

Send the recording as a Video message

```
POST /vmrest/messages?userobjectid=84c14db9-7439-4326-a2e2-e516aa192dff HTTP/1.1
Content-Type: multipart/form-data;boundary=Boundary_1_16617866_1263568442453
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 731

\--Boundary_1_16617866_1263568442453
Content-Type: application/json
{"Subject":"send message test","ArrivalTime":"0","FromSub":"false"}
\--Boundary_1_16617866_1263568442453
Content-Type: application/json

{"Recipient":{"Type":"TO","Address":
{"UserGuid":"84c14db9-7439-4326-a2e2-e516aa192dff","DisplayName":"Operator"}
}}
\--Boundary_1_16617866_1263568442453
Content-Type: application/xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><CallControl><op>PLAY</op><resourceType>STREAM</resourceType><resourceId>cf1cb014-6394-4279-
ab5a-74a6d680e440.wav</resourceId><sessionId><lastResult>0</lastResult><speed>100</speed><volume>100</volume><startPosition>0</startPosition></CallControl>

\--Boundary_1_16617866_1263568442453-\-
```

## Play
                        	 Greetings

Play Audio Greetings

Audio Greeting of users, user templates, call handler can be played
                              		  using CUTI API. a)For a user with mailbox following should be the request:

```
Request:
POST https://<connection-server>/vmrest/calls/<call-id> 
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>   
</CallControl>
```

```
Response:
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>
   <speed>100</speed>
   <volume>100</volume>
   <startPosition>0</startPosition>
   <lastResult>0</lastResult>
</CallControl>
Response code:200   Ok
```

JSON Example

```
Request
POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 159

{"op":"PLAY","resourceType":"HANDLER","resourceId":"0bc5155b-0989-4523-a75a-948cc691b99e.wav","lastResult":"0","speed":"100","volume":"100","startPosition":"0"}
```

```
Response: HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=CD7B1064CEB9385B6FE9279ECBDB40E3; Path=/
Set-Cookie: JSESSIONID=201BD26E840AA2CEEC242A9CCD0FE8F6; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:
1({"op":"PLAY","resourceType":"HANDLER","resourceId":"0bc5155b-0989-4523-a75a-948cc691b99e.wav","lastResult":"0","speed":"100","volume":"100","startPosition":"0"}
```

For a System administrator following should be the request:

In this case greeting of handler whose objectId "handlerObjectId"is
                              		  passed in request will be played.

```
POST https://<connection-server>/vmrest/calls/<call-id>?handlerObjectId=<handlerObjectId> 
Request:
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>   
</CallControl>
```

```
Response:
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>
   <speed>100</speed>
   <volume>100</volume>
   <startPosition>0</startPosition>
   <lastResult>0</lastResult>
</CallControl>
Response code:200   Ok
```

JSON Example

```
Request:
POST /vmrest/calls/1 ? handlerObjectId=<handlerObjectId>
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 159

{"op":"PLAY","resourceType":"HANDLER","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav"}
```

```
Response: 
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=CD7B1064CEB9385B6FE9279ECBDB40E3; Path=/
Set-Cookie: JSESSIONID=201BD26E840AA2CEEC242A9CCD0FE8F6; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:
1({"op":"PLAY","resourceType":"HANDLER","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","lastResult":"0","speed":"100","volume":"100","startPosition":"0")
```

Play Video Greetings

Video greeting of users, user templates, handler can be played using
                              		  CUTI API. a)For a user with video account following should be the request:

```
Request:
POST https://<connection-server>/vmrest/calls/<call-id>
```

```
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <sessionId>55d146ced50d1</sessionId>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>   
   <lastResult>0</lastResult>
</CallControl>
```

```
Response:
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>
   <sessionId>55d146ced50d1</sessionId>
   <lastResult>0</lastResult>
</CallControl>
Response code:200   Ok
```

JSON Example

```
Request:
POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 159

{"op":"PLAY","resourceType":"HANDLER","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","sessionId":"2f61469411d7131"}
```

```
Response: 
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=CD7B1064CEB9385B6FE9279ECBDB40E3; Path=/
Set-Cookie: JSESSIONID=201BD26E840AA2CEEC242A9CCD0FE8F6; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:

1({"op":"PLAY","resourceType":"HANDLER","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","sessionId":"2f61469411d7131","lastResult":"0"})
```

For a System administrator following should be the request: In this
                              		  case video greeting of handler, whose objectId "handlerObjectId"is passed in
                              		  request will be played.

```
POST https://<connection-server>/vmrest/calls/<call-id>?handlerObjectId=<handlerObjectId> 
Request:
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <sessionId>55d146ced50d1</sessionId>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>   
   <lastResult>0</lastResult>
</CallControl>
Response:
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>
   <sessionId>55d146ced50d1</sessionId>
   <lastResult>0</lastResult>
</CallControl>
Response code:200   Ok
```

JSON Example

```
Request:
POST /vmrest/calls/1 ? handlerObjectId=<handlerObjectId>
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 159

{"op":"PLAY","resourceType":"HANDLER","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","sessionId":"2f61469411d7131"}
```

```
Response: 
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=CD7B1064CEB9385B6FE9279ECBDB40E3; Path=/
Set-Cookie: JSESSIONID=201BD26E840AA2CEEC242A9CCD0FE8F6; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:

1({"op":"PLAY","resourceType":"HANDLER","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","sessionId":"2f61469411d7131","lastResult":"0"})
```

Add new Resource Type: HANDLER in section" Playing and Recording by
                              		  Using a Call"

## Save Video
                        	 Greetings

Unity Connection allows you to
                              		  save video greetings using both GET and PUT requests.

Example of GET Request

```
GET http://<connection-server>/vmrest/handlers/callhandlers/<call handler object ID>/greetings/<greeting type>/greetingstreamfiles/<language code>/video
```

The following is the response of the above GET command and the output
                              		  may vary depending on your inputs.

```
Response: 200
<CallControl>
    <resourceId>aad91d6d-aeca-4a72-8069-b656efb3041f.wav</resourceId>
    <sessionId>570146ed1504cb1</sessionId>
</CallControl
```

JSON Example

```
Request 
GET  vmrest/handlers/callhandlers/30600b21-1a4c-47a3-a078-8078984e5376/greetings/Standard/greetingstreamfiles/1033/video
Accept: application/json
User-Agent: Java/1.6.0_17
Host: <connection-server>
Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg=
```

```
Response
HTTP/1.1 201
Content-Type: application/json
Date: Fri, 15 Jan 2010 15:14:11 GMT
Server:
{ “resourceId” :” aad91d6d-aeca-4a72-8069-b656efb3041f.wav”, “sessionId” : ”570146ed1504cb1”}
```

Example of PUT Request

```
PUT http://<connection-server>/vmrest/handlers/callhandlers/<call handler object ID>/greetings/<greeting type>/greetingstreamfiles/<language code>/video
```

```
<CallControl>
     <resourceId>aad91d6d-aeca-4a72-8069-b656efb3041f.wav</resourceId>
     <sessionId>570146ed1504cb1</sessionId>
</CallControl>
```

```
Response: 201 OK
```

JSON Example

```
Request 
PUT  vmrest/handlers/callhandlers/30600b21-1a4c-47a3-a078-8078984e5376/greetings/Standard/greetingstreamfiles/1033/video
Content-Type: application/json
Accept: application/json
Host: <connection-server>
Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==

{ “resourceId” :” aad91d6d-aeca-4a72-8069-b656efb3041f.wav”, “sessionId” : ”570146ed1504cb1”}
```

```
Response :
HTTP/1.1 201
Content-Type: application/json
Date: Fri, 15 Jan 2010 15:14:11 GMT
Server:
```

## Example of Data
                        	 Fields

| Note | Max time limit for a paused call to be resumed will be idle time
                                          			 out. |
|---|---|

| POST http://<server>/vmrest/calls/<call id> |
|---|

| POST /vmrest/calls HTTP/1.1
Content-Type: application/json

Accept: application/json

User-Agent: Java/1.6.0_17

Host: cuc-install-67.cisco.com

Connection: keep-alive

Authorization: Basic
Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 36
 
{"number":"2119","maximumRings":"4"} |
|---|

| HTTP/1.1 201 Created
Set-Cookie:
JSESSIONIDSSO=CB2BE1D9771621DBEA24B479C1A9C10A; Path=/
Set-Cookie:
JSESSIONID=EB7C33B4DC0AAE91CB002D799C8734BA; Path=/vmrest
Location:
[http://cuc-install-67.cisco.com/vmrest/calls/vmrest/calls/1]
Content-Type: application/json
Transfer-Encoding: chunked

Date: Fri, 15 Jan 2010 15:14:11 GMT
Server: |
|---|

| POST https://<connection-server>/vmrest/calls |
|---|

| <Call>
   <number>1096</number>
   <maximumRings>5</maximumRings>
   <callType>Video</callType>
</Call> |
|---|

| Response Code: 201
/vmrest/calls/66
CallType:video |
|---|

| POST /vmrest/calls HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic
Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 36
{"number":"1097","maximumRings":"4","callType":"video"} |
|---|

| Response Code: 201
/vmrest/calls/66
CallType: Audio
CallDowngradeReason: Video Service Account does not exist |
|---|

| Response Code: 201
/vmrest/calls/66
CallType: Audio
CallDowngradeReason: Video Service not found |
|---|

| Response Code: 201
/vmrest/calls/66
CallType: Audio
CallDowngradeReason: Not allowed to Playback and Record Video Greetings |
|---|

| GET /vmrest/calls/1 HTTP/1.1
Accept: application/json

User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com

Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg== |
|---|

| HTTP/1.1 200 OK
Pragma: No-cache
Cache-Control: no-cache
Expires: Wed, 31 Dec 1969 16:00:00 PST
Set-Cookie: JSESSIONIDSSO=849167D3D61D2F30BA278BBF949FDF0F; Path=/
Set-Cookie: JSESSIONID=28A69142E490EC63A56690F9811BDDF9; Path=/vmrest
Content-Type: application/json 
{"id":"1","connected":"true","nativeConnectionId":"2"} |
|---|

| GET https://<connection-server>/vmrest/calls/<call-id> |
|---|

| Response Code: 200 |
|---|

| <Call>
   <number>1007</number>
   <id>1105</id>
   <connected>true</connected>
   <callType>video</callType>
   <nativeConnectionId>16</nativeConnectionId>
</Call> |
|---|

| GET /vmrest/calls/1 HTTP/1.1
Accept: application/json

User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com

Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg== |
|---|

| HTTP/1.1 200 OK
Pragma: No-cache
Cache-Control: no-cache
Expires: Wed, 31 Dec 1969 16:00:00 PST
Set-Cookie: JSESSIONIDSSO=849167D3D61D2F30BA278BBF949FDF0F; Path=/
Set-Cookie: JSESSIONID=28A69142E490EC63A56690F9811BDDF9; Path=/vmrest
Content-Type: application/json
{"number":"1097","id":"40","connected":"true","callType":"video","nativeConnectionId":"45"} |
|---|

| POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 15
{"op":"RECORD"} |
|---|

| HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=8279B639488165EFFAC8D330FD2A1281; Path=/
Set-Cookie: JSESSIONID=AA008CFCC9B329EA961CD1E660384785; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:13 GMT
Server:
{"op":"RECORD","resourceType":"STREAM","resourceId":"cf1cb014-6394- 4279-ab5a-74a6d680e440.wav",
"lastResult":"0","speed":"100","volume":"100","startPosition":"0"} |
|---|

| POST https://<connection-server>/vmrest/calls/<call-id> |
|---|

| <CallControl>
<op>RECORD</op>
</CallControl> |
|---|

| Response Code: 200 |
|---|

| <CallControl>
  <op>RECORD</op>
  <resourceType>STREAM</resourceType>
  <resourceId>9d59b180-6147-4796-9488-014ef73203a0.wav</resourceId>
  <sessionId>3514637e02b471</sessionId>
  <lastResult>0</lastResult>
</CallControl> |
|---|

| POST /vmrest/calls/<call-id> HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 15
{"op":"RECORD"} |
|---|

| HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=8279B639488165EFFAC8D330FD2A1281; Path=/
Set-Cookie: JSESSIONID=AA008CFCC9B329EA961CD1E660384785; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:13 GMT
Server:
1({"op":"RECORD","resourceType":"STREAM","resourceId":"a899bac7-9ee2-4c75-b3a7-e6a2a5d6d2dc.wav","sessionId":"1e14628d9a9ac1","lastResult":"0"}) |
|---|

| POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: ucbu-aricent-vm5.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
{"op":"PAUSE"} |
|---|

| HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=6A4C99C02E79D696A2DEC46C24A0B2DA; Path=/; Secure
Set-Cookie: JSESSIONID=1E642B010F5AD5630DE922B1378679DF; Path=/vmrest; Secure
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 01 Jun 2012 06:33:49 GMT
Server: 

{"op":"PAUSE","lastResult":"0","speed":"100","volume":"100","startPosition":"0"} |
|---|

| POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: ucbu-aricent-vm5.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
{"op":"RESUME"} |
|---|

| HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=687E20DEFCC984797342E37A656A1F32; Path=/; Secure
Set-Cookie: JSESSIONID=48D31DBFCBAEF586F2A9398AB11204CC; Path=/vmrest; Secure
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 01 Jun 2012 06:34:25 GMT
Server: 

{"op":"RESUME","lastResult":"0","speed":"100","volume":"100","startPosition":"0"} |
|---|

| POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 159

{"op":"PLAY","resourceType":"STREAM","resourceId":"cf1cb014-6394-4279-ab5a-74a6d680e440.wav",
"lastResult":"0","speed":"100","volume":"100","startPosition":"0"} |
|---|

| HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=CD7B1064CEB9385B6FE9279ECBDB40E3; Path=/
Set-Cookie: JSESSIONID=201BD26E840AA2CEEC242A9CCD0FE8F6; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:

{"op":"PLAY","resourceType":"STREAM","resourceId":"cf1cb014-6394-4279-ab5a-74a6d680e440.wav",
"lastResult":"0","speed":"100","volume":"100","startPosition":"0"} |
|---|

| POST https://<connection-server>/vmrest/calls/<call-id> |
|---|

| Request:
<CallControl>
   <op>PLAY</op>
   <resourceType>STREAM</resourceType>
   <resourceId>1218f93a-2ce2-4987-9589-f8e06bd54a14.wav</resourceId>
   <sessionId>2f61469411d7131</sessionId>
   <lastResult>0</lastResult>
</CallControl> |
|---|

| Response: 200 Ok
<CallControl>
   <op>PLAY</op>
   <resourceType>STREAM</resourceType>
   <resourceId>1218f93a-2ce2-4987-9589-f8e06bd54a14.wav</resourceId>
   <sessionId>2f61469411d7131</sessionId>
   <lastResult>0</lastResult>
</CallControl> |
|---|

| Request:
POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 159

{"op":"PLAY","resourceType":"STREAM","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","sessionId":"2f61469411d7131","lastResult":"0"} |
|---|

| Response:
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=CD7B1064CEB9385B6FE9279ECBDB40E3; Path=/
Set-Cookie: JSESSIONID=201BD26E840AA2CEEC242A9CCD0FE8F6; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:

1({"op":"PLAY","resourceType":"STREAM","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","sessionId":"2f61469411d7131","lastResult":"0"}) |
|---|

| DELETE /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Accept: text/html, image/gif, image/jpeg, \*; q=.2, \*/*; q=.2
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg== |
|---|

| HTTP/1.1 204 No Content
Pragma: No-cache
Cache-Control: no-cache
Expires: Wed, 31 Dec 1969 16:00:00 PST
Set-Cookie: JSESSIONIDSSO=93B286C6584533F9EE793A01E5804465; Path=/
Set-Cookie: JSESSIONID=0CCFFFCAD1C11A45EAD1E8F04B22D28D; Path=/vmrest
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server: |
|---|

| POST /vmrest/messages?userobjectid=84c14db9-7439-4326-a2e2-e516aa192dff HTTP/1.1
Content-Type: multipart/form-data;boundary=Boundary_1_16617866_1263568442453
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 731

\--Boundary_1_16617866_1263568442453
Content-Type: application/json
{"Subject":"send message test","ArrivalTime":"0","FromSub":"false"}
\--Boundary_1_16617866_1263568442453
Content-Type: application/json

{"Recipient":{"Type":"TO","Address":
{"UserGuid":"84c14db9-7439-4326-a2e2-e516aa192dff","DisplayName":"Operator"}
}}
\--Boundary_1_16617866_1263568442453
Content-Type: application/xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><CallControl><op>PLAY</op><resourceType>STREAM</resourceType><resourceId>cf1cb014-6394-4279-
ab5a-74a6d680e440.wav</resourceId><lastResult>0</lastResult><speed>100</speed><volume>100</volume><startPosition>0</startPosition></CallControl>

\--Boundary_1_16617866_1263568442453-\- |
|---|

| HTTP/1.1 202 Accepted
Set-Cookie: JSESSIONIDSSO=3D875CAE50B6B4947DEDCF5EDA119922; Path=/
Set-Cookie: JSESSIONID=842B1A6E53DAE329F6DA7525951668B4; Path=/vmrest
Content-Type: application/json
Content-Length: 0
Date: Fri, 15 Jan 2010 15:14:16 GMT
Server: |
|---|

| POST /vmrest/messages?userobjectid=84c14db9-7439-4326-a2e2-e516aa192dff HTTP/1.1
Content-Type: multipart/form-data;boundary=Boundary_1_16617866_1263568442453
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 731

\--Boundary_1_16617866_1263568442453
Content-Type: application/json
{"Subject":"send message test","ArrivalTime":"0","FromSub":"false"}
\--Boundary_1_16617866_1263568442453
Content-Type: application/json

{"Recipient":{"Type":"TO","Address":
{"UserGuid":"84c14db9-7439-4326-a2e2-e516aa192dff","DisplayName":"Operator"}
}}
\--Boundary_1_16617866_1263568442453
Content-Type: application/xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?><CallControl><op>PLAY</op><resourceType>STREAM</resourceType><resourceId>cf1cb014-6394-4279-
ab5a-74a6d680e440.wav</resourceId><sessionId><lastResult>0</lastResult><speed>100</speed><volume>100</volume><startPosition>0</startPosition></CallControl>

\--Boundary_1_16617866_1263568442453-\- |
|---|

| Request:
POST https://<connection-server>/vmrest/calls/<call-id> 
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>   
</CallControl> |
|---|

| Response:
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>
   <speed>100</speed>
   <volume>100</volume>
   <startPosition>0</startPosition>
   <lastResult>0</lastResult>
</CallControl>
Response code:200   Ok |
|---|

| Request
POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 159

{"op":"PLAY","resourceType":"HANDLER","resourceId":"0bc5155b-0989-4523-a75a-948cc691b99e.wav","lastResult":"0","speed":"100","volume":"100","startPosition":"0"} |
|---|

| Response: HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=CD7B1064CEB9385B6FE9279ECBDB40E3; Path=/
Set-Cookie: JSESSIONID=201BD26E840AA2CEEC242A9CCD0FE8F6; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:
1({"op":"PLAY","resourceType":"HANDLER","resourceId":"0bc5155b-0989-4523-a75a-948cc691b99e.wav","lastResult":"0","speed":"100","volume":"100","startPosition":"0"} |
|---|

| POST https://<connection-server>/vmrest/calls/<call-id>?handlerObjectId=<handlerObjectId> 
Request:
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>   
</CallControl> |
|---|

| Response:
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>
   <speed>100</speed>
   <volume>100</volume>
   <startPosition>0</startPosition>
   <lastResult>0</lastResult>
</CallControl>
Response code:200   Ok |
|---|

| Request:
POST /vmrest/calls/1 ? handlerObjectId=<handlerObjectId>
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 159

{"op":"PLAY","resourceType":"HANDLER","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav"} |
|---|

| Response: 
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=CD7B1064CEB9385B6FE9279ECBDB40E3; Path=/
Set-Cookie: JSESSIONID=201BD26E840AA2CEEC242A9CCD0FE8F6; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:
1({"op":"PLAY","resourceType":"HANDLER","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","lastResult":"0","speed":"100","volume":"100","startPosition":"0") |
|---|

| Request:
POST https://<connection-server>/vmrest/calls/<call-id> |
|---|

| <CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <sessionId>55d146ced50d1</sessionId>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>   
   <lastResult>0</lastResult>
</CallControl> |
|---|

| Response:
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>
   <sessionId>55d146ced50d1</sessionId>
   <lastResult>0</lastResult>
</CallControl>
Response code:200   Ok |
|---|

| Request:
POST /vmrest/calls/1 HTTP/1.1
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 159

{"op":"PLAY","resourceType":"HANDLER","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","sessionId":"2f61469411d7131"} |
|---|

| Response: 
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=CD7B1064CEB9385B6FE9279ECBDB40E3; Path=/
Set-Cookie: JSESSIONID=201BD26E840AA2CEEC242A9CCD0FE8F6; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:

1({"op":"PLAY","resourceType":"HANDLER","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","sessionId":"2f61469411d7131","lastResult":"0"}) |
|---|

| POST https://<connection-server>/vmrest/calls/<call-id>?handlerObjectId=<handlerObjectId> 
Request:
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <sessionId>55d146ced50d1</sessionId>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>   
   <lastResult>0</lastResult>
</CallControl>
Response:
<CallControl>
   <op>PLAY</op>
   <resourceType>HANDLER</resourceType>
   <resourceId>0bc5155b-0989-4523-a75a-948cc691b99e.wav</resourceId>
   <sessionId>55d146ced50d1</sessionId>
   <lastResult>0</lastResult>
</CallControl>
Response code:200   Ok |
|---|

| Request:
POST /vmrest/calls/1 ? handlerObjectId=<handlerObjectId>
Content-Type: application/json
Accept: application/json
User-Agent: Java/1.6.0_17
Host: cuc-install-67.cisco.com
Connection: keep-alive
Authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==
Content-Length: 159

{"op":"PLAY","resourceType":"HANDLER","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","sessionId":"2f61469411d7131"} |
|---|

| Response: 
HTTP/1.1 200 OK
Set-Cookie: JSESSIONIDSSO=CD7B1064CEB9385B6FE9279ECBDB40E3; Path=/
Set-Cookie: JSESSIONID=201BD26E840AA2CEEC242A9CCD0FE8F6; Path=/vmrest
Content-Type: application/json
Transfer-Encoding: chunked
Date: Fri, 15 Jan 2010 15:14:15 GMT
Server:

1({"op":"PLAY","resourceType":"HANDLER","resourceId":"1218f93a-2ce2-4987-9589-f8e06bd54a14.wav","sessionId":"2f61469411d7131","lastResult":"0"}) |
|---|

| GET http://<connection-server>/vmrest/handlers/callhandlers/<call handler object ID>/greetings/<greeting type>/greetingstreamfiles/<language code>/video |
|---|

| Response: 200
<CallControl>
    <resourceId>aad91d6d-aeca-4a72-8069-b656efb3041f.wav</resourceId>
    <sessionId>570146ed1504cb1</sessionId>
</CallControl |
|---|

| Request 
GET  vmrest/handlers/callhandlers/30600b21-1a4c-47a3-a078-8078984e5376/greetings/Standard/greetingstreamfiles/1033/video
Accept: application/json
User-Agent: Java/1.6.0_17
Host: <connection-server>
Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg= |
|---|

| Response
HTTP/1.1 201
Content-Type: application/json
Date: Fri, 15 Jan 2010 15:14:11 GMT
Server:
{ “resourceId” :” aad91d6d-aeca-4a72-8069-b656efb3041f.wav”, “sessionId” : ”570146ed1504cb1”} |
|---|

| PUT http://<connection-server>/vmrest/handlers/callhandlers/<call handler object ID>/greetings/<greeting type>/greetingstreamfiles/<language code>/video |
|---|

| <CallControl>
     <resourceId>aad91d6d-aeca-4a72-8069-b656efb3041f.wav</resourceId>
     <sessionId>570146ed1504cb1</sessionId>
</CallControl> |
|---|

| Response: 201 OK |
|---|

| Request 
PUT  vmrest/handlers/callhandlers/30600b21-1a4c-47a3-a078-8078984e5376/greetings/Standard/greetingstreamfiles/1033/video
Content-Type: application/json
Accept: application/json
Host: <connection-server>
Connection: keep-alive
authorization: Basic Y2NtYWRtaW5pc3RyYXRvcjplY3NidWxhYg==

{ “resourceId” :” aad91d6d-aeca-4a72-8069-b656efb3041f.wav”, “sessionId” : ”570146ed1504cb1”} |
|---|

| Response :
HTTP/1.1 201
Content-Type: application/json
Date: Fri, 15 Jan 2010 15:14:11 GMT
Server: |
|---|

| Field Name | Data Type | Operation | Description |
|---|---|---|---|
| number | Integer | Read/Write Only | The user extension where the caller want to
                                          					 place a call. |
| maximumRings | Integer | Read/Write | The maximum number of phone rings when a
                                          					 call is placed and if the call is not picked, the caller will get
                                          					 ring-no-answer message. Default value: 4. |
| mediaSwithObjectid | String | Read Only | The unique identifier of the MediaSwitch
                                          					 object that Cisco Unity Connection uses for placing the call to the subscriber
                                          					 phone. |
| callType | String | Read/Write | Displays whether the call type is audio or
                                          					 video. |
| callId | Integer | Read Only | The unique identifier of the call that
                                          					 Cisco Unity Connection uses for placing the call to the subscriber phone. |
| connected | Boolean | Read Only | Displays whether the subscriber is
                                          					 connected to a call or not. |
| nativeConnectionId | Integer | Read Only | The unique identifier of the call created
                                          					 by Unity Connection. |
| sessionId | String | Read/Write | This is a reference of the video recording
                                          					 on the MediaSense Server using Record API. MediaSense uniquely identifies the
                                          					 recording using the sessionId. |