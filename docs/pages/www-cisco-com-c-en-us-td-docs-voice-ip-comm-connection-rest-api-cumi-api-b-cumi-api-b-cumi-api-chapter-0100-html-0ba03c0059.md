---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cumi-api-b-cumi-api-b-cumi-api-chapter-0100-html-0ba03c0059
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUMI_API/b_CUMI-API/b_CUMI-API_chapter_0100.html
retrieved_at: 2026-08-21T08:06:23.034849+00:00
---

Cisco Unity Connection Messaging Interface (CUMI) API

# Cisco Unity Connection Messaging Interface (CUMI) API

Updated: December 23, 2018

Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API -- Message Recall API

## Chapter: Cisco Unity Connection Messaging
	 Interface (CUMI) API -- Message Recall API

- Cisco Unity Connection Messaging                              	 Interface (CUMI) API -- Message Recall API

- Message Recall                              	 API

# Cisco Unity Connection Messaging
                     	 Interface (CUMI) API -- Message Recall API

## Message Recall
                        	 API

About Recalling Messages

In Cisco Unity Connection 10.0 and later, CUMI allows recalling of
                              		  voice mails until the sent messages is available in sent folder.

Recalling Message using API

CUMI API allows recalling of voicemails using API. If messages is
                              		  read by another user then this message will not get recalled from that user. If
                              		  voice message is available in sent folder then voice message can be recalled
                              		  and total count of voicemails for that user will be reduced. A message can be
                              		  recall by a PUT request to the root URI:

```
/vmrest/messages/<message-id>/recall
```

```
Response:  Messages is successfully recalled
HTTP1.1  204
```

Example of API:

```
https://<ser/vmrest/messages/0:a8deea61-c2e3-4896-ad0a-124d1723ddcc/recall
```

| /vmrest/messages/<message-id>/recall |
|---|

| https://<ser/vmrest/messages/0:a8deea61-c2e3-4896-ad0a-124d1723ddcc/recall |
|---|