---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-8800-firmware-11-1-2-p881-b-release-notes-for-8800mpp-110102-html-0666427bae
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/8800/firmware/11-1-2/p881_b_release_notes_for_8800mpp_110102.html
retrieved_at: 2026-08-21T13:45:13.146416+00:00
---

Cisco IP Phone 8800 Series with Multiplatform Firmware Release Notes for Firmware Release 11.1(2)

# Cisco IP Phone 8800 Series with Multiplatform Firmware Release Notes for Firmware Release 11.1(2)

### Download Options

Updated: May 14, 2018

First Published: May 14, 2018

# Cisco IP Phone 8800 Series with Multiplatform Firmware Release Notes for Firmware Release 11.1(2)

Use these release notes with the following Cisco IP Phone 8800 Series Multiplatform Phones running SIP Firmware Release 11.1(2).

Cisco IP Phone 8811, 8841, 8851, and 8861 Multiplatform Phones

Cisco IP Phone 8845 and 8865 Multiplatform Phones

The following table describes the individual phone requirements.

Phone

Support Server

Cisco IP Phone 8800 Series Multiplatform Phones

BroadSoft BroadWorks 22.0

MetaSphere CFS version 9.4

Asterisk 11.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone
                  	 8800 Series Documentation

See the publications that are specific to your language, phone model,
                        		  and multiplatform firmware release. Navigate from the following Uniform
                        		  Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-8800-series-multiplatform-firmware/index.html

## New and Changed Features

### Control Reverse Name Lookup

You can control the ability to display the caller name on the phone screen instead of the incoming or outgoing phone number.
                        You must configure either the LDAP Directory or the XML directory. You enable or disable the reverse name lookup using the
                        phone administration web page or by using XML provisioning.

Reverse name lookup is enabled by default.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### DHCP VLAN Options

You can add DHCP VLAN options for the voice VLAN of your phones. You configure a predefined DHCP option to learn the VLAN
                        ID.

The phone transfers the predefined DHCP option, such as option 132, using a DHCP request message in the existing VLAN. The
                        server to which the phone is connected, returns the voice VLAN ID. When the phone receives the voice VLAN ID, it releases
                        the IP address in the existing VLAN, switches to voice VLAN, and starts new DHCP settings.

The feature can be used when VLAN info is not available using CDP/LLDP and manual VLAN.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Emergency Call Support

You can register each IP-based phone with an emergency call service provider by supplying the E911 Geolocation information.
                        Registration obtains the phone's location. The location can specify the street address, building number, floor, room, and
                        other office location information. When you dial an emergency number, the emergency service receives the phone location and
                        a call-back number. If an emergency call disconnects, the emergency service uses the call-back number to reconnect to the
                        caller.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

### HTTPS Support for XSI Services

You can use the HTTPS protocol with the X/Open System Interface (XSI) services. When you add HTTPS:// in the XSI host server, the server uses the HTTPS protocol instead of the default HTTP protocol.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### LDAP over TLS

You can configure Lightweight Directory Access Protocol (LDAP) over Transport Layer Security (TLS), abbreviated LDAPS. LDAPS
                        uses TLS to secure communication between the LDAP clients and the LDAP servers.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

### Cisco Headset 500 Series

The Cisco Headset 531 and Cisco Headset 532 are two headsets that are developed for Cisco products and services. The 531 headset features a single earpiece, and offers
                        lightweight comfort. The 532 headset features two earpieces for use in a noisy environment or busy office.

RJ9 connector.

USB headset adapter with enhanced call control.

The Cisco Headset USB Adapter is available for use with the Cisco Headset 531 and 532. With the adapter, you can test your
                        headset, and customize your bass and treble, gain or microphone volume, and sidetone or feedback settings. The adapter also
                        retains your settings if you switch between phones.

The Cisco Headset 500 Series offers a more enhanced experience with:

In-call indicators: LED(s) on ear plate

Simplified call controls

Customized audio

The Cisco USB adapter is supported on Cisco IP Phone 8851, 8861, and 8865 with Multiplatform Firmware.

The Cisco Headset 531 and Cisco Headset 532 require Multiplatform Firmware Release 11.1(2) and later. Upgrade your phones to the latest firmware before using these headsets.

#### Where to Find More Information

Cisco IP Phone 8800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 8800 Series Multiplatform Phones User Guide

## Upgrade the Firmware

Cisco IP 8811, 8841, 8851, and 8861 Phones with Multiplatform Firmware (Audio only)

Cisco IP 8845 and 8865 Phones with Multiplatform Firmware (Video)

After the firmware upgrade completes, the phone reboots automatically.

Click the following URL:

https://software.cisco.com/download/home/286311392

Select IP Phone 8800 Series with Multiplatform Firmware in the middle pane.

Select your phone model (with Multiplatform Firmware) in the right pane.

Select the Multiplatform Firmware software type.

In the All Releases > MPPv11 folder, select 11.1.2 .

(Optional) Place your mouse pointer on the filename to display the file details and checksum values.

Download one of these files:

For the 8811, 8841, 8851, and 8861 cmterm-88xx.11-1-2MPP-351_REL.zip

For the 8845 and 8865 cmterm-8845_65.11-1-2MPP-351_REL.zip

Click Accept License Agreement when you accept the software license.

Unzip the firmware files.

Put the files in the TFTP, HTTP, or HTTPS download directory.

You can upgrade the phone firmware using either of the following methods:

Configure the Upgrade Rule on the Provisioning tab in the phone web page with the upgrade URL.

URL Format: <upgrade_protocol>://<serv_ip[:port]>/<filepath>/sipMMxx.RR-nnn.loads

Where the user input values are:

<upgrade_protocol> –HTTP, TFTP, or HTTPS.

<serv_ip[:port]> –Server IP address and optional port number.

<filepath> –File folder on the server that contains the firmware upgrade *.loads file.

MMxx –Cisco IP Phone MM Series with Multiplatform Firmware (for example, 68xx, 78xx, or 88xx)

or

MMxx –Cisco specific phone model (for example, 8845_65 or 7832)

RR –Major and minor release numbers (for example, 11-1-2 or 11-1-1SR1)

nnn –Build number (for example, 351)

Example using the Upgrade Rule for the Cisco IP 8811, 8841, 8851, and 8861 phones.

tftp://10.73.10.192/firmware/sip88xx.11-1-2MPP-351.loads

Provide a URL in a web browser that directs the call server to download the firmware to the phone.

URL Format: <phone_protocol>://<phone_ip[:port]>/admin/upgrade?

<upgrade_protocol>://<serv_ip[:port]>/<filepath>/sipMMxx.RR-nnn.loads

Where the user input values are:

<phone_protocol> –HTTP or HTTPS only.

<phone_ip[:port] –Phone IP address and optional port number.

<upgrade_protocol> –HTTP, TFTP, or HTTPS.

<serv_ip[:port]> –Server IP address and optional port number.

<filepath> –File folder on the server that contains the firmware upgrade *.loads file.

MMxx –Cisco IP Phone MM Series with Multiplatform Firmware (for example, 68xx, 78xx, or 88xx)

or

MMxx –Cisco specific phone model (for example, 8845_65 or 7832)

RR –Major and minor release numbers (for example, 11-1-2 or 11-1-1SR1)

nnn –Build number (for example, 351)

Example using the web browser URL for the Cisco IP 8845 and 8865 phones.

https://10.74.10.225/admin/upgrade?http//10.73.10.192/firmware/sip8845_65.11-1-2MPP-351.loads

Use the *.loads file in the URL. The *.zip file contains other files.

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

## Caveats

### View Caveats

You can search for caveats using the Cisco Bug Search tool.

Known caveats (bugs) are graded according to severity level, and can be either open or resolved.

Before you begin

#### Before you begin

To view the caveats, you need the following items:

Internet connection

Web browser

Cisco.com user ID and password

Perform one of the following actions:

To find all of the caveats for the 11.1.2 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&rls=11.1(2)&sb=anfr&bt=custV

To find all open caveats for the 11.1.2 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&rls=11.1(2)&sb=afr&bt=custV

To find all resolved caveats for the 11.1.2 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&rls=11.1(2)&sb=fr&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) To look for information about a specific problem, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 8800 Series Multiplatform Phones that use Firmware Release 11.1(2).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were open at the time this
                        report was compiled. For an updated view of the open defects or to view specific bugs, access the Bug Search Toolkit as described
                        in the View Caveats .

Some caveats only apply to specific Cisco IP Phone 8800 Series with Multiplatform Firmware phones. The list annotates these
                                    caveats using this example notation: [8845 and 8865 only] .

CSCvi30334 Phones fail to configure more than 21 key expansion module keys to SD+BLF with a 1000M switch. [8841 and 8851 only]

CSCvi31149 Phone switch from VLAN with IPv6 to VLAN without IPv6, unexpectedly, IPv6 status is still shown OK.

CSCvi36532 Key expansion module not powering up under special environment

CSCvi39946 Phone screen LCD can add maximum of 64 character voicemail description, but on a phone web page can only add 63
                              characters.

CSCvi40419 Phone cannot display the call forward logo set with the start codes (*72). [8845 and 8865 only]

CSCvi43542 Active call is held when quickly ending an incoming page.

CSCvi45913 No audio when the number of secure calls exceeds 50 and RTP port count is less than 100.

CSCvi45988 Pressing a digit hard key does not wake up the screen after receiving an XML file with PhoneExecute.

CSCvi47963 Phone still displays the missed call icon and shortcut, deletes the call history, after receiving an XML file.

CSCvi62072 Incoming paging cannot end when receiving two paging calls.

CSCvi64969 Phone connects to switch port which without configured any VLAN, it displays a duplicate IPv6 address message.

CSCvi67248 Phone displays connection successfully (DHCP pool full) when no IP address obtained on wireless.

CSCvi67452 Phone prompts with message Ethernet must be ... , which has no cable connected when you select Wi-Fi configure. [8845 and 8865 only]

CSCvi67535 Speak dial tone uses same volume with headset after ending a headset call (sharedline only).

CSCvi67698 User can input Extension Mobility (EM) sign-in password using special characters, without any limitation.

CSCvi67969 Sometimes the phone exits the Accessory Unsupported menu when you plug in a Cisco 531 or 532 headset.

CSCvi71664 The call ends if you press Return hard key and Cancel softkey after using an active DND with a star code.

CSCvi71678 In the Extension Mobility (EM) sign-in window, no response to phone screen LED if you insert a Cisco 531 or 532
                              headset and receive a shared line incoming call.

CSCvi71940 A paging call cannot end when you dial the second paging call using the Personal directory.

CSCvi72074 No ringtone setting works for a directory entry after you cancel the second incoming call.

CSCvi72138 Using the XML Directory service, phone always displays the first directory entry username when dialing an invalid
                              number.

CSCvi72223 Resync using autoconfig IPv6 IP address did not use DHCP IPv6 IP address. [8845 only]

CSCvi73581 Call failing when the TCP/TLS connection fails back to the primary server and does not register.

CSCvi76113 Cannot provision a phone from the phone web when the Upgrade Error Retry Delay is too short and the upgrade fails.

CSCvi76658 Line status PLK LED does not change to red when an in-dialog subscription fails.

CSCvi77714 An outgoing N-Way conference call is rolling over to extension 2.

CSCvi78340 When editing a call number, navigate to the left, then Return to the previous softkey page. Move right no longer
                              works.

CSCvi78547 Phone screen LCD has no response and web GUI cannot access. Caused by provisioning the phone with 1600 contacts
                              in an XML file.

CSCvi79560 Phone screen LCD: Incoming call page pops up frequently while using an electronic hookswitch (EHS) button init
                              call, phone connects BT or USB headset.

CSCvi80805 Report rule isn't sent occasionally.

CSCvi81189 Phone UI is stuck after configuring the XML service with 1600 contacts and having an invalid file format.

CSCvi81263 Password rule from LCD screen is not the same as on the phone web page.

CSCvi87525 Phone reboots when downloading a large profile and generates a PRT at same time.

CSCvi87566 Enable SCA Barge-In. Share line status does not change to Idle after successfully transferring the call.

CSCvi92212 Caller dual mode, SDP Preference set IPv6, callee IPv4 only, the call only has audio, but no video. [8845 and 8865 only]

CSCvi92270 Phone LCD displays error for some locales.

CSCvi92292 Paging icon disappears after navigating to the Display brightness menu on the LCD.

CSCvi94469 Press Speaker button to go onhook and dial tone still plays if sharedline re-syncs the DND or CFW.

CSCvi94869 DUT displays XML directory contact name after unparked through PLK.

CSCvi95028 LCD: Call forward first digit could be missed if user inputs a number very quickly.

CSCvi95569 TR69 ACS connection tear down happens before a command is posted.

CSCvi96421 Feature Key Sync is Yes, 88xx and 78xx phones have different behavior for the CFW setting.

CSCvi96613 USB headset cannot hear audio while Preferred audio device is set to Bluetooth and answering a call by softkey.

CSCvi96665 After phone receives paging call and the call is ended, no ringtone for a shared line incoming call.

CSCvi96666 Video secure call, secondary dialing stage, callee offhook, caller reboots. [8845 and 8865 only]

CSCvi96685 When preferred audio device is a speaker, phone always use the speaker to page.

CSCvi98839 The volume of speaker suddenly gets louder when you change the Control Timer Values to the maximum limit.

CSCvi98853 Change Startup delay value of the Ethernet configuration sometimes does not take effect.

CSCvi98881 LCD should not display Delete softkey when the screen focus is on the problem description under the Report Problem menu.

CSCvi99303 During a local conference, unexpected PrivaHold softkey displays when caller presses Conference before called phone answers.

CSCvi99398 Configure Paging Serv from yes to no or no to yes, the setting doesn't work until you reboot the phone.

CSCvi99736 Phone does not return to the front menu when save the settings of the corporate directory using the phone screen.

CSCvj06066 Sharedline call only has one-way audio when the two parties have different SIP & SDP preference modes.

CSCvj3115 PRT HTTPS Report Rule using a POST upload hangs up or becomes corrupted upon adding authentication.

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 8800 Series Multiplatform Phones that use Firmware Release 11.1(2).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). Register at Cisco.com to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                        this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                        as described in the View Caveats .

Some caveats only apply to specific Cisco IP Phone 8800 Series with Multiplatform Firmware phones. The list annotates these
                                    caveats using this notation: [8845 and 8865 only] .

CSCvg00958 Phone doesn't send 420 Bad Extension when it receives INVITE with an unsupported value.

CSCvg59538 No record in reboot reason when the reboot was triggered by VLAN change during the IPv6-only mode.

CSCvg81958 BLF does not light up RED for the phone.

CSCvg87077 BLF status fails with Shared Call Appearance.

CSCvg97169 Phone can perform a factory reset using the web GUI when a paging call is active.

CSCvg97235 Audio path switching fails during a paging call.

CSCvh12121 Phone reboots when input containing the host name and domain are at maximum character length in the web page.

CSCvh13736 Phone cannot choose the language when just modifying the d1 .

CSCvh14570 Phone reboots when input upgrade rule is at maximum character length in the web page.

CSCvh15538 Video path is not available on DUTA when DUTB exits the conference call early before DUTC answers.

CSCvh16152 First, MOS data is all zeroes. Second, phone should not send out this invalid data.

CSCvh16923 When making an AMR-WB call, coding mode cannot be changed for AMR-WB codec.

CSCvh17106 The packet capture by phone has an FCS error when the switch port has a voice VLAN configuration.

CSCvh46105 Phone uses wrong SIP SDP c line, when multiple m-lines exist, causing an audio issue.

CSCvh57718 The LDAP login phone recorded an account password on the phone log without encryption.

CSCvh61045 Custom Certificate Authority (CA) download provisioning status displays as failed, when is succeeded. [8845 only]

CSCvh61146 The phone cannot show Answer, Decline softkey when it received a new call. [8845 and 8865 only]

CSCvh62647 Define speed dial page does not display, when pressing the KEM softkey for an extended period. [8845 and 8865 only]

CSCvh66529 Phone reboots - Not handling the multipart/mixed and multipart/related MIME types properly.

CSCvh67018 Phone upgrade fails when receiving an HTTP 302 or 303 response.

CSCvh67088 Softkey disappears when you continually plug and unplug the Cisco 531 or 532 headset.

CSCvh67243 Speaker LED does not light when picking up a call.

DNS sequence does not work if you reconfigure the DNS order.

CSCvh72666 Phone cannot successfully register and repeatedly reboots with power adapter connected. [8845 and 8865 only]

CSCvh76496 Phone cannot get the correct content from an HTTP 301 response.

CSCvh76520 Phone always reports the download failed when receiving a 301 after reboot.

CSCvh76689 Phone cannot handle the correct content from an HTTP 302 response.

CSCvh77161 Call center Dispositioncode sent to the third-party server mis-matches the DispostionCode set.

CSCvh78148 Backlight does not turn off if set to 5 minutes or 30 minutes.

CSCvh78615 Static redundancy, phone keeps rebooting after setting a non-supported format for proxy.

CSCvh78788 Static A record format, still have DNS query after power cycle.

CSCvh80232 LKEM sometimes does not display speed dial name.

CSCvh80256 Call UI only has Hold and End call softkeys after the video is disabled. [8845 and 8865 only]

CSCvh80416 KEM Busy Lamp Field LCD GUI has a display problem.

CSCvh81045 Customer cannot dial '##' for feature activation.

CSCvh81658 Phone receive black video from VVX 500 after hold/resume. [8865 only]

CSCvh81785 The copyright of phone should be 2000-2018.

CSCvh82288 Phone web GUI displays KEM information after the KEM was disconnected.

CSCvh82317 Boundary issue: The maximum length of the phone BLF URI does not match the maximum character length of BLF URI
                              on the server.

CSCvh84244 Unplug the USB headset and the Accessories detail page still displays on the phone screen.

CSCvh86484 Get a resync from NTP server, however the time returned was incorrect.

CSCvh87513 XML App CiscoIPPhoneText is truncated at 100 characters.

CSCvh87790 Dual-mode phone should try to use the IPv4 address to upload PRT if no IPv6 address exists.

CSCvh90062 IPv6 HTTPS upgrade and download with domain name failure.

CSCvh91770 Phone reboots when receiving too many BLF messages. [8845 only]

CSCvh93677 Guest UI freezes while entering the Guest-In userId and when disconnecting the KEMs. [8845 and 8865 only]

CSCvh93697 UI stuck frozen and cannot receive or make a call. [8811 only]

CSCvh94566 Phone web GUI KEM information unit enable parameter displays no when you disconnect the KEM.

CSCvi01982 Phone taking longer to boot up after a factory reset or upgrade.

CSCvi15255 Phone language script only recognizes 9 language entries, rather than 19.

CSCvi17535 Extra Delete soft icon displays on the Attendant console preferences page. [8845 and 8865 only]

CSCvi20317 Call forward no answer doesn't work on line 2 when pressing *92 for Call Forward no answer activation code.

CSCvi20508 Mute LED is off when muting a paging call, after an incoming call.

CSCvi23087 Phone freezes when you repeatedly refresh the IM&P connection information on the LCD, until the phone web page
                              loses connection and phone does not restart.

CSCvi23108 Quickly press paging call sd twice; the second page dial window remains after phone goes offhook.

CSCvi24919 Phone restarts when add a long Voice Mail Number exceeding 912 characters.

CSCvi26086 No audible tone when using paging service.

CSCvi27880 Phone reboots after connecting 3 KEMs with one USB device.

CSCvi28162 For selection of input method window, plug in or disconnect the KEM yields no LED GUI response.

CSCvi28224 Extended Mobility (EM) signin returns success when profile rule uses an invalid domain; phone then cannot take
                              incoming call.

CSCvi28471 Phone reboots after pressing Call Park PLK when the sharedline seized the call.

CSCvi29841 PRT upload showing error for 20x responses.

CSCvi30306 Phone takes more than 30 seconds to display call window using a shared line and a phone in screensaver state.

CSCvi30474 Missing Recall: characters on the LCD; sometimes until the park time expires.

CSCvi32423 SIP stack mishandling Tel URL.

CSCvi32962 TR069 ACS URL https connection fails.

CSCvi33307 XSI directory service support over HTTPS.

CSCvi33480 Set backlight timer does not work.

CSCvi35080 KEM background does not turn off when the backlight timer times out.

CSCvi35223 Phone reboots (crashes) when attempting to process incorrect XML code.

CSCvi35670 Phone only checked password and ignored authorization ID although the Auth INVITE setting is Yes .

CSCvi35843 Phone status is incorrect when you press line key (for several seconds) to set SD on a shared line.

CSCvi36526 BLF subscription is not being sent.

CSCvi37888 Unpark call unsuccessful and phone line key mis-associated to call with special unpark operation.

CSCvi37924 Phone speaker LED does not go off when the phone ringing and having an incoming page, then ends the paging.

CSCvi39933 Missed call shortcut does not work on line 10.

CSCvi39937 Phone restarts when you input a long DN after pressing unpark softkey.

CSCvi40377 Extra backspace softkey can be seen under some menus.

CSCvi41035 TCP mode: phone goes offline during a secure call dialing timeout.

CSCvi45511 Set HTTP Report Method as PUT for Report Rule ; no HTTP packet sent out.

CSCvi51538 Wallpaper does not download and show right on the devices.

CSCvi54746 Fail to handle a long URL in a Custom Certificate Authority (CA) Rule.

CSCvi55311 Phone reboots when input upgrade rule is at maximum character length in the phone web page.

CSCvi59926 Phone restarts when save a long sd PLK.

CSCvi60428 Status of line 2 is incorrect after placing a paging number.

CSCvi63592 SIP subscribe messages are sending although the device is not registered.

CSCvi64922 On the phone LCD GUI, KEM hardware version display truncated, but the software version displays OK.

CSCvi65381 There is no audio in IPv6-only mode.

CSCvi65422 KEM not powering up and phone stuck.

CSCvi65651 Paging call priority 3 function doesn't work.

CSCvi68555 PRT upload failed; not supporting PRT URL with user information such as @ or [--uid ...] .

CSCvi68771 Device cannot dial ## when locale CW activated.

CSCvi69486 Device does not restart using phone admin menu.

CSCvi69493 No gateway information in INFORM TR69.

CSCvi69717 Phone continues to restart when all 16 PSKs have a maximum length name.

CSCvi71631 Phone speaker LED does not come on when phone ringtone has an incoming page; then suddenly ends the page.

CSCvi73894 Phone reboots when select server all call and has sharedline seize event at same time.

CSCvi74101 Fail to make SD through PLK at the second time in the Edit personal address entry window.

CSCvi74170 Phone reboots when use a very long profile URL to sync on the LCD GUI.

CSCvi74192 Phone reboots when phone registration fails and you dial a paging number.

CSCvi76399 Submit a maximum character length Picture Download URL , reboot the phone; phone keeps rebooting.

CSCvi76472 Phone reboots if you have an incoming call when animated spinner icon is running.

CSCvi81195 Phone reboots after configuring XML service with 1600 contacts.

CSCvi81266 Caller in dual mode, callee in IPv6-only mode, there is one-way audio after caller holds and resumes call with
                              callee.

CSCvi81278 Change startup delay to a large value and set LLDP-MED at same time; phone does not start up.

CSCvi81514 Phone restarts after pressing a maximum length sd unit key (for several seconds) and save it on the KEM.

CSCvi87602 Fail to change Display mode from phone LCD.

CSCvi88320 Wrong RTP port in SDP.

CSCvi88553 Failed to handle long XSI Login User ID.

CSCvi94568 You will hear sounds like "dididi" when receive a paging call after you activate Do Not Disturb (DND).

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Server |
|---|---|
| Cisco IP Phone 8800 Series Multiplatform Phones | BroadSoft BroadWorks 22.0 MetaSphere CFS version 9.4 Asterisk 11.0 |

| Step 1 | Click the following URL: https://software.cisco.com/download/home/286311392 |
|---|---|
| Step 2 | Select IP Phone 8800 Series with Multiplatform Firmware in the middle pane. |
| Step 3 | Select your phone model (with Multiplatform Firmware) in the right pane. |
| Step 4 | Select the Multiplatform Firmware software type. |
| Step 5 | In the All Releases > MPPv11 folder, select 11.1.2 . |
| Step 6 | (Optional) Place your mouse pointer on the filename to display the file details and checksum values. |
| Step 7 | Download one of these files: For the 8811, 8841, 8851, and 8861 cmterm-88xx.11-1-2MPP-351_REL.zip For the 8845 and 8865 cmterm-8845_65.11-1-2MPP-351_REL.zip |
| Step 8 | Click Accept License Agreement when you accept the software license. |
| Step 9 | Unzip the firmware files. |
| Step 10 | Put the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 11 | You can upgrade the phone firmware using either of the following methods: Configure the Upgrade Rule on the Provisioning tab in the phone web page with the upgrade URL. URL Format: <upgrade_protocol>://<serv_ip[:port]>/<filepath>/sipMMxx.RR-nnn.loads Where the user input values are: <upgrade_protocol> –HTTP, TFTP, or HTTPS. <serv_ip[:port]> –Server IP address and optional port number. <filepath> –File folder on the server that contains the firmware upgrade *.loads file. MMxx –Cisco IP Phone MM Series with Multiplatform Firmware (for example, 68xx, 78xx, or 88xx) or MMxx –Cisco specific phone model (for example, 8845_65 or 7832) RR –Major and minor release numbers (for example, 11-1-2 or 11-1-1SR1) nnn –Build number (for example, 351) Example using the Upgrade Rule for the Cisco IP 8811, 8841, 8851, and 8861 phones. tftp://10.73.10.192/firmware/sip88xx.11-1-2MPP-351.loads Provide a URL in a web browser that directs the call server to download the firmware to the phone. URL Format: <phone_protocol>://<phone_ip[:port]>/admin/upgrade? <upgrade_protocol>://<serv_ip[:port]>/<filepath>/sipMMxx.RR-nnn.loads Where the user input values are: <phone_protocol> –HTTP or HTTPS only. <phone_ip[:port] –Phone IP address and optional port number. <upgrade_protocol> –HTTP, TFTP, or HTTPS. <serv_ip[:port]> –Server IP address and optional port number. <filepath> –File folder on the server that contains the firmware upgrade *.loads file. MMxx –Cisco IP Phone MM Series with Multiplatform Firmware (for example, 68xx, 78xx, or 88xx) or MMxx –Cisco specific phone model (for example, 8845_65 or 7832) RR –Major and minor release numbers (for example, 11-1-2 or 11-1-1SR1) nnn –Build number (for example, 351) Example using the web browser URL for the Cisco IP 8845 and 8865 phones. https://10.74.10.225/admin/upgrade?http//10.73.10.192/firmware/sip8845_65.11-1-2MPP-351.loads Note Use the *.loads file in the URL. The *.zip file contains other files. | Note | Use the *.loads file in the URL. The *.zip file contains other files. |
| Note | Use the *.loads file in the URL. The *.zip file contains other files. |

| Note | Use the *.loads file in the URL. The *.zip file contains other files. |
|---|---|

| Step 1 | Perform one of the following actions: To find all of the caveats for the 11.1.2 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&rls=11.1(2)&sb=anfr&bt=custV To find all open caveats for the 11.1.2 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&rls=11.1(2)&sb=afr&bt=custV To find all resolved caveats for the 11.1.2 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286311392&rls=11.1(2)&sb=fr&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) To look for information about a specific problem, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |

| Note | Some caveats only apply to specific Cisco IP Phone 8800 Series with Multiplatform Firmware phones. The list annotates these
                                    caveats using this example notation: [8845 and 8865 only] . |
|---|---|

| Note | Some caveats only apply to specific Cisco IP Phone 8800 Series with Multiplatform Firmware phones. The list annotates these
                                    caveats using this notation: [8845 and 8865 only] . |
|---|---|