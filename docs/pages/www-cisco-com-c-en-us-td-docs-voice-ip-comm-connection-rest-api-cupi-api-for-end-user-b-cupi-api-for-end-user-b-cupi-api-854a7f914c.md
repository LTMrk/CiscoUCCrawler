---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-854a7f914c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_0111.html
retrieved_at: 2026-08-21T08:04:46.789880+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 18, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Private Lists

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Private Lists

- Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Private Lists

- About Private Lists

- Voice Names

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Private Lists

## About Private Lists

A user can view, modify, create, and delete their own private lists. End users have access only to the ObjectId, DisplayName,
                              NumericId, and VoiceName fields of a private list.

Below are the various private list URIs that a user has access to.

```
GET /vmrest/user/privatelists
GET /vmrest/user/privatelists/<private list object id>
PUT /vmrest/user/privatelists/<private list object id>
POST /vmrest/user/privatelists
DELETE /vmrest/user/privatelists/<private list object id>
```

## Voice Names

A PUT to the URI below, where the HTTP content type is "audio/wav" and the payload content is the audio data, will add the
                              audio as a voice name to the private list:

```
PUT /vmrest/user/privatelists/<private list object id>/voicename
```

The voice name can always be retrieved through the URI below. It will return the audio of the voice name as an "audio/wav"
                              media type.

```
GET /vmrest/user/privatelists/<private list object id>/voicename
```

For additional details about private lists, see CUPI Private Lists.

| GET /vmrest/user/privatelists
GET /vmrest/user/privatelists/<private list object id>
PUT /vmrest/user/privatelists/<private list object id>
POST /vmrest/user/privatelists
DELETE /vmrest/user/privatelists/<private list object id> |
|---|

| PUT /vmrest/user/privatelists/<private list object id>/voicename |
|---|

| GET /vmrest/user/privatelists/<private list object id>/voicename |
|---|