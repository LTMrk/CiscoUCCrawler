---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-cucm-b-feature-configuration-guide-for-15-cucm-mp-abb2648f-00-aud-dde29d70eb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/cucm_b_feature-configuration-guide-for-15/cucm_mp_abb2648f_00_audible-message-waiting-indicator-12-0.html
retrieved_at: 2026-08-16T16:03:25.330082+00:00
---

Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Feature Configuration Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: March 26, 2026

Chapter: Audible Message Waiting Indicator

## Chapter: Audible Message Waiting Indicator

# Audible Message Waiting Indicator

## Audible Message
                        	 Waiting Indicator Overview

You can configure Audible Message Waiting Indicator (AMWI) to play a stutter dial tone on the Cisco Unified IP Phone to notify users of new voice messages. Users hear a stutter dial tone whenever the phone goes off hook on a line on which
                           a voice message was left.

You can configure AMWI for all the phones in a cluster or for only
                           		certain directory numbers. The directory-number-level configuration takes
                           		precedence over the cluster-wide configuration.

## Audible Message
                        	 Waiting Indicator Prerequisites

You can configure AMWI only on Cisco Unified IP Phone that are running phone firmware Release 8.3(1) or later.

## Audible Message
                        	 Waiting Indicator Configuration Task Flow

### Before you begin

Review Audible Message Waiting Indicator Prerequisites .

Step 1

Generate a Phone Feature List

Generate a
                                          				report to identify devices that support the Audible Message Waiting Indicator
                                          				feature.

Step 2

Configure Audible Message Waiting Indicator Service Parameters

Step 3

Configure Audible Message Waiting Indicator for a Directory Number

Step 4

Configure Audible Message Waiting Indicator for a SIP Profile

### Configure Audible
                           	 Message Waiting Indicator Service Parameters

#### Before you begin

Generate a Phone Feature List

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

From the Server drop-down list, choose the server that is
                                          			 running the Cisco CallManager service.

Step 3

From the Service drop-down list, choose Cisco
                                             				CallManager .

Step 4

In the Clusterwide Parameters ( Feature - General) section,
                                          			 choose the Audible Message Waiting Indication Policy service
                                          			 parameter. This parameter determines whether the Audible Message Waiting
                                          			 Indicator is turned on of off for all the devices in the cluster.

Step 5

Click Save .

### Configure Audible
                           	 Message Waiting Indicator for a Directory Number

Follow these steps
                                 		  to configure AMWI for a directory number that is associated with a device.

The AMWI setting
                                             			 on an individual directory number overrides the clusterwide setting.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

In the Association section, click Add a
                                             				new DN .

Step 3

Select the Audible Message Waiting Indicator Policy . Choose one
                                          			 of the following options:

Off

On —When you select this option, the users will receive a stutter dial tone when the handset is off hook

Default —When you select this option, the phone uses the default that was set at the system level.

Step 4

Configure the
                                          			 remaining fields in the Directory Number Configuration window. See the online
                                          			 help for more information about the fields and their configuration options.

Step 5

Click Save .

### Configure Audible
                           	 Message Waiting Indicator for a SIP Profile

Follow these steps
                                 		  to configure Audible Message Waiting Indicator (AMWI) for a SIP profile.

The AMWI setting
                                             			 on an individual SIP profile overrides the clusterwide setting.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile .

Step 2

Enter the
                                          			 search criteria to use and click Find .

Step 3

Click the SIP
                                          			 profile that you want to update.

Step 4

Check the Stutter Message Waiting check box to activate
                                          			 stutter dial tone when the phone is off hook and a message is waiting.

Step 5

Click Save .

Step 6

Click Apply
                                             				Config .

## Audible Message
                        	 Waiting Indicator Troubleshooting

### Audible Message
                           	 Waiting Indicator Is Not Heard on the Phone

Problem Phone does not play stutter
                                 		  dial tone to notify the user of new voice messages.

If the user uses
                                 		  an SCCP phone, check the following:

Ensure that the phone firmware release is 8.3(1) or later.

Check the AMWI setting for the phone and the line on which the user went off hook.

Verify that the Cisco CallManager service is running on the server.

Check the sniffer trace between the phone and Unified Communications Manager . Make sure that the phone receives the StartTone message with tone type equal to 42.

If the user uses a SIP phone, check the following:

Ensure that the phone firmware release is 8.3(1) or later.

Check the line (directory number) configuration. The phone must display the settings such as line1_msgWaitingAMWI : 1, line2_msgWaitingAMWI
                                       : 0.

Ensure that the Stutter Message Waiting check box is checked in the SIP Profile Configuration window in Cisco Unified CM Administration.

### Localized AMWI
                           	 Tone Is Not Played in a Specific Locale

Problem The phone that is
                                 		  configured in a non-English locale does not play the localized tone.

Solution Check the following:

From Cisco Unified CM Administration, verify the User Locale in the Device Profile Configuration window ( Device > Device Settings > Device Profile ).

Make sure that the user resets the phone after changing the locale.

Check user/local/cm/tftp /<locale name> directory and verify that the AMWI tone is defined in the localized g3-tones.xml file.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Generate a Phone Feature List | Generate a
                                          				report to identify devices that support the Audible Message Waiting Indicator
                                          				feature. |
| Step 2 | Configure Audible Message Waiting Indicator Service Parameters | Configure
                                       			 AMWI default setting for all phones in a cluster. |
| Step 3 | Configure Audible Message Waiting Indicator for a Directory Number | Configure
                                       			 AMWI for a directory number that is associated to a device. |
| Step 4 | Configure Audible Message Waiting Indicator for a SIP Profile | Configure
                                       			 AMWI for SIP profiles. Perform this procedure to configure AMWI for SIP phones. |

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down list, choose the server that is
                                          			 running the Cisco CallManager service. |
| Step 3 | From the Service drop-down list, choose Cisco
                                             				CallManager . |
| Step 4 | In the Clusterwide Parameters ( Feature - General) section,
                                          			 choose the Audible Message Waiting Indication Policy service
                                          			 parameter. This parameter determines whether the Audible Message Waiting
                                          			 Indicator is turned on of off for all the devices in the cluster. |
| Step 5 | Click Save . |

| Note | The AMWI setting
                                             			 on an individual directory number overrides the clusterwide setting. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | In the Association section, click Add a
                                             				new DN . The Directory Number Configuration window appears. |
| Step 3 | Select the Audible Message Waiting Indicator Policy . Choose one
                                          			 of the following options: Off On —When you select this option, the users will receive a stutter dial tone when the handset is off hook . Default —When you select this option, the phone uses the default that was set at the system level. |
| Step 4 | Configure the
                                          			 remaining fields in the Directory Number Configuration window. See the online
                                          			 help for more information about the fields and their configuration options. |
| Step 5 | Click Save . |

| Note | The AMWI setting
                                             			 on an individual SIP profile overrides the clusterwide setting. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > SIP Profile . The Find and List SIP Profiles window appears. |
|---|---|
| Step 2 | Enter the
                                          			 search criteria to use and click Find . The
                                          			 window displays a list of SIP profiles that match the search criteria. |
| Step 3 | Click the SIP
                                          			 profile that you want to update. The SIP
                                             				Profile Configuration window appears. |
| Step 4 | Check the Stutter Message Waiting check box to activate
                                          			 stutter dial tone when the phone is off hook and a message is waiting. |
| Step 5 | Click Save . |
| Step 6 | Click Apply
                                             				Config . |