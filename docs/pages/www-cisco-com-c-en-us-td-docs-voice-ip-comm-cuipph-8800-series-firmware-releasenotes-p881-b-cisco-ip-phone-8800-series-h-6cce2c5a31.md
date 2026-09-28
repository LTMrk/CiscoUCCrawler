---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-firmware-releasenotes-p881-b-cisco-ip-phone-8800-series-h-6cce2c5a31
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/firmware/releasenotes/p881_b_cisco-ip-phone-8800-series.html
retrieved_at: 2026-08-21T13:32:32.966052+00:00
---

Cisco IP Phone 8800 Series Release Notes for Firmware Release 11.5(1)

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 11.5(1)

### Download Options

Updated: October 13, 2016

First Published: June 03, 2016

Last Updated: October 13, 2016

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 11.5(1)

These release
		  notes support the Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861, and 8865 running SIP Firmware Release
		  11.5(1).

Cisco IP
					 Phone

Protocol

Support
					 Requirements

8811,
					 8841, 8845, 8851, 8851NR, 8861, and 8865

SIP

Cisco
					 Unified Communications Manager 8.5(1) and later

Cisco
					 Unified Communications Manager DST Olsen version D or later

SRST 8.0
					 (IOS load 15.1(1)T) and above

Cisco Expressway 8.7

8811,
					 8841,  8851, 8851NR, and 8861

SIP

CME 10.0
					 (IOS load 15.3(3)M)

## Related
	 Documentation

Use the following sections to
		obtain related information.

### Cisco IP Phone 8800 Series Documentation

Refer to
		  publications that are specific to your language, phone model, and call control
		  system. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​collaboration-endpoints/​unified-ip-phone-8800-series/​tsd-products-support-series-home.html

The Design Guides are located at the following URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​collaboration-endpoints/​unified-ip-phone-8800-series/​products-implementation-design-guides-list.html

### Cisco Unified
				Communications Manager Documentation

See the Cisco Unified
				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
				Communications Manager release. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​tsd-products-support-series-home.html

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

#### Enhanced Do Not Disturb

When users turn on Do Not Disturb, the header section of the phone screen turns red, and Do not disturb displays on the phone screen. Previously when DND was turned on, an icon displayed on the phone.

On the Cisco IP Phone 8811, the header section turns dark gray because this phone has a black and white display screen.

You can set Do Not Disturb in the Product Specific Configuration Layout portion of the Device Configuration window in Cisco Unified Communications Manager.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

#### Customized Dial Tone for SIP Phones

Default: The inside dial tone is used for inside calls. The outside dial tone is used for outside calls.

Inside: The inside dial tone is used for all calls.

Outside: The outside dial tone is used for all calls.

The inside dial tone is slightly quieter than the outside dial tone.

Dial tones are customized from the Service Parameter window, with Cisco CallManager selected as the service.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

#### Wi-Fi Security Enhancements

You can balance network security with ease of use by setting the number of authentication requests sent by  a phone.  By limiting the number of requests,  traffic is reduced across your network and denial of service attacks are more easily identified. It is also easier for users  to stay connected to the network because they are prompted for their password only if authentication fails.

Enable the number of authentication requests from the Product Specific Configuration Layout portion of the Device Configuration window in Cisco Unified Communications Manager. The default setting is two attempts, but you can choose from 1 to 3 attempts.

The second security enhancement is the WLAN Profile 1 Prompt Mode. This feature keeps your network secure by prompting users for their sign-in credentials when the phone powers-up in Wi-Fi mode.

WLAN Profile 1 Prompt Mode is set  from the Product Specific Configuration Layout portion of the Device Configuration window in Cisco Unified Communications Manager. It is disabled by default.

The Wi-Fi Security enhancements are supported on Cisco Unified Communications Manager 9.1(2) and later, and require the latest Device Package to function.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

### Features Available
	 with the Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require
		the new firmware and the latest Cisco Unified Communications Manager Device
		Pack.

For information about the Cisco Unified IP Phones and the required Cisco
		Unified Communications Manager device packs, see the following URL:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​compat/​devpack_​comp_​mtx.html

#### Enhanced Line Mode

The buttons on the left and right of the phone screen can be set up as line buttons, giving up to five more line keys. Users see an alert for an incoming call.

Enhanced line mode is supported on Cisco Unified Communications Manager 9.1(2), 10.5(2), and 11.0(1) and any higher releases that are generally available. The latest Device Package is required. You can set the line mode in the Product Specific Configuration Layout portion of the Device Configuration window in Cisco Unified Communications Manager.

Enhanced line mode supports most but not all features with Firmware Release 11.5(1). Enabling a feature does not imply support. Read the following table to confirm that a feature is supported.

Feature

Supported by Firmware Release 11.5(1)

Notes

Answer

Yes

Automatically Answer Calls

Yes

Barge/cBarge

Yes

Bluetooth Smartphone integration

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Bluetooth USB Headsets

Yes

Call Back

Yes

Call Chaperone

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Call Forward All

Yes

Call Park

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Call Park Line Status

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Call Pickup

Yes

Call Pickup Line Status

Yes

CFWA on multiple calls

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Cisco Extension Mobility Cross Cluster

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Cisco IP Manager Assistant (IPMA)

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Cisco Unified Communications Manager Express

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Conference

Yes

Computer Telephony Integration (CTI) applications

Yes

Decline

Yes

Device Invoked Recording

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Directed Park BLF

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Do Not Disturb

Yes

Enhanced SRST

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Extension Mobility

Yes

Group Pickup

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Hold

Yes

Hunt Groups

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Incoming Call Alert with configurable timer

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Intercom

Yes

Key Expansion Module

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Malicious Call Identification (MCID)

Yes

Meet Me

Yes

Mobile Connect

Yes

Multilevel Precedence and Preemption

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Mute

Yes

Programmable Line Key (PLK) Support for Queue Status

Yes

Privacy

Yes

Queue Status

Yes

Quality Reporting Tool (QRT)

Yes

Right to Left locale support

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Redial

Yes

Silent Monitoring and Recording

Not supported  by Firmware Release 11.5(1)

This feature is being considered for future releases.

Speed Dial

Yes

Survivable Remote Site Telephony (SRST)

Yes

Transfer

Yes

Uniform Resource Identifier (URI) Dialing

Yes

Video Calls

Yes

Visual Voicemail

Yes

Voicemail

Yes

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide

Cisco IP Phone 8800 Series User Guide

#### Postpone a Phone Upgrade

Users can delay the phone firmware upgrade for 1 hour, up to 11 times.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

#### Opus Audio Codec

The phones now support the Opus audio codec, which offers an improved, higher-quality audio for voice and video calls. Opus is supported on Cisco Unified Communications Manager version 11.0(1) and later.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

#### FIPS 140-2 Level 1 Support

The phones support Federal Information processing standard (FIPS) 140-2 level 1, which requires server certificates to be 2048 bits or greater. The certificates ensure secure communications between the Cisco Unified Communications Manager (Unified CM) and the phone.

Phones with certificates less than 2048 bits cannot register with Unified CM.

FIPS mode is enabled from the Product Specific Configuration Layout portion of the Device Configuration window in Cisco Unified Communications Manager. This feature is supported on Cisco Unified Communications Manager  9.1(2) or higher.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

#### Wireless LAN Profile for Cisco IP Phone 8861 and 8865

Set up a Wireless LAN profile and users can connect to your wireless network without configuring the Wi-Fi client. This helps you control network access while making it easier for users to access your network. You can download and apply one profile to a phone.

To configure a Wireless LAN  profile on Cisco Unified Communication Manager, navigate to Cisco Unified Communications Administration and select Device > Device Settings > Wireless LAN  profile .

You can apply a Wireless LAN profile to just one phone or to a group of phones. But you can configure only one Wireless LAN profile  per group. If the  authentication mode of the  Wireless LAN profile group is None then the existing configured profile is removed.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

#### Network Information

Use the information displayed on the Network Info screen to resolve connection issues on a phone. No configuration  is required.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide

#### Actionable Incoming Call Alert

Show for All Incoming Calls is now the default setting for Actionable Incoming Call Alert.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications Manager is running the latest device pack.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​compat/​devpack_​comp_​mtx.html .

### Install the Firmware Release on Cisco Unified Communications Manager

Before using the
		  phone firmware release on the Cisco Unified Communications Manager, you must
		  install the latest Cisco Unified Communications Manager firmware on all Cisco
		  Unified Communications Manager servers in the cluster.

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283

For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx-sip.11-5-1-18.k3.cop.sgn

For Cisco IP Phone 8845 and 8865—cmterm-8845_65-sip.11-5-1-18.k3.cop.sgn

If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file.

### Install the Firmware Zip Files

If a Cisco Unified
		  Communications Manager is not available to load the installer program, the
		  following .zip files are available to load the firmware.

For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861— cmterm-88xx.11-5-1-18.zip

For Cisco IP Phone 8845 and 8865— cmterm-8845_65.11-5-1-18.zip

Firmware upgrades
		  over the WLAN interface may take longer than upgrades using a wired connection.
		  Upgrade times over the WLAN interface may take more than an hour, depending on
		  the quality and bandwidth of the wireless connection.

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

You can search for
		  caveats using the Cisco Bug Search.

Known caveats
		  (bugs) are graded according to severity level, and can be either open or
		  resolved.

To view caveats,
		  you need the following items:

Internet
				connection

Web browser

Cisco.com user
				ID and password

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

| Cisco IP
					 Phone | Protocol | Support
					 Requirements |
|---|---|---|
| 8811,
					 8841, 8845, 8851, 8851NR, 8861, and 8865 | SIP | Cisco
					 Unified Communications Manager 8.5(1) and later Cisco
					 Unified Communications Manager DST Olsen version D or later SRST 8.0
					 (IOS load 15.1(1)T) and above Cisco Expressway 8.7 |
| 8811,
					 8841,  8851, 8851NR, and 8861 | SIP | CME 10.0
					 (IOS load 15.3(3)M) |

| Note | Some features may require the installation of a Cisco Unified
		  Communications Manager Device Package. Failure to install the Device Package
		  before the phone firmware upgrade may render the phones unusable. |
|---|---|

| Feature | Supported by Firmware Release 11.5(1) | Notes |
|---|---|---|
| Answer | Yes |  |
| Automatically Answer Calls | Yes |  |
| Barge/cBarge | Yes |  |
| Bluetooth Smartphone integration | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Bluetooth USB Headsets | Yes |  |
| Call Back | Yes |  |
| Call Chaperone | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Call Forward All | Yes |  |
| Call Park | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Call Park Line Status | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Call Pickup | Yes |  |
| Call Pickup Line Status | Yes |  |
| CFWA on multiple calls | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Cisco Extension Mobility Cross Cluster | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Cisco IP Manager Assistant (IPMA) | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Cisco Unified Communications Manager Express | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Conference | Yes |  |
| Computer Telephony Integration (CTI) applications | Yes |  |
| Decline | Yes |  |
| Device Invoked Recording | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Directed Park BLF | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Do Not Disturb | Yes |  |
| Enhanced SRST | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Extension Mobility | Yes |  |
| Group Pickup | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Hold | Yes |  |
| Hunt Groups | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Incoming Call Alert with configurable timer | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Intercom | Yes |  |
| Key Expansion Module | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Malicious Call Identification (MCID) | Yes |  |
| Meet Me | Yes |  |
| Mobile Connect | Yes |  |
| Multilevel Precedence and Preemption | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Mute | Yes |  |
| Programmable Line Key (PLK) Support for Queue Status | Yes |  |
| Privacy | Yes |  |
| Queue Status | Yes |  |
| Quality Reporting Tool (QRT) | Yes |  |
| Right to Left locale support | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Redial | Yes |  |
| Silent Monitoring and Recording | Not supported  by Firmware Release 11.5(1) | This feature is being considered for future releases. |
| Speed Dial | Yes |  |
| Survivable Remote Site Telephony (SRST) | Yes |  |
| Transfer | Yes |  |
| Uniform Resource Identifier (URI) Dialing | Yes |  |
| Video Calls | Yes |  |
| Visual Voicemail | Yes |  |
| Voicemail | Yes |  |

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the
			 following URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco
				IP Phone 8800 Series . |
| Step 3 | Choose your
			 phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 11.5(1) . |
| Step 6 | Select the
			 firmware file, click the Download or Add to
				cart button, and follow the prompts: For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx-sip.11-5-1-18.k3.cop.sgn For Cisco IP Phone 8845 and 8865—cmterm-8845_65-sip.11-5-1-18.k3.cop.sgn Note If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. | Note | If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. |
| Note | If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. |
| Step 7 | Click the + next to the firmware file name in the Download
			 Cart section to access additional information about this file. The hyperlink
			 for the readme file is in the Additional Information section, which contains
			 installation instructions for the corresponding firmware. |
| Step 8 | Follow the
			 instructions in the readme file to install the firmware. |

| Note | If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. |
|---|---|

| Step 1 | Go to the
			 following URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco
				IP Phones 8800 Series . |
| Step 3 | Choose your
			 phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 11.5(1) . |
| Step 6 | Download the
			 relevant zip files. |
| Step 7 | Unzip the
			 files. |
| Step 8 | Manually copy
			 the unzipped files to the directory on the TFTP server. See Cisco
				Unified Communications Operating System Administration Guide for
			 information about how to manually copy the firmware files to the server. |

| Step 1 | Perform one of
			 the following actions: |
|---|---|
| Step 2 | When prompted,
			 log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for
			 field, then press Enter . |

| Note | The latest
			 Locale Installer may not be immediately available; continue to check the
			 website for updates. |
|---|---|

| Note | The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer do not update the English user guides on the Cisco Unified Communications Manager. |
|---|---|

| Tip | Administrators may want to bookmark the web pages for the phone models that are deployed in their company and send these URLs to their users. |
|---|---|