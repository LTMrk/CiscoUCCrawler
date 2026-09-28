---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-e1455dc44c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_01010101.html
retrieved_at: 2026-08-16T17:37:44.136456+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Multilevel Precedence and Preemption

## Chapter: Configure Multilevel Precedence and Preemption

# Configure Multilevel Precedence and Preemption

## Multilevel Precedence and Preemption Overview

The Multilevel Precedence and Preemption (MLPP) service allows placement of priority calls. Properly validated users can
                           preempt lower priority phone calls with higher priority calls. An authenticated user can preempt calls either to targeted
                           stations or through fully subscribed TDM trunks. This capability assures high-ranking personnel of communication to critical
                           organizations and personnel during network stress situations, such as a national emergency or degraded network situations.

## Multilevel Precedence and Preemption Prerequisites

Supported SCCP or SIP phones. See the Cisco IP Phone Administration Guide and Cisco IP Phone User Guide for your phones for feature support and more information.

## Multilevel Precendence and Preemption Task Flow

### Before you begin

Step 1

To Configure Domains and Domain Lists , perform the following subtasks:

- Configure a Multilevel Precedence and Preemption Domain

- Configure a Resource Priority Namespace Network Domain

- Configure a Resource Priority Namespace Network Domain List

Configure an MLPP domain to specify the devices and resources that are associated with an MLPP subscriber.

Step 2

Configure a Common Device Configuration for Multilevel Precedence and Preemption

A common device configuration includes MLPP-related information that can be applied to multiple users and their devices.
                                          Ensure that each device is associated with a common device configuration. These settings override the enterprise parameter
                                          settings.

Step 3

Configure the Enterprise Parameters for Multilevel Precedence and Preemption

Set enterprise parameters to enable MLPP indication and preemption. If individual devices and devices in common device configurations
                                          have MLPP settings of Default, the MLLP-related enterprise parameters apply to these devices and common device configurations.

Step 4

Configure a Partition for Multilevel Precedence and Preemption

Configure a partition to create a logical grouping of directory numbers (DNs) and route patterns with similar reachability
                                          characteristics. Devices that are typically placed in partitions include DNs and route patterns. These entities associate
                                          with DNs that users dial. For simplicity, partition names usually reflect their characteristics.

Step 5

Configure a Calling Search Space for Multilevel Precedence and Preemption

A calling search space is an ordered list of partitions. Calling
                                          search spaces determine the partitions that calling devices,
                                          including IP phones, softphones, and gateways, can search when
                                          attempting to complete a call.

Step 6

Configure a Route Pattern for Multilevel Precedence and Preemption

Configure route patterns to route or block both internal and external calls.

Step 7

Configure a Translation Pattern for Multilevel Precedence and Preemption

Configure translation patterns to specify how to route a call after it is placed. Configuring translation patterns allows
                                          your system to manipulate calling and called digits as needed. When the system identifies that a pattern match occurred, your
                                          system uses the calling search space that is configured for the translation pattern to perform the subsequent match.

Step 8

Configure Multilevel Precedence and Preemption for Gateways

Configure Cisco Unified Communications Manager to communicate with non-IP telecommunications devices.

Step 9

Configure Multilevel Precedence and Preemption for Phones

Step 10

Configure a Directory Number to Place Multilevel Precedence and Preemption Calls

After you configure a device, you can add a line (directory number) from the updated Device Configuration window.

Step 11

Configure a User Device Profile for Multilevel Precedence and Preemption

When a user profile is assigned to a phone, the phone inherits the configuration of the assigned user, including any CSS that
                                          is associated with the user. The phone CSS can, however, override the user profile. Cisco Unified Communications Manager assigns
                                          the precedence level that is associated with the dialed pattern to the call when a pattern match occurs. The system sets the
                                          call request as a precedence call with the assigned precedence level.

Step 12

Configure the Default Device Profile for Multilevel Precedence and Preemption

Use the default device profile for whenever a user logs on to a phone model for which no user device profile exists.  A default
                                          device profile comprises the set of services and features that are associated with a particular device.

### Configure Domains and Domain Lists

Configure an MLPP domain to specify the devices and resources that are associated with an MLPP subscriber.

Step 1

Configure a Multilevel Precedence and Preemption Domain

Associate devices and resources with an  MLPP subscriber. When an MLPP
                                             subscriber that belongs to a particular domain places a precedence
                                             call to another MLPP subscriber that belongs to the same domain,
                                             the MLPP service can preempt the existing call that the called MLPP
                                             subscriber is on for a higher precedence call. MLPP service
                                             availability does not span across different domains.

The MLPP domain subscription
                                             of the originating user determines the domain of the call and its
                                             connections. Only higher precedence calls in one domain can preempt
                                             connections that calls in the same domain are using.

Step 2

Configure a Resource Priority Namespace Network Domain

Configure namespace domains for a Voice over Secured IP
                                             (VoSIP) network that uses SIP trunks.  Your system prioritizes the SIP-signaled
                                             resources so that those resources can be used most effectively
                                             during emergencies and congestion of telephone circuits, IP
                                             bandwidth, and gateways. Endpoints receive the precedence and
                                             preemption information.

Step 3

Configure a Resource Priority Namespace Network Domain List

Configure a list of acceptable network domains. Incoming calls are compared to the list and processed, if an acceptable network
                                             domain is in the list.

#### Configure a Multilevel Precedence and Preemption Domain

Associate devices and resources with an  MLPP subscriber. When an MLPP
                                    subscriber that belongs to a particular domain places a precedence
                                    call to another MLPP subscriber that belongs to the same domain,
                                    the MLPP service can preempt the existing call that the called MLPP
                                    subscriber is on for a higher precedence call. MLPP service
                                    availability does not span across different domains.

The MLPP domain subscription
                                    of the originating user determines the domain of the call and its
                                    connections. Only higher precedence calls in one domain can preempt
                                    connections that calls in the same domain are using.

Step 1

From Cisco Unified CM Administration, choose System > MLPP > Domain > MLPP Domain .

Step 2

Click Add New .

Step 3

In the Domain Name field, enter the name that you want to assign to the new MLPP domain.

You can enter up to 50 alphanumeric characters, and any combination of spaces, periods (.), hyphens (-), and underscore characters
                                                (_).

Step 4

In the Domain ID field, enter a unique six-character hexadecimal MLPP domain ID.

Domain IDs must fall in the range between 000001 and FFFFFF. (000000 is reserved for the default MLPP domain ID.)

Step 5

Click Save .

#### Configure a Resource Priority Namespace Network Domain

Configure namespace domains for a Voice over Secured IP
                                    (VoSIP) network that uses SIP trunks.  Your system prioritizes the SIP-signaled
                                    resources so that those resources can be used most effectively
                                    during emergencies and congestion of telephone circuits, IP
                                    bandwidth, and gateways. Endpoints receive the precedence and
                                    preemption information.

Step 1

From Cisco Unified CM Administration, System > MLPP > Namespace > Resource Priority Namespace Network Domain .

Step 2

Enter the name for the Resource Priority Namespace Network Domain in the information section. The maximum number of domain
                                             names is 100.

Step 3

Enter a description for the domain name.

The description can include up to 50 characters in any language, but it cannot include double-quotes ("), percentage sign
                                                (%), ampersand (&), or angle brackets (<>).

Step 4

Check the Make this the Default Resource Priority Namespace Network Domain check box  if you want the domain name to be the default.

Step 5

Click Save .

#### Configure a Resource Priority Namespace Network Domain List

Configure a list of acceptable network domains. Incoming calls are compared to the list and processed, if an acceptable network
                                    domain is in the list.

Step 1

From Cisco Unified CM Administration, choose System > MLPP > Namespace > Resource Priority Namespace List .

Step 2

Enter the name for the Resource Priority Namespace List. The maximum number of characters is 50.

Step 3

Enter a description for the list. The description can include up to 50 characters in any language, but it cannot include
                                             double-quotes ("), percentage sign (%), ampersand (&), back-slash (\), or angle brackets (<>).

Step 4

Use the Up and Down Arrows to move a Resource Priority Namespace Network Domain to the Selected Resource Priority Namespaces field.

Step 5

Click Save .

### Configure a Common Device Configuration for Multilevel Precedence and Preemption

A common device configuration includes MLPP-related information that can be applied to multiple users and their devices.
                                 Ensure that each device is associated with a common device configuration. These settings override the enterprise parameter
                                 settings.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration .

Step 2

Perform one of
                                          			 the following tasks:

- Click Find to modify an existing common device configuration and choose a common device configuration from the resulting list.

- Click Add New to add a new common device configuration.

Step 3

Configure the fields on the Common Device Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 4

Click Save .

### Configure the Enterprise Parameters for Multilevel Precedence and Preemption

Set enterprise parameters to enable MLPP indication and preemption. If individual devices and devices in common device configurations
                                 have MLPP settings of Default, the MLLP-related enterprise parameters apply to these devices and common device configurations.

Step 1

Choose System > Enterprise Parameters .

Step 2

Configure the MLPP enterprise parameters on the Enterprise Parameters Configuration window. See the Related Topics section for more information about the parameters and their configuration options.

Step 3

Click Save .

#### Enterprise Parameters for Multilevel Precedence and Preemption

Parameter

Description

MLPP Domain Identifier

Set this
                                                   				parameter to define a domain. Because MLPP service applies to a domain, Cisco Unified Communications Manager marks only connections and resources
                                                   				that belong to calls from MLPP users in a given domain with a precedence level. Cisco Unified Communications Manager can preempt only lower precedence
                                                   				calls from MLPP users in the same domain.

The default is 000000 .

MLPP Indication Status

This parameter specifies whether devices use MLPP tones and special
                                                   				displays to indicate MLPP precedence calls. To enable MLPP indication across
                                                   				the enterprise, set this parameter to MLPP Indication turned on.

The default is MLPP Indication turned
                                                      				off .

MLPP Preemption Setting

This parameter determines whether devices should apply preemption and
                                                   				preemption signaling (such as preemption tones) to accommodate higher
                                                   				precedence calls. To enable MLPP preemption across the enterprise, set this
                                                   				parameter to Forceful Preemption.

The default is No preemption allowed .

Precedence Alternate Party
                                                   			 Timeout

In a precedence call, if the called
                                                   			 party subscribes to alternate party diversion, this timer indicates the seconds
                                                   			 after which Cisco Unified Communications Manager will divert the call to the alternate
                                                   			 party if the called party does not acknowledge preemption or does not answer a
                                                   			 precedence call.

The default is 30 seconds.

Use Standard VM Handling
                                                   			 For Precedence Calls

This parameter determines
                                                   			 whether a precedence call will forward to the voice-messaging system.

If the
                                                   			 parameter is set to False, precedence calls do not forward to the
                                                   			 voice-messaging system. If the parameter is set to True, precedence calls
                                                   			 forward to the voice-messaging system.

For MLPP, the recommended setting for
                                                   			 this parameter is False, as users, not the voice-messaging system, should
                                                   			 always answer precedence calls.

The default is False .

### Configure a Partition for Multilevel Precedence and Preemption

Configure a partition to create a logical grouping of directory numbers (DNs) and route patterns with similar reachability
                                 characteristics. Devices that are typically placed in partitions include DNs and route patterns. These entities associate
                                 with DNs that users dial. For simplicity, partition names usually reflect their characteristics.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition .

Step 2

Click Add
                                             				New to create a new partition.

Step 3

In
                                          			 the Partition
                                             				Name, Description field, enter a name for the partition that is
                                          			 unique to the route plan.

Step 4

Enter a
                                          			 comma (,) after the partition name and enter a description of the partition on
                                          			 the same line.

Step 5

To create
                                          			 multiple partitions, use one line for each partition entry.

Step 6

From the Time
                                             				Schedule drop-down list, choose a time schedule to associate with
                                          			 this partition.

Step 7

Select one
                                          			 of the following radio buttons to configure the Time
                                             				Zone :

- Originating
                                                				  Device —When you select this radio button, the system compares the
                                             				time zone of the calling device to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call.

- Specific Time
                                                				  Zone —After you select this radio button, choose a time zone from
                                             				the drop-down list. The system compares the chosen time zone to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call.

Step 8

Click Save .

#### Partition Naming Guidelines

The list of partitions in a calling search space is limited to a maximum of 1024 characters. This means that the maximum number
                                    of partitions in a CSS varies depending on the length of the partition names. Use the following table to determine the maximum
                                    number of partitions that you can add to a calling search space if partition names are of fixed length.

Partition
                                                					 Name Length

Maximum
                                                					 Number of Partitions

2 characters

340

3 characters

256

4 characters

204

5 characters

172

...

...

10
                                                					 characters

92

15
                                                					 characters

64

### Configure a Calling Search Space for Multilevel Precedence and Preemption

A calling search space is an ordered list of partitions. Calling
                                 search spaces determine the partitions that calling devices,
                                 including IP phones, softphones, and gateways, can search when
                                 attempting to complete a call.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space .

Step 2

Click Add New .

Step 3

In the Name field, enter a name.

Ensure that
                                             				each calling search space name is unique to the system. The name can include up
                                             				to 50 alphanumeric characters and can contain any combination of spaces,
                                             				periods (.), hyphens (-), and underscore characters (_).

Step 4

In the Description field, enter a description.

The
                                             				description can include up to 50 characters in any language, but it cannot
                                             				include double-quotes ("), percentage sign (%), ampersand (&), back-slash
                                             				(\), or angle brackets (<>).

Step 5

From the Available Partitions drop-down list, perform one of
                                          			 the following steps:

- For a single partition,
                                             				select that partition.

- For multiple partitions,
                                             				hold down the Control (CTRL) key, then select the appropriate
                                             				partitions.

Step 6

Select the
                                          			 down arrow between the boxes to move the partitions to the Selected Partitions field.

Step 7

(Optional) Change the priority of selected partitions by using the arrow keys to the right
                                          			 of the Selected Partitions box.

Step 8

Click Save .

### Configure a Route Pattern for Multilevel Precedence and Preemption

Configure route patterns to route or block both internal and external calls.

Step 1

From  Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Pattern .

Step 2

Perform one of the following tasks:

- To modify the settings for an existing route pattern, enter search criteria, click Find , and then choose an existing route pattern from the resulting list.

- To add a new route pattern, click Add New .

Step 3

Configure the fields on the Route Pattern Configuration window. See the Related Topics section for more information about the fields and their configuration options.

Step 4

Click Save .

#### Route Pattern Configuration Fields for Multilevel Precedence and Preemption

Field

Description

Route Pattern

Enter the route pattern, including numbers and wildcards, without spaces. For example, for NANP, enter 9.@ for typical local
                                                access or 8XXX for a typical private network numbering plan. Valid characters include the uppercase characters A, B, C, and
                                                D and \+, which represents the international escape character +.

MLPP Precedence

Choose an MLPP precedence setting for this route pattern from the drop-down list:

Executive Override—Highest precedence setting for MLPP calls.

Flash Override—Second highest precedence setting for MLPP calls.

Flash—Third highest precedence setting for MLPP calls.

Immediate—Fourth highest precedence setting for MLPP calls.

Priority—Fifth highest precedence setting for MLPP calls.

Routine—Lowest precedence setting for MLPP calls.

Default-—Does not override the incoming precedence level but rather lets it pass unchanged.

Apply Call Blocking Percentage

Check this check box to enable the Destination Code Control (DCC) feature. By enabling DCC, all calls other than flash and
                                                higher precedence calls made to the destination are filtered and allowed or disallowed based on the Call Blocking Percentage
                                                quota set for the destination. Flash and higher precedence calls are allowed at all times. DCC is disabled by default.

The Apply Call Blocking Percentage field is enabled only if the MLPP level is immediate, priority, routine or default.

Call Blocking Percentage (%)

Enter the percentage of calls to be blocked for this destination in numerals. This value specifies the percentage of lower
                                                precedence calls made to this destination that get blocked by the route pattern. This percentage limits the lower precedence
                                                calls only; the flash and higher precedence calls made to this destination are allowed at all times

The Call Blocking Percentage (%) field is enabled only if the Apply Call Blocking Percentage check box is checked.

Resource Priority Namespace Network Domain

Choose a Resource Priority Namespace Network Domain from the drop-down list. To configure the Resource Priority Namespace
                                                Network Domains, choose System > MLPP > Namespace > Resource Priority Namespace Network Domain.

### Configure a Translation Pattern for Multilevel Precedence and Preemption

Configure translation patterns to specify how to route a call after it is placed. Configuring translation patterns allows
                                 your system to manipulate calling and called digits as needed. When the system identifies that a pattern match occurred, your
                                 system uses the calling search space that is configured for the translation pattern to perform the subsequent match.

Step 1

In Cisco Unified CM Administration, choose Call Routing > Translation Pattern .

Step 2

Perform one of the following tasks:

- To modify the settings for an existing translation pattern, enter search criteria, click Find , and choose an existing Translation Pattern from the resulting list.

- To add a new translation pattern, click Add New .

Step 3

From the MLPP Precedence drop-down list, choose one of the following settings for this translation pattern:

- Executive Override —Highest precedence setting for MLPP calls.

- Flash Override —Second highest precedence setting for MLPP calls.

- Flash —Third highest precedence setting for MLPP calls.

- Immediate —Fourth highest precedence setting for MLPP calls.

- Priority —Fifth highest precedence setting for MLPP calls.

- Routine —Lowest precedence setting for MLPP calls.

- Default —Does not override the incoming precedence level but rather lets it pass unchanged.

Step 4

From the Resource-Priority Namespace Network Domain drop-down list, choose a resource priority namespace network domain that you configured.

Step 5

From the Calling Search Space drop-down list, choose the calling search space that you configured.

Step 6

Click Save .

### Configure Multilevel Precedence and Preemption for Gateways

Configure Cisco Unified Communications Manager to communicate with non-IP telecommunications devices.

#### Before you begin

Configure one of the following gateways:

Cisco Catalyst 6000 24 port FXS Gateway

Cisco Catalyst 6000 E1 VoIP Gateway

Cisco Catalyst 6000 T1 VoIP Gateway

Cisco DE-30+ Gateway

Cisco DT-24+ Gateway

H.323 Gateway

Step 1

From Cisco Unified CM Administration, choose Device > Gateway

Step 2

Perform one of the following tasks:

- To modify the settings for an existing gateway, enter search criteria, click Find , and choose a gateway from the resulting list.

Click Add New .

From the Gateway Type drop-down list, choose one of the supported gateway models.

Click Next .

Step 3

Configure the MLPP fields on the Gateway Configuration window. See the Related Topics section for more information about the fields and their configuration options.

Step 4

Click Save .

### Configure Multilevel Precedence and Preemption for Phones

Caution

Do not
                                             					 configure a device with the following combination of settings: MLPP Indication
                                             					 is set to Off or Default (when default is Off) while MLPP Preemption is set to
                                             					 Forceful.

Step 1

From Cisco Unified CM Administration, choose Device > Phone .

Step 2

Enter search criteria.

Step 3

Click Find and choose a phone from the resulting list.

Step 4

Configure the MLPP fields on the Phone Configuration window. See the Related Topics section for more information about the fields and their configuration options.

#### Multilevel Precedence and Preemption Settings for Phones

Field

Description

Common Device Configuration

Choose the common device configuration that you configured. The common device configuration includes the attributes (services
                                                or features) that are associated with a particular user.

Calling Search Space

From the drop-down list, choose a calling search space (CSS) that you configured . A calling search space comprises a collection
                                                of partitions that are searched to determine how a dialed number should be routed. The calling search space for the device
                                                and the calling search space for the directory number are used together. The directory number CSS takes precedence over the
                                                device CSS.

MLPP Domain

Choose an MLPP domain from the drop-down list for the MLPP domain that is associated with this device. If you leave the None value, this device inherits its MLPP domain from the value that was set in the common device configuration. If the common
                                                device configuration does not have an MLPP domain setting, this device inherits its MLPP domain from the value that was set
                                                for the MLPP Domain Identifier enterprise parameter.

MLPP Indication

If available, this setting specifies whether a device that can play precedence tones will use the capability when it places
                                                an MLPP precedence call.

From the drop-down list, choose a setting to assign to this device from the following options:

Default —This device inherits its MLPP indication setting from the common device configuration.

Off —This device does not handle nor process indication of an MLPP precedence call.

On —This device handles and processes indication of an MLPP precedence call.

Do not configure a device with the following combination of settings: MLPP Indication is set to Off or Default (when default
                                                            is Off) while MLPP Preemption is set to Forceful.

Turning on MLPP Indication (at the enterprise parameter or device level) disables normal Ring Setting behavior for the lines
                                                            on a device, unless MLPP Indication is turned off (overridden) for the device.

MLPP Preemption

Be aware that this setting is not available on all devices. If available, this setting specifies whether a device that can
                                                preempt calls in progress will use the capability when it places an MLPP precedence call.

From the drop-down list, choose a setting to assign to this device from the following options:

Default

Disabled —This device does not allow preemption of lower precedence calls to take place when necessary for completion of higher precedence
                                                      calls.

Forceful —This device allows preemption of lower precedence calls to take place when necessary for completion of higher precedence
                                                      calls.

### Configure a Directory Number to Place Multilevel Precedence and Preemption Calls

After you configure a device, you can add a line (directory number) from the updated Device Configuration window.

Step 1

From Cisco Unified CM Administration in the Device Configuration window, click Add a new DN for the appropriate line.

Step 2

In the Target
                                             					 (Destination) field, enter the
                                          					 number to which MLPP precedence calls should be diverted if this directory
                                          					 number receives a precedence call and neither this number nor its call forward
                                          					 destination answers the precedence call.

Values can
                                             					 include numeric characters, octothorpe (#), and asterisk (*).

Step 3

From the MLPP
                                             					 Calling Search Space drop-down list, choose the calling search space to associate with the MLPP
                                          					 alternate party target (destination) number.

Step 4

In the MLPP No
                                             					 Answer Ring Duration (seconds) , enter the
                                          					 number of seconds (between 4 and 60) after which an MLPP precedence call is directed to this directory number alternate
                                          party if this directory number
                                          					 and its call-forwarding destination have not answered the precedence call.

Leave this
                                             					 setting blank to use the value that is set in the Precedence Alternate
                                                					 Party Timeout enterprise parameter.

Step 5

Click Save .

### Configure a User Device Profile for Multilevel Precedence and Preemption

When a user profile is assigned to a phone, the phone inherits the configuration of the assigned user, including any CSS that
                                 is associated with the user. The phone CSS can, however, override the user profile. Cisco Unified Communications Manager assigns
                                 the precedence level that is associated with the dialed pattern to the call when a pattern match occurs. The system sets the
                                 call request as a precedence call with the assigned precedence level.

Step 1

From Cisco Unified CM Administration, choose Device > Device Settings > Device Profile .

Step 2

Perform one of the following tasks:

- To modify the settings for an existing device profile, enter search criteria, click Find , and then choose an existing device profile from the resulting list.

Click Add New .

From the Device Profile Type drop-down list, choose a profile type.

Click Next .

From the Device Protocol drop-down list, choose either SIP or SCCP .

Step 3

Click Next .

Step 4

From the MLPP Domain drop-down list, choose an MLLP domain that you configured.

Step 5

From the MLPP Indication drop-down list, choose one of the following settings to specify whether a device that is capable of playing precedence tones
                                          will use the capability when it places an MLPP precedence call:

Default —This device inherits its MLPP indication setting from its device pool.

Off —This device does not handle nor process indication of an MLPP precedence call.

On —This device does handle and process indication of an MLPP precedence call.

Step 6

From the MLPP Preemption drop-down list, choose one of the following settings to specify whether a device that is capable of preempting calls in progress
                                          will use the capability when it places an MLPP precedence call:

Default —This device inherits its MLPP preemption setting from its device pool.

Disabled —This device does not allow preemption of lower precedence calls to take place when necessary for completion of higher precedence
                                                      calls.

Forceful —This device allows preemption of lower precedence calls to take place when necessary for completion of higher precedence
                                                      calls.

Step 7

Click Save .

### Configure the Default Device Profile for Multilevel Precedence and Preemption

Use the default device profile for whenever a user logs on to a phone model for which no user device profile exists.  A default
                                 device profile comprises the set of services and features that are associated with a particular device.

Caution

Do not configure a default device profile with the following combination of settings: MLPP Indication is set to Off or Default
                                             (when default is Off) while MLPP Preemption is set to Forceful.

Step 1

In Cisco Unified CM Administration, choose Device > Device Settings > Default Device Profile .

Step 2

Perform one of the following tasks:

- To modify the settings for an existing default device profile, choose an existing default device profile from the Device Profile Defaults section.

- To add a new default device profile, choose a device profile type from the drop-down list, click Next , choose a device protocol, and then click Next .

Step 3

From the MLPP Domain drop-down list, choose an MLPP domain that you configured to associate to the device.

Step 4

From the MLPP Indication drop-down list, choose one of the following settings to specify whether a device that is capable of playing precedence tones
                                          will use the capability when it places an MLPP precedence call:

- Default —This device inherits its MLPP indication setting from its device pool.

- Off —This device does not handle nor process indication of an MLPP precedence call.

- On —This device does handle and process indication of an MLPP precedence call.

Step 5

From the MLPP Preemption drop-down list, choose one of the following settings to specify whether a device that is capable of preempting calls in progress
                                          will use the capability when it places an MLPP precedence call:

- Default —This device inherits its MLPP preemption setting from its device pool.

- Disabled —This device does not allow preemption of lower precedence calls to take place when necessary for completion of higher precedence
                                             calls.

- Forceful —This device allows preemption of lower precedence calls to take place when necessary for completion of higher precedence
                                             calls.

Step 6

Click Save .

## Multilevel Precedence and Preemption Interactions and Restrictions

### Multilevel Precedence and Preemption Interactions

Feature

Interaction

729 Annex A

729 Annex A is supported.

Cisco Extension Mobility

The MLPP service domain remains associated with a user device profile when a user logs in to a device by using extension mobility.
                                             The MLPP Indication and Preemption settings also propagate with extension mobility. If either the device or the device profile
                                             do not support MLPP, these settings do not propagate.

Cisco Unified Communications Manager Assistant

- When Cisco Unified Communications Manager Assistant handles an MLPP precedence call, Cisco Unified Communications Manager
                                                   Assistant preserves call precedence.

- Cisco Unified Communications Manager Assistant filters MLPP precedence calls in the same manner as it filters all other
                                                   calls. The precedence of a call does not affect whether the call is filtered.

- Because Cisco Unified Communications Manager Assistant does not register the precedence of a call, it does not provide any
                                                   additional indication of the precedence of a call on the assistant console.

Immediate Divert

Immediate Divert diverts calls to voice-messaging mail boxes regardless of the type of call (for example, a precedence call).
                                             When Alternate Party Diversion (call precedence) is activated, Call Forward No Answer (CFNA) is also deactivated.

Resource Reservation Protocol (RSVP)

RSVP supports MLPP inherently. The Cisco Unified Communications Manager System Guide explains how MLPP functions when RSVP
                                             is activated.

Supplementary Services

MLPP interacts with multiple line appearances, call transfer, call forwarding, three-way calling, call pickup, and hunt pilots
                                             as documented in the  and the subsections that describe the interaction with each service.

### Multilevel Precedence and Preemption Restrictions

Restriction

Description

Bandwidth

Cisco Unified Communications Manager preempts lower precedence calls when adjusting video bandwidth for high priority calls.
                                          If the bandwidth is not sufficient to preempt, Cisco Unified Communications Manager instructs endpoints to use previously
                                          reserved lower video bandwidth. When Cisco Unified Communications Manager preempts a video call, the preempted party receives
                                          a preemption tone and the call gets cleared.

Call Detail Records

For the DRSN, CDRs represent precedence levels with values 0, 1, 2, 3, and 4 where 0 specifies Executive Override and 4 specifies
                                          Routine, as used in DSN. CDRs thus do not use the DRSN format.

Common Network Facility Preemption

Common Network Facility Preemption support exists only for T1-CAS and T1-PRI (North American) interfaces on targeted Voice
                                          over IP gateways that Cisco Unified Communications Manager controls by using MGCP protocol and that have been configured as
                                          MLPP Preemption Enabled.

Intercluster trunks

Intercluster trunk MLPP carries precedence information through dialed digits. Domain information does not get preserved and
                                          must be configured per trunk for incoming calls.

Line Groups

MLPP-enabled devices are not supported in line groups. We recommend the following guidelines:

MLPP-enabled devices should not be configured in a line group. Route groups, however, are supported. Both trunk selection
                                                and hunting methods are supported.

If an MLPP-enabled device is configured in a line group or route group, in the event of preemption, if the route list does
                                                not lock onto the device, the preempted call may be rerouted to other devices in the route/hunt list and preemption indication
                                                may be returned only after no devices are able to receive the call.

Route lists can be configured to support either of two algorithms of trunk selection and hunting for precedence calls. In
                                                method 1, perform a preemptive search directly. In method 2, first perform a friendly search. If this search is not successful,
                                                perform a preemptive search. Method 2 requires two iterations through devices in a route list. If route lists are configured
                                                for method 2, in certain scenarios involving line groups, route lists may seem to iterate through the devices twice for precedence
                                                calls.

Look Ahead For Busy

Cisco Unified Communications Manager does not support the Look Ahead for Busy (LFB) option.

MLPP Notification

Only MLPP Indication Enabled devices generate MLPP-related notifications, such as tones and ringers. If a precedence call
                                          terminates at a device that is not MLPP Indication Enabled, no precedence ringer gets applied. If a precedence call originates
                                          from a device that is not MLPP Indication Enabled, no precedence ringback tone is applied. If a device that is not MLPP Indication
                                          Enabled is involved in a call that is preempted (that is, the other side of the call initiated preemption), no preemption
                                          tone gets applied to the device.

Phones and trunks

For phones, devices that are MLPP indication disabled (that is, MLPP Indication is set to Off) cannot be preempted. For trunks,
                                          MLPP indication and preemption function independently.

Ring Setting Behavior

Turning on MLPP Indication (at the enterprise parameter, common device configuration, or device level) disables normal Ring
                                          Setting behavior for the lines on a device, unless MLPP Indication is turned off (overridden) for the device.

SCCP

IOS gateways support the SCCP interface to Cisco Unified Communications Manager. They support BRI and analog phones that appear
                                          on Cisco Unified Communications Manager as supported phone models. SCCP phones support the MLPP feature, and so do some phones
                                          with specific SIP loads. See the relevant phone administration and user guides for Cisco IP phone support information.

MLPP support for supplementary services specifies the following restrictions:

MLPP addresses only the basic Call Pickup feature and Group Call Pickup feature, not Other Group Pickup.

Call Forward All (CFA) support for inbound MLPP calls always forwards the call to the MLPP Alternate Party (MAP) target of
                                                the called party, if the MAP target is configured. In the event of an incorrect configuration (that is, if no MAP target is
                                                specified), the call is rejected, and the calling party receives a reorder tone.

Call Forward No Answer (CFNA) support for inbound MLPP calls forwards the call once to a CFNA target. After the first hop,
                                                if the call is unanswered, the call is sent to the MAP target of the original called party, if the MAP target has been configured.
                                                In the event of an incorrect configuration (that is, if no MAP target is specified), the call gets rejected, and the calling
                                                party receives a reorder tone

Call Forward Busy (CFB) support for inbound MLPP calls forwards the call up to the maximum number that has been configured
                                                for forwarding hops. If the maximum hop count gets reached, the call gets sent to the MAP target of the original called party,
                                                if the MAP target has been configured. In the event of an incorrect configuration (that is, no MAP target is specified), the
                                                call gets rejected, and the calling party receives a reorder tone.

For hunt pilot support, the hunt group algorithm must specify Longest Idle Time, Top Down, or Circular. Ensure the hunt group
                                                options for busy treatment, no answer treatment, and unregistered treatment are set to Try next member, but do not go to the
                                                next group. Preemption only occurs across a single hunt group.

User Access Channel

User Access Channel support exists only for the following Cisco Unified IP Phone models, which must be configured as MLPP
                                          Preemption Enabled:

Cisco Unified IP Phone 7960, 7962, 7965

Cisco Unified IP Phone 7940, 7942, 7945

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | To Configure Domains and Domain Lists , perform the following subtasks: Configure a Multilevel Precedence and Preemption Domain Configure a Resource Priority Namespace Network Domain Configure a Resource Priority Namespace Network Domain List | Configure an MLPP domain to specify the devices and resources that are associated with an MLPP subscriber. |
| Step 2 | Configure a Common Device Configuration for Multilevel Precedence and Preemption | A common device configuration includes MLPP-related information that can be applied to multiple users and their devices.
                                          Ensure that each device is associated with a common device configuration. These settings override the enterprise parameter
                                          settings. |
| Step 3 | Configure the Enterprise Parameters for Multilevel Precedence and Preemption | Set enterprise parameters to enable MLPP indication and preemption. If individual devices and devices in common device configurations
                                          have MLPP settings of Default, the MLLP-related enterprise parameters apply to these devices and common device configurations. |
| Step 4 | Configure a Partition for Multilevel Precedence and Preemption | Configure a partition to create a logical grouping of directory numbers (DNs) and route patterns with similar reachability
                                          characteristics. Devices that are typically placed in partitions include DNs and route patterns. These entities associate
                                          with DNs that users dial. For simplicity, partition names usually reflect their characteristics. |
| Step 5 | Configure a Calling Search Space for Multilevel Precedence and Preemption | A calling search space is an ordered list of partitions. Calling
                                          search spaces determine the partitions that calling devices,
                                          including IP phones, softphones, and gateways, can search when
                                          attempting to complete a call. |
| Step 6 | Configure a Route Pattern for Multilevel Precedence and Preemption | Configure route patterns to route or block both internal and external calls. |
| Step 7 | Configure a Translation Pattern for Multilevel Precedence and Preemption | Configure translation patterns to specify how to route a call after it is placed. Configuring translation patterns allows
                                          your system to manipulate calling and called digits as needed. When the system identifies that a pattern match occurred, your
                                          system uses the calling search space that is configured for the translation pattern to perform the subsequent match. |
| Step 8 | Configure Multilevel Precedence and Preemption for Gateways | Configure Cisco Unified Communications Manager to communicate with non-IP telecommunications devices. |
| Step 9 | Configure Multilevel Precedence and Preemption for Phones |  |
| Step 10 | Configure a Directory Number to Place Multilevel Precedence and Preemption Calls | After you configure a device, you can add a line (directory number) from the updated Device Configuration window. |
| Step 11 | Configure a User Device Profile for Multilevel Precedence and Preemption | When a user profile is assigned to a phone, the phone inherits the configuration of the assigned user, including any CSS that
                                          is associated with the user. The phone CSS can, however, override the user profile. Cisco Unified Communications Manager assigns
                                          the precedence level that is associated with the dialed pattern to the call when a pattern match occurs. The system sets the
                                          call request as a precedence call with the assigned precedence level. |
| Step 12 | Configure the Default Device Profile for Multilevel Precedence and Preemption | Use the default device profile for whenever a user logs on to a phone model for which no user device profile exists.  A default
                                          device profile comprises the set of services and features that are associated with a particular device. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Multilevel Precedence and Preemption Domain | Associate devices and resources with an  MLPP subscriber. When an MLPP
                                             subscriber that belongs to a particular domain places a precedence
                                             call to another MLPP subscriber that belongs to the same domain,
                                             the MLPP service can preempt the existing call that the called MLPP
                                             subscriber is on for a higher precedence call. MLPP service
                                             availability does not span across different domains. The MLPP domain subscription
                                             of the originating user determines the domain of the call and its
                                             connections. Only higher precedence calls in one domain can preempt
                                             connections that calls in the same domain are using. |
| Step 2 | Configure a Resource Priority Namespace Network Domain | Configure namespace domains for a Voice over Secured IP
                                             (VoSIP) network that uses SIP trunks.  Your system prioritizes the SIP-signaled
                                             resources so that those resources can be used most effectively
                                             during emergencies and congestion of telephone circuits, IP
                                             bandwidth, and gateways. Endpoints receive the precedence and
                                             preemption information. |
| Step 3 | Configure a Resource Priority Namespace Network Domain List | Configure a list of acceptable network domains. Incoming calls are compared to the list and processed, if an acceptable network
                                             domain is in the list. |

| Step 1 | From Cisco Unified CM Administration, choose System > MLPP > Domain > MLPP Domain . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Domain Name field, enter the name that you want to assign to the new MLPP domain. You can enter up to 50 alphanumeric characters, and any combination of spaces, periods (.), hyphens (-), and underscore characters
                                                (_). |
| Step 4 | In the Domain ID field, enter a unique six-character hexadecimal MLPP domain ID. Domain IDs must fall in the range between 000001 and FFFFFF. (000000 is reserved for the default MLPP domain ID.) |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, System > MLPP > Namespace > Resource Priority Namespace Network Domain . |
|---|---|
| Step 2 | Enter the name for the Resource Priority Namespace Network Domain in the information section. The maximum number of domain
                                             names is 100. |
| Step 3 | Enter a description for the domain name. The description can include up to 50 characters in any language, but it cannot include double-quotes ("), percentage sign
                                                (%), ampersand (&), or angle brackets (<>). |
| Step 4 | Check the Make this the Default Resource Priority Namespace Network Domain check box  if you want the domain name to be the default. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > MLPP > Namespace > Resource Priority Namespace List . |
|---|---|
| Step 2 | Enter the name for the Resource Priority Namespace List. The maximum number of characters is 50. |
| Step 3 | Enter a description for the list. The description can include up to 50 characters in any language, but it cannot include
                                             double-quotes ("), percentage sign (%), ampersand (&), back-slash (\), or angle brackets (<>). |
| Step 4 | Use the Up and Down Arrows to move a Resource Priority Namespace Network Domain to the Selected Resource Priority Namespaces field. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Common Device Configuration . |
|---|---|
| Step 2 | Perform one of
                                          			 the following tasks: Click Find to modify an existing common device configuration and choose a common device configuration from the resulting list. Click Add New to add a new common device configuration. |
| Step 3 | Configure the fields on the Common Device Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 4 | Click Save . |

| Step 1 | Choose System > Enterprise Parameters . |
|---|---|
| Step 2 | Configure the MLPP enterprise parameters on the Enterprise Parameters Configuration window. See the Related Topics section for more information about the parameters and their configuration options. |
| Step 3 | Click Save . |

| Parameter | Description |
|---|---|
| MLPP Domain Identifier | Set this
                                                   				parameter to define a domain. Because MLPP service applies to a domain, Cisco Unified Communications Manager marks only connections and resources
                                                   				that belong to calls from MLPP users in a given domain with a precedence level. Cisco Unified Communications Manager can preempt only lower precedence
                                                   				calls from MLPP users in the same domain. The default is 000000 . |
| MLPP Indication Status | This parameter specifies whether devices use MLPP tones and special
                                                   				displays to indicate MLPP precedence calls. To enable MLPP indication across
                                                   				the enterprise, set this parameter to MLPP Indication turned on. The default is MLPP Indication turned
                                                      				off . |
| MLPP Preemption Setting | This parameter determines whether devices should apply preemption and
                                                   				preemption signaling (such as preemption tones) to accommodate higher
                                                   				precedence calls. To enable MLPP preemption across the enterprise, set this
                                                   				parameter to Forceful Preemption. The default is No preemption allowed . |
| Precedence Alternate Party
                                                   			 Timeout | In a precedence call, if the called
                                                   			 party subscribes to alternate party diversion, this timer indicates the seconds
                                                   			 after which Cisco Unified Communications Manager will divert the call to the alternate
                                                   			 party if the called party does not acknowledge preemption or does not answer a
                                                   			 precedence call. The default is 30 seconds. |
| Use Standard VM Handling
                                                   			 For Precedence Calls | This parameter determines
                                                   			 whether a precedence call will forward to the voice-messaging system. If the
                                                   			 parameter is set to False, precedence calls do not forward to the
                                                   			 voice-messaging system. If the parameter is set to True, precedence calls
                                                   			 forward to the voice-messaging system. For MLPP, the recommended setting for
                                                   			 this parameter is False, as users, not the voice-messaging system, should
                                                   			 always answer precedence calls. The default is False . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition . |
|---|---|
| Step 2 | Click Add
                                             				New to create a new partition. |
| Step 3 | In
                                          			 the Partition
                                             				Name, Description field, enter a name for the partition that is
                                          			 unique to the route plan. Partition
                                          			 names can contain alphanumeric characters, as well as spaces, hyphens (-), and
                                          			 underscore characters (_). See the online help for guidelines about partition
                                          			 names. |
| Step 4 | Enter a
                                          			 comma (,) after the partition name and enter a description of the partition on
                                          			 the same line. The
                                          			 description can contain up to 50 characters in any language, but it cannot
                                          			 include double quotes ("), percentage sign (%), ampersand (&), backslash
                                          			 (\), angle brackets (<>), or square brackets ([ ]). If you do
                                          			 not enter a description, Cisco Unified Communications Manager automatically
                                          			 enters the partition name in this field. |
| Step 5 | To create
                                          			 multiple partitions, use one line for each partition entry. |
| Step 6 | From the Time
                                             				Schedule drop-down list, choose a time schedule to associate with
                                          			 this partition. The time
                                          			 schedule specifies when the partition is available to receive incoming calls.
                                          			 If you choose None , the partition remains active at all times. |
| Step 7 | Select one
                                          			 of the following radio buttons to configure the Time
                                             				Zone : Originating
                                                				  Device —When you select this radio button, the system compares the
                                             				time zone of the calling device to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call. Specific Time
                                                				  Zone —After you select this radio button, choose a time zone from
                                             				the drop-down list. The system compares the chosen time zone to the Time Schedule to determine whether the partition is
                                             				available is available to receive an incoming call. |
| Step 8 | Click Save . |

| Partition
                                                					 Name Length | Maximum
                                                					 Number of Partitions |
|---|---|
| 2 characters | 340 |
| 3 characters | 256 |
| 4 characters | 204 |
| 5 characters | 172 |
| ... | ... |
| 10
                                                					 characters | 92 |
| 15
                                                					 characters | 64 |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Calling Search Space . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | In the Name field, enter a name. Ensure that
                                             				each calling search space name is unique to the system. The name can include up
                                             				to 50 alphanumeric characters and can contain any combination of spaces,
                                             				periods (.), hyphens (-), and underscore characters (_). |
| Step 4 | In the Description field, enter a description. The
                                             				description can include up to 50 characters in any language, but it cannot
                                             				include double-quotes ("), percentage sign (%), ampersand (&), back-slash
                                             				(\), or angle brackets (<>). |
| Step 5 | From the Available Partitions drop-down list, perform one of
                                          			 the following steps: For a single partition,
                                             				select that partition. For multiple partitions,
                                             				hold down the Control (CTRL) key, then select the appropriate
                                             				partitions. |
| Step 6 | Select the
                                          			 down arrow between the boxes to move the partitions to the Selected Partitions field. |
| Step 7 | (Optional) Change the priority of selected partitions by using the arrow keys to the right
                                          			 of the Selected Partitions box. |
| Step 8 | Click Save . |

| Step 1 | From  Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Pattern . |
|---|---|
| Step 2 | Perform one of the following tasks: To modify the settings for an existing route pattern, enter search criteria, click Find , and then choose an existing route pattern from the resulting list. To add a new route pattern, click Add New . |
| Step 3 | Configure the fields on the Route Pattern Configuration window. See the Related Topics section for more information about the fields and their configuration options. |
| Step 4 | Click Save . |

| Field | Description |
|---|---|
| Route Pattern | Enter the route pattern, including numbers and wildcards, without spaces. For example, for NANP, enter 9.@ for typical local
                                                access or 8XXX for a typical private network numbering plan. Valid characters include the uppercase characters A, B, C, and
                                                D and \+, which represents the international escape character +. |
| MLPP Precedence | Choose an MLPP precedence setting for this route pattern from the drop-down list: Executive Override—Highest precedence setting for MLPP calls. Flash Override—Second highest precedence setting for MLPP calls. Flash—Third highest precedence setting for MLPP calls. Immediate—Fourth highest precedence setting for MLPP calls. Priority—Fifth highest precedence setting for MLPP calls. Routine—Lowest precedence setting for MLPP calls. Default-—Does not override the incoming precedence level but rather lets it pass unchanged. |
| Apply Call Blocking Percentage | Check this check box to enable the Destination Code Control (DCC) feature. By enabling DCC, all calls other than flash and
                                                higher precedence calls made to the destination are filtered and allowed or disallowed based on the Call Blocking Percentage
                                                quota set for the destination. Flash and higher precedence calls are allowed at all times. DCC is disabled by default. The Apply Call Blocking Percentage field is enabled only if the MLPP level is immediate, priority, routine or default. |
| Call Blocking Percentage (%) | Enter the percentage of calls to be blocked for this destination in numerals. This value specifies the percentage of lower
                                                precedence calls made to this destination that get blocked by the route pattern. This percentage limits the lower precedence
                                                calls only; the flash and higher precedence calls made to this destination are allowed at all times The Call Blocking Percentage (%) field is enabled only if the Apply Call Blocking Percentage check box is checked. |
| Resource Priority Namespace Network Domain | Choose a Resource Priority Namespace Network Domain from the drop-down list. To configure the Resource Priority Namespace
                                                Network Domains, choose System > MLPP > Namespace > Resource Priority Namespace Network Domain. |

| Step 1 | In Cisco Unified CM Administration, choose Call Routing > Translation Pattern . |
|---|---|
| Step 2 | Perform one of the following tasks: To modify the settings for an existing translation pattern, enter search criteria, click Find , and choose an existing Translation Pattern from the resulting list. To add a new translation pattern, click Add New . |
| Step 3 | From the MLPP Precedence drop-down list, choose one of the following settings for this translation pattern: Executive Override —Highest precedence setting for MLPP calls. Flash Override —Second highest precedence setting for MLPP calls. Flash —Third highest precedence setting for MLPP calls. Immediate —Fourth highest precedence setting for MLPP calls. Priority —Fifth highest precedence setting for MLPP calls. Routine —Lowest precedence setting for MLPP calls. Default —Does not override the incoming precedence level but rather lets it pass unchanged. |
| Step 4 | From the Resource-Priority Namespace Network Domain drop-down list, choose a resource priority namespace network domain that you configured. |
| Step 5 | From the Calling Search Space drop-down list, choose the calling search space that you configured. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Gateway |
|---|---|
| Step 2 | Perform one of the following tasks: To modify the settings for an existing gateway, enter search criteria, click Find , and choose a gateway from the resulting list. To add a new gateway: Click Add New . From the Gateway Type drop-down list, choose one of the supported gateway models. Click Next . |
| Step 3 | Configure the MLPP fields on the Gateway Configuration window. See the Related Topics section for more information about the fields and their configuration options. |
| Step 4 | Click Save . |

| Caution | Do not
                                             					 configure a device with the following combination of settings: MLPP Indication
                                             					 is set to Off or Default (when default is Off) while MLPP Preemption is set to
                                             					 Forceful. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Device > Phone . |
|---|---|
| Step 2 | Enter search criteria. |
| Step 3 | Click Find and choose a phone from the resulting list. |
| Step 4 | Configure the MLPP fields on the Phone Configuration window. See the Related Topics section for more information about the fields and their configuration options. |

| MLPP Settings for Phones Field | Description |
|---|---|
| Common Device Configuration | Choose the common device configuration that you configured. The common device configuration includes the attributes (services
                                                or features) that are associated with a particular user. |
| Calling Search Space | From the drop-down list, choose a calling search space (CSS) that you configured . A calling search space comprises a collection
                                                of partitions that are searched to determine how a dialed number should be routed. The calling search space for the device
                                                and the calling search space for the directory number are used together. The directory number CSS takes precedence over the
                                                device CSS. |
| MLPP Domain | Choose an MLPP domain from the drop-down list for the MLPP domain that is associated with this device. If you leave the None value, this device inherits its MLPP domain from the value that was set in the common device configuration. If the common
                                                device configuration does not have an MLPP domain setting, this device inherits its MLPP domain from the value that was set
                                                for the MLPP Domain Identifier enterprise parameter. |
| MLPP Indication | If available, this setting specifies whether a device that can play precedence tones will use the capability when it places
                                                an MLPP precedence call. From the drop-down list, choose a setting to assign to this device from the following options: Default —This device inherits its MLPP indication setting from the common device configuration. Off —This device does not handle nor process indication of an MLPP precedence call. On —This device handles and processes indication of an MLPP precedence call. Note Do not configure a device with the following combination of settings: MLPP Indication is set to Off or Default (when default
                                                            is Off) while MLPP Preemption is set to Forceful. Turning on MLPP Indication (at the enterprise parameter or device level) disables normal Ring Setting behavior for the lines
                                                            on a device, unless MLPP Indication is turned off (overridden) for the device. | Note | Do not configure a device with the following combination of settings: MLPP Indication is set to Off or Default (when default
                                                            is Off) while MLPP Preemption is set to Forceful. Turning on MLPP Indication (at the enterprise parameter or device level) disables normal Ring Setting behavior for the lines
                                                            on a device, unless MLPP Indication is turned off (overridden) for the device. |
| Note | Do not configure a device with the following combination of settings: MLPP Indication is set to Off or Default (when default
                                                            is Off) while MLPP Preemption is set to Forceful. Turning on MLPP Indication (at the enterprise parameter or device level) disables normal Ring Setting behavior for the lines
                                                            on a device, unless MLPP Indication is turned off (overridden) for the device. |
| MLPP Preemption | Be aware that this setting is not available on all devices. If available, this setting specifies whether a device that can
                                                preempt calls in progress will use the capability when it places an MLPP precedence call. From the drop-down list, choose a setting to assign to this device from the following options: Default —This device inherits its MLPP preemption setting from the common device configuration. Disabled —This device does not allow preemption of lower precedence calls to take place when necessary for completion of higher precedence
                                                      calls. Forceful —This device allows preemption of lower precedence calls to take place when necessary for completion of higher precedence
                                                      calls. |

| Note | Do not configure a device with the following combination of settings: MLPP Indication is set to Off or Default (when default
                                                            is Off) while MLPP Preemption is set to Forceful. Turning on MLPP Indication (at the enterprise parameter or device level) disables normal Ring Setting behavior for the lines
                                                            on a device, unless MLPP Indication is turned off (overridden) for the device. |
|---|---|

| Step 1 | From Cisco Unified CM Administration in the Device Configuration window, click Add a new DN for the appropriate line. |
|---|---|
| Step 2 | In the Target
                                             					 (Destination) field, enter the
                                          					 number to which MLPP precedence calls should be diverted if this directory
                                          					 number receives a precedence call and neither this number nor its call forward
                                          					 destination answers the precedence call. Values can
                                             					 include numeric characters, octothorpe (#), and asterisk (*). |
| Step 3 | From the MLPP
                                             					 Calling Search Space drop-down list, choose the calling search space to associate with the MLPP
                                          					 alternate party target (destination) number. |
| Step 4 | In the MLPP No
                                             					 Answer Ring Duration (seconds) , enter the
                                          					 number of seconds (between 4 and 60) after which an MLPP precedence call is directed to this directory number alternate
                                          party if this directory number
                                          					 and its call-forwarding destination have not answered the precedence call. Leave this
                                             					 setting blank to use the value that is set in the Precedence Alternate
                                                					 Party Timeout enterprise parameter. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Device > Device Settings > Device Profile . |
|---|---|
| Step 2 | Perform one of the following tasks: To modify the settings for an existing device profile, enter search criteria, click Find , and then choose an existing device profile from the resulting list. To add a new device profile: Click Add New . From the Device Profile Type drop-down list, choose a profile type. Click Next . From the Device Protocol drop-down list, choose either SIP or SCCP . |
| Step 3 | Click Next . |
| Step 4 | From the MLPP Domain drop-down list, choose an MLLP domain that you configured. |
| Step 5 | From the MLPP Indication drop-down list, choose one of the following settings to specify whether a device that is capable of playing precedence tones
                                          will use the capability when it places an MLPP precedence call: Default —This device inherits its MLPP indication setting from its device pool. Off —This device does not handle nor process indication of an MLPP precedence call. On —This device does handle and process indication of an MLPP precedence call. |
| Step 6 | From the MLPP Preemption drop-down list, choose one of the following settings to specify whether a device that is capable of preempting calls in progress
                                          will use the capability when it places an MLPP precedence call: Default —This device inherits its MLPP preemption setting from its device pool. Disabled —This device does not allow preemption of lower precedence calls to take place when necessary for completion of higher precedence
                                                      calls. Forceful —This device allows preemption of lower precedence calls to take place when necessary for completion of higher precedence
                                                      calls. |
| Step 7 | Click Save . |

| Caution | Do not configure a default device profile with the following combination of settings: MLPP Indication is set to Off or Default
                                             (when default is Off) while MLPP Preemption is set to Forceful. |
|---|---|

| Step 1 | In Cisco Unified CM Administration, choose Device > Device Settings > Default Device Profile . |
|---|---|
| Step 2 | Perform one of the following tasks: To modify the settings for an existing default device profile, choose an existing default device profile from the Device Profile Defaults section. To add a new default device profile, choose a device profile type from the drop-down list, click Next , choose a device protocol, and then click Next . |
| Step 3 | From the MLPP Domain drop-down list, choose an MLPP domain that you configured to associate to the device. |
| Step 4 | From the MLPP Indication drop-down list, choose one of the following settings to specify whether a device that is capable of playing precedence tones
                                          will use the capability when it places an MLPP precedence call: Default —This device inherits its MLPP indication setting from its device pool. Off —This device does not handle nor process indication of an MLPP precedence call. On —This device does handle and process indication of an MLPP precedence call. |
| Step 5 | From the MLPP Preemption drop-down list, choose one of the following settings to specify whether a device that is capable of preempting calls in progress
                                          will use the capability when it places an MLPP precedence call: Default —This device inherits its MLPP preemption setting from its device pool. Disabled —This device does not allow preemption of lower precedence calls to take place when necessary for completion of higher precedence
                                             calls. Forceful —This device allows preemption of lower precedence calls to take place when necessary for completion of higher precedence
                                             calls. |
| Step 6 | Click Save . |

| Feature | Interaction |
|---|---|
| 729 Annex A | 729 Annex A is supported. |
| Cisco Extension Mobility | The MLPP service domain remains associated with a user device profile when a user logs in to a device by using extension mobility.
                                             The MLPP Indication and Preemption settings also propagate with extension mobility. If either the device or the device profile
                                             do not support MLPP, these settings do not propagate. |
| Cisco Unified Communications Manager Assistant | MLPP interacts with Cisco Unified Communications Manager Assistant as follows: When Cisco Unified Communications Manager Assistant handles an MLPP precedence call, Cisco Unified Communications Manager
                                                   Assistant preserves call precedence. Cisco Unified Communications Manager Assistant filters MLPP precedence calls in the same manner as it filters all other
                                                   calls. The precedence of a call does not affect whether the call is filtered. Because Cisco Unified Communications Manager Assistant does not register the precedence of a call, it does not provide any
                                                   additional indication of the precedence of a call on the assistant console. |
| Immediate Divert | Immediate Divert diverts calls to voice-messaging mail boxes regardless of the type of call (for example, a precedence call).
                                             When Alternate Party Diversion (call precedence) is activated, Call Forward No Answer (CFNA) is also deactivated. |
| Resource Reservation Protocol (RSVP) | RSVP supports MLPP inherently. The Cisco Unified Communications Manager System Guide explains how MLPP functions when RSVP
                                             is activated. |
| Supplementary Services | MLPP interacts with multiple line appearances, call transfer, call forwarding, three-way calling, call pickup, and hunt pilots
                                             as documented in the  and the subsections that describe the interaction with each service. |

| Restriction | Description |
|---|---|
| Bandwidth | Cisco Unified Communications Manager preempts lower precedence calls when adjusting video bandwidth for high priority calls.
                                          If the bandwidth is not sufficient to preempt, Cisco Unified Communications Manager instructs endpoints to use previously
                                          reserved lower video bandwidth. When Cisco Unified Communications Manager preempts a video call, the preempted party receives
                                          a preemption tone and the call gets cleared. |
| Call Detail Records | For the DRSN, CDRs represent precedence levels with values 0, 1, 2, 3, and 4 where 0 specifies Executive Override and 4 specifies
                                          Routine, as used in DSN. CDRs thus do not use the DRSN format. |
| Common Network Facility Preemption | Common Network Facility Preemption support exists only for T1-CAS and T1-PRI (North American) interfaces on targeted Voice
                                          over IP gateways that Cisco Unified Communications Manager controls by using MGCP protocol and that have been configured as
                                          MLPP Preemption Enabled. |
| Intercluster trunks | Intercluster trunk MLPP carries precedence information through dialed digits. Domain information does not get preserved and
                                          must be configured per trunk for incoming calls. |
| Line Groups | MLPP-enabled devices are not supported in line groups. We recommend the following guidelines: MLPP-enabled devices should not be configured in a line group. Route groups, however, are supported. Both trunk selection
                                                and hunting methods are supported. If an MLPP-enabled device is configured in a line group or route group, in the event of preemption, if the route list does
                                                not lock onto the device, the preempted call may be rerouted to other devices in the route/hunt list and preemption indication
                                                may be returned only after no devices are able to receive the call. Route lists can be configured to support either of two algorithms of trunk selection and hunting for precedence calls. In
                                                method 1, perform a preemptive search directly. In method 2, first perform a friendly search. If this search is not successful,
                                                perform a preemptive search. Method 2 requires two iterations through devices in a route list. If route lists are configured
                                                for method 2, in certain scenarios involving line groups, route lists may seem to iterate through the devices twice for precedence
                                                calls. |
| Look Ahead For Busy | Cisco Unified Communications Manager does not support the Look Ahead for Busy (LFB) option. |
| MLPP Notification | Only MLPP Indication Enabled devices generate MLPP-related notifications, such as tones and ringers. If a precedence call
                                          terminates at a device that is not MLPP Indication Enabled, no precedence ringer gets applied. If a precedence call originates
                                          from a device that is not MLPP Indication Enabled, no precedence ringback tone is applied. If a device that is not MLPP Indication
                                          Enabled is involved in a call that is preempted (that is, the other side of the call initiated preemption), no preemption
                                          tone gets applied to the device. |
| Phones and trunks | For phones, devices that are MLPP indication disabled (that is, MLPP Indication is set to Off) cannot be preempted. For trunks,
                                          MLPP indication and preemption function independently. |
| Ring Setting Behavior | Turning on MLPP Indication (at the enterprise parameter, common device configuration, or device level) disables normal Ring
                                          Setting behavior for the lines on a device, unless MLPP Indication is turned off (overridden) for the device. |
| SCCP | IOS gateways support the SCCP interface to Cisco Unified Communications Manager. They support BRI and analog phones that appear
                                          on Cisco Unified Communications Manager as supported phone models. SCCP phones support the MLPP feature, and so do some phones
                                          with specific SIP loads. See the relevant phone administration and user guides for Cisco IP phone support information. |
| Supplementary Services | MLPP support for supplementary services specifies the following restrictions: MLPP addresses only the basic Call Pickup feature and Group Call Pickup feature, not Other Group Pickup. Call Forward All (CFA) support for inbound MLPP calls always forwards the call to the MLPP Alternate Party (MAP) target of
                                                the called party, if the MAP target is configured. In the event of an incorrect configuration (that is, if no MAP target is
                                                specified), the call is rejected, and the calling party receives a reorder tone. Call Forward No Answer (CFNA) support for inbound MLPP calls forwards the call once to a CFNA target. After the first hop,
                                                if the call is unanswered, the call is sent to the MAP target of the original called party, if the MAP target has been configured.
                                                In the event of an incorrect configuration (that is, if no MAP target is specified), the call gets rejected, and the calling
                                                party receives a reorder tone . Call Forward Busy (CFB) support for inbound MLPP calls forwards the call up to the maximum number that has been configured
                                                for forwarding hops. If the maximum hop count gets reached, the call gets sent to the MAP target of the original called party,
                                                if the MAP target has been configured. In the event of an incorrect configuration (that is, no MAP target is specified), the
                                                call gets rejected, and the calling party receives a reorder tone. For hunt pilot support, the hunt group algorithm must specify Longest Idle Time, Top Down, or Circular. Ensure the hunt group
                                                options for busy treatment, no answer treatment, and unregistered treatment are set to Try next member, but do not go to the
                                                next group. Preemption only occurs across a single hunt group. |
| User Access Channel | User Access Channel support exists only for the following Cisco Unified IP Phone models, which must be configured as MLPP
                                          Preemption Enabled: Cisco Unified IP Phone 7960, 7962, 7965 Cisco Unified IP Phone 7940, 7942, 7945 |