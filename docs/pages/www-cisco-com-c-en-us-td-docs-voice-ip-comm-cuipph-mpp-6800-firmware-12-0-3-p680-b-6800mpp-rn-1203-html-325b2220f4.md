---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-6800-firmware-12-0-3-p680-b-6800mpp-rn-1203-html-325b2220f4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/6800/firmware/12-0-3/p680_b_6800mpp-rn-1203.html
retrieved_at: 2026-08-17T01:06:10.523307+00:00
---

Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 12.0(3)

# Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 12.0(3)

### Download Options

Updated: August 17, 2023

First Published: August 17, 2023

# Release Notes

Use these release notes with the following Cisco IP Phone 6800 Series Multiplatform Phones running SIP Firmware Release 12.0(3).

Cisco IP Phone 6821 Multiplatform Phones

Cisco IP Phone 6841 Multiplatform Phones

Cisco IP Phone 6851 Multiplatform Phones

Cisco IP Phone 6861 Multiplatform Phones

Cisco IP Phone 6871 Multiplatform Phones

This document doesn't include the DECT phones.

The following table describes the individual phone requirements.

Phone

Support Servers

Cisco IP Phone 6800 Series Multiplatform Phones

Cisco BroadWorks 24.0

MetaSphere CFS version 9.5

Asterisk 16.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone 6800 Series Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/tsd-products-support-series-home.html

## New and Changed Features

### Automatic Renewal of MIC Certificate

From 12.0.3 release onwards, all phones can automatically renew its Manufacture Installed Certificate (MIC) by reaching out
                        to cloud service at sudirenewal.cisco.com. To allow traffic to the cloud service, make sure to update your firewall settings.
                        If you are a service provider and your servers challenge phones for their certificate, make sure to update the server trust
                        store to include new root CA. For more information, see the field notice FN - 72302 - https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72302.html .

From 12.0.3 release, SUDI feature is enabled by default.

#### Where to Find More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

### Factory Reset with SIP-Notify

You can initiate a factory reset of a phone when the phone is deleted from server. Once deleted by the administrator, phone
                        will receive SIP-NOTIFY message with event:factory-reset and performs factory-reset accordingly.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

### HTTPS Enablement by Default

With this release you must enable Https by default to access the phone administration web page. To enable this feature from the phone administration web page, use
                        the Enable Protocol and Web Server Port under System Configuration section from Voice > System . A phone with Firmware version 12.0(3) and later always gets redirected to https://<ip address>:443 . When you enable protocol to Https and web server port to 443 , after the factory reset, if you do not change the values and your user wants to access the phone administration web page
                        with http://<ip address> or http://<ip address>:80 , the URL gets redirected to https://<ip address>:443 .

#### Where to Find More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

### Invoking of XML Service with Multicast Paging

This feature allows phones to recieve pages from a server to optionally display an image or other UI elements. With this feature,
                        you can invoke the XML service from multicast paging. When configured, user will not be able to see the XML application in the Information and settings menu on the phone.

To enable this feature from the phone administration web page, use the XML Application Service URL parameter under XML Service from Voice > Phone .

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

### Password Alert after Factory Reset

After a factory reset, when the phone boots up for the first time, it displays a prompt to set up a password as a security
                        measure. If the user chooses to skip the password setup, phone shows a warning message. You can set the user password in the
                        phone administration web page. If the password is not created, the user can use the Create softkey on the Issues screen to create a new password. Once the user creates the password the phone displays an unlock icon on the phone screen.

To enable this feature from the phone administration web page, use the Display Password Warnings parameter under System Configuration section from Voice > System .

#### Where to Find More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

## Upgrade Firmware

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

### SUMMARY STEPS

- Click this link:

- Select your phone model in the right pane.

- On the next page that is displayed, select Multiplatform Firmware .

- On the next page that is displayed, select 12.0.3 in the All Releases > MPPv12 folder.

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

6821:

https://10.73.10.223/firmware/sip6821.12-0-3MPP0001-87.loads

Other phones in 6800 series:

https://10.73.10.223/firmware/sip68xx.12-0-3MPP0001-87.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

6821:

https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip6821.12-0-3MPP0001-87.loads

Other phones in 6800 series:

https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip68xx.12-0-3MPP0001-87.loads

### DETAILED STEPS

Step 1

Click this link:

https://software.cisco.com/download/home/286318380

On the Software Download web page that is displayed, ensure that IP Phone 6800 Series with Multiplatform Firmware is selected in the middle pane.

Step 2

Select your phone model in the right pane.

Step 3

On the next page that is displayed, select Multiplatform Firmware .

Step 4

On the next page that is displayed, select 12.0.3 in the All Releases > MPPv12 folder.

Step 5

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Step 6

Download the corresponding file.

6821: cmterm-6821.12-0-3MPP0001-87_REL.zip

Other phones in 6800 series: cmterm-68xx.12-0-3MPP0001-87_REL.zip

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

6821:

https://10.73.10.223/firmware/sip6821.12-0-3MPP0001-87.loads

Other phones in 6800 series:

https://10.73.10.223/firmware/sip68xx.12-0-3MPP0001-87.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

6821:

https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip6821.12-0-3MPP0001-87.loads

Other phones in 6800 series:

https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip68xx.12-0-3MPP0001-87.loads

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

## Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 6800 Series Multiplatform Phones that use Firmware Release 12.0(3).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCwb46008—Many PRTs with logs missing for around 5 seconds.

## Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 6800 Series Multiplatform Phones that use Firmware Release 12.0(3).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCwe80034—68xx crash in mPhone process.

CSCwd44995—Not able to upgrade firmware when using long FQDN in upgrade rule.

CSCwb61351—The o-line IP address is not EXT_IP in a NAT call.

CSCwd58480—Cisco MPP phones uses data VLAN IP address on boot-up when connected to Aruba switch.

CSCwe37668—Vulnerabilities in linux-kernel, multiple versions CVE-2023-23559.

CSCwd89382—Vulnerabilities in linux-kernel, multiple versions CVE-2022-1048.

CSCwf82386—Expiring SUDI/MIC in MPP phones.

CSCwd99838—Cisco CP-6821 IP Phone Sensitive Data Accessible via Exposed Interface.

CSCwf29727—Hard transfer button does not transfer.

CSCwf35777—Inbound caller ID issue.

CSCwh20086—MPP restarts randomly while idle.

CSCwh14446—MPP is losing registration randomly.

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Note | This document doesn't include the DECT phones. |
|---|---|

| Phone | Support Servers |
|---|---|
| Cisco IP Phone 6800 Series Multiplatform Phones | Cisco BroadWorks 24.0 MetaSphere CFS version 9.5 Asterisk 16.0 |

| Note | From 12.0.3 release, SUDI feature is enabled by default. |
|---|---|

| Step 1 | Click this link: https://software.cisco.com/download/home/286318380 On the Software Download web page that is displayed, ensure that IP Phone 6800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select your phone model in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | On the next page that is displayed, select 12.0.3 in the All Releases > MPPv12 folder. |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the corresponding file. 6821: cmterm-6821.12-0-3MPP0001-87_REL.zip Other phones in 6800 series: cmterm-68xx.12-0-3MPP0001-87_REL.zip |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: 6821: https://10.73.10.223/firmware/sip6821.12-0-3MPP0001-87.loads Other phones in 6800 series: https://10.73.10.223/firmware/sip68xx.12-0-3MPP0001-87.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: 6821: https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip6821.12-0-3MPP0001-87.loads Other phones in 6800 series: https://10.74.10.225/admin/upgrade?https://10.73.10.223/firmware/sip68xx.12-0-3MPP0001-87.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=anfr&rls=12.0(2)&kw=*&bt=custV&prdNam=Cisco%20IP%20Phone%206800%20Series%20with%20Multiplatform%20Firmware To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=afr&rls=12.0(2)&kw=*&bt=custV&prdNam=Cisco%20IP%20Phone%206800%20Series%20with%20Multiplatform%20Firmware To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=fr&rls=12.0(2)&kw=*&bt=custV&prdNam=Cisco%20IP%20Phone%206800%20Series%20with%20Multiplatform%20Firmware |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |