---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7832-firmware-12-0-7sr3-cs78-b-7832mpp-rn-1207sr3-html-247fd7d10c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7832/firmware/12-0-7sr3/cs78_b_7832mpp-rn-1207sr3.html
retrieved_at: 2026-08-17T01:09:50.398820+00:00
---

Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 12.0(7)SR3

# Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 12.0(7)SR3

### Download Options

Updated: November 19, 2025

First Published: November 19, 2025

# Release Notes

Use these release notes with the Cisco IP Conference Phone 7832 Multiplatform Phones running SIP Firmware Release 12.0(7)SR3.

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Conference Phone 7832 Multiplatform Phones

BroadSoft BroadWorks RI

Asterisk 20

## Cisco IP Conference Phone 7832 Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation
                     URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/tsd-products-support-series-home.html

## New and Changed Features

### Support for TLS 1.3

With Firmware Release 12.0(7)SR3, the minimum TLS value of the phone is 1.3.

#### Where to Find More Information

Cisco IP Conference Phone Multiplatform Phone Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Enhance SSRC Reset for the new RTP and SRTP sessions

With Firmware Release 12.0(7)SR3, a new configuration SSRC Reset on Tx RE-INVITE is added to control whether to reset the RTP Tx SSRC when a phone sends an outgoing RE-INVITE. Hence, you can avoid the one-way
                        audio issue on a long duration call followed by a hold-resume action in certain Webex Calling environments where the SRTP
                        is end-to-end encrypted.

Meanwhile, the legacy configuration of SSRC Reset on RE-INVITE is now renamed to SSRC Reset on Rx RE-INVITE to avoid confusion. The corresponding XML parameter in the phone configuration file (cfg.xml) is updated to <SSRC_Reset_on_Rx_RE-INVITE>.
                        This parameter now controls whether to reset the RTP Tx SSRC on any incoming RE-INVITE.

#### Where to Find More Information

Cisco IP Conference Phone Multiplatform Phone Administration Guide

Cisco IP Desk Phone with Multiplatform Firmware (MPP) Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

## Upgrade the Firmware

The Cisco IP Conference Phone 7832 Multiplatform Phones support a single image upgrade using TFTP, HTTP, or HTTPS protocols with a URL.

After the firmware upgrade completes, the phone reboots automatically.

### SUMMARY STEPS

- Click the following URL:

- Select IP Phone 7800 Series with Multiplatform Firmware in the center pane.

- Select IP Conference Phone 7832 with Multiplatform Firmware in the right pane.

- Select the Multiplatform Firmware software type.

- Under All Release , select the MPP v12 > 12.0.7 folder.

- (Optional) Place your mouse pointer on the file name to display the file details and checksum values.

- Download the cmterm-7832.12-0-7MPP0301-92_REL.zip file.

- Click Accept License Agreement when you accept the software license.

- Unzip the firmware files.

- Put the files in the TFTP, HTTP, or HTTPS download directory.

- Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced > Voice > Provisioning tab, Firmware Upgrade section. In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

http://10.73.10.223/firmware/sip7832.12-0-7MPP0301-92.loads

https://server.domain.com/firmware/sip7832.12-0-7MPP0301-92.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

<phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL>

Load file URL format:

<upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads

Example:

http://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip7832.12-0-7MPP0301-92.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip7832.12-0-7MPP0301-92.loads

### DETAILED STEPS

Step 1

Click the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286311381&i=rm

Step 2

Select IP Phone 7800 Series with Multiplatform Firmware in the center pane.

Step 3

Select IP Conference Phone 7832 with Multiplatform Firmware in the right pane.

Step 4

Select the Multiplatform Firmware software type.

Step 5

Under All Release , select the MPP v12 > 12.0.7 folder.

Step 6

(Optional) Place your mouse pointer on the file name to display the file details and checksum values.

Step 7

Download the cmterm-7832.12-0-7MPP0301-92_REL.zip file.

Step 8

Click Accept License Agreement when you accept the software license.

Step 9

Unzip the firmware files.

Step 10

Put the files in the TFTP, HTTP, or HTTPS download directory.

Step 11

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced > Voice > Provisioning tab, Firmware Upgrade section. In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

http://10.73.10.223/firmware/sip7832.12-0-7MPP0301-92.loads

https://server.domain.com/firmware/sip7832.12-0-7MPP0301-92.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

<phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL>

Load file URL format:

<upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads

Example:

http://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip7832.12-0-7MPP0301-92.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip7832.12-0-7MPP0301-92.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

### Caveats

## View Caveats

You can search for caveats (bugs) with the Cisco Bug Search tool.

Known caveats are graded according to severity level, and are either open or resolved.

Before you begin

### Before you begin

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

## Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 7832 Multiplatform Phones that use Firmware Release 12.0(7)SR3.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in View Caveats .

CSCwf10956—Macro $SERVIP is not expanded in Log Request Msg in syslog.

CSCwb46008—Many PRTs with logs missing for around 5 seconds.

## Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 7832 Multiplatform Phones that use Firmware Release 12.0(7)SR3.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in View Caveats .

CSCwr83928—Unintended direct transfer to held calls occurs after a user cancels a transfer.

## Cisco IP Phone Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Requirements |
|---|---|
| Cisco IP Conference Phone 7832 Multiplatform Phones | BroadSoft BroadWorks RI Asterisk 20 |

| Step 1 | Click the following URL: https://software.cisco.com/download/navigator.html?mdfid=286311381&i=rm |
|---|---|
| Step 2 | Select IP Phone 7800 Series with Multiplatform Firmware in the center pane. |
| Step 3 | Select IP Conference Phone 7832 with Multiplatform Firmware in the right pane. |
| Step 4 | Select the Multiplatform Firmware software type. |
| Step 5 | Under All Release , select the MPP v12 > 12.0.7 folder. |
| Step 6 | (Optional) Place your mouse pointer on the file name to display the file details and checksum values. |
| Step 7 | Download the cmterm-7832.12-0-7MPP0301-92_REL.zip file. |
| Step 8 | Click Accept License Agreement when you accept the software license. |
| Step 9 | Unzip the firmware files. |
| Step 10 | Put the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 11 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced > Voice > Provisioning tab, Firmware Upgrade section. In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads Examples: http://10.73.10.223/firmware/sip7832.12-0-7MPP0301-92.loads https://server.domain.com/firmware/sip7832.12-0-7MPP0301-92.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<server ip address>[:<port>]>/<path>/<file name>.loads Example: http://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip7832.12-0-7MPP0301-92.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip7832.12-0-7MPP0301-92.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319849&rls=12.0(7)&sb=anfr&bt=custV To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319849&rls=12.0(7)&sb=anfr&sts=open&bt=custV To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319849&rls=12.0(7)&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |