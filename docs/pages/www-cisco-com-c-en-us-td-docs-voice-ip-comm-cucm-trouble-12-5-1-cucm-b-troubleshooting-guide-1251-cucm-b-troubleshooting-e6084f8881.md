---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-trouble-12-5-1-cucm-b-troubleshooting-guide-1251-cucm-b-troubleshooting-e6084f8881
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/trouble/12_5_1/cucm_b_troubleshooting-guide-1251/cucm_b_troubleshooting-guide-1251_chapter_0111.html
retrieved_at: 2026-08-16T18:15:44.717753+00:00
---

Troubleshooting Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Troubleshooting Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: November 24, 2023

Chapter: Voice Messaging Issues

## Chapter: Voice Messaging Issues

# Voice Messaging Issues

This section covers the solutions for the most common voice-messaging issues.

For extensive troubleshooting information for Cisco Unity voice messaging, refer to the Cisco Unity Troubleshooting Guide at the following URL:

http://www.cisco.com/en/US/products/sw/voicesw/ps2237/prod_troubleshooting_guides_list.html

For all documentation that relates to Cisco Unity systems, refer to the following URL: http://www.cisco.com/en/us/products/sw/voicesw/ps2237/tsd_products_support_series_home.html

## Voice Messaging Stops After 30 Seconds

### Symptom

When Cisco Unity system is running with Unified Communications Manager , a caller gets only 30 seconds in which to leave a voice-mail message.

### Possible 
                              
                              Cause

This problem occurs when a caller is leaving a voice message and the call terminates 30 seconds into the message. Reproduce
                              this easily by dialing a valid extension/number and attempting to leave a voice message that is longer than 30 seconds.

### Recommended 
                              
                              Action

To resolve this problem, verify that the Media Gateway Control Protocol (MGCP) is being used on the voice gateway.

If the MGCP is being used, add the no mgcp timer receive-rtcp command.

If MGCP is not on the voice gateway, enable Skinny traces for the Cisco Unity server and Cisco Communications Manager traces.

For information on setting Cisco Unity diagnostic traces, refer to the "Diagnostic Trace Utilities and Logs" section of the applicable Cisco Unity Troubleshooting Guide at http://www.cisco.com/en/US/products/sw/voicesw/ps2237/prod_troubleshooting_guides_list.html

## Cisco Unity System Does Not Roll Over: Receive Busy Tone

### Symptom

Cisco Unity Connection system does not get past the first line and will not roll over to the second port.

Example

```
Call 5000 from 1001Get Unity
Place the call on Hold
Press New Call
Dial 5000
Get Busy tone
Press End Call
Press Resume Call
Press End Call
```

### Possible 
                              
                              Cause

The Cisco Messaging Interface (CMI) service is configured with the same number as Cisco Unity Connection (5000), and it is registering the intercept, so the call is hitting the CMI.

### Recommended 
                              
                              Action

Check the CMI service parameters to ensure that the voicemaildn parameter is not configured.

## Calls That Are Forwarded to Voice Messaging System Get Treated as a Direct Call to Cisco Unity System

### Symptom

Calls from one Cisco Unified IP Phone to another that are forwarded to voice-messaging system get treated as a direct call to Cisco Unity Connection system from the phone that is making the call. However, this only occurs if the digits are dialed but works properly (receiving
                              the called-phone greeting) if the Redial softkey is pressed.

### Possible 
                              
                              Cause

The logic in the TSP states that if the call is a forwarded call and the originalCalledPartyName is "Voicemail," mark the call as a direct call. This was done for failover Cisco Unity Connection systems that are using Unified Communications Manager .

### Recommended 
                              
                              Action

On the Unified Communications Manager server, change the name of the Display field on the Cisco Voice Mail ports to anything other than "VoiceMail."

On the Cisco Unity Connection server, add a new Registry string value of HKLM\Software\ActiveVoice\AvSkinny\voiceMail display Name= anything other than
                                    VoiceMail.

## Administrator Account Is Not Associated with Cisco Unity Subscriber

### Symptom

While attempting to access the System Administrator (SA) page, you receive a message stating that the administrator account
                           is not associated with the Cisco Unity subscriber.

### Possible 
                              
                              Cause

Access was not configured for the user.

### Recommended 
                              
                              Action

To gain appropriate rights to access the SA page, you must run the GrantUnityAccess utility. Locate this tool at C:\commserver\grantunityaccess.exe

For more information about the GrantUnityAccess utility, refer to the "Granting Administrative Rights to Other Cisco Unity" section of the "Accessing the Cisco Unity Administrator" chapter in the applicable Cisco Unity System Administration Guide at http://www.cisco.com/en/US/products/sw/voicesw/ps2237/prod_troubleshooting_guides_list.html

For more information about the GrantUnityAccess utility, see Granting Administrative Rights to Other Cisco Unity Servers at the following URL: http://www.cisco.com/en/US/docs/voice_ip_comm/unity/3x/administration/guide/312/SAG_0255.html#wp1060485

If you run this utility with no options, the instructions should display. The normal use of this tool provides the domain/alias
                                    of the account that is to have access to the SA and then provides information about from which account to copy those rights.

For example, if the alias of the user to whom you want to give administration rights is TempAdministrator and your domain
                                    name is MyDOMAIN, you would use the following command at the DOS prompt:

GrantUnityAccess -u MyDOMAIN\TempAdministrator -s Installer -f.

The installer account designates a special account that always has administration rights but is not created in the directory
                                    itself; it is local to the SQL database only.

| Note | For more information about the GrantUnityAccess utility, refer to the "Granting Administrative Rights to Other Cisco Unity" section of the "Accessing the Cisco Unity Administrator" chapter in the applicable Cisco Unity System Administration Guide at http://www.cisco.com/en/US/products/sw/voicesw/ps2237/prod_troubleshooting_guides_list.html |
|---|---|

| Note | For more information about the GrantUnityAccess utility, see Granting Administrative Rights to Other Cisco Unity Servers at the following URL: http://www.cisco.com/en/US/docs/voice_ip_comm/unity/3x/administration/guide/312/SAG_0255.html#wp1060485 |
|---|---|