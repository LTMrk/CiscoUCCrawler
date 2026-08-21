---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-windows-200120-troubleshoot-call-decline-issues-in-jabb-bedae0ca2a
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber-windows/200120-Troubleshoot-Call-Decline-Issues-in-Jabb.html
retrieved_at: 2026-08-21T06:59:49.954170+00:00
---

Troubleshoot Call Decline Issues in Jabber for Windows

# Troubleshoot Call Decline Issues in Jabber for Windows

### Download Options

Updated: September 12, 2018

Document ID: 200120

Contents

## Contents

## Introduction

This document describes the common issues you might experience with the decline option on an incoming call in Cisco Jabber for Microsoft Windows.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communication Manager (CUCM)

- Cisco Jabber for Windows

### Components Used

The information in this document is based on these software versions:

- CUCM 8.x or later

- Cisco Jabber for Windows 9.x and 10.x

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

The Decline button redirects the call to the Voicemail Pilot number configured for the directory number. The Voicemail profile is configured at the Directory Number (DN) level of the device. If the user has a Voicemail profile configured in Unity Connection, it plays the user-specific prompt, otherwise it plays the default voice mail prompt.

## Problem 1: No Decline Button on Incoming Call

This image illustrates an issue in which the Decline button does not appear on an incoming call:

## Solution

This issue can occur when there is no Voicemail profile assigned on the line configuration of the device.

Ensure that the user's Client Services Framework (CSF) line configuration has a Voicemail profile configured in order to get the Decline button displayed on the incoming call. As shown in this image, select Voice Mail Profile from the drop-down list:

## Problem 2: Call is Not Sent to Voice Mail when Decline Button is Clicked

This image illustrates an issue in which the Decline button appears on an incoming call:

The Decline button appears for an incoming call; however, when it is clicked, the call is not sent to voice mail, and the caller continues to hear the ring back.

## Solution

For incoming calls from an internal DN, ensure that the Calling Search Space (CSS) of the calling number has the Voicemail Pilot Partition.

For incoming calls from the service provider, the CSS of the Gateway or the Trunk must have the partition of the Voicemail Pilot as illustrated in the image.

Also, CSS assigned on the Call Forward setting of the line configuration must include required Voicemail Partition added.

Note : The incoming call cannot be completely dropped or disconnected when the Decline button is clicked. The Decline button only redirects the call to the configured voice mail pilot number.

If there is no voice mail server, you can configure a dummy voice mail profile and pilot number in order to display the Decline button; however, nothing will happen when the Decline button is clicked.

In order to ensure that the feature works properly, configure a voice mail profile in Cisco Unity Connection.

## Related Information

- Cisco Unified Communications Manager Administration Guide, Release 10.0(1)

- Cisco Jabber 10.6 Deployment and Installation Guide

- Technical Support & Documentation - Cisco Systems

### Contributed by Cisco Engineers

Nagajothi Thangapandian

Cisco TAC Engineer

### This Document Applies to These Products

- Jabber for Windows