---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su2-systemconfig-cucm-b-system-configuration-guide-1251su2--33dc59d25d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU2/systemConfig/cucm_b_system-configuration-guide-1251su2/cucm_b_system-configuration-guide-for-cisco-1251su2_chapter_010110.html
retrieved_at: 2026-08-16T17:46:39.261052+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: July 31, 2025

Chapter: Calling Party Normalization

## Chapter: Calling Party Normalization

# Calling Party Normalization

## Calling Party
                        	 Normalization Overview

Calling Party
                              		  Normalization allows you to globalize and localize phone numbers so that the
                              		  appropriate calling presentation displays on the phone. Calling Party
                              		  Normalization enhances the dialing capabilities of some phones and improves
                              		  callback functionality when a call is routed to multiple geographic locations.
                              		  The feature allows you to map a global calling party number to its localized
                              		  variant such that a phone can return a call without modifying the directory
                              		  number in the call log directories on the phone.

### Globalization
                              		  of the Calling Party Number

By configuring a
                              		  Calling Party Number Type and prefixes in Cisco Unified CM Administration, you
                              		  can set Cisco Unified Communications Manager to reformat the calling party
                              		  number that displays on the called phone to a globalized version that includes
                              		  prefixes such as international country codes, thereby allowing the number to be
                              		  dialed from anywhere in the world.

Cisco Unified
                              		  Communications Manager uses various number patterns, such as route patterns or
                              		  translation patterns, along with the value for the Calling Party Number Type to
                              		  globalize a phone number. For example, you can configure Cisco Unified
                              		  Communications Manager to take a localized German phone number of 069XXXXXXX
                              		  with a Subscriber calling party number type and globalize it to +49 40
                              		  69XXXXXXX, which includes the German country code and city code.

For calls that are
                              		  routed to multiple geographic locations, the different translation settings
                              		  that are applied for each routing path can globalize the calling party number
                              		  uniquely for each call path. Cisco Unified Communications Manager can also be
                              		  configured such that the phone displays a localized calling party number on the
                              		  phone screen and the globalized number in the call log directories on the
                              		  phone. To ensure that the phone user does not need to edit the call log
                              		  directory entry on the phone before placing a call, map the global calling
                              		  party number to its local variant.

### Localization
                              		  of the Calling Party Number

For the final
                              		  presentation of the calling party number, you can configure calling party
                              		  transformation patterns for each calling party number type (National,
                              		  International, Subscriber, and Unknown), and apply strip digits and prefix
                              		  instructions specific to the calling party number type for that call. This
                              		  allows Cisco Unified Communications Manager to reformat the calling party
                              		  number such that the calling party number that displays on the called phone is
                              		  a localized number that does not include unnecessary country codes and
                              		  international access codes.

For example,
                              		  assume an incoming number arrives from the PSTN with a globalized number of +49
                              		  40 69XXXXXXX where +49 represents the country code, 40 represents the city
                              		  code, and the calling party number type is Subscriber. Cisco Unified
                              		  Communications Manager can be configured with a calling party transformation
                              		  pattern, along with instructions to strip the country code, city code, and add
                              		  a prefix of 0. After the instructions are applied, the calling party number
                              		  displays in the dialed phone as 069XXXXXXX.

### Map Globalized
                              		  Calling Party Number to a Localized Version

To ensure that the
                              		  phone user does not need to edit the call log directory entry on the phone
                              		  before placing a call, use route patterns and called party transformation
                              		  patterns to map the global calling party number to a localized version. This
                              		  ensures that when the called party returns the call, Cisco Unified
                              		  Communications Manager can route the call to the correct gateway.

Mapping the global
                              		  calling party number improves callback functionality so that the called party
                              		  can return a call without having to modify the directory number in the call log
                              		  directories on the phone.

## Calling Party Normalization Prerequisites

Make sure to activate the Cisco CallManager service in Cisco Unified Serviceability before you configure Calling Party Normalization. For more information, see the Cisco Unified Serviceability Administration Guide .

If you want Cisco Unified Communications Manager to determine the Calling Party Number Type, configure patterns that assign
                              the Calling Party Number Type value that matches the calls that you expect. You can create and apply patterns in the following configuration windows:

Route patterns

Hunt pilots

Translation patterns

Calling party number transformation patterns

Calling Party Transformation works only with the original calling party. Any modifications done for redirecting numbers affect
                                          only the diversion header. Review your configuration from the SIP trunk chapter, and add a diversion header on the SIP trunk
                                          itself.

## Calling
                        	 Party Normalization Configuration Task Flow

Calling Party Normalization prefixes and strip digits rules can be applied in a variety of ways in Unified Communications
                              Manager. For example, you can apply digit transformations to device pools, route patterns, translation patterns, hunt pilots,
                              gateways, and trunks. The manner in which you apply digit transformations depends on how you deploy your dial plan, devices,
                              and trunks. For details, review topics relating to dial plans, route patterns, translation patterns, and transformation patterns.

Step 1

If you want Unified Communications Manager to determine the calling party number type, create a pattern and configure the
                                       Calling Party Number Type that matches the calls that you expect. You can create and apply patterns in the following configuration
                                       windows:

- Route patterns

- Hunt pilots

- Translation patterns

- Calling party number transformation patterns

Step 2

Globalize Calling Party Numbers

Step 3

Set up Calling Search Spaces

Step 4

Create Calling Party Transformation Patterns

Step 5

Apply Calling Party Transformation Patterns to a Calling Search Space

### Globalize Calling
                           	 Party Numbers

For incoming calls
                                 		  that arrive via the PSTN, configure settings that will globalize calling party
                                 		  numbers. You can apply settings that will globalize calling party numbers and
                                 		  apply them to a device pool, or to individual devices. Alternatively, you can
                                 		  configure service parameters that will apply calling party normalization
                                 		  settings on a clusterwide basis.

To globalize
                                 		  calling party numbers, perform the following steps:

Step 1

If you want to
                                          			 apply calling party normalization settings to particular devices, perform the
                                          			 following steps:

Open the
                                                				  configuration window for the device on which you want to apply settings. For
                                                				  example, device pools, gateways, phones, and trunks.

In the
                                                				  Incoming Calling Party Settings section for the configuration window, apply
                                                				  prefix and strip digit instructions for each calling party number type.

Step 2

If you want to
                                          			 use service parameters to globalize calling party numbers on all devices
                                          			 clusterwide, perform the following steps:

From Cisco
                                                				  Unified CM Administration, choose System > Service
                                                      						Parameters .

From the Server drop-down list, select the server on which you want the service to run.

From the Service drop-down list, select Cisco CallManager.

Click Advanced .

Configure
                                                				  values for the following parameters, which can be applied on a clusterwide
                                                				  basis to phones, MGCP gateways, or H.323 gateways:

- Incoming Calling Party
                                             				National Number Prefix

- Incoming Calling Party
                                             				International Number Prefix

- Incoming Calling Party
                                             				Unknown Number Prefix

- Incoming Calling Party
                                             				Subscriber Number Prefix

### Set up Calling
                           	 Search Spaces

Use this procedure if you are setting up calling search spaces to handle the calling party normalization feature.

Step 1

In Cisco Unified CM
                                          			 Administration, choose Call Routing > Class of
                                                				  Control > Partitions .

Step 2

Create partitions for your network.

Step 3

In Cisco Unified CM Administration, choose Call Routing > Class of
                                                				  Control > Calling Search Space .

Step 4

Create calling search spaces for your calling party transformation
                                          			 patterns.

Step 5

For each calling search space, assign partitions to the calling
                                          			 search spaces

### Create Calling
                           	 Party Transformation Patterns

Use this procedure if you are setting up calling party transformation patterns to handle the calling party normalization feature.

Step 1

In Cisco Unified CM
                                          			 Administration, choose Call
                                                				  Routing > Transformation
                                                				  Pattern > Calling Party Transformation
                                                				  Pattern .

Step 2

Create transformation patterns.

Step 3

For each calling party transformation pattern that you create,
                                          			 assign prefixes or strip digits commands that will globalize or localize the
                                          			 calling party number.

Step 4

For each calling party transformation pattern, assign a partition
                                          			 that is associated to one of your calling search spaces.

### Apply Calling
                           	 Party Transformation Patterns to a Calling Search Space

For your devices, assign the incoming Calling Party Transformation CSS
                                 		  to your devices such as device pools, gateways, and trunks.

Step 1

In Cisco Unified CM
                                          			 Administration, choose the configuration window that applies to the device on
                                          			 which you want to apply calling party transformations.

- Gateways

- Trunks

- Device Pools

Step 2

To localize calling party numbers, in the Calling Search Space
                                          			 drop-down list box, choose the CSS that contains the calling party
                                          			 transformation pattern that you want to apply.

Step 3

To globalize calling party numbers, in the Incoming Calling Party
                                          			 Settings section, choose the calling search space that contains the calling
                                          			 party transformation pattern that you want to apply.

### Calling Party
                           	 Normalization Service Parameter Examples

The following
                                 		  service parameters can be applied on a clusterwide basis to phones, MGCP
                                 		  gateways, or H.323 gateways. In order for a particular device to use the
                                 		  clusterwide parameter, the prefix in the device configuration must be set to
                                 		  Default.:

- Incoming Calling Party
                                    			 National Number Prefix

- Incoming Calling Party
                                    			 International Number Prefix

- Incoming Calling Party
                                    			 Unknown Number Prefix

- Incoming Calling Party
                                    			 Subscriber Number Prefix

The following
                                 		  table provides examples of prefix and strip digits configurations and how these
                                 		  values can be used to transform the display of the calling party number. For
                                 		  the service parameter configurations, the numbers after the colon represent the
                                 		  number of digits to strip from the beginning of the calling party number while
                                 		  the digits after the colon represent the prefix to add to the beginning of the
                                 		  calling party number.

Original Calling Number

Service Parameter Value

Description

Final Calling Number

04423452345

+:1

Strip the first digit then add a prefix of +

+4423452345

04423452345

:2

Strip the first two digits

423452345

552345

+1:6

Strip the first 6 digits and then add a prefix of +1

+1

552345

+1:8

Final number is blank because more digits are stripped than
                                             					 are available

552345

123

Add a prefix of 123

123552345

blank

+1:2

If calling number is blank no prefix is applied

blank

0442345

:26

Calling Party Normalization allows only 24 digits to be
                                             					 stripped

Cisco Unified Communications Manager does not allow this
                                             					 configuration

## Calling Party Normalization Interactions and Restrictions

### Calling Party Normalization Interactions

The following
                                 		  table describes feature interactions with the Calling Party Normalization
                                 		  feature.

Feature

Interaction

Transferred Calls

Calling
                                             						Party Normalization may not be supported for some transferred call scenarios
                                             						because the transfer feature relies on midcall updates and calling party
                                             						normalization occurs during initial call setup for each call hop. Following is
                                             						one example of how calling party normalization can work for transfer.

Phone A
                                             						with extension 12345 and phone number of 972 500 2345 calls Phone B with
                                             						extension 54321 and phone number 972 500 4321. On Phone B, the calling party
                                             						number 12345 displays, but Phone B transfers the call through a San Jose
                                             						gateway to Phone C. During the initial transfer, Phone C displays a calling
                                             						party number of 972 500 4321, but after the transfer completes, Phone C
                                             						displays the calling party number for Phone A as 12345.

Forwarded Calls

Forwarded calls support globalization and localization of
                                             						calling party numbers. For example, a caller with Phone F calls Phone G in
                                             						Dallas through the PSTN, but Phone G has forwarded calls to Phone H in San
                                             						Jose. On the incoming Dallas gateway the calling party number displays as
                                             						555-5555/Subscriber, but the call is forwarded to a San Jose gateway. The
                                             						outgoing call from Dallas displays as 972 555 5555. On the incoming San Jose
                                             						gateway the +1 is prefixed and Phone F displays a calling number of +1 972 555
                                             						5555.

Call
                                             						Detail Records

For
                                             						details of how calling party normalization works with CDR records, see the Cisco Unified Communications Manager Call Detail Records
                                                						  Administration Guide.

Cisco
                                             						Unified Communications Manager Assistant

Cisco
                                             						Unified Communications Manager Assistant automatically supports localized and
                                             						globalized calls if you configure the Calling Party Normalization feature.
                                             						Cisco Unified Communications Manager Assistant can display localized calling
                                             						party numbers on the user interfaces. In addition, for an incoming call to the
                                             						manager, Cisco Unified Communications Manager Assistant can display localized
                                             						and globalized calling party numbers when filter pattern matching occurs. For
                                             						information on configuring Cisco Unified Communications Manager Assistant, see 
                                             						the Feature Configuration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

Cisco
                                             						Unity Connection

Cisco
                                             						Unity Connection does not support the international escape character (+).
                                             						Therefore, you must ensure that calls to Cisco Unity Connection do not contain
                                             						the +, so that voice-messaging features work as expected.

For
                                             						Cisco Unity Connection to work as expected, treat this application as a device
                                             						and configure calling party transformations that ensure that the + does not get
                                             						sent to this voice-messaging application. If the Cisco Unity Connection server
                                             						uses a North American-based dial plan, localize the calling party number to
                                             						NANP format before Cisco Unity Connection receives the calling party number.
                                             						Because no calling party transformation options exist in Cisco Unified
                                             						Communications Manager Administration for voice-messaging ports, make sure that
                                             						you configure the calling party number transformations in the device pool that
                                             						is associated with the voice-messaging ports. To localize the calling party
                                             						number, also consider adding prefixes for access codes so that the
                                             						voice-messaging application easily can redial the number for certain features,
                                             						such as Live Reply. For example, you can convert +12225551234 to 912225551234,
                                             						and you can convert international number, +4423453456, to include the
                                             						international escape code, 90114423453456.

Device
                                             						Mobility

The
                                             						Calling Party Transformation CSS of the roaming device pool overrides the
                                             						device-level configuration of the phone roaming within same Device Mobility
                                             						Group, even when the Use Device Pool Calling Party Transformation CSS check box
                                             						in the phone configuration window remains unchecked.

The
                                             						following examples demonstrate how calling party normalization works with
                                             						device mobility for a phone with a home location of Dallas which is currently
                                             						roaming in San Jose.

When the
                                             						phone is roaming in San Jose, a call comes through the PSTN from 972 500 1212
                                             						<National> in Dallas. On the incoming San Jose gateway, the calling party
                                             						number gets converted to the global format of + 1 408 500 1212. On the phone
                                             						that currently is in San Jose, the calling party number displays as 1 972 500
                                             						1212.

When the
                                             						phone is roaming in San Jose, a call comes through the PSTN from 500 1212
                                             						<Subscriber> from a seven-digit dialing area in San Jose. On the incoming
                                             						San Jose gateway, the calling party number gets converted to the global format
                                             						of + 1 408 500 1212. On the phone that currently is in San Jose, the calling
                                             						party number displays as 9 500 1212.

### Calling Party Normalization Restrictions

The following table displays restrictions that the Calling Party Normalization feature has with certain features and system
                                 components of Cisco Unified Communications Manager.

Feature

Restriction

Share lines

The calling
                                             				party number that displays for a shared line depends on the sequence of call
                                             				control events in Cisco Unified Communications
                                                				  Manager . To avoid displaying an incorrect localized calling party
                                             				number on a shared line, especially when the shared line occurs in different
                                             				geographical locations, make sure that you configure the same Calling Party
                                             				Transformation CSS for different devices that share the same line.

SIP trunks and MGCP gateways

SIP trunks and
                                             				MGCP gateways can support sending the international escape character, (+) for
                                             				calls. H.323 gateways do not support the +. QSIG trunks do not attempt to send
                                             				the +. For outgoing calls through a gateway that supports +, Cisco Unified Communications
                                                				  Manager can send the + with the dialed digits to the gateway. For
                                             				outgoing calls through a gateway that does not support +, the international
                                             				escape character + gets stripped when Cisco Unified Communications
                                                				  Manager sends the call information to the gateway.

SIP

SIP does not
                                             				support the number type, so calls through SIP trunks support only the Incoming
                                             				Number settings for calling party number types of Unknown.

QSIG

A QSIG
                                             				configuration usually supports a uniform dial plan. Transformation of numbers
                                             				and prefixes may cause feature interaction issues if you use QSIG.

Calling Party Transformation CSS

For localizing
                                             				the calling party number, the device must apply the transformation by using
                                             				digit analysis. If you configure the Calling Party Transformation CSS as None ,
                                             				the transformation does not match and does not get applied. Ensure that you
                                             				configure the Calling Party Transformation Pattern in a non-null partition that
                                             				is not used for routing.

T1-CAS and FXO ports

The Calling
                                             				Party Transformation CSS settings do not apply to T1-CAS and FXO ports on the
                                             				gateway.

Cisco Unity Connection

CiscoUnity Connection does not support the international escape
                                             			 character (+). Therefore, you must ensure that calls to CiscoUnity Connection
                                             			 do not contain the +, so that voice-messaging features work as expected.

For detailed information on Cisco Unity Connection, go to http://www.cisco.com/c/en/us/products/unified-communications/unity-connection/index.html .

| Note | Calling Party Transformation works only with the original calling party. Any modifications done for redirecting numbers affect
                                          only the diversion header. Review your configuration from the SIP trunk chapter, and add a diversion header on the SIP trunk
                                          itself. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | If you want Unified Communications Manager to determine the calling party number type, create a pattern and configure the
                                       Calling Party Number Type that matches the calls that you expect. You can create and apply patterns in the following configuration
                                       windows: Route patterns Hunt pilots Translation patterns Calling party number transformation patterns |  |
| Step 2 | Globalize Calling Party Numbers | For incoming
                                       			 calls that arrive through the PSTN, configure settings that will globalize
                                       			 calling party numbers. |
| Step 3 | Set up Calling Search Spaces | Set up your
                                       			 partitions and calling search spaces. |
| Step 4 | Create Calling Party Transformation Patterns | Create
                                       			 calling party transformation patterns that transform the calling party number
                                       			 to a globalized or localized version and assign each pattern to a partition. |
| Step 5 | Apply Calling Party Transformation Patterns to a Calling Search Space | Apply the
                                       			 incoming Calling Party Transformation CSS to your devices such as device pools,
                                       			 gateways, and trunks |

| Step 1 | If you want to
                                          			 apply calling party normalization settings to particular devices, perform the
                                          			 following steps: Open the
                                                				  configuration window for the device on which you want to apply settings. For
                                                				  example, device pools, gateways, phones, and trunks. In the
                                                				  Incoming Calling Party Settings section for the configuration window, apply
                                                				  prefix and strip digit instructions for each calling party number type. Note Cisco
                                                            					 Unified Communications Manager includes the prefix in the calling party number
                                                            					 field for all additional actions, such as supplementary services including call
                                                            					 forwarding, call park, voice messaging, and CDR data that pertain to the call. | Note | Cisco
                                                            					 Unified Communications Manager includes the prefix in the calling party number
                                                            					 field for all additional actions, such as supplementary services including call
                                                            					 forwarding, call park, voice messaging, and CDR data that pertain to the call. |
|---|---|---|---|
| Note | Cisco
                                                            					 Unified Communications Manager includes the prefix in the calling party number
                                                            					 field for all additional actions, such as supplementary services including call
                                                            					 forwarding, call park, voice messaging, and CDR data that pertain to the call. |
| Step 2 | If you want to
                                          			 use service parameters to globalize calling party numbers on all devices
                                          			 clusterwide, perform the following steps: From Cisco
                                                				  Unified CM Administration, choose System > Service
                                                      						Parameters . From the Server drop-down list, select the server on which you want the service to run. From the Service drop-down list, select Cisco CallManager. Click Advanced . Configure
                                                				  values for the following parameters, which can be applied on a clusterwide
                                                				  basis to phones, MGCP gateways, or H.323 gateways: Incoming Calling Party
                                             				National Number Prefix Incoming Calling Party
                                             				International Number Prefix Incoming Calling Party
                                             				Unknown Number Prefix Incoming Calling Party
                                             				Subscriber Number Prefix Note In order
                                                      				for Cisco Unified Communications Manager to apply the clusterwide service
                                                      				parameter settings on a particular phone, the prefix setting for that phone
                                                      				must be set to the default option at both the device and device pool levels. | Note | In order
                                                      				for Cisco Unified Communications Manager to apply the clusterwide service
                                                      				parameter settings on a particular phone, the prefix setting for that phone
                                                      				must be set to the default option at both the device and device pool levels. |
| Note | In order
                                                      				for Cisco Unified Communications Manager to apply the clusterwide service
                                                      				parameter settings on a particular phone, the prefix setting for that phone
                                                      				must be set to the default option at both the device and device pool levels. |

| Note | Cisco
                                                            					 Unified Communications Manager includes the prefix in the calling party number
                                                            					 field for all additional actions, such as supplementary services including call
                                                            					 forwarding, call park, voice messaging, and CDR data that pertain to the call. |
|---|---|

| Note | In order
                                                      				for Cisco Unified Communications Manager to apply the clusterwide service
                                                      				parameter settings on a particular phone, the prefix setting for that phone
                                                      				must be set to the default option at both the device and device pool levels. |
|---|---|

| Step 1 | In Cisco Unified CM
                                          			 Administration, choose Call Routing > Class of
                                                				  Control > Partitions . |
|---|---|
| Step 2 | Create partitions for your network. |
| Step 3 | In Cisco Unified CM Administration, choose Call Routing > Class of
                                                				  Control > Calling Search Space . |
| Step 4 | Create calling search spaces for your calling party transformation
                                          			 patterns. |
| Step 5 | For each calling search space, assign partitions to the calling
                                          			 search spaces |

| Step 1 | In Cisco Unified CM
                                          			 Administration, choose Call
                                                				  Routing > Transformation
                                                				  Pattern > Calling Party Transformation
                                                				  Pattern . |
|---|---|
| Step 2 | Create transformation patterns. |
| Step 3 | For each calling party transformation pattern that you create,
                                          			 assign prefixes or strip digits commands that will globalize or localize the
                                          			 calling party number. |
| Step 4 | For each calling party transformation pattern, assign a partition
                                          			 that is associated to one of your calling search spaces. |

| Step 1 | In Cisco Unified CM
                                          			 Administration, choose the configuration window that applies to the device on
                                          			 which you want to apply calling party transformations. Gateways Trunks Device Pools |
|---|---|
| Step 2 | To localize calling party numbers, in the Calling Search Space
                                          			 drop-down list box, choose the CSS that contains the calling party
                                          			 transformation pattern that you want to apply. Note If you configure the CSS against the Device Pool, you must also
                                                      				apply that device pool to your phones. | Note | If you configure the CSS against the Device Pool, you must also
                                                      				apply that device pool to your phones. |
| Note | If you configure the CSS against the Device Pool, you must also
                                                      				apply that device pool to your phones. |
| Step 3 | To globalize calling party numbers, in the Incoming Calling Party
                                          			 Settings section, choose the calling search space that contains the calling
                                          			 party transformation pattern that you want to apply. |

| Note | If you configure the CSS against the Device Pool, you must also
                                                      				apply that device pool to your phones. |
|---|---|

| Original Calling Number | Service Parameter Value | Description | Final Calling Number |
|---|---|---|---|
| 04423452345 | +:1 | Strip the first digit then add a prefix of + | +4423452345 |
| 04423452345 | :2 | Strip the first two digits | 423452345 |
| 552345 | +1:6 | Strip the first 6 digits and then add a prefix of +1 | +1 |
| 552345 | +1:8 | Final number is blank because more digits are stripped than
                                             					 are available |  |
| 552345 | 123 | Add a prefix of 123 | 123552345 |
| blank | +1:2 | If calling number is blank no prefix is applied | blank |
| 0442345 | :26 | Calling Party Normalization allows only 24 digits to be
                                             					 stripped | Cisco Unified Communications Manager does not allow this
                                             					 configuration |

| Feature | Interaction |
|---|---|
| Transferred Calls | Calling
                                             						Party Normalization may not be supported for some transferred call scenarios
                                             						because the transfer feature relies on midcall updates and calling party
                                             						normalization occurs during initial call setup for each call hop. Following is
                                             						one example of how calling party normalization can work for transfer. Phone A
                                             						with extension 12345 and phone number of 972 500 2345 calls Phone B with
                                             						extension 54321 and phone number 972 500 4321. On Phone B, the calling party
                                             						number 12345 displays, but Phone B transfers the call through a San Jose
                                             						gateway to Phone C. During the initial transfer, Phone C displays a calling
                                             						party number of 972 500 4321, but after the transfer completes, Phone C
                                             						displays the calling party number for Phone A as 12345. |
| Forwarded Calls | Forwarded calls support globalization and localization of
                                             						calling party numbers. For example, a caller with Phone F calls Phone G in
                                             						Dallas through the PSTN, but Phone G has forwarded calls to Phone H in San
                                             						Jose. On the incoming Dallas gateway the calling party number displays as
                                             						555-5555/Subscriber, but the call is forwarded to a San Jose gateway. The
                                             						outgoing call from Dallas displays as 972 555 5555. On the incoming San Jose
                                             						gateway the +1 is prefixed and Phone F displays a calling number of +1 972 555
                                             						5555. |
| Call
                                             						Detail Records | For
                                             						details of how calling party normalization works with CDR records, see the Cisco Unified Communications Manager Call Detail Records
                                                						  Administration Guide. |
| Cisco
                                             						Unified Communications Manager Assistant | Cisco
                                             						Unified Communications Manager Assistant automatically supports localized and
                                             						globalized calls if you configure the Calling Party Normalization feature.
                                             						Cisco Unified Communications Manager Assistant can display localized calling
                                             						party numbers on the user interfaces. In addition, for an incoming call to the
                                             						manager, Cisco Unified Communications Manager Assistant can display localized
                                             						and globalized calling party numbers when filter pattern matching occurs. For
                                             						information on configuring Cisco Unified Communications Manager Assistant, see 
                                             						the Feature Configuration Guide for Cisco Unified Communications Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html . |
| Cisco
                                             						Unity Connection | Cisco
                                             						Unity Connection does not support the international escape character (+).
                                             						Therefore, you must ensure that calls to Cisco Unity Connection do not contain
                                             						the +, so that voice-messaging features work as expected. For
                                             						Cisco Unity Connection to work as expected, treat this application as a device
                                             						and configure calling party transformations that ensure that the + does not get
                                             						sent to this voice-messaging application. If the Cisco Unity Connection server
                                             						uses a North American-based dial plan, localize the calling party number to
                                             						NANP format before Cisco Unity Connection receives the calling party number.
                                             						Because no calling party transformation options exist in Cisco Unified
                                             						Communications Manager Administration for voice-messaging ports, make sure that
                                             						you configure the calling party number transformations in the device pool that
                                             						is associated with the voice-messaging ports. To localize the calling party
                                             						number, also consider adding prefixes for access codes so that the
                                             						voice-messaging application easily can redial the number for certain features,
                                             						such as Live Reply. For example, you can convert +12225551234 to 912225551234,
                                             						and you can convert international number, +4423453456, to include the
                                             						international escape code, 90114423453456. |
| Device
                                             						Mobility | The
                                             						Calling Party Transformation CSS of the roaming device pool overrides the
                                             						device-level configuration of the phone roaming within same Device Mobility
                                             						Group, even when the Use Device Pool Calling Party Transformation CSS check box
                                             						in the phone configuration window remains unchecked. The
                                             						following examples demonstrate how calling party normalization works with
                                             						device mobility for a phone with a home location of Dallas which is currently
                                             						roaming in San Jose. When the
                                             						phone is roaming in San Jose, a call comes through the PSTN from 972 500 1212
                                             						<National> in Dallas. On the incoming San Jose gateway, the calling party
                                             						number gets converted to the global format of + 1 408 500 1212. On the phone
                                             						that currently is in San Jose, the calling party number displays as 1 972 500
                                             						1212. When the
                                             						phone is roaming in San Jose, a call comes through the PSTN from 500 1212
                                             						<Subscriber> from a seven-digit dialing area in San Jose. On the incoming
                                             						San Jose gateway, the calling party number gets converted to the global format
                                             						of + 1 408 500 1212. On the phone that currently is in San Jose, the calling
                                             						party number displays as 9 500 1212. |

| Feature | Restriction |
|---|---|
| Share lines | The calling
                                             				party number that displays for a shared line depends on the sequence of call
                                             				control events in Cisco Unified Communications
                                                				  Manager . To avoid displaying an incorrect localized calling party
                                             				number on a shared line, especially when the shared line occurs in different
                                             				geographical locations, make sure that you configure the same Calling Party
                                             				Transformation CSS for different devices that share the same line. |
| SIP trunks and MGCP gateways | SIP trunks and
                                             				MGCP gateways can support sending the international escape character, (+) for
                                             				calls. H.323 gateways do not support the +. QSIG trunks do not attempt to send
                                             				the +. For outgoing calls through a gateway that supports +, Cisco Unified Communications
                                                				  Manager can send the + with the dialed digits to the gateway. For
                                             				outgoing calls through a gateway that does not support +, the international
                                             				escape character + gets stripped when Cisco Unified Communications
                                                				  Manager sends the call information to the gateway. |
| SIP | SIP does not
                                             				support the number type, so calls through SIP trunks support only the Incoming
                                             				Number settings for calling party number types of Unknown. |
| QSIG | A QSIG
                                             				configuration usually supports a uniform dial plan. Transformation of numbers
                                             				and prefixes may cause feature interaction issues if you use QSIG. |
| Calling Party Transformation CSS | For localizing
                                             				the calling party number, the device must apply the transformation by using
                                             				digit analysis. If you configure the Calling Party Transformation CSS as None ,
                                             				the transformation does not match and does not get applied. Ensure that you
                                             				configure the Calling Party Transformation Pattern in a non-null partition that
                                             				is not used for routing. |
| T1-CAS and FXO ports | The Calling
                                             				Party Transformation CSS settings do not apply to T1-CAS and FXO ports on the
                                             				gateway. |
| Cisco Unity Connection | CiscoUnity Connection does not support the international escape
                                             			 character (+). Therefore, you must ensure that calls to CiscoUnity Connection
                                             			 do not contain the +, so that voice-messaging features work as expected. For detailed information on Cisco Unity Connection, go to http://www.cisco.com/c/en/us/products/unified-communications/unity-connection/index.html . |