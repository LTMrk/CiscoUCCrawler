---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-firmware-11-3-2sr1-releasenotes-at9x-b-ata-191-192-rn-1132sr1--64bb63ea65
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/firmware/11-3-2SR1/releasenotes/at9x_b_ata-191_192-rn-1132sr1.html
retrieved_at: 2026-08-21T12:49:43.343933+00:00
---

Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.3(2)SR1

# Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.3(2)SR1

### Download Options

Updated: July 9, 2026

First Published: July 9, 2026

# Release Notes

These release notes support the Cisco ATA 191 and 192 Analog Telephone Adapter for Multiplatform Firmware Release 11.3(2)SR1.

The following table lists the support and protocol compatibility for the Cisco ATA.

Cisco IP Phone

Protocol

Support Requirements

Cisco ATA 191 and 192

SIP

BroadSoft BroadWorks 24.0

Asterisk 13.1

## Cisco ATA 190 Series Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation
                     URL:

https://www.cisco.com/c/en/us/products/unified-communications/ata-190-series-analog-telephone-adapters/index.html

## Upgrade the Firmware

The Cisco ATA 191 and 192 Multiplatform support dual image upgrades by TFTP, HTTP, or HTTPS.

Step 1

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286282490&flowid=83468

Step 2

Choose Cisco ATA 190 Series Analog Telephone Adapters .

Step 3

Choose your ATA model.

Step 4

In the Latest Releases folder, choose 11.3.2 MSR1 .

Step 5

Download the file ATA19x.11-3-2MPP0102-233.zip.

Step 6

Unzip the files.

Step 7

Put the files on the TFTP/HTTP/HTTPS download directory.

Step 8

Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is:

<schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img

Here is an example,

http://192.168.1.100/firmware/ATA19x.11-3-2MPP0102-233.img

After the firmware upgrade completes, the phone reboots automatically.

## New and Changed Features

This release is a maintenance release and doesn't contain any new or enhanced features.

To view the resolved and open caveats for this release, see View Caveats .

### Caveats

## View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

### Before you begin

To view caveats, you need the following items:

Cisco.com user ID and password

Step 1

Use this URL for all and resolved caveats: https://bst.cloudapps.cisco.com/bugsearch?pf=prdNm&sb=fr&rls=11.3(2)SR1&kw=*&bt=custV

Step 2

When prompted, log in with your Cisco.com user ID and password.

Step 3

(Optional) Enter the bug ID number in the Search for field, then press Enter .

## Open Caveats

There are no open caveats in this release.

## Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco ATA 191 and 192 Analog Telephone
                     Adapter Multiplatform Phones for Firmware Release 11.3(2)SR1.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                     You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                     report was compiled. For an updated view of open defects, access Bug Toolkit as described in View Caveats .

CSCwt95573—When an ATA emergency service is configured with matching geolocation URLs, the service might fail and return an
                           error code.

CSCwt87845—When Proxy_Mode is Auto and no PAC URL is configured, SIP registration fails.

CSCwu09104—The ATA device doesn't respond incorrectly with the NTLM authentication method.

CSCwv11476—ATA192 would not follow the DHCP option 160 and perform the DNS query accordingly.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and, in some cases, can cause a call to drop. Sources of
                        network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco ATA 191 and 192 | SIP | BroadSoft BroadWorks 24.0 Asterisk 13.1 |

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=286282490&flowid=83468 |
|---|---|
| Step 2 | Choose Cisco ATA 190 Series Analog Telephone Adapters . |
| Step 3 | Choose your ATA model. |
| Step 4 | In the Latest Releases folder, choose 11.3.2 MSR1 . |
| Step 5 | Download the file ATA19x.11-3-2MPP0102-233.zip. |
| Step 6 | Unzip the files. |
| Step 7 | Put the files on the TFTP/HTTP/HTTPS download directory. |
| Step 8 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is: <schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img Here is an example, http://192.168.1.100/firmware/ATA19x.11-3-2MPP0102-233.img After the firmware upgrade completes, the phone reboots automatically. |

| Step 1 | Use this URL for all and resolved caveats: https://bst.cloudapps.cisco.com/bugsearch?pf=prdNm&sb=fr&rls=11.3(2)SR1&kw=*&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |