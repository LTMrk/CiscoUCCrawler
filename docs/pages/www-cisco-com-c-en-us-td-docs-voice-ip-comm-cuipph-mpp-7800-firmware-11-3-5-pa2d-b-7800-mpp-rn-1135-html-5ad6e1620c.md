---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-firmware-11-3-5-pa2d-b-7800-mpp-rn-1135-html-5ad6e1620c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/firmware/11-3-5/pa2d_b_7800-mpp-rn-1135.html
retrieved_at: 2026-08-21T23:19:17.365909+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.3(5)

# Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.3(5)

### Download Options

Updated: September 16, 2021

First Published: September 9, 2021

# Release Notes

Use these release notes with the Cisco IP Phone 7800 Series Multiplatform Phones running SIP Firmware Release 11.3(5).

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 7800 Series Multiplatform Phones

BroadSoft BroadWorks 24.0

MetaSphere CFS version 9.5

Asterisk 16.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone 7800 Series Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/index.html

## New and Changed Features

### 7841 New H/W Disallows Downgrade

Cisco IP Phone 7841 multiplatform phone with new hardware version 41 and later and virtual ID (VID) 18 and above cannot be
                        downgraded to the MPP firmware version older than 11.3(5). Also, it cannot be migrated to the Enterprise firmware version
                        older than 14.0(1).

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 7800 and 8800 Series Migration Guide (Multiplatform Phones to On-Premises)

### Keep Focus on the Active Call

You can set up the phone to ensure that the active call is still in focus on the phone screen when the phone receives an incoming
                        call.

To enable this feature, use the Keep Focus On Active Call field under the Supplementary Services section from Voice > User .

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### MIC Certificate Renewal by SUDI Service

You can now renew the Manufacture Installed Certificate (MIC) by a Secure Unique Device Identifier (SUDI) renewal service.
                        This is an easy way to provide encryption and to help secure the phone. The MIC certificate involves some features that are
                        related to SSL/TLS protocol. If the MIC certificate expires, these features don't work until you renew the certificate.

When this feature is enabled, the phone automatically renews the MIC certificate. Therefore, there's no additional action
                        required by the user or admin.

To enable this feature, use the parameters under the MIC Cert Settings section from Voice > Provisioning .

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Phone Migration without Transition Load

You can now obtain and authorize the licence from the server to migrate your multiplatform phone to enterprise phone firmware
                        in a single step without using transition firmware load. To enable this feature, in the phone web page, use the Transition Authorization Rule and Transition Authorization Type parameters from Voice > Provisioning > Firmware Upgrade .

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### STIR/SHAKEN Visual Confirmation on the Phones

This release supports new technology standard Secure Telephony Identity Revisited (STIR) and Signature-based Handling of Asserted
                        information using toKENs (SHAKEN). STIR/SHAKEN has been mandated by Federal Communications Commission (FCC). These standards
                        define procedures to authenticate and verify caller identification for calls carried over the IP network. The STIR-SHAKEN
                        framework is developed to provide the end user with a great degree of identification and control over the type of calls they
                        receive. These sets of standards are intended to provide a basis for verifying calls, classifying calls, and facilitating
                        the ability to trust caller identity end to end. Illegitimate callers can easily be identified.

When STIR/SHAKEN support is implemented on the server, the phone displays an extra icon next to the caller ID based on the
                        caller's STIR/SHAKEN verification result. Based on the verification result, the phone displays three types of icons.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

### Support for Dialog-Based Shared Line Appearance

You can now enable dialog-based shared line appearance (SLA) so that the phones in the shared line can subscribe to the dialog
                        event package. This feature supports the following functionalities:

Incoming call

Outgoing call

Public/Private hold and resume

Barge-in

Call forward.

To enable this feature, use the Share Line Event Package Type parameter from Voice > SIP > SIP Parameters of the phone web interface.

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Voicemail Subscription Service Control

You can enable the subscription to a specified voicemail server for an extension. After you configure the voicemail server
                        correctly and enable the subscription to the voicemail server, your user can receive voicemail messages on the phone.

To enable the feature, use the Voice Mail Enable field under the Call Feature Settings section from Voice > Ext (n) .

#### Where to Find More Information

Cisco IP Phone 7800 Series Multiplatform Phones Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

## Upgrade the Firmware

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

Click this link:

https://software.cisco.com/download/home/286318380

On the Software Download web page that is displayed, ensure that IP Phone 7800 Series with Multiplatform Firmware is selected in the middle pane.

Select your phone model in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

On the next page that is displayed, select 11.3.5 in the All Releases > MPPv11 folder.

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Download the corresponding file.

cmterm-78xx.11-3-5MPP0001.276_REL.zip

Click Accept License Agreement .

Unzip the file and place the files in the appropriate location on your upgrade server.

The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade.

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

http://10.73.10.223/firmware/sip78xx.11-3-5MPP0001-276.loads

https://server.domain.com/firmware/sip78xx.11-3-5MPP0001-276.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip78xx.11-3-5MPP0001-276.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip78xx.11-3-5MPP0001-276.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone audio and, in some cases, can cause a call to drop. Sources of
                        network degradation can include, but are not limited to, the following activities:

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

## Caveats

### View Caveats

You can search for caveats (bugs) with the Cisco Bug Search tool.

Known caveats are graded according to severity level, and are either open or resolved.

Before you begin

#### Before you begin

Click one of the following links:

To view all caveats that affect this release:

To view open caveats that affect this release:

To view resolved caveats that affect this release:

When prompted, log in with your Cisco.com user ID and password.

(Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 7800 Series Multiplatform Phones that use Firmware Release 11.3(4).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                        this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                        as described in the View Caveats .

CSCvw72979 Phone will show the call center softkey after answer executive or call forward call.

CSCvx44952 Phone showing Failed to download configurations even when it was successful while migrating to MPP

CSCvy98097 Set all or part of cfw items to "na" and enable user mode, see the forward sk or cfw item in menu

CSCvz67625 License prompt is always displayed on the GDS input screen if the phone is converted from On-Prem

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series Multiplatform Phones that use Firmware Release 11.3(5).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                        this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                        as described in the View Caveats .

CSCvv21588 6821/7811/7832: PSK labels for Extend PSK functionality feature are truncated

CSCvy27737 No reorder tone and will not time out when network conference fail

CSCvx69154 MPP Not Setting "Don't Fragment" (DF) Bit

CSCvy36096 Unexpected 481 sent by phone when off/on-hook shared line quickly

CSCvx44944 Short activation code taking a long time to get configurations

CSCvs52371 MPP phone call focus on new incoming call

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 7800 Series Multiplatform Phones | BroadSoft BroadWorks 24.0 MetaSphere CFS version 9.5 Asterisk 16.0 |

| Step 1 | Click this link: https://software.cisco.com/download/home/286318380 On the Software Download web page that is displayed, ensure that IP Phone 7800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select your phone model in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | On the next page that is displayed, select 11.3.5 in the All Releases > MPPv11 folder. |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the corresponding file. cmterm-78xx.11-3-5MPP0001.276_REL.zip |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: http://10.73.10.223/firmware/sip78xx.11-3-5MPP0001-276.loads https://server.domain.com/firmware/sip78xx.11-3-5MPP0001-276.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip78xx.11-3-5MPP0001-276.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip78xx.11-3-5MPP0001-276.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311381&rls=11.3(5)&sb=anfr&bt=custV To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311381&rls=11.3(5)&sb=afr&bt=custV To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311381&rls=11.3(5)&sb=fr&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |