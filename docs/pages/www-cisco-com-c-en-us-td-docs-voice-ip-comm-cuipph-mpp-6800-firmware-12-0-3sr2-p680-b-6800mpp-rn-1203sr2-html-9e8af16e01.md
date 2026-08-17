---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-6800-firmware-12-0-3sr2-p680-b-6800mpp-rn-1203sr2-html-9e8af16e01
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/6800/firmware/12-0-3sr2/p680_b_6800mpp-rn-1203sr2.html
retrieved_at: 2026-08-17T01:05:49.363635+00:00
---

Cisco IP Phone 6821 Multiplatform Phones Release Notes for Firmware Release 12.0(3)SR2

# Cisco IP Phone 6821 Multiplatform Phones Release Notes for Firmware Release 12.0(3)SR2

- 12.0(3)SR2

- 11.2(2)

### Download Options

Updated: October 17, 2024

First Published: October 17, 2024

# Release Notes

This release contains only internal changes to optimize manufacturing process.

Use these release notes with the  running SIP Firmware Release 12.0(3)SR2.

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 6821 Multiplatform Phones

Cisco BroadWorks 23.0

MetaSphere CFS version 9.5

Asterisk 11.0

## New and Changed Features

This release is a maintenance release and doesn't contain any new or enhanced features.

## Cisco IP Phone 6800 Series Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                     following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/tsd-products-support-series-home.html

## Upgrade the Firmware

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

Step 1

Click this link:

https://software.cisco.com/download/home/286318380

On the Software Download web page that is displayed, ensure that IP Phone 6800 Series with Multiplatform Firmware is selected in the middle pane.

Step 2

Select your phone model in the right pane.

Step 3

On the next page that is displayed, select Multiplatform Firmware .

Step 4

Under All Release , select the MPPv12 folder, then select the 12.0.3SR2 folder.

Step 5

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Step 6

Download the file cmterm-6821.12-0-3MPP0203-204_REL.zip .

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

http://10.73.10.223/firmware/sip6821.12-0-3MPP0203-204.loads

https://server.domain.com/firmware/sip6821.12-0-3MPP0203-204.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

```
https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip6821.12-0-3MPP0203-204.loads
```

```
https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip6821.12-0-3MPP0203-204.loads
```

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

Step 1

Click one of the following links:

To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch?pf=prdNm&sb=anfr&rls=12.0(2)&kw=*&bt=custV&prdNam=Cisco%20IP%20Phone%206800%20Series%20with%20Multiplatform%20Firmware

To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=afr&rls=12.0(2)&kw=*&bt=custV&prdNam=Cisco%20IP%20Phone%206800%20Series%20with%20Multiplatform%20Firmware

To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=fr&rls=12.0(2)&kw=*&bt=custV&prdNam=Cisco%20IP%20Phone%206800%20Series%20with%20Multiplatform%20Firmware

Step 2

When prompted, log in with your Cisco.com user ID and password.

Step 3

(Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

## Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 6800 Series Multiplatform Phones that use Firmware Release 12.0(3)SR2.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in View Caveats .

CSCwb46008 Many PRTs with logs missing for around 5 seconds.

## Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 6800 Series Multiplatform Phones that use Firmware Release 12.0(3)SR2.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in View Caveats .

CSCwm86242 6821-v06 stuck in a reboot loop due to short of memory.

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 6821 Multiplatform Phones | Cisco BroadWorks 23.0 MetaSphere CFS version 9.5 Asterisk 11.0 |

| Step 1 | Click this link: https://software.cisco.com/download/home/286318380 On the Software Download web page that is displayed, ensure that IP Phone 6800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select your phone model in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | Under All Release , select the MPPv12 folder, then select the 12.0.3SR2 folder. |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the file cmterm-6821.12-0-3MPP0203-204_REL.zip . |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: http://10.73.10.223/firmware/sip6821.12-0-3MPP0203-204.loads https://server.domain.com/firmware/sip6821.12-0-3MPP0203-204.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip6821.12-0-3MPP0203-204.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip6821.12-0-3MPP0203-204.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch?pf=prdNm&sb=anfr&rls=12.0(2)&kw=*&bt=custV&prdNam=Cisco%20IP%20Phone%206800%20Series%20with%20Multiplatform%20Firmware To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=afr&rls=12.0(2)&kw=*&bt=custV&prdNam=Cisco%20IP%20Phone%206800%20Series%20with%20Multiplatform%20Firmware To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=fr&rls=12.0(2)&kw=*&bt=custV&prdNam=Cisco%20IP%20Phone%206800%20Series%20with%20Multiplatform%20Firmware |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |