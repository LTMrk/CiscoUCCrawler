---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8832-firmware-11-3-6-cs88-b-8832mpp-rn-1136-html-ad3ae4d82d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8832/firmware/11-3-6/cs88_b_8832mpp-rn-1136.html
retrieved_at: 2026-08-21T13:42:47.078234+00:00
---

Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 11.3(6)

# Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 11.3(6)

### Download Options

Updated: January 24, 2022

First Published: January 26, 2022

# Release Notes

Use these release notes with the Cisco IP Conference Phone 8832 Multiplatform Phones running SIP Firmware Release 11.3(6).

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

### Call Focus Enhancement

The existing feature Keep Focus on the Active Call has an enhancement in this release. Now the focus on the phone screen can automatically move to an incoming call if the user
                        places the active call on hold.

To enable this feature, use the Keep Focus on Active Call filed under the Supplementary Services section from Voice > User .

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### Enhancements of Displaying Contact Numbers from the LDAP Directory

The phone now separately displays the LDAP user's contact numbers in the contact details screen. As a user, you can select
                        one of the contact numbers before you edit the number or directly make a call.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

### Enhancements of Displaying Contact Numbers from the XML Directory

The phone now displays the contact numbers of a XML address entry separately on the phone screen. As a user, you can do the
                        following activities:

View the details of an XML address entry

Select a specific contact number to dial out by viewing the details of an XML address entry

Dial out the first contact number of an XML address entry

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

### Multiplatform Phones Support Webex Contacts

You can enable phone to support Webex contacts. The phone must onboards to Webex cloud to support this feature. You can also
                        modify the Webex directory name. When you add support for Webex contacts, on the phone the user can see the Webex directory
                        name under the Directory screen that you have created.

To enable this feature from the phone administration web page, use the Directory Enable parameter under the Webex section from Voice > Phone . To modify the Webex directory name, use the Directory Name parameter of Webex section.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Series Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Series Multiplatform Phones User Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

Webex for Cisco BroadWorks Solution Guide

### Multiplatform Phones Support Webex Call Logs

You can now enable a phone to support Webex call logs. The phone must onboards to Webex cloud to support this feature. When
                        you enable this feature, the Display recents from menu under the Recents screen includes the Webex option in the calls list. The user then can set the option Webex to see the list of recent Webex calls.

To enable this feature from the phone administration web page, use the Display Recents From parameter under the Call Log section from Voice > Phone . Under the Call Log section, you must also enable the CallLog Enable parameter and select a phone line from CallLog Associated Line for which you want to display the Webex recent call logs.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Series Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Series Multiplatform Phones User Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

Webex for Cisco BroadWorks Solution Guide

### Permission Only for the Call Forward All Service Setup

You can configure the phone to allow the user directly set up the Call Forward All service by pressing the Forward all softkey. By default, the user can set up all call forward services, including Call Forward All, Call Forward Busy, and Call
                        Forward No Answer by the Forward softkey.

To enable this feature, use the Forward Softkey parameter under the Call Forward section from Voice > User on the phone web interface,.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

### PRT Generation of Multiplatform Phones from the Webex Control Hub

You can now generate a problem report of a phone from the Webex Control Hub if the phone successfully onboards to Webex cloud.

After you generate a problem report, check the PRT upload information on the phone from a new phone menu, Last problem report info . On the phone administration web page, from Info > Status > PRT Status , you can see that the upload information is triggered from the Webex Control Hub.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Series Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Series Multiplatform Phones User Guide

Webex for Cisco BroadWorks Solution Guide

### Reboot of Multiplatform Phones from the Webex Control Hub

You can reboot phone remotely from the Webex Control Hub. The phone must onboards to Webex cloud if you want to reboot it
                        remotely. You can only reboot a phone that is in idle state. If the phone is in use, such as in a call, the phone doesn’t
                        reboot.

After successful reboot, check the status on the phone administration web page from Info > Status > Reboot History . The Reboot Reason parameter under Reboot History shows the reboot reason as Cloud Trigerred . You can also check the reboot reason as Cloud triggered on the phone from Application > Status > Reboot history .

#### Where to Find More Information

Cisco IP Conference Phone 8832 Series Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Series Multiplatform Phones User Guide

Webex for Cisco BroadWorks Solution Guide

### Support for French (Canada) Language

Phone now supports French (Canada) language. All multiplatform IP phones and all key expansion modules (KEM) now support the
                        language.

In the phone web interface, you can use the Dictionary Server Script parameter from Voice > Regional > Language to configure the language support.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Series Multiplatform Phones Administration Guide

### Webex Cloud Onboarding of Multiplatform Phones

You can onboard a phone to Webex cloud either with activation code onboarding (GDS) or with phone MAC address (EDOS device
                        activation). When the phone onboards to Webex cloud, you can reboot the phone and can also generate a problem report from
                        the Webex Control Hub.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Series Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Series Multiplatform Phones User Guide

Webex for Cisco BroadWorks Solution Guide

## Upgrade Overview

The upgrade procedure is different according to the current phone firmware version.

If the current phone firmware is 11.3(1) SR3 or later, see Upgrade the Firmware from a version after 11.3(1) SR3 .

If the current phone firmware is 11.3(1) SR2 or earlier, see Upgrade the Firmware from a Version before 11.3(1) SR2 .

### Upgrade the Firmware from a version after 11.3(1) SR3

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

The phone firmware supports the following upgrade paths:

From 11.3(1) SR3 to 11.3(6)

From 11.3(2) to 11.3(6)

From 11.3(3) to 11.3(6)

From 11.3(4) to 11.3(6)

From 11.3(5) to 11.3(6)

Click this link:

https://software.cisco.com/download/home/286311392

On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane.

Select IP Conference Phone 8832 with Multiplatform Firmware in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

On the next page that is displayed, select 11.3.6 in the All Releases > MPPv11 folder.

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Download the cmterm-8832.11-3-6MPP0001-273_REL.zip file.

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

http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads

https://server.domain.com/sip8832.11-3-6MPP0001-273.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]/<file name>.loads

Examples:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.11-3-6MPP0001-273.loads

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

Under Latest Release , select 11.3.6 .

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Download the corresponding file.

cmterm-8832.11-3-6MPP0001-273_REL.zip

Click Accept License Agreement .

Unzip the file and place the files in the appropriate location on your upgrade server.

The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                    upgrade.

If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server.

Example:

http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads

If the file is placed under a non-root directory of the upgrade server, the upgrade fails.

Example:

http://10.73.10.223/firmware/sip8832.11-3-6MPP0001-273.loads

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<file name>.loads

Examples:

http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads

https://server.domain.com/sip8832.11-3-6MPP0001-273.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]/<file name>.loads

Examples:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.11-3-6MPP0001-273.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Backward Compatibility of Password

Since Firmware Release 11.3(6) introduces a mechanism to enhance the security, certain passwords don't support back-compatibility.

This behaviour only affects the passwords that are updated in the 11.3(6).

For more information, refer to the Saved Passwords Become Invalid after Downgrade section in the following guide:

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

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

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 8832 Multiplatform Phones that use Firmware Release 11.3(6).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this
                     report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described
                     in View Caveats .

CSCvx18250 8800 series IP Phones do not display "calling party number" for the inbound HUNTcalls.

CSCvx44952 Phone showing Failed to download configurations even when it was successful while migrating to MPP

CSCvx49825 Phone stuck at configuration check in progress during firmware migration if it was on WiFi before

CSCvx78045 Add "PoE Power Required" parameter definitions to 8800 MPP administration guide

CSCvz35920 SSRC changes for outgoing Re-INVITES

CSCvz67625 License prompt is always displayed on the GDS input screen if the phone is converted from On-Prem

## Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 8832 Multiplatform Phones that use Firmware Release 11.3(6).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCvy27737 No reorder tone and will not time out when network conference fail

CSCvx44944 Short activation code taking a long time to get configurations

CSCvy36096 Unexpected 481 sent by phone when off/on-hook shared line quickly

CSCvy39554 MPP Mutual auth fails in HTTPS for E911

CSCvy98097 Set all or part of cfw items to "na" and enable user mode, see the forward sk or cfw item in menu

CSCvx69154 MPP Not Setting "Don't Fragment" (DF) Bit

CSCvs52371 MPP phone call focus on new incoming call

CSCwa01555 Optimize the performance for MPP when Webex Call is made

CSCwa03481 Optimize the call flow for MPP phone

CSCwa04807 Optimize the mute for MPP phone

CSCwa37662 CIAM: curl 7.21.6 TPSD cleanup: libcurl

CSCvz47388 ICE : MS crash seen during an incoming call

CSCvy98097 Set all or part of cfw items to "na" and enable user mode, see the forward sk or cfw item in menu

CSCvz66685 Change call focus on incoming call if first call is held

CSCwa70820 MPP phones - Incorrect Date & Time in "Recents" Page

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
| Step 4 | On the next page that is displayed, select 11.3.6 in the All Releases > MPPv11 folder. |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the cmterm-8832.11-3-6MPP0001-273_REL.zip file. |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                    upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<file name>.loads Examples: http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads https://server.domain.com/sip8832.11-3-6MPP0001-273.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address>[:<port>]/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]/<file name>.loads Examples: https://10.74.10.225/admin/upgrade?http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.11-3-6MPP0001-273.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click this link: https://software.cisco.com/download/home/286311392 On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select IP Conference Phone 8832 with Multiplatform Firmware in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | Under Latest Release , select 11.3.6 . |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the corresponding file. cmterm-8832.11-3-6MPP0001-273_REL.zip |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                    upgrade. Note If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server. Example: http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads If the file is placed under a non-root directory of the upgrade server, the upgrade fails. Example: http://10.73.10.223/firmware/sip8832.11-3-6MPP0001-273.loads | Note | If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server. Example: http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads If the file is placed under a non-root directory of the upgrade server, the upgrade fails. Example: http://10.73.10.223/firmware/sip8832.11-3-6MPP0001-273.loads |
| Note | If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server. Example: http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads If the file is placed under a non-root directory of the upgrade server, the upgrade fails. Example: http://10.73.10.223/firmware/sip8832.11-3-6MPP0001-273.loads |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<file name>.loads Examples: http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads https://server.domain.com/sip8832.11-3-6MPP0001-273.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address>[:<port>]/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]/<file name>.loads Examples: https://10.74.10.225/admin/upgrade?http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.11-3-6MPP0001-273.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server. Example: http://10.73.10.223/sip8832.11-3-6MPP0001-273.loads If the file is placed under a non-root directory of the upgrade server, the upgrade fails. Example: http://10.73.10.223/firmware/sip8832.11-3-6MPP0001-273.loads |
|---|---|

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&rls=11.3(6)&sb=anfr&bt=custV To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&rls=11.3(6)&sb=anfr&sts=open&bt=custV To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&rls=11.3(6)&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |