---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8832-firmware-12-0-7-cs88-b-8832mpp-rn-1207-html-af75b0ed5e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8832/firmware/12-0-7/cs88_b_8832mpp-rn-1207.html
retrieved_at: 2026-08-17T01:17:13.790639+00:00
---

Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 12.0(7)

# Cisco IP Conference Phone 8832 Multiplatform Phones Release Notes for Firmware Release 12.0(7)

### Download Options

Updated: January 22, 2025

First Published: January 22, 2025

# Release Notes

Use these release notes with the Cisco IP Conference Phone 8832 Multiplatform Phones running SIP Firmware Release 12.0(7).

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Conference Phone 8832 Multiplatform Phones

BroadSoft BroadWorks RI

Asterisk 20

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Conference Phone 8832 Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/index.html

## New and Changed Features

### Accessibility features

With the Firmware Release 12.0(7), the Voice Feedback feature is available on the Cisco IP Conference Phone 8832 Multiplatform Phones . This feature enables visually impaired and blind persons to work effectively with the Cisco phones. The phone's voice feedback
                        reads incoming caller IDs, displayed screens and settings, and button functions.

To have a better visual experience, you can adjust the size of the fonts that are displayed on the phone screen. Note that
                        the customization of the font size does not change few of the texts, such as the texts on the phone screen header row (the
                        current date and time), the texts on the bottom row (the softkey labels), and the texts in a prompt window.

#### Where to Find More Information

Cisco IP Conference Phone 8832 Multiplatform Phones User Guide

Cisco IP Conference Phone Multiplatform Phone Administration Guide

Accessibility Features for the Cisco IP Conference Phone 8832 Multiplatform Phones

### Support for Office Hours

With the Firmware Release 12.0(7), the Office Hours feature is available on the Cisco IP Conference Phone 8832 Multiplatform Phones . This feature helps to reduce power consumption during periods of inactivity. When the Office Hours feature is enabled, the
                        phone enters the Display Off Mode and turns off the screen to save power outside of the designated working hours. The display
                        will be turned on again if you press any key on the phone or if there are any incoming calls or voicemails. The display remains
                        on until the phone has been in idle for a designated length of time, then it turns off automatically.

Meanwhile, when the phone screen is off, you can also control whether to light up the backlight of the Select button in the Navigation cluster.

#### Where to Find More Information

Cisco IP Conference Phone Multiplatform Phone Administration Guide

### Support for Custom Device Certificate on 802.1x

You can install a Custom Device Certificate (CDC) by using one of the following methods:

Manual installation by uploading the .p12 or .pfx certificate from the phone administration web page.

The .p12 or .pfx certificate typically contains a user private key, a user certificate, certificate chains, and an extract
                              password associated with it.

Auto installation by a Simple Certificate Enrollment Protocol (SCEP) server.

You can configure the SCEP parameters by using one of the following methods:

The phone administration web page

XML provisioning

DHCP option 43

The certificate can be installed for the wired network with 802.1x authentication.

On the phone administration web page, you can check the installation status of the certificate, view details of the installed
                        certificate, and remove the installed certificate.

On the phone screen or phone administration web page, you can select the certificate type ( Manufacturing installed or Custom installed ) for the 802.1x authentication in wired network environment.

#### Where to Find More Information

Cisco IP Conference Phone Multiplatform Phone Administration Guide

## Upgrade the Firmware

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

### SUMMARY STEPS

- Click this link:

- Select IP Conference Phone 8832 with Multiplatform Firmware in the right pane.

- On the next page that is displayed, select Multiplatform Firmware .

- Select All Release > MPP v12 > 12.0.7 .

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

http://10.73.10.223/firmware/sip8832.12-0-7MPP0001-46.loads

https://server.domain.com/firmware/sip8832.12-0-7MPP0001-46.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

http://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip8832.12-0-7MPP0001-46.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.12-0-7MPP0001-46.loads

### DETAILED STEPS

Step 1

Click this link:

https://software.cisco.com/download/home/286311392

On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane.

Step 2

Select IP Conference Phone 8832 with Multiplatform Firmware in the right pane.

Step 3

On the next page that is displayed, select Multiplatform Firmware .

Step 4

Select All Release > MPP v12 > 12.0.7 .

Step 5

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Step 6

Download the corresponding file.

cmterm-8832.12-0-7MPP0001-46_REL.zip

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

http://10.73.10.223/firmware/sip8832.12-0-7MPP0001-46.loads

https://server.domain.com/firmware/sip8832.12-0-7MPP0001-46.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

http://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip8832.12-0-7MPP0001-46.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.12-0-7MPP0001-46.loads

Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

Caveats

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

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 8832 Multiplatform Phones that use Firmware Release 12.0(7).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this
                     report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described
                     in View Caveats .

CSCwe55809—Personal contact calls play the distinctive ring while there's an active call on 8800 phones.

CSCwf10956—Macro $SERVIP is not expanded in Log Request Msg in syslog.

CSCwb46008—Many PRTs with logs missing for around 5 seconds.

## Resolved Caveats

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this
                     report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described
                     in View Caveats .

CSCwf10291—CP-8832-K9= does not support wireless after migration to MPP phone firmware.

CSCwi27445—Remove the "b=" and "t=" parameters from MPP Ringtone documentation.

CSCwi64037—Packet capture feature available without authentication.

CSCwk59424—Cannot use the '+' on keypad on 8832NR.

CSCwm41649—MPP 8800 Series Stored Cross-Site Scripting Vulnerability - unexpected XSS payload.

CSCwm41710—MPP 8800 Series Stored Cross-Site Scripting Vulnerability - regular expression.

CSCwm90601—Vulnerabilities in linux-kernel 5.4.124 CVE-2022-0185.

CSCwn25118—SRTP one-way audio after long conference and Hold-Resumes.

CSCwn50436—Encode/decode codec is not displayed on the LCD statistics page.

CSCwn79823—Redundant activating device is displayed on Control Hub when the device is activated via AC code.

## Cisco IP Phone Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Requirements |
|---|---|
| Cisco IP Conference Phone 8832 Multiplatform Phones | BroadSoft BroadWorks RI Asterisk 20 |

| Step 1 | Click this link: https://software.cisco.com/download/home/286311392 On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select IP Conference Phone 8832 with Multiplatform Firmware in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | Select All Release > MPP v12 > 12.0.7 . |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the corresponding file. cmterm-8832.12-0-7MPP0001-46_REL.zip |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: http://10.73.10.223/firmware/sip8832.12-0-7MPP0001-46.loads https://server.domain.com/firmware/sip8832.12-0-7MPP0001-46.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: http://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip8832.12-0-7MPP0001-46.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8832.12-0-7MPP0001-46.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&rls=12.0(7)&sb=anfr&bt=custV To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&rls=12.0(7)&sb=anfr&sts=open&bt=custV To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319904&rls=12.0(7)&sb=anfr&sts=fd&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |