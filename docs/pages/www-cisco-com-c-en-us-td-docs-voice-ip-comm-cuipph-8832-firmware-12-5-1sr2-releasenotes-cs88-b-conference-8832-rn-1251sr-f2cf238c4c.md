---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8832-firmware-12-5-1sr2-releasenotes-cs88-b-conference-8832-rn-1251sr-f2cf238c4c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8832/firmware/12-5-1SR2/releasenotes/cs88_b_conference-8832-rn-1251sr2.html
retrieved_at: 2026-08-21T13:28:52.359763+00:00
---

Cisco IP Conference Phone 8832 Release Notes for Firmware Release 12.5(1)SR2

# Cisco IP Conference Phone 8832 Release Notes for Firmware Release 12.5(1)SR2

### Download Options

Updated: March 25, 2019

First Published: March 25, 2019

# Cisco IP Conference Phone 8832 Release Notes for Firmware Release 12.5(1)SR2

These release notes support the Cisco IP Conference Phone 8832 running SIP Firmware Release 12.5(1)SR2.

Firmware Release 12.5(1)SR2 replaces Firmware Release 12.5(1) and Firmware 12.5(1)SR1. Firmware Release 12.5(1) and Firmware
                              Release 12.5(1)SR1 have been deferred in favor of Firmware Release 12.5(1)SR2.

The following table lists the support and protocol compatibility for the Cisco IP Phones.

Cisco IP Phone

Protocol

Support Requirements

8832

SIP

Cisco Unified Communications Manager 10.5(2) and later

Cisco Unified Communications Manager time zone update 2016d or later

SRST 8.0 (IOS load 15.1(1)T) and above

Cisco Expressway 8.7

8832

SIP

Unified CME 12.3 (Cisco IOS XE Fuji 16.9.1 release)

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Conference Phone 8832 Documentation

Refer to publications that are specific to your language, phone model, and call control system. Navigate from the following
                        documentation URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/tsd-products-support-general-information.html

### Cisco Unified
                     				Communications Manager Documentation

See the Cisco Unified
                              				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                           				Communications Manager release. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html

## New and Changed Features Introduced in Firmware Release 12.5(1) and 12.5(1)SR1

In Firmware Release 12.5(1) and Firmware Release 12.5(1)SR1, we introduced the features in the following sections. No new
                     features were introduced in Firmware Release 12.5(1)SR2.

### Features Available
                  	 with the Firmware Release

The following sections describe the features available with the Firmware
                     		Release.

#### Transport Layer Security 1.2 and Wireless Authentication

Transport Layer Security (TLS) 1.2 for wireless authentication is now supported on Wi-Fi enabled phones.

Wireless 802.1x authentication uses Cisco ISE 2.4 as the RADIUS server. However, EAP-FAST authenticate mode is not supported
                                          when Transport Layer Security (TLS) 1.2 is enabled.

TLS is supported on the Cisco IP Phone 8832.

TLS 1.2 is a cryptographic protocol that improves network security, and it replaces Socket Layer (SSL) as the recommended
                           security protocol for Wi-Fi enabled phones.

TLS Setup chapter in the Security Guide for Cisco Unified Communications Manager, Release 11.5(1)SU3 or later, available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

TLS 1.2 Compatibility Matrix available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/unified/communications/system/Compatibility/TLS/TLS1-2-Compatibility-Matrix.html

This feature has no user impact.

##### Where to Find More Information

Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

#### Whisper Paging and Cisco Unified Communications Manager Express

Your users have an improved call experience with whisper paging. In previous releases, your calls were interrupted by a page.
                           But now your phone rejects any pages when you are on a call, and ensures a distraction-free experience.

This feature is supported on Cisco Unified Communications Manager Express.

##### Where to Find More Information

Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

#### Elliptic Curve Support

Your Cisco IP Phone has been made even more secure with support for Elliptic Curve Digital Signature Algorithm (ECDSA) certificates.
                           These certificates are stronger than the RSA-based certificates and require a smaller key size, making them a quicker solution
                           for your network security.

The ECDSA certificates are available in the following areas—Certificate Manager, SIP, Certificate Authority Proxy Function
                           (CAPF), Transport Layer Security (TLS) Tracing, Entropy, HTTP, and computer telephony integration (CTI) Manager.

Elliptic Curve Digital Signature Algorithm (ECDSA) certificates require Cisco Unified Communications Manager 12.5(1) or later.

##### Where to Find More Information

Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

Security Guide for Cisco Unified Communications Manager, Release 12.0(1)

### Features Available
                  	 with the Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require
                     		the new firmware and the latest Cisco Unified Communications Manager Device
                     		Pack.

For information about the Cisco Unified IP Phones and the required Cisco
                     		Unified Communications Manager device packs, see the following URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html

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

Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

#### Enbloc Dialing

You can now place calls quicker with Enbloc Dialing. When enabled, this feature eliminates the delay often experienced when
                           dialing a phone number during the following scenarios:

On hook dialing and redialing

Speed dial and Speed dial BLF

Voice mail

Calls that are made from your Recent list

Calls that are made from your Directory

Previously users experienced a delay of up to 15 seconds when placing a call.

Administrators can find the Enbloc Dialing parameter in the Product Specific Configuration Layout section of the Cisco Unified
                           Communications Manager. When enabled, it overrides the T.302 timer and the entire dialed string is sent to the Cisco Unified
                           Communications Manager once the dialing is complete.

Forced Authorization Codes (FAC) or Client Matter Codes (CMC) do not support Enbloc Dialing. If you use FAC or CMC to manage
                           call access and accounting, then you cannot use this feature.

##### Where to Find More Information

Cisco Collaboration System 12.x Solution Reference Network Designs

Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

## Installation

### Installation
                  	 Requirements

Before you install
                        		  the firmware release, you must ensure that your Cisco Unified Communications
                        		  Manager is running the latest device pack. After you install a device pack on
                        		  the Cisco Unified Communications Manager servers in the cluster, reboot all the
                        		  servers.

The Cisco IP Conference Phone 8832 PoE Injector is supported on phones running firmware release 12.0(1)SR2 and later. Confirm
                                    			 that the latest firmware release is installed on the Cisco Unified
                                    			 Communications Manager before you connect the Cisco IP Conference Phone 8832
                                    			 with the PoE injector to the network.

If you are not
                                    			 using the latest firmware release, then your phone may downgrade to an earlier
                                    			 firmware release, and lose network connectivity.

### Install the Firmware Release on Cisco Unified Communications Manager

Before using the phone firmware release on the Cisco Unified Communications Manager, you must install the latest Cisco Unified
                        Communications Manager firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose IP Conference Phone 8832 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.5(1)SR2 .

Select the firmware file, click the Download or Add to cart button, and follow the prompts.

The firmware filename is cmterm-8832-sip.12-5-1SR2-2.k3.cop.sgn.

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following .zip file is available
                        to load the firmware:

cmterm-8832.12-5-1SR2-2.zip

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                        interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose IP Conference Phone 8832 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.5(1)SR2 .

Download the relevant zip files.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone voice and in some cases can cause a call to drop. Sources of
                        network degradation can include, but are not limited to, the following activities:

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Firmware
                  	 Limitation of Cisco IP Conference Phone 8832 with Cisco IP Conference Phone
                  	 8832 PoE Injector

The Cisco IP Conference Phone 8832 PoE Injector is supported on phones running firmware release 12.0(1)SR2 and later. Confirm that the latest firmware release is installed
                     on the Cisco Unified Communications Manager before you connect the Cisco IP Conference Phone 8832 with the PoE injector to
                     the network.

If you are not using the latest firmware release, then your phone may downgrade to an earlier firmware release, and lose the
                     network connectivity.

To recover a phone that has lost network connectivity, update Device Defaults for the Cisco IP Conference Phone 8832 to 8832-sip.12-0-1SR2-2.k3.cop.sgn or later in Cisco Unified Communications Manager Administration. Then, perform one of the following steps:

Force the phone to reboot from the alternate software image that supports the PoE Injector. To reboot your phone from the
                           backup image, see Boot Up the Conference Phone from the Alternate Partition section in the Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager .

Install and use the Cisco IP Conference Phone 8832 Ethernet Injector on the phone. This allows you to regain network connectivity. After the phone has upgraded to the latest firmware, you can
                           again use the Cisco IP Conference Phone 8832 PoE Injector .

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

### Wireless Microphone Battery Limitation

When you press the Show detail softkey, the Cisco IP Conference Phone 8832 occasionally displays a false Bad battery warning. This issue occurs when you quickly reseat the wireless microphone 20 consecutive times or more.

To recover from this issue, perform the following steps in order:

Remove the microphone from the charging cradle.

Press the Mute button for approximately 10 seconds or until the microphone LED stops blinking white. Then, reseat the microphone on the
                              charging cradle.

Restart the phone by disconnecting and reconnecting the Cisco IP Conference Phone 8832 Power Adapter.

The Bad battery warning on the phone screen disappears and the current battery status appears. If you do not see the battery status, then
                              the microphone battery has deteriorated and you must replace it.

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

To find all caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286317183&rls=12.5(1)&sb=anfr&sts=open&svr=3nH&bt=custV

To find all open caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286317183&rls=12.5(1)&sb=afr&sts=open&svr=3nH&bt=custV

To find all resolved caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286317183&rls=12.5(1),12.5(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional)  To look for information about a specific problem, enter the bug ID number in the Search for field, and press Enter .

### Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 8832 for Firmware
                        Release 12.5(1)SR2.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in View Caveats .

CSCvh27756: 8832 with smart adapter can not link up after switch changes speed from 10 to 100

CSCvh46147: The "Network statistics" show "No link" when configure the switch port with same settings "100half"

CSCvj03598: 8832 cannot set static IP manully on wifi (without default router)

### Resolved Caveats

The following lists contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 8832 for Firmware
                        Release 12.5(1)SR2.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were resolved at the time this
                        report was compiled. For an updated view of closed defects, access Bug Toolkit as described in View Caveats .

CSCvn25400: java crashed during sharedline stress test

CSCvn39812: 8832 phone cannot display the scanned wireless SSID list sometimes

CSCvn79514: No audible alert played for 7800/8800 IP phones when night service is enabled

CSCvn88077: 8832 phones will display the incorrect information after input CFA numberr

CSCvo39524: 88xx: Display screen ON cannot be set for the 24h and kept ON always

CSCvo50891: 78xx Multiple Vulnerabilities in libxml2

The following lists contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 8832 for Firmware
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

The following lists contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 8832 for Firmware
                        Release 12.5(1).

CSCvh65310: 8832: there is pop noise if pressing volume up/down after cancel dialing

CSCvi19720: double talk performance refinement at max volume

CSCvi98837: 8832 can connect the ssid while 802.11 mode error

CSCvj01727: 8832 cannot change 802.11 mode from 2.4G to 5G after fail to connect with ssid by other softkey

CSCvj14231: 8832 HTTP Security Header Not Detected vulnerability reported by vulnerability scanner

CSCvj33740: When 8832 phones downgrade from 12-0-1SR3-1 to 12-0-1-12 phone does not boot

CSCvm22237: wpa_supplicant EAPOL-Key Messages Information Disclosure Vulnerability

CSCvm46669: IP phone 8832 incompatibility with Juniper switch

CSCvm77026: Linux Kernel vmacache_flush_all() Function Use-After-Free Vulnerability

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

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| 8832 | SIP | Cisco Unified Communications Manager 10.5(2) and later Cisco Unified Communications Manager time zone update 2016d or later SRST 8.0 (IOS load 15.1(1)T) and above Cisco Expressway 8.7 |
| 8832 | SIP | Unified CME 12.3 (Cisco IOS XE Fuji 16.9.1 release) |

| Note | Wireless 802.1x authentication uses Cisco ISE 2.4 as the RADIUS server. However, EAP-FAST authenticate mode is not supported
                                          when Transport Layer Security (TLS) 1.2 is enabled. |
|---|---|

| Warning | The Cisco IP Conference Phone 8832 PoE Injector is supported on phones running firmware release 12.0(1)SR2 and later. Confirm
                                    			 that the latest firmware release is installed on the Cisco Unified
                                    			 Communications Manager before you connect the Cisco IP Conference Phone 8832
                                    			 with the PoE injector to the network. If you are not
                                    			 using the latest firmware release, then your phone may downgrade to an earlier
                                    			 firmware release, and lose network connectivity. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose IP Conference Phone 8832 . |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | In the Latest Releases folder, choose 12.5(1)SR2 . |
| Step 5 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. The firmware filename is cmterm-8832-sip.12-5-1SR2-2.k3.cop.sgn. Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 6 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 7 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose IP Conference Phone 8832 . |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | In the Latest Releases folder, choose 12.5(1)SR2 . |
| Step 5 | Download the relevant zip files. |
| Step 6 | Unzip the files. |
| Step 7 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

| Step 1 | Perform one of the following actions: To find all caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286317183&rls=12.5(1)&sb=anfr&sts=open&svr=3nH&bt=custV To find all open caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286317183&rls=12.5(1)&sb=afr&sts=open&svr=3nH&bt=custV To find all resolved caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286317183&rls=12.5(1),12.5(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV |
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