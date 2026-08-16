---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-multicast-moh-html-9abcf0dcbf
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-multicast-moh.html
retrieved_at: 2026-08-16T15:51:32.323862+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Multicast Music-on-Hold Support on Cisco UBE

## Chapter: Multicast Music-on-Hold Support on Cisco UBE

# Multicast Music-on-Hold Support on Cisco UBE

The Multicast Music-on-Hold (MMOH) feature enables you to subscribe to a music streaming service when you are using a Cisco
                        Unified Border Element. Music streams from an MMOH server to the interface of Cisco UBE, which then converts it into unicast.
                        To play the MMOH to customers using Cisco UBE, you must enable the MMOH feature on Cisco UBE.

## Feature Information for
                        	 Multicast Music-on-Hold Support on Cisco UBE

The following table
                              		  provides release information about the feature or features described in this
                              		  module. This table lists only the software release that introduced support for
                              		  a given feature in a given software release train. Unless noted otherwise,
                              		  subsequent releases of that software release train also support that feature.

Use Cisco Feature Navigator to find information about platform support and software image support. Cisco Feature Navigator
                              enables you to determine which software images support a specific software release, feature set, or platform. To access Cisco
                              Feature Navigator, go to http://www.cisco.com/go/cfn . An account on Cisco.com is not required.

Feature
                                          					 Name

Releases

Feature
                                          					 Information

Multicast Music-on-Hold Support on Cisco UBE

Baseline Functionality

The Multicast Music-on-Hold (MMOH) feature enables you to subscribe to a music streaming service when you are using a Cisco
                                          Unified Border Element. To play MMOH to customers using Cisco UBE, you must enable the MMOH feature on Cisco UBE.

## Restrictions for Multicast
                        	 Music-on-Hold Support on Cisco UBE

The Multicast
                                 			 Music-on-Hold (MMOH) feature will not work when the Session Description
                                 			 Protocol (SDP) Passthrough feature is enabled on Cisco UBE.

The MMOH feature
                                 			 will work for Low Density Transcoded calls but not for High Density Transcoded
                                 			 calls.

MMOH is supported
                                 			 only on SIP-to-SIP call flows on Cisco UBE.

MMOH with RTCP is not supported.

MMOH is not supported for SRTP trunk.

MMOH with media flow-around is not supported.

## Information About Multicast Music-on-Hold Support onCisco UBE

### Multicast Music-on-Hold

To play Multicast Music-on-Hold (MMOH) to customers using Cisco UBE, you must enable the MMOH feature on Cisco UBE. When Cisco
                              UBE receives an MMOH call, it converts the multicast address received on the inbound leg into a unicast address and sends
                              the address on the outbound leg.

Cisco UBE uses preconfigured CLIs to "listen" for Real-Time Transport Protocol (RTP) packets that are broadcast from an MMOH
                              server in the network and converts them to unicast. When a call is placed on hold, the MOH server streams the RTP packets
                              to the Cisco UBE interface. This interface converts the RTP packets to unicast and relays the packets to the appropriate voice
                              interfaces that have been placed on hold.

MMOH is already supported on SIP-TDM gateways.

## How to Enable Multicast Music-on-Hold on Cisco UBE

### Enable MMOH on Cisco UBE

Perform this task to enable the MMOH feature on Cisco UBE.

### SUMMARY STEPS

- enable

- configure terminal

- ip multicast-routing distributed

- interface gigabitethernet router-shelf/slot/port

- ip address ip-address subnet-mask

- ip pim dense-mode

- negotiation auto

- exit

- ccm-manager music-on-hold

- exit

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables
                                             				privileged EXEC mode.

Enter your
                                                   					 password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ip multicast-routing distributed

#### Example:

```
Device(config)# ip multicast-routing distributed
```

Enables
                                             				distributed IP multicast routing.

Step 4

interface gigabitethernet router-shelf/slot/port

#### Example:

```
Device(config)# interface gigabitethernet 0/0/0
```

Configures a Gigabit Ethernet interface and enters interface
                                             				configuration mode.

Step 5

ip address ip-address subnet-mask

#### Example:

```
Device(config-if)# ip address 9.40.1.140 255.255.0.0
```

Configures the IP address and the subnet mask on the interface.

Step 6

ip pim dense-mode

#### Example:

```
Device(config-if)# ip pim dense-mode
```

Enables protocol-independent multicast (PIM) dense-mode operation.

Step 7

negotiation auto

#### Example:

```
Device(config-if)# negotiation auto
```

Performs link auto-negotiation.

Step 8

exit

#### Example:

```
Device(config-if)# exit
```

Exits interface configuration mode.

Step 9

ccm-manager music-on-hold

#### Example:

```
Device(config)# ccm-manager music-on-hold
```

Enables the
                                             				multicast music-on-hold feature on a voice gateway.

Step 10

exit

#### Example:

```
Device(config)# exit
```

Exits global
                                             				configuration mode and enters privileged EXEC mode.

### Verify the MMOH Support on Cisco UBE

Perform this task to verify the MMOH support on Cisco UBE. The show commands can be entered in any order.

### SUMMARY STEPS

- enable

- show ccm-manager music-on-hold

- show voip rtp connections

- show call active voice compact

- show platform hardware qfp active feature sbc mmoh
                                       				  global

- show platform hardware qfp active feature sbc mmoh group

### DETAILED STEPS

Step 1

enable

Enables
                                             				privileged EXEC mode.

#### Example:

```
Device> enable
```

Step 2

show ccm-manager music-on-hold

Displays
                                             				information about all the multicast music-on-hold (MOH) sessions in the gateway
                                             				at any given time.

#### Example:

```
Device# show ccm-manager music-on-hold Current active multicast sessions: 1
Multicast Address   RTP port number    Packets in/out    CallId   Codec    Incoming Interface
239.1.1.1           16386              614/614           132     g711ulaw
Gi0/0
```

Step 3

show voip rtp connections

Displays
                                             				RTP-named event packets.

#### Example:

```
Device# show voip rtp connections VoIP RTP Port Usage Information:
Max Ports Available: 20000, Ports Reserved: 101, Ports in Use: 2
Port range not configured, Min: 8000, Max: 48200
	Ports       Ports       Ports     
Media-Address Range                     	Available   Reserved    In-use    
Default Address-Range                   	20000       101         2 

VoIP RTP active connections:
No. CallId     dstCallId       LocalRTP RmtRTP     LocalIP                                RemoteIP
1     140        141            18792    18638     9.42.30.10                             9.42.30.32
2     141        140            19256    26184     9.42.30.10                             9.42.30.189
Found 2 active RTP sessions
```

Step 4

show call active voice compact

Displays a
                                             				compact version of voice calls in progress.

#### Example:

```
Device# show call active voice compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 3
       140 ANS     T644   g711ulaw    VOIP        P10000       9.42.30.32:18638
       141 ORG     T644   g711ulaw    VOIP        P708090      9.42.30.189:26184
       145 ORG     T643   g711ulaw    VOIP        P595959      9.42.29.7:3852
```

Step 5

show platform hardware qfp active feature sbc mmoh
                                                				  global

Displays SBC multicast Music-on-Hold global statistics.

#### Example:

```
Device# show platform hardware qfp active feature sbc mmoh global SBC multicast Music-on-Hold Global Statistics
------------------------------------------------------------------
 Total MMOH groups                           = 1
 Total RTP packets received                  = 6311
 Total RTP octects received                  = 1262200
 Total RTP packets replicated                = 6311
 Total RTP octects replicated                = 1262200
 Total RTP packets dropped                   = 0
 Total RTP octects dropped                   = 0
```

Step 6

show platform hardware qfp active feature sbc mmoh group

Displays SBC multicast Music-on-Hold group structure.

#### Example:

```
Device# show platform hardware qfp active feature sbc mmoh group SBC multicast Music-on-Hold group structure:
---------------------------------------
 VRF                                   = 0
 IP                                    = 239.1.1.1
 Port                                  = 16384
 Protocol                              = 1
 Calls in group                        = 1
 
SBC MMOH group Statistics
---------------------------------------
  Total RTP packets received                  = 406
  Total RTP octects received                  = 81200
  Total RTP packets replicated                = 406
  Total RTP octects replicated                = 81200
  Total RTP packets dropped                   = 0
  Total RTP octects dropped                   = 0
```

### Troubleshooting Tips

The following commands can help troubleshoot MMOH:

debug ccm-manager music-on-hold [ all | errors | events ]

debug voip rtp

debug ccsip all

## Configuration Examples for Multicast Music-on-Hold Support on Cisco UBE

### Example: Enabling MMOH on
                           	 Cisco UBE

```
Device> enable Device# configure terminal Device(config)# ip multicast-routing distributed Device(config)# interface gigabitethernet 0/0/0 Device(config-if)# ip address 9.40.1.140 255.255.0.0 Device(config-if)# ip pim dense-mode Device(config-if)# negotiation auto Device(config-if)# exit Device(config)# ccm-manager music-on-hold Device# show running-config Building configuration...
Current configuration : 2375 bytes
!
! Last configuration change at 11:01:36 UTC Wed Jan 5 2011
!
version 15.1
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname carbon-1
!
boot-start-marker
boot system flash usbflash0:c2951-universalk9-mz.SSA.MMOH-carbon_dev
boot-end-marker
!
!
!
no aaa new-model
!
no ipv6 cef
ip source-route
ip cef
!
!
!
ip multicast-routing
!
!
no ip domain lookup
multilink bundle-name authenticated
!
!
!
!
!
crypto pki token default removal timeout 0
!
!
voice-card 0
!
!
!
voice service voip
 mode border-element license capacity 1200
 allow-connections sip to sip
 sip
!
!
!
!
!
license udi pid CISCO2951/K9 sn FHK1433F39H
hw-module pvdm 0/0
!
!
!
!
redundancy inter-device
!
!
redundancy
!
!
!
!
!
!
interface GigabitEthernet0/0
 ip address 9.42.30.12 255.255.0.0
 duplex auto
 speed auto
!
interface GigabitEthernet0/1
no ip address
 shutdown
 duplex auto
 speed auto
!
interface GigabitEthernet0/2
 no ip address
 shutdown
 duplex auto
 speed auto
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
ip route 0.0.0.0 0.0.0.0 9.42.0.1
!
!
nls resp-timeout 1
cpd cr-id 1
!
!
control-plane
!
!
ccm-manager music-on-hold
!
!
mgcp profile default
!
!
dial-peer voice 100 voip
 destination-pattern 878767
 session protocol sipv2
 session target ipv4:9.42.30.5
 codec g711ulaw
!
gatekeeper
 shutdown
!
!
!
line con 0
 speed 115200
line aux 0
line vty 0 4
 login
 transport input all
!
exception data-corruption buffer truncate
scheduler allocate 20000 1000
end
```

| Feature
                                          					 Name | Releases | Feature
                                          					 Information |
|---|---|---|
| Multicast Music-on-Hold Support on Cisco UBE | Baseline Functionality | The Multicast Music-on-Hold (MMOH) feature enables you to subscribe to a music streaming service when you are using a Cisco
                                          Unified Border Element. To play MMOH to customers using Cisco UBE, you must enable the MMOH feature on Cisco UBE. |

| Note | MMOH is already supported on SIP-TDM gateways. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ip multicast-routing distributed Example: Device(config)# ip multicast-routing distributed | Enables
                                             				distributed IP multicast routing. |
| Step 4 | interface gigabitethernet router-shelf/slot/port Example: Device(config)# interface gigabitethernet 0/0/0 | Configures a Gigabit Ethernet interface and enters interface
                                             				configuration mode. |
| Step 5 | ip address ip-address subnet-mask Example: Device(config-if)# ip address 9.40.1.140 255.255.0.0 | Configures the IP address and the subnet mask on the interface. |
| Step 6 | ip pim dense-mode Example: Device(config-if)# ip pim dense-mode | Enables protocol-independent multicast (PIM) dense-mode operation. |
| Step 7 | negotiation auto Example: Device(config-if)# negotiation auto | Performs link auto-negotiation. |
| Step 8 | exit Example: Device(config-if)# exit | Exits interface configuration mode. |
| Step 9 | ccm-manager music-on-hold Example: Device(config)# ccm-manager music-on-hold | Enables the
                                             				multicast music-on-hold feature on a voice gateway. |
| Step 10 | exit Example: Device(config)# exit | Exits global
                                             				configuration mode and enters privileged EXEC mode. |

| Step 1 | enable Enables
                                             				privileged EXEC mode. Example: Device> enable |
|---|---|
| Step 2 | show ccm-manager music-on-hold Displays
                                             				information about all the multicast music-on-hold (MOH) sessions in the gateway
                                             				at any given time. Example: Device# show ccm-manager music-on-hold Current active multicast sessions: 1
Multicast Address   RTP port number    Packets in/out    CallId   Codec    Incoming Interface
239.1.1.1           16386              614/614           132     g711ulaw
Gi0/0 |
| Step 3 | show voip rtp connections Displays
                                             				RTP-named event packets. Example: Device# show voip rtp connections VoIP RTP Port Usage Information:
Max Ports Available: 20000, Ports Reserved: 101, Ports in Use: 2
Port range not configured, Min: 8000, Max: 48200
	Ports       Ports       Ports     
Media-Address Range                     	Available   Reserved    In-use    
Default Address-Range                   	20000       101         2 

VoIP RTP active connections:
No. CallId     dstCallId       LocalRTP RmtRTP     LocalIP                                RemoteIP
1     140        141            18792    18638     9.42.30.10                             9.42.30.32
2     141        140            19256    26184     9.42.30.10                             9.42.30.189
Found 2 active RTP sessions |
| Step 4 | show call active voice compact Displays a
                                             				compact version of voice calls in progress. Example: Device# show call active voice compact <callID>  A/O FAX T<sec> Codec       type        Peer Address       IP R<ip>:<udp>
Total call-legs: 3
       140 ANS     T644   g711ulaw    VOIP        P10000       9.42.30.32:18638
       141 ORG     T644   g711ulaw    VOIP        P708090      9.42.30.189:26184
       145 ORG     T643   g711ulaw    VOIP        P595959      9.42.29.7:3852 |
| Step 5 | show platform hardware qfp active feature sbc mmoh
                                                				  global Displays SBC multicast Music-on-Hold global statistics. Example: Device# show platform hardware qfp active feature sbc mmoh global SBC multicast Music-on-Hold Global Statistics
------------------------------------------------------------------
 Total MMOH groups                           = 1
 Total RTP packets received                  = 6311
 Total RTP octects received                  = 1262200
 Total RTP packets replicated                = 6311
 Total RTP octects replicated                = 1262200
 Total RTP packets dropped                   = 0
 Total RTP octects dropped                   = 0 |
| Step 6 | show platform hardware qfp active feature sbc mmoh group Displays SBC multicast Music-on-Hold group structure. Example: Device# show platform hardware qfp active feature sbc mmoh group SBC multicast Music-on-Hold group structure:
---------------------------------------
 VRF                                   = 0
 IP                                    = 239.1.1.1
 Port                                  = 16384
 Protocol                              = 1
 Calls in group                        = 1
 
SBC MMOH group Statistics
---------------------------------------
  Total RTP packets received                  = 406
  Total RTP octects received                  = 81200
  Total RTP packets replicated                = 406
  Total RTP octects replicated                = 81200
  Total RTP packets dropped                   = 0
  Total RTP octects dropped                   = 0 |