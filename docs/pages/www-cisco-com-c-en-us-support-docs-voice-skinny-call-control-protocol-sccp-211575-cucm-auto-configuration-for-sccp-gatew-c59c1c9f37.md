---
doc_id: www-cisco-com-c-en-us-support-docs-voice-skinny-call-control-protocol-sccp-211575-cucm-auto-configuration-for-sccp-gatew-c59c1c9f37
source_url: https://www.cisco.com/c/en/us/support/docs/voice/skinny-call-control-protocol-sccp/211575-CUCM-Auto-Configuration-for-SCCP-Gateway.html
retrieved_at: 2026-08-16T23:42:19.973692+00:00
---

CUCM Auto Configuration for SCCP Gateways

# CUCM Auto Configuration for SCCP Gateways

### Download Options

Updated: July 22, 2016

Document ID: 211575

Contents

## Contents

## Introduction

This document describes how to use Skinny Client Control Protocol (SCCP) auto configuration on Cisco Interworking Operating System (IOS) gateways with Cisco Unified Communications Manager (CUCM).

Contributed by Luis Ramirez, Cisco TAC Engineer.

## Prerequisites

### Requirements

Ensure these requirements are met before you attempt this configuration:

- Full connectivity between the gateway and CUCM Server

- IOS version compatible with CUCM Server version

- Add SCCP gateway and the endpoints in CUCM Server

### Components Used

The information in this document is based on certain software and hardware versions, refer to the compatibility matrix.

Caution : The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Compatibility

To determine compatibility between CUCM and IOS, refer to Cisco Collaboration Systems Release Summary Matrix for IP Telephony .

## Configure

### Summary Steps

Step 1. enable

Step 2. configure terminal

Step 3. ccm-manager config server [CUCM IP address]

Step 4. ccm-manager sccp local [Interface]

Step 5. sccp local [Interface]

Step 6. ccm-manager sccp

### Detailed Steps

Command or Action

Purpose

Step 1.

enable

Example:

Router> enable

Enables privileged EXEC mode.

•Enter your password if prompted.

Step 2.

configure terminal

Example:

Router# configure terminal

Enters global configuration mode.

Step 3.

ccm-manager config server [ CUCM IP address]

Example:

Router(config)# ccm-manager config server 192.168.1.154

Sets address of configuration server.

• CUCM IP Address —Specifies the IP address or logical name of the Trivial File Transfer Protocol ( TFTP) server from which the Extensible Markup Language ( XML) configuration files are downloaded from.

Step 4.

ccm-manager sccp local [Interface]

Example:

Router(config)# ccm-manager sccp local FastEthernet 0/0

Select the local interface that the Skinny Client Control Protocol (SCCP) application uses to register with Cisco CallManager.

• For the gateway to know which interface MAC address will be used to build the XML file name to request to CUCM.

Step 5.

sccp local [Interface]

Example:

Router(config)# sccp local FastEthernet 0/0

Select the local interface that the Skinny Client Control Protocol (SCCP) application uses to register with Cisco CallManager.

•The interface that will be used to reach CUCM for registration.

Step 6.

ccm-manager sccp

Example:

Router(config)# ccm-manager sccp

To enable Cisco CallManager autoconfiguration of the Cisco IOS gateway.

•      Use this command to trigger TFTP download of the eXtensible Markup Language (XML) configuration file. Issuing this command immediately triggers the download, and also enables the Skinny Client Control Protocol (SCCP) and SCCP Telephony Control Application (STCAPP), applications that enable Cisco CallManager control of gateway-connected telephony endpoints.

## Example

CUCM adds the Domain Name System (DNS) Servers configured on CUCM to the Voice Gateway.

```
ip name-server 192.168.1.156
ip name-server 192.168.1.1
```

CUCM adds the active Call Manager Servers with the same priority configured under Cisco Unified Communications Manager Group , the sccp ccm group and enables sccp .

```
sccp ccm 192.168.1.154 identifier 2 version 4.1
sccp ccm 192.168.1.167 identifier 1 version 4.1
sccp
sccp ccm group 1
 associate ccm 1 priority 1
 associate ccm 2 priority 2
```

CUCM creates the dial-peers for the configured ports.

```
dial-peer voice 999000 pots
 service stcapp
 port 0/0
 
dial-peer voice 999001 pots
 service stcapp
 port 0/1
```

CUCM adds this configuration to the existing voice-ports .

```
voice-port 0/0
 timeouts initial 60
 timeouts interdigit 60
 timeouts ringing infinity
 
voice-port 0/1
 timeouts initial 60
 timeouts interdigit 60
 timeouts ringing infinity
```

CUCM configures the stcapp ccm-group , enables stcapp , configures stcapp feature access-code and stcapp speed-dials .

```
stcapp ccm-group 1
stcapp
stcapp feature access-code
stcapp feature speed-dial
```

Note : Ensure there is no sccp ccm-group with tag number 1 or stcapp ccm-group with tag number 1 previously configured on the router.

## Relevant sections of XML Configuration File

```
<product> VG204 </product> <- Device Type <callManagerGroup>
 
<name> Luis-SUB-PUB-DP </name> <- Call Manager Group Configured on CUCM <members>
<member  priority=" 0 "> <- First Priority Device <callManager>
<name> CUCM9-1SUB </name> <- CUCM Server with First Priority <ports>
<ethernetPhonePort> 2000 </ethernetPhonePort> <- SCCP Port </ports>
 
</member>
<member  priority=" 1 "> <- Second Priority Device <callManager>
<name>CUCM9-1</name>
<description> CUCM9-1 </description> <- CUCM Server with Second Priority <ports>
<ethernetPhonePort> 2000 </ethernetPhonePort> <- SCCP Port <product> ANALOG </product> <- Product Type Analog <product> 4FXS-SCCP </product> <- 4 FXS with SCCP <deviceProtocol> SCCP </deviceProtocol> <- Device Will Run SCCP
```

## Troubleshoot

This section provides steps to troubleshoot SCCP auto-registration issues.

Step 1. The command show ccm-manager config-download shows the auto-configuration download status.

Check the MAC address used, interface used, TFTP configuration attempts (fails and succeeds), Configuration Error History, etc.

```
Router# show ccm-manager confing-download SCCP auto-configuration status
=============================================================== Registered with Call Manager: Yes
Local interface: FastEthernet0/0 (001f.cac3.de10) Current version-id: 1397830563-94fb712b-0c8f-48fa-ac91-a5edfcc9611b
Current config applied at: 04:16:01 UTC Jun 29 2002 Gateway downloads succeeded: 2
Gateway download attempts: 2 Last gateway download attempt: 04:20:43 UTC Jun 29 2002
Last successful gateway download: 04:20:43 UTC Jun 29 2002 Current TFTP server: 192.168.1.154 Gateway resets: 0
Gateway restarts: 0
Managed endpoints: 2 Endpoint downloads succeeded: 2
Endpoint download attempts: 2 Last endpoint download attempt: 04:16:01 UTC Jun 29 2002
Last successful endpoint download: 04:16:01 UTC Jun 29 2002
Endpoint resets: 0
Endpoint restarts: 0 Configuration Error History:
```

Step 2. Enable debug ccm-manager config-download all in order to see the configuration and download process on the Voice Gateway.

TFTP Address where the GW sends the configuration request.

```
040908: *Jun 22 05:31:19.909: cmapp_sccp_chk_cfg_tftp_server: TFTP server 192.168.1.154 has been configured
```

DNS Servers configured by CUCM.

```
040909: *Jun 22 05:31:19.909: cmapp_sccp_cfg_optional_dns_server: get prim name server addr 192.168.1.156
040911: *Jun 22 05:31:19.913: cmapp_sccp_cfg_optional_dns_server: added ip name-server 192.168.1.156
040912: *Jun 22 05:31:19.913: cmapp_sccp_cfg_optional_dns_server: get sec name server addr 192.168.1.1
040914: *Jun 22 05:31:19.913: cmapp_sccp_cfg_optional_dns_server: added ip name-server 192.168.1.1
```

XML file request.

```
040920: *Jun 22 05:31:19.913: cmapp_sccp_get_gw_name: XML file name generated->SKIGW1FCAC3DE10.cnf.xml
```

XML download attempt.

```
040925: *Jun 22 05:31:19.985: cmapp_sccp_tftp_download_file: File (tftp://192.168.105.154/SKIGW1FCAC3DE10.cnf.xml) read 5261 bytes
040926: *Jun 22 05:31:19.985: cmapp_sccp_get_xml_file_via_tftp: Read file tftp://192.168.105.154/SKIGW1FCAC3DE10.cnf.xml, len = 5261
```

Configuration of the dial-peers.

```
040944: *Jun 22 05:31:19.993: cmapp_sccp_build_cli: build new dial-peers
040945: *Jun 22 05:31:19.993: cmapp_sccp_add_new_dialpeers:
040946: *Jun 22 05:31:19.993: cmapp_sccp_get_intf_type: Searching for vdb for [0/-1/0]
040950: *Jun 22 05:31:20.005: cmapp_sccp_create_dialpeer: added dial-peer 999000
```

CUCM Servers are added, priority is configured and SCCP is enabled.

```
040964: *Jun 22 05:31:20.013: cmapp_sccp_cfg_global_parms: SCCP not enabled. Configure sccp
040966: *Jun 22 05:31:23.025: cmapp_sccp_cfg_global_parms: added sccp ccm CUCM9-1SUB identifer 1
040968: *Jun 22 05:31:23.029: cmapp_sccp_cfg_global_parms: added sccp ccm CUCM9-1 identifer 2
040970: *Jun 22 05:31:23.037: cmapp_sccp_cfg_global_parms: added associate ccm 1 priority 1
040972: *Jun 22 05:31:23.037: cmapp_sccp_cfg_global_parms: added associate ccm 2 priority 2
040974: *Jun 22 05:31:23.045: cmapp_sccp_cfg_global_parms: SCCP has been enabled
```

CUCM enables stcapp.

```
Jun 22 05:31:23.061: cmapp_sccp_cfg_global_parms: stcapp has been enabled
040978: *Jun 22 05:31:23.069: cmapp_sccp_cfg_global_parms: add CLI stcapp feature speed-dial
040979: *Jun 22 05:31:23.069: cmapp_sccp_cfg_global_parms: add CLI stcapp feature access-code
```

### Contributed by Cisco Engineers

Luis Ramirez

Cisco TAC

|  | Command or Action | Purpose |
|---|---|---|
| Step 1. | enable Example: Router> enable | Enables privileged EXEC mode. •Enter your password if prompted. |
| Step 2. | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3. | ccm-manager config server [ CUCM IP address] Example: Router(config)# ccm-manager config server 192.168.1.154 | Sets address of configuration server. • CUCM IP Address —Specifies the IP address or logical name of the Trivial File Transfer Protocol ( TFTP) server from which the Extensible Markup Language ( XML) configuration files are downloaded from. |
| Step 4. | ccm-manager sccp local [Interface] Example: Router(config)# ccm-manager sccp local FastEthernet 0/0 | Select the local interface that the Skinny Client Control Protocol (SCCP) application uses to register with Cisco CallManager. • For the gateway to know which interface MAC address will be used to build the XML file name to request to CUCM. |
| Step 5. | sccp local [Interface] Example: Router(config)# sccp local FastEthernet 0/0 | Select the local interface that the Skinny Client Control Protocol (SCCP) application uses to register with Cisco CallManager. •The interface that will be used to reach CUCM for registration. |
| Step 6. | ccm-manager sccp Example: Router(config)# ccm-manager sccp | To enable Cisco CallManager autoconfiguration of the Cisco IOS gateway. •      Use this command to trigger TFTP download of the eXtensible Markup Language (XML) configuration file. Issuing this command immediately triggers the download, and also enables the Skinny Client Control Protocol (SCCP) and SCCP Telephony Control Application (STCAPP), applications that enable Cisco CallManager control of gateway-connected telephony endpoints. |