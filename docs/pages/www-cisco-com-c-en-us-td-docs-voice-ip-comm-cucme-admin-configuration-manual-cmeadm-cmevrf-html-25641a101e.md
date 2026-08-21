---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmevrf-html-25641a101e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmevrf.html
retrieved_at: 2026-08-21T07:25:33.879663+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: VRF Support

## Chapter: VRF Support

# VRF Support

Virtual Route Forwarding (VRF) divides a physical router into multiple
                        		logical routers, each having its own set of interfaces and routing and
                        		forwarding tables. VRF support in voice networks can be used to split
                        		Cisco Unified Communications Manager Express (Cisco Unified CME) into multiple
                        		virtual systems for SIP and SCCP endpoints and TAPI-based client applications
                        		and softphones on your PC.

## Prerequisites for
                        	 Configuring VRF Support

For Multi-VRF
                                       				support on SIP phones, Cisco Unified CME version has to be 10.5 and later.

For Multi-VRF
                                       				support on SCCP phones, Cisco Unified CME 7.0(1) or a later version must be
                                       				configured on the Cisco router.

VRF-Aware
                                       				H.323 and SIP must be configured on the Cisco Unified CME router, including the
                                       				following:

Up to five
                                                					 VRFs must be configured on the Cisco Unified CME router by using the ip vrf command. For configuration information, see VRF-Aware H.323 and SIP for Voice
                                                   						Gateways .

One of the
                                                					 groups must be designated as a global voice VRF (SIP Trunk) by using the voice vrf command. For configuration information, see VRF-Aware H.323 and SIP for Voice
                                                   						Gateways .

Example:

```
voice vrf voice-vrf
ip vrf data-vrf1
 rd 801:1
 route-target export 801:1
 route-target import 1000:1
!
ip vrf data-vrf2
 rd 802:1
 route-target export 802:1
 route-target import 1000:1
!
ip vrf voice-vrf
 rd 1000:1
 route-target export 1000:1
 route-target import 801:1
 route-target import 802:1
!
```

Interfaces on
                                       				the router must be configured for the VRFs by using the ip vrf forwarding command.

Only global
                                                   				  voice VRF is supported for SIP trunk.

Example:

```
interface GigabitEthernet0/0.301
 encapsulation dot1Q 301
 ip vrf forwarding data-vrf1
 ip address 10.1.10.1 255.255.255.0
!
interface GigabitEthernet0/0.302
 encapsulation dot1Q 302
 ip vrf forwarding data-vrf1
 ip address 10.2.10.1 255.255.255.0
!
interface GigabitEthernet0/0.303
 encapsulation dot1Q 303
 ip vrf forwarding voice-vrf
 ip address 10.3.10.1 255.255.255.0
```

VRFs must be
                                       				mapped to IP addresses using DHCP. For configuration information, see DHCP Service .

Example:

```
!<=== no ip dhcp command required only if “ip vrf forward” is specified under ip dhcp
no ip dhcp use vrf connected pool===>
!<=== Associate subnets with VRFs. Overlapping IP addresses are NOT supported.===>
ip dhcp pool vcme1
   network 10.1.10.0 255.255.255.0
   default-router 10.1.10.1 
   option 150 ip 10.1.10.1 
   class vcme1
      address range 10.1.10.10 10.1.10.250
!         
ip dhcp pool vcme2
   network 10.2.10.0 255.255.255.0
   default-router 10.2.10.1 
   option 150 ip 10.2.10.1 
   class vcme2
      address range 10.2.10.10 10.2.10.250
```

For more
                                       				configuration examples, see Example for Mapping IP Address Ranges to VRF Using DHCP .

Dial peers for
                                       				H323 and SIP trucks must be routed through the global voice VRF.

Dial peers
                                                   				  are global resources belonging to the voice VRF and shared with and accessible
                                                   				  from any VRF. There is no need to configure a dial peer for each individual
                                                   				  VRF.

## Restrictions for
                        	 Configuring VRF Support

Multi-VRF is not supported on Cisco 4000 Series Integrated Services
                                 			 Routers for Unified CME.

For SIP phones
                                 			 in Cisco Unified CME: SIP proxy and registrar must be in the same VRF.

IP-address
                                 			 overlap between VRFs is not supported.

Cross-VRF video
                                 			 is not supported.

The following
                                 			 call types are not supported for a voice VRF:

IP-to-IP
                                       				  gateway and gatekeeper configured on the same router.

IP-to-IP
                                       				  gateway with a VRF configured on one call leg and not on another call leg.

IP-to-IP
                                       				  gateway with one VRF configured for the H.323 call leg and a different VRF
                                       				  configured for the SIP call leg.

For H.323
                                       				  calls, only TCP is supported. H.323 UDP signaling is not supported. SIP calls
                                       				  support both TCP and UDP signaling.

The following
                                 			 features are not supported by on a VRF:

Call-fallback and RSVP features.

H.323 Annex
                                       				  E calls.

AAA and DNS
                                       				  components in voice-capable access routers. These routers communicate with AAA
                                       				  and DNS using the default routing table.

If a global
                                 			 voice VRF is not configured, signaling and media packets are sent using the
                                 			 default routing table.

Only the global
                                 			 voice VRF is supported for SIP trunk.

Cisco Unity
                                 			 Express on the Cisco Unified CME router must belong to the global voice VRF.

For Unified SIP CME, secondary source-address can’t be configured under a VRF group. Hence, redundancy isn’t supported under
                                 a VRF group.

Telnet is used to
                                       		  access Cisco Unity Express on the global voice VRF because the Service-Engine
                                       		  Service-Engine 1/0 session command is for non-VRF aware Cisco Unified CME only.
                                       		  To access the Cisco Unity Express module for defining voice-mail users on
                                       		  global voice VRF, telnet through the global voice VRF. For example: telnet
                                       		  10.10.10.5 2066 /vrf vrf. For more information, see the “Installing
                                          			 Cisco Unity Express Software” chapter in the appropriate Cisco Unity Express
                                          			 Administrator Guide for Cisco Unified CME .

## Information About VRF Support

### VRF-Aware Cisco Unified CME

VRF implementations enable you to consolidate voice communication into
                              		one logically-partitioned network to separate voice and data communication on a
                              		converged multimedia network.

#### VRF-Aware
                              	 Cisco Unified CME for SCCP Phones

In Cisco Unified CME
                                 		7.0(1) and later versions, VRF in voice networks can be used to share a
                                 		Cisco Unified CME among multiple closed-users groups with different
                                 		requirements. The actual call processing rules can be applied by voice on a per
                                 		VRF basis. A virtual Cisco Unified CME on each VRF is a collection of phones in
                                 		VRF groups that register in Cisco Unified CME through the VRF. All SCCP and SIP
                                 		phones connected to Cisco Unified CME register through the global voice VRF.
                                 		TAPI-based client applications and softphones on a PC must register through a
                                 		data VRF and can communicate with phones on the voice VRF.

VRF Support on
                                 		Cisco Unified CME provides the following enhancements to the VRF-Aware H.323
                                 		and SIP for Voice Gateways feature:

Line side
                                       			 support for up to 5 VRFs.

Interworks with
                                       			 the global voice VRF on an H323 or SIP Trunk.

Line side VRF
                                       			 can be a global voice VRF.

VRFs are
                                       			 assigned on a per-phone level.

Support for
                                       			 cross-VRF shared-lines.

For configuration
                                 		information, see Configure VRF Support .

#### Multi-VRF Support on Cisco Unified CME for SIP Phones

The Multi-VRF support on Cisco Unified CME for SIP Phones, provides the
                                 		following enhancements:

Up to five VRF groups can be configured on SIP line side under voice register global.

Under voice register pool, we can configure a VRF group to which the phone is associated with.

All SIP signaling and media traffic between CME and the phones would be routed on the specified VRF.

## Configure VRF Support

### Create VRF Groups
                           	 for SCCP Phones

To configure up to
                                 		  five VRF groups for users and phones in Cisco Unified CME, perform the
                                 		  following steps for each group to be configured.

### SUMMARY STEPS

- enable

- configure terminal

- telephony-service

- group group-tag [ vrf vrf name ]

- ip source-address ip-address [ port port ]

- url { authentication | directories | idle | information | messages | proxy-server | services } url

- service phone webAccess
                                       				  0

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

telephony-service

#### Example:

```
Router(config)# telephony-service
```

Enters
                                             				telephony-service configuration mode.

Step 4

group group-tag [ vrf vrf name ]

#### Example:

```
Router(config-telephony)# group 1
```

Creates a VRF
                                             				group for Cisco Unified CME users and phones.

group-tag —Unique identifier for VRF group being
                                                   					 configured. Range: 1 to 5.

(Optional) vrf vrfname —Name
                                                   					 of previously configured VRF to which this group is associated.

By
                                                   					 default, VRF groups are associated with a global voice VRF unless otherwise
                                                   					 specified by using the vrf vrfname keyword and argument combination.

Step 5

ip source-address ip-address [ port port ]

#### Example:

```
Router(conf-tele-group)# ip source-address 10.1.10.1 port 2000
```

Associates VRF
                                             				group with Cisco Unified CME.

ip address and port through
                                                   					 which Cisco Unified IP phones communicate with Cisco Unified CME.

Step 6

url { authentication | directories | idle | information | messages | proxy-server | services } url

#### Example:

```
Router(conf-tele-group)# url directories http://10.1.10.1/localdirectory
```

Provisions
                                             				uniform resource locators (URLs) for Cisco Unified IP phones connected to
                                             				Cisco Unified CME.

Step 7

service phone webAccess
                                                				  0

#### Example:

```
Router(conf-tele-group)# service phone webAccess 0
```

Enables
                                             				webAccess for IP phones. This is required for 9.x firmware, since the web
                                             				server is disabled by default. 8.x firmware and lower had the web server
                                             				enabled by default.

Step 8

end

#### Example:

```
Router(conf-tele-group)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  partial output from the show
                                       				running-config commands shows how to define three VRF groups for
                                 		  Cisco Unified CME. Group 1 is on the global voice VRF and the other two groups
                                 		  are on data VRFs.

```
telephony-service
 sdspfarm conference mute-on # mute-off #
 sdspfarm units 4
 sdspfarm transcode sessions 10
 sdspfarm tag 1 xcode101
 sdspfarm tag 2 conf103
 group  1 
  ip source-address 10.1.10.1 port 2000
  url directories http://10.1.10.1/localdirectory
 !
 group  2 vrf data-vrf1
  ip source-address 10.2.10.1 port 2000
 !
 group  3 vrf data-vrf2
  ip source-address 10.3.10.1 port 2000
```

### Create VRF Groups
                           	 for SIP Phones

In Cisco Unified
                                 		  CME 10.5 release the VRF support for SIP phones is added. Up to five VRF groups
                                 		  can be configured on SIP line side under voice register global. Under voice
                                 		  register pool, we can configure VRF group to which the phone is associated
                                 		  with. To configure VRF support, perform the following steps:

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- group group-tag [ vrf vrfname ]

- source-address ip-address

- url { authentication | directory | service } url

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

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register global

#### Example:

```
Router(config)# voice register global
```

Enters voice
                                             				register global configuration mode.

Step 4

group group-tag [ vrf vrfname ]

#### Example:

```
Router(config-register-global)# group 1
```

Creates a VRF
                                             				group for Cisco Unified CME users and phones.

group-tag —Unique identifier for VRF group being configured. Range: 1 to 5.

(Optional) vrf vrfname —Name of previously configured VRF to which this group is associated.

By default, this group is not associated with any VRF unless otherwise specified by using the vrf vrfname keyword and argument combination.

Defines unique identifiers group between 1 to 5, which can then be applied on individual pools.

The default behavior is no shut.

Step 5

source-address ip-address

#### Example:

```
Router(config-voice-register-group)# source-address 10.1.10.1
```

Associates VRF
                                             				group with Cisco Unified CME.

ip address through which Cisco Unified IP phones communicate with Cisco Unified CME.

Step 6

url { authentication | directory | service } url

#### Example:

```
Router(config-voice-register-group)# url directory http://10.1.10.1/localdirectory
```

Provisions uniform resource locators (URLs) for Cisco Unified IP phones connected to Cisco Unified CME.

Step 7

exit

#### Example:

```
Router(config-voice-register-group)# exit
```

Exits to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  sample output displays how to configure SIP CME support for VRF by provisioning
                                 		  its source address under a group:

```
voice register global or 
voice register dn
or 
voice register pool
 mode  cme
 max-dn 100
 max-pool 100

 group 1 vrf voice-vrf1
  source-address 8.0.0.1
```

### Add
                           	 Cisco Unified CME SCCP Phones to a VRF Group

To add an SCCP
                                 		  Cisco Unified IP phone, TAPI-based client, or softphone in Cisco Unified CME to
                                 		  a VRF group, perform the following steps for each phone to be added.

Restriction

All SCCP
                                                   				  phones in Cisco Unified CME must register through the global voice VRF and must
                                                   				  be added to the VRF group on the global voice VRF only.

Analog
                                                   				  phones connected to FXS ports on a IOS gateway must register through the global
                                                   				  voice VRF and must be added to the VRF group on the global voice VRF only.

TAPI-based
                                                   				  client applications and softphones on a PC must register through the data VRF
                                                   				  and must be added to a VRF group on a data VRF only.

VRF groups
                                                   				  do not support identical IP addresses or shared lines.

#### Before you begin

All ephone
                                       				configurations to be included in a VRF group must be already configured in
                                       				Cisco Unified CME. For configuration information, see Configure Phones to Make Basic Call .

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag

- description string

- mac-address [ mac-address ]

- group phone group-tag [ tapi group-tag ]

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

- Enter your password if
                                                				  prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

ephone phone-tag

#### Example:

```
Router(config)# ephone 11
```

Enters ephone
                                             				configuration mode for a Cisco Unified IP phone.

Step 4

description string

#### Example:

```
Router(config-ephone)# description cme-2801 srst
```

(Optional)
                                             				Includes descriptive text about the interface.

Step 5

mac-address [ mac-address ]

#### Example:

```
Router(config-ephone)# mac-address 0012.8055.d2EE
```

Associates the
                                             				MAC address of a Cisco Unified IP phone with an ephone configuration.

Step 6

group phone group-tag [ tapi group-tag ]

#### Example:

```
Router(config-ephone)# group phone 1
```

Adds a phone,
                                             				TAPI-based client, or softphone to a VRF group.

group-tag —Unique identifier for VRF group that was
                                                   					 previously configured by using the group command
                                                   					 in telephony-service configuration mode. Range: 1 to 5.

- This command can also be configured in
                                                				  ephone-template configuration mode and applied to one or more phones. The
                                                				  ephone configuration has priority over the ephone-template configuration.

Step 7

end

#### Example:

```
Router(config-ephone)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows how to add phones to VRF groups. Phones 1 and 3 are in VRF group
                                 		  1 on the global voice VRF. Phone 1 TAPI client and softphone 3 are in group 1
                                 		  on the data-vrf2. Phone 3 TAPI client and softphone 4 are in group 3 on
                                 		  data-vrf 2.

```
telephony-service 
		 sdspfarm conference mute-on # mute-off # 
		 sdspfarm units 4 
		 sdspfarm transcode sessions 10 
		 sdspfarm tag 1 xcode101 
		 sdspfarm tag 2 conf103 
		 group  1 vrf voice-vrf 
		  ip source-address 10.1.10.1 port 2000 
		  url directories http://10.1.10.1/localdirectory 
		 ! 
		 group  2 vrf data-vrf1 
		  ip source-address 10.2.10.1 port 2000 
		 ! 
		group  3 vrf data-vrf2 
		  ip source-address 10.3.10.1 port 2000 
		 ! 
		. 
		. 
		ephone-template 1 
		 group phone 1 tapi 2 
		ephone-template 2 
		 group phone 2 
		... 
		ephone 1 
		 ephone-template 1 
		ephone 2 
		 ephone-template 2 
		ephone 3 
		 group phone 1 tapi 3 
		ephone 4 
		 group phone 3 
		ephone  201 
		 group phone 1 
		 type anl
```

### Add
                           	 Cisco Unified CME SIP Phones to a VRF Group

To add an SIP
                                 		  Cisco Unified IP phone, or softphone in Cisco Unified CME to a VRF group,
                                 		  perform the following steps for each phone to be added.

#### Before you begin

All voice register pool configurations to be included in a VRF group must be already configured in Cisco Unified CME. For
                                       configuration information, see Configure Phones to Make Basic Call .

### SUMMARY STEPS

- enable

- configure terminal

- voice register pool pool-tag

- id mac [ mac-address ]

- group group-tag

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

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Router# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice register pool pool-tag

#### Example:

```
Router(config-register-pool)# group
```

Enters voice
                                             				reigster pool configuration mode for a Cisco Unified IP phone.

Step 4

id mac [ mac-address ]

#### Example:

```
Router(config-regoster-pool)# id mac 0012.8055.d2EE
```

Associates the
                                             				MAC address of a Cisco Unified IP phone with an voice register pool
                                             				configuration.

Step 5

group group-tag

#### Example:

```
Router(config-register pool)# group 1
```

Adds a phone,
                                             				or softphone to a VRF group.

group-tag —Unique identifier for VRF group that was previously configured by using the group command in voice register global configuration mode. Range: 1 to 5.

Step 6

end

#### Example:

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows how to add SIP phones to VRF groups.

```
voice register global 
		 mode  cme
		 max-dn 100
		 max-pool 100 
		 authenticate realm ccmsipline 
		 voicemail 24001
		 phone-mode phone-only
		 tftp-path flash: 
		 create profile sync 0000443960010126
		 conference hardware 
		 group 1 vrf voice-vrf1 
		  source-address 8.0.0.1 
		 ! 
		 group 2 vrf data-vrf1 
		  url authentication http://7.0.0.1/CCMCIP/authenticate.asp
		  source-address 7.0.0.1 
		 ! 
		 group 3 vrf data-vrf1 
		  source-address 10.104.45.142 
		 ! 
		 group 4 vrf voice-vrf1 
		  source-address 9.42.29.101 
		 ! 
		! 
		voice register pool  1 
		 id mac A40C.C395.7B5C 
		 session-transport tcp
		 type 9971 
		 number 1 dn 1 
		 group 1 
		 template 1 
		 dtmf-relay rtp-nte 
		 username 14001 password 14001 
		 codec g711ulaw 
		 paging-dn 99 
		!
```

## Configuration Examples for Configuring VRF Support

### Example for Mapping IP Address Ranges to VRF Using DHCP

Duplicate IP addresses, with or without specifying a VRF, are not
                                             			 supported in Cisco Unified CME 7.0(1).

There are three ways to assign DHCP addresses: global address
                                 		  allocation; VRF pool; or individual host

With a global address allocation scheme, you must use the no ip dhcp use vrf connected command.

```
no ip dhcp use vrf connected
!
ip dhcp pool vcme1
   network 209.165.201.10 255.255.255.224
   option 150 ip 209.165.201.9 
   default-router 209.165.201.9 
   class vcme1
      address range 209.165.201.1 209.165.201.30
!
```

The following example shows how to assign addresses from VRF pool
                                 		  vcme1.

```
ip dhcp use vrf connected
!
ip dhcp pool vcme1
   vrf data-vrf1
   network 209.165.201.10 255.255.255.224
   option 150 ip 209.165.201.9
   default-router 209.165.201.9 
   class vcme1
      address range 209.165.201.1 209.165.201.30
!
```

The following example show how to assign an address by an individual
                                 		  host. You must replace the first two hexadecimal digits of a host MAC address
                                 		  with 01 .

```
ip dhcp pool phone3
   host 209.165.201.15 255.255.255.224
   client-identifier 0100.0ed7.4ce6.3d
   default-router 209.165.201.11 
   option 150 ip 209.165.201.11 
!
```

### Example for
                           	 Configuring VRF-Aware Hardware Conferencing

#### Hardware
                                 		  Conferencing with Internal DSP Farm

The internal
                                          				DSPFarm must be registered through a local loopback interface.

The loopback
                                          				allows Cisco Unified CME to access the media path in global routing table.

The boldface
                                 		  commands in the following configuration example show that the signaling and
                                 		  media paths are accessed through the global routing table and the loopback
                                 		  interface is in default routing table.

```
interface Loopback5 ip address 12.5.10.1 255.255.255.255 ! sccp local Loopback5 sccp ccm 12.5.10.1 identifier 2 version 4.1
		sccp
		!
		sccp ccm group 2 bind interface Loopback5 associate ccm 2 priority 1
		 associate profile 103 register conf103
		 associate profile 101 register xcode101
		!
		telephony-service
		 sdspfarm conference mute-on # mute-off #
		 sdspfarm units 4
		 sdspfarm transcode sessions 10
		 sdspfarm tag 1 xcode101
		 sdspfarm tag 2 conf103
		 group  1 vrf vrf1
		 ip source-address 10.1.10.1 port 2000
		!
		 group  2 vrf vrf2
		  ip source-address 10.2.10.1 port 2000
		!
		group  3 vrf vrf3
		  ip source-address 10.3.10.1 port 2000
		!
		group  4 vrf vrf4
		  ip source-address 10.4.10.1 port 2000
		! group  5 ip source-address 12.5.10.1 port 2000 !
		conference hardware
		max-ephones 240
		max-dn 480
		voicemail 7710
		max-conferences 8 gain -6
```

#### Hardware
                                 		  Conferencing with External DSP Farm

Configure DSP
                                          				farm as usual on a Cisco router.

The external
                                          				DSP farm must be registered to Cisco Unified CME through the interface or
                                          				subinterface assigned to the global voice VRF. Make sure the connection path is
                                          				coming in through the voice VRF.

The router on
                                          				which the external DSP farm is configured does not have to be VRF-aware.

For information
                                 		  about configuring DSP Farms, see Configure Transcoding Resources .

### Example for
                           	 Configuring Cisco Unity Express on Global Voice VRF

```
voice vrf vrf2 
		   ip vrf data-vrf2 
		   rd 100:2  
		   route-target export 100:2  
		   route-target import 100:2 
		  ! 
		  Interface loop back 0 
		  ip vrf forwarding data-vrf2 
		  Ip address 21.10.10.2 
		  !<==The following config puts CUE in the voice vrf. Service-engine interface and service-module must have an IP address.===> 
		  ! 
		  interface Service-Engine1/0  
		   ip vrf forwarding voice-vrf3 ip address 21.10.10.5 255.255.255.0 
		   service-module ip address 21.10.10.6 255.255.255.0 
		   service-module ip default-gateway 21.10.10.2! 
		   ip route 21.10.10.6 255.255.255.255 Service-Engine1/0 
		  … 
		  line 66  
		  no activation-character
```

Hardware
                                    			 Conferencing with Internal DSP Farm

The internal
                                       				DSPFarm must be registered through a local loopback interface.

The loopback
                                       				allows Cisco Unified CME to access the media path in global routing table.

The boldface
                                 		  commands in the following configuration example show that the signaling and
                                 		  media paths are accessed through the global routing table and the loopback
                                 		  interface is in default routing table.

```
interface Loopback5 ip address 12.5.10.1 255.255.255.255 ! sccp local Loopback5 sccp ccm 12.5.10.1 identifier 2 version 4.1 
		  sccp 
		  ! 
		  sccp ccm group 2 bind interface Loopback5 associate ccm 2 priority 1 
		   associate profile 103 register conf103 
		   associate profile 101 register xcode101 
		  ! 
		  telephony-service 
		   sdspfarm conference mute-on # mute-off # 
		   sdspfarm units 4 
		   sdspfarm transcode sessions 10 
		   sdspfarm tag 1 xcode101 
		   sdspfarm tag 2 conf103 
		   group  1 vrf vrf1 
		    ip source-address 10.1.10.1 port 2000 
		  ! 
		   group  2 vrf vrf2 
		    ip source-address 10.2.10.1 port 2000 
		  ! 
		  group  3 vrf vrf3 
		    ip source-address 10.3.10.1 port 2000 
		  ! 
		  group  4 vrf vrf4 
		    ip source-address 10.4.10.1 port 2000 
		  ! group  5 ip source-address 12.5.10.1 port 2000 ! 
		  conference hardware 
		  max-ephones 240 
		  max-dn 480 
		  voicemail 7710 
		  max-conferences 8 gain -6
```

Hardware
                                    			 Conferencing with External DSP Farm

Configure DSP
                                       				farm as usual on a Cisco router.

The external
                                       				DSP farm must be registered to Cisco Unified CME through the interface or
                                       				subinterface assigned to the global voice VRF. Make sure the connection path is
                                       				coming in through the voice VRF.

The router on
                                       				which the external DSP farm is configured does not have to be VRF-aware.

For information
                                 		  about configuring DSP Farms, see Configure Transcoding Resources .

### Example for Configuring Multi- VRF Support for Cisco Unified CME SIP
                           	 Phones

The following sample output displays CME configuration which enables
                                 		  the user to accept registrations from multiple VRFs.

```
voice register global
		 mode  cme
		 max-dn 100
		 max-pool 100
		 authenticate realm ccmsipline
		 voicemail 24001
		 phone-mode phone-only
		 tftp-path flash:
		 create profile sync 0000443960010126
		 conference hardware
		 group 1 vrf voice-vrf1
		  source-address 8.0.0.1
		 !
		 group 2 vrf data-vrf1
		  url authentication http://7.0.0.1/CCMCIP/authenticate.asp
		  source-address 7.0.0.1
		 !
		 group 3 vrf data-vrf1
		  source-address 10.104.45.142
		 !
		 group 4 vrf voice-vrf1
		  source-address 9.42.29.101
		 !
		!
		voice register dn  1
		 number 14001
		 name voicevrf-ph1
		!
		voice register dn  2
		 number 14002
		 allow watch
		 name datavrf-ph1
		!
		voice register dn  3
		 number 14003
		 allow watch
		 name voicevrf-ph2
		!
		voice register dn  4
		 voice-hunt-groups login
		 number 14004
		 name Jabber-Win
		!
		voice register dn  5
		 number 14005
		 name Jabber-Android
		!
		voice register dn  6
		 number 14006
		 allow watch
		 mobility
		 snr 24001 delay 5 timeout 50
		!
		voice register dn  7
		 number 14007
		 name voicevrf-7841
		!
		voice register dn  8
		 number 14008
		 name jabbed-android-2
		!
		voice register dn  10
		 number 14010
		 allow watch
		 name intervrf-shared-line
		 shared-line max-calls 8
		!
		voice register dn  11
		 number 14011
		 shared-line
		!
		voice register dn  12
		 number 15002
		 name em-logged-in
		!
		voice register dn  21
		 number 1101
		 name CME1-Phone1
		!
		voice register dn  22
		 number 1102
		 name CME1-Phone2
		!
		voice register template  1
		 softkeys idle  Newcall Pickup Redial Cfwdall DND
		 softkeys ringIn  Answer DND iDivert
		 softkeys connected  Endcall Hold Mobility iDivert Park
		!
		voice register pool  1
		 id mac A40C.C395.7B5C
		 session-transport tcp
		 type 9971
		 number 1 dn 1
		 group 1
		 template 1
		 dtmf-relay rtp-nte
		 username 14001 password 14001
		 codec g711ulaw
		 paging-dn 99
		!
		voice register pool  2
		 fastdial 1 14003 name voice-vrf1-ph1
		 id mac ACA0.16FC.9742
		 type 9971
		 number 1 dn 2
		 number 2 dn 10
		 group 2
		 template 1
		 presence call-list
		 dtmf-relay rtp-nte
		 codec g711ulaw
		 paging-dn 99
		 blf-speed-dial 1 13001 label "13001"
		 blf-speed-dial 2 14006 label "14006"
		!
		voice register pool  3
		 fastdial 1 14002 name datavrf,ph1
		 id mac 2893.FEA3.2557
		 type 9951
		 number 1 dn 3
		 number 2 dn 10
		 group 1
		 template 1
		 dtmf-relay rtp-nte
		 username 14003 password 14003
		 codec g711ulaw
		 blf-speed-dial 1 14002 label "14002"
		 blf-speed-dial 2 14006 label "14006"
		 blf-speed-dial 3 13001 label "13001"
		!
		voice register pool  4
		 id device-id-name arunsrin
		 type Jabber-CSF-Client
		 number 1 dn 4
		 group 3
		 dtmf-relay rtp-nte
		 username arunsrin password cisco
		 codec g711ulaw
		!
		voice register pool  5
		 registration-timer max 720 min 660
		 id mac 980C.821B.26CD
		 session-transport tcp
		 type Jabber-Android
		 number 1 dn 5
		 group 3
		 dtmf-relay rtp-nte
		 username frodo password cisco
		 codec g711ulaw
		!
		voice register pool  6
		 busy-trigger-per-button 40
		 id mac 6C41.6A36.900D
		 type 7821
		 number 1 dn 6
		 group 1
		 template 1
		 presence call-list
		 dtmf-relay rtp-nte
		 codec g711ulaw
		 paging-dn 99
		!
		voice register pool  7
		 busy-trigger-per-button 40
		 id mac 6C41.6A36.9110
		 session-transport tcp
		 type 7841
		 number 1 dn 7
		 group 2
		 dtmf-relay rtp-nte
		 codec g711ulaw
		 paging-dn 99
		!
		voice register pool  8
		 registration-timer max 720 min 660
		 id mac 980C.821A.5D28
		 session-transport tcp
		 type Jabber-Android
		 number 1 dn 8
		 group 3
		 dtmf-relay rtp-nte
		 username pippin password cisco
		 codec g711ulaw
		!
		voice register pool  21
		 id mac 1000.1000.1101
		 type 7970
		 number 1 dn 21
		 group 4
		 username 1101 password 1101
		 codec g711ulaw
		!
		voice register pool  22
		 id mac 1000.1000.1102
		 type 7970
		 number 1 dn 21
		 group 4
		 username 1102 password 1102
		 codec g711ulaw
		!
		voice hunt-group 1 parallel
		 phone-display
		 final 13002
		 list 14001,14002,14003
		 timeout 3 
		 pilot 14999 
		!
		!
		voice hunt-group 2 parallel
		 final 14001
		 list 14004,*,14002
		 timeout 5 
		 pilot 14998 
		 name test-vhg
		!
		!
		voice logout-profile 1
		 pin 1234
		 user 14002 password 14002
		 number 14002 type normal
		 speed-dial 1 13002 label "ephone2" 
		!
		voice user-profile 1
		 user me password me
		 number 15002 type normal
		!
		!
		!
		voice translation-rule 217351
		 rule 1 /^24/ /9924\1/
		!
		!
		voice translation-profile 217351
```

## Feature
                        	 Information for VRF Support

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Cisco Unified CME Version

Feature Information

VRF Support in Cisco Unified CME

7.0(1)

VRF supports Cisco Unified CME, conferencing, transcoding, and
                                          					 RSVP components. VRF also allows soft phones in data VRF resources to
                                          					 communicate with phones in a VRF voice gateway.

| Note | Only global
                                                   				  voice VRF is supported for SIP trunk. |
|---|---|

| Note | Dial peers
                                                   				  are global resources belonging to the voice VRF and shared with and accessible
                                                   				  from any VRF. There is no need to configure a dial peer for each individual
                                                   				  VRF. |
|---|---|

| Note | Telnet is used to
                                       		  access Cisco Unity Express on the global voice VRF because the Service-Engine
                                       		  Service-Engine 1/0 session command is for non-VRF aware Cisco Unified CME only.
                                       		  To access the Cisco Unity Express module for defining voice-mail users on
                                       		  global voice VRF, telnet through the global voice VRF. For example: telnet
                                       		  10.10.10.5 2066 /vrf vrf. For more information, see the “Installing
                                          			 Cisco Unity Express Software” chapter in the appropriate Cisco Unity Express
                                          			 Administrator Guide for Cisco Unified CME . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | telephony-service Example: Router(config)# telephony-service | Enters
                                             				telephony-service configuration mode. |
| Step 4 | group group-tag [ vrf vrf name ] Example: Router(config-telephony)# group 1 | Creates a VRF
                                             				group for Cisco Unified CME users and phones. group-tag —Unique identifier for VRF group being
                                                   					 configured. Range: 1 to 5. (Optional) vrf vrfname —Name
                                                   					 of previously configured VRF to which this group is associated. By
                                                   					 default, VRF groups are associated with a global voice VRF unless otherwise
                                                   					 specified by using the vrf vrfname keyword and argument combination. |
| Step 5 | ip source-address ip-address [ port port ] Example: Router(conf-tele-group)# ip source-address 10.1.10.1 port 2000 | Associates VRF
                                             				group with Cisco Unified CME. ip address and port through
                                                   					 which Cisco Unified IP phones communicate with Cisco Unified CME. |
| Step 6 | url { authentication \| directories \| idle \| information \| messages \| proxy-server \| services } url Example: Router(conf-tele-group)# url directories http://10.1.10.1/localdirectory | Provisions
                                             				uniform resource locators (URLs) for Cisco Unified IP phones connected to
                                             				Cisco Unified CME. |
| Step 7 | service phone webAccess
                                                				  0 Example: Router(conf-tele-group)# service phone webAccess 0 | Enables
                                             				webAccess for IP phones. This is required for 9.x firmware, since the web
                                             				server is disabled by default. 8.x firmware and lower had the web server
                                             				enabled by default. |
| Step 8 | end Example: Router(conf-tele-group)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice
                                             				register global configuration mode. |
| Step 4 | group group-tag [ vrf vrfname ] Example: Router(config-register-global)# group 1 | Creates a VRF
                                             				group for Cisco Unified CME users and phones. group-tag —Unique identifier for VRF group being configured. Range: 1 to 5. (Optional) vrf vrfname —Name of previously configured VRF to which this group is associated. By default, this group is not associated with any VRF unless otherwise specified by using the vrf vrfname keyword and argument combination. Defines unique identifiers group between 1 to 5, which can then be applied on individual pools. Note Use the shutdown command to temporarily shutdown the group without effecting the other groups. Use the no form of the command
                                                            to enable the group. The default behavior is no shut. | Note | Use the shutdown command to temporarily shutdown the group without effecting the other groups. Use the no form of the command
                                                            to enable the group. |
| Note | Use the shutdown command to temporarily shutdown the group without effecting the other groups. Use the no form of the command
                                                            to enable the group. |
| Step 5 | source-address ip-address Example: Router(config-voice-register-group)# source-address 10.1.10.1 | Associates VRF
                                             				group with Cisco Unified CME. ip address through which Cisco Unified IP phones communicate with Cisco Unified CME. |
| Step 6 | url { authentication \| directory \| service } url Example: Router(config-voice-register-group)# url directory http://10.1.10.1/localdirectory | Provisions uniform resource locators (URLs) for Cisco Unified IP phones connected to Cisco Unified CME. |
| Step 7 | exit Example: Router(config-voice-register-group)# exit | Exits to
                                             				privileged EXEC mode. |

| Note | Use the shutdown command to temporarily shutdown the group without effecting the other groups. Use the no form of the command
                                                            to enable the group. |
|---|---|

| Restriction | All SCCP
                                                   				  phones in Cisco Unified CME must register through the global voice VRF and must
                                                   				  be added to the VRF group on the global voice VRF only. Analog
                                                   				  phones connected to FXS ports on a IOS gateway must register through the global
                                                   				  voice VRF and must be added to the VRF group on the global voice VRF only. TAPI-based
                                                   				  client applications and softphones on a PC must register through the data VRF
                                                   				  and must be added to a VRF group on a data VRF only. VRF groups
                                                   				  do not support identical IP addresses or shared lines. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if
                                                				  prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag Example: Router(config)# ephone 11 | Enters ephone
                                             				configuration mode for a Cisco Unified IP phone. |
| Step 4 | description string Example: Router(config-ephone)# description cme-2801 srst | (Optional)
                                             				Includes descriptive text about the interface. |
| Step 5 | mac-address [ mac-address ] Example: Router(config-ephone)# mac-address 0012.8055.d2EE | Associates the
                                             				MAC address of a Cisco Unified IP phone with an ephone configuration. |
| Step 6 | group phone group-tag [ tapi group-tag ] Example: Router(config-ephone)# group phone 1 | Adds a phone,
                                             				TAPI-based client, or softphone to a VRF group. group-tag —Unique identifier for VRF group that was
                                                   					 previously configured by using the group command
                                                   					 in telephony-service configuration mode. Range: 1 to 5. This command can also be configured in
                                                				  ephone-template configuration mode and applied to one or more phones. The
                                                				  ephone configuration has priority over the ephone-template configuration. |
| Step 7 | end Example: Router(config-ephone)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice register pool pool-tag Example: Router(config-register-pool)# group | Enters voice
                                             				reigster pool configuration mode for a Cisco Unified IP phone. |
| Step 4 | id mac [ mac-address ] Example: Router(config-regoster-pool)# id mac 0012.8055.d2EE | Associates the
                                             				MAC address of a Cisco Unified IP phone with an voice register pool
                                             				configuration. |
| Step 5 | group group-tag Example: Router(config-register pool)# group 1 | Adds a phone,
                                             				or softphone to a VRF group. group-tag —Unique identifier for VRF group that was previously configured by using the group command in voice register global configuration mode. Range: 1 to 5. |
| Step 6 | end Example: Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

| Note | Duplicate IP addresses, with or without specifying a VRF, are not
                                             			 supported in Cisco Unified CME 7.0(1). |
|---|---|

| Feature Name | Cisco Unified CME Version | Feature Information |
|---|---|---|
| VRF Support in Cisco Unified CME | 7.0(1) | VRF supports Cisco Unified CME, conferencing, transcoding, and
                                          					 RSVP components. VRF also allows soft phones in data VRF resources to
                                          					 communicate with phones in a VRF voice gateway. |