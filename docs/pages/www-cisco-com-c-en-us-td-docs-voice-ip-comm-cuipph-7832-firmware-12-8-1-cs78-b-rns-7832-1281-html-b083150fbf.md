---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7832-firmware-12-8-1-cs78-b-rns-7832-1281-html-b083150fbf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7832/firmware/12-8-1/cs78_b_rns-7832-1281.html
retrieved_at: 2026-08-21T13:22:30.759703+00:00
---

Cisco IP Conference Phone 7832 Release Notes for Firmware Release 12.8(1)

# Cisco IP Conference Phone 7832 Release Notes for Firmware Release 12.8(1)

### Download Options

Updated: April 30, 2020

First Published: April 30, 2020

Last Updated: May 19, 2020

# Cisco IP Conference Phone 7832 Release Notes for Firmware Release 12.8(1)

These release notes support the Cisco IP Conference Phone 7832 running SIP Firmware Release 12.8(1).

The following table lists the support compatibility for the Cisco IP Phones.

Cisco IP Phone

Support Requirements

7832

Cisco Unified Communications Manager 10.5(2) and later

Cisco Unified Communications Manager DST Olsen version D or later

SRST 8.0 (IOS load 15.1(1)T) and above

Cisco Expressway 8.7

7832

Unified CME 12.3 (Cisco IOS XE Fuji 16.9.1 release)

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Conference Phone 7832 Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation
                        URL:

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

##### Limitations for Lines and Line Keys

If the old phone has more lines or more line buttons than the new phone supports, only the supported number of lines or line
                           buttons are migrated.

For example:

Scenario: The old phone had 4 line buttons and the new phone has 2 line buttons

Migration result: The new phone has the line buttons set up like the first 2 line buttons on the old phone.

##### Where to Find More Information

Cisco IP Conference Phone 7832 Administration Guide

Feature Configuration Guide for Cisco Unified Communications
                                    Manager , Release 12.5(1)SU3 or later

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications Manager is running the latest
                     device pack. After you install a device pack on the Cisco Unified Communications Manager servers in the cluster, you need
                     to reboot all the servers.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html .

### Install the Firmware Release on Cisco Unified Communications Manager

If a Cisco Unified Communications Manager is not available to load the installer program, the following zip file is available
                        to load the firmware:

cmterm-7832-sip.12-8-1-0001-455.k3.cop.sgn

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                        interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco IP Phones 7800 Series .

Choose IP Conference Phone 7832 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.8(1) .

Download the relevant zip files.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server. See Administration Guide for Cisco Unified Communications Manager and IM and Presence Service for information about how to manually copy the firmware files to the server.

### Install the Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following zip file is available
                        to load the firmware:

cmterm-7832.12-8-1-0001-455.zip

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN
                        interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco IP Phones 7800 Series .

Choose IP Conference Phone 7832 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 12.8(1) .

Download the relevant zip files.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server. See Administration Guide for Cisco Unified Communications Manager and IM and Presence Service for information about how to manually copy the firmware files to the server.

## Limitations and Restrictions

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

### Phone Data Migration Limitation

The text that displays on the phone for this feature has been localized. The text for the feature in Cisco Unified
                           				Communications Manager Software Release 11.5SU8 hasn't been localized. Localization of the text is complete in Cisco Unified
                           				Communications Manager Software Release 12.5(1)SU3 and later.

## Caveats

### Open Caveats

There are no open severity 1, 2, and 3 defects for the Cisco IP Conference Phone 7832 for Firmware Release 12.8(1).

Because defect status continually changes, the information in this section is a snapshot of the defects that were resolved
                        at the time this report was compiled. For an updated view of resolved defects, access the Bug Toolkit as described in View Caveats .

### Resolved Caveats

There are no resolved severity 1, 2, and 3 defects for the Cisco IP Conference Phone 7832 for Firmware Release 12.8(1).

Because defect status continually changes, the information in this section is a snapshot of the defects that were resolved
                        at the time this report was compiled. For an updated view of resolved defects, access the Bug Toolkit as described in View Caveats .

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

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.8(1.*),12.8(1)&sb=anfr&svr=3nH&bt=custV

To find all open caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.8(1)&sb=afr&sts=open&svr=3nH&bt=custV

To find all resolved caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.8(1.*),12.8(1)&sb=anfr&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional)  To look for information about a specific problem, enter the bug ID number in the Search for field, and press Enter .

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
| 7832 | Cisco Unified Communications Manager 10.5(2) and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above Cisco Expressway 8.7 |
| 7832 | Unified CME 12.3 (Cisco IOS XE Fuji 16.9.1 release) |

| Note | Some features may require the installation of a Cisco Unified Communications Manager Device Package. Failure to install the
                              Device Package before the phone firmware upgrade may render the phones unusable. |
|---|---|

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phones 7800 Series . |
| Step 3 | Choose IP Conference Phone 7832 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.8(1) . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Administration Guide for Cisco Unified Communications Manager and IM and Presence Service for information about how to manually copy the firmware files to the server. |

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phones 7800 Series . |
| Step 3 | Choose IP Conference Phone 7832 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 12.8(1) . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Administration Guide for Cisco Unified Communications Manager and IM and Presence Service for information about how to manually copy the firmware files to the server. |

| Step 1 | Perform one of the following actions: To find all caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.8(1.*),12.8(1)&sb=anfr&svr=3nH&bt=custV To find all open caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.8(1)&sb=afr&sts=open&svr=3nH&bt=custV To find all resolved caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=12.8(1.*),12.8(1)&sb=anfr&svr=3nH&bt=custV |
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