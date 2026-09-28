---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-firmware-12-5-1sr2-releasenotes-pa2d-b-release-notes-1251-124b651913
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/firmware/12-5-1SR2/releasenotes/pa2d_b_release-notes-1251sr2-7800.html
retrieved_at: 2026-08-21T13:24:07.422788+00:00
---

Cisco IP Phone 7800 Series Release Notes for Firmware Release 12.5(1)SR2

# Cisco IP Phone 7800 Series Release Notes for Firmware Release 12.5(1)SR2

### Download Options

Updated: March 22, 2019

First Published: March 25, 2019

Last Updated: February 10, 2021

# Cisco IP Phone 7800 Series Release Notes for Firmware Release 12.5(1)SR2

These release notes support the Cisco IP Phones 7811, 7821, 7841, and 7861 running SIP Firmware Release 12.5(1)SR2.

Firmware Release 12.5(1)SR2 replaces Firmware Release 12.5(1) and Firmware 12.5(1)SR1. Firmware Release 12.5(1) and Firmware
                              Release 12.5(1)SR1 have been deferred in favor of Firmware Release 12.5(1)SR2.

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

## New and Changed Features Introduced in Firmware Release 12.5(1) and Firmware Release 12.5(1)SR1

In Firmware Release 12.5(1) and Firmware Release 12.5(1)SR1, we introduced the features in the following sections. No new
                     features were introduced in Firmware Release 12.5(1)SR2.

### Features Available
                  	 with the Firmware Release

The following sections describe the features available with the Firmware
                     		Release.

#### Cisco Headset Support

The Cisco IP Phone 7800 Series now supports Cisco Headset 561 and 562.

Cisco Headset 561 has a single earpiece that makes it lightweight. Cisco Headset 562 has a dual earpiece for use in a noisy
                           workplace. Both headsets are compatible with the standard base and the multibase.

Administrators can remotely configure the Cisco Headset 500 Series settings. Download the defaultheadsetconfig.json sample
                           file from the Cisco Headset 500 Series section of the Cisco Software Download website. The URL is http://software.cisco.com/download/navigator.html?mdfid=286320550 . The sample file is with headset Firmware Release 1.0(2).

Remote configuration is only available for on-premises phones and supports Cisco Unified Communications Manager Software Releases
                           10.5(2), 11.0(1), 11.5(1), 12.0(1), and 12.5(1).

Remote configuration is supported on the following Cisco headsets:

Cisco Headset 531 and 532

Cisco Headset 561 and 562

##### Where to Find More Information

Cisco Headset 500 Series User Guide

Cisco Headset 500 Series Administration Guide

#### Whisper Paging and Cisco Unified Communications Manager Express

Your users have an improved call experience with whisper paging. In previous releases, your calls were interrupted by a page.
                           But now your phone rejects any pages when you are on a call, and ensures a distraction-free experience.

This feature is supported on Cisco Unified Communications Manager Express.

##### Where to Find More Information

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

#### Elliptic Curve Support

Your Cisco IP Phone has been made even more secure with support for Elliptic Curve Digital Signature Algorithm (ECDSA) certificates.
                           These certificates are stronger than the RSA-based certificates and require a smaller key size, making them a quicker solution
                           for your network security.

The ECDSA certificates are available in the following areas—Certificate Manager, SIP, Certificate Authority Proxy Function
                           (CAPF), Transport Layer Security (TLS) Tracing, Entropy, HTTP, and computer telephony integration (CTI) Manager.

Elliptic Curve Digital Signature Algorithm (ECDSA) certificates require Cisco Unified Communications Manager 12.5(1) or later.

##### Where to Find More Information

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

Security Guide for Cisco Unified Communications Manager, Release 12.0(1)

#### Interactive Connectivity Establishment and Media Paths

Mobile Remote Access (MRA) now supports Interactive Connectivity Establishment (ICE). ICE is an optional deployment that improves
                           the reliability of MRA calls across a firewall or Network Address Translation (NAT). It uses Serial Tunneling and Traversal
                           Using Relays around NAT services to select the best media path for a call.

ICE is configured in these ways:

System defaults—You apply ICE settings across a network with the Enterprise Phone Configuration window.

ICE Profiles—You apply ICE settings to a phone group with the Common Phone Profile Configuration .

Secondary Turn Server and Turn Server Failover is not supported.

You can find additional information in the Internet Engineering Task Force (IETF) Request for Comment documents:

Traversal Using Relays around NAT (TURN): Relay Extensions to Session Traversal Utilities for NAT (STUN) (RFC 5766)

Interactive Connectivity Establishment (ICE): A Protocol for Network Address Translator (NAT) Traversal for Offer/Answer Protocols (RFC 5245)

Interactive Connectivity Establishment requires Cisco Unified Communications Manager 12.5(1) or later to function properly.
                           Interactive Connectivity Establishment is also supported on Cisco Expressway X12.5 or later.

##### Where to Find More Information

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

#### Activation Code Onboarding

Cisco Unified Communications Bulk Administration Tool (BAT)

Cisco Unified Communications Manager Administration interface

Administrative XML Web Service (AXL)

Administrators find this approach improves control because phones cannot register until the activation code is entered and
                           the Manufacturing Installed Certificate (MIC) is verified. It is also a convenient way to bulk onboard phones because it doesn't
                           use the Tool for Auto-registered Phone Support (TAPS) or autoregistration.

Activation Code Onboarding is an easy way for users to configure their phones because they only enter a 16-digit activation
                           code. Codes are entered either manually or with a QR code if a phone has a video camera. An administrator provides the codes,
                           or a user may be able to get one from the Self Care portal. But they expire after 1 week by default and an administrator regenerates
                           a new one.

This feature is supported on phones that are used within a company's premises.

Activation Code Onboarding requires Cisco Unified Communications Manager 12.5(1) or later to function properly.

##### Where to Find More Information

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

Cisco IP Phone 7800 Series User Guide

### Features Available
                  	 with the Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require the new firmware and the
                     			latest Cisco Unified Communications Manager Device Pack. The applicable device packs are
                     			released after the firmware release.

For information about the Cisco Unified IP Phones and the required Cisco
                     		Unified Communications Manager device packs, see the following URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html

#### Disable the Handset for Headset Users

Administrators can now disable the handset audio path on a phone. This allows users to easily handle calls with their headset,
                           and use their headset as the primary call management device. This is ideal for any user who frequently handles calls with
                           a headset, or for anyone who prefers the convenience of a headset.

Users must select Headset on the phone. The headset button on the phone is lit when the headset is selected. If the headset is not selected, then there
                           is no audio on the phone.

This feature is controlled with the Disable Handset parameter. Sign into Cisco Unified Communications Manager Administration,
                           and navigate to Device > Phone . Select your phone, and navigate to the Disable Handset field in the Product Specific Configuration Layout pane.

The Disable Speakerphone and the Disable Speakerphone and Headset parameters also control the audio path to the phone. If
                           these two parameters are used with the Disable Handset parameter, then there is no audio to the phone.

Disable Handset can be configured for individual phones, or for a group of phones with the Common Phone Profile.

##### Where to Find More Information

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

Cisco IP Phone 7800 Series User Guide

#### Disable Transport Layer Support Ciphers

You can now disable specific Transport Layer Support (TLS) cipher suites that are used by the TLS connection, or handshake
                           between the network and a phone. This allows you to tailor your security for known vulnerabilities, and to align your network
                           with your company's policies for ciphers.

You disable ciphers with the Disable TLS Ciphers parameter. Sign into Cisco Unified Communications Manager Administration,
                           and navigate to Device > Phones . Select your phone, and navigate to the Disable TLS Ciphers field in the Product Specific Configuration Layout pane.

Your choices are:

None

TLS_RSA_WITH_3DES_EDE_CBC_SHA

TLS_RSA_WITH_AES_128_CBC_SHA

TLS_RSA_WITH_AES_256_CBC_SHA

TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256

TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256

TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384

TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384

None is the default setting. If you select all of the phone ciphers, then phone TLS service is impacted.

For more information about phone ciphers and security, see Cisco IP Phone 7800 and 8800 Series Security Overview available at https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-8800-series/white-paper-listing.html

This feature has no user impact.

##### Where to Find More Information

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified
                        				Communications Manager ( Unified CM ) is running the latest device pack. After you install a device pack on the Unified CM servers in the cluster, you need to reboot all the servers.

If your Unified CM doesn't have the required device pack to support this firmware release, the firmware may not work correctly.

For information on the Unified CM Device Packs, see https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix.html .

### Install the Firmware Release on Cisco Unified Communications Manager

Before using the phone firmware release on the Cisco Unified Communications Manager, you must install the latest Cisco Unified
                        Communications Manager firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Choose Cisco IP Phone 7800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.5(1)SR2 .

Select the firmware file, click the Download or Add to cart button, and follow the prompts.

The firmware filename is cmterm-78xx.12-5-1SR2-2.k3.cop.sgn.

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following zip files are available
                        to load the firmware.

cmterm-78xx.12-5-1SR2-2.zip

Go to the following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Choose Cisco IP Phones 7800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.5(1)SR2 .

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

For additional information about SHA-2 use and support, see Security Guide for Cisco Unified Communications Manager ( https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html ).

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

### Softkey Templates and Video Mode

You can't configure softkey
                        				templates for Video mode on the Cisco IP Phone 7800 Series phones. If a softkey
                        				appears on the phone, then it will not function correctly.

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

Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.5(1),12.5(1.*)&sb=anfr&sts=fd&svr=3nH&bt=custV

Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.5(1),12.5(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV

Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.5(1),12.5(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco IP Phone 7800 Series for Firmware Release
                        12.5(1)SR2.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access the Bug Toolkit as described in View Caveats .

CSCvj80263: Sometimes the Phone will register back to vCluster after reset all on phone in hCluster

### Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series for Firmware
                        Release 12.5(1)SR2.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of resolved defects, access the Bug Toolkit as described in View Caveats .

CSCvn25400: java crashed during sharedline stress test

CSCvo24499: 88xx phones not sending audio alert to EHS headsets

CSCvn79514: No audible alert played for 7800/8800 IP phones when night service is enabled

CSCvo39524: 88xx: Display screen ON cannot be set for the 24h and kept ON always

CSCvo50891: 78xx Multiple Vulnerabilities in libxml2

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series for Firmware
                        Release 12.5(1)SR1.

CSCvn14646: CVE-2018-18559: Linux Kernel Use-After-Free Race Condition Vulnerability

CSCvn47250: Phone crashes after receiving malformed CDP/LLDP data

CSCvn54297: Slow user interface due to PAE process memory leak when 802.1x is enabled but not used

CSCvn56168: Buffer overflow vulnerability in the phone webserver

CSCvn56175: Authorization bypass in phone web interface

CSCvn56213: Phone file upload path traversal and null injection vulnerability

CSCvn56221: CSRF vulnerability in the phone upload function

CSCvn57643: No ringback tone played after initial announcement

CSCvn72978: IP Phone getting unregistered when using Alcatel Switch

The following table lists severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series for Firmware Release
                        12.5(1).

CSCvh50751: Sometimes phone will play "pop" "pop" noise after do factory reset/power cycle to the phone.

CSCvj70969: 7800/8800 DND SIP PUBLISH does not stop when there is no 200 OK reply

CSCvj74252: CP 78XX phone crash when using the Russian locale

CSCvk01549: Extension Mobility: CUCM Remember last logged in user. Parse error on phone

CSCvk70068: 78XX / 88XX freezes after quick operations

CSCvm44063: Phone unresponsive (gets frozen) when the phone connect to the laptop which has CUVA driver enable

CSCvm59252: CVE-2018-14618: cURL and libcurl NTLM Password buffer overflow vulnerability

CSCvm77024: CVE-2018-17182: Use-after-free in vmacache-flush_all() kernel function vulnerability

CSCvm91270: Java memory leak in AnimatedGraphic when making basic calls

CSCvn16281: 78XX Phones do not follow the DSCP policy of CUCM.

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

| Note | Firmware Release 12.5(1)SR2 replaces Firmware Release 12.5(1) and Firmware 12.5(1)SR1. Firmware Release 12.5(1) and Firmware
                              Release 12.5(1)SR1 have been deferred in favor of Firmware Release 12.5(1)SR2. |
|---|---|

| Cisco IP Phone | Protocol | Cisco Unified Communications Manager |
|---|---|---|
| Cisco IP Phones 7811, 7821, 7841, and 7861 | SIP | Cisco Unified Communications Manager version 8.5(1) and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above |
| Cisco IP Phones 7811, 7821, 7841, and 7861 | SIP | CME 10.0 (IOS load 15.3(3)M) |
| Cisco IP Phones 7811, 7821, 7841, and 7861 |  | Cisco Expressway X8.7 or Cisco TelePresence Video Communication Server X8.7 (for Mobile and Remote Access) |

| Note | If your Unified CM doesn't have the required device pack to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phone 7800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.5(1)SR2 . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. The firmware filename is cmterm-78xx.12-5-1SR2-2.k3.cop.sgn. Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
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
| Step 5 | In the Latest Releases folder, choose 12.5(1)SR2 . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

| Caution | Do not connect the SW and PC ports into the LAN. |
|---|---|

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.5(1),12.5(1.*)&sb=anfr&sts=fd&svr=3nH&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.5(1),12.5(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.5(1),12.5(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV |
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