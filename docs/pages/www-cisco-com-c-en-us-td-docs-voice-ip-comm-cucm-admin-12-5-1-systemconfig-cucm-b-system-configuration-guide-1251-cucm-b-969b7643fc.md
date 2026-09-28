---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1-systemconfig-cucm-b-system-configuration-guide-1251-cucm-b-969b7643fc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1/systemConfig/cucm_b_system-configuration-guide-1251/cucm_b_system-configuration-guide-1251_chapter_010101.html
retrieved_at: 2026-08-16T17:30:50.475911+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: July 31, 2025

Chapter: Configure Hunt Pilots

## Chapter: Configure Hunt Pilots

# Configure Hunt Pilots

## Hunt Pilot Overview

A hunt pilot comprises a number or pattern and a set of associated digit manipulations that can route calls to a group of
                              phones or directory numbers in a line group.

Hunt pilots work in conjunction with hunt lists, which are prioritized lists of eligible paths (line groups) for incoming
                              calls. When a call is placed to a hunt pilot DN, the system offers the call to the first line group specified in the hunt
                              list. If no one in the first line group answers the call, the system offers the call to the next line group specified in the
                              hunt list. Line groups control the order in which the call is distributed to phones within the group. They point to specific
                              extensions, which are typically IP phone extensions or voicemail ports. Line groups cannot point to Computer Telephony Integration
                              (CTI) ports and CTI route points, so you cannot use hunt pilots to distribute calls to endpoints that are controlled through
                              CTI applications such as Cisco Customer Response Solution (CRS) or IP Interactive Voice Response (IP IVR).

A hunt pilot can distribute calls to any of its assigned line groups, even if the line groups and the hunt pilot reside in
                              different partitions. A call distributed by the hunt pilot overrides all the partitions and calling search space restrictions.

## Hunt Pilot Configuration Task Flow

Step 1

Configure Line Groups

Create a line group to enable multiple phones to answer calls that are directed to a single directory number (DN).

Step 2

Configure Hunt Lists

Configure a hunt list with a prioritized order of line groups.

Step 3

Configure Hunt Pilots

Configure a hunt pilot number or pattern that the system uses to direct calls to a hunt list.

### Configure Line Groups

Line groups let multiple phones answer calls that are directed to a single directory number. The Distribution Algorithm controls
                                 the order in which an incoming call gets distributed to the phones in the group.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Line Group .

Step 2

Choose one of the following options:

- Click Add New to create a new line group.

- Click Find and select an existing line group.

Step 3

Enter a Line Group Name .

Step 4

From the Distribution Algorithm field, select the type of algorithm that you want to use to distribute calls.

Step 5

Configure the fields in the Line Group Members to Add to Line Group section to add directory numbers to the line group:

Select a Partition where the directory numbers that you want to add reside.

Optional. Filter the search by completing the Directory Number Contains field.

Click Find . The list of Directory Numbers from the Partition appears in the  box

In the Available DN/Route Partition list box, select each directory number that you want to add to the group and click Add to Line Group .

Step 6

Configure the remaining fields in the Line Group Configuration window. See the online help for more information about the fields and their configuration options.

Step 7

Click Save .

### Configure Hunt Lists

A hunt list is a prioritized list of line groups. When the system routes a call through a hunt list, it uses the line groups
                                 in the order that you define in the hunt list.

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Hunt List .

Step 2

Choose one of the following options:

- Click Add New to create a new list.

- Click Find and select an existing list.

Step 3

Enter the Name for the Hunt List.

Step 4

Select a Cisco Unified Communications Manager Group to which you want to register the Hunt List.

Step 5

Check the Enable this Hunt List check box to enable the hunt list immediately when you click Save.

Step 6

Check the For Voice Mail Usage check box if the hunt list is for voice mail.

Step 7

Click Save .

Step 8

Add line groups to your hunt list:

Click Add Line Group .

From the Line Group drop-down, select a line group to add to the hunt list.

Click Save .

Repeat these steps to add additional line groups.

### Configure Hunt Pilots

Step 1

From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Hunt Pilot .

Step 2

Choose one of the following options:

- Click Add New to create a new hunt pilot.

- Click Find and select an existing hunt pilot.

Step 3

In the Hunt Pilot field, enter the number or pattern that you want to use to route calls.

Step 4

From the Hunt List drop-down, select the hunt list to which you want to direct calls that match the hunt pilot number.

Step 5

Complete the remaining fields in the Hunt Pilot Configuration window. For help with the fields and their settings, see the online help.

Step 6

If you want to enable Call Queuing, check the Queue Calls check box and configure the fields in the Queuing section.

Step 7

Assign any digit transformation patterns that you want to apply to calling, connected or called parties.

Step 8

Click Save .

#### Wildcards and Special Characters in Hunt Pilots

Wildcards and special characters in hunt pilots allow a hunt pilot to match a range of numbers (addresses). Use these wildcards
                                    and special characters also to build instructions that enable the Cisco Unified Communications Manager to manipulate a number
                                    before sending it to an adjacent system.

The following table describes the wildcards and special characters that Cisco Unified Communications Manager supports.

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

#### Performance and Scalability for Hunt Pilots

The following performance and scalability restrictions apply:

A single Unified CM Cluster supports a maximum of
                                          15,000 hunt list devices.

A single Unified CM Subscriber supports a maximum of
                                          100 hunt pilots with call queuing enabled per node

Hunt list devices may be a combination of 1500 hunt
                                          lists with ten IP phones in each hunt list, 750 hunt lists with
                                          twenty IP phones in each hunt list, or similar combinations

When using the broadcast algorithm for call coverage, the number of
                                                      hunt list devices is limited
                                                      by the number of busy hour call attempts (BHCA). Note that a BHCA
                                                      of 10 on a hunt pilot
                                                      pointing to a hunt list or hunt group containing 10 phones and
                                                      using the broadcast algorithm is
                                                      equivalent to 10 phones with a BHCA of 10.

The maximum number of hunt pilots is 100 per Unified CM subscriber node with call queue enabled when configured with 32 callers
                                          which is allowed in the queue. The total number of queue slots per node (the value of "Maximum Number of Callers Allowed in
                                          Queue" for all Call Queuing Enabled Hunt Pilots on the node combined) is limited to 3200. The maximum number of simultaneous
                                          callers in a queue for each hunt pilot is 100, meaning 100 callers per hunt pilot is allowed in a queue and the maximum number
                                          of hunt pilots is reduced to 32. The maximum number of members across all hunt lists does not change when call queuing is
                                          enabled.

The maximum wait time in queue for each hunt pilot that you can
                                          configure ranges from 0 to 3600 seconds (default 900). An increase in the number of hunt lists can require you to
                                          increase the dial plan initialization timer that is specified in
                                          the Unified Communications Manager service parameters. We recommend
                                          that you set the dial plan initialization timer to 600 seconds if
                                          you have 1500 hunt lists configured.

We recommend having no more than 35 directory numbers for a
                                          single line group when using broadcast algorithms with call
                                          queuing. Additionally, the number
                                          of broadcast line groups depends
                                          on the busy hour call completion rate (BHCC). If there are multiple broadcast line groups in a
                                          Unified CM system, the number of
                                          maximum directory numbers in a line group must be less than 35. The
                                          number of busy hour call
                                          attempts (BHCA) for all the broadcast line groups should not exceed
                                          35 calls set up per second.

## Hunt Pilot Interactions and Restrictions

Feature

Interactions and Restrictions

Single Number Reach with Hunt Groups

If you have a hunt group configured and one or more of the directory numbers that the hunt group points toward also has Single
                                       Number Reach (SNR) enabled, the call does not extend to the SNR remote destinations unless all devices in the hunt group are
                                       logged in.

For each device within the hunt group, the Logged Into Hunt Group check box must be checked within the Phone Configuration window for that device.

Call Queuing

Call Queuing is a subfeature of hunt pilots. When call queuing is enabled and the incoming call requirement to a particular
                                       hunt pilot exceeds the number of hunt members whom are available to answer a call, the system queues incoming calls until
                                       a hunt member is available to answer them. You can configure announcements and music on hold to play to callers while they
                                       are waiting.

For additional configuration details, see the 'Configure Call Queuing' chapter of the Feature Configuration Guide for Cisco Unified Communications Manager .

Unified Mobility

We don’t recommend configuring Unified Mobility devices in Hunt pilot.

### Calls Not Being Distributed

Restriction

Description

Calls are not being distributed correctly in Circular algorithm for a line group with BOT and TCT devices.

When a call is extended to an agent who is in a logged off state and the call is rejected with a different reject type other
                                          than the " Huntlogout " type. Then the index will not get incremented and the call will go to the same agent who had answered the previous call.

Calls are not distributed correctly in Circular algorithm for a line group.

While distributing the calls in a circular algorithm, when an agent is busy, the call is extended to the next available agent
                                          (i.e. the next agent will answer the call on behalf of the busy agent).

In the case of multiple calls at the same time, the next available agent answers the call.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Configure Line Groups | Create a line group to enable multiple phones to answer calls that are directed to a single directory number (DN). |
| Step 2 | Configure Hunt Lists | Configure a hunt list with a prioritized order of line groups. |
| Step 3 | Configure Hunt Pilots | Configure a hunt pilot number or pattern that the system uses to direct calls to a hunt list. |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Line Group . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New to create a new line group. Click Find and select an existing line group. |
| Step 3 | Enter a Line Group Name . |
| Step 4 | From the Distribution Algorithm field, select the type of algorithm that you want to use to distribute calls. |
| Step 5 | Configure the fields in the Line Group Members to Add to Line Group section to add directory numbers to the line group: Select a Partition where the directory numbers that you want to add reside. Optional. Filter the search by completing the Directory Number Contains field. Click Find . The list of Directory Numbers from the Partition appears in the  box In the Available DN/Route Partition list box, select each directory number that you want to add to the group and click Add to Line Group . |
| Step 6 | Configure the remaining fields in the Line Group Configuration window. See the online help for more information about the fields and their configuration options. |
| Step 7 | Click Save . |

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Hunt List . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New to create a new list. Click Find and select an existing list. |
| Step 3 | Enter the Name for the Hunt List. |
| Step 4 | Select a Cisco Unified Communications Manager Group to which you want to register the Hunt List. |
| Step 5 | Check the Enable this Hunt List check box to enable the hunt list immediately when you click Save. |
| Step 6 | Check the For Voice Mail Usage check box if the hunt list is for voice mail. |
| Step 7 | Click Save . |
| Step 8 | Add line groups to your hunt list: Click Add Line Group . From the Line Group drop-down, select a line group to add to the hunt list. Click Save . Repeat these steps to add additional line groups. |

| Note | For information about wildcards and special characters that you can use for the hunt pilot, see Wildcards and Special Characters in Hunt Pilots . |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose Call Routing > Route/Hunt > Hunt Pilot . |
|---|---|
| Step 2 | Choose one of the following options: Click Add New to create a new hunt pilot. Click Find and select an existing hunt pilot. |
| Step 3 | In the Hunt Pilot field, enter the number or pattern that you want to use to route calls. |
| Step 4 | From the Hunt List drop-down, select the hunt list to which you want to direct calls that match the hunt pilot number. |
| Step 5 | Complete the remaining fields in the Hunt Pilot Configuration window. For help with the fields and their settings, see the online help. |
| Step 6 | If you want to enable Call Queuing, check the Queue Calls check box and configure the fields in the Queuing section. |
| Step 7 | Assign any digit transformation patterns that you want to apply to calling, connected or called parties. |
| Step 8 | Click Save . |

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

| Note | When using the broadcast algorithm for call coverage, the number of
                                                      hunt list devices is limited
                                                      by the number of busy hour call attempts (BHCA). Note that a BHCA
                                                      of 10 on a hunt pilot
                                                      pointing to a hunt list or hunt group containing 10 phones and
                                                      using the broadcast algorithm is
                                                      equivalent to 10 phones with a BHCA of 10. |
|---|---|

| Feature | Interactions and Restrictions |
|---|---|
| Single Number Reach with Hunt Groups | If you have a hunt group configured and one or more of the directory numbers that the hunt group points toward also has Single
                                       Number Reach (SNR) enabled, the call does not extend to the SNR remote destinations unless all devices in the hunt group are
                                       logged in. For each device within the hunt group, the Logged Into Hunt Group check box must be checked within the Phone Configuration window for that device. |
| Call Queuing | Call Queuing is a subfeature of hunt pilots. When call queuing is enabled and the incoming call requirement to a particular
                                       hunt pilot exceeds the number of hunt members whom are available to answer a call, the system queues incoming calls until
                                       a hunt member is available to answer them. You can configure announcements and music on hold to play to callers while they
                                       are waiting. For additional configuration details, see the 'Configure Call Queuing' chapter of the Feature Configuration Guide for Cisco Unified Communications Manager . |
| Unified Mobility | We don’t recommend configuring Unified Mobility devices in Hunt pilot. |

| Restriction | Description |
|---|---|
| Calls are not being distributed correctly in Circular algorithm for a line group with BOT and TCT devices. | When a call is extended to an agent who is in a logged off state and the call is rejected with a different reject type other
                                          than the " Huntlogout " type. Then the index will not get incremented and the call will go to the same agent who had answered the previous call. |
| Calls are not distributed correctly in Circular algorithm for a line group. | While distributing the calls in a circular algorithm, when an agent is busy, the call is extended to the next available agent
                                          (i.e. the next agent will answer the call on behalf of the busy agent). Note In the case of multiple calls at the same time, the next available agent answers the call. | Note | In the case of multiple calls at the same time, the next available agent answers the call. |
| Note | In the case of multiple calls at the same time, the next available agent answers the call. |

| Note | In the case of multiple calls at the same time, the next available agent answers the call. |
|---|---|