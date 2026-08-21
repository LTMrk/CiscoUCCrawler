---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-english-releasenotes-p881-bk-cab208a2-00-cisco-ip-phone-8-4e850b6898
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/releasenotes/P881_BK_CAB208A2_00_cisco-ip-phone-8800-series.html
retrieved_at: 2026-08-21T13:32:46.231136+00:00
---

Cisco IP Phone 8800 Series Release Notes for Firmware Release 10.3(2)

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 10.3(2)

### Download Options

Updated: August 31, 2015

First Published: July 13, 2015

Last Updated: August 31, 2015

# Introduction

These release
		  notes support the Cisco IP Phone 8845 and 8865 running SIP Firmware Release
		  10.3(2).

The following
		  table lists the support and protocol compatibility for the Cisco IP Phones.

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

8811,
					 8841, 8851, 8851NR, and 8861

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

## New and Changed Features

### Features Available
	 with the Firmware Release

The following sections describe the features available with the Firmware
		Release.

#### Cisco IP Phone
	 8845 and 8865

Firmware Release
		  10.3(2) introduces support for Cisco IP Phone 8845 and 8865, full feature Cisco
		  IP Phones with video capability. In addition to video calls, Cisco IP Phone
		  8845 and 8865 function much like a digital business phone, allowing you to
		  place and receive calls and to access features such as mute, hold, transfer,
		  speed dial, call forward, and more. The Cisco IP Phone 8845 and 8865 also
		  supports telephony feature integration with your personal mobile devices using
		  Cisco Intelligent Proximity for Mobile Voice.

For general information about the features and technical details of
		  Cisco IP Phone 8845 and 8865, see http:/​/​www.cisco.com/​c/​en/​us/​products/​collaboration-endpoints/​unified-ip-phone-8800-series/​index.html .

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide for Cisco
				  Unified Communications Manager

Cisco IP Phone 8800 Series User Guide for Cisco Unified
				  Communications Manager

### Features Available
	 with the Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require
		the new firmware and the latest Cisco Unified Communications Manager Device
		Pack.

For information about the Cisco Unified IP Phones and the required Cisco
		Unified Communications Manager device packs, see the following URL:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​compat/​devpack_​comp_​mtx.html

#### Mobile and Remote Access
				Through Expressway (Market Beta)

The Mobile and Remote Access
				Through Expressway feature provides a way for remote workers to easily and securely connect into
		  the corporate network without using a virtual private network (VPN) client
		  tunnel.

The marketing
			 beta release of Mobile and Remote Access Through Expressway is made available
			 to allow customers to test and evaluate the feature, but is NOT recommended for
			 production use. There is no official Cisco TAC support until the feature is
			 officially released in a future firmware load. For those who want to provide
			 feedback, send an email to cefeedback@cisco.com.

This feature
		  requires Cisco Expressway version 8.5.2 and Cisco Unified Communications
		  Manager version 10.5.2 SU2 or later to operate in the Beta trial.

The feature uses
		  Transport Layer Security (TLS) to secure network traffic.

Abbreviated
				Dialing

Assisted
				Directed Call Park

Busy Lamp
				Field

Busy Lamp
				Field Pickup

Busy Lamp
				Field Speed Dial

Call Back

Call Forward

Call Forward
				Notification

Call Park

Call Pickup

Conference

Direct
				Transfer

Directed Call
				Park

Divert

Do Not Disturb

Group Call
				Pickup

Hold and
				Resume - There is a known issue of one - way audio after 25 minutes on a
				PSTN/Jabber call when the user holds and resumes the call ( CSCut64844 )

Hold Reversion

Immediate
				Divert

Join

MeetMe
				Conference

Message
				Waiting Indicator

Mobile Connect

Mobile Voice
				Access

Music On Hold

Mute

Off-Hook
				Dialing

On-Hook
				Dialing

Plus Dialing

Redial

Speed Dial

Transfer

Uniform
				Resource Identifier Dialing

Some major call
		  features, like multiple lines, shared lines, Extension Mobility, CTI,
		  monitoring, and recording, are not supported in Expressway mode.

The feature is
		  supported on the following phones:

Cisco IP Phone
				8811

Cisco IP Phone
				8841

Cisco IP Phone
				8851

Cisco IP Phone
				8851NR

Cisco IP Phone
				8861

##### Where to Find
		  More Information

Cisco IP Phone 8811, 8841,
				  8851, 8851NR, and 8861 Administration Guide for Cisco Unified Communications
				  Manager 10.5

Cisco IP Phone 8811, 8841,
				  8851, 8851NR, and 8861 User Guide for Cisco Unified Communications Manager
				  10.5

Cisco Expressway X8.5.2
				  Software Release Notes

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications Manager is running the latest device pack.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​compat/​devpack_​comp_​mtx.html .

### Install Firmware
	 Release on Cisco Unified Communications Manager

Before using the
		  phone firmware release on the Cisco Unified Communications Manager, you must
		  install the latest Cisco Unified Communications Manager firmware on all Cisco
		  Unified Communications Manager servers in the cluster.

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283

If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file.

### Install Firmware
	 Zip Files

If a Cisco Unified
		  Communications Manager is not available to load the installer program, the
		  following .zip files are available to load the firmware.

cmterm-8845_65.10-3-2-16.zip

Firmware upgrades
		  over the WLAN interface may take longer than upgrades using a wired connection.
		  Upgrade times over the WLAN interface may take more than an hour, depending on
		  the quality and bandwidth of the wireless connection.

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283

## Limitations and Restrictions

### Phone Behavior
	 During Times of Network Congestion

Anything that
		  degrades network performance can affect Cisco IP Phone voice and video quality,
		  and in some cases, can cause a call to drop. Sources of network degradation can
		  include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that
				occur on your network, such as a Denial of Service attack

### Health-Care
	 Environment Use

This product is not a
		medical device and uses an unlicensed frequency band that is susceptible to
		interference from other devices or equipment.

## View
	 Caveats

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
					 (IOS load 15.1(1)T) and above |
| 8811,
					 8841, 8851, 8851NR, and 8861 | SIP | CME 10.0
					 (IOS load 15.3(3)M) |

| Note | The marketing
			 beta release of Mobile and Remote Access Through Expressway is made available
			 to allow customers to test and evaluate the feature, but is NOT recommended for
			 production use. There is no official Cisco TAC support until the feature is
			 officially released in a future firmware load. For those who want to provide
			 feedback, send an email to cefeedback@cisco.com. |
|---|---|

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the
			 following URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Depending on
			 your phone model, choose Cisco
				IP Phone 8800 Series . |
| Step 3 | Choose your
			 phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 10.3(2) . |
| Step 6 | Select the
			 firmware file cmterm-8845_65-sip.10-3-2-16.k3.cop.sgn, click the Download or Add to
				cart button, and follow the prompts: Note If you added
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
			 phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 10.3(2) . |
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
| Step 3 | To look for
			 information about a specific problem, enter the bug ID number in the Search for
			 field, then press Enter . |

| Note | The latest
			 Locale Installer may not be immediately available; continue to check the
			 website for updates. |
|---|---|

| Note | The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer do not update the English user guides on the Cisco Unified Communications Manager. |
|---|---|

| Tip | Administrators may want to bookmark the web pages for the phone models that are deployed in their company and send these URLs to their users. |
|---|---|