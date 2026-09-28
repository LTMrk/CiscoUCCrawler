---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-firmware-11-1-1sr1-releasenotes-at92-b-mpp-release-1110sr1-ata-4f46149834
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/firmware/11-1-1SR1/releasenotes/at92_b_mpp-release-1110sr1-ata-191.html
retrieved_at: 2026-08-22T01:11:50.570761+00:00
---

Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones Release Notes for Firmware Release 11.1(0)SR1

# Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones Release Notes for Firmware Release 11.1(0)SR1

### Download Options

Updated: May 30, 2018

First Published: May 30, 2018

# Release Notes for Cisco ATA 191 and 192 Analog Telephone Adapter for Multiplatform Firmware Release 11.1(0)SR1

These release notes support the Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones running Multiplatform
                  Firmware Release 11.1(0)SR1.

The following table lists the support and protocol compatibility for the Cisco ATA.

Cisco IP Phone

Protocol

Support Requirements

Cisco ATA 191 and 192

SIP

BroadSoft BroadWorks 21.0

Asterisk 13.1

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco ATA 190 Series Documentation

Refer to publications that are specific to your language and call control system. Navigate from the following documentation
                        URL:

https://www.cisco.com/c/en/us/products/unified-communications/ata-190-series-analog-telephone-adapters/index.html

## Installation

### Upgrade Firmware

The Cisco ATA 191 and 192 support dual image upgrades by TFTP, HTTP, or HTTPS.

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286282490&flowid=83468

Choose Cisco ATA 190 Series .

Choose your ATA model.

In the Latest Releases folder, choose 11.1.0 MSR1-1 .

Download the file ATA19x.11-1-0MSR1-1.zip.

Unzip the files.

Put the files on the tftp/http/https download directory.

Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is:

<schema>://<serv_ip[:port]>/filepath/sipxxx.loads

The third-party call control can also upgrade with a URL in the web browser:

<schema>://<serv_ip[:port]>/filepath/sipxxx.loads

Here is an example,

http://10.74.10.225/firmware/sipXXX.XX-0-0MPP-XXdev.loads

The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file
                                                is used in the above URL.

After the firmware upgrade completes, the phone reboots automatically.

## Caveats

### View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

#### Before you begin

To view caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%2011.1.0MSR1&pf=prdNm&sb=null%20&sts=open&bt=custV

Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%2011.1.0MSR1&pf=prdNm&sb=null&sts=fd&bt=custV

Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%2011.1.0MSR1&pf=prdNm&sb=anfr&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

The following table lists severity 1, 2, and 3 defects that are open for the Cisco ATA 191 and 192 Analog Telephone Adapter
                        Multiplatform Phones for Firmware Release 11.1(0)SR1.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

Identifier

Description

CSCvg01656

DUT connect to half duplex Ethernet port can't link up after power on

### Resolved Caveats

The following table lists severity 1, 2, and 3 defects that are resolved for the Cisco ATA 191 and 192 Analog Telephone Adapter
                        Multiplatform Phones for Firmware Release 11.1(0)SR1.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

Identifier

Description

CSCvh28785

Some analog phone cannot display call waiting callerID

CSCvh29694

DUT can't download configuration file with IP address via IPv6 TR069

CSCvh29800

DUT can't download firmware via IPv6 TR069

CSCvh28384

Modem call does not connect successfully

CSCvh28202

ATA does not handle RTP send/receive in different IP stack

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

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video
                        		  quality, and in some cases, can cause a call to drop. Sources of network
                        		  degradation can include, but are not limited to, the following activities:

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco ATA 191 and 192 | SIP | BroadSoft BroadWorks 21.0 Asterisk 13.1 |

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=286282490&flowid=83468 |
|---|---|
| Step 2 | Choose Cisco ATA 190 Series . |
| Step 3 | Choose your ATA model. |
| Step 4 | In the Latest Releases folder, choose 11.1.0 MSR1-1 . |
| Step 5 | Download the file ATA19x.11-1-0MSR1-1.zip. |
| Step 6 | Unzip the files. |
| Step 7 | Put the files on the tftp/http/https download directory. |
| Step 8 | Configure the Upgrade Rule on the Provisioning tab in the web page with the valid URL. The format is: <schema>://<serv_ip[:port]>/filepath/sipxxx.loads The third-party call control can also upgrade with a URL in the web browser: <schema>://<serv_ip[:port]>/filepath/sipxxx.loads Here is an example, http://10.74.10.225/firmware/sipXXX.XX-0-0MPP-XXdev.loads Note The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file
                                                is used in the above URL. After the firmware upgrade completes, the phone reboots automatically. | Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file
                                                is used in the above URL. |
| Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file
                                                is used in the above URL. |

| Note | The loads file is put in the file path of the above url. The zip file contains other file types also. Only the loads file
                                                is used in the above URL. |
|---|---|

| Step 1 | Perform one of the following actions: Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%2011.1.0MSR1&pf=prdNm&sb=null%20&sts=open&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%2011.1.0MSR1&pf=prdNm&sb=null&sts=fd&bt=custV Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=Customer%20visible%20bug%20for%2011.1.0MSR1&pf=prdNm&sb=anfr&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |

| Identifier | Description |
|---|---|
| CSCvg01656 | DUT connect to half duplex Ethernet port can't link up after power on |

| Identifier | Description |
|---|---|
| CSCvh28785 | Some analog phone cannot display call waiting callerID |
| CSCvh29694 | DUT can't download configuration file with IP address via IPv6 TR069 |
| CSCvh29800 | DUT can't download firmware via IPv6 TR069 |
| CSCvh28384 | Modem call does not connect successfully |
| CSCvh28202 | ATA does not handle RTP send/receive in different IP stack |

| Step 1 | To access Cisco Bug Search, go to: https://tools.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                                 			 Cisco.com user ID and password. |
| Step 3 | To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter . |