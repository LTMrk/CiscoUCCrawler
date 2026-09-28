---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-english-admin-guide-pa2d-b-7800-series-admin-guide-cucm-p-8a71609259
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/english/admin-guide/pa2d_b_7800-series-admin-guide-cucm/pa2d_b_7800-series-admin-guide-cucm_chapter_01111.html
retrieved_at: 2026-08-21T13:26:49.994669+00:00
---

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

Updated: May 29, 2025

Chapter: Maintenance

## Chapter: Maintenance

# Maintenance

## Basic Reset

Performing a basic reset of a Cisco IP Phone provides a way to recover when the phone experiences an error. The reset provides
                              a way to reset or restore various configuration and security settings.

The following table describes the ways to perform a basic reset. You can reset a phone with any of these operations after
                              the phone has started up. Choose the operation that is applicable for your situation.

Operation

Action

Explanation

Restart phone

Press Services , Applications , or Directories and then press **#** .

Press Settings and choose Device Administration > Restart .

Resets any user and network setup changes that you have made,
                                          					 but that the phone has not written to its Flash memory, to previously saved
                                          					 settings, then restarts the phone.

Reset settings

Press Settings and choose Device Administration > Factory Reset .

Restores phone configuration or settings to factory default.

To reset settings, press Applications > Admin Settings > Custom Reset .

Restores phone configuration or settings to noncustomized default.

### Factory Reset the Phone with the Keypad

Use these steps to reset the phone to factory default settings using the phone keypad.

#### Before you begin

You must know if your phone is an original hardware release or if the hardware has been updated and re-released.

Step 1

Unplug the phone:

- If using PoE, unplug the LAN cable.

- If using the power cube, unplug the power cube.

Step 2

Wait 5 seconds.

Step 3

On earlier hardware versions, the Mute button lights up. Wait for the Mute button to turn off.

### Perform Reset All Settings from Phone Menu

To perform a factory reset of a phone,

Step 1

Press Applications .

Step 2

Choose Admin
                                                				  Settings > Reset
                                                				  Settings > All .

If required, unlock the phone options.

### Perform Factory Reset from Phone Menu

Step 1

Press Applications .

Step 2

Select Device administration > Factory reset .

Step 3

Scroll to Admin Settings > Reset Settings , and select All .

Step 4

To restore phone configuration or settings to factory default, press OK .

### Perform Custom Reset from Phone Menu

Step 1

Press Applications .

Step 2

Scroll to Admin
                                             				Settings and select Custom Reset .

Step 3

To restore phone configuration or settings to noncustomized default, press Ok .

### Reboot Your Phone from the Backup Image

Your Cisco IP Phone has a second, backup image that allows you to recover the phone when the default image has been compromised.

To reboot your phone from the backup, perform the following procedure.

Step 1

Disconnect the power supply.

Step 2

Press and hold the pound (#) key.

Step 3

Reconnect the power. Continue pressing the pound key until the Speakerphone and Headset buttons turn green.

Step 4

Release the pound key.

## Remove CTL
                        	 File

Deletes only the CTL file from the phone.

Step 1

From the Admin Settings menu, if required, unlock phone
                                       			 options.

Step 2

Choose Reset Settings > Security .

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
| Restart phone | Press Services , Applications , or Directories and then press **#** . Press Settings and choose Device Administration > Restart . | Resets any user and network setup changes that you have made,
                                          					 but that the phone has not written to its Flash memory, to previously saved
                                          					 settings, then restarts the phone. |
| Reset settings | Press Settings and choose Device Administration > Factory Reset . | Restores phone configuration or settings to factory default. |
| To reset settings, press Applications > Admin Settings > Custom Reset . | Restores phone configuration or settings to noncustomized default. |

| Step 1 | Unplug the phone: If using PoE, unplug the LAN cable. If using the power cube, unplug the power cube. |
|---|---|
| Step 2 | Wait 5 seconds. |
| Step 3 | On earlier hardware versions, the Mute button lights up. Wait for the Mute button to turn off. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Choose Admin
                                                				  Settings > Reset
                                                				  Settings > All . If required, unlock the phone options. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Factory reset . |
| Step 3 | Scroll to Admin Settings > Reset Settings , and select All . |
| Step 4 | To restore phone configuration or settings to factory default, press OK . |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Scroll to Admin
                                             				Settings and select Custom Reset . |
| Step 3 | To restore phone configuration or settings to noncustomized default, press Ok . |

| Step 1 | Disconnect the power supply. |
|---|---|
| Step 2 | Press and hold the pound (#) key. |
| Step 3 | Reconnect the power. Continue pressing the pound key until the Speakerphone and Headset buttons turn green. |
| Step 4 | Release the pound key. |

| Step 1 | From the Admin Settings menu, if required, unlock phone
                                       			 options. |
|---|---|
| Step 2 | Choose Reset Settings > Security . |

| Note | Concealment
                                          			 ratio and concealment seconds are primary measurements based on frame loss. A
                                          			 Conceal Ratio of zero indicates that the IP network is delivering frames and
                                          			 packets on time with no loss. |
|---|---|

| Metric Change | Condition |
|---|---|
| Conceal Ratio and Conceal Seconds increase significantly | Network impairment from packet loss or high jitter. |
| Conceal Ratio is near or at zero, but the voice quality is poor. | Noise or distortion in the audio channel such as echo or audio levels. Tandem calls that undergo multiple encode/decode such as calls to a cellular network or calling card network. Acoustic problems coming from a speakerphone, handsfree cellular phone or wireless headset. Check packet transmit (TxCnt) and packet receive (RxCnt) counters to verify that voice packets are flowing. |

| Note | Voice quality metrics do not account for noise or distortion, only frame loss. |
|---|---|