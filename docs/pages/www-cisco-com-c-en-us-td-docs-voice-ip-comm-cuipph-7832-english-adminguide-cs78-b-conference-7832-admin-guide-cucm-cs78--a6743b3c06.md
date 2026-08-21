---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7832-english-adminguide-cs78-b-conference-7832-admin-guide-cucm-cs78--a6743b3c06
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7832/english/adminguide/cs78_b_conference-7832-admin-guide-cucm/cs78_b_conference-7832-admin-guide-cucm_chapter_01000.html
retrieved_at: 2026-08-21T13:27:40.616954+00:00
---

Cisco IP Conference Phone 7832 Administration Guide for Cisco Unified Communication Manager

# Cisco IP Conference Phone 7832 Administration Guide for Cisco Unified Communication Manager

Updated: November 6, 2025

Chapter: Maintenance

## Chapter: Maintenance

# Maintenance

## Restart or Reset the Conference Phone

You perform a basic reset of a phone
                              		  to recover if the phone experiences an error. You can also restore configuration and security settings to factory default
                              settings.

### Restart the Conference Phone

When you restart the phone, any user and network setup changes that aren't committed to the flash memory in the phone are
                                 lost.

Press Settings > Admin Settings > Reset settings > Reset device .

### Reset the Conference Phone Settings from the Phone Menu

Step 1

Press Settings .

Step 2

Choose Admin Settings > Reset Settings .

Step 3

Select the type of reset.

- All —Restores the factory settings.

- Reset device —Resets the device. The existing settings don't change.

- Network —Resets the network configuration to default settings.

- Service mode —Clears the current service mode, deactivates the VPN and restarts the phone.

- Security —Resets the security configuration to default settings. This option deletes the CTL file.

Step 4

Press Reset or Cancel .

### Reset the Conference Phone to Factory Defaults from the Keypad

When you reset the phone from the keypad, the phone reverts to the factory settings.

Step 1

Unplug the
                                          			 phone:

- If using PoE, unplug the
                                             				LAN cable.

- If using the power cube, unplug the power cube.

Step 2

Wait 5
                                          			 seconds.

Step 3

Press and hold # , and plug the phone back in.

Step 4

When the phone boots up, the LED strip lights up. As soon as the LED strip turns on, press 123456789*0# in sequence.

After you press these buttons, the phone goes through the factory reset process.

If you press the buttons out of sequence, the phone powers on normally.

Caution

Do not power down the phone until it completes the factory reset process, and the main screen appears.

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

| Press Settings > Admin Settings > Reset settings > Reset device . |
|---|

| Step 1 | Press Settings . |
|---|---|
| Step 2 | Choose Admin Settings > Reset Settings . |
| Step 3 | Select the type of reset. All —Restores the factory settings. Reset device —Resets the device. The existing settings don't change. Network —Resets the network configuration to default settings. Service mode —Clears the current service mode, deactivates the VPN and restarts the phone. Security —Resets the security configuration to default settings. This option deletes the CTL file. |
| Step 4 | Press Reset or Cancel . |

| Step 1 | Unplug the
                                          			 phone: If using PoE, unplug the
                                             				LAN cable. If using the power cube, unplug the power cube. |
|---|---|
| Step 2 | Wait 5
                                          			 seconds. |
| Step 3 | Press and hold # , and plug the phone back in. |
| Step 4 | When the phone boots up, the LED strip lights up. As soon as the LED strip turns on, press 123456789*0# in sequence. After you press these buttons, the phone goes through the factory reset process. If you press the buttons out of sequence, the phone powers on normally. Caution Do not power down the phone until it completes the factory reset process, and the main screen appears. | Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
| Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |

| Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
|---|---|

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