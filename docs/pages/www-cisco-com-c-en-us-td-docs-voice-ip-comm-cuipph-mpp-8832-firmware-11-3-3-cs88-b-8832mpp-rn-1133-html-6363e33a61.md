---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8832-firmware-11-3-3-cs88-b-8832mpp-rn-1133-html-6363e33a61
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8832/firmware/11-3-3/cs88_b_8832mpp-rn-1133.html
retrieved_at: 2026-08-21T13:42:59.511058+00:00
---

Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 11.3(3)

# Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 11.3(3)

### Download Options

Updated: December 2, 2020

First Published: February 1, 2021

# Release Notes

Use these release notes with the Cisco IP Conference Phone 8832 Multiplatform Phones running SIP Firmware Release 11.3(3).

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Conference Phone 8832 Multiplatform Phones

Cisco BroadWorks 24.0

MetaSphere CFS version 9.5

Asterisk 13.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Conference Phone 8832 Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/index.html

## New and Changed Features

### Contacts Management of the BroadSoft Personal Directory on the Phone

You can set the BroadSoft Personal directory as the target directory to store the newly added contacts. When this feature
                        is enabled, your users can select the new option Add contact to add contacts to the target directory on the phone.

To enable this feature, use the field Add Contacts to Directory Personal under the section XSI Phone Service from Voice > Phone .

The phone now supports the users to add, edit, and delete the contacts in the BroadSoft Personal directory. It also supports
                        the users to add contacts from recent calls or any types of directories (if enabled), including:

All directories

Personal address book

BroadSoft directory, including the following subdirectories:

Enterprise

Group

Personal

Enterprise Common

Group Common

LDAP directory

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

### Enable Preconditions

You can enable or disable precondition signaling separately.

As in the previous release, precondition is combined with the 100REL SIP extension. When you enable the 100REL SIP feature,
                        the precondition signaling is enabled at the same time.

Precondition signaling defers incoming call notifications until the phone receives the message that preconditions are satisfied
                        to establish the call.

To enable this feature, you can use the Precondition Support field under the SIP Settings section from Voice > Ext (n) .

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

### HTTP Header Specification for PRT

You can specify the HTTP header for the URL that is used for the PRT upload script.

Only the PRT log collector uses the feature.

To enable this feature, you can use the PRT HTTP Header and PRT HTTP Header Value fields under the Problem Report Tool section from Voice > Provisioning .

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

### Show Product Configuration Version

You can customize the product configuration version that shows as the menu item Configuration version on the phone screen Product information .

To enable this feature, set the value for the element <Device_Config_Version> in the phone configuration file (cfg.xml).

This is the only method to configure the element.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

### Softkeys Configuration to Calls History List

You can configure the Option , Call , Edit call , Filter , and Back softkeys on the screen for All, Placed, Received, and Missed calls list. When you press the Recents softkey on the phone, you can directly access the All calls screen and see the list of all types of recents calls.

To implement this feature, a new parameter Broadsoft Call History Key List is added. In the phone web interface, access this new parameter in the Programmable Softkeys section from Voice > Phone tab. The Broadsoft Call History Key List parameter defines the values for the softkeys Option , Call , Edit call , Filter , and Back for All, Placed, Received, and Missed calls list.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

### Synchronization of Call Waiting and Anonymous Call Rejection

You can enable synchronization of the Call Waiting and Anonymous Call Rejection functions between a specific line and a BroadSoft
                        server. When enabled, the line gets the latest status of the functions from the BroadSoft server, and the line can put the
                        setting of the functions to the BroadSoft server. For example, if the functions are disabled on the BroadSoft server, the
                        functions don't work on the line. If the user enables or disables the functions on the line, the setting modifies the status
                        of the functions on the BroadSoft server.

The setting of the synchronization is only available for specific lines. The priority of the synchronized functions is higher
                        than the local call waiting ( CW Setting ) and anonymous call blocking ( Block ANC Setting ) functions. The settings of the local functions are under the Supplementary Services section from Voice > User of the phone administration web page.

To enable synchronization of Call Waiting between a line and an XSI service, use the Call Waiting Enable field under the XSI Line Service section from Voice > Ext (n) of the phone administration web page.

To enable synchronization of Anonymous Call Rejection between a line and an XSI service, use the Block Anonymous Call Enable field under the XSI Line Service section from Voice > Ext (n) of the phone administration web page.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

### Unavailable Text Box of Agent Status Control

This feature enables you to control the availability of the Unavailable menu text box of the agent status on the phone. To control the display of this text box for each line, use the Unavailable Reason Code Enable parameter on the Voice > Ext(n) tab of the phone administration web page. Set the parameter to No to hide the Unavailable menu text box.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones Administration Guide

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

## Upgrade Overview

The upgrade procedure is different according to the current phone firmware version.

If the current phone firmware is 11.3(1) SR3 or later, see Upgrade the Firmware from a version after 11.3(1) SR3 .

If the current phone firmware is 11.3(1) SR2 or earlier, see Upgrade the Firmware from a version before 11.3(1) SR2 .

### Upgrade the Firmware from a version after 11.3(1) SR3

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

The phone firmware supports the following upgrade paths:

From 11.3(1) SR3 to 11.3(3)

From 11.3(2) to 11.3(3)

Click this link:

https://software.cisco.com/download/home/286311392

On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane.

Select IP Conference Phone 8832 with Multiplatform Firmware in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

On the next page that is displayed, select 11.3.3 in the All Releases > MPPv11 folder.

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Download the cmterm-8832.11-3-3MPP0001-377_REL.zip file.

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

http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads

https://server.domain.com/sip8832.11-3-3MPP0001-377.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]/<file name>.loads

Examples:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.11-3-3MPP0001-377.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

### Upgrade the Firmware from a version before 11.3(1) SR2

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

Under Latest Release , select 11.3.3 .

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Download the corresponding file.

cmterm-8832.11-3-3MPP0001-377_REL.zip

Click Accept License Agreement .

Unzip the file and place the files in the appropriate location on your upgrade server.

The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                    upgrade.

If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server.

Example:

http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads

If the file is placed under a non-root directory of the upgrade server, the upgrade fails.

Example:

http://10.73.10.223/firmware/sip8832.11-3-3MPP0001-377.loads

Upgrade the phone firmware with one of these methods.

Upgrade the phone firmware from the phone administration web page:

On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade .

In the Upgrade Rule field, enter the load file URL as described below.

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<file name>.loads

Examples:

http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads

https://server.domain.com/sip8832.11-3-3MPP0001-377.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]/<file name>.loads

Examples:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.11-3-3MPP0001-377.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

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

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 8832 Multiplatform Phones that use Firmware Release 11.3(3).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this
                     report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described
                     in View Caveats .

CSCvw69851 CP-8832-3PCC buzzing noise

CSCvw82717 MPP phones - SBC is rejecting a specific line-seize SIP SUBSCRIBE

CSCvv20301 POR: Not all characters are shown in the character preview pop-up

CSCvv51309 MPP software is not completing the ICE procedures when placing a call to L2SIP

CSCvw21396 ICE, Offer not having ICE candidates should be handled

CSCvw56643 Will not get the new IP address after changing the VLAN of the switch port

CSCvw87814 Dropped Media from ICE enabled Device on Non ICE Call Path

CSCvx05499 Two "Anonymous" were shown on LCD when shareline reiceving anonymous calls

CSCvx08073 BS DIR - can't search name containing the non ASCII char like ä

## Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 8832 Multiplatform Phones that use Firmware Release 11.3(3).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCvt79137 Multiple Vulnerabilities in linux_kernel

CSCvt50003 MPP phones listen to multicast paging group '800' by default

CSCvu20649 MPP phones - unable to activate via device activation code

CSCvt13644 88xx Voice Feedback Disables After Reboot if UI-User-Mode is Enabled

CSCvu31850 Set_Local_Date and Set_Local_Time not Taking Effect

CSCvv29937 Incoming Display ID shows incorrect value if PAB entry is deleted

CSCvt06292 Linux Kernel vc_do_resize Function Use-After-Free Vulnerability

CSCvu50856 libcurl curl_easy_unescape Heap Overflow Remote Code Execution Vulnerability

CSCvt26126 Evaluation of 8832 for expired certificates

CSCvs62320 Multiple Vulnerabilities in linux_kernel

CSCvt52122 MPP phones - Transferor hears busy signal during consultative transfer

CSCvs54500 Error prompt during Profile Account Setup and default input alphanumeric

CSCvs59424 3pcc-88xx: Phone is not uploading the config when Report To Server is set to On Local Change

CSCvr86301 Remote SDK: WebSocket Control Server URL waits 10 seconds after HTTP 401 Challenge

CSCvs01888 CP-88xx-3PCC When Answer confirmation is set to ON there is one-way audio

CSCvs70834 LDAP reverse lookup not pulling info from LDAP server on incoming INVITE

CSCvs31198 480 timeout value in Cadence tag is hardcoded to 60 seconds when infinite value is set

CSCvr61497 Upgrade libpcap to 1.9.1 and tcpdump to 4.9.3

CSCvs88350 MPP phones Multicast Paging Ended By Itself

CSCvv20465 MPP sends '183' even when '100rel' is disabled

CSCvs66815 Cisco IP Phone TCP Packet Flood Denial of Service Vulnerability

CSCvu33942 Language Reverts to English After Reboot if Locale Server Connection is Lost

CSCvs44645 Multiple Vulnerabilities in linux_kernel

CSCvs35121 Linux Kernel ath9k_wmi_cmd() Function Memory Leak Denial of Service Vulnerability

CSCvs44650 Linux Kernel vcs_write Write Access Prevention Vulnerability

CSCvs31788 Linux Kernel drivers/net/wireless/ath/ath9k/htc_hst.c Memory Leak Denial of Service Vulnerability

CSCvu57297 Multiple Vulnerabilities in linux_kernel

CSCvv03397 MPP phones - when callee pauses recording caller can hear callee but callee does not hear caller

CSCvv33336 Reverse name lookup against BS Dir failed if more than 1 results are received

CSCvu88718 Call Filter In Settings Always Be Off

CSCvs35094 Linux Kernel i2400m_op_rfkill_sw_toggle() Function Memory Leak Denial of Service Vulnerability

CSCvs35119 Multiple Vulnerabilities in linux_kernel

CSCvs31890 Multiple Vulnerabilities in linux_kernel

CSCvs35092 Multiple Vulnerabilities in linux_kernel

CSCvs31786 Multiple Vulnerabilities in linux_kernel

CSCvt24809 Conference phone 8832 fail to upgrade from prior to MPP 11.3.1SR2 to MPP 11.3.2

CSCvu29265 Multiple Vulnerabilities in linux_kernel

CSCvu29263 Multiple Vulnerabilities in linux_kernel

CSCvv19782 Phone can't send publish if Voice Quality Report Address is "proxy domain"+port

CSCvv15154 When phone playing hold remind and have an incoming call,both hold remind and ringer not played

CSCvv32982 LDAP sign-in window is not popped up when using plk or psk in legacy mode

CSCvw73648 "Custom LED Type" settings do not take effect after first time configuration from the phone's web UI

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Requirements |
|---|---|
| Cisco IP Conference Phone 8832 Multiplatform Phones | Cisco BroadWorks 24.0 MetaSphere CFS version 9.5 Asterisk 13.0 |

| Note | This is the only method to configure the element. |
|---|---|

| Step 1 | Click this link: https://software.cisco.com/download/home/286311392 On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select IP Conference Phone 8832 with Multiplatform Firmware in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | On the next page that is displayed, select 11.3.3 in the All Releases > MPPv11 folder. |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the cmterm-8832.11-3-3MPP0001-377_REL.zip file. |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                    upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<file name>.loads Examples: http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads https://server.domain.com/sip8832.11-3-3MPP0001-377.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address>[:<port>]/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]/<file name>.loads Examples: https://10.74.10.225/admin/upgrade?http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.11-3-3MPP0001-377.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click this link: https://software.cisco.com/download/home/286311392 On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select IP Conference Phone 8832 with Multiplatform Firmware in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | Under Latest Release , select 11.3.3 . |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the corresponding file. cmterm-8832.11-3-3MPP0001-377_REL.zip |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                    upgrade. Note If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server. Example: http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads If the file is placed under a non-root directory of the upgrade server, the upgrade fails. Example: http://10.73.10.223/firmware/sip8832.11-3-3MPP0001-377.loads | Note | If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server. Example: http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads If the file is placed under a non-root directory of the upgrade server, the upgrade fails. Example: http://10.73.10.223/firmware/sip8832.11-3-3MPP0001-377.loads |
| Note | If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server. Example: http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads If the file is placed under a non-root directory of the upgrade server, the upgrade fails. Example: http://10.73.10.223/firmware/sip8832.11-3-3MPP0001-377.loads |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<file name>.loads Examples: http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads https://server.domain.com/sip8832.11-3-3MPP0001-377.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address>[:<port>]/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]/<file name>.loads Examples: https://10.74.10.225/admin/upgrade?http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.11-3-3MPP0001-377.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | If you miss the step to upgrade the phone firmware to 11.3.1 MSR2-6 , then you must place the file under the root directory of the TFTP, HTTP, or HTTPs upgrade server. Example: http://10.73.10.223/sip8832.11-3-3MPP0001-377.loads If the file is placed under a non-root directory of the upgrade server, the upgrade fails. Example: http://10.73.10.223/firmware/sip8832.11-3-3MPP0001-377.loads |
|---|---|

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&rls=11.3(3)&sb=anfr&bt=custV To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&rls=11.3(3)&sb=anfr&sts=open&bt=custV To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&rls=11.3(3)&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |