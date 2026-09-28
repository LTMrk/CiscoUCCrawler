---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-firmware-11-1-0sr3-releasenotes-at92-b-ata-191-and-192-release-761ee67c0f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/firmware/11-1-0SR3/releasenotes/at92_b_ata-191-and-192-release.html
retrieved_at: 2026-08-22T01:11:40.383168+00:00
---

Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones Release Notes for Firmware Release 11.1(0)SR3

# Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones Release Notes for Firmware Release 11.1(0)SR3

### Download Options

Updated: June 13, 2019

First Published: June 13, 2019

# Release Notes for Cisco ATA 191 and 192 Analog Telephone Adapter for Multiplatform Firmware Release 11.1(0)SR3

These release notes support the Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones running Multiplatform
                  Firmware Release 11.1(0)SR3.

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

In the Latest Releases folder, choose 11.1.0 MSR3 .

Download the file ATA19x.11-1-0MSR3.zip.

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

Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319456&rls=11.1(0)MSR3&sb=anfr&sts=fd&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

Firmware Release 11.1(0)SR3 for Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones does not have any open
                        caveats.

### Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the Cisco ATA 191 and 192 Analog Telephone
                        Adapter Multiplatform Phones for Firmware Release 11.1(0)SR3.

For more information about an individual defect, access the Bug Search toolkit and search for the defect using the Identifier.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCvi62887: DUT does not retry all IP addresses during downloading profile rule

CSCvm13724: ATA191-3PCC: renaming of PRT file

CSCvm15413: ATA191-3PCC : router part of configuration file size limitation

CSCvp08964: PCM capture typo on web ui

CSCvp14263: "show phone information" displays SPA122 information for ATA 191

CSCvp55388: HTTP profile account support

CSCvp55393: DUT should NOT reboot when downloading fail during upgrade

CSCvp55414: Feature Request- "PRT Name" which also supports MACRO expansion

CSCvp60813: Incorrectly and inconsistently handle HTTP auth in provision

CSCvp55406: SIP TLS SAN check support

CSCvn87582: CVE-2018-18559: Linux Kernel Use-After-Free Race Condition Vulnerability

CSCvn87638: cURL and libcurl NTLM Password Buffer Overflow Vulnerability

CSCvn87692: Vulnerable version of busybox in use

CSCvi58046: Click 'generate PRT' on web does not work correctly.

CSCvp05857: CVE-2019-5747 CVE-2018-20679 Multiple Vulnerabilities in busybox

CSCvi62569: The web protocol change via provision needs power cycle to apply

CSCvh61339: The log file name should use system current time but ATA stick in GMT+8

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

Anything that degrades network performance can affect phone voice and in some cases can cause a call to drop. Sources of
                        network degradation can include, but are not limited to, the following activities:

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
| Step 4 | In the Latest Releases folder, choose 11.1.0 MSR3 . |
| Step 5 | Download the file ATA19x.11-1-0MSR3.zip. |
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

| Step 1 | Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319456&rls=11.1(0)MSR3&sb=anfr&sts=fd&svr=3nH&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |

| Step 1 | To access Cisco Bug Search, go to: https://tools.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                                 			 Cisco.com user ID and password. |
| Step 3 | To look for
                                 			 information about a specific problem, enter the bug ID number in the Search for
                                 			 field, then press Enter . |