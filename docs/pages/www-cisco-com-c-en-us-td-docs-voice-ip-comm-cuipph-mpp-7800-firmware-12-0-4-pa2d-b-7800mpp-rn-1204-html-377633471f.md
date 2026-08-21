---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-firmware-12-0-4-pa2d-b-7800mpp-rn-1204-html-377633471f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/firmware/12-0-4/pa2d_b_7800mpp-rn-1204.html
retrieved_at: 2026-08-21T23:18:52.570136+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 12.0(4)

# Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 12.0(4)

### Download Options

Updated: January 30, 2024

First Published: January 30, 2024

# Release Notes

Use these release notes with the Cisco IP Phone 7800 Series Multiplatform Phones running SIP Firmware Release 12.0(4).

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Phone 7800 Series Multiplatform Phones

Cisco BroadWorks RI

MetaSphere CFS version 9.5

Asterisk 18.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone 7800 Series Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/index.html

## New and Changed Features

### Administrator Sets Preferred Value

With the Firmware release 12.0(4), you can set preferred values for user with the attribute user-pref to provide them a seamless experience. Also, further changes made by the user using the phone or from the phone administration
                        web page is preserved.

#### Where to Fine More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

### Call Park Extension Enhancement

This feature lets admin to configure specific line keys (using extended function configuration) for monitoring Call Park Extension.
                        As a result, only a single button is required to park/unpark a call.

To enable this feature from the phone administration web page, navigate to Voice > Att Console > General and set the BLF Callpark On Line Key Enable parameter to Yes .

#### Where to Find More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

### LLDP X-SWITCH-INFO Support for E911

For enterprises that might use nomadic 911 capabilities, public and private IP addresses are not sufficient to identify a
                        specific location. In such scenarios, it is recommended to utilize the network switching infrastructure to help determine
                        the client’s location. In this approach, customer can add relevant network switches and switch ports into the map for a location
                        or sub-location, and need to probe for and report their respective switch ports when reporting network data, as part of the
                        emergency call flow.

To enable this feature from the phone administration web page for both wired and wireless phones, choose the X-SWITCH-INFO Support parameter from the Voice > System > Optional Network Configuration .

#### Where to Find More Information

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

### Support for One Call Per Line

With the Firmware release 12.0(4), you can configure a line to allow only one call at a time.

You can use the Call Appearances Per Line parameter in the phone administration web page from Voice > Phone to configure this feature.

#### Where to Fine More Information

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

Cisco IP Desk Phone with Multiplatform Firmware (MPP) － Administration Guide

XML Reference Guide for Cisco IP Phone Multiplatform Phones

## Upgrade Firmware

You can upgrade the phone firmware with TFTP, HTTP, or HTTPS. After the upgrade completes, the phone reboots automatically.

Step 1

Click this link:

https://software.cisco.com/download/home/286318380

On the Software Download web page that is displayed, ensure that IP Phone 7800 Series with Multiplatform Firmware is selected in the middle pane.

Step 2

Select your phone model in the right pane.

Step 3

On the next page that is displayed, select Multiplatform Firmware .

Step 4

On the next page that is displayed, select 12.0.4 in the All Releases > MPPv12 folder.

Step 5

(Optional) Place your mouse pointer on the file name to see the file details and checksum values.

Step 6

Download the corresponding file.

cmterm-78xx.12-0-4MPP0001-195_REL.zip

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

http://10.73.10.223/firmware/sip78xx.12-0-4MPP0001-195.loads

https://server.domain.com/firmware/sip78xx.12-0-4MPP0001-195.loads

Click Submit All Changes .

Upgrade the phone firmware directly from your web browser:

In the address bar of your web browser, enter the phone upgrade URL as described below.

Phone upgrade URL format:

Load file URL format:

<upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads

Examples:

https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip78xx.12-0-4MPP0001-195.loads

https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip78xx.12-0-4MPP0001-195.loads

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

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 7800 Series Multiplatform Phones that use Firmware Release 12.0(3).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCwf10956—Macro $SERVIP is not expanded in Log Request Msg in syslog.

CSCwf70230—78xx is stripping leading "+" when dialling from the monitored line button without extension.

- CSCwi60009—MPP should retry call park resume in race condition scenario with incoming call

## Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series Multiplatform Phones that use Firmware Release 12.0(4).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                     tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                     this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                     as described in the View Caveats .

CSCwh14446—MPP is losing registration randomly.

CSCwf29727—Hard transfer button does not transfer.

- CSCwh64092—MPP 7861 BLF call park resume failed by pressing line key multiple times.

CSCwi66404—'Mute' cannot be disabled on a call to a predefined emergency number.

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Phone | Support Requirements |
|---|---|
| Cisco IP Phone 7800 Series Multiplatform Phones | Cisco BroadWorks RI MetaSphere CFS version 9.5 Asterisk 18.0 |

| Step 1 | Click this link: https://software.cisco.com/download/home/286318380 On the Software Download web page that is displayed, ensure that IP Phone 7800 Series with Multiplatform Firmware is selected in the middle pane. |
|---|---|
| Step 2 | Select your phone model in the right pane. |
| Step 3 | On the next page that is displayed, select Multiplatform Firmware . |
| Step 4 | On the next page that is displayed, select 12.0.4 in the All Releases > MPPv12 folder. |
| Step 5 | (Optional) Place your mouse pointer on the file name to see the file details and checksum values. |
| Step 6 | Download the corresponding file. cmterm-78xx.12-0-4MPP0001-195_REL.zip |
| Step 7 | Click Accept License Agreement . |
| Step 8 | Unzip the file and place the files in the appropriate location on your upgrade server. The appropriate location is the TFTP, HTTP, or HTTPS download folder, depending on the protocol that you want to use for the
                                 upgrade. |
| Step 9 | Upgrade the phone firmware with one of these methods. Upgrade the phone firmware from the phone administration web page: On the phone administration web page, go to Admin Login > Advanced , Voice > Provisioning > Firmware Upgrade . In the Upgrade Rule field, enter the load file URL as described below. Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: http://10.73.10.223/firmware/sip78xx.12-0-4MPP0001-195.loads https://server.domain.com/firmware/sip78xx.12-0-4MPP0001-195.loads Click Submit All Changes . Upgrade the phone firmware directly from your web browser: In the address bar of your web browser, enter the phone upgrade URL as described below. Phone upgrade URL format: <phone protocol>://<phone ip address[:port]>/admin/upgrade?<load file URL> Load file URL format: <upgrade protocol>://<upgrade server ip address>[:<port>]>/<path>/<file name>.loads Examples: https://10.74.10.225/admin/upgrade?http://10.73.10.223/firmware/sip78xx.12-0-4MPP0001-195.loads https://10.74.10.225/admin/upgrade?https://server.domain.com/firmware/sip78xx.12-0-4MPP0001-195.loads Note Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. | Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |

| Note | Specify the <file name>.loads file in the URL. The <file name>.zip file contains other files. |
|---|---|

| Step 1 | Click one of the following links: To view all caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=anfr&prdNam=Cisco%20IP%20Phone%207800%20Series%20with%20Multiplatform%20Firmware&kw=*&bt=custV&rls=12.0(3) To view open caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=afr&kw=*&bt=custV&rls=12.0(4)&prdNam=Cisco%20IP%20Phone%207800%20Series%20with%20Multiplatform%20Firmware To view resolved caveats that affect this release: https://bst.cloudapps.cisco.com/bugsearch/search?pf=prdNm&sb=fr&kw=*&bt=custV&rls=12.0(4)&prdNam=Cisco%20IP%20Phone%207800%20Series%20with%20Multiplatform%20Firmware |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) For information about a specific caveat, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |