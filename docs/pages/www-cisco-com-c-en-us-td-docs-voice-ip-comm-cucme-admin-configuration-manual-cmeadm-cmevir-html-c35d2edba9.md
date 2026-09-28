---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucme-admin-configuration-manual-cmeadm-cmevir-html-c35d2edba9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucme/admin/configuration/manual/cmeadm/cmevir.html
retrieved_at: 2026-08-21T07:21:51.268613+00:00
---

Cisco Unified Communications Manager Express System Administrator Guide

# Cisco Unified Communications Manager Express System Administrator Guide

Updated: August 15, 2022

Chapter: Virtual CME

## Chapter: Virtual CME

# Virtual CME

## Overview

The Cisco Unified Communications Manager Express (Unified CME) feature set is delivered with hardware router platforms, such
                           as the Cisco Integrated Services Router (ISR) series. From Cisco IOS XE Gibraltar 16.10.1, a subset of Unified CME features
                           (virtual CME) is used in virtualized environments with the Cisco CSR 1000v Series Cloud Services Router .

From Cisco IOS XE Bengaluru 17.4.1a , virtual CME is available for use with Cisco Catalyst 8000V Edge Software (Catalyst 8000V) series.

When upgrading to C8000V software from a CSR1000V release, an existing throughput configuration will be reset to a maximum
                                       of 250 Mbps. Install an HSEC authorization code, which you can obtain from your Smart License account, before reconfiguring
                                       your required throughput level.

## Prerequisites for Virtual CME

Virtual CME has the following prerequisites:

Hardware Requirements for Virtual CME

Software Requirements for Virtual CME

### Hardware Requirements for Virtual CME

The virtual CME feature set is included with the Cisco virtual router software. For more information about the virtual CME
                              host platform, see Cisco CSR 1000V Series Cloud Services Router Software Configuration Guide and Cisco Catalyst 8000V Edge Software Configuration Guide .

As part of the Unified CME 14.1 release, virtual CME features have been verified using the following:

VMware ESXi Hypervisor 6.5.0

Cisco UCS Server—Cisco UCS C240 M5 (UCSC-C240-M5SX)

For more information on the requirements on supported hypervisors, see CSR1000V Data Sheets and Cisco Catalyst 8000V Edge Software Data Sheet .

Virtual CME supports up to 450 device registrations and 113 active calls for any of the virtual machine resource profiles.
                              The resource files can be small, medium, large, or large plus extra RAM. For more information, see the following table:

Resource Profiles

vCPU

Memory

Cisco UCS

Hypervisor

Number of Devices Registered to Virtual CME

Number of Active Calls Supported on Virtual CME

Small

1

4

UCSC-C240-M5SX

ESXi 6.5.0

450

113

Medium

2

4

Large

4

4

Large plus Extra RAM

4

8

For information on the best practices for setting BIOS parameters for performance, see BIOS Settings .

For information on how to configure network interfaces for Unified CME, see Mapping Cisco CSR 1000v Network Interfaces to VM Network Interfaces and Mapping the Cisco Catalyst 8000V Network Interfaces to VM Network Interfaces .

### Software Requirements for Virtual CME

Install the appropriate Cisco IOS image router and configure a working VoIP network. See Install Virtual CME for more information. Cisco IOS XE Gibraltar 16.10.1a is the minimum IOS version that supports virtual CME.

Obtain the relevant license for the router platform. See Licensing Requirements for more information.

Virtual CME is validated and supported only on the Cisco CSR 1000v Series Cloud Services Router .

## Protocol Support

The endpoints with the following protocols are supported on virtual CME:

SIP—All SIP endpoints that are supported on Unified CME. For information on the endpoints supported on Unified CME, see Virtual Cisco Unified Communications Manager Express 12.5 Supported Firmware, Platforms, Memory, and Voice Products .

SCCP—Only Analog Voice Gateways, such as Cisco VG310, VG320, and VG350 are supported as SCCP endpoints on virtual CME.

Mixed Deployment (SIP and VG acting as SCCP endpoints). SCCP phones are not supported with virtual CME.

## Feature Support for Virtual CME

Virtual CME supports most of the features that are supported by Unified CME. Due to the physical architecture of the router
                           platform, the following features are not available with virtual CME:

Hardware Conference (Due to the limitation in supporting the PVDM hardware)

Transcoding (Due to the limitation in supporting the PVDM hardware)

Physical Voice Ports

The following phone features are not supported by virtual CME:

Music On Hold Groups

cBarge

Hold and Remote Resume with Shared Line (not supported for Analog VG endpoints)

Multicast MOH is not supported for SIP or Analog VG endpoints.

Live MOH is not supported for SIP or Analog VG endpoints.

### Feature Support

All SIP endpoints supported by Unified CME, including the Cisco IP Phone 7800 Series and Cisco 8800 Series IP Phones, are
                              supported by virtual CME. SCCP is only supported for use with Cisco VG 300 Series Analog Voice Gateways (VG310, VG320, and
                              VG350) only.

For detailed feature support information on virtual CME for SIP endpoints and Cisco VG300 Series Analog Voice Gateways (SCCP),
                              see Cisco Unified Communications Manager Express Platform Protocol Compatibility Matrix .

For more information on memory and platform recommendations for virtual CME, see Virtual Cisco Unified Communications Manager Express 12.5 Supported Firmware, Platforms, Memory, and Voice Products .

## CLI Support on Virtual CME

Virtual CME does not support the hardware conferencing-related CLI commands available on Unified CME.

The following CLI commands cannot be configured on virtual CME:

Within telephony-service configuration mode:

conference hardware

fxo hook-flash

Virtual CME does not support any of the sdspfarm related commands that are supported in Unified CME. Some of the examples are:

sdspfarm units number

sdspfarm conference mute-on mute-ondigits mute-off mute-off-digits

sdspfarm tag number device-name

Within voice register global configuration mode:

conference hardware

Within ephone-dn configuration mode:

conference ad-hoc | meetme

Within global configuration mode:

call-manager-fallback

## Restrictions of Virtual CME

All caveats, restrictions, and limitations of Cisco IOS XE Gibraltar 16.12.1a are applicable to virtual CME.

Only Unified CME features supported by Cisco IOS XE Fuji 16.9.1 (Unified CME 12.3) are available on virtual CME.

As DSP or voice interface hardware is not available for the CSR 1000V or the CSR 8000V, related Unified CME features such
                                 as transcoding and hardware conferencing are not supported on virtual CME.

NIM-based Analog or Digital PSTN Trunks are not supported.

No support for colocation with CUBE.

## Install Virtual CME

Use the CSR1000V or C8000V OVA application file (available from software.cisco.com) to deploy a new virtual instance directly
                           in VMware ESXi. For details about how to perform the deployment, see Installing the Cisco CSR 1000v in VMware ESXi Environments and Installing Catalyst 8000V in VMware ESXi Environment .

Explicit subscription of CPUs and Memory is required while deploying OVA provided by Cisco CSR 1000V or C8000V series.

## Licensing Requirements

Virtual CME offers the same licensing options that are available for Unified CME.

To allow the configuration of virtual CME:

Enable an APPX or AX license on a Cisco CSR 1000v Series Cloud Services Router .

Enable a DNA Advantage subscription on a C8000V series.

The licensing options for virtual CME on the router platform are available under the CLI command license boot level :

```
Router(config)#license boot level ?
  appx      Enable appx license
  ax        Enable ax(ipb+sec+appx) license
  ipbase    Enable ipbase license
  security  Enable security license
```

For virtual CME, throughput license suitable for the number of calls and other traffic processed by the router should be selected.
                           For information on throughput licenses, see Changing Throughput Licenses .

Install Cisco Smart License for virtual CME. Cisco Smart License for virtual CME is enabled with the same entitlement tags
                           that are assigned for Unified CME.

For more information on licensing options available for Unified CME, see Licensing .

For detailed steps about how to install Cisco CSR 1000V Licenses or C8000V series, see Installing Cisco CSR 1000V Licenses and Cisco Catalyst 8000V Licensing .

## Enable Virtual CME

Perform the following steps to enable virtual CME.

### Before you begin

Cisco CSR 1000v Series Cloud Services Router or C8000V series.

Virtual CME license. See Licensing Requirements .

Mandatory hardware and software. See Hardware Requirements for Virtual CME and Software Requirements for Virtual CME .

Acceptance of End User License Agreement (EULA).

### SUMMARY STEPS

- enable

- configure terminal

- voice register global

- mode cme

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Router# enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Router# configure terminal
```

Enters global configuration mode.

Step 3

voice register global

### Example:

```
Router(config)# voice register global
```

Enters voice register global configuration mode to set parameters for all supported SIP phones in virtual CME.

Step 4

mode cme

### Example:

```
Router(config-register-global)# mode cme
```

Enables mode for provisioning SIP phones in Unified CME.

Step 5

end

### Example:

```
Router(config-register-global)# end
```

Returns to privileged EXEC mode.

## Example for Cisco VG300 Series Registration as SCCP Endpoint with Virtual CME

Cisco VG300 Series Voice Gateways support Skinny Client Control Protocol (SCCP) registration with virtual CME for Cisco IOS
                              XE Gibraltar 16.10.1a or later releases.

The analog phone or fax machine is connected to the VG350’s Foreign Exchange Station (FXS) port. The VG350 is registered to
                              virtual CME through SCCP and communicates to the public switched telephone network (PSTN) provider through a Foreign Exchange
                              Office (FXO) port.

```
hostname GW-VG350
!
interface GigabitEthernet0/0
 ip address 10.8.1.10 255.255.255.0
 duplex auto
 speed auto
 !--- For modem or fax support using NSE based switchover.

voice-port 2/0
caller-id enable
!
voice-port 2/23
caller-id enable
!
!--- Set source interface of SCCP packets. Also determines which MAC address is used to register to vCME.

sccp local GigabitEthernet0/0

!--- Set address of SCCP agent, must match the IP source address of vCME.

sccp ccm 10.8.1.2 identifier 1 version 7.0
sccp
!
sccp ccm group 1

!--- Associate SCCP agent with CCM group.

  associate ccm 1 priority 1
!

!--- Associate STCAPP to CCM Group

stcapp ccm-group 1
stcapp
!
!--- Enable STCAPP on voice port.
 
dial-peer voice 1000 pots
 service stcapp 
 port 2/0
!
dial-peer voice 1023 pots
 service stcapp
 port 2/23
!
```

```
hostname VCME
!
telephony-service
 
 ip source-address 10.8.1.2 port 2000
 create cnf-files version-stamp Jan 01 2002 00:00:00
!
ephone-dn  8  dual-line
 number 4441 secondary 9191114441
 description vg350-2/0
 name Joe
!
ephone-dn  9  dual-line
 number 4442
 description vg350-2/23
 name Jane
 call-forward busy 5200
 call-forward noan 5200 timeout 10
!
ephone-dn  20
 number 8000....

!
ephone-dn  21
 number 8001....

ephone  5
 mac-address C863.9018.0417
 type anl 
 button  1:9
!
!--- phone for VG350 port 2/0.

ephone  8
 mac-address C863.9018.0400
 type anl
 button  1:8
```

### MAC Address Convention

After configuring the Analog Voice Gateway, enable the command show stcapp device summary to display the output summary with MAC address of all voice ports, as follows:

```
VCME#show stcapp device summary
Total Devices: 3
Total Calls in Progress: 0
Total Call Legs in Use: 0

Port Device Device Call Dev Directory Dev
Identifier Name State State Type Number Cntl
---------- --------------- -------- ------------- ------- ----------- ----
0/0/0 AN6549AEBB58000 IS IDLE ALG 6901 CME
0/0/1 AN6549AEBB58001 IS IDLE ALG 6902 CME
0/0/2 AN6549AEBB58002 IS IDLE ALG 6903 CME
Router_VG350#
```

The MAC address of the voice ports can be identified by removing the first three characters of the Device Name displayed in
                              the show stcapp device summary output. For example, the MAC address of the device with Device Name AN6549AEBB58000 is 549A.EBB5.8000.

```
VCME#show run | sec ephone
ephone 1
mac-address 549A.EBB5.8000
max-calls-per-button 2
type anl
button 1:5
ephone 2
mac-address 549A.EBB5.8001
max-calls-per-button 2
type anl
button 1:6
ephone 3
mac-address 549A.EBB5.8002
max-calls-per-button 2
type anl
button 1:7
Router_VCME#
```

## Feature Information for Virtual   CME

The following table provides release information about the feature or features described in this module. This table lists
                              only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                              subsequent releases of that software release train also support that feature.

Feature Name

Unified CME Version

Modification

Virtual CME

14.1

Support introduced for Virtual CME on C8000V series.

Virtual CME

12.5

Support introduced for Virtual CME on Cisco CSR 1000v Series Cloud Services Router .

| Note | When upgrading to C8000V software from a CSR1000V release, an existing throughput configuration will be reset to a maximum
                                       of 250 Mbps. Install an HSEC authorization code, which you can obtain from your Smart License account, before reconfiguring
                                       your required throughput level. |
|---|---|

| Note | For more information on the requirements on supported hypervisors, see CSR1000V Data Sheets and Cisco Catalyst 8000V Edge Software Data Sheet . |
|---|---|

| Resource Profiles | vCPU | Memory | Cisco UCS | Hypervisor | Number of Devices Registered to Virtual CME | Number of Active Calls Supported on Virtual CME |
|---|---|---|---|---|---|---|
| Small | 1 | 4 | UCSC-C240-M5SX | ESXi 6.5.0 | 450 | 113 |
| Medium | 2 | 4 |
| Large | 4 | 4 |
| Large plus Extra RAM | 4 | 8 |

| Note | Virtual CME is validated and supported only on the Cisco CSR 1000v Series Cloud Services Router . |
|---|---|

| Note | Explicit subscription of CPUs and Memory is required while deploying OVA provided by Cisco CSR 1000V or C8000V series. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Router# enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Router# configure terminal | Enters global configuration mode. |
| Step 3 | voice register global Example: Router(config)# voice register global | Enters voice register global configuration mode to set parameters for all supported SIP phones in virtual CME. |
| Step 4 | mode cme Example: Router(config-register-global)# mode cme | Enables mode for provisioning SIP phones in Unified CME. |
| Step 5 | end Example: Router(config-register-global)# end | Returns to privileged EXEC mode. |

| Feature Name | Unified CME Version | Modification |
|---|---|---|
| Virtual CME | 14.1 | Support introduced for Virtual CME on C8000V series. |
| Virtual CME | 12.5 | Support introduced for Virtual CME on Cisco CSR 1000v Series Cloud Services Router . |