---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7821-7841-7861-firmware-10-1-1-english-release-notes-pa2d-bk-rfc9d799-cadc8b26ec
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7821_7841_7861/firmware/10_1_1/english/release_notes/PA2D_BK_RFC9D799_00_rn-10_1_1-7821-7841-7861/PA2D_BK_RFC9D799_00_rn-10_1_1-7821-7841-7861_chapter_00.html
retrieved_at: 2026-08-25T12:27:39.398066+00:00
---

Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)

# Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)

Updated: May 23, 2018

Chapter: Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)

## Chapter: Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)

# Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.1(1)

## Introduction

These release notes
                           		support the Cisco IP Phones 7821, 7841, and 7861 running SIP firmware release
                           		10.1(1).

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

## Cisco IP Phone 7800 Series Features

The Cisco® IP
                              		  Phone 7800 Series is a high-fidelity voice communications portfolio designed
                              		  for people- centric collaboration. It combines always-on reliability and
                              		  security, full-featured easy-to-use IP telephony, and wideband audio to
                              		  increase productivity, with an earth-friendly design for reduced costs.

The Cisco IP
                              		  Phone 7800 Series brings a higher quality standard, with full wideband audio
                              		  support for handset, headset and speaker, to our voice-centric portfolio. A new
                              		  ergonomic design includes support for larger grayscale, graphical backlit
                              		  displays. The Cisco IP Phone 7800 Series also offers customers very low power
                              		  consumption, as the phones are IEEE Class 1 devices. Combined with support for
                              		  Cisco EnergyWise™, this delivers greater economies of scale in customers wiring
                              		  closets as well as helping to reduce operating expenditures with energy
                              		  savings. Other key differences include Electronic Hook-switch capability, for
                              		  call control while using third-party headsets, encrypted communications, and a
                              		  field replaceable bezel option.

For more information on the Cisco IP Phone 7800 Series, see http://www.cisco.com/en/US/products/ps13220/tsd_products_support_series_home.html

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

### Install Firmware
                           	 Release on Cisco Unified Communications Manager

Before using the
                                 		  Cisco Unified IP Phone Firmware Release 10.1(1) with Cisco Unified
                                 		  Communications Manager, you must install the latest firmware on all Cisco
                                 		  Unified Communications Manager servers in the cluster.

Step 1

Go to the
                                          			 following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Step 2

Depending on
                                          			 your phone model, choose Cisco
                                             				IP Phones 7800 Series .

Step 3

Choose your
                                          			 phone type.

Step 4

Choose Session Initiation Protocol (SIP) Software .

Step 5

In the Latest
                                          			 Releases folder, choose 10.1(1) .

Step 6

Select one of
                                          			 the following firmware files, click the Download or Add to
                                             				cart button, and follow the prompts:

cmterm-78xx.10-1-1-9.cop.sgn

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

### Install Firmware
                           	 Zip Files

If a Cisco Unified
                                 		  Communications Manager is not available to load the installer program, the
                                 		  following .zip files are available to load the firmware.

cmterm-78xx.10-1-1-9.cop.sgn

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
                                          			 Releases folder, choose 10.1(1) .

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

### Open Caveats

The following table
                              		lists severity 1, 2, and 3 defects that are open for the Cisco IP Phones for
                              		Firmware Release 10.1(1).

For more information
                              		about an individual defect, you can access the online record for the defect by
                              		clicking the Identifier or going to the URL that is shown. You must be a
                              		registered Cisco.com user to access this online information.

Because defect
                              		status continually changes, the table reflects a snapshot of the defects that
                              		were open at the time this report was compiled. For an updated view of open
                              		defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCug60432

Previous
                                          				unregister reason message always show in the unregister screen

CSCuh07996

Phone cannot
                                          				go back to idle state and indicated incoming calls in the line area

CSCuh34236

Display of
                                          				phone is incorrect when PC port/SW port is 10/10

CSCuh34454

Users keep
                                          				hearing high frequency noice in daisy chain environment.

CSCui31769

There is no
                                          				toast but the screen and LED will flash once when press "Pickup" and "Opickup"

CSCui49609

A noisy tone
                                          				when start a voicemail and press hold/resume

CSCui55340

Havn't
                                          				"CallPark Reversion" toast if enable DND-R on Phone

CSCui95975

The details
                                          				of meet-me conf is unavailable on the first party

CSCuj01203

A 7861 phone
                                          				freeze SK and buttons after swap calls once

CSCuj04310

User locale
                                          				select Arabic_Saudi_Arabia;""New call"" softkey is wrong

CSCuj11854

the call
                                          				would not be disconnected after hanging up the handset

CSCuj16464

Monitoring
                                          				phone not send RTCP

CSCuj25165

Highlighted
                                          				backgroound has afterimage when switch among calls on 7861

CSCuj37314

If a call on
                                          				shared line is hold/retrieved multiple times; local & remote log is
                                          				incorrect

CSCuj44373

Phone reset
                                          				auto during do cBarge and recording operation

CSCuj52180

Phone can
                                          				not answer a incoming call with handset

CSCuj52759

IPv6 mode
                                          				phone fail to register if CUCM v4/v6 hostname are different

CSCuj53099

ipv6 address
                                          				is wrong when phone has arabic/hebrew locales

CSCuj53400

No message
                                          				indicate for 2nd incoming call if phone is in app menu

CSCuj64649

Sometimes
                                          				DTMF for digits during VM has a delay

CSCuj67931

7821 SW
                                          				port can not back to AUTO after PALS

CSCuj68134

RTP port
                                          				shoule be closed when hold the call

CSCuj70809

The chaos
                                          				behavior when phone do meet-me with AS-SIP

CSCuj71309

No focus in
                                          				the Applications menu

CSCuj73093

The call
                                          				can't be ended by handset

CSCuj73412

one log
                                          				recorded when the call is transferred with translation pattern

CSCuj74004

Phone not
                                          				open RTCP port when dual mode phone call IPv6 only phone

CSCuj75870

phone load
                                          				information display error

CSCuj76575

Phone fail
                                          				to pass 802.1x authentication for unknown reason

CSCuj76590

AM/PM
                                          				shouldn't be displayed as a small box when locale is Greek

CSCuj78805

Some titles
                                          				with brackets aren't correctly translated into Arabic

CSCuj78823

The titles
                                          				with brackets aren't correctly translated into it_LT locale

CSCuj79769

Outgoing
                                          				call bubble overlaps with Contact Window

CSCuj79970

Calls
                                          				disconnect after one minute

CSCuj82934

Idle URL
                                          				screen can't display if 7861 phone has missed call notification

CSCuj89882

Volume
                                          				overlap

CSCuj90061

daisychain
                                          				phone can't register sometime

CSCuj90768

JPN+KOR+CHS: 78xx: Multi-Byte Service name is corrupted

CSCuj93181

[Wistron]Group pickup; the call log should not recorded group unmber

CSCuj93193

[WistronDT]when phone show change saved successfully in ringtone page

CSCuj93201

[WistronDT]The phone will back to idle when press 4 times speaker

CSCuj93251

[WistronDT]Phone header shows other line number using other line to make

CSCuj96094

DND beep
                                          				not played when on hook from handset

CSCul01193

Phone can't
                                          				add participant by PD in conference/transfer

CSCul01196

Call
                                          				history can't display once

CSCul01236

no phone
                                          				icon nor picture for 78xx phone in CUCM user page

CSCul01935

A incoming
                                          				call can't be answered by the speaker or headset button

### Resolved
                           	 Caveats

The following table
                              		lists severity 1, 2, and 3 defects that are resolved for the Cisco IP Phones
                              		for Firmware Release 10.1(1).

For more information
                              		about an individual defect, you can access the online record for the defect by
                              		clicking the Identifier or going to the URL that is shown. You must be a
                              		registered Cisco.com user to access this online information.

Because defect
                              		status continually changes, the table reflects a snapshot of the defects that
                              		were open at the time this report was compiled. For an updated view of open
                              		defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCug20406

When turn down CUCM and EM service on both hCluster and
                                          				vCluster;phone will registered on hSRST

CSCuh23709

Phone use hDN to failover to vSRST when lost connect to all cucms

CSCuh51175

JAVA usually block when reset all

CSCuf43923

Snoopy plus
                                          				phone can not register back to the CUCM of vCluster after stop the CUCM of
                                          				hcluster

CSCug20387

When phone in
                                          				hold_reverted state; its can alert 10 minutes before Phone Off Time

CSCuh93187

Phone do not
                                          				behavioral normally after press ""BLF direct call park"" PLK"

CSCui46950

UE performance is worse than RTL

CSCui52299

"Speed dial not configured" popup goes very late

CSCui79444

Phone play no
                                          				sound when RTPMRx for 5 min

CSCui92484

Phone UI shows
                                          				different after a wrong FAC code is input.

CSCuj04320

Dark screen
                                          				with crosstalk on 50 Celsius 90% humidity within 24 hours

CSCuj27582

Multi-language
                                          				related bug for Wistron

CSCuj43600

UI issue when
                                          				phone in preservation mode

CSCuj46802

User locale in
                                          				UDP doesn't work

CSCuj46859

7841 phone
                                          				hasn't "call transferred successfully" prompt when dPark done

CSCuj49053

7861:Screen
                                          				overlap when on-hook dial and incoming call

CSCuj49378

7861 lost SKs
                                          				after restart

CSCuj61891

WistronDT not
                                          				show the toast unable to obtain additional ringtones

CSCuj67437

CUCM hostname
                                          				display null on phone if CUCM IPv6 Address set to null

CSCuj68110

FAC Prompt Text doesnot work if changed to non-default

CSCuj70181

7861 can't indicate missed call correctly

CSCuj70644

7861 can't display prompt of missed call and new VM fluently

CSCuj70785

No CTL erase prompt when set alt TFTP from yes to no

CSCuj73999

Only Details
                                          				SK is show when a call comes in

CSCuj78557

phone PLK inconsistent after EMCC logout when vTFTP down

CSCuj78596

There is an extra softkey appears in connect state when locale is
                                          				Greek

CSCuj78720

The direction of the arrow is wrong in Admin Set list if locale
                                          				is ar_SA

CSCuj78811

Memory leak during overnight stress test

CSCuj78841

phone still
                                          				show idle when unplug network cable with power brick connect

CSCuj79787

One factory 7821 does not allow alt TFTP server entry

CSCuj79986

number disappear for long time at dialing stage

CSCuj82581

AMWI tone error for Network Locale Japan

CSCuj82667

Japan Time zone doesn't work

CSCuj82695

NPE during phone's boot & register process

CSCuj85239

78xx phones
                                          				are not able to register

CSCuj86869

Details of Upgrade in Progress are not displayed completely

CSCuj86981

Call history ui is very chaos on one 7821 phone

CSCuj87528

One 7841 phone stuck once after shareline cBarge meet-me
                                          				conference

CSCuj86999

Issues
                                          				occur after phone resume hold revert call

CSCuj87297

Delay to
                                          				enter "IPv4 Setup" menu when keypad index navigation

CSCuj87537

group call
                                          				pickup failed on 2nd line

CSCuj90768

JPN: 7821: Enable Extension Mobility Service name is corrupted

CSCuj93985

Shouldn't show Swap softkey when phone cbarge to shareline

CSCuj94036

Shouldn't show caller softkey when two calls both on remote use

CSCuj95943

link local DAD not work

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

| Step 1 | Go to the
                                          			 following URL: http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Depending on
                                          			 your phone model, choose Cisco
                                             				IP Phones 7800 Series . |
| Step 3 | Choose your
                                          			 phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest
                                          			 Releases folder, choose 10.1(1) . |
| Step 6 | Select one of
                                          			 the following firmware files, click the Download or Add to
                                             				cart button, and follow the prompts: cmterm-78xx.10-1-1-9.cop.sgn Note If you added
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
                                          			 Releases folder, choose 10.1(1) . |
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

| Identifier | Headline |
|---|---|
| CSCug60432 | Previous
                                          				unregister reason message always show in the unregister screen |
| CSCuh07996 | Phone cannot
                                          				go back to idle state and indicated incoming calls in the line area |
| CSCuh34236 | Display of
                                          				phone is incorrect when PC port/SW port is 10/10 |
| CSCuh34454 | Users keep
                                          				hearing high frequency noice in daisy chain environment. |
| CSCui31769 | There is no
                                          				toast but the screen and LED will flash once when press "Pickup" and "Opickup" |
| CSCui49609 | A noisy tone
                                          				when start a voicemail and press hold/resume |
| CSCui55340 | Havn't
                                          				"CallPark Reversion" toast if enable DND-R on Phone |
| CSCui95975 | The details
                                          				of meet-me conf is unavailable on the first party |
| CSCuj01203 | A 7861 phone
                                          				freeze SK and buttons after swap calls once |
| CSCuj04310 | User locale
                                          				select Arabic_Saudi_Arabia;""New call"" softkey is wrong |
| CSCuj11854 | the call
                                          				would not be disconnected after hanging up the handset |
| CSCuj16464 | Monitoring
                                          				phone not send RTCP |
| CSCuj25165 | Highlighted
                                          				backgroound has afterimage when switch among calls on 7861 |
| CSCuj37314 | If a call on
                                          				shared line is hold/retrieved multiple times; local & remote log is
                                          				incorrect |
| CSCuj44373 | Phone reset
                                          				auto during do cBarge and recording operation |
| CSCuj52180 | Phone can
                                          				not answer a incoming call with handset |
| CSCuj52759 | IPv6 mode
                                          				phone fail to register if CUCM v4/v6 hostname are different |
| CSCuj53099 | ipv6 address
                                          				is wrong when phone has arabic/hebrew locales |
| CSCuj53400 | No message
                                          				indicate for 2nd incoming call if phone is in app menu |
| CSCuj64649 | Sometimes
                                          				DTMF for digits during VM has a delay |
| CSCuj67931 | 7821 SW
                                          				port can not back to AUTO after PALS |
| CSCuj68134 | RTP port
                                          				shoule be closed when hold the call |
| CSCuj70809 | The chaos
                                          				behavior when phone do meet-me with AS-SIP |
| CSCuj71309 | No focus in
                                          				the Applications menu |
| CSCuj73093 | The call
                                          				can't be ended by handset |
| CSCuj73412 | one log
                                          				recorded when the call is transferred with translation pattern |
| CSCuj74004 | Phone not
                                          				open RTCP port when dual mode phone call IPv6 only phone |
| CSCuj75870 | phone load
                                          				information display error |
| CSCuj76575 | Phone fail
                                          				to pass 802.1x authentication for unknown reason |
| CSCuj76590 | AM/PM
                                          				shouldn't be displayed as a small box when locale is Greek |
| CSCuj78805 | Some titles
                                          				with brackets aren't correctly translated into Arabic |
| CSCuj78823 | The titles
                                          				with brackets aren't correctly translated into it_LT locale |
| CSCuj79769 | Outgoing
                                          				call bubble overlaps with Contact Window |
| CSCuj79970 | Calls
                                          				disconnect after one minute |
| CSCuj82934 | Idle URL
                                          				screen can't display if 7861 phone has missed call notification |
| CSCuj89882 | Volume
                                          				overlap |
| CSCuj90061 | daisychain
                                          				phone can't register sometime |
| CSCuj90768 | JPN+KOR+CHS: 78xx: Multi-Byte Service name is corrupted |
| CSCuj93181 | [Wistron]Group pickup; the call log should not recorded group unmber |
| CSCuj93193 | [WistronDT]when phone show change saved successfully in ringtone page |
| CSCuj93201 | [WistronDT]The phone will back to idle when press 4 times speaker |
| CSCuj93251 | [WistronDT]Phone header shows other line number using other line to make |
| CSCuj96094 | DND beep
                                          				not played when on hook from handset |
| CSCul01193 | Phone can't
                                          				add participant by PD in conference/transfer |
| CSCul01196 | Call
                                          				history can't display once |
| CSCul01236 | no phone
                                          				icon nor picture for 78xx phone in CUCM user page |
| CSCul01935 | A incoming
                                          				call can't be answered by the speaker or headset button |

| Identifier | Headline |
|---|---|
| CSCug20406 | When turn down CUCM and EM service on both hCluster and
                                          				vCluster;phone will registered on hSRST |
| CSCuh23709 | Phone use hDN to failover to vSRST when lost connect to all cucms |
| CSCuh51175 | JAVA usually block when reset all |
| CSCuf43923 | Snoopy plus
                                          				phone can not register back to the CUCM of vCluster after stop the CUCM of
                                          				hcluster |
| CSCug20387 | When phone in
                                          				hold_reverted state; its can alert 10 minutes before Phone Off Time |
| CSCuh93187 | Phone do not
                                          				behavioral normally after press ""BLF direct call park"" PLK" |
| CSCui46950 | UE performance is worse than RTL |
| CSCui52299 | "Speed dial not configured" popup goes very late |
|  |  |
| CSCui79444 | Phone play no
                                          				sound when RTPMRx for 5 min |
| CSCui92484 | Phone UI shows
                                          				different after a wrong FAC code is input. |
| CSCuj04320 | Dark screen
                                          				with crosstalk on 50 Celsius 90% humidity within 24 hours |
| CSCuj27582 | Multi-language
                                          				related bug for Wistron |
| CSCuj43600 | UI issue when
                                          				phone in preservation mode |
| CSCuj46802 | User locale in
                                          				UDP doesn't work |
| CSCuj46859 | 7841 phone
                                          				hasn't "call transferred successfully" prompt when dPark done |
| CSCuj49053 | 7861:Screen
                                          				overlap when on-hook dial and incoming call |
| CSCuj49378 | 7861 lost SKs
                                          				after restart |
| CSCuj61891 | WistronDT not
                                          				show the toast unable to obtain additional ringtones |
| CSCuj67437 | CUCM hostname
                                          				display null on phone if CUCM IPv6 Address set to null |
| CSCuj68110 | FAC Prompt Text doesnot work if changed to non-default |
| CSCuj70181 | 7861 can't indicate missed call correctly |
| CSCuj70644 | 7861 can't display prompt of missed call and new VM fluently |
| CSCuj70785 | No CTL erase prompt when set alt TFTP from yes to no |
| CSCuj73999 | Only Details
                                          				SK is show when a call comes in |
| CSCuj78557 | phone PLK inconsistent after EMCC logout when vTFTP down |
| CSCuj78596 | There is an extra softkey appears in connect state when locale is
                                          				Greek |
| CSCuj78720 | The direction of the arrow is wrong in Admin Set list if locale
                                          				is ar_SA |
| CSCuj78811 | Memory leak during overnight stress test |
| CSCuj78841 | phone still
                                          				show idle when unplug network cable with power brick connect |
| CSCuj79787 | One factory 7821 does not allow alt TFTP server entry |
| CSCuj79986 | number disappear for long time at dialing stage |
| CSCuj82581 | AMWI tone error for Network Locale Japan |
| CSCuj82667 | Japan Time zone doesn't work |
| CSCuj82695 | NPE during phone's boot & register process |
| CSCuj85239 | 78xx phones
                                          				are not able to register |
| CSCuj86869 | Details of Upgrade in Progress are not displayed completely |
| CSCuj86981 | Call history ui is very chaos on one 7821 phone |
| CSCuj87528 | One 7841 phone stuck once after shareline cBarge meet-me
                                          				conference |
| CSCuj86999 | Issues
                                          				occur after phone resume hold revert call |
| CSCuj87297 | Delay to
                                          				enter "IPv4 Setup" menu when keypad index navigation |
| CSCuj87537 | group call
                                          				pickup failed on 2nd line |
| CSCuj90768 | JPN: 7821: Enable Extension Mobility Service name is corrupted |
| CSCuj93985 | Shouldn't show Swap softkey when phone cbarge to shareline |
| CSCuj94036 | Shouldn't show caller softkey when two calls both on remote use |
| CSCuj95943 | link local DAD not work |