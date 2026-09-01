---
doc_id: sec-cloudapps-cisco-com-security-center-resources-forensic-guides-ios-xr-forensic-investigation-html-dc18df55c8
source_url: https://sec.cloudapps.cisco.com/security/center/resources/forensic_guides/ios_xr_forensic_investigation.html
retrieved_at: 2026-09-01T14:10:54.152447+00:00
---

Home / Cisco Security

Cisco IOS XR Software Forensic Data Collection Procedures

# Cisco IOS XR Software Forensic Data Collection Procedures

Introduction

Prerequisites

Step One - Cisco IOS XR Device Problem Description

Step Two - Document the Cisco IOS XR Run-Time Environment

Step Three - Execute the Cisco IOS XR Forensic Data Collection Script

Step Four - Obtaining a Core File

Related Documentation

Cisco IOS XR Device Forensic Report Checklist

Appendix A - Manual Process Enumeration and Examination

Step A1 – Cisco IOS XR Process Enumeration

Step A2 – Cisco IOS XR Process Examination

Step A3 – Container Enumeration

Revision History

## Introduction

This document provides guidance for collecting evidence from Cisco IOS XR devices that are suspected of compromise or tampering. It outlines a number of commands that can be run to gather evidence for an investigation along with the respective output that should be collected upon running these commands. This document also provides information on how to enumerate critical processes and identify unusual run-time characteristics of these processes.

Note: It is extremely important when triaging a network device for compromise or tampering that it is not rebooted. Rebooting a device during an initial assessment will irrecoverably lose all volatile information contained within the device (e.g., RAM contents, arp & routing tables, NAT translations, ACL hit & drop counts, etc.).

Note: It is highly recommended that a device suspected of tampering or compromise be isolated from the network prior to conducting an initial forensic examination. This may prevent remote unloading of any implants or malware installed on the device and will prevent an adversary from monitoring commands entered on the device under investigation.

If you require assistance or have questions regarding the procedures below, please contact the Cisco Product Security Incident Response Team (PSIRT) .

This document contains four main sections:

1.      Cisco IOS XR Device Problem Description – Describe why the platform is a candidate for forensic examination.

2.      Cisco IOS XR Run-Time Environment – Collect platform configuration and run-time state.

3.      Cisco IOS XR Process Enumeration and Examination – Leverage a script to automate the collection of critical processes and their allocated memory characteristics.

4.      Memory/Core Export – Collect a core dump and process information from any processes that are displaying inappropriate run-time attributes.

## Prerequisites

The procedures that are outlined in this document assume that the reader has a basic understanding of Cisco IOS XR Software and Linux shell command syntax.

A valid cisco.com account is required to view individual Cisco IOS XR file hashes for software file integrity checking, or a publicly available comprehensive list of file hashes (Bulk Hash File) can be downloaded from https://www.cisco.com/c/en/us/about/trust-center/downloads.html .

The Cisco IOS XR Forensic Data Collection shell script can be downloaded from https://sec.cloudapps.cisco.com/security/center/resources/ios_xr_forensic_script.html .

A Cisco Technical Assistance Center (TAC) service request (SR) for the device in question is required because these procedures assume that the information gathered in each step will be uploaded to a TAC SR.

Note: The examples that are used in this document are based on Cisco IOS XR Software Release 25.3.1 command syntax. The output that is produced by a command may vary depending on the software release that is deployed and/or the features that are supported or configured on the device. Not all commands that are used in these procedures may be supported on earlier releases of the software.

## Step One – Cisco IOS XR Device Problem Description

Describe in as much detail as possible WHY the device is a candidate for forensic examination. Are there configuration changes that cannot be explained? Is there unusual traffic originating from or terminating on the device? Are there anomalous entries in the device logs or in syslog messages? Is the device exhibiting odd behavior that cannot be attributed to a misconfiguration or a software/hardware defect? Are there any typical device administration commands that are now returning unusual output or no output at all?

Submit the problem description collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Two – Document the Cisco IOS XR Run-Time Environment

The initial stage of evidence gathering is completed by issuing a number of show and dir commands, and the output produced may vary dependent on the particular Cisco IOS XR hardware platform, software release, and/or configured features.

Execute each of the following commands and record the output:

```
terminal length 0
# system-level commands
show tech-support
show version
show tcp brief
show udp brief
show install active summary
show sdr detail
admin show platform
show redundancy
show logging
show placement
show running-config
show filesystem
show ip int brief
# modify the target of dir commands as needed. Note the rootfs partition may only
# be accessible from the CLI on older versions of the software
dir /recurse apphost:
dir /recurse config:
dir /recurse disk0:
dir /recurse harddisk:
dir /recurse rootfs:
show history detail
show history run-mode console
show history run-mode vty
show history run-mode aux
# CPU and process-level commands
show processes all
show processes startup
show processes aborts
show process memory
# platform integrity commands
show platform security integrity log secure-boot status
show platform security integrity dossier include packages reboot-history /
rollback-history system-integrity-snapshot filesystem-inventory /
system-inventory nonce 1580 | utility sign nonce 1580 include-certificate
```

Submit all command output and any system log files that were collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step Three – Execute the Cisco IOS XR Forensic Data Collection Script

Note: The steps and commands that are outlined in this and subsequent sections are intended for Cisco IOS XR Software that is running on 64-bit versions of the Linux operating system. To determine which operating system is in use by Cisco IOS XR Software, execute the following command:

```
run uname -s
```

An example of this procedures follows:

```
RP/0/RP0/CPU0:ios# run uname -s Tue Aug 27 14:07:10.165 UTC Linux
```

If the uname command returns a value of Linux , proceed with the steps that are outlined in this document. Alternatively, if the uname command returns a value of QNX , contact the Cisco Technical Assistance Center (TAC) for further assistance.

Note: The remainder of this section provides instructions on how to download and execute a Linux bash script, which automates the collection of forensic information from platforms that are running Cisco IOS XR Software. See Appendix A – Manual Process Enumeration and Examination at the end of this document for the steps needed to execute this process manually instead of running the script.

The required steps in this section are:

- Download the Cisco IOS XR Forensic Data Collection shell script from the Cisco Security Center.

- Download the script to the platform to be examined.

- Execute the Bash shell.

- Calculate a hash of the script and compare it to the value that is noted on the download page.

- Execute the script.

- Calculate a hash value for the compressed tar archive.

- Copy the compressed tar archive off the platform.

An example of this entire procedure follows:

```
RP/0/RP0/CPU0:ios# copy ftp:iosxr_fdc.sh harddisk: Wed Oct  8 13:27:10.191 UTC
Address or name of remote host [10.1.1.1]?
Source username: [anonymous]?
Source password: [anonymous@ios]?
Destination filename [/harddisk:/iosxr_fdc.sh]?
Accessing ftp://anonymous:*@10.1.1.1/iosxr_fdc.sh
C
13276 bytes copied in      1 sec 
Copy operation success

RP/0/RP0/CPU0:ios# run bash Wed Oct  8 13:28:29.843 UTC
[xr-vm_node0_RP0_CPU0:~]$ cd /harddisk\: [xr-vm_node0_RP0_CPU0:/harddisk:]$ md5sum iosxr_fdc.sh 93d38f4874e90f723bace0965e929458  iosxr_fdc.sh

[xr-vm_node0_RP0_CPU0:/harddisk:]$ bash iosxr_fdc.sh -p /harddisk\: Using /harddisk: as the primary destination
Running IOS-XR forensic data collection script for device: ios
Collection initiated on: Wed Oct  8 13:32:05 UTC 2025
Script executed as: uid=0(root) gid=0(root) groups=0(root)

=== Collecting system information ===

Kernel information: Linux xr-vm_node0_RP0_CPU0 6.6.69-yocto-standard #1 SMP Wed Aug 20 19:25:30 UTC 2025 x86_64 GNU/Linux

Version and build information:

Cisco IOS XR Software, Version 25.3.1
Copyright (c) 2013-2025 by Cisco Systems, Inc.

Build Information:
 Built By     : swtools
 Built On     : Mon Sep 15 06:59:11 PDT 2025
 Built Host   : iox-ucs-1004
 Workspace    : /auto/srcarchive12/prod/25.3.1/xrv9k/ws
 Version      : 25.3.1
 Location     : /opt/cisco/XR/packages/
 Label        : 25.3.1

cisco IOS-XRv 9000 () processor
System uptime is 23 hours 43 minutes

Platform system database:

Node              Type                       State             Config state
---------------------------------------------------------------------------
0/0/CPU0          R-IOSXRV9000-LC-C          IOS XR RUN        NSHUT
0/RP0/CPU0        R-IOSXRV9000-RP-C(Active)  IOS XR RUN        NSHUT

*** Executing netstat and iptables commands for each vrf ***
   --> Listing all sockets under namespace xrnns
   --> Listing iptables rules for namespace xrnns

   --> Listing all sockets under namespace tpnns
   --> Listing iptables rules for namespace tpnns

   --> Listing all sockets under namespace vrf-default
   --> Listing iptables rules for namespace vrf-default

   --> Listing all sockets under namespace global-vrf
   --> Listing iptables rules for namespace global-vrf

Done!

*** Collecting meminfo information ***
Done!

*** Collecting process list ***
Done!

*** Listing currently loaded kernel modules ***
Done!

*** Collecting smaps for each process ***
smaps for all processes written to /harddisk:/all-process-smaps.gz

*** Hashing running binaries ***
Done!

*** Searching for running processes with deleted binaries ***
Done!

*** Checking for virtual devices ***
Done!

*** Listing /dev/shm directory contents ***
Done!

*** Collecting package manager data ***
YUM and DNF are not installed - skipping check.

   --> Collecting RPM package manager data
Done!

*** Collecting any bash_history files ***
Done!

*** Collecting Docker information ***
Docker daemon is not running - skipping check
=== End of system information collection ===

*** Checking critical processes ***
*** Results of this check will be written to critical-process-maps.txt ***

   --> Collecting process names from netio_show
   --> Collecting process names from packet_show
   --> Collecting PIDs for each process
   --> Checking for executable memory regions and collecting memory  
	 information

Executing show memory for process: dumper (PID:2094)
Collecting memory maps for process: dumper (PID:2094)

Executing show memory for process: netio_main (PID:3000)
Collecting memory maps for process: netio_main (PID:3000)

[output omitted]

Executing show memory for process: vservice_mgr (PID:5955)
Collecting memory maps for process: vservice_mgr (PID:5955)

Executing show memory for process: l2vpn_mgr_main (PID:5899)
Collecting memory maps for process: l2vpn_mgr_main (PID:5899)

Printing dumpcore commands for affected processes

Archiving all files to: /harddisk:/ios.tar.gz
/harddisk:/all-process-smaps.gz
/harddisk:/iosxr_fdc.txt
/harddisk:/critical-process-maps.txt
Done!

[xr-vm_node0_RP0_CPU0:/harddisk:]$ md5sum ios.tar.gz 10220a6031ad00633e8a8e84d63539b5  ios.tar.gz

[xr-vm_node0_RP0_CPU0:/harddisk:]$ exit logout

RP/0/RP0/CPU0:ios# cd harddisk: RP/0/RP0/CPU0:ios# copy ios.tar.gz ftp: Wed Oct  8 13:37:37.913 UTC
Address or name of remote host [10.1.1.1]?
Destination username: [anonymous]?
Destination password: [anonymous@ios]?
Destination filename [ios.tar.gz]?
Writing ftp://anonymous:*@10.1.1.1/ios.tar.gz
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
9402388 bytes copied in      4 sec (  2350597)bytes/sec
Copy operation success

RP/0/RP0/CPU0:ios#
```

Once the compressed tar archive has been copied off the platform, search the iosxr_fdc.txt text file for the string suspicious to identify processes which have the read, write, and execute attributes set. If there are no processes marked as suspicious, Step 4 may be omitted. If there are processes marked as suspicious, proceed to the next step to obtain core files for these processes.

An example of suspicious process detection follows:

```
# grep suspicious iosxr_fdc.txt Found RWX maps for ether_sock (suspicious)
Found RWX maps for tcp (suspicious)
```

Submit all of the command and script output that was obtained in this step to the relevant TAC SR, and proceed to the next section of this document.

## Step Four – Obtaining a Core File

If any of the process memory maps that were examined in the previous section displayed inappropriate attributes (read, write, or execute), a core file should be obtained so that further investigation and analysis can be conducted. This can be accomplished by executing the following command:

```
dumpcore running <process_name> verbose
```

For example, if the netio process contained a memory map with the rwx bits set, a core dump can be obtained by executing the commands as shown in the following example:

```
RP/0/RP0/CPU0:ios# dumpcore running netio verbose Tue Aug 27 18:40:00.733 UTC Dump core success
```

The dumpcore command will create two files, (1) a core file with a .gz extension and (2) additional debugging and diagnostic information in a file with a .txt extension. A copy of the text file will be placed in the disk0:/core directory, and the g-zipped core file is typicall written to the /misc/disk1 directory in the underlying Linux filesystem.

The following example illustrates how to calculate a SHA-512 hash for both files, retrieve a copy of the core file from the Linux file system, and copy both files to an FTP server for later analysis:

```
RP/0/RP0/CPU0:ios# cd disk0:/core RP/0/RP0/CPU0:ios# run ls -la /misc/disk1 Tue Aug 27 20:29:33.083 UTC
total 7616
drwxr-xr-x 10 root root    4096 Aug 27 18:40 .
drwxr-xr-x  6 root root    4096 Jun 14 20:33 ..
-rw-r--r--  1 root root  589824 Jan 18  2019 .csbsc
drwxr-xr-x  5 root root    4096 Jan 18  2019 apprepo-dont-delete
drwxr-xr-x  5 root root    4096 Aug 26 00:54 cisco_support
drwxr-xr-x  2 root root    4096 Jan 18  2019 dumper
drwxr-xr-x  2 root root    4096 Jan 18  2019 ipodwdm_log -rwxr-xr-x  1 root root 6972439 Aug 27 18:40 netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.gz -rw-r--r--  1 root root  188827 Aug 27 18:40 netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.txt drwxr-xr-x  2 root root    4096 Jan 18  2019 nvram
drwxr-xr-x  2 root root    4096 Aug 20 14:45 showtech
drwxr-xr-x  2 root root    4096 Jan 18  2019 shutdown
drwxr-xr-x  2 root root    4096 Jan 18  2019 tftpboot

RP/0/RP0/CPU0:ios# run sha512sum /misc/disk1/netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.gz Tue Aug 27 20:32:01.569 UTC
8355d13404532994b723bd941ad5721b3686b043a66df09be9fdc14f7fea967bd8bddae098490ac6e9c20fa9382778c1cc6e630b7a83aa6225a61588d0660100
/misc/disk1/netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.gz

RP/0/RP0/CPU0:ios# run sha512sum /misc/disk1/netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.txt Tue Aug 27 20:32:06.301 UTC
236fccd767e4204e36d4b0221ed10dffdbfe84b62621406687d817bbd147a037da3d4cfdc209f9334782f4522010e750ae79c01904cc520d15de063239ba3dd6
/misc/disk1/netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.txt

RP/0/RP0/CPU0:ios# run cp /misc/disk1/netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.txt . Tue Aug 27 20:32:27.442 UTC

RP/0/RP0/CPU0:ios# run cp /misc/disk1/netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.gz . Tue Aug 27 20:32:34.408 UTC

RP/0/RP0/CPU0:ios# dir Tue Aug 27 20:32:37.060 UTC

Directory of disk0:/core 45 -rwxr-xr-x 1 6972439 Aug 27 20:32 netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.gz
46 -rw-r--r-- 1  188827 Aug 27 20:32 netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.txt RP/0/RP0/CPU0:ios# copy disk0:/core/netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.gz ftp: Tue Aug 27 20:33:37.752 UTC
Address or name of remote host [10.1.1.1]?
Destination username: [anonymous]?
Destination password: [anonymous@ios]?
Destination filename [netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.gz]?
Writing ftp://anonymous:*@10.1.1.1/netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.gz
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
6972439 bytes copied in      3 sec (  1920253)bytes/sec

RP/0/RP0/CPU0:ios# copy disk0:/core/netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.txt ftp: Tue Aug 27 20:34:06.108 UTC
Address or name of remote host [10.1.1.1]?
Destination username: [anonymous]?
Destination password: [anonymous@ios]?
Destination filename [netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.txt]?
Writing ftp://anonymous:*@10.1.1.1/netio_4158.by.user.20190827-184001.xr-vm_node0_RP0_CPU0.31f27.core.txt
CCCCCCCCCCCC
188827 bytes copied in      0 sec
```

It is highly recommended that hash values be calculated again for all files after they have been copied to the FTP server to ensure no errors were introduced during the file transfer process.

Submit all command output (including calculated hash values) and all process and core files that were obtained in this step to the relevant TAC SR.

## Related Documentation

Additional information about Cisco Software Integrity Assurance, as well as forensic investigation procedures for other platforms, can be found at the following link:

Cisco Security Tactical Resources

https://tools.cisco.com/security/center/tacticalresources.x

## Cisco IOS XR Device Forensic Response Checklist

Step 1 – Create the Cisco IOS XR Device Problem Description

Device Problem Description uploaded to SR

Step 2 – Document Cisco IOS XR Run-Time Environment

Output of system-level show and dir commands uploaded to SR

Output of directory commands uploaded to SR

Ouput of CPU and process-level show commands uploaded to SR

Output of system integrity commands uploaded to SR

Step 3 – Execute the Cisco IOS XR Forensic Data Dollection Script

Output of the forensic data collection script uploaded to SR

Step 4 – Obtaining a Core File

Core dump .gz file uploaded to SR

Sha512sum of core dump .gz file uploaded to SR

Core dump .txt file uploaded to SR

Sha512sum of core dump .txt file uploaded to SR

Note: If the manual analysis that is outlined in Appendix A was used instead of the automated data collection script in Step 3, submit the following additional items:

Step A1 – Cisco IOS XR Process Enumeration

Output of show netio clients uploaded to SR

Output of show packet-memory clients uploaded to SR

Step A2 – Cisco IOS XR Process Examination

Output of run show_memory_ng -p <PID> uploaded to SR

Output of run grep r.x /proc/<PID>/maps uploaded to SR

Step A3 – Container Enumeration

Output of all yum and docker commands uploaded to SR

## Appendix A – Manual Process Enumeration and Examination

## Step A1 – Cisco IOS XR Process Enumeration

Note: The commands in this section should only be executed if the automated forensic data collection script cannot be used in Step 3 of this document.

The base set of Cisco IOS XR Software processes that should be examined first are in the following list:

```
netio
 	dumper
	processmgr
 	syslogd
 	syslog_dev
 	syslogd_helper
 	sysdb_shared_nc
 	sysdb_shared_sc
 	sysdb_svr_admin
 	sysdb_svr_local
 	sysdb_mc
 	sysdb_bagregister
 	sysdb_show_health
```

In addition, the processes that are returned in the output of the following commands should be appended to the base set of processes:

```
show netio clients
 	show packet-memory clients
```

Note: The show netio  clients and show packet-memory clients commands will list all processes that are communicating with the Cisco IOS XR network stack (through netio) and all processes with access to Cisco IOS XR packet processing memory (similar to iomem in Cisco IOS Software), respectively. These processes are the most likely targets of tampering or modification to read, write, or modify packets traversing the platform or to hide the presence of malicious code.

Access the command line of the Cisco IOS XR device and issue the following commands:

```
show netio clients
show packet-memory clients
```

Note: The procedures in the following examples were executed on a minimally configured platform and are only for illustration of the concepts. Platforms in a production environment are likely to have additional processes running (particularly processes for configured dynamic routing protocols), and memory maps and core dumps should be acquired for all processes reported by the show netio clients and show packet-memory clients commands.

An example of this procedure follows:

```
RP/0/RP0/CPU0:ios# show netio clients | begin ClientID Tue Aug 27 14:07:54.534 UTC
ClientID         Drop/Total        Drop/Total      Cur/High/Max    Cur/High/Max 
--------------------------------------------------------------------------------
ipv6_icmp           0/0               0/0             0/0/1000        0/0/1000  
icmp                0/24              0/0             0/1/1000        0/0/1000  
clns              L 0/0               0/0           L 0/0/2000        0/0/0     
                  H 0/0                             H 0/0/2000                  
eth_mgmt            0/0               0/0        
ipv6_io             0/0               0/0             0/0/1000        0/0/1000  
ipv6_nd             0/2               0/0             0/1/1500        0/0/1000  
l2snoop             0/0               0/0             0/0/1000        0/0/0     
ether_sock          0/0               0/0        
icmpv6_unreach_jump        0/0               0/0        
raw               L 0/0               0/0           L 0/0/6400        0/0/0     
                  H 0/0                             H 0/0/6400                  
tcp               L 0/20594           0/0          L 0/19/6400        0/0/0     
                  H 0/0                             H 0/0/6400                  
udp               L 0/67877           0/0           L 0/4/6400        0/0/0     
                  H 0/0                             H 0/0/6400                  
ipp                 0/0               0/0        
arp                 0/1264268         0/0             0/8/1000        0/0/1000  
mpls_io             0/0               0/0             0/0/1000        0/0/1000  
ipv4                0/0               0/0             0/0/1000        0/0/1000  
ipv6                0/0               0/0             0/0/1000        0/0/1000  

Key:
  L = queue for lower priority packets
  H = queue for higher priority packets
```

Note the process name in the ClientID column, add each entry to the base list of processes for examination, and proceed to the next step.

```
RP/0/RP0/CPU0:ios# show packet-memory clients Tue Aug 27 14:08:05.703 UTC

Connected clients to the Packet Manager
=======================================

Job Id    Coid      Options   Process             
------    ----      -------   -------             
280       73        0         aib                 
194       64        0         ipv6_io             
370       33        0         ncd                 
369       35        0         nsr_ping_reply      
308       48        0         ipv4_io             
362       46        0x22      netio               
362       122       0x1       netio               
138       67        0x1       fib_mgr             
325       45        0         ipv6_nd             
319       224       0x1       iedged              
330       39        0         ether_sock          
205       41        0         ipv6_assembler      
240       85        0         clns                
235       41        0         l2snoop             
293       87        0         mpls_io             
307       51        0         tcp                 
299       50        0x1       object_tracking     
412       41        0         raw_ip              
136       41        0         udp                 
318       50        0x1       fhrp_output         
365       76        0         arp                 
211       94        0x1       l2fib_mgr           
1186      124       0         telemetry_encoder   
302       138       0         ipsec_pp            
1194      63        0x1       vservice_mgr        
1199      71        0x1       l2tp_mgr            
1196      98        0x1       xtc_agent           
1197      229       0x1       l2vpn_mgr
```

Note the process name in the Process column, add each entry to the running list (base list plus show netio clients output) of processes for examination, and remove any duplicate process names.

In this example, the list of candidate processes for examination is as follows:

```
netio
dumper
processmgr
syslogd
syslog_dev
syslogd_helper
sysdb_shared_nc
sysdb_shared_sc
sysdb_svr_admin
sysdb_svr_local
sysdb_mc
sysdb_bagregister
sysdb_show_health
ipv6_icmp
icmp
clns 
eth_mgmt
ipv6_io  
ipv6_nd  
l2snoop     
ether_sock        
icmpv6_unreach_jump        
raw                  
tcp        
udp                  
ipp 
arp 
mpls_io
ipv4
ipv6
aib                 
ncd                 
nsr_ping_reply      
ipv4_io             
fib_mgr             
iedged              
ipv6_assembler             
object_tracking     
raw_ip              
fhrp_output         
l2fib_mgr           
telemetry_encoder   
ipsec_pp            
vservice_mgr        
l2tp_mgr            
xtc_agent           
l2vpn_mgr
```

Next, iterate through the list of candidate processes and determine its process identification (PID) number using the show process <process_name> command. An example of this procedure follows.

Note: Processes registered but not actively executing will not return a PID value.

```
RP/0/RP0/CPU0:ios# show process netio | inc PID Tue Aug 27 14:52:42.190 UTC
                     PID: 4158
RP/0/RP0/CPU0:ios# show process dumper | inc PID Tue Aug 27 14:53:03.054 UTC
                     PID: 3244
RP/0/RP0/CPU0:ios# show process processmgr | inc PID Tue Aug 27 14:53:22.049 UTC
                     PID: 3210

RP/0/RP0/CPU0:ios# show process syslogd | inc PID Tue Aug 27 14:53:23.064 UTC
                     PID: 3252
RP/0/RP0/CPU0:ios# show process syslog_dev | inc PID Tue Aug 27 14:53:30.071 UTC
                     PID: 3254
RP/0/RP0/CPU0:ios# show process syslogd_helper | inc PID Tue Aug 27 14:53:45.938 UTC
                     PID: 3253
[output truncated]
```

Next, add the PID to the list of candidate processes, similar to the following example:

```
Process Name		Process Identifier (PID)
netio			4158
dumper			3244
processmgr		3210
syslogd			3252
syslog_dev		3254
syslogd_helper		3253
sysdb_shared_nc		3357
sysdb_shared_sc		3358
sysdb_svr_admin		3359
sysdb_svr_local		3265
sysdb_mc		3277
sysdb_bagregister	3282
sysdb_show_health	<no PID>
ipv6_icmp		<no PID>
icmp			<no PID>
clns 			5303
eth_mgmt		4166
ipv6_io  		4196
ipv6_nd  		4192
l2snoop     		5325
ether_sock        	4956
icmpv6_unreach_jump 	<no PID>      	
raw                 	<no PID>
tcp   			5308     
udp        		5309          
ipp 			<no PID>
arp 			5304
mpls_io			5253
ipv4			<no PID>
ipv6			<no PID>
aib 			4182                
ncd                 	4170
nsr_ping_reply  	4174    
ipv4_io           	4190  
fib_mgr   		4194          
iedged              	4210
ipv6_assembler		5241             
object_tracking   	5494  
raw_ip			5306           
fhrp_output    		5310     
l2fib_mgr		5222           
telemetry_encoder	5105   
ipsec_pp        	5458    
vservice_mgr     	7251   
l2tp_mgr            	7226
xtc_agent    		7229       
l2vpn_mgr    		7228
```

Submit all command or script output that was collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step A2 – Cisco IOS XR Process Examination

This section outlines the steps necessary to examine running processes for unusual memory mappings, which may indicate that the platform has been tampered with or that malicious code has been placed on the system.

Linux process memory maps are typically flagged with one or more of the following attributes:

- r – indicates the memory region is readble

- w – indicates the memory region is writable

- x – indicates the memory region contains executable code

- s – indicates the memory region is shared

- R – indicates the memory region does not have swap space reserved

Executable code is generally contained in mappings with attributes r-x—(read and execute), and memory regions with mappings of rwx—(read, write, and execute) may indicate the presence of tampered software.

Process memory regions may be examined using the following command:

```
run show_memory_ng -p <PID>
```

Memory mappings for libraries or modules loaded by a process have a similar attribute scheme:

- r – indicates the memory region is readable

- w – indicates the memory region is writable

- x – indicates the memory region contains executable code

- s or p – indicates the memory region is shared or private

Memory mappings for libraries or modules loaded by a process may be examined by using the following command:

```
run grep r.x /proc/<PID>/maps
```

It is important that both the run show_memory_ng and run grep commands be executed for each process that was identified in the previous section. An example of this procedure follows:

```
RP/0/RP0/CPU0:ios# run show_memory_ng -p 4158 Tue Aug 27 18:37:47.053 UTC
4158:   netio d
Address           Kbytes     RSS    Anon  Locked Mode   Mapping
0000000060000000   43972       -       -       - rw-s-  particle_body
0000000062af1000    8064       -       -       - rw-s-  particle_header
00000000632d1000    1004       -       -       - rw-s-  particle_clone
00000000633cc000   18504       -       -       - rw-s-  pakhdr
00000000645de000    1628       -       -       - rw-s-  pakfsv
0000000064775000    1028       -       -       - rw-s-  paktrace
0000000100000000      64       -       -       - ---s-  zero (deleted)
0000000100010000      28       -       -       - rw-s-  header
0000000100017000     676       -       -       - ---s-  zero (deleted)
00000001000c0000      32       -       -       - rw-s-  header
[output truncated]

RP/0/RP0/CPU0:ios# run grep r.x /proc/4158/maps Tue Aug 27 18:38:17.013 UTC
7f55c9789000-7f55c978a000 r-xp 00000000 07:04 15136
/opt/cisco/XR/packages/xrv9k-fwding-2.0.0.0-r633/all/lib/libip_acl_config.so
7f55c99a4000-7f55c99a6000 r-xp 00000000 07:04 132403              
/opt/cisco/XR/packages/xrv9k-iosxr-fwding-6.0.0.0-r633/all/lib/libl2vpn_util.so
7f55c9ba6000-7f55c9ba9000 r-xp 00000000 07:04 132364 /opt/cisco/XR/packages/xrv9k-iosxr-fwding-6.0.0.0-r633/all/lib/libl2fib_gsp.so
7f55c9db4000-7f55c9dc2000 r-xp 00000000 07:04 132388 /opt/cisco/XR/packages/xrv9k-iosxr-fwding-6.0.0.0-r633/all/lib/libl2vpn_gsp.so
7f55c9fc2000-7f55c9fcd000 r-xp 00000000 07:04 9719 /opt/cisco/XR/packages/xrv9k-iosxr-infra-4.2.0.0-r633/all/lib/libpacktlv.so
7f55ca1ce000-7f55ca1d5000 r-xp 00000000 07:04 132236 /opt/cisco/XR/packages/xrv9k-iosxr-fwding-6.0.0.0-r633/all/lib/libgen_dbg_ltrace.so
[output truncated]
```

Lastly, retrieve a list of all modules loaded by the operating system kernel using the following command:

```
run cat /proc/modules
```

An example of this procedure follows:

```
RP/0/RP0/CPU0:ios# run cat /proc/modules Tue Aug 27 18:45:07.012 UTC
dm_thin_pool 46373 1 - Live 0xffffffffa055c000
dm_persistent_data 52976 1 dm_thin_pool, Live 0xffffffffa0549000
libcrc32c 1371 1 dm_persistent_data, Live 0xffffffffa0545000
crc32c 1802 1 - Live 0xffffffffa0541000
dm_bio_prison 6128 1 dm_thin_pool, Live 0xffffffffa053c000
dm_bufio 20186 1 dm_persistent_data, Live 0xffffffffa0532000
igb_uio 4936 7 - Live 0xffffffffa052d000 (O)
vhost_net 11216 0 - Live 0xffffffffa0526000
vhost 24752 1 vhost_net, Live 0xffffffffa051a000
vfat 10844 0 - Live 0xffffffffa0514000
fat 56402 1 vfat, Live 0xffffffffa0500000
xts 3422 9 - Live 0xffffffffa04fc000
gf128mul 7124 1 xts, Live 0xffffffffa04f7000
dm_crypt 18301 9 - Live 0xffffffffa04ee000
veth 5099 0 - Live 0xffffffffa04e9000
tun 21858 4 vhost_net, Live 0xffffffffa04de000
bridge 105980 0 - Live 0xffffffffa04ba000
ip6table_filter 1831 0 - Live 0xffffffffa04b6000
ip6_tables 17032 1 ip6table_filter, Live 0xffffffffa04ad000
iptable_filter 1826 0 - Live 0xffffffffa04a9000
ip_tables 17715 1 iptable_filter, Live 0xffffffffa04a0000
8021q 22175 0 - Live 0xffffffffa0495000
garp 7046 1 8021q, Live 0xffffffffa0490000
stp 2084 2 bridge,garp, Live 0xffffffffa048c000
 [output truncated]
```

Submit all command or script output that was collected in this section to the relevant TAC SR, and proceed to the next section of this document.

## Step A3 – Container Enumeration

Cisco IOS XR Routers provide application-hosting features that simplify the integration of applications, configuration management tools, and industry-standard zero-touch provisioning mechanisms. Applications may be hosted natively in the Cisco IOS XR control plane, or applications may be deployed in Linux containers (LXCs) in the third-party container.

Both the Cisco IOS XR control plane and third-party container should be examined when determining the integrity of the Cisco IOS XR operating system.

Cisco IOS XR Native Hosting Commands

The native hosting environment is enumerated by accessing the Bash shell, checking to ensure that root -level privileges are obtained, and then executing the yum (Yellowdog Updater, Modified) command to examine YUM history, YUM repository lists, and installed packages as follows:

```
bash
id
yum history list
yum repolist all
yum list installed
```

An example of this procedure follows:

```
RP/0/RP0/CPU0:ios# bash [ios:~]$ id uid=0(root) gid=0(root) groups=0(root)

[ios:~]$ yum history list Loaded plugins: downloadonly, protect-packages, rpm-persistence
ID     | Command line             | Date and time    | Action(s)   | Altered
------------------------------------------------------------------------------
     2 | install iperf3-doc       | 2021-11-18 14:46 | Install     |    1   
     1 | install https://devhub.c | 2021-11-18 11:37 | Install     |    1 PP
history list

[ios:~]$ yum repolist all Loaded plugins: downloadonly, protect-packages, rpm-persistence
localdb  |  951 B     00:00 ... 
repo id               repo name                        status
localdb               Local RPM Database               enabled: 2
devhub.cisco.com_artifactory_xr600_3rdparty_x86_64_
added from: https://devhub.cisco.com/artifactory/xr600/3rdparty/x86_64/                                                                                  
                                                       enabled: 5912
repolist: 5914

[ios:~]$ yum list installed Loaded plugins: downloadonly, protect-packages, rpm-persistence
Installed Packages
aer-inject.x86_64             git-r1.0                   installed
alsa-conf.x86_64              1.0.28-r0.0                installed
alsa-conf-base.x86_64         1.0.28-r0.0                installed
attr.x86_64                   2.4.47-r0.0                installed
attr-setfattr.static.x86_64   2.4.47-r0.0                installed
audit.x86_64                  2.3.2-r8.0                 installed
auditd.x86_64                 2.3.2-r8.0                 installed
base-files.x86_64             3.0.14-r89.0               installed
base-passwd.x86_64            3.5.29-r0.1.0              installed
bash.x86_64                   4.3-r0.0                   installed
binutils.x86_64               2.24-r0.0                  installed
bluez4.x86_64                 4.101-r11.0                installed
bridge-utils.x86_64           1.5-r0.0                   installed
busybox.x86_64                1.22.1-r32.1.0             installed
busybox-hwclock.x86_64        1.22.1-r32.1.0             installed
bzip2.x86_64                  1.0.6-r5.0                 installed
ca-certificates.x86_64        20140325-r0.0              installed
cbt.x86_64                    1.0-r3.0                   installed
ccctools.x86_64               1.0-r2.0                   installed
ccore.x86_64                  1.0-r3.0                   installed
cdrtools.x86_64               3.01a20-r0.0               installed
checkpolicy.x86_64            2.3-r0.0                   installed
[output truncated]
```

Cisco IOS XR Third-Party Hosting Commands

The third-party hosting environment is enumerated by accessing the Bash shell, checking to ensure that root -level privileges are obtained, and then executing several docker commands to examine the Docker system and LXC container configurations as follows:

```
bash
id
docker system info
docker images
docker container ls
docker network ls 
docker volume ls
```

An example of this procedure follows:

```
RP/0/RP0/CPU0:ios# bash [ios:~]$ id uid=0(root) gid=0(root) groups=0(root)
[ios:~]$

[ios:~]$ docker system info Containers: 2
 Running: 2
 Paused: 0
 Stopped: 0
Images: 1
Server Version: 18.05.0-ce
Storage Driver: devicemapper
 Pool Name: docker-253:0-34-pool
 Pool Blocksize: 65.54kB
 Base Device Size: 2.147GB
 Backing Filesystem: ext4
 Udev Sync Supported: true
 Data file: /dev/loop11
 Metadata file: /dev/loop12
 Data loop file: /var/lib/docker/devicemapper/devicemapper/data
 Metadata loop file: /var/lib/docker/devicemapper/devicemapper/metadata
 Data Space Used: 112.1MB
 Data Space Total: 107.4GB
 Data Space Available: 4.035GB
 Metadata Space Used: 700.4kB
 Metadata Space Total: 2.147GB
 Metadata Space Available: 2.147GB
 Thin Pool Minimum Free Space: 10.74GB
 Deferred Removal Enabled: false
 Deferred Deletion Enabled: false
 Deferred Deleted Device Count: 0
 Library Version: 1.02.76 (2012-08-07)
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins:
 Volume: local
 Network: bridge host macvlan null overlay
 Log: awslogs fluentd gcplogs gelf journald json-file logentries splunk syslog
Swarm: inactive
Runtimes: runc
Default Runtime: runc
Init Binary: docker-init
containerd version: 773c489c9c1b21a6d78b5c538cd395416ec50f88
runc version: 4fc53a81fb7c994640722ac585fa9ca548971871
init version: 949e6fa
Kernel Version: 3.14.23-WR7.0.0.2_standard
Operating System: <unknown>
OSType: linux
Architecture: x86_64
CPUs: 2
Total Memory: 19.45GiB
Name: host
ID: V2QU:4TEH:U5AB:5UJA:OHNL:KOLB:JLYE:BTVT:JW25:ODT2:LV74:UXA7
Docker Root Dir: /var/lib/docker
Debug Mode (client): false
Debug Mode (server): true
 File Descriptors: 27
 Goroutines: 41
 System Time: 2021-12-10T00:09:53.538829081Z
 EventsListeners: 0
Registry: https://index.docker.io/v1/
Labels:
Experimental: false
Insecure Registries:
 127.0.0.0/8
Live Restore Enabled: false

[ios:~]$ docker images REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
alpine              latest              c059bfaa849c        2 weeks ago         5.58MB

[ios:~]$ docker container ls CONTAINER ID   IMAGE    COMMAND    CREATED      STATUS     PORTS    NAMES
52812dfc5b82   alpine   "/bin/sh"  4 hours ago  Up 4 hours          alpine2
ce90aa616ed8   alpine   "/bin/sh"  5 hours ago  Up 5 hours          alpine

[ios:~]$ docker network ls NETWORK ID          NAME                DRIVER              SCOPE
5d8d27f2494c        host                host                local
7bde8d3c4233        none                null                local

[ios:~]$ docker volume ls DRIVER              VOLUME NAME
```

Submit all command output that was collected in this section to the relevant TAC SR.

End of Appendix A.

## Revision History

This document is part of the Cisco Security portal. Cisco provides the official information contained on the Cisco Security portal in English only.

This document is provided on an “as is” basis and does not imply any kind of guarantee or warranty, including the warranties of merchantability or fitness for a particular use. Your use of the information in the document or materials linked from the document is at your own risk. Cisco reserves the right to change or update this document without notice at any time.

Back to Top

| Version | Date | Author | Comments |
|---|---|---|---|
|  |  |  |  |
| 1.0 | 11/15/2019 | J. Barnes/D. Maunz | Initial public release. |
| 1.1 | 01/19/2022 | Dan Maunz | Added container enumeration. |
| 1.2 | 01/26/2023 | Dan Maunz | Validated procedure on Release 7.5.2. |
| 1.3 | 07/12/2023 | Dan Maunz | Clarified memory map and core file targets. |
| 1.4 | 11/01/2024 | Dan Maunz | Automated steps 3 and 4. |
| 1.5 | 10/14/2025 | Dan Maunz | Validated procedures on Release 25.3.1 |