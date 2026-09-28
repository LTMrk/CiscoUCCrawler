---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-sip-param-dhcp-html-a0c27e3022
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-sip-param-dhcp.html
retrieved_at: 2026-08-16T15:48:09.498128+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Configurable SIP Parameters via DHCP

## Chapter: Configurable SIP Parameters via DHCP

# Configurable SIP Parameters via DHCP

## Overview

The Configurable SIP Parameters via DHCP feature allows a Dynamic Host Configuration Protocol (DHCP) server to provide Session
                           Initiation Protocol (SIP) parameters via a DHCP client. These parameters are used for user registration and call routing.

The DHCP server returns the SIP Parameters via DHCP options 120 and 125. These options are used to specify the SIP user registration
                           and call routing information. The SIP parameters returned are the SIP server address via Option 120, and vendor-specific information
                           such as the pilot, contract or primary number, an additional range of secondary numbers, and the SIP domain name via Option
                           125.

In the event of changes to the SIP parameter values, this feature also allows a DHCP message called DHCPFORCERENEW to reset
                           or apply a new set of values.

The SIP parameters provisioned by DHCP are stored, so that on reboot they can be reused.

To perform basic Configurable SIP Parameters via DHCP configuration tasks, you should understand the following concepts:

### Cisco Unified Border Element (CUBE) Support for Configurable SIP Parameters via DHCP

The CUBE provides the support for the DHCP provisioning of the SIP parameters.

The NGN is modeled using SIP as a VoIP protocol. In order to connect to NGN, the User to Network Interface (UNI) specification
                              is used. Cisco TelePresence Systems (CTS), consisting of an IP Phone, a codec, and Cisco Unified Communications Manager, are
                              required to internetwork over the NGN for point-to-point and point-to-multipoint video calls. Because Cisco Unified Communications
                              Manager does not provide a UNI interface, there has to be an entity to provide the UNI interface. The CUBE provides the UNI interface and has several advantages such as demarcation, delayed offer to early offer, and registration.

The figure below shows the CUBE providing the UNI interface for the NGN.

### DHCP to Provision SIP Server, Domain Name, and Phone Number

NGN requires CUBE to support DHCP (RFC 2131 and RFC 2132) to provision the following:

IP address for CUBE ’s UNI interface facing NGN

SIP server address using option 120

Option 125 vendor specific information to get:

Pilot number (also called primary or contract number), there is only one pilot number in DHCPACK, and REGISTER is done only
                                          for the pilot number

Additional numbers, or secondary numbers, are in DHCPACK; there is no REGISTER for additional numbers

SIP domain name

DHCPFORCERENEW to reset or apply a new set of SIP parameters (RFC 3203)

### DHCP-SIP Call Flow

The following scenario shows the DHCP messages involved in provisioning information such as the IP address for UNI interface,
                              and SIP parameters including the SIP server address, phone number, and domain name, along with how SIP messages use the provisioned
                              information.

The figure below shows the DHCP and SIP messages involved in obtaining the SIP parameters and using them for REGISTER and
                              INVITE.

### DHCP Message Details

The DHCP call flow involved in obtaining CUBE provision information, including the IP address for UNI interface and SIP information such as phone number, domain, and SIP
                              server, is shown in the figure below.

The DHCP messages involved in provisioning the SIP parameters are described in Steps 1 to 6.

F1: The CUBE DHCP client sends a DHCPDISCOVER message to find the available NGN DHCP servers on the network and obtain a valid IPv4 address.
                                    The Cisco Unified Border Element DHCP client identity (computer name) and MAC address are included in this message.

F2: The CUBE DHCP client receives a DHCPOFFER message from each available NGN DHCP server. The DHCPOFFER message includes the offered
                                    DHCP server’s IPv4 address, the DHCP client’s MAC address, and other configuration parameters.

F3: The CUBE DHCP client selects an NGN DHCP server and its IPv4 address configuration from the DHCPOFFER messages it receives, and sends
                                    a DHCPREQUEST message requesting its usage. Note that this is where CUBE requests SIP server information via DHCP Option 120 and vendor- identifying information via DHCP Option 125.

F4: The chosen NGN DHCP server assigns its IPv4 address configuration to the CUBE DHCP client by sending a DHCPACK message to it. The Cisco Unified Border Element DHCP client receives the DHCPACK message.
                                    This is where the SIP server address, phone number and domain name information are received via DHCP options 120 and 125.
                                    The CUBE will use the information for registering the phone number and routing INVITE messages to the given SIP server.

F5: When NGN has a change of information or additional information (such as changing SIP server address from 1.1.1.1 to 2.2.2.2)
                                    for assigning to CUBE , the DHCP server initiates DHCPFORCERENEW to the CUBE . If the authentication is successful, the CUBE DHCP client accepts the DHCPFORCERENEW and moves to the next stage of sending DHCPREQUEST. Otherwise DHCPFORCERENEW is ignored
                                    and the current information is retained and used.

F6 and F7: In response to DHCPFORCERENEW, similar to steps F3 and F4, the CUBE requests DHCP Options 120 and 125. Upon getting the response, SIP will apply these parameters if they are different by sending
                                    an UN-REGISTER message for the previous phone number and a REGISTER message for the new number. Similarly, a new domain and
                                    SIP server address will be used. If the returned information is the same as the current set, it is ignored and hence registration
                                    and call routing remains the same.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Configurable SIP Parameters via DHCP

Baseline Functionality

The feature introduces the configuring of SIP parameters via DHCP.

## Prerequisites

A DHCP interface has to be associated with SIP before configurable SIP parameters via DHCP can be enabled.

## Restrictions for Configurable SIP Parameters via DHCP

DHCP Option 120 is the standard DHCP option (RFC3361) to get a SIP server address, and this can be used by any vendor DHCP
                                 server. Only one address is supported, which is in the IPv4 address format. Multiple IPv4 address entries are not supported.
                                 Also, there is no support for a DNS name in this or for any port number given behind the IPv4 address.

DHCP Option 125 (RFC 3925) provides vendor-specific information and its interpretation is associated with the enterprise identity.
                                 The primary and secondary phone numbers and domain are obtained using Option 125, which is vendor-specific. As long as other
                                 customers use the same format as in the Next Generation Network (NGN) DHCP specification, they can use this feature.

A primary or contract number is required in suboption 202 of DHCP Option 125. There can be only one instance of the primary
                                 number and not multiple instances.

Multiple secondary or numbers in suboption 203 of DHCP Option 125 are supported. Up to five numbers are accepted and the rest
                                 ignored. Also, they have to follow the contract number in the DHCP packet data.

Authentication is not supported for REGISTER and INVITE messages sent from a Cisco Unified Border Element that uses DHCP provisioning

The DHCP provisioning of SIP Parameters is supported only over one DHCP interface.

The DHCP option is available only to be configured for the primary registrar. It will not be available for a secondary registrar.

## Configure SIP Parameters via DHCP

### Configure the DHCP Client

To receive the SIP configuration parameters the CUBE has to act as a DHCP client. This is because in the NGN network, a DHCP server pushes the configuration to a DHCP client.
                                 Thus the Cisco Unified Border Element must be configured as a DHCP client.

Perform this task to configure the DHCP client.

#### Before you begin

You must configure the ip dhcp client commands before entering the ip address dhcp command on an interface to ensure that the DHCPDISCOVER messages that are generated contain the correct option values. The ip dhcp client commands are checked only when an IP address is acquired from DHCP. If any of the ip dhcp client commands are entered after an IP address has been acquired from DHCP, the DHCPDISCOVER messages’ correct options will not
                                 be present or take effect until the next time the router acquires an IP address from DHCP. This means that the new configuration
                                 will only take effect after either the ip address dhcp command or the release dhcp and renew dhcp EXEC commands have been configured.

### SUMMARY STEPS

- enable

- configure terminal

- interface type number

- ip dhcp client request sip-server-address

- ip dhcp client request vendor-identifying-specific

- ip address dhcp

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

interface type number

#### Example:

```
Router(config)# interface gigabitethernet 0/0/0
```

Configures an interface type and enters interface configuration mode.

Step 4

ip dhcp client request sip-server-address

#### Example:

```
Router(config-if)# ip dhcp client request sip-server-address
```

Configures the DHCP client to request a SIP server address from a DHCP server.

Step 5

ip dhcp client request vendor-identifying-specific

#### Example:

```
Router(config-if)# ip dhcp client request vendor-identifying-specific
```

Configures the DHCP client to request vendor-specific information from a DHCP server.

Step 6

ip address dhcp

#### Example:

```
Router(config-if)# ip address dhcp
```

Acquires an IP address on the interface from the DHCP.

Step 7

exit

#### Example:

```
Router(config-if)# exit
```

Exits the current mode.

### Example: Configure the DHCP Client

The following is an example is to enable the DHCP client:

```
Router> enable Router# configure terminal Router(config)# interface gigabitethernet 0/0/0 Router(config-if)# ip dhcp client request sip-server-address Router(config-if)# ip dhcp client request vendor-identifying-specific Router(config-if)# ip address dhcp Router(config-if)# exit
```

### Enable the SIP Configuration

Enabling the SIP configuration allows the CUBE to use the SIP parameters received via DHCP for user registration and call
                                 routing. Perform this task to enable the SIP configuration.

#### Before you begin

The dhcp interface command has to be entered to declare the interface before the registrar and credential commands are entered.

### SUMMARY STEPS

- enable

- configure terminal

- interface type number

- sip-ua

- dhcp interface type number

- registrar dhcp expires seconds random-contact refresh-ratio seconds

- credentials dhcp password [ 0 | 7 ] password realm domain-name

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

interface type number

#### Example:

```
Router(config)# interface gigabitethernet 0/0
```

Configures an interface type and enters interface configuration mode.

Step 4

sip-ua

#### Example:

```
Router(config-if)# s ip-ua
```

Enters SIP user-agent configuration mode.

Step 5

dhcp interface type number

#### Example:

```
Router(sip-ua)# dhcp interface gigabitethernet 0/0
```

Assigns a specific interface for DHCP provisioning of SIP parameters.

Multiple interfaces on the CUBE can be configured with DHCP. This command specifies the DHCP interface used with SIP.

Step 6

registrar dhcp expires seconds random-contact refresh-ratio seconds

#### Example:

```
Router(sip-ua)# registrar dhcp expires 100 random-contact refresh-ratio 90
```

Registers E.164 numbers on behalf of analog telephone voice ports (FXS) and IP phone virtual voice ports (EFXS) with an external
                                             SIP proxy or SIP registrar server.

expires seconds --Specifies the default registration time, in seconds. Range is 60 to 65535. Default is 3600.

refresh-ratio seconds --Specifies the refresh-ratio, in seconds. Range is 1 to 100 seconds. Default is 80.

Step 7

credentials dhcp password [ 0 | 7 ] password realm domain-name

#### Example:

```
Router(sip-ua)# credentials dhcp password cisco realm cisco.com
```

Sends a SIP registration message from a Cisco Unified Border Element in the UP state.

Ensure that realm name is configured with domain name. It should not be configured with an IP address as its name.

Step 8

exit

#### Example:

```
Router(sip-ua)# exit
```

Exits the current mode.

### Enable the SIP Configuration Example

The following is an example to enable the SIP configuration:

```
Router> enable Router# configure terminal Router(config)# interface gigabitethernet 1/0 Router(config-if)# sip-ua Router(sip-ua)# dhcp interface gigabitethernet 1/0 Router(sip-ua)# registrar dhcp expires 90 random-contact refresh-ratio 90 Router(sip-ua)# credentials dhcp password cisco realm cisco.com Router(sip-ua)# exit
```

### Tips to Troubleshoot

To display information on DHCP and SIP interaction when SIP parameters are provisioned by DHCP, use the debug ccsip dhcp command in privileged EXEC mode.

### Configure a SIP Outbound Proxy Server

An outbound-proxy configuration sets the Layer 3 address (IP address) for any outbound REGISTER and INVITE SIP messages. The
                              SIP server can be configured as an outbound proxy server in voice service SIP configuration mode or dial peer configuration
                              mode. When enabled in voice service SIP configuration mode, all the REGISTER and INVITE messages are forwarded to the configured
                              outbound proxy server. When enabled in dial-peer configuration mode, only the messages hitting the defined dial-peer will
                              be forwarded to the configured outbound proxy server.

The configuration tasks in each mode are presented in the following sections:

Perform either of these tasks to configure the SIP server as a SIP outbound proxy server.

### Configure a SIP Outbound Proxy Server in Voice Service VoIP Configuration Mode

Perform this task to configure the SIP server as a SIP outbound proxy server in voice service SIP configuration mode.

### SUMMARY STEPS

- enable

- configure terminal

- voice service voip

- sip

- outbound-proxy dhcp

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

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters voice service VoIP configuration mode and specifies VoIP as the voice-encapsulation type.

Step 4

sip

#### Example:

```
Router(config-voi-srv)# sip
```

Enters voice service SIP configuration mode.

Step 5

outbound-proxy dhcp

#### Example:

```
Router(conf-serv-sip)# outbound-proxy dhcp
```

Configures the DHCP client to request a SIP server address from a DHCP server.

Step 6

exit

#### Example:

```
Router(config-serv-sip)# exit
```

Exits the current mode.

### Configure a SIP Outbound Proxy Server in Voice Service VoIP Configuration Mode Example

The following is an example to configure a SIP outbound proxy in voice service SIP configuration mode:

```
Router> enable Router# configure terminal Router(config)# voice service voip Router(config-voi-srv)# sip Router(conf-serv-sip)# outbound-proxy dhcp Router(config-serv-if)# exit
```

### Configure a SIP Outbound Proxy Server and Session Target in Dial Peer Configuration Mode

Perform this task to configure the SIP server as a SIP outbound proxy server in dial peer configuration mode.

SIP must be configured on the dial pier before DHCP is configured. Therefore the session protocol sipv2 command must be executed before the session target dhcp command. DHCP is supported only with SIP configured on the dial peer.

### SUMMARY STEPS

- enable

- configure terminal

- dial-peer voice number voip

- session protocol sipv2

- voice-class sip outbound-proxy dhcp

- session target dhcp

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

dial-peer voice number voip

#### Example:

```
Router(config)# dial-peer voice 10 voip
```

Defines a dial peer, specifies VoIP as the method of voice encapsulation, and enters dial peer configuration mode.

Step 4

session protocol sipv2

#### Example:

```
Router(config-dial-peer)# session protocol sipv2
```

Enters the session protocol type as SIP.

Step 5

voice-class sip outbound-proxy dhcp

#### Example:

```
Router(config-dial-peer)# voice-class sip outbound-proxy dhcp
```

Configures the SIP server received from the DHCP server as a SIP outbound proxy server.

Step 6

session target dhcp

#### Example:

```
Router(config-dial-peer)# session target dhcp
```

Specifies that the DHCP protocol is used to determine the IP address of the session target.

Step 7

exit

#### Example:

```
Router(config-dial-peer)# exit
```

Exits the current mode.

### Configure a SIP Outbound Proxy Server in Dial Peer Configuration Mode Example

The following is an example of how to configure a SIP outbound proxy in dial peer configuration mode:

```
Router> enable Router# configure terminal Router(config)# dial-peer voice 11 voip Router(config-dial-peer)# session protocol sipv2 Router(config-dial-peer)# voice-class sip outbound-proxy dhcp
Router(config-dial-peer)# session target dhcp Router(config-dial-peer)# exit
```

| Feature Name | Releases | Feature Information |
|---|---|---|
| Configurable SIP Parameters via DHCP | Baseline Functionality | The feature introduces the configuring of SIP parameters via DHCP. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | interface type number Example: Router(config)# interface gigabitethernet 0/0/0 | Configures an interface type and enters interface configuration mode. |
| Step 4 | ip dhcp client request sip-server-address Example: Router(config-if)# ip dhcp client request sip-server-address | Configures the DHCP client to request a SIP server address from a DHCP server. |
| Step 5 | ip dhcp client request vendor-identifying-specific Example: Router(config-if)# ip dhcp client request vendor-identifying-specific | Configures the DHCP client to request vendor-specific information from a DHCP server. |
| Step 6 | ip address dhcp Example: Router(config-if)# ip address dhcp | Acquires an IP address on the interface from the DHCP. |
| Step 7 | exit Example: Router(config-if)# exit | Exits the current mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | interface type number Example: Router(config)# interface gigabitethernet 0/0 | Configures an interface type and enters interface configuration mode. |
| Step 4 | sip-ua Example: Router(config-if)# s ip-ua | Enters SIP user-agent configuration mode. |
| Step 5 | dhcp interface type number Example: Router(sip-ua)# dhcp interface gigabitethernet 0/0 | Assigns a specific interface for DHCP provisioning of SIP parameters. Multiple interfaces on the CUBE can be configured with DHCP. This command specifies the DHCP interface used with SIP. |
| Step 6 | registrar dhcp expires seconds random-contact refresh-ratio seconds Example: Router(sip-ua)# registrar dhcp expires 100 random-contact refresh-ratio 90 | Registers E.164 numbers on behalf of analog telephone voice ports (FXS) and IP phone virtual voice ports (EFXS) with an external
                                             SIP proxy or SIP registrar server. expires seconds --Specifies the default registration time, in seconds. Range is 60 to 65535. Default is 3600. refresh-ratio seconds --Specifies the refresh-ratio, in seconds. Range is 1 to 100 seconds. Default is 80. |
| Step 7 | credentials dhcp password [ 0 \| 7 ] password realm domain-name Example: Router(sip-ua)# credentials dhcp password cisco realm cisco.com | Sends a SIP registration message from a Cisco Unified Border Element in the UP state. Note Ensure that realm name is configured with domain name. It should not be configured with an IP address as its name. | Note | Ensure that realm name is configured with domain name. It should not be configured with an IP address as its name. |
| Note | Ensure that realm name is configured with domain name. It should not be configured with an IP address as its name. |
| Step 8 | exit Example: Router(sip-ua)# exit | Exits the current mode. |

| Note | Ensure that realm name is configured with domain name. It should not be configured with an IP address as its name. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice service voip Example: Router(config)# voice service voip | Enters voice service VoIP configuration mode and specifies VoIP as the voice-encapsulation type. |
| Step 4 | sip Example: Router(config-voi-srv)# sip | Enters voice service SIP configuration mode. |
| Step 5 | outbound-proxy dhcp Example: Router(conf-serv-sip)# outbound-proxy dhcp | Configures the DHCP client to request a SIP server address from a DHCP server. |
| Step 6 | exit Example: Router(config-serv-sip)# exit | Exits the current mode. |

| Note | SIP must be configured on the dial pier before DHCP is configured. Therefore the session protocol sipv2 command must be executed before the session target dhcp command. DHCP is supported only with SIP configured on the dial peer. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | dial-peer voice number voip Example: Router(config)# dial-peer voice 10 voip | Defines a dial peer, specifies VoIP as the method of voice encapsulation, and enters dial peer configuration mode. |
| Step 4 | session protocol sipv2 Example: Router(config-dial-peer)# session protocol sipv2 | Enters the session protocol type as SIP. |
| Step 5 | voice-class sip outbound-proxy dhcp Example: Router(config-dial-peer)# voice-class sip outbound-proxy dhcp | Configures the SIP server received from the DHCP server as a SIP outbound proxy server. |
| Step 6 | session target dhcp Example: Router(config-dial-peer)# session target dhcp | Specifies that the DHCP protocol is used to determine the IP address of the session target. |
| Step 7 | exit Example: Router(config-dial-peer)# exit | Exits the current mode. |