---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-firmware-12-5-1sr3-releasenotes-pa2d-b-7800-release-notes-83fa028fc1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/firmware/12-5-1SR3/releasenotes/pa2d_b_7800-release-notes-1251sr3.html
retrieved_at: 2026-08-21T13:24:11.553693+00:00
---

Cisco IP Phone 7800 Series Release Notes for Firmware Release 12.5(1)SR3

# Cisco IP Phone 7800 Series Release Notes for Firmware Release 12.5(1)SR3

### Download Options

Updated: June 3, 2019

First Published: June 6, 2019

Last Updated: February 10, 2021

# Cisco IP Phone 7800 Series Release Notes for Firmware Release 12.5(1)SR3

These release notes support the Cisco IP Phones 7811, 7821, 7841, and 7861 running SIP Firmware Release 12.5(1)SR3.

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

## User Guide Accessibility

The Cisco IP Phone 7800 Series User Guide is accessible for people with limited sight or who are blind. The HTML version of the document is now compatible with the
                     Job Access With Speech (JAWS) reader, so visually impaired users can access information about their phone.

### Where to Find More Information

Cisco IP Phone 7800 Series User Guide

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

#### Cisco Headset Management

You can manage and control your Cisco headsets from a central location on Cisco Unified Communications Manager Administration.
                           You can:

Apply customized settings and control default templates

Track deployed headsets and to generate inventory reports

You manage the headsets in Cisco Unified Communications Manager Administration with the Device > Headsets page.

This feature requires Cisco Unified Communications Manager 12.5(1)SU1 or later, and Cisco Headset 500 Series Firmware Release
                           1.5(0) or later to function.

##### Where to Find More Information

Administration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU1

Cisco Headset 500 Series Administration Guide

#### Reset Headset Settings

Users can reset their Cisco Headset 530 Series or Cisco Headset 560 Series headset settings to remove their customizations.
                           The headsets take the settings configured in the user's headset profile, as described in Cisco Headset Management .

The headset must be connected to the phone (USB connector for the Cisco Headset 530; USB connector or Y-cable to the Cisco
                           Headset 560 Standard Base or Multibase). To reset the settings, the user presses Applications and selects Settings > Accessories > Setup > Reset settings .

##### Where to Find More Information

Cisco IP Phone 7800 Series User Guide

Cisco IP Phone 7800 and 8800 Series Accessories Guide

#### Generate a Problem Report Tool Log from Cisco Unified Communications Manager

You can generate a Problem Report Tool (PRT) log for a phone from Cisco Unified Communications Manager Administration. This
                           allows you to collect the phone logs without generating a report from the phone. With this release, headset information is
                           also displayed in the log, which you can use for troubleshooting.

You generate the PRT log in Cisco Unified Communications Manager Administration with the Device > Phone page.

You need to add a server address to the Customer Support Upload URL field on Cisco Unified Communications Manager before you generate the PRT log.

This feature requires Cisco Unified Communications Manager 12.5(1)SU1 or later.

##### Where to Find More Information

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

### Features Available
                  	 with the Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require the new firmware and the
                     			latest Cisco Unified Communications Manager Device Pack. The applicable device packs are
                     			released after the firmware release.

For information about the Cisco Unified IP Phones and the required Cisco
                     		Unified Communications Manager device packs, see the following URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html

#### Activation Code Onboarding for Mobile and Remote Access

You can use Activation Code Onboarding with Mobile and Remote Access when you deploy Cisco IP Phones for off-premises users.
                           This feature is a secure way to deploy off-premises phones when autoregistration is not required. But you can also configure
                           a phone for autoregistration when on-premises, and activation codes when off-premises.

This feature extends the on-premises Activation Code Onboarding feature to off-premises phones.

Activation Code Onboarding for Mobile and Remote Access requires the following to function:

Smart Licensing

Cisco Expressway X12.5 or later.

Cisco Unified Communications Manager 12.5(1)SU1 or later

To enable this feature, you select Allow Activation Code via MRA and Require Activation Code for Onboarding in the Device Information section of the Phone Configuration page.

##### Where to Find More Information

Cisco IP Phone 7800 Series Administration Guide for Cisco Unified Communications Manager

Administration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 12.0(1) or later

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

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

In the Latest Releases folder, choose 12.5(1)SR3 .

Select the firmware file, click the Download or Add to cart button, and follow the prompts.

The firmware filename is cmterm-78xx.12-5-1SR3-74.k3.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following zip files are available
                        to load the firmware.

cmterm-78xx.12-5-1SR3-74.zip

Go to the following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Choose Cisco IP Phones 7800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.5(1)SR3 .

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

Use this URL for all caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.5(1)SR3&sb=anfr&svr=3nH&bt=custV

Use this URL for all open caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.5(1)SR3&sb=afr&svr=3nH&bt=custV

Use this URL for all resolved caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.5(1)SR3&sb=fr&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco IP Phone 7800 Series for Firmware Release
                        12.5(1)SR3.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access the Bug Toolkit as described in View Caveats .

CSCvp76009: The Missed call UI disappears and displays blank

### Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series for Firmware
                        Release 12.5(1)SR3.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of resolved defects, access the Bug Toolkit as described in View Caveats .

CSCvj80263: Sometimes the Phone will register back to vCluster after reset all on phone in hCluster

CSCvm44063: Phone unresponsive/frozen when connected to a laptop with CUVA setup

CSCvo88584: Multiple Vulnerabilities in glibc

CSCvp69871: 78xx media server may crash when sending buffered pre recording packets

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

| Cisco IP Phone | Protocol | Cisco Unified Communications Manager |
|---|---|---|
| Cisco IP Phones 7811, 7821, 7841, and 7861 | SIP | Cisco Unified Communications Manager version 8.5(1) and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above |
| Cisco IP Phones 7811, 7821, 7841, and 7861 | SIP | CME 10.0 (IOS load 15.3(3)M) |
| Cisco IP Phones 7811, 7821, 7841, and 7861 |  | Cisco Expressway X8.7 or Cisco TelePresence Video Communication Server X8.7 (for Mobile and Remote Access) |

| Note | Some features may require the installation of a Cisco Unified Communications Manager Device Package. Failure to install the
                              Device Package before the phone firmware upgrade may render the phones unusable. |
|---|---|

| Note | If your Unified CM doesn't have the required device pack to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phone 7800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.5(1)SR3 . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. The firmware filename is cmterm-78xx.12-5-1SR3-74.k3.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
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
| Step 5 | In the Latest Releases folder, choose 12.5(1)SR3 . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

| Caution | Do not connect the SW and PC ports into the LAN. |
|---|---|

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.5(1)SR3&sb=anfr&svr=3nH&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.5(1)SR3&sb=afr&svr=3nH&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.5(1)SR3&sb=fr&svr=3nH&bt=custV |
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