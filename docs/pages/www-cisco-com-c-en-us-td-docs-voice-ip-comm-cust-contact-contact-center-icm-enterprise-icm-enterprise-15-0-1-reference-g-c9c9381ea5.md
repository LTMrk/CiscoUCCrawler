---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-reference-g-c9c9381ea5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/reference/guide/ucce-b-database-schema-handbook-for-cisco-unified-icm-contact-center-enterprise-release-1501/ucce_m_tables-by-group_15_0_1.html
retrieved_at: 2026-08-16T19:44:31.906486+00:00
---

Database Schema Handbook for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Database Schema Handbook for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: November 28, 2025

Chapter: Tables by Group

## Chapter: Tables by Group

# Tables by Group

## Overview

This section explains
                           		major areas of the schema. Tables are arranged in logical groups based on their
                           		domains and interrelationships.

For each section, you
                           		can find:

an illustration
                                 			 that maps the connections among tables in that group

links to detailed
                                 			 information on each individual table in the group

a link to the
                                 			 database rules for the group

For details on the
                           		columns in each table, see All Tables.

## Blended Agent
                        	 (Outbound Option)

This figure depicts
                           		the tables in the Blended Agent (Outbound Option) category and their
                           		connections.

In this graphic:

A single box
                                 			 represents a single table.

A stack of boxes
                                 			 represents several tables in another category of the schema.

A single arrowhead
                                 			 indicates a one-to-one relationship, and a double arrowhead indicates a
                                 			 one-to-many relationship.

To see database rules
                           		for tables in the Blended Agent group, see Blended Agent Tables (Outbound Option) .

Tables that hold Blended Agent
                              		  (Outbound Option) data are listed below.

## Business Hours

This figure depicts the tables in this category and their connections.

In this graphic:

A single box represents a single table.

A single arrowhead indicates a one-to-one relationship, and a double arrowhead indicates a one-to-many relationship.

A stack of boxes represents several tables in another category of the schema.

To see the database rules for these tables, see Business Hours Tables .

Tables in the Business Hours category include the following:

## Device

This
                           figure depicts the tables in this category and their connections.

In this graphic:

A single box represents
                                 a single table.

A box with a + plus sign represents a
                                 subcategory of table with related detail: Peripheral and Trunk
                                 Group.

A stack of boxes represents several tables in
                                 another category of the schema.

A single arrowhead
                                 indicates a one-to-one relationship, and a double arrowhead indicates a
                                 one-to-many relationship.

To see database rules for these tables, see Device Tables .

Tables in the Device category include the
                           following:

### Peripheral
                           	 Detail

The figure below
                              		illustrates the tables in the Peripheral Detail subcategory.

These tables are:

### Trunk Group Detail

The figure below illustrates the tables in the Trunk Detail
                              subcategory.

These tables are:

## Enterprise

The figure below shows the relationships among tables in the
                           Enterprise category.

A single box represents a single
                                 table.

A stack of boxes represents several tables in
                                 another category of the schema.

A single arrowhead
                                 indicates a one-to-one relationship, and a double arrowhead indicates a
                                 one-to-many relationship.

To see database rules for these tables, see Enterprise Tables .

Tables that hold Enterprise data are listed below.

## Media Routing

The figure below shows the relationships among the tables in the
                           Media Routing category.

A single box represents a
                                 single table.

A stack of boxes represents several tables
                                 in another category of the schema.

A single arrowhead
                                 indicates a one-to-one relationship, and a double arrowhead indicates a
                                 one-to-many relationship.

To see Database rules for the Media Routing tables, see Media Routing Tables .

Media Routing Tables are listed below:

## Precision Queue

This figure depicts the tables in the Precision Queue category and their connections.

In this graphic:

A single box represents a single table.

A single arrowhead indicates a one-to-one relationship, and a double arrowhead indicates a one-to-many relationship.

Tables that hold Precision Queue data are listed below:

Agent_Real_Time

Agent_Skill_Group_Interval

Agent_Skill_Group_Real_Time

Call_Type_SG_Interval

Precision_Q_Real_Time_Table

Precision_Queue_Step

Precision_Queue_Term

Router_Queue_Interval

Skilll_Group

Skill_Group_Interval

Termination_Call_Detail

### Precision Queue Detail

The figure below illustrates the tables in the Precision Queue Detail subcategory.

## Route

This figure depicts
                           		the tables in this category and their connections.

In this graphic:

A single box
                                 			 represents a single table.

A box with a +
                                 			 plus sign represents a subcategory of table with related detail: Route Detail.

A stack of boxes
                                 			 represents several tables in another category of the schema.

A single arrowhead
                                 			 indicates a one-to-one relationship, and a double arrowhead indicates a
                                 			 one-to-many relationship.

To see Database Rules for Route
                           		Tables, see Route Tables .

Tables that hold Route data are
                           		listed below.

Route Detail Tables

The figure below
                           		illustrates the tables in the Route Details subcategory.

Route Detail Tables
                           		are:

## Schedule

This figure depicts
                           		the tables in this category.

In this graphic:

A single box
                                 			 represents a single table.

A stack of boxes
                                 			 represents several tables in another category of the schema.

A single arrowhead
                                 			 indicates a one-to-one relationship, and a double arrowhead indicates a
                                 			 one-to-many relationship.

To see Database Rules for
                           		Schedule Tables, see Schedule Tables .

Tables that hold Schedule data
                           		are listed below.

## Script

This
                           figure depicts the tables in this category.

In this
                           graphic:

A single box represents a single
                                 table.

A box with a + plus sign represents a subcategory
                                 of table with related detail: Call Type, Region, and Script.

A stack of boxes represents several tables in another category of the
                                 schema.

A single arrowhead indicates a one-to-one
                                 relationship, and a double arrowhead indicates a one-to-many
                                 relationship.

To see database rules for these tables, see Script Tables .

Script Tables are listed below

### Call Type
                           	 Detail

The figure below
                              		illustrates the tables in the Call Type subcategory.

These tables are:

Call_Type

### Region Detail

The figure below illustrates the tables in the Region Detail
                              subcategory.

Region Detail Tables are listed below:

### Script Detail

The figure below illustrates the tables in the Script Detail
                              subcategory.

Script Detail Tables are listed below:

## Security

The figure below shows the relationships among tables in the
                           Security category.

A single box represents a single
                                 table.

A stack of boxes represents several tables in
                                 another category of the schema.

A single arrowhead
                                 indicates a one-to-one relationship, and a double arrowhead indicates a
                                 one-to-many relationship.

To see database
                              rules for these tables, see Security Tables .

Tables that hold Security data are listed below.

## Skill Target

This figure shows the
                           		relationships among tables in the Skill Target category. The Agent, Service,
                           		Skill Group, and Skill Group Member tables each have related tables, as
                           		indicated by the + (plus signs) in the illustration.

In this graphic:

A single box
                                 			 represents a single table.

A box with a +
                                 			 plus sign represents a subcategory of table with related detail: Agent,
                                 			 Service, Skill Group, and Skill Group Member.

A stack of boxes
                                 			 represents several tables in another category of the schema.

A single arrowhead
                                 			 indicates a one-to-one relationship, and a double arrowhead indicates a
                                 			 one-to-many relationship.

To see database rules for Skill Target tables, see Skill Target Tables .

Skill Target tables include the following:

Agent Table. See
                                 			 the Agent Detail section, below.

Agent_Desk_Settings

Agent_Interval

Person

Service Tables.
                                 			 See the Service Detail section, below.

Service_Member

Skill Group and
                                 			 Skill Group Member Tables. See the Skill Group Detail Section, below.

Skill_Target

Translation_Route

Translation_Route_Half_Hour

### Agent Detail

The figure below
                              		illustrates tables in the Agent subcategory.

Agent Detail tables are
                              		listed below:

### Service
                           	 Detail

The figure below
                              		illustrates tables in the Service subcategory.

Service tables include:

Service

Service_Five_Minute

Service_Real_Time

### Skill Group
                           	 Detail

The figures below
                              		illustrate tables in the Skill Group and Skill Group Member subcategories.

Skill Group and Skill Group Member
                                 		  Tables include the following:

## Smart License

### Smart_License_Info

This table is one of the Smart License tables.

This table captures the Registration and Authorization status for a Smart License Agent instance running on a Unified CCE
                                 instance. The fields in this table represent the responses received from the Cisco Smart Software Manager (CSSM) portal using
                                 internal APIs.

Each row displays the information for one Smart Agent instance.

#### Related Tables

Smart_License_Server

Smart_License_Product

Smart_License_Entitlements

index_name

index_description

index_keys

XPKSmart_License_Info

Primary key

SmartLicenseInfoID

#### Fields in the Smart_License_Info Table

Name

Description

Data Type

Keys and NULL Option

AuthorizationExpires

Date and time of expiry of the product license authorization. Product license authorization must be renewed before this date.

DBDATETIME

NULL

AuthorizationFailedReason

ChangeStamp

CssmAuthorizationStatus

Authorization status ID of Unified CCE with CSSM or Satellite.

Default value is 5

CssmRegistrationStatus

Registration status ID of Unified CCE with CSSM or Satellite.

Default value is 2

DaysLeftInEvaluationMode

Number of days left in evaluation mode.

NULL

DaysLeftInOutOfCompliance

Number of days left in Out Of Compliance mode.

NULL

DateTimeStamp

ExportControlledAllow

N indicates that encryption cannot be turned on.

Values Y or N are allowed

NULL

EvaluationExpiredTime

Date and time of expiry of the product evaluation period.

DBDATETIME

NULL

FutureUseDateTime1

Reserved Field

DBDATETIME

NULL

FutureUseInt1

FutureUseInt1

FutureUseInt2

FutureUseInt3

FutureUseInt4

FutureUseInt5

FutureUseInt6

FutureUseVarChar1

FutureUseVarChar2

FutureUseVarChar3

FutureUseVarChar4

FutureUseVarChar5

IsAuthorizationFailed

Y if the product license authorization attempt fails.

Values Y or N are allowed

NULL

IsRegistrationFailed

Y if the product license registration attempt fails.

Values Y or N are allowed

NULL

LastAuthorizationAttempt

LastRenewalAttempt

NextAuthorizationAttempt

NextRenewalAttempt

OverageDays

The number of days you can use Unified CCE when Out Of Compliance.

OverageDaysUpdatedTime

ProductInstance

Registered Product instance with CSSM.

VARCHAR(100)

NULL

RegistrationExpires

RegistrationFailedReason

SmartAccount

Name of Smart Account Name.

VARCHAR(100)

NULL

SmartLicenseInfoID

Gets the Smart License ID from the Next_Available_Number table.

DBINT

PK

Clustered

SmartLicenseServerId

VirtualAccount

Name of Virtual Account Name.

VARCHAR(100)

NULL

### Smart_License_Server

This table is one of the Smart License tables.

This table stores the Unified CCE specific configuration information that is required for connection and registration to CSSM.

This table will come under configuration database table.

#### Related Tables

Smart_License_Info

Smart_License_Product

Smart_License_Entitlements

index_name

index_description

index_keys

XPKSmart_License_Server

Primary key

SmartLicenseServerID

Name

Description

Data Type

Keys and NULL Option

AgentId

ID that is used to identify the source of the notification when there are multiple instances of an agent on the same system.

VARCHAR(255)

NULL

ChangeStamp

Increments when the record is changed in the database.

CHANGESTAMP

NOT NULL

CssmResponseTimeout

Maximum wait time from CSSM before SmartAgent times out and  API fails.

DBINT

NULL

DateTimeStamp

Records the date and time when the record was added/updated.

DBDATETIME

NULL

DeploymentMode

Enterprise

DBINT

NOT NULL

ExcludeSpikes

Applies the 95 percentile formula to exclude spikes if this value set to Y .

Values Y or N are allowed

Default value is Y

DBCHAR

NOT NULL

FutureUseInt1

Reserved for future use.

DBINT

NULL

FutureUseInt2

Reserved for future use.

DBINT

NULL

FutureUseInt3

Reserved for future use.

DBINT

NULL

FutureUseInt4

Reserved for future use.

DBINT

NULL

FutureUseInt5

Reserved for future use.

DBINT

NULL

FutureUseVarChar1

Reserved for future use.

VARCHAR(255)

NULL

FutureUseVarChar2

Reserved for future use.

VARCHAR(255)

NULL

FutureUseVarChar3

Reserved for future use.

VARCHAR(255)

NULL

FutureUseVarChar4

Reserved for future use.

VARCHAR(255)

NULL

FutureUseVarChar5

Reserved for future use.

VARCHAR(255)

NULL

IDToken

Get the token from Cisco Licensing Cloud CSSM.

VARCHAR(255)

NULL

IsProvisionAllowed

Defines the enforcement level applied. Default value is Y which allows MACD operation on Agents and Features. Default.

Values Y or N are allowed.

DBCHAR

NOT NULL

LicenseType

1 -Perpetual

2 - Flex

DBINT

NOT NULL

OutOfCompliance

Defines if the system is OutOfCompliance.

Allowed: Y or N

DBCHAR

NULL

OutOfComplianceStartTime

The Out-of-Compliance start date.

DBDATETIME

NULL

OutOfComplianceCount

Number of times system went into Out Of Compliance.

Default Value: 0

DBINT

NULL

ProxyHostnameOrIP

Intermediate HTTP/HTTPS proxy Host name or IP address

VARCHAR(255)

NULL

ProxyPort

Intermediate HTTP/HTTPS proxy port address

DBINT

NULL

SmartCode

For internal use.

VARCHAR(255)

NULL

SmartLicenseServerID

Gets the Smart License ID from the Next_Available_Number table.

DBINT

PK

Clustered

SerialNumber

Serial number to identify the product.

VARCHAR(50)

NULL

Reservation Type

Reservation State:

0 - Disabled

1 - Enabled

DBINT

NULL

SlrStatus

SLR Status

0 - NONE

1 - IN_PROGRESS

2 - UNIVERSAL

3 - SPECIFIC

DBINT

NULL

TransportGatewayUrl

Smart Software Manager Satellite URL only in mediated deployment mode.

VARCHAR(255)

NULL

TransportType

0 - Direct

1 - On-Prem CSSM

2 - Proxy

DBINT

NOT NULL

TransportUrl

Cisco Smart Software Manager transport URL in non-mediated deployment mode.

VARCHAR(255)

NULL

TransportMode

Transport mechanism to connect Smart Agent To CSSM

1 - Smart Call Home

2 - Smart Transport

DBINT

NULL

UsageMode

The two License Usage Modes are:

0 - Production

1 - Non-Production system

DBINT

NULL

### Smart_License_Entitlements

This table is one of the Smart License tables.

This table stores the information on the pre-defined entitlement tags for identifying and reporting licenses on CSSM.

The information is presented in the table in multiple rows, one for each supported entitlement such as Standard and Premium
                                 Agent Entitlement for each supported product.

#### Related Tables

Smart_License_Info

Smart_License_Product

Smart_License_Server

index_name

index_description

index_keys

XPKSmart_License_Entitlements

Primary key

SmartLicenseEntitlementsTagID

Name

Description

Data Type

Keys and NULL Option

ChangeStamp

Increments when the record is changed in the database.

CHANGESTAMP

NOT NULL

DateTimeStamp

Records the date and time when the record was added/updated.

DBDATETIME

NULL

DeploymentType

Deployment mode of the system.

varchar(255)

NULL

EntitlementTag

Unique tag per Product ID (PID).

For example, Standard or Premium Agent EntitlementTag. EntitlementTag names are different for different types licenses.

VARCHAR(255)

NULL

EntitlementDisplayname

Identifies the entitlement names for the configured deployment.

VARCHAR(255)

NULL

EntitlementDescription

Displays the description of the Entitlement on CSSM.

1 - Direct

2 - Proxy

3 - Satellite Connected

4 - Satellite Disconnected

VARCHAR(255)

NULL

EntitlementVersion

Entitlement Version is usually 1.0 unless multiple versions are required by the product.

VARCHAR(255)

NULL

EnforcementMode

Current enforcement mode of the entitlement.

List of the probable modes:

Invalid

Licenses not in use

Waiting

InCompliance

OutOfCompliance

Overage

Evaluation Mode

EvalExpired

AuthorizedPeriodExpired

Disabled

InvalidTag

NotApplicable

ReservedInCompliance

NotAuthorized

NotInUse

VARCHAR(50)

NULL

FutureUseVarChar1

Reserved for future use.

VARCHAR(255)

NULL

FutureUseVarChar2

Reserved for future use.

VARCHAR(255)

NULL

FutureUseInt1

Reserved for future use.

DBINT

NULL

FutureUseInt2

Reserved for future use.

DBINT

NULL

LicenseType

The two types of license supported are:

1 - Perpetual

2 - Flex

The default value 1(Perpetual).

DBINT

NULL

LockUsage

It is the highest license consumption value above and beyond entitlement value when the system is in Out-of-compliance state.

DBINT

NULL

OutOfCompliance

This flag tells whether this Entitlement is in OutOfCompliance.

DBINT

NULL

OutOfComplianceCount

Displays the number of times the Entitlements are OutOfCompliance.

DBINT

NULL

PeakUsage

Displays the peak usage of this entitlement

DBINT

NULL

SmartLicense EntitlementsTagID

Gets the Smart License ID from the Next_Available_Number table.

DBINT

NOT NULL

### Smart_License_Product

This table is one of the Smart License tables.

This table stores the information about the pre-defined product tag, display name and description to identify the product
                                 instances on CSSM.

#### Related Tables

Smart_License_Info

Smart_License_Server

Smart_License_Entitlements

index_name

index_description

index_keys

XPKSmart_License_Product

Primary key

SmartLicenseProductID

Name

Description

Data Type

Keys and NULL Option

ChangeStamp

This field is incremented when the record is changed in the database.

CHANGESTAMP

NOT NULL

DateTimeStamp

Records the date and time when the license record was added/updated.

DBDATETIME

NULL

FutureUseInt1

Reserved for future use.

DBINT

NULL

FutureUseInt2

Reserved for future use.

DBINT

NULL

FutureUseVarChar1

Reserved for future use.

VARCHAR(255)

NULL

FutureUseVarChar2

Reserved for future use.

VARCHAR(255)

NULL

ProductDescription

Displays the description of the product license in the product instance overview of CSSM.

VARCHAR (255)

NULL

ProductDisplayName

Displays the name of the product in the product instance overview of CSSM.

VARCHAR (255)

NOT NULL

ProductEnvironment

Displays the environment of the product in the product instance overview of CSSM.

The two types of  environments supported are:

0: Production (default value)

1: Development

DBINT

NULL

PrivacyEnabled

Displays the privacy status of the product in the product instance overview of CSSM.

Values 0 or 1 are allowed.

0: Privacy disabled

1: Privacy enabled (default value)

DBINT

NULL

ProductTag

Is a unique id defined for each product like

UCCE

PCCE

VARCHAR (255)

NOT NULL

ProductVersion

Product Version is usually 1.0 unless multiple versions are required by the product.

VARCHAR (30)

NULL

SmartLicenseProductID

Gets the Smart License ID from the Next_Available_Number table.

DBINT

PK

Clustered

## System

The figure below
                           		illustrates tables in the System category. To see database rules for these tables, see System Tables .

To see database rules for these tables, see System Tables .

System Tables are listed below

## User Preferences

The figure below illustrates the relationships among the Uesr
                           Preferences tables.

A single box represents a single
                                 table.

A stack of boxes represents several tables in
                                 another category of the schema.

A single arrowhead
                                 indicates a one-to-one relationship, and a double arrowhead indicates a
                                 one-to-many relationship.

To see database rules for these
                           tables, see User Preferences Tables .

User Preferences Tables include the following:

## VRU Micro-application

The figure below illustrates the relationships among
                           the VRU Micro-Application tables.

A single box
                                 represents a single table.

A single arrowhead indicates a
                                 one-to-one relationship, and a double arrowhead indicates a one-to-many
                                 relationship.

For database rules , see VRU Micro-applications Tables .

VRU MicroApplication Tables are listed below:

Vru_Currency

Vru_Defaults

Vru_Locale

## Tables Reserved for
                        	 Future Use

Although the following tables have been added to the Unified CCE Schema, they are reserved for future use:

Application_Gateway_License

Campaign_Half_Hour

Campaign_Real_Time

Dialer Skill Group
                                 			 Half Hour

Dialer Skill Group
                                 			 Real Time

License_Definition

License_Real_Time

Phone_Strategy

Phone_Strategy_Node

| index_name | index_description | index_keys |
|---|---|---|
| XPKSmart_License_Info | Primary key | SmartLicenseInfoID |

| Name | Description | Data Type | Keys and NULL Option |
|---|---|---|---|
| AuthorizationExpires | Date and time of expiry of the product license authorization. Product license authorization must be renewed before this date. | DBDATETIME | NULL |
| AuthorizationFailedReason | Reason for failure of authorization attempt. | VARCHAR(255) | NULL |
| ChangeStamp | Incremented when the record is changed in the database. | CHANGESTAMP | NOT NULL |
| CssmAuthorizationStatus | Authorization status ID of Unified CCE with CSSM or Satellite. Default value is 5 | DBINT | NULL |
| CssmRegistrationStatus | Registration status ID of Unified CCE with CSSM or Satellite. Default value is 2 | DBINT | NULL |
| DaysLeftInEvaluationMode | Number of days left in evaluation mode. | DBINT | NULL |
| DaysLeftInOutOfCompliance | Number of days left in Out Of Compliance mode. | DBINT | NULL |
| DateTimeStamp | Records the date and time when the record is added/updated. | DBDATETIME | NULL |
| ExportControlledAllow | N indicates that encryption cannot be turned on. Values Y or N are allowed | DBCHAR | NULL |
| EvaluationExpiredTime | Date and time of expiry of the product evaluation period. | DBDATETIME | NULL |
| FutureUseDateTime1 | Reserved Field | DBDATETIME | NULL |
| FutureUseInt1 | Reserved Field | DBINT | NULL |
| FutureUseInt1 | Reserved Field | DBINT | NULL |
| FutureUseInt2 | Reserved Field | DBINT | NULL |
| FutureUseInt3 | Reserved Field | DBINT | NULL |
| FutureUseInt4 | Reserved Field | DBINT | NULL |
| FutureUseInt5 | Reserved Field | DBINT | NULL |
| FutureUseInt6 | Reserved Field | DBINT | NULL |
| FutureUseVarChar1 | Reserved Field | VARCHAR(255) | NULL |
| FutureUseVarChar2 | Reserved Field | VARCHAR(255) | NULL |
| FutureUseVarChar3 | Reserved Field | VARCHAR(255) | NULL |
| FutureUseVarChar4 | Reserved Field | VARCHAR(255) | NULL |
| FutureUseVarChar5 | Reserved Field | VARCHAR(255) | NULL |
| IsAuthorizationFailed | Y if the product license authorization attempt fails. Values Y or N are allowed | DBCHAR | NULL |
| IsRegistrationFailed | Y if the product license registration attempt fails. Values Y or N are allowed | DBCHAR | NULL |
| LastAuthorizationAttempt | Date and Time of the last renewal attempt for the product license authorization. | DBDATETIME | NULL |
| LastRenewalAttempt | Date and Time of the last renewal attempt for the product license registration. | DBDATETIME | NULL |
| NextAuthorizationAttempt | Date and Time of the next renewal attempt for the product license authorization. | DBDATETIME | NULL |
| NextRenewalAttempt | Date and Time of the next renewal attempt for the product license registration. | DBDATETIME | NULL |
| OverageDays | The number of days you can use Unified CCE when Out Of Compliance. | DBINT | NULL |
| OverageDaysUpdatedTime | Time stamp when the overage days column is updated. | DBDATETIME | NULL |
| ProductInstance | Registered Product instance with CSSM. | VARCHAR(100) | NULL |
| RegistrationExpires | Date and Time at which the product license registration will expire. Product license registration must be renewed before this
                                          date. | DBDATETIME | NULL |
| RegistrationFailedReason | Reason for registration attempt failure. | VARCHAR(255) | NULL |
| SmartAccount | Name of Smart Account Name. | VARCHAR(100) | NULL |
| SmartLicenseInfoID | Gets the Smart License ID from the Next_Available_Number table. | DBINT | PK Clustered |
| SmartLicenseServerId | Foreign key to SmartLicenseServer | DBINT | NULL |
| VirtualAccount | Name of Virtual Account Name. | VARCHAR(100) | NULL |

| index_name | index_description | index_keys |
|---|---|---|
| XPKSmart_License_Server | Primary key | SmartLicenseServerID |

| Name | Description | Data Type | Keys and NULL Option |
|---|---|---|---|
| AgentId | ID that is used to identify the source of the notification when there are multiple instances of an agent on the same system. | VARCHAR(255) | NULL |
| ChangeStamp | Increments when the record is changed in the database. | CHANGESTAMP | NOT NULL |
| CssmResponseTimeout | Maximum wait time from CSSM before SmartAgent times out and  API fails. | DBINT | NULL |
| DateTimeStamp | Records the date and time when the record was added/updated. | DBDATETIME | NULL |
| DeploymentMode | Enterprise | DBINT | NOT NULL |
| ExcludeSpikes | Applies the 95 percentile formula to exclude spikes if this value set to Y . Values Y or N are allowed Default value is Y | DBCHAR | NOT NULL |
| FutureUseInt1 | Reserved for future use. | DBINT | NULL |
| FutureUseInt2 | Reserved for future use. | DBINT | NULL |
| FutureUseInt3 | Reserved for future use. | DBINT | NULL |
| FutureUseInt4 | Reserved for future use. | DBINT | NULL |
| FutureUseInt5 | Reserved for future use. | DBINT | NULL |
| FutureUseVarChar1 | Reserved for future use. | VARCHAR(255) | NULL |
| FutureUseVarChar2 | Reserved for future use. | VARCHAR(255) | NULL |
| FutureUseVarChar3 | Reserved for future use. | VARCHAR(255) | NULL |
| FutureUseVarChar4 | Reserved for future use. | VARCHAR(255) | NULL |
| FutureUseVarChar5 | Reserved for future use. | VARCHAR(255) | NULL |
| IDToken | Get the token from Cisco Licensing Cloud CSSM. | VARCHAR(255) | NULL |
| IsProvisionAllowed | Defines the enforcement level applied. Default value is Y which allows MACD operation on Agents and Features. Default. Values Y or N are allowed. | DBCHAR | NOT NULL |
| LicenseType | 1 -Perpetual 2 - Flex | DBINT | NOT NULL |
| OutOfCompliance | Defines if the system is OutOfCompliance. Allowed: Y or N | DBCHAR | NULL |
| OutOfComplianceStartTime | The Out-of-Compliance start date. | DBDATETIME | NULL |
| OutOfComplianceCount | Number of times system went into Out Of Compliance. Default Value: 0 | DBINT | NULL |
| ProxyHostnameOrIP | Intermediate HTTP/HTTPS proxy Host name or IP address | VARCHAR(255) | NULL |
| ProxyPort | Intermediate HTTP/HTTPS proxy port address | DBINT | NULL |
| SmartCode | For internal use. | VARCHAR(255) | NULL |
| SmartLicenseServerID | Gets the Smart License ID from the Next_Available_Number table. | DBINT | PK Clustered |
| SerialNumber | Serial number to identify the product. | VARCHAR(50) | NULL |
| Reservation Type | Reservation State: 0 - Disabled 1 - Enabled | DBINT | NULL |
| SlrStatus | SLR Status 0 - NONE 1 - IN_PROGRESS 2 - UNIVERSAL 3 - SPECIFIC | DBINT | NULL |
| TransportGatewayUrl | Smart Software Manager Satellite URL only in mediated deployment mode. | VARCHAR(255) | NULL |
| TransportType | 0 - Direct 1 - On-Prem CSSM 2 - Proxy | DBINT | NOT NULL |
| TransportUrl | Cisco Smart Software Manager transport URL in non-mediated deployment mode. | VARCHAR(255) | NULL |
| TransportMode | Transport mechanism to connect Smart Agent To CSSM 1 - Smart Call Home 2 - Smart Transport | DBINT | NULL |
| UsageMode | The two License Usage Modes are: 0 - Production 1 - Non-Production system | DBINT | NULL |

| index_name | index_description | index_keys |
|---|---|---|
| XPKSmart_License_Entitlements | Primary key | SmartLicenseEntitlementsTagID |

| Name | Description | Data Type | Keys and NULL Option |
|---|---|---|---|
| ChangeStamp | Increments when the record is changed in the database. | CHANGESTAMP | NOT NULL |
| DateTimeStamp | Records the date and time when the record was added/updated. | DBDATETIME | NULL |
| DeploymentType | Deployment mode of the system. | varchar(255) | NULL |
| EntitlementTag | Unique tag per Product ID (PID). For example, Standard or Premium Agent EntitlementTag. EntitlementTag names are different for different types licenses. | VARCHAR(255) | NULL |
| EntitlementDisplayname | Identifies the entitlement names for the configured deployment. | VARCHAR(255) | NULL |
| EntitlementDescription | Displays the description of the Entitlement on CSSM. 1 - Direct 2 - Proxy 3 - Satellite Connected 4 - Satellite Disconnected | VARCHAR(255) | NULL |
| EntitlementVersion | Entitlement Version is usually 1.0 unless multiple versions are required by the product. | VARCHAR(255) | NULL |
| EnforcementMode | Current enforcement mode of the entitlement. List of the probable modes: Invalid Licenses not in use Waiting InCompliance OutOfCompliance Overage Evaluation Mode EvalExpired AuthorizedPeriodExpired Disabled InvalidTag NotApplicable ReservedInCompliance NotAuthorized NotInUse | VARCHAR(50) | NULL |
| FutureUseVarChar1 | Reserved for future use. | VARCHAR(255) | NULL |
| FutureUseVarChar2 | Reserved for future use. | VARCHAR(255) | NULL |
| FutureUseInt1 | Reserved for future use. | DBINT | NULL |
| FutureUseInt2 | Reserved for future use. | DBINT | NULL |
| LicenseType | The two types of license supported are: 1 - Perpetual 2 - Flex The default value 1(Perpetual). | DBINT | NULL |
| LockUsage | It is the highest license consumption value above and beyond entitlement value when the system is in Out-of-compliance state. | DBINT | NULL |
| OutOfCompliance | This flag tells whether this Entitlement is in OutOfCompliance. | DBINT | NULL |
| OutOfComplianceCount | Displays the number of times the Entitlements are OutOfCompliance. | DBINT | NULL |
| PeakUsage | Displays the peak usage of this entitlement | DBINT | NULL |
| SmartLicense EntitlementsTagID | Gets the Smart License ID from the Next_Available_Number table. | DBINT | NOT NULL |

| index_name | index_description | index_keys |
|---|---|---|
| XPKSmart_License_Product | Primary key | SmartLicenseProductID |

| Name | Description | Data Type | Keys and NULL Option |
|---|---|---|---|
| ChangeStamp | This field is incremented when the record is changed in the database. | CHANGESTAMP | NOT NULL |
| DateTimeStamp | Records the date and time when the license record was added/updated. | DBDATETIME | NULL |
| FutureUseInt1 | Reserved for future use. | DBINT | NULL |
| FutureUseInt2 | Reserved for future use. | DBINT | NULL |
| FutureUseVarChar1 | Reserved for future use. | VARCHAR(255) | NULL |
| FutureUseVarChar2 | Reserved for future use. | VARCHAR(255) | NULL |
| ProductDescription | Displays the description of the product license in the product instance overview of CSSM. | VARCHAR (255) | NULL |
| ProductDisplayName | Displays the name of the product in the product instance overview of CSSM. | VARCHAR (255) | NOT NULL |
| ProductEnvironment | Displays the environment of the product in the product instance overview of CSSM. The two types of  environments supported are: 0: Production (default value) 1: Development | DBINT | NULL |
| PrivacyEnabled | Displays the privacy status of the product in the product instance overview of CSSM. Values 0 or 1 are allowed. 0: Privacy disabled 1: Privacy enabled (default value) | DBINT | NULL |
| ProductTag | Is a unique id defined for each product like UCCE PCCE | VARCHAR (255) | NOT NULL |
| ProductVersion | Product Version is usually 1.0 unless multiple versions are required by the product. | VARCHAR (30) | NULL |
| SmartLicenseProductID | Gets the Smart License ID from the Next_Available_Number table. | DBINT | PK Clustered |