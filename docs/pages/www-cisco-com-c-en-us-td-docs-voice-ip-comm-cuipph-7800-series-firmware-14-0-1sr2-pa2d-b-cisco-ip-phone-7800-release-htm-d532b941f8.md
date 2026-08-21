---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-firmware-14-0-1sr2-pa2d-b-cisco-ip-phone-7800-release-htm-d532b941f8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/firmware/14_0_1SR2/pa2d_b_cisco-ip-phone-7800-release.html
retrieved_at: 2026-08-21T13:23:42.307332+00:00
---

Cisco IP Phone 7800 Release Notes for Firmware Release 14.0(1)SR2

# Cisco IP Phone 7800 Release Notes for Firmware Release 14.0(1)SR2

First Published: July 29, 2021

# Cisco IP Phone 7800 Release Notes for Firmware Release 14.0(1)SR2

These release notes support the Cisco IP Phones 7811, 7821, 7841, and 7861 running SIP Firmware Release 14.0(1)SR2.

The following table lists the support compatibility for the Cisco IP Phones.

Cisco IP Phone

Cisco Unified Communications Manager

Cisco IP Phones 7811, 7821, 7841, and 7861

Cisco Unified Communications Manager version 10.0 and later

Cisco Unified Communications Manager DST Olsen version D or later

SRST 8.0 (IOS load 15.1(1)T) and above

Cisco IP Phones 7811, 7821, 7841, and 7861

CME 10.0 (IOS load 15.3(3)M)

Cisco IP Phones 7811, 7821, 7841, and 7861

Cisco Expressway X8.7 or Cisco TelePresence Video Communication Server X8.7 (for Mobile and Remote Access)

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone 7800 Series Documentation

Refer to publications that are specific to your language, phone model, and call control system. Navigate from the following
                        documentation URL:

https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-7800-series/index.html

### Cisco Unified
                     				Communications Manager Documentation

See the Cisco Unified
                              				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                           				Communications Manager release. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html

## New Hardware

### New Cisco IP Phone 7841 Harware

The Cisco IP Phones 7841 hardware has been updated. The new hardware version is V18.

Phones manufactured with the new hardware updates must run Firmware Release 14.0(1)SR2 or later. The phone firmware does not
                        allow the phone to be downgraded to releases earlier than Firmware Release 14.0(1)SR2.

Cisco 7811/7821/7861 IP Phones hardware has not been updated.

This feature has no user impact.

## New and Changed Features

This release contains no new or changed features.

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified
                        				Communications Manager is running the latest device package. After you install a device package on the Cisco Unified
                        				Communications Manager servers in the cluster, you need to reboot all the servers.

If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly.

For information on the Cisco Unified
                        				Communications Manager Device Packages, see https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix.html .

### Install the Firmware Release on Cisco Unified Communications Manager

You must install the latest Cisco Unified Communications Manager firmware on all Cisco Unified Communications Manager servers
                        in the cluster.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Choose Cisco IP Phone 7800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 14.0(1)SR2 .

Select the firmware file, click the Download or Add to Cart button, and follow the prompts.

The firmware filename is cmterm-78xx.14-0-1-0201-169.k3.cop.sha512

If you added the firmware file to the cart, click the Download All link when you are ready to download the file.

Click the + next to the firmware file name in the File Information section to access additional information about this file. The hyperlink
                                 for the Readme file is in the Details section, which contains installation instructions for the corresponding firmware.

Follow the instructions in the Readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following zip file is available
                        to load the firmware: cmterm-78xx.14-0-1-0201-169.zip

Go to the following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Choose Cisco IP Phones 7800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 14.0(1)SR2 .

Download the relevant zip files.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and video quality, and in some cases, can cause a call to
                        drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Health-Care
                  	 Environment Use

This product is not a
                     		medical device and uses an unlicensed frequency band that is susceptible to
                     		interference from other devices or equipment.

### On-Hook Transfer Limitation in SIP Phones

When the Cisco Unified Communications Manager Transfer On-Hook Enabled field is enabled, users might report a problem with direct call transfer in SIP phones. If the user transfers the call and
                        immediately goes on hook before they hear the ring signal, the call may drop instead of being transferred.

The user needs to hear the ring signal so that they can be sure that the call is being routed.

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

### Softkey Templates and Video Mode

You can't configure softkey
                        				templates for Video mode on the Cisco IP Phone 7800 Series phones. If a softkey
                        				appears on the phone, then it will not function correctly.

## Caveats

### View Caveats

You can search for caveats using the Cisco Bug Search Tool.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

#### Before you begin

To view caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284883944&rls=14.0(1.),14.0(1)&sb=anfr&svr=3nH&bt=custV

Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284883944&rls=14.0(1)&sb=afr&sts=open&svr=3nH&bt=custV

Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284883944&rls=14.0(1.*),14.0(1)&sb=fr&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Resolved Caveats

The following list contains severity 1, 2, and 3 caveats that are resolved for the Cisco IP Phone 7800 Series for Firmware
                        Release 14.0(1)SR2.

For more information about an individual caveat, access the Bug Search Tool and search for the caveat using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because bug status continually changes, the list reflects a snapshot of the caveats that were open at the time this report
                        was compiled. For an updated view of resolved caveats, access the Bug Tool as described in View Caveats .

CSCvx84334 Evaluation of 88x1/78x1/8832/7832 phone for OpenSSL March 2021 vulnerabilities

CSCvx85820 Evaluation of 88x1/78x1/7832/8832 for debugsh read file escape

CSCvy27416 Voicemail button does not go to VM pilot with delayed PLAR enabled

CSCvy15256 7841 Built-in bridge audio level output is lower than original call

CSCvy15834 Disturbed sound after 30minutes on MRA IP phones for video callback from Webex

CSCvy16927 8845/65 Phones Over MRA won't refresh Token after power cycle

CSCvw30093 Cisco IP Phone 8800 Series, CDP packets ignored if switch hostname starts with SEPCS

Cvw45287 8851 phone over MRA phone stuck after loosing connectivity

CSCvy11282 88xx Download daemon may hang after configuration file download

CSCvy67835 Evaluation of 7800 for boot script replacement vulnerability

### Open Caveats

The following list contains a snapshot of severity 1, 2, and 3 caveats that are open for the Cisco IP Phone 7800 Series for
                        Firmware Release 14.0(1)SR2.

For more information about an individual bug, access the Bug Search Tool and search for the caveat using the Identifier. You
                        must be a registered Cisco.com user to access this online information.

Because caveat status continually changes, the list reflects a snapshot of the caveats that were open at the time this report
                        was compiled. For an updated view of open caveats, access the Bug Search Tool as described in View Caveats .

CSCvs26183 78xx phone aux port upgrade 56x without headset need 22mins

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

| Cisco IP Phone | Cisco Unified Communications Manager |
|---|---|
| Cisco IP Phones 7811, 7821, 7841, and 7861 | Cisco Unified Communications Manager version 10.0 and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above |
| Cisco IP Phones 7811, 7821, 7841, and 7861 | CME 10.0 (IOS load 15.3(3)M) |
| Cisco IP Phones 7811, 7821, 7841, and 7861 | Cisco Expressway X8.7 or Cisco TelePresence Video Communication Server X8.7 (for Mobile and Remote Access) |

| Note | If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phone 7800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 14.0(1)SR2 . |
| Step 6 | Select the firmware file, click the Download or Add to Cart button, and follow the prompts. The firmware filename is cmterm-78xx.14-0-1-0201-169.k3.cop.sha512 Note If you added the firmware file to the cart, click the Download All link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download All link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download All link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware file name in the File Information section to access additional information about this file. The hyperlink
                                 for the Readme file is in the Details section, which contains installation instructions for the corresponding firmware. |
| Step 8 | Follow the instructions in the Readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download All link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phones 7800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 14.0(1)SR2 . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284883944&rls=14.0(1.),14.0(1)&sb=anfr&svr=3nH&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284883944&rls=14.0(1)&sb=afr&sts=open&svr=3nH&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284883944&rls=14.0(1.*),14.0(1)&sb=fr&svr=3nH&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |

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