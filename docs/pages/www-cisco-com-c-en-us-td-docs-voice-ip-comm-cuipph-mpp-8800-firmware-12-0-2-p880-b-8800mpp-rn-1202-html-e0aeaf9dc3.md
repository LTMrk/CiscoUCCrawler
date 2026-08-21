---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-firmware-12-0-2-p880-b-8800mpp-rn-1202-html-e0aeaf9dc3
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/firmware/12-0-2/p880_b_8800mpp-rn-1202.html
retrieved_at: 2026-08-21T13:45:46.685340+00:00
---

Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 12.0(2)

# Cisco IP Phone 8800 Series Multiplatform Phones Release Notes for Firmware Release 12.0(2)

### Download Options

Updated: May 15, 2023

First Published: May 15, 2023

Last Updated: May 15, 2023

# Release Notes

Use these release notes with the Cisco IP Phone 8800 Series Multiplatform Phones running SIP Firmware Release 12.0(2).

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 8800 Series Multiplatform Phones

BroadSoft BroadWorks 24.0

MetaSphere CFS version 9.5

Asterisk 16.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone 8800 Series Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/index.html

## New and Changed Features

### Configurable License Retry Timer for Authorization Failure

If an authorization operation to upgrade a license fails, the phone tries to authorize again after a time specified in seconds.
                        If the delay is set to 0, the device does not do the retry.

#### Where to Find More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Controlling the TLS Minimum Value

You can control the phone minimum value of TLS with the new TLS parameter.

To enable this feature from the phone administration web page, use the TLS Min Version parameter under the Security Settings from Voice > System .

#### Where to Find More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Digest Algorithms for Hoteling Subscription

Phone now support SHA-256, SHA512, and SHA 256 digest algorithms for hoteling authentication. Prior to release 12.0(2), phone
                        only has support for MD5 alogorithm.

#### Where to Find More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Enabling Phone Authorization with RFC-8760

You can enable the phone authorization with RFC8760.

To enable this feature from the phone administration web page, use the Auth Support RFC8760 parameter under the SIP Settings section from Voice > Ext (n) .

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Enabling the Webex Metrics Services

With Metrics Enable, enable the phone control of all metric services.

To enable this feature from the phone administration web page, use the Metrics Enable parameter under the Webex section Voice > Phone .

#### Where to Find More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Enabling PRT Upload at Crash Services

You can indicate whether to automatically upload the PRT package to the server when the phone crashes.

To enable this feature from the phone administration web page, use the PRT Upload at Crash parameter under the Problem Reporting Tool section Voice > Provisioning

#### Where to Find More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Enhancements in Hybrid Meetings Functionalities

Hybrid meeting functionalities have enhancements with the release 12.0(2). The following enhancements are implemented:

Display of participants list and the participants status.

Display of meeting recording status on the phone, such as recording and pause recording.

Participants can mute or unmute themselves with softkey, hardkey, and headset. Also, mute and unmute status synchronizes with
                              server side.

Participants can mute or unmute video either with camera shutter or sofkeys.

Participants can join as a host or a guest and use PIN to join the hybrid meeting if the meeting is configured to be accessed
                              only through a PIN.

Shared line call retrieve while in a Webex meeting

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

### Managing Participants List for Ad Hoc Conference

During an Ad Hoc conference, the host and the participants can show the participants list by pressing the Participants softkey on the phone. Also, both the host and the participants can add another person into the conference. However, only
                        the host is allowed to remove a participant from the participant list.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Synchronizing Mute or Unmute with Phone and Bluetooth Headset

Both the headset and the phone will sync their muted status. When the current call on the phone is active and the audio path
                        is headset.

The phone will be forced to mute if the headset is forced to be muted.

The mute status of the headset will match that of the phone if it is not forced to be muted.

With the special requirement that the current call is active and the audio path is the headset, this function synchronizes
                        the mute/unmute status between the phone and the headset.

The scope that supports this feature is listed in the following table:

Phone model

8845,8865,8851.8861

Phone version

12.0.2 and newer

Headset

Cisco 720 and 730 series

Headset version

All headset version do support mute or unmute sync, but only 1-12 version and newer will support force mute.

This feature is not supported by non-Cisco headsets.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

## Upgrade Firmware

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

### SUMMARY STEPS

- Click this link:

- Select your phone model in the right pane.

- On the next page that is displayed, select Multiplatform Firmware .

- On the next page that is displayed, select 12.0.2 in the All Releases > MPPv11 folder.

- (Optional) Place your mouse pointer on the file name to see the file details and checksum values.

- Download the corresponding file.

- Click Accept License Agreement .

- Unzip the file and place the files in the appropriate location on your upgrade server.

- Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

8845 and 8865:

http://10.73.10.223/firmware/sip8845_65.12.0.2MPP0001.116.loads

https://server.domain.com/firmware/sip8845_65.12.0.2MPP0001.116.loads

Other phones in 8800 series:

http://10.73.10.223/firmware/sip88xx.12.0.2MPP0001.116.loads

https://server.domain.com/firmware/sip88xx.12.0.2MPP0001.116.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

8845 and 8865:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip8845_65.12.0.2MPP0001.116.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8845_65.12.0.2MPP0001.116.loads

Other phones in 8800 series:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip88xx.12.0.2MPP0001.116.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip88xx.12.0.2MPP0001.116.loads

### DETAILED STEPS

Step 1

Click this link:

https://software.cisco.com/download/home/286318380

On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane.

Step 2

Select your phone model in the right pane.

Step 3

On the next page that is displayed, select Multiplatform Firmware .

Step 4

On the next page that is displayed, select 12.0.2 in the All Releases > MPPv11 folder.

Step 5

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Step 6

Download the corresponding file.

8845 and 8865: cmterm-8845_65.12.0.2MPP0001.116_REL.zip

Other phones in 8800 series: cmterm-88xx.12.0.2MPP0001.116_REL.zip

Step 7

Click Accept License Agreement .

Step 8

Unzip the file and place the files in the appropriate location on your upgrade server.

The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade.

Step 9

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

8845 and 8865:

http://10.73.10.223/firmware/sip8845_65.12.0.2MPP0001.116.loads

https://server.domain.com/firmware/sip8845_65.12.0.2MPP0001.116.loads

Other phones in 8800 series:

http://10.73.10.223/firmware/sip88xx.12.0.2MPP0001.116.loads

https://server.domain.com/firmware/sip88xx.12.0.2MPP0001.116.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

8845 and 8865:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip8845_65.12.0.2MPP0001.116.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8845_65.12.0.2MPP0001.116.loads

Other phones in 8800 series:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip88xx.12.0.2MPP0001.116.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip88xx.12.0.2MPP0001.116.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and, in some cases, can cause a call to drop. Sources of
                        network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

## Caveats

### View Caveats

You can search for caveats (bugs) with the Cisco Bug Search tool.

Known caveats are graded according to severity level, and are either open or resolved.

Before you begin

#### Before you begin

You have your Cisco.com user ID and password.

### SUMMARY STEPS

- Click one of the following links:

- When prompted, log in with your Cisco.com user ID and password.

- (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

### DETAILED STEPS

Step 1

Click one of the following links:

To view all caveats that affect this release:

To view open caveats that affect this release:

To view resolved caveats that affect this release:

Step 2

When prompted, log in with your Cisco.com user ID and password.

Step 3

(Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 8800 Series Multiplatform Phones that use Firmware Release 12.0(2).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                        this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                        as described in the View Caveats .

CSCvy86354: MPP phones - 8845/8865 phones are randomly crashing.

CSCwb27243: 8865 Crash - null pointer at libmmalvcp.so

CSCwe55809: Personal contact calls play the distinctive ring while there's an active call on 8800 phones.

CSCwf24915: 8865 no video since srtpm_srtpifUnprotect failure after hold resume several times

CSCwf30157: Video phone: Camera led may be off in ad-hoc conference call

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 8800 Series Multiplatform Phones that use Firmware Release 12.0(1).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                        this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                        as described in the View Caveats .

CSCwc61284: SSH is not available for phones running Multiplatform Phone (MPP) firmware.

CSCwd01853: Cisco MPP Phones reboots when park and retrieve a call too fast.

CSCwc29314: MPP phones (88xx/68xx/78xx) do not support dual registration with TCP.

CSCwd62034: AWR-WB Media Type does not conform to RFC4867.

CSCwd93487: 8851 KEM Memory leak causing reboot

CSCvb65980: Nav hard key can't move cursor in Search Enterprise Directory.

CSCwb85883: 88xx 88x5 the generated PRT toast content will overlap when a paging call is received.

CSCwa95349: Cloud awareness: Phone will create new registration after reboot or for each refresh request

CSCwd47209: The 'ACK' from MPP phone does not have 'Route' header.

CSCwd56139: Cisco MPP phones "Debug" level log still print out when log level set to "Notice"

CSCwd62809: Intermittent audio noises are heard on Webex calls

CSCwe27819: Vulnerabilities in linux-kernel - multiple versions CVE-2016-0821

CSCwe67157: Vulnerabilities in linux-kernel - multiple versions CVE-2023-26545

CSCwe01828: Vulnerabilities in linux-kernel - multiple versions CVE-2021-4037

CSCwe24803: Vulnerabilities in linux-kernel 4.9.118 CVE-2022-3643

CSCwe38474: Held calls cannot resume on 8845/8865

CSCwe46781: MPP 8865/8861 External Audio Output does not work after upgrade to 12.0.1

CSCwc08931: Cisco MPP 8851 IP Phone with Cisco 561 USB headset are randomly crashing

CSCwb65913: ICE: Phone becomes not operational when Media ports are not getting released

CSCwd86078: Vulnerabilities in u-boot - multiple versions CVE-2022-34835 cmd_i2c.c

CSCwe86166: 'Transfer' softkey in the Connected Key List is not working in 11.3.5 or later releases

CSCwe46272: MPP 12.x not properly optimizing media via ICE on calls to LGW

CSCwe46781: MPP 8865/8861 External Audio Output does not work after upgrade to 12.0.1

CSCwf17564: MPP - 8851 Phone Lag/Freeze on 12.0.1 Firmware

CSCwf23858: Selfview frozen for user in a 1:1 call

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 8800 Series Multiplatform Phones | BroadSoft BroadWorks 24.0 MetaSphere CFS version 9.5 Asterisk 16.0 |

| Phone model | 8845,8865,8851.8861 |
|---|---|
| Phone version | 12.0.2 and newer |
| Headset | Cisco 720 and 730 series |
| Headset version | All headset version do support mute or unmute sync, but only 1-12 version and newer will support force mute. |

| Note | This feature is not supported by non-Cisco headsets. |
|---|---|

| Step 1 | Click this link: https://software.cisco.com/download/home/286318380 On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select your phone model in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | On the next page that is displayed, select 12.0.2 in the All Releases > MPPv11 folder. |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the corresponding file. 8845 and 8865: cmterm-8845_65.12.0.2MPP0001.116_REL.zip Other phones in 8800 series: cmterm-88xx.12.0.2MPP0001.116_REL.zip |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: 8845 and 8865: http://10.73.10.223/firmware/sip8845_65.12.0.2MPP0001.116.loads https://server.domain.com/firmware/sip8845_65.12.0.2MPP0001.116.loads Other phones in 8800 series: http://10.73.10.223/firmware/sip88xx.12.0.2MPP0001.116.loads https://server.domain.com/firmware/sip88xx.12.0.2MPP0001.116.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: 8845 and 8865: https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip8845_65.12.0.2MPP0001.116.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8845_65.12.0.2MPP0001.116.loads Other phones in 8800 series: https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip88xx.12.0.2MPP0001.116.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip88xx.12.0.2MPP0001.116.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=12.0(2)&sb=anfr&bt=custV&prdNam=Cisco%20IP%20Phone%208800%20Series%20with%20Multiplatform%20Firmware To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=12.0(2)&sb=afr&bt=custV&prdNam=Cisco%20IP%20Phone%208800%20Series%20with%20Multiplatform%20Firmware To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&rls=12.0(2)&sb=fr&bt=custV&prdNam=Cisco%20IP%20Phone%208800%20Series%20with%20Multiplatform%20Firmware |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |