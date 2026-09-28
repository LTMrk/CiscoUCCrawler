---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-command-reference-cme-cr-cme-cr-chapter-0110-html-0c9a3a7400
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/command/reference/cme_cr/cme_cr_chapter_0110.html
retrieved_at: 2026-08-21T22:56:07.033019+00:00
---

Cisco Unified Communications Manager Express Command Reference

# Cisco Unified Communications Manager Express Command Reference

Updated: July 19, 2018

Chapter: Cisco Unified CME Commands: G

## Chapter: Cisco Unified CME Commands: G

# Cisco Unified CME Commands: G

## gsm-support

To define the gsm
                              		  support for a Cisco Unified SIP IP phone on Cisco Unified CME, use the gsm-support command in voice register pool-type
                              		  mode. To remove the gsm support, use the no form of
                              		  this command. no form is typically used to override the inherited property of
                              		  the reference ephone with default value.

gsm-support

no gsm-support

### Syntax
                              		  Description

This command has
                              		  no arguments or keywords.

### Command Default

By default, the
                              		  gsm-support is not enabled. When reference-pooltype is configured, the gsm-support value of the reference phone is inherited.

### Command Modes

Voice Register Pool-type Configuration (config-register-pooltype)

## Command History

15.3(3)M

Cisco SIP
                                       					 CME 10.0

This
                                       					 command was introduced.

### Usage Guidelines

Use this command
                              		  to define the maximum number of addon modules for a Cisco Unified SIP IP phone
                              		  on Cisco Unified CME. When you use the no form of this command, the inherited
                              		  properties of the reference phone is takes precedence over the default value.

## Examples

The following
                              		  example shows how to enter voice register pool configuration mode and define
                              		  themaximum number of addon modules for a Cisco Unified SIP IP phone on Cisco
                              		  Unified CME:

```
Router(config)# voice register pool-type 9900 Router(config-register-pool-type)# gsm-support
```

### Related Commands

Command

Description

Adds a new Cisco Unified SIP IP phone to Cisco Unified CME.

## group (lpcor custom)

To add a logical partitioning class of restriction (LPCOR) resource
                              		  group to the custom resource list, use the group command in LPCOR custom configuration
                              		  mode. To remove a resource group, use the no form of this command.

group number lpcor-group

no group number

### Syntax Description

number

Group number of the LPCOR entry. Range: 1 to 64.

lpcor-group

Name of a LPCOR resource group.

### Command Default

LPCOR resource group is not defined.

### Command Modes

LPCOR custom configuration (cfg-lpcor-custom)

## Command History

Cisco IOS Release

Cisco Product

Modification

15.0(1)XA

Cisco Unified CME 8.0

This command was introduced.

15.1(1)T

Cisco Unified CME 8.0

This command was integrated into Cisco IOS Release
                                          						15.1(1)T.

### Usage Guidelines

Use this command to define all of the LPCOR resource groups that you
                              		  are provisioning on the Cisco Unified CME router. You must logically partition
                              		  the resources of the Cisco Unified CME router (trunks and phones) into
                              		  different LPCOR resource groups so that you can apply the required call
                              		  restrictions to each group.

## Examples

The following example shows a LPCOR configuration with six resource
                              		  groups:

```
voice lpcor custom
 group 1 sccp_phone_local
 group 2 sip_phone_local
 group 3 analog_phone_local
 group 4 sip_remote
 group 5 sccp_remote
 group 6 isdn_local
```

### Related Commands

Command

Description

voice lpcor enable

Enables LPCOR functionality on the Cisco Unified CME
                                          						router.

voice lpcor policy

Creates a LPCOR policy for a resource group.

## group (telephony-service)

To create a (VRF) group for Cisco Unified CME users and phones, use
                              		  the group command in telephony-service configuration mode. To remove a
                              		  group, use the no form of this command.

group group-tag [ vrf vrfname ]

no group

### Syntax Description

group-tag

Unique identifier for VRF group being configured. Range 1
                                          						to 5

vrf vrfname

(Optional) Name of already-configured VRF to which this VRF
                                          						group is associated.

### Command Default

No group is configured.

### Command Modes

Telephony-service configuration (config-telephony)

## Command History

Release

Modification

12.4(22)T

This command was introduced.

### Usage Guidelines

By default, VRF groups are associated with a global voice VRF unless
                              		  you use the vrf vrfname keyword and argument combination to
                              		  specifiy otherwise.

If you configure this command, the ip source-address , url and cnf-file location commands in telephony-service configuration mode are
                              		  automatically converted into group 1 with a default global VRF for nvgen during
                              		  system upgrade.

If you configure this command and the cnf-file location command is configured for system: , the per phone or per phone type file
                              		  for an ephone in the VRF group is created in system:/its/vrf<group-tag>/ . Local files are still
                              		  created in system:/its/.

If you configure this command and the cnf-file location command is configured as flash: or slot0: , the per phone or per phone type file
                              		  for an ephone in the VRF group is named flash:/its/vrf<group-tag>_<filename> or
                                 			 slot0:/its/vrf<group tag>_filename> .

The location of the locale files is not affected by configuring a VRF
                              		  group.

## Examples

The following example shows the configuration for three VRF groups.
                              		  Group 1 is on a global voice VRF and the other two groups are on data VRFs.

```
telephony-service
 sdspfarm conference mute-on # mute-off #
 sdspfarm units 4
 sdspfarm transcode sessions 10
 sdspfarm tag 1 xcode101
 sdspfarm tag 2 conf103
 group  1 
  ip source-address 10.1.10.1 port 2000
  url directories http://210.1.10.1/localdirectory
 !
 group  2 vrf data-vrf1
  ip source-address 10.2.10.1 port 2000
 !
 group  3 vrf data-vrf2
  ip source-address 10.3.10.1 port 2000
 !
.
.
.
```

### Related Commands

Command

Description

ip vrf

Defines a VRF for a router.

cnf-file location

Specifies a storage location for phone configuration files

## group
                        	 phone

To add a phone,
                              		  including a TAPI-based client application, or a softphone on a PC to a VRF
                              		  group for Cisco Unified CME, use the group command in ephone or ephone-template configuration mode. To
                              		  remove the group configuration, use the no form of
                              		  this command.

group

no group

### Syntax Description

This command has no arguments or keywords.

### Command Default

By default, this
                              		  feature is disabled.

### Command Modes

Ephone configuration (config-ephone)

Ephone-template configuration (config-ephone-template)

## Command History

Cisco
                                          						IOS Release

Cisco
                                          						Products

Modification

12.4(22)T

Cisco
                                          						Unified CME 7.0(1)

This
                                          						command was introduced.

### Usage Guidelines

This command
                              		  enables to configure the voice VRF group for SIP phones. This command adds a
                              		  softphone on a PC, an IP phone, or a TAPI client on an IP phone to a VRF group.

VRF groups for
                              		  users and phones in Cisco Unified CME are created by using the group command
                              		  in telephony-service configuration mode. All SCCP and SIP phones connected to
                              		  Cisco Unified CME must register through the global voice VRF. TAPI-based client
                              		  on an IP phone and softphones on a PC must register in Cisco Unified CME
                              		  through a data VRF.

Before you can
                              		  use this command, the MAC address for the IP phone being configured must be
                              		  configured by using the mac-address command in ephone configuration mode.

If you use an
                              		  ephone template to apply a command to an ephone and you also use the same
                              		  command in ephone configuration mode, the value that you set in ephone
                              		  configuration mode has priority over the ephone-template configuration.

## Examples

The following
                              		  example shows four phones in three VRF groups, two on data VRFs and one on a
                              		  global voice VRF.

```
telephony-service
 sdspfarm conference mute-on # mute-off #
 sdspfarm units 4
 sdspfarm transcode sessions 10
 sdspfarm tag 1 xcode101
 sdspfarm tag 2 conf103
 group  1 
  ip source-address 209.165.201.1 port 2000
  url directories http://209.165.201.1/localdirectory
 !
 group  2 vrf data-vrf1
  ip source-address 209.165.201.2 port 2000
 !
group  3 vrf data-vrf2
  ip source-address 209.165.201.3 port 2000
 !
.
.
!
ephone-template 1
  group phone 1 tapi 2
ephone-template 2
  group phone 2
...
ephone 1
  mac-address 1111.2222.3333
  ephone-template 1
ephone 2
  mac-address 2222.2222.3333
  ephone-template 2
ephone 3
  mac-address 1111.3333.3333
  group phone 1 tapi 3
ephone 4
  mac-address 1111.2222.4444
  group phone 3
!
```

## Examples

The following
                              		  example shows four phones in three VRF groups, two on data VRFs and one on a
                              		  global voice VRF.

```
Router(config)# voice register template Router(config-telephony)# group <group-tag>
```

### Related Commands

Command

Description

voice register
                                                							 pool

Enters
                                          						voice register pool configuration mode.

voice register
                                                							 template

Enters
                                          						voice register template configuration mode.

ephone-template (ephone)

Applies
                                          						an ephone template to an ephone configuration.

group (telephony-service)

Creates
                                          						a VRF group for phones and users in Cisco Unified CME.

mac-address

Associates the MAC address of a Cisco IP phone with an ephone configuration.

## group (voice
                        	 register global)

To add a phone or
                              		  a softphone on a PC to a Virtual routing and forwarding (VRF) group for Cisco
                              		  Unified CME, use the group command in voice register global configuration mode. To
                              		  remove the configuration, use the no form of
                              		  this command. To configure SIP CME support for VRF by provisioning its source
                              		  address under a group, use the vrfname command. To remove the configuration, use the no form of
                              		  this command.

group group-tag

no group

group group-tag vrf vrfname

no group vrf vrfname

### Syntax Description

group-tag

Unique identifier of VRF group. Range is from 1 to 5.

vrfname

Specifies the name of the vrf group.

### Command Default

By default, this
                              		  feature is disabled.

### Command Modes

voice register global (config-register global)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

This command
                              		  enables to configure the VRF group for SIP phones. This command is used to
                              		  configure multiple VRF groups for SIP phones and soft phones on PC or mobile
                              		  devices registering to CME. Each VRF group can be associated with a specific IP
                              		  VRF. Phones in this VRF will use the source-address configured under this VRF
                              		  group to register to CME.

## Examples

The following
                              		  example shows three different VRF groups that have been configured, a voice
                              		  VRF, a Data VRF, and a Voice VRF:

```
vovoice register global
 mode  cme
 max-dn 100
 max-pool 100
 
 group 1 vrf voice-vrf
  source-address 8.0.0.1
 
 group 2 vrf data-vrf
  source-address 9.0.0.1

 group 3 vrf voice-vrf1
  source-address 10.0.0.1
```

### Related Commands

Command

Description

group (telephony-service)

Creates a VRF group for phones and users in Cisco Unified CME.

## group (voice
                        	 register pool)

To configure
                              		  multiple virtual routing and forwarding (VRF) groups for SIP phones and soft
                              		  phones on PC or mobile, use the group command in voice register pool configuration or voice register template
                              		  configuration modes. To remove the configuration, use the no form of
                              		  this command. You can configure upto 5 VRF groups.

To add a phone or
                              		  a softphone on a PC to a VRF group for Cisco Unified CME, use the group command in voice register pool or voice register template
                              		  configuration modes. To remove the configuration, use the no form of
                              		  this command.

group group-tag

no group

### Syntax Description

group-tag

Unique identifier of VRF group. Range is from 1 to 5.

### Command Default

By default, this
                              		  feature is disabled.

### Command Modes

voice register pool (config-register pool)

voice register template (config-register template)

## Command History

This
                                       					 command was introduced.

### Usage Guidelines

This command
                              		  enables to configure the VRF group for SIP phones. The group id configured
                              		  under voice register global can be associated to the voice register pool or
                              		  template using the group <group-tag> command.

## Examples

The following
                              		  example shows phones configured in different VRF groups under voice register
                              		  pool and voice register template modes:

```
voice register pool  1 
group 1 

voice register template 1 
group 3
```

### Related Commands

Command

Description

voice register
                                                							 global

Enters
                                          						voice register global configuration mode.

voice register
                                                							 template

Enters
                                          						voice register template configuration mode.

| Release | Cisco Product | Modification |
|---|---|---|
| 15.3(3)M | Cisco SIP
                                       					 CME 10.0 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| voice register pool-type | Adds a new Cisco Unified SIP IP phone to Cisco Unified CME. |

| number | Group number of the LPCOR entry. Range: 1 to 64. |
|---|---|
| lpcor-group | Name of a LPCOR resource group. |

| Cisco IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.0(1)XA | Cisco Unified CME 8.0 | This command was introduced. |
| 15.1(1)T | Cisco Unified CME 8.0 | This command was integrated into Cisco IOS Release
                                          						15.1(1)T. |

| Command | Description |
|---|---|
| voice lpcor enable | Enables LPCOR functionality on the Cisco Unified CME
                                          						router. |
| voice lpcor policy | Creates a LPCOR policy for a resource group. |

| group-tag | Unique identifier for VRF group being configured. Range 1
                                          						to 5 |
|---|---|
| vrf vrfname | (Optional) Name of already-configured VRF to which this VRF
                                          						group is associated. |

| Release | Modification |
|---|---|
| 12.4(22)T | This command was introduced. |

| Command | Description |
|---|---|
| ip vrf | Defines a VRF for a router. |
| cnf-file location | Specifies a storage location for phone configuration files |

| Cisco
                                          						IOS Release | Cisco
                                          						Products | Modification |
|---|---|---|
| 12.4(22)T | Cisco
                                          						Unified CME 7.0(1) | This
                                          						command was introduced. |

| Command | Description |
|---|---|
| voice register
                                                							 pool | Enters
                                          						voice register pool configuration mode. |
| voice register
                                                							 template | Enters
                                          						voice register template configuration mode. |
| ephone-template (ephone) | Applies
                                          						an ephone template to an ephone configuration. |
| group (telephony-service) | Creates
                                          						a VRF group for phones and users in Cisco Unified CME. |
| mac-address | Associates the MAC address of a Cisco IP phone with an ephone configuration. |

| group-tag | Unique identifier of VRF group. Range is from 1 to 5. |
|---|---|
| vrfname | Specifies the name of the vrf group. |

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified CME 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| group (telephony-service) | Creates a VRF group for phones and users in Cisco Unified CME. |

| group-tag | Unique identifier of VRF group. Range is from 1 to 5. |
|---|---|

| Cisco
                                    				  IOS Release | Cisco Product | Modification |
|---|---|---|
| 15.4(3)M | Cisco Unified CME 10.5 | This
                                       					 command was introduced. |

| Command | Description |
|---|---|
| voice register
                                                							 global | Enters
                                          						voice register global configuration mode. |
| voice register
                                                							 template | Enters
                                          						voice register template configuration mode. |