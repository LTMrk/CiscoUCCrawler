---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-6901-6911-firmware-9-3-1-sr3-p069-b-6901-rn-931sr3-html-2717a31a4d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/6901_6911/firmware/9_3_1_SR3/p069_b_6901-rn-931sr3.html
retrieved_at: 2026-08-21T06:23:49.086881+00:00
---

Cisco Unified IP Phone 6901 Release Notes for Firmware Release 9.3(1)SR3 (SCCP and SIP)

# Cisco Unified IP Phone 6901 Release Notes for Firmware Release 9.3(1)SR3 (SCCP and SIP)

### Download Options

Updated: September 7, 2023

First Published: September 7, 2023

# Introduction

These release notes support the Cisco Unified IP Phone 6901 running SIP Firmware Release 9.3(1)SR3.

The following table lists the Cisco Unified Communications Manager release and protocol compatibility for the Cisco IP Phones.

Cisco IP Phone

Protocol

Cisco Unified Communications Manager

Cisco Unified IP Phone 6901

SIP

Cisco Unified Communications Manager Release 7.1(5) and later.

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco Unified IP Phone 6900 Series Documentation

Refer to publications that are specific to your language, phone model and Cisco Unified
                           				Communications Manager release. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-6900-series/tsd-products-support-series-home.html

### Cisco Unified
                     				Communications Manager Documentation

See the Cisco Unified
                              				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                           				Communications Manager release on the product support page.

### Cisco Business Edition
                     				3000 Documentation

See the Cisco Business Edition
                              				3000 Documentation Guide and other publications that are specific to your Cisco Business Edition
                           				3000 release. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/unified-communications/business-edition-3000/tsd-products-support-series-home.html

### Cisco Business Edition
                     				5000 Documentation

See the Cisco Business Edition
                              				5000 Documentation Guide and other publications that are specific to your Cisco Business Edition
                           				5000 release. Navigate from the following URL:

https://www.cisco.com/c/en/us/support/unified-communications/business-edition-5000/tsd-products-support-series-home.html

### Cisco Unified
                     				Communications Manager Express Documentation

See the publications that are specific to your language, phone model, and release on the product support page for Cisco Unified
                              				Communications Manager Express .

## New and Changed Features

This release contains no new or changed features.

## Installation

### Upgrade Notes

Direct upgrades, using signed load files, are supported to firmware release 9.3(1)SR3 from 9.x. You can use the following
                        firmware release file for these direct upgrades.

Firmware Release 9.3(1)SR3 only applies to the Cisco Unified IP Phone 6901.

cmterm-6901-sip.9-3-1-SR3-1.k4.cop.sha512

cmterm-6901-sccp.9-3-1-SR3-1.k4.cop.sha512

### Install Firmware Release on Cisco Unified Communications Manager

Before using the Cisco Unified IP Phone Firmware Release 9.3(1)SR3 with Cisco Unified Communications Manager, you must install
                        the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

Firmware Release 9.3(1)SR3 only applies to the Cisco Unified IP Phone 6901.

Step 1

Go to the following URL:

https://software.cisco.com/download/home/282933048/type

Step 2

Choose one of the following firmware types:

Session Initiation Protocol (SIP) Software

Skinny Client Control Protocol (SCCP) Software

Step 3

In the Latest Releases folder, choose 9.3(1)SR3 .

Step 4

Select one of the following firmware files, click the Download Now or Add to cart button, and follow the prompts:

The files for the Cisco Unified IP Phone 6901 are:

cmterm-6901-sip.9-3-1-SR3-1.k4.cop.sha512

cmterm-6901-sccp.9-3-1-SR3-1.k4.cop.sha512

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Step 5

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware:

cmterm-6901-sip.9-3-1-SR3-1-readme.html

cmterm-6901-sccp.9-3-1-SR3-1-readme.html

Step 6

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following .zip files are available
                        to load the firmware.

Firmware Release 9.3(1)SR3 only applies to the Cisco Unified IP Phone 6901.

SIP: cmterm-6901-sip.9-3-1-SR3-1.zip

SCCP: cmterm-6901-sccp.9-3-1-SR3-1.zip

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                                    interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Step 1

Go to the following URL:

https://software.cisco.com/download/home/282933048/type

Step 2

Choose one of the following firmware types:

Session Initiation Protocol (SIP) Software

Skinny Client Control Protocol (SCCP) Software

Step 3

In the Latest Releases folder, choose 9.3(1)SR3 .

Step 4

Download the relevant zip files.

Step 5

Unzip the files.

Step 6

Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server.

## Limitations and Restrictions

### Phone Limitation During SVI Change

Cisco IP Phones use a Switch Virtual Interface (SVI) to manage VLANs. If the SVI changes and the phones require new IP addresses,
                        some phones require a reboot so that the new IP address is used. The following phones must be rebooted in this condition:

Cisco Unified IP Phone 6901

Cisco Unified IP Phone 6911

Cisco Unified IP Phone 6921

Cisco Unified IP Phone 6941

Cisco Unified IP Phone 6945

Cisco Unified IP Phone 6961

Cisco Unified IP Phone 8941

Cisco Unified IP Phone 8945

Cisco Unified IP Phone 8961

Cisco Unified IP Phone 9951

Cisco Unified IP Phone 9971

### Phone Behavior
                  	 During Times of Network Congestion

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

### On-Hook Transfer Limitation in SIP Phones

When the Cisco Unified Communications Manager Transfer On-Hook Enabled field is enabled, users might report a problem with direct call transfer in SIP phones. If the user transfers the call and
                        immediately goes on hook before they hear the ring signal, the call may drop instead of being transferred.

The user needs to hear the ring signal so that they can be sure that the call is being routed.

## Caveats

This section
                     		  describes the resolved and open caveats, and provides information on accessing
                     		  the Cisco Software Bug Toolkit.

### Access Cisco Bug
                  	 Search

Known problems
                        		  (bugs) are graded according to severity level. These release notes contain
                        		  descriptions of the following:

All severity
                              				level 1 or 2 bugs

Significant
                              				severity level 3 bugs

You can search for
                        		  problems by using Cisco Bug Search.

Before you begin

#### Before you begin

To access Cisco Bug
                        		  Search, you need the following items:

Internet
                              				connection

Web browser

Cisco.com user
                              				ID and password

Step 1

To access Cisco Bug Search, go to:

https://tools.cisco.com/bugsearch

Step 2

Log in with your
                                 			 Cisco.com user ID and password.

Step 3

To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter .

### Open Caveats

The following table lists severity 1, 2, and 3 defects that are open for the Cisco Unified IP Phones 6901  for Firmware Release
                        9.3(1)SR3.

For more information about an individual defect, you can access the online record for the defect by clicking the Identifier
                        or going to the URL that is shown. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCud26030

6901 SCCP: DUT can't setup secure conference in secure SRST

CSCuj76132

Not re-request config file if get TFTP "Disk full or allocation exceed"

### Resolved Caveats

The following table lists severity 1, 2, and 3 defects that are resolved for the Cisco Unified IP Phones 6901 for Firmware
                        Release 9.3(1)SR3.

For more information about an individual defect, you can access the online record for the defect by clicking the Identifier
                        or going to the URL that is shown. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were resolved at the time this
                        report was compiled. For an updated view of resolved defects, access Bug Toolkit as described in Access Cisco Bug Search .

Identifier

Headline

CSCud21672

6901 : LSC certificates cannot be installed on 6901 SCCP phone

CSCuf20123

CP-6901 Unable to hear a particular IP Address range of Multicast MoH

CSCuo12086

Phone 6901 No audio via a CUBE SIP Trunk

CSCuo35614

Cannot change locale on 6901 & 6911 registered to CME

CSCus13427

6901-CL SCCP phone will not register in SRST when secured

CSCva55382

6901 phones fails to register after sudden WAN outage

CSCvx62505

Cisco IP Phone Cisco Discovery Protocol Out-of-Bound Read Vulnerability on DeviceID

CSCvx62541

Cisco IP Phone Cisco Discovery Protocol Out-of-Bound Read Vulnerability on Addresses TLV

CSCvt27640

Evaluation of odm_jdm_phones for call logs in unauthenticated serviceability web UI

CSCwf58592

Evaluation of stored XSS vulnerability on odm_jdm_phones

CSCun05383

Certificate size is too small on 6901 phones for 802.1x Authentication

CSCus48540

6901 ip phone not registering to CUCM with 802.1x authentication

CSCuu15108

6901 phones with 802.1x sending EAPol-Start just once

CSCuv12329

6901 fails to upgrade the CTL

CSCud19323

6901/11 Factory reset does not erase the existing Locale(CME only)

CSCvp59887

6901 phones don't negotiate the dot1x

CSCvm09579

Upgrade BusyBox to resolve CVE-2015-9261

CSCvq19697

Evaluation of odm_jdm_phones for TCP_SACK

CSCvv42735

TCP Sequence Number Approximation Based Denial of Service (CVE-2004-0230)

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

## Cisco IP Phone Documentation Updates on Cisco Unified Communications Manager

The Cisco Unified Communications Manager Self Care Portal (Release 10.0 and later) and User Options web pages (Release 9.1
                     and earlier) provide  links to the IP Phone user guides in PDF format. These user guides are stored on the Cisco Unified Communications
                     Manager and are up to date when the Cisco Unified Communications Manager release is first made available to customers.

After a Cisco Unified Communications Manager release, subsequent updates to the user guides appear only on the Cisco website.
                     The phone firmware release notes contain the applicable documentation URLs. In the web pages, updated documents display "Updated" beside the document link.

The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer
                                 do not update the English user guides on the Cisco Unified Communications Manager.

You and your users should check the Cisco website for updated user guides and download the PDF files. You can also make the
                     files available to your users on your company website.

Tip

You may want to bookmark the web pages for the phone models that are deployed in your company and send these URLs to your
                                 users.

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Cisco IP Phone | Protocol | Cisco Unified Communications Manager |
|---|---|---|
| Cisco Unified IP Phone 6901 | SIP | Cisco Unified Communications Manager Release 7.1(5) and later. |

| Note | Firmware Release 9.3(1)SR3 only applies to the Cisco Unified IP Phone 6901. |
|---|---|

| Note | Firmware Release 9.3(1)SR3 only applies to the Cisco Unified IP Phone 6901. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/home/282933048/type |
|---|---|
| Step 2 | Choose one of the following firmware types: Session Initiation Protocol (SIP) Software Skinny Client Control Protocol (SCCP) Software |
| Step 3 | In the Latest Releases folder, choose 9.3(1)SR3 . |
| Step 4 | Select one of the following firmware files, click the Download Now or Add to cart button, and follow the prompts: The files for the Cisco Unified IP Phone 6901 are: cmterm-6901-sip.9-3-1-SR3-1.k4.cop.sha512 cmterm-6901-sccp.9-3-1-SR3-1.k4.cop.sha512 Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 5 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware: cmterm-6901-sip.9-3-1-SR3-1-readme.html cmterm-6901-sccp.9-3-1-SR3-1-readme.html |
| Step 6 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Note | Firmware Release 9.3(1)SR3 only applies to the Cisco Unified IP Phone 6901. |
|---|---|

| Note | Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                                    interface may take more than an hour, depending on the quality and bandwidth of the wireless connection. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/home/282933048/type |
|---|---|
| Step 2 | Choose one of the following firmware types: Session Initiation Protocol (SIP) Software Skinny Client Control Protocol (SCCP) Software |
| Step 3 | In the Latest Releases folder, choose 9.3(1)SR3 . |
| Step 4 | Download the relevant zip files. |
| Step 5 | Unzip the files. |
| Step 6 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

| Step 1 | To access Cisco Bug Search, go to: https://tools.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                                 			 Cisco.com user ID and password. |
| Step 3 | To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter . |

| Identifier | Headline |
|---|---|
| CSCud26030 | 6901 SCCP: DUT can't setup secure conference in secure SRST |
| CSCuj76132 | Not re-request config file if get TFTP "Disk full or allocation exceed" |

| Identifier | Headline |
|---|---|
| CSCud21672 | 6901 : LSC certificates cannot be installed on 6901 SCCP phone |
| CSCuf20123 | CP-6901 Unable to hear a particular IP Address range of Multicast MoH |
| CSCuo12086 | Phone 6901 No audio via a CUBE SIP Trunk |
| CSCuo35614 | Cannot change locale on 6901 & 6911 registered to CME |
| CSCus13427 | 6901-CL SCCP phone will not register in SRST when secured |
| CSCva55382 | 6901 phones fails to register after sudden WAN outage |
| CSCvx62505 | Cisco IP Phone Cisco Discovery Protocol Out-of-Bound Read Vulnerability on DeviceID |
| CSCvx62541 | Cisco IP Phone Cisco Discovery Protocol Out-of-Bound Read Vulnerability on Addresses TLV |
| CSCvt27640 | Evaluation of odm_jdm_phones for call logs in unauthenticated serviceability web UI |
| CSCwf58592 | Evaluation of stored XSS vulnerability on odm_jdm_phones |
| CSCun05383 | Certificate size is too small on 6901 phones for 802.1x Authentication |
| CSCus48540 | 6901 ip phone not registering to CUCM with 802.1x authentication |
| CSCuu15108 | 6901 phones with 802.1x sending EAPol-Start just once |
| CSCuv12329 | 6901 fails to upgrade the CTL |
| CSCud19323 | 6901/11 Factory reset does not erase the existing Locale(CME only) |
| CSCvp59887 | 6901 phones don't negotiate the dot1x |
| CSCvm09579 | Upgrade BusyBox to resolve CVE-2015-9261 |
| CSCvq19697 | Evaluation of odm_jdm_phones for TCP_SACK |
| CSCvv42735 | TCP Sequence Number Approximation Based Denial of Service (CVE-2004-0230) |

| Note | The latest
                                 			 Locale Installer may not be immediately available; continue to check the
                                 			 website for updates. |
|---|---|

| Note | The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer
                                 do not update the English user guides on the Cisco Unified Communications Manager. |
|---|---|

| Tip | You may want to bookmark the web pages for the phone models that are deployed in your company and send these URLs to your
                                 users. |
|---|---|