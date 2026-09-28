---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-admin-sccp-sip-srst-configuration-guide-sccp-and-sip-srst-admin-guide-75c53d32d9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/admin/sccp_sip_srst/configuration/guide/SCCP_and_SIP_SRST_Admin_Guide/srst_setting_up_the_network.html
retrieved_at: 2026-08-21T02:49:02.576722+00:00
---

Cisco Unified SRST Administration Guide (All Versions)

# Cisco Unified SRST Administration Guide (All Versions)

Updated: April 25, 2026

Chapter: Setting Up the Network

## Chapter: Setting Up the Network

# Setting Up the Network

This chapter describes how to configure your Cisco Unified Survivable Remote Site Telephony (SRST) router to run DHCP and
                        to communicate with the IP phones during Cisco Unified Communications Manager fallback.

## Information About Setting Up the Network

When the WAN link fails, the Cisco Unified IP Phones detect that they are no longer receiving keepalive packets from Cisco
                           Unified Communications Manager. The Cisco Unified IP Phones then register with the router. The Cisco Unified SRST software
                           is automatically activated and builds a local database of all Cisco Unified IP Phones attached to it (up to its configured
                           maximum). The IP phones are configured to query the router as a backup call-processing source when the central Cisco Unified
                           Communications Manager does not acknowledge keepalive packets. The Cisco Unified SRST router now performs call setup and processing,
                           call maintenance, and call termination.

Cisco Unified Communications Manager uses DHCP to provide Cisco Unified IP Phones with the IP address of Cisco Unified Communications
                           Manager. In a remote branch office, DHCP service is provided either by the SRST router itself or through the Cisco Unified
                           SRST router using DHCP relay. Configuring DHCP is one of two main tasks in setting up network communication. The other task
                           is configuring the Cisco Unified SRST router to receive messages from the Cisco IP phones through the specified IP addresses.
                           Keepalive intervals are also set now.

### MGCP Gateways and SRST

MGCP fallback is a different feature than SRST and, when configured as an individual feature, can be used by a PSTN gateway.
                              To use SRST as your fallback mode on an MGCP gateway, SRST and MGCP fallback must both be configured on the same gateway.
                              MGCP and SRST have had the capability to be configured on the same gateway since Cisco IOS Release 12.2(11)T.

To make outbound calls while in SRST mode on your MGCP gateway, two fallback commands must be configured on the MGCP gateway.
                              These two commands allow SRST to assume control over the voice port and over call processing on the MGCP gateway. With Cisco
                              IOS earlier than 12.3(14)T, the two commands are the ccm-manager fallback-mgcp and call application alternate commands. With Cisco IOS releases after 12.3(14)T, the ccm-manager fallback-mgcp and service commands must be configured. A complete configuration for these commands is shown in the section the Enabling Cisco Unified SRST on an MGCP Gateway section.

The commands listed above are ineffective unless both commands are configured. For instance, your configuration will not work
                                          if you only configure the ccm-manager fallback-mgcp command.

For more information on the fallback methods for MGCP gateways, see Configuring MGCP Gateway Support for Cisco Unified Communications Manager document or the MGCP Gateway Fallback Transition to Default H.323 Session Application document.

### How to Set Up the Network

## Enabling Cisco Unified SRST on an MGCP Gateway

To use SRST as your fallback mode with an MGCP gateway, SRST and MGCP fallback must both be configured on the same gateway.
                           The configuration in the following section allows SRST to assume control over the voice port and over call processing on the
                           MGCP gateway. Due to command changes that were made in Cisco IOS Release 12.3(14)T, use the configuration task that corresponds
                           with the Cisco IOS Release you have installed.

The commands in the configuration section are ineffective unless both commands are configured. For instance, your configuration
                                       will not work if you only configure the ccm-manager fallback-mgcp command.

When an MGCP-controlled PRI goes into SRST mode, do not make or save configuration changes to the NVRAM on the router. If
                                       configuration changes are made and saved in SRST mode, the MGCP-controlled PRI fails when normal MGCP operation is restored.

In IP phone firmware version 14.3.1 and onward, IP phones drop traffic that fails source IP validation. This typically happens
                                       when there is a mismatch between the SRST configuration of the phone and the responding IP address of the SRST gateway.

### Configuring Cisco Unified SRST on an MGCP Gateway Before Cisco IOS Release 12.3(14)T

Perform this task to enable SRST on an MGCP Gateway if you are using software release before Cisco IOS Release 12.3(14)T.

### SUMMARY STEPS

- enable

- configure terminal

- ccm-manager fallback-mgcp

- call application alternate [ application-name ] OR service [ alternate | default ] service-name location

- exit

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

ccm-manager fallback-mgcp

#### Example:

```
Router(config)# ccm-manager fallback-mgcp
```

Enables the gateway fallback feature and allows an MGCP voice gateway to provide call processing services through SRST or
                                             other configured applications when Cisco Unified Communications Manager is unavailable.

Step 4

call application alternate [ application-name ] OR service [ alternate | default ] service-name location

#### Example:

```
Router(config)# call application alternate
```

OR

```
Router(config)# service default
```

The call application alternate command specifies that the default voice application takes over if the MGCP application is not available. The application-name argument is optional and indicates the name of the specific voice application to use if the application in the dial peer
                                             fails. If a specific application name is not entered, the gateway uses the default application.

OR

The service command loads and configures a specific, standalone application on a dial peer. The keywords and arguments are
                                             as follows:

Alternate (Optional). Alternate service to use if the service configured on the dial peer fails.

Default (Optional). Specifies that the default service DEFAULT on the dial peer is used if the alternate service fails.

Service-name: Name that identifies the voice application.

Location: Directory and filename of the Tcl script or VoiceXML document in URL format. For example, flash memory flash:filename , a TFTP tftp://../filename , or an HTTP server http://../filename are valid locations.

Step 5

exit

#### Example:

```
Router(config)# exit
```

Exits global configuration mode and returns to privileged EXEC mode.

### Configuring SRST on an MGCP Gateway Using Cisco IOS Release 12.3(14)T or Later Releases

Perform this task to enable SRST on an MGCP Gateway if you are using Cisco IOS Release 12.3(14)T or later version.

#### Before you begin

Effective with Cisco IOS Release 12.3(14)T, the call application alternate command is replaced by the service command. The
                                 service command can be used in all releases after Cisco IOS Release 12.3(14)T.

### SUMMARY STEPS

- enable

- configure terminal

- ccm-manager fallback-mgcp

- application [ application-name ]

- global

- service [ alternate | default ] service-name location

- exit

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

ccm-manager fallback-mgcp

#### Example:

```
Router(config)# ccm-manager fallback-mgcp
```

Enables the gateway fallback feature and allows an MGCP voice gateway to provide call processing services through SRST or
                                             other configured applications when Cisco Unified Communications Manager is unavailable.

Step 4

application [ application-name ]

#### Example:

```
Router(config) application app-xfer
```

The application-name argument is optional and indicates the name of the specific voice application to use if the application in the dial peer
                                             fails. If a specific application name is not entered, the gateway uses the DEFAULT application.

Step 5

global

#### Example:

```
Router(config)# global
```

Enters global configuration mode.

Step 6

service [ alternate | default ] service-name location

#### Example:

```
Router(config) service myapp
https://myserver/myfile.vxml
```

Loads and configures a specific, standalone application on a dial peer.

Alternate (Optional). Alternate service to use if the service configured on the dial peer fails.

Default (Optional). Specifies that the default service DEFAULT on the dial peer is used if the alternate service fails.

Service-name: Name that identifies the voice application.

Location: Directory and filename of the Tcl script or VoiceXML document in URL format. For example, flash memory flash:filename , a TFTP tftp://../filename , or an HTTP server http://../filename are valid locations.

Step 7

exit

#### Example:

```
Router(config)# exit
```

Exits global configuration mode and returns to privileged EXEC mode.

### Configuration Example of Enabling SRST on a MGCP Gateway using Cisco IOS Release 12.3(14)T

The following is an example of configuring SRST on an MGCP Gateway if you are using Cisco IOS Release 12.3(14)T or later release:

```
isdn switch-type primary-net5
!
!
ccm-manager fallback-mgcp
ccm-manager mgcp
ccm-manager config
mta receive maximum-recipients 0
!
controller E1 1/0
pri-group timeslots 1-12,16 service mgcp
!
controller E1 1/1
!
!
!
interface Ethernet0/0
ip address 10.48.80.9 255.255.255.0
half-duplex
!
interface Serial1/0:15
no ip address
no logging event link-status
isdn switch-type primary-net5
isdn incoming-voice voice
isdn bind-l3 ccm-manager
no cdp enable
!
!
!
call rsvp-sync
!
call application alternate DEFAULT
!--- For Cisco IOS® Software Release 12.3(14)T or later,
this command was replaced by the service command
in global application configuration mode.
application
global
service alternate Default
!
voice-port 1/0:15
!
mgcp
mgcp dtmf-relay voip codec all mode cisco
mgcp package-capability rtp-package
mgcp sdp simple
!
mgcp profile default
!
!
!
dial-peer cor custom
!
!
!
dial-peer voice 10 pots
application mgcpapp
incoming called-number
destination-pattern 9T
direct-inward-dial
port 1/0:15
!
!
call-manager-fallback
limit-dn 7960 2
ip source-address 10.48.80.9 port 2000
max-ephones 10
max-dn 32
dialplan-pattern 1 704.... extension-length 4
keepalive 20
default-destination 5002
alias 1 5003 to 5002
call-forward busy 5002
call-forward noan 5002 timeout 12
time-format 24
!
!
line con 0
exec-timeout 0 0
line aux
```

## Configuring DHCP for Cisco Unified SRST Phones

To perform this task, you must have your network configured with DHCP. For further details about DHCP configuration, see the Cisco IOS DHCP Server document and see your Cisco Unified Communications Manager documentation.

When a Cisco IP phone is connected to the Cisco Unified SRST system, it automatically queries for a DHCP server. The DHCP
                           server responds by assigning an IP address to the Cisco IP phone and providing the IP address of the TFTP server through DHCP
                           option 150. Then, the phone registers with the Cisco Unified Communications Manager system server and attempts to get configuration
                           and phone firmware files from the Cisco Unified Communications Manager TFTP server address provided by the DHCP server.

When setting up your network, configure your DHCP server local to your site. You may use your SRST router to provide DHCP
                           service (recommended). If your DHCP server is across the WAN and there is an extended WAN outage, the DHCP lease times on
                           your Cisco Unified IP Phones may expire. This may cause your phones to lose their IP addresses, resulting in a loss of service.
                           Rebooting your phones when there is no DHCP server available after the DHCP lease has expired will not reactivate the phones,
                           because they will be unable to obtain an IP address or other configuration information. Having your DHCP server local to your
                           remote site ensures that the phones can continue to renew their IP address leases in the event of an extended WAN failure.

Choose one of the following tasks to set up DHCP service for your Cisco UnifiedIP Phones:

Defining a Single DHCP IP Address Pool —Use this method if the Cisco Unified SRST router is a DHCP server and if you can use a single shared address pool for all
                                 your DHCP clients.

Defining a Separate DHCP IP Address Pool for Each Cisco Unified IP Phone —Use this method if the Cisco Unified SRST router is a DHCP server and you need separate pools for non-IP-phone DHCP clients.

Defining the DHCP Relay Server —Use this method if the Cisco Unified SRST router is not a DHCP server and you want to relay DHCP requests from IP phones
                                 to a DHCP server on a different router.

### Defining a Single DHCP IP Address Pool

This task creates a large shared pool of IP addresses in which all DHCP clients receive the same information, including the
                                 option 150 TFTP server IP address. The benefit of selecting this method is that you set up only one DHCP pool. However, defining
                                 a single DHCP IP address pool can be a problem if non-IP phone clients need to use a different TFTP server address.

### SUMMARY STEPS

- ip dhcp pool pool-name

- network ip-address [ mask | prefix -length

- option 150 ip ip-address

- default-router ip-address

- exit

### DETAILED STEPS

Step 1

ip dhcp pool pool-name

#### Example:

```
Router(config)# ip dhcp pool mypool
```

Creates a name for the DHCP server address pool and enters DHCP pool configuration mode.

Step 2

network ip-address [ mask | prefix -length

#### Example:

```
Router(config-dhcp)# network 10.0.0.0 255.255.0.0
```

Specifies the IP address of the DHCP address pool and the optional mask or number of bits in the address prefix, preceded
                                             by a forward slash.

Step 3

option 150 ip ip-address

#### Example:

```
Router(config-dhcp)# option 150 ip 10.0.22.1
```

Specifies the TFTP server address from which the Cisco IP phone downloads the image configuration file. This needs to be the
                                             IP address of Cisco Unified CM.

Step 4

default-router ip-address

#### Example:

```
Router(config-dhcp)# default-router 10.0.0.1
```

Specifies the router to which the Cisco Unified IP phones are connected directly.

This router should be the Cisco Unified SRST router because this is the default address that is used to obtain SRST service
                                             in the event of a WAN outage. As long as the Cisco IP phones have a connection to the Cisco Unified SRST router, the phones
                                             are able to get the required network details.

Step 5

exit

#### Example:

```
Router(config-dhcp)# exit
```

Exits DHCP pool configuration mode.

### Defining a Separate DHCP IP Address Pool for Each Cisco Unified IP Phone

This task creates a name for the DHCP server address pool and specifies IP addresses. This method requires you to make an
                                 entry for every Cisco Unified IP phone.

### SUMMARY STEPS

- ip dhcp pool pool-name

- host ip-address subnet-mask

- option 150 ip ip-address

- default-router ip-address

- exit

### DETAILED STEPS

Step 1

ip dhcp pool pool-name

#### Example:

```
Router(config)# ip dhcp pool pool2
```

Creates a name for the DHCP server address pool and enters DHCP pool configuration mode.

Step 2

host ip-address subnet-mask

#### Example:

```
Router(config-dhcp)# host 10.0.0.0 255.255.0.0
```

Specifies the IP address that you want the phone to use.

Step 3

option 150 ip ip-address

#### Example:

```
Router(config-dhcp)# option 150 ip 10.0.22.1
```

Specifies the TFTP server address from which the Cisco IP phone downloads the image configuration file. This needs to be the
                                             IP address of Cisco Unified CM.

Step 4

default-router ip-address

#### Example:

```
Router(config-dhcp)# default-router 10.0.0.1
```

Specifies the router to which the Cisco Unified IP phones are connected directly.

This router should be the Cisco Unified SRST router because this is the default address that is used to obtain SRST service
                                             in the event of a WAN outage. As long as the Cisco IP phones have a connection to the Cisco Unified SRST router, the phones
                                             are able to get the required network details.

Step 5

exit

#### Example:

```
Router(config-dhcp)# exit
```

Exits DHCP pool configuration mode.

### Defining the DHCP Relay Server

This task sets up DHCP relay on the LAN interface where the Cisco Unified IP phones are connected and enables the Cisco IOS
                                 DHCP server feature to relay requests from DHCP clients (phones) to a DHCP server. For further details about DHCP configuration,
                                 see the Cisco IOS DHCP Server document. The Cisco IOS DHCP server feature is enabled on routers by default. If the DHCP server is not enabled on your Cisco
                                 Unified SRST router, use the following steps to enable it.

### SUMMARY STEPS

- service dhcp

- interface type number

- ip helper-address ip-address

- exit

### DETAILED STEPS

Step 1

service dhcp

#### Example:

```
Router(config)# service dhcp
```

Enables the Cisco IOS DHCP Server feature on the router.

Step 2

interface type number

#### Example:

```
Router(config)# interface serial 0
```

Enters interface configuration mode for the specified interface. See Cisco IOS Interface and Hardware Component Command Reference, Release 12.3T for more information.

Step 3

ip helper-address ip-address

#### Example:

```
Router(config-if)# ip helper-address 10.0.22.1
```

Specifies the helper address for any unrecognized broadcast for TFTP server and Domain Name System (DNS) requests. For each
                                             server, a separate ip helper-address command is required if the servers are on different hosts. You can also configure multiple TFTP server targets by using the ip helper-address command for multiple servers.

Step 4

exit

#### Example:

```
Router(config-if)# exit
```

Exits interface configuration mode.

## Specifying Keepalive Intervals

The keepalive interval is the period of time between keepalive messages sent by a network device. A keepalive message is a
                              message sent by one network device to inform another network device that the virtual circuit between the two is still active.

If you plan to use the default time interval between messages, which is 30 seconds, you do not have to perform this task.

### SUMMARY STEPS

- call-manager-fallback

- keepalive seconds

- exit

### DETAILED STEPS

Step 1

call-manager-fallback

### Example:

```
Router(config)# call-manager-fallback
```

Enters call-manager-fallback configuration mode.

Step 2

keepalive seconds

### Example:

```
Router(config-cm-fallback)# keepalive 60
```

Sets the time interval, in seconds, between keepalive messages that are sent to the router by Cisco Unified IP Phones.

Seconds: Range is 10 to 65535. Default is 30.

Step 3

exit

### Example:

```
Router(config-cm-fallback)# exit
```

Exits call-manager-fallback configuration mode.

### Example

The following example sets a keepalive interval of 45 seconds:

```
call-manager-fallback
keepalive 45
```

### What to do next

The next step is setting up the phone and getting a dial tone. For instructions, see the Cisco Unified SIP SRST 4.1 section.

| Note | The commands listed above are ineffective unless both commands are configured. For instance, your configuration will not work
                                          if you only configure the ccm-manager fallback-mgcp command. |
|---|---|

| Note | The commands in the configuration section are ineffective unless both commands are configured. For instance, your configuration
                                       will not work if you only configure the ccm-manager fallback-mgcp command. |
|---|---|

| Note | When an MGCP-controlled PRI goes into SRST mode, do not make or save configuration changes to the NVRAM on the router. If
                                       configuration changes are made and saved in SRST mode, the MGCP-controlled PRI fails when normal MGCP operation is restored. |
|---|---|

| Note | In IP phone firmware version 14.3.1 and onward, IP phones drop traffic that fails source IP validation. This typically happens
                                       when there is a mismatch between the SRST configuration of the phone and the responding IP address of the SRST gateway. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | ccm-manager fallback-mgcp Example: Router(config)# ccm-manager fallback-mgcp | Enables the gateway fallback feature and allows an MGCP voice gateway to provide call processing services through SRST or
                                             other configured applications when Cisco Unified Communications Manager is unavailable. |
| Step 4 | call application alternate [ application-name ] OR service [ alternate \| default ] service-name location Example: Router(config)# call application alternate OR Router(config)# service default | The call application alternate command specifies that the default voice application takes over if the MGCP application is not available. The application-name argument is optional and indicates the name of the specific voice application to use if the application in the dial peer
                                             fails. If a specific application name is not entered, the gateway uses the default application. OR The service command loads and configures a specific, standalone application on a dial peer. The keywords and arguments are
                                             as follows: Alternate (Optional). Alternate service to use if the service configured on the dial peer fails. Default (Optional). Specifies that the default service DEFAULT on the dial peer is used if the alternate service fails. Service-name: Name that identifies the voice application. Location: Directory and filename of the Tcl script or VoiceXML document in URL format. For example, flash memory flash:filename , a TFTP tftp://../filename , or an HTTP server http://../filename are valid locations. |
| Step 5 | exit Example: Router(config)# exit | Exits global configuration mode and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | ccm-manager fallback-mgcp Example: Router(config)# ccm-manager fallback-mgcp | Enables the gateway fallback feature and allows an MGCP voice gateway to provide call processing services through SRST or
                                             other configured applications when Cisco Unified Communications Manager is unavailable. |
| Step 4 | application [ application-name ] Example: Router(config) application app-xfer | The application-name argument is optional and indicates the name of the specific voice application to use if the application in the dial peer
                                             fails. If a specific application name is not entered, the gateway uses the DEFAULT application. |
| Step 5 | global Example: Router(config)# global | Enters global configuration mode. |
| Step 6 | service [ alternate \| default ] service-name location Example: Router(config) service myapp
https://myserver/myfile.vxml | Loads and configures a specific, standalone application on a dial peer. Alternate (Optional). Alternate service to use if the service configured on the dial peer fails. Default (Optional). Specifies that the default service DEFAULT on the dial peer is used if the alternate service fails. Service-name: Name that identifies the voice application. Location: Directory and filename of the Tcl script or VoiceXML document in URL format. For example, flash memory flash:filename , a TFTP tftp://../filename , or an HTTP server http://../filename are valid locations. |
| Step 7 | exit Example: Router(config)# exit | Exits global configuration mode and returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | ip dhcp pool pool-name Example: Router(config)# ip dhcp pool mypool | Creates a name for the DHCP server address pool and enters DHCP pool configuration mode. |
| Step 2 | network ip-address [ mask \| prefix -length Example: Router(config-dhcp)# network 10.0.0.0 255.255.0.0 | Specifies the IP address of the DHCP address pool and the optional mask or number of bits in the address prefix, preceded
                                             by a forward slash. |
| Step 3 | option 150 ip ip-address Example: Router(config-dhcp)# option 150 ip 10.0.22.1 | Specifies the TFTP server address from which the Cisco IP phone downloads the image configuration file. This needs to be the
                                             IP address of Cisco Unified CM. |
| Step 4 | default-router ip-address Example: Router(config-dhcp)# default-router 10.0.0.1 | Specifies the router to which the Cisco Unified IP phones are connected directly. This router should be the Cisco Unified SRST router because this is the default address that is used to obtain SRST service
                                             in the event of a WAN outage. As long as the Cisco IP phones have a connection to the Cisco Unified SRST router, the phones
                                             are able to get the required network details. |
| Step 5 | exit Example: Router(config-dhcp)# exit | Exits DHCP pool configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | ip dhcp pool pool-name Example: Router(config)# ip dhcp pool pool2 | Creates a name for the DHCP server address pool and enters DHCP pool configuration mode. |
| Step 2 | host ip-address subnet-mask Example: Router(config-dhcp)# host 10.0.0.0 255.255.0.0 | Specifies the IP address that you want the phone to use. |
| Step 3 | option 150 ip ip-address Example: Router(config-dhcp)# option 150 ip 10.0.22.1 | Specifies the TFTP server address from which the Cisco IP phone downloads the image configuration file. This needs to be the
                                             IP address of Cisco Unified CM. |
| Step 4 | default-router ip-address Example: Router(config-dhcp)# default-router 10.0.0.1 | Specifies the router to which the Cisco Unified IP phones are connected directly. This router should be the Cisco Unified SRST router because this is the default address that is used to obtain SRST service
                                             in the event of a WAN outage. As long as the Cisco IP phones have a connection to the Cisco Unified SRST router, the phones
                                             are able to get the required network details. |
| Step 5 | exit Example: Router(config-dhcp)# exit | Exits DHCP pool configuration mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | service dhcp Example: Router(config)# service dhcp | Enables the Cisco IOS DHCP Server feature on the router. |
| Step 2 | interface type number Example: Router(config)# interface serial 0 | Enters interface configuration mode for the specified interface. See Cisco IOS Interface and Hardware Component Command Reference, Release 12.3T for more information. |
| Step 3 | ip helper-address ip-address Example: Router(config-if)# ip helper-address 10.0.22.1 | Specifies the helper address for any unrecognized broadcast for TFTP server and Domain Name System (DNS) requests. For each
                                             server, a separate ip helper-address command is required if the servers are on different hosts. You can also configure multiple TFTP server targets by using the ip helper-address command for multiple servers. |
| Step 4 | exit Example: Router(config-if)# exit | Exits interface configuration mode. |

| Note | If you plan to use the default time interval between messages, which is 30 seconds, you do not have to perform this task. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | call-manager-fallback Example: Router(config)# call-manager-fallback | Enters call-manager-fallback configuration mode. |
| Step 2 | keepalive seconds Example: Router(config-cm-fallback)# keepalive 60 | Sets the time interval, in seconds, between keepalive messages that are sent to the router by Cisco Unified IP Phones. Seconds: Range is 10 to 65535. Default is 30. |
| Step 3 | exit Example: Router(config-cm-fallback)# exit | Exits call-manager-fallback configuration mode. |