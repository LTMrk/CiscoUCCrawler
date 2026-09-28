---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-rest-api-cupi-api-b-cupi-api-m-voice-names-html-f08dfbae00
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/REST-API/CUPI_API/b_CUPI-API/m_voice-names.html
retrieved_at: 2026-08-17T03:47:31.822507+00:00
---

Cisco Unity Connection Provisioning Interface (CUPI) API

# Cisco Unity Connection Provisioning Interface (CUPI) API

Updated: June 20, 2022

Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Voice Names

## Chapter: Cisco Unity
	 Connection Provisioning Interface (CUPI) API -- Voice Names

# Cisco Unity
                     	 Connection Provisioning Interface (CUPI) API -- Voice Names

Links to Other API pages: Cisco_Unity_Connection_APIs

## About Voice
                        	 Names

Many objects available via the CUPI interface have a voice name field.
                           		There are two ways to access the voice name for these objects:

- For Connection versions 7.x
                                 		  and 8.0.x the voice names are accessed by using the VoiceFileURI. Modifying the
                                 		  voice name as a voice file requires a three step process as detailed below.

- For Connection versions 8.5
                                 		  and later the voice name access has been simplified so that it can be accessed
                                 		  by using a VoiceNameURI. This new URI is a standard sub-resource of the primary
                                 		  resource URI (see example below). Modifying the voice name by using the new URI
                                 		  reduces the three step process to a single step. The old VoiceFileURI still
                                 		  works in the later versions of Connection, but use of the new URI is easier.

```
http://<server>/users/<user object id>/voicename)
```

## Listing and
                        	 Viewing

### Voice Name GET for Connection 8.5 and Later

Use the standard VoiceNameURI directly to get the file:

```
GET http://<connection-server>/vmrest/<resource>/<resource id>/voicename
```

The response will return the audio/wav data for the voice name.

### Voice Name GET for
                           	 Connection 7.x and 8.0.x

First get the primary resource to
                              		find out the voice file URI, then use the VoiceFileURI to get the file:

```
GET http://<connection-server>/vmrest/voicefiles/<voice file name>
```

The response will return the audio/wav data for the voice name.

## Setting Voice
                        	 Names

Setting a Voice Name in
                              		  Connection 8.5 and Later

PUT the audio data directly to the standard resource voice name URI:

```
PUT /vmrest/<object>/<object id>/voicename

content is audio/wav data
```

The response is a 204 indicating that the content has been accepted and
                           		copied into the temporary file.

Setting a Voice Name in Connection 7.x and 8.0.x

To create a voice name for a resource is a three step process.

A place-holder for the WAV file must be created with a POST. This
                                    			 is a temporary file place-holder that can be used for up to 30 minutes. If it
                                    			 is not used within 30 minutes (assigned to a resource), the file is assumed to
                                    			 be abandoned and is automatically cleaned.

```
POST /vmrest/voicefiles
```

The response code is 201 and the content is the name of the newly
                                    			 created temporary file.

Use the temporary file name to PUT the new audio data. The HTTP
                                    			 content type is "audio/wav" and the payload content is the audio data.

```
PUT /vmrest/voicefiles/<temporary file name>
```

The response is a 204 indicating that the content has been accepted
                                    			 and copied into the temporary file.

Set the voicename field of the target resource to the temporary file
                                    			 name. See the example for a user below:

```
PUT /vmrest/users/<user object id>

<?xml version="1.0" encoding="UTF-8"?>
<User>
<VoiceName>temporary file name</VoiceName>
</User>
```