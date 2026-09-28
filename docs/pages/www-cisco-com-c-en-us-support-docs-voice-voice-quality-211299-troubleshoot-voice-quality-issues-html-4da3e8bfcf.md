---
doc_id: www-cisco-com-c-en-us-support-docs-voice-voice-quality-211299-troubleshoot-voice-quality-issues-html-4da3e8bfcf
source_url: https://www.cisco.com/c/en/us/support/docs/voice/voice-quality/211299-Troubleshoot-Voice-Quality-Issues.html
retrieved_at: 2026-08-21T07:21:12.544519+00:00
---

Troubleshoot  Voice Quality Issues

# Troubleshoot  Voice Quality Issues

### Download Options

Updated: May 25, 2017

Document ID: 211299

Contents

## Contents

## Introduction

This document describes methods to troubleshoot and isolate voice quality issues in a Cisco Unified Communications Manager (CUCM) environment.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Cisco Unified Communication Manager.

- Voice over IP (VOIP)

### Components Used

The information in this document is not based on any specific software or hardware versions:

## Background Information

One of the most important steps in troubleshoot voice quality related issues is isolate them, either to a particular phone, set of phones, switch, gateway, etc. This so allows for targeted troubleshooting and faster resolution of the problem. One analogy that illustrates the importance of the isolation of the issue is a lost car in an airport parking lot. Find a lost car in an airport parking lot is a difficult task, when you know that the car is in a specific section of the parking lot (section 1 for example), makes the task less daunting, but when you also have the section and row (section 5, row D) it greatly reduces the time it would take to find the car.

### Where to Start?

Once the issue has been identified via users that report issues, Call Detail Records (CDRs) or some other means, it is important to gather data to help isolate it. Voice quality issues typically fall into one of three categories: network related (includes Gateway (GW), and PSTN issues), phone model/firmware related, or equipment (ex. headset) related. It is important to gather data to determine which of these categories the voice quality issues are a result of. This data allows a comparison between phones without voice quality issues and phones with voice quality issues to find the differences between them, which is a crucial step to solve many voice quality issues.

Step 1. The first step to isolate the voice quality issue is to find out exactly which users experience it and talk to them, either in person or over the phone, to get an accurate description of it. If there are a large number of users that report the issue talk to a sample (maybe 5-10) of them to get an accurate description of the symptoms. If only a few users report the issue, talk to the people around them to see if they also experience any problem as the issue can be more widespread than it appears as many users won't report it.

Step 2. Take note of the physical location (ex. Site A, Floor 2), user name (of the user's the phone), directory numbers (DNs), phone model (ex 8865), phone firmware (ex. 11.5.1) and IP addresses of the phones that experience voice quality issues. Create a spreadsheet with this information sorted by physical location. The 30 minutes (or less) it takes to create this spreadsheet when you start to troubleshoot, could save hours, or even days of troubleshoot time.

Step 3. Once the spreadsheet has been created take a look at the list of phones and see what they have in common and what is different about them and other phones that don't have voice quality issues. After that you can realize that all phones with the issue are in the same building and on the same floor, you can realize that the phones that have issues are connected to switches which were recently upgraded or you can see that all of the phones that have the issue are on a particular firmware.

### Questions to ask in all Scenarios

These questions helps to narrow down the voice path of the effected calls.

1. Does the issue occur on only external calls, only internal calls, or both?

The audio for external and internal calls typically takes different paths. An external call typically leaves the Cisco voice network via a (GW) or CUBE connected to the PSTN or a SIP provider. If the issue is with internal calls only you can rule out the GW in most cases as the GW is not be involved in the call. The exception to this would be if media resources (Media Termination Point (MTP), or Transcoder (Xcoder) that reside on the GW are invoked.

2. Does the issue effect only outbound audio that leaves the phone (from the user to the person they talk to), inbound audio to the phone (from the person they talk to, to the user) or both?

3. Is the call a basic IP phone to IP phone call (User A --> Switch --> User B) or IP phone to PSTN call ( User --> Switch -->  GW --> PSTN) or is the call more complex?

For example, is Extension Mobility Cross Cluster (EMCC) used? is this a call center environment with Unified Contact Center (UCC) or Unified Contact Center Express (UCCX)? etc. If you take the complexity out of the call when you place a basic IP Phone to IP Phone or IP phone to PSTN call does the problem still exist?

4. If the call flow with the reported voice quality issue is complex, a UCCX call for example, does the user/phone experience the voice quality issue if they make/receive a basic call (both internal and external)?

### One User Experiencing Issues

If the issue is with one User, work with her/him to determine these points:

Step 1. Verify that the phone with the issue runs the same firmware as other known phones that work fine, if the firmware is different a firmware upgrade can resolve the issue.

Step 2.  Does the user experience the issue while she/he uses their handset, speakerphone, headset, all three?

a. If the issue is with the handset only, verify the handset connections, if there is still an issue, swap out the handset with the handset from a different phone that has no reported issues, if the issue persists there can be an issue with the phone/phone firmware.

b. If the issue is with the speakerphone try to adjust the volume, if issue persists, swap the phone with a known working phone, if the issue persists there can be an issue with the phone/phone firmware.

c. If there is an issue with the headset verify that all connections between the phone and the headset (headset base), are other users with the same make/model of the headset without issue? If they are test a known headset that works fine with the phone with the reported issue, if there is no audio problem when you use the known headset that works fine the issue is likely with the headset and you can need to contact the headset manufacturer, if there is a problem with the known headset that works fine there can be a problem with the phone/phone firmware.

Step 3. If the phone is on the same firmware as other phones without issues, and the user has issues with the headset, speakerphone, and headset the issue is likely to be with the physical phone itself or the network cabling from the phone to the switch. One way to test this would be to unplug the patch cable from back of the phone (as to not bring a potentially bad patch cable from the user's location to a test location), find a known working phone, and plug the patch cable from the working phone into the non-working phone and perform a test. If the audio issues are still present, there is likely an issue with the physical phone. If there are no audio issues, try replacing the patch cable (with a known working patch cable) that was plugged into the phone that experience issues, if it persists check the network cabling and all connections/punch downs between the users Ethernet jack and the switch.

### Multiple Users Experiencing Issues

If the steps taken up until this point have not isolated the source of the poor voice quality the next step is to take packet captures along the network path that the RTP packets follow. Wireshark (or another tool capable to decode RTP streams) packet captures can help us narrow down the source of the issue with these steps.

Step 1. Create a simple topology that shows the path that the RTP packets takes. This example uses this topology, the issue is that the customer on the PSTN side has audio quality issues when listens to the user, the user can hear the customer without issue. With this information, you know to focus only on the RTP packets that travels from the user side to the customer side.

Step 2. Once you have the topology written out, the first step is to take packet captures on one side of the topology and work your way to the other end of the topology.

a. Take the first capture with a port span of the switch port that the IP Phone is plugged into. Use Wireshark to decode the RTP stream and play back the audio. If there is an issue with the audio (the users voice is not clear) the focus can be placed on the cabling from the phone to the switch, the phone equipment (handset, headset, speakerphone), and the phone itself. If there is no issue with the audio (the users voice is clear), you can eliminate the phone, cabling from the phone to the switch, and the phone equipment (handset, headset, speakerphone) as the source of the poor quality. At this point move to Step (b) if there is no issue with the audio.

b. Take a packet capture at router_A (ingress and egress), then decode and play back the audio streams. If there is an issue with the audio at ingress you have isolated the issue, as you know that the audio entered switch_A without issue but entered router_A with an issue. If there is no issue with the audio at ingress and the audio quality was poor on egress, you have isolated the issue to router_A. If there is no issue with the audio move to Step (c), continue to gather packet captures along the RTP path.

c. Take a packet capture at router_B (ingress and egress), then decode and play back the audio streams. If there is an issue with audio at the ingress of router_B, and you know that there was no audio issue at the egress of router_A from previous packet captures, you have isolated the issue and know that the issue is between router_A and router_B (the WAN in this example). If there is no issue with the audio at ingress and the audio quality was poor on egress, you have isolated the issue to router_B. If there is no issue with the audio move to Step (d) to gather more packet captures.

d. At this point in the troubleshoot process you have determined that the audio quality is good from the IP Phone, switch_A, router_A, the WAN, and the egress of router_B. The next packet capture must be taken from the GW. If there is a problem with the audio at the ingress of the GW the issue has been isolated to switch_B. If there is an audio issue with audio quality at egress, you have isolated the issue to the GW. If there is no issue with audio quality at egress the issue is likely on the PSTN/Provider side, contact your Provider, provide them with a packet capture with the audio that leaves the GW without issue would be the next step in the troubleshoot process.

### Additional Resources

1. Collecting a packet capture from a Cisco IP Phone

2. UC Troubleshooting with Wireshark (Audio Playback Method from RTP)

3. How to troubleshoot voice quality issues in a UCM environment (bad sound, no audio)

4. Recognizing and Categorizing Symptoms of Voice Quality Problems

5. How to use Wireshark for VOIP Troubleshooting