---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-6800-english-ag-p680-b-6800-mpp-ag-new-p680-b-6800-mpp-adminguide-b71b9da112
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/6800/english/AG/p680_b_6800-mpp-ag_new/p680_b_6800-mpp-adminguide_chapter_010010.html
retrieved_at: 2026-08-21T23:16:38.737824+00:00
---

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide for Release 11.3(1) and Later

# Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide for Release 11.3(1) and Later

Updated: November 21, 2019

Chapter: Maintenance

## Chapter: Maintenance

# Maintenance

## Basic Reset

Performing a basic reset of a Cisco IP Phone provides a way to recover when the phone experiences an error. The reset provides
                              a way to reset or restore various configuration and security settings.

When you set up emergency calls, the phone requests an updated location whenever a person restarts the phone.

The following table describes the ways to perform a basic reset. You can reset a phone with any of these operations after
                              the phone has started up. Choose the operation that is applicable for your situation.

Operation

Action

Explanation

Restart phone

Press Services , Applications , or Directories and then press **#** .

Resets any user and network setup changes that you have made,
                                          					 but that the phone has not written to its Flash memory, to previously saved
                                          					 settings, then restarts the phone.

Reset settings

Restores phone configuration or settings to factory default.

To reset settings, press Applications > Admin Settings > Custom Reset .

Restores phone configuration or settings to noncustomized default.

When you set up emergency calls, the phone requests an updated location whenever the you do the following actions:

Registers the phone with the call server.

Restarts the phone (phone is registered).

Changes the network interface that is used for the SIP registration.

Changes the IP address of the phone.

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

Do one of the following actions:

Method 1 : Press and hold # and plug the phone back in.

Method 2 : Press and hold 0 and plug the phone back in.

Only the Cisco IP Phone 6821 support the method.

On earlier hardware versions, the Mute button lights up. Wait for the Mute button to turn off.

Do one of the following actions:

Method 1 : Press 123456789*0# in sequence.

When you press 1 , the lights on the headset button turns off. The light on the Select button flashes when a button is pressed.

After you press these buttons, the phone goes through the factory reset process.

If you press the buttons out of sequence, the phone powers on normally.

Do not power down the phone until it completes the factory reset process, and the main screen appears.

Method 2 : Press 369# in sequence.

For Cisco IP Phone 6821, after you press these buttons, the phone still remains on the same screen, and all LEDs change to
                                                   solid green.

If you use the Method 2 , unplug and plug in the phone again to reboot it.

After the phone reboots, the main screen appears.

### Perform Factory Reset from Phone Menu

Press Applications .

Select Device administration > Factory reset .

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

| Note | When you set up emergency calls, the phone requests an updated location whenever a person restarts the phone. |
|---|---|

| Operation | Action | Explanation |
|---|---|---|
| Restart phone | Press Services , Applications , or Directories and then press **#** . | Resets any user and network setup changes that you have made,
                                          					 but that the phone has not written to its Flash memory, to previously saved
                                          					 settings, then restarts the phone. |
| Reset settings |  | Restores phone configuration or settings to factory default. |
| To reset settings, press Applications > Admin Settings > Custom Reset . | Restores phone configuration or settings to noncustomized default. |

| Note | When you set up emergency calls, the phone requests an updated location whenever the you do the following actions: Registers the phone with the call server. Restarts the phone (phone is registered). Changes the network interface that is used for the SIP registration. Changes the IP address of the phone. |
|---|---|

| Step 1 | Unplug the phone: If using PoE, unplug the LAN cable. If using the power cube, unplug the power cube. |
|---|---|
| Step 2 | Wait 5 seconds. |
| Step 3 | Do one of the following actions: Method 1 : Press and hold # and plug the phone back in. Method 2 : Press and hold 0 and plug the phone back in. Only the Cisco IP Phone 6821 support the method. The phone begins the reboot process. The headset button and the speaker button light up. |
| Step 4 | On earlier hardware versions, the Mute button lights up. Wait for the Mute button to turn off. |
| Step 5 | Do one of the following actions: Method 1 : Press 123456789*0# in sequence. When you press 1 , the lights on the headset button turns off. The light on the Select button flashes when a button is pressed. After you press these buttons, the phone goes through the factory reset process. If you press the buttons out of sequence, the phone powers on normally. Caution Do not power down the phone until it completes the factory reset process, and the main screen appears. Method 2 : Press 369# in sequence. For Cisco IP Phone 6821, after you press these buttons, the phone still remains on the same screen, and all LEDs change to
                                                   solid green. | Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
| Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
| Step 6 | If you use the Method 2 , unplug and plug in the phone again to reboot it. After the phone reboots, the main screen appears. |

| Caution | Do not power down the phone until it completes the factory reset process, and the main screen appears. |
|---|---|

| Step 1 | Press Applications . |
|---|---|
| Step 2 | Select Device administration > Factory reset . |
| Step 3 | To restore phone configuration or settings to factory default, press OK . |

| Reset your phone from the phone web page from one of the methods: Enter the URL in a supported web browser and click Confirm Factory Reset . You can enter URL in the format: http://<Phone IP>/admin/factory-reset where: Phone IP = actual IP address of your phone. /admin = path to access admin page of your phone. factory-reset = command that you need to enter in the phone web page to factory-reset your phone. On the phone web page, select Admin Login > Advanced > Info > Debug Info .Click Factory Reset in the Factory Reset section and confirm the factory reset message in the next screen. Click Submit All Changes . |
|---|

| In a supported web browser, enter a URL that consists of your phone IP address and the destination IP that you want to ping.
                                          Enter the URL using the format: http:/<Phone IP>/admin/ping?<ping destination> , where: <Phone IP> = actual IP address of your phone. /admin = path to the access admin page of your phone. <ping destination> = any IP address or domain name that you want to ping. The ping destination allows only alphanumeric characters, ‘-’, and “_” (underscores). Otherwise the phone shows an error on
                                             the web page. If the <ping destination> includes spaces, the phone uses only the first part of the address as the pinging destination. For example, to ping the 192.168.1.1 address: http://<Phone IP>/admin/ping?192.168.1.1 |
|---|