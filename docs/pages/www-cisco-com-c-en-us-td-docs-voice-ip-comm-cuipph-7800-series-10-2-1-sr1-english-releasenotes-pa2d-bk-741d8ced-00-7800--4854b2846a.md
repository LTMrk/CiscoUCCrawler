---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-7800-series-10-2-1-sr1-english-releasenotes-pa2d-bk-741d8ced-00-7800--4854b2846a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/7800-series/10-2-1-SR1/english/releasenotes/PA2D_BK_741D8CED_00_7800-series-rn-1021sr1/PA2D_BK_741D8CED_00_7800-series-rn-1021sr1_chapter_00.html
retrieved_at: 2026-08-25T12:12:09.891910+00:00
---

Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.2(1)SR1

# Cisco IP Phone 7821, 7841, and 7861 Release Notes for Firmware Release 10.2(1)SR1

Updated: May 22, 2018

Chapter: Cisco IP Phone 7821, 7841, and 7861 Release Notes for
Firmware Release 10.2(1)SR1

## Chapter: Cisco IP Phone 7821, 7841, and 7861 Release Notes for
Firmware Release 10.2(1)SR1

# Cisco IP Phone 7821, 7841, and 7861 Release Notes for
                     Firmware Release 10.2(1)SR1

## Introduction

These release notes
                              		support the Cisco IP Phones 7821, 7841, and 7861 running SIP Firmware Release
                              		10.2(1)SR1.

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

Cisco Unified
                                          				Communications Manager version 8.5(1) and later.

Cisco Unified
                                          				Communications Manager DST Olsen version D or later

## Related
                        	 Documentation

### Cisco IP Phone 7800 Series Documentation

Find documentation specific to your language, phone model, and call control system on the product support page for the Cisco IP Phone 7800 Series.

### Cisco Unified
                              				Communications Manager Documentation

See the Cisco Unified
                                       				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                                    				Communications Manager release on the product support page.

## New and Changed Features

This release contains no new or changed features.

## Installation

### Install Firmware Release on Cisco Unified Communications Manager

Before using the
                                 		  Cisco Unified IP Phone Firmware Release 10.2(1)SR1 with Cisco Unified
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
                                          			 Releases folder, choose 10.2(1)SR1 .

Step 6

Select the following firmware file, click the Download or Add to
                                             				cart button, and follow the prompts:

- cmterm-78xx.10-2-1-12SR1-4.cop.sgn

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
                                 		  following zip files are available to load the firmware.

- 78xx.10-2-1-12SR1-4.zip

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
                                          			 Releases folder, choose 10.2(1)SR1 .

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

### Open Caveats

The following table lists severity 1, 2, and 3 defects that are open for the Cisco IP Phone 7800 Series for Firmware Release
                                 10.3(1).

For more information about an individual defect, you can access the online record for the defect by accessing the Bug Search
                                 tool and entering the Identifier. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were open at the time this report
                                 was compiled. For an updated view of open defects, access Bug Toolkit as described in Access Cisco Bug Search .

Identifier

Headline

CSCur77888

phone could not register to cucm if change fips configuration

CSCus51283

7811: phone unregister during Codenomicon ICMPV6 testing

CSCuu03128

7811 softkey disappear when config undefined soft key

CSCuu03127

7811 phone display abnormal in ipv4 setup interface

CSCuu12357

78xx: can not play preset ringtone

CSCuu14236

No DN appeare on 7811 when the phone calls another one

CSCus32998

speed dial failed via pick up the handset if speaker disabled

CSCus34815

No Resume SK in ROH when use headset if speaker disabled

CSCus41425

phone ui shows wrong new voice mail info for light only

CSCus42707

JANUARY 2015 OpenSSL Vulnerabilities

CSCus72195

No load version could be found from CUCM on the 78xx CE phone

CSCus76499

Sometimes phone UI will be showed blank.

CSCus76500

UE display wrong when the shareline phone ringing

CSCus84738

The phone UI showed error and toast Extension mobility Unavailable

CSCus92469

Call info not shown on shared-line phone

CSCut15070

align 78xx CE related phrases with BE phone

CSCut29161

cipcfg shows error for 78xx

CSCut36890

New call trigged incorrectly from call history and couldn't be ended

CSCut46200

MARCH 2015 OpenSSL Vulnerabilities

CSCut47560

78xx: CE login process abnormal when password wrong and press app key

CSCut57209

Recording error when "Media Termination Point Required" is enabled

CSCut62446

78xx: softkey missing in CE mode with reset all (once)

CSCut66203

the shared line key's status is incorrect

CSCut76463

messages not same when maximum call reach under shared line

CSCut76502

phone UE become chaos after press setting or directory keys

CSCut79172

VCS interop with SL CE - phone oneway audio after hold/resume

CSCut79209

There's no console logs from the phone web

CSCut83897

Edge gateway crash after execute 'pkill -9 java' when download rootfs

CSCut86500

Phone cannot update network config upon user change from UI

CSCut87780

88xx IP phones attempt to connect to TFTP after SRST incorrectly

CSCut94385

phone occurs java core dump ("appmgr MQThread")

CSCuu03731

Web/SSH not accessible on 7841 on-prem phone; didn't upgrade to -10

CSCuu05348

the development model is different from load info

CSCuu05381

7811 upgrade failed from 10-3-1-8 to -10 caused by the lack of memory

CSCuu08052

CE: can't register with cucm after enable alt tftp

CSCuu10274

UI stuck after press transfer softkey

CSCuu10295

Several on-premise 78xx phones failed to upgrade

CSCuu12072

the back key does not work after saving the ringtone

CSCuu14370

78xx: dhcp release message does not have server id option

CSCuu14765

78xx Phones: Content-Length Header Not Sent in 200 OK Indicating Failure

CSCus46014

JANUARY 2015 OpenSSL Vulnerabilities

CSCus54846

phone can't display alert info when reach 96 calls

CSCus65461

Toast doesn't need popup when transfer to Dpark

CSCus76474

There is a timer displayed after pressing the linekey

CSCus76472

Missed call icon display wrong

CSCus76487

Conference test linekey can not answer the call (just find one time)

CSCus76490

Phone have speaker tone sometime when press the hook switch fast.

CSCus80361

Conference display abnormal

CSCus86984

Phone A doesnt display the dial out number on UE

CSCus88440

78xx: Phone play noise after reset phone on cucm occasionally

CSCut15049

Duration test: redial failed in about 12~24h

CSCut22400

the characters cannot scroll to display after the locale is changed

CSCut26360

blackbar on 7841 phone screen

CSCut28341

call history item records wrong number

CSCut33650

The directed call park infor will be shown incorrect on 7841 mode.

CSCut39749

remove recents when phone cbarge

CSCut41913

The phone load version shows wrong in boot log.

CSCut42219

phone caller id has problem when cbarge

CSCut44077

Conference title sometimes disappear when Cbarge call

CSCut46217

MARCH 2015 OpenSSL Vulnerabilities

CSCut68712

sometimes phone ui dn disappear

CSCut69273

Phone make some issue when having three incoming call.

CSCut78736

phone foucs error when offhook in sharelne

CSCut78744

new call softkey doesn't work when remote in use

CSCut96962

UI display blank DN when end the call from line 2

CSCus80364

The overflow of characters cant be use

CSCus86981

Call back and FWD test fail

CSCus89519

78xx Nothing is displayed on phone when a call arrives.

CSCut13591

7811 softkey error when in remote-in-use state

CSCut14947

78xx: display "unprovisioned" when phone restart

CSCut14960

Session list update slowly when conference

CSCut15605

One 78xx phone always fail to submit PRT reprot

CSCut64844

CE: A 25-min-long PSTN/Jabber call became oneway audio after hold/resume

### Resolved Caveats

The following table lists severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series for Firmware Release
                                 10.3(1).

For more information about an individual defect, you can access the online record for the defect by accessing the Bug Search
                                 tool and entering the Identifier. You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the table reflects a snapshot of the defects that were resolved at the time this
                                 report was compiled. For an updated view of resolved defects, access Bug Toolkit as described in Access Cisco Bug Search .

Identifier

Headline

CSCup22421

Calls answered on 78xx phones are placed on hold automatically

CSCuq02713

Phones Should Enable the MAB on uplink Switch

CSCuq46372

MAC addr bypass authentication failed in DOT1X

CSCuq58308

7841 phone audio on speaker muted when both parties talk

CSCuq61332

78xx shows XML error when open App menu and ext services unavailable

CSCuq66793

CP-78xx doesn't display "Service interruption" in SRST after hung up

CSCuq69025

78xx phones do not use Secondary TVS for EM after Failover

CSCuq72739

7841 cannot handle internal URL in custom XML/external services

CSCuq73819

78XX phone diskspace(var/volatile) Increases while setting ringtone

CSCuq82601

XML Parse Error Issue on both Corporate and Personal Directory on 78XX

CSCuq89138

7861 can't display missed call correctly by pushing "missed" softkey

CSCuq92866

78XX are unable to handle larger ptime value in SDP

CSCuq96598

XML Error on 78XX phones

CSCur16953

"Can't set PFK of ""Missed Calls""."

CSCur25099

78xx Hebrew locale issues with 10-2-1 firmware

CSCur35134

Jabber Video does not work with Cisco 78XX Phones

CSCur35773

7841 failing to create conference from CTI application

CSCur39715

CP 7821/7841 may become unusable when re-registering multiple times

CSCur41631

Direct call park button is not enabled after failback from SRST

CSCur45352

CP78XX cancel calls because of no enough codec resource

CSCur49750

78XX phone not mounting mnt/flash2 even after upgrading to 10-2-1-12ES1

CSCur52030

Undefined softkey don't take effect on 78XX Phone

CSCur54113

cann't make new call with speaker/headset/handset

CSCur57934

7800 phones stop playing multicast audio (informacast)

CSCur59644

When using CiscoIPPhoneInput, the submit button does not always appear

CSCur60763

Caller ID not displayed correctly on 78XX when Arabic locale is used

CSCur60954

78xx phone should hide call history when history urls are disabled

CSCur61721

7800 Series handset doesn't answer second line when the first is on hold

CSCur64844

unable to off hook after receiving a call in shared line simultaneously

CSCur66884

Connected another call after selecting "Hold" with 3rd party application

CSCur75727

phone freezed completedly including softkey and hardkey

CSCur78719

78xx phones not showing Call history and EM service

CSCur90234

78xx Label for Services URL not showing if assigned to button 4

CSCur98445

Not refresh configure file after network recover

CSCus03197

Call history selection highlight is incorrect

CSCus07000

There are serious kernel "error" on the console log

CSCus10285

CP7861/41/21 background noise on G729 calls

CSCus18070

7841 will not register back to CUCM cluster after SRST failover

CSCus18360

One way audio on inbound call

CSCus20047

78XX phones sending IP instead of hostname while accessing phone service

CSCus20746

Commit IP Phone 78XX 10.2.(1) feature safe/size safe support in CUCM DB

CSCus25031

78xx phone breaks audio in between call when used with jabber (CAST)

CSCus33522

SP 78XX POODLE vulnerability evaluation - CVE-2014-3566

CSCus33653

78XX phone not sending Call statistics in the 200OK.

CSCus42190

78xx phone cannot play preview of Non-Wideband Ringtone (.raw)

CSCus49612

phone should keep consistent action when conference from line

CSCus52642

press hold/resume softkey in a shorter time, phone responsed slowly

CSCus52824

Phone UI changed slowly if cBarge the call

CSCus54642

7821 cannot complete agent greeting conference with BIB recording

CSCus57373

8x to 9x upgrades broken due to incorrect reference of phone XML rule

CSCus58355

answer softkey shows for local hold call.

CSCus59083

7821 phone crashes intermittently when recording is enabled

CSCus64017

phone can not register to CUCM after add second shared line back

CSCus67926

"undefined" softkey come out when remote in use

CSCus70130

7811 phone could not make/answer call any more

CSCus70263

Evaluation of CVE-2015-0235 'GHOST' vulnerability

CSCus72226

78xx phone intermittently fail to clear CE info after reset all

CSCus73097

7861 phone BLF out of sync issue on Shared lines - NPE issue

CSCus74260

CP-7861 Offhook and press line key in a short time should answer a call

CSCus74598

78xx:softkeys error after phone failover/fallback

CSCus75230

7800 series phones cannot handle certificates greater than 2048 bytes

CSCus76475

78XX IP Phone stops writing logs and will eventually freeze or reboot

CSCus81661

No BLF audio in 78xx phones after firmware upgrade

CSCus81800

78xx: phone reboots during Fuzzing.sh udp attack

CSCus84647

7841 CE failed to send PRT

CSCus84727

The phone's UE diaplays unnormal when dial message waiting on number

CSCus84741

Two share line phone dial each other,header display error

CSCus86094

"Applications" key is disabled when phone is registered with CME

CSCus86225

78xx: prt process should align with 88xx

CSCus88504

78xx: phone can't set Call Fwd All from call history

CSCus88521

78xx: Phone don't play du-du tone after press Fwd All sk in the off-hook

CSCut13256

Softkey miss when cancel an on-hook dialing call

CSCut13357

78xx: CE login window header shows "???" when login

CSCut13545

7821 phones | https web access doesnt work

CSCut13591

7811 softkey error when in remote-in-use state

CSCut14947

78xx: display "unprovisioned" when phone restart

CSCut14964

All softkey disappear when phone is "remote in use" status

CSCut15095

Duration test: upgrade_downgrade failed in about 12~24h

CSCut15593

Phone UI update error when called the third incoming call

CSCut15614

Softkey and phrase error in PRT

CSCut15714

Phone can't return to PRT initial screen if exit menu in PRT process

CSCut15988

No error display if http service not accessible

CSCut16069

Conference window with Recents softkey problem

CSCut18015

the call forward off softkey will disappear after running the script

CSCut31158

Locale: a tftp change alert string is hard coded

CSCut32858

78xx series phones cannot handle certificates greater than 2048 bytes

CSCut50230

Actionable toast will not show when failover to SRST

CSCut52345

7811: Phone UI display error after stop recording manually

CSCut54724

E-hook not work

CSCut54790

the softkey will become chaos after running the shared line script

CSCut54800

CP-7861 Media Server crash on 10.3.1-4

CSCut57520

Phone should use the same softkey template when failover to SRST

CSCut62130

the remote-in-use phones occur ms crash

CSCut62498

(Crash in sip rccapp during IPMA stress testing(BE-video)--it may fix the CSCut70796:remote in used phone occurs java core
                                             dump aftrer running script

CSCut64286

7800 phone should display error on locations bandwidth limitation

CSCut64393

ui update problem when conference from call list

CSCut64665

"Decline" softkey should not show when failover to SRST

CSCut65621

No way to return to CE sign-in screen on 78xx phones without a reboot

CSCut65636

No PRT button available for collecting logs on 78xx via collab edge

CSCut66411

Phone shows 2 cursors for the 2nd call

CSCut77203

78xx IP phones attempt to connect to TFTP after SRST incorrectly

CSCut79183

78xx CE phone got stuck and could not boot up after upgrade and reboot

CSCut83929

7861 phone CPU usage is nearly 100%

CSCut86600

transfer/conference hardkey doesn't work in detail page

CSCut88230

phone should not show an unexpected toast using Japan locale

CSCut92250

phone restart after running the script since MS watchdog timeout

CSCut92476

phone will reboot and occur out of memory

CSCut92671

UI stuck after press transfer and conference button in details window

CSCut92793

Phone should use prime line to dial out a call

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

## Cisco IP Phone Documentation Updates on Cisco Unified Communications Manager

The Cisco Unified Communications Manager Self Care Portal (Release 10.0 and later) and User Options web pages (Release 9.1
                              and earlier) provide  links to the IP Phone user guides in PDF format. These user guides are stored on the Cisco Unified Communications
                              Manager and are up to date when the Cisco Unified Communications Manager release is first made available to customers.

After a Cisco Unified Communications Manager release, subsequent updates to the user guides appear only on the Cisco website.
                              The phone firmware release notes contain the applicable documentation URLs. In the web pages, updated documents display "Updated" beside the document link.

The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer
                                          do not update the English user guides on the Cisco Unified Communications Manager.

You and your users should check the Cisco website for updated user guides and download the PDF files. You can also make the
                              files available to your users on your company website.

Tip

You may want to bookmark the web pages for the phone models that are deployed in your company and send these URLs to your
                                          users.

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
                                          				Phones 7821, 7841, and 7861 | SIP | Cisco Unified
                                          				Communications Manager version 8.5(1) and later. Cisco Unified
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
                                          			 Releases folder, choose 10.2(1)SR1 . |
| Step 6 | Select the following firmware file, click the Download or Add to
                                             				cart button, and follow the prompts: cmterm-78xx.10-2-1-12SR1-4.cop.sgn Note If you added
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
                                          			 Releases folder, choose 10.2(1)SR1 . |
| Step 6 | Download the
                                          			 relevant zip files. |
| Step 7 | Unzip the
                                          			 files. |
| Step 8 | Manually copy
                                          			 the unzipped files to the directory on the TFTP server. See Cisco
                                             				Unified Communications Operating System Administration Guide for
                                          			 information about how to manually copy the firmware files to the server. |

| Step 1 | To access Cisco Bug Search, go to: https://bst.cloudapps.cisco.com/bugsearch |
|---|---|
| Step 2 | Log in with your
                                          			 Cisco.com user ID and password. |
| Step 3 | To look for
                                          			 information about a specific problem, enter the bug ID number in the Search for
                                          			 field, then press Enter . |

| Identifier | Headline |
|---|---|
| CSCur77888 | phone could not register to cucm if change fips configuration |
| CSCus51283 | 7811: phone unregister during Codenomicon ICMPV6 testing |
| CSCuu03128 | 7811 softkey disappear when config undefined soft key |
| CSCuu03127 | 7811 phone display abnormal in ipv4 setup interface |
| CSCuu12357 | 78xx: can not play preset ringtone |
| CSCuu14236 | No DN appeare on 7811 when the phone calls another one |
| CSCus32998 | speed dial failed via pick up the handset if speaker disabled |
| CSCus34815 | No Resume SK in ROH when use headset if speaker disabled |
| CSCus41425 | phone ui shows wrong new voice mail info for light only |
| CSCus42707 | JANUARY 2015 OpenSSL Vulnerabilities |
| CSCus72195 | No load version could be found from CUCM on the 78xx CE phone |
| CSCus76499 | Sometimes phone UI will be showed blank. |
| CSCus76500 | UE display wrong when the shareline phone ringing |
| CSCus84738 | The phone UI showed error and toast Extension mobility Unavailable |
| CSCus92469 | Call info not shown on shared-line phone |
| CSCut15070 | align 78xx CE related phrases with BE phone |
| CSCut29161 | cipcfg shows error for 78xx |
| CSCut36890 | New call trigged incorrectly from call history and couldn't be ended |
| CSCut46200 | MARCH 2015 OpenSSL Vulnerabilities |
| CSCut47560 | 78xx: CE login process abnormal when password wrong and press app key |
| CSCut57209 | Recording error when "Media Termination Point Required" is enabled |
| CSCut62446 | 78xx: softkey missing in CE mode with reset all (once) |
| CSCut66203 | the shared line key's status is incorrect |
| CSCut76463 | messages not same when maximum call reach under shared line |
| CSCut76502 | phone UE become chaos after press setting or directory keys |
| CSCut79172 | VCS interop with SL CE - phone oneway audio after hold/resume |
| CSCut79209 | There's no console logs from the phone web |
| CSCut83897 | Edge gateway crash after execute 'pkill -9 java' when download rootfs |
| CSCut86500 | Phone cannot update network config upon user change from UI |
| CSCut87780 | 88xx IP phones attempt to connect to TFTP after SRST incorrectly |
| CSCut94385 | phone occurs java core dump ("appmgr MQThread") |
| CSCuu03731 | Web/SSH not accessible on 7841 on-prem phone; didn't upgrade to -10 |
| CSCuu05348 | the development model is different from load info |
| CSCuu05381 | 7811 upgrade failed from 10-3-1-8 to -10 caused by the lack of memory |
| CSCuu08052 | CE: can't register with cucm after enable alt tftp |
| CSCuu10274 | UI stuck after press transfer softkey |
| CSCuu10295 | Several on-premise 78xx phones failed to upgrade |
| CSCuu12072 | the back key does not work after saving the ringtone |
| CSCuu14370 | 78xx: dhcp release message does not have server id option |
| CSCuu14765 | 78xx Phones: Content-Length Header Not Sent in 200 OK Indicating Failure |
| CSCus46014 | JANUARY 2015 OpenSSL Vulnerabilities |
| CSCus54846 | phone can't display alert info when reach 96 calls |
| CSCus65461 | Toast doesn't need popup when transfer to Dpark |
| CSCus76474 | There is a timer displayed after pressing the linekey |
| CSCus76472 | Missed call icon display wrong |
| CSCus76487 | Conference test linekey can not answer the call (just find one time) |
| CSCus76490 | Phone have speaker tone sometime when press the hook switch fast. |
| CSCus80361 | Conference display abnormal |
| CSCus86984 | Phone A doesnt display the dial out number on UE |
| CSCus88440 | 78xx: Phone play noise after reset phone on cucm occasionally |
| CSCut15049 | Duration test: redial failed in about 12~24h |
| CSCut22400 | the characters cannot scroll to display after the locale is changed |
| CSCut26360 | blackbar on 7841 phone screen |
| CSCut28341 | call history item records wrong number |
| CSCut33650 | The directed call park infor will be shown incorrect on 7841 mode. |
| CSCut39749 | remove recents when phone cbarge |
| CSCut41913 | The phone load version shows wrong in boot log. |
| CSCut42219 | phone caller id has problem when cbarge |
| CSCut44077 | Conference title sometimes disappear when Cbarge call |
| CSCut46217 | MARCH 2015 OpenSSL Vulnerabilities |
| CSCut68712 | sometimes phone ui dn disappear |
| CSCut69273 | Phone make some issue when having three incoming call. |
| CSCut78736 | phone foucs error when offhook in sharelne |
| CSCut78744 | new call softkey doesn't work when remote in use |
| CSCut96962 | UI display blank DN when end the call from line 2 |
| CSCus80364 | The overflow of characters cant be use |
| CSCus86981 | Call back and FWD test fail |
| CSCus89519 | 78xx Nothing is displayed on phone when a call arrives. |
| CSCut13591 | 7811 softkey error when in remote-in-use state |
| CSCut14947 | 78xx: display "unprovisioned" when phone restart |
| CSCut14960 | Session list update slowly when conference |
| CSCut15605 | One 78xx phone always fail to submit PRT reprot |
| CSCut64844 | CE: A 25-min-long PSTN/Jabber call became oneway audio after hold/resume |

| Identifier | Headline |
|---|---|
| CSCup22421 | Calls answered on 78xx phones are placed on hold automatically |
| CSCuq02713 | Phones Should Enable the MAB on uplink Switch |
| CSCuq46372 | MAC addr bypass authentication failed in DOT1X |
| CSCuq58308 | 7841 phone audio on speaker muted when both parties talk |
| CSCuq61332 | 78xx shows XML error when open App menu and ext services unavailable |
| CSCuq66793 | CP-78xx doesn't display "Service interruption" in SRST after hung up |
| CSCuq69025 | 78xx phones do not use Secondary TVS for EM after Failover |
| CSCuq72739 | 7841 cannot handle internal URL in custom XML/external services |
| CSCuq73819 | 78XX phone diskspace(var/volatile) Increases while setting ringtone |
| CSCuq82601 | XML Parse Error Issue on both Corporate and Personal Directory on 78XX |
| CSCuq89138 | 7861 can't display missed call correctly by pushing "missed" softkey |
| CSCuq92866 | 78XX are unable to handle larger ptime value in SDP |
| CSCuq96598 | XML Error on 78XX phones |
| CSCur16953 | "Can't set PFK of ""Missed Calls""." |
| CSCur25099 | 78xx Hebrew locale issues with 10-2-1 firmware |
| CSCur35134 | Jabber Video does not work with Cisco 78XX Phones |
| CSCur35773 | 7841 failing to create conference from CTI application |
| CSCur39715 | CP 7821/7841 may become unusable when re-registering multiple times |
| CSCur41631 | Direct call park button is not enabled after failback from SRST |
| CSCur45352 | CP78XX cancel calls because of no enough codec resource |
| CSCur49750 | 78XX phone not mounting mnt/flash2 even after upgrading to 10-2-1-12ES1 |
| CSCur52030 | Undefined softkey don't take effect on 78XX Phone |
| CSCur54113 | cann't make new call with speaker/headset/handset |
| CSCur57934 | 7800 phones stop playing multicast audio (informacast) |
| CSCur59644 | When using CiscoIPPhoneInput, the submit button does not always appear |
| CSCur60763 | Caller ID not displayed correctly on 78XX when Arabic locale is used |
| CSCur60954 | 78xx phone should hide call history when history urls are disabled |
| CSCur61721 | 7800 Series handset doesn't answer second line when the first is on hold |
| CSCur64844 | unable to off hook after receiving a call in shared line simultaneously |
| CSCur66884 | Connected another call after selecting "Hold" with 3rd party application |
| CSCur75727 | phone freezed completedly including softkey and hardkey |
| CSCur78719 | 78xx phones not showing Call history and EM service |
| CSCur90234 | 78xx Label for Services URL not showing if assigned to button 4 |
| CSCur98445 | Not refresh configure file after network recover |
| CSCus03197 | Call history selection highlight is incorrect |
| CSCus07000 | There are serious kernel "error" on the console log |
| CSCus10285 | CP7861/41/21 background noise on G729 calls |
| CSCus18070 | 7841 will not register back to CUCM cluster after SRST failover |
| CSCus18360 | One way audio on inbound call |
| CSCus20047 | 78XX phones sending IP instead of hostname while accessing phone service |
| CSCus20746 | Commit IP Phone 78XX 10.2.(1) feature safe/size safe support in CUCM DB |
| CSCus25031 | 78xx phone breaks audio in between call when used with jabber (CAST) |
| CSCus33522 | SP 78XX POODLE vulnerability evaluation - CVE-2014-3566 |
| CSCus33653 | 78XX phone not sending Call statistics in the 200OK. |
| CSCus42190 | 78xx phone cannot play preview of Non-Wideband Ringtone (.raw) |
| CSCus49612 | phone should keep consistent action when conference from line |
| CSCus52642 | press hold/resume softkey in a shorter time, phone responsed slowly |
| CSCus52824 | Phone UI changed slowly if cBarge the call |
| CSCus54642 | 7821 cannot complete agent greeting conference with BIB recording |
| CSCus57373 | 8x to 9x upgrades broken due to incorrect reference of phone XML rule |
| CSCus58355 | answer softkey shows for local hold call. |
| CSCus59083 | 7821 phone crashes intermittently when recording is enabled |
| CSCus64017 | phone can not register to CUCM after add second shared line back |
| CSCus67926 | "undefined" softkey come out when remote in use |
| CSCus70130 | 7811 phone could not make/answer call any more |
| CSCus70263 | Evaluation of CVE-2015-0235 'GHOST' vulnerability |
| CSCus72226 | 78xx phone intermittently fail to clear CE info after reset all |
| CSCus73097 | 7861 phone BLF out of sync issue on Shared lines - NPE issue |
| CSCus74260 | CP-7861 Offhook and press line key in a short time should answer a call |
| CSCus74598 | 78xx:softkeys error after phone failover/fallback |
| CSCus75230 | 7800 series phones cannot handle certificates greater than 2048 bytes |
| CSCus76475 | 78XX IP Phone stops writing logs and will eventually freeze or reboot |
| CSCus81661 | No BLF audio in 78xx phones after firmware upgrade |
| CSCus81800 | 78xx: phone reboots during Fuzzing.sh udp attack |
| CSCus84647 | 7841 CE failed to send PRT |
| CSCus84727 | The phone's UE diaplays unnormal when dial message waiting on number |
| CSCus84741 | Two share line phone dial each other,header display error |
| CSCus86094 | "Applications" key is disabled when phone is registered with CME |
| CSCus86225 | 78xx: prt process should align with 88xx |
| CSCus88504 | 78xx: phone can't set Call Fwd All from call history |
| CSCus88521 | 78xx: Phone don't play du-du tone after press Fwd All sk in the off-hook |
| CSCut13256 | Softkey miss when cancel an on-hook dialing call |
| CSCut13357 | 78xx: CE login window header shows "???" when login |
| CSCut13545 | 7821 phones \| https web access doesnt work |
| CSCut13591 | 7811 softkey error when in remote-in-use state |
| CSCut14947 | 78xx: display "unprovisioned" when phone restart |
| CSCut14964 | All softkey disappear when phone is "remote in use" status |
| CSCut15095 | Duration test: upgrade_downgrade failed in about 12~24h |
| CSCut15593 | Phone UI update error when called the third incoming call |
| CSCut15614 | Softkey and phrase error in PRT |
| CSCut15714 | Phone can't return to PRT initial screen if exit menu in PRT process |
| CSCut15988 | No error display if http service not accessible |
| CSCut16069 | Conference window with Recents softkey problem |
| CSCut18015 | the call forward off softkey will disappear after running the script |
| CSCut31158 | Locale: a tftp change alert string is hard coded |
| CSCut32858 | 78xx series phones cannot handle certificates greater than 2048 bytes |
| CSCut50230 | Actionable toast will not show when failover to SRST |
| CSCut52345 | 7811: Phone UI display error after stop recording manually |
| CSCut54724 | E-hook not work |
| CSCut54790 | the softkey will become chaos after running the shared line script |
| CSCut54800 | CP-7861 Media Server crash on 10.3.1-4 |
| CSCut57520 | Phone should use the same softkey template when failover to SRST |
| CSCut62130 | the remote-in-use phones occur ms crash |
| CSCut62498 | (Crash in sip rccapp during IPMA stress testing(BE-video)--it may fix the CSCut70796:remote in used phone occurs java core
                                             dump aftrer running script |
| CSCut64286 | 7800 phone should display error on locations bandwidth limitation |
| CSCut64393 | ui update problem when conference from call list |
| CSCut64665 | "Decline" softkey should not show when failover to SRST |
| CSCut65621 | No way to return to CE sign-in screen on 78xx phones without a reboot |
| CSCut65636 | No PRT button available for collecting logs on 78xx via collab edge |
| CSCut66411 | Phone shows 2 cursors for the 2nd call |
| CSCut77203 | 78xx IP phones attempt to connect to TFTP after SRST incorrectly |
| CSCut79183 | 78xx CE phone got stuck and could not boot up after upgrade and reboot |
| CSCut83929 | 7861 phone CPU usage is nearly 100% |
| CSCut86600 | transfer/conference hardkey doesn't work in detail page |
| CSCut88230 | phone should not show an unexpected toast using Japan locale |
| CSCut92250 | phone restart after running the script since MS watchdog timeout |
| CSCut92476 | phone will reboot and occur out of memory |
| CSCut92671 | UI stuck after press transfer and conference button in details window |
| CSCut92793 | Phone should use prime line to dial out a call |

| Note | The latest
                                          			 Locale Installer may not be immediately available; continue to check the
                                          			 website for updates. |
|---|---|

| Note | The Cisco Unified Communications Manager Device Packages and the Unified Communications Manager Endpoints Locale Installer
                                          do not update the English user guides on the Cisco Unified Communications Manager. |
|---|---|

| Tip | You may want to bookmark the web pages for the phone models that are deployed in your company and send these URLs to your
                                          users. |
|---|---|