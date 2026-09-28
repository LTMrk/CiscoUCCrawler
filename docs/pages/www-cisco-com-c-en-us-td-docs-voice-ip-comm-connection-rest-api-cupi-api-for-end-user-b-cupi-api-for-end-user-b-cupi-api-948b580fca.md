---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-948b580fca
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_011001.html
retrieved_at: 2026-09-28T12:08:39.890809+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 24, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- UserPinSettings API

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- UserPinSettings API

- Cisco Unity Connection Provisioning Interface (CUPI) API -- UserPinSettings API

- Update Password/PIN Settings

# Cisco Unity Connection Provisioning Interface (CUPI) API -- UserPinSettings API

## Cisco Unity Connection Provisioning Interface (CUPI) API -- UserPinSettings API

### Update Password/PIN Settings

#### JSON Example

For PIN:

```
PUT https://<connection-server>/vmrest/user/credential/pin?newpin=<PIN>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

```
PUT https://<connection-server>/vmrest/user/credential/pin?newpin=<PIN>
Accept: application/json
Content-type: application/json
Connection: keep-alive
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code: 204
```

## Figuras

![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)

![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)