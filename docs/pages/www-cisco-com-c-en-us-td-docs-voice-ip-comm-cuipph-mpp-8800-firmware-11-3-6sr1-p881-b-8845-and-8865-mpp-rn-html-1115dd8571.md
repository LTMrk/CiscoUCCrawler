---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-firmware-11-3-6sr1-p881-b-8845-and-8865-mpp-rn-html-1115dd8571
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/firmware/11-3-6SR1/p881_b_8845-and-8865-mpp-rn.html
retrieved_at: 2026-08-21T13:44:10.084483+00:00
---

Cisco IP Phone 8845 and 8865 Multiplatform Phones Release Notes for Firmware Release 11.3(6)SR1

# Cisco IP Phone 8845 and 8865 Multiplatform Phones Release Notes for Firmware Release 11.3(6)SR1

### Download Options

Updated: May 5, 2022

First Published: May 4, 2022

# Release Notes

Use these release notes with the Cisco IP Phone 8845 Multiplatform Phones and Cisco IP Phone 8865 Multiplatform Phones running
                  SIP Firmware Release 11.3(6)SR1.

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 8845 Multiplatform Phones and Cisco IP Phone 8865 Multiplatform Phones

Cisco BroadWorks 24.0

MetaSphere CFS version 9.5

Asterisk 13.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone 8800 Series Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/index.html

## New and Changed Features

This release is a maintenance release and doesn't contain any new or enhanced features.

## Upgrade the Firmware

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

Click this link:

https://software.cisco.com/download/home/286318380

On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane.

Select your phone model in the right pane.

On the next page that is displayed, select Multiplatform Firmware .

On the next page that is displayed, select 11.3.6 MSR1 in the All Releases > MPPv11 folder.

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Download the corresponding file.

8845 and 8865: cmterm-8845_65.11-3-6MPP0102-277_REL.zip

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

8845 and 8865:

http://10.73.10.223/firmware/cmterm-8845_65.11-3-6MPP0102-277.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

8845 and 8865:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip8845_65.11-3-6MPP0102-277.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8845_65.11-3-6MPP0102-277.loads

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

Click one of the following links:

To view all caveats that affect this release:

To view open caveats that affect this release:

To view resolved caveats that affect this release:

When prompted, log in with your Cisco.com user ID and password.

(Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

## Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 8845 Multiplatform Phones
                     and Cisco IP Phone 8865 Multiplatform Phones that use Firmware Release 11.3(6)SR1.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCwb59080 No LCD display with certain hold-mute/unmute-resume sequence

CSCwb68352 Video phone camera light stay on after call hangs up

CSCwb71049 Video call may get stuck with Webex meeting and mute/unmute performed repeatedly

## Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 8845 Multiplatform Phones
                     and Cisco IP Phone 8865 Multiplatform Phones that use Firmware Release 11.3(6)SR1.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCwb04217 Setting NALU size base on negotiated value

CSCwb04221 Optimize the call of vcp_stop on MPP phone

CSCwb24990 Add one parameter to enable reboot at AM on Saturday

CSCwb15914 Add mutext protection on IDR request api

CSCwb29110 Optimize call flow between video phone and audio-only phone

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 8845 Multiplatform Phones and Cisco IP Phone 8865 Multiplatform Phones | Cisco BroadWorks 24.0 MetaSphere CFS version 9.5 Asterisk 13.0 |

| Step 1 | Click this link: https://software.cisco.com/download/home/286318380 On the Software Download web page that is displayed, ensure that IP Phone 8800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select your phone model in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | On the next page that is displayed, select 11.3.6 MSR1 in the All Releases > MPPv11 folder. |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the corresponding file. 8845 and 8865: cmterm-8845_65.11-3-6MPP0102-277_REL.zip |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: 8845 and 8865: http://10.73.10.223/firmware/cmterm-8845_65.11-3-6MPP0102-277.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: 8845 and 8865: https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip8845_65.11-3-6MPP0102-277.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip8845_65.11-3-6MPP0102-277.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=286311392&rls=11.3(6)&sb=anfr&bt=custV To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=&pf=prdNm&pfVal=286311392&rls=11.3(6)&sb=afr&bt=custV To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&rls=11.3(6)&sb=fr&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |