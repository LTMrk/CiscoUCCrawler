---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-mpp-6800-firmware-11-2-1-p680-b-rn-1121-html-205fd80f6b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/MPP/6800/firmware/11-2-1/p680_b_rn-1121.html
retrieved_at: 2026-08-21T23:14:21.096481+00:00
---

Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 11.2(1)

# Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 11.2(1)

### Download Options

Updated: July 30, 2018

First Published: July 30, 2018

# Cisco IP Phone 6800 Series Multiplatform Phones Release Notes for Firmware Release 11.2(1)

Use these release notes with the following Cisco IP Phone 6800 Series Multiplatform Phones running SIP Firmware Release 11.2(1).

Cisco IP Phone 6841 and 6851 Multiplatform Phones

The following table describes the individual phone requirements.

Phone

Support Servers

Cisco IP Phone 6800 Series Multiplatform Phones

BroadSoft BroadWorks 22.0

MetaSphere CFS version 9.4

Asterisk 11.0

## Related
               	 Documentation

Use the following sections to obtain related information.

### Cisco IP Phone 6800 Series Documentation

See the publications that are specific to your language, phone model, and multiplatform firmware release. Navigate from the
                        following Uniform Resource Locator (URL):

https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/tsd-products-support-series-home.html

## New and Changed Features

### BroadWorks Anywhere

You can configure a phone to allow a call to seamlessly move from one desk phone or location to another mobile phone or desk
                        phone or location. The user can receive an incoming call from multiple locations. When you enable this feature, the user can
                        edit the locations list from the Anywhere menu on the phone screen.

You can enable this feature on the phone web page from Voice > Ext (n) > XSI Line Service .

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

### BroadWorks XSI Call Logs Display

You can enable the user to view local call logs or remote call logs recorded at the XSI server. When you enable the feature,
                        the user sees the Display recents from menu in the Recents list of the phone.

You can configure this feature on the phone web page from Voice > Phone > XSI Phone Service .

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

### Bypass the Set Password Screen

As a service provider, you can enable users to bypass the Set password screen on the first boot or after a factory reset.

The phone attempts to configure itself using DHCP or EDOS settings that can include a user password. The phone software waits
                        until the DHCP configuration completes and the EDOS configuration attempt completes, before it reads the phone configuration
                        file. If you set a user password in the phone configuration file, the Set password screen does not display.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Provisioning Guide

### BroadWorks XSI Caller ID Blocking

You can block the display of a phone's caller ID from the phone screen. When you enable this feature, the caller ID does not
                        display on the called phone when the user makes an outgoing call.

When you enable this feature, the Block caller id menu is displayed on the phone screen. This menu allows the user to block the phone's caller ID.

You can enable this feature on the phone web page from Voice > Ext(n) > XSI Line Service .

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

### EDOS Certificate and Encryption Enhancements

As a service provider, you can upload your root Certificate Authority (CA) file to the Cisco EDOS server. The formats supported
                        are: .pem, .cer, .cert, .crt.

When you upload your root certificate file to EDOS, the server provides a URL to the certificate. You use the URL as the Custom
                        CA URL when you configure devices.

As well, you can also select the encryption hash (MD5, SHA1, or SHA256) when Cisco signs your CSR. Cisco recommends that you
                        select SHA256, which provides the highest security.

#### Where to Find More Information

Cisco EDOS documentation and online help

Cisco IP Phone 6800 Series Multiplatform Phones Provisioning Guide

### Incoming Call Silence

You can configure an Ignore softkey on the phone that the user can press to silence an incoming call. The user presses the Ignore softkey or the Volume down button to silence the incoming call.

You can configure the softkey in the Programmable Softkeys area from Voice > Phone on the phone web page.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

### NAPTR Support

You use the Name Authority Pointer (NAPTR) to allow the phone to automatically determine and select the appropriate transport
                        protocol for the phone line.

As before, you can specify the transport protocol of your choice (UDP, TCP, or TLS) on the phone web page. You use the new
                        Auto option in the SIP transport field to enable the phone to automatically select the protocol.

You can configure the setting in the SIP Transport field from Voice > Ext(n) > SIP Settings on the phone web page.

When you configure the setting to Auto, the phone determines the transport protocol based on the Name Authority Pointer (NAPTR)
                        records on the DNS server. The phone uses the protocol specified in the record that has the lowest order and preference. When
                        there are multiple records with the same order and preference, the phone looks for a protocol within the records, in the following
                        order of preference: UDP, TCP, and TLS. The phone uses the highest priority protocol that it finds in a record.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

### New Domain Support while Provisioning

When a phone connects to a network for the first time or after a factory reset, if there are no DHCP options setup, it contacts
                        a device activation server for zero touch provisioning. Starting with this firmware release, phones will use activate.cisco.com instead of webapps.cisco.com for provisioning. Phones with older versions of the firmware will continue to use webapps.cisco.com . Cisco recommends that you allow both the domain names through your firewall.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Provisioning Guide

### Peer Firmware Sharing

You can enable Peer Firmware Sharing (PFS) when you want a phone to find other phones of the same model or series on the subnet
                        and share updated firmware files. The phones are organized into a hierarchy using Cisco Peer-to-Peer-Distribution Protocol
                        (CPPDP), which is a Cisco proprietary protocol. One of the phones in that hierarchy acts as a root phone. The root phone downloads
                        the firmware image from the load server and then transfers the firmware to other phones in the hierarchy.

You can configure this feature on the phone web page from Voice > Provisioning > Firmware Upgrade .

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

### Phone Menu Access Control

You can restrict the access to the phone menus and options on the phone screen by configuring the provisioning file. The configurations
                        take effect when the parameter Phone-UI-User-Mode (in the Voice > System > System Configuration section) is Yes.

When an element is designated with ua= "na" , users don't see the Settings menu on the phone screen.

When an element is designated with ua= "ro" , users can see the Settings menu on the phone screen, but can't change the settings.

When an element is designated with ua= "rw" , users can see the Settings menu and change the settings on the phone screen.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

### Privacy Header Configuration

Privacy header configuration protects user privacy. You can specify the level of user privacy within your trust network. The
                        levels available are: Disabled (default), none, header, session, user, and id.

You use the administration phone web page or add XML tags to the config.xml provisioning file. You can set each of the 10 phone line extensions to send out a specific privacy header and request user
                        privacy needs in the SIP messages.

You can configure the privacy header on the phone web page from Voice > Ext(n) > SIP Settings .

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

### Profile Account for 401 HTTP Authentication Error

Users can now quickly and easily collect authentication information used for provisioning when the phone receives HTTP or
                        HTTPS 401 authentication response. When this error occurs, the Profile Accounts Setup screen is displayed on the phone, and users can collect their user ID and password for the phone to resynchronize.

You can enable this feature in the Configuration Profile area from Voice > Provisioning on the phone web page.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

### Ringtone Menu Change

Your user can access the Ringtone menu under the User preferences screen to change the ringtones of the phone.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

### Screen Saver Type without Lock Option

You can only add three types of screen saver: Clock , Logo , and Download Picture . Support for "lock" as one of the screen saver type is removed now.

If the user configures screen saver type to lock with TR069 and config file, the screen saver type default is set to Clock .

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

Cisco IP Phone 6800 Series Multiplatform Phones User Guide

### SIP Message Blocking from a Non-Proxy Device

The phone can now silently block or ignore any Session Initiation Protocol (SIP) messages from a non-proxy device. When the
                        phone discards such messages, the user does not see any notifications on the phone screen. You can enable or disable this
                        feature by changing the values in the Block Nonproxy SIP field from the phone web page or from xml provisioning.

Set Block Nonproxy SIP to No for phones that use TCP or TLS to transport SIP messages. Nonproxy SIP messages transported over TCP or TLS are blocked
                        by default.

When non-proxy messages are blocked, the phone only accepts SIP messages from:

proxy server

outbound proxy server

alternative proxy server

alternative outbound proxy server

IN-Dialog message from both proxy and non-proxy device. For example, Call session dialog and Subscribe dialog.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

### TR-069 Provisioning Enhancements

If you use TR-069 to configure the phones, the list of parameters available is extended. This feature ensures that you can
                        manage phone devices in your network with Auto Configuration Server (ACS), instead of an XML provisioning server.

#### Where to Find More Information

Cisco IP Phone 6800 Series Multiplatform Phones Administration Guide

## Upgrade the Firmware

The Cisco IP Phone 6800 Series Multiplatform Phones support a single image upgrade using the TFTP, HTTP, or HTTPS protocols with a URL.

After the firmware upgrade completes, the phone reboots automatically.

Click the following URL:

https://software.cisco.com/download/navigator.html?mdfid=286318380&i=rm

Choose IP Phone 6800 Series with Multiplatform Firmware in the middle pane.

Choose your phone model in the right pane.

Choose the Multiplatform Firmware software type.

In the All Releases > MPPv11 folder, select 11.2.1 .

(Optional) Place your mouse pointer on the filename to display the file details and checksum values.

Download the cmterm-68xx.11-2-1MPP-630_REL.zip file.

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

Example using the Upgrade Rule for the 6800 Series Multiplatform Phones.

tftp://10.73.10.192/firmware/sip68xx.11-2-1MPP-630.loads

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

Example using the web browser URL for the 6800 Series Multiplatform Phones.

https://10.74.10.225/admin/upgrade?http//10.73.10.192/firmware/sip68xx.11-2-1MPP-630.loads

Use the *.loads file in the URL. The *.zip file contains other files.

## Limitations and Restrictions

### Phone Behavior
                  	 During Times of Network Congestion

Anything that degrades network performance can affect phone voice and video quality, and in some cases, can cause a call
                        to drop. Sources of network degradation can include, but are not limited to, the following activities:

Administrative
                              				tasks, such as an internal port scan or security scan

Attacks that
                              				occur on your network, such as a Denial of Service attack

### Caller Identification and Other Phone Functions

Caller identification or other phone functions have not been verified with third-party applications for the visually or hearing
                        impaired.

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

To find all of the caveats for the 11.2.1 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.2(1)&sb=anfr&bt=custV

To find all open caveats for the 11.2.1 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.2(1)&sb=afr&bt=custV

To find all resolved caveats for the 11.2.1 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.2(1)&sb=fr&bt=custV

When prompted, log in with your Cisco.com user ID and password.

(Optional) To look for information about a specific problem, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter .

### Open Caveats

The following list contains the severity 1, 2, and 3 defects that are open for the Cisco IP Phone 6800 Series Multiplatform Phones that use Firmware Release 11.2(1).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                        this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                        as described in the View Caveats .

CSCvi81457 web-gui and lcd-gui display wrong ipv4 gateway when dhcpv4 server is disabled from enabled

CSCvi81805 web-gui and lcd-gui displays wrong ipv6 prefix length

CSCvi90086 BLF doesn't work when BLF List URI is xxxxx@ipv6_addr under ipv6 only mode

CSCvk22456 JPN: lcd_gui: "Failed to get XSI settings. DNS error" is not localized

### Resolved Caveats

The following list contains the severity 1, 2, and 3 defects that are resolved for the Cisco IP Phone 6800 Series Multiplatform Phones that use Firmware Release 11.2(1).

For more information about an individual defect, you can access the online history for the defect by accessing the Bug Search
                        tool and entering the Identifier ( CSCxxnnnnn ). You must be a registered Cisco.com user to access this defect information.

Because the defect status continually changes, the list reflects a snapshot of the defects that were resolved at the time
                        this report was compiled. For an updated view of the resolved defects or to view specific bugs, access the Bug Search Toolkit
                        as described in the View Caveats .

CSCvf61571 68xx: Power saver doesn't work

CSCvf62642 68xx: 802.1X do not work normally

CSCvf64140 68xx: FW upgrade can't continue after plug out/in network cable while DUT FW upgrate in progress

CSCvf68983 68xx Device backlight doesn't work

CSCvf76679 68xx: Contrast level can't be set to 1

CSCvf82957 68xx: Hardcode PC Port,the switch/port port config don't have the opinion "1000M full"

CSCvf90731 68xx: Wrong upgrade status displayed in phone webpage

CSCvf92265 68xx: WEB GUI current Time will earlier one hour if manual setting time on DUT LCD-GUI

CSCvf99407 68xx: http authentication fail after changing user id

CSCvg01372 68xx:Right hardware macro condition should not triggered by resync rule

CSCvg35997 Can config min rtp-port bigger than max prt-port in web-gui

CSCvg41909 phone can't call out with speed dial if the format is DN@IP (ip is ipv6 address)

CSCvg45977 factory reset phone,change phone volume,the first time report delta is incorrect

CSCvg47432 phone will use speaker when the second call using speed dial

CSCvg63336 Multiple Vulnerabilities in glibc

CSCvg65520 when change the voice vlan of switch port,phone can't show the ipv4 information in lcd-gui

CSCvh78242 Phone not record name on call history by using LDAP Reverse name lookup when call not succeed

CSCvi35149 Phone ui will stuck if restart it with KEM connected

CSCvi52671 phone can't upgrade with ipv6 address

CSCvi87716 UI displays Anonymous call and this call won't exit after one conference call isn't setup successful

CSCvj43637 ML_MPP: phone not response with ccapi or web except telnet after many stress case

CSCvk15839 Press Set softkey can not change "Block caller ID" value

CSCvk16565 68xx-3PCC: Cannot make outbound calls

CSCvk39385 68xx: TelephoneEvent is not added

## Cisco IP Phone
               	 Firmware Support Policy

For information on the support policy for phones, see https://cisco.com/go/phonefirmwaresupport .

| Phone | Support Servers |
|---|---|
| Cisco IP Phone 6800 Series Multiplatform Phones | BroadSoft BroadWorks 22.0 MetaSphere CFS version 9.4 Asterisk 11.0 |

| Step 1 | Click the following URL: https://software.cisco.com/download/navigator.html?mdfid=286318380&i=rm |
|---|---|
| Step 2 | Choose IP Phone 6800 Series with Multiplatform Firmware in the middle pane. |
| Step 3 | Choose your phone model in the right pane. |
| Step 4 | Choose the Multiplatform Firmware software type. |
| Step 5 | In the All Releases > MPPv11 folder, select 11.2.1 . |
| Step 6 | (Optional) Place your mouse pointer on the filename to display the file details and checksum values. |
| Step 7 | Download the cmterm-68xx.11-2-1MPP-630_REL.zip file. |
| Step 8 | Click Accept License Agreement when you accept the software license. |
| Step 9 | Unzip the firmware files. |
| Step 10 | Put the files in the TFTP, HTTP, or HTTPS download directory. |
| Step 11 | You can upgrade the phone firmware using either of the following methods: Configure the Upgrade Rule on the Provisioning tab in the phone web page with the upgrade URL. URL Format: <upgrade_protocol>://<serv_ip[:port]>/<filepath>/sipMMxx.RR-nnn.loads Where the user input values are: <upgrade_protocol> –HTTP, TFTP, or HTTPS. <serv_ip[:port]> –Server IP address and optional port number. <filepath> –File folder on the server that contains the firmware upgrade *.loads file. MMxx –Cisco IP Phone MM Series with Multiplatform Firmware (for example, 68xx, 78xx, or 88xx) or MMxx –Cisco specific phone model (for example, 8845_65 or 7832) RR –Major and minor release numbers (for example, 11-1-2 or 11-1-1SR1) nnn –Build number (for example, 351) Example using the Upgrade Rule for the 6800 Series Multiplatform Phones. tftp://10.73.10.192/firmware/sip68xx.11-2-1MPP-630.loads Provide a URL in a web browser that directs the call server to download the firmware to the phone. URL Format: <phone_protocol>://<phone_ip[:port]>/admin/upgrade? <upgrade_protocol>://<serv_ip[:port]>/<filepath>/sipMMxx.RR-nnn.loads Where the user input values are: <phone_protocol> –HTTP or HTTPS only. <phone_ip[:port] –Phone IP address and optional port number. <upgrade_protocol> –HTTP, TFTP, or HTTPS. <serv_ip[:port]> –Server IP address and optional port number. <filepath> –File folder on the server that contains the firmware upgrade *.loads file. MMxx –Cisco IP Phone MM Series with Multiplatform Firmware (for example, 68xx, 78xx, or 88xx) or MMxx –Cisco specific phone model (for example, 8845_65 or 7832) RR –Major and minor release numbers (for example, 11-1-2 or 11-1-1SR1) nnn –Build number (for example, 351) Example using the web browser URL for the 6800 Series Multiplatform Phones. https://10.74.10.225/admin/upgrade?http//10.73.10.192/firmware/sip68xx.11-2-1MPP-630.loads Note Use the *.loads file in the URL. The *.zip file contains other files. | Note | Use the *.loads file in the URL. The *.zip file contains other files. |
| Note | Use the *.loads file in the URL. The *.zip file contains other files. |

| Note | Use the *.loads file in the URL. The *.zip file contains other files. |
|---|---|

| Step 1 | Perform one of the following actions: To find all of the caveats for the 11.2.1 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.2(1)&sb=anfr&bt=custV To find all open caveats for the 11.2.1 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.2(1)&sb=afr&bt=custV To find all resolved caveats for the 11.2.1 release, use this URL: https://bst.cloudapps.cisco.com/bugsearch/search?kw=*&pf=prdNm&pfVal=286318380&rls=11.2(1)&sb=fr&bt=custV |
|---|---|
| Step 2 | When prompted, log in with your Cisco.com user ID and password. |
| Step 3 | (Optional) To look for information about a specific problem, enter the bug ID number ( CSCxxnnnnn ) in the Search for field, and press Enter . |