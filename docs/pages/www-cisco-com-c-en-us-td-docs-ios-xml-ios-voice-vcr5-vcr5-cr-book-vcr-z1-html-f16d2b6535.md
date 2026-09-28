---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-vcr5-vcr5-cr-book-vcr-z1-html-f16d2b6535
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/vcr5/vcr5-cr-book/vcr-z1.html
retrieved_at: 2026-08-16T23:16:29.190620+00:00
---

Cisco IOS Voice Command Reference - T through Z

# Cisco IOS Voice Command Reference - T through Z

Updated: April 25, 2026

Chapter: Z

## Chapter: Z

# Z

## zone access

To configure the accessibility of your local zone, use the zone access command in gatekeeper configuration mode. To remove any accessibility configurations, use the no form of this command.

zone access local-zone-name { default | remote-zone remote-zone-name } { direct | proxied }

no zone access local-zone-name remote-zone remote-zone-name

### Syntax Description

local - zone - name

Name of local zone (synonymous with local gatekeeper).

default

Use with the direct or proxied keyword to define the mode of behavior for all remote zones that have not been specially named using the remote - zone remote - zone - name keyword and argument combination.

remote - zone remote - zone - name

Name of remote zone (synonymous with remote gatekeeper) for which a special mode of behavior is defined.

direct

Configures direct calls (without use of proxies) between endpoints. The local zone (or gatekeeper) offers the local endpoint
                                          IP address instead of the IP address of a local proxy.

proxied

Configures calls using proxies between endpoints. The local zone (or gatekeeper) offers the IP address of a local proxy instead
                                          of the local endpoint address.

### Command Default

The local zone allows proxied access for all remote zones.

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

11.3(2)NA

This command was introduced on the Cisco 2500 series and Cisco 3600 series.

### Usage Guidelines

By default, a gatekeeper offers a local proxy IP address when queried by a remote gatekeeper about a target local endpoint.
                              This is considered proxied access. By using the zone access command, you can configure the local gatekeeper to offer the local endpoint address instead of the local proxy address. This
                              is considered direct access.

The zone access command, configured on your local gatekeeper, affects only the use of proxies for incoming calls (that is, it does not affect
                                          the use of local proxies for outbound calls). When originating a call, a gatekeeper uses a proxy only if the remote gatekeeper
                                          offers a proxy at the remote end. A call between two endpoints in the same zone is always a direct (nonproxied) call.

You can define the accessibility behavior of a local zone relative to certain remote zones using the remote - zone remote - zone - name keyword and argument combination with the direct or proxied keyword. You can define the default behavior of a local zone relative to all other remote zones using the default keyword with the direct or proxied keywords. To remove an explicitly named remote zone so that it is governed by the default-behavior rule, use the no zone access command.

## Examples

The following example allows direct access to the local zone eng.xyz.com from remote zones within xyz corporation. All other
                              remote locations will have proxied access to eng.xzy.com.

```
zone local eng.xyz.com xyz.com
zone access eng.xyz.com remote-zone mfg.xyz.com direct
zone access eng.xyz.com remote-zone mktg.xyz.com direct
zone access eng.xyz.com remote-zone sales.xyz.com direct
zone access eng.xyz.com default proxied
```

The following example supposes that only local gatekeepers within xyz.com have direct access to each other because your corporation
                              has firewalls or you do not advertise your gatekeepers externally. You have excellent Quality of Service (QoS) within your
                              corporate network, except for a couple of foreign offices. In this case, use proxies with the foreign offices (in Milan and
                              Tokyo) and nowhere else.

```
zone local sanjose.xyz.com xyz.com
zone access sanjose.xyz.com default direct
zone access sanjose.xyz.com remote-zone milan.xyz.com proxied
zone access sanjose.xyz.com remote-zone tokyo.xyz.com proxied
```

### Related Commands

Command

Description

show proxy h323 calls

Displays a list of each active call on the proxy.

zone local

Specifies a zone controlled by a gatekeeper.

## zone bw

To set the maximum bandwidth allowed in a gatekeeper zone at any one time, use the zone bw command in gatekeeper configuration mode. To remove the maximum bandwidth setting and make the bandwidth unlimited, use the no form of this command.

zone bw gatekeeper-name max-bandwidth

no zone bw gatekeeper-name max-bandwidth

### Syntax Description

gatekeeper - name

Name of the gatekeeper that controls the zone.

max - bandwidth

Maximum bidirectional bandwidth, in kbps, allowed in the zone at any one time.

### Command Default

Bandwidth is unlimited.

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

11.3(2)NA

This command was introduced on Cisco 2500 series and Cisco 3600 series.

## Examples

The following example sets the maximum bandwidth to 1000 kbps for zone gk1:

```
zone bw gk1 
1000
```

### Related Commands

Command

Description

show proxy h323 calls

Displays a list of each active call on the proxy.

## zone circuit-id

To associate a remote zone with a circuit, use the zone circuit - id command in gatekeeper configuration mode. To delete the circuit ID for a zone, use the no form of this command.

zone circuit-id remote-zone-name circuit-id [ override-source-circuitid ]

no zone circuit-id remote-zone-name circuit-id

### Syntax Description

remote - zone - name

Name of the remote zone.

circuit - id

ID of the circuit to be associated with the remote zone.

override-source-circuitid

(Optional) Specifies whether the source circuit ID of the incoming location request (LRQ) message needs to be overridden with
                                          this keyword.

### Command Default

The override flag is disabled and the incoming source circuit ID is used if present.

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

12.2(11)T

This command was introduced.

12.3(14)T

The override-source-circuitid keyword was added.

### Usage Guidelines

VoIP calls with an LRQ message that come to a gatekeeper from a non-cisco gatekeeper in a remote zone (for example, from an
                              Internet telephony service provider [ITSP]), the LRQ message does not include a source circuit identifier. This command allows
                              the gatekeeper to assign a circuit identifier to the zone and an IP address of the call origination. If the source circuit
                              ID is already present then the configured value will not be used. To enforce the usage of configured source circuit ID, even
                              if the incoming LRQ has a value, configure the override-source-circuitid keyword. The Gatekeeper Transaction Message Protocol (GKTMP) server application uses this data to determine a route for the
                              call.

## Examples

The following example configures the remote zone GKout1 with a circuit ID CarrierA:

```
Router(config)# gatekeeper Router(config-gk)# zone circuit-id GKout1 CarrierA
```

The following example configures the remote zone GKout2 with a circuit ID CarrierB and overrides the incoming LRQ source circuit-id
                              value:

```
Router(config)# gatekeeper Router(config-gk)# zone circuit-id GKout2 CarrierB override-source-circuitid
```

### Related Commands

Command

Description

endpoint circuit-id h323id

Assigns a circuit to a non-Cisco endpoint.

show gatekeeper circuits

Displays circuit information on the gatekeeper.

show gatekeeper endpoint circuits

Displays information for all registered endpoints and carriers for the gatekeeper.

## zone cluster local

To define a local grouping of gatekeepers, including the gatekeeper that you are configuring, use the zone cluster local command in gatekeeper configuration mode. To disable the local grouping of gatekeepers, use the no form of this command.

zone cluster local cluster-name local-zone-name

no zone cluster local

### Syntax Description

cluster - name

Cluster name.

local - zone - name

Local zone name.

### Command Default

No default behavior or values

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

12.1(5)XM

This command was introduced.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XB1

This command was implemented on Cisco AS5850.

### Usage Guidelines

Use this command to define a local cluster of gatekeepers that are alternates of each other. Each of these gatekeepers must
                              be configured in a compatible manner for the cluster to work effectively.

## Examples

The following example defines a local grouping of gatekeepers named EuropeCluster in the ParisGK time zone:

```
zone cluster local EuropeCluster ParisGK
```

### Related Commands

Command

Description

element

Defines component elements of local or remote clusters.

zone cluster remote

Defines a remote grouping of gatekeepers, including the gatekeeper that you are configuring.

## zone cluster remote

To define a remote grouping of gatekeepers, including the gatekeeper that you are configuring, use the zone cluster remote command in gatekeeper configuration mode. To disable the remote grouping of gatekeepers, use the no form of this command.

{ zone cluster remote cluster name [ cost cost-value [ priority priority-value ]] [ foreign-domain ] [ invia inbound gatekeeper ] |  [ outvia outbound gatekeeper ]}

no zone cluster remote

### Syntax Description

cluster name

Cluster name.

cost

(Optional) Cost.

cost - value

(Optional) Cost value. Range is from 1 to 100. The default is L50.

priority

(Optional) Priority.

priority - value

(Optional) Priority value. Range is from 1 to 100. The default is 50.

foreign - domain

(Optional) Cluster is in a different administrative domain.

invia

Specifies gatekeeper for calls entering this zone.

inbound gatekeeper

Name of gatekeeper.

outvia

Specifies gatekeeper for calls leaving this zone.

outbound gatekeeper

Name of gatekeeper.

### Command Default

No default behavior or values

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

12.1(5)XM

This command was introduced.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XA

The foreign - domain keyword was added.

12.2(4)T

This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release.

12.2(2)XB1

This command was implemented on Cisco AS5850.

12.2(13)T3

The invia and outvia keywords were added.

### Usage Guidelines

Use this command to define a set of remote gatekeepers that act as alternates to each other and that form a local cluster.
                              This command causes the gatekeeper to optimize these remote gatekeepers by round-robin sending of Location Request (LRQ) messages.

## Examples

The following example shows how to define a remote grouping of gatekeepers:

```
zone cluster remote AsiaCluster cost 70 priority 10
```

### Related Commands

Command

Description

element

Defines component elements of local or remote clusters.

zone cluster local

Defines a local grouping of gatekeepers, including the gatekeeper that you are configuring.

zone local

Specifies a zone controlled by a gatekeeper.

## zone qos

To configure the Differentiated Services Code Point (DSCP) value for a specific zone or a common DSCP value for all zones
                              in Quality of Service (QoS) configurations on a Cisco router, use the zone qos command in gatekeeper configuration mode. To remove the DSCP configuration, use the no form of this command.

zone qos { gatekeeper-name | global } dscp dscp-value

no zone qos { gatekeeper-name | global } dscp dscp-value

### Syntax Description

gatekeeper-name

The gatekeeper name to be configured.

global

Configures the DSCP value globally.

dscp

Specifies the DSCP to be configured.

dscp-value

The predefined DSCP keyword or its equivalent numeric value. Refer to the table below for more details.

### Command Default

This command is disabled by default.

### Command Modes

Gatekeeper configuration (conf-gk)

## Command History

Release

Modification

15.0(1)M

This command was introduced.

### Usage Guidelines

To configure a common DSCP value for all local and remote zones, use the global keyword and then specify the dscp keyword and its value. To change a globally configured DSCP value for a zone-specific DSCP value, the globally configured
                              value should be removed first using the no form of the command. If not, a warning message will be displayed. Use the gatekeeper name and the dscp keyword with the specific value to configure a zone-based DSCP value.

DSCP can be configured using the predefined DSCP keywords or its equivalent numeric value. For example, to configure the
                              DSCP value of a zone, the cs1 keyword can be replaced with the numeric value 8. However, the show gatekeeper zone status output displays the configured DSCP as cs1. The table below provides the predefined DSCP keywords and their equivalent numeric
                              values. The hexadecimal value is the number that is displayed in the QOS field of the IP header.

Keyword

Numeric Value

Hexadecimal Value

default

0

0x00

cs1

8

0x20

af11

10

0x28

af12

12

0X30

af13

14

0x38

cs2

16

0x40

af21

18

0x48

af22

20

0x50

af23

22

0x58

cs3

24

0x60

af31

26

0x68

af32

28

0x70

af33

30

0x78

cs4

32

0x80

af41

34

0x88

af42

36

0x90

af43

38

0x98

cs5

40

0xA0

ef

46

0xB8

cs6

48

0xC0

cs7

56

0xE0

## Examples

The following example shows how to configure the DSCP value for a specific zone using the zone qos gatekeeper-name dscp dscp-value command:

```
Router(config)# gatekeeper Router(conf-gk)# zone qos GK-08 dscp cs3
```

The following example shows how to configure the global DSCP value using the zone qos global dscp dscp-value command:

```
Router(config)# gatekeeper Router(conf-gk)# zone qos global dscp af11
```

### Related Commands

Command

Description

show gatekeeper zone status

Displays the status of the zones related to the gatekeeper.

## zone local

To specify a zone controlled by a gatekeeper, use the zone local command in gatekeeper configuration mode. To remove a zone controlled by a gatekeeper, use the no form of this command.

zone local gatekeeper-name domain-name [ras-IP-address] [ invia inbound gatekeeper | outvia outbound gatekeeper [ enable-intrazone ]]

no zone local gatekeeper-name domain-name [ invia inbound gatekeeper | outvia outbound gatekeeper [ enable-intrazone ]]

### Syntax Description

gatekeeper-name

Gatekeeper name or zone name. This is usually the fully domain-qualified host name of the gatekeeper. For example, if the domain-name is cisco.com, the gatekeeper-name might be gk1.cisco.com. However, if the gatekeeper is controlling multiple zones, the gatekeeper-name for each zone should be some unique mnemonic string.

domain-name

The domain name served by this gatekeeper.

ras-IP-address

(Optional) IP address of one of the interfaces on the gatekeeper. When the gatekeeper responds to gatekeeper discovery messages,
                                          it signals the endpoint or gateway to use this address in future communications.

Setting this address for one local zone makes it the address used for all local zones.

invia

Specifies gatekeeper for calls entering this zone.

inbound gatekeeper

Name of gatekeeper.

outvia

Specifies gatekeeper for calls leaving this zone.

outbound gatekeeper

Name of gatekeeper.

enable-intrazone

Forces all intrazone calls to use the via gatekeeper.

### Command Default

No local zone is defined.

The gatekeeper cannot operate without at least one local zone definition. Without local zones, the gatekeeper goes to an inactive
                                          state when the no shutdown command is issued.

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

11.3(2)NA

This command was introduced on Cisco 2500 and Cisco 3600 series routers.

12.2(11)T

This command was implemented on the Cisco MC3810 and Cisco 7200 series.

12.3(4)T

The invia , outvia , and enable-intrazone keywords were added.

### Usage Guidelines

Multiple local zones can be defined. The gatekeeper manages all configured local zones. Intrazone and interzone behavior remains
                              the same (zones are controlled by the same or different gatekeepers).

Only one ras-IP-address argument can be defined for all local zones. You cannot configure each zone to use a different RAS IP address. If you define
                              this in the first zone definition, you can omit it for all subsequent zones, which automatically pick up this address. If
                              you set it in a subsequent zone local command, it changes the RAS address of all previously configured local zones as well. Once defined, you can change it by
                              reissuing any zone local command with a different ras-IP-address argument.

If the ras-IP-address argument is a Hot Standby Router Protocol (HSRP) virtual address, it automatically puts the gatekeeper into HSRP mode. In
                              this mode, the gatekeeper assumes STANDBY or ACTIVE status according to whether the HSRP interface is on STANDBY or ACTIVE
                              status.

You cannot remove a local zone if there are endpoints or gateways registered in it. To remove the local zone, shut down the
                              gatekeeper first, which forces unregistration.

Multiple zones are controlled by multiple logical gatekeepers on the same Cisco IOS platform.

The maximum number of local zones defined in a gatekeeper should not exceed 100.

This command can also be used to change the IP address used by the gatekeeper.

## Examples

The following example creates a zone controlled by a gatekeeper in the domain called "cisco.com":

```
Router(config)# gatekeeper Router(config-gk)# zone local easterngk.cisco.com cisco.com
```

### Related Commands

Command

Description

show proxy h323 calls

Displays a list of each active call on the proxy.

zone subnet

Specifies a zone controlled by a gatekeeper.

## zone prefix

To add a prefix to the gatekeeper zone list, use the zone prefix command in gatekeeper configuration mode.
                              		  To remove knowledge of a zone prefix, use the no form of this command with the gatekeeper
                              		  name and prefix. To remove the priority assignment for a specific gateway, use
                              		  the no form of this command with the gw - priority option.

zone
                                 				  prefix gatekeeper-name e164 prefix [ blast | sequence ] { gw-priority priority-gw-alias [ gw-alias.. ]}

zone
                                 				  prefix gatekeeper-name e164 prefix [ blast | sequence ] { gw-priority priority-gw-alias [ gw-alias.. ]}

### Syntax Description

gatekeeper - name

Name of a local or remote gatekeeper, which must have been
                                          						defined by using the zone local or zone remote command.

e164 - prefix

E.164 prefix in standard form followed by dots (.). Each
                                          						dot represents a number in the E.164 address. For example, 212....... is
                                          						matched by 212 and any seven numbers.

Although a dot representing each digit in an E.164
                                                      						address is the preferred configuration method, you can also enter an asterisk
                                                      						(*) to match any number of digits.

blast

(Optional) If you list multiple hopoffs, this indicates
                                          						that the LRQs should be sent simultaneously to the gatekeepers based on the
                                          						order in which they were listed. The default is seq .

seq

(Optional) If you list multiple hopoffs, this indicates
                                          						that the LRQs should be sent sequentially to the gatekeepers based on the order
                                          						in which they were listed. The default is seq .

gw - priority pri - 0 - to - 10 gw - alias

(Optional) Defines how the gatekeeper selects gateways in
                                          						its local zone for calls to numbers beginning with prefix e164-prefix . Do not use this option
                                          						to set priority levels for a prefix assigned to a remote gatekeeper.

Range is from 0 to 10, where 0 prevents the gatekeeper from
                                          						using the gateway gw-alias for that prefix and 10
                                          						places the highest priority on gateway gw-alias . The default is 5.

To assign the same priority value for one prefix to
                                          						multiple gateways, list all the gateway names after the pri-0-to-10 value.

gw-alias name is the H.323 ID of a
                                          						gateway that is registered or will register with the gatekeeper. This name is
                                          						set on the gateway with the h323 - gateway voip h.323 - id command.

### Command Default

No knowledge of the gatekeeper zone prefix or the prefix of any other
                              		  zone is defined. Gateway priority is 5.

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

11.3(6)Q

This command was introduced.

11.3(7)NA

This command was modified for H.323 Version 1.

12.0(5)T

The display format was modified for H.323 Version 2.

12.1(5)XM

The command was implemented on Cisco AS5350 and Cisco
                                          						AS5400.

12.2(4)T

This command was integrated into Cisco IOS Release
                                          						12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not
                                          						included in this release.

12.2(2)XB1

This command was implemented on the Cisco AS5850.

12.2(8)T

Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400,
                                          						and Cisco AS5850 is not included in this release.

12.2(11)T

This command was integrated into Cisco IOS Release
                                          						12.2(11)T and was implemented on the following platforms: Cisco 2600 series,
                                          						Cisco 3600 series, Cisco 3700 series, Cisco 7200 series, and Cisco MC3810. This
                                          						command is supported on the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco
                                          						AS5850 in this release.

### Usage Guidelines

A gatekeeper can handle more than one zone prefix, but a zone prefix
                              		  cannot be shared by more than one gatekeeper. If you have defined a zone prefix
                              		  as being handled by a gatekeeper and now define it as being handled by a second
                              		  gatekeeper, the second assignment cancels the first.

If you need a gatekeeper to handle more than one prefix, but for cost
                              		  reasons you want to be able to group its gateways by prefix usage, there are
                              		  two ways to do it.

The first method is simpler, has less overhead, and is recommended if
                              		  your gateways can be divided into distinct groups, in which each group is to be
                              		  used for a different set of prefixes. For instance, if a group of gateways is
                              		  used for calling area codes 408 and 650, and another group is used for calling
                              		  area code 415, you can use this method. In this case, you define a local zone
                              		  for each set of prefixes and have the group of gateways to be used for that set
                              		  of prefixes register with that specific local zone. Do not define any gateway
                              		  priorities. All gateways in each local zone are treated equally in the
                              		  selection process.

However, if your gateways cannot be cleanly divided into
                              		  nonintersecting groups (for instance, if one gateway is used for calls to 408
                              		  and 415 and another gateway is used for calls to 415 and 650), you can put all
                              		  these gateways in the same local zone and use the gw - priority option
                              		  to define which gateways will be used for which prefixes.

When choosing a gateway, the gatekeeper first looks for the longest
                              		  zone prefix match; then it uses the priority and the gateway status to select
                              		  from the gateways.

If all gateways are available, the gatekeeper chooses the
                              		  highest-priority gateway. If all the highest-priority gateways are busy (see
                              		  the gateway resource threshold command), a lower-priority gateway is selected.

The zone prefix command matches a prefix to a gateway. It
                                          		  does not register the gateway. The gateway must register with the gatekeeper
                                          		  before calls can be completed through that gateway.

## Examples

The following example shows how you can define multiple local zones
                              		  for separating your gateways:

```
Router(config-gk)# zone local gk408or650 xyz.com Router(config-gk)# zone local gk415 xyz.com Router(config-gk)# zone prefix gk408or650 408 ....... Router(config-gk)# zone prefix gk408or650 650.. ..... Router(config-gk)# zone prefix gk415 415...... .
```

Now you need to configure all the gateways to be used for area codes
                              		  408 or 650 to register with gk408or650 and all gateways to be used for area
                              		  code 415 to register with gk415. On Cisco voice gateways, you configure the
                              		  gateways to register with the appropriate gatekeepers by using the h323 voip id command.

The following example shows how you can put all your gateways in the
                              		  same zone but use the gw - priority keyword
                              		  to determine which gateways are used for calling different area codes:

```
Router(config-gk)# zone local localgk xyz.com Router(config-gk)# zone prefix localgk 408....... Router(config-gk)# zone prefix localgk 415....... gw-priority 10 gw1 gw2 Router(config-gk)# zone prefix localgk 650....... gw-priority 0 gw1
```

The commands shown accomplish the following tasks:

Domain xyz.com is
                                    			 assigned to gatekeeper localgk.

Prefix 408...... is assigned to gatekeeper localgk, and no gateway priorities are defined for it; therefore, all gateways
                                    registering to localgk can be used equally for calls to the 408 area code. No special gateway lists are built for the 408.......
                                    prefix; selection is made from the primary list for the zone.

Prefix 415....... is
                                    			 added to gatekeeper localgk, and priority 10 is assigned to gateways gw1 and
                                    			 gw2.

Prefix 650....... is
                                    			 added to gatekeeper localgk, and priority 0 is assigned to gateway gw1.

A priority 0 is assigned to gateway gw1 to exclude it from the
                              		  gateway pool for prefix 650. When gateway gw2 registers with gatekeeper
                              		  localgk, it is added to the gateway pool for each prefix as follows:

For gateway pool for 415,
                                    			 gateway gw2 is set to priority 10.

For gateway pool for 650,
                                    			 gateway gw2 is set to priority 5.

The following example changes gateway gw2 from priority 10 for zone
                              		  415....... to the default priority 5:

```
Router(config)# gatekeeper Router(config-gk)# no zone prefix localgk 415....... gw-priority 10 gw2
```

The following example changes both gateways gw1 and gw2 from priority
                              		  10 for zone 415....... to the default priority 5:

```
Router(config)# gatekeeper Router(config-gk)# no zone prefix localgk 415....... gw-priority 10 gw1 gw2
```

In this example, the prefix 415....... remains assigned to gatekeeper
                              		  localgk. All gateways that do not specify a priority level for this prefix are
                              		  assigned a default priority of 5. The following example removes the prefix and
                              		  all associated gateways and priorities from this gatekeeper:

```
Router(config)# gatekeeper Router(config-gk)# no zone prefix localgk 415.......
```

### Related Commands

Command

Description

register

Configures a gateway to register or deregister a fully
                                          						qualified dial-peer E.164 address with a gatekeeper.

resource threshold

Configures a gateway to report H.323 resource availability
                                          						to the gatekeeper of the gateway.

show call resource voice threshold

Displays the threshold configuration settings and status
                                          						for an H.323 gateway.

show gateway

Displays the current gateway status.

zone local

Specifies a zone controlled by a gatekeeper.

zone remote

Statically specifies a remote zone if DNS is unavailable or
                                          						undesirable.

## zone remote

To statically specify a remote zone if domain name service (DNS) is unavailable or undesirable, use the zone remote command in gatekeeper configuration mode. To remove the remote zone, use the no form of this command.

{ zone remote other-gatekeeper-name other-domain-name other-gatekeeper-ip-address [port-number] [ cost cost-value [ priority priority-value ]] [ foreign-domain ] [ invia inbound gatekeeper ] |  [ outvia outbound gatekeeper ]}

{ no zone remote other-gatekeeper-name other-domain-name other-gatekeeper-ip-address [port-number] [ cost cost-value [ priority priority-value ]] [ foreign-domain ] [ invia inbound gatekeeper ] |  [ outvia outbound gatekeeper ]}

### Syntax Description

other - gatekeeper - name

Name of the remote gatekeeper.

other - domain - name

Domain name of the remote gatekeeper.

other - gatekeeper-ip - address

IP address of the remote gatekeeper.

port-number

(Optional) RAS signaling port number for the remote zone. Range is from 1 to 65535. If the value is not set, the default is
                                          the well-known RAS port number 1719.

cost cost - value

(Optional) Cost of the zone. Range is from 1 to 100. The default is 50.

priority priority-value

(Optional) Priority of the zone. Range is from 1 to 100. The default is 50.

foreign - domain

(Optional) Cluster is in a different administrative domain.

invia

Specifies gatekeeper for calls entering this zone.

inbound gatekeeper

Name of gatekeeper.

outvia

Specifies gatekeeper for calls leaving this zone.

outbound gatekeeper

Name of gatekeeper.

### Command Default

No remote zone is defined. DNS will locate the remote zone.
                              Default RAS port is 1719.
                              Cost value is 50.
                              Priority value is 50.

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

11.3(2)NA

This command was introduced on Cisco 2500 and Cisco 3600 series routers.

12.0(3)T

This command was integrated into Cisco IOS Release 12.0(3)T.

12.1(5)XM

The cost and priority keywords were added.

12.2(2)T

This command was integrated into Cisco IOS Release 12.2(2)T.

12.2(2)XA

The foreign - domain keyword was added.

12.2(4)T

The command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is
                                          not included in this release.

12.2(2)XB1

This command was implemented on Cisco AS5850 universal gateways.

12.2(8)T

Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release.

12.2(11)T

This command was integrated into Cisco IOS Release 12.2(11)T and was implemented on the Cisco 7200 series. This command is
                                          supported on the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release.

12.2(13)T3

The invia and outvia keywords were added.

### Usage Guidelines

Not all gatekeepers have to be in the DNS. For those that are not, use the zone remote command so that the local gatekeeper knows how to access them. In addition, you may wish to improve call response time slightly
                              for frequently accessed zones. If the zone remote command is configured for a particular zone, you do not need to make a DNS lookup transaction.

The maximum number of zones defined on a gatekeeper varies depending on the mode or the call model or both. For example, a
                              directory gatekeeper may be in the mode of being responsible for forwarding Location Request (LRQ) messages and not handling
                              any local registrations and calls; the call model might be E.164 addressed calls instead of H.323-ID addressed calls.

For a directory gatekeeper that does not handle local registrations and calls, the maximum remote zones defined should not
                              exceed 10,000; an additional 4 MB of memory is required to store this maximum number of remote zones.

For a gatekeeper that handles local registrations and only E.164 addressed calls, the number of remote zones defined should
                              not exceed 2000.

For a gatekeeper that handles H.323-ID calls, the number of remote zones defined should not exceed 200.

When there are several remote zones configured, they can be ranked by cost and priority value. A zone with a lower cost value
                              and a higher priority value is given preference over others.

## Examples

The following example configures the local gatekeeper to reach targets of the form xxx .cisco.com by sending queries to the gatekeeper named "sj3.cisco.com" at IP address 10.1.1.12.

```
Router(config)# gatekeeper Router(config-gk)# zone remote sj3.cisco.com cisco.com 10.1.1.12
```

The following example shows how to configure the cost and priority for the gatekeeper "GK10" that serves zone 1.

```
Router(config)# gatekeeper Router(config-gk)# zone remote GK10 Zone1 209.165.200.224 cost 20 priority 5
```

### Related Commands

Command

Description

show proxy h323 calls

Lists each active call on the proxy.

zone local

Specifies a zone controlled by a gatekeeper.

## zone subnet

To configure a gatekeeper to accept discovery and registration
                              		  messages sent by endpoints in designated subnets, use the zone subnet command in gatekeeper configuration mode. To disable the
                              		  gatekeeper from acknowledging discovery and registration messages from subnets
                              		  or to remove subnets entirely, use the no form of this command.

zone subnet local-gatekeeper-name { default | subnet-address { /bits-in-mask | mask-address }} enable

no zone subnet local-gatekeeper-name { default | subnet-address { /bits-in-mask | mask-address }} enable

### Syntax Description

local - gatekeeper - name

Name of the local gatekeeper.

default

Applies to all other subnets that are not specifically
                                          						defined by the zone subnet command.

subnet - address

Address of the subnet being defined.

/ bits - in - mask

Number of bits of the mask to be applied to the subnet
                                          						address.

mask - address

Mask (in dotted string format) to be applied to the subnet
                                          						address.

enable

Gatekeeper accepts discovery and registration from the
                                          						specified subnets.

### Command Default

The local gatekeeper accepts discovery and registration requests from
                              		  all subnets. If the request specifies a gatekeeper name, it must match the
                              		  local gatekeeper name or the request is not accepted.

### Command Modes

Gatekeeper configuration (config-gk)

## Command History

Release

Modification

11.3(2)NA

This command was introduced on Cisco 2500 series and Cisco
                                          						3600 series.

12.0(3)T

This command was integrated into Cisco IOS Release
                                          						12.0(3)T.

### Usage Guidelines

You can use the zone subnet command more than once to create a list of
                              		  subnets controlled by a gatekeeper. The subnet masks do not have to match
                              		  actual subnets in use at your site. For example, to specify a particular
                              		  endpoint, you can supply its address with a 32-bit netmask.

## Examples

The following example starts by disabling the gatekeeper,
                              		  gk1.cisco.com, from accepting discovery and registration messages from all
                              		  subnets. Next, gk1.cisco.com is configured to accept discovery and registration
                              		  messages from all H.323 nodes on the subnet 172.21.127.0.

In addition, gk1.cisco.com is configured to accept discovery and
                              		  registration messages from a particular endpoint with the IP address
                              		  172.21.128.56.

```
no zone subnet gk1.cisco.com default enable
zone subnet gk1.cisco.com 172.21.127.0/24 enable
zone subnet gk1.cisco.com 172.21.128.56/32 enable
```

### Related Commands

Command

Description

show gatekeeper zone status

Displays the status of zones related to a gatekeeper.

zone local

Specifies a zone controlled by a gatekeeper.

| local - zone - name | Name of local zone (synonymous with local gatekeeper). |
|---|---|
| default | Use with the direct or proxied keyword to define the mode of behavior for all remote zones that have not been specially named using the remote - zone remote - zone - name keyword and argument combination. |
| remote - zone remote - zone - name | Name of remote zone (synonymous with remote gatekeeper) for which a special mode of behavior is defined. |
| direct | Configures direct calls (without use of proxies) between endpoints. The local zone (or gatekeeper) offers the local endpoint
                                          IP address instead of the IP address of a local proxy. |
| proxied | Configures calls using proxies between endpoints. The local zone (or gatekeeper) offers the IP address of a local proxy instead
                                          of the local endpoint address. |

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced on the Cisco 2500 series and Cisco 3600 series. |

| Note | The zone access command, configured on your local gatekeeper, affects only the use of proxies for incoming calls (that is, it does not affect
                                          the use of local proxies for outbound calls). When originating a call, a gatekeeper uses a proxy only if the remote gatekeeper
                                          offers a proxy at the remote end. A call between two endpoints in the same zone is always a direct (nonproxied) call. |
|---|---|

| Command | Description |
|---|---|
| show proxy h323 calls | Displays a list of each active call on the proxy. |
| zone local | Specifies a zone controlled by a gatekeeper. |

| gatekeeper - name | Name of the gatekeeper that controls the zone. |
|---|---|
| max - bandwidth | Maximum bidirectional bandwidth, in kbps, allowed in the zone at any one time. |

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced on Cisco 2500 series and Cisco 3600 series. |

| Command | Description |
|---|---|
| show proxy h323 calls | Displays a list of each active call on the proxy. |

| remote - zone - name | Name of the remote zone. |
|---|---|
| circuit - id | ID of the circuit to be associated with the remote zone. |
| override-source-circuitid | (Optional) Specifies whether the source circuit ID of the incoming location request (LRQ) message needs to be overridden with
                                          this keyword. |

| Release | Modification |
|---|---|
| 12.2(11)T | This command was introduced. |
| 12.3(14)T | The override-source-circuitid keyword was added. |

| Command | Description |
|---|---|
| endpoint circuit-id h323id | Assigns a circuit to a non-Cisco endpoint. |
| show gatekeeper circuits | Displays circuit information on the gatekeeper. |
| show gatekeeper endpoint circuits | Displays information for all registered endpoints and carriers for the gatekeeper. |

| cluster - name | Cluster name. |
|---|---|
| local - zone - name | Local zone name. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XB1 | This command was implemented on Cisco AS5850. |

| Command | Description |
|---|---|
| element | Defines component elements of local or remote clusters. |
| zone cluster remote | Defines a remote grouping of gatekeepers, including the gatekeeper that you are configuring. |

| cluster name | Cluster name. |
|---|---|
| cost | (Optional) Cost. |
| cost - value | (Optional) Cost value. Range is from 1 to 100. The default is L50. |
| priority | (Optional) Priority. |
| priority - value | (Optional) Priority value. Range is from 1 to 100. The default is 50. |
| foreign - domain | (Optional) Cluster is in a different administrative domain. |
| invia | Specifies gatekeeper for calls entering this zone. |
| inbound gatekeeper | Name of gatekeeper. |
| outvia | Specifies gatekeeper for calls leaving this zone. |
| outbound gatekeeper | Name of gatekeeper. |

| Release | Modification |
|---|---|
| 12.1(5)XM | This command was introduced. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XA | The foreign - domain keyword was added. |
| 12.2(4)T | This command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400
                                          is not included in this release. |
| 12.2(2)XB1 | This command was implemented on Cisco AS5850. |
| 12.2(13)T3 | The invia and outvia keywords were added. |

| Command | Description |
|---|---|
| element | Defines component elements of local or remote clusters. |
| zone cluster local | Defines a local grouping of gatekeepers, including the gatekeeper that you are configuring. |
| zone local | Specifies a zone controlled by a gatekeeper. |

| gatekeeper-name | The gatekeeper name to be configured. |
|---|---|
| global | Configures the DSCP value globally. |
| dscp | Specifies the DSCP to be configured. |
| dscp-value | The predefined DSCP keyword or its equivalent numeric value. Refer to the table below for more details. |

| Release | Modification |
|---|---|
| 15.0(1)M | This command was introduced. |

| Keyword | Numeric Value | Hexadecimal Value |
|---|---|---|
| default | 0 | 0x00 |
| cs1 | 8 | 0x20 |
| af11 | 10 | 0x28 |
| af12 | 12 | 0X30 |
| af13 | 14 | 0x38 |
| cs2 | 16 | 0x40 |
| af21 | 18 | 0x48 |
| af22 | 20 | 0x50 |
| af23 | 22 | 0x58 |
| cs3 | 24 | 0x60 |
| af31 | 26 | 0x68 |
| af32 | 28 | 0x70 |
| af33 | 30 | 0x78 |
| cs4 | 32 | 0x80 |
| af41 | 34 | 0x88 |
| af42 | 36 | 0x90 |
| af43 | 38 | 0x98 |
| cs5 | 40 | 0xA0 |
| ef | 46 | 0xB8 |
| cs6 | 48 | 0xC0 |
| cs7 | 56 | 0xE0 |

| Command | Description |
|---|---|
| show gatekeeper zone status | Displays the status of the zones related to the gatekeeper. |

| gatekeeper-name | Gatekeeper name or zone name. This is usually the fully domain-qualified host name of the gatekeeper. For example, if the domain-name is cisco.com, the gatekeeper-name might be gk1.cisco.com. However, if the gatekeeper is controlling multiple zones, the gatekeeper-name for each zone should be some unique mnemonic string. |
|---|---|
| domain-name | The domain name served by this gatekeeper. |
| ras-IP-address | (Optional) IP address of one of the interfaces on the gatekeeper. When the gatekeeper responds to gatekeeper discovery messages,
                                          it signals the endpoint or gateway to use this address in future communications. Note Setting this address for one local zone makes it the address used for all local zones. | Note | Setting this address for one local zone makes it the address used for all local zones. |
| Note | Setting this address for one local zone makes it the address used for all local zones. |
| invia | Specifies gatekeeper for calls entering this zone. |
| inbound gatekeeper | Name of gatekeeper. |
| outvia | Specifies gatekeeper for calls leaving this zone. |
| outbound gatekeeper | Name of gatekeeper. |
| enable-intrazone | Forces all intrazone calls to use the via gatekeeper. |

| Note | Setting this address for one local zone makes it the address used for all local zones. |
|---|---|

| Note | The gatekeeper cannot operate without at least one local zone definition. Without local zones, the gatekeeper goes to an inactive
                                          state when the no shutdown command is issued. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced on Cisco 2500 and Cisco 3600 series routers. |
| 12.2(11)T | This command was implemented on the Cisco MC3810 and Cisco 7200 series. |
| 12.3(4)T | The invia , outvia , and enable-intrazone keywords were added. |

| Command | Description |
|---|---|
| show proxy h323 calls | Displays a list of each active call on the proxy. |
| zone subnet | Specifies a zone controlled by a gatekeeper. |

| gatekeeper - name | Name of a local or remote gatekeeper, which must have been
                                          						defined by using the zone local or zone remote command. |
|---|---|
| e164 - prefix | E.164 prefix in standard form followed by dots (.). Each
                                          						dot represents a number in the E.164 address. For example, 212....... is
                                          						matched by 212 and any seven numbers. Note Although a dot representing each digit in an E.164
                                                      						address is the preferred configuration method, you can also enter an asterisk
                                                      						(*) to match any number of digits. | Note | Although a dot representing each digit in an E.164
                                                      						address is the preferred configuration method, you can also enter an asterisk
                                                      						(*) to match any number of digits. |
| Note | Although a dot representing each digit in an E.164
                                                      						address is the preferred configuration method, you can also enter an asterisk
                                                      						(*) to match any number of digits. |
| blast | (Optional) If you list multiple hopoffs, this indicates
                                          						that the LRQs should be sent simultaneously to the gatekeepers based on the
                                          						order in which they were listed. The default is seq . |
| seq | (Optional) If you list multiple hopoffs, this indicates
                                          						that the LRQs should be sent sequentially to the gatekeepers based on the order
                                          						in which they were listed. The default is seq . |
| gw - priority pri - 0 - to - 10 gw - alias | (Optional) Defines how the gatekeeper selects gateways in
                                          						its local zone for calls to numbers beginning with prefix e164-prefix . Do not use this option
                                          						to set priority levels for a prefix assigned to a remote gatekeeper. Range is from 0 to 10, where 0 prevents the gatekeeper from
                                          						using the gateway gw-alias for that prefix and 10
                                          						places the highest priority on gateway gw-alias . The default is 5. To assign the same priority value for one prefix to
                                          						multiple gateways, list all the gateway names after the pri-0-to-10 value. gw-alias name is the H.323 ID of a
                                          						gateway that is registered or will register with the gatekeeper. This name is
                                          						set on the gateway with the h323 - gateway voip h.323 - id command. |

| Note | Although a dot representing each digit in an E.164
                                                      						address is the preferred configuration method, you can also enter an asterisk
                                                      						(*) to match any number of digits. |
|---|---|

| Release | Modification |
|---|---|
| 11.3(6)Q | This command was introduced. |
| 11.3(7)NA | This command was modified for H.323 Version 1. |
| 12.0(5)T | The display format was modified for H.323 Version 2. |
| 12.1(5)XM | The command was implemented on Cisco AS5350 and Cisco
                                          						AS5400. |
| 12.2(4)T | This command was integrated into Cisco IOS Release
                                          						12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is not
                                          						included in this release. |
| 12.2(2)XB1 | This command was implemented on the Cisco AS5850. |
| 12.2(8)T | Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400,
                                          						and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command was integrated into Cisco IOS Release
                                          						12.2(11)T and was implemented on the following platforms: Cisco 2600 series,
                                          						Cisco 3600 series, Cisco 3700 series, Cisco 7200 series, and Cisco MC3810. This
                                          						command is supported on the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco
                                          						AS5850 in this release. |

| Note | The zone prefix command matches a prefix to a gateway. It
                                          		  does not register the gateway. The gateway must register with the gatekeeper
                                          		  before calls can be completed through that gateway. |
|---|---|

| Command | Description |
|---|---|
| register | Configures a gateway to register or deregister a fully
                                          						qualified dial-peer E.164 address with a gatekeeper. |
| resource threshold | Configures a gateway to report H.323 resource availability
                                          						to the gatekeeper of the gateway. |
| show call resource voice threshold | Displays the threshold configuration settings and status
                                          						for an H.323 gateway. |
| show gateway | Displays the current gateway status. |
| zone local | Specifies a zone controlled by a gatekeeper. |
| zone remote | Statically specifies a remote zone if DNS is unavailable or
                                          						undesirable. |

| other - gatekeeper - name | Name of the remote gatekeeper. |
|---|---|
| other - domain - name | Domain name of the remote gatekeeper. |
| other - gatekeeper-ip - address | IP address of the remote gatekeeper. |
| port-number | (Optional) RAS signaling port number for the remote zone. Range is from 1 to 65535. If the value is not set, the default is
                                          the well-known RAS port number 1719. |
| cost cost - value | (Optional) Cost of the zone. Range is from 1 to 100. The default is 50. |
| priority priority-value | (Optional) Priority of the zone. Range is from 1 to 100. The default is 50. |
| foreign - domain | (Optional) Cluster is in a different administrative domain. |
| invia | Specifies gatekeeper for calls entering this zone. |
| inbound gatekeeper | Name of gatekeeper. |
| outvia | Specifies gatekeeper for calls leaving this zone. |
| outbound gatekeeper | Name of gatekeeper. |

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced on Cisco 2500 and Cisco 3600 series routers. |
| 12.0(3)T | This command was integrated into Cisco IOS Release 12.0(3)T. |
| 12.1(5)XM | The cost and priority keywords were added. |
| 12.2(2)T | This command was integrated into Cisco IOS Release 12.2(2)T. |
| 12.2(2)XA | The foreign - domain keyword was added. |
| 12.2(4)T | The command was integrated into Cisco IOS Release 12.2(4)T. Support for the Cisco AS5300, Cisco AS5350, and Cisco AS5400 is
                                          not included in this release. |
| 12.2(2)XB1 | This command was implemented on Cisco AS5850 universal gateways. |
| 12.2(8)T | Support for the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 is not included in this release. |
| 12.2(11)T | This command was integrated into Cisco IOS Release 12.2(11)T and was implemented on the Cisco 7200 series. This command is
                                          supported on the Cisco AS5300, Cisco AS5350, Cisco AS5400, and Cisco AS5850 in this release. |
| 12.2(13)T3 | The invia and outvia keywords were added. |

| Command | Description |
|---|---|
| show proxy h323 calls | Lists each active call on the proxy. |
| zone local | Specifies a zone controlled by a gatekeeper. |

| local - gatekeeper - name | Name of the local gatekeeper. |
|---|---|
| default | Applies to all other subnets that are not specifically
                                          						defined by the zone subnet command. |
| subnet - address | Address of the subnet being defined. |
| / bits - in - mask | Number of bits of the mask to be applied to the subnet
                                          						address. |
| mask - address | Mask (in dotted string format) to be applied to the subnet
                                          						address. |
| enable | Gatekeeper accepts discovery and registration from the
                                          						specified subnets. |

| Release | Modification |
|---|---|
| 11.3(2)NA | This command was introduced on Cisco 2500 series and Cisco
                                          						3600 series. |
| 12.0(3)T | This command was integrated into Cisco IOS Release
                                          						12.0(3)T. |

| Command | Description |
|---|---|
| show gatekeeper zone status | Displays the status of zones related to a gatekeeper. |
| zone local | Specifies a zone controlled by a gatekeeper. |