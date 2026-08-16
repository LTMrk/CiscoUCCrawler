---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-voi-cube-enum-enhance-kaplan-html-aeeffd6d12
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/voi-cube-enum-enhance-kaplan.html
retrieved_at: 2026-08-16T15:46:07.599133+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: ENUM Enhancement per Kaplan Draft RFC

## Chapter: ENUM Enhancement per Kaplan Draft RFC

# ENUM Enhancement per Kaplan Draft RFC

## Overview

The Cisco Unified Border Element (CUBE) facilitates the mapping of E.164 called numbers to Session Initiation Protocol (SIP)
                           Uniform Resource Identifiers (URIs). The SIP ENUM technology allows the traditional telephony part of the network (using E.164
                           numbering to address destinations) to interwork with the SIP telephony part of the network, generally using SIP URIs. From
                           the Public Switched Telephone Network (PSTN) network, if an end user dials an E.164 called party, the number can be translated
                           by an ENUM gateway into the corresponding SIP URI. This SIP URI is then used to look up the Domain Name System (DNS) Naming
                           Authority Pointer (NAPTR) Resource Records (RR). The NAPTR RR (as defined in RFC 2915) describes how the call should be forwarded
                           or terminated and records information, such as email addresses, a fax number, a personal website, a VoIP number, mobile phone
                           numbers, voicemail systems, IP-telephony addresses, and web pages. Alternately, when the calling party is a VoIP endpoint
                           and dials an E.164 number, then the originator's SIP user agent (UA) converts it into a SIP URI to be used to look up at the
                           ENUM gateway DNS and fetch the NAPTR RR.

The ENUM enhancement per Kaplan draft RFC provides source-based routing, that is, SIP-to-SIP calls can be routed based on
                           the source SIP requests. To provide source-based routing and to interact with the Policy Server, an EDNS0 OPT pseudo resource
                           record with source URI, incoming SIP call ID, outbound SIP call ID, and Call Session Identification are added to the ENUM
                           DNS query, according to draft-kaplan-enum-sip-routing-04 . The incoming SIP call ID, outbound SIP call ID, and Call Session Identification are automatically included with an EDNS0
                           OPT pseudo resource record in the ENUM DNS query only if “source-uri no-cache” is enabled and XCC service is registered. This
                           feature also provides the flexibility to disable route caching.

SIP-to-SIP calls can be routed based on the source SIP requests, using the ENUM enhancement feature. To provide source-based
                           routing and to interact with Policy Server, an EDNS0 OPT pseudo resource record with source URI, incoming SIP call ID, outbound
                           SIP call ID, and Call session Identification are added to the ENUM DNS query. The DNS server filters its response based on
                           the source URI and call ID information and returns the appropriate NAPTR entries. To enable this feature, you must use the source-uri option in the voice enum-match-table <table-number> command. In addition, you can use the no-cache option to disable caching.

Refer to RFC 3761 and draft-kaplan-enum-sip-routing-04 for more information about routing SIP requests with ENUM.

### Feature
                           	 Information for ENUM Enhancement per Kaplan Draft RFC

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature
                                             					 Name

Releases

Feature
                                             					 Information

ENUM
                                             					 Enhancement per Kaplan Draft RFC

Cisco IOS
                                             					 XE 3.14S

Cisco IOS
                                             					 15.5(1)T

The ENUM
                                             					 enhancement per Kaplan draft RFC provides source-based routing, that is,
                                             					 SIP-to-SIP calls can be routed based on the source SIP requests. To provide
                                             					 this source-based routing, an EDNS0 OPT pseudo resource record with source URI
                                             					 is added to the ENUM DNS query, according to draft-kaplan-enum-sip-routing-04 . This feature also provides
                                             					 the flexibility to disable route caching.

Support to
                                             					 include inbound call ID, outbound call ID and Call Session Identification to
                                             					 ENUM DNS query

Cisco IOS
                                             					 15.5(2)T

Cisco IOS
                                             					 XE 3.15S

This
                                             					 feature allows you to add incoming SIP call ID, outbound SIP call ID, and Call
                                             					 Session Identification to an EDNS0 OPT pseduo resource record in the ENUM DNS
                                             					 query.

## Restrictions

Supported only
                                 			 for SIP-to-SIP calls.

The full command
                                 			 of voice
                                       				  enum-match-table , including the options, needs to be specified
                                 			 whenever being referenced by its subcommand. If not, the defaults, no source-uri and no no-cached (or caching) will take effect.

As the maximum
                                 			 number of characters of the host shown in the show host command is 25, the source URI may not be displayed completely.

The source URI
                                 			 is displayed in a separate line below, starting with “source-uri=”. Refer to
                                 			 the show command outputs in this chapter.

If no-cache is configured in the voice
                                    				enum-match-table , no cache table look-up would be made and hence an ENUM
                                 			 query would be made regardless of what is in the cache table.

Both the target
                                 			 and source, where the source can be null/undefined or defined, need to be
                                 			 matched when looking up the cache table.

The OPT RR will
                                 			 be added to the query for a SIP-to-SIP call only if the source-uri is configured for the outbound enum-match-table .

The route will
                                 			 not be cached if the server does not support the OPT RR (it is recommended to
                                 			 remove the source-uri for this scenario if caching is preferred).

The source URL
                                 			 can be prefixed with a host/target in the host name field in a double quote in
                                 			 the show host host command to display routes for the host specific with this source.

A wild card,
                                 			 “*”, can be used to denote “all” hosts in the show host command. It can be by itself or any host matched with its prefix. The prefix
                                 			 can be a host name, partial or complete, or a domain name with partial or
                                 			 complete source URL.

Refer to the document titled Cisco Unified Border Element ENUM Support Configuration Example for a detailed message format.

## Configure ENUM

### Enable Source-Based Routing

### SUMMARY STEPS

- enable

- configure terminal

- voice enum-match-table match-table-index [ source-uri ]
                                    				[ no-cache ]

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables
                                             				privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

#### Example:

```
Device# configure terminal
```

Enters global
                                             				configuration mode.

Step 3

voice enum-match-table match-table-index [ source-uri ]
                                             				[ no-cache ]

#### Example:

```
Device(config)# voice enum-match-table 5 source-uri no-cache
```

Enables source
                                             				URI filtering for the enum match table entry. You can use the no-cache option to disable the caching to
                                             				the voice enum command.

Step 4

end

#### Example:

```
Device(config-enum)# end
```

Returns to
                                             				privileged EXEC mode.

### Test the ENUM Request

To test the ENUM
                                 		  request, you can use the source-url option so that the source-based routing enum can be tested.

### SUMMARY STEPS

- enable

- test enum match-table-index input
                                       				  -pattern source-url source-url more parameter

- end

### DETAILED STEPS

Step 1

enable

#### Example:

```
Device> enable
```

Enables
                                             				privileged EXEC mode.

Enter your password if prompted.

Step 2

test enum match-table-index input
                                                				  -pattern source-url source-url more parameter

#### Example:

```
Device# test enum 1117777 source sip:1116666@10.1.50.16 more “ibcall-id=1-23735@10.1.50.16;
obcall-id=7190DF-F1AA3CF1@10.1.110.222;sbc-id=1
```

Tests the
                                             				source-based routing ENUM.

The source routing or no caching features depend on the voice enum-match-table command. If the source-uri command is not configured, the source-url source-url in the test command is ignored.

Step 3

end

#### Example:

```
Device# end
```

Returns to
                                             				privileged EXEC mode.

### Verify the ENUM Request

Use the following show commands to verify your network setup. You can compare the output of these commands to the output of
                                 the ENUM test in order to verify that ENUM is working.

### SUMMARY STEPS

- show host
                                       				  *

- show host
                                       				  1.0.9.3.e164-test*

- show host
                                       				  1*

- show host
                                       				  "1.0.9.3.e164-test sip*"

### DETAILED STEPS

Step 1

show host
                                                				  *

#### Example:

```
Device# show host * Host                      Port     Flags    Age Type  Address(es)
ns.e164-test              None   (temp, OK)  0  IP    127.0.0.1
1.0.9.3.e164-test sip:540 NA     (temp, OK)  0  NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:5403@1.4.65.5"
1.1.9.3.e164-test sip:540 NA     (temp, OK)  0  NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:5403@1.4.65.5"
1.0.9.3.e164-test sip:540 NA     (temp, OK)  0  NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:3401@1.4.65.5"
```

Step 2

show host
                                                				  1.0.9.3.e164-test*

#### Example:

```
Device# show host  1.0.9.3.e164-test* Host                                Port     Flags          Age Type       Address(es)
1.0.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:5403@1.4.65.5"
1.0.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:3401@1.4.65.5"
```

Step 3

show host
                                                				  1*

#### Example:

```
Device# show host 1* Host                                Port     Flags          Age Type       Address(es)
1.0.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:5403@1.4.65.5"
1.1.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:5403@1.4.65.5"
1.0.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:3401@1.4.65.5"
```

Step 4

show host
                                                				  "1.0.9.3.e164-test sip*"

#### Example:

```
Device# show host “1.0.9.3.e164-test sip*” Host                                Port     Flags          Age Type       Address(es)
ns.e164-test                     None   (temp, OK)  0     IP          127.0.0.1
1.0.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:5403@1.4.65.5"
1.0.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:3401@1.4.65.5"
```

## Troubleshooting
                        	 Tips

Use the following
                           		commands for debugging information:

debug voip enum detail

debug ip domain

debug ccsip message

debug voip ccapi inout

clear voip fpi session correlator-id —This command is used to clear the
                                 			 hung FPI sessions. After the hung session is identified using the existing show commands
                                 			 and its correlator is obtained, the clear voip fpi
                                       				  session correlator-id command can be used to clear the
                                 			 session.

Use the following show command
                           		that is helpful for debugging:

show host [ all | * | host-name | partial -host
                                    				-name *]

Below is an extract of a sample ENUM DNS query containing the EDNS0 OPT
                           		psedo resource record fields as per Kaplan Draft that is helpful in debugging.
                           		In the below query the values corresponding to ibcall-id, obcall-id, and sbc-id
                           		represent the incoming SIP call ID, outbound SIP call ID and Call Session
                           		Identification respectively.

```
7.7.7.7.1.1.1.e164.arpa sip:1116666@10.1.50.16enum_dns_query: name = 7.7.7.7.1.1.1.e164.arpa
sip:1116666@10.1.50.16 type = 35, ns_server = 0x0 no_cache 1 more_data ;ibcall-id=1-23735@10.1.50.16;
obcall-id=7190DF-39DD11E4-8008EDAD-F1AA3CF1@10.1.110.222;sbc-id=1
```

## Configuration
                        	 Examples for ENUM Enhancement per Kaplan Draft RFC

```
voice enum-match-table 1 source-uri // The source URI is sent to the DNS server to filter the route. //
  description enable source-uri
  rule 2 1 /^\(.*\)$/ /\1/ e164.arpa
  
voice enum-match-table 2 source-uri no-cache
rule 1 1 /^\(.*\)$/ /\1/ e164-test

voice enum-match-table 3 no-cache // The cache table is not looked up and the route is not cached. //
 rule 1 1 /^\(.*\)$/ /\1/ e164-test
```

The following is a
                              		  sample configuration for the ENUM enhancement feature:

```
dial-peer voice 1 voip
	description ENUM Inbound dialpeer
	session protocol sipv2
	incoming called-number 1116666

dial-peer voice 2 voip
	description ENUM Outbound dialpeer 
	destination-pattern 1117777
	session protocol sipv2
	session target enum:1 // Session target configured to look up ENUM table 1. //
```

| Feature
                                             					 Name | Releases | Feature
                                             					 Information |
|---|---|---|
| ENUM
                                             					 Enhancement per Kaplan Draft RFC | Cisco IOS
                                             					 XE 3.14S Cisco IOS
                                             					 15.5(1)T | The ENUM
                                             					 enhancement per Kaplan draft RFC provides source-based routing, that is,
                                             					 SIP-to-SIP calls can be routed based on the source SIP requests. To provide
                                             					 this source-based routing, an EDNS0 OPT pseudo resource record with source URI
                                             					 is added to the ENUM DNS query, according to draft-kaplan-enum-sip-routing-04 . This feature also provides
                                             					 the flexibility to disable route caching. |
| Support to
                                             					 include inbound call ID, outbound call ID and Call Session Identification to
                                             					 ENUM DNS query | Cisco IOS
                                             					 15.5(2)T Cisco IOS
                                             					 XE 3.15S | This
                                             					 feature allows you to add incoming SIP call ID, outbound SIP call ID, and Call
                                             					 Session Identification to an EDNS0 OPT pseduo resource record in the ENUM DNS
                                             					 query. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                             				configuration mode. |
| Step 3 | voice enum-match-table match-table-index [ source-uri ]
                                             				[ no-cache ] Example: Device(config)# voice enum-match-table 5 source-uri no-cache | Enables source
                                             				URI filtering for the enum match table entry. You can use the no-cache option to disable the caching to
                                             				the voice enum command. |
| Step 4 | end Example: Device(config-enum)# end | Returns to
                                             				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                             				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | test enum match-table-index input
                                                				  -pattern source-url source-url more parameter Example: Device# test enum 1117777 source sip:1116666@10.1.50.16 more “ibcall-id=1-23735@10.1.50.16;
obcall-id=7190DF-F1AA3CF1@10.1.110.222;sbc-id=1 | Tests the
                                             				source-based routing ENUM. The source routing or no caching features depend on the voice enum-match-table command. If the source-uri command is not configured, the source-url source-url in the test command is ignored. |
| Step 3 | end Example: Device# end | Returns to
                                             				privileged EXEC mode. |

| Step 1 | show host
                                                				  * Example: Device# show host * Host                      Port     Flags    Age Type  Address(es)
ns.e164-test              None   (temp, OK)  0  IP    127.0.0.1
1.0.9.3.e164-test sip:540 NA     (temp, OK)  0  NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:5403@1.4.65.5"
1.1.9.3.e164-test sip:540 NA     (temp, OK)  0  NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:5403@1.4.65.5"
1.0.9.3.e164-test sip:540 NA     (temp, OK)  0  NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:3401@1.4.65.5" |
|---|---|
| Step 2 | show host
                                                				  1.0.9.3.e164-test* Example: Device# show host  1.0.9.3.e164-test* Host                                Port     Flags          Age Type       Address(es)
1.0.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:5403@1.4.65.5"
1.0.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:3401@1.4.65.5" |
| Step 3 | show host
                                                				  1* Example: Device# show host 1* Host                                Port     Flags          Age Type       Address(es)
1.0.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:5403@1.4.65.5"
1.1.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:5403@1.4.65.5"
1.0.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:3401@1.4.65.5" |
| Step 4 | show host
                                                				  "1.0.9.3.e164-test sip*" Example: Device# show host “1.0.9.3.e164-test sip*” Host                                Port     Flags          Age Type       Address(es)
ns.e164-test                     None   (temp, OK)  0     IP          127.0.0.1
1.0.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:5403@1.4.65.5"
1.0.9.3.e164-test sip:540 NA      (temp, OK)  0     NAPTR 0 0 U sip+E2U /^.*$/sip:3901@10.1.18.28/ Source-uri ="sip:3401@1.4.65.5" |