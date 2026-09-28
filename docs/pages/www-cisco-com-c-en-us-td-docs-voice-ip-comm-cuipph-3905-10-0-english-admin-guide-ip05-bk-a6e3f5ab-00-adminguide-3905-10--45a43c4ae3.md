---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-3905-10-0-english-admin-guide-ip05-bk-a6e3f5ab-00-adminguide-3905-10--45a43c4ae3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/3905/10_0/english/admin_guide/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0/IP05_BK_A6E3F5AB_00_adminguide-3905-10_0_chapter_01011.html
retrieved_at: 2026-08-21T14:35:33.775815+00:00
---

Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

# Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0

Updated: May 9, 2025

Chapter: Maintenance

## Chapter: Maintenance

# Maintenance

## Basic Reset

Performing a basic reset of a CiscoIP Phone
                              		  provides a way to recover if the phone experiences an error and provides a way
                              		  to reset or restore various configuration and security settings.

The following table describes the ways to perform a basic
                              		  reset. You can reset a phone  after the phone has
                              		  started up. Choose the operation that is appropriate for your situation.

Operation

Action

Explanation

Restart phone

Press Services, Applications, or Directories and then press **#** .

Resets any user and network setup changes that you have made,
                                          					 but that the phone has not written to its Flash memory, to previously saved
                                          					 settings, then restarts the phone.

### Reset the Phone to the Factory Settings from the Keypad

You can reset the phone to the factory settings. The reset clears all the phone parameters.

Step 1

Remove power from the phone in one of these ways:

- Unplug the power adapter.

- Unplug the LAN cable.

Step 2

Press the pound (#) key and plug the phone in.

Step 3

When prompted, enter the following key sequence:

123456789*0#

### Perform Factory Reset from Phone Menu

To perform a factory reset of a phone,

Step 1

Press Applications .

Step 2

Choose Admin
                                                				  Settings > Reset
                                                				  All .

If required, unlock the phone options.

Step 3

Choose Yes and press Select .

## Voice Quality
                        	 Monitoring

To
                              		  measure the voice quality of calls that are sent and received within the
                              		  network, Cisco IP Phones use these statistical metrics that are based on
                              		  concealment events. The DSP plays concealment frames to mask frame loss in the
                              		  voice packet stream.

Concealment Ratio metrics—Show the ratio of concealment frames over total speech frames. An interval conceal ratio is calculated
                                    every 3 seconds.

Concealed Second metrics—Show the number of seconds in which the DSP plays concealment frames due to lost frames. A severely "concealed second" is a second in which the DSP plays more than five percent concealment frames.

Concealment
                                          			 ratio and concealment seconds are primary measurements based on frame loss. A
                                          			 Conceal Ratio of zero indicates that the IP network is delivering frames and
                                          			 packets on time with no loss.

You can
                              		  access voice quality metrics from the Cisco IP Phone using the Call Statistics
                              		  screen or remotely by using Streaming Statistics.

### Voice Quality Troubleshooting Tips

When you observe significant and persistent changes to metrics, use the following table for general troubleshooting information.

Metric Change

Condition

Conceal Ratio and Conceal Seconds increase significantly

Network impairment from packet loss or high jitter.

Conceal Ratio is near or at zero, but the voice quality is poor.

- Noise or distortion in the audio channel such as echo or audio levels.

- Tandem calls that undergo multiple encode/decode such as calls to a cellular network or calling card network.

- Acoustic problems coming from a speakerphone, handsfree cellular phone or wireless headset.

Check packet transmit (TxCnt) and packet receive (RxCnt) counters to verify that voice packets are flowing.

MOS LQK scores decrease significantly

Network impairment from packet loss or high jitter levels:

- Average MOS LQK decreases may indicate widespread and uniform impairment.

- Individual MOS LQK decreases may indicate bursty impairment.

Cross-check the conceal ratio and conceal seconds for evidence of packet loss and jitter.

MOS LQK scores increase significantly

- Check to see if the phone is using a different codec than expected (RxType and TxType).

- Check to see if the MOS LQK version changed after a firmware upgrade.

Voice quality metrics do not account for noise or distortion, only frame loss.

## Cisco IP Phone Cleaning

To clean your Cisco IP Phone, use only a dry soft
                              		cloth to gently wipe the phone and the phone screen. Do not apply liquids or
                              		powders directly to the phone. As with all non-weatherproof electronics,
                              		liquids and powders can damage the components and cause failures.

When the phone is in sleep mode, the screen is blank and
                              		the 
                              		Select button is not lit. When the phone is in
                              		this condition, you can clean the screen, as long as you know that the phone
                              		will remain asleep until after you finish cleaning.

| Operation | Action | Explanation |
|---|---|---|
| Restart phone | Press Services, Applications, or Directories and then press **#** . | Resets any user and network setup changes that you have made,
                                          					 but that the phone has not written to its Flash memory, to previously saved
                                          					 settings, then restarts the phone. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Remove power from the phone in one of these ways: Unplug the power adapter. Unplug the LAN cable. |  |
| Step 2 | Press the pound (#) key and plug the phone in. |  |
| Step 3 | When prompted, enter the following key sequence: | 123456789*0# The phone resets. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Choose Admin
                                                				  Settings > Reset
                                                				  All . If required, unlock the phone options. |
| Step 3 | Choose Yes and press Select . |

| Note | Concealment
                                          			 ratio and concealment seconds are primary measurements based on frame loss. A
                                          			 Conceal Ratio of zero indicates that the IP network is delivering frames and
                                          			 packets on time with no loss. |
|---|---|

| Metric Change | Condition |
|---|---|
| Conceal Ratio and Conceal Seconds increase significantly | Network impairment from packet loss or high jitter. |
| Conceal Ratio is near or at zero, but the voice quality is poor. | Noise or distortion in the audio channel such as echo or audio levels. Tandem calls that undergo multiple encode/decode such as calls to a cellular network or calling card network. Acoustic problems coming from a speakerphone, handsfree cellular phone or wireless headset. Check packet transmit (TxCnt) and packet receive (RxCnt) counters to verify that voice packets are flowing. |
| MOS LQK scores decrease significantly | Network impairment from packet loss or high jitter levels: Average MOS LQK decreases may indicate widespread and uniform impairment. Individual MOS LQK decreases may indicate bursty impairment. Cross-check the conceal ratio and conceal seconds for evidence of packet loss and jitter. |
| MOS LQK scores increase significantly | Check to see if the phone is using a different codec than expected (RxType and TxType). Check to see if the MOS LQK version changed after a firmware upgrade. |

| Note | Voice quality metrics do not account for noise or distortion, only frame loss. |
|---|---|