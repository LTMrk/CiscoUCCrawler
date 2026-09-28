---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-trouble-12-5-1-cucm-b-troubleshooting-guide-1251-cucm-b-troubleshooting-056cf29a0c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/trouble/12_5_1/cucm_b_troubleshooting-guide-1251/cucm_b_troubleshooting-guide-1251_chapter_0101.html
retrieved_at: 2026-08-16T18:15:36.387129+00:00
---

Troubleshooting Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Troubleshooting Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: November 24, 2023

Chapter: Dial Plans and Routing Issues

## Chapter: Dial Plans and Routing Issues

# Dial Plans and Routing Issues

This section addresses common problems that you may experience with dial plans, route partitions, and calling search spaces.

## Route Partitions and
                        	 Calling Search Spaces

Route partitions inherit the error-handling capabilities for the Unified Communications Manager software. This means that a console and SDI file trace are provided for logging information and error messages. These messages
                           will be part of the digit analysis component of the traces. You must know how the Partitions and Calling Search Spaces are
                           configured and what devices are in each partition and its associated calling search space to determine the source of the problem.
                           The Calling Search Space determines what numbers are available for making a call. The Partition determines allowable calls
                           to a device or route list.

Refer to the route plan chapters in the System Configuration Guide for Cisco Unified Communications Manager for more information.

The following
                           		trace shows an example of a dialed number that is in the device Calling Search
                           		Space. For more detailed explanations about SDI traces, review the case studies
                           		in this document.

```
08:38:54.968 CCM Communications Manager|StationInit - InboundStim - OffHookMessageID tcpHandle=0x6b8802808:38:54.968 CCM CallManager|StationD - stationOutputDisplayText tcpHandle=0x6b88028, Display= 5000 
08:38:54.968 CCM CallManager|StationD - stationOutputSetLamp stim: 9=Line instance=1 lampMode=LampOn tcpHandle=0x6b88028
08:38:54.968 CCM CallManager|StationD - stationOutputCallState tcpHandle=0x6b88028
08:38:54.968 CCM CallManager|StationD - stationOutputDisplayPromptStatus tcpHandle=0x6b88028
08:38:54.968 CCM CallManager|StationD - stationOutputSelectSoftKeys tcpHandle=0x6b88028
08:38:54.968 CCM CallManager|StationD - stationOutputActivateCallPlane tcpHandle=0x6b88028
08:38:54.968 CCM CallManager|Digit analysis: match(fqcn="5000", cn="5000", pss="RTP_NC_Hardwood:RTP_NC_Woodland:Local RTP", dd="")
```

In the Digit
                           		Analysis component of the previous trace, the pss (Partition Search Space, also
                           		known as Calling Search Space) gets listed for the device that is placing the
                           		call.

In the
                           		following trace, RTP_NC_Hardwood;RTP_NC_Woodland;Local_RTP represent the
                           		partitions that this device is allowed to call.

```
08:38:54.968 CCM CallManager|Digit analysis: potentialMatches=PotentialMatchesExist08:38:54.968 CCM CallManager|StationD - stationOutputStartTone: 33=InsideDialTone tcpHandle=0x6b88028
08:38:55.671 CCM CallManager|StationInit - InboundStim - KeypadButtonMessageID kpButton: 5 tcpHandle=0x6b88028
08:38:55.671 CCM CallManager|StationD - stationOutputStopTone tcpHandle=0x6b88028
08:38:55.671 CCM CallManager|StationD - stationOutputSelectSoftKeys tcpHandle=0x6b88028
08:38:55.671 CCM CallManager|Digit analysis: match(fqcn="5000", cn="5000", pss="RTP_NC_Hardwood:RTP_NC_Woodland:Local RTP", dd="5")
08:38:55.671 CCM CallManager|Digit analysis: potentialMatches=PotentialMatchesExist
08:38:56.015 CCM CallManager|StationInit - InboundStim - KeypadButtonMessageID kpButton: 0 tcpHandle=0x6b88028
08:38:56.015 CCM CallManager|Digit analysis: match(fqcn="5000", cn="5000", pss="RTP_NC_Hardwood:RTP_NC_Woodland:Local RTP", dd="50")
08:38:56.015 CCM CallManager|Digit analysis: potentialMatches=PotentialMatchesExist
08:38:56.187 CCM CallManager|StationInit - InboundStim - KeypadButtonMessageID kpButton: 0 tcpHandle=0x6b88028
08:38:56.187 CCM CallManager|Digit analysis: match(fqcn="5000", cn="5000", pss="RTP_NC_Hardwood:RTP_NC_Woodland:Local RTP", dd="500")
08:38:56.187 CCM CallManager|Digit analysis: potentialMatches=PotentialMatchesExist
08:38:56.515 CCM CallManager|StationInit - InboundStim - KeypadButtonMessageID kpButton: 3 tcpHandle=0x6b88028
08:38:56.515 CCM CallManager|Digit analysis: match(fqcn="5000", cn="5000", pss="RTP_NC_Hardwood:RTP_NC_Woodland:Local RTP", dd="5003")
08:38:56.515 CCM CallManager|Digit analysis: analysis results
08:38:56.515 CCM CallManager||PretransformCallingPartyNumber=5000
```

Be aware that
                           		PotentialMatchesExist is the result of digit analysis of the numbers that were
                           		dialed until the exact match is found and the call is routed accordingly.

The following trace describes what happens when the Unified Communications Manager is attempting to dial the directory number
                           1001 and it is not in the Calling Search Space for that device. Again, be aware that the digit analysis routine had potential
                           matches until only the first digit was dialed. The route pattern that is associated with the digit 1 resides in a partition
                           that is not in the device calling search space, RTP_NC_Hardwood;RTP_NC_Woodland;Local_RTP. Therefore, the phone received a
                           reorder tone (busy signal).

```
08:38:58.734 CCM CallManager|StationInit - InboundStim - OffHookMessageID tcpHandle=0x6b8802808:38:58.734 CCM CallManager|StationD - stationOutputDisplayText tcpHandle=0x6b88028, Display= 5000 
08:38:58.734 CCM CallManager|StationD - stationOutputSetLamp stim: 9=Line instance=1 lampMode=LampOn tcpHandle=0x6b88028
08:38:58.734 CCM CallManager|StationD - stationOutputCallState tcpHandle=0x6b88028
08:38:58.734 CCM CallManager|StationD - stationOutputDisplayPromptStatus tcpHandle=0x6b88028
08:38:58.734 CCM CallManager|StationD - stationOutputSelectSoftKeys tcpHandle=0x6b88028
08:38:58.734 CCM CallManager|StationD - stationOutputActivateCallPlane tcpHandle=0x6b88028
08:38:58.734 CCM CallManager|Digit analysis: match(fqcn="5000", cn="5000", pss="RTP_NC_Hardwood:RTP_NC_Woodland:Local RTP", dd="")
08:38:58.734 CCM CallManager|Digit analysis: potentialMatches=PotentialMatchesExist
08:38:58.734 CCM CallManager|StationD - stationOutputStartTone: 33=InsideDialTone tcpHandle=0x6b88028
08:38:59.703 CCM CallManager|StationInit - InboundStim - KeypadButtonMessageID kpButton: 1 tcpHandle=0x6b88028
08:38:59.703 CCM CallManager|StationD - stationOutputStopTone tcpHandle=0x6b88028
08:38:59.703 CCM CallManager|StationD - stationOutputSelectSoftKeys tcpHandle=0x6b88028
08:38:59.703 CCM CallManager|Digit analysis: match(fqcn="5000", cn="5000", pss="RTP_NC_Hardwood:RTP_NC_Woodland:Local RTP", dd="1")
08:38:59.703 CCM CallManager|Digit analysis: potentialMatches=NoPotentialMatchesExist
08:38:59.703 CCM CallManager|StationD - stationOutputStartTone: 37=ReorderTone tcpHandle=0x6b88028
```

Route
                           		partitions work by associating a partition name with every directory number in
                           		the system. The directory number can be called only if the calling device
                           		contains the partition within a list of partitions to which it is permitted to
                           		place calls—its partition search space. This provides for extremely powerful
                           		control over routing.

When a call
                           		is being placed, digit analysis attempts to resolve the dialed address only in
                           		those partitions that the partition search space specifies. Each partition name
                           		comprises a discrete subset of the global dialable address space. From each
                           		listed partition, digit analysis retrieves the pattern that best matches the
                           		sequence of dialed digits. Then, from among the matching patterns, digit
                           		analysis chooses the best match. If two patterns equally match the sequence of
                           		dialed digits, digit analysis breaks the tie by choosing the pattern that is
                           		associated with the partition that is listed first in the partition search
                           		space.

## Group Pickup Configuration

### Symptom

Group pickup feature does not work for a group that is configured with a partition.

### Possible 
                              
                              Cause

The Calling Search Space (CSS) may not be configured correctly for each Directory Number (DN) in the group

### Example

The following steps provide an example of correct group pickup configuration with partitioning:

Configure a pickup group named Marketing/5656, where Marketing is the partition and 5656 is the pickup number.

On the configuration for DNs 6000 and 7000, respectively, add these DNs to the pickup group that is named Marketing/5656 .

### Recommended 
                              
                              Action

If group pickup fails, check the CSS of each domain name (DNs 6000 and 7000 in this example). If the partition that is called Marketing is not contained in each CSS in this example, then the configuration is incorrect and may cause a failed pickup.

## Dial Plan Issues

This section addresses dial plan issues.

### Problem When Dialing
                           	 a Number

#### Symptom

Problems
                                 		  occur when a number is dialed.

#### Possible
                                 		  Cause

A Dial Plan comprises a list of numbers and groups of numbers that tell the Unified Communications Manager to what devices (such as phones and gateways) to send calls when a certain string of digits is collected. Consider this setup
                                 as analogous to a static routing table in a router.

Be sure that your dial plan concepts, basic call routing, and planning are carefully considered and properly configured before
                                 trying to troubleshoot a potential dial plan issue. Often, the problem lies with planning and configuration. Refer to the
                                 route plan configuration chapters in the System Configuration Guide for Cisco Unified Communications Manager for more information.

#### Recommended
                                 		  Action

Identify the
                                       				Directory Number (DN) that is originating the call.

Identify the
                                       				Calling Search Space for this DN.

Tip

The Calling
                                                   				  Search Space determines what numbers are available for making a call.

If applicable,
                                       				identify devices with which the Calling Search Space associates with this DN.
                                       				Make sure that you identify the correct device; because multiple line
                                       				appearances are supported, you can have the same DN on multiple devices. Keep
                                       				track of the device calling search space.

If this is a Cisco Unified IP Phone that is originating the call, remember that a particular line (DN) and the device with
                                       which a line is associated have calling search spaces. They will get combined when a call is made. For example, if line instance
                                       1000 has a Calling Search Space of AccessLevelX and the Cisco Unified IP Phone that has extension 1000 configured on it has
                                       AccessLevelY as its Calling Search Space, then when making a call from that line appearance, Unified Communications Manager will search through partitions that are contained in Calling Search Space AccessLevelX and AccessLevelY.

Identify which
                                       				Partitions associate with the Calling Search Space(s).

Tip

The Partition
                                                   				  determines allowable calls to a device or route list.

Identify to
                                       				which Partition of the device the call should (or should not) go.

Identify which
                                       				number is being dialed. Keep track of if and when the user is getting a
                                       				secondary dial tone. Also keep track of what they receive after all the digits
                                       				have been entered (reorder, fast-busy). Does the user get the progress tones
                                       				before expecting to receive anything? Make sure that callers wait at least 10
                                       				seconds after entering the last digit because they may have to wait for the
                                       				interdigit timer to expire.

Generate a Route Plan Report in Unified Communications Manager and use it to examine all the route patterns for the partitions that are in the Calling Search Space for the problem call.

If necessary,
                                       				add or modify the Route Patterns or Route Filters.

If you can find
                                       				the Route Pattern to which the call is being sent, keep track of the Route List
                                       				or Gateway to which the pattern points.

If it is a Route
                                       				List, check which Route Groups are part of the list and which gateway(s) is
                                       				part of the Route Groups.

Verify that the applicable devices are registered with Unified Communications Manager .

If a gateway has no access to Unified Communications Manager , use the show tech command to capture and verify this information.

Pay attention to
                                       				the @ sign. This macro can expand to include many different things. It gets
                                       				often used in combination with filtering options.

If a device is
                                       				not part of a partition, consider it to be part of the Null or default
                                       				partition. Every user should be able to call that device. The system always
                                       				searches the Null partition last.

If you dial an
                                       				outside number that is matching a 9.@ pattern and it takes 10 seconds before
                                       				the call goes through, check the filtering options. By default, with a 9.@
                                       				pattern, when a 7-digit number is dialed, the Cisco Unified IP Phone will wait
                                       				10 seconds before placing the call. You need to apply a Route Filter to the
                                       				pattern that displays LOCAL-AREA-CODE DOES-NOT- EXIST and END-OF-DIALING
                                       				DOES-NOT-EXIST.

### Secure Dial Plan

Use partitions and calling search spaces, in addition to more common filtering based on sections of the @ macro (which stands
                              for the North American Numbering Plan) in a route pattern, to configure Unified Communications Manager to create a secure dialing plan for users. Partitions and Calling Search Spaces provide an integral part of security and
                              are especially useful for multitenant environments and for creating an individual user level. Filtering, a subset of the Calling
                              Search Space/Partition concept, can add additional granularity to the security plan.

Be advised that usually the last thing that you want to do when you try to fix a filtering problem is to run an SDI trace.
                              Not enough information exists, and the potential for causing more harm is too great.

## Automated Alternate Routing (AAR) Limitation with Remote Gateways

### Symptom

AAR exhibits the limitation that calls routed over a remote gateway during a high-bandwidth situation fail, and the calls
                              cannot be routed over the local gateway when AAR is used. This functionality is important to customers who use Tail-End Hop
                              Off (TEHO) for toll bypass.

### Recommended 
                              
                              Action

The following example provides a workaround to use for calls that must be routed over a remote gateway in high-bandwidth situations
                              when AAR is in use.

### Workaround Example

Use a specific partition for the TEHO in question.

In the following example, headquarters (HQ) has area code 408 and the Branch (BR1) has area code 919.

Configure as follows:

Create theTehoBr1forHQPt partition and assign this partition to the calling search space (CSS) of the HQ devices with a higher
                                    priority than the regular PSTN access uses.

Create the TehoBr1forHQRL route list and add the BR1 gateway route group to this route list as the first option and the HQ
                                    gateway as the second option.

Apply called party modification within the route list. In this case, apply predot called party modification for the BR1 route
                                    group, and apply predot and prefix 1919 called party modification for the HQ route group.

Ensure that the gateway does not perform called party modification.

Create a route pattern in the TehoBr1forHQPt partition.

Ensure that no called party modifications are applied in the route pattern.

### Results

In an out-of-bandwidth situation, after Unified Communications Manager tries to allocate the first route group for TEHO (BR1 route group), Unified Communications Manager retries the second route group, at which point the system strips the 91919 string and replaces it with the 1919 string, which
                              is suitable for long-distance dialing. Because the string is configured for use by the local gateway, less rerouting takes
                              place.

AAR works on a per-external-phone-number-mask basis and cannot be processed for an external PSTN number because the system
                              does not know the phone number mask of the PSTN number. This workaround provides AAR functionality and improves network resiliency.

| Tip | The Calling
                                                   				  Search Space determines what numbers are available for making a call. |
|---|---|

| Tip | The Partition
                                                   				  determines allowable calls to a device or route list. |
|---|---|