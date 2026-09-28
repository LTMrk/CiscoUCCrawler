---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8832-firmware-12-7-1sr1-cs88-b-rns-8832-1271sr1-html-14ad2a15bb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8832/firmware/12-7-1SR1/cs88_b_rns-8832-1271sr1.html
retrieved_at: 2026-08-21T13:28:35.511031+00:00
---

Cisco IP Conference Phone 8832 Release Notes for Firmware Release 12.7(1)SR1

# Cisco IP Conference Phone 8832 Release Notes for Firmware Release 12.7(1)SR1

### Download Options

Updated: July 16, 2020

First Published: July 20, 2020

# Cisco IP Conference Phone 8832 Release Notes for Firmware Release 12.7(1)SR1

These release notes support the Cisco IP Conference Phone 8832 running Firmware
                  				Release 12.7(1)SR1.

The following table lists the support compatibility for the Cisco IP Phones.

Cisco IP Phone

Support Requirements

8832

Cisco Unified Communications Manager 10.5(2) and later

Cisco Unified Communications Manager time zone update 2016d or
                              									later

SRST 8.0 (IOS load 15.1(1)T) and above

Cisco Expressway 8.7

8832

Unified CME 12.3 (Cisco IOS XE Fuji 16.9.1 release)

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone 8800 Series Documentation

Refer to
                        		  publications that are specific to your language, phone model, and call control
                        		  system. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-8800-series/index.html

The Deployment Guide is located at the following URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-implementation-design-guides-list.html

### Cisco Unified
                     				Communications Manager Documentation

See the Cisco Unified
                              				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                           				Communications Manager release. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html

## New and Changed Features

This release contains no new or changed features.

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications
                     Manager is running the latest device pack. The applicable device packs are released
                     after the firmware release. After you install a device pack on the Cisco Unified
                     Communications Manager servers in the cluster, you need to reboot all the servers.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html .

### Install the Firmware Release on Cisco Unified Communications Manager

Before using the phone firmware release on the Cisco Unified Communications Manager,
                        				you must install the latest Cisco Unified Communications Manager firmware on all
                        				Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose IP Conference Phone 8832 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.7(1)SR1 .

Select the firmware file, click the Download or Add to cart button, and follow the prompts.

The firmware filename is cmterm-8832-sip.12-7-1-0101-415.k3.cop.sgn

If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file.

Click the + next to the firmware file name in the
                                 					Download Cart section to access additional information about this file. The
                                 					hyperlink for the readme file is in the Additional Information section, which
                                 					contains installation instructions for the corresponding firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer
                        				program, the following .zip file is available to load the firmware:

cmterm-8832.12-7-1-0101-415.zip

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired
                        				connection. Upgrade times over the WLAN interface may take more than an hour,
                        				depending on the quality and bandwidth of the wireless connection.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose IP Conference Phone 8832 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.7(1)SR1 .

Download the relevant zip files.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration
                                    						Guide for information about how to manually copy the firmware files
                                 					to the server.

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

### On-Hook Transfer Limitation in SIP Phones

When the Cisco Unified Communications Manager Transfer On-Hook Enabled field is enabled, users might report a problem with direct call transfer in SIP phones. If the user transfers the call and
                        immediately goes on hook before they hear the ring signal, the call may drop instead of being transferred.

The user needs to hear the ring signal so that they can be sure that the call is being routed.

### Ringtone Limitation During Firmware Downgrade from Release 11.5(1)

When the phone downgrades from Firmware Release 11.5(1) to Firmware Release 11.0(1), the phone may not ring when there is
                        an incoming call. The ringtone for the line has been deleted and must be manually set in the Settings > Ringtone menu.

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

## Caveats

### View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open
                        				or resolved.

Before you begin

#### Before you begin

To view caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

To find all caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.7(1.*),12.7(1)&sb=anfr&svr=3nH&bt=custV

To find all open caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.7(1)&sb=afr&sts=open&svr=3nH&bt=custV

To find all resolved caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.7(1.*),12.7(1)&sb=fr&sts=fd&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional)  To look for information about a specific problem, enter the bug ID number in
                                 					the Search for field, and press Enter .

### Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco
                        				IP Conference Phone 8832 for Firmware Release 12.7(1)SR1.

For more information about an individual defect, access the Bug Search toolkit and
                        				search for the defect using the Identifier. You must be a registered Cisco.com user
                        				to access this online information.

Because defect status continually changes, the list reflects a snapshot of the
                        				defects that were open at the time this report was compiled. For an updated view of
                        				open defects, access Bug Toolkit as described in View Caveats .

CSCvq23279 No wireless sign in access port under settings when sign in access
                              						enabled.

CSCvq55980 Network name still displayed ssid when no wifi radio available

### Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the
                        				Cisco IP Conference Phone 8832 for Firmware Release 12.7(1)SR1.

For more information about an individual defect, access the Bug Search toolkit and
                        				search for the defect using the Identifier. You must be a registered Cisco.com user
                        				to access this online information.

Because defect status continually changes, the list reflects a snapshot of the
                        				defects that were open at the time this report was compiled. For an updated view of
                        				open defects, access Bug Toolkit as described in View Caveats .

CSCvs75879 Cisco 88xx Phones show lag/slowness when dialing out an
                              						extension

CSCvs91971 CVE-2016-9843: zlib crc32_big Function Numeric Errors
                              						Vulnerability

CSCvs95092 Multiple Vulnerabilities in Qt

CSCvs95116 8861/8865 is not reconnecting to Aruba AP after network outage

CSCvt31520 88xx DMAN crash

CSCvt47267 88XX intermittently crashing retrieving a call placed on hold by
                              						another device

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

| Cisco IP Phone | Support Requirements |
|---|---|
| 8832 | Cisco Unified Communications Manager 10.5(2) and later Cisco Unified Communications Manager time zone update 2016d or
                              									later SRST 8.0 (IOS load 15.1(1)T) and above Cisco Expressway 8.7 |
| 8832 | Unified CME 12.3 (Cisco IOS XE Fuji 16.9.1 release) |

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose IP Conference Phone 8832 . |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | In the Latest Releases folder, choose 12.7(1)SR1 . |
| Step 5 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. The firmware filename is cmterm-8832-sip.12-7-1-0101-415.k3.cop.sgn Note If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file. |
| Step 6 | Click the + next to the firmware file name in the
                                 					Download Cart section to access additional information about this file. The
                                 					hyperlink for the readme file is in the Additional Information section, which
                                 					contains installation instructions for the corresponding firmware. |
| Step 7 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose IP Conference Phone 8832 . |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | In the Latest Releases folder, choose 12.7(1)SR1 . |
| Step 5 | Download the relevant zip files. |
| Step 6 | Unzip the files. |
| Step 7 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration
                                    						Guide for information about how to manually copy the firmware files
                                 					to the server. |

| Step 1 | Perform one of the following actions: To find all caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.7(1.*),12.7(1)&sb=anfr&svr=3nH&bt=custV To find all open caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.7(1)&sb=afr&sts=open&svr=3nH&bt=custV To find all resolved caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.7(1.*),12.7(1)&sb=fr&sts=fd&svr=3nH&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional)  To look for information about a specific problem, enter the bug ID number in
                                 					the Search for field, and press Enter . |

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