---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-f868bd6b51
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_0110.html
retrieved_at: 2026-08-21T08:04:42.726672+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 18, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Location

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Location

- Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Location

- Listing and Viewing

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Location

## Listing and Viewing

The following is an example of a GET that lists your location:

```
GET http://<connection-server>/vmrest/user/location
```

The following is an example of the response from the above GET request:

```
200
OK
<?xml version="1.0" encoding="UTF-8"?>
<ConnectionLocation>
  <DefaultWaveFormatObjectId>cb85b520-e2de-4878-96e2-3331607f4671</DefaultWaveFormatObjectId>
  <DefaultWaveFormatURI>/vmrest/waveformats/cb85b520-e2de-4878-96e2-3331607f4671</DefaultWaveFormatURI>
  <DisplayName>cuc-install-43</DisplayName>
</ConnectionLocation>
```

The default wave format is the wave format that your recorded messages are stored in.

| GET http://<connection-server>/vmrest/user/location |
|---|

| 200
OK
<?xml version="1.0" encoding="UTF-8"?>
<ConnectionLocation>
  <DefaultWaveFormatObjectId>cb85b520-e2de-4878-96e2-3331607f4671</DefaultWaveFormatObjectId>
  <DefaultWaveFormatURI>/vmrest/waveformats/cb85b520-e2de-4878-96e2-3331607f4671</DefaultWaveFormatURI>
  <DisplayName>cuc-install-43</DisplayName>
</ConnectionLocation> |
|---|