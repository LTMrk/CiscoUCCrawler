---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8821-firmware-11-0-2-sr1-w88x-b-cisco-8821-rns-110002sr1-html-2320da014b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8821/firmware/11-0-2-SR1/w88x_b_cisco-8821-rns-110002sr1.html
retrieved_at: 2026-08-21T13:35:43.163236+00:00
---

Cisco Wireless IP Phone 8821 Release Notes for Firmware Release 11.0(2)SR1

# Cisco Wireless IP Phone 8821 Release Notes for Firmware Release 11.0(2)SR1

First Published: August 24, 2016

Last Updated: June 26, 2017

# Cisco Wireless IP Phone 8821 Release Notes for Firmware Release 11.0(2)SR1

These release notes support the Cisco Wireless IP Phone 8821 Firmware Release 11.0(2)SR1.

The following table describes the systems and versions that the phone requires.

System

Minimum Version

Recommended Versions

Cisco Unified Communications Manager

9.1(2)

9.1(2),10.5(2), 11.0(1), 11.5(1),and later

Cisco Communications Manager Express

10.5 through Fast Track

See http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucme/​feature/​phone_feature/​phone_​feature_​support_​guide.html

Cisco Wireless LAN Controller

8.0.121.0

8.0.135.0, 8.1.131.0, 8.2.110.0 and later.

Cisco IOS Access Points (Autonomous)

12.4(21a)JY

12.4(25d)JA2, 15.2(4)JB6, 15.3(3)JAB

Cisco Meraki

## New and Changed Features

This release contains no new or changed features.

## Related
	 Documentation

Use the following sections to
		obtain related information.

### Cisco Wireless IP Phone 882x Series Documentation

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

### Cisco Unified
				Communications Manager Express Documentation

See the publications that are specific to your language, phone model and Cisco Unified
				Communications Manager Express release. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-express/​tsd-products-support-series-home.html

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications Manager is running the latest device pack. After you install a device pack on the Cisco Unified Communications Manager servers in the cluster, you need to reboot all the servers.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​compat/​devpack_​comp_​mtx.html .

### Install Firmware Release 11.0(2)SR1 on Cisco Unified Communications Manager

Before you can use the
		  phone firmware release on the Cisco Unified Communications Manager, you must
		  install the latest Cisco Unified Communications Manager firmware on all Cisco
		  Unified Communications Manager servers in the cluster. 
		For this release, you must also install the device pack that provides support for the Cisco Wireless IP Phone 8821.

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286308995&i=rm

Firmware file: cmterm-8821-sip.11-0-2SR1-1.k3.cop.sgn

If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file.

### Install the 11.0(2)SR1 Firmware Zip File

If a Cisco Unified
		  Communications Manager is not available to load the installer program, the
		  following .zip file is available to load the firmware:

cmterm-8821.11-0-2SR1-1.zip

Firmware upgrades
		  over the WLAN interface may take longer than upgrades using a wired connection.
		  Upgrade times over the WLAN interface may take more than an hour, depending on
		  the quality and bandwidth of the wireless connection.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm

### Install Firmware Release 11.0(2)SR1 on Cisco Unified Communications Manager Express

You must download the Cisco Wireless IP Phone 8821 firmware image file from the software download center.

For information on Cisco Unified Communications Manager Express support, see http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucme/​feature/​phone_feature/​phone_​feature_​support_​guide.html .

For more information about this procedure, refer to the "Install and Upgrade Cisco Unified CME Software" chapter in the Cisco Unified Communications Manager Express System Administrator Guide at this URL:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucme/​admin/​configuration/​manual/​cmeadm.html

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283

The file to download is cmterm-8821.11-0-2SR1-1.zip

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

## View Caveats

You can search for
		  caveats using the Cisco Bug Search tool.

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

| System | Minimum Version | Recommended Versions |
|---|---|---|
| Cisco Unified Communications Manager | 9.1(2) | 9.1(2),10.5(2), 11.0(1), 11.5(1),and later |
| Cisco Communications Manager Express | 10.5 through Fast Track | See http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucme/​feature/​phone_feature/​phone_​feature_​support_​guide.html |
| Cisco Wireless LAN Controller | 8.0.121.0 | 8.0.135.0, 8.1.131.0, 8.2.110.0 and later. |
| Cisco IOS Access Points (Autonomous) | 12.4(21a)JY | 12.4(25d)JA2, 15.2(4)JB6, 15.3(3)JAB |
| Cisco Meraki |  |  |

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the
			 following URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=286308995&i=rm |
|---|---|
| Step 2 | Choose Cisco
				IP Phone 8800 Series . |
| Step 3 | Choose Cisco Wireless IP Phone 8821 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 11.0(2)SR1 . |
| Step 6 | Select the
			 firmware file, click the Download or Add to
				cart button, and follow the prompts. Firmware file: cmterm-8821-sip.11-0-2SR1-1.k3.cop.sgn Note If you added
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
			 following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco
				IP Phones 8800 Series . |
| Step 3 | Choose Cisco Wireless IP Phone 8821 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 11.0(2)SR1 . |
| Step 6 | Download the
			 relevant zip file. |
| Step 7 | Unzip the
			 files. |
| Step 8 | Manually copy
			 the unzipped files to the directory on the TFTP server. See Cisco
				Unified Communications Operating System Administration Guide for
			 information about how to manually copy the firmware files to the server. |

| Step 1 | To access the firmware files, go to this URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco Wireless IP Phone 8821 . |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | Choose 11.0(2)SR1 in the Latest Releases folder. |
| Step 5 | Click Download or Add to cart and follow the prompts. The file to download is cmterm-8821.11-0-2SR1-1.zip |
| Step 6 | Extract the files from the zip file, manually copy them to the Cisco Unified Communications Manager Express TFTP server (router flash), and enable them for TFTP. |

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