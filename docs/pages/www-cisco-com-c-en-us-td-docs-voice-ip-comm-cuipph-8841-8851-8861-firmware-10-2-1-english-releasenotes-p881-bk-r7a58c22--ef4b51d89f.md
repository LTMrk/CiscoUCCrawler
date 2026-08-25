---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8841-8851-8861-firmware-10-2-1-english-releasenotes-p881-bk-r7a58c22--ef4b51d89f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8841_8851_8861/firmware/10-2-1/english/ReleaseNotes/P881_BK_R7A58C22_00_rn-10_2_1-8841-8851-8861/P881_BK_R7A58C22_00_rn-10_2_1-8841-8851-8861_chapter_00.html
retrieved_at: 2026-08-25T14:06:54.028197+00:00
---

Cisco IP Phone 8841, 8851, and 8861 Release Notes for Firmware Release 10.2(1)

# Cisco IP Phone 8841, 8851, and 8861 Release Notes for Firmware Release 10.2(1)

Updated: June 14, 2017

Chapter: Cisco IP Phone 8841, 8851, and 8861 Release Notes for Firmware
Release 10.2(1)

## Chapter: Cisco IP Phone 8841, 8851, and 8861 Release Notes for Firmware
Release 10.2(1)

# Cisco IP Phone 8841, 8851, and 8861 Release Notes for Firmware
                     Release 10.2(1)

## Introduction

These release notes support the Cisco IP Phones 8841, 8851, and 8861
                           		running SIP Firmware Release 10.2(1).

The following table lists the support and protocol compatibility for the Cisco IP Phones.

Cisco IP Phone

Protocol

Support Requirements

Cisco IP Phones 8841, 8851, and 8861

SIP

Cisco Unified Communications Manager 8.5(1) and later

Cisco Unified Communications Manager DST Olsen version D or later

SRST 8.0 (IOS load 15.1(1)T) and above

CME 10.0 (IOS load 15.3(3)M) and above through
                                       Fast-Track

## Cisco IP Phone 8841, 8851, and 8861 Features

The Cisco IP Phone 8841, 8851, and 8861 delivers easy-to-use, highly secure voice communications. Cisco Intelligent Proximity
                           integrates telephony features with  personal mobile devices. Options, including support for Wi-Fi networks, offer added flexibility.

A comprehensive set of Cisco Unified Communications
                           Manager features are supported.

The following sections describe some of the important phone features. For more information, see http://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-8800-series/index.html .

### Bluetooth Handsfree Profile Audio Gateway

Cisco IP Phones 8851 and 8861 support Hands-free Audio Gateway mode to work with your Bluetooth headset.

### Cisco Intelligent Proximity Support

Users can
                              share contacts and call history. They can also move the audio path of active
                              voice and video calls from a personal mobile device to the Cisco IP Phone 8851 and Cisco IP Phone 8861 for a superior audio
                              experience.

The Cisco IP Phones 8851 and 8861 support contact and
                                    call history sharing from the mobile cellular device through the Bluetooth PBA profile. A maximum of  1500 contacts can be
                                    imported and
                                    displayed on Cisco IP Phones 8851 and 8861. Each contact item can have a maximum of  5
                                    numbers with a maximum 30 characters for each number. The allowed
                                    contact name is a maximum of 60 characters.

When an Android phone is connected, the user sees
                                                an alert pop-up asking whether Phone Book Access is allowed on that
                                                Android device. The user must select Allowed within 30 seconds in
                                                order to import the Android phone book to Cisco IP Phones 8851 and 8861.

An iPhone can connect to two Cisco IP Phones 8851 and 8861 at the same
                                                time, but only one of the IP phones can access the iPhone phone book.

Cisco IP Phones 8851 and 8861 support Hands-free Unit mode
                                    to work with mobile cellular devices for full telephony integration
                                    and two-way hands-free audio.

Hands-free Unit mode with mobile cellular devices  is only supported on the following devices:

Apple iPhone 4 and 5 series

Samsung Galaxy S4, Note 2, and Note 3 series

### IPMA Support

The Cisco IP Phones 8841, 8851, and 8861 support Cisco IP Manager Assistant (IPMA). IPMA is supported on Cisco Unified Communications
                              Manager Releases 9.1(2) SU2 and 10.5.

Support for IPMA on the Cisco Unified Communications Manager Releases 8.6 and 10.0 will be available soon.

IPMA is not supported on Cisco Unified Communications Manager Release 8.5.1 or earlier.

### SHA-256 Manufacturing Installed Certificate

The Cisco IP Phones 8841, 8851, and 8861 use a manufacturing installed certificate (MIC) with
                              the signature algorithm of SHA-256 with an RSA 2048 key. The signature
                              algorithm requires Cisco Unified Communications Manager, ACS, and Secure SRST support.

The Cisco certificate authority issuing the MIC for
                              this series of phones can be obtained from the following links if
                              separate applications are used and these applications need to authenticate MIC from
                              the phone.

http://www.cisco.com/security/pki/certs/cmca2.cer

http://www.cisco.com/security/pki/certs/crcam2.cer

The SHA-256 MIC feature has the following support requirements:

Cisco Unified Communications Manager releases:

The compatible Cisco Unified Communications Manager releases are Cisco Unified Communications Manager 9.1(2) and
                                          later.

Cisco Unified Communications Manager 8.6(2) support is planned.

There is
                                          no plan to support this SHA-256 MIC on Cisco Unified Communications Manager Release 8.5 or earlier.

The compatible ACS release is ACS 5.2 and
                                    later.

The compatible SRST release is IOS 12.4(15)T1 and
                                    later.

### USB Charging

The Cisco IP Phones 8851 and 8861 allow users to charge personal mobile devices using the phone USB ports. The following table
                              describes the USB charging specifications for personal mobile devices.

Smart phone charging

Yes (802.3af)

Yes (802.3af)

Tablet charging

No (no back USB port)

Yes (802.3at)

The side USB port on the Cisco IP Phones 8851 and 8861 only supports slow
                              charging with limited 500mA/2.5W maximum power.

The back USB port on the Cisco IP Phone 8861 supports fast charging up
                              to 2.1A/10.5W maximum power.

When the Cisco IP Phone 8861 is using PoE with an 802.3af switch, the back USB port  can only work in slow-charging mode
                                          due to the limited power supply from 802.3af switch.

### Wi-Fi Client

The Cisco IP Phone 8861 supports campuses with 802.11a/b/g/n/ac
                              WLAN enabled. Customers need to ensure that 12 Mbps is enabled in the WLAN
                              Controller or Access Point (AP) data rate configuration.

We recommend that customers use 5 GHz as there are more channels and less
                              interferers with those frequencies.

Attention

The network administrator must ensure that the AP configuration conforms to local regulatory laws.

## Related
                        	 Documentation

### Cisco IP Phone 8800 Series Documentation

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Phone 8800 Series.

For help information about Cisco Video Phone 8875, see Cisco Video Phone 8875 .

The Deployment Guide is located at the following URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-implementation-design-guides-list.html

### Cisco Unified
                              				Communications Manager Documentation

See the Cisco Unified
                                       				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                                    				Communications Manager release on the product support page.

## Installation

### Install the Firmware
                           	 Release on the Cisco Unified Communications Manager

Before using the phone firmware release on
                                 		  the Cisco Unified Communications Manager, you must install the latest Cisco Unified Communications Manager firmware on
                                 		  all Cisco Unified Communications Manager servers in the cluster.

Step 1

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Step 2

Depending on your phone model, choose Cisco IP Phone 8800 Series .

Step 3

Choose your phone type.

Step 4

Choose Session Initiation Protocol (SIP) Software .

Step 5

In the Latest Releases folder, choose 10.2(1) .

Step 6

Select one of the following firmware files, click the Download or Add to cart button, and follow the prompts:

cmterm-88xx-sip.10-2-1-16.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to
                                                         				  download the file.

Step 7

Click the + next to the firmware file name in the
                                          			 Download Cart section to access additional information about this file. The
                                          			 hyperlink for the readme file is in the Additional Information section, which
                                          			 contains installation instructions for the corresponding firmware.

Step 8

Follow the instructions in the readme file to install the
                                          			 firmware.

### Install Firmware
                           	 Zip Files

If a Cisco Unified Communications Manager is not available to load the
                                 		  installer program, the following .zip files are available to load the firmware.

cmterm-88xx-sip.10-2-1-16.zip

Firmware upgrades over the WLAN interface may take longer than
                                 		  upgrades using a wired connection. Upgrade times over the WLAN interface may
                                 		  take more than an hour, depending on the quality and bandwidth of the wireless
                                 		  connection.

Step 1

Go to the following URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Step 2

Choose Cisco IP Phones 8800 Series .

Step 3

Choose your phone type.

Step 4

Choose Session Initiation Protocol (SIP) Software .

Step 5

In the Latest Releases folder, choose 10.2(1) .

Step 6

Download the relevant zip files.

Step 7

Unzip the files.

Step 8

Manually copy the unzipped files to the directory on the TFTP
                                          			 server. See Cisco Unified Communications Operating System Administration
                                             				Guide for information about how to manually copy the firmware files to
                                          			 the server.

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

## Limitations and Restrictions

### Bluetooth Phone Book Access Profile Limitations

Cisco IP Phones 8851 and 8861 cannot display certain characters in
                                    the Contact/Call history imported from a mobile device if those
                                    characters are not included in the phone  locale.

In this release, Cisco IP Phones 8851 and 8861 do not support the ability to
                                    initiate a new call from the mobile contact book through the Cisco Unified Communications Manager VoIP
                                    network.

### Bluetooth Handsfree Profile Limitations

Only one Bluetooth device can be connected with
                                    Cisco IP Phones 8851 and 8861 at the same time, either a BT headset or a mobile phone.

Tablet pairing and connecting is not supported in
                                    this release.

Due to mobile device OS limitations, some soft
                                    clients on a mobile device (for example, Cisco Jabber or Skype) cannot make
                                    full telephony integration with Cisco IP Phones 8851 and 8861 for call controls
                                    like Answer, End, Hold, or Resume a call. Some known issues
                                    include:

The incoming call event sent from mobile soft client
                                          to Cisco IP Phones 8851 and 8861 causes the ongoing VoIP call to go on hold
                                          automatically.

The call information might not be displayed correctly
                                          on Cisco IP Phones 8851 and 8861.

The call session does not disappear on Cisco IP Phones 8851 and 8861 when
                                          the Jabber call ends on the mobile device. Jabber version 10.5 and later removes this limitation.

### Phone Behavior
                           	 During Times of Network Congestion

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

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
                                 		  table lists severity 1, 2, and 3 defects that are open for the Cisco Unified IP
                                 		  Phones that use Firmware Release 10.2(1).

For more
                                 		  information about an individual defect, you can access the online record for
                                 		  the defect by clicking the Identifier or going to the URL that is shown. You
                                 		  must be a registered Cisco.com user to access this online information.

Because defect
                                 		  status continually changes, the table reflects a snapshot of the defects that
                                 		  were open at the time this report was compiled. For an updated view of open
                                 		  defects, access Bug Toolkit as described in Access Cisco Bug Search .

CSCum62659

Phone will DNS query (none).domain after reset

CSCum64968

Display not be lit when On-Time comes with duration 00:00

CSCum75600

Wrong CUCM IP address in REFER before and after re-registration

CSCun19698

Conference feature layer shall close while participant side park.

CSCun24183

8861 doesn't make active scan in roaming

CSCun29272

8861 may doesn't reply eap-request in roaming

CSCun30024

Phone can answer a call from same phone

CSCun38032

Accessary(CDROM) Added window keeps pop up forever

CSCun41637

Wrong ReasonForOutOfService after IP address lost

CSCun47590

softkey response time is long

CSCun62056

Unable to complete conference; toast is wrong.

CSCun64117

ethernet interface drops 2% packet periodically

CSCun72773

Phone still shown as Application softkey set when register back to CCM

CSCun75414

USB headset on 8851 phone volume not loud enough

CSCun77699

CLI: show stream summary; should have only 1 active stream

CSCun78088

softkeys for xml file is gray and xml file is not display

CSCun78115

Line sequence in Ringtone menu not consistent with line button order

CSCun80759

Incorrect date showed in "Status Messages" after changing phone's load

CSCun83523

8861 ipv6:phone restart several times if 1st CUCM refused the register

CSCun88493

Service URL PLK doesn't work when failover to SRST

CSCun88943

Toast window not popup in time when feature PLK pressed

CSCun93340

iPad Mini USB charging caused Switches shut down the switch port of 8861

CSCun93597

CLI: Cannot get callReference from SessionItemModel

CSCun94444

CLI:Remote call state return empty via cli when shared line during call.

CSCun96422

Missing XML section in ModeInfo of Add Bluetooth Device window

CSCun98930

CLI:"show line all" cannot show "All Calls" line in bigeasy

CSCun99543

CLI: Call state show incorrectly via cli when phone play busy tone.

CSCuo02024

Character can't be shown on the UI if use a white color background image

CSCuo04139

UI response slow if configure multiple PFK BLF SD with same destination

CSCuo10939

CLI: erase ctl, but ctl is still shown

CSCuo10969

Connect/disconnect USB cause wrong last upgrade time on phone UI

CSCuo18535

Crash when plug/unplug usb hub during call

CSCuo18546

plugin/plugout USB hub, phone stuck.

CSCuo18779

8861 establish a call very slowly

CSCuo21617

MWI LED off and icon disappear for seconds after power cycle

CSCuo23873

post 'key:Key:KeyPad0 to Key:KeyPad9' can not work when display is off

CSCuo26551

Earring should not be heard from headset when DND reject call on.

CSCuo26761

No lock icon at the intercom received side sometimes

CSCuo31268

setRingtone Failed if phone stay on ringtone list page

CSCuo31577

Dial window flash twice when there's other app window behind

CSCuo33582

Sometimes iphone disconnected automatically after it connected with BE

CSCuo34073

No 'DHCP6 BOUND' status message for network statistics

CSCuo35638

Pilot number overlap with the scroll bar if pilot long enough

CSCuo35834

Missed call icon not display on related line if restart on one 8851

CSCuo38121

<< softkey didn't greyed even no digit here

CSCuo38272

Wrong message for dns down when phone accesses url with domain name

CSCuo40264

iPhone does not automatical connected after paired successful

CSCuo40482

share line key led is off after switch to another line in a short time

CSCuo40517

The statistics for starMedia URI is only 1 direction

CSCuo42529

Prompt IPC error in Jindo after running switch load scripts

CSCuo42726

HFU signal display not accurate on the phone

CSCuo42755

Phone can't exit from the error application

CSCuo43206

Autopickup history is incorrectly logged

CSCuo45443

Conference call history issues

CSCuo45740

Phone may fails to accept some IPv6 multicast packets over Wi-Fi

CSCuo47255

8861 rebooted by itself when resuming a call.

CSCuo47261

No focus when switching to missed call list view

CSCuo47265

Phone still ring after all calls are ended

CSCuo47545

Nav_select hardkey didn't work on xsi object

CSCuo47565

phone doesn't show valid information when not configure the primary line

CSCuo47589

No available line to play the message during VVM stress test

CSCuo48017

Wong alert trust list message but no tftp server change

CSCuo50527

change alt-tftp tftp 1 will blank tftp 2

CSCuo50761

IPv6 default router manual config cleared after switching to IPv4

CSCuo50988

Some noise heard on 8861 P2 during a call.

CSCuo51021

UI of paired devices for bluetooth page is not friendly

CSCuo51154

Phone shouldn't send RTCP package with even number during intercom call

CSCuo51278

Bluetooth ICON disappeared.

CSCuo52950

hourly archived logs are listed in disorder

CSCuo52962

phone is stuck when alter tftp to HCUCM

CSCuo52966

8861 connect with another AP slowly when the current AP disable

CSCuo53035

A blank screen shown if press back hardkey to exit a service

CSCuo53058

88xx Phone should remember password/username for HTTP service

CSCuo53169

Missed call icon on 2nd line disappear after open HFU

CSCuo53422

Audio disconnect after roaming

CSCuo53623

Phone stuck once after pressing hfu on/off quickly

CSCuo53938

Application windows can't regenerate after end the call

CSCuo55437

The LineInfo for HFU is wrong

CSCuo55493

phone plays old ringtone chirp instead of Delight

CSCuo55998

Phone restart during EM stress test

CSCuo56015

sometimes TFTP server IP cannot be cleared by UI after releasing DHCPv4

CSCuo56065

DN logged in history detail page is incorrect

CSCuo59730

URI share line can not record call log

CSCuo59782

New call window appear slower than white background when dial by speaker

CSCuo59994

8861 slow response to the network change

CSCuo61369

Still highlight the previous item after disable setting access

CSCuo61370

[IPMA]Assistant status window popup problem when hold/resume call

CSCuo61390

Different display about conference in Recents

CSCuo61398

delete softkey always disabled

CSCuo61740

8861 may register fail after wifi Session Timeout

CSCuo61741

Press NAV_Select hardkey will create a new session

CSCuo61789

UI slow in dozens of seconds after phone restart and configured with DNs

CSCuo61817

Fail to connect to EM service during EM stress test

CSCuo61867

Dial intra-cluster call from call history will fail

CSCuo61925

arp cache not timeout on wlan interface as defined by dhcp option 35

CSCuo62126

unknown string ??? display on "Status Message" page

CSCuo62506

Wrong history logged for anonymous@domain uri call

CSCuo62527

application window still on the top when make a HFU call

CSCuo62589

Phone can't enter the sub-window when pressing digit

CSCuo62598

Bluetooth menu is still accessible when settings access is disable

CSCuo62648

disable contacts access on BE, HFU line call history still exist.

CSCuo62944

Analog headset can hear voice from Handset in activated call

CSCuo64323

The order of PBAP contacts menu changes if get exit then enter in

CSCuo64598

delete softkey always enabled in wireless sign in page

CSCuo64696

no CUCM/TFTP/CAPF/TVS when checking CTL/ITL

CSCuo64830

8861 WLAN call duration test failed with "Network Busy"

CSCuo64846

incorrect administrator password is kept for inputting

CSCuo64877

No TCLAS for IPv6 signal or voice stream

CSCuo64886

Speed Dial softkey enabled on CME

CSCuo65174

PBAP contacts not refresh immediately if disable bluetooth contacts

CSCuo65477

screen turn off to black and show cisco log again when booting

CSCuo67334

White screen will last 1-2 second during phone bootup

CSCuo67572

The speaker still light after the HFU call audio moved to cellphone

CSCuo67644

The MLPP precedence indication didn't shown on the conference window

CSCuo69658

DNS Unknown IPv6 Host xxxx is shown in Status Messages

CSCuo69759

only one call log for share line join conference call

CSCuo69840

Can't sync up call histories from cell phone after successfully paired

CSCuo70043

Phone could not add more participants in conference chain

CSCuo72112

The title of Recent page is wrong when locale is set to Arabic(ar_LB)

CSCuo72121

The content of CTL/ITL written on the line when locale is Greek(el_GR)

CSCuo72163

Status for Decline softkey does not consist

CSCuo72296

Phone didn't honor HTTP expire header

CSCuo72678

"PC Vlan" display error in Locale ar_EG

CSCuo72827

some noise can be heard during the swap between headset and speaker

CSCuo72954

Actional incoming call is not dismissed after DND-R is on

CSCuo74475

8861: phone crash if plug out USB3.0 HUB during a call

CSCuo74718

Remember me can't set to Yes after change the extension

CSCuo75197

On one phone, cannot delete or disconnect bluetooth device

CSCuo75227

Name and the date will be overlapped if HFU phone name long

CSCuo77225

8861 can't register to tftp via wifi when dns response is a invalid ip

CSCuo77424

The DTMF tone could not be heard clearly on BT headset when dialing

CSCuo77499

Disable "Logging Display" 88xx still print logs to phone console

CSCuo77660

Screenshot got 503 error

CSCuo77666

HFU call bubble disappears but audio is kept after CUCM restarts

CSCuo77670

Bad audio quality via headset connected to USB hub

CSCuo77812

PBAP cannot sync when disable then enable contacts import on cucm

CSCuo79553

8861 with wifi lost server connection during whole night conference

CSCuo79598

No expected EnergyWise alert if set level 0 from switch

CSCuo79658

dhcp off failed via wifi

CSCuo79673

Wrong ip address in CUCM

CSCuo79884

88xx phone should not support parameter "Call Pickup Toast Timer"

CSCuo80147

"Clear List" softkey doesn't work well

CSCuo80369

Failed to make call after EM login/logout many times.

CSCuo80570

Phone fail to upgrade from 10-2-2MN-21 to 10-2-2MN-23 (seen once)

CSCuo80732

[Thailand]The message of "Reset All Settings" beyond the border

CSCuo82084

Incoming call toast didn't disappear even if share line answer the call

CSCuo82111

8861 crashed after plugin/push out Jabra 6470 headset

CSCuo82199

8861 got UI stuck

CSCuo82286

Call Session is blank when reached the max remote hold call

CSCuo82365

Conference via wifi with psk may disconnect

CSCuo82402

Contact does not disappear after HFU is disconnected from BE

CSCuo82446

CLI:"show call detail line 1" return unexpected null

CSCuo82498

Phone reject CUCM SIP SUBSCRIBE message in call duration test

CSCuo82535

Toast queue is not cleared when whisper session has ended

CSCuo82546

BE can not sync contact from Samsung SIM card

CSCuo84744

Call is disconnected by pressing mute key on GN 2000 for several times

CSCuo84750

Mute status NOT sync to headset after switch audio path

CSCuo84763

PLK line is disappeared after HFU line status changed

CSCuo84769

HFU call ended up when press speak Hardkey in SIP line

CSCuo84772

BT and HFU line status can be changed during active HFU call

CSCuo84831

Conference via wifi with psk disconnect after session timeout

CSCuo84921

rapidly disconnect/connect HFU phone several times, audio path disappear

CSCuo85029

phone doesn't USB charge after plug/unplug iphone for several times

CSCuo85149

Auto Answer still work when HFU line connected

CSCuo85499

wireless phone is not able to obtain an IPv6 address when DAD enabled

CSCuo86592

No softkey displayed after modify the button template

CSCuo87108

8861 cannot make call due to network busy if 12Mbps disabled on WLC

CSCuo87177

Phone can not register after setting admin vlan

CSCuo87682

"Decline" soft key should be disabled in incoming call alert on
                                             SRST

CSCuo87718

HFU DN does not hidden after disable/enable from CUCM

CSCuo87758

wireless 8861 phone takes long time to register after associate
                                             to AP

CSCuo89344

it can't return to debug shell after executing settmask

CSCuo89379

88xx phones do not set hosts HTTP header properly

CSCuo89418

No audio for connected call if unplug aux line for ehook headset
                                             GN9330

CSCuo89460

No BE Wallpaper after installed devpack.

CSCuo89850

Service Dial:<number> not work on service URL

CSCuo89883

[PLAR]phone can't clear old config when apply sip dia rule

CSCuo89906

One PP phone may make call fail and unregister

CSCuo89992

Miss call count may confuse the user sometimes

CSCuo90088

Can not cancel out going call, session bubble can not
                                             disappear.

CSCuo90121

Max size of background image should be 1M

CSCuo90186

8861 crash -continuously initiate call, with CAC enabled

CSCuo90211

Phone may suddenly restarts

CSCuo90309

Info in Trust List Installed UI could not be displayed
                                             completely

CSCuo90322

UI freeze in stress call test via wifi

CSCuo90335

Phone ignore URI directory after %25 in the call session
                                             bubble

CSCuo90375

%25 should display as % in the BLF sd

CSCuo90406

Info is not align with the frame

CSCuo90422

DAD can't be disabled when IPv6 is manually set over Wi-Fi

CSCuo91754

Phone reset after 30 hours missed call + 48 hours idle

CSCuo91778

PBAP contacts item will flash quickly when press save

CSCuo91807

Network busy in stresscall test via wifi

CSCuo91834

two '100 half' items will be list below SW/PC port setup

CSCuo91857

Noise voice play after pressing the speaker or new call
                                             softkey

CSCuo91875

one 8861 wireless phone cannot boot after upgrading to
                                             10-2-1-16

CSCuo91983

BLF status not display correctly if blf sd include a special
                                             character

CSCuo92047

Rarely phone lost registration after idle for a while

CSCuo92062

PBAP sync icon will never disappear if disable contacts during
                                             sync

CSCuo92106

Plantronics headset has noise when phone Idle state.

CSCuo92160

Phone can't register to cucm after restart wlan

CSCuo92242

SIP crashed during WLAN duration test

CSCuo92371

Phone UI freeze after running basic call 5 hours

CSCuo92400

occasional reboot while switching RF channels

CSCuo92489

phone may stop scanning while off-hooking during channel
                                             switch

CSCuo92541

Unexpected simplified new call ui displayed if we press session
                                             key.

CSCuo92596

Failed to register to sub after disconnect net to pub during
                                             upgrade

CSCuo92639

sometimes cucm is not shown in phone information UI menu

CSCuo94496

Call history in BE aren't synced correctly after HFU
                                             connect/disconnect

CSCuo94536

Phone is frozen occasionally after changing Alt-TFTP address

CSCuo94552

Blank screen always shown on phone UI if cancel the HTTP
                                             connection

CSCup01256

Brightness level different on different phones

### Resolved
                           	 Caveats

There are no resolved caveats for this release.

## Cisco IP Phone
                        	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

## Documentation, Service Requests, and Additional Information

For information on obtaining documentation, submitting a service request, and gathering additional information, see the monthly What’s New in Cisco Product Documentation , which also lists all new and revised Cisco technical documentation, at:

http://www.cisco.com/c/en/us/td/docs/general/whatsnew/whatsnew.html

Subscribe to the What’s New in Cisco Product Documentation as a Really Simple Syndication (RSS) feed and set content to be delivered directly to your desktop using a reader application.
                           The RSS feeds are a free service and Cisco currently supports RSS Version 2.0.

| Cisco IP Phone | Protocol | Support Requirements |
|---|---|---|
| Cisco IP Phones 8841, 8851, and 8861 | SIP | Cisco Unified Communications Manager 8.5(1) and later Cisco Unified Communications Manager DST Olsen version D or later SRST 8.0 (IOS load 15.1(1)T) and above CME 10.0 (IOS load 15.3(3)M) and above through
                                       Fast-Track |

| Note | When an Android phone is connected, the user sees
                                                an alert pop-up asking whether Phone Book Access is allowed on that
                                                Android device. The user must select Allowed within 30 seconds in
                                                order to import the Android phone book to Cisco IP Phones 8851 and 8861. |
|---|---|

| Note | An iPhone can connect to two Cisco IP Phones 8851 and 8861 at the same
                                                time, but only one of the IP phones can access the iPhone phone book. |
|---|---|

|  | Cisco IP Phone 8851 | Cisco IP Phone 8861 |
|---|---|---|
| Smart phone charging | Yes (802.3af) | Yes (802.3af) |
| Tablet charging | No (no back USB port) | Yes (802.3at) |

| Note | When the Cisco IP Phone 8861 is using PoE with an 802.3af switch, the back USB port  can only work in slow-charging mode
                                          due to the limited power supply from 802.3af switch. |
|---|---|

| Attention | The network administrator must ensure that the AP configuration conforms to local regulatory laws. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Depending on your phone model, choose Cisco IP Phone 8800 Series . |
| Step 3 | Choose your phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 10.2(1) . |
| Step 6 | Select one of the following firmware files, click the Download or Add to cart button, and follow the prompts: cmterm-88xx-sip.10-2-1-16.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to
                                                         				  download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to
                                                         				  download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to
                                                         				  download the file. |
| Step 7 | Click the + next to the firmware file name in the
                                          			 Download Cart section to access additional information about this file. The
                                          			 hyperlink for the readme file is in the Additional Information section, which
                                          			 contains installation instructions for the corresponding firmware. |
| Step 8 | Follow the instructions in the readme file to install the
                                          			 firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to
                                                         				  download the file. |
|---|---|

| Step 1 | Go to the following URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco IP Phones 8800 Series . |
| Step 3 | Choose your phone type. |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 10.2(1) . |
| Step 6 | Download the relevant zip files. |
| Step 7 | Unzip the files. |
| Step 8 | Manually copy the unzipped files to the directory on the TFTP
                                          			 server. See Cisco Unified Communications Operating System Administration
                                             				Guide for information about how to manually copy the firmware files to
                                          			 the server. |

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
| CSCum62659 | Phone will DNS query (none).domain after reset |
| CSCum64968 | Display not be lit when On-Time comes with duration 00:00 |
| CSCum75600 | Wrong CUCM IP address in REFER before and after re-registration |
| CSCun19698 | Conference feature layer shall close while participant side park. |
| CSCun24183 | 8861 doesn't make active scan in roaming |
| CSCun29272 | 8861 may doesn't reply eap-request in roaming |
| CSCun30024 | Phone can answer a call from same phone |
| CSCun38032 | Accessary(CDROM) Added window keeps pop up forever |
| CSCun41637 | Wrong ReasonForOutOfService after IP address lost |
| CSCun47590 | softkey response time is long |
| CSCun62056 | Unable to complete conference; toast is wrong. |
| CSCun64117 | ethernet interface drops 2% packet periodically |
| CSCun72773 | Phone still shown as Application softkey set when register back to CCM |
| CSCun75414 | USB headset on 8851 phone volume not loud enough |
| CSCun77699 | CLI: show stream summary; should have only 1 active stream |
| CSCun78088 | softkeys for xml file is gray and xml file is not display |
| CSCun78115 | Line sequence in Ringtone menu not consistent with line button order |
| CSCun80759 | Incorrect date showed in "Status Messages" after changing phone's load |
| CSCun83523 | 8861 ipv6:phone restart several times if 1st CUCM refused the register |
| CSCun88493 | Service URL PLK doesn't work when failover to SRST |
| CSCun88943 | Toast window not popup in time when feature PLK pressed |
| CSCun93340 | iPad Mini USB charging caused Switches shut down the switch port of 8861 |
| CSCun93597 | CLI: Cannot get callReference from SessionItemModel |
| CSCun94444 | CLI:Remote call state return empty via cli when shared line during call. |
| CSCun96422 | Missing XML section in ModeInfo of Add Bluetooth Device window |
| CSCun98930 | CLI:"show line all" cannot show "All Calls" line in bigeasy |
| CSCun99543 | CLI: Call state show incorrectly via cli when phone play busy tone. |
| CSCuo02024 | Character can't be shown on the UI if use a white color background image |
| CSCuo04139 | UI response slow if configure multiple PFK BLF SD with same destination |
| CSCuo10939 | CLI: erase ctl, but ctl is still shown |
| CSCuo10969 | Connect/disconnect USB cause wrong last upgrade time on phone UI |
| CSCuo18535 | Crash when plug/unplug usb hub during call |
| CSCuo18546 | plugin/plugout USB hub, phone stuck. |
| CSCuo18779 | 8861 establish a call very slowly |
| CSCuo21617 | MWI LED off and icon disappear for seconds after power cycle |
| CSCuo23873 | post 'key:Key:KeyPad0 to Key:KeyPad9' can not work when display is off |
| CSCuo26551 | Earring should not be heard from headset when DND reject call on. |
| CSCuo26761 | No lock icon at the intercom received side sometimes |
| CSCuo31268 | setRingtone Failed if phone stay on ringtone list page |
| CSCuo31577 | Dial window flash twice when there's other app window behind |
| CSCuo33582 | Sometimes iphone disconnected automatically after it connected with BE |
| CSCuo34073 | No 'DHCP6 BOUND' status message for network statistics |
| CSCuo35638 | Pilot number overlap with the scroll bar if pilot long enough |
| CSCuo35834 | Missed call icon not display on related line if restart on one 8851 |
| CSCuo38121 | << softkey didn't greyed even no digit here |
| CSCuo38272 | Wrong message for dns down when phone accesses url with domain name |
| CSCuo40264 | iPhone does not automatical connected after paired successful |
| CSCuo40482 | share line key led is off after switch to another line in a short time |
| CSCuo40517 | The statistics for starMedia URI is only 1 direction |
| CSCuo42529 | Prompt IPC error in Jindo after running switch load scripts |
| CSCuo42726 | HFU signal display not accurate on the phone |
| CSCuo42755 | Phone can't exit from the error application |
| CSCuo43206 | Autopickup history is incorrectly logged |
| CSCuo45443 | Conference call history issues |
| CSCuo45740 | Phone may fails to accept some IPv6 multicast packets over Wi-Fi |
| CSCuo47255 | 8861 rebooted by itself when resuming a call. |
| CSCuo47261 | No focus when switching to missed call list view |
| CSCuo47265 | Phone still ring after all calls are ended |
| CSCuo47545 | Nav_select hardkey didn't work on xsi object |
| CSCuo47565 | phone doesn't show valid information when not configure the primary line |
| CSCuo47589 | No available line to play the message during VVM stress test |
| CSCuo48017 | Wong alert trust list message but no tftp server change |
| CSCuo50527 | change alt-tftp tftp 1 will blank tftp 2 |
| CSCuo50761 | IPv6 default router manual config cleared after switching to IPv4 |
| CSCuo50988 | Some noise heard on 8861 P2 during a call. |
| CSCuo51021 | UI of paired devices for bluetooth page is not friendly |
| CSCuo51154 | Phone shouldn't send RTCP package with even number during intercom call |
| CSCuo51278 | Bluetooth ICON disappeared. |
| CSCuo52950 | hourly archived logs are listed in disorder |
| CSCuo52962 | phone is stuck when alter tftp to HCUCM |
| CSCuo52966 | 8861 connect with another AP slowly when the current AP disable |
| CSCuo53035 | A blank screen shown if press back hardkey to exit a service |
| CSCuo53058 | 88xx Phone should remember password/username for HTTP service |
| CSCuo53169 | Missed call icon on 2nd line disappear after open HFU |
| CSCuo53422 | Audio disconnect after roaming |
| CSCuo53623 | Phone stuck once after pressing hfu on/off quickly |
| CSCuo53938 | Application windows can't regenerate after end the call |
| CSCuo55437 | The LineInfo for HFU is wrong |
| CSCuo55493 | phone plays old ringtone chirp instead of Delight |
| CSCuo55998 | Phone restart during EM stress test |
| CSCuo56015 | sometimes TFTP server IP cannot be cleared by UI after releasing DHCPv4 |
| CSCuo56065 | DN logged in history detail page is incorrect |
| CSCuo59730 | URI share line can not record call log |
| CSCuo59782 | New call window appear slower than white background when dial by speaker |
| CSCuo59994 | 8861 slow response to the network change |
| CSCuo61369 | Still highlight the previous item after disable setting access |
| CSCuo61370 | [IPMA]Assistant status window popup problem when hold/resume call |
| CSCuo61390 | Different display about conference in Recents |
| CSCuo61398 | delete softkey always disabled |
| CSCuo61740 | 8861 may register fail after wifi Session Timeout |
| CSCuo61741 | Press NAV_Select hardkey will create a new session |
| CSCuo61789 | UI slow in dozens of seconds after phone restart and configured with DNs |
| CSCuo61817 | Fail to connect to EM service during EM stress test |
| CSCuo61867 | Dial intra-cluster call from call history will fail |
| CSCuo61925 | arp cache not timeout on wlan interface as defined by dhcp option 35 |
| CSCuo62126 | unknown string ??? display on "Status Message" page |
| CSCuo62506 | Wrong history logged for anonymous@domain uri call |
| CSCuo62527 | application window still on the top when make a HFU call |
| CSCuo62589 | Phone can't enter the sub-window when pressing digit |
| CSCuo62598 | Bluetooth menu is still accessible when settings access is disable |
| CSCuo62648 | disable contacts access on BE, HFU line call history still exist. |
| CSCuo62944 | Analog headset can hear voice from Handset in activated call |
| CSCuo64323 | The order of PBAP contacts menu changes if get exit then enter in |
| CSCuo64598 | delete softkey always enabled in wireless sign in page |
| CSCuo64696 | no CUCM/TFTP/CAPF/TVS when checking CTL/ITL |
| CSCuo64830 | 8861 WLAN call duration test failed with "Network Busy" |
| CSCuo64846 | incorrect administrator password is kept for inputting |
| CSCuo64877 | No TCLAS for IPv6 signal or voice stream |
| CSCuo64886 | Speed Dial softkey enabled on CME |
| CSCuo65174 | PBAP contacts not refresh immediately if disable bluetooth contacts |
| CSCuo65477 | screen turn off to black and show cisco log again when booting |
| CSCuo67334 | White screen will last 1-2 second during phone bootup |
| CSCuo67572 | The speaker still light after the HFU call audio moved to cellphone |
| CSCuo67644 | The MLPP precedence indication didn't shown on the conference window |
| CSCuo69658 | DNS Unknown IPv6 Host xxxx is shown in Status Messages |
| CSCuo69759 | only one call log for share line join conference call |
| CSCuo69840 | Can't sync up call histories from cell phone after successfully paired |
| CSCuo70043 | Phone could not add more participants in conference chain |
| CSCuo72112 | The title of Recent page is wrong when locale is set to Arabic(ar_LB) |
| CSCuo72121 | The content of CTL/ITL written on the line when locale is Greek(el_GR) |
| CSCuo72163 | Status for Decline softkey does not consist |
| CSCuo72296 | Phone didn't honor HTTP expire header |
| CSCuo72678 | "PC Vlan" display error in Locale ar_EG |
| CSCuo72827 | some noise can be heard during the swap between headset and speaker |
| CSCuo72954 | Actional incoming call is not dismissed after DND-R is on |
| CSCuo74475 | 8861: phone crash if plug out USB3.0 HUB during a call |
| CSCuo74718 | Remember me can't set to Yes after change the extension |
| CSCuo75197 | On one phone, cannot delete or disconnect bluetooth device |
| CSCuo75227 | Name and the date will be overlapped if HFU phone name long |
| CSCuo77225 | 8861 can't register to tftp via wifi when dns response is a invalid ip |
| CSCuo77424 | The DTMF tone could not be heard clearly on BT headset when dialing |
| CSCuo77499 | Disable "Logging Display" 88xx still print logs to phone console |
| CSCuo77660 | Screenshot got 503 error |
| CSCuo77666 | HFU call bubble disappears but audio is kept after CUCM restarts |
| CSCuo77670 | Bad audio quality via headset connected to USB hub |
| CSCuo77812 | PBAP cannot sync when disable then enable contacts import on cucm |
| CSCuo79553 | 8861 with wifi lost server connection during whole night conference |
| CSCuo79598 | No expected EnergyWise alert if set level 0 from switch |
| CSCuo79658 | dhcp off failed via wifi |
| CSCuo79673 | Wrong ip address in CUCM |
| CSCuo79884 | 88xx phone should not support parameter "Call Pickup Toast Timer" |
| CSCuo80147 | "Clear List" softkey doesn't work well |
| CSCuo80369 | Failed to make call after EM login/logout many times. |
| CSCuo80570 | Phone fail to upgrade from 10-2-2MN-21 to 10-2-2MN-23 (seen once) |
| CSCuo80732 | [Thailand]The message of "Reset All Settings" beyond the border |
| CSCuo82084 | Incoming call toast didn't disappear even if share line answer the call |
| CSCuo82111 | 8861 crashed after plugin/push out Jabra 6470 headset |
| CSCuo82199 | 8861 got UI stuck |
| CSCuo82286 | Call Session is blank when reached the max remote hold call |
| CSCuo82365 | Conference via wifi with psk may disconnect |
| CSCuo82402 | Contact does not disappear after HFU is disconnected from BE |
| CSCuo82446 | CLI:"show call detail line 1" return unexpected null |
| CSCuo82498 | Phone reject CUCM SIP SUBSCRIBE message in call duration test |
| CSCuo82535 | Toast queue is not cleared when whisper session has ended |
| CSCuo82546 | BE can not sync contact from Samsung SIM card |
| CSCuo84744 | Call is disconnected by pressing mute key on GN 2000 for several times |
| CSCuo84750 | Mute status NOT sync to headset after switch audio path |
| CSCuo84763 | PLK line is disappeared after HFU line status changed |
| CSCuo84769 | HFU call ended up when press speak Hardkey in SIP line |
| CSCuo84772 | BT and HFU line status can be changed during active HFU call |
| CSCuo84831 | Conference via wifi with psk disconnect after session timeout |
| CSCuo84921 | rapidly disconnect/connect HFU phone several times, audio path disappear |
| CSCuo85029 | phone doesn't USB charge after plug/unplug iphone for several times |
| CSCuo85149 | Auto Answer still work when HFU line connected |
| CSCuo85499 | wireless phone is not able to obtain an IPv6 address when DAD enabled |
| CSCuo86592 | No softkey displayed after modify the button template |
| CSCuo87108 | 8861 cannot make call due to network busy if 12Mbps disabled on WLC |
| CSCuo87177 | Phone can not register after setting admin vlan |
| CSCuo87682 | "Decline" soft key should be disabled in incoming call alert on
                                             SRST |
| CSCuo87718 | HFU DN does not hidden after disable/enable from CUCM |
| CSCuo87758 | wireless 8861 phone takes long time to register after associate
                                             to AP |
| CSCuo89344 | it can't return to debug shell after executing settmask |
| CSCuo89379 | 88xx phones do not set hosts HTTP header properly |
| CSCuo89418 | No audio for connected call if unplug aux line for ehook headset
                                             GN9330 |
| CSCuo89460 | No BE Wallpaper after installed devpack. |
| CSCuo89850 | Service Dial:<number> not work on service URL |
| CSCuo89883 | [PLAR]phone can't clear old config when apply sip dia rule |
| CSCuo89906 | One PP phone may make call fail and unregister |
| CSCuo89992 | Miss call count may confuse the user sometimes |
| CSCuo90088 | Can not cancel out going call, session bubble can not
                                             disappear. |
| CSCuo90121 | Max size of background image should be 1M |
| CSCuo90186 | 8861 crash -continuously initiate call, with CAC enabled |
| CSCuo90211 | Phone may suddenly restarts |
| CSCuo90309 | Info in Trust List Installed UI could not be displayed
                                             completely |
| CSCuo90322 | UI freeze in stress call test via wifi |
| CSCuo90335 | Phone ignore URI directory after %25 in the call session
                                             bubble |
| CSCuo90375 | %25 should display as % in the BLF sd |
| CSCuo90406 | Info is not align with the frame |
| CSCuo90422 | DAD can't be disabled when IPv6 is manually set over Wi-Fi |
| CSCuo91754 | Phone reset after 30 hours missed call + 48 hours idle |
| CSCuo91778 | PBAP contacts item will flash quickly when press save |
| CSCuo91807 | Network busy in stresscall test via wifi |
| CSCuo91834 | two '100 half' items will be list below SW/PC port setup |
| CSCuo91857 | Noise voice play after pressing the speaker or new call
                                             softkey |
| CSCuo91875 | one 8861 wireless phone cannot boot after upgrading to
                                             10-2-1-16 |
| CSCuo91983 | BLF status not display correctly if blf sd include a special
                                             character |
| CSCuo92047 | Rarely phone lost registration after idle for a while |
| CSCuo92062 | PBAP sync icon will never disappear if disable contacts during
                                             sync |
| CSCuo92106 | Plantronics headset has noise when phone Idle state. |
| CSCuo92160 | Phone can't register to cucm after restart wlan |
| CSCuo92242 | SIP crashed during WLAN duration test |
| CSCuo92371 | Phone UI freeze after running basic call 5 hours |
| CSCuo92400 | occasional reboot while switching RF channels |
| CSCuo92489 | phone may stop scanning while off-hooking during channel
                                             switch |
| CSCuo92541 | Unexpected simplified new call ui displayed if we press session
                                             key. |
| CSCuo92596 | Failed to register to sub after disconnect net to pub during
                                             upgrade |
| CSCuo92639 | sometimes cucm is not shown in phone information UI menu |
| CSCuo94496 | Call history in BE aren't synced correctly after HFU
                                             connect/disconnect |
| CSCuo94536 | Phone is frozen occasionally after changing Alt-TFTP address |
| CSCuo94552 | Blank screen always shown on phone UI if cancel the HTTP
                                             connection |
| CSCup01256 | Brightness level different on different phones |