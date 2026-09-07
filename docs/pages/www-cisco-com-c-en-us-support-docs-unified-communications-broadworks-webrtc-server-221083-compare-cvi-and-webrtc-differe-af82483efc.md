---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-webrtc-server-221083-compare-cvi-and-webrtc-differe-af82483efc
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks-webrtc-server/221083-compare-cvi-and-webrtc-differences-and.html
retrieved_at: 2026-09-07T13:01:59.494422+00:00
---

Compare CVI and WebRTC (Differences and Configuring)

# Compare CVI and WebRTC (Differences and Configuring)

### Download Options

Updated: October 11, 2023

Document ID: 221083

Contents

## Contents

## Introduction

This document describes the differences between CVI and WebRTC.

## Background Information

CVI -The Cisco Webex Video Integration for Microsoft Teams(VIMT)

offers users a seamless experience to join Microsoft Teams meetings from Cisco or any SIP capable video device registered either in the cloud or on-premises.

WebRTC

An open source communication technology for mobile and desktop platforms. Built on APIs that require no plugins, and, is supported by all major web browsers and operating systems.

It is common for apps that use WebRTC to be browser-based

WebRTC is typically used in real-time audio and video communications.  Commonly used in browser-based apps for person-to-person communication

handles all the details of directly connecting two devices and transmitting the audio and video data in real-time  using several standards and protocols.

### CVI

This was created because Microsoft  teams is a closed solution.

Only Microsoft clients can join Microsoft meetings. So Microsoft made CVI (Cloud Video Interops)

VIMT is  Cisco partnering with Microsoft Teams to to make solution:

### WebRTC

When you start a WebRTC call your app must establish a connection with other devices that connect to the call.

Before that can happen WebRTC app must go through firewalls and NAT. Because your PC only knows your private address so the WebRTC app contact the STUN Server to retrieve your public facing IP address.

Next WebRTC app retrieves the public facing IP from other devices connected to the call as well. Once the app knows all the necessary IP addresses it builds a list of potential connection configurations called ICE (Interactive Connectivity Establishment ) candidates selects the most efficient configuration.

Next WebRTC app opens a private data channel where all the devices on the WebRTC call can exchange audio and video data in real time. This is a private connection and can not be accessed by anyone on the call.

If a direct connection can not be established then WebRTC app uses a TURN(Traversal Using Relays Around NAT)  server.

The TURN server acts as a repeater. If a direct connection cannot be established between the device on a WebRTC call, the app then has computers send audio and video data to the TURN server, which transmits the data to the receiving device and reverse. Using a TURN server for WebRTC communication is a last resort.

In addition supporting technologies are used to navigate the complex system of ports, protocols, and networks between the devices on a WebRTC call. APIs are used to access cameras and microphones and gather the audio and visual data.

### Who Can Use?

In Commercial Sites -

- CVI and WebRTC is supported in commercial

- We are working on better features for WebRTC such as join via meeting number

In Fedramp Sites -

- CVI works in Fedramp but its not supported

- We do not support CVI calls in our Fedramp environment as it provides choppy audio during VIMT calls if you are able to configure a connection.

- We support WebRTC to join Microsoft Teams meetings. (not GCC- high)

## Configure

### Setup CVI

This requires Full Admin Privileges for the Webex Org and not Partner Admin; Access to account with Microsoft tenant Global Admin Privileges; Subdomain added to the Webex org.

Ensure Webex Video Integration for Microsoft Teams License are displayed within Subscription Panel in Control Hub, Within the organization along with licenses from a subscription. You can also locate the organization license state of Licensed Org Card, Existing Setup Org Card or Unlicensed Org Card in Control Hub under Hybrid Services.

### VIMT Deployment

View Prerequisites link that display documentation for deployment and a checklist. Select Authorize to be prompted for login by a Microsoft login prompt. There is a prompt to login with the O365 Global Administrator account and Accept the Permissions requested. Paste into PowerShell the two configurations provided. The first configuration line provided by the Setup Page within Control Hub; this configures. The Second Configuration line provides the "global flag" that enables the feature for all Microsoft Teams users in the Org.

Cisco Webex Video integration is now be included as an Enterprise Application within Azure Active Directory Admin Center.

### Setup WebRTC

Enable Hybrid Calendar -

Enable Microsoft Teams under Meeting providers in Devices -> Settings.

Ensure web engine is enabled on the device ( Devices => Settings => WebRTC Support ).

### Revision History

1.0

11-Oct-2023

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 11-Oct-2023 | Initial Release |