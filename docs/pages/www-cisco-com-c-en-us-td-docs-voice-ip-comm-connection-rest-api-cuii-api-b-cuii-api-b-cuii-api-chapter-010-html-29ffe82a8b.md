---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cuii-api-b-cuii-api-b-cuii-api-chapter-010-html-29ffe82a8b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUII_API/b_CUII_API/b_CUII_API_chapter_010.html
retrieved_at: 2026-08-21T08:07:38.926004+00:00
---

Cisco Unity Connection Imaging Interface (CUII) API

# Cisco Unity Connection Imaging Interface (CUII) API

Updated: December 28, 2018

Chapter: Cisco Unity
	 Connection Imaging Interface (CUII) API -- Using CUII for Getting Message
	 Specific Information

## Chapter: Cisco Unity
	 Connection Imaging Interface (CUII) API -- Using CUII for Getting Message
	 Specific Information

- Cisco Unity                              	 Connection Imaging Interface (CUII) API -- Using CUII for Getting Message                              	 Specific Information

- Using CUII for                              	 Getting Message Specific Information

# Cisco Unity
                     	 Connection Imaging Interface (CUII) API -- Using CUII for Getting Message
                     	 Specific Information

Links to Other API pages: Cisco_Unity_Connection_APIs

## Cisco Unity
                        	 Connection Imaging Interface (CUII) API -- Using CUII for Getting Message
                        	 Specific Information

Links to Other API pages: Cisco_Unity_Connection_APIs

### Using CUII for
                           	 Getting Message Specific Information

```
GET https://<connection-server>/vmrest/mailbox/folders/inbox/<user-alias>/notification?messageid=<messageid
```

The above request returns the message specific information, that is
                                 		  message state and message state image URL along with the unread count, unread
                                 		  urgent count, MWI status, MWI image URL for the INBOX folder.

The following is the sample response from the above GET request. The
                                 		  values can differ depending on the state of the mailbox and the message. Note
                                 		  that for deleted, invalid, or non existing message IDs, the message state is
                                 		  DELETED.

```
<NotificationInformation>
  <UnreadMsgCount>2</UnreadMsgCount>
  <UnreadUrgentMsgCount>0</UnreadUrgentMsgCount>
  <Mwi>ON</Mwi>
  <MwiImageUrl>
  /vmrest/mailbox/folders/inbox/<user_alias>/mwistatusimage
  </MwiImageUrl>
  <MsgState>Unread</MsgState>
  <MsgStateImageUrl> /vmrest/mailbox/folders/inbox/<user_alias>/msgstateimage?messageid=<msgid>
  </MsgStateImageUrl>
  </NotificationInformation>
```

| GET https://<connection-server>/vmrest/mailbox/folders/inbox/<user-alias>/notification?messageid=<messageid |
|---|

| <NotificationInformation>
  <UnreadMsgCount>2</UnreadMsgCount>
  <UnreadUrgentMsgCount>0</UnreadUrgentMsgCount>
  <Mwi>ON</Mwi>
  <MwiImageUrl>
  /vmrest/mailbox/folders/inbox/<user_alias>/mwistatusimage
  </MwiImageUrl>
  <MsgState>Unread</MsgState>
  <MsgStateImageUrl> /vmrest/mailbox/folders/inbox/<user_alias>/msgstateimage?messageid=<msgid>
  </MsgStateImageUrl>
  </NotificationInformation> |
|---|