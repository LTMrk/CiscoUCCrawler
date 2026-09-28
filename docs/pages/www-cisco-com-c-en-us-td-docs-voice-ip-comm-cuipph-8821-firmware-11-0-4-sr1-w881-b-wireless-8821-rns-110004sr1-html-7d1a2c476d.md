---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8821-firmware-11-0-4-sr1-w881-b-wireless-8821-rns-110004sr1-html-7d1a2c476d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8821/firmware/11-0-4-sr1/w881_b_wireless-8821-rns-110004sr1.html
retrieved_at: 2026-08-21T13:35:18.244684+00:00
---

Cisco Wireless IP Phone 8821 Release Notes for Firmware Release 11.0(4)SR1

# Cisco Wireless IP Phone 8821 Release Notes for Firmware Release 11.0(4)SR1

### Download Options

Updated: August 24, 2018

First Published: August 22, 2018

Last Updated: August 24, 2018

# Cisco Wireless IP Phone 8821 Release Notes for Firmware Release 11.0(4)SR1

These release notes support the Cisco Wireless IP Phone 8821 Firmware Release 11.0(4)SR1.

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

8.0.152.0, 8.2.170.0, 8.3.141.0, 8.5.135.0

Cisco IOS Access Points (Autonomous)

12.4(21a)JY

12.4(25d)JA2, 15.2(4)JB6, 15.3(3)JF1

Cisco Meraki

MR 25.9, MX 13.33

MR 25.11, MX 13.33

## New and Changed Features

This release contains no new or changed features.

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

### Install Firmware Release 11.0(4)SR1 on Cisco Unified Communications Manager

Before you can use the phone firmware release on the Cisco Unified Communications Manager, you must install the latest Cisco
                        Unified Communications Manager firmware on all Cisco Unified Communications Manager servers in the cluster.

Go to the following URL:

http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm

Choose Cisco IP Phone 8800 Series .

Choose Cisco Wireless IP Phone 8821 .

Choose Session Initiation Protocol (SIP) Software .

In the Latest Releases folder, choose 11.0(4)SR1 .

Select the firmware file, click the Download or Add to cart button, and follow the prompts.

Firmware file: cmterm-8821-sip.11-0-4SR1-13.k3.cop.sgn

If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file.

Click the + next to the firmware file name in the Download Cart section to access additional information about this file. The hyperlink
                                 for the readme file is in the Additional Information section, which contains installation instructions for the corresponding
                                 firmware.

Follow the instructions in the readme file to install the firmware.

### Install Firmware Release 11.0(4)SR1 on Cisco Communications Manager Express

You must download the Cisco Wireless IP Phone 8821 firmware image file from the software download center.

For information on Cisco Unified Communications Manager Express support, see http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/feature/phone_feature/phone_feature_support_guide.html .

For more information about this procedure, refer to the "Install and Upgrade Cisco Unified CME Software" chapter in the Cisco Unified Communications Manager Express System Administrator Guide at this URL:

http://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm.html

To access the firmware files, go to this URL:

https://software.cisco.com/download/navigator.html?mdfid=284729655&flowid=75283

Choose Cisco Wireless IP Phone 8821 .

Choose Session Initiation Protocol (SIP) Software .

Choose 11.0(4)SR1 in the Latest Releases folder.

Click Download or Add to cart and follow the prompts.

The file to download is cmterm-8821.11-0-4SR1-13.zip

Extract the files from the zip file, manually copy them to the Cisco Unified Communications Manager Express TFTP server (router
                                 flash), and enable them for TFTP.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call
                        to drop. Sources of network degradation can include, but are not limited to, the following activities:

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

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%284%29SR1&sb=anfr&bt=custV

Use this URL for all open caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%284%29SR1&sb=afr&bt=custV

Use this URL for all resolved caveats:

https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%284%29SR1&sb=fr&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) Enter the bug ID number in the Search for field, then press Enter .

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco Wireless IP Phone 8821 that use Firmware
                        Release 11.0(4)SR1.

For more information about an individual defect, you can access the online record for the defect from the Bug Search Toolkit.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were open at the time this report
                        was compiled. For an updated view of open defects or to view specific bugs, access the Bug Search Toolkit as described in View Caveats .

CSCuw10789 Configuration: RTP/sRTP Port Range Configuration

CSCux86153 Reverting Focus Priority set at \"Lower\" doesn't work as expected.

CSCuz22603 Phone may fail to update trust list files after reset

CSCva02670 Not able to delete paired BT devices when Bluetooth is turned off

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

CSCvh27418 Transfer soft key shall be grey before C answer while semi-transfer is diabled.

CSCvh27809 Focus and soft key error while press up-down hard key during conference

CSCvh27815 8821 reached its maximum number of calls after being declined twice

CSCvh28187 Can't pair with Plantronics VoyagerPro BT headset after disable/enable BT

CSCvh31648 Call should be disconnected while BT headset out of range for more than 30 seconds

CSCvh40589 Call disconnected while power off Jabra MOTION BT headset during call

CSCvh40728 Sometimes redial from Plantronics VoyagerPro BT headset not work

CSCvh47665 No Secure tone played on protected phones while enable speaker

CSCvh50994 No error toast prompts while cBarge failed due to maximum participants has been reached

CSCvh55508 WFi chip is not waking up at regular interval in single AP mode

CSCvh64535 Random roaming timeouts seen on conducted roaming testbed

CSCvh72297 Voice mail speed dial is not working if services provisioning set to External URL

CSCvh89574 Pressing Green button to make a call - missing in PD/CD & Line View

CSCvi24947 Display will not off while phone has one-way incoming intercom call

CSCvi66235 PB: When configuring a Favorite, middle button can dial number by mistake when in Contact details

CSCvi68937 8821 advertises dongle MAC instead of phone MAC via CDP

CSCvi87634 Sometimes time display error on call session bubble for 3-5 seconds

CSCvj02218 Park resume is greyed out in 8821 registered in CME

CSCvj30229 Change focus in line view app window display

CSCvj38637 CUCM WLAN Profile download and apply occurs prior to user cert install via SCEP

CSCvj39392 Call drop for pending conference after scroll up then press Merge all soft key

CSCvj39548 The session can't resume when switch back to the session initiated by conf method

CSCvj42007 DUT don't vibrate sometimes when pickup call with DND enable

CSCvj42039 Voice volume setting of BT headset hasn't been saved after headset power off and on

CSCvj42047 Somtimes there is no MOH when call with Bluetooth headset on

CSCvj43956 New call soft key not work while focus on BLF speed dial

CSCvj44276 No notification tone for callback when intercom call is in active status

CSCvj45498 Ringer shouldn't play thu headset in Australia network locale when inserting headset during ringing

CSCvj46981 \"Battery charging\" toast not display when power charging with USB cable.

CSCvj47001 Ringer for incoming call switches to headset after docked when ringer output is set to speaker

CSCvj53208 White screen flash while charging powered off phone

CSCvj54504 Blank call view after end the call on one line and then resume call on another line

CSCvj54731 Should delay ringer output for 4 sec if 2nd call comes in immediately after 1st call is ended

CSCvj55168 ip can be pinged after dhcp address released through \"wifi interface\"

CSCvj55253 Can't move focus to other lines with nav-button when phone is in dialing.

CSCvj59203 Phone lost IP due to encryption/decryption issue caused by wrong key

CSCvj92752 Failed to answer the reverting call by BT (Jabra SUPREME,Plantronics Legend,Plantronics PRO)

CSCvj94952 On Phone's LCD, the DN has not been changed after access hCluster successfully with EMCC method

CSCvk22665 8821 display comes on sometimes when on call with shared line

CSCvk30176 No response while press conf soft key after merge all on secured SRST

CSCvk49377 TX/Rx data packets issue after roaming during JFW stress test

CSCvk54638 8821 Not Ringing While Connected To Single Bay Charger (CP-DSKCH-8821)

CSCvk73764 Phone unable to connect to BTheadset after phone power cycle

CSCvm03674 one 8821 can't fallback to sub-cucm after sub CM service start more than half an hour

CSCvm04637 Continuous scan busy is reproducible on Conducted test bed with channel setting 36/44@20Mhz

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco Wireless IP Phone 8821 that use
                        Firmware Release 11.0(4)SR1.

For more information about an individual defect, you can access the online record for the defect from the Bug Search Toolkit.
                        You must be a registered Cisco.com user to access this online information.

Because defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                        report was compiled. For an updated view of resolved defects or to view specific bugs, access the Bug Search Toolkit as described
                        in View Caveats .

CSCvg52085 Misleading unregistration reason code when 8821 is powered off

CSCvj31724 Phone stays at blue screen with Cisco logo when booting and battery is low

CSCvj37175 Java crash and phone reset after press merge all on secured SRST

CSCvj44543 8821 IP Phone loses DHCP IP Address after OOR event on Meraki AP

CSCvj47572 8821 only try to resolve IP of TVS server one time after boot up

CSCvj61343 Cisco IP Phone 8821 Denial of Service Vulnerability

CSCvj63107 Phone rebooted during active call due to java restart

CSCvj65574 Hourly logs files may be corrupted which hinders troubleshooting activity

CSCvj87057 Filled up messagequeue of pwrman thread may prevent 8821 from sleep/wakeup

CSCvj91058 playtone in asynchronization way will use up java heap memory

CSCvj91846 Java null pointer when viewing certificate webpage after upload user cert without private key

CSCvj92442 Unlock softkey missed after 8821 received Init:Services

CSCvj94600 Phone log cannot send to remote syslog server after DUT roaming success

CSCvj97176 Continuous DHCP_DISCOVER from 8821 phone

CSCvj99911 8821 log files can be duplicated between tar files.

CSCvk11147 when to show app, NullPointerException may be thrown

CSCvk13631 CP-8821 - ssl buffer limit exceeded

CSCvk33193 Softkeys not retained on XSI page after back from second page or end a call

CSCvk34280 After call or RTP session, Phone battery life lasts approx 24 hours

CSCvk38084 Problems with Exit and Back keys

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
| Cisco Wireless LAN Controller | 8.0.121.0 | 8.0.152.0, 8.2.170.0, 8.3.141.0, 8.5.135.0 |
| Cisco IOS Access Points (Autonomous) | 12.4(21a)JY | 12.4(25d)JA2, 15.2(4)JB6, 15.3(3)JF1 |
| Cisco Meraki | MR 25.9, MX 13.33 | MR 25.11, MX 13.33 |

| Note | If your Cisco Unified Communications Manager does not have the required device pack to support this firmware release, the
                                 firmware may not work correctly. |
|---|---|

| Step 1 | Go to the following URL: http://software.cisco.com/download/navigator.html?mdfid=284883944&i=rm |
|---|---|
| Step 2 | Choose Cisco IP Phone 8800 Series . |
| Step 3 | Choose Cisco Wireless IP Phone 8821 . |
| Step 4 | Choose Session Initiation Protocol (SIP) Software . |
| Step 5 | In the Latest Releases folder, choose 11.0(4)SR1 . |
| Step 6 | Select the firmware file, click the Download or Add to cart button, and follow the prompts. Firmware file: cmterm-8821-sip.11-0-4SR1-13.k3.cop.sgn Note If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. | Note | If you added the firmware file to the cart, click the Download Cart link when you are ready to download the file. |
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
| Step 4 | Choose 11.0(4)SR1 in the Latest Releases folder. |
| Step 5 | Click Download or Add to cart and follow the prompts. The file to download is cmterm-8821.11-0-4SR1-13.zip |
| Step 6 | Extract the files from the zip file, manually copy them to the Cisco Unified Communications Manager Express TFTP server (router
                                 flash), and enable them for TFTP. |

| Step 1 | Perform one of the following actions: Use this URL for all caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%284%29SR1&sb=anfr&bt=custV Use this URL for all open caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%284%29SR1&sb=afr&bt=custV Use this URL for all resolved caveats: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286308995&rls=11.0%284%29SR1&sb=fr&bt=custV |
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