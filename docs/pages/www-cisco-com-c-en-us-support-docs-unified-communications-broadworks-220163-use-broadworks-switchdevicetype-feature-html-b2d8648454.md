---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-broadworks-220163-use-broadworks-switchdevicetype-feature-html-b2d8648454
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/broadworks/220163-use-broadworks-switchdevicetype-feature.html
retrieved_at: 2026-09-07T13:02:16.080528+00:00
---

Use BroadWorks switchDeviceType Feature

# Use BroadWorks switchDeviceType Feature

### Download Options

Updated: January 31, 2023

Document ID: 220163

Contents

## Contents

## Introduction

This document describes the use of the BroadWorks switchDeviceType feature.

## Prerequisites

### Requirements

There are no specific requirements for this document.

### Components Used

This document is not restricted to specific software and hardware versions.

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Background Information

From BroadWorks, release 23.0 and later, a mechanism was introduced to switch a device profile type from one to another.

## Usage Options

The switchDeviceType can be performed from either the BWCLI or the oci-p command, SystemDeviceManagementSwitchDeviceTypeDeviceRequest .

### BWCLI

```
AS_CLI/System/Device/IpDeviceMgmt> help switchDeviceType This command is used to switch device profiles from one device type to another. Parameters description: attribute : The name of the attribute that scopes the command. system : This parameter specifies the switch command is issued at the system level. fromDeviceType : This parameter specifies the original device type. toDeviceType : This parameter specifies the destination device type. serviceProvider : This parameter specifies the switch command is issued at the service provider level. svcProviderId : This parameter specifies the ID of the service provider. group : This parameter specifies the switch command is issued at the group level. groupId : This parameter specifies the valid group within the service provider. systemDeviceProfile : This parameter specifies the switch command is issued for a single device profile at the system level. deviceName : This parameter specifies the name of the device profile. svcProvDeviceProfile: This parameter specifies the switch command is issued for a single device profile at the service provider level. groupDeviceProfile : This parameter specifies the switch command is issued for a single device profile at the group level. ====================================================================== switchDeviceType <attribute>, Choice = {system, serviceProvider, group, systemDeviceProfile, svcProvDeviceProfile, groupDeviceProfile} system: <fromDeviceType>, String {1 to 40 characters} <toDeviceType>, String {1 to 40 characters} serviceProvider: <svcProviderId>, String {1 to 30 characters} <fromDeviceType>, String {1 to 40 characters} <toDeviceType>, String {1 to 40 characters} group: <svcProviderId>, String {1 to 30 characters} <groupId>, String {1 to 30 characters} <fromDeviceType>, String {1 to 40 characters} <toDeviceType>, String {1 to 40 characters} systemDeviceProfile: <deviceName>, String {1 to 40 characters} <toDeviceType>, String {1 to 40 characters} svcProvDeviceProfile: <svcProviderId>, String {1 to 30 characters} <deviceName>, String {1 to 40 characters} <toDeviceType>, String {1 to 40 characters} groupDeviceProfile: <svcProviderId>, String {1 to 30 characters} <groupId>, String {1 to 30 characters} <deviceName>, String {1 to 40 characters} <toDeviceType>, String {1 to 40 characters}
```

### OCI-P Command

```
<?xml version="1.0" encoding="ISO-8859-1"?> <BroadsoftDocument protocol="OCI" xmlns="C" xmlns:xsi=" http://www.w3.org/2001/XMLSchema-instance "> <sessionId xmlns="">SESSIONID</sessionId> <command xsi:type="SystemDeviceManagementSwitchDeviceTypeDeviceRequest" xmlns=""> <svcProviderId>YOUR ENT/SP</svcProviderId> <groupId>YOUR GROUP</groupId> <deviceName>ORIGINAL DEVICE TYPE</deviceName> <toDeviceType>NEW DEVICE TYPE</toDeviceType> </command> </BroadsoftDocument>
```

### XML Schema

```
<xs:complexType name="SystemDeviceManagementSwitchDeviceTypeDeviceRequest"> <xs:annotation> <xs:appinfo> <bwAppInfo bwtag="_1843b06e76464254bf146a91622df7b4"/> <asDataModeSupported>true</asDataModeSupported> <amplifyDataModeSupported>true</amplifyDataModeSupported> <xsDataModeSupported>true</xsDataModeSupported> </xs:appinfo> <xs:documentation> Switch the device type for a specified device. To switch a system level device profile, serviceProviderId and groupId should not be present. To switch a service provider level device profile, only serviceProviderId should be specified. To switch a group level device profile, serviceProviderId and groupId should specified. The response is either a SuccessResponse or an ErrorResponse. </xs:documentation> </xs:annotation> <xs:complexContent> <xs:extension base="core:OCIRequest"> <xs:sequence> <xs:choice minOccurs="0"> <xs:element name="serviceProviderId" type="ServiceProviderId"/> <xs:sequence> <xs:element name="svcProviderId" type="ServiceProviderId"/> <xs:element name="groupId" type="GroupId"/> </xs:sequence> </xs:choice> <xs:element name="deviceName" type="AccessDeviceName"/> <xs:element name="toDeviceType" type="AccessDeviceType"/> </xs:sequence> </xs:extension> </xs:complexContent> </xs:complexType>
```

## Lab Example

### BWCLI Example

For this example, you switch a groupDeviceProfile from Poly_VVX_D230 device type to the Cisco-CP-78xx-88xx-68xx-3PCC device type.

- Add a group device profile Poly_VVX_D230_Switch and assign the device Poly_VVX_D230:

```
AS_CLI/System/Device/IpDeviceMgmt> add pws_ent pws_grp Poly_VVX_D230_Switch Poly_VVX_D230 macAddress 678678678678
```

- Perform the switch of profile Poly_VVX_D230_Switch to  Cisco-CP-78xx-88xx-68xx-3PCC:

```
AS_CLI/System/Device/IpDeviceMgmt> switchDeviceType groupDeviceProfile pws_ent pws_grp Poly_VVX_D230_Switch Cisco-CP-78xx-88xx-68xx-3PCC ...Done [Request for switch is being processed; Rebuild triggered for device type: Cisco-CP-78xx-88xx-68xx-3PCC, please refer to DMEventQueues for completion status.]
```

## Log Example

This is a log example for this request type seen from the PSLog.

```
2022.05.26 09:34:57:686 EDT | Info | OCI-P | BCCT Worker #0 Received the following request from: 127.0.0.1:56212 <?xml version="1.0" encoding="ISO-8859-1"?> <BroadsoftDocument protocol="OCI" xmlns="C" xmlns:xsi=" http://www.w3.org/2001/XMLSchema-instance "> <sessionId xmlns="">16535720065220.14787900206648874</sessionId> <command xsi:type="SystemDeviceManagementSwitchDeviceTypeDeviceRequest" xmlns=""> <svcProviderId>pws_ent</svcProviderId> <groupId>pws_grp</groupId> <deviceName>Poly_VVX_D230_Switch</deviceName> <toDeviceType>Cisco-CP-78xx-88xx-68xx-3PCC</toDeviceType> </command> </BroadsoftDocument> 2022.05.26 09:34:57:711 EDT | FieldDebug | Generic | BCCT Worker #0 OCI Transaction com.broadsoft.oci.transactions.system.SystemDeviceManagementSwitchDeviceTypeDeviceTransaction write5193 executed. User: Default Administrator (admin) Authorization Level: System Start Time: 2022.05.26 09:34:57:687 EDT End Time: 2022.05.26 09:34:57:711 EDT Duration: 24 ms 2022.05.26 09:34:57:711 EDT | Info | OCI-P | BCCT Worker #0 | admin TO 127.0.0.1:56212 <?xml version="1.0" encoding="ISO-8859-1"?> <BroadsoftDocument protocol="OCI" xmlns="C" xmlns:xsi=" http://www.w3.org/2001/XMLSchema-instance "> <sessionId xmlns="">16535720065220.14787900206648874</sessionId> <command echo="" xsi:type="c:SuccessResponse" xmlns:c="C" xmlns=""/> </BroadsoftDocument>
```

## Related Information

- DeviceProfileTypeCustomizationEnhancements-AS-FD

- Cisco Technical Support & Downloads

### Revision History

2.0

31-Jan-2023

Initial Release

1.0

30-Jan-2023

Initial Release

### Contributed by Cisco Engineers

Paul Sanderson

Cisco Technical Consulting Engineer

### This Document Applies to These Products

- BroadWorks

| Revision | Publish Date | Comments |
|---|---|---|
| 2.0 | 31-Jan-2023 | Initial Release |
| 1.0 | 30-Jan-2023 | Initial Release |