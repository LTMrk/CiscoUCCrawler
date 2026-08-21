---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-firmware-12-1-1-releasenotes-pa2d-b-7800-release-notes-fo-c5ba8281f1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/firmware/12-1-1/releasenotes/pa2d_b_7800-release-notes-for-firmware.html
retrieved_at: 2026-08-21T13:24:20.343657+00:00
---

Cisco IP Phone 7800 Series Release Notes for Firmware Release 12.1(1)

# Cisco IP Phone 7800 Series Release Notes for Firmware Release 12.1(1)

### Download Options

Updated: August 20, 2018

First Published: March 26, 2018

Last Updated: August 20, 2018

# Cisco IP Phone 7800 Series Release Notes for Firmware Release 12.1(1)

These release notes support the Cisco IP Phones 7811, 7821, 7841, and 7861 running SIP Firmware Release 12.1(1).

The following table lists the Cisco Unified Communications Manager release and protocol compatibility for the Cisco IP Phones.

Cisco IP Phone

Protocol

Cisco Unified Communications Manager

Cisco IP Phones 7811, 7821, 7841, and 7861

SIP

Cisco Unified Communications Manager version 8.5(1) and later

Cisco Unified Communications Manager DST Olsen version D or later

SRST 8.0 (IOS load 15.1(1)T) and above

Cisco IP Phones 7811, 7821, 7841, and 7861

SIP

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

## New and Changed
               	 Features

The following sections describe the features that are new or have
                  		changed in this release.

### Features Available
                  	 with the Firmware Release

The following sections describe the features available with the Firmware
                     		Release.

#### Cisco Headset 531 and Cisco Headset 532

The Cisco Headset 531 and Cisco Headset 532 are two standard headsets developed for Cisco IP Phones and devices. The 531 features a single earpiece, and offers lightweight
                           comfort. The 532 features two earpieces for use in a noisy environment or busy office.

Both headsets plug into your headset port with a RJ connector.

##### Where to Find More Information

Cisco IP Phone 7800 and 8800 Series Accessories Guide for Cisco Unified Communications Manager

Cisco IP Phone 7800 Series User Guide for Cisco Unified Communications Manager

#### G722.2 AMR-WB Support

Cisco IP Phone 7800 Series now supports the G722.2 Adaptive Multirate Wideband (AMR-WB) audio codec. This codec offers improved
                           audio, a lower bit-rate compression, and enhanced network performance during your times of peak traffic.

##### Where to Find More Information

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

### Features Available
                  	 with the Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require
                     		the new firmware and the latest Cisco Unified Communications Manager Device
                     		Pack.

For information about the Cisco Unified IP Phones and the required Cisco
                     		Unified Communications Manager device packs, see the following URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html

#### Transport Layer Security Enhancements

Administrators now have improved security over phones that act as a HTTPs server. With the parameter Disable TLS1.0 and TLS1.1
                           for web access, you can apply TLS1.0, TLS1.1, and TLS 1.2 mode, or just TLS 1.2 mode to any phone, or group of phones that
                           function as a HTTPs server.

For other configurations, TLS protocols are configured on the Cisco Unified Communications Manager. As of Cisco Unified Communications
                           Manager 12.0, there are also TLS settings configured by a CLI command. See Release Notes for Cisco Unified Communications Manager and IM & Presence Service, Release 12.0(1) for information about new CLI commands on Cisco Unified Communications Manager.

Disable TLS1.0 and TLS1.1 for web access is configured from the Product Specific Configuration Layout pane of your Cisco Unified
                           Communications Manager. Install the latest device package for this feature to function.

Disable TLS1.0 and TLS1.1 is supported on Cisco Unified Communications Manager 11.5(1)SU3 and later.

##### Where to Find More Information

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications Manager is running the latest
                     device pack. After you install a device pack on the Cisco Unified Communications Manager servers in the cluster, you need
                     to reboot all the servers.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html .

### Install the Firmware Release on Cisco Unified Communications Manager

Before using the Cisco Unified IP Phone Firmware Release 12.1(1) with Cisco Unified Communications Manager, you must install
                        the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Choose Cisco IP Phones 7800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.1(1) .

Select the following firmware file, click the Download or Add to cart button, and follow the prompts:

- cmterm-78xx.12-1-1-12.k3.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following zip files are available
                        to load the firmware.

- cmterm-78xx.12-1-1-12.zip

Go to the following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Choose Cisco IP Phones 7800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.1(1) .

Download the relevant zip files.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server.

## Limitations and Restrictions

### Manufacturing Installed Certificate Signature and SHA-256 Support

The manufacturing installed certificate(MIC) signature has been updated from SHA-128 with RSA to SHA-256 with RSA. You must
                        update and install the new SHA-2 certificates on the Cisco Unified Communications Manager for secure mode to function. You
                        can download the new certificate from http://www.cisco.com/security/pki/certs/cmca2.cer .

Cisco Unified Communications Manager

Cisco Unified Survivable Remote Site Telephony

Cisco Secure Access Control System

Cisco Identity Services Engine

For additional information about SHA-2 use and support, see Security Guide for Cisco Unified Communications Manager .

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call
                        to drop. Sources of network degradation can include, but are not limited to, the following activities:

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

### Ringtone Limitation During Firmware Downgrade from Release 11.0

When the phone downgrades from Firmware Release 11.0 to Firmware Release 10.3, the phone may not ring when there is an incoming
                        call. The ringtone for the line has been deleted and must be manually set in the Settings > Ringtone menu.

### Connections with the PC and SW Ports

If you only have one LAN cable at your desk, you can plug your phone into the LAN with the SW port and then connect your computer
                        into the PC port.

You can also daisy chain two phones together.  Connect the PC port of the first phone to the SW port of the second phone.

Do not connect the SW and PC ports into the LAN.

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

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

#### Before you begin

To view caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.1(1),12.1(1.*)&sb=anfr&svr=3nH&bt=custV

Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.1(1)&sb=afr&sts=open&svr=3nH&bt=custV

Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.1(1),12.1(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

The following table lists severity 1, 2, and 3 defects that are open for the Cisco IP Phone 7800 Series for Firmware Release
                        12.1(1).

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

Identifier

Description

CSCvh50751

Sometimes phone will play "pop" "pop" noise after do factory reset/power cycle to the phone

CSCvh58919

Phone placed or received calls will delay during the DNS query at the first time on SRST

CSCvi26356

7811 when Blind transferring to a busy destination

### Resolved Caveats

The following table lists severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series for Firmware Release
                        12.1(1).

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

Identifier

Description

CSCve70173:

Phone cannot end call by speaker button after phone login EMCC to make a call and then logout

CSCvf99694

The "Settings" and "Favorites" softkey can display but not work in 7811 with CUCM_12.0

CSCvg92940

78XX: sdump stops logging after a while

CSCvh27731

Memory leak when inter operate with UCCX

CSCvf70819

IP phone decline when NoVoicemail is configured results in Service Not Available message

CSCvf84416

78xx Java out of memory causes phones to reset

CSCvg65640

7821 phone displays a blank page after logging in to EM

CSCvg69127

78XX IP phone logs are not archived

CSCvg77031

78xx stuck on Cisco logo after upgrade from 10.3.1 to 12.0.1

CSCvg81235

Pressed digits disappear when getting an incoming call until another digit is pressed

CSCvg91780

CP-7800 one way audio by RTP sequence number reset

CSCvg97127

Phone sends DHCP Discover frame in bound state after DHCP failure

CSCvh53666

CP7841 using french canadian locale have issues with line when calls arrive w/"Formation" Caller-ID

CSCvh66567

7821 user may miss hearing the first word

CSCvh78167

78xx: "Logged in" message is shown for a split second

CSCvh78564

78xx recording does not work when button assigned with service URL is pressed directly

CSCvh78823

Phone stays in the input digit screen until it receives “180 Ringing” response

CSCvg91780

CP-7800 one way audio by RTP sequence number reset

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

To access Cisco Bug Search, go to:

https://tools.cisco.com/bugsearch

Log in with your
                                 			 Cisco.com user ID and password.

To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter .

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

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/c/en/us/td/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application.
                  The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco IP Phone | Protocol | Cisco Unified Communications Manager |
|---|---|---|
| Cisco IP Phones 7811, 7821, 7841, and 7861 | SIP | Cisco Unified Communications Manager version 8.5(1) and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above |
| Cisco IP Phones 7811, 7821, 7841, and 7861 | SIP | CME 10.0 (IOS load 15.3(3)M) |
| Cisco IP Phones 7811, 7821, 7841, and 7861 |  | Cisco Expressway X8.7 or Cisco TelePresence Video Communication Server X8.7 (for Mobile and Remote Access) |

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phones 7800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.1(1) . |
| Step 6 | Select the following firmware file, click the Download or Add to cart button, and follow the prompts: cmterm-78xx.12-1-1-12.k3.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 8 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phones 7800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.1(1) . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

| Caution | Do not connect the SW and PC ports into the LAN. |
|---|---|

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.1(1),12.1(1.*)&sb=anfr&svr=3nH&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.1(1)&sb=afr&sts=open&svr=3nH&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.1(1),12.1(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |

| Identifier | Description |
|---|---|
| CSCvh50751 | Sometimes phone will play "pop" "pop" noise after do factory reset/power cycle to the phone |
| CSCvh58919 | Phone placed or received calls will delay during the DNS query at the first time on SRST |
| CSCvi26356 | 7811 when Blind transferring to a busy destination |

| Identifier | Description |
|---|---|
| CSCve70173: | Phone cannot end call by speaker button after phone login EMCC to make a call and then logout |
| CSCvf99694 | The "Settings" and "Favorites" softkey can display but not work in 7811 with CUCM_12.0 |
| CSCvg92940 | 78XX: sdump stops logging after a while |
| CSCvh27731 | Memory leak when inter operate with UCCX |
| CSCvf70819 | IP phone decline when NoVoicemail is configured results in Service Not Available message |
| CSCvf84416 | 78xx Java out of memory causes phones to reset |
| CSCvg65640 | 7821 phone displays a blank page after logging in to EM |
| CSCvg69127 | 78XX IP phone logs are not archived |
| CSCvg77031 | 78xx stuck on Cisco logo after upgrade from 10.3.1 to 12.0.1 |
| CSCvg81235 | Pressed digits disappear when getting an incoming call until another digit is pressed |
| CSCvg91780 | CP-7800 one way audio by RTP sequence number reset |
| CSCvg97127 | Phone sends DHCP Discover frame in bound state after DHCP failure |
| CSCvh53666 | CP7841 using french canadian locale have issues with line when calls arrive w/"Formation" Caller-ID |
| CSCvh66567 | 7821 user may miss hearing the first word |
| CSCvh78167 | 78xx: "Logged in" message is shown for a split second |
| CSCvh78564 | 78xx recording does not work when button assigned with service URL is pressed directly |
| CSCvh78823 | Phone stays in the input digit screen until it receives “180 Ringing” response |
| CSCvg91780 | CP-7800 one way audio by RTP sequence number reset |

| Step 1 | To access Cisco Bug Search, go to: https://tools.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                                 			 Cisco.com user ID and password. |
| Step 3 | To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter . |

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