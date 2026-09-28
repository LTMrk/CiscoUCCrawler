---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-vrf-design-guide-vrfdesignguide-html-78de37d6cf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/vrf/design/guide/vrfDesignGuide.html
retrieved_at: 2026-08-21T09:46:40.979616+00:00
---

Virtual Route Forwarding Design Guide

# Virtual Route Forwarding Design Guide

- Guide

- Connectivity

### Download Options

Updated: November 12, 2008

## Table Of Contents

Virtual Route Forwarding Design Guide for VRF-Aware Cisco Unified Communications Manager Express

Contents

Introduction

Virtualization of Networks

Topology

Elements Description

SIP Cisco Unified CME

SCCP Cisco Unified CME

SCCP Controlled Analog Endpoints

Configuring a Voice VRF

Prerequisites

Restrictions

Examples

Cisco IOS Global Configuration

VoIP and POTS Dial Peers

DHCP Configurations

Cisco Unified CME SCCP Phone Configuration

Cisco Unified CME SIP Phone Configuration

CME Supplementary Services

VRF-Aware Configuration Example

Configuring Cisco Unified CME 1

Configuring Cisco Unified CME 2

Configuring Cisco Unity Express for Cisco Unified CME Voice Mail

Configuring Cisco Unified CME and DSP Farm on the Same Box for Conference, Transcoder, and Media Termination Point

Configuring Cisco Unified CME and DSP Farm on the Different Boxes for Conference, Transcoder, and Media Termination Point

Verification

## Virtual Route Forwarding Design Guide for VRF-Aware Cisco Unified Communications Manager Express

First Published: October 10, 2008

This document provides an overview, a sample configuration, and other information for connecting and using Virtual Route Forwarding (VRF) with your network.

## Contents

• Introduction

• Topology

• Elements Description

• Configuring a Voice VRF

• Verification

## Introduction

Virtualization is a technique for hiding the physical characteristics of computing resources from the way in which other systems, applications, or end users interact with those resources. This includes making a single physical resource (such as a server, an operating system, an application, storage device, or network) appear to function as multiple logical resources; or it can include making multiple physical resources (such as storage devices or servers) appear as a single logical resource.

Virtual networks is a generic term that uses many different technologies to provide virtualization. Fundamentally, virtual networks all provide a mechanism to deploy what looks and operates like multiple networks, and are actually all using the same hardware and physical connectivity.

A distinction needs to be made among the types of virtualization and which layer this network virtualization occurs at:

• Physical (Layer 1)—A Time Division Multiplexer (TDM) provides a way to make a single physical connection look like many physical connections, while still maintaining separation.

• Datalink (Layer 2)—Frame Relay, Asynchronous Transfer Mode (ATM), and Ethernet switches are all examples of how a single physical link may provide multiple logical or virtual connections per physical connection.

• Network (Layer 3)—Routers are examples of how multiple sessions can be carried over a single connection using IP addresses as the identifier. Routers use IP addresses to direct the data to the correct destination. When an IP packet is received the destination address is looked up in a route table to determine the next hop to send the packet to. Normally all packets within a physical router use the same route table or global table.

### Virtualization of Networks

If we needed IP networks that are isolated as they were used by different companies, departments, or organizations, we would normally deploy multiple IP networks made up of separate physical routers that were not connected to each other. They may still be using a shared Layer 2 or Layer 1 infrastructure, however at Layer 3 they are not connected and do not form a network.

Network virtualization allows a single physical router to have multiple route tables. The global table contains all IP interfaces that are not part of a specific virtual network and route tables are for each unique virtual network assigned to an IP interface.

In its basic form this allows a FastEthernet 0/0 IP interface to be in virtual network 10 and FastEthernet 0/1 IP interface to be in virtual network 20. Packets arriving on FastEthernet 0/0 are only forwarded to other interfaces in virtual network 10 and do not use FastEthernet 0/1, because it is not in its virtual network: virtual network 10 has no routing knowledge of other virtual networks.

Additional virtualization can be provided by allowing multiple virtual networks per physical connection. This is enabled by using Layer 2 logical connections. For a FastEthernet physical port, the use of multiple virtual LANs (VLANs) allows each VLAN to use a different virtual network.

Virtual Route Forward (VRF) is a technique which creates multiple virtual networks within a single network entity ( Figure 1 ). In a single network component, multiple VRF resources create the isolation between virtual networks.

Figure 1

Virtual Route Forwarding

VRF implementations in Cisco Unified Communications Manager Express (Cisco Unified CME) include:

• Single voice network and multiple data networks, which consolidate voice communication into one logically partitioned network to separate voice and data communication on a converged multimedia network.

• Enable Cisco Unified CME on an MPLS provider edge router.

• Enable Cisco Unified CME on multiple CE (VRF Lite) routers.

• Multiple voice networks and multiple data networks, which share a Cisco Unified CME by multiple closed users group with different requirements. Check the feature restrictions for details; VRF does not support identical IP addresses or shared-lines.

## Topology

With an increased adoption of IP communications, the data and voice networks co-exist. VLAN is the existing virtualization technique that is used to separate voice networks from data networks. However, in a case where a softphone from a PC (in a data VLAN) wants to talk to a hard-phone in a voice VLAN, the current solution is to allow routing between these two networks through a global routing table. As a result, it creates a potential security threat since the voice VLAN is now visible from the data network.

With the old TDM telephony model, these two were independent networks and have no visibility to each other. A customer talking to an agent on a voice network has no access to the data world of that agent. However, with IP communications, since both are on the same network, security is a significant concern.

Security can be improved by deploying virtualization at the network level. VRF technology can be used with the rules and policies so that each VRF network achieves the expected level of security. The system allow only the softphone application to talk to the hard-phone in a voice VRF, or allow different soft phones within data VRF resources to talk to each other, however, do not allow other applications to communicate with each other.

Figure 2 shows the traditional deployment of Cisco Unified CME, where multiple departments are connected to Cisco Unified CME for voice and data communication. In this deployment, we see both PSTN and WAN connectivity, allowing for interbranch communication through the WAN link. They can reach the rest of the world through the PSTN. In a real life deployment, we may not see that all the phones and PCs directly connected to Ethernet ports of the Cisco Unified CME router. There may be a lot of Ethernet switches in between the Cisco Unified CME and IP devices.

Whatever way the phones and computers are connected to the Cisco Unified CME router, the voice and data network is always separated by VLANs. Usually, all the IP phones are part of the voice VLAN and all other IP devices are in the regular data VLAN. IP phones are not accessible from the data network, although they may share the same physical layers. Virtualization is created through VLANs. To accommodate multiple departments, multiple VLANs are created for security purposes.

Figure 2 Typical Deployment of Cisco Unified Communications Manager Express

To explain the deployment scenario, we show the detail connectivity in Figure 3 , where all the devices from "Finance" and "Sales" departments are connected directly to the Ethernet ports of the Cisco Unified CME. In Figure 3 , there are 3 different VLANs:

• VLAN ID 201: Used for phones. All the IP phones belong to this VLAN, regardless of the department. That means that both the finance and sales departments have the same VLAN ID for phones.

• VLAN ID 202: Created to pass data within finance department.

• VLAN ID 203: Created to support data within sales department.

This is layer-2 virtualization. The limitations are:

• Softphones cannot communicate with IP phones, because they belong to different VLANS (data and voice VLANs, respectively).

• There is no separation of traffic when it flows towards the WAN link.

• This box cannot be shared by different organizations. For example, if this box is located in a superstore and then a bank wants to setup a small booth inside that superstore, the bank cannot use this box. The reason is security: there would be no separation between the networks.

Figure 3

Typical Deployment of Cisco Unified Communications Manager Express with VLAN

Now, in the same network, we can introduce Layer-3 virtualization by using Virtual Route Forward (VRF). With VRF the Cisco Unified CME can be virtually partitioned into multiple Cisco Unified CME routers. An example for this application is a single Cisco Unified CME being shared by both a supermarket and a Coffee shop/Bank in a campus, but as networks, they can not talk to each other except over a PSTN or through restricted route leaks.

Another example of the VRF in voice networks is to split Cisco Unified CME into different VRF networks, one for each department, such as finance, sales, HR, marketing, guest network, employees, and so on. The actual call processing rules can be applied by voice on a per VRF basis in this case.

Each of the virtual Cisco Unified CME routers handles the phones registered under that virtual Cisco Unified CME. Figure 4 shows two virtual Cisco Unified CME routers hosted in a single Cisco Unified CME platform. They work like independent Cisco Unified CME routers.

Figure 4

Typical Deployment of Cisco Unified Communications Manager Express with VRF

In this example, we have both data and voice together where:

• Finance Virtual — Cisco Unified CME has its own voice and data network (VRF: Finance)

• Sales Virtual — Cisco Unified CME has its own voice and data network (VRF: Sales)

• The Finance department has its own secured server, where only the Finance department can access those resources. Similarly, the Sales department has its own server, which is accessible to only the Sales department.

• Finance should not be able to access Sales servers/resources and vice versa.

• Both the Finance and Sales departments have IP telephones controlled by Cisco Unified CME. Those phones should be able to communicate among each other, including sharing the common voice gateways, voice mail servers, and so on. In Figure 4 , the Finance department has 3 IP phones and few computers. The Sales department has 2 IP phones, softphones, and computers.

• Softphones from both data VRF resources (Finance and Sales) can communicate with IP phones.

A VRF is assigned to an interface. The devices behind this interface are all under a particular VRF and all phones behind this VRF interface can communicate with its server in the same VRF. In this case, the Cisco Unified CME router is the server. In a device with multiple interfaces, each of the interfaces can be assigned a VRF. The interfaces that are not assigned to a VRF use the global routing table as the default routing table (for example, the VRF table ID is 0).

## Elements Description

Voice network virtualization adds VRF support for Cisco Unified CME, conferencing, transcoding, and so on. Enabling VRF-awareness in Cisco Unified CME and SRST (Survivable Remote Site Telephony) allows the SCCP phone or SIP IP phones associated with Cisco Unified CME or SRST to be assigned a VRF-ID. Cisco Unified CME IP phones and conferencing/transcoding/TRP (Media Termination Functionality) voice components can be assigned to the voice VRF. It also allows softphones in data VRF resources to communicate with hard phones in a voice VRF.

The overall components for Cisco Unified CME deployment include:

• SIP/SCCP phones under Cisco Unified CME

• Internal Xcoder/Conference/TRP (Media Termination Functionality)

• Hard/analog phone in a single voice VRF and a softphone in multiple data VRF resources

In this solution, we assume that the softphones (SCCP only) from PCs register through a data VRF. We also assume that all hard phones are registered through a voice VRF (a global and default VRF). Like softphones, the TAPI client from PCs also register to the SCCP server through a data VRF.

We recommend that you use a TRP device (controlled by a Cisco Unified CME server process, internal TRP) when interVRF communication needs to be done. For SCCP Cisco Unified CME, the TRP device handles media transmit functions for both media streams in order to flow through Cisco Unified CME. You must set correct VRF IDs for both media streams through this TRP functionality in the Cisco Unified CME router.

### SIP Cisco Unified CME

The SIP layer is made VRF aware. Cisco IOS software supports single voice VRF for SIP, which is based on global voice VRF configuration.

### SCCP Cisco Unified CME

Cisco Unified CME behaves like an independent Cisco Unified CME for each of the VRF endpoints. In Figure 5 , endpoints shown in blue register and communicate with Cisco Unified CME, which is listening on a standard socket in the blue Cisco Unified CME address space. This is the same for other VRF resources —green endpoints send their registration and other communications to their advertised green Cisco Unified CME address.

Figure 5

Different Components Register to Cisco Unified CME

The endpoints themselves contact Cisco Unified CME as they did before. No software change is required on the endpoint itself. The Cisco Unified CME ephone server process is now be able to receive registration from different interfaces, (each representing a separate VRF) then to verify and accept the calls coming in from different VRFs.

In the case of SCCP Cisco Unified CME, the VRF ID information is configured for each ephone or a group of ephones, and configuration is used in the routing process. When a call is being routed, depending on the VRF of the outgoing interface, the VRF ID is set on that interface and the call is routed accordingly. The Cisco Unified CME server process determines the VRF of the outgoing interface and sets it accordingly. This applies to both inter and intraVRF form signaling.

For the SCCP Cisco Unified CME TAPI client, the VRF ID information is configured and verified when the TAPI client registers. Registration request for the phone or TAPI client from a different VRF interface other than configured will be rejected.

For media, in a SCCP Cisco Unified CME, two modes are supported. In one mode, media always flows between the endpoints. This is still true for inter-VRF communication, because each of these end devices is capable of reaching the other directly. The second mode is currently to force the media to go through the Cisco Unified CME router. This is achieved using the "TRP" configuration under ephone. This will continue to work for intraVRF media flow-through also without "TRP" configuration.

### SCCP Controlled Analog Endpoints

Figure 5 also shows an analog voice gateway with an FXS interface to analog phones. The VGW (Cisco VG224) talks to Cisco Unified CME using SCCP. The media path between analog VGW and Cisco Unified CME is flow-through when a call goes through the H323/SIP trunk. If the call is between two SCCP endpoints, the path is directly between endpoints. For all practical purposes, the Cisco VG224 acts like an SCCP endpoint. All the phones map 1:1 between a voice port and the ephone. In order for VRF awareness to be extended to these phones, we assume that all the analog phones registering to Cisco Unified CME through the Cisco VG224 are similar to hard ephones and are in the same VRF as hard phones. In order for interVRF calls between phones from analog phones behind analog VGW and data, VRF is the same as interVRF described earlier.

## Configuring a Voice VRF

To configure a voice VRF, you must shutdown voice services on the gateway, assign a previously defined VPN VRF to the VoIP SPI, and then restart voice services.

This section describes the tasks required to configure VRF-aware voice gateways.

Note If a voice VRF is not configured, signaling and media packets are sent using the default routing table.

### Prerequisites

Be sure to check the following prerequisites before configuring a voice VRF:

• To ensure there are no active calls on the voice gateway during a VRF change, you must shut down the voice gateway before you configure or make changes to a voice VRF.

• If your configuration uses address binding, use the h323-gateway voip bind srcaddr ip-address command to bind the gateway to an interface that belongs to the voice VRF.

• If the voice gateway configuration has H.323 RAS enabled, use the h323-gateway voip interface command to configure RAS on the interface that belongs to the voice VRF.

### Restrictions

Restrictions for configuring VRF-aware H.323 and SIP are as follows:

• If the voice gateway configuration has H.323 RAS enabled, the gatekeeper must be accessible to the gateway in the configured voice VRF.

• When voice VRF is configured, the H.323 gateway and gatekeeper cannot communicate with each other if they are on the same router.

Voice VRF supports only the following call types:

• A single VRF for SIP-to-SIP calls

• A single VRF for H323-to-SIP calls

• A single VRF for H323-to-H323 calls

• A single VRF in IP-to-IP gateway calls with a gatekeeper involved, however the gatekeeper is not on the same router.

• A SIP SRST call

• A SCCP SRST call

• A SCCP Cisco Unified CME call

• A SIP Cisco Unified CME call

### SUMMARY STEPS

1. enable

2. configure terminal

3. ip vrf vrfname

4. rd route-distinguisher

5. route-target { import | export | both } route-target-ext-community

6. exit

7. voice service voip

8. shutdown

9. exit

10. voice vrf vrfname

11. voice service voip

12. no shutdown

13. end

### DETAILED STEPS

Command or Action

Purpose

Step 1

enable

Example:

Router> enable

Enables privileged EXEC mode.

• Enter your password if prompted.

Step 2

configure terminal

Example:

Router# configure terminal

Enters global configuration mode.

Step 3

ip vrf vrfname

Example:

Router(config)# ip vrf vrf1

Defines a Virtual Private Network (VPN) routing/forwarding (VRF) instance and enters VRF configuration mode.

• vrfname —Identifier for the VRF.

Step 4

rd route-distinguisher

Example:

Router(config-vrf)# rd 1:1

Creates a routing and forwarding table for a VPN VRF.

• route-distinguisher —Adds an 8-byte value to an IPv4 prefix to create a VPN IPv4 prefix.

Step 5

route-target {import | export | both} route-target-ext-community

Example:

Router(config-vrf)# route-target export 1:2

Creates a list of import or export route target communities for the specified VRF.

• import —Imports routing information from the target VPN extended community.

• export —Exports routing information to the target VPN extended community.

• both —Imports both import and export routing information to the target VPN extended community.

• route-target-ext-community —Adds the route-target extended community attributes to the VRF's list of import, export, or both (import and export) route-target extended communities.

Step 6

exit

Example:

Router(config-vrf)# exit

Exits VRF configuration mode.

Step 7

voice service voip

Example:

Router(config)# voice service voip

Enters voice-service configuration mode.

Step 8

shutdown

Example:

Router(config-voi-serv)# shutdown

Shuts down voice services.

Step 9

exit

Example:

Router(config-voi-serv)# exit

Exits voice-service configuration mode.

Step 10

voice vrf name

Example:

Router(config)# voice vrf vrf1

Assigns a predefined VRF to voice services.

• vrfname —Identifier for the VRF.

Step 11

voice service voip

Example:

Router(config)# voice service voip

Enters voice-service configuration mode.

Step 12

no shutdown

Example:

Router(config-voi-serv)# no shutdown

Restarts voice services.

Step 13

end

Example:

Router(config-voi-serv)# end

Returns to privileged EXEC mode.

### Examples

```
!
```

```
ip vrf vrf1
```

```
rd 1:1
```

```
route-target export 1:2
```

```
route-target import 1:2
```

```
!
```

```
voice vrf vrf1
```

```
!
```

```
voice service voip
```

```
!
```

### Cisco IOS Global Configuration

The following example is part of a Cisco Unified CME/SRST configuration. There are two VRF resources, VPN801 and VPN802, defined for two groups of phones. Cisco Unified CME belongs to the third VRF and is named ccm .

VRF resources VPN801 and VPN802 import routes from and import routes to VRF ccm. VPN801 and VPN802 can access VRF ccm, but their routes are independent of each other.

The default voice VRF is ccm, where SIP phones must belong to and be registered with Cisco Unified CME.

Initially, phones belonging to VRF VPN801 and VPN802 register to Cisco Unified CME.

```
voice vrf ccm
```

```
ip vrf VPN801
```

```
rd 801:1
```

```
route-target export 801:1
```

```
route-target import 1000:1
```

```
!
```

```
ip vrf VPN802
```

```
rd 802:1
```

```
route-target export 802:1
```

```
route-target import 1000:1
```

```
!
```

```
ip vrf ccm
```

```
rd 1000:1
```

```
route-target export 1000:1
```

```
route-target import 801:1
```

```
route-target import 802:1
```

```
!
```

```
interface FastEthernet0/0
```

```
no ip address
```

```
duplex auto
```

```
speed auto
```

```
!
```

```
interface FastEthernet0/0.801
```

```
encapsulation dot1Q 801
```

```
ip vrf forwarding VPN801
```

```
ip address 21.22.21.1 255.255.255.0
```

```
ip helper-address global 21.20.10.11
```

```
!
```

```
interface FastEthernet0/0.802
```

```
encapsulation dot1Q 802
```

```
ip vrf forwarding VPN802
```

```
ip address 21.22.22.1 255.255.255.0
```

```
ip helper-address 21.20.10.11
```

### VoIP and POTS Dial Peers

The dial peers are a global resource and belongs to voice VRF, which are shared and accessible from any VRF. There is no need to specify a dial peer for an individual VRF.

The following example shows how to configure one outgoing ISDN PRI trunk, SIP trunk, and H.323 trunk to any service provider or another Cisco Unified CME.

```
dial-peer voice 2822 pots
```

```
corlist outgoing PSTN-TRUNK
```

```
destination-pattern 7....
```

```
direct-inward-dial
```

```
port 1/0/0:23
```

```
forward-digits 4
```

```
!
```

```
dial-peer voice 2821 voip
```

```
corlist outgoing SIP-TRUNK
```

```
destination-pattern 8....
```

```
voice-class codec 1
```

```
session protocol sipv2
```

```
session target ipv4:11.2.0.1
```

```
dtmf-relay sip-notify
```

```
no vad
```

```
!
```

```
dial-peer voice 1000 voip
```

```
voice-class codec 1
```

```
!
```

```
dial-peer voice 2823 voip
```

```
corlist outgoing H323-TRUBK
```

```
destination-pattern 9....
```

```
voice-class codec 1
```

```
session target ipv4:11.2.0.1
```

```
!
```

```
dial-peer voice 28211 voip
```

```
translation-profile incoming STRIP
```

```
voice-class codec 1
```

```
incoming called-number.%
```

```
no vad
```

```
!
```

### DHCP Configurations

The three ways to define DHCP address allocation are shown below. Duplicate IP addresses, even with VRF specified, are not supported.

1. With a global address allocation scheme, you must use the no ip dhcp use vrf connected command.

```
no ip dhcp use vrf connected
```

```
ip dhcp pool vcme1
```

```
network 20.1.10.0 255.255.255.0
```

```
option 150 ip 20.1.10.1
```

```
default-router 20.1.10.1
```

```
class vcme1
```

```
address range 20.1.10.10 20.1.10.250
```

```
!
```

2. The following example shows how to assign addresses from VRF pool VPN801.

```
ip dhcp use vrf connected
```

```
!
```

```
ip dhcp pool vcme1
```

```
vrf VPN801
```

```
network 20.1.10.0 255.255.255.0
```

```
option 150 ip 20.1.10.1
```

```
default-router 20.1.10.1
```

```
class vcme1
```

```
address range 20.1.10.10 20.1.10.250
```

```
!
```

3. The following example show how to assign an address by an individual host. You must replace the first two hexadecimal digits of a host MAC address with 01 .

```
ip dhcp pool phone3
```

```
host 20.2.10.11 255.0.0.0
```

```
client-identifier 0100.0ed7.4ce6.3d
```

```
default-router 20.2.10.1
```

```
option 150 ip 20.2.10.1
```

```
!
```

### Cisco Unified CME SCCP Phone Configuration

The following example shows how to define telephony-service with up to two VRF resources and two groups of phones.

```
telephony-service
```

```
sdspfarm conference mute-on # mute-off #
```

```
sdspfarm units 4
```

```
sdspfarm transcode sessions 10
```

```
sdspfarm tag 1 xcode101
```

```
sdspfarm tag 2 conf103
```

```
group  1 vrf VPN801
```

```
ip source-address 20.1.10.1 port 2000
```

```
url directories http://20.1.10.1/localdirectory
```

```
!
```

```
group  2 vrf VPN802
```

```
ip source-address 20.2.10.1 port 2000
```

```
!
```

```
load 7960-7940 P00308000400
```

```
load 7941 SCCP41.8-2-1S
```

```
load 7970 SCCP70.8-3-1S
```

```
max-ephones 52
```

```
max-dn 192
```

```
auto assign 100 to 167 type 7960
```

```
auto assign 168 to 192 type anl
```

```
calling-number initiator
```

```
system message vcme 2821
```

```
time-zone 5
```

```
max-conferences 1 gain 6
```

```
call-park system redirect
```

```
call-forward pattern .T
```

```
call-forward system redirecting-expanded
```

```
moh music-on-hold.au
```

```
web admin system name cisco secret 5 $1$3.ZT$q0g3MXmIP8doZmA7v1mXz.
```

```
dn-webedit
```

```
time-webedit
```

```
transfer-system full-consult dss
```

```
transfer-pattern 9.T
```

```
secondary-dialtone 9
```

```
directory last-name-first
```

```
create cnf-files version-stamp 7960 Jan 15 2008 22:32:06
```

```
!
```

```
ephone-dn  1
```

```
number 7483001
```

```
description 7483001
```

```
name 7483001
```

```
!
```

```
!ephone-dn  2
```

```
number 7493001
```

```
description 7493001
```

```
name 7493001
```

```
!
```

```
!ephone  1
```

```
description cme-2801 srst : Aug 27 2007 18:18:20
```

```
mac-address 0012.8055.D2EE
```

```
group phone 1
```

```
button  1:1
```

```
!
```

```
!!ephone  2
```

```
description cme-2801 srst : Aug 27 2007 18:18:20
```

```
mac-address 000E.D710.9F4A
```

```
group phone 2
```

```
button  1:2
```

```
!
```

### Cisco Unified CME SIP Phone Configuration

The following example shows SIP phone registration and definition. A SIP phone must belong to voice VRF. Otherwise, SIP phones do not register properly.

```
voice register global
```

```
mode cme
```

```
source-address 20.2.10.1 port 5060
```

```
max-dn 192
```

```
max-pool 48
```

```
create profile sync 0111955967541377
```

```
!
```

```
voice register dn  5
```

```
number 2002
```

```
allow watch
```

```
label vcme2
```

```
!
```

```
voice register pool  5
```

```
id mac 0014.698C.5D9F
```

```
type 7960
```

```
number 1 dn 5
```

```
presence call-list
```

```
voice-class codec 1
```

```
username xxxx password xxxx
```

```
blf-speed-dial 2 2001 label "group2"
```

```
blf-speed-dial 3 3001 label "group3"
```

```
blf-speed-dial 4 1001 label "group1"
```

```
blf-speed-dial 5 5001 label "group5"
```

```
!
```

### CME Supplementary Services

These services are shared among groups of phones and you must specify a VRF for each service. Phones in VPN801 and VPN802 are controlled by the same set of parameters.

```
voice service voip
```

```
allow-connections h323 to h323
```

```
allow-connections h323 to sip
```

```
allow-connections sip to h323
```

```
allow-connections sip to sip
```

```
supplementary-service h450.12
```

```
h323
```

```
sip
```

```
registrar server expires max 3600 min 3600
```

### VRF-Aware Configuration Example

Figure 6 shows a configuration topology for VRF-Aware SIP call flows on Cisco Unified CME.

Figure 6

Topology for Cisco Unified CME

### Configuring Cisco Unified CME 1

Here is the full configuration of the Cisco Unified CME 1 running on a Cisco ISR 3845 router:

```
!
```

```
version 12.4
```

```
no service timestamps debug uptime
```

```
no service timestamps log uptime
```

```
no service password-encryption
```

```
!
```

```
hostname Router
```

```
!
```

```
boot-start-marker
```

```
boot-end-marker
```

```
!
```

```
card type t1 3 1
```

```
logging message-counter syslog
```

```
no logging buffered
```

```
no logging console
```

```
enable password xxxx
```

```
!
```

```
no aaa new-model
```

```
clock timezone PST -8
```

```
clock summer-time pdt recurring
```

```
no network-clock-participate slot 3
```

```
!
```

```
dot11 syslog
```

```
ip source-route
```

```
ip auth-proxy max-nodata-conns 3
```

```
ip admission max-nodata-conns 3
```

```
ip cef
```

```
!
```

```
!
```

```
no ip dhcp use vrf connected
```

```
!
```

```
ip dhcp pool phone
```

```
network 10.10.10.0 255.255.255.0
```

```
default-router 10.10.10.1
```

```
option 150 ip 10.10.10.1
```

```
!
```

```
ip dhcp pool vrf1
```

```
network 10.1.10.0 255.255.255.0
```

```
default-router 10.1.10.1
```

```
option 150 ip 10.1.10.1
```

```
class vrf1
```

```
address range 10.1.10.10 10.1.10.250
```

```
!
```

```
ip dhcp pool vrf2
```

```
network 10.2.10.0 255.255.255.0
```

```
default-router 10.2.10.1
```

```
option 150 ip 10.2.10.1
```

```
class vrf2
```

```
address range 10.2.10.10 10.2.10.250
```

```
!
```

```
ip dhcp pool vrf3
```

```
network 10.3.10.0 255.255.255.0
```

```
option 150 ip 10.3.10.1
```

```
default-router 10.3.10.1
```

```
class vrf3
```

```
address range 10.3.10.10 10.3.10.250
```

```
!
```

```
ip dhcp pool vrf4
```

```
network 10.4.10.0 255.255.255.0
```

```
default-router 10.4.10.1
```

```
option 150 ip 10.4.10.1
```

```
class vrf4
```

```
address range 10.4.10.10 10.4.10.250
```

```
!
```

```
ip dhcp pool vrf5
```

```
network 10.5.10.0 255.255.255.0
```

```
default-router 10.5.10.1
```

```
option 150 ip 10.5.10.1
```

```
class vrf5
```

```
address range 10.5.10.10 10.5.10.250
```

```
!
```

```
ip dhcp pool subcme4
```

```
network 11.4.10.0 255.255.255.0
```

```
default-router 11.4.10.1
```

```
option 150 ip 11.4.10.1
```

```
class subcme4
```

```
address range 11.4.10.10 11.4.10.250
```

```
!
```

```
ip dhcp pool subcme5
```

```
network 11.5.10.0 255.255.255.0
```

```
default-router 11.5.10.1
```

```
option 150 ip 11.5.10.1
```

```
class subcme5
```

```
address range 11.5.10.10 11.5.10.250
```

```
!
```

```
ip dhcp pool subcme3
```

```
network 11.3.10.0 255.255.255.0
```

```
default-router 11.3.10.1
```

```
option 150 ip 11.3.10.1
```

```
class subcme3
```

```
address range 11.3.10.10 11.3.10.250
```

```
!
```

```
ip dhcp pool subcme2
```

```
network 11.2.10.0 255.255.255.0
```

```
default-router 11.2.10.1
```

```
option 150 ip 11.2.10.1
```

```
class subcme2
```

```
address range 11.2.10.10 11.2.10.250
```

```
!
```

```
ip dhcp pool subcme1
```

```
network 11.1.10.0 255.255.255.0
```

```
option 150 ip 11.1.10.1
```

```
default-router 11.1.10.1
```

```
class subcme1
```

```
address range 11.1.10.10 11.1.10.250
```

```
!
```

```
!
```

```
ip dhcp class vrf1
```

```
!
```

```
ip dhcp class vrf2
```

```
!
```

```
ip dhcp class vrf3
```

```
!
```

```
ip dhcp class vrf4
```

```
!
```

```
ip dhcp class vrf5
```

```
!
```

```
ip dhcp class subcme4
```

```
!
```

```
ip dhcp class subcme5
```

```
!
```

```
ip dhcp class subcme3
```

```
!
```

```
ip dhcp class subcme2
```

```
!
```

```
ip dhcp class subcme1
```

```
!
```

```
ip vrf vrf1
```

```
rd 100:1
```

```
route-target export 100:1
```

```
route-target import 100:1
```

```
!
```

```
ip vrf vrf2
```

```
rd 100:2
```

```
route-target export 100:2
```

```
route-target import 100:2
```

```
!
```

```
ip vrf vrf3
```

```
rd 100:3
```

```
route-target export 100:3
```

```
route-target import 100:3
```

```
!
```

```
ip vrf vrf4
```

```
rd 100:4
```

```
route-target export 100:4
```

```
route-target import 100:4
```

```
!
```

```
ip vrf vrf5
```

```
rd 100:5
```

```
route-target export 100:5
```

```
route-target import 100:5
```

```
!
```

```
no ipv6 cef
```

```
!
```

```
multilink bundle-name authenticated
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
ctl-client
```

```
voice-card 0
```

```
dsp services dspfarm
```

```
!
```

```
voice-card 3
```

```
no dspfarm
```

```
!
```

```
!
```

```
voice rtp send-recv
```

```
voice vrf vrf2
```

```
!
```

```
voice service voip
```

```
allow-connections h323 to h323
```

```
allow-connections h323 to sip
```

```
allow-connections sip to h323
```

```
allow-connections sip to sip
```

```
supplementary-service h450.12
```

```
h323
```

```
h225 timeout keepalive
```

```
sip
```

```
registrar server expires max 3600 min 3600
```

```
!
```

```
!
```

```
voice class codec 1
```

```
codec preference 1 g711ulaw
```

```
codec preference 2 g711alaw
```

```
codec preference 3 g729r8
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
voice register dn  10
```

```
number 2098
```

```
!
```

```
voice register pool  10
```

```
id mac 0017.E014.2473
```

```
number 1 dn 10
```

```
voice-class codec 1
```

```
!
```

```
!
```

```
voice translation-rule 1
```

```
rule 1 /81098/ /1098/
```

```
rule 2 /84099/ /4099/
```

```
rule 3 /91098/ /1098/
```

```
rule 4 /94099/ /4099/
```

```
rule 5 /82099/ /2099/
```

```
rule 6 /81098/ /1098/
```

```
rule 7 /82098/ /2098/
```

```
!
```

```
!
```

```
voice translation-profile STRIP
```

```
translate called 1
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
username xxxx password xxxx
```

```
archive
```

```
log config
```

```
hidekeys
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
controller T1 3/0
```

```
!
```

```
controller T1 3/1
```

```
!
```

```
ip ftp username Administrator
```

```
ip ftp password xxxx
```

```
!
```

```
class-map match-all L3-to-L2_VoIP-Cntrl
```

```
match  dscp af31
```

```
class-map match-all L3-to-L2_VoIP-RTP
```

```
match  dscp ef
```

```
class-map match-all SIP
```

```
match protocol sip
```

```
class-map match-all RTP
```

```
match protocol rtp
```

```
!
```

```
!
```

```
policy-map EthOut
```

```
class RTP
```

```
policy-map output-L3-to-L2
```

```
class L3-to-L2_VoIP-RTP
```

```
set cos 5
```

```
class L3-to-L2_VoIP-Cntrl
```

```
set cos 3
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
interface Loopback5
```

```
ip address 12.5.10.1 255.255.255.255
```

```
!
```

```
interface Loopback101
```

```
ip vrf forwarding vrf1
```

```
ip address 11.1.0.1 255.255.255.255
```

```
!
```

```
interface Loopback102
```

```
ip vrf forwarding vrf2
```

```
ip address 11.2.0.1 255.255.255.255
```

```
!
```

```
interface Loopback103
```

```
ip vrf forwarding vrf3
```

```
ip address 11.3.0.1 255.255.255.255
```

```
!
```

```
interface Loopback104
```

```
ip vrf forwarding vrf4
```

```
ip address 11.4.0.1 255.255.255.255
```

```
!
```

```
interface Loopback105
```

```
ip vrf forwarding vrf5
```

```
ip address 11.5.0.1 255.255.255.255
```

```
!
```

```
interface GigabitEthernet0/0
```

```
no ip address
```

```
duplex auto
```

```
speed auto
```

```
media-type rj45
```

```
no keepalive
```

```
!
```

```
interface GigabitEthernet0/0.301
```

```
encapsulation dot1Q 301
```

```
ip vrf forwarding vrf1
```

```
ip address 10.1.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/0.302
```

```
encapsulation dot1Q 302
```

```
ip vrf forwarding vrf2
```

```
ip address 10.2.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/0.303
```

```
encapsulation dot1Q 303
```

```
ip vrf forwarding vrf3
```

```
ip address 10.3.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/0.304
```

```
encapsulation dot1Q 304
```

```
ip vrf forwarding vrf4
```

```
ip address 10.4.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/0.305
```

```
encapsulation dot1Q 305
```

```
ip vrf forwarding vrf5
```

```
ip address 10.5.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/1
```

```
no ip address
```

```
duplex auto
```

```
speed auto
```

```
media-type rj45
```

```
no keepalive
```

```
!
```

```
interface GigabitEthernet0/1.101
```

```
encapsulation dot1Q 101
```

```
ip vrf forwarding vrf1
```

```
ip address 11.1.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/1.102
```

```
encapsulation dot1Q 102
```

```
ip vrf forwarding vrf2
```

```
ip address 11.2.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/1.103
```

```
encapsulation dot1Q 103
```

```
ip vrf forwarding vrf3
```

```
ip address 11.3.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/1.104
```

```
encapsulation dot1Q 104
```

```
ip vrf forwarding vrf4
```

```
ip address 11.4.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/1.105
```

```
encapsulation dot1Q 105
```

```
ip vrf forwarding vrf5
```

```
ip address 11.5.10.1 255.255.255.0
```

```
!
```

```
interface FastEthernet0/1/0
```

```
!
```

```
interface FastEthernet0/1/1
```

```
!
```

```
interface FastEthernet0/1/2
```

```
!
```

```
interface FastEthernet0/1/3
```

```
!
```

```
interface Service-Engine1/0
```

```
no ip address
```

```
shutdown
```

```
!
```

```
interface Vlan1
```

```
no ip address
```

```
!
```

```
router ospf 101 vrf vrf1
```

```
log-adjacency-changes
```

```
network 10.1.0.0 0.0.255.255 area 0
```

```
network 11.1.0.1 0.0.0.0 area 0
```

```
network 11.0.0.0 0.255.255.255 area 0
```

```
!
```

```
router ospf 102 vrf vrf2
```

```
log-adjacency-changes
```

```
network 10.2.0.0 0.0.255.255 area 0
```

```
network 11.2.0.1 0.0.0.0 area 0
```

```
network 11.0.0.0 0.255.255.255 area 0
```

```
!
```

```
router ospf 103 vrf vrf3
```

```
log-adjacency-changes
```

```
network 10.3.0.0 0.0.255.255 area 0
```

```
network 11.3.0.1 0.0.0.0 area 0
```

```
network 11.0.0.0 0.255.255.255 area 0
```

```
!
```

```
router ospf 104 vrf vrf4
```

```
log-adjacency-changes
```

```
network 10.4.0.0 0.0.255.255 area 0
```

```
network 11.4.0.1 0.0.0.0 area 0
```

```
network 11.0.0.0 0.255.255.255 area 0
```

```
!
```

```
router ospf 105 vrf vrf5
```

```
log-adjacency-changes
```

```
network 10.5.0.0 0.0.255.255 area 0
```

```
network 11.5.0.1 0.0.0.0 area 0
```

```
network 11.0.0.0 0.255.255.255 area 0
```

```
!
```

```
router ospf 109
```

```
log-adjacency-changes
```

```
network 11.9.0.0 0.0.255.255 area 0
```

```
!
```

```
router ospf 210
```

```
log-adjacency-changes
```

```
network 21.10.0.0 0.0.255.255 area 0
```

```
!
```

```
ip forward-protocol nd
```

```
ip http server
```

```
ip http authentication local
```

```
no ip http secure-server
```

```
ip http path flash:
```

```
!
```

```
!
```

```
!
```

```
access-list 101 permit ip host 10.1.10.251 any
```

```
access-list 102 permit ip host 21.10.10.6 any
```

```
access-list 103 permit ip any host 21.10.10.6
```

```
access-list 104 permit ip any host 12.5.10.1
```

```
access-list 105 permit ip host 12.5.10.1 any
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
control-plane
```

```
!
```

```
!
```

```
!
```

```
voice-port 0/0/0
```

```
!
```

```
voice-port 0/0/1
```

```
!
```

```
voice-port 0/0/2
```

```
!
```

```
voice-port 0/0/3
```

```
!
```

```
ccm-manager fax protocol cisco
```

```
!
```

```
mgcp fax t38 ecm
```

```
!
```

```
sccp local Loopback5
```

```
sccp ccm 12.5.10.1 identifier 2 version 4.1
```

```
sccp
```

```
!
```

```
sccp ccm group 2
```

```
bind interface Loopback5
```

```
associate ccm 2 priority 1
```

```
associate profile 103 register conf103
```

```
associate profile 101 register xcode101
```

```
!
```

```
dspfarm profile 101 transcode
```

```
codec g711ulaw
```

```
codec g711alaw
```

```
codec g729ar8
```

```
codec g729abr8
```

```
codec g729r8
```

```
maximum sessions 1
```

```
associate application SCCP
```

```
!
```

```
dspfarm profile 103 conference
```

```
codec g711ulaw
```

```
codec g711alaw
```

```
codec g729ar8
```

```
codec g729abr8
```

```
codec g729r8
```

```
codec g729br8
```

```
maximum sessions 1
```

```
associate application SCCP
```

```
!
```

```
!
```

```
dial-peer voice 3845 voip
```

```
destination-pattern 8....
```

```
voice-class codec 1
```

```
session protocol sipv2
```

```
session target ipv4:20.2.10.1
```

```
dtmf-relay rtp-nte
```

```
no vad
```

```
!
```

```
dial-peer voice 3847 voip
```

```
destination-pattern 9....
```

```
voice-class codec 1
```

```
session target ipv4:20.2.10.1
```

```
!
```

```
dial-peer voice 3851 voip
```

```
destination-pattern 51022.....
```

```
voice-class codec 1
```

```
session target ipv4:20.2.10.1
```

```
dtmf-relay h245-alphanumeric
```

```
!
```

```
dial-peer voice 3850 pots
```

```
destination-pattern 51012.....
```

```
direct-inward-dial
```

```
forward-digits 10
```

```
!
```

```
!
```

```
gateway
```

```
timer receive-rtp 1200
```

```
!
```

```
!
```

```
!
```

```
telephony-service
```

```
sdspfarm conference mute-on # mute-off #
```

```
sdspfarm units 4
```

```
sdspfarm transcode sessions 10
```

```
sdspfarm tag 1 xcode101
```

```
sdspfarm tag 2 conf103
```

```
group  1 vrf vrf1
```

```
ip source-address 10.1.10.1 port 2000
```

```
!
```

```
group  2 vrf vrf2
```

```
ip source-address 10.2.10.1 port 2000
```

```
!
```

```
group  3 vrf vrf3
```

```
ip source-address 10.3.10.1 port 2000
```

```
!
```

```
group  4 vrf vrf4
```

```
ip source-address 10.4.10.1 port 2000
```

```
!
```

```
group  5
```

```
ip source-address 12.5.10.1 port 2000
```

```
!
```

```
conference hardware
```

```
no auto-reg-ephone
```

```
em logout 0:0 0:0 0:0
```

```
max-ephones 240
```

```
max-dn 480
```

```
auto assign 1 to 100 type 7960
```

```
auto assign 204 to 230
```

```
calling-number initiator
```

```
system message vcme3845
```

```
load 7941 SCCP41.8-3-3-13S
```

```
load 7970 SCCP70.8-3-3-13S
```

```
time-zone 5
```

```
voicemail 7710
```

```
max-conferences 8 gain -6
```

```
call-forward pattern .T
```

```
call-forward system redirecting-expanded
```

```
moh music-on-hold.au
```

```
dn-webedit
```

```
time-webedit
```

```
transfer-system full-consult dss
```

```
transfer-pattern 9.T
```

```
secondary-dialtone 9
```

```
create cnf-files version-stamp Jan 01 2002 00:00:00
```

```
!
```

```
!
```

```
ephone-dn  186  dual-line
```

```
number 3333
```

```
conference ad-hoc
```

```
preference 5
```

```
!
```

```
!
```

```
ephone-dn  187  dual-line
```

```
number 3333
```

```
conference ad-hoc
```

```
preference 4
```

```
no huntstop
```

```
!
```

```
!
```

```
ephone-dn  188  dual-line
```

```
number 3333
```

```
conference ad-hoc
```

```
preference 3
```

```
no huntstop
```

```
!
```

```
!
```

```
ephone-dn  189  dual-line
```

```
number 3333
```

```
conference ad-hoc
```

```
preference 2
```

```
no huntstop
```

```
!
```

```
!
```

```
ephone-dn  190  dual-line
```

```
number 3333
```

```
conference ad-hoc
```

```
preference 1
```

```
no huntstop
```

```
!
```

```
!
```

```
ephone-dn  231  dual-line
```

```
number 2099
```

```
label vrf2
```

```
description 2099
```

```
name 2099
```

```
!
```

```
!
```

```
ephone-dn  232  dual-line
```

```
number 70098
```

```
label vrf1
```

```
description 70098
```

```
name 70098
```

```
!
```

```
!
```

```
ephone-dn  233  dual-line
```

```
number 3099
```

```
label vrf3
```

```
description 3099
```

```
name 3099
```

```
call-forward noan 7710 timeout 10
```

```
!
```

```
!
```

```
ephone  59
```

```
device-security-mode none
```

```
!
```

```
!
```

```
!
```

```
ephone  231
```

```
device-security-mode none
```

```
mac-address 000B.5FC2.2C23
```

```
group phone 2
```

```
type 7960
```

```
keep-conference
```

```
button  1:231
```

```
!
```

```
!
```

```
ephone  232
```

```
device-security-mode none
```

```
mac-address 001A.A246.05AC
```

```
group phone 1
```

```
type 7941
```

```
keep-conference
```

```
button  1:232
```

```
!
```

```
!
```

```
ephone  233
```

```
device-security-mode none
```

```
mac-address 000E.D748.5DE3
```

```
group phone 3
```

```
type 7960
```

```
keep-conference
```

```
button  1:233
```

```
!
```

```
!
```

```
line con 0
```

```
exec-timeout 0 0
```

```
line aux 0
```

```
line 66
```

```
no activation-character
```

```
no exec
```

```
transport preferred none
```

```
transport input all
```

```
transport output pad telnet rlogin lapb-ta mop udptn v120
```

```
line vty 0 4
```

```
password xxxx
```

```
login
```

```
!
```

```
exception protocol ftp
```

```
exception dump 9.20.20.253
```

```
exception data-corruption buffer truncate
```

```
scheduler allocate 20000 1000
```

```
end
```

```
Router#
```

### Configuring Cisco Unified CME 2

This is the full configuration of the Cisco Unified CME 2 running on a Cisco ISR 2821 router:

```
!
```

```
! Last configuration change at 22:45:41 pdt Mon Jun 9 2008
```

```
!
```

```
version 12.4
```

```
no service timestamps debug uptime
```

```
no service timestamps log uptime
```

```
no service password-encryption
```

```
!
```

```
hostname Router
```

```
!
```

```
boot-start-marker
```

```
boot-end-marker
```

```
!
```

```
logging message-counter syslog
```

```
no logging buffered
```

```
no logging console
```

```
enable password xxxx
```

```
!
```

```
no aaa new-model
```

```
clock timezone PST -8
```

```
clock summer-time pdt recurring
```

```
no network-clock-participate slot 1
```

```
!
```

```
voice-card 0
```

```
no dspfarm
```

```
!
```

```
voice-card 1
```

```
!
```

```
ip source-route
```

```
!
```

```
!
```

```
ip cef
```

```
no ip dhcp use vrf connected
```

```
!
```

```
ip dhcp pool vrf1
```

```
network 20.1.10.0 255.255.255.0
```

```
default-router 20.1.10.1
```

```
option 150 ip 20.1.10.1
```

```
class vrf1
```

```
address range 20.1.10.10 20.1.10.250
```

```
!
```

```
ip dhcp pool vrf2
```

```
network 20.2.10.0 255.255.255.0
```

```
default-router 20.2.10.1
```

```
option 150 ip 20.2.10.1
```

```
class vrf2
```

```
address range 20.2.10.10 20.2.10.250
```

```
!
```

```
ip dhcp pool vrf3
```

```
network 20.3.10.0 255.255.255.0
```

```
option 150 ip 20.3.10.1
```

```
default-router 20.3.10.1
```

```
class vrf3
```

```
address range 20.3.10.10 20.3.10.250
```

```
!
```

```
ip dhcp pool vrf4
```

```
network 20.4.10.0 255.255.255.0
```

```
default-router 20.4.10.1
```

```
option 150 ip 20.4.10.1
```

```
class vrf4
```

```
address range 20.4.10.10 20.4.10.250
```

```
!
```

```
ip dhcp pool vrf5
```

```
network 20.5.10.0 255.255.255.0
```

```
default-router 20.5.10.1
```

```
option 150 ip 20.5.10.1
```

```
class vrf5
```

```
address range 20.5.10.10 20.5.10.250
```

```
!
```

```
ip dhcp pool phone3
```

```
host 20.2.10.11 255.0.0.0
```

```
client-identifier 0100.0ed7.4ce6.3d
```

```
default-router 20.2.10.1
```

```
option 150 ip 20.2.10.1
```

```
!
```

```
ip dhcp pool phone4
```

```
host 20.3.10.11 255.0.0.0
```

```
client-identifier 0100.1280.55d3.cd
```

```
default-router 20.3.10.1
```

```
option 150 ip 20.3.10.1
```

```
!
```

```
ip dhcp pool subcme4
```

```
network 21.4.10.0 255.255.255.0
```

```
default-router 21.4.10.1
```

```
option 150 ip 21.4.10.1
```

```
class subcme4
```

```
address range 21.4.10.10 21.4.10.250
```

```
!
```

```
ip dhcp pool subcme5
```

```
network 21.5.10.0 255.255.255.0
```

```
default-router 21.5.10.1
```

```
option 150 ip 21.5.10.1
```

```
class subcme5
```

```
address range 21.5.10.10 21.5.10.250
```

```
!
```

```
ip dhcp pool subcme3
```

```
network 21.3.10.0 255.255.255.0
```

```
default-router 21.3.10.1
```

```
option 150 ip 21.3.10.1
```

```
class subcme3
```

```
address range 21.3.10.10 21.3.10.250
```

```
!
```

```
ip dhcp pool subcme2
```

```
network 21.2.10.0 255.255.255.0
```

```
default-router 21.2.10.1
```

```
option 150 ip 21.2.10.1
```

```
class subcme2
```

```
address range 21.2.10.10 21.2.10.250
```

```
!
```

```
ip dhcp pool subcme1
```

```
network 21.1.10.0 255.255.255.0
```

```
option 150 ip 21.1.10.1
```

```
default-router 21.1.10.1
```

```
class subcme1
```

```
address range 21.1.10.10 21.1.10.250
```

```
!
```

```
!
```

```
ip dhcp class vrf1
```

```
!
```

```
ip dhcp class vrf2
```

```
!
```

```
ip dhcp class vrf3
```

```
!
```

```
ip dhcp class vrf4
```

```
!
```

```
ip dhcp class vrf5
```

```
!
```

```
ip dhcp class subcme4
```

```
!
```

```
ip dhcp class subcme5
```

```
!
```

```
ip dhcp class subcme3
```

```
!
```

```
ip dhcp class subcme2
```

```
!
```

```
ip dhcp class subcme1
```

```
!
```

```
ip vrf service
```

```
rd 210:1
```

```
route-target export 210:1
```

```
route-target import 201:1
```

```
route-target import 202:1
```

```
route-target import 203:1
```

```
route-target import 204:1
```

```
route-target import 205:1
```

```
!
```

```
ip vrf vrf1
```

```
rd 201:1
```

```
route-target export 201:1
```

```
route-target import 201:1
```

```
route-target import 210:1
```

```
!
```

```
ip vrf vrf2
```

```
rd 202:1
```

```
route-target export 202:1
```

```
route-target import 202:1
```

```
route-target import 210:1
```

```
!
```

```
ip vrf vrf3
```

```
rd 203:1
```

```
route-target export 203:1
```

```
route-target import 203:1
```

```
route-target import 210:1
```

```
!
```

```
ip vrf vrf4
```

```
rd 204:1
```

```
route-target export 204:1
```

```
route-target import 204:1
```

```
route-target import 210:1
```

```
!
```

```
ip vrf vrf5
```

```
rd 205:1
```

```
route-target export 205:1
```

```
route-target import 205:1
```

```
route-target import 210:1
```

```
!
```

```
no ipv6 cef
```

```
multilink bundle-name authenticated
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
voice rtp send-recv
```

```
voice vrf vrf2
```

```
!
```

```
voice service voip
```

```
allow-connections h323 to h323
```

```
allow-connections h323 to sip
```

```
allow-connections sip to h323
```

```
allow-connections sip to sip
```

```
supplementary-service h450.12
```

```
h323
```

```
h225 timeout keepalive
```

```
sip
```

```
registrar server expires max 3600 min 3600
```

```
!
```

```
!
```

```
voice class codec 1
```

```
codec preference 1 g711ulaw
```

```
codec preference 2 g711alaw
```

```
codec preference 3 g729r8
```

```
!
```

```
!
```

```
!
```

```
!
```

```
!
```

```
archive
```

```
log config
```

```
hidekeys
```

```
!
```

```
!
```

```
controller T1 1/0/0
```

```
!
```

```
controller T1 1/0/1
```

```
!
```

```
ip ftp username Administrator
```

```
ip ftp password xxxx
```

```
!
```

```
!
```

```
interface Loopback201
```

```
ip vrf forwarding vrf1
```

```
ip address 21.1.0.1 255.255.255.255
```

```
!
```

```
interface Loopback202
```

```
ip vrf forwarding vrf2
```

```
ip address 21.2.0.1 255.255.255.255
```

```
!
```

```
interface Loopback203
```

```
ip vrf forwarding vrf3
```

```
ip address 21.3.0.1 255.255.255.255
```

```
!
```

```
interface Loopback204
```

```
ip vrf forwarding vrf4
```

```
ip address 21.4.0.1 255.255.255.255
```

```
!
```

```
interface Loopback205
```

```
ip vrf forwarding vrf5
```

```
ip address 21.5.0.1 255.255.255.255
```

```
!
```

```
interface GigabitEthernet0/0
```

```
no ip address
```

```
duplex auto
```

```
speed auto
```

```
no keepalive
```

```
!
```

```
interface GigabitEthernet0/0.301
```

```
encapsulation dot1Q 401
```

```
ip vrf forwarding vrf1
```

```
ip address 20.1.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/0.302
```

```
encapsulation dot1Q 402
```

```
ip vrf forwarding vrf2
```

```
ip address 20.2.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/0.303
```

```
encapsulation dot1Q 403
```

```
ip vrf forwarding vrf3
```

```
ip address 20.3.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/0.304
```

```
encapsulation dot1Q 404
```

```
ip vrf forwarding vrf4
```

```
ip address 20.4.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/0.305
```

```
encapsulation dot1Q 405
```

```
ip vrf forwarding vrf5
```

```
ip address 20.5.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/1
```

```
no ip address
```

```
duplex auto
```

```
speed auto
```

```
no keepalive
```

```
!
```

```
interface GigabitEthernet0/1.101
```

```
encapsulation dot1Q 201
```

```
ip vrf forwarding vrf1
```

```
ip address 21.1.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/1.102
```

```
encapsulation dot1Q 202
```

```
ip vrf forwarding vrf2
```

```
ip address 21.2.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/1.103
```

```
encapsulation dot1Q 203
```

```
ip vrf forwarding vrf3
```

```
ip address 21.3.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/1.104
```

```
encapsulation dot1Q 204
```

```
ip vrf forwarding vrf4
```

```
ip address 21.4.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/1.105
```

```
encapsulation dot1Q 205
```

```
ip vrf forwarding vrf5
```

```
ip address 21.5.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/1.209
```

```
encapsulation dot1Q 209
```

```
ip address 21.9.10.1 255.255.255.0
```

```
!
```

```
interface GigabitEthernet0/1.210
```

```
encapsulation dot1Q 210
```

```
ip vrf forwarding service
```

```
ip address 21.10.10.1 255.255.255.0
```

```
!
```

```
router ospf 201 vrf vrf1
```

```
log-adjacency-changes
```

```
network 20.1.0.0 0.0.255.255 area 0
```

```
network 21.1.0.1 0.0.0.0 area 0
```

```
network 21.0.0.0 0.255.255.255 area 0
```

```
!
```

```
router ospf 202 vrf vrf2
```

```
log-adjacency-changes
```

```
network 20.2.0.0 0.0.255.255 area 0
```

```
network 21.2.0.1 0.0.0.0 area 0
```

```
network 21.0.0.0 0.255.255.255 area 0
```

```
!
```

```
router ospf 203 vrf vrf3
```

```
log-adjacency-changes
```

```
network 20.3.0.0 0.0.255.255 area 0
```

```
network 21.3.0.1 0.0.0.0 area 0
```

```
network 21.0.0.0 0.255.255.255 area 0
```

```
!
```

```
router ospf 204 vrf vrf4
```

```
log-adjacency-changes
```

```
network 20.4.0.0 0.0.255.255 area 0
```

```
network 21.4.0.1 0.0.0.0 area 0
```

```
network 21.0.0.0 0.255.255.255 area 0
```

```
!
```

```
router ospf 205 vrf vrf5
```

```
log-adjacency-changes
```

```
network 20.5.0.0 0.0.255.255 area 0
```

```
network 21.5.0.1 0.0.0.0 area 0
```

```
network 21.0.0.0 0.255.255.255 area 0
```

```
!
```

```
router ospf 210 vrf service
```

```
log-adjacency-changes
```

```
redistribute bgp 100 metric-type 1 subnets
```

```
network 21.10.0.0 0.0.255.255 area 0
```

```
!
```

```
router ospf 209
```

```
log-adjacency-changes
```

```
network 21.9.0.0 0.0.255.255 area 0
```

```
!
```

```
router bgp 100
```

```
no synchronization
```

```
bgp router-id 28.21.0.0
```

```
bgp log-neighbor-changes
```

```
no auto-summary
```

```
!
```

```
address-family ipv4 vrf vrf5
```

```
redistribute connected
```

```
no synchronization
```

```
exit-address-family
```

```
!
```

```
address-family ipv4 vrf vrf4
```

```
redistribute connected
```

```
no synchronization
```

```
exit-address-family
```

```
!
```

```
address-family ipv4 vrf vrf3
```

```
redistribute connected
```

```
no synchronization
```

```
exit-address-family
```

```
!
```

```
address-family ipv4 vrf vrf2
```

```
redistribute connected
```

```
no synchronization
```

```
exit-address-family
```

```
!
```

```
address-family ipv4 vrf vrf1
```

```
redistribute connected
```

```
no synchronization
```

```
exit-address-family
```

```
!
```

```
address-family ipv4 vrf service
```

```
redistribute connected
```

```
no synchronization
```

```
exit-address-family
```

```
!
```

```
ip forward-protocol nd
```

```
ip route 223.255.254.254 255.255.255.255 2.8.0.1
```

```
!
```

```
!
```

```
ip http server
```

```
!
```

```
access-list 101 permit ip host 11.2.10.1 host 20.2.10.1
```

```
access-list 102 permit ip any host 223.255.254.254
```

```
access-list 103 permit ip any host 20.1.10.1
```

```
!
```

```
!
```

```
!
```

```
!
```

```
control-plane
```

```
!
```

```
!
```

```
!
```

```
ccm-manager fax protocol cisco
```

```
!
```

```
mgcp fax t38 ecm
```

```
!
```

```
!
```

```
dial-peer cor custom
```

```
name PSTN
```

```
name SIP
```

```
name H323
```

```
!
```

```
!
```

```
dial-peer cor list PSTN-TRUNK
```

```
member PSTN
```

```
!
```

```
dial-peer cor list SIP-TRUNK
```

```
member SIP
```

```
!
```

```
dial-peer cor list H323-TRUBK
```

```
member H323
```

```
!
```

```
dial-peer cor list user-sip
```

```
member SIP
```

```
!
```

```
dial-peer cor list user-pstn
```

```
member PSTN
```

```
!
```

```
dial-peer cor list user-h323
```

```
member H323
```

```
!
```

```
!
```

```
dial-peer voice 2821 pots
```

```
corlist outgoing PSTN-TRUNK
```

```
destination-pattern 70007
```

```
direct-inward-dial
```

```
forward-digits 10
```

```
!
```

```
dial-peer voice 2822 pots
```

```
corlist outgoing PSTN-TRUNK
```

```
destination-pattern 70017
```

```
direct-inward-dial
```

```
forward-digits 10
```

```
!
```

```
dial-peer voice 2823 voip
```

```
corlist outgoing H323-TRUBK
```

```
destination-pattern 70008
```

```
voice-class codec 1
```

```
session target ipv4:11.2.10.1
```

```
dtmf-relay h245-alphanumeric
```

```
!
```

```
dial-peer voice 2824 voip
```

```
corlist outgoing H323-TRUBK
```

```
destination-pattern 70018
```

```
voice-class codec 1
```

```
session target ipv4:11.2.10.1
```

```
dtmf-relay h245-alphanumeric
```

```
!
```

```
dial-peer voice 282145 voip
```

```
destination-pattern 70009
```

```
voice-class codec 1
```

```
session protocol sipv2
```

```
session target ipv4:11.2.10.1
```

```
dtmf-relay rtp-nte
```

```
no vad
```

```
!
```

```
dial-peer voice 282146 voip
```

```
destination-pattern 70019
```

```
voice-class codec 1
```

```
session protocol sipv2
```

```
session target ipv4:11.2.10.1
```

```
dtmf-relay rtp-nte
```

```
no vad
```

```
!
```

```
!
```

```
presence
```

```
presence call-list
```

```
watcher all
```

```
!
```

```
gateway
```

```
timer receive-rtp 1200
```

```
!
```

```
sip-ua
```

```
presence enable
```

```
!
```

```
!
```

```
telephony-service
```

```
sdspfarm conference mute-on # mute-off #
```

```
sdspfarm units 4
```

```
sdspfarm transcode sessions 10
```

```
sdspfarm tag 1 xcode101
```

```
sdspfarm tag 2 conf103
```

```
group  1 vrf vrf1
```

```
ip source-address 20.1.10.1 port 2000
```

```
!
```

```
group  2 vrf vrf2
```

```
ip source-address 20.2.10.1 port 2000
```

```
url directories http://20.2.10.1//localdirectory
```

```
!
```

```
group  3 vrf vrf3
```

```
ip source-address 20.3.10.1 port 2000
```

```
url directories http://20.3.10.1//localdirectory
```

```
!
```

```
group  4 vrf vrf4
```

```
ip source-address 20.4.10.1 port 2000
```

```
!
```

```
group  5 vrf vrf5
```

```
ip source-address 20.5.10.1 port 2000
```

```
!
```

```
conference hardware
```

```
no auto-reg-ephone
```

```
em logout 0:0 0:0 0:0
```

```
max-ephones 52
```

```
max-dn 192
```

```
auto assign 100 to 167 type 7960
```

```
auto assign 168 to 192 type anl
```

```
calling-number initiator
```

```
system message vcme 2821
```

```
time-zone 5
```

```
max-conferences 1 gain 6
```

```
call-park system redirect
```

```
call-forward pattern .T
```

```
call-forward system redirecting-expanded
```

```
moh music-on-hold.au
```

```
dn-webedit
```

```
time-webedit
```

```
transfer-system full-consult dss
```

```
transfer-pattern 9.T
```

```
secondary-dialtone 9
```

```
directory last-name-first
```

```
create cnf-files version-stamp 7960 Jun 09 2008 22:45:03
```

```
!
```

```
!
```

```
ephone-template  2
```

```
conference admin
```

```
group phone 2
```

```
!
```

```
!
```

```
ephone-template  3
```

```
conference admin
```

```
group phone 3
```

```
!
```

```
!
```

```
ephone-dn  132  dual-line
```

```
number 1001
```

```
label vrf1
```

```
name 1001
```

```
!
```

```
!
```

```
ephone-dn  152  dual-line
```

```
number 2001
```

```
label vrf2
```

```
name dc lin
```

```
allow watch
```

```
call-forward busy 2002
```

```
call-forward noan 3001 timeout 15
```

```
!
```

```
!
```

```
ephone-dn  153  dual-line
```

```
number 3001
```

```
label vrf3
```

```
name dd lin
```

```
allow watch
```

```
!
```

```
!
```

```
ephone-dn  186  dual-line
```

```
number 3333
```

```
conference ad-hoc
```

```
preference 5
```

```
!
```

```
!
```

```
ephone-dn  187  dual-line
```

```
number 3333
```

```
conference ad-hoc
```

```
preference 4
```

```
no huntstop
```

```
!
```

```
!
```

```
ephone-dn  188  dual-line
```

```
number 3333
```

```
conference ad-hoc
```

```
preference 3
```

```
no huntstop
```

```
!
```

```
!
```

```
ephone-dn  189  dual-line
```

```
number 3333
```

```
conference ad-hoc
```

```
preference 2
```

```
no huntstop
```

```
!
```

```
!
```

```
ephone-dn  190  dual-line
```

```
number 3099
```

```
label vrf3
```

```
description 3099
```

```
name 3099
```

```
conference ad-hoc
```

```
preference 1
```

```
no huntstop
```

```
!
```

```
!
```

```
ephone  132
```

```
mac-address 0018.BA14.B129
```

```
group phone 1
```

```
type 7941
```

```
button  1:132
```

```
!
```

```
!
```

```
!
```

```
ephone  152
```

```
mac-address 000E.D74C.E63D
```

```
ephone-template 2
```

```
type 7960
```

```
keep-conference endcall
```

```
button  1:152
```

```
!
```

```
!
```

```
!
```

```
ephone  153
```

```
video
```

```
mac-address 0012.8055.D3CD
```

```
ephone-template 3
```

```
type 7970
```

```
keep-conference endcall
```

```
button  1:153
```

```
!
```

```
!
```

```
!
```

```
ephone  231
```

```
mac-address 000B.5FC2.2C23
```

```
group phone 1
```

```
type 7940
```

```
keep-conference
```

```
!
```

```
!
```

```
!
```

```
ephone  232
```

```
mac-address 0017.95B0.44C7
```

```
group phone 1
```

```
type 7960
```

```
keep-conference
```

```
!
```

```
!
```

```
!
```

```
ephone  233
```

```
mac-address 000E.D748.5DE3
```

```
group phone 3
```

```
type 7960
```

```
keep-conference
```

```
!
```

```
!
```

```
!
```

```
line con 0
```

```
exec-timeout 0 0
```

```
line aux 0
```

```
line vty 0 4
```

```
exec-timeout 0 0
```

```
password xxxx
```

```
login
```

```
!
```

```
exception protocol ftp
```

```
exception dump 9.20.20.253
```

```
exception data-corruption buffer truncate
```

```
scheduler allocate 20000 1000
```

```
end
```

```
Router#
```

### Configuring Cisco Unity Express for Cisco Unified CME Voice Mail

The followings are required for defining Cisco Unity Express with VRF awareness Cisco Unified CME:

• Telnet is used to access Cisco Unity Express, not the "Service-Engine Service-Engine 1/0 session" which is for non-VRF awareness Cisco Unified CME commands. Access the Cisco Unity Express module for defining Cisco Unity Express users with "voice vrf vrf2" telnet 21.10.10.5 2066 /vrf vrf2

• One IP address is required for "interface service engine," used to assign the interface to "voice vrf."

The example is for configuring Cisco Unity Express for Cisco Unified CME Voice Mail.

```
voice vrf vrf2
```

```
....
```

```
ip vrf vrf2
```

```
rd 100:2
```

```
route-target export 100:2
```

```
route-target import 100:2
```

```
.....
```

```
interface GigabitEthernet0/1.210
```

```
encapsulation dot1Q 210
```

```
ip address 21.10.10.2 255.255.255.0
```

```
!
```

```
......
```

```
interface Service-Engine1/0
```

```
ip vrf forwarding vrf2
```

```
ip address 21.10.10.5 255.255.255.0
```

```
service-module ip address 21.10.10.6 255.255.255.0
```

```
service-module ip default-gateway 21.10.10.2
```

```
!
```

```
......
```

```
line 66
```

```
no activation-character
```

```
no exec
```

```
transport preferred none
```

```
transport input all
```

```
transport output pad telnet rlogin lapb-ta mop udptn v120
```

### Configuring Cisco Unified CME and DSP Farm on the Same Box for Conference, Transcoder, and Media Termination Point

```
interface Loopback5
```

```
ip address 12.5.10.1 255.255.255.255
```

```
!
```

```
......
```

```
sccp local Loopback5
```

```
sccp ccm 12.5.10.1 identifier 2 version 4.1
```

```
sccp
```

```
!
```

```
sccp ccm group 2
```

```
bind interface Loopback5
```

```
associate ccm 2 priority 1
```

```
associate profile 103 register conf103
```

```
associate profile 101 register xcode101
```

```
!
```

```
dspfarm profile 101 transcode
```

```
codec g711ulaw
```

```
codec g711alaw
```

```
codec g729ar8
```

```
codec g729abr8
```

```
codec g729r8
```

```
maximum sessions 1
```

```
associate application SCCP
```

```
!
```

```
dspfarm profile 103 conference
```

```
codec g711ulaw
```

```
codec g711alaw
```

```
codec g729ar8
```

```
codec g729abr8
```

```
codec g729r8
```

```
codec g729br8
```

```
maximum sessions 1
```

```
associate application SCCP
```

```
.....
```

```
telephony-service
```

```
sdspfarm conference mute-on # mute-off #
```

```
sdspfarm units 4
```

```
sdspfarm transcode sessions 10
```

```
sdspfarm tag 1 xcode101
```

```
sdspfarm tag 2 conf103
```

```
group  1 vrf vrf1
```

```
ip source-address 10.1.10.1 port 2000
```

```
!
```

```
group  2 vrf vrf2
```

```
ip source-address 10.2.10.1 port 2000
```

```
!
```

```
group  3 vrf vrf3
```

```
ip source-address 10.3.10.1 port 2000
```

```
!
```

```
group  4 vrf vrf4
```

```
ip source-address 10.4.10.1 port 2000
```

```
!
```

```
group  5
```

```
ip source-address 12.5.10.1 port 2000
```

```
!
```

```
conference hardware
```

```
load 7941 SCCP41.8-3-3-13S
```

```
load 7970 SCCP70.8-3-3-13S
```

```
max-ephones 240
```

```
max-dn 480
```

```
auto assign 1 to 100 type 7960
```

```
auto assign 204 to 230
```

```
calling-number initiator
```

```
system message vcme3845
```

```
time-zone 5
```

```
voicemail 7710
```

```
max-conferences 8 gain -6
```

```
call-forward pattern .T
```

```
call-forward system redirecting-expanded
```

```
moh music-on-hold.au
```

```
web admin system name cisco secret 5 $1$S04p$HfTwkOyOYAa8zU2pANKqg/
```

```
dn-webedit
```

```
time-webedit
```

```
transfer-system full-consult dss
```

```
transfer-pattern 9.T
```

```
secondary-dialtone 9
```

```
create cnf-files version-stamp 7960 Feb 16 2008 22:45:55
```

```
!
```

### Configuring Cisco Unified CME and DSP Farm on the Different Boxes for Conference, Transcoder, and Media Termination Point

There are no changes to defining the DSP farm. Do make sure that the DSP farm messages and flows are coming through the interface and subinterface defined as "voice VRF" interface and subinterface.

The following example has the DSP farm defined on another box.

```
interface FastEthernet0/0.202
```

```
encapsulation dot1Q 202
```

```
ip address 21.2.10.2 255.255.255.0
```

```
!
```

```
........
```

```
sccp local FastEthernet0/0.202
```

```
sccp ccm 20.2.10.1 identifier 2 version 4.0
```

```
sccp
```

```
!
```

```
sccp ccm group 2
```

```
associate ccm 2 priority 1
```

```
associate profile 103 register conf103
```

```
associate profile 101 register xcode101
```

```
!
```

```
dspfarm profile 101 transcode
```

```
codec g711ulaw
```

```
codec g711alaw
```

```
codec g729r8
```

```
maximum sessions 1
```

```
associate application SCCP
```

```
shutdown
```

```
!
```

```
dspfarm profile 103 conference
```

```
codec g711ulaw
```

```
codec g711alaw
```

```
codec g729ar8
```

```
codec g729abr8
```

```
codec g729r8
```

```
codec g729br8
```

```
maximum sessions 1
```

```
associate application SCCP
```

```
!
```

## Verification

This section shows configuration verification commands.

```
show ip vrf interface
```

```
router#show ip vrf interface 
Interface  IP-Address  VRF    Protocol 
Lo101      11.1.0.1    vcme1  up  
Gi0/0.301  10.1.10.1   vcme1  up  
Gi0/1.101  11.1.10.1   vcme1  up  
Lo102      11.2.0.1    vcme2  up  
Gi0/0.302  10.2.10.1   vcme2  up  
Gi0/1.102  11.2.10.1   vcme2  up  
Se1/0      21.10.10.5  vcme2  up  
Lo103      11.3.0.1    vcme3  up  
Gi0/0.303  10.3.10.1   vcme3  up  
Gi0/1.103  11.3.10.1   vcme3  up  
Lo104      11.4.0.1    vcme4  up  
Gi0/0.304  10.4.10.1   vcme4  up
```

```
show ip vrf interface vcme2
```

```
router#show ip vrf interface vcme2 
Interface  IP-Address  VRF    Protocol 
Lo102      11.2.0.1    vcme2  up  
Gi0/0.302  10.2.10.1   vcme2  up  
Gi0/1.102  11.2.10.1   vcme2  up  
Se1/0      21.10.10.5  vcme2  up  
router#
```

```
show ip vrf detail Csco3845_1
```

```
router#show ip vrf detail
```

```
VRF vcme1; default RD 100:1; default VPNID <not set> 
Interfaces: 
Lo101 Gi0/0.301 Gi0/1.101  
VRF Table ID = 1 
Export VPN route-target communities 
RT:100:1  
Import VPN route-target communities 
RT:100:1  
No import route-map 
No export route-map 
VRF label distribution protocol: not configured 
VRF label allocation mode: per-prefix
```

```
VRF vcme2; default RD 100:2; default VPNID <not set> 
Interfaces: 
Lo102 Gi0/0.302 Gi0/1.102  
Se1/0  
VRF Table ID = 2 
Export VPN route-target communities 
RT:100:2  
Import VPN route-target communities 
RT:100:2  
No import route-map
```

```
show sccp all Csco3845_1
```

```
router#show sccp all
```

```
SCCP Admin State: UP 
Gateway IP Address: 12.5.10.1, Port Number: 2000 
IP Precedence: 5 
User Masked Codec list: None 
Call Manager: 12.5.10.1, Port Number: 2000 
Priority: N/A, Version: 4.1, Identifier: 2 
Trustpoint: N/A
```

```
Transcoding Oper State: ACTIVE - Cause Code: NONE 
Active Call Manager: 12.5.10.1, Port Number: 2000 
TCP Link Status: CONNECTED, Profile Identifier: 101 
Reported Max Streams: 2, Reported Max OOS Streams: 0 
Supported Codec: g711ulaw, Maximum Packetization Period: 30 
Supported Codec: g711alaw, Maximum Packetization Period: 30 
Supported Codec: g729ar8, Maximum Packetization Period: 60 
Supported Codec: g729abr8, Maximum Packetization Period: 60 
Supported Codec: g729r8, Maximum Packetization Period: 60 
Supported Codec: rfc2833 dtmf, Maximum Packetization Period: 30 
Supported Codec: rfc2833 pass-thru, Maximum Packetization Period: 30 
Supported Codec: inband-dtmf to rfc2833 conversion, Maximum Packetization Period: 30
```

```
Conferencing Oper State: ACTIVE - Cause Code: NONE 
--More--
```

```
show sccp connection Csco3845_1
```

```
router#show sccp connection
```

```
sess_id conn_id stype mode codec ripaddr rport sport
```

```
-1073676287 131075 conf sendrecv g711u 12.5.10.1 2000 18214 
-1073676287 131074 conf sendrecv g711u 12.5.10.1 2000 19226 
-1073676287 131073 conf sendrecv g711u 12.5.10.1 2000 18170
```

```
Total number of active session(s) 1, and connection(s) 3 
6) show ip route vrf vcme2 Csco3845_1#show ip route vrf vcme2
```

```
Routing Table: vcme2 
Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP 
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area  
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2 
E1 - OSPF external type 1, E2 - OSPF external type 2 
i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2 
ia - IS-IS inter area, * - candidate default, U - per-user static route 
o - ODR, P - periodic downloaded static route
```

```
Gateway of last resort is not set
```

```
O E2 223.255.254.0/24 [110/20] via 11.2.10.2, 18:31:10, GigabitEthernet0/1.102 
21.0.0.0/8 is variably subnetted, 3 subnets, 2 masks 
C 21.10.10.0/24 is directly connected, Service-Engine1/0 
O 21.2.0.1/32 [110/3] via 11.2.10.2, 18:31:10, GigabitEthernet0/1.102 
O 21.2.10.0/24 [110/2] via 11.2.10.2, 18:31:10, GigabitEthernet0/1.102 
20.0.0.0/24 is subnetted, 1 subnets 
O 20.2.10.0 [110/3] via 11.2.10.2, 18:31:10, GigabitEthernet0/1.102 
10.0.0.0/24 is subnetted, 1 subnets 
C 10.2.10.0 is directly connected, GigabitEthernet0/0.302 
11.0.0.0/8 is variably subnetted, 2 subnets, 2 masks 
C 11.2.10.0/24 is directly connected, GigabitEthernet0/1.102
```

```
show ip ospf neighbor Csco3845_1
```

```
router#show ip ospf neighbor
```

```
Neighbor   ID Pri State Dead Time Address     Interface 
21.10.10.1 1  FULL/DR   00:00:31  21.10.10.1  GigabitEthernet0/1.210 
21.1.10.2  1  FULL/DR   00:00:39  11.9.10.2   GigabitEthernet0/1.109 
21.4.10.2  1  FULL/DR   00:00:38  11.5.10.2   GigabitEthernet0/1.105 
21.5.10.2  1  FULL/DR   00:00:38  11.4.10.2   GigabitEthernet0/1.104 
21.9.10.2  1  FULL/DR   00:00:38  11.3.10.2   GigabitEthernet0/1.103 
21.3.10.2  1  FULL/DR   00:00:39  11.2.10.2   GigabitEthernet0/1.102 
21.2.10.2  1  FULL/DR   00:00:39  11.1.10.3   GigabitEthernet0/1.101 8) 
show dspfarm dsp active Csco3845_1#show dspfarm dsp active 
SLOT DSP VERSION STATUS CHNL USE TYPE RSC_ID BRIDGE_ID PKTS_TXED PKTS_RXED
```

```
0 2 22.3.0 UP 1 USED conf 2 0x7 34665 34658  
0 2 22.3.0 UP 1 USED conf 2 0x9 34664 34651  
0 2 22.3.0 UP 1 USED conf 2 0xB 34662 34640
```

```
Total number of DSPFARM DSP channel(s) 1
```

```
show voice dsp voice Csco3845_1
```

```
router#show voice dsp voice
```

```
DSP DSP DSPWARE CURR BOOT PAK TX/RX 
TYPE NUM CH CODEC    VERSION    STATE STATE   RST AI VOICEPORT TS ABORT PACK COUNT 
==== === == ======== ========== ===== ======= === == ========= == ===== ============ 
edsp 001 01 g729r8 p 0.1 IDLE 50/0/186.1  
edsp 002 02 g729r8 p 0.1 IDLE 50/0/186.2  
edsp 003 01 g729r8 p 0.1 IDLE 50/0/187.1  
edsp 004 02 g729r8 p 0.1 IDLE 50/0/187.2  
edsp 005 01 g729r8 p 0.1 IDLE 50/0/188.1  
edsp 006 02 g729r8 p 0.1 IDLE 50/0/188.2  
edsp 007 01 g711ulaw 0.1 busy 50/0/189.1  
edsp 008 02 g729r8 p 0.1 IDLE 50/0/189.2  
edsp 009 01 g711ulaw 0.1 busy 50/0/190.1  
edsp 010 02 g711ulaw 0.1 busy 50/0/190.2  
edsp 011 01 g729r8 p 0.1 IDLE 50/0/197.1  
edsp 012 02 g729r8 p 0.1 IDLE 50/0/197.2
```

```
show telephony-service conference hardware detail Csco3845_1
```

```
router#show telephony-service conference hardware detail
```

```
Conference Type Active Max Peak Master MasterPhone Last 
cur(initial)  
======================================================================================= 
3333 Ad-hoc 3 8 3 3099 3099 233 (233) 1098 1098  
Conference parties (number:phone) 
1098 1098:232  
2099 2099:231  
3099 3099:233
```

```
debug tftp events Csco3845_1#
```

```
TFTP: Looking for CTLSEP000ED7485DE3.tlv 
TFTP: Looking for CTLSEP000ED7485DE3.tlv
```

```
debug tftp packets TFTP: Server request for port 50919, socket_id 0x71523394 for process 
334
```

```
TFTP: read request from host 10.2.10.11(50919) via GigabitEthernet0/0.302 
TFTP: Looking for CTLSEP000B5FC22C23.tlv 
TFTP: Sending error 1 No such file 
TFTP: Server request for port 49785, socket_id 0x71523394 for process 334 
TFTP: read request from host 10.3.10.10(49785) via GigabitEthernet0/0.303 
TFTP: Looking for CTLSEP000ED7485DE3.tlv 
TFTP: Sending error 1 No such file
```

```
debug sccp message
```

```
Csco3845_1(config)# 
SCCP operational state bring up is successful. 
SCCP:send RegisterMessage, protocol_ver=0xA000000 
SCCP:send IpPortMessage 
SCCP:send MediaResourceNotification 
SCCP:send RegisterMessage, protocol_ver=0xA000000 
SCCP:send IpPortMessage 
SCCP:send MediaResourceNotification 
%SDSPFARM-6-REGISTER: mtp-1:xcode101 IP:12.5.10.1 Socket:1 DeviceType:MTP has registered. 
%HWCONF-6-REGISTER: hwconf-2:conf103 IP:12.5.10.1 Socket:2 DeviceType:HW Conference has 
registered. 
SCCP:rcvd RegisterAckMessage 
SCCP:keepaalive interval=30, agreed_sccp_ver=10 
SCCP:send MediaResourceNotification 
SCCP:send VersionReqMessage 
SCCP:rcvd RegisterAckMessage 
SCCP:keepaalive interval=30, agreed_sccp_ver=10 
SCCP:send MediaResourceNotification 
SCCP:send VersionReqMessage 
SCCP:rcvd CapabilitiesReqMessage 
SCCP:send CapabilitiesResMessage 
SCCP:rcvd CapabilitiesReqMessage 
SCCP:send CapabilitiesResMessage 
SCCP:rcvd VersionMessage 
VersionMsg Info:  
version:  
SCCP:rcvd VersionMessage 
VersionMsg Info:  
version:
```

### CCDE, CCENT, Cisco Eos, Cisco Lumin, Cisco Nexus, Cisco StadiumVision, Cisco TelePresence, Cisco WebEx, the Cisco logo, DCE, and Welcome to the Human Network are trademarks; Changing the Way We Work, Live, Play, and Learn and Cisco Store are service marks; and Access Registrar, Aironet, AsyncOS, Bringing the Meeting To You, Catalyst, CCDA, CCDP, CCIE, CCIP, CCNA, CCNP, CCSP, CCVP, Cisco, the Cisco Certified Internetwork Expert logo, Cisco IOS, Cisco Press, Cisco Systems, Cisco Systems Capital, the Cisco Systems logo, Cisco Unity, Collaboration Without Limitation, EtherFast, EtherSwitch, Event Center, Fast Step, Follow Me Browsing, FormShare, GigaDrive, HomeLink, Internet Quotient, IOS, iPhone, iQuick Study, IronPort, the IronPort logo, LightStream, Linksys, MediaTone, MeetingPlace, MeetingPlace Chime Sound, MGX, Networkers, Networking Academy, Network Registrar, PCNow, PIX, PowerPanels, ProConnect, ScriptShare, SenderBase, SMARTnet, Spectrum Expert, StackWise, The Fastest Way to Increase Your Internet Quotient, TransPath, WebEx, and the WebEx logo are registered trademarks of Cisco Systems, Inc. and/or its affiliates in the United States and certain other countries.

### All other trademarks mentioned in this document or website are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (0809R)

### Any Internet Protocol (IP) addresses used in this document are not intended to be actual addresses. Any examples, command display output, and figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses in illustrative content is unintentional and coincidental. © 2008 Cisco Systems, Inc. All rights reserved.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. • Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | ip vrf vrfname Example: Router(config)# ip vrf vrf1 | Defines a Virtual Private Network (VPN) routing/forwarding (VRF) instance and enters VRF configuration mode. • vrfname —Identifier for the VRF. |
| Step 4 | rd route-distinguisher Example: Router(config-vrf)# rd 1:1 | Creates a routing and forwarding table for a VPN VRF. • route-distinguisher —Adds an 8-byte value to an IPv4 prefix to create a VPN IPv4 prefix. |
| Step 5 | route-target {import \| export \| both} route-target-ext-community Example: Router(config-vrf)# route-target export 1:2 | Creates a list of import or export route target communities for the specified VRF. • import —Imports routing information from the target VPN extended community. • export —Exports routing information to the target VPN extended community. • both —Imports both import and export routing information to the target VPN extended community. • route-target-ext-community —Adds the route-target extended community attributes to the VRF's list of import, export, or both (import and export) route-target extended communities. |
| Step 6 | exit Example: Router(config-vrf)# exit | Exits VRF configuration mode. |
| Step 7 | voice service voip Example: Router(config)# voice service voip | Enters voice-service configuration mode. |
| Step 8 | shutdown Example: Router(config-voi-serv)# shutdown | Shuts down voice services. |
| Step 9 | exit Example: Router(config-voi-serv)# exit | Exits voice-service configuration mode. |
| Step 10 | voice vrf name Example: Router(config)# voice vrf vrf1 | Assigns a predefined VRF to voice services. • vrfname —Identifier for the VRF. |
| Step 11 | voice service voip Example: Router(config)# voice service voip | Enters voice-service configuration mode. |
| Step 12 | no shutdown Example: Router(config-voi-serv)# no shutdown | Restarts voice services. |
| Step 13 | end Example: Router(config-voi-serv)# end | Returns to privileged EXEC mode. |