---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-firmware-12-1-1sr1-release-notes-at91-b-ata-1201sr1-html-d31c4c434d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/firmware/12-1-1SR1/release_notes/at91_b_ata-1201sr1.html
retrieved_at: 2026-08-22T01:11:30.573218+00:00
---

Cisco ATA 191 Analog Telephone Adapter Release Notes for Firmware Release 12.0(1)SR1

# Cisco ATA 191 Analog Telephone Adapter Release Notes for Firmware Release 12.0(1)SR1

### Download Options

Updated: November 14, 2018

First Published: March 29, 2018

Last Updated: November 14, 2018

# Release Notes for Cisco ATA 191 Analog Telephone Adapter for Firmware Release 12.0(1)SR1

These release notes support the Cisco 191 Analog Telephone Adapter (ATA) running Firmware Release 12.0(1)SR1.

The following table lists the support and protocol compatibility for the Cisco ATA 191.

Cisco IP Phone

Protocol

Support Requirements

Cisco ATA 191

SIP

Cisco Unified Communications Manager 10.5(1) and later

Cisco Unified Communications Manager DST Olsen version D or later

Cisco ATA 191

SIP

CME 12.6

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco Unified
                     				Communications Manager Documentation

See the Cisco Unified
                              				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                           				Communications Manager release. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications Manager is running the latest
                     device pack. After you install a device pack on the Cisco Unified Communications Manager servers in the cluster, you need
                     to reboot all the servers.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html .

### Install the Firmware Release on Cisco Unified Communications Manager

Before you use the Cisco Analog Telephone Adapter with Cisco Unified Communications Manager 10.5, or higher, you must install
                        the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

Besides Cisco Unified Communications Manager, the Cisco ATA 191 can also work with Cisco Unified Communications Manager Express
                        and Cisco Unified Survivable Remote Site Telephony (SRST). Refer to the Related Documentation section for more information.

Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=268437683&flowid=77852

Choose ATA 190 Series Analog Telephone Adapters > ATA 191 Analog Telephone Adapter .

In the Latest Releases folder, choose 12.0(1)SR1 .

Select cmterm-ata191.12-0-1SR1-1.k3.cop.sgn firmware, click the Download or Add to cart button, and follow the prompts.

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

In the Latest Releases folder, choose 12.0(1)SR1 .

Select cmterm-ata191.12-0-1SR1-1.zip firmware, click the Download or Add to cart button, and follow the prompts.

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

Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%20ATA191%2012.0.1SR1&pf=prdNm&pfVal=286319456&sb=anfr&bt=custV

Use this URL for open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%20ATA191%2012.0.1SR1&pf=prdNm&pfVal=286319456&sb=null&sts=open&bt=custV

Use this URL for resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%20ATA191%2012.0.1SR1&pf=prdNm&pfVal=286319456&sb=null&sts=fd&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

The following table lists severity 1, 2, and 3 defects that are open for the Cisco ATA 191 Analog Telephone Adapter Firmware
                        Release 12.0(1)SR1.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

Identifier

Description

CSCvg61100

Within about 10 seconds after MWI off, off-hook no dial tone

CSCvg01656

DUT connect to half duplex Ethernet port can't link up after power on

CSCvg05091

DHCPv6 Solicit content cannot be recognized by IPv6 Ready Logo DHCPv6 tool

### Resolved Caveats

The following table lists severity 1, 2, and 3 defects that are resolved for the Cisco ATA 191 Analog Telephone Adapter Release
                        Firmware Release 12.0(1)SR1.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

Identifier

Description

CSCvg08575

Does not support daylight saving time in non-legacy phone supported timezone

CSCvf41125

DUT sends un-configured multicast packets

CSCvg12065

Telephony event and inband DTMF should not be generated at the same time

CSCvg32457

When there's private call, ATA should let analog phone display some kind of "Blocked" string

CSCvg79108

Incorrect reverse polarity behavior

CSCvf92297

The configuration of DSCP can't take effect

CSCvg82381

ATA does not play IPv6 MOH when two-way voice is IPv4 RTP

CSCvg77965

DUT can't dial out and it lost IPv6 address from CUCM view

CSCvh56729

AX betwween T38 and passthrough has low pass rate on FAXLab test (May have DSPG dependency)

CSCvh56709

Modem call does not connect successfully (DSPG dependency)

CSCvh88547

T.38 sender to pass through receiver cause DUT restart after on hook

CSCvi33600

No audio when swap call legs of call waiting

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

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/c/en/us/td/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application.
                  The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco ATA 191 | SIP | Cisco Unified Communications Manager 10.5(1) and later Cisco Unified Communications Manager DST Olsen version D or later |
| Cisco ATA 191 | SIP | CME 12.6 |

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=268437683&flowid=77852 |
|---|---|
| Step 2 | Choose ATA 190 Series Analog Telephone Adapters > ATA 191 Analog Telephone Adapter . |
| Step 3 | In the Latest Releases folder, choose 12.0(1)SR1 . |
| Step 4 | Select cmterm-ata191.12-0-1SR1-1.k3.cop.sgn firmware, click the Download or Add to cart button, and follow the prompts. |
| Step 5 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 6 | Follow the instructions in the readme file to install the firmware. |

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=268437683&flowid=77852 |
|---|---|
| Step 2 | Choose ATA 190 Series Analog Telephone Adapters > ATA 191 Analog Telephone Adapter . |
| Step 3 | In the Latest Releases folder, choose 12.0(1)SR1 . |
| Step 4 | Select cmterm-ata191.12-0-1SR1-1.zip firmware, click the Download or Add to cart button, and follow the prompts. |
| Step 5 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 6 | Follow the instructions in the readme file to install the firmware. |

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%20ATA191%2012.0.1SR1&pf=prdNm&pfVal=286319456&sb=anfr&bt=custV Use this URL for open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%20ATA191%2012.0.1SR1&pf=prdNm&pfVal=286319456&sb=null&sts=open&bt=custV Use this URL for resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%20ATA191%2012.0.1SR1&pf=prdNm&pfVal=286319456&sb=null&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |

| Identifier | Description |
|---|---|
| CSCvg61100 | Within about 10 seconds after MWI off, off-hook no dial tone |
| CSCvg01656 | DUT connect to half duplex Ethernet port can't link up after power on |
| CSCvg05091 | DHCPv6 Solicit content cannot be recognized by IPv6 Ready Logo DHCPv6 tool |

| Identifier | Description |
|---|---|
| CSCvg08575 | Does not support daylight saving time in non-legacy phone supported timezone |
| CSCvf41125 | DUT sends un-configured multicast packets |
| CSCvg12065 | Telephony event and inband DTMF should not be generated at the same time |
| CSCvg32457 | When there's private call, ATA should let analog phone display some kind of "Blocked" string |
| CSCvg79108 | Incorrect reverse polarity behavior |
| CSCvf92297 | The configuration of DSCP can't take effect |
| CSCvg82381 | ATA does not play IPv6 MOH when two-way voice is IPv4 RTP |
| CSCvg77965 | DUT can't dial out and it lost IPv6 address from CUCM view |
| CSCvh56729 | AX betwween T38 and passthrough has low pass rate on FAXLab test (May have DSPG dependency) |
| CSCvh56709 | Modem call does not connect successfully (DSPG dependency) |
| CSCvh88547 | T.38 sender to pass through receiver cause DUT restart after on hook |
| CSCvi33600 | No audio when swap call legs of call waiting |

| Step 1 | To access Cisco Bug Search, go to: https://tools.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                                 			 Cisco.com user ID and password. |
| Step 3 | To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter . |