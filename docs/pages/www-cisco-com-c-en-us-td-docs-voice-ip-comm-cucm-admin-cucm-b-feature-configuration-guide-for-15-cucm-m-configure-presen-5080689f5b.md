---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-cucm-b-feature-configuration-guide-for-15-cucm-m-configure-presen-5080689f5b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/cucm_b_feature-configuration-guide-for-15/cucm_m_configure-presentation-sharing-using-bfcp.html
retrieved_at: 2026-08-16T16:07:18.251047+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: March 26, 2026

Chapter: Configure Presentation Sharing using BFCP

## Chapter: Configure Presentation Sharing using BFCP

# Configure Presentation Sharing using BFCP

## Binary Floor Control Protocol Overview

Unified Communications Manager supports presentation sharing using the Binary Floor Control Protocol (BFCP) for supported
                           Cisco endpoints and third-party video endpoints. This feature lets users share a presentation within ongoing audio or video
                           conversation.

The following example describes how presentation sharing works using BFCP:

An ongoing video conversation exists between two video phones. User A decides to share content with User B during the conversation.
                                 User A has the option to share the entire screen or share the specific application.

The BFCP stream allows User B to view User A's shared content.

An audio-video call with content share requires at least four channels: audio, main video, the second video, and BFCP control
                           channel, to achieve video conferencing and sharing presentations in the second video channel.  If the call parties are capable
                           of Far-End Camera Control (FECC), a fifth channel must be established.

### Presentation Sharing with BFCP

From release 12.5(1)SU3 onwards, for Unified Communications Manager registered SIP endpoints, the BFCP work when:

Two video-capable endpoints that start the conversation in audio-only mode share content during the call using BFCP support.

TRP is allocated during the call.

### BFCP Architecture

Presentation sharing using BFCP is supported only on BFCP enabled SIP networks. The entire network, including the endpoint
                              devices and trunks, must be SIP.

Unified Communications Manager aids in the negotiation of the BFCP stream by relaying SIP messages between two endpoints.

This negotiation involves establishing a floor, which is a temporary permission to access shared resources.

The BFCP stream is a point-to-point stream between the endpoints. Unified Communications Manager is never a target of the
                              BFCP stream.

The following figure provides an example of a complex video network with multiple Unified Communications Manager clusters.
                              BFCP must be enabled on all the trunks and lines connecting the devices. For this network, BFCP must be enabled on the four
                              SIP trunks and two SIP lines that connect the endpoints.

### BFCP Limitations

Unified Communications Manager rejects the BFCP stream in the following scenarios:

The Allow Presentation Sharing using BFCP check box on the SIP Profile page is unchecked for one of the SIP lines or trunks in the network.

One endpoint offers BFCP, but the other does not.

When the SIP line or SIP trunk uses MTP (non pass-through mode) or Transcoder.

BFCP control channel is always unencrypted. However, the presentation channel is encrypted if both phones are encrypted.

## Presentation Sharing using BFCP Prerequisites

Make sure all endpoints and trunks in the call flow are running SIP profile.

Check Phone Support procedure and generate a report for the feature BFCP Support to obtain a list of Cisco endpoints that support Presentation Sharing using BFCP. For these endpoints, BFCP support is enabled
                                 by default. You need not perform any additional configuration for the phone to support BFCP. For more information, see Generate a Phone Feature List .

## Presentation Sharing using BFCP Configuration Task Flow

Complete the following tasks to enable Presentation sharing using the Binary Floor Control Protocol (BFCP).

Step 1

Enable BFCP Support for SIP Trunks

Enables BFCP support on all SIP trunks in the call flow.

Step 2

Enable Presentation Sharing using BFCP for Third-Party Phones

Enables BFCP support in the third-party phone configuration, if you are using third-party SIP endpoints.

### Enable BFCP Support for SIP Trunks

If you are using Presentation sharing with BFCP, the feature must be enabled in the SIP Profile that is used by all trunks
                                 in the messaging or call flow. The BFCP stream will be rejected by any trunk that does not support presentation sharing.

Step 1

Enable BFCP support within the SIP Profile that is used by the SIP trunk:

From the Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile .

Perform either of the following steps:

Click Find to select an existing SIP profile.

Click Add New to create a new SIP profile.

In the SDP Information section, check the Allow Presentation Sharing using BFCP check box to enable BFCP in the Unified Communications Manager.

By default, the check box is unchecked. For presentation sharing, BFCP must be enabled for all SIP trunks between the Unified
                                                   CM clusters.

Complete any other fields in the SIP Profile Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Click Save .

Step 2

Associate the BFCP enabled SIP Profile to your SIP trunks:

From the Cisco Unified CM Administration, choose Device > Trunks .

Click Find and select an existing SIP trunk.

In the SIP Information section, choose the SIP Profile for which you enabled BFCP to share the presentation in the intercluster call from the SIP Profile drop-down list.

Click Save .

Repeat this step for all SIP trunks that will be in the call flow of a BFCP session.

### Enable Presentation Sharing using BFCP for Third-Party Phones

If you want to use Presentation sharing using BFCP with third-party SIP Phones, you must make sure that the feature is enabled
                                 for the endpoint. This feature is supported by the following third-party phone types:

Third-party SIP Device (Advanced)

Third-party AS-SIP Endpoint

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Click Find and select an existing third-party SIP phone.

Step 3

Check the Allow Presentation Sharing using BFCP check box.

Step 4

Click Save .

| Note | BFCP control channel is always unencrypted. However, the presentation channel is encrypted if both phones are encrypted. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Enable BFCP Support for SIP Trunks | Enables BFCP support on all SIP trunks in the call flow. |
| Step 2 | Enable Presentation Sharing using BFCP for Third-Party Phones | Enables BFCP support in the third-party phone configuration, if you are using third-party SIP endpoints. |

| Step 1 | Enable BFCP support within the SIP Profile that is used by the SIP trunk: From the Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile . Perform either of the following steps: Click Find to select an existing SIP profile. Click Add New to create a new SIP profile. In the SDP Information section, check the Allow Presentation Sharing using BFCP check box to enable BFCP in the Unified Communications Manager. By default, the check box is unchecked. For presentation sharing, BFCP must be enabled for all SIP trunks between the Unified
                                                   CM clusters. Complete any other fields in the SIP Profile Configuration window. For more information on the fields and their configuration options, see the system Online Help. Click Save . |
|---|---|
| Step 2 | Associate the BFCP enabled SIP Profile to your SIP trunks: From the Cisco Unified CM Administration, choose Device > Trunks . Click Find and select an existing SIP trunk. In the SIP Information section, choose the SIP Profile for which you enabled BFCP to share the presentation in the intercluster call from the SIP Profile drop-down list. Click Save . Repeat this step for all SIP trunks that will be in the call flow of a BFCP session. |

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Click Find and select an existing third-party SIP phone. |
| Step 3 | Check the Allow Presentation Sharing using BFCP check box. |
| Step 4 | Click Save . |