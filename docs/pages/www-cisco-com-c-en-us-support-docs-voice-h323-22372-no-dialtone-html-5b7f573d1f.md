---
doc_id: www-cisco-com-c-en-us-support-docs-voice-h323-22372-no-dialtone-html-5b7f573d1f
source_url: https://www.cisco.com/c/en/us/support/docs/voice/h323/22372-no-dialtone.html
retrieved_at: 2026-08-21T07:17:31.067053+00:00
---

Troubleshooting No Dial Tone Issues

# Troubleshooting No Dial Tone Issues

Updated: February 2, 2006

Document ID: 22372

Contents

## Contents

## Introduction

This document discusses how to troubleshoot a voice network when no dial tone is heard from a voice port that is in the off-hook condition.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software or hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

### Conventions

For more information on document conventions, refer to the Cisco Technical Tips Conventions .

## Problem

A common problem in the voice network is when no dial tone is heard from a voice port in the off-hook condition. This could be related to configuration issues, a hardware problem, a Digital Signal Processor (DSP) problem, or a bug in Cisco IOS® software. A voice port that is configured with connection trunk does not provide dial tone. A faulty network module or Foreign Exchange Station (FXS) card may cause silence or no dial tone in a voice port.

## Solutions

The scenarios in this section describe the various problems and solutions related to no dial tone issues from a voice port.

### No LED When Phone Off the Hook

Use this procedure if there is no LED when your phone is off hook:

Check the cable to ensure that it is RJ-11 with two pins for the FXS port.

Use a different phone to test the LED.

Check Cisco IOS to ensure that the feature set is either IP Plus or Enterprise Plus.

If Steps 1 through 3 do not work, then replace the voice interface card (VIC).

Note: Narrow the problem to either VIC-2FXS or NM-2V. DSPs reside on NM-2V. If you have two FXS ports, test both of them.

### Router Does Not Recognize Voice Port

When a router does not recognize a voice port, it may be because the router is not loaded with the proper Cisco IOS image required for voice support. For a Cisco 1750 router, ensure that it does not have PVDM-256K-4 and PVDM-256K-8 DSPs. These are packet voice/data modules (PVDMs) for Cisco routers 1751 and later. If the Cisco 1750 router does not have the correct PVDM, the voice ports may appear in show version and show diag command output; however, there is no dial tone. Also, no DSPs are seen in the show voice dsp command output. The Cisco 1750 router should carry the proper PVDM-4 and PVDM-8 DSP cards.

For Cisco 1750, 2600, 3600, and MC3810 routers, a bad network module could be another problem. If there is an alarm light on the network module, then remove the module, put it back in the slot, and cycle the power. If the alarm light is still on, then replace the network module. Also, you can try to plug an analog phone into the FXS port with a good cable; if there is no dial tone, replace the FXS card.

Note: FXS-Direct Inward Dialing (DID) does not provide dial tone.

### Voice Ports Configured as Connection Trunk

If voice ports are configured as Connection Trunk or Connection PLAR (Private Line Automatic Ringdown), then the voice ports do not provide dial tone. In these cases, the remote PBX/PSTN (Public Switched Telephone Network) provides the dial tone.

Remove the Connection Trunk/PLAR configuration to ensure that you are getting the dial tone. If you need the Connection Trunk or PLAR configuration, refer to Configuring Connection Trunk for VoIP Gateways and Configuring Connection PLAR for VoIP Gateways for further assistance.

### No Dial Tone On Digital Voice Port

Check to see if the dial-peer pots are configured with the direct-inward-dial command. This command disables dial tone from the voice port. For example:

```
dial-peer voice 1 pots
destination-pattern .T direct-inward-dial port 0:D
```

If you remove the direct-inward-dial command from the dial-peer pots, then the digital voice port provides dial tone.

### Voice Ports are in the Shutdown State

When voice ports are in the shutdown state, they do not provide dial tone. To fix this problem, enable the voice port with the no shut command under the voice port.

### No Ring Descriptor Error Appears

This is an example of the No Ring Descriptor error:

```
(*Mar 5 16:05:40 UTC: %C542-1-NO_RING_DESCRIPTORS)
```

In this case, it is recommended that you open a service request ( registered customers only) with Cisco Technical Support .

### debug Command Output Shows VTSP Timeout

The VTSP and DSP timeouts are known issues that appear in many forms. Issue the test dsps slot# command to see if they are alive. Cisco IOS Software Releases 12.2.6a and later include fixes for many of these issues, but possibly not all of them. The problem was temporarily cleared by power cycle. In this case, it is recommended that you open a service request ( registered customers only) with Cisco Technical Support .

### Digital Voice Port Channels Lock Up in EM_PARK and EM_PENDING State

Some channels of a digital voice port lock up in the EM_PARK and EM_PENDING state after a period of normal operation. Sometimes, ports remain seized; other times, the PSTN does not clear the call, which keeps the port in the EM_PARK state.

For further details to troubleshoot this issue, refer to Troubleshooting the DSP on NM-HDV for Cisco 2600/3600/VG200 Series Routers . If the issue persists, open a service request ( registered customers only) with Cisco Technical Support .

## Related Information