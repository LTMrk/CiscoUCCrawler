---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-211297-configure-op-e7eaf84345
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/211297-Configure-Opus-Support-on-Cisco-Unified.html
retrieved_at: 2026-08-21T13:56:11.783966+00:00
---

Configure Opus Support on Cisco Unified Communication Manager

# Configure Opus Support on Cisco Unified Communication Manager

### Download Options

Updated: May 25, 2017

Document ID: 211297

Contents

## Contents

## Introduction

This Document describes the Configuration to Enable Opus codec support that was added as part of Cisco Unified Communications Manager Release 11.0(1) and the list of Devices that support Opus.

Contributed by Akash Sethi Cisco TAC Engineer.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unfied Communication Manager.

- Voice over Internet Protocol (VoIP)

### Components Used

The information in this document is based on these software versions:

- Cisco Unified Communications Manager ( CUCM) version 11 and above.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## What is Opus?

Opus codec is an interactive speech and audio codec that is, designed to handle a wide range of interactive audio applications such as VoIP, video conferencing, in-game chat, and live distributed music performance.

The Opus codec scales from 6 kbit/s narrowband mono speech to 510 kbit/s fullband stereo music. It can seamlessly switch between all of its various operating modes, giving it a great deal of flexibility to adapt to varying content and network conditions without renegotiating the current session.

Opus is supported for SIP devices. The Opus codec service parameter Opus Codec Enabled is set to Enabled for All Devices by default. The Other Possible values for this parameter can be enable Opus codec for all non-recording devices or Disabled for all the devices.

### Cisco Devices that Support OPUS

Device

Protocol

Minimum Firmware Requirement

7811/78221/7841/7861

SIP

78xx.11-5-1-18

8865/8845

SIP

8845_65-sip.11-5-1-18

8841/8841/8851/8861

SIP

88xx-sip.11-5-1-18

Cisco Jabber

SIP

11.0

## Configuration to enable Opus.

- Enable the Service Parameter for Opus Codec

- Enable the Enterprise parameter for Advertise G.722 Codec

Step 1. In order to enable OPUS Support Login to Cisco Unified CM Administration Page, Navigate to System > Service parameters .

Step 2 . From the Drop-down Menu Choose the Server as your Call Manager and service as Call Manager Service.

Step 3. Search for Opus Codec Enabled Parameter and set it to Enabled for All Devices to enable the Opus for all devices. Save the Configuration.

Note : All devices does not mean that the Codec would be enabled for all devices that are registered on CUCM. It would be enabled for All the Devices that Support Opus. Not All the Cisco Devices Support Opus. For list of Devices that Support OPUS please see “Cisco Devices that Support OPUS” Section.

Step 4 . Navigate to System > Enterprise Parameter on Cisco Unified CM Administration Page.

Step 5 . Enable Advertise G.722 Codec Parameter.

Note : If the Advertise G.722 Codec Parameter is set to Disabled, Devices would not use OPUS even if the OPUS Codec enabled parameter under service parameter is set to Enabled.

After the Changes have been made you would need to Click on “Apply Config” and “Reset” buttons for Changes to take effect.

Note : A Reset Command for Enterprise parameter would reset all the Devices registered to the CUCM.

### Defects associated

- CSCva48193

### Contributed by Cisco Engineers

Akash Sethi

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

| Device | Protocol | Minimum Firmware Requirement |
|---|---|---|
| 7811/78221/7841/7861 | SIP | 78xx.11-5-1-18 |
| 8865/8845 | SIP | 8845_65-sip.11-5-1-18 |
| 8841/8841/8851/8861 | SIP | 88xx-sip.11-5-1-18 |
| Cisco Jabber | SIP | 11.0 |