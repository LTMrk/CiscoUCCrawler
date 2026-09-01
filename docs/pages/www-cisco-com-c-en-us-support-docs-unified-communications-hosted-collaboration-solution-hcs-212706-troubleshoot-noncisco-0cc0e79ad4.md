---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-hosted-collaboration-solution-hcs-212706-troubleshoot-noncisco-0cc0e79ad4
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/hosted-collaboration-solution-hcs/212706-troubleshoot-noncisco-device-shown-on-pc.html
retrieved_at: 2026-09-01T14:58:43.352301+00:00
---

Troubleshoot NonCisco Device shown on PCA 11

# Troubleshoot NonCisco Device shown on PCA 11

### Download Options

Updated: January 30, 2018

Document ID: 212706

Contents

## Contents

## Introduction

This document describes how to fix inventory Prime Collaboration Assurance (PCA) issues while adding the Cisco Unified Communications Manager (CUCM) and Prime License Manager (PLM). The inventory shows the device as Non Cisco whereas it is a CUCM application or PLM.

Contributed by Michal Myszor and Andrea Cingolani, Cisco TAC Engineers.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document applies to:

- PCA 11.X Managed Service Provider mode (MSP)

- Hosted Collaboration Mediation Fulfillment (HCM-F) 10.6.X

- Cisco Unified Communications Manager (CUCM) 11.5.X

- Standalone PLM 11.5.X

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, make sure that you understand the potential impact of any command.

## Problem

The CUCM device is shown as Non Cisco on the inventory page or in the device view when PCA cannot determine the device type based on SNMP queries.

PCA Inventory shows :

Same is presented on Device 360 view:

AccessLevelDiscovery log shows:

```
12-Sep-2017|15:25:43.003|DEBUG|AccessLevelDiscovery|pool-4-thread-4|work() : Starting Access Level Discovery for device  10.48.55.29
12-Sep-2017|15:25:43.003|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.AbstractDiscoveryStage|updateStatusReason|41| Later Error Index for device 10.48.55.29 is 1022 Old Message 
12-Sep-2017|15:25:43.003|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.AbstractDiscoveryStage|updateStatusReason|94| Error Index for device 10.48.55.29 is 1022 New Message Discovery in progress.
12-Sep-2017|15:25:43.003|DEBUG|AccessLevelDiscovery|pool-4-thread-4|probeAccessLevel() : Started for device  10.48.55.29
12-Sep-2017|15:25:43.003|DEBUG|AccessLevelDiscovery|pool-4-thread-4|probeAccessLevel() : Matching credentials for  10.48.55.29
12-Sep-2017|15:25:43.003|ERROR|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceAccessLevelDiscovery$MyWorkItem|getFinalDeviceCredentialsList|709| Ignoring the DEFAULT profile as the snmp community string is not provided.
12-Sep-2017|15:25:43.005|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceAccessLevelDiscovery$MyWorkItem|getFinalDeviceCredentialsList|760| probeAccessLevel() : CmDevice Credentials List size : 0
12-Sep-2017|15:25:43.006|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceAccessLevelDiscovery$MyWorkItem|probeAccessLevel|231| Before classificationOfDeviceType,  device credential id is 6429244
12-Sep-2017|15:25:43.007|DEBUG|AccessLevelDiscovery|pool-4-thread-4|probeAccessLevel() : isDeviceTypeReDiscoveryEnabled flag has set to true or mode is MSP -  10.48.55.29  device type is re-initilize to Unknown.
12-Sep-2017|15:25:43.007|DEBUG|AccessLevelDiscovery|pool-4-thread-4|probeAccessLevel() : ******* CmDevice Type Classification - STARTS [ 10.48.55.29 ]******* 12-Sep-2017|15:25:43.007|DEBUG|AccessLevelDiscovery|pool-4-thread-4|probeAccessLevel() : DeviceType is null/Other/Unknown for device  10.48.55.29
12-Sep-2017|15:25:43.007|DEBUG|AccessLevelDiscovery|pool-4-thread-4|probeAccessLevel() : Running device type classification for device  10.48.55.29
12-Sep-2017|15:25:43.007|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceTypeGeneratorManager|getDeviceType|167| getDeviceType() : For device 10.48.55.29 - Find the device Type
12-Sep-2017|15:25:43.007|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceTypeGeneratorManager|getDeviceType|169| getDeviceType() : For device 10.48.55.29; DC PROFILE NAME : 10.48.55.29
12-Sep-2017|15:25:43.007|INFO |AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceTypeGeneratorManager|getDeviceType|217| DC Id: 6429244
12-Sep-2017|15:25:43.008|INFO |AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.access.DeviceUtil|getSysOID|759| DeviceUtil.getSysOID:Before invoking PAL for SysOID10.48.55.29
12-Sep-2017|15:25:43.077|INFO |AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.access.DeviceUtil|getSysOID|766| DeviceUtil.getSysOID:After involking PAL: sysOID =1.3.6.1.4.1.9.1.1348 Ip Address 10.48.55.29
12-Sep-2017|15:25:43.107|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceTypeGeneratorManager|getDeviceType|240| getDeviceType(): SysOID and SysDescr are fetched from device 10.48.55.29
12-Sep-2017|15:25:43.107|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceTypeGeneratorManager|getDeviceType|241| getDeviceType(): SysOID   : 1.3.6.1.4.1.9.1.1348
12-Sep-2017|15:25:43.107|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceTypeGeneratorManager|getDeviceType|242| getDeviceType(): SysDescr : Linux release:2.6.32-431.20.3.el6.x86_64 machine:x86_64
12-Sep-2017|15:25:43.108|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceTypeGeneratorManager|getDeviceType|268| Device type of profile is null
12-Sep-2017|15:25:43.108|INFO |AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.impl.DeviceSwitchType|getDeviceType|17| Checking is Switch Type check for 10.48.55.29
12-Sep-2017|15:25:43.108|INFO |AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.impl.DeviceRouterType|getDeviceType|17| Checking is Router Type for 10.48.55.29
(...)
12-Sep-2017|15:25:44.548|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.impl.DeviceUC500SeriesType|getDeviceType|19| DeviceUC500SeriesType:getDeviceType
12-Sep-2017|15:25:44.548|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.impl.DeviceUC500SeriesType|getDeviceType|26| DeviceGroup- Call Control : DeviceName - Cisco CallManager
12-Sep-2017|15:25:44.637|ERROR|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.impl.DeviceESXType|checkifESX|65| Exception in checkIfESXnull
12-Sep-2017|15:25:44.692|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.impl.DeviceCIMType|checkIfCIM|61| checkIfCIM ()
12-Sep-2017|15:25:45.390|INFO |AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.impl.DeviceSOFTSWITCHType|getDeviceType|42| From DeviceSOFTSWITCHType
12-Sep-2017|15:25:45.390|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.impl.DeviceSOFTSWITCHType|checkIfSoftSwitch|60| checkIfSoftSwitch ()
12-Sep-2017|15:25:46.070|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.impl.DeviceSOFTSWITCHType|getDeviceType|51| Device 10.48.55.29 is not a SOFTSWITCH
12-Sep-2017|15:25:46.070|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.impl.DeviceNonCiscoType|getDeviceType|32| DeviceNonCiscoType: device Type is Non Cisco 12-Sep-2017|15:25:46.139|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceTypeGeneratorManager|getDeviceType|175| probeAccessLevel() : Found DeviceType NONCISCO for device 10.48.55.29
12-Sep-2017|15:25:46.139|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceAccessLevelDiscovery$MyWorkItem|classificationOfDeviceType|339| probeAccessLevel() : ******* CmDevice Type Classification - ENDS ******* 12-Sep-2017|15:25:46.140|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceAccessLevelDiscovery$MyWorkItem|probeAccessLevel|244| After classificationOfDeviceType,  device credential id is 6429244
12-Sep-2017|15:25:46.140|DEBUG|AccessLevelDiscovery|pool-4-thread-4|com.cisco.nm.emms.inv.access.core.DeviceAccessLevelDiscovery$MyWorkItem|probeAccessLevel|251| After resetting to original  id,  device credential id  is 6429244
12-Sep-2017|15:25:46.140|DEBUG|AccessLevelDiscovery|pool-4-thread-4|probeAccessLevel() : DC  10.48.55.29  with type  null NOT matched CmDevice  10.48.55.29  with type NONCISCO
```

## Solution

Check whether the SNMP service runs on UC application.

Note : Cisco CUCM has two SNMP services.

```
SNMP Master Agent[STARTED]
(...)
Cisco CallManager SNMP Service[STOPPED]  Service Not Activated
```

Cisco CallManager SNMP Service is responsible for answering Cisco specific MIB SNMP queries

The SNMP service down is already fixed in PCA 11.6, and SNMP service being down is suggested:

```
11-Sep-2017|12:56:52.752|DEBUG|AccessLevelDiscovery|pool-6-thread-10|com.cisco.nm.emms.inv.AbstractDiscoveryStage|updateStatusReason|109| Error Index for device 10.48.50.59 is 1003 New Message SNMP timed out. Probable reasons could be: 1. SNMP service not enabled in the device. 2. SNMP credentials do not match. 3. Firewall settings blocking the port. Refer the Install and Upgrade guide for the exact ports to be unblocked.
```

## Problem

The PLM device is shown as Non Cisco on the inventory page.

## Solution

- Select the PLM server in the Inventory page and suspend the device.

- Delete the device from the PCA inventory.

- Delete any community string added in the PLM via Command Line Interface (CLI):

utils snmp config 1/2c community-string delete

4. Add the device back in the PCA with the use of operating system platform crendential (OS PLM CLI) into the HTTP(s) PCA device credential field as shown in the image.

### Contributed by Cisco Engineers

Michal Myszor

Andrea Cingolani

### This Document Applies to These Products

- Hosted Collaboration Solution (HCS)