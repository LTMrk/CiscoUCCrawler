---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-english-adminguide-p881-bk-c136782f-00-cisco-ip-phone-880-cf1b8f0878
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/adminguide/P881_BK_C136782F_00_cisco-ip-phone-8800_series/P881_BK_C136782F_00_cisco-ip-phone-8811-8841_chapter_01111.html
retrieved_at: 2026-08-21T01:53:29.357134+00:00
---

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

# Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

Updated: November 6, 2025

Chapter: Maintenance

## Chapter: Maintenance

# Maintenance

## Basic Reset

Performing a basic reset of a CiscoIP Phone
                              		  provides a way to recover if the phone experiences an error and provides a way
                              		  to reset or restore various configuration and security settings.

The following table describes the ways to perform a basic
                              		  reset. You can reset a phone with any of these operations after the phone has
                              		  started up. Choose the operation that is appropriate for your situation.

Operation

Action

Explanation

Restart phone

Press Applications . Go to Admin settings > Reset settings > Reset device .

Resets any user and network setup changes that you have made,
                                          					 but that the phone has not written to its Flash memory, to previously saved
                                          					 settings, then restarts the phone.

Reset settings

To reset settings, press Applications and choose Administrator Settings > Reset Settings > Network .

Resets user and network setup settings to their default
                                          					 values, and restarts the phone.

To reset the CTL file, press Applications and choose Administrator Settings > Reset Settings > Security .

Resets the CTL file.

### Reset the Phone to the Factory Settings from the Phone Keypad

You can reset the phone to the factory settings. The reset clears all the phone parameters.

Step 1

Remove power from the phone in one of these ways:

- Unplug the power adapter.

- Unplug the LAN cable.

Step 2

Wait for 5 seconds.

Step 3

Press and hold # and plug the phone back in. Release the # only when the Headset and Speaker buttons are lit.

In some hardware versions, the Mute button also lights along with Headset and Speaker buttons when you plug the phone back in. In that case, wait for all of them to go out and release # only when the Headset and Speaker buttons are lit again.

Step 4

Enter the following key sequence:

123456789*0#

The light for the Headset button turns off after you press the 1 key. After you enter the key sequence, the Mute button lights.

Caution

Do not power down the phone until it completes the factory reset process, and the main screen appears.

### Perform Reset All
                           	 Settings from Phone Menu

Perform this task if you want to reset your user and network setup settings to the default values.

Step 1

Press Applications .

Step 2

Choose Administrator settings > Reset settings > All settings .

If necessary, unlock the phone options.

### Reboot Your Phone from the Backup Image

Your Cisco IP Phone has a second, backup image that allows you to recover the phone when the default image has been compromised.

To reboot your phone from the backup image, perform the following procedure.

Step 1

Disconnect the power supply.

Step 2

Press and hold the star (*) key.

Step 3

Reconnect the power. Continue pressing the star key until the Mute LED turns off.

Step 4

Release the star key.

## Perform Network
                        	 Configuration Reset

Resets
                              		  network configuration settings to their default values and resets the phone.
                              		  This method causes DHCP to reconfigure the IP address of the phone.

Step 1

From the
                                       			 Administrator Settings menu, if required, unlock phone options.

Step 2

Choose Reset
                                             				  Settings > Network Setup .

## Perform User Network Configuration Reset

Resets any user and network configuration changes that you
                              		  have made, but that the phone has not written to flash memory, to previously
                              		  saved settings.

Step 1

From the Administrator Settings menu, if required, unlock phone options.

Step 2

Choose Reset
                                             				  Settings > Reset Device .

## Remove CTL File

Deletes
                              		  only the CTL file from the phone.

Step 1

From the Administrator
                                       			 Settings menu, if required, unlock phone options.

Step 2

Choose Reset
                                             				  Settings > Security Settings .

## Quality Report Tool

The Quality Report Tool (QRT) is a voice quality and general
                              		problem-reporting tool for the Cisco IP Phone. The QRT feature is
                              		installed as part of Cisco Unified Communications Manager installation.

You can configure user Cisco IP Phones with QRT.
                              		When you do so, users can report problems with phone calls by pressing Report
                              		Quality. This softkey or button is available only when the Cisco IP
                              		Phone is in the Connected, Connected Conference, Connected Transfer, or OnHook
                              		states.

When a user presses Report Quality, a list of problem
                              		categories appears. The user selects the appropriate problem category, and this
                              		feedback is logged in an XML file. Actual information that is logged depends on the
                              		user selection and whether the destination device is a Cisco IP Phone.

For more information about using QRT, see the documentation for your particular Cisco Unified Communications Manager release.

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
| Restart phone | Press Applications . Go to Admin settings > Reset settings > Reset device . | Resets any user and network setup changes that you have made,
                                          					 but that the phone has not written to its Flash memory, to previously saved
                                          					 settings, then restarts the phone. |
| Reset settings | To reset settings, press Applications and choose Administrator Settings > Reset Settings > Network . | Resets user and network setup settings to their default
                                          					 values, and restarts the phone. |
| To reset the CTL file, press Applications and choose Administrator Settings > Reset Settings > Security . | Resets the CTL file. |

| Step 1 | Remove power from the phone in one of these ways: Unplug the power adapter. Unplug the LAN cable. |
|---|---|
| Step 2 | Wait for 5 seconds. |
| Step 3 | Press and hold # and plug the phone back in. Release the # only when the Headset and Speaker buttons are lit. Note In some hardware versions, the Mute button also lights along with Headset and Speaker buttons when you plug the phone back in. In that case, wait for all of them to go out and release # only when the Headset and Speaker buttons are lit again. | Note | In some hardware versions, the Mute button also lights along with Headset and Speaker buttons when you plug the phone back in. In that case, wait for all of them to go out and release # only when the Headset and Speaker buttons are lit again. |
| Note | In some hardware versions, the Mute button also lights along with Headset and Speaker buttons when you plug the phone back in. In that case, wait for all of them to go out and release # only when the Headset and Speaker buttons are lit again. |
| Step 4 | Enter the following key sequence: 123456789*0# The light for the Headset button turns off after you press the 1 key. After you enter the key sequence, the Mute button lights. Caution Do not power down the phone until it completes the factory reset process, and the main screen appears. The phone resets. | Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
| Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |

| Note | In some hardware versions, the Mute button also lights along with Headset and Speaker buttons when you plug the phone back in. In that case, wait for all of them to go out and release # only when the Headset and Speaker buttons are lit again. |
|---|---|

| Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Choose Administrator settings > Reset settings > All settings . If necessary, unlock the phone options. |

| Step 1 | Disconnect the power supply. |
|---|---|
| Step 2 | Press and hold the star (*) key. |
| Step 3 | Reconnect the power. Continue pressing the star key until the Mute LED turns off. |
| Step 4 | Release the star key. The phone reboots from the backup image. |

| Step 1 | From the
                                       			 Administrator Settings menu, if required, unlock phone options. |
|---|---|
| Step 2 | Choose Reset
                                             				  Settings > Network Setup . |

| Step 1 | From the Administrator Settings menu, if required, unlock phone options. |
|---|---|
| Step 2 | Choose Reset
                                             				  Settings > Reset Device . |

| Step 1 | From the Administrator
                                       			 Settings menu, if required, unlock phone options. |
|---|---|
| Step 2 | Choose Reset
                                             				  Settings > Security Settings . |

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