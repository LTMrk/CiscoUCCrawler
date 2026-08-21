---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-bd2fdb4ece
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_serviceability-api_1501.html
retrieved_at: 2026-08-21T16:48:16.289012+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Serviceability API

## Chapter: Serviceability API

- Serviceability API

- Serviceability API

- System Validation                              	 Rules

# Serviceability API

## Serviceability API

Use the Serviceability API to view information about the system, such as API statistics and version information.

### URL

https://<server>/unifiedconfig/config/serviceability

### Operations

get : Returns serviceability information.

Query parameters:

category:   Use this query parameter to reduce the number of parameters returned. The values allowed match the names of the
                                                parameters. For example, https://<server>/unifiedconfig/config/serviceability? category=systemValidationStatus&category=capacityInfo .

### Parameters

currentTime: The time at which this web request was made.

instanceName: The name of the active Unified CCE instance.

version: Version information for Packaged CCE. Includes the following parameters:

buildDate: The date the application was built.

buildVersion: The build number of the application.

esVersion: The engineering special (ES) version.

maintenanceVersion: The maintenance version.

majorVersion: The major version.

minorVersion: The minor version.

srVersion: The SR version.

ucceVersion: Version information for Unified CCE. Includes the same parameters listed for the version parameter, above, as
                                    well as:

versionString: Textual representation of the Unified CCE version.

patchInfos: A collection of patch information, including majorVersion, minorVersion, maintenanceVersion, srVersion, and esVersion
                                          parameters.

capacityInfo:  A collection of capacityRules indicating if the capacity limits are valid. Each rule contains the following
                                    parameters:

name: The name of the capacity rule.

max: The maximum number of items allowed for the rule.

actual: The current number of items configured for the rule.

systemValidationStatus: A collection of validationRules that show the potential errors regarding system configuration. For
                                    more information on the rules, see System Validation Rules. Each rule contains the following parameters:

name: The name of the rule.

isValid: Indicates if the rule is passing. Values are true/false.

min: The minimum number of items required to match for this rule.

max: The maximum number of items required to match for this rule.

actual: The current number of items configured that match this rule.

### Example Get Response

```
<Serviceability>
  <currentTime>Tue Nov 29 04:00:45 EST 2011</currentTime>
  <instanceName>instance</instanceName>
  <version>
    <majorVersion>9</majorVersion>
    <minorVersion>0</minorVersion>
    <maintenanceVersion>0</maintenanceVersion>
    <srVersion>0</srVersion>
    <esVersion>0</esVersion>
    <buildVersion>1</buildVersion>
    <buildDate>1969-12-31T19:00:00-05:00</buildDate>
  </version>
  <ucceVersion>
    <majorVersion>9</majorVersion>
    <minorVersion>5</minorVersion>
    <maintenanceVersion>3</maintenanceVersion>
    <srVersion>0</srVersion>
    <esVersion>0</esVersion>
    <buildVersion>375</buildVersion>
    <versionString>9.5.3.0.0.375</versionString>
    <patchInfos>
      <patchInfo>
        <majorVersion>9</majorVersion>
        <minorVersion>5</minorVersion>
        <maintenanceVersion>3</maintenanceVersion>
        <srVersion>0</srVersion>
        <esVersion>0</esVersion>
      </patchInfo>
      <patchInfo>
        <majorVersion>9</majorVersion>
        <minorVersion>5</minorVersion>
        <maintenanceVersion>2</maintenanceVersion>
        <srVersion>0</srVersion>
        <esVersion>0</esVersion>
      </patchInfo>
    </patchInfos>
  </ucceVersion>
</Serviceability>
```

## System Validation
                        	 Rules

The system
                              		  validation rules show the potential errors regarding system configuration.

Rule

Explanation

ECC_VARIABLES_CTI_SIZE

ECC Variables: Total bytes required for enabled variables in CTI Server must not exceed 2500.

CMS_NODE_DISABLED

CMS
                                          						Node: Configuration Management Service (CMS) Node and Agent Re-skilling Web
                                          						Tool must be disabled using Unified CCE Web Setup.

ENTERPRISE_SERVICE_COUNT

Enterprise Services: No Enterprise Services may be configured.

PCCE_MR_PIM_COUNT

Peripheral: Exactly 4 Media Routing Peripherals must be
                                          						configured on each Media Routing PG. This rule counts the quantity that are not
                                          						compliant.

DESK_SETTING_WITH_RING_NO_ANSWER _SET_COUNT

Agent
                                          						Desk Settings: Ring No Answer Timer must not be set.

ENT_SG_COUNT

Skill
                                          						Groups: No Enterprise Skill Groups may be configured.

ENT_SG_MEMBER_COUNT

Skill
                                          						Groups: No Enterprise Skill Group Members may be configured.

ENT_ROUTE_COUNT

Enterprise Routes: No Enterprise Routes may be configured.

ENT_ROUTE_MEMBER_COUNT

Enterprise Routes: No Enterprise Route Members may be
                                          						configured.

PCCE_CUCM_PG_COUNT

Peripheral Gateway: There must be at least 1 Unified CM
                                          						Peripheral Gateway configured but no more than 11.

VRU_PG_COUNT

Peripheral Gateway: There must be at least 1 VRU Peripheral
                                          						Gateway configured but no more than 11.

MR_PG_COUNT

Peripheral Gateway: There must be at least one Media Routing
                                          						Peripheral Gateway configured but no more than 11.

MULTICHANNEL_COUNT

Peripheral: Exactly 1 MR PIM must be configured with the
                                          						Enterprise Name of Multichannel .

OUTBOUND_COUNT

Peripheral: Exactly 1 MR PIM must be configured with the
                                          						Enterprise Name of Outbound .

UNSUPPORTED_PG_COUNT

Peripheral Gateway: Only PGs with CUCM, MediaRouting, and VRU
                                          						client types are supported. This rule counts the quantity that are not
                                          						compliant.

SERVICE_MEMBER_COUNT

Service
                                          						Members: No Service Members may be configured.

TYPE10_NETWORK_VRU_COUNT

VRU:
                                          						Exactly 1 Type 10 Network VRU must be configured in the Network VRU Explorer.

TYPE10_NETWORK_VRU_MAP_COUNT

Peripheral Gateway: All VRU Peripherals must be configured on a
                                          						VRU PG and associated with the Type 10 Network VRU. This rule counts the
                                          						quantity that are not compliant.

UCM_PIM_COUNT

Peripheral: Exactly 1 Unified CM Peripheral must be configured
                                          						on each Unified CM PG in the Peripheral Explorer tool.

VRU_PIM_COUNT

Peripheral: Exactly 2 VRU Peripherals must be configured on each
                                          						VRU PG.

NOT_SKILL_GROUP_ROUTE_NAME_COUNT

Skill
                                          						Groups: All Skill Group records must have a corresponding Route record with the
                                          						same Enterprise Name as the Skill Group record.

ECC_VARIABLES_ENABLED_COUNT

ECC
                                          						Variables: ECC variables must be enabled in the System Information tool.

SERVICE_COUNT

Services: No Services may be configured.

TRANSLATION_ROUTE_COUNT

Translation Routes: No Translation Routes may be configured.

NIC_COUNT

NICs: No
                                          						NICs may be configured.

MRD_COUNT

Max
                                          						Media Routing Domains: The maximum number of Media Routing Domains is 20.

MEDIA_CLASS_COUNT

Max
                                          						Media Classes: The maximum number of Media Classes is 10.

NOT_PARTITIONED_COUNT

Partitioning: Partitioning must be disabled in the System
                                          						Information tool.

NON_NULL_SERVICE_LEVEL_COUNT

Service Level Threshold: The default service level must not be
                                          						set in the Peripheral Explorer tool. The default is set in the System
                                          						Information tool.

DEVICE_TARGET_COUNT

Device
                                          						Targets: No Device Targets can be configured.

CVP_LABEL_COUNT

VRU:
                                          						Each VRU PIM in the PG Explorer tool must have exactly 1 label with a length of
                                          						10 digits. This rule counts the number of VRU PIMs that are not compliant.

CUCM_LABEL_COUNT

CUCM
                                          						Routing Label: Each Unified CM Peripheral in the PG Explorer tool must have
                                          						exactly 1 label with length of 10 digits. This rule counts the number of
                                          						Unified CM Peripherals that are not compliant.

CORRELATION_ID_RANGE_COUNT

Correlation ID: The minimum and maximum correlation number in
                                          						the VRU section of the System Information tool must be 1001 and 9999
                                          						respectively.

NULL_FEATURE_SET_ID_COUNT

Feature Control Set: The Feature Control Set in the Customer
                                          						Definition of the ICM Instance Explorer must set to NONE.

ECC_FOR_CVP_COUNT

ECC
                                          						Variables: Exactly 9 Expanded Call Variables are required for CVP.

NETWORK_VRU_SCRIPT_COUNT

VRU:
                                          						There must be a Network VRU Script with the Enterprise Name of VXML_Server and the Script Name of GS,Server,V configured in the Network VRU Script tool.

DEFAULT_DESK_SETTING_COUNT

Agent
                                          						Desk Settings: Default_Agent_Desk_Setting must be set as the default Agent Desk
                                          						Settings for the CUCM PIM in the PG Explorer tool.

PCCE_APP_INSTANCE_MULTICHANNEL _COUNT

Multichannel Application Instance: An Application Instance must
                                          						be defined for Multichannel.

TYPE2_NETWORK_VRU_COUNT

VRU:
                                          						Exactly one Type 2 Network VRU must be configured in the Network VRU Explorer
                                          						tool.

PCCE_TYPE2_NETWORK_VRU_MAP_COUNT

Peripheral: Each MR PIM must be associated with the Type 2
                                          						Network VRU in the PG Explorer tool. This rule counts the quantity that are not
                                          						compliant.

DIALED_NUMBER_EXTERNAL_VOICE_COUNT

Dialed
                                          						Numbers: For each External Voice Dialed Numbers, there must be exactly 2 Dialed
                                          						Number records for each Dialed Number String, with one for each VRU PIM.

DIALED_NUMBER_MAP_COUNT

Dialed
                                          						Numbers: All Dialed Number records must not have an associated Region, ANI, and
                                          						must have a maximum of 1 Call Type associated in the Call Type Map.

AGENT_REAL_TIME_ENABLED_COUNT

Peripheral: Agent Reporting must be enabled on the Unified CM
                                          						Peripheral in the PG Explorer tool.

CUSTOMER_DEFINITION_COUNT

Customer Definition: Exactly 1 Customer Definition must be
                                          						configured in the ICM Instance Explorer.

CUSTOMER_DEFINITION_HAS_TYPE10 _NETWORK_VRU

Customer Definition: Exactly 1 Customer Definition must have a
                                          						Type 10 Network VRU selected in the ICM Instance Explorer.

DIALED_NUMBERS_REQUIRE _CUSTOMER_DEFINITION

Dialed
                                          						Numbers: No Dialed Number records can have the Customer set to None.

SCRIPT_VERSIONS_TO_RETAIN

Script
                                          						Versions to Retain: The number of script versions to retain must be between 1
                                          						and 100, inclusively.

NON_CUSTOM_APP_GATEWAY_COUNT

Application Gateway: No Application Gateways with application
                                          						gateway type other than Custom Gateway may be configured.

DATABASE_LOOKUP_COUNT

Database Lookups: No Database Lookups may be configured.

SCRIPT_VERSIONS_ALLOWED

Max
                                          						Script Versions: The maximum number of script versions allowed is 100 (minimum
                                          						is 1).

OEM_CP_MATCHES_DB_COLLATION

The system locale must be compatible with the database collation. The valid pairs are: cp437 / iso_1 (US English) and cp850
                                          / iso_1 (Other Latin derivatives). All other valid pairs must be identical strings: cp936 / cp936 (Chinese), cp866/cp866 (Russian),
                                          cp 932/cp932 (Japanese), and so on. For more information, see the Collation and Locale Settings for Localization section in
                                          the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide in the https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html .

AGENT_TARGETING_RULE

Each
                                          						Unified CM Peripheral must have exactly one agent targeting rule defined in
                                          						CCE. This rule counts the quantity that are not compliant.

| Rule | Explanation |
|---|---|
| ECC_VARIABLES_CTI_SIZE | ECC Variables: Total bytes required for enabled variables in CTI Server must not exceed 2500. |
| CMS_NODE_DISABLED | CMS
                                          						Node: Configuration Management Service (CMS) Node and Agent Re-skilling Web
                                          						Tool must be disabled using Unified CCE Web Setup. |
| ENTERPRISE_SERVICE_COUNT | Enterprise Services: No Enterprise Services may be configured. |
| PCCE_MR_PIM_COUNT | Peripheral: Exactly 4 Media Routing Peripherals must be
                                          						configured on each Media Routing PG. This rule counts the quantity that are not
                                          						compliant. |
| DESK_SETTING_WITH_RING_NO_ANSWER _SET_COUNT | Agent
                                          						Desk Settings: Ring No Answer Timer must not be set. |
| ENT_SG_COUNT | Skill
                                          						Groups: No Enterprise Skill Groups may be configured. |
| ENT_SG_MEMBER_COUNT | Skill
                                          						Groups: No Enterprise Skill Group Members may be configured. |
| ENT_ROUTE_COUNT | Enterprise Routes: No Enterprise Routes may be configured. |
| ENT_ROUTE_MEMBER_COUNT | Enterprise Routes: No Enterprise Route Members may be
                                          						configured. |
| PCCE_CUCM_PG_COUNT | Peripheral Gateway: There must be at least 1 Unified CM
                                          						Peripheral Gateway configured but no more than 11. |
| VRU_PG_COUNT | Peripheral Gateway: There must be at least 1 VRU Peripheral
                                          						Gateway configured but no more than 11. |
| MR_PG_COUNT | Peripheral Gateway: There must be at least one Media Routing
                                          						Peripheral Gateway configured but no more than 11. |
| MULTICHANNEL_COUNT | Peripheral: Exactly 1 MR PIM must be configured with the
                                          						Enterprise Name of Multichannel . |
| OUTBOUND_COUNT | Peripheral: Exactly 1 MR PIM must be configured with the
                                          						Enterprise Name of Outbound . |
| UNSUPPORTED_PG_COUNT | Peripheral Gateway: Only PGs with CUCM, MediaRouting, and VRU
                                          						client types are supported. This rule counts the quantity that are not
                                          						compliant. |
| SERVICE_MEMBER_COUNT | Service
                                          						Members: No Service Members may be configured. |
| TYPE10_NETWORK_VRU_COUNT | VRU:
                                          						Exactly 1 Type 10 Network VRU must be configured in the Network VRU Explorer. |
| TYPE10_NETWORK_VRU_MAP_COUNT | Peripheral Gateway: All VRU Peripherals must be configured on a
                                          						VRU PG and associated with the Type 10 Network VRU. This rule counts the
                                          						quantity that are not compliant. |
| UCM_PIM_COUNT | Peripheral: Exactly 1 Unified CM Peripheral must be configured
                                          						on each Unified CM PG in the Peripheral Explorer tool. |
| VRU_PIM_COUNT | Peripheral: Exactly 2 VRU Peripherals must be configured on each
                                          						VRU PG. |
| NOT_SKILL_GROUP_ROUTE_NAME_COUNT | Skill
                                          						Groups: All Skill Group records must have a corresponding Route record with the
                                          						same Enterprise Name as the Skill Group record. |
| ECC_VARIABLES_ENABLED_COUNT | ECC
                                          						Variables: ECC variables must be enabled in the System Information tool. |
| SERVICE_COUNT | Services: No Services may be configured. |
| TRANSLATION_ROUTE_COUNT | Translation Routes: No Translation Routes may be configured. |
| NIC_COUNT | NICs: No
                                          						NICs may be configured. |
| MRD_COUNT | Max
                                          						Media Routing Domains: The maximum number of Media Routing Domains is 20. |
| MEDIA_CLASS_COUNT | Max
                                          						Media Classes: The maximum number of Media Classes is 10. |
| NOT_PARTITIONED_COUNT | Partitioning: Partitioning must be disabled in the System
                                          						Information tool. |
| NON_NULL_SERVICE_LEVEL_COUNT | Service Level Threshold: The default service level must not be
                                          						set in the Peripheral Explorer tool. The default is set in the System
                                          						Information tool. |
| DEVICE_TARGET_COUNT | Device
                                          						Targets: No Device Targets can be configured. |
| CVP_LABEL_COUNT | VRU:
                                          						Each VRU PIM in the PG Explorer tool must have exactly 1 label with a length of
                                          						10 digits. This rule counts the number of VRU PIMs that are not compliant. |
| CUCM_LABEL_COUNT | CUCM
                                          						Routing Label: Each Unified CM Peripheral in the PG Explorer tool must have
                                          						exactly 1 label with length of 10 digits. This rule counts the number of
                                          						Unified CM Peripherals that are not compliant. |
| CORRELATION_ID_RANGE_COUNT | Correlation ID: The minimum and maximum correlation number in
                                          						the VRU section of the System Information tool must be 1001 and 9999
                                          						respectively. |
| NULL_FEATURE_SET_ID_COUNT | Feature Control Set: The Feature Control Set in the Customer
                                          						Definition of the ICM Instance Explorer must set to NONE. |
| ECC_FOR_CVP_COUNT | ECC
                                          						Variables: Exactly 9 Expanded Call Variables are required for CVP. |
| NETWORK_VRU_SCRIPT_COUNT | VRU:
                                          						There must be a Network VRU Script with the Enterprise Name of VXML_Server and the Script Name of GS,Server,V configured in the Network VRU Script tool. |
| DEFAULT_DESK_SETTING_COUNT | Agent
                                          						Desk Settings: Default_Agent_Desk_Setting must be set as the default Agent Desk
                                          						Settings for the CUCM PIM in the PG Explorer tool. |
| PCCE_APP_INSTANCE_MULTICHANNEL _COUNT | Multichannel Application Instance: An Application Instance must
                                          						be defined for Multichannel. |
| TYPE2_NETWORK_VRU_COUNT | VRU:
                                          						Exactly one Type 2 Network VRU must be configured in the Network VRU Explorer
                                          						tool. |
| PCCE_TYPE2_NETWORK_VRU_MAP_COUNT | Peripheral: Each MR PIM must be associated with the Type 2
                                          						Network VRU in the PG Explorer tool. This rule counts the quantity that are not
                                          						compliant. |
| DIALED_NUMBER_EXTERNAL_VOICE_COUNT | Dialed
                                          						Numbers: For each External Voice Dialed Numbers, there must be exactly 2 Dialed
                                          						Number records for each Dialed Number String, with one for each VRU PIM. |
| DIALED_NUMBER_MAP_COUNT | Dialed
                                          						Numbers: All Dialed Number records must not have an associated Region, ANI, and
                                          						must have a maximum of 1 Call Type associated in the Call Type Map. |
| AGENT_REAL_TIME_ENABLED_COUNT | Peripheral: Agent Reporting must be enabled on the Unified CM
                                          						Peripheral in the PG Explorer tool. |
| CUSTOMER_DEFINITION_COUNT | Customer Definition: Exactly 1 Customer Definition must be
                                          						configured in the ICM Instance Explorer. |
| CUSTOMER_DEFINITION_HAS_TYPE10 _NETWORK_VRU | Customer Definition: Exactly 1 Customer Definition must have a
                                          						Type 10 Network VRU selected in the ICM Instance Explorer. |
| DIALED_NUMBERS_REQUIRE _CUSTOMER_DEFINITION | Dialed
                                          						Numbers: No Dialed Number records can have the Customer set to None. |
| SCRIPT_VERSIONS_TO_RETAIN | Script
                                          						Versions to Retain: The number of script versions to retain must be between 1
                                          						and 100, inclusively. |
| NON_CUSTOM_APP_GATEWAY_COUNT | Application Gateway: No Application Gateways with application
                                          						gateway type other than Custom Gateway may be configured. |
| DATABASE_LOOKUP_COUNT | Database Lookups: No Database Lookups may be configured. |
| SCRIPT_VERSIONS_ALLOWED | Max
                                          						Script Versions: The maximum number of script versions allowed is 100 (minimum
                                          						is 1). |
| OEM_CP_MATCHES_DB_COLLATION | The system locale must be compatible with the database collation. The valid pairs are: cp437 / iso_1 (US English) and cp850
                                          / iso_1 (Other Latin derivatives). All other valid pairs must be identical strings: cp936 / cp936 (Chinese), cp866/cp866 (Russian),
                                          cp 932/cp932 (Japanese), and so on. For more information, see the Collation and Locale Settings for Localization section in
                                          the Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide in the https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html . |
| AGENT_TARGETING_RULE | Each
                                          						Unified CM Peripheral must have exactly one agent targeting rule defined in
                                          						CCE. This rule counts the quantity that are not compliant. |