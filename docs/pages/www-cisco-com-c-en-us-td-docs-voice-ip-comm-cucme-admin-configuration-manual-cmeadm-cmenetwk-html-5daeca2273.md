---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmenetwk-html-5daeca2273
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmenetwk.html
retrieved_at: 2026-08-21T07:22:05.387742+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Network Parameters

## Chapter: Network Parameters

# Network Parameters

## Prerequisites for Defining Network Parameters

IP routing must be enabled.

VoIP networking must be operational. For quality and security purposes, we recommend you have separate virtual LANs (VLANs)
                                 for data and voice. The IP network assigned to each VLAN should be large enough to support addresses for all nodes on that
                                 VLAN. Cisco Unified CME phones receive their IP addresses from the voice network, whereas all other nodes such as PCs, servers,
                                 and printers receive their IP addresses from the data network. For configuration information, see Configure VLANs on a Cisco Switch .

If applicable, PSTN lines are configured and operational.

If applicable, the WAN links are configured and operational.

Trivial File Transfer Protocol (TFTP) must be enabled on the router
                                 			 to allow IP phones to download phone firmware files.

To support IP phones that are running SIP to be directly connected to the Cisco Unified CME router, Cisco Unified CME 3.4
                                 or later must be installed on the router.

To provide voice-mail support for phones connected to the
                                 			 Cisco Unified CME router, install and configure voice mail on your network.

## Restrictions for Defining Network Parameters

In Cisco Unified CME 4.0 and later versions, Layer-3-to-Layer-2 VLAN Class of Service (CoS) priority marking is not automatically
                           processed. Cisco Unified CME 4.0 and later versions will continue to mark Layer 3, but Layer 2 marking is now only handled
                           in the Cisco IOS software. Any Quality of Service (QoS) design that requires Layer 2 marking will have to be explicitly configured,
                           either on a Catalyst switch that supports this capability or on the Cisco Unified CME router under the Ethernet interface
                           configuration. For configuration information, see Enterprise QoS Solution Reference Network Design Guide .

## Information About Defining Network Parameters

### DHCP Service

When a Cisco Unified IP phone is connected to the Cisco Unified CME
                              		system, it automatically queries for a Dynamic Host Configuration Protocol
                              		(DHCP) server. The DHCP server responds by assigning an IP address to the
                              		Cisco Unified IP phone and providing the IP address of the TFTP server through
                              		DHCP option 150. Then the phone registers with the Cisco Unified CME server and
                              		attempts to get configuration and phone firmware files from the TFTP server.

For configuration information, perform only one of the following procedures to set up DHCP service for your IP
                              		phones:

If your Cisco Unified CME router is the DHCP server and you can use a single shared address pool for all your DHCP clients,
                                    see Configure Single DHCP IP Address Pool .

If your Cisco Unified CME router is the DHCP server and you need separate pools for non-IP-phone DHCP clients, see Configure Separate DHCP IP Address Pool for Each DHCP Client .

If the Cisco Unified CME router is not the DHCP server and you want to relay DHCP requests from IP phones to a DHCP server
                                    on a different router, see Configure DHCP Relay .

### Network Time Protocol for the Cisco Unified CME Router

Network Time Protocol (NTP) allows you to synchronize your Cisco Unified CME router to a single clock on the network, which
                              is known as the clock primary. NTP is disabled on all interfaces by default, but it is essential for Cisco Unified CME so
                              you must ensure that it is enabled. For information about configuring NTP for the Cisco Unified CME router, see Enable Network Time Protocol .

### Olson Timezones

Before Cisco Unified CME 9.0, some Cisco Unified SCCP IP phones and
                              		Cisco Unified SIP IP phones displayed exactly the same time as that of the
                              		Cisco Unified CME. For these phones, the correct time was displayed whenever
                              		the Cisco Unified CME time was set correctly. The clock timezone , clock summer-time , and clock set commands were the only commands used
                              		to set the Cisco Unified CME time correctly.

Other phones used only the time-zone command in telephony-service
                              		configuration mode and the timezone command in voice register global
                              		configuration mode to specify which time zone they were in so that the correct
                              		local time was displayed on Cisco Unified SCCP IP phones and Cisco Unified SIP
                              		IP phones, respectively. The phones calculated and displayed the time based on
                              		the Greenwich Mean Time (GMT) provided by the Cisco Unified CME or the Network
                              		Time Protocol server. The problem with this method is that every time a new
                              		country or new time zone was available or an old time zone was changed, the
                              		Cisco Unified CME time-zone and timezone commands and the phone loads had to be
                              		updated.

In Cisco Unified CME 9.0 and later versions, the Olson Timezone feature
                              		eliminates the need to update time zone commands or phone loads to accommodate
                              		a new country with a new time zone or an existing country whose city or state
                              		wants to change their time zone. Oracle’s Olson Timezone updater tool,
                              		tzupdater.jar, only needs to be current for you to set the correct time using
                              		the olsontimezone command in either
                              		telephony-service or voice register global configuration mode.

For Cisco Unified 3911 and 3951 SIP IP phones and Cisco Unified 6921,
                              		6941, 6945, and 6961 SCCP and SIP IP phones, the correct Olson Timezone updater
                              		file is TzDataCSV.csv. The TzDataCSV.csv file is created based on the
                              		tzupdater.jar file.

To set the correct time zone, you must determine the Olson Timezone
                              		area/location where the Cisco Unified CME is located and download the latest
                              		tzupdater.jar or TzDataCSV.csv to a TFTP server that is accessible to the Cisco
                              		Unified CME, such as flash or slot 0.

After a complete reboot, the phone checks if the version of its
                              		configuration file is earlier or later than 2010o. If it is earlier, the phone
                              		loads the latest tzupdater.jar and uses that updater file to calculate the
                              		Olson Timezone.

To make the Olson Timezone feature backward compatible, both the time-zone and timezone commands are retained as legacy time
                              		zones. Because the olsontimezone command covers approximately 500
                              		time zones (Version 2010o of the tzupdater.jar file supports approximately 453
                              		Olson Timezone IDs.), this command takes precedence when either the time-zone or the timezone command (that covers a total of 90 to
                              		100 time zones only) is present at the same time as the olsontimezone command.

For more information on setting the time zone so that the correct local time is displayed on an IP phone, see Set Olson Timezone for SCCP Phones or Set Olson Timezone for SIP Phones .

### DTMF Relay

IP phones connected to Cisco Unified CME systems require the use of
                              		out-of-band DTMF relay to transport DTMF (keypad) digits across VoIP
                              		connections. The reason for this is that the codecs used for in-band transport
                              		may distort DTMF tones and make them unrecognizable. DTMF relay solves the
                              		problem of DTMF tone distortion by transporting DTMF tones out-of-band, or
                              		separate, from the encoded voice stream.

For IP phones on H.323 networks, DTMF is relayed using the H.245 alphanumeric method, which is defined by the ITU H.245 standard.
                              This method separates DTMF digits from the voice stream and sends them as ASCII characters in H.245 user input indication
                              messages through the H.245 signaling channel instead of the RTP channel. For information about configuring a DTMF relay in
                              a multisite installation, see Configure DTMF Relay for H.323 Networks in Multisite Installations .

To use remote voice-mail or IVR applications on SIP networks from
                              		Cisco Unified CME phones, the DTMF digits used by the Cisco Unified CME phones
                              		must be converted to the RFC 2833 in-band DTMF relay mechanism used by SIP
                              		phones. The SIP DTMF relay method is needed in the following situations:

When SIP is used to connect a Cisco Unified CME system to a remote
                                    			 SIP-based IVR or voice-mail application.

When SIP is used to connect a Cisco Unified CME system to a remote
                                    			 SIP-PSTN voice gateway that goes through the PSTN to a voice-mail or IVR
                                    			 application.

The requirement for out-of-band DTMF relay conversion is limited to SCCP
                              		phones. SIP phones natively support in-band DTMF relay as specified in RFC
                              		2833.

To use voice mail on a SIP network that connects to a Cisco Unity Express system, which uses a nonstandard SIP Notify format,
                              the DTMF digits used by the Cisco Unified CME phones must be converted to the Notify format. Additional configuration may
                              be required for backward compatibility with Cisco CME 3.0 and 3.1. For configuration information about enabling DTMF relay
                              for SIP networks, see Configure SIP Trunk Support .

### SIP Register Support

SIP register support enables a SIP gateway to register E.164 numbers
                              		with a SIP proxy or SIP registrar, similar to the way that H.323 gateways can
                              		register E.164 numbers with a gatekeeper. SIP gateways allow registration of
                              		E.164 numbers to a SIP proxy or registrar on behalf of analog telephone voice
                              		ports (FXS) and IP phone virtual voice ports (EFXS) for local SCCP phones.

When registering E.164 numbers in dial peers with an external registrar, you can also register them with a secondary SIP proxy
                              or registrar to provide redundancy. The secondary registration can be used if the primary registrar fails.

By default, SIP gateways do not generate SIP Register messages, so the gateway must be configured to register the gateway’s
                              E.164 telephone numbers with an external SIP registrar. For information about configuring the SIP gateway to register phone
                              numbers with Cisco Unified CME, see Configure SIP Trunk Support .

## Define Network Parameters

### Enable Calls in
                           	 Your VoIP Network

Restriction

SIP
                                                   				  endpoints are not supported on H.323 trunks. SIP endpoints are supported on SIP
                                                   				  trunks only.

Cisco Unified CME 3.4 and later versions support Media
                                                   				  Flow-through mode only; enabling SIP-to-SIP calls is required before you can
                                                   				  successfully make SIP-to-SIP calls.

Media
                                                   				  Flow-around configured with the media
                                                         						flow-around command is not supported by Cisco Unified CME with
                                                   				  SIP phones.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- allow-connections from - type to to - type

- sip

- registrar server [ expires [ max sec ] [ min sec ] ]

- exit

- sip-ua

- notify telephone-event
                                       				  max-duration time

- registrar { dns: host-name | ipv4: ip-address } expires seconds [ tcp ] [ secondary ]

- retry
                                       				  register number

- timers
                                       				  register time

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters voice
                                             				service configuration mode and specifies Voice over IP (VoIP) encapsulation.

Step 4

allow-connections from - type to to - type

#### Example:

```
Router(config-voi-srv)# allow-connections h323 to h323
```

```
Router(config-voi-srv)# allow-connections h323 to SIP
```

```
Router(config-voi-srv)# allow-connections SIP to SIP
```

Enables calls
                                             				between specific types of endpoints in a VoIP network.

A separate
                                                   					 allow-connections command is required for each type of endpoint to be
                                                   					 supported.

Step 5

sip

#### Example:

```
Router(config-voi-srv)# sip
```

(Optional)
                                             				Enters SIP configuration mode.

Required
                                                   					 if you are connecting IP phones running SIP directly in Cisco CME 3.4 and
                                                   					 later.

Step 6

registrar server [ expires [ max sec ] [ min sec ] ]

#### Example:

```
Router(config-voi-sip)# registrar server expires max 600 min 60
```

(Optional)
                                             				Enables SIP registrar functionality in Cisco Unified CME.

Required
                                                   					 if you are connecting IP phones running SIP directly in Cisco CME 3.4 and
                                                   					 later.

Cisco Unified CME does not maintain a persistent database of
                                                         				  registration entries across reloads. Because SIP phones do not use a keepalive
                                                         				  functionality, the SIP phones must register again. To decrease the amount of
                                                         				  time after which the SIP phones register again, we recommend that you change
                                                         				  the expiry.

max sec —(Optional) Range: 600 to 86400. Default: 3600.
                                                   					 Recommended value: 600.

Ensure that
                                                         				  the registration expiration timeout is set to a value smaller than the TCP
                                                         				  connection aging timeout to avoid disconnection from the TCP.

min sec —(Optional) Range: 60 to 3600. Default: 60.

Step 7

exit

#### Example:

```
Router(config-voi-sip)# exit
```

Exits
                                             				dial-peer configuration mode.

Step 8

sip-ua

#### Example:

```
Router(config)# sip-ua
```

Enters SIP
                                             				user-agent configuration mode.

Step 9

notify telephone-event
                                                				  max-duration time

#### Example:

```
Router(config-sip-ua)# notify telephone-event max-duration 2000
```

Configures
                                             				the maximum time interval allowed between two consecutive NOTIFY messages for a
                                             				single DTMF event.

- max-duration time —Range: 500 to 3000. Default: 2000.

Step 10

registrar { dns: host-name | ipv4: ip-address } expires seconds [ tcp ] [ secondary ]

#### Example:

```
Router(config-sip-ua)# registrar ipv4:10.8.17.40 expires 3600 secondary
```

Registers
                                             				E.164 numbers on behalf of analog telephone voice ports (FXS) and IP phone
                                             				virtual voice ports (EFXS) with an external SIP proxy or SIP registrar server.

Step 11

retry
                                                				  register number

#### Example:

```
Router(config-sip-ua)# retry register 10
```

Sets the
                                             				total number of SIP Register messages that the gateway should send.

number —Number of Register message retries.
                                                   					 Range: 1 to 10. Default: 10.

Step 12

timers
                                                				  register time

#### Example:

```
Router(config-sip-ua)# timers register 500
```

Sets how
                                             				long the SIP user agent (UA) waits before sending Register requests.

time —Waiting time, in milliseconds.
                                                   					 Range: 100 to 1000. Default: 500.

Step 13

end

#### Example:

```
Router(config-sip-ua)# end
```

Exits
                                             				configuration mode and enters privileged EXEC mode.

### Configure
                           	 DHCP

If your Cisco Unified CME router is the DHCP server and you can use
                                       			 a single shared address pool for all your DHCP clients, see Configure Single DHCP IP Address Pool .

If your Cisco Unified CME router is the DHCP server and you need
                                       			 separate pools for each IP phone and each non-IP-phone DHCP client, see Configure Separate DHCP IP Address Pool for Each DHCP Client .

If the Cisco Unified CME router is not the DHCP server and you want
                                       			 to relay DHCP requests from IP phones to a DHCP server on a different router,
                                       			 see Configure DHCP Relay .

#### Configure Single
                              	 DHCP IP Address Pool

To create a shared
                                    		  pool of IP addresses for all DHCP clients, perform the following step.

Do not perform this task if you already have a DHCP server on the LAN that can be used
                                                			 to provide addresses to the Cisco Unified CME phones. See Enable Network Time Protocol .

Restriction

A single DHCP IP
                                                			 address pool cannot be used if non-IP-phone clients, such as PCs, must use a
                                                			 different TFTP server address.

##### Before you begin

Your
                                    		  Cisco Unified CME router is a DHCP server.

### SUMMARY STEPS

- enable

- configure terminal

- ip dhcp pool pool-name

- network ip-address [ mask | / prefix-length ]

- option 150 ip ip-address

- default-router ip-address

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

ip dhcp pool pool-name

##### Example:

```
Router(config)# ip dhcp pool mypool
```

Creates a name
                                                				for the DHCP server address pool and enters DHCP pool configuration mode.

Step 4

network ip-address [ mask | / prefix-length ]

##### Example:

```
Router(config-dhcp)# network 10.0.0.0 255.255.0.0
```

Specifies the
                                                				IP address of the DHCP address pool to be configured.

Step 5

option 150 ip ip-address

##### Example:

```
Router(config-dhcp)# option 150 ip 10.0.0.1
```

Specifies the
                                                				TFTP server address from which the Cisco Unified IP phone downloads the image
                                                				configuration file.

This is
                                                      					 your Cisco Unified CME router’s address.

Step 6

default-router ip-address

##### Example:

```
Router(config-dhcp)# default-router 10.0.0.1
```

(Optional)
                                                				Specifies the router that the IP phones will use to send or receive IP traffic
                                                				that is external to their local subnet.

If the
                                                      					 Cisco Unified CME router is the only router on the network, this address should
                                                      					 be the Cisco Unified CME IP source address. This command can be omitted if IP
                                                      					 phones need to send or receive IP traffic only to or from devices on their
                                                      					 local subnet.

The IP
                                                      					 address that you specify for default router will be used by the IP phones for
                                                      					 fallback purposes. If the Cisco Unified CME IP source address becomes
                                                      					 unreachable, IP phones will attempt to register to the address specified in
                                                      					 this command.

Step 7

end

##### Example:

```
Router(config-dhcp)# end
```

Returns to
                                                				privileged EXEC mode.

##### What to do next

If you are
                                          				configuring Cisco Unified CME for the first time on this router, you are ready
                                          				to configure NTP for the Cisco Unified CME router. For more information, see Enable Network Time Protocol .

If you are
                                          				finished modifying network parameters for an already configured
                                          				Cisco Unified CME router, see Configuration Files for Phones .

#### Configure Separate
                              	 DHCP IP Address Pool for Each DHCP Client

To create a DHCP
                                    		  IP address pool for each DHCP client, including non-IP-phone clients such as
                                    		  PCs, perform the following steps.

Do not perform this task if you already have a DHCP server on the LAN that can be used
                                                			 to provide addresses to the Cisco Unified CME phones. See Enable Network Time Protocol .

Restriction

To use a
                                                			 separate DHCP IP address pool for each DHCP client, make an entry for each IP
                                                			 phone.

##### Before you begin

Your
                                    		  Cisco Unified CME router is a DHCP server.

### SUMMARY STEPS

- enable

- configure terminal

- ip dhcp pool pool-name

- host ip-address
                                          				  subnet-mask

- client-identifier mac-address

- option 150 ip ip-address

- default-router ip-address

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

ip dhcp pool pool-name

##### Example:

```
Router(config)# ip dhcp pool pool2
```

Creates a name
                                                				for the DHCP server address pool and enters DHCP pool configuration mode.

Step 4

host ip-address
                                                   				  subnet-mask

##### Example:

```
Router(config-dhcp)# host 10.0.0.0 255.255.0.0
```

Specifies the
                                                				IP address that you want the phone to get.

Step 5

client-identifier mac-address

##### Example:

```
Router(config-dhcp)# client-identifier 01238.380.3056
```

Specifies the
                                                				MAC address of the phone, which is printed on a label on each
                                                				Cisco Unified IP phone.

A separate
                                                      					 client-identifier command is required for each DHCP client.

Add “01”
                                                      					 prefix number before the MAC address.

Step 6

option 150 ip ip-address

##### Example:

```
Router(config-dhcp)# option 150 ip 10.0.0.1
```

Specifies the
                                                				TFTP server address from which the Cisco Unified IP phone downloads the image
                                                				configuration file.

This is
                                                      					 your Cisco Unified CME router’s address.

Step 7

default-router ip-address

##### Example:

```
Router(config-dhcp)# default-router 10.0.0.1
```

(Optional)
                                                				Specifies the router that the IP phones will use to send or receive IP traffic
                                                				that is external to their local subnet.

If the
                                                      					 Cisco Unified CME router is the only router on the network, this address should
                                                      					 be the Cisco Unified CME IP source address. This command can be omitted if IP
                                                      					 phones need to send or receive IP traffic only to or from devices on their
                                                      					 local subnet.

The IP
                                                      					 address that you specify for default router will be used by the IP phones for
                                                      					 fallback purposes. If the Cisco Unified CME IP source address becomes
                                                      					 unreachable, IP phones will attempt to register to the address specified in
                                                      					 this command.

Step 8

end

##### Example:

```
Router(config-dhcp)# end
```

Returns to
                                                				privileged EXEC mode.

##### What to do next

If you are
                                          				configuring Cisco Unified CME for the first time on this router, you are ready
                                          				to configure NTP for the Cisco Unified CME router. See Enable Network Time Protocol .

If you are
                                          				finished modifying network parameters for an already configured
                                          				Cisco Unified CME router, see Configuration Files for Phones .

#### Configure DHCP
                              	 Relay

To set up DHCP
                                    		  relay on the LAN interface where the Cisco Unified IP phones are connected and
                                    		  enable the DHCP relay to relay requests from the phones to the DHCP server,
                                    		  perform the following steps.

Restriction

The
                                                			 Cisco Unified CME router cannot be the DHCP server.

##### Before you begin

There is a DHCP
                                    		  server that is not on this Cisco Unified CME router on the LAN that can provide
                                    		  addresses to the Cisco Unified CME phones.

### SUMMARY STEPS

- enable

- configure terminal

- service dhcp

- interface type number

- ip helper-address ip -address

- end

### DETAILED STEPS

Step 1

enable

##### Example:

```
Router> enable
```

Enables
                                                				privileged EXEC mode.

Enter your
                                                      					 password if prompted.

Step 2

configure terminal

##### Example:

```
Router# configure terminal
```

Enters global
                                                				configuration mode.

Step 3

service dhcp

##### Example:

```
Router(config)# service dhcp
```

Enables the
                                                				Cisco IOS DHCP server feature on the router.

Step 4

interface type number

##### Example:

```
Router(config)# interface vlan 10
```

Enters
                                                				interface configuration mode for the specified interface.

Step 5

ip helper-address ip -address

##### Example:

```
Router(config-if)# ip helper-address 10.0.0.1
```

Specifies the
                                                				helper address for any unrecognized broadcast for TFTP server and DNS server
                                                				requests.

A separate ip
                                                            						  helper-address command is required for each server if the servers
                                                      					 are on different hosts.

You can
                                                      					 also configure multiple TFTP server targets by using the ip
                                                            						  helper-address commands for multiple servers.

Step 6

end

##### Example:

```
Router(config-if)# end
```

Returns to
                                                				privileged EXEC mode.

##### What to do next

If you are
                                          				configuring Cisco Unified CME for the first time on this router, you are ready
                                          				to configure NTP for the Cisco Unified CME router. See Enable Network Time Protocol .

If you are
                                          				finished modifying network parameters for an already configured
                                          				Cisco Unified CME router, see Configuration Files for Phones .

### Enable Network
                           	 Time Protocol

### SUMMARY STEPS

- enable

- configure terminal

- clock timezone zone hours-offset [ minutes-offset ]

- clock summer-time zone recurring [ week day month hh : mm week day month
                                       				  hh : mm [ offset ] ]

- ntp server ip-address

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

clock timezone zone hours-offset [ minutes-offset ]

#### Example:

```
Router(config)# clock timezone pst -8
```

Sets the local
                                             				time zone.

Step 4

clock summer-time zone recurring [ week day month hh : mm week day month
                                                				  hh : mm [ offset ] ]

#### Example:

```
Router(config)# clock summer-time pdt recurring
```

(Optional)
                                             				Specifies daylight savings time.

Default:
                                                   					 summer time is disabled. If the clock
                                                         						  summer-time zone recurring command is specified without
                                                   					 parameters, the summer time rules default to United States rules. Default of
                                                   					 the offset argument is 60.

Step 5

ntp server ip-address

#### Example:

```
Router(config)# ntp server 10.1.2.3
```

Synchronizes
                                             				software clock of router with the specified NTP server.

Step 6

exit

#### Example:

```
Router(config-telephony)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

If you are
                                       				configuring Cisco Unified CME for the first time on this router and if you have
                                       				a multisite installation, you are ready to configure a DTMF relay. See Configure DTMF Relay for H.323 Networks in Multisite Installations .

If
                                       				Cisco Unified CME will interact with a SIP Gateway, you must set up support for
                                       				the gateway. See Configure SIP Trunk Support .

If you are
                                       				configuring Cisco Unified CME for the first time on this router and you are
                                       				ready to configure system parameters. See System-Level Parameters .

If you are
                                       				finished modifying network parameters for an already configured
                                       				Cisco Unified CME router, see Configuration Files for Phones .

### Set Olson Timezone
                           	 for SCCP Phones

To set the Olson
                                 		  Timezone so that the correct local time is displayed on a Cisco Unified SCCP IP
                                 		  phone, perform the following steps.

#### Before you begin

TzDataCSV.csv
                                       				file is added to the configuration files of Cisco Unified 6921, 6941, 6945, and
                                       				6961 SCCP IP phones.

tzupdater.jar
                                       				file is added to the configuration files of Cisco Unified 7961 SCCP IP phones.

### SUMMARY STEPS

- enable

- configure terminal

- tftp-server device: tzupdater.jar

- tftp-server device: TZDataCSV.csv

- telephony-service

- olsontimezone timezone version number

- create cnf-files

- time-zone number

- exit

- clock
                                       				  timezone zone hours-offset

- clock
                                       				  summer-time zone date date month year hh:mm
                                       				  date month year hh:mm

- exit

- clock set hh:mm:ss day month
                                       				  year

- configure terminal

- telephony-service

- reset

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

tftp-server device: tzupdater.jar

#### Example:

```
Router(config)# tftp-server flash:tzupdater.jar
```

Enables access
                                             				to the tzupdater.jar file on the TFTP server.

device —TFTP server that is accessible to the Cisco
                                                   					 Unified CME, such as flash or slot 0.

Step 4

tftp-server device: TZDataCSV.csv

#### Example:

```
Router(config)# tftp-server flash:TZDataCSV.csv
```

Enables access
                                             				to the TZDataCSV.csv file on the TFTP server.

device —TFTP server that is accessible to the Cisco
                                                   					 Unified CME, such as flash or slot 0.

Step 5

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 6

olsontimezone timezone version number

#### Example:

```
Router(config-telephony)# olsontimezone America/Argentina/Buenos Aires version 2010o
```

Sets the Olson
                                             				Timezone so that the correct local time is displayed on Cisco Unified SCCP IP
                                             				phones or Cisco Unified SIP IP phones.

timezone —Olson Timezone names, which include the
                                                   					 area (name of continent or ocean) and location (name of a specific location
                                                   					 within that region, usually cities or small islands).

version number —Version of the tzupdater.jar or
                                                   					 TzDataCSV.csv file. The version indicates whether the file needs to be updated
                                                   					 or not.

In Cisco
                                                         				  Unified CME 9.0, the latest version is 2010o.

Step 7

create cnf-files

#### Example:

```
Router(config-telephony)# create cnf-files
```

Builds the
                                             				eXtensible Markup Language (XML) configuration files that are required for
                                             				Cisco Unified SCCP IP phones in Cisco Unified CME.

Step 8

time-zone number

#### Example:

```
Router(config-telephony)# time-zone 21
```

Sets the time
                                             				zone so that the correct local time is displayed on Cisco Unified SCCP IP
                                             				phones.

number —Numeric code for a named time zone.

Step 9

exit

#### Example:

```
Router(config-telephony)# exit
```

Exits
                                             				telephony-service configuration mode.

Step 10

clock
                                                				  timezone zone hours-offset

#### Example:

```
Router(config)# clock timezone CST -6
```

Sets the
                                             				time zone for display purposes.

zone —Name
                                                   					 of the time zone to be displayed when standard time is in effect. The length of
                                                   					 the zone argument is limited to 7 characters.

hours-offset —Hours difference from UTC.

Step 11

clock
                                                				  summer-time zone date date month year hh:mm
                                                				  date month year hh:mm

#### Example:

```
Router(config)# clock summer-time CST date 12 October 2010 2:00 26 April 2011 2:00
```

(Optional)
                                             				Configures the Cisco Unified CME system to automatically switch to summer time
                                             				(daylight saving time).

zone —Name
                                                   					 of the time zone (for example, “PDT” for Pacific Daylight Time) to be displayed
                                                   					 when summer time is in effect. The length of the zone argument is limited to 7
                                                   					 characters.

date —Indicates that summer time should start on
                                                   					 the first specific date listed in the command and end on the second specific
                                                   					 date in the command.

date —Date
                                                   					 of the month (1 to 31).

month —Month
                                                   					 (January, February, and so on).

year —Year
                                                   					 (1993 to 2035).

hh:mm —Time
                                                   					 (24-hour format) in hours and minutes.

Step 12

exit

#### Example:

```
Router(config)# exit
```

Exits global
                                             				configuration mode.

Step 13

clock set hh:mm:ss day month
                                                				  year

#### Example:

```
Router# clock set 19:29:00 13 May 2011
```

Manually
                                             				sets the system software clock.

hh:mm:ss —Current time in hours (24-hour format),
                                                   					 minutes, and seconds.

day —Current
                                                   					 day (by date) in the month.

month —Current month (by name).

year —Current year (no abbreviation).

Step 14

configure terminal

#### Example:

```
Router# configure terminal
```

Enters
                                             				global configuration mode.

Step 15

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 16

reset

#### Example:

```
Router(config-telephony)# reset
```

Performs a
                                             				complete reboot of Cisco Unfiied SCCP IP phones associated with a Cisco Unified
                                             				CME router.

Step 17

end

#### Example:

```
Router(config-telephony)# end
```

Exits to
                                             				privileged EXEC mode.

### Set Olson Timezone
                           	 for SIP Phones

To set the Olson
                                 		  Timezone so that the correct local time is displayed on a Cisco Unified SIP IP
                                 		  phone, perform the following steps.

#### Before you begin

TzDataCSV.csv
                                       				file is added to the configuration files of Cisco Unified 3911, 3951, 6921,
                                       				6941, 6945, and 6961 SIP IP phones.

tzupdater.jar
                                       				file is added to the configuration files of Cisco Unified 7961 SIP IP phones.

### SUMMARY STEPS

- enable

- configure terminal

- tftp-server device : tzupdater.jar

- tftp-server device : TZDataCSV.csv

- voice register global

- olsontimezone timezone version number

- create profile

- timezone number

- exit

- clock
                                       				  timezone zone hours-offset

- clock
                                       				  summer-time zone date date month year hh:mm
                                       				  date month year hh:mm

- exit

- clock set hh:mm:ss day month
                                       				  year

- configure terminal

- voice register
                                       				  global

- reset

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

tftp-server device : tzupdater.jar

#### Example:

```
Router(config)# tftp-server slot0:tzupdater.jar
```

Enables access
                                             				to the tzupdater.jar file on the TFTP server.

device —TFTP server that is accessible to the Cisco
                                                   					 Unified CME, such as flash or slot 0.

Step 4

tftp-server device : TZDataCSV.csv

#### Example:

```
Router(config)# tftp-server slot0:TZDataCSV.csv
```

Enables access
                                             				to the TZDataCSV.csv file on the TFTP server.

device —TFTP server that is accessible to the Cisco
                                                   					 Unified CME, such as flash or slot 0.

Step 5

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode.

Step 6

olsontimezone timezone version number

#### Example:

```
Router(config-register-global)# olsontimezone America/Argentina/Buenos Aires version 2010o
```

Sets the Olson
                                             				Timezone so that the correct local time is displayed on Cisco Unified SCCP IP
                                             				phones or Cisco Unified SIP IP phones.

timezone —Olson Timezone names, which include the
                                                   					 area (name of continent or ocean) and location (name of a specific location
                                                   					 within that region, usually cities or small islands).

version number —Version of the tzupdater.jar or
                                                   					 tzdatacsv.csv file. The version indicates whether the file needs to be updated
                                                   					 or not.

In Cisco
                                                         				  Unified CME 9.0, the latest version is 2010o.

Step 7

create profile

#### Example:

```
Router(config-register-global)# create profile
```

Generates the
                                             				configuration profile files required for Cisco Unified SIP IP phones.

Step 8

timezone number

#### Example:

```
Router(config-register-global)# timezone 21
```

Sets the time
                                             				zone used for Cisco Unified SIP IP phones.

number —Range is 1 to 53. Default is 5, Pacific
                                                   					 Standard/Daylight Time.

Step 9

exit

#### Example:

```
Router(config-register-global)# exit
```

Exits voice
                                             				register global configuration mode.

Step 10

clock
                                                				  timezone zone hours-offset

#### Example:

```
Router(config)# clock timezone CST -6
```

Sets the
                                             				time zone for display purposes.

zone —Name
                                                   					 of the time zone to be displayed when standard time is in effect. The length of
                                                   					 the zone argument is limited to 7 characters.

hours-offset —Hours difference from UTC.

Step 11

clock
                                                				  summer-time zone date date month year hh:mm
                                                				  date month year hh:mm

#### Example:

```
Router(config)# clock summer-time CST date 12 October 2010 2:00 26 April 2011 2:00
```

(Optional)
                                             				Configures the Cisco Unified CME system to automatically switch to summer time
                                             				(daylight saving time).

zone —Name
                                                   					 of the time zone (for example, “PDT” for Pacific Daylight Time) to be displayed
                                                   					 when summer time is in effect. The length of the zone argument is limited to 7
                                                   					 characters.

date —Indicates that summer time should start on
                                                   					 the first specific date listed in the command and end on the second specific
                                                   					 date in the command.

date —Date
                                                   					 of the month (1 to 31).

month —Month
                                                   					 (January, February, and so on).

year —Year
                                                   					 (1993 to 2035).

hh:mm —Time
                                                   					 (24-hour format) in hours and minutes.

Step 12

exit

#### Example:

```
Router(config)# exit
```

Exits global
                                             				configuration mode.

Step 13

clock set hh:mm:ss day month
                                                				  year

#### Example:

```
Router# clock set 15:25:00 17 November 2011
```

Manually
                                             				sets the system software clock.

hh:mm:ss —Current time in hours (24-hour format),
                                                   					 minutes, and seconds.

day —Current
                                                   					 day (by date) in the month.

month —Current month (by name).

year —Current year (no abbreviation).

Step 14

configure terminal

#### Example:

```
Router# configure terminal
```

Enters
                                             				global configuration mode.

Step 15

voice register
                                                				  global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode.

Step 16

reset

#### Example:

```
Router(config-register-global)# reset
```

Performs a
                                             				complete reboot of Cisco Unified SIP phones associated with a Cisco Unified CME
                                             				router.

Step 17

end

#### Example:

```
Router(config-register-global)# end
```

Exits to
                                             				privileged EXEC mode.

### Configure DTMF
                           	 Relay for H.323 Networks in Multisite Installations

To configure DTMF
                                 		  relay for H.323 networks in a multisite installation only, perform the
                                 		  following steps.

To configure
                                             			 DTMF relay on SIP networks, see Configure SIP Trunk Support .

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- dtmf-relay h245-alphanumeric

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

dial-peer voice tag voip

#### Example:

```
Router(config)# dial-peer voice 2 voip
```

Enters
                                             				dial-peer configuration mode.

Step 4

dtmf-relay h245-alphanumeric

#### Example:

```
Router(config-dial-peer)# dtmf-relay h245-alphanumeric
```

Specifies the
                                             				H.245 alphanumeric method for relaying dual tone multifrequency (DTMF) tones
                                             				between telephony interfaces and an H.323 network.

Step 5

end

#### Example:

```
Router(config-dial-peer)# end
```

Returns to
                                             				privileged EXEC mode.

#### What to do next

To set up
                                       				support for a SIP trunk, see Configure SIP Trunk Support .

If you are
                                       				configuring Cisco Unified CME for the first time on this router and you are
                                       				ready to configure system parameters. For more information, see System-Level Parameters .

If you are
                                       				finished modifying network parameters for an already configured
                                       				Cisco Unified CME router, see Configuration Files for Phones .

### Configure SIP
                           	 Trunk Support

To enable DTMF
                                 		  relay on a dial-peer for a SIP gateway and set up the gateway to register phone
                                 		  numbers with Cisco Unified CME, perform the following steps.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice tag voip

- dtmf-relay rtp-nte

- dtmf-relay sip-notify

- exit

- sip-ua

- notify telephone-event max-duration msec

- registrar { dns: host-name | ipv4: ip-address } expires seconds [ tcp ] [ secondary ]

- retry register number

- timers
                                       				  register msec

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

dial-peer voice tag voip

#### Example:

```
Router(config)# dial-peer voice 2 voip
```

Enters
                                             				dial-peer configuration mode.

Step 4

dtmf-relay rtp-nte

#### Example:

```
Router(config-dial-peer)# dtmf-relay rtp-nte
```

Forwards DTMF
                                             				tones by using Real-Time Transport Protocol (RTP) with the Named Telephone
                                             				Event (NTE) payload type and enables DTMF relay using the RFC 2833 standard
                                             				method.

Step 5

dtmf-relay sip-notify

#### Example:

```
Router(config-dial-peer)# dtmf-relay sip-notify
```

Forwards DTMF
                                             				tones using SIP NOTIFY messages.

Step 6

exit

#### Example:

```
Router(config-dial-peer)# exit
```

Exits
                                             				dial-peer configuration mode.

Step 7

sip-ua

#### Example:

```
Router(config)# sip-ua
```

Enters SIP
                                             				user-agent configuration mode.

Step 8

notify telephone-event max-duration msec

#### Example:

```
Router(config-sip-ua)# notify telephone-event max-duration 2000
```

Sets the
                                             				maximum milliseconds allowed between two consecutive NOTIFY messages for a
                                             				single DTMF event.

max-duration time —Range:
                                                   					 500 to 3000. Default: 2000.

Step 9

registrar { dns: host-name | ipv4: ip-address } expires seconds [ tcp ] [ secondary ]

#### Example:

```
Router(config-sip-ua)# registrar ipv4:10.8.17.40 expires 3600 secondary
```

Registers
                                             				E.164 numbers on behalf of analog telephone voice ports (FXS) and IP phone
                                             				virtual voice ports (EFXS) with an external SIP proxy or SIP registrar server.

Step 10

retry register number

#### Example:

```
Router(config-sip-ua)# retry register 10
```

Sets the
                                             				total number of SIP Register messages that the gateway should send.

number —Number of Register message retries.
                                                   					 Range: 1 to 10. Default: 10.

Step 11

timers
                                                				  register msec

#### Example:

```
Router(config-sip-ua)# timers register 500
```

Sets how
                                             				long the SIP user agent (UA) waits before sending Register requests.

time —Waiting time, in milliseconds.
                                                   					 Range: 100 to 1000. Default: 500.

Step 12

end

#### Example:

```
Router(config-sip-ua)# end
```

Returns to
                                             				privileged EXEC mode.

### Verify SIP Trunk Support Configuration

To verify SIP trunk configuration, perform the following steps in any order.

Step 1

show sip-ua status

Use this command to display the time interval between consecutive NOTIFY messages for a telephone event. In the following
                                             example, the time interval is 2000 ms:

#### Example:

```
Router# show sip-ua status
```

```
SIP User Agent Status
```

```
SIP User Agent for UDP :ENABLED
```

```
SIP User Agent for TCP :ENABLED
```

```
SIP User Agent bind status(signaling):DISABLED
```

```
SIP User Agent bind status(media):DISABLED
```

```
SIP early-media for 180 responses with SDP:ENABLED
```

```
SIP max-forwards :6
```

```
SIP DNS SRV version:2 (rfc 2782)
```

```
NAT Settings for the SIP-UA
```

```
Role in SDP:NONE
```

```
Check media source packets:DISABLED
```

```
Maximum duration for a telephone-event in NOTIFYs:2000 ms
```

```
SIP support for ISDN SUSPEND/RESUME:ENABLED
```

```
Redirection (3xx) message handling:ENABLED
```

```
SDP application configuration:
```

```
Version line (v=) required
```

```
Owner line (o=) required
```

```
Timespec line (t=) required
```

```
Media supported:audio image
```

```
Network types supported:IN
```

```
Address types supported:IP4
```

```
Transport types supported:RTP/AVP udptl
```

Step 2

show sip-ua timers

This command displays the waiting time before Register requests are sent; that is, the value that has been set with the timers register command.

Step 3

show sip-ua register status

This command displays the status of local E.164 registrations.

Step 4

show sip-ua statistics

This command displays the Register messages that have been sent.

### Change the TFTP Address on a DHCP Server

To change the TFTP IP address after it has already been configured,
                                 		  perform the following steps.

Restriction

If the DHCP server is on a different router than Cisco Unified CME,
                                             			 reconfigure the external DHCP server with the new IP address of the TFTP
                                             			 server.

#### Before you begin

Your Cisco Unified CME router is a DHCP server.

### SUMMARY STEPS

- enable

- configure terminal

- ip dhcp pool pool-name

- option 150 ip ip-address

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Router> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

ip dhcp pool pool-name

#### Example:

```
Router(config)# ip dhcp pool pool2
```

Enters DHCP pool configuration mode to create or modify a DHCP
                                             				pool.

pool-name —Previously configured
                                                   					 unique identifier for the pool to be configured.

Step 4

option 150 ip ip-address

#### Example:

```
Router(config-dhcp)# option 150 ip 10.0.0.1
```

Specifies the TFTP server IP address from which the
                                             				Cisco Unified IP phone downloads the image configuration file,
                                             				XmlDefault.cnf.xml.

Step 5

end

#### Example:

```
Router(config-dhcp)# end
```

Returns to privileged EXEC mode.

## Configuration Examples for Network Parameters

### NTP Server

The following example defines the pst timezone as 8 hours offset from
                                 		  UTC, using a recurring daylight savings time called pdt, and synchronizes the
                                 		  clock with the NTP server at 10.1.2.3:

```
clock timezone pst -8
```

```
clock summer-time pdt recurring
```

```
ntp server 10.1.2.3
```

### DTMF Relay for H.323 Networks

The following excerpt from the show running-config command output shows a
                                 		  dial peer configured to use H.245 alphanumeric DTMF relay:

```
dial-peer voice 4000 voip
```

```
destination-pattern 4000
```

```
session target ipv4:10.0.0.25
```

```
codec g711ulaw
```

```
dtmf-relay h245-alphanumeric
```

## Where to Go Next

If you are configuring Cisco Unified CME for the first time on this router, you are ready to configure system-level parameters.
                                 See System-Level Parameters .

If you modified network parameters for an already configured Cisco Unified CME router, you are ready to generate the configuration
                                 file to save the modifications. See Configuration Files for Phones .

## Feature
                        	 Information for Network Parameters

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature
                                          					 Name

Cisco Unified CME Version

Modification

Olson
                                          					 Timezone

9.0

Eliminates
                                          					 the need to update time zone commands or phone loads to accommodate a new
                                          					 country with a new time zone or an existing country whose city or state wants
                                          					 to change their time zone, using the olsontimezone command in either telephony-service or voice register global configuration
                                          					 mode.

| Note | No commands allow registration between the H.323 and SIP protocols. |
|---|---|

| Note | When you configure SIP on a router, the ports on all its interfaces are open by default. This makes the router vulnerable
                                       to malicious attackers who can execute toll fraud across the gateway if the router has a public IP address and a public switched
                                       telephone network (PSTN) connection. To eliminate the threat, you should bind an interface to private IP address that is not
                                       accessible by untrusted hosts. In addition, you should protect any public or untrusted interface by configuring a firewall
                                       or an access control list (ACL) to prevent unwanted traffic from traversing the router. |
|---|---|

| Restriction | SIP
                                                   				  endpoints are not supported on H.323 trunks. SIP endpoints are supported on SIP
                                                   				  trunks only. Cisco Unified CME 3.4 and later versions support Media
                                                   				  Flow-through mode only; enabling SIP-to-SIP calls is required before you can
                                                   				  successfully make SIP-to-SIP calls. Media
                                                   				  Flow-around configured with the media
                                                         						flow-around command is not supported by Cisco Unified CME with
                                                   				  SIP phones. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice
                                             				service configuration mode and specifies Voice over IP (VoIP) encapsulation. |
| Step 4 | allow-connections from - type to to - type Example: Router(config-voi-srv)# allow-connections h323 to h323 Router(config-voi-srv)# allow-connections h323 to SIP Router(config-voi-srv)# allow-connections SIP to SIP | Enables calls
                                             				between specific types of endpoints in a VoIP network. A separate
                                                   					 allow-connections command is required for each type of endpoint to be
                                                   					 supported. |
| Step 5 | sip Example: Router(config-voi-srv)# sip | (Optional)
                                             				Enters SIP configuration mode. Required
                                                   					 if you are connecting IP phones running SIP directly in Cisco CME 3.4 and
                                                   					 later. |
| Step 6 | registrar server [ expires [ max sec ] [ min sec ] ] Example: Router(config-voi-sip)# registrar server expires max 600 min 60 | (Optional)
                                             				Enables SIP registrar functionality in Cisco Unified CME. Required
                                                   					 if you are connecting IP phones running SIP directly in Cisco CME 3.4 and
                                                   					 later. Note Cisco Unified CME does not maintain a persistent database of
                                                         				  registration entries across reloads. Because SIP phones do not use a keepalive
                                                         				  functionality, the SIP phones must register again. To decrease the amount of
                                                         				  time after which the SIP phones register again, we recommend that you change
                                                         				  the expiry. max sec —(Optional) Range: 600 to 86400. Default: 3600.
                                                   					 Recommended value: 600. Note Ensure that
                                                         				  the registration expiration timeout is set to a value smaller than the TCP
                                                         				  connection aging timeout to avoid disconnection from the TCP. min sec —(Optional) Range: 60 to 3600. Default: 60. | Note | Cisco Unified CME does not maintain a persistent database of
                                                         				  registration entries across reloads. Because SIP phones do not use a keepalive
                                                         				  functionality, the SIP phones must register again. To decrease the amount of
                                                         				  time after which the SIP phones register again, we recommend that you change
                                                         				  the expiry. | Note | Ensure that
                                                         				  the registration expiration timeout is set to a value smaller than the TCP
                                                         				  connection aging timeout to avoid disconnection from the TCP. |
| Note | Cisco Unified CME does not maintain a persistent database of
                                                         				  registration entries across reloads. Because SIP phones do not use a keepalive
                                                         				  functionality, the SIP phones must register again. To decrease the amount of
                                                         				  time after which the SIP phones register again, we recommend that you change
                                                         				  the expiry. |
| Note | Ensure that
                                                         				  the registration expiration timeout is set to a value smaller than the TCP
                                                         				  connection aging timeout to avoid disconnection from the TCP. |
| Step 7 | exit Example: Router(config-voi-sip)# exit | Exits
                                             				dial-peer configuration mode. |
| Step 8 | sip-ua Example: Router(config)# sip-ua | Enters SIP
                                             				user-agent configuration mode. |
| Step 9 | notify telephone-event
                                                				  max-duration time Example: Router(config-sip-ua)# notify telephone-event max-duration 2000 | Configures
                                             				the maximum time interval allowed between two consecutive NOTIFY messages for a
                                             				single DTMF event. max-duration time —Range: 500 to 3000. Default: 2000. |
| Step 10 | registrar { dns: host-name \| ipv4: ip-address } expires seconds [ tcp ] [ secondary ] Example: Router(config-sip-ua)# registrar ipv4:10.8.17.40 expires 3600 secondary | Registers
                                             				E.164 numbers on behalf of analog telephone voice ports (FXS) and IP phone
                                             				virtual voice ports (EFXS) with an external SIP proxy or SIP registrar server. |
| Step 11 | retry
                                                				  register number Example: Router(config-sip-ua)# retry register 10 | Sets the
                                             				total number of SIP Register messages that the gateway should send. number —Number of Register message retries.
                                                   					 Range: 1 to 10. Default: 10. |
| Step 12 | timers
                                                				  register time Example: Router(config-sip-ua)# timers register 500 | Sets how
                                             				long the SIP user agent (UA) waits before sending Register requests. time —Waiting time, in milliseconds.
                                                   					 Range: 100 to 1000. Default: 500. |
| Step 13 | end Example: Router(config-sip-ua)# end | Exits
                                             				configuration mode and enters privileged EXEC mode. |

| Note | Cisco Unified CME does not maintain a persistent database of
                                                         				  registration entries across reloads. Because SIP phones do not use a keepalive
                                                         				  functionality, the SIP phones must register again. To decrease the amount of
                                                         				  time after which the SIP phones register again, we recommend that you change
                                                         				  the expiry. |
|---|---|

| Note | Ensure that
                                                         				  the registration expiration timeout is set to a value smaller than the TCP
                                                         				  connection aging timeout to avoid disconnection from the TCP. |
|---|---|

| Note | Do not perform this task if you already have a DHCP server on the LAN that can be used
                                                			 to provide addresses to the Cisco Unified CME phones. See Enable Network Time Protocol . |
|---|---|

| Restriction | A single DHCP IP
                                                			 address pool cannot be used if non-IP-phone clients, such as PCs, must use a
                                                			 different TFTP server address. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | ip dhcp pool pool-name Example: Router(config)# ip dhcp pool mypool | Creates a name
                                                				for the DHCP server address pool and enters DHCP pool configuration mode. |
| Step 4 | network ip-address [ mask \| / prefix-length ] Example: Router(config-dhcp)# network 10.0.0.0 255.255.0.0 | Specifies the
                                                				IP address of the DHCP address pool to be configured. |
| Step 5 | option 150 ip ip-address Example: Router(config-dhcp)# option 150 ip 10.0.0.1 | Specifies the
                                                				TFTP server address from which the Cisco Unified IP phone downloads the image
                                                				configuration file. This is
                                                      					 your Cisco Unified CME router’s address. |
| Step 6 | default-router ip-address Example: Router(config-dhcp)# default-router 10.0.0.1 | (Optional)
                                                				Specifies the router that the IP phones will use to send or receive IP traffic
                                                				that is external to their local subnet. If the
                                                      					 Cisco Unified CME router is the only router on the network, this address should
                                                      					 be the Cisco Unified CME IP source address. This command can be omitted if IP
                                                      					 phones need to send or receive IP traffic only to or from devices on their
                                                      					 local subnet. The IP
                                                      					 address that you specify for default router will be used by the IP phones for
                                                      					 fallback purposes. If the Cisco Unified CME IP source address becomes
                                                      					 unreachable, IP phones will attempt to register to the address specified in
                                                      					 this command. |
| Step 7 | end Example: Router(config-dhcp)# end | Returns to
                                                				privileged EXEC mode. |

| Note | Do not perform this task if you already have a DHCP server on the LAN that can be used
                                                			 to provide addresses to the Cisco Unified CME phones. See Enable Network Time Protocol . |
|---|---|

| Restriction | To use a
                                                			 separate DHCP IP address pool for each DHCP client, make an entry for each IP
                                                			 phone. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | ip dhcp pool pool-name Example: Router(config)# ip dhcp pool pool2 | Creates a name
                                                				for the DHCP server address pool and enters DHCP pool configuration mode. |
| Step 4 | host ip-address
                                                   				  subnet-mask Example: Router(config-dhcp)# host 10.0.0.0 255.255.0.0 | Specifies the
                                                				IP address that you want the phone to get. |
| Step 5 | client-identifier mac-address Example: Router(config-dhcp)# client-identifier 01238.380.3056 | Specifies the
                                                				MAC address of the phone, which is printed on a label on each
                                                				Cisco Unified IP phone. A separate
                                                      					 client-identifier command is required for each DHCP client. Add “01”
                                                      					 prefix number before the MAC address. |
| Step 6 | option 150 ip ip-address Example: Router(config-dhcp)# option 150 ip 10.0.0.1 | Specifies the
                                                				TFTP server address from which the Cisco Unified IP phone downloads the image
                                                				configuration file. This is
                                                      					 your Cisco Unified CME router’s address. |
| Step 7 | default-router ip-address Example: Router(config-dhcp)# default-router 10.0.0.1 | (Optional)
                                                				Specifies the router that the IP phones will use to send or receive IP traffic
                                                				that is external to their local subnet. If the
                                                      					 Cisco Unified CME router is the only router on the network, this address should
                                                      					 be the Cisco Unified CME IP source address. This command can be omitted if IP
                                                      					 phones need to send or receive IP traffic only to or from devices on their
                                                      					 local subnet. The IP
                                                      					 address that you specify for default router will be used by the IP phones for
                                                      					 fallback purposes. If the Cisco Unified CME IP source address becomes
                                                      					 unreachable, IP phones will attempt to register to the address specified in
                                                      					 this command. |
| Step 8 | end Example: Router(config-dhcp)# end | Returns to
                                                				privileged EXEC mode. |

| Restriction | The
                                                			 Cisco Unified CME router cannot be the DHCP server. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                                				privileged EXEC mode. Enter your
                                                      					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                                				configuration mode. |
| Step 3 | service dhcp Example: Router(config)# service dhcp | Enables the
                                                				Cisco IOS DHCP server feature on the router. |
| Step 4 | interface type number Example: Router(config)# interface vlan 10 | Enters
                                                				interface configuration mode for the specified interface. |
| Step 5 | ip helper-address ip -address Example: Router(config-if)# ip helper-address 10.0.0.1 | Specifies the
                                                				helper address for any unrecognized broadcast for TFTP server and DNS server
                                                				requests. A separate ip
                                                            						  helper-address command is required for each server if the servers
                                                      					 are on different hosts. You can
                                                      					 also configure multiple TFTP server targets by using the ip
                                                            						  helper-address commands for multiple servers. |
| Step 6 | end Example: Router(config-if)# end | Returns to
                                                				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | clock timezone zone hours-offset [ minutes-offset ] Example: Router(config)# clock timezone pst -8 | Sets the local
                                             				time zone. |
| Step 4 | clock summer-time zone recurring [ week day month hh : mm week day month
                                                				  hh : mm [ offset ] ] Example: Router(config)# clock summer-time pdt recurring | (Optional)
                                             				Specifies daylight savings time. Default:
                                                   					 summer time is disabled. If the clock
                                                         						  summer-time zone recurring command is specified without
                                                   					 parameters, the summer time rules default to United States rules. Default of
                                                   					 the offset argument is 60. |
| Step 5 | ntp server ip-address Example: Router(config)# ntp server 10.1.2.3 | Synchronizes
                                             				software clock of router with the specified NTP server. |
| Step 6 | exit Example: Router(config-telephony)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | tftp-server device: tzupdater.jar Example: Router(config)# tftp-server flash:tzupdater.jar | Enables access
                                             				to the tzupdater.jar file on the TFTP server. device —TFTP server that is accessible to the Cisco
                                                   					 Unified CME, such as flash or slot 0. |
| Step 4 | tftp-server device: TZDataCSV.csv Example: Router(config)# tftp-server flash:TZDataCSV.csv | Enables access
                                             				to the TZDataCSV.csv file on the TFTP server. device —TFTP server that is accessible to the Cisco
                                                   					 Unified CME, such as flash or slot 0. |
| Step 5 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 6 | olsontimezone timezone version number Example: Router(config-telephony)# olsontimezone America/Argentina/Buenos Aires version 2010o | Sets the Olson
                                             				Timezone so that the correct local time is displayed on Cisco Unified SCCP IP
                                             				phones or Cisco Unified SIP IP phones. timezone —Olson Timezone names, which include the
                                                   					 area (name of continent or ocean) and location (name of a specific location
                                                   					 within that region, usually cities or small islands). version number —Version of the tzupdater.jar or
                                                   					 TzDataCSV.csv file. The version indicates whether the file needs to be updated
                                                   					 or not. Note In Cisco
                                                         				  Unified CME 9.0, the latest version is 2010o. | Note | In Cisco
                                                         				  Unified CME 9.0, the latest version is 2010o. |
| Note | In Cisco
                                                         				  Unified CME 9.0, the latest version is 2010o. |
| Step 7 | create cnf-files Example: Router(config-telephony)# create cnf-files | Builds the
                                             				eXtensible Markup Language (XML) configuration files that are required for
                                             				Cisco Unified SCCP IP phones in Cisco Unified CME. |
| Step 8 | time-zone number Example: Router(config-telephony)# time-zone 21 | Sets the time
                                             				zone so that the correct local time is displayed on Cisco Unified SCCP IP
                                             				phones. number —Numeric code for a named time zone. |
| Step 9 | exit Example: Router(config-telephony)# exit | Exits
                                             				telephony-service configuration mode. |
| Step 10 | clock
                                                				  timezone zone hours-offset Example: Router(config)# clock timezone CST -6 | Sets the
                                             				time zone for display purposes. zone —Name
                                                   					 of the time zone to be displayed when standard time is in effect. The length of
                                                   					 the zone argument is limited to 7 characters. hours-offset —Hours difference from UTC. |
| Step 11 | clock
                                                				  summer-time zone date date month year hh:mm
                                                				  date month year hh:mm Example: Router(config)# clock summer-time CST date 12 October 2010 2:00 26 April 2011 2:00 | (Optional)
                                             				Configures the Cisco Unified CME system to automatically switch to summer time
                                             				(daylight saving time). zone —Name
                                                   					 of the time zone (for example, “PDT” for Pacific Daylight Time) to be displayed
                                                   					 when summer time is in effect. The length of the zone argument is limited to 7
                                                   					 characters. date —Indicates that summer time should start on
                                                   					 the first specific date listed in the command and end on the second specific
                                                   					 date in the command. date —Date
                                                   					 of the month (1 to 31). month —Month
                                                   					 (January, February, and so on). year —Year
                                                   					 (1993 to 2035). hh:mm —Time
                                                   					 (24-hour format) in hours and minutes. |
| Step 12 | exit Example: Router(config)# exit | Exits global
                                             				configuration mode. |
| Step 13 | clock set hh:mm:ss day month
                                                				  year Example: Router# clock set 19:29:00 13 May 2011 | Manually
                                             				sets the system software clock. hh:mm:ss —Current time in hours (24-hour format),
                                                   					 minutes, and seconds. day —Current
                                                   					 day (by date) in the month. month —Current month (by name). year —Current year (no abbreviation). |
| Step 14 | configure terminal Example: Router# configure terminal | Enters
                                             				global configuration mode. |
| Step 15 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 16 | reset Example: Router(config-telephony)# reset | Performs a
                                             				complete reboot of Cisco Unfiied SCCP IP phones associated with a Cisco Unified
                                             				CME router. |
| Step 17 | end Example: Router(config-telephony)# end | Exits to
                                             				privileged EXEC mode. |

| Note | In Cisco
                                                         				  Unified CME 9.0, the latest version is 2010o. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | tftp-server device : tzupdater.jar Example: Router(config)# tftp-server slot0:tzupdater.jar | Enables access
                                             				to the tzupdater.jar file on the TFTP server. device —TFTP server that is accessible to the Cisco
                                                   					 Unified CME, such as flash or slot 0. |
| Step 4 | tftp-server device : TZDataCSV.csv Example: Router(config)# tftp-server slot0:TZDataCSV.csv | Enables access
                                             				to the TZDataCSV.csv file on the TFTP server. device —TFTP server that is accessible to the Cisco
                                                   					 Unified CME, such as flash or slot 0. |
| Step 5 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode. |
| Step 6 | olsontimezone timezone version number Example: Router(config-register-global)# olsontimezone America/Argentina/Buenos Aires version 2010o | Sets the Olson
                                             				Timezone so that the correct local time is displayed on Cisco Unified SCCP IP
                                             				phones or Cisco Unified SIP IP phones. timezone —Olson Timezone names, which include the
                                                   					 area (name of continent or ocean) and location (name of a specific location
                                                   					 within that region, usually cities or small islands). version number —Version of the tzupdater.jar or
                                                   					 tzdatacsv.csv file. The version indicates whether the file needs to be updated
                                                   					 or not. Note In Cisco
                                                         				  Unified CME 9.0, the latest version is 2010o. | Note | In Cisco
                                                         				  Unified CME 9.0, the latest version is 2010o. |
| Note | In Cisco
                                                         				  Unified CME 9.0, the latest version is 2010o. |
| Step 7 | create profile Example: Router(config-register-global)# create profile | Generates the
                                             				configuration profile files required for Cisco Unified SIP IP phones. |
| Step 8 | timezone number Example: Router(config-register-global)# timezone 21 | Sets the time
                                             				zone used for Cisco Unified SIP IP phones. number —Range is 1 to 53. Default is 5, Pacific
                                                   					 Standard/Daylight Time. |
| Step 9 | exit Example: Router(config-register-global)# exit | Exits voice
                                             				register global configuration mode. |
| Step 10 | clock
                                                				  timezone zone hours-offset Example: Router(config)# clock timezone CST -6 | Sets the
                                             				time zone for display purposes. zone —Name
                                                   					 of the time zone to be displayed when standard time is in effect. The length of
                                                   					 the zone argument is limited to 7 characters. hours-offset —Hours difference from UTC. |
| Step 11 | clock
                                                				  summer-time zone date date month year hh:mm
                                                				  date month year hh:mm Example: Router(config)# clock summer-time CST date 12 October 2010 2:00 26 April 2011 2:00 | (Optional)
                                             				Configures the Cisco Unified CME system to automatically switch to summer time
                                             				(daylight saving time). zone —Name
                                                   					 of the time zone (for example, “PDT” for Pacific Daylight Time) to be displayed
                                                   					 when summer time is in effect. The length of the zone argument is limited to 7
                                                   					 characters. date —Indicates that summer time should start on
                                                   					 the first specific date listed in the command and end on the second specific
                                                   					 date in the command. date —Date
                                                   					 of the month (1 to 31). month —Month
                                                   					 (January, February, and so on). year —Year
                                                   					 (1993 to 2035). hh:mm —Time
                                                   					 (24-hour format) in hours and minutes. |
| Step 12 | exit Example: Router(config)# exit | Exits global
                                             				configuration mode. |
| Step 13 | clock set hh:mm:ss day month
                                                				  year Example: Router# clock set 15:25:00 17 November 2011 | Manually
                                             				sets the system software clock. hh:mm:ss —Current time in hours (24-hour format),
                                                   					 minutes, and seconds. day —Current
                                                   					 day (by date) in the month. month —Current month (by name). year —Current year (no abbreviation). |
| Step 14 | configure terminal Example: Router# configure terminal | Enters
                                             				global configuration mode. |
| Step 15 | voice register
                                                				  global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode. |
| Step 16 | reset Example: Router(config-register-global)# reset | Performs a
                                             				complete reboot of Cisco Unified SIP phones associated with a Cisco Unified CME
                                             				router. |
| Step 17 | end Example: Router(config-register-global)# end | Exits to
                                             				privileged EXEC mode. |

| Note | In Cisco
                                                         				  Unified CME 9.0, the latest version is 2010o. |
|---|---|

| Note | To configure
                                             			 DTMF relay on SIP networks, see Configure SIP Trunk Support . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 2 voip | Enters
                                             				dial-peer configuration mode. |
| Step 4 | dtmf-relay h245-alphanumeric Example: Router(config-dial-peer)# dtmf-relay h245-alphanumeric | Specifies the
                                             				H.245 alphanumeric method for relaying dual tone multifrequency (DTMF) tones
                                             				between telephony interfaces and an H.323 network. |
| Step 5 | end Example: Router(config-dial-peer)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 2 voip | Enters
                                             				dial-peer configuration mode. |
| Step 4 | dtmf-relay rtp-nte Example: Router(config-dial-peer)# dtmf-relay rtp-nte | Forwards DTMF
                                             				tones by using Real-Time Transport Protocol (RTP) with the Named Telephone
                                             				Event (NTE) payload type and enables DTMF relay using the RFC 2833 standard
                                             				method. |
| Step 5 | dtmf-relay sip-notify Example: Router(config-dial-peer)# dtmf-relay sip-notify | Forwards DTMF
                                             				tones using SIP NOTIFY messages. |
| Step 6 | exit Example: Router(config-dial-peer)# exit | Exits
                                             				dial-peer configuration mode. |
| Step 7 | sip-ua Example: Router(config)# sip-ua | Enters SIP
                                             				user-agent configuration mode. |
| Step 8 | notify telephone-event max-duration msec Example: Router(config-sip-ua)# notify telephone-event max-duration 2000 | Sets the
                                             				maximum milliseconds allowed between two consecutive NOTIFY messages for a
                                             				single DTMF event. max-duration time —Range:
                                                   					 500 to 3000. Default: 2000. |
| Step 9 | registrar { dns: host-name \| ipv4: ip-address } expires seconds [ tcp ] [ secondary ] Example: Router(config-sip-ua)# registrar ipv4:10.8.17.40 expires 3600 secondary | Registers
                                             				E.164 numbers on behalf of analog telephone voice ports (FXS) and IP phone
                                             				virtual voice ports (EFXS) with an external SIP proxy or SIP registrar server. |
| Step 10 | retry register number Example: Router(config-sip-ua)# retry register 10 | Sets the
                                             				total number of SIP Register messages that the gateway should send. number —Number of Register message retries.
                                                   					 Range: 1 to 10. Default: 10. |
| Step 11 | timers
                                                				  register msec Example: Router(config-sip-ua)# timers register 500 | Sets how
                                             				long the SIP user agent (UA) waits before sending Register requests. time —Waiting time, in milliseconds.
                                                   					 Range: 100 to 1000. Default: 500. |
| Step 12 | end Example: Router(config-sip-ua)# end | Returns to
                                             				privileged EXEC mode. |

| Step 1 | show sip-ua status Use this command to display the time interval between consecutive NOTIFY messages for a telephone event. In the following
                                             example, the time interval is 2000 ms: Example: Router# show sip-ua status SIP User Agent Status SIP User Agent for UDP :ENABLED SIP User Agent for TCP :ENABLED SIP User Agent bind status(signaling):DISABLED SIP User Agent bind status(media):DISABLED SIP early-media for 180 responses with SDP:ENABLED SIP max-forwards :6 SIP DNS SRV version:2 (rfc 2782) NAT Settings for the SIP-UA Role in SDP:NONE Check media source packets:DISABLED Maximum duration for a telephone-event in NOTIFYs:2000 ms SIP support for ISDN SUSPEND/RESUME:ENABLED Redirection (3xx) message handling:ENABLED SDP application configuration: Version line (v=) required Owner line (o=) required Timespec line (t=) required Media supported:audio image Network types supported:IN Address types supported:IP4 Transport types supported:RTP/AVP udptl |
|---|---|
| Step 2 | show sip-ua timers This command displays the waiting time before Register requests are sent; that is, the value that has been set with the timers register command. |
| Step 3 | show sip-ua register status This command displays the status of local E.164 registrations. |
| Step 4 | show sip-ua statistics This command displays the Register messages that have been sent. |

| Restriction | If the DHCP server is on a different router than Cisco Unified CME,
                                             			 reconfigure the external DHCP server with the new IP address of the TFTP
                                             			 server. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | ip dhcp pool pool-name Example: Router(config)# ip dhcp pool pool2 | Enters DHCP pool configuration mode to create or modify a DHCP
                                             				pool. pool-name —Previously configured
                                                   					 unique identifier for the pool to be configured. |
| Step 4 | option 150 ip ip-address Example: Router(config-dhcp)# option 150 ip 10.0.0.1 | Specifies the TFTP server IP address from which the
                                             				Cisco Unified IP phone downloads the image configuration file,
                                             				XmlDefault.cnf.xml. |
| Step 5 | end Example: Router(config-dhcp)# end | Returns to privileged EXEC mode. |

| Feature
                                          					 Name | Cisco Unified CME Version | Modification |
|---|---|---|
| Olson
                                          					 Timezone | 9.0 | Eliminates
                                          					 the need to update time zone commands or phone loads to accommodate a new
                                          					 country with a new time zone or an existing country whose city or state wants
                                          					 to change their time zone, using the olsontimezone command in either telephony-service or voice register global configuration
                                          					 mode. |