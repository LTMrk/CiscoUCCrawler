---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-firmware-11-5-1-sr1-release-notes-p881-b-release-notes-88-c0f05f7630
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/firmware/11-5-1-SR1/release_notes/p881_b_release-notes-8800-series-1151sr1.html
retrieved_at: 2026-08-21T13:32:37.327659+00:00
---

Cisco IP Phone 8800 Series Release Notes for Firmware Release 11.5(1)SR1

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 11.5(1)SR1

### Download Options

Updated: November 16, 2016

First Published: November 16, 2016

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 11.5(1)SR1

These release notes support the Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR running SIP Firmware Release 11.5(1)SR1.

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

https:/​/​www.cisco.com/​c/​en/​us/​support/​collaboration-endpoints/​unified-ip-phone-8800-series/​tsd-products-support-series-home.html

The Deployment Guide is located at the following URL:

https:/​/​www.cisco.com/​c/​en/​us/​support/​collaboration-endpoints/​unified-ip-phone-8800-series/​products-implementation-design-guides-list.html

### Cisco Unified
				Communications Manager Documentation

See the Cisco Unified
				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
				Communications Manager release. Navigate from the following documentation URL:

https:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​tsd-products-support-series-home.html

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

#### Cisco IP Phone 8865NR Support

Firmware Release 11.5(1)SR1 introduces support for Cisco IP Phone 8865NR. This phone delivers the same features as Cisco IP Phone 8865, except for Bluetooth and Wi-Fi support. Cisco IP Phone 8865NR does not support Bluetooth or Wi-Fi, or any Bluetooth or Wi-Fi-dependent features.

Administrators must install the latest Device Package before the Cisco IP Phone 8865NR can function.

For general information about the features and technical details of Cisco IP Phone 8865NR, see http:/​/​www.cisco.com/​c/​en/​us/​products/​collaboration-endpoints/​unified-ip-phone-8800-series/​index.html .

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

#### Record and Monitor Calls on Enhanced Line Mode

Users of Enhanced Line Mode (ELM) can now record their phone calls when Device Invoked Recording is enabled. Supervisors who use ELM can monitor and coach their employees when Monitoring and Recording is enabled.

Feature

Supported

Firmware Release

Answer

Yes

11.5(1) and later

Automatically Answer Calls

Yes

11.5(1) and later

Barge/cBarge

Yes

11.5(1) and later

Bluetooth Smartphone integration

No

-

Bluetooth USB Headsets

Yes

11.5(1) and later

Call Back

Yes

11.5(1) and later

Call Chaperone

No

-

Call Forward All

Yes

11.5(1) and later

Call Park

No

-

Call Park Line Status

No

-

Call Pickup

Yes

11.5(1) and later

Call Pickup Line Status

Yes

11.5(1) and later

CFWA on multiple calls

No

-

Cisco Extension Mobility Cross Cluster

No

-

Cisco IP Manager Assistant (IPMA)

No

-

Cisco Unified Communications Manager Express

No

-

Conference

Yes

11.5(1) and later

Computer Telephony Integration (CTI) applications

Yes

11.5(1) and later

Decline

Yes

11.5(1) and later

Device Invoked Recording

Yes

11.5(1)SR1 and later

Directed BLF

No

-

Do Not Disturb

Yes

11.5(1) and later

Enhanced SRST

No

-

Extension Mobility

Yes

11.5(1) and later

Group Pickup

No

-

Hold

Yes

11.5(1) and later

Hunt Groups

No

-

Incoming Call Alert with configurable timer

No

-

Intercom

Yes

11.5(1) and later

Key Expansion Module

No

-

Malicious Call Identification (MCID)

Yes

11.5(1) and later

Meet Me

Yes

11.5(1) and later

Mobile Connect

Yes

11.5(1) and later

Multilevel Precedence and Preemption

No

-

Mute

Yes

11.5(1) and later

Programmable Line Key (PLK) Support for Queue Status

Yes

11.5(1) and later

Privacy

Yes

11.5(1) and later

Queue Status

Yes

11.5(1) and later

Quality Reporting Tool (QRT)

Yes

11.5(1) and later

Right to Left locale support

No

-

Redial

Yes

11.5(1) and later

Silent Monitoring and Recording

Yes

11.5(1)SR1 and later

Speed Dial

Yes

11.5(1) and later

Survivable Remote Site Telephony (SRST)

Yes

11.5(1) and later

Transfer

Yes

11.5(1) and later

Uniform Resource Identifier (URI) Dialing

Yes

11.5(1) and later

Video Calls

Yes

11.5(1) and later

Visual Voicemail

Yes

11.5(1) and later

Voicemail

Yes

11.5(1) and later

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

#### Make a Video Call with a Closed Shutter

You can now close your camera shutter during a video call. Use this feature when you want the privacy of an audio call, but want to see video from others on the call. A closed shutter icon displays on your phone screen when you use this feature.

Administrators should note that with the camera shutter closed, the user broadcasts a black screen. The call is still a video call with the bandwidth and media requirements of a video call.

The closed shutter feature is supported on Cisco IP Phone 8845, 8865, and 8865NR.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

#### Priority Calls and Do Not Disturb

Firmware Release 11.5(1)SR1 introduces support for multilevel precedence and preemption (MLPP) with do not disturb (DND).

If you receive a priority call, your phone rings with a special ringtone even if you have turned on do not disturb (DND).

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

#### Security Enhancements for Your Phone Network

You can enable Cisco Unified Communications Manager 11.5(1) and later to operate in an enhanced security environment. With these enhancements, your phone network operates under a set of strict security and risk management controls to protect you and your users.

For additional information about working with and enabling these security requirements, see the "FIPS 140-2 Mode Setup" chapter of the Security Guide for Cisco Unified Communications Manager .

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

#### Wi-Fi Enhancements

Wi-Fi users can now quickly join a wireless network by selecting from a list of available networks in their area. This feature is supported on Cisco IP Phone 8861 and 8865.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

### Features Available
	 with the Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require
		the new firmware and the latest Cisco Unified Communications Manager Device
		Pack.

For information about the Cisco Unified IP Phones and the required Cisco
		Unified Communications Manager device packs, see the following URL:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​compat/​devpack_​comp_​mtx.html

#### Configure Ringtone

You can configure the ringtone on a phone with the Admin Configurable Ringer field in Cisco Unified Communications Manager Administration. If you set the ringtone, users cannot change it.

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

For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx-sip.11-5-1SR1-1.k3.cop.sgn

For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65-sip.11-5-1SR1-1.k3.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following .zip files are available to load the firmware.

For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861— cmterm-88xx.11-5-1SR1-1.zip

For Cisco IP Phone 8845, 8865, and 8865NR— cmterm-8845_65.11-5-1SR1-1.zip

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

To access the Locale Installer required for a release, access https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286037605&flowid=46245 , navigate to your phone model, and select the Unified Communications Manager Endpoints Locale Installer link.

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

| Feature | Supported | Firmware Release |
|---|---|---|
| Answer | Yes | 11.5(1) and later |
| Automatically Answer Calls | Yes | 11.5(1) and later |
| Barge/cBarge | Yes | 11.5(1) and later |
| Bluetooth Smartphone integration | No | - |
| Bluetooth USB Headsets | Yes | 11.5(1) and later |
| Call Back | Yes | 11.5(1) and later |
| Call Chaperone | No | - |
| Call Forward All | Yes | 11.5(1) and later |
| Call Park | No | - |
| Call Park Line Status | No | - |
| Call Pickup | Yes | 11.5(1) and later |
| Call Pickup Line Status | Yes | 11.5(1) and later |
| CFWA on multiple calls | No | - |
| Cisco Extension Mobility Cross Cluster | No | - |
| Cisco IP Manager Assistant (IPMA) | No | - |
| Cisco Unified Communications Manager Express | No | - |
| Conference | Yes | 11.5(1) and later |
| Computer Telephony Integration (CTI) applications | Yes | 11.5(1) and later |
| Decline | Yes | 11.5(1) and later |
| Device Invoked Recording | Yes | 11.5(1)SR1 and later |
| Directed BLF | No | - |
| Do Not Disturb | Yes | 11.5(1) and later |
| Enhanced SRST | No | - |
| Extension Mobility | Yes | 11.5(1) and later |
| Group Pickup | No | - |
| Hold | Yes | 11.5(1) and later |
| Hunt Groups | No | - |
| Incoming Call Alert with configurable timer | No | - |
| Intercom | Yes | 11.5(1) and later |
| Key Expansion Module | No | - |
| Malicious Call Identification (MCID) | Yes | 11.5(1) and later |
| Meet Me | Yes | 11.5(1) and later |
| Mobile Connect | Yes | 11.5(1) and later |
| Multilevel Precedence and Preemption | No | - |
| Mute | Yes | 11.5(1) and later |
| Programmable Line Key (PLK) Support for Queue Status | Yes | 11.5(1) and later |
| Privacy | Yes | 11.5(1) and later |
| Queue Status | Yes | 11.5(1) and later |
| Quality Reporting Tool (QRT) | Yes | 11.5(1) and later |
| Right to Left locale support | No | - |
| Redial | Yes | 11.5(1) and later |
| Silent Monitoring and Recording | Yes | 11.5(1)SR1 and later |
| Speed Dial | Yes | 11.5(1) and later |
| Survivable Remote Site Telephony (SRST) | Yes | 11.5(1) and later |
| Transfer | Yes | 11.5(1) and later |
| Uniform Resource Identifier (URI) Dialing | Yes | 11.5(1) and later |
| Video Calls | Yes | 11.5(1) and later |
| Visual Voicemail | Yes | 11.5(1) and later |
| Voicemail | Yes | 11.5(1) and later |

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phone 8800 Series . |
| Step 3 | Choose your phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 11.5(1)SR1 . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts: For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx-sip.11-5-1SR1-1.k3.cop.sgn For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65-sip.11-5-1SR1-1.k3.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
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
| Step 5 | In the Latest Releases folder, choose 11.5(1)SR1 . |
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