---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-administrat-258e4c99f1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/administration/guide/administration-guide-for-cisco-unified-contact-center-enterprise-release-1262/ucce_m_web-based-cce-administration.html
retrieved_at: 2026-08-16T20:45:35.266104+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise Release, 12.6(2)

# Administration Guide for Cisco Unified Contact Center Enterprise Release, 12.6(2)

Updated: December 3, 2025

Chapter: Web Based CCE Administration

## Chapter: Web Based CCE Administration

# Web Based CCE Administration

## Unified CCE Web Administration

The Configuration Manager enables you to perform most of the Unified CCE administrative tasks. The gadgets in the Unified
                           CCE Web Administration application enables you to manage other Unified CCE administrative tasks and system settings.

For more information on each gadget, please see the online help available in the CCE Web Administration page.

Users are logged out of the Unified CCE Administration console automatically after 30 minutes of inactivity.

### Access Unified CCE Administrative Gadgets

To manage agents, attributes, precision queues, bucket intervals, media routing domains, license, and bulk jobs, use the corresponding card in the Unified CCE Web Administration application. For example, to access business hours :

Step 1

From your desktop, double-click the Unified CCE Tools icon, and then select Administration Tools .

Step 2

Double-click the CCE Web Administration link.

Step 3

From the left navigation bar, select Overview and then select Organization Setup card .

Step 4

Select Business Hours .

### Access Unified CCE System Management Gadgets

To configure system settings such as deployment type and system information, use the Infrastructure Settings card. To configure Single Sign-On (SSO), use the Features card in the Unified CCE Web Administration application. For example, to set the deployment type:

Step 1

From your desktop, double-click the Unified CCE Tools icon, and then select Administration Tools .

Step 2

Double-click the CCE Web Administration link.

Step 3

Select Deployment Settings .

Step 4

On the Deployment Type page, click on deployment type and then select an instance from the drop-down list.

### Contact Center AI Configuration

In the Unified CCE Administration console, the Contact Center AI (CCAI) feature tab allows administrators to associate the
                              CCAI configuration (created in the Control Hub at https://admin.webex.com/ ) with all the call types (global configuration) or with a specific call type. Upon associating a CCAI configuration with
                              the call type, the global configuration (if any) gets overridden for the specific call type.

To access this feature, add Cloud Connect to the inventory and register it in the Unified CCE Administration console.

#### Associate Contact Center AI Configuration with All Call Types

You can view, update, or reset the Contact Center AI configuration, which is associated with all call types.

##### View Contact Center AI Configuration

In the Unified CCE Administration , navigate to Overview > Features > Contact Center AI . The Contact Center AI Configuration search box displays the name of the CCAI configuration that was previously associated with all call types.

##### Update Contact Center AI Configuration

Only one configuration can be associated globally with all call types.

Step 1

In the Unified CCE Administration , navigate to Overview > Features > Contact Center AI .

Step 2

In the Contact Center AI Configuration search box, click the search icon. A pop-up window displays a list of CCAI configurations.

Step 3

Select the required configuration and click Save .

##### Reset Contact Center AI Global Configuration

This procedure explains how to reset the Contact Center AI configuration. Upon reset, the previously associated configuration
                                       is cleared from the search box.

Step 1

In the Unified CCE Administration , navigate to Overview > Features > Contact Center AI .

Step 2

In the Contact Center AI Configuration search box, next to the configuration name, click the x icon.

Step 3

Click Save .

#### Associate Contact Center AI Configuration with a Call Type

You can view, update, or delete the Contact Center AI configuration associated with a specific call type.

##### View Contact Center AI Configuration

In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Type . The Contact Center AI Configuration search box displays the name of the CCAI configuration that was previously associated with the call type.

##### Update Contact Center AI Configuration

This procedure explains how to update the Contact Center AI configuration associated with a call type.

Only one configuration can be associated with a call type.

Step 1

In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings .

Step 2

Click the Contact Center AI tab.

Step 3

In the Contact Center AI Configuration search box, click the search icon. A pop-up window displays a list of CCAI configurations.

Step 4

Select the required configuration and click Save .

##### Reset Contact Center AI Configuration

This procedure explains how to reset the Contact Center AI configuration. Upon reset, the previously associated configuration
                                       with the call type is cleared from the search box.

Step 1

In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings .

Step 2

Click the Call Type tab.

Step 3

In the Contact Center AI Configuration search box, next to the configuration name, click the x icon.

Step 4

Click Save .

### Manage digital channels

To access this feature, ensure that you add Cloud Connect to the inventory in the Unified CCE Administration portal and register
                                          it.

As an administrator, perform the following configurations in the Unified CCE Administration portal to manage digital channel
                              capabilities for your customers to reach business:

Set up media channels such as chat, email, social, voice callback, . See Set up media channels .

Synchronize agents in AW database to Webex Engage database. See Configure User Sync .

Define Expanded Call Context (ECC) variables to assist agents with relevant information. See Define ECC variables .

Integrate Cloud Connect with Webex Connect using the Open Authorization v2.0 (OAuth v2.0) standard. See Integrate Cloud Connect with Webex Connect .

Customize the connection parameters between Cloud Connect and MR PG. See Manage connection between Cloud Connect and MR PG .

#### Set up media channels

Contact Center Enterprise (CCE) supports media channels, such as Live Chat, Email, and SMS, with enhanced capabilities. These
                                    media channels are mapped to media type and Media Routing Domains (MRDs) for providing granular channel-specific reporting
                                    and agent state control. Based on this configuration, Cloud Connect associates the received task request to the appropriate
                                    MRD.

MRDs are used to map agents' skill group with the media channels, based on which the agents are assigned a task. You can map
                                    multiple media channels to the same MRD. For example, you can map SMS and Chat channels to the same MRD. For more information
                                    on MRDs, see the Media Routing Domains section in the Configuration Guide for Cisco Unified ICM Enterprise .

Media type is a broad category of media channels and it is different from the media class or MRD in CCE. The Digital Routing
                                    service has internal sub-limits and different maximum queue time parameters that it applies for tasks of a certain Media Type
                                    as defined by the Queue Settings. The media types are Chat , Email , Telephony (Voice Callback), Social .

Webex Connect offers support for the pre-provisioned system defined media channels. You can add a custom media channel if
                                    one of the many media channels that Webex Connect supports in the future has to be allowed in the CCE system. If not, you
                                    can skip adding a Media Channel.

Queue Settings for media channels is used to configure the maximum queue limit and maximum queue time for each media type, individually.
                                    For more information on configuring queue settings for media channels, see Queue Settings .

To set up media channels:

Step 1

In the Unified CCE Administration portal, navigate to Overview > Digital Channels > Digital Channel Settings > Media Channel . The list of existing media channels is displayed in a grid. This is the default page.

Step 2

Click New . On the New Media Channel page, do the following:

In the Name field, type the name of the media channel.

From the Media Type drop-down list, select the required media type.

In the Media Routing Domain field, search and select the MRD that you want to map to the media channel.

Step 3

Click Save . The channel is added to the list on the Digital Channel Settings page.

When you have created a media channel, you can modify only the Media Routing Domain field. If you want to modify any other fields, you must delete the media channel and create afresh. To delete a media channel,
                                                hover over the media channel and click the X icon.

##### Configure queue settings

The Digital Routing service maintains a queue for all the incoming tasks. The service accommodates up to a maximum of 100,000
                                       tasks in the queue at any given point in time. Out of these 100,000 tasks, you can configure the maximum number of tasks that
                                       can be queued for each media type in the Digital Routing service. The following are the default values in percentage for each
                                       media channel:

Media type

Queue setting in %

Description

Email

50%

50,000 tasks can be queued for Email.

Social

40%

40,000 tasks can be queued for SMS.

Voice callback

5%

5,000 tasks can be queued for Voice callbacks.

Chat

5%

5,000 tasks can be queued for live chat.

You can also define the maximum duration for which a task remains in the queue for each media type.

The following are the scenarios in which the Digital Routing service rejects the tasks and sends them back to Webex Connect:

The number of tasks exceeds the maximum value that is configured for the media channel. For example, consider that the Digital
                                             Routing service queue has 50,000 email tasks, which is the maximum queue setting defined for the Email media channel. If Webex
                                             Connect further injects email tasks, the Digital Routing service rejects the incoming tasks and sends them back to Webex Connect
                                             with an error code of 20286 (MEDIA_TYPE_QUEUE_LIMIT_EXCEEDED). For example, a flow developer can decide to provide appropriate
                                             messaging to the end customer and invoke other backend systems to denote queue capacity issues.

Task exceeds the maximum duration that is defined for the media channel. The Create Task node is successful. There is a Closed
                                             webhook event triggered when the task gets autoclosed after exceeding the maximum time in the queue, with a specific disposition
                                             code set to CD_MAX_DIALOG_LIFETIME_EXCEEDED.

The flow debug logs show the error code returned by the Create Task node API call. For more information about the Create Task
                                       node, see Create Task .

The Digital Routing Service doesn't use the Maximum Queue Time from the MRD to decide if a task should be dropped from the
                                                   queue. Instead, it only considers the Queue Settings for the media type configured in the Unified CCE Administration portal
                                                   as described below. To avoid premature drops, make sure the Max Queue Time configured in the MRD is more than the queue time
                                                   configured in the Unified CCE Administration portal.

To configure the queue settings for the media channels:

Step 1

In the Unified CCE Administration portal, navigate to Overview > Digital Channels > Digital Channel Settings > Media Channel .

Step 2

Click Queue Settings .

Step 3

Enter the required values in percentage for each media channel.

Make sure that the sum of the percentage values configured for all the media channels is 100.

Step 4

Define the duration in days, hours, and minutes for each media channel. This is the maximum duration for which a task that
                                                belongs to the specific media channel remains in the queue after which it gets timed out.

Media Channel

Default Duration

Email

3 days

Social Media

3 days

Voice callback

2 hours

Chat

2 hours

Step 5

Click Save .

### Configure User Sync

To synchronize the CCE agents who are configured for digital channel interactions with Webex Connect:

Step 1

In the Unified CCE Administration portal, navigate to Overview > Digital Channels > Digital Channel Settings > User Sync .

The DataConn service is active only on the publisher node of Cloud Connect. Ensure that the publisher node is accessible for
                                                         you to view the User Sync page.

Step 2

In the Network Entry Point field, enter the hostname or FQDN of the load balancer or the reverse proxy server based on your deployment. It is through
                                          this network entry point that the Webex Engage sends the response request to the DataConn service for agent synchronization.

Step 3

In the AW Database Details area, complete the following fields to configure the DataConn service for the Primary and the Secondary Server:

In the AW Datasource Host field, enter the IP address or the host name of the AW server that has the agent configurations.

In the Port field, enter the SQL port number of the AW database server.

In the Database Name field , enter the name of the AW database server.

In the Database User ID and Password fields, enter the user ID and password of the SQL user account that you created for digital channels.

Step 4

Click Test Connection to make sure that the DataConn service can read the data from the AW Primary server.

Step 5

Switch on the Enable Failover toggle button to enable the failover to the Secondary AW server.

Step 6

To synchronize agents, choose one of the following options:

Enable the Enable Sync toggle button to automatically synchronize agents in an interval of 30 minutes.

Click Sync Now to manually synchronize the agents. This option is available only when the Current Sync Status field appears as Scheduled .

If you recreate your AW Database to fix any errors, ensure that you disable User Sync before starting with the recreation
                                                         process. Enable the User Sync only after the AW Database is created and synchronized with the central controller database.

Step 7

In the Last sync field, view the date, time and status of the previous synchronization.

Step 8

In the Agents Sync Details field, view the number of agents that are synchronized successfully. The number of agents appears as a clickable link. Click
                                          the link to view the list of agent records that have failed to synchronize and the list of agent records that are pending
                                          for synchronization. You can choose to refresh the agent records at any given point in time.

Step 9

In the Current Sync Status field, you can view one of the following statuses:

No sync is in progress or scheduled —This status appears when the Enable Sync toggle button is off.

Scheduled —This status appears when the Enable Sync toggle button is on.

In Progress —This status appears when the scheduled sync or manual sync is in progress.

Manual Sync Failed —This status appears when the manual sync has failed.

Unknown —When sync status is not available.

Step 10

Click Save .

### Define ECC variables

The Expanded Call Context (ECC) variables are data that are embedded within the call and are visible to the agent on the Agent
                                 Desktop. ECC variables are passed back and forth in ECC payloads. ECC variables assist the agent with relevant information
                                 without the customer having to repeat the same information.

To define the ECC variables:

Step 1

In the Unified CCE Administration portal, navigate to Overview > Digital Channels > Digital Channel Settings > ECC Variable .

Step 2

On the ECC Variable page, click the plus icon (+). The Add ECC Variable page appears with existing variables Name and Enabled details. It excludes the built-in variables.

Step 3

Select the required variable. The ECC Variable page displays the newly added ECC variable.

Step 4

Click Save .

### Integrate Cloud Connect with Webex Connect

You can integrate Cloud Connect with Webex Connect using the Open Authorization v2.0 (OAuth v2.0) standard. You must configure
                                 Webex Connect client ID and client secret in the Digital Routing service for the service to gain access to Webex Connect using
                                 the access token. This set of client credentials uniquely identifies the Cloud Connect and its permissions to access Webex
                                 Connect.

The Cloud Connect Management service is active only on the publisher node of Cloud Connect.

To configure client credentials for OAuth v2.0 access token:

Step 1

In the Unified CCE Administration portal, navigate to Overview > Digital Channels > Digital Channel Settings > Integration .

Step 2

On the OAuth2 Authentication Details page, perform the following steps.

In the Name field, enter a name for the Cloud Connect integration. This field is editable.

In the Description field, enter a description of what the client application does.

In the Client Id and Client Secret fields, enter the client id and secret key that you can retrieve from the Webex Connect portal (navigate to Assets > Integrations > CCE pre-built integrations > Actions > Manage ).

In the  field, enter the password that is provided to you at the time of registration. This is the secret key that was used
                                                for generating the token.

From the Method drop-down list, select the POST method for Webex Connect integration.

From the Content Type drop-down list, select a media content type. This determines the response format. The available options are application/json , application/xml , and application/x-www-form-urlencoded . For Webex Connect integration, select application/x-www-form-urlencoded .

In the Access Token JSON path , enter the path in the JSON response to fetch the value of the access token. For the Webex Connect integration, enter access_token .

(Optional) In the Header List section, click + icon to add a header name and value and click Add . The header name and value are used to pass any additional information that Webex Connect may require for Cloud Connect integration.

Step 3

Click Save to save the OAuth2 authentication details.

Step 4

Go to the Webhook tab to register the Webhook URL in the Digital Routing service. To fetch the Webhook URL:

In the Webex Connect portal, navigate to Assets > Integrations .

In the CCE pre-built integrations row, from the Actions column, select Manage . The Manage Integration - Prebuilt Integration page appears.

In the Inbound Events section, copy the Webhook URL.

Step 5

Paste the URL in the Webhook URL field in the Unified CCE Administration portal ( Overview > Digital Channels > Digital Channel Settings > Integration > Webhook ).

### Manage connection between Cloud Connect and MR PG

To customize the connection parameters between Cloud Connect and Media Routing Peripheral Gateway (MR PG):

Step 1

In the Unified CCE Administration portal, navigate to Overview > Digital Channels > Digital Channel Settings > Advanced Settings .

Step 2

The Port is a display-only field and the default value is 38001 . It is through this port that Cloud Connect and MR PG communicates with each other.

Step 3

The Secured toggle switch is turned on by default. It is to establish a secured connection between Cloud Connect and MR PG. You can turn-off
                                          this toggle switch to disable the secure connection.

Step 4

Click Save .

### Contact Center AI Services

Administrators and supervisors can enable or disable Contact Center AI services such as Agent Answers , VAV Transcript, and Call Transcript for each agent or multiple agents together.

#### Enable or Disable Contact Center AI Services for an Agent

Step 1

In Unified CCE Administration , choose Users > Agents .

Step 2

Click on the agent row whose services are to be modified.

Step 3

Click the Contact Center AI tab.

Step 4

To enable or disable the required Contact Center AI Services , check or uncheck the check boxes corresponding to the services.

Step 5

Click Save .

#### Enable or Disable Contact Center AI Services for Multiple Agents

All agents must belong to the same site and the same department, or all agents must be global agents. The Edit button is disabled if:

Agents from different sites , departments, or peripheral sets are selected.

A mix of global and departmental agents are selected.

Step 1

In Unified CCE Administration , choose Users > Agents .

Step 2

Check the check box corresponding to each agent whose services you want to edit.

Step 3

Click Edit > Contact Center AI .

If the service is enabled for all the agents selected for editing, the check box is checked.

If the service is disabled for all the agents selected for editing, the check box is unchecked.

If the service is enabled for some agents and disabled for the others, the check box has a dash (—).

Step 4

To enable or disable the Contact Center AI Services , check or uncheck the check boxes corresponding to the services.

Step 5

Click Save , and then click Yes to confirm the changes.

#### Enable or Disable Answers Contact Center AI Services for Agents using Bulk Job

Step 1

Navigate to Unified CCE Administration > Overview > Bulk Import .

Step 2

Click Templates .

The Download Templates popup window opens.

Step 3

Click the Download icon for the Contact Center AI template you want to use.

Step 4

Click OK to close the Download Templates popup window.

Step 5

Open the .csv template in Microsoft Excel.

Step 6

Populate the file as described in the Bulk Contact Center AI Services Content File .

Step 7

Save the populated file to the local machine.

Step 8

Navigate to Unified CCE Administration > Overview > Bulk Import .

Step 9

Click New .

Step 10

In the optional Description field, enter up to 255 characters to describe the bulk job.

Step 11

In the Content file field, choose the file to upload, and then click Save .

## Managing
                        	 Agents

The Agents tool in
                           		Unified CCE Administration contains a list of agents. These agents are created
                           		in Agent
                              		  Explorer under Configuration Manager .

Rows in the list
                           		show the following fields for each agent:

Username

Peripheral

Last Name

First Name

Description

The username maps to
                           		the login name in Agent
                              		  Explorer .

Contact Center AI service Contact Center AI Services can be enabled or disabled for each agent or for multiple agents together. For more information, see Contact Center AI Services .

You cannot create
                           		or delete agents in this tool. You must create or delete agents in the Configuration Manager Agent Explorer tool.

Ensure that Agent ID (Peripheral number) and agent Login name is unique for each user.

## Attributes

Attributes identify a call routing
                           requirement, such as language, location, or agent expertise.

You can create two types of attributes:

Boolean

Proficiency

Use
                           Boolean attributes to identify an agent attribute value as true or false .

For example, you can create a Boston attribute. This attribute specifies that the agent assigned to this attribute must be located
                           in Boston. An agent in Boston would have Boston as True as the term
                           for that attribute.

Use Proficiency attributes to establish a level of expertise in a range from 1 to 10 , with 10 being the highest level of expertise.

For example, for a Spanish language attribute, an original speaker would have the attribute Proficiency as 10 . When you create a precision queue, you identify which attributes are part of that queue and then implement the queue in
                              a script.

When you assign a new attribute to an agent and the attribute value matches the precision queue criteria, the agent is automatically
                              associated with the precision queue.

Attributes is a prerequisite for Precision Queue.

## Precision
                        	 Queues

## Managing Bucket
                        	 Intervals

Configure bucket
                           		intervals to report on how many calls are handled or abandoned during specific,
                           		incremental time slots.

Each bucket interval
                           		has a maximum of nine configurable time slots, called Upper Bounds. Upper
                           		Bounds are ranges measured in seconds to segment and capture call-handling
                           		activity. You can run reports that show calls answered and calls abandoned for
                           		these intervals.

If your goal is
                              		  to have calls handled within 1 minute, you might set up Upper
                                 			 Bounds for intervals that show how many calls are handled in less
                              		  than or more than 1 minute. Intervals might be for 30, 60, 80,120, 150, 180,
                              		  and 240 seconds. Using these intervals, you can see if calls are being answered
                              		  within 1 minute or if callers are waiting longer.

The intervals also
                              		  give you insight into how long callers are willing to wait before cancelling a
                              		  call. Perhaps many callers do not abandon a call until they have waited for two
                              		  minutes. This might indicate that you can modify your goal.

You can associate
                           		bucket intervals with call types, skill groups, and precision queues. The
                           		system automatically creates a built-in bucket interval, which you cannot edit
                           		or delete.

## Media Routing Domains

Media Routing Domains (MRDs)
                           organize how requests for each communication medium, such as voice
                           and email, are routed to agents.

An agent can handle requests from
                           multiple MRDs.

For example, an agent can belong to a skill group in
                           an MRD for email and to a skill group in an MRD for voice calls.
                           Configure at least one MRD for each communication medium your
                           system supports. You do not need to configure an MRD for voice; the
                           Cisco_Voice MRD is built in. You can add and update only
                           Multichannel MRDs using the Unified CCE Administration Media
                           Routing Domain tool.

To add or update
                                       Multichannel MRDs for Enterprise Chat and Email, use the
                                       Configuration Manager Media Routing Domain List tool.

## Manage Bulk Jobs

Bulk jobs are a fast and efficient way to migrate existing agent and supervisor to single sign-on accounts. You can enable or disable Contact Center AI services for the agents using Bulk jobs (see Enable or Disable AnswersContact Center AI Services for Agents using Bulk Job ).

Do not run bulk jobs during heavy call
                                       load.

Supervisors have no access to the
                                       Bulk Jobs tool.

### Bulk Contact Center AI Services Content File

The content file for Contact Center AI bulk job contains the fields given in the following table. Enter the values appropriately in the given fields to enable or
                              disable Contact Center AI Services for the agents.

Field

Required?

Description

agentId

Agent ID or Username

Existing agentId for which you want to enable or disable the Contact Center AI Services .

You must provide either an agentId or the userName. If both are provided, agentId takes precedence over the userName. If the
                                          agentId value is left blank, the userName will reference an existing agent.

userName

Username of the agent for which you want to enable or disable the Contact Center AI Services .

If no agent is found with the given username, the Contact Center AI Services association fails.

agentServices

Yes (to enable Contact Center AI Services )

The type of Contact Center AI Services to be associated with the agent. Supported values are AgentAnswers , VAV Transcript, and Transcript. To associate more than one services, seperate the values using semicolon (;).

If the value is updated, any existing enabled service gets overwritten. If the value is left empty, no service gets associated
                                          with the agent.

## Deployment
                        	 Type

The deployment type you select, significantly impacts the call processing capacity, configuration limits, and access to features
                           and configuration tools. The configuration steps vary for every deployment type.

You can select any one of the following deployment types:

Packaged CCE Deployment types:

Packaged CCE: Lab Mode

Packaged CCE:2000 Agents

Packaged CCE: 4000 Agents

Packaged CCE: 12000 Agents

Unified CCE deployment types:

UCCE: Progger (Lab Only)

ICM Rogger (Non-Reference Design)

ICM Router/Logger (Non-Reference Design)

UCCE: 8000 Agents Router/Logger (Non-Reference Design)

UCCE: 2000 Agents

UCCE: 4000 Agents Rogger

UCCE: 12000 Agents Router/Logger

UCCE: 24000 Agents Router/Logger

Contact Director

For information on using the gadget after you select a deployment type, see the Cisco Unified Contact Center Enterprise Developer Reference Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-programming-reference-guides-list.html and the online help.

## Auto Discovery

Sample

## Settings

The system can support a defined
                           call capacity based on deployment model. Exceeding the supported
                           rate of incoming calls degrades performance and can result in late
                           calls, dropped calls, delivery of new incoming calls, the time out
                           of requests, and potential system failures. (Call transfers are
                           permitted.)

The System Information tool
                           enforces limits to protect against overloading the system and
                           establishes continuous monitoring of the incoming call rate
                           according to the configured settings.

## Single Sign-On (SSO)

The  Single sign-on (SSO) is an
                           authentication and authorization process. Authentication proves
                           you are the user you say that you are, and authorization verifies
                           that you are allowed to do what you are trying to do.

SSO allows
                           users to sign in to one application and then securely access other
                           authorized applications without a prompt to provide the user
                           credentials once again. SSO permits Cisco supervisors or agents to sign on
                           only once with a username and password to gain access to all of
                           their Cisco browser-based applications and services within a single
                           browser instance.

By using SSO, Cisco administrators can manage all
                           users from a common user directory and enforce password policies
                           for all users consistently.

SSO is an optional feature. If you
                           are using SSO, use the Single Sign-On tool to configure the Cisco
                           Identity Service (IdS). You can then register and test components
                           with the IdS, and set the SSO mode on components.

## Business Hours

Business hours are the working hours during which you conduct business. You can create and modify business hours and set weekly
                           and daily schedules for each business hour. You can create different business hour schedules for regular working days and
                           holidays. You can also open or close the business hours if there is an emergency.

You can define the status reasons for business hours and assign codes for each status reason. Status reason is required when
                           you force open or force close a business hour, and when you add special hours and holidays.

### Add and Maintain Business Hours

Step 1

In Unified CCE Administration , choose Organization > Business Hours .

Step 2

On the Business Hours page, click New to open the New Business Hours page.

Step 3

Complete the following information on the General tab and click Save .

Status

-

Select one of the following statuses for the business hour:

Open/Closed as per Business Calendar

Force Open

Force Close

Status Reason

Yes, if the status is Force Open or Force Close.

This field is enabled only if the status is Force Open or Force Close. Search and select a status reason for the business
                                                         hour.

Name

Yes

Enter a unique name for the business hour. Maximum length is 32 characters. Valid characters are alphanumeric, period (.),
                                                         and underscore (_). The first character must be alphanumeric.

Description

No

Enter a description of the business hour.

Time Zone

Yes

Select a time zone of the business hour from the drop-down list.

Department

-

Search and select a department to associate with the business hour. Default is Global.

This is applicable for Packaged CCE deployment only.

Step 4

Click the Regular Hours tab and complete the following information:

Select one of the following Business Hour Type :

24x7 : Always open. You cannot customize the working hours.

Custom : You can customize the working hours.

If you select Custom , enable at least one business day and select the Start Time and End Time .

Step 5

Click the Special Hours & Holiday tab. You can either add or import special hours and holidays.

Step 6

Click Add to open the Add Special Hours & Holiday popup window. Complete the following information:

Date

Yes

Select a date from the calendar.

Description

No

Enter a description for the special hour.

Status

-

Select a status.

If the status is Open , the Start Time and End Time fields are enabled.

Start Time

Yes, if status is Open.

Select a start time for the special hour.

End Time

Yes, if status is Open.

Select an end time for the special hour.

Duration

-

Displays the duration of the special hour.

Status Reason

Yes

Search and select a status reason.

Step 7

Click Save to add the special hours and holidays.

Step 8

To import special hours and holidays, follow these steps.

Click Import to open the Import Special Hours and Holidays pop-up window.

Click the download icon to download the Special Hours & Holidays template. Use this template to enter the special hours and
                                                holidays.

Click Choose File and browse to the special hours and holidays file. Click Import to upload the file.

The file must contain at least one special hour and holiday.

The file must be in CSV format with a file extension as .txt or .csv.

Step 9

Click Export to download the special hours and holidays in .csv format.

Step 10

Click Save .

The imported business hours overwrites the existing ones.

### Add Business Hours by Copying an Existing Business Hour Record

Step 1

In Unified CCE Administration , choose Organization > Business Hours .

Step 2

Click the Business Hour you want to copy, and then click the Copy button in the Edit <Business Hour> page.

Step 3

Enter Name and Description for the Business Hour.

Step 4

Review the rest of the fields on the General , Regular Hours , and Special Hours & Holiday tabs that were copied from the original Business Hour record, and make any necessary changes.

Step 5

Click Save to return to the List window.

### Add Status Reasons

This procedure explains how to add and maintain status reasons for business hours.

Step 1

In Unified CCE Administration , choose Organization > Business Hours > Status Reasons .

Step 2

Click Add to open the Add Status Reason popup window.

Step 3

Enter the Status Reason. Maximum length is 255 characters.

Step 4

Enter a unique Reason Code. Range is 1001 to 65535. Codes 1 to 1000 are reserved as system-defined reason codes.

Step 5

Click Save .

To add more status reasons, repeat steps from 2 to 5.

Step 6

Click Done to return to the List window.

### Edit Status for Multiple Business Hours

Step 1

On the Business Hours page, select two or more business hours to edit.

Step 2

Choose Edit > Status to open the Edit Business Hours page.

Step 3

Check the Status check box and select the required status.

Step 4

If you select the status as Force Open or Force Close , search and select a Status Reason .

Step 5

Click Save .

### Edit Schedule for Multiple Business Hours

Step 1

On the Business Hours page, select two or more business hours to edit.

Step 2

Choose Edit > Schedule to open the Edit Business Hours page.

Step 3

Check the Time Zone check box and the select the required time zone from the drop-down list.

Step 4

Check the Type check box and select the required business hour type.

Step 5

If you select Custom , enable atleast one business day and select the Start Time and End Time .

Step 6

Click Save .

### Configure Yearly Schedules

You can configure and maintain Business Hour schedules for the whole year.

Step 1

Configure the regular working hours for weekdays.

Step 2

Configure Special Hours & Holidays schedules for whole year by doing the following:

Add the Special Hours & Holidays details for all the special hours and holidays for the whole year into the CSV template file.

On the Import Special Hours & Holidays page, click Choose File and browse to the special hours and holidays file.

Click Import to upload the file.

After you import the configuration file, the BH configurations are loaded on the Business Hours page. Validate the configurations.

Click Save .

When you update the configured Business Hours, remove any elapsed schedules and then update the new schedules for any new
                                                         special hours or holidays in a Business Hour configuration.

## Cloud Connect Administration

Cloud Connect is a component that hosts services that allow customers to use cloud capabilities such as Cisco Webex Experience Management , VAV Transcript , Agent Answers, Call Transcription, Digital Channel, and CCE Orchestration.

### Cloud Connect Integration

Step 1

In Unified CCE Administration , choose Overview > Features > Cloud Connect Integration .

Step 2

On Cloud Connect Integration page, registration
                                          information is displayed. To register or deregister click Cisco
                                             Webex .

Field

Required?

Description

Registration

-

Cloud Connect registration status of Control Hub will be
                                                         displayed.

Cisco Webex

-

On Cloud Connect Integration , if you click the Cisco Webex link, you will be
                                                         re-directed to Cisco Webex login page.

Proxy Details

NO

Enter the proxy details used by the Cloud Connect.

For example: abc.cisco.com:8080

By default, HTTP uses the port 80, but you can
                                                                     specify a different port number in the proxy.

Deployment ID

-

Read-only field that displays the Deployment ID, an
                                                         auto-generated identifier of the Unified CCE
                                                         instance.

Deployment Name

NO

Enter a valid deployment name.

### Initial Configuration for Cloud Connect

For more information, see the section Certificates for CCE Web Administration at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

In the Add Machine dialog box:

Select Cloud Connect Publisher from the Type list.

Enter Hostname or IP Address of the Cloud Connect Publisher Node.

Enter Username and Password for your Cloud Connect cluster Administrator.

Click Save .

#### Edit Cloud Connect Configuration

Step 1

In the Unified CCE Administration, navigate to Overview > Infrastructure Settings , click Inventory .

Step 2

Click the Cloud Connector Publisher device to open the Edit window.

If you edit the Cloud Connect Publisher, the Cloud Connect Subscriber associated with the publisher is updated automatically.
                                                            You cannot edit Cloud Connect Subscriber from the Inventory page.

Step 3

Edit the Username and Password for your Cloud Connect cluster Administrator.

Step 4

Click Save .

##### Monitor Server Status Rules

In CCE deployments, the Unified CCE Administration page displays the total number of alerts for machines with validation rules.
                                    Click the alert count to view the list of all alerts for each machine. Upon clicking Alerts for the respective machine, you
                                    can view the details of the alerts grouped by the following categories:

Configuration

Rules for installation and configuration of a component.

These rules identify problems with mismatched configuration between components, missing services, and incorrectly configured
                                                services.

Cloud Connect: The status and alerts will appear only if the Cloud Connect is added to the Inventory.

For example:Webex Experience Management service must be reachable on the network

When the machine status is out of sync, every 10mins auto sync will be triggered to synchronize the machine configuration.

Operation

Rules for the runtime status of a component.

These rules identify services and processes that cannot be reached, are not running, or are not in the expected state.

#### Delete Cloud Connect Configuration

Step 1

Navigate to Unified CCE Administration > Infrastructure Settings > Inventory .

Step 2

Hover over the Cloud Connect Publisher device and click the x icon.

Step 3

Click Yes to confirm the deletion.

If you delete the Cloud Connect Publisher, the Cloud Connect Subscriber associated with the publisher is deleted automatically.
                                                            You cannot delete Cloud Connect Subscriber from the Inventory page.

#### Delete Cloud Connect Subscriber

This section describes how to delete the Cloud Connect subscriber configuration. You
                                    cannot delete the publisher node; but you can delete the subscriber node.

Step 1

Run the unset cloudconnect subscriber command.

The command removes the Cloud Connect subscriber node configuration from the
                                                cluster. For more information, see Cloud Connect CLI Command in the Cisco Unified Contact Center Enterprise Installation and Upgrade
                                                   Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

Step 2

Power off the subscriber node.

When a subscriber node is removed from a cluster, its certificates still
                                                            exist in the publisher node. The administrator must manually remove the
                                                            following:

The certificate of the subscriber node from the trust-store of
                                                                  the publisher node.

The certificates of the publisher from the trust-store of the
                                                                  removed subscriber node.

Step 3

Run the utils system restart command to restart the
                                             publisher node.

### Provision Experience Management Service on Cloud Connect

Before provisioning Experience Management service on Cloud Connect, ensure to setup and enable Cloud Connect. For more information, see the Cloud Connect Administration section in Administration Guide for Cisco Unified Contact Center Enterprise

Provision Experience Management service using the following CLI on Cloud Connect.

```
set cloudconnect cherrypoint config
```

For more commands related to Experience Management service, see the Cloud Connect CLI section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

The partner hosted module which is a part of Experience Management Invitations solution is required to send surveys to customers
                              over emails and SMS.

For information about Partner Hosted Module Architecture refer to https://xm.webex.com/docs/cxsetup/guides/partnerarchitecture/

For information about how to provision the infrastructure required to deploy the partner hosted
                              components of the Experience Management Invitations module, see https://xm.webex.com/docs/cxsetup/guides/partnerinfra/ .

For information about how to deploy the partner hosted components on the Experience Management
                              Invitations module once the infrastructure is provisioned, see https://xm.webex.com/docs/cxsetup/guides/partnerdeployment/ .

#### Upload Audio Files for Questions in Experience Management

To upload audio files for the survey questions in Experience Management, follow these steps:

Step 1

Login to Experience Management tool with your admin credentials.

Step 2

In Experience Management tool, navigate to CX Setup > Questionnaire > .

You can select the questionnaire and associate it to the voice survey.

To create or modify questionnaires refer to https://xm.webex.com/docs/cxsetup/questionnaires/ https://xm.webex.com/docs/cxsetup/questionnaires/

Step 3

On the right side of the screen, click IVR button beside the question and upload the audio file.

Step 4

Follow the above steps to upload audio files for more questionnaires.

Experience Management is configured to capture only the complete feedback after the voice calls. If the caller drops the call
                                                            without answering all the questions, the partial feedback is discarded.

#### Configure Expanded Call Variables

Step 1

In the Configuration Manager menu, select Tools > List Tools > Expanded Call Variables List .

Step 2

Click Retrieve to view the list of existing ECC variables.

Step 3

Check if the user.microapp.isPostCallSurvey variable exists. If the variable does not exist, do the following to create a new variable:

Click Add .

In the Attributes tab that appears, enter user.microapp.isPostCallSurvey in the Name field.

Set Max Length to 1.

Check the Enabled check box.

Click Save .

When your CCE routing scripts starts, the Post Call Survey field is enabled by default even if user.microapp.isPostCallSurvey has not yet been set in the script. You can turn off Post Call Survey field in the script by setting user.microapp.isPostCallSurvey to n . You can later enable Post Call Survey in the same path of the script by setting this variable to y .

Step 4

Check if the user.CxSurveyInfo variable exists. If the variable does not exist, do the following to create a new variable:

Click Add .

In the Attributes tab that appears, enter user.CxSurveyInfo in the Name field.

Set the Max Length to 133 for Type 10 VRUs. For all other routing clients, set Max Length to 80.

Check the Enabled check box.

Step 5

Click Save .

The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                            payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice.

Step 6

Populate the POD. ID variable.

Step 7

Restart the active VRU PG (side A or B) to register the new ECC variable.

The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                            of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'.

##### Configure POD.ID

Cisco provided variables are predefined, but for POD.ID, the maximum length should be set to 120.

You can modify the variables only if you have the edit access.

Populate the value in the script with multiple attributes in a key-value pair format. Each key-value pair is seperated with
                                    a semi-colon. The following table displays the supported attributes:

Attribute

Description

Applicable

cc_CustomerId

Unique ID for a customer across multiple channels

Chat and Email surveys for Digital Channels

Email

Email ID of the caller for Email surveys

Email survey for voice channel

Mobile

Phone number for SMS surveys

SMS survey for voice channel

cc_language

Language of the survey

For the list of supported languages, refer to the Webex Experience Management documentation at https://xm.webex.com/docs/user/getting-help/#cloudcherry-language-support

Email, SMS, and Voice surveys for voice channel

Optin

Whether to opt in or opt out of the survey

Email, SMS, and Voice surveys for voice channel

Example: cc_CustomerId=xxx;Email=xx;Mobile=xxx;cc_langauge=xxx;Optin=yes/no

For more information on Expanded Call Context Variables , see the chapter Configure Variables in the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

You can also configure POD.ID from CVP Call Studio. For more information, refer to the topic Configure Call Studio App Data Format in the Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html .

#### Configure Dialed Number and Call Type

Step 1

In Configuration Manager , navigate to Tools > List Tools > DialedNumber/Script Selector List .

Step 2

In DialedNumber/Script Selector List create Incoming Dialed Number and Post Call Survey Dialed Number .

For more information on how to create a PCS Dialed Number, refere to the section Configure ICM for Post Call Survey in Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Step 3

Click Save . You will be re-directed to the Configuration Manager window.

Step 4

In Configuration Manager , navigate to Tools > List Tools > Call Type List .

Step 5

In Call Type List create the Call Type . You should associate to the incoming call script and PCS script.

You should associate the incoming call type with the survey from CCEAdmin.

For more information, refer to the topic Associate Survey to Call Type in Unified CCE Admin .

#### Associate Survey to Call Type in Unified CCE Admin

You can associate the Call Type to the survey only if you have added Cloud Connect in the Inventory page and configured the survey in Webex Experience Management portal.

Only one survey can be associated to a Call Type.

Call Types are created and managed in Configuration Manager tool and the survey is associated using the CCE Admin tool.

Step 1

In Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Types .

The list of all the Call Types are displayed.

For more information on Call Types, refer to the Help in ConfigManager > List Tools > Call Types .

Step 2

Click on the Call Type which you want to associate to the Survey. Associate the survey with the last call type before the call is first connected
                                             to an agent.

Step 3

Select the Enable Experience Management check box to associate the Webex Experience Management survey.

The Experience Management tab is enabled with the following options:

Inline Survey (post-call voice survey)

Deferred Survey (post-call Email and SMS survey)

Step 4

Click on the magnifying glass icon, and the configured surveys will be populated in the pop-up window.

Step 5

Select the survey from the pop-up window and click Save .

| Note | For more information on each gadget, please see the online help available in the CCE Web Administration page. Users are logged out of the Unified CCE Administration console automatically after 30 minutes of inactivity. |
|---|---|

| Step 1 | From your desktop, double-click the Unified CCE Tools icon, and then select Administration Tools . |
|---|---|
| Step 2 | Double-click the CCE Web Administration link. |
| Step 3 | From the left navigation bar, select Overview and then select Organization Setup card . |
| Step 4 | Select Business Hours . Note For more information about business hours, see Business Hours . | Note | For more information about business hours, see Business Hours . |
| Note | For more information about business hours, see Business Hours . |

| Note | For more information about business hours, see Business Hours . |
|---|---|

| Step 1 | From your desktop, double-click the Unified CCE Tools icon, and then select Administration Tools . |
|---|---|
| Step 2 | Double-click the CCE Web Administration link. |
| Step 3 | Select Deployment Settings . |
| Step 4 | On the Deployment Type page, click on deployment type and then select an instance from the drop-down list. Note For more information about deployment type, see Deployment Type . | Note | For more information about deployment type, see Deployment Type . |
| Note | For more information about deployment type, see Deployment Type . |

| Note | For more information about deployment type, see Deployment Type . |
|---|---|

| Note | To access this feature, add Cloud Connect to the inventory and register it in the Unified CCE Administration console. |
|---|---|

| Note | Only one configuration can be associated globally with all call types. |
|---|---|

| Step 1 | In the Unified CCE Administration , navigate to Overview > Features > Contact Center AI . |
|---|---|
| Step 2 | In the Contact Center AI Configuration search box, click the search icon. A pop-up window displays a list of CCAI configurations. |
| Step 3 | Select the required configuration and click Save . |

| Step 1 | In the Unified CCE Administration , navigate to Overview > Features > Contact Center AI . |
|---|---|
| Step 2 | In the Contact Center AI Configuration search box, next to the configuration name, click the x icon. |
| Step 3 | Click Save . |

| Note | Only one configuration can be associated with a call type. |
|---|---|

| Step 1 | In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings . |
|---|---|
| Step 2 | Click the Contact Center AI tab. |
| Step 3 | In the Contact Center AI Configuration search box, click the search icon. A pop-up window displays a list of CCAI configurations. |
| Step 4 | Select the required configuration and click Save . |

| Step 1 | In the Unified CCE Administration , navigate to Overview > Call Settings > Route Settings . |
|---|---|
| Step 2 | Click the Call Type tab. |
| Step 3 | In the Contact Center AI Configuration search box, next to the configuration name, click the x icon. |
| Step 4 | Click Save . |

| Note | To access this feature, ensure that you add Cloud Connect to the inventory in the Unified CCE Administration portal and register
                                          it. |
|---|---|

| Note | System-defined media channels cannot be deleted. |
|---|---|

| Step 1 | In the Unified CCE Administration portal, navigate to Overview > Digital Channels > Digital Channel Settings > Media Channel . The list of existing media channels is displayed in a grid. This is the default page. |
|---|---|
| Step 2 | Click New . On the New Media Channel page, do the following: In the Name field, type the name of the media channel. From the Media Type drop-down list, select the required media type. In the Media Routing Domain field, search and select the MRD that you want to map to the media channel. |
| Step 3 | Click Save . The channel is added to the list on the Digital Channel Settings page. When you have created a media channel, you can modify only the Media Routing Domain field. If you want to modify any other fields, you must delete the media channel and create afresh. To delete a media channel,
                                                hover over the media channel and click the X icon. |

| Media type | Queue setting in % | Description |
|---|---|---|
| Email | 50% | 50,000 tasks can be queued for Email. |
| Social | 40% | 40,000 tasks can be queued for SMS. |
| Voice callback | 5% | 5,000 tasks can be queued for Voice callbacks. |
| Chat | 5% | 5,000 tasks can be queued for live chat. |

| Note | The Digital Routing Service doesn't use the Maximum Queue Time from the MRD to decide if a task should be dropped from the
                                                   queue. Instead, it only considers the Queue Settings for the media type configured in the Unified CCE Administration portal
                                                   as described below. To avoid premature drops, make sure the Max Queue Time configured in the MRD is more than the queue time
                                                   configured in the Unified CCE Administration portal. |
|---|---|

| Step 1 | In the Unified CCE Administration portal, navigate to Overview > Digital Channels > Digital Channel Settings > Media Channel . |
|---|---|
| Step 2 | Click Queue Settings . |
| Step 3 | Enter the required values in percentage for each media channel. Note Make sure that the sum of the percentage values configured for all the media channels is 100. | Note | Make sure that the sum of the percentage values configured for all the media channels is 100. |
| Note | Make sure that the sum of the percentage values configured for all the media channels is 100. |
| Step 4 | Define the duration in days, hours, and minutes for each media channel. This is the maximum duration for which a task that
                                                belongs to the specific media channel remains in the queue after which it gets timed out. Media Channel Default Duration Email 3 days Social Media 3 days Voice callback 2 hours Chat 2 hours | Media Channel | Default Duration | Email | 3 days | Social Media | 3 days | Voice callback | 2 hours | Chat | 2 hours |
| Media Channel | Default Duration |
| Email | 3 days |
| Social Media | 3 days |
| Voice callback | 2 hours |
| Chat | 2 hours |
| Step 5 | Click Save . |

| Note | Make sure that the sum of the percentage values configured for all the media channels is 100. |
|---|---|

| Media Channel | Default Duration |
|---|---|
| Email | 3 days |
| Social Media | 3 days |
| Voice callback | 2 hours |
| Chat | 2 hours |

| Step 1 | In the Unified CCE Administration portal, navigate to Overview > Digital Channels > Digital Channel Settings > User Sync . Note The DataConn service is active only on the publisher node of Cloud Connect. Ensure that the publisher node is accessible for
                                                         you to view the User Sync page. | Note | The DataConn service is active only on the publisher node of Cloud Connect. Ensure that the publisher node is accessible for
                                                         you to view the User Sync page. |
|---|---|---|---|
| Note | The DataConn service is active only on the publisher node of Cloud Connect. Ensure that the publisher node is accessible for
                                                         you to view the User Sync page. |
| Step 2 | In the Network Entry Point field, enter the hostname or FQDN of the load balancer or the reverse proxy server based on your deployment. It is through
                                          this network entry point that the Webex Engage sends the response request to the DataConn service for agent synchronization. |
| Step 3 | In the AW Database Details area, complete the following fields to configure the DataConn service for the Primary and the Secondary Server: In the AW Datasource Host field, enter the IP address or the host name of the AW server that has the agent configurations. In the Port field, enter the SQL port number of the AW database server. In the Database Name field , enter the name of the AW database server. In the Database User ID and Password fields, enter the user ID and password of the SQL user account that you created for digital channels. |
| Step 4 | Click Test Connection to make sure that the DataConn service can read the data from the AW Primary server. |
| Step 5 | Switch on the Enable Failover toggle button to enable the failover to the Secondary AW server. |
| Step 6 | To synchronize agents, choose one of the following options: Enable the Enable Sync toggle button to automatically synchronize agents in an interval of 30 minutes. Click Sync Now to manually synchronize the agents. This option is available only when the Current Sync Status field appears as Scheduled . Note If you recreate your AW Database to fix any errors, ensure that you disable User Sync before starting with the recreation
                                                         process. Enable the User Sync only after the AW Database is created and synchronized with the central controller database. | Note | If you recreate your AW Database to fix any errors, ensure that you disable User Sync before starting with the recreation
                                                         process. Enable the User Sync only after the AW Database is created and synchronized with the central controller database. |
| Note | If you recreate your AW Database to fix any errors, ensure that you disable User Sync before starting with the recreation
                                                         process. Enable the User Sync only after the AW Database is created and synchronized with the central controller database. |
| Step 7 | In the Last sync field, view the date, time and status of the previous synchronization. |
| Step 8 | In the Agents Sync Details field, view the number of agents that are synchronized successfully. The number of agents appears as a clickable link. Click
                                          the link to view the list of agent records that have failed to synchronize and the list of agent records that are pending
                                          for synchronization. You can choose to refresh the agent records at any given point in time. |
| Step 9 | In the Current Sync Status field, you can view one of the following statuses: No sync is in progress or scheduled —This status appears when the Enable Sync toggle button is off. Scheduled —This status appears when the Enable Sync toggle button is on. In Progress —This status appears when the scheduled sync or manual sync is in progress. Manual Sync Failed —This status appears when the manual sync has failed. Unknown —When sync status is not available. |
| Step 10 | Click Save . |

| Note | The DataConn service is active only on the publisher node of Cloud Connect. Ensure that the publisher node is accessible for
                                                         you to view the User Sync page. |
|---|---|

| Note | If you recreate your AW Database to fix any errors, ensure that you disable User Sync before starting with the recreation
                                                         process. Enable the User Sync only after the AW Database is created and synchronized with the central controller database. |
|---|---|

| Step 1 | In the Unified CCE Administration portal, navigate to Overview > Digital Channels > Digital Channel Settings > ECC Variable . |
|---|---|
| Step 2 | On the ECC Variable page, click the plus icon (+). The Add ECC Variable page appears with existing variables Name and Enabled details. It excludes the built-in variables. |
| Step 3 | Select the required variable. The ECC Variable page displays the newly added ECC variable. |
| Step 4 | Click Save . |

| Note | The Cloud Connect Management service is active only on the publisher node of Cloud Connect. |
|---|---|

| Step 1 | In the Unified CCE Administration portal, navigate to Overview > Digital Channels > Digital Channel Settings > Integration . |
|---|---|
| Step 2 | On the OAuth2 Authentication Details page, perform the following steps. In the Name field, enter a name for the Cloud Connect integration. This field is editable. In the Description field, enter a description of what the client application does. In the Client Id and Client Secret fields, enter the client id and secret key that you can retrieve from the Webex Connect portal (navigate to Assets > Integrations > CCE pre-built integrations > Actions > Manage ). In the  field, enter the password that is provided to you at the time of registration. This is the secret key that was used
                                                for generating the token. From the Method drop-down list, select the POST method for Webex Connect integration. From the Content Type drop-down list, select a media content type. This determines the response format. The available options are application/json , application/xml , and application/x-www-form-urlencoded . For Webex Connect integration, select application/x-www-form-urlencoded . In the Access Token JSON path , enter the path in the JSON response to fetch the value of the access token. For the Webex Connect integration, enter access_token . (Optional) In the Header List section, click + icon to add a header name and value and click Add . The header name and value are used to pass any additional information that Webex Connect may require for Cloud Connect integration. |
| Step 3 | Click Save to save the OAuth2 authentication details. |
| Step 4 | Go to the Webhook tab to register the Webhook URL in the Digital Routing service. To fetch the Webhook URL: In the Webex Connect portal, navigate to Assets > Integrations . In the CCE pre-built integrations row, from the Actions column, select Manage . The Manage Integration - Prebuilt Integration page appears. In the Inbound Events section, copy the Webhook URL. |
| Step 5 | Paste the URL in the Webhook URL field in the Unified CCE Administration portal ( Overview > Digital Channels > Digital Channel Settings > Integration > Webhook ). |

| Step 1 | In the Unified CCE Administration portal, navigate to Overview > Digital Channels > Digital Channel Settings > Advanced Settings . |
|---|---|
| Step 2 | The Port is a display-only field and the default value is 38001 . It is through this port that Cloud Connect and MR PG communicates with each other. |
| Step 3 | The Secured toggle switch is turned on by default. It is to establish a secured connection between Cloud Connect and MR PG. You can turn-off
                                          this toggle switch to disable the secure connection. |
| Step 4 | Click Save . |

| Step 1 | In Unified CCE Administration , choose Users > Agents . |
|---|---|
| Step 2 | Click on the agent row whose services are to be modified. |
| Step 3 | Click the Contact Center AI tab. Displays a list of services enabled or disabled for the agent. |
| Step 4 | To enable or disable the required Contact Center AI Services , check or uncheck the check boxes corresponding to the services. |
| Step 5 | Click Save . |

| Step 1 | In Unified CCE Administration , choose Users > Agents . |
|---|---|
| Step 2 | Check the check box corresponding to each agent whose services you want to edit. |
| Step 3 | Click Edit > Contact Center AI . The Edit Services dialog displays a list of services that are the service that is enabled or disabled. If the service is enabled for all the agents selected for editing, the check box is checked. If the service is disabled for all the agents selected for editing, the check box is unchecked. If the service is enabled for some agents and disabled for the others, the check box has a dash (—). |
| Step 4 | To enable or disable the Contact Center AI Services , check or uncheck the check boxes corresponding to the services. |
| Step 5 | Click Save , and then click Yes to confirm the changes. |

| Step 1 | Navigate to Unified CCE Administration > Overview > Bulk Import . |
|---|---|
| Step 2 | Click Templates . The Download Templates popup window opens. |
| Step 3 | Click the Download icon for the Contact Center AI template you want to use. |
| Step 4 | Click OK to close the Download Templates popup window. |
| Step 5 | Open the .csv template in Microsoft Excel. |
| Step 6 | Populate the file as described in the Bulk Contact Center AI Services Content File . |
| Step 7 | Save the populated file to the local machine. |
| Step 8 | Navigate to Unified CCE Administration > Overview > Bulk Import . |
| Step 9 | Click New . |
| Step 10 | In the optional Description field, enter up to 255 characters to describe the bulk job. |
| Step 11 | In the Content file field, choose the file to upload, and then click Save . |

| Note | Contact Center AI service Contact Center AI Services can be enabled or disabled for each agent or for multiple agents together. For more information, see Contact Center AI Services . |
|---|---|

| Note | Ensure that Agent ID (Peripheral number) and agent Login name is unique for each user. |
|---|---|

| Note | Attributes is a prerequisite for Precision Queue. |
|---|---|

| Note | To add or update
                                       Multichannel MRDs for Enterprise Chat and Email, use the
                                       Configuration Manager Media Routing Domain List tool. |
|---|---|

| Note | Do not run bulk jobs during heavy call
                                       load. |
|---|---|

| Note | Supervisors have no access to the
                                       Bulk Jobs tool. |
|---|---|

| Note | Bulk job is available for administrators only when Cloud Connect is added in the inventory and registered on the Control Hub. |
|---|---|

| Field | Required? | Description |
|---|---|---|
| agentId | Agent ID or Username | Existing agentId for which you want to enable or disable the Contact Center AI Services . You must provide either an agentId or the userName. If both are provided, agentId takes precedence over the userName. If the
                                          agentId value is left blank, the userName will reference an existing agent. |
| userName | Username or Agent ID | Username of the agent for which you want to enable or disable the Contact Center AI Services . If no agent is found with the given username, the Contact Center AI Services association fails. |
| agentServices | Yes (to enable Contact Center AI Services ) | The type of Contact Center AI Services to be associated with the agent. Supported values are AgentAnswers , VAV Transcript, and Transcript. To associate more than one services, seperate the values using semicolon (;). If the value is updated, any existing enabled service gets overwritten. If the value is left empty, no service gets associated
                                          with the agent. |

| Note | For information on using the gadget after you select a deployment type, see the Cisco Unified Contact Center Enterprise Developer Reference Guide at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-programming-reference-guides-list.html and the online help. |
|---|---|

| Step 1 | In Unified CCE Administration , choose Organization > Business Hours . |
|---|---|
| Step 2 | On the Business Hours page, click New to open the New Business Hours page. |
| Step 3 | Complete the following information on the General tab and click Save . Field Required? Description Status - Select one of the following statuses for the business hour: Open/Closed as per Business Calendar Force Open Force Close Status Reason Yes, if the status is Force Open or Force Close. This field is enabled only if the status is Force Open or Force Close. Search and select a status reason for the business
                                                         hour. Name Yes Enter a unique name for the business hour. Maximum length is 32 characters. Valid characters are alphanumeric, period (.),
                                                         and underscore (_). The first character must be alphanumeric. Description No Enter a description of the business hour. Time Zone Yes Select a time zone of the business hour from the drop-down list. Department - Search and select a department to associate with the business hour. Default is Global. Note This is applicable for Packaged CCE deployment only. | Field | Required? | Description | Status | - | Select one of the following statuses for the business hour: Open/Closed as per Business Calendar Force Open Force Close | Status Reason | Yes, if the status is Force Open or Force Close. | This field is enabled only if the status is Force Open or Force Close. Search and select a status reason for the business
                                                         hour. | Name | Yes | Enter a unique name for the business hour. Maximum length is 32 characters. Valid characters are alphanumeric, period (.),
                                                         and underscore (_). The first character must be alphanumeric. | Description | No | Enter a description of the business hour. | Time Zone | Yes | Select a time zone of the business hour from the drop-down list. | Department | - | Search and select a department to associate with the business hour. Default is Global. Note This is applicable for Packaged CCE deployment only. | Note | This is applicable for Packaged CCE deployment only. |
| Field | Required? | Description |
| Status | - | Select one of the following statuses for the business hour: Open/Closed as per Business Calendar Force Open Force Close |
| Status Reason | Yes, if the status is Force Open or Force Close. | This field is enabled only if the status is Force Open or Force Close. Search and select a status reason for the business
                                                         hour. |
| Name | Yes | Enter a unique name for the business hour. Maximum length is 32 characters. Valid characters are alphanumeric, period (.),
                                                         and underscore (_). The first character must be alphanumeric. |
| Description | No | Enter a description of the business hour. |
| Time Zone | Yes | Select a time zone of the business hour from the drop-down list. |
| Department | - | Search and select a department to associate with the business hour. Default is Global. Note This is applicable for Packaged CCE deployment only. | Note | This is applicable for Packaged CCE deployment only. |
| Note | This is applicable for Packaged CCE deployment only. |
| Step 4 | Click the Regular Hours tab and complete the following information: Select one of the following Business Hour Type : 24x7 : Always open. You cannot customize the working hours. Custom : You can customize the working hours. If you select Custom , enable at least one business day and select the Start Time and End Time . |
| Step 5 | Click the Special Hours & Holiday tab. You can either add or import special hours and holidays. |
| Step 6 | Click Add to open the Add Special Hours & Holiday popup window. Complete the following information: Field Required? Description Date Yes Select a date from the calendar. Description No Enter a description for the special hour. Status - Select a status. If the status is Open , the Start Time and End Time fields are enabled. Start Time Yes, if status is Open. Select a start time for the special hour. End Time Yes, if status is Open. Select an end time for the special hour. Duration - Displays the duration of the special hour. Status Reason Yes Search and select a status reason. | Field | Required? | Description | Date | Yes | Select a date from the calendar. | Description | No | Enter a description for the special hour. | Status | - | Select a status. If the status is Open , the Start Time and End Time fields are enabled. | Start Time | Yes, if status is Open. | Select a start time for the special hour. | End Time | Yes, if status is Open. | Select an end time for the special hour. | Duration | - | Displays the duration of the special hour. | Status Reason | Yes | Search and select a status reason. |
| Field | Required? | Description |
| Date | Yes | Select a date from the calendar. |
| Description | No | Enter a description for the special hour. |
| Status | - | Select a status. If the status is Open , the Start Time and End Time fields are enabled. |
| Start Time | Yes, if status is Open. | Select a start time for the special hour. |
| End Time | Yes, if status is Open. | Select an end time for the special hour. |
| Duration | - | Displays the duration of the special hour. |
| Status Reason | Yes | Search and select a status reason. |
| Step 7 | Click Save to add the special hours and holidays. |
| Step 8 | To import special hours and holidays, follow these steps. Click Import to open the Import Special Hours and Holidays pop-up window. Click the download icon to download the Special Hours & Holidays template. Use this template to enter the special hours and
                                                holidays. Click Choose File and browse to the special hours and holidays file. Click Import to upload the file. Note The file must contain at least one special hour and holiday. The file must be in CSV format with a file extension as .txt or .csv. | Note | The file must contain at least one special hour and holiday. The file must be in CSV format with a file extension as .txt or .csv. |
| Note | The file must contain at least one special hour and holiday. The file must be in CSV format with a file extension as .txt or .csv. |
| Step 9 | Click Export to download the special hours and holidays in .csv format. |
| Step 10 | Click Save . Note The imported business hours overwrites the existing ones. | Note | The imported business hours overwrites the existing ones. |
| Note | The imported business hours overwrites the existing ones. |

| Field | Required? | Description |
|---|---|---|
| Status | - | Select one of the following statuses for the business hour: Open/Closed as per Business Calendar Force Open Force Close |
| Status Reason | Yes, if the status is Force Open or Force Close. | This field is enabled only if the status is Force Open or Force Close. Search and select a status reason for the business
                                                         hour. |
| Name | Yes | Enter a unique name for the business hour. Maximum length is 32 characters. Valid characters are alphanumeric, period (.),
                                                         and underscore (_). The first character must be alphanumeric. |
| Description | No | Enter a description of the business hour. |
| Time Zone | Yes | Select a time zone of the business hour from the drop-down list. |
| Department | - | Search and select a department to associate with the business hour. Default is Global. Note This is applicable for Packaged CCE deployment only. | Note | This is applicable for Packaged CCE deployment only. |
| Note | This is applicable for Packaged CCE deployment only. |

| Note | This is applicable for Packaged CCE deployment only. |
|---|---|

| Field | Required? | Description |
|---|---|---|
| Date | Yes | Select a date from the calendar. |
| Description | No | Enter a description for the special hour. |
| Status | - | Select a status. If the status is Open , the Start Time and End Time fields are enabled. |
| Start Time | Yes, if status is Open. | Select a start time for the special hour. |
| End Time | Yes, if status is Open. | Select an end time for the special hour. |
| Duration | - | Displays the duration of the special hour. |
| Status Reason | Yes | Search and select a status reason. |

| Note | The file must contain at least one special hour and holiday. The file must be in CSV format with a file extension as .txt or .csv. |
|---|---|

| Note | The imported business hours overwrites the existing ones. |
|---|---|

| Step 1 | In Unified CCE Administration , choose Organization > Business Hours . |
|---|---|
| Step 2 | Click the Business Hour you want to copy, and then click the Copy button in the Edit <Business Hour> page. The New Business Hour page opens. |
| Step 3 | Enter Name and Description for the Business Hour. |
| Step 4 | Review the rest of the fields on the General , Regular Hours , and Special Hours & Holiday tabs that were copied from the original Business Hour record, and make any necessary changes. |
| Step 5 | Click Save to return to the List window. |

| Step 1 | In Unified CCE Administration , choose Organization > Business Hours > Status Reasons . |
|---|---|
| Step 2 | Click Add to open the Add Status Reason popup window. |
| Step 3 | Enter the Status Reason. Maximum length is 255 characters. |
| Step 4 | Enter a unique Reason Code. Range is 1001 to 65535. Codes 1 to 1000 are reserved as system-defined reason codes. |
| Step 5 | Click Save . To add more status reasons, repeat steps from 2 to 5. |
| Step 6 | Click Done to return to the List window. |

| Step 1 | On the Business Hours page, select two or more business hours to edit. |
|---|---|
| Step 2 | Choose Edit > Status to open the Edit Business Hours page. |
| Step 3 | Check the Status check box and select the required status. |
| Step 4 | If you select the status as Force Open or Force Close , search and select a Status Reason . |
| Step 5 | Click Save . |

| Step 1 | On the Business Hours page, select two or more business hours to edit. |
|---|---|
| Step 2 | Choose Edit > Schedule to open the Edit Business Hours page. |
| Step 3 | Check the Time Zone check box and the select the required time zone from the drop-down list. |
| Step 4 | Check the Type check box and select the required business hour type. |
| Step 5 | If you select Custom , enable atleast one business day and select the Start Time and End Time . |
| Step 6 | Click Save . |

| Step 1 | Configure the regular working hours for weekdays. |
|---|---|
| Step 2 | Configure Special Hours & Holidays schedules for whole year by doing the following: Add the Special Hours & Holidays details for all the special hours and holidays for the whole year into the CSV template file. On the Import Special Hours & Holidays page, click Choose File and browse to the special hours and holidays file. Click Import to upload the file. After you import the configuration file, the BH configurations are loaded on the Business Hours page. Validate the configurations. Click Save . Note When you update the configured Business Hours, remove any elapsed schedules and then update the new schedules for any new
                                                         special hours or holidays in a Business Hour configuration. | Note | When you update the configured Business Hours, remove any elapsed schedules and then update the new schedules for any new
                                                         special hours or holidays in a Business Hour configuration. |
| Note | When you update the configured Business Hours, remove any elapsed schedules and then update the new schedules for any new
                                                         special hours or holidays in a Business Hour configuration. |

| Note | When you update the configured Business Hours, remove any elapsed schedules and then update the new schedules for any new
                                                         special hours or holidays in a Business Hour configuration. |
|---|---|

| Step 1 | In Unified CCE Administration , choose Overview > Features > Cloud Connect Integration . |
|---|---|
| Step 2 | On Cloud Connect Integration page, registration
                                          information is displayed. To register or deregister click Cisco
                                             Webex . Field Required? Description Registration Registration - Cloud Connect registration status of Control Hub will be
                                                         displayed. Cisco
                                                         Webex Cisco Webex - On Cloud Connect Integration , if you click the Cisco Webex link, you will be
                                                         re-directed to Cisco Webex login page. Cluster
                                                         Information Proxy Details NO Enter the proxy details used by the Cloud Connect. For example: abc.cisco.com:8080 Note By default, HTTP uses the port 80, but you can
                                                                     specify a different port number in the proxy. Deployment ID - Read-only field that displays the Deployment ID, an
                                                         auto-generated identifier of the Unified CCE
                                                         instance. Deployment Name NO Enter a valid deployment name. | Field | Required? | Description | Registration | Registration | - | Cloud Connect registration status of Control Hub will be
                                                         displayed. | Cisco
                                                         Webex | Cisco Webex | - | On Cloud Connect Integration , if you click the Cisco Webex link, you will be
                                                         re-directed to Cisco Webex login page. | Cluster
                                                         Information | Proxy Details | NO | Enter the proxy details used by the Cloud Connect. For example: abc.cisco.com:8080 Note By default, HTTP uses the port 80, but you can
                                                                     specify a different port number in the proxy. | Note | By default, HTTP uses the port 80, but you can
                                                                     specify a different port number in the proxy. | Deployment ID | - | Read-only field that displays the Deployment ID, an
                                                         auto-generated identifier of the Unified CCE
                                                         instance. | Deployment Name | NO | Enter a valid deployment name. |
| Field | Required? | Description |
| Registration |
| Registration | - | Cloud Connect registration status of Control Hub will be
                                                         displayed. |
| Cisco
                                                         Webex |
| Cisco Webex | - | On Cloud Connect Integration , if you click the Cisco Webex link, you will be
                                                         re-directed to Cisco Webex login page. |
| Cluster
                                                         Information |
| Proxy Details | NO | Enter the proxy details used by the Cloud Connect. For example: abc.cisco.com:8080 Note By default, HTTP uses the port 80, but you can
                                                                     specify a different port number in the proxy. | Note | By default, HTTP uses the port 80, but you can
                                                                     specify a different port number in the proxy. |
| Note | By default, HTTP uses the port 80, but you can
                                                                     specify a different port number in the proxy. |
| Deployment ID | - | Read-only field that displays the Deployment ID, an
                                                         auto-generated identifier of the Unified CCE
                                                         instance. |
| Deployment Name | NO | Enter a valid deployment name. |

| Field | Required? | Description |
|---|---|---|
| Registration |
| Registration | - | Cloud Connect registration status of Control Hub will be
                                                         displayed. |
| Cisco
                                                         Webex |
| Cisco Webex | - | On Cloud Connect Integration , if you click the Cisco Webex link, you will be
                                                         re-directed to Cisco Webex login page. |
| Cluster
                                                         Information |
| Proxy Details | NO | Enter the proxy details used by the Cloud Connect. For example: abc.cisco.com:8080 Note By default, HTTP uses the port 80, but you can
                                                                     specify a different port number in the proxy. | Note | By default, HTTP uses the port 80, but you can
                                                                     specify a different port number in the proxy. |
| Note | By default, HTTP uses the port 80, but you can
                                                                     specify a different port number in the proxy. |
| Deployment ID | - | Read-only field that displays the Deployment ID, an
                                                         auto-generated identifier of the Unified CCE
                                                         instance. |
| Deployment Name | NO | Enter a valid deployment name. |

| Note | By default, HTTP uses the port 80, but you can
                                                                     specify a different port number in the proxy. |
|---|---|

| In the Add Machine dialog box: Select Cloud Connect Publisher from the Type list. Enter Hostname or IP Address of the Cloud Connect Publisher Node. Enter Username and Password for your Cloud Connect cluster Administrator. Click Save . |
|---|

| Step 1 | In the Unified CCE Administration, navigate to Overview > Infrastructure Settings , click Inventory . |
|---|---|
| Step 2 | Click the Cloud Connector Publisher device to open the Edit window. Note If you edit the Cloud Connect Publisher, the Cloud Connect Subscriber associated with the publisher is updated automatically.
                                                            You cannot edit Cloud Connect Subscriber from the Inventory page. | Note | If you edit the Cloud Connect Publisher, the Cloud Connect Subscriber associated with the publisher is updated automatically.
                                                            You cannot edit Cloud Connect Subscriber from the Inventory page. |
| Note | If you edit the Cloud Connect Publisher, the Cloud Connect Subscriber associated with the publisher is updated automatically.
                                                            You cannot edit Cloud Connect Subscriber from the Inventory page. |
| Step 3 | Edit the Username and Password for your Cloud Connect cluster Administrator. |
| Step 4 | Click Save . |

| Note | If you edit the Cloud Connect Publisher, the Cloud Connect Subscriber associated with the publisher is updated automatically.
                                                            You cannot edit Cloud Connect Subscriber from the Inventory page. |
|---|---|

| Server Status Category | Description | Example Rules |
|---|---|---|
| Configuration | Rules for installation and configuration of a component. These rules identify problems with mismatched configuration between components, missing services, and incorrectly configured
                                                services. | Cloud Connect: The status and alerts will appear only if the Cloud Connect is added to the Inventory. For example:Webex Experience Management service must be reachable on the network Note When the machine status is out of sync, every 10mins auto sync will be triggered to synchronize the machine configuration. | Note | When the machine status is out of sync, every 10mins auto sync will be triggered to synchronize the machine configuration. |
| Note | When the machine status is out of sync, every 10mins auto sync will be triggered to synchronize the machine configuration. |
| Operation | Rules for the runtime status of a component. These rules identify services and processes that cannot be reached, are not running, or are not in the expected state. |

| Note | When the machine status is out of sync, every 10mins auto sync will be triggered to synchronize the machine configuration. |
|---|---|

| Step 1 | Navigate to Unified CCE Administration > Infrastructure Settings > Inventory . |
|---|---|
| Step 2 | Hover over the Cloud Connect Publisher device and click the x icon. |
| Step 3 | Click Yes to confirm the deletion. Note If you delete the Cloud Connect Publisher, the Cloud Connect Subscriber associated with the publisher is deleted automatically.
                                                            You cannot delete Cloud Connect Subscriber from the Inventory page. | Note | If you delete the Cloud Connect Publisher, the Cloud Connect Subscriber associated with the publisher is deleted automatically.
                                                            You cannot delete Cloud Connect Subscriber from the Inventory page. |
| Note | If you delete the Cloud Connect Publisher, the Cloud Connect Subscriber associated with the publisher is deleted automatically.
                                                            You cannot delete Cloud Connect Subscriber from the Inventory page. |

| Note | If you delete the Cloud Connect Publisher, the Cloud Connect Subscriber associated with the publisher is deleted automatically.
                                                            You cannot delete Cloud Connect Subscriber from the Inventory page. |
|---|---|

| Step 1 | Run the unset cloudconnect subscriber command. The command removes the Cloud Connect subscriber node configuration from the
                                                cluster. For more information, see Cloud Connect CLI Command in the Cisco Unified Contact Center Enterprise Installation and Upgrade
                                                   Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |
|---|---|
| Step 2 | Power off the subscriber node. Note When a subscriber node is removed from a cluster, its certificates still
                                                            exist in the publisher node. The administrator must manually remove the
                                                            following: The certificate of the subscriber node from the trust-store of
                                                                  the publisher node. The certificates of the publisher from the trust-store of the
                                                                  removed subscriber node. | Note | When a subscriber node is removed from a cluster, its certificates still
                                                            exist in the publisher node. The administrator must manually remove the
                                                            following: The certificate of the subscriber node from the trust-store of
                                                                  the publisher node. The certificates of the publisher from the trust-store of the
                                                                  removed subscriber node. |
| Note | When a subscriber node is removed from a cluster, its certificates still
                                                            exist in the publisher node. The administrator must manually remove the
                                                            following: The certificate of the subscriber node from the trust-store of
                                                                  the publisher node. The certificates of the publisher from the trust-store of the
                                                                  removed subscriber node. |
| Step 3 | Run the utils system restart command to restart the
                                             publisher node. |

| Note | When a subscriber node is removed from a cluster, its certificates still
                                                            exist in the publisher node. The administrator must manually remove the
                                                            following: The certificate of the subscriber node from the trust-store of
                                                                  the publisher node. The certificates of the publisher from the trust-store of the
                                                                  removed subscriber node. |
|---|---|

| Step 1 | Login to Experience Management tool with your admin credentials. |
|---|---|
| Step 2 | In Experience Management tool, navigate to CX Setup > Questionnaire > . You can select the questionnaire and associate it to the voice survey. Note To create or modify questionnaires refer to https://xm.webex.com/docs/cxsetup/questionnaires/ https://xm.webex.com/docs/cxsetup/questionnaires/ | Note | To create or modify questionnaires refer to https://xm.webex.com/docs/cxsetup/questionnaires/ https://xm.webex.com/docs/cxsetup/questionnaires/ |
| Note | To create or modify questionnaires refer to https://xm.webex.com/docs/cxsetup/questionnaires/ https://xm.webex.com/docs/cxsetup/questionnaires/ |
| Step 3 | On the right side of the screen, click IVR button beside the question and upload the audio file. Figure 1. upload the audio file |
| Step 4 | Follow the above steps to upload audio files for more questionnaires. Note Experience Management is configured to capture only the complete feedback after the voice calls. If the caller drops the call
                                                            without answering all the questions, the partial feedback is discarded. | Note | Experience Management is configured to capture only the complete feedback after the voice calls. If the caller drops the call
                                                            without answering all the questions, the partial feedback is discarded. |
| Note | Experience Management is configured to capture only the complete feedback after the voice calls. If the caller drops the call
                                                            without answering all the questions, the partial feedback is discarded. |

| Note | To create or modify questionnaires refer to https://xm.webex.com/docs/cxsetup/questionnaires/ https://xm.webex.com/docs/cxsetup/questionnaires/ |
|---|---|

| Note | Experience Management is configured to capture only the complete feedback after the voice calls. If the caller drops the call
                                                            without answering all the questions, the partial feedback is discarded. |
|---|---|

| Step 1 | In the Configuration Manager menu, select Tools > List Tools > Expanded Call Variables List . The Expanded Call Variables List window appears. |
|---|---|
| Step 2 | Click Retrieve to view the list of existing ECC variables. |
| Step 3 | Check if the user.microapp.isPostCallSurvey variable exists. If the variable does not exist, do the following to create a new variable: Click Add . In the Attributes tab that appears, enter user.microapp.isPostCallSurvey in the Name field. Set Max Length to 1. Check the Enabled check box. Click Save . When your CCE routing scripts starts, the Post Call Survey field is enabled by default even if user.microapp.isPostCallSurvey has not yet been set in the script. You can turn off Post Call Survey field in the script by setting user.microapp.isPostCallSurvey to n . You can later enable Post Call Survey in the same path of the script by setting this variable to y . Note To enable Experience Management, user.microapp.isPostCallSurvey must be set to y . | Note | To enable Experience Management, user.microapp.isPostCallSurvey must be set to y . |
| Note | To enable Experience Management, user.microapp.isPostCallSurvey must be set to y . |
| Step 4 | Check if the user.CxSurveyInfo variable exists. If the variable does not exist, do the following to create a new variable: Click Add . In the Attributes tab that appears, enter user.CxSurveyInfo in the Name field. Set the Max Length to 133 for Type 10 VRUs. For all other routing clients, set Max Length to 80. Check the Enabled check box. |
| Step 5 | Click Save . Note The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                            payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. | Note | The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                            payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. |
| Note | The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                            payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. |
| Step 6 | Populate the POD. ID variable. For more information on populating this variable, refer to the topic Configure POD.ID . |
| Step 7 | Restart the active VRU PG (side A or B) to register the new ECC variable. If the ECC variable already exists, you can skip this step. Note The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                            of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. | Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                            of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. |
| Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                            of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. |

| Note | To enable Experience Management, user.microapp.isPostCallSurvey must be set to y . |
|---|---|

| Note | The newly created ECC variables are added to the default payload list. If you want to save the ECC variables to a different
                                                            payload list, in the Configuration Manager , navigate to Tools > List Tools > Expanded Call Variable Payload List and add the ECC variables to the payload list of your choice. |
|---|---|

| Note | The user.microapp.isPostCallSurvey setting takes effect on Unified CVP only when it receives a connect or temporary connect message. If you do not want the survey to run, without first reaching an agent (such as 'after hours
                                                            of treatment'), set the isPostCallSurvey to n before the initial 'Run script request'. |
|---|---|

| Attribute | Description | Applicable |
|---|---|---|
| cc_CustomerId | Unique ID for a customer across multiple channels | Chat and Email surveys for Digital Channels |
| Email | Email ID of the caller for Email surveys | Email survey for voice channel |
| Mobile | Phone number for SMS surveys | SMS survey for voice channel |
| cc_language | Language of the survey For the list of supported languages, refer to the Webex Experience Management documentation at https://xm.webex.com/docs/user/getting-help/#cloudcherry-language-support | Email, SMS, and Voice surveys for voice channel |
| Optin | Whether to opt in or opt out of the survey | Email, SMS, and Voice surveys for voice channel |

| Step 1 | In Configuration Manager , navigate to Tools > List Tools > DialedNumber/Script Selector List . |
|---|---|
| Step 2 | In DialedNumber/Script Selector List create Incoming Dialed Number and Post Call Survey Dialed Number . For more information on how to create a PCS Dialed Number, refere to the section Configure ICM for Post Call Survey in Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Step 3 | Click Save . You will be re-directed to the Configuration Manager window. |
| Step 4 | In Configuration Manager , navigate to Tools > List Tools > Call Type List . |
| Step 5 | In Call Type List create the Call Type . You should associate to the incoming call script and PCS script. You should associate the incoming call type with the survey from CCEAdmin. For more information, refer to the topic Associate Survey to Call Type in Unified CCE Admin . |

| Note | Only one survey can be associated to a Call Type. |
|---|---|

| Step 1 | In Unified CCE Administration , navigate to Overview > Call Settings > Route Settings > Call Types . The list of all the Call Types are displayed. For more information on Call Types, refer to the Help in ConfigManager > List Tools > Call Types . |
|---|---|
| Step 2 | Click on the Call Type which you want to associate to the Survey. Associate the survey with the last call type before the call is first connected
                                             to an agent. |
| Step 3 | Select the Enable Experience Management check box to associate the Webex Experience Management survey. The Experience Management tab is enabled with the following options: Inline Survey (post-call voice survey) Deferred Survey (post-call Email and SMS survey) |
| Step 4 | Click on the magnifying glass icon, and the configured surveys will be populated in the pop-up window. |
| Step 5 | Select the survey from the pop-up window and click Save . |