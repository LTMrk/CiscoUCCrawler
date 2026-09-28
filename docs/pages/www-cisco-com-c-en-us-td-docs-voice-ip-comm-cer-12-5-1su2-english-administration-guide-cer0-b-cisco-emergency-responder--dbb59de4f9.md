---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1su2-english-administration-guide-cer0-b-cisco-emergency-responder--dbb59de4f9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1su2/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-1251SU2/cer0_b_cisco-emergency-responder-administration-guide-1251su3_appendix_010111.html
retrieved_at: 2026-08-21T15:49:43.836177+00:00
---

Cisco Emergency Responder Administration Guide for Release 12.5(1)SU2

# Cisco Emergency Responder Administration Guide for Release 12.5(1)SU2

Updated: November 23, 2021

Chapter: Cisco Emergency Responder Port Usage

## Chapter: Cisco Emergency Responder Port Usage

- Cisco Emergency Responder Port Usage

# Cisco Emergency Responder Port Usage

Cisco
                           		  Emergency Responder (Emergency Responder) uses the following ports:

Protocol

TCP
                                       					 /UDP

Port
                                       					 Range

For
                                       					 this protocol, app or box is: <Client, Server, or Peer>

What is other end?

Relevance to Product

What it does

CTI

UDP

16384 to 32767

Used for communication between Emergency Responder and Unified Communications Manager.

CTI

TCP

2748

Used for Emergency Responder JTAPI connections to Unified Communications Manager for CTI route points and CTI ports

CTI

TCP

2749

Used for Emergency Responder Secure JTAPI connections to Unified Communications Manager for CTI route points and CTI ports.

SNMP

UDP

161

Provides services for SNMP-based management app.

SNMP

UDP

6161

Native SNMP agent listens for requests forwarded by SNMP master
                                       					 agents.

TCP

TCP

7161

Used for communication between SNMP master agent and subagents.

TCP

TCP

1500

IDS
                                       					 DB

TCP

TCP

1501

IDS
                                       					 DB

XML

TCP

1515

IDS DB

Proprietary

TCP

8500

IPsec Cluster Manager

N/A

TCP

22

sshd

Secure File Transfer Protocol

TCP

TCP

22

sshd

SSH port for remote access

N/A

UDP

123

NTP port used on Unified Communications Manager server

N/A

UDP

546

DHCPv6 Client

N/A

UDP

6666

netdump

Port should be open for systems running the netdump server

HTTPS

TCP

443

HTTPS

N/A

TCP

9443

haproxy

Searches authenticated contacts

N/A

UDP

500

Internet Security Association and Key Management Protocol

N/A

UDP

514

System Logging Service

Proprietary

TCP

2444

Used by CTL Client to communicate with CTL Provider to set the
                                       					 cluster security mode and manage the CTL file

TCP

TCP

3804

Certificate Authority Proxy Function (CAPF) Port for listening
                                       					 to incoming requests from endpoints

XML

TCP

5555

License Manager listens for license requests on this port

TCP

TCP

7070

Certificate Manager Daemon

TCP

TCP

7999

Cellular Digital Packet Data Protocol

HTTPS

TCP

50000-50004

HTTPS to HP SIM

N/A

UDP

67 and 68

DHCP port used on Unified CM server

N/A

UDP

ephemeral

Package Management Tool

N/A

UDP

ephemeral

DNS

N/A

TCP

32768:61000

Generic Ephemeral port

N/A

UDP

32768:61000

Generic Ephemeral port

N/A

IP

GRE: IP 47, ESP: IP 50, AH: IP 51, IPSec: UDP 500.

IPsec configuration

SMTP

TCP

25

client

SMTP Mail Server(*)

core

Send e-pages, e-mail notifications

CDP

client

core

Discovery of CDP-enabled phones

CLM

TCP

8500

server

clm

core

cluster manager

CLM

UDP

8500

server

clm

core

cluster manager

SYSLOGD

UDP

514

server

syslog server

optional

event syslog port for 514

SYSLOGD

TCP

601

server

syslog server

optional

audit syslog port for 601

SYSLOG

UDP

8888

client

syslog client

optional

syslog port

HTTPS

TCP

8443

server

Browser

core

secure web access (Tomcat)

HTTP

TCP

8080

server

Browser

core

web access (Tomcat)

HTTP

TCP

80

server

Browser

core

web access (Tomcat)

NTPD

UDP

123

client

NTP server

optional

network time sync

Peer TCP

TCP

17001

peer

Emergency Responder Server

core

Emergency Responder Primary Backup Failover

Peer RMI

TCP

7777

server

Emergency Responder Server

core

Emergency Responder Server RMI ports

Peer RMI

TCP

7778

server

Emergency Responder Admin

core

Emergency Responder Admin RMI ports

Applet

TCP

55000

server

Applets

core

Web alert

SNMP

UDP

162

server

SNMP Agents

optional

Network Management

DBLRPC

TCP

1515

server

dblrpc

core

Db replication port

RACOON

ESP

client

Emergency Responder Server

optional

IPsec traffic

RACOON

UDP

500

client

Emergency Responder Server

optional

IPsec setup port

IDS

TCP

1500

server

IDS

Informix database server

TCP

TCP

1099

AMC

AMC RMI Registry port

TCP

TCP

1090

AMC

AMC RMI Object port

TCP

TCP

4040

CiscoDRFMaster

DRS Master Agent port

| Protocol | TCP
                                       					 /UDP | Port
                                       					 Range | For
                                       					 this protocol, app or box is: <Client, Server, or Peer> | What is other end? | Relevance to Product | What it does |
|---|---|---|---|---|---|---|
| CTI | UDP | 16384 to 32767 |  |  |  | Used for communication between Emergency Responder and Unified Communications Manager. |
| CTI | TCP | 2748 |  |  |  | Used for Emergency Responder JTAPI connections to Unified Communications Manager for CTI route points and CTI ports |
| CTI | TCP | 2749 |  |  |  | Used for Emergency Responder Secure JTAPI connections to Unified Communications Manager for CTI route points and CTI ports. |
| SNMP | UDP | 161 |  |  |  | Provides services for SNMP-based management app. |
| SNMP | UDP | 6161 |  |  |  | Native SNMP agent listens for requests forwarded by SNMP master
                                       					 agents. |
| TCP | TCP | 7161 |  |  |  | Used for communication between SNMP master agent and subagents. |
| TCP | TCP | 1500 |  |  |  | IDS
                                       					 DB |
| TCP | TCP | 1501 |  |  |  | IDS
                                       					 DB |
| XML | TCP | 1515 |  |  |  | IDS DB |
| Proprietary | TCP | 8500 |  |  |  | IPsec Cluster Manager |
| N/A | TCP | 22 |  |  | sshd | Secure File Transfer Protocol |
| TCP | TCP | 22 |  |  | sshd | SSH port for remote access |
| N/A | UDP | 123 |  |  |  | NTP port used on Unified Communications Manager server |
| N/A | UDP | 546 |  |  |  | DHCPv6 Client |
| N/A | UDP | 6666 |  |  | netdump | Port should be open for systems running the netdump server |
| HTTPS | TCP | 443 |  |  |  | HTTPS |
| N/A | TCP | 9443 |  |  | haproxy | Searches authenticated contacts |
| N/A | UDP | 500 |  |  |  | Internet Security Association and Key Management Protocol |
| N/A | UDP | 514 |  |  |  | System Logging Service |
| Proprietary | TCP | 2444 |  |  |  | Used by CTL Client to communicate with CTL Provider to set the
                                       					 cluster security mode and manage the CTL file |
| TCP | TCP | 3804 |  |  |  | Certificate Authority Proxy Function (CAPF) Port for listening
                                       					 to incoming requests from endpoints |
| XML | TCP | 5555 |  |  |  | License Manager listens for license requests on this port |
| TCP | TCP | 7070 |  |  |  | Certificate Manager Daemon |
| TCP | TCP | 7999 |  |  |  | Cellular Digital Packet Data Protocol |
| HTTPS | TCP | 50000-50004 |  |  |  | HTTPS to HP SIM |
| N/A | UDP | 67 and 68 |  |  |  | DHCP port used on Unified CM server |
| N/A | UDP | ephemeral |  |  |  | Package Management Tool |
| N/A | UDP | ephemeral |  |  |  | DNS |
| N/A | TCP | 32768:61000 |  |  |  | Generic Ephemeral port |
| N/A | UDP | 32768:61000 |  |  |  | Generic Ephemeral port |
| N/A | IP | GRE: IP 47, ESP: IP 50, AH: IP 51, IPSec: UDP 500. |  |  |  | IPsec configuration |
| SMTP | TCP | 25 | client | SMTP Mail Server(*) | core | Send e-pages, e-mail notifications |
| CDP |  |  | client |  | core | Discovery of CDP-enabled phones |
| CLM | TCP | 8500 | server | clm | core | cluster manager |
| CLM | UDP | 8500 | server | clm | core | cluster manager |
| SYSLOGD | UDP | 514 | server | syslog server | optional | event syslog port for 514 |
| SYSLOGD | TCP | 601 | server | syslog server | optional | audit syslog port for 601 |
| SYSLOG | UDP | 8888 | client | syslog client | optional | syslog port |
| HTTPS | TCP | 8443 | server | Browser | core | secure web access (Tomcat) |
| HTTP | TCP | 8080 | server | Browser | core | web access (Tomcat) |
| HTTP | TCP | 80 | server | Browser | core | web access (Tomcat) |
| NTPD | UDP | 123 | client | NTP server | optional | network time sync |
| Peer TCP | TCP | 17001 | peer | Emergency Responder Server | core | Emergency Responder Primary Backup Failover |
| Peer RMI | TCP | 7777 | server | Emergency Responder Server | core | Emergency Responder Server RMI ports |
| Peer RMI | TCP | 7778 | server | Emergency Responder Admin | core | Emergency Responder Admin RMI ports |
| Applet | TCP | 55000 | server | Applets | core | Web alert |
| SNMP | UDP | 162 | server | SNMP Agents | optional | Network Management |
| DBLRPC | TCP | 1515 | server | dblrpc | core | Db replication port |
| RACOON | ESP |  | client | Emergency Responder Server | optional | IPsec traffic |
| RACOON | UDP | 500 | client | Emergency Responder Server | optional | IPsec setup port |
| IDS | TCP | 1500 | server | IDS |  | Informix database server |
| TCP | TCP | 1099 |  |  | AMC | AMC RMI Registry port |
| TCP | TCP | 1090 |  |  | AMC | AMC RMI Object port |
| TCP | TCP | 4040 |  |  | CiscoDRFMaster | DRS Master Agent port |