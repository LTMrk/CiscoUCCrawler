---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8821-firmware-11-0-6-w881-b-wireless-8821-rns-110006-html-ef50834bf5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8821/firmware/11-0-6/w881_b_wireless-8821-rns-110006.html
retrieved_at: 2026-08-21T13:34:48.452516+00:00
---

Cisco Wireless IP Phone 8821 and 8821-EX Release Notes for Firmware Release 11.0(6)

# Cisco Wireless IP Phone 8821 and 8821-EX Release Notes for Firmware Release 11.0(6)

### Download Options

Updated: September 18, 2020

First Published: September 24, 2020

# Cisco Wireless IP Phone 8821 and 8821-EX Release Notes for Firmware Release 11.0(6)

These release notes support the Cisco Wireless IP Phone 8821 and 8821-EX Firmware Release
               			11.0(6).

The following table describes the systems and versions that the phone requires.

Call Control System

Minimum Version

Recommended Versions

Cisco Unified Communications Manager

9.1(2)

10.5(2), 11.0(1), 11.5(1), 12.0(1), 12.5(1), and later

Cisco Unified Communications Manager Express

10.5 through Fast Track

11.7 and later

Cisco Unified Survivable Remote Site Telephony

10.5

11.7 and later

Access Point Hardware

Minimum Version

Recommended Versions

Cisco AireOS Wireless LAN Controller

8.0.121.0

8.0.152.0, 8.2.170.0, 8.3.150.0, 8.5.161.0, 8.8.130.0, 8.10.130.0

Cisco Catalyst IOS XE Wireless LAN Controller

16.12.1s

16.12.3

Cisco Mobility Express

8.3.143.0

8.3.150.0, 8.5.161.0, 8.8.130.0, 8.10.130.0

Cisco IOS Access Points (Autonomous)

12.4(21a)JY

12.4(25d)JA1, 15.2(4)JB6, 15.3(3)JD17, 15.3(3)JF12i, 15.3(3)JPJ4

Cisco Meraki

MR 25.9, MX 13.33

MR 26.8.1, MX14.42

## New and Changed
               	 Features

The following sections describe the features that are new or have
                  		changed in this release.

Some features may require the installation of a Cisco Unified Communications Manager Device Package. Failure to install the
                              Device Package before the phone firmware upgrade may render the phones unusable.

### Cisco Wireless IP Phone 8821 Silicone Case

You can purchase the Cisco Wireless IP Phone 8821 Silicone Case . The case fits over either wireless phone model. It has these benefits:

Hypoallergenic

Antimicrobial

Resistant to wear from 15% alcohol, 75% alcohol, 2.5% hydrogen peroxide, mineral oil, soap, water, bleach, and dish soap.

Use the lowest-strength cleaning agent to prolong the life and look of the case.

Reduces damage when the phone is dropped

Better phone coverage because it covers more of the phone than the other cases.

The case doesn't need to be removed to charge the battery in the desktop charger or multicharger. You remove the cup in the
                        charger to place the phone and case into the charger.

#### Where to Find More Information

Cisco Wireless IP Phone 8821 and 8821-EX Accessory Guide

### Features Available
                  	 with the Firmware Release

The following sections describe the features available with the Firmware
                     		Release.

#### Increase Maximum Extract Password Length for Certificates

Manually-installed user certificates can have a maximum extract password of 16 characters instead of the previous 12 characters.

##### Where to Find More Information

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide

#### Location Reporting

The phones now report their location to Cisco Unified Communications Manager (Unified CM). Unified CM stores this information.

The wireless phones report their location when they first register. They report their location when the location changes;
                           for example, when walking around the building. The wireless phones also report their location every 24 hours if they are not
                           moving.

There is no administrator or user impact to this feature.

This feature requires Cisco Unified Communication Manager Release 11.0 or later. This
                           feature also requires an updated locale file.

##### Where to Find More Information

Cisco Unified Communications Manager documentation

### Features Available with the Latest Cisco Unified
                     				Communications Manager Device Package

The following sections describe features in the release which require the new firmware and the latest Cisco Unified
                        				Communications Manager device package. The applicable device packages are released after the firmware release.

For information about the Cisco devices and the required Cisco Unified
                        				Communications Manager device packages, see the following URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html

#### Configurable Application Timer

You can configure the application timer to 5 (default) or 20 seconds. This timer controls how long the phone waits after an
                           application message is sent to a phone before it identifies a communication issue.

Previously, the timer was set to five seconds. If the action (for example, play a ringtone) took longer than the timer, the
                           timer expired and an error message (405) was sent to the logging system.

In Cisco Unified Communications Manager Administration, set the field Application Request Timer in the Device > Phone page.

##### Where to Find More Information

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide

#### Configurable Left Softkey

You can configure the left softkey of an inactive phone to be:

None

Favorites (default)

Local Contacts

Voicemail

In Cisco Unified Communications Manager Administration, set the field Left
                              Softkey in the Device > Phone page.

##### Where to Find More Information

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide

Cisco Wireless IP Phone 8821 and 8821-EX User Guide

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco Wireless IP Phone 882x Series Documentation

Find documentation that is specific to your phone model, call control system, and language on the product support page for
                        the Cisco Wireless IP Phone 8821 and Cisco Wireless IP Phone 8821-EX . From these pages, you can also find the Cisco Wireless IP Phone 8821 and 8821-EX Wireless LAN Deployment Guide .

### Cisco Unified
                     				Communications Manager Documentation

See the Cisco Unified
                              				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                           				Communications Manager release on the product support page.

### Cisco Unified
                     				Communications Manager Express Documentation

See the publications that are specific to your language, phone model, and release on the product support page for Cisco Unified
                              				Communications Manager Express .

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified
                        				Communications Manager is running the latest device package. After you install a device package on the Cisco Unified
                        				Communications Manager servers in the cluster, you need to reboot all the servers.

If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly.

For information on the device packages, see the Cisco Unified
                        				Communications Manager Device Package Compatibility Matrix .

### Install Firmware Release 11.0(6) on Cisco Unified Communications Manager

Before you can use the phone firmware release on the Cisco Unified Communications
                        				Manager, you must install the latest Cisco Unified Communications Manager firmware
                        				on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Choose Cisco IP Phone 8800 Series .

Choose Cisco Wireless IP Phone 8821 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 11.0(6) .

Select the firmware file, click the Download or Add to cart button, and follow the prompts.

Firmware file: cmterm-8821-sip.11-0-6-7.k3.cop.sgn

If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file.

Click the + next to the firmware file name in the
                                 					Download Cart section to access additional information about this file. The
                                 					hyperlink for the readme file is in the Additional Information section, which
                                 					contains installation instructions for the corresponding firmware.

Follow the instructions in the readme file to install the firmware.

### Install Firmware Release 11.0(6) on Cisco Communications Manager Express

You must download the Cisco Wireless IP Phone 8821 firmware image file from the
                        				software download center.

For information on Cisco Unified Communications Manager Express support, see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/feature/phone_feature/phone_feature_support_guide.html .

For more information about this procedure, refer to the "Install and Upgrade Cisco
                           					Unified CME Software" chapter in the Cisco Unified Communications
                           					Manager Express System Administrator Guide at this URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm.html

To access the firmware files, go to this URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco Wireless IP Phone 8821 .

Choose Session Initiation Protocol (SIP) Software .

Choose 11.0(6) in the Latest
                                    						Releases folder.

Click Download or Add to cart and
                                 					follow the prompts.

The file to download is cmterm-8821.11-0-6-7.zip

Extract the files from the zip file, manually copy them to the Cisco Unified
                                 					Communications Manager Express TFTP server (router flash), and enable them for
                                 					TFTP.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Administrative tasks, such as an internal port scan or security scan.

Attacks that occur on your network, such as a Denial of Service attack.

### Health-Care
                  	 Environment Use

This product is not a
                     		medical device and uses an unlicensed frequency band that is susceptible to
                     		interference from other devices or equipment.

### Recording Tone Volume Limitation

If you use the recording feature, we recommend that you change the Recording Tone Local Volume configured in Cisco Unified
                           				Communications Manager . Change the field from the default of 100 to 20, as described in CSCvc14605 .

The Cisco Unified
                           				Communications Manager device packs (October 2017 and later) have the default set to 20.

### TLS 1.2 Tunnel Limitation with ISE 2.0 to 2.3

To support a TLS 1.2 tunnel between the phone and the Cisco Identity Service Engine (ISE) server, the ISE patch to resolve CSCvm03681 must be applied. This patch is required for ISE servers running Release 2.0 to 2.3; ISE Release 2.4 and later include the
                        patch.

## Caveats

### View Caveats

You can search for caveats using the Cisco Bug Search tool.

Known caveats (bugs) are graded according to severity level, and can be either open
                        				or resolved.

Before you begin

#### Before you begin

To view caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

Use this URL for all caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%286%29&sb=anfr&bt=custV

Use this URL for all open caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%286%29&sb=afr&bt=custV

Use this URL for all resolved caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%286%29&sb=fr&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco
                        				Wireless IP Phone 8821 and 8821-EX that use Firmware Release 11.0(6).

For more information about an individual defect, you can access the online record for
                        				the defect from the Bug Search Toolkit. You must be a registered Cisco.com user to
                        				access this online information.

Because defect status continually changes, the list reflects a snapshot of the
                        				defects that were open at the time this report was compiled. For an updated view of
                        				open defects or to view specific bugs, access the Bug Search Toolkit as described in View Caveats .

CSCvh47665 No Secure tone played on protected phones while enable speaker

CSCvm66028 Phone will eventually loose WiFi when roaming between 2 AP's set
                              						at 80MHz/40MHz

CSCvm69293 Network configuration info not displayed on current wlan
                              						profile

CSCvm74978 8821 phone sometimes couldn't receive the EAP identity request on
                              						2.4G JFW test bed.

CSCvn05182 UI error while enable FAC

CSCvn18501 MLPP priority lost in session bubble during xfer/conference

CSCvn25375 Failed to run Codenomicon TLS client test suite on 8821

CSCvn58894 8821 Persional Directory Login should not display again after
                              						success login & exit without logout

CSCvn63992 UI: missing SSID if in neighbor list before WLAN connection

CSCvn81608 Java process sometimes has significant delay in receiving events
                              						from wlanmgr after OOR & In Range

CSCvo05996 No Recording Tone heard after hold/resume several times.

CSCvo08723 Phone not able to re-connect to highest priority WLAN profile
                              						after connect to lower priority one

CSCvo10371 Phone did not do full authentication after deauth 7 causing call
                              						preservation

CSCvo46442 Phone shut down when battery was showing 13%

CSCvo74044 Hear short sharp ring tone during hold revert with Chirp1&2
                              						ringtone and RIU session.

CSCvo74177 Sometimes(90%) ringer is very low in hold reversion state when
                              						ringer volume is maximized

CSCvo74782 Phone log and multimeter discrepancy when measuring battery at
                              						full charge and drained

CSCvo74800 Voltage loss of 1V shown in phone log after boot with fully
                              						charged battery

CSCvo82607 Wrong behavior after press red key on originator phone in
                              						conference call when failover to SRST

CSCvp14422 Phone will not roam from 5GHz WLAN profile to 2.4GHz WLAN profile
                              						if SSID disabled via WLC

CSCvq22593 kernel timer didn't follow the interval parameter set by user
                              						space application (wlanmgr)

CSCvr86735 Phone does not ring for hold reverted call after disconnecting
                              						another active call

CSCvs16657 Call is automatically muted when dock station power is
                              						disconnected

CSCvs85963 'undefined' and 'Rcvr packets' swapping on Call statistics
                              						screen

CSCvt02503 Phone no longer plays recording tone after a few calls

CSCvv04725 8821 has no dial tone after fallback from srst to cucm

CSCvv45769 8821 can't set local time from LCD if its dhcp server has option
                              						42 configured

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for
                        				the Cisco Wireless IP Phone 8821 and 8821-EX that use Firmware Release 11.0(6).

For more information about an individual defect, you can access the online record for
                        				the defect from the Bug Search Toolkit. You must be a registered Cisco.com user to
                        				access this online information.

Because defect status continually changes, the list reflects a snapshot of the
                        				defects that were resolved at the time this report was compiled. For an updated view
                        				of resolved defects or to view specific bugs, access the Bug Search Toolkit as
                        				described in View Caveats .

CSCvh27418 Transfer soft key shall be grey before C answer while
                              						semi-transfer is disabled

CSCvm58907 Firmware sometimes couldn't complete the fresh association

CSCvm87368 Phone can't get ip address when DHCP option 150 field configured
                              						with MaxLength

CSCvm95611 XML message does not display on lock screen if http url priority
                              						is 1 or 2

CSCvn07039 \"Error:Invalid Code in Speed dial\" not display while press SD
                              						including error FAC or CMC

CSCvn41362 cp8821ï¼šno \"CAL Text#\" displayed in \"incoming call toast\"

CSCvn43154 No \"details\" softkey in multi-leg call history

CSCvn64510 Neighbor list shows multiple AP's and does not update when in
                              						Single AP mode

CSCvn66303 Phone not vibrate while with hold or RIU session when vibrate on
                              						ring:on

CSCvo09354 No toast message displayed after unchecking \"Logged into
                              						Huntgroup\" checkbox

CSCvo26159 8821 failing to roam flexconnect over the air after reassoc_resp
                              						it tries to auth with previous AP

CSCvo30508 Softkey options shouldn't be shown in line missed calls page if
                              						blank

CSCvo32881 Both speaker icon displayed when setting auto answer with speaker
                              						on shared line

CSCvo37017 The ring doesn't play when a call in hold revert

CSCvo44285 Multiple Vulnerabilities in qt
                              						(CVE-2018-19870)(CVE-2018-15518)

CSCvo45809 OpenSSH Bailout Delaying User Enumeration Vulnerability
                              						(CVE-2018-15473)

CSCvo45811 Multiple Vulnerabilities in glibc

CSCvo55873 CFW info on non-primary line shall not be carried to SRST

CSCvo78333 Conference call UI display error on SRST

CSCvp00913 After disable SSH Access from CUCM, still can access phone via SSH
                              						on rel phone

CSCvp02109 UI got into abnormal state after exiting PRT prior to completion
                              						then back to Settings when done

CSCvp07713 WLAN diag not showing 2.4GHz AP's in WLAN profile set for
                              						2.4GHz

CSCvq25311 Multiple Vulnerabilities in dbus

CSCvq31290 BusyBox add_match Function Arbitrary Code Execution
                              						Vulnerability

CSCvq76705 Observe battery level 99%~100% floating issue after fully
                              						charged

CSCvq80441 Cisco 8821 Wireless IP Phone Key Negotiation of Bluetooth
                              						Vulnerability

CSCvr06067 Dnsmasq DNS Packet Processing Buffer Overflow Vulnerability

CSCvr30314 Multiple Vulnerabilities in linux kernel (CVE-2019-10638 and
                              						CVE-2019-10639)

CSCvr54353 Linux Kernel CVE (CVE-2019-16413 to CVE-2019-3874)

CSCvr55596 cURL and libcurl tftp_receive_packet() Function Heap Buffer
                              						Overflow ...

CSCvr57950 Phone continues blinking amber after shared line answers 2nd
                              						incoming call

CSCvr70039 Vulnerability in linux kernel (CVE-2019-11190)

CSCvr71242 Vulnerability in linux kernel (CVE-2019-11599)

CSCvr71414 Vulnerability in linux kernel (CVE-2019-15214)

CSCvr76650 Vulnerability in linux kernel (CVE-2019-15916)

CSCvr87703 Vulnerability in linux kernel (CVE-2019-15666)

CSCvr89188 Vulnerability in linux kernel (CVE-2019-16994)

CSCvr94805 Vulnerability in linux kernel (CVE-2019-15927)

CSCvs22379 Single click on green button sometimes triggers Redial

CSCvs33435 Linux Kernel Use-After-Free Vulnerability CVE-2017-10661

CSCvs61484 Multiple Vulnerabilities in linux_kernel CVE-2018-10879

CSCvs63233 Multiple Vulnerabilities in linux_kernel CVE-2018-5344

CSCvs76925 libxml2 xmlParseBalancedChunkMemoryRecover Memory Leak
                              						Vulnerability

CSCvs77087 cURL FILE: URL Creation Vulnerability

CSCvs87896 CVE-2019-15126: WPA and WPA2 Information Disclosure
                              						Vulnerability

CSCvs95078 Qt SVG Document Exponential XML Entity Expansion Attack
                              						Vulnerability

CSCvt00332 CDP parameter configuration does not show on phone webpage

CSCvt00409 Multiple Vulnerabilities in zlib 1.2.8

CSCvt01522 8821:roaming: after re-association phone responds with ACK to
                              						frames from previous AP

CSCvt08482 Multiple Vulnerabilities in linux_kernel CVE-2019-19252

CSCvt16802 Unable to answer incoming call from wired headset when keypad is
                              						locked

CSCvt27645 Cisco IP Phone Call Log Information Disclosure Vulnerability

CSCvt81786 xpointer.c in libxml2 before 2.9.5 (as used in Apple iOS before
                              						10, ...

CSCvt85130 Buffer overflow in libxml2 allows remote attackers to execute
                              						arbitr ...

CSCvt87456 WLAN chip crashing on 8821 phones due to CCKM roaming failure.

CSCvt96006 libcurl curl_easy_unescape Heap Overflow Remote Code Execution
                              						Vulne ...

CSCvu00767 8821 WLAN Manager is reporting no roaming candidates

CSCvu16168 Evaluation of sl-wireless-phones for Method Confusion Pairing
                              						Vulnerability for LE and BR/EDR Implem

CSCvu52381 CP-8821 - After AP sends a Deauth the WPA_supplicant is stuck in
                              						the disconnected state

CSCvu74127 WLAN manager report \"No valid APs\" after a roaming is skipped
                              						during the EAP authentication

CSCvu97168 CIAM: linux-kernel 3.0.31 (CVE-2014-2523)

CSCvv41751 CIAM: linux-kernel 3.0.31 CVE-2016-10229

## Cisco Unified Communication Manager Public Keys

To improve software integrity protection, public keys are used to sign cop files for Cisco Unified Communications Manager
                     Release 10.0.1 and later. These cop files have "k3 or k4" in their name. To install a k3 or k4 cop file on a pre-10.0.1 Cisco Unified Communications Manager, consult the Readme for
                     the ciscocm.version3-keys.cop.sgn to determine if you must install this additional cop file on your specific Cisco Unified
                     Communications Manager version. If these keys are not present and are required, you will see the error "The selected file is not valid" when you try to install the software package.

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

You may want to bookmark the web pages for the phone models that are deployed in your company and send these URLs to your
                                 users.

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see the Cisco IP Phone Firmware Support Policy .

| Call Control System | Minimum Version | Recommended Versions |
|---|---|---|
| Cisco Unified Communications Manager | 9.1(2) | 10.5(2), 11.0(1), 11.5(1), 12.0(1), 12.5(1), and later |
| Cisco Unified Communications Manager Express | 10.5 through Fast Track | 11.7 and later |
| Cisco Unified Survivable Remote Site Telephony | 10.5 | 11.7 and later |

| Access Point Hardware | Minimum Version | Recommended Versions |
|---|---|---|
| Cisco AireOS Wireless LAN Controller | 8.0.121.0 | 8.0.152.0, 8.2.170.0, 8.3.150.0, 8.5.161.0, 8.8.130.0, 8.10.130.0 |
| Cisco Catalyst IOS XE Wireless LAN Controller | 16.12.1s | 16.12.3 |
| Cisco Mobility Express | 8.3.143.0 | 8.3.150.0, 8.5.161.0, 8.8.130.0, 8.10.130.0 |
| Cisco IOS Access Points (Autonomous) | 12.4(21a)JY | 12.4(25d)JA1, 15.2(4)JB6, 15.3(3)JD17, 15.3(3)JF12i, 15.3(3)JPJ4 |
| Cisco Meraki | MR 25.9, MX 13.33 | MR 26.8.1, MX14.42 |

| Note | Some features may require the installation of a Cisco Unified Communications Manager Device Package. Failure to install the
                              Device Package before the phone firmware upgrade may render the phones unusable. |
|---|---|

| Note | Use the lowest-strength cleaning agent to prolong the life and look of the case. |
|---|---|

| Note | If your Cisco Unified
                                    				Communications Manager doesn't have the required device package to support this firmware release, the firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phone 8800 Series . |
| Step 3 | Choose Cisco Wireless IP Phone 8821 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 11.0(6) . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. Firmware file: cmterm-8821-sip.11-0-6-7.k3.cop.sgn Note If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware file name in the
                                 					Download Cart section to access additional information about this file. The
                                 					hyperlink for the readme file is in the Additional Information section, which
                                 					contains installation instructions for the corresponding firmware. |
| Step 8 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download
                                                   								Cart link when you are ready to download the file. |
|---|---|

| Step 1 | To access the firmware files, go to this URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco Wireless IP Phone 8821 . |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | Choose 11.0(6) in the Latest
                                    						Releases folder. |
| Step 5 | Click Download or Add to cart and
                                 					follow the prompts. The file to download is cmterm-8821.11-0-6-7.zip |
| Step 6 | Extract the files from the zip file, manually copy them to the Cisco Unified
                                 					Communications Manager Express TFTP server (router flash), and enable them for
                                 					TFTP. |

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%286%29&sb=anfr&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%286%29&sb=afr&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%286%29&sb=fr&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) Enter the bug ID number in the Search for field, then press Enter . |

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