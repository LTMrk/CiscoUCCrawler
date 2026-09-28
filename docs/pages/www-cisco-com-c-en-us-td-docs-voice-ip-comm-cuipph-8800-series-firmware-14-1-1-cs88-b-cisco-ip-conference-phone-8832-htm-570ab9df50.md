---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-firmware-14-1-1-cs88-b-cisco-ip-conference-phone-8832-htm-570ab9df50
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/firmware/14-1-1/cs88_b_cisco-ip-conference-phone-8832.html
retrieved_at: 2026-08-21T13:28:14.007218+00:00
---

Cisco IP Conference Phone 8832 Release Notes for Firmware Release 14.1(1)

# Cisco IP Conference Phone 8832 Release Notes for Firmware Release 14.1(1)

First Published: November 19, 2021

# Cisco IP Conference Phone 8832 Release Notes for Firmware Release 14.1(1)

These release notes support the Cisco IP Conference Phone 8832 running SIP Firmware Release 14.1(1).

The following table lists the support compatibility for the Cisco IP Phones.

Cisco IP Phone

Support Requirements

8832

Cisco Unified Communications Manager 10.5(2) and later

Cisco Unified Communications Manager time zone update 2016d or later

SRST 8.0 (IOS load 15.1(1)T) and above

Cisco Expressway 8.7

8832

Unified CME 12.3 (Cisco IOS XE Fuji 16.9.1 release)

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Conference Phone 8832 Documentation

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Phone 7800 Series.

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

#### OAuth and Proxy TFTP Security Improvement

OAuth is now supported for Proxy Trivial File Transfer Protocol (TFTP). This feature keeps
                           				your phone secure during the registration process.

It requires Cisco Unified Communications Manager Release 14.0(1)SU1 or later.

OAuth Proxy TFTP is not supported for Mobile and Remote Access
                              				Through Expressway (MRA).

##### Where to Find More Information

Feature Configuration Guide for Cisco Unified Communications
                                    							Manager (Release 14.0(1) or later)

System Configuration Guide for Cisco Unified Communications Manager (Release 14.0(1) or later)

#### Improved Call Alert for Hunt Group

Hunt Group has been improved to make it easier to identify calls.

The Call Alert shows Caller ID (when Caller ID is configured), Directory Number and Hunt Group Pilot Number for the hunt group call. The hunt group number is displayed after the label Hunt Group .

##### Where to Find More Information

#### Expanded Speed Dial

It is easier to use the following call features because of the softkey Speed Dial :

Call transfer

Conference calls

Group pickup

When you perform one of above call features, you will be able to use a new softkey Speed Dial to go to the speed dial list window you need to dial out. Use the navigation ring to move within the window, and to select
                           your speed dial.

This feature doesn't require any configuration.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide

Cisco IP Phone 8800 Series User Guide

#### Phone Migration without Transition Load

You can now migrate your enterprise phone to a multiplatform phone firmware in a single step without using transition firmware
                           load, and then obtain and authorize the migration license from the server.

##### Where to Find More Information

Cisco IP Phone 7800 and 8800 Series Migration Guide (On-Premises to Multiplatform Phones)

Convert between Enterprise Firmware and Multiplatform Firmware for Cisco IP Phone 7800 and 8800 Series

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

### Install the Firmware Release on CUCM

Before using the phone firmware release on the Cisco Unified Communications Manager, you must install the latest Cisco Unified
                        Communications Manager firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the Software Download page for the Cisco IP Conference Phone 8832

Choose your phone model .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 14.1(1) .

Select the firmware file, click the Download or Add to cart button, and follow the prompts.

The firmware filename is cmterm-8832-sip.14-1-1-0001-125.k4.cop.sha512

If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All .

Click the + next to the firmware file name in the Download Cart section to access additional information about this file.

Click the Readme link to open the installation instructions for the firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, a zip file is available to load
                        the firmware.

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                        interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Go to the software download page for the IP Conference Phone 8832

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 14.1(1) .

Select the firmware file, click the Download Downlod or Add to Cart button, and follow the prompts.

The firmware filename is cmterm-8832.14-1-1-0001-125.zip

Unzip the files.

For information about how to manually copy the firmware files to the server, see the Cisco Unified Communications Operating System Administration Guide

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

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

### Phone Data Migration Limitation for Cisco Unified
                     				Communications Manager Software Release 11.5SU8

The Phone Data Migration feature in Cisco Unified
                           				Communications Manager 11.5SU8 is not localized. Parameters and other items may not display in your
                        native language. The limitation does not apply to information displayed on the
                        phones.

Localization is complete for Cisco Unified
                           				Communications Manager Software Release 12.5(1)SU3 and later.

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

Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.1(1),14.1(1.*)&sb=anfr&sts=fd&svr=3nH&bt=custV

Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.1(1)&sb=afr&sts=open&svr=3nH&bt=custV

Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.1(1),14.1(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional)  To look for information about a specific problem, enter the bug ID number in the Search for field, and press Enter .

### Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 8832 for Firmware
                        Release 14.1(1).

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in View Caveats .

CSCvq55980 - Network name still displayed ssid when no wifi radio available

### Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 8832 for Firmware
                        Release 14.1(1).

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in View Caveats .

CSCvy08413 HW version on 8832 web page is error

## Application Programming Interface

Cisco supports phone API utilization by 3rd party applications that have been tested and certified through Cisco by the 3rd
                     party application developer. Any phone issues related to uncertified application interaction must be addressed by the 3rd
                     party and will not be addressed by Cisco.

For support model of Cisco certified 3rd party applications/solutions, please refer to Cisco Solution Partner Program website for details.

## Cisco Unified Communication Manager Public Keys

To improve software integrity protection, public keys are used to sign cop files for Cisco Unified Communications Manager
                     Release 10.0.1 and later. These cop files have "k3 or k4" in their name. To install a k3 or k4 cop file on a pre-10.0.1 Cisco Unified Communications Manager, consult the README for
                     the ciscocm.version3-keys.cop.sgn to determine if you must install this additional cop file on your specific Cisco Unified
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

To access the Locale Installer required for a release, access the Software Download page, navigate to your phone model, and select the Unified Communications Manager Endpoints Locale Installer link.

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

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Cisco IP Phone | Support Requirements |
|---|---|
| 8832 | Cisco Unified Communications Manager 10.5(2) and later Cisco Unified Communications Manager time zone update 2016d or later SRST 8.0 (IOS load 15.1(1)T) and above Cisco Expressway 8.7 |
| 8832 | Unified CME 12.3 (Cisco IOS XE Fuji 16.9.1 release) |

| Warning | The Cisco IP Conference Phone 8832 PoE Injector is supported on phones running firmware release 12.0(1)SR2 and later. Confirm
                                    			 that the latest firmware release is installed on the Cisco Unified
                                    			 Communications Manager before you connect the Cisco IP Conference Phone 8832
                                    			 with the PoE injector to the network. If you are not
                                    			 using the latest firmware release, then your phone may downgrade to an earlier
                                    			 firmware release, and lose network connectivity. |
|---|---|

| Step 1 | Go to the Software Download page for the Cisco IP Conference Phone 8832 |
|---|---|
| Step 2 | Choose your phone model . |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | In the Latest Releases folder, choose 14.1(1) . |
| Step 5 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. The firmware filename is cmterm-8832-sip.14-1-1-0001-125.k4.cop.sha512 Note If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . | Note | If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . |
| Note | If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . |
| Step 6 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. |
| Step 7 | Click the Readme link to open the installation instructions for the firmware. |
| Step 8 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . |
|---|---|

| Step 1 | Go to the software download page for the IP Conference Phone 8832 |
|---|---|
| Step 2 | Choose your phone model. |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | In the Latest Releases folder, choose 14.1(1) . |
| Step 5 | Select the firmware file, click the Download Downlod or Add to Cart button, and follow the prompts. The firmware filename is cmterm-8832.14-1-1-0001-125.zip |
| Step 6 | Unzip the files. |
| Step 7 | For information about how to manually copy the firmware files to the server, see the Cisco Unified Communications Operating System Administration Guide |

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.1(1),14.1(1.*)&sb=anfr&sts=fd&svr=3nH&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.1(1)&sb=afr&sts=open&svr=3nH&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.1(1),14.1(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV |
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