---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-3905-firmware-9-4-1-sr2-releasenotes-ip05-b-3905-release-notes-941sr2-e9384a4ad1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/3905/firmware/9-4-1-SR2/releasenotes/ip05_b_3905-release-notes-941sr2.html
retrieved_at: 2026-08-21T06:25:10.254209+00:00
---

Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1)SR2

# Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1)SR2

### Download Options

Updated: January 12, 2017

First Published: November 30, 2015

Last Updated: January 12, 2017

# Cisco Unified SIP Phone 3905 Release Notes for Firmware Release 9.4(1)SR2

These release notes
		support the Cisco Unified SIP Phone 3905 running Firmware Release 9.4(1)SR2.

The following table
		lists the Cisco Unified Communications Manager release and protocol
		compatibility for the Cisco Unified SIP Phone 3905.

Cisco
					 Unified IP Phone

Protocol

Cisco
					 Unified Communications Manager

Cisco
					 Unified SIP Phone 3905

SIP

Cisco
					 Unified Communications Manager Release 7.1(5) and later.

## Related
	 Documentation

Use the following sections to
		obtain related information.

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

### Features Available
	 with the Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require
		the new firmware and the latest Cisco Unified Communications Manager Device
		Pack.

For information about the Cisco Unified IP Phones and the required Cisco
		Unified Communications Manager device packs, see the following URL:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​voice_ip_comm/​cucm/​compat/​devpack_​comp_​mtx.html

#### Line Text Label

The Line Text Label feature enables the administrator to add a label to a line appearance on the phone. The label displays instead of the directory number, and helps to distinguish the lines when a phone has multiple lines. For example, lines could be labeled with the person's name, the department name, or other information that would help identify the line.

The administrator sets the Line Text Label field in the Device > Phone window of the Cisco Unified Communications Manager.

## Installation

### Install the Firmware Release on the Cisco Unified Communications Manager

Before using the
		  Cisco Unified SIP Phone 3905 Firmware Release 9.4(1)SR2 with Cisco Unified
		  Communications Manager, you must install the latest firmware on all Cisco
		  Unified Communications Manager servers in the cluster.

http:/​/​software.cisco.com/​download/​navigator.html?mdfid=280896546&i=rm

cmterm-3905.9-4-1SR2-2.k3.cop.sgn

If you added
				  the firmware file to the cart, click the Download Cart link when you are ready to download
				  the file.

cmterm-3905-sip-9-4-1SR2-2-readme.html

### Install the Firmware Zip Files

If a Cisco Unified
		  Communications Manager is not available to load the installer program, the
		  following .zip files are available to load the firmware.

cmterm-3905.9-4-1SR2-2.zip

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

Anything that degrades network performance can affect Cisco IP Phone voice and video quality, and in some cases, can cause a call to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative tasks, such as an internal port scan or security scan

Attacks that occur on your network, such as a Denial of Service attack

### On-Hook Transfer Limitation in SIP Phones

When the Cisco Unified Communications Manager Transfer On-Hook Enabled field is enabled, users might report a problem with direct call transfer in SIP phones. If the user transfers the call and immediately goes on hook before they hear the ring signal, the call may drop instead of being transferred.

The user needs to hear the ring signal so that they can be sure that the call is being routed.

### Language Limitation

There is no localized Keyboard
Alpha-Numeric Text Entry (KATE) support for the following Asian
locales:

Chinese (China)

Chinese (Hong Kong)

Chinese (Taiwan)

Japanese (Japan)

Korean (Korea Republic)

The default English (United States) KATE is presented to the user instead.

For example, the phone screen will show text in Korean, but the 2 key on the keypad willdisplay a b c 2 A B C .

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
		  table lists severity 1, 2, and 3 defects that are open for the Cisco Unified SIP Phone 3905
		  for Firmware Release 9.4(1)SR2.

For more
		  information about an individual defect, you can access the online record for
		  the defect using the Bug Toolkit. You
		  must be a registered Cisco.com user to access this online information.

Because defect
		  status continually changes, the table reflects a snapshot of the defects that
		  were open at the time this report was compiled. For an updated view of open
		  defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCug96869

Not request new address after DHCPv6 assigned address
duplicated

CSCuh02720

Take long time to bootup if DHCPv4 server shutdown

CSCuh10981

No DSCP to 802.1Q priority mapping for both IPv4 and IPv6

CSCuh15911

Phone should keep re-provision if version stamp mismatch

CSCuh51331

Phone stuck after IPv6 isic6 attack

CSCuh91119

Phone stuck during Codenomicon HTTP Server/TCP for IPv4 suite
testing

CSCui16740

Attack RTP port during active call, one-way voice occurs

CSCui21409

3905:DUT will restart and change IPv6 address when running
ISIC

CSCui57035

Phone stuck after 10 hours DHCP_option and VLAN_Flapping
stress

CSCuj73157

Not re-request config file if get TFTP "Disk full or allocation
exceed"

CSCun58512

Can't transfer after set CFwdAll and answer call in same pickup
group

### Resolved Caveats

The following
		  table lists severity 1, 2, and 3 defects that are resolved for the Cisco Unified SIP Phone 3905
		  for Firmware Release 9.4(1)SR2.

For more
		  information about an individual defect, you can access the online record for
		  the defect using the Bug Toolkit. You
		  must be a registered Cisco.com user to access this online information.

Because defect
		  status continually changes, the table reflects a snapshot of the defects that
		  were resolved at the time this report was compiled. For an updated view of open
		  defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCur30436

One way voice if 3905 phone hold/trnf to phones whose ip address
has 58

CSCur86828

3905 phone cannot play "attendee ID" prompt when joining webex
meeting

CSCus73041

3905 Genereated DTMF events are not processed by IVR system

CSCus73252

CP-3905 Low volume issue on firmware version 9-4--1

CSCus78772

3905 intermittently sends RTP packets with silence.

CSCus92717

calls through MGCP GW facing 1 way audio using 3905 phones

CSCus95093

CP3905 - Intermittent Choppy or Low audio volume issues

CSCuu79634

3905 phones display FAC code when when fac prompt changed from
default

CSCuv91502

3905 utilizes old subscription to send notify

CSCuw91247

When DUT conference\transfer invalidly, LCD shows incorrect
display.

CSCux04042

3905 Phone not following RFC timer specifications for Active
Subscribes

CSCux05467

3905 phones don't send 'screen=' parameter in
Remote-Party-ID.

## Cisco Unified Communication Manager Public Keys

To improve software integrity protection, new public keys are used to sign cop files for Cisco Unified Communications Manager Release 10.0.1 and later. These cop files have "k3" in their name. To install a k3 cop file on a pre-10.0.1 Cisco Unified Communications Manager, consult the README for the ciscocm.version3-keys.cop.sgn to determine if this additional cop file must first be installed on your specific Cisco Unified Communications Manager version. If these keys are not present and are required, you will see the error "The selected file is not valid" when you try to install the software package.

## Unified
	 Communications Manager Endpoints Locale Installer

By default, Cisco
		  IP Phones are set up for the English (United States) locale. To use the Cisco
		  IP Phones in other locales, you must install the locale-specific version of the
		  Unified Communications Manager Endpoints Locale Installer on every Cisco
		  Unified Communications Manager server in the cluster. The Locale Installer
		  installs the latest translated text for the phone user interface and
		  country-specific phone tones on your system so that they are available for the
		  Cisco IP Phones.

To access the
		  Locale Installer required for a release, access http:/​/​software.cisco.com/​download/​navigator.html?mdfid=286037605&flowid=46245 , navigate to your phone model, and
		  select the Unified Communications Manager Endpoints Locale Installer link.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

The latest
			 Locale Installer may not be immediately available; continue to check the
			 website for updates.

## Cisco IP Phone
	 Firmware Support Policy

For information on
		  the support policy for Cisco IP Phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Cisco IP Phone Documentation Updates on Cisco Unified Communications Manager

The Cisco Unified Communications Manager Self Care Portal (Release 10.0 and later) and User Options web pages (Release 9.1 and earlier) provide  links to the IP Phone user guides in PDF format. These user guides are stored on the Cisco Unified Communications Manager and are up to date when the Cisco Unified Communications Manager release is first made available to customers.

After a Cisco Unified Communications Manager release, subsequent updates to the user guides appear only on the Cisco website. The phone firmware release notes contain the applicable documentation URLs. In the web pages, updated documents display "Updated" beside the document link.

The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer do not update the English user guides on the Cisco Unified Communications Manager.

Administrators and users should check the Cisco website for updated user guides and download the PDF files. Administrators can also make the files available to the users on their company website.

Administrators may want to bookmark the web pages for the phone models that are deployed in their company and send these URLs to their users.

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco
					 Unified IP Phone | Protocol | Cisco
					 Unified Communications Manager |
|---|---|---|
| Cisco
					 Unified SIP Phone 3905 | SIP | Cisco
					 Unified Communications Manager Release 7.1(5) and later. |

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
			 Releases folder, choose 9.4(1)SR2 . |
| Step 6 | Select the
			 following firmware file, click the Download or Add to
				cart button, and follow the prompts: cmterm-3905.9-4-1SR2-2.k3.cop.sgn Note If you added
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
			 installation instructions for the corresponding firmware: cmterm-3905-sip-9-4-1SR2-2-readme.html |
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
				Unified SIP Phone 3900 Series . |
| Step 3 | Choose Cisco Unified SIP Phone 3905 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
			 Releases folder, choose 9.4(1)SR2 . |
| Step 6 | Download the
			 relevant zip files. |
| Step 7 | Unzip the
			 files. |
| Step 8 | Manually copy
			 the unzipped files to the directory on the TFTP server. See Cisco
				Unified Communications Operating System Administration Guide for
			 information about how to manually copy the firmware files to the server. |

| Step 1 | To access Cisco Bug Search, go to: https:/​/​tools.cisco.com/​bugsearch |
|---|---|
| Step 2 | Log in with your
			 Cisco.com user ID and password. |
| Step 3 | To look for
			 information about a specific problem, enter the bug ID number in the Search for
			 field, then press Enter . |

| Identifier | Headline |
|---|---|
| CSCug96869 | Not request new address after DHCPv6 assigned address
duplicated |
| CSCuh02720 | Take long time to bootup if DHCPv4 server shutdown |
| CSCuh10981 | No DSCP to 802.1Q priority mapping for both IPv4 and IPv6 |
| CSCuh15911 | Phone should keep re-provision if version stamp mismatch |
| CSCuh51331 | Phone stuck after IPv6 isic6 attack |
| CSCuh91119 | Phone stuck during Codenomicon HTTP Server/TCP for IPv4 suite
testing |
| CSCui16740 | Attack RTP port during active call, one-way voice occurs |
| CSCui21409 | 3905:DUT will restart and change IPv6 address when running
ISIC |
| CSCui57035 | Phone stuck after 10 hours DHCP_option and VLAN_Flapping
stress |
| CSCuj73157 | Not re-request config file if get TFTP "Disk full or allocation
exceed" |
| CSCun58512 | Can't transfer after set CFwdAll and answer call in same pickup
group |

| Identifier | Headline |
|---|---|
| CSCur30436 | One way voice if 3905 phone hold/trnf to phones whose ip address
has 58 |
| CSCur86828 | 3905 phone cannot play "attendee ID" prompt when joining webex
meeting |
| CSCus73041 | 3905 Genereated DTMF events are not processed by IVR system |
| CSCus73252 | CP-3905 Low volume issue on firmware version 9-4--1 |
| CSCus78772 | 3905 intermittently sends RTP packets with silence. |
| CSCus92717 | calls through MGCP GW facing 1 way audio using 3905 phones |
| CSCus95093 | CP3905 - Intermittent Choppy or Low audio volume issues |
| CSCuu79634 | 3905 phones display FAC code when when fac prompt changed from
default |
| CSCuv91502 | 3905 utilizes old subscription to send notify |
| CSCuw91247 | When DUT conference\transfer invalidly, LCD shows incorrect
display. |
| CSCux04042 | 3905 Phone not following RFC timer specifications for Active
Subscribes |
| CSCux05467 | 3905 phones don't send 'screen=' parameter in
Remote-Party-ID. |

| Note | The latest
			 Locale Installer may not be immediately available; continue to check the
			 website for updates. |
|---|---|

| Note | The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer do not update the English user guides on the Cisco Unified Communications Manager. |
|---|---|

| Tip | Administrators may want to bookmark the web pages for the phone models that are deployed in their company and send these URLs to their users. |
|---|---|