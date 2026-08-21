---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-210536-supporting-v-a2719cda07
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/210536-Supporting-Variable-Length-Dial-Plans-fo.html
retrieved_at: 2026-08-21T13:55:55.686028+00:00
---

Supporting Variable Length Dial Plans for Cisco CallManager Route Patterns - an Exercise in Designing a Route Pattern that Covers a National Dial Plan

# Supporting Variable Length Dial Plans for Cisco CallManager Route Patterns - an Exercise in Designing a Route Pattern that Covers a National Dial Plan

### Download Options

Updated: April 9, 2017

Document ID: 210536

Contents

## Contents

## Introduction

This document describes how to make Cisco CallManager dial the PUblic Switch Telephone Network (PSTN) number as soon as the last digit is dialed.

## Prerequisites

### Requirements

There are no specific requirements for this document.

This configuration was tested with Cisco CallManager version 11.x and IOS® Software version 12.1.3aXI5 IP plus feature set on the Gateway Router. This example assumes a Cisco CallManager outside access code of 0.

The information presented in this document was created from devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If you are in a production network, ensure that you understand the potential impact of any command before use it.

## Background Information

Cisco CallManager installations in North America are able to use the '@' macro in the route patterns to allow the use of variable length dial plans. If a caller dials a seven digit local number, or a ten/eleven digit long distance number, the call will be sent out to the public switched telephone network (PSTN) immediately after the last digit is dialed. However, this macro does not work outside of North America. In the past, customers have used the alternative route pattern of 0.! to handle calls with variable length dial plans. This wildcard character allows a called number string of any length, but it will wait a default interdigit timeout of ten seconds before route the called number to the gateway device. Customers have the option of shorten this timer, but it can lead to problems with users who pause mid way through dialing. The Cisco CallManager may interpret the pause as the end of dial delay and outpulse an incomplete number.

As an alternative to use the '!' wildcard, as follows is a case study in create a variable length dial plan for a national numbering scheme. With this dial plan users can dial services, informational, local and long distance numbers without the need to wait the interdigit timeout period.

The international access code will still use the '!' wildcard, as we cannot match all foreign dial plans, this is normally not a concern for most users.

## Design a Dial Plan that Meets Your Requirements

In this example, you will create a national dial plan that corresponds to the Australian national number system. It should be a simple matter to apply these principles to any other country, provided they use a consistent number scheme for local and long distance calls.

The dial plan below was developed for a CallManager located in a regional area. If youwant to have multiple levels of call barring that allowed for local (local exchange area only), regional STD (long distance), state STD, national STD and ISD (International) access. This was accomplished when you create granular matches on the dialed numbers and separating the numbers with the local prefix (555XXXXX) from the other number combinations. The different route patterns were put into separate partitions. Then calling party search spaces that included the different partitions were created. This provided an easy way of controll outdial access from each handset.

Note : You will need to modify this area of the dial plan to suit the local numbers where the Cisco CallManager is situated. The [] wildcards allow specifying a range of numbers, which reduces the overall number of similar route patterns.

The Australian Dial Plan consists of eight digit local numbers for the local exchange area. The first two digits of the eight digit local number are a region code. There is a two digit long distance (STD) access code which works on a state basis (leading digit is always 0, for example: 02) and it uses 0011 as the international access code. Mobile phones are in the range 04XX XXXXXX. Freecall Informational services come under 1-30X-XXXXXX, 1-800-XXXXXX , 1-900-XXXXXX or 13XXXX. Emergency calls use 000.

The 0055 Paycall Informational services have not been included in this dial plan, although this could have easily been done. If you did not want access for this service, though it would have been an easy matter to specify the 0055XXXXXX number range as a route pattern, then set the block this pattern option to bar the calls.

Please note that this is not an exhaustive list of all possible combinations. It is likely that there are other numbers that are not listed here, so it would be worthwhile to investigate the particular dial plan of your locality. Phone books often have lists of area code and informational/service numbers.

Dial Plan

Route

Pattern

Comments

0.000

emergency

0.013

information

0.123X

medical

0.124XX

medical

0.125XXX

medical

0.1194

time

0.1196

weather

0.12455

information

0.130XXXXXXX

130XXXXXXX

Freecall numbers

0.13[1-9]XXX

130000

Freecall information

0.1[8-9]XXXXXXXX

1-800/1-900

Freecall numbers

0.0[2-9]XXXXXXXX

02XXXXXXXX-09XXXXXXXX

national/mobile

0.[2-4]XXXXXXX

2XXXXXXX - 4XXXXXXX

STD - VIC - state

0.[6-9]XXXXXXX

6XXXXXXX - 9XXXXXXX

STD - VIC - state

0.5[0-4]XXXXXX

50XXXXXX - 54XXXXXX

STD - VIC - regional

0.5[6-9]XXXXXX

56XXXXXX - 59XXXXXX

STD - VIC - regional

0.55[0-4]XXXXX

550XXXXX - 554XXXXX

STD - VIC - regional

0.55[6-9]XXXXX

556XXXXX - 559XXXXX

STD - VIC - regional

0.555XXXXX

Local exchange numbers - 8 digit numbers

0.0011!

International - uses interdigit timeout (10 seconds)

0.0011!#

International-uses # as end of dial character

## Configure the Dial Plan in Cisco CallManager

Follow the steps below to configure the dial plan in Cisco CallManager.

- Enter an Access code of 0 '.' as the access code delimiter. Add the route pattern digits or wildcard matches.

- Ensure that the Route this pattern and Provide secondary dial tone options are set.

- Point the route pattern to a gateway device (H323, MGCP , SAA or SDA).

- If the gateway device is MGCP, SAA or SDA (Skinny protocol), the access code needs to be discarded. Under Called Party Transformations, set discard digits to < pre-dot >.

- If the gateway device is an IOS based H323 gateway, the access code needs to be passed with the called digits. Under Called Party Transformations, set discard digits to < none >.

- Insert the Route Pattern into the database.

- If the gateway device is an IOS based H323 gateway, proceed to Configuring the Router to Route the Calls

## Verify the Dial Plan

Verify the Dial Plan by examine the contents of the Route Pattern Configuration screen.

Once configured, the Cisco CallManager Dial Plan configuration should look some like this:

## Configure the Router to Route the Calls

This section explains how a Cisco IOS gateway is configured as a CallManager H323 gateway.

On the gateway router POTS dial peer that points to the PSTN ports, use a destination pattern of '0' to match the leading digit (access code) of the dialed digits that come from the CallManager. This explicit match on the '0' will cause the dial peer to strip off the leading 0, hence the rest of the called number is sent out. This is shown in the configuration segment below.

!

dial-peer voice 100 pots

direct-inward-dial

!-- DID for incoming calls

destination-pattern 0

!-- 0 is stripped when call is placed

port 1/0:15

!-- Direct the call to the PRI

port 1/0

!

You do not need any other POTS dial peers unless there are multiple POTS ports that will go into a hunt group. For example, if you had two FXO ports, the dial peers would look like this:

!

dial-peer voice 100 pots

destination-pattern 0

port 1/0/0

!

dial-peer voice 101 pots

destination-pattern 0

port 1/0/1

!

The calls will then cycle through these two configured voice ports.

## Summary

Cisco CallManager installations outside of North America are unable to use the inbuilt '@' route pattern macro as it only relates to the North American numbering plan. When use the procedure in this application note, you can develop local dial plans for their CallManager systems that remove the need to wait an interdigit timeout, and it allows calls to be placed as soon as the minimum required number of digits has been keyed in on the handsets.

Contributed by Cisco Engineers

### Contributed by Cisco Engineers

### This Document Applies to These Products

- Unified Communications Manager (CallManager)

| Dial Plan |
|---|
| Route | Pattern | Comments |
| 0.000 |  | emergency |
| 0.013 |  | information |
| 0.123X |  | medical |
| 0.124XX |  | medical |
| 0.125XXX |  | medical |
| 0.1194 |  | time |
| 0.1196 |  | weather |
| 0.12455 |  | information |
| 0.130XXXXXXX | 130XXXXXXX | Freecall numbers |
| 0.13[1-9]XXX | 130000 | Freecall information |
| 0.1[8-9]XXXXXXXX | 1-800/1-900 | Freecall numbers |
| 0.0[2-9]XXXXXXXX | 02XXXXXXXX-09XXXXXXXX | national/mobile |
| 0.[2-4]XXXXXXX | 2XXXXXXX - 4XXXXXXX | STD - VIC - state |
| 0.[6-9]XXXXXXX | 6XXXXXXX - 9XXXXXXX | STD - VIC - state |
| 0.5[0-4]XXXXXX | 50XXXXXX - 54XXXXXX | STD - VIC - regional |
| 0.5[6-9]XXXXXX | 56XXXXXX - 59XXXXXX | STD - VIC - regional |
| 0.55[0-4]XXXXX | 550XXXXX - 554XXXXX | STD - VIC - regional |
| 0.55[6-9]XXXXX | 556XXXXX - 559XXXXX | STD - VIC - regional |
| 0.555XXXXX |  | Local exchange numbers - 8 digit numbers |
| 0.0011! |  | International - uses interdigit timeout (10 seconds) |
| 0.0011!# |  | International-uses # as end of dial character |