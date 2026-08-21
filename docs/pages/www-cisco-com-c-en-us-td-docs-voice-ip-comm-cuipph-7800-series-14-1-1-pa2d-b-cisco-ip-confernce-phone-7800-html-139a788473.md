---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-14-1-1-pa2d-b-cisco-ip-confernce-phone-7800-html-139a788473
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/14-1-1/pa2d_b_cisco-ip-confernce-phone-7800.html
retrieved_at: 2026-08-21T13:23:33.926420+00:00
---

Cisco IP Phone 7800 Release Notes for Firmware Release 14.1(1)

# Cisco IP Phone 7800 Release Notes for Firmware Release 14.1(1)

First Published: November 19, 2021

# Cisco IP Phone 7800 Release Notes for Firmware Release 14.1(1)

These release notes support the Cisco IP Phones 7811, 7821, 7841, and 7861 running SIP Firmware Release 14.1(1).

The following table lists the support compatibility for the Cisco IP Phones.

Cisco IP Phone

Cisco Unified Communications Manager

Cisco IP Phones 7811, 7821, 7841, and 7861

Cisco Unified Communications Manager version 8.5(1) and later

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

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Phone 7800 Series.

### Cisco Unified
                     				Communications Manager Documentation

See the Cisco Unified
                              				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                           				Communications Manager release on the product support page.

## New and Changed Features

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

#### Configurable Delayed PLAR

Delayed Private Line Automatic Ringdown (PLAR) improves hotline calling by adding a timer to
                           				PLAR. A user now has up to 15 seconds to place a call before it is routed to a
                           				pre-configured phone number. This gives a user an additional option during an
                           				emergency.

The Off-hook to First Digit Timer parameter controls this
                           				feature. It's configurable from  0-15 seconds, but the default is 15 seconds. It's
                           				disabled by default.

The parameter is on Cisco Unified Communications Manager (Unified CM) . Navigate Device > Device Settings > SIP Profile .

##### Where to Find More Information

Feature Configuration Guide for Cisco Unified Communications
                                    							Manager (Release 14.0(1) or later)

#### MRA Support for Extension Mobility Login with Cisco Headsets

Mobile and Remote Access Through Expressway (MRA) now supports logging into Extension Mobility with the Cisco Headsets. To
                        implement this feature, you enable Headset-based Extension Mobility in Cisco Unified Communications Manager (Unified CM) for
                        your phone. Where to Find More Information

##### Where to Find More Information

#### Phone Migration without Transition Load

You can now migrate your enterprise phone to a multiplatform phone firmware in a single step without using transition firmware
                           load, and then obtain and authorize the migration license from the server.

##### Where to Find More Information

Cisco IP Phone 7800 and 8800 Series Migration Guide (On-Premises to Multiplatform Phones)

Convert between Enterprise Firmware and Multiplatform Firmware for Cisco IP Phone 7800 and 8800 Series

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified
                        				Communications Manager is running the latest device package. After you install a device package on the Cisco Unified
                        				Communications Manager servers in the cluster, you need to reboot all the servers.

If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly.

For information on the device packages, see the Cisco Unified
                        				Communications Manager Device Package Compatibility Matrix .

### Install the Firware Release on Cisco Unified Communications Manager

Before using the phone firmware release on the Cisco Unified Communications Manager, you must install the latest Cisco Unified
                        Communications Manager firmware on all Cisco Unified Communications Manager servers in the cluster.

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                        interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Go to the Software Download page for the Cisco IP Phone 7800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Release folder, choose 14.1(1) .

Select the firmware file, click the Download or Add to cart button, and follow the prompts.

The firmware filename is: cmterm-78xx.14-1-1-0001-136.k4.cop.sha512

If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All .

Click the + next to the firmware file name in the Download Cart section to access more information about this file.

Click the Readme link to open the installation instructions for the firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip files

If a Cisco Unified Communications Manager is not available to load the installer program, a zip file is available to load
                        the firmware.

Go to the Software Download page for the Cisco IP Phones 7800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 14.1(1) .

Select the firmware file, click the Downlod or Add to Cart button, and follow the prompts. The firmware file name is: cmterm-78xx.14-1-1-0001-136.zip

Unzip the files.

For more information about how to manually copy the firmware files to the server, see the Cisco Unified Communications Operating System Administration Guide

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

### Phone Data Migration Limitation for Cisco Unified
                     				Communications Manager Software Release 11.5SU8

The Phone Data Migration feature in Cisco Unified
                           				Communications Manager 11.5SU8 is not localized. Parameters and other items may not display in your
                        native language. The limitation does not apply to information displayed on the
                        phones.

Localization is complete for Cisco Unified
                           				Communications Manager Software Release 12.5(1)SU3 and later.

### Simplify Extension Mobility Login with Cisco Headsets Limitation

The text that displays on the phone for this feature has been localized. The text for the feature in Cisco Unified
                           				Communications Manager Software Release 11.5SU8 hasn't been localized. Localization of the text is complete in Cisco Unified
                           				Communications Manager Software Release 12.5(1)SU3 and later.

### Softkey Templates and Video Mode

## Caveats

### View Caveats

You can search for bugs using the Cisco Bug Search Tool.

Known caveats are graded according to severity level, and can be either open or resolved.

Before you begin

#### Before you begin

To view caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=14.1(1.*),14.1(1)&sb=anfr&svr=3nH&bt=custV

Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=14.1(1)&sb=afr&sts=open&svr=3nH&bt=custV

Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=14.1(1),14.1(1.*)&sb=fr&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search For field, then press Enter .

### Open Caveats

The following list contains a snapshot of the severity 1, 2, and 3 caveats that are open for the Cisco IP Phone 7800 Series
                        for Firmware Release 14.1(1).

For more information about an individual caveat, access the Bug Search Tool and search for the caveat using the bug ID number.
                        You must be a registered Cisco.com user to access this online information.

Because bug status continually changes, the list reflects a snapshot of the bugs that were open at the time this report was compiled. For an updated view of open caveats, access the Bug Search Tool as described
                        in View Caveats .

CSCvs26183 - 78xx phone aux port upgrade 56x without headset need 22mins

CSCwa12226 - Sometimes the DN will remain or disappear after login/logout the EMCC service.

### Resolved Caveats

The following list contains severity 1, 2, and 3 caveats that are resolved for the Cisco IP Phone 7800 Series for Firmware
                        Release 14.1(1).

For more information about an individual caveat, access the Bug Search Tool and search for the caveat using the bug ID number.
                        You must be a registered Cisco.com user to access this online information.

Because bug status continually changes, the list reflects a snapshot of the caveats that were open at the time this report
                        was compiled. For an updated view of resolved caveats, access the Bug Tool as described in View Caveats .

CSCvz73608 - 7800 phone can't dial out on speed dial list through headset/speaker hardkey or offhook handset

CSCvz54600 - not popup headset upgrade toast when phone register with 11.5.1 CUCM without headset template

CSCvy86009 - MRA login window has no softkey after enable activation code onboarding

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

| Cisco IP Phone | Cisco Unified Communications Manager |
|---|---|
| Cisco IP Phones 7811, 7821, 7841, and 7861 | Cisco Unified Communications Manager version 8.5(1) and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above |
| Cisco IP Phones 7811, 7821, 7841, and 7861 | CME 10.0 (IOS load 15.3(3)M) |
| Cisco IP Phones 7811, 7821, 7841, and 7861 | Cisco Expressway X8.7 or Cisco TelePresence Video Communication Server X8.7 (for Mobile and Remote Access) |

| Note | If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the Software Download page for the Cisco IP Phone 7800 Series . |
|---|---|
| Step 2 | Choose your phone model. |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | In the Latest Release folder, choose 14.1(1) . |
| Step 5 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. The firmware filename is: cmterm-78xx.14-1-1-0001-136.k4.cop.sha512 Note If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . | Note | If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . |
| Note | If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . |
| Step 6 | Click the + next to the firmware file name in the Download Cart section to access more information about this file. |
| Step 7 | Click the Readme link to open the installation instructions for the firmware. |
| Step 8 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . |
|---|---|

| Step 1 | Go to the Software Download page for the Cisco IP Phones 7800 Series . |
|---|---|
| Step 2 | Choose your phone model. |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | In the Latest Releases folder, choose 14.1(1) . |
| Step 5 | Select the firmware file, click the Downlod or Add to Cart button, and follow the prompts. The firmware file name is: cmterm-78xx.14-1-1-0001-136.zip |
| Step 6 | Unzip the files. |
| Step 7 | For more information about how to manually copy the firmware files to the server, see the Cisco Unified Communications Operating System Administration Guide |

| Caution | Do not connect the SW and PC ports into the LAN. |
|---|---|

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=14.1(1.*),14.1(1)&sb=anfr&svr=3nH&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=14.1(1)&sb=afr&sts=open&svr=3nH&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=14.1(1),14.1(1.*)&sb=fr&svr=3nH&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search For field, then press Enter . |

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