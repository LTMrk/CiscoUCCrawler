---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-7800-firmware-11-1-2-pa2d-b-7800-mpp-rn-1112-html-66f12237e9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/7800/firmware/11-1-2/pa2d_b_7800-mpp-rn-1112.html
retrieved_at: 2026-08-21T23:20:16.153767+00:00
---

Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(2)

# Cisco IP Phone 7800 Series Multiplatform Phones Release Notes for Firmware Release 11.1(2)

### Download Options

Updated: May 14, 2018

First Published: May 14, 2018

# Cisco IP Phone
            	 7800 Series Multiplatform Phones Release Notes for Firmware Release
            	 11.1(2)

Use these release
                  		  notes with the following Cisco IP Phone 7800 Series Multiplatform Phones running SIP Firmware Release 11.1(2).

Cisco IP Phone
                        				7811 Multiplatform Phones

Cisco IP Phone
                        				7821 Multiplatform Phones

Cisco IP Phone
                        				7841 Multiplatform Phones

Cisco IP Phone
                        				7861 Multiplatform Phones

The following
                  		  table describes the individual phone requirements.

Phone

Support
                              						Server

Cisco IP Phone 7800 Series Multiplatform Phones

BroadSoft BroadWorks 22.0

MetaSphere CFS version 9.4

Asterisk
                              						11.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone
                  	 7800 Series Documentation

See the
                        		  publications that are specific to your language, phone model, and multiplatform
                        		  firmware release. Navigate from the following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/products/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/index.html

## New and Changed Features

### Control Reverse
                  	 Name Lookup

You can control the ability to display the caller name on the phone screen instead of the incoming or outgoing phone number.
                        You must configure either the LDAP Directory or the XML directory. You enable or disable the reverse name lookup in the phone
                        administration web page or with xml provisioning. By default reverse name lookup is enabled.

#### Where to Find
                        		  More Information

Cisco IP Phone 7800 Series
                                 				  Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series Multiplatform Phones User Guide

### DHCP VLAN
                  	 Options

You can add DHCP
                        		  VLAN options for the voice VLAN of your phones. You configure a predefined DHCP
                        		  option to learn the VLAN ID.

The phone sends
                        		  the predefined DHCP option, such as option 132, as a DHCP request message in
                        		  the existing VLAN. The server to which the phone is connected, returns the
                        		  voice VLAN ID. When the phone receives the voice VLAN ID, it releases the IP
                        		  address in the existing VLAN, switches to voice VLAN, and starts new DHCP
                        		  settings.

The feature can
                        		  be used when VLAN info is not available by CDP/LLDP and manual VLAN.

#### Where to Find
                        		  More Information

Cisco IP Phone 7800 Series
                                 				  Multiplatform Phones Administration Guide

### Emergency 911
                  	 Support

You can register
                        		  each IP-based phone with an emergency call service provider by supplying the
                        		  E911 Geolocation information. Registration obtains the phone's location. The
                        		  location can specify the street address, building number, floor, room, and
                        		  other office location information. When you dial an emergency number, the
                        		  emergency service receives the phone location and a call-back number. If an
                        		  emergency call disconnects, the emergency service uses the call-back number to
                        		  reconnect to the caller.

#### Where to Find
                        		  More Information

Cisco IP Phone 7800 Series
                                 				  Multiplatform Phones Administration Guide

Cisco IP Phone 7800 Series
                                 				  Multiplatform Phones User Guide

### HTTPS Support in
                  	 XSI Host Server

You can enable HTTPs protocol for XSI service. When you add HTTPS:// in the XSI host server, the server uses HTTPS protocol instead of the default HTTP protocol.

#### Where to Find
                        		  More Information

Cisco IP Phone 7800 Series
                                 				  Multiplatform Phones Administration Guide

### LDAP over
                  	 TLS

You can configure
                        		  LDAP over TLS (LDAPS). LDAPS uses Transport Layer Security (TLS) to secure
                        		  communication between the Lightweight Directory Access Protocol (LDAP) clients
                        		  and the LDAP servers.

#### Where to Find
                        		  More Information

Cisco IP Phone 7800 Series
                                 				  Multiplatform Phones Administration Guide

## Upgrade the
               	 Firmware

The Cisco IP Conference Phone 7832 Multiplatform Phones have a different firmware image. For more information, see the Cisco IP Conference Phone 7832 Multiplatform Phones Release Notes for Firmware Release 11.1(2), at this URL:

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-7800-series-multiplatform-firmware/products-release-notes-list.html

The Cisco IP Phone 7800 Series Multiplatform Phones support a single image upgrade using TFTP, HTTP, or HTTPS.

After the firmware upgrade completes, the phone reboots automatically.

Click the
                              			 following URL:

https://software.cisco.com/download/navigator.html?mdfid=286311381

Select the IP Phone 7800 Series With Multiplatform Firmware in the middle pane.

Select your phone model in the right pane.

Select Multiplatform Firmware .

In the All Releases > MPPv11 folder, select 11.1.2 .

(Optional) Place your mouse pointer on the filename to display the file details and checksum values.

Download the cmterm-78xx.11-1-2MPP-351_REL.zip file.

Click Accept License Agreement when you accept the software license.

Unzip the files.

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

Example using the Upgrade Rule for the 7800 Series Multiplatform Phones.

tftp://10.73.10.192/firmware/sip78xx.11-1-2MPP-351.loads

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

Example using the web browser URL for the 7800 Series Multiplatform Phones.

https://10.74.10.225/admin/upgrade?http//10.73.10.192/firmware/sip78xx.11-1-2MPP-351.loads

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

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

### No Beep Sound Heard when the Mute Key is Pressed

When you press the Mute button during a call, you may not hear a beep sound. For anyone who is visually impaired, press the Mute button once to mute the phone and press the button twice to unmute the phone.

### Phone Has a Firmware Build Earlier than 11.0.0

Sometimes, a phone taken out of the box has a firmware build earlier than 11.0.0. When this happens, you must upgrade the
                        firmware on your phone to 11.0.0. Then you must update to 11.1.1 or later before you provision it.

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

To find all of the caveats for the 11.1.2 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=11.1(2)&sb=anfr&bt=custV

To find all open caveats for the 11.1.2 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=11.1(2)&sb=afr&bt=custV

To find all resolved caveats for the 11.1.2 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=11.1(2)&sb=fr&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) To look for information about a specific problem, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

### Open
                  	 Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 7800 Series Multiplatform Phones that use Firmware Release 11.1(2).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because a defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                        report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit as
                        described in the View Caveats .

CSCvi20892 Phone reboots when it has an incoming page call and maximum number calls.

CSCvi57576 Phone can only receive 5 calls but the phone screen GUI shows 8 calls.

CSCvi59903 Phone screen GUI displays Anonymous when changing the dial plan.

CSCvi88531 Different behavior of call status for shared conference bridge from private conference bridge.

CSCvi90594 Phone may un-register when switching between call history and personal directory.

CSCvi96787 Secure call one way-audio if the caller and callee's SDP support IP mode and use secondary dial steps.

CSCvi98838 Missing Back softkey when edit settings of the Enterprise Directory using the phone screen.

CSCvi99554 Secure call transfer, no audio if transferee and person transferring the call have different SIP & SDP preference
                              modes.

CSCvj01440 Setting the wrong static IP, GW, or DNS at same time does not overwrite the older phone configuration.

CSCvj3115 PRT HTTPS Report Rule using a POST upload hangs up or becomes corrupted upon adding authentication.

### Resolved
                  	 Caveats

The following list
                        		  contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 7800 Series Multiplatform Phones that use Firmware Release 11.1(2).

For more
                        		  information about an individual defect, you can access the online history for
                        		  the defect by accessing the Bug Search tool and entering the Identifier
                        		  ( CSCxxnnnnn ). You must be a registered Cisco.com user
                        		  to access this defect information.

Because a defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time this
                        report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit as
                        described in the View Caveats .

CSCvg91741 phone can't access the webpage with http protocal

CSCvh13875 Agent associating multiple call-center only shows one
                              				call-center's Queue Status

CSCvh19503 PC port mirror does not work on 78xx with switch voice
                              				vlan configured

CSCvh59168 LDAP directory name display issue

CSCvh67018 Phone upgrade fails when it receives 302 or 303 response.

CSCvh76496 Phone cannot get the correct content from an HTTP 301 response.

CSCvh76689 Phone cannot handle the content from an HTTP 302 response.

CSCvh90129 Phone reboots when you configure BLF only without mapped line key. [7811 only]

CSCvi28353 phone reboot when have long XML User Name or password

CSCvi30920 7811/7832: String "Show detail" is truncated on English
                              				US

CSCvi40614 7861 reboot just use last line to make a call

CSCvi79573 DUT failed to resync with multiple options

CSCvi88682 re-enter Server All calls or Enterprise Directory,
                              				Cancel, then phone reboots

CSCvi90186 should limit the "TOS/DiffServ Value" on web,if
                              				not,phone will keep rebooting with max length value

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support
                              						Server |
|---|---|
| Cisco IP Phone 7800 Series Multiplatform Phones | BroadSoft BroadWorks 22.0 MetaSphere CFS version 9.4 Asterisk
                              						11.0 |

| Step 1 | Click the
                              			 following URL: https://software.cisco.com/download/navigator.html?mdfid=286311381 |
|---|---|
| Step 2 | Select the IP Phone 7800 Series With Multiplatform Firmware in the middle pane. |
| Step 3 | Select your phone model in the right pane. |
| Step 4 | Select Multiplatform Firmware . |
| Step 5 | In the All Releases > MPPv11 folder, select 11.1.2 . |
| Step 6 | (Optional) Place your mouse pointer on the filename to display the file details and checksum values. |
| Step 7 | Download the cmterm-78xx.11-1-2MPP-351_REL.zip file. |
| Step 8 | Click Accept License Agreement when you accept the software license. |
| Step 9 | Unzip the files. |
| Step 10 | Put the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 11 | You can upgrade the phone firmware using either of the following methods: Configure the Upgrade Rule on the Provisioning tab in the phone web page with the upgrade URL. URL Format: <upgrade_protocol>://<serv_ip[:port]>/<filepath>/sipMMxx.RR-nnn.loads Where the user input values are: <upgrade_protocol> –HTTP, TFTP, or HTTPS. <serv_ip[:port]> –Server IP address and optional port number. <filepath> –File folder on the server that contains the firmware upgrade *.loads file. MMxx –Cisco IP Phone MM Series with Multiplatform Firmware (for example, 68xx, 78xx, or 88xx) or MMxx –Cisco specific phone model (for example, 8845_65 or 7832) RR –Major and minor release numbers (for example, 11-1-2 or 11-1-1SR1) nnn –Build number (for example, 351) Example using the Upgrade Rule for the 7800 Series Multiplatform Phones. tftp://10.73.10.192/firmware/sip78xx.11-1-2MPP-351.loads Provide a URL in a web browser that directs the call server to download the firmware to the phone. URL Format: <phone_protocol>://<phone_ip[:port]>/admin/upgrade? <upgrade_protocol>://<serv_ip[:port]>/<filepath>/sipMMxx.RR-nnn.loads Where the user input values are: <phone_protocol> –HTTP or HTTPS only. <phone_ip[:port] –Phone IP address and optional port number. <upgrade_protocol> –HTTP, TFTP, or HTTPS. <serv_ip[:port]> –Server IP address and optional port number. <filepath> –File folder on the server that contains the firmware upgrade *.loads file. MMxx –Cisco IP Phone MM Series with Multiplatform Firmware (for example, 68xx, 78xx, or 88xx) or MMxx –Cisco specific phone model (for example, 8845_65 or 7832) RR –Major and minor release numbers (for example, 11-1-2 or 11-1-1SR1) nnn –Build number (for example, 351) Example using the web browser URL for the 7800 Series Multiplatform Phones. https://10.74.10.225/admin/upgrade?http//10.73.10.192/firmware/sip78xx.11-1-2MPP-351.loads Note Use the *.loads file in the URL. The *.zip file contains other files. | Note | Use the *.loads file in the URL. The *.zip file contains other files. |
| Note | Use the *.loads file in the URL. The *.zip file contains other files. |

| Note | Use the *.loads file in the URL. The *.zip file contains other files. |
|---|---|

| Step 1 | Perform one of the following actions: To find all of the caveats for the 11.1.2 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=11.1(2)&sb=anfr&bt=custV To find all open caveats for the 11.1.2 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=11.1(2)&sb=afr&bt=custV To find all resolved caveats for the 11.1.2 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=284883944&rls=11.1(2)&sb=fr&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) To look for information about a specific problem, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |