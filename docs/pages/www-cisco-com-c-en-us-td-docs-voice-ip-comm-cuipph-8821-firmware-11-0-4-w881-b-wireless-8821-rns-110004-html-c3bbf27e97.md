---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8821-firmware-11-0-4-w881-b-wireless-8821-rns-110004-html-c3bbf27e97
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8821/firmware/11-0-4/w881_b_wireless-8821-rns-110004.html
retrieved_at: 2026-08-21T13:35:22.753841+00:00
---

Cisco Wireless IP Phone 8821 Release Notes for Firmware Release 11.0(4)

# Cisco Wireless IP Phone 8821 Release Notes for Firmware Release 11.0(4)

### Download Options

Updated: July 9, 2018

First Published: June 5, 2018

Last Updated: July 9, 2018

# Cisco Wireless IP Phone 8821 Release Notes for Firmware Release 11.0(4)

These release notes support the Cisco Wireless IP Phone 8821 Firmware Release 11.0(4).

The following table describes the systems and versions that the phone requires.

System

Minimum Version

Recommended Versions

Cisco Unified Communications Manager

9.1(2)

10.5(2), 11.0(1), 11.5(1), and later

Cisco Unified Communications Manager Express

10.5 through Fast Track

11.0, 11.5, 11.7 (native support), and later

Cisco Unified Survivable Remote Site Telephony

10.5

11.0, 11.5, 11.7, and later

Cisco Wireless LAN Controller

8.0.121.0

8.0.152.0, 8.2.166.0, 8.3.141.0, 8.5.120.0

Cisco IOS Access Points (Autonomous)

12.4(21a)JY

12.4(25d)JA2, 15.2(4)JB6, 15.3(3)JF1

Cisco Meraki

## New and Changed
               	 Features

The following sections describe the features that are new or have
                  		changed in this release.

Some features may require the installation of a Cisco Unified Communications Manager Device Package. Failure to install the
                              Device Package before the phone firmware upgrade may render the phones unusable.

### Features Available
                  	 with the Firmware Release

The following sections describe the features available with the Firmware
                     		Release.

#### Configurable Home Screen

The configurable home screen feature enables you to set a user's phone to display the main (Applications) screen or the Line
                           view screen by default. Users who make or receive frequent phone calls may prefer to have the Line view as their home screen.

You set the view using the Home Screen field in the Cisco Unified Communication Manager Administration window Device > Phone .

##### Where to Find More Information

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

Cisco Wireless IP Phone 8821 and 8821-EX User Guide

#### Local Contacts

The local contacts feature enables users to keep a phone book that is local to their phone. Users can add entries to their
                           Local contacts from their Personal Directory. They can also add entries to a Favorites list. Users can have up to 200 entries
                           in their Local contacts and 50 entries in their Favorites list.

You can also add entries to a user's phone from the phone web page. You control access to the phone web page with the Web Admin field. A comma separated value (CSV) file can be imported or exported from the web page. The CSV file uses the following
                           format:

First name, Last name, Nickname, Company, Work number, Home number, Mobile number, Email address, Work primary, Home primary,
                              Mobile primary, Work favorite, Home favorite, Mobile favorite

##### Where to Find More Information

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

Cisco Wireless IP Phone 8821 and 8821-EX User Guide

#### Problem Report Tool

You can get a problem report generated from the phone. The report contains information that Cisco TAC requires for troubleshooting.

You or your user can generate the problem report from the phone. After the report is generated, you can access the report
                           from the phone administration web page.

##### Where to Find More Information

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

Cisco Wireless IP Phone 8821 and 8821-EX User Guide

#### Ringtone Enhancements

You can hear the Chirp1 and Chirp2 ringtones better in noisy environments. New versions of these ringtones are optimised for
                           the wireless phone speaker.

In the Settings app, select Phone settings > Sounds > Ringtone and choose Chirp1(mobile) or Chirp2(mobile) .

#### User Interface Enhancements for Firmware Release 11.0(4)

Firmware Release 11.0(4) introduces these user interface changes:

The default level for the screen brightness changes from 8 to 5.

The default screen display timeout changes from 30 seconds to 10 seconds.

The transmitter and receiver Wireless Multi Media (WMM) UP values are now displayed in the call statistics pages.

If you upgrade from a previous release,

Users retain their previously-configured screen brightness.

If the user changed the screen display timeout, their previous setting is retained. However, if the user had the timeout set
                                 to 30 seconds, then their setting changes to 10 seconds.

##### Where to Find More Information

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

Cisco Wireless IP Phone 8821 and 8821-EX User Guide

### Features Available
                  	 with the Latest Cisco Unified Communications Manager Device Pack

The following sections describe features in the release which require
                     		the new firmware and the latest Cisco Unified Communications Manager Device
                     		Pack.

For information about the Cisco Unified IP Phones and the required Cisco
                     		Unified Communications Manager device packs, see the following URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html

#### Resized Wallpapers

The 11.0(4) release introduces new wallpapers that are customized for the wireless phone screen. The wallpapers have these
                           sizes:

Full size image—240 pixels (width) x 320 pixels (height)

Thumbnail image—117 pixels (width) x 117 pixels (height)

The wallpapers are stored in a new TFTP folder: Desktops/240x320x24 .

Some of the previous wallpapers are no longer available in the new format.

If you have a custom wallpaper (for example, your company logo), then you need to resize the wallpaper and thumbnail images
                           to match the above specifications and store them in the Desktops/240x320x24 folder on your TFTP server.

This feature requires the installation of the wallpaper COP file: cmterm-8821-sip.11-0-4_wallpaper.k3.cop.sgn either alone or as part of the next device pack.

Existing users do not see any difference in their screens after the upgrade. They continue to use the previous wallpapers.
                           But when they access the Settings app to change the wallpaper, they can view and select the new wallpapers. They may not, however, see the old wallpaper in
                           the new list of wallpapers.

##### Where to Find More Information

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco Wireless IP Phone 882x Series Documentation

Refer to
                        		  publications that are specific to your language, phone model, and call control
                        		  system. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/tsd-products-support-series-home.html

The Deployment Guide is located at the following URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/unified-ip-phone-8800-series/products-implementation-design-guides-list.html

### Cisco Unified
                     				Communications Manager Documentation

See the Cisco Unified
                              				Communications Manager Documentation Guide and other publications that are specific to your Cisco Unified
                           				Communications Manager release. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/tsd-products-support-series-home.html

### Cisco Unified
                     				Communications Manager Express Documentation

See the publications that are specific to your language, phone model and Cisco Unified
                           				Communications Manager Express release. Navigate from the following documentation URL:

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-express/tsd-products-support-series-home.html

## Installation

### Installation Requirements

Before you install the firmware release, you must ensure that your Cisco Unified Communications Manager is running the latest
                     device pack. After you install a device pack on the Cisco Unified Communications Manager servers in the cluster, you need
                     to reboot all the servers.

If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly.

For information on the Cisco Unified Communications Manager Device Packs, see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/compat/devpack_comp_mtx.html .

### Install Firmware Release 11.0(4) on Cisco Unified Communications Manager

Before you can use the phone firmware release on the Cisco Unified Communications Manager, you must install the latest Cisco
                        Unified Communications Manager firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Choose Cisco IP Phone 8800 Series .

Choose Cisco Wireless IP Phone 8821 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 11.0(4) .

Select the firmware file, click the Download or Add to cart button, and follow the prompts.

Firmware file: cmterm-8821-sip.11-0-4-14.k3.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

### Install Firmware Release 11.0(4) on Cisco Communications Manager Express

You must download the Cisco Wireless IP Phone 8821 firmware image file from the software download center.

For information on Cisco Unified Communications Manager Express support, see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/feature/phone_feature/phone_feature_support_guide.html .

For more information about this procedure, refer to the "Install and Upgrade Cisco Unified CME Software" chapter in the Cisco Unified Communications Manager Express System Administrator Guide at this URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm.html

To access the firmware files, go to this URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco Wireless IP Phone 8821 .

Choose Session Initiation Protocol (SIP) Software .

Choose 11.0(4) in the Latest Releases folder.

Click Download or Add to cart and follow the prompts.

The file to download is cmterm-8821.11-0-4-14.zip

Extract the files from the zip file, manually copy them to the Cisco Unified Communications Manager Express TFTP server (router
                                 flash), and enable them for TFTP.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video
                        		  quality, and in some cases, can cause a call to drop. Sources of network
                        		  degradation can include, but are not limited to, the following activities:

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Health-Care
                  	 Environment Use

This product is not a
                     		medical device and uses an unlicensed frequency band that is susceptible to
                     		interference from other devices or equipment.

### Recording Tone Volume Limitation

If you use the recording feature, we recommend that you change the Recording Tone Local Volume configured in Cisco Unified
                        Communications Manager. Change the field from the default of 100 to 20.

The CUCM device packs (October 2017 and later) have the default set to 20.

For more information, look at CSCvc14605 using https://tools.cisco.com/bugsearch .

## Caveats

### View Caveats

You can search for caveats using the Cisco Bug Search tool.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

#### Before you begin

To view caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

Use this URL for all caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%284.&sb=anfr&bt=custV

Use this URL for all open caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%284.&sb=afr&bt=custV

Use this URL for all resolved caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%284.&sb=fr&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco Wireless IP Phone  8821 that use
                        Firmware Release 11.0(4).

For more information about an individual defect, you can access the online record for the defect from the Bug Search Toolkit.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects or to view specific bugs, access the Bug Search Toolkit as described in View Caveats .

CSCus70389 No effect on failure on setting Detect Unified CM Connection Failure

CSCuw10789 Configuration: RTP/sRTP Port Range Configuration

CSCux86153 Reverting Focus Priority set at \"Lower\" doesn't work as expected.

CSCuz22603 Phone may fail to update trust list files after reset

CSCva89241 Call doesn't forward to Voicemail when \"No Ring on duration\" set to 200

CSCvb72018 Should dial from the highlighted line when posting Dial URI to the phone

CSCvc26512 8821 FIPPA does not show notification of Server Failure on CCX Failover

CSCvd49867 Phone doesn't execute application button activation timer accurately

CSCvd72816 RSSI value for connected AP is slow to update when phone is in Single AP mode

CSCve00725 Key processing failed due to QT issue

CSCvf61864 Messages received before keypad auto lock will not display after ending incoming calls

CSCvg06985 8821 won't boot, won't power on: LOADER authentication failure

CSCvg33518 Entering PD/CD Multiple Times Causes Memory Leak

CSCvg59066 Speed Dial & BLF SD are not working when on call

CSCvg73175 One way audio occurred after long call duration

CSCvh27815 8821 reached its maximum number of calls after being declined twice

CSCvh55508 WFi chip is not waking up at regular interval in single AP mode

CSCvh64535 Random roaming timeouts seen on conducted roaming testbed

CSCvh89574 Pressing Green button to make a call - missing in PD/CD & Line View

CSCvi68937 8821 advertises dongle MAC instead of phone MAC via CDP

CSCvj02218 Park resume is greyed out in 8821 registered in CME

CSCvj31724 Phone stays at blue screen with Cisco logo when booting and battery is low

CSCvj38637 CUCM WLAN Profile download and apply occurs prior to user cert install via SCEP

CSCvj39392 Call drop for pending conference after scroll up then press Merge all soft key

CSCvj39548 The session can't resume when switch back to the session initiated by conf method

CSCvj42007 DUT don't vibrate sometimes when pickup call with DND enable

CSCvj42039 Voice volume setting of BT headset hasn't been saved after headset power off and on

CSCvj42047 Somtimes there is no MOH when call with Bluetooth headset on

CSCvj43956 New call soft key not work while focus on BLF speed dial

CSCvj44276 No notification tone for callback when intercom call is in active status

CSCvj44543 8821 IP Phone loses DHCP IP Address after OOR event on Meraki AP

CSCvj45498 Ringer shouldn't play thu headset in Australia network locale when inserting headset during ringing

CSCvj46981 \"Battery charging\" toast not display when power charging with USB cable.

CSCvj47001 Ringer for incoming call switches to headset after docked when ringer output is set to speaker

CSCvj53208 White screen flash while charging powered off phone

CSCvj54504 Blank call view after end the call on one line and then resume call on another line

CSCvj54731 Should delay ringer output for 4 sec if 2nd call comes in immediately after 1st call is ended

CSCvj55168 ip can be pinged after dhcp address released through \"wifi interface\"

CSCvj63107 Phone rebooted during active call due to java restart

CSCvj65574 Hourly logs files may be corrupted which hinders troubleshooting activity

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco Wireless IP Phone  8821 that
                        use Firmware Release 11.0(4).

For more information about an individual defect, you can access the online record for the defect from the Bug Search Toolkit.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                        report was compiled. For an updated view of resolved defects or to view specific bugs, access the Bug Search Toolkit as described
                        in View Caveats .

CSCuw70288 After factory reset BT functionality is set to disabled by admin

CSCva23418 WLAN Diags does not show APs for subsequent profiles if the SSID is not broadcasted

CSCvb73660 Empty string in EditDial should not dial out when pressing green button

CSCvc29244 Delayed ringer audio is not audible after un-docking the phone

CSCvc93714 CP-8821: Not updated center phone icon when saving CFA destination via web

CSCvd63574 8821 does not send firmware download complete to CUCM

CSCve10782 Icons on phone line view screen should be on the right when using RTL locales

CSCve38060 8821 caches credentials after Reset Network Settings

CSCve73040 Continuous device or resource busy

CSCve88286 The deleted recent call history was restored after rebooting the phone

CSCve97390 WLAN Info shows highest priority enabled profile data instead of current connected profile

CSCvf49935 Reset Security Settings does not remove EAP-FAST PAC files

CSCvf70504 All 2G neighbors disappear when shut 5G network down when phone in auto-band wifi mode

CSCvf70712 One phone took 30+ seconds to register after OOR for 45 minutes.

CSCvf86441 Call dropped due to two successive EAP authenticaion failure

CSCvf87854 8821 should give priority to 8821-WLAN< MAC >.xml over 8821-WLANDefault.xml

CSCvf91949 URI navigation key is not working on line view when on call

CSCvf93727 Call UI not brought up when answering an incoming call after making intercom call

CSCvg00814 8821 UI resets when USB Ethernet interface comes up after docking or goes down after undocking

CSCvg04349 WLAN Diagnostics does not work with SR3 and SR4

CSCvg22234 Evaluation of sl-wireless-phones for Dnsmasq October 2017 vulnerabilities

CSCvg23146 NullPointerException could occur when UI was switching focus between the PD and CallUI pages

CSCvg31303 8821 : DHCP process fails on boot up after roaming in a foreign-anchor WLC configuration

CSCvg40447 NullPointerException when viewing Call Stats via webpage and Voice CAC is disabled

CSCvg48649 8821 - EAP-TLS User Certificate Upload Fails With Extract Passwords = 12

CSCvg49062 ioremap error in logs

CSCvg60329 De-registration triggered after roaming timeout

CSCvg70069 Session bubble shall not display Recording while on hold

CSCvg71662 Phone will reset itself after end the conference call

CSCvg73959 Phone can't resume call after hold then lost register

CSCvg77010 One way audio hit after roaming on 8821

CSCvg78924 Java thread crash caused dark screen

CSCvg93137 8821 phone need to request DHCP uppon receiving Deauth 108 from WLC

CSCvh05429 Hunt Pilot name not displayed for huntgroup calling

CSCvh05930 [8821] Phone may hang or crash at power on, during SSH or updating Wi-Fi profiles

CSCvh13427 Phone not switching profiles when there are auth failures

CSCvh15285 DNS info got lost after phone power off/on when DHCP in off status

CSCvh16733 FW unable to hear mgmt packet responses from AP on some channels

CSCvh17753 8821 one-way audio for an active call when incoming call on group gets cancelled

CSCvh20089 8821: improve ringer perceptibility

CSCvh27866 UI error after press green button of park revert during conference set up

CSCvh27921 Phone become to black screen and not respond to any key press

CSCvh28099 8821 not waking at DTIM when AP does not support Proxy ARP

CSCvh32833 Proxy ARP status in WLAN Diags is tied to CCX version not Standard version

CSCvh45788 8821 unable to roam to near AP when 802.11 mode is set to Auto

CSCvh50566 Long contact name should be truncated and replaced with ellipsis

CSCvh54037 Call details and Recents details do not display hunt group call information

CSCvh54525 Blind transfer on CME not work

CSCvh58389 BDU file not applied to 8821 phone if PSK passphrase contains characters & < > \" \"

CSCvh59694 No 'Unlock' softkey after sending URL=\"Init:Services\" via XML to 8821 while XML popup present

CSCvh62273 Call drop on 11r PSK over time due to deauth reason code 108

CSCvh64525 RSSI fluctuation after some time when on call roaming between 2 AP's

CSCvh67010 AP details in neighbor list are incorrect when set to Auto and has both 5 GHz and 2.4 GHz neighbors

CSCvh67451 Phone with static IP is not able to register to the CUCM in case of OOR

CSCvh73039 BDU: 8821 shows blank WEP key shows for Profiles 2-4

CSCvh75975 Screen repeatedly turns on when in unpowered docking station

CSCvh83331 8821: Phone powers itself up after power down

CSCvh91232 BDU: Export and error consistency fixes

CSCvh92766 'Unlock' softkey missing after placing call to 8821

CSCvi03165 User ID and Password are cleared when pushing down CUCM WLAN Profile

CSCvi25073 LCD cannot be turned on under DIM status when receiving an XML message

CSCvi33354 HTTP response can not release wake lock and impact battery life

CSCvi41091 8821 sometimes does not reply to ARP request if far end cleared its ARP cache

CSCvi47178 Phone should always use configured sleep timer regardless of registered state

CSCvi49699 Phone doesn't go to sleep per configured sleep timer when powered on OOR

CSCvi50362 Transferor didn't turn to idle status after Consultative Transfer finished over SRS

CSCvi55889 8821 : Black screen and would not wake up, incoming calls will ring but cannot be answered

CSCvi67005 Race condition for EAPOL pkt handler in wpa_supplicant using CCKM causes EAP handshake failure

CSCvi71413 Softkeys are displayed for highlighted SURL when they shouldn't be

CSCvi72144 8821 not sending SCEP request to Cisco RA when using static IP

CSCvi73505 Phone played constant noise after long call duration

CSCvi73544 Check in the wlan firmware release 6.50.0.12

CSCvi78358 8821 can't save debug command after reset or power-cycle

CSCvi95656 Auto scan triggers frequent scans after roaming causing battery drain

CSCvj04847 Call end softkey is not working in 8821 for japanese locale

CSCvj07546 Phone de-registered due to re-IP during overnight testing

CSCvj16686 Phone stuck on Cisco logo startup screen java.util.ConcurrentModificationException

CSCvj43381 Unlock softkey not displayed after received XSI object then missed a call

## Cisco Unified Communication Manager Public Keys

To improve software integrity protection, new public keys are used to sign cop files for Cisco Unified Communications Manager
                     Release 10.0.1 and later. These cop files have "k3" in their name. To install a k3 cop file on a pre-10.0.1 Cisco Unified Communications Manager, consult the README for the
                     ciscocm.version3-keys.cop.sgn to determine if this additional cop file must first be installed on your specific Cisco Unified
                     Communications Manager version. If these keys are not present and are required, you will see the error "The selected file is not valid" when you try to install the software package.

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

To access the Locale Installer required for a release, access https://software.cisco.com/download/navigator.html?mdfid=286037605&flowid=46245 , navigate to your phone model, and select the Unified Communications Manager Endpoints Locale Installer link.

For more information, see the documentation for your particular Cisco Unified Communications Manager release.

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

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| System | Minimum Version | Recommended Versions |
|---|---|---|
| Cisco Unified Communications Manager | 9.1(2) | 10.5(2), 11.0(1), 11.5(1), and later |
| Cisco Unified Communications Manager Express | 10.5 through Fast Track | 11.0, 11.5, 11.7 (native support), and later |
| Cisco Unified Survivable Remote Site Telephony | 10.5 | 11.0, 11.5, 11.7, and later |
| Cisco Wireless LAN Controller | 8.0.121.0 | 8.0.152.0, 8.2.166.0, 8.3.141.0, 8.5.120.0 |
| Cisco IOS Access Points (Autonomous) | 12.4(21a)JY | 12.4(25d)JA2, 15.2(4)JB6, 15.3(3)JF1 |
| Cisco Meraki |  |  |

| Note | Some features may require the installation of a Cisco Unified Communications Manager Device Package. Failure to install the
                              Device Package before the phone firmware upgrade may render the phones unusable. |
|---|---|

| Note | This feature requires the installation of the wallpaper COP file: cmterm-8821-sip.11-0-4_wallpaper.k3.cop.sgn either alone or as part of the next device pack. |
|---|---|

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phone 8800 Series . |
| Step 3 | Choose Cisco Wireless IP Phone 8821 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 11.0(4) . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. Firmware file: cmterm-8821-sip.11-0-4-14.k3.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
| Step 7 | Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware. |
| Step 8 | Follow the instructions in the readme file to install the firmware. |

| Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
|---|---|

| Step 1 | To access the firmware files, go to this URL: https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283 |
|---|---|
| Step 2 | Choose Cisco Wireless IP Phone 8821 . |
| Step 3 | Choose Session Initiation Protocol (SIP) Software . |
| Step 4 | Choose 11.0(4) in the Latest Releases folder. |
| Step 5 | Click Download or Add to cart and follow the prompts. The file to download is cmterm-8821.11-0-4-14.zip |
| Step 6 | Extract the files from the zip file, manually copy them to the Cisco Unified Communications Manager Express TFTP server (router
                                 flash), and enable them for TFTP. |

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%284.&sb=anfr&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%284.&sb=afr&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%284.&sb=fr&bt=custV |
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