---
doc_id: www-cisco-com-c-en-us-support-docs-customer-collaboration-unified-intelligence-center-201003-collecting-the-logs-for-cui-a260cf891f
source_url: https://www.cisco.com/c/en/us/support/docs/customer-collaboration/unified-intelligence-center/201003-Collecting-the-Logs-for-CUIC-Performance.html
retrieved_at: 2026-08-16T19:24:31.609514+00:00
---

Collecting the Logs for CUIC Performance Issues

# Collecting the Logs for CUIC Performance Issues

### Download Options

Updated: March 11, 2017

Document ID: 201003

Contents

## Contents

## Introduction

This document describes a process of configuring and collecting Cisco Unified Intelligence Center (CUIC) logs when troubleshooting reporting performance issues. Troubleshooting CUIC performance issues could be challenging due to a lot of technologies, products and components involved. Also performance issues manifest themselfs in different ways, so it is important to have a clear picture during the troubleshooting.

The intent of this document is not to describe the troubleshooting process in a great detail, but to highlight the main points when collecting the logs required by Cisco TAC or Cisco Engineering.

## Collecting the Logs for CUIC Performance Issues

### General Guidelines

Collecting all logs in one take is challenging and time consuming. The whole procedure should take from 1 to 4 hours. It depends on how well a customer or a partner will prepare the environment.

Note : There is no downtime required for this activity although a customer may need to submit some change requests.

It is highly recommended to do the tests using Firefox browser specifically due to more comprehensive developer tools (F12).

You need to know ip addresses that CUIC client and server are using for communication.

These ip addresses are used for CUIC client and the server in this article.

Client IP Address: 10.111.16.157

Server IP Address: 10.222.6.29

Tip : For CUIC performance troubleshooting it is highly recommended to reproduce the problem using a client located in UCCE LAN environment. This will eliminate the impact of network connection between CUIC client and the server.

There may be multiple log collection attempts thus it is important to maintain clear naming of the files collected. Create a folder on your client's desktop with a name like tac<date>_<time> (eg. tac27feb17_1334) or tac_<date>_<attempt> (eg. tac27feb17_take3). After collecting the logs, put all of them into this folder, archive it and attach it to the case.

Try to find a node in the cluster that performs the best from perspective of CPU, memory, ioWait stats and still has performance issues. Make tests with this node directly avoiding load balancer (if any).

### Typical Set of Logs

- Client Browser F12 logs

- Client HTTP packet capture

- Server HTTP packet capture

- Intelligence Center Reporting Service

- Cisco Informix Database Service

- Cisco RIS Data Collector PerfMonLog

- Cisco Tomcat

- Event Viewer-Application Log

- Event Viewer-System Log

- Packet Capture Logs

### Define a Problem

#### Example 1. Error or Timeout

During peak hours CUIC reporting users on all nodes in the cluster notice several errors for real-time reports.

E1: "Retrieving dataset information java.lang.IllegalStateException"

E2: "Last refresh timed out(getDataSetMaxReached), click refresh to reload."

E3: "Last refresh timed out(reportRefreshRetry). Please wait for next automatic refresh or click 'Refresh'."

The problem started on February 27th in the morning after these specific changes in network, security and data center implemented on weekend. We have verified these sizing guidelines for our CUIC cluster.

Cisco Unified Intelligence Center Solution Reference Network Design (SRND), Release 11.0(1)

#### Example 2. Big Delay

Constantly CUIC reporting users only on the first subscriber node are experiencing delays of 30-40 seconds when displaying real-time reports.

The problem started on February 26th after upgrading firmware of our SAN network devices. We have verified these sizing guidelines for our CUIC cluster.

Cisco Unified Intelligence Center Solution Reference Network Design (SRND), Release 11.0(1)

### Resources Provided by Customer

Here is the summary of tools/applications that customers or partners need to use when collecting the logs for CUIC performance issues.

- Client: Windows Command Prompt (CMD)

- Client: Wireshark

- Client: Firefox browser

- Client: Real-Time Monitoring Tool (RTMT) or a Secure File Transfer Protocol (SFTP) server

- CUIC server command line (CLI)

Note : In some cases it may be complicated to collect CUIC logs using RTMT. So you need to download the logs from CUIC CLI to an SFTP server.

### Preparing the Reproduction

#### 1. Client Interface Name and Address

Use CMD to collect all CUIC client ip addresses.

Find out network interface and ip address that is used to communicate with CUIC server. You need to use it when collecting a packet capture from a server side.

```
C:\Users\Administrator> route print -4 | findstr 222 10.222.6.0    255.255.254.0         On-link 10.111.16.157 1
```

Determine correct interface name that later need to be selected in Wireshark with this command. The interface name and its ip address are in italic.

```
c:\tmp> ipconfig Windows IP Configuration Wireless LAN adapter wifi0 : IPv4 Address. . . . . . . . . . . : 10.111.16.157 Ethernet adapter Local Area Connection 2: IPv4 Address. . . . . . . . . . . : 192.168.123.1 <output omited for brevity>
```

#### 2. Client HTTP Packet Capture

Ensure the Wireshark application is installed and working fine. Select the correct interface determined in the previous step, but for now stop the packet capture.

Tip : If no interfaces are discovered in Wireshark a common solution to that is to reinstall Pcap software that is bundled with Wireshark.

#### 3. Client Browser F12 Logs

3.1 Open Firefox browser and verify its version. It has to be a supported one.

Press F12 and navigate to Network ( Network Monitor , CTRL+Shift+Q) tab. Select All (or HTML , JS , XHR , Media , Flash , WS , Other ).

#### 4. Server RTMT Logs

Log in to CUIC with RTMT and select these services on all nodes

- Intelligence Center Reporting Service

- Cisco Informix Database Service

- Cisco RIS Data Collector PerfMonLog

- Cisco Tomcat

- Event Viewer-Application Log

- Event Viewer-System Log

- Packet Capture Logs

Select Absolute Range or Relative Range and provide a meaningful name for the folder with these logs.

#### 5. Server HTTP Packet Capture

In order to simplify the troubleshooting process there need to be a simple way of tracking single query from client to server. By default HTTPS encrypted transport is used which does not reveal such details. That is why HTTP should be enabled temporarily for the time of issue reproduction.

To enable HTTP communication type this command in CUIC CLI. It should be enabled on the node that is used for the test.

```
admin: set cuic properties http-enabled on Value has been successfully set admin: show cuic properties http-enabled http_enabled ============ on
```

Note : You don't need to restart Cisco Tomcat service. The only impact is an unencrypted communication between CUIC client and server.

Start a packet capture with Wireshark on CUIC client.

Start a packet capture with this command on CUIC server node. Ensure that correct ip address of the client is specified.

```
admin: utils network capture file packetcapture count 100000 size all host ip 10.111.16.157 Executing command with options: size=ALL count=100000 interface=eth0 src=dest= port= ip=10.111.16.157
```

#### 6 . Session Recording

It is highly recommended to include along with the logs a screen video recording of the reproduction to show CUIC user experience especially when dealing with report display timeouts and delays.

Any screen recording software can be used. Cisco Webex recording feature also provides such fuctionality.

### Reproducing the Problem

Try to reproduce the problem with least amount of steps performed. Try to avoid doing uncessary tasks during the reproduction. This will greatly speed-up the log analysis done by Cisco TAC.

An example of a very simple test would be to login to CUIC Main Administration page -> Security -> User List (or User Groups , or User Permissions ).

If the above test will not show the delay after several attempts a customer may try to reproduce the issue by running a report or dashboard. In that case it is very important to write down the report or dashboard name.

During the reproduction test click on Windows Clock and open Change date and time settings ... at the right bottom. It is required to monitor the time precicely to the seconds.

Log all actions taken. It is helpful to have some gaps in time between the actions. You can use this example.

14:16:30 - typed CUIC address in Firefox browser

14:17:42 - pressed Enter after typing the credentials

14:20:20 - the system loaded the Main.htmx web page

14:21:02 - clicked User List and CUIC started loading it

14:28:15 - User List was loaded successfully (with delay of 7m 10s)

Have a notepad opened and copy the template above. Then, ideally, just replace the time or step description if needed.

### Collecting the Logs After Reproduction

#### 1. Collect Client HTTP Packet Capture

Stop the packet capture on the client (Wireshark).

Stop the packet capture on the CUIC node by pressing CTRL+C .

In Wireshark save client packet capture and move it to the TAC folder.

#### 2. Collect Client Browser F12 Logs

Right click on any request and press Save All As HAR . Then select TAC folder location and and click Save .

This type of file can be analysed with G Suite HAR Analyser tool.

This example shows that the cause of report delays is a low network bandwidth between CUIC client and server.

#### 3. Collect Server RTMT Logs

Ensure that CUIC server packet capture is already stopped. If not then press CTRL+C in CLI session.

Navigate to CUIC RTMT that was pre setup before and press Finish .

Note : If using RTMT, ensure all untrusted certificate prompts are accepted.

If RTMT log collection process is slow, there is an option to download log files to an SFTP server.

Use these commands to collect the necessary logs to an SFTP server.

```
file get activelog /cuic/logs/cuic/* reltime hours 1 file get activelog /cuic/logs/cuicsrvr/* reltime hours 1 file get activelog /cm/log/informix/* reltime hours 1 file get activelog /cm/log/ris/csv/PerfMon* reltime hours 1 file get activelog /syslog/CiscoSyslog* reltime days 1 file get activelog /syslog/AlternateSyslog* reltime days 1 file get activelog /syslog/messages* reltime days 1 file get activelog /cuic/logs/cuic/* reltime hours 1 file get activelog /cuic/logs/cuic/* reltime hours 1 file get activelog /tomcat/logs/localhost_access*.txt reltime hours 1 file get activelog /platform/cli/*.cap reltime hours 1
```

Along with the logs provide these CUIC CLI outputs taken from the test node.

```
show status show tech network hosts utils ntp status utils service list utils dbreplication runtimestate file list activelog /core/ file dump install system-history.log show process using-most cpu show process using-most memory run sql SELECT COUNT(*) FROM cuic_data:cuicuser show perf query counter ReportingEngineInfo ReportsUsersLoggedin
```

#### 4. Capture Session Recording

Stop and add the screen recording to the TAC folder.

### Revert the Changes

Disable HTTP communication on CUIC node.

```
admin: set cuic properties http-enabled off Value has been successfully set admin: show cuic properties http-enabled http_enabled ============ off
```

### Contributed by Cisco Engineers

Alexander Levichev

Cisco TAC Engineer

### Customers Also Viewed

- Configuring of Standalone CUIC with UCCX 12.5

### This Document Applies to These Products

- Unified Intelligence Center