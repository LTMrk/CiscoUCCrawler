---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-firmware-12-7-1sr1-p881-b-rns-8800-1271sr1-html-b95d6ca2d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/firmware/12-7-1SR1/p881_b_rns-8800-1271sr1.html
retrieved_at: 2026-08-21T13:29:55.134926+00:00
---

Cisco IP Phone 8800 Series Release Notes for Firmware Release 12.7(1)SR1

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 12.7(1)SR1

### Download Options

Updated: July 21, 2020

First Published: July 20, 2020

Last Updated: February 10, 2021

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 12.7(1)SR1

These release notes support the Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861,
                  				8865, and 8865NR running SIP Firmware Release 12.7(1)SR1.

The following table lists the support compatibility for the Cisco IP Phones.

Cisco IP Phone

Support Requirements

8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR

Cisco Unified Communications Manager 8.5(1) and later

Cisco Unified Communications Manager DST Olsen version D or later

SRST 8.0 (IOS load 15.1(1)T) and above

Cisco Expressway 8.7

8811, 8841, 8851, 8851NR, and 8861

CME 10.0 (IOS load 15.3(3)M)

For information about phone hardware versions and the minimum firmware versions, see https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/english/compatibility/p881_b_phone-8800-series-compatibility.html .

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

Before you install the firmware release, you must ensure that your Cisco Unified
                        				Communications Manager ( Unified CM ) is running the latest device pack. After you install a device pack on the Unified CM servers in the cluster, you need to reboot all the servers.

If your Unified CM doesn't have the required device pack to support this firmware release, the firmware may not work correctly.

For information on the Unified CM Device Packs, see https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix.html .

### Install the Firmware Release on Cisco Unified Communications Manager

Before using the phone firmware release on the Cisco Unified Communications Manager,
                        				you must install the latest Cisco Unified Communications Manager firmware on all
                        				Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco IP Phone 8800 Series .

Choose your phone type.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.7(1)SR1 .

Select the firmware file, click the Download or Add to cart button, and follow the prompts:

For Cisco IP Phone 8811, 8841, 8851, 8851NR, and
                                          								8861—cmterm-8xx-sip.12-7-1-0101-415.k3.cop.sgn

For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65.12-7-1-0101-415.k3.cop.sgn

If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file.

Click the + next to the firmware file name in the
                                 					Download Cart section to access additional information about this file. The
                                 					hyperlink for the readme file is in the Additional Information section, which
                                 					contains installation instructions for the corresponding firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer
                        				program, the following .zip files are available to load the firmware:

For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx.12-7-1-0101-415.zip

For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65.12-7-1-0101-415.zip

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired
                        				connection. Upgrade times over the WLAN interface may take more than an hour,
                        				depending on the quality and bandwidth of the wireless connection.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco IP Phones 8800 Series .

Choose your phone model.

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

### Ringtone Limitation During Firmware Downgrade from Release 11.5(1)

When the phone downgrades from Firmware Release 11.5(1) to Firmware Release 11.0(1), the phone may not ring when there is
                        an incoming call. The ringtone for the line has been deleted and must be manually set in the Settings > Ringtone menu.

### Language Limitation

There is no localized Keyboard
                        Alphanumeric Text Entry (KATE) support for the following Asian
                        locales:

Chinese (Hong Kong)

Chinese (Taiwan)

Japanese (Japan)

Korean (Korea Republic)

The default English (United States) KATE is presented to the user instead.

For example, the phone screen will show text in Korean, but the 2 key on the keypad will display a b c 2 A B C .

Chinese input works similar to PCs and mobile phones in Chinese. The Chinese locale installer is required for Chinese input
                        to function.

### Softkey Templates and Video Mode

You can't configure softkey
                        				templates for Video mode on the Cisco IP Phone 8800 Series phones. If a softkey
                        				appears on the phone, then it will not function correctly.

## Caveats

### View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open
                        				or resolved.

Perform one of the following actions:

Use this URL for all caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.7(1.*),12.7(1)&sb=anfr&svr=3nH&bt=custV

Use this URL for all open caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.7(1)&sb=afr&sts=open&svr=3nH&bt=custV

Use this URL for all resolved caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.7(1.*),12.7(1)&sb=fr&sts=fd&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the
                        				Cisco IP Phone 8800 Series that uses Firmware Release 12.7(1)SR1.

For more information about an individual defect, you can access the online record
                        				for the defect from the Bug Search Toolkit. You must be a registered Cisco.com user
                        				to access this online information.

Because defect status continually changes, the list reflects a snapshot of the
                        				defects that were resolved at the time this report was compiled. For an updated view
                        				of resolved defects or to view specific bugs, access the Bug Search Toolkit as
                        				described in View Caveats .

CSCvn86806 remove the usb2 cable from mac will cause IP phone popup remove
                              						toast

CSCvo71625 Sometimes the phone screen doesn't display the last digit of the
                              						phone number

CSCvo74172 8861 phone should not roaming from WLC with Platinum QOS to WLC
                              						with Silver QOS

CSCvp34626 No wifi icon displayed at the upper right corner of LCD after wifi
                              						connection done

CSCvp34626 No wifi icon displayed at the upper right corner of LCD after wifi
                              						connection done

CSCvq21512 8861 deregister when running JFW roaming about 3 hours(EAP-TLS
                              						with WPA2+ 11r over the DS)

CSCvq32455 8845_65 ip phone reset/restart intermittently after disconnect of
                              						a call

CSCvq37245 Active server shows empty under phone information page in ipv6
                              						only mode

CSCvq59064 802.11r fast transition sometimes failed to work on 8861

CSCvq89463 8845/8865 freezing randomly

CSCvt04909 The spam list can not be cleared after EM logout

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for
                        				the Cisco IP Phone 8800 Series that uses Firmware Release 12.7(1)SR1.

For more information about an individual defect, you can access the online record
                        				for the defect from the Bug Search Toolkit. You must be a registered Cisco.com user
                        				to access this online information.

Because defect status continually changes, the list reflects a snapshot of the
                        				defects that were resolved at the time this report was compiled. For an updated view
                        				of resolved defects or to view specific bugs, access the Bug Search Toolkit as
                        				described in View Caveats .

CSCvr19868 DTMF RFC 2833 differences between Cisco IP phone 8851 PID VID over
                              						V08 with below V08

CSCvs73770 Different beeping behavior on receiving a call with APU-76 headset
                              						and shared line

CSCvs75879 Cisco 88xx Phones show lag/slowness when dialing out an
                              						extension

CSCvs87895 Evaluation of 8851/61/45/65 for Kr00k attack - CVE-2019-15126

CSCvs91971 CVE-2016-9843: zlib crc32_big Function Numeric Errors
                              						Vulnerability

CSCvs95092 Multiple Vulnerabilities in Qt

CSCvs95116 8861/8865 is not reconnecting to Aruba AP after network outage

CSCvs98676 88xx phones are not displaying the speed-dials when pressing the
                              						navigation down key

CSCvt04894 Disable 'Lower Your Voice Alert' feature by default in CP-88xx

CSCvt11376 8861 HW Rev V15 and above unable to connect to VPN

CSCvt14542 88xx: CLIB is not displayed in enhanced line mode in firmware
                              						version 12.7

CSCvt14542 88xx: CLIB is not displayed in enhanced line mode in firmware
                              						version 12.7

CSCvt16645 Disable 'Spam Call' feature in CP-88xx

CSCvt31520 88xx DMAN crash

CSCvt37331 8865/8845 Black screen in the beginning of video call

CSCvt45473 8861 HW Rev V15 and above unable to do Jabber deskphone video

CSCvt47267 88XX intermittently crashing retrieving a call placed on hold by
                              						another device

CSCvt55471 8865 unable to register when use a custom background

CSCvt64703 8861 FW 12.7.1 Wireless (Wi-Fi) Phone VPN Not Registering

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
| 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR | Cisco Unified Communications Manager 8.5(1) and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above Cisco Expressway 8.7 |
| 8811, 8841, 8851, 8851NR, and 8861 | CME 10.0 (IOS load 15.3(3)M) |

| Note | If your Unified CM doesn't have the required device pack to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phone 8800 Series . |
| Step 3 | Choose your phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.7(1)SR1 . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts: For Cisco IP Phone 8811, 8841, 8851, 8851NR, and
                                          								8861—cmterm-8xx-sip.12-7-1-0101-415.k3.cop.sgn For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65.12-7-1-0101-415.k3.cop.sgn Note If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware file name in the
                                 					Download Cart section to access additional information about this file. The
                                 					hyperlink for the readme file is in the Additional Information section, which
                                 					contains installation instructions for the corresponding firmware. |
| Step 8 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phones 8800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.7(1)SR1 . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration
                                    						Guide for information about how to manually copy the firmware files
                                 					to the server. |

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.7(1.*),12.7(1)&sb=anfr&svr=3nH&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.7(1)&sb=afr&sts=open&svr=3nH&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.7(1.*),12.7(1)&sb=fr&sts=fd&svr=3nH&bt=custV |
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