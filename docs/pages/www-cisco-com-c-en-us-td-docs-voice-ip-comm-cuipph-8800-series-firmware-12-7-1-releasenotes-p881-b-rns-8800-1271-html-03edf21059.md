---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-firmware-12-7-1-releasenotes-p881-b-rns-8800-1271-html-03edf21059
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/firmware/12-7-1/releasenotes/p881_b_rns-8800-1271.html
retrieved_at: 2026-08-21T13:31:55.129235+00:00
---

Cisco IP Phone 8800 Series Release Notes for Firmware Release 12.7(1)

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 12.7(1)

### Download Options

Updated: May 4, 2020

First Published: January 23, 2020

Last Updated: February 10, 2021

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 12.7(1)

These release notes support the Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR running SIP Firmware
                  Release 12.7(1).

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

## New and Changed
               	 Features

The following sections describe the features that are new or have
                  		changed in this release.

Some features may require the installation of a Cisco Unified Communications Manager Device Package. Failure to install the
                              Device Package before the phone firmware upgrade may render the phones unusable.

### Features Available
                  	 with the Firmware Release

The following sections describe the features available with the Firmware
                     		Release.

#### Cisco Headset 730 Support

Users can now use the Cisco Headset 730 with their Cisco IP Phone 8800 Series phone. This headset is a wireless headset that uses Bluetooth connectivity to pair with the phone. The headset features full
                           call control and music playback capabilities in addition to powerful noise cancellation and ambient audio enhancement systems
                           for use in a busy office environment.

The headset comes with a USB Bluetooth Adapter (dongle) for use with devices that don't offer a reliable Bluetooth solution.
                           A USB-C cable acts as a charging cable and can connect to any powered USB adapter. The USB-C cable can also be plugged into
                           the phone USB port to give full functionality, including call control, local tuning and setup, and firmware upgrades.

Currently, customization, firmware management, and inventory management are only supported when the headset is connected to
                           the phone with the USB-C cable.

The following table shows the support of the headset by connection type and phone model.

Connection Type

8811

8841

8845

8851

8851NR

8861

8865

8865NR

USB

(dongle or USB-C cable)

Not supported

Not supported

Not supported

Supported

Supported

Supported

Supported

Supported

Bluetooth

Not supported

Not supported

Supported

Supported

Not supported

Supported

Supported

Not supported

Users can customize their headset from the phone screen. Customization includes noise cancellation, sidetone levels, and some
                           common actions.

For this release, users can customize their headset only when the headset is connected to the phone with the USB-C cable.
                           If users connect the headset by Bluetooth or the USB dongle, customization is not available.

You can view headset information in the phone web pages.

The headset is supported with the Cisco Unified
                              				Communications Manager Administration Headset Serviceability pages. Cisco Headset 730 serviceability is available on Cisco Unified Communications Manager Software Release 11.5(1)SU7, and 12.5(1)SU1 or later.

##### Where to Find More Information

Cisco IP Phone 7800 and 8800 Series Accessories Guide for Cisco Unified Communications Manager

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

Cisco IP Phone 8800 Series User Guide

Cisco Headset 730 documentation

Cisco Unified
                                    				Communications Manager documentation

#### Enable Electronic Hookswitch Control on Your Phone

Users can now enable the  Electronic hookswitch control or e-hook from their phone. Previously, this parameter was located
                           on the phone page in Cisco Unified Communications Manager. This improvement makes it easier for users to enable and use their
                           headsets.

You provide access to the administration settings on the phone. Users enable this parameter by navigating Admin settings > Aux port .

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

#### Hunt Groups and Incoming Call Alerts

You can configure your hunt groups to display either the hunt group name or hunt group number for incoming calls. This makes
                           it easier for users to recognize and respond to group calls when logged into the queue.

By default, the pilot number displays for the incoming call. To have the group name display, enter a name in the Alerting
                           Name field when you configure the pilot number.

This feature requires Cisco Unified Communications Manager 11.5(1)SU1 or later.

##### Where to Find More Information

Feature Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Cisco IP Phone 8800 Series User Guide

#### Lower Your Voice Alert

Users can help keep their phone conversations at an appropriate volume level with the Lower Your Voice alert.

When you speak loudly, a warning message displays on the phone screen. You can lower your voice or select Ignore .

This feature is enabled by default and is located in the phone settings menu if you want to disable it. It does not require
                           any configuration in Cisco Unified Communications Manager.

Lower Your Voice is available for handsets and headsets only.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

#### Mark A Call as Spam

You can use the Mark spam feature to reduce the number of unwanted calls you receive. With this feature, you designate a phone
                           number as either a fraudulent call or as a telemarketer call. Fraudulent calls are declined and blocked. Telemarketer calls
                           ring through to you. But these calls have the term Telemarketer in the Incoming Call Alert and they have an icon next to them
                           in Recents.

You mark active, or recent calls. You can view and edit your Spam call list from the Settings menu. The Spam call list can have up to 150 calls.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

#### Select Button LED and Energy Save Mode

Users can turn off the Select button LED when in Power Save mode. This helps reduce visual distractions.

Users control the Select button LED in Settings > Power save indicator .

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

#### User Interface Change

When Enhanced Line Mode users receive an incoming call, they see the word "For" followed by the name of the person or line used to make the call.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

#### User Interface Enhancements to Support the Cisco Headset 500 Series

You can use the headset information on the IP Phone web page to assist in troubleshooting problems. When you access the web
                           page, the information is on the Device Information page.

The following information is displayed:

Port—Displays how the headset connects to the phone.

Version—Displays the headset firmware version.

Radio range—Displays the strength configured for the DECT radio. Applicable to the Cisco Headset 560 Series only.

Bandwidth—Displays if the headset uses Wide band or Narrow band. Applicable to the Cisco Headset 560 Series only.

Bluetooth—Displays if Bluetooth is enabled or disabled. Applicable to the Cisco Headset 560 Series only.

Conference—Displays if the conference feature is enabled or disabled. Applicable to the Cisco Headset 560 Series only.

This feature has no user impacts.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager

Cisco Headset 500 Series documentation

#### Wallpaper Support on Key Expansion Modules

You can use wallpaper or background images on both your Cisco IP Phone and your key expansion module. This provides a consistent
                           look across your device, and is a popular way to display corporate images. Users can select an image from one of the provided
                           backgrounds or you can upload a customized image.

If you are using a customized image then you need an image for the phone and an image for the key expansion module. Upload
                           the images to your TFTP server in the following directories:

Cisco IP Phone 8800 Series—Desktops/800x480x24.

Cisco IP Phone 8851 and 8861 Key Expansion Module with a dual LCD screen—Desktops/320x480x24.

Cisco IP Phone 8865 Key Expansion Module with a dual LCD screen—Desktops/320x480x24.

Cisco IP Phone 8800 Key Expansion Module with a single LCD screen—Desktops/272x480x24.

Thumbnail images—139 pixels (width) by 109 pixels (height).

Cisco IP Phone 8800 Series—800 pixels by 480 pixels.

Cisco IP Phone 8851and 8861 Key Expansion Module with a dual LCD screen—320 by 480 pixels.

Cisco IP Phone 8865 Key Expansion Module with a dual LCD screen—320 by 480 pixels.

Cisco IP Phone 8800 Key Expansion Module with a single LCD screen—272 by 480 pixels.

You restart the TFTP server after the images upload. Apply the images and restart the phone.

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide .

Cisco IP Phone 8800 Series Administration Guide for Cisco Unified Communications Manager .

Customized Wallpapers Best Practices Cisco IP Phone 8800 Series ( https://www.cisco.com/c/dam/en/us/products/collateral/collaboration-endpoints/unified-ip-phone-8800-series/white-paper-c11-740036.pdf ).

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

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco IP Phone 8800 Series .

Choose your phone type.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.7(1) .

Select the firmware file, click the Download or Add to cart button, and follow the prompts:

For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx-sip.12-7-1-0001-393.k3.cop.sgn

For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65-sip.12-7-1-0001-393.k3.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following .zip files are available
                        to load the firmware:

For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx.12-7-1-0001-393.zip

For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65.12-7-1-0001-393.zip

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                        interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco IP Phones 8800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.7(1) .

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

### Softkey Templates and Video Mode

You can't configure softkey
                        				templates for Video mode on the Cisco IP Phone 8800 Series phones. If a softkey
                        				appears on the phone, then it will not function correctly.

## Caveats

### View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

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

The following list contains severity 1, 2, and 3 defects that are open for the Cisco IP Phone 8800 Series for Firmware Release
                        12.7(1).

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in View Caveats .

CSCvn86806 remove the usb2 cable from mac will cause IP phone popup remove toast

CSCvo71625 Sometimes the phone screen doesn't display the last digit of the phone number

CSCvo74172 8861 phone should not roaming from WLC with Platinum QOS to WLC with Silver QOS

CSCvp34626 No wifi icon displayed at the upper right corner of LCD after wifi connection done

CSCvq21512 8861 deregister when running JFW roaming about 3 hours(EAP-TLS with WPA2+ 11r over the DS)

CSCvq32455 8845_65 ip phone reset/restart intermittently after disconnect of a call

CSCvq37245 Active server shows empty under phone information page in ipv6 only mode

CSCvq59064 802.11r fast transition sometimes failed to work on 8861

CSCvq89463 8845/8865 freezing randomly

CSCvt04909 The spam list can not be cleared after EM logout

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 8800 Series that uses
                        Firmware Release 12.7(1).

For more information about an individual defect, you can access the online record for the defect from the Bug Search Toolkit.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                        report was compiled. For an updated view of resolved defects or to view specific bugs, access the Bug Search Toolkit as described
                        in View Caveats .

CSCvb90559 Add option to enable or disable 88XX LED on Navigation button

CSCvg41896 Option to change the background color/image on a Cisco 8861 Expansion Module

CSCvn39109 88XX/78xx/7832/8832 not able to parse Call-Info huntpiloturi parameter

CSCvq10079 Phone can't connect to the network with new channel after change channel from wlc several times

CSCvq13251 Wrap the Pre-recording buffering solution inside "Customer Support Use" tag

CSCvq44854 DUT cannot get ip address after many times reboot by script

CSCvq75308 8851/8861 : With CME/BE4k MWI always shows 1 message regardless of number of messages

CSCvq80439 Cisco 8851 8861 IP Phone Key Negotiation of Bluetooth Vulnerability

CSCvr06323 CUCM Server1 and CUCM Server3 null values for Active Server

CSCvr19868 DTMF RFC 2833 differences between Cisco IP phone 8851 hardware version 8 and version below 8

CSCvr21699 8800 Display issue with CiscoIPPhoneText

CSCvr21736 Phone displays "???" when releasing a call

CSCvr21781 Unexpected audio tone played for call recording INVITE

CSCvr35161 PRT Status: uploading-failed when generatiing PRT via web access

CSCvr52021 CP 8832 allow user to access Phone Settings when Setting access is set to restricted

CSCvr56478 "Attempting VPN connection" banner on phone screen doesn't go away after VPN connection establishes

CSCvr56496 Call park number not displayed on phone screen after parking call in Enhanced Line Mode

CSCvr62841 MeetMe Conference list doesn't show the conference participants when registered with CME

CSCvr69093 Phone stuck in registering status due to Memory leak in sipstack

CSCvr96066 Cisco IP Phone Remote Code Execution and Denial of Service Vulnerability

CSCvr96069 Cisco IP Phone Remote Code Execution and Denial of Service Vulnerability

CSCvr96101 Cisco IP Phone CDP Broadcast Issue

CSCvs15211 Cisco IP Phone 88xx intermittently sent Model Number: 0 via CAST protocol

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

| Note | Some features may require the installation of a Cisco Unified Communications Manager Device Package. Failure to install the
                              Device Package before the phone firmware upgrade may render the phones unusable. |
|---|---|

| Connection Type | 8811 | 8841 | 8845 | 8851 | 8851NR | 8861 | 8865 | 8865NR |
|---|---|---|---|---|---|---|---|---|
| USB (dongle or USB-C cable) | Not supported | Not supported | Not supported | Supported | Supported | Supported | Supported | Supported |
| Bluetooth | Not supported | Not supported | Supported | Supported | Not supported | Supported | Supported | Not supported |

| Note | If your Unified CM doesn't have the required device pack to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phone 8800 Series . |
| Step 3 | Choose your phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.7(1) . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts: For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx-sip.12-7-1-0001-393.k3.cop.sgn For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65-sip.12-7-1-0001-393.k3.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 8 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phones 8800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.7(1) . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

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