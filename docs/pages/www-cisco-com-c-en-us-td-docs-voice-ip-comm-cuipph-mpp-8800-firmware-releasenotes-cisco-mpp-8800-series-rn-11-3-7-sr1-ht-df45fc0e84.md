---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-firmware-releasenotes-cisco-mpp-8800-series-rn-11-3-7-sr1-ht-df45fc0e84
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/firmware/ReleaseNotes/cisco-mpp-8800-series-rn-11-3-7-sr1.html
retrieved_at: 2026-08-21T13:42:38.264060+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.3(7)SR1

# Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.3(7)SR1

### Download Options

Updated: October 26, 2022

Changes in this release . 3

Build information . 3

Open bugs . 3

Resolved bugs . 4

Bug Search Tool 4

This is a maintenance release and contains defects and security fixes.

Changes in this release

Webex Onboarding retry timer changes

Multiplatform Phones (MPP) support Webex services starting with MPP 11.3.6 release. This feature is enabled seamlessly for all the MPP phones registered to Webex Calling ( learn more ) and also for the Webex for Broadworks service providers that enable it ( learn more ). In the prior releases, for the cases when MPP device is unable to onboard to Webex services, it would retry every two minutes. We are changing this retry timer to gradually back off to once every 24 hours. If you are trying to resolve the issues with Webex services connection, you can force the MPP phone to retry immediately by rebooting it.

PRT (Problem Report Tool) file name restrictions

This firmware does not allow the use of “.” character in PRT name either used directly or included as a part of the macro variable.

Build information

The following firmware versions correspond to this release.

· 8811/8841/8851/8861 — sip88xx.11-3-7MPP0101-284

· 8845/8865 — sip8845_65.11-3-7MPP0101-284

· 8832 — sip8832.11-3-7MPP0101-284

Open bugs

Bug number

Severity

Description

CSCvy86354

S3

MPP phones restart intermittently

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

CSCwb84477

S3

8865: KEM Type is set to unsupported option, phone will not report kem "offline" status to cloud

CSCwb85883

S3

88xx 88x5 the generated PRT toast content will overlap when a paging call is received

CSCwb61351

S3

The o-line IP address is not EXT_IP in a NAT call

Resolved bugs

Bug number

Severity

Description

CSCwb65913

S3

ICE: Phone crashes when STUN server is not reachable due to port block

CSCwc75949

S3

8832 intermittently mutes and unmutes the microphone without user intervention

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

CSCwb65732

S3

Camera LED is still on after hanging up the video call

CSCwb92297

S2

Original 7821, 7841, 7861 Enterprise phones with hardware version V20 or later converted to MPP firmware cannot convert back to Enterprise firmware.

Bug Search Tool

We report open and resolved customer-found bugs of severity 1 to 3. You can find details about listed bugs and search for other bugs by using the Cisco Bug Search Tool. For more info on using the Bug Search, see Bug Search Tool Help .

| Bug number | Severity | Description |
|---|---|---|
| CSCvy86354 | S3 | MPP phones restart intermittently |
| CSCvw72979 | S3 | Phone will show the call center softkey after answer executive or call forward call |
| CSCvz35920 | S3 | SSRC changes for outgoing Re-INVITES |
| CSCwa70238 | S3 | MPP should block sending CANCEL when Park button is pressed twice quickly |
| CSCwb46008 | S3 | Many PRTs with logs missing for around 5 seconds |
| CSCwb84477 | S3 | 8865: KEM Type is set to unsupported option, phone will not report kem "offline" status to cloud |
| CSCwb85883 | S3 | 88xx 88x5 the generated PRT toast content will overlap when a paging call is received |
| CSCwb61351 | S3 | The o-line IP address is not EXT_IP in a NAT call |

| Bug number | Severity | Description |
|---|---|---|
| CSCwb65913 | S3 | ICE: Phone crashes when STUN server is not reachable due to port block |
| CSCwc75949 | S3 | 8832 intermittently mutes and unmutes the microphone without user intervention |
| CSCwc78400 | S3 | Command injection during PRT file generation |
| CSCwc78413 | S3 | Stored XSS via packet capture filename |
| CSCwc78427 | S2 | Secure data partition is world readable and writable |
| CSCwc78405 | S3 | Privilege escalation to root user via continually executing script |
| CSCwb65732 | S3 | Camera LED is still on after hanging up the video call |
| CSCwb92297 | S2 | Original 7821, 7841, 7861 Enterprise phones with hardware version V20 or later converted to MPP firmware cannot convert back to Enterprise firmware. |