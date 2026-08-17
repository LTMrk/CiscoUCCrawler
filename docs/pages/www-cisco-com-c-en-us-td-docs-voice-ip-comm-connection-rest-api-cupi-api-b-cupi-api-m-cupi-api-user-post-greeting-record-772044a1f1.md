---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-cupi-api-user-post-greeting-record-772044a1f1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_cupi_api-user-post-greeting-recording.html
retrieved_at: 2026-08-17T03:48:25.599704+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Post Greeting Recording

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- User Post Greeting Recording

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- User Post Greeting Recording

Links to Other API pages: Cisco_Unity_Connection_APIs

## Post Greeting
                        	 Recording Settings API

The following URI can be used to
                              		  view the user object ID:

```
GET https://<connection-server>/vmrest/users/<user-objectid>
```

From the above URI, get the call handler object ID.

### Update Post
                           	 Greeting Recording Settings

```
Request Body:
<CallhandlerPrimaryTemplate>
    <PlayPostGreetingRecording>1</PlayPostGreetingRecording>
</CallhandlerPrimaryTemplate>
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

JSON Example

To update post greeting recording settings, do the following:

```
Request URI:
PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<ObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
    "PlayPostGreetingRecording":"1"
}
```

The following is the response from the *PUT* request and the actual
                                 		  response will depend upon the information given by you:

```
Response Code: 204
```

### Explanation of
                           	 Data Fields

- 0: Do Not Play Recording

- 1: Play Recording to All Callers

- 2: Play Recording Only to Unidentified Callers

```
https://<connection-server>/vmrest/postgreetingrecordings
```

| GET https://<connection-server>/vmrest/users/<user-objectid> |
|---|

| Request Body:
<CallhandlerPrimaryTemplate>
    <PlayPostGreetingRecording>1</PlayPostGreetingRecording>
</CallhandlerPrimaryTemplate> |
|---|

| Response Code: 204 |
|---|

| Request URI:
PUT https://<connection-server>/vmrest/callhandlerprimarytemplates/<ObjectId>
Accept: application/json
Content-type: application/json
Connection: keep-alive
Request Body:
{
    "PlayPostGreetingRecording":"1"
} |
|---|

| Response Code: 204 |
|---|

| Parameters | Data Type | Operations | Values |
|---|---|---|---|
| PlayPostGreetingRecording | Integer | Read/Write | 0: Do Not Play Recording 1: Play Recording to All Callers 2: Play Recording Only to Unidentified Callers |
| PostGreetingRecordingObjectId | String(64) | Read/Write | Object Id of post greeting. URI to fetch it: https://<connection-server>/vmrest/postgreetingrecordings | https://<connection-server>/vmrest/postgreetingrecordings |
| https://<connection-server>/vmrest/postgreetingrecordings |

| https://<connection-server>/vmrest/postgreetingrecordings |
|---|