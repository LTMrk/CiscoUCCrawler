---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8831-3pcc-english-9-3-4-admin-guide-8831-3pcc-ag-field-reference-html-a71fb1f61e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8831/3PCC/english/9_3_4/admin-guide/8831-3pcc-ag/field-reference.html
retrieved_at: 2026-08-21T02:09:44.022892+00:00
---

Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

# Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Administration Guide, Release 9.3(4)

Updated: October 22, 2014

Chapter: Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Field Reference

## Chapter: Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Field Reference

## Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Field Reference

This appendix describes the fields in the following sections (tabs) of the phone web user interface:

## Info

The fields on this tab are read-only and cannot be edited.

### System Status

### System Information

Connection Type

Indicates the type of internet connection for the phone:

- DHCP

- Static IP

Current IP

Displays the current IP address assigned to the IP phone.

Host Name

Displays the current host name assigned to the phone.

Domain

Displays the network domain name of the phone.

Defaults to cisco.com.

Current Netmask

Displays the network mask assigned to the phone.

DNS from DHCP

Displays the IP address assigned by DHCP server.

Primary DNS

Displays the primary DNS server assigned to the phone.

Current Gateway

Displays the default router assigned to the phone.

Secondary DNS

Displays the secondary DNS server assigned to the phone.

### Reboot History

The conference phone stores the reasons for the last five reboots or refreshes. When the phone is reset to factory defaults, this information is deleted.

The reboot history is displayed in reverse chronological order, with the reasons for the latest reboot displayed in the Reboot Reason 1 field.

Each Reboot Reason field displays the reason for the reboot and a time stamp indicating when the reboot took place as in the following examples:

The following is a list of the supported reboot/refresh reasons:

Upgrade

An upgrade operation caused a reboot (regardless whether the upgrade completed or failed).

Provisioning

Changes made to parameter values by using the phone LCD or Web GUI, or a resync caused a reboot.

SIP Triggered

A SIP request caused a reboot.

RC

A remote customization caused a reboot.

User Triggered

The user manually triggered a cold reboot.

IP Changed

The phone IP address was changed triggering a warm reboot.

You can view the reboot history from the phone Web GUI, and the phone Status Dump file (http:// phoneIP /status.xml or http:// phoneIP /admin/status.xml).

### Viewing the Reboot History in the Status Dump File

The reboot history is stored in the Status Dump file (http:// <phone_IP_address> /admin/status.xml). In this file, tags Reboot_Reason_1 to Reboot_Reason_3 store the reboot history, as shown in this example:

The Web GUI and the LCD screen get the reboot history from these tags.

### Product Information

Product Name

Model number of the conference phone.

Software Version

Version number of the conference phone software.

MAC Address

Hardware address of the conference phone.

Customization

For an RC unit, this field indicates whether the unit has been customized or not. Pending indicates a new RC unit that is ready for provisioning. If the unit has already retrieved its customized profile, this field displays the name of the company that provisioned the unit.

Serial Number

Serial number of the conference phone.

Hardware Version

Version number of the conference phone hardware.

Client Certificate

Status of the client certificate, which authenticates the conference phone for use in the ITSP network. This field indicates if the client certificate is properly installed in the phone.

Wireless Microphone Region

Wireless microphone region of the conference phone.

### Phone Status

Current Time

Current date and time of the system; for example, 08/06/14 1:42:56 a.m.

Elapsed Time

Total time elapsed since the last reboot of the system; for example, 7 days, 02:13:02.

Operational VLAN ID

ID of the VLAN currently in use if applicable.

SW Port

Displays the type of Ethernet connection from the IP phone to the switch.

### Call Status

### Ext Status

The following parameters show for each extension on the phone.

Registration State

Shows “Registered” if the phone is registered, “Not Registered” if the phone is not registered to the ITSP.

Last Registration At

Last date and time the line was registered.

Next Registration In

Number of seconds before the next registration renewal.

Mapped SIP Port

Port number of the SIP port mapped by NAT.

### Call 1 Status/Call 2 Status

The following parameters show for each line and call on the phone.

Call State

Status of the call.

Duration

Duration of the call.

Remote Address

Address of the remote device.

Local Address

Address of the local device.

Start Time

Starting time of the call

Type

Direction of the call.

Peer Name

Name of the internal phone.

Peer Phone

Phone number of the internal phone.

Sender Packets

Number of RTP voice packets transmitted since voice stream was opened.

Note This number is not necessarily identical to the number of RTP voice packets transmitted since the call began because the call might have been placed on hold.

Sender Octets

Total number of octets sent by the phone.

Sender Codec

Type of voice stream transmitted (RTP streaming audio from codec): G.729, iLBC, G.711 u-law, or G.711 A-law.

Rcvr Lost Packets

Missing RTP packets (lost in transit.)

Avg Jitter

Estimated average RTP packet jitter (dynamic delay that a packet encounters when going through the network) observed since the receiving voice stream was opened.

Rcvr Codec

Type of voice stream received (RTP streaming audio from codec): G.729, iLBC, G.711 u-law, or G.711 A-law.

Rcvr Packets

Number of RTP voice packets received since voice stream was opened.

Note This number is not necessarily identical to the number of RTP voice packets received since the call began because the call might have been placed on hold

Rcvr Octets

Total number of octets received by the phone.

MOS-LQK

Score that is an objective estimate of the mean opinion score (MOS) for listening quality (LQK) that rates from 5 (excellent) to 1 (bad). This score is based on audible concealment events due to frame loss in the preceding 8-second interval of the voice stream.

Note The MOS LQK score can vary based on the type of codec that the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control uses.

AVG MOS LQK

Average MOS LQK score observed for the entire voice stream.

Min MOS LQK

Lowest MOS LQK score observed from start of the voice stream.

Max MOS LQK

Baseline or highest MOS LQK score observed from start of the voice stream.

These codecs provide the following maximum MOS LQK score under normal conditions with no frame loss:

- G.711 gives 4.5

- G.722 gives 4.5

- G.729 A /AB gives 3.7

- iLBC gives 3.9

MOS LQK Version

Version of the Cisco proprietary algorithm used to calculate MOS LQK scores

Cumulative Conceal Ratio

Total number of concealment frames divided by total number of speech frames received from start of the voice stream.

Interval Conceal Ratio

Ratio of concealment frames to speech frames in preceding 3-second interval of active speech. If using voice activity detection (VAD), a longer interval might be required to accumulate 3 seconds of active speech.

Max Conceal Ratio

Highest interval concealment ratio from start of the voice stream.

Conceal Secs:

Number of seconds that have concealment events (lost frames) from the start of the voice stream (includes severely concealed seconds).

Severely Conceal Secs

Number of seconds that have more than 5 percent concealment events (lost frames) from the start of the voice stream.

Latency

Number of milliseconds for latency.

Max Jitter

Number of milliseconds for receiver jitter.

Rcvr Discarded

Number of RTP packets in the receiving voice stream that have been discarded (bad packets, too late, and so on).

Note The phone will discard payload type 19 comfort noise packets that are generated by Cisco Gateways, which will increment this counter.

### Download Status

### Downloaded Ring Tone

Ring Tone Download Status

Indicates whether the phone is downloading a ring tone (and from where) or if it is idle.

Ring Tone 1

Information about the user downloaded ring tone 1: name, size, and time-stamp of the tone.

Ring Tone 2

Information about the user downloaded ring tone 2: name, size, and time-stamp of the tone.

### Downloaded Locale Package

Locale Download Status

Displays the downloaded locale package status.

Downloaded Dictionary Info

Dictionary downloaded from the TFTP/HTTP provisioning server indicated in the phone.

Downloaded Font Info

Displays the downloaded font name.

### Firmware Upgrade Status

Firmware Upgrade Status 1

Displays the upgrade status (failed or succeeded) with reason for the same.

Firmware Upgrade Status 2

Firmware Upgrade Status 3

### Provisioning Status

Provisioning Status 1

Displays the provisioning status (resync) of the phone.

Provisioning Status 2

Provisioning Status 3

Note The Upgrade and Provisioning Status are displayed in reverse chronological order (like reboot history) displaying status with time and reason.

### Custom CA Status

These fields display the status of provisioning using a custom Certificate Authority (CA).

Custom CA Provisioning Status

Indicates whether provisioning using a custom CA succeeded or failed:

- Last provisioning succeeded on mm/dd/yyyy HH:MM:SS; or

- Last provisioning failed on mm/dd/yyyy HH:MM:SS

Custom CA Info

Displays information about the custom CA:

- Installed—Displays the “CN Value,” where “CN Value” is the value of the CN parameter for the Subject field in the first certificate.

- Not Installed—Displays if no custom CA certificate is installed.

Custom CA certificates are configured in the Provisioning tab. For more information about custom CA certificates, see the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Provisioning Guide .

### Debug Info

### Console Logs

Displays the syslog output of the phone in the reverse order, where messages is the latest one. Includes hyperlinks to individual log files. The console log files include debug and error messages received on the phone.

l

Debug Message 0

messages

Debug Message 1

messages.0

Debug Message 2

messages.1

Debug Message 3

messages.2

Debug Message 4

messages.3

Debug Message 5

messages.4

Debug Message 6

messages.5

Debug Message 7

messages.6

Debug Message 8

messages.7

### Browser Info

Loading Time

The amount of elapsed time when the page is loaded on the browser.

Note Safari and IE version before 9 does not support this parameter.

Browser Version

Version of the browser. For example, Firefox 31

OS Version

Version of the Windows operating system.

Platform

The platform to which the browser is compiled.

Width

Current width of the browser.

Height

Current height of the browser.

## Voice

### System

### System Configuration

Restricted Access Domains

This feature is used when implementing software customization.

Enable Web Server

Enable/disable web server of the IP phone.

Defaults to Yes.

Web Server Port

Port number of the phone web user interface.

Defaults to 80.

Enable Web Admin Access

Lets you enable or disable local access to the phone web user interface. Select Yes or No from the drop-down menu.

Defaults to Yes.

Admin Password

Password for the administrator.

Defaults to no password.

User Password

Password for the user.

Defaults to blank.

Phone-UI-User-Mode

Allows you to restrict the menus and options that phone users see when they use the phone interface. Choose yes to enable this parameter and restrict access. The default is no.

Specific parameters are then designated as “na” or “ro” using provisioning files. Parameters designated as “na” will not appear on the phone interface. Parameters designated as “ro” will not be editable by the user.

### Internet Connection Type

Connection Type

Choose the type of internet connection:

###### DHCP

###### Static IP

### Static IP Settings

Static IP

If static IP was chosen as the type of internet connection, displays the static IP address assigned to the phone.

Netmask

If static IP was chosen as the type.

Gateway

Default router IP address. Blank if DHCP assigned.

### Optional Network Configuration

Host Name

The host name of the conference phone.

Domain

The network domain of the conference phone.

Primary DNS

DNS server used by the conference phone in addition to DHCP supplied DNS servers if DHCP is enabled; when DHCP is disabled, this is the primary DNS server.

Defaults to 0.0.0.0.

Secondary DNS

DNS server used by the conference phone in addition to DHCP supplied DNS servers if DHCP is enabled; when DHCP is disabled, this is the secondary DNS server.

Defaults to 0.0.0.0.

Syslog Server

Specify the syslog server name and port. This feature specifies the server for logging IP phone system information and critical events. If both Debug Server and Syslog Server are specified, Syslog messages are also logged to the Debug Server.

Debug Level

The debug level from 0-3. The higher the level, the more debug information is generated. Zero (0) means no debug information is generated. To log SIP messages, you must set the Debug Level to at least 2.

Defaults to 0.

Layer 2 Logging

Used for IP phone network layer debugging purposes. Do not use except when advised to do so by Cisco technical support, as this may impact system performance. Set to No by default.

Primary NTP Server

IP address or name of primary NTP server.

Secondary NTP Server

IP address or name of secondary NTP server.

SSH Access

If enabled, the phone supports console access for debugging and testing.

DNS Cache TTL Ignore

If enabled, the phone continues to use the previous cached DNS result if the DNS server does not respond when the phone tries to renew its DNS query.

When disabled, the phone uses the previous TTL value and clears the DNS query result cache.

SSH User ID

User ID for SSH login.

SSH Password

Password for the SSH login.

### VLAN Settings

Enable CDP

Enable CDP only if you are using a switch that has Cisco Discovery Protocol. CDP is negotiation based and determines which VLAN the IP phone resides in.

Enable LLDP-MED

Choose Yes to enable LLDP-MED for the phone to advertise itself to devices that use that discovery protocol.

When the LLDP-MED feature is enabled, after the phone has initialized and Layer 2 connectivity is established, the phone sends out LLDP-MED PDU frames. If the phone receives no acknowledgment, the manually configured VLAN or default VLAN will be used if applicable. If the CDP is used concurrently, the waiting period of 6 seconds is used. The waiting period will increase the overall startup time for the phone.

Network Startup Delay

Setting this value causes a delay for the switch to get to the forwarding state before the phone will send out the first LLDP-MED packet. The default delay is 3 seconds. For configuration of some switches, you might need to increase this value to a higher value for LLDP-MED to work. Configuring a delay can be important for networks that use Spanning Tree Protocol.

VLAN ID

If you use a VLAN without CDP (VLAN enabled and CDP disabled), enter a VLAN ID for the IP phone. Note that only voice packets are tagged with the VLAN ID. Do not use 1 for the VLAN ID.

### Inventory Settings

Asset ID

Provides the ability to enter an asset ID for inventory management when using LLDP-MED. The default value for Asset ID is empty. Enter a string of less than 32 characters if you are using this field.

The Asset ID can be provisioned only by using the web management interface or remote provisioning. The Asset ID is not displayed on the phone screen.

Changing the Asset ID field causes the phone to reboot.

### SIP

### SIP Parameters

Max Forward

SIP Max Forward value, which can range from 1 to 255.

Defaults to 70.

Max Redirection

Number of times an invite can be redirected to avoid an infinite loop.

Defaults to 5.

SIP User Agent Name

Used in outbound REGISTER requests.

Defaults to $VERSION. If empty, the header is not included. Macro expansion of $A to $D corresponding to GPP_A to GPP_D allowed

SIP Server Name

Server header used in responses to inbound responses.

Defaults to $VERSION.

SIP Reg User Agent Name

User-Agent name to be used in a REGISTER request. If this is not specified, the <SIP User Agent Name> is also used for the REGISTER request.

Defaults to blank.

SIP Accept Language

Accept-Language header used. To access, click the SIP tab, and fill in the SIP Accept Language field.

There is no default. If empty, the header is not included.

RFC 2543 Call Hold

If set to yes, unit will include c=0.0.0.0 syntax in SDP when sending a SIP re-INVITE to the peer to hold the call. If set to no, unit will not include the c=0.0.0.0 syntax in the SDP. The unit will always include a=sendonly syntax in the SDP in either case.

Defaults to Yes.

SIP TCP Port Min

Specifies the lowest TCP port number that can be used for SIP sessions. Defaults to 5060.

SIP TCP Port Max

Specifies the highest TCP port number that can be used for SIP sessions. Defaults to 5080.

Caller ID Header

Provides the option to take the caller ID from PAID-RPID-FROM, P-ASSERTEDIDENTITY, REMOTE-PARTY-ID, or FROM header.

Max INVITE Retry Attempts

Maximum number of INVITE retry attempts by the phone.

Defaults to 6.

Max NON-INVITE Retry Attempts

Maximum number of NON-INVITE retry attempts by the phone.

Defaults to 6.

### SIP Timer Values

SIP T1

RFC 3261 T1 value (RTT estimate) that can range from 0 to 64 seconds. Defaults to 0.5 seconds.

SIP T2

RFC 3261 T2 value (maximum retransmit interval for non-INVITE requests and INVITE responses) that can range from 0 to 64 seconds.

Defaults to 4 seconds.

INVITE Expires

INVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to 2000000.

Defaults to 240 seconds.

ReINVITE Expires

ReINVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to 2000000.

Defaults to 30.

Reg Retry Intv

Interval to wait before the conference phone retries registration after failing during the last registration.

Defaults to 30.

Reg Retry Long Intvl

When registration fails with a SIP response code that does not match<Retry Reg RSC>, the conference phone waits for the specified length of time before retrying. If this interval is 0, the phone stops trying. This value should be much larger than the Reg Retry Intvl value, which should not be 0.

Defaults to 1200.

Reg Retry Random Delay

Random delay range (in seconds) to add to <Register Retry Intvl> when retrying REGISTER after a failure.

Defaults to 0.

Reg Retry Long Random Delay

Random delay range (in seconds) to add to <Register Retry Long Intvl> when retrying REGISTER after a failure.

Defaults to 0.

Reg Retry Intvl Cap

The maximum value to cap the exponential back-off retry delay (which starts at <Register Retry Intvl> and doubles on every REGISTER retry after a failure). In other words, the retry interval is always at <Register Retry Intvl> seconds after a failure. If this feature is enabled, <Reg Retry Random Delay> is added on top of the exponential back-off adjusted delay value.

Defaults to 0.

### Response Status Code Handling

Try Backup RSC

This parameter may be set to invoke failover upon receiving specified response codes.

Defaults to blank

Retry Reg RSC

Interval to wait before the CP-8831-3PCC retries registration after failing during the last registration.

Defaults to blank.

### RTP Parameters

RTP Port Min

Minimum port number for RTP transmission and reception. Minimum port number for RTP transmission and reception. Should define a range that contains at least 10 even number ports (twice the number of lines); for example, configure RTP port min to 16384 and RTP port max to 16538.

Defaults to 16384.

RTP Port Max

Maximum port number for RTP transmission and reception. Should define a range that contains at least 10 even number ports (twice the number of lines); for example, configure RTP port min to 16384 and RTP port max to 16538.

Defaults to 16538.

RTP Packet Size

Packet size in seconds, which can range from 0.01 to 0.16. Valid values must be a multiple of 0.01 seconds.

Defaults to 0.02.

RTCP Tx Enable

Enables RTCP for an active connection.

Defaults to No.

### SDP Payload Types

AVT Dynamic Payload

AVT dynamic payload type. Ranges from 96-127.

Defaults to 101.

### NAT Support Parameters

NAT Keep Alive Intvl

Interval between NAT-mapping keep alive messages.

Defaults to 15.

### Provisioning

For information about the Provisioning page, see the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control Provisioning Guide .

### Regional

### Control Timer Values (sec)

Interdigit Long Timer

Long timeout between entering digits when dialing. The interdigit timer values are used as defaults when dialing. The Interdigit_Long_Timer is used after any one digit, if all valid matching sequences in the dial plan are incomplete as dialed. Range: 0–64 seconds.

Defaults to 10

Interdigit Short Timer

Short timeout between entering digits when dialing. The Interdigit_Short_Timer is used after any one digit, if at least one matching sequence is complete as dialed, but more dialed digits would match other as yet incomplete sequences. Range: 0–64 seconds.

Defaults to 3.

### Time

Set Local Date (mm/dd)

Sets the local date (mm represents the month and dd represents the day). The year is optional and uses two or four digits.

Set Local Time (HH/mm)

Sets the local time (hh represents hours and mm represents minutes). Seconds are optional.

Time Zone

Selects the number of hours to add to GMT to generate the local time for caller ID generation. Choices are GMT-12:00, GMT-11:00,…, GMT, GMT+01:00, GMT+02:00, …, GMT+13:00.

Defaults to GMT-08:00.

Time Offset (HH/mm)

This specifies the offset from GMT to use for the local system time.

Ignore DHCP Time Offset

When used with some routers that have DHCP with time offset values configured, the 3PCC phone uses the router settings and ignores the phone time zone and offset settings. To ignore the router DHCP time offset value, and use the local time zone and offset settings, choose yes for this option. Choosing no causes the IP phone to use the router’s DHCP time offset value.

The default value is Yes.

Daylight Saving Time Rule

Enter the rule for calculating daylight saving time; it should include the start, end, and save values. This rule is comprised of three fields. Each field is separated by ; (a semicolon) as shown below. Optional values inside [ ] (the brackets) are assumed to be 0 if they are not specified. Midnight is represented by 0:0:0 of the given date.

This is the format of the rule: Start = <start-time>; end=<end-time>; save = <save-time>.

The <start-time> and <end-time> values specify the start and end dates and times of daylight saving time. Each value is in this format: <month> /<day> /<weekday>[/HH:[mm[:ss]]]

The <save-time> value is the number of hours, minutes, and/or seconds to add to the current time during daylight saving time. The <save-time> value can be preceded by a negative (-) sign if subtraction is desired instead of addition. The <save-time> value is in this format: [/[+|-]HH:[mm[:ss]]]

The <month> value equals any value in the range 1-12 (January-December).

The <day> value equals [+|-] any value in the range 1-31.

If <day> is 1, it means the <weekday> on or before the end of the month (in other words the last occurrence of < weekday> in that month).

Daylight Saving Time Rule (continued)

The <weekday> value equals any value in the range 1-7 (Monday-Sunday). It can also equal 0. If the <weekday> value is 0, this means that the date to start or end daylight saving is exactly the date given. In that case, the <day> value must not be negative. If the <weekday> value is not 0 and the <day> value is positive, then daylight saving starts or ends on the <weekday> value on or after the date given. If the <weekday> value is not 0 and the <day> value is negative, then daylight saving starts or ends on the <weekday> value on or before the date given. Where:

HH stands for hours (0-23).

mm stands for minutes (0-59).

ss stands for seconds (0-59).

The default Daylight Saving Time Rule is start=3/-1/7/2;end=10/-1/7/2;save=1.

Daylight Saving Time Enable

Select Yes to enable Daylight Saving Time.

### Localization

Dictionary Server Script

Defines the location of the dictionary server, the languages available, and the associated dictionary. See the “Create a Dictionary Server Script” section .

Language Selection

Specifies the default language. The value must match one of the languages supported by the dictionary server. The script (dx value) is:

Defaults to blank; the maximum number of characters is 512. For example:

Locale

Choose the locale that should be set in the HTTP Accept-Language header

### Phone

### QoS Settings

SIP TOS Value

TOS field value in UDP IP packets carrying a SIP message.

Defaults to 0x60.

RTP TOS Value

ToS/DiffServ field value in UDP IP packets carrying RTP data.

Defaults to 0xb8.

### General

Station Display Name

Name to identify the conference phone; appears on the phone screen. You can use spaces in this field and the name does not have to be unique.

Text Logo

Text logo to display when the phone boots up. A service provider, for example, can enter logo text as follows:

- Up to 2 lines of text

- Each line must be fewer than 32 characters

- Insert a new line character (\n) between lines

- Insert escape code %0a

For example, Super\n%0aTelecom displays:

Super

Telecom

Use the + character to add spaces for formatting. For example, you can add multiple + characters before and after the text to center it.

PNG Picture Download URL

URL locating the (.png) file to display on the phone screen background.

For more information, see the “Configure Phone Information and Display Settings” section .

Select Logo

Select from None, PNG Picture, or Text Logo.

Defaults to None.

Select Background Picture

Select from PNG Picture, or None.

Defaults to Default.

Screen Saver Enable

Enables a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode.

Screen Saver Wait

Amount of idle time before screen saver displays.

Defaults to 300.

Screen Saver Icon

In screen saver mode, the display unit can display:

- A background picture.

- Station time in the middle of the screen.

- A moving Cisco icon. When the phone is locked, the status line displays a scrolling message “Press any key to unlock your phone.”

- Cisco Logo

- The station date and time in the middle of the screen.

Co-branding Banner Picture Download URL

URL to download a.gif (.png or.jpeg) image on the web GUI for co-branding.

### Miscellaneous Line Key Settings

Call Appearances Per Line

This parameter allows you to choose the number of calls per line button. You can choose a value from 2 (the default) to 10.

### Supplementary Services

Conference Serv

Enable/disable Three way conference service.

Defaults to Yes.

Attn Transfer Serv

Enable/disable attended-call-transfer service.

Defaults to Yes.

Blind Transfer Serv

Enable/disable blind-call-transfer service.

Defaults to Yes.

Cfwd All Serv

Enable/disable call-forward-all service.

Defaults to Yes.

Cfwd Busy Serv

Enable/disable call-forward-on-busy service.

Defaults to Yes.

Cfwd No Ans Serv

Enable/disable call-forward-no-answer service.

Defaults to Yes.

### BroadSoft Settings

Directory Enable

Set to Yes to enable BroadSoft directory for the phone user.

Defaults to Yes.

XSI Host Server

Enter the name of the server; for example, xsi.iop1.broadworks.net.

Directory Name

Name of the directory. Displays on the phone as a directory choice.

Directory Type

Select the type of BroadSoft directory:

Enterprise (default): Allows users to search on last name, first name, user or group ID, phone number, extension, department, or email address.

Group: Allows users to search on last name, first name, user ID, phone number, extension, department, or email address.

Personal: Allows users to search on last name, first name, or telephone number.

Directory User ID

BroadSoft User ID of the phone user; for example, johndoe@xdp.broadsoft.com.

Directory Password

Alphanumeric password associated with the User ID.

### LDAP Corporate Directory Search

LDAP Dir Enable

Choose Yes to enable LDAP.

LDAP Corp Dir Name

Enter a free-form text name, such as “Corporate Directory.”

LDAP Server

Enter a fully qualified domain name or IP address of LDAP server, in the following format:

nnn.nnn.nnn.nnn

LDAP Auth Method

Select the authentication method that the LDAP server requires. Choices are:

None—No authentication is used between the client and the server.

Simple—The client sends its fully-qualified domain name and password to the LDAP server. Might present security issues.

Digest-MD5—The LDAP server sends authentication options and a token to the client. The client returns an encrypted response that is decrypted and verified by the server.

LDAP Client DN

Enter the distinguished name domain components [dc]; for example:

dc=cv2bu,dc=com

If using the default Active Directory schema (Name(cn)->Users->Domain), an example of the client DN follows:

cn="David Lee",dc=users,dc=cv2bu,dc=com

LDAP Username

Enter the username for a credentialed user on the LDAP server.

LDAP Password

Enter the password for the LDAP username.

LDAP Search Base

Specify a starting point in the directory tree from which to search. Separate domain components [dc] with a comma. For example:

dc=cv2bu,dc=com

LDAP Last Name Filter

This defines the search for surnames [sn], known as last name in some parts of the world. For example, sn:(sn=*$VALUE*). This search allows the provided text to appear anywhere in a name, beginning, middle, or end.

LDAP First Name Filter

This defines the search for the common name [cn]. For example, cn:(cn=*$VALUE*). This search allows the provided text to appear anywhere in a name, beginning, middle, or end.

LDAP Search Item 3

Additional customized search item. Can be blank if not needed.

LDAP Item 3 Filter

Customized filter for the searched item. Can be blank if not needed.

LDAP Search Item 4

Additional customized search item. Can be blank if not needed.

LDAP Item 4 Filter

Customized filter for the searched item. Can be blank if not needed.

LDAP Display Attrs

Format of LDAP results display on phone where:

- a—Attribute name

- cn—Common name

- sn—Surname (last name)

- telephoneNumber—Phone number

- n—Display name

For example, n=Phone causes "Phone:" to be displayed in front of the phone number of an LDAP query result when the detail soft button is pressed.

- t—type

When t=p, that is, t is of type phone number, then the retrieved number can be dialed. Only one number can be made dialable. If two numbers are defined as dialable, only the first number is used. For example, a=ipPhone, t=p; a=mobile, t=p;

This example results in only the IP Phone number being dialable and the mobile number will be ignored.

- p—phone number

When p is assigned to a type attribute, example t=p, then the retrieved number is dialable by the phone.

LDAP Number Mapping

Can be blank if not needed.

Note With the LDAP number mapping you can manipulate the number that was retrieved from the LDAP server. For example, you can append 9 to the number if your dial plan requires a user to enter 9 before dialing. Add the 9 prefix by adding (<:9xx.>) to the LDAP Number Mapping field. For example, 555 1212 would become 9555 1212.

If you do not manipulate the number in this fashion, a user can use the Edit Dial feature to edit the number before dialing out.

### XML Service

XML Directory Service Name:

Name of the XML Directory. Displays on the user’s phone as a directory choice

XML Directory Service URL

URL where the XML Directory is located.

XML Application Service Name

Name of the XML application. Displays on the user’s phone as a web application choice.

XML Application Service URL

URL where the XML application is located.

XML User Name

XML service username for authentication purposes

XML Password

XML service password for authentication purposes

### User

### Call Forward

Cfwd All Dest

Enter the extensions to which the call is forwarded.

Cfwd Busy Dest

Enter the extensions to forward calls to when the line is busy.

Defaults to voicemail.

Cfwd No Ans Dest

Enter the extension to forward calls to when the call is not answered.

Defaults to voice mail.

Cfwd No Ans Delay

Enter the delay in time (in seconds) to wait before forwarding a call that is unanswered.

Defaults to 20 seconds.

### Speed Dial

You can configure speed dials on the conference phone from the LCD GUI or the web GUI.

Speed Dial 2 through 9: Target phone number (or URL) assigned to speed dial 2, 3, 4, 5, 6, 7, 8, or 9. Press the digit key (2-9) to dial out the assigned number.

Defaults to blank.

### Supplementary Services

Time Format:

Choose the time format for the phone (12 or 24 hour).

Date Format

Choose the date format for the phone (month/day or day/month).

### Audio

Ringer Volume

Sets the default volume for the ringer.

Speaker Volume

Sets the default volume for the speakerphone.

### LCD

LCD Contrast

Enter a number value from 1 to 30. The higher the number, the greater the contrast on the IP phone screen.

Back Light Timer (seconds)

Select the number of seconds before the back light should turn off (10s, 20s, or 30s) or Off or Always On.

### Extension

In a configuration profile, the Line parameters must be appended with the appropriate numeral to indicate the line to which the setting applies. For example:

### General

Line Enable: To enable this line for service, select yes. Otherwise, select no. Defaults to yes.

### NAT Settings

NAT Keep Alive Enable

To send the configured NAT keep alive message periodically, select yes. Otherwise, select no.

Defaults to No.

NAT Keep Alive Msg

Enter the keep alive message that should be sent periodically to maintain the current NAT mapping. If the value is $NOTIFY, a NOTIFY message is sent. If the value is $REGISTER, a REGISTER message without contact is sent.

Defaults to $NOTIFY.

### Call Feature Settings

Default Ring

Type of ring heard. Choose from No Ring or 1 through 10.

## Call History

Displays the call history for the phone. To change the information displayed, select the type of call history from the drop-down list:

- All Calls

- Received Calls

- Placed Calls

- Missed Calls

| Parameter | Description |
|---|---|
| Connection Type | Indicates the type of internet connection for the phone: DHCP Static IP |
| Current IP | Displays the current IP address assigned to the IP phone. |
| Host Name | Displays the current host name assigned to the phone. |
| Domain | Displays the network domain name of the phone. Defaults to cisco.com. |
| Current Netmask | Displays the network mask assigned to the phone. |
| DNS from DHCP | Displays the IP address assigned by DHCP server. |
| Primary DNS | Displays the primary DNS server assigned to the phone. |
| Current Gateway | Displays the default router assigned to the phone. |
| Secondary DNS | Displays the secondary DNS server assigned to the phone. |

| Reason | Description |
|---|---|
| Upgrade | An upgrade operation caused a reboot (regardless whether the upgrade completed or failed). |
| Provisioning | Changes made to parameter values by using the phone LCD or Web GUI, or a resync caused a reboot. |
| SIP Triggered | A SIP request caused a reboot. |
| RC | A remote customization caused a reboot. |
| User Triggered | The user manually triggered a cold reboot. |
| IP Changed | The phone IP address was changed triggering a warm reboot. |

| Parameter | Description |
|---|---|
| Product Name | Model number of the conference phone. |
| Software Version | Version number of the conference phone software. |
| MAC Address | Hardware address of the conference phone. |
| Customization | For an RC unit, this field indicates whether the unit has been customized or not. Pending indicates a new RC unit that is ready for provisioning. If the unit has already retrieved its customized profile, this field displays the name of the company that provisioned the unit. |
| Serial Number | Serial number of the conference phone. |
| Hardware Version | Version number of the conference phone hardware. |
| Client Certificate | Status of the client certificate, which authenticates the conference phone for use in the ITSP network. This field indicates if the client certificate is properly installed in the phone. |
| Wireless Microphone Region | Wireless microphone region of the conference phone. |

| Parameter | Description |
|---|---|
| Current Time | Current date and time of the system; for example, 08/06/14 1:42:56 a.m. |
| Elapsed Time | Total time elapsed since the last reboot of the system; for example, 7 days, 02:13:02. |
| Operational VLAN ID | ID of the VLAN currently in use if applicable. |
| SW Port | Displays the type of Ethernet connection from the IP phone to the switch. |

| Parameter | Description |
|---|---|
| Registration State | Shows “Registered” if the phone is registered, “Not Registered” if the phone is not registered to the ITSP. |
| Last Registration At | Last date and time the line was registered. |
| Next Registration In | Number of seconds before the next registration renewal. |
| Mapped SIP Port | Port number of the SIP port mapped by NAT. |

| Parameter | Description |
|---|---|
| Call State | Status of the call. |
| Duration | Duration of the call. |
| Remote Address | Address of the remote device. |
| Local Address | Address of the local device. |
| Start Time | Starting time of the call |
| Type | Direction of the call. |
| Peer Name | Name of the internal phone. |
| Peer Phone | Phone number of the internal phone. |
| Sender Packets | Number of RTP voice packets transmitted since voice stream was opened. Note This number is not necessarily identical to the number of RTP voice packets transmitted since the call began because the call might have been placed on hold. |
| Sender Octets | Total number of octets sent by the phone. |
| Sender Codec | Type of voice stream transmitted (RTP streaming audio from codec): G.729, iLBC, G.711 u-law, or G.711 A-law. |
| Rcvr Lost Packets | Missing RTP packets (lost in transit.) |
| Avg Jitter | Estimated average RTP packet jitter (dynamic delay that a packet encounters when going through the network) observed since the receiving voice stream was opened. |
| Rcvr Codec | Type of voice stream received (RTP streaming audio from codec): G.729, iLBC, G.711 u-law, or G.711 A-law. |
| Rcvr Packets | Number of RTP voice packets received since voice stream was opened. Note This number is not necessarily identical to the number of RTP voice packets received since the call began because the call might have been placed on hold |
| Rcvr Octets | Total number of octets received by the phone. |
| MOS-LQK | Score that is an objective estimate of the mean opinion score (MOS) for listening quality (LQK) that rates from 5 (excellent) to 1 (bad). This score is based on audible concealment events due to frame loss in the preceding 8-second interval of the voice stream. Note The MOS LQK score can vary based on the type of codec that the Cisco Unified IP Conference Phone 8831 for Third-Party Call Control uses. |
| AVG MOS LQK | Average MOS LQK score observed for the entire voice stream. |
| Min MOS LQK | Lowest MOS LQK score observed from start of the voice stream. |
| Max MOS LQK | Baseline or highest MOS LQK score observed from start of the voice stream. These codecs provide the following maximum MOS LQK score under normal conditions with no frame loss: G.711 gives 4.5 G.722 gives 4.5 G.729 A /AB gives 3.7 iLBC gives 3.9 |
| MOS LQK Version | Version of the Cisco proprietary algorithm used to calculate MOS LQK scores |
| Cumulative Conceal Ratio | Total number of concealment frames divided by total number of speech frames received from start of the voice stream. |
| Interval Conceal Ratio | Ratio of concealment frames to speech frames in preceding 3-second interval of active speech. If using voice activity detection (VAD), a longer interval might be required to accumulate 3 seconds of active speech. |
| Max Conceal Ratio | Highest interval concealment ratio from start of the voice stream. |
| Conceal Secs: | Number of seconds that have concealment events (lost frames) from the start of the voice stream (includes severely concealed seconds). |
| Severely Conceal Secs | Number of seconds that have more than 5 percent concealment events (lost frames) from the start of the voice stream. |
| Latency | Number of milliseconds for latency. |
| Max Jitter | Number of milliseconds for receiver jitter. |
| Rcvr Discarded | Number of RTP packets in the receiving voice stream that have been discarded (bad packets, too late, and so on). Note The phone will discard payload type 19 comfort noise packets that are generated by Cisco Gateways, which will increment this counter. |

| Parameter | Description |
|---|---|
| Ring Tone Download Status | Indicates whether the phone is downloading a ring tone (and from where) or if it is idle. |
| Ring Tone 1 | Information about the user downloaded ring tone 1: name, size, and time-stamp of the tone. |
| Ring Tone 2 | Information about the user downloaded ring tone 2: name, size, and time-stamp of the tone. |

| Parameter | Description |
|---|---|
| Locale Download Status | Displays the downloaded locale package status. |
| Downloaded Dictionary Info | Dictionary downloaded from the TFTP/HTTP provisioning server indicated in the phone. |
| Downloaded Font Info | Displays the downloaded font name. |

| Parameter | Description |
|---|---|
| Firmware Upgrade Status 1 | Displays the upgrade status (failed or succeeded) with reason for the same. |
| Firmware Upgrade Status 2 |
| Firmware Upgrade Status 3 |

| Parameter | Description |
|---|---|
| Provisioning Status 1 | Displays the provisioning status (resync) of the phone. |
| Provisioning Status 2 |
| Provisioning Status 3 |

| Parameter | Description |
|---|---|
| Custom CA Provisioning Status | Indicates whether provisioning using a custom CA succeeded or failed: Last provisioning succeeded on mm/dd/yyyy HH:MM:SS; or Last provisioning failed on mm/dd/yyyy HH:MM:SS |
| Custom CA Info | Displays information about the custom CA: Installed—Displays the “CN Value,” where “CN Value” is the value of the CN parameter for the Subject field in the first certificate. Not Installed—Displays if no custom CA certificate is installed. |

| Parameter | Description |
|---|---|
| Debug Message 0 | messages |
| Debug Message 1 | messages.0 |
| Debug Message 2 | messages.1 |
| Debug Message 3 | messages.2 |
| Debug Message 4 | messages.3 |
| Debug Message 5 | messages.4 |
| Debug Message 6 | messages.5 |
| Debug Message 7 | messages.6 |
| Debug Message 8 | messages.7 |

| Parameter | Description |
|---|---|
| Loading Time | The amount of elapsed time when the page is loaded on the browser. Note Safari and IE version before 9 does not support this parameter. |
| Browser Version | Version of the browser. For example, Firefox 31 |
| OS Version | Version of the Windows operating system. |
| Platform | The platform to which the browser is compiled. |
| Width | Current width of the browser. |
| Height | Current height of the browser. |

| Parameter | Description |
|---|---|
| Restricted Access Domains | This feature is used when implementing software customization. |
| Enable Web Server | Enable/disable web server of the IP phone. Defaults to Yes. |
| Web Server Port | Port number of the phone web user interface. Defaults to 80. |
| Enable Web Admin Access | Lets you enable or disable local access to the phone web user interface. Select Yes or No from the drop-down menu. Defaults to Yes. |
| Admin Password | Password for the administrator. Defaults to no password. |
| User Password | Password for the user. Defaults to blank. |
| Phone-UI-User-Mode | Allows you to restrict the menus and options that phone users see when they use the phone interface. Choose yes to enable this parameter and restrict access. The default is no. Specific parameters are then designated as “na” or “ro” using provisioning files. Parameters designated as “na” will not appear on the phone interface. Parameters designated as “ro” will not be editable by the user. |

| Parameter | Description |
|---|---|
| Connection Type | Choose the type of internet connection: DHCP Static IP |

| Parameter | Description |
|---|---|
| Static IP | If static IP was chosen as the type of internet connection, displays the static IP address assigned to the phone. |
| Netmask | If static IP was chosen as the type. |
| Gateway | Default router IP address. Blank if DHCP assigned. |

| Parameter | Description |
|---|---|
| Host Name | The host name of the conference phone. |
| Domain | The network domain of the conference phone. |
| Primary DNS | DNS server used by the conference phone in addition to DHCP supplied DNS servers if DHCP is enabled; when DHCP is disabled, this is the primary DNS server. Defaults to 0.0.0.0. |
| Secondary DNS | DNS server used by the conference phone in addition to DHCP supplied DNS servers if DHCP is enabled; when DHCP is disabled, this is the secondary DNS server. Defaults to 0.0.0.0. |
| Syslog Server | Specify the syslog server name and port. This feature specifies the server for logging IP phone system information and critical events. If both Debug Server and Syslog Server are specified, Syslog messages are also logged to the Debug Server. |
| Debug Level | The debug level from 0-3. The higher the level, the more debug information is generated. Zero (0) means no debug information is generated. To log SIP messages, you must set the Debug Level to at least 2. Defaults to 0. |
| Layer 2 Logging | Used for IP phone network layer debugging purposes. Do not use except when advised to do so by Cisco technical support, as this may impact system performance. Set to No by default. |
| Primary NTP Server | IP address or name of primary NTP server. |
| Secondary NTP Server | IP address or name of secondary NTP server. |
| SSH Access | If enabled, the phone supports console access for debugging and testing. |
| DNS Cache TTL Ignore | If enabled, the phone continues to use the previous cached DNS result if the DNS server does not respond when the phone tries to renew its DNS query. When disabled, the phone uses the previous TTL value and clears the DNS query result cache. |
| SSH User ID | User ID for SSH login. |
| SSH Password | Password for the SSH login. |

| Parameter | Description |
|---|---|
| Enable CDP | Enable CDP only if you are using a switch that has Cisco Discovery Protocol. CDP is negotiation based and determines which VLAN the IP phone resides in. |
| Enable LLDP-MED | Choose Yes to enable LLDP-MED for the phone to advertise itself to devices that use that discovery protocol. When the LLDP-MED feature is enabled, after the phone has initialized and Layer 2 connectivity is established, the phone sends out LLDP-MED PDU frames. If the phone receives no acknowledgment, the manually configured VLAN or default VLAN will be used if applicable. If the CDP is used concurrently, the waiting period of 6 seconds is used. The waiting period will increase the overall startup time for the phone. |
| Network Startup Delay | Setting this value causes a delay for the switch to get to the forwarding state before the phone will send out the first LLDP-MED packet. The default delay is 3 seconds. For configuration of some switches, you might need to increase this value to a higher value for LLDP-MED to work. Configuring a delay can be important for networks that use Spanning Tree Protocol. |
| VLAN ID | If you use a VLAN without CDP (VLAN enabled and CDP disabled), enter a VLAN ID for the IP phone. Note that only voice packets are tagged with the VLAN ID. Do not use 1 for the VLAN ID. |

| Parameter | Description |
|---|---|
| Asset ID | Provides the ability to enter an asset ID for inventory management when using LLDP-MED. The default value for Asset ID is empty. Enter a string of less than 32 characters if you are using this field. The Asset ID can be provisioned only by using the web management interface or remote provisioning. The Asset ID is not displayed on the phone screen. Changing the Asset ID field causes the phone to reboot. |

| Parameter | Description |
|---|---|
| Max Forward | SIP Max Forward value, which can range from 1 to 255. Defaults to 70. |
| Max Redirection | Number of times an invite can be redirected to avoid an infinite loop. Defaults to 5. |
| SIP User Agent Name | Used in outbound REGISTER requests. Defaults to $VERSION. If empty, the header is not included. Macro expansion of $A to $D corresponding to GPP_A to GPP_D allowed |
| SIP Server Name | Server header used in responses to inbound responses. Defaults to $VERSION. |
| SIP Reg User Agent Name | User-Agent name to be used in a REGISTER request. If this is not specified, the <SIP User Agent Name> is also used for the REGISTER request. Defaults to blank. |
| SIP Accept Language | Accept-Language header used. To access, click the SIP tab, and fill in the SIP Accept Language field. There is no default. If empty, the header is not included. |
| RFC 2543 Call Hold | If set to yes, unit will include c=0.0.0.0 syntax in SDP when sending a SIP re-INVITE to the peer to hold the call. If set to no, unit will not include the c=0.0.0.0 syntax in the SDP. The unit will always include a=sendonly syntax in the SDP in either case. Defaults to Yes. |
| SIP TCP Port Min | Specifies the lowest TCP port number that can be used for SIP sessions. Defaults to 5060. |
| SIP TCP Port Max | Specifies the highest TCP port number that can be used for SIP sessions. Defaults to 5080. |
| Caller ID Header | Provides the option to take the caller ID from PAID-RPID-FROM, P-ASSERTEDIDENTITY, REMOTE-PARTY-ID, or FROM header. |
| Max INVITE Retry Attempts | Maximum number of INVITE retry attempts by the phone. Defaults to 6. |
| Max NON-INVITE Retry Attempts | Maximum number of NON-INVITE retry attempts by the phone. Defaults to 6. |

| Parameter | Description |
|---|---|
| SIP T1 | RFC 3261 T1 value (RTT estimate) that can range from 0 to 64 seconds. Defaults to 0.5 seconds. |
| SIP T2 | RFC 3261 T2 value (maximum retransmit interval for non-INVITE requests and INVITE responses) that can range from 0 to 64 seconds. Defaults to 4 seconds. |
| INVITE Expires | INVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to 2000000. Defaults to 240 seconds. |
| ReINVITE Expires | ReINVITE request Expires header value. If you enter 0, the Expires header is not included in the request. Ranges from 0 to 2000000. Defaults to 30. |
| Reg Retry Intv | Interval to wait before the conference phone retries registration after failing during the last registration. Defaults to 30. |
| Reg Retry Long Intvl | When registration fails with a SIP response code that does not match<Retry Reg RSC>, the conference phone waits for the specified length of time before retrying. If this interval is 0, the phone stops trying. This value should be much larger than the Reg Retry Intvl value, which should not be 0. Defaults to 1200. |
| Reg Retry Random Delay | Random delay range (in seconds) to add to <Register Retry Intvl> when retrying REGISTER after a failure. Defaults to 0. |
| Reg Retry Long Random Delay | Random delay range (in seconds) to add to <Register Retry Long Intvl> when retrying REGISTER after a failure. Defaults to 0. |
| Reg Retry Intvl Cap | The maximum value to cap the exponential back-off retry delay (which starts at <Register Retry Intvl> and doubles on every REGISTER retry after a failure). In other words, the retry interval is always at <Register Retry Intvl> seconds after a failure. If this feature is enabled, <Reg Retry Random Delay> is added on top of the exponential back-off adjusted delay value. Defaults to 0. |

| Parameter | Description |
|---|---|
| Try Backup RSC | This parameter may be set to invoke failover upon receiving specified response codes. Defaults to blank |
| Retry Reg RSC | Interval to wait before the CP-8831-3PCC retries registration after failing during the last registration. Defaults to blank. |

| Parameter | Description |
|---|---|
| RTP Port Min | Minimum port number for RTP transmission and reception. Minimum port number for RTP transmission and reception. Should define a range that contains at least 10 even number ports (twice the number of lines); for example, configure RTP port min to 16384 and RTP port max to 16538. Defaults to 16384. |
| RTP Port Max | Maximum port number for RTP transmission and reception. Should define a range that contains at least 10 even number ports (twice the number of lines); for example, configure RTP port min to 16384 and RTP port max to 16538. Defaults to 16538. |
| RTP Packet Size | Packet size in seconds, which can range from 0.01 to 0.16. Valid values must be a multiple of 0.01 seconds. Defaults to 0.02. |
| RTCP Tx Enable | Enables RTCP for an active connection. Defaults to No. |

| Parameter | Description |
|---|---|
| AVT Dynamic Payload | AVT dynamic payload type. Ranges from 96-127. Defaults to 101. |

| Parameter | Description |
|---|---|
| NAT Keep Alive Intvl | Interval between NAT-mapping keep alive messages. Defaults to 15. |

| Parameter | Description |
|---|---|
| Interdigit Long Timer | Long timeout between entering digits when dialing. The interdigit timer values are used as defaults when dialing. The Interdigit_Long_Timer is used after any one digit, if all valid matching sequences in the dial plan are incomplete as dialed. Range: 0–64 seconds. Defaults to 10 |
| Interdigit Short Timer | Short timeout between entering digits when dialing. The Interdigit_Short_Timer is used after any one digit, if at least one matching sequence is complete as dialed, but more dialed digits would match other as yet incomplete sequences. Range: 0–64 seconds. Defaults to 3. |

| Parameter | Description |
|---|---|
| Set Local Date (mm/dd) | Sets the local date (mm represents the month and dd represents the day). The year is optional and uses two or four digits. |
| Set Local Time (HH/mm) | Sets the local time (hh represents hours and mm represents minutes). Seconds are optional. |
| Time Zone | Selects the number of hours to add to GMT to generate the local time for caller ID generation. Choices are GMT-12:00, GMT-11:00,…, GMT, GMT+01:00, GMT+02:00, …, GMT+13:00. Defaults to GMT-08:00. |
| Time Offset (HH/mm) | This specifies the offset from GMT to use for the local system time. |
| Ignore DHCP Time Offset | When used with some routers that have DHCP with time offset values configured, the 3PCC phone uses the router settings and ignores the phone time zone and offset settings. To ignore the router DHCP time offset value, and use the local time zone and offset settings, choose yes for this option. Choosing no causes the IP phone to use the router’s DHCP time offset value. The default value is Yes. |
| Daylight Saving Time Rule | Enter the rule for calculating daylight saving time; it should include the start, end, and save values. This rule is comprised of three fields. Each field is separated by ; (a semicolon) as shown below. Optional values inside [ ] (the brackets) are assumed to be 0 if they are not specified. Midnight is represented by 0:0:0 of the given date. This is the format of the rule: Start = <start-time>; end=<end-time>; save = <save-time>. The <start-time> and <end-time> values specify the start and end dates and times of daylight saving time. Each value is in this format: <month> /<day> /<weekday>[/HH:[mm[:ss]]] The <save-time> value is the number of hours, minutes, and/or seconds to add to the current time during daylight saving time. The <save-time> value can be preceded by a negative (-) sign if subtraction is desired instead of addition. The <save-time> value is in this format: [/[+\|-]HH:[mm[:ss]]] The <month> value equals any value in the range 1-12 (January-December). The <day> value equals [+\|-] any value in the range 1-31. If <day> is 1, it means the <weekday> on or before the end of the month (in other words the last occurrence of < weekday> in that month). |
| Daylight Saving Time Rule (continued) | The <weekday> value equals any value in the range 1-7 (Monday-Sunday). It can also equal 0. If the <weekday> value is 0, this means that the date to start or end daylight saving is exactly the date given. In that case, the <day> value must not be negative. If the <weekday> value is not 0 and the <day> value is positive, then daylight saving starts or ends on the <weekday> value on or after the date given. If the <weekday> value is not 0 and the <day> value is negative, then daylight saving starts or ends on the <weekday> value on or before the date given. Where: HH stands for hours (0-23). mm stands for minutes (0-59). ss stands for seconds (0-59). The default Daylight Saving Time Rule is start=3/-1/7/2;end=10/-1/7/2;save=1. |
| Daylight Saving Time Enable | Select Yes to enable Daylight Saving Time. |

| Parameter | Description |
|---|---|
| Dictionary Server Script | Defines the location of the dictionary server, the languages available, and the associated dictionary. See the “Create a Dictionary Server Script” section . |
| Language Selection | Specifies the default language. The value must match one of the languages supported by the dictionary server. The script (dx value) is: <Language_Selection ua="na"> </Language_Selection> Defaults to blank; the maximum number of characters is 512. For example: <Language_Selection ua="na"> Spanish </Language_Selection> |
| Locale | Choose the locale that should be set in the HTTP Accept-Language header |

| Parameter | Description |
|---|---|
| SIP TOS Value | TOS field value in UDP IP packets carrying a SIP message. Defaults to 0x60. |
| RTP TOS Value | ToS/DiffServ field value in UDP IP packets carrying RTP data. Defaults to 0xb8. |

| Parameter | Description |
|---|---|
| Station Display Name | Name to identify the conference phone; appears on the phone screen. You can use spaces in this field and the name does not have to be unique. |
| Text Logo | Text logo to display when the phone boots up. A service provider, for example, can enter logo text as follows: Up to 2 lines of text Each line must be fewer than 32 characters Insert a new line character (\n) between lines Insert escape code %0a For example, Super\n%0aTelecom displays: Super Telecom Use the + character to add spaces for formatting. For example, you can add multiple + characters before and after the text to center it. |
| PNG Picture Download URL | URL locating the (.png) file to display on the phone screen background. For more information, see the “Configure Phone Information and Display Settings” section . |
| Select Logo | Select from None, PNG Picture, or Text Logo. Defaults to None. |
| Select Background Picture | Select from PNG Picture, or None. Defaults to Default. |
| Screen Saver Enable | Enables a screen saver on the phone. When the phone is idle for a specified time, it enters screen saver mode. |
| Screen Saver Wait | Amount of idle time before screen saver displays. Defaults to 300. |
| Screen Saver Icon | In screen saver mode, the display unit can display: A background picture. Station time in the middle of the screen. A moving Cisco icon. When the phone is locked, the status line displays a scrolling message “Press any key to unlock your phone.” Cisco Logo The station date and time in the middle of the screen. |
| Co-branding Banner Picture Download URL | URL to download a.gif (.png or.jpeg) image on the web GUI for co-branding. |

| Parameter | Description |
|---|---|
| Call Appearances Per Line | This parameter allows you to choose the number of calls per line button. You can choose a value from 2 (the default) to 10. |

| Parameter | Description |
|---|---|
| Conference Serv | Enable/disable Three way conference service. Defaults to Yes. |
| Attn Transfer Serv | Enable/disable attended-call-transfer service. Defaults to Yes. |
| Blind Transfer Serv | Enable/disable blind-call-transfer service. Defaults to Yes. |
| Cfwd All Serv | Enable/disable call-forward-all service. Defaults to Yes. |
| Cfwd Busy Serv | Enable/disable call-forward-on-busy service. Defaults to Yes. |
| Cfwd No Ans Serv | Enable/disable call-forward-no-answer service. Defaults to Yes. |

| Parameter | Description |
|---|---|
| Directory Enable | Set to Yes to enable BroadSoft directory for the phone user. Defaults to Yes. |
| XSI Host Server | Enter the name of the server; for example, xsi.iop1.broadworks.net. |
| Directory Name | Name of the directory. Displays on the phone as a directory choice. |
| Directory Type | Select the type of BroadSoft directory: Enterprise (default): Allows users to search on last name, first name, user or group ID, phone number, extension, department, or email address. Group: Allows users to search on last name, first name, user ID, phone number, extension, department, or email address. Personal: Allows users to search on last name, first name, or telephone number. |
| Directory User ID | BroadSoft User ID of the phone user; for example, johndoe@xdp.broadsoft.com. |
| Directory Password | Alphanumeric password associated with the User ID. |

| Parameter | Description |
|---|---|
| LDAP Dir Enable | Choose Yes to enable LDAP. |
| LDAP Corp Dir Name | Enter a free-form text name, such as “Corporate Directory.” |
| LDAP Server | Enter a fully qualified domain name or IP address of LDAP server, in the following format: nnn.nnn.nnn.nnn |
| LDAP Auth Method | Select the authentication method that the LDAP server requires. Choices are: None—No authentication is used between the client and the server. Simple—The client sends its fully-qualified domain name and password to the LDAP server. Might present security issues. Digest-MD5—The LDAP server sends authentication options and a token to the client. The client returns an encrypted response that is decrypted and verified by the server. |
| LDAP Client DN | Enter the distinguished name domain components [dc]; for example: dc=cv2bu,dc=com If using the default Active Directory schema (Name(cn)->Users->Domain), an example of the client DN follows: cn="David Lee",dc=users,dc=cv2bu,dc=com |
| LDAP Username | Enter the username for a credentialed user on the LDAP server. |
| LDAP Password | Enter the password for the LDAP username. |
| LDAP Search Base | Specify a starting point in the directory tree from which to search. Separate domain components [dc] with a comma. For example: dc=cv2bu,dc=com |
| LDAP Last Name Filter | This defines the search for surnames [sn], known as last name in some parts of the world. For example, sn:(sn=*$VALUE*). This search allows the provided text to appear anywhere in a name, beginning, middle, or end. |
| LDAP First Name Filter | This defines the search for the common name [cn]. For example, cn:(cn=*$VALUE*). This search allows the provided text to appear anywhere in a name, beginning, middle, or end. |
| LDAP Search Item 3 | Additional customized search item. Can be blank if not needed. |
| LDAP Item 3 Filter | Customized filter for the searched item. Can be blank if not needed. |
| LDAP Search Item 4 | Additional customized search item. Can be blank if not needed. |
| LDAP Item 4 Filter | Customized filter for the searched item. Can be blank if not needed. |
| LDAP Display Attrs | Format of LDAP results display on phone where: a—Attribute name cn—Common name sn—Surname (last name) telephoneNumber—Phone number n—Display name For example, n=Phone causes "Phone:" to be displayed in front of the phone number of an LDAP query result when the detail soft button is pressed. t—type When t=p, that is, t is of type phone number, then the retrieved number can be dialed. Only one number can be made dialable. If two numbers are defined as dialable, only the first number is used. For example, a=ipPhone, t=p; a=mobile, t=p; This example results in only the IP Phone number being dialable and the mobile number will be ignored. p—phone number When p is assigned to a type attribute, example t=p, then the retrieved number is dialable by the phone. |
| LDAP Number Mapping | Can be blank if not needed. Note With the LDAP number mapping you can manipulate the number that was retrieved from the LDAP server. For example, you can append 9 to the number if your dial plan requires a user to enter 9 before dialing. Add the 9 prefix by adding (<:9xx.>) to the LDAP Number Mapping field. For example, 555 1212 would become 9555 1212. If you do not manipulate the number in this fashion, a user can use the Edit Dial feature to edit the number before dialing out. |

| Parameter | Description |
|---|---|
| XML Directory Service Name: | Name of the XML Directory. Displays on the user’s phone as a directory choice |
| XML Directory Service URL | URL where the XML Directory is located. |
| XML Application Service Name | Name of the XML application. Displays on the user’s phone as a web application choice. |
| XML Application Service URL | URL where the XML application is located. |
| XML User Name | XML service username for authentication purposes |
| XML Password | XML service password for authentication purposes |

| Parameter | Description |
|---|---|
| Cfwd All Dest | Enter the extensions to which the call is forwarded. |
| Cfwd Busy Dest | Enter the extensions to forward calls to when the line is busy. Defaults to voicemail. |
| Cfwd No Ans Dest | Enter the extension to forward calls to when the call is not answered. Defaults to voice mail. |
| Cfwd No Ans Delay | Enter the delay in time (in seconds) to wait before forwarding a call that is unanswered. Defaults to 20 seconds. |

| Parameter | Description |
|---|---|
| Time Format: | Choose the time format for the phone (12 or 24 hour). |
| Date Format | Choose the date format for the phone (month/day or day/month). |

| Parameter | Description |
|---|---|
| Ringer Volume | Sets the default volume for the ringer. |
| Speaker Volume | Sets the default volume for the speakerphone. |

| Parameter | Description |
|---|---|
| LCD Contrast | Enter a number value from 1 to 30. The higher the number, the greater the contrast on the IP phone screen. |
| Back Light Timer (seconds) | Select the number of seconds before the back light should turn off (10s, 20s, or 30s) or Off or Always On. |

| Parameter | Description |
|---|---|
| NAT Keep Alive Enable | To send the configured NAT keep alive message periodically, select yes. Otherwise, select no. Defaults to No. |
| NAT Keep Alive Msg | Enter the keep alive message that should be sent periodically to maintain the current NAT mapping. If the value is $NOTIFY, a NOTIFY message is sent. If the value is $REGISTER, a REGISTER message without contact is sent. Defaults to $NOTIFY. |

| Parameter | Description |
|---|---|
| Default Ring | Type of ring heard. Choose from No Ring or 1 through 10. |