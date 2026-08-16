---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-release-gui-1628c2202b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/release/guide/rcct_b_cce-solution-rns-12-6/rcct_m_ece_12_6.html
retrieved_at: 2026-08-16T19:38:24.686675+00:00
---

Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1)

# Release Notes for Cisco Contact Center Enterprise Solutions Release 12.6(1)

Updated: May 14, 2021

Chapter: Cisco Enterprise Chat and Email

## Chapter: Cisco Enterprise Chat and Email

# Cisco Enterprise Chat and Email

## New Features

### Support for 2500 Concurrent Agents and Reduced Application and Web Servers for Fully Distributed Model

No change in VMs or agent support for existing 1500 agent deployment.

For 2500 concurrent agents with 3 Web/App support, use the 2500 Agent OVA.

For 1500 concurrent agents with 2 Web/App support, use the 2500 Agent OVA.

The ‘not-required’ application and web servers can be uninstalled and removed by following the appropriate guides.

### Decoupled ECE Login/Logout of SSO Agents From Finesse

As per previous design, if SSO is configured at Finesse and ECE side and when the agent logs in to Finesse agent desktop,
                              the agent gets logged in automatically to digital channels offered by ECE and doesn't have an option to log out of ECE gadget.
                              This results in consuming a premium license for the agent though the agent doesn't want to work on ECE tasks for that day
                              or session. This results in additional cost on the customers adapting to Smart Licensing. With ECE 12.6(1) ES3, agents will
                              only be logged in to ECE, when they click on ECE gadget and also will be able to log out from only ECE, if they want to. A
                              new logout option is enabled inside the ECE gadget. For more details, refer the Enterprise Chat and Email Agent’s Guide, Release 12.6(1) .

### New Settings for Auto-Completion of Real-Time and Asynchronous Chat Activities

Auto-complete unselected and abandoned real-time chat activities.

Auto-complete unselected and abandoned asynchronous chat activities.

### Platform

#### Infrastructure

All new installations and systems upgrading to 12.6(1) should use Microsoft Windows and
                                 				Microsoft SQL Server versions and combinations documented in Compatability Matrix 12.6(1) .

#### Cross-Browser Support

The Administration Console and Agent Console are now supported only on Chrome, Edge, and Firefox browsers. Administration
                                 Console and Agent Console are not supported on Internet Explorer. Only the Reports Console is supported on Internet Explorer.
                                 The latest version of each browser was tested at time of release.

#### User Interface in Polish and Czech

The user interface for all consoles is now available in Polish and Czech languages. Note that Dictionary support is not available
                                 for these two new languages.

### Simplified Administration Console

Simplified Administration Console for Unified CCE

The Administration Console has been fully redesigned to be more contemporary and efficient. The new console streamlines administrative
                              tasks by merging actions that were previously distributed across the Administration, System, and Tools Consoles.

Consolidation of Consoles into the Administration Console

System Console functions have been consolidated into the new Administration Console. This group of features is available
                                    only to users who have system-level view permissions and system-level manage permissions.

Tools Console functions have been consolidated into the new Administration Console. Some of the utilities within the Tools
                                    Console are available only to users who have system- level view permissions and system-level manage permissions.

Reorganization of Configurations and Settings

Settings and the configuration processes necessary to setup and maintain the product have been restructured and reorganized
                                    to improve the user experience.

Settings that are specific to particular apps or features of the application can be configured within the same space.

Apps and their configuration elements have been combined to reduce the number of mouse-clicks and navigation necessary to
                                    complete an app’s configuration process.

Pagination and Filters

The Administration Console has been restructured to use pagination to improve the user experience. This removes clutter from
                                    the console and allows users to navigate through the different functions of the console with ease.

A filtering search feature is available to help users to quickly find the functions they want. This search feature works across
                                    the pagination and auto-completes as the user types in the feature name. Filtering search functionality is available in the
                                    List and Properties pages to quickly locate objects in the system and save time during the configuration process.

Enhanced Administration Console for Packaged CCE

As a part of overall Administration Console enhancements, several additions have been made to the ECE administration console
                              that is hosted as a gadget within the Packaged CCE web admin console., This includes the ability to create workflows and supervision
                              monitors, manage storage and purge configuration, and so on. Administrators now do not have to navigate away from the Packaged
                              CCE Administration interface to manage anything specific to ECE, apart for the Reports console.

### New Administrator Privileges

#### System Administrator Privileges

New privileges have been created for system administrators that supersede all other roles, permissions, and actions: the Manage
                                       System Resource and View System Resource privilege.

When combined, these privileges form a full-fledged system administration user. System administrators can only be created
                                       by other system administrators.

System administrators are granted the View Partition Resource action, by default. This allows them a read-only view of all
                                       partition-level and department-level nodes.

System administrators are now users who can perform system-level tasks. This reassignment of the system administrator’s access
                                       and permissions reduces the effort required for business users to configure the application to meet their needs.

#### Partition Administrator Privileges

Two new privileges have been created for partition administrators that supersede other roles, permissions, and actions: The
                                 Manage Partition Resource privilege and View Partition Resource privilege.

When combined, the privileges form a full-fledged partition administration user. These users can only be created by other
                                 partition administrators.

For details about configuring this feature, see the Enterprise Chat and Email Administrator’s Guide to Administration Console at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

### Chat Throttling

A security feature has been added to web chat to prevent a single chat client from creating multiple chats and flooding chat
                              queues with spam chats.

The feature limits the number of chats that can be created from one IP address in one hour.

This feature is configured in the Security configuration section (Security > Access Restrictions > Blocked Visitors) of the
                                    Administration Console and is disabled by default.

For details about configuring this feature, see the Enterprise Chat and Email Administrator’s Guide to Administration Console
                              at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html

### Audit Reporting for Administration Actions

All actions performed by an administrator in the application are logged and can be viewed in the Administration Console.

The new audit interface can be used to view, filter, and trace any specific administrator action performed in the last four
                                    weeks.

This feature ensures that any actions performed in the application can be reviewed and any unintended results can be resolved
                                    easily.

For details about configuring this feature, see the Enterprise Chat and Email Administrator’s Guide to Administration Console at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

### Aria Chat Template

A new chat template, Aria, is available with this release. Aria uses an updated template structure that separates the core
                              and custom components that allows for the styles, appearance, and formatting of the template to be further customized easily.

For more information about personalizing chat templates, see the Enterprise Chat and Email Administrator’s Guide to Chat Resources
                              at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

### Support for Grammarly in the Agent Gadget

The Grammarly browser plugin is now supported in the Agent Console.

### APIs

#### Improved Interaction APIs

Users can compose activities with an active queue.

Users do not need the View Tools Console action to mask the activity if the users with Manage Utilities action is assigned.

Users assigned with Manage Utilities action can complete activities.

Users can create a contact point of the apple opaque ID type using the following APIs:

Create Individual Customer

Edit Individual Customer

Users can retrieve purge flags and the contact points of the apple opaque ID types using the Get activity by ID and Activity
                                       Search APIs.

Users can edit the content of completed email and chat activities.

With ECE 12.6(1) ES2, the following changes are made to ECE APIs to enhance the experience of obfuscation of customer data:

Customer search API: Enhanced to incorporate the date of customer creation. The API has a range parameter and returns a list
                                       of customers in the specified range.

Obfuscate customers API: Introduced to obfuscate customers asynchronously. Only one customer information is processed at any
                                       given time. As part of running this API, the information of customers that are provided in the request is obfuscated from
                                       the application.

Get Obfuscate Request Status API: Allows users to retrieve the status of a CSV file that is used in the obfuscate customer
                                       request. The status helps to identify the successful and failed transactions in the obfuscate customer API request.

Before running the obfuscation APIs, consider the following recommendations:

Run the APIs during nonbusiness hours.

Have the number of customers to be obfuscated. The time taken will be high when the number of customers is more.

To estimate the time taken to run the APIs, refer to the time guidance calculator.

Run these APIs when there are no maintenance tasks scheduled.

#### Messaging APIs

New Messaging APIs have been added to allow users to deactivate the webhook callback URL.

The following new message types are now supported: Delivered, Read and Geolocation

Customers can retrieve the contact points of the apple opaque ID type by using the Get Conversation Details API.

### Routing

#### Preferred Agent for Chats

Agents can now be set as the preferred agent for a particular customer during chat interactions. After the preferred agent
                                 is set, the routing of incoming chat activities from the same customer is configured by Unified CCE scripts to consider the
                                 preferred agent for the incoming chat.

Administrators must add and configure the Queue to Agent node in the Unified CCE script by referencing Call.PreferredAgentID.
                                       For more information, about Configuring Queue to Agent Node , see the Scripting and Media Routing Guide at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/User/guide/ucce_b_scripting-and-media-routing-guide_12_6.html .

The following settings are added to the ECE Administration Console to allow administrators to refine their routing methods
                                       for chats in the application.

Enable preferred agent assignment—To enable the preferred agent feature in the application.

Set last assigned agent as preferred agent—Automatically sends the skill target ID of the agent who most recently handled
                                             a customer's chat or messaging activity as the preferred agent ID for the customer to Unified CCE.

Allow agent to set preferred agent—Allows agents to mark themselves as the preferred agent for a customer.

Allow agent to reset preferred agent—Allows agents to clear the selected preferred agent for a customer.

Assign to preferred agent—Determines when to send the preferred agent ID to Unified CCE. One of the following options can
                                             be selected: Always, Logged In, and Available.

Ignore maximum load for preferred agent assignment—The preferred agent ID is sent to Unified CCE even if an agent has reached
                                             the maximum concurrent task limit for chat activities.

Preferred agent assignment duration—Determines the length of time for which an agent can be marked as preferred agent for
                                             a customer. This duration starts after an activity for which the preferred agent is set gets completed. After this duration
                                             is passed, standard routing method is used to assign chat activities.

Preferred agent assignment duration in days—Determines the number of days for which an agent can be marked as preferred agent
                                             for a customer. This duration starts after an activity for which preferred agent is set gets completed.

Auto-pushback chats from preferred agent—Decides whether to automatically push back chat activities from the preferred agent's
                                             inbox if the agent does not click the activity in the time defined in the Expiry time for auto-pushback for chats setting.

## Updated Features

### Administration

#### Storage Purge Management and Reporting

The Purge Job feature has been enhanced to the application, providing a self-serve method of purging data. The feature provides
                                 centralized reporting of allocated and used data across email and chat in the installation.

The feature ensures businesses to reduce storage costs.

The purge jobs process only needs to be configured once, allowing automatic purge jobs to run without any intervention from
                                       an administrator.

The purge jobs process can operate with no service disruptions.

Diagnostic information and audits are maintained for all purge jobs, ensuring that purge job errors and alerts are handled
                                       gracefully.

For more information, see the Enterprise Chat and Email Administrator’s Guide to Administration Console at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

#### Custom Attributes

The system now allows adding custom attributes to the Contact Person Data and make them visible in the Agent Gadget.

#### Shortcut Settings

A new Enable Shortcuts setting is now available, which can be used to enable or disable the keyboard navigation shortcuts
                                 in the Agent Console.

For details about configuring these features, see the Enterprise Chat and Email Administrator’s Guide to Administration Console at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

#### Object Limits

Maximum limit is introduced in the objects creation for performance reasons.

For more details about the object limits, see the Enterprise Chat and Email Administrator’s Guide to Administration Console at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

### Agent Gadgets

#### Conversational View Improvements

Agents and supervisors can now easily view all communication that has transpired between a customer and an agent through the
                                       Reply pane. The following activity types are included in the conversation view: Email, Chat.

For activities selected from the Main Inbox, an agent can view the most recent communication to and from a customer by clicking
                                       the View Conversation option.

From the Chat Inbox, an agent can scroll up through the chat transcript in the Reply pane. All messages that a customer has
                                       sent to and received from the application are displayed. This includes previous chat interactions with other agents.

For details about this features, see the Enterprise Chat and Email Agent’s Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-user-guide-list.html

#### Chat Monitors

Supervisors can now select multiple agents and queues for monitoring in the Agent Console.

For details about this features, see the Enterprise Chat and Email Agent’s Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-user-guide-list.html

### Platform

#### ECDSA Support

ECDSA certificates are now supported across secured interfaces (internal and external) and Unified CC Enterprise web services.

#### Security

Several improvements are made to security and stability. The following vulnerabilities are addressed:

CVE-2015-5182

CVE-2020-13920

CVE-2020-13947

CVE-2020-1941

CVE-2021-26117

CVE-2021-21290

CVE-2021-21295

CVE-2021-23899

CVE-2021-23900

CVE-2021-20227

CVE-2020-1945

For more details, refer to Cisco ECE 12.6(1) ES1 readme file.

### Outlook Rest API v2.0 Email Support

Microsoft deprecates Basic authentication. Hence, ECE application uses Outlook REST API version 2.0 for authentication through
                              POP and IMAP protocols. From ECE 12.6(1) ES10 onwards, support for "IMAP and SMTP" and "POP3 and SMTP" for O365 will be deprecated.
                              For more details, see the Deprecated Features section.

### Reports Console

#### Edge Certification

If the support for Internet Explorer ends, then the reports can be accessed in the  compatibility mode of Microsoft Edge.

## Important Notes

All the interaction and messaging APIs will be restructured after ECE 12.6(1) release. This release adheres to OpenAPI Specification
                           (OAS) and that results in:

Standardized API URL formats across all APIs.

Semantic versioning of the APIs.

RESTful resource CRUD-based operations.

Standardized request and response payloads.

Error formats, and Page Info.

Consistent header and query string parameter naming.

Paging, Filtering, and Sorting.

Adopting open standards.

## Deprecated Features

Deprecated features are fully supported. However, there is no additional development for deprecated features. These features
                           may be scheduled to be removed in a future release. Plan to transition to the designated replacement feature. If you are implementing
                           a new deployment, use the replacement technology rather than the deprecated feature.

Deprecated Feature

Announced in Release

Replacement

Notes

1500 agent OVAs

12.6 ES2

None

1500 agent OVAs stand deprecated and will be removed post 12.6.

Support for “IMAP and SMTP” and “POP3 and SMTP” for O365

12.6(1) ES10

Graph API

Microsoft has deprecated the Outlook REST API version 2.0. For email server configuration, the options “IMAP and SMTP” and
                                       “POP3 and SMTP” options will be replaced by Graph API only.

Aqua Chat Template

12.6(1)

None

Aqua template for chat is deprecated in ECE 12.6(1) release. Upgraded customers can continue to use the template. But no new
                                       features will be available on these templates.

Reports Console

12.6(1)

None

None

## Removed and Unsupported Features

The features listed in the following table are no longer available.

Feature

Effective from Release

Replacement

Abandoned Chat Notifications for partition users

12.6(1)

None

Context Service

12.6(1)

None

Users administration section for PA administrator:

Business

Personal

Miscellaneous

12.6(1)

None

| Note | Available starting ECE 12.6(1) ES3 only. |
|---|---|

| Note | Available starting ECE 12.6(1) ES3 only. |
|---|---|

| Note | Available starting ECE 12.6(1) ES3 only. |
|---|---|

| Note | To enable this enhancement in ECE 12.6(1), install the ECE 12.6(1) ES1 patch or the latest ECE ES patch. |
|---|---|

| Deprecated Feature | Announced in Release | Replacement | Notes |
|---|---|---|---|
| 1500 agent OVAs | 12.6 ES2 | None | 1500 agent OVAs stand deprecated and will be removed post 12.6. |
| Support for “IMAP and SMTP” and “POP3 and SMTP” for O365 | 12.6(1) ES10 | Graph API | Microsoft has deprecated the Outlook REST API version 2.0. For email server configuration, the options “IMAP and SMTP” and
                                       “POP3 and SMTP” options will be replaced by Graph API only. |
| Aqua Chat Template | 12.6(1) | None | Aqua template for chat is deprecated in ECE 12.6(1) release. Upgraded customers can continue to use the template. But no new
                                       features will be available on these templates. |
| Reports Console | 12.6(1) | None | None |

| Feature | Effective from Release | Replacement |
|---|---|---|
| Abandoned Chat Notifications for partition users | 12.6(1) | None Note The abandoned chat notifications can only be sent to department users. | Note | The abandoned chat notifications can only be sent to department users. |
| Note | The abandoned chat notifications can only be sent to department users. |
| Context Service | 12.6(1) | None |
| Users administration section for PA administrator: Business Personal Miscellaneous | 12.6(1) | None Note If any of these fields are used in ECE 12.5, it will no longer be accessible in 12.6(1). | Note | If any of these fields are used in ECE 12.5, it will no longer be accessible in 12.6(1). |
| Note | If any of these fields are used in ECE 12.5, it will no longer be accessible in 12.6(1). |

| Note | The abandoned chat notifications can only be sent to department users. |
|---|---|

| Note | If any of these fields are used in ECE 12.5, it will no longer be accessible in 12.6(1). |
|---|---|