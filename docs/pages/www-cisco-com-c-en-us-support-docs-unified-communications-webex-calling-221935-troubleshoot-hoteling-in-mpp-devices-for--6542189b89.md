---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-webex-calling-221935-troubleshoot-hoteling-in-mpp-devices-for--6542189b89
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/webex-calling/221935-troubleshoot-hoteling-in-mpp-devices-for.html
retrieved_at: 2026-08-21T07:16:35.925176+00:00
---

Troubleshoot Hoteling in MPP Devices for Webex Calling

# Troubleshoot Hoteling in MPP Devices for Webex Calling

### Download Options

Updated: April 23, 2024

Document ID: 221935

Contents

## Contents

## Introduction

This document describes the most common issues encountered with Hoteling in MPP devices for Webex calling and how to troubleshoot them.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Webex Calling

- Control Hub

- Hoteling feature

- MPP devices PRT

### Components Used

This document is not restricted to specific hardware and software version. The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

Hoteling is a Calling feature enables a user's calling profile information such as, number, features and calling plan, to be temporarily loaded into another phone to be accessible from it.

## Common Configuration Issues

### Ensure Voice Portal is Set for the Location

Step 1. Click the Location for the users facing the issue.

Step 2. Click Calling .

Step 3. In Calling features settings , click Voice Portal .

Step 4. In Incoming Call , add a Phone Number available from the drop-down menu in the Location or an Extension or both.

Step 5. Click Save .

### Ensure that the Host Device is Set as a Hoteling Host

Step 1. Under MANAGEMENT , click Devices and click the device to be set as Hoteling Host.

Step 2. Under Overview > Hoteling enable the Toggle Allow this device to be used as a Hoteling Host by visiting guests .

Allow This Device to be Used as a Hoteling Host by Visiting Guests

Step 3. Power reset the device.

Step 4. The Guest In softkey must appear in Host device display.

### Sign-In Failed Issues

If a Sing-In Failed prompts after an attempt of authentication for Guest In, follow these troubleshooting steps:

#### Obtainment and Basic Analysis of the PRT from the Device

Step 1. Set the Default Logging Level to Debugging for the device.

Step 2. Enable the MPP Web Access (User) toggle.

Step 3. Power reset the device.

Step 4. Reproduce the Sing-In issue.

Step 5. Access the device GUI though a web browser.

Step 6. Click Info > Debug Info > Generate PRT .

Step 7. Click the file generated to download it.

In the PRT you can find the SIP SUBSCRIBE and NOTIFY the device uses for Hoteling.

The device sends a SUBSCRIBE e.g:

```
SUBSCRIBE sip:2X.8X.X.1XX:89XX;transport=tls SIP/2.0^M
	Via: SIP/2.0/TLS 1XX.1XX.X.1XX:50XX;branch=z9hG4bK-5c65a186^M
	From: <sip:dckvbcsohk@9044XXXX.cisco-bcld.com>;tag=316c637a772774e7^M
	To: <sip:dckvbcsohk@9044XXXX.cisco-bcld.com>;tag=394818446-1712859294626^M
	Call-ID: ae75b30c-16372ea@1XX.1XX.X.1XX^M
	CSeq: 20314 SUBSCRIBE^M
	Max-Forwards: 70^M
	Authorization: Digest username="+121035XXXX",realm="BroadWorks",nonce="BroadWorksXluvk76avT78ohryBW",uri="sip:2X.8X.1.1XX:89XX",algorithm=MD5,response="b3618fa6023a0594dfde6acf406eb93a",qop=auth,nc=00000002,cnonce="da2a8978"^M
	Contact: <sip:dckvbcsohk@1XX.1XX.X.1XX:50XX;transport=tls>^M
	Accept: application/x-broadworks-hoteling+xml^M
	Expires: 3600^M
	Event: x-broadworks-hoteling^M
	User-Agent: Cisco-CP-8865-3PCC/12.0.3_dcf719f39350_d4e6994b-60bc-4fba-a490-fe5f8e74ceea_dcf719f3-9350-4fba-a490-fe5f8e74ceea^M
	Session-ID: 4e85b7ad00105000a000dcf719f39350;remote=1abed7e0008042159d92c35291039b58^M
	Content-Length: 152^M
	Content-Type: applicati
	NOT Apr 11 18:16:44.288201 (1745-1842) voice-on/x-broadworks-hoteling+xml^M
	^M
	<?xml version="1.0" encoding="ISO-8859-1"?>
	<SetHoteling xmlns="http://schema.broadsoft.com/hoteling">
	  <guestAddress>Guest Extension</guestAddress>
</SetHoteling>
```

In response to the SUBSCRIBE , a 200 OK is sent:

```
SIP/2.0 200 OK^M
Via:SIP/2.0/TLS 1xx.1xx.x.1xx:5061;received=2xx.2xx.2xx.4x;branch=z9hG4bK-5c65a186^M
From:<sip:dckvbcsohk@9044xxxx.cisco-bcld.com>;tag=316c637a772774e7^M
To:<sip:dckvbcsohk@9044xxxx.cisco-bcld.com>;tag=394818446-1712859294626^M
Call-ID:ae75b30c-16372ea@1xx.1xx.x.1xx^M
CSeq:20314 SUBSCRIBE^M
Session-ID:1abed7e0008042159d92c35291039b58;remote=4e85b7ad00105000a000dcf719f39350^M
Expires:3424^M
Contact:<sip:2x.8x.x.1xx:89xx;transport=tls>^M
Content-Length:0^M
^M
```

The Webex Calling cloud sends a NOTIFY :

In this NOTIFY example the <guestAddress/> does not contains the Guest Extension which is the result of the Sing-In failed attempt.

```
NOTIFY sip:dckvbcsohk@1XX.1XX.X.1XX:50XX;transport=tls SIP/2.0^M
	Via:SIP/2.0/TLS 2X.8X.X.1XX:89XX;branch=z9hG4bKBroadworksSSE.-2XX.2XX.2XX.4XV5061-0-101-394818446-1712859294626^M
	From:<sip:dckvbcsohk@9044xxxx.cisco-bcld.com>;tag=394818446-1712859294626^M
	To:<sip:dckvbcsohk@9044xxxx.cisco-bcld.com>;tag=316c637a772774e7^M
	Call-ID:ae75b30c-16372ea@1XX.1XX.X.1XX^M
	CSeq:101 NOTIFY^M
	Contact:<sip:2X.8X.X.1XX:89XX;transport=tls>^M
	Subscription-State:active;expires=3424^M
	Max-Forwards:69^M
	Session-ID:1abed7e0008042159d92c35291039b58;remote=4e85b7ad00105000a000dcf719f39350^M
	Event:x-broadworks-hoteling^M
	Content-Type:application/x-broadworks-hoteling+xml^M
	Content-Length:134^M
	^M
	<?xml version="1.0" encoding="UTF-8"?>
	<HotelingEvent xmlns="http://schema.broadsoft.com/hoteling">
	<guestAddress/>
	</HotelingEvent>^M
```

In response to the NOTIFY, a 200 OK is sent:

```
SIP/2.0 200 OK^M
To:<sip:dckvbcsohk@9044xxxx.cisco-bcld.com>;tag=316c637a772774e7^M
From:<sip:dckvbcsohk@9044xxxx.cisco-bcld.com>;tag=394818446-1712859294626^M
Call-ID:ae75b30c-16372ea@1xx.1xx.x.1xx^M
CSeq:101 NOTIFY^M
Via:SIP/2.0/TLS 2x.8x.x.1xx:89xx;branch=z9hG4bKBroadworksSSE.-2xx.2xx.2xx.4xV5061-0-101-394818446-1712859294626^M
Server: Cisco-CP-8865-3PCC/12.0.3_dcf719f39350^M
Session-ID: dbb009eb00105000a000dcf719f39350;remote=1abed7e0008042159d92c35291039b58^M
Content-Length: 0^M
^M
```

### Ensure that the Voicemail PIN is Correct

In case a new Voicemail PIN is needed:

Step 1. Log in with the User credentials in User Hub .

Step 2. Click Settings > Calling > Voicemail .

Step 3. Click Voicemail PIN > Reset voicemail PIN .

Step 4. Enter a new Voicemail PIN that meets the requirements.

Step 5. Click Save .

### Ensure Hoteling is Enabled for the Guest

Step 1. Under MANAGEMENT > Users, click the Hoteling guest user.

Step 2. Click Calling > Between-user permissions > Hoteling .

Between-User Permissions

Step 3. Click the toggle Allow this user to connect to a Hoteling host device .

Hoteling Toggle

Step 4. Select a Limit Association Period .

Step 5. Click Save .

### Successful NOTIFY for Hoteling SUBSCRIBE from Webex Calling Cloud

The successful NOTIFY shows the Guest Extension and Subscription expiration Time.

```
NOTIFY sip:dckvbcsohk@1xx.1xx.x.1xx:50xx;transport=tls SIP/2.0^M
		Via:SIP/2.0/TLS 2x.8x.x.1xx:89xx;branch=z9hG4bKBroadworksSSE.-2xx.2xx.2xx.4xV5061-0-103-394818446-1712859294626^M
		From:<sip:dckvbcsohk@9044xxxx.cisco-bcld.com>;tag=394818446-1712859294626^M
		To:<sip:dckvbcsohk@9044xxxx.cisco-bcld.com>;tag=316c637a772774e7^M
		Call-ID:ae75b30c-16372ea@1xx.1x.x.1xx^M
		CSeq:103 NOTIFY^M
		Contact:<sip:2x.8x.x.1xx:89xx;transport=tls>^M
		Subscription-State:active;expires=3324^M
		Max-Forwards:69^M
		Session-ID:1abed7e0008042159d92c35291039b58;remote=4e85b7ad00105000a000dcf719f39350^M
		Event:x-broadworks-hoteling^M
		Content-Type:application/x-broadworks-hoteling+xml^M
		Content-Length:176^M
		^M
		<?xml version="1.0" encoding="UTF-8"?>
		<HotelingEvent xmlns="http://schema.broadsoft.com/hoteling">
		<guestAddress>Guest Extension</guestAddress>
		<expires>Subscription Time</expires>
		</HotelingEvent>^M
```

In response to the NOTIFY , a 200 OK is sent:

```
SIP/2.0 200 OK^M
To:<sip:dckvbcsohk@9044xxxx.cisco-bcld.com>;tag=316c637a772774e7^M
From:<sip:dckvbcsohk@9044xxxx.cisco-bcld.com>;tag=394818446-1712859294626^M
Call-ID:ae75b30c-16372ea@1xx.1xx.x.1xx^M
CSeq:102 NOTIFY^M
Via:SIP/2.0/TLS 2x.8x.x.1xx:89xx;branch=z9hG4bKBroadworksSSE.-2xx.2xx.2xx.4xV5061-0-102-394818446-1712859294626^M
Server: Cisco-CP-8865-3PCC/12.0.3_dcf719f39350^M
Session-ID: 7e64aa9c00105000a000dcf719f39350;remote=1abed7e0008042159d92c35291039b58^M
Content-Length: 0^M
^M
```

## Recommended Information for a TAC Case

If an issue persists after the troubleshooting steps in this document have been performed and a TAC case is needed, Cisco recommends to include this information:

- Organization ID

- Location ID or Location Name

- Host User's Number, extension and mail

- Guest User's Number, extension and mail

- Time zone and Timestamp of the Sing-In attempt

- A detailed description of the issue experienced.

- Attach the PRT obtained file from the device.

## Related Inform atio n

Hoteling in Control Hub

### Revision History

1.0

24-Apr-2024

Initial Release

### Contributed by Cisco Engineers

Roberto Alvarez

Technical Consulting Engineer

### This Document Applies to These Products

- Webex Calling

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 24-Apr-2024 | Initial Release |