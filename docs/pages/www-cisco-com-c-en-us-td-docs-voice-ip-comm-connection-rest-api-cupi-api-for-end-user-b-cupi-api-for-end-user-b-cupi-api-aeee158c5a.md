---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-for-end-user-b-cupi-api-for-end-user-b-cupi-api-aeee158c5a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API_for_End_User/b_CUPI_API_for_End_User/b_CUPI_API_for_End_User_chapter_01.html
retrieved_at: 2026-08-21T08:04:21.527234+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users

Updated: December 21, 2018

Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Basics, Voice Name, Greetings

## Chapter: Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Basics, Voice Name, Greetings

# Cisco Unity Connection Provisioning Interface (CUPI) API -- For End Users -- Basics, Voice Name, Greetings

## Basic User Information

Do the following GET to see a subset of the User fields that an administrator can access:

```
GET /vmrest/user
```

## Voice Name

The following GET allows end users to get the audio that is their recorded voice name and to change the audio:

```
GET /vmrest/user/voicename
PUT /vmrest/user/voicename
```

PUT takes audio/wav data as the HTTP content.

## Greeting Audio

The following GET allows end users to listen to and modify their personal greeting:

```
GET /vmrest/user/greetings/\{greeting type\}/greetingstreamfiles
```

The \{greeting type\} can be any one of the following:

Standard

Alternate

Busy

Closed

Holiday

Error

Internal

An end user can have greetings in more than one language. The first resource allows users to access the list of greetings
                              that currently have audio. It is possible that the user has no greetings recorded, in which case the list will be empty.

A GET will return a GreetingStreamFiles object that contains a set of GreetingStreamFile objects for the specified greeting
                              type. Each GreetingStreamFile object will have a URI that allows access to the greeting audio. The individual audio URI's
                              are in the format:

```
GET /vmrest/user/greetings/\{greeting type\}/greetingstreamfiles/\{language\}
```

The \{language\} is a locale identifier (e.g. 1033 is English - United States).

This resource identifier returns the audio of the greeting as an "audio/wav" media type:

```
PUT /vmrest/user/greetings/\{greeting type\}/greetingstreamfiles/\{language\}
```

The HTTP content type of the PUT is "audio/wav" and the payload content is the audio data. If the greeting for the given type
                              and language does not exist, the greeting audio will be created. If the greeting audio already exists, the existing audio
                              is replaced by the new audio.

## Class of Services

The user's class of service (COS) can be retrieved but not set via the following URL:

```
GET /vmrest/user/cos
```

| GET /vmrest/user |
|---|

| GET /vmrest/user/voicename
PUT /vmrest/user/voicename |
|---|

| GET /vmrest/user/greetings/\{greeting type\}/greetingstreamfiles |
|---|

| GET /vmrest/user/greetings/\{greeting type\}/greetingstreamfiles/\{language\} |
|---|

| PUT /vmrest/user/greetings/\{greeting type\}/greetingstreamfiles/\{language\} |
|---|

| GET /vmrest/user/cos |
|---|