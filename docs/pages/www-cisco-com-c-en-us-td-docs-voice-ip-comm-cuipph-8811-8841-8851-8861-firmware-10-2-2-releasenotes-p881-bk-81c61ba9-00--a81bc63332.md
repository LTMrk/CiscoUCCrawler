---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8811-8841-8851-8861-firmware-10-2-2-releasenotes-p881-bk-81c61ba9-00--a81bc63332
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8811_8841_8851_8861/firmware/10-2-2/releasenotes/P881_BK_81C61BA9_00_8800-phone-series-rn-10_2_2/P881_BK_81C61BA9_00_8800-phone-series-rn-10_2_2_chapter_00.html
retrieved_at: 2026-08-25T13:11:07.605297+00:00
---

Cisco IP Phone 8800 Series Release Notes for Firmware Release 10.2(2)

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 10.2(2)

Updated: May 6, 2015

Chapter: Cisco IP Phone 8800 Series Release Notes for Firmware Release 10.2(2)

## Chapter: Cisco IP Phone 8800 Series Release Notes for Firmware Release 10.2(2)

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 10.2(2)

## Introduction

These release notes support the Cisco IP Phones 8811, 8841, 8851, and 8861
                           		running SIP Firmware Release 10.2(2).

The following table lists the support and protocol compatibility for the Cisco IP Phones.

Cisco IP Phone

Protocol

Support Requirements

Cisco IP Phones 8811, 8841, 8851, and 8861

SIP

Cisco Unified Communications Manager 8.5(1) and later

Cisco Unified Communications Manager DST Olsen version D or later

SRST 8.0 (IOS load 15.1(1)T) and above

CME 10.0 (IOS load 15.3(3)M) and above through
                                       Fast-Track

## Related
                        	 Documentation

### Cisco IP Phone 8800 Series Documentation

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Phone 8800 Series.

For help information about Cisco Video Phone 8875, see Cisco Video Phone 8875 .

The Deployment Guide is located at the following URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-implementation-design-guides-list.html

### Cisco Unified
                              				Communications Manager Documentation

See the Cisco Unified
                                       				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                                    				Communications Manager release on the product support page.

## New and Changed
                        	 Features

The following sections describe the features that are new or have
                           		changed in this release.

### Features Available
                           	 with the Firmware Release

The following sections describe the features available with the Firmware
                              		Release.

#### Bluetooth Multiconnection

The Bluetooth Multiconnection feature enables users to pair more than one Bluetooth device with the phone and have up to two
                                 Bluetooth devices connected to the phone at the same time. The following connection scenarios are supported:

one Bluetooth headset

one Bluetooth headset and one mobile phone

one Bluetooth headset and one tablet

Users cannot pair a mobile device and a tablet at the same time.

When the user connects a Bluetooth headset and a mobile phone or tablet at the same time, the Bluetooth headset cannot be
                                             used to answer the audio from the mobile phone or tablet.

The feature is supported on the following phones:

Cisco IP Phone 8851

Cisco IP Phone 8861

##### Where to Find More Information

Cisco IP Phone 8811, 8841, 8851, and 8861 Administration Guide for Cisco Unified Communications Manager 10.5

Cisco IP Phone 8811, 8841, 8851, and 8861 User Guide for Cisco Unified Communications Manager 10.5

#### Display Battery Strength and Signal Strength Icons

The Display Battery Strength and Signal Strength Icons feature displays the battery and signal strength of the mobile phone
                                 in the header on the IP Phone when the mobile phone is connected to the IP Phone using Bluetooth.

This feature requires no administration.

The feature is supported on the following phones:

Cisco IP Phone 8851

Cisco IP Phone 8861

##### Where to Find More Information

Cisco IP Phone 8811, 8841, 8851, and 8861 Administration Guide for Cisco Unified Communications Manager 10.5

Cisco IP Phone 8811, 8841, 8851, and 8861 User Guide for Cisco Unified Communications Manager 10.5

#### Line Status in Corporate Directory

The Line Status in Corporate Directory  feature enables the phone to display the line status for telephone numbers that are
                                 stored in the Corporate Directory. This feature is similar to the existing Line Status for Call Lists feature.

The administrator uses the BLF For Call Lists field in the Cisco Unified Communications Manager to control this feature.

The feature is supported on the following phones:

Cisco IP Phone 8811

Cisco IP Phone 8841

Cisco IP Phone 8851

Cisco IP Phone 8861

##### Where to Find More Information

Cisco IP Phone 8811, 8841, 8551, and 8861 Administration Guide for Cisco Unified Communications Manager  10.5

Cisco IP Phone 8811, 8841, 8551, and 8861 User Guide for Cisco Unified Communications Manager  10.5

#### Phone Trust List Notification in Cisco Unified Communications Manager

The Phone Trust List Notification in Cisco Unified Communications Manager enables the phone to send an alarm to the Cisco
                                 Unified Communications Manager when the Trust List (TL) is updated.

The following table contains the alarm messages and meaning.

1 - TL_SUCCESS

Received new CTL and/or ITL

2 - CTL_INITIAL_SUCCESS

Received new CTL, no existing TL

3 - ITL_INITIAL_SUCCESS

Received new ITL, no existing TL

4 - TL_INITIAL_SUCCESS

Received new CTL and ITL, no existing TL

5 - TL_FAILED_OLD_CTL

Update to new CTL failed, but have previous TL

6 - TL_FAILED_NO_TL

Update to new TL failed, and have no old TL

7 - TL_FAILED

Generic failure

8 - TL_FAILED_OLD_ITL

Update to new ITL failed, but have previous TL

9 - TL_FAILED_OLD_TL

Update to new TL failed, but have previous TL

This feature has no user impact.

The feature is supported on the following phones:

Cisco IP Phone 8811

Cisco IP Phone 8841

Cisco IP Phone 8851

Cisco IP Phone 8861

##### Where to Find More Information

Cisco IP Phone 8811, 8841, 8851, and 8861 Administration Guide for Cisco Unified Communications Manager 10.5

Cisco Unified Communications Manager documentation

#### Remove Call Ended Timer

The Remove Call Ended Timer feature improves the End Call response time by removing the Call ended message display on the phone screen.

This feature has no administration impacts.

The feature is supported on the following phones:

Cisco IP Phone 8811

Cisco IP Phone 8841

Cisco IP Phone 8851

Cisco IP Phone 8861

#### Simplified Tablet Support

The Simplified Tablet Support feature enables a user to pair a tablet to the phone using Bluetooth, and then use the phone
                                 for the audio part of a call on the tablet.

The tablet manages the audio path; the phone has no audio control (for example, the phone cannot place the audio on hold or
                                 end the call). The Cisco IP Phone acts as a simple Bluetooth speaker. When the paired tablet is actively transmitting or receiving
                                 data to the phone, the phone header displays the mobile icon.

The administrator controls access using the Bluetooth and Allow Bluetooth Mobile Handsfree Mode fields in the Cisco Unified
                                 Communications Manager Administration.

The following tablet operating systems are supported:

Android version 4.4

iOS version 7.1

The feature was tested with the following tablets:

iPad Air

iPad Mini. iPad Mini 2

iPad 4

Samsung Galaxy TabPro

The feature is supported on the following phones:

Cisco IP Phone 8851

Cisco IP Phone 8861

##### Where to Find More Information

Cisco IP Phone 8811, 8841, 8851, and 8861 Administration Guide for Cisco Unified Communications Manager 10.5

Cisco IP Phone 8811, 8841, 8851, and 8861 User Guide for Cisco Unified Communications Manager 10.5

#### Unconfigured Primary Line Notification

The Unconfigured Primary Line Notification feature alerts the user when the system administrator has not configured the primary
                                 line. The user sees the message Unprovisioned on the phone screen.

This feature requires no administration.

The feature is supported on the following phones:

Cisco IP Phone 8811

Cisco IP Phone 8841

Cisco IP Phone 8851

Cisco IP Phone 8861

##### Where to Find More Information

Cisco IP Phone 8811, 8841, 8851, and 8861 Administration Guide for Cisco Unified Communications Manager 10.5

Cisco IP Phone 8811, 8841, 8851, and 8861 User Guide for Cisco Unified Communications Manager 10.5

#### User Interface Updates for List, Alert, and Visual Voice Mail

The User Interface Updates for List, Alert, and Visual Voice Mail feature increases the width of the application window to
                                 ensure that long phrases can be displayed on the phone. The feature impacts the following windows:

Call History

Settings

VPN

Alerts

Corporate and Personal Directories

Visual Voice Mail

The Barge softkey has been renamed to Merge, and the Barge alert entry in Settings menu has been renamed Merge alert.

The feature is supported on the following phones:

Cisco IP Phone 8811

Cisco IP Phone 8841

Cisco IP Phone 8851

Cisco IP Phone 8861

##### Where to Find More Information

Cisco IP Phone 8811, 8841, 8851, and 8861 Administration Guide for Cisco Unified Communications Manager 10.5

Cisco IP Phone 8811, 8841, 8851, and 8861 User Guide for Cisco Unified Communications Manager 10.5

### Features Available with the Latest Cisco Unified
                              				Communications Manager Device Package

The following sections describe features in the release which require the new firmware and the latest Cisco Unified
                                 				Communications Manager device package. The applicable device packages are released after the firmware release.

For information about the Cisco devices and the required Cisco Unified
                                 				Communications Manager device packages, see the following URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html

#### Cisco IP Phone 8800 Key Expansion Module

The Cisco IP Phone 8800 Key Expansion Module (KEM) increases the number of line/feature key appearances on the Cisco IP Phone 8851 and 8861 . The 18 keys can be customized for frequently used telephony features such as speed dials, and offering one-button push access
                                 to colleagues contacted most often. It also supports shared-line appearances to increase responsiveness and personal interaction
                                 with incoming callers. It enhances productivity with simpler and more efficient communications.

The Cisco IP Phone 8800 Key Expansion Module is supported on the following phones:

Cisco IP Phone 8851 : up to 2 KEMs supported

Cisco IP Phone 8861 : up to 3 KEMs supported

The Cisco IP Phone 8811 and Cisco IP Phone 8841 do not support the Cisco IP Phone 8800 Key Expansion Module .

##### Where to Find More Information

Cisco IP Phone 8811, 8841, 8851, and 8861 Administration Guide for Cisco Unified Communications Manager 10.5

Cisco IP Phone 8811, 8841, 8851, and 8861 User Guide for Cisco Unified Communications Manager 10.5

#### Cisco IP Phone 8811 Support

The Cisco IP Phone 8811 Support feature introduces the Cisco IP Phone 8811. This phone delivers easy to use, highly secure,
                                 and powerful
                                 mission-critical voice communications. It
                                 offers support of wideband audio and a large grayscale display.

The Cisco IP Phone 8811 supports the same features and functionality as the Cisco IP Phone 8841. The only difference between
                                 these two models is the type of LCD display.

The Cisco IP Phone 8811 requires Firmware Release 10.2(2) or later.

##### Where to Find More information

Cisco IP Phone 8811, 8841, 8851, and 8861 Administration Guide for Cisco Unified Communications Manager 10.5

Cisco IP Phone 8811, 8841, 8851, and 8861 User Guide for Cisco Unified Communications Manager 10.5

#### Enable/Disable JAL/TAL

The Enable/Disable JAL/TAL feature allows the administrator to control the Join Across Lines (JAL) and Direct Transfer Across
                                 Lines (TAL) features.  The administrator can disable JAL/TAL to avoid users joining or transferring calls by mistake.

The feature is supported from the Cisco Unified Communications Manager Administration window using the Join and Direct Transfer
                                 Policy field. The field supports the following choices:

- Same line, across line enable (default)

- Same line enable

- Same line, across line disable

The feature is supported on the following phones:

Cisco IP Phone 8811

Cisco IP Phone 8841

Cisco IP Phone 8851

Cisco IP Phone 8861

##### Where to Find More Information

Cisco IP Phone 8811, 8841, 8851, and 8861 Administration Guide for Cisco Unified Communications Manager 10.5

Cisco IP Phone 8811, 8841, 8851, and 8861 User Guide for Cisco Unified Communications Manager 10.5

## Installation

### Install Firmware Release on Cisco Unified Communications Manager

Before using the phone firmware release on
                                 		  the Cisco Unified Communications Manager, you must install the latest Cisco Unified Communications Manager firmware on
                                 		  all Cisco Unified Communications Manager servers in the cluster.

Step 1

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Step 2

Depending on your phone model, choose Cisco IP Phone 8800 Series .

Step 3

Choose your phone type.

Step 4

Choose Session Initiation Protocol (SIP) Software .

Step 5

In the Latest Releases folder, choose 10.2(2) .

Step 6

Select the  firmware file cmterm-88xx-sip.10-2-2-16.cop.sgn 
                                          				  , click the Download or Add to cart button, and follow the prompts:

If you added the firmware file to the cart, click the Download Cart link when you are ready to
                                                         				  download the file.

Step 7

Click the + next to the firmware file name in the
                                          			 Download Cart section to access additional information about this file. The
                                          			 hyperlink for the readme file is in the Additional Information section, which
                                          			 contains installation instructions for the corresponding firmware.

Step 8

Follow the instructions in the readme file to install the
                                          			 firmware.

### Install Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the
                                 		  installer program, the following .zip files are available to load the firmware.

cmterm-88xx-sip.10-2-2-16.zip

Firmware upgrades over the WLAN interface may take longer than
                                 		  upgrades using a wired connection. Upgrade times over the WLAN interface may
                                 		  take more than an hour, depending on the quality and bandwidth of the wireless
                                 		  connection.

Step 1

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Step 2

Choose Cisco IP Phones 8800 Series .

Step 3

Choose your phone type.

Step 4

Choose Session Initiation Protocol (SIP) Software .

Step 5

In the Latest Releases folder, choose 10.2(2) .

Step 6

Download the relevant zip files.

Step 7

Unzip the files.

Step 8

Manually copy the unzipped files to the directory on the TFTP
                                          			 server. See Cisco Unified Communications Operating System Administration
                                             				Guide for information about how to manually copy the firmware files to
                                          			 the server.

## Unified
                        	 Communications Manager Endpoints Locale Installer

By default, Cisco IP Phones are set up for the English (United States) locale. To use the Cisco IP Phones in other locales,
                              you must install the locale-specific version of the Unified Communications Manager Endpoints Locale Installer on every Cisco Unified
                                 				Communications Manager server in the cluster. The Locale Installer installs the latest translated text for the phone user interface and country-specific
                              phone tones on your system so that they are available for the Cisco IP Phones.

To access the Locale Installer required for a release, access the Software Download page, navigate to your phone model, and select the Unified Communications Manager Endpoints Locale Installer link.

For more information, see the documentation for your particular Cisco Unified
                                 				Communications Manager release.

The latest
                                          			 Locale Installer may not be immediately available; continue to check the
                                          			 website for updates.

## Limitations and Restrictions

### Bluetooth Phone Book Access Profile Limitations

Cisco IP Phones 8851 and 8861 cannot display certain characters in
                                    the Contact/Call history imported from a mobile device if those
                                    characters are not included in the phone  locale.

In this release, Cisco IP Phones 8851 and 8861 do not support the ability to
                                    initiate a new call from the mobile contact book through the Cisco Unified Communications Manager VoIP
                                    network.

### Bluetooth Handsfree Profile Limitations

Only one Bluetooth device can be connected with
                                    Cisco IP Phones 8851 and 8861 at the same time, either a BT headset or a mobile phone.

Tablet pairing and connecting is not supported in
                                    this release.

Due to mobile device OS limitations, some soft
                                    clients on a mobile device (for example, Cisco Jabber or Skype) cannot make
                                    full telephony integration with Cisco IP Phones 8851 and 8861 for call controls
                                    like Answer, End, Hold, or Resume a call. Some known issues
                                    include:

The incoming call event sent from mobile soft client
                                          to Cisco IP Phones 8851 and 8861 causes the ongoing VoIP call to go on hold
                                          automatically.

The call information might not be displayed correctly
                                          on Cisco IP Phones 8851 and 8861.

The call session does not disappear on Cisco IP Phones 8851 and 8861 when
                                          the Jabber call ends on the mobile device. Jabber version 10.5 and later removes this limitation.

### Phone Behavior
                           	 During Times of Network Congestion

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

## View Caveats

You can search for
                              		  caveats using the Cisco Bug Search.

Known caveats
                              		  (bugs) are graded according to severity level, and can be either open or resolved.

### Before you begin

To view caveats, you need the following items:

Internet
                                    				connection

Web browser

Cisco.com user
                                    				ID and password

Step 1

Perform one of the following actions:

To find all caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284729655&rls=10.2(2)&sb=anfr&srtBy=svr&bt=custV

To find all open caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284729655&rls=10.2(2)&sb=afr&srtBy=svr&bt=custV

To find all resolved caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284729655&rls=10.2(2)&sb=fr&srtBy=svr&bt=custV

Step 2

When prompted, log in with your
                                       			 Cisco.com user ID and password.

Step 3

To look for
                                       			 information about a specific problem, enter the bug ID number in the Search for
                                       			 field, then press Enter .

## Cisco IP Phone
                        	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/c/en/us/td/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application.
                           The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco IP Phones 8811, 8841, 8851, and 8861 | SIP | Cisco Unified Communications Manager 8.5(1) and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above CME 10.0 (IOS load 15.3(3)M) and above through
                                       Fast-Track |

| Note | When the user connects a Bluetooth headset and a mobile phone or tablet at the same time, the Bluetooth headset cannot be
                                             used to answer the audio from the mobile phone or tablet. |
|---|---|

| Code and Message | Description |
|---|---|
| 1 - TL_SUCCESS | Received new CTL and/or ITL |
| 2 - CTL_INITIAL_SUCCESS | Received new CTL, no existing TL |
| 3 - ITL_INITIAL_SUCCESS | Received new ITL, no existing TL |
| 4 - TL_INITIAL_SUCCESS | Received new CTL and ITL, no existing TL |
| 5 - TL_FAILED_OLD_CTL | Update to new CTL failed, but have previous TL |
| 6 - TL_FAILED_NO_TL | Update to new TL failed, and have no old TL |
| 7 - TL_FAILED | Generic failure |
| 8 - TL_FAILED_OLD_ITL | Update to new ITL failed, but have previous TL |
| 9 - TL_FAILED_OLD_TL | Update to new TL failed, but have previous TL |

| Note | The Cisco IP Phone 8811 and Cisco IP Phone 8841 do not support the Cisco IP Phone 8800 Key Expansion Module . |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Depending on your phone model, choose Cisco IP Phone 8800 Series . |
| Step 3 | Choose your phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 10.2(2) . |
| Step 6 | Select the  firmware file cmterm-88xx-sip.10-2-2-16.cop.sgn 
                                          				  , click the Download or Add to cart button, and follow the prompts: Note If you added the firmware file to the cart, click the Download Cart link when you are ready to
                                                         				  download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to
                                                         				  download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to
                                                         				  download the file. |
| Step 7 | Click the + next to the firmware file name in the
                                          			 Download Cart section to access additional information about this file. The
                                          			 hyperlink for the readme file is in the Additional Information section, which
                                          			 contains installation instructions for the corresponding firmware. |
| Step 8 | Follow the instructions in the readme file to install the
                                          			 firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to
                                                         				  download the file. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phones 8800 Series . |
| Step 3 | Choose your phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 10.2(2) . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP
                                          			 server. See Cisco Unified Communications Operating System Administration
                                             				Guide for information about how to manually copy the firmware files to
                                          			 the server. |

| Note | The latest
                                          			 Locale Installer may not be immediately available; continue to check the
                                          			 website for updates. |
|---|---|

| Step 1 | Perform one of the following actions: To find all caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284729655&rls=10.2(2)&sb=anfr&srtBy=svr&bt=custV To find all open caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284729655&rls=10.2(2)&sb=afr&srtBy=svr&bt=custV To find all resolved caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284729655&rls=10.2(2)&sb=fr&srtBy=svr&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your
                                       			 Cisco.com user ID and password. |
| Step 3 | To look for
                                       			 information about a specific problem, enter the bug ID number in the Search for
                                       			 field, then press Enter . |