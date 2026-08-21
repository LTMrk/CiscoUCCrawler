---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-firmware-11-2-4-releasenotes-at9x-b-ata-191-192-rn-1124-html-0b79b55f50
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/firmware/11-2-4/releasenotes/at9x_b_ata-191_192-rn-1124.html
retrieved_at: 2026-08-21T12:50:13.442588+00:00
---

Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.2(4)

# Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.2(4)

### Download Options

Updated: August 31, 2023

First Published: August 31, 2023

# Release Notes

These release notes support the Cisco ATA 191 and 192 Analog Telephone Adapter for Multiplatform Firmware Release 11.2(4).

The following table lists the support and protocol compatibility for the Cisco ATA.

Cisco IP Phone

Protocol

Support Requirements

Cisco ATA 191 and 192

SIP

BroadSoft BroadWorks 24.0

Asterisk 13.1

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco ATA 190 Series Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation
                        URL:

https://www.cisco.com/c/en/us/products/unified-communications/ata-190-series-analog-telephone-adapters/index.html

## Upgrade the firmware

The Cisco ATA 191 and 192 support dual image upgrades by TFTP, HTTP, or HTTPS.

Step 1

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286282490&flowid=83468

Step 2

Choose Cisco ATA 190 Series Analog Telephone Adapters .

Step 3

Choose your ATA model.

Step 4

In the Latest Releases folder, choose 11.2.4 .

Step 5

Download the file ATA19x.11-2-4MPP0001-115.zip.

Step 6

Unzip the files.

Step 7

Put the files on the TFTP/HTTP/HTTPS download directory.

Step 8

Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is:

<schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img

Here is an example,

http://192.168.1.100/firmware/ATA19x.11-2-4MPP0001-115.img

After the firmware upgrade completes, the phone reboots automatically.

## New and Changed Features

### Default Web Access Protocol Changes to HTTPS

From the firmware release 11.2(4), the default protocol for the ATA web page access changes from HTTP to HTTPS to enhance
                        the security. This change also applies to the remote access to the ATA web page.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

### Extend Maximum Number of A Records for SRV Record

The ATA now can store up to 10 DNS A records for a SRV record. Before the release, the maximum number is 5.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

### Log Management for Users

The ATA provides the log management for both users and administrators. Before this release, only administrators have the permission.

Users can access the Phone Adapter Configuration Utility web page to configure and manage the logs. The navigation path is: Administration > Log .

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter User Guide for Multiplatform Firmware

### OPTIONS Support in NAT Keep Alive Messages

The ATA supports the OPTIONS method in the NAT keep alive messages to maintain the current NAT mapping.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

### Outbound Fax Refinement

The ATA now supports maximum of two "m=" lines of the SDP packet. If enabled, the ATA can avoid the outbound FAX failure when
                        it receives multiple "m=" lines.

To enable this feature, use the fields FAX Enable T38 and FAX Passthru Method from Voice > Line (n) in the ATA administration web page.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Caveats

## Access Cisco Bug Search

Known problems (bugs) are graded according to severity level. These release notes contain descriptions of the following:

All severity level 1 or 2 bugs

Significant severity level 3 bugs

You can search for problems by using Cisco Bug Search.

Before you begin

### Before you begin

To access Cisco Bug Search, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Step 1

To access Cisco Bug Search, go to:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2(4)&sb=fr&sts=fd&svr=6nH&bt=custV&prdNam=Cisco%20Small%20Business%20IP%20Phones

Step 2

Log in with your Cisco.com user ID and password.

Step 3

To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter .

## View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

### Before you begin

To view caveats, you need the following items:

Cisco.com user ID and password

Step 1

Use this URL for all and resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2(4)&sb=fr&sts=fd&svr=6nH&bt=custV&prdNam=Cisco%20Small%20Business%20IP%20Phones

Step 2

When prompted, log in with your Cisco.com user ID and password.

Step 3

(Optional) Enter the bug ID number in the Search for field, then press Enter .

## Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco ATA 191 and 192 Analog Telephone Adapter
                     Multiplatform Phones for Firmware Release 11.2(4)

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                     You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                     was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

There are no open caveats in this release.

## Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco ATA 191 and 192 Analog Telephone
                     Adapter Multiplatform Phones for Firmware Release 11.2(4)

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                     You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                     report was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCwd39040 MPP ATA19X Not able to detect DTMF event duration short than 40ms

CSCwd82252 MPP ATA19x Two line registered to different proxy

CSCwd94502 ATA19x As MoH SAS Server will make parties hear each other and listen to MoH

CSCwf42615 ATA19x Random registration with the 2nd SBC

CSCwf91619 ATA19x Choppy Tx audio issue with firmware 11.2.3

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
| Step 4 | In the Latest Releases folder, choose 11.2.4 . |
| Step 5 | Download the file ATA19x.11-2-4MPP0001-115.zip. |
| Step 6 | Unzip the files. |
| Step 7 | Put the files on the TFTP/HTTP/HTTPS download directory. |
| Step 8 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is: <schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img Here is an example, http://192.168.1.100/firmware/ATA19x.11-2-4MPP0001-115.img After the firmware upgrade completes, the phone reboots automatically. |

| Step 1 | To access Cisco Bug Search, go to: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2(4)&sb=fr&sts=fd&svr=6nH&bt=custV&prdNam=Cisco%20Small%20Business%20IP%20Phones |
|---|---|
| Step 2 | Log in with your Cisco.com user ID and password. |
| Step 3 | To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . |

| Step 1 | Use this URL for all and resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2(4)&sb=fr&sts=fd&svr=6nH&bt=custV&prdNam=Cisco%20Small%20Business%20IP%20Phones |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |