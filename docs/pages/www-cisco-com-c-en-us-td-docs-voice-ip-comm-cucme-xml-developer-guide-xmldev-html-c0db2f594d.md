---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-xml-developer-guide-xmldev-html-c0db2f594d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/xml/developer/guide/xmldev.html
retrieved_at: 2026-08-21T09:47:52.821074+00:00
---

XML Provisioning Guide for Cisco CME/SRST

# XML Provisioning Guide for Cisco CME/SRST

### Download Options

Updated: November 2, 2007

## Table Of Contents

XML API for Cisco Unified CME and Cisco Unified SRST Developer Guide

Contents

Target Audience

Prerequisites

Information About the XML API

Examples

ISexecCLI

Request:: Example

Response: Example

ISSaveConfig

Request: Example

Response: Example

ISgetGlobal

Request: Example

Response: Example

ISgetDevice

SCCP Request: Example

SCCP Response: Example

SIP Request: Example

SIP Response: Example

ISgetExtension

SCCP Request: Example

SCCP Response: Example

SIP Request: Example

SIP Response: Example

ISsetKeyPhones

Request: Example

Response

ISunsetKeyPhones

Request: Example

Response: Example

ISgetEvtCounts

Request: Example

Response: Example

ISgetDevEvts

Request: Example

Response: Example

ISgetExtEvts

Request: Example

Response: Example

ISgetUser

Request: Example

Response: Example

ISupdateUser

Request: Example

Response: Example

ISgetVoiceRegGlobal

Request: Example

Response: Example

ISgetSessionServer

Request: Example

Response: Example

ISgetPresenceGlobal

Request: Example:

Response: Example

Additional References

Related Documents

Technical Assistance

## XML API for Cisco Unified CME and Cisco Unified SRST Developer Guide

Last Updated: September 8, 2008

This document describes the eXtensible Markup Language (XML) Application Programming Interface (API) supported in Cisco Unified Communications Express (Cisco Unified CME) and Cisco Unified Survivable Remote Site Telephony (Cisco Unified SRST).

## Contents

• Target Audience

• Prerequisites

• Information About the XML API

• Examples

• Additional References

## Target Audience

This guide assumes the developer has knowledge of a high-level programming language, such as C++, Java, or an equivalent language. The developer must also have knowledge or experience in the following areas:

• TCP/IP Protocol

• Hypertext Transport Protocol

• Socket programming

• XML

In addition, users of this programming guide must have a firm grasp of XML Schema, which was used to define the AXL requests, responses, and errors. For more information on XML Schema, please see the XML Schema Part 0: Primer Second Edition .

## Prerequisites

• For Cisco Unified CME: XML API must be configured in Cisco Unified CME. For configuration information, see the "Configuring the XML API" section of the Cisco Unified CME Administrator Guide .

• For Cisco Unified SRST: URL for the XML API schema must be configured in Cisco Unified SRST. For configuration information, see the "Defining XML API Schema" section of the Cisco Unified SRST Administrator Guide .

## Information About the XML API

The XML API support in Cisco Unified CME and Cisco Unified SRST provides a mechanism for inserting, retrieving, updating, and removing data from the Cisco router using eXtensible Markup Language (XML).

Request methods are XML structures that are passed to the XML server in Cisco Unified CME and Cisco Unified SRST using HTTP POST. The XML server receives the XML structures and executes the request. If the request completes successfully, then the appropriate XML response is returned.

Table 1 lists the request and response methods for the XML API along with the purpose and printers for each method.

Table 1

Description

Request

Parameter

Response

System

Execute configuration commands.

ISexecCLI

command

ISexecCLIResponse

Save router configuration to nvram.

ISSaveConfig

—

ISSaveConfigResult

SCCP

Get system status for Cisco Unified CME or Cisco Unified SRST.

ISgetGlobal

—

ISgetGlobalResponse

Get status of an IP phone.

ISgetDevice

Any combination of the following:

ISDevID ISDevName

ISgetDeviceResponse

Get status of an extension associated with an IP phone.

ISgetExtension

Any combination of the following:

ISExtID ISExtNumber

ISgetExtensionResponse

Set key phones

ISsetKeyPhones

ISPhoneName

ISsetKeyPhonesResponse

Remove key phone configuration.

ISunsetKeyPhones

ISPhoneName

ISunsetKeyPhonesResponse

Get total event counts.

ISgetEvtCounts

—

ISgetEvtCountsResponse

Get device event history

ISgetDevEvts

Any combination of the following:

ISDevID ISDevName ISDevEvtID

ISgetDevEvtsResponse

Get extension event history

ISgetExtEvts

Any combination of the following:

ISExtID ISExtNumber ISExtEvtID

ISgetExtEvtsResponse

Get user information

ISgetUser

ISuserID

ISgetUserResponse

Set user information

ISupdateUser

ISuserID and ISpassword

ISupdateUserResult

SIP

Get system status for a Cisco Unified CME running SIP.

ISgetVoiceRegGlobal

—

ISgetVoiceRegGlobalResponse

Get status of an IP phone.

ISgetDevice

Any combination of the following:

ISPoolID ISPoolName

ISgetDeviceResponse

Get status of an extension associated with an IP phone.

ISgetExtension

Any combination of the following:

ISVoiceRegDNID ISVoiceRegDNName ISVoiceRegNumber

ISgetExtensionResponse

Get status of a session server.

ISgetSessionServer

Any combination of the following:

ISSessionServerID ISSessionServerName

ISgetSessionServerResponse

Get configuration for Presence.

ISgetPresenceGlobal

—

ISgetPresenceGlobalResponse

XML API Methods: Request and Response

## Examples

This section contains the following examples for the following XML API methods:

• ISexecCLI

• ISSaveConfig

• ISgetGlobal

• ISgetDevice

• ISgetExtension

• ISsetKeyPhones

• ISunsetKeyPhones

• ISgetEvtCounts

• ISgetDevEvts

• ISgetExtEvts

• ISgetUser

• ISupdateUser

• ISgetVoiceRegGlobal

• ISgetSessionServer

• ISgetPresenceGlobal

### ISexecCLI

Use ISexecCLI to execute a list of Cisco IOS commands on the Cisco router. The request must include the CLI parameter with the Cisco IOS command string for each command to be executed.

### Request:: Example

<SOAP-ENV:Envelope>

<SOAP-ENV:Body>

<axl>

<request xsi:type="ISexecCLI">

<ISexecCLI>

<CLI>ephone 4</CLI>

<CLI>mac-address 000D.BC80.EB51</CLI>

<CLI>type 7960</CLI>

<CLI>button 1:1</CLI>

</ISexecCLI>

</request>

</axl>

</SOAP-ENV:Body>

</SOAP-ENV:Envelope>

### Response: Example

The value of "0" for ISexecCLIResponse in the following example shows the response when the request is completed successfully.

<SOAP-ENV:Envelope >

<SOAP-ENV:Body>

<axl >

<response xsi:type="ISexecCLIResponse" >

<ISexecCLIResponse>0</ISexecCLIResponse>

<ISexecCLIError></ISexecCLIError>

</response>

</axl>

</SOAP-ENV:Body>

</SOAP-ENV:Envelope>

The following example shows the response when the request fails. The value of ISexecCLIResponse identifies which line number in the request failed. Any subsequent commands in the list of commands are not executed. All preceding commands in the list were executed.

<SOAP-ENV:Envelope >

<SOAP-ENV:Body>

<axl >

<response xsi:type="ISexecCLIResponse" >

<ISexecCLIResponse>4</ISexecCLIResponse>

<ISexecCLIError> invalid input dn parameter for button 1</ISexecCLIError>

</response>

</axl>

</SOAP-ENV:Body>

</SOAP-ENV:Envelope>

### ISSaveConfig

Use ISSaveConfig to save the running configuration on a router to the startup configuration on the same router.

### Request: Example

<request xsi:type="ISSaveConfig">

<ISSaveConfig></ISSaveConfig>

</request>

### Response: Example

The following example shows that the ISSaveConfig request was successfully completed.

<response xsi:type=" ISSaveConfig">

<ISSaveConfigResult>success</ISSaveConfigResult>

</request>

The following example shows the response when the request fails.

<response xsi:type=" ISSaveConfig">

<ISSaveConfigResult>fail</ISSaveConfigResult>

</request>

The following example shows that response when the request is delayed, typically because there is another terminal session connected to Cisco Unified CME. The running configuration will be saved later by a background process after all other terminal sessions are disconnected.

<response xsi:type=" ISSaveConfig">

<ISSaveConfigResult>delay</ISSaveConfigResult>

</request>

### ISgetGlobal

Use ISgetGlobal to retrieve configuration and status information for the Cisco Unified CME or Cisco Unified SRST system.

### Request: Example

<request xsi:type="ISgetGlobal">

<ISgetGlobal></ISgetGlobal>

</request>

### Response: Example

<response xsi:type="ISgetGlobalResponse">

<ISAddress>10.10.10.1</ISAddress>

<ISMode>ITS</ISMode>

<ISVersion>3.1</ISVersion>

<ISDeviceRegistered>3</ISDeviceRegistered>

<ISPeakDeviceRegistered>3</ISPeakDeviceRegistered>

<ISPeakDeviceRegisteredTime>61392</ISPeakDeviceRegisteredTime>

<ISKeepAliveInterval>30</ISKeepAliveInterval>

<ISConfiguredDevice>100</ISConfiguredDevice>

<ISConfiguredExtension>100</ISConfiguredExtension>

<ISServiceEngine>0.0.0.0</ISServiceEngine>

<ISName>router's host name </ISName>

<ISPortNumber>2000</ISPortNumber>

<ISMaxConference>8</ISMaxConference>

<ISMaxRedirect>5</ISMaxRedirect>

<ISMaxEphone>10</ISMaxEphone>

<ISMaxDN>20</ISMaxDN>

<ISVoiceMail>4089999999</ISVoiceMail>

<ISUrlServices>

<ISUrlType>EPHONE_URL_DIRECTOREIES</ISUrlType>

<ISUrlLink>www.yahoo.com</ISUrlLink>

</ISUrlServices>

</response>

### ISgetDevice

Use ISgetDevice to retrieve configuration and status information for IP phones.

For SCCP Phones

For SCCP phones, use any combination of the following parameters in the request message to specific one or more SCCP phones:

• ISDevID with the ephone tag number of SCCP phone to be queried.

• ISDevName with the MAC address of SCCP phone to be queried.

• ISDevName with one of the following keywords:

– all—All configured SCCP phones.

– allRegistered—All registered SCCP phones.

– allUnregistered—All unregistered SCCP phones.

– allKeyphone—All SCCP phones that are designated as key phones.

– allTag—Ephone tag numbers for all configured SCCP phones.

For SIP Phones

For SIP phones, use any combination of the following parameters in the request message to specify one or more SIP phones:

• ISPoolID with the voice register pool tag number of SIP phone to be queried.

• ISPoolName with one of the following keywords:

– all—All configured voice register pools.

– available—Next available not-configured voice-register-pool tag.

### SCCP Request: Example

<request xsi:type="ISgetDevice">

<ISgetDevice>

<ISDevID>1</ISDevID>

<ISDevName>SEP0012DA8AC43D</ISDevName>

<ISDevName>allKeyphone</ISDevName>

</ISgetDevice>

</request>

### SCCP Response: Example

```
<response xsi:type="ISgetDeviceResponse">
```

```
<ISDevice>
```

```
<ISDevID>1</ISDevID>
```

```
<ISDevName>SEP00036B09538A</ISDevName>
```

```
<ISDevType>IP Phone Telecaster 7960</ISDevType>
```

```
<ISDevUserName>ephone1</ISDevUserName>
```

```
<ISDevLineButton>
```

```
<ISDevLineButtonID>1</ISDevLineButtonID>
```

```
<ISDevLineButtonMode>Normal</ISDevLineButtonMode>
```

```
</ISDevLineButton>
```

```
<ISDevAddr>
```

```
<Xipv4Address>10.10.10.2</Xipv4Address>
```

```
</ISDevAddr>
```

```
<ISPhoneLineList>
```

```
<ExtMapStatus>
```

```
<LineId>1</LineId>
```

```
<ExtId>1</ExtId>
```

```
<ExtNumber>2001</ExtNumber>
```

```
<ExtStatus>true</ExtStatus>
```

```
<LineState>idle</LineState>
```

```
</ExtMapStatus>
```

```
</ISPhoneLineList>
```

```
<ISKeyPhone>false</ISKeyPhone>
```

```
<ISTapiClientAddr>
```

```
<Xipv4Address>0.0.0.0</Xipv4Address>
```

```
</ISTapiClientAddr>
```

```
<ISDevStatus>registered</ISDevStatus>
```

```
<ISDevLastStatus>unregistered</ISDevLastStatus>
```

```
<ISDevChangeTime>54887</ISDevChangeTime>
```

```
<ISDevKeepAlives>21</ISDevKeepAlives>
```

```
<ISDevTapiCStatus></ISDevTapiCStatus>
```

```
<ISDevTapiCLastStatus></ISDevTapiCLastStatus>
```

```
<ISTapiCChangeTime></ISTapiCChangeTime>
```

```
<ISTapiCKeepAlive></ISTapiCKeepAlive>
```

```
<ISDevDND>no</ISDevDND>
```

```
</ISDevice>
```

```
</response>
```

### SIP Request: Example

<request xsi:type="ISgetDevice">

<ISgetDevice>

<ISPoolID>1</ISPoolID>

<ISPoolName>available</ISPoolName>

</ISgetDevice>

</request>

### SIP Response: Example

<response xsi:type="ISgetDeviceResponse" >

<ISDevice>

<ISPoolID>1</ISPoolID>

<ISDevMac>SEPFFFFFFFFFFFF</ISDevMac>

<ISDevSessionServer>1</ISDevSessionServer>

<ISDevAddr>

<Xipv4Address>1.7.120.120</Xipv4Address>

</ISDevAddr>

<ISPhoneLineList>

<ExtMapStatus>

<LineId>1</LineId>

<ExtId>7</ExtId>

<ExtNumber>2777</ExtNumber>

<LineState>idle</LineState>

</ExtMapStatus>

</ISPhoneLineList>

<ISPoolMaxRegistration>42</ISPoolMaxRegistration>

<ISPoolDtmfRelay>rtp-nte</ISPoolDtmfRelay>

<ISDevCodec>g729r8</ISDevCodec>

</ISDevice>

</response>

### ISgetExtension

Use ISgetExtension to retrieve configuration and status information for extension numbers associated with Cisco Unified IP phones.

For SCCP Phones

For SCCP phones, use any combination of the following parameters in the request message to specifiy one or more SCCP phones:

• ISExtID with ephone tag number of SCCP phone to be queried.

• ISExtNumber with directory number of SCCP phone to be queried.

• ISExtNumber with keywords: all; allUp; allDown; allTag

For SIP Phones

For SIP phones, use any combination of the following parameters in the request message to specifiy one or more SIP phones:

• ISVoiceRegDNID with voice register dn tag number of SIP phone to be queried.

• ISVoiceRegDNName with directory number of SIP phone to be queried.

• ISVoiceRegNumber with one of the following keywords:

– all—All configured voice register DNs.

– available—Next available not-configured voice register dn.

### SCCP Request: Example

<request xsi:type="ISgetExtension">

<ISgetExtension>

<ISExtID>1</ISExtID>

<ISExtNumber>2001</ISExtNumber>

<ISExtNumber>allUp</ISExtNumber>

</ISgetExtension>

</request>

### SCCP Response: Example

```
<response xsi:type="ISgetExtensionResponse">
```

```
<ISExtension>
```

```
<ISExtID>1</ISExtID>
```

```
<ISExtNumber>2001</ISExtNumber>
```

```
<ISExtSecNumber>2100</ISExtSecNumber>
```

```
<ISExtType>normal</ISExtType>
```

```
<ISExtStatus>up</ISExtStatus>
```

```
<ISExtChangeTime>53785</ISExtChangeTime>
```

```
<ISExtUsage>0</ISExtUsage>
```

```
<ISExtHomeAddress>0.0.0.0</ISExtHomeAddress>
```

```
<ISExtMultiLines>1</ISExtMultiLines>
```

```
<ISExtPortName>EFXS 50/0/1</ISExtPortName>
```

```
<ISExtLineMode>DUAL_LINE</ISExtLineMode>
```

```
<ISExtCallStatus>IDLE</ISExtCallStatus>
```

```
<ISAllowWatch>true</ISAllowWatch>
```

```
<firstname>Peter</firstName>
```

```
<lastname>Lee</lastName>
```

```
<callForwardAll>1234</callForwardAll>
```

```
<ISSessionServerID>1</ISSessionServerID>
```

```
<ISDevList>
```

```
<ISDeviceID>2</ISDeviceID>
```

```
<ISDeviceID>4</ISDeviceID>
```

```
</ISDevList>
```

```
</ISExtension>
```

```
</response>
```

### SIP Request: Example

<request xsi:type="ISgetExtension">

<ISgetExtension>

<ISVoiceRegDNID>1</ISVoiceRegDNID>

<ISVoiceRegNumber>2777</ISVoiceRegNumber>

<ISVoiceRegDNName>available</ISVoiceRegDNName>

</ISgetExtension>

</request>

### SIP Response: Example

<response xsi:type="ISgetExtensionResponse" >

<ISExtension>

<ISVoiceRegDNID>1</ISVoiceRegDNID>

<ISExtNumber>2777</ISExtNumber>

<ISDevSessionServer>1</ISDevSessionServer>

<ISAllowWatch>true</ISAllowWatch>

```
<firstname>Peter</firstName>
```

```
<lastname>Lee</lastName>
```

<ISDevList>

<ISPoolID>7</ISPoolID>

</ISDevList>

</ISExtension>

</response>

### ISsetKeyPhones

Use ISsetKeyPhones to desiginate a list of MAC address of SCCP phones as key-system phones in Cisco Unified CME.

### Request: Example

<request xsi:type="ISsetKeyPhones">

<ISsetKeyPhones>

<ISPhoneName>SEP000000000000</ISPhoneName>

<ISPhoneName>SEP000DEDAB3566</ISPhoneName>

</ISsetKeyPhones>

</request>

### Response

The following example shows that the first phone in the previous example failed to be designated as a key-system phone and that the request for the 2nd phone in the example was completed successfully.

<response xsi:type="ISsetKeyPhonesResponse">

<ISsetResult>false</ISsetResult>

<ISsetResult>true</ISsetResult>

</response>

### ISunsetKeyPhones

Use ISunsetKeyPhones to remove the key phone designation for a list of MAC address of SCCP phones in Cisco Unified CME.

### Request: Example

```
<request xsi:type="ISunsetKeyPhones">
```

```
<ISunsetKeyPhones>
```

```
<ISPhoneName>SEP000DEDAB3566</ISPhoneName>
```

```
</ISunsetKeyPhones>
```

```
</request>
```

### Response: Example

If the request is successful, the value for ISunsetResult is "true." If the request fails, the value is "false."

<response xsi:type="ISunsetKeyPhonesResponse">

<ISunsetResult>true</ISunsetResult>

</response>

### ISgetEvtCounts

Use ISgetEvtCounts to display the total number events for devices and directory numbers associated with phones connected to the router.

The response includes the following parameters:

• ISDevEvtCount with a number for total device events.

• ISExtEvtCount with number for total extension events.

### Request: Example

<request xsi:type="ISgetEvtCounts">

<ISgetEvtCounts></ISgetEvtCounts>

</request>

### Response: Example

<response xsi:type="ISgetEvtCountsResponse">

<ISDevEvtCount>12</ISDevEvtCount>

<ISExtEvtCount>288</ISExtEvtCount>

</response>

### ISgetDevEvts

Use ISgetDevEvts to display the event history details for a phone. Use any combination of the following parameters in the request message to specifiy one or more phone events:

• ISDevEvtID with the index number of the event.

• ISDevID with the ephone tag number of the phone.

• ISDevName with one of the following:

– The MAC address of the phone.

– The keyword "all" to display all the events associated with the phone.

### Request: Example

<request xsi:type="ISgetDevEvts">

<ISgetDevEvts>

<ISDevEvtID>11</ISDevEvtID>

<ISDevID>2</ISDevID>

<IDDevName>SEP000DEDAB3566</ISDevName>

<IDDevName>all</ISDevName>

</ISgetDevEvts>

</request>

### Response: Example

<response xsi:type="ISgetDevEvtsResponse">

<ISDevEvent>

<ISDevID>1</ISDevID>

<ISDevName>SEP000DEDAB3566</ISDevName>

<ISDevEventTime>1504</ISDevEventTime>

<ISDevEventType>Device</ISDevEventType>

<ISDevStatus>unregistered</ISDevStatus>

</ISDevEvent>

<ISDevEvent>

<ISDevID>1</ISDevID>

<ISDevName>SEP000DEDAB3566</ISDevName>

<ISDevEventTime>5837</ISDevEventTime>

<ISDevEventType>Device</ISDevEventType>

<ISDevStatus>registered</ISDevStatus>

</ISDevEvent>

</response>

### ISgetExtEvts

Use ISgetExtEvts to display the event history details for an extension number. Use any combination of the following parameters in the request message to specifiy one or more extension events:

• ISExtEvtID with the index number of the event.

• ISExtID with the ephone-dn tag number.

• ISExtNumber with one of the following:

– A directory number associated with an ephone-dn.

– The keyword "all" to display all the events associated with the directory number.

### Request: Example

<request xsi:type="ISgetExtEvts">

<ISgetExtEvts>

<ISExtEvtID>170</ISExtEvtID>

<ISExtID>80</ISExtID>

<ISExtNumber>2080</ISExtNumber>

<ISExtNumber>all</ISExtNumber>

</ISgetExtEvts>

</request>

### Response: Example

<response xsi:type="ISgetExtEvtsResponse">

<ISExtEvent>

<ISextID>80</ISextID>

<ISextNumber>2080</ISextNumber>

<ISExtEventTime>90355</ISExtEventTime>

<ISExtStatusChangeEvent>Down</ISExtStatusChangeEvent>

</ISExtEvent>

</response>

### ISgetUser

Use ISgetUser to retrieve information for a particular user in Cisco Unified CME. The request must include the ISuserID parameter with a user name that is configured in Cisco Unified CME.

### Request: Example

<request xsi:type="ISgetUser">

<ISgetUser>

<ISuserID>peter</ISuserID>

</ISgetUser>

</request>

### Response: Example

If the request contains a valid ISuserID, the response includes the user-name tag number (ISuserTag) and type for this user.

The value for ISuserType corresponds to how a username is configured in Cisco Unified CME, as follows:

• 0—INVALID_CME_USER

• 1—EPHONE_USER

• 2—LOGOUT_PROFILE_USER

• 3—USER_PROFILE_USER

If the request contains an invalid ISuserID, the value for ISuserTag and ISuserType will both be "0."

The following example shows that the username "peter" with the user-name tag #6 is configured as an ephone-user.

<response xsi:type="ISgetUserResponse" >

<ISuser>

<ISuserID>peter</ISuserID>

<ISuserType>1</ISuserType>

<ISuserTag>6</ISuserTag>

</ISuser>

</response>

### ISupdateUser

Use ISupdateUser to change the password for a valid username in Cisco Unified CME. The request must include the following parameters:

• IsuserID with a user name that is configured in Cisco Unified CME.

• ISpassword with a string of alphanumeric characters to be configured as the new password for the username.

### Request: Example

<request xsi:type="ISupdateUser">

<ISupdateUser>

<ISuserID>peter</ISuserID>

<ISpassword>abc</ISpassword>

</ISupdateUser>

</request>

### Response: Example

If the user information is updated successfully, then the value for ISsetResult is "true."

<response xsi:type="ISupdateUserResponse" >

<ISsetResult>true</ISsetResult>

</response>

If the request fails, the value is "false" and the failure reason is specified in ISsetError.

<response xsi:type="ISupdateUserResponse" >

<ISsetResult>false</ISsetResult>

<ISsetError>User peter does not exist</ISsetError>

</response>

### ISgetVoiceRegGlobal

Use ISgetVoiceRegGlobal to retrieve information for a Cisco Unified CME SIP system.

### Request: Example

<request xsi:type="ISgetVoiceRegGlobal">

<ISgetVoiceRegGlobal></ISgetVoiceRegGlobal>

</request>

### Response: Example

<response xsi:type="ISgetVoiceRegGlobalResponse" >

<ISAddress>1.7.120.103</ISAddress>

<ISMode>cme</ISMode>

<ISVersion>4.0(0)</ISVersion>

<ISServiceEngine>1.7.120.103</ISServiceEngine>

<ISAuthMode>all</ISAuthMode>

<ISPortNumber>5060</ISPortNumber>

<ISMaxPool>10</ISMaxPool>

<ISMaxDN>10</ISMaxDN>

<ISMaxRedirect>5</ISMaxRedirect>

</response>

### ISgetSessionServer

Use ISgetSessionServer to retrieve configuration information for session servers in Cisco Unified CME. Use any combination of the following parameters in the request message to specifiy one or more session servers:

• ISSessionServerID with the session server tag number.

• ISSessionserverName with one of the following keywords:

– all—All configured session servers

– available—Next available session server tag number to be configured.

### Request: Example

<request xsi:type="ISgetSessionServer">

<ISgetSessionServer>

<ISSessionServerID>1</ISSessionServerID>

<ISSessionServerID>2</ISSessionServerID>

<ISSessionServerName>available</ISSessionServerName>

</ISgetExtension>

</request>

### Response: Example

<response xsi:type="ISgetSessionServerResponse" >

<ISSessionServer>

<ISSessionServerID>1</ISSessionServerID>

<ISSessionRegisterID>CRS</ISSessionRegisterID>

<ISSessionKeepAlives>60</ISSessionKeepAlives>

</ISSessionServer>

### ISgetPresenceGlobal

Use ISgetPresenceGlobal to retrieve configuration information and status for the presence engine in Cisco Unified CME.

### Request: Example:

<request xsi:type="ISgetPresenceGlobal">

<ISgetPresenceGlobal></ISgetPresenceGlobal>

</request>

### Response: Example

<response xsi:type="ISgetPresenceGlobalResponse" >

<ISPresenceEnable>false</ISPresenceEnable>

<ISMode>cme</ISMode>

<ISAllowSub>false</ISAllowSub>

<ISAllowWatch>false</ISAllowWatch>

<ISMaxSubAllow>100</ISMaxSubAllow>

<ISSipUaPresenceStatus>false</ISSipUaPresenceStatus>

</response>

## Additional References

The following sections provide references related to the XML interface to Cisco Unified CME and Cisco Unified SRST.

### Related Documents

Related Topic

Document Title

Cisco Unified CME

• Cisco Unified Communications Express

Cisco Unified SRST

• Cisco Unified Survivable Remote Site Telephony

Microsoft Telephony Applications Program Interfaces (TAPI)

• Microsoft Windows TAPI

• Microsoft Telephony

• TAPI Quickstart

### Technical Assistance

Description

Link

The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving technical issues with Cisco products and technologies.

To receive security and technical information about your products, you can subscribe to various services, such as the Product Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds.

Access to most tools on the Cisco Support website requires a Cisco.com user ID and password.

http://www.cisco.com/techsupport

### CCDE, CCENT, Cisco Eos, Cisco Lumin, Cisco Nexus, Cisco StadiumVision, Cisco TelePresence, the Cisco logo, DCE, and Welcome to the Human Network are trademarks; Changing the Way We Work, Live, Play, and Learn and Cisco Store are service marks; and Access Registrar, Aironet, AsyncOS, Bringing the Meeting To You, Catalyst, CCDA, CCDP, CCIE, CCIP, CCNA, CCNP, CCSP, CCVP, Cisco, the Cisco Certified Internetwork Expert logo, Cisco IOS, Cisco Press, Cisco Systems, Cisco Systems Capital, the Cisco Systems logo, Cisco Unity, Collaboration Without Limitation, EtherFast, EtherSwitch, Event Center, Fast Step, Follow Me Browsing, FormShare, GigaDrive, HomeLink, Internet Quotient, IOS, iPhone, iQ Expertise, the iQ logo, iQ Net Readiness Scorecard, iQuick Study, IronPort, the IronPort logo, LightStream, Linksys, MediaTone, MeetingPlace, MeetingPlace Chime Sound, MGX, Networkers, Networking Academy, Network Registrar, PCNow, PIX, PowerPanels, ProConnect, ScriptShare, SenderBase, SMARTnet, Spectrum Expert, StackWise, The Fastest Way to Increase Your Internet Quotient, TransPath, WebEx, and the WebEx logo are registered trademarks of Cisco Systems, Inc. and/or its affiliates in the United States and certain other countries.

### All other trademarks mentioned in this document or Website are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (0807R)

### Any Internet Protocol (IP) addresses used in this document are not intended to be actual addresses. Any examples, command display output, and figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses in illustrative content is unintentional and coincidental. © 2003-2008 Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- Unified Communications Manager Express

| Description | Request | Parameter | Response |
|---|---|---|---|
| System |
| Execute configuration commands. | ISexecCLI | command | ISexecCLIResponse |
| Save router configuration to nvram. | ISSaveConfig | — | ISSaveConfigResult |
| SCCP |
| Get system status for Cisco Unified CME or Cisco Unified SRST. | ISgetGlobal | — | ISgetGlobalResponse |
| Get status of an IP phone. | ISgetDevice | Any combination of the following: ISDevID ISDevName | ISgetDeviceResponse |
| Get status of an extension associated with an IP phone. | ISgetExtension | Any combination of the following: ISExtID ISExtNumber | ISgetExtensionResponse |
| Set key phones | ISsetKeyPhones | ISPhoneName | ISsetKeyPhonesResponse |
| Remove key phone configuration. | ISunsetKeyPhones | ISPhoneName | ISunsetKeyPhonesResponse |
| Get total event counts. | ISgetEvtCounts | — | ISgetEvtCountsResponse |
| Get device event history | ISgetDevEvts | Any combination of the following: ISDevID ISDevName ISDevEvtID | ISgetDevEvtsResponse |
| Get extension event history | ISgetExtEvts | Any combination of the following: ISExtID ISExtNumber ISExtEvtID | ISgetExtEvtsResponse |
| Get user information | ISgetUser | ISuserID | ISgetUserResponse |
| Set user information | ISupdateUser | ISuserID and ISpassword | ISupdateUserResult |
| SIP |
| Get system status for a Cisco Unified CME running SIP. | ISgetVoiceRegGlobal | — | ISgetVoiceRegGlobalResponse |
| Get status of an IP phone. | ISgetDevice | Any combination of the following: ISPoolID ISPoolName | ISgetDeviceResponse |
| Get status of an extension associated with an IP phone. | ISgetExtension | Any combination of the following: ISVoiceRegDNID ISVoiceRegDNName ISVoiceRegNumber | ISgetExtensionResponse |
| Get status of a session server. | ISgetSessionServer | Any combination of the following: ISSessionServerID ISSessionServerName | ISgetSessionServerResponse |
| Get configuration for Presence. | ISgetPresenceGlobal | — | ISgetPresenceGlobalResponse |

| Related Topic | Document Title |
|---|---|
| Cisco Unified CME | • Cisco Unified Communications Express |
| Cisco Unified SRST | • Cisco Unified Survivable Remote Site Telephony |
| Microsoft Telephony Applications Program Interfaces (TAPI) | • Microsoft Windows TAPI • Microsoft Telephony • TAPI Quickstart |

| Description | Link |
|---|---|
| The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving technical issues with Cisco products and technologies. To receive security and technical information about your products, you can subscribe to various services, such as the Product Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds. Access to most tools on the Cisco Support website requires a Cisco.com user ID and password. | http://www.cisco.com/techsupport |