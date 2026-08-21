---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmelpcor-html-42e8fe0fe6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmelpcor.html
retrieved_at: 2026-08-21T07:24:46.673896+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Call Restriction Regulations

## Chapter: Call Restriction Regulations

# Call Restriction Regulations

## Prerequisites for LPCOR

Cisco IOS Release 15.0(1)XA or a later release.

Cisco Unified CME 8.0 or a later version.

## Information About LPCOR

### LPCOR
                           	 Overview

The Telecom
                              		Regulatory Authority of India (TRAI) has regulations that restrict the mixing
                              		of voice traffic between the PSTN and VoIP networks. Previously, this required
                              		a user to have two phones to handle both PSTN and VoIP calls; an IP phone
                              		connected to the Electronic Private Automatic Branch Exchange (EPABX) for
                              		intra-office and inter-office VoIP calls and a separate phone connected to a
                              		PABX for PSTN calls, as shown in Separate PBX
                                 		  and EPABX Systems .

New regulations
                              		allow for a single network infrastructure and single EPABX to connect to both
                              		the PSTN and VoIP networks by using a logical partitioning between the PSTN and
                              		IP leased lines.

The logical
                              		partitioning class of restriction (LPCOR) feature enables a single directory
                              		number on an IP phone or analog phone registered to Cisco Unified CME to
                              		connect to both PSTN and VoIP calls according to the connection restrictions
                              		specified by TRAI regulations. Cisco Unified CME can support both VoIP and PSTN
                              		calls while restricting the mixing of voice traffic between the PSTN and VoIP
                              		networks and preventing PSTN calls from connecting to remote locations over an
                              		IP trunk, as shown in Single EPAPX
                                 		  System with PSTN and VoIP Calls Partitioning .

### LPCOR Policy and Resource Groups

Cisco Unified CME supports a high-level class of restriction by allowing
                              		you to logically partition its resources (PSTN trunks, IP trunks, IP phones,
                              		and analog phones) into different groups. The resources of each group are
                              		scalable based on the voice interface, trunk group, or IP address subnet. In
                              		general, you should not have to modify your existing dial plan to support LPCOR
                              		functionality. The dial peer class of restriction (COR) feature remains
                              		unchanged when the LPCOR feature is added to Cisco Unified CME.

LPCOR control is based on the location of resources, where calls are
                              		originating and terminating. You must partition the resources of the
                              		Cisco Unified CME router into different resource groups and then create a LPCOR
                              		policy for each group to which you want to apply call restrictions.

You create a LPCOR policy matrix for individual resource groups by
                              		defining its LPCOR policy to either accept or reject calls that originate from
                              		any of the other resource groups. You can define one LPCOR policy for each
                              		resource group.

The same LPCOR policy is applied to multiple directory numbers from the
                              		same resource. For example, if multiple directory numbers are defined for a
                              		SCCP phone, the same LPCOR policy is enforced for all calls to the different
                              		directory numbers on the SCCP phone.

In the following example, PSTN trunks, IP trunks (H.323 and SIP), analog
                              		FXS phones, and IP phones for a Cisco Unified CME router are partitioned into
                              		five different resource groups (RG1 to RG5).

Resource Groups

RG1

RG2

RG3

RG4

RG5

RG1

Yes

No

Yes

No

Yes

RG2

Yes

Yes

No

Yes

No

RG3

Yes

Yes

Yes

Yes

No

RG4

No

No

No

Yes

Yes

RG5

No

Yes

Yes

Yes

No

Call from RG1 to target RG1 is allowed

Call from RG2 to target RG3 is not allowed

Call from RG3 to target RG2 is allowed

Call from RG5 to target RG5 is not allowed

#### Default LPCOR Policy

The default LPCOR policy means that there are no restrictions between
                                 		the call source and its target destination. When a call is presented to a
                                 		target destination, Cisco Unified CME bypasses LPCOR validation if either the
                                 		incoming call is not associated with a LPCOR policy or the LPCOR policy is not
                                 		defined for the target destination.

TRAI regulations allow the same directory number on a local IP phone or
                                 		SCCP analog Foreign Exchange Station (FXS) phone in Cisco Unified CME to handle
                                 		both PSTN and VoIP calls. Locally connected phones do not have to be associated
                                 		with any resource group.

### How LPCOR Policies are Associated with Resource Groups

Call restrictions are applied to LPCOR resource groups based on the
                              		location of the resources. You create LPCOR policies that define the call
                              		restrictions to apply to calls that originate or terminate at the following
                              		types of resources.

#### Analog
                              	 Phones

TRAI regulations
                                 		allow an analog FXS phone to accept both PSTN and VoIP calls if the phone is
                                 		locally registered to Cisco Unified CME. Locally connected phones do not have
                                 		to be associated with any resource group; the default LPCOR policy is applied
                                 		to this phone type.

A specific LPCOR
                                 		policy can be defined through the voice port or trunk group. For configuration
                                 		information, see Associate a LPCOR Policy with Analog Phone or PSTN Trunk Calls .

#### IP Phones

LPCOR supports both
                                 		SCCP and SIP IP phones. TRAI regulations allow an IP phone to accept both PSTN
                                 		and VoIP calls if the IP phone is registered locally to Cisco Unified CME
                                 		through the LAN. If the IP phone is registered to Cisco Unified CME through the
                                 		WAN, PSTN calls must be blocked from the remote IP phones.

If an IP phone
                                 		always registers to Cisco Unified CME from the same local or remote region, the
                                 		phone is provisioned with a static LPCOR policy. For configuration information,
                                 		see Associate a LPCOR Policy with IP Phone or SCCP FXS Phone Calls .

If the phone is a
                                 		mobile-type IP phone and moves between the local and remote regions, such as an
                                 		Extension Mobility phone, Cisco IP Communicator softphone, or a remote
                                 		teleworker phone, the LPCOR policy is provisioned dynamically based on the IP
                                 		phone’s currently registered IP address. For configuration information, see Associate LPCOR with Mobile Phone Calls .

#### PSTN
                              	 Trunks

An incoming LPCOR
                                 		resource group is associated with a PSTN trunk (digital or analog) through the
                                 		voice port or trunk group.

When a call is
                                 		routed to the PSTN network, the LPCOR policy of the target PSTN trunk can block
                                 		calls from any resource group it is not explicitly configured to accept.
                                 		Outgoing calls from a PSTN trunk are associated with a LPCOR policy based on
                                 		either the voice port or trunk group, whichever is configured in the outbound
                                 		POTS dial-peer.

For configuration
                                 		information, see Associate a LPCOR Policy with Analog Phone or PSTN Trunk Calls .

#### VoIP
                              	 Trunks

An incoming VoIP
                                 		trunk call (H.323 or SIP) is associated with a LPCOR policy based on the remote
                                 		IP address as follows:

##### Incoming H.323
                                    		  trunk call

IP address of
                                             				the previous hub or originating gateway

##### Incoming SIP
                                    		  trunk call

IP address of
                                             				the originating gateway

Hostname from
                                             				the earliest Via header of an incoming INVITE message. If the hostname is in
                                             				domain name format, a DNS query is performed to resolve the name into an IP
                                             				address.

Cisco Unified CME
                                    		  uses the resolved hostname or resolved IP address to determine the LPCOR policy
                                    		  based on the entries in the IP-trunk subnet table. If the LPCOR policy cannot
                                    		  be found through the IP address or hostname, the incoming H.323 or SIP trunk
                                    		  call is associated with the incoming LPCOR policy configured in voice service
                                    		  configuration mode.

The LPCOR policy
                                    		  of the VoIP target is determined through the configuration of the outbound VoIP
                                    		  dial-peer. The default LPCOR policy is applied to the VoIP target if an
                                    		  outgoing LPCOR policy is not defined in the target VoIP dial-peer.

For configuration
                                    		  information, see Associate a LPCOR Policy with VoIP Trunk Calls .

### LPCOR Support for
                           	 Supplementary Services

Table 1 describes LPCOR support for calls using supplementary services.

Feature

Description

SCCP Phone

SIP Phone

Basic Call

Cisco Unified CME invokes the LPCOR policy validation if both
                                             				  the incoming call and target destination are associated with a LPCOR policy.

If the LPCOR
                                             				  policy validation fails, cause-code 63 (no service available) or the
                                             				  user-defined cause-code is returned to the remote switch. The call can hunt to
                                             				  the next destination.

Yes

Yes

Call Forward

When a call
                                             				  is forwarded to a new destination, Cisco Unified CME invokes the LPCOR policy
                                             				  validation between the source and the forwarding target. The call is not
                                             				  forwarded to the target if the LPCOR policy is restricted.

Yes

Yes

Call
                                             				  Transfer

Blind and
                                             				  Consultative Call Transfer is restricted if the LPCOR policy validation fails
                                             				  between the transferee and transfer-to parties.

For
                                             				  consultative call transfers, the reorder tone plays and an error message
                                             				  displays on the transferor phone. The call is not disconnected between the
                                             				  transferee and transferor.

Yes

Yes

Ad Hoc
                                             				  Conference (software-based, 3-party)

Cisco Unified CME invokes the LPCOR policy validation for each
                                             				  call joined to a conference. A call is blocked from joining the conference if
                                             				  the LPCOR policy validation fails.

The reorder
                                             				  tone plays and the conference cannot complete message displays on the IP phone
                                             				  that initiated the conference. The call is resumed by the transferor who
                                             				  initiated the conference.

If the
                                                         					 LPCOR policy validation fails during a blind transfer setup to a conference
                                                         					 bridge, the call is released.

LPCOR
                                                         					 validation is not supported for additional call transfer or conference
                                                         					 operations from a 3-party software conference call.

Yes

No

Ad Hoc
                                             				  Conference (hardware-based)

Yes

Yes

Meet-Me
                                             				  Conference

LPCOR policy
                                             				  of each conference party is validated when a new call is joined to a
                                             				  conference. The call is blocked from joining the conference if the LPCOR policy
                                             				  validation fails.

The reorder
                                             				  tone plays and the conference cannot complete message displays on the IP phone
                                             				  that initiated the Meet-Me conference.

Yes

Yes (join
                                             				  only)

Call
                                             				  Pickup/Group Pickup (Cisco Unified CME 7.1 and later versions)

Call Pickup
                                             				  and Pickup Groups enable phone users to answer a call that is ringing on a
                                             				  different extension. The pickup is blocked if the LPCOR policy validation
                                             				  between the call and the pickup phone fails.

The reorder
                                             				  tone plays and the unknown number message displays on the IP phone that
                                             				  attempts the call pickup.

Yes

Yes

Call Park
                                             				  (Cisco Unified CME 7.1 and later versions)

Phone users
                                             				  can place a call on hold at a special extension so it can be retrieved by other
                                             				  phones.

A phone is
                                             				  not allowed to retrieve a parked call if the LPCOR policy validation fails. The
                                             				  reorder tone plays and the unknown number message displays on the IP phone that
                                             				  attempts to retrieve the parked call. The call remains parked at the call-park
                                             				  slot.

Yes

Yes

Call Park
                                             				  Retrieval

Yes

Yes

Hunt Group
                                             				  Pilot (ephone hunt group)

Supported
                                             				  for sequential and longest idle hunt groups. The LPCOR policy validation is
                                             				  performed when a call is directed to a SCCP endpoint through the ephone
                                             				  hunt-group.

Yes

No

Hunt Group
                                             				  Pilot (voice hunt group)

Supported
                                             				  for parallel hunt groups only. A hunt target can be a SCCP phone, SIP phone,
                                             				  VoIP trunk, or PSTN trunk. The LPCOR policy validation is performed between the
                                             				  call and the pilot hunt target. A call is blocked from a target if the LPCOR
                                             				  policy is restricted.

Yes

Yes

Shared
                                             				  Line

Phones
                                             				  with a shared directory number must have the same LPCOR policy.

Yes

Yes

CBarge

Phone
                                             				  users who share a directory number can join an active call on the shared line.
                                             				  Phones must have the same LPCOR policy.

Yes

Yes

Third-Party Call Control

Cisco
                                             				  Unified CME supports out-of-dialog refer (OOD-R) by a remote call-control
                                             				  system. The LPCOR validation is performed during the second outbound call setup
                                             				  after the first outbound call is established. The OOD-R request fails if the
                                             				  LPCOR policy between the first and second outbound call is restricted.

Yes

Yes

### Phone Display and
                           	 Warning Tone for LPCOR

Cisco Unified CME
                              		plays the reorder tone to callers when it blocks calls due to LPCOR policy
                              		authentication. Table 1 lists the message that displays on the phone when a call is blocked.

Call Block
                                             				  Type

Phone
                                             				  Display Message

SCCP Phone

SIP Phone

Call
                                             				  Transfer

Unable to
                                             				  Transfer

Transfer
                                             				  Failed

Conference

Cannot
                                             				  Complete Conference

Meet-Me
                                             				  Conference

No Screen
                                             				  Display Update

Pickup

Unknown
                                             				  Number

Park

Unknown
                                             				  Number

### LPCOR VSAs

New vendor-specific
                              		attributes (VSAs) for the LPCOR policy associated with a call are included in
                              		the call detail records (CDRs) generated by Cisco Unified CME for Remote
                              		Authentication Dial-in User Services (RADIUS) accounting. A null value is used
                              		for call legs without an associated LPCOR policy, which is the default LPCOR
                              		value. The incoming or outgoing LPCOR policy of a call is added to RADIUS stop
                              		records.

Table 1 lists
                              		the new VSAs.

Attribute

VSA No.
                                             				  (Decimal)

Format for
                                             				  Value or Text

Sample Value
                                             				  or Text

Description

in-lpcor-group

1

String

```
pstn_group
```

Logical
                                             				  partitioning class of restriction (LPCOR) resource-group policy associated with
                                             				  an incoming call.

out-lpcor-group

1

String

```
voip_group
```

LPCOR
                                             				  resource-group policy associated with an outgoing call.

## Configure LPCOR

### Define a LPCOR
                           	 Policy

To enable LPCOR
                                 		  functionality and define a policy for each resource group that requires call
                                 		  restrictions, perform the following task. You can define one LPCOR policy for
                                 		  each resource group. Do not create a LPCOR policy for resource groups that do
                                 		  not require call restrictions. A target resource group without a LPCOR policy
                                 		  can accept incoming calls from any other resource group.

### SUMMARY STEPS

- enable

- configure terminal

- voice lpcor enable

- voice lpcor call-block cause cause-code

- voice lpcor custom

- group number lpcor-group

- exit

- voice lpcor policy lpcor-group

- accept lpcor-group

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

voice lpcor enable

#### Example:

```
Router(config)# voice lpcor enable
```

Enables LPCOR
                                             				functionality on the Cisco Unified CME router.

Step 4

voice lpcor call-block cause cause-code

#### Example:

```
Router(config)# voice lpcor call-block cause 79
```

(Optional)
                                             				Defines the cause code to use when a call is blocked because LPCOR validation
                                             				fails.

Range: 1
                                                   					 to 180. Default: 63 (serv/opt-unavail-unspecified). Type ? to display
                                                   					 a description of the cause codes.

Step 5

voice lpcor custom

#### Example:

```
Router(config)# voice lpcor custom
```

Defines the
                                             				name and number of LPCOR resource groups on the Cisco Unified CME router.

Step 6

group number lpcor-group

#### Example:

```
Router(cfg-lpcor-custom)# group 1 pstn_trunk
```

Adds a LPCOR
                                             				resource group to the custom resource list.

number —Group number of the LPCOR entry.
                                                   					 Range: 1 to 64.

lpcor-group —String that identifies the LPCOR
                                                   					 resource group.

Step 7

exit

#### Example:

```
Router(cfg-lpcor-custom)# exit
```

Exits LPCOR
                                             				custom configuration mode.

Step 8

voice lpcor policy lpcor-group

#### Example:

```
Router(config)# voice lpcor policy pstn_trunk
```

Creates a
                                             				LPCOR policy for a resource group.

lpcor-group —Name of the resource group that you
                                                   					 defined in Step 6.

Step 9

accept lpcor-group

#### Example:

```
Router(cfg-lpcor-policy)# accept analog_phone
```

Allows a LPCOR
                                             				policy to accept calls associated with the specified resource group.

Default:
                                                   					 Calls from other groups are rejected; calls from the same resource group are
                                                   					 accepted.

Repeat
                                                   					 this command for each resource group whose calls you want this policy to
                                                   					 accept.

Step 10

end

#### Example:

```
Router(cfg-lpcor-policy)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows a LPCOR configuration where resources are partitioned into five
                                 		  groups. Three of the resource groups have LPCOR policies that limit the calls
                                 		  they can accept. The other two groups, ipphone_local and analog_phone, can
                                 		  accept calls from any of the other resource groups because they do not have a
                                 		  LPCOR policy defined.

```
voice lpcor enable
voice lpcor call-block cause invalid-number
voice lpcor custom
 group 1 pstn_trunk
 group 2 analog_phone
 group 3 iptrunk
 group 4 ipphone_local
 group 5 ipphone_remote
!
voice lpcor policy pstn_trunk
 accept analog_phone
 accept ipphone_local
!
voice lpcor policy iptrunk
 accept analog_phone
 accept ipphone_local
 accept ipphone_remote
!
voice lpcor policy ipphone_remote
 accept iptrunk
 accept analog_phone
 accept ipphone_local
```

siptrunk—Accepts all IP trunk calls.

h323trunk—Accepts all IP trunk calls.

pstn—Blocks
                                          				all IP trunk and voice-mail calls.

voicemail—Accepts both IP trunk and PSTN calls.

```
voice lpcor enable
voice lpcor custom
 group 1 siptrunk
 group 2 h323trunk
 group 3 pstn
 group 4 voicemail
!
voice lpcor policy siptrunk
 accept h323trunk
 accept voicemail
!
voice lpcor policy h323trunk
 accept siptrunk
 accept voicemail
!
voice lpcor policy pstn
!
voice lpcor policy voicemail
 accept siptrunk
 accept h323trunk
 accept pstn
```

The following
                                 		  example shows a LPCOR policy that is configured to reject calls associated with
                                 		  itself. Devices that belong to the local_phone resource group cannot accept
                                 		  calls from each other.

```
voice lpcor policy local_phone
	no accept local_phone
	accept analog_phone
```

### Associate a LPCOR
                           	 Policy with Analog Phone or PSTN Trunk Calls

To associate a
                                 		  LPCOR policy with calls that originate or terminate at an analog phone or PSTN
                                 		  trunk, perform the following task. You can apply a specific LPCOR policy
                                 		  through the voice port or trunk group to remote analog phones or to local
                                 		  analog phones that you do not want to associate with the default LPCOR policy.

For an analog
                                             			 FXS phone that is locally registered to Cisco Unified CME through the LAN, see Associate a LPCOR Policy with IP Phone or SCCP FXS Phone Calls .

Voice port

Trunk group

If the
                                          				outbound dial peer is configured with the port command,
                                          				an outgoing call uses the LPCOR policy specified in the voice port.

If the
                                          				outbound dial-peer is configured with the trunkgroup command, the call uses the LPCOR policy specified in the trunk group.

#### Before you begin

The LPCOR policy
                                 		  must be defined. See Define a LPCOR Policy .

### SUMMARY STEPS

- enable

- configure terminal

- trunk group name

- lpcor incoming lpcor-group

- lpcor outgoing lpcor-group

- exit

- voice-port port

- lpcor incoming lpcor-group

- lpcor outgoing lpcor-group

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

trunk group name

#### Example:

```
Router(config)# trunk group isdn1
```

Enters
                                             				trunk-group configuration mode to define a trunk group.

Step 4

lpcor incoming lpcor-group

#### Example:

```
Router(config-trunk-group)# lpcor incoming isdn_group1
```

Associates a
                                             				LPCOR resource-group policy with an incoming call.

Step 5

lpcor outgoing lpcor-group

#### Example:

```
Router(config-trunk-group)# lpcor outgoing isdn_group1
```

Associates a
                                             				LPCOR resource-group policy with an outgoing call.

Step 6

exit

#### Example:

```
Router(config-trunk-group)# exit
```

Step 7

voice-port port

#### Example:

```
Router(config)# voice-port 0/1/0
```

Enters
                                             				voice-port configuration mode.

Port argument is platform-dependent; type ? to display
                                                   					 syntax.

Step 8

lpcor incoming lpcor-group

#### Example:

```
Router(config-voiceport)# lpcor incoming vp_group3
```

Associates a
                                             				LPCOR resource-group policy with an incoming call.

Step 9

lpcor outgoing lpcor-group

#### Example:

```
Router(config-voiceport)# lpcor outgoing vp_group3
```

Associates a
                                             				LPCOR resource-group policy with an outgoing call.

Step 10

end

#### Example:

```
Router(config-voiceport)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples for
                                 		  Configuring LPCOR for a PSTN Trunk and Analog Phones

The following
                                 		  example shows a configuration for a PSTN trunk. Outbound calls from dial peer
                                 		  201 use LPCOR policy isdn_group1 because dial peer 201 is configured with trunk
                                 		  group isdn1. Outbound calls from dial peer 202 use LPCOR policy vp_group3
                                 		  because dial peer 202 is configured with voice port 3/1:15. A dial peer can be
                                 		  configured with either a voice port or trunk group; it cannot use both.

```
trunk group isdn1
 lpcor incoming isdn_group1
 lpcor outgoing isdn_group1
!
interface Serial2/0:15
 isdn incoming-voice voice
 trunk-group isdn1
...
voice-port 3/1:15
 lpcor incoming vp_group3
 lpcor outgoing vp_group3
!
!
dial-peer voice 201 pots
description TG outbound dial-peer
destination-pattern 201T
trunkgroup isdn1
!
dial-peer voice 202 pots
description VP outbound dial-peer
destination-pattern 202T
port 3/1:15
```

The following
                                 		  example shows a LPCOR configuration for analog phones:

```
trunk group analog1
 lpcor incoming analog_group1
 lpcor outgoing analog_group1
!
voice-port 1/0/0
!
voice-port 1/0/1
!
voice-port 1/1/0
 lpcor incoming vp_group1
 lpcor outgoing vp_group1
!
dial-peer voice 100 pots
 description VP dial-peer
 destination-pattern 100
 port 1/0/0
!
dial-peer voice 101 pots
 description VP dial-peer
 destination-pattern 101
 port 1/0/1
!
dial-peer voice 110 pots
 description VP dial-peer
 destination-pattern 110
 port 1/1/0
!
dial-peer voice 300 pots
 description TG outbound dial-peer
 destination-pattern 300
 trunk-group analog1
```

### Associate a LPCOR
                           	 Policy with VoIP Trunk Calls

To associate a
                                 		  LPCOR policy with calls that originate or terminate at a VoIP trunk (H.323 or
                                 		  SIP), perform the following task.

IP-trunk
                                          				subnet table

Voice service
                                          				voip configuration

Outbound VoIP
                                          				dial peer

Default LPCOR
                                          				policy (no LPCOR policy is applied)

Restriction

The LPCOR IP-trunk subnet table is not supported for calls with an IPv6 address. The LPCOR policy specified with the lpcor incoming command in voice service configuration mode is supported for IPv6 trunk calls.

Only a
                                                      				  single LPCOR policy is applied to outgoing IP trunk calls if the outbound VoIP
                                                      				  dial-peer is configured with the session
                                                            						target command using the sip-server or ras keyword.

If a dial
                                                      				  peer COR and LPCOR are both defined in a dial peer, the dial peer COR
                                                      				  configuration has priority over LPCOR. For example, if the dial peer COR
                                                      				  restricts the call and LPCOR allows the call, the call fails because of the
                                                      				  dial peer COR before ever considering LPCOR.

#### Before you begin

The LPCOR policy
                                 		  must be defined. See Define a LPCOR Policy .

### SUMMARY STEPS

- enable

- configure terminal

- voice lpcor ip-trunk subnet incoming

- index index-number lpcor-group { ipv4-address network-mask | hostname hostname }

- exit

- voice service voip

- lpcor incoming lpcor-group

- exit

- dial-peer voice tag voip

- lpcor outgoing lpcor-group

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

voice lpcor ip-trunk subnet incoming

#### Example:

```
Router(config)# voice lpcor ip-trunk subnet incoming
```

Creates a
                                             				LPCOR IP-trunk subnet table for incoming calls from a VoIP trunk.

Step 4

index index-number lpcor-group { ipv4-address network-mask | hostname hostname }

#### Example:

```
Router(cfg-lpcor-iptrunk-subnet)# index 1 h323_group1 172.19.33.0 255.255.255.0
```

Adds a LPCOR
                                             				resource group to the IP trunk subnet table.

Step 5

exit

#### Example:

```
Router(cfg-lpcor-iptrunk-subnet)# exit
```

Exits LPCOR
                                             				custom configuration mode.

Step 6

voice service voip

#### Example:

```
Router(config)# voice service voip
```

Enters
                                             				voice-service configuration mode to specify the VoIP encapsulation type.

Step 7

lpcor incoming lpcor-group

#### Example:

```
Router(conf-voi-serv)# lpcor incoming voip_trunk_1
```

Associates a
                                             				LPCOR resource-group policy with an incoming call.

Step 8

exit

#### Example:

```
Router(conf-voi-serv)# exit
```

Exits
                                             				voice-service configuration mode.

Step 9

dial-peer voice tag voip

#### Example:

```
Router(config)# dial-peer voice 233 voip
```

Enters
                                             				dial-peer configuration mode to define a dial peer for VoIP calls.

Step 10

lpcor outgoing lpcor-group

#### Example:

```
Router(config-dial-peer)# lpcor outgoing h323_group1
```

Associates a
                                             				LPCOR resource-group policy with an outgoing call.

Step 11

end

#### Example:

```
Router(config-dial-peer)# end
```

Returns to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows a LPCOR configuration for VoIP trunks:

```
voice lpcor ip-trunk subnet incoming
 index 1 h323_group1 172.19.33.0 255.255.255.0
 index 2 sip_group1 172.19.22.0 255.255.255.0
 index 3 sip_group2 hostname sipexample
!
voice service voip
 lpcor incoming voip_trunk_1
!
dial-peer voice 233 voip
 description H323 trunk outbound dial-peer
 destination-pattern 233T
 session target ipv4:172.19.33.233
 lpcor outgoing h323_group1
!
dial-peer voice 2255 voip
 description SIP trunk outbound dial-peer
 destination-pattern 255T
 session protocol sipv2
 session target ipv4:172.19.33.255
 lpcor outgoing sip_group1
```

### Associate a LPCOR
                           	 Policy with IP Phone or SCCP FXS Phone Calls

To associate a
                                 		  LPCOR policy with calls that originate or terminate at a local or remote IP
                                 		  phone or local SCCP analog (FXS) phone, perform the following task.

According to TRAI
                                 		  requirements, an IP phone or a SCCP FXS phone can accept both PSTN and VoIP
                                 		  calls if it is locally registered to Cisco Unified CME through the LAN. If a
                                 		  phone is registered to Cisco Unified CME through the WAN, then PSTN calls must
                                 		  be blocked from that remote phone.

Restriction

Phones that
                                                      				  share a directory number must be configured with the same LPCOR policy. A
                                                      				  warning message displays if you try to configure a different LPCOR policy
                                                      				  between IP phones that share the same directory number.

Local and
                                                      				  remote IP phones cannot use the same LPCOR policy.

Software-based three-party ad hoc conferencing is not supported
                                                      				  on SIP phones.

Hardware-based ad hoc conferening is not supported on SIP
                                                      				  phones.

LPCOR
                                                      				  feature is not supported on voice gateways such as the Cisco VG224 or
                                                      				  Cisco integrated service router if the voice gateway is registered to
                                                      				  Cisco Unified Communications Manager. Cisco Unified Communications Manager does
                                                      				  not support LPCOR.

If a
                                                      				  third-party call-control application makes two separate calls to
                                                      				  Cisco Unified CME and performs a media bridging between the two calls, LPCOR
                                                      				  validation is not supported because Cisco Unified CME is not aware of the
                                                      				  bridging.

#### Before you begin

The LPCOR
                                          				policy must be defined. See Define a LPCOR Policy .

SCCP FXS
                                          				phones are configured with the type anl command.

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag or voice register pool phone-tag

- lpcor type { local | remote }

- lpcor incoming lpcor-group

- lpcor outgoing lpcor-group

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

ephone phone-tag or voice register pool phone-tag

#### Example:

```
Router(config)# ephone 2
```

or

```
Router(config)# voice register pool 4
```

Enters ephone
                                             				configuration mode to set phone-specific parameters for an SCCP phone.

or

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

phone-tag —Unique sequence number that identifies
                                                   					 the phone. Range is version and platform-dependent; type ? to display
                                                   					 range.

Step 4

lpcor type { local | remote }

#### Example:

```
Router(config-ephone)# lpcor type remote
```

or

```
Router(config-register-pool)# lpcor type local
```

Sets the LPCOR
                                             				type for an IP phone.

local —IP phone always registers to
                                                   					 Cisco Unified CME through the LAN.

remote —IP phone always registers to
                                                   					 Cisco Unified CME through the WAN.

This
                                                   					 command can also be configured in ephone-template or voice register template
                                                   					 configuration mode and applied to one or more phones. The phone configuration
                                                   					 has precedence over the template configuration.

Step 5

lpcor incoming lpcor-group

#### Example:

```
Router(config-ephone)# lpcor incoming ephone_group1
```

or

```
Router(config-register-pool)# lpcor incoming remote_group3
```

Associates a
                                             				LPCOR resource-group policy with an incoming call.

If this
                                                   					 phone shares a directory number with another phone, you cannot configure a
                                                   					 LPCOR policy that is different than the LPCOR policy on the other phone.

This
                                                   					 command can also be configured in ephone-template or voice register template
                                                   					 configuration mode and applied to one or more phones. The phone configuration
                                                   					 has precedence over the template configuration.

Step 6

lpcor outgoing lpcor-group

#### Example:

```
Router(config-ephone)# lpcor outgoing ephone_group2
```

or

```
Router(config-register-pool)# lpcor outgoing remote_group3
```

Associates a
                                             				LPCOR resource-group policy with an outgoing call.

If this
                                                   					 phone shares a directory number with another phone, you cannot configure a
                                                   					 LPCOR policy that is different than the LPCOR policy on the other phone.

This
                                                   					 command can also be configured in ephone-template or voice register template
                                                   					 configuration mode and applied to one or more phones. The phone configuration
                                                   					 has precedence over the template configuration.

Step 7

end

#### Example:

```
Router(config-ephone)# end
```

or

```
Router(config-register-pool)# end
```

Returns to
                                             				privileged EXEC mode.

#### Example for
                                 		  Configuring LPCOR on SCCP Phone, SIP Phones, and SCCP FXS Phones

The following
                                 		  example shows a LPCOR configuration for two SCCP phones. One configuration is
                                 		  applied directly to the phone and the other is applied through a phone
                                 		  template:

```
ephone-template 1
 lpcor type local
 lpcor incoming ephone_group1
 lpcor outgoing ephone_group1
!
ephone 1
 mac-address 00E1.CB13.0395
 ephone-template 1
 type 7960
 button 1:1
!
ephone 2
 lpcor type remote
 lpcor incoming ephone_group2
 lpcor outgoing ephone_group2
 mac-address 001C.821C.ED23
 type 7960
 button 1:2
```

The following
                                 		  example shows a LPCOR configuration for two SIP phones:

```
voice register template 1
 lpcor type local
 lpcor incoming test_group
 lpcor outgoing test_group
!
voice register pool 3
 id mac 001B.D584.E80A
 type 7960
 number 1 dn 2
 template 1
 codec g711ulaw
!
voice register pool 4
 lpcor type remote
 lpcor incoming remote_group3
 lpcor outgoing remote_group3
 id mac 0030.94C2.9A55
 type 7960
 number 1 dn 2
 dtmf-relay rtp-nt
```

The following
                                 		  example shows a LPCOR configuration for two SCCP FXS phones connected to a
                                 		  Cisco VG224 and controlled by Cisco Unified CME:

```
dial-peer voice 102 pots
 service stcapp
 port 1/0/2
!
ephone 5
 lpcor type local
 lpcor incoming analog_vg224
 lpcor outgoing analog_vg224
 mac-address F9E5.8B28.2402
 ephone-template 1
 max-calls-per-button 2
 type anl
 button 1:5
!
ephone 6
 lpcor type local
 lpcor incoming analog_vg224
 lpcor outgoing analog_vg224
 mac-address F9E5.8B28.2403
 ephone-template 1
 max-calls-per-button 2
 type anl
 button 1:6
```

SCCP FXS
                                    			 Phones Managed by Cisco Unified CME shows an example of a network with SCCP FXS phones managed by
                                 		  Cisco Unified CME.

### Associate LPCOR
                           	 with Mobile Phone Calls

To associate a
                                 		  LPCOR policy with calls that originate or terminate at a mobile-type phone,
                                 		  perform the following task.

A mobile-type
                                 		  phone can register to Cisco Unified CME through either the LAN or WAN. For
                                 		  example an Extension Mobility phone, Cisco IP Communicator softphone, or a
                                 		  remote teleworker phone.

IP-phone
                                          				subnet table

Default LPCOR
                                          				policy for mobile-type phones

Restriction

The LPCOR
                                             			 IP-phone subnet table is not supported for calls with an IPv6 address.

#### Before you begin

The LPCOR policy
                                 		  must be defined. See Define a LPCOR Policy .

### SUMMARY STEPS

- enable

- configure terminal

- ephone phone-tag or voice register pool phone-tag

- lpcor type mobile

- exit

- voice lpcor ip-phone subnet { incoming | outgoing }

- index index-number lpcor-group { ipv4-address network-mask [ vrf vrf-name ] | dhcp-pool pool-name }

- exit

- voice lpcor ip-phone mobility { incoming | outgoing } lpcor-group

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

ephone phone-tag or voice register pool phone-tag

#### Example:

```
Router(config)# ephone 1
```

or

```
Router(config)# voice register pool 1
```

Enters ephone
                                             				configuration mode to set phone-specific parameters for an SCCP phone.

or

Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone.

phone-tag —Unique sequence number that identifies
                                                   					 the phone. Range is version and platform-dependent; type ? to display
                                                   					 range.

Step 4

lpcor type mobile

#### Example:

```
Router(config-ephone)# lpcor type mobile
```

Sets the LPCOR
                                             				type for a mobile-type phone.

This
                                                   					 command can also be configured in ephone-template or voice register template
                                                   					 configuration mode and applied to one or more phones. The phone configuration
                                                   					 has precedence over the template configuration.

Step 5

exit

#### Example:

```
Router(config-ephone)# exit
```

Exits the
                                             				phone configuration.

Step 6

voice lpcor ip-phone subnet { incoming | outgoing }

#### Example:

```
Router(config)# voice lpcor ip-phone subnet incoming
```

Creates a
                                             				LPCOR IP-phone subnet table for calls to or from a mobile-type phone.

Step 7

index index-number lpcor-group { ipv4-address network-mask [ vrf vrf-name ] | dhcp-pool pool-name }

#### Example:

```
Router(cfg-lpcor-ipphone-subnet)# index 1 local_group1 dhcp-pool pool1
```

Adds a LPCOR
                                             				group to the IP-phone subnet table.

Step 8

exit

#### Example:

```
Router(cfg-lpcor-ipphone-subnet)# exit
```

Exits LPCOR
                                             				IP-phone configuration mode.

Step 9

voice lpcor ip-phone mobility { incoming | outgoing } lpcor-group

#### Example:

```
Router(config)# voice lpcor ip-phone mobility incoming remote_group1
```

Sets the default LPCOR policy for mobile-type phones.

Step 10

exit

#### Example:

```
Router(config)# exit
```

Exits to
                                             				privileged EXEC mode.

#### Examples

The following
                                 		  example shows the configuration for three mobile-type phones:

```
ephone 270
 lpcor type mobile
 mac-address 1234.4321.6000
 type 7960
 button 1:6
 mtp
 codec g729r8 dspfarm-assist
 description teleworker remote phone
ephone 281
 lpcor type mobile
 mac-address 0003.4713.5554
 type CIPC
 button 1:5
...
voice register pool 6
 lpcor type mobile
 id mac 0030.94C2.9A66
 type 7960
 number 1 dn 3
 dtmf-relay rtp-nte
```

The following
                                 		  example shows a LPCOR IP-phone subnet configuration with a single shared IP
                                 		  address pool. Any mobile-type IP phones with a shared IP address from DHCP
                                 		  pool1 are considered local IP phones and are associated with the local_group1
                                 		  LPCOR policy. Other mobile-type IP phones without a shared IP address are
                                 		  considered remote IP phones and are associated with remote_group1, the default
                                 		  LPCOR policy for mobile-type phones.

```
ip dhcp pool pool1
	network 10.0.0.0 255.255.0.0
	option 150 ip 10.0.0.1
	default-router 10.0.0.1
!
!
voice lpcor ip-phone subnet incoming
	index 1 local_group1 dhcp-pool pool1
!
voice lpcor ip-phone subnet outgoing
	index 1 local_group1 dhcp-pool pool1
!
voice lpcor ip-phone mobility incoming remote_group1
	voice lpcor ip-phone mobility outgoing remote_group1
```

The following
                                 		  example shows a LPCOR IP-phone subnet configuration with a separate IP address
                                 		  DHCP pools. Any mobile-type IP phones with separate DHCP pools are considered
                                 		  local IP phones and are assigned the local_group1 LPCOR policy. Other
                                 		  mobile-type IP phones without a DHCP address are considered remote IP phones
                                 		  and are assigned the remote_group1 LPCOR policy.

```
ip dhcp pool client1
 network 10.0.0.0 255.255.0.0
 mac-address 0003.4713.5554
 option 150 ip 10.0.0.1
 default-router 10.0.0.1
!
ip dhcp pool client2
   network 10.0.0.0 255.255.0.0
   mac-address 0030.94C2.9A66
   option 150 ip 10.0.0.1
   default-router 10.0.0.1
!
!
voice lpcor ip-phone subnet incoming
 index 1 local_group1 dhcp-pool client1
 index 2 local_group1 dhcp-pool client2
!
voice lpcor ip-phone subnet outgoing
 index 1 local_group1 dhcp-pool client1
 index 2 local_group1 dhcp-pool client2
!
voice lpcor ip-phone mobility incoming remote_group1
voice lpcor ip-phone mobility outgoing remote_group1
```

The following
                                 		  example shows a LPCOR IP phone subnet configuration with both an IP address
                                 		  network mask and a single shared-address DHCP pool. A specific LPCOR policy can
                                 		  be associated with an IP phone by matching the IP address network mask in the
                                 		  IP-phone subnet table. LPCOR policy local_group2 is associated with the local
                                 		  IP phone with IP address 10.0.10.23. LPCOR local_group2 is associated with the
                                 		  other local IP phones through the DHCP-pool match.

```
ip dhcp pool pool1
   network 10.0.0.0 255.255.0.0
   option 150 ip 10.0.0.1
   default-router 10.0.0.1
!
!
voice lpcor ip-phone subnet incoming
 index 1 local_g2 10.0.10.23 255.255.255.0 vrf vrf-group2
 index 2 remote_g2 172.19.0.0 255.255.0.0
 index 3 local_g1 dhcp-pool pool1
!
voice lpcor ip-phone subnet outgoing
index 1 local_g4 10.1.10.23 255.255.255.0 vrf vrf-group2
index 2 remote_g4 172.19.0.0 255.255.0.0
index 3 local_g5 dhcp-pool pool1
!
voice lpcor ip-phone mobility incoming remote_g1
voice lpcor ip-phone mobility outgoing remote_g1
```

### Verify LPCOR Configuration

Use the following show commands to display LPCOR configuration
                              		information and to verify the LPCOR policy associated with calls.

show call active voice —Displays the LPCOR
                                    			 information for incoming and outgoing call legs (VoIP, ephone, SIP, PSTN).

show call history voice —Displays the LPCOR
                                    			 information for incoming and outgoing call legs (VoIP, ephone, SIP, PSTN). Also
                                    			 displays the LPCOR call-block cause code if the call is blocked due to LPCOR
                                    			 policy validation.

show dial-peer voice —Displays
                                    			 configuration settings for voice dial peers including the LPCOR setting for
                                    			 incoming and outgoing calls.

show trunk group —Displays configuration
                                    			 settings for trunk groups including the LPCOR setting for incoming and outgoing
                                    			 calls.

show voice lpcor —Displays information
                                    			 about LPCOR calls including the LPCOR policy associated with each resource
                                    			 group and directory number, and statistics for failed calls.

show voice port —Displays configuration
                                    			 settings for voice ports including the LPCOR setting for incoming and outgoing
                                    			 calls.

## Configuration Examples for LPCOR

### Example for
                           	 Configuring LPCOR for Cisco Unified CME

local_group—Analog and IP phones, including a mobile-type phone,
                                          				connected locally to Cisco Unified CME.

pstn_group—Trunks between the PSTN and Cisco Unified CME.

remote_group—IP phones, including a mobile-type phone, and a SIP
                                          				proxy server connected remotely to Cisco Unified CME through the WAN.

voice_mail_group—Cisco Unity Express voice-mail system connected
                                          				remotely to Cisco Unified CME through the WAN.

Blocks calls
                                          				between remote_group and pstn_group

Blocks calls
                                          				from voice_mail_group to pstn_group and remote_group

Allows calls
                                          				between local_group and remote_group

Allows calls
                                          				between local_group and pstn_group

Allows all
                                          				calls to voice_mail_group

The following
                                 		  output shows the LPCOR configuration for this example and describes the steps.
                                 		  Comments describing the configuration are included in the output.

Enable LPCOR
                                       				functionality in Cisco Unified CME and define custom LPCOR group.

```
voice lpcor enable 
!
voice lpcor custom 
	group 1 pstn_group 
	group 2 local_group 
	group 3 remote_group 
	group 4 voice_mail_group 
	! 
	#Allow calls only from local group to PSTN group 
	voice lpcor policy pstn_group 
	 accept local_group 
	! 
	# Allow calls from PSTN, remote, and voice_mail groups to local group 
	voice lpcor policy local_group 
		accept pstn_group 
		accept remote_group 
		accept voice_mail_group 
	! 
	# Allow calls only from local group to remote group 
	voice lpcor policy remote_group 
		accept local_group 
	! 
	# Allow calls from PSTN, remote, and local groups to voice_mail group 
	voice lpcor voice_mail_group 
	 accept pstn_group
	 accept local_group 
	 accept remote_group 
	!
```

Assign LPCOR
                                       				to the phone, trunk, and IP resources.

```
# analog phone5
voice-port 1/0/0
 lpcor incoming local_group
 lpcor outgoing local_group
!
# analog phone6
voice-port 1/0/1
 lpcor incoming local_group
 lpcor outgoing local_group
!
# TDM trunks
voice-port 2/1:23
 lpcor incoming pstn_group
 lpcor outgoing pstn_group
!
!
# Specific LPCOR setting for incoming calls from voice_mail_group
voice lpcor ip-trunk subnet incoming
 voice_mail_group 172.19.28.11 255.255.255.255
!
!
# Default LPCOR setting for any incoming VoIP calls
voice service voip
 lpcor incoming remote_group
!
# Cisco Unified CME is DHCP server
ip dhcp pool client1
 network 10.0.0.0 255.255.0.0
 mac-address 0003.4713.5554
  option 150 ip 10.0.0.1
default-router 10.0.0.1
!
# IP phone1 (local)
ephone 1
 lpcor type local
 lpcor incoming local_group
 lpcor outgoing local_group
!
# IP phone2 (mobile)
ephone 2
 lpcor type mobile
!
# IP phone3 (remote)
ephone 3
 lpcor type remote
 lpcor incoming remote_group
 lpcor outgoing remote_group
!
# IP phone4 (mobile)
ephone 4
 lpcor type mobile
!
# IP-phone subnet tables for mobile IP phones
voice lpcor ip-phone subnet incoming
 local_group dhcp-pool pool1
!
voice lpcor ip-phone subnet outgoing
 local_group dhcp-pool client1
!
# Default LPCOR policy for mobile IP phones that
# are not provisioned through IP-phone subnet tables
voice lpcor ip-phone mobility incoming remote_group
voice lpcor ip-phone mobility outgoing remote_group
```

Define
                                       				outgoing LPCOR setting for outgoing VoIP calls.

```
# VoIP outbound dial-peer to Cisco Unity Express mail
dial-peer voice 1234 voip
 destination-pattern 56800
 session target ipv4:172.19.281.1
 pcor outgoing voice_mail_group
!
# VoIP outbound dial-peer to SIP proxy
dial-peer voice 1255 voip
 destination-pattern 1255T
 session protocol sipv2
 session target sip-server
 lpcor outgoing remote
```

### Example for Configuring LPCOR on Cisco 3800 Series Integrated Services
                           	 Router

```
Router# show running-config
 
Building configuration...
 
 
Current configuration : 10543 bytes
!
version 12.4
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname Router
!
boot-start-marker
boot-end-marker
!
card type t1 2 1
logging message-counter syslog
logging buffered 2000000
no logging console
!
no aaa new-model
network-clock-participate slot 2 
!
ip source-route
ip cef
!
!
ip dhcp excluded-address 192.168.20.1
ip dhcp excluded-address 192.168.20.1 192.168.20.5
!
ip dhcp pool voice
   network 192.168.20.0 255.255.255.0
   option 150 ip 192.168.20.1 
   default-router 192.168.20.1 
!
!
no ip domain lookup
no ipv6 cef
multilink bundle-name authenticated
!
!
isdn switch-type primary-5ess
!
voice-card 0
!
voice-card 2
!
!
voice service voip 
 notify redirect ip2pots
 allow-connections sip to sip
 sip
  bind control source-interface GigabitEthernet0/1
  bind media source-interface GigabitEthernet0/1
  registrar server expires max 120 min 60
!
!
!
voice class custom-cptone leavetone
 dualtone conference
  frequency 400 800
  cadence 400 50 200 50 200 50
!
voice class custom-cptone jointone
 dualtone conference
  frequency 600 900
  cadence 300 150 300 100 300 50
!
!
voice iec syslog
voice register global
 mode cme
 source-address 192.168.20.1 port 5060
 max-dn 20
 max-pool 20
 load 7970 SIP70.8-4-2S
 load 7960-7940 P0S3-08-11-00
 authenticate realm cisco.com
 tftp-path flash:
 telnet level 2
 create profile sync 0000312474383825
!
voice register dn  1
 number 4000
 name cme-sip1
 label 4000
!
voice register dn  2
 number 4001
 name cme-sip-2
 label 4001
!
voice register dn  3
 number 4002
 name cme-remote
 label 4002
!
voice register template  1
 softkeys remote-in-use  cBarge Barge Newcall
!
voice register pool  1
 lpcor type local
 lpcor incoming local_sip
 lpcor outgoing local_sip
 id mac 001B.D4C6.AE44
 type 7960
 number 1 dn 1
 dtmf-relay rtp-nte
 codec g711ulaw
!
voice register pool  2
 lpcor type local
 lpcor incoming local_sip
 lpcor outgoing local_sip
 id mac 001E.BE8F.96C1
 type 7940
 number 1 dn 2
 dtmf-relay rtp-nte
 codec g711ulaw
!
voice register pool  3
 lpcor type remote
 lpcor incoming remote_sip
 lpcor outgoing remote_sip
 id mac 001E.BE8F.96C0
 type 7940
 number 1 dn 3
 dtmf-relay rtp-nte
 codec g711ulaw
!
!
voice lpcor enable
voice lpcor call-block cause invalid-number
voice lpcor custom
 group 1 voip_siptrunk
 group 2 voip_h323trunk
 group 3 pstn_trunk
 group 4 cue_vmail_local
 group 5 cue_vmail_remote
 group 6 vmail_unity
 group 7 local_sccp
 group 8 local_sip
 group 9 remote_sccp
 group 10 remote_sip
 group 11 analog_vg224
 group 12 analog_fxs
 group 13 mobile_phone
!
voice lpcor policy voip_siptrunk
 accept cue_vmail_local
 accept local_sccp
 accept local_sip
 accept analog_vg224
!
voice lpcor policy cue_vmail_local
 accept voip_siptrunk
 accept voip_h323trunk
 accept local_sccp
 accept local_sip
!
voice lpcor policy local_sccp
 accept local_sip
 accept remote_sccp
 accept remote_sip
 accept analog_vg224
 accept analog_fxs
!
voice lpcor policy remote_sccp
 accept local_sccp
 accept local_sip
 accept remote_sip
!
voice lpcor policy analog_vg224
 accept local_sccp
 accept local_sip
 accept remote_sccp
 accept remote_sip
!
voice lpcor policy analog_fxs
 accept local_sccp
 accept local_sip
!
voice lpcor ip-phone subnet incoming
 index 1 local_sccp dhcp-pool voice
!
voice lpcor ip-phone subnet outgoing
 index 1 local_sccp dhcp-pool voice
!
!
!
archive
 log config
  hidekeys
!
!
controller T1 2/0
 cablelength short 133
 pri-group timeslots 1-24
!
controller T1 2/1
!
!
interface Loopback1
 ip address 192.168.21.1 255.255.255.0
 ip ospf network point-to-point
!
interface GigabitEthernet0/0
 ip address 192.168.160.1 255.255.255.0
 duplex auto
 speed auto
 media-type rj45
!
interface GigabitEthernet0/1
 ip address 192.168.20.1 255.255.255.0
 duplex auto
 speed auto
 media-type rj45
!
interface FastEthernet0/2/0
 ip address 192.168.98.1 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/2/1
 no ip address
 duplex auto
 speed auto
!
interface Service-Engine1/0
 ip unnumbered Loopback1
 service-module ip address 192.168.21.100 255.255.255.0
 service-module ip default-gateway 192.168.21.1
!
interface Serial2/0:23
 no ip address
 encapsulation hdlc
 isdn switch-type primary-5ess
 isdn incoming-voice voice
 no cdp enable
!
router ospf 1
 log-adjacency-changes
 network 192.168.160.0 0.0.0.255 area 0
 network 192.168.20.0 0.0.0.255 area 0
 network 192.168.21.0 0.0.0.255 area 0
!
ip forward-protocol nd
ip route 192.168.21.100 255.255.255.255 Service-Engine1/0
!
!
no ip http server
!
!
tftp-server flash:term41.default.loads
tftp-server flash:term61.default.loads
tftp-server flash:SCCP41.8-3-1S.loads
tftp-server flash:apps41.8-3-0-50.sbn
tftp-server flash:cnu41.8-3-0-50.sbn
tftp-server flash:P003-08-11-00.bin
tftp-server flash:P003-08-11-00.sbn
tftp-server flash:P0S3-08-11-00.sb2
tftp-server flash:P0S3-08-11-00.loads
tftp-server flash:term71.default.loads
tftp-server flash:term70.default.loads
tftp-server flash:jar70sccp.8-2-2TR2.sbn
tftp-server flash:dsp70.8-2-2TR2.sbn
tftp-server flash:cvm70sccp.8-2-2TR2.sbn
tftp-server flash:apps70.8-2-2TR2.sbn
tftp-server flash:SCCP70.8-2-2SR2S.loads
!
control-plane
!
!
voice-port 0/1/0
 lpcor incoming analog_fxs
 lpcor outgoing analog_fxs
 station-id name FXS-Phone
 station-id number 3000
 caller-id enable
!
voice-port 0/1/1
!
voice-port 2/0:23
!
ccm-manager fax protocol cisco
!
mgcp fax t38 ecm
!
!
!
dial-peer voice 2 voip
 destination-pattern 2...
 lpcor outgoing voip_siptrunk
 session protocol sipv2
 session target ipv4:192.168.97.1
 codec g711ulaw
 ip qos dscp cs5 media
 ip qos dscp cs4 signaling
!
dial-peer voice 5050 voip
 description *** VMAIL Dial-Peer ***
 destination-pattern 5...
 lpcor outgoing cue_vmail_local
 session protocol sipv2
 session target ipv4:192.168.21.100
 dtmf-relay sip-notify
 codec g711ulaw
 no vad
!
dial-peer voice 30 pots
 destination-pattern 3000
 direct-inward-dial
 port 0/1/0
!
!
sip-ua 
 mwi-server ipv4:192.168.21.100 expires 3600 port 5060 transport udp 
 registrar ipv4:192.168.21.1 expires 3600
!
!
telephony-service
 em logout 0:0 0:0 0:0 
 max-ephones 15
 max-dn 15
 ip source-address 192.168.20.1 port 2000
 service phone videoCapability 1
 load 7941 SCCP41.8-3-1S
 date-format dd-mm-yy
 voicemail 5050
 max-conferences 12 gain -6
 transfer-system full-consult
 transfer-pattern .T
 transfer-pattern ....
 fac standard
 create cnf-files version-stamp Jan 01 2002 00:00:00
!
!
ephone-template  1
 softkeys hold  Join Newcall Resume Select
 softkeys idle  Cfwdall ConfList Dnd Join Newcall Pickup Redial RmLstC
 softkeys seized  Endcall Redial Cfwdall Pickup
!
!
ephone-template  2
 lpcor type remote
 lpcor incoming remote_sccp
 lpcor outgoing remote_sccp
!
!
ephone-dn  1  dual-line
 number 5000
 call-forward busy 5050
 call-forward noan 5050 timeout 10
 mwi sip
!
!
ephone-dn  2  dual-line
 number 5001
 call-forward busy 5050
 call-forward noan 5050 timeout 10
 mwi sip
!
!
ephone-dn  3  dual-line
 number 5010
 description vg224-1/1
 name analog-1
!
!
ephone-dn  4  dual-line
 number 5011
 description vg224-1/2
 name analog-2
!
!
ephone-dn  5  dual-line
 number 5012
 description vg224-1/3
 name analog-3
!
!
ephone-dn  6  dual-line
 number 5013
 description vg224-1/4
 name analog-4
!
!
ephone-dn  7  dual-line
 number 5020
 name SCCP-Remote
 mwi sip
!
!
ephone  1
 lpcor type local
 lpcor incoming local_sccp
 lpcor outgoing local_sccp
 mac-address 001E.7A26.EB60
 ephone-template 1
 type 7941
 button  1:1
!
!
!
ephone  2
 lpcor type local
 lpcor incoming local_sccp
 lpcor outgoing local_sccp
 mac-address 001E.7AC2.CCF9
 ephone-template 1
 type 7941
 button  1:2
!
!
!
ephone  3 
 lpcor type local
 lpcor incoming analog_vg224
 lpcor outgoing analog_vg224
 mac-address F9E5.8B28.2400
 ephone-template 1
 max-calls-per-button 2
 type anl
 button  1:3
!
!
!
ephone  4
 lpcor type local
 lpcor incoming analog_vg224
 lpcor outgoing analog_vg224
 mac-address F9E5.8B28.2401
 ephone-template 1
 max-calls-per-button 2
 type anl
 button  1:4
!
!
!
ephone  5
 lpcor type local
 lpcor incoming analog_vg224
 lpcor outgoing analog_vg224
 mac-address F9E5.8B28.2402
 ephone-template 1
 max-calls-per-button 2
 type anl
 button  1:5
!
!
!
ephone  6
 lpcor type local
 lpcor incoming analog_vg224
 lpcor outgoing analog_vg224
 mac-address F9E5.8B28.2403
 ephone-template 1
 max-calls-per-button 2
 type anl
 button  1:6
!
!
!
ephone  7
 mac-address 001B.D52C.DF1F
 ephone-template 2
 type 7970
 button  1:7
!
!
alias exec cue ser ser 1/0 sess
!
line con 0
line aux 0
line 66
 no activation-character
 no exec
 transport preferred none
 transport input all
 transport output pad telnet rlogin lapb-ta mop udptn v120
line vty 0 4
 login
!
exception data-corruption buffer truncate
scheduler allocate 20000 1000
endRouter# show running-config
 
Building configuration...
 
 
Current configuration : 10543 bytes
!
version 12.4
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname Router
!
boot-start-marker
boot-end-marker
!
card type t1 2 1
logging message-counter syslog
logging buffered 2000000
no logging console
!
no aaa new-model
network-clock-participate slot 2 
!
ip source-route
ip cef
!
!
ip dhcp excluded-address 192.168.20.1
ip dhcp excluded-address 192.168.20.1 192.168.20.5
!
ip dhcp pool voice
   network 192.168.20.0 255.255.255.0
   option 150 ip 192.168.20.1 
   default-router 192.168.20.1 
!
!
no ip domain lookup
no ipv6 cef
multilink bundle-name authenticated
!
!
isdn switch-type primary-5ess
!
voice-card 0
!
voice-card 2
!
!
voice service voip 
 notify redirect ip2pots
 allow-connections sip to sip
 sip
  bind control source-interface GigabitEthernet0/1
  bind media source-interface GigabitEthernet0/1
  registrar server expires max 120 min 60
!
!
!
voice class custom-cptone leavetone
 dualtone conference
  frequency 400 800
  cadence 400 50 200 50 200 50
!
voice class custom-cptone jointone
 dualtone conference
  frequency 600 900
  cadence 300 150 300 100 300 50
!
!
voice iec syslog
voice register global
 mode cme
 source-address 192.168.20.1 port 5060
 max-dn 20
 max-pool 20
 load 7970 SIP70.8-4-2S
 load 7960-7940 P0S3-08-11-00
 authenticate realm cisco.com
 tftp-path flash:
 telnet level 2
 create profile sync 0000312474383825
!
voice register dn  1
 number 4000
 name cme-sip1
 label 4000
!
voice register dn  2
 number 4001
 name cme-sip-2
 label 4001
!
voice register dn  3
 number 4002
 name cme-remote
 label 4002
!
voice register template  1
 softkeys remote-in-use  cBarge Barge Newcall
!
voice register pool  1
 lpcor type local
 lpcor incoming local_sip
 lpcor outgoing local_sip
 id mac 001B.D4C6.AE44
 type 7960
 number 1 dn 1
 dtmf-relay rtp-nte
 codec g711ulaw
!
voice register pool  2
 lpcor type local
 lpcor incoming local_sip
 lpcor outgoing local_sip
 id mac 001E.BE8F.96C1
 type 7940
 number 1 dn 2
 dtmf-relay rtp-nte
 codec g711ulaw
!
voice register pool  3
 lpcor type remote
 lpcor incoming remote_sip
 lpcor outgoing remote_sip
 id mac 001E.BE8F.96C0
 type 7940
 number 1 dn 3
 dtmf-relay rtp-nte
 codec g711ulaw
!
!
voice lpcor enable
voice lpcor call-block cause invalid-number
voice lpcor custom
 group 1 voip_siptrunk
 group 2 voip_h323trunk
 group 3 pstn_trunk
 group 4 cue_vmail_local
 group 5 cue_vmail_remote
 group 6 vmail_unity
 group 7 local_sccp
 group 8 local_sip
 group 9 remote_sccp
 group 10 remote_sip
 group 11 analog_vg224
 group 12 analog_fxs
 group 13 mobile_phone
!
voice lpcor policy voip_siptrunk
 accept cue_vmail_local
 accept local_sccp
 accept local_sip
 accept analog_vg224
!
voice lpcor policy cue_vmail_local
 accept voip_siptrunk
 accept voip_h323trunk
 accept local_sccp
 accept local_sip
!
voice lpcor policy local_sccp
 accept local_sip
 accept remote_sccp
 accept remote_sip
 accept analog_vg224
 accept analog_fxs
!
voice lpcor policy remote_sccp
 accept local_sccp
 accept local_sip
 accept remote_sip
!
voice lpcor policy analog_vg224
 accept local_sccp
 accept local_sip
 accept remote_sccp
 accept remote_sip
!
voice lpcor policy analog_fxs
 accept local_sccp
 accept local_sip
!
voice lpcor ip-phone subnet incoming
 index 1 local_sccp dhcp-pool voice
!
voice lpcor ip-phone subnet outgoing
 index 1 local_sccp dhcp-pool voice
!
!
!
archive
 log config
  hidekeys
!
!
controller T1 2/0
 cablelength short 133
 pri-group timeslots 1-24
!
controller T1 2/1
!
!
interface Loopback1
 ip address 192.168.21.1 255.255.255.0
 ip ospf network point-to-point
!
interface GigabitEthernet0/0
 ip address 192.168.160.1 255.255.255.0
 duplex auto
 speed auto
 media-type rj45
!
interface GigabitEthernet0/1
 ip address 192.168.20.1 255.255.255.0
 duplex auto
 speed auto
 media-type rj45
!
interface FastEthernet0/2/0
 ip address 192.168.98.1 255.255.255.0
 duplex auto
 speed auto
!
interface FastEthernet0/2/1
 no ip address
 duplex auto
 speed auto
!
interface Service-Engine1/0
 ip unnumbered Loopback1
 service-module ip address 192.168.21.100 255.255.255.0
 service-module ip default-gateway 192.168.21.1
!
interface Serial2/0:23
 no ip address
 encapsulation hdlc
 isdn switch-type primary-5ess
 isdn incoming-voice voice
 no cdp enable
!
router ospf 1
 log-adjacency-changes
 network 192.168.160.0 0.0.0.255 area 0
 network 192.168.20.0 0.0.0.255 area 0
 network 192.168.21.0 0.0.0.255 area 0
!
ip forward-protocol nd
ip route 192.168.21.100 255.255.255.255 Service-Engine1/0
!
!
no ip http server
!
!
tftp-server flash:term41.default.loads
tftp-server flash:term61.default.loads
tftp-server flash:SCCP41.8-3-1S.loads
tftp-server flash:apps41.8-3-0-50.sbn
tftp-server flash:cnu41.8-3-0-50.sbn
tftp-server flash:P003-08-11-00.bin
tftp-server flash:P003-08-11-00.sbn
tftp-server flash:P0S3-08-11-00.sb2
tftp-server flash:P0S3-08-11-00.loads
tftp-server flash:term71.default.loads
tftp-server flash:term70.default.loads
tftp-server flash:jar70sccp.8-2-2TR2.sbn
tftp-server flash:dsp70.8-2-2TR2.sbn
tftp-server flash:cvm70sccp.8-2-2TR2.sbn
tftp-server flash:apps70.8-2-2TR2.sbn
tftp-server flash:SCCP70.8-2-2SR2S.loads
!
control-plane
!
!
voice-port 0/1/0
 lpcor incoming analog_fxs
 lpcor outgoing analog_fxs
 station-id name FXS-Phone
 station-id number 3000
 caller-id enable
!
voice-port 0/1/1
!
voice-port 2/0:23
!
ccm-manager fax protocol cisco
!
mgcp fax t38 ecm
!
!
!
dial-peer voice 2 voip
 destination-pattern 2...
 lpcor outgoing voip_siptrunk
 session protocol sipv2
 session target ipv4:192.168.97.1
 codec g711ulaw
 ip qos dscp cs5 media
 ip qos dscp cs4 signaling
!
dial-peer voice 5050 voip
 description *** VMAIL Dial-Peer ***
 destination-pattern 5...
 lpcor outgoing cue_vmail_local
 session protocol sipv2
 session target ipv4:192.168.21.100
 dtmf-relay sip-notify
 codec g711ulaw
 no vad
!
dial-peer voice 30 pots
 destination-pattern 3000
 direct-inward-dial
 port 0/1/0
!
!
sip-ua 
 mwi-server ipv4:192.168.21.100 expires 3600 port 5060 transport udp 
 registrar ipv4:192.168.21.1 expires 3600
!
!
telephony-service
 em logout 0:0 0:0 0:0 
 max-ephones 15
 max-dn 15
 ip source-address 192.168.20.1 port 2000
 service phone videoCapability 1
 load 7941 SCCP41.8-3-1S
 date-format dd-mm-yy
 voicemail 5050
 max-conferences 12 gain -6
 transfer-system full-consult
 transfer-pattern .T
 transfer-pattern ....
 fac standard
 create cnf-files version-stamp Jan 01 2002 00:00:00
!
!
ephone-template  1
 softkeys hold  Join Newcall Resume Select
 softkeys idle  Cfwdall ConfList Dnd Join Newcall Pickup Redial RmLstC
 softkeys seized  Endcall Redial Cfwdall Pickup
!
!
ephone-template  2
 lpcor type remote
 lpcor incoming remote_sccp
 lpcor outgoing remote_sccp
!
!
ephone-dn  1  dual-line
 number 5000
 call-forward busy 5050
 call-forward noan 5050 timeout 10
 mwi sip
!
!
ephone-dn  2  dual-line
 number 5001
 call-forward busy 5050
 call-forward noan 5050 timeout 10
 mwi sip
!
!
ephone-dn  3  dual-line
 number 5010
 description vg224-1/1
 name analog-1
!
!
ephone-dn  4  dual-line
 number 5011
 description vg224-1/2
 name analog-2
!
!
ephone-dn  5  dual-line
 number 5012
 description vg224-1/3
 name analog-3
!
!
ephone-dn  6  dual-line
 number 5013
 description vg224-1/4
 name analog-4
!
!
ephone-dn  7  dual-line
 number 5020
 name SCCP-Remote
 mwi sip
!
!
ephone  1
 lpcor type local
 lpcor incoming local_sccp
 lpcor outgoing local_sccp
 mac-address 001E.7A26.EB60
 ephone-template 1
 type 7941
 button  1:1
!
!
!
ephone  2
 lpcor type local
 lpcor incoming local_sccp
 lpcor outgoing local_sccp
 mac-address 001E.7AC2.CCF9
 ephone-template 1
 type 7941
 button  1:2
!
!
!
ephone  3 
 lpcor type local
 lpcor incoming analog_vg224
 lpcor outgoing analog_vg224
 mac-address F9E5.8B28.2400
 ephone-template 1
 max-calls-per-button 2
 type anl
 button  1:3
!
!
!
ephone  4
 lpcor type local
 lpcor incoming analog_vg224
 lpcor outgoing analog_vg224
 mac-address F9E5.8B28.2401
 ephone-template 1
 max-calls-per-button 2
 type anl
 button  1:4
!
!
!
ephone  5
 lpcor type local
 lpcor incoming analog_vg224
 lpcor outgoing analog_vg224
 mac-address F9E5.8B28.2402
 ephone-template 1
 max-calls-per-button 2
 type anl
 button  1:5
!
!
!
ephone  6
 lpcor type local
 lpcor incoming analog_vg224
 lpcor outgoing analog_vg224
 mac-address F9E5.8B28.2403
 ephone-template 1
 max-calls-per-button 2
 type anl
 button  1:6
!
!
!
ephone  7
 mac-address 001B.D52C.DF1F
 ephone-template 2
 type 7970
 button  1:7
!
!
alias exec cue ser ser 1/0 sess
!
line con 0
line aux 0
line 66
 no activation-character
 no exec
 transport preferred none
 transport input all
 transport output pad telnet rlogin lapb-ta mop udptn v120
line vty 0 4
 login
!
exception data-corruption buffer truncate
scheduler allocate 20000 1000
end
```

## Feature
                        	 Information for LPCOR

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Cisco Unified CME Version

Feature Information

Call Restriction Regulations for Cisco Unified CME

8.0

Introduced support for LPCOR feature.

| Resource Groups | RG1 | RG2 | RG3 | RG4 | RG5 |
|---|---|---|---|---|---|
| RG1 | Yes | No | Yes | No | Yes |
| RG2 | Yes | Yes | No | Yes | No |
| RG3 | Yes | Yes | Yes | Yes | No |
| RG4 | No | No | No | Yes | Yes |
| RG5 | No | Yes | Yes | Yes | No |

| Feature | Description | SCCP Phone | SIP Phone |
|---|---|---|---|
| Basic Call | Cisco Unified CME invokes the LPCOR policy validation if both
                                             				  the incoming call and target destination are associated with a LPCOR policy. If the LPCOR
                                             				  policy validation fails, cause-code 63 (no service available) or the
                                             				  user-defined cause-code is returned to the remote switch. The call can hunt to
                                             				  the next destination. | Yes | Yes |
| Call Forward | When a call
                                             				  is forwarded to a new destination, Cisco Unified CME invokes the LPCOR policy
                                             				  validation between the source and the forwarding target. The call is not
                                             				  forwarded to the target if the LPCOR policy is restricted. | Yes | Yes |
| Call
                                             				  Transfer | Blind and
                                             				  Consultative Call Transfer is restricted if the LPCOR policy validation fails
                                             				  between the transferee and transfer-to parties. For
                                             				  consultative call transfers, the reorder tone plays and an error message
                                             				  displays on the transferor phone. The call is not disconnected between the
                                             				  transferee and transferor. | Yes | Yes |
| Ad Hoc
                                             				  Conference (software-based, 3-party) | Cisco Unified CME invokes the LPCOR policy validation for each
                                             				  call joined to a conference. A call is blocked from joining the conference if
                                             				  the LPCOR policy validation fails. The reorder
                                             				  tone plays and the conference cannot complete message displays on the IP phone
                                             				  that initiated the conference. The call is resumed by the transferor who
                                             				  initiated the conference. Note If the
                                                         					 LPCOR policy validation fails during a blind transfer setup to a conference
                                                         					 bridge, the call is released. Note LPCOR
                                                         					 validation is not supported for additional call transfer or conference
                                                         					 operations from a 3-party software conference call. | Note | If the
                                                         					 LPCOR policy validation fails during a blind transfer setup to a conference
                                                         					 bridge, the call is released. | Note | LPCOR
                                                         					 validation is not supported for additional call transfer or conference
                                                         					 operations from a 3-party software conference call. | Yes | No |
| Note | If the
                                                         					 LPCOR policy validation fails during a blind transfer setup to a conference
                                                         					 bridge, the call is released. |
| Note | LPCOR
                                                         					 validation is not supported for additional call transfer or conference
                                                         					 operations from a 3-party software conference call. |
| Ad Hoc
                                             				  Conference (hardware-based) | Yes | Yes |
| Meet-Me
                                             				  Conference | LPCOR policy
                                             				  of each conference party is validated when a new call is joined to a
                                             				  conference. The call is blocked from joining the conference if the LPCOR policy
                                             				  validation fails. The reorder
                                             				  tone plays and the conference cannot complete message displays on the IP phone
                                             				  that initiated the Meet-Me conference. | Yes | Yes (join
                                             				  only) |
| Call
                                             				  Pickup/Group Pickup (Cisco Unified CME 7.1 and later versions) | Call Pickup
                                             				  and Pickup Groups enable phone users to answer a call that is ringing on a
                                             				  different extension. The pickup is blocked if the LPCOR policy validation
                                             				  between the call and the pickup phone fails. The reorder
                                             				  tone plays and the unknown number message displays on the IP phone that
                                             				  attempts the call pickup. | Yes | Yes |
| Call Park
                                             				  (Cisco Unified CME 7.1 and later versions) | Phone users
                                             				  can place a call on hold at a special extension so it can be retrieved by other
                                             				  phones. A phone is
                                             				  not allowed to retrieve a parked call if the LPCOR policy validation fails. The
                                             				  reorder tone plays and the unknown number message displays on the IP phone that
                                             				  attempts to retrieve the parked call. The call remains parked at the call-park
                                             				  slot. | Yes | Yes |
| Call Park
                                             				  Retrieval | Yes | Yes |
| Hunt Group
                                             				  Pilot (ephone hunt group) | Supported
                                             				  for sequential and longest idle hunt groups. The LPCOR policy validation is
                                             				  performed when a call is directed to a SCCP endpoint through the ephone
                                             				  hunt-group. | Yes | No |
| Hunt Group
                                             				  Pilot (voice hunt group) | Supported
                                             				  for parallel hunt groups only. A hunt target can be a SCCP phone, SIP phone,
                                             				  VoIP trunk, or PSTN trunk. The LPCOR policy validation is performed between the
                                             				  call and the pilot hunt target. A call is blocked from a target if the LPCOR
                                             				  policy is restricted. | Yes | Yes |
| Shared
                                             				  Line | Phones
                                             				  with a shared directory number must have the same LPCOR policy. | Yes | Yes |
| CBarge | Phone
                                             				  users who share a directory number can join an active call on the shared line.
                                             				  Phones must have the same LPCOR policy. | Yes | Yes |
| Third-Party Call Control | Cisco
                                             				  Unified CME supports out-of-dialog refer (OOD-R) by a remote call-control
                                             				  system. The LPCOR validation is performed during the second outbound call setup
                                             				  after the first outbound call is established. The OOD-R request fails if the
                                             				  LPCOR policy between the first and second outbound call is restricted. | Yes | Yes |

| Note | If the
                                                         					 LPCOR policy validation fails during a blind transfer setup to a conference
                                                         					 bridge, the call is released. |
|---|---|

| Note | LPCOR
                                                         					 validation is not supported for additional call transfer or conference
                                                         					 operations from a 3-party software conference call. |
|---|---|

| Call Block
                                             				  Type | Phone
                                             				  Display Message |
|---|---|
|  | SCCP Phone | SIP Phone |
| Call
                                             				  Transfer | Unable to
                                             				  Transfer | Transfer
                                             				  Failed |
| Conference | Cannot
                                             				  Complete Conference |
| Meet-Me
                                             				  Conference | No Screen
                                             				  Display Update |
| Pickup | Unknown
                                             				  Number |
| Park | Unknown
                                             				  Number |

| Attribute | VSA No.
                                             				  (Decimal) | Format for
                                             				  Value or Text | Sample Value
                                             				  or Text | Description |
|---|---|---|---|---|
| in-lpcor-group | 1 | String | pstn_group | Logical
                                             				  partitioning class of restriction (LPCOR) resource-group policy associated with
                                             				  an incoming call. |
| out-lpcor-group | 1 | String | voip_group | LPCOR
                                             				  resource-group policy associated with an outgoing call. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice lpcor enable Example: Router(config)# voice lpcor enable | Enables LPCOR
                                             				functionality on the Cisco Unified CME router. |
| Step 4 | voice lpcor call-block cause cause-code Example: Router(config)# voice lpcor call-block cause 79 | (Optional)
                                             				Defines the cause code to use when a call is blocked because LPCOR validation
                                             				fails. Range: 1
                                                   					 to 180. Default: 63 (serv/opt-unavail-unspecified). Type ? to display
                                                   					 a description of the cause codes. |
| Step 5 | voice lpcor custom Example: Router(config)# voice lpcor custom | Defines the
                                             				name and number of LPCOR resource groups on the Cisco Unified CME router. |
| Step 6 | group number lpcor-group Example: Router(cfg-lpcor-custom)# group 1 pstn_trunk | Adds a LPCOR
                                             				resource group to the custom resource list. number —Group number of the LPCOR entry.
                                                   					 Range: 1 to 64. lpcor-group —String that identifies the LPCOR
                                                   					 resource group. |
| Step 7 | exit Example: Router(cfg-lpcor-custom)# exit | Exits LPCOR
                                             				custom configuration mode. |
| Step 8 | voice lpcor policy lpcor-group Example: Router(config)# voice lpcor policy pstn_trunk | Creates a
                                             				LPCOR policy for a resource group. lpcor-group —Name of the resource group that you
                                                   					 defined in Step 6. |
| Step 9 | accept lpcor-group Example: Router(cfg-lpcor-policy)# accept analog_phone | Allows a LPCOR
                                             				policy to accept calls associated with the specified resource group. Default:
                                                   					 Calls from other groups are rejected; calls from the same resource group are
                                                   					 accepted. Repeat
                                                   					 this command for each resource group whose calls you want this policy to
                                                   					 accept. |
| Step 10 | end Example: Router(cfg-lpcor-policy)# end | Returns to
                                             				privileged EXEC mode. |

| Note | For an analog
                                             			 FXS phone that is locally registered to Cisco Unified CME through the LAN, see Associate a LPCOR Policy with IP Phone or SCCP FXS Phone Calls . |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | trunk group name Example: Router(config)# trunk group isdn1 | Enters
                                             				trunk-group configuration mode to define a trunk group. |
| Step 4 | lpcor incoming lpcor-group Example: Router(config-trunk-group)# lpcor incoming isdn_group1 | Associates a
                                             				LPCOR resource-group policy with an incoming call. |
| Step 5 | lpcor outgoing lpcor-group Example: Router(config-trunk-group)# lpcor outgoing isdn_group1 | Associates a
                                             				LPCOR resource-group policy with an outgoing call. |
| Step 6 | exit Example: Router(config-trunk-group)# exit |  |
| Step 7 | voice-port port Example: Router(config)# voice-port 0/1/0 | Enters
                                             				voice-port configuration mode. Port argument is platform-dependent; type ? to display
                                                   					 syntax. |
| Step 8 | lpcor incoming lpcor-group Example: Router(config-voiceport)# lpcor incoming vp_group3 | Associates a
                                             				LPCOR resource-group policy with an incoming call. |
| Step 9 | lpcor outgoing lpcor-group Example: Router(config-voiceport)# lpcor outgoing vp_group3 | Associates a
                                             				LPCOR resource-group policy with an outgoing call. |
| Step 10 | end Example: Router(config-voiceport)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | The LPCOR IP-trunk subnet table is not supported for calls with an IPv6 address. The LPCOR policy specified with the lpcor incoming command in voice service configuration mode is supported for IPv6 trunk calls. Only a
                                                      				  single LPCOR policy is applied to outgoing IP trunk calls if the outbound VoIP
                                                      				  dial-peer is configured with the session
                                                            						target command using the sip-server or ras keyword. If a dial
                                                      				  peer COR and LPCOR are both defined in a dial peer, the dial peer COR
                                                      				  configuration has priority over LPCOR. For example, if the dial peer COR
                                                      				  restricts the call and LPCOR allows the call, the call fails because of the
                                                      				  dial peer COR before ever considering LPCOR. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice lpcor ip-trunk subnet incoming Example: Router(config)# voice lpcor ip-trunk subnet incoming | Creates a
                                             				LPCOR IP-trunk subnet table for incoming calls from a VoIP trunk. |
| Step 4 | index index-number lpcor-group { ipv4-address network-mask \| hostname hostname } Example: Router(cfg-lpcor-iptrunk-subnet)# index 1 h323_group1 172.19.33.0 255.255.255.0 | Adds a LPCOR
                                             				resource group to the IP trunk subnet table. |
| Step 5 | exit Example: Router(cfg-lpcor-iptrunk-subnet)# exit | Exits LPCOR
                                             				custom configuration mode. |
| Step 6 | voice service voip Example: Router(config)# voice service voip | Enters
                                             				voice-service configuration mode to specify the VoIP encapsulation type. |
| Step 7 | lpcor incoming lpcor-group Example: Router(conf-voi-serv)# lpcor incoming voip_trunk_1 | Associates a
                                             				LPCOR resource-group policy with an incoming call. |
| Step 8 | exit Example: Router(conf-voi-serv)# exit | Exits
                                             				voice-service configuration mode. |
| Step 9 | dial-peer voice tag voip Example: Router(config)# dial-peer voice 233 voip | Enters
                                             				dial-peer configuration mode to define a dial peer for VoIP calls. |
| Step 10 | lpcor outgoing lpcor-group Example: Router(config-dial-peer)# lpcor outgoing h323_group1 | Associates a
                                             				LPCOR resource-group policy with an outgoing call. |
| Step 11 | end Example: Router(config-dial-peer)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | Phones that
                                                      				  share a directory number must be configured with the same LPCOR policy. A
                                                      				  warning message displays if you try to configure a different LPCOR policy
                                                      				  between IP phones that share the same directory number. Local and
                                                      				  remote IP phones cannot use the same LPCOR policy. Software-based three-party ad hoc conferencing is not supported
                                                      				  on SIP phones. Hardware-based ad hoc conferening is not supported on SIP
                                                      				  phones. LPCOR
                                                      				  feature is not supported on voice gateways such as the Cisco VG224 or
                                                      				  Cisco integrated service router if the voice gateway is registered to
                                                      				  Cisco Unified Communications Manager. Cisco Unified Communications Manager does
                                                      				  not support LPCOR. If a
                                                      				  third-party call-control application makes two separate calls to
                                                      				  Cisco Unified CME and performs a media bridging between the two calls, LPCOR
                                                      				  validation is not supported because Cisco Unified CME is not aware of the
                                                      				  bridging. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag or voice register pool phone-tag Example: Router(config)# ephone 2 or Router(config)# voice register pool 4 | Enters ephone
                                             				configuration mode to set phone-specific parameters for an SCCP phone. or Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. phone-tag —Unique sequence number that identifies
                                                   					 the phone. Range is version and platform-dependent; type ? to display
                                                   					 range. |
| Step 4 | lpcor type { local \| remote } Example: Router(config-ephone)# lpcor type remote or Router(config-register-pool)# lpcor type local | Sets the LPCOR
                                             				type for an IP phone. local —IP phone always registers to
                                                   					 Cisco Unified CME through the LAN. remote —IP phone always registers to
                                                   					 Cisco Unified CME through the WAN. This
                                                   					 command can also be configured in ephone-template or voice register template
                                                   					 configuration mode and applied to one or more phones. The phone configuration
                                                   					 has precedence over the template configuration. |
| Step 5 | lpcor incoming lpcor-group Example: Router(config-ephone)# lpcor incoming ephone_group1 or Router(config-register-pool)# lpcor incoming remote_group3 | Associates a
                                             				LPCOR resource-group policy with an incoming call. If this
                                                   					 phone shares a directory number with another phone, you cannot configure a
                                                   					 LPCOR policy that is different than the LPCOR policy on the other phone. This
                                                   					 command can also be configured in ephone-template or voice register template
                                                   					 configuration mode and applied to one or more phones. The phone configuration
                                                   					 has precedence over the template configuration. |
| Step 6 | lpcor outgoing lpcor-group Example: Router(config-ephone)# lpcor outgoing ephone_group2 or Router(config-register-pool)# lpcor outgoing remote_group3 | Associates a
                                             				LPCOR resource-group policy with an outgoing call. If this
                                                   					 phone shares a directory number with another phone, you cannot configure a
                                                   					 LPCOR policy that is different than the LPCOR policy on the other phone. This
                                                   					 command can also be configured in ephone-template or voice register template
                                                   					 configuration mode and applied to one or more phones. The phone configuration
                                                   					 has precedence over the template configuration. |
| Step 7 | end Example: Router(config-ephone)# end or Router(config-register-pool)# end | Returns to
                                             				privileged EXEC mode. |

| Restriction | The LPCOR
                                             			 IP-phone subnet table is not supported for calls with an IPv6 address. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables
                                             				privileged EXEC mode. Enter your
                                                   					 password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | ephone phone-tag or voice register pool phone-tag Example: Router(config)# ephone 1 or Router(config)# voice register pool 1 | Enters ephone
                                             				configuration mode to set phone-specific parameters for an SCCP phone. or Enters voice
                                             				register pool configuration mode to set phone-specific parameters for a SIP
                                             				phone. phone-tag —Unique sequence number that identifies
                                                   					 the phone. Range is version and platform-dependent; type ? to display
                                                   					 range. |
| Step 4 | lpcor type mobile Example: Router(config-ephone)# lpcor type mobile | Sets the LPCOR
                                             				type for a mobile-type phone. This
                                                   					 command can also be configured in ephone-template or voice register template
                                                   					 configuration mode and applied to one or more phones. The phone configuration
                                                   					 has precedence over the template configuration. |
| Step 5 | exit Example: Router(config-ephone)# exit | Exits the
                                             				phone configuration. |
| Step 6 | voice lpcor ip-phone subnet { incoming \| outgoing } Example: Router(config)# voice lpcor ip-phone subnet incoming | Creates a
                                             				LPCOR IP-phone subnet table for calls to or from a mobile-type phone. |
| Step 7 | index index-number lpcor-group { ipv4-address network-mask [ vrf vrf-name ] \| dhcp-pool pool-name } Example: Router(cfg-lpcor-ipphone-subnet)# index 1 local_group1 dhcp-pool pool1 | Adds a LPCOR
                                             				group to the IP-phone subnet table. |
| Step 8 | exit Example: Router(cfg-lpcor-ipphone-subnet)# exit | Exits LPCOR
                                             				IP-phone configuration mode. |
| Step 9 | voice lpcor ip-phone mobility { incoming \| outgoing } lpcor-group Example: Router(config)# voice lpcor ip-phone mobility incoming remote_group1 | Sets the default LPCOR policy for mobile-type phones. |
| Step 10 | exit Example: Router(config)# exit | Exits to
                                             				privileged EXEC mode. |

| Feature Name | Cisco Unified CME Version | Feature Information |
|---|---|---|
| Call Restriction Regulations for Cisco Unified CME | 8.0 | Introduced support for LPCOR feature. |