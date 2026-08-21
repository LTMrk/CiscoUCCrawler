---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-firmware-10-3-1-sr6-cs38-b-rns-8831-1031sr6-html-eb777bc06c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/firmware/10-3-1-sr6/cs38_b_rns-8831-1031sr6.html
retrieved_at: 2026-08-21T13:33:31.901927+00:00
---

Cisco Unified IP Conference Phone 8831 Release Notes for Firmware Release 10.3(1)SR6

# Cisco Unified IP Conference Phone 8831 Release Notes for Firmware Release 10.3(1)SR6

### Download Options

Updated: April 16, 2020

First Published: April 14, 2020

Last Updated: April 16, 2021

# Introduction

These release notes support the Cisco Unified IP Conference Phone 8831 running SIP Firmware Release 10.3(1)SR6.

The following table lists the support and protocol compatibility for the Cisco IP Phones.

Cisco IP Phone

Protocol

Support Requirements

Cisco Unified IP Conference Phone 8831

SIP

Cisco Unified Communications Manager 7.1(5) and later

Cisco Business Edition 3000 8.6(1) and later

Cisco Business Edition 6000 8.6(5) and later

Cisco Unified Communications Manager Express 10.0 and later; on IOS, release 15.4(1)T or later

Cisco Hosted Collaboration Solution 8.6(2) and later

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco Unified IP Conference Phone 8831 Documentation

Refer to
                        		  publications that are specific to your language, phone model, and call control
                        		  system. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/tsd-products-support-series-home.html

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

### Features Available
                  	 with the Firmware Release

The following sections describe the features available with the Firmware
                     		Release.

#### Transport Layer Security Enhancements

The Cisco Unified IP Conference Phone 8831 now supports Transport Layer Security (TLS) 1.0, 1.1 and 1.2.

TLS 1.0 and TLS 1.1 cannot be disabled from the Cisco Unified Communications Manager (Unified CM) for the Cisco Unified IP
                           Conference Phone 8831.

To use TLS 1.2, you must install a LSC certificate that supports TLS 1.2.

##### Where to Find More Information

Cisco IP Conference Phone 8831 Administration Guide

## Installation

When you install the 10.3(1)SR6 firmware, the steps you follow depend on the firmware version on your phone.

You need to install an interim firmware load before you install the 10.3(1)SR6 firmware.

You can directly upgrade to 10.3(1)SR6.

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified
                        				Communications Manager is running the latest device package. After you install a device package on the Cisco Unified
                        				Communications Manager servers in the cluster, you need to reboot all the servers.

If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly.

For information on the Cisco Unified
                        				Communications Manager Device Packages, see https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix.html .

### Upgrade from 10.3(1) to 10.3(1)SR6

If your Cisco Unified IP Conference Phone 8831 is running Firmware Release 10.3(1), 10.3(1)SR1, 10.3(1)SR2, 10.3(1)SR3, 10.3(1)SR4,
                        10.3(1)SR4b or 10.3(1)SR5, use this set of upgrade instructions.

Before you begin

#### Before you begin

Before using Cisco Unified IP Phone Firmware Release 10.3(1)SR6 with Cisco Unified Communications Manager, you must install
                        the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

http://www.cisco.com/cisco/software/navigator.html?mdfid=268437892&flowid=5293

Choose Cisco Unified IP Phones 8800 Series .

Choose Cisco Unified IP Conference Phone 8831 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 10.3(1)SR6 .

Select the required region-specific file as described in the following table, click the Download Now or Add to cart button, and follow the prompts.

Region

Region-Specific Firmware

North America

cmterm-8831-sip.10-3-1SR6-4-NA.cop.sgn

Europe

cmterm-8831-sip.10-3-1SR6-4-EU.cop.sgn

Latin America

cmterm-8831-sip.10-3-1SR6-4-LA.cop.sgn

Brazil

cmterm-8831-sip.10-3-1SR6-4-BR.cop.sgn

Taiwan

cmterm-8831-sip.10-3-1SR6-4-TW.cop.sgn

Japan

cmterm-8831-sip.10-3-1SR6-4-JP.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware filename in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware:

cmterm-8831-sip.10-3-1SR6-4-readme.html

Follow the instructions in the readme file to install the firmware.

If the Cisco Unified Communications Manager Device Pack to support this release is not available, download the file cmterm-8831-QED-1031-4.k3.cop.sgn and install it on the Cisco Unified Communications Manager.

Follow the instructions in the readme file to install the firmware.

### Upgrade from 9.3(3) to 10.3(1)SR6

If your Cisco Unified IP Conference Phone 8831 is running Firmware Release 9.3(3) or 9.3(3)SE9, use these upgrade instructions.
                        You must upgrade the phone from 9.3(3) to the interim release version 9-3-3-TO-10-3-1-v2 and then to the region specific load
                        of 10.3(1) and later.

Before you begin

#### Before you begin

Before using Cisco Unified IP Phone Firmware Release 10.3(1)SR6 with Cisco Unified Communications Manager, you must install
                        the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&i=rm

Choose Cisco Unified IP Phones 8800 Series .

Choose Cisco Unified IP Conference Phone 8831 .

Choose Session Initiation Protocol (SIP) Software .

In the All Releases folder, expand the SIPv.10 folder and choose 10.3(1) .

Select the file cmterm-8831-sip.9-3-3-TO-10-3-1-v2.cop.sgn , click the Download Now or Add to cart button, and follow the prompts.

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware filename in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware:

cmterm-8831-sip.9-3-3-TO-10-3-1-v2-readme.html

Follow the instructions in the readme file to install the firmware.

Return to the firmware download page.

In the Latest Releases folder, choose 10.3(1)SR6 .

Select the required region-specific file as described in the following table, click the Download Now or Add to cart button, and follow the prompts.

Region

Region-Specific Firmware

North America

cmterm-8831-sip.10-3-1SR6-4-NA.cop.sgn

Europe

cmterm-8831-sip.10-3-1SR6-4-EU.cop.sgn

Latin America

cmterm-8831-sip.10-3-1SR6-4-LA.cop.sgn

Brazil

cmterm-8831-sip.10-3-1SR6-4-BR.cop.sgn

Taiwan

cmterm-8831-sip.10-3-1SR6-4-TW.cop.sgn

Japan

cmterm-8831-sip.10-3-1SR6-4-JP.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware filename in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

If the Cisco Unified Communications Manager Device Pack to support this release is not available, download the file cmterm-8831-QED-1031-4.k3.cop.sgn and install it on the Cisco Unified Communications Manager.

Follow the instructions in the readme file to install the firmware.

### Upgrade from 10.3(1) to 10.3(1)SR6 with Zip Files

If a Cisco Unified Communications Manager is not available to load the installer, you can use a .zip file to load the firmware.

If your Cisco Unified IP Conference Phone 8831 is running Firmware Release 10.3(1), 10.3(1)SR1, 10.3(1)SR2, 10.3(1)SR3, 10.3(1)SR4,
                        10.3(1)SR4b, or 10.3(1)SR5 use this set of upgrade instructions.

Before you begin

#### Before you begin

Before using Cisco Unified IP Phone Firmware Release 10.3(1)SR6 with Cisco Unified Communications Manager, you must install
                        the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

http://www.cisco.com/cisco/software/navigator.html?mdfid=268437892&flowid=5293

Choose Cisco Unified IP Phones 8800 Series .

Choose Cisco Unified IP Conference Phone 8831 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 10.3(1)SR6 .

Download the zip file for your region.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server.

If the Cisco Unified Communications Manager Device Pack to support this release is not available, download the file cmterm-8831-QED-1031-4.k3.cop.sgn and install it on the Cisco Unified Communications Manager.

### Upgrade from 9.3(3) to 10.3(1)SR6 with Zip Files

If a Cisco Unified Communications Manager is not available to load the installer, you can use a .zip file to load the firmware.

If your Cisco Unified IP Conference Phone 8831 is running Firmware Release 9.3(3) or 9.3(3)SE9, use these upgrade instructions.
                        You must upgrade the phone from 9.3(3) to the interim release version 9-3-3-TO-10-3-1-v2 and then to the region specific load
                        of 10.3(1) and later.

Before you begin

#### Before you begin

Before using Cisco Unified IP Phone Firmware Release 10.3(1)SR6 with Cisco Unified Communications Manager, you must install
                        the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&i=rm

Choose Cisco Unified IP Phones 8800 Series .

Choose Cisco Unified IP Conference Phone 8831 .

Choose Session Initiation Protocol (SIP) Software .

In the All Releases folder, expand the SIPv.10 folder and choose 10.3(1) .

Select the file cmterm-8831-sip.9-3-3-TO-10-3-1-v2.zip , click the Download Now or Add to cart button, and follow the prompts.

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware filename in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware:

cmterm-8831-sip.9-3-3-TO-10-3-1-v2-readme.html

Follow the instructions in the readme file to install the firmware.

Return to the firmware download page.

In the Latest Releases folder, choose 10.3(1)SR6 .

Select the required region-specific file as described in the following table, click the Download Now or Add to cart button, and follow the prompts.

Region

Region-Specific Firmware

North America

cmterm-8831-sip.10-3-1SR6-4-NA.zip

Europe

cmterm-8831-sip.10-3-1SR6-4-EU.zip

Latin America

cmterm-8831-sip.10-3-1SR6-4-LA.zip

Brazil

cmterm-8831-sip.10-3-1SR6-4-BR.zip

Taiwan

cmterm-8831-sip.10-3-1SR6-4-TW.zip

Japan

cmterm-8831-sip.10-3-1SR6-4-JP.zip

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware filename in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Unzip the files.

Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server.

If the Cisco Unified Communications Manager Device Pack to support this release is not available, download the file cmterm-8831-QED-1031-4.k3.cop.sgn and install it on the Cisco Unified Communications Manager.

## Limitations and Restrictions

### Firmware Downgrade Limitation

After you install Firmware Release 10.3(1)SR3 on a conference phone, you cannot downgrade the firmware to a previous version.

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

https://bst.cloudapps.cisco.com/bugsearch/search?kw=10.3(1)SR6&pf=prdNm&sb=anfr&bt=custV

To find all open caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=10.3(1)SR6&pf=prdNm&sb=anfr&sts=open&bt=custV

To find all resolved caveats for this release, use this URL:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=10.3(1)SR6&pf=prdNm&sb=anfr&sts=fd&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

There are no open defects for the 10.3(1)SR6 Firmware Release.

For an updated view of open defects, access Bug Toolkit as described in View Caveats .

### Resolved Caveats

The following list contains the defects that are resolved for the 10.3(1)SR6 Firmware Release.

For more information about an individual defect, you can access the online record for the defect by accessing the Bug Search
                        tool and entering the Identifier. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                        report was compiled. For an updated view of resolved defects, access Bug Toolkit as described in View Caveats .

CSCvo19825 Cisco IP Phone 8831 Series SIP XML Denial of Service Vulnerability

CSCvo55040 Cisco IP Phone 8831 Series CDP and LLDP Denial of Service Vulnerability

CSCvo55920 Multiple Vulnerabilities in libxml2

CSCvo74251 xinetd TCPMUX Services User and Group Directives Issue

CSCvp29372 HTTP Security Header X-Content-Type-Options Not Detected by vulnerability scanner

CSCvp34356 Vulnerable version of busybox in use

CSCvp36548 IP Phone Service not executing on a 8831

CSCvq23976 Evaluation of odm_jdm_phones for TCP SACK vulnerabilities

CSCvq27230 802.1x auth failure for 8831 phones because of the server Hello message was treated as Alert message

CSCvq64657 CVE-2015-3153 CVE-2014-0015 CVE-2018-16842 Multiple Vulnerabilities in curl

CSCvr96738 Cisco IP Phone Remote Code Execution and Denial of Service Vulnerability

CSCvr96748 Cisco IP Phone CDP Broadcast Issue

CSCvs22421 8831 reboots when receiving CDP packet from switch with LLC traffic and value set to 3

CSCvs39617 8831 phones have robotic audio in third-party IVR

CSCvt33913 Cisco 8831 Conference Phone TLS 1.2 Support

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
| Cisco Unified IP Conference Phone 8831 | SIP | Cisco Unified Communications Manager 7.1(5) and later Cisco Business Edition 3000 8.6(1) and later Cisco Business Edition 6000 8.6(5) and later Cisco Unified Communications Manager Express 10.0 and later; on IOS, release 15.4(1)T or later Cisco Hosted Collaboration Solution 8.6(2) and later |

| Note | If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: http://www.cisco.com/cisco/software/navigator.html?mdfid=268437892&flowid=5293 |
|---|---|
| Step 2 | Choose Cisco Unified IP Phones 8800 Series . |
| Step 3 | Choose Cisco Unified IP Conference Phone 8831 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 10.3(1)SR6 . |
| Step 6 | Select the required region-specific file as described in the following table, click the Download Now or Add to cart button, and follow the prompts. Table 2. Wireless Microphone Regions and Firmware Loads Region Region-Specific Firmware North America cmterm-8831-sip.10-3-1SR6-4-NA.cop.sgn Europe cmterm-8831-sip.10-3-1SR6-4-EU.cop.sgn Latin America cmterm-8831-sip.10-3-1SR6-4-LA.cop.sgn Brazil cmterm-8831-sip.10-3-1SR6-4-BR.cop.sgn Taiwan cmterm-8831-sip.10-3-1SR6-4-TW.cop.sgn Japan cmterm-8831-sip.10-3-1SR6-4-JP.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Region | Region-Specific Firmware | North America | cmterm-8831-sip.10-3-1SR6-4-NA.cop.sgn | Europe | cmterm-8831-sip.10-3-1SR6-4-EU.cop.sgn | Latin America | cmterm-8831-sip.10-3-1SR6-4-LA.cop.sgn | Brazil | cmterm-8831-sip.10-3-1SR6-4-BR.cop.sgn | Taiwan | cmterm-8831-sip.10-3-1SR6-4-TW.cop.sgn | Japan | cmterm-8831-sip.10-3-1SR6-4-JP.cop.sgn | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Region | Region-Specific Firmware |
| North America | cmterm-8831-sip.10-3-1SR6-4-NA.cop.sgn |
| Europe | cmterm-8831-sip.10-3-1SR6-4-EU.cop.sgn |
| Latin America | cmterm-8831-sip.10-3-1SR6-4-LA.cop.sgn |
| Brazil | cmterm-8831-sip.10-3-1SR6-4-BR.cop.sgn |
| Taiwan | cmterm-8831-sip.10-3-1SR6-4-TW.cop.sgn |
| Japan | cmterm-8831-sip.10-3-1SR6-4-JP.cop.sgn |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware filename in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware: cmterm-8831-sip.10-3-1SR6-4-readme.html |
| Step 8 | Follow the instructions in the readme file to install the firmware. |
| Step 9 | If the Cisco Unified Communications Manager Device Pack to support this release is not available, download the file cmterm-8831-QED-1031-4.k3.cop.sgn and install it on the Cisco Unified Communications Manager. |
| Step 10 | Follow the instructions in the readme file to install the firmware. |

| Region | Region-Specific Firmware |
|---|---|
| North America | cmterm-8831-sip.10-3-1SR6-4-NA.cop.sgn |
| Europe | cmterm-8831-sip.10-3-1SR6-4-EU.cop.sgn |
| Latin America | cmterm-8831-sip.10-3-1SR6-4-LA.cop.sgn |
| Brazil | cmterm-8831-sip.10-3-1SR6-4-BR.cop.sgn |
| Taiwan | cmterm-8831-sip.10-3-1SR6-4-TW.cop.sgn |
| Japan | cmterm-8831-sip.10-3-1SR6-4-JP.cop.sgn |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&i=rm |
|---|---|
| Step 2 | Choose Cisco Unified IP Phones 8800 Series . |
| Step 3 | Choose Cisco Unified IP Conference Phone 8831 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the All Releases folder, expand the SIPv.10 folder and choose 10.3(1) . |
| Step 6 | Select the file cmterm-8831-sip.9-3-3-TO-10-3-1-v2.cop.sgn , click the Download Now or Add to cart button, and follow the prompts. Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware filename in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware: cmterm-8831-sip.9-3-3-TO-10-3-1-v2-readme.html |
| Step 8 | Follow the instructions in the readme file to install the firmware. |
| Step 9 | Return to the firmware download page. |
| Step 10 | In the Latest Releases folder, choose 10.3(1)SR6 . |
| Step 11 | Select the required region-specific file as described in the following table, click the Download Now or Add to cart button, and follow the prompts. Table 3. Wireless Microphone Regions and Firmware Loads Region Region-Specific Firmware North America cmterm-8831-sip.10-3-1SR6-4-NA.cop.sgn Europe cmterm-8831-sip.10-3-1SR6-4-EU.cop.sgn Latin America cmterm-8831-sip.10-3-1SR6-4-LA.cop.sgn Brazil cmterm-8831-sip.10-3-1SR6-4-BR.cop.sgn Taiwan cmterm-8831-sip.10-3-1SR6-4-TW.cop.sgn Japan cmterm-8831-sip.10-3-1SR6-4-JP.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Region | Region-Specific Firmware | North America | cmterm-8831-sip.10-3-1SR6-4-NA.cop.sgn | Europe | cmterm-8831-sip.10-3-1SR6-4-EU.cop.sgn | Latin America | cmterm-8831-sip.10-3-1SR6-4-LA.cop.sgn | Brazil | cmterm-8831-sip.10-3-1SR6-4-BR.cop.sgn | Taiwan | cmterm-8831-sip.10-3-1SR6-4-TW.cop.sgn | Japan | cmterm-8831-sip.10-3-1SR6-4-JP.cop.sgn | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Region | Region-Specific Firmware |
| North America | cmterm-8831-sip.10-3-1SR6-4-NA.cop.sgn |
| Europe | cmterm-8831-sip.10-3-1SR6-4-EU.cop.sgn |
| Latin America | cmterm-8831-sip.10-3-1SR6-4-LA.cop.sgn |
| Brazil | cmterm-8831-sip.10-3-1SR6-4-BR.cop.sgn |
| Taiwan | cmterm-8831-sip.10-3-1SR6-4-TW.cop.sgn |
| Japan | cmterm-8831-sip.10-3-1SR6-4-JP.cop.sgn |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 12 | Click the + next to the firmware filename in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 13 | If the Cisco Unified Communications Manager Device Pack to support this release is not available, download the file cmterm-8831-QED-1031-4.k3.cop.sgn and install it on the Cisco Unified Communications Manager. |
| Step 14 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Region | Region-Specific Firmware |
|---|---|
| North America | cmterm-8831-sip.10-3-1SR6-4-NA.cop.sgn |
| Europe | cmterm-8831-sip.10-3-1SR6-4-EU.cop.sgn |
| Latin America | cmterm-8831-sip.10-3-1SR6-4-LA.cop.sgn |
| Brazil | cmterm-8831-sip.10-3-1SR6-4-BR.cop.sgn |
| Taiwan | cmterm-8831-sip.10-3-1SR6-4-TW.cop.sgn |
| Japan | cmterm-8831-sip.10-3-1SR6-4-JP.cop.sgn |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Step 1 | Go to the following URL: http://www.cisco.com/cisco/software/navigator.html?mdfid=268437892&flowid=5293 |
|---|---|
| Step 2 | Choose Cisco Unified IP Phones 8800 Series . |
| Step 3 | Choose Cisco Unified IP Conference Phone 8831 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 10.3(1)SR6 . |
| Step 6 | Download the zip file for your region. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |
| Step 9 | If the Cisco Unified Communications Manager Device Pack to support this release is not available, download the file cmterm-8831-QED-1031-4.k3.cop.sgn and install it on the Cisco Unified Communications Manager. |

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&i=rm |
|---|---|
| Step 2 | Choose Cisco Unified IP Phones 8800 Series . |
| Step 3 | Choose Cisco Unified IP Conference Phone 8831 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the All Releases folder, expand the SIPv.10 folder and choose 10.3(1) . |
| Step 6 | Select the file cmterm-8831-sip.9-3-3-TO-10-3-1-v2.zip , click the Download Now or Add to cart button, and follow the prompts. Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware filename in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware: cmterm-8831-sip.9-3-3-TO-10-3-1-v2-readme.html |
| Step 8 | Follow the instructions in the readme file to install the firmware. |
| Step 9 | Return to the firmware download page. |
| Step 10 | In the Latest Releases folder, choose 10.3(1)SR6 . |
| Step 11 | Select the required region-specific file as described in the following table, click the Download Now or Add to cart button, and follow the prompts. Table 4. Wireless Microphone Regions and Firmware Loads Region Region-Specific Firmware North America cmterm-8831-sip.10-3-1SR6-4-NA.zip Europe cmterm-8831-sip.10-3-1SR6-4-EU.zip Latin America cmterm-8831-sip.10-3-1SR6-4-LA.zip Brazil cmterm-8831-sip.10-3-1SR6-4-BR.zip Taiwan cmterm-8831-sip.10-3-1SR6-4-TW.zip Japan cmterm-8831-sip.10-3-1SR6-4-JP.zip Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Region | Region-Specific Firmware | North America | cmterm-8831-sip.10-3-1SR6-4-NA.zip | Europe | cmterm-8831-sip.10-3-1SR6-4-EU.zip | Latin America | cmterm-8831-sip.10-3-1SR6-4-LA.zip | Brazil | cmterm-8831-sip.10-3-1SR6-4-BR.zip | Taiwan | cmterm-8831-sip.10-3-1SR6-4-TW.zip | Japan | cmterm-8831-sip.10-3-1SR6-4-JP.zip | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Region | Region-Specific Firmware |
| North America | cmterm-8831-sip.10-3-1SR6-4-NA.zip |
| Europe | cmterm-8831-sip.10-3-1SR6-4-EU.zip |
| Latin America | cmterm-8831-sip.10-3-1SR6-4-LA.zip |
| Brazil | cmterm-8831-sip.10-3-1SR6-4-BR.zip |
| Taiwan | cmterm-8831-sip.10-3-1SR6-4-TW.zip |
| Japan | cmterm-8831-sip.10-3-1SR6-4-JP.zip |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 12 | Click the + next to the firmware filename in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 13 | Unzip the files. |
| Step 14 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |
| Step 15 | If the Cisco Unified Communications Manager Device Pack to support this release is not available, download the file cmterm-8831-QED-1031-4.k3.cop.sgn and install it on the Cisco Unified Communications Manager. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Region | Region-Specific Firmware |
|---|---|
| North America | cmterm-8831-sip.10-3-1SR6-4-NA.zip |
| Europe | cmterm-8831-sip.10-3-1SR6-4-EU.zip |
| Latin America | cmterm-8831-sip.10-3-1SR6-4-LA.zip |
| Brazil | cmterm-8831-sip.10-3-1SR6-4-BR.zip |
| Taiwan | cmterm-8831-sip.10-3-1SR6-4-TW.zip |
| Japan | cmterm-8831-sip.10-3-1SR6-4-JP.zip |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Step 1 | Perform one of the following actions: To find all caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=10.3(1)SR6&pf=prdNm&sb=anfr&bt=custV To find all open caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=10.3(1)SR6&pf=prdNm&sb=anfr&sts=open&bt=custV To find all resolved caveats for this release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=10.3(1)SR6&pf=prdNm&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . |

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