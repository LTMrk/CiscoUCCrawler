---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-security-12-5-1su5-cucm-b-security-guide-1251su5-cucm-m-secure-recordin-2dde56c2a2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/12_5_1SU5/cucm_b_security-guide-1251su5/cucm_m_secure-recording-and-monitoring.html
retrieved_at: 2026-08-21T18:05:06.331191+00:00
---

Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU5

# Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU5

Updated: March 22, 2024

Chapter: Secure Recording and Monitoring

## Chapter: Secure Recording and Monitoring

- Secure Recording and Monitoring

- About Secure Call Monitoring and Recording Setup

- Set Up Secure Call                              	 Monitoring and Recording

# Secure Recording and Monitoring

## About Secure Call Monitoring and Recording Setup

Secure calls can be monitored and recorded, as described in this section:

A supervisor can establish a secured monitoring session for a secured or a non-secured call.

The call security of the original call is never impacted or downgraded as a result of a call monitoring request.

The monitoring call is allowed to proceed only when it can be established and maintained at the same security level as the
                                    device capability of the agent.

The original call between the agent and customer must have different crypto keys than that of monitoring call. In a monitoring
                                    session, the system encrypts the mixed voices of the agent and customer with the new key first before sending to the supervisor.

Unified Communications Manager supports call recording for authenticated calls while using a nonsecure recorder. For calls with a secure call recorder,
                                          recording is allowed only if the recorder supports SRTP fallback, so that the media stream to the recorder falls back to RTP.

To record calls that use authenticated phones:

Set the Authenticated Phone Recording , a Cisco CallManager service parameter, to Allow Recording . In this case, the call is authenticated, but the connection to the recording server is unauthenticated and unencrypted.

Unified Communications Manager should be always configured in a Mixed mode cluster security for SIP OAuth enabled phones to
                                                make secure recordings.

## Set Up Secure Call
                        	 Monitoring and Recording

Use this procedure to configure Secure Call Monitoring and Recording.

Step 1

Provision secure
                                       			 capability on agent and supervisor phones.

Step 2

Create a secure
                                       			 SIP trunk with the following configuration:

Set the Device Security Mode to Encrypted.

Check the Transmit Security Status check box.

Check the SRTP Allowed check box.

Configure the TLS SIP trunk to the recorder.

Step 3

Configure
                                       			 monitoring and recording, in the same way you would for non-secure monitoring
                                       			 and recording.

Configure a
                                             				  built-in bridge for the agent phone.

Configure the Recording Option ( Automatic Call Recording Enabled and Application Invoked Call Recording Enabled .) using the Directory Number page on the agent phone.

Create a route pattern for the recorder.

Add a call recording profile to the Directory Number.

Provision
                                             				  monitoring and recording tones as needed.

For more information and detailed procedures, see the "Monitoring and Recording" chapter in the Feature Configuration Guide for Cisco Unified Communications Manager .

| Note | Unified Communications Manager supports call recording for authenticated calls while using a nonsecure recorder. For calls with a secure call recorder,
                                          recording is allowed only if the recorder supports SRTP fallback, so that the media stream to the recorder falls back to RTP. To record calls that use authenticated phones: Set the Authenticated Phone Recording , a Cisco CallManager service parameter, to Allow Recording . In this case, the call is authenticated, but the connection to the recording server is unauthenticated and unencrypted. Unified Communications Manager should be always configured in a Mixed mode cluster security for SIP OAuth enabled phones to
                                                make secure recordings. |
|---|---|

| Step 1 | Provision secure
                                       			 capability on agent and supervisor phones. |
|---|---|
| Step 2 | Create a secure
                                       			 SIP trunk with the following configuration: Set the Device Security Mode to Encrypted. Check the Transmit Security Status check box. Check the SRTP Allowed check box. Configure the TLS SIP trunk to the recorder. |
| Step 3 | Configure
                                       			 monitoring and recording, in the same way you would for non-secure monitoring
                                       			 and recording. Configure a
                                             				  built-in bridge for the agent phone. Configure the Recording Option ( Automatic Call Recording Enabled and Application Invoked Call Recording Enabled .) using the Directory Number page on the agent phone. Create a route pattern for the recorder. Add a call recording profile to the Directory Number. Provision
                                             				  monitoring and recording tones as needed. For more information and detailed procedures, see the "Monitoring and Recording" chapter in the Feature Configuration Guide for Cisco Unified Communications Manager . |