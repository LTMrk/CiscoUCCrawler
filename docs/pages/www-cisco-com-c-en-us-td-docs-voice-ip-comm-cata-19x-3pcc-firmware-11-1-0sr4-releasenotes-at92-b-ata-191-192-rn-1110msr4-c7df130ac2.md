---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cata-19x-3pcc-firmware-11-1-0sr4-releasenotes-at92-b-ata-191-192-rn-1110msr4-c7df130ac2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cata/19x/3PCC/firmware/11-1-0SR4/releasenotes/at92_b_ata-191_192_rn-1110msr4.html
retrieved_at: 2026-08-21T12:50:38.145995+00:00
---

Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.1(0)SR4

# Cisco ATA 191 and 192 Analog Telephone Adapter Release Notes for Multiplatform Firmware Release 11.1(0)SR4

### Download Options

Updated: November 5, 2020

First Published: October 28, 2020

# Release Notes

These release notes support the Cisco ATA 191 and 192 Analog Telephone Adapter for
                  				Multiplatform Firmware Release 11.1(0)SR4.

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

In the Latest Releases folder, choose 11.1.0 MSR4 .

Download the file ATA19x.11-1-0MPP0401-002.zip.

Unzip the files.

Put the files on the tftp/http/https download directory.

Configure the Upgrade Rule on the Provisioning tab in the
                                 					web page with the valid URL. The format is:

<schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img

Here is an example,

http://192.168.1.100/firmware/ATA19X.11-1-0MPP0401-002.img

After the firmware upgrade completes, the phone reboots
                                 					automatically.

## Caveats

### Access Cisco Bug Search

Known problems (bugs) are graded according to severity level. These release notes
                        				contain descriptions of the following:

All severity level 1 or 2 bugs

Significant severity level 3 bugs

You can search for problems by using Cisco Bug Search.

Before you begin

#### Before you begin

To access Cisco Bug Search, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

To access Cisco Bug Search, go to:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=274259360&rls=11.1(0)MSR4&sb=anfr&sts=fd&svr=6nH&bt=custV

Log in with your Cisco.com user ID and password.

To look for information about a specific problem, enter the bug ID number in
                                 					the Search for field, then press Enter .

### View Caveats

You can search for caveats using the Cisco Bug Search.

Known caveats (bugs) are graded according to severity level, and can be either open
                        				or resolved.

Before you begin

#### Before you begin

To view caveats, you need the following items:

Cisco.com user ID and password

Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319456&rls=11.1(0)MSR4&sb=anfr&sts=fd&svr=3nH&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

This release for Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones
                        does not have any open caveats.

### Resolved Caveats

The following list contains severity 1, 2, and 3 defects that are resolved for the
                        				Cisco ATA 191 and 192 Analog Telephone Adapter Multiplatform Phones for Firmware
                        				Release 11.1(0)MSR4.

For more information about an individual defect, access the Bug Search toolkit and
                        				search for the defect using the Identifier. You must be a registered Cisco.com user
                        				to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that
                        				were open at the time this report was compiled. For an updated view of open defects,
                        				access Bug Toolkit as described in Access Cisco Bug Search .

CSCvq10268: ATA191 crashes whenever it receives or makes a call to DX80
                              						endpoint

CSCvr44220: ATA19x MPP failed to response simultaneous incoming SIP INVITE
                              						under Webex Calling

CSCvr17698: ATA192 failed to finish conference call setup

CSCvs09327: ATA19x MPP network config cannot be configured by remote
                              						provisioning

CSCvq23757: Evaluation of 3pcc-ata191 for TCP SACK vulnerabilities

CSCvr44321: ATA19x MPP version Host name can not be provisioned

CSCvr44218: ATA191-MPP server can not parse the PRT file name when uploading
                              						with PUT method

CSCvr44220: ATA19x MPP failed to response simultaneous incoming SIP INVITE
                              						under Webex Calling

CSCvs24769: ATA19x MPP in reboot loop due to parameter not applied.

CSCvs24808: ATA19x MPP admin credentials don't take effect by provisioning
                              						after factory reset

CSCvs32158: CVE-2018-17972: Linux kernel proc_pid_stack function
                              						Vulnerability

CSCvs32168: CVE-2019-15916: Linux memory leak vulnerability in
                              						register_queue_kobjects()

CSCvs32174: CVE-2019-15214: Linux use-after-free vulnerability in the sound
                              						subsystem

CSCvs32179: CVE-2019-10638: Linux hash collisions vulnerability

CSCvs32187: CVE-2019-11190: Linux bypass ASLR on setuid programs
                              						vulnerability

CSCvs34025: CVE-2019-5482: Heap buffer overflow in the TFTP protocol handler
                              						in cURL 7.19.4 to 7.65.3

CSCvs34770: ATA191 does not recognize HTTP '204' response from Broadsoft as
                              						successful PRT upload

CSCvs76201: ATA191 MPP does not send voice after changing the rtp media
                              						port

CSCvu04381: ATA191 MPP DNS dead loop issue when upgrading

CSCvu04390: ATA191 MPP crash when auto upgrade on webex calling with http chunk modeATA191
                              						MPP sprvoip crash loop when auto upgrade on webex calling server

CSCvt65602: ATA191 MPP Extend SIP auth password max length from 39 to 128

CSCvt65593: MPP ATA19x two lines register to the different SBCs in SRV case

CSCvv15157: ATA191 MPP failover register outage when TCP and not initiate
                              						invite when UDP

CSCvu04372: ATA19x MPP report invalid rule when the conditional upgrade and provision have
                              						version compare

CSCvu83297: ATA19x Host name will be changed to default value when set <Host_Name> NULL
                              						value via provision/web

CSCvu83296: ATA192 can not access web after enable remote management via
                              						provision

CSCvv21496: ATA fail to do full factory reset via TR069

CSCvv15925: ATA19x fail to download configuration file if HTTP response doesn't have
                              						content-length header

CSCvv45800: IPv4 Settings page not being displayed (404) when logged in as
                              						user

CSCvv45849: Add LED indication for RESET button factory reset case

CSCvv46175: ATA19x unregister caused by hostname change when dhcp renew

CSCvv70173: ATA19x MPP support provision SAN check with the parameter
                              						HTTPS_Name_Validate

CSCvv62356: ATA19x Message Waiting Indicator (MWI) not functioning on analog
                              						phones

CSCvv81235: ATA19x try DNS query with each server strictly in the order of DNS servers

CSCvw15173: ATA19x DHCP discover/request host name header is not changeable

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

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
| Step 4 | In the Latest Releases folder, choose 11.1.0 MSR4 . |
| Step 5 | Download the file ATA19x.11-1-0MPP0401-002.zip. |
| Step 6 | Unzip the files. |
| Step 7 | Put the files on the tftp/http/https download directory. |
| Step 8 | Configure the Upgrade Rule on the Provisioning tab in the
                                 					web page with the valid URL. The format is: <schema>://<serv_ip[:port]>/filepath/ATA19x.xxxx.img Here is an example, http://192.168.1.100/firmware/ATA19X.11-1-0MPP0401-002.img After the firmware upgrade completes, the phone reboots
                                 					automatically. |

| Step 1 | To access Cisco Bug Search, go to: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=274259360&rls=11.1(0)MSR4&sb=anfr&sts=fd&svr=6nH&bt=custV |
|---|---|
| Step 2 | Log in with your Cisco.com user ID and password. |
| Step 3 | To look for information about a specific problem, enter the bug ID number in
                                 					the Search for field, then press Enter . |

| Step 1 | Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286319456&rls=11.1(0)MSR4&sb=anfr&sts=fd&svr=3nH&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |