---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8821-english-adminguide-w88x-b-wireless-8821-8821ex-admin-guide-w88x--f8ec6bf570
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8821/english/adminguide/w88x_b_wireless-8821-8821ex-admin-guide/w88x_b_wireless-8821-8821ex-admin-guide_chapter_01000.html
retrieved_at: 2026-08-21T01:56:30.764998+00:00
---

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

# Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

Updated: June 28, 2016

Chapter: Maintenance

## Chapter: Maintenance

# Maintenance

## Reboot the Phone

You can reboot the phone to ensure that the configuration is applied to the phone.

Access the Settings app.

Select Admin settings > Reset settings > Reset device .

Press Reset .

### Boot the Phone to the Alternate Firmware

You can reboot the phone to the previous version of the phone firmware. This allows you to temporarily use the previous firmware
                                 load.

When the phone next powers on, it will use the new firmware load.

Press and hold Power/End Call until the phone turns off.

Press and hold Asterisk (*) , and then press and hold Power/End Call .

When the LED changes to red, release the Asterisk (*) and Power/End Call keys.

The phone boots to the previous firmware version.

### Restart the Phone from the Administration Web Page

You can restart the phone from the phone administration web page. Ensure that the user is not on an active call before you
                                 restart the phone.

#### Before you begin

Access the phone administration web page. See Access the Phone Administration Web Page .

Click on the Restart link in the left pane.

Click Restart .

## Phone Reset

You can restore the factory default settings to the phone to clear the current configuration. This restore can be for all
                              values, for the network settings, or for the security settings.

### Reset the Phone to Factory Defaults from the Phone Menu

You can reset the phone to the factory defaults. The phone  resets user and network setup settings to their default values
                                 and then restarts.

Access the Settings app.

Select Admin settings > Reset settings > All settings .

Press Reset .

### Reset the Phone to Factory Defaults from the Phone Keypad

Press and hold Power/End Call until the phone turns off.

Press and hold Pound (#) , and then press and hold Power/End Call .

When the LED changes to amber, release the Pound (#) and Power/End Call keys.

Press 1 2 3 4 5 6 7 8 9 * 0 # .

If the LED blinks green, the factory reset is in progress.

If the LED blinks red, the factory reset was not accepted.

### Reset the Network Settings

You can reset the network settings on the phone to the factory defaults. The phone  resets network setup settings to their
                                 default values and then restarts.

Access the Settings app.

Select Admin settings > Reset settings > Network settings .

Press Reset .

### Reset the Security Settings

You can reset the security settings on the phone to the factory defaults. The phone  resets security settings to their default
                                 values and then restarts.

Access the Settings app.

Select Admin settings > Reset settings > Security settings .

Press Reset .

## Voice Quality Monitoring

To measure the voice quality of calls that are sent and
                           		received within the network, CiscoIP Phones use the following statistical
                           		metrics that are based on concealment events. The DSP plays concealment frames
                           		to mask frame loss in the voice packet stream.

Shows the ratio of concealment frames over
                                 			 total speech frames. An interval conceal ratio is calculated every 3 seconds.

Shows the number of seconds in which the
                                 			 DSP plays concealment frames due to lost frames. A severely "concealed second" is a second in which the DSP plays more than
                                 			 5 percent concealment frames.

Uses a numeric score to estimate the relative voice
                                 			 listening quality. The phone calculates the mean opinion score
                                 			 (MOS) for listening quality (LQK) based audible concealment events due to frame
                                 			 loss in the preceding 8 seconds, and includes perceptual weighting factors such
                                 			 as codec type and frame size.

MOS LQK scores are produced by a Cisco proprietary algorithm, Cisco
                                 			 Voice Transmission Quality (CVTQ) index. Depending on the MOS LQK version
                                 			 number, these scores might be compliant with the International
                                 			 Telecommunications Union (ITU) standard P.564. This standard defines evaluation
                                 			 methods and performance accuracy targets that predict listening quality scores
                                 			 based on observation of actual network impairment.

Concealment ratio and concealment seconds are primary measurements
                                       		  based on frame loss while MOS LQK scores project a "human-weighted" version of the same information on a scale from 5
                                       		  (excellent) to 1 (bad) for measuring listening quality.

Listening quality scores (MOS LQK) relate to the clarity or
                           		sound of the received voice signal. Conversational quality scores (MOS CQ such
                           		as G.107) include impairment factors, such as delay, that degrade the natural
                           		flow of conversation.

For information about configuring voice quality metrics for
                           		phones, see the 
                           		phone metrics sections in the Cisco Unified Communications Manager documents.

You can access voice quality metrics on the phone or remotely by using
                           		Streaming Statistics.

### Voice Quality Metrics

To use the metrics for monitoring voice quality, note the typical scores under normal conditions of zero packet loss and use
                              the metrics as a baseline for comparison.

It is important to distinguish significant changes from random changes in metrics. Significant changes are scores that change
                              about 0.2 MOS or greater and persist in calls that last longer than 30 seconds. Conceal Ratio changes should indicate greater
                              than 3 percent frame loss.

MOS LQK scores can vary based on the codec that the phone uses. The following codecs provide these MOS LQK scores under normal
                              conditions with zero frame loss:

G.711 and G.722 codecs have maximum scores of 4.5

G.729A/AB codec has a maximum score of 3.8

A Conceal Ratio of zero indicates that the IP network is delivering frames and packets on time with no loss.

### Voice Quality Troubleshooting Tips

When you observe significant and persistent changes to
                                 		  metrics, use the following table for general troubleshooting information.

Metric change

Condition

MOS LQK scores decrease significantly

Network impairment from packet loss or high jitter:

- Average MOS LQK
                                                						decreases could indicate widespread and uniform impairment.

- Individual MOS LQK
                                                						decreases indicate bursty impairment.

Cross-check with Conceal Ratio and Conceal Seconds
                                             					 for evidence of packet loss and jitter.

MOS LQK scores decrease significantly

- Check to see if
                                                						the phone is using a different codec than expected (Sender Codec and Rcvr Codec).

- Check to see if
                                                						the MOS LQK version changed after a firmware upgrade.

Conceal Ratio and Conceal Seconds increase
                                             					 significantly

- Network impairment
                                                						from packet loss or high jitter.

Conceal Ratio is near or at zero, but the voice
                                             					 quality is poor

- Noise or
                                                						distortion in the audio channel such as echo or audio levels.

- Tandem calls that
                                                						undergo multiple encode/decode such as calls to a cellular network or calling
                                                						card network.

- Acoustic problems
                                                						coming from a speakerphone, hands-free cellular phone or wireless headset.

Check packet transmit (TxCnt) and packet receive
                                             					 (RxCnt) counters to verify that voice packets are flowing.

Voice quality metrics do not account for noise or distortion, only
                                             			 frame loss.

## Manage Core Dumps from the Admin Web Page

You can generate or delete the Java core dump log with the admin web page.

Only one core dump can be stored on the phone. The phone retains the core dump until it reboots. If a new core dump is created,
                              the previous one is overwritten.

### Before you begin

Connect to the admin web page. For more information, see Access the Phone Administration Web Page .

Click Device logs > Core dumps .

Click Generate java core & heap dump .

(Optional) Click Delete to delete the core dump file.

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Admin settings > Reset settings > Reset device . |
| Step 3 | Press Reset . |

| Step 1 | Press and hold Power/End Call until the phone turns off. |
|---|---|
| Step 2 | Press and hold Asterisk (*) , and then press and hold Power/End Call . |
| Step 3 | When the LED changes to red, release the Asterisk (*) and Power/End Call keys. The phone boots to the previous firmware version. |

| Step 1 | Click on the Restart link in the left pane. |
|---|---|
| Step 2 | Click Restart . |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Admin settings > Reset settings > All settings . |
| Step 3 | Press Reset . |

| Step 1 | Press and hold Power/End Call until the phone turns off. |
|---|---|
| Step 2 | Press and hold Pound (#) , and then press and hold Power/End Call . |
| Step 3 | When the LED changes to amber, release the Pound (#) and Power/End Call keys. |
| Step 4 | Press 1 2 3 4 5 6 7 8 9 * 0 # . If the LED blinks green, the factory reset is in progress. If the LED blinks red, the factory reset was not accepted. |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Admin settings > Reset settings > Network settings . |
| Step 3 | Press Reset . |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Admin settings > Reset settings > Security settings . |
| Step 3 | Press Reset . |

| Note | Concealment ratio and concealment seconds are primary measurements
                                       		  based on frame loss while MOS LQK scores project a "human-weighted" version of the same information on a scale from 5
                                       		  (excellent) to 1 (bad) for measuring listening quality. |
|---|---|

| Metric change | Condition |
|---|---|
| MOS LQK scores decrease significantly | Network impairment from packet loss or high jitter: Average MOS LQK
                                                						decreases could indicate widespread and uniform impairment. Individual MOS LQK
                                                						decreases indicate bursty impairment. Cross-check with Conceal Ratio and Conceal Seconds
                                             					 for evidence of packet loss and jitter. |
| MOS LQK scores decrease significantly | Check to see if
                                                						the phone is using a different codec than expected (Sender Codec and Rcvr Codec). Check to see if
                                                						the MOS LQK version changed after a firmware upgrade. |
| Conceal Ratio and Conceal Seconds increase
                                             					 significantly | Network impairment
                                                						from packet loss or high jitter. |
| Conceal Ratio is near or at zero, but the voice
                                             					 quality is poor | Noise or
                                                						distortion in the audio channel such as echo or audio levels. Tandem calls that
                                                						undergo multiple encode/decode such as calls to a cellular network or calling
                                                						card network. Acoustic problems
                                                						coming from a speakerphone, hands-free cellular phone or wireless headset. Check packet transmit (TxCnt) and packet receive
                                             					 (RxCnt) counters to verify that voice packets are flowing. |

| Note | Voice quality metrics do not account for noise or distortion, only
                                             			 frame loss. |
|---|---|

| Step 1 | Click Device logs > Core dumps . |
|---|---|
| Step 2 | Click Generate java core & heap dump . |
| Step 3 | (Optional) Click Delete to delete the core dump file. |