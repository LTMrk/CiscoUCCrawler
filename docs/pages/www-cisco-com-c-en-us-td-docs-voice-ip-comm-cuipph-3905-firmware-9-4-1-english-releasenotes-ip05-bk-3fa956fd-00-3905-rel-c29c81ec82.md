---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-3905-firmware-9-4-1-english-releasenotes-ip05-bk-3fa956fd-00-3905-rel-c29c81ec82
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/3905/firmware/9_4_1/english/releasenotes/IP05_BK_3FA956FD_00_3905-release-notes-9_4_1/IP05_BK_3FA956FD_00_3905-release-notes-9_4_1_chapter_00.html
retrieved_at: 2026-08-21T14:31:03.138910+00:00
---

Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1)

# Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1)

Updated: October 8, 2014

Chapter: Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1)

## Chapter: Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1)

# Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1)

## Introduction

These release notes support the Cisco Unified SIP Phone 3905 running
		Firmware Release 9.4(1).

The following table lists the Cisco Unified Communications Manager
		release and protocol compatibility for the Cisco Unified SIP Phone 3905.

Cisco Unified IP Phone

Protocol

Cisco Unified Communications Manager

Cisco Unified SIP Phone 3905

SIP

Cisco Unified Communications Manager Release 7.1(5) and later

## Related
	 Documentation

### Cisco Unified SIP Phone 3905 Documentation

Refer to publications that are specific to your language, phone model and Cisco Unified
				Communications Manager release. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​collaboration-endpoints/​unified-sip-phone-3900-series/​tsd-products-support-series-home.html

### Cisco Unified
				Communications Manager Documentation

See the Cisco Unified
				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
				Communications Manager release. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-callmanager/​tsd-products-support-series-home.html

### Cisco Business Edition
				3000 Documentation

See the Cisco Business Edition
				3000 Documentation Guide and other publications that are specific to your Cisco Business Edition
				3000 release. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​business-edition-3000/​tsd-products-support-series-home.html

### Cisco Business Edition
				5000 Documentation

See the Cisco Business Edition
				5000 Documentation Guide and other publications that are specific to your Cisco Business Edition
				5000 release. Navigate from the following URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​business-edition-5000/​tsd-products-support-series-home.html

## New and Changed Features

The following sections describe the features that are new or have changed in this release.

Failure to install the Device Package before the phone firmware upgrade may render the phones unusable.

- Features Available
	 with Firmware Release

- Features Available
	 with Latest Cisco Unified Communications Manager Device Pack

### Features Available
	 with Firmware Release

The following sections describe the features available with the Firmware
		Release.

#### IPv6 Ready Logo (SIP)

The IPv6 Ready Logo (SIP) feature ensures that IP addressing on Cisco SIP Phones passes component level conformance and interoperability testing as identified in the TAHI Project.

The feature is supported on the following phones:

Cisco Unified SIP Phone 3905

#### IPv6
	 Support

The IPv6 Support
		feature provides support for expanded IP addressing on Cisco IP Phones. The
		phones support IPv6 support in stand-alone or dual-stack modes. In dual-stack
		mode, phones can communicate using IPv4 and IPv6 simultaneously.

The default
		configuration is dual-stack mode.

The feature is
		controlled using the IP Addressing Mode and the IP Addressing Mode Preference
		for Signalling parameters in the Common Phone Profile: Device > Device
			 Settings > Common Phone Profile of the Cisco
		Unified Communications Manager Administration window.

The IP Addressing
		Mode and the IP Addressing Mode Preference for Signaling parameters have the
		following options:

IPv4 Only

IPv6 Only

IPv4 and IPv6
			 (default)

This feature has no
		user impact.

The feature is
		supported on the following phone:

Cisco Unified
			 SIP Phone 3905

##### Where to Find
		  More Information

Cisco Unified SIP Phone
			 3905 Administration Guide for Cisco Unified Communications Manager 10.0
			 (SIP)

#### Multiple Date Display Formats

The Multiple Date Display Formats feature provides the ability for the phone to display one of three date formats controlled by the CUCM. The supported date formats include:

Day, Month, Year (DD/MM/YYYY)

Month, Day, Year (MM/DD/YYYY)

Year, Month, Day (YYYY/MM/DD)

The feature is supported on the following phones:

Cisco Unified SIP Phone 3905

##### Where to Find More Information

Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0 (SIP)

#### Native Paging for
	 Cisco Unified Communications Manager Express

The Native Paging
		for Cisco Unified Communications Manager Express feature provides users with
		the ability to create a one-way voice path to a designated group of phones. The
		receiving phones hear the message, but cannot respond to the call.

The feature is
		supported for IP multicast and unicast, in IPv4 address mode only.

The administrator
		assigns a specific paging number to a designated group of phones.

The feature is
		supported on the following phone:

Cisco Unified
			 SIP Phone 3905

For more information, see the Cisco Unified Communications Manager
		Express documentation.

### Features Available
	 with Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require
		the new firmware and the latest Cisco Unified Communications Manager Device
		Pack.

For information about the Cisco Unified IP Phones and the required Cisco
		Unified Communications Manager device packs, see the following URL:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​compat/​devpack_​comp_​mtx.html

- Paging Support on
	 Cisco Unified Communications Manager

- SIP MD5 Digest Authentication

#### Paging Support on
	 Cisco Unified Communications Manager

The Paging Support
		on Cisco Unified Communications Manager feature provides users with the ability
		to create a one-way voice path to a designated group of phones using Singlewire
		InformaCast software.

The paging phone
		must be configured to support HTTP authentication and RTP multicast.

The administrator
		enables paging support by selecting basic HTTP authentication for the Cisco
		Unified Communications Manager.

The feature is
		supported on the following phones:

Cisco Unified IP
			 SIP Phone 3905

##### Where to Find
		  More Information

Cisco Unified SIP Phone
				  3905 Administration Guide for Cisco Unified Communications Manager 10.0
				  (SIP)

Cisco Unified SIP Phone
				  3905 User Guide for Cisco Unified Communications Manager 10.0 (SIP)

#### SIP MD5 Digest Authentication

The SIP MD5 Digest Authentication feature allows administrators to enable or disable MD5 digest authentication for SIP.

MD5 is used for security.

The feature is supported on the following phone:

Cisco Unified IP Phone 3905

##### Where to Find More Information

Cisco Unified SIP Phone 3905 Administration Guide for Cisco Unified Communications Manager 10.0 (SIP)

## Installation

- Install Firmware
	 Release on Cisco Unified Communications Manager

- Install Firmware
	 Zip Files

### Install Firmware
	 Release on Cisco Unified Communications Manager

Before using the
		  Cisco Unified SIP Phone 3905 Firmware Release 9.4(1) with Cisco Unified
		  Communications Manager, you must install the latest firmware on all Cisco
		  Unified Communications Manager servers in the cluster.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=280896546&i=rm

cmterm-3905.9-4-1-0.cop.sgn

If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file.

cmterm-3905-sip-9-4-1-0-readme.html

### Install Firmware
	 Zip Files

If a Cisco Unified
		  Communications Manager is not available to load the installer program, the
		  following .zip file are available to load the firmware.

cmterm-3905.9-4-1-0.zip

Firmware upgrades
		  over the WLAN interface may take longer than upgrades using a wired connection.
		  Upgrade times over the WLAN interface may take more than an hour, depending on
		  the quality and bandwidth of the wireless connection.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=280896546&i=rm

## Limitations and Restrictions

### Call Admission
	 Control with Cisco Unified Communications Manager

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

This section
		  describes the resolved and open caveats, and provides information on accessing
		  the Cisco Software Bug Toolkit.

- Access Cisco Bug
	 Search

- Open
	 Caveats

- Resolved
	 Caveats

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

### Open
	 Caveats

The following
		  table lists severity 1, 2, and 3 defects that are open for the Cisco Unified IP
		  Phones for Firmware Release 9.4(1).

For more
		  information about an individual defect, you can access the online record for
		  the defect by clicking the Identifier or going to the URL that is shown. You
		  must be a registered Cisco.com user to access this online information.

Because defect
		  status continually changes, the table reflects a snapshot of the defects that
		  were open at the time this report was compiled. For an updated view of open
		  defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCug96869

Not
					 request new address after DHCPv6 assigned address duplicated

CSCuh02720

Take long
					 time to bootup if DHCPv4 server shutdown

CSCuh10981

No DSCP
					 to 802.1Q priority mapping for both IPv4 and IPv6

CSCuh15911

Phone
					 should keep re-provision if version stamp mismatch

CSCuh51331

Phone
					 stuck after IPv6 isic6 attack

CSCuh91119

Phone
					 stuck during Codenomicon HTTP Server/TCP for IPv4 suite testing

CSCui16740

Attack RTP port during active call, one-way voice occurs

CSCui21409

3905:DUT will restart and change IPv6 address when running ISIC

CSCui57035

Phone stuck after 10 hours DHCP_option and VLAN_Flapping stress

CSCuj73157

Not re-request config file if get TFTP "Disk full or
					 allocation exceed"

### Resolved
	 Caveats

The following
		  table lists severity 1, 2, and 3 defects that are resolved for the Cisco
		  Unified IP Phones for Firmware Release 9.4(1).

For more
		  information about an individual defect, you can access the online record for
		  the defect by clicking the Identifier or going to the URL that is shown. You
		  must be a registered Cisco.com user to access this online information.

Because defect
		  status continually changes, the table reflects a snapshot of the defects that
		  were resolved at the time this report was compiled. For an updated view of
		  resolved defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCtw59242

Calls
					 established with no audio on IP Phones 3905

CSCty26479

Phone
					 unable to dial variable length route patterns with FAC enabled.

CSCty55380

3905 IP
					 Phones always display GMT Time

CSCtz96290

3905
					 CME: Phone can’t work with VM server by enable DTMF
					 integration

CSCtz96937

Brazilian cptone not working on a 3905 phone

CSCub09465

CP-3905
					 fails to configure voice VLAN via LLDP-MED.

CSCuc17539

3905
					 Phone - No audio

CSCuc90106

Call
					 xfer on 3905 phone doesn't work after removing CfwdAll settings

CSCud02155

DSP
					 module timing issue and corrupt data make 3905 hang in call

CSCud13126

3905
					 Phones using more power than it's class allows during speakerphone

CSCud31483

error
					 in G.729 codec handling make no audio

CSCuf03705

3905
					 phone won't stay registered to third-party switch

CSCug20931

BE3K:
					 3905 - Unable to dial from Placed Calls (Call History)

CSCug30895

Date
					 & Time Format enhancement for IST in 3905 SIP phones

CSCug54295

3905
					 phone ignores timeout for variable length SIP Dial Rule pattern

CSCug59461

39xx phon
					 model won't restrict read access to the netw setting

CSCug61605

3905
					 plays incorrect ringbacktone when NETWORK LOCALE is set to AU or UK

CSCug88894

3905 IP
					 phone shows "rejected" on CUCM if we delete and add it back

CSCuh58560

3905
					 cannot stop ringback when Display field contains the letters "tag"

CSCuh75574

3905
					 allows Telnet access to port 7870 exposing access to Busy Box shell

CSCuh79852

Not send
					 KPML via Notify message in some scenario

CSCui73186

3905 get
					 stuck using hold in call preservation

CSCui84692

3905 hear
					 busy tone when cancel transfer

CSCuj04191

3905
					 Phone sip module,SRST, re- registration thread and failover thread

## Cisco IP Phone
	 Firmware Support Policy

For information on
		  the support policy for Cisco IP Phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco Unified IP Phone | Protocol | Cisco Unified Communications Manager |
|---|---|---|
| Cisco Unified SIP Phone 3905 | SIP | Cisco Unified Communications Manager Release 7.1(5) and later |

| Note | Failure to install the Device Package before the phone firmware upgrade may render the phones unusable. |
|---|---|

| Step 1 | Go to the
			 following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=280896546&i=rm |
|---|---|
| Step 2 | Choose Cisco
				Unified SIP Phone 3900 Series . |
| Step 3 | Choose Cisco Unified SIP Phone 3905 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 9.4(1) . |
| Step 6 | Select the
			 following firmware file, click the Download or Add to
				cart button, and follow the prompts: cmterm-3905.9-4-1-0.cop.sgn Note If you added
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
			 installation instructions for the corresponding firmware: cmterm-3905-sip-9-4-1-0-readme.html |
| Step 8 | Follow the
			 instructions in the readme file to install the firmware. |

| Note | If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file. |
|---|---|

| Step 1 | Go to the
			 following URL: http:/​/​software.cisco.com/​download/​navigator.html?mdfid=280896546&i=rm |
|---|---|
| Step 2 | Choose Cisco
				Unified SIP Phone 3900 Series . |
| Step 3 | Choose Cisco Unified SIP Phone 3905 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 9.4(1) . |
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

| Identifier | Headline |
|---|---|
| CSCug96869 | Not
					 request new address after DHCPv6 assigned address duplicated |
| CSCuh02720 | Take long
					 time to bootup if DHCPv4 server shutdown |
| CSCuh10981 | No DSCP
					 to 802.1Q priority mapping for both IPv4 and IPv6 |
| CSCuh15911 | Phone
					 should keep re-provision if version stamp mismatch |
| CSCuh51331 | Phone
					 stuck after IPv6 isic6 attack |
| CSCuh91119 | Phone
					 stuck during Codenomicon HTTP Server/TCP for IPv4 suite testing |
| CSCui16740 | Attack RTP port during active call, one-way voice occurs |
| CSCui21409 | 3905:DUT will restart and change IPv6 address when running ISIC |
| CSCui57035 | Phone stuck after 10 hours DHCP_option and VLAN_Flapping stress |
| CSCuj73157 | Not re-request config file if get TFTP "Disk full or
					 allocation exceed" |

| Identifier | Headline |
|---|---|
| CSCtw59242 | Calls
					 established with no audio on IP Phones 3905 |
| CSCty26479 | Phone
					 unable to dial variable length route patterns with FAC enabled. |
| CSCty55380 | 3905 IP
					 Phones always display GMT Time |
| CSCtz96290 | 3905
					 CME: Phone can’t work with VM server by enable DTMF
					 integration |
| CSCtz96937 | Brazilian cptone not working on a 3905 phone |
| CSCub09465 | CP-3905
					 fails to configure voice VLAN via LLDP-MED. |
| CSCuc17539 | 3905
					 Phone - No audio |
| CSCuc90106 | Call
					 xfer on 3905 phone doesn't work after removing CfwdAll settings |
| CSCud02155 | DSP
					 module timing issue and corrupt data make 3905 hang in call |
| CSCud13126 | 3905
					 Phones using more power than it's class allows during speakerphone |
| CSCud31483 | error
					 in G.729 codec handling make no audio |
| CSCuf03705 | 3905
					 phone won't stay registered to third-party switch |
| CSCug20931 | BE3K:
					 3905 - Unable to dial from Placed Calls (Call History) |
| CSCug30895 | Date
					 & Time Format enhancement for IST in 3905 SIP phones |
| CSCug54295 | 3905
					 phone ignores timeout for variable length SIP Dial Rule pattern |
| CSCug59461 | 39xx phon
					 model won't restrict read access to the netw setting |
| CSCug61605 | 3905
					 plays incorrect ringbacktone when NETWORK LOCALE is set to AU or UK |
| CSCug88894 | 3905 IP
					 phone shows "rejected" on CUCM if we delete and add it back |
| CSCuh58560 | 3905
					 cannot stop ringback when Display field contains the letters "tag" |
| CSCuh75574 | 3905
					 allows Telnet access to port 7870 exposing access to Busy Box shell |
| CSCuh79852 | Not send
					 KPML via Notify message in some scenario |
| CSCui73186 | 3905 get
					 stuck using hold in call preservation |
| CSCui84692 | 3905 hear
					 busy tone when cancel transfer |
| CSCuj04191 | 3905
					 Phone sip module,SRST, re- registration thread and failover thread |