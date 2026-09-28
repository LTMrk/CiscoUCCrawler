---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-callmanager-215537-network-time-5b13c6d611
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/215537-network-time-protocol-ntp-on-cucm.html
retrieved_at: 2026-08-16T23:42:02.795051+00:00
---

Configure and Troubleshoot NTP on CUCM and IM&P

# Configure and Troubleshoot NTP on CUCM and IM&P

### Download Options

Updated: November 22, 2023

Document ID: 215537

Contents

## Contents

## Introduction

This document describes Network Time Protocol (NTP) for Cisco Unified Communications Manager (CUCM).

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Purpose of the Feature

This document covers the purpose of NTP with CUCM, the configuration of NTP, what data to collect to troubleshoot, example analysis of the data, and related resources for additional research.

The purpose of the NTP with CUCM is to ensure that the servers are aware of the correct time. The time in the CUCM servers is important because Voice Over Internet Protocol (VOIP) is extremely sensitive to time variations.

The CUCM cluster must maintain a time synchronization that remains close to the other servers in the cluster, this is due to database replication requirements.

Lastly, time to troubleshoot is important as you want to have the correct timestamps in the logs.

## Configure

Note : CUCM requires certain NTP servers.

The Windows NTP server is not supported for CUCM; however, other types such as Linux NTP sources, Cisco IOS® NTP sources, and Nexus OS NTP sources are acceptable.

Although other Cisco solutions can utilize Windows Servers for the NTP solution, UC Solutions such as Call Manager, Cisco Unity, and Instant Messaging and Presence, are unable to do so and require either a Linux-based or Cisco IOS®-based NTP solution.

This is because Windows Time Services often uses SNTP which Linux systems have difficulty synchronizing with.

### Network Diagram

The CUCM publisher needs an NTP source that is not a member of the CUCM cluster; therefore, the CUCM publisher synchronizes its time with the NTP server. In this exchange, the CUCM publisher is an NTP client.

The CUCM subscribers synchronize their time with the CUCM publisher. In this exchange, the CUCM publisher is an NTP server where the CUCM subscribers are NTP clients.

Caution : Be aware that the Cisco Instant Messaging & Presence (IM&P) servers are also considered subscribers of the CUCM cluster, hence, they also rely on the CUCMs NTP. In other words, if the NTP is out-of-sync on the IM&P server, it causes issues in the system with its Database Replication and High Availability.

### Installation Process

When CUCM is installed, there is a prompt to determine if the server is the first node in the cluster.

If the server is not the first node in the cluster, then the installation wizard moves past the NTP configuration phase; however, you are been prompted for the NTP server(s) if it is the first node in the cluster.

### After Installation, Use the OS Admin Web Page

### After Installation, Use the Command Line Interface

As shown in the images, you can find the commands used to access and modify the NTP servers within the CUCM server.

- The command utils ntp server list shows the NTP servers configured on your system.

- The command utils ntp server add ntp_address adds a new NTP server to the system.

Note : Keep in mind that if you want to add a new NTP server, the CUCM server tests reachability before it adds it, if it fails, the next error is seen.

- The command utils ntp server delete allows you to delete any of the NTPs already configured within the system.

## Troubleshoot

### Data to Collect

When you troubleshoot an NTP issue, you are required to collect this data from whichever CUCM server(s) have the NTP issues:

- The output from the command utils diagnose test .

- The output from the command utils ntp status .

- The NTP logs from the CUCM gathered from the Cisco Real-Time Monitor Tool (RTMT).

### Example Analysis

For example purposes, the next information from the CUCM Publisher and the NTP has been used:

CUCM Publisher

Version: 11.5(1) SU5

FQDN: cucm-115.home.lab

IP address starts with 192.X.X.X

NTP

From Google NTP Server

FQDN: time1.example.com.ntp

IP address starts with 216.X.X.X

#### PCAP Review for CUCM - No File

Notice the port number is 123. This is the port for NTP.  In the output from the command in the text box, you can see the NTP version is 4 as noted by the NTPv4. You can also take note of the publisher, which acts as a client when it establishes its communication with time1.example.com; however, it works as a server when it establishes communication with cucm-sub1, cucm-sub2 and cucm-sub3.

```
From the CLI of the publisher run the command " utils network capture port 123 "

Wait until you see traffic (this can take a little time, or it may be instant) then hit ctrl+c. Look in the traffic to find where your publisher is communicating with its NTP server and the NTP server is communication with the publisher (if the NTP server isn't replying then it is an issue in the network or with the NTP server). The primary focus of this output is the NTP version. In CUCM 9 and later NTP version 3 (NTPv3) can cause issues and an NTP source using NTPv4 should be the NTP server for the publisher.
```

```
admin:utils network capture size all count 10000000 port 123 Executing command with options:
 size=128                count=1000              interface=eth0
 src=dest=                   port=123
 ip=

16:08:43.199710 IP cucm-sub3.home.lab.39417 > cucm-115.home.lab.ntp: NTPv4 , Client, length 48
16:08:43.199737 IP cucm-115.home.lab.ntp > cucm-sub3.home.lab.39417: NTPv4, Server , length 48
16:08:43.199823 IP cucm-sub3.home.lab.39417 > cucm-115.home.lab.ntp: NTPv4, Client , length 48
16:08:43.199859 IP cucm-115.home.lab.ntp > cucm-sub3.home.lab.39417: NTPv4, Server, length 48
16:09:01.640980 IP cucm-115.home.lab.50141 > time1.example.com.ntp: NTPv4, Client , length 48
16:09:01.654675 IP time1.example.com.ntp > cucm-115.home.lab.50141: NTPv4, Server, length 48
16:09:01.654733 IP cucm-115.home.lab.50141 > time1.example.com.ntp: NTPv4, Client, length 48
16:09:01.667368 IP time1.example.com.ntp > cucm-115.home.lab.50141: NTPv4, Server, length 48
16:09:01.668612 IP cucm-115.home.lab.50141 > time1.example.com.ntp: NTPv4, Client, length 48
16:09:01.681366 IP time1.example.com.ntp > cucm-115.home.lab.50141: NTPv4, Server, length 48
16:09:01.681518 IP cucm-115.home.lab.50141 > time1.google.com.ntp: NTPv4, Client, length 48
16:09:01.694108 IP time1.google.com.ntp > cucm-115.home.lab.50141: NTPv4, Server, length 48
16:09:01.875016 IP cucm-115.home.lab.48422 > time1.google.com.ntp: NTPv4, Client, length 48
16:09:01.884476 IP cucm-sub3.home.lab.58072 > cucm-115.home.lab.ntp: NTPv4, Client, length 48
16:09:01.884568 IP cucm-115.home.lab.ntp > cucm-sub3.home.lab.58072: NTPv4, Server, length 48
16:09:01.884954 IP cucm-sub3.home.lab.58072 > cucm-115.home.lab.ntp: NTPv4, Client, length 48
16:09:01.884999 IP cucm-115.home.lab.ntp > cucm-sub3.home.lab.58072: NTPv4, Server, length 48
16:09:01.885381 IP cucm-sub3.home.lab.58072 > cucm-115.home.lab.ntp: NTPv4, Client, length 48
16:09:01.885423 IP cucm-115.home.lab.ntp > cucm-sub3.home.lab.58072: NTPv4, Server, length 48
16:09:01.886147 IP cucm-sub3.home.lab.58072 > cucm-115.home.lab.ntp: NTPv4, Client, length 48
16:09:01.886184 IP cucm-115.home.lab.ntp > cucm-sub3.home.lab.58072: NTPv4, Server, length 48
16:09:01.888555 IP time1.google.com.ntp > cucm-115.home.lab.48422: NTPv4, Server, length 48
16:09:01.888642 IP cucm-115.home.lab.48422 > time1.google.com.ntp: NTPv4, Client, length 48
16:09:01.900926 IP time1.google.com.ntp > cucm-115.home.lab.48422: NTPv4, Server, length 48
16:09:01.901017 IP cucm-115.home.lab.48422 > time1.google.com.ntp: NTPv4, Client, length 48
16:09:01.913497 IP time1.google.com.ntp > cucm-115.home.lab.48422: NTPv4, Server, length 48
16:09:01.913566 IP cucm-115.home.lab.48422 > time1.google.com.ntp: NTPv4, Client, length 48
16:09:01.926693 IP time1.google.com.ntp > cucm-115.home.lab.48422: NTPv4, Server, length 48
16:09:02.038981 IP cucm-sub2.home.lab.42078 > cucm-115.home.lab.ntp: NTPv4, Client, length 48
16:09:02.039117 IP cucm-115.home.lab.ntp > cucm-sub2.home.lab.42078: NTPv4, Server, length 48
16:09:02.039281 IP cucm-sub2.home.lab.42078 > cucm-115.home.lab.ntp: NTPv4, Client, length 48
16:09:02.039345 IP cucm-115.home.lab.ntp > cucm-sub2.home.lab.42078: NTPv4, Server, length 48
16:09:02.039434 IP cucm-sub2.home.lab.42078 > cucm-115.home.lab.ntp: NTPv4, Client, length 48
16:09:02.039535 IP cucm-115.home.lab.ntp > cucm-sub2.home.lab.42078: NTPv4, Server, length 48
16:09:02.039607 IP cucm-sub2.home.lab.42078 > cucm-115.home.lab.ntp: NTPv4, Client, length 48
16:09:02.039814 IP cucm-115.home.lab.ntp > cucm-sub2.home.lab.42078: NTPv4, Server, length 48
16:09:02.066544 IP cucm-sub1.home.lab.46400 > cucm-115.home.lab.ntp: NTPv4, Client, length 48
16:09:02.066622 IP cucm-115.home.lab.ntp > cucm-sub1.home.lab.46400: NTPv4, Server, length 48
16:09:02.066751 IP cucm-sub1.home.lab.46400 > cucm-115.home.lab.ntp: NTPv4, Client, length 48
16:09:02.066892 IP cucm-115.home.lab.ntp > cucm-sub1.home.lab.46400: NTPv4, Server, length 48
16:09:02.066968 IP cucm-sub1.home.lab.46400 > cucm-115.home.lab.ntp: NTPv4, Client, length 48
16:09:02.067104 IP cucm-115.home.lab.ntp > cucm-sub1.home.lab.46400: NTPv4, Server, length 48
16:09:02.067155 IP cucm-sub1.home.lab.46400 > cucm-115.home.lab.ntp: NTPv4, Client, length 48
16:09:02.067189 IP cucm-115.home.lab.ntp > cucm-sub1.home.lab.46400: NTPv4, Server, length 48
```

#### PCAP Review for CUCM - With File

The filter used to troubleshoot the NTP issue in the packet capture is: udp.port == 123. With that filter, you could see that the CUCM publisher established communication with the Google NTP server and that the CUCM publisher communicated with the CUCM subscribers as well.

#### CLI Output Review for CUCM

utils ntp status output

```
NOTE : All nodes will show the current time in UTC regardless of the time zone of the server (listed in UTC time). This makes it easy to compare times on the different CUCM nodes. NOTE : If there is a time difference of 15 minutes or more, it is expected that DB replication will be broken 1) If the publisher is ahead by 15 minutes, this can result in the pub send data to the sub and the sub would have a delay to process the data because it has not yet reached the time in the timestamp of the packets from the publisher (this is expected behavior in this type of situation) 2) If  the subscriber is ahead by 15 minutes, this would result in the subscriber drop the data from the publisher because the subscriber sees it as old data (15 minutes old)
```

```
admin:utils ntp status ntpd (pid 28435) is running...

     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
 203.0.113.0    .GOOG.           1 u   44   64    3   11.724   -0.021   0.064

unsynchronised
   polling server every 8 s

Current time in UTC is : Fri Sep  6 20:54:50 UTC 2019
Current time in America/New_York is : Fri Sep  6 16:54:50 EDT 2019
admin:
```

Read the next information, as it explains the previous output in detail.

```
The very first column contains the " tally code " character. Short overview: 

    * the source you are synchronized to (syspeer)
    # source selected, distance exceeds maximum value
    o the PPS(Pulse Per Second) source if your ntpd (ppspeer, only if you have a PPS capable system and refclock)
    + candidate, i.e. it is considered a good source
    - outlyer, i.e. quality is not good enough
    x falseticker, i.e. this one is considered to distribute bad time
    blank: source discarded, failed sanity 

See the Select field of the Peer status word on the NTP Event Messages and Status Words page for more information on the tally codes. remote the hostname or IP of the remote machine. refid the identification of the time source to which the remote machines is synced. May be (for example) a radio clock or another ntp server) st the stratum of the remote machine. 16 is "unsynchronized". 0 is the best value, that could be (for example) a radio clock or the ntp servers private caesium clock (see http://www.eecis.udel.edu/~mills/ntp/html/index.html#intro for more information about ntp in general). t types available:

        l = local (such as a GPS, WWVB)
        u = unicast (most common)
        m = multicast
        b = broadcast
        - = netaddr when how many seconds since the last poll of the remote machine. poll the polling interval in seconds. reach an 8-bit left-rotating register. Any 1 bit means that a "time packet" was received. The right most bit indicate the status of the last connection with the NTP server. It is Octal number. Use calculator in progammer interface to translate from OCT to BIN: For example 377 translates to 11111111. Each 1 means a successful connection to the NTP server. If you just start a NTP service, and it connects successfully with its server, this number will change as follows (if connectivity is good): 

    00000001 = 001
    00000011 = 003
    00000111 = 007
    00001111 = 017
    00011111 = 037
    00111111 = 077
    01111111 = 177
    11111111 = 377 delay the time delay (in milliseconds) to communicate with the remote. offset the offset (in milliseconds) between our time and that of the remote. jitter the observed jitter (in milliseconds) of time with the remote.
```

Utils diagnose test output

```
admin:utils diagnose test

Log file: platform/log/diag1.log

Starting diagnostic test(s)
===========================
test - disk_space          : Passed (available: 6463 MB, used: 12681 MB)
skip - disk_files          : This module must be run directly and off hours
test - service_manager     : Passed
test - tomcat              : Passed
test - tomcat_deadlocks    : Passed
test - tomcat_keystore     : Passed
test - tomcat_connectors   : Passed
test - tomcat_threads      : Passed
test - tomcat_memory       : Passed
test - tomcat_sessions     : Passed
skip - tomcat_heapdump     : This module must be run directly and off hours
test - validate_network    : Passed
test - raid                : Passed
test - system_info         : Passed (Collected system information in diagnostic log)
test - ntp_reachability    : Passed
test - ntp_clock_drift     : Passed
test - ntp_stratum         : Passed
skip - sdl_fragmentation   : This module must be run directly and off hours
skip - sdi_fragmentation   : This module must be run directly and off hours

Diagnostics Completed

 The final output will be in Log file: platform/log/diag1.log

 Please use 'file view activelog platform/log/diag1.log' command to see the output

admin:
```

If NTP fails in the utils diagnose test output, you would see something similar to this:

```
admin:utils diagnose test

Log file: platform/log/diag1.log

Starting diagnostic test(s)
===========================
test - disk_space          : Passed (available: 6463 MB, used: 12681 MB)
skip - disk_files          : This module must be run directly and off hours
test - service_manager     : Passed
test - tomcat              : Passed
test - tomcat_deadlocks    : Passed
test - tomcat_keystore     : Passed
test - tomcat_connectors   : Passed
test - tomcat_threads      : Passed
test - tomcat_memory       : Passed
test - tomcat_sessions     : Passed
skip - tomcat_heapdump     : This module must be run directly and off hours
test - validate_network    : Passed
test - raid                : Passed
test - system_info         : Passed (Collected system information in diagnostic log) test - ntp_reachability    : Warning The NTP service is restarting, it can take about 5 minutes. test - ntp_clock_drift     : Warning The local clock is not synchronised.
None of the designated NTP servers are reachable/functioning or legitimate. test - ntp_stratum         : Warning The local clock is not synchronised.
None of the designated NTP servers are reachable/functioning or legitimate.

skip - sdl_fragmentation   : This module must be run directly and off hours
```

Confirm NTP was good at the time of install. Run the command:

run sql select pkid,name,dbinfo('utc_to_datetime', cdrtime) as CDRTIME  from device where cdrtime > getCurrTime()

This command compares the current time to the cdrtime (when the table was modified). If you used a bad NTP in the install/upgrade and then corrected the NTP, the database goes out of sync every time a change is made. This issue would not be seen when you run the typical NTP commands (for example, utils ntp status ) because you have moved away from the bad NTP source to a good one.

It would be good that you moved away from the bad NTP to a good one; however, a movement to a good NTP source would not fix the tables that were created while the install/upgrade.

When you run this command, the expected output is this:

```
admin:run sql select pkid,name,dbinfo('utc_to_datetime', cdrtime) as CDRTIME  from device where cdrtime > getCurrTime()

pkid name cdrtime

==== ==== =======

admin:
```

If you have a similar output to the next one, it is a sign that the NTP used for the install/upgrade has not been used, and has caused problems that affect the database replication:

```
admin:run sql select pkid,name,dbinfo('utc_to_datetime', cdrtime) as CDRTIME from device where cdrtime > getCurrTime()

pkid                                    name          cdrtime

=============================           =====         =====================

bf80dd31-9911-43ce-81fd-a99ec0333fb5    MTP_2         2016-09-11 14:38:14.0
4c38fc05-760d-4afb-96e8-69333c195e74    CFB_2         2016-09-11 14:38:14.0
90878c80-e213-4c7e-82b9-6c780aac72f3    ANN_2         2016-09-11 14:38:14.0
08b5bff4-da94-4dfb-88af-ea9ffa96872c    MOH_2         2016-09-11 14:38:14.0
93320e4d-1b73-4099-9a7c-c4cddfadb5d9    MTP_3         2016-09-11 14:38:14.0
a6850d42-5f0a-49ce-9fa3-80d45b800e23    CFB_3         2016-09-11 14:38:14.0
9963c9cb-58b0-4191-93e1-8676584f6461    ANN_3         2016-09-11 14:38:14.0
def79fb7-c801-4fb3-85fb-4e94310bf0bd    MOH_3         2016-09-11 14:38:14.0
4cd64584-089b-4331-9291-79774330cbc     2 MTP_4       2016-09-11 14:38:14.0
27b18882-db83-4d14-8bce-d3f8dc439610    CFB_4         2016-09-11 14:38:14.0
a40da882-e04f-4649-b2eb-2f79d1289e81    ANN_4         2016-09-11 14:38:14.0
36575ff4-cdea-4945-87e7-638cc555463e    MOH_4         2016-09-11 14:38:14.0
```

### Further Considerations

1) If you upgrade the ESXi hosts without the VM hardware considerations into account, you can experience NTP issues.

2) Ensure that the ESXi version is in compliance with the virtualization matrix. 3) Ensure that the ESXi version and hardware version are compatible.

## Related Information

### Revision History

4.0

22-Nov-2023

Updated Introduction, Alt Text, and Formatting to meet current Cisco guidelines.

3.0

18-Oct-2022

Updated potential PII, and search engine optimization.

2.0

15-Mar-2022

Grammar updates.

1.0

20-May-2020

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 4.0 | 22-Nov-2023 | Updated Introduction, Alt Text, and Formatting to meet current Cisco guidelines. |
| 3.0 | 18-Oct-2022 | Updated potential PII, and search engine optimization. |
| 2.0 | 15-Mar-2022 | Grammar updates. |
| 1.0 | 20-May-2020 | Initial Release |