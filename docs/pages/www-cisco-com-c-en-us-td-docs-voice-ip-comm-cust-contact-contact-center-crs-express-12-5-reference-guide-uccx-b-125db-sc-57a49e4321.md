---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-reference-guide-uccx-b-125db-sc-57a49e4321
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/reference/guide/uccx_b_125db-schema-guide/uccx_b_125db-schema-guide_chapter_01.html
retrieved_at: 2026-08-16T20:55:10.954366+00:00
---

Cisco Unified Contact Center Express Database Schema Guide, Release 12.5(1)

# Cisco Unified Contact Center Express Database Schema Guide, Release 12.5(1)

Book Contents

- Book Title Page

- Preface

- Database
	 Schema

Find Matches in This Book

## Results

Updated: February 5, 2020

Chapter: Database
	 Schema

## Chapter: Database
	 Schema

# Database
                     	 Schema

db_cra – Used to
                                 			 store information for historical and real-time reports, including Unified CCX
                                 			 configuration information, stored procedures, and call statistics.

db_cra_repository - Used to store information related to
                                 			 prompts, grammars, scripts, and documents.

All the tables
                        		described in this document are in the above two databases.

SQL is
                                    		  case-insensitive and the queries written against the database can be in any
                                    		  case. However, you might have to change the case for the column names depending
                                    		  on the third-party tool that you use for querying the database. Refer to the
                                    		  documentation for these third-party tools for more information.

The following
                        		sections include these topics:

## General Database Concepts

This section provides an overview of some basic database concepts.

### Tables, Columns,
                           	 and Rows

A database
                                 		  contains one or more tables of data. Each table in a database defines a set of
                                 		  columns, which are called fields .
                                 		  Within each table, the database stores data in rows, which are called records .
                                 		  Each record (row) contains one value for each field (column) of the table.

Database tables
                                 		  and the number and names of their fields are constant. The number of records in
                                 		  a table and the data that those records contain will vary according your
                                 		  system.

### Table
                           	 Relationships

Related tables in
                                 		  a database share one or more common fields. For example, both the Skill and the
                                 		  SkillGroup tables include the skillID field. Each record in the Skill table is
                                 		  related to each record in the SkillGroup table that shares the same skillID
                                 		  value.

Relationships
                                 		  between tables can be one-to-one or one-to-many. For example, because one skill
                                 		  can be associated with many skill groups, the relationship between the Skill
                                 		  and SkillGroup tables is one-to-many. On the other hand, each call or call leg
                                 		  has its own set of data about the agent who handled the call and other
                                 		  information. Therefore, the relationship between the AgentConnectionDetail and
                                 		  ContactCallDetail table is one-to-one.

Each database
                                 		  table description in this manual is followed by a Related Tables section. These
                                 		  sections show the fields by which a table is related to other tables. If the
                                 		  fields have different names in each table, these sections show the mapping.

## Database Table
                        	 Details

Each description provides the following information:

Database Table Name—Name of the Unified CCX database table.

Field Name—Name of a field as it appears in the database table.

Description—Description of the field, including valid values where
                                    				appropriate.

Storage—Information about the data in each field as follows:

For storage characteristics and limitations of the data
                                                         						  types used for the fields in the databases refer to "IBM Informix SQL Reference
                                                         						  Guide". The date and time in the database fields are stored in Coordinated
                                                         						  Universal Time (UTC).

If the NULL value is valid, the database will record a
                                                         						  value of -1 for a numeric field and an empty string for other fields.

“Primary Key” if the field is a primary key, or part of a
                                          					 primary key, in the database table.

### Overview of
                           	 Tables

The following tables are described in this guide:

AgentConnectionDetail , contains records written for calls that are connected to an agent.

AgentStateDetail , contains records written when an agent changes state.

AgentCallDetailSnapshot , contains records of agent call details in a day.

AgentStateDetailSnapshot , contains records of agent state change details in a day.

AuditReskill , contains records written when the resource is added or removed from the CSQ because of the changes that are made to the
                                       resource or CSQ skills.

AuditSkillGroup , contains records written when the resource skills or competency level changes are made to the resource or CSQ.

AreaCode , contains the area code and time zone information used for outbound calls.

Campaign , contains records with campaign configuration information.

CampaignCSQMap , provides a relationship between campaigns and Contact Service Queues (CSQs).

CampaignSupervisorMap , provides a relationship between campaigns and supervisors.

CampaignData , contains records with the campaign data information.

ChatProblemStatement , contains the associated problem statements and tag ids for each chat widget.

ChatTriggerPoint , contains the chat CSQ tag information.

ChatUserForm , contains the user form fields included in each chat widget along with the order of the fields in the widget.

ChatWidget , contains the chat widget information.

ChatBubble , contains the chat bubble information.

ContactCallDetail , contains records written for every incoming, outgoing, or internal call.

ContactQueueDetail , contains records written for calls that are queued for CSQs; one record for each CSQ is queued.

ContactRoutingDetail , contains records written for calls that are queued for CSQs; one record for each call.

ContactServiceQueue , contains records written for CSQs configured on the Unified CCX Administration user interface.

CrsApplication , contains records about applications that are uniquely identified by application name.

CrsGroup , contains records about groups that are identified by a combination of group class name and group ID.

CrsTrigger , contains records about triggers that are uniquely identified by trigger name.

DialingList , contains records with outbound contacts that need to be dialed for a particular campaign.

MonitoredResourceDetail , contains records written for agents who are monitored by a Supervisor.

ProfileIDMapping , contains records written for profiles defined on the Unified CCX Administration user interface.

PurgeHistory , contains records written for tracking of the history of purge information for both Manual and Scheduled purge.

RemoteMonitoringDetail , contains records written for remote monitoring calls made by a Supervisor.

Resource , contains records written for resources (agents) that are configured on the Cisco Unified Communications Manager (Unified
                                       CM) Administration user interface.

ResourceGroup , contains records written for resource groups configured on the Unified CCX Administration user interface.

ResourceSkillMapping , is a relationship table between resources and skills.

RmonCSQConfig , contains records written for CSQs configured for a Supervisor’s remote monitoring allowed list on the Unified CCX Administration
                                       user interface.

RmonResConfig , contains records written for resources configured for a Supervisor’s remote monitoring allowed list on the Unified CCX Administration
                                       user interface.

RmonUser , contains records written for remote monitoring Supervisors configured on the Unified CCX Administration user interface.

RtCSQsSummary , contains real-time statistics for configured CSQs.

RtICDStatistics , contains Unified CCX summary statistics.

Skill , contains records written for skills configured on the Unified CCX Administration user interface.

SkillGroup , is a relationship table between skills and CSQs.

Supervisor , contains records written for Supervisors configured on the Unified CCX Administration user interface.

SupervisorCampaignMap , contains records for the list of campaigns that can be associated with no or more campaigns to a Supervisor and managed
                                       by the Supervisor.

SupervisorApplicationMap , contains records for the list of applications that can be associated to a Supervisor and managed by the Supervisor.

Team , contains records written for teams configured on the Unified CCX Administration user interface.

TeamCSQMapping , is a relationship table between teams and CSQs.

TextAgentConnectionDetail , contains information relating to the agent who handled the contact or leg.

TextAgentStateDetails , contains information about the chat agent and about the event that caused the chat agent state change.

TextContactDetail , contains detailed information about the contact or leg.

TextContactQueueDetail , is a relationship table between teams and CSQs.

TextCustomerDetails , contains customer-related information corresponding to the chat contact.

WorkflowTask , contains records written for workflow tasks that are executed.

ConsultLegDetail , contains records of agents corresponding to the consult call details.

### AgentConnectionDetail

Database table name : AgentConnectionDetail

The Unified CCX system creates a new record in the AgentConnectionDetail table when an agent disconnects a call or a leg by
                                 hanging up or by transferring the call. (A new call leg starts each time that a call is transferred, except when a call is
                                 transferred from a Cisco Computer Telephony Interface [CTI] port to an agent.)

An AgentConnectionDetail record contains information relating to the agent who handled the call or call leg.

Field Name

Description

Storage

sessionID

Identifier that the system assigns to the call. This identifier remains the same for all legs of the call.

decimal(18, 0)

NOT NULL

Primary Key

sessionSeqNum

Session sequence number that the system assigned to the call or the leg. Each leg of a call is assigned a new sequence number.

smallint

NOT NULL

Primary Key

nodeID

Unique identifier assigned to each Unified CCX server in the cluster.

smallint

NOT NULL

Primary Key

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

resourceID

Identifier of the agent who handled the call.

int

NOT NULL

Primary Key

startDateTime

Date and time that the call or the leg started ringing at the device of an agent.

datetime year to fraction (3)

NOT NULL

Primary Key

endDateTime

Date and time that the call or the leg was transferred or disconnected.

datetime year to fraction (3)

NOT NULL

qIndex

For all the new calls that are coming to an agent’s extension through a route point, the value of qIndex is 1. Thereafter,
                                             the value of qIndex is incremented by 1, whenever there is a conference through the route point.

The value of qIndex of an agent is 0, whenever an agent receives a call to the extension directly (by conference and transfer
                                                         legs) instead of a route point. This is applicable only for the AgentConnectionDetail table.

smallint

NOT NULL

Primary Key

gmtOffset

Offset, in minutes, between the local time of the Unified CCX server and Greenwich Mean Time. As the time information is stored
                                             in GMT, this field will always be zero.

smallint

NOT NULL

ringTime

Amount of time, in seconds, between the time the call or the leg first rang at the extension of an agent and one of the following
                                             events:

The agent answered the call or the leg

The caller hung up before the call or the leg was answered

The system retrieved the call or the leg before the call or the leg was answered

smallint

NULL

talkTime

Amount of time, in seconds, that passed from the time an agent answered the call or the leg to the time the call or the leg
                                             was disconnected or transferred, not including hold time.

int

NULL

holdTime

Amount of time, in seconds, that the call or the leg spent on hold.

smallint

NULL

workTime

Amount of time, in seconds, that an agent spent in Work State after the call or the leg.

smallint

NULL

callWrapupData

After-call information that the agent enters through the Agent Desktop user interface while the agent is in the work state.

varchar(40)

NULL

callResult

Outcome of the outbound dialer call.

1 = Voice (Customer answered and was connected to agent)

2 = Fax/Modem (Fax machine detected)

3 = Answering Machine (answering machine detected)

4 = Invalid (Number reported as invalid by the network)

5 = Do Not Call (customer does not want to be called again)

6 = Wrong Number (number successfully contacted but wrong number)

7 = Customer Not Home (number successfully contacted but reached the wrong person)

8 = Callback (customer requested regular callback)

9 = Agent Rejected (Agent has skipped or rejected a preview call)

10 = Agent Closed (Agent has skipped or rejected a preview call with the close option)

11 = Busy (busy signal detected)

12 = RNA (the agent lets the call go ring-no-answer)

20 = OB_XFER is default (the agent transfers or conferences the outbound call to another agent.

smallint

NULL

dialinglistid

Unique identifier of a contact that is dialed for an outbound campaign. Links with DialingList.dialingListID

int

NULL

rna

Specifies if the call or the leg hasn’t been answered by an agent within the configured ring time. This equates to ’t’ if
                                             the call hasn’t been answered.

Boolean

loginsessionid

Unique identifier of an agent login session. This identifier remains the same until the session ends.

varchar(18)

contactid

Unique identifier for all records related to a single call across various tables in Unified CCX.

varchar(40)

csqrecordid

Numeric identifier of CSQ for CSQ-based calls, else -1 is stored.

int

consultsessionid

This field is NOT NULL for conferenced or transferred agents through consult call. The value will be the sessionID of the
                                             consult call.

decimal (18, 0)

### AgentStateDetail

Database table name : AgentStateDetail

The Unified CCX system creates a new record in the AgentStateDetail table each time the state of an agent changes. An AgentStateDetail
                                 record contains information about the agent and about the event that caused the agent state change.

Field Name

Description

Storage

agentID

Identifier of the agent whose state has changed.

int

NOT NULL

Primary Key

eventDateTime

Date and time that the agent state changed.

datetime year to fraction (3)

NOT NULL

Primary Key

gmtOffset

Offset, in minutes, between the local time of the Unified CCX server and Greenwich Mean Time. As the time information is stored
                                             in GMT, this field will always be zero.

smallint

NOT NULL

eventType

Event that triggered the agent state change:

1—Log In

2—Not Ready

3—Ready

4—Reserved

5—Talking

6—Work

7—Log Out

smallint

NOT NULL

Primary Key

reasonCode

Code, as set up in the Cisco Desktop Administrator, for the reason that the agent changed to Not Ready State or to Log Out
                                             State.

Null if a reason code is not configured.

smallint

NOT NULL

Primary Key

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

loginsessionid

Unique identifier of an agent login session. This identifier remains the same until the session ends.

varchar(18)

contactid

Unique identifier for all records related to a single call across various tables in Unified CCX.

varchar(40)

### AgentCallDetailSnapshot

Database table name : AgentCallDetailSnapshot

The Unified CCX system stores the records of agent call details in a day in the AgentCallDetailSnapshot table. All previous
                                 day records will be purged as part of the scheduled purge at mid-night.

Field Name

Description

Storage

contactid

Alphanumeric identifier for the contact.

int

NOT NULL

Primary Key

sessionseqnum

Session sequence number that the system assigned to the call or the leg. Each leg of a call is assigned a new sequence number.

smallint

NOT NULL

Primary Key

agentID

Identifier of the agent whose ACD call details are stored.

int

NOT NULL

Primary Key

calltype

Identifier of the type of all incoming and outgoing calls of agents' ACD line extension.

int

NOT NULL

startdatetime

Start date and time of the agent call details that are to be stored.

BIG INT

NOT NULL

Primary Key

phonenumber

Identifier of the phone number of the calls that were handled by the agent.

varchar (30)

NOT NULL

disposition

Identifier of the contact disposition.

int

NULL

wrapupdata

Information that the agents enter in the desktop user interface after a call, while the agents are still in the work state.

lvarchar (804)

NULL

csqname

Identifier of the CSQ name that the agent was assigned to.

nvarchar (50)

NULL

enddatetime

End date and time of the agent call details that are to be stored.

BIG INT

NOT NULL

### AgentStateDetailSnapshot

Database table name : AgentStateDetailSnapshot

The Unified CCX system stores the records of agent state change details in a day in the AgentStateDetailSnapshot table. All
                                 previous day records will be purged as part of the scheduled purge at mid-night.

Field Name

Description

Storage

agentID

Identifier of the agent whose state has changed.

int

NOT NULL

Primary Key

eventDateTime

Date and time that the agent state changed.

BIG INT

NOT NULL

Primary Key

eventType

Event that triggered the agent state change:

1—Log In

2—Not Ready

3—Ready

4—Reserved

5—Talking

6—Work

7—Log Out

smallint

NOT NULL

Primary Key

reasonCode

Code, as set up in the Cisco Desktop Administrator, for the reason that the agent changed to Not Ready State or to Log Out
                                             State.

Null if a reason code is not configured.

smallint

NOT NULL

Primary Key

wrapupData

After-call information that the agent enters through the Agent Desktop user interface while the agent is in the work state.

lvarchar (804)

NULL

Related Tables

Resource (agentID maps to resourceID and via profileID)

### Application Prompt Map

Database table name : ApplicationPromptMap

The Unified CCX system creates a new record in the applicationpromptmap table when an administrator is associating prompt files, a folder of prompts, or a combination of prompt files and folders
                                 to an application.

Field Name

Description

Storage

recordid

Unique identifier of the record.

int

NOT NULL

Primary Key

profileid

Profile ID of the node.

int

NOT NULL

Primary Key

applicationname

Name of the application.

nvarchar (50)

NOT NULL

promptid

Unique identifier for the prompt file or folder assigned to the application. This is retrieved from assignedprompts table.

int

NOT NULL

active

Indicates whether the record is active or not. By default, it is True . It is marked as False when either the application or the assigned prompt (file or folder) is deleted.

boolean

dateinactive

Date and Time at which, the record is marked as inactive.

Default value: NULL

date time year to second

### AreaCode

Database table name : AreaCode

The AreaCode table
                                 		  contains a mapping of area codes and their time zones. This table is used as a
                                 		  reference for populating the gmtPhone and dstPhone columns of the DialingList
                                 		  table. This table is pre-populated by the Unified CCX system with the data for
                                 		  North America during the installation process, using a SQL script that the
                                 		  installer invokes. If the Unified CCX is installed in a different location,
                                 		  administrators can enter the area code and time zone information for that
                                 		  region using Unified CCX Administration, and the data is stored in this table.

Field Name

Description

Storage

profileid

Identifier
                                                					 of the profile.

int

NOT NULL

Primary
                                                					 Key

createdatetime

Default
                                                					 -CURRENT_TIMESTAMP

datetime
                                                					 year to second

NOT NULL

recordid

Unique
                                                					 identifier for the record

int

NOT NULL

Primary
                                                					 Key

areacode

The area
                                                					 code of the call.

nvarchar(10)

NOT NULL

Primary
                                                					 Key

regioncode

Uses the
                                                					 same data as that of gmtzone.

nvarchar(10)

NULL

daylightsavingsenabled

N =
                                                         						  Daylight savings time is not observed.

Y =
                                                         						  Daylight savings time is observed.

char(1)

NOT NULL

gmtzone

Stores
                                                					 identifiers that internally maps to the GMT offset corresponding to the area
                                                					 code.

int

NULL

privatedata

Any fields
                                                					 which are to be used internally only.

BLOB

NULL

active

Whether
                                                					 the record is active in the system. A record becomes inactive if the team is
                                                					 deleted from the system.

f =
                                                					 Inactive

t = Active

boolean

NOT NULL

dateinactive

Date
                                                					 this record was deleted.

datetime
                                                					 year to second

NULL

### Assigned Prompts

Database table name : AssignedPrompts

This table stores the details of prompt files and folders that are assigned to applications. Before updating the applicationpromptmap table, the system verifies if the selected prompt file or prompt folder is available in this table. If it is not available,
                                 a new record is created.

Field Name

Description

Storage

recordid

Unique identifier of the record.

int

NOT NULL

Primary Key

profileid

Profile ID of the node.

int

NOT NULL

Primary Key

promptid

Unique identifier for the prompt file or folder assigned to the application.

int

NOT NULL

type

To identify if the selection is a prompt file or folder.

0 = File

1 = Folder

Default value: 0

small int

NOT NULL

parentfolderid

The ID of parent folder of this prompt, which is stored in the assignedFolder table.

int

NOT NULL

name

Name of the prompt file or folder.

lvarchar (255)

NOT NULL

active

Indicates whether the record is active in the Unified CCX system. A record becomes inactive if a prompt file or folder is
                                             renamed or deleted ( name ).

f = Inactive

t - Active

boolean

dateinactive

Date and Time at which, the record is marked as inactive.

Default value: NULL

date time year to second

### AuditResidualSkills

Database table name : audit_residualskills

The Unified CCX system stores the skills or competencies that could not be removed due to overlapping skills across queues
                                 in the AuditResidualSkills table.

Field Name

Description

Storage

recordid

Unique identifier for the record.

Default value = 0

int

NOT NULL

Primary Key

resourceloginid

The resource login ID.

nvarchar(50)

NOT NULL

skillid

Numeric identifier of the skill that was not removed from the audit_skillgroup table.

int

NOT NULL

fromcompetency

Agent’s existing skill level that was not removed from the audit_skillgroup table.

int

NOT NULL

tocompetency

Agent’s modified skill level that was not removed from the audit_skillgroup table.

int

NOT NULL

operation

The type of operation performed on the skill that was not removed from the audit_skillgroup table.

smallint

NOT NULL

residualparentid

Record ID of the audit_reskill table, which is the parent of the residual entity.

Default value = 0

int

NOT NULL

active

Indicates if the record is active or not.

Default value = f, which indicates that the record is inactive. The record is inactive when you remove the residual skill
                                             or modify the competency.

t = Indicates that the record is active. The record is active when the residual skill exists in the resource.

boolean

NOT NULL

dateinactive

Date and Time at which, the record is made inactive.

datetime year to second

The values in the skillid, fromcompetency, tocompetency, and operation fields are the same as that of the corresponding record
                                             in the audit_skillgroup table.

### AuditReskill

Database table
                                    			 name : audit_reskill

The Unified CCX system creates a new record in the audit_reskill table for addition, deletion, and increase or decrease in
                                 the competency level of resources or CSQ skills.

Supervisors can revert the changes that are made to the resource skills either manually or through the Auto-Removal option
                                 from the Supervisor desktop.

Field
                                             					 Name

Description

Storage

recordID

Numeric
                                             					 identifier of the record.

int

NOT NULL

Primary
                                             					 Key

profileID

Identifier of the Unified CCX profile that is associated with
                                             					 this record.

int

NOT NULL

Primary
                                             					 Key

resourceLoginID

User ID
                                             					 in the Unified CM configuration.

nvarchar(50,0)

NOT NULL

csqID

Numeric
                                             					 identifier for the CSQ.

int

NOT NULL

operation

The type
                                             					 of operation performed on the resource or CSQ:

Resource_Modified(1)

Csq_Modified(2)

Csq_Added(3)

Csq_Deleted(4)

Skill_Deleted(5)

smallint

NOT NULL

result

The
                                             					 resultant action because of type of operation performed on the resource:

Added_to_csq(1)

Removed_from_csq(2)

smallint

NOT NULL

skillgrouprecordid

The
                                             					 record ID corresponding to the skill group from the audit_skillgroup table for
                                             					 a CSQ.

int

NOT NULL

reskiller

Login ID
                                             					 of the user.

nvarchar(100,0)

NOT NULL

reskiller_type

Resource
                                             					 is reskilled by:

Supervisor(1)

Admin(2)

System(3)

smallint

NOT NULL

reskilledtimestamp

Date and
                                             					 Time this record was changed.

datetime
                                             					 year to fraction(3)

NOT NULL

active

Indicates whether the record is active based on the values in
                                             					 the "result" field in the audit_reskill table.

True=The record is active when a resource is added to a CSQ and
                                                   						  the value of the "result" field is "Added_to_csq".

False =The record is inactive when the resource is removed from
                                                   						  the CSQ and the value of the "result" field is "Removed_from_csq". If an active
                                                   						  record exists for the same resource and the same CSQ, then this record is alo
                                                   						  marked inactive.

boolean

NOT NULL

### AuditSkillGroup

Database table name : audit_skillgroup

The Unified CCX system creates a new record in the audit_skillgroup table when resources are added or removed from a CSQ.
                                 This record is created when addition, deletion, or increase or decrease in the competency level of a resource skill.

Field Name

Description

Storage

recordID

Numeric identifier of the record.

int

NOT NULL

Primary Key

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

skillID

Numeric identifier of the skill.

int

NOT NULL

Primary Key

fromcompetency

Existing skill level of the agents. Values range from 1 (lowest) to 10 (highest).

int

NOT NULL

tocompetency

Modified skill level of the agents. Values range from 1 (lowest) to 10 (highest).

int

NOT NULL

operation

The type of operation performed on the skill:

Skill Add(1)

Skill Removed(2)

Competency Increased(3)

Competency Decreased(4)

smallint

NOT NULL

### CalendarAssociation

Database table name : CalendarAssociation

The calendar and application association is persisted in the CalendarAssociation table.

Field Name

Description

Storage

recordid

Unique identifier of the record.

serial

NOT NULL

Primary Key

calendarid

A unique identifier for the calendar.

int

NOT NULL

entity

Application name or the chat widget ID associated with the calendar.

nvarchar(50)

NOT NULL

entitytype

Indicates whether the calendar is associated with an application or a chat widget.

smallint

NOT NULL

active

Indicates wheather the record is deleted.

boolean

NOT NULL

dateinactive

Date and time when the record was deleted.

datetime year to second

### Campaign

Database table name : Campaign

The campaign
                                 		  configuration information is stored in this table. A campaign is associated
                                 		  with one or more CSQs. This mapping of Campaigns and CSQs is stored separately
                                 		  in CampaignCSQMap table.

Field Name

Description

Storage

recordid

A unique
                                                					 identifier for the record.

int

NOT NULL

Primary
                                                					 Key

campaignid

A unique
                                                					 identifier for the campaign.

int

NOT NULL

Primary
                                                					 Key

profileid

Identifier
                                                					 of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary
                                                					 Key

createdatetime

Default
                                                					 -CURRENT_TIMESTAMP

datetime
                                                					 year to second

NOT NULL

campaignname

Name of
                                                					 the campaign. Must be unique.

nvarchar(10)

NULL

enabled

0 =
                                                      						  campaign is enabled

1 =
                                                      						  campaign is disabled

smallint

NOT NULL

description

A
                                                					 description of the campaign.

varchar(50)

NULL

starttime

When the
                                                					 campaign starts (based on server time). This is stored in minutes.

int

NOT NULL

endtime

When the
                                                					 campaign ends (based on server time). This is stored in minutes.

int

NOT NULL

cachesize

Number
                                                					 of contacts to be retrieved in a batch for dialing for this campaign.

int

NOT NULL

maxattempts

Maximum
                                                					 number of attempts made to dial a contact for this campaign.

int

NOT NULL

ansmachineretry

0 =
                                                					 Dialer should try dialing a contact again if it reached an answering machine

1 =
                                                					 Dialer should not try dialing a contact again if it reached an answering
                                                					 machine

smallint

NOT NULL

callbacktimelimit

The
                                                					 amount of time in minutes before and after the scheduled callback time, during
                                                					 which the Dialer attempts a callback.

int

NULL

missedcallbackaction

Indicates what the Dialer should do if a callback could not be
                                                					 placed at the scheduled time:

0 =
                                                					 reschedule callback to same time the next business day

1 = make
                                                					 an ordinary retry

2 =
                                                					 close record

int

NULL

privatedata

Any
                                                					 fields which are used internally only can be stored in this column in a blob.

BLOB

NULL

active

Indicates whether the record is active in the system. A record
                                                					 becomes inactive if the campaign is deleted from the system.

f =
                                                					 Inactive

t =
                                                					 Active

boolean

NOT NULL

dateinactive

Date
                                                					 this record was deleted.

datetime
                                                					 year to second

NULL

dialertype

The type
                                                					 of the dialer used for the campaign. The dialer can be any one of the following
                                                					 three types - Predictive, Progressive or Preview Outbound.

0 -
                                                					 Direct Preview Dialer

1 - IVR
                                                					 based Predictive Dialer

2 - IVR
                                                					 based Progressive Dialer

Default
                                                					 value = 0

smallint

NOT NULL

campaignType

The
                                                					 campaign type can be IVR-based or ICD-based.

0 - IVR
                                                					 based campaign

1 -
                                                					 Agent based campaign

Default
                                                					 value = 1

smallint

NOT NULL

campaignCallingNum

The
                                                					 campaign calling number that is displayed to the contact. This number is used
                                                					 by the outbound IVR dialer.

This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive.

BLOB

NULL

applicationTrigger

This is
                                                					 the JTAPI trigger associated with this campaign.

This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive.

BLOB

NULL

applicationName

The name
                                                					 of the application associated with the above-mentioned JTAPI trigger.

This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive.

BLOB

NULL

### CampaignCSQMap

Database table name : CampaignCSQMap

The CampaignCSQMap
                                 		  table shows the relationship between campaigns and contact service queues
                                 		  (CSQs). A new record is created in the CampaignCSQMap table when a campaign is
                                 		  associated with a CSQ in Unified CCX Administration.

Field Name

Description

Storage

recordid

A unique
                                                					 identifier for the record

int

NOT NULL

Primary
                                                					 Key

campaignid

A unique
                                                					 identifier for the campaign, from the Campaign table.

int

NOT NULL

Primary
                                                					 Key

csqid

A unique
                                                					 identifier for the CSQ, from the ContactServiceQueue table.

int

NOT NULL

Primary
                                                					 Key

active

Indicates
                                                					 whether the record is active in the system. A record becomes inactive if the
                                                					 campaign is deleted from the system.

f =
                                                					 Inactive

t = Active

smallint

NULL

createdatetime

Default,
                                                					 CURRENT_TIME_STAMP

datetime
                                                					 year to second

NULL

dateinactive

Date this
                                                					 record was deleted.

datetime
                                                					 year to second

NULL

### CampaignSupervisorMap

Database table name : CampaignSupervisorMap

The
                                 		  CampaignSupervisorMap table shows the relationship between campaign and
                                 		  supervisor associated with that campaign. A new record is created in the
                                 		  CampaignSupervisorMap table when a campaign is associated with a supervisor in
                                 		  Unified CCX Administration.

Field Name

Description

Storage

recordid

A unique
                                                					 identifier for the record

int

NOT NULL

Primary
                                                					 Key

campaignid

A unique
                                                					 identifier for the campaign, from the Campaign table.

int

NOT NULL

Primary
                                                					 Key

supervisorid

A unique
                                                					 identifier for the supervisor, based on the supervisor’s resourceloginid.

nvarchar(50,0)

NOT NULL

Primary
                                                					 Key

active

Indicates
                                                					 whether the record is active in the system. A record becomes inactive if the
                                                					 campaign is deleted from the system.

f =
                                                					 Inactive

t = Active

boolean

NOT NULL

createdatetime

Default,
                                                					 CURRENT_TIME_STAMP

datetime
                                                					 year to second

NOT NULL

dateinactive

Date this
                                                					 record was deleted.

datetime
                                                					 year to second

NULL

### CampaignData

Database table name : CampaignData

If you have
                                 		  configured a campaign as an outbound IVR campaign and have chosen Predictive
                                 		  dialer type, the number of lines per port along with the other parameters are
                                 		  stored in the CampaignData table every half hour.

Field Name

Description

Storage

recordId

A unique identifier for the record

int

NOT NULL

Primary Key

campaignId

The campaign for which the data is recorded

int

NOT NULL

Primary Key

startDate

Start date
                                                					 and time of the interval

datetime
                                                					 year to fraction

NOT NULL

endDate

End date
                                                					 and time of the interval

datetime
                                                					 year to fraction

NOT NULL

attemptedCalls

The number
                                                					 of attempted calls in the interval

int

NOT NULL

abandonedCalls

The number
                                                					 of abandoned calls in the interval

int

NOT NULL

voiceCalls

The number
                                                					 of voice calls in the interval

int

NOT NULL

linesPerPort

Lines Per
                                                					 Port value computed depending on the abandoned calls/voice calls

decimal(8,
                                                					 3)

NOT NULL

active

Indicates
                                                					 whether the data stored is for an active campaign or not.

f =
                                                					 Inactive

t = Active

boolean

NOT NULL

dateinactive

The date
                                                					 on which this campaign was deleted

datetime
                                                					 year to fraction

### CCCalendar

Database table name : CCCalendar

This table stores the calendar information.

Field Name

Description

Storage

recordid

A unique identifier for the record.

serial

NOT NULL

Primary Key

calid

A unique identifier for the calendar.

int

NOT NULL

name

Name of the calendar.

lvarchar (30)

NOT NULL

description

The description of the calendar that is configured in the Unified CCX Administration Calendar Management.

lvarchar (70)

NULL

timezone

The time zone of the calendar.

nvarchar (50)

NOT NULL

caltype

Indicates the type of calendar.

1—Full time

2—Flexible

smallint

NOT NULL

hasspecialdays

Indicates the availability of the special days.

boolean

NOT NULL

hasholidays

Indicates the availability of the holidays.

boolean

NOT NULL

active

Indicates whether the record is currently active or not.

f = Inactive

t = Active

boolean

NOT NULL

dateinactive

Date and time of the record when it is marked as inactive.

DATETIME year to second

NULL

### CCHolidays

Database table name : CCHolidays

This table stores the configured business holidays of a calendar.

Field Name

Description

Storage

recordid

A unique identifier for the record.

serial

NOT NULL

Primary Key

calid

A unique identifier for the calendar.

int

NOT NULL

name

Name of the calendar.

nvarchar (50)

NOT NULL

caldate

Date of the special day.

DATETIME YEAR TO DAY

NOT NULL

active

Indicates whether the record is currently active or not.

f = Inactive

t = Active

boolean

NOT NULL

dateinactive

Date and time of the record when it is marked as inactive.

DATETIME year to second

NULL

### ChannelProvider

Database table name : ChannelProvider

This table
                                 		  contains the channel provider configurations, including the type of channel,
                                 		  and server details with fully qualified domain name (FQDN), protocol, and port.
                                 		  Channel providers enable the use of non-interactive media channels such as
                                 		  email with Unified CCX.

Field Name

Description

Storage

Id

Unique
                                                					 identifier of the channel provider. Server ID is the foreign key that
                                                					 associates this table with the ContactServiceQueue table.

int

NOT NULL

Primary
                                                					 Key

channelType

Type of
                                                					 contact channel.

varchar
                                                					 (20, 0)

NOT NULL

sendserverfqdn

FQDN of
                                                					 the channel provider for sending the channel type.

Varchar(255, 0)

NOT NULL

sendprotocol

Sending
                                                					 protocol that is used to communicate with the channel provider.

Varchar(20, 0)

NOT NULL

sendserverport

16-bit
                                                					 port number that is used to communicate with the channel provider for sending
                                                					 the channel type.

int

NOT NULL

receiveserverfqdn

FQDN of
                                                					 the channel provider for receiving the channel type.

Varchar(255, 0)

NOT NULL

receiveprotocol

Receiving
                                                					 protocol that is used to communicate with the channel provider.

Varchar(20, 0)

NOT NULL

receiveserverport

16-bit
                                                					 port number that is used to communicate with the channel provider for receiving
                                                					 the channel type.

int

NOT NULL

description

Description of the channel provider.

Lvarchar(400)

active

Indicates whether the record is currently active or not. A
                                                					 record becomes inactive if the record is deleted or updated from the system.

f =
                                                					 Inactive

t =
                                                					 Active

Boolean

NOT NULL

dateinactive

If the
                                                					 active field is “f”, this field indicates the date and time that the record
                                                					 became inactive.

datetime
                                                					 year to second

proxytype

Indicates whether Enable/Disable option is selected for SOCKS
                                                					 Proxy in Mail server configuration page.

Lvarchar(25)

mailservertype

Indicates the mail server type. The default is microsoft.

Lvarchar(50)

### ChatProblemStatement

Database table name : ChatProblemStatement

This table contains the associated problem statements and tag ids for
                                 		  each chat widget. Chat widget is the widget that enables the Unified CCX
                                 		  Administrator to create a chat interface for the end user.

Field Name

Description

Storage

wdID

Unique ID for each chat widget. It is the foreign key which
                                                					 associates this table with the chatwidget table.

int

NOT NULL

Primary Key

tagID

The tagID for the csq associated with the problem statement.

nvarchar(50)

NOT NULL

problemStmt

The definition of the problem.

lvarchar (256)

NOT NULL

psOrder

Order of the problem statement in the chat widget.

int

NOT NULL

Primary Key

### ChatScheduledHours

Database table name : ChatScheduledHours

This table stores the custom weekly business hours configured by administrator.

Field Name

Description

Storage

profileId

A unique identifier for the record.

int

NOT NULL

Primary Key

wdID

A unique ID for each widget.

int

NOT NULL

Primary Key

scheduledDay

Scheduled working days in a week.

LVARCHAR(3)

NOT NULL

fromTime

Start time of business hours.

int

NOT NULL

toTime

End time of business hours.

int

NOT NULL

active

Indicates whether the widget is currently active or not.

f = Inactive

t = Active

boolean

NOT NULL

dateinactive

The date and time when the record became inactive.

datetime year to second

### ChatScheduledSpecialDays

Database table name : ChatScheduledSpecialDays

This table stores the business holidays and specially extended hours for specific days.

Field Name

Description

Storage

profileId

A unique identifier for the record.

int

NOT NULL

Primary Key

wdID

A unique ID for each widget.

int

NOT NULL

Primary Key

customType

Scheduled business holiday or the special day.

small int

NOT NULL

name

Name of the business holiday or the special day.

LVARCHAR(256)

NOT NULL

dateConfigured

Date of the business holiday or the special day.

datetime year to second

NOT NULL

fromTime

Start time of business hours.

int

toTime

End time of business hours.

int

active

Indicates whether the widget is currently active or not.

f = Inactive

t = Active

boolean

NOT NULL

dateinactive

The date and time when the record became inactive.

datetime year to second

### ChatTriggerPoint

Database table name : ChatTriggerPoint

This table describes chat CSQ tag information. A ChatTriggerPoint is
                                 		  uniquely identified by a csqID and a chattriggerpointname. Chat contacts
                                 		  inserted into Unified CCX are queued to respective CSQs based on the
                                 		  chattriggerpointname present in the contact. When a chat CSQ is created, a new
                                 		  record is inserted into this table. When a CSQ is modified, the old record is
                                 		  marked as inactive, and a new record is inserted into the table with a the new
                                 		  csqID. When a CSQ is deleted, the corresponding record is marked as inactive.

Field Name

Description

Storage

csqID

Numeric identifier for the CSQ.

int

NOT NULL

chattriggerpointname

Name of fields present in the chat trigger point.

Ivarchar(256)

NOT NULL

active

Indicates whether the record is currently active.

f = Inactive

t = Active

boolean

NOT NULL

dateinactive

If the active field is “f”, date and time that the record
                                                					 became inactive.

Datetime year to fraction(3)

NULL

### ChatUserForm

Database table name : ChatUserForm

This table contains the user form fields included in each chat widget
                                 		  along with the order of the fields in the widget.

Field Name

Description

Storage

wdID

Unique ID for each chat widget. It is the foreign key which
                                                					 associates this table with the chatwidget table.

int

NOT NULL

Primary Key

fieldName

Name of fields present in the user form.

lvarchar (200)

NOT NULL

fieldID

ID of fields present in the user form.

int

NOT NULL

Primary Key

fieldOrder

Order of the field in the widget.

smallint

NOT NULL

active

Indicates whether the record is currently active or not.

f = Inactive

t = Active

Boolean

NOT NULL

lastmodifieddate

The date and time when the user form details were last
                                                					 modified.

datetime year to fraction (3)

### ChatWidget

Database table name : ChatWidget

This table stores the chat widget information.

Field Name

Description

Storage

wdID

A unique
                                                					 ID for each widget.

int

NOT NULL

Primary
                                                					 Key

wdName

Name of
                                                					 the widget.

lvarchar (50)

NOT NULL

wdDescription

The
                                                					 description of the widget that is configured in the Unified CCX Administration.

lvarchar
                                                					 (256)

NULL

wdWelcome

The
                                                					 welcome message that is displayed when the customer joins the chat sessions.

lvarchar
                                                					 (256)

NULL

wdLogo

The
                                                					 Location of the logo file that is displayed in the customer facing chat widget.

lvarchar
                                                					 (256)

NULL

wdError

The message that is displayed to the customer when the chat is unavailable.

lvarchar (360)

wdJoinTimeout

The
                                                					 message that is displayed to the customer when a chat request is not handled
                                                					 within the set time.

lvarchar
                                                					 (256)

NULL

wdCode

Blob data
                                                					 to store the HTML code generated for the widget.

BLOB

NULL

active

Indicates
                                                					 whether the widget is currently active or not.

f =
                                                					 Inactive

t = Active

boolean

NOT NULL

lastModifiedDate

The date
                                                					 and time on which the widget details were last modified.

datetime
                                                					 year to fraction (3)

NULL

offHoursMessage

A
                                                					 message to be displayed off the scheduled business hours.

lvarchar
                                                					 (256)

NULL

wdType

Indicates the type of widget:

0- Chat Bubble

small
                                                					 int

NOT NULL

Default
                                                					 0

### ChatBubble

Database table name : ChatBubble

This table stores the chat bubble information.

Field Name

Description

Storage

recordId

A unique ID for a set of chat bubble properties.

int

NOT NULL

Primary Key

wdId

The ID of the chat widget record that contains the chat bubble record. It is the foreign key which associates this table with
                                             the chatwidget table.

int

NOT NULL

Primary Key

titleText

Title text of the chat bubble.

lvarchar (96)

NOT NULL

titleTextColor

Text color of the chat bubble title in hex code.

lvarchar (7)

NOT NULL

titleBackgroundColor

Background color of the chat bubble title text in hex code.

lvarchar (7)

NOT NULL

Default #EBEBEC

buttonText

The text of the chat button.

lvarchar (60)

NOT NULL

buttonTextColor

Color of the chat button text in hex code.

lvarchar (7)

NOT NULL

buttonBackgroundColor

Background color of the chat button in hex code.

lvarchar (7)

NOT NULL

afterResumeNewChatMsg

Text on the chat window that demarks new chat messages from old ones.

lvarchar (60)

NOT NULL

agentMessageTextColor

Color of the agent message text in hex code.

lvarchar (7)

NOT NULL

agentMessageBackgroundColor

Background color of the agent message in hex code.

lvarchar(7)

NOT NULL

fontTypeFace

Font family used for the text in the chat web form and chat window.

lvarchar (120)

NOT NULL

problemStmtCaption

Label that asks the user to choose a problem statement.

lvarchar (120)

NOT NULL

ratingEnabled

Whether post-chat rating is available for the chat.

boolean

NOT NULL

active

Indicates whether the entry is active or inactive.

f= Inactive

t= Active

boolean

NOT NULL

dateInactive

Date when the record became inactive.

datetime year to second

### ConsultLegDetail

Database table name : ConsultLegDetail

The Unified CCX system creates a new record in the ConsultLegDetail table when agents are in a consult call.

Field Name

Description

Storage

sessionid

Identifier that the system assigns to the call.

decimal (18, 0)

NOT NULL

Primary Key

sessionseqnum

Session sequence number that the system assigns to the call.

smallint

NOT NULL

nodeid

Unique identifier assigned to each server in the cluster.

smallint

NOT NULL

sourceresourceid

Identifier of the agent who initiated the consult call.

int

NOT NULL

destinationresourceid

Identifier of the agent who answered the call.

int

NOT NULL

startdatetime

Date and time when agents are connected and start conversation.

datetime year to fraction (3)

NOT NULL

enddatetime

Date and time when the call is disconnected.

datetime year to fraction (3)

NOT NULL

contactid

Unique Identifier for the contact.

varchar (40)

NOT NULL

csqrecordid

Numeric identifier of the selected CSQ for CSQ-based calls, else -1 is stored.

int

NOT NULL

### ContactCallDetail

Database table name : ContactCallDetail

The Unified CCX system creates a new record in the ContactCallDetail table for each call or call leg that is processed by
                                 the system. A new call leg starts each time a call is transferred or redirected, except when a call is transferred from a
                                 Cisco CTI port to an agent.

A ContactCallDetail record contains detailed information about the call or leg. A minimum of one such record will exist for
                                 each call.

Field Name

Description

Storage

sessionID

Identifier that the system assigned to the call. This identifier remains the same for all legs of the call.

decimal(18,0)

NOT NULL

Primary Key

sessionSeqNum

Session sequence number that the system assigned to the call or the leg. Each leg of a call is assigned a new sequence number.

smallint

NOT NULL

Primary Key

nodeID

Unique identifier that is assigned to each server in the cluster.

smallint

NOT NULL

Primary Key

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

contactType

Contact type of the call or the leg:

1—Incoming. Outside call received by the Unified CCX system.

2—Outgoing. Call originated by the Unified CCX system, other than a call made within the system.

3—Internal. Call transferred or conferenced between agents, or a call made within the system.

4—Redirect in

5—Transfer in

6—Preview Outbound

7—IVR Outbound

8—Agent Outbound

9—Agent Outbound call that is transferred to IVR

smallint

NOT NULL

contactDisposition

Disposition of the call or the leg.

1—Abandoned

2—Handled

3—Do not care

4—Aborted 1

5-22—Rejected

99—Cleared

smallint

NOT NULL

dispositionReason

Reason for disposition.

1—System Error

2—Consult Transfer

3—Blind Transfer

5—Blind Transfer to Experience Management for IVR Survey

6—SIPURI Retrieval Failure for Experience Management Survey

7—JTAPI Transfer Failure for Experience Management Survey

8—Notified Experience Management for SMS/Email Survey

varchar(100,0)

NULL

originatorType

Originator of the call or the leg:

1—Agent. Call originated by an agent.

2—Device. Call originated by a simulated caller (used for testing) and an agent phone where the agent is not currently logged
                                                   in.

3—Unknown. Call originated by an outside caller through a gateway or by an unknown device.

smallint

NOT NULL

originatorID

Numeric identifier of the agent who originated the call or the leg.

Used only if originatorType is 1.

int

NULL

originatorDN

If originatorType is 1 and the call was placed by the agent using the non-IPCC extension then this field contains the non-IPCC
                                             extension, else it contains an empty character ('').

If originatorType is 2, this field shows the CTI port number.

If originatorType is 3, this field shows the telephone number of the caller as received by the Unified CM, if available.

An empty character ('') if originatorType is 1. This is not applicable for agent based progressive and predictive outbound
                                             calls.

nvarchar(30,0)

NULL

destinationType

Destination of the call or the leg:

1—Agent. Call presented to an agent.

2—Device. Call presented to a route point.

3—Unknown. Call presented to an outside destination through a gateway or to an unknown device.

Null if no destination.

smallint

NULL

destinationID

Numeric identifier of the agent who received the call or the leg.

Used only if destinationType is 1.

int

NULL

destinationDN

If the destinationType is 1 and the call was received by an agent using the non-IPCC extension, then this field contains the
                                             non-IPCC extension, else it contains an empty character ('').

If destinationType is 2, this field shows the CTI port number.

If destinationType is 3, this field shows the telephone number called, if available.

An empty character ('') if destinationType is 1.

nvarchar(30)

NULL

startDateTime

For an incoming call or a leg, date and time that the call or the leg started to ring in the system.

For an internal call or for an outgoing call, date and time that the call originated.

For a transferred call or a leg, endDateTime of the transferring call or leg.

datetime year to fraction (3)

NOT NULL

endDateTime

Date and time that this call or the leg was transferred or was disconnected.

datetime year to fraction (3)

NOT NULL

gmtOffset

Offset, in minutes, between the local time of the Unified CCX server and Greenwich Mean Time. As the time information is stored
                                             in GMT, this field will always be zero.

smallint

NOT NULL

calledNumber

Telephone number of the device to which the call or leg was presented.

If the call or leg was placed to a Unified CCX Route Point, this field shows the directory number configured in the Unified
                                             CM for that Route Point.

If the call was placed to an external party, this field shows the telephone number dialed by the caller.

nvarchar(30)

NULL

origCalledNumber

Telephone number dialed by the caller if the call was placed from an IP phone.

The Unified CM directory number to which the VoIP gateway routed the call if the call was placed from outside the VoIP 2 network (for example, from the PSTN 3 or a TDM 4 PBX 5 ).

Null if the caller picked up the phone but did not dial any digits.

nvarchar(30)

NULL

applicationTaskID

Identifier of the Unified CCX or Cisco Unified IP IVR 6 (Unified IP IVR) application task that is associated with the call or the leg.

Null for a call that does not have an application associated with it.

decimal(18,0)

NULL

applicationID

Identifier of the Unified CCX or Unified IP IVR application that processed the call or the leg.

Null for a call or a leg that does not have an application associated with it.

int

NULL

applicationName

Name of the Unified CCX or Unified IP IVR application associated with the call.

Null for a call or a leg that does not have an application associated with it.

nvarchar(30)

NULL

connectTime

Duration of the call in seconds.

int

NULL

customVariable1

Contents of the variable _ccdrVar1, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked.

Null if this variable is not set.

varchar(40)

NULL

customVariable2

Contents of the variable _ccdrVar2, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked.

Null if this variable is not set.

varchar(40)

NULL

customVariable3

Contents of the variable _ccdrVar3, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked.

Null if this variable is not set.

varchar(40)

NULL

customVariable4

Contents of the variable _ccdrVar4, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked.

Null if this variable is not set.

varchar(40)

NULL

customVariable5

Contents of the variable _ccdrVar5, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked.

Null if this variable is not set.

varchar(40)

NULL

customVariable6

Contents of the variable _ccdrVar6, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked.

Null if this variable is not set.

varchar(40)

NULL

customVariable7

Contents of the variable _ccdrVar7, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked.

Null if this variable is not set.

varchar(40)

NULL

customVariable8

Contents of the variable _ccdrVar8, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked.

Null if this variable is not set.

varchar(40)

NULL

customVariable9

Contents of the variable _ccdrVar9, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked.

Null if this variable is not set.

varchar(40)

NULL

customVariable10

Contents of the variable _ccdrVar10, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked.

Null if this variable is not set.

varchar(40)

NULL

accountNumber

Account number entered by the caller.

varchar(40)

NULL

callerEnteredDigits

Phone number entered by the caller.

varchar(40)

NULL

badCallTag

Tag for a bad call.

Default = N

char(1)

NULL

transfer

Was this call leg transferring the call:

t = transfer

f = no

boolean

NULL

redirect

Was this call leg redirecting the call:

t = redirect

f = no

boolean

NULL

conference

Was this call leg conferencing the call:

t = conference

f = no

boolean

NULL

flowout

When this flag is set, it means this call leg is sent to another application or destination outside the system.

boolean

NULL

metServiceLevel

Did the call meet the service level:

t = met service level

f = no

Note: Reserved for future use.

boolean

NULL

campaignID

Unique identifier of the campaign that generated this call.

int

NULL

OrigProtocolCallRef

Unique identifier to identify a call leg that enters the Unified CCX system. This is used to trace a call which has traversed
                                             from some product to the Unified CCX.

Varchar(32)

NULL

DestProtocolCallRef

Unique Identifier to identify a call leg that exits the Unified CCX system. This is used to trace a call which has traversed
                                             from Unified CCX to some other product.

Varchar(32)

NULL

CallResult

The result of an IVR based or agent based progressive or predictive outbound call.

smallint

NULL

dialingListID

Unique identifier of a contact that is dialed for an outbound campaign. Links with DialingList.dialingListID.

int

NULL

contactid

A unique identifier for all the records related to a single call across various tables in Unified CCX.

varchar(40)

lastleg

Indicates whether this is the last leg corresponding to the original call.

boolean

### ContactHoldDetail

Database table name : ContactHoldDetail

The Unified CCX system creates a new record in the ContactHoldDetail table each time a contact is put on hold.

Field Name

Description

Storage

contact id

varchar(40)

NOT NULL

sessionID

An identifier that the system assigns to the call. This

decimal(18,0)

NOT NULL

sessionSeqNum

A session sequence number that the system assigns to the call or the call leg. Each leg of the call is assigned a new sequence
                                          number.

smallint

NOT NULL

startDateTime

Date and time the call was put on hold.

datetime year to fraction(3)

NOT NULL

endDateTime

Date and time the call changed from hold state to retrieved or disconnected state.

datetime year to fraction(3)

NOT NULL

type

Indicates the hold initiation type.

1 - Agent Initiated

2 - System Initiated

smallint

NOT NULL

resourceid

Identifier of the agent who has put the call on hold.

int

NOT NULL

### ContactQueueDetail

Database table name : ContactQueueDetail

The Unified CCX system writes the record when the call is queued for CSQs. Then, one of the following happens:

Call is abandoned while queued for CSQs

Call is being dequeued

Caller is connected to an agent

Field Name

Description

Storage

sessionID

Identifier that the system assigned to the call. This identifier remains the same for all legs of the call.

decimal(18,0)

NOT NULL

Primary Key

sessionSeqNum

Session sequence number that the system assigned to the call or the leg. Each leg of a call is assigned a new sequence number.

smallint

NOT NULL

Primary Key

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

nodeID

Unique identifier assigned to each server in the cluster.

smallint

NOT NULL

Primary Key

targetID

Numeric ID of the CSQ or the agent depending upon the targetType.Numeric ID of the CSQ or the agent depending upon the targetType.

0—Numeric record ID of the CSQ. (See record ID description in the Contact Service Queue Table)

1—Numeric agent ID (see resourceID description in the Resource Table)

int

NOT NULL

Primary Key

targetType

Indicates whether the call was queued for a CSQ or for an agent.

0 = CSQ

1 = Agent

smallint

NOT NULL

Primary Key

qIndex

For all the new calls that are coming to an agent’s extension through a route point, the value of qIndex is 1. Thereafter,
                                             the value of qIndex is incremented by 1, whenever there is a conference through the route point.

smallint

NOT NULL

Primary Key

queueOrder

The order of the call in the queue.

smallint

NOT NULL

disposition

Disposition for this leg of the call for this CSQ.

Abandoned = 1 7

Handled by CSQ = 2

Dequeued from CSQ = 3

Handled by script = 4

Handled by another CSQ = 5

smallint

NULL

metServiceLevel

Call answered within the configured number of seconds of queue time for this CSQ.

Yes = t

No = f

boolean

NULL

queueTime

Number of seconds that the caller spent in this CSQ.

int

NULL

startDateTime

Date and time of an incoming call that is queued to a particular CSQ.

datetime year to fraction (3)

endDateTime

Date and time of an incoming call that is dequeued from a particular CSQ.

datetime year to fraction (3)

contactid

A unique identifier for all the records related to a single call across various tables in Unified CCX.

varchar(40)

### ContactRoutingDetail

Database table name : ContactRoutingDetail

The Unified CCX
                                 		  system creates a new record in the ContactRoutingDetail table for each Unified
                                 		  CCX call or call leg that is queued for one or more CSQs. A new call leg starts
                                 		  each time that a call is transferred or redirected, except when a call is
                                 		  transferred from a Cisco CTI port to an agent. The system also creates a new
                                 		  record in the ContactRoutingDetail table if a call is conferenced to a Unified
                                 		  CCX script.

A
                                 		  ContactRoutingDetail record contains information about call priority and
                                 		  accumulated queue time. This differs from the ContactQueueDetail record which
                                 		  shows individual queue time for each CSQ.

Field Name

Description

Storage

sessionID

Identifier that the system assigned to the call. This identifier remains the same for all legs of the call.

decimal(18, 0)

NOT NULL

Primary Key

sessionSeqNum

Session sequence number that the system assigned to the call or the leg. Each leg of a call is assigned a new sequence number.

smallint

NOT NULL

Primary Key

nodeID

Unique identifier assigned to each server in the cluster.

smallint

NOT NULL

Primary Key

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

qIndex

For all the new calls that are coming to an agent’s extension through a route point, the value of qIndex is 1. Thereafter,
                                             the value of qIndex is incremented by 1, whenever there is a conference through the route point.

smallint

NOT NULL

Primary Key

origPriority

Priority level assigned to the call or the leg when it was first queued.

Null if a priority was not assigned.

smallint

NULL

finalPriority

Priority level of the call or the leg when it ended.

Null if a priority was not assigned.

smallint

NULL

queueTime

Time (in seconds) that the call was in queue before an agent picked up the call. If the call was in multiple CSQs, then it
                                             is the total time that the call has spent in multiple CSQs.

int

NULL

startDateTime

For an incoming call or a leg, date and time that the call or the leg was queued for the first CSQ.

datetime year to fraction (3)

NOT NULL

contactid

A unique identifier for all the records related to a single call across various tables in Unified CCX.

varchar(40)

### ContactServiceQueue

Database table name : ContactServiceQueue

The Unified CCX
                                 		  system creates a new record in the ContactServiceQueue table when a CSQ is set
                                 		  up in Unified CCX Administration.

A
                                 		  ContactServiceQueue record contains information about the CSQ. One such record
                                 		  exists for each active and inactive CSQ. When a CSQ is deleted (deactivated),
                                 		  its record still remains in the database marked as inactive; that is, the
                                 		  active field value is “f”.

Field Name

Description

Storage

contactServiceQueueID

Numeric identifier of the CSQ. This ID does not change when CSQ attributes are changed through the Unified CCX Administration
                                             user interface.

int

NOT NULL

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

CSQName

Name of the CSQ as set up in Unified CCX Administration.

nvarchar(50,0)

NOT NULL

resourcePoolType

Type of resource pool that is set up in Unified CCX Administration:

1—Resource groups

2—Resource skills

smallint

NOT NULL

resourceGroupID

If resourcePoolType is 1, unique identifier used to locate the associated resource group in the Resource Group table.

Not used if resourcePoolType is 2.

int

NULL

selectionCriteria

Resource pool selection model that is set up in the Unified CCX Administration.

nvarchar(30,0)

NOT NULL

skillGroupID

If resourcePoolType is 2, unique identifier used to locate the associated skill group in the SkillGroup table.

Not used if resourcePoolType is 1.

int

NULL

serviceLevel

Goal, in seconds, for the maximum time that a caller spends in the queue before the call is answered by an agent, as set up
                                             in Unified CCX Administration.

int

NOT NULL

serviceLevelPercentage

Goal for the percentage of calls that meet the service level that is shown in the serviceLevel field, as set up in Unified
                                             CCX Administration.

smallint

NOT NULL

active

Indicates whether the record is active:

f = Inactive

t = Active

A record becomes inactive if the CSQ is deleted from the system or if the attributes are changed through the Unified CCX Administration
                                             user interface. When an attribute is changed, the record is marked inactive; that is, the active field is changed to “f”,
                                             and a new record is created.

boolean

NOT NULL

autoWork

Whether an agent goes to Work State after handling a call from this CSQ:

f —No

t —Yes

boolean

NOT NULL

dateInactive

If the active field is “f”, date and time that the record became inactive.

datetime year to fraction (3)

NULL

queueAlgorithm

Criterion that specifies how contacts are queued, as set up in Unified CCX Administration.

nvarchar(30,0)

NOT NULL

recordID

Identifier of this record. When any CSQ attribute, such as service level, is changed through the Unified CCX Administration
                                             user interface, the record is marked inactive; that is, the value of the active field changes to “f”, and a new record is
                                             created with a new record ID; the contactServiceQueueID stays the same for that CSQ.

int

NOT NULL

Primary Key

orderList

Reserved for future use.

int

NULL

wrapupTime

Time in seconds that agent is placed in Work state.

Possible values:

1 – 7200

0 – disabled

smallint

NULL

prompt

The prompt value is used for remote monitoring. The customer can record the name of the CSQ and store it in a WAV file. This
                                             field contains the name of the WAV file.

nvarchar (256)

NOT NULL

privateData

Any fields which are used internally only can be stored in this column in a blob.

BLOB

NULL

queueType

A type of the CSQ.

Possible values:

0 – voice CSQ

1 – email CSQ

2 – chat CSQ

smallint

NOT NULL

queueTypeName

The name displayed for the CSQ type. Possible values:

Voice

Chat

Email

nvarchar(30,0)

NULL

accountuserId

The userid of the email account mapped to an email CSQ.

nvarchar(255,0)

NULL

channelproviderId

The unique identifier for the channel provider.

int

NULL

reviewQueueId

Reserved.

int

NULL

routingType

The type of routing:

Interactive

Noninteractive

nvarchar(30,0)

NULL

foldeerName

The name of the email folder that needs to be polled for mails on the mail server.

nvarchar(255,0)

NULL

pollingInterval

The time (in seconds) on how frequently the email server is polled for any new emails.

int

NULL

snapshotAge

The time (in minutes) to indicate how far to go back to fetch emails on startup.

int

NULL

feedId

The unique identifier for the feeds from Customer Collaboration Platform .

nvarchar(30,0)

NULL

### ContactWrapupData

Database table name : ContactWrapupData

The Unified CCX system creates a new record in the contactwrapupdata table each time the agent selects a Wrap-Up reason.

Identifier that the system assigned to the call. This identifier remains the same for all legs of the call.

decimal (18)

NOT NULL

Primary Key

smallint

NOT NULL

Primary Key

int

NOT NULL

Primary Key

wrapupData

Call related information that the agent enters through the Agent Desktop user interface while the agent is in the talking/work
                                             state.

varchar (160)

NOT NULL

Primary Key

nodeid

Unique identifier assigned to each Unified CCX server in the cluster.

smallint

Primary Key

qindex

A new qIndex is created whenever a Unified CCX call is conferenced to a Unified CCX route point.

smallint

Primary Key

startDateTime

Date and time that the call or the leg started ringing at the device of an agent.

datetime year to fraction

Primary Key

wrapupindex

Unique number of wrapup reasons for a particular call. A call can have maximum of five wrapup reasons.

smallint

contactid

A unique identifier for all the records related to a single call across various tables in Unified CCX.

varchar(40)

### CrsApplication

Database table name : CrsApplication

The CrsApplication table records application information. An application is uniquely identified by applicationName. When an
                                 application is created, a new record is inserted into this table. When an application is modified, the old record is marked
                                 as inactive, and a new record is inserted into the table with a new recordID. When an application is deleted, the corresponding
                                 record is marked as inactive.

Field Name

Description

Storage

record ID

Unique numeric ID for each record. Introduced for historical reporting purposes.

Possible values: 1, 2, 3....

int

NOT NULL

Primary Key

profileID

The indentifier of the profile

int

NOT NULL

Primary Key

applicationID

Configurable application identifier. Not unique for an application. Exposed for Cisco Unified Intelligent Contact Management
                                             Enterprise (Unified ICME) integration. Configured on Unified CCX Administration, modifiable.

Possible values: -1, 1, 2, 3...

int

NOT NULL

configClass

Represents application configuration class.

Possible values:

com.cisco.app.ApplicationConfig

ApplicationConfig.class

lvarchar(512)

NOT NULL

version

Specifies internal configuration schema version.

Possible values: 1

int

NOT NULL

configImplClass

Represents application configuration implementation class.

Possible value:

com.cisco.crs.app.ScriptApplicationConfig

lvarchar(512)

NOT NULL

applicationName

Name that uniquely identifies the application

nvarchar(50,0)

NOT NULL

applicationType

The type of application.

Possible values:

Busy

Ring-No-Answer

Cisco Script Application

Simulation Script

Unified ICME Post-Routing

Unified ICME Translation Routing

nvarchar(128,0)

NOT NULL

applicationEnabled

Whether or not the application is enabled.

Possible values:

f = disabled

t = enabled

boolean

NOT NULL

numOfSessions

Maximum number of sessions

int

NOT NULL

description

The description of the application that is configured in the Unified CCX Administration.

nvarchar(128,0)

NULL

privateData

Internal data not exposed to customers.

BLOB

NULL

createDateTime

The time when the record is created or updated.

Default value: Current year to second

datetime year to second

NOT NULL

active

Whether this record is active.

Possible values:

f = inactive

t = active

boolean

NOT NULL

dateInactive

If active = f, the time when this record became inactive.

datetime year to second

NULL

surveyname

Name of the IVR survey that is associated with the application for post-call survey.

lvarchar(512)

dispatchid

The ID of the SMS/Email dispatch that is associated with the application for post-call survey.

varchar(24)

### CrsGroup

Database table name : CrsGroup table

The CrsGroup table
                                 		  describes group information. A group is uniquely identified by the combination
                                 		  of groupClassName and groupID. When a group is created, a new record is
                                 		  inserted into this table. When a group is modified, the old record is marked as
                                 		  inactive, and a new record is inserted into the table with a new recordID. When
                                 		  a group is deleted, the corresponding record is marked as inactive.

Field Name

Description

Storage

recordID

A unique
                                                					 numeric ID for each record. Introduced for historical reporting purposes.

int

NOT NULL

Primary
                                                					 Key

profileID

Indentifier of the profile

Possible
                                                					 values: 1, 2, 3....

int

NOT NULL

Primary
                                                					 Key

configClass

Represents
                                                					 Group configuration class.

Possible
                                                					 values: GroupConfig.class

lvarchar(512)

NOT NULL

version

Specifies
                                                					 internal configuration schema version.

Possible
                                                					 values: 2

int

NOT NULL

configImplClass

Represents
                                                					 group configuration implementation class.

com.cisco.crs.email.

CiscoEmailControlGroupConfig.

lvarchar(512)

NOT NULL

groupClass

Uniquely
                                                					 identifies a group together with the groupID. The class of channels being
                                                					 managed by the group.

lvarchar(400)

NOT NULL

groupID

Uniquely
                                                					 identifies a group together with groupClassName. Group identifier unique for a
                                                					 give class of channels.

int

NOT NULL

groupType

Type of
                                                					 the group, corresponding to type of the channels managed by the group as
                                                					 defined since CRS 3.0.

nvarchar(128,0)

NOT NULL

groupEnabled

Whether
                                                					 the group is enabled.

Possible
                                                					 values:

f =
                                                					 disabled

t =
                                                					 enabled

boolean

NOT NULL

numOfChannels

Number
                                                					 of channels defined in the group.

int

NOT NULL

description

Description of the group.

nvarchar(128,0)

NULL

privateData

Internal
                                                					 data not exposed to customers.

BLOB

NULL

createDateTime

When the
                                                					 group was created.

Default
                                                					 value: Current year to second

datetime
                                                					 year to second

NOT NULL

active

Whether
                                                					 this record is active.

Possible
                                                					 values:

f =
                                                					 inactive

t =
                                                					 active

boolean

NOT NULL

dateInactive

If
                                                					 active = f, the time when the record became inactive.

datetime
                                                					 year to second

NULL

### CrsTrigger

Database table name : CrsTrigger

The CrsTrigger
                                 		  table describes trigger information. A trigger is uniquely identified by a
                                 		  trigger name (triggerName). When a trigger is created, a new record is inserted
                                 		  into this table. When a trigger is modified, the old record is marked as
                                 		  inactive, and a new record is inserted into the table with a new recordID. When
                                 		  a trigger is deleted, the corresponding record will be marked as inactive.

Field Name

Description

Storage

recordID

Unique
                                                					 numeric ID for each record. Introduced for historical reporting purposes.

int

NOT NULL

Primary
                                                					 Key

profileID

Indentifier of the profile

Possible
                                                					 values: 1, 2, 3....

int

NOT NULL

Primary
                                                					 Key

configClass

Represents
                                                					 trigger configuration class.

Possible
                                                					 values:

ApplicationTriggerConfig.class

lvarchar(512)

NOT NULL

version

Specifies
                                                					 internal configuration schema version.

Possible
                                                					 values: 3

int

NOT NULL

configImplClass

Represents
                                                					 trigger configuration implementation class.

com.cisco.crs.email.

CiscoEmailControlGroupConfig.

lvarchar(512)

NOT NULL

triggerName

Uniquely
                                                					 identifies a trigger. Available from CRS 4.5 onwards. The API does limit the
                                                					 string length. Go back and revisit the length.

nvarchar(50,0)

NOT NULL

triggerType

Hard
                                                					 coded.

Cisco
                                                         						  Http Trigger

Cisco
                                                         						  JTAPI Trigger

nvarchar(128,0)

NOT NULL

applicationName

Application name being triggered by the trigger.

nvarchar(50,0)

NOT NULL

triggerEnabled

Whether
                                                					 the trigger is enabled

f =
                                                         						  disabled

t =
                                                         						  enabled

boolean

NOT NULL

numOfSessions

Maximum
                                                					 number of sessions

Possible
                                                					 values: 0, 1, 2...

int

NOT NULL

idleTimeout

Idle
                                                					 time out in milliseconds

int

NOT NULL

triggerLocale

Default
                                                					 locale for the trigger.

system.default (the currently configured system default locale)

accept.trigger (the locale provided by the incoming event)

nvarchar(50,0)

NOT
                                                					 NULL

description

Description of the trigger

nvarchar(128,0)

NULL

misc1

For HTTP
                                                					 trigger, this field contains the URL. For JTAPI and call triggers, this is the
                                                					 dialed number (DN).

lvarchar(256)

NULL

misc2

For
                                                					 JTAPI trigger, this is the partition.

lvarchar(256)

NULL

privateData

Internal
                                                					 data not exposed to customers, such as parameters or groups associated with a
                                                					 trigger.

BLOB

NULL

createDateTime

When the
                                                					 trigger was created.

Default
                                                					 value: Current year to second

datetime
                                                					 year to second

Not
                                                					 NULL

active

Whether
                                                					 this record is active.

Possible
                                                					 values:

f =
                                                					 inactive

t =
                                                					 active

boolean

NOT NULL

dateInactive

If
                                                					 active = f, the time when the record became inactive.

datetime
                                                					 year to second

NULL

### DateShiftMap

Database table name : DateShiftMap

This table stores the special business days configured for calendars.

Field Name

Description

Storage

recordid

A unique identifier for the record.

serial

NOT NULL

Primary Key

calid

A unique identifier for the calendar.

int

NOT NULL

name

Name of the calendar.

nvarchar (50)

NOT NULL

caldate

Date of the special day.

DATETIME YEAR TO DAY

NOT NULL

shiftname

The shift name configured for the specific day of the week.

nvarchar (25)

NOT NULL

shifttype

Type of the shift.

smallint

NOT NULL

fromtime

Shift start time.

int

NOT NULL

totime

Shift end time.

int

NOT NULL

active

Indicates whether the record is currently active or not.

f = Inactive

t = Active

boolean

NOT NULL

dateinactive

Date and time of the record when it is marked as inactive.

DATETIME year to second

NULL

### DayShiftMap

Database Table Name : DayShiftMap

This table stores the custom weekly business days configured for calendars.

Field Name

Description

Storage

recordid

A unique identifier for the record.

serial

NOT NULL

Primary Key

calid

A unique identifier for the calendar.

int

NOT NULL

dow

Day of the week.

nvarchar (3)

NOT NULL

shiftname

The shift name configured for the specific day of the week.

nvarchar (25)

NOT NULL

shifttype

Type of the shift.

NOT NULL

smallint

fromtime

Shift start time in 24 hour format.

int

NOT NULL

totime

Shift end time in 24 hour format.

int

NOT NULL

active

Indicates whether the record is currently active or not.

f = Inactive

t = Active

boolean

NOT NULL

dateinactive

Date and time of the record when it is marked as inactive.

DATETIME year to second

NULL

### DialingList

Database table name : DialingList

The DialingList
                                 		  table contains the outbound contacts that need to be dialed for a particular
                                 		  campaign. This table is populated when a text file containing the outbound
                                 		  contacts is imported from the Campaigns configuration page in the Unified CCX
                                 		  Administration.

When the outbound
                                 		  contacts are imported into the database from the Unified CCX Administration,
                                 		  the callStatus field has the default value of 1 (Pending); that is, the
                                 		  contacts are yet to be dialed.

Field Name

Description

Storage

recordid

A unique
                                                					 identifier for the record.

int

NOT NULL

Primary
                                                					 Key

dialinglistid

A unique
                                                					 identifier for a contact.

int

NOT NULL

Primary
                                                					 Key

profileid

Identifier
                                                					 of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary
                                                					 Key

campaignid

Campaign
                                                					 identifier

int

NULL

createdatetime

Default
                                                					 -CURRENT_TIMESTAMP

datetime
                                                					 year to second

NULL

accountnumber

The
                                                					 account number of the contact (from the imported file). This field is sent to
                                                					 the agent desktop.

nvarchar(25, 0)

NULL

firstname

The first
                                                					 name of the contact (from the imported file).

nvarchar(50, 0)

NULL

lastname

The last
                                                					 name of the contact (from the imported file).

nvarchar(50,0)

NULL

phone01

Primary
                                                					 phone number of the contact (from the imported file).

varchar(28,0)

NOT NULL

phone02

Additional number of the contact (from the imported file). The
                                                					 number is dialed when the agent selects Skip-Next for the preview call.

varchar(28,0)

NULL

phone03

Additional number of the contact (from the imported file). This
                                                					 number is dialed if attempts to dial the first two numbers are unsuccessful.

varchar(28,0)

NULL

gmtzonephone01

The time
                                                					 zone for the first phone number of the contact.

smallint

NOT NULL

dstphone01

0 =
                                                					 Daylight Savings Time (DST) is observed at this phone number.

1 = DST
                                                					 is not observed at this phone number

smallint

NOT NULL

gmtzonephone02

The time
                                                					 zone for the second phone number of the contact.

smallint

NOT NULL

dstphone02

0 = DST
                                                					 is observed at this phone number.

1 = DST
                                                					 is not observed at this phone number.

smallint

NOT NULL

gmtzonephone03

The time
                                                					 zone for the third phone number of the contact.

smallint

NOT NULL

dstphone03

0 = DST
                                                					 is observed at this phone number.

1 = DST
                                                					 is not observed at this phone number.

smallint

NOT NULL

callbacknumber

Phone
                                                					 number to be used for callback (can be supplied by the agent).

varchar(28,0)

NULL

callbackdatetime

Customer
                                                					 requested callback time.

datetime
                                                					 year to second

NULL

callstatus

The
                                                					 status of the contact record:

1 =
                                                					 Pending. The call is pending.

2 =
                                                					 Active. The record is sent (active) to the Outbound subsystem for dialing.

3 =
                                                					 Closed. The record is closed.

4 =
                                                					 Callback. The record is marked for a callback.

5 = Max
                                                					 Calls. Maximum attempts have been reached for this record (considered closed).

6 =
                                                					 Retry. The call is redialed immediately whenever there is any miss.

7 =
                                                					 Unknown. If the Outbound subsystem was restarted with records in the Active (2)
                                                					 state, the records are moved to this state.

8 =
                                                					 Retries with delay. The call is redialed as it was either busy, no answer,
                                                					 customer abandoned or system abandoned. Retry time is set as per the
                                                					 corresponding configuration in the Unified CCX Application Administration web
                                                					 interface.

smallint

NOT NULL

callresult

The call
                                                					 result from the last call placed for this record.

1 =
                                                					 Voice. Customer answered and was connected to agent.

2 = Fax.
                                                					 Fax machine reached.

3 =
                                                					 Answering machine. Answering machine reached.

4 =
                                                					 Invalid. Number reported as invalid by the network or by the agent.

5 = Do
                                                					 Not Call. Customer does not want to be called again.

6 =
                                                					 Wrong Number. Number successfully contacted but wrong number.

7 =
                                                					 Wrong Person. Number successfully contacted but reached the wrong person.

8 =
                                                					 Callback. Customer requested regular callback.

9 =
                                                					 Skip/Reject. Agent skipped or rejected a preview call.

10 =
                                                					 Skip-Close/Reject-Close. Agent skipped or rejected a preview call with the
                                                					 close option.

11 =
                                                					 Busy. Busy signal detected or marked busy by agent.

12 =
                                                					 Agent did not respond to the preview call within the timeout duration.

13 =
                                                					 Callback Failed - this value is not written to the database; this is for
                                                					 internal use only.

14 =
                                                					 Callback missed and marked for Retry.

15 =
                                                					 Customer's phone timed out either due to Ring No Answer (RNA) or Gateway
                                                					 failure.

16 =
                                                					 Call was abandoned because IVR port was unavailable or Unified CCX failed to
                                                					 transfer the call to the IVR port.

17 =
                                                					 Call failed due any one of the reasons.

18 =
                                                					 Customer abandoned as customer or agent disconnected the call within the time
                                                					 limit as configured in “Abandoned Call Wait Time” in Unified CCX Application
                                                					 Administration web interface.

smallint

NOT NULL

callresult01

The call
                                                					 result from the last time phone01 was called.

Values
                                                					 are the same as for callResult.

smallint

NULL

callresult02

The call
                                                					 result from the last time phone02 was called.

Values
                                                					 are the same as for callResult.

smallint

NULL

callresult03

The call
                                                					 result from the last time phone03 was called.

Values
                                                					 are the same as for callResult.

smallint

NULL

lastnumberdialed

The last
                                                					 number dialed.

1 =
                                                					 phone01

2 =
                                                					 phone02

3 =
                                                					 phone03

smallint

NULL

callsmadetophone01

The
                                                					 number of call attempts made to phone01. If there is an error in an attempt to
                                                					 call this number, the attempt is not counted here.

smallint

NULL

callsmadetophone02

The
                                                					 number of call attempts made to phone02. If there is an error in an attempt to
                                                					 call this number, the attempt is not counted here.

smallint

NULL

callsmadetophone03

The
                                                					 number of call attempts made to phone03. If there is an error in an attempt to
                                                					 call this number, the attempt is not counted here.

smallint

NULL

retry

Indicates whether the contact has to be retried.

boolean

NULL

active

Contacts
                                                					 becomes inactive for a campaign in the following scenarios:

1 =
                                                					 delete a campaign

2 =
                                                					 delete all the contacts for a campaign

f =
                                                					 Inactive

t =
                                                					 Active

boolean

NOT NULL

dateinactive

The date
                                                					 when record became inactive.

datetime
                                                					 year to second

NULL

numMissedCallback

Number
                                                					 of missed callbacks.

smallint

NULL

### DialingListHistory

Database table name : DialingList

The DialingList
                                 		  table contains the outbound contacts that need to be dialed for a particular
                                 		  campaign. This table is populated when a text file containing the outbound
                                 		  contacts is imported from the Campaigns configuration page in the Unified CCX
                                 		  Administration.

When the outbound
                                 		  contacts are imported into the database from the Unified CCX Administration,
                                 		  the callStatus field has the default value of 1 (Pending); that is, the
                                 		  contacts are yet to be dialed.

Field Name

Description

Storage

recordid

A unique
                                                					 identifier for the record.

int

NOT NULL

Primary
                                                					 Key

dialinglistid

A unique
                                                					 identifier for a contact.

int

NOT NULL

Primary
                                                					 Key

profileid

Identifier
                                                					 of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary
                                                					 Key

campaignid

Campaign
                                                					 identifier

int

NULL

createdatetime

Default
                                                					 -CURRENT_TIMESTAMP

datetime
                                                					 year to second

NULL

accountnumber

The
                                                					 account number of the contact (from the imported file). This field is sent to
                                                					 the agent desktop.

nvarchar(25,0)

NULL

firstname

The first
                                                					 name of the contact (from the imported file).

nvarchar(50,0)

NULL

lastname

The last
                                                					 name of the contact (from the imported file).

nvarchar(50,0)

NULL

phone01

Primary
                                                					 phone number of the contact (from the imported file).

varchar(28,0)

NULL

phone02

Additional number of the contact (from the imported file). The
                                                					 number is dialed when the agent selects Skip-Next for the preview call.

varchar(28,0)

NULL

phone03

Additional number of the contact (from the imported file). This
                                                					 number is dialed if attempts to dial the first two numbers are unsuccessful.

varchar(28,0)

NULL

gmtzonephone01

The time
                                                					 zone for the first phone number of the contact.

smallint

NULL

dstphone01

0 =
                                                					 Daylight Savings Time (DST) is observed at this phone number.

1 = DST
                                                					 is not observed at this phone number

smallint

NULL

gmtzonephone02

The time
                                                					 zone for the second phone number of the contact.

smallint

NULL

dstphone02

0 = DST
                                                					 is observed at this phone number.

1 = DST
                                                					 is not observed at this phone number.

smallint

NULL

gmtzonephone03

The time
                                                					 zone for the third phone number of the contact.

smallint

NULL

dstphone03

0 = DST
                                                					 is observed at this phone number.

1 = DST
                                                					 is not observed at this phone number.

smallint

NULL

callbacknumber

Phone
                                                					 number to be used for callback (can be supplied by the agent).

varchar(28)

NULL

callbackdatetime

Customer
                                                					 requested callback time.

datetime
                                                					 year to second

NULL

callstatus

The
                                                					 status of the contact record:

1 =
                                                					 Pending. The call is pending.

2 =
                                                					 Active. The record is sent (active) to the Outbound subsystem for dialing.

3 =
                                                					 Closed. The record is closed.

4 =
                                                					 Callback. The record is marked for a callback.

5 = Max
                                                					 Calls. Maximum attempts have been reached for this record (considered closed).

6 =
                                                					 Retry. The call is redialed immediately whenever there is any miss.

7 =
                                                					 Unknown. If the Outbound subsystem was restarted with records in the Active (2)
                                                					 state, the records are moved to this state.

8 =
                                                					 Retries with delay. The call is redialed as it was either busy, no answer,
                                                					 customer abandoned or system abandoned. Retry time is set as per the
                                                					 corresponding configuration in the Unified CCX Application Administration web
                                                					 interface.

smallint

NULL

callresult

The call
                                                					 result from the last call placed for this record.

1 =
                                                					 Voice. Customer answered and was connected to agent.

2 = Fax.
                                                					 Fax machine reached.

3 =
                                                					 Answering machine. Answering machine reached.

4 =
                                                					 Invalid. Number reported as invalid by the network or by the agent.

5 = Do
                                                					 Not Call. Customer does not want to be called again.

6 =
                                                					 Wrong Number. Number successfully contacted but wrong number.

7 =
                                                					 Wrong Person. Number successfully contacted but reached the wrong person.

8 =
                                                					 Callback. Customer requested regular callback.

9 =
                                                					 Skip/Reject. Agent skipped or rejected a preview call.

10 =
                                                					 Skip-Close/Reject-Close. Agent skipped or rejected a preview call with the
                                                					 close option.

11 =
                                                					 Busy. Busy signal detected or marked busy by agent.

12 =
                                                					 Agent did not respond to the preview call within the timeout duration.

13 =
                                                					 Callback Failed - this value is not written to the database; this is for
                                                					 internal use only.

14 =
                                                					 Callback missed and marked for Retry.

15 =
                                                					 Customer's phone timed out either due to Ring No Answer (RNA) or Gateway
                                                					 failure.

16 =
                                                					 Call was abandoned because IVR port was unavailable or Unified CCX failed to
                                                					 transfer the call to the IVR port.

17 =
                                                					 Call failed due any one of the reasons.

18 =
                                                					 Customer abandoned as customer or agent disconnected the call within the time
                                                					 limit as configured in “Abandoned Call Wait Time” in Unified CCX Application
                                                					 Administration web interface.

smallint

NULL

callresult01

The call
                                                					 result from the last time phone01 was called.

Values
                                                					 are the same as for callResult.

smallint

NULL

callresult02

The call
                                                					 result from the last time phone02 was called.

Values
                                                					 are the same as for callResult.

smallint

NULL

callresult03

The call
                                                					 result from the last time phone03 was called.

Values
                                                					 are the same as for callResult.

smallint

NULL

lastnumberdialed

The last
                                                					 number dialed.

1 =
                                                					 phone01

2 =
                                                					 phone02

3 =
                                                					 phone03

smallint

NULL

callsmadetophone01

The
                                                					 number of call attempts made to phone01. If there is an error in an attempt to
                                                					 call this number, the attempt is not counted here.

smallint

NULL

callsmadetophone02

The
                                                					 number of call attempts made to phone02. If there is an error in an attempt to
                                                					 call this number, the attempt is not counted here.

smallint

NULL

callsmadetophone03

The
                                                					 number of call attempts made to phone03. If there is an error in an attempt to
                                                					 call this number, the attempt is not counted here.

smallint

NULL

retry

Indicates whether the contact has to be retried.

boolean

NULL

active

Contacts
                                                					 becomes inactive for a campaign in the following scenarios:

1 =
                                                					 delete a campaign

2 =
                                                					 delete all the contacts for a campaign

3 = when
                                                					 callStatus becomes 3 (closed) or 5 (max calls)

f =
                                                					 Inactive

t =
                                                					 Active

boolean

NULL

dateinactive

The date
                                                					 when record became inactive.

datetime
                                                					 year to second

NULL

numMissedCallback

Number
                                                					 of missed callbacks.

smallint

NULL

### MonitoredResourceDetail

Database table name : MonitoredResourceDetail

The MonitoredResourceDetail table records the actual agents who are monitored. The RemoteMonitoringDetail table records the
                                 original agent or the CSQ that the supervisor plans to monitor. Monitoring a CSQ involves monitoring the agents who handle
                                 calls for that CSQ. So the actual agents (which can be more than one) that are monitored will be recorded in the MonitoredResourceDetail
                                 table.

Field Name

Description

Storage

sessionid

Identifier that the system assigned to the call. This identifier remains the same for all legs of the call. It is the sessionID
                                                of the IVR call; that is, when the supervisor starts monitoring, the monitoring call itself is an IVR call. The supervisor
                                                monitors one or more Unified CCX calls.

decimal(18)

NOT NULL

Primary Key

startmonitoringreqtime

The time and date that the remote supervisor attempted to monitor the agent.

datetime year to fraction (3)

NOT NULL

startmonitoringcalltime

The time and date that the supervisor began monitoring the call.

datetime year to fraction (3)

NOT NULL

Primary Key

monitoredrsrcid

Identifier of the resource being monitored.

int

NOT NULL

monitoredsessionseqnum

The session sequence number of the Unified CCX call that is being monitored.

smallint

NOT NULL

profileid

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

gmtoffset

Offset, in minutes, between the local time of the Unified CCX server and Greenwich Mean Time. As the time information is stored
                                                in GMT, this field will always be zero.

int

NOT NULL

nodeid

Unique identifier assigned to each server in the cluster.

smallint

NOT NULL

Primary Key

### MediaCustomerDataMapping

Database table name : MediaCustomerDataMapping

The MediaCustomerDataMapping table contains mapping between the
                                 		  customer data fields for a specific media (such as email and other media types)
                                 		  and the order of fields stored in the TextCustomerDetail table.

Do not edit this table directly. It is for internal use only

Field Name

Description

Storage

recordId

Unique identifier for the record.

int

NOT NULL

Primary Key

mediaType

Type of the media such as email and other media types.

varchar(30,0)

NOT NULL

Primary Key

fieldName

Name of the field in the customer data.

varchar(50,0)

NOT NULL

columnId

Field ID in the TextCustomerDetail where this field is stored.

int

NOT NULL

### ProfileIDMapping

Database table name : ProfileIDMapping

The Unified CCX system creates a new record in the ProfileIDMapping table when a new profile is set up in the Unified CCX
                                 Administration.

A ProfileIDMapping record shows the mapping of the profile name to its unique identifier.

Field Name

Description

Storage

profileName

Name of the profile, as set up in the Unified CCX Administration.

nvarchar(50,0)

NOT NULL

Primary Key

profileID

Identifier of the profile.

int

NOT NULL

### PurgeHistory

Database table name : PurgeHistory

PurgeHistory is
                                 		  mainly to keep track of the history of purge information for both Manual and
                                 		  Scheduled purge.

Field Name

Description

Storage

nodeId

Unique
                                                					 identifier assigned to each server in the cluster.

int

NOT NULL

Primary
                                                					 Key

purgeHistoryId

Sequence
                                                					 numbers.

int

NOT NULL

Primary
                                                					 Key

purgeType

PurgeType
                                                					 MANUAL or SCHEDULED.

nvarchar(10,0)

NOT NULL

purgeState

PurgeState
                                                					 can be any one of, RUNNING, COMPLETED_SUCCESSFULLY, COMPLETED_WITH_ERRORS,
                                                					 UNKNOWN.

nvarchar(30,0)

NOT NULL

purgeStartedDateTime

Purge
                                                					 start time.

datetime
                                                					 year to fraction(3)

NOT NULL

hrDbSizeBeforePurge

Historical
                                                					 db size before purge which will have the value using store procedure getDbSize
                                                					 with column name as "used”.

int

NULL

configDbSizeBeforePurge

Config db
                                                					 size before purge which will have the value using store procedure
                                                					 getDBspaceUsage('db_cra') with column name as "used".

int

NULL

oldestRecDateTimeBeforePurge

Oldest
                                                					 record date and time before purge.

datetime
                                                					 year to fraction(3)

NULL

purgeCompletedDateTime

Purge
                                                					 completion time.

datetime
                                                					 year to fraction(3)

NULL

hrDbSizeAfterPurge

Historical
                                                					 db size after purge which will have the value using store procedure getDbSize
                                                					 with column name as "used".

int

NULL

configDbSizeAfterPurge

Config db
                                                					 size after purge which will have the value using store procedure
                                                					 getDBspaceUsage('db_cra') with column name as "used".

int

NULL

oldestRecDateTimeAfterPurge

Oldest
                                                					 record date time after purge.

datetime
                                                					 year to fraction(3)

NULL

purgetRunTime

Purge
                                                					 run time in minutes which is the difference between purgeCompletedDataTime and
                                                					 purgeStartedDateTime.

int

NULL

### ReasoncodeLabelMap

Database table name : ReasoncodeLabelMap

Unified CCX
                                 		  System maintains a reason code and label for Logout and Not Ready states, that
                                 		  are available in Cisco Finesse Administration.

This table holds
                                 		  the mapping between reason code and label.

Field Name

Description

Storage

code

Reason
                                                					 code, as configured in Finesse Administration.

Smallint

NOT NULL

Primary Key

label

Reason
                                                					 label, as configured in Finesse Administration.

NVARCHAR(40,0)

NOT NULL

category

Type of
                                                					 reason code, label:

NOT_READY

LOGOUT

NVARCHAR(15,0)

NOT NULL

Primary Key

active

Whether
                                                					 the record is active in the system. A record becomes Inactive if reason code
                                                					 label is deleted from Finesse Administration and this field will be marked
                                                					 "FALSE".

boolean

NULL

dateinactive

Date and
                                                					 time this record was added, modified, or deleted from Cisco Finesse
                                                					 Administration.

Date time
                                                					 year to second

NULL

### RemoteMonitoringDetail

Database table name : RemoteMonitoringDetail

The Remote
                                 		  Monitoring Detail Record provides information about sessions where remote
                                 		  monitoring is used.

Field Name

Description

Storage

sessionid

Identifier
                                                					 that the system assigned to the call. This identifier remains the same for all
                                                					 legs of the call. This is the sessionID of the IVR call; that is, the call that
                                                					 the supervisor makes to monitor other Unified CCX calls.

decimal(18)

NOT NULL

Primary
                                                					 Key

startmonitoringreqtime

The time
                                                					 and date that the remote supervisor attempted to monitor the agent.

datetime
                                                					 year to fraction (3)

NOT NULL

Primary
                                                					 Key

remoteloginid

The
                                                					 numeric ID the supervisor enters before starting to monitor a call

varchar(50,0)

NULL

rmonid

Numeric ID
                                                					 of the supervisor who does the monitoring.

int

NOT NULL

endmonitoringtime

The date
                                                					 and time the monitoring ended.

datetime
                                                					 year to fraction (3)

NOT NULL

origmonitoredid

1
                                                         						  (agent), this field contains the extension of the agent being monitored.

2
                                                         						  (CSQ), this field contains the CSQ ID of the CSQ being monitored.

int

NOT NULL

origmonitoredidtype

1 =
                                                         						  agent

2 =
                                                         						  CSQ

smallint

NOT NULL

cause

3 =
                                                         						  Normal (Monitored)

100 =
                                                         						  Normal (Agent RNA)

0 =
                                                         						  Error (Other)

–9 =
                                                         						  Error (Unable to Stop Monitoring)

–8 =
                                                         						  Error (Unable to Monitor New Call)

–7 =
                                                         						  Error (Agent Logged Off)

–6 =
                                                         						  Error (Network Problem)

–5 =
                                                         						  Error (VoIP Server unable to communicate)

–4 =
                                                         						  Error (Monitoring not allowed)

–3 =
                                                         						  Error (Agent not logged in)

–2 =
                                                         						  Error (Invalid input)

–1 =
                                                         						  Error (Other)

smallint

NULL

sessionSeqNum

The
                                                					 sequence number for the IVR call; that is, the call the supervisor makes to
                                                					 monitor other Unified CCX calls.

smallint

NOT NULL

monitoredSessionID

The
                                                					 sessionID of the monitored Unified CCX call.

decimal(18)

NOT NULL

profileID

Identifier of the Unified CCX profile that is associated with
                                                					 this record.

int

NOT NULL

Primary
                                                					 Key

gmtOffset

Offset,
                                                					 in minutes, between the local time of the Unified CCX server and Greenwich Mean
                                                					 Time. As the time information is stored in GMT, this field will always be zero.

int

NULL

nodeID

Unique
                                                					 identifier assigned to each server in the cluster.

smallint

NOT NULL

Primary
                                                					 Key

### Resource

Database table name : Resource

The Unified CCX system creates a new record in the Resource table when the Unified CCX system retrieves agent information
                                 from the Unified CM.

A Resource record contains information about the resource (agent). One such record exists for each active and inactive resource.
                                 When a resource is deleted, the old record is flagged as inactive; when a resource is updated, a new record is created and
                                 the old one is flagged as inactive.

Field Name

Description

Storage

resourceID

Numeric identifier of the resource.

int

NOT NULL

Primary Key

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

resourceLoginID

The login name assigned to the resource in the Unified CM.

nvarchar(50,0)

NOT NULL

resourceName

The first name and the last name of the resource.

nvarchar(50,0)

NOT NULL

resourceGroupID

Resource group to which the resource belongs.

Null if no resource group is assigned to the resource.

int

NULL

resourceType

Type of the resource:

1—Agent

2—Supervisor

3—Administrator

smallint

NOT NULL

active

Whether this record is active:

f —Inactive

t —Active

A record becomes inactive if the resource is deleted or updated.

boolean

NOT NULL

autoAvail

Determines whether the resource goes to Ready State after handling a Unified CCX call:

f —No

t —Yes

boolean

NOT NULL

extension

The Unified CCX extension of the resource.

nvarchar(50,0)

NOT NULL

orderInRG

Order in which the resource resides within the resource group.

Null if no resource group is assigned to the resource.

int

NULL

dateInactive

Date and time that the record became inactive when the active field is "f".

datetime year to fraction(3)

NULL

resourceSkillMapID

Identifier used to locate the associated skill set of the resource in the ResourceSkillMapping table. The ResourceSkillMapping
                                             table can contain multiple records for one resource.

int

NOT NULL

assignedTeamID

Team ID of the resource.

int

NOT NULL

resourceFirstName

First name of the resource.

nvarchar(50,0)

NOT NULL

resourceLastName

Last name of the resource.

nvarchar(50,0)

NOT NULL

resourceAlias

Alias name of the resource.

nvarchar(50,0)

NULL

capabilities

Advanced Supervisor Capabilities for the resource.

smallint

NOT NULL

resourceEmailId

Email ID of the resource.

nvarchar(255)

NULL

AgentConnectionDetail (via resourceID, profileID)

AgentStateDetail (resourceID maps to agentID, via profileID)

ContactCallDetail (resourceID maps originatorID/destinationID when originatorType/destinageType is 1, via profileID)

ContactQueueDetail (resourceID maps to targetID when targetType is 1, via profileID)

MonitoredResourceDetail (resourceID maps to monitoredRsrcID, via profileID)

ProfileIDMapping (via profileID)

RemoteMonitoringDetail (resourceID maps to origMonitoredID when origMonitoredIDType is 1, via profileID)

ResourceGroup (via resourceGroupID, profileID)

ResourceSkillMapping (via resourceSkillMapID, profileID)

Supervisor (via resourceLoginID, profileID)

Team (assignedTeamID maps to teamID, via profileID)

### ResourceGroup

Database table name : ResourceGroup

The Unified CCX system creates a new record in the ResourceGroup table when a resource group is set up in the Unified CCX
                                 Administration.

A ResourceGroup record contains information about the resource group. One such record exists for each active and inactive
                                 resource group.

Field Name

Description

Storage

resourceGroupID

Numeric identifier of the resource group.

int

NOT NULL

Primary Key

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

resourceGroupName

Name of the resource group, as set up in the Unified CCX Administration.

nvarchar(50,0)

NULL

active

Whether the record is active in the Unified CCX system:

f —Inactive

t —Active

A record becomes inactive if the resource group is deleted or updated.

boolean

NOT NULL

dateInactive

If the active field is “f”, date and time that the record became inactive.

datetime year to fraction(3)

NULL

### ResourceSkillMapping

Database table name : ResourceSkillMapping

The Unified CCX system creates a new record in the ResourceSkillMapping table when an agent is associated with a skill in
                                 the Unified CCX Administration.

A ResourceSkillMapping record contains information about all of the skills that are assigned to resources.

Field Name

Description

Storage

resourceSkillMapID

Identifier of the skill set that is associated with a resource.

int

NOT NULL

Primary Key

skillID

Identifier of the skill that is associated with a resource.

int

NOT NULL

Primary Key

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

competenceLevel

Competence level associated with the skill, as set up in the Unified CCX Administration. Values range from 1 (lowest) to 10
                                                (highest).

smallint

NOT NULL

active

Whether the record is active in the Unified CCX system:

f —Inactive

t —Active

A record becomes inactive if the resource group is deleted or updated.

boolean

NOT NULL

### RmonCSQConfig

Database table name : RmonCSQConfig

The Remote
                                 		  Monitoring Contact Service Queue Configuration table contains the CSQs that a
                                 		  remote monitoring supervisor is allowed to monitor (the supervisor’s allowed
                                 		  list). This table is updated when you configure the Unified CCX system through
                                 		  the Unified CCX Administration pages.

Field Name

Description

Storage

rmonID

Numeric
                                                					 identifier of the remote supervisor.

int

NOT NULL

Primary
                                                					 Key

contactServiceQueueID

The
                                                					 numeric identifier of the CSQ, relating to contactServiceQueueID in the
                                                					 ContactServiceQueue table.

int

NOT NULL

Primary
                                                					 Key

profileID

Identifier
                                                					 of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary
                                                					 Key

### RmonResConfig

Database table name : RmonResConfig

The Remote Monitoring Resource Configuration table contains the list of the agents (resources) that a remote monitoring supervisor
                                 is allowed to monitor (the supervisor’s allowed list). This table is updated when you configure the system through the Unified
                                 CCX Administration pages.

Field Name

Description

Storage

rmonID

Numeric identifier of the remote supervisor.

int

NOT NULL

Primary Key

resourceLoginID

The login ID of the resource that the remote supervisor is allowed to monitor.

nvarchar(50,0)

NOT NULL

Primary Key

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

### RmonUser

Database table name : RmonUser

The Remote
                                 		  Monitoring User table provides information about the supervisor who is logged
                                 		  in to remotely monitor agents.

Field Name

Description

Storage

rmonID

Numeric
                                                					 identifier of the remote supervisor.

int

NOT NULL

Primary
                                                					 Key

LoginID

User login
                                                					 name of the remote supervisor.

nvarchar(50,0)

NOT NULL

name

Name of
                                                					 the supervisor.

nvarchar(50,0)

NOT NULL

profileID

Identifier
                                                					 of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary
                                                					 Key

type

The type
                                                					 of supervisor:

0 =
                                                					 regular supervisor

1 = remote
                                                					 monitoring supervisor

int

NOT NULL

active

Determines
                                                					 whether the remote supervisor is active.

f =
                                                					 inactive

t = active

boolean

NOT NULL

dateInactive

Date and
                                                					 time the remote supervisor became inactive.

datetime
                                                					 year to second

NULL

### RtCSQsSummary

Database table name : RtCSQsSummary

The rtcsqssummary
                                 		  table contains real-time statistics about all configured Contact Service Queues
                                 		  in the system. This table gets updated automatically when real-time snapshot
                                 		  data writing for this table is enabled through the Unified CCX Administration
                                 		  pages ( Tools > Real-time snapshot configuration menu
                                 		  option). The updating frequency is based on the configured data writing
                                 		  interval.

Field Name

Description

Storage

csqname

Name of
                                                					 the contact service queue.

nvarchar(50,0)

NOT NULL

Primary
                                                					 Key

loggedinagents

Number
                                                					 agents who are logged in.

int

NULL

availableagents

Number of
                                                					 available (idle) agents.

int

NULL

unavailableagents

Number of
                                                					 unavailable agents.

int

NULL

totalcalls

Total
                                                					 number of calls.

int

NULL

oldestcontact

Oldest
                                                					 contact in the queue.

int

NULL

callshandled

Number of
                                                					 calls handled.

int

NULL

callsabandoned

Number of
                                                					 calls abandoned.

int

NULL

callsdequeued

Number of
                                                					 calls dequeued.

int

NULL

avgtalkduration

Average
                                                					 talk duration.

int

NULL

avgwaitduration

Average
                                                					 wait duration.

int

NULL

longesttalkduration

Longest
                                                					 talk duration.

int

NULL

longestwaitduration

Longest
                                                					 wait duration.

int

NULL

callswaiting

Number
                                                					 of calls waiting.

int

NULL

enddatetime

The date
                                                					 and time that this table data was last updated.

datetime
                                                					 year to second

NULL

workingagents

Number
                                                					 of agents who are in the working state.

int

NULL

talkingagents

Number
                                                					 of agents who are in the talking state.

int

NULL

reservedagents

Number
                                                					 of agents who are in the reserved state.

int

NULL

startdatetime

The date
                                                					 and time that this table’s statistics get collected.

datetime
                                                					 year to second

NULL

convavgtalkduration

Average
                                                					 talk duration in HH:MM:SS format.

varchar(25,0)

NULL

convavgwaitduration

Average
                                                					 wait duration in HH:MM:SS format.

varchar(25,0)

NULL

convlongesttalkduration

Longest
                                                					 talk duration in HH:MM:SS format.

varchar(25,0)

NULL

convlongestwaitduration

Longest
                                                					 wait duration in HH:MM:SS format.

varchar(25,0)

NULL

convoldestcontact

Oldest
                                                					 call in the queue in HH:MM:SS format.

varchar(25,0)

NULL

### RtICDStatistics

Database table name : RtICDStatistics

The
                                 		  RtICDStatistics table contains real-time summary statistics about Unified CCX.
                                 		  This table gets updated automatically when real-time snapshot data writing for
                                 		  this table is enabled through the Unified CCX Administration pages
                                 		  ( Tools > Real-time snapshot configuration menu
                                 		  option). The updating frequency is based on the configured data writing
                                 		  interval.

Field Name

Description

Storage

type

Contact
                                                					 Service Queue type that identifies the contact type it services. It can be
                                                					 either voice or e-mail.

nvarchar(50,0)

NOT NULL

Primary
                                                					 Key

totalcsqs

Number of
                                                					 CSQs configured.

int

NULL

loggedinagents

Number of
                                                					 agents who are logged in.

int

NULL

workingagents

Number of
                                                					 agents who are in the working state.

int

NULL

reservedagents

Number of
                                                					 agents who are in the reserved state.

int

NULL

talkingagents

Number of
                                                					 agents who are in the talking state.

int

NULL

availableagents

Number of
                                                					 available (idle) agents.

int

NULL

unavailableagents

Number of
                                                					 unavailable agents.

int

NULL

totalcalls

Total
                                                					 number of calls.

int

NULL

callswaiting

Number of
                                                					 calls waiting.

int

NULL

callshandled

Number
                                                					 of calls handled.

int

NULL

callsabandoned

Number
                                                					 of calls abandoned.

int

NULL

avgtalkduration

Average
                                                					 talk duration.

int

NULL

avgwaitduration

Average
                                                					 wait duration.

int

NULL

longesttalkduration

Longest
                                                					 talk duration.

int

NULL

longestwaitduration

Longest
                                                					 wait duration.

int

NULL

oldestcontact

Oldest
                                                					 contact in the queue.

int

NULL

startdatetime

Data
                                                					 collection starting time.

datetime
                                                					 year to second

NULL

enddatetime

Date and
                                                					 time this table was last updated.

datetime
                                                					 year to second

NULL

convavgtalkduration

Average
                                                					 talk duration in HH:MM:SS format.

varchar(25,0)

NULL

convavgwaitduration

Average
                                                					 wait duration in HH:MM:SS format.

varchar(25,0)

NULL

convlongesttalkduration

Longest
                                                					 talk duration in HH:MM:SS format.

varchar(25,0)

NULL

convlongestwaitduration

Longest
                                                					 wait duration in HH:MM:SS format.

varchar(25,0)

NULL

convoldestcontact

Oldest
                                                					 call in the queue in HH:MM:SS format.

varchar(25,0)

NULL

### Schedule Reskill

Database table name : schedule_reskill

The Unified CCX system creates a new record in the Schedule Reskill table when an agent is scheduled to be added or removed
                                 from a queue. It also indicates whether the agent was scheduled by a supervisor or administrator.

Field Name

Description

Storage

recordid

Unique identifier of the record.

int

NOT NULL

Primary Key

resourceloginid

The login ID of the resource being rekilled for a CSQ.

nvarchar(50)

NOT NULL

csqid

Unique identifier of the CSQ for which the resource is being reskilled.

int

NOT NULL

operation

Indicates the type of operation to be performed - either addition/removal of a resource for a CSQ.

Scheduled Addition(1)

Scheduled Removal(2)

smallint

NOT NULL

reskiller

Login ID of the resource who has scheduled addition/removal of a resource for a CSQ.

nvarchar(50)

NOT NULL

reskiller_type

Indicates whether supervisor/admin has scheduled addition/removal of a resource for a CSQ.

Supervisor(1)

Administrator(2)

smallint

NOT NULL

scheduletime

Epoch time in seconds, indicating when the resource will be added/removed for a CSQ.

bigint

NOT NULL

active

Indicates whether the record is active or not. When a resource is successfully added/removed for a CSQ, this field is set
                                             to false.

boolean

NOT NULL

dateinactive

Date and time of the record when it is marked as inactive.

datetime year to second

### Schedule Reskill Status

Database table name : schedule_reskill_status

The Unified CCX system stores the results of schedule operation in the Schedule Reskill Status table.

Field Name

Description

Storage

nodeid

Identifier used for conflict resolution in an island mode.

int

NOT NULL

scheduledid

Foreign key to the schedule_reskill table.

int

NOT NULL

timestamp

Schedule execution time.

datetime year to second

NOT NULL

status

0 = Agent is successfully added or removed for the CSQ.

1 = Agent is already part of the CSQ or is removed from the CSQ.

2 = Operation failed due to connectivity issues.

3 = Agent is not available in the Unified CCX system.

4 = CSQ is not available in the Unified CCX system.

5 = Failed to complete the operation due to internal errors.

smallint

NOT NULL

### Skill

Database table name : Skill

The Unified CCX
                                 		  system creates a new record in the Skill table when a skill is set up in the
                                 		  Unified CCX Administration.

A Skill record
                                 		  contains information about a skill. One such record exists for each configured
                                 		  skill.

Field Name

Description

Storage

skillID

Numeric
                                                					 identifier of the skill.

int

NOT NULL

Primary
                                                					 Key

profileID

Identifier
                                                					 of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary
                                                					 Key

skillName

Name of
                                                					 the skill, as set up in the Unified CCX Administration.

nvarchar(50,0)

NOT NULL

active

Determines
                                                					 whether the record is active in the Unified CCX system:

f
                                                					 —Inactive

t —Active

A record
                                                					 becomes inactive if the skill is deleted or updated.

boolean

NOT NULL

dateInactive

If the
                                                					 active field is “f”, date and time that the record became inactive.

datetime
                                                					 year to fraction(3)

NULL

### SkillGroup

Database table name : SkillGroup

The Unified CCX
                                 		  system creates a new record in the SkillGroup table when skills are associated
                                 		  with a CSQ in the Unified CCX Administration.

A SkillGroup
                                 		  record describes each skill that is associated with the CSQ.

Field Name

Description

Storage

skillGroupID

Numeric
                                                					 identifier of the skill group.

int

NOT NULL

Primary
                                                					 Key

skillID

Numeric
                                                					 identifier of the skill.

int

NOT NULL

Primary
                                                					 Key

profileID

Identifier
                                                					 of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary
                                                					 Key

competenceLevel

Minimum
                                                					 acceptable skill level for agents with this skill, as set up in the Unified CCX
                                                					 Administration. Values range from 1 (lowest) to 10 (highest).

smallint

NOT NULL

active

Determines
                                                					 whether the record is active in the CSQ:

f
                                                					 —Inactive

t —Active

A record
                                                					 becomes inactive if the new skill group is deleted or updated.

boolean

NOT NULL

skillWeight

Skills
                                                					 within a CSQ can be assigned weights. This field is used in the weighted skill
                                                					 calculation of the skill-based resource selection algorithm.

Default
                                                					 value is 1.

int

NOT NULL

skillOrder

Skills
                                                					 within a CSQ can be ordered. This field is used in the order skill calculation
                                                					 of the skill-based resource selection algorithm.

Default
                                                					 value is 1.

int

NOT NULL

### Supervisor

Database table name : Supervisor

The Supervisor table contains the information about supervisors.

Field Name

Description

Storage

recordID

Numeric identifier of this supervisor.

int

NOT NULL

Primary Key

resourceLoginID

User ID in the Unified CM configuration.

nvarchar(50,0)

NOT NULL

managedTeamID

Team identifier of the managed team.

int

NOT NULL

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

supervisorType

Type of supervisor for this team

0 = Primary

1 = Secondary

smallint

NOT NULL

active

Indicates whether the record is active in the Unified CCX system. A record becomes inactive if a team is deleted or updated.

f = Inactive

t = Active

boolean

NOT NULL

dateInactive

Date this record was deleted.

datetime year to second

NULL

### SupervisorCampaignMap

Database table name : SupervisorCampaignMap

This table provides the list of campaigns that are managed by Supervisors. A Supervisor can be associated with one or more
                                 campaigns to manage.

Field Name

Description

Storage

recordid

A unique identifier for the record.

int

NOT NULL

Primary Key

profileid

An identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

resourceloginid

The login name assigned to the resource in the Unified CM.

nvarchar(50,0)

NOT NULL

campaignid

A unique identifier for the campaign.

int

NOT NULL

active

Indicates whether the record is active.

boolean

NOT NULL

dateinactive

Date this record is deleted.

datetime year to second

NULL

### SupervisorApplicationMap

Database table name : SupervisorApplicationMap

This table provides the list of applications that are managed by Supervisors. A Supervisor can be associated with one or more
                                 applications to manage.

Field Name

Description

Storage

recordid

A unique identifier for the record.

int

NOT NULL

Primary Key

profileid

An identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

resourceloginid

The login name assigned to the resource in the Unified CM.

nvarchar(50,0)

NOT NULL

applicationid

A unique identifier for the application.

int

NOT NULL

active

Indicates whether the record is active.

boolean

NOT NULL

dateinactive

Date this record is deleted.

datetime year to second

NULL

### Team

Database table name : Team

The Team table contains information about specific teams.

Field Name

Description

Storage

teamID

Numeric identifier for this team.

int

NOT NULL

Primary Key

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

teamName

Name of this team.

nvarchar(50,0)

NOT NULL

active

Indicates whether the record is active in the Unified CCX system. A record becomes inactive if a team is deleted or updated.

f = Inactive

t = Active

boolean

NOT NULL

dateInactive

Date this record was deleted.

datetime year to fraction(3)

NULL

### TeamCSQMapping

Database table name : TeamCSQMapping

The TeamCSQMapping table shows the relationship between Teams and CSQs; for example, Team 1 is CSQ3, Team 4 is CSQ10.

Field Name

Description

Storage

recordID

Numeric identifier for this record.

int

NOT NULL

Primary Key

csqID

Numeric identifier for the CSQ.

int

NOT NULL

teamID

Numeric identifier for the team.

int

NOT NULL

profileID

Identifier of the Unified CCX profile that is associated with this record.

int

NOT NULL

Primary Key

active

Indicates whether the record is active in the Unified CCX system. A record becomes inactive if a team is deleted or updated.

f = Inactive

t = Active

boolean

NOT NULL

dateInactive

Date this record was deleted.

datetime year to second

NULL

ContactServiceQueue (csqID maps to contactServiceQueueID, and via profileID)

ProfileIDMapping (via ProfileID)

Team (via teamID and profileID)

### TextAgentConnectionDetail

Database table name : TextAgentConnectionDetail

The Unified CCX system creates a new record in the TextAgentConnectionDetail table when an agent receives an email or chat.

Field Name

Description

Storage

ContactID

Alphanumeric identifier for the contact.

varchar (64,0)

NOT NULL

Primary Key

ContactSeqNum

Contact sequence number that the system assigned to the contact or the leg. Each leg of a contact is assigned a new contact
                                             sequence number.

To be used later.

smallint

NOT NULL

Primary Key

nodeID

Numeric identifier for the node.

smallint

NOT NULL

resourceID

Numeric identifier for the resource.

int

NOT NULL

Primary Key

startDateTime

Date and time that the contact or leg entered the system.

datetime year to fraction (3)

NOT NULL

Primary Key

endDateTime

Date and time that the contact or the leg was transferred or disconnected.

datetime year to fraction (3)

NOT NULL

qIndex

A new qIndex is created whenever a Unified CCX contact is conferenced to a Unified CCX route point.

To be used later.

smallint

NOT NULL

acceptTime

Amount of time, in seconds, that passed from the time a contact or leg was presented to an agent and the agent answered the
                                             contact.

smallint

NULL

talkTime

Amount of time, in seconds, that passed from the time an agent answered the contact or the leg to the time the contact or
                                             the leg was disconnected or transferred, not including hold time.

smallint

NULL

workTime

Amount of time, in seconds, that an agent spent in Work State after the contact or the leg.

To be used later.

smallint

NULL

WrapupData

The contact information that the agent enters after the contact is handled through the Agent Desktop user interface.

varchar(40,0)

NULL

contactdisposition

Disposition of the contact.

smallint

NOT NULL

Default: 0

loginsessionid

Unique identifier of an agent login session. This identifier remains the same until the session ends.

varchar(18)

mediasessionid

Indicates the media session identifier assigned while assigning the contact. It can be 1 to 5 for ‘Chat’ media and 26 to 30
                                             for ‘Email’ media, depending on the maximum sessions configured by the administrator in ‘Channel Parameter’ configuration
                                             page of AppAdmin.

smallint

csqrecordid

Numeric identifier of the CSQ in which the agent received an email or chat contact.

int

### TextAgentStateDetails

Database table name : TextAgentStateDetail

The Unified CCX system creates a new record in the TextAgentStateDetail table each time the state of the agent changes while
                                 the agent is handling chat and email. The TextAgentStateDetail record contains information about the agent and about the event
                                 that caused the agent state to change.

Field Name

Description

Storage

agentID

Identifier of the agent whose state has changed.

int

NOT NULL

Primary Key

stateChangeDatetime

Date and time that the chat agent state changed.

datetime year to fraction (3)

NOT NULL

Primary Key

agentStateID

Event that triggered the chat agent state change:

0—Logon

1—Log off

2—Not available

3—Available

4—Busy

5—Unknown

6—Partial busy

7—Reserved

smallint

NOT NULL

Primary Key

reasonCode

Code, as written to the database, for the reason that the chat agent changed to Not Ready state or to Log Out state.

32750—Non chat agent

32755—Contact ended

32757—Media handler failure

32760—Login

32763—Contact not accepted

32764—CCX failure

32765—Connection down

smallint

NOT NULL

Primary Key

routingType

Routing type of the contact or leg:

1—Interactive

2—Non Interactive

smallint

NOT NULL

Primary Key

loginsessionid

Unique identifier of an agent login session. This identifier remains the same until the session ends.

varchar(18)

contactid

Alphanumeric identifier for the contact.

This field will have an identifier only if the agent state changes due to allocating or handling a contact. Else, it will
                                             be NULL.

varchar(64)

### TextAgentWrapupDetail

Database table name : TextAgentWrapupDetail

The Unified CCX
                                 		  system creates a new record in the TextAgentWrapupDetail table each time the
                                 		  agent enters a Wrap-Up detail.

Field Name

Description

Storage

ContactID

Alphanumeric identifier for the contact.

varchar
                                                					 (64,0)

NOT NULL

Primary
                                                					 Key

resourceID

Numeric
                                                					 identifier for the resource.

int

NOT NULL

Primary
                                                					 Key

reasonID

Numeric
                                                					 identifier for the reason.

int

NOT NULL

wrapupTime

Date and
                                                					 time that the Wrap-Up is applied.

datetime
                                                					 year to fraction (3)

NOT NULL

Primary
                                                					 Key

MediaType

Type of
                                                					 the media such as email and other media types.

1—Chat

3—Email

smallint

NULL

### TextContactDetail

Database table name : TextContactDetail

The Unified CCX
                                 		  system creates a new record in the TextContactDetail table for each chat and
                                 		  email contact or leg processed by the system. A new contact or leg starts each
                                 		  time a contact is transferred or redirected.

A
                                 		  TextContactDetail record contains detailed information about the contact or
                                 		  leg. At least one such record will exist for each contact or leg.

Field Name

Description

Storage

ContactID

Alphanumeric identifier for this record.

varchar (64,0)

NOT NULL

Primary Key

ContactSeqNum

Contact sequence number that the system assigned to the contact or the leg. Each leg of a contact is assigned a new contact
                                             sequence number.

To be used later.

smallint

NOT NULL

Primary Key

nodeID

Numeric identifier for the node.

smallint

NOT NULL

contactType

Type of contact or leg:

1—Incoming. Outside contact received by the Unified CCX system.

smallint

NOT NULL

mediaType

Type of the media such as email and other media types.

1—Chat

3—Email

smallint

NOT NULL

contactDisposition

Disposition of the contact or the leg.

1—Abandoned

2—Handled

3—Do not care

4—Aborted 8

5—Rejected

6—Cleared

7—Unknown

smallint

NOT NULL

dispositionReason

Reason why the contact is aborted or rejected by the system.

Unknown

Chat_agent_ended

Chat_customer_ended

Chat_agent_aborted

Chat_agent_abandoned

Chat_customer_abandoned

Chat_abandoned_timeout

Chat_customer_abandoned

Chat _customer_waited

Chat_system_failure

Chat_system_failure_before_agent_joined

Chat_agent_connection_failure

Chat_agent_end_before_in _chatroom

varchar(100,0)

NULL

originatorType

Originator of the contact or the leg:

1—Agent. Contact originated by an agent.

2—Unknown. Contact originated from outside.

smallint

NOT NULL

originator

Numeric identifier of the agent who originated the contact or the leg.

Used only if originatorType is 1.

nvarchar(50,0)

int

NULL

destinationType

Destination of the contact or the leg:

1—Agent. Contact presented to an agent.

Null if no destination.

smallint

NOT NULL

destination

Numeric identifier of the agent who received the contact or the leg.

Used only if destinationType is 1.

nvarchar(50,0)

int

NULL

startDateTime

Date and the time that the contact or the leg is presented to the agent.

datetime year to fraction (3)

NOT NULL

endDateTime

Date and time that the contact or the leg is transferred or disconnected.

datetime year to fraction (3)

NOT NULL

tagID

The string with which the contact or the leg is tagged.

nvarchar(50,0)

NULL

source

Source from which the contact originated.

1—Bubble Chat

2—Fb Messenger

-1—Others

smallint

### TextContactQueueDetail

Database table name : TextContactQueueDetail

Contact or leg
                                          				is abandoned while queued for chat and email CSQs

Contact or leg
                                          				is being dequeued

Contact or leg
                                          				is connected to an agent

Field Name

Description

Storage

ContactID

Alphanumeric identifier for the contact.

varchar
                                                					 (64,0)

NOT NULL

Primary
                                                					 Key

ContactSeqNum

Contact
                                                					 sequence number that the system assigned to the contact or the leg. Each leg of
                                                					 a call is assigned a new contact sequence number.

To be used
                                                					 later.

smallint

NOT NULL

Primary
                                                					 Key

nodeID

Numeric
                                                					 identifier for the node.

smallint

NOT NULL

csqRecordID

Numeric
                                                					 identifier for the chat and email CSQ.

int

NOT NULL

Primary
                                                					 Key

qIndex

A new
                                                					 qIndex is created whenever a Unified CCX contact is conferenced to a Unified
                                                					 CCX route point.

To be used
                                                					 later.

smallint

NOT NULL

Primary
                                                					 Key

disposition

Abandoned = 1 9

Handled by CSQ = 2

Dequeued from CSQ = 3

Handled by another CSQ = 4

smallint

NULL

metServiceLevel

Yes =
                                                         						  t

No = f

To be
                                                					 used later.

boolean

NULL

queueTime

Number
                                                					 of seconds the contact spent in queue for this CSQ and this leg of the contact.

int

NULL

### TextCustomerDetails

Database table name : TextCustomerDetail

The Unified CCX system creates a new record in the TextCustomerDetails
                                 		  table when a chat
                                 		  and email agent receives the contact.

The TextCustomerDetail table captures customer related information
                                 		  corresponding to the chat
                                 		  and email contact. Maximum 10 customer fields can be
                                 		  persisted in the table. The chat
                                 		  and email customer is advised to limit each field value as
                                 		  per the details mentioned in the below table so that the data truncation will
                                 		  not happen while storing the customer data into the database. Customer can
                                 		  write custom reports on top of this historical reporting table and use the
                                 		  persisted data.

Field Name

Description

Storage

ContactID

Alphanumeric identifier for this record.

nvarchar (64,0)

NOT NULL

Primary Key

FieldID1 to FieldID10

The unique field IDs corresponding to the field names in the
                                                					 non-voice contact or MediaCustomerDataMapping
                                                					 table.

In actual table schema there are 10 individual columns named
                                                					 FieldID1 through FieldID10.

int

NOT NULL

FieldValue1 to FieldValue5

FieldValue9 to FieldValue10

Indicates the field values provided for the corresponding
                                                					 field names in
                                                					 the non-voice contact or MediaCustomerDataMapping table.

In actual table schema there are 10 individual columns named
                                                					 FieldValue1 through FieldValue10.

lvarchar (600)

NOT NULL

FieldValue6 to FieldValue8

Indicates the field values provided for the corresponding
                                                					 field names in the non-voice contact or MediaCustomerDataMapping table.

In case of email contact the field values 6 to 8 are used for
                                                					 the Agent added email addresses in the CC, BCC and To fields respectively.

lvarchar (5080)

NULL

InsertionDate

Indicates the date and time of insertion.

datetime year to fraction(3)

NOT NULL

### TextRatingDetail

Database table name : TextRatingDetail

The Unified CCX system creates a new record in the TextRatingDetail table each time the customer rates a chat experience.

Field Name

Description

Storage

ContactID

Alphanumeric identifier for this record.

varchar (64)

NOT NULL

Primary Key

Rating

The rating given by the customer.

smallint

NOT NULL

RatingTime

Date and time the customer assigned the rating.

datetime year to fraction (3)

NOT NULL

### WorkflowTask

Database table name : WorkflowTask

A WorkflowTask
                                 		  record contains information about a task or a subtask that runs on the Unified
                                 		  CCX system.

Field Name

Description

Storage

taskID

Identifier
                                                					 of the task.

decimal(18,0)

NOT NULL

Primary
                                                					 Key

parentTaskID

Identifier
                                                					 of the parent task, if the task is a subtask.

decimal(18,0)

NULL

startDateTime

Date and
                                                					 the time that the task started executing.

datetime
                                                					 year to second

NULL

endDateTime

Date and
                                                					 the time that the task completed executing.

datetime
                                                					 year to second

NULL

applicationServerID

Unique
                                                					 identifier assigned to each Unified CCX server in the cluster.

smallint

NOT NULL

Primary
                                                					 Key

### WrapupCategory

Database table name : WrapupCategory

Wrap-Up reason
                                 		  category information is stored in this table. A Wrap-Up Reason is associated
                                 		  with one or more CSQs. This mapping of Wrap-Up Reasons and CSQs is stored
                                 		  separately in wrapupCsqMap table.

Field Name

Description

Storage

categoryid

A unique identifier for the Wrap-Up category.

int

NOT NULL

Primary Key

profileid

Identifier
                                                					 of the Unified CCX profile that is associated with this record.

int

NOT
                                                					 NULL

Primary
                                                					 Key

recordid

A unique identifier for the record.

int

NOT NULL

Primary Key

name

The name
                                                					 of the Wrap-Up category.

nvarchar(160,0)

NOT
                                                					 NULL

type

The type
                                                					 of interaction for which the Wrap-Up reason is applied. For example, Non-Voice.

lvarchar(40)

NOT
                                                					 NULL

global

Indicates
                                                					 whether the Wrap-Up category is tagged at global or CSQ level.

boolean

NOT
                                                					 NULL

active

Indicates
                                                					 whether the record is currently active.

boolean

NOT
                                                					 NULL

dateinactive

The date
                                                					 and time when the record became inactive.

datetime
                                                					 year to second

NULL

createdatetime

The date and time that the record is created.

Default value: Current year to second.

bigint

NULL

### WrapupReasons

Database table name : WrapupReasons

This table stores
                                 		  the details about the Wrap-Up reasons that are configured by the administrator.

Field Name

Description

Storage

reasonid

A unique identifier for the Wrap-Up reason.

int

NOT NULL

Primary Key

categoryid

A unique
                                                					 identifier for the Wrap-Up category.

int

NOT
                                                					 NULL

reason

The name of the Wrap-Up reason.

nvarchar(160,0)

NOT NULL

active

Indicates whether the record is currently active.

boolean

NOT NULL

dateinactive

The date and time when the record became inactive.

datetime year to second

NULL

createdatetime

The date
                                                					 and time that the record is created.

Default
                                                					 value: Current year to second.

bigint

NULL

### WrapupCsqMap

Database table name : WrapupCsqMap

The mapping of
                                 		  Wrap-Up Reasons and CSQs is stored in this table.

Field Name

Description

Storage

recordid

A unique
                                                					 identifier for the record.

int

NOT NULL

Primary
                                                					 Key

categoryid

A unique
                                                					 identifier for the Wrap-up Category.

int

NOT
                                                					 NULL

csqid

A unique
                                                					 identifier for the CSQ from the ContactServiceQueue table.

int

NOT
                                                					 NULL

active

Indicates
                                                					 whether the record is currently active.

boolean

NOT
                                                					 NULL

dateinactive

The date and time when the record became inactive.

datetime year to second

NULL

createdatetime

The date
                                                					 and time that the record is created.

Default
                                                					 value: Current year to second.

bigint

NULL

| Note | SQL is
                                    		  case-insensitive and the queries written against the database can be in any
                                    		  case. However, you might have to change the case for the column names depending
                                    		  on the third-party tool that you use for querying the database. Refer to the
                                    		  documentation for these third-party tools for more information. |
|---|---|

| Note | For storage characteristics and limitations of the data
                                                         						  types used for the fields in the databases refer to "IBM Informix SQL Reference
                                                         						  Guide". The date and time in the database fields are stored in Coordinated
                                                         						  Universal Time (UTC). |
|---|---|

| Note | If the NULL value is valid, the database will record a
                                                         						  value of -1 for a numeric field and an empty string for other fields. |
|---|---|

| Field Name | Description | Storage |
|---|---|---|
| sessionID | Identifier that the system assigns to the call. This identifier remains the same for all legs of the call. | decimal(18, 0) NOT NULL Primary Key |
| sessionSeqNum | Session sequence number that the system assigned to the call or the leg. Each leg of a call is assigned a new sequence number. | smallint NOT NULL Primary Key |
| nodeID | Unique identifier assigned to each Unified CCX server in the cluster. | smallint NOT NULL Primary Key |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| resourceID | Identifier of the agent who handled the call. | int NOT NULL Primary Key |
| startDateTime | Date and time that the call or the leg started ringing at the device of an agent. | datetime year to fraction (3) NOT NULL Primary Key |
| endDateTime | Date and time that the call or the leg was transferred or disconnected. | datetime year to fraction (3) NOT NULL |
| qIndex | For all the new calls that are coming to an agent’s extension through a route point, the value of qIndex is 1. Thereafter,
                                             the value of qIndex is incremented by 1, whenever there is a conference through the route point. Note The value of qIndex of an agent is 0, whenever an agent receives a call to the extension directly (by conference and transfer
                                                         legs) instead of a route point. This is applicable only for the AgentConnectionDetail table. | Note | The value of qIndex of an agent is 0, whenever an agent receives a call to the extension directly (by conference and transfer
                                                         legs) instead of a route point. This is applicable only for the AgentConnectionDetail table. | smallint NOT NULL Primary Key |
| Note | The value of qIndex of an agent is 0, whenever an agent receives a call to the extension directly (by conference and transfer
                                                         legs) instead of a route point. This is applicable only for the AgentConnectionDetail table. |
| gmtOffset | Offset, in minutes, between the local time of the Unified CCX server and Greenwich Mean Time. As the time information is stored
                                             in GMT, this field will always be zero. | smallint NOT NULL |
| ringTime | Amount of time, in seconds, between the time the call or the leg first rang at the extension of an agent and one of the following
                                             events: The agent answered the call or the leg The caller hung up before the call or the leg was answered The system retrieved the call or the leg before the call or the leg was answered | smallint NULL |
| talkTime | Amount of time, in seconds, that passed from the time an agent answered the call or the leg to the time the call or the leg
                                             was disconnected or transferred, not including hold time. | int NULL |
| holdTime | Amount of time, in seconds, that the call or the leg spent on hold. | smallint NULL |
| workTime | Amount of time, in seconds, that an agent spent in Work State after the call or the leg. | smallint NULL |
| callWrapupData | After-call information that the agent enters through the Agent Desktop user interface while the agent is in the work state. | varchar(40) NULL |
| callResult | Outcome of the outbound dialer call. 1 = Voice (Customer answered and was connected to agent) 2 = Fax/Modem (Fax machine detected) 3 = Answering Machine (answering machine detected) 4 = Invalid (Number reported as invalid by the network) 5 = Do Not Call (customer does not want to be called again) 6 = Wrong Number (number successfully contacted but wrong number) 7 = Customer Not Home (number successfully contacted but reached the wrong person) 8 = Callback (customer requested regular callback) 9 = Agent Rejected (Agent has skipped or rejected a preview call) 10 = Agent Closed (Agent has skipped or rejected a preview call with the close option) 11 = Busy (busy signal detected) 12 = RNA (the agent lets the call go ring-no-answer) 20 = OB_XFER is default (the agent transfers or conferences the outbound call to another agent. | smallint NULL |
| dialinglistid | Unique identifier of a contact that is dialed for an outbound campaign. Links with DialingList.dialingListID | int NULL |
| rna | Specifies if the call or the leg hasn’t been answered by an agent within the configured ring time. This equates to ’t’ if
                                             the call hasn’t been answered. | Boolean |
| loginsessionid | Unique identifier of an agent login session. This identifier remains the same until the session ends. | varchar(18) |
| contactid | Unique identifier for all records related to a single call across various tables in Unified CCX. | varchar(40) |
| csqrecordid | Numeric identifier of CSQ for CSQ-based calls, else -1 is stored. | int |
| consultsessionid | This field is NOT NULL for conferenced or transferred agents through consult call. The value will be the sessionID of the
                                             consult call. | decimal (18, 0) |

| Note | The value of qIndex of an agent is 0, whenever an agent receives a call to the extension directly (by conference and transfer
                                                         legs) instead of a route point. This is applicable only for the AgentConnectionDetail table. |
|---|---|

| Field Name | Description | Storage |
|---|---|---|
| agentID | Identifier of the agent whose state has changed. | int NOT NULL Primary Key |
| eventDateTime | Date and time that the agent state changed. | datetime year to fraction (3) NOT NULL Primary Key |
| gmtOffset | Offset, in minutes, between the local time of the Unified CCX server and Greenwich Mean Time. As the time information is stored
                                             in GMT, this field will always be zero. | smallint NOT NULL |
| eventType | Event that triggered the agent state change: 1—Log In 2—Not Ready 3—Ready 4—Reserved 5—Talking 6—Work 7—Log Out | smallint NOT NULL Primary Key |
| reasonCode | Code, as set up in the Cisco Desktop Administrator, for the reason that the agent changed to Not Ready State or to Log Out
                                             State. Null if a reason code is not configured. | smallint NOT NULL Primary Key |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| loginsessionid | Unique identifier of an agent login session. This identifier remains the same until the session ends. | varchar(18) |
| contactid | Unique identifier for all records related to a single call across various tables in Unified CCX. | varchar(40) |

| Field Name | Description | Storage |
|---|---|---|
| contactid | Alphanumeric identifier for the contact. | int NOT NULL Primary Key |
| sessionseqnum | Session sequence number that the system assigned to the call or the leg. Each leg of a call is assigned a new sequence number. | smallint NOT NULL Primary Key |
| agentID | Identifier of the agent whose ACD call details are stored. | int NOT NULL Primary Key |
| calltype | Identifier of the type of all incoming and outgoing calls of agents' ACD line extension. | int NOT NULL |
| startdatetime | Start date and time of the agent call details that are to be stored. | BIG INT NOT NULL Primary Key |
| phonenumber | Identifier of the phone number of the calls that were handled by the agent. | varchar (30) NOT NULL |
| disposition | Identifier of the contact disposition. | int NULL |
| wrapupdata | Information that the agents enter in the desktop user interface after a call, while the agents are still in the work state. | lvarchar (804) NULL |
| csqname | Identifier of the CSQ name that the agent was assigned to. | nvarchar (50) NULL |
| enddatetime | End date and time of the agent call details that are to be stored. | BIG INT NOT NULL |

| Field Name | Description | Storage |
|---|---|---|
| agentID | Identifier of the agent whose state has changed. | int NOT NULL Primary Key |
| eventDateTime | Date and time that the agent state changed. | BIG INT NOT NULL Primary Key |
| eventType | Event that triggered the agent state change: 1—Log In 2—Not Ready 3—Ready 4—Reserved 5—Talking 6—Work 7—Log Out | smallint NOT NULL Primary Key |
| reasonCode | Code, as set up in the Cisco Desktop Administrator, for the reason that the agent changed to Not Ready State or to Log Out
                                             State. Null if a reason code is not configured. | smallint NOT NULL Primary Key |
| wrapupData | After-call information that the agent enters through the Agent Desktop user interface while the agent is in the work state. | lvarchar (804) NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | Unique identifier of the record. | int NOT NULL Primary Key |
| profileid | Profile ID of the node. | int NOT NULL Primary Key |
| applicationname | Name of the application. | nvarchar (50) NOT NULL |
| promptid | Unique identifier for the prompt file or folder assigned to the application. This is retrieved from assignedprompts table. | int NOT NULL |
| active | Indicates whether the record is active or not. By default, it is True . It is marked as False when either the application or the assigned prompt (file or folder) is deleted. | boolean |
| dateinactive | Date and Time at which, the record is marked as inactive. Default value: NULL | date time year to second |

| Field Name | Description | Storage |
|---|---|---|
| profileid | Identifier
                                                					 of the profile. | int NOT NULL Primary
                                                					 Key |
| createdatetime | Default
                                                					 -CURRENT_TIMESTAMP | datetime
                                                					 year to second NOT NULL |
| recordid | Unique
                                                					 identifier for the record | int NOT NULL Primary
                                                					 Key |
| areacode | The area
                                                					 code of the call. | nvarchar(10) NOT NULL Primary
                                                					 Key |
| regioncode | Uses the
                                                					 same data as that of gmtzone. | nvarchar(10) NULL |
| daylightsavingsenabled | Indicates
                                                					 whether daylight savings time is observed. N =
                                                         						  Daylight savings time is not observed. Y =
                                                         						  Daylight savings time is observed. | char(1) NOT NULL |
| gmtzone | Stores
                                                					 identifiers that internally maps to the GMT offset corresponding to the area
                                                					 code. | int NULL |
| privatedata | Any fields
                                                					 which are to be used internally only. | BLOB NULL |
| active | Whether
                                                					 the record is active in the system. A record becomes inactive if the team is
                                                					 deleted from the system. f =
                                                					 Inactive t = Active | boolean NOT NULL |
| dateinactive | Date
                                                					 this record was deleted. | datetime
                                                					 year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | Unique identifier of the record. | int NOT NULL Primary Key |
| profileid | Profile ID of the node. | int NOT NULL Primary Key |
| promptid | Unique identifier for the prompt file or folder assigned to the application. | int NOT NULL |
| type | To identify if the selection is a prompt file or folder. 0 = File 1 = Folder Default value: 0 | small int NOT NULL |
| parentfolderid | The ID of parent folder of this prompt, which is stored in the assignedFolder table. | int NOT NULL |
| name | Name of the prompt file or folder. | lvarchar (255) NOT NULL |
| active | Indicates whether the record is active in the Unified CCX system. A record becomes inactive if a prompt file or folder is
                                             renamed or deleted ( name ). f = Inactive t - Active | boolean |
| dateinactive | Date and Time at which, the record is marked as inactive. Default value: NULL | date time year to second |

| Field Name | Description | Storage |
|---|---|---|
| recordid | Unique identifier for the record. Default value = 0 | int NOT NULL Primary Key |
| resourceloginid | The resource login ID. | nvarchar(50) NOT NULL |
| skillid | Numeric identifier of the skill that was not removed from the audit_skillgroup table. | int NOT NULL |
| fromcompetency | Agent’s existing skill level that was not removed from the audit_skillgroup table. | int NOT NULL |
| tocompetency | Agent’s modified skill level that was not removed from the audit_skillgroup table. | int NOT NULL |
| operation | The type of operation performed on the skill that was not removed from the audit_skillgroup table. | smallint NOT NULL |
| residualparentid | Record ID of the audit_reskill table, which is the parent of the residual entity. Default value = 0 | int NOT NULL |
| active | Indicates if the record is active or not. Default value = f, which indicates that the record is inactive. The record is inactive when you remove the residual skill
                                             or modify the competency. t = Indicates that the record is active. The record is active when the residual skill exists in the resource. | boolean NOT NULL |
| dateinactive | Date and Time at which, the record is made inactive. | datetime year to second |

| Note | The values in the skillid, fromcompetency, tocompetency, and operation fields are the same as that of the corresponding record
                                             in the audit_skillgroup table. |
|---|---|

| Field
                                             					 Name | Description | Storage |
|---|---|---|
| recordID | Numeric
                                             					 identifier of the record. | int NOT NULL Primary
                                             					 Key |
| profileID | Identifier of the Unified CCX profile that is associated with
                                             					 this record. | int NOT NULL Primary
                                             					 Key |
| resourceLoginID | User ID
                                             					 in the Unified CM configuration. | nvarchar(50,0) NOT NULL |
| csqID | Numeric
                                             					 identifier for the CSQ. | int NOT NULL |
| operation | The type
                                             					 of operation performed on the resource or CSQ: Resource_Modified(1) Csq_Modified(2) Csq_Added(3) Csq_Deleted(4) Skill_Deleted(5) | smallint NOT NULL |
| result | The
                                             					 resultant action because of type of operation performed on the resource: Added_to_csq(1) Removed_from_csq(2) | smallint NOT NULL |
| skillgrouprecordid | The
                                             					 record ID corresponding to the skill group from the audit_skillgroup table for
                                             					 a CSQ. | int NOT NULL |
| reskiller | Login ID
                                             					 of the user. | nvarchar(100,0) NOT NULL |
| reskiller_type | Resource
                                             					 is reskilled by: Supervisor(1) Admin(2) System(3) Note If
                                                      					 the resource is reskilled by the Auto-Removal option, the reskiller_type is
                                                      					 System. | Note | If
                                                      					 the resource is reskilled by the Auto-Removal option, the reskiller_type is
                                                      					 System. | smallint NOT NULL |
| Note | If
                                                      					 the resource is reskilled by the Auto-Removal option, the reskiller_type is
                                                      					 System. |
| reskilledtimestamp | Date and
                                             					 Time this record was changed. | datetime
                                             					 year to fraction(3) NOT NULL |
| active | Indicates whether the record is active based on the values in
                                             					 the "result" field in the audit_reskill table. True=The record is active when a resource is added to a CSQ and
                                                   						  the value of the "result" field is "Added_to_csq". False =The record is inactive when the resource is removed from
                                                   						  the CSQ and the value of the "result" field is "Removed_from_csq". If an active
                                                   						  record exists for the same resource and the same CSQ, then this record is alo
                                                   						  marked inactive. | boolean NOT NULL |

| Note | If
                                                      					 the resource is reskilled by the Auto-Removal option, the reskiller_type is
                                                      					 System. |
|---|---|

| Field Name | Description | Storage |
|---|---|---|
| recordID | Numeric identifier of the record. | int NOT NULL Primary Key |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| skillID | Numeric identifier of the skill. | int NOT NULL Primary Key |
| fromcompetency | Existing skill level of the agents. Values range from 1 (lowest) to 10 (highest). | int NOT NULL |
| tocompetency | Modified skill level of the agents. Values range from 1 (lowest) to 10 (highest). | int NOT NULL |
| operation | The type of operation performed on the skill: Skill Add(1) Skill Removed(2) Competency Increased(3) Competency Decreased(4) | smallint NOT NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | Unique identifier of the record. | serial NOT NULL Primary Key |
| calendarid | A unique identifier for the calendar. | int NOT NULL |
| entity | Application name or the chat widget ID associated with the calendar. | nvarchar(50) NOT NULL |
| entitytype | Indicates whether the calendar is associated with an application or a chat widget. | smallint NOT NULL |
| active | Indicates wheather the record is deleted. | boolean NOT NULL |
| dateinactive | Date and time when the record was deleted. | datetime year to second |

| Field Name | Description | Storage |
|---|---|---|
| recordid | A unique
                                                					 identifier for the record. | int NOT NULL Primary
                                                					 Key |
| campaignid | A unique
                                                					 identifier for the campaign. | int NOT NULL Primary
                                                					 Key |
| profileid | Identifier
                                                					 of the Unified CCX profile that is associated with this record. | int NOT NULL Primary
                                                					 Key |
| createdatetime | Default
                                                					 -CURRENT_TIMESTAMP | datetime
                                                					 year to second NOT NULL |
| campaignname | Name of
                                                					 the campaign. Must be unique. | nvarchar(10) NULL |
| enabled | 0 =
                                                      						  campaign is enabled 1 =
                                                      						  campaign is disabled | smallint NOT NULL |
| description | A
                                                					 description of the campaign. | varchar(50) NULL |
| starttime | When the
                                                					 campaign starts (based on server time). This is stored in minutes. | int NOT NULL |
| endtime | When the
                                                					 campaign ends (based on server time). This is stored in minutes. | int NOT NULL |
| cachesize | Number
                                                					 of contacts to be retrieved in a batch for dialing for this campaign. | int NOT NULL |
| maxattempts | Maximum
                                                					 number of attempts made to dial a contact for this campaign. | int NOT NULL |
| ansmachineretry | 0 =
                                                					 Dialer should try dialing a contact again if it reached an answering machine 1 =
                                                					 Dialer should not try dialing a contact again if it reached an answering
                                                					 machine | smallint NOT NULL |
| callbacktimelimit | The
                                                					 amount of time in minutes before and after the scheduled callback time, during
                                                					 which the Dialer attempts a callback. | int NULL |
| missedcallbackaction | Indicates what the Dialer should do if a callback could not be
                                                					 placed at the scheduled time: 0 =
                                                					 reschedule callback to same time the next business day 1 = make
                                                					 an ordinary retry 2 =
                                                					 close record | int NULL |
| privatedata | Any
                                                					 fields which are used internally only can be stored in this column in a blob. | BLOB NULL |
| active | Indicates whether the record is active in the system. A record
                                                					 becomes inactive if the campaign is deleted from the system. f =
                                                					 Inactive t =
                                                					 Active | boolean NOT NULL |
| dateinactive | Date
                                                					 this record was deleted. | datetime
                                                					 year to second NULL |
| dialertype | The type
                                                					 of the dialer used for the campaign. The dialer can be any one of the following
                                                					 three types - Predictive, Progressive or Preview Outbound. 0 -
                                                					 Direct Preview Dialer 1 - IVR
                                                					 based Predictive Dialer 2 - IVR
                                                					 based Progressive Dialer Default
                                                					 value = 0 | smallint NOT NULL |
| campaignType | The
                                                					 campaign type can be IVR-based or ICD-based. 0 - IVR
                                                					 based campaign 1 -
                                                					 Agent based campaign Default
                                                					 value = 1 | smallint NOT NULL |
| campaignCallingNum | The
                                                					 campaign calling number that is displayed to the contact. This number is used
                                                					 by the outbound IVR dialer. Note This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive. | Note | This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive. | BLOB NULL |
| Note | This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive. |
| applicationTrigger | This is
                                                					 the JTAPI trigger associated with this campaign. Note This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive. | Note | This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive. | BLOB NULL |
| Note | This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive. |
| applicationName | The name
                                                					 of the application associated with the above-mentioned JTAPI trigger. Note This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive. | Note | This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive. | BLOB NULL |
| Note | This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive. |

| Note | This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive. |
|---|---|

| Note | This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive. |
|---|---|

| Note | This
                                                            						field will have value only if you have an Outbound IVR license on top of
                                                            						Unified CCX premium license in your Unified CCX and the dialer type is
                                                            						progressive or predictive. |
|---|---|

| Field Name | Description | Storage |
|---|---|---|
| recordid | A unique
                                                					 identifier for the record | int NOT NULL Primary
                                                					 Key |
| campaignid | A unique
                                                					 identifier for the campaign, from the Campaign table. | int NOT NULL Primary
                                                					 Key |
| csqid | A unique
                                                					 identifier for the CSQ, from the ContactServiceQueue table. | int NOT NULL Primary
                                                					 Key |
| active | Indicates
                                                					 whether the record is active in the system. A record becomes inactive if the
                                                					 campaign is deleted from the system. f =
                                                					 Inactive t = Active | smallint NULL |
| createdatetime | Default,
                                                					 CURRENT_TIME_STAMP | datetime
                                                					 year to second NULL |
| dateinactive | Date this
                                                					 record was deleted. | datetime
                                                					 year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | A unique
                                                					 identifier for the record | int NOT NULL Primary
                                                					 Key |
| campaignid | A unique
                                                					 identifier for the campaign, from the Campaign table. | int NOT NULL Primary
                                                					 Key |
| supervisorid | A unique
                                                					 identifier for the supervisor, based on the supervisor’s resourceloginid. | nvarchar(50,0) NOT NULL Primary
                                                					 Key |
| active | Indicates
                                                					 whether the record is active in the system. A record becomes inactive if the
                                                					 campaign is deleted from the system. f =
                                                					 Inactive t = Active | boolean NOT NULL |
| createdatetime | Default,
                                                					 CURRENT_TIME_STAMP | datetime
                                                					 year to second NOT NULL |
| dateinactive | Date this
                                                					 record was deleted. | datetime
                                                					 year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordId | A unique identifier for the record | int NOT NULL Primary Key |
| campaignId | The campaign for which the data is recorded | int NOT NULL Primary Key |
| startDate | Start date
                                                					 and time of the interval | datetime
                                                					 year to fraction NOT NULL |
| endDate | End date
                                                					 and time of the interval | datetime
                                                					 year to fraction NOT NULL |
| attemptedCalls | The number
                                                					 of attempted calls in the interval | int NOT NULL |
| abandonedCalls | The number
                                                					 of abandoned calls in the interval | int NOT NULL |
| voiceCalls | The number
                                                					 of voice calls in the interval | int NOT NULL |
| linesPerPort | Lines Per
                                                					 Port value computed depending on the abandoned calls/voice calls | decimal(8,
                                                					 3) NOT NULL |
| active | Indicates
                                                					 whether the data stored is for an active campaign or not. f =
                                                					 Inactive t = Active | boolean NOT NULL |
| dateinactive | The date
                                                					 on which this campaign was deleted | datetime
                                                					 year to fraction |

| Field Name | Description | Storage |
|---|---|---|
| recordid | A unique identifier for the record. | serial NOT NULL Primary Key |
| calid | A unique identifier for the calendar. | int NOT NULL |
| name | Name of the calendar. | lvarchar (30) NOT NULL |
| description | The description of the calendar that is configured in the Unified CCX Administration Calendar Management. | lvarchar (70) NULL |
| timezone | The time zone of the calendar. | nvarchar (50) NOT NULL |
| caltype | Indicates the type of calendar. 1—Full time 2—Flexible | smallint NOT NULL |
| hasspecialdays | Indicates the availability of the special days. | boolean NOT NULL |
| hasholidays | Indicates the availability of the holidays. | boolean NOT NULL |
| active | Indicates whether the record is currently active or not. f = Inactive t = Active | boolean NOT NULL |
| dateinactive | Date and time of the record when it is marked as inactive. | DATETIME year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | A unique identifier for the record. | serial NOT NULL Primary Key |
| calid | A unique identifier for the calendar. | int NOT NULL |
| name | Name of the calendar. | nvarchar (50) NOT NULL |
| caldate | Date of the special day. | DATETIME YEAR TO DAY NOT NULL |
| active | Indicates whether the record is currently active or not. f = Inactive t = Active | boolean NOT NULL |
| dateinactive | Date and time of the record when it is marked as inactive. | DATETIME year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| Id | Unique
                                                					 identifier of the channel provider. Server ID is the foreign key that
                                                					 associates this table with the ContactServiceQueue table. | int NOT NULL Primary
                                                					 Key |
| channelType | Type of
                                                					 contact channel. | varchar
                                                					 (20, 0) NOT NULL |
| sendserverfqdn | FQDN of
                                                					 the channel provider for sending the channel type. | Varchar(255, 0) NOT NULL |
| sendprotocol | Sending
                                                					 protocol that is used to communicate with the channel provider. | Varchar(20, 0) NOT NULL |
| sendserverport | 16-bit
                                                					 port number that is used to communicate with the channel provider for sending
                                                					 the channel type. | int NOT NULL |
| receiveserverfqdn | FQDN of
                                                					 the channel provider for receiving the channel type. | Varchar(255, 0) NOT NULL |
| receiveprotocol | Receiving
                                                					 protocol that is used to communicate with the channel provider. | Varchar(20, 0) NOT NULL |
| receiveserverport | 16-bit
                                                					 port number that is used to communicate with the channel provider for receiving
                                                					 the channel type. | int NOT NULL |
| description | Description of the channel provider. | Lvarchar(400) |
| active | Indicates whether the record is currently active or not. A
                                                					 record becomes inactive if the record is deleted or updated from the system. f =
                                                					 Inactive t =
                                                					 Active | Boolean NOT NULL |
| dateinactive | If the
                                                					 active field is “f”, this field indicates the date and time that the record
                                                					 became inactive. | datetime
                                                					 year to second |
| proxytype | Indicates whether Enable/Disable option is selected for SOCKS
                                                					 Proxy in Mail server configuration page. | Lvarchar(25) |
| mailservertype | Indicates the mail server type. The default is microsoft. | Lvarchar(50) |

| Field Name | Description | Storage |
|---|---|---|
| wdID | Unique ID for each chat widget. It is the foreign key which
                                                					 associates this table with the chatwidget table. | int NOT NULL Primary Key |
| tagID | The tagID for the csq associated with the problem statement. | nvarchar(50) NOT NULL |
| problemStmt | The definition of the problem. | lvarchar (256) NOT NULL |
| psOrder | Order of the problem statement in the chat widget. | int NOT NULL Primary Key |

| Field Name | Description | Storage |
|---|---|---|
| profileId | A unique identifier for the record. | int NOT NULL Primary Key |
| wdID | A unique ID for each widget. | int NOT NULL Primary Key |
| scheduledDay | Scheduled working days in a week. | LVARCHAR(3) NOT NULL |
| fromTime | Start time of business hours. | int NOT NULL |
| toTime | End time of business hours. | int NOT NULL |
| active | Indicates whether the widget is currently active or not. f = Inactive t = Active | boolean NOT NULL |
| dateinactive | The date and time when the record became inactive. | datetime year to second |

| Field Name | Description | Storage |
|---|---|---|
| profileId | A unique identifier for the record. | int NOT NULL Primary Key |
| wdID | A unique ID for each widget. | int NOT NULL Primary Key |
| customType | Scheduled business holiday or the special day. | small int NOT NULL |
| name | Name of the business holiday or the special day. | LVARCHAR(256) NOT NULL |
| dateConfigured | Date of the business holiday or the special day. | datetime year to second NOT NULL |
| fromTime | Start time of business hours. | int |
| toTime | End time of business hours. | int |
| active | Indicates whether the widget is currently active or not. f = Inactive t = Active | boolean NOT NULL |
| dateinactive | The date and time when the record became inactive. | datetime year to second |

| Field Name | Description | Storage |
|---|---|---|
| csqID | Numeric identifier for the CSQ. | int NOT NULL |
| chattriggerpointname | Name of fields present in the chat trigger point. | Ivarchar(256) NOT NULL |
| active | Indicates whether the record is currently active. f = Inactive t = Active | boolean NOT NULL |
| dateinactive | If the active field is “f”, date and time that the record
                                                					 became inactive. | Datetime year to fraction(3) NULL |

| Field Name | Description | Storage |
|---|---|---|
| wdID | Unique ID for each chat widget. It is the foreign key which
                                                					 associates this table with the chatwidget table. | int NOT NULL Primary Key |
| fieldName | Name of fields present in the user form. | lvarchar (200) NOT NULL |
| fieldID | ID of fields present in the user form. | int NOT NULL Primary Key |
| fieldOrder | Order of the field in the widget. | smallint NOT NULL |
| active | Indicates whether the record is currently active or not. f = Inactive t = Active | Boolean NOT NULL |
| lastmodifieddate | The date and time when the user form details were last
                                                					 modified. | datetime year to fraction (3) |

| Field Name | Description | Storage |
|---|---|---|
| wdID | A unique
                                                					 ID for each widget. | int NOT NULL Primary
                                                					 Key |
| wdName | Name of
                                                					 the widget. | lvarchar (50) NOT NULL |
| wdDescription | The
                                                					 description of the widget that is configured in the Unified CCX Administration. | lvarchar
                                                					 (256) NULL |
| wdWelcome | The
                                                					 welcome message that is displayed when the customer joins the chat sessions. | lvarchar
                                                					 (256) NULL |
| wdLogo | The
                                                					 Location of the logo file that is displayed in the customer facing chat widget. | lvarchar
                                                					 (256) NULL |
| wdError | The message that is displayed to the customer when the chat is unavailable. | lvarchar (360) |
| wdJoinTimeout | The
                                                					 message that is displayed to the customer when a chat request is not handled
                                                					 within the set time. | lvarchar
                                                					 (256) NULL |
| wdCode | Blob data
                                                					 to store the HTML code generated for the widget. | BLOB NULL |
| active | Indicates
                                                					 whether the widget is currently active or not. f =
                                                					 Inactive t = Active | boolean NOT NULL |
| lastModifiedDate | The date
                                                					 and time on which the widget details were last modified. | datetime
                                                					 year to fraction (3) NULL |
| offHoursMessage | A
                                                					 message to be displayed off the scheduled business hours. | lvarchar
                                                					 (256) NULL |
| wdType | Indicates the type of widget: 0- Chat Bubble | small
                                                					 int NOT NULL Default
                                                					 0 |

| Field Name | Description | Storage |
|---|---|---|
| recordId | A unique ID for a set of chat bubble properties. | int NOT NULL Primary Key |
| wdId | The ID of the chat widget record that contains the chat bubble record. It is the foreign key which associates this table with
                                             the chatwidget table. | int NOT NULL Primary Key |
| titleText | Title text of the chat bubble. | lvarchar (96) NOT NULL |
| titleTextColor | Text color of the chat bubble title in hex code. | lvarchar (7) NOT NULL |
| titleBackgroundColor | Background color of the chat bubble title text in hex code. | lvarchar (7) NOT NULL Default #EBEBEC |
| buttonText | The text of the chat button. | lvarchar (60) NOT NULL |
| buttonTextColor | Color of the chat button text in hex code. | lvarchar (7) NOT NULL |
| buttonBackgroundColor | Background color of the chat button in hex code. | lvarchar (7) NOT NULL |
| afterResumeNewChatMsg | Text on the chat window that demarks new chat messages from old ones. | lvarchar (60) NOT NULL |
| agentMessageTextColor | Color of the agent message text in hex code. | lvarchar (7) NOT NULL |
| agentMessageBackgroundColor | Background color of the agent message in hex code. | lvarchar(7) NOT NULL |
| fontTypeFace | Font family used for the text in the chat web form and chat window. | lvarchar (120) NOT NULL |
| problemStmtCaption | Label that asks the user to choose a problem statement. | lvarchar (120) NOT NULL |
| ratingEnabled | Whether post-chat rating is available for the chat. | boolean NOT NULL |
| active | Indicates whether the entry is active or inactive. f= Inactive t= Active | boolean NOT NULL |
| dateInactive | Date when the record became inactive. | datetime year to second |

| Field Name | Description | Storage |
|---|---|---|
| sessionid | Identifier that the system assigns to the call. | decimal (18, 0) NOT NULL Primary Key |
| sessionseqnum | Session sequence number that the system assigns to the call. | smallint NOT NULL |
| nodeid | Unique identifier assigned to each server in the cluster. | smallint NOT NULL |
| sourceresourceid | Identifier of the agent who initiated the consult call. | int NOT NULL |
| destinationresourceid | Identifier of the agent who answered the call. | int NOT NULL |
| startdatetime | Date and time when agents are connected and start conversation. | datetime year to fraction (3) NOT NULL |
| enddatetime | Date and time when the call is disconnected. | datetime year to fraction (3) NOT NULL |
| contactid | Unique Identifier for the contact. | varchar (40) NOT NULL |
| csqrecordid | Numeric identifier of the selected CSQ for CSQ-based calls, else -1 is stored. | int NOT NULL |

| Field Name | Description | Storage |
|---|---|---|
| sessionID | Identifier that the system assigned to the call. This identifier remains the same for all legs of the call. | decimal(18,0) NOT NULL Primary Key |
| sessionSeqNum | Session sequence number that the system assigned to the call or the leg. Each leg of a call is assigned a new sequence number. | smallint NOT NULL Primary Key |
| nodeID | Unique identifier that is assigned to each server in the cluster. | smallint NOT NULL Primary Key |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| contactType | Contact type of the call or the leg: 1—Incoming. Outside call received by the Unified CCX system. 2—Outgoing. Call originated by the Unified CCX system, other than a call made within the system. 3—Internal. Call transferred or conferenced between agents, or a call made within the system. 4—Redirect in 5—Transfer in 6—Preview Outbound 7—IVR Outbound 8—Agent Outbound 9—Agent Outbound call that is transferred to IVR | smallint NOT NULL |
| contactDisposition | Disposition of the call or the leg. 1—Abandoned 2—Handled 3—Do not care 4—Aborted 1 5-22—Rejected 99—Cleared | smallint NOT NULL |
| dispositionReason | Reason for disposition. 1—System Error 2—Consult Transfer 3—Blind Transfer 5—Blind Transfer to Experience Management for IVR Survey 6—SIPURI Retrieval Failure for Experience Management Survey 7—JTAPI Transfer Failure for Experience Management Survey 8—Notified Experience Management for SMS/Email Survey | varchar(100,0) NULL |
| originatorType | Originator of the call or the leg: 1—Agent. Call originated by an agent. 2—Device. Call originated by a simulated caller (used for testing) and an agent phone where the agent is not currently logged
                                                   in. 3—Unknown. Call originated by an outside caller through a gateway or by an unknown device. | smallint NOT NULL |
| originatorID | Numeric identifier of the agent who originated the call or the leg. Used only if originatorType is 1. | int NULL |
| originatorDN | If originatorType is 1 and the call was placed by the agent using the non-IPCC extension then this field contains the non-IPCC
                                             extension, else it contains an empty character (''). If originatorType is 2, this field shows the CTI port number. If originatorType is 3, this field shows the telephone number of the caller as received by the Unified CM, if available. An empty character ('') if originatorType is 1. This is not applicable for agent based progressive and predictive outbound
                                             calls. | nvarchar(30,0) NULL |
| destinationType | Destination of the call or the leg: 1—Agent. Call presented to an agent. 2—Device. Call presented to a route point. 3—Unknown. Call presented to an outside destination through a gateway or to an unknown device. Null if no destination. | smallint NULL |
| destinationID | Numeric identifier of the agent who received the call or the leg. Used only if destinationType is 1. | int NULL |
| destinationDN | If the destinationType is 1 and the call was received by an agent using the non-IPCC extension, then this field contains the
                                             non-IPCC extension, else it contains an empty character (''). If destinationType is 2, this field shows the CTI port number. If destinationType is 3, this field shows the telephone number called, if available. An empty character ('') if destinationType is 1. | nvarchar(30) NULL |
| startDateTime | For an incoming call or a leg, date and time that the call or the leg started to ring in the system. For an internal call or for an outgoing call, date and time that the call originated. For a transferred call or a leg, endDateTime of the transferring call or leg. | datetime year to fraction (3) NOT NULL |
| endDateTime | Date and time that this call or the leg was transferred or was disconnected. | datetime year to fraction (3) NOT NULL |
| gmtOffset | Offset, in minutes, between the local time of the Unified CCX server and Greenwich Mean Time. As the time information is stored
                                             in GMT, this field will always be zero. | smallint NOT NULL |
| calledNumber | Telephone number of the device to which the call or leg was presented. If the call or leg was placed to a Unified CCX Route Point, this field shows the directory number configured in the Unified
                                             CM for that Route Point. If the call was placed to an external party, this field shows the telephone number dialed by the caller. | nvarchar(30) NULL |
| origCalledNumber | Telephone number dialed by the caller if the call was placed from an IP phone. The Unified CM directory number to which the VoIP gateway routed the call if the call was placed from outside the VoIP 2 network (for example, from the PSTN 3 or a TDM 4 PBX 5 ). Null if the caller picked up the phone but did not dial any digits. | nvarchar(30) NULL |
| applicationTaskID | Identifier of the Unified CCX or Cisco Unified IP IVR 6 (Unified IP IVR) application task that is associated with the call or the leg. Null for a call that does not have an application associated with it. | decimal(18,0) NULL |
| applicationID | Identifier of the Unified CCX or Unified IP IVR application that processed the call or the leg. Null for a call or a leg that does not have an application associated with it. | int NULL |
| applicationName | Name of the Unified CCX or Unified IP IVR application associated with the call. Null for a call or a leg that does not have an application associated with it. | nvarchar(30) NULL |
| connectTime | Duration of the call in seconds. | int NULL |
| customVariable1 | Contents of the variable _ccdrVar1, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked. Null if this variable is not set. | varchar(40) NULL |
| customVariable2 | Contents of the variable _ccdrVar2, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked. Null if this variable is not set. | varchar(40) NULL |
| customVariable3 | Contents of the variable _ccdrVar3, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked. Null if this variable is not set. | varchar(40) NULL |
| customVariable4 | Contents of the variable _ccdrVar4, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked. Null if this variable is not set. | varchar(40) NULL |
| customVariable5 | Contents of the variable _ccdrVar5, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked. Null if this variable is not set. | varchar(40) NULL |
| customVariable6 | Contents of the variable _ccdrVar6, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked. Null if this variable is not set. | varchar(40) NULL |
| customVariable7 | Contents of the variable _ccdrVar7, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked. Null if this variable is not set. | varchar(40) NULL |
| customVariable8 | Contents of the variable _ccdrVar8, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked. Null if this variable is not set. | varchar(40) NULL |
| customVariable9 | Contents of the variable _ccdrVar9, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked. Null if this variable is not set. | varchar(40) NULL |
| customVariable10 | Contents of the variable _ccdrVar10, if this variable is set by the Set Enterprise Call step in the script that the Unified
                                             CCX or Unified IP IVR application associated with this call or this leg invoked. Null if this variable is not set. | varchar(40) NULL |
| accountNumber | Account number entered by the caller. | varchar(40) NULL |
| callerEnteredDigits | Phone number entered by the caller. | varchar(40) NULL |
| badCallTag | Tag for a bad call. Default = N | char(1) NULL |
| transfer | Was this call leg transferring the call: t = transfer f = no | boolean NULL |
| redirect | Was this call leg redirecting the call: t = redirect f = no | boolean NULL |
| conference | Was this call leg conferencing the call: t = conference f = no | boolean NULL |
| flowout | When this flag is set, it means this call leg is sent to another application or destination outside the system. | boolean NULL |
| metServiceLevel | Did the call meet the service level: t = met service level f = no Note: Reserved for future use. | boolean NULL |
| campaignID | Unique identifier of the campaign that generated this call. | int NULL |
| OrigProtocolCallRef | Unique identifier to identify a call leg that enters the Unified CCX system. This is used to trace a call which has traversed
                                             from some product to the Unified CCX. | Varchar(32) NULL |
| DestProtocolCallRef | Unique Identifier to identify a call leg that exits the Unified CCX system. This is used to trace a call which has traversed
                                             from Unified CCX to some other product. | Varchar(32) NULL |
| CallResult | The result of an IVR based or agent based progressive or predictive outbound call. | smallint NULL |
| dialingListID | Unique identifier of a contact that is dialed for an outbound campaign. Links with DialingList.dialingListID. | int NULL |
| contactid | A unique identifier for all the records related to a single call across various tables in Unified CCX. | varchar(40) |
| lastleg | Indicates whether this is the last leg corresponding to the original call. | boolean |

| Field Name | Description | Storage |
|---|---|---|
| contact id | A unique identifier for the contact. This is used to identify all call records pertaining to a single customer whose call
                                       details are stored across various tables within Unified CCX. | varchar(40) NOT NULL |
| sessionID | An identifier that the system assigns to the call. This identifier remains the same for all legs of the call. | decimal(18,0) NOT NULL |
| sessionSeqNum | A session sequence number that the system assigns to the call or the call leg. Each leg of the call is assigned a new sequence
                                          number. | smallint NOT NULL |
| startDateTime | Date and time the call was put on hold. | datetime year to fraction(3) NOT NULL |
| endDateTime | Date and time the call changed from hold state to retrieved or disconnected state. | datetime year to fraction(3) NOT NULL |
| type | Indicates the hold initiation type. 1 - Agent Initiated 2 - System Initiated | smallint NOT NULL |
| resourceid | Identifier of the agent who has put the call on hold. | int NOT NULL |

| Field Name | Description | Storage |
|---|---|---|
| sessionID | Identifier that the system assigned to the call. This identifier remains the same for all legs of the call. | decimal(18,0) NOT NULL Primary Key |
| sessionSeqNum | Session sequence number that the system assigned to the call or the leg. Each leg of a call is assigned a new sequence number. | smallint NOT NULL Primary Key |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| nodeID | Unique identifier assigned to each server in the cluster. | smallint NOT NULL Primary Key |
| targetID | Numeric ID of the CSQ or the agent depending upon the targetType.Numeric ID of the CSQ or the agent depending upon the targetType. 0—Numeric record ID of the CSQ. (See record ID description in the Contact Service Queue Table) 1—Numeric agent ID (see resourceID description in the Resource Table) | int NOT NULL Primary Key |
| targetType | Indicates whether the call was queued for a CSQ or for an agent. 0 = CSQ 1 = Agent | smallint NOT NULL Primary Key |
| qIndex | For all the new calls that are coming to an agent’s extension through a route point, the value of qIndex is 1. Thereafter,
                                             the value of qIndex is incremented by 1, whenever there is a conference through the route point. | smallint NOT NULL Primary Key |
| queueOrder | The order of the call in the queue. | smallint NOT NULL |
| disposition | Disposition for this leg of the call for this CSQ. Abandoned = 1 7 Handled by CSQ = 2 Dequeued from CSQ = 3 Handled by script = 4 Handled by another CSQ = 5 | smallint NULL |
| metServiceLevel | Call answered within the configured number of seconds of queue time for this CSQ. Yes = t No = f | boolean NULL |
| queueTime | Number of seconds that the caller spent in this CSQ. | int NULL |
| startDateTime | Date and time of an incoming call that is queued to a particular CSQ. | datetime year to fraction (3) |
| endDateTime | Date and time of an incoming call that is dequeued from a particular CSQ. | datetime year to fraction (3) |
| contactid | A unique identifier for all the records related to a single call across various tables in Unified CCX. | varchar(40) |

| Field Name | Description | Storage |
|---|---|---|
| sessionID | Identifier that the system assigned to the call. This identifier remains the same for all legs of the call. | decimal(18, 0) NOT NULL Primary Key |
| sessionSeqNum | Session sequence number that the system assigned to the call or the leg. Each leg of a call is assigned a new sequence number. | smallint NOT NULL Primary Key |
| nodeID | Unique identifier assigned to each server in the cluster. | smallint NOT NULL Primary Key |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| qIndex | For all the new calls that are coming to an agent’s extension through a route point, the value of qIndex is 1. Thereafter,
                                             the value of qIndex is incremented by 1, whenever there is a conference through the route point. | smallint NOT NULL Primary Key |
| origPriority | Priority level assigned to the call or the leg when it was first queued. Null if a priority was not assigned. | smallint NULL |
| finalPriority | Priority level of the call or the leg when it ended. Null if a priority was not assigned. | smallint NULL |
| queueTime | Time (in seconds) that the call was in queue before an agent picked up the call. If the call was in multiple CSQs, then it
                                             is the total time that the call has spent in multiple CSQs. | int NULL |
| startDateTime | For an incoming call or a leg, date and time that the call or the leg was queued for the first CSQ. | datetime year to fraction (3) NOT NULL |
| contactid | A unique identifier for all the records related to a single call across various tables in Unified CCX. | varchar(40) |

| Field Name | Description | Storage |
|---|---|---|
| contactServiceQueueID | Numeric identifier of the CSQ. This ID does not change when CSQ attributes are changed through the Unified CCX Administration
                                             user interface. | int NOT NULL |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL |
| CSQName | Name of the CSQ as set up in Unified CCX Administration. | nvarchar(50,0) NOT NULL |
| resourcePoolType | Type of resource pool that is set up in Unified CCX Administration: 1—Resource groups 2—Resource skills | smallint NOT NULL |
| resourceGroupID | If resourcePoolType is 1, unique identifier used to locate the associated resource group in the Resource Group table. Not used if resourcePoolType is 2. | int NULL |
| selectionCriteria | Resource pool selection model that is set up in the Unified CCX Administration. | nvarchar(30,0) NOT NULL |
| skillGroupID | If resourcePoolType is 2, unique identifier used to locate the associated skill group in the SkillGroup table. Not used if resourcePoolType is 1. | int NULL |
| serviceLevel | Goal, in seconds, for the maximum time that a caller spends in the queue before the call is answered by an agent, as set up
                                             in Unified CCX Administration. | int NOT NULL |
| serviceLevelPercentage | Goal for the percentage of calls that meet the service level that is shown in the serviceLevel field, as set up in Unified
                                             CCX Administration. | smallint NOT NULL |
| active | Indicates whether the record is active: f = Inactive t = Active A record becomes inactive if the CSQ is deleted from the system or if the attributes are changed through the Unified CCX Administration
                                             user interface. When an attribute is changed, the record is marked inactive; that is, the active field is changed to “f”,
                                             and a new record is created. | boolean NOT NULL |
| autoWork | Whether an agent goes to Work State after handling a call from this CSQ: f —No t —Yes | boolean NOT NULL |
| dateInactive | If the active field is “f”, date and time that the record became inactive. | datetime year to fraction (3) NULL |
| queueAlgorithm | Criterion that specifies how contacts are queued, as set up in Unified CCX Administration. | nvarchar(30,0) NOT NULL |
| recordID | Identifier of this record. When any CSQ attribute, such as service level, is changed through the Unified CCX Administration
                                             user interface, the record is marked inactive; that is, the value of the active field changes to “f”, and a new record is
                                             created with a new record ID; the contactServiceQueueID stays the same for that CSQ. | int NOT NULL Primary Key |
| orderList | Reserved for future use. | int NULL |
| wrapupTime | Time in seconds that agent is placed in Work state. Possible values: 1 – 7200 0 – disabled | smallint NULL |
| prompt | The prompt value is used for remote monitoring. The customer can record the name of the CSQ and store it in a WAV file. This
                                             field contains the name of the WAV file. | nvarchar (256) NOT NULL |
| privateData | Any fields which are used internally only can be stored in this column in a blob. | BLOB NULL |
| queueType | A type of the CSQ. Possible values: 0 – voice CSQ 1 – email CSQ 2 – chat CSQ | smallint NOT NULL |
| queueTypeName | The name displayed for the CSQ type. Possible values: Voice Chat Email | nvarchar(30,0) NULL |
| accountuserId | The userid of the email account mapped to an email CSQ. | nvarchar(255,0) NULL |
| channelproviderId | The unique identifier for the channel provider. | int NULL |
| reviewQueueId | Reserved. | int NULL |
| routingType | The type of routing: Interactive Noninteractive | nvarchar(30,0) NULL |
| foldeerName | The name of the email folder that needs to be polled for mails on the mail server. | nvarchar(255,0) NULL |
| pollingInterval | The time (in seconds) on how frequently the email server is polled for any new emails. | int NULL |
| snapshotAge | The time (in minutes) to indicate how far to go back to fetch emails on startup. | int NULL |
| feedId | The unique identifier for the feeds from Customer Collaboration Platform . | nvarchar(30,0) NULL |

| Field Name | Description | Storage |
|---|---|---|
| sessionID | Identifier that the system assigned to the call. This identifier remains the same for all legs of the call. | decimal (18) NOT NULL Primary Key |
| sessionSeqNum | Session sequence number that the system assigned to the call or the leg. Each leg of a call is assigned a new sequence number. | smallint NOT NULL Primary Key |
| resourceID | Numeric identifier of the resource. | int NOT NULL Primary Key |
| wrapupData | Call related information that the agent enters through the Agent Desktop user interface while the agent is in the talking/work
                                             state. | varchar (160) NOT NULL Primary Key |
| nodeid | Unique identifier assigned to each Unified CCX server in the cluster. | smallint Primary Key |
| qindex | A new qIndex is created whenever a Unified CCX call is conferenced to a Unified CCX route point. | smallint Primary Key |
| startDateTime | Date and time that the call or the leg started ringing at the device of an agent. | datetime year to fraction Primary Key |
| wrapupindex | Unique number of wrapup reasons for a particular call. A call can have maximum of five wrapup reasons. | smallint |
| contactid | A unique identifier for all the records related to a single call across various tables in Unified CCX. | varchar(40) |

| Field Name | Description | Storage |
|---|---|---|
| record ID | Unique numeric ID for each record. Introduced for historical reporting purposes. Possible values: 1, 2, 3.... | int NOT NULL Primary Key |
| profileID | The indentifier of the profile | int NOT NULL Primary Key |
| applicationID | Configurable application identifier. Not unique for an application. Exposed for Cisco Unified Intelligent Contact Management
                                             Enterprise (Unified ICME) integration. Configured on Unified CCX Administration, modifiable. Possible values: -1, 1, 2, 3... | int NOT NULL |
| configClass | Represents application configuration class. Possible values: com.cisco.app.ApplicationConfig ApplicationConfig.class | lvarchar(512) NOT NULL |
| version | Specifies internal configuration schema version. Possible values: 1 | int NOT NULL |
| configImplClass | Represents application configuration implementation class. Possible value: com.cisco.crs.app.ScriptApplicationConfig | lvarchar(512) NOT NULL |
| applicationName | Name that uniquely identifies the application | nvarchar(50,0) NOT NULL |
| applicationType | The type of application. Possible values: Busy Ring-No-Answer Cisco Script Application Simulation Script Unified ICME Post-Routing Unified ICME Translation Routing | nvarchar(128,0) NOT NULL |
| applicationEnabled | Whether or not the application is enabled. Possible values: f = disabled t = enabled | boolean NOT NULL |
| numOfSessions | Maximum number of sessions | int NOT NULL |
| description | The description of the application that is configured in the Unified CCX Administration. | nvarchar(128,0) NULL |
| privateData | Internal data not exposed to customers. | BLOB NULL |
| createDateTime | The time when the record is created or updated. Default value: Current year to second | datetime year to second NOT NULL |
| active | Whether this record is active. Possible values: f = inactive t = active | boolean NOT NULL |
| dateInactive | If active = f, the time when this record became inactive. | datetime year to second NULL |
| surveyname | Name of the IVR survey that is associated with the application for post-call survey. | lvarchar(512) |
| dispatchid | The ID of the SMS/Email dispatch that is associated with the application for post-call survey. | varchar(24) |

| Field Name | Description | Storage |
|---|---|---|
| recordID | A unique
                                                					 numeric ID for each record. Introduced for historical reporting purposes. | int NOT NULL Primary
                                                					 Key |
| profileID | Indentifier of the profile Possible
                                                					 values: 1, 2, 3.... | int NOT NULL Primary
                                                					 Key |
| configClass | Represents
                                                					 Group configuration class. Possible
                                                					 values: GroupConfig.class | lvarchar(512) NOT NULL |
| version | Specifies
                                                					 internal configuration schema version. Possible
                                                					 values: 2 | int NOT NULL |
| configImplClass | Represents
                                                					 group configuration implementation class. Possible
                                                					 values: com.cisco.crs.email. CiscoEmailControlGroupConfig. | lvarchar(512) NOT NULL |
| groupClass | Uniquely
                                                					 identifies a group together with the groupID. The class of channels being
                                                					 managed by the group. | lvarchar(400) NOT NULL |
| groupID | Uniquely
                                                					 identifies a group together with groupClassName. Group identifier unique for a
                                                					 give class of channels. | int NOT NULL |
| groupType | Type of
                                                					 the group, corresponding to type of the channels managed by the group as
                                                					 defined since CRS 3.0. | nvarchar(128,0) NOT NULL |
| groupEnabled | Whether
                                                					 the group is enabled. Possible
                                                					 values: f =
                                                					 disabled t =
                                                					 enabled | boolean NOT NULL |
| numOfChannels | Number
                                                					 of channels defined in the group. | int NOT NULL |
| description | Description of the group. | nvarchar(128,0) NULL |
| privateData | Internal
                                                					 data not exposed to customers. | BLOB NULL |
| createDateTime | When the
                                                					 group was created. Default
                                                					 value: Current year to second | datetime
                                                					 year to second NOT NULL |
| active | Whether
                                                					 this record is active. Possible
                                                					 values: f =
                                                					 inactive t =
                                                					 active | boolean NOT NULL |
| dateInactive | If
                                                					 active = f, the time when the record became inactive. | datetime
                                                					 year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordID | Unique
                                                					 numeric ID for each record. Introduced for historical reporting purposes. | int NOT NULL Primary
                                                					 Key |
| profileID | Indentifier of the profile Possible
                                                					 values: 1, 2, 3.... | int NOT NULL Primary
                                                					 Key |
| configClass | Represents
                                                					 trigger configuration class. Possible
                                                					 values: ApplicationTriggerConfig.class | lvarchar(512) NOT NULL |
| version | Specifies
                                                					 internal configuration schema version. Possible
                                                					 values: 3 | int NOT NULL |
| configImplClass | Represents
                                                					 trigger configuration implementation class. Possible
                                                					 values: com.cisco.crs.email. CiscoEmailControlGroupConfig. | lvarchar(512) NOT NULL |
| triggerName | Uniquely
                                                					 identifies a trigger. Available from CRS 4.5 onwards. The API does limit the
                                                					 string length. Go back and revisit the length. | nvarchar(50,0) NOT NULL |
| triggerType | Hard
                                                					 coded. Possible
                                                					 values: Cisco
                                                         						  Http Trigger Cisco
                                                         						  JTAPI Trigger | nvarchar(128,0) NOT NULL |
| applicationName | Application name being triggered by the trigger. | nvarchar(50,0) NOT NULL |
| triggerEnabled | Whether
                                                					 the trigger is enabled Possible
                                                					 values: f =
                                                         						  disabled t =
                                                         						  enabled | boolean NOT NULL |
| numOfSessions | Maximum
                                                					 number of sessions Possible
                                                					 values: 0, 1, 2... | int NOT NULL |
| idleTimeout | Idle
                                                					 time out in milliseconds | int NOT NULL |
| triggerLocale | Default
                                                					 locale for the trigger. Possible
                                                					 values: system.default (the currently configured system default locale) accept.trigger (the locale provided by the incoming event) | nvarchar(50,0) NOT
                                                					 NULL |
| description | Description of the trigger | nvarchar(128,0) NULL |
| misc1 | For HTTP
                                                					 trigger, this field contains the URL. For JTAPI and call triggers, this is the
                                                					 dialed number (DN). | lvarchar(256) NULL |
| misc2 | For
                                                					 JTAPI trigger, this is the partition. | lvarchar(256) NULL |
| privateData | Internal
                                                					 data not exposed to customers, such as parameters or groups associated with a
                                                					 trigger. | BLOB NULL |
| createDateTime | When the
                                                					 trigger was created. Default
                                                					 value: Current year to second | datetime
                                                					 year to second Not
                                                					 NULL |
| active | Whether
                                                					 this record is active. Possible
                                                					 values: f =
                                                					 inactive t =
                                                					 active | boolean NOT NULL |
| dateInactive | If
                                                					 active = f, the time when the record became inactive. | datetime
                                                					 year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | A unique identifier for the record. | serial NOT NULL Primary Key |
| calid | A unique identifier for the calendar. | int NOT NULL |
| name | Name of the calendar. | nvarchar (50) NOT NULL |
| caldate | Date of the special day. | DATETIME YEAR TO DAY NOT NULL |
| shiftname | The shift name configured for the specific day of the week. | nvarchar (25) NOT NULL |
| shifttype | Type of the shift. | smallint NOT NULL |
| fromtime | Shift start time. | int NOT NULL |
| totime | Shift end time. | int NOT NULL |
| active | Indicates whether the record is currently active or not. f = Inactive t = Active | boolean NOT NULL |
| dateinactive | Date and time of the record when it is marked as inactive. | DATETIME year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | A unique identifier for the record. | serial NOT NULL Primary Key |
| calid | A unique identifier for the calendar. | int NOT NULL |
| dow | Day of the week. | nvarchar (3) NOT NULL |
| shiftname | The shift name configured for the specific day of the week. | nvarchar (25) NOT NULL |
| shifttype | Type of the shift. | NOT NULL smallint |
| fromtime | Shift start time in 24 hour format. | int NOT NULL |
| totime | Shift end time in 24 hour format. | int NOT NULL |
| active | Indicates whether the record is currently active or not. f = Inactive t = Active | boolean NOT NULL |
| dateinactive | Date and time of the record when it is marked as inactive. | DATETIME year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | A unique
                                                					 identifier for the record. | int NOT NULL Primary
                                                					 Key |
| dialinglistid | A unique
                                                					 identifier for a contact. | int NOT NULL Primary
                                                					 Key |
| profileid | Identifier
                                                					 of the Unified CCX profile that is associated with this record. | int NOT NULL Primary
                                                					 Key |
| campaignid | Campaign
                                                					 identifier | int NULL |
| createdatetime | Default
                                                					 -CURRENT_TIMESTAMP | datetime
                                                					 year to second NULL |
| accountnumber | The
                                                					 account number of the contact (from the imported file). This field is sent to
                                                					 the agent desktop. | nvarchar(25, 0) NULL |
| firstname | The first
                                                					 name of the contact (from the imported file). | nvarchar(50, 0) NULL |
| lastname | The last
                                                					 name of the contact (from the imported file). | nvarchar(50,0) NULL |
| phone01 | Primary
                                                					 phone number of the contact (from the imported file). | varchar(28,0) NOT NULL |
| phone02 | Additional number of the contact (from the imported file). The
                                                					 number is dialed when the agent selects Skip-Next for the preview call. | varchar(28,0) NULL |
| phone03 | Additional number of the contact (from the imported file). This
                                                					 number is dialed if attempts to dial the first two numbers are unsuccessful. | varchar(28,0) NULL |
| gmtzonephone01 | The time
                                                					 zone for the first phone number of the contact. | smallint NOT NULL |
| dstphone01 | 0 =
                                                					 Daylight Savings Time (DST) is observed at this phone number. 1 = DST
                                                					 is not observed at this phone number | smallint NOT NULL |
| gmtzonephone02 | The time
                                                					 zone for the second phone number of the contact. | smallint NOT NULL |
| dstphone02 | 0 = DST
                                                					 is observed at this phone number. 1 = DST
                                                					 is not observed at this phone number. | smallint NOT NULL |
| gmtzonephone03 | The time
                                                					 zone for the third phone number of the contact. | smallint NOT NULL |
| dstphone03 | 0 = DST
                                                					 is observed at this phone number. 1 = DST
                                                					 is not observed at this phone number. | smallint NOT NULL |
| callbacknumber | Phone
                                                					 number to be used for callback (can be supplied by the agent). | varchar(28,0) NULL |
| callbackdatetime | Customer
                                                					 requested callback time. | datetime
                                                					 year to second NULL |
| callstatus | The
                                                					 status of the contact record: 1 =
                                                					 Pending. The call is pending. 2 =
                                                					 Active. The record is sent (active) to the Outbound subsystem for dialing. 3 =
                                                					 Closed. The record is closed. 4 =
                                                					 Callback. The record is marked for a callback. 5 = Max
                                                					 Calls. Maximum attempts have been reached for this record (considered closed). 6 =
                                                					 Retry. The call is redialed immediately whenever there is any miss. 7 =
                                                					 Unknown. If the Outbound subsystem was restarted with records in the Active (2)
                                                					 state, the records are moved to this state. 8 =
                                                					 Retries with delay. The call is redialed as it was either busy, no answer,
                                                					 customer abandoned or system abandoned. Retry time is set as per the
                                                					 corresponding configuration in the Unified CCX Application Administration web
                                                					 interface. | smallint NOT NULL |
| callresult | The call
                                                					 result from the last call placed for this record. 1 =
                                                					 Voice. Customer answered and was connected to agent. 2 = Fax.
                                                					 Fax machine reached. 3 =
                                                					 Answering machine. Answering machine reached. 4 =
                                                					 Invalid. Number reported as invalid by the network or by the agent. 5 = Do
                                                					 Not Call. Customer does not want to be called again. 6 =
                                                					 Wrong Number. Number successfully contacted but wrong number. 7 =
                                                					 Wrong Person. Number successfully contacted but reached the wrong person. 8 =
                                                					 Callback. Customer requested regular callback. 9 =
                                                					 Skip/Reject. Agent skipped or rejected a preview call. 10 =
                                                					 Skip-Close/Reject-Close. Agent skipped or rejected a preview call with the
                                                					 close option. 11 =
                                                					 Busy. Busy signal detected or marked busy by agent. 12 =
                                                					 Agent did not respond to the preview call within the timeout duration. 13 =
                                                					 Callback Failed - this value is not written to the database; this is for
                                                					 internal use only. 14 =
                                                					 Callback missed and marked for Retry. 15 =
                                                					 Customer's phone timed out either due to Ring No Answer (RNA) or Gateway
                                                					 failure. 16 =
                                                					 Call was abandoned because IVR port was unavailable or Unified CCX failed to
                                                					 transfer the call to the IVR port. 17 =
                                                					 Call failed due any one of the reasons. 18 =
                                                					 Customer abandoned as customer or agent disconnected the call within the time
                                                					 limit as configured in “Abandoned Call Wait Time” in Unified CCX Application
                                                					 Administration web interface. | smallint NOT NULL |
| callresult01 | The call
                                                					 result from the last time phone01 was called. Values
                                                					 are the same as for callResult. | smallint NULL |
| callresult02 | The call
                                                					 result from the last time phone02 was called. Values
                                                					 are the same as for callResult. | smallint NULL |
| callresult03 | The call
                                                					 result from the last time phone03 was called. Values
                                                					 are the same as for callResult. | smallint NULL |
| lastnumberdialed | The last
                                                					 number dialed. 1 =
                                                					 phone01 2 =
                                                					 phone02 3 =
                                                					 phone03 | smallint NULL |
| callsmadetophone01 | The
                                                					 number of call attempts made to phone01. If there is an error in an attempt to
                                                					 call this number, the attempt is not counted here. | smallint NULL |
| callsmadetophone02 | The
                                                					 number of call attempts made to phone02. If there is an error in an attempt to
                                                					 call this number, the attempt is not counted here. | smallint NULL |
| callsmadetophone03 | The
                                                					 number of call attempts made to phone03. If there is an error in an attempt to
                                                					 call this number, the attempt is not counted here. | smallint NULL |
| retry | Indicates whether the contact has to be retried. | boolean NULL |
| active | Contacts
                                                					 becomes inactive for a campaign in the following scenarios: 1 =
                                                					 delete a campaign 2 =
                                                					 delete all the contacts for a campaign f =
                                                					 Inactive t =
                                                					 Active | boolean NOT NULL |
| dateinactive | The date
                                                					 when record became inactive. | datetime
                                                					 year to second NULL |
| numMissedCallback | Number
                                                					 of missed callbacks. | smallint NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | A unique
                                                					 identifier for the record. | int NOT NULL Primary
                                                					 Key |
| dialinglistid | A unique
                                                					 identifier for a contact. | int NOT NULL Primary
                                                					 Key |
| profileid | Identifier
                                                					 of the Unified CCX profile that is associated with this record. | int NOT NULL Primary
                                                					 Key |
| campaignid | Campaign
                                                					 identifier | int NULL |
| createdatetime | Default
                                                					 -CURRENT_TIMESTAMP | datetime
                                                					 year to second NULL |
| accountnumber | The
                                                					 account number of the contact (from the imported file). This field is sent to
                                                					 the agent desktop. | nvarchar(25,0) NULL |
| firstname | The first
                                                					 name of the contact (from the imported file). | nvarchar(50,0) NULL |
| lastname | The last
                                                					 name of the contact (from the imported file). | nvarchar(50,0) NULL |
| phone01 | Primary
                                                					 phone number of the contact (from the imported file). | varchar(28,0) NULL |
| phone02 | Additional number of the contact (from the imported file). The
                                                					 number is dialed when the agent selects Skip-Next for the preview call. | varchar(28,0) NULL |
| phone03 | Additional number of the contact (from the imported file). This
                                                					 number is dialed if attempts to dial the first two numbers are unsuccessful. | varchar(28,0) NULL |
| gmtzonephone01 | The time
                                                					 zone for the first phone number of the contact. | smallint NULL |
| dstphone01 | 0 =
                                                					 Daylight Savings Time (DST) is observed at this phone number. 1 = DST
                                                					 is not observed at this phone number | smallint NULL |
| gmtzonephone02 | The time
                                                					 zone for the second phone number of the contact. | smallint NULL |
| dstphone02 | 0 = DST
                                                					 is observed at this phone number. 1 = DST
                                                					 is not observed at this phone number. | smallint NULL |
| gmtzonephone03 | The time
                                                					 zone for the third phone number of the contact. | smallint NULL |
| dstphone03 | 0 = DST
                                                					 is observed at this phone number. 1 = DST
                                                					 is not observed at this phone number. | smallint NULL |
| callbacknumber | Phone
                                                					 number to be used for callback (can be supplied by the agent). | varchar(28) NULL |
| callbackdatetime | Customer
                                                					 requested callback time. | datetime
                                                					 year to second NULL |
| callstatus | The
                                                					 status of the contact record: 1 =
                                                					 Pending. The call is pending. 2 =
                                                					 Active. The record is sent (active) to the Outbound subsystem for dialing. 3 =
                                                					 Closed. The record is closed. 4 =
                                                					 Callback. The record is marked for a callback. 5 = Max
                                                					 Calls. Maximum attempts have been reached for this record (considered closed). 6 =
                                                					 Retry. The call is redialed immediately whenever there is any miss. 7 =
                                                					 Unknown. If the Outbound subsystem was restarted with records in the Active (2)
                                                					 state, the records are moved to this state. 8 =
                                                					 Retries with delay. The call is redialed as it was either busy, no answer,
                                                					 customer abandoned or system abandoned. Retry time is set as per the
                                                					 corresponding configuration in the Unified CCX Application Administration web
                                                					 interface. | smallint NULL |
| callresult | The call
                                                					 result from the last call placed for this record. 1 =
                                                					 Voice. Customer answered and was connected to agent. 2 = Fax.
                                                					 Fax machine reached. 3 =
                                                					 Answering machine. Answering machine reached. 4 =
                                                					 Invalid. Number reported as invalid by the network or by the agent. 5 = Do
                                                					 Not Call. Customer does not want to be called again. 6 =
                                                					 Wrong Number. Number successfully contacted but wrong number. 7 =
                                                					 Wrong Person. Number successfully contacted but reached the wrong person. 8 =
                                                					 Callback. Customer requested regular callback. 9 =
                                                					 Skip/Reject. Agent skipped or rejected a preview call. 10 =
                                                					 Skip-Close/Reject-Close. Agent skipped or rejected a preview call with the
                                                					 close option. 11 =
                                                					 Busy. Busy signal detected or marked busy by agent. 12 =
                                                					 Agent did not respond to the preview call within the timeout duration. 13 =
                                                					 Callback Failed - this value is not written to the database; this is for
                                                					 internal use only. 14 =
                                                					 Callback missed and marked for Retry. 15 =
                                                					 Customer's phone timed out either due to Ring No Answer (RNA) or Gateway
                                                					 failure. 16 =
                                                					 Call was abandoned because IVR port was unavailable or Unified CCX failed to
                                                					 transfer the call to the IVR port. 17 =
                                                					 Call failed due any one of the reasons. 18 =
                                                					 Customer abandoned as customer or agent disconnected the call within the time
                                                					 limit as configured in “Abandoned Call Wait Time” in Unified CCX Application
                                                					 Administration web interface. | smallint NULL |
| callresult01 | The call
                                                					 result from the last time phone01 was called. Values
                                                					 are the same as for callResult. | smallint NULL |
| callresult02 | The call
                                                					 result from the last time phone02 was called. Values
                                                					 are the same as for callResult. | smallint NULL |
| callresult03 | The call
                                                					 result from the last time phone03 was called. Values
                                                					 are the same as for callResult. | smallint NULL |
| lastnumberdialed | The last
                                                					 number dialed. 1 =
                                                					 phone01 2 =
                                                					 phone02 3 =
                                                					 phone03 | smallint NULL |
| callsmadetophone01 | The
                                                					 number of call attempts made to phone01. If there is an error in an attempt to
                                                					 call this number, the attempt is not counted here. | smallint NULL |
| callsmadetophone02 | The
                                                					 number of call attempts made to phone02. If there is an error in an attempt to
                                                					 call this number, the attempt is not counted here. | smallint NULL |
| callsmadetophone03 | The
                                                					 number of call attempts made to phone03. If there is an error in an attempt to
                                                					 call this number, the attempt is not counted here. | smallint NULL |
| retry | Indicates whether the contact has to be retried. | boolean NULL |
| active | Contacts
                                                					 becomes inactive for a campaign in the following scenarios: 1 =
                                                					 delete a campaign 2 =
                                                					 delete all the contacts for a campaign 3 = when
                                                					 callStatus becomes 3 (closed) or 5 (max calls) f =
                                                					 Inactive t =
                                                					 Active | boolean NULL |
| dateinactive | The date
                                                					 when record became inactive. | datetime
                                                					 year to second NULL |
| numMissedCallback | Number
                                                					 of missed callbacks. | smallint NULL |

| Field Name | Description | Storage |
|---|---|---|
| sessionid | Identifier that the system assigned to the call. This identifier remains the same for all legs of the call. It is the sessionID
                                                of the IVR call; that is, when the supervisor starts monitoring, the monitoring call itself is an IVR call. The supervisor
                                                monitors one or more Unified CCX calls. | decimal(18) NOT NULL Primary Key |
| startmonitoringreqtime | The time and date that the remote supervisor attempted to monitor the agent. | datetime year to fraction (3) NOT NULL |
| startmonitoringcalltime | The time and date that the supervisor began monitoring the call. | datetime year to fraction (3) NOT NULL Primary Key |
| monitoredrsrcid | Identifier of the resource being monitored. | int NOT NULL |
| monitoredsessionseqnum | The session sequence number of the Unified CCX call that is being monitored. | smallint NOT NULL |
| profileid | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| gmtoffset | Offset, in minutes, between the local time of the Unified CCX server and Greenwich Mean Time. As the time information is stored
                                                in GMT, this field will always be zero. | int NOT NULL |
| nodeid | Unique identifier assigned to each server in the cluster. | smallint NOT NULL Primary Key |

| Note | Do not edit this table directly. It is for internal use only |
|---|---|

| Field Name | Description | Storage |
|---|---|---|
| recordId | Unique identifier for the record. | int NOT NULL Primary Key |
| mediaType | Type of the media such as email and other media types. | varchar(30,0) NOT NULL Primary Key |
| fieldName | Name of the field in the customer data. | varchar(50,0) NOT NULL |
| columnId | Field ID in the TextCustomerDetail where this field is stored. | int NOT NULL |

| Field Name | Description | Storage |
|---|---|---|
| profileName | Name of the profile, as set up in the Unified CCX Administration. | nvarchar(50,0) NOT NULL Primary Key |
| profileID | Identifier of the profile. | int NOT NULL |

| Field Name | Description | Storage |
|---|---|---|
| nodeId | Unique
                                                					 identifier assigned to each server in the cluster. | int NOT NULL Primary
                                                					 Key |
| purgeHistoryId | Sequence
                                                					 numbers. | int NOT NULL Primary
                                                					 Key |
| purgeType | PurgeType
                                                					 MANUAL or SCHEDULED. | nvarchar(10,0) NOT NULL |
| purgeState | PurgeState
                                                					 can be any one of, RUNNING, COMPLETED_SUCCESSFULLY, COMPLETED_WITH_ERRORS,
                                                					 UNKNOWN. | nvarchar(30,0) NOT NULL |
| purgeStartedDateTime | Purge
                                                					 start time. | datetime
                                                					 year to fraction(3) NOT NULL |
| hrDbSizeBeforePurge | Historical
                                                					 db size before purge which will have the value using store procedure getDbSize
                                                					 with column name as "used”. | int NULL |
| configDbSizeBeforePurge | Config db
                                                					 size before purge which will have the value using store procedure
                                                					 getDBspaceUsage('db_cra') with column name as "used". | int NULL |
| oldestRecDateTimeBeforePurge | Oldest
                                                					 record date and time before purge. | datetime
                                                					 year to fraction(3) NULL |
| purgeCompletedDateTime | Purge
                                                					 completion time. | datetime
                                                					 year to fraction(3) NULL |
| hrDbSizeAfterPurge | Historical
                                                					 db size after purge which will have the value using store procedure getDbSize
                                                					 with column name as "used". | int NULL |
| configDbSizeAfterPurge | Config db
                                                					 size after purge which will have the value using store procedure
                                                					 getDBspaceUsage('db_cra') with column name as "used". | int NULL |
| oldestRecDateTimeAfterPurge | Oldest
                                                					 record date time after purge. | datetime
                                                					 year to fraction(3) NULL |
| purgetRunTime | Purge
                                                					 run time in minutes which is the difference between purgeCompletedDataTime and
                                                					 purgeStartedDateTime. | int NULL |

| Field Name | Description | Storage |
|---|---|---|
| code | Reason
                                                					 code, as configured in Finesse Administration. | Smallint NOT NULL Primary Key |
| label | Reason
                                                					 label, as configured in Finesse Administration. | NVARCHAR(40,0) NOT NULL |
| category | Type of
                                                					 reason code, label: NOT_READY LOGOUT | NVARCHAR(15,0) NOT NULL Primary Key |
| active | Whether
                                                					 the record is active in the system. A record becomes Inactive if reason code
                                                					 label is deleted from Finesse Administration and this field will be marked
                                                					 "FALSE". | boolean NULL |
| dateinactive | Date and
                                                					 time this record was added, modified, or deleted from Cisco Finesse
                                                					 Administration. | Date time
                                                					 year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| sessionid | Identifier
                                                					 that the system assigned to the call. This identifier remains the same for all
                                                					 legs of the call. This is the sessionID of the IVR call; that is, the call that
                                                					 the supervisor makes to monitor other Unified CCX calls. | decimal(18) NOT NULL Primary
                                                					 Key |
| startmonitoringreqtime | The time
                                                					 and date that the remote supervisor attempted to monitor the agent. | datetime
                                                					 year to fraction (3) NOT NULL Primary
                                                					 Key |
| remoteloginid | The
                                                					 numeric ID the supervisor enters before starting to monitor a call | varchar(50,0) NULL |
| rmonid | Numeric ID
                                                					 of the supervisor who does the monitoring. | int NOT NULL |
| endmonitoringtime | The date
                                                					 and time the monitoring ended. | datetime
                                                					 year to fraction (3) NOT NULL |
| origmonitoredid | If
                                                					 origMonitoredIDType is: 1
                                                         						  (agent), this field contains the extension of the agent being monitored. 2
                                                         						  (CSQ), this field contains the CSQ ID of the CSQ being monitored. | int NOT NULL |
| origmonitoredidtype | Indicates
                                                					 an agent or a CSQ. 1 =
                                                         						  agent 2 =
                                                         						  CSQ | smallint NOT NULL |
| cause | The
                                                					 termination cause of a monitoring session: 3 =
                                                         						  Normal (Monitored) 100 =
                                                         						  Normal (Agent RNA) 0 =
                                                         						  Error (Other) –9 =
                                                         						  Error (Unable to Stop Monitoring) –8 =
                                                         						  Error (Unable to Monitor New Call) –7 =
                                                         						  Error (Agent Logged Off) –6 =
                                                         						  Error (Network Problem) –5 =
                                                         						  Error (VoIP Server unable to communicate) –4 =
                                                         						  Error (Monitoring not allowed) –3 =
                                                         						  Error (Agent not logged in) –2 =
                                                         						  Error (Invalid input) –1 =
                                                         						  Error (Other) | smallint NULL |
| sessionSeqNum | The
                                                					 sequence number for the IVR call; that is, the call the supervisor makes to
                                                					 monitor other Unified CCX calls. | smallint NOT NULL |
| monitoredSessionID | The
                                                					 sessionID of the monitored Unified CCX call. | decimal(18) NOT NULL |
| profileID | Identifier of the Unified CCX profile that is associated with
                                                					 this record. | int NOT NULL Primary
                                                					 Key |
| gmtOffset | Offset,
                                                					 in minutes, between the local time of the Unified CCX server and Greenwich Mean
                                                					 Time. As the time information is stored in GMT, this field will always be zero. | int NULL |
| nodeID | Unique
                                                					 identifier assigned to each server in the cluster. | smallint NOT NULL Primary
                                                					 Key |

| Field Name | Description | Storage |
|---|---|---|
| resourceID | Numeric identifier of the resource. | int NOT NULL Primary Key |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| resourceLoginID | The login name assigned to the resource in the Unified CM. | nvarchar(50,0) NOT NULL |
| resourceName | The first name and the last name of the resource. | nvarchar(50,0) NOT NULL |
| resourceGroupID | Resource group to which the resource belongs. Null if no resource group is assigned to the resource. | int NULL |
| resourceType | Type of the resource: 1—Agent 2—Supervisor 3—Administrator | smallint NOT NULL |
| active | Whether this record is active: f —Inactive t —Active A record becomes inactive if the resource is deleted or updated. | boolean NOT NULL |
| autoAvail | Determines whether the resource goes to Ready State after handling a Unified CCX call: f —No t —Yes | boolean NOT NULL |
| extension | The Unified CCX extension of the resource. | nvarchar(50,0) NOT NULL |
| orderInRG | Order in which the resource resides within the resource group. Null if no resource group is assigned to the resource. | int NULL |
| dateInactive | Date and time that the record became inactive when the active field is "f". | datetime year to fraction(3) NULL |
| resourceSkillMapID | Identifier used to locate the associated skill set of the resource in the ResourceSkillMapping table. The ResourceSkillMapping
                                             table can contain multiple records for one resource. | int NOT NULL |
| assignedTeamID | Team ID of the resource. | int NOT NULL |
| resourceFirstName | First name of the resource. | nvarchar(50,0) NOT NULL |
| resourceLastName | Last name of the resource. | nvarchar(50,0) NOT NULL |
| resourceAlias | Alias name of the resource. | nvarchar(50,0) NULL |
| capabilities | Advanced Supervisor Capabilities for the resource. | smallint NOT NULL |
| resourceEmailId | Email ID of the resource. | nvarchar(255) NULL |

| Field Name | Description | Storage |
|---|---|---|
| resourceGroupID | Numeric identifier of the resource group. | int NOT NULL Primary Key |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| resourceGroupName | Name of the resource group, as set up in the Unified CCX Administration. | nvarchar(50,0) NULL |
| active | Whether the record is active in the Unified CCX system: f —Inactive t —Active A record becomes inactive if the resource group is deleted or updated. | boolean NOT NULL |
| dateInactive | If the active field is “f”, date and time that the record became inactive. | datetime year to fraction(3) NULL |

| Field Name | Description | Storage |
|---|---|---|
| resourceSkillMapID | Identifier of the skill set that is associated with a resource. | int NOT NULL Primary Key |
| skillID | Identifier of the skill that is associated with a resource. | int NOT NULL Primary Key |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| competenceLevel | Competence level associated with the skill, as set up in the Unified CCX Administration. Values range from 1 (lowest) to 10
                                                (highest). | smallint NOT NULL |
| active | Whether the record is active in the Unified CCX system: f —Inactive t —Active A record becomes inactive if the resource group is deleted or updated. | boolean NOT NULL |

| Field Name | Description | Storage |
|---|---|---|
| rmonID | Numeric
                                                					 identifier of the remote supervisor. | int NOT NULL Primary
                                                					 Key |
| contactServiceQueueID | The
                                                					 numeric identifier of the CSQ, relating to contactServiceQueueID in the
                                                					 ContactServiceQueue table. | int NOT NULL Primary
                                                					 Key |
| profileID | Identifier
                                                					 of the Unified CCX profile that is associated with this record. | int NOT NULL Primary
                                                					 Key |

| Field Name | Description | Storage |
|---|---|---|
| rmonID | Numeric identifier of the remote supervisor. | int NOT NULL Primary Key |
| resourceLoginID | The login ID of the resource that the remote supervisor is allowed to monitor. | nvarchar(50,0) NOT NULL Primary Key |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |

| Field Name | Description | Storage |
|---|---|---|
| rmonID | Numeric
                                                					 identifier of the remote supervisor. | int NOT NULL Primary
                                                					 Key |
| LoginID | User login
                                                					 name of the remote supervisor. | nvarchar(50,0) NOT NULL |
| name | Name of
                                                					 the supervisor. | nvarchar(50,0) NOT NULL |
| profileID | Identifier
                                                					 of the Unified CCX profile that is associated with this record. | int NOT NULL Primary
                                                					 Key |
| type | The type
                                                					 of supervisor: 0 =
                                                					 regular supervisor 1 = remote
                                                					 monitoring supervisor | int NOT NULL |
| active | Determines
                                                					 whether the remote supervisor is active. f =
                                                					 inactive t = active | boolean NOT NULL |
| dateInactive | Date and
                                                					 time the remote supervisor became inactive. | datetime
                                                					 year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| csqname | Name of
                                                					 the contact service queue. | nvarchar(50,0) NOT NULL Primary
                                                					 Key |
| loggedinagents | Number
                                                					 agents who are logged in. | int NULL |
| availableagents | Number of
                                                					 available (idle) agents. | int NULL |
| unavailableagents | Number of
                                                					 unavailable agents. | int NULL |
| totalcalls | Total
                                                					 number of calls. | int NULL |
| oldestcontact | Oldest
                                                					 contact in the queue. | int NULL |
| callshandled | Number of
                                                					 calls handled. | int NULL |
| callsabandoned | Number of
                                                					 calls abandoned. | int NULL |
| callsdequeued | Number of
                                                					 calls dequeued. | int NULL |
| avgtalkduration | Average
                                                					 talk duration. | int NULL |
| avgwaitduration | Average
                                                					 wait duration. | int NULL |
| longesttalkduration | Longest
                                                					 talk duration. | int NULL |
| longestwaitduration | Longest
                                                					 wait duration. | int NULL |
| callswaiting | Number
                                                					 of calls waiting. | int NULL |
| enddatetime | The date
                                                					 and time that this table data was last updated. | datetime
                                                					 year to second NULL |
| workingagents | Number
                                                					 of agents who are in the working state. | int NULL |
| talkingagents | Number
                                                					 of agents who are in the talking state. | int NULL |
| reservedagents | Number
                                                					 of agents who are in the reserved state. | int NULL |
| startdatetime | The date
                                                					 and time that this table’s statistics get collected. | datetime
                                                					 year to second NULL |
| convavgtalkduration | Average
                                                					 talk duration in HH:MM:SS format. | varchar(25,0) NULL |
| convavgwaitduration | Average
                                                					 wait duration in HH:MM:SS format. | varchar(25,0) NULL |
| convlongesttalkduration | Longest
                                                					 talk duration in HH:MM:SS format. | varchar(25,0) NULL |
| convlongestwaitduration | Longest
                                                					 wait duration in HH:MM:SS format. | varchar(25,0) NULL |
| convoldestcontact | Oldest
                                                					 call in the queue in HH:MM:SS format. | varchar(25,0) NULL |

| Field Name | Description | Storage |
|---|---|---|
| type | Contact
                                                					 Service Queue type that identifies the contact type it services. It can be
                                                					 either voice or e-mail. | nvarchar(50,0) NOT NULL Primary
                                                					 Key |
| totalcsqs | Number of
                                                					 CSQs configured. | int NULL |
| loggedinagents | Number of
                                                					 agents who are logged in. | int NULL |
| workingagents | Number of
                                                					 agents who are in the working state. | int NULL |
| reservedagents | Number of
                                                					 agents who are in the reserved state. | int NULL |
| talkingagents | Number of
                                                					 agents who are in the talking state. | int NULL |
| availableagents | Number of
                                                					 available (idle) agents. | int NULL |
| unavailableagents | Number of
                                                					 unavailable agents. | int NULL |
| totalcalls | Total
                                                					 number of calls. | int NULL |
| callswaiting | Number of
                                                					 calls waiting. | int NULL |
| callshandled | Number
                                                					 of calls handled. | int NULL |
| callsabandoned | Number
                                                					 of calls abandoned. | int NULL |
| avgtalkduration | Average
                                                					 talk duration. | int NULL |
| avgwaitduration | Average
                                                					 wait duration. | int NULL |
| longesttalkduration | Longest
                                                					 talk duration. | int NULL |
| longestwaitduration | Longest
                                                					 wait duration. | int NULL |
| oldestcontact | Oldest
                                                					 contact in the queue. | int NULL |
| startdatetime | Data
                                                					 collection starting time. | datetime
                                                					 year to second NULL |
| enddatetime | Date and
                                                					 time this table was last updated. | datetime
                                                					 year to second NULL |
| convavgtalkduration | Average
                                                					 talk duration in HH:MM:SS format. | varchar(25,0) NULL |
| convavgwaitduration | Average
                                                					 wait duration in HH:MM:SS format. | varchar(25,0) NULL |
| convlongesttalkduration | Longest
                                                					 talk duration in HH:MM:SS format. | varchar(25,0) NULL |
| convlongestwaitduration | Longest
                                                					 wait duration in HH:MM:SS format. | varchar(25,0) NULL |
| convoldestcontact | Oldest
                                                					 call in the queue in HH:MM:SS format. | varchar(25,0) NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | Unique identifier of the record. | int NOT NULL Primary Key |
| resourceloginid | The login ID of the resource being rekilled for a CSQ. | nvarchar(50) NOT NULL |
| csqid | Unique identifier of the CSQ for which the resource is being reskilled. | int NOT NULL |
| operation | Indicates the type of operation to be performed - either addition/removal of a resource for a CSQ. Scheduled Addition(1) Scheduled Removal(2) | smallint NOT NULL |
| reskiller | Login ID of the resource who has scheduled addition/removal of a resource for a CSQ. | nvarchar(50) NOT NULL |
| reskiller_type | Indicates whether supervisor/admin has scheduled addition/removal of a resource for a CSQ. Supervisor(1) Administrator(2) | smallint NOT NULL |
| scheduletime | Epoch time in seconds, indicating when the resource will be added/removed for a CSQ. | bigint NOT NULL |
| active | Indicates whether the record is active or not. When a resource is successfully added/removed for a CSQ, this field is set
                                             to false. | boolean NOT NULL |
| dateinactive | Date and time of the record when it is marked as inactive. | datetime year to second |

| Field Name | Description | Storage |
|---|---|---|
| nodeid | Identifier used for conflict resolution in an island mode. | int NOT NULL |
| scheduledid | Foreign key to the schedule_reskill table. | int NOT NULL |
| timestamp | Schedule execution time. | datetime year to second NOT NULL |
| status | The status of the schedule while adding or removing the agents for the CSQ. 0 = Agent is successfully added or removed for the CSQ. 1 = Agent is already part of the CSQ or is removed from the CSQ. 2 = Operation failed due to connectivity issues. 3 = Agent is not available in the Unified CCX system. 4 = CSQ is not available in the Unified CCX system. 5 = Failed to complete the operation due to internal errors. | smallint NOT NULL |

| Field Name | Description | Storage |
|---|---|---|
| skillID | Numeric
                                                					 identifier of the skill. | int NOT NULL Primary
                                                					 Key |
| profileID | Identifier
                                                					 of the Unified CCX profile that is associated with this record. | int NOT NULL Primary
                                                					 Key |
| skillName | Name of
                                                					 the skill, as set up in the Unified CCX Administration. | nvarchar(50,0) NOT NULL |
| active | Determines
                                                					 whether the record is active in the Unified CCX system: f
                                                					 —Inactive t —Active A record
                                                					 becomes inactive if the skill is deleted or updated. | boolean NOT NULL |
| dateInactive | If the
                                                					 active field is “f”, date and time that the record became inactive. | datetime
                                                					 year to fraction(3) NULL |

| Field Name | Description | Storage |
|---|---|---|
| skillGroupID | Numeric
                                                					 identifier of the skill group. | int NOT NULL Primary
                                                					 Key |
| skillID | Numeric
                                                					 identifier of the skill. | int NOT NULL Primary
                                                					 Key |
| profileID | Identifier
                                                					 of the Unified CCX profile that is associated with this record. | int NOT NULL Primary
                                                					 Key |
| competenceLevel | Minimum
                                                					 acceptable skill level for agents with this skill, as set up in the Unified CCX
                                                					 Administration. Values range from 1 (lowest) to 10 (highest). | smallint NOT NULL |
| active | Determines
                                                					 whether the record is active in the CSQ: f
                                                					 —Inactive t —Active A record
                                                					 becomes inactive if the new skill group is deleted or updated. | boolean NOT NULL |
| skillWeight | Skills
                                                					 within a CSQ can be assigned weights. This field is used in the weighted skill
                                                					 calculation of the skill-based resource selection algorithm. Default
                                                					 value is 1. | int NOT NULL |
| skillOrder | Skills
                                                					 within a CSQ can be ordered. This field is used in the order skill calculation
                                                					 of the skill-based resource selection algorithm. Default
                                                					 value is 1. | int NOT NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordID | Numeric identifier of this supervisor. | int NOT NULL Primary Key |
| resourceLoginID | User ID in the Unified CM configuration. | nvarchar(50,0) NOT NULL |
| managedTeamID | Team identifier of the managed team. | int NOT NULL |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| supervisorType | Type of supervisor for this team 0 = Primary 1 = Secondary | smallint NOT NULL |
| active | Indicates whether the record is active in the Unified CCX system. A record becomes inactive if a team is deleted or updated. f = Inactive t = Active | boolean NOT NULL |
| dateInactive | Date this record was deleted. | datetime year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | A unique identifier for the record. | int NOT NULL Primary Key |
| profileid | An identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| resourceloginid | The login name assigned to the resource in the Unified CM. | nvarchar(50,0) NOT NULL |
| campaignid | A unique identifier for the campaign. | int NOT NULL |
| active | Indicates whether the record is active. | boolean NOT NULL |
| dateinactive | Date this record is deleted. | datetime year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | A unique identifier for the record. | int NOT NULL Primary Key |
| profileid | An identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| resourceloginid | The login name assigned to the resource in the Unified CM. | nvarchar(50,0) NOT NULL |
| applicationid | A unique identifier for the application. | int NOT NULL |
| active | Indicates whether the record is active. | boolean NOT NULL |
| dateinactive | Date this record is deleted. | datetime year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| teamID | Numeric identifier for this team. | int NOT NULL Primary Key |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| teamName | Name of this team. | nvarchar(50,0) NOT NULL |
| active | Indicates whether the record is active in the Unified CCX system. A record becomes inactive if a team is deleted or updated. f = Inactive t = Active | boolean NOT NULL |
| dateInactive | Date this record was deleted. | datetime year to fraction(3) NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordID | Numeric identifier for this record. | int NOT NULL Primary Key |
| csqID | Numeric identifier for the CSQ. | int NOT NULL |
| teamID | Numeric identifier for the team. | int NOT NULL |
| profileID | Identifier of the Unified CCX profile that is associated with this record. | int NOT NULL Primary Key |
| active | Indicates whether the record is active in the Unified CCX system. A record becomes inactive if a team is deleted or updated. f = Inactive t = Active | boolean NOT NULL |
| dateInactive | Date this record was deleted. | datetime year to second NULL |

| Field Name | Description | Storage |
|---|---|---|
| ContactID | Alphanumeric identifier for the contact. | varchar (64,0) NOT NULL Primary Key |
| ContactSeqNum | Contact sequence number that the system assigned to the contact or the leg. Each leg of a contact is assigned a new contact
                                             sequence number. To be used later. | smallint NOT NULL Primary Key |
| nodeID | Numeric identifier for the node. | smallint NOT NULL |
| resourceID | Numeric identifier for the resource. | int NOT NULL Primary Key |
| startDateTime | Date and time that the contact or leg entered the system. | datetime year to fraction (3) NOT NULL Primary Key |
| endDateTime | Date and time that the contact or the leg was transferred or disconnected. | datetime year to fraction (3) NOT NULL |
| qIndex | A new qIndex is created whenever a Unified CCX contact is conferenced to a Unified CCX route point. To be used later. | smallint NOT NULL |
| acceptTime | Amount of time, in seconds, that passed from the time a contact or leg was presented to an agent and the agent answered the
                                             contact. | smallint NULL |
| talkTime | Amount of time, in seconds, that passed from the time an agent answered the contact or the leg to the time the contact or
                                             the leg was disconnected or transferred, not including hold time. | smallint NULL |
| workTime | Amount of time, in seconds, that an agent spent in Work State after the contact or the leg. To be used later. | smallint NULL |
| WrapupData | The contact information that the agent enters after the contact is handled through the Agent Desktop user interface. | varchar(40,0) NULL |
| contactdisposition | Disposition of the contact. | smallint NOT NULL Default: 0 |
| loginsessionid | Unique identifier of an agent login session. This identifier remains the same until the session ends. | varchar(18) |
| mediasessionid | Indicates the media session identifier assigned while assigning the contact. It can be 1 to 5 for ‘Chat’ media and 26 to 30
                                             for ‘Email’ media, depending on the maximum sessions configured by the administrator in ‘Channel Parameter’ configuration
                                             page of AppAdmin. | smallint |
| csqrecordid | Numeric identifier of the CSQ in which the agent received an email or chat contact. | int |

| Field Name | Description | Storage |
|---|---|---|
| agentID | Identifier of the agent whose state has changed. | int NOT NULL Primary Key |
| stateChangeDatetime | Date and time that the chat agent state changed. | datetime year to fraction (3) NOT NULL Primary Key |
| agentStateID | Event that triggered the chat agent state change: 0—Logon 1—Log off 2—Not available 3—Available 4—Busy 5—Unknown 6—Partial busy 7—Reserved | smallint NOT NULL Primary Key |
| reasonCode | Code, as written to the database, for the reason that the chat agent changed to Not Ready state or to Log Out state. 32750—Non chat agent 32755—Contact ended 32757—Media handler failure 32760—Login 32763—Contact not accepted 32764—CCX failure 32765—Connection down | smallint NOT NULL Primary Key |
| routingType | Routing type of the contact or leg: 1—Interactive 2—Non Interactive | smallint NOT NULL Primary Key |
| loginsessionid | Unique identifier of an agent login session. This identifier remains the same until the session ends. | varchar(18) |
| contactid | Alphanumeric identifier for the contact. This field will have an identifier only if the agent state changes due to allocating or handling a contact. Else, it will
                                             be NULL. | varchar(64) |

| Field Name | Description | Storage |
|---|---|---|
| ContactID | Alphanumeric identifier for the contact. | varchar
                                                					 (64,0) NOT NULL Primary
                                                					 Key |
| resourceID | Numeric
                                                					 identifier for the resource. | int NOT NULL Primary
                                                					 Key |
| reasonID | Numeric
                                                					 identifier for the reason. | int NOT NULL |
| wrapupTime | Date and
                                                					 time that the Wrap-Up is applied. | datetime
                                                					 year to fraction (3) NOT NULL Primary
                                                					 Key |
| MediaType | Type of
                                                					 the media such as email and other media types. 1—Chat 3—Email | smallint NULL |

| Field Name | Description | Storage |
|---|---|---|
| ContactID | Alphanumeric identifier for this record. | varchar (64,0) NOT NULL Primary Key |
| ContactSeqNum | Contact sequence number that the system assigned to the contact or the leg. Each leg of a contact is assigned a new contact
                                             sequence number. To be used later. | smallint NOT NULL Primary Key |
| nodeID | Numeric identifier for the node. | smallint NOT NULL |
| contactType | Type of contact or leg: 1—Incoming. Outside contact received by the Unified CCX system. | smallint NOT NULL |
| mediaType | Type of the media such as email and other media types. 1—Chat 3—Email | smallint NOT NULL |
| contactDisposition | Disposition of the contact or the leg. 1—Abandoned 2—Handled 3—Do not care 4—Aborted 8 5—Rejected 6—Cleared 7—Unknown | smallint NOT NULL |
| dispositionReason | Reason why the contact is aborted or rejected by the system. Unknown Chat_agent_ended Chat_customer_ended Chat_agent_aborted Chat_agent_abandoned Chat_customer_abandoned Chat_abandoned_timeout Chat_customer_abandoned Chat _customer_waited Chat_system_failure Chat_system_failure_before_agent_joined Chat_agent_connection_failure Chat_agent_end_before_in _chatroom | varchar(100,0) NULL |
| originatorType | Originator of the contact or the leg: 1—Agent. Contact originated by an agent. 2—Unknown. Contact originated from outside. | smallint NOT NULL |
| originator | Numeric identifier of the agent who originated the contact or the leg. Used only if originatorType is 1. | nvarchar(50,0) int NULL |
| destinationType | Destination of the contact or the leg: 1—Agent. Contact presented to an agent. Null if no destination. | smallint NOT NULL |
| destination | Numeric identifier of the agent who received the contact or the leg. Used only if destinationType is 1. | nvarchar(50,0) int NULL |
| startDateTime | Date and the time that the contact or the leg is presented to the agent. | datetime year to fraction (3) NOT NULL |
| endDateTime | Date and time that the contact or the leg is transferred or disconnected. | datetime year to fraction (3) NOT NULL |
| tagID | The string with which the contact or the leg is tagged. | nvarchar(50,0) NULL |
| source | Source from which the contact originated. 1—Bubble Chat 2—Fb Messenger -1—Others | smallint |

| Field Name | Description | Storage |
|---|---|---|
| ContactID | Alphanumeric identifier for the contact. | varchar
                                                					 (64,0) NOT NULL Primary
                                                					 Key |
| ContactSeqNum | Contact
                                                					 sequence number that the system assigned to the contact or the leg. Each leg of
                                                					 a call is assigned a new contact sequence number. To be used
                                                					 later. | smallint NOT NULL Primary
                                                					 Key |
| nodeID | Numeric
                                                					 identifier for the node. | smallint NOT NULL |
| csqRecordID | Numeric
                                                					 identifier for the chat and email CSQ. | int NOT NULL Primary
                                                					 Key |
| qIndex | A new
                                                					 qIndex is created whenever a Unified CCX contact is conferenced to a Unified
                                                					 CCX route point. To be used
                                                					 later. | smallint NOT NULL Primary
                                                					 Key |
| disposition | Disposition for this leg of the contact for this CSQ. Abandoned = 1 9 Handled by CSQ = 2 Dequeued from CSQ = 3 Handled by another CSQ = 4 | smallint NULL |
| metServiceLevel | Contact
                                                					 answered within the configured number of seconds of queue time for this CSQ. Yes =
                                                         						  t No = f To be
                                                					 used later. | boolean NULL |
| queueTime | Number
                                                					 of seconds the contact spent in queue for this CSQ and this leg of the contact. | int NULL |

| Field Name | Description | Storage |
|---|---|---|
| ContactID | Alphanumeric identifier for this record. | nvarchar (64,0) NOT NULL Primary Key |
| FieldID1 to FieldID10 | The unique field IDs corresponding to the field names in the
                                                					 non-voice contact or MediaCustomerDataMapping
                                                					 table. In actual table schema there are 10 individual columns named
                                                					 FieldID1 through FieldID10. | int NOT NULL |
| FieldValue1 to FieldValue5 FieldValue9 to FieldValue10 | Indicates the field values provided for the corresponding
                                                					 field names in
                                                					 the non-voice contact or MediaCustomerDataMapping table. In actual table schema there are 10 individual columns named
                                                					 FieldValue1 through FieldValue10. | lvarchar (600) NOT NULL |
| FieldValue6 to FieldValue8 | Indicates the field values provided for the corresponding
                                                					 field names in the non-voice contact or MediaCustomerDataMapping table. In case of email contact the field values 6 to 8 are used for
                                                					 the Agent added email addresses in the CC, BCC and To fields respectively. | lvarchar (5080) NULL |
| InsertionDate | Indicates the date and time of insertion. | datetime year to fraction(3) NOT NULL |

| Field Name | Description | Storage |
|---|---|---|
| ContactID | Alphanumeric identifier for this record. | varchar (64) NOT NULL Primary Key |
| Rating | The rating given by the customer. | smallint NOT NULL |
| RatingTime | Date and time the customer assigned the rating. | datetime year to fraction (3) NOT NULL |

| Field Name | Description | Storage |
|---|---|---|
| taskID | Identifier
                                                					 of the task. | decimal(18,0) NOT NULL Primary
                                                					 Key |
| parentTaskID | Identifier
                                                					 of the parent task, if the task is a subtask. | decimal(18,0) NULL |
| startDateTime | Date and
                                                					 the time that the task started executing. | datetime
                                                					 year to second NULL |
| endDateTime | Date and
                                                					 the time that the task completed executing. | datetime
                                                					 year to second NULL |
| applicationServerID | Unique
                                                					 identifier assigned to each Unified CCX server in the cluster. | smallint NOT NULL Primary
                                                					 Key |

| Field Name | Description | Storage |
|---|---|---|
| categoryid | A unique identifier for the Wrap-Up category. | int NOT NULL Primary Key |
| profileid | Identifier
                                                					 of the Unified CCX profile that is associated with this record. | int NOT
                                                					 NULL Primary
                                                					 Key |
| recordid | A unique identifier for the record. | int NOT NULL Primary Key |
| name | The name
                                                					 of the Wrap-Up category. | nvarchar(160,0) NOT
                                                					 NULL |
| type | The type
                                                					 of interaction for which the Wrap-Up reason is applied. For example, Non-Voice. | lvarchar(40) NOT
                                                					 NULL |
| global | Indicates
                                                					 whether the Wrap-Up category is tagged at global or CSQ level. | boolean NOT
                                                					 NULL |
| active | Indicates
                                                					 whether the record is currently active. | boolean NOT
                                                					 NULL |
| dateinactive | The date
                                                					 and time when the record became inactive. | datetime
                                                					 year to second NULL |
| createdatetime | The date and time that the record is created. Default value: Current year to second. | bigint NULL |

| Field Name | Description | Storage |
|---|---|---|
| reasonid | A unique identifier for the Wrap-Up reason. | int NOT NULL Primary Key |
| categoryid | A unique
                                                					 identifier for the Wrap-Up category. | int NOT
                                                					 NULL |
| reason | The name of the Wrap-Up reason. | nvarchar(160,0) NOT NULL |
| active | Indicates whether the record is currently active. | boolean NOT NULL |
| dateinactive | The date and time when the record became inactive. | datetime year to second NULL |
| createdatetime | The date
                                                					 and time that the record is created. Default
                                                					 value: Current year to second. | bigint NULL |

| Field Name | Description | Storage |
|---|---|---|
| recordid | A unique
                                                					 identifier for the record. | int NOT NULL Primary
                                                					 Key |
| categoryid | A unique
                                                					 identifier for the Wrap-up Category. | int NOT
                                                					 NULL |
| csqid | A unique
                                                					 identifier for the CSQ from the ContactServiceQueue table. | int NOT
                                                					 NULL |
| active | Indicates
                                                					 whether the record is currently active. | boolean NOT
                                                					 NULL |
| dateinactive | The date and time when the record became inactive. | datetime year to second NULL |
| createdatetime | The date
                                                					 and time that the record is created. Default
                                                					 value: Current year to second. | bigint NULL |