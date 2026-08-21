---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8811-8841-8851-8861-firmware-10-3-1-releasenotes-p881-bk-ca4c768a-00--84efe53e4a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8811_8841_8851_8861/firmware/10-3-1/releasenotes/P881_BK_CA4C768A_00_cisco-ip-phone-8800-series.html
retrieved_at: 2026-08-21T13:33:19.239548+00:00
---

Cisco IP Phone 8800 Series Release Notes for Firmware Release 10.3(1)

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 10.3(1)

### Download Options

Updated: August 31, 2015

First Published: May 07, 2015

Last Updated: August 31, 2015

# Introduction

These release
		  notes support the Cisco IP Phones 8811, 8841, 8851, 8851NR, and 8861 running
		  SIP Firmware Release 10.3(1).

The following
		  table lists the support and protocol compatibility for the Cisco IP Phones.

Cisco IP
					 Phone

Protocol

Support
					 Requirements

Cisco IP
					 Phones 8811, 8841, 8851, 8851NR, and 8861

SIP

Cisco
					 Unified Communications Manager 8.5(1) and later

Cisco
					 Unified Communications Manager DST Olsen version D or later

SRST 8.0
					 (IOS load 15.1(1)T) and above

CME 10.0
					 (IOS load 15.3(3)M) and above through Fast-Track

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

#### Cisco IP Phone
	 8851NR Support

Firmware Release
		  10.3(1) introduces support for Cisco IP Phone 8851NR. This phone delivers the
		  same features as Cisco IP Phone 8851, with the exception of Bluetooth support.
		  Cisco IP Phone 8851NR does not support Bluetooth or any Bluetooth dependent
		  features.

##### Where to Find
		  More Information

Cisco IP Phone 8811, 8841,
				  8851, 8851NR, and 8861 Administration Guide for Cisco Unified Communications
				  Manager 10.5

Cisco IP Phone 8811, 8841,
				  8851, 8851NR, and 8861 User Guide for Cisco Unified Communications Manager
				  10.5

#### AES 256 Encryption
	 Support for TLS and SIP SRTP

The AES 256 Encryption Support for Phones feature enables the phones
		  to take advantage of the AES 256 Encryption Support for TLS and SIP SRTP
		  feature in Cisco Unified Communications Manager Release 10.5(2) and later.

With Cisco Unified Communications Manager Release 10.5(2), the AES
		  256 encryption support for TLS and SIP SRTP is enhanced to focus on AES 256
		  cipher support in signaling and media encryption. This feature enables phones
		  to initiate and support TLS 1.2 connections with the AES-256 based ciphers that
		  conform to SHA-2 (Secure Hash Algorithm) standards and is Federal Information
		  Processing Standards (FIPS) compliant.

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

For more
		  information, see the Release Notes
			 for Cisco Unified Communications Manager Release 10.5(2) and IM and Presence
			 Service Release 10.5(2b) located at http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​products-release-notes-list.html .

### Features Available
	 with the Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require
		the new firmware and the latest Cisco Unified Communications Manager Device
		Pack.

For information about the Cisco Unified IP Phones and the required Cisco
		Unified Communications Manager device packs, see the following URL:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​compat/​devpack_​comp_​mtx.html

#### Configurable
	 Energy Efficient Ethernet for PC and Switch Port

The Configurable
		  Energy Efficient Ethernet (EEE) feature enables the administrator to control
		  the EEE function on the personal computer port and switch port. IEEE 802.3az
		  Energy Efficient Ethernet is an extension of the IEEE 802.3 standard that
		  provides a method for reducing energy usage without reducing the vital function
		  of network interfaces.

This feature is enabled by default.

Energy Efficient
				  Ethernet : PC Port: Provides seamless connection with personal computers.
				Administrator can select Enabled or Disabled options to control the function.

Energy
				  Efficient Ethernet : Switch Port: Provides seamless connection

Administrators  can turn this feature off if they are experiencing  performance issues on a PC connected to the phone,  or a phone connected to an upstream switch port.

EEE has no user
		  impact.

Configurable
		  Energy Efficient Ethernet is supported on the following phones:

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

#### Problem Report
	 Tool

The Problem Report
		  Tool (PRT) feature provides users with a way to submit phone logs or report
		  problems to their administrator.

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

cmterm-88xx.10-3-1-20.zip

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

To find
					 all caveats for this release, use this URL: Caveats

To find
					 all open caveats for this release, use this URL: Open Caveats

To find
					 all resolved caveats for this release, use this URL: Resolved Caveats

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
| Cisco IP
					 Phones 8811, 8841, 8851, 8851NR, and 8861 | SIP | Cisco
					 Unified Communications Manager 8.5(1) and later Cisco
					 Unified Communications Manager DST Olsen version D or later SRST 8.0
					 (IOS load 15.1(1)T) and above CME 10.0
					 (IOS load 15.3(3)M) and above through Fast-Track |

| Note | Some features may require the installation of a Cisco Unified
			 Communications Manager Device Package. Failure to install the Device Package
			 before the phone firmware upgrade may render the phones unusable. |
|---|---|

| Note | Administrators must confirm that the Override Check box is checked on all applicable  UCM pages or EEE  will not function. |
|---|---|

| Note | If you are in
		  on-premises mode then the PRT feature is only available for log collection. |
|---|---|

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
			 Releases folder, choose 10.3(1) . |
| Step 6 | Select the
			 firmware file cmterm-88xx-sip.10-3-1-20.k3.cop.sgn, click the Download or Add to
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
			 Releases folder, choose 10.3(1) . |
| Step 6 | Download the
			 relevant zip files. |
| Step 7 | Unzip the
			 files. |
| Step 8 | Manually copy
			 the unzipped files to the directory on the TFTP server. See Cisco
				Unified Communications Operating System Administration Guide for
			 information about how to manually copy the firmware files to the server. |

| Step 1 | Perform one of
			 the following actions: To find
					 all caveats for this release, use this URL: Caveats To find
					 all open caveats for this release, use this URL: Open Caveats To find
					 all resolved caveats for this release, use this URL: Resolved Caveats |
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