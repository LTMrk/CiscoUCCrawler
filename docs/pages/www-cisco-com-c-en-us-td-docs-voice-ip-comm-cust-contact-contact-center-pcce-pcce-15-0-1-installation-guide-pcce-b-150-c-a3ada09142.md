---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-installation-guide-pcce-b-150-c-a3ada09142
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/installation/guide/pcce_b_150_cisco_pcce_installationandupgrade_guide/orchestration.html
retrieved_at: 2026-08-21T12:09:39.667203+00:00
---

Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: CCE Orchestration

## Chapter: CCE Orchestration

# CCE Orchestration

## Overview

The Orchestration feature provides partners and administrators an option to automatically download software updates and simplify
                           the installation and rollback processes. The Orchestration framework is built within the Cloud Connect server that connects
                           to the Cisco hosted cloud software repository. This framework provides the ability to check and download new software updates as and when they are available and notify the
                              administrators via email about the new updates along with the release notes.

Orchestration currently supports installation and rollback of Cisco Engineering Specials (ES), Service Updates (SU), Minor
                           Releases (MR), Major Releases, and Microsoft Patches. Orchestration supports rollback of major releases only if the major
                           release of the CCE component supports rollback.

### Email Notification

The Cloud Connect server checks for new software updates daily at a predefined time. When the new
                              software updates are available, an email notification is sent. This email notification
                              consists of available software updates details along with the release notes and is
                              triggered to the administrators who have subscribed for it.

Email notifications are also sent to provide updates on the success and failure of any upgrade,
                              rollback, or switch forward procedure. These notifications include details such as:

Specific nodes on which the upgrade, rollback, or switch forward is
                                    initiated.

Cloud Connect server name from where the procedure is triggered.

Time (Cloud Connect server time) at which the procedure is started.

Details about build versions of the respective nodes. For example, for an upgrade
                                    procedure, it shows both the version from which it is upgraded (FromVersion) and
                                    the version to which it is upgraded (ToVersion).

Status of the procedure for respective nodes to indicate whether the procedure is
                                    successful or has failed; the subject line of the email indicates the overall
                                    status: success, failure, or partial success.

Cloud Connect server downloads the available software from Cisco software repository every day at the configured time. Email
                                    notification is triggered from Cloud Connect server to subscribed users with software download failure details. Also, Cisco
                                    software artifactory will trigger an email notification with entitlement or compliance failure details to the email address
                                    mapped to CCO ID that is used to generate the Artifactory Authentication Credentials .

The name of the deployment is shown in the subject line of the email,
                                                      depending on the configuration in the inventory file.

For patch install or rollback, email notifications are not sent to
                                                      indicate whether the procedure is successful or if it is a
                                                      failure.

## Orchestration in CCE Deployment

The Orchestration feature is part of the Cloud Connect node that is configured in the CCE deployment.

To access this feature, Cloud Connect must be added to the inventory in the Unified CCE Administration console.

For more information, see Configure Cloud Connect section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

### System Requirements

Cloud Connect should be on 15.0(1) or latest 15.0(1) SU.

Orchestration supports parallel patching of multiple selected nodes. To use this feature, ensure that the Cloud Connect instance
                                                is running version 15.0(1) SU1 or later.

Orchestration supports parallel upgrade, switch-forward, and rollback of multiple selected VOS nodes. To use this feature,
                                                ensure that the Cloud Connect instance is running version 15.0(1) SU2 or later.

Each CCE deployment is required to have a dedicated Cloud Connect for Orchestration.

For supported upgrade and patching scenarios, see Orchestration Support using Cloud Connect Server .

#### VOS Component Upgrade

Before you begin the VOS node upgrade from 12.6(1) to 12.6(2) or 15.0(1), check if the ucos.keymanagement.v02.cop.sgn is applied on the base version. If not, you must install it; else the upgrade will fail. Restart the VOS node after installing ucos.keymanagement.v02.cop.sgn .

Before you begin the VOS node upgrade from 12.5(1) to 12.6(2), check if the ucos.keymanagement.v01.cop.sgn is applied on the base version. If not, you must install it; else the upgrade will fail. Restart the VOS node after installing ucos.keymanagement.v01.cop.sgn .

The upgrade from 12.5(2) or 12.6(2) to 15.0(1) doesn't require any mandatory COP to be applied.

For the minimum software requirements to enable orchestration in 12.5(1), see the System Requirements section in the CCE Orchestration chapter in Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2) .

Refer to the Virtualization for Unified Contact Center Enterprise document and ensure the Virtual Machine resources are updated as per the recommended VM configuration before triggering the
                                             upgrade from Orchestration.

### Orchestration Support using Cloud Connect Server

Cloud Connect 15.0(1) or the latest 15.0(1) SU supports orchestration in the following scenarios:

Engineering Specials (ES) for Unified CCE 12.5(2), 12.6(x), and 15.0(1), along with Windows updates, can be orchestrated.

Software upgrades can be orchestrated from Unified CCE 12.5(2) or 12.6(x) to CCE 15.0(1) or 15.0(1) SU, and from CCE 15.0(1)
                                    to CCE 15.0(1) SU.

Software upgrades can be orchestrated from Unified CCE 12.5(x) to CCE 12.6(2), and from Unified CCE 12.6(1) to CCE 12.6(2).

Orchestration supports patch operations for all deployment sizes, including those exceeding 4,000 agents. Upgrades to Major
                                          Releases and Service Updates (SU) for VOS nodes are supported for all deployment sizes when Cloud Connect 15.0.1 SU2 or later
                                          is installed.

Upgrades for Windows nodes are currently limited to deployments of 4,000 agents or fewer.

### Parallel Running of CLI

Parallel running of the same or different CLIs on a Cloud Connect server is disabled for Orchestration. However, parallel
                              running of CLIs is allowed for the following commands:

set cloudconnect orchestration config

show cloudconnect orchestration config

utils image-repository show

utils deployment compatibility-check

utils deployment show in-progress

utils system inventory export

utils system inventory import

utils deployment show progress-HA

email configuration-related commands, see Configure Email Notification .

Attention

You cannot run the utils smtp test-connection command in parallel while the same or a different CLI command is actively running on the specific Cloud Connect node.

utils set software-download time

utils set software-download bandwidth

### Orchestration Deployment Task Flow

Generate the Artifactory Identity Token

Configure Identity Token Auto Rotation

### Administration Task Flow

### Maintenance Task Flow

### Deployment Tasks

#### CLI To Configure Orchestration Maximum Parallel Tasks

The maximum number of concurrent tasks to be executed across selected nodes during an orchestration operation can be configured.

##### Set Command Overview

Specify the allowed maximum number of parallel Orchestration tasks.

The value must be between 1 and the total number of onboarded nodes.

The maximum number of parallel tasks cannot exceed the number of nodes currently onboarded for orchestration.

The CLI validates the input and, upon successful validation, configures the specified max-parallel-tasks setting on the Cloud Connect server.

The utils set orchestration max-parallel-tasks command must be executed on the publisher node of the Cloud Connect server. After successful execution, the configuration
                                                      is automatically replicated to the subscriber node.

The configured maximum parallel tasks setting applies to Orchestration patch manager operations when Cloud Connect 15.0.1
                                                      SU1 or later is installed. This setting also applies to VOS upgrade, switch-forward, and rollback operations when Cloud Connect
                                                      15.0.1 SU2 or later is installed.

If this setting is not configured, Orchestration patch manager operations will default to using the maximum number of selected
                                                      nodes.

At least one node must be onboarded before configuring the maximum number of parallel tasks.

##### Show Command Overview

##### Reset Command Overview

The command resets the configured value to default for the maximum number of parallel Orchestration tasks on the Cloud Connect
                                                server.

The utils orchestration max-parallel-tasks reset-to-default command can only be executed on the publisher node of the Cloud Connect server. After successful execution, the configuration
                                                is automatically replicated to the subscriber node.

These CLI commands are available in Cloud Connect version 15.0 SU1 and later.

#### CLI to Enforce Deployment Cache Update

To initiate deployment cache update on Cloud Connect server, run the utils deployment cache initiate command.

Command

utils deployment cache initiate

Description

Expected Inputs

Step 1: Menu Selection

After triggering the command, you will be presented with a menu to choose the cache update type:

Choose the Deployment Cache update type:

Refresh Software Artifactory Cache Data

Refresh Deployment Nodes Cache Data

Refresh Cache to Add Missing Node Data

Refresh Both Deployment Nodes and Software Artifactory Cache Data

Step 2: User Confirmation

After selecting an option, provide confirmation to proceed with selected cache update option.

Expected Outcome

The deployment cache update can only be initiated from the publisher node. Once the update completes successfully on the publisher,
                                                   the cache data is automatically replicated to the subscriber node.

Periodic deployment cache updates occur daily at 5:00 AM, or at a time configured by the administrator. Use this CLI to initiate
                                                   a cache update if needed before the next scheduled update, or after any manual upgrade or patch operations are performed on
                                                   the nodes.

Orchestration operations are not allowed during a cache update. The time required to complete the cache update varies based
                                                   on the number of nodes or component types that need to be updated.

This CLI only initiates the cache update and the actual update starts after the prerequisites are met. Please check the cache
                                                   update status using the utils deployment cache status CLI.

Below are the Supported Cache Update Types

This CLI command is available in Cloud Connect version 15.0 SU1 and later.

#### CLI to Check Status of Orchestration Deployment Cache

To check the status of the Orchestration deployment cache, run the utils deployment cache status command. This command provides insights into the cache's creation, update, and synchronization status.

Expected Input

Not applicable

Expected Outcome

The output varies depending on whether the command is executed on a publisher or subscriber node.

When executed on a Publisher node:

The command displays the following information:

Last Known Cache Scheduled-Job Status:

Status : Indicates the state of the last cache operation triggered by deployment cache scheduled job. Periodic deployment cache update
                                                         happens everyday at 5 AM or at the time configured by admin.

Triggered at : The date and time when the scheduled job was triggered.

Unreachable node(s) during scheduled job cache operation : Lists any node(s) that were unreachable during the scheduled cache operation.

Cache data missing for node(s) during scheduled job cache operation : Lists any node(s) for which cache data is missing during the scheduled cache operation.

Last Known Cache CLI Status:

Status : Indicates the state of the last cache operation triggered by utils deployment cache initiate CLI command.

Triggered at : The date and time when the CLI command was triggered.

Unreachable node(s) during CLI-triggered cache operation : Lists any node(s) that were unreachable during the CLI-triggered cache operation.

Cache data missing for node(s) during CLI-triggered cache operation : Lists any node(s) for which cache data is missing during the CLI-triggered cache operation.

Last Known Status of Cache Sync from Subscriber to Publisher:

Status : Indicates the status of the last cache synchronization from Cloud Connect subscriber to publisher.

Completed at : The date and time when the last synchronization was completed.

When executed on a Subscriber node:

Last Known Status of Cache Sync from Publisher to Subscriber:

Status : Indicates the status of the last cache synchronization from Cloud Connect publisher to the subscriber.

Completed at : The date and time when the last synchronization was completed.

This CLI command is available in Cloud Connect version 15.0 SU1 and later.

#### CLI to Configure Orchestration Scheduled Jobs

Orchestration job schedules are configurable. The following CLI commands are available to manage these settings:

utils orchestration-job update schedule : Modifies the default schedule or updates an existing orchestration job schedule .

utils orchestration-job show schedule : Displays the current orchestration job schedule configuration.

utils orchestration-job reset schedule : Restores the schedule configuration to the default settings.

Choose the orchestration scheduled job you want to update from the options below:

Software Download from Cisco Artifactory

Deployment Cache Update

Software Update Email Notification

Auto-rotate Cisco Artifactory Token

For your selected job, the CLI displays the current schedule and prompt you to enter new values for hours (0-23) and minutes
                                             (0-59). Press Enter to keep the current value for either field.

The CLI then displays the updated schedule and ask for confirmation (yes/no) before applying the changes.

Expected Output

The system displays a message indicating whether the update to the scheduled job configuration succeeded or failed.

The table below shows the default schedules for existing Orchestration jobs. The system automatically checks whether your
                                             preferred new schedule conflicts with other scheduled jobs or overlaps with their estimated completion times.

Orchestration Job

Default Schedule

Default Maximum Estimated Duration

Software Download from Cisco Artifactory

2:00 AM

3 hours

Deployment Cache Update

5:00 AM

2 hours

Software Update Email Notification

1:00 AM

1 hour

Auto-rotate Cisco Artifactory Token

12:30 AM

10 min

Cisco recommends adjusting the default schedule times to meet your specific requirements.

Ensure that you configure the schedule times for relevant jobs independently on both the Cloud Connect publisher and subscriber
                                                   nodes.

When scheduling an Orchestration job, select times that do not conflict with other automated jobs. Allow sufficient time between
                                                   tasks based on their expected duration. If a new schedule overlaps with an existing Orchestration job, the CLI will reject
                                                   the update.

Cisco recommends configuring different software download schedules for the Cloud Connect publisher and subscriber, preferably
                                                   with a one-hour interval between them. For example, if the Cloud Connect publisher is set to download at 3:00 AM, schedule
                                                   the Cloud Connect subscriber for 4:00 AM. This approach helps optimize network bandwidth usage.

Command

utils orchestration-job show schedule

Description

Displays the current schedule for orchestration-related scheduled jobs configured on the system.

Expected Input

None required

Expected Output

Shows the current schedule of all orchestration-related scheduled jobs set up on the system.

Command

utils orchestration-job reset schedule

Description

Restores orchestration-related scheduled jobs to their default schedules.

Expected Input

Displays the current and default schedules for all configured orchestration-related jobs, then prompts you to confirm the
                                             reset.

Expected Output

After confirmation, the system restores the orchestration jobs to their default schedules and shows a success message.

These CLI commands are available in Cloud Connect version 15.0 SU1 and later.

#### CLI to configure proxy for orchestration

You can enable proxy configuration for orchestration to check and fetch updates from the Cisco-hosted cloud artifactory.

To configure the proxy for orchestration, run the set cloudconnect orchestration config command. To view the proxy configured for orchestration, run the show cloudconnect orchestration config command.

At the Proxy Configured prompt, enter Yes to enable the proxy or No to turn off the proxy.

If you choose to enable the proxy, you’ll be prompted to enter the Proxy Host and Proxy Port details.

Proxy Host should be the proxy-server FQDN or IP address.

The proxy is turned off by default.

Orchestration supports only HTTPS proxy (That understands the HTTP CONNECT command).

You can run this command only from the publisher node of the Cloud Connect server. The proxy configuration replicates automatically
                                             from the publisher node to the subscriber node when the set cloudconnect orchestration config command is run successfully on the publisher node.

#### CLI to configure authentication method for artifactory

Configuration of authentication method (Identity Token) is required for connecting to Cisco Artifactory from Cloud Connect.

Command

utils image-repository authentication-type set

Description

This command configures the authentication method (Identity Token) required for connecting to Cisco Artifactory from Cloud
                                                Connect.

Expected Inputs

CLI displays the currently configured authentication method and user confirmation is required to proceed to switch the authentication
                                                method.

Expected Outcome

Displays message on the CLI if the authentication method configuration is a success or a failure.

Identity Token is the default authentication method that is configured in release 15.0(1)SU2 and later.

You can run this command only from the publisher node of the Cloud Connect server. When the utils image-repository authentication-type set command runs successfully on the publisher node, the authentication method configured on the publisher node is replicated
                                                      automatically on the subscriber node.

After configuring the authentication method using the utils image-repository authentication-type set command, configure Identity Token by running the utils image-repository set command.

#### Generate Artifactory Authentication Credentials

Artifactory supports authentication via Identity Token. For details on configuring the authentication method, refer to the
                                 section CLI to configure authentication method for artifactory

The CCO ID used to generate Artifactory authentication credentials must possess valid software entitlements, such as an active
                                                   SWSS (service contract) or Flex subscription.

Cisco recommends generating unique credentials for each distinct deployment (e.g., test, staging, production) using different
                                                   CCO IDs. However, within a single deployment, the same credential can be shared between the Cloud Connect publisher and subscriber.

#### Generate the Artifactory Identity Token

Follow these steps to generate an Artifactory Identity Token:

Access https://devhub-download.cisco.com/console using your CCO credentials.

Navigate to the Manage Identity Token page.

Click Generate or Regenerate Token .

Click Copy to save the Identity Token to your clipboard.

Ensure you save the token immediately. For security reasons, the token will not be displayed after you confirm the copy action.

If necessary, you can use the Revoke Token option on the Manage Identity Token page to invalidate existing tokens.

##### Renewing Identity Tokens

Automatic Rotation : Enable Identity Token Auto Rotation to keep the tokens secure and up to date without manual intervention. For configuration details, refer to the Configure Identity Token Auto Rotation section.

Manual Regeneration : Log in to https://devhub-download.cisco.com/console/ , click Regenerate Token , and then update the configuration by running the utils image-repository set command.

For detailed instructions on configuring authentication credentials, refer to the section CLI to Configure Artifactory URL and Artifactory Authentication Credentials

#### Configure Identity Token Auto Rotation

Command: utils image-repository authentication-token auto-rotate

Use this command to enable, disable, or configure the automatic rotation of the Cisco Artifactory Identity Token. This feature
                                    ensures that orchestration tokens are refreshed automatically before they expire. Auto-rotation is enabled by default in release 15.0(1)SU2 and later.

Use this command to enable, disable, or configure the automatic rotation of the Cisco Artifactory Identity Token. By default,
                                                auto rotation is disabled.

User confirmation to proceed with enabling or disabling identity token auto rotation.

If you choose to enable auto-rotation, the CLI will prompt for the following settings:

Rotation Trigger: The number of days before token expiry to initiate rotation (Range: 1–30 days; Default: 30).

Failure Notification: The number of days before token expiry to begin sending failure alert emails (Range: 1–10 days; Default: 10).

CLI will display a success or failure message confirming the status change or configuration update.

Schedule: When auto-rotation is enabled, the system checks daily at 12:30 AM Cloud Connect Publisher time whether the Identity Token
                                                      meets the configured number of days before expiry for auto-rotation. If the criteria is met, the system attempts to rotate
                                                      and configure the Identity Token accordingly.

Prerequisite: Ensure Artifactory is configured to use Identity Token as the authentication method before enabling this feature.

Manual Management: If auto-rotation is disabled, tokens must be managed and rotated manually.

Notifications: Automated email notifications are sent by the system when an Identity Token auto-rotation succeeds or fails. However, these
                                                      emails are only triggered if email notifications are configured for orchestration.

Node Restrictions: You can run this command only from the publisher node of the Cloud Connect server.

Identity Token has been supported as an authentication method for Cisco Devhub Artifactory starting from Cloud Connect version
                                                15.0(1). The Identity Token auto-rotation feature is available from Cloud Connect version 15.0(1) ES202511 onwards.

#### CLI to Configure Artifactory URL and Artifactory Authentication Credentials

Cisco hosts all the software artifacts in a cloud-based artifactory. The Cloud Connect server uses this artifactory to download
                                 and notify new updates.

Configure the Cloud Connect server with Cisco-hosted software Artifactory URL, Repository Name, and Artifactory Authentication Credentials . Run the command utils image-repository set . Refer to the Set Command table.

To view the configured Artifactory URL, Repository Name, and Artifactory Authentication Credentials in the Cloud Connect server, run the command utils image-repository show . Refer to the Show Command table.

You can run the utils image-repository set command only in the publisher node of the Cloud Connect server. The replication of image repository configuration occurs
                                             automatically from the publisher node to the subscriber node when you run this command with successful results on the publisher
                                             node.

Before running the command utils image-repository set on the CLI, access the link https://software.cisco.com/download/eula and accept the End User License Agreement (EULA)

Artifactory supports authentication via an Identity Token. For detailed instructions on configuring the authentication method,
                                             refer to the section CLI to configure authentication method for artifactory .

If the Cisco.com ID used to generate the Artifactory Authentication Credentials has entitlement to download the Cisco Contact Center software.

If the EULA is signed by the Cisco.com ID that generates the Artifactory Authentication Credentials .

If the Cisco.com ID that generates the Artifactory Authentication Credentials has the customer company's full address that is updated in the Cisco.com profile and validated by Cisco.

If the Cloud Connect server is deployed in embargoed countries where software download is restricted.

If the user has valid Authentication Credentials.

If the Artifactory authentication method is set to Identity Token and the authentication credentials are invalid, regenerate
                                                                     the Identity Token and update the authentication credentials on Cloud Connect. For detailed instructions, refer to the section Generate the Artifactory Identity Token .

If compliance validation fails, the Cisco.com ID user must perform the below-mentioned actions:

For EULA compliance failure, confirm that you have read and agreed to be bound by the terms of Cisco EULA. Access the link https://software.cisco.com/download/eula to view and accept the agreement.

For customer company's address verification failure, access the link https://rpfa.cloudapps.cisco.com/rpfa/profile/profile_management.do to update the address.

For Entitlement failure, where Cisco service contract information indicates that you're not authorized to download the Contact
                                                   Center software, perform one or more of the following actions:

Identify the product name and MDFID of the Contact Center product for which the entitlement failed. To find the product name
                                                         and corresponding MDFID of the product, check the CLI log for the keyword Entitlement check failed for MDFID . Refer to the Serviceability section for the command to retrieve the CLI log.

The service contract or subscription containing coverage for the product may not be associated to the Cisco.com user ID. To
                                                         associate the relevant service contract to the Cisco user ID, use the Cisco Profile Manager , and select Add Access to request access to the contract (which can now be done using the Serial Number of the product).

If your software is covered by a Smart License subscription, go to Cisco Software Central to request access to your company's
                                                         Smart Account in the Administration section.

Contact your Cisco representative, partner, or reseller to ensure that the product is covered by a service contract or subscription
                                                   that is associated with your Cisco.com user ID. Use the Partner Locator link to locate your nearest partner.

For assistance, contact your Cisco Accounts Manager or Partner.

To expedite your request, include the following information:

User ID (Cisco.com ID used to generate the Artifactory Authentication Credentials)

Contact Name

Company Name

Contract Number

Product ID or MDFID, Product Name, and Release

You can obtain access to U.S. export-restricted software by completing the K9 agreement form .

Upon successful configuration of artifactory details, artifacts are downloaded locally to the Cloud Connect server periodically
                                                               at the configured time. During artifact download, the compliance validation is done. The Cisco.com ID user performs the above-mentioned
                                                               actions for any compliance failure during artifact download.

User should input Artifactory URL, Artifactory Repository Name, and Artifactory Authentication Credentials .

The Cisco-hosted software Artifactory URL is https://devhub-download.cisco.com/binaries and Artifactory Repository Name is ent-platform-release-external .

CLI provides an option to the customer to choose between using export-restricted and unrestricted software, based on the entitlement
                                             associated with the Cisco.com ID. For example, VVB has export-restricted and unrestricted software.

Use the command utils image-repository set to change export-restricted or unrestricted software in the deployment. Use the CLI utils initiate software-download to enforce the cleanup and download the restricted vs unrestricted software.

On the successful configuration of artifactory details, artifacts are downloaded locally to the Cloud Connect server at the
                                             scheduled or default time. Orchestration operations such as patch install, rollback, or upgrade can be performed only after
                                             the artifacts are downloaded. If you need to download the artifacts immediately after the configuration, use the utils initiate software-download CLI. Usage of orchestration-related CLI is blocked during download, and this duration depends on the number of artifacts
                                             to be downloaded.

#### Onboard VOS Nodes to Orchestration Control Node

The onboarding process helps to establish a password-less connection between the Cloud Connect node and the VOS nodes.

Prerequisites :

Ensure that the Cloud Connect server and target nodes maintain the minimum
                                       software versions that are required as outlined in System Requirements .

If you are using self-signed certificates, import the self-signed Tomcat
                                       certificate of the Cloud Connect server into the VOS nodes which you have to
                                       onboard. Ensure to import both Cloud Connect publisher and subscriber node
                                       certificates on all VOS publisher and subscriber nodes. For details, see Self-Signed Certificate .

To onboard Finesse, CUIC, VVB, IDS, LD to a Cloud Connect server, run the utils system
                                    onboard initiate command from the publisher node of the respective VOS
                                 cluster that you wish to onboard. The publisher node of the Cloud Connect server must be
                                 up and running when onboarding is initiated from VOS node. When the onboarding is
                                 initiated from VOS node, FQDN of the Cloud Connect server must be used.

Cloud Connect server FQDN

Cloud Connect application username

Password

If the system (cluster) onboards to the Cloud Connect server with partial error,
                                             check the reason for the error and correct it. Then, run the utils system
                                                onboard update command instead of running the utils system
                                                onboard initiate command.

Onboarding is allowed only when all the publisher and subscriber nodes in the Cloud
                                             Connect server are reachable.

If the Cloud Connect server is corrupted and redeployed by doing fresh install, the
                                             administrator has to run utils system onboard remove from the VOS
                                             node and then run utils system onboard initiate to onboard the
                                             VOS nodes again.

After every successful onboard on Cloud Connect version 15.0(1) SU1 or later, refresh the deployment cache by executing the utils deployment cache initiate command on the Cloud Connect publisher node. Alternatively, the cache will update automatically during the next daily scheduled
                                             update.

#### Onboard Windows nodes to orchestration control node

The onboarding process helps to establish a password-less connection between the Cloud Connect node and the Windows nodes.
                                    To onboard the Windows-based nodes to orchestration control node, perform the following steps:

Step 1

Configure SSH public key on the Windows nodes by following the steps in the section Configure SSH public key on Windows nodes .

Step 2

From the cloud connect server, run the utils system inventory export command to download the inventory to an SFTP server. For details, see Export and Import of Nodes Managed by Orchestration Control Node .

Step 3

Edit the inventory file to include the Windows components. Refer to the default template section in the inventory file.

The syntax, alignment, and indentation must be exactly the same as mentioned in the inventory file.

Ensure the CRLF line endings are of UNIX-Style. Use a Linux-based or a Mac OS-based editor to create the Windows inventory
                                                                  file.

The following fields in the inventory file are mandatory.

Field

Description

ProductName

The ProductName mentioned in the inventory file must be in uppercase and cannot be changed. For example, CVPREPORTING, CVPSERVER, CVPOAMP,
                                                            DISTRIBUTOR, LOGGER, PG, ROGGER or ROUTER.

Pair under product

This is a user-defined pair name.

Hostname

This can be a valid IP, or hostname, or FQDN name of the target node.

Side of the deployment

It can either be A or B.

User configured on host

This is the username for which the SSH keys are configured in Step 1.

User name can be in User Principal Name (UPN) format or Domain username (domain\username) format for domain administrator
                                                                        or local administrator user name.

Example:

UPN format : administrator@stooges.icm

Domain Administrator: stooges\administrator

Local Administrator: administrator

Step 4

Import the inventory back from the SFTP server by running the command utils system inventory import on the Cloud Connect publisher node. For details, see Export and Import of Nodes Managed by Orchestration Control Node .

#### Add Deployment Type and Deployment Name

Step 1

Download the inventory to an SFTP server by running the utils system inventory export command. For details, see Export and Import of Nodes Managed by Orchestration Control Node .

Step 2

Edit the following strings in the inventory file, if
                                                required.

deploymentType : This field is used for compatibility check during an upgrade or rollback or switch forward procedure.

Ensure that the values entered in this field conform to the below format. The deployment type is case sensitive. For Example:
                                                      UCCE-4000-Agents.

By default, deployment Type will be UCCE-2000-Agents, update it to the correct value to realise some Orchestration features.
                                                                  If you want to scale more than 24000 agents for UCCE, set it as UCCE-24000-Agents only.

HCS-CC-2000-Agents

HCS-CC-4000-Agents

Orchestration is not supported for 12000, 24000 and 36000 agent deployment models. HCS-SCC (Small Contact Center ) deployment model is currently not supported for Orchestration.

Ensure that the values entered in this field conform to the above format. The deployment type is case sensitive.

deploymentName :
                                                      Provide a unique name for the deployment.

The administrator can update or edit the default
                                                            values, if required, based on their deployment
                                                            type and preferred deployment name.

Step 3

Import the inventory back from the SFTP server by running the
                                             utils system inventory import command on the Cloud Connect
                                             publisher node. For details, see Export and Import of Nodes Managed by Orchestration Control Node .

#### Validate Onboarded Nodes for Orchestration

To validate the onboarding of VOS and Windows nodes, and to check whether the Orchestration feature is ready to be used, run
                                 the utils deployment test-connection command.

#### Configure Email Notification

If an email notification is configured, the Cloud Connect server checks the Cisco-hosted artifact
                                 repository  periodically at scheduled times and sends email notifications
                                 along with the release notes when new software updates are available.
                                 Administrators can decide when to apply a patch or perform an upgrade. Email
                                 notifications are not triggered if no new software updates are
                                 available.

The SMTP server referred to in this section is the mail server that is used within
                                             the customer organization for their internal email communication.

Perform the following procedures in the same sequence as given here.

##### Set up Email Notification

Configure the email notification by running the following set of commands:

Set the IP address or hostname of the SMTP server by running the set smtp-host command.

Set the email address from which emails are triggered by running the set smtp-from-email command.

Enable or disable SMTP authentication by running the set smtp-use-auth command.

Set the username to be used for SMTP server connection by running the set smtp-user command. This is an optional configuration that needs to be set only when the SMTP authentication is enabled.

Set the password for SMTP server connection by running the set smtp-pswd command. This is an optional configuration that needs to be set only when the SMTP authentication is enabled.

##### Validate Email configuration

Validate the email configuration by running the utils smtp test-connection command.

utils smtp test-connection

This command is used to check the connection to the SMTP server using the configured parameters. You can also trigger a test
                                                email notification from Orchestration to validate the SMTP configuration.

Yes or No

A confirmation to trigger a test email to validate the SMTP configuration.

Shows whether the SMTP connection is successful or not.

If the connection is unsuccessful, displays the details of the missing or invalid SMTP mandatory configuration.

If the connection is successful, displays a confirmation message and provides an option to send a test email. As per the confirmation,
                                                displays whether the test email is successfully triggered to the configured subscribers.

##### Subscribe to Email Notification

Subscribe to email notifications by running the utils smtp subscribe command.
                                    Specify the email addresses to which the email notifications must be sent.

```
utils smtp subscribe <emailaddress1,emailaddress2,.....emailaddressesN>
```

#### Configure Windows Server for Updates (Optional)

Microsoft Windows update configuration needs to be done on the target Windows node. Microsoft Windows updates can be downloaded
                                 in one of following ways on the target Windows node:

by directly connecting to the Microsoft server;

from the Windows update server configured. To deploy or configure Windows server
                                       update services, refer to https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/deploy/deploy-windows-server-update-services .

### Administration Tasks

Before upgrade or rollback of nodes managed by Orchestration, make sure to take
                                          backup as suggested by respective component documentation. Backup has to be done
                                          manually.

In case the upgrade or rollback on VOS node fails, then the respective VOS node
                                          restart is mandatory before attempting the next upgrade or rollback on the same
                                          node. If the administrator does not restart, the next attempt to upgrade or rollback
                                          might fail.

#### Check Installed Software Version and Patches

To check the currently installed software version and patches on a node or group of nodes or all nodes in either Windows
                                 or VOS systems, run the utils deployment show status command.

#### Install or Roll Back Patch or Upgrade Cloud Connect Server

To install a patch or to roll back a previously installed patch on Cloud Connect server or to upgrade Cloud Connect Server to next available version , run the utils system upgrade initiate command. The Local Repository option in this command lists the patches and upgrade options available from Cisco artifactory for patch install or rollback or upgrade on Cloud Connect server. This command can be run separately on the Cloud Connect publisher and subscriber nodes.

The Cloud Connect publisher should be upgraded before upgrading the subscriber. The
                                             switch version on publisher should be done first before doing switch version on
                                             subscriber, use utils system switch version command to switch
                                             between versions.

Select the patch to install or roll back or upgrade option to upgrade Cloud Connect server .

The Local Repository option is used only after the Cisco Artifactory is successfully configured on Cloud Connect server. See CLI to Configure Artifactory URL and Artifactory Authentication Credentials for configuring Cisco artifactory.

Optionally, to receive email notification about the status of the patch installation
                                             or rollback or upgrade for
                                             Cloud Connect server, provide the SMTP host server details when prompted by the
                                             CLI.

Patch install or rollback or upgrade on Cloud Connect server initiated using utils system upgrade initiate command can be canceled using utils system upgrade cancel command. The utils system upgrade status command can be used to check the status.

Use the CLI command utils initiate software-download to download the Unified ICM and Unified CVP 15.0(1) software to the Cloud Connect Server after upgrading Cloud Connect to 15.0(1) or 15.0 SU1 for both publisher and subscriber nodes. Alternatively, wait for the default or scheduled software download to finish before
                                             starting the Unified CVP/ICM upgrade to 15.0(1).

#### List Available Patches for Specific Node or Group of Nodes

To get a list of available patches for a specific node or group of nodes in the inventory, run
                                 the utils patch-manager list command.

#### Install Patch to Specific Node or Group of Nodes

To install patch to a specific node or group of nodes, run the utils patch-manager install command.

Expected Inputs

Select the node or group of Windows or VOS nodes on which the patch needs to be installed. After you select the nodes, only
                                                the nodes containing the patches are displayed. For example, if you select 3 nodes and Windows or VOS patches are available
                                                for only 1 of them, you are asked to proceed with only one node. Confirm to proceed. You are also asked to confirm whether
                                                the target node needs to be rebooted after installing the patch.

The Patch Install Orchestration CLI is supported with enhanced options for platform selection from 15.01 SU1 release:

All Side A VOS node and All Side B VOS nodes under the VOS platform.

All Side A Windows node and All Side B Windows nodes under the Windows platform.

These new options enable parallel patch installation operations on either all Side A or all Side B nodes (Windows/VOS) within
                                                the deployment.

Selection of components such as Finesse, CVP Call Server, IdS, PG, Router, and Rogger that are running on supported version
                                                of the maintenance mode, will provide the options "With maintenance mode” and “Without maintenance mode”. For details on maintenance
                                                mode supported version and prerequisites, see the Initiate maintenance mode for a specific nodes .

If you select a group of nodes with some nodes on maintenance mode supported version and some nodes on unsupported version,
                                                then "With maintenance mode” or “Without maintenance mode” option is not available. If maintenance mode option is required,
                                                select the respective node which is on maintenance mode supported version.

If you select “With maintenance mode” option, the maintenance mode is initiated for the selected node to failover active traffic
                                                gracefully or shutdown the services gracefully without interrupting the active traffic or causing outage for new traffic before
                                                installing the update and automatically rebooting. If you select, “Without maintenance mode” option, you are initially asked
                                                to confirm to proceed.

Next, you are asked to provide confirmation on rebooting the node after installing the patch.

To start Unified ICM services, post the successful completion of patch install with reboot on Unified ICM nodes. See Start ICM Services .

You can check the status of the patch install which is currently in-progress. For more information, see Check Status .

Maintenance mode for IDS co-resident in 2000 Agents Deployment model is not supported

Prerequisites for All Side A/B options

Ensure you follow the considerations below when using the All Side A/B platform options in patch CLI commands.

Install mandatory 15.0.1 SU1 or later release to enable this enhanced platform selection for Orchestration patching operations.

Ensure to update Correct deploymentType in the inventory. For more information, see Add Deployment Type and Deployment Name section on updating the deployment Type.

Ensure side information for VOS nodes to be present in the inventory to enable this option.

If you plan to use the enhanced All Side A/B options immediately after installing the 15.01 SU1 release before the schedule job run, then it is recommended to update
                                          the deployment cache by running the utils deployment cache initiate command. This prepares the system for using the new options. If the cache is not updated, you may experience inconsistent
                                          CLI behaviour. For more information, see CLI to Enforce Deployment Cache Update section.

For more information, see CLI To Configure Orchestration Maximum Parallel Tasks section for details on configuring the maximum number of nodes that can be processed concurrently during Orchestration patching
                                          operation.

Parallel patching is supported only for version 15.0 Quarterly Cumulative ES and above. For the VOS platform, this includes
                                                      Quarterly Cumulative ES and any common ES for all VOS components version 15.0 or higher.

The same operation cannot be performed simultaneously from both the Cloud Connect publisher and subscriber. For example, if
                                                      a patch operation is already triggered for All Side A VOS Nodes from the Cloud Connect publisher, that same option cannot be used for any patch operation triggered from the Cloud Connect
                                                      subscriber at the same time. However, you can patch all of Side A by running All Side A VOS Nodes from the Cloud Connect publisher and All Side A Windows Nodes from the Cloud Connect subscriber, or vice versa.

This option does not provide the ability to put nodes in maintenance mode before performing the patch operation for the All Side A/B option. If needed, place the relevant nodes in maintenance mode before starting the operation.

Patch operations using the All Side A/B VOS option cannot be performed simultaneously on both CUIC publisher and subscriber nodes. If both nodes are present on a given
                                                      side, only the expected nodes will be processed; any additional nodes will be skipped, as the operation must be completed
                                                      on the publisher before proceeding on the subscriber. You can retry the operation on any skipped nodes after the current operation
                                                      finishes.

#### Roll Back Patch from Specific Node or Group of Nodes

To roll back a previously installed patch on a specific node or a group of nodes, run the utils patch-manager rollback command.

In case of Windows-based nodes, the latest applied patch is allowed to roll back. In case of VOS-based nodes, the latest applied
                                                ES is rolled back.

Expected Inputs

From the list of Windows/VOS nodes displayed, select the node or group of Windows/VOS nodes on which the patch needs to be
                                                rolled back. Once you select the nodes, only the nodes for which Windows/VOS patch rollback is available will be displayed.
                                                For example, if you select 3 nodes and Windows/VOS patch rollback is available for only 1 of them, you are asked to proceed
                                                with only one node. There is also a message displayed indicating that the machine would restart after the patch is rolled
                                                back. Confirm to proceed.

The Patch Rollback Orchestration CLI is supported with additional options for platform selection when Cloud Connect is upgraded
                                                to 15.0.1 SU1 or later.

All Side A VOS node and All Side B VOS nodes under the VOS platform.

All Side A Windows node and All Side B Windows nodes under the Windows platform.

These new options enable parallel rollback of patches on either all Side A or all Side B nodes (Windows/VOS) within the deployment.

For more information, refer to Prerequisites for All Side A/B options section of Install Patch to Specific Node or Group of Nodes .

Selection of components such as Finesse, CVP Call Server, IdS, PG, Router, and Rogger that are running on supported version
                                                of the maintenance mode, will provide the options "With maintenance mode” and “Without maintenance mode”. For details on maintenance
                                                mode supported version and prerequisites, see the Initiate maintenance mode for a specific nodes .

If you select a group of nodes with some nodes on maintenance mode supported version and some nodes on unsupported version,
                                                then "With maintenance mode” or “Without maintenance mode” option is not available. If maintenance mode option is required,
                                                select the respective node which is on maintenance mode supported version.

If you select “With maintenance mode” option, the maintenance mode is initiated for the selected node to failover active traffic
                                                gracefully or shutdown the services gracefully without interrupting the active traffic or causing outage for new traffic before
                                                rollback and automatically rebooting. If you select, “Without maintenance mode” option, you are initially asked to confirm
                                                to proceed.

Next, you are asked to provide confirmation on rebooting the node after rollback.

To start Unified ICM services, post the successful completion of patch rollback with reboot on Unified ICM nodes. See Start ICM Services

You can check the status of patch rollback which is currently in-progress. For more information, see Check Status .

#### Install Windows Updates to Specific Node or Group of Nodes

To install Windows updates to a node or group of nodes or all Windows nodes, run the utils patch-manager ms-patches install command.

Before running this command, refer to the recommended guidelines in the Microsoft Security Updates section of the Security Guide for Cisco Unified Contact Center Enterprise at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

Microsoft Windows updates are NOT hosted on Cisco-hosted Software Artifactory. You must configure the target Windows node
                                 to fetch the Microsoft Windows updates, either by directly connecting to the Microsoft Server via Internet or from the Windows
                                 Update Server. For more details, refer to the Configure Windows Server for Updates section. The utils patch-manager ms-patches install command will not list the available Windows updates for the administrator to choose for the target node. Instead, it will
                                 check the available updates for the below listed Windows update categories and install all the available updates:

Application

Connectors

DefinitionUpdates

DeveloperKits

FeaturePacks

Guidance

ServicePacks

Tools

UpdateRollups

CriticalUpdates

SecurityUpdates

Updates

The administrator can control the installation of Windows updates using Windows Update Server, instead of directly connecting
                                 to the Microsoft Server via Internet. Ansible log, generated during the running of utils patch-manager ms-patches install CLI, captures the details of the Windows updates, along with the Knowledge Base (KB) number of the updates that were installed
                                 on the target node. Refer to the Serviceability section for the command to retrieve the Ansible log.

Expected Inputs

From the list of Windows nodes displayed, select the node or group of Windows nodes or all Windows nodes to which the updates
                                             need to be applied. You can also select all the Windows nodes in the inventory. Once you select the nodes, only the nodes
                                             for which Windows updates are available will be displayed. For example, if you select 3 nodes and Windows updates are available
                                             for only 1 of them, you are asked to proceed with only one node. Confirm to proceed. You are asked to confirm whether the
                                             target nodes needs to be rebooted after installing the updates.

Selection of components such as Finesse, CVP Call Server, IdS, PG, Router, and Rogger that are running on supported version
                                             of the maintenance mode, will provide the options "With maintenance mode” and “Without maintenance mode”. For details on maintenance
                                             mode supported version and prerequisites, see the Initiate maintenance mode for a specific nodes .

If you select a group of nodes with some nodes on maintenance mode supported version and some nodes on unsupported version,
                                             then "With maintenance mode” or “Without maintenance mode” option is not available. If maintenance mode option is required,
                                             select the respective node which is on maintenance mode supported version.

If you select “With maintenance mode” option, the maintenance mode is initiated for the selected node to failover active traffic
                                             gracefully or shutdown the services gracefully without interrupting the active traffic or causing outage for new traffic before
                                             installing the update and automatically rebooting. If you select, “Without maintenance mode” option, you are initially asked
                                             to confirm to proceed.

Next, you are asked to provide confirmation on rebooting the node after installing the patch.

The utils patch-manager ms-patches install operation may require a considerable amount of time to complete, depending on the number of Windows updates available on
                                             the target node.

#### Roll Back Windows Update from Specific Node or Group of Nodes

To roll back Windows update from a specific node or group of nodes or all Windows nodes, run the utils patch-manager ms-patches rollback command.

Before running this command, refer to the recommended guidelines in the Microsoft Security Updates section of the Security Guide for Cisco Unified Contact Center Enterprise at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

Listing of Windows updates available for rollback is not supported.

Expected Inputs

Select the node or group of Windows nodes or all Windows nodes on which the rollback needs to be performed. You can also select
                                             all the Windows nodes in the inventory for rollback. Provide the Knowledge Base (KB) number you want to rollback. Once the
                                             KB number is provided, only the nodes that are applicable for the rollback will be displayed. For Example, if you select 4
                                             nodes to roll back and the KB number provided is applicable for only one of them, you are asked to proceed with only one node.
                                             Confirm to proceed. You are asked to confirm whether the target nodes need to be rebooted after rollback.

Selection of components such as Finesse, CVP Call Server, IdS, PG, Router, and Rogger that are running on supported version
                                             of the maintenance mode, will provide the options "With maintenance mode” and “Without maintenance mode”. For details on maintenance
                                             mode supported version and prerequisites, see the Initiate maintenance mode for a specific nodes .

If you select a group of nodes with some nodes on maintenance mode supported version and some nodes on unsupported version,
                                             then "With maintenance mode” or “Without maintenance mode” option is not available. If maintenance mode option is required,
                                             select the respective node which is on maintenance mode supported version.

If you select “With maintenance mode” option, the maintenance mode is initiated for the selected node to failover active traffic
                                             gracefully or shutdown the services gracefully without interrupting the active traffic or causing outage for new traffic after
                                             rollback and automatically rebooting. If you select, “Without maintenance mode” option, you are initially asked to confirm
                                             to proceed.

Next, you are asked to provide confirmation on rebooting the node after rollback.

#### Enable or Disable Compatibility Enforcement

You can enable or disable compatibility enforcement. When the compatibility enforcement
                                 is enabled, it ensures that the upgrade, rollback, or switch forward is as per the
                                 compatibility matrix published by Cisco for reference design-based deployment. To enable
                                 or disable compatibility enforcement, run the utils deployment
                                    compatibility-check command.

By default, the compatibility enforcement is enabled.

When the compatibility enforcement is disabled, the Orchestration framework does not
                                             enforce upgrade, rollback, or switch forward as per the compatibility matrix
                                             published by Cisco.

You can run this command only from the publisher node of the Cloud Connect server.
                                             The compatibility configuration replicates automatically from the publisher node to
                                             the subscriber node when the utils deployment compatibility-check command is run with successful results on the publisher node.

#### Initiate maintenance mode for a specific nodes

Initiating maintenance mode allows the components to failover gracefully or shutdown the services gracefully (depending on
                                 the selected components) without interrupting the active traffic or causing outage to new traffic. This ensures that the system
                                 can be taken down for maintenance activity such as installing new software updates, restarting services etc. The maintenance mode is supported for PG, CVP server, IdS, Finesse, Router, and Rogger .

Pre-requisites for Maintenance Mode Support

Maintenance mode is supported for PG, CVP server, IdS, and Finesse if the target nodes are on 12.6(1) and above.

Maintenance Mode is supported for Router and Rogger if the target nodes are on version 15.0(1) and above, or if the target
                                       nodes are installed with 12.6(2) Router Component ES that is ES68 or higher.

To enable Maintenance Mode support for Router and Rogger in Orchestration, install Cloud Connect mandatory 15.0(1) ES202508 or above.

To initiate maintenance mode for a specific node in the inventory, run the utils
                                    system maintenance initiate command.

When run, this command prompts you to select a node based on the inventory.

If the selected nodes are Router or Rogger components, the following reasons are prompted for selection:

Microsoft Updates install or rollback

Engineering Special (ES) install

Engineering Special (ES) rollback

Maintenance Release (MR) install

Maintenance Release (MR) rollback

ISO or Major Release upgrade

Other Maintenance Activity (excluding patching or upgrade operations)

If you don't want to initiate maintenance mode for performing any operations mentioned in options 1 to 6, select option 7.
                                             Confirm to proceed with maintenance mode for the selected option.

If either the Publisher or Subscriber or the active/inactive node is already in maintenance mode in any of the components,
                                             the other server cannot be initiated for maintenance.

You can check the status of system maintenance initiate which is currently in-progress. For more information, see Check Status .

Maintenance mode for IDS co-resident in 2000 Agents Deployment model is not
                                             supported

#### List Available Upgrade Options

To get a list of available upgrade options for VOS and Windows nodes individually or for group of
                                 nodes or for all nodes in the
                                 inventory, run the utils upgrade-manager list command.

If the selected node or
                                             group of nodes or all nodes are already running the latest software
                                             version, a message is displayed to indicate that.

#### Upgrade a specific node or group of nodes

To perform software version upgrades on VOS or Windows nodes , run the utils upgrade-manager upgrade command from the Cloud Connect server. It’s recommended to run this command during a maintenance window as the procedure
                                 involves a system restart that causes a service outage.

To upgrade the selected VOS or Windows component, a compatibility check is performed in the background based on the configured
                                 deployment type. This ensures that all the associated components are onboarded . If the components are onboarded, the upgrade procedure begins either the required dependent components are in the same target
                                 upgrade version or backward compatible version. However, if the components are not onboarded, you have to onboard them first
                                 or if the versions are not compatible, upgrade them to the required version.

For example, if you select to upgrade the Rogger nodes to the 12.6(2) version, the intercomponent compatibility check is run
                                 for the Rogger dependent components such as Finesse, Cisco Unified Customer Voice Portal, VVB, and CUIC. These must already
                                 be in the 12.6(2) version and PG must be in the backward compatible version, that is, 12.5(2).

The subcomponents sequence dependencies aren’t validated as part of the upgrade compatibility. Refer to the upgrade guides
                                                   of the respective components for the correct sequence. For example, in Cisco Unified Customer Voice Portal, we have subcomponents
                                                   such as Operations Console, Unified Cisco Unified Customer Voice Portal Reporting Server, and Unified Cisco Unified Customer
                                                   Voice Portal Server. These must be upgraded in the required sequence.

Orchestration ensures 15.0(1) ICM and CVP are deployed on the supported Windows Operating System. Before upgrading ICM or
                                                   CVP to 15.0(1), ensure that the Windows Operating System is upgraded to a supported version. Else, Orchestration will not
                                                   allow the upgrade to 15.0(1). Refer to Unified CCE 15.0(1) Compatibility Matrix for the details on supported Windows Operating System for ICM and CVP.

CVP Reporting Server upgrade to 15.0(1) is not supported through Orchestration. For details on manually upgrading CVP Reporting
                                                   Server to 15.0(1), refer to the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal .

For the VOS node/cluster, switch forward is optional at the end of the upgrade. If administrators opt for switch forward,
                                 the target node is restarted and the active/inactive partition is switched. If they decide not to switch forward, the upgraded
                                 version remains in the inactive partition of the target node. Switch forward for these nodes can be performed later. For details,
                                 see Perform Switch Forward on Specific VOS Node or Group of Nodes .

For the VOS cluster, the upgrade or the switch forward procedure is performed first on the publisher and then on the subscriber
                                 nodes. If a switch forward is performed immediately after an upgrade, the overall procedure takes a significant amount of
                                 time; hence plan the maintenance window accordingly.

Prerequisites

Before upgrading the Unified CCE and its associated components, refer to the installation and upgrade guide for each component.
                                       This should be part of your deployment upgrade planning to address component-specific prerequisites, such as modifying resources
                                       based on OVA requirements, following Windows updates and antivirus recommendations, performing in-place Windows/SQL upgrades,
                                       identifying unsupported features, meeting backup requirements, and ensuring that components are deployed with valid, unexpired
                                       certificates.

The following prerequisites must be completed on Unified ICM and Unified CVP components before initiating the upgrade to a
                                       major release (for example, 15.0(1)) remotely through Orchestration. If the prerequisites aren’t completed, the Unified  ICM
                                       and Unified CVP ISO upgrade fails. After the prerequisites are completed, you must manually restart the nodes before initiating
                                       the upgrade from Orchestration.

Unified ICM and Unified CVP components

Username configured in the Orchestration inventory must not conflict with any local or domain user. For example, a domain
                                             administrator user may have conflicting local administrator user on the node.

Disable the Windows Defender Real-Time Protection . For more information, see https://learn.microsoft.com/en-us/defender-endpoint/configure-real-time-protection-microsoft-defender-antivirus

Windows should be up-to-date with the latest updates.

Disable the Windows update service.

To enable auto-logon, update the following registry keys. Use the username configured in the Cloud Connect inventory for this
                                             Virtual Machine when updating the below registry key value:

Update the following keys:

AutoAdminLogon - Set to value 1

DefaultDomainName - Provide Domain Name, if applicable

DefaultUserName - Provide the username which is configured in the Cloud Connect Inventory

DefaultPassword - Provide the password

Unified ICM components

All the User Account Control (UAC) group policies must be configured with the default value. However, you must update the
                                             following policies with the given value under Local Security Policy → Local Policies → Security Options in the Local Security Policy :

Behavior of the elevation prompt for administrators in Admin Approval Mode—Elevate without prompting.

Switch to the secure desktop when prompting for elevation—Disabled.

Security setting shouldn’t be marked as Not Applicable for any policy under Local Security Policy → Local Policies → Security Options in the Local Security Policy .

The following enhanced platform selection options are available when Cloud Connect 15.0.1 SU2 or later is installed:

All Side A VOS nodes and All Side B VOS nodes under the VOS platform.

These options allow the administrator to initiate the upgrade of all Side A or all Side B VOS nodes in parallel.

Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes below.

From the list of upgrade options available for the selected node, select the appropriate option and confirm. A compatibility
                                             check is then run in the background.

During Call Server upgrade to 15.0(1), the following details are prompted to the administrator:

Confirmation on whether manual backup of existing CVP installation folder and log files onto a different computer has been
                                                   completed.

Details required for X.509 certificate creation. You will be able to enter "Common Name" or use hostname as "Common Name"
                                                   for each of the selected nodes. Option is provided to enter X.509 certificate fields that are common to all the selected nodes.

If the selected node or group of nodes has either ROGGER, LOGGER or DISTRIBUTOR component for ICM and the selected upgrade
                                             option is a major release version (for example, 15.0(1)), you must confirm the following:

If EDMT has been run on the selected nodes. Else, you must log in to the selected nodes and run EDMT to migrate the database
                                                   to the required version before triggering the upgrade from Orchestration.

If the SQL Server Security Hardening must be applied on the applicable target nodes during the upgrade. You can also apply
                                                   Security Hardening settings after the upgrade by running the Security Wizard directly on the applicable target nodes.

Once the upgrade procedure begins, you can see the progress details for each of the computers. You can also see the elapsed
                                             time since the procedure started.

For faster upgrades, the Cloud Connect server downloads locally all the new
                                                   software updates from the Cisco hosted repository at a predefined time.

To start the Unified ICM services, post the successful completion of upgrade with reboot on Unified ICM nodes. See Start ICM Services .

The option to upgrade “All nodes” in the deployment (VOS and Windows nodes together) to CCE 15.0(1) via Orchestration is not
                                                   supported. The administrator can upgrade the individual components to 15.0(1) by selecting the respective VOS or Windows nodes.
                                                   All nodes option is currently supported only for upgrading to CCE 12.6(x)

By default, the selected operation is executed in parallel on all selected VOS nodes. To limit the number of nodes on which
                                                   the operation runs at the same time, configure the maximum parallel tasks value. For details, see the CLI To Configure Orchestration Maximum Parallel Tasks section.

You can check the status of the upgrade that is currently in-progress. For more information, see Check Status .

##### Prerequisites for All Side A/B VOS nodes option

Ensure you follow the considerations below when using the All Side A/B VOS nodes options in upgrade-manager CLI commands.

Cloud Connect must be running version 15.0.1 SU2 or later to use the All Side A/B VOS nodes option for Orchestration upgrade operations.

Side information for VOS nodes must be correctly mapped in the inventory. A node is included under Side A or Side B based
                                          on its side mapping in the inventory

The All Side A/B VOS nodes option relies on the internal deployment cache. The cache stores target node details such as installed versions and component types, along with available upgrade information
                                          from Artifactory. If the cache is outdated, CLI behavior may be inconsistent. If cache data is missing:

Deployments of 4,000 agents or fewer : The system attempts to fetch the required data directly from the node(s) and Artifactory.

Deployments exceeding 4,000 agents : Node(s) for which cache data is not available are skipped.

If you plan to use the All Side A/B VOS nodes option immediately after upgrading the Cloud Connect node and before the next scheduled cache update, run utils deployment cache initiate CLI to update the deployment cache.

Ensure the correct deploymentType is configured in the inventory. The deploymentType determines how the system handles missing or outdated cache data; whether it fetches data directly from target node(s) and
                                          Artifactory or skips node(s) where cache data is unavailable. An incorrect deploymentType may lead to unexpected CLI behavior during the operation. For more information, see the Add Deployment Type and Deployment Name section.

The All Side A/B VOS nodes option supports upgrade of target nodes to versions 15.0.1 and later.

The same node selection (for example, All Side A VOS nodes ) cannot be operated on simultaneously from both the Cloud Connect Publisher and Subscriber. If any upgrade or patch operation
                                                      is already in progress on the All Side A VOS nodes selection from the Publisher, the same selection is blocked on the Subscriber,
                                                      and vice versa, until the operation completes.

Simultaneous upgrade operations across alternate sides are also restricted. For example, if an upgrade operation is in progress
                                                      on All Side A VOS nodes from the Cloud Connect Publisher, then upgrade, rollback, or switch-forward operations on All Side B VOS nodes from the Cloud Connect Subscriber are blocked, and vice versa. However, patch install and rollback operations are not affected
                                                      and can proceed independently.

All Side A/B VOS nodes option does not provide the ability to put nodes in maintenance mode before performing the upgrade operations for the All Side A/B
                                                      VOS option. If needed, place the relevant nodes in maintenance mode before starting the operation.

Compatibility checks are not enforced by Orchestration for upgrade-manager operations on All Side A/B VOS nodes.

The Cloud Connect component is excluded from All Side A/B VOS nodes upgrade-manager operations.

When you select the All Side A/B VOS nodes option, Orchestration prompts you to perform the optional switch-forward operation at the end of the upgrade. If the selected
                                                      side includes publisher nodes, ensure that the switch-forward operation is performed in the required publisher-subscriber
                                                      sequence for the component. Performing switch-forward out of sequence may cause nodes to go out of cluster.

When using the All Side A/B VOS nodes option for upgrade, each node on the selected side is evaluated individually. Nodes for which the selected upgrade is applicable
                                                      are processed; nodes that are not applicable are skipped.

Upgrade operations using the All Side A/B VOS option do not run simultaneously on both the publisher and subscriber of the same VOS component (for example, CUIC). If both
                                                      the publisher and subscriber of a component are present on the selected side, the publisher is processed first and the subscriber
                                                      is skipped. You can retry the operation on skipped nodes after the current operation completes.

#### Perform Switch Forward on Specific VOS Node or Group of Nodes

Administrators can perform switch forward on target VOS nodes independently. When the active partition is on lower version
                                 and the inactive partition is on higher version, run the utils upgrade-manager switch-forward command to perform a switch forward. It is recommended to run this command during a maintenance window as the procedure involves
                                 system restart that will cause service outage.

The following enhanced platform selection options are available when Cloud Connect 15.0.1 SU2 or later is installed:

All Side A VOS nodes and All Side B VOS nodes under the VOS platform.

These options allow the administrator to initiate the switch-forward of all Side A or all Side B VOS nodes in parallel.

A compatibility check is then run in the background.

If there are components whose versions are not compatible or the components are not onboarded as per the compatibility requirements,
                                                   a list of those components is displayed. Upgrade or switch forward the listed components to the required software versions
                                                   and re-run this command.

If the versions of the associated components are compatible with the node’s inactive version, then the switch forward procedure
                                                   continues.

Once the switch-forward procedure begins, you can see the progress details for each of the machines. You can also see the
                                             elapsed time since the procedure started.

You can check the status of switch forward which is currently in-progress. For more information, see Check Status .

By default, all selected nodes under VOS platform option are processed concurrently. If you have a specific requirement to
                                             limit concurrency, the value can be configured. For details, see the CLI To Configure Orchestration Maximum Parallel Tasks section.

#### Roll Back upgrade from a specific node or group of nodes

To roll back an upgrade on VOS or Windows nodes, run the utils upgrade-manager rollback command from the Cloud Connect server. It’s recommended to run this command during a maintenance window as the procedure
                                 involves the system restart that causes a service outage.

For the selected VOS or Windows component for rollback, a compatibility check is performed in the background to ensure that
                                 all the associated components are onboarded and the versions are compatible. If the components are onboarded and the versions are compatible with each other, the rollback procedure
                                 begins. However, if the components aren't onboarded, you have to onboard them first or if the versions aren't compatible,
                                 roll them back to the required version.

For VOS nodes/cluster, the rollback (switch backward) must be initiated from an active higher version to an inactive lower
                                 version of the node. Also, the publisher node of the managed cluster must be rolled back before the subscriber node of the
                                 cluster.

Orchestration does not allow rollback from major release versions, for example, 15.0(1), for Unified ICM and Unified CVP components.
                                             However, CVP components can be manually rolled back from major release versions on the target node(s).

The following enhanced platform selection options are available when Cloud Connect 15.0.1 SU2 or later is installed:

All Side A VOS nodes and All Side B VOS nodes under the VOS platform.

These options allow the administrator to initiate the rollback of all Side A or all Side B VOS nodes in parallel.

If there are components whose versions aren’t compatible or if the components aren’t onboarded as per the compatibility requirements,
                                                   a list of these components is displayed. Roll back the listed components to the required software versions and then rerun
                                                   this command.

Uninstallation is not supported for both Unified ICM and CVP 15.0(1) via Orchestration; however, Unified CVP 15.0(1) can be
                                                   manually uninstalled. When compatibility checks are enabled, components with versions incompatible with Unified ICM 15.0(1)
                                                   or CVP 15.0(1) can't be rolled back to a previous version. This restriction is in place because Unified ICM 15.0(1) and CVP
                                                   15.0(1) don't support uninstallation. However, this restriction won't apply if compatibility enforcement is disabled. For
                                                   more details on compatibility enforcement, see Enable or Disable Compatibility Enforcement .

If the versions of the associated components are compatible with the selected node's rollback version, then the rollback procedure
                                                   begins.

To start Unified ICM services, post the successful completion of rollback upgrade with reboot on Unified ICM nodes. See Start ICM Services .

You can check the status of the rollback which is currently in-progress. For more information, see Check Status .

By default, all selected nodes under VOS platform option are processed concurrently. If you have a specific requirement to
                                             limit concurrency, the value can be configured. For details, see the CLI To Configure Orchestration Maximum Parallel Tasks section.

#### Check Status

To check the current status of patch manager install, patch manager rollback, upgrade manager upgrade, upgrade manager rollback,
                                 switch-forward, or system maintenance initiate , run the utils deployment show in-progress command. You can run this command if connectivity to CLI is lost after initiating any of above procedures.

If there is no procedure in progress, this command gives the last successful/failed procedure status.

If there is no active patch manager install, patch manager rollback, upgrade manager upgrade, upgrade manager rollback, switch-forward,
                                             or system maintenance initiate operations, then you see the status of the previous upgrade/rollback/maintenance if no other
                                             Orchestration operation is attempted post these operations.

#### Check Last Known Orchestration Operation Status on Remote Node

To check the last known orchestration operation status (last completed state or last known state when the operation is in
                                 progress or when the remote node is not reachable) on the remote node, run the utils deployment show progress-HA command. This command is applicable for patch manager install, patch manager rollback, upgrade manager upgrade, upgrade manager rollback,
                                    switch-forward, and system maintenance initiate.

This command can be used only in Cloud Connect High Availability setup.

The snapshot of the last known operation status is displayed.

Last known orchestration operation status will not be synchronized to remote node, in
                                             case of communication loss to remote node after initiating the orchestration
                                             operation and operation being completed before re-establishing the
                                             communication.

#### Start Unified ICM Services

To start Unified ICM services from Cloud Connect server, run the utils system icm-services start command.

User should choose individual or group of Unified ICM hosts from the list.

User should give confirmation yes/no to proceed with start of Unified ICM services

When the Unified ICM services are started successfully from stop state, the message “ Services started ” is displayed.

When the Unified ICM services are already up and running, the message “ Services running ” is displayed.

### Maintenance Tasks

#### CLI to configure the bandwidth for Orchestration software download

To configure the bandwidth that the Orchestration feature uses to download the software from Cisco hosted software artifactory
                                    to Cloud Connect server, run the utils set software-download bandwidth command.

When run, this command prompts for the following:

Your confirmation with yes or no for turn-on or turn-off the bandwidth configuration.

Enter a valid bandwidth value if you have chosen to turn-on the bandwidth configuration.

Make sure to suffix the bandwidth value with M for Mbps, K for Kbps and None for Bytes per second.

Following are the outcomes:

Displays the success or failure message when you turn-on or turn-off the bandwidth configuration.

If you have turned-on the bandwidth configuration and entered a valid value, this CLI validates and configures the entered
                                                      bandwidth value.

Make sure that you configure the bandwidth for software download, on the publisher and subscriber separately.

Software download bandwidth control is disabled by default. The maximum available bandwidth is used during software download.
                                                      This might have an impact on the features supported by Cloud Connect only during software download.

Cisco recommends minimum10-Mbps bandwidth for optimal software download. If you configure the bandwidth to a value that is
                                                      lesser than 10-Mbps, the duration of the software download increases and the orchestration operations cannot be performed
                                                      during the software download duration. If you configure the bandwidth to a value that is greater than the maximum available
                                                      bandwidth, the software download uses only the maximum available bandwidth.

Proxy configured for orchestration might have an impact on the maximum available bandwidth for software download. Check the
                                                      proxy configuration and ensure the configured bandwidth will be available for the software download when proxy is used for
                                                      orchestration.

#### Enforce software download from Cisco hosted software artifactory

To initiate software download from Cisco hosted software artifactory to cloud connect server, run the utils initiate software-download command.

Software download must be planned during off-peak hours as it consumes network bandwidth and resources. The duration of the
                                                      download depends on the number of software that needs to be downloaded.

Periodic software download happens everyday at 2 AM or at the time configured by admin. Use this CLI to initiate software
                                                      download before the next scheduled download.

Software download needs to be initiated in the publisher and the subscriber separately. While software download is in progress
                                                      on the publisher, you can run the orchestration operation from the subscriber, or vice-versa.

This CLI only initiates the software download and the download starts after prerequisites are met.

#### Update VOS Nodes Onboarded to Orchestration Control Node

To update VOS based nodes that have been onboarded, run the utils system onboard update command from the publisher node in the VOS node/cluster that you want to update.

Cloud Connect server FQDN

Cloud Connect application username and password

After every successful update on Cloud Connect version 15.0(1) SU1 or later, refresh the deployment cache by executing the utils deployment cache initiate command on the Cloud Connect publisher node. Alternatively, the cache will update automatically during the next daily scheduled
                                             update.

#### Remove VOS Nodes from Orchestration Control Node

To remove any existing VOS-based node or cluster, run the utils system onboard remove command from the publisher node in the VOS node/cluster that you want to remove.

Cloud Connect server FQDN

Cloud Connect application username and password

After every successful remove on Cloud Connect version 15.0(1) SU1 or later, refresh the deployment cache by executing the utils deployment cache initiate command on the Cloud Connect publisher node. Alternatively, the cache will update automatically during the next daily scheduled
                                             update.

#### Update Windows Nodes Onboarded to Orchestration Control Node

The update procedure is similar to the onboarding procedure described in Onboard Windows nodes to orchestration control node .

If SSH connection is already established, skip Step 1 in the above procedure.

#### Validate Updated Nodes Onboarded for Orchestration

The procedure to validate updated nodes that have been onboarded is the same as described in Validate Onboarded Nodes for Orchestration .

#### View Email Configuration

You can check your email configuration details by running the respective commands as described below:

Get the IP address or hostname of the SMTP server by running the show smtp-host command.

Get the email address from which the emails are triggered by running the show smtp-from-email command.

See if SMTP authentication is enabled or not by running the show smtp-use-auth command.

Get the username for SMTP server connection by running the show smtp-user command.

See if the SMTP password is set or not by running the show smtp-pswd command.

See the email addresses subscribed for notification by running the utils smtp show subscriptions command.

If there is no email address subscribed, a message is displayed indicating it.

#### Delete Configuration for Email Notification

To remove the configuration for email notifications, run the utils smtp remove-config command.

#### Unsubscribe Email Notification

To unsubscribe from email notifications, run the utils smtp unsubscribe command.

You can get a list of subscribed email addresses using the utils smtp show subscriptions command.

```
utils smtp unsubscribe <emailaddress1,emailaddress2,.....emailaddressesN>
```

You can also remove all the subscribed email addresses from the subscription list at once. To do that, run utils smtp unsubscribe all and confirm.

#### Export and Import of Nodes Managed by Orchestration Control Node

To export inventory to an SFTP server, run the utils system inventory export command.

SFTP Server: IP address of the SFTP remote server

SFTP User

SFTP User's Password

SFTP Directory: Location of the remote server directory where the inventory needs to be exported

Provide the location only; the filename is inventory.conf by default.

To import inventory to Cloud Connect server, run the utils system inventory import command.

SFTP Server: IP address of the SFTP remote server

SFTP User

SFTP User's Password

SFTP Directory: Location of the remote server directory from where the inventory needs to be imported

Provide the location only. The filename is inventory.conf by default.

During inventory import, the inventory.conf filename should have the side information added for each node. For example, side: "A" /side: "B". During inventory import,
                                                                     the cluster information cannot be blank. It should have valid host details or a default value {}. For example, "ROGGER":{}

After successful import on Cloud Connect version 15.0(1) SU1 or later, it is recommended to update the deployment cache by
                                             running the CLI command utils deployment cache initiate , or you may wait for the daily scheduled update.

For information on adding deployment type and deployment name in the inventory file, see Add Deployment Type and Deployment Name .

#### Export Current Patch Level Details

Available patches for nodes in the deployment can be obtained in either of the following ways:

Email Notification

Using the utils deployment export status command.

Effective with release 15.0.1 SU1, the CLI command utils patch-manager export status has been renamed to utils deployment export-status . Please note that this is a nomenclature update only and does not impact the command's functionality.

Current patch levels can be exported in text file format using the utils deployment export status command.

#### Serviceability

Deployment Cache Update Logs

Run the following commands on the Cloud Connect publisher node to retrieve deployment cache update related logs:

Current transaction logs: file get activelog ansible/ansible_component_cache_update_cron.log

Historical logs: file get activelog ansible/ansible_component_cache_update_cron_history.log

Process logs: file get activelog ansible/component_cache_update.log

Audit Logs

Audit trial for administrative operation that is initiated from Orchestration CLI on
                                 Cloud Connect is captured in Orchestration Audit logs. Audit trial captures the user,
                                 action and date/time details of the CLI operation.

file get activelog
                                          orchestration-audit/audit.log*

CLI Logs

Run the following command on the Cloud Connect node to retrieve CLI logs:

file get activelog platform/log/cli*.log

Ansible Logs

Run the following commands on the Cloud Connect node to retrieve ansible-related
                                 logs:

Current transaction logs: file get activelog
                                          ansible/ansible.log

Historical logs: file get activelog
                                          ansible/ansible_history.log

Main activity log: auto_rotate_token_schedule_job.log

Token log: auto_rotate_token_schedule_job.log

Operation log: ansible_auto_rotate_token_schedule_job.log

Operation Status HA Synchronization Logs

Run the following command on the Cloud Connect node to retrieve synchronization-related
                                 logs:

file get activelog
                                          ansible/sync_ansible_log_to_remote_cc.log

Email Notification-related Logs

Run the following commands on the Cloud Connect node to retrieve email-related logs:

Current transaction logs: file get activelog
                                          ansible/ansible_email_cron.log

Software Download Logs

Run the following commands on the Cloud Connect node to retrieve software
                                 download-related logs:

Current transaction logs: file get activelog
                                          ansible /software_download_ansible.log

Historical logs: file get activelog
                                          ansible/software_download_ansible_history.log

Process logs: file get activelog
                                          ansible/software_download_process.log

Software is downloaded separately on Cloud Connect publisher and subscriber.

Orchestration Logs in RTMT

You can also view the below-mentioned logs using the Real-Time Monitoring Tool
                                 (RTMT):

Audit logs by selecting 'Orchestration Audit' as the Cloud Connect service

Ansible logs by selecting 'Ansible Controller' as the Cloud Connect service

To download RTMT from Cloud Connect, access https://%3Cfqdnoripaddress%3E:8443/plugins/CiscoRTMTPlugin.zip .

For more information, refer to the Cisco Unified Real-Time Monitoring Tool
                                    Administration Guide at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

For logs on individual components, refer to the Serviceability Guide for Cisco Unified Contact Center Enterprise available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

#### Enable and View Windows Open SSH Logs

To enable and view open SSH logs, do the following:

Make sure the sshd_config file %programdata%\ssh\sshd_config has the
                                       value as 'LogLevel DEBUG' and uncomment the line.

Restart the service (select service name OpenSSH SSH
                                          Server ).

In the Windows Event Viewer, select option Show Analytic and Debug
                                          Logs from View on the top menu bar.

Select Debug channel from OpenSSH folder.

On the right hand side, under Actions from Debug channel, select Enable log .

To turn on file-based logging, do the following:

In the sshd_config file %programdata%\ssh\sshd_config , set the value
                                       as "SyslogFacility LOCAL0" and uncomment the line.

Restart the service (select service name OpenSSH SSH
                                          Server ).

The file based logs are collected at location %programdata%\ssh\logs .

## Configure SSH public key on Windows nodes

This section describes how to establish password-less Secure Shell (SSH) connection between Cloud Connect server and Windows
                           node (CVP and ICM) using an SSH public key. The Windows node can be in a Workgroup or Domain.

Navigate to %Users%\<logonUser>\.ssh\ and create authorized_keys file, if it doesn't exist.

The authorized_keys extension type is File and you should not modify it.

The user must have either domain admin or local administrator privilege.

Open the browser and enter the following Cloud Connect publisher URL: https://<CloudConnectIP>:8445/inventory/controlnode/key

Provide your Cloud Connect application admin credentials. Upon successful authentication, a REST API response fetches the
                                 Cloud Connect Public SSH Key.

Copy the public key value that appears between quotes in the API response into the authorized_keys file in %Users%\<logonUser>\.ssh\ .

Repeat steps 2, 3, and 4 to fetch the Cloud Connect subscriber public key (if Cloud
                                 Connect is HA setup).

You must copy the Cloud Connect publisher and subscriber public keys into a single authorized_keys file. The publisher and subscriber entries should be in separate lines and should not use any extra space, comma, or any
                                             special characters at the end of the line.

Restart the following OpenSSH services:

OpenSSH SSH Server

OpenSSH Authentication Agent

For more information on Windows security hardening, see the Windows Server Hardening section in the Security Guide for Cisco Unified Contact Center Enterprise .

## Self-Signed Certificate

You must import the self-signed certificates of both Cloud Connect publisher and subscriber nodes
                           to the VOS publisher and subscriber nodes.

### Get Tomcat Certificate from Cloud Connect Server

Step 1

Login to the Cloud Connect server using: https://<cloud connect hostname>:8443/cmplatform .

Step 2

Navigate to Security > Certificate Management .

Step 3

Click Find .

Step 4

Click on the Tomcat certificate of the Cloud Connect server.

Step 5

Download the .PEM file and save the file.

### Import Cloud Connect Server Tomcat Certificate to VOS Nodes

Step 1

Login to the VOS node server using: https://<VOS node hostname>:8443/cmplatform .

Step 2

Navigate to Security > Certificate Management .

Step 3

Click on Upload Certificate/Certificate Chain.

Step 4

Select ‘tomcat-trust’ from the drop-down list in the Certificate Purpose field.

Step 5

Click Browse to upload the Cloud Connect server .PEM file .

Step 6

Click Upload .

Step 7

Restart the specific VOS node by running the utils system restart command.

## Things to Know

Orchestration doesn't support for Customer Collaboration Platform (CCP), ECE, CCDM, CCMP, and non-Contact Center Cisco products
                                 such as UCM, Unity Connection, CUBE gateways, Cisco Contact Center SIP Proxy (CCCSP) , IM&P, and so on. Patches and upgrade operations for these components are performed in a traditional manner.

Orchestration is supported only for upgrades and patch install and not for tech
                                 refresh or fresh install.

If any activity is blocked with a message Previous operation is still in progress. Please retry after sometime , even if there's no active operation, then restart the Cloud Connect server.

If one component ES has a dependency on another component ES, then they have to be considered by the administrator before
                                 initiating the patch installation from the Cloud Connect server. The administrator should read the release notes that are
                                 notified through an email to understand the dependency. The Orchestration framework doesn't track this aspect automatically.
                                 For example, if an ES of Finesse has a dependency on an ES of Live Data and has to be installed in a specific order, then
                                 the administrator must consider this before initiating the patch installation from the Cloud Connect server.

Within Upgrade commands 'All Nodes' option for the Roll Back and Switch version commands aren't available.

Only Microsoft Exchange Server is supported for email notification; Office 365 and Gmail aren't supported as of now.

Email notifications are triggered about the available software upgrade from the publisher node of the Cloud Connect server.
                                 If the publisher node is down at the trigger time, then the Admin won't receive any notification.

For Packaged CCE deployment, only multistage upgrade is supported from Orchestration.

For Packaged CCE deployment, CVPOAMP is not supported.

The option to upgrade “All nodes” in the deployment (VOS and Windows nodes together) to CCE 15.0(1) via Orchestration is not
                                 supported. The administrator can upgrade the individual components to 15.0(1) by selecting the respective VOS or Windows nodes.
                                 All nodes option is currently supported only for upgrading to CCE 12.6(x).

Orchestration Cache Management

Orchestration maintains an internal cache that updates automatically at 5:00 AM system time or at the time configured by the
                                 administrator.

The following operations utilize the component cache to get the max efficiency:

utils upgrade-manager list : Uses cache when the All nodes option is selected. When Cloud Connect is running version 15.0(1) SU2 or later, the cache is used by all options in this
                                       CLI.

Orchestration patch manager CLIs : Uses cache when Cloud Connect is running version 15.0(1) SU1 or later.

Orchestration upgrade manager CLIs for VOS nodes : Uses cache when Cloud Connect is running version 15.0(1) SU2 or later.

Manual component upgrades or patch operations do not automatically update the internal cache. To ensure the cache reflects
                                 the current system state, perform the following steps based on the installed version:

For Cloud Connect 15.0(1) SU1 and later: Execute the utils deployment cache initiate command.

For releases earlier than 15.0(1) SU1: Execute the utils system inventory export command, followed by the utils system inventory import command.

When Cloud Connect is running version 15.0(1) SU1, if you perform patch operations immediately after an upgrade, you must
                                             first update the cache by executing the utils deployment cache initiate command. This ensures the cache reflects the updated node versions before patching.

Important Considerations

utils upgrade-manager list behavior: This command displays the latest available component versions when individual VOS nodes,
                                       Windows nodes, or group of nodes options are selected. In Cloud Connect 15.0(1) SU2 and later, the available component versions
                                       are retrieved from the internal cache. In releases prior to 15.0(1) SU2, the available component versions are directly retrieved
                                       from the nodes.

Version Reversion: When reverting Cloud Connect from 15.0(1) to 12.6(x), ensure the cache is updated by executing the utils
                                       system inventory export command, followed by the utils system inventory import command.

| Note | The name of the deployment is shown in the subject line of the email,
                                                      depending on the configuration in the inventory file. For patch install or rollback, email notifications are not sent to
                                                      indicate whether the procedure is successful or if it is a
                                                      failure. |
|---|---|

| Note | Orchestration supports parallel patching of multiple selected nodes. To use this feature, ensure that the Cloud Connect instance
                                                is running version 15.0(1) SU1 or later. Orchestration supports parallel upgrade, switch-forward, and rollback of multiple selected VOS nodes. To use this feature,
                                                ensure that the Cloud Connect instance is running version 15.0(1) SU2 or later. Each CCE deployment is required to have a dedicated Cloud Connect for Orchestration. |
|---|---|

| Note | The upgrade from 12.5(2) or 12.6(2) to 15.0(1) doesn't require any mandatory COP to be applied. |
|---|---|

| Note | Refer to the Virtualization for Unified Contact Center Enterprise document and ensure the Virtual Machine resources are updated as per the recommended VM configuration before triggering the
                                             upgrade from Orchestration. |
|---|---|

| Note | Orchestration supports patch operations for all deployment sizes, including those exceeding 4,000 agents. Upgrades to Major
                                          Releases and Service Updates (SU) for VOS nodes are supported for all deployment sizes when Cloud Connect 15.0.1 SU2 or later
                                          is installed. Upgrades for Windows nodes are currently limited to deployments of 4,000 agents or fewer. |
|---|---|

| Attention | You cannot run the utils smtp test-connection command in parallel while the same or a different CLI command is actively running on the specific Cloud Connect node. |
|---|---|

| CLI To Configure Orchestration Maximum Parallel Tasks |
|---|
| CLI to Enforce Deployment Cache Update |
| CLI to Check Status of Orchestration Deployment Cache |
| CLI to Configure Orchestration Scheduled Jobs |
| CLI to configure proxy for orchestration |
| CLI to configure authentication method for artifactory |
| Generate Artifactory Authentication Credentials |
| Generate the Artifactory Identity Token |
| Configure Identity Token Auto Rotation |
| CLI to Configure Artifactory URL and Artifactory Authentication Credentials |
| Onboard VOS Nodes to Orchestration Control Node |
| Onboard Windows nodes to orchestration control node |
| Add Deployment Type and Deployment Name |
| Validate Onboarded Nodes for Orchestration |
|  |
| Configure Email Notification |
| Configure Windows Server for Updates (Optional) |

| Check Installed Software Version and Patches |
|---|
| Install or Roll Back Patch or Upgrade Cloud Connect Server |
| List Available Patches for Specific Node or Group of Nodes |
| Install Patch to Specific Node or Group of Nodes |
| Roll Back Patch from Specific Node or Group of Nodes |
| Install Windows Updates to Specific Node or Group of Nodes |
| Roll Back Windows Update from Specific Node or Group of Nodes |
| Enable or Disable Compatibility Enforcement |
| Initiate maintenance mode for a specific nodes |
| List Available Upgrade Options |
| Upgrade a specific node or group of nodes |
| Perform Switch Forward on Specific VOS Node or Group of Nodes |
| Roll Back upgrade from a specific node or group of nodes |
| Check Status |
| Check Last Known Orchestration Operation Status on Remote Node |
| Start Unified ICM Services |

|  |
|---|
| CLI to configure the bandwidth for Orchestration software download |
| Enforce software download from Cisco hosted software artifactory |
| Update VOS Nodes Onboarded to Orchestration Control Node |
| Remove VOS Nodes from Orchestration Control Node |
| Update Windows Nodes Onboarded to Orchestration Control Node |
| Validate Updated Nodes Onboarded for Orchestration |
| View Email Configuration |
| Delete Configuration for Email Notification |
| Unsubscribe Email Notification |
| Export and Import of Nodes Managed by Orchestration Control Node |
| Export Current Patch Level Details |
| Serviceability |
| Enable and View Windows Open SSH Logs |

| Command | utils set orchestration max-parallel-tasks |
|---|---|
| Description | Configures the maximum number of nodes that can be processed concurrently during Orchestration operations. This allows you
                                             to manage system resource utilization and optimize operation performance. |
| Expected Input | Specify the allowed maximum number of parallel Orchestration tasks. Note The value must be between 1 and the total number of onboarded nodes. The maximum number of parallel tasks cannot exceed the number of nodes currently onboarded for orchestration. | Note | The value must be between 1 and the total number of onboarded nodes. The maximum number of parallel tasks cannot exceed the number of nodes currently onboarded for orchestration. |
| Note | The value must be between 1 and the total number of onboarded nodes. The maximum number of parallel tasks cannot exceed the number of nodes currently onboarded for orchestration. |
| Expected Output | The CLI validates the input and, upon successful validation, configures the specified max-parallel-tasks setting on the Cloud Connect server. |

| Note | The value must be between 1 and the total number of onboarded nodes. The maximum number of parallel tasks cannot exceed the number of nodes currently onboarded for orchestration. |
|---|---|

| Note | The utils set orchestration max-parallel-tasks command must be executed on the publisher node of the Cloud Connect server. After successful execution, the configuration
                                                      is automatically replicated to the subscriber node. The configured maximum parallel tasks setting applies to Orchestration patch manager operations when Cloud Connect 15.0.1
                                                      SU1 or later is installed. This setting also applies to VOS upgrade, switch-forward, and rollback operations when Cloud Connect
                                                      15.0.1 SU2 or later is installed. If this setting is not configured, Orchestration patch manager operations will default to using the maximum number of selected
                                                      nodes. At least one node must be onboarded before configuring the maximum number of parallel tasks. |
|---|---|

| Command | utils show orchestration max-parallel-tasks |
|---|---|
| Description | Displays the current configuration for the maximum number of parallel Orchestration tasks on the Cloud Connect server. |
| Expected Input | None |
| Expected Output | The command returns the configured value for the maximum number of parallel Orchestration tasks on the Cloud Connect server. |

| Command | utils orchestration max-parallel-tasks reset-to-default |
|---|---|
| Description | Resets the orchestration maximum parallel tasks to the default value, setting it equal to the number of selected nodes. |
| Expected Input | None |
| Expected Output | The command resets the configured value to default for the maximum number of parallel Orchestration tasks on the Cloud Connect
                                                server. |

| Note | The utils orchestration max-parallel-tasks reset-to-default command can only be executed on the publisher node of the Cloud Connect server. After successful execution, the configuration
                                                is automatically replicated to the subscriber node. |
|---|---|

| Note | These CLI commands are available in Cloud Connect version 15.0 SU1 and later. |
|---|---|

| Command | utils deployment cache initiate |
|---|---|
| Description | This command triggers an interactive menu on the Cloud Connect server, allowing you to select the specific deployment cache
                                          update to perform. |
| Expected Inputs | Step 1: Menu Selection After triggering the command, you will be presented with a menu to choose the cache update type: Choose the Deployment Cache update type: Refresh Software Artifactory Cache Data Refresh Deployment Nodes Cache Data Refresh Cache to Add Missing Node Data Refresh Both Deployment Nodes and Software Artifactory Cache Data Step 2: User Confirmation After selecting an option, provide confirmation to proceed with selected cache update option. |
| Expected Outcome | Displays a CLI message confirming the success or failure of the deployment cache update initiated. |

| Note | The deployment cache update can only be initiated from the publisher node. Once the update completes successfully on the publisher,
                                                   the cache data is automatically replicated to the subscriber node. Periodic deployment cache updates occur daily at 5:00 AM, or at a time configured by the administrator. Use this CLI to initiate
                                                   a cache update if needed before the next scheduled update, or after any manual upgrade or patch operations are performed on
                                                   the nodes. Orchestration operations are not allowed during a cache update. The time required to complete the cache update varies based
                                                   on the number of nodes or component types that need to be updated. This CLI only initiates the cache update and the actual update starts after the prerequisites are met. Please check the cache
                                                   update status using the utils deployment cache status CLI. |
|---|---|

| Note | This CLI command is available in Cloud Connect version 15.0 SU1 and later. |
|---|---|

| Command | utils deployment cache status |
|---|---|
| Description | This command displays the current status of the Orchestration deployment cache. The output varies based on whether the command
                                          is executed on a Cloud Connect publisher or subscriber node. It provides detailed information on the status of scheduled cache
                                          operations, CLI-triggered cache operations, and synchronisation processes. |
| Expected Input | Not applicable |
| Expected Outcome | The output varies depending on whether the command is executed on a publisher or subscriber node. When executed on a Publisher node: The command displays the following information: Last Known Cache Scheduled-Job Status: Status : Indicates the state of the last cache operation triggered by deployment cache scheduled job. Periodic deployment cache update
                                                         happens everyday at 5 AM or at the time configured by admin. Triggered at : The date and time when the scheduled job was triggered. Unreachable node(s) during scheduled job cache operation : Lists any node(s) that were unreachable during the scheduled cache operation. Cache data missing for node(s) during scheduled job cache operation : Lists any node(s) for which cache data is missing during the scheduled cache operation. Last Known Cache CLI Status: Status : Indicates the state of the last cache operation triggered by utils deployment cache initiate CLI command. Triggered at : The date and time when the CLI command was triggered. Unreachable node(s) during CLI-triggered cache operation : Lists any node(s) that were unreachable during the CLI-triggered cache operation. Cache data missing for node(s) during CLI-triggered cache operation : Lists any node(s) for which cache data is missing during the CLI-triggered cache operation. Last Known Status of Cache Sync from Subscriber to Publisher: Status : Indicates the status of the last cache synchronization from Cloud Connect subscriber to publisher. Completed at : The date and time when the last synchronization was completed. |
| When executed on a Subscriber node: Last Known Status of Cache Sync from Publisher to Subscriber: Status : Indicates the status of the last cache synchronization from Cloud Connect publisher to the subscriber. Completed at : The date and time when the last synchronization was completed. |

| Note | This CLI command is available in Cloud Connect version 15.0 SU1 and later. |
|---|---|

| Command | utils orchestration-job update schedule |
|---|---|
| Description | Use this command to modify the default schedule or update an existing orchestration job schedule. |
| Expected Input | Choose the orchestration scheduled job you want to update from the options below: Software Download from Cisco Artifactory Deployment Cache Update Software Update Email Notification Auto-rotate Cisco Artifactory Token For your selected job, the CLI displays the current schedule and prompt you to enter new values for hours (0-23) and minutes
                                             (0-59). Press Enter to keep the current value for either field. The CLI then displays the updated schedule and ask for confirmation (yes/no) before applying the changes. |
| Expected Output | The system displays a message indicating whether the update to the scheduled job configuration succeeded or failed. |

| Note | The table below shows the default schedules for existing Orchestration jobs. The system automatically checks whether your
                                             preferred new schedule conflicts with other scheduled jobs or overlaps with their estimated completion times. Orchestration Job Default Schedule Default Maximum Estimated Duration Software Download from Cisco Artifactory 2:00 AM 3 hours Deployment Cache Update 5:00 AM 2 hours Software Update Email Notification 1:00 AM 1 hour Auto-rotate Cisco Artifactory Token 12:30 AM 10 min Cisco recommends adjusting the default schedule times to meet your specific requirements. Ensure that you configure the schedule times for relevant jobs independently on both the Cloud Connect publisher and subscriber
                                                   nodes. When scheduling an Orchestration job, select times that do not conflict with other automated jobs. Allow sufficient time between
                                                   tasks based on their expected duration. If a new schedule overlaps with an existing Orchestration job, the CLI will reject
                                                   the update. Cisco recommends configuring different software download schedules for the Cloud Connect publisher and subscriber, preferably
                                                   with a one-hour interval between them. For example, if the Cloud Connect publisher is set to download at 3:00 AM, schedule
                                                   the Cloud Connect subscriber for 4:00 AM. This approach helps optimize network bandwidth usage. | Orchestration Job | Default Schedule | Default Maximum Estimated Duration | Software Download from Cisco Artifactory | 2:00 AM | 3 hours | Deployment Cache Update | 5:00 AM | 2 hours | Software Update Email Notification | 1:00 AM | 1 hour | Auto-rotate Cisco Artifactory Token | 12:30 AM | 10 min |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Orchestration Job | Default Schedule | Default Maximum Estimated Duration |
| Software Download from Cisco Artifactory | 2:00 AM | 3 hours |
| Deployment Cache Update | 5:00 AM | 2 hours |
| Software Update Email Notification | 1:00 AM | 1 hour |
| Auto-rotate Cisco Artifactory Token | 12:30 AM | 10 min |

| Orchestration Job | Default Schedule | Default Maximum Estimated Duration |
|---|---|---|
| Software Download from Cisco Artifactory | 2:00 AM | 3 hours |
| Deployment Cache Update | 5:00 AM | 2 hours |
| Software Update Email Notification | 1:00 AM | 1 hour |
| Auto-rotate Cisco Artifactory Token | 12:30 AM | 10 min |

| Command | utils orchestration-job show schedule |
|---|---|
| Description | Displays the current schedule for orchestration-related scheduled jobs configured on the system. |
| Expected Input | None required |
| Expected Output | Shows the current schedule of all orchestration-related scheduled jobs set up on the system. |

| Command | utils orchestration-job reset schedule |
|---|---|
| Description | Restores orchestration-related scheduled jobs to their default schedules. |
| Expected Input | Displays the current and default schedules for all configured orchestration-related jobs, then prompts you to confirm the
                                             reset. |
| Expected Output | After confirmation, the system restores the orchestration jobs to their default schedules and shows a success message. |

| Note | These CLI commands are available in Cloud Connect version 15.0 SU1 and later. |
|---|---|

| Command | set cloudconnect orchestration config |
|---|---|
| Description | This command enables the proxy configuration for orchestration to check and fetch updates from the Cisco-hosted cloud artifactory. |
| Expected Inputs | At the Proxy Configured prompt, enter Yes to enable the proxy or No to turn off the proxy. If you choose to enable the proxy, you’ll be prompted to enter the Proxy Host and Proxy Port details. Note Proxy Host should be the proxy-server FQDN or IP address. The proxy is turned off by default. Orchestration supports only HTTPS proxy (That understands the HTTP CONNECT command). | Note | Proxy Host should be the proxy-server FQDN or IP address. The proxy is turned off by default. Orchestration supports only HTTPS proxy (That understands the HTTP CONNECT command). |
| Note | Proxy Host should be the proxy-server FQDN or IP address. The proxy is turned off by default. Orchestration supports only HTTPS proxy (That understands the HTTP CONNECT command). |
| Expected Outcome | This CLI enables or turns-off the proxy for orchestration based on user input. |

| Note | Proxy Host should be the proxy-server FQDN or IP address. The proxy is turned off by default. Orchestration supports only HTTPS proxy (That understands the HTTP CONNECT command). |
|---|---|

| Note | You can run this command only from the publisher node of the Cloud Connect server. The proxy configuration replicates automatically
                                             from the publisher node to the subscriber node when the set cloudconnect orchestration config command is run successfully on the publisher node. |
|---|---|

| Command | show cloudconnect orchestration config |
|---|---|
| Description | This command displays the proxy configuration for orchestration to check and fetch updates from the Cisco-hosted cloud artifactory. |
| Expected Inputs | NA |
| Expected Outcome | If the proxy is enabled, the proxy host and proxy port details are displayed. |

| Command | utils image-repository authentication-type set |
|---|---|
| Description | This command configures the authentication method (Identity Token) required for connecting to Cisco Artifactory from Cloud
                                                Connect. |
| Expected Inputs | CLI displays the currently configured authentication method and user confirmation is required to proceed to switch the authentication
                                                method. |
| Expected Outcome | Displays message on the CLI if the authentication method configuration is a success or a failure. |

| Note | Identity Token is the default authentication method that is configured in release 15.0(1)SU2 and later. You can run this command only from the publisher node of the Cloud Connect server. When the utils image-repository authentication-type set command runs successfully on the publisher node, the authentication method configured on the publisher node is replicated
                                                      automatically on the subscriber node. After configuring the authentication method using the utils image-repository authentication-type set command, configure Identity Token by running the utils image-repository set command. |
|---|---|

| Note | The CCO ID used to generate Artifactory authentication credentials must possess valid software entitlements, such as an active
                                                   SWSS (service contract) or Flex subscription. Cisco recommends generating unique credentials for each distinct deployment (e.g., test, staging, production) using different
                                                   CCO IDs. However, within a single deployment, the same credential can be shared between the Cloud Connect publisher and subscriber. |
|---|---|

| Note | Ensure you save the token immediately. For security reasons, the token will not be displayed after you confirm the copy action. |
|---|---|

| Note | For detailed instructions on configuring authentication credentials, refer to the section CLI to Configure Artifactory URL and Artifactory Authentication Credentials |
|---|---|

| Command | utils image-repository authentication-token auto-rotate |
|---|---|
| Description | Use this command to enable, disable, or configure the automatic rotation of the Cisco Artifactory Identity Token. By default,
                                                auto rotation is disabled. |
| Expected Inputs | User confirmation to proceed with enabling or disabling identity token auto rotation. If you choose to enable auto-rotation, the CLI will prompt for the following settings: Rotation Trigger: The number of days before token expiry to initiate rotation (Range: 1–30 days; Default: 30). Failure Notification: The number of days before token expiry to begin sending failure alert emails (Range: 1–10 days; Default: 10). |
| Expected Outcome | CLI will display a success or failure message confirming the status change or configuration update. |

| Note | Schedule: When auto-rotation is enabled, the system checks daily at 12:30 AM Cloud Connect Publisher time whether the Identity Token
                                                      meets the configured number of days before expiry for auto-rotation. If the criteria is met, the system attempts to rotate
                                                      and configure the Identity Token accordingly. Prerequisite: Ensure Artifactory is configured to use Identity Token as the authentication method before enabling this feature. Manual Management: If auto-rotation is disabled, tokens must be managed and rotated manually. Notifications: Automated email notifications are sent by the system when an Identity Token auto-rotation succeeds or fails. However, these
                                                      emails are only triggered if email notifications are configured for orchestration. Node Restrictions: You can run this command only from the publisher node of the Cloud Connect server. |
|---|---|

| Note | Identity Token has been supported as an authentication method for Cisco Devhub Artifactory starting from Cloud Connect version
                                                15.0(1). The Identity Token auto-rotation feature is available from Cloud Connect version 15.0(1) ES202511 onwards. |
|---|---|

| Note | You can run the utils image-repository set command only in the publisher node of the Cloud Connect server. The replication of image repository configuration occurs
                                             automatically from the publisher node to the subscriber node when you run this command with successful results on the publisher
                                             node. |
|---|---|

| Note | Before running the command utils image-repository set on the CLI, access the link https://software.cisco.com/download/eula and accept the End User License Agreement (EULA) |
|---|---|

| Note | Artifactory supports authentication via an Identity Token. For detailed instructions on configuring the authentication method,
                                             refer to the section CLI to configure authentication method for artifactory . |
|---|---|

| Command | utils image-repository set |
|---|---|
| Description | This command allows you to configure the Cisco hosted software Artifactory URL, Artifactory Repository Name, and Artifactory Authentication Credentials . For information on Artifactory Authentication Credentials , refer to the Generate Artifactory Authentication Credentials section. This command validates the below: If the Cisco.com ID used to generate the Artifactory Authentication Credentials has entitlement to download the Cisco Contact Center software. If the EULA is signed by the Cisco.com ID that generates the Artifactory Authentication Credentials . If the Cisco.com ID that generates the Artifactory Authentication Credentials has the customer company's full address that is updated in the Cisco.com profile and validated by Cisco. If the Cloud Connect server is deployed in embargoed countries where software download is restricted. If the user has valid Authentication Credentials. Note If the Artifactory authentication method is set to Identity Token and the authentication credentials are invalid, regenerate
                                                                     the Identity Token and update the authentication credentials on Cloud Connect. For detailed instructions, refer to the section Generate the Artifactory Identity Token . If compliance validation fails, the Cisco.com ID user must perform the below-mentioned actions: For EULA compliance failure, confirm that you have read and agreed to be bound by the terms of Cisco EULA. Access the link https://software.cisco.com/download/eula to view and accept the agreement. For customer company's address verification failure, access the link https://rpfa.cloudapps.cisco.com/rpfa/profile/profile_management.do to update the address. For Entitlement failure, where Cisco service contract information indicates that you're not authorized to download the Contact
                                                   Center software, perform one or more of the following actions: Identify the product name and MDFID of the Contact Center product for which the entitlement failed. To find the product name
                                                         and corresponding MDFID of the product, check the CLI log for the keyword Entitlement check failed for MDFID . Refer to the Serviceability section for the command to retrieve the CLI log. The service contract or subscription containing coverage for the product may not be associated to the Cisco.com user ID. To
                                                         associate the relevant service contract to the Cisco user ID, use the Cisco Profile Manager , and select Add Access to request access to the contract (which can now be done using the Serial Number of the product). If your software is covered by a Smart License subscription, go to Cisco Software Central to request access to your company's
                                                         Smart Account in the Administration section. Contact your Cisco representative, partner, or reseller to ensure that the product is covered by a service contract or subscription
                                                   that is associated with your Cisco.com user ID. Use the Partner Locator link to locate your nearest partner. For assistance, contact your Cisco Accounts Manager or Partner. To expedite your request, include the following information: User ID (Cisco.com ID used to generate the Artifactory Authentication Credentials) Contact Name Company Name Contract Number Product ID or MDFID, Product Name, and Release You can obtain access to U.S. export-restricted software by completing the K9 agreement form . Note Upon successful configuration of artifactory details, artifacts are downloaded locally to the Cloud Connect server periodically
                                                               at the configured time. During artifact download, the compliance validation is done. The Cisco.com ID user performs the above-mentioned
                                                               actions for any compliance failure during artifact download. | Note | If the Artifactory authentication method is set to Identity Token and the authentication credentials are invalid, regenerate
                                                                     the Identity Token and update the authentication credentials on Cloud Connect. For detailed instructions, refer to the section Generate the Artifactory Identity Token . | Note | Upon successful configuration of artifactory details, artifacts are downloaded locally to the Cloud Connect server periodically
                                                               at the configured time. During artifact download, the compliance validation is done. The Cisco.com ID user performs the above-mentioned
                                                               actions for any compliance failure during artifact download. |
| Note | If the Artifactory authentication method is set to Identity Token and the authentication credentials are invalid, regenerate
                                                                     the Identity Token and update the authentication credentials on Cloud Connect. For detailed instructions, refer to the section Generate the Artifactory Identity Token . |
| Note | Upon successful configuration of artifactory details, artifacts are downloaded locally to the Cloud Connect server periodically
                                                               at the configured time. During artifact download, the compliance validation is done. The Cisco.com ID user performs the above-mentioned
                                                               actions for any compliance failure during artifact download. |
| Expected Inputs | User should input Artifactory URL, Artifactory Repository Name, and Artifactory Authentication Credentials . The Cisco-hosted software Artifactory URL is https://devhub-download.cisco.com/binaries and Artifactory Repository Name is ent-platform-release-external . Note Cisco recommends not to use the same Artifactory Artifactory Authentication Credentials generated by a single CCO ID across multiple deployments. For multiple deployments such as test, pre-production, production,
                                                      and so on, generate the Artifactory Artifactory Authentication Credentials for each deployment using different CCO IDs. Artifactory Artifactory Authentication Credentials generated by a single CCO ID can be used in both publisher and subscriber of Cloud Connect in a single deployment. CLI provides an option to the customer to choose between using export-restricted and unrestricted software, based on the entitlement
                                             associated with the Cisco.com ID. For example, VVB has export-restricted and unrestricted software. | Note | Cisco recommends not to use the same Artifactory Artifactory Authentication Credentials generated by a single CCO ID across multiple deployments. For multiple deployments such as test, pre-production, production,
                                                      and so on, generate the Artifactory Artifactory Authentication Credentials for each deployment using different CCO IDs. Artifactory Artifactory Authentication Credentials generated by a single CCO ID can be used in both publisher and subscriber of Cloud Connect in a single deployment. |
| Note | Cisco recommends not to use the same Artifactory Artifactory Authentication Credentials generated by a single CCO ID across multiple deployments. For multiple deployments such as test, pre-production, production,
                                                      and so on, generate the Artifactory Artifactory Authentication Credentials for each deployment using different CCO IDs. Artifactory Artifactory Authentication Credentials generated by a single CCO ID can be used in both publisher and subscriber of Cloud Connect in a single deployment. |
| Expected Outcome | This CLI validates the entitlement associated with the Cisco.com ID and connection to the Cisco-hosted software artifactory
                                          using the given configuration. Based on successful validation, the artifactory details are configured in the Cloud Connect
                                          server. |

| Note | If the Artifactory authentication method is set to Identity Token and the authentication credentials are invalid, regenerate
                                                                     the Identity Token and update the authentication credentials on Cloud Connect. For detailed instructions, refer to the section Generate the Artifactory Identity Token . |
|---|---|

| Note | Upon successful configuration of artifactory details, artifacts are downloaded locally to the Cloud Connect server periodically
                                                               at the configured time. During artifact download, the compliance validation is done. The Cisco.com ID user performs the above-mentioned
                                                               actions for any compliance failure during artifact download. |
|---|---|

| Note | Cisco recommends not to use the same Artifactory Artifactory Authentication Credentials generated by a single CCO ID across multiple deployments. For multiple deployments such as test, pre-production, production,
                                                      and so on, generate the Artifactory Artifactory Authentication Credentials for each deployment using different CCO IDs. Artifactory Artifactory Authentication Credentials generated by a single CCO ID can be used in both publisher and subscriber of Cloud Connect in a single deployment. |
|---|---|

| Note | Use the command utils image-repository set to change export-restricted or unrestricted software in the deployment. Use the CLI utils initiate software-download to enforce the cleanup and download the restricted vs unrestricted software. |
|---|---|

| Note | On the successful configuration of artifactory details, artifacts are downloaded locally to the Cloud Connect server at the
                                             scheduled or default time. Orchestration operations such as patch install, rollback, or upgrade can be performed only after
                                             the artifacts are downloaded. If you need to download the artifacts immediately after the configuration, use the utils initiate software-download CLI. Usage of orchestration-related CLI is blocked during download, and this duration depends on the number of artifacts
                                             to be downloaded. |
|---|---|

| Note | Before you configure the bandwidth using the utils set software-download bandwidth command, make sure the software is downloaded locally for the first time after the artifactory is successfully configured
                                          using the utils image-repository set command. To download the artifacts immediately after the configuration, use the utils initiate software-download command. |
|---|---|

| Command | utils image-repository show |
|---|---|
| Description | This command displays the configured Cisco-hosted software Artifactory URL, Repository Name, and the Artifactory Authentication Credentials (the mix of hash and last 4 characters of the Credentials) in the Cloud Connect server. |
| Expected Inputs | NA |
| Expected Outcome | Displays the configured Artifactory URL, Repository Name, and the Artifactory Authentication Credentials . |

| Command | utils system onboard initiate |
|---|---|
| Description | This command is used to onboard a VOS node such as Finesse, CUIC, VVB, etc., to a Cloud Connect server. |
| Expected Inputs | When run, the command prompts for: Cloud Connect server FQDN Cloud Connect application username Password |
| Expected Outcome | The nodes are onboarded to the Cloud Connect server orchestration inventory. A message is
                                          displayed indicating the status. |

| Note | If the system (cluster) onboards to the Cloud Connect server with partial error,
                                             check the reason for the error and correct it. Then, run the utils system
                                                onboard update command instead of running the utils system
                                                onboard initiate command. |
|---|---|

| Note | Onboarding is allowed only when all the publisher and subscriber nodes in the Cloud
                                             Connect server are reachable. |
|---|---|

| Note | If the Cloud Connect server is corrupted and redeployed by doing fresh install, the
                                             administrator has to run utils system onboard remove from the VOS
                                             node and then run utils system onboard initiate to onboard the
                                             VOS nodes again. |
|---|---|

| Note | After every successful onboard on Cloud Connect version 15.0(1) SU1 or later, refresh the deployment cache by executing the utils deployment cache initiate command on the Cloud Connect publisher node. Alternatively, the cache will update automatically during the next daily scheduled
                                             update. |
|---|---|

| Step 1 | Configure SSH public key on the Windows nodes by following the steps in the section Configure SSH public key on Windows nodes . |
|---|---|
| Step 2 | From the cloud connect server, run the utils system inventory export command to download the inventory to an SFTP server. For details, see Export and Import of Nodes Managed by Orchestration Control Node . |
| Step 3 | Edit the inventory file to include the Windows components. Refer to the default template section in the inventory file. Note The syntax, alignment, and indentation must be exactly the same as mentioned in the inventory file. Ensure the CRLF line endings are of UNIX-Style. Use a Linux-based or a Mac OS-based editor to create the Windows inventory
                                                                  file. The following fields in the inventory file are mandatory. Field Description ProductName The ProductName mentioned in the inventory file must be in uppercase and cannot be changed. For example, CVPREPORTING, CVPSERVER, CVPOAMP,
                                                            DISTRIBUTOR, LOGGER, PG, ROGGER or ROUTER. Pair under product This is a user-defined pair name. Hostname This can be a valid IP, or hostname, or FQDN name of the target node. Side of the deployment It can either be A or B. User configured on host This is the username for which the SSH keys are configured in Step 1. Note The user must have either domain admin or local administrator privilege. Note User name can be in User Principal Name (UPN) format or Domain username (domain\username) format for domain administrator
                                                                        or local administrator user name. Example: UPN format : administrator@stooges.icm Domain Administrator: stooges\administrator Local Administrator: administrator | Note | The syntax, alignment, and indentation must be exactly the same as mentioned in the inventory file. Ensure the CRLF line endings are of UNIX-Style. Use a Linux-based or a Mac OS-based editor to create the Windows inventory
                                                                  file. | Field | Description | ProductName | The ProductName mentioned in the inventory file must be in uppercase and cannot be changed. For example, CVPREPORTING, CVPSERVER, CVPOAMP,
                                                            DISTRIBUTOR, LOGGER, PG, ROGGER or ROUTER. | Pair under product | This is a user-defined pair name. | Hostname | This can be a valid IP, or hostname, or FQDN name of the target node. | Side of the deployment | It can either be A or B. | User configured on host | This is the username for which the SSH keys are configured in Step 1. Note The user must have either domain admin or local administrator privilege. Note User name can be in User Principal Name (UPN) format or Domain username (domain\username) format for domain administrator
                                                                        or local administrator user name. Example: UPN format : administrator@stooges.icm Domain Administrator: stooges\administrator Local Administrator: administrator | Note | The user must have either domain admin or local administrator privilege. | Note | User name can be in User Principal Name (UPN) format or Domain username (domain\username) format for domain administrator
                                                                        or local administrator user name. Example: UPN format : administrator@stooges.icm Domain Administrator: stooges\administrator Local Administrator: administrator |
| Note | The syntax, alignment, and indentation must be exactly the same as mentioned in the inventory file. Ensure the CRLF line endings are of UNIX-Style. Use a Linux-based or a Mac OS-based editor to create the Windows inventory
                                                                  file. |
| Field | Description |
| ProductName | The ProductName mentioned in the inventory file must be in uppercase and cannot be changed. For example, CVPREPORTING, CVPSERVER, CVPOAMP,
                                                            DISTRIBUTOR, LOGGER, PG, ROGGER or ROUTER. |
| Pair under product | This is a user-defined pair name. |
| Hostname | This can be a valid IP, or hostname, or FQDN name of the target node. |
| Side of the deployment | It can either be A or B. |
| User configured on host | This is the username for which the SSH keys are configured in Step 1. Note The user must have either domain admin or local administrator privilege. Note User name can be in User Principal Name (UPN) format or Domain username (domain\username) format for domain administrator
                                                                        or local administrator user name. Example: UPN format : administrator@stooges.icm Domain Administrator: stooges\administrator Local Administrator: administrator | Note | The user must have either domain admin or local administrator privilege. | Note | User name can be in User Principal Name (UPN) format or Domain username (domain\username) format for domain administrator
                                                                        or local administrator user name. Example: UPN format : administrator@stooges.icm Domain Administrator: stooges\administrator Local Administrator: administrator |
| Note | The user must have either domain admin or local administrator privilege. |
| Note | User name can be in User Principal Name (UPN) format or Domain username (domain\username) format for domain administrator
                                                                        or local administrator user name. Example: UPN format : administrator@stooges.icm Domain Administrator: stooges\administrator Local Administrator: administrator |
| Step 4 | Import the inventory back from the SFTP server by running the command utils system inventory import on the Cloud Connect publisher node. For details, see Export and Import of Nodes Managed by Orchestration Control Node . |

| Note | The syntax, alignment, and indentation must be exactly the same as mentioned in the inventory file. Ensure the CRLF line endings are of UNIX-Style. Use a Linux-based or a Mac OS-based editor to create the Windows inventory
                                                                  file. |
|---|---|

| Field | Description |
|---|---|
| ProductName | The ProductName mentioned in the inventory file must be in uppercase and cannot be changed. For example, CVPREPORTING, CVPSERVER, CVPOAMP,
                                                            DISTRIBUTOR, LOGGER, PG, ROGGER or ROUTER. |
| Pair under product | This is a user-defined pair name. |
| Hostname | This can be a valid IP, or hostname, or FQDN name of the target node. |
| Side of the deployment | It can either be A or B. |
| User configured on host | This is the username for which the SSH keys are configured in Step 1. Note The user must have either domain admin or local administrator privilege. Note User name can be in User Principal Name (UPN) format or Domain username (domain\username) format for domain administrator
                                                                        or local administrator user name. Example: UPN format : administrator@stooges.icm Domain Administrator: stooges\administrator Local Administrator: administrator | Note | The user must have either domain admin or local administrator privilege. | Note | User name can be in User Principal Name (UPN) format or Domain username (domain\username) format for domain administrator
                                                                        or local administrator user name. Example: UPN format : administrator@stooges.icm Domain Administrator: stooges\administrator Local Administrator: administrator |
| Note | The user must have either domain admin or local administrator privilege. |
| Note | User name can be in User Principal Name (UPN) format or Domain username (domain\username) format for domain administrator
                                                                        or local administrator user name. Example: UPN format : administrator@stooges.icm Domain Administrator: stooges\administrator Local Administrator: administrator |

| Note | The user must have either domain admin or local administrator privilege. |
|---|---|

| Note | User name can be in User Principal Name (UPN) format or Domain username (domain\username) format for domain administrator
                                                                        or local administrator user name. Example: UPN format : administrator@stooges.icm Domain Administrator: stooges\administrator Local Administrator: administrator |
|---|---|

| Step 1 | Download the inventory to an SFTP server by running the utils system inventory export command. For details, see Export and Import of Nodes Managed by Orchestration Control Node . |
|---|---|
| Step 2 | Edit the following strings in the inventory file, if
                                                required. deploymentType : This field is used for compatibility check during an upgrade or rollback or switch forward procedure. Ensure that the values entered in this field conform to the below format. The deployment type is case sensitive. For Example:
                                                      UCCE-4000-Agents. Note By default, deployment Type will be UCCE-2000-Agents, update it to the correct value to realise some Orchestration features.
                                                                  If you want to scale more than 24000 agents for UCCE, set it as UCCE-24000-Agents only. HCS-CC-2000-Agents HCS-CC-4000-Agents Note Orchestration is not supported for 12000, 24000 and 36000 agent deployment models. HCS-SCC (Small Contact Center ) deployment model is currently not supported for Orchestration. Ensure that the values entered in this field conform to the above format. The deployment type is case sensitive. deploymentName :
                                                      Provide a unique name for the deployment. This
                                                   name appears in the subject line of the email
                                                   notification. If it is not configured, the subject
                                                   line of the email notification contains only the
                                                   type of procedure and the overall status. Note The administrator can update or edit the default
                                                            values, if required, based on their deployment
                                                            type and preferred deployment name. | Note | By default, deployment Type will be UCCE-2000-Agents, update it to the correct value to realise some Orchestration features.
                                                                  If you want to scale more than 24000 agents for UCCE, set it as UCCE-24000-Agents only. | Note | Orchestration is not supported for 12000, 24000 and 36000 agent deployment models. HCS-SCC (Small Contact Center ) deployment model is currently not supported for Orchestration. | Note | The administrator can update or edit the default
                                                            values, if required, based on their deployment
                                                            type and preferred deployment name. |
| Note | By default, deployment Type will be UCCE-2000-Agents, update it to the correct value to realise some Orchestration features.
                                                                  If you want to scale more than 24000 agents for UCCE, set it as UCCE-24000-Agents only. |
| Note | Orchestration is not supported for 12000, 24000 and 36000 agent deployment models. HCS-SCC (Small Contact Center ) deployment model is currently not supported for Orchestration. |
| Note | The administrator can update or edit the default
                                                            values, if required, based on their deployment
                                                            type and preferred deployment name. |
| Step 3 | Import the inventory back from the SFTP server by running the
                                             utils system inventory import command on the Cloud Connect
                                             publisher node. For details, see Export and Import of Nodes Managed by Orchestration Control Node . |

| Note | By default, deployment Type will be UCCE-2000-Agents, update it to the correct value to realise some Orchestration features.
                                                                  If you want to scale more than 24000 agents for UCCE, set it as UCCE-24000-Agents only. |
|---|---|

| Note | Orchestration is not supported for 12000, 24000 and 36000 agent deployment models. HCS-SCC (Small Contact Center ) deployment model is currently not supported for Orchestration. |
|---|---|

| Note | The administrator can update or edit the default
                                                            values, if required, based on their deployment
                                                            type and preferred deployment name. |
|---|---|

| Command | utils deployment test-connection |
|---|---|
| Description | This command is used to validate whether password-less SSH connection is successful between the onboarded nodes and the Cloud
                                          Connect server. You can test the connection to all nodes on the deployment or to a specific group or individual nodes. |
| Expected Inputs | NA |
| Expected Outcome | Shows whether the inventory is accurate and the Cloud Connect node is able to connect to the
                                          managed hosts. |

| Note | The SMTP server referred to in this section is the mail server that is used within
                                             the customer organization for their internal email communication. |
|---|---|

| 1 | Set up Email Notification |
|---|---|
| 2 | Validate Email configuration |
| 3 | Subscribe to Email Notification |
| 4 | View Email Configuration |

| Command | set smtp-host |
|---|---|
| Description | This command is used to set the IP address or hostname of the SMTP server. |
| Expected Inputs | SMTP server IP Address/HostName |
| Expected Outcome | The SMTP address is updated. |

| Command | set smtp-from-email |
|---|---|
| Description | This command is used to set the email address from which the emails are triggered. This email address is not monitored and
                                                   therefore  not used for replying to any emails. |
| Expected Inputs | When run, this command takes an input for a complete email address. |
| Expected Outcome | Configures the email address from which email notifications are triggered. |

| Command | set smtp-use-auth |
|---|---|
| Description | This command is used to enable or disable SMTP authentication. By default, this is disabled. |
| Expected Inputs | The command takes an input for the values Enable or Disable . |
| Expected Outcome | SMTP authentication type is updated. |

| Command | set smtp-user |
|---|---|
| Description | This command is used to set the username to be used for SMTP server connection. |
| Expected Inputs | The command takes an input for the username to be used for SMTP authentication. |
| Expected Outcome | Configures the SMTP username. |

| Command | set smtp-pswd |
|---|---|
| Description | This command is used to set the password for SMTP server connection. The password is stored in an encrypted format. To change
                                                   the password, run this command again. |
| Expected Inputs | The command prompts for a password for the SMTP connection. |
| Expected Outcome | Configures the SMTP password. |

| Command | utils smtp test-connection |
|---|---|
| Description | This command is used to check the connection to the SMTP server using the configured parameters. You can also trigger a test
                                                email notification from Orchestration to validate the SMTP configuration. |
| Expected Inputs | Yes or No A confirmation to trigger a test email to validate the SMTP configuration. |
| Expected Outcome | Shows whether the SMTP connection is successful or not. If the connection is unsuccessful, displays the details of the missing or invalid SMTP mandatory configuration. If the connection is successful, displays a confirmation message and provides an option to send a test email. As per the confirmation,
                                                displays whether the test email is successfully triggered to the configured subscribers. |

| Command | utils smtp subscribe |
|---|---|
| Description | This command is used to specify the email addresses that subscribe to the email notifications. |
| Expected Inputs | Provide a list of valid email addresses, separated by commas, with no spaces in between. For example: utils smtp subscribe <emailaddress1,emailaddress2,.....emailaddressesN> |
| Expected Outcome | Email addresses provided are subscribed for notification. |

| Note | Before upgrade or rollback of nodes managed by Orchestration, make sure to take
                                          backup as suggested by respective component documentation. Backup has to be done
                                          manually. |
|---|---|

| Note | In case the upgrade or rollback on VOS node fails, then the respective VOS node
                                          restart is mandatory before attempting the next upgrade or rollback on the same
                                          node. If the administrator does not restart, the next attempt to upgrade or rollback
                                          might fail. |
|---|---|

| Command | utils deployment show status |
|---|---|
| Description | This command is used to check the currently installed software version and patches for the
                                          selected Windows or VOS node individually or group of nodes or for all nodes in
                                             the inventory by selecting the option 'All Nodes in the inventory'. |
| Expected Inputs | Select the node or group of nodes or all nodes from the inventory. |
| Expected Outcome | Displays information about the installed software version and the patches for the selected
                                          node or group of nodes or all nodes from the inventory. If there is no
                                          patch installed, a message "No patch installed" is displayed to indicate
                                          that along with software version. |

| Note | The Cloud Connect publisher should be upgraded before upgrading the subscriber. The
                                             switch version on publisher should be done first before doing switch version on
                                             subscriber, use utils system switch version command to switch
                                             between versions. |
|---|---|

| Command | utils system upgrade initiate |
|---|---|
| Description | This command is used to initiate the patch install or to roll back the previously installed patch on Cloud Connect server or to upgrade Cloud Connect Server to the next available version . The patches and upgrade options available for patch install or rollback or upgrade are listed from Cisco artifactory. |
| Expected Inputs | Select the Local Repository option to list the patches and upgrade options available for patch install or rollback or upgrade . Select the patch to install or roll back or upgrade option to upgrade Cloud Connect server . |
| Expected Outcome | The selected patch for install or rollback is installed on Cloud
                                          Connect server or
                                             selected upgrade option is used to upgrade the Cloud Connect
                                             server . |

| Note | The Local Repository option is used only after the Cisco Artifactory is successfully configured on Cloud Connect server. See CLI to Configure Artifactory URL and Artifactory Authentication Credentials for configuring Cisco artifactory. |
|---|---|

| Note | Optionally, to receive email notification about the status of the patch installation
                                             or rollback or upgrade for
                                             Cloud Connect server, provide the SMTP host server details when prompted by the
                                             CLI. |
|---|---|

| Note | Patch install or rollback or upgrade on Cloud Connect server initiated using utils system upgrade initiate command can be canceled using utils system upgrade cancel command. The utils system upgrade status command can be used to check the status. |
|---|---|

| Note | Use the CLI command utils initiate software-download to download the Unified ICM and Unified CVP 15.0(1) software to the Cloud Connect Server after upgrading Cloud Connect to 15.0(1) or 15.0 SU1 for both publisher and subscriber nodes. Alternatively, wait for the default or scheduled software download to finish before
                                             starting the Unified CVP/ICM upgrade to 15.0(1). |
|---|---|

| Command | utils patch-manager list |
|---|---|
| Description | This command is used to get a list of patches available for installation for a specific node
                                          or group of nodes based on the selected option. |
| Expected Inputs | Select a node or group of nodes based on the inventory. |
| Expected Outcome | Displays information about available patches for the selected node or group of nodes. |

| Command | utils patch-manager install |
|---|---|
| Description | This command is used to install patches on a specific node or group of nodes onboarded to the Cloud Connect inventory. |
| Expected Inputs | Select the node or group of Windows or VOS nodes on which the patch needs to be installed. After you select the nodes, only
                                                the nodes containing the patches are displayed. For example, if you select 3 nodes and Windows or VOS patches are available
                                                for only 1 of them, you are asked to proceed with only one node. Confirm to proceed. You are also asked to confirm whether
                                                the target node needs to be rebooted after installing the patch. The Patch Install Orchestration CLI is supported with enhanced options for platform selection from 15.01 SU1 release: All Side A VOS node and All Side B VOS nodes under the VOS platform. All Side A Windows node and All Side B Windows nodes under the Windows platform. These new options enable parallel patch installation operations on either all Side A or all Side B nodes (Windows/VOS) within
                                                the deployment. Selection of components such as Finesse, CVP Call Server, IdS, PG, Router, and Rogger that are running on supported version
                                                of the maintenance mode, will provide the options "With maintenance mode” and “Without maintenance mode”. For details on maintenance
                                                mode supported version and prerequisites, see the Initiate maintenance mode for a specific nodes . If you select a group of nodes with some nodes on maintenance mode supported version and some nodes on unsupported version,
                                                then "With maintenance mode” or “Without maintenance mode” option is not available. If maintenance mode option is required,
                                                select the respective node which is on maintenance mode supported version. If you select “With maintenance mode” option, the maintenance mode is initiated for the selected node to failover active traffic
                                                gracefully or shutdown the services gracefully without interrupting the active traffic or causing outage for new traffic before
                                                installing the update and automatically rebooting. If you select, “Without maintenance mode” option, you are initially asked
                                                to confirm to proceed. Next, you are asked to provide confirmation on rebooting the node after installing the patch. |
| Expected Outcome | The selected patch is installed on the selected node or group of nodes. |

| Note | To start Unified ICM services, post the successful completion of patch install with reboot on Unified ICM nodes. See Start ICM Services . |
|---|---|

| Note | You can check the status of the patch install which is currently in-progress. For more information, see Check Status . |
|---|---|

| Note | Maintenance mode for IDS co-resident in 2000 Agents Deployment model is not supported |
|---|---|

| Note | Parallel patching is supported only for version 15.0 Quarterly Cumulative ES and above. For the VOS platform, this includes
                                                      Quarterly Cumulative ES and any common ES for all VOS components version 15.0 or higher. The same operation cannot be performed simultaneously from both the Cloud Connect publisher and subscriber. For example, if
                                                      a patch operation is already triggered for All Side A VOS Nodes from the Cloud Connect publisher, that same option cannot be used for any patch operation triggered from the Cloud Connect
                                                      subscriber at the same time. However, you can patch all of Side A by running All Side A VOS Nodes from the Cloud Connect publisher and All Side A Windows Nodes from the Cloud Connect subscriber, or vice versa. This option does not provide the ability to put nodes in maintenance mode before performing the patch operation for the All Side A/B option. If needed, place the relevant nodes in maintenance mode before starting the operation. Patch operations using the All Side A/B VOS option cannot be performed simultaneously on both CUIC publisher and subscriber nodes. If both nodes are present on a given
                                                      side, only the expected nodes will be processed; any additional nodes will be skipped, as the operation must be completed
                                                      on the publisher before proceeding on the subscriber. You can retry the operation on any skipped nodes after the current operation
                                                      finishes. |
|---|---|

| Command | utils patch-manager rollback |
|---|---|
| Description | This command is used to roll back previously installed patches on a specific node or group of nodes. In case of Windows-based nodes, the latest applied patch is allowed to roll back. In case of VOS-based nodes, the latest applied
                                                ES is rolled back. |
| Expected Inputs | From the list of Windows/VOS nodes displayed, select the node or group of Windows/VOS nodes on which the patch needs to be
                                                rolled back. Once you select the nodes, only the nodes for which Windows/VOS patch rollback is available will be displayed.
                                                For example, if you select 3 nodes and Windows/VOS patch rollback is available for only 1 of them, you are asked to proceed
                                                with only one node. There is also a message displayed indicating that the machine would restart after the patch is rolled
                                                back. Confirm to proceed. The Patch Rollback Orchestration CLI is supported with additional options for platform selection when Cloud Connect is upgraded
                                                to 15.0.1 SU1 or later. All Side A VOS node and All Side B VOS nodes under the VOS platform. All Side A Windows node and All Side B Windows nodes under the Windows platform. These new options enable parallel rollback of patches on either all Side A or all Side B nodes (Windows/VOS) within the deployment. For more information, refer to Prerequisites for All Side A/B options section of Install Patch to Specific Node or Group of Nodes . Selection of components such as Finesse, CVP Call Server, IdS, PG, Router, and Rogger that are running on supported version
                                                of the maintenance mode, will provide the options "With maintenance mode” and “Without maintenance mode”. For details on maintenance
                                                mode supported version and prerequisites, see the Initiate maintenance mode for a specific nodes . If you select a group of nodes with some nodes on maintenance mode supported version and some nodes on unsupported version,
                                                then "With maintenance mode” or “Without maintenance mode” option is not available. If maintenance mode option is required,
                                                select the respective node which is on maintenance mode supported version. If you select “With maintenance mode” option, the maintenance mode is initiated for the selected node to failover active traffic
                                                gracefully or shutdown the services gracefully without interrupting the active traffic or causing outage for new traffic before
                                                rollback and automatically rebooting. If you select, “Without maintenance mode” option, you are initially asked to confirm
                                                to proceed. Next, you are asked to provide confirmation on rebooting the node after rollback. |
| Expected Outcome | The previously installed patch is rolled back on the selected node or group of nodes. |

| Note | To start Unified ICM services, post the successful completion of patch rollback with reboot on Unified ICM nodes. See Start ICM Services |
|---|---|

| Note | You can check the status of patch rollback which is currently in-progress. For more information, see Check Status . |
|---|---|

| Note | Before running this command, refer to the recommended guidelines in the Microsoft Security Updates section of the Security Guide for Cisco Unified Contact Center Enterprise at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
|---|---|

| Command | utils patch-manager ms-patches install |
|---|---|
| Description | This command is used to install the latest Windows updates to a node or a group of Windows
                                          nodes or all Windows nodes. |
| Expected Inputs | From the list of Windows nodes displayed, select the node or group of Windows nodes or all Windows nodes to which the updates
                                             need to be applied. You can also select all the Windows nodes in the inventory. Once you select the nodes, only the nodes
                                             for which Windows updates are available will be displayed. For example, if you select 3 nodes and Windows updates are available
                                             for only 1 of them, you are asked to proceed with only one node. Confirm to proceed. You are asked to confirm whether the
                                             target nodes needs to be rebooted after installing the updates. Selection of components such as Finesse, CVP Call Server, IdS, PG, Router, and Rogger that are running on supported version
                                             of the maintenance mode, will provide the options "With maintenance mode” and “Without maintenance mode”. For details on maintenance
                                             mode supported version and prerequisites, see the Initiate maintenance mode for a specific nodes . If you select a group of nodes with some nodes on maintenance mode supported version and some nodes on unsupported version,
                                             then "With maintenance mode” or “Without maintenance mode” option is not available. If maintenance mode option is required,
                                             select the respective node which is on maintenance mode supported version. If you select “With maintenance mode” option, the maintenance mode is initiated for the selected node to failover active traffic
                                             gracefully or shutdown the services gracefully without interrupting the active traffic or causing outage for new traffic before
                                             installing the update and automatically rebooting. If you select, “Without maintenance mode” option, you are initially asked
                                             to confirm to proceed. Next, you are asked to provide confirmation on rebooting the node after installing the patch. |
| Expected Outcome | The selected Windows updates are installed on the selected node or group of nodes or all
                                          Windows nodes. |

| Note | The utils patch-manager ms-patches install operation may require a considerable amount of time to complete, depending on the number of Windows updates available on
                                             the target node. |
|---|---|

| Note | Before running this command, refer to the recommended guidelines in the Microsoft Security Updates section of the Security Guide for Cisco Unified Contact Center Enterprise at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html Listing of Windows updates available for rollback is not supported. |
|---|---|

| Command | utils patch-manager ms-patches rollback |
|---|---|
| Description | This command is used to roll back a specific Windows update from a specific node or group of
                                          nodes or all Windows nodes. |
| Expected Inputs | Select the node or group of Windows nodes or all Windows nodes on which the rollback needs to be performed. You can also select
                                             all the Windows nodes in the inventory for rollback. Provide the Knowledge Base (KB) number you want to rollback. Once the
                                             KB number is provided, only the nodes that are applicable for the rollback will be displayed. For Example, if you select 4
                                             nodes to roll back and the KB number provided is applicable for only one of them, you are asked to proceed with only one node.
                                             Confirm to proceed. You are asked to confirm whether the target nodes need to be rebooted after rollback. Selection of components such as Finesse, CVP Call Server, IdS, PG, Router, and Rogger that are running on supported version
                                             of the maintenance mode, will provide the options "With maintenance mode” and “Without maintenance mode”. For details on maintenance
                                             mode supported version and prerequisites, see the Initiate maintenance mode for a specific nodes . If you select a group of nodes with some nodes on maintenance mode supported version and some nodes on unsupported version,
                                             then "With maintenance mode” or “Without maintenance mode” option is not available. If maintenance mode option is required,
                                             select the respective node which is on maintenance mode supported version. If you select “With maintenance mode” option, the maintenance mode is initiated for the selected node to failover active traffic
                                             gracefully or shutdown the services gracefully without interrupting the active traffic or causing outage for new traffic after
                                             rollback and automatically rebooting. If you select, “Without maintenance mode” option, you are initially asked to confirm
                                             to proceed. Next, you are asked to provide confirmation on rebooting the node after rollback. |
| Expected Outcome | The selected Windows updates are rolled back. |

| Note | By default, the compatibility enforcement is enabled. When the compatibility enforcement is disabled, the Orchestration framework does not
                                             enforce upgrade, rollback, or switch forward as per the compatibility matrix
                                             published by Cisco. |
|---|---|

| Command | utils deployment compatibility-check |
|---|---|
| Description | This command is used to enable or disable compatibility
                                          enforcement. |
| Expected Inputs | User confirmation to proceed with enabling or disabling
                                          compatibility enforcement. |
| Expected Outcome | Message about the success or failure of enabling or disabling
                                          compatibility enforcement. |

| Note | You can run this command only from the publisher node of the Cloud Connect server.
                                             The compatibility configuration replicates automatically from the publisher node to
                                             the subscriber node when the utils deployment compatibility-check command is run with successful results on the publisher node. |
|---|---|

| Note | Ensure that not all CVP servers are put into maintenance mode at same time, so that incoming call traffic can be distributed. |
|---|---|

| Note | To enable Maintenance Mode support for Router and Rogger in Orchestration, install Cloud Connect mandatory 15.0(1) ES202508 or above. |
|---|---|

| Command | utils system maintenance initiate |
|---|---|
| Description | This command is used to initiate maintenance mode for a specific node based on the selected option. The initiate maintenance command is available for Finesse, CVP Call Server, IdS, PG, Router, and Rogger components. |
| Expected Inputs | When run, this command prompts you to select a node based on the inventory. If the selected nodes are Router or Rogger components, the following reasons are prompted for selection: Microsoft Updates install or rollback Engineering Special (ES) install Engineering Special (ES) rollback Maintenance Release (MR) install Maintenance Release (MR) rollback ISO or Major Release upgrade Other Maintenance Activity (excluding patching or upgrade operations) If you don't want to initiate maintenance mode for performing any operations mentioned in options 1 to 6, select option 7.
                                             Confirm to proceed with maintenance mode for the selected option. |
| Expected Outcome | Information about success or failure of the initiate maintenance
                                          command for a selected node is displayed. |

| Note | If either the Publisher or Subscriber or the active/inactive node is already in maintenance mode in any of the components,
                                             the other server cannot be initiated for maintenance. |
|---|---|

| Note | You can check the status of system maintenance initiate which is currently in-progress. For more information, see Check Status . |
|---|---|

| Note | Maintenance mode for IDS co-resident in 2000 Agents Deployment model is not
                                             supported |
|---|---|

| Command | utils upgrade-manager list |
|---|---|
| Description | This command is used to get a list of upgrade options available for the selected VOS or Windows node or
                                             group of nodes or all nodes in the inventory by selecting the option
                                             "All nodes in the inventory". . |
| Expected Inputs | Select a node or group of nodes or all nodes based on the inventory. |
| Expected Outcome | Displays information about available upgrade options for selected VOS or Windows nodes or
                                          group of nodes or all nodes in the inventory. If the selected node or
                                             group of nodes or all nodes are already running the latest software
                                             version, a message is displayed to indicate that. |

| Note | The subcomponents sequence dependencies aren’t validated as part of the upgrade compatibility. Refer to the upgrade guides
                                                   of the respective components for the correct sequence. For example, in Cisco Unified Customer Voice Portal, we have subcomponents
                                                   such as Operations Console, Unified Cisco Unified Customer Voice Portal Reporting Server, and Unified Cisco Unified Customer
                                                   Voice Portal Server. These must be upgraded in the required sequence. Orchestration ensures 15.0(1) ICM and CVP are deployed on the supported Windows Operating System. Before upgrading ICM or
                                                   CVP to 15.0(1), ensure that the Windows Operating System is upgraded to a supported version. Else, Orchestration will not
                                                   allow the upgrade to 15.0(1). Refer to Unified CCE 15.0(1) Compatibility Matrix for the details on supported Windows Operating System for ICM and CVP. CVP Reporting Server upgrade to 15.0(1) is not supported through Orchestration. For details on manually upgrading CVP Reporting
                                                   Server to 15.0(1), refer to the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal . |
|---|---|

| Command | utils upgrade-manager upgrade |
|---|---|
| Description | This command is used to upgrade VOS or Windows nodes or group of nodes  in the inventory. |
| Expected Inputs | Select the Windows or VOS node or group of nodes  that you want to upgrade. The following enhanced platform selection options are available when Cloud Connect 15.0.1 SU2 or later is installed: All Side A VOS nodes and All Side B VOS nodes under the VOS platform. These options allow the administrator to initiate the upgrade of all Side A or all Side B VOS nodes in parallel. Note Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes below. From the list of upgrade options available for the selected node, select the appropriate option and confirm. A compatibility
                                             check is then run in the background. During Call Server upgrade to 15.0(1), the following details are prompted to the administrator: Confirmation on whether manual backup of existing CVP installation folder and log files onto a different computer has been
                                                   completed. Details required for X.509 certificate creation. You will be able to enter "Common Name" or use hostname as "Common Name"
                                                   for each of the selected nodes. Option is provided to enter X.509 certificate fields that are common to all the selected nodes. If the selected node or group of nodes has either ROGGER, LOGGER or DISTRIBUTOR component for ICM and the selected upgrade
                                             option is a major release version (for example, 15.0(1)), you must confirm the following: If EDMT has been run on the selected nodes. Else, you must log in to the selected nodes and run EDMT to migrate the database
                                                   to the required version before triggering the upgrade from Orchestration. If the SQL Server Security Hardening must be applied on the applicable target nodes during the upgrade. You can also apply
                                                   Security Hardening settings after the upgrade by running the Security Wizard directly on the applicable target nodes. Once the upgrade procedure begins, you can see the progress details for each of the computers. You can also see the elapsed
                                             time since the procedure started. | Note | Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes below. |
| Note | Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes below. |
| Expected Outcome | The selected node or group of nodes  are upgraded. |

| Note | Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes below. |
|---|---|

| Note | For faster upgrades, the Cloud Connect server downloads locally all the new
                                                   software updates from the Cisco hosted repository at a predefined time. To start the Unified ICM services, post the successful completion of upgrade with reboot on Unified ICM nodes. See Start ICM Services . The option to upgrade “All nodes” in the deployment (VOS and Windows nodes together) to CCE 15.0(1) via Orchestration is not
                                                   supported. The administrator can upgrade the individual components to 15.0(1) by selecting the respective VOS or Windows nodes.
                                                   All nodes option is currently supported only for upgrading to CCE 12.6(x) By default, the selected operation is executed in parallel on all selected VOS nodes. To limit the number of nodes on which
                                                   the operation runs at the same time, configure the maximum parallel tasks value. For details, see the CLI To Configure Orchestration Maximum Parallel Tasks section. |
|---|---|

| Note | You can check the status of the upgrade that is currently in-progress. For more information, see Check Status . |
|---|---|

| Note | The All Side A/B VOS nodes option supports upgrade of target nodes to versions 15.0.1 and later. The same node selection (for example, All Side A VOS nodes ) cannot be operated on simultaneously from both the Cloud Connect Publisher and Subscriber. If any upgrade or patch operation
                                                      is already in progress on the All Side A VOS nodes selection from the Publisher, the same selection is blocked on the Subscriber,
                                                      and vice versa, until the operation completes. Simultaneous upgrade operations across alternate sides are also restricted. For example, if an upgrade operation is in progress
                                                      on All Side A VOS nodes from the Cloud Connect Publisher, then upgrade, rollback, or switch-forward operations on All Side B VOS nodes from the Cloud Connect Subscriber are blocked, and vice versa. However, patch install and rollback operations are not affected
                                                      and can proceed independently. All Side A/B VOS nodes option does not provide the ability to put nodes in maintenance mode before performing the upgrade operations for the All Side A/B
                                                      VOS option. If needed, place the relevant nodes in maintenance mode before starting the operation. Compatibility checks are not enforced by Orchestration for upgrade-manager operations on All Side A/B VOS nodes. The Cloud Connect component is excluded from All Side A/B VOS nodes upgrade-manager operations. When you select the All Side A/B VOS nodes option, Orchestration prompts you to perform the optional switch-forward operation at the end of the upgrade. If the selected
                                                      side includes publisher nodes, ensure that the switch-forward operation is performed in the required publisher-subscriber
                                                      sequence for the component. Performing switch-forward out of sequence may cause nodes to go out of cluster. When using the All Side A/B VOS nodes option for upgrade, each node on the selected side is evaluated individually. Nodes for which the selected upgrade is applicable
                                                      are processed; nodes that are not applicable are skipped. Upgrade operations using the All Side A/B VOS option do not run simultaneously on both the publisher and subscriber of the same VOS component (for example, CUIC). If both
                                                      the publisher and subscriber of a component are present on the selected side, the publisher is processed first and the subscriber
                                                      is skipped. You can retry the operation on skipped nodes after the current operation completes. |
|---|---|

| Command | utils upgrade-manager switch-forward |
|---|---|
| Description | This command is used to switch forward on target VOS node/cluster from Cloud Connect server. |
| Expected Inputs | Select the VOS node/cluster on which you want to perform the switch forward. You will see the details of the current active/inactive
                                          versions. Confirm to proceed with the switch forward. The following enhanced platform selection options are available when Cloud Connect 15.0.1 SU2 or later is installed: All Side A VOS nodes and All Side B VOS nodes under the VOS platform. These options allow the administrator to initiate the switch-forward of all Side A or all Side B VOS nodes in parallel. Note Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes under Upgrade a specific node or group of nodes . A compatibility check is then run in the background. If there are components whose versions are not compatible or the components are not onboarded as per the compatibility requirements,
                                                   a list of those components is displayed. Upgrade or switch forward the listed components to the required software versions
                                                   and re-run this command. If the versions of the associated components are compatible with the node’s inactive version, then the switch forward procedure
                                                   continues. Once the switch-forward procedure begins, you can see the progress details for each of the machines. You can also see the
                                             elapsed time since the procedure started. | Note | Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes under Upgrade a specific node or group of nodes . |
| Note | Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes under Upgrade a specific node or group of nodes . |
| Expected Outcome | The system restarts and the current version of the system is on a higher version. |

| Note | Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes under Upgrade a specific node or group of nodes . |
|---|---|

| Note | You can check the status of switch forward which is currently in-progress. For more information, see Check Status . By default, all selected nodes under VOS platform option are processed concurrently. If you have a specific requirement to
                                             limit concurrency, the value can be configured. For details, see the CLI To Configure Orchestration Maximum Parallel Tasks section. |
|---|---|

| Note | Orchestration does not allow rollback from major release versions, for example, 15.0(1), for Unified ICM and Unified CVP components.
                                             However, CVP components can be manually rolled back from major release versions on the target node(s). |
|---|---|

| Command | utils upgrade-manager rollback |
|---|---|
| Description | This command is used to roll back an upgrade on VOS or Windows nodes. |
| Expected Inputs | Select the Windows node or VOS node/cluster on which you want to perform the rollback. Once you select the nodes, only the
                                          nodes for which rollback is applicable will be displayed. For example, if you select three nodes and rollback is applicable
                                          for only one of them, you are asked to proceed with only one node. There is also a message displayed indicating that the machine
                                          would restart after the node is rolled back. Confirm to proceed. A compatibility check is then run in the background. The following enhanced platform selection options are available when Cloud Connect 15.0.1 SU2 or later is installed: All Side A VOS nodes and All Side B VOS nodes under the VOS platform. These options allow the administrator to initiate the rollback of all Side A or all Side B VOS nodes in parallel. Note Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes under Upgrade a specific node or group of nodes . If there are components whose versions aren’t compatible or if the components aren’t onboarded as per the compatibility requirements,
                                                   a list of these components is displayed. Roll back the listed components to the required software versions and then rerun
                                                   this command. Uninstallation is not supported for both Unified ICM and CVP 15.0(1) via Orchestration; however, Unified CVP 15.0(1) can be
                                                   manually uninstalled. When compatibility checks are enabled, components with versions incompatible with Unified ICM 15.0(1)
                                                   or CVP 15.0(1) can't be rolled back to a previous version. This restriction is in place because Unified ICM 15.0(1) and CVP
                                                   15.0(1) don't support uninstallation. However, this restriction won't apply if compatibility enforcement is disabled. For
                                                   more details on compatibility enforcement, see Enable or Disable Compatibility Enforcement . If the versions of the associated components are compatible with the selected node's rollback version, then the rollback procedure
                                                   begins. After the rollback procedure begins, you can see the progress details for each of the systems. You can also see the elapsed
                                          time since the procedure started. | Note | Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes under Upgrade a specific node or group of nodes . |
| Note | Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes under Upgrade a specific node or group of nodes . |
| Expected Outcome | The selected node or group of nodes is rolled back. |

| Note | Before selecting the All Side A VOS nodes or All Side B VOS nodes option, review the Prerequisites for All Side A/B VOS nodes option section and the associated Notes under Upgrade a specific node or group of nodes . |
|---|---|

| Note | To start Unified ICM services, post the successful completion of rollback upgrade with reboot on Unified ICM nodes. See Start ICM Services . |
|---|---|

| Note | You can check the status of the rollback which is currently in-progress. For more information, see Check Status . By default, all selected nodes under VOS platform option are processed concurrently. If you have a specific requirement to
                                             limit concurrency, the value can be configured. For details, see the CLI To Configure Orchestration Maximum Parallel Tasks section. |
|---|---|

| Command | utils deployment show in-progress |
|---|---|
| Description | This command is used to check the current status of any patch manager install, patch manager rollback, upgrade manager upgrade,
                                          upgrade manager rollback, switch-forward or system maintenance initiate . It also shows the subsequent progress, if applicable, for each node on which the procedure is initiated. If there is no procedure in progress, this command gives the last successful/failed procedure status. |
| Expected Inputs | NA |
| Expected Outcome | Shows the current status of the patch manager install, patch manager rollback, upgrade manager upgrade, upgrade manager rollback,
                                          switch-forward or system maintenance initiate for each node. If there is no active patch manager install, patch manager rollback, upgrade manager upgrade, upgrade manager rollback, switch-forward,
                                             or system maintenance initiate operations, then you see the status of the previous upgrade/rollback/maintenance if no other
                                             Orchestration operation is attempted post these operations. |

| Command | utils deployment show progress-HA |
|---|---|
| Description | This command is used to check the last known operation status run on
                                          remote node. This will only display the snapshot of the last known
                                          operation status and will not display the continuous status changes for
                                          the operation that is currently in progress. This command can be used to
                                          check the last known operation status on the remote node when the Cloud
                                          Connect node is not reachable. |
| Expected Inputs | NA |
| Expected Outcome | The snapshot of the last known operation status is displayed. |

| Note | Last known orchestration operation status will not be synchronized to remote node, in
                                             case of communication loss to remote node after initiating the orchestration
                                             operation and operation being completed before re-establishing the
                                             communication. |
|---|---|

| Command | utils system icm-services start |
|---|---|
| Description | This command is used to start the Unified ICM services from Cloud Connect server. This CLI will present the user with a list
                                          of Unified ICM hosts configured in the inventory, and the admin can select individual or group of Unified ICM hosts. |
| Expected Inputs | User should choose individual or group of Unified ICM hosts from the list. User should give confirmation yes/no to proceed with start of Unified ICM services |
| Expected Outcome | As part of CLI output, there are two kinds of messages which displays
                                          success as shown below: When the Unified ICM services are started successfully from stop state, the message “ Services started ” is displayed. When the Unified ICM services are already up and running, the message “ Services running ” is displayed. |

| Note | Before you configure the bandwidth using the utils set software-download bandwidth command, make sure the software is downloaded locally for the first time after the artifactory is successfully configured
                                             using the utils image-repository set command. To download the artifacts immediately after the configuration, use the utils initiate software-download command. |
|---|---|

| Command | utils set software-download bandwidth |
|---|---|
| Description | This command configures the bandwidth that the Orchestration feature uses to download software. |
| Expected inputs | When run, this command prompts for the following: Your confirmation with yes or no for turn-on or turn-off the bandwidth configuration. Enter a valid bandwidth value if you have chosen to turn-on the bandwidth configuration. Note Make sure to suffix the bandwidth value with M for Mbps, K for Kbps and None for Bytes per second. | Note | Make sure to suffix the bandwidth value with M for Mbps, K for Kbps and None for Bytes per second. |
| Note | Make sure to suffix the bandwidth value with M for Mbps, K for Kbps and None for Bytes per second. |
| Expected outcome | Following are the outcomes: Displays the success or failure message when you turn-on or turn-off the bandwidth configuration. If you have turned-on the bandwidth configuration and entered a valid value, this CLI validates and configures the entered
                                                      bandwidth value. |

| Note | Make sure to suffix the bandwidth value with M for Mbps, K for Kbps and None for Bytes per second. |
|---|---|

| Note | Make sure that you configure the bandwidth for software download, on the publisher and subscriber separately. Software download bandwidth control is disabled by default. The maximum available bandwidth is used during software download.
                                                      This might have an impact on the features supported by Cloud Connect only during software download. Cisco recommends minimum10-Mbps bandwidth for optimal software download. If you configure the bandwidth to a value that is
                                                      lesser than 10-Mbps, the duration of the software download increases and the orchestration operations cannot be performed
                                                      during the software download duration. If you configure the bandwidth to a value that is greater than the maximum available
                                                      bandwidth, the software download uses only the maximum available bandwidth. Proxy configured for orchestration might have an impact on the maximum available bandwidth for software download. Check the
                                                      proxy configuration and ensure the configured bandwidth will be available for the software download when proxy is used for
                                                      orchestration. |
|---|---|

| Command | utils initiate software-download |
|---|---|
| Description | This command initiates the software download from Cisco hosted software artifactory to Cloud Connect server. |
| Expected inputs | User confirmation with yes or no to proceed with software download. |
| Expected outcome | Displays the CLI message about the success or failure for the software download initiated. |

| Note | Software download must be planned during off-peak hours as it consumes network bandwidth and resources. The duration of the
                                                      download depends on the number of software that needs to be downloaded. Periodic software download happens everyday at 2 AM or at the time configured by admin. Use this CLI to initiate software
                                                      download before the next scheduled download. Software download needs to be initiated in the publisher and the subscriber separately. While software download is in progress
                                                      on the publisher, you can run the orchestration operation from the subscriber, or vice-versa. This CLI only initiates the software download and the download starts after prerequisites are met. |
|---|---|

| Command | utils system onboard update |
|---|---|
| Description | This command is used to update a node/cluster on a Cloud Connect node. |
| Expected Inputs | When run, this command prompts for: Cloud Connect server FQDN Cloud Connect application username and password |
| Expected Outcome | The existing node/cluster is updated in the Cloud Connect node inventory. |

| Note | After every successful update on Cloud Connect version 15.0(1) SU1 or later, refresh the deployment cache by executing the utils deployment cache initiate command on the Cloud Connect publisher node. Alternatively, the cache will update automatically during the next daily scheduled
                                             update. |
|---|---|

| Command | utils system onboard remove |
|---|---|
| Description | This command is used to remove a node/cluster from a Cloud Connect node. |
| Expected Inputs | When run, this command prompts for: Cloud Connect server FQDN Cloud Connect application username and password |
| Expected Outcome | The node/cluster is successfully removed from the Cloud Connect node inventory. |

| Note | After every successful remove on Cloud Connect version 15.0(1) SU1 or later, refresh the deployment cache by executing the utils deployment cache initiate command on the Cloud Connect publisher node. Alternatively, the cache will update automatically during the next daily scheduled
                                             update. |
|---|---|

| Note | If SSH connection is already established, skip Step 1 in the above procedure. |
|---|---|

| Command | show smtp-host |
|---|---|
| Description | This command is used to get the IP address or hostname of the SMTP server. |
| Expected Inputs | NA |
| Expected Outcome | Shows the configured IP address or host name of the SMTP server. If the smtp host details are not configured, a message is
                                                displayed indicating it. |

| Command | show smtp-from-email |
|---|---|
| Description | This command is used to get the email address from which the emails are triggered. This email address is not monitored and
                                                therefore not used for replying to any emails. |
| Expected Inputs | NA |
| Expected Outcome | Shows the email address from which the emails are triggered. If the smtp from-email is not configured, a message is displayed
                                                indicating it. |

| Command | show smtp-use-auth |
|---|---|
| Description | This command is used to know if SMTP authentication is enabled or not. |
| Expected Inputs | NA |
| Expected Outcome | SMTP authentication : <enable/disable> |

| Command | show smtp-user |
|---|---|
| Description | This command is used to show the user name to be used for SMTP server connection. |
| Expected Inputs | NA |
| Expected Outcome | Shows the SMTP username. If the smtp user details are not configured, a message is displayed indicating it. |

| Command | show smtp-pswd |
|---|---|
| Description | This command is used to know if the SMTP password is set or not. To reset the password, run the set smtp-pswd command. |
| Expected Inputs | NA |
| Expected Outcome | Shows whether the SMTP password is set or not. If the smtp password details are not configured, a message is displayed indicating
                                                it. |

| Command | utils smtp show subscriptions |
|---|---|
| Description | This command is used to get a list of all the email addresses subscribed for email notification. |
| Expected Inputs | NA |
| Expected Outcome | Shows the email addresses that are subscribed for email notification. If there is no email address subscribed, a message is displayed indicating it. |

| Command | utils smtp remove-config |
|---|---|
| Description | This command is used to remove the SMTP configuration from the control node. Email notification will no longer be sent to
                                          the subscribed email addresses. This command removes only the SMTP configuration, not the subscribed email addresses. |
| Expected Inputs | NA |
| Expected Outcome | SMTP configuration is deleted. |

| Command | utils smtp unsubscribe |
|---|---|
| Description | This command is used to remove one or more email addresses from the existing list of subscribers for email notification. Note You can get a list of subscribed email addresses using the utils smtp show subscriptions command. | Note | You can get a list of subscribed email addresses using the utils smtp show subscriptions command. |
| Note | You can get a list of subscribed email addresses using the utils smtp show subscriptions command. |
| Expected Inputs | Provide a list of valid email addresses, separated by commas, with no spaces in between. For example: utils smtp unsubscribe <emailaddress1,emailaddress2,.....emailaddressesN> You can also remove all the subscribed email addresses from the subscription list at once. To do that, run utils smtp unsubscribe all and confirm. |
| Expected Outcome | Removes the email addresses you provided as the input from the subscription list. |

| Note | You can get a list of subscribed email addresses using the utils smtp show subscriptions command. |
|---|---|

| Command | utils system inventory export |
|---|---|
| Description | This command is used to export inventory to an SFTP server location. The inventory file can then be viewed and edited as required. |
| Expected Inputs | When run, this command prompts for: SFTP Server: IP address of the SFTP remote server SFTP User SFTP User's Password SFTP Directory: Location of the remote server directory where the inventory needs to be exported Note Provide the location only; the filename is inventory.conf by default. | Note | Provide the location only; the filename is inventory.conf by default. |
| Note | Provide the location only; the filename is inventory.conf by default. |
| Expected Outcome | Inventory is exported to the SFTP server location. |

| Note | Provide the location only; the filename is inventory.conf by default. |
|---|---|

| Command | utils system inventory import |
|---|---|
| Description | This command is used to import inventory to Cloud Connect server. |
| Expected Inputs | When run, this command prompts for: SFTP Server: IP address of the SFTP remote server SFTP User SFTP User's Password SFTP Directory: Location of the remote server directory from where the inventory needs to be imported Note Provide the location only. The filename is inventory.conf by default. During inventory import, the inventory.conf filename should have the side information added for each node. For example, side: "A" /side: "B". During inventory import,
                                                                     the cluster information cannot be blank. It should have valid host details or a default value {}. For example, "ROGGER":{} | Note | Provide the location only. The filename is inventory.conf by default. During inventory import, the inventory.conf filename should have the side information added for each node. For example, side: "A" /side: "B". During inventory import,
                                                                     the cluster information cannot be blank. It should have valid host details or a default value {}. For example, "ROGGER":{} |
| Note | Provide the location only. The filename is inventory.conf by default. During inventory import, the inventory.conf filename should have the side information added for each node. For example, side: "A" /side: "B". During inventory import,
                                                                     the cluster information cannot be blank. It should have valid host details or a default value {}. For example, "ROGGER":{} |
| Expected Outcome | Inventory is imported to Cloud Connect server. |

| Note | Provide the location only. The filename is inventory.conf by default. During inventory import, the inventory.conf filename should have the side information added for each node. For example, side: "A" /side: "B". During inventory import,
                                                                     the cluster information cannot be blank. It should have valid host details or a default value {}. For example, "ROGGER":{} |
|---|---|

| Note | After successful import on Cloud Connect version 15.0(1) SU1 or later, it is recommended to update the deployment cache by
                                             running the CLI command utils deployment cache initiate , or you may wait for the daily scheduled update. |
|---|---|

| Note | For information on adding deployment type and deployment name in the inventory file, see Add Deployment Type and Deployment Name . |
|---|---|

| Note | Effective with release 15.0.1 SU1, the CLI command utils patch-manager export status has been renamed to utils deployment export-status . Please note that this is a nomenclature update only and does not impact the command's functionality. |
|---|---|

| Command | utils deployment export status |
|---|---|
| Description | This command is used to export the patch level details of a node or a group of nodes in a text file format. |
| Expected Inputs | Select the node(s) and enter the SFTP server details. |
| Expected Outcome | A text file with the current patch levels of the selected nodes is exported to the provided location. A success message is
                                          displayed along with the location where the file is saved. |

| Note | Software is downloaded separately on Cloud Connect publisher and subscriber. |
|---|---|

| Note | The authorized_keys extension type is File and you should not modify it. The user must have either domain admin or local administrator privilege. |
|---|---|

| Note | You must copy the Cloud Connect publisher and subscriber public keys into a single authorized_keys file. The publisher and subscriber entries should be in separate lines and should not use any extra space, comma, or any
                                             special characters at the end of the line. |
|---|---|

| Note | For more information on Windows security hardening, see the Windows Server Hardening section in the Security Guide for Cisco Unified Contact Center Enterprise . |
|---|---|

| Step 1 | Login to the Cloud Connect server using: https://<cloud connect hostname>:8443/cmplatform . |
|---|---|
| Step 2 | Navigate to Security > Certificate Management . |
| Step 3 | Click Find . |
| Step 4 | Click on the Tomcat certificate of the Cloud Connect server. |
| Step 5 | Download the .PEM file and save the file. |

| Step 1 | Login to the VOS node server using: https://<VOS node hostname>:8443/cmplatform . |
|---|---|
| Step 2 | Navigate to Security > Certificate Management . |
| Step 3 | Click on Upload Certificate/Certificate Chain. |
| Step 4 | Select ‘tomcat-trust’ from the drop-down list in the Certificate Purpose field. |
| Step 5 | Click Browse to upload the Cloud Connect server .PEM file . |
| Step 6 | Click Upload . |
| Step 7 | Restart the specific VOS node by running the utils system restart command. |

| Note | When Cloud Connect is running version 15.0(1) SU1, if you perform patch operations immediately after an upgrade, you must
                                             first update the cache by executing the utils deployment cache initiate command. This ensures the cache reflects the updated node versions before patching. |
|---|---|