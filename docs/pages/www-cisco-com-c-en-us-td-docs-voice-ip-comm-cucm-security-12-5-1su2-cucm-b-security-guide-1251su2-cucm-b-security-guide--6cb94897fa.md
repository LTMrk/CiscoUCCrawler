---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-security-12-5-1su2-cucm-b-security-guide-1251su2-cucm-b-security-guide--6cb94897fa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/12_5_1SU2/cucm_b_security-guide-1251SU2/cucm_b_security-guide-1251SU2_chapter_010010.html
retrieved_at: 2026-08-21T08:40:45.191802+00:00
---

Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: March 22, 2024

Chapter: Call Secure Status Policy

## Chapter: Call Secure Status Policy

- Call Secure Status Policy

- About Call Secure Status Policy

- Setup Call Secure                              	 Status Policy

# Call Secure Status Policy

## About Call Secure Status Policy

Call Secure Status Policy controls display of secure status icon on phones.  The following are the policy options:

All media except BFCP and iX application streams must be encrypted

This is the default value.  The security status of the call is not dependent on the encryption status of BFCP and iX application
                                       streams.

All media except iX application streams must be encrypted

The security status of the call is not dependent on the encryption status iX application streams.

All media except BFCP application streams must be encrypted

The security status of the call is not dependent on the encryption status BFCP.

All media in a session must be encrypted

The security status of the call is dependent on the encryption status of all the media streams of an established phone session.

Only Audio must be encrypted

The security status of the call is dependent on the encryption of the audio stream.

## Setup Call Secure
                        	 Status Policy

Step 1

Find the Call Secure Status Policy service parameter, as described in the "Configure Service Parameters" section of the System Configuration Guide for Cisco Unified Communications Manager .

Step 2

From the Secure
                                          				Call Icon Display Policy drop-down list, choose a policy option.

A warning
                                          				message with the impact on video calls and secure tone is displayed.

Step 3

Click Save .

The window refreshes, and Unified Communications Manager updates the service parameter with your changes.

| Note | Changes to the policy impacts display of the secure icon and playing of secure tone on the phone. |
|---|---|

| Step 1 | Find the Call Secure Status Policy service parameter, as described in the "Configure Service Parameters" section of the System Configuration Guide for Cisco Unified Communications Manager . |
|---|---|
| Step 2 | From the Secure
                                          				Call Icon Display Policy drop-down list, choose a policy option. A warning
                                          				message with the impact on video calls and secure tone is displayed. |
| Step 3 | Click Save . The window refreshes, and Unified Communications Manager updates the service parameter with your changes. |