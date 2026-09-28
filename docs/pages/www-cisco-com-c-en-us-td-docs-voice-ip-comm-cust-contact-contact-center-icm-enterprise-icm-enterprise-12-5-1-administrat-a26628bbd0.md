---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-administrat-a26628bbd0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/administration/guide/ucce_b_administration-guide-for-cisco-unified12_5/ucce_b_administration-guide-for-cisco-unified12_5_chapter_0111.html
retrieved_at: 2026-08-16T20:49:55.619290+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)

# Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)

Updated: February 7, 2019

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

You can search and sort this list, and you can click the row for an agent to open the Edit Agent window. You can only edit an agent's attribute settings.

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

Bulk jobs are a fast and efficient way to migrate existing agent and supervisor to single sign-on accounts.

Do not run bulk jobs during heavy call
                                       load.

Supervisors have no access to the
                                       Bulk Jobs tool.

## Deployment
                        	 Type

The deployment type you select, significantly impacts the call processing capacity, configuration limits, smart license type,
                           and access to the features and configuration tools. The configuration steps vary for every deployment type.

You can select any one of the following deployment types:

Packaged CCE Deployment types:

Packaged CCE: Lab Mode

Packaged CCE:2000 Agents

Packaged CCE: 4000 Agents

Packaged CCE: 12000 Agents

HCS for Contact Center deployment types:

HCS-CC: 2000 Agents

HCS-CC: 4000 Agents

HCS-CC: 12000 Agents

HCS-CC: 24000 Agents

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

Cloud Connect is a component that hosts services that allow customers to use cloud capabilities such as Cisco Webex Experience Management and CCE Orchestration.

The administrator should configure the Cloud Connect server settings in the Finesse Administration console to contact the
                           Cisco cloud services. For more information, see Cloud Connect Server Settings section in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html

### Initial Configuration for Cloud Connect

For more information, see the section Certificates for CCE Web Administration at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Step 1

In the Unified CCE Administration, navigate to Overview > Infrastructure Settings , click Inventory .

Step 2

In the Inventory page, click New to add the new machine to the System Inventory.

Step 3

In the Add Machine dialog box:

Select Cloud Connect Publisher from the Type list.

Enter Hostname or IP Address of the Cloud Connect Publisher Node.

Enter Username and Password for your Cloud Connect cluster Administrator.

Click Save .

When you configure Cloud Connect Publisher, its Cloud Connect Subscriber is added to the Inventory automatically.

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

| Step 1 | In the Unified CCE Administration, navigate to Overview > Infrastructure Settings , click Inventory . |
|---|---|
| Step 2 | In the Inventory page, click New to add the new machine to the System Inventory. |
| Step 3 | In the Add Machine dialog box: Select Cloud Connect Publisher from the Type list. Enter Hostname or IP Address of the Cloud Connect Publisher Node. Enter Username and Password for your Cloud Connect cluster Administrator. Click Save . Note When you configure Cloud Connect Publisher, its Cloud Connect Subscriber is added to the Inventory automatically. | Note | When you configure Cloud Connect Publisher, its Cloud Connect Subscriber is added to the Inventory automatically. |
| Note | When you configure Cloud Connect Publisher, its Cloud Connect Subscriber is added to the Inventory automatically. |

| Note | When you configure Cloud Connect Publisher, its Cloud Connect Subscriber is added to the Inventory automatically. |
|---|---|

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
                                                services. | Cloud Connect: The status and alerts will appear only if the Cloud Connect is added to the Inventory. Note When the machine status is out of sync, every 10mins auto sync will be triggered to synchronize the machine configuration. | Note | When the machine status is out of sync, every 10mins auto sync will be triggered to synchronize the machine configuration. |
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