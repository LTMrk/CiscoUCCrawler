---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7821-7841-7861-10-1-english-release-notes-pa2d-bk-r1b754c7-00-rn-10-1-163fe234b2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7821_7841_7861/10_1/english/release_notes/PA2D_BK_R1B754C7_00_rn-10_1_1-7821-41-61-sr1/PA2D_BK_R1B754C7_00_rn-10_1_1-7821-41-64-sr1_chapter_00.html
retrieved_at: 2026-08-25T12:23:13.448016+00:00
---

Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)SR1

# Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)SR1

Updated: May 22, 2018

Chapter: Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)SR1

## Chapter: Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)SR1

# Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)SR1

## Introduction

These release notes
                           		support the Cisco IP Phones 7821, 7841, and 7861 running SIP Firmware Release
                           		10.1(1)SR1.

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

The following sections describe the new and changed features in this release.

### Features Available with Firmware Release

The following sections describe the features available in the firmware.

#### Hardware Updates

The Cisco IP Phone 7841 10.1(1)SR1 release has a hardware update to V02 (VID). Phone manufactured with the new version ID
                                 must run Firmware Release 10.1(1)SR1 or later. The phone firmware does not allow the phone to be downgraded to releases earlier
                                 than Firmware Release 10.1(1)SR1.

No hardware change is applied to Cisco IP Phones 7821 and 7861.

## Related
                        	 Documentation

### Cisco IP Phone 7800 Series Documentation

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Phone 7800 Series.

### Cisco Unified
                              				Communications Manager Documentation

See the Cisco Unified
                                       				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                                    				Communications Manager release on the product support page.

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified
                                 				Communications Manager is running the latest device package. For more information about how to install a Unified CM device package, see Cisco Unified Communications Manager Device Package Installation Guide .

If your Cisco Unified
                                             				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly.

For information on the device packages, see the Cisco Unified
                                 				Communications Manager Device Package Compatibility Matrix .

### Install Firmware Release on Cisco Unified Communications Manager

Before using the
                                 		  Cisco IP Phone Firmware Release 10.1(1)SR1 with Cisco Unified
                                 		  Communications Manager, you must install the latest firmware on all Cisco
                                 		  Unified Communications Manager servers in the cluster.

Step 1

Go to the
                                          			 following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Step 2

Choose Cisco
                                             				IP Phones 7800 Series .

Step 3

Choose your
                                          			 phone type.

Step 4

Choose Session Initiation Protocol (SIP) Software .

Step 5

In the Latest
                                          			 Releases folder, choose 10.1(1)SR1 .

Step 6

Select one of
                                          			 the following firmware files, click the Download or Add to
                                             				cart button, and follow the prompts:

cmterm-78xx.10-1-1SR1-4.cop.sgn

If you added
                                                         				  the firmware file to the cart, click the Download Cart link when you are ready to download
                                                         				  the file.

Step 7

Click the + next to the firmware file name in the Download
                                          			 Cart section to access additional information about this file. The hyperlink
                                          			 for the readme file is in the Additional Information section, which contains
                                          			 installation instructions for the corresponding firmware.

Step 8

Follow the
                                          			 instructions in the readme file to install the firmware.

### Install Firmware Zip Files

If a Cisco Unified
                                 		  Communications Manager is not available to load the installer program, the
                                 		  following .zip files are available to load the firmware.

cmterm-78xx.10-1-1SR1-4.zip

Firmware upgrades
                                 		  over the WLAN interface may take longer than upgrades using a wired connection.
                                 		  Upgrade times over the WLAN interface may take more than an hour, depending on
                                 		  the quality and bandwidth of the wireless connection.

Step 1

Go to the
                                          			 following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Step 2

Choose Cisco
                                             				IP Phones 7800 Series .

Step 3

Choose your
                                          			 phone type.

Step 4

Choose Session Initiation Protocol (SIP) Software .

Step 5

In the Latest
                                          			 Releases folder, choose 10.1(1)SR1 .

Step 6

Download the
                                          			 relevant zip files.

Step 7

Unzip the
                                          			 files.

Step 8

Manually copy
                                          			 the unzipped files to the directory on the TFTP server. See Cisco
                                             				Unified Communications Operating System Administration Guide for
                                          			 information about how to manually copy the firmware files to the server.

## Limitations and Restrictions

### Manufacturing Installed Certificate Signature and SHA-256 Support

The manufacturing installed certificate(MIC) signature has been updated from SHA-128 with RSA to SHA-256 with RSA. You must
                                 update and install the new SHA-2 certificates on the Cisco Unified Communications Manager for secure mode to function. You
                                 can download the new certificate from http://www.cisco.com/security/pki/certs/cmca2.cer .

Cisco Unified Communications Manager

Cisco Unified Survivable Remote Site Telephony

Cisco Secure Access Control System

Cisco Identity Services Engine

For additional information about SHA-2 use and support, see Security Guide for Cisco Unified Communications Manager ( https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html ).

### Voice VLAN and
                           	 IPv6 Limitation

If the PC attached to the PC port of the phone is using IPv6, we recommend that the PC Voice LAN access be disabled. This
                                 ensures that the PC cannot connect to the Voice VLAN.

### Phone Behavior
                           	 During Times of Network Congestion

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

## Unified
                        	 Communications Manager Endpoints Locale Installer

By default, Cisco IP Phones are set up for the English (United States) locale. To use the Cisco IP Phones in other locales,
                              you must install the locale-specific version of the Unified Communications Manager Endpoints Locale Installer on every Cisco Unified
                                 				Communications Manager server in the cluster. The Locale Installer installs the latest translated text for the phone user interface and country-specific
                              phone tones on your system so that they are available for the Cisco IP Phones.

To access the Locale Installer required for a release, access the Software Download page, navigate to your phone model, and select the Unified Communications Manager Endpoints Locale Installer link.

For more information, see the documentation for your particular Cisco Unified
                                 				Communications Manager release.

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
                                 		  problems by using Cisco Bug Search.

#### Before you begin

To access Cisco Bug
                                 		  Search, you need the following items:

Internet
                                       				connection

Web browser

Cisco.com user
                                       				ID and password

Step 1

To access Cisco Bug Search, go to:

https://bst.cloudapps.cisco.com/bugsearch

Step 2

Log in with your
                                          			 Cisco.com user ID and password.

Step 3

To look for
                                          			 information about a specific problem, enter the bug ID number in the Search for
                                          			 field, then press Enter .

### Open
                           	 Caveats

The following
                              		table lists severity 1, 2, and 3 defects that are open for the Cisco IP Phones
                              		for Firmware Release 10.1(1)SR1.

For more
                              		information about an individual defect, you can access the online record for
                              		the defect by clicking the Identifier or going to the URL that is shown. You
                              		must be a registered Cisco.com user to access this online information.

Because defect
                              		status continually changes, the table reflects a snapshot of the defects that
                              		were open at the time this report was compiled. For an updated view of open
                              		defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCuh34236

Display of
                                          				phone is incorrect when PC port/SW port is 10/10

CSCuj16464

Monitoring
                                          				phone not send RTCP

CSCuj25165

Highlighted
                                          				backgroound has afterimage when switch among calls on 7861

CSCuj52759

IPv6 mode
                                          				phone fail to register if CUCM v4/v6 hostname are different

CSCuj53400

No message
                                          				indicate for 2nd incoming call if phone is in app menu

CSCuj73412

one log
                                          				recorded when the call is transferred with translation pattern

CSCuj93181

Group
                                          				pickup; the call log should not recorded group unmber

CSCuj96094

DND beep not
                                          				played when on hook from handset

CSCul01193

Phone can't
                                          				add participant by PD in conference/transfer

CSCul19064

Press the
                                          				update SK and then press the back SK navigation har

CSCul19068

It will
                                          				flash secure icon one time after answer a call

CSCul28593

The line
                                          				with '#' in the DN still display on phone's ui in srst mode

CSCun07043

DN
                                          				displaying wrongly during transfer in 7841 phone Model

CSCun30345

78xx :line
                                          				Led behavior wrong if phone has incoming and hold revert call

CSCun35603

missed call
                                          				number not increased accordingly

CSCun35740

78xx can't
                                          				access VM when setting media using ipv6 prefer.

CSCun38492

Kate
                                          				overlap the SK

CSCun45084

incoming
                                          				call toast behavior not consentaneous

CSCun45099

extra
                                          				cursor on 7861 when dial quick after cancel previous dialing

CSCun45165

Call is
                                          				dropped unexpectedly after pressing resume softkey

CSCun45175

local/remote ipv6 addr under stream info error in webpage

CSCun45190

arabic/Hebrew:v6 gateway/v6 dns/tftp v6 address orientation is wrong

CSCun46787

7861:UI
                                          				still display missed calls state if remote call in hold

CSCun46904

Line LED
                                          				not changed to green for active call if remote hold there

CSCun47170

Icon shows
                                          				wrong for share line testbed

CSCun47290

phone
                                          				couldn't switch to another line if 2 remote hold call bubble there

CSCun47366

line key
                                          				flashing too long time for broadcast huntgroup

CSCun47509

call bubble
                                          				not show for huntgroup number

CSCun50430

phone EW
                                          				alerting is abnormal after making an incoming call

CSCun50485

78xx Can
                                          				not use the default gateway as SRST

CSCun51311

not support
                                          				the 32-bit SRTCP

CSCun55006

Phone will
                                          				send out a number automatically after offhook

### Resolved
                           	 Caveats

The following
                              		table lists severity 1, 2, and 3 defects that are resolved for the Cisco IP
                              		Phones that use Firmware Release 10.1(1)SR1.

For more
                              		information about an individual defect, you can access the online record for
                              		the defect by clicking the Identifier or going to the URL that is shown. You
                              		must be a registered Cisco.com user to access this online information.

Because defect
                              		status continually changes, the table reflects a snapshot of the defects that
                              		were open at the time this report was compiled. For an updated view of open
                              		defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCuj70181

7861 can't
                                          				indicate missed call correctly

CSCuj70644

7861 can't
                                          				display prompt of missed call and new VM fluently

CSCuj82934

Idle URL
                                          				screen can't display if 7861 phone has missed call notification

CSCuj90768

CSCul09519

No alert
                                          				info returns via cli command when power saving alert pop up

CSCul14019

78XX webpage
                                          				shows ITL file not installed when it is installed

CSCul65321

making a new
                                          				call when hoot&holler is active may lead to phone's crash

CSCul80224

ATA186/187
                                          				consumes Enhanced UCL After Device Pack 9.1.2.11013-1 install

CSCum11153

CTL file
                                          				display not correct on 78XX phone

CSCum18214

7800 series
                                          				phones do not prevent shared lines from being used if the lines have already
                                          				hit maxcalls

CSCum42565

78xx: phone
                                          				can't answer call on CME byspeaker/headset/handset

CSCum47662

can't
                                          				answer call by speaker/headset/handset when MNC/BT set to 1/1

CSCum71019

CSCun03177

CSCun04706

Cancel
                                          				button not working in 7841 Phones during transfer

CSCun06634

78xx :
                                          				shareline line key flash wrongly

CSCun06643

78xx :
                                          				missed call count disappear unexpectedly

CSCun09390

78xx: 7841
                                          				line icon stuck in ringin state after many incoming calls.

CSCun09496

78xx no
                                          				"Call transferred successfully" after on-hook transfer

CSCun09667

7841 sw/pc
                                          				port speed/duplex can't be updated from cucm.

CSCun17651

7861 send
                                          				malformed "From" field in keepalive cause phone unregister

CSCun20005

78xx: new
                                          				incoming call toast shows '0 incoming calls'

CSCun20057

CP78xx Park
                                          				number is disappeared after OnHook

CSCun20060

78xx: can't
                                          				answer incoming call when checking its detail.

CSCun20186

Park number
                                          				is not displayed in 7841 phone model in second line

CSCun23612

7841 Cannot
                                          				join VLAN if broadcast over 30kbps

CSCun29884

78xx : not
                                          				focus on the incoming call from call pickup

CSCun30490

7821/41 has
                                          				no call toast when phone is off hook and new call comes in

CSCun32516

phone can't
                                          				enter into energywise after incoming call

CSCun35676

7861:UI
                                          				issues if make call between shared lines

CSCun37850

phone will
                                          				dial out to the speed dial number after press CFA

CSCun46873

Park number
                                          				is displayed a moment and disappeared sometimes

## Cisco IP Phone
                        	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/c/en/us/td/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application.
                           The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco IP Phone | Protocol | Cisco Unified
                                       				Communications Manager |
|---|---|---|
| Cisco IP
                                       				Phones 7821, 7841, and 7861 | SIP | Cisco Unified Communications Manager Release 8.5(1) or later Cisco Unified
                                       				Communications Manager DST Olsen version D or later |

| Note | If your Cisco Unified
                                             				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the
                                          			 following URL: http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco
                                             				IP Phones 7800 Series . |
| Step 3 | Choose your
                                          			 phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
                                          			 Releases folder, choose 10.1(1)SR1 . |
| Step 6 | Select one of
                                          			 the following firmware files, click the Download or Add to
                                             				cart button, and follow the prompts: cmterm-78xx.10-1-1SR1-4.cop.sgn Note If you added
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
                                          			 following URL: http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco
                                             				IP Phones 7800 Series . |
| Step 3 | Choose your
                                          			 phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
                                          			 Releases folder, choose 10.1(1)SR1 . |
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

| Step 1 | To access Cisco Bug Search, go to: https://bst.cloudapps.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                                          			 Cisco.com user ID and password. |
| Step 3 | To look for
                                          			 information about a specific problem, enter the bug ID number in the Search for
                                          			 field, then press Enter . |

| Identifier | Description |
|---|---|
| CSCuh34236 | Display of
                                          				phone is incorrect when PC port/SW port is 10/10 |
| CSCuj16464 | Monitoring
                                          				phone not send RTCP |
| CSCuj25165 | Highlighted
                                          				backgroound has afterimage when switch among calls on 7861 |
| CSCuj52759 | IPv6 mode
                                          				phone fail to register if CUCM v4/v6 hostname are different |
| CSCuj53400 | No message
                                          				indicate for 2nd incoming call if phone is in app menu |
| CSCuj73412 | one log
                                          				recorded when the call is transferred with translation pattern |
| CSCuj93181 | Group
                                          				pickup; the call log should not recorded group unmber |
| CSCuj96094 | DND beep not
                                          				played when on hook from handset |
| CSCul01193 | Phone can't
                                          				add participant by PD in conference/transfer |
| CSCul19064 | Press the
                                          				update SK and then press the back SK navigation har |
| CSCul19068 | It will
                                          				flash secure icon one time after answer a call |
| CSCul28593 | The line
                                          				with '#' in the DN still display on phone's ui in srst mode |
| CSCun07043 | DN
                                          				displaying wrongly during transfer in 7841 phone Model |
| CSCun30345 | 78xx :line
                                          				Led behavior wrong if phone has incoming and hold revert call |
| CSCun35603 | missed call
                                          				number not increased accordingly |
| CSCun35740 | 78xx can't
                                          				access VM when setting media using ipv6 prefer. |
| CSCun38492 | Kate
                                          				overlap the SK |
| CSCun45084 | incoming
                                          				call toast behavior not consentaneous |
| CSCun45099 | extra
                                          				cursor on 7861 when dial quick after cancel previous dialing |
| CSCun45165 | Call is
                                          				dropped unexpectedly after pressing resume softkey |
| CSCun45175 | local/remote ipv6 addr under stream info error in webpage |
| CSCun45190 | arabic/Hebrew:v6 gateway/v6 dns/tftp v6 address orientation is wrong |
| CSCun46787 | 7861:UI
                                          				still display missed calls state if remote call in hold |
| CSCun46904 | Line LED
                                          				not changed to green for active call if remote hold there |
| CSCun47170 | Icon shows
                                          				wrong for share line testbed |
| CSCun47290 | phone
                                          				couldn't switch to another line if 2 remote hold call bubble there |
| CSCun47366 | line key
                                          				flashing too long time for broadcast huntgroup |
| CSCun47509 | call bubble
                                          				not show for huntgroup number |
| CSCun50430 | phone EW
                                          				alerting is abnormal after making an incoming call |
| CSCun50485 | 78xx Can
                                          				not use the default gateway as SRST |
| CSCun51311 | not support
                                          				the 32-bit SRTCP |
| CSCun55006 | Phone will
                                          				send out a number automatically after offhook |

| Identifier | Headline |
|---|---|
| CSCuj70181 | 7861 can't
                                          				indicate missed call correctly |
| CSCuj70644 | 7861 can't
                                          				display prompt of missed call and new VM fluently |
| CSCuj82934 | Idle URL
                                          				screen can't display if 7861 phone has missed call notification |
| CSCuj90768 | JPN+KOR+CHS:
                                          				78xx: Multi-Byte Service name is corrupted Note The fix
                                                      				  for this defect will be available with the next device pack. | Note | The fix
                                                      				  for this defect will be available with the next device pack. |
| Note | The fix
                                                      				  for this defect will be available with the next device pack. |
| CSCul09519 | No alert
                                          				info returns via cli command when power saving alert pop up |
| CSCul14019 | 78XX webpage
                                          				shows ITL file not installed when it is installed |
| CSCul65321 | making a new
                                          				call when hoot&holler is active may lead to phone's crash |
| CSCul80224 | ATA186/187
                                          				consumes Enhanced UCL After Device Pack 9.1.2.11013-1 install |
| CSCum11153 | CTL file
                                          				display not correct on 78XX phone |
| CSCum18214 | 7800 series
                                          				phones do not prevent shared lines from being used if the lines have already
                                          				hit maxcalls |
| CSCum42565 | 78xx: phone
                                          				can't answer call on CME byspeaker/headset/handset |
| CSCum47662 | can't
                                          				answer call by speaker/headset/handset when MNC/BT set to 1/1 |
| CSCum71019 | BLF on 7841
                                          				phone appears blank on applying the Hebrew Locale. Note The fix
                                                      				  for this defect will be available with the next device pack. | Note | The fix
                                                      				  for this defect will be available with the next device pack. |
| Note | The fix
                                                      				  for this defect will be available with the next device pack. |
| CSCun03177 | 7821 phones
                                          				consume Enhanced UCL instead of Basic - in CUCM 9.x and 10.x. Note The fix
                                                      				  for this defect will be available with the next device pack. | Note | The fix
                                                      				  for this defect will be available with the next device pack. |
| Note | The fix
                                                      				  for this defect will be available with the next device pack. |
| CSCun04706 | Cancel
                                          				button not working in 7841 Phones during transfer |
| CSCun06634 | 78xx :
                                          				shareline line key flash wrongly |
| CSCun06643 | 78xx :
                                          				missed call count disappear unexpectedly |
| CSCun09390 | 78xx: 7841
                                          				line icon stuck in ringin state after many incoming calls. |
| CSCun09496 | 78xx no
                                          				"Call transferred successfully" after on-hook transfer |
| CSCun09667 | 7841 sw/pc
                                          				port speed/duplex can't be updated from cucm. |
| CSCun17651 | 7861 send
                                          				malformed "From" field in keepalive cause phone unregister |
| CSCun20005 | 78xx: new
                                          				incoming call toast shows '0 incoming calls' |
| CSCun20057 | CP78xx Park
                                          				number is disappeared after OnHook |
| CSCun20060 | 78xx: can't
                                          				answer incoming call when checking its detail. |
| CSCun20186 | Park number
                                          				is not displayed in 7841 phone model in second line |
| CSCun23612 | 7841 Cannot
                                          				join VLAN if broadcast over 30kbps |
| CSCun29884 | 78xx : not
                                          				focus on the incoming call from call pickup |
| CSCun30490 | 7821/41 has
                                          				no call toast when phone is off hook and new call comes in |
| CSCun32516 | phone can't
                                          				enter into energywise after incoming call |
| CSCun35676 | 7861:UI
                                          				issues if make call between shared lines |
| CSCun37850 | phone will
                                          				dial out to the speed dial number after press CFA |
| CSCun46873 | Park number
                                          				is displayed a moment and disappeared sometimes |

| Note | The fix
                                                      				  for this defect will be available with the next device pack. |
|---|---|

| Note | The fix
                                                      				  for this defect will be available with the next device pack. |
|---|---|

| Note | The fix
                                                      				  for this defect will be available with the next device pack. |
|---|---|