---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-english-adminguide-administration-pa2d-b-7800-mpp-ag-11-pa2d-659227f30c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/english/adminguide/administration/pa2d_b_7800-mpp-ag-11/pa2d_b_7800-mpp-ag-11_chapter_01101.html
retrieved_at: 2026-09-01T15:41:53.569714+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

# Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Updated: April 29, 2019

Chapter: Maintenance

## Chapter: Maintenance

# Maintenance

## Basic Reset

Performing a basic reset of a Cisco IP Phone provides a way to recover when the phone experiences an error. The reset provides
                              a way to reset or restore various configuration and security settings.

When you set up emergency calls, the phone requests an updated location whenever a person performs a phone restart.

The following table describes the ways to perform a basic reset. You can reset a phone with any of these operations after
                              the phone has started up. Choose the operation that is applicable for your situation.

Operation

Action

Explanation

Restart phone

Press Applications and choose Admin Settings > Restart .

Resets any user and network setup changes that you have made, to the previously saved settings that the phone has not written
                                          to its flash memory. The phone then restarts.

Reset settings

To reset settings, press Applications and choose Admin Settings > Factory Reset .

Restores the phone configuration or settings to factory default.

When an administrator has set up emergency calls, the phone requests an updated location whenever the administrator does the
                                          following actions:

Registers the phone with the call server.

Restarts the phone (phone is registered).

Changes the network interface that is used for the SIP registration.

Changes the IP address of the phone.

### Factory Reset the Phone with the Keypad

Use
                                 		  these steps to reset the phone to factory default settings using the phone
                                 		  keypad.

Unplug the
                                          			 phone:

- If using PoE, unplug the
                                             				LAN cable.

- If using the power cube,
                                             				unplug the power cube.

Wait 5
                                          			 seconds.

Press and hold # and plug the phone back in.

When the phone boots up, the headset button, the speaker button, and the mute button light up. When the light on the Mute
                                          button turns off, press the 123456789*0# keys in sequence.

When you press 1 , the lights on the headset button turns off. The light on the Select button flashes when a button is pressed.

After you press these buttons, the phone goes through the factory reset process.

If you press the buttons out of sequence, the phone powers on normally.

Do not power down the phone until it completes the factory reset process, and the main screen appears.

### Perform Factory Reset from Phone Menu

Press Applications .

Select Device administration > Factory reset .

Scroll to Admin Settings > Reset Settings , and select All .

To restore phone configuration or settings to factory default, press OK .

### Factory Reset the Phone from Phone Web Page

You can restore your phone to its original manufacturer settings from the phone web page. After you reset the phone, you can
                                 reconfigure it.

Reset your phone from the phone web page from one of the methods:

You can enter URL in the format:

where:

Phone IP = actual IP address of your phone.

/admin = path to access admin page of your phone.

factory-reset = command that you need to enter in the phone web page to factory-reset your phone.

- On the phone web page, select Admin Login > Advanced > Info > Debug Info .Click Factory Reset in the Factory Reset section and confirm the factory reset message in the next screen. Click Submit All Changes .

### Identify Phone Issues with a URL in the Phone Web Page

When the phone doesn't work or doesn't register, a network error or any misconfiguration might be the cause. To identify the
                                 cause, add a specific IP address or a domain name to the phone admin page. Then, try to access so that the phone can ping
                                 the destination and display the cause.

In a supported web browser, enter a URL that consists of your phone IP address and the destination IP that you want to ping.
                                          Enter the URL using the format:

http:/<Phone IP>/admin/ping?<ping destination> , where:

<Phone IP> = actual IP address of your phone.

/admin = path to the access admin page of your phone.

<ping destination> = any IP address or domain name that you want to ping.

The ping destination allows only alphanumeric characters, ‘-’, and “_” (underscores). Otherwise the phone shows an error on
                                             the web page. If the <ping destination> includes spaces, the phone uses only the first part of the address as the pinging destination.

For example, to ping the 192.168.1.1 address:

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

## Voice Quality Reporting

You can capture voice quality metrics for Voice over Internet Protocol (VoIP) sessions with a Session Initiation Protocol
                           (SIP) event package. Voice call quality information derived from RTP and call information from SIP is conveyed from a User
                           Agent (UA) in a session (reporter) to a third party (collector).

The Cisco IP phone uses User Datagram Protocol (UDP) to send a SIP PUBLISH message to a collector server.

### Supported Scenarios for Voice Quality Reporting

Currently, only the basic call scenario supports voice quality reporting. A basic call can be a peer to peer incoming or
                              outgoing call. The phone supports periodic SIP publish message.

### Mean Opinion Scores and Codecs

The voice quality metrics use Mean Opinion Score (MOS) to rate the quality. A MOS rating of 1 is the lowest quality; a MOS
                              rating of 5 is the highest quality. The following table gives a description of some of the codecs and MOS scores. The phone
                              supports all codecs. For all codecs, the phone sends the SIP Publish message.

Codec

Complexity and Description

MOS

Minimum Call Duration for Valid MOS Value

G.711 (A-law and u-law)

Very low complexity. Supports uncompressed 64 kbps digitized voice transmission at one to ten 5 ms voice frames-per-packet.
                                          This codec provides the highest voice quality and uses the most bandwidth of any of the available codecs.

A minimum value of 4.1 indicates good voice quality.

10 seconds

G.729A

Low to medium complexity.

A minimum value of 3.5 indicates good voice quality.

30 seconds

G.729AB

Contains the same reduced complexity modifications present in the G.729A.

A minimum value of 3.5 indicates good voice quality.

30 seconds

### Configure Voice Quality Reporting

You can enable voice quality reporting on the phone with the web interface. Each extension on a phone has a separate voice
                                 quality report.  For each extension on the phone, use the corresponding Voice Quality Report Address field to configure the generation of voice quality report.

On the Phone Web  page, select Admin Login > advanced > Voice > Ext x .

Ext x = the extension number on the phone

In SIP Settings , enter a value in the Voice Quality Report Address x field. You can enter either a domain name or an IP address in this field.

You can also add a port number along with the domain name or an IP address in this field. If you do not enter a port number,
                                             the value of the SIP UDP Port (5060) is used by default. If the collector server URL parameter is blank, a SIP PUBLISH message is not sent out.

Click Submit All Changes .

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

## View Phone Information

To check the current status of the Cisco IP Phone, click the Info tab.

The Info tab shows information about all phone extensions, including phone statistics and the registration status.

## Reboot Reasons

The phone stores the most recent five reasons that the phone was refreshed or rebooted. When the phone is reset to factory
                              defaults, this information is deleted.

The following table describes the reboot and refresh reasons for the Cisco IP Phone.

Reason

Description

Upgrade

The reboot was a result of an upgrade operation (regardless whether the upgrade completed or failed).

Provisioning

The reboot was the result of changes made to parameter values by using the IP phone screen or phone web user interface, or
                                          as a result of synchronization.

SIP Triggered

The reboot was triggered by a SIP request.

RC

The reboot was triggered as a result of remote customization.

User Triggered

The user manually triggered a cold reboot.

IP Changed

The reboot was triggered after the phone IP address changed.

You can view the reboot history as follows:

From the phone web user interface

From the IP phone screen

From the phone Status Dump file (http:// phoneIP /status.xml or http:// phoneIP /admin/status.xml)

### Reboot History on the Phone Web User Interface

On the Info > System Status page, the Reboot History section displays the device reboot history, the five most recent reboot dates and times, and a reason for the reboot. Each
                                 field displays the reason for the reboot and a time stamp that indicates when the reboot took place.

For example:

```
Reboot Reason 1: [08/13/14 06:12:38] User Triggered
Reboot Reason 2: [08/10/14 10:30:10] Provisioning
Reboot Reason 3: [08/10/14 10:28:20] Upgrade
```

The reboot history displays in reverse chronological order; the reason for the most recent reboot displays in Reboot Reason 1 .

### Reboot History on the Cisco IP Phone Screen

Reboot History is located under Apps > Admin Settings > Status menu. In the Reboot History window, the reboot entries displays in reverse chronological order, similar to the sequence that
                                 displays on the phone web user interface.

### Reboot History in the Status Dump File

The reboot history is stored in the Status Dump file  (http:// <phone_IP_address> /admin/status.xml).

In this file, tags Reboot_Reason_1 to Reboot_Reason_3 store the reboot history, as shown in this example:

```
<Reboot_History>
<Reboot_Reason_1>[08/10/14 14:03:43]Provisioning</Reboot_Reason_1>
<Reboot_Reason_2>[08/10/14 13:58:15]Provisioning</Reboot_Reason_2>
<Reboot_Reason_3>[08/10/14 12:08:58]Provisioning</Reboot_Reason_3>
<Reboot_Reason_4>
<Reboot_Reason_5>
<Reboot_History/>
```

## Phone Behavior During Times of Network Congestion

Anything that degrades network performance can affect Cisco IP Phone voice and video quality, and in some cases, can cause
                              a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that occur on your network, such as a Denial of Service attack

To reduce or eliminate any adverse effects to the phones, schedule administrative network tasks during a time when the phones
                              are not being used or exclude the phones from testing.

| Note | When you set up emergency calls, the phone requests an updated location whenever a person performs a phone restart. |
|---|---|

| Operation | Action | Explanation |
|---|---|---|
| Restart phone | Press Applications and choose Admin Settings > Restart . | Resets any user and network setup changes that you have made, to the previously saved settings that the phone has not written
                                          to its flash memory. The phone then restarts. |
| Reset settings | To reset settings, press Applications and choose Admin Settings > Factory Reset . | Restores the phone configuration or settings to factory default. |

| Note | When an administrator has set up emergency calls, the phone requests an updated location whenever the administrator does the
                                          following actions: Registers the phone with the call server. Restarts the phone (phone is registered). Changes the network interface that is used for the SIP registration. Changes the IP address of the phone. |
|---|---|

| Step 1 | Unplug the
                                          			 phone: If using PoE, unplug the
                                             				LAN cable. If using the power cube,
                                             				unplug the power cube. |
|---|---|
| Step 2 | Wait 5
                                          			 seconds. |
| Step 3 | Press and hold # and plug the phone back in. |
| Step 4 | When the phone boots up, the headset button, the speaker button, and the mute button light up. When the light on the Mute
                                          button turns off, press the 123456789*0# keys in sequence. |
| Step 5 | When you press 1 , the lights on the headset button turns off. The light on the Select button flashes when a button is pressed. After you press these buttons, the phone goes through the factory reset process. If you press the buttons out of sequence, the phone powers on normally. Caution Do not power down the phone until it completes the factory reset process, and the main screen appears. | Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
| Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |

| Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Factory reset . |
| Step 3 | Scroll to Admin Settings > Reset Settings , and select All . |
| Step 4 | To restore phone configuration or settings to factory default, press OK . |

| Reset your phone from the phone web page from one of the methods: Enter the URL in a supported web browser and click Confirm Factory Reset . You can enter URL in the format: http://<Phone IP>/admin/factory-reset where: Phone IP = actual IP address of your phone. /admin = path to access admin page of your phone. factory-reset = command that you need to enter in the phone web page to factory-reset your phone. On the phone web page, select Admin Login > Advanced > Info > Debug Info .Click Factory Reset in the Factory Reset section and confirm the factory reset message in the next screen. Click Submit All Changes . |
|---|

| In a supported web browser, enter a URL that consists of your phone IP address and the destination IP that you want to ping.
                                          Enter the URL using the format: http:/<Phone IP>/admin/ping?<ping destination> , where: <Phone IP> = actual IP address of your phone. /admin = path to the access admin page of your phone. <ping destination> = any IP address or domain name that you want to ping. The ping destination allows only alphanumeric characters, ‘-’, and “_” (underscores). Otherwise the phone shows an error on
                                             the web page. If the <ping destination> includes spaces, the phone uses only the first part of the address as the pinging destination. For example, to ping the 192.168.1.1 address: http://<Phone IP>/admin/ping?192.168.1.1 |
|---|

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

| Codec | Complexity and Description | MOS | Minimum Call Duration for Valid MOS Value |
|---|---|---|---|
| G.711 (A-law and u-law) | Very low complexity. Supports uncompressed 64 kbps digitized voice transmission at one to ten 5 ms voice frames-per-packet.
                                          This codec provides the highest voice quality and uses the most bandwidth of any of the available codecs. | A minimum value of 4.1 indicates good voice quality. | 10 seconds |
| G.729A | Low to medium complexity. | A minimum value of 3.5 indicates good voice quality. | 30 seconds |
| G.729AB | Contains the same reduced complexity modifications present in the G.729A. | A minimum value of 3.5 indicates good voice quality. | 30 seconds |

| Step 1 | On the Phone Web  page, select Admin Login > advanced > Voice > Ext x . Where: Ext x = the extension number on the phone |
|---|---|
| Step 2 | In SIP Settings , enter a value in the Voice Quality Report Address x field. You can enter either a domain name or an IP address in this field. You can also add a port number along with the domain name or an IP address in this field. If you do not enter a port number,
                                             the value of the SIP UDP Port (5060) is used by default. If the collector server URL parameter is blank, a SIP PUBLISH message is not sent out. |
| Step 3 | Click Submit All Changes . |

| To check the current status of the Cisco IP Phone, click the Info tab. The Info tab shows information about all phone extensions, including phone statistics and the registration status. |
|---|

| Reason | Description |
|---|---|
| Upgrade | The reboot was a result of an upgrade operation (regardless whether the upgrade completed or failed). |
| Provisioning | The reboot was the result of changes made to parameter values by using the IP phone screen or phone web user interface, or
                                          as a result of synchronization. |
| SIP Triggered | The reboot was triggered by a SIP request. |
| RC | The reboot was triggered as a result of remote customization. |
| User Triggered | The user manually triggered a cold reboot. |
| IP Changed | The reboot was triggered after the phone IP address changed. |