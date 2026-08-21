---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cuti-api-b-cuti-api-b-cuti-api-chapter-0100-html-d2e2470099
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUTI_API/b_CUTI_API/b_CUTI_API_chapter_0100.html
retrieved_at: 2026-08-21T08:07:09.446092+00:00
---

Cisco Unity Connection Telephony Interface (CUTI) API

# Cisco Unity Connection Telephony Interface (CUTI) API

Updated: December 27, 2018

Chapter: Cisco Unity Connection Provisioning Interface (CUTI) API -- Voice Name Upload for Distribution Lists

## Chapter: Cisco Unity Connection Provisioning Interface (CUTI) API -- Voice Name Upload for Distribution Lists

# Cisco Unity Connection Provisioning Interface (CUTI) API -- Voice Name Upload for Distribution Lists

Links to Other API pages: Cisco_Unity_Connection_APIs

## Voice Name Upload for Distribution Lists

This API is used to upload voice name to the distribution lists. There are three ways of uploading the voice name:

1. Upload a .wav file from the desktop.

2. Record using CUTI(Cisco Unity Telephony Interface) and then upload the recording.

3. Pass the .wav file as the input stream to upload the voice name.

### Add/Update the Voice Name for Users by Uploading a File from the Desktop

It is a 3 step process:

A placeholder for the WAV file must be created with a POST request. This is a temporary file placeholder that can be used
                                          for up to 30 minutes. If it is not used within 30 minutes (assigned to a resource), the file is assumed to be abandoned and
                                          is automatically cleaned.

The request is as follows:

```
POST https: //<connection-server>/vmrest/voicefiles
```

```
Response Code: 201
```

The content will be the name of the newly created temporary .wav file.

JSON Example

```
POST https://<connection-sever>/vmrest/voicefiles
Accept: application/json
Content-Type; application/json
Connection: keep-alive
```

```
Response Code: 201
0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav
```

Use the temporary file name to put the new audio data. The HTTP content type is "audio/wav" and the payload content is the
                                          audio data.

The length of the greeting can be set under the System Settings > General Configuration settings. Here you can enter the maximum
                                                         length for system call handler greetings. The range is 1 to 1,200 seconds and default setting is 90 seconds.

The request is as follows:

```
PUT https://<connection-server>/vmrest/voicefiles/<temporary file name>
```

```
Response Code: 204
```

The content has been accepted and copied into the temporary file.

JSON Example

```
POST https://<connection-sever>/vmrest/voicefiles/<temporary file name>
Accept: application/json
Content-Type; application/json
Connection: keep-alive
```

```
Response Code: 204
```

Add the file to the voice name. The request is as follows:

```
PUT https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Request Body:
<Distributionlists>
     <VoiceName>0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav</VoiceName>
</Distributionlists>
```

```
Response Code: 201
```

JSON Example

```
POST https://<connection-sever>/vmrest/distributionlists/<distributionlistobjectid>
Accept: application/json
Content-Type; application/json
Connection: keep-alive
{
     "VoiceName":"0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav"
}
```

```
Response Code: 201
```

Use the below URL in the browser to listen to the voice name.

https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename

### Add/Update Voice Name Recording the Greeting using Telephony Interface

It’s a three step process to record a new file then modify the current stream with this new stream

Call Connection

In the first step, the integration between Unity Connection and Call Manager must be setup so that a call can be setup. Refer
                                             to the document at the below link to check how to make the call.

http://docwiki.cisco.com/wiki/Cisco_Unity_Connection_Telephony_Interface_(CUTI)_API_--_Using_CUTI_for_Basic_Call_Operations&nbsp

Recording

Once the phone is answered, the second step is to record the greeting. The length of the greeting can be set under the System
                                             Settings > General Configuration settings. Here you can enter the maximum length for system call handler greetings. The range
                                             is 1 to 1,200 seconds and default setting is 90 seconds. The minimum and maximum length of the recording using telephony integration
                                             can be seen in Connection Administration under the Advanced >> Telephony settings.

Maximum Recording Time in Milliseconds – default value 1200000

Minimum Recording Duration in Milliseconds -default value 1000

The same can be fetched using APIs using the following URL:

https://<connection-server>/vmrest/configurationvalues

Check for the values

The request is as follows:

```
<ConfigurationValue>
     <Type>3</Type>
     <LastModifiedTime>2013-01-21 07:21:53.49</LastModifiedTime>
     <LastModifiedByComponent>CUADMIN</LastModifiedByComponent>
     <FullName>System.Telephony.RecordingMinimumLengthMs</FullName>
     <Value>1000</Value>
     <UserSetting>true</UserSetting>
     <MinVal>0</MinVal>
     <MaxVal>5000</MaxVal>
     <RequiresRestart>false</RequiresRestart>
</ConfigurationValue>
```

```
Response Code: 200
```

Configuration values can be modified using Connection Administration..

JSON Example

```
GET https://<connection-server>/vmrest/configurationvalues
Accept : application/json
Connection : keep-alive
{
  "@total": "2",
  "ConfigurationValue":
  [
  {
     "Type": "1",
     "FullName": "System",
     "UserSetting": "false"
     "MinVal": "0",
     "MaxVal": "0",
     "RequiresRestart": "false"
  },
  {
     "Type": "1",
     "FullName": "System.Notifier",
     "UserSetting": "false",
     "MinVal": "0",
     "MaxVal": "0",
     "RequiresRestart": "false"
  }
  ]
}
```

```
Response Code: 200
```

Use the following request to record the voice name:

```
POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Request Body:
<CallControl>
     <op>RECORD</op>
</CallControl>
```

```
Response Code: 201
```

Make a note of the output obtained, that will be the input for uploading a wave file.

JSON Example

```
POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Accept : application/json
Content-Type : application/json
Connection : keep-alive
Request Body:
{
     "op":"RECORD"
}
```

```
Response Code: 201
```

Upload the .WAV File

The third step is to upload the wave file to the distribution list voice name.

```
PUT https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename
Request Body:
<CallControl>
     <op>RECORD</op>
     <resourceType>STREAM</resourceType>
     <resourceId>67ed783c-203f-454b-a0e6-57b77820c831.wav</resourceId>
     <lastResult>0</lastResult>
     <speed>100</speed>
     <volume>100</volume>
     <startPosition>0</startPosition>
</CallControl>
```

```
Response Code: 204
```

JSON Example

```
POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename
Accept : application/json
Content-Type : application/json
Connection : keep-alive
Request Body:
{
     "op":"RECORD",
     "resourceType":"STREAM",
     "resourceId":"67ed783c-203f-454b-a0e6-57b77820c831.wav",
     "lastResult":"0", "speed":"100",
     "volume":"100",
     "startPosition":"0"
}
```

```
Response Code: 204
```

Use the following URL to listen to the voice name associated with the interview handler: Paste the URL in the browser and
                                             listen to the voice name.

https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename

### Adding Voice Name by Passing Input Stream in the Request

The voice name can also be updated using the input stream. An input stream can be created from the .wav file and passed as
                                 the request body. The URL for this should be:

https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename

The request body should be like this:

```
put.setRequestBody(new FileInputStream(file3));
```

where the PUT request is created to upload the file3 .wav file. Make sure the content type for the request should be passed
                                 as "audio/wav". Use the following URL from the browser to listen to the voice name associated with the distribution list:

https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename

| Step 1 | A placeholder for the WAV file must be created with a POST request. This is a temporary file placeholder that can be used
                                          for up to 30 minutes. If it is not used within 30 minutes (assigned to a resource), the file is assumed to be abandoned and
                                          is automatically cleaned. The request is as follows: POST https: //<connection-server>/vmrest/voicefiles Response Code: 201 The content will be the name of the newly created temporary .wav file. JSON Example POST https://<connection-sever>/vmrest/voicefiles
Accept: application/json
Content-Type; application/json
Connection: keep-alive Response Code: 201
0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav | POST https: //<connection-server>/vmrest/voicefiles | Response Code: 201 | POST https://<connection-sever>/vmrest/voicefiles
Accept: application/json
Content-Type; application/json
Connection: keep-alive | Response Code: 201
0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav |
|---|---|---|---|---|---|
| POST https: //<connection-server>/vmrest/voicefiles |
| Response Code: 201 |
| POST https://<connection-sever>/vmrest/voicefiles
Accept: application/json
Content-Type; application/json
Connection: keep-alive |
| Response Code: 201
0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav |
| Step 2 | Use the temporary file name to put the new audio data. The HTTP content type is "audio/wav" and the payload content is the
                                          audio data. Note The length of the greeting can be set under the System Settings > General Configuration settings. Here you can enter the maximum
                                                         length for system call handler greetings. The range is 1 to 1,200 seconds and default setting is 90 seconds. The request is as follows: PUT https://<connection-server>/vmrest/voicefiles/<temporary file name> Response Code: 204 The content has been accepted and copied into the temporary file. JSON Example POST https://<connection-sever>/vmrest/voicefiles/<temporary file name>
Accept: application/json
Content-Type; application/json
Connection: keep-alive Response Code: 204 | Note | The length of the greeting can be set under the System Settings > General Configuration settings. Here you can enter the maximum
                                                         length for system call handler greetings. The range is 1 to 1,200 seconds and default setting is 90 seconds. | PUT https://<connection-server>/vmrest/voicefiles/<temporary file name> | Response Code: 204 | POST https://<connection-sever>/vmrest/voicefiles/<temporary file name>
Accept: application/json
Content-Type; application/json
Connection: keep-alive | Response Code: 204 |
| Note | The length of the greeting can be set under the System Settings > General Configuration settings. Here you can enter the maximum
                                                         length for system call handler greetings. The range is 1 to 1,200 seconds and default setting is 90 seconds. |
| PUT https://<connection-server>/vmrest/voicefiles/<temporary file name> |
| Response Code: 204 |
| POST https://<connection-sever>/vmrest/voicefiles/<temporary file name>
Accept: application/json
Content-Type; application/json
Connection: keep-alive |
| Response Code: 204 |
| Step 3 | Add the file to the voice name. The request is as follows: PUT https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Request Body:
<Distributionlists>
     <VoiceName>0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav</VoiceName>
</Distributionlists> Response Code: 201 JSON Example POST https://<connection-sever>/vmrest/distributionlists/<distributionlistobjectid>
Accept: application/json
Content-Type; application/json
Connection: keep-alive
{
     "VoiceName":"0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav"
} Response Code: 201 Use the below URL in the browser to listen to the voice name. https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename | PUT https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Request Body:
<Distributionlists>
     <VoiceName>0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav</VoiceName>
</Distributionlists> | Response Code: 201 | POST https://<connection-sever>/vmrest/distributionlists/<distributionlistobjectid>
Accept: application/json
Content-Type; application/json
Connection: keep-alive
{
     "VoiceName":"0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav"
} | Response Code: 201 |
| PUT https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Request Body:
<Distributionlists>
     <VoiceName>0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav</VoiceName>
</Distributionlists> |
| Response Code: 201 |
| POST https://<connection-sever>/vmrest/distributionlists/<distributionlistobjectid>
Accept: application/json
Content-Type; application/json
Connection: keep-alive
{
     "VoiceName":"0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav"
} |
| Response Code: 201 |

| POST https: //<connection-server>/vmrest/voicefiles |
|---|

| Response Code: 201 |
|---|

| POST https://<connection-sever>/vmrest/voicefiles
Accept: application/json
Content-Type; application/json
Connection: keep-alive |
|---|

| Response Code: 201
0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav |
|---|

| Note | The length of the greeting can be set under the System Settings > General Configuration settings. Here you can enter the maximum
                                                         length for system call handler greetings. The range is 1 to 1,200 seconds and default setting is 90 seconds. |
|---|---|

| PUT https://<connection-server>/vmrest/voicefiles/<temporary file name> |
|---|

| Response Code: 204 |
|---|

| POST https://<connection-sever>/vmrest/voicefiles/<temporary file name>
Accept: application/json
Content-Type; application/json
Connection: keep-alive |
|---|

| Response Code: 204 |
|---|

| PUT https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Request Body:
<Distributionlists>
     <VoiceName>0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav</VoiceName>
</Distributionlists> |
|---|

| Response Code: 201 |
|---|

| POST https://<connection-sever>/vmrest/distributionlists/<distributionlistobjectid>
Accept: application/json
Content-Type; application/json
Connection: keep-alive
{
     "VoiceName":"0ad46c53-44eb-4da6-988c-4f07fabc6bdd.wav"
} |
|---|

| Response Code: 201 |
|---|

| Step 1 | Call Connection In the first step, the integration between Unity Connection and Call Manager must be setup so that a call can be setup. Refer
                                             to the document at the below link to check how to make the call. http://docwiki.cisco.com/wiki/Cisco_Unity_Connection_Telephony_Interface_(CUTI)_API_--_Using_CUTI_for_Basic_Call_Operations&nbsp |
|---|---|
| Step 2 | Recording Once the phone is answered, the second step is to record the greeting. The length of the greeting can be set under the System
                                             Settings > General Configuration settings. Here you can enter the maximum length for system call handler greetings. The range
                                             is 1 to 1,200 seconds and default setting is 90 seconds. The minimum and maximum length of the recording using telephony integration
                                             can be seen in Connection Administration under the Advanced >> Telephony settings. Maximum Recording Time in Milliseconds – default value 1200000 Minimum Recording Duration in Milliseconds -default value 1000 The same can be fetched using APIs using the following URL: https://<connection-server>/vmrest/configurationvalues Check for the values The request is as follows: <ConfigurationValue>
     <Type>3</Type>
     <LastModifiedTime>2013-01-21 07:21:53.49</LastModifiedTime>
     <LastModifiedByComponent>CUADMIN</LastModifiedByComponent>
     <FullName>System.Telephony.RecordingMinimumLengthMs</FullName>
     <Value>1000</Value>
     <UserSetting>true</UserSetting>
     <MinVal>0</MinVal>
     <MaxVal>5000</MaxVal>
     <RequiresRestart>false</RequiresRestart>
</ConfigurationValue> Response Code: 200 Configuration values can be modified using Connection Administration.. JSON Example GET https://<connection-server>/vmrest/configurationvalues
Accept : application/json
Connection : keep-alive
{
  "@total": "2",
  "ConfigurationValue":
  [
  {
     "Type": "1",
     "FullName": "System",
     "UserSetting": "false"
     "MinVal": "0",
     "MaxVal": "0",
     "RequiresRestart": "false"
  },
  {
     "Type": "1",
     "FullName": "System.Notifier",
     "UserSetting": "false",
     "MinVal": "0",
     "MaxVal": "0",
     "RequiresRestart": "false"
  }
  ]
} Response Code: 200 Use the following request to record the voice name: POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Request Body:
<CallControl>
     <op>RECORD</op>
</CallControl> Response Code: 201 Make a note of the output obtained, that will be the input for uploading a wave file. JSON Example POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Accept : application/json
Content-Type : application/json
Connection : keep-alive
Request Body:
{
     "op":"RECORD"
} Response Code: 201 | <ConfigurationValue>
     <Type>3</Type>
     <LastModifiedTime>2013-01-21 07:21:53.49</LastModifiedTime>
     <LastModifiedByComponent>CUADMIN</LastModifiedByComponent>
     <FullName>System.Telephony.RecordingMinimumLengthMs</FullName>
     <Value>1000</Value>
     <UserSetting>true</UserSetting>
     <MinVal>0</MinVal>
     <MaxVal>5000</MaxVal>
     <RequiresRestart>false</RequiresRestart>
</ConfigurationValue> | Response Code: 200 | GET https://<connection-server>/vmrest/configurationvalues
Accept : application/json
Connection : keep-alive
{
  "@total": "2",
  "ConfigurationValue":
  [
  {
     "Type": "1",
     "FullName": "System",
     "UserSetting": "false"
     "MinVal": "0",
     "MaxVal": "0",
     "RequiresRestart": "false"
  },
  {
     "Type": "1",
     "FullName": "System.Notifier",
     "UserSetting": "false",
     "MinVal": "0",
     "MaxVal": "0",
     "RequiresRestart": "false"
  }
  ]
} | Response Code: 200 | POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Request Body:
<CallControl>
     <op>RECORD</op>
</CallControl> | Response Code: 201 | POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Accept : application/json
Content-Type : application/json
Connection : keep-alive
Request Body:
{
     "op":"RECORD"
} | Response Code: 201 |
| <ConfigurationValue>
     <Type>3</Type>
     <LastModifiedTime>2013-01-21 07:21:53.49</LastModifiedTime>
     <LastModifiedByComponent>CUADMIN</LastModifiedByComponent>
     <FullName>System.Telephony.RecordingMinimumLengthMs</FullName>
     <Value>1000</Value>
     <UserSetting>true</UserSetting>
     <MinVal>0</MinVal>
     <MaxVal>5000</MaxVal>
     <RequiresRestart>false</RequiresRestart>
</ConfigurationValue> |
| Response Code: 200 |
| GET https://<connection-server>/vmrest/configurationvalues
Accept : application/json
Connection : keep-alive
{
  "@total": "2",
  "ConfigurationValue":
  [
  {
     "Type": "1",
     "FullName": "System",
     "UserSetting": "false"
     "MinVal": "0",
     "MaxVal": "0",
     "RequiresRestart": "false"
  },
  {
     "Type": "1",
     "FullName": "System.Notifier",
     "UserSetting": "false",
     "MinVal": "0",
     "MaxVal": "0",
     "RequiresRestart": "false"
  }
  ]
} |
| Response Code: 200 |
| POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Request Body:
<CallControl>
     <op>RECORD</op>
</CallControl> |
| Response Code: 201 |
| POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Accept : application/json
Content-Type : application/json
Connection : keep-alive
Request Body:
{
     "op":"RECORD"
} |
| Response Code: 201 |
| Step 3 | Upload the .WAV File The third step is to upload the wave file to the distribution list voice name. PUT https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename
Request Body:
<CallControl>
     <op>RECORD</op>
     <resourceType>STREAM</resourceType>
     <resourceId>67ed783c-203f-454b-a0e6-57b77820c831.wav</resourceId>
     <lastResult>0</lastResult>
     <speed>100</speed>
     <volume>100</volume>
     <startPosition>0</startPosition>
</CallControl> Response Code: 204 JSON Example POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename
Accept : application/json
Content-Type : application/json
Connection : keep-alive
Request Body:
{
     "op":"RECORD",
     "resourceType":"STREAM",
     "resourceId":"67ed783c-203f-454b-a0e6-57b77820c831.wav",
     "lastResult":"0", "speed":"100",
     "volume":"100",
     "startPosition":"0"
} Response Code: 204 Use the following URL to listen to the voice name associated with the interview handler: Paste the URL in the browser and
                                             listen to the voice name. https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename | PUT https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename
Request Body:
<CallControl>
     <op>RECORD</op>
     <resourceType>STREAM</resourceType>
     <resourceId>67ed783c-203f-454b-a0e6-57b77820c831.wav</resourceId>
     <lastResult>0</lastResult>
     <speed>100</speed>
     <volume>100</volume>
     <startPosition>0</startPosition>
</CallControl> | Response Code: 204 | POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename
Accept : application/json
Content-Type : application/json
Connection : keep-alive
Request Body:
{
     "op":"RECORD",
     "resourceType":"STREAM",
     "resourceId":"67ed783c-203f-454b-a0e6-57b77820c831.wav",
     "lastResult":"0", "speed":"100",
     "volume":"100",
     "startPosition":"0"
} | Response Code: 204 |
| PUT https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename
Request Body:
<CallControl>
     <op>RECORD</op>
     <resourceType>STREAM</resourceType>
     <resourceId>67ed783c-203f-454b-a0e6-57b77820c831.wav</resourceId>
     <lastResult>0</lastResult>
     <speed>100</speed>
     <volume>100</volume>
     <startPosition>0</startPosition>
</CallControl> |
| Response Code: 204 |
| POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename
Accept : application/json
Content-Type : application/json
Connection : keep-alive
Request Body:
{
     "op":"RECORD",
     "resourceType":"STREAM",
     "resourceId":"67ed783c-203f-454b-a0e6-57b77820c831.wav",
     "lastResult":"0", "speed":"100",
     "volume":"100",
     "startPosition":"0"
} |
| Response Code: 204 |

| <ConfigurationValue>
     <Type>3</Type>
     <LastModifiedTime>2013-01-21 07:21:53.49</LastModifiedTime>
     <LastModifiedByComponent>CUADMIN</LastModifiedByComponent>
     <FullName>System.Telephony.RecordingMinimumLengthMs</FullName>
     <Value>1000</Value>
     <UserSetting>true</UserSetting>
     <MinVal>0</MinVal>
     <MaxVal>5000</MaxVal>
     <RequiresRestart>false</RequiresRestart>
</ConfigurationValue> |
|---|

| Response Code: 200 |
|---|

| GET https://<connection-server>/vmrest/configurationvalues
Accept : application/json
Connection : keep-alive
{
  "@total": "2",
  "ConfigurationValue":
  [
  {
     "Type": "1",
     "FullName": "System",
     "UserSetting": "false"
     "MinVal": "0",
     "MaxVal": "0",
     "RequiresRestart": "false"
  },
  {
     "Type": "1",
     "FullName": "System.Notifier",
     "UserSetting": "false",
     "MinVal": "0",
     "MaxVal": "0",
     "RequiresRestart": "false"
  }
  ]
} |
|---|

| Response Code: 200 |
|---|

| POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Request Body:
<CallControl>
     <op>RECORD</op>
</CallControl> |
|---|

| Response Code: 201 |
|---|

| POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>
Accept : application/json
Content-Type : application/json
Connection : keep-alive
Request Body:
{
     "op":"RECORD"
} |
|---|

| Response Code: 201 |
|---|

| PUT https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename
Request Body:
<CallControl>
     <op>RECORD</op>
     <resourceType>STREAM</resourceType>
     <resourceId>67ed783c-203f-454b-a0e6-57b77820c831.wav</resourceId>
     <lastResult>0</lastResult>
     <speed>100</speed>
     <volume>100</volume>
     <startPosition>0</startPosition>
</CallControl> |
|---|

| Response Code: 204 |
|---|

| POST https://<connection-server>/vmrest/distributionlists/<distributionlistobjectid>/voicename
Accept : application/json
Content-Type : application/json
Connection : keep-alive
Request Body:
{
     "op":"RECORD",
     "resourceType":"STREAM",
     "resourceId":"67ed783c-203f-454b-a0e6-57b77820c831.wav",
     "lastResult":"0", "speed":"100",
     "volume":"100",
     "startPosition":"0"
} |
|---|

| Response Code: 204 |
|---|

| put.setRequestBody(new FileInputStream(file3)); |
|---|