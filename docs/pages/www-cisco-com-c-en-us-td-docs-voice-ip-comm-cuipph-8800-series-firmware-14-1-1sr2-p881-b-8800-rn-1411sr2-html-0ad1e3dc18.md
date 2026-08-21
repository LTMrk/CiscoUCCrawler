---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-firmware-14-1-1sr2-p881-b-8800-rn-1411sr2-html-0ad1e3dc18
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/firmware/14-1-1sr2/p881_b_8800-rn-1411sr2.html
retrieved_at: 2026-08-21T13:29:29.859905+00:00
---

Cisco IP Phone 8800 Release Notes for Firmware Release 14.1(1)SR2

# Cisco IP Phone 8800 Release Notes for Firmware Release 14.1(1)SR2

### Download Options

Updated: October 31, 2022

First Published: October 31, 2022

# Cisco IP Phone 8800 Release Notes for Firmware Release 14.1(1)SR2

These release notes support the Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR running SIP Firmware
                  Release 14.1(1)SR2.

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

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Phone 8800 Series.

### Cisco Unified
                     				Communications Manager Documentation

See the Cisco Unified
                              				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                           				Communications Manager release on the product support page.

## Features Available with the Firmware Release

The following section describes the feature available with the Firmware Release.

### Improved Call History for Hunt Group

The call history on the phone screen has been improved to identify the calls.

The call history shows Caller ID (if configured), directory number, hunt group name (if configured), and hunt group number.
                        The hunt group name or number, or both, are displayed after the label Hunt group: .

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

Go to the Software Download page for the Cisco IP Phone 8800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Release folder, choose 14.1(1)SR2 .

Select the firmware file, click the Download or Add to cart button, and follow the prompts:

The firmware filename is cmterm-8845_65-sip.14-1-1-0211-134.k4.cop.sha512 or cmterm-88xx-sip.14-1-1-0211-134.k4.cop.sha512,
                                    depending on the model you choose.

If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All .

Click the + next to the firmware file name in the Download Cart section to access more information about this file.

Click the Readme link to open the installation instructions for the firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following .zip files are available
                        to load the firmware: cmterm-8845_65.14-1-1-0211-134.zip or cmterm-88xx.14-1-1-0211-134.zip.

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                        interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Go to the Software Download page for the Cisco IP Phones 8800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 14.1(1)SR2 .

Select the firmware file, click the Downlod or Add to Cart button, and follow the prompts.

The firmware file name is cmterm-8845_65.14-1-1-0211-134.zip or cmterm-88xx.14-1-1-0211-134.zip, depending on the model you
                                    choose.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server.

For more information about how to manually copy the firmware files to the server, see the Cisco Unified Communications Operating System Administration Guide .

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and video quality, and in some cases, can cause a call to
                        drop. Sources of network degradation can include, but are not limited to, the following activities:

Anything that degrades network performance can affect phone audio and, in some cases, can cause a call to drop. Sources of
                        network degradation can include, but are not limited to, the following activities:

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

You can't configure softkey
                        				templates for Video mode on the Cisco IP Phone 8800 Series phones. If a softkey
                        				appears on the phone, then it will not function correctly.

Caveats

## View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Perform one of the following actions:

Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.1(1),14.1(1.*)&sb=anfr&sts=fd&svr=3nH&bt=custV

Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.1(1)&sb=afr&sts=open&svr=3nH&bt=custV

Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.1(1),14.1(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

## Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco IP Phone 8800 Series for Firmware Release
                     14.1(1)SR2.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                     You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                     was compiled. For an updated view of open defects, access Bug Toolkit as described in View Caveats .

CSCvo74172 - 8861 phone should not roaming from WLC with Platinum QOS to WLC with Silver QOS

CSCvp34626 - No wifi icon displayed at the upper right corner of LCD after wifi connection done

CSCvq21512 - 8861 deregister when running JFW roaming about 3 hours(EAP-TLS with WPA2+ 11r over the DS)

CSCvq32455 - 8845_65 ip phone reset/restart intermittently after disconnect of a call

CSCvq37245 - Active server shows empty under phone information page in ipv6 only mode

CSCvq59064 - 802.11r fast transition sometimes failed to work on 8861

CSCvq89463 - 8845/8865 freezing randomly

CSCvt18121 - 8865 Phones video freezing on CMS in side-by-side view

CSCwa00308 - fail to reject second incoming call on cisco 530 headset

## Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 8800 Series that uses
                     Firmware Release 14.1(1)SR2.

For more information about an individual defect, you can access the online record for the defect from the Bug Search Toolkit.
                     You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                     report was compiled. For an updated view of resolved defects or to view specific bugs, access the Bug Search Toolkit as described
                     in View Caveats .

CSCwa37034 Unable to push a new SSID and PSK via Wireless Device Profiles on CP-8832

CSCwa38238 88xx model desk phones fail to cast video to Jabber

CSCwa44341 Headset stuck in downgrade state which prevent EM touchless login to be triggered

CSCwa21996 8865 Video Freeze due to high H.264 encoding bitrate

CSCwa92403 During DHCP Server migration, phones fail to rebind to the new DHCP Server

CSCwa68850 "Show cisco headset info" command is not working in 14-1-1 Phone release

CSCwb74332 IP Phones with Speaker Disabled are able to setup call from Speed Dial

CSCwb97182 Cisco 8851 phone recording fails via analog adapter

CSCwb72019 Remote Party number is displayed twice in the call history for hunt calls

CSCwb48865 Automatic Login to Extension with Touchless EM feature when Headset is disconnected

CSCwc69646  Wi-Fi passwd is printed in phone log when bootup

CSCwc89076 88x1 handset sidetone gain

CSCwc78427  Secure data partition is world readable and writable

CSCwc34935 8851 Buzzing / Wind sound when using Speaker (V18 units)

CSCwd04973 8865 phone can't connect to AP with EAP-TLS + MIC as User Cert

CSCwd30417 88xx cannot initiate plus dialing when Simplified Call UI and enhanced line mode are both enabled

CSCwd20381 CP-8861 wlan profile is removed after WLAN disconnected and reconnected

## Application Programming Interface

Cisco supports phone API utilization by 3rd party applications that have been tested and certified through Cisco by the 3rd
                     party application developer. Any phone issues related to uncertified application interaction must be addressed by the 3rd
                     party and will not be addressed by Cisco.

For support model of Cisco certified 3rd party applications/solutions, please refer to Cisco Solution Partner Program website for details.

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

| Note | If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the Software Download page for the Cisco IP Phone 8800 Series . |
|---|---|
| Step 2 | Choose your phone model. |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | In the Latest Release folder, choose 14.1(1)SR2 . |
| Step 5 | Select the firmware file, click the Download or Add to cart button, and follow the prompts: The firmware filename is cmterm-8845_65-sip.14-1-1-0211-134.k4.cop.sha512 or cmterm-88xx-sip.14-1-1-0211-134.k4.cop.sha512,
                                    depending on the model you choose. Note If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . | Note | If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . |
| Note | If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . |
| Step 6 | Click the + next to the firmware file name in the Download Cart section to access more information about this file. |
| Step 7 | Click the Readme link to open the installation instructions for the firmware. |
| Step 8 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added firmware to the cart, when you are ready to download the files, click the Cart and then click Download All . |
|---|---|

| Step 1 | Go to the Software Download page for the Cisco IP Phones 8800 Series . |
|---|---|
| Step 2 | Choose your phone model. |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | In the Latest Releases folder, choose 14.1(1)SR2 . |
| Step 5 | Select the firmware file, click the Downlod or Add to Cart button, and follow the prompts. The firmware file name is cmterm-8845_65.14-1-1-0211-134.zip or cmterm-88xx.14-1-1-0211-134.zip, depending on the model you
                                    choose. |
| Step 6 | Unzip the files. |
| Step 7 | Manually copy the unzipped files to the directory on the TFTP server. For more information about how to manually copy the firmware files to the server, see the Cisco Unified Communications Operating System Administration Guide . |

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.1(1),14.1(1.*)&sb=anfr&sts=fd&svr=3nH&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.1(1)&sb=afr&sts=open&svr=3nH&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=14.1(1),14.1(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV |
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