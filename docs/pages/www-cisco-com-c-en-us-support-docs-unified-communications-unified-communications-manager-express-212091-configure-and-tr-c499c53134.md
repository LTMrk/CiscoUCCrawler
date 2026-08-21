---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-express-212091-configure-and-tr-c499c53134
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-express/212091-Configure-and-Troubleshoot-Directory-Ser.html
retrieved_at: 2026-08-21T09:47:09.057015+00:00
---

Configure and Troubleshoot Directory Service on CME

# Configure and Troubleshoot Directory Service on CME

### Download Options

Updated: September 14, 2017

Document ID: 212091

Contents

## Contents

## Introduction

This documents describes how to configure and troubleshhot directory services on Cisco Unfied Communications Manager Express (CME).

Contributed by Srinivasa Dee Conda and edited by Ramiro Amaya, Cisco TAC Engineers.

## Prerequisites

### Requirements

Cisco recommeds that you have basic understanding of these topics:

- CME Configuration ad Troubleshooting

- IP Phones

### Components used

This document is not restricted to a specific software version. However, the components used in this documents are:

- CME

- IP Phones

## Background Information

1. Local Directory

- CME creates a local directory which is presented to each IP Phone registered.

- This local directory includes all ephone DNs created in CME.

- In addition, numbers can be added to local directory manually by CME admin.

- Phone user can browse this directory in this way:

- Select Local Directory

- Type the First/Last name of the targeted user to search for. In case those fields left blank, all users in local directory is displayed

- The local directory page is displayed to phone user in XML format accessed using HTTP without password protection. Once Directories button pressed, the phone sends HTTP request to CME for URL http://#CME-IP#/localdirectory . CME parses the URL and respond with XML one.

- This URL is provided to phone Directories feature button as part of phone configuration file during phone registration.

2. External Directory

- Each feature button in IP Phone (Messages, Directories, Settings, etc) supports URL association

- The function of the button are based on the associated URL

- Based on this, you can assign external URL to Directories feature button. Once this is done, IP Phone browses an external directory instead of local directory in CME

- Once external directory URL is created, local directory services are automatically disabled in CME

Note :  The IP Phone needs to be reset in order to get the new URL

3. Called-Name Display

- This feature enables the display of called-party name on called-party phone

- The called-party name is obtained from local directory. This can be the name assigned to ephone DN or manually added to local directory.

- In case of overlap between ephone DN name and manual directory entry, the manual entry takes precedence.

## Configurations

```
telephony-service
 service dnis dir-lookup
 directory entry 1 3011 name Test-Phone1
!
ephone-dn 1 dual-line
 number 3011 
 name Test-Phone1
```

Configuration Template

```
ip http server

!

telephony-service

 directory {first-name-first | last-name-first}         !!!... Change the display mode of directory entries

 directory entry {directory-tag number name name | clear}           !!!... Manually add directory entries

 no service local-directory           !!!... Manually disable local directory services

 url directories url           !!!... Configure external directory URL

 service dnis dir-lookup           !!!... Enable called-name display feature

!

voice register global

 url directory url

!

ephone-dn dn-tag

 name name

!

voice register dn dn-tag

 name name
```

## Restrictions

- Configuring external directory service only works with non-Java based phones. Any Java based phone will display duplicate directories for the following:

- Missed

- Received

- Placed

- In case you want to use CUCM as external directory, the phones should be configured in CUCM to realize their MAC addresses. Its not necessary for the phones to register with CUCM or to assign DNs but they have to be configured for MAC address purpose.

## Troubleshoot

Collect packet capture on CME and collect " debug ip http all " on the CME to check the interaction between CME and the IP Phone for the local directory service.

This snippet explains the step by step interaction between the ip phone and the CME for a directory search.

Successful Search Scenario

1. Press Directory Button on the Phone

```
Router2811#
101245: Mar 24 07:29:24.992: %RITE-5-CAPTURE_START: Started IP traffic capture for interface FastEthernet0/0
101246: Mar 24 07:29:33.424: lds_urlhook, url=/localdirectory
101247: Mar 24 07:29:33.424: Mon, 24 Mar 2014 07:29:33 GMT 10.65.47.115 /localdirectory ok
 Protocol = HTTP/1.1 Method = GET Query = locale=English_United_States&name=SEP000000000002
101248: Mar 24 07:29:33.424:
101249: Mar 24 07:29:33.428: local_directory_search_get_action: minor = 0, uri_index =locale=English_United_States&name=SEP000000000002
101250: Mar 24 07:29:33.428: ipkeyswitch_ldir_send_file 1: page 0
101251: Mar 24 07:29:33.428: ipkeyswitch_ldir_send_file 3: to send prologue
Router2811#
```

2. Select Directory

```
Router2811#
101252: Mar 24 07:29:54.696: lds_urlhook, url=/localdirectory/query
101253: Mar 24 07:29:54.696: Mon, 24 Mar 2014 07:29:54 GMT 10.65.47.115 /localdirectory/query ok
 Protocol = HTTP/1.1 Method = GET
101254: Mar 24 07:29:54.696:
101255: Mar 24 07:29:54.700: local_directory_search_get_action: minor = 1, uri_index =
101256: Mar 24 07:29:54.700: ipkeyswitch_ldir_send_file 1: page 1
101257: Mar 24 07:29:54.700: ipkeyswitch_ldir_send_file 3: to send prologue
Router2811#
```

3.  Enter First Name of the User and Press Submit (example first name=Test)

```
Router2811#
101258: Mar 24 07:30:15.909: lds_urlhook, url=/localdirectory/search
101259: Mar 24 07:30:15.909: Mon, 24 Mar 2014 07:30:15 GMT 10.65.47.115 /localdirectory/search ok
 Protocol = HTTP/1.1 Method = GET Query = f=Test
101260: Mar 24 07:30:15.909:
101261: Mar 24 07:30:15.913: local_directory_search_get_action: minor = 2, uri_index =f=Test
101262: Mar 24 07:30:15.913: ipkeyswitch_ldir_send_file 1: page 2
101263: Mar 24 07:30:15.913: ipkeyswitch_ldir_send_file 3: to send prologue
101264: Mar 24 07:30:15.913: ipkeyswitch_dir_search_result 1: f=Test
101265: Mar 24 07:30:15.913: ipkeyswitch_dir_search_result 2: f=Test
101266: Mar 24 07:30:15.913: ipkeyswitch_dir_search_result token:f=Test, l=, p=
101267: Mar 24 07:30:15.913: ipkeyswitch_dir_search_result length:f=4, l=0, p=0
101268: Mar 24 07:30:15.913: valid_ephone_dn check for number: 3001
101269: Mar 24 07:30:15.913: valid_ephone_dn check for number: 3002
101270: Mar 24 07:30:15.917: valid_ephone_dn check for number: 3003
101271: Mar 24 07:30:15.917: valid_ephone_dn check for number: 3004
101272: Mar 24 07:30:15.917: valid_ephone_dn check for number: 3005
101273: Mar 24 07:30:15.917: valid_ephone_dn check for number: 3006
101274: Mar 24 07:30:15.917: valid_ephone_dn check for number: 3007
101275: Mar 24 07:30:15.917: valid_ephone_dn check for number: 19990000
101276: Mar 24 07:30:15.917: valid_ephone_dn invalid dn 9 number: 19990000
101277: Mar 24 07:30:15.917: valid_ephone_dn check for number: 3101
101278: Mar 24 07:30:15.917: valid_ephone_dn check for number: 3102
101279: Mar 24 07:30:15.917: valid_ephone_dn check for number:
101280: Mar 24 07:30:15.917: valid_ephone_dn check for number: 28282
101281: Mar 24 07:30:15.917: valid_ephone_dn check for number: 3998
101282: Mar 24 07:30:15.917: valid_ephone_dn check for number: 3457
101283: Mar 24 07:30:15.921: valid_ephone_dn check for number:
101284: Mar 24 07:30:15.921: valid_ephone_dn check for number: 3011
101285: Mar 24 07:30:15.921: ip_keyswitch_search_ephone_dn:
 f=Test-Phone1, l=
101286: Mar 24 07:30:15.921: ip_keyswitch_search_ephone_dn:
 matches: 1
101287: Mar 24 07:30:15.921: valid_ephone_dn check for number: 3012
101288: Mar 24 07:30:15.921: ip_keyswitch_search_sip_phone:
 f=cisco, l=
101289: Mar 24 07:30:15.921: ip_keyswitch_search_sip_phone:
 f=Harp, l=Test
101290: Mar 24 07:30:15.921: ip_keyswitch_search_directory_entry :
 f=Test-Phone1, l=
101291: Mar 24 07:30:15.921: ip_keyswitch_search_directory_entry: 2
```

### Contributed by Cisco Engineers

Srinivasa Dee Conda

Cisco TAC Engineer

Edited by Ramiro Amaya

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager Express