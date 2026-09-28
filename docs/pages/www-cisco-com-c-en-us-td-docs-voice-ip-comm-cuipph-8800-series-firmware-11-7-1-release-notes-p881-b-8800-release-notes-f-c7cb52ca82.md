---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-firmware-11-7-1-release-notes-p881-b-8800-release-notes-f-c7cb52ca82
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/firmware/11-7-1/Release_Notes/p881_b_8800-release-notes-for-1171.html
retrieved_at: 2026-08-21T13:32:28.572305+00:00
---

Cisco IP Phone 8800 Series Release Notes for Firmware Release 11.7(1)

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 11.7(1)

### Download Options

Updated: March 7, 2017

First Published: January 27, 2017

Last Updated: March 07, 2017

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 11.7(1)

These release notes support the Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR running SIP Firmware Release 11.7(1).

Cisco IP Phone

Protocol

Support Requirements

8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR

SIP

Cisco Unified Communications Manager 8.5(1) and later

Cisco Unified Communications Manager DST Olsen version D or later

SRST 8.0 (IOS load 15.1(1)T) and above

Cisco Expressway 8.7

8811, 8841, 8851, 8851NR, and 8861

SIP

CME 10.0 (IOS load 15.3(3)M)

## Related
	 Documentation

Use the following sections to
		obtain related information.

### Cisco IP Phone 8800 Series Documentation

Refer to
		  publications that are specific to your language, phone model, and call control
		  system. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​collaboration-endpoints/​unified-ip-phone-8800-series/​tsd-products-support-series-home.html

The Deployment Guide is located at the following URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​collaboration-endpoints/​unified-ip-phone-8800-series/​products-implementation-design-guides-list.html

### Cisco Unified
				Communications Manager Documentation

See the Cisco Unified
				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
				Communications Manager release. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​tsd-products-support-series-home.html

## New Hardware

### Cisco IP Phone 8851 and PoE

Cisco IP Phone 8851 with new hardware version ID V08 is now classified as IEEE Power over Ethernet (PoE) Class 4 from Class 3. This improvement allows support of up to two Key Expansion Modules with IEEE Power over Ethernet. Previously, the Cisco IP Phone Power Cube 4 was required to power two Key Expansion Modules.

#### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

### New Cisco IP Phones 8811, 8841, 8851, and 8851NR Hardware

The Cisco IP phones 8811, 8841, 8851, and 8851NR has hardware updates. The new phone version IDs are:

Cisco IP Phone 8811: V08

Cisco IP Phone 8841: V08

Cisco IP Phone 8851: V08

Cisco IP Phone 8851NR: V08

Phones manufactured with the new version ID must run Firmware Release 11.7(1) or later. The phone firmware does not allow the phone to be downgraded to releases earlier than Firmware Release 11.7(1). There is no hardware upgrade for Cisco IP Phone 8861.

This feature has no user impact.

## New and Changed
	 Features

The following sections describe the features that are new or have
		changed in this release.

Some features may require the installation of a Cisco Unified
		  Communications Manager Device Package. Failure to install the Device Package
		  before the phone firmware upgrade may render the phones unusable.

### Features Available
	 with the Firmware Release

The following sections describe the features available with the Firmware
		Release.

#### New Desktop Icons, Background, and Missed Calls Display

Firmware release 11.7(1) introduces an improved user experience with new badged icons.

If you have missed calls, the missed call icon, and a counter showing the number of missed calls, display on your phone desktop. If you receive a voicemail, the missed call icon changes to the voicemail icon and voicemail counter until you listen to your messages.

In addition, there are new icons for multiple calls. If you have more than one call on a line, either the held icon or the off hook icon change to show the number of calls.

It is now easier to see your missed calls by selecting a line key to view the missed calls for that line in the call window. The missed call counter clears when you return to the idle screen.

Your phone display is now enhanced with a new default background for your phone desktop.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide for Cisco Unified Communications Manager

#### Video Call Enhancement

Firmware release 11.7(1) introduces an improved quality of service and network performance for video calls. During a call, you can now make a true transition from an audio call to a video call by opening the camera shutter mid-call. When you open the shutter, the associated DSCP values change from DSCP 46 (EF) to DSCP 34 (AF41). Prior to firmware release 11.7(1), a true transition from an audio call to a video call mid-call was not supported.

You can mute the video by closing the shutter, but the call remains a video call.

The video call enhancement is enabled by default. It is supported on Cisco IP Phone 8845, 8865, and 8865NR.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

#### SRSTv6 Support for Cisco IP Phone 8800 Series

Cisco Unified Survivable Remote Site Telephony(SRST) supports IPv6. This feature requires Cisco Unified Communications Manager 12.0 and later.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications Manager is running the latest device pack. After you install a device pack on the Cisco Unified Communications Manager servers in the cluster, you need to reboot all the servers.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​compat/​devpack_​comp_​mtx.html .

### Install the Firmware Release on Cisco Unified Communications Manager

Before using the phone firmware release on the Cisco Unified Communications Manager, you must install the latest Cisco Unified Communications Manager firmware on all Cisco Unified Communications Manager servers in the cluster.

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283

For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx-sip.11-7-1-17.k3.cop.sgn

For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65-sip.11-7-1-17.k3.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following .zip files are available to load the firmware.

For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx.11-7-1-17.zip

For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65.11-7-1-17.zip

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283

## Limitations and Restrictions

### Phone Behavior During Times of Network Congestion

Anything that degrades network performance can affect Cisco IP Phone voice and video quality, and in some cases, can cause a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that occur on your network, such as a Denial of Service attack

### Health-Care
	 Environment Use

This product is not a
		medical device and uses an unlicensed frequency band that is susceptible to
		interference from other devices or equipment.

### On-Hook Transfer Limitation in SIP Phones

When the Cisco Unified Communications Manager Transfer On-Hook Enabled field is enabled, users might report a problem with direct call transfer in SIP phones. If the user transfers the call and immediately goes on hook before they hear the ring signal, the call may drop instead of being transferred.

The user needs to hear the ring signal so that they can be sure that the call is being routed.

### Ringtone Limitation During Firmware Downgrade from Release 11.5(1)

When the phone downgrades from Firmware Release 11.5(1) to Firmware Release 11.0(1), the phone may not ring when there is an incoming call. The ringtone for the line has been deleted and must be manually set in the Settings > Ringtone menu.

### Language Limitation

There is no localized Keyboard
Alphanumeric Text Entry (KATE) support for the following Asian
locales:

Chinese (China)

Chinese (Hong Kong)

Chinese (Taiwan)

Japanese (Japan)

Korean (Korea Republic)

The default English (United States) KATE is presented to the user instead.

For example, the phone screen will show text in Korean, but the 2 key on the keypad will display a b c 2 A B C .

## View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

To view caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

## Cisco Unified Communication Manager Public Keys

To improve software integrity protection, new public keys are used to sign cop files for Cisco Unified Communications Manager Release 10.0.1 and later. These cop files have "k3" in their name. To install a k3 cop file on a pre-10.0.1 Cisco Unified Communications Manager, consult the README for the ciscocm.version3-keys.cop.sgn to determine if this additional cop file must first be installed on your specific Cisco Unified Communications Manager version. If these keys are not present and are required, you will see the error "The selected file is not valid" when you try to install the software package.

## Unified
	 Communications Manager Endpoints Locale Installer

By default, Cisco
		  IP Phones are set up for the English (United States) locale. To use the Cisco
		  IP Phones in other locales, you must install the locale-specific version of the
		  Unified Communications Manager Endpoints Locale Installer on every Cisco
		  Unified Communications Manager server in the cluster. The Locale Installer
		  installs the latest translated text for the phone user interface and
		  country-specific phone tones on your system so that they are available for the
		  Cisco IP Phones.

To access the
		  Locale Installer required for a release, access http:/​/​software.cisco.com/​download/​navigator.html?mdfid=286037605&flowid=46245 , navigate to your phone model, and
		  select the Unified Communications Manager Endpoints Locale Installer link.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

The latest
			 Locale Installer may not be immediately available; continue to check the
			 website for updates.

## Cisco IP Phone Documentation Updates on Cisco Unified Communications Manager

The Cisco Unified Communications Manager Self Care Portal (Release 10.0 and later) and User Options web pages (Release 9.1 and earlier) provide  links to the IP Phone user guides in PDF format. These user guides are stored on the Cisco Unified Communications Manager and are up to date when the Cisco Unified Communications Manager release is first made available to customers.

After a Cisco Unified Communications Manager release, subsequent updates to the user guides appear only on the Cisco website. The phone firmware release notes contain the applicable documentation URLs. In the web pages, updated documents display "Updated" beside the document link.

The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer do not update the English user guides on the Cisco Unified Communications Manager.

Administrators and users should check the Cisco website for updated user guides and download the PDF files. Administrators can also make the files available to the users on their company website.

Administrators may want to bookmark the web pages for the phone models that are deployed in their company and send these URLs to their users.

## Cisco IP Phone
	 Firmware Support Policy

For information on
		  the support policy for Cisco IP Phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR | SIP | Cisco Unified Communications Manager 8.5(1) and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above Cisco Expressway 8.7 |
| 8811, 8841, 8851, 8851NR, and 8861 | SIP | CME 10.0 (IOS load 15.3(3)M) |

| Note | Some features may require the installation of a Cisco Unified
		  Communications Manager Device Package. Failure to install the Device Package
		  before the phone firmware upgrade may render the phones unusable. |
|---|---|

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phone 8800 Series . |
| Step 3 | Choose your phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 11.7(1) . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts: For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx-sip.11-7-1-17.k3.cop.sgn For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65-sip.11-7-1-17.k3.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink for the readme file is in the Additional Information section, which contains installation instructions for the corresponding firmware. |
| Step 8 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phones 8800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 11.7(1) . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

| Step 1 | Perform one of the following actions: |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |

| Note | The latest
			 Locale Installer may not be immediately available; continue to check the
			 website for updates. |
|---|---|

| Note | The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer do not update the English user guides on the Cisco Unified Communications Manager. |
|---|---|

| Tip | Administrators may want to bookmark the web pages for the phone models that are deployed in their company and send these URLs to their users. |
|---|---|