---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-release-gui-d2d7cee3aa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/release/guide/rcct_b_1501_cce-solutions-rns/rcct_m_1501_ece.html
retrieved_at: 2026-08-16T19:36:58.967144+00:00
---

Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1)

# Release notes for Cisco Contact Center Enterprise Solutions, Release 15.0(1)

Updated: April 30, 2025

Chapter: Cisco Enterprise Chat and Email

## Chapter: Cisco Enterprise Chat and Email

# Cisco Enterprise Chat and Email

## New Features

The following table lists the new features available for Enterprise Chat and Email in Release 15.0(1).

### APIs

Edit Activities API

Edit Activities API allows users with agent or supervisor roles to edit activities that are assigned to other users or are
                                 in a queue to which they do have access. The API can be used to edit the dueDate, priority, language and the custom attributes
                                 of an activity. User can modify only one activity at a time.

Get All Departments and Active Aliases

An API has been introduced to allow users to retrieve all departments and active aliases configured in a department while
                                 composing or replying to emails.

Enable and Disable Entry Points

New APIs have been added to enable or disable entry points for different channels at the same time. This allows users to have
                                 the flexibility to make a channel available as per their needs.

Enhance User Rest APIs to Return Role Details

API to get user roles based on user ID

Improved Search for Cases

Case Lookup API has been modified to enable users to search a case using the following attributes: Case Owner (Agent Id or
                                 Username), Department name, Creation Date and Last Modified Date.

Get Entry Point Details for Department API

The Get Entry Point API has been published to return entry point details for a department. This gets entry point IDs for specific
                                 departments.

Contact Search By Custom Attribute

A new Contact Person Search by Custom Attribute API has been published to return all the Contact Persons matching the attribute.

### Serviceability

Support for SYSLOG

SYSLOG support has been introduced in this release.  The application and services process START/STOP events can be recorded
                                 on SYSLOG server after configuring the server name of the syslog server via SA setting “Server name or IP od Syslog server”

Centralized log collection for HA and Distributed Deployments

A new method for centralized log collection has been introduced to improve log management in HA and fully distributed deployments.
                                 Now, all Java process logs from different servers are available in a central location on the FILE_SERVER. The logs are stored
                                 under:

<FILE_SERVER_INSTALLATION_DIR>\eService\logs<SERVERNAME> . Here, SERVERNAME represents the specific server type, such as application, services, or messaging.

## Updated Features

The following table lists the new features available for Enterprise Chat and Email in Release 15.0(1).

### Security and Compliance

#### GDPR Enhancements

API Support for Obfuscating Customer Data

API support for obfuscating customer data in compliance with GDPR has been introduced, extending the functionality of the
                                    existing GDPR utility. This feature provides users with a streamlined process for data anonymization, ensuring compliance
                                    with data protection regulations.

Data Extract Request Improvements

Enhancements have been made to GDPR data extract requests to include all activities, notes, and other relevant information
                                    for compliance purposes.

Custom Attribute based customer lookup

GDPR support for customer lookup based on custom attributes.

Configure Private Hosts & Proxy Server Settings

A setting has been introduced to configure proxy server settings and specify hosts that can bypass proxy requests for commercial
                                    setups.

This feature enhances supportability by providing users with more control over proxy configurations and host management.

#### Purge Enhancements

Reduction in Purge Time

Reduced the minimum time for a purge job from 90 days to 15 days. This saves storage space, reduces clutter, and gives users
                                    more control over purge.

Continue Purge of Email data with open activities

Users can now purge jobs even if open activities remain. A warning message will notify users of any open activities qualified
                                    by the criteria when saving the purge job for adding supportability.

#### Microsoft Graph API Support for O365

Support for Microsoft Graph API has been added to connect to O365 mailboxes. This feature enhances security and compliance
                                 by leveraging modern authentication methods. It is recommended to plan and follow the guidelines before upgrading from OAuth
                                 to Graph, if not already done.

#### OAuth Support for Default SMTP Settings

OAuth support has been introduced for the default SMTP server settings, allowing administrators to choose between basic and
                                 OAuth authentication and providing a more secure and modern authentication method for SMTP server settings.

#### OAuth 2.0 Support for GSuite Email Services

OAuth support for Gmail has been added to email services.

### Serviceability

Log File Compression & Configuration

Log management has been improved to allow for log files to be compressed. As part of this improvement, the 'Maximum Backups
                                 of Log Files' setting has been added to the Administration Console. This setting determines the number of zip files to be
                                 generated, which is 100 by default and can be increased up to 5000 if desired.

### Agent Experience

#### Email

Configurable Redirect Email Option

A new setting has been introduced to hide or unhide the Redirect email option in the ECE Agent gadget, allowing administrators
                                    to control the visibility of the reply options and providing flexibility in managing email handling options for agents.

Configurable Filter criteria and Sort Order for Email lookup during outbound emails

Administrators can now configure and customize the email addresses available to contact center agents for outbound emails.
                                    This feature provides flexibility in managing email addresses, improving agent efficiency and reducing errors.

Notify Agents to Respond to Latest Email Activity

For an inbound email activity, the following message is displayed in the Reply pane to prompt agents to respond to the latest
                                    email activity: You are not responding to the latest email in the thread. Click here for the latest email.

By clicking the link, the agents are redirected to the latest email activity. This allows agents to provide the most suitable
                                    assistance to customers by not missing out on any information from them in their most recent email reply.

Subject Line Consistency for Email Group Replies

The subjects of individual email activities are now retained when multiple emails are selected as a group to forward or reply
                                    in the Advisor Desktop.

#### Chat

Chat Auto-Accept

A new Chat Auto Accept setting has been introduced, allowing incoming chat requests to be automatically accepted by agents.
                                    This feature can be enabled or disabled for specific agents or queues, providing flexibility in chat handling.

Lower Minimum Time for Expiry Time of Auto-Pushback of Chats

The minimum time for the expiry time of auto-pushback of chats has been lowered to 5 seconds.

Increased Limit for Chat Quick Responses

The limit for chat Quick Responses per queue has been increased from 75 to 150 providing more flexibility in managing quick
                                    responses for chat interactions.

Support for Adding Custom Attributes for Mid-Chat Authentication

Customers can now pass certain customer-specific attributes that are specific to the activity in the SAML token during mid-chat
                                    authentication. After the authentication, these attributes are also reflected in the Agent Console.

Authenticated Customer Records

Existing unauthenticated customer details can now be automatically updated when the customer creates a chat as an authenticated
                                    customer using his/her email id.

#### Chat Templates

Chat Template Cookie Updates

The standard chat templates have been updated to comply with the European Union ePrivacy Directive, ensuring that cookies
                                    are only loaded after user interaction with the chat icon. This feature ensures that non-essential cookies are only used with
                                    consent from the user.

Support for Multiple Domains and Subdomains in Chat Template

Support for multiple domains and their subdomains has been added to the Aria chat template, addressing customer requirements
                                    for domain management.

Encrypted ECE Chat Communication

ECE Chat communication between customers and agents has been secured with encryption, ensuring end-to-end data protection.
                                    This feature addresses current security standards, safeguarding sensitive information during chat interactions.

#### Agent Console

Agent Availability

Agents now can view the Not Ready Reason Code in use and change it without marking themselves available for chat or email.
                                    Agents can now track their availability resulting in more accurate analytics.

Attachments Drag and Drop

In the Agent Console, users can now drag and drop attachments in both email and chat. Files are attached in the order they
                                    are uploaded when dropping multiple items. In the case that attached files exceed the size capacity, users receive an error
                                    message.

Chat Reply Pane Usability Improvements

Usability improvements have been made to the Chat Reply Pane to enhance the overall user experience. This includes:

More of the chat transcript is visible without scrolling

Screen names are displayed with more contrast

Activity Note Indicator for Pick Window

An indicator has been added to the pick window to inform agents that a note is attached to an activity. This helps make agents
                                    aware that information may require review before completing the activity.

Activity Body View in Search Results

The ability to view the activity body and details in a single pane in the Search window has been added. This feature enhances
                                    agent productivity by streamlining the process of viewing activity details.

### Integration

Enable Agent Sync Mechanism for Integrated Deployments

Integration between ECE and Unified CCE has been improved with the addition of a sync mechanism, which is used to handle when
                                 invalid agent state mismatch responses are sent by UCCE against task assignments. This feature is designed to ensure the current
                                 availability state of an agent is correctly matched in both environments.

A new setting has been added to allow administrators to determine the frequency at which the agent state sync mechanism automatically
                                 operates. Administrators can also set the threshold of the number of invalid agent state occurrences that are to be allowed
                                 before the system resyncs the agent availability states.

### Custom Attributes

Support Date Type of Custom Attribute

A new custom attribute is available supporting date and time data. This allows partners, developers, and customers to extend
                                 and personalize the eGain solution to better meet their needs.

String format Validation for Custom Attributes

String Data entered for custom attributes can now be validated by using the Validation Tab added to the custom attribute creation
                                 workflow.

Optimized Search with Custom Attributes

Users can now search using a “contains” custom attribute. This feature is disabled by default and can be enabled by the cloud
                                 team. Enhancements have been made to the search framework to improve performance and enable specific custom attributes for
                                 search.

## Deprecated Features

None.

## Removed and Unsupported Features

None.

## Third Party Software Impacts

For the list of third-party software, see Open Source Documents . Filter by Product/Release Name and Version to download the required Open Source document.

### Customers Also Viewed

- Configure Webex AI Agent for CCE