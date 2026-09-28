---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7832-firmware-11-1-2sr1-cs78-b-release-notes-for-7832mpp-1112sr1--3a7658a22d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7832/firmware/11-1-2sr1/cs78_b_release-notes-for-7832mpp-1112sr1.html
retrieved_at: 2026-08-21T23:18:23.616505+00:00
---

Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.1(2)SR1

# Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.1(2)SR1

### Download Options

Updated: August 31, 2018

First Published: August 31, 2018

# Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.1(2)SR1

Use these release notes with the Cisco IP Conference Phone 7832 Multiplatform Phones running SIP Firmware Release 11.1(2)SR1.

The following table describes the individual phone requirements.

Phone

Support Requirements

Cisco IP Conference Phone 7832 Multiplatform Phones

BroadSoft BroadWorks 21.0

MetaSphere CFS version 9.4

Asterisk 13.1

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Conference Phone 7832 Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation
                        URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/tsd-products-support-series-home.html

## New and Changed
               	 Features

The following sections describe the features that are new or have
                  		changed in this release.

### New Domain Support while Provisioning

When a phone connects to a network for the first time or after a factory reset, if there are no DHCP options setup, it contacts
                        a device activation server for zero touch provisioning. Starting with this firmware release, phones will use activate.cisco.com instead of webapps.cisco.com for provisioning. Phones with older versions of the firmware will continue to use webapps.cisco.com . Cisco recommends that you allow both the domain names through your firewall.

#### Where to Find More Information

Cisco IP Phone 7800 Series and Cisco IP Conference Phone 7832 Multiplatform Phones Provisioning Guide

## Upgrade the Firmware

The Cisco IP Conference Phone 7832 Multiplatform Phones support a single image upgrade using TFTP, HTTP, or HTTPS protocols with a URL.

After the firmware upgrade completes, the phone reboots automatically.

Click the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286311381&i=rm

Select IP Phone 7800 Series with Multiplatform Firmware in the center pane.

Select IP Conference Phone 7832 with Multiplatform Firmware in the right pane.

Select the Multiplatform Firmware software type.

Under Latest , select the 11.1.2 MSR1-1 folder.

(Optional) Place your mouse pointer on the filename to display the file details and checksum values.

Download the cp-7832.11-1-2MSR1-1_REL.zip file.

Click Accept License Agreement when you accept the software license.

Unzip the firmware files.

Put the files in the TFTP, HTTP, or HTTPS download directory.

Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL.

Use the URL format– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

You can also upgrade the third-party call control by using a URL in a web browser– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads

Example

https://10.74.10.225/firmware/sip7832.11-1-2MSR1-1.loads

Use the *.loads file in the URL. The *.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call
                        to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

## Caveats

### Access Cisco Bug
                  	 Search

Known problems
                        		  (bugs) are graded according to severity level. These release notes contain
                        		  descriptions of the following:

All severity
                              				level 1 or 2 bugs

Significant
                              				severity level 3 bugs

You can search for
                        		  problems by using Cisco Bug Search.

Before you begin

#### Before you begin

To access Cisco Bug
                        		  Search, you need the following items:

Internet
                              				connection

Web browser

Cisco.com user
                              				ID and password

To access Cisco Bug Search, go to:

https://tools.cisco.com/bugsearch

Log in with your
                                 			 Cisco.com user ID and password.

To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter .

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Conference Phone 7832 Multiplatform Phones that use Firmware Release 11.1(2)SR1.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this
                        report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described
                        in the Access Cisco Bug Search .

CSCvi20892 Phone reboots when it has an incoming page call and maximum number calls.

CSCvi57576 Phone can only receive 5 calls but the phone screen GUI shows 8 calls.

CSCvi59903 Phone screen GUI displays Anonymous when changing the dial plan.

CSCvi88531 Different behavior of call status for shared conference bridge from private conference bridge.

CSCvi90594 Phone may un-register when switching between call history and personal directory.

CSCvi96787 Secure call one way-audio if the caller and callee's SDP support IP mode and use secondary dial steps.

CSCvi98838 Missing Back softkey when edit settings of the Enterprise Directory using the phone screen.

CSCvi99554 Secure call transfer, no audio if transferee and person transferring the call have different SIP & SDP preference
                              modes.

CSCvj01440 Setting the wrong static IP, GW, or DNS at same time does not overwrite the older phone configuration.

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Conference Phone 7832 Multiplatform Phones that use Firmware Release 11.1(2)SR1.

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier. You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                        this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                        as described in the Access Cisco Bug Search .

CSCvj07154 CP-88xx-3PCC - Unable to hear beep from voicemail server

CSCvj59089 Phone fails to provision using TR-69

CSCvj84294 Can not open phone's web page with Chrome browser(Ver:67.0.3396.79)

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Requirements |
|---|---|
| Cisco IP Conference Phone 7832 Multiplatform Phones | BroadSoft BroadWorks 21.0 MetaSphere CFS version 9.4 Asterisk 13.1 |

| Step 1 | Click the following URL: https://software.cisco.com/download/navigator.html?mdfid=286311381&i=rm |
|---|---|
| Step 2 | Select IP Phone 7800 Series with Multiplatform Firmware in the center pane. |
| Step 3 | Select IP Conference Phone 7832 with Multiplatform Firmware in the right pane. |
| Step 4 | Select the Multiplatform Firmware software type. |
| Step 5 | Under Latest , select the 11.1.2 MSR1-1 folder. |
| Step 6 | (Optional) Place your mouse pointer on the filename to display the file details and checksum values. |
| Step 7 | Download the cp-7832.11-1-2MSR1-1_REL.zip file. |
| Step 8 | Click Accept License Agreement when you accept the software license. |
| Step 9 | Unzip the firmware files. |
| Step 10 | Put the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 11 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. Use the URL format– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads You can also upgrade the third-party call control by using a URL in a web browser– <protocol>://<serv_ip[:port]>/<filepath>/sipxxx.loads Example https://10.74.10.225/firmware/sip7832.11-1-2MSR1-1.loads Note Use the *.loads file in the URL. The *.zip file contains other files. | Note | Use the *.loads file in the URL. The *.zip file contains other files. |
| Note | Use the *.loads file in the URL. The *.zip file contains other files. |

| Note | Use the *.loads file in the URL. The *.zip file contains other files. |
|---|---|

| Step 1 | To access Cisco Bug Search, go to: https://tools.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                                 			 Cisco.com user ID and password. |
| Step 3 | To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter . |