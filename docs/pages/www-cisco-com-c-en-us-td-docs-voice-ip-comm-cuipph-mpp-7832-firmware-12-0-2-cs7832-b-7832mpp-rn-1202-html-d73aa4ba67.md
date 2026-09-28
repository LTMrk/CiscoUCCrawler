---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7832-firmware-12-0-2-cs7832-b-7832mpp-rn-1202-html-d73aa4ba67
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7832/firmware/12-0-2/cs7832_b_7832mpp-rn-1202.html
retrieved_at: 2026-08-21T23:17:11.841462+00:00
---

Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 12.0(2)

# Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 12.0(2)

### Download Options

Updated: May 15, 2023

First Published: May 15, 2023

# Release Notes

Use these release notes with the Cisco IP Conference Phone 7832 Multiplatform Phones running SIP Firmware Release 12.0(2).

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Conference Phone 7832 Multiplatform Phones

Cisco BroadWorks 24.0

MetaSphere CFS version 9.5

Asterisk 16.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Conference Phone 7832 Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation
                        URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/tsd-products-support-series-home.html

## New and Changed Features

### Configurable License Retry Timer for Authorization Failure

If an authorization operation to upgrade a license fails, the phone tries to authorize again after a time specified in seconds.
                        If the delay is set to 0, the device does not do the retry.

#### Where to Find More Information

Cisco IP Conference Phone Multiplatform Phone AdministrationGuide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Controlling the TLS Minimum Value

You can control the phone minimum value of TLS with the new TLS parameter.

To enable this feature from the phone administration web page, use the TLS Min Version parameter under the Security Settings from Voice > System .

#### Where to Find More Information

Cisco IP Conference Phone Multiplatform Phone AdministrationGuide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Digest Algorithms for Hoteling Subscription

Phone now support SHA-256, SHA512, and SHA 256 digest algorithms for hoteling authentication. Prior to release 12.0(2), phone
                        only has support for MD5 alogorithm.

#### Where to Find More Information

Cisco IP Conference Phone Multiplatform Phone AdministrationGuide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Enabling Phone Authorization with RFC-8760

You can enable the phone authorization with RFC8760.

To enable this feature from the phone administration web page, use the Auth Support RFC8760 parameter under the SIP Settings section from Voice > Ext (n) .

#### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones Administration Guide

### Enabling the Webex Metrics Services

With Metrics Enable, enable the phone control of all metric services.

To enable this feature from the phone administration web page, use the Metrics Enable parameter under the Webex section Voice > Phone .

#### Where to Find More Information

Cisco IP Conference Phone Multiplatform Phone AdministrationGuide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Enabling PRT Upload at Crash Services

You can indicate whether to automatically upload the PRT package to the server when the phone crashes.

To enable this feature from the phone administration web page, use the PRT Upload at Crash parameter under the Problem Reporting Tool section Voice > Provisioning

#### Where to Find More Information

Cisco IP Conference Phone Multiplatform Phone AdministrationGuide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Managing Participants List for Ad Hoc Conference

During an Ad Hoc conference, the host and the participants can show the participants list by pressing the Participants softkey on the phone. Also, both the host and the participants can add another person into the conference. However, only
                        the host is allowed to remove a participant from the participant list.

#### Where to Find More Information

Cisco IP Conference Phone 7832 Multiplatform Phones User Guide

Cisco IP Conference Phone Multiplatform Phone AdministrationGuide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

## Upgrade Firmware

Use the information in this section to upgrade the firmware on Cisco IP Conference Phone 7832 Multiplatform Phones .

The Cisco IP Phone 7811, 7821, 7841, and 7861 Multiplatform Phones have a different firmware image. For more information,
                     see the Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 12.0(2), at this location:

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

### SUMMARY STEPS

- Click this link:

- Select IP Conference Phone 7832 with Multiplatform Firmware in the right pane.

- On the next page that is displayed, select Multiplatform Firmware .

- On the next page that is displayed, select 12.0.2 in the All Releases > MPPv11 folder.

- (Optional) Place your mouse pointer on the file name to see the file details and checksum values.

- Download the cmterm-7832.12.0.2MPP0001.116.zip file.

- Click Accept License Agreement .

- Unzip the file and place the files in the appropriate location on your upgrade server.

- Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Example:

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Example:

https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip7832.12.0.2MPP0001.116.loads

### DETAILED STEPS

Step 1

Click this link:

https://software.cisco.com/download/home/286311381

On the Software Download web page that is displayed, ensure that IP Phone 7800 Series with Multiplatform Firmware is selected in the middle pane.

Step 2

Select IP Conference Phone 7832 with Multiplatform Firmware in the right pane.

Step 3

On the next page that is displayed, select Multiplatform Firmware .

Step 4

On the next page that is displayed, select 12.0.2 in the All Releases > MPPv11 folder.

Step 5

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Step 6

Download the cmterm-7832.12.0.2MPP0001.116.zip file.

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

Example:

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Example:

https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip7832.12.0.2MPP0001.116.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and, in some cases, can cause a call to drop. Sources of
                        network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

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

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 7832 Multiplatform Phones that use Firmware Release 12.0(2).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this
                        report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described
                        in View Caveats .

CSCwf10956 Macro $SERVIP is not expanded in Log Request Msg in syslog

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 7832 Multiplatform Phones that use Firmware Release 12.0(2).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                        this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                        as described in the View Caveats .

CSCwd81572 Specific tones are not heard on speaker phone, but can be heard on the handset

CSCwd51776 Virtual extention number is not provided on MPP with "webex directory" contact search

CSCwd61181 Cisco MPP Phones reboots upon receiving "GetSoftKeys" API calls

CSCwd41757 Cisco MPP phones: Call is disconnected during a call

CSCvb83904 MPP-78XX - phone's switch not change Cos value after extended Cos changes

## Cisco IP Phone Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Requirements |
|---|---|
| Cisco IP Conference Phone 7832 Multiplatform Phones | Cisco BroadWorks 24.0 MetaSphere CFS version 9.5 Asterisk 16.0 |

| Step 1 | Click this link: https://software.cisco.com/download/home/286311381 On the Software Download web page that is displayed, ensure that IP Phone 7800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select IP Conference Phone 7832 with Multiplatform Firmware in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | On the next page that is displayed, select 12.0.2 in the All Releases > MPPv11 folder. |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the cmterm-7832.12.0.2MPP0001.116.zip file. |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.73.10.223/firmware/sip7832.12.0.2MPP0001.116.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Example: https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip7832.12.0.2MPP0001.116.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319849&rls=12.0(2)&sb=anfr&bt=custV To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319849&rls=12.0(2)&sb=anfr&sts=open&bt=custV To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319849&rls=12.0(2)&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |