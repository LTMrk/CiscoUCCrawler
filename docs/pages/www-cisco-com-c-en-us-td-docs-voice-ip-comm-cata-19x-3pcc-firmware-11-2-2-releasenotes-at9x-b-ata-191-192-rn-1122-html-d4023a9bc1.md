---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-firmware-11-2-2-releasenotes-at9x-b-ata-191-192-rn-1122-html-d4023a9bc1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/firmware/11-2-2/releasenotes/at9x_b_ata-191_192-rn-1122.html
retrieved_at: 2026-08-21T12:50:26.074122+00:00
---

Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.2(2)

# Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.2(2)

### Download Options

Updated: March 22, 2022

First Published: March 23, 2022

# Release Notes

These release notes support the Cisco ATA 191 and 192 Analog Telephone Adapter for Multiplatform Firmware Release 11.2(2).

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

## Upgrade the Firmware

The Cisco ATA 191 and 192 support dual image upgrades by TFTP, HTTP, or HTTPS.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286282490&flowid=83468

Choose Cisco ATA 190 Series Analog Telephone Adapters .

Choose your ATA model.

In the Latest Releases folder, choose 11.2.2 .

Download the file ATA19x.11-2-2MPP0001-011.zip.

Unzip the files.

Put the files on the tftp/http/https download directory.

Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is:

<schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img

Here is an example,

http://192.168.1.100/firmware/ATA19x.11-2-2MPP0001-011.img

After the firmware upgrade completes, the phone reboots automatically.

## New and Changed Features

### DNS NAPTR Support

You can use the Name Authority Pointer (NAPTR) to allow the ATA to automatically determine and select the appropriate transport
                        protocol for the Line 1 and Line 2 (PHONE 1 and PHONE 2).

To enable this feature, use the SIP Transport field under the SIP Settings section from Voice > Line (n) of the ATA administration web page. Set the value of the field to AUTO .

When you enable the feature, the line determines the protocol based on the NAPTR records on the DNS server. The ATA uses the
                        protocol specified in the record that has the lowest order and preference value. When there are multiple records with the
                        same order and preference value, the ATA looks for a protocol within the records, in the following order of preference: UDP,
                        TCP, and TLS. The ATA uses the highest priority protocol that it finds in a record.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

### Secure Line Setup

You can configure a line to only accept secure calls. If the line is configured to only accept secure calls, then any calls
                        the line makes will be secure. You can configure to automatically select RTP or SRTP based on the transport. If SIP transport
                        is set to TLS, the ATA automatically chooses SRTP, else the ATA chooses RTP.

To enable this feature, use the Secure Call Option under the Call Feature Settings section from Voice > Line (n) of the ATA administration web page.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

### SIP Proxy Redundancy Enhancement

The SIP Proxy Redundancy enhancements are:

Increase support for up to 6 NAPTR records and 12 SRV records in a DNS query

Add ability to seamless switch between different SIP transport protocols during server failover and failback

Add ability to disable SIP proxy failback. Set the Proxy Fallback Intvl parameter to 0 in the ATA administration web page.

Retain an active call on the fallback server until after the call completes. After the call completes, if the primary server
                              is available and the failback conditions are met, then perform the failback.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

### Support Maximum of 12 SRV Records in a Query

The maximum number of the DNS SRV records supported in a query increases from 5 to 12.

Before the 11.2(2) release, the maximum number of the DNS SRV records is 5.

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

To access Cisco Bug Search, go to:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2(2)&sb=fr&sts=fd&svr=6nH&bt=custV&prdNam=Cisco%20Small%20Business%20IP%20Phones

Log in with your Cisco.com user ID and password.

To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter .

## View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

### Before you begin

To view caveats, you need the following items:

Cisco.com user ID and password

Use this URL for all and resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2(2)&sb=fr&sts=fd&svr=6nH&bt=custV&prdNam=Cisco%20Small%20Business%20IP%20Phones

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

## Open Caveats

The following list contains severity 1, 2, and 3 defects that are open for the Cisco ATA 191 and 192 Analog Telephone Adapter
                     Multiplatform Phones for Firmware Release 11.2(2)

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                     You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                     was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCvy79547 In bridge mode, LAN PC cannot get IP from data VLAN DHCP server

## Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco ATA 191 and 192 Analog Telephone
                     Adapter Multiplatform Phones for Firmware Release 11.2(2)

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                     You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                     report was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCvz87809 Screeching noise during call waiting caller ID displaying

CSCvz81377 Call Waiting and Call Waiting with Caller ID tones leak to the far end

CSCvy80730 DTMF tone keeps playing when off-hook if the previous call hangs up before tone stops

CSCwa06244 DTMF doesn't work when payload type is 100

CSCwa61593 MPP ATA19X call waiting tone can not be configured on web

CSCvz93493 CDP/LLDP heap Overflow and more vulnerabilities

CSCwa24842 Cisco ATA 19x Memory Leak

CSCwa24844 Cisco ATA 19x Out-of-Bounds Read

CSCwa51151 MPP ATA19X CVE-2019-20054: Linux kernel NULL pointer dereference issue

CSCwa51158 MPP ATA19X CVE-2019-19066: Linux kernel memory leak issue

CSCwa51162 MPP ATA19X CVE-2019-19252: Linux kernel does not prevent write access issue

CSCvw92006 MPP ATA19X CVE-2017-10661: Linux kernel use-after-free vulnerability

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
| Step 4 | In the Latest Releases folder, choose 11.2.2 . |
| Step 5 | Download the file ATA19x.11-2-2MPP0001-011.zip. |
| Step 6 | Unzip the files. |
| Step 7 | Put the files on the tftp/http/https download directory. |
| Step 8 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is: <schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img Here is an example, http://192.168.1.100/firmware/ATA19x.11-2-2MPP0001-011.img After the firmware upgrade completes, the phone reboots automatically. |

| Step 1 | To access Cisco Bug Search, go to: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2(2)&sb=fr&sts=fd&svr=6nH&bt=custV&prdNam=Cisco%20Small%20Business%20IP%20Phones |
|---|---|
| Step 2 | Log in with your Cisco.com user ID and password. |
| Step 3 | To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . |

| Step 1 | Use this URL for all and resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=11.2(2)&sb=fr&sts=fd&svr=6nH&bt=custV&prdNam=Cisco%20Small%20Business%20IP%20Phones |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |