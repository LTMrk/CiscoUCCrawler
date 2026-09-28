---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-dx-series-admin-1025-dx00-bk-cb112361-00-cisco-dx-series-ag-1025-dx00-bk-cb1-cdf5e1acd0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/dx/series/admin/1025/DX00_BK_CB112361_00_cisco-dx-series-ag-1025/DX00_BK_CB112361_00_cisco-dx-series-ag-1025_chapter_01101.html
retrieved_at: 2026-08-21T20:58:58.073637+00:00
---

Cisco DX Series Administration Guide, Release 10.2(5)

# Cisco DX Series Administration Guide, Release 10.2(5)

Updated: December 8, 2015

Chapter: Model Information Status and Statistics

## Chapter: Model Information Status and Statistics

# Model Information Status and Statistics

## Model Information

To display model information, choose About
                                 				device in the Settings application. The Model Information screen includes the
                              		  items that are listed in the following table.

Item

Description

Status

Submenu that provides additional information about 
                                          					 the device.

Cisco user guide

Provides link to documentation.

Legal information

Includes open-source licenses.

Model number

Model number.

Android version

Indicates version of Android.

Kernel version

Linux kernel number.

Build number

Current software build.

SELinux status

Indicates enforcing or permissive.

Cisco load information

Active load

Version of firmware that is currently installed.

Last upgrade

Date of the most recent firmware upgrade.

An 
                                                      						"Upgrade Progress" message appears
                                                      						under 
                                                      						"Cisco load information" group if 
                                                      						the device is
                                                      						upgrading.

Cisco Unified Communications Manager

Active server

DNS or IP address of the server to which 
                                          					 the device is
                                          					 registered.

Standby Server

DNS or IP address of the standby server.

Cisco Collaboration Problem Reporting Tool

Cisco Collaboration  Problem Reporting Tool

Tool for reporting problems. Tap to
                                          					 select and enter date, time, problem application problem description, and customer support email
                                          					 address. Tap Create email report to gather log information and send
                                          					 to support.

If the user is connected to a secure or authenticated server,
                              		  a corresponding icon (lock or certificate) is displayed on the home screen to
                              		  the right of the server option. If the user is not connected to a secure or
                              		  authenticated server, no icon appears.

## Device Status

To display the device status, choose About
                                    				device > Status in the Settings application.

Item

Description

Status Messages

Provides the Status Messages screen, which shows a log of
                                          					 important system messages.

MDN

Indicates device mobile directory  number.

IP address

Indicates device IP address.

Wi-Fi MAC address

Provides the MAC address of the current Wi-Fi connection.

Ethernet MAC address

Provides the MAC address of the current Ethernet connection.

Bluetooth address

Provides the MAC address of the Bluetooth chipset.

DHCP information

Displays DHCP information screen.

Up time

Run time for 
                                          					 the device.

Current access point

Provides the Current access point screen, if applicable.

Ethernet Statistics

Provides the Ethernet statistics screen, which shows Ethernet
                                          					 traffic statistics.

WLAN statistics

Provides the WLAN statistics screen if applicable.

Call statistics (audio)

Provides counters and statistics for the audio portion of the
                                          					 current call.

Call statistics (video)

Provides counters and statistics for the video portion of the
                                          					 current call.

Call statistics (presentation)

Provides counters and statistics for the presentation portion of the
                                          					 current call.

### Status Messages

The Status Messages screen lists the 50 most recent status
                                 		  messages that 
                                 		  the device has generated. The
                                 		  following table describes the status messages that might appear. This table
                                 		  also includes actions you can take to address errors.

To display the Status messages screen, tap Status messages .

To remove current status messages, tap Clear .

To exit the Status messages screen, tap OK .

Message

Description

Possible Explanation and Action

CFG TFTP Size Error

The configuration file is too large for file system.

Power cycle the device.

Checksum Error

Downloaded software file is corrupted.

Obtain a new copy of the device firmware and place it in the
                                             					 TFTPPath directory. Copy files into this directory only when the TFTP server
                                             					 software is shut down; otherwise, the files may be corrupted.

DHCP timeout

DHCP server did not respond.

- Network is busy -
                                                						The errors resolve themselves when the network load reduces.

- No network
                                                						connectivity between the DHCP server and 
                                                						the device - Verify
                                                						the network connections.

- DHCP server is
                                                						down - Check configuration of DHCP server.

- Errors persist -
                                                						Consider assignment of a static IP address.

DNS timeout

DNS server did not respond.

- Network is busy -
                                                						The errors resolve themselves when the network load reduces.

- No network
                                                						connectivity between the DNS server and 
                                                						the device - Verify
                                                						the network connections.

- DNS server is down
                                                						- Check configuration of DNS server.

DNS unknown host

DNS could not resolve the name of the TFTP server or Cisco Unified Communications Manager .

- Verify that the
                                                						hostnames of the TFTP server or Cisco Unified Communications Manager are configured properly in DNS.

- Consider use of IP
                                                						addresses rather than hostnames.

Duplicate IP

Another device is using the IP address that is assigned to the device.

- If 
                                                						the device has a
                                                						static IP address, verify that you have not assigned a duplicate IP address.

- If you are using
                                                						DHCP, check the DHCP server configuration.

Error update locale

One or more localization files could not be found in the
                                             					 TFTPPath directory or were not valid. The locale was not changed.

From Cisco Unified Communications Manager ,
                                             					 check that the following files are located within subdirectories in TFTP
                                             					 File Management:

Located in subdirectory with same name network locale:

- tones.xml

- glyphs.xml

- dictionary.xml

- kate.xml

File not found <Cfg File>

The name-based and default configuration file was not found on
                                             					 the TFTP Server.

The device is not registered with Cisco Unified Communications Manager .

You must manually add the device to Cisco Unified Communications Manager if you are not allowing devices to
                                                      						  auto-register.

- If you are using
                                                   						DHCP, verify that the DHCP server is pointing to the correct TFTP server.

- If you are using
                                                   						static IP addresses, check configuration of the TFTP server.

IP address released

The device is configured to release its IP
                                             					 address.

The device remains idle until it is power cycled or until you reset
                                             					 the DHCP address.

Load rejected HC

The application that was downloaded is not compatible with
                                             					 the device.

Occurs if you were attempting to install a version of software
                                             					 on this device that did not support hardware changes on this device.

Check the load ID assigned to the device (from Cisco Unified Communications Manager , choose Device > Phone ).
                                             					 Reenter the load that is displayed on the device.

No default router

DHCP or static configuration did not specify a default router.

- If 
                                                						the device has a
                                                						static IP address, verify that the default router has been configured.

- If you are using
                                                						DHCP, the DHCP server has not provided a default router. Check the DHCP server
                                                						configuration.

No DNS server IP

A name was specified but DHCP or static IP configuration did
                                             					 not specify a DNS server address.

- If 
                                                						the device has a
                                                						static IP address, verify that the DNS server has been configured.

- If you are using
                                                						DHCP, the DHCP server has not provided a DNS server. Check the DHCP server
                                                						configuration.

No Trust List installed

The CTL file or the ITL file is not installed on the device.

The Trust List is not configured on Cisco Unified Communications Manager , which does not support security by default.

For more information about the Trust List, see the Cisco Unified Communications Manager Security Guide .

Restart requested by Cisco Unified Communications Manager

The device is restarting based on a request from Cisco Unified Communications Manager .

Configuration changes have likely been made to the device in Cisco Unified Communications Manager , and Apply has been pressed so that the
                                             					 changes take effect.

TFTP access error

TFTP server is pointing to a directory that does not exist.

- If you are using
                                                						DHCP, verify that the DHCP server is pointing to the correct TFTP server.

- If you are using
                                                						static IP addresses, check configuration of TFTP server.

TFTP error

The device does not recognize an error code that  the
                                             					 TFTP server provided.

Contact Cisco Technical Assistance Center (TAC).

TFTP timeout

TFTP server did not respond.

- Network is busy -
                                                						The errors resolve themselves when the network load diminishes.

- No network
                                                						connectivity between the TFTP server and 
                                                						the device - Verify
                                                						the network connections.

- TFTP server is
                                                						down - Check configuration of TFTP server.

Timed Out

Supplicant attempted 802.1X transaction but timed out due to the
                                             					 absence of an authenticator.

Authentication typically times out if 802.1X is not configured
                                             					 on the switch.

Trust List update failed, verification failure

Updating CTL and ITL files failed.

Message displayed in case of error.

Version error

The name of the load file is incorrect.

Make sure that the device load file has the correct name.

XmlDefault.cnf.xml, or .cnf.xml corresponding to the
                                             					 device name

Name of the configuration file.

None. This configuration file provides an informational
                                             					 message that indicates the name of the configuration file.

### Ethernet Statistics

The Ethernet Statistics screen provides information about
                                 		  the device and network performance. The following table describes the
                                 		  information that appears on this screen.

To display Ethernet Statistics, choose About
                                       				device > Status > Ethernet
                                       				statistics in the Settings application.

To reset the Rx Frames, Tx Frames, and Rx Broadcasts
                                 		  statistics to 0, tap Clear .

To exit the Ethernet statistics screen, tap OK .

Item

Description

Rx Frames

Number of packets received

Tx Frames

Number of packets sent

Rx Broadcasts

Number of broadcast packets received

Port 1

Speed and duplex for switch port

Port 2

Speed and duplex for PC port

CDP status

Current CDP status

### WLAN Statistics

The WLAN Statistics screen provides statistics about the
                                 		   
                                 		  device and WLAN. The following
                                 		  table describes the information that appears on this screen.

To display the WLAN Statistics screen, choose About
                                       				device > Status > WLAN
                                       				statistics .

To exit the WLAN statistics screen, tap OK .

Item

Description

tx bytes

Number of bytes transmitted

rx bytes

Number of bytes received

tx  packets

Number of data packets transmitted

rx packets

Number of data packets received

tx packets dropped

Number of transmitted data packets dropped

rx packets dropped

Number of received data packets dropped

tx packet errors

Number of transmitted data packet errors

rx packet errors

Number of received data packet errors

Tx frames

Number of frames transmitted

tx multicast frames

Number of frames transmitted as broadcast or multicast

tx retry

Number of messages retransmitted a single time being
                                             					 acknowledged by the receiving device

tx multi retry

Number of transmit retries prior to success

tx failure

Number of frames that failed to be transmitted

rts success

A corresponding CTS was received

rts failure

Number of frames that failed to be received.

ack failure

Access point did not acknowledge a transmission

rx duplicate frames

Number of duplicate multicast packets transmitted

rx fragmented packets

Number of fragmented packets received

roaming count

Number of times roamed from current access point

### Audio Call Statistics

Access Call Statistics (audio) on 
                                 		  the device to display
                                 		  counters, statistics, and voice-quality metrics for the most recent call.

You can use
                                             			 a web browser to access the Streaming Statistics web page and remotely view the call statistics information. This web
                                             page
                                             			 contains additional RTP Control Protocol (RTCP) statistics that are not available on 
                                             			 the device.

A single call can have multiple voice streams, but data is
                                 		  captured only for the last voice stream. A voice stream is a packet stream
                                 		  between two endpoints. If one endpoint is put on hold, the voice stream stops
                                 		  even though the call is still connected. When the call resumes, a new voice
                                 		  packet stream begins, and the new call data overwrites the former call data.

To display  Call Statistics (audio) for information about
                                 		  the latest voice stream, choose Settings > About
                                       				device > Status > Call statistics
                                       				(audio) .

The following table lists and describes the items that the
                                 		  Call statistics (audio) screen provides.

Item

Description

Rcvr codec

Type of voice stream received (RTP streaming audio from
                                             					 codec):  AAC-LD, G.722, iSAC, G.711 u-law, G.711 A-law, iLBC and G.729.

Sender codec

Type of voice stream transmitted (RTP streaming audio from
                                             					 codec):  AAC-LD, G.722, iSAC, G.711 u-law, G.711 A-law, iLBC and G.729.

Rcvr size

Size of voice packets, in milliseconds, in the receiving voice
                                             					 stream (RTP streaming audio).

Sender size

Size of voice packets, in milliseconds, in the transmitting
                                             					 voice stream.

Rcvr packets

Number of RTP voice packets received since voice stream was
                                             					 opened.

This number is not necessarily identical to the number of
                                                         						RTP voice packets received since the call began, because the call might have
                                                         						been placed on hold.

Sender packets

Number of RTP voice packets transmitted since voice stream was
                                             					 opened.

This number is not necessarily identical to the number of
                                                         						RTP voice packets transmitted since the call began, because the call might have
                                                         						been placed on hold.

Avg jitter

Estimated average RTP packet jitter (dynamic delay that a
                                             					 packet encounters when going through the network), in milliseconds, observed
                                             					 since the receiving voice stream was opened.

Max jitter

Maximum jitter, in milliseconds, observed since the receiving
                                             					 voice stream was opened.

Rcvr discarded

Number of RTP packets in the receiving voice stream that have
                                             					 been discarded (bad packets, too late, and so on).

The device discards
                                                         						payload type 19 comfort noise packets that Cisco gateways generate, which
                                                         						increments this counter.

Rcvr lost packets

Missing RTP packets (lost in transit).

The percentage of missing RTP packets is shown in parentheses.

Cumulative conceal ratio

Total number of concealment frames divided by total number of speech frames received from start of the voice stream.

Interval conceal ratio

Ratio of concealment frames to speech frames in preceding three-second interval of active speech. If voice activity detection
                                             (VAD) is in use, a longer interval might be required to accumulate 3 seconds of active speech.

Max conceal ratio

Highest interval concealment ratio from start of the voice stream.

Conceal secs

Number of seconds that have concealment events (lost frames) from the start of the voice stream (includes severely concealed
                                             seconds).

Severely conceal secs

Number of seconds that have more than 5 percent concealment events (lost frames) from the start of the voice stream.

Latency

Estimate of the network latency, expressed in milliseconds.
                                             					 Represents a running average of the round-trip delay, measured when RTCP
                                             					 receiver report blocks are received.

Sender DSCP

DSCP value for sender SIP signaling packets

Receiver DSCP

DSCP value for receiver SIP signaling packets

Sender RTCP DSCP

DSCP value for sender RTP packets

Receiver RTCP DSCP

DSCP value for sender RTP packets

| Item | Description |
|---|---|
| Status | Submenu that provides additional information about 
                                          					 the device. |
| Cisco user guide | Provides link to documentation. |
| Legal information | Includes open-source licenses. |
| Model number | Model number. |
| Android version | Indicates version of Android. |
| Kernel version | Linux kernel number. |
| Build number | Current software build. |
| SELinux status | Indicates enforcing or permissive. |
| Cisco load information |
| Active load | Version of firmware that is currently installed. |
| Last upgrade | Date of the most recent firmware upgrade. |
| Note An 
                                                      						"Upgrade Progress" message appears
                                                      						under 
                                                      						"Cisco load information" group if 
                                                      						the device is
                                                      						upgrading. | Note | An 
                                                      						"Upgrade Progress" message appears
                                                      						under 
                                                      						"Cisco load information" group if 
                                                      						the device is
                                                      						upgrading. |
| Note | An 
                                                      						"Upgrade Progress" message appears
                                                      						under 
                                                      						"Cisco load information" group if 
                                                      						the device is
                                                      						upgrading. |
| Cisco Unified Communications Manager |
| Active server | DNS or IP address of the server to which 
                                          					 the device is
                                          					 registered. |
| Standby Server | DNS or IP address of the standby server. |
| Cisco Collaboration Problem Reporting Tool |
| Cisco Collaboration  Problem Reporting Tool | Tool for reporting problems. Tap to
                                          					 select and enter date, time, problem application problem description, and customer support email
                                          					 address. Tap Create email report to gather log information and send
                                          					 to support. |

| Note | An 
                                                      						"Upgrade Progress" message appears
                                                      						under 
                                                      						"Cisco load information" group if 
                                                      						the device is
                                                      						upgrading. |
|---|---|

| Item | Description |
|---|---|
| Status Messages | Provides the Status Messages screen, which shows a log of
                                          					 important system messages. |
| MDN | Indicates device mobile directory  number. |
| IP address | Indicates device IP address. |
| Wi-Fi MAC address | Provides the MAC address of the current Wi-Fi connection. |
| Ethernet MAC address | Provides the MAC address of the current Ethernet connection. |
| Bluetooth address | Provides the MAC address of the Bluetooth chipset. |
| DHCP information | Displays DHCP information screen. |
| Up time | Run time for 
                                          					 the device. |
| Current access point | Provides the Current access point screen, if applicable. |
| Ethernet Statistics | Provides the Ethernet statistics screen, which shows Ethernet
                                          					 traffic statistics. |
| WLAN statistics | Provides the WLAN statistics screen if applicable. |
| Call statistics (audio) | Provides counters and statistics for the audio portion of the
                                          					 current call. |
| Call statistics (video) | Provides counters and statistics for the video portion of the
                                          					 current call. |
| Call statistics (presentation) | Provides counters and statistics for the presentation portion of the
                                          					 current call. |

| Message | Description | Possible Explanation and Action |
|---|---|---|
| CFG TFTP Size Error | The configuration file is too large for file system. | Power cycle the device. |
| Checksum Error | Downloaded software file is corrupted. | Obtain a new copy of the device firmware and place it in the
                                             					 TFTPPath directory. Copy files into this directory only when the TFTP server
                                             					 software is shut down; otherwise, the files may be corrupted. |
| DHCP timeout | DHCP server did not respond. | Network is busy -
                                                						The errors resolve themselves when the network load reduces. No network
                                                						connectivity between the DHCP server and 
                                                						the device - Verify
                                                						the network connections. DHCP server is
                                                						down - Check configuration of DHCP server. Errors persist -
                                                						Consider assignment of a static IP address. |
| DNS timeout | DNS server did not respond. | Network is busy -
                                                						The errors resolve themselves when the network load reduces. No network
                                                						connectivity between the DNS server and 
                                                						the device - Verify
                                                						the network connections. DNS server is down
                                                						- Check configuration of DNS server. |
| DNS unknown host | DNS could not resolve the name of the TFTP server or Cisco Unified Communications Manager . | Verify that the
                                                						hostnames of the TFTP server or Cisco Unified Communications Manager are configured properly in DNS. Consider use of IP
                                                						addresses rather than hostnames. |
| Duplicate IP | Another device is using the IP address that is assigned to the device. | If 
                                                						the device has a
                                                						static IP address, verify that you have not assigned a duplicate IP address. If you are using
                                                						DHCP, check the DHCP server configuration. |
| Error update locale | One or more localization files could not be found in the
                                             					 TFTPPath directory or were not valid. The locale was not changed. | From Cisco Unified Communications Manager ,
                                             					 check that the following files are located within subdirectories in TFTP
                                             					 File Management: Located in subdirectory with same name network locale: tones.xml Located in
                                                						subdirectory with same name user locale: glyphs.xml dictionary.xml kate.xml |
| File not found <Cfg File> | The name-based and default configuration file was not found on
                                             					 the TFTP Server. | The configuration file is created when the device is added to the Cisco Unified Communications Manager database. If the device has not been added to the Cisco Unified Communications Manager database,
                                             					 the TFTP server generates a CFG File Not Found response. The device is not registered with Cisco Unified Communications Manager . You must manually add the device to Cisco Unified Communications Manager if you are not allowing devices to
                                                      						  auto-register. If you are using
                                                   						DHCP, verify that the DHCP server is pointing to the correct TFTP server. If you are using
                                                   						static IP addresses, check configuration of the TFTP server. |
| IP address released | The device is configured to release its IP
                                             					 address. | The device remains idle until it is power cycled or until you reset
                                             					 the DHCP address. |
| Load rejected HC | The application that was downloaded is not compatible with
                                             					 the device. | Occurs if you were attempting to install a version of software
                                             					 on this device that did not support hardware changes on this device. Check the load ID assigned to the device (from Cisco Unified Communications Manager , choose Device > Phone ).
                                             					 Reenter the load that is displayed on the device. |
| No default router | DHCP or static configuration did not specify a default router. | If 
                                                						the device has a
                                                						static IP address, verify that the default router has been configured. If you are using
                                                						DHCP, the DHCP server has not provided a default router. Check the DHCP server
                                                						configuration. |
| No DNS server IP | A name was specified but DHCP or static IP configuration did
                                             					 not specify a DNS server address. | If 
                                                						the device has a
                                                						static IP address, verify that the DNS server has been configured. If you are using
                                                						DHCP, the DHCP server has not provided a DNS server. Check the DHCP server
                                                						configuration. |
| No Trust List installed | The CTL file or the ITL file is not installed on the device. | The Trust List is not configured on Cisco Unified Communications Manager , which does not support security by default. For more information about the Trust List, see the Cisco Unified Communications Manager Security Guide . |
| Restart requested by Cisco Unified Communications Manager | The device is restarting based on a request from Cisco Unified Communications Manager . | Configuration changes have likely been made to the device in Cisco Unified Communications Manager , and Apply has been pressed so that the
                                             					 changes take effect. |
| TFTP access error | TFTP server is pointing to a directory that does not exist. | If you are using
                                                						DHCP, verify that the DHCP server is pointing to the correct TFTP server. If you are using
                                                						static IP addresses, check configuration of TFTP server. |
| TFTP error | The device does not recognize an error code that  the
                                             					 TFTP server provided. | Contact Cisco Technical Assistance Center (TAC). |
| TFTP timeout | TFTP server did not respond. | Network is busy -
                                                						The errors resolve themselves when the network load diminishes. No network
                                                						connectivity between the TFTP server and 
                                                						the device - Verify
                                                						the network connections. TFTP server is
                                                						down - Check configuration of TFTP server. |
| Timed Out | Supplicant attempted 802.1X transaction but timed out due to the
                                             					 absence of an authenticator. | Authentication typically times out if 802.1X is not configured
                                             					 on the switch. |
| Trust List update failed, verification failure | Updating CTL and ITL files failed. | Message displayed in case of error. |
| Version error | The name of the load file is incorrect. | Make sure that the device load file has the correct name. |
| XmlDefault.cnf.xml, or .cnf.xml corresponding to the
                                             					 device name | Name of the configuration file. | None. This configuration file provides an informational
                                             					 message that indicates the name of the configuration file. |

| Item | Description |
|---|---|
| Rx Frames | Number of packets received |
| Tx Frames | Number of packets sent |
| Rx Broadcasts | Number of broadcast packets received |
| Port 1 | Speed and duplex for switch port |
| Port 2 | Speed and duplex for PC port |
| CDP status | Current CDP status |

| Item | Description |
|---|---|
| tx bytes | Number of bytes transmitted |
| rx bytes | Number of bytes received |
| tx  packets | Number of data packets transmitted |
| rx packets | Number of data packets received |
| tx packets dropped | Number of transmitted data packets dropped |
| rx packets dropped | Number of received data packets dropped |
| tx packet errors | Number of transmitted data packet errors |
| rx packet errors | Number of received data packet errors |
| Tx frames | Number of frames transmitted |
| tx multicast frames | Number of frames transmitted as broadcast or multicast |
| tx retry | Number of messages retransmitted a single time being
                                             					 acknowledged by the receiving device |
| tx multi retry | Number of transmit retries prior to success |
| tx failure | Number of frames that failed to be transmitted |
| rts success | A corresponding CTS was received |
| rts failure | Number of frames that failed to be received. |
| ack failure | Access point did not acknowledge a transmission |
| rx duplicate frames | Number of duplicate multicast packets transmitted |
| rx fragmented packets | Number of fragmented packets received |
| roaming count | Number of times roamed from current access point |

| Note | You can use
                                             			 a web browser to access the Streaming Statistics web page and remotely view the call statistics information. This web
                                             page
                                             			 contains additional RTP Control Protocol (RTCP) statistics that are not available on 
                                             			 the device. |
|---|---|

| Item | Description |
|---|---|
| Rcvr codec | Type of voice stream received (RTP streaming audio from
                                             					 codec):  AAC-LD, G.722, iSAC, G.711 u-law, G.711 A-law, iLBC and G.729. |
| Sender codec | Type of voice stream transmitted (RTP streaming audio from
                                             					 codec):  AAC-LD, G.722, iSAC, G.711 u-law, G.711 A-law, iLBC and G.729. |
| Rcvr size | Size of voice packets, in milliseconds, in the receiving voice
                                             					 stream (RTP streaming audio). |
| Sender size | Size of voice packets, in milliseconds, in the transmitting
                                             					 voice stream. |
| Rcvr packets | Number of RTP voice packets received since voice stream was
                                             					 opened. Note This number is not necessarily identical to the number of
                                                         						RTP voice packets received since the call began, because the call might have
                                                         						been placed on hold. | Note | This number is not necessarily identical to the number of
                                                         						RTP voice packets received since the call began, because the call might have
                                                         						been placed on hold. |
| Note | This number is not necessarily identical to the number of
                                                         						RTP voice packets received since the call began, because the call might have
                                                         						been placed on hold. |
| Sender packets | Number of RTP voice packets transmitted since voice stream was
                                             					 opened. Note This number is not necessarily identical to the number of
                                                         						RTP voice packets transmitted since the call began, because the call might have
                                                         						been placed on hold. | Note | This number is not necessarily identical to the number of
                                                         						RTP voice packets transmitted since the call began, because the call might have
                                                         						been placed on hold. |
| Note | This number is not necessarily identical to the number of
                                                         						RTP voice packets transmitted since the call began, because the call might have
                                                         						been placed on hold. |
| Avg jitter | Estimated average RTP packet jitter (dynamic delay that a
                                             					 packet encounters when going through the network), in milliseconds, observed
                                             					 since the receiving voice stream was opened. |
| Max jitter | Maximum jitter, in milliseconds, observed since the receiving
                                             					 voice stream was opened. |
| Rcvr discarded | Number of RTP packets in the receiving voice stream that have
                                             					 been discarded (bad packets, too late, and so on). Note The device discards
                                                         						payload type 19 comfort noise packets that Cisco gateways generate, which
                                                         						increments this counter. | Note | The device discards
                                                         						payload type 19 comfort noise packets that Cisco gateways generate, which
                                                         						increments this counter. |
| Note | The device discards
                                                         						payload type 19 comfort noise packets that Cisco gateways generate, which
                                                         						increments this counter. |
| Rcvr lost packets | Missing RTP packets (lost in transit). The percentage of missing RTP packets is shown in parentheses. |
| Cumulative conceal ratio | Total number of concealment frames divided by total number of speech frames received from start of the voice stream. |
| Interval conceal ratio | Ratio of concealment frames to speech frames in preceding three-second interval of active speech. If voice activity detection
                                             (VAD) is in use, a longer interval might be required to accumulate 3 seconds of active speech. |
| Max conceal ratio | Highest interval concealment ratio from start of the voice stream. |
| Conceal secs | Number of seconds that have concealment events (lost frames) from the start of the voice stream (includes severely concealed
                                             seconds). |
| Severely conceal secs | Number of seconds that have more than 5 percent concealment events (lost frames) from the start of the voice stream. |
| Latency | Estimate of the network latency, expressed in milliseconds.
                                             					 Represents a running average of the round-trip delay, measured when RTCP
                                             					 receiver report blocks are received. |
| Sender DSCP | DSCP value for sender SIP signaling packets |
| Receiver DSCP | DSCP value for receiver SIP signaling packets |
| Sender RTCP DSCP | DSCP value for sender RTP packets |
| Receiver RTCP DSCP | DSCP value for sender RTP packets |

| Note | This number is not necessarily identical to the number of
                                                         						RTP voice packets received since the call began, because the call might have
                                                         						been placed on hold. |
|---|---|

| Note | This number is not necessarily identical to the number of
                                                         						RTP voice packets transmitted since the call began, because the call might have
                                                         						been placed on hold. |
|---|---|

| Note | The device discards
                                                         						payload type 19 comfort noise packets that Cisco gateways generate, which
                                                         						increments this counter. |
|---|---|