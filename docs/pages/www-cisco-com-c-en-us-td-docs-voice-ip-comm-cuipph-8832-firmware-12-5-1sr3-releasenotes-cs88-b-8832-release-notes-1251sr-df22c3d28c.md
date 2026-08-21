---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8832-firmware-12-5-1sr3-releasenotes-cs88-b-8832-release-notes-1251sr-df22c3d28c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8832/firmware/12-5-1SR3/releasenotes/cs88_b_8832-release-notes-1251sr3.html
retrieved_at: 2026-08-21T13:28:47.962639+00:00
---

Cisco IP Conference Phone 8832 Release Notes for Firmware Release 12.5(1)SR3

# Cisco IP Conference Phone 8832 Release Notes for Firmware Release 12.5(1)SR3

### Download Options

Updated: June 6, 2019

First Published: June 6, 2019

# Cisco IP Conference Phone 8832 Release Notes for Firmware Release 12.5(1)SR3

These release notes support the Cisco IP Conference Phone 8832 running SIP Firmware Release 12.5(1)SR3.

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

## User Guide Accessibility

The Cisco IP Conference Phone 8832 User Guide is accessible for people with limited sight or who are blind. The HTML version of the document is now compatible with the
                     Job Access With Speech (JAWS) reader, so visually impaired users can access information about their phone.

### Where to Find More Information

Cisco IP Conference Phone 8832 User Guide

## New and Changed
               	 Features

The following sections describe the features that are new or have
                  		changed in this release.

### Features Available
                  	 with the Firmware Release

The following sections describe the features available with the Firmware
                     		Release.

#### Generate a Problem Report Tool Log from Cisco Unified Communications Manager

You can generate a Problem Report Tool (PRT) log for a phone from Cisco Unified Communications Manager Administration. This
                           allows you to collect the phone logs without generating a report from the phone. With this release, headset information is
                           also displayed in the log, which you can use for troubleshooting.

You generate the PRT log in Cisco Unified Communications Manager Administration with the Device > Phone page.

You need to add a server address to the Customer Support Upload URL field on Cisco Unified Communications Manager before you generate the PRT log.

This feature requires Cisco Unified Communications Manager 12.5(1)SU1 or later.

##### Where to Find More Information

Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

### Features Available
                  	 with the Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require
                     		the new firmware and the latest Cisco Unified Communications Manager Device
                     		Pack.

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

Cisco IP Conference Phone 8832 Administration Guide for Cisco Unified Communications Manager

Administration Guide for Cisco Unified Communications Manager and IM and Presence Service, Release 12.0(1) or later

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

In the Latest Releases folder, choose 12.5(1)SR3 .

Select the firmware file, click the Download or Add to cart button, and follow the prompts.

The firmware filename is cmterm-8832-sip.12-5-1SR3-74.k3.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following .zip file is available
                        to load the firmware:

cmterm-8832.12-5-1SR3-74.zip

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                        interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose IP Conference Phone 8832 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.5(1)SR3 .

Download the relevant zip files.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server.

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

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286317183&rls=12.5(1)SR3&sb=anfr&svr=3nH&bt=custV

To find all open caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286317183&rls=12.5(1)SR3&sb=afr&svr=3nH&bt=custV

To find all resolved caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286317183&rls=12.5(1)SR3&sb=fr&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional)  To look for information about a specific problem, enter the bug ID number in the Search for field, and press Enter .

### Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 8832 for Firmware
                        Release 12.5(1)SR3.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in View Caveats .

CSCvp76317: Display error while wifi connection using 64 characters username and password

CSCvp78786: Vulnerabilities in wlan firmware: EAPOL M3 Embedded GTK : double buffer overflow

### Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 8832 for Firmware
                        Release 12.5(1)SR3.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                        report was compiled. For an updated view of closed defects, access Bug Toolkit as described in View Caveats .

CSCvp46558: Linux Kernel Stale TLB Entry Unauthorized Access Vulnerability

CSCvp66155: 8832: Wireless Mic lost connection after phone power cycle.

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

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| 8832 | SIP | Cisco Unified Communications Manager 10.5(2) and later Cisco Unified Communications Manager time zone update 2016d or later SRST 8.0 (IOS load 15.1(1)T) and above Cisco Expressway 8.7 |
| 8832 | SIP | Unified CME 12.3 (Cisco IOS XE Fuji 16.9.1 release) |

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
| Step 4 | In the Latest Releases folder, choose 12.5(1)SR3 . |
| Step 5 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. The firmware filename is cmterm-8832-sip.12-5-1SR3-74.k3.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
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
| Step 4 | In the Latest Releases folder, choose 12.5(1)SR3 . |
| Step 5 | Download the relevant zip files. |
| Step 6 | Unzip the files. |
| Step 7 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

| Step 1 | Perform one of the following actions: To find all caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286317183&rls=12.5(1)SR3&sb=anfr&svr=3nH&bt=custV To find all open caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286317183&rls=12.5(1)SR3&sb=afr&svr=3nH&bt=custV To find all resolved caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286317183&rls=12.5(1)SR3&sb=fr&svr=3nH&bt=custV |
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