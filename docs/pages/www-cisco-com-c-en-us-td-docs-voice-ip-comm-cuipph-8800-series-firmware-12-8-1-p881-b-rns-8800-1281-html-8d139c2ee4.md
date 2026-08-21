---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8800-series-firmware-12-8-1-p881-b-rns-8800-1281-html-8d139c2ee4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8800-series/firmware/12-8-1/p881_b_rns-8800-1281.html
retrieved_at: 2026-08-21T13:29:50.845934+00:00
---

Cisco IP Phone 8800 Series Release Notes for Firmware Release 12.8(1)

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 12.8(1)

### Download Options

Updated: April 24, 2020

First Published: April 30, 2020

Last Updated: February 10, 2021

# Cisco IP Phone 8800 Series Release Notes for Firmware Release 12.8(1)

These release notes support the Cisco IP Phone 8811, 8841, 8845, 8851, 8851NR, 8861, 8865, and 8865NR running SIP Firmware
                  Release 12.8(1).

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

#### Headset Integration with Cisco Unified Contact Center

This feature is a demonstration feature for Cisco Contact Center. It allows customers to test and evaluate the feature, but
                                          we do not recommend that you use it in a production environment. Cisco TAC support is limited to best effort support. For
                                          more information, see the Contact Center white paper.

##### Where to Find More Information

https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cucm/whitePaper/CUCM_Headsets_for_ContactCenter_WP.pdf

#### Headset Update Enhancement

You can see the headset firmware update source on the phone web page. The information displays on the Device Information page.

This feature has no user impact.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide

#### Phone Data Migration

If you need to replace a user's phone, you can easily migrate the old phone configuration to the new phone. To support this
                           feature, you need new phones that run Firmware Release 12.8(1).

The change may be required for a number of reasons, for example:

You have updated your Cisco Unified
                                    				Communications Manager ( Unified CM ) to a software version that doesn't support the phone model. In this case, the user needs a new, supported phone.

The phone requires repair or replacement with the same phone model.

To migrate the phone, the old phone must be powered off. You power on the new phone, and receive a prompt to either replace
                           an existing phone or provision a new phone. If you select the option to replace an existing phone, the phone prompts you for
                           the extension number of the old phone (and PIN, if required). The phone contacts the Unified CM and the old phone configuration is copied into the configuration record for the new phone.

This feature supports migration of SIP and SCCP phones.

This feature requires Unified CM Release 11.5SU8 or later, or Release 12.5SU3 or later. The feature requires configuration of new fields in the Enterprise Parameters Configuration administration page. The feature also requires that the Unified CM administrator disable phone autoconfiguration.

Migration to a model in the Cisco IP Phone 8800 Series results in a phone in Session Line Mode.

If the old phone has a key expansion model configured, the Unified CM copies the expansion module information to the new phone at the same time. When the user connects a compatible key expansion
                           module to the new phone, the new expansion module gets the migrated expansion module information.

If the old phone has a key expansion model configured and the new phone doesn't support an expansion module, the Unified CM doesn't copy the expansion module information.

##### Limitations for Lines and Line Keys

If the old phone has more lines or more line buttons than the new phone supports, only the supported number of lines or line
                           buttons are migrated.

For example:

Scenario: The old phone had 4 line buttons and the new phone has 2 line buttons

Migration result: The new phone has the line buttons set up like the first 2 line buttons on the old phone.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide

Feature Configuration Guide for Cisco Unified Communications
                                    Manager , Release 12.5(1)SU3 or later

#### Simplify Extension Mobility Login with Cisco Headsets

Your Extension Mobility users can easily start their sign in to Extension Mobility when they plug their Cisco Headset 500 Series or Cisco Headset 730 into someone else's phone. To support this, you need to enable the Headset-based Extension Mobility field in Cisco Unified
                              				Communications Manager for your phones.

The Cisco Headset 500 Series needs to connect to the phone with the USB or Y-cable, or be paired and connected to the phone through the Cisco Headset 560 Series Standard Base or Cisco Headset 560 Series Multibase .

The Cisco Headset 730 needs to connect to the phone with the USB cable. The Cisco Headset 730 USB dongle is not supported.

When the user connects the headset into a phone, the phone checks with Cisco Unified
                              				Communications Manager ( Unified CM ) to discover if the headset serial number is mapped to a user.

If the mapping exists, the phone displays the Extension Mobility screen and displays the user ID associated with the headset.
                                 The user enters their PIN to sign in.

If the mapping doesn't exist, the user sees a headset association page and enters their user ID and PIN. The phone relays
                                 the headset serial number to the Unified CM , which maps the headset to the user. Then the Extension Mobility sign-in screen displays. The user changes the user ID to
                                 their user ID and and enters their PIN.

The next time the user plugs their headset into a phone, the Unified CM finds the user ID, based on the headset serial number.

With Unified CM Software Release 12.5(1)SU3, you can disable the requirement for the PIN input when the headset is register to a user.

The user automatically signs out of Extension Mobility when they unplug the headset or after a predetermined inactivity time.

The user can also be signed out automatically if the Cisco Headset 560 Series is taken too far from the base. In this case, if the headset reconnects with the base before the inactivity timer expires,
                           the user doesn't need to sign in again.

Users can associate their headset with their user ID from the Accessories menu on the phone

Administrators can associate the headset with a user in Unified CM from the User  Management page.

This feature requires:

Unified CM :

Software Release 11.5(1)SU8 or later

Software Release 12.5(1)SU3 or later

The feature requires configuration of new fields in the Service Parameter Configuration administration page. the feature also needs the Cisco Headset Service to be active on the Unified CM .

If the headset is upgrading or the user is on a call, the association can't be made. The user must wait until the upgrade
                                       is finished or the call is finished before they perform this procedure.

Mobile and Remote Access doesn't support this feature..

##### Where to Find More Information

Cisco IP Phone 8800 Series User Guide

Feature Configuration Guide for Cisco Unified Communications Manager

#### Wallpaper Enhancement

With this release, we improved the font color selection algorithm for custom wallpapers.
                           				Custom wallpaper users may see changes to the font colors on the phone screen.

If you use custom wallpapers, follow the recommendations in the Customized
                              					Wallpapers Best Practices Cisco IP Phone 8800 Series .

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide

Customized Wallpapers Best Practices Cisco IP Phone 8800 Series https://www.cisco.com/c/dam/en/us/products/collateral/collaboration-endpoints/unified-ip-phone-8800-series/white-paper-c11-740036.pdf

### Features Available
                  	 with the Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require the new firmware and the
                     			latest Cisco Unified Communications Manager Device Pack. The applicable device packs are
                     			released after the firmware release.

For information about the Cisco Unified IP Phones and the required Cisco
                     		Unified Communications Manager device packs, see the following URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html

#### Feature Control Changes

You can control the Lower your voice and the Mark call as spam features for your users in the Cisco Unified Communication
                           Manager (Unified CM) Administration pages. By default, the features are disabled, but you can enable them for one, some, or
                           all users.

You control the features in the Product Specific Configuration Layout area, for example, in Device > Phones .

Lower your voice alert field: By default, the field is set to Disabled .

When the field is disabled:

The phone doesn't display the Lower your voice menu item in the Settings menu.

Users won't see the message on their screen when they speak loudly.

When the  field is enabled,

Users control the feature from the Lower your voice menu item in the Settings menu. By default, this field is set to On .

Mark call as spam field: By default, the field is set to Disabled .

When the field is disabled:

The phone doesn't display the Mark spam softkey.

The Spam list item in the Settings menu doesn't display.

If there are spam call records for the phone, the records are cleared and can't be recovered. This means that any number previously
                                             identified as spam will ring on the phone.

When the field is enabled,

The phone displays the Mark spam softkey.

The Spam list item in the Settings menu displays. The spam list is empty.

##### Where to Find More Information

Cisco IP Phone 8800 Series Administration Guide

Cisco IP Phone 8800 Series User Guide

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

In the Latest Releases folder, choose 12.8(1) .

Select the firmware file, click the Download or Add to cart button, and follow the prompts:

For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx-sip.12-8-1-0001-455.k3.cop.sgn

For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65-sip.12-8-1-0001-455.k3.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following .zip files are available
                        to load the firmware:

For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx.12-8-1-0001-455.zip

For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65.12-8-1-0001-455.zip

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                        interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco IP Phones 8800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.8(1) .

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

## Caveats

### Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco IP Phone 8800 Series for Firmware Release
                        128(1).

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in View Caveats .

CSCvo74172 8861 phone should not roaming from WLC with Platinum QOS to WLC with Silver QOS

CSCvp34626 No wifi icon displayed at the upper right corner of LCD after wifi connection done

CSCvq21512 8861 deregister when running JFW roaming about 3 hours(EAP-TLS with WPA2+ 11r over the DS)

CSCvq32455 8845_65 ip phone reset/restart intermittently after disconnect of a call

CSCvq37245 Active server shows empty under phone information page in ipv6 only mode

CSCvq59064 802.11r fast transition sometimes failed to work on 8861

CSCvq89463 8845/8865 freezing randomly

CSCvt18121 8865 Phones video freezing on CMS in side-by-side view

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 8800 Series that uses
                        Firmware Release 12.8(1).

For more information about an individual defect, you can access the online record for the defect from the Bug Search Toolkit.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                        report was compiled. For an updated view of resolved defects or to view specific bugs, access the Bug Search Toolkit as described
                        in View Caveats .

CSCuy32083 Change the way 88xx series phone park a call

CSCvn86806 Remove the usb2 cable from mac will cause IP phone popup remove toast

CSCvo71625 Sometimes the phone screen doesn't display the last digit of the phone number

CSCvs73770 Different beeping behavior on receiving a call with APU-76 headset and shared line

CSCvs75879 Cisco 88xx Phones show lag/slowness when dialing out an extension

CSCvs91971 CVE-2016-9843: zlib crc32_big Function Numeric Errors Vulnerability

CSCvs95092 Multiple Vulnerabilities in Qt

CSCvs95116 8861/8865 is not reconnecting to Aruba AP after network outage

CSCvs98676 88xx phones are not displaying the speed-dials when pressing the navigation button down

CSCvt04894 – Disable 'Lower Your Voice Alert' feature by default in CP-88xx

CSCvt11376 8861 HW Rev V15 and above unable to connect to VPN

CSCvt14542 88xx: CLIB is not displayed in enhanced line mode in firmware version 12.7

CSCvt16645 Disable 'Spam Call' feature in CP-88xx

CSCvt31520 88xx DMAN crash

CSCvt37331 8865/8845 Black screen in the beginning of video call

CSCvt45473 8861 HW Rev V15 and above unable to do Jabber deskphone video

CSCvt47267 88XX intermittently crashing retrieving a call placed on hold by another device

CSCvt55471 8865 unable to register when use a custom background

CSCvt64703 8861 FW 12.7.1 Wireless (Wi-Fi) Phone VPN Not Registering

### View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Perform one of the following actions:

Use this URL for all caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.8(1),12.8(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV

Use this URL for all open caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.8(1)&sb=afr&sts=open&svr=3nH&bt=custV

Use this URL for all resolved caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.8(1),12.8(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

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

| Note | This feature is a demonstration feature for Cisco Contact Center. It allows customers to test and evaluate the feature, but
                                          we do not recommend that you use it in a production environment. Cisco TAC support is limited to best effort support. For
                                          more information, see the Contact Center white paper. |
|---|---|

| Note | With Unified CM Software Release 12.5(1)SU3, you can disable the requirement for the PIN input when the headset is register to a user. |
|---|---|

| Note | If the headset is upgrading or the user is on a call, the association can't be made. The user must wait until the upgrade
                                       is finished or the call is finished before they perform this procedure. |
|---|---|

| Note | If your Unified CM doesn't have the required device pack to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phone 8800 Series . |
| Step 3 | Choose your phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.8(1) . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts: For Cisco IP Phone 8811, 8841, 8851, 8851NR, and 8861—cmterm-88xx-sip.12-8-1-0001-455.k3.cop.sgn For Cisco IP Phone 8845, 8865, and 8865NR—cmterm-8845_65-sip.12-8-1-0001-455.k3.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
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
| Step 5 | In the Latest Releases folder, choose 12.8(1) . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.8(1),12.8(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.8(1)&sb=afr&sts=open&svr=3nH&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284729655&rls=12.8(1),12.8(1.*)&sb=fr&sts=fd&svr=3nH&bt=custV |
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