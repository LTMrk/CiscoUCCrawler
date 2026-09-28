---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jvdi-14-1-jvdi-b-jvdi-release-notes-141-jvdi-m-caveats-141-html-2ef0375247
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jvdi/14_1/jvdi_b_jvdi-release-notes-141/jvdi_m_caveats-141.html
retrieved_at: 2026-08-25T23:18:29.580359+00:00
---

Release Notes for Cisco Jabber Softphone for VDI Release 14.1

# Release Notes for Cisco Jabber Softphone for VDI Release 14.1

Updated: March 9, 2022

Chapter: Caveats

## Chapter: Caveats

# Caveats

## Bug Severity Levels

Known defects, or bugs, have a severity level that indicates the priority of the defect. These release notes include the following
                              bug types:

All severity level 1 or 2 bugs

Significant severity level 3 bugs

All customer-found bugs except severity level 6 enhancement requests

Severity Level

Description

1 Catastrophic

Reasonably common circumstances cause the entire system to fail, or a major subsystem to stop working, or other devices on
                                          the network to be disrupted. No workarounds exist.

2 Severe

Important functions are unusable and workarounds do not exist. Other functions and the rest of the network is operating normally.

3 Moderate

Failures occur in unusual circumstances, or minor features do not work at all, or other failures occur but low-impact workarounds
                                          exist.

This is the highest level for documentation bugs.

4 Minor

Failures occur under very unusual circumstances, but operation essentially recovers without intervention. Users do not need
                                          to install any workarounds and performance impact is tolerable.

5 Cosmetic

Defects do not cause any detrimental effect on system functionality.

6 Enhancement

Requests for new functionality or feature improvements.

## Search for Bugs

To search for bugs not listed here, use the Bug Search Tool.

Step 1

To access the Bug Search Tool, go to https://tools.cisco.com/bugsearch/search .

Step 2

Sign in with your Cisco.com user ID and password.

Step 3

To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . Alternatively, you can search by product and release.

For more information, select Help at the top right of
                                          the Bug Search page.

## Resolved caveats in Release 14.1.4

See the Jabber release notes for resolved caveats in Jabber for Windows.

Caveat ID

Severity

Description

CSCwb80658

3

VDI module should ignore the order change of TFTP Server or CCMCIP Server.  The fix for this issue requires you to upgrade
                                          the HVD to Jabber for Windows version 14.1.5 or later.

CSCwd95193

3

User A logs out of session but leaves Jabber up in VDI. User B logs in and CPU spikes.

CSCwf28064

3

Jabber in VDI using CPU (around 5-10% per VDI) while in Idle state. The fix for this issue requires you to upgrade the HVD
                                          to Jabber for Windows version 14.1.5 or later.

## Resolved caveats in Release 14.1.3

See the Jabber release notes for resolved caveats in Jabber for Windows.

Caveat ID

Severity

Description

CSCwd21433

3

Screen flickering when Jabber is running (Linux platform)

CSCwd21535

3

Jabber VDI 14.0.1 on Linux issue with mute/unmute from Jabra headset when in Zoom meeting

CSCwd50790

3

Unable to collect PRT remotely on Jabber VDI from CUCM (All thin client platforms)

CSCwd63866

3

JVDI Client 14.0.3 on Linux freezes or crashes when failing to connect to PulseAudio

CSCwd85202

3

Jabber VDI 14.1 on eLux Digital Signature Certificate has expired (Debian package)

## Resolved caveats in Release 14.1.2

See the Jabber release notes for resolved caveats in Jabber for Windows.

Caveat ID

Severity

Description

CSCwb80658

3

VDI module should ignore the order change of TFTP Server or CCMCIP Server.

CSCwc14388

3

Jabber VDI for Mac OS Virtual Channel fails when using Citrix Workspace 2111 or 2201

CSCwc36902

3

Can not switch Softphone / Hardphone. It hangs

CSCwc26870

4

Phone service for Jabber VDI disconnecting randomly

## Resolved caveats in Release 14.1.1

See the Jabber release notes for resolved caveats in Jabber for Windows.

Caveat ID

Severity

Description

CSCwb00609

3

Jabber 14.1 Windows JVDI client call control freezing with contact center call flows

CSCwb53316

3

Jabber Softphone Mute Behavior Does Not Match that Of Cisco 532 Headset on JVDI

## Resolved Caveats in Release 14.1

Caveat ID

Severity

Description

CSCvy80559

3

Jabber VDI video Black Screen - version 14

CSCvz44805

3

Jabber For Windows Becomes Slow to Respond During Large CMS Conferences

CSCvz75206

3

Jabber JVDI deployment - grey video

CSCvz79812

3

Jabber fails to login immediately after logout

CSCwa33411

3

Unable to disable screen sharing in Jabber VDI

CSCwa38601

3

jabber on vdi generating prt will timeout

CSCwa75037

3

JabberVDI for macOS overwrites login key chains

| Severity Level | Description |
|---|---|
| 1 Catastrophic | Reasonably common circumstances cause the entire system to fail, or a major subsystem to stop working, or other devices on
                                          the network to be disrupted. No workarounds exist. |
| 2 Severe | Important functions are unusable and workarounds do not exist. Other functions and the rest of the network is operating normally. |
| 3 Moderate | Failures occur in unusual circumstances, or minor features do not work at all, or other failures occur but low-impact workarounds
                                          exist. This is the highest level for documentation bugs. |
| 4 Minor | Failures occur under very unusual circumstances, but operation essentially recovers without intervention. Users do not need
                                          to install any workarounds and performance impact is tolerable. |
| 5 Cosmetic | Defects do not cause any detrimental effect on system functionality. |
| 6 Enhancement | Requests for new functionality or feature improvements. |

| Step 1 | To access the Bug Search Tool, go to https://tools.cisco.com/bugsearch/search . |
|---|---|
| Step 2 | Sign in with your Cisco.com user ID and password. |
| Step 3 | To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . Alternatively, you can search by product and release. For more information, select Help at the top right of
                                          the Bug Search page. |

| Caveat ID | Severity | Description |
|---|---|---|
| CSCwb80658 | 3 | VDI module should ignore the order change of TFTP Server or CCMCIP Server.  The fix for this issue requires you to upgrade
                                          the HVD to Jabber for Windows version 14.1.5 or later. |
| CSCwd95193 | 3 | User A logs out of session but leaves Jabber up in VDI. User B logs in and CPU spikes. |
| CSCwf28064 | 3 | Jabber in VDI using CPU (around 5-10% per VDI) while in Idle state. The fix for this issue requires you to upgrade the HVD
                                          to Jabber for Windows version 14.1.5 or later. |

| Caveat ID | Severity | Description |
|---|---|---|
| CSCwd21433 | 3 | Screen flickering when Jabber is running (Linux platform) |
| CSCwd21535 | 3 | Jabber VDI 14.0.1 on Linux issue with mute/unmute from Jabra headset when in Zoom meeting |
| CSCwd50790 | 3 | Unable to collect PRT remotely on Jabber VDI from CUCM (All thin client platforms) |
| CSCwd63866 | 3 | JVDI Client 14.0.3 on Linux freezes or crashes when failing to connect to PulseAudio |
| CSCwd85202 | 3 | Jabber VDI 14.1 on eLux Digital Signature Certificate has expired (Debian package) |

| Caveat ID | Severity | Description |
|---|---|---|
| CSCwb80658 | 3 | VDI module should ignore the order change of TFTP Server or CCMCIP Server. |
| CSCwc14388 | 3 | Jabber VDI for Mac OS Virtual Channel fails when using Citrix Workspace 2111 or 2201 |
| CSCwc36902 | 3 | Can not switch Softphone / Hardphone. It hangs |
| CSCwc26870 | 4 | Phone service for Jabber VDI disconnecting randomly |

| Caveat ID | Severity | Description |
|---|---|---|
| CSCwb00609 | 3 | Jabber 14.1 Windows JVDI client call control freezing with contact center call flows |
| CSCwb53316 | 3 | Jabber Softphone Mute Behavior Does Not Match that Of Cisco 532 Headset on JVDI |

| Caveat ID | Severity | Description |
|---|---|---|
| CSCvy80559 | 3 | Jabber VDI video Black Screen - version 14 |
| CSCvz44805 | 3 | Jabber For Windows Becomes Slow to Respond During Large CMS Conferences |
| CSCvz75206 | 3 | Jabber JVDI deployment - grey video |
| CSCvz79812 | 3 | Jabber fails to login immediately after logout |
| CSCwa33411 | 3 | Unable to disable screen sharing in Jabber VDI |
| CSCwa38601 | 3 | jabber on vdi generating prt will timeout |
| CSCwa75037 | 3 | JabberVDI for macOS overwrites login key chains |