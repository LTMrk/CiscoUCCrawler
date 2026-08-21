---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cuii-api-b-cuii-api-b-cuii-api-chapter-01-html-f958dba929
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUII_API/b_CUII_API/b_CUII_API_chapter_01.html
retrieved_at: 2026-08-21T08:07:34.935786+00:00
---

Cisco Unity Connection Imaging Interface (CUII) API

# Cisco Unity Connection Imaging Interface (CUII) API

Updated: December 28, 2018

Chapter: Cisco Unity
	 Connection Imaging Interface (CUII) API -- Using CUII for Getting the Message
	 Status

## Chapter: Cisco Unity
	 Connection Imaging Interface (CUII) API -- Using CUII for Getting the Message
	 Status

- Cisco Unity                              	 Connection Imaging Interface (CUII) API -- Using CUII for Getting the Message                              	 Status

- Cisco Unity                              	 Connection Imaging Interface (CUII) API -- Using CUII for Getting the Message                              	 Status

# Cisco Unity
                     	 Connection Imaging Interface (CUII) API -- Using CUII for Getting the Message
                     	 Status

Links to Other API pages: Cisco_Unity_Connection_APIs

```
GET https://<connection-server>/vmrest/mailbox/folders/inbox/<user-alias>/notification
```

The above request returns unread message count, unread urgent count, MWI
                        		status, and MWI image URL for the INBOX folder. The following are the sample
                        		GET requests and responses. The values can differ depending on the state of the
                        		mailbox. Note that for displaying correct behavior of MWI status and its
                        		corresponding image, MWI must be configured properly in the system. If not
                        		configured properly, the default value 'OFF' is returned, even if the unread
                        		messages are present in the mailbox.

Get Request

```
GET https://<connection-server>/vmrest/mailbox/folders/inbox/jsmith/notification
   Response
   <NotificationInformation>
   <UnreadMsgCount>2</UnreadMsgCount>
   <UnreadUrgentMsgCount>0</UnreadUrgentMsgCount>
   <Mwi>ON</Mwi>
   <MwiImageUrl>
   /vmrest/mailbox/folders/inbox/jsmith/mwistatusimage
   </MwiImageUrl>
   <MsgState> </MsgState>
   <MsgStateImageUrl> </MsgStateImageUrl>
   </NotificationInformation>
```

Get Request

```
GET https://<connection-server>/vmrest/mailbox/folders/inbox/gjoseph/notification
   Response
   <NotificationInformation>
   <UnreadMsgCount>4</UnreadMsgCount>
   <UnreadUrgentMsgCount>2</UnreadUrgentMsgCount>
   <Mwi>ON</Mwi>
   <MwiImageUrl>
   /vmrest/mailbox/folders/inbox/gjoseph/mwistatusimage
   </MwiImageUrl>
   <MsgState> </MsgState>
   <MsgStateImageUrl> </MsgStateImageUrl>
   </NotificationInformation>
```

## Cisco Unity
                        	 Connection Imaging Interface (CUII) API -- Using CUII for Getting the Message
                        	 Status

Links to Other API pages: Cisco_Unity_Connection_APIs

```
GET https://<connection-server>/vmrest/mailbox/folders/inbox/<user-alias>/notification
```

The above request returns unread message count, unread urgent count, MWI
                           		status, and MWI image URL for the INBOX folder. The following are the sample
                           		GET requests and responses. The values can differ depending on the state of the
                           		mailbox. Note that for displaying correct behavior of MWI status and its
                           		corresponding image, MWI must be configured properly in the system. If not
                           		configured properly, the default value 'OFF' is returned, even if the unread
                           		messages are present in the mailbox.

Get Request

```
GET https://<connection-server>/vmrest/mailbox/folders/inbox/jsmith/notification
   Response
   <NotificationInformation>
   <UnreadMsgCount>2</UnreadMsgCount>
   <UnreadUrgentMsgCount>0</UnreadUrgentMsgCount>
   <Mwi>ON</Mwi>
   <MwiImageUrl>
   /vmrest/mailbox/folders/inbox/jsmith/mwistatusimage
   </MwiImageUrl>
   <MsgState> </MsgState>
   <MsgStateImageUrl> </MsgStateImageUrl>
   </NotificationInformation>
```

Get Request

```
GET https://<connection-server>/vmrest/mailbox/folders/inbox/gjoseph/notification
   Response
   <NotificationInformation>
   <UnreadMsgCount>4</UnreadMsgCount>
   <UnreadUrgentMsgCount>2</UnreadUrgentMsgCount>
   <Mwi>ON</Mwi>
   <MwiImageUrl>
   /vmrest/mailbox/folders/inbox/gjoseph/mwistatusimage
   </MwiImageUrl>
   <MsgState> </MsgState>
   <MsgStateImageUrl> </MsgStateImageUrl>
   </NotificationInformation>
```

| GET https://<connection-server>/vmrest/mailbox/folders/inbox/<user-alias>/notification |
|---|

| GET https://<connection-server>/vmrest/mailbox/folders/inbox/jsmith/notification
   Response
   <NotificationInformation>
   <UnreadMsgCount>2</UnreadMsgCount>
   <UnreadUrgentMsgCount>0</UnreadUrgentMsgCount>
   <Mwi>ON</Mwi>
   <MwiImageUrl>
   /vmrest/mailbox/folders/inbox/jsmith/mwistatusimage
   </MwiImageUrl>
   <MsgState> </MsgState>
   <MsgStateImageUrl> </MsgStateImageUrl>
   </NotificationInformation> |
|---|

| GET https://<connection-server>/vmrest/mailbox/folders/inbox/gjoseph/notification
   Response
   <NotificationInformation>
   <UnreadMsgCount>4</UnreadMsgCount>
   <UnreadUrgentMsgCount>2</UnreadUrgentMsgCount>
   <Mwi>ON</Mwi>
   <MwiImageUrl>
   /vmrest/mailbox/folders/inbox/gjoseph/mwistatusimage
   </MwiImageUrl>
   <MsgState> </MsgState>
   <MsgStateImageUrl> </MsgStateImageUrl>
   </NotificationInformation> |
|---|

| GET https://<connection-server>/vmrest/mailbox/folders/inbox/<user-alias>/notification |
|---|

| GET https://<connection-server>/vmrest/mailbox/folders/inbox/jsmith/notification
   Response
   <NotificationInformation>
   <UnreadMsgCount>2</UnreadMsgCount>
   <UnreadUrgentMsgCount>0</UnreadUrgentMsgCount>
   <Mwi>ON</Mwi>
   <MwiImageUrl>
   /vmrest/mailbox/folders/inbox/jsmith/mwistatusimage
   </MwiImageUrl>
   <MsgState> </MsgState>
   <MsgStateImageUrl> </MsgStateImageUrl>
   </NotificationInformation> |
|---|

| GET https://<connection-server>/vmrest/mailbox/folders/inbox/gjoseph/notification
   Response
   <NotificationInformation>
   <UnreadMsgCount>4</UnreadMsgCount>
   <UnreadUrgentMsgCount>2</UnreadUrgentMsgCount>
   <Mwi>ON</Mwi>
   <MwiImageUrl>
   /vmrest/mailbox/folders/inbox/gjoseph/mwistatusimage
   </MwiImageUrl>
   <MsgState> </MsgState>
   <MsgStateImageUrl> </MsgStateImageUrl>
   </NotificationInformation> |
|---|