---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-firmware-11-1-2sr1-p881-b-rn-11-1-2-sr1-html-79194207ac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/firmware/11-1-2sr1/p881_b_rn_11-1-2-sr1.html
retrieved_at: 2026-08-21T13:45:08.709683+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(2)SR1

# Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(2)SR1

### Download Options

Updated: August 3, 2018

First Published: August 3, 2018

# Release Notes

Use these release notes with the following Cisco IP Phone 8800 Series Multiplatform Phones running SIP firmware release 11.1(2)SR1.

Cisco IP Phone 8811, 8841, 8851, and 8861 Multiplatform Phones

Cisco IP Phone 8845 and 8865 Multiplatform Phones

The following table describes the individual phone requirements.

Phone

Support Server

Cisco IP Phone 8800 Series Multiplatform Phones

BroadSoft BroadWorks 22.0

MetaSphere CFS version 9.4

Asterisk 11.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone 8800 Series Documentation

Refer to
                        		  publications that are specific to your language, phone model, and call control
                        		  system. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-8800-series/index.html

The Deployment Guide is located at the following URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-implementation-design-guides-list.html

New and Changed Features

## New Domain Support while Provisioning

When a phone connects to a network for the first time or after a factory reset, if there are no DHCP options setup, it contacts
                     a device activation server for zero touch provisioning. Starting with this firmware release, phones will use activate.cisco.com instead of webapps.cisco.com for provisioning. Phones with older versions of the firmware will continue to use webapps.cisco.com . Cisco recommends that you allow both the domain names through your firewall.

### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Provisioning Guide

## Upgrade the Firmware

Two firmware images are available for Cisco IP Phone 8800 Series Multiplatform Phones :

Firmware for Cisco IP Phone 8811, 8841, 8851, and 8861 Multiplatform Phones (Audio only)

Firmware for Cisco IP Phone 8845 and 8865 Multiplatform Phones (Video)

After the firmware upgrade completes, the phone reboots automatically.

Click the following URL:

https://software.cisco.com/download/home/286311392

In the middle pane, select IP Phone 8800 Series With Multiplatform Firmware .

Select your phone model in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

On the next page that is displayed, in the All Releases > MPP v11 folder, select 11.1.2 MSR1-1 .

(Optional) Place your mouse pointer on the file name in the right pane, to see the file details and checksum values.

Download the file:

For Cisco IP Phone 8811, 8841, 8851, and 8861 Multiplatform Phones: cp-88xx.11-1-2MSR1-1_REL.zip

For Cisco IP Phone 8845 and 8865 Multiplatform Phones: cp-8845_65.11-1-2MSR1-1_REL.zip

Click Accept License Agreement .

Unzip the files.

Place the files in the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the upgrade.

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced > Voice > Provisioning tab, Firmware Upgrade section. In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads

Example:

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads

Example:

```
https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/ sip88xx.11-1-2MSR1-1.loads
```

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call
                        to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

### No Beep Sound Heard when the Mute Key is Pressed

When you press the Mute button during a call, you may not hear a beep sound. For anyone who is visually impaired, press the Mute button once to mute the phone and press the button twice to unmute the phone.

### Phone Has a Firmware Build Earlier than 11.0.0

Sometimes, a phone taken out of the box has a firmware build earlier than 11.0.0. When this happens, you must upgrade the
                        firmware on your phone to 11.0.0. Then you must update to 11.1.1 or later before you provision it.

Caveats

## View Caveats

You can search for caveats using the Cisco Bug Search tool.

Known caveats (bugs) are graded according to severity level, and are either open or resolved.

Before you begin

### Before you begin

To view the caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

To find all caveats, use this URL:

To find all open caveats, use this URL:

To find all resolved caveats, use this URL:

When prompted, log in with your Cisco.com user ID and password.

(Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

## Open Caveats

The following list contains the severity 1, 2, and 3 caveats that are open for the Cisco IP Phone 8800 Series Multiplatform Phones that use the firmware release 11.1(2)SR1.

This list reflects a snapshot of the caveats that were open at the time this report was compiled. The status of caveats may
                     have changed since then. For an updated view of the open caveats, or to view details or history for specific caveats, access
                     the Bug Search Toolkit as described in View Caveats . You must be a registered Cisco.com user to access this information.

CSCvi30334 Phones fail to configure more than 21 key expansion module keys to SD+BLF with a 1000M switch. [8841 and 8851 only]

CSCvi31149 Phone switch from VLAN with IPv6 to VLAN without IPv6, unexpectedly, IPv6 status is still shown OK.

CSCvi36532 Key expansion module not powering up under special environment

CSCvi39946 Phone screen LCD can add maximum of 64 character voicemail description, but on a phone web page can only add 63
                           characters.

CSCvi40419 Phone cannot display the call forward logo set with the start codes (*72). [8845 and 8865 only]

CSCvi43542 Active call is held when quickly ending an incoming page.

CSCvi45913 No audio when the number of secure calls exceeds 50 and RTP port count is less than 100.

CSCvi45988 Pressing a digit hard key does not wake up the screen after receiving an XML file with PhoneExecute.

CSCvi47963 Phone still displays the missed call icon and shortcut, deletes the call history, after receiving an XML file.

CSCvi62072 Incoming paging cannot end when receiving two paging calls.

CSCvi64969 Phone connects to switch port which without configured any VLAN, it displays a duplicate IPv6 address message.

CSCvi67248 Phone displays connection successfully (DHCP pool full) when no IP address obtained on wireless.

CSCvi67452 Phone prompts with message Ethernet must be ..., which has no cable connected when you select Wi-Fi configure.
                           [8845 and 8865 only]

CSCvi67535 Speak dial tone uses same volume with headset after ending a headset call (sharedline only).

CSCvi67698 User can input Extension Mobility (EM) sign-in password using special characters, without any limitation.

CSCvi67969 Sometimes the phone exits the Accessory Unsupported menu when you plug in a Cisco 531 or 532 headset.

CSCvi71664 The call ends if you press Return hard key and Cancel softkey after using an active DND with a star code.

CSCvi71678 In the Extensin Mobility (EM) sign-in window, no response to phone screen LED if you insert a Cisco 531 or 532
                           headset and receive a shared line incoming call.

CSCvi71940 A paging call cannot end when you dial the second paging call using the Personal directory.

CSCvi72074 No ringtone setting works for a directory entry after you cancel the second incoming call.

CSCvi72138 Using the XML Directory service, phone always displays the first directory entry username when dialing an invalid
                           number

CSCvi72223 Resync using autoconfig IPv6 IP address did not use DHCP IPv6 IP address. [8845 only]

CSCvi73581 Call failing when the TCP/TLS connection fails back to the primary server and does not register.

CSCvi76113 Cannot provision a phone from the phone web when the Upgrade Error Retry Delay is too short and the upgrade fails.

CSCvi76658 Line status PLK LED does not change to red when an in-dialog subscription fails.

CSCvi77714 An outgoing N-Way conference call is rolling over to extension 2.

CSCvi78340 When editing a call number, navigate to the left, then Return to the previous softkey page. Move right no longer
                           works.

CSCvi78547 Phone screen LCD has no response and web GUI cannot access. Caused by provisioning the phone with 1600 contacts
                           in an XML file.

CSCvi79560 Phone creen LCD: Incoming call page pops up frequently while using an electronic hookswitch (EHS) button init call,
                           phone connects BT or USB headset.

CSCvi80805 Report rule isn't sent occasionally.

CSCvi81189 Phone UI is stuck after configuring the XML service with 1600 contacts and having an invalid file format.

CSCvi81263 Password rule from LCD screen is not the same as on the phone web page.

CSCvi87525 Phone reboots when downloading a large profile and generates a PRT at same time.

CSCvi87566 Enable SCA Barge-In. Share line status does not change to Idle after successfully transferring the call.

CSCvi92212 Caller dual mode, SDP Preference set IPv6, callee IPv4 only, the call only has audio, but no video. [8845 and 8865
                           only]

CSCvi92270 Phone LCD displays error for some locales.

CSCvi92292 Paging icon disappears after navigating to the Display brightness menu on the LCD.

CSCvi94469 Press Speaker button to go onhook and dial tone still plays if sharedline re-syncs the DND or CFW.

CSCvi94869 DUT displays XML directory contact name after unparked through PLK.

CSCvi95028 LCD: Call forward first digit could be missed if user inputs a number very quickly.

CSCvi95569 TR69 ACS connection tear down happens before a command is posted.

CSCvi96421 Feature Key Sync is Yes, 88xx and 78xx phones have different behavior for the CFW setting.

CSCvi96613 USB headset cannot hear audio while Preferred audio device is set to Bluetooth and answering a call by softkey.

CSCvi96665 After phone receives paging call and the call is ended, no ringtone for a shared line incoming call.

CSCvi96666 Video secure call, secondary dialing stage, callee offhook, caller reboots. [8845 and 8865 only]

CSCvi96685 When preferred audio device is a speaker, phone always use the speaker to page.

CSCvi98839 The volume of speaker suddenly gets louder when you change the Control Timer Values to the maximum limit.

CSCvi98853 Change Startup delay value of the Ethernet configuration sometimes does not take effect.

CSCvi98881 LCD should not display Delete softkey when the screen focus is on the problem description under the Report Problem
                           menu.

CSCvi99303 During a local conference, unexpected PrivaHold softkey displays when caller presses Conference before called phone
                           answers.

CSCvi99398 Configure Paging Serv from yes to no or no to yes, the setting doesn't work until you reboot the phone.

CSCvi99736 Phone does not return to the front menu when save the settings of the corporate directory using the phone screen.

CSCvj06066 Sharedline call only has one-way audio when the two parties have different SIP & SDP preference modes.

## Resolved Caveats

The following list contains the severity 1, 2, and 3 caveats that are resolved for the Cisco IP Phone 8800 Series Multiplatform Phones that use Firmware Release 11.1(2)SR1.

This list reflects a snapshot of the caveats that were resolved at the time this report was compiled. The status of caveats
                     may have changed since then. For an updated view of the resolved caveats, or to view details or history for specific caveats,
                     access the Bug Search Toolkit as described in View Caveats . You must be a registered Cisco.com user to access this information.

CSCvj07154 CP-88xx-3PCC - Unable to hear beep from voicemail server

CSCvj59089 Phone fails to provision using TR-69

CSCvj84294 Can not open phone's web page with Chrome

| Phone | Support Server |
|---|---|
| Cisco IP Phone 8800 Series Multiplatform Phones | BroadSoft BroadWorks 22.0 MetaSphere CFS version 9.4 Asterisk 11.0 |

| Step 1 | Click the following URL: https://software.cisco.com/download/home/286311392 |
|---|---|
| Step 2 | In the middle pane, select IP Phone 8800 Series With Multiplatform Firmware . |
| Step 3 | Select your phone model in the right pane. |
| Step 4 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 5 | On the next page that is displayed, in the All Releases > MPP v11 folder, select 11.1.2 MSR1-1 . |
| Step 6 | (Optional) Place your mouse pointer on the file name in the right pane, to see the file details and checksum values. |
| Step 7 | Download the file: For Cisco IP Phone 8811, 8841, 8851, and 8861 Multiplatform Phones: cp-88xx.11-1-2MSR1-1_REL.zip For Cisco IP Phone 8845 and 8865 Multiplatform Phones: cp-8845_65.11-1-2MSR1-1_REL.zip |
| Step 8 | Click Accept License Agreement . |
| Step 9 | Unzip the files. |
| Step 10 | Place the files in the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the upgrade. |
| Step 11 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced > Voice > Provisioning tab, Firmware Upgrade section. In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.73.10.223/firmware/sip88xx.11-1-2MSR1-1.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/ sip88xx.11-1-2MSR1-1.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Perform one of the following actions: To find all caveats, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&sb=anfr&bt=custV To find all open caveats, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&sb=anfr&sts=open&bt=custV To find all resolved caveats, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |