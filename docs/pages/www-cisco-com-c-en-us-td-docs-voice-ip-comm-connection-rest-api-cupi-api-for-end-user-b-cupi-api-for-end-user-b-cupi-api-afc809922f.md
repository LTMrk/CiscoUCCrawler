---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-afc809922f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_010010.html
retrieved_at: 2026-08-21T08:05:33.295493+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: January 24, 2019

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Greetings API

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- Greetings API

# Cisco Unity Connection Provisioning Interface (CUPI) API -- Greetings API

## About Greeting API

The greeting type can be any one of the following:

Standard

Alternate

Busy

Closed

Holiday

Error

Internal

An end user can have greetings in more than one language. The first resource allows users to access the list of greetings
                              that currently have audio. In case there are no greetings recorded, the list will be empty.

### Listing Details of a Greeting

A GET will return a GreetingStreamFiles object that contains a set of GreetingStreamFile objects for the specified greeting
                                 type. Each GreetingStreamFile object has a URI that allows access to the greeting audio. The individual audio URI's are in
                                 the following format:

```
https://<connection-server>/vmrest/user/greetings/<greetingType/greetingstreamfiles
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
<GreetingStreamFiles>
  <GreetingStreamFile>
   <URI>/vmrest/user/greetings/Alternate/greetingstreamfiles/1033</URI>
  </GreetingStreamFile>
</GreetingStreamFiles>
```

```
Response Code:200
```

JSON Example

```
https://<connection-server>/vmrest/user/greetings/<greetingType>/greetingstreamfiles
Accept: application/json
Connection: keep-alive
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
{
"GreetingStreamFiles":
  {
   "GreetingStreamFile":
   {
   "URI": "/vmrest/user/greetings/Alternate/greetingstreamfiles/1033"
   }
  }
}
```

```
Response Code:200
```

To get the audio/wav file associated with a greeting type, a GET operation on the URL below needs to be performed:

```
GET https://<connection-server>/vmrest/user/greetings/<greetingType>/greetingstreamfiles/{/language-code\}
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code:200
```

Get setting for a greeting: Every user with a mailbox has an associated call handler, and thus a full compliment of greetings

```
GET https://<connection-server>/vmrest/user/greetings/<greetingType>
```

The following is the response from the above *GET* request and the actual response will depend upon the information given
                                 by you:

```
<Greeting>
  <PlayWhat>0</PlayWhat>
  <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
  <GreetingType><greetingType></GreetingType>
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt>
</Greeting>
```

```
Response Code: 200
```

JASON Example

```
https://<connection-server>/vmrest/user/greetings/<greetingType>
Accept:  application/json
Connection:  keep-alive
```

```
{
 "TimeExpires": "1972-01-01 00:00:00.0",
 "GreetingType": "Alternate",
 "PlayWhat": "0",
 "EnablePersonalVideoRecording":"false",
 "PlayRecordVideoMessagePrompt":"false"

}
```

```
Response Code:200
```

### Enabling or Disabling Greetings

The TimeExpires field determines whether a greeting is enabled or disabled. To enable a greeting, TimeExpires needs to be
                                 set to a future date, which is the date on which the greeting will expire (be disabled). To disable a greeting, simply set
                                 TimeExpires to a date in the past. Also, if TimeExpires is set to null that means it is enabled indefinitely (currently CUPI
                                 offers no ability to set this field to null).

TimeExpires is always calculated as GMT. Any time zone conversion is the responsibility of the client.

To enable the Holiday greeting until March 9th 2020, you would use the following PUT request:

```
PUT https://<connection-server>/vmrest/user/greetings/<greetingType>
```

```
<Greeting>
  <TimeExpires>2020-03-09 00:00:00.0</TimeExpires>
</Greeting>
```

The following is the response from the above *PUT* request and the actual response will depend upon the information given
                                 by you:

```
Response Code:204
```

To disable a greeting you would do a PUT request with the TimeExpires field set to a date in the past, as follows:

```
<Greeting>
  <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
</Greeting>
```

```
Response Code:204
```

### Update Greeting

The HTTPS content type of the PUT operation to update the greeting is "audio/wav" and the payload content is the audio data.
                                 If the greeting for the given type and language does not exist, the greeting audio will be created. If the greeting audio
                                 already exists, the existing audio is replaced by the new audio.

```
PUT https://<connection-server>/vmrest/user/greetings/<greetingType>/greetingstreamfiles/\{language-code\}
```

This request consumes audio/wav file. Attach a file to the request for adding or updating the greeting.

```
Response Code 204
```

### Using the CUTI to record greetings via the Phone

Greetings can be updated using recorded wave files or by using the Phone interface via the CUTI.

The following example demonstrates how to achieve this task.

Record the greeting using CUTI, the details are available at

http://docwiki.cisco.com/wiki/Cisco_Unity_Connection_Telephony_Interface_%28CUTI%29_API_--_Using_CUTI_for_Basic_Call_Operations

Update the user greeting with the recorded file:

The record operation in Step-1 returns XML/JSON output containing the details of the recorded file.

Send a PUT request on the URL

```
https://<connection-server>/vmrest/user/greetings/<greetingType>/greetingstreamfiles/<language-code>
```

with the XML/JSON returned in the step above. Below is an example JSON request body:

```
{
  "op":"RECORD",
  "resourceType":"STREAM",
  "resourceId":"cf1cb014-6394- 4279-ab5a-74a6d680e440.wav",
  "lastResult":"0",
  "speed":"100",
  "volume":"100",
  "startPosition":"0"
}
```

The Put request will update the Greetings. The update of a Greetings wave file is similar whether a audio wave file is being
                                 used or the audio is a CallControl XML/JSON schema.

| https://<connection-server>/vmrest/user/greetings/<greetingType/greetingstreamfiles |
|---|

| <GreetingStreamFiles>
  <GreetingStreamFile>
   <URI>/vmrest/user/greetings/Alternate/greetingstreamfiles/1033</URI>
  </GreetingStreamFile>
</GreetingStreamFiles> |
|---|

| Response Code:200 |
|---|

| https://<connection-server>/vmrest/user/greetings/<greetingType>/greetingstreamfiles
Accept: application/json
Connection: keep-alive |
|---|

| {
"GreetingStreamFiles":
  {
   "GreetingStreamFile":
   {
   "URI": "/vmrest/user/greetings/Alternate/greetingstreamfiles/1033"
   }
  }
} |
|---|

| Response Code:200 |
|---|

| GET https://<connection-server>/vmrest/user/greetings/<greetingType>/greetingstreamfiles/{/language-code\} |
|---|

| Response Code:200 |
|---|

| GET https://<connection-server>/vmrest/user/greetings/<greetingType> |
|---|

| <Greeting>
  <PlayWhat>0</PlayWhat>
  <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
  <GreetingType><greetingType></GreetingType>
  <EnablePersonalVideoRecording>false</EnablePersonalVideoRecording>
  <PlayRecordVideoMessagePrompt>false</PlayRecordVideoMessagePrompt>
</Greeting> |
|---|

| Response Code: 200 |
|---|

| https://<connection-server>/vmrest/user/greetings/<greetingType>
Accept:  application/json
Connection:  keep-alive |
|---|

| {
 "TimeExpires": "1972-01-01 00:00:00.0",
 "GreetingType": "Alternate",
 "PlayWhat": "0",
 "EnablePersonalVideoRecording":"false",
 "PlayRecordVideoMessagePrompt":"false"

} |
|---|

| Response Code:200 |
|---|

| PUT https://<connection-server>/vmrest/user/greetings/<greetingType> |
|---|

| <Greeting>
  <TimeExpires>2020-03-09 00:00:00.0</TimeExpires>
</Greeting> |
|---|

| Response Code:204 |
|---|

| <Greeting>
  <TimeExpires>1972-01-01 00:00:00.0</TimeExpires>
</Greeting> |
|---|

| Response Code:204 |
|---|

| PUT https://<connection-server>/vmrest/user/greetings/<greetingType>/greetingstreamfiles/\{language-code\} |
|---|

| Response Code 204 |
|---|

| https://<connection-server>/vmrest/user/greetings/<greetingType>/greetingstreamfiles/<language-code> |
|---|

| {
  "op":"RECORD",
  "resourceType":"STREAM",
  "resourceId":"cf1cb014-6394- 4279-ab5a-74a6d680e440.wav",
  "lastResult":"0",
  "speed":"100",
  "volume":"100",
  "startPosition":"0"
} |
|---|