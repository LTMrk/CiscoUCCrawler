---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cuii-api-b-cuii-api-b-cuii-api-chapter-0101-html-95c336ca38
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUII_API/b_CUII_API/b_CUII_API_chapter_0101.html
retrieved_at: 2026-08-21T08:07:47.554146+00:00
---

Cisco Unity Connection Imaging Interface (CUII) API

# Cisco Unity Connection Imaging Interface (CUII) API

Updated: January 4, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Using CUII to Get the Current Status of a Message

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Using CUII to Get the Current Status of a Message

- Cisco Unity Connection Provisioning Interface (CUPI) API -- Using CUII to Get the Current Status of a Message

# Cisco Unity Connection Provisioning Interface (CUPI) API -- Using CUII to Get the Current Status of a Message

```
GET https://<connection-server>/vmrest/mailbox/folders/inbox/<user_alias>/msgstateimage?messageid=<msgid>
```

The above request returns the image with respect to current status of the message. The message state can be read, unread,
                        deleted, read urgent, or unread urgent.

| GET https://<connection-server>/vmrest/mailbox/folders/inbox/<user_alias>/msgstateimage?messageid=<msgid> |
|---|