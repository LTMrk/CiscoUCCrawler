---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-mpp-conversion-enterprise-to-mpp-cuip-b-conversion-guide-ipphone--2a6f6cd46e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/MPP-conversion/enterprise-to-mpp/cuip_b_conversion-guide-ipphone/cuip_b_conversion-guide-ipphone_appendix_010.html
retrieved_at: 2026-09-01T15:42:22.995176+00:00
---

Cisco IP Phone 7800 and 8800 Series Migration Guide (On-Premises to Multiplatform Phones)

# Cisco IP Phone 7800 and 8800 Series Migration Guide (On-Premises to Multiplatform Phones)

Find Matches in This Book

## Results

Updated: March 29, 2019

Chapter: Support Information

## Chapter: Support Information

# Support Information

## If You Need Phone Information

### Find the IP Address of the Phone

You can gather information about your phone IP address to help your administrator troubleshoot.

Press Applications .

Select Status > Network Status > . .

View the phone IP address in the IPv4 status or in the IPv6 status fields.

### Find the Current Firmware Load

You can gather information about your phone firmware to help your administrator troubleshoot.

Press Applications .

Select Status > Product Information > Software version to view the firmware version of the phone.

## If You Have Firmware Migration Problems

If you experience problems during the firmware migration, your administrator can help troubleshoot the root cause of the problem.
                           You can gather information to help your administrator troubleshoot.

You can provide the following report to your administrator to help resolve the issues:

Increase the Log Debug Level. See Change the Log Levels

Start capturing ethernet packets, reproduce the problem, and stop the packet capture. Collect the packet captures. See Capture Ethernet Packets

Generate a problem report and download the report with a Problem Report Tool (PRT). See Generate a Problem Report and Download the Problem Reports

Reset the Debug Level to NOTICE . See Change the Log Levels

### Change the Log Levels

By default, the log files capture routine information. When you are troubleshooting problems, you can increase the debug level
                                 to capture detailed logs.

A debug log level of DEBUG can cause delays in the system. Only use DEBUG while you collect logs about a problem and return
                                             the level to NOTICE as soon as possible.

On the phone web page, select Admin Login > Advanced .

Select Voice > System .

In the Optional Network Configuration section, set the Debug Level field to DEBUG .

Click Submit All Changes .

After the detailed log files are captured, set the Debug Level to NOTICE .

Click Submit All Changes .

### Capture Ethernet Packets

The Ethernet packets contain detailed information that can be used to troubleshoot problems.

On the phone web page, select Admin Login > Advanced .

Select Info > Debug Info .

In the Problem Report Tool section, click the Start Packet Capture button in the Packet Capture field.

Choose All to capture all packets that the phone receives and select Host IP Address to capture packets only when source or destination is the IP address of the phone.

Reproduce your problem.

When you want to stop the packet capture, click Stop Packet Capture .

Click Submit .

### Generate a Problem Report

To help troubleshoot the issues that you experience during firmware migration, logs from the Problem Report Tool can be used.
                                 You can generate PRT logs using the phone web page and upload them to a remote log server.

On the phone web page, select Admin Login > Advanced .

Select Info > Debug Info .

In the Problem Reports section, click Generate PRT .

Enter the following information in the Report Problem screen:

Enter the date that you experienced the problem in the Date field. The current date appears in this field by default.

Enter the time that you experienced the problem in the Time field. The current time appears in this field by default.

In the Select Problem drop-down list box, choose the description of the problem from the available options.

Click Submit in the Report Problem screen.

The Submit button is enabled only if you select if you select a value in the Select Problem drop-down list box.

You get a notification alert on the phone web page that indicates if the PRT upload was successful or not.

### Download the Problem Reports

After you generate the problem reports, you need to download the reports to help resolve any issues that you experience during
                                 firmware migration.

On the phone web page, select Admin Login > Advanced .

Select Info > Debug Info .

In the Problem Reports area, click the problem report file to download.

Save the file to your local system and open the file to access the problem reporting logs.

## Additional Information and Help

If you experience problems while running migration firmware, you can factory reset the phone to troubleshoot the problem.
                           To factory reset your phone, perform one of the following instructions.

### Factory Reset the Phone from the Phone Menu

To troubleshoot the phone you can perform a factory reset.

Press Applications .

Select Device Administration .

Select Factory reset and confirm.

### Factory Reset the Phone with the Keypad

Use these steps to reset the phone to factory default settings using the phone keypad.

You have two methods to perform the factory reset by using the keypad:

Method 1 (recommended): Press # > 123456789*0#

Method 2 : Press 0 > 369#

#### Before you begin

You must know if your phone is an original hardware release or if the hardware has been updated and re-released.

Unplug the phone:

- If using PoE, unplug the LAN cable.

- If using the power cube, unplug the power cube.

Wait 5 seconds.

Press and hold # and plug the phone back in.

Do one of the following actions:

Method 1 : Press and hold # and plug the phone back in.

Method 2 : Press and hold 0 and plug the phone back in.

Only the Cisco IP Phone 6821 support the method.

Only the Cisco IP Phone 8845, 8865, 8841, 8851 and 8861 support the method. And the hardware version of Cisco IP Phone 8841,
                                                   8851, and 8861 must be 15 or later.

On earlier hardware versions, the Mute button lights up. Wait for the Mute button to turn off.

Press # , then press 123456789*0# in sequence.

When you press 1 , the lights on the headset button turns off. The light on the Select button flashes when a button is pressed.

After you press these buttons, the phone goes through the factory reset process.

If you press the buttons out of sequence, the phone powers on normally.

Do not power down the phone until it completes the factory reset process, and the main screen appears.

Do one of the following actions:

Method 1 : Press 123456789*0# in sequence.

After you press these buttons, the phone goes through the factory reset process.

If you press the buttons out of sequence, the phone powers on normally.

Do not power down the phone until it completes the factory reset process, and the main screen appears.

Method 2 : Press 369# in sequence.

For Cisco IP Phone 6821, after you press these buttons, the phone still remains on the same screen, and all LEDs change to
                                                   solid green.

After you press these buttons, the phone still remains on the same screen, and all LEDs change to solid green.

For the Cisco IP Phone 8845, 8865, 8841, 8851 and 8861, the phone screen disappears. At the same time, the lights on the Headset,
                                                   Speaker, and Mute are flashing.

If you use the Method 2 , unplug and plug in the phone again to reboot it.

After the phone reboots, the main screen appears.

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Status > Network Status > . . |
| Step 3 | View the phone IP address in the IPv4 status or in the IPv6 status fields. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Status > Product Information > Software version to view the firmware version of the phone. |

| Caution | A debug log level of DEBUG can cause delays in the system. Only use DEBUG while you collect logs about a problem and return
                                             the level to NOTICE as soon as possible. |
|---|---|

| Step 1 | On the phone web page, select Admin Login > Advanced . |
|---|---|
| Step 2 | Select Voice > System . |
| Step 3 | In the Optional Network Configuration section, set the Debug Level field to DEBUG . |
| Step 4 | Click Submit All Changes . |
| Step 5 | After the detailed log files are captured, set the Debug Level to NOTICE . |
| Step 6 | Click Submit All Changes . |

| Step 1 | On the phone web page, select Admin Login > Advanced . |
|---|---|
| Step 2 | Select Info > Debug Info . |
| Step 3 | In the Problem Report Tool section, click the Start Packet Capture button in the Packet Capture field. |
| Step 4 | Choose All to capture all packets that the phone receives and select Host IP Address to capture packets only when source or destination is the IP address of the phone. |
| Step 5 | Reproduce your problem. |
| Step 6 | When you want to stop the packet capture, click Stop Packet Capture . |
| Step 7 | Click Submit . You see a file name link in the Capture File field. This file contains the filtered packets. Click this file name link to download it. |

| Step 1 | On the phone web page, select Admin Login > Advanced . |
|---|---|
| Step 2 | Select Info > Debug Info . |
| Step 3 | In the Problem Reports section, click Generate PRT . |
| Step 4 | Enter the following information in the Report Problem screen: Enter the date that you experienced the problem in the Date field. The current date appears in this field by default. Enter the time that you experienced the problem in the Time field. The current time appears in this field by default. In the Select Problem drop-down list box, choose the description of the problem from the available options. |
| Step 5 | Click Submit in the Report Problem screen. The Submit button is enabled only if you select if you select a value in the Select Problem drop-down list box. You get a notification alert on the phone web page that indicates if the PRT upload was successful or not. |

| Step 1 | On the phone web page, select Admin Login > Advanced . |
|---|---|
| Step 2 | Select Info > Debug Info . |
| Step 3 | In the Problem Reports area, click the problem report file to download. |
| Step 4 | Save the file to your local system and open the file to access the problem reporting logs. |

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device Administration . |
| Step 3 | Select Factory reset and confirm. |

| Step 1 | Unplug the phone: If using PoE, unplug the LAN cable. If using the power cube, unplug the power cube. |
|---|---|
| Step 2 | Wait 5 seconds. |
| Step 3 | Press and hold # and plug the phone back in. |
| Step 4 | Do one of the following actions: Method 1 : Press and hold # and plug the phone back in. Method 2 : Press and hold 0 and plug the phone back in. Only the Cisco IP Phone 6821 support the method. Only the Cisco IP Phone 8845, 8865, 8841, 8851 and 8861 support the method. And the hardware version of Cisco IP Phone 8841,
                                                   8851, and 8861 must be 15 or later. |
| Step 5 | On earlier hardware versions, the Mute button lights up. Wait for the Mute button to turn off. |
| Step 6 | Press # , then press 123456789*0# in sequence. When you press 1 , the lights on the headset button turns off. The light on the Select button flashes when a button is pressed. After you press these buttons, the phone goes through the factory reset process. If you press the buttons out of sequence, the phone powers on normally. Caution Do not power down the phone until it completes the factory reset process, and the main screen appears. | Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
| Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
| Step 7 | Do one of the following actions: Method 1 : Press 123456789*0# in sequence. After you press these buttons, the phone goes through the factory reset process. If you press the buttons out of sequence, the phone powers on normally. Caution Do not power down the phone until it completes the factory reset process, and the main screen appears. Method 2 : Press 369# in sequence. For Cisco IP Phone 6821, after you press these buttons, the phone still remains on the same screen, and all LEDs change to
                                                   solid green. After you press these buttons, the phone still remains on the same screen, and all LEDs change to solid green. For the Cisco IP Phone 8845, 8865, 8841, 8851 and 8861, the phone screen disappears. At the same time, the lights on the Headset,
                                                   Speaker, and Mute are flashing. | Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
| Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
| Step 8 | If you use the Method 2 , unplug and plug in the phone again to reboot it. After the phone reboots, the main screen appears. |

| Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
|---|---|

| Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
|---|---|