---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-254ba545d8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_vvb-configuration-api_1501.html
retrieved_at: 2026-08-21T16:49:07.159435+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: VVB Configuration API

## Chapter: VVB Configuration API

- VVB Configuration API

- Virtualized Voice Browser Configuration API

# VVB Configuration API

## Virtualized Voice Browser Configuration API

The Cisco Virtualized Voice Browser (VVB) is an optional component that is configured as an external machine in the Packaged
                           CCE System Inventory. Cisco VVB can be used as an alternative to the use of VXML gateways, which is to send the HTTP requests
                           to CVP VXML server.

This API is used to configure the VVB parameters like Media and Security, Speech Servers, Applications properties, and fetch
                           the configured data from AW DB.

### URL

For Main site, provide site_name as 'Core'.

### Operations

get : Gets the VVB device configuration data for the core or remote datacenter.

update : Updates the VVB device configurations.

### Parameters

Media Parameter

codec : Required. Audio codecs are supported.

MRCPVersion : Required. Version of the MRCP protocol used to communicate between ASR/TTS server and Cisco VVB.

ASR-TTS service is not supported using G729 codec; therefore, MRCP is not applicable for this codec.

overrideSystemPrompt : To override the system default prompt files. When enabled, the system plays the custom recorded prompt that is uploaded
                                          to the appropriate language directory under Prompt Management on Cisco VVB Admin UI.

Parameter

Default value

Supported values

Editable

VVB engine restart required after modification

codec

G711U

G711U

G711A

G729

Yes

Yes

MRCPVersion

MRCPv2

MRCPv1

MRCPv2

Yes

Yes

overrideSystemPrompt

false

true, false

Yes

Yes

Security Parameter

sipTLSEnabled : Required. When enabled, this setting secures SIP signaling on the IVR leg.

tlsVersion : Required. Allows you to select one or more TLS versions of SIP. When you select a given TLS (SIP) version, Cisco VVB will
                                          support SIP TLS requests for this version and the higher supported versions.

To enable this parameter, set the sipTLSEnabled parameter value to true.

cipher : Required. Defines the ciphers supported by Cisco VVB, with key size lesser than or equal to 1024 bits.

To enable this parameter, set the sipTLSEnabled parameter value to true.

srtpEnabled : When SRTP (Secure Real-time Transport Protocol) is enabled, the IVR media is encrypted. The IVR leg is secured. SRTP uses
                                          Crypto-Suite AES_CM_128_HMAC_SHA1_32 for encrypting the media stream.

To enable this parameter, set the sipTLSEnabled parameter value to true.

allowMixedMode : When Allow RTP (Mixed mode) is enabled, the VVB accepts both SRTP and RTP call flows. You can enable Allow RTP (Mixed mode)
                                          only when SRTP is enabled.

To enable this parameter, set the sipTLSEnabled and srtpEnabled parameters value to true.

Parameter

Default value

Supported values

Editable

VVB engine restart required after modification

sipTLSEnabled

false

true, false

Yes

Yes

tlsVersion

TLSv1.2

TLSv1.0

TLSv1.1

TLSv1.2

Yes

Yes

cipher

TLS_RSA_WITH_AES_128_CBC_SHA - this cipher must be part of the cipher list as it is mandatory for TLSv1.2

Any other JDK supported ciphers

Add/Delete

Yes

srtpEnabled

false

true, false

Yes

Yes

allowMixedMode

false

true, false

Yes

Yes

Speech Server

asrServerName : Required. Hostname or IP address of the ASR server.

ttsServerName : Required. Hostname or IP address of the TTS server.

Application & Triggers

By default, Packaged CCE will configure three applications - Comprehensive, Ringtone and Error. Below are the application
                                    specific parameters that you can edit.

Comprehensive

Parameter

Description

applicationName

Required. Application name - Comprehensive

sigDigits

The data type of the attribute is Integer. Enter the number of digits that are used as sigdigit. Range is 0 to 20.

When Cisco VVB receives a call, the CVP comprehensive service is configured to strip the digits, so that when the IVR leg
                                                      of the call is set up, the original label is used on the incoming VoiceXML request.

maximumSession

Required. Number of sessions to associate with the Comprehensive application.

This number must not exceed the maximum number of ports supported for Cisco VVB profile.

The data type of the attribute is integer. The default value is 600. Range is 1 to 600.

enableSecurity

Enable the option to encrypt the communication between Cisco VVB and VXML server.

By default, this feature is disabled. The data type of the attribute is Boolean (Enable/Disable).

sipTriggers

SIP triggers required to invoke the application in response to incoming calls.

Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application.

Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too.

Ringtone

Parameter

Description

applicationName

Required. Application name - Ringtone

maximumSession

Required. Number of sessions to associate with the Ringtone application.

The data type of the attribute is integer. The default value is 600. Range is 1 to 600.

sipTriggers

SIP triggers required to invoke the application in response to incoming calls.

Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application.

Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too.

Error

Parameter

Description

applicationName

Required. Application name - Error

maximumSession

Required. Number of sessions to associate with the Error application.

The data type of the attribute is integer. The default value is 600. Range is 1 to 600.

customErrorPrompt

The custom error .wav file to play. The parameter is editable.

Specify the custom prompt already uploaded into Cisco VVB, else default error prompt will be used.

sipTriggers

SIP triggers required to invoke the application in response to incoming calls.

Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application.

Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too.

### Example Get Response

```
<VVB>
<media>
    <codec>G711U</codec>
    <MRCPVersion>MRCPv2</MRCPVersion>
    <overrideSystemPrompt>false</overrideSystemPrompt>
</media>
<security>
    <sipTLSEnabled>false</sipTLSEnabled>
    <tlsVersion>TLSv1.2</tlsVersion>
    <ciphers>
        <cipher>TLS_RSA_WITH_AES_128_CBC_SHA</cipher>
    </ciphers>
    <srtp>false</srtp>
    <allowMixedMode>false</allowMixedMode>
</security>
<Applications>
    <application>
        <applicationName>Comprehensive</applicationName>
        <sigDigits>0</sigDigits>
        <maximumSession>600</maximumSession>
        <enableSecurity>false</enableSecurity>
        <sipTriggers>
            <label>7777*</label>
            <label>8888*</label>
        </sipTriggers>
    </application>
    <application>
        <applicationName>Ringtone</applicationName>
        <maximumSession>600</maximumSession>
        <sipTriggers>
            <label>91919191*</label>
        </sipTriggers>
    </application>
    <application>
        <applicationName>Error</applicationName>
        <maximumSession>600</maximumSession>
        <sipTriggers>
            <label>92929292*</label>
        </sipTriggers>
    </application>
</Applications>
<asrServers>
    <asrServer>
        <asrServerName>10.10.10.10</asrServerName>
        <port>5060</port>
    </asrServer>
    <asrServer>
        <asrServerName>11.11.11.11</asrServerName>
        <port>5060</port>
    </asrServer>
</asrServers>
<ttsServers>
    <ttsServer>
        <ttsServerName>10.10.10.10</ttsServerName>
        <port>5060</port>
    </ttsServer>
    <ttsServer>
        <ttsServerName>11.11.11.11</ttsServerName>
        <port>5060</port>
    </ttsServer>
</ttsServers>
</VVB>
```

Following are the REST responses received when the REST API runs to configure the VVB devices for a given site:

Success - Configuration changes persist in AW DB and synchronized with respective VVB devices.

Code: 200

Response: Successfully saved

Partial Success - Configuration changes persist in AW DB, but failed to synchronize with one or more VVB devices.

Code: 200

Response: Configuration update failed for one or more devices. (This occurs when the AW DB is updated but Sync with VVB failed.)

Code: 503

Response: The server is currently busy. Please try again later. (This occurs when data synchronization to a device is in progress.)

```
<apiErrors>
<apiError>
<errorMessage>Configuration update failed for one or more devices.</errorMessage>
<errorType>PARTIAL_SUCCESS</errorType>
</apiError>
</apiErrors>
```

Failure - The configuration updates to AW DB is failed.

| Note | For Main site, provide site_name as 'Core'. |
|---|---|

| Note | ASR-TTS service is not supported using G729 codec; therefore, MRCP is not applicable for this codec. |
|---|---|

| Parameter | Default value | Supported values | Editable | VVB engine restart required after modification |
|---|---|---|---|---|
| codec | G711U | G711U G711A G729 | Yes | Yes |
| MRCPVersion | MRCPv2 | MRCPv1 MRCPv2 | Yes | Yes |
| overrideSystemPrompt | false | true, false | Yes | Yes |

| Parameter | Default value | Supported values | Editable | VVB engine restart required after modification |
|---|---|---|---|---|
| sipTLSEnabled | false | true, false | Yes | Yes |
| tlsVersion | TLSv1.2 | TLSv1.0 TLSv1.1 TLSv1.2 | Yes | Yes |
| cipher | TLS_RSA_WITH_AES_128_CBC_SHA - this cipher must be part of the cipher list as it is mandatory for TLSv1.2 | Any other JDK supported ciphers | Add/Delete | Yes |
| srtpEnabled | false | true, false | Yes | Yes |
| allowMixedMode | false | true, false | Yes | Yes |

| Parameter | Description |
|---|---|
| applicationName | Required. Application name - Comprehensive |
| sigDigits | The data type of the attribute is Integer. Enter the number of digits that are used as sigdigit. Range is 0 to 20. When Cisco VVB receives a call, the CVP comprehensive service is configured to strip the digits, so that when the IVR leg
                                                      of the call is set up, the original label is used on the incoming VoiceXML request. |
| maximumSession | Required. Number of sessions to associate with the Comprehensive application. Note This number must not exceed the maximum number of ports supported for Cisco VVB profile. The data type of the attribute is integer. The default value is 600. Range is 1 to 600. | Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. |
| Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. |
| enableSecurity | Enable the option to encrypt the communication between Cisco VVB and VXML server. By default, this feature is disabled. The data type of the attribute is Boolean (Enable/Disable). |
| sipTriggers | SIP triggers required to invoke the application in response to incoming calls. Note Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application. Valid input triggers are numbers (0-9), asterisk (*), and period (.). For example: 9191*. Note Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too. | Note | Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application. | Note | Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too. |
| Note | Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application. |
| Note | Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too. |

| Note | This number must not exceed the maximum number of ports supported for Cisco VVB profile. |
|---|---|

| Note | Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application. |
|---|---|

| Note | Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too. |
|---|---|

| Parameter | Description |
|---|---|
| applicationName | Required. Application name - Ringtone |
| maximumSession | Required. Number of sessions to associate with the Ringtone application. The data type of the attribute is integer. The default value is 600. Range is 1 to 600. |
| sipTriggers | SIP triggers required to invoke the application in response to incoming calls. Note Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application. Valid input triggers are numbers (0-9), asterisk (*), and period (.). For example: 9191*. Note Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too. | Note | Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application. | Note | Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too. |
| Note | Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application. |
| Note | Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too. |

| Note | Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application. |
|---|---|

| Note | Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too. |
|---|---|

| Parameter | Description |
|---|---|
| applicationName | Required. Application name - Error |
| maximumSession | Required. Number of sessions to associate with the Error application. The data type of the attribute is integer. The default value is 600. Range is 1 to 600. |
| customErrorPrompt | The custom error .wav file to play. The parameter is editable. Note Specify the custom prompt already uploaded into Cisco VVB, else default error prompt will be used. | Note | Specify the custom prompt already uploaded into Cisco VVB, else default error prompt will be used. |
| Note | Specify the custom prompt already uploaded into Cisco VVB, else default error prompt will be used. |
| sipTriggers | SIP triggers required to invoke the application in response to incoming calls. Note Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application. Valid input triggers are numbers (0-9), asterisk (*), and period (.). For example: 9191*. Note Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too. | Note | Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application. | Note | Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too. |
| Note | Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application. |
| Note | Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too. |

| Note | Specify the custom prompt already uploaded into Cisco VVB, else default error prompt will be used. |
|---|---|

| Note | Each time you invoke the API, the new list of SIP triggers overrides the existing triggers associated with the application. |
|---|---|

| Note | Do not create a trigger with only an asterisk or a period. If the trigger contains these characters, provide a number too. |
|---|---|