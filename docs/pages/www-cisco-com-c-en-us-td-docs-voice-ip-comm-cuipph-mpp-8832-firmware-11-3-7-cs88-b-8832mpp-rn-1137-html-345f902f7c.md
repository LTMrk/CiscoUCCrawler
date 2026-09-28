---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8832-firmware-11-3-7-cs88-b-8832mpp-rn-1137-html-345f902f7c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8832/firmware/11-3-7/cs88_b_8832mpp-rn-1137.html
retrieved_at: 2026-08-21T13:42:42.387994+00:00
---

Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 11.3(7)

# Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 11.3(7)

### Download Options

Updated: June 27, 2022

First Published: June 28, 2022

# Release Notes

Use these release notes with the Cisco IP Conference Phone 8832 Multiplatform Phones running SIP Firmware Release 11.3(7).

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Conference Phone 8832 Multiplatform Phones

Cisco BroadWorks 24.0

MetaSphere CFS version 9.5

Asterisk 16.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Conference Phone 8832 Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/index.html

## New and Changed Features

### HTTP Proxy Support

You can set up the phone to connect the Internet through a specified HTTP proxy server for security purposes. Your users can
                        also set up a proxy server on the phone LCD UI. You can set up the proxy server by one of the proxy modes: Auto and Manual.

To enable this feature, you configure the parameters under the HTTP Proxy Settings section from Voice > System on the phone web interface.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### LDAP Search Enhancement

You can enable the unified search in the LDAP directory. The search allows you to enter any value as filters. You can search
                        with first name, last name, extension, or phone number. The phone transfers the request as a single search request.

To enable this feature from the phone administration web page, use the Unified Search Enable parameter under the LDAP section from Voice > Phone .

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

### Login Credential for the Call Statistics Menu

Your phone has enhanced security for access to the Call statistics menu. If the user password is set, the users will be prompted to enter the password when they try to access the menu, in
                        order to view the details of the recent calls.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

### Spam Indication of Incoming Calls on the Phones

This release supports the new technology standard Secure Telephony Identity Revisited (STIR) and Signature-based Handling
                        of Asserted information using toKENs (SHAKEN) for the Webex call logs, local call logs, and local call sessions when the phone
                        is in Webex enviroment. STIR/SHAKEN has been mandated by Federal Communications Commission (FCC). These standards define procedures
                        to authenticate and verify caller identification for calls carried over the IP network. The STIR-SHAKEN framework is developed
                        to provide the end user with a great degree of identification and control over the type of calls they receive. These sets
                        of standards are intended to provide a basis for verifying calls, classifying calls, and facilitating the ability to trust
                        caller identity end to end. Illegitimate callers can easily be identified.

When STIR/SHAKEN support is implemented on the Webex server, the phone displays an extra icon next to the caller ID based
                        on the caller's STIR/SHAKEN verification result.

Based on the verification result, the phone displays three types of icons.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

## Upgrade Overview

The upgrade procedure is different according to the current phone firmware version.

If the current phone firmware is 11.3(1) SR3 or later, see Upgrade the Firmware from a version after 11.3(1) SR3 .

If the current phone firmware is 11.3(1) SR2 or earlier, see Upgrade the Firmware from a Version before 11.3(1) SR2 .

### Upgrade the Firmware from a version after 11.3(1) SR3

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

The phone firmware supports the following upgrade paths:

From 11.3(1) SR3 to 11.3(7)

From 11.3(2) to 11.3(7)

From 11.3(3) to 11.3(7)

From 11.3(4) to 11.3(7)

From 11.3(5) to 11.3(7)

From 11.3(6) to 11.3(7)

Click this link:

https://software.cisco.com/download/home/286311392

On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane.

Select IP Conference Phone 8832 with Multiplatform Firmware in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

On the next page that is displayed, select 11.3.7 in the All Releases > MPPv11 folder.

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Download the cmterm-8832.11-3-7MPP0001.272_REL.zip file.

Click Accept License Agreement .

Unzip the file and place the files in the appropriate location on your upgrade server.

The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                    upgrade.

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<file name>.loads

Examples:

http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads

https://server.domain.com/sip8832.11-3-7MPP0001.272.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]/<file name>.loads

Examples:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.11-3-7MPP0001.272.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

### Upgrade the Firmware from a Version before 11.3(1) SR2

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

Before you begin

#### Before you begin

If the current phone firmware is one of the following versions, you must first upgrade the phone firmware to 11.3(1) SR2.

11.2(3)

11.2(3) SR1

11.3.1

11.3(1) SR1

For more information, see Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 11.3(1)SR2 .

Click this link:

https://software.cisco.com/download/home/286311392

On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane.

Select IP Conference Phone 8832 with Multiplatform Firmware in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

Under Latest Release , select 11.3.7 .

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Download the corresponding file.

cmterm-8832.11-3-7MPP0001.272_REL.zip

Click Accept License Agreement .

Unzip the file and place the files in the appropriate location on your upgrade server.

The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                    upgrade.

If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server.

Example:

http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads

If the file is placed under a non-root directory of the upgrade server, the upgrade fails.

Example:

http://10.73.10.223/firmware/sip8832.11-3-7MPP0001.272.loads

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<file name>.loads

Examples:

http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads

https://server.domain.com/sip8832.11-3-7MPP0001.272.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]/<file name>.loads

Examples:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.11-3-7MPP0001.272.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and, in some cases, can cause a call to drop. Sources of
                        network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

Caveats

## View Caveats

You can search for caveats (bugs) with the Cisco Bug Search tool.

Known caveats are graded according to severity level, and are either open or resolved.

Before you begin

### Before you begin

Click one of the following links:

To view all caveats that affect this release:

To view open caveats that affect this release:

To view resolved caveats that affect this release:

When prompted, log in with your Cisco.com user ID and password.

(Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

## Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 8832 Multiplatform Phones that use Firmware Release 11.3(7).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this
                     report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described
                     in View Caveats .

CSCvx44952 Phone showing Failed to download configurations even when it was successful while migrating to MPP

CSCvx49825 Phone stuck at configuration check in progress during firmware migration if it was on WiFi before

CSCvx78045 Add "PoE Power Required" parameter definitions to 8800 MPP administration guide

CSCvz35920 SSRC changes for outgoing Re-INVITES

CSCvz67625 License prompt is always displayed on GDS input screen if the phone is converted from On-Premises

CSCwb46008 Many PRTs with logs missing for around 5 seconds

## Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 8832 Multiplatform Phones that use Firmware Release 11.3(7).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCwb54978 CiscoIPPhoneStatus and CiscoIPPhoneStatusFile object is not mirrored in RTL mode

CSCwb31031 Voicemail pin locked after unsuccessful login attempt by Hoteling Guest

CSCwb23631 In German, department and email for directory are both displayed incorrectly

CSCwa70835 When g722 is negotiated, the callee hears himself and the caller gets no audio

CSCwa70820 MPP phones - Incorrect date and time in Recents page

CSCwa95349 Cloud awareness: Phone will create new registration after reboot or for each refresh request

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Phone | Support Requirements |
|---|---|
| Cisco IP Conference Phone 8832 Multiplatform Phones | Cisco BroadWorks 24.0 MetaSphere CFS version 9.5 Asterisk 16.0 |

| Step 1 | Click this link: https://software.cisco.com/download/home/286311392 On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select IP Conference Phone 8832 with Multiplatform Firmware in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | On the next page that is displayed, select 11.3.7 in the All Releases > MPPv11 folder. |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the cmterm-8832.11-3-7MPP0001.272_REL.zip file. |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                    upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<file name>.loads Examples: http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads https://server.domain.com/sip8832.11-3-7MPP0001.272.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address>[:<port>]/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]/<file name>.loads Examples: https://10.74.10.225/admin/upgrade?http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.11-3-7MPP0001.272.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click this link: https://software.cisco.com/download/home/286311392 On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select IP Conference Phone 8832 with Multiplatform Firmware in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | Under Latest Release , select 11.3.7 . |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the corresponding file. cmterm-8832.11-3-7MPP0001.272_REL.zip |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                    upgrade. Note If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server. Example: http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads If the file is placed under a non-root directory of the upgrade server, the upgrade fails. Example: http://10.73.10.223/firmware/sip8832.11-3-7MPP0001.272.loads | Note | If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server. Example: http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads If the file is placed under a non-root directory of the upgrade server, the upgrade fails. Example: http://10.73.10.223/firmware/sip8832.11-3-7MPP0001.272.loads |
| Note | If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server. Example: http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads If the file is placed under a non-root directory of the upgrade server, the upgrade fails. Example: http://10.73.10.223/firmware/sip8832.11-3-7MPP0001.272.loads |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<file name>.loads Examples: http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads https://server.domain.com/sip8832.11-3-7MPP0001.272.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address>[:<port>]/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]/<file name>.loads Examples: https://10.74.10.225/admin/upgrade?http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.11-3-7MPP0001.272.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server. Example: http://10.73.10.223/sip8832.11-3-7MPP0001.272.loads If the file is placed under a non-root directory of the upgrade server, the upgrade fails. Example: http://10.73.10.223/firmware/sip8832.11-3-7MPP0001.272.loads |
|---|---|

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&rls=11.3(7)&sb=anfr&bt=custV To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&rls=11.3(7)&sb=anfr&sts=open&bt=custV To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&rls=11.3(7)&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |