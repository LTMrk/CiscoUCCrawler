---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7821-7841-7861-10-1-english-release-notes-pa2d-bk-c93adaa2-00-cisco-u-cf21042578
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7821_7841_7861/10_1/english/release_notes/PA2D_BK_C93ADAA2_00_cisco-unified-ip-phone-7821/PA2D_BK_C93ADAA2_00_cisco-unified-ip-phone-7821_chapter_00.html
retrieved_at: 2026-08-25T12:23:04.902705+00:00
---

Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.2(1)

# Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.2(1)

## Results

Updated: May 23, 2018

Chapter: Cisco IP Phone
	 7821, 7841, and 7861 Firmware Release 10.2(1)

## Chapter: Cisco IP Phone
	 7821, 7841, and 7861 Firmware Release 10.2(1)

# Cisco IP Phone
                     	 7821, 7841, and 7861 Firmware Release 10.2(1)

## Introduction

These release notes
                           		support the Cisco IP Phones 7811, 7821, 7841, and 7861 running SIP Firmware Release
                           		10.3(1).

The following table
                           		lists the Cisco Unified Communications Manager release and protocol
                           		compatibility for the Cisco IP Phones.

Cisco IP Phone

Protocol

Cisco Unified
                                       				Communications Manager

Cisco IP
                                       				Phones 7811, 7821, 7841, and 7861

SIP

Cisco Unified
                                       				Communications Manager version 8.5(1) and later

Cisco Unified
                                       				Communications Manager DST Olsen version D or later

## Related
                        	 Documentation

### Cisco IP Phone 7800 Series Documentation

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Phone 7800 Series.

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

#### CiscoSans 2.0
                              	 Latin Font Support

The Cisco Sans 2.0
                                 		Latin Font Support feature improves Call Display by introducing the CiscoSans
                                 		2.0 font for all Latin characters.

There is no
                                 		administrator impact with this feature.

This feature is
                                 		supported on the following SIP phones:

Cisco IP Phone
                                       			 7821

Cisco IP Phone
                                       			 7841

Cisco IP Phone
                                       			 7861

##### Where to Find
                                    		  More Information

Cisco IP Phone 7821, 7841,
                                       			 and 7861 User Guide for Cisco Unified Communications Manager 10.0 (SIP)

#### Improve Caller
                              	 Name and Number Display

The Improve Caller
                                 		Name and Number Display feature improves the display of caller names and
                                 		numbers. If the Caller Name is unknown then the Caller Number is now displayed
                                 		instead of Unknown.

This feature is
                                 		supported on the following SIP phones:

Cisco IP Phone
                                       			 7821

Cisco IP Phone
                                       			 7841

Cisco IP Phone
                                       			 7861

##### Where to Find
                                    		  More Information

Cisco IP Phone 7821, 7841,
                                       			 and 7861 User Guide for Cisco Unified Communications Manager 10.0 (SIP)

#### Line Display
                              	 Enhancement

The Line Display
                                 		Enhancement feature improves Call Display by removing the central dividing line
                                 		when it is not required.

This feature is
                                 		supported on Cisco IP Phone 7841 (SIP).

##### Where to Find
                                    		  More Information

Cisco IP Phone 7821, 7841,
                                       			 and 7861 User Guide for Cisco Unified Communications Manager 10.0 (SIP)

#### Multilevel
                              	 Precedence and Preemption Icon

The Multilevel Precedence and Preemption (MLPP) Icon feature enables the
                                 		user to make and receive urgent or critical calls in some specialized
                                 		environments such as military or government offices.

No administrator action is required.

This feature is supported on the following SIP phones:

Cisco IP Phone 7821

Cisco IP Phone 7841

Cisco IP Phone 7861

##### Where to Find More Information

Cisco IP Phone 7821, 7841, and 7861 User Guide for Cisco Unified
                                       			 Communications Manager 10.0 (SIP)

#### Pause in Speed Dial

The Pause in Speed Dial feature enables users to set up the speed dial feature to reach destinations that require a Forced
                                 Authorization Code (FAC), Client Matter Code (CMC), dialing pauses, and additional digits (such as a user extension, a meeting
                                 access code, or a voicemail password) without manual intervention. When the user presses the speed dial, the phone establishes
                                 the call to the specified DN and sends the specified FAC, CMC, and DTMF digits to the destination with dialing pauses inserted.

- Differentiates overlapping dial patterns (for example 9.xxx from 9.xxxxx)

- Differentiates overlapping FAC or CMC (for example, 8787 from 87879)

- Identifies the destination number when using variable-length dial patterns (for example 9.!)

- FAC must always precede CMC in the speed dial string.

- A speed dial label is required for speed dials containing FAC and DTMF digits.

- Only one comma is allowed between FAC and CMC digits in the string.

For any additional DTMF digits specified after the FAC and CMC, the phone dials these additional digits (with pauses) after
                                 the call is connected.

This feature is supported on the following SIP phones:

Cisco IP Phone 7821

Cisco IP Phone 7841

Cisco IP Phone 7861

##### Where to Find More Information

Cisco  IP Phone 7821, 7841, and 7861 Administration Guide for Cisco Unified Communications Manager 10.0 (SIP)

#### Show Duration for
                              	 Call History

The Show Call
                                 		Duration for Call History feature displays the time duration of placed and
                                 		received calls in the Call History details.

No administrator or
                                 		user action is required.

This feature is
                                 		supported on the following SIP phones:

Cisco IP Phone
                                       			 7821

Cisco IP Phone
                                       			 7841

Cisco IP Phone
                                       			 7861

##### Where to Find
                                    		  More Information

Cisco IP Phone 7821, 7841,
                                       			 and 7861 User Guide for Cisco Unified Communications Manager 10.0 (SIP)

### Features Available with the Latest Cisco Unified
                              				Communications Manager Device Package

The following sections describe features in the release which require the new firmware and the latest Cisco Unified
                                 				Communications Manager device package. The applicable device packages are released after the firmware release.

For information about the Cisco devices and the required Cisco Unified
                                 				Communications Manager device packages, see the following URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html

#### Extension Mobility
                              	 Size Safe and Feature Safe

The Extension
                                 		Mobility Size Safe and Feature Safe feature offers a greater choice in phone
                                 		button template. With Feature Safe, your phone can use any phone button
                                 		template that has the same number of line buttons that the phone model
                                 		supports. With Size Safe, your phone can use any phone button template that is
                                 		configured on your system.

This feature is
                                 		supported on the following SIP phones:

Cisco IP Phone
                                       			 7821

Cisco IP Phone
                                       			 7841

Cisco IP Phone
                                       			 7861

##### Where to Find
                                    		  More Information

Cisco IP Phone 7821, 7841,
                                       			 and 7861 User Guide for Cisco Unified Communications Manager 10.0 (SIP)

#### Outbound
                              	 Rollover

The Outbound Rollover feature allows users to make a call when the
                                 		number of calls for a line exceeds the maximum number of calls (MNC).

This feature is supported on the following SIP phones:

Cisco IP Phone 7821

Cisco IP Phone 7841

Cisco IP Phone 7861

##### Where to Find More Information

Cisco IP Phone 7821, 7841, and 7861 User Guide for Cisco Unified
                                       			 Communications Manager 10.0 (SIP)

#### Serviceability for
                              	 SIP Endpoints

- Remotely run debug
                                       		  commands on a phone or group of phones without logging into each device
                                       		  separately.

- Collect the phone log
                                       		  without logging into each phone separately.

- Troubleshoot phones by
                                       		  using multiple debug categories with the debugsh (debug telephony) command

- Log Profile - values:
                                       		  Preset (default), Default, Telephony

- Remote Log - values:
                                       		  Disable (default), Enable

- Log Server - IP address
                                       		  (IPv4 or IPv6 address)

- The format for IPv4 Log
                                       		  Server is: address:<port>@@base=<0-7>;pfs=<0-1> .

- The format for IPv6 Log
                                       		  Server is: address:<port>@@base=<0-7>;pfs=<0-1> .

This feature is
                                 		supported on the following SIP phones:

Cisco IP Phone
                                       			 7821

Cisco IP Phone
                                       			 7841

Cisco IP Phone
                                       			 7861

##### Where to Find
                                    		  More Information

Cisco IP Phone 7821, 7841,
                                       			 and 7861 Administration Guide for Cisco Unified Communications Manager 10.0
                                       			 (SIP)

## Installation

### Install Firmware
                           	 on Cisco Unified Communications Manager

Before using the
                                 		  Cisco Unified IP Phone Firmware Release 10.2(1) with Cisco Unified
                                 		  Communications Manager, you must install the latest firmware on all Cisco
                                 		  Unified Communications Manager servers in the cluster.

Step 1

Go to the
                                          			 following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Step 2

Depending on
                                          			 your phone model, choose Cisco
                                             				IP Phones 7800 Series .

Step 3

Choose your
                                          			 phone type.

Step 4

Choose Session Initiation Protocol (SIP) Software .

Step 5

In the Latest
                                          			 Releases folder, choose 10.2(1) .

Step 6

Select one of
                                          			 the following firmware files, click the Download or Add to
                                             				cart button, and follow the prompts:

cmterm-78xx.10-2-1-12.cop.sgn

If you added
                                                         				  the firmware file to the cart, click the Download Cart link when you are ready to download
                                                         				  the file.

Step 7

Click the + next to the firmware file name in the Download
                                          			 Cart section to access additional information about this file. The hyperlink
                                          			 for the readme file is in the Additional Information section, which contains
                                          			 installation instructions for the corresponding firmware.

Step 8

Follow the
                                          			 instructions in the readme file to install the firmware.

### Install Firmware
                           	 Zip Files

If a Cisco Unified
                                 		  Communications Manager is not available to load the installer program, the
                                 		  following zip files are available to load the firmware.

cmterm-78xx.10-2-1-12_REL.zip

Step 1

Go to the
                                          			 following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Step 2

Choose Cisco
                                             				IP Phones 7800 Series .

Step 3

Choose your
                                          			 phone type.

Step 4

Choose Session Initiation Protocol (SIP) Software .

Step 5

In the Latest
                                          			 Releases folder, choose 10.2(1) .

Step 6

Download the
                                          			 relevant zip files.

Step 7

Unzip the
                                          			 files.

Step 8

Manually copy
                                          			 the unzipped files to the directory on the TFTP server. See Cisco
                                             				Unified Communications Operating System Administration Guide for
                                          			 information about how to manually copy the firmware files to the server.

## Limitations and Restrictions

### Manufacturing Installed Certificate Signature and SHA-256 Support

The manufacturing installed certificate(MIC) signature has been updated from SHA-128 with RSA to SHA-256 with RSA. You must
                                 update and install the new SHA-2 certificates on the Cisco Unified Communications Manager for secure mode to function. You
                                 can download the new certificate from http://www.cisco.com/security/pki/certs/cmca2.cer .

Cisco Unified Communications Manager

Cisco Unified Survivable Remote Site Telephony

Cisco Secure Access Control System

Cisco Identity Services Engine

For additional information about SHA-2 use and support, see Security Guide for Cisco Unified Communications Manager ( https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html ).

### Phone Behavior
                           	 During Times of Network Congestion

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

## View
                        	 Caveats

You can search for
                              		  caveats using the Cisco Bug Search.

Known caveats
                              		  (bugs) are graded according to severity level, and can be either open or
                              		  resolved.

### Before you begin

To view caveats,
                              		  you need the following items:

Internet
                                    				connection

Web browser

Cisco.com user
                                    				ID and password

Step 1

Perform one of the following actions:

To find all caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=10.2(1)&sb=anfr&srtBy=byRel&bt=CustV

To find all open caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=10.2(1)&sb=afr&srtBy=byRel&bt=custV

To find all resolved caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=10.2(1)&sb=fr&srtBy=byRel&bt=custV

Step 2

When prompted,
                                       			 log in with your Cisco.com user ID and password.

Step 3

To look for
                                       			 information about a specific problem, enter the bug ID number in the Search for
                                       			 field, then press Enter .

### Resolved
                           	 Caveats

The following table lists severity 1, 2, and 3 defects that are
                                 		  resolved for the Cisco IP Phones for Firmware Release 10.2(1) at the time that this document was originally published.

To view individual bugs or to view the updated list, follow the instructions in View Caveats .

Identifier

Headline

CSCuj16464

Monitoring phone not send RTCP

CSCun37850

phone will dial out to the speed dial number after press CFA

CSCun45165

Call is dropped unexpectedly after pressing resume softkey

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

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/c/en/us/td/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application.
                           The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco IP Phone | Protocol | Cisco Unified
                                       				Communications Manager |
|---|---|---|
| Cisco IP
                                       				Phones 7811, 7821, 7841, and 7861 | SIP | Cisco Unified
                                       				Communications Manager version 8.5(1) and later Cisco Unified
                                       				Communications Manager DST Olsen version D or later |

| Step 1 | Go to the
                                          			 following URL: http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Depending on
                                          			 your phone model, choose Cisco
                                             				IP Phones 7800 Series . |
| Step 3 | Choose your
                                          			 phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
                                          			 Releases folder, choose 10.2(1) . |
| Step 6 | Select one of
                                          			 the following firmware files, click the Download or Add to
                                             				cart button, and follow the prompts: cmterm-78xx.10-2-1-12.cop.sgn Note If you added
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
                                          			 following URL: http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco
                                             				IP Phones 7800 Series . |
| Step 3 | Choose your
                                          			 phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
                                          			 Releases folder, choose 10.2(1) . |
| Step 6 | Download the
                                          			 relevant zip files. |
| Step 7 | Unzip the
                                          			 files. |
| Step 8 | Manually copy
                                          			 the unzipped files to the directory on the TFTP server. See Cisco
                                             				Unified Communications Operating System Administration Guide for
                                          			 information about how to manually copy the firmware files to the server. |

| Step 1 | Perform one of the following actions: To find all caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=10.2(1)&sb=anfr&srtBy=byRel&bt=CustV To find all open caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=10.2(1)&sb=afr&srtBy=byRel&bt=custV To find all resolved caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=10.2(1)&sb=fr&srtBy=byRel&bt=custV |
|---|---|
| Step 2 | When prompted,
                                       			 log in with your Cisco.com user ID and password. |
| Step 3 | To look for
                                       			 information about a specific problem, enter the bug ID number in the Search for
                                       			 field, then press Enter . |

| Identifier | Headline |
|---|---|
| CSCuj16464 | Monitoring phone not send RTCP |
| CSCun37850 | phone will dial out to the speed dial number after press CFA |
| CSCun45165 | Call is dropped unexpectedly after pressing resume softkey |

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