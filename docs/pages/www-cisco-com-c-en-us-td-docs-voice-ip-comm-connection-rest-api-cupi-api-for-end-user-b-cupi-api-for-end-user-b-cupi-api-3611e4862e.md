---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-3611e4862e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_010011.html
retrieved_at: 2026-08-21T08:05:37.427293+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 24, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Location API

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Location API

# Cisco Unity Connection Provisioning Interface (CUPI) API -- Location API

## Location API

This section contains information on how to use the API to list the details of your location when using CUPI APIs for users.
                           The location object holds several critical pieces of information, but only select pieces of information are exposed to the
                           end user through this URI.

### Listing the Location Details of a User

```
GET http://<connection-server>/vmrest/user/location
```

The following is the response from the *GET* request and the actual response will depend upon the information given by you:

```
<ConnectionLocation>
  <DefaultWaveFormatObjectId>cb85b520-e2de-4878-96e2-3331607f4671</DefaultWaveFormatObjectId>
  <DefaultWaveFormatURI>/vmrest/waveformats/cb85b520-e2de-4878-96e2-3331607f4671</DefaultWaveFormatURI>
  <DisplayName>cuc-install-43</DisplayName>
</ConnectionLocation>
```

```
Response Code: 200
```

JSON Example

```
GET http://<connection-server>/vmrest/user/location
Accept: application/json 
Content-type: application/json
Connection: keep-alive
```

The following is the response from the *GET* request and the actual response will depend upon the information given by you:

```
{ 
  "DefaultWaveFormatObjectId": "cb85b520-e2de-4878-96e2-3331607f4671",
  "DefaultWaveFormatURI": "/vmrest/waveformats/cb85b520-e2de-4878-96e2-3331607f4671",
  "DisplayName": "cuc-install-43"
}
```

```
Response Code: 200
```

The default wave format is the wave format that your recorded messages are stored in.

### Explanation of Data Field

Parameter

Operation

Data Type

Comments

DefaultWaveFormatObjectId

Read Only

String

The unique identifier of the WaveFormat object that specifies the wave format in which recorded messages are stored if the
                                             requested format is not available on the system.

DefaultWaveFormatObjectIdURI

Read Only

String

URI of the WaveFormat object that specifies the wave format in which recorded messages are stored if the requested format
                                             is not available on the system.

DisplayName

Read Only

String

Hostname of the Connection server.

| GET http://<connection-server>/vmrest/user/location |
|---|

| <ConnectionLocation>
  <DefaultWaveFormatObjectId>cb85b520-e2de-4878-96e2-3331607f4671</DefaultWaveFormatObjectId>
  <DefaultWaveFormatURI>/vmrest/waveformats/cb85b520-e2de-4878-96e2-3331607f4671</DefaultWaveFormatURI>
  <DisplayName>cuc-install-43</DisplayName>
</ConnectionLocation> |
|---|

| Response Code: 200 |
|---|

| GET http://<connection-server>/vmrest/user/location
Accept: application/json 
Content-type: application/json
Connection: keep-alive |
|---|

| { 
  "DefaultWaveFormatObjectId": "cb85b520-e2de-4878-96e2-3331607f4671",
  "DefaultWaveFormatURI": "/vmrest/waveformats/cb85b520-e2de-4878-96e2-3331607f4671",
  "DisplayName": "cuc-install-43"
} |
|---|

| Response Code: 200 |
|---|

| Parameter | Operation | Data Type | Comments |
|---|---|---|---|
| DefaultWaveFormatObjectId | Read Only | String | The unique identifier of the WaveFormat object that specifies the wave format in which recorded messages are stored if the
                                             requested format is not available on the system. |
| DefaultWaveFormatObjectIdURI | Read Only | String | URI of the WaveFormat object that specifies the wave format in which recorded messages are stored if the requested format
                                             is not available on the system. |
| DisplayName | Read Only | String | Hostname of the Connection server. |