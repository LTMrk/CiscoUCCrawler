---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-6900-series-firmware-931-6900-931-6900-931-chapter-00-html-15de2e3ece
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/6900_series/firmware/931/6900_931/6900_931_chapter_00.html
retrieved_at: 2026-08-21T14:23:24.515779+00:00
---

Cisco Unified IP Phone 6900 Series Release Notes for Firmware Release 9.3(1)

# Cisco Unified IP Phone 6900 Series Release Notes for Firmware Release 9.3(1)

Updated: March 27, 2015

Chapter: Cisco Unified IP Phone 6900 Series Release Notes for Firmware Release 9.3(1)

## Chapter: Cisco Unified IP Phone 6900 Series Release Notes for Firmware Release 9.3(1)

# Cisco Unified IP Phone 6900 Series Release Notes for Firmware Release 9.3(1)

These release notes provide the following information. You might need to notify your users about some of the information provided in this document.

Before deploying the 9.3(1) firmware, the Cisco Unified Communications Manager must be updated to the latest device pack.

## Related
	 Documentation

### Cisco Unified IP Phone 6900 Series Documentation

Refer to publications that are specific to your language, phone model and Cisco Unified
				Communications Manager release. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​collaboration-endpoints/​unified-ip-phone-6900-series/​tsd-products-support-series-home.html

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

### Cisco Unified
				Communications Manager Express Documentation

See the publications that are specific to your language, phone model and Cisco Unified
				Communications Manager Express release. Navigate from the following documentation URL:

http:/​/​www.cisco.com/​c/​en/​us/​support/​unified-communications/​unified-communications-manager-express/​tsd-products-support-series-home.html

## New and Changed Features

The following sections describe the features that are new or have changed in this release.

Failure to install the Device Package before the phone firmware upgrade may render the phones unusable.

### Device Invoked Recording

The Device Invoked Recording feature enables users to control the recording of phone calls using the Record button on the phone.

Users see a status indicator on the phone display, showing when a conversation is being recorded.

The Device Invoked Recording feature is supported on the following phones (SCCP and SIP):

Cisco Unified IP Phone 6921

Cisco Unified IP Phone 6941

Cisco Unified IP Phone 6945

Cisco Unified IP Phone 6961

#### Where to Find More Information

Cisco Unified IP Phone 6921, 6941, 6945, and 6961 Administration Guide for Cisco Unified Communications Manager  9.0 (SCCP and SIP)

Cisco Unified IP Phone 6921, 6941, 6945, and 6961 User Guide for Cisco Unified Communications Manager  9.0 (SCCP and SIP)

### Extension Mobility Cross Cluster Enhancement

The Extension Mobility Cross Cluster (EMCC) Enhancement feature preserves the network and security configurations on the phone. By so doing, security policies are maintained, network bandwidth is preserved and network failure is avoided within the visiting cluster (VC).

The feature is supported on the following SCCP and SIP phones:

Cisco Unified IP Phone 6921

Cisco Unified IP Phone 6941

Cisco Unified IP Phone 6945

Cisco Unified IP Phone 6961

#### Where to Find More Information

Cisco Unified IP Phone 6921, 6941, 6945, and 6961 Administration Guide for Cisco Unified Communications Manager 9.0 (SCCP and SIP)

### Headset Sidetone Control

Headset Sidetone Control lets the user adjust the headset tone levels and can be accessed in the Preferences menu. The users can adjust headset levels to one of the four following settings:

High

Normal

Low

Off

This feature only applies to wired headsets and does not apply to Bluetooth or wireless headsets.

There is no configuration requirement.

This feature is supported on the following Cisco Unified IP Phones (SCCP and SIP):

Cisco Unified IP Phone 6921

Cisco Unified IP Phone 6941

Cisco Unified IP Phone 6945

Cisco Unified IP Phone 6961

#### Where to Find More Information

Cisco Unified IP Phone 6921, 6941, 6945, and 6961 User Guide for Cisco Unified Communications Manager 9.0 (SCCP and SIP)

### Line Status for Call Lists

The Line Status for Call Lists feature enables the user to see the availability status of monitored line numbers in the Call History list. The administrator enables or disables this feature using the Line Status for Call Lists parameter in the Enterprise Parameters Configuration window.

When the Line Status for Call Lists parameter is Enabled, the phone line numbers in the Call History register Line Status notifications and an icon appears next to each Call History item in the Call History list. The icon notifies the user that the lines are in one of the following states:

Idle

Busy

DND

When the Line Status for Call Lists parameter is Disabled, the phone line numbers in the Call History list do not register the Line Status notifications.

This feature is supported on the following Cisco Unified IP Phones (SCCP and SIP):

Cisco Unified IP Phone 6921

Cisco Unified IP Phone 6941

Cisco Unified IP Phone 6945

Cisco Unified IP Phone 6961

#### Where to Find More Information

Cisco Unified IP Phone 6921, 6941, 6945, and 6961 Administration Guide for Cisco Unified Communications Manager 9.0 (SCCP and SIP)

Cisco Unified IP Phone 6921, 6941, 6945, and 6961 User Guide for Cisco Unified Communications Manager 9.0 (SCCP and SIP)

### PLK Support for Queue Statistics

The PLK Support for Queue Statistics enables the users to query the call queue statistics for hunt pilots and the information appears on phone screen.

The programmable line button Queue Status can be configured by the administrator. When the user presses Queue Status, the phone displays the Queue Status screen. The Queue Status screen includes hunt pilot directory number, number of callers in queue, and the longest call waiting time in queue.

The statistics information is not updated automatically. The user must press the Update button to view updated statistics. To exit from the queue display screen, the user presses the Exit button.

This feature is supported on the following Cisco Unified IP Phones (SCCP and SIP):

Cisco Unified IP Phone 6921

Cisco Unified IP Phone 6941

Cisco Unified IP Phone 6945

Cisco Unified IP Phone 6961

#### Where to Find More Information

Cisco Unified IP Phone 6921, 6941, 6945, and 6961 Administration Guide for Cisco Unified Communications Manager (SCCP and SIP)

Cisco Unified IP Phone 6921, 6941, 6945, and 6961 User Guide for Cisco Unified Communications Manager (SCCP and SIP)

### Ring Cadence Localization

The Ring Cadence Localization feature allows IP Phones to use either a North American ring cadence or a Japanese ring cadence. In the Cisco Unified Communications Manager Administration, the administrator sets the Ring Locale field to be either Default or Japan from the Common Profile and phone-specific profile windows.

When Ring Locale is set to Japan, the user does not see the Ringtone entry in the Preferences menu.

The Cisco Unified IP Phone 6901 and 6911 do not have a Preferences menu.

The feature is supported on the following SCCP and SIP phones:

Cisco Unified IP Phone 6901

Cisco Unified IP Phone 6911

Cisco Unified IP Phone 6921

Cisco Unified IP Phone 6941

Cisco Unified IP Phone 6945

Cisco Unified IP Phone 6961

#### Where to Find More Information

Cisco Unified IP Phone 6901 and 6911 Administration Guide for Cisco Unified Communications Manager  9.0 (SCCP and SIP)

Cisco Unified IP Phone 6901 and 6911 User Guide for Cisco Unified Communications Manager 9.0 (SCCP and SIP)

Cisco Unified IP Phone 6921, 6941, 6945, and 6961 Administration Guide for Cisco Unified Communications Manager 9.0 (SCCP and SIP)

Cisco Unified IP Phone 6921, 6941, 6945, and 6961 User Guide for Cisco Unified Communications Manager 9.0 (SCCP and SIP)

### RTCP Behavior On Hold

The RTCP Hold For SIP feature ensures that held calls are not dropped by the gateway. The gateway checks the status of the RTCP port to determine if a call is active or not. By keeping the phone port open, the gateway will not end held calls.

This feature has no administration or user impacts.

The feature is supported on the following SIP phones:

Cisco Unified IP Phone 6901

Cisco Unified IP Phone 6911

Cisco Unified IP Phone 6921

Cisco Unified IP Phone 6941

Cisco Unified IP Phone 6945

Cisco Unified IP Phone 6961

### View Call Logs From Shared Line

The Call History for Shared Line feature offers enhanced viewing of shared line activity in the Cisco Unified IP Phone call history. In addition to logging missed calls for a shared line, this feature will log all answered and placed calls on a shared line.

Cisco Unified IP Phone 6921

Cisco Unified IP Phone 6941

Cisco Unified IP Phone 6945

Cisco Unified IP Phone 6961

#### Where to Find More Information

Cisco Unified IP Phones 6921, 6941, 6945, and 6961 Administration Guide for Cisco Unified Communications Manager 9.0 (SCCP and SIP)

Cisco Unified IP Phones 6921, 6941, 6945, and 6961 User Guide for Cisco Unified Communications Manager Guide 9.0 (SCCP and SIP)

## Installation

### Upgrade Notes

Direct upgrades, using signed load files, are supported to firmware releases 9.3(1) from 9.x. You can use the following firmware release file for these direct upgrades.

For Cisco Unified IP Phone 6901 and 6911:

cmterm-6901_6911-sccp.9-3-1-2.cop.sgn

cmterm-6901_6911-sip.9-3-1-2.cop.sgn

For Cisco Unified IP Phone 6921, 6941, and 6961

cmterm-69xx-sccp.9-3-1-3.cop.sgn

cmterm-69xx-sip.9-3-1-5.cop.sgn

For Cisco Unified IP Phone 6945

cmterm-6945-sccp.9-3-1-3.cop.sgn

cmterm-6945-sip.9-3-1-5.cop.sgn

Note for Cisco Unified IP Phone 6901, 6911, and 6945:

Direct upgrade to firmware release SCCP or SIP 9.3(1) is supported.

Notes for Cisco Unified IP Phone 6921, 6941, and 6961:

Converting SIP to previous 9.1(1) SCCP does not work due to a known issue CSCtj89983 . The workaround is to perform factory reset after upgrade completes.

Converting previous 9.1(1) SCCP to SIP does not support Autoregistration due to a known issue CSCth26499 .

Direct upgrade from firmware release 9.0(x) to 9.3(1) is supported. After you upgrade from an earlier firmware release to 9.3(1) and for subsequent firmware releases, you can upgrade or downgrade only to signed firmware releases.

If you are using unsigned load and want to upgrade Cisco Unified Communication Manager to release 8.6 and later then manually install unsigned load to upgrade because phone load upgrade will fail due to signed load in Cisco Unified Communication Manager by default.

### Install Latest Cisco Unified
				Communications Manager Release

Before using the Cisco Unified IP Phone with Cisco Unified
				Communications Manager , your Cisco Unified
				Communications Manager servers must be running a version of the
server software that supports the phones. All Cisco Unified
				Communications Manager servers in the cluster must support the
phones. For information about the minimum Cisco Unified
				Communications Manager software version that the phone requires,
see the introductory sections of these release notes.

For more information on Cisco Unified
				Communications Manager installations and upgrades, see the
documents for your Cisco Unified
				Communications Manager version at
the following location: http:/​/​www.cisco.com/​en/​US/​products/​sw/​voicesw/​ps556/​prod_​installation_​guides_​list.html

To download and install the Cisco Unified
				Communications Manager version, perform these steps.

http:/​/​www.cisco.com/​cisco/​software/​navigator.html?mdfid=268439621&catid=278875240

### Install Latest Cisco Unified
				Communications Manager Express Firmware

To download and install the Cisco Unified
				Communications Manager Express firmware, follow these steps:

http:/​/​www.cisco.com/​cisco/​software/​type.html?mdfid=277641082&flowid=5337

### Install Firmware Release on Cisco Unified Communications Manager

Before using the Cisco Unified IP Phone Firmware Release 9.3(1) with Cisco Unified Communications Manager, you must install the latest firmware on all Cisco Unified Communications Manager servers in the cluster.

Skinny Client Control Protocol (SCCP) Software

Session Initiation Protocol (SIP) Software

The files for the Cisco Unified IP Phone 6900 Series are:

For Cisco Unified IP Phone 6901 and 6911

cmterm-6901_6911-sccp.9-3-1-2.cop.sgn

cmterm-6901_6911-sip.9-3-1-2.cop.sgn

For Cisco Unified IP Phone 6921, 6941, and 6961

cmterm-69xx-sccp.9-3-1-3.cop.sgn

cmterm-69xx-sip.9-3-1-5.cop.sgn

For Cisco Unified IP Phone 6945

cmterm-6945-sccp.9-3-1-3.cop.sgn

cmterm-6945-sip.9-3-1-5.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

cmterm-6901_6911-sccp.9-3-1-2-readme.html

cmterm-6901_6911-sip.9-3-1-2-readme.html

cmterm-6921_6941_6961-sccp.9-3-1-3-readme.html

cmterm-6921_6941_6961-sip.9-3-1-5-readme.html

cmterm-6945-sccp.9-3-1-3-readme.html

cmterm-6945-sip.9-3-1-5-readme.html

### Install Firmware Zip Files

If a Cisco Unified Communications Manager is not available to load the installer program, the following .zip files are available to load the firmware.

SCCP

cmterm-6901_6911-sccp.9-3-1-2.zip

cmterm-69xx-sccp.9-3-1-3.zip

cmterm-6945-sccp.9-3-1-3.zip

SIP

cmterm-6901_6911-sip.9-3-1-2.zip

cmterm-69xx-sip.9-3-1-5.zip

cmterm-6945-sip.9-3-1-5.zip

Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN interface may take more than an hour, depending on the quality and bandwidth of the wireless connection.

Skinny Client Control Protocol (SCCP) Software

Session Initiation Protocol (SIP) Software

## Important Notes

This section provides important information about Cisco Unified IP Phone 6900 Series feature functionality.

- DTMF During On-Hook Dialing

- Phone Limitation During SVI Change

- Phone Behavior During Times of Network Congestion

### DTMF During On-Hook Dialing

On-hook dialing can result in users hearing the DTMF from the key press in the handset. The tones are heard if the handset is picked up while the last digit is pressed. If users pick up the handset after pressing the last digit, they will normally not hear any DTMF.

### Phone Limitation During SVI Change

Cisco IP Phones use a Switch Virtual Interface (SVI) to manage VLANs. If the SVI changes and the phones require new IP addresses, some phones require a reboot so that the new IP address is used. The following phones must be rebooted in this condition:

Cisco Unified IP Phone 6901

Cisco Unified IP Phone 6911

Cisco Unified IP Phone 6921

Cisco Unified IP Phone 6941

Cisco Unified IP Phone 6945

Cisco Unified IP Phone 6961

Cisco Unified IP Phone 8941

Cisco Unified IP Phone 8945

Cisco Unified IP Phone 8961

Cisco Unified IP Phone 9951

Cisco Unified IP Phone 9971

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

- Open Caveats

- Resolved Caveats

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

The following table lists severity 1, 2, and 3 defects that are open for the Cisco Unified IP Phones 6900 Series for Firmware Release 9.3(1).

For more information about an individual defect, you can access the online record for the defect by clicking the Identifier or going to the URL that is shown. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

Cisco Unified IP Phone 6901 and 6911

CSCtz55425

6901/6911 phones can't register using Voice VLAN learnt through LLDP

Cisco Unified IP Phone 6921, 6941, and 6961

CSCtu09371

When Speaker is enabled, low audio observed when both the parties speak

CSCua07297

IP Phone 6921 shows restricted CGPN for forwarded calls

Cisco Unified IP Phone 6945

CSCtz38370

694x Web Access should be disabled by default

### Resolved Caveats

The following table lists severity 1, 2, and 3 defects that are resolved for the Cisco Unified IP Phones 6900 Series for Firmware Release 9.3(1).

For more information about an individual defect, you can access the online record for the defect by clicking the Identifier or going to the URL that is shown. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were resolved at the time this report was compiled. For an updated view of resolved defects, access Bug Toolkit as described in Access Cisco Bug Search .

Cisco Unified IP Phone 6901 and 6911

CSCtz54879

6911 Poor audio quality

Cisco Unified IP Phone 6921, 6941, and 6961

CSCtx84110

6941 phone is not sending http request to CME

CSCtr97656

Default ringtones for 6961 phones not working in version
9-2-1-0

CSCty09722

69xx answers calls differently after firmware upgrade

CSCty24748

Hold/Forward button has no effect while Call Ended popup is
visible

CSCty30749

69xx pop-up toast doesn't disappear while dialing transfer /
conference

CSCty32459

69XX reverse numeric digits with Arabic locale

CSCty44892

69xx 1 Missed call: XXXX not displayed when LINE-12 receives a
call

CSCty51278

6921/41/61:PO Locale: Personal Directory, Corporate Directory in
English

CSCty78955

69xx Unable to stop blinking LINE LED after receiving calls

CSCty78977

6961 freeze when receiving multiple calls simultaneously

CSCty84518

GPickup : 6961 switch from call A to Call B after going in
handset mode

CSCty88764

Corporate Directory issue on 69XX phones

CSCty90462

'Call Transfer Successful' appear on shareline if Transfer
Onhook enable

CSCtz66394

Screenshot on 6900 series phone without authentication

CSCty29289

69xx phones freeze due to get_clog_ext_hdr malloc failed

Cisco Unified IP Phone 6945

CSCty16495

6945 On-Hook Personal Address Book Dialing Fails Across WAN

CSCty77368

Hunt Group Logout LED button turns off after restart on 69xx sip
phones

CSCtx76044

6945 phone can not handle "()" in corporate directory

CSCty11107

69xx phones don't respect hierarchical authentication

CSCty46888

"Corporate Directory" always show up even it is not enabled on
cucm.

CSCty85247

6945 phones sends voice packets untagged after reboot if PC vlan
is 1

CSCtz15149

69XX phones should not set Do Not Fragment bit

CSCty29289

69xx phones freeze due to get_clog_ext_hdr malloc failed

## Cisco IP Phone
	 Firmware Support Policy

For information on
		  the support policy for Cisco IP Phones, see http:/​/​www.cisco.com/​c/​en/​us/​support/​docs/​collaboration-endpoints/​unified-ip-phone-7900-series/​116684-technote-ipphone-00.html .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http:/​/​www.cisco.com/​c/​en/​us/​td/​docs/​general/​whatsnew/​whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application. The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Note | Before deploying the 9.3(1) firmware, the Cisco Unified Communications Manager must be updated to the latest device pack. |
|---|---|

| Note | Failure to install the Device Package before the phone firmware upgrade may render the phones unusable. |
|---|---|

| Step 1 | Go to the following URL: http:/​/​www.cisco.com/​cisco/​software/​navigator.html?mdfid=268439621&catid=278875240 |
|---|---|
| Step 2 | Choose your Cisco Unified
				Communications Manager version. |
| Step 3 | Choose the appropriate software type. |
| Step 4 | Hover over the desired file. When the popup window displays, click the Readme link to open the readme file. |
| Step 5 | Choose Download or Add to cart for the desired file. |
| Step 6 | Use the instructions in the readme file to install the updated file on the Cisco Unified
				Communications Manager . |

| Step 1 | Go to the following URL: http:/​/​www.cisco.com/​cisco/​software/​type.html?mdfid=277641082&flowid=5337 |
|---|---|
| Step 2 | Choose your Cisco Unified
				Communications Manager Express version from the Select a File to Download section. |

| Step 1 | Go to the following URL: http:/​/​www.cisco.com/​cisco/​software/​navigator.html?mdfid=282677102&i=rm |
|---|---|
| Step 2 | Choose your phone model. |
| Step 3 | Choose one of the following firmware types: Skinny Client Control Protocol (SCCP) Software Session Initiation Protocol (SIP) Software |
| Step 4 | In the Latest Releases folder, choose 9.3(1) . |
| Step 5 | Select one of the following firmware files, click the Download Now or Add to cart button, and follow the prompts: The files for the Cisco Unified IP Phone 6900 Series are: For Cisco Unified IP Phone 6901 and 6911 cmterm-6901_6911-sccp.9-3-1-2.cop.sgn cmterm-6901_6911-sip.9-3-1-2.cop.sgn For Cisco Unified IP Phone 6921, 6941, and 6961 cmterm-69xx-sccp.9-3-1-3.cop.sgn cmterm-69xx-sip.9-3-1-5.cop.sgn For Cisco Unified IP Phone 6945 cmterm-6945-sccp.9-3-1-3.cop.sgn cmterm-6945-sip.9-3-1-5.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 6 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink for the readme file is in the Additional Information section, which contains installation instructions for the corresponding firmware: cmterm-6901_6911-sccp.9-3-1-2-readme.html cmterm-6901_6911-sip.9-3-1-2-readme.html cmterm-6921_6941_6961-sccp.9-3-1-3-readme.html cmterm-6921_6941_6961-sip.9-3-1-5-readme.html cmterm-6945-sccp.9-3-1-3-readme.html cmterm-6945-sip.9-3-1-5-readme.html |
| Step 7 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Note | Firmware upgrades over the WLAN interface may take longer than upgrades using a wired connection. Upgrade times over the WLAN interface may take more than an hour, depending on the quality and bandwidth of the wireless connection. |
|---|---|

| Step 1 | Go to the following URL: http:/​/​www.cisco.com/​cisco/​software/​navigator.html?mdfid=282677102&i=rm |
|---|---|
| Step 2 | Choose your phone model. |
| Step 3 | Choose one of the following firmware types: Skinny Client Control Protocol (SCCP) Software Session Initiation Protocol (SIP) Software |
| Step 4 | In the Latest Releases folder, choose 9.3(1) . |
| Step 5 | Download the relevant zip files. |
| Step 6 | Unzip the files. |
| Step 7 | Manually copy the unzipped files to the directory on the TFTP server. See Cisco Unified Communications Operating System Administration Guide for information about how to manually copy the firmware files to the server. |

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
| Cisco Unified IP Phone 6901 and 6911 |
| CSCtz55425 | 6901/6911 phones can't register using Voice VLAN learnt through LLDP |
| Cisco Unified IP Phone 6921, 6941, and 6961 |
| CSCtu09371 | When Speaker is enabled, low audio observed when both the parties speak |
| CSCua07297 | IP Phone 6921 shows restricted CGPN for forwarded calls |
| Cisco Unified IP Phone 6945 |
| CSCtz38370 | 694x Web Access should be disabled by default |

| Identifier | Headline |
|---|---|
| Cisco Unified IP Phone 6901 and 6911 |
| CSCtz54879 | 6911 Poor audio quality |
| Cisco Unified IP Phone 6921, 6941, and 6961 |
| CSCtx84110 | 6941 phone is not sending http request to CME |
| CSCtr97656 | Default ringtones for 6961 phones not working in version
9-2-1-0 |
| CSCty09722 | 69xx answers calls differently after firmware upgrade |
| CSCty24748 | Hold/Forward button has no effect while Call Ended popup is
visible |
| CSCty30749 | 69xx pop-up toast doesn't disappear while dialing transfer /
conference |
| CSCty32459 | 69XX reverse numeric digits with Arabic locale |
| CSCty44892 | 69xx 1 Missed call: XXXX not displayed when LINE-12 receives a
call |
| CSCty51278 | 6921/41/61:PO Locale: Personal Directory, Corporate Directory in
English |
| CSCty78955 | 69xx Unable to stop blinking LINE LED after receiving calls |
| CSCty78977 | 6961 freeze when receiving multiple calls simultaneously |
| CSCty84518 | GPickup : 6961 switch from call A to Call B after going in
handset mode |
| CSCty88764 | Corporate Directory issue on 69XX phones |
| CSCty90462 | 'Call Transfer Successful' appear on shareline if Transfer
Onhook enable |
| CSCtz66394 | Screenshot on 6900 series phone without authentication |
| CSCty29289 | 69xx phones freeze due to get_clog_ext_hdr malloc failed |
| Cisco Unified IP Phone 6945 |
| CSCty16495 | 6945 On-Hook Personal Address Book Dialing Fails Across WAN |
| CSCty77368 | Hunt Group Logout LED button turns off after restart on 69xx sip
phones |
| CSCtx76044 | 6945 phone can not handle "()" in corporate directory |
| CSCty11107 | 69xx phones don't respect hierarchical authentication |
| CSCty46888 | "Corporate Directory" always show up even it is not enabled on
cucm. |
| CSCty85247 | 6945 phones sends voice packets untagged after reboot if PC vlan
is 1 |
| CSCtz15149 | 69XX phones should not set Do Not Fragment bit |
| CSCty29289 | 69xx phones freeze due to get_clog_ext_hdr malloc failed |