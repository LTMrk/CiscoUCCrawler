---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-customer-voice-portal-901-200266-configure-fetch-audio-79835cca39
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-customer-voice-portal-901/200266-Configure-Fetch-Audio-Feature-to-Reduce.html
retrieved_at: 2026-08-21T13:21:44.500902+00:00
---

Configure Fetch Audio Feature to Reduce the Impact of Network Latency

# Configure Fetch Audio Feature to Reduce the Impact of Network Latency

### Download Options

Updated: July 17, 2016

Document ID: 200266

Contents

## Contents

## Introduction

This document describes how to configure Fetch Audio feature to reduce the impact of network latency, which is expected to be much less than 200 ms round trip when it is between Cisco Unified Customer Voice Portal (CVP) server and VoiceXML (VXML) gateway.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- CVP Server

- VXML Gateway

- Cisco Unified Intelligent Contact Management (ICM), Cisco Unified Contact Center Enterprise (UCCE) Deployments

### Components Used

The information in this document is based on these software and hardware versions:

- CVP Server

- VXML Gateway

- UCCE

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Background Information

If the latency value approaches or exceeds 200 ms, CVP  and Cisco Unified Interactive Voice Response (IVR) performance will be severely impacted.

### Symptoms

- Call drops

- No VXML app audio is played

- Microapp works fine, but VXML apps (for example: helloworld app) experience, no audio or delayed audio for over 5 seconds

CVP 8 Solution Network Reference Design (SRND) document in network latency section describes a possible workaround to not only reduce the effect of delayed audio but also the silence from VXML application due to network latency between VXML server and VXML gateway.

To configure the fetch audio feature can be performed on IVR subsystem level and on the Expanded Call Context (ECC) Variable level as the SRND document neither covered the configuration in details nor mentioned a caveat.

## Configure

IVR subsystem setting for IVR.FetchAudioDelay and IVR.FetchAudioMinimum are added. They are WAN Delay settings for the root document when the fetch is delayed over the WAN link.

These configurations should be carried out in one of the CVP configuration files: C:\Cisco\CVP\conf\ivr.properties

1. IVR.FetchAudioDelay=2

This is the length of time (in seconds) to wait, at the start of the fetch delay before the fetchaudio media plays.

This setting takes effect if the value of fetchaudio is not empty.

Default value is 2 seconds. It is used to avoid a blip sound heard in a normal network scenario (without delay).

Setting this value to zero will play fetchaudio media immediately, for a minimum of 5 seconds.

Values: 1 through 9

2. IVR.FetchAudioMinimum=5

This is the minimum length of time to play audio specified by fetchaudio even if the requested resource arrives in the mean time.

This setting takes effect only if value offetchaudio is not empty.

Default: 5 seconds

Values: 1 through 9

3. IVR.fetchaudio=flash:holdmusic.wav

This is the variable to specify the location of the fetchaudio. The holdmusic.wav should be loaded on the VXMLgateway flash.

Do not place quotation marks around the value flash:holdmusic.wav, because IVR subsystem will added another layer of quotation for example; flash:holdmusic.wav in the final string (Refer to the bug CSCub05699 )

IVR.FetchAudio=flash:holdmusic.wav

Save the ivr.properties file, and restart the callserver from the device controller in the OAMP console.

## Verify

There is currently no verification procedure available for this configuration.

## Troubleshoot

There is currently no specific troubleshooting information available for this configuration.

### Contributed by Cisco Engineers

Tian Lei Xia

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Contact Center Express