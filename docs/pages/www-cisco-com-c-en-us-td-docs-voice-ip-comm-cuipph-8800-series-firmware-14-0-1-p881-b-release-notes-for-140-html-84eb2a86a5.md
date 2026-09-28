---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-firmware-14-0-1-p881-b-release-notes-for-140-html-84eb2a86a5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/firmware/14_0_1/p881_b_release-notes-for-140.html
retrieved_at: 2026-08-21T13:29:42.270243+00:00
---

Cisco IP Phone 8800 Release Notes for Firmware Release 14.0(1)

# Cisco IP Phone 8800 Release Notes for Firmware Release 14.0(1)

### Download Options

Updated: March 31, 2021

First Published: April 1, 2021

Last Updated: March 25, 2022

# Cisco IP Phone 8800 Release Notes for Firmware Release 14.0(1)

These release notes support the Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR running SIP Firmware
                  Release 14.0(1).

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

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Phone 7800 Series.

The Deployment Guide is located at the following URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-implementation-design-guides-list.html

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

#### User Interface Enhancements

This release contains the following enhancements to the phone user interface:

When the phone is in Mobile and Remote Access mode, Extension Mobility
                                 						doesn't allow automatic sign-in when the user plugs in their headset.

This feature requires no administration.

When the phone is in Survivable Remote Site Telephony (SRST) mode, the phone can display a
                                 						programmable line key with a Service URL.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

Cisco IP Phone 8800 Series Administration Guide

#### COP File SHA-512 Enhancement

Beginning with Cisco Unified Communications Manager version 14.0, all phone loads must be encrypted with the SHA512 hashing
                           algorithm and end with the file name .cop.sha512 .

##### Where to Find More Information

Security Guide for Cisco Unified Communications Manager 14.0(1)

#### Cisco Headset 730 Enhancements for Cisco IP Phone 8800 Series

This release provides these Cisco Headset 730 enhancements:

An animated upgrade process indicator displays on the phone screen.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

#### Headset Ringtone Setting on Cisco IP Phones

You can change your headset ringtone behavior through the Preferences menu on the Cisco IP Phone 7800 and 8800 Series.

The setting saves to the phone and applies to any Cisco headset that connects.

If you use the Cisco Headset 560 Multibase, you need to press on the base for your ringtone changes to take effect.

By default, your phone follows the behavior of the phone ringer settings. Select On if you want to hear the phone ring whenever you have an incoming call. Select Off if you don't want to hear any ring through your headset when there’s an incoming call.

##### Where to Find More Information

Cisco Headset 500 Series User Guide

Cisco IP Phone 8800 Series User Guide

#### Hunt Group Enhancements

Hunt group enhancements:

If a phone is part of a broadcast hunt group, calls picked up by other members of the hunt
                                 						group display in call history as a Received call.

The Hunt Group label now includes the term Hunt group followed by the Hunt group number or name. This improvement helps you
                                 identify Hunt Group calls, and it is included in the Received call list, the All calls list, and Call details.

This feature requires Cisco Unified Communications Manager 12.5(1)SU3 or later to work.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

Cisco Unified Communications Manager documentation

#### Security Enhancement

This release provides the following security enhancement:

Datagram Transport Layer Security (DTLS) 1.2 support.

DTLS 1.2 requires Cisco Adaptive Security Appliance (ASA) Release 9.10 or later. You configure the minimum DTLS version for
                                       a VPN connection in ASA.

DTLS 1.2 has no user or administrator impact.

##### Where to Find More Information

ASDM Book 3: Cisco ASA Series VPN ASDM Configuration Guide at https://www.cisco.com/c/en/us/support/security/asa-5500-series-next-generation-firewalls/products-installation-and-configuration-guides-list.html

#### SIP OAuth Mode for Mobile and Remote Access Through Expressway

SIP OAuth mode is now supported for Mobile and Remote Access
                              				Through Expressway . This mode allows you to use OAuth access tokens for authentication in secure
                           				environments.

SIP OAuth mode is supported on Cisco Expressway release X14.0(1) and later, and Cisco Unified
                           				Communications Manager 14.0(1) and later.

For SIP OAuth in Mobile and Remote Access (MRA) mode, use only Activation Code Onboarding
                                       					with Mobile and Remote Access when you deploy the phone. Activation with
                                       					username and password is not supported.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide

Feature Configuration Guide for Cisco Unified Communications Manager (Release
                                 						14.0(1) or later)

#### OAuth Enhancement

You can improve the security of your phones to use OAuth tokens to authenticate the phones. SIP lines with OAuth allow secure
                           signalling and media.

The feature requires Cisco Unified Communications Manager Release 14.0(1) or later.

You enable the feature from the Cisco Unified Communications Manager Administration System > Enterprise Parameters page.

This feature has no user impact.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide

Feature Configuration Guide for Cisco Unified Communications Manager (Release
                                 						14.0(1) or later)

### Features Available with the Latest Cisco Unified
                     				Communications Manager Device Package

The following sections describe features in the release which require the new firmware and the latest Cisco Unified
                        				Communications Manager device package. The applicable device packages are released after the firmware release.

For information about the Cisco devices and the required Cisco Unified
                        				Communications Manager device packages, see the following URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html

#### Call Park Monitoring Enhancement

You can set up call park in two different ways:

The parked call displays on the phone where the user can pick it up.

The user must dial the displayed number to pick up the call.

You set the field Dedicate one line for Call Park in Cisco Unified
                           				Communications Manager to enable or disable the feature. By default, the feature is
                           				enabled.

When the field is enabled, the parked call remains on the user's line and they can use the Resume softkey to pick up the call. The user sees the
                           				extension number for the parked call on the phone display.

When the field is disabled, the parked call transfers to the call park line. The user's line
                           				returns to the idle state and they see the call park extension in a pop-up window.
                           				The user dials the extension to pick up the call.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide

Cisco IP Phone 8800 Series User Guide

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified
                        				Communications Manager is running the latest device package. After you install a device package on the Cisco Unified
                        				Communications Manager servers in the cluster, you need to reboot all the servers.

If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly.

For information on the device packages, see the Cisco Unified
                        				Communications Manager Device Package Compatibility Matrix .

### Install the Firmware Release on Cisco Unified Communications Manager

Before using the phone firmware release on the Cisco Unified Communications Manager, you must install the latest Cisco Unified
                        Communications Manager firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco IP Phone 8800 Series .

Choose your phone type.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 14.0(1) .

Select the firmware file, click the Download or Add to Cart button, and follow the prompts:

The firmware filename is cmterm-88xx-sip.14-0-1-0001-135.k3.cop.sha512

If you added the firmware file to the cart, click the Download All link when you are ready to download the file.

Click the + next to the firmware file name in the File Information section to access additional information about this file. The hyperlink
                                 for the Readme file is in the Details section, which contains installation instructions for the corresponding firmware.

Follow the instructions in the Readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following .zip files are available
                        to load the firmware:

cmterm-88xx.14-0-1-0001-135_REL.zip

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                        interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco IP Phones 8800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 14.0(1) .

Download the relevant zip files.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and video quality, and in some cases, can cause a call to
                        drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

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
                        				templates for Video mode on the Cisco IP Phone 8800 Series phones. If a softkey
                        				appears on the phone, then it will not function correctly.

## Caveats

### View Caveats

You can search for caveats using the Cisco Bug Search Tool.

Known caveats are graded according to severity level, and can be either open or resolved.

Perform one of the following actions:

Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284729655&rls=14.0(1),14.0(1.)&sb=anfr&sts=fd&svr=3nH&bt=custV

Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.0(1)&sb=afr&sts=open&svr=3nH&bt=custV

Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284729655&rls=14.0(1),14.0(1.)&sb=fr&sts=fd&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

The following list contains a snapshot of severity 1, 2, and 3 caveats that are open for the Cisco IP Phone 8800 Series for
                        Firmware Release 14.0(1).

For more information about an individual bug, access the Bug Search Tool and search for the caveat using the Identifier. You
                        must be a registered Cisco.com user to access this online information.

Because caveat status continually changes, the list reflects a snapshot of the caveats that were open at the time this report
                        was compiled. For an updated view of open caveats, access the Bug Search Tool as described in View Caveats .

CSCvo74172 - 8861 phone should not roaming from WLC with Platinum QOS to WLC with Silver QOS

CSCvp34626 - No wifi icon displayed at the upper right corner of LCD after wifi connection done

CSCvq21512 - 8861 deregister when running JFW roaming about 3 hours(EAP-TLS with WPA2+ 11r over the DS)

CSCvq32455 - 8845_65 ip phone reset/restart intermittently after disconnect of a call

CSCvq37245 - Active server shows empty under phone information page in ipv6 only mode

CSCvq59064 - 802.11r fast transition sometimes failed to work on 8861

CSCvq89463 - 8845/8865 freezing randomly

CSCvt18121 - 8865 Phones video freezing on CMS in side-by-side view

### Resolved Caveats

The following list contains the snapshot of severity 1, 2, and 3 caveats that are resolved for the Cisco IP Phone 8800 Series
                        that uses Firmware Release 14.0(1).

For more information about an individual caveat, you can access the online record for the caveat from the Bug Search Tool.
                        You must be a registered Cisco.com user to access this online information.

Because bug status continually changes, the list reflects a snapshot of the caveats that were resolved at the time this report
                        was compiled. For an updated view of resolved caveats or to view specific caveats, access the Bug Search Tool as described
                        in View Caveats .

CSCvu24261 - 8865 enbloc dialing DTMF not working when calling to UCCX

CSCvu05618 - Missing SRST information on Phone webpage

CSCvu43767 - Missing RTP stream when Built-in-Bridge Recording through MRA is used for IPhone

CSCvv66008 - CP-88xx sends corrupted SIP messages when debugs are enabled

CSCvv58736 - 88xx phone can't conference/transfer external pstn phone when the jtapi application

CSCvu84549 - remote log profile settings on CUCM do not take effect on phone

CSCvu59349 - Multiple BufferOverflow + Out of Bounds Read for LLDP and CDP

CSCvw14189 - 8865 EAP-TLS User Certificate Upload Fails With Extract Passwords = 12

CSCvv86511 - JTAPI application will miss once 8851 call PSTN number

CSCvw09869 - Adding key-value pair to support additional "For %s" translations.

CSCvt27644 - Cisco IP Phone Call Log Information Disclosure Vulnerability

CSCvw30093 - Cisco IP Phone 8800 Series, CDP packets ignored if switch hostname starts with SEP

CSCvw29327 - VPN connection on 8861 phone does not auto reconnect after TFTP setting is changed

CSCvw45287 - 8851 phone over MRA phone stuck after loosing connectivity

CSCvw21091 - 8861 phone / infinite loop of querying DHCP server every second

CSCvw41907 - SIP phones call stats had Vopktlost & LostPkt with negative values -1, -6

CSCvw05530 - Third party USB headset audio mute not working on 8861

CSCvx49514 - BE HW Rev 42 - One way audio for CIPC <-> IP Phone call using iSAC codec

CSCvx31021 - mute button on 8861 V15+ phones doesn't take effect when connected with BT heads

CSCvw96157 - Ghost call seen when closing a conference call with 88xx phones

CSCvx18825 - Cisco 730 headset with USB connected to 8851/8865 does not appear on CUCM headset

CSCvw60960 - 8851 phones sometimes use TLS 1.0 instead of 1.2 for HTTPS

## Cisco Unified Communication Manager Public Keys

To improve software integrity protection, public keys are used to sign cop files for Cisco Unified Communications Manager
                     Release 10.0.1 and later. These cop files have "k3 or k4" in their name. To install a k3 or k4 cop file on a pre-10.0.1 Cisco Unified Communications Manager, consult the Readme for
                     the ciscocm.version3-keys.cop.sgn to determine if you must install this additional cop file on your specific Cisco Unified
                     Communications Manager version. If these keys are not present and are required, you will see the error "The selected file is not valid" when you try to install the software package.

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

You may want to bookmark the web pages for the phone models that are deployed in your company and send these URLs to your
                                 users.

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Cisco IP Phone | Support Requirements |
|---|---|
| 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR | Cisco Unified Communications Manager 8.5(1) and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above Cisco Expressway 8.7 |
| 8811, 8841, 8851, 8851NR, and 8861 | CME 10.0 (IOS load 15.3(3)M) |

| Note | This feature requires Cisco Unified Communications Manager 12.5(1)SU3 or later to work. |
|---|---|

| Note | DTLS 1.2 requires Cisco Adaptive Security Appliance (ASA) Release 9.10 or later. You configure the minimum DTLS version for
                                       a VPN connection in ASA. |
|---|---|

| Note | For SIP OAuth in Mobile and Remote Access (MRA) mode, use only Activation Code Onboarding
                                       					with Mobile and Remote Access when you deploy the phone. Activation with
                                       					username and password is not supported. |
|---|---|

| Note | If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phone 8800 Series . |
| Step 3 | Choose your phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 14.0(1) . |
| Step 6 | Select the firmware file, click the Download or Add to Cart button, and follow the prompts: The firmware filename is cmterm-88xx-sip.14-0-1-0001-135.k3.cop.sha512 Note If you added the firmware file to the cart, click the Download All link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download All link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download All link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware file name in the File Information section to access additional information about this file. The hyperlink
                                 for the Readme file is in the Details section, which contains installation instructions for the corresponding firmware. |
| Step 8 | Follow the instructions in the Readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download All link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phones 8800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 14.0(1) . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284729655&rls=14.0(1),14.0(1.)&sb=anfr&sts=fd&svr=3nH&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.0(1)&sb=afr&sts=open&svr=3nH&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=284729655&rls=14.0(1),14.0(1.)&sb=fr&sts=fd&svr=3nH&bt=custV |
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