---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-application-server-220158-troubleshoot-broadworks-s-2cea92bd25
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks-application-server/220158-troubleshoot-broadworks-snmp-availabilit.html
retrieved_at: 2026-09-07T13:03:06.800771+00:00
---

Troubleshoot BroadWorks SNMP Availability Report Failure

# Troubleshoot BroadWorks SNMP Availability Report Failure

### Download Options

Updated: January 26, 2023

Document ID: 220158

Contents

## Contents

## Introduction

This document describes the configuration to properly align the Network Function Managers (NFM) SNMP service availability with the managed nodes.

## Prerequisites

Cisco recommends that you have a knowledge of these topics:

Linux SNMP configuration

CLI configuration for for the BroadWorks servers

### Requirements

#### Network Function Manager

The NFM has been defined with a IP Address range for the SNMP variables to be defined for, or the individual node requirements have been set from the NFM Portal.  To validate the SNMP configuration navigate to nfmPortal > Network Monitoring > Open Console > Configure OpenNMS (admin dropdown) > Configure SNMP Community Names by IP Address .

The configured SNMP information is maintained on the Primary and Standby Network Monitoring NFM in /usr/local/opennms/opennms_base/etc/snmp-config.xml .

In the example, provided you can see that there are 2 ranges with unique write communities, and one specific IP defined with a unique read and write community string.  The information in this file must match what is defined in the managed node.

```
/usr/local/opennms/opennms_base/etc/snmp-config.xml
<snmp-config xmlns="http://xmlns.opennms.org/xsd/config/snmp" max-vars-per-pdu="1" version="v2c" read-community="public" timeout="3000" retry="1" port="8001">
  <definition write-community="public" port="8001">
    <range begin="10.201.207.5" end="10.201.207.250"/>
  </definition>
  <definition write-community="notPublic">
    <range begin="10.201.210.5" end="10.201.210.255"/>
  </definition>
  <definition write-community="hamBurger" read-community="hamBurger">
    <specific>10.201.191.220</specific>
  </definition>
</snmp-config>
```

#### Managed Node

Adjust the default BroadWorks SNMP community strings "public" to what is required in your environment.

```
ADP_CLI/Interface/SNMP/Agent> get
  port = 8001
  encoding = ISO-8859-1
  readCommunity = hamBurger
  writeCommunity = hamBurger
  trapCommunity = public
  trapSourceAddress = 10.201.191.220
  disableV2 = false
  hostMibII = false
```

Dependant on your base Operating Systems (OS) SNMP configuration, you must update the community string needed for the BroadWorks agent to proxy the incoming requests.  You can use a text editor like vi to adjust the values in /usr/local/broadworks/bw_base/conf/BWSnmpProxy.conf to match the OS /etc/snmp/snmpd.conf string.  In the example provided, you can see the alignment for the BWSnmpProxy.conf and snmpd.conf community string for ' hotDogs '.

```
/usr/local/broadworks/bw_base/conf/BWSnmpProxy.conf
<SNMP_PROXY>
   <MASTER_AGENT>
        <NAME>BroadWorks Master SNMP Agent</NAME>
        <DESCRIPTION>Configuration MIB</DESCRIPTION>
        <TRAP_LISTENING_PORT>20162</TRAP_LISTENING_PORT>
        <STATUS>On</STATUS>
        <CLI>ConfigurationManagement</CLI>
        <OID>.1.3.6.1.4.1.6431.1.1.5</OID>
        <MIB>/usr/local/broadworks/bw_base/conf/BroadworksConfiguration.mib</MIB>
        <CLI_VISIBLE>True</CLI_VISIBLE>
   </MASTER_AGENT>
   <SUB_AGENT>
        <NAME>LicenseManager</NAME>
        <DESCRIPTION>LicenseManager MIB</DESCRIPTION>
        <HOST></HOST>
        <PORT></PORT>
        <OID>.1.3.6.1.4.1.6431.1.1.6</OID>
        <CLI>LicenseManager</CLI>
        <STATUS>ON</STATUS>
        <START></START>
        <STOP></STOP>
        <MIB>/usr/local/broadworks/bw_base/conf/BW-LicenseManager.mib</MIB>
        <COMMUNITY></COMMUNITY>
        <CLI_VISIBLE>True</CLI_VISIBLE>
   </SUB_AGENT>
   <SUB_AGENT>
        <NAME>Net-Snmp</NAME>
        <DESCRIPTION>Linux MIB-II sub agent</DESCRIPTION>
        <HOST>localhost</HOST>
        <PORT>161</PORT>
        <OID>.1.3.6.1.2.1</OID>
        <CLI>Mib-II</CLI>
        <STATUS>ON</STATUS>
        <START></START>
        <STOP></STOP>
        <MIB>/usr/local/broadworks/bw_base/conf/mibII.mib</MIB>
        <COMMUNITY>hotDogs</COMMUNITY>
        <CLI_VISIBLE>True</CLI_VISIBLE>
    </SUB_AGENT>
    <SUB_AGENT>
        <NAME>Net-Snmp-Ucd</NAME>
        <DESCRIPTION>Linux UCD-SNMP sub agent</DESCRIPTION>
        <HOST>localhost</HOST>
        <PORT>161</PORT>
        <OID>.1.3.6.1.4.1.2021</OID>
        <CLI>UCD-SNMP</CLI>
        <STATUS>ON</STATUS>
        <START></START>
        <STOP></STOP>
        <MIB>/usr/local/broadworks/bw_base/conf/UCD-SNMP-MIB.mib</MIB>
        <COMMUNITY>hotDogs</COMMUNITY>
        <CLI_VISIBLE>True</CLI_VISIBLE>
    </SUB_AGENT>
    <SUB_AGENT>
        <NAME>HostResources</NAME>
        <DESCRIPTION>Linux HOST-RESOURCES sub agent</DESCRIPTION>
        <HOST>localhost</HOST>
        <PORT>161</PORT>
        <OID>.1.3.6.1.2.1.25</OID>
        <CLI>HostResources</CLI>
        <STATUS>ON</STATUS>
        <START></START>
        <STOP></STOP>
        <MIB>/usr/local/broadworks/bw_base/conf/HOST-RESOURCES-MIB.mib</MIB>
        <COMMUNITY>hotDogs</COMMUNITY>
        <CLI_VISIBLE>True</CLI_VISIBLE>
    </SUB_AGENT>
</SNMP_PROXY>
```

```
/etc/snmp/snmpd.conf
com2sec notConfigUser  default       hotDogs
group   notConfigGroup v1           notConfigUser
group   notConfigGroup v2c           notConfigUser
view    systemview    included   .1.3.6.1.2.1
access  notConfigGroup ""      any       noauth    exact  systemview none none
syslocation <support_location_URL>
syscontact <support_email_address>
dontLogTCPWrappersConnects yes
disk / 10000
view    systemview    included   .1.3.6.1.4.1.2021
sysdescr BroadWorks Application Delivery Platform
sysobjectid .1.3.6.1.4.1.6431.1.1.8.1.29
view    systemview    included   .1.3.6.1.4.1.6431.1.1.11
pass_persist .1.3.6.1.4.1.6431.1.1.11 /usr/local/perl/perl_base/bin/perl /usr/local/broadworks/bw_base/sbin/system-mib.pl
pass  .1.3.6.1.2.1.55 /usr/local/perl/perl_base/bin/perl /usr/local/broadworks/bw_base/bin/ipv6-mib.pl
```

## Additional Checks and Information to Collect and Update in your SR

If the NFM still shows the service availability down for the managed node, this information can be collected then provided to TAC with your SR.

### NFM

$ tech-support > /export/home/bwadmin/$(date +%Y-%m-%d)_`hostname`_tech-support.txt

- attach file generated in /export/home/bwadmin/

$ cat /usr/local/opennms/opennms_base/etc/snmp-config.xml > /export/home/bwadmin/$(date +%Y-%m-%d)_`hostname`_snmp-config.xml

- attach file generated in /export/home/bwadmin/

$ /usr/local/netsnmp/netsnmp_base/bin/snmpget -v2c -c <community_name> <managed_node_IP>:8001 SNMPv2-MIB::sysDescr.0

- attach output to SR

$ /usr/local/netsnmp/netsnmp_base/bin/snmpget -v2c -c <community_name> <managed_node_IP>:161 SNMPv2-MIB::sysDescr.0

- attach output to SR

### Managed Node

$ tech-support > /export/home/bwadmin/$(date +%Y-%m-%d)_`hostname`_tech-support.txt

- attach file generated in /export/home/bwadmin/

$ cat /etc/snmp/snmpd.conf |grep -v ^# > /export/home/bwadmin/`hostname`_snmpd.conf

- attach file generated in /export/home/bwadmin/

$ cat /usr/local/broadworks/bw_base/conf/BWSnmpProxy.conf > /export/home/bwadmin/`hostname`_BWSnmpProxy.conf $ cat /usr/local/broadworks/bw_base/conf/netsnmpd.conf > /export/home/bwadmin/`hostname`_netsnmpd.conf

$ /usr/local/netsnmp/netsnmp_base/bin/snmpget -v2c -c <community_name> <managed_node_IP>:8001 SNMPv2-MIB::sysDescr.0

- attach output to SR

$ /usr/local/netsnmp/netsnmp_base/bin/snmpget -v2c -c <community_name> <managed_node_IP>:161 SNMPv2-MIB::sysDescr.0

- attach output to SR

### Revision History

1.0

26-Jan-2023

Initial Release

### Contributed by Cisco Engineers

Danny Hartobey

Cisco TAC Engineer

### This Document Applies to These Products

- BroadWorks Application Server

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 26-Jan-2023 | Initial Release |