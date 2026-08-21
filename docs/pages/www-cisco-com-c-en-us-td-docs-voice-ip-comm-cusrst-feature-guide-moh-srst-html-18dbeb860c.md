---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cusrst-feature-guide-moh-srst-html-18dbeb860c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusrst/feature/guide/MOH_srst.html
retrieved_at: 2026-08-21T21:30:02.725484+00:00
---

Cisco Unified Survivable Remote Site Telephony 8.0 Music On Hold Enhancement

# Cisco Unified Survivable Remote Site Telephony 8.0 Music On Hold Enhancement

### Download Options

Updated: July 11, 2010

## Table Of Contents

Cisco Unified Survivable Remote Site Telephony 8.0 Music On Hold Enhancement

Finding Feature Information

Contents

Prerequisites for Cisco Unified SRST  8.0

Information About MOH Enhancement for Cisco Unified SRST  8.0

Music On Hold Enhancement

Caching MOH Files for Enhanced System Performance

Cisco Unified SRST and Cisco Unified Communications Manager

How to Configure Cisco Unified SRST 8.0 New Features

Configuring MOH-groups for Cisco Unified SRST (fallback)

Prerequisites

Configuring Buffer Size for MOH Files

Prerequisites

Restrictions

Examples

Verifying MOH File Caching

Mapping Phone Extensions and Multicast Addresses (standby mode)

Verifying Music on Hold Enhancements

Additional References

Related Documents

Standards

MIBs

RFCs

Technical Assistance

Command Reference

Feature Information for Cisco Unified SRST 8.0

## Cisco Unified Survivable Remote Site Telephony 8.0 Music On Hold Enhancement

First Published: October,21, 2009

Last Updated: October,21, 2009

This document describes the Music On Hold Enhancement introduced in Cisco Unified Survivable Remote Site Telephony 8.0 (Cisco Unified SRST).

## Finding Feature Information

Your software release may not support all the features documented in this module. For the latest feature information and caveats, see the release notes for your platform and software release. To find information about the features documented in this module, and to see a list of the releases in which each feature is supported, see the "Feature Information for Cisco Unified SRST 8.0" section .

Use Cisco Feature Navigator to find information about platform support and Cisco IOS, Catalyst OS, and Cisco IOS XE software image support. To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn . An account on Cisco.com is not required.

## Contents

• Prerequisites for Cisco Unified SRST  8.0

• Information About MOH Enhancement for Cisco Unified SRST  8.0

• How to Configure Cisco Unified SRST 8.0 New Features

• Additional References

• Command Reference

• Feature Information for Cisco Unified SRST 8.0

## Prerequisites for Cisco Unified SRST  8.0

• Cisco Unified SRST 8.0

• Cisco IOS Release 15.0(1)XA

## Information About MOH Enhancement for Cisco Unified SRST  8.0

To configure Music On Hold Enhancement feature, you should understand the following concept:

• Music On Hold Enhancement

• Caching MOH Files for Enhanced System Performance

• Cisco Unified SRST and Cisco Unified Communications Manager

### Music On Hold Enhancement

Cisco Unified SRST 8.0 and later versions enhance the MOH feature by playing different media streams to PSTN and VoIP G.711 callers who are placed on hold. The MOH enhancement allows you to configure up to five additional media streams supplied from different media files stored in a router's flash memory and eliminates the need of separate routers for streaming multiple MOH media files.

Cisco Unified SRST 8.0 MOH enhancement creates five MOH groups for Cisco Unified SRST voice gateway and allows you to associate phones with different MOH-groups on the basis of their extension numbers to receive different MOH media streams.When Cisco Unified SRST is in fallback mode, callers to the extension numbers configured under the extension-range defined in MOH groups can listen to MOH media streams when they are placed on hold.

You can configure up to five MOH groups with media source files for ephones in different departments in a branch. Each MOH media file can be of 100 KB file size. For configuration information, see the "Configuring MOH-groups for Cisco Unified SRST (fallback)" section .

Following precedence rules are applicable when an ephone caller is placed on hold:

– If an ephone falls within an extension-range defined in a voice MOH-group, then the MOH defined in that voice MOH-group takes precedence.

– Ephones that do not fall in any extension-ranges defined in a voice MOH group default to MOH defined in call-manager-fallback.

Note We recommend that departments in a branch must have mutually exclusive extension numbers and multicast destinations for configuring MOH groups,

### Caching MOH Files for Enhanced System Performance

Caching MOH files helps enhance the system performance by reducing the CPU usage. However, caching requires memory buffer to store a large MOH file. You can set up a buffer file size for caching MOH files that you might use in the future. The default MOH file buffer size is 64 KB (8 seconds). The maximum buffer size (per file) can be configured anywhere between 64 KB (8 seconds) to 10000 KB (approximately 20 minutes), You can use the moh-file-buffer command to allocate MOH file buffer for future MOH files, see the, Configuring Buffer Size for MOH Files . To verify if a file is being cached and to update a cached moh-file, see the, Verifying MOH File Caching

Note If the file size is larger than the allocated buffer size, caching is disabled.

### Cisco Unified SRST and Cisco Unified Communications Manager

When the Cisco Unified SRST is in "standby" mode the Cisco Unified Communications Manager is in operation and all ephones are registered to Cisco Unified Communications Manager. The Cisco Unified SRST is not involved in processing any hold request. Media packets are streamed from different MOH files to several multicast and loopback addresses. An accurate mapping of multicast address and extension numbers is required between Cisco Unified Communications Manager and Cisco Unified SRST routers so that the phones can listen to the correct MOH media stream when placed on hold. For more information see "Mapping Phone Extensions and Multicast Addresses (standby mode)" section

## How to Configure Cisco Unified SRST 8.0 New Features

This section contains the following tasks.

• Configuring MOH-groups for Cisco Unified SRST (fallback)

• Mapping Phone Extensions and Multicast Addresses (standby mode)

• Verifying Music on Hold Enhancements

### Configuring MOH-groups for Cisco Unified SRST (fallback)

To configure voice MOH-groups on Cisco Unified SRST, perform the following steps:

### Prerequisites

• Cisco Unified SRST 8.0 or a later version.

• You must configure at least one ephone and directory number (DN), even if the gateway is not used for Cisco Unified SRST.

### SUMMARY STEPS

1. enable

2. configure terminal

3. voice moh-group moh-group-tag

4. description string

5. moh filename

6. multicast moh ip-address port port-number route ip-address-list

7. extension-range starting-extension to ending-extension

8. exit

### DETAILED STEPS

Command or Action

Purpose

Step 1

enable

Example:

Router> enable

Enables privileged EXEC mode.

• Enter your password if prompted.

Step 2

configure terminal

Example:

Router# configure terminal

Enters global configuration mode.

Step 3

moh-group tag

Example:

Router(conf)#voice moh-group 1

Router(conf-voice-moh-group)#

Enters the voice MOH-group configuration mode. You can create up to five voice MOH-groups for ephones receiving music on hold audio files when placed on hold. Range for the voice MOH-groups is 1 to 5.

Step 4

description string

Example:

Router(config)#

Router(config)#voice moh-group 1#

Router(config-voice-moh-group)# descri ption this is a moh group for sales

(Optional) Allows you to add a brief description specific to a voice MOH group. You can use up to 64 characters to describe the voice MOH group.

Step 5

Moh - filename

Example:

```
Router(config)# voice moh-group 1
```

```
Router(config-voice-moh-group)#description this 
is a moh group for sales
```

```
Router(config-voice-moh-group)# moh 
flash:/minuet.wav
```

Enables music on hold from a flash G.711 audio file. This file must exist on flash. The MOH filename should be unique among all MOH-groups. MOH filename length should not exceed 128 characters. You must provide the directory and filename of the MOH file in URL format. For example: moh flash:/minuet.au

• If you specify a file with this command and later want to use a different file, you must disable use of the first file with the no moh command before configuring the second file.

Step 6

multicast moh

Example:

```
Router(config)# voice moh-group 1
```

```
Router(config-voice-moh-group) #description this is a moh group for sales
```

```
Router(config-voice-moh-group)# moh minuet.wav 
Router(config-voice-moh-group)# multicast moh 
239.1.1.21 port 16384 route 10.1.4.31 10.1.1.2
```

Specifies that this audio stream is to be used for multicast and also for MOH. The multicast IP address must be unique among all MOH groups.

Note This command is required to use MOH for internal calls and it must be configured after MOH is enabled with the moh command.

• ip-address —Destination IP address for multicast.

• port port-number —Media port for multicast. Range is 2000 to 65535. We recommend port 2000 because it is already used for normal RTP media transmissions between IP phones and the router.

• route —(Optional) List of explicit router interfaces for the IP multicast packets.

• ip-address-list —(Optional) List of up to four explicit routes for multicast MOH. The default is that the MOH multicast stream is automatically output on the interfaces that correspond to the address that was configured with the ip source-address command.

Note For MOH on internal calls, packet flow must be enabled to the subnet on which the phones are located.

Step 7

Extension-range starting-extension to ending-extension

Example:

```
Router(config)# voice moh-group 1
```

```
Router(config-voice-moh-group)#description this 
is a moh group for sales
```

Router(config-voice-moh-group)# moh minuet.wav Router(config-voice-moh-group)# multicast moh 239.1.1.21 port 16384 route 10.1.4.31 10.1.1.2

Router(config-voice-moh-group)# extension-range 1021 to 1021

(Optional) Identifies MOH callers calling the extension numbers specified in a MOH group during Cisco Unified SRST fallback mode. Extension number must be in hexadecimal digits (0-9) or (A-F). Repeat this command to add additional extension ranges. Multiple extension-ranges can be defined in a MOH-group.

• starting-extension —Lists the starting extension number for a moh-group.

• ending-extension —Lists the ending extension number for a moh-group.

Note The ending extension number must be greater than the starting extension number. Extension-ranges must not overlap with any other extension-range configured in any other MOH-groups.

Note If an ephone number does not match any extension ranges in any MOH-groups, the caller will default to the MOH configuration in ccm-manager-fallback .

Step 8

end

Example:

Router(config)# end

Returns to privileged EXEC mode.

### Configuring Buffer Size for MOH Files

### Prerequisites

• Cisco Unified SRST 8.0 or a later version.

### Restrictions

• MOH file caching is prohibited if live-feed is enabled for MOH-group 0.

• MOH file buffer size must be larger than the MOH file size that needs to be cached.

• Sufficient system memory must be available for MOH file caching.

### SUMMARY STEPS

1. enable

2. configure terminal

3. call-manager-fallback

4. moh-file-buffer file size

5. end

### DETAILED STEPS

Command or Action

Purpose

Step 1

enable

Example:

Router> enable

Enables privileged EXEC mode.

• Enter your password if prompted.

Step 2

configure terminal

Example:

Router# configure terminal

Enters global configuration mode.

Step 3

call-manager-fallback

Example:

Router(config-cm-fallback)#

Enters call-manager-fallback configuration mode.

Step 4

m oh-file-buffer file size

Example:

Router(config-telephony)# moh-file-buffer 2000

(Optional) Allows to set a buffer for the MOH file size. You can configure a max file buffer size (per file) anywhere between 64KB (8 seconds) to 10000 KB (approximately 20 minutes), Default moh-file-buffer size is 64 KB (8 seconds).

Note A large buffer size is desirable to cache the largest MOH file and a better system performance.

Step 5

end

Example:

Router(config-ephone)# end

Returns to privileged EXEC mode.

### Examples

The following example shows a moh-file-buffer size of 2000 KB assigned for future moh files under the call-manager-fallback configuration mode.

!

!

!

!

call-manager-fallback

max-conferences 8 gain -6

transfer-system full-consult

moh-file-buffer 2000

!

!

line con 0

exec-timeout 0 0

line aux 0

### Verifying MOH File Caching

Step 1 Use the show ephone moh command to verify if the a MOH file is being cached. The following example shows that the minuet.au music file in MOH group 1 is not cached. Follow steps a through d to verify the MOH file is being cached.

```
Router #show ephone moh
```

```
Skinny Music On Hold Status (moh-group 1)
```

```
Active MOH clients 0 (max 830), Media Clients 0
```

```
File flash:/minuet.au (not cached) type AU Media_Payload_G711Ulaw64k 160 bytes
```

```
Moh multicast 239.10.16.6 port 2000
```

a. If the file is not cached as in MOH group 1 in the above example, then check file size in the flash.

For example:

```
Router# dir flash:/minuet.au
```

```
Directory of flash:/minuet.au 32  -rw- 1865696  Apr 25 2009 00:47:12 +00:00  moh1.au
```

b. Under telephony-service, configure "moh-file-buffer < file size >". Default file size is 64 KB (8 seconds). Make sure you enter a larger file size to cache large MOH files that you may use in future.

For example:

```
Router(config)# telephony-service
```

```
Router(config-telephony)# moh-file-buffer 2000
```

c. Under voice moh-group ( group tag ), configure "no moh", and immediately configure "moh ( filename )". This allows the system to read the file immediately from flash again.

```
For example:
```

```
Router(config-telephony)# voice moh-group 1
```

```
Router(config-voice-moh-group)# no moh
```

```
Router(config-voice-moh-group)# moh flash:/minuet.au
```

d. Depending on the size of the file, you should see the MOH file caching after a few minutes (approximately, 2 minutes).

```
For example:
```

```
Router #show ephone moh
```

```
Skinny Music On Hold Status - group 1
```

```
Active MOH clients 0 (max 830), Media Clients 0
```

```
File flash:/moh1.au (cached) type AU Media_Payload_G711Ulaw64k 160 bytes
```

```
Moh multicast 239.10.16.6 port 2000
```

### Mapping Phone Extensions and Multicast Addresses (standby mode)

To map the multicast address and extension number between Cisco Unified Communications Manager and Cisco Unified SRST routers, use the following command on Cisco Unified Communications Manager version 5.0 or later platform CLI.:

un sql select D.name, M.mohaudiosourceid, M.multicastaddress, M.multicastport, C.name codec from mohservermulticastinfo as M, device AS D, OUTER typemohcodec as C WHERE M.fkdevice = D.pkid AND M.tkmohcodec = C.enu

Note Running the above command on Cisco Unified Communications Manager version 5.0 and later platform CLI allows you to find the multicast addresses used by a MOH group.

Table 1 shows the difference between incrementing on an IP address and incrementing on a port number, using the base IP address of 239.1.1.1 and the base port number of 16384. The table also matches Cisco Unified Communications Manager audio sources and codecs to IP addresses and port numbers.

Table 1 Example of the Differences Between Incrementing Multicast on IP Address and Incrementing Multicast on Port Number

MOH Group

Codec

Increment Multicast on IP Address

Increment Multicast on Port Number

Destination IP Address

Destination Port

Destination IP Address

Destination

Port

1

G.711 mu-law

239.1.1.1

16384

239.1.1.1

16384

1

G.711 a-law

239.1.1.2

16384

239.1.1.1

16386

1

G.729

239.1.1.3

16384

239.1.1.1

16388

1

Wide band

239.1.1.4

16384

239.1.1.1

16390

2

G.711 mu-law

239.1.1.5

16384

239.1.1.1

16392

2

G.711 a-law

239.1.1.6

16384

239.1.1.1

16394

2

G.729

239.1.1.7

16384

239.1.1.1

16396

2

Wide band

239.1.1.8

16384

239.1.1.1

16398

For example, as seen in Table 1 , IP address 239.1.1.1 port 16384 for G.711 mu-law codec is assigned to audio source group 1 and 239.1.1.5 port 16384 for G.711 mu-law is assigned to audio source group 2. It is important to configure a Cisco Unified Communications Manager IP address and port number that use a G.711 audio sources for Cisco Unified SRST multicast MOH.

The MOH Server Configuration window is also where the multicast audio source for the MOH server is configured. For Cisco Unified SRST multicast MOH, the Cisco Unified Communications Manager MOH server can use only one audio source. An audio source is selected by inputting the audio source's maximum number of hops.

The Max Hops configuration sets the length of the transmission of the audio source packets. Limiting the number of hops is one way to stop audio packets from reaching the WAN and thus spoofing Cisco Unified Communications Manager so Cisco Unified SRST can multicast MOH. If all of your branches run Cisco Unified SRST, use a low number of hops to prevent audio source packets from crossing the WAN. If your system configuration includes routers that do not run Cisco Unified SRST, enter a high number of hops to allow source packets to cross the WAN. For more information on setting up the MOH on Cisco Unified Communications Manager see the Cisco Unified Communications Manager Administration Guide

### Verifying Music on Hold Enhancements

Step 1 Use the show voice moh-group command to display one or the entire MOH group configuration. The following example shows six (include MOH group 0) MOH groups. MOH group 0 is configured under call-manager-fallback configuration and all the other MOH groups are configured under voice MOH-group.

Router# sh voice moh-group

call-manager-fallback

moh flash:/alaska.wav

Moh multicast 239.1.1.1 port 16384 route 10.1.4.31 10.1.1.2

voice moh-group 1

description (not configured)

moh flash:/1001.au

multicast moh 239.1.1.5 port 16384 route 10.1.4.31 10.1.1.2

extension-range 1001 to 1001

voice moh-group 2

description (not configured)

moh RedRedWine8bitmulawg711.wav

multicast moh 239.1.1.9 port 16384 route 10.1.4.31 10.1.1.2

extension-range 1006 to 1006

voice moh-group 3

description (not configured)

moh flash2:/enter_dest1.au

multicast moh 239.1.1.13 port 16384 route 10.1.4.31 10.1.1.2

extension-range 1011 to 1011

voice moh-group 4

description (not configured)

moh flash:/audio/dir_menu.au

multicast moh 239.1.1.17 port 16384 route 10.1.4.31 10.1.1.2

extension-range 1016 to 1016

voice moh-group 5

description (not configured)

moh flash:/moh-f1004-on1s-off1s-g711u.wav

multicast moh 239.1.1.21 port 16384 route 10.1.4.31 10.1.1.2

extension-range 1021 to 1021

Step 2 Use the show ephone moh to display the status of different MOH groups configured for ephones. The following example shows five MOH groups configured for ephones.

Router #show ephone moh

Skinny Music On Hold Status (moh-group 1)

Active MOH clients 0 (max 830), Media Clients 0

File flash:/minuet.au (not cached) type AU Media_Payload_G711Ulaw64k 160 bytes

Moh multicast 239.10.16.6 port 2000

Skinny Music On Hold Status (moh-group 2)

Active MOH clients 0 (max 830), Media Clients 0

File flash:/audio/hello.au type AU Media_Payload_G711Ulaw64k 160 bytes

Moh multicast on 239.10.16.6 port 2000 via 0.0.0.0

Skinny Music On Hold Status (moh-group 3)

Active MOH clients 0 (max 830), Media Clients 0

File flash:/bells.au type AU Media_Payload_G711Ulaw64k 160 bytes

Moh multicast on 239.10.16.5 port 2000 via 0.0.0.0

Skinny Music On Hold Status (moh-group 4)

Active MOH clients 0 (max 830), Media Clients 0

File flash:/3003.au type AU Media_Payload_G711Ulaw64k 160 bytes

Moh multicast on 239.10.16.7 port 2000 via 0.0.0.0

Skinny Music On Hold Status (moh-group 5)

Active MOH clients 0 (max 830), Media Clients 0

File flash:/4004.au type AU Media_Payload_G711Ulaw64k 160 bytes

Moh multicast on 239.10.16.8 port 2000 via 0.0.0.0

Step 3 Use the show voice moh-group statistics command to display the MOH subsystem statistics information. In the following example, the MOH Group Streaming Interval Timing Statistics shows the media packet counts during streaming intervals.

MOH Group Packet Transmission Timing Statistics shows the numbers the time it takes for the MOH groups to send out the packets. These numbers are microseconds in maximum and minimum.

The MOH Group Loopback Interval Timing Statistics is available when loopback interface is configured as part of the multicast MOH routes as in the case of SRST. These counts are loopback packet counts within certain streaming timing intervals.

```
Router# show voice moh-group statistics
```

MOH Group Streaming Interval Timing Statistics:

Grp# ~19 msec 20~39 40~59 60~99 100~199 200+ msec

==== ========== ========== ========== ========== ========= ==========

0: 25835 17559966 45148 0 0 1

1: 19766 17572103 39079 0 0 1

2: 32374 17546886 51687 0 0 1

3: 27976 17555681 47289 0 0 1

4: 34346 17542940 53659 0 0 1

5: 14971 17581689 34284 0 0 1

MOH Group Packet Transmission Timing Statistics:

Grp# max(usec) min(usec)

==== ========= ==========

0: 97 7.

1: 95 7.

2: 97 7.

3: 96 7.

4: 94 7.

5: 67 7.

MOH Group Loopback Interval Timing Statistics:

loopback event array: svc_index=1542, free_index=1549, max_q_depth=31

Grp# ~19 msec 20~39 40~59 60~99 100~199 200+ msec

==== ========== ========== ========== ========== ========== ==========

0: 8918821 8721527 10023 0 1 1

1: 9007373 8635813 7184 0 1 1

2: 8864760 8772851 12758 0 1 1

3: 8924447 8715457 10464 0 1 1

4: 8858393 8778957 13017 0 1 1

5: 9005511 8639936 4919 0 1 1

Statistics collect time: 4 days 2 hours 5 minutes 39 seconds.

Step 4 Use the clear voice moh-group statistics command to clear the display of MOH subsystem statistics information.

Example:

```
Router# clear voice moh-group statistics
```

All moh group stats are cleared

## Additional References

The following sections provide references related to Cisco Unified SRST.

### Related Documents

Related Topic

Document Title

Cisco Unified SRST configuration

• Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions)

• Cisco Unified SRST and SIP SRST Command Reference

Cisco IOS voice configuration

• Cisco IOS Voice Configuration Library

• Cisco IOS Voice Command Reference

### Standards

Standard

Title

No new or modified standards are supported by this feature, and support for existing standards has not been modified by this feature.

—

### MIBs

MIB

MIBs Link

No new or modified MIBs are supported by this feature, and support for existing MIBs has not been modified by this feature.

To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco MIB Locator found at the following URL:

http://www.cisco.com/go/mibs

### RFCs

RFC

Title

No new or modified RFCs are supported by this feature, and support for existing RFCs has not been modified by this feature.

—

### Technical Assistance

Description

Link

The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving technical issues with Cisco products and technologies.

To receive security and technical information about your products, you can subscribe to various services, such as the Product Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds.

Access to most tools on the Cisco Support website requires a Cisco.com user ID and password.

http://www.cisco.com/techsupport

## Command Reference

The following commands are introduced or modified in the features documented in this module. For information about these commands, see the Cisco Unified SRST and SIP SRST Command Reference at http://www.cisco.com/en/US/docs/voice_ip_comm/cusrst/command/reference/srstcr.html .

For information about all Cisco IOS commands, use the Command Lookup Tool at http://tools.cisco.com/Support/CLILookup or the Cisco IOS Master Command List, All Releases , at http://www.cisco.com/en/US/docs/ios/mcl/allreleasemcl/all_book.html .

• clear voicemoh-group statistics

• description (moh-group)

• extension-range

• moh-file-buffer

• moh(voice-moh-group)

• show ephone moh

• show ephone summary

• show voice moh-group

• show moh-group statistics

• voice moh-group

## Feature Information for Cisco Unified SRST 8.0

Table 2 lists the release history for this feature.

Not all commands may be available in your Cisco IOS software release. For release information about a specific command, see the command reference documentation.

Use Cisco Feature Navigator to find information about platform support and software image support. Cisco Feature Navigator enables you to determine which Cisco IOS software images support a specific software release, feature set, or platform. To access Cisco Feature Navigator, go to http://www.cisco.com/go/cfn . An account on Cisco.com is not required.

Note Table 2 lists only the Cisco IOS software release that introduced support for a given feature in a given Cisco IOS software release train. Unless noted otherwise, subsequent releases of that Cisco IOS software release train also support that feature.

Table 2 Feature Information for Cisco Unified SRST 8.0

Feature Name

Releases

Feature Information

Cisco Unified SRST 8.0

15.0(1)XA

• Adds support for Music on Hold Enhancement.

### Cisco and the Cisco Logo are trademarks of Cisco Systems, Inc. and/or its affiliates in the U.S. and other countries. A listing of Cisco's trademarks can be found at www.cisco.com/go/trademarks . Third party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1005R)

### Any Internet Protocol (IP) addresses used in this document are not intended to be actual addresses. Any examples, command display output, and figures included in the document are shown for illustrative purposes only. Any use of actual IP addresses in illustrative content is unintentional and coincidental. © 2009 Cisco Systems, Inc. All rights reserved.

### This Document Applies to These Products

- Unified Survivable Remote Site Telephony

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. • Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | moh-group tag Example: Router(conf)#voice moh-group 1 Router(conf-voice-moh-group)# | Enters the voice MOH-group configuration mode. You can create up to five voice MOH-groups for ephones receiving music on hold audio files when placed on hold. Range for the voice MOH-groups is 1 to 5. |
| Step 4 | description string Example: Router(config)# Router(config)#voice moh-group 1# Router(config-voice-moh-group)# descri ption this is a moh group for sales | (Optional) Allows you to add a brief description specific to a voice MOH group. You can use up to 64 characters to describe the voice MOH group. |
| Step 5 | Moh - filename Example: Router(config)# voice moh-group 1 Router(config-voice-moh-group)#description this 
is a moh group for sales Router(config-voice-moh-group)# moh 
flash:/minuet.wav | Enables music on hold from a flash G.711 audio file. This file must exist on flash. The MOH filename should be unique among all MOH-groups. MOH filename length should not exceed 128 characters. You must provide the directory and filename of the MOH file in URL format. For example: moh flash:/minuet.au • If you specify a file with this command and later want to use a different file, you must disable use of the first file with the no moh command before configuring the second file. |
| Step 6 | multicast moh Example: Router(config)# voice moh-group 1 Router(config-voice-moh-group) #description this is a moh group for sales Router(config-voice-moh-group)# moh minuet.wav 
Router(config-voice-moh-group)# multicast moh 
239.1.1.21 port 16384 route 10.1.4.31 10.1.1.2 | Specifies that this audio stream is to be used for multicast and also for MOH. The multicast IP address must be unique among all MOH groups. Note This command is required to use MOH for internal calls and it must be configured after MOH is enabled with the moh command. • ip-address —Destination IP address for multicast. • port port-number —Media port for multicast. Range is 2000 to 65535. We recommend port 2000 because it is already used for normal RTP media transmissions between IP phones and the router. • route —(Optional) List of explicit router interfaces for the IP multicast packets. • ip-address-list —(Optional) List of up to four explicit routes for multicast MOH. The default is that the MOH multicast stream is automatically output on the interfaces that correspond to the address that was configured with the ip source-address command. Note For MOH on internal calls, packet flow must be enabled to the subnet on which the phones are located. |
| Step 7 | Extension-range starting-extension to ending-extension Example: Router(config)# voice moh-group 1 Router(config-voice-moh-group)#description this 
is a moh group for sales Router(config-voice-moh-group)# moh minuet.wav Router(config-voice-moh-group)# multicast moh 239.1.1.21 port 16384 route 10.1.4.31 10.1.1.2 Router(config-voice-moh-group)# extension-range 1021 to 1021 | (Optional) Identifies MOH callers calling the extension numbers specified in a MOH group during Cisco Unified SRST fallback mode. Extension number must be in hexadecimal digits (0-9) or (A-F). Repeat this command to add additional extension ranges. Multiple extension-ranges can be defined in a MOH-group. • starting-extension —Lists the starting extension number for a moh-group. • ending-extension —Lists the ending extension number for a moh-group. Note The ending extension number must be greater than the starting extension number. Extension-ranges must not overlap with any other extension-range configured in any other MOH-groups. Note If an ephone number does not match any extension ranges in any MOH-groups, the caller will default to the MOH configuration in ccm-manager-fallback . |
| Step 8 | end Example: Router(config)# end | Returns to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router> enable | Enables privileged EXEC mode. • Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | call-manager-fallback Example: Router(config-cm-fallback)# | Enters call-manager-fallback configuration mode. |
| Step 4 | m oh-file-buffer file size Example: Router(config-telephony)# moh-file-buffer 2000 | (Optional) Allows to set a buffer for the MOH file size. You can configure a max file buffer size (per file) anywhere between 64KB (8 seconds) to 10000 KB (approximately 20 minutes), Default moh-file-buffer size is 64 KB (8 seconds). Note A large buffer size is desirable to cache the largest MOH file and a better system performance. |
| Step 5 | end Example: Router(config-ephone)# end | Returns to privileged EXEC mode. |

| MOH Group | Codec | Increment Multicast on IP Address | Increment Multicast on Port Number |
|---|---|---|---|
| Destination IP Address | Destination Port | Destination IP Address | Destination Port |
| 1 | G.711 mu-law | 239.1.1.1 | 16384 | 239.1.1.1 | 16384 |
| 1 | G.711 a-law | 239.1.1.2 | 16384 | 239.1.1.1 | 16386 |
| 1 | G.729 | 239.1.1.3 | 16384 | 239.1.1.1 | 16388 |
| 1 | Wide band | 239.1.1.4 | 16384 | 239.1.1.1 | 16390 |
| 2 | G.711 mu-law | 239.1.1.5 | 16384 | 239.1.1.1 | 16392 |
| 2 | G.711 a-law | 239.1.1.6 | 16384 | 239.1.1.1 | 16394 |
| 2 | G.729 | 239.1.1.7 | 16384 | 239.1.1.1 | 16396 |
| 2 | Wide band | 239.1.1.8 | 16384 | 239.1.1.1 | 16398 |

| Related Topic | Document Title |
|---|---|
| Cisco Unified SRST configuration | • Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions) • Cisco Unified SRST and SIP SRST Command Reference |
| Cisco IOS voice configuration | • Cisco IOS Voice Configuration Library • Cisco IOS Voice Command Reference |

| Standard | Title |
|---|---|
| No new or modified standards are supported by this feature, and support for existing standards has not been modified by this feature. | — |

| MIB | MIBs Link |
|---|---|
| No new or modified MIBs are supported by this feature, and support for existing MIBs has not been modified by this feature. | To locate and download MIBs for selected platforms, Cisco IOS releases, and feature sets, use Cisco MIB Locator found at the following URL: http://www.cisco.com/go/mibs |

| RFC | Title |
|---|---|
| No new or modified RFCs are supported by this feature, and support for existing RFCs has not been modified by this feature. | — |

| Description | Link |
|---|---|
| The Cisco Support website provides extensive online resources, including documentation and tools for troubleshooting and resolving technical issues with Cisco products and technologies. To receive security and technical information about your products, you can subscribe to various services, such as the Product Alert Tool (accessed from Field Notices), the Cisco Technical Services Newsletter, and Really Simple Syndication (RSS) Feeds. Access to most tools on the Cisco Support website requires a Cisco.com user ID and password. | http://www.cisco.com/techsupport |

| Feature Name | Releases | Feature Information |
|---|---|---|
| Cisco Unified SRST 8.0 | 15.0(1)XA | • Adds support for Music on Hold Enhancement. |