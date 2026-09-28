---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cumi-api-b-cumi-api-b-cumi-api-chapter-011-html-12449a23a9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUMI_API/b_CUMI-API/b_CUMI-API_chapter_011.html
retrieved_at: 2026-08-21T08:06:19.004662+00:00
---

Cisco Unity Connection Messaging Interface (CUMI) API

# Cisco Unity Connection Messaging Interface (CUMI) API

Updated: December 23, 2018

Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API -- Sending a Voice Message with One or More
	 Attachments

## Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API -- Sending a Voice Message with One or More
	 Attachments

- Cisco Unity Connection Messaging                              	 Interface (CUMI) API -- Sending a Voice Message with One or More                              	 Attachments

- About Sending                              	 Voice Messages with One or More Attachments

- Sending a Voice                              	 Message with Attachments

# Cisco Unity Connection Messaging
                     	 Interface (CUMI) API -- Sending a Voice Message with One or More
                     	 Attachments

## About Sending
                        	 Voice Messages with One or More Attachments

In Cisco Unity Connection 8.5 and
                           		later, CUMI will allow voice mails to be sent that have additional attachments
                           		of any type. (In earlier versions of Connection, CUMI allows only voice
                           		messages with one audio attachment to be sent.)

## Sending a Voice
                        	 Message with Attachments

The basics of sending a voice message involve a creating multipart
                              		  HTTP form that contains an object representation of a Message, an object
                              		  representation of a Recipient list and a set of zero or more additional parts
                              		  that will be added as message attachments. If there are parts beyond the first
                              		  two, then the third one must be either audio/wav data or an object
                              		  representation of a CallControl object (the CallControl object is used when the
                              		  stream resides on the server after using CUTI to record over the phone). The
                              		  third part is considered to be the "primary" body of the voice message.

The parts beyond the third part are passed transparently to the
                              		  message system to be added as an attachment. These additional parts must have a
                              		  content type and some data.

HTTP example for a send message POST request:

```
POST /vmrest/messages HTTP/1.1
 Content-Type: multipart/mixed;boundary=Boundary_1_25804854_1282226936453
 Accept: application/xml
 MIME-Version: 1.0
 User-Agent: Java/1.6.0_21
 Host: cuc-install-67.cisco.com
 Connection: keep-alive
 Content-Length: 489122
 --Boundary_1_25804854_1282226936453
 Content-Type: application/json
 {"Subject":"subscriber send message test","ArrivalTime":"0","FromSub":"false"}
 --Boundary_1_25804854_1282226936453
 Content-Type: application/json
 {"Recipient":{"Type":"TO","Address":  
 {"ObjectId":"cffc8051-1374-4e57-8d83-9e25aff4385a","Type":"SUBSCRIBER"}}}
 --Boundary_1_25804854_1282226936453
 Content-Type: audio/wav
 RIFFWAVEfmt @>data
 ""
 <snip>
 --Boundary_1_25804854_1282226936453
 Content-Type: text/plain;name=textfile.tx
 This is a test text message
 A third line
 end on 5
 --Boundary_1_25804854_1282226936453
 Content-Type: audio/wav
 RIFFÀ¹
 <snip>
 --Boundary_1_25804854_1282226936453
 Content-Type: text/plain;name=textfile.txt
 This is a test text message
 A third line
 end on 5
 --Boundary_1_25804854_1282226936453--
```

| POST /vmrest/messages HTTP/1.1
 Content-Type: multipart/mixed;boundary=Boundary_1_25804854_1282226936453
 Accept: application/xml
 MIME-Version: 1.0
 User-Agent: Java/1.6.0_21
 Host: cuc-install-67.cisco.com
 Connection: keep-alive
 Content-Length: 489122
 --Boundary_1_25804854_1282226936453
 Content-Type: application/json
 {"Subject":"subscriber send message test","ArrivalTime":"0","FromSub":"false"}
 --Boundary_1_25804854_1282226936453
 Content-Type: application/json
 {"Recipient":{"Type":"TO","Address":  
 {"ObjectId":"cffc8051-1374-4e57-8d83-9e25aff4385a","Type":"SUBSCRIBER"}}}
 --Boundary_1_25804854_1282226936453
 Content-Type: audio/wav
 RIFFWAVEfmt @>data
 ""
 <snip>
 --Boundary_1_25804854_1282226936453
 Content-Type: text/plain;name=textfile.tx
 This is a test text message
 A third line
 end on 5
 --Boundary_1_25804854_1282226936453
 Content-Type: audio/wav
 RIFFÀ¹
 <snip>
 --Boundary_1_25804854_1282226936453
 Content-Type: text/plain;name=textfile.txt
 This is a test text message
 A third line
 end on 5
 --Boundary_1_25804854_1282226936453-- |
|---|