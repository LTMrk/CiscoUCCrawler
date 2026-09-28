---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7821-7841-7861-firmware-10-1-1sr2-english-releasenotes-pa2d-bk-r26463-f431bb6d05
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7821_7841_7861/firmware/10-1-1SR2/english/releasenotes/PA2D_BK_R264634B_00_rn-7821-7841-7861-10_1_1_sr2/PA2D_BK_R264634B_00_rn-7821-7841-7861-10_1_1_sr2_chapter_00.html
retrieved_at: 2026-08-25T12:27:30.946948+00:00
---

Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)SR2

# Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)SR2

Updated: April 1, 2015

Chapter: Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)SR2

## Chapter: Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)SR2

# Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)SR2

## Introduction

These release notes
		support the Cisco IP Phones 7821, 7841, and 7861 running SIP Firmware Release
		10.1(1)SR2.

The following table
		lists the Cisco Unified Communications Manager release and protocol
		compatibility for the Cisco IP Phones.

Cisco IP Phone

Protocol

Cisco Unified
				Communications Manager

Cisco IP
				Phones 7821, 7841, and 7861

SIP

Cisco Unified Communications Manager Release 8.5(1) or later

Cisco Unified
				Communications Manager DST Olsen version D or later

## New and Changed Features

This release contains no new or changed features.

## Related
	 Documentation

- Cisco IP Phone 7800 Series Documentation

- Cisco Unified
				Communications Manager Documentation

### Cisco IP Phone 7800 Series Documentation

Refer to
		  publications that are specific to your language, phone model and Cisco Unified
				Communications Manager release. Navigate from the following
		  documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​collaboration-endpoints/​unified-ip-phone-7800-series/​tsd-products-support-general-information.html

### Cisco Unified
				Communications Manager Documentation

See the Cisco Unified
				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
				Communications Manager release. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​tsd-products-support-series-home.html

## Installation

- Installation Requirements

- Install the Firmware Release on the Cisco Unified Communications Manager

- Install the Firmware Zip Files

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications Manager is running the latest device pack.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​compat/​devpack_​comp_​mtx.html .

### Install the Firmware Release on the Cisco Unified Communications Manager

Before using the
		  Cisco IP Phone Firmware Release 10.1(1)SR2 with Cisco Unified
		  Communications Manager, you must install the latest firmware on all Cisco
		  Unified Communications Manager servers in the cluster.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm

cmterm-78xx.10-1-1SR2-1.cop.sgn

If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file.

### Install the Firmware Zip Files

If a Cisco Unified
		  Communications Manager is not available to load the installer program, the
		  following .zip files are available to load the firmware.

cmterm-78xx.10-1-1SR2-1.zip

Firmware upgrades
		  over the WLAN interface may take longer than upgrades using a wired connection.
		  Upgrade times over the WLAN interface may take more than an hour, depending on
		  the quality and bandwidth of the wireless connection.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm

## Limitations and Restrictions

### Voice VLAN and
	 IPv6 Limitation

If the PC attached to the PC port of the phone is using IPv6, we
		  recommend that the PC Voice LAN access be disabled. This ensures that the PC
		  can connect to the Voice VLAN.

### Phone Behavior During Times of Network Congestion

Anything that degrades network performance can
affect  Cisco IP Phone voice
and video quality, and in some cases, can
cause a call to drop. Sources of
network degradation can include, but are not limited to, the
following activities:

Administrative
tasks, such as an internal port scan or security scan

Attacks that
occur on your network, such as a Denial of Service
attack

To reduce or eliminate any adverse effects
to the phones, schedule administrative network tasks during a
time when the phones are not being used or exclude the phones
from testing.

## Unified
	 Communications Manager Endpoints Locale Installer

By default, Cisco
		  IP Phones are set up for the English (United States) locale. To use the Cisco
		  IP phones in other locales, you must install the locale-specific version of the
		  Unified Communications Manager Endpoints Locale Installer on every Cisco
		  Unified Communications Manager server in the cluster. The Locale Installer
		  installs the latest translated text for the phone user interface and
		  country-specific phone tones on your system so that they are available for the
		  Cisco IP Phones.

To access the
		  Locale Installer required for a release, access http:/​/​software.cisco.com/​download/​navigator.html?mdfid=286037605&flowid=46245 , navigate to your phone model, and
		  select the Unified Communications Manager Endpoints Locale Installer link.

For more
		  information, see the "Locale
			 Installer" section in the Cisco Unified
			 Communications Operating System Administration Guide .

The latest
			 Locale Installer may not be immediately available; continue to check the
			 website for updates.

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
		  problems by using the Cisco Bug Search.

To access Cisco Bug
		  Search, you need the following items:

Internet
				connection

Web browser

Cisco.com user
				ID and password

https:/​/​tools.cisco.com/​bugsearch

### Open Caveats

The following
		table lists severity 1, 2, and 3 defects that are open for the Cisco IP Phones
		for Firmware Release 10.1(1)SR2.

For more
		information about an individual defect, you can access the online record for
		the defect by clicking the Identifier or going to the URL that is shown. You
		must be a registered Cisco.com user to access this online information.

Because defect
		status continually changes, the table reflects a snapshot of the defects that
		were open at the time this report was compiled. For an updated view of open
		defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCuh34236

Display of phone is incorrect when PC port/SW port is 10/10

CSCuj16464

Monitoring phone not send RTCP

CSCuj25165

Highlighted background has afterimage when switch among calls
on 7861

CSCuj52759

IPv6 mode phone fail to register if CUCM v4/v6 hostname are
different

CSCuj73412

one log recorded when the call is transferred with translation
pattern

CSCuj93181

Group pickup; the call log should not recorded group number

CSCuj96094

DND beep not played when on hook from handset

CSCul01193

Phone can't add participant by PD in conference/transfer

CSCul19068

It will flash secure icon one time after answer a call

CSCul28593

The line with '#' in the DN still display on phone's ui in srst
mode

CSCun07043

DN displaying wrongly during transfer in 7841 phone Model

CSCun30345

78xx :line Led behavior wrong if phone has incoming and hold
revert call

CSCun35603

missed call number not increased accordingly

CSCun35740

78xx can't access VM when setting media using ipv6 prefer.

CSCun38492

Kate overlap the SK

CSCun45084

incoming call toast behavior not consentaneous

CSCun45099

extra cursor on 7861 when dial quick after cancel previous
dialing

CSCun45165

Call is dropped unexpectedly after pressing resume softkey

CSCun45175

local/remote ipv6 addr under stream info error in webpage

CSCun45190

arabic/Hebrew:v6 gateway/v6 dns/tftp v6 address orientation is
wrong

CSCun46787

7861:UI still display missed calls state if remote call in
hold

CSCun47366

line key flashing too long time for broadcast huntgroup

CSCun47509

call bubble not show for huntgroup number

CSCun50485

78xx Can not use the default gateway as SRST

CSCun51311

not support the 32-bit SRTCP

CSCun60728

7800 series phones not formatting special characters for http
get

CSCuo17616

Event Duration for Digit 0 is too short

CSCuo62751

TVS keeps trying when CUCM TVS server do not respond

CSCuo64932

Phone should reject EAP-MD5 auth request

CSCuo69837

Display issue after secure call change to non-secure

CSCuo70124

Error happened after pressing line key during transfer in
SRST

CSCuo72188

Call can't be hold after pressing hold key during conference in
SRST

CSCuo75012

7861: Call forward info display error after enable Redirected
Number

CSCuo80370

Dpark pfk error after phone fallback from srst

CSCuo89757

7861 will reset after receiving many simultaneous calls in load
test

CSCuo95583

78xx Phone doesn't play out of sequence rtp packets

### Resolved Caveats

The following
		table lists severity 1, 2, and 3 defects that are resolved for the Cisco IP
		Phones that use Firmware Release 10.1(1)SR2.

For more
		information about an individual defect, you can access the online record for
		the defect by clicking the Identifier or going to the URL that is shown. You
		must be a registered Cisco.com user to access this online information.

Because defect
		status continually changes, the table reflects a snapshot of the defects that
		were open at the time this report was compiled. For an updated view of open
		defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCun47170

Icon shows wrong for share line testbed

CSCun47290

phone couldn't switch to another line if 2 remote hold call
bubble there

CSCun55006

Phone will send out a number automatically after offhook

CSCun65437

7821/41/61: Transfer/Hold/Conf Buttons Stop Working

CSCuo10914

answer softkey is missing for incoming call

CSCuo10953

only incoming call toast shows on phone LCD, no linekey LED
flashing

CSCuo16987

Cisco 7800 series IP Phones vulnerable to CVE-2014-0160 -aka
Heartbleed

CSCuo17174

7861 phone becomes unresponsive to a softkeys, buttons on the
phone

CSCuo23398

7861 : Memory issue on shared line

## Cisco IP Phone
	 Firmware Support Policy

For information on
		  the support policy for Cisco IP Phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco IP Phone | Protocol | Cisco Unified
				Communications Manager |
|---|---|---|
| Cisco IP
				Phones 7821, 7841, and 7861 | SIP | Cisco Unified Communications Manager Release 8.5(1) or later Cisco Unified
				Communications Manager DST Olsen version D or later |

| Step 1 | Go to the
			 following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco
				IP Phones 7800 Series . |
| Step 3 | Choose your
			 phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 10.1(1)SR2 . |
| Step 6 | Select one of
			 the following firmware files, click the Download or Add to
				cart button, and follow the prompts: cmterm-78xx.10-1-1SR2-1.cop.sgn Note If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. | Note | If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. |
| Note | If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. |
| Step 7 | Click the + next to the firmware file name in the Download
			 Cart section to access additional information about this file. The hyperlink
			 for the readme file is in the Additional Information section, which contains
			 installation instructions for the corresponding firmware. |
| Step 8 | Follow the
			 instructions in the readme file to install the firmware. |

| Note | If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. |
|---|---|

| Step 1 | Go to the
			 following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco
				IP Phones 7800 Series . |
| Step 3 | Choose your
			 phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 10.1(1)SR2 . |
| Step 6 | Download the
			 relevant zip files. |
| Step 7 | Unzip the
			 files. |
| Step 8 | Manually copy
			 the unzipped files to the directory on the TFTP server. See Cisco
				Unified Communications Operating System Administration Guide for
			 information about how to manually copy the firmware files to the server. |

| Note | The latest
			 Locale Installer may not be immediately available; continue to check the
			 website for updates. |
|---|---|

| Step 1 | To access the
			 Cisco Bug Search, go to: https:/​/​tools.cisco.com/​bugsearch |
|---|---|
| Step 2 | Log in with your
			 Cisco.com user ID and password. |
| Step 3 | To look for
			 information about a specific problem, enter the bug ID number in the Search for
			 field, then press Enter . |

| Identifier | Description |
|---|---|
| CSCuh34236 | Display of phone is incorrect when PC port/SW port is 10/10 |
| CSCuj16464 | Monitoring phone not send RTCP |
| CSCuj25165 | Highlighted background has afterimage when switch among calls
on 7861 |
| CSCuj52759 | IPv6 mode phone fail to register if CUCM v4/v6 hostname are
different |
| CSCuj73412 | one log recorded when the call is transferred with translation
pattern |
| CSCuj93181 | Group pickup; the call log should not recorded group number |
| CSCuj96094 | DND beep not played when on hook from handset |
| CSCul01193 | Phone can't add participant by PD in conference/transfer |
| CSCul19068 | It will flash secure icon one time after answer a call |
| CSCul28593 | The line with '#' in the DN still display on phone's ui in srst
mode |
| CSCun07043 | DN displaying wrongly during transfer in 7841 phone Model |
| CSCun30345 | 78xx :line Led behavior wrong if phone has incoming and hold
revert call |
| CSCun35603 | missed call number not increased accordingly |
| CSCun35740 | 78xx can't access VM when setting media using ipv6 prefer. |
| CSCun38492 | Kate overlap the SK |
| CSCun45084 | incoming call toast behavior not consentaneous |
| CSCun45099 | extra cursor on 7861 when dial quick after cancel previous
dialing |
| CSCun45165 | Call is dropped unexpectedly after pressing resume softkey |
| CSCun45175 | local/remote ipv6 addr under stream info error in webpage |
| CSCun45190 | arabic/Hebrew:v6 gateway/v6 dns/tftp v6 address orientation is
wrong |
| CSCun46787 | 7861:UI still display missed calls state if remote call in
hold |
| CSCun47366 | line key flashing too long time for broadcast huntgroup |
| CSCun47509 | call bubble not show for huntgroup number |
| CSCun50485 | 78xx Can not use the default gateway as SRST |
| CSCun51311 | not support the 32-bit SRTCP |
| CSCun60728 | 7800 series phones not formatting special characters for http
get |
| CSCuo17616 | Event Duration for Digit 0 is too short |
| CSCuo62751 | TVS keeps trying when CUCM TVS server do not respond |
| CSCuo64932 | Phone should reject EAP-MD5 auth request |
| CSCuo69837 | Display issue after secure call change to non-secure |
| CSCuo70124 | Error happened after pressing line key during transfer in
SRST |
| CSCuo72188 | Call can't be hold after pressing hold key during conference in
SRST |
| CSCuo75012 | 7861: Call forward info display error after enable Redirected
Number |
| CSCuo80370 | Dpark pfk error after phone fallback from srst |
| CSCuo89757 | 7861 will reset after receiving many simultaneous calls in load
test |
| CSCuo95583 | 78xx Phone doesn't play out of sequence rtp packets |

| Identifier | Headline |
|---|---|
| CSCun47170 | Icon shows wrong for share line testbed |
| CSCun47290 | phone couldn't switch to another line if 2 remote hold call
bubble there |
| CSCun55006 | Phone will send out a number automatically after offhook |
| CSCun65437 | 7821/41/61: Transfer/Hold/Conf Buttons Stop Working |
| CSCuo10914 | answer softkey is missing for incoming call |
| CSCuo10953 | only incoming call toast shows on phone LCD, no linekey LED
flashing |
| CSCuo16987 | Cisco 7800 series IP Phones vulnerable to CVE-2014-0160 -aka
Heartbleed |
| CSCuo17174 | 7861 phone becomes unresponsive to a softkeys, buttons on the
phone |
| CSCuo23398 | 7861 : Memory issue on shared line |