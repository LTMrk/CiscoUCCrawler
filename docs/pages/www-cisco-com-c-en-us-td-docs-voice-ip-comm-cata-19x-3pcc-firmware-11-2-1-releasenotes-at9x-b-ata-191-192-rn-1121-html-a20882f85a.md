---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-firmware-11-2-1-releasenotes-at9x-b-ata-191-192-rn-1121-html-a20882f85a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/firmware/11-2-1/releasenotes/at9x_b_ata-191_192-rn-1121.html
retrieved_at: 2026-08-21T12:50:33.997721+00:00
---

Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.2(1)

# Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.2(1)

### Download Options

Updated: July 11, 2021

First Published: July 15, 2021

# Release Notes

These release notes support the Cisco ATA 191 and 192 Analog Telephone Adapter for Multiplatform Firmware Release 11.2(1).

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

## Installation

### Upgrade Firmware

The Cisco ATA 191 and 192 support dual image upgrades by TFTP, HTTP, or HTTPS.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286282490&flowid=83468

Choose Cisco ATA 190 Series Analog Telephone Adapters .

Choose your ATA model.

In the Latest Releases folder, choose 11.2.1 .

Download the file ATA19x.11-2-1MPP0001-006.zip.

Unzip the files.

Put the files on the tftp/http/https download directory.

Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is:

<schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img

Here is an example,

http://192.168.1.100/firmware/ATA19X.11-2-1MPP0001-006.img

After the firmware upgrade completes, the phone reboots automatically.

## New and Changed

### E911 Geolocation Service

#### E911 Geolocation Service

You can register each IP-based phone with an emergency call service provider by supplying the E911 Geolocation information.
                        Registration obtains the location of the analog phone that connects to the ATA. The location can specify the street address,
                        building number, floor, room, and other office location information. When you dial an emergency number, the emergency service
                        receives the phone location and a call-back number. If an emergency call disconnects, the emergency service uses the call-back
                        number to reconnect to the caller.

To configure this feature, use the parameters under the E911 Geolocation Configuration section from Voice > Line (n) of the ATA administration web page.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter User Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

### Remotely Intiated Problem Reports

You can initiate a problem report remotely. To do this, initiate a SIP-NOTIFY message from the server to the ATA, with the Event specified as prt-gen .

When the ATA receives the notification, it generates a PRT and sends it to the specified server when you set the parameter PRT Upload URL . The notification is in the form of a SIP message, and the PRT is transmitted over the HTTP and HTTPS protocol.

You can access a remotely-initiated problem report from the same location as locally-initiated problem reports on the administration
                        web page.

This feature has no user impact.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

### Reporting End-of-Call Statistics in SIP BYE and SIP ReINVITE Messages

This feature enables you to send call statistics to a remote end when a call terminates or is on hold. The statistics include
                        Real-time Transport Protocol (RTP) packets sent or received, total bytes sent or received, total number of packets that are
                        lost, delay jitter, round-trip delay, and call duration. Thus it helps the server to collect audio quality data.

When a call terminates, the SIP BYE message appends headers such as RTP-RxStat, RTP-TxStat for audio session.

The call statistics are sent as a new header in the BYE message or in the 200 OK message (response to BYE message).

When a call is on hold, headers RTP-RxStat, RTP-TxStat are sent in the Re-Invite SIP message.

When a call is put on hold, in the 200OK for this Re-Invite headers RTP-RxStat, RTP-TxStat are sent.

#### Where to Get More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

### Serviceability Enhancements

#### New Log Modules Support for Audio Issues

You can enable the debug logging for the audio related issues. After you enable the audio debug logging, you can track what
                        happened and troubleshoot audio related issues according to Real-time Transport Protocol (RTP), facsimile (Fax), and the voice
                        related messages.

To enable the specific log modules, use the CSSD_RTP , CSSD_FAX , or CSSD_ANY fields from the Administrator > Log > Debug Log Module page.

#### Where to Find More Information

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Administration Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter User Guide for Multiplatform Firmware

Cisco ATA 191 and ATA 192 Analog Telephone Adapter Provisioning Guide for Multiplatform Firmware

## Caveats

### Access Cisco Bug Search

Known problems (bugs) are graded according to severity level. These release notes contain descriptions of the following:

All severity level 1 or 2 bugs

Significant severity level 3 bugs

You can search for problems by using Cisco Bug Search.

Before you begin

#### Before you begin

To access Cisco Bug Search, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

To access Cisco Bug Search, go to:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=274259360&rls=11.2(1)&sb=anfr&sts=fd&svr=6nH&bt=custV

Log in with your Cisco.com user ID and password.

To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter .

### View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

#### Before you begin

To view caveats, you need the following items:

Cisco.com user ID and password

Use this URL for all and resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=274259360&rls=11.2(1)&sb=fr&sts=fd&svr=6nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

This release for Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones does not have any open caveats.

### Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco ATA 191 and 192 Analog Telephone
                        Adapter Multiplatform Phones for Firmware Release 11.2(1)

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCvx05795: MPP ATA19x - Can not make call for some time

CSCvx05785: MPP ATA19x - No audio on either side due to RTP start failure

CSCvx94262: ATA19x intermittent one-way and big noise audio during call

CSCvw73093: MPP ATA19x - Setting TR69 Parameters with empty string values will result in TR069 server disconnect

CSCvw60654: ATA19x should not send AAAA dns query for IPV4 only case

CSCvw56885: ATA19x flooding DNS requests

CSCvx28351: ATA19x enter restart loop due to domain name can not be provisioned

CSCvx75578: MPP ATA19x unexpected reboot due to kernel tick error

CSCvx75523: ATA19x Firmware download error for http server chunk mode

CSCvx63611: ATA19x initial connection removed for no UserID scenario to avoid multiple TCP connection attempts

CSCvx63566: ATA19x lost IP address when it is idle

CSCvx48193: Evaluation of 3pcc-ata19x for Web UI Privilege Escalation and Command Injection

CSCvx61614 - MPP ATA19x certificate issue during provisioning due to NTP time response delay

CSCvy30310: ATA19x MPP does not include MAC in the certificate it supplies for HTTPS PRT uploading

CSCvy11161: ATA19x MPP provides no "User-Agent" header for HTTP PRT uploading

CSCvy05269: ATA19x MPP provides no TLS certificate for HTTPS PRT uploading

CSCvy06654: MPP ATA19x needs to recover in case TCP/SSL handshake is stuck

CSCvx65307: ATA19x does not send correct caller ID or call waiting caller ID signaling to UK analog phones

CSCvy50632: MPP ATA19x cannot register with static SRV outbound proxy configuration

CSCvw22570: ATA19x will lose wan IP after icmpsic flooding attack. PSIRT-0739134501

CSCvx61614: Certificate handling enhancement during provisioning with NTP server response time delay

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco ATA 191 and 192 | SIP | BroadSoft BroadWorks 24.0 Asterisk 13.1 |

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=286282490&flowid=83468 |
|---|---|
| Step 2 | Choose Cisco ATA 190 Series Analog Telephone Adapters . |
| Step 3 | Choose your ATA model. |
| Step 4 | In the Latest Releases folder, choose 11.2.1 . |
| Step 5 | Download the file ATA19x.11-2-1MPP0001-006.zip. |
| Step 6 | Unzip the files. |
| Step 7 | Put the files on the tftp/http/https download directory. |
| Step 8 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is: <schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img Here is an example, http://192.168.1.100/firmware/ATA19X.11-2-1MPP0001-006.img After the firmware upgrade completes, the phone reboots automatically. |

| Step 1 | To access Cisco Bug Search, go to: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=274259360&rls=11.2(1)&sb=anfr&sts=fd&svr=6nH&bt=custV |
|---|---|
| Step 2 | Log in with your Cisco.com user ID and password. |
| Step 3 | To look for information about a specific problem, enter the bug ID number in the Search for field, then press Enter . |

| Step 1 | Use this URL for all and resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=274259360&rls=11.2(1)&sb=fr&sts=fd&svr=6nH&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |