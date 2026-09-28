---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-firmware-12-0-1sr4-at91-b-cisco-ata-191-rn-1201sr4-html-94f46716f4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/firmware/12-0-1SR4/at91_b_cisco-ata-191-rn-1201sr4.html
retrieved_at: 2026-08-21T12:50:30.008730+00:00
---

Cisco ATA 191 Analog Telephone Adapter Release Notes for Firmware Release 12.0(1)SR4

# Cisco ATA 191 Analog Telephone Adapter Release Notes for Firmware Release 12.0(1)SR4

### Download Options

Updated: October 5, 2021

First Published: September 29, 2021

# Release Notes

These release notes support the Cisco 191 Analog Telephone Adapter (ATA) running Firmware Release 12.0(1)SR4.

The following table lists the support and protocol compatibility for the Cisco ATA 191.

Cisco IP Phone

Protocol

Support Requirements

Cisco ATA 191

SIP

Cisco Unified Communications Manager 10.5(1) and later

Cisco Unified Communications Manager DST Olsen version D or later

## Cisco ATA 191 Analog Telephone Adapter

The Cisco ATA 191 Analog Telephone Adapter allows you to turn an analogue phone or fax communication devices into an IP phone.
                     With this device, you can retain your investment in your current equipment, but also benefit from an IP-based telephony network.

The ATA 191 supports many of the current telephony features, including shared lines, conferencing, and voicemail. It has two
                     images or partitions in permanent storage, which allows the device to recover if the initial image is corrupted. With the
                     dedicated Problem Report Tool button, you can quickly and easily collect troubleshooting information.

The Cisco ATA 191 also supports IPv6, and SSH.

The ATA 191 is easily integrated into your current network. It has two RJ11 ports, each with a phone number, and one RJ45
                     port that provides access to an Ethernet network. Phone configuration is done through an IVR system, and you use a web interface
                     to monitor logs and provide device information.

### Where to Find More Information

Cisco ATA 191 Analog Telephone Adapter Administration Guide for Cisco Unified Communications Manager

Cisco ATA 191 Analog Telephone Adapter User Guide for Cisco Unified Communications Manager

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco Unified
                     				Communications Manager Documentation

See the Cisco Unified
                              				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                           				Communications Manager release. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html

### Cisco Unified Communications Manager Express Documentation

See the Cisco Unified Communications Manager Express publications that are specific to your Cisco Unified Communications Manager
                        Express release. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-express/tsd-products-support-series-home.html

### Cisco ATA 190 Series Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation
                        URL:

https://www.cisco.com/c/en/us/products/unified-communications/ata-190-series-analog-telephone-adapters/index.html

## User Guide Accessibility

The Cisco ATA 191 User Guide for Cisco Unified Communications Manager is accessible for people with limited sight or who are blind. The HTML version of the document is now compatible with the
                     Job Access With Speech (JAWS) reader, so visually impaired users can access information about their device.

### Where to Find More Information

Cisco ATA 191 User Guide for Cisco Unified Communications Manager

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified
                        				Communications Manager is running the latest device package. After you install a device package on the Cisco Unified
                        				Communications Manager servers in the cluster, you need to reboot all the servers.

If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly.

For information on the Cisco Unified
                        				Communications Manager Device Packages, see https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/matrix/CMDP_BK_CCBDA741_00_cucm-device-package-compatibility-matrix.html .

### Install the Firmware Release on Cisco Unified Communications Manager

Before you use the Cisco Analog Telephone Adapter with Cisco Unified Communications Manager 10.5, or higher, you must install
                        the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

Besides Cisco Unified Communications Manager, the Cisco ATA 191 can also work with Cisco Unified Communications Manager Express
                        and Cisco Unified Survivable Remote Site Telephony (SRST). Refer to the Related Documentation section for more information.

Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=268437683&flowid=77852

Choose ATA 190 Series Analog Telephone Adapters > ATA 191 Analog Telephone Adapter .

In the Latest Releases folder, choose 12.0.1 SR4 .

Select cmterm-ATA191.12-0-1-0405-005.k4.cop.sha512 firmware, click the Download or Add to cart button, and follow the prompts.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

### Install the Firmware Zip Files

Before you use the Cisco Analog Telephone Adapter with Cisco Unified Communications Manager 10.5, or higher, you must install
                        the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

Besides Cisco Unified Communications Manager, the Cisco ATA 191 can also work with Cisco Unified Communications Manager Express
                        and Cisco Unified Survivable Remote Site Telephony (SRST). Refer to the Related Documentation section for more information.

Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=268437683&flowid=77852

Choose ATA 190 Series Analog Telephone Adapters > ATA 191 Analog Telephone Adapter .

In the Latest Releases folder, choose 12.0.1 SR4 .

Select cmterm-ata191.12-0-1-0405-005.zip firmware, click the Download or Add to cart button, and follow the prompts.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

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

## Caveats

This section
                     		  describes the resolved and open caveats, and provides information on accessing
                     		  the Cisco Software Bug Toolkit.

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

Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286282490&rls=12.0(1)SR4&sb=fr&bt=custV

Use this URL for open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286282490&rls=12.0(1)SR4&sb=fr&sts=open&bt=custV

Use this URL for resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286282490&rls=12.0(1)SR4&sb=fr&sts=fd&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

The following lists shows the severity 1, 2, and 3 defects that are open for the Cisco ATA 191 Analog Telephone Adapter Firmware
                        Release 12.0(1)SR4.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

There are no open caveats in this release.

### Resolved Caveats

The following list shows the severity 1, 2, and 3 defects that are resolved for the Cisco ATA 191 Analog Telephone Adapter
                        Release Firmware Release 12.0(1)SR4.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCvw25740 ATA191 will lose WAN IP after icmpsic flooding attack

CSCvz27471 ATA191 intermittent one-way and big noise audio during call

CSCvz27489 ATA191 no audio on either side due to RTP start failure

CSCvz28400 ATA191 lost IP address when it is idle

CSCvz28419 ATA191 provides no "User-Agent" header for HTTP PRT uploading

CSCvz28422 ATA191 does not send correct caller ID or call waiting caller ID signaling to UK analog phones

### Access Cisco Bug
                  	 Search

Known problems
                        		  (bugs) are graded according to severity level. These release notes contain
                        		  descriptions of the following:

All severity
                              				level 1 or 2 bugs

Significant
                              				severity level 3 bugs

You can search for
                        		  problems by using Cisco Bug Search.

Before you begin

#### Before you begin

To access Cisco Bug
                        		  Search, you need the following items:

Internet
                              				connection

Web browser

Cisco.com user
                              				ID and password

To access Cisco Bug Search, go to:

https://tools.cisco.com/bugsearch

Log in with your
                                 			 Cisco.com user ID and password.

To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter .

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco ATA 191 | SIP | Cisco Unified Communications Manager 10.5(1) and later Cisco Unified Communications Manager DST Olsen version D or later |

| Note | If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=268437683&flowid=77852 |
|---|---|
| Step 2 | Choose ATA 190 Series Analog Telephone Adapters > ATA 191 Analog Telephone Adapter . |
| Step 3 | In the Latest Releases folder, choose 12.0.1 SR4 . |
| Step 4 | Select cmterm-ATA191.12-0-1-0405-005.k4.cop.sha512 firmware, click the Download or Add to cart button, and follow the prompts. |
| Step 5 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 6 | Follow the instructions in the readme file to install the firmware. |

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=268437683&flowid=77852 |
|---|---|
| Step 2 | Choose ATA 190 Series Analog Telephone Adapters > ATA 191 Analog Telephone Adapter . |
| Step 3 | In the Latest Releases folder, choose 12.0.1 SR4 . |
| Step 4 | Select cmterm-ata191.12-0-1-0405-005.zip firmware, click the Download or Add to cart button, and follow the prompts. |
| Step 5 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 6 | Follow the instructions in the readme file to install the firmware. |

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286282490&rls=12.0(1)SR4&sb=fr&bt=custV Use this URL for open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286282490&rls=12.0(1)SR4&sb=fr&sts=open&bt=custV Use this URL for resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286282490&rls=12.0(1)SR4&sb=fr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |

| Step 1 | To access Cisco Bug Search, go to: https://tools.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                                 			 Cisco.com user ID and password. |
| Step 3 | To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter . |