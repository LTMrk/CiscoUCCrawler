---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-191-firmware-12-0-1-release-notes-at91-b-release-notes-cisco-ata-191-ht-8a85d0251a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/191/firmware/12-0-1/release_notes/at91_b_release-notes-cisco-ata-191.html
retrieved_at: 2026-08-22T01:11:35.113860+00:00
---

Cisco ATA 191 Analog Telephone Adapter Release Notes for Firmware Release 12.0(1)

# Cisco ATA 191 Analog Telephone Adapter Release Notes for Firmware Release 12.0(1)

### Download Options

Updated: November 14, 2018

First Published: November 22, 2017

Last Updated: November 14, 2018

# Release Notes for Cisco ATA 191 Analog Telephone Adapter for Firmware Release 12.0(1)

These release notes support the Cisco 191 Analog Telephone Adapter (ATA) running Firmware Release 12.0(1).

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

In the Latest Releases folder, choose 12.0(1) .

Select cmterm-ata191.12-0-1-29.k3.cop.sgn firmware, click the Download or Add to cart button, and follow the prompts.

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

In the Latest Releases folder, choose 12.0(1) .

Select cmterm-ata191.12-0-1-29.zip firmware, click the Download or Add to cart button, and follow the prompts.

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

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=268437683&flowid=77852 |
|---|---|
| Step 2 | Choose ATA 190 Series Analog Telephone Adapters > ATA 191 Analog Telephone Adapter . |
| Step 3 | In the Latest Releases folder, choose 12.0(1) . |
| Step 4 | Select cmterm-ata191.12-0-1-29.k3.cop.sgn firmware, click the Download or Add to cart button, and follow the prompts. |
| Step 5 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 6 | Follow the instructions in the readme file to install the firmware. |

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=268437683&flowid=77852 |
|---|---|
| Step 2 | Choose ATA 190 Series Analog Telephone Adapters > ATA 191 Analog Telephone Adapter . |
| Step 3 | In the Latest Releases folder, choose 12.0(1) . |
| Step 4 | Select cmterm-ata191.12-0-1-29.zip firmware, click the Download or Add to cart button, and follow the prompts. |
| Step 5 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 6 | Follow the instructions in the readme file to install the firmware. |

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%20ATA191%2012.0.1SR1&pf=prdNm&pfVal=286319456&sb=anfr&bt=custV Use this URL for open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%20ATA191%2012.0.1SR1&pf=prdNm&pfVal=286319456&sb=null&sts=open&bt=custV Use this URL for resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%20ATA191%2012.0.1SR1&pf=prdNm&pfVal=286319456&sb=null&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |