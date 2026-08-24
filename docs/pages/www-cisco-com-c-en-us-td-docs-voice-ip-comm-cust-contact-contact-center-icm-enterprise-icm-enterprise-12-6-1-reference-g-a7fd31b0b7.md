---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-reference-g-a7fd31b0b7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/reference/guide/ucce_b_database-schema-handbook_12_6_1/ucce_b_database-schema-handbook_12_6_1_chapter_0101.html
retrieved_at: 2026-08-24T23:13:20.193371+00:00
---

Database Schema Handbook for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

# Database Schema Handbook for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1)

Updated: May 14, 2021

Chapter: Database Rules

## Chapter: Database Rules

# Database Rules

## Blended Agent Tables
                        	 (Outbound Option)

To see a list and an
                           		illustration of the Blended Options tables, see Blended Agent (Outbound Option) .

With the optional
                           		Outbound Option feature, you can configure a contact center for automated
                           		inbound and outbound calling activities.

The 
                           		Blended Agent Options (see Blended_Agent_Options )
                           		contains all options that are global to a Blended Agent deployment, such as
                           		time parameters for calling a contact.

Campaign and Query Rules

A campaign delivers outgoing calls to agents for a specific purpose or goal. The goal
                           		might be to send a particular message (for example, to invite current clients
                           		to take advantage of a new service) or make a particular query (for example, to
                           		inquire about an account).

A query rule is a
                           		SQL filter function that selects contact records and associates those records
                           		with a campaign. Contact records are selected from import lists you provide to
                           		the Blended Agent software.

The 
                           		Campaign (see Campaign ) contains
                           		information for all the campaigns defined in a Outbound Option implementation.
                           		(There is a single row for every configured campaign.)

The 
                           		Campaign Half Hour (see Campaign_Half_Hour )
                           		provides historical reporting for campaign attributes.

The 
                           		Campaign Query Rule (see Campaign_Query_Rule ) is
                           		a cross-reference table between the Campaign table and the Query Rule Table.

The 
                           		Campaign Skill Group (see Campaign_Skill_Group )
                           		is a cross-reference table between Campaign table and the Skill Groups table.
                           		It defines the association between skill groups and campaigns.

The 
                           		Campaign Target
                           		  Sequence (see Campaign_Target_Sequence ) contains the target type and sequence with which numbers are
                           		dialed within a campaign.

The 
                           		Campaign Query Rule Real
                           		  Time (see Campaign_Query_Rule_Real_Time ) and 
                           		Campaign Query Rule Half
                           		  Hour (see Campaign_Query_Rule_Half_Hour ) provide statistics on particular Campaign-Query Rule combinations.

The 
                           		Query Rule Clause (see Query_Rule_Clause )
                           		contains the SQL rules associated with each query rule. There is a single row
                           		for each configured query rule.

The 
                           		Query Rule (see Query_Rule ) is a
                           		cross-reference table between Query Rule Clause table and the Import Rule
                           		table.

Import Rules

An import rule defines how Blended Agent imports data from an import list into a contact
                           		table. The information in the contact table can then be used to build a dialing
                           		list.

An import list is a
                           		raw set of customer contacts (in text file format) that can be imported into a
                           		contact table and used to build a dialing list. The import list may also be
                           		referred to as an import file or a contact file .
                           		The import list is associated with a particular campaign and query rule.

The 
                           		Import Rule (see Import_Rule ) contains a
                           		list of all the import rules and their associated import lists.

The 
                           		Import Rule Real Time (see Import_Rule_Real_Time )
                           		and the 
                           		Import Rule History (see Import_Rule_History )
                           		contain statistics on the Outbound Option imports and the success rate of the
                           		imports.

The 
                           		Import Rule Clause (see Import_Rule_Clause )
                           		defines the portions of an import list to be imported by the Blended Agent
                           		Import Rule process.

Dialers

The dialer is is
                           		used in Outbound Option to define the relationship between skill groups, the
                           		ACDs to which they are connected, and the ports on a dialer board. The settings
                           		you assign to the dialer control how it handles dialing from your location and
                           		how it responds to answering machines or human voices. Several database tables
                           		control dialer configuration and record statistics.

The 
                           		Dialer (see Dialer ) contains
                           		configuration information for each dialer in a Outbound Option implementation.

The 
                           		Dialer Port Map (see Dialer_Port_Map ) maps
                           		port numbers on the dialer to the ports on the ACD, and identifies the ACD
                           		stations and their mapping to dialer ports.

Two reporting tables, Dialer Real Time (see Dialer_Real_Time ) and Dialer Half Hour (see Dialer_Half_Hour ) provide statistics for reporting on dialer implementation.

Two reporting tables, 
                           		Dialer Skill Group Real
                           		  Time (see Dialer_Skill_Group_Real_Time ) and 
                           		Dialer Skill Group Half
                           		  Hour (see Dialer_Skill_Group_Half_Hour ) provide reports on campaigns running on a dialer.

The Dialer Detail (see Dialer_Detail ) is a historical table that saves the detailed dialer records that allow enhanced troubleshooting and tracking of dialer
                           attempts, agent-skipped calls, and termination codes.

## Business Hours Tables

To see a list and an illustration of the Business Hour tables, see Business Hours .

Business_Hours contains one entry for each business hour and maps to business hour reason, time zone, and department.

Business_Hours_Real_Time maps to business hours.

Business_Hours_Reason contains one entry for each business reason.

Special_Day_Schedule contains one entry for each special day schedule and maps to business hour and business reason.

Time_Zone_Location contains time zones from the system and maps to business hour.

Week_Day_Schedule contains one entry each for weekday schedule and maps to business hour.

## Contact Sharing
                        	 Tables

To see a list and an
                           		illustration of the Contact Sharing tables, see Contact Sharing .

A Contact Share
                           		Group (see the Contact_Share_Group )
                           		applies to a group of contact share precision queues and/or skill groups.

Each Contact Share
                           		Group Member (see the Contact_Share_Group_Member )
                           		contains one or more contact share queues.

Each Contact Share
                           		Queue (see the Contact_Share_Queue )
                           		maps to either a skill group or a precision queue using a TargetQueueID.

A Contact Share Rule
                           		(see the Contact_Share_Rule )
                           		applies for all contact share precision queues or skill groups within a contact
                           		share group.

## CX Survey_Table (For Future Use)

To see a list and an illustration of the Survey tables, see Survey (For Future Use) .

Survey (For Future Use) contains one entry for each survey and maps to survey_question and calltype.

Survey_Question (For Future Use) contains one entry per question for each survey type.

Call_Type contains new columns which maps to surveyID. one calltype can map to one surveyID.

Survey_Result (For Future Use) contains response for each question type per survey and maps to surveyID and question type.

## Device
                        	 Tables

To see a list and an
                           		illustration of the Device tables, see Device .

A 
                           		Logical Interface
                           		  Controller (see Logical_Interface_Controller ) is either a Peripheral Gateway (PG) or a Network Interface
                           		Controller (NIC) .

Each logical interface
                           		controller maps to a 
                           		Physical Interface
                           		  Controller (see Physical_Interface_Controller ). If NICs are duplexed, each NIC in the duplexed pair maps to
                           		a separate Physical Interface Controller. A duplexed pair of PGs share a single
                           		Physical Interface Controller.

A 
                           		Routing Client (see Routing_Client ) is a service,  such as AT&T, MCI, or Sprint, or a switch within a private network. If a logical
                           		interface controller is a NIC, it has one or more associated routing clients.
                           		If a logical interface controller is a PG, it may have one or more associated
                           		routing clients (if peripherals managed by the PG support Post-Routing)

Each routing client
                           		may have one or more associated 
                           		Dial Number Plans (see Dial_Number_Plan ).

A 
                           		Peripheral (see Peripheral ) is an ACD,
                           		PBX, or VRU . Each peripheral is associated with a Peripheral Gateway.

Trunks

Each peripheral has
                           		one or more 
                           		Trunk Groups (see Trunk_Group ). The
                           		public telephone network may group trunks differently, so each PG may have one
                           		or more 
                           		Network Trunk Groups (see Network_Trunk_Group ).

Each Trunk Group
                           		contains one or more Trunks. Each trunk belongs to one trunk group.

Statistics

At Five-Minute
                           		intervals status information is produced for each 
                           		Routing Client (see Routing_Client ).

Statistics are
                           		produced for each Trunk Group in Real-Time, at Five-Minute intervals, and every
                           		Half-hour. Statistics are also produced for each Network Trunk Group in
                           		Real-Time and at Half-hour intervals.

Each Peripheral can
                           		have a 
                           		Default Route (see Route ) that is
                           		used to account for calls at the peripheral that are not associated with any
                           		other route.

Real-time statistics
                           		are generated for each Peripheral.

For some peripheral
                           		types, you must specify what entities to collect data for by including them in
                           		the 
                           		Peripheral Monitor (see Peripheral_Monitor ).

Multiple PIM Types

The Unified ICM PG can
                           		support multiple device types (for example, ACDs and VRUs). Each device type
                           		requires a separate Peripheral Interface Manager (PIM). In cases where ACD and
                           		VRU PIMs are controlled by the same PG, you must specify how VRU ports map to
                           		ACD ports or trunks.

Service Level Threshold

The 
                           		Service Level
                           		  Threshold (see Service_Level_Threshold ) contains information on how the system software calculates the
                           		service level. Each row defines the service level threshold default values for
                           		a particular Peripheral-Media Routing Domain pair.

## Enterprise Tables

To see an
                           illustration and a list of the Enterprise tables, see Enterprise .

Each Route (see Route ) can belong to one
                           or more Enterprise Routes (see Enterprise_Route ).

The
                           Enterprise Route Member (see Enterprise_Route_Member ) maps Routes to Enterprise Routes.

Each
                           Skill Group (see Skill_Group )
                           can belong to one or more Enterprise Skill Groups (see Enterprise_Skill_Group ).

The Enterprise Skill Group Member (see Enterprise_Skill_Group_Member ) maps Skill Groups to
                           Enterprise Skill Groups.

Each
                           Service (see Service ) can
                           belong to one or more Enterprise Services (see Enterprise_Service ).

The
                           Enterprise Service Member (see Enterprise_Service_Member ) maps services to enterprise services.

Each Peripheral Gateway (PG) can have one or more associated
                           Service Arrays (see Service_Array ).

Each
                           Service Array (see ) Service_Array contains one or more Services (see Service ); but all
                           services in an array must be from peripherals associated with the same PG.

The Service Array Member (see Service_Array_Member ) maps
                           Services (see Service ) to
                           Service Arrays.

## Media Routing Tables

To see an illustration and a list of the
                           Media Routing tables, see Media Routing .

Application_Instance contains configuration data about external
                           application instances. The data in this table enables the system software to
                           identify application instances and grant them access to the Configuration
                           Management Service (CMS).

Application_Path defines a path from a registered application instances
                           to a CTI Server. Applications need an interface to CTI Server in order to
                           report logins, agent states, and task messages to the system software.

Application_Path_Real_Time provides real-time status and connection data for
                           application paths.

Application_Path_Member defines the Media Routing Domains (MRDs) that use a
                           particular application path.

Media Class is a combination or single instance of physical media that are to be treated as
                           a single concept by Unified ICM/Unified CCE software.

Media_Class defines a type of media class. This table is populated initially with
                           default media classes.

Media Routing
                              Domain (MRD) is a collection of skill groups and services that are
                           associated with a common communication medium.

Media_Routing_Domain describes a single implementation of a media class.
                           For example, a media class such as Cisco single-session chat might have one or
                           more Media Routing Domains (MRDs) defined. These MRDs would all be of the same
                           media class. However, they might be on different servers or handle slightly
                           different types of requests.

## Route Tables

To see an illustration
                           		and a list of all tables in the Route category, see Route .

Unified ICM/Unified
                           		CCE selects a 
                           		Route (see Route ) for each call.
                           		The route specifies a service for the call and a skill target to handle the
                           		call. A skill target is a service, skill group, agent, or translation route.

The 
                           		Network Target (see Network_Target )
                           		specifies a destination for a call. A network target can be an 
                           		Announcement (see Announcement ), a 
                           		Peripheral Target (see Peripheral_Target ) or a
                           		
                           		Scheduled Target (see Scheduled_Target ). A
                           		peripheral target is a trunk group on which to deliver the call and a DNIS
                           		value to send with it. A scheduled target is a destination for which the
                           		Unified ICM/Unified CCE knows only the number of scheduled resources and the
                           		number of calls in progress. For each scheduled target, the Unified ICM/Unified
                           		CCE maintains Scheduled Target Real Time data.

The routing client
                           		presents the Unified ICM/Unified CCE with a 
                           		Dialed Number (see Dialed_Number ). A
                           		dialed number can be an 800 number such as 800-555-1234, or a string such as
                           		"RTE.007." Each Dialed Number can have a default route.

A route is associated
                           		with one or more Network Targets. The network target has one or more associated
                           		Labels. A label is the string that is passed back to the network to indicate
                           		the appropriate target. The 
                           		Dialed Number Label (see Dialed_Number_Label )
                           		indicates which labels are valid for each dialed number (or you can choose to
                           		make all labels valid for a routing client valid for all of that routing
                           		client's dialed numbers).

For each route,
                           		statistics are produced in Real Time, every Five Minutes, and every Half-hour.

A 
                           		Route Call Detail (see Route_Call_Detail )
                           		record is produced immediately after the Unified ICM/Unified CCE determines a
                           		route. This records information about the request and the route determined by
                           		the Unified ICM/Unified CCE.

A 
                           		Termination Call
                           		  Detail (see Termination_Call_Detail ) record is produced at the end of each call. Data for this record
                           		comes from the Peripheral Gateway . It provides information about how the call
                           		was handled at the peripheral. The Route Call Detail and Termination Call
                           		Detail are linked by the Day and RouterCallKey fields.

A script may direct a call to a Network VRU (see Network_Vru ) associated with the routing client. The script returns a label to the routing client. It may also specify a Network Vru
                           Script (see Network_Vru_Script ) to be run by the VRU.

## Schedule Tables

To see an illustration and a list of all tables in
                           the Schedule category, see Schedule .

With the
                           optional Schedule Import feature, you can import schedules for each agent,
                           skill group, and service from a workforce management system.

Schedule contains one entry for each schedule.

Schedule_Import contains the actual scheduling data for various time
                           periods. Schedule_Import_Real_Time contains the scheduling data that is
                           currently in effect.

Schedule_Source indicates where the data are imported from. Schedule_Map gives the primary key value for the scheduling data in the source.

ICR_View indicates how the Schedule Import records for a
                           schedule are to be interpreted.

View_Column indicates how to interpret each field in Schedule Import

Import_Schedule defines import processes to be run automatically at
                           specified times.

Import_Log contains information about these import processes.

A schedule
                           may recur daily, weekly, monthly, etc. The Recurring Schedule Map describes a
                           recurrence pattern for a schedule.

## Script Tables

To see an illustration and a list of all tables in the
                           Script category, see Script .

The
                           Unified ICM/Unified CCE classifies each incoming call into a
                           Call Type (see Call_Type )
                           based on a Dialed Number Map (see Dialed_Number_Map ). The mapping considers the dialed number, caller-entered
                           digits, and calling line ID. The calling line ID can be specified as a specific
                           number, a wildcard, or a Region (see Region ) composed of
                           Prefixes. Each routing client may have a
                           Default Call Type (see Default_Call_Type ).

A script is a series of steps performed to determine the best route for a call or to perform periodic administrative actions.
                           You can create several versions of each script. General information about each script is stored in the Master Script (see Master_Script ). Specific information about each version is stored in the Script (see Script ). The binary representation of the script version is stored in the Script Data (see Script_Data ) table. Each Script version has a Cross Reference for each database entity that it references.

A
                           Call Type Map (see Call_Type_Map )
                           associates one or more routing scripts to the call type based on a schedule of
                           when each script is active. An
                           Admin Script Schedule Map (see Admin_Script_Schedule_Map ) schedules a periodic administrative script. For each script
                           version, Real Time and Five-Minute data are produced. Also, Real-Time data are
                           produced for each call type.

You can define
                           User Variables (see User_Variable ) that you can set and reference in scripts. Optionally,
                           you can define Persistent Variables (see Persistent_Variable ) that retain their values between script invocations. You
                           can also define custom functions that are stored as
                           User Formulas (see User_Formula ). The expression associated with a custom function is
                           stored in User Formula Equation (see User_Formula_Equation ).

With the optional Gateway feature, a script
                           can communicate with an external application. An
                           Application Gateway (see Application_Gateway ) represents such an external application. Each side of the
                           Central Controller can maintain a separate Connection for each Application
                           Gateway. Unified ICM/Unified CCE software also maintains Global default values
                           for Application Gateway connections. Half-hour data are produced for each
                           Application Gateway.

With the optional Gateway SQL feature, a
                           script can query an external database. The tables that can be accessed are
                           stored in Script Table (see Script ) and the specific columns in Script Table Column (see Script_Table_Column ).

The
                           Script Queue Real Time (see Script_Queue_Real_Time ) contains data on how tasks are processed in a script queue.

## Security Tables

To see an illustration and
                           a list of all tables in the Security category, see Security .

You might choose to restrict access to some objects in the Unified
                           ICM/Unified CCE database to specific users, specific groups of users, or to a
                           specific entity (such as a division within a company). The enterprise consists
                           of one or more entities. The
                           Business Entity (see Business_Entity ) defines the entities within an enterprise.

The User Group (see User_Group ) defines groups of users or individual users who have
                           specific access rights. If a row in the User Group table defines a group, each
                           user who is a member of that group is configured in the
                           User Group Member (see User_Group_Member ). Unified ICM/Unified CCE software also uses the
                           Sec Group (see Sec_Group ) and
                           Sec User (see Sec_User ) to track the state of user groups. The
                           User Supervisor Map (see User_Supervisor_Map ) is used to allow an agent to log in as a Supervisor.

The Feature Control Set (see Feature_Control_Set ) defines the different feature sets that may be
                           used by different users. One set of features may be mapped to multiple users.

Each individual item for which the Unified ICM/Unified CCE
                           software controls access is an object. The
                           Object List (see Object_List ) contains information about these objects. The Ids (see Ids )
                           contains information about row-level security for objects. The
                           Object Security (see Object_Security ) defines the access that specific user groups have
                           for specific objects.

The
                           User Security Control (see User_Security_Control ) defines the access that specific users have for
                           specific objects. The possible access levels for each object are defined in the
                           Object Access Xref (see Object_Access_Xref ). The Unified ICM/Unified CCE software uses the
                           Group Security Control as an intermediate table to build User Security
                           Control records.

A category of objects on which access is
                           controlled is a class. The Class List (see Class_List ) defines
                           these categories. The Class Security (see Class_Security )
                           specifies the level of access a user group has to a specific class. The access
                           levels that are available for a class are specified in the
                           Class Access Xref (see Class_Access_Xref ).

The
                           ClassID To ObjectType (see ClassID_To_ObjectType ) defines the mapping of classes to
                           objects.

## Skill Target
                        	 Tables

To see an illustration
                           		and a list of the Skill Target tables, see Skill Target .

Peripheral Targets

Each peripheral can
                           		have many 
                           		Services (see Service ), Agents,
                           		Skill Groups, and Translation Routes (see Translation_Route ).
                           		These entities are collectively known as 
                           		Skill Targets (see Skill_Target ).

Each agent can be
                           		assigned to an 
                           		team of agents (see Agent_Team ).
                           		Teams are for monitoring purposes only; they are not used for routing calls.
                           		The 
                           		Agent Team Member (see Agent_Team_Member ) maps
                           		agents to teams.

The 
                           		Agent Team Supervisor (see Agent_Team_Supervisor )
                           		is a configuration table that specifies the mapping of supervisors to agent
                           		teams.

For agents that are
                           		not associated with an ACD, you can define 
                           		Agent Desk Settings (see Agent_Desk_Settings ),
                           		which specify features available and how the Unified ICM handles certain state
                           		changes for an agent.

A 
                           		Person (see Person ) record provides
                           		primary identification and authentication for all system users, including both
                           		agents and administrators.

Each service has one
                           		or more associated skill groups. Each skill group can be associated with one or
                           		more service. The 
                           		Service Member (see Service_Member ) maps
                           		skill groups to services.

Each Skill Group has
                           		one or more member agents. Each agent can be associated with one or more skill
                           		groups. The 
                           		Skill Group Member (see Skill_Group_Member )
                           		maps agents to skill groups.

For some peripherals,
                           		a base Skill Group can have multiple related Skill Groups with different
                           		priorities.

Statistics

Real-Time statistics
                           		are produced for each 
                           		Agent (see Agent ), 
                           		Skill Group (see Skill_Group ), 
                           		Service (see Service , and each 
                           		Skill Group Member (see Skill_Group_Member ).

At Five-Minute
                           		intervals statistics are produced for each 
                           		Skill Group (see Skill_Group ) and Service (see Service ).

Every Half-hour,
                           		statistics are produced for each 
                           		Skill Group (see Skill_Group ), 
                           		Service (see Service ), and 
                           		Translation Route (see Translation_Route ).

For each agent, the
                           		Unified ICM/Unified CCE software maintains a State Trace, which tracks the
                           		states an agent has been in. When an agent logs out, the Unified ICM/Unified
                           		CCE software creates an 
                           		Agent Logout record (see Agent_Logout ).

## System
                        	 Tables

To see an illustration
                           		and a list of the System tables, see System .

Application_Event contains information about application events generated by the Unified
                           		ICM/Unified CCE software. This is a subset of the events reported in the Event
                           		table.

AWControl maintains information about the Admin Workstation and its local database.

Config_Message_Log contains database system information.

Controller_Time contains the current time as kept by the Central Controller.

Event contains information about system events generated by the Unified ICM/Unified
                           		CCE software.

ICR_Globals contains some general information about the system.

ICR_Locks contains a row for each database lock currently held.

Logger_Admin maintains information about scheduled administration jobs run on the central
                           		database by the Unified ICM/Unified CCE software.

Logger_Meters contains performance information about the Logger process.

Logger_Type specifies the type of Logger (that is, standard, Customer ICM (CICM)) , or Network Applications Manager (NAM) and, if the
                           Logger is a NAM Logger, whether or not the NAM is a secondary NAM.

Next_Available_Number identifies the next available unique integer ID value for a specific database
                           		table.

Recovery contains internal status about each table in the database.

Region_Info specifies which prefixes and regions are pre-defined by the Unified ICM/Unified
                           		CCE software.

Rename is an internal table.

Version records the current versions of the Unified ICM/Unified CCE schema installed in
                           		the central and local databases.

## User Preferences Tables

To see an illustration and a list of the
                           User Preferences tables, see User Preferences .

Tables in the User Preferences
                           group are used to create custom tool sets and desktop appearances for users of
                           the system software.

The "Cfg" tables control the desktop
                           settings, or appearance, of Configuration Manager tool, which allows users to
                           define desktop settings, and to view, edit, or delete the records of existing
                           desktop settings.

Cfg_Mngr_App_Snapshot_State defines a specific state of the Unified ICM
                           Configuration Manager that a user has saved. Information from this table is
                           used to reconstruct the Unified ICM Configuration Manager state when the
                           Administration & DataServer is restarted.

Cfg_Mngr_User_Desktop_Snap retains information on the current Configuration
                           Manager state for a particular user.

Cfg_Mngr_User_Menu holds information that describes the default and custom
                           menus in use for each user of the Configuration Manager.

Cfg_Mngr_View holds the information necessary to produce the tree view structure for
                           multiple default and custom menus within the Unified ICM Configuration Manager.

Cfg_Mngr_User_Settings holds specific Unified ICM Configuration
                           Manager settings for each user of the Configuration Manager tool. Each row in
                           this table specifies the personal settings for one user (for example, whether
                           or not the user want to save the Configuration Manager desktop settings in
                           place when Configuration Manager is closed).

Cfg_Mngr_Globals contains a single record that stores version information about the menu system
                           that Unified ICM Configuration Manager is currently using.

## VRU Micro-applications Tables

To see an
                           illustration and a list of the VRU Micro-Applications tables, see VRU Micro-application .

Vru_Currency contains a list of currencies supported by VRU
                           micro-applications.

Vru_Defaults contains a single row of data that contains the default values for a
                           particular VRU micro-application.

Vru_Locale contains a list of locales (a locale is a combination of language and
                           country) supported by VRU micro-applications.

### Customers Also Viewed

- Database Schema Handbook for Cisco Unified ICM/Contact Center Enterprise, Release 12.6(1) --- All Tables