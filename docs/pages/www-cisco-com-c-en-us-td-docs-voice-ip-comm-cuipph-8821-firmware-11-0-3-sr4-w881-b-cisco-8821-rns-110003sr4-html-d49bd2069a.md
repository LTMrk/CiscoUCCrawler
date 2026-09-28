---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8821-firmware-11-0-3-sr4-w881-b-cisco-8821-rns-110003sr4-html-d49bd2069a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8821/firmware/11-0-3-SR4/w881_b_cisco-8821-rns-110003sr4.html
retrieved_at: 2026-08-21T13:35:35.140296+00:00
---

Cisco Wireless IP Phone 8821 Release Notes for Firmware Release 11.0(3)SR4

# Cisco Wireless IP Phone 8821 Release Notes for Firmware Release 11.0(3)SR4

### Download Options

Updated: October 26, 2017

First Published:

Last Updated:

Text Part Number:

# Cisco Wireless IP Phone 8821 Release Notes for Firmware Release 11.0(3)SR4

These release notes support the Cisco Wireless IP Phone 8821 Firmware Release 11.0(3)SR4.

The following table describes the systems and versions that the phone requires.

System

Minimum Version

Recommended Versions

Cisco Unified Communications Manager

9.1(2)

10.5(2), 11.0(1), 11.5(1), and later

Cisco Unified Communications Manager Express

10.5 through Fast Track

11.0, 11.5, 11.7 (native support), and later

Cisco Unified Survivable Remote Site Telephony

10.5

11.0, 11.5, 11.7, and later

Cisco Wireless LAN Controller

8.0.121.0

8.0.140.0, 8.2.160.0, 8.3.112.0

Cisco IOS Access Points (Autonomous)

12.4(21a)JY

12.4(25d)JA2, 15.2(4)JB6, 15.3(3)JE

Cisco Meraki

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

#### OPUS Codec Support

The Cisco Wireless IP Phone 8821 supports the OPUS codec, starting with Firmware Release 11.0(3)SR4. The OPUS codec provides improved speech and music transmission.

##### Where to Find More Information

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

#### Bulk Deployment Utility

The Bulk Deployment Utility (BDU) for the Cisco Wireless IP Phone 8821 and 8821-EX can be used for initial deployment or after the phones have been deployed. The BDU provides quick provisioning and deployment when unique 802.1x accounts are used with EAP-FAST, PEAP-GTC, or PEAP-MSCHAPV2 or when a common set of credentials are used by all phones (for example, PSK or a single 802.1x account).

The BDU requires Firmware Release 11.0(3)SR4 or later on the phones.

This version of the BDU is not the same as the BDU for the Cisco Unified Wireless IP Phone 792x Series.

You download the BDU from this location:

https:/​/​software.cisco.com/​download/​type.html?mdfid=286308995&flowid=80142

For more information, see the Bulk Deployment Utility Guide for Cisco Wireless Phone 8821 and 8821-EX located here: https:/​/​www.cisco.com/​web/​software/​282074239/​14006/​882xBD.1-0-readme.pdf .

## Related
	 Documentation

Use the following sections to
		obtain related information.

### Cisco Wireless IP Phone 882x Series Documentation

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

### Cisco Unified
				Communications Manager Express Documentation

See the publications that are specific to your language, phone model and Cisco Unified
				Communications Manager Express release. Navigate from the following documentation URL:

https:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-express/​tsd-products-support-series-home.html

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications Manager is running the latest device pack. After you install a device pack on the Cisco Unified Communications Manager servers in the cluster, you need to reboot all the servers.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​compat/​devpack_​comp_​mtx.html .

### Install Firmware Release 11.0(3)SR4 on Cisco Unified Commmunications Manager

Before you can use the phone firmware release on the Cisco Unified Communications Manager, you must install the latest Cisco Unified Communications Manager firmware on all Cisco Unified Communications Manager servers in the cluster.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm

Firmware file: cmterm-8821-sip.11-0-3SR4-3.k3.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

### Install Firmware Release 11.0(3)SR4 on Cisco Commmunications Manager Express

You must download the Cisco Wireless IP Phone 8821 firmware image file from the software download center.

For information on Cisco Unified Communications Manager Express support, see http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucme/​feature/​phone_feature/​phone_​feature_​support_​guide.html .

For more information about this procedure, refer to the "Install and Upgrade Cisco Unified CME Software" chapter in the Cisco Unified Communications Manager Express System Administrator Guide at this URL:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucme/​admin/​configuration/​manual/​cmeadm.html

https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283

The file to download is cmterm-8821.11-0-3SR4-3.zip

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

### Recording Tone Volume Limitation

If you use the recording feature, we recommend that you change the Recording Tone Local Volume configured in Cisco Unified Communications Manager. Change the field from the default of 100 to 20.

The CUCM device packs (October 2017 and later) have the default set to 20.

For more information, look at CSCvc14605 using https:/​/​tools.cisco.com/​bugsearch .

## View Caveats

You can search for caveats using the Cisco Bug Search tool.

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

For information on the support policy for phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

| System | Minimum Version | Recommended Versions |
|---|---|---|
| Cisco Unified Communications Manager | 9.1(2) | 10.5(2), 11.0(1), 11.5(1), and later |
| Cisco Unified Communications Manager Express | 10.5 through Fast Track | 11.0, 11.5, 11.7 (native support), and later |
| Cisco Unified Survivable Remote Site Telephony | 10.5 | 11.0, 11.5, 11.7, and later |
| Cisco Wireless LAN Controller | 8.0.121.0 | 8.0.140.0, 8.2.160.0, 8.3.112.0 |
| Cisco IOS Access Points (Autonomous) | 12.4(21a)JY | 12.4(25d)JA2, 15.2(4)JB6, 15.3(3)JE |
| Cisco Meraki |  |  |

| Note | Some features may require the installation of a Cisco Unified
		  Communications Manager Device Package. Failure to install the Device Package
		  before the phone firmware upgrade may render the phones unusable. |
|---|---|

| Note | This version of the BDU is not the same as the BDU for the Cisco Unified Wireless IP Phone 792x Series. |
|---|---|

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phone 8800 Series . |
| Step 3 | Choose Cisco Wireless IP Phone 8821 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 11.0(3)SR4 . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. Firmware file: cmterm-8821-sip.11-0-3SR4-3.k3.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink for the readme file is in the Additional Information section, which contains installation instructions for the corresponding firmware. |
| Step 8 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Step 1 | To access the firmware files, go to this URL: https:/​/​software.cisco.com/​download/​navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco Wireless IP Phone 8821 . |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | Choose 11.0(3)SR4 in the Latest Releases folder. |
| Step 5 | Click Download or Add to cart and follow the prompts. The file to download is cmterm-8821.11-0-3SR4-3.zip |
| Step 6 | Extract the files from the zip file, manually copy them to the Cisco Unified Communications Manager Express TFTP server (router flash), and enable them for TFTP. |

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