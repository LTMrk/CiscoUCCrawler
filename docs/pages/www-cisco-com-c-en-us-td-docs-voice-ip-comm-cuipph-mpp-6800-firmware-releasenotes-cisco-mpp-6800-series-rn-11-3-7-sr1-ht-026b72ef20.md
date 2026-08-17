---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-6800-firmware-releasenotes-cisco-mpp-6800-series-rn-11-3-7-sr1-ht-026b72ef20
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/6800/firmware/ReleaseNotes/cisco-mpp-6800-series-rn-11-3-7-sr1.html
retrieved_at: 2026-08-17T01:06:22.906105+00:00
---

Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 11.3(7)SR1

# Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 11.3(7)SR1

Changes in this release . 3

Build information . 3

Open bugs . 3

Resolved bugs . 3

Bug Search Tool 4

This is a maintenance release and contains defects and security fixes.

Changes in this release

Webex Onboarding retry timer changes

Multiplatform Phones (MPP) support Webex services starting with MPP 11.3.6 release. This feature is enabled seamlessly for all the MPP phones registered to Webex Calling ( learn more ) and also for the Webex for Broadworks service providers that enable it ( learn more ). In the prior releases, for the cases when MPP device is unable to onboard to Webex services, it would retry every two minutes. We are changing this retry timer to gradually back off to once every 24 hours. If you are trying to resolve the issues with Webex services connection, you can force the MPP phone to retry immediately by rebooting it.

PRT (Problem Report Tool) file name restrictions

This firmware does not allow the use of “.” character in PRT name either used directly or included as a part of the macro variable.

Build information

The following firmware versions correspond to this release.

· 6841/6851/6861/6871 — sip68xx.11-3-7MPP0101-284

· 6821 — sip6821.11-3-7MPP0101-284

Open bugs

Bug number

Severity

Description

CSCvw72979

S3

Phone will show the call center softkey after answer executive or call forward call

CSCvz35920

S3

SSRC changes for outgoing Re-INVITES

CSCwa70238

S3

MPP should block sending CANCEL when Park button is pressed twice quickly

CSCwb46008

S3

Many PRTs with logs missing for around 5 seconds

CSCvx05369

S3

KEM works slowly after adding directories shortcut key to it

Resolved bugs

Bug number

Severity

Description

CSCwb65913

S3

ICE: Phone crashes when STUN server is not reachable due to port block

CSCwc78400

S3

Command injection during PRT file generation

CSCwc78413

S3

Stored XSS via packet capture filename

CSCwc78427

S2

Secure data partition is world readable and writable

CSCwc78405

S3

Privilege escalation to root user via continually executing script

Bug Search Tool

We report open and resolved customer-found bugs of severity 1 to 3. You can find details about listed bugs and search for other bugs by using the Cisco Bug Search Tool. For more info on using the Bug Search, see Bug Search Tool Help .

| Bug number | Severity | Description |
|---|---|---|
| CSCvw72979 | S3 | Phone will show the call center softkey after answer executive or call forward call |
| CSCvz35920 | S3 | SSRC changes for outgoing Re-INVITES |
| CSCwa70238 | S3 | MPP should block sending CANCEL when Park button is pressed twice quickly |
| CSCwb46008 | S3 | Many PRTs with logs missing for around 5 seconds |
| CSCvx05369 | S3 | KEM works slowly after adding directories shortcut key to it |

| Bug number | Severity | Description |
|---|---|---|
| CSCwb65913 | S3 | ICE: Phone crashes when STUN server is not reachable due to port block |
| CSCwc78400 | S3 | Command injection during PRT file generation |
| CSCwc78413 | S3 | Stored XSS via packet capture filename |
| CSCwc78427 | S2 | Secure data partition is world readable and writable |
| CSCwc78405 | S3 | Privilege escalation to root user via continually executing script |