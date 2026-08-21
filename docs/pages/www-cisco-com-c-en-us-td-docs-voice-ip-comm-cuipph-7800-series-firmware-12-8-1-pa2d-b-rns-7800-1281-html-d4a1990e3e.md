---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-firmware-12-8-1-pa2d-b-rns-7800-1281-html-d4a1990e3e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/firmware/12-8-1/pa2d_b_rns-7800-1281.html
retrieved_at: 2026-08-21T13:23:54.597137+00:00
---

Cisco IP Phone 7800 Series Release Notes for Firmware Release 12.8(1)

# Cisco IP Phone 7800 Series Release Notes for Firmware Release 12.8(1)

### Download Options

Updated: April 24, 2020

First Published: April 30, 2020

Last Updated: February 10, 2021

# Cisco IP Phone 7800 Series Release Notes for Firmware Release 12.8(1)

These release notes support the Cisco IP Phones 7811, 7821, 7841, and 7861 running SIP Firmware Release 12.8(1).

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

Refer to publications that are specific to your language, phone model, and call control system. Navigate from the following
                        documentation URL:

https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-7800-series/index.html

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

Cisco IP Phone 7800 Series Administration Guide

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

If the old phone has a key expansion model configured and the new phone doesn't support an expansion module, the Unified CM doesn't copy the expansion module information.

##### Limitations for Lines and Line Keys

If the old phone has more lines or more line buttons than the new phone supports, only the supported number of lines or line
                           buttons are migrated.

For example:

Scenario: The old phone had 4 line buttons and the new phone has 2 line buttons

Migration result: The new phone has the line buttons set up like the first 2 line buttons on the old phone.

##### Where to Find More Information

Cisco IP Phone 7800 Series Administration Guide

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

Cisco IP Phone 7800 Series User Guide

Feature Configuration Guide for Cisco Unified Communications Manager

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

In the Latest Releases folder, choose 12.8(1) .

Select the firmware file, click the Download or Add to cart button, and follow the prompts.

The firmware filename is cmterm-78xx.12-8-1-0001-455.k3.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following zip file is available
                        to load the firmware:

cmterm-78xx.12-8-1-0001-455.zip

Go to the following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Choose Cisco IP Phones 7800 Series .

Choose your phone model.

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.8(1) .

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
                        				templates for Video mode on the Cisco IP Phone 7800 Series phones. If a softkey
                        				appears on the phone, then it will not function correctly.

## Caveats

### Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco IP Phone 7800 Series for Firmware Release
                        12.8(1).

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access the Bug Toolkit as described in View Caveats .

CSCvs26183 - 78xx phone aux port upgrade 56x without headset need 22mins

### Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series for Firmware
                        Release 12.8(1).

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of resolved defects, access the Bug Toolkit as described in View Caveats .

CSCvs76940 - libxml2 xmlParseBalancedChunkMemoryRecover Memory Leak Vulnerability

CSCvt19392 - 78xx/88xx phones not playing local ring back when 180 w/o SDP & non g.711u early

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

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.8(1.*),12.8(1)&sb=anfr&svr=3nH&bt=custV

Use this URL for all open caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.8(1)&sb=afr&sts=open&svr=3nH&bt=custV

Use this URL for all resolved caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.8(1.*),12.8(1)&sb=anfr&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

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

| Cisco IP Phone | Cisco Unified Communications Manager |
|---|---|
| Cisco IP Phones 7811, 7821, 7841, and 7861 | Cisco Unified Communications Manager version 8.5(1) and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above |
| Cisco IP Phones 7811, 7821, 7841, and 7861 | CME 10.0 (IOS load 15.3(3)M) |
| Cisco IP Phones 7811, 7821, 7841, and 7861 | Cisco Expressway X8.7 or Cisco TelePresence Video Communication Server X8.7 (for Mobile and Remote Access) |

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

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phone 7800 Series . |
| Step 3 | Choose your phone model. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.8(1) . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. The firmware filename is cmterm-78xx.12-8-1-0001-455.k3.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
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
| Step 5 | In the Latest Releases folder, choose 12.8(1) . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

| Caution | Do not connect the SW and PC ports into the LAN. |
|---|---|

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.8(1.*),12.8(1)&sb=anfr&svr=3nH&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.8(1)&sb=afr&sts=open&svr=3nH&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.8(1.*),12.8(1)&sb=anfr&svr=3nH&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |

| Note | The latest
                                 			 Locale Installer may not be immediately available; continue to check the
                                 			 website for updates. |
|---|---|