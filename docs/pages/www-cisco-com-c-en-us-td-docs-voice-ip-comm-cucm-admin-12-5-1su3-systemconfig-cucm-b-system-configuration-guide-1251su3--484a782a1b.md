---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-systemconfig-cucm-b-system-configuration-guide-1251su3--484a782a1b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/systemConfig/cucm_b_system-configuration-guide-1251su3/cucm_m_configure-call-routing.html
retrieved_at: 2026-08-16T17:41:57.244956+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Configure Call Routing

## Chapter: Configure Call Routing

# Configure Call Routing

## Call Routing Overview

The system uses route plans to determine how to route calls between clusters, and how to route external calls to a private
                              network or to the Public Switched Telephone Network (PSTN). The route plan that you configure specifies the path that the
                              system uses to route each type of call. For example, you can create a route plan that uses the IP network for On-Net calls,
                              or that uses one carrier for local PSTN calls and another for international calls.

### Translation Patterns

You can configure translation patterns to manipulate digits for any type of call. Translation patterns follow the same general
                              rules and use the same wildcards as route patterns. As with route patterns, you assign a translation pattern to a partition.
                              However, when the dialed digits match the translation pattern, Unified CM does not route the call to an outside entity such
                              as a gateway; instead, it performs the translation first and then routes the call again, this time using the calling search
                              space that is configured within the translation pattern.

For each translation pattern that you create, ensure that the combination of partition, route filter, and numbering plan is
                                          unique. If you receive an error that indicates duplicate entries, check the route pattern or hunt pilot, translation pattern,
                                          directory number, call park number, call pickup number, or meet-me number configuration windows.

### Transformation Patterns

Transformation patterns can be used to discard digits, add prefix digits, add a calling party transformation mask, and control
                              the presentation of the calling party number before the system sends the call to the phone or to the PSTN.

Configure transformation patterns and associate them to a route partition, thereby assigning the pattern to the calling search
                              space that contains the partition. You can assign the pattern to the call settings for a specific device, device pool, gateway,
                              or trunk via the Calling Party Transformation CSS or Called Party Transformation CSS fields in the configuration windows.

You can configure the following transformation patterns:

Calling Party Transformation Patterns — Allow the system to adapt the global form of the calling party's number into the local form required by off-cluster networks
                                    connected to the route group devices, such as gateways or trunks.

Called Party Transformation Patterns — Allow the system to adapt the global form of the called party's number into the local form required by off-cluster networks
                                    connected to the route group devices.

### Route Patterns

The system has a three-tiered approach to route planning that uses the following components:

Route Patterns — The system searches for a configured route pattern that matches the external dial string and uses it to direct the call
                                    to a gateway or route list. You can assign route patterns to gateways, trunks, or to a route list that includes one or more
                                    route groups.

Route Lists — A prioritized list of the available paths for the call.

Route Groups — The available paths; the route group distributes the call to gateways and trunks.

### Additional Call Routing

The route plan can also include the following optional components:

Local Route Groups — If you have multiple sites, you can use local route groups so that Off-Net calls can be routed to a gateway as specified
                                    by the device pool rather than by the route pattern configuration. This allows you to use a single set of route patterns for
                                    multiple locations.

Route Filters — Create route filters and add them to your route patterns or hunt pilots to restrict users from using the pattern. Route
                                    filters are mandatory is you are using a dial plan installer file, but are optional for manual dial plan configurations. For
                                    manual configurations, route filters apply only if your pattern uses the @ wildcard.

Automated Alternate Routing — Automatically reroute calls through the PSTN or another network when the system blocks a call due to insufficient bandwidth.

Time-of-day Routing — Create a time schedule that specifies when a given partition is available to receive incoming calls.

## Call Routing Prerequisites

Complete the tasks in the Partition Configuration Task Flow .

Ensure that you have the following information:

Internal number extensions

A plan listing the calls that route to each gateway

For detailed information on planning your call routing, refer to the Call Control and Routing topics in the Cisco Collaboration System Solution Reference Network Design .

## Call Routing Configuration Task Flow

Step 1

Configure Translation Patterns

Configure translation patterns to specify how to complete digit translations for calls in a particular partition.

Step 2

Configure Calling Party Transformation Patterns

Use this procedure to transform the calling number. For example, you can configure a transformation pattern that replaces
                                          a caller's extension with the office's main number when calling the PSTN.

Step 3

Configure Called Party Transformation Patterns

Use this procedure to transform the called number. For example, you can configure a transformation pattern that retains only
                                          the last five digits of a ten-digit calling number.

Step 4

Configure Local Route Groups

Optional . Local route groups let you use a single set of route patterns for multiple locations. Unified CM assigns the gateway based
                                          on the calling device location rather than the route pattern.

Step 5

Configure Route Groups

Step 6

Configure Route Lists

Step 7

Configure Route Filters

Optional . Use route filters to restrict certain numbers that are otherwise allowed by a route pattern.

Step 8

Configure Route Patterns

Step 9

Enable Clusterwide Automated Alternate Routing

Optional . Enable Automated Alternate Routing (AAR) to let the system reroute calls to the PSTN or other networks when calls are blocked
                                          due to insufficient bandwidth.

Step 10

Configure AAR Group

Optional . Configure an AAR group with digit transformations to apply for Automated Alternate Routing.

Step 11

Configure Time of Day Routing

Optional . Create a time schedule that specifies when a given partition is available to receive incoming calls.

### Configure Translation Patterns

Configure translation patterns to apply digit manipulations to the calling and called numbers when the dial string matches
                                 the pattern. The system completes the digit translation and then reroutes the call.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Translation Pattern .

Step 2

Choose one of the following options:

- Click Add New to add a new translation pattern.

- Click Find , and select an exisiting translation pattern.

Step 3

In the Translation Pattern field, enter the pattern that you want the system to match to dial strings that use this pattern.

Step 4

From the Partition drop-down list, select the partition where you want to assign this pattern.

Step 5

Complete the remaining fields in the Translation Pattern Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 6

Click Save .

### Configure Calling Party Transformation Patterns

Use this procedure to transform the calling number. For example, you can configure a transformation pattern that replaces
                                 a caller's extension
                                 with the office's main number when calling the PSTN.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Transformation > Transformation Pattern > Calling Party Transformation Pattern .

Step 2

Choose one of the following options:

- Click Add New to add a new calling party transformation pattern.

- Click Find and select an existing pattern.

Step 3

From the Pattern field, enter the pattern that you want to match to the calling party number.

For Outboud Calls:

The calling party transformation mask is selected based on the pre transform calling party number. (extension assigned to
                                                         the IP Phone).

While selecting the calling party transformation mask on the SIP trunk, if the calling party number is transformed to a different
                                                         number on either the route pattern/group, the pre transform calling number is always used to select the calling party transformation
                                                         mask.

Whereas according to the Dialed Number Analyzer (DNA), the transformed number is used to select the calling party transformation
                                                         mask. However, this is the wrong behavior of DNA.

Step 4

Complete the remaining fields in the Calling Party Transformation Pattern Configuration window. For more information on the fields and their configuration options, see Online Help.

Step 5

Click Save .

### Configure Called Party Transformation Patterns

Use this procedure to transform the called number. For example, you can configure a transformation pattern that retains only
                                 the last five
                                 digits of a call dialed as a ten-digit number.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Transformation > Transformation Pattern > Called Party Transformation Pattern .

Step 2

Choose one of the following options:

- Click Add New , to add a new called party transformation pattern.

- Click Find and select an existing pattern.

Step 3

From the Pattern field, enter the pattern that you want to match to the called number.

Step 4

Complete the remaining fields in the Called Party Transformation Pattern Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 5

Click Save .

### Configure Local Route Groups

Optional . You can configure local route groups to reduce the number of route lists that you need. Route lists point to the PSTN gateway
                                 that the system uses to route the call, based on the location of the PSTN gateway. As an alternative, you can use local route
                                 groups to decouple the location of a PSTN gateway from the route patterns that are used to access the gateway. This configuration
                                 allows phones and other devices from different locations to use a single set of route patterns, while Cisco Unified Communication Manager selects the correct gateway to route the call.

For example, a local route group allows you to have a single dial plan
                                 				for a whole country rather than have separate dial plans for every city in the
                                 				country. This approach works for
                                 				centralized call-deployment scenarios only.

Step 1

Configure Local Route Group Names

Optional . The system provides a default local route group called Standard Local Route Group, but you can configure additional local
                                             route groups. Use this procedure to name the additional local route groups.

Step 2

Associate a Local Route Group with a Device Pool

To ensure that each device in the
                                             system is provisioned to know its local route group, associate the local route group with a device pool.

Step 3

Add Local Route Group to a Route List

Optional . Configure a local route group that you can add to your route list. When you create a local route group, the system routes
                                             outgoing calls to the gateways that are defined for the user at the device pool level.

#### Configure Local Route Group Names

Optional . The system provides a default local route group called Standard Local Route Group, but you can configure additional local
                                    route groups. Use this procedure to name the additional local route groups.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Local Route Group Names .

Step 2

Click Add Row .

Step 3

Enter a name and description for the new local route group.

Step 4

Click Save .

#### Associate a Local Route Group with a Device Pool

You can assign a local route group to use an existing route group, based on the device pool setting of the originating device.
                                    This configuration allows phones and other devices from different locations to use a single set of route patterns, while Unified Communications Manager selects the correct gateway to route the call.

To ensure that each device in the
                                    system is provisioned to know its local route group, associate the local route group with a device pool.

Step 1

From Cisco Unified CM Administration, choose System > Device Pool .

Step 2

Enter search criteria, click Find , and select a device pool from the resulting list.

Step 3

In the Local Route Group Settings area, select a route group from the Standard Local Route Group drop-down list.

Step 4

Click Save .

#### Add Local Route Group to a Route List

Configure a local route group that you can add to your route list. When you create a local route group, the system routes
                                    outgoing calls to the gateways that are defined for the user at the device pool level.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route List .

Step 2

Choose one of the following options:

- Click Add New button to add a new route list.

- Click Find and select a route list from the resulting list, to modify the settings for an existing route list.

Step 3

To add a local route group to the route list, click the Add Route Group button.

Step 4

From the Route Group drop-down list, select a local route group to add to the route list. You can add the standard local route group, or you can
                                             add a custom local route group that you have created.

Step 5

Click Save .

Step 6

Click Apply Config .

### Configure Route Groups

Configure a route group to prioritize the order in which the system selects gateways for outgoing calls. Use this procedure
                                 to group together gateways that have similar characteristics, so that any gateway in the group can dial the call. The system
                                 selects the gateway to use based on the order that you specify when you configure the route group.

You can assign a device to multiple route groups.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Group .

The Route Group Configuration window appears.

Step 2

Choose one of the following options:

- Click Add New , to add a new route group.

- Click Find and choose a route group from the resulting list, to modify the settings for an existing route group.

Step 3

Configure the fields in the Route Group Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 4

Click Save .

### Configure Route
                           	 Lists

Configure a route list to identify a set of route groups and place them in priority order. Unified Communications Manager
                                 uses the order in the route list to search for available devices for outgoing calls.

If you configure a route list, you must configure at least one route group. A route list can contain only route groups and
                                 local route groups.

When an outbound call is sent through a route list, the route list process locks the outbound device to prevent sending an
                                             alert message before the call is completed. After the outbound device is locked, the Hunt List stops hunting down the incoming
                                             calls.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route List .

Step 2

Choose one of
                                          			 the following options:

- Click Add New , to add a new route list.

- Click Find and select a route list from the resulting list, to modify the settings for an existing route list.

Step 3

Configure the fields in the Route List Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 4

To add a route group to the route list, click the Add Route Group button.

Step 5

From the Route
                                             				Group drop-down list, choose a route group to add to the route
                                          			 list.

Step 6

Click Save .

Step 7

Click Apply
                                             				Config .

### Configure Route Filters

Route filters use dialed-digit strings to determine how a call is handled. Route filters apply only when you configure a route
                                 pattern that contains the @ wildcard. When the route pattern contains the @ wildcard, Unified Communications Manager routes
                                 calls according to the numbering plan that you specify in this procedure.

Route filters are mandatory if you are using a dial plan installer; that is, if you install a dial plan file and then configure
                                 a route pattern based on that numbering plan. Route plans are optional when configuring dial plans manually.

If you are configuring a dial plan manually, you need to configure route filters whenever you have a route pattern that contains
                                 the @ wildcard. When the route pattern contains the @ wildcard, the system routes calls according to the numbering plan that
                                 you specify with a route filter.

When configuring your call routing, ensure that you do not assign a single route filter to many route patterns. A system
                                             core could result if you were to edit a route filter that has hundreds of associated route patterns. This is due to the extra
                                             system processing that is required to update call routing for all of the route patterns that use the route filter. Create
                                             duplicate route filters and associate any single route filter with no more than 250 Route Patterns.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route Filter .

Step 2

From the Numbering Plan drop-down list, choose a dial plan and click Next .

Step 3

Enter a name in the Route Filter Name field.

Step 4

Choose the route filter tags and operators and enter the data to create a clause for this route filter.

For more information about available route filter tags, see Route Filter Tags .

Step 5

Choose the route filter operators and enter data, where appropriate, to create a clause for this route filter.

For more inforation about available route filter operators, see Route Filter Operators .

Step 6

Click Save .

Step 7

Click Apply Config .

#### Route Filter Settings

Route filtering is the process where certain routes are not considered for inclusion in the local route database. It is applied
                                 only when a route pattern is configured.

The following topics list the information on route filter preferences.

Route Filter Tags

Route Filter Operators

Route Filter Examples

##### Route Filter Tags

The tag serves as the core component of a route filter. A
                                       		  tag applies a name to a subset of the dialed-digit string. For example, the
                                       		  NANP number 972-555-1234 comprises LOCAL-AREA-CODE (972), OFFICE-CODE (555),
                                       		  and SUBSCRIBER (1234) route filter tags.

Route filter tags require operators and can require
                                       		  additional values to decide which calls are filtered.

The values for route filter tag fields can contain the
                                       		  wildcard characters X, *, #, [,], -, ^, and the numbers 0 through 9. The descriptions in the following table use the notations
                                       		  [2-9] and XXXX to represent actual digits. In this notation, [2-9] represents
                                       		  any single digit in the range 2 through 9, and X represents any single digit in
                                       		  the range 0 through 9. Therefore, the three-digit area code in
                                       		  the form [2-9]XX means that you can enter the actual digits 200 through 999,
                                       		  or all wildcards, or any mixture of actual digits and wildcards that results in
                                       		  a pattern with that range.

Route filter tags vary depending on the numbering plan that
                                       		  you choose from the Numbering Plan drop-down list box on the Route Filter
                                       		  Configuration window. The following table describes the route filter tags for
                                       		  the North American Numbering Plan.

Tag

Description

AREA-CODE

This three-digit area code in the form [2-9]XX identifies the
                                                   					 area code for long-distance calls.

COUNTRY CODE

These one-, two-, or three-digit codes specify the destination
                                                   					 country for international calls.

END-OF-DIALING

This single character identifies the end of the dialed-digit
                                                   					 string. The # character serves as the end-of-dialing signal for international
                                                   					 numbers that are dialed within the NANP.

INTERNATIONAL-ACCESS

This two-digit access code specifies international dialing.
                                                   					 Calls that originate in the U.S. use 01 for this code.

INTERNATIONAL-DIRECT-DIAL

This one-digit code identifies a direct-dialed international
                                                   					 call. Calls that originate in the U.S. use 1 for this code.

INTERNATIONAL-OPERATOR

This one-digit code identifies an operator-assisted
                                                   					 international call. This code specifies 0 for calls that originate in the U.S.

LOCAL-AREA-CODE

This three-digit local area code in the form [2-9]XX
                                                   					 identifies the local area code for 10-digit local calls.

LOCAL-DIRECT-DIAL

This one-digit code identifies a direct-dialed local call.
                                                   					 NANP calls use 1 for this code.

LOCAL-OPERATOR

This one-digit code identifies an operator-assisted local
                                                   					 call. NANP calls use 0 for this code.

LONG-DISTANCE-DIRECT-DIAL

This one-digit code identifies a direct-dialed, long-distance
                                                   					 call. NANP calls use 1 for this code.

LONG-DISTANCE-OPERATOR

These one- or two-digit codes identify an operator-assisted,
                                                   					 long-distance call within the NANP. Operator-assisted calls use 0 for this
                                                   					 code, and operator access uses 00.

NATIONAL-NUMBER

This tag specifies the nation-specific part of the digit
                                                   					 string for an international call.

OFFICE-CODE

This tag designates the first three digits of a seven-digit
                                                   					 directory number in the form [2-9]XX.

SATELLITE-SERVICE

This one-digit code provides access to satellite connections
                                                   					 for international calls.

SERVICE

This three-digit code designates services such as 911 for
                                                   					 emergency, 611 for repair, and 411 for information.

SUBSCRIBER

This tag specifies the last four digits of a seven-digit
                                                   					 directory number in the form XXXX.

TRANSIT-NETWORK

This four-digit value identifies a long-distance carrier.

Do not include the leading 101 carrier access code prefix in
                                                   					 the TRANSIT-NETWORK value. See TRANSIT-NETWORK-ESCAPE for more information.

TRANSIT-NETWORK-ESCAPE

This three-digit value precedes the long-distance carrier
                                                   					 identifier. The value for this field specifies 101. Do not include the
                                                   					 four-digit carrier identification code in the TRANSIT-NETWORK-ESCAPE value. See
                                                   					 TRANSIT-NETWORK for more information.

##### Route Filter Operators

Route filter tag operators determine whether a call is
                                       		  filtered based on the
                                       		  dialed-digit string that is associated with that tag. The operators EXISTS and
                                       		  DOES-NOT-EXIST simply check for the existence of that part of the dialed-digit
                                       		  string. The operator == matches the actual dialed digits with the specified
                                       		  value or pattern. The following table describes the operators that you can use
                                       		  with route filter tags.

Operator

Description

NOT-SELECTED

Specifies do not filter calls based on the dialed-digit string
                                                   					 that is associated with this tag.

The presence or absence of the tag with which the operator
                                                               						is associated does not prevent Cisco Unified Communications Manager from routing the
                                                               						call.

EXISTS

Specifies filter calls when the dialed-digit string that is
                                                   					 associated with this tag is found.

Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string contains a sequence of digits that are
                                                               						associated with the tag.

DOES-NOT-EXIST

Specifies filter calls when the dialed-digit string that is
                                                   					 associated with this tag is not found.

Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string does not contain a sequence of digits
                                                               						that are associated with the tag.

==

Specifies filter calls when the dialed-digit string that is
                                                   					 associated with this tag matches the specified value.

Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string contains a sequence of digits that are
                                                               						associated with the tag and within the numbering range that is specified in the
                                                               						attached field.

##### Route Filter Examples

Example 1: A route filter that uses AREA-CODE and the operator DOES-NOT-EXIST selects all dialed-digit strings that do not
                                       include an area code.

Example 2: A route filter that uses AREA-CODE, the operator ==, and the entry 515 selects all dialed-digit strings that include
                                       the 515 area code.

Example 3: A route filter that uses AREA-CODE, the operator ==, and the entry 5[2-9]X selects all dialed-digit strings that
                                       include area codes in the range of 520 through 599.

Example 4: A route filter that uses TRANSIT-NETWORK, the operator ==, and the entry 0288 selects all dialed-digit strings
                                       with the carrier access code 1010288.

### Configure Route Patterns

Unified Communications Manager uses route patterns to route or block internal and external calls. You can assign route patterns
                                 to gateways, to trunks, or to a route list that contains one or more route groups.

Although the route pattern can point directly to a
                                             gateway, we recommend that you configure route lists and route groups. This approach provides the greatest flexibility in
                                             call routing and scalability.

If a route pattern is assigned directly to a gateway or trunk, then the gateway or trunk is not available for association
                                             to a route group. Similarly, a gateway or trunk that is already a member of a Route List is not available for association
                                             to a route pattern.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Pattern .

Step 2

Perform one of the following:

- Click Add New to create a new route pattern.

- Click Find and select an existing route pattern.

Step 3

In the Route Pattern field, enter the number pattern that the dial string must match.

Step 4

From the Gateway/Route drop-down list, select the destination where you want to send calls that match this route pattern.

Step 5

Complete the remaining fields in the Route Pattern Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 6

Click Save .

#### Route Patterns Settings

You can create different route patterns that comprises a string of digits (an address) and a set of associated digit(s) to
                                 enable Unified CM to manipulate that route calls to a route list or a gateway.

The following are the examples of the type of route pattern that you want to configure:

##### Wildcards and Special Characters in Route Patterns

Wildcards and special characters in route patterns allow a single route pattern to match a range of numbers (addresses). Use
                                       these wildcards and special characters also to build instructions that enable the Unified Communications Manager to manipulate
                                       a number before sending it to an adjacent system.

The following table describes the wildcards and special characters that Unified Communications Manager supports.

Character

Description

Examples

@

The at symbol (@) wildcard matches all National Numbering Plan numbers.

Each route pattern can have only one @ wildcard.

The route pattern 9.@ routes or blocks all numbers that the National Numbering Plan recognizes.

The following route patterns examples show National Numbering Plan numbers that
                                                   					 the @ wildcard encompasses:

0

1411

19725551234

101028819725551234

01133123456789

X

The X wildcard matches any single digit in the range 0 through
                                                   					 9.

The route pattern 9XXX routes or blocks all numbers in the
                                                   					 range 9000 through 9999.

!

The exclamation point (!) wildcard matches one or more digits
                                                   					 in the range 0 through 9.

The route pattern 91! routes or blocks all numbers in the
                                                   					 range 910 through 91999999999999999999999.

?

The question mark (?) wildcard matches zero or more
                                                   					 occurrences of the preceding digit or wildcard value.

If the question mark (??) wildcard is used, the second question mark does not match the empty input. Example router pattern:
                                                               *33X?*X?*X?#

The route pattern 91X? routes or blocks all numbers in the
                                                   					 range 91 through 91999999999999999999999.

+

The plus sign (+) wildcard matches one or more occurrences of
                                                   					 the preceding digit or wildcard value.

The route pattern 91X+ routes or blocks all numbers in the
                                                   					 range 910 through 91999999999999999999999.

[ ]

The square bracket ([ ]) characters enclose a range of values.

The route pattern 813510[012345] routes or blocks all numbers
                                                   					 in the range 8135100 through 8135105.

-

The hyphen (-) character, used with the square brackets,
                                                   					 denotes a range of values.

The route pattern 813510[0-5] routes or blocks all numbers in
                                                   					 the range 8135100 through 8135105.

^

The circumflex (^) character, used with the square brackets,
                                                   					 negates a range of values. Ensure that it is the first character following the
                                                   					 opening bracket ([).

Each route pattern can have only one ^ character.

The route pattern 813510[^0-5] routes or blocks all numbers in
                                                   					 the range 8135106 through 8135109.

.

The dot (.) character, used as a delimiter, separates the Cisco Unified Communications Manager access code from the directory
                                                   number.

Use this special character, with the discard digits instructions, to strip off the Cisco Unified Communications Manager access
                                                   code before sending the number to an adjacent system.

Each route pattern can have only one dot (.) character.

The route pattern 9.@ identifies the initial 9 as the Cisco Unified Communications Manager access code in a National Numbering
                                                   Plan call.

*

The asterisk (*) character can provide an extra digit for
                                                   					 special dialed numbers.

You can configure the route pattern *411 to provide access to
                                                   					 the internal operator for directory assistance.

#

The octothorpe (#) character generally identifies the end of
                                                   					 the dialing sequence.

Ensure the # character is the last character in the pattern.

The route pattern 901181910555# routes or blocks an
                                                   					 international number that is dialed from within the National Numbering Plan. The # character after
                                                   					 the last 5 identifies this digit as the last digit in the sequence.

\+

A plus sign preceded by a backslash, that is, \+, indicates
                                                   					 that you want to configure the international escape character +.

Using \+ means that the international escape character + is
                                                   					 used as a dialable digit, not as a wildcard.

##### Example of Pre-dot Digit Removal

One example of using pre-dot digit removal in a route pattern is when you want the phone users to dial an access code to reach
                                       an outside line. In North America, users typically dial 9 to access an outside line. You can specify using the following route
                                       patterns:

Local calls: 9.@ or 9.[2-9]XXXXXX

National calls: 9.1[2-9]XX

International calls: 9.011!#

In these patterns, 9 is the access code for an external line, and the dot (.) is a separator that helps format the route
                                       pattern by indicating which digits are internal to the network, and which ones are outside digits. When the system sends the
                                       dialed digits to the PSTN, you can use the Discard Digits option to strip the pre-dot digit from the dialed string so that
                                       the PSTN can route the call.

##### Example of Digit Prefixing

One example of using digit prefixing in a route pattern is when you configure On-Net dialing between sites. You can create
                                       a route pattern so that users within your organization dial 8 + XXX-XXXX to call between sites. For Off-Net calls, you can
                                       remove the prefix digit (8) and add a new prefix of 1<area code> so that you can route the call to the PSTN in E.164 format.

##### Example of On-Net and Off-Net Patterns

You can configure a route pattern as OnNet or OffNet using the Call Classification field. You can classify calls as Off-Net in cases where you want your users to get a secondary dial tone to let them know
                                       that their call is going outside your organization. For example, if you create a route pattern that requires users to dial
                                       9 to access an outside line, and you classify it as an Off-Net pattern, the system provides the following dial tones:

A dial tone when the phone is off-hook, before the you dial 9.

A secondary dial tone, after the you dial 9 to indicate that the system is ready to call the Public Switched Telephone Network
                                             (PSTN) number.

Ensure that you deselect the Allow Device Override check box when you use this option.

##### Example of Block and Route Patterns

Use block and route patterns to prevent outgoing or incoming calls that you do not want to route. Use block patterns to:

Block specific patterns. For example, blocking the pattern 91900XXXXXXX prevents users from placing calls to 900 services.

Prevent toll fraud by blocking calls to specific area codes and locations.

### Enable Clusterwide Automated Alternate Routing

Enable Automated Alternate Routing (AAR) for the cluster.

Step 1

From Cisco Unified CM Administration, choose System > Service Parameters .

Step 2

Select a node in the Server drop-down box.

Step 3

From the Service drop-down list, select Cisco Call Manager.

Step 4

In the Clusterwide Parameters (System - CCM Automated Alternate Routing) area, set the Automated Alternate Routing Enable parameter to True .

### Configure AAR Group

Configure Automated Alternate Routing (AAR) to automatically reroute calls through the PSTN or other networks when the system
                                 blocks a call due to insufficient location bandwidth. With AAR, the caller does not need to hang up and redial the called
                                 party.

Step 1

From Cisco Unified CM Administration, choose Call Routing > AAR Group .

Step 2

Choose one of the following options:

- Click Add New , to add a new AAR group.

- Click Find and choose an AAR group from the resulting list, to modify the settings for an existing AAR group.

Step 3

In the Name field, enter the name that you want to assign to the new AAR group.

The name can contain up to 20 alphanumeric characters and can contain any combination of spaces, periods (.), hyphens (-),
                                             and underscore characters (_).

Step 4

Configure the fields on the AAR Group Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 5

Click Save .

Optional . To enable AAR to work with hunt pilots, see Hunt Pilot Configuration Task Flow .

### Configure Time of
                           	 Day Routing

Optional. Create a
                                 		  time schedule that specifies when a partition is available to receive incoming
                                 		  calls.

Time of Day routing is not implemented for Message Waiting
                                             			 Indication (MWI) intercept.

Step 1

Configure a Time Period

Use this
                                             				procedure to define time periods. You can define a start time and an end time,
                                             				and also specify repetition interval either as days of the week or a specified
                                             				date on the yearly calendar.

Step 2

Configure a Time Schedule

Use this
                                             				procedure to create a schedule. The time periods that you configured in the
                                             				previous procedure are building blocks for this schedule. You can assign time
                                             				periods to multiple schedules.

Step 3

Associate a Time Schedule with a Partition

Associate time
                                             				schedules with partitions to determine where calling devices search when they
                                             				are attempting to complete a call during a particular time of day.

#### Configure a Time
                              	 Period

Use this procedure to define time periods. You can define a start time and an end time, and  
                                    			 also specify repetition interval either as days of the week or a specified date on the yearly calendar.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Time Period .

Step 2

Configure the fields in the Time Period Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 3

Click Save .

#### Configure a Time
                              	 Schedule

Use this procedure to create a schedule. The time periods that you configured in the previous procedure are building blocks
                                    for this schedule. You can assign time periods to multiple schedules.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Time Schedule .

Step 2

Configure the fields in the Time Schedule Configuration window. For more information on the fields and their configuration options, see the system Online Help.

Step 3

Click Save .

#### Associate a Time
                              	 Schedule with a Partition

Associate time
                                    				schedules with partitions to determine where calling devices search when they
                                    				are attempting to complete a call during a particular time of day.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition .

Step 2

From the Time Schedule drop-down list, choose a time schedule to
                                             			 associate with this partition.

Step 3

Click Save .

## Call Routing Restrictions

Feature

Restriction

Route Filter Associations

When configuring your call routing, be careful not to assign a single route filter to too many route patterns. A system core
                                          crash could result if you were to edit a route filter that has hundreds of associated route patterns. This is due to the extra
                                          system processing that is required to update call routing for all of the route patterns that use the route filter. Create
                                          duplicate route filters to ensure that this does not happen.

External Call Control

External call control lets an adjunct route server make call routing decisions for Unified Communications Manager by using
                                          the Cisco Unified Routing Rules Interface. When you configure external call control, Unified Communications Manager issues
                                          a route request that contains the calling party and called party information to the adjunct route server. That server receives
                                          the request, applies appropriate business logic, and returns a route response that instructs your system on how to route the
                                          call along with any additional call treatment to apply.

For details, see the Configure External Call Control chapter of the Feature Configuration Guide for Cisco Unified Communications Manager .

Route Plan Report

You can view a detailed route plan within the Route Plan Report window of Cisco Unified CM Administration (Call Routing >
                                          Route Plan Report). The route plan report allows you to view either a partial or full list of your route plan and to go directly
                                          to the associated configuration windows by clicking the entry in the Pattern/Directory Number, Partition, or Route Detail
                                          columns of the report.

In addition, the route plan report allows you to save report data into a .csv file that you can import into other applications.
                                          The .csv file contains more detailed information than the web pages, including directory numbers for phones, route patterns,
                                          pattern usage, device name, and device description.

## Troubleshooting with Dialed Number Analyzer

Dialed Number Analyzer installs as a feature service along with Cisco Unified Communications Manager. The tool allows you
                              to test a Cisco Unified Communications Manager dial plan configuration before deploying it. You can also use the tool to analyze
                              dial plans after the dial plan is deployed.

Because a dial plan can be complex, involving multiple devices, translation patterns, route patterns, route lists, route groups,
                              calling and called party transformations, and device level transformations, a dial plan may contain errors. You can use Dialed
                              Number Analyzer to test a dial plan by providing dialed digits as input. The tool analyzes the dialed digits and shows details
                              of the calls. You can use these results to diagnose the dial plan, identify problems if any, and tune the dial plan before
                              you deploy it.

For details on how to set up and use the Dialed Number Analyzer, refer to the document Dialed Number Analyzer for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

## Line Group Setup

This chapter provides information to add or delete a line group or to add directory numbers to or to remove directory numbers
                           from a line group.

For additional information, see topics related to understanding route plans in the Cisco Unified Communications Manager System Guide .

### About Line Group Setup

In Cisco Unified Communications Manager Administration , use the Call Routing > Route/Hunt > Line Group menu path to configure line groups.

A line group allows you to designate the order in which directory numbers are chosen. Cisco Unified Communications Manager distributes a call to idle or available members of a line group based on a call distribution algorithm and on the Ring No
                                 Answer Reversion (RNAR) Timeout setting.

Users cannot pick up calls to a DN that belongs to a line group by using the Directed Call Pickup feature.

Tip

Although you can configure an empty line group with no members (directory numbers), Cisco Unified Communications Manager does not support this configuration for routing calls. If the line group contains no members, the hunt list stops hunting
                                             when the call gets routed to the empty line group. To avoid this situation, make sure that you configure at least one member
                                             in the line group.

#### Line Group Configuration Tips

You must define one or more directory numbers before configuring a line group.

After you configure or update a line group, you can add or remove members from that line group.

### Line Group Deletion

You can delete a line group that one or more route/hunt lists
                                 		  references. If you try to delete a line group that is in use, Cisco Unified
                                 		  Communications Manager displays an error message.

Tip

Dependency
                                             			 Records is not supported for line groups. As a best practice, always check the
                                             			 configuration before you delete a line group.

### Line Group Settings

Field

Description

Line Group Information

Line Group Name

Enter a name for this line group. The name can comprise up to
                                             					 50 alphanumeric characters and can contain any combination of spaces, periods
                                             					 (.), hyphens (-), and underscore characters (_). Ensure that each line group
                                             					 name is unique to the route plan.

Timesaver

Use concise and descriptive names for your line groups. The
                                                         						CompanynameLocationGroup format usually provides a sufficient level of detail
                                                         						and is short enough to enable you to quickly and easily identify a line group.
                                                         						For example, CiscoDallasAA1 identifies a Cisco Access Analog line group for the
                                                         						Cisco office in Dallas.

RNA Reversion Timeout

Enter a time, in seconds, after which Unified Communications Manager will
                                             					 distribute a call to the next available or idle member of this line group or to
                                             					 the next line group if the call is not answered and if the first hunt option,
                                             					 Try next member; then, try next group in Hunt List, is chosen. The RNA
                                             					 Reversion Timeout applies at the line-group level to all members.

Distribution Algorithm

Choose a distribution algorithm, which applies at the
                                             					 line-group level, from the options in the drop-down list box:

Top Down—If you choose this distribution algorithm, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member.

Circular—If you choose this distribution algorithm, Unified Communications Manager distributes a call to idle or available members starting from the (n+1)th member of a route group, where the nth member is
                                                   the next sequential member in the list who is either idle or busy but not "down." If the nth member is the last member of a route group, Unified Communications Manager distributes a call starting from the top of the route group.

Longest Idle Time—If you choose this distribution algorithm, Unified Communications Manager only distributes a call to idle members, starting from the longest idle member to the least idle member of a line group.

Broadcast—If you choose this distribution algorithm, Unified Communications Manager distributes a call to all idle or available members of a line group simultaneously. See the Note in the description of the
                                                   Selected DN/Route Partition field for additional limitations in using the Broadcast distribution algorithm.

The default value specifies Longest Idle Time.

Hunt Options

No Answer

For a given distribution algorithm, choose a hunt option for Unified Communications Manager to use if a call is distributed to a member of a line group
                                             					 that does not answer. This option gets applied at the member level. Choose from
                                             					 the options in the drop-down list box:

Try next member; then, try next group in Hunt List—If you choose this hunt option, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. If unsuccessful, Unified Communications Manager then tries the next line group in a hunt list.

Try next member, but do not go to next group—If you choose this hunt option, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. Unified Communications Manager stops trying upon reaching the last member of the current line group.

Skip remaining members, and go directly to next group—If you choose this hunt option, Unified Communications Manager skips the remaining members of this line group when the RNA reversion timeout value elapses for the first member. Unified Communications Manager then proceeds directly to the next line group in a hunt list.

Stop hunting—If you choose this hunt option, Unified Communications Manager stops hunting after trying to distribute a call to the first member of this line group and the member does not answer the
                                                   call.

Automatically Logout Hunt Member on No Answer

If this check box is checked, line members will be logged off the hunt list automatically. Line members can log back in using
                                             the "HLOG" softkey or PLK.

Busy

For a given distribution algorithm, choose a hunt option for Unified Communications Manager to use if a call is distributed to a member of a line group
                                             					 that is busy. Choose from the options in the drop-down list box:

Try next member; then, try next group in Hunt List—If you choose this hunt option, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. If unsuccessful, Unified Communications Manager then tries the next line group in a hunt list.

Try next member, but do not go to next group—If you choose this hunt option, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. Unified Communications Manager stops trying upon reaching the last member of the current line group.

Skip remaining members, and go directly to next group—If you choose this hunt option, Unified Communications Manager skips the remaining members of this line group upon encountering a busy member. Unified Communications Manager proceeds directly to the next line group in a hunt list.

Stop hunting—If you choose this hunt option, Unified Communications Manager stops hunting after trying to distribute a call to the first busy member of this line group.

Not Available

For a given distribution algorithm, choose a hunt option for Unified Communications Manager to use if a call is distributed to a member of a line group
                                             					 that is not available. The Not Available condition occurs when none of the
                                             					 phones that are associated with the DN in question is registered. Not Available
                                             					 also occurs when extension mobility is in use and the DN/user is not logged in.
                                             					 Choose from the options in the drop-down list box:

Try next member; then, try next group in Hunt List—If you choose this hunt option, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. If unsuccessful, Unified Communications Manager then tries the next line group in a hunt list.

Try next member, but do not go to next group—If you choose this hunt option, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. Unified Communications Manager stops trying upon reaching the last member of the current line group.

Skip remaining members, and go directly to next group—If you choose this hunt option, Unified Communications Manager skips the remaining members of this line group upon encountering the first unavailable member. Unified Communications Manager proceeds directly to the next line group in a hunt list.

Stop hunting—If you choose this hunt option, Unified Communications Manager stops hunting after trying to distribute a call to the first unavailable member of this line group.

Line Group Member Information

Find Directory Numbers to Add to Line Group

Partition

Choose a route partition for this line group from the
                                             					 drop-down list box. The default value specifies <None>.

If you click Find, the Available DN/Route Partition list box
                                             					 displays all DNs that belong to the chosen partition.

Directory Number Contains

Enter the character(s) that are found in the directory number
                                             					 that you are seeking and click the Find button. Directory numbers that match
                                             					 the character(s) that you entered display in the Available DN/Route Partition
                                             					 box.

Available DN/Route Partition

Choose a directory number in the Available DN/Route Partition
                                             					 list box and add it to the Selected DN/Route Partition list box by clicking Add
                                             					 to Line Group.

Current Line Group Members

Broadcast algorithm with shared line DNs

To change the priority of a directory number, choose a
                                             					 directory number in the Selected DN/Route Partition list box. Move the
                                             					 directory number up or down in the list by clicking the arrows on the right
                                             					 side of the list box.

To reverse the priority order of the directory numbers in the
                                             					 Selected DN/Route Partition list box, click Reverse Order of Selected DNs/Route
                                             					 Partitions.

When adding DNs and Route Partitions to your line group, do not put DNs that are shared lines in a line group that uses the
                                                         Broadcast distribution algorithm. Unified Communications Manager cannot display all DNs that are shared lines on devices where the DNs are configured as shared lines if the DNs are members
                                                         of a line group that uses the Broadcast distribution algorithm.

Removed DN/Route Partition

Choose a directory number in the Selected DN/Route Partition
                                             					 list box and add it to the Removed DN/Route Partition list box by clicking the
                                             					 down arrow between the two list boxes.

Directory Numbers

(list of DNs that currently belong to this line group)

Click a directory number in this list to go to the Directory
                                             					 Number Configuration window for the specified directory number.

When you are adding a new line group, this list does not
                                                         						display until you save the line group.

### Add Members to Line Group

You can add members to a new line group or to an existing line group. The following procedure describes adding a member to
                                 an existing line group.

#### Before you begin

You must define one or more directory numbers before performing this procedure.

Step 1

Choose Call Routing > Route/Hunt > Line Group .

Step 2

Locate the line group to which you want to add a member.

Step 3

If you need to locate a directory number, choose a route partition from the Partition drop-down list box, enter a search string
                                          in the Directory Number Contains field, and click Find. To find all directory numbers that belong to a partition, leave the
                                          Directory Number Contains field blank and click Find.

A list of matching directory numbers displays in the Available DN/Route Partition list box.

Step 4

In the Available DN/Route Partition list box, choose a directory number to add and click Add to Line Group to move it to the
                                          Selected DN/Route Partition list box. Repeat this step for each member that you want to add to this line group.

Step 5

In the Selected DN/Route Partition list box, choose the order in which the new directory number(s) is to be accessed in this
                                          line group. To change the order, click a directory number and use the Up and Down arrows to the right of the list box to change
                                          the order of directory numbers.

Step 6

Click Save to add the new directory numbers and to update the directory number order for this line group.

### Remove Members From Line Group

You can remove members from a new line group or from an existing line group. The following procedure describes removing a
                                 directory number from an existing line group.

Step 1

Choose Call Routing > Route/Hunt > Line Group .

Step 2

Locate the line group from which you want to remove a directory number.

Step 3

In the Selected DN/Route Partition list box, choose a directory number to be deleted and click the down arrow below the list
                                          box to move the directory number to the Removed DN/Route Partition list box. Repeat this step for each member that you want
                                          to remove from this line group.

Step 4

To remove the members, click Save.

| Note | For each translation pattern that you create, ensure that the combination of partition, route filter, and numbering plan is
                                          unique. If you receive an error that indicates duplicate entries, check the route pattern or hunt pilot, translation pattern,
                                          directory number, call park number, call pickup number, or meet-me number configuration windows. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Translation Patterns | Configure translation patterns to specify how to complete digit translations for calls in a particular partition. |
| Step 2 | Configure Calling Party Transformation Patterns | Use this procedure to transform the calling number. For example, you can configure a transformation pattern that replaces
                                          a caller's extension with the office's main number when calling the PSTN. |
| Step 3 | Configure Called Party Transformation Patterns | Use this procedure to transform the called number. For example, you can configure a transformation pattern that retains only
                                          the last five digits of a ten-digit calling number. |
| Step 4 | Configure Local Route Groups | Optional . Local route groups let you use a single set of route patterns for multiple locations. Unified CM assigns the gateway based
                                          on the calling device location rather than the route pattern. |
| Step 5 | Configure Route Groups | Optional . Configure route groups to set the selection order of the gateway devices. Route groups contain one or more devices. |
| Step 6 | Configure Route Lists | Optional . Route lists contain one or more route groups. Configure route lists to control the selection order of the route groups. |
| Step 7 | Configure Route Filters | Optional . Use route filters to restrict certain numbers that are otherwise allowed by a route pattern. |
| Step 8 | Configure Route Patterns | Configure route patterns to direct calls to specific devices and to include or exclude specific digit patterns. |
| Step 9 | Enable Clusterwide Automated Alternate Routing | Optional . Enable Automated Alternate Routing (AAR) to let the system reroute calls to the PSTN or other networks when calls are blocked
                                          due to insufficient bandwidth. |
| Step 10 | Configure AAR Group | Optional . Configure an AAR group with digit transformations to apply for Automated Alternate Routing. |
| Step 11 | Configure Time of Day Routing | Optional . Create a time schedule that specifies when a given partition is available to receive incoming calls. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Translation Pattern . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New to add a new translation pattern. Click Find , and select an exisiting translation pattern. |
| Step 3 | In the Translation Pattern field, enter the pattern that you want the system to match to dial strings that use this pattern. |
| Step 4 | From the Partition drop-down list, select the partition where you want to assign this pattern. |
| Step 5 | Complete the remaining fields in the Translation Pattern Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 6 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Transformation > Transformation Pattern > Calling Party Transformation Pattern . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New to add a new calling party transformation pattern. Click Find and select an existing pattern. |
| Step 3 | From the Pattern field, enter the pattern that you want to match to the calling party number. Note For Outboud Calls: The calling party transformation mask is selected based on the pre transform calling party number. (extension assigned to
                                                         the IP Phone). While selecting the calling party transformation mask on the SIP trunk, if the calling party number is transformed to a different
                                                         number on either the route pattern/group, the pre transform calling number is always used to select the calling party transformation
                                                         mask. Whereas according to the Dialed Number Analyzer (DNA), the transformed number is used to select the calling party transformation
                                                         mask. However, this is the wrong behavior of DNA. | Note | For Outboud Calls: The calling party transformation mask is selected based on the pre transform calling party number. (extension assigned to
                                                         the IP Phone). While selecting the calling party transformation mask on the SIP trunk, if the calling party number is transformed to a different
                                                         number on either the route pattern/group, the pre transform calling number is always used to select the calling party transformation
                                                         mask. Whereas according to the Dialed Number Analyzer (DNA), the transformed number is used to select the calling party transformation
                                                         mask. However, this is the wrong behavior of DNA. |
| Note | For Outboud Calls: The calling party transformation mask is selected based on the pre transform calling party number. (extension assigned to
                                                         the IP Phone). While selecting the calling party transformation mask on the SIP trunk, if the calling party number is transformed to a different
                                                         number on either the route pattern/group, the pre transform calling number is always used to select the calling party transformation
                                                         mask. Whereas according to the Dialed Number Analyzer (DNA), the transformed number is used to select the calling party transformation
                                                         mask. However, this is the wrong behavior of DNA. |
| Step 4 | Complete the remaining fields in the Calling Party Transformation Pattern Configuration window. For more information on the fields and their configuration options, see Online Help. |
| Step 5 | Click Save . |

| Note | For Outboud Calls: The calling party transformation mask is selected based on the pre transform calling party number. (extension assigned to
                                                         the IP Phone). While selecting the calling party transformation mask on the SIP trunk, if the calling party number is transformed to a different
                                                         number on either the route pattern/group, the pre transform calling number is always used to select the calling party transformation
                                                         mask. Whereas according to the Dialed Number Analyzer (DNA), the transformed number is used to select the calling party transformation
                                                         mask. However, this is the wrong behavior of DNA. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Transformation > Transformation Pattern > Called Party Transformation Pattern . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New , to add a new called party transformation pattern. Click Find and select an existing pattern. |
| Step 3 | From the Pattern field, enter the pattern that you want to match to the called number. |
| Step 4 | Complete the remaining fields in the Called Party Transformation Pattern Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 5 | Click Save . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Local Route Group Names | Optional . The system provides a default local route group called Standard Local Route Group, but you can configure additional local
                                             route groups. Use this procedure to name the additional local route groups. |
| Step 2 | Associate a Local Route Group with a Device Pool | To ensure that each device in the
                                             system is provisioned to know its local route group, associate the local route group with a device pool. |
| Step 3 | Add Local Route Group to a Route List | Optional . Configure a local route group that you can add to your route list. When you create a local route group, the system routes
                                             outgoing calls to the gateways that are defined for the user at the device pool level. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Local Route Group Names . |
|---|---|
| Step 2 | Click Add Row . |
| Step 3 | Enter a name and description for the new local route group. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose System > Device Pool . |
|---|---|
| Step 2 | Enter search criteria, click Find , and select a device pool from the resulting list. |
| Step 3 | In the Local Route Group Settings area, select a route group from the Standard Local Route Group drop-down list. |
| Step 4 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route List . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New button to add a new route list. Click Find and select a route list from the resulting list, to modify the settings for an existing route list. The Route List Configuration window appears. |
| Step 3 | To add a local route group to the route list, click the Add Route Group button. |
| Step 4 | From the Route Group drop-down list, select a local route group to add to the route list. You can add the standard local route group, or you can
                                             add a custom local route group that you have created. |
| Step 5 | Click Save . |
| Step 6 | Click Apply Config . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Group . The Route Group Configuration window appears. |
|---|---|
| Step 2 | Choose one of the following options: Click Add New , to add a new route group. Click Find and choose a route group from the resulting list, to modify the settings for an existing route group. The Route Group Configuration window appears. |
| Step 3 | Configure the fields in the Route Group Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 4 | Click Save . |

| Note | When an outbound call is sent through a route list, the route list process locks the outbound device to prevent sending an
                                             alert message before the call is completed. After the outbound device is locked, the Hunt List stops hunting down the incoming
                                             calls. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route List . |
|---|---|
| Step 2 | Choose one of
                                          			 the following options: Click Add New , to add a new route list. Click Find and select a route list from the resulting list, to modify the settings for an existing route list. |
| Step 3 | Configure the fields in the Route List Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 4 | To add a route group to the route list, click the Add Route Group button. |
| Step 5 | From the Route
                                             				Group drop-down list, choose a route group to add to the route
                                          			 list. |
| Step 6 | Click Save . |
| Step 7 | Click Apply
                                             				Config . |

| Note | When configuring your call routing, ensure that you do not assign a single route filter to many route patterns. A system
                                             core could result if you were to edit a route filter that has hundreds of associated route patterns. This is due to the extra
                                             system processing that is required to update call routing for all of the route patterns that use the route filter. Create
                                             duplicate route filters and associate any single route filter with no more than 250 Route Patterns. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route Filter . |
|---|---|
| Step 2 | From the Numbering Plan drop-down list, choose a dial plan and click Next . |
| Step 3 | Enter a name in the Route Filter Name field. Ensure each route filter name is unique to the route plan. |
| Step 4 | Choose the route filter tags and operators and enter the data to create a clause for this route filter. For more information about available route filter tags, see Route Filter Tags . Note Do not enter route filter tag values for tags that are using the operators EXISTS, DOES-NOT-EXIST, or NOT-SELECTED. | Note | Do not enter route filter tag values for tags that are using the operators EXISTS, DOES-NOT-EXIST, or NOT-SELECTED. |
| Note | Do not enter route filter tag values for tags that are using the operators EXISTS, DOES-NOT-EXIST, or NOT-SELECTED. |
| Step 5 | Choose the route filter operators and enter data, where appropriate, to create a clause for this route filter. For more inforation about available route filter operators, see Route Filter Operators . |
| Step 6 | Click Save . |
| Step 7 | Click Apply Config . |

| Note | Do not enter route filter tag values for tags that are using the operators EXISTS, DOES-NOT-EXIST, or NOT-SELECTED. |
|---|---|

| Tag | Description |
|---|---|
| AREA-CODE | This three-digit area code in the form [2-9]XX identifies the
                                                   					 area code for long-distance calls. |
| COUNTRY CODE | These one-, two-, or three-digit codes specify the destination
                                                   					 country for international calls. |
| END-OF-DIALING | This single character identifies the end of the dialed-digit
                                                   					 string. The # character serves as the end-of-dialing signal for international
                                                   					 numbers that are dialed within the NANP. |
| INTERNATIONAL-ACCESS | This two-digit access code specifies international dialing.
                                                   					 Calls that originate in the U.S. use 01 for this code. |
| INTERNATIONAL-DIRECT-DIAL | This one-digit code identifies a direct-dialed international
                                                   					 call. Calls that originate in the U.S. use 1 for this code. |
| INTERNATIONAL-OPERATOR | This one-digit code identifies an operator-assisted
                                                   					 international call. This code specifies 0 for calls that originate in the U.S. |
| LOCAL-AREA-CODE | This three-digit local area code in the form [2-9]XX
                                                   					 identifies the local area code for 10-digit local calls. |
| LOCAL-DIRECT-DIAL | This one-digit code identifies a direct-dialed local call.
                                                   					 NANP calls use 1 for this code. |
| LOCAL-OPERATOR | This one-digit code identifies an operator-assisted local
                                                   					 call. NANP calls use 0 for this code. |
| LONG-DISTANCE-DIRECT-DIAL | This one-digit code identifies a direct-dialed, long-distance
                                                   					 call. NANP calls use 1 for this code. |
| LONG-DISTANCE-OPERATOR | These one- or two-digit codes identify an operator-assisted,
                                                   					 long-distance call within the NANP. Operator-assisted calls use 0 for this
                                                   					 code, and operator access uses 00. |
| NATIONAL-NUMBER | This tag specifies the nation-specific part of the digit
                                                   					 string for an international call. |
| OFFICE-CODE | This tag designates the first three digits of a seven-digit
                                                   					 directory number in the form [2-9]XX. |
| SATELLITE-SERVICE | This one-digit code provides access to satellite connections
                                                   					 for international calls. |
| SERVICE | This three-digit code designates services such as 911 for
                                                   					 emergency, 611 for repair, and 411 for information. |
| SUBSCRIBER | This tag specifies the last four digits of a seven-digit
                                                   					 directory number in the form XXXX. |
| TRANSIT-NETWORK | This four-digit value identifies a long-distance carrier. Do not include the leading 101 carrier access code prefix in
                                                   					 the TRANSIT-NETWORK value. See TRANSIT-NETWORK-ESCAPE for more information. |
| TRANSIT-NETWORK-ESCAPE | This three-digit value precedes the long-distance carrier
                                                   					 identifier. The value for this field specifies 101. Do not include the
                                                   					 four-digit carrier identification code in the TRANSIT-NETWORK-ESCAPE value. See
                                                   					 TRANSIT-NETWORK for more information. |

| Operator | Description |
|---|---|
| NOT-SELECTED | Specifies do not filter calls based on the dialed-digit string
                                                   					 that is associated with this tag. Note The presence or absence of the tag with which the operator
                                                               						is associated does not prevent Cisco Unified Communications Manager from routing the
                                                               						call. | Note | The presence or absence of the tag with which the operator
                                                               						is associated does not prevent Cisco Unified Communications Manager from routing the
                                                               						call. |
| Note | The presence or absence of the tag with which the operator
                                                               						is associated does not prevent Cisco Unified Communications Manager from routing the
                                                               						call. |
| EXISTS | Specifies filter calls when the dialed-digit string that is
                                                   					 associated with this tag is found. Note Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string contains a sequence of digits that are
                                                               						associated with the tag. | Note | Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string contains a sequence of digits that are
                                                               						associated with the tag. |
| Note | Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string contains a sequence of digits that are
                                                               						associated with the tag. |
| DOES-NOT-EXIST | Specifies filter calls when the dialed-digit string that is
                                                   					 associated with this tag is not found. Note Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string does not contain a sequence of digits
                                                               						that are associated with the tag. | Note | Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string does not contain a sequence of digits
                                                               						that are associated with the tag. |
| Note | Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string does not contain a sequence of digits
                                                               						that are associated with the tag. |
| == | Specifies filter calls when the dialed-digit string that is
                                                   					 associated with this tag matches the specified value. Note Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string contains a sequence of digits that are
                                                               						associated with the tag and within the numbering range that is specified in the
                                                               						attached field. | Note | Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string contains a sequence of digits that are
                                                               						associated with the tag and within the numbering range that is specified in the
                                                               						attached field. |
| Note | Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string contains a sequence of digits that are
                                                               						associated with the tag and within the numbering range that is specified in the
                                                               						attached field. |

| Note | The presence or absence of the tag with which the operator
                                                               						is associated does not prevent Cisco Unified Communications Manager from routing the
                                                               						call. |
|---|---|

| Note | Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string contains a sequence of digits that are
                                                               						associated with the tag. |
|---|---|

| Note | Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string does not contain a sequence of digits
                                                               						that are associated with the tag. |
|---|---|

| Note | Cisco Unified Communications Manager routes or blocks
                                                               						the call only if the dialed-digit string contains a sequence of digits that are
                                                               						associated with the tag and within the numbering range that is specified in the
                                                               						attached field. |
|---|---|

| Note | Although the route pattern can point directly to a
                                             gateway, we recommend that you configure route lists and route groups. This approach provides the greatest flexibility in
                                             call routing and scalability. If a route pattern is assigned directly to a gateway or trunk, then the gateway or trunk is not available for association
                                             to a route group. Similarly, a gateway or trunk that is already a member of a Route List is not available for association
                                             to a route pattern. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Route Pattern . |
|---|---|
| Step 2 | Perform one of the following: Click Add New to create a new route pattern. Click Find and select an existing route pattern. The Route Pattern Configuration Window appears. |
| Step 3 | In the Route Pattern field, enter the number pattern that the dial string must match. |
| Step 4 | From the Gateway/Route drop-down list, select the destination where you want to send calls that match this route pattern. |
| Step 5 | Complete the remaining fields in the Route Pattern Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 6 | Click Save . |

| Character | Description | Examples |
|---|---|---|
| @ | The at symbol (@) wildcard matches all National Numbering Plan numbers. Each route pattern can have only one @ wildcard. | The route pattern 9.@ routes or blocks all numbers that the National Numbering Plan recognizes. The following route patterns examples show National Numbering Plan numbers that
                                                   					 the @ wildcard encompasses: 0 1411 19725551234 101028819725551234 01133123456789 |
| X | The X wildcard matches any single digit in the range 0 through
                                                   					 9. | The route pattern 9XXX routes or blocks all numbers in the
                                                   					 range 9000 through 9999. |
| ! | The exclamation point (!) wildcard matches one or more digits
                                                   					 in the range 0 through 9. | The route pattern 91! routes or blocks all numbers in the
                                                   					 range 910 through 91999999999999999999999. |
| ? | The question mark (?) wildcard matches zero or more
                                                   					 occurrences of the preceding digit or wildcard value. Note If the question mark (??) wildcard is used, the second question mark does not match the empty input. Example router pattern:
                                                               *33X?*X?*X?# | Note | If the question mark (??) wildcard is used, the second question mark does not match the empty input. Example router pattern:
                                                               *33X?*X?*X?# | The route pattern 91X? routes or blocks all numbers in the
                                                   					 range 91 through 91999999999999999999999. |
| Note | If the question mark (??) wildcard is used, the second question mark does not match the empty input. Example router pattern:
                                                               *33X?*X?*X?# |
| + | The plus sign (+) wildcard matches one or more occurrences of
                                                   					 the preceding digit or wildcard value. | The route pattern 91X+ routes or blocks all numbers in the
                                                   					 range 910 through 91999999999999999999999. |
| [ ] | The square bracket ([ ]) characters enclose a range of values. | The route pattern 813510[012345] routes or blocks all numbers
                                                   					 in the range 8135100 through 8135105. |
| - | The hyphen (-) character, used with the square brackets,
                                                   					 denotes a range of values. | The route pattern 813510[0-5] routes or blocks all numbers in
                                                   					 the range 8135100 through 8135105. |
| ^ | The circumflex (^) character, used with the square brackets,
                                                   					 negates a range of values. Ensure that it is the first character following the
                                                   					 opening bracket ([). Each route pattern can have only one ^ character. | The route pattern 813510[^0-5] routes or blocks all numbers in
                                                   					 the range 8135106 through 8135109. |
| . | The dot (.) character, used as a delimiter, separates the Cisco Unified Communications Manager access code from the directory
                                                   number. Use this special character, with the discard digits instructions, to strip off the Cisco Unified Communications Manager access
                                                   code before sending the number to an adjacent system. Each route pattern can have only one dot (.) character. | The route pattern 9.@ identifies the initial 9 as the Cisco Unified Communications Manager access code in a National Numbering
                                                   Plan call. |
| * | The asterisk (*) character can provide an extra digit for
                                                   					 special dialed numbers. | You can configure the route pattern *411 to provide access to
                                                   					 the internal operator for directory assistance. |
| # | The octothorpe (#) character generally identifies the end of
                                                   					 the dialing sequence. Ensure the # character is the last character in the pattern. | The route pattern 901181910555# routes or blocks an
                                                   					 international number that is dialed from within the National Numbering Plan. The # character after
                                                   					 the last 5 identifies this digit as the last digit in the sequence. |
| \+ | A plus sign preceded by a backslash, that is, \+, indicates
                                                   					 that you want to configure the international escape character +. | Using \+ means that the international escape character + is
                                                   					 used as a dialable digit, not as a wildcard. |

| Note | If the question mark (??) wildcard is used, the second question mark does not match the empty input. Example router pattern:
                                                               *33X?*X?*X?# |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | Select a node in the Server drop-down box. |
| Step 3 | From the Service drop-down list, select Cisco Call Manager. |
| Step 4 | In the Clusterwide Parameters (System - CCM Automated Alternate Routing) area, set the Automated Alternate Routing Enable parameter to True . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > AAR Group . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New , to add a new AAR group. Click Find and choose an AAR group from the resulting list, to modify the settings for an existing AAR group. The AAR Group Configuration window appears. |
| Step 3 | In the Name field, enter the name that you want to assign to the new AAR group. The name can contain up to 20 alphanumeric characters and can contain any combination of spaces, periods (.), hyphens (-),
                                             and underscore characters (_). The window refreshes and displays additional fields. |
| Step 4 | Configure the fields on the AAR Group Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 5 | Click Save . Note Optional . To enable AAR to work with hunt pilots, see Hunt Pilot Configuration Task Flow . | Note | Optional . To enable AAR to work with hunt pilots, see Hunt Pilot Configuration Task Flow . |
| Note | Optional . To enable AAR to work with hunt pilots, see Hunt Pilot Configuration Task Flow . |

| Note | Optional . To enable AAR to work with hunt pilots, see Hunt Pilot Configuration Task Flow . |
|---|---|

| Note | Time of Day routing is not implemented for Message Waiting
                                             			 Indication (MWI) intercept. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure a Time Period | Use this
                                             				procedure to define time periods. You can define a start time and an end time,
                                             				and also specify repetition interval either as days of the week or a specified
                                             				date on the yearly calendar. |
| Step 2 | Configure a Time Schedule | Use this
                                             				procedure to create a schedule. The time periods that you configured in the
                                             				previous procedure are building blocks for this schedule. You can assign time
                                             				periods to multiple schedules. |
| Step 3 | Associate a Time Schedule with a Partition | Associate time
                                             				schedules with partitions to determine where calling devices search when they
                                             				are attempting to complete a call during a particular time of day. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Time Period . |
|---|---|
| Step 2 | Configure the fields in the Time Period Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 3 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Time Schedule . |
|---|---|
| Step 2 | Configure the fields in the Time Schedule Configuration window. For more information on the fields and their configuration options, see the system Online Help. |
| Step 3 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Class of Control > Partition . |
|---|---|
| Step 2 | From the Time Schedule drop-down list, choose a time schedule to
                                             			 associate with this partition. The time schedule specifies when the partition is available
                                             			 to receive incoming calls. If you choose None , the partition remains active at all
                                             			 times. |
| Step 3 | Click Save . |

| Feature | Restriction |
|---|---|
| Route Filter Associations | When configuring your call routing, be careful not to assign a single route filter to too many route patterns. A system core
                                          crash could result if you were to edit a route filter that has hundreds of associated route patterns. This is due to the extra
                                          system processing that is required to update call routing for all of the route patterns that use the route filter. Create
                                          duplicate route filters to ensure that this does not happen. |
| External Call Control | External call control lets an adjunct route server make call routing decisions for Unified Communications Manager by using
                                          the Cisco Unified Routing Rules Interface. When you configure external call control, Unified Communications Manager issues
                                          a route request that contains the calling party and called party information to the adjunct route server. That server receives
                                          the request, applies appropriate business logic, and returns a route response that instructs your system on how to route the
                                          call along with any additional call treatment to apply. For details, see the Configure External Call Control chapter of the Feature Configuration Guide for Cisco Unified Communications Manager . |
| Route Plan Report | You can view a detailed route plan within the Route Plan Report window of Cisco Unified CM Administration (Call Routing >
                                          Route Plan Report). The route plan report allows you to view either a partial or full list of your route plan and to go directly
                                          to the associated configuration windows by clicking the entry in the Pattern/Directory Number, Partition, or Route Detail
                                          columns of the report. In addition, the route plan report allows you to save report data into a .csv file that you can import into other applications.
                                          The .csv file contains more detailed information than the web pages, including directory numbers for phones, route patterns,
                                          pattern usage, device name, and device description. |

| Note | Users cannot pick up calls to a DN that belongs to a line group by using the Directed Call Pickup feature. |
|---|---|

| Tip | Although you can configure an empty line group with no members (directory numbers), Cisco Unified Communications Manager does not support this configuration for routing calls. If the line group contains no members, the hunt list stops hunting
                                             when the call gets routed to the empty line group. To avoid this situation, make sure that you configure at least one member
                                             in the line group. |
|---|---|

| Tip | Dependency
                                             			 Records is not supported for line groups. As a best practice, always check the
                                             			 configuration before you delete a line group. |
|---|---|

| Field | Description |
|---|---|
| Line Group Information |
| Line Group Name | Enter a name for this line group. The name can comprise up to
                                             					 50 alphanumeric characters and can contain any combination of spaces, periods
                                             					 (.), hyphens (-), and underscore characters (_). Ensure that each line group
                                             					 name is unique to the route plan. Timesaver Use concise and descriptive names for your line groups. The
                                                         						CompanynameLocationGroup format usually provides a sufficient level of detail
                                                         						and is short enough to enable you to quickly and easily identify a line group.
                                                         						For example, CiscoDallasAA1 identifies a Cisco Access Analog line group for the
                                                         						Cisco office in Dallas. | Timesaver | Use concise and descriptive names for your line groups. The
                                                         						CompanynameLocationGroup format usually provides a sufficient level of detail
                                                         						and is short enough to enable you to quickly and easily identify a line group.
                                                         						For example, CiscoDallasAA1 identifies a Cisco Access Analog line group for the
                                                         						Cisco office in Dallas. |
| Timesaver | Use concise and descriptive names for your line groups. The
                                                         						CompanynameLocationGroup format usually provides a sufficient level of detail
                                                         						and is short enough to enable you to quickly and easily identify a line group.
                                                         						For example, CiscoDallasAA1 identifies a Cisco Access Analog line group for the
                                                         						Cisco office in Dallas. |
| RNA Reversion Timeout | Enter a time, in seconds, after which Unified Communications Manager will
                                             					 distribute a call to the next available or idle member of this line group or to
                                             					 the next line group if the call is not answered and if the first hunt option,
                                             					 Try next member; then, try next group in Hunt List, is chosen. The RNA
                                             					 Reversion Timeout applies at the line-group level to all members. |
| Distribution Algorithm | Choose a distribution algorithm, which applies at the
                                             					 line-group level, from the options in the drop-down list box: Top Down—If you choose this distribution algorithm, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. Circular—If you choose this distribution algorithm, Unified Communications Manager distributes a call to idle or available members starting from the (n+1)th member of a route group, where the nth member is
                                                   the next sequential member in the list who is either idle or busy but not "down." If the nth member is the last member of a route group, Unified Communications Manager distributes a call starting from the top of the route group. Longest Idle Time—If you choose this distribution algorithm, Unified Communications Manager only distributes a call to idle members, starting from the longest idle member to the least idle member of a line group. Broadcast—If you choose this distribution algorithm, Unified Communications Manager distributes a call to all idle or available members of a line group simultaneously. See the Note in the description of the
                                                   Selected DN/Route Partition field for additional limitations in using the Broadcast distribution algorithm. The default value specifies Longest Idle Time. |
| Hunt Options |
| No Answer | For a given distribution algorithm, choose a hunt option for Unified Communications Manager to use if a call is distributed to a member of a line group
                                             					 that does not answer. This option gets applied at the member level. Choose from
                                             					 the options in the drop-down list box: Try next member; then, try next group in Hunt List—If you choose this hunt option, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. If unsuccessful, Unified Communications Manager then tries the next line group in a hunt list. Try next member, but do not go to next group—If you choose this hunt option, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. Unified Communications Manager stops trying upon reaching the last member of the current line group. Skip remaining members, and go directly to next group—If you choose this hunt option, Unified Communications Manager skips the remaining members of this line group when the RNA reversion timeout value elapses for the first member. Unified Communications Manager then proceeds directly to the next line group in a hunt list. Stop hunting—If you choose this hunt option, Unified Communications Manager stops hunting after trying to distribute a call to the first member of this line group and the member does not answer the
                                                   call. |
| Automatically Logout Hunt Member on No Answer | If this check box is checked, line members will be logged off the hunt list automatically. Line members can log back in using
                                             the "HLOG" softkey or PLK. |
| Busy | For a given distribution algorithm, choose a hunt option for Unified Communications Manager to use if a call is distributed to a member of a line group
                                             					 that is busy. Choose from the options in the drop-down list box: Try next member; then, try next group in Hunt List—If you choose this hunt option, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. If unsuccessful, Unified Communications Manager then tries the next line group in a hunt list. Try next member, but do not go to next group—If you choose this hunt option, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. Unified Communications Manager stops trying upon reaching the last member of the current line group. Skip remaining members, and go directly to next group—If you choose this hunt option, Unified Communications Manager skips the remaining members of this line group upon encountering a busy member. Unified Communications Manager proceeds directly to the next line group in a hunt list. Stop hunting—If you choose this hunt option, Unified Communications Manager stops hunting after trying to distribute a call to the first busy member of this line group. |
| Not Available | For a given distribution algorithm, choose a hunt option for Unified Communications Manager to use if a call is distributed to a member of a line group
                                             					 that is not available. The Not Available condition occurs when none of the
                                             					 phones that are associated with the DN in question is registered. Not Available
                                             					 also occurs when extension mobility is in use and the DN/user is not logged in.
                                             					 Choose from the options in the drop-down list box: Try next member; then, try next group in Hunt List—If you choose this hunt option, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. If unsuccessful, Unified Communications Manager then tries the next line group in a hunt list. Try next member, but do not go to next group—If you choose this hunt option, Unified Communications Manager distributes a call to idle or available members starting from the first idle or available member of a line group to the last
                                                   idle or available member. Unified Communications Manager stops trying upon reaching the last member of the current line group. Skip remaining members, and go directly to next group—If you choose this hunt option, Unified Communications Manager skips the remaining members of this line group upon encountering the first unavailable member. Unified Communications Manager proceeds directly to the next line group in a hunt list. Stop hunting—If you choose this hunt option, Unified Communications Manager stops hunting after trying to distribute a call to the first unavailable member of this line group. |
| Line Group Member Information |
| Find Directory Numbers to Add to Line Group |
| Partition | Choose a route partition for this line group from the
                                             					 drop-down list box. The default value specifies <None>. If you click Find, the Available DN/Route Partition list box
                                             					 displays all DNs that belong to the chosen partition. |
| Directory Number Contains | Enter the character(s) that are found in the directory number
                                             					 that you are seeking and click the Find button. Directory numbers that match
                                             					 the character(s) that you entered display in the Available DN/Route Partition
                                             					 box. |
| Available DN/Route Partition | Choose a directory number in the Available DN/Route Partition
                                             					 list box and add it to the Selected DN/Route Partition list box by clicking Add
                                             					 to Line Group. |
| Current Line Group Members |
| Broadcast algorithm with shared line DNs | To change the priority of a directory number, choose a
                                             					 directory number in the Selected DN/Route Partition list box. Move the
                                             					 directory number up or down in the list by clicking the arrows on the right
                                             					 side of the list box. To reverse the priority order of the directory numbers in the
                                             					 Selected DN/Route Partition list box, click Reverse Order of Selected DNs/Route
                                             					 Partitions. Note When adding DNs and Route Partitions to your line group, do not put DNs that are shared lines in a line group that uses the
                                                         Broadcast distribution algorithm. Unified Communications Manager cannot display all DNs that are shared lines on devices where the DNs are configured as shared lines if the DNs are members
                                                         of a line group that uses the Broadcast distribution algorithm. | Note | When adding DNs and Route Partitions to your line group, do not put DNs that are shared lines in a line group that uses the
                                                         Broadcast distribution algorithm. Unified Communications Manager cannot display all DNs that are shared lines on devices where the DNs are configured as shared lines if the DNs are members
                                                         of a line group that uses the Broadcast distribution algorithm. |
| Note | When adding DNs and Route Partitions to your line group, do not put DNs that are shared lines in a line group that uses the
                                                         Broadcast distribution algorithm. Unified Communications Manager cannot display all DNs that are shared lines on devices where the DNs are configured as shared lines if the DNs are members
                                                         of a line group that uses the Broadcast distribution algorithm. |
| Removed DN/Route Partition | Choose a directory number in the Selected DN/Route Partition
                                             					 list box and add it to the Removed DN/Route Partition list box by clicking the
                                             					 down arrow between the two list boxes. |
| Directory Numbers |
| (list of DNs that currently belong to this line group) | Click a directory number in this list to go to the Directory
                                             					 Number Configuration window for the specified directory number. Note When you are adding a new line group, this list does not
                                                         						display until you save the line group. | Note | When you are adding a new line group, this list does not
                                                         						display until you save the line group. |
| Note | When you are adding a new line group, this list does not
                                                         						display until you save the line group. |

| Timesaver | Use concise and descriptive names for your line groups. The
                                                         						CompanynameLocationGroup format usually provides a sufficient level of detail
                                                         						and is short enough to enable you to quickly and easily identify a line group.
                                                         						For example, CiscoDallasAA1 identifies a Cisco Access Analog line group for the
                                                         						Cisco office in Dallas. |
|---|---|

| Note | When adding DNs and Route Partitions to your line group, do not put DNs that are shared lines in a line group that uses the
                                                         Broadcast distribution algorithm. Unified Communications Manager cannot display all DNs that are shared lines on devices where the DNs are configured as shared lines if the DNs are members
                                                         of a line group that uses the Broadcast distribution algorithm. |
|---|---|

| Note | When you are adding a new line group, this list does not
                                                         						display until you save the line group. |
|---|---|

| Step 1 | Choose Call Routing > Route/Hunt > Line Group . |
|---|---|
| Step 2 | Locate the line group to which you want to add a member. |
| Step 3 | If you need to locate a directory number, choose a route partition from the Partition drop-down list box, enter a search string
                                          in the Directory Number Contains field, and click Find. To find all directory numbers that belong to a partition, leave the
                                          Directory Number Contains field blank and click Find. A list of matching directory numbers displays in the Available DN/Route Partition list box. |
| Step 4 | In the Available DN/Route Partition list box, choose a directory number to add and click Add to Line Group to move it to the
                                          Selected DN/Route Partition list box. Repeat this step for each member that you want to add to this line group. |
| Step 5 | In the Selected DN/Route Partition list box, choose the order in which the new directory number(s) is to be accessed in this
                                          line group. To change the order, click a directory number and use the Up and Down arrows to the right of the list box to change
                                          the order of directory numbers. |
| Step 6 | Click Save to add the new directory numbers and to update the directory number order for this line group. |

| Step 1 | Choose Call Routing > Route/Hunt > Line Group . |
|---|---|
| Step 2 | Locate the line group from which you want to remove a directory number. |
| Step 3 | In the Selected DN/Route Partition list box, choose a directory number to be deleted and click the down arrow below the list
                                          box to move the directory number to the Removed DN/Route Partition list box. Repeat this step for each member that you want
                                          to remove from this line group. |
| Step 4 | To remove the members, click Save. |