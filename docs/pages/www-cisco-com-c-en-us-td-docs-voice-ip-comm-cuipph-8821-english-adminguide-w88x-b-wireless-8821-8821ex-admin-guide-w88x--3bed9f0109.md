---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cuipph-8821-english-adminguide-w88x-b-wireless-8821-8821ex-admin-guide-w88x--3bed9f0109
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cuipph/8821/english/adminguide/w88x_b_wireless-8821-8821ex-admin-guide/w88x_b_wireless-8821-8821ex-admin-guide_chapter_0111.html
retrieved_at: 2026-08-21T01:56:26.603353+00:00
---

Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

# Cisco Wireless IP Phone 8821 and 8821-EX Administration Guide for Cisco Unified Communications Manager

Updated: June 28, 2016

Chapter: Phone Statistics

## Chapter: Phone Statistics

# Phone Statistics

## Statistics Available on the Phone

You can see statistics and information about the phone from the Settings menu on the phone.

These menus help you  troubleshoot problems when you are in the same location as your user.

### View Phone Information

When you troubleshoot phone problems, you often need information from the phone.

Access the Settings app.

Select Phone information .

#### Access Device Information

The Device information menu and submenus provide information related to the connections between the phone and the call control
                                    system.

Access the Settings app.

Select Phone information > Device information .

Select one of the following entries.

- Call manager —displays information about the call control system.

- Network —displays information about the IPv4 network.

- WLAN —displays information about the Wi-Fi connection.

- HTTP —displays information about configured URLs.

- Locale —displays information about the language locale.

- Security —displays information about the security settings.

- QoS —displays information related to the Quality of Service.

- UI —displays information related to the user interface.

- Battery —displays information related to the battery.

##### Device Information

The following tables describe the submenus and fields in the Device Information menu.

Field

Description

Cisco Unified CM 1

Primary call manager server that the phone uses. Displays the IP address and status.

Cisco Unified CM 2

Secondary call manager server that the phones uses. Displays the IP address and status, or is blank if not in use.

Cisco Unified CM 3

Displays the IP address and status of an additional call manager server, or is blank if not in use.

Cisco Unified CM 4

Displays the IP address and status of an additional call manager server, or is blank if not in use.

Cisco Unified CM 5

Displays the IP address and status of an additional call manager server, or is blank if not in use.

Any of these call manager fields can also show the IP address of an SRST router that is
                                       					 capable of providing limited call control system
                                       					 functionality.

Each available server displays the server IP address and one of the following states:

Call control system from which the phone is currently receiving call-processing
                                             						services.

Call control system to which the phone switches if the current server becomes
                                             						unavailable.

No current
                                             						connection to this Call control system.

Field

Description

MAC address

MAC address of the phone.

Host name

Unique, fixed name that is automatically assigned to
                                                   					 the phone based on the MAC address.

Domain name

Name of the DNS in which the phone resides.

DHCP server

IP address of the DHCP server from which the phone
                                                   					 obtains its IP address.

IP address

IP address of the phone.

Subnet mask

Subnet mask used by the phone.

Default router

IP address for the default gateway used by the
                                                   					 phone.

DNS server 1

Primary DNS server used by the phone.

DNS server 2

First backup DNS server used by the phone.

DNS server 3

Second backup DNS server used by the phone.

Alternate TFTP

Address of the TFTP server (other than the one assigned by DHCP).

TFTP server1

Primary TFTP server used by the phone.

TFTP server 2

Secondary TFTP server used by the phone.

Load server

Host name or IP address for the alternate server that the phone uses for firmware upgrades.

BOOTP server

CDP

Cisco
                                                   					 Discovery Protocol (CDP) usage.

GARP

Gratuitous ARP used for MAC address discovery.

Field Name

Description

Profile name

Name of the network profile that the phone is
                                                   					 currently using.

SSID

Service Set ID (SSID) that the phone is currently using.

Security mode

Authentication method that the phone is currently
                                                   					 using in the wireless network.

802.11 mode

Wireless signal mode that the phone is currently
                                                   					 using.

On call power save

Type of power save mode that the phone uses to save
                                                   					 battery power: PS-Poll or U-APSD.

Scan mode

Type of AP scanning.

WLAN SCEP server

URL or host name of the Simple Certificate Enrollment Protocol (SCEP)server

WLAN Root CA fingerprint

SHA256 or SHA1 fingerprint of the Root CA for WLAN authentication.

Field Name

Description

Authentication URL

URL that the phone uses to validate requests made to the phone web server.

Directories URL

URL of the server from which the phone obtains
                                                   					 directory information.

Idle URL

URL of an XML service that the phone displays when the phone has not been used for the time specified in the Idle URL Time
                                                   option and no menu is open.

For example, you could use the Idle URL option and the Idle URL Time option to display a stock quote or a calendar on the
                                                   LCD screen when the phone has not been used for 5 minutes.

Idle time

Number of seconds that the phone has not been used and no menu is open before the XML service specified in the Idle URL option
                                                   is activated.

Information URL

URL of the help text that appears on the phone.

Messages URL

URL of the server from which the phone obtains
                                                   					 message services.

IP phone proxy address

URL of proxy server, which makes HTTP requests to remote host addresses on behalf of the phone HTTP client and provides responses
                                                   from the remote host to the phone HTTP client.

Services URL

URL of the server from which the phone obtains
                                                   					 phone services.

Secured authentication URL

Secure URL that the phone uses to validate requests made to the phone web server.

Secured directory URL

Secure URL of the server from which the phone obtains
                                                   					 directory information.

Secured idle URL

Secure URL of an XML service that the phone displays when the phone has not been used for the time specified in the Idle URL
                                                   Time option and no menu is open.

Secured information URL

Secure URL of the help text that appears on the phone.

Secured messages URL

Secure URL of the server from which the phone obtains
                                                   					 message services.

Secured services URL

Secure URL of the server from which the phone obtains
                                                   					 phone services.

Field

Description

User locale

User locale associated with the phone user. Identifies a set of detailed information to support users, including language,
                                                   font, date and time formatting, and alphanumeric keyboard text information.

Network locale

Network locale associated with the phone user.
                                                   					 Identifies a set of detailed information to support the phone in a specific
                                                   					 location, including definitions of the tones and cadences used by the phone.

User locale version

Version of the user locale loaded on the phone.

Network locale version

Version of the network locale loaded on the phone.

Field

Description

Web access

Indicated web access capability for the phone.

No self care portal access.

Can view information only.

Can use the configuration pages

Web admin

Indicates if the web admin page is enabled.

Security mode

Security mode assigned to the phone

Field Name

Description

DSCP for call control

Differentiated Services Code Point (DSCP) IP
                                                   					 classification for call control signaling.

DSCP for configuration

DSCP IP classification for any phone configuration
                                                   					 transfer.

DSCP for services

DSCP IP classification for phone-based service.

Field Name

Description

BLF for call lists

Indicates whether the Busy Lamp Field (BLF) is enabled for call
                                                   lists.

Reverting focus priority

Indicates whether the phone shifts the call focus on the phone
                                                   screen to an incoming call or a reverting hold call.

Personalization

Indicates whether the phone has been enabled for configuration
                                                   of custom ring tones and wallpaper images.

Field Name

Description

Battery health

Indicates the overall health of the battery.

Battery temperature

Indicates the current temperature of the battery. If the battery runs excessively hot, the battery may fail soon.

Battery level

Indicates the current charge level of the battery.

#### Access Model Information

The Model information  menu provides information related to the phone model.

Access the Settings app.

Select Phone information > Model information .

##### Model Information

The following table describes the fields and contents in the Phone information > Model information screen.

Field Name

Description

Model number

Set to CP-8821 or CP-8821-EX

MAC address

MAC address of the phone

App load ID

Firmware version running on the phone

Serial number

Phone serial number

USB vendor ID

Set to Cisco

USB product ID

Set to 8821 or 8821-EX

RNDIS device address

Remote Network Device Interface Specification (RNDIS) address of the USB

RNDIS host address

RNDIS for the USB

#### Access Firmware Version

The Firmware version  menu provides information related to the firmware running on the phone.

Access the Settings app.

Select Phone information > Firmware version .

##### Firmware Version Information

The following table describes the fields and contents in the Phone information > Firmware version screen.

Field Name

Description

Active load

Firmware load that is active

Last upgrade

Upgrade status: date and time for successful update; otherwise messages about upgrade failure

Boot load ID

Identification of the boot loader version

WLAN driver ID

Identification of the WLAN driver

WLAN firmware ID

Identification of the WLAN firmware load

### Phone Statistics in the Admin Settings Menu

You can access some statistics about the phone from the Admin settings menu. These are the same statistics that are displayed if you access the phone from the administration web page.

#### Neighbor List Menu

The Neighbor list from the Admin settings menu shows  the available access points.

#### Access the Status Menu

The Status menu on the phone gives you important information about the phone.

Access the Settings app.

Select Admin settings > Status .

##### Status Messages

The Status messages screen provides a list of status messages. Each message has a date and time stamp. You can use these messages to troubleshoot
                                       problems.

##### WLAN Statistics

Field

Description

tx bytes

Number of bytes transmitted

rx bytes

Number of bytes received

tx packets

Number of packet transmitted

rx packets

Number of packet received

tx packets dropped

Number of packets transmitted that were dropped

rx packets dropped

Number of packets received that were dropped

tx packets errors

Number of transmitted packet errors

rx packets errors

Number of transmitted packet errors

tx frames

Number of frames transmitted

tx multicast frames

Number of multicast frames transmitted

tx retry

Number of transmission retries

tx multi retry

Number of muilticast transmission retries

tx failure

Number of transmission failures

rts success

Number of request to send (rts) successes

rts failure

Number of rts failures

ack failure

rx duplicate frames

Number of duplicate frames received

rx fragmented packets

Number of fragmented packets received

Roaming count

##### Call Statistics

Field

Description

Receiver codec

Type of audio encoding received by the phone: G.729, G.711 u-law, G.711 A-law

Sender codec

Type of audio encoding sent by the phone: G.729, G.711 u-law, G.711 A-law

Receiver size

Sender size

Rcvr packets

Number of packets received by the phone

Sender packets

Transmitter DSCP

Receiver DSCP

Transmitter WMM UP

Wireless Multi Media (WMM) Up transmitter

Receiver WMM UP

Wireless Multi Media (WMM) Up receiver

Avg jitter

Estimated average RTP packet jitter (dynamic delay that a packet encounters when going through the network).

Max jitter

Maximum jitter observed since the receiving voice stream was opened.

Receiver discarded

Rcvr lost packets

Cumulative conceal ratio

Total number of concealment frames divided by total number of speech frames received from start of the voice stream.

Interval conceal ratio

Ratio of concealment frames to speech frames in preceding 3-second interval of active speech. If using voice activity detection
                                                   (VAD), a longer interval might be required to accumulate 3 seconds of active speech.

Max conceal ratio

Highest interval concealment ratio from start of the voice stream.

Severely conceal seconds

Number of seconds that have more than 5 percent concealment events (lost frames) from the start of the voice stream.

Latency

##### Trace Settings

The Trace settings menu gives you information for troubleshooting parameters.

Field

Description

Remote syslog

Support of remote system logging

Log profile

Type of logging

Additional debugs

Not currently supported

## Statistics Available from the Phone Web Pages

You can use the phone web pages to see statistics and other phone information from the web. These pages display the same information
                              that you can see if you access the statistics on the phone.

These pages can help you troubleshoot problems, no matter where your user is located.

### Access Web Page
                           	 for Phone

To access
                                 		  the web page for a phone, follow these steps:

If you cannot
                                             			 access the web page, it may be disabled by default.

Obtain the IP
                                          			 address of the Cisco IP Phone by using one of these methods:

Search for
                                                				  the phone in Cisco Unified Communications Manager Administration by choosing Device > Phone . Phones that register with Cisco
                                                				  Unified Communications Manager display the IP address on the Find and List
                                                   				  Phones window and at the top of the Phone Configuration window.

On the
                                                				  Cisco IP Phone, access the Settings app,
                                                					 select Phone information > Device information > Network > IPv4 , and then scroll to the IP
                                                					 Address field.

Open a web
                                          			 browser and enter the following URL, where IP_address is the IP
                                          			 address of the Cisco IP Phone:

http:// IP_address

### Device Information Web Page

The Device Information page is the first page you see when you access the Phone web pages. Use the left pane to navigate to the other pages.

Field

Description

Active network interface

Active network type

MAC address

Media Access Control (MAC) address of the phone

Wireless MAC address

Wireless Media Access Control (MAC) address of the phone

Host name

Unique, fixed name that is automatically assigned to the phone based on the MAC address.

Phone DN

Directory number assigned to the phone

App load ID

Firmware version running on the phone

Boot load ID

Version of the boot firmware

Version

Firmware version running on the phone

Hardware revision

Version of the phone hardware

Serial number

Serial number of the phone

Model number

Model name of the phone

Message waiting

State of the message waiting indicator

UDI

Information about the phone (type, model name, model ID, hardware version, and serial number)

Time

Current time

Time zone

Current time zone

Date

Current date

System free memory

Amount of unused memory in the phone

Java heap free memory

Free internal Java heap memory

Java pool free memory

Free internal Java pool memory

FIPS mode enabled

Not currently supported

Battery health

Overall health of the battery

Battery temperature

Current temperature of the battery

Battery level

Current battery charge level

### Network Setup Web Page

The Network Setup page gives information about the phone and the network configuration.

Field

Description

MAC address

Media Access Control (MAC) address of the phone

Host name

Unique, fixed name that is automatically assigned to the phone based on the MAC address.

Domain name

Name of the Domain Name System(DNS) domain in which the phone resides.

DHCP server

IP address of the Dynamic Host Configuration Protocol (DHCP) server from which the phone obtains its IP address.

BOOTP server

Not used.

DHCP

Status of DHCP use.

IP address

Internet Protocol (IP) address of the phone.

Subnet mask

Subnet mask used by the phone.

Default router

IP address for the default gateway used by the phone.

DNS server 1

Primary Domain Name System (DNS) server used by the phone.

DNS server 2

Backup DNS server used by the phone.

DNS server 3

Backup DNS server used by the phone.

Alternate TFTP

Alternate Trivial File Transfer Protocol (TFTP) server. Displays Yes if enabled and No if disabled.

TFTP server 1

Primary TFTP server used by the phone.

TFTP server 2

Secondary TFTP server used by the phone.

DHCP address released

Server 1 – 5

Host names or IP addresses, in prioritized order, of the Cisco Unified Communications Manager servers with which the phone
                                             can register. An item can also show the IP address of an Survivable Remote Site Telephony (SRST) router that can provide limited
                                             Cisco Unified Communications Manager functionality, if such a router is available.

Each available server shows the Cisco Unified Communications Manager server IP address and one of the following states:

Cisco Unified Communications Manager server from which the phone is currently receiving call-processing services.

Cisco Unified Communications Manager server to which the phone switches if the current server becomes unavailable.

No current connection to this Cisco Unified Communications Manager server.

Information URL

URL of the help text that appears on the phone.

Directories URL

URL of the server from which the phone obtains directory information.

Messages URL

URL of the server from which the phone obtains message services.

Services URL

URL of the server from which the phone obtains phone services.

Idle URL

URL of an XML service that the phone displays when the phone has not been used for the time specified in the Idle URL Time
                                             option and no menu is open.

For example, you could use the Idle URL option and the Idle URL Time option to display a stock quote or a calendar on the
                                             LCD screen when the phone has not been used for 5 minutes.

Idle URL time

Number of seconds that the phone has not been used and no menu is open before the XML service specified in the Idle URL option
                                             is activated.

Proxy server URL

URL of proxy server, which makes HTTP requests to remote host addresses on behalf of the phone HTTP client and provides responses
                                             from the remote host to the phone HTTP client.

Authentication URL

URL that the phone uses to validate requests made to the phone web server.

User locale

User locale associated with the phone user. Identifies a set of detailed information to support users, including language,
                                             font, date and time formatting, and alphanumeric keyboard text information.

Network locale

Network locale associated with the phone user. Identifies a set of detailed information to support the phone in a specific
                                             location, including definitions of the tones and cadences used by the phone.

User locale version

Version of the user locale loaded on the phone.

Network locale version

Version of the network locale loaded on the phone.

Speaker enabled

Status of  the speakerphone.

GARP enabled

Status of Gratuitous ARP. When enabled, the phone learns MAC addresses from Gratuitous ARP responses.

Auto line select enabled

DSCP for call control

Differentiated Services Code Point (DSCP) IP classification for call control signaling.

DSCP for configuration

DSCP IP classification for any phone configuration transfer.

DSCP for services

DSCP IP classification for phone-based service.

Security mode

Mode set for the phone.

Web access

Indicates whether access to phone web pages is enabled (Yes) or disabled (No).

SSH access enabled

Indicates if SSH access is permitted

Load server

Indicates the IP address of the load server.

CTL file

ITL file

ITL signature

CAPF server

TVS

TFTP server

TFTP server

DF_BIT

Indicates the DF bit setting for packets.

### Network Web Page

When you select the Network hyperlink under Network statistics, the Port information page displays.

Field

Description

tx bytes

Number of bytes transmitted

rx bytes

Number of bytes received

tx packets

Number of packets transmitted by the phone

rx packets

Number of packets received by the phone

tx packets dropped

rx packets dropped

tx packet errors

rx packet errors

Number of error packets received by the phone

Tx frames

Number of frames transmitted

tx multicast frames

Number of multicast packets transmitted by the phone

tx retry

Number of times the phone retried and failed to send packets

tc multi retry

Number of times the phone retried to send multicast packets

tx failure

Number of transmission failures

rts success

Number of request to send (RTS) successes

rts failure

Number of request to send (RTS) failures

ack failure

Number of packet acknowledgments that failed

rx duplicate frames

Number of duplicate frames received.

rx fragmented packets

Number of fragmented packets received

Roaming count

### Console Logs Web Page

The Console logs page contains links to log files that Cisco TAC might need to troubleshoot problems. For instructions on how to download
                                 the logs, see Capture Phone Logs .

### Core Dumps Web Page

The Core dumps page contains information that Cisco TAC needs to troubleshoot problems.

### Status Messages Web Page

The Status messages page provides a list of status messages and each message has a date and time stamp. You can use these messages to troubleshoot
                                 problems.

### Debug Display Web Page

The Debug page shows recent messages and each message contains the date and time. You can use these messages when you troubleshoot problems.

### Streaming Statistics Web Page

The phone has five Stream pages. All the pages have the same fields. These pages give you information about calls when you troubleshoot problems.

Field

Description

Remote address

IP address of the caller

Local address

IP address of the phone

Start time

Timestamp for the call

Stream status

Host name

Name of the phone

Sender packets

Number of RTP voice packets transmitted since the voice stream opened.

This number is not necessarily identical to the number of RTP voice packets transmitted since the call began because the call
                                             might have been placed on hold.

Sender octets

Total number of octets sent by the phone.

Sender codec

Type of audio encoding sent by the phone: G.729, G.711 u-law, G.711 A-law

Sender reports sent

Sender report time sent

Rcvr lost packets

Number of missing RTP packets (lost in transit)

Avg jitter

Estimated average RTP packet jitter (dynamic delay that a packet encounters when going through the network).

Receiver codec

Type of audio encoding received by the phone: G.729, G.711 u-law, G.711 A-law

Receiver reports sent

Number of times this streaming statistics report has been accessed from the web page (resets when the phone resets)

Receiver report time sent

Rcvr packets

Number of packets received by the phone

Rcvr octets

Total number of octets received by the phone.

Transmitter DSCP

Receiver DSCP

Transmitter WMM UP

Receiver WMM UP

MOS LQK

Score that is an objective estimate of the mean opinion score (MOS) for listening quality (LQK) that rates from 5 (excellent)
                                             to 1 (bad). This score is based on audible concealment events due to frame loss in the preceding 8-second interval of the
                                             voice stream.

The MOS LQK score can vary based on the type of codec that the phone uses.

Avg MOS LQK

Average MOS LQK score observed for the entire voice stream.

Min MOS LQK

Lowest MOS LQK score observed from start of the voice stream

Max MOS LQK

Baseline or highest MOS LQK score observed from start of the voice stream.

These codecs provide the following maximum MOS LQK score under normal conditions with no frame loss:

G.711 gives 4.5

G.729 A /AB gives 3.7

MOS LQK version

Version of the Cisco proprietary algorithm used to calculate MOS LQK scores

Cumulative conceal ratio

Total number of concealment frames divided by total number of speech frames received from start of the voice stream.

Interval conceal ratio

Ratio of concealment frames to speech frames in preceding 3-second interval of active speech. If using voice activity detection
                                             (VAD), a longer interval might be required to accumulate 3 seconds of active speech

Max conceal ratio

Highest interval concealment ratio from start of the voice stream.

Conceal seconds

Number of seconds that have concealment events (lost frames) from the start of the voice stream (includes severely concealed
                                             seconds)

Severely conceal seconds

Number of seconds that have more than 5 percent concealment events (lost frames) from the start of the voice stream.

Latency

Max jitter

Maximum jitter observed since the receiving voice stream was opened.

Sender size

Sender reports received

Sender report time received

Receiver size

Receiver discarded

Receiver reports received

Receiver report time received

Rcvr encrypted

Sender encrypted

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Phone information . |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Phone information > Device information . |
| Step 3 | Select one of the following entries. Call manager —displays information about the call control system. Network —displays information about the IPv4 network. WLAN —displays information about the Wi-Fi connection. HTTP —displays information about configured URLs. Locale —displays information about the language locale. Security —displays information about the security settings. QoS —displays information related to the Quality of Service. UI —displays information related to the user interface. Battery —displays information related to the battery. |

| Field | Description |
|---|---|
| Cisco Unified CM 1 | Primary call manager server that the phone uses. Displays the IP address and status. |
| Cisco Unified CM 2 | Secondary call manager server that the phones uses. Displays the IP address and status, or is blank if not in use. |
| Cisco Unified CM 3 | Displays the IP address and status of an additional call manager server, or is blank if not in use. |
| Cisco Unified CM 4 | Displays the IP address and status of an additional call manager server, or is blank if not in use. |
| Cisco Unified CM 5 | Displays the IP address and status of an additional call manager server, or is blank if not in use. |

| Field | Description |
|---|---|
| MAC address | MAC address of the phone. |
| Host name | Unique, fixed name that is automatically assigned to
                                                   					 the phone based on the MAC address. |
| Domain name | Name of the DNS in which the phone resides. |
| DHCP server | IP address of the DHCP server from which the phone
                                                   					 obtains its IP address. |
| IP address | IP address of the phone. |
| Subnet mask | Subnet mask used by the phone. |
| Default router | IP address for the default gateway used by the
                                                   					 phone. |
| DNS server 1 | Primary DNS server used by the phone. |
| DNS server 2 | First backup DNS server used by the phone. |
| DNS server 3 | Second backup DNS server used by the phone. |
| Alternate TFTP | Address of the TFTP server (other than the one assigned by DHCP). |
| TFTP server1 | Primary TFTP server used by the phone. |
| TFTP server 2 | Secondary TFTP server used by the phone. |
| Load server | Host name or IP address for the alternate server that the phone uses for firmware upgrades. |
| BOOTP server |  |
| CDP | Cisco
                                                   					 Discovery Protocol (CDP) usage. |
| GARP | Gratuitous ARP used for MAC address discovery. |

| Field Name | Description |
|---|---|
| Profile name | Name of the network profile that the phone is
                                                   					 currently using. |
| SSID | Service Set ID (SSID) that the phone is currently using. |
| Security mode | Authentication method that the phone is currently
                                                   					 using in the wireless network. |
| 802.11 mode | Wireless signal mode that the phone is currently
                                                   					 using. |
| On call power save | Type of power save mode that the phone uses to save
                                                   					 battery power: PS-Poll or U-APSD. |
| Scan mode | Type of AP scanning. |
| WLAN SCEP server | URL or host name of the Simple Certificate Enrollment Protocol (SCEP)server |
| WLAN Root CA fingerprint | SHA256 or SHA1 fingerprint of the Root CA for WLAN authentication. |

| Field Name | Description |
|---|---|
| Authentication URL | URL that the phone uses to validate requests made to the phone web server. |
| Directories URL | URL of the server from which the phone obtains
                                                   					 directory information. |
| Idle URL | URL of an XML service that the phone displays when the phone has not been used for the time specified in the Idle URL Time
                                                   option and no menu is open. For example, you could use the Idle URL option and the Idle URL Time option to display a stock quote or a calendar on the
                                                   LCD screen when the phone has not been used for 5 minutes. |
| Idle time | Number of seconds that the phone has not been used and no menu is open before the XML service specified in the Idle URL option
                                                   is activated. |
| Information URL | URL of the help text that appears on the phone. |
| Messages URL | URL of the server from which the phone obtains
                                                   					 message services. |
| IP phone proxy address | URL of proxy server, which makes HTTP requests to remote host addresses on behalf of the phone HTTP client and provides responses
                                                   from the remote host to the phone HTTP client. |
| Services URL | URL of the server from which the phone obtains
                                                   					 phone services. |
| Secured authentication URL | Secure URL that the phone uses to validate requests made to the phone web server. |
| Secured directory URL | Secure URL of the server from which the phone obtains
                                                   					 directory information. |
| Secured idle URL | Secure URL of an XML service that the phone displays when the phone has not been used for the time specified in the Idle URL
                                                   Time option and no menu is open. |
| Secured information URL | Secure URL of the help text that appears on the phone. |
| Secured messages URL | Secure URL of the server from which the phone obtains
                                                   					 message services. |
| Secured services URL | Secure URL of the server from which the phone obtains
                                                   					 phone services. |

| Field | Description |
|---|---|
| User locale | User locale associated with the phone user. Identifies a set of detailed information to support users, including language,
                                                   font, date and time formatting, and alphanumeric keyboard text information. |
| Network locale | Network locale associated with the phone user.
                                                   					 Identifies a set of detailed information to support the phone in a specific
                                                   					 location, including definitions of the tones and cadences used by the phone. |
| User locale version | Version of the user locale loaded on the phone. |
| Network locale version | Version of the network locale loaded on the phone. |

| Field | Description |
|---|---|
| Web access | Indicated web access capability for the phone. Disabled No self care portal access. ReadOnly Can view information only. Enabled: HTTP and HTTPS Can use the configuration pages |
| Web admin | Indicates if the web admin page is enabled. |
| Security mode | Security mode assigned to the phone |

| Field Name | Description |
|---|---|
| DSCP for call control | Differentiated Services Code Point (DSCP) IP
                                                   					 classification for call control signaling. |
| DSCP for configuration | DSCP IP classification for any phone configuration
                                                   					 transfer. |
| DSCP for services | DSCP IP classification for phone-based service. |

| Field Name | Description |
|---|---|
| BLF for call lists | Indicates whether the Busy Lamp Field (BLF) is enabled for call
                                                   lists. |
| Reverting focus priority | Indicates whether the phone shifts the call focus on the phone
                                                   screen to an incoming call or a reverting hold call. |
| Personalization | Indicates whether the phone has been enabled for configuration
                                                   of custom ring tones and wallpaper images. |

| Field Name | Description |
|---|---|
| Battery health | Indicates the overall health of the battery. |
| Battery temperature | Indicates the current temperature of the battery. If the battery runs excessively hot, the battery may fail soon. |
| Battery level | Indicates the current charge level of the battery. |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Phone information > Model information . |

| Field Name | Description |
|---|---|
| Model number | Set to CP-8821 or CP-8821-EX |
| MAC address | MAC address of the phone |
| App load ID | Firmware version running on the phone |
| Serial number | Phone serial number |
| USB vendor ID | Set to Cisco |
| USB product ID | Set to 8821 or 8821-EX |
| RNDIS device address | Remote Network Device Interface Specification (RNDIS) address of the USB |
| RNDIS host address | RNDIS for the USB |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Phone information > Firmware version . |

| Field Name | Description |
|---|---|
| Active load | Firmware load that is active |
| Last upgrade | Upgrade status: date and time for successful update; otherwise messages about upgrade failure |
| Boot load ID | Identification of the boot loader version |
| WLAN driver ID | Identification of the WLAN driver |
| WLAN firmware ID | Identification of the WLAN firmware load |

| Step 1 | Access the Settings app. |
|---|---|
| Step 2 | Select Admin settings > Status . |

| Field | Description |
|---|---|
| tx bytes | Number of bytes transmitted |
| rx bytes | Number of bytes received |
| tx packets | Number of packet transmitted |
| rx packets | Number of packet received |
| tx packets dropped | Number of packets transmitted that were dropped |
| rx packets dropped | Number of packets received that were dropped |
| tx packets errors | Number of transmitted packet errors |
| rx packets errors | Number of transmitted packet errors |
| tx frames | Number of frames transmitted |
| tx multicast frames | Number of multicast frames transmitted |
| tx retry | Number of transmission retries |
| tx multi retry | Number of muilticast transmission retries |
| tx failure | Number of transmission failures |
| rts success | Number of request to send (rts) successes |
| rts failure | Number of rts failures |
| ack failure |  |
| rx duplicate frames | Number of duplicate frames received |
| rx fragmented packets | Number of fragmented packets received |
| Roaming count |  |

| Field | Description |
|---|---|
| Receiver codec | Type of audio encoding received by the phone: G.729, G.711 u-law, G.711 A-law |
| Sender codec | Type of audio encoding sent by the phone: G.729, G.711 u-law, G.711 A-law |
| Receiver size |  |
| Sender size |  |
| Rcvr packets | Number of packets received by the phone |
| Sender packets |  |
| Transmitter DSCP |  |
| Receiver DSCP |  |
| Transmitter WMM UP | Wireless Multi Media (WMM) Up transmitter |
| Receiver WMM UP | Wireless Multi Media (WMM) Up receiver |
| Avg jitter | Estimated average RTP packet jitter (dynamic delay that a packet encounters when going through the network). |
| Max jitter | Maximum jitter observed since the receiving voice stream was opened. |
| Receiver discarded |  |
| Rcvr lost packets |  |
| Cumulative conceal ratio | Total number of concealment frames divided by total number of speech frames received from start of the voice stream. |
| Interval conceal ratio | Ratio of concealment frames to speech frames in preceding 3-second interval of active speech. If using voice activity detection
                                                   (VAD), a longer interval might be required to accumulate 3 seconds of active speech. |
| Max conceal ratio | Highest interval concealment ratio from start of the voice stream. |
| Severely conceal seconds | Number of seconds that have more than 5 percent concealment events (lost frames) from the start of the voice stream. |
| Latency |  |

| Field | Description |
|---|---|
| Remote syslog | Support of remote system logging |
| Log profile | Type of logging |
| Additional debugs | Not currently supported |

| Note | If you cannot
                                             			 access the web page, it may be disabled by default. |
|---|---|

| Step 1 | Obtain the IP
                                          			 address of the Cisco IP Phone by using one of these methods: Search for
                                                				  the phone in Cisco Unified Communications Manager Administration by choosing Device > Phone . Phones that register with Cisco
                                                				  Unified Communications Manager display the IP address on the Find and List
                                                   				  Phones window and at the top of the Phone Configuration window. On the
                                                				  Cisco IP Phone, access the Settings app,
                                                					 select Phone information > Device information > Network > IPv4 , and then scroll to the IP
                                                					 Address field. |
|---|---|
| Step 2 | Open a web
                                          			 browser and enter the following URL, where IP_address is the IP
                                          			 address of the Cisco IP Phone: http:// IP_address |

| Field | Description |
|---|---|
| Active network interface | Active network type |
| MAC address | Media Access Control (MAC) address of the phone |
| Wireless MAC address | Wireless Media Access Control (MAC) address of the phone |
| Host name | Unique, fixed name that is automatically assigned to the phone based on the MAC address. |
| Phone DN | Directory number assigned to the phone |
| App load ID | Firmware version running on the phone |
| Boot load ID | Version of the boot firmware |
| Version | Firmware version running on the phone |
| Hardware revision | Version of the phone hardware |
| Serial number | Serial number of the phone |
| Model number | Model name of the phone |
| Message waiting | State of the message waiting indicator |
| UDI | Information about the phone (type, model name, model ID, hardware version, and serial number) |
| Time | Current time |
| Time zone | Current time zone |
| Date | Current date |
| System free memory | Amount of unused memory in the phone |
| Java heap free memory | Free internal Java heap memory |
| Java pool free memory | Free internal Java pool memory |
| FIPS mode enabled | Not currently supported |
| Battery health | Overall health of the battery |
| Battery temperature | Current temperature of the battery |
| Battery level | Current battery charge level |

| Field | Description |
|---|---|
| MAC address | Media Access Control (MAC) address of the phone |
| Host name | Unique, fixed name that is automatically assigned to the phone based on the MAC address. |
| Domain name | Name of the Domain Name System(DNS) domain in which the phone resides. |
| DHCP server | IP address of the Dynamic Host Configuration Protocol (DHCP) server from which the phone obtains its IP address. |
| BOOTP server | Not used. |
| DHCP | Status of DHCP use. |
| IP address | Internet Protocol (IP) address of the phone. |
| Subnet mask | Subnet mask used by the phone. |
| Default router | IP address for the default gateway used by the phone. |
| DNS server 1 | Primary Domain Name System (DNS) server used by the phone. |
| DNS server 2 | Backup DNS server used by the phone. |
| DNS server 3 | Backup DNS server used by the phone. |
| Alternate TFTP | Alternate Trivial File Transfer Protocol (TFTP) server. Displays Yes if enabled and No if disabled. |
| TFTP server 1 | Primary TFTP server used by the phone. |
| TFTP server 2 | Secondary TFTP server used by the phone. |
| DHCP address released |  |
| Server 1 – 5 | Host names or IP addresses, in prioritized order, of the Cisco Unified Communications Manager servers with which the phone
                                             can register. An item can also show the IP address of an Survivable Remote Site Telephony (SRST) router that can provide limited
                                             Cisco Unified Communications Manager functionality, if such a router is available. Each available server shows the Cisco Unified Communications Manager server IP address and one of the following states: Active Cisco Unified Communications Manager server from which the phone is currently receiving call-processing services. Standby Cisco Unified Communications Manager server to which the phone switches if the current server becomes unavailable. Blank No current connection to this Cisco Unified Communications Manager server. |
| Information URL | URL of the help text that appears on the phone. |
| Directories URL | URL of the server from which the phone obtains directory information. |
| Messages URL | URL of the server from which the phone obtains message services. |
| Services URL | URL of the server from which the phone obtains phone services. |
| Idle URL | URL of an XML service that the phone displays when the phone has not been used for the time specified in the Idle URL Time
                                             option and no menu is open. For example, you could use the Idle URL option and the Idle URL Time option to display a stock quote or a calendar on the
                                             LCD screen when the phone has not been used for 5 minutes. |
| Idle URL time | Number of seconds that the phone has not been used and no menu is open before the XML service specified in the Idle URL option
                                             is activated. |
| Proxy server URL | URL of proxy server, which makes HTTP requests to remote host addresses on behalf of the phone HTTP client and provides responses
                                             from the remote host to the phone HTTP client. |
| Authentication URL | URL that the phone uses to validate requests made to the phone web server. |
| User locale | User locale associated with the phone user. Identifies a set of detailed information to support users, including language,
                                             font, date and time formatting, and alphanumeric keyboard text information. |
| Network locale | Network locale associated with the phone user. Identifies a set of detailed information to support the phone in a specific
                                             location, including definitions of the tones and cadences used by the phone. |
| User locale version | Version of the user locale loaded on the phone. |
| Network locale version | Version of the network locale loaded on the phone. |
| Speaker enabled | Status of  the speakerphone. |
| GARP enabled | Status of Gratuitous ARP. When enabled, the phone learns MAC addresses from Gratuitous ARP responses. |
| Auto line select enabled |  |
| DSCP for call control | Differentiated Services Code Point (DSCP) IP classification for call control signaling. |
| DSCP for configuration | DSCP IP classification for any phone configuration transfer. |
| DSCP for services | DSCP IP classification for phone-based service. |
| Security mode | Mode set for the phone. |
| Web access | Indicates whether access to phone web pages is enabled (Yes) or disabled (No). |
| SSH access enabled | Indicates if SSH access is permitted |
| Load server | Indicates the IP address of the load server. |
| CTL file |  |
| ITL file |  |
| ITL signature |  |
| CAPF server |  |
| TVS |  |
| TFTP server |  |
| TFTP server |  |
| DF_BIT | Indicates the DF bit setting for packets. |

| Field | Description |
|---|---|
| tx bytes | Number of bytes transmitted |
| rx bytes | Number of bytes received |
| tx packets | Number of packets transmitted by the phone |
| rx packets | Number of packets received by the phone |
| tx packets dropped |  |
| rx packets dropped |  |
| tx packet errors |  |
| rx packet errors | Number of error packets received by the phone |
| Tx frames | Number of frames transmitted |
| tx multicast frames | Number of multicast packets transmitted by the phone |
| tx retry | Number of times the phone retried and failed to send packets |
| tc multi retry | Number of times the phone retried to send multicast packets |
| tx failure | Number of transmission failures |
| rts success | Number of request to send (RTS) successes |
| rts failure | Number of request to send (RTS) failures |
| ack failure | Number of packet acknowledgments that failed |
| rx duplicate frames | Number of duplicate frames received. |
| rx fragmented packets | Number of fragmented packets received |
| Roaming count |  |

| Field | Description |
|---|---|
| Remote address | IP address of the caller |
| Local address | IP address of the phone |
| Start time | Timestamp for the call |
| Stream status |  |
| Host name | Name of the phone |
| Sender packets | Number of RTP voice packets transmitted since the voice stream opened. This number is not necessarily identical to the number of RTP voice packets transmitted since the call began because the call
                                             might have been placed on hold. |
| Sender octets | Total number of octets sent by the phone. |
| Sender codec | Type of audio encoding sent by the phone: G.729, G.711 u-law, G.711 A-law |
| Sender reports sent |  |
| Sender report time sent |  |
| Rcvr lost packets | Number of missing RTP packets (lost in transit) |
| Avg jitter | Estimated average RTP packet jitter (dynamic delay that a packet encounters when going through the network). |
| Receiver codec | Type of audio encoding received by the phone: G.729, G.711 u-law, G.711 A-law |
| Receiver reports sent | Number of times this streaming statistics report has been accessed from the web page (resets when the phone resets) |
| Receiver report time sent |  |
| Rcvr packets | Number of packets received by the phone |
| Rcvr octets | Total number of octets received by the phone. |
| Transmitter DSCP |  |
| Receiver DSCP |  |
| Transmitter WMM UP |  |
| Receiver WMM UP |  |
| MOS LQK | Score that is an objective estimate of the mean opinion score (MOS) for listening quality (LQK) that rates from 5 (excellent)
                                             to 1 (bad). This score is based on audible concealment events due to frame loss in the preceding 8-second interval of the
                                             voice stream. The MOS LQK score can vary based on the type of codec that the phone uses. |
| Avg MOS LQK | Average MOS LQK score observed for the entire voice stream. |
| Min MOS LQK | Lowest MOS LQK score observed from start of the voice stream |
| Max MOS LQK | Baseline or highest MOS LQK score observed from start of the voice stream. These codecs provide the following maximum MOS LQK score under normal conditions with no frame loss: G.711 gives 4.5 G.729 A /AB gives 3.7 |
| MOS LQK version | Version of the Cisco proprietary algorithm used to calculate MOS LQK scores |
| Cumulative conceal ratio | Total number of concealment frames divided by total number of speech frames received from start of the voice stream. |
| Interval conceal ratio | Ratio of concealment frames to speech frames in preceding 3-second interval of active speech. If using voice activity detection
                                             (VAD), a longer interval might be required to accumulate 3 seconds of active speech |
| Max conceal ratio | Highest interval concealment ratio from start of the voice stream. |
| Conceal seconds | Number of seconds that have concealment events (lost frames) from the start of the voice stream (includes severely concealed
                                             seconds) |
| Severely conceal seconds | Number of seconds that have more than 5 percent concealment events (lost frames) from the start of the voice stream. |
| Latency |  |
| Max jitter | Maximum jitter observed since the receiving voice stream was opened. |
| Sender size |  |
| Sender reports received |  |
| Sender report time received |  |
| Receiver size |  |
| Receiver discarded |  |
| Receiver reports received |  |
| Receiver report time received |  |
| Rcvr encrypted |  |
| Sender encrypted |  |