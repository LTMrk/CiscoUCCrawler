---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7832-firmware-12-6-1-sr1-cs78-b-7832-release-notes-1261sr1-html-1dc9528291
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7832/firmware/12-6-1-sr1/cs78_b_7832-release-notes-1261sr1.html
retrieved_at: 2026-08-21T13:22:39.019567+00:00
---

Cisco IP Conference Phone 7832 Release Notes for Firmware Release 12.6(1)SR1

# Cisco IP Conference Phone 7832 Release Notes for Firmware Release 12.6(1)SR1

### Download Options

Updated: November 21, 2019

First Published: November 21, 2019

# Cisco IP Conference Phone 7832 Series Release Notes for Firmware Release 12.6(1)SR1

These release notes support the Cisco IP Conference Phone 7832 running SIP Firmware Release 12.6(1)SR1.

The following table lists the support and protocol compatibility for the Cisco IP Phones.

Cisco IP Phone

Protocol

Support Requirements

7832

SIP

Cisco Unified Communications Manager 10.5(2) and later

Cisco Unified Communications Manager DST Olsen version D or later

SRST 8.0 (IOS load 15.1(1)T) and above

Cisco Expressway 8.7

7832

SIP

Unified CME 12.3 (Cisco IOS XE Fuji 16.9.1 release)

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Conference Phone 7832 Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation
                        URL:

https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-7800-series/index.html

### Cisco Unified
                     				Communications Manager Documentation

See the Cisco Unified
                              				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                           				Communications Manager release. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html

## New and Changed Features

This release contains no new or changed features.

### Features from Release 12.6(1)

Cisco Conference IP Phone 7832 Firmware Release 12.6(1) was deprecated. It had no new features.

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications Manager is running the latest
                     device pack. After you install a device pack on the Cisco Unified Communications Manager servers in the cluster, you need
                     to reboot all the servers.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html .

### Install the Firmware Release on Cisco Unified Communication Manager

Before using the phone firmware release on the Cisco Unified Communications Manager, you must install the latest Cisco Unified
                        Communications Manager firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Choose Cisco IP Phone 7800 Series .

Choose IP Conference Phone 7832 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.6(1)SR1 .

Select the firmware file, click the Download or Add to cart button, and follow the prompts.

The firmware filename is cmterm-7832-sip.12-6-1-0101-692.k3.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following zip file is available
                        to load the firmware:

cmterm-7832.12-6-1-0101-692.zip

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                        interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco IP Phones 7800 Series .

Choose IP Conference Phone 7832 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.6(1)SR1 .

Download the relevant zip files.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server. See Administration Guide for Cisco Unified Communications Manager and IM and Presence Service for information about how to manually copy the firmware files to the server.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and, in some cases, can cause a call to drop. Sources of
                        network degradation can include, but are not limited to, the following activities:

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Health-Care
                  	 Environment Use

This product is not a
                     		medical device and uses an unlicensed frequency band that is susceptible to
                     		interference from other devices or equipment.

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

### Caveats

#### View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

##### Before you begin

To view caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

To find all caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=12.6.1%20release%207832%20audio&pf=prdNm&rls=12.6(1)&sb=anfr&bt=empCustV

To find all open caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=12.6.1%20release%207832%20audio&pf=prdNm&rls=12.6(1)&sb=anfr&sts=open&bt=empCustV

To find all resolved caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=12.6.1%20release%207832%20audio&pf=prdNm&rls=12.6(1)&sb=anfr&sts=fd&bt=empCustV

When prompted, log in with your Cisco.com user ID and password.

(Optional)  To look for information about a specific problem, enter the bug ID number in the Search for field, and press Enter .

#### Open Caveats

There are no open defects for the Cisco IP Conference Phone 7832 for Firmware Release 12.6(1)SR1.

Because defect status continually changes, the information in this section is a snapshot of the defects that were open at
                           the time this report was compiled. For an updated view of open defects, access the Bug Toolkit as described in View Caveats .

#### Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 7832 for Firmware
                           Release 12.6(1)SR1.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                           You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the information in this section is a snapshot of the defects that were resolved
                           at the time this report was compiled. For an updated view of resolved defects, access the Bug Toolkit as described in View Caveats .

CSCvq75308 8851/8861 : With CME/BE4k MWI always shows 1 message regardless of number of messages

CSCvq83109 ms crash caused by watchdog timeout

CSCvq93141 External phone number mask is not displayed as the directory number after an incoming call when more than 11 lines
                                 are configured

CSCvr06323 CUCM Server1 and CUCM Server3 null values for Active Server

CSCvr21736 Phone displays "???" when releasing a call

CSCvr21781 Unexpected audio tone played for call recording INVITE

CSCvr27035 7841 phones do not request custom directory URLs

CSCvr31360 No DTMF sent after entering Forced Authorization Code (FAC) on 7832 phones

CSCvr35161 PRT Status: uploading-failed when generating PRT via web access

CSCvr54598 Intermittently not ring after upgrade to 12.6

CSCvr56478 "Attempting VPN connection" banner on phone screen doesn't go away after VPN connection establishes

CSCvr69093 Phone stuck in registering status due to Memory leak in sipstack

##### Bugs Resolved in Firmware Release 12.6(1)

Because Firmware Release 12.6(1) was deprecated, here are the bugs resolved in that release.

CSCvq00185: In the shared line mode the screen of 7832 will quickly display "dnd is on"when hanging up

CSCvq01736: LSC Authentication string come out as a plain text on phone UI

CSCvq16455: MRA Login: 7832 phone call setup failed

## Cisco Unified Communication Manager Public Keys

To improve software integrity protection, new public keys are used to sign cop files for Cisco Unified Communications Manager
                     Release 10.0.1 and later. These cop files have "k3" in their name. To install a k3 cop file on a pre-10.0.1 Cisco Unified Communications Manager, consult the README for the
                     ciscocm.version3-keys.cop.sgn to determine if this additional cop file must first be installed on your specific Cisco Unified
                     Communications Manager version. If these keys are not present and are required, you will see the error "The selected file is not valid" when you try to install the software package.

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

To access the Locale Installer required for a release, access https://software.cisco.com/download/navigator.html?mdfid=286037605&flowid=46245 , navigate to your phone model, and select the Unified Communications Manager Endpoints Locale Installer link.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

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

You may want to bookmark the web pages for the phone models that are deployed in your company and send these URLs to your
                                 users.

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| 7832 | SIP | Cisco Unified Communications Manager 10.5(2) and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above Cisco Expressway 8.7 |
| 7832 | SIP | Unified CME 12.3 (Cisco IOS XE Fuji 16.9.1 release) |

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phone 7800 Series . |
| Step 3 | Choose IP Conference Phone 7832 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.6(1)SR1 . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. The firmware filename is cmterm-7832-sip.12-6-1-0101-692.k3.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 8 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phones 7800 Series . |
| Step 3 | Choose IP Conference Phone 7832 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.6(1)SR1 . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Administration Guide for Cisco Unified Communications Manager and IM and Presence Service for information about how to manually copy the firmware files to the server. |

| Step 1 | Perform one of the following actions: To find all caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=12.6.1%20release%207832%20audio&pf=prdNm&rls=12.6(1)&sb=anfr&bt=empCustV To find all open caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=12.6.1%20release%207832%20audio&pf=prdNm&rls=12.6(1)&sb=anfr&sts=open&bt=empCustV To find all resolved caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=12.6.1%20release%207832%20audio&pf=prdNm&rls=12.6(1)&sb=anfr&sts=fd&bt=empCustV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional)  To look for information about a specific problem, enter the bug ID number in the Search for field, and press Enter . |

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