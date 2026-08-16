---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-installatio-5c2c05f89a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/installation/guide/ucce_b_12_5_Install_upgrade_guide_ucce/hcs-cc_m_orchestration.html
retrieved_at: 2026-08-16T19:55:47.368874+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.5(1) and 12.5(2)

Updated: February 3, 2020

Chapter: CCE Orchestration

## Chapter: CCE Orchestration

# CCE Orchestration

## Overview

The Orchestration feature provides partners and administrators an option to automatically
                           download software updates and simplify the installation and rollback processes. The
                           Orchestration framework is built within the Cloud Connect server that connects to the
                           Cisco hosted cloud software repository. 
                           Orchestration currently supports installation and rollback of Cisco
                           Engineering Specials (ES), Service Updates (SU), Minor Releases (MR), and Microsoft
                           Patches.

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

Cloud Connect server downloads the available software from Cisco software
                                    repository every day at the configured time. Email notification is triggered
                                    from Cloud Connect server to subscribed users with software download failure
                                    details. Also, Cisco software artifactory will trigger an email notification
                                    with entitlement or compliance failure details to the email address mapped to
                                    CCO ID that is used to generate the Artifactory API key.

The name of the deployment is shown in the subject line of the email,
                                                      depending on the configuration in the inventory file.

For patch install or rollback, email notifications are not sent to
                                                      indicate whether the procedure is successful or if it is a
                                                      failure.

## Orchestration in CCE Deployment

The Orchestration feature is part of the Cloud Connect node that is configured in the CCE deployment.

To access this feature, Cloud Connect must be added to the inventory in the Unified CCE Administration console.

For more information, see Initial Configuration for Cloud Connect section in the Cisco Unified Contact CenterEnterprise Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-maintenance-guides-list.html .

### System Requirements

Cloud Connect 12.5(x) is obsolete. Cloud Connect 12.6(x) is required.

#### VOS Component Upgrade

Refer below for the minimum software version required to enable this feature for the
                                 following components:

Finesse

CUIC/LD/IDS/Co-resident

VVB

Apply the ES ucos.orchestration.enable-12.5.1.cop.sgn on the above-mentioned
                                 components with 12.5(1) version to on-board and orchestrate VOS nodes from Cloud
                                 Connect server.

Before initiating 12.5(2) or 12.6(1) upgrade on VOS nodes from Orchestration, install the mandatory ES ucos.keymanagement.v01.cop.sgn from Orchestration on target 12.5(1) VOS nodes.

#### Windows Component Upgrade

Unified ICM 12.5(1)

Install mandatory ES66 or Unified ICM 12.5(2) manually

Unified ICM 12.5(1) nodes onboarded with manual install of ES66 will get an option for upgrade to or rollback from Unified
                                             CCE 12.5(2) and 12.6(1)

Unified CVP 12.5(1)

Install mandatory ES23 manually

### Orchestration Support using Cloud Connect Server

Cloud Connect 12.6(x) supports orchestration in the following scenarios:

Unified CCE 12.5(x) ES, Unified CCE 12.6(x) ES and Windows Updates can be orchestrated from Cloud Connect 12.6(x)

Unified CCE 12.5(x) to Unified CCE 12.6(x), software upgrade can be orchestrated from Cloud Connect 12.6(x)

Unified CCE 12.5(1) to Unified CCE 12.5(2) software upgrade is supported in orchestration.

Unified CCE 12.5(2) to Unified CCE 12.6(1) upgrade is not supported either manually or via orchestration.

See System Requirements for minimum software requirement to enable
                              orchestration for the above supported model.

### Orchestration Deployment Task Flow

### Administration Task Flow

### Maintenance Task Flow

### Deployment Tasks

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

Step 4

Import the inventory back from the SFTP server by running the command utils system inventory import on the Cloud Connect publisher node. For details, see Export and Import of Nodes Managed by Orchestration Control Node .

#### Add Deployment Type and Deployment Name

Step 1

Download the inventory to an SFTP server by running the utils system inventory export command. For details, see Export and Import of Nodes Managed by Orchestration Control Node .

Step 2

Edit the following strings in the inventory file,

deploymentType : This field is used for compatibility check during an upgrade or rollback or switch forward procedure. The supported deployment
                                                      types are:

UCCE-2000-Agents

UCCE-4000-Agents

PCCE-2000-Agents

PCCE-4000-Agents

HCS-CC-2000-Agents

HCS-CC-4000-Agents

Orchestration is not supported for 12000, 24000 and 36000 agent deployment models. HCS-SCC (Small Contact Center ) deployment model is currently not supported for Orchestration.

Ensure that the values entered in this field conform to the above format.

deploymentName :
                                                      Provide a unique name for the deployment.

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

##### Validate Email Configuration

Validate the configuration by running the utils smtp test-connection command.

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

#### Check Installed Software Version and Patches

To check the currently installed software version and patches on a node or group of nodes 
                                 in either Windows
                                 or VOS systems, run the utils deployment show status command.

#### Install or Roll Back Patch for Cloud Connect Server

To install a patch or to roll back a previously installed patch on Cloud Connect server , run the utils system upgrade initiate command. The Local Repository option in this command lists the patches  available from Cisco artifactory for patch install or rollback  on Cloud Connect
                                 server. This command can be run separately on the Cloud Connect publisher and subscriber nodes.

The Local Repository option is also available on the Cisco Unified OS Administration web page of Cloud Connect server. Select this option to install
                                             a patch or to roll back a previously installed patch on Cloud Connect server .

Select the patch to install or roll back .

Optionally, to receive email notification about the status of the patch installation
                                             or rollback  for
                                             Cloud Connect server, provide the SMTP host server details when prompted by the
                                             CLI.

Patch install or rollback  on Cloud Connect server initiated using utils system upgrade initiate command can be canceled using utils system upgrade cancel command. The utils system upgrade status command can be used to check the status.

Use the CLI command utils initiate software-download to download the Unified ICM and Unified CVP 15.0(1) software to the Cloud Connect Server after upgrading Cloud Connect to
                                             15.0(1) for both publisher and subscriber nodes. Alternatively, wait for the default or scheduled software download to finish
                                             before starting the Unified CVP/ICM upgrade to 15.0(1).

#### List Available Patches for Specific Node or Group of Nodes

To get a list of available patches for a specific node or group of nodes in the inventory, run
                                 the utils patch-manager list command.

#### Install Patch to Specific Node or Group of Nodes

To install patch to a specific node or group of nodes, run the utils patch-manager
                                    install command.

You can check the status of the patch install which is currently in-progress. For more information, see Check Status .

#### Roll Back Patch from Specific Node or Group of Nodes

To roll back a previously installed patch on a specific node or a group of nodes, run the utils patch-manager rollback command.

In case of Windows-based nodes, the latest applied patch is
                                             allowed to roll back. In case of VOS-based nodes, the latest applied
                                             ES is rolled back.

You can check the status of patch rollback which is currently in-progress. For more information, see Check Status .

#### Install Windows Updates to Specific Node or Group of Nodes

To install Windows updates to a node or group of nodes or all Windows nodes, run the utils patch-manager ms-patches install command.

Before running this command, refer to the recommended guidelines in the Microsoft Security Updates section of the SecurityGuide for CiscoUnified ICM/Contact Center Enterprise at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

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

#### Roll Back Windows Update from Specific Node or Group of Nodes

To roll back Windows update from a specific node or group of nodes or all Windows nodes, run the utils patch-manager ms-patches rollback command.

Before running this command, refer to the recommended guidelines in the Microsoft Security Updates section of the SecurityGuide for CiscoUnified ICM/Contact Center Enterprise at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

Listing of Windows updates available for rollback is not supported.

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

#### List Available Upgrade Options

To get a list of available upgrade options for VOS and Windows nodes individually or for group of
                                 nodes  in the
                                 inventory, run the utils upgrade-manager list command.

If the selected node or
                                             group of nodes or all nodes are already running the latest software
                                             version, a message is displayed to indicate that.

#### Upgrade a Specific Node or Group of Nodes or All Nodes

To perform software version upgrades on VOS or Windows nodes
                                 , run the utils upgrade-manager
                                    upgrade command from the Cloud Connect server. It is recommended to run
                                 this command during a maintenance window as the procedure involves system restart that
                                 will cause service outage.

For the selected VOS or Windows component for upgrade, a compatibility check is performed in the background based on the configured
                                 deployment type to ensure that all the associated components  If the components are onboarded and the required dependent components
                                 are either in same target upgrade version or backward compatible version, the upgrade procedure begins. However, if the components
                                 are not onboarded, you have to onboard them first or if the versions are not compatible, upgrade them to the required version.
                                 For example, if you select to upgrade the Rogger nodes to 12.6(1) version, the inter-component compatibility check is run
                                 for the Rogger dependent components such as Finesse, CVP, VVB, CUIC. These must already be in 12.6(1) version and PG must
                                 be backward compatible version, that is, 12.5(1) or 12.0(1) .

The sub-components sequence dependencies are not validated as part of the upgrade compatibility. Refer to the upgrade guides
                                             of the respective components for the correct sequence. For example, in case of CVP, we have sub-components such as Operations
                                             Console, Unified CVP Reporting Server and Unified CVP Server. These must be upgraded in the required sequence.

For VOS node/cluster, switch forward is optional at the end of upgrade. If administrators opt for
                                 switch forward, the target node is restarted and the active/inactive partition is
                                 switched. If they decide not to switch forward, the upgraded version remains in the
                                 inactive partition of the target node. Switch forward for these nodes can be performed
                                 later. For details, see Perform Switch Forward on Specific VOS Node or Group of Nodes .

For VOS cluster, the upgrade or the switch forward procedure is performed first on the
                                 publisher and then on the subscriber nodes. If switch forward is performed immediately
                                 after an upgrade, the overall procedure takes a significant amount of time; hence plan
                                 the maintenance window accordingly.

From the list of upgrade options available for the
                                             selected node or group of nodes or all nodes, select the appropriate
                                             option and confirm. A compatibility check is then run in the
                                             background.

Once the upgrade procedure begins, you can see the
                                             progress details for each of the machines. You can also see the
                                             elapsed time since the procedure started.

For faster upgrades, the Cloud Connect server downloads locally all the new
                                                   software updates from the Cisco hosted repository at a predefined time.

All nodes upgrade to 12.5(2) is not supported.

You can check the status of upgrade which is currently in-progress. For more information, see Check Status .

#### Perform Switch Forward on Specific VOS Node or Group of Nodes

Administrators can perform switch forward on target VOS nodes independently. When the active partition is on lower version
                                 and the inactive partition is on higher version, run the utils upgrade-manager switch-forward command to perform a switch forward. It is recommended to run this command during a maintenance window as the procedure involves
                                 system restart that will cause service outage.

A compatibility check is then run in the
                                             background.

Once the
                                             switch-forward procedure begins, you can see the progress details
                                             for each of the machines. You can also see the elapsed time since
                                             the procedure started.

You can check the status of switch forward which is currently in-progress. For more information, see Check Status .

#### Roll Back Upgrade from Specific Node or Group of Nodes

To roll back an upgrade on VOS or Windows nodes, run the utils upgrade-manager rollback command from the Cloud Connect server. It is recommended to run this command during a maintenance window as the procedure
                                 involves system restart that will cause service outage.

For the selected VOS or Windows component for rollback, a compatibility check is
                                 performed in the background to ensure that all the associated components  versions
                                 are compatible. If the components are onboarded and the versions are compatible with
                                 each other, the rollback procedure begins. However, if the components are not onboarded,
                                 you have to onboard them first or if the versions are not compatible, roll them back to
                                 the required version.

For VOS nodes/cluster, the rollback (switch backward) must be initiated from an active higher version to an inactive lower
                                 version of the node. Also, the publisher node of the managed cluster must be rolled back before the subscriber node of the
                                 cluster.

If there are components whose versions are not compatible or
                                                   if the components are not onboarded as per the compatibility
                                                   requirements, a list of these components is displayed. Roll
                                                   back the listed components to the required software versions
                                                   and then re-run this command.

If the versions of the associated components are compatible
                                                   with the selected node's rollback version, then the rollback
                                                   procedure begins.

You can check the status of rollback which is currently in-progress. For more information, see Check Status .

#### Check Status

To check the current status of patch manager install, patch manager rollback, upgrade manager upgrade, upgrade manager rollback,
                                 switch-forward, , run the utils deployment show in-progress command. You can run this command if connectivity to CLI is lost after initiating any of above procedures.

If there is no procedure in progress, this command gives the last successful/failed procedure status.

If there is no patch
                                             manager install, patch manager rollback, upgrade manager upgrade,
                                             upgrade manager rollback, switch-forward, then you see the status of the previous upgrade,
                                             rollback.

#### Start Unified ICM Services

To start Unified ICM services from Cloud Connect server, run the utils system icm-services start command.

User should choose individual or group of Unified ICM hosts from the list.

User should give confirmation yes/no to proceed with start of Unified ICM services

When the Unified ICM services are started successfully from stop state, the message “ Services started ” is displayed.

When the Unified ICM services are already up and running, the message “ Services running ” is displayed.

### Maintenance Tasks

#### Update VOS Nodes Onboarded to Orchestration Control Node

To update VOS based nodes that have been onboarded, run the utils system onboard update command from the publisher node in the VOS node/cluster that you want to update.

Cloud Connect server FQDN

Cloud Connect application username and password

#### Remove VOS Nodes from Orchestration Control Node

To remove any existing VOS-based node or cluster, run the utils system onboard remove command from the publisher node in the VOS node/cluster that you want to remove.

Cloud Connect server FQDN

Cloud Connect application username and password

#### Update Windows Nodes Onboarded to Orchestration Control Node

The update procedure is similar to the onboarding procedure described in Onboard Windows nodes to orchestration control node .

If SSH connection is already established, skip Step 1 in the above procedure.

#### Validate Updated Nodes Onboarded for Orchestration

The procedure to validate updated nodes that have been onboarded is the same as described in Validate Onboarded Nodes for Orchestration .

#### Configure Email Configuration

You can check your email configuration details by running the respective commands as described below:

Get the IP address and hostname of the SMTP server by running the show smtp-host command.

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

For information on adding deployment type and deployment name in the inventory file, see Add Deployment Type and Deployment Name .

#### Export Current Patch Level Details

Available patches for nodes in the deployment can be obtained in either of the following ways:

Email Notification

Using the utils patch-manager list command.

Current patch levels can be exported in text file format using the utils patch-manager export status command.

#### Serviceability

Audit Logs

Audit trial for administrative operation that is initiated from Orchestration CLI on
                                 Cloud Connect is captured in Orchestration Audit logs. Audit trial captures the user,
                                 action and date/time details of the CLI operation.

CLI Logs

Run the following command on the Cloud Connect node to retrieve CLI logs:

file get activelog platform/log/cli*.log

Ansible Logs

Run the following commands on the Cloud Connect node to retrieve ansible-related
                                 logs:

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

Ansible logs by selecting 'Ansible Controller' as the service

Audit logs by selecting 'Orchestration Audit' as the service

To download RTMT from Cloud Connect, access https://FQDN:8443/plugins/CcmServRtmtPlugin.exe .

For more information, refer to the Cisco Unified Real-Time Monitoring Tool
                                    Administration Guide at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

For logs on individual components, refer to the Serviceability Guide for Cisco
                                    Unified ICM/Contact Center Enterprise available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

## Configure SSH public key on Windows nodes

This section describes how to establish password-less Secure Shell (SSH) connection between Cloud Connect server and Windows
                           node (CVP and ICM) using an SSH public key. The Windows node can be in a Workgroup or Domain.

If the Windows node (CVP and ICM) version is 12.5, install 12.5 mandatory ES or MR patch before performing this procedure. See System Requirements for details.

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

For more information on Windows security hardening, see the Windows Server Hardening section in the Security Guide for Cisco Unified ICM/Contact Center Enterprise .

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

Orchestration is not supported for CTIOS, Customer Collaboration Platform (CCP),
                                 ECE, CCDM, CCMP, and non-Contact Center Cisco products such as UCM, Unity
                                 Connection, CUBE gateways, CUSP, IM&P etc. Patches and upgrade operations
                                 for these components can be performed in a traditional manner.

Orchestration is supported only for upgrades and patch install and not for tech
                                 refresh or fresh install.

If any activity is blocked with a message previous orchestration or
                                    upgrade operation is still in progress even if there is no active
                                 operation, then restart Cloud Connect server.

If one component ES has a dependency on another component ES, then they have to
                                 be taken into consideration by the administrator before initiating the patch
                                 installation from Cloud Connect server. The administrator should read the
                                 release notes that is notified through an email to understand the dependency.
                                 The Orchestration framework does not track this aspect automatically. For
                                 example, if an ES of Finesse has a dependency on an ES of Live Data and has to
                                 be installed in a specific order, then the administrator must consider this
                                 before initiating the patch installation from Cloud Connect server.

Within Upgrade commands 'All Nodes' option for the Roll Back and Switch version
                                 commands are not available.

Only Microsoft Exchange Server is supported for email notification; Office 365
                                 and Gmail are not supported as of now.

Email notifications are triggered about the available software upgrade from the
                                 publisher node of Cloud Connect server. If the publisher node is down at the
                                 trigger time, then the Admin will not receive any notification.

All nodes option in utils upgrade-manager list CLI uses an internal cache, which is updated every day at 5 AM. The latest version of components that are upgraded before
                                 the cache update scheduled time will not be listed in All nodes option. The latest version of components can be listed by
                                 selecting the individual VOS or Windows or group of nodes option in the utils upgrade-manager list CLI. The cache update can be enforced by running the utils system inventory import CLI.

For Packaged CCE deployment, only multistage upgrade is supported from Orchestration.

For Packaged CCE deployment, CVPOAMP is not supported.

| Note | The name of the deployment is shown in the subject line of the email,
                                                      depending on the configuration in the inventory file. For patch install or rollback, email notifications are not sent to
                                                      indicate whether the procedure is successful or if it is a
                                                      failure. |
|---|---|

| Note | Cloud Connect 12.6(1) requires the latest ES i.e., cloudconnect.1261.ES04.23.cop.sgn or above on both the publisher and subscriber nodes of Cloud Connect server. You must apply this ES before initiating any
                                       orchestration commands. |
|---|---|

| Note | Before initiating 12.5(2) or 12.6(1) upgrade on VOS nodes from Orchestration, install the mandatory ES ucos.keymanagement.v01.cop.sgn from Orchestration on target 12.5(1) VOS nodes. |
|---|---|

| Unified ICM 12.5(1) | Install mandatory ES66 or Unified ICM 12.5(2) manually | Unified ICM 12.5(1) nodes onboarded with manual install of ES66 will get an option for upgrade to or rollback from Unified
                                             CCE 12.5(2) and 12.6(1) |
|---|---|---|
| Unified CVP 12.5(1) | Install mandatory ES23 manually |  |

| Note | Unified CCE 12.5(1) to Unified CCE 12.5(2) software upgrade is supported in orchestration. Unified CCE 12.5(2) to Unified CCE 12.6(1) upgrade is not supported either manually or via orchestration. |
|---|---|

|  |
|---|
|  |
|  |
| Onboard VOS Nodes to Orchestration Control Node |
| Onboard Windows nodes to orchestration control node |
| Add Deployment Type and Deployment Name |
| Validate Onboarded Nodes for Orchestration |
|  |
| Configure Email Notification |
| Configure Windows Server for Updates (Optional) |

| Check Installed Software Version and Patches |
|---|
| Install or Roll Back Patch for Cloud Connect Server |
| List Available Patches for Specific Node or Group of Nodes |
| Install Patch to Specific Node or Group of Nodes |
| Roll Back Patch from Specific Node or Group of Nodes |
| Install Windows Updates to Specific Node or Group of Nodes |
| Roll Back Windows Update from Specific Node or Group of Nodes |
| Enable or Disable Compatibility Enforcement |
|  |
| List Available Upgrade Options |
| Upgrade a Specific Node or Group of Nodes or All Nodes |
| Perform Switch Forward on Specific VOS Node or Group of Nodes |
| Roll Back Upgrade from Specific Node or Group of Nodes |
|  |
|  |
|  |

|  |
|---|
|  |
|  |
| Update VOS Nodes Onboarded to Orchestration Control Node |
| Remove VOS Nodes from Orchestration Control Node |
| Update Windows Nodes Onboarded to Orchestration Control Node |
| Validate Updated Nodes Onboarded for Orchestration |
| Configure Email Configuration |
| Delete Configuration for Email Notification |
| Unsubscribe Email Notification |
| Export and Import of Nodes Managed by Orchestration Control Node |
| Export Current Patch Level Details |
| Serviceability |
|  |

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

| Step 1 | Configure SSH public key on the Windows nodes by following the steps in the section Configure SSH public key on Windows nodes . |
|---|---|
| Step 2 | From the cloud connect server, run the utils system inventory export command to download the inventory to an SFTP server. For details, see Export and Import of Nodes Managed by Orchestration Control Node . |
| Step 3 | Edit the inventory file to include the Windows components. Refer to the default template section in the inventory file. Note The syntax, alignment, and indentation must be exactly the same as mentioned in the inventory file. Ensure the CRLF line endings are of UNIX-Style. Use a Linux-based or a Mac OS-based editor to create the Windows inventory
                                                                  file. The following fields in the inventory file are mandatory. Field Description ProductName The ProductName mentioned in the inventory file must be in uppercase and cannot be changed. For example, CVPREPORTING, CVPSERVER, CVPOAMP,
                                                            DISTRIBUTOR, LOGGER, PG, ROGGER or ROUTER. Pair under product This is a user-defined pair name. Hostname This can be a valid IP, or hostname, or FQDN name of the target node. Side of the deployment It can either be A or B. User configured on host This is the username for which the SSH keys are configured in Step 1. Note The user must have either domain admin or local administrator privilege. | Note | The syntax, alignment, and indentation must be exactly the same as mentioned in the inventory file. Ensure the CRLF line endings are of UNIX-Style. Use a Linux-based or a Mac OS-based editor to create the Windows inventory
                                                                  file. | Field | Description | ProductName | The ProductName mentioned in the inventory file must be in uppercase and cannot be changed. For example, CVPREPORTING, CVPSERVER, CVPOAMP,
                                                            DISTRIBUTOR, LOGGER, PG, ROGGER or ROUTER. | Pair under product | This is a user-defined pair name. | Hostname | This can be a valid IP, or hostname, or FQDN name of the target node. | Side of the deployment | It can either be A or B. | User configured on host | This is the username for which the SSH keys are configured in Step 1. Note The user must have either domain admin or local administrator privilege. | Note | The user must have either domain admin or local administrator privilege. |
| Note | The syntax, alignment, and indentation must be exactly the same as mentioned in the inventory file. Ensure the CRLF line endings are of UNIX-Style. Use a Linux-based or a Mac OS-based editor to create the Windows inventory
                                                                  file. |
| Field | Description |
| ProductName | The ProductName mentioned in the inventory file must be in uppercase and cannot be changed. For example, CVPREPORTING, CVPSERVER, CVPOAMP,
                                                            DISTRIBUTOR, LOGGER, PG, ROGGER or ROUTER. |
| Pair under product | This is a user-defined pair name. |
| Hostname | This can be a valid IP, or hostname, or FQDN name of the target node. |
| Side of the deployment | It can either be A or B. |
| User configured on host | This is the username for which the SSH keys are configured in Step 1. Note The user must have either domain admin or local administrator privilege. | Note | The user must have either domain admin or local administrator privilege. |
| Note | The user must have either domain admin or local administrator privilege. |
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
| User configured on host | This is the username for which the SSH keys are configured in Step 1. Note The user must have either domain admin or local administrator privilege. | Note | The user must have either domain admin or local administrator privilege. |
| Note | The user must have either domain admin or local administrator privilege. |

| Note | The user must have either domain admin or local administrator privilege. |
|---|---|

| Step 1 | Download the inventory to an SFTP server by running the utils system inventory export command. For details, see Export and Import of Nodes Managed by Orchestration Control Node . |
|---|---|
| Step 2 | Edit the following strings in the inventory file, deploymentType : This field is used for compatibility check during an upgrade or rollback or switch forward procedure. The supported deployment
                                                      types are: UCCE-2000-Agents UCCE-4000-Agents PCCE-2000-Agents PCCE-4000-Agents HCS-CC-2000-Agents HCS-CC-4000-Agents Note Orchestration is not supported for 12000, 24000 and 36000 agent deployment models. HCS-SCC (Small Contact Center ) deployment model is currently not supported for Orchestration. Ensure that the values entered in this field conform to the above format. deploymentName :
                                                      Provide a unique name for the deployment. This
                                                   name appears in the subject line of the email
                                                   notification. If it is not configured, the subject
                                                   line of the email notification contains only the
                                                   type of procedure and the overall status. | Note | Orchestration is not supported for 12000, 24000 and 36000 agent deployment models. HCS-SCC (Small Contact Center ) deployment model is currently not supported for Orchestration. |
| Note | Orchestration is not supported for 12000, 24000 and 36000 agent deployment models. HCS-SCC (Small Contact Center ) deployment model is currently not supported for Orchestration. |
| Step 3 | Import the inventory back from the SFTP server by running the
                                             utils system inventory import command on the Cloud Connect
                                             publisher node. For details, see Export and Import of Nodes Managed by Orchestration Control Node . |

| Note | Orchestration is not supported for 12000, 24000 and 36000 agent deployment models. HCS-SCC (Small Contact Center ) deployment model is currently not supported for Orchestration. |
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
| 2 | Validate Email Configuration |
| 3 | Subscribe to Email Notification |
| 4 | Configure Email Notification |

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
| Description | This command is used to establish a connection to the SMTP server using the given configuration. |
| Expected Inputs | NA |
| Expected Outcome | Shows whether SMTP connection is successful or not. |

| Command | utils smtp subscribe |
|---|---|
| Description | This command is used to specify the email addresses that subscribe to the email notifications. |
| Expected Inputs | Provide a list of valid email addresses, separated by commas, with no spaces in between. For example: utils smtp subscribe <emailaddress1,emailaddress2,.....emailaddressesN> |
| Expected Outcome | Email addresses provided are subscribed for notification. |

| Command | utils deployment show status |
|---|---|
| Description | This command is used to check the currently installed software version and patches for the
                                          selected Windows or VOS node individually or group of nodes |
| Expected Inputs | Select the node or group of nodes or all nodes from the inventory. |
| Expected Outcome | Displays information about the installed software version and the patches for the selected
                                          node or group of nodes or all nodes from the inventory. If there is no
                                          patch installed, a message "No patch installed" is displayed to indicate
                                          that along with software version. |

| Note | The Local Repository option is also available on the Cisco Unified OS Administration web page of Cloud Connect server. Select this option to install
                                             a patch or to roll back a previously installed patch on Cloud Connect server . |
|---|---|

| Command | utils system upgrade initiate |
|---|---|
| Description | This command is used to initiate the patch install or to roll back the previously installed patch on Cloud Connect server
                                          . The patches  available for patch install or rollback  are listed from Cisco artifactory. |
| Expected Inputs | Select the Local Repository option to list the patches  available for patch install or rollback . Select the patch to install or roll back . |
| Expected Outcome | The selected patch for install or rollback is installed on Cloud
                                          Connect server . |

| Note | Optionally, to receive email notification about the status of the patch installation
                                             or rollback  for
                                             Cloud Connect server, provide the SMTP host server details when prompted by the
                                             CLI. |
|---|---|

| Note | Patch install or rollback  on Cloud Connect server initiated using utils system upgrade initiate command can be canceled using utils system upgrade cancel command. The utils system upgrade status command can be used to check the status. |
|---|---|

| Note | Use the CLI command utils initiate software-download to download the Unified ICM and Unified CVP 15.0(1) software to the Cloud Connect Server after upgrading Cloud Connect to
                                             15.0(1) for both publisher and subscriber nodes. Alternatively, wait for the default or scheduled software download to finish
                                             before starting the Unified CVP/ICM upgrade to 15.0(1). |
|---|---|

| Command | utils patch-manager list |
|---|---|
| Description | This command is used to get a list of patches available for installation for a specific node
                                          or group of nodes based on the selected option. |
| Expected Inputs | Select a node or group of nodes based on the inventory. |
| Expected Outcome | Displays information about available patches for the selected node or group of nodes. |

| Command | utils patch-manager install |
|---|---|
| Description | This command is used to install patches on a specific node or group of nodes onboarded to the
                                          Cloud Connect inventory. |
| Expected Inputs | From the list of Windows/VOS nodes displayed, select the node or group of Windows/VOS nodes on which the patch needs to be
                                          installed. Once you select the nodes, only the nodes for which patches are available will be displayed. For example, if you
                                          select 3 nodes and Windows/VOS patches are available for only 1 of them, you are asked to proceed with only one node. Confirm
                                          to proceed. You are also asked to confirm whether the target node needs to be rebooted after installing the patch.Next, you
                                          are asked to provide confirmation on rebooting the node after installing the patch. |
| Expected Outcome | The selected patch is installed on the selected node or group of nodes. |

| Note | You can check the status of the patch install which is currently in-progress. For more information, see Check Status . |
|---|---|

| Command | utils patch-manager rollback |
|---|---|
| Description | This command is used to roll back previously installed patches on a specific node or group of
                                          nodes. In case of Windows-based nodes, the latest applied patch is
                                             allowed to roll back. In case of VOS-based nodes, the latest applied
                                             ES is rolled back. |
| Expected Inputs | From the list of Windows/VOS nodes displayed, select the node or group of Windows/VOS nodes on which the patch needs to be
                                          rolled back. Once you select the nodes, only the nodes for which Windows/VOS patch rollback is available will be displayed.
                                          For example, if you select 3 nodes and Windows/VOS patch rollback is available for only 1 of them, you are asked to proceed
                                          with only one node. There is also a message displayed indicating that the machine would restart after the patch is rolled
                                          back. Confirm to proceed.Next, you are asked to provide confirmation on rebooting the node after rollback. |
| Expected Outcome | The previously installed patch is rolled back on the selected node or group of nodes. |

| Note | You can check the status of patch rollback which is currently in-progress. For more information, see Check Status . |
|---|---|

| Note | Before running this command, refer to the recommended guidelines in the Microsoft Security Updates section of the SecurityGuide for CiscoUnified ICM/Contact Center Enterprise at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
|---|---|

| Command | utils patch-manager ms-patches install |
|---|---|
| Description | This command is used to install the latest Windows updates to a node or a group of Windows
                                          nodes or all Windows nodes. |
| Expected Inputs | From the list of Windows nodes displayed, select the node or group of Windows nodes or all Windows nodes to which the updates
                                          need to be applied. You can also select all the Windows nodes in the inventory. Once you select the nodes, only the nodes
                                          for which Windows updates are available will be displayed. For example, if you select 3 nodes and Windows updates are available
                                          for only 1 of them, you are asked to proceed with only one node. Confirm to proceed. You are asked to confirm whether the
                                          target nodes needs to be rebooted after installing the updates.Next, you are asked to provide confirmation on rebooting the
                                          node after installing the patch. |
| Expected Outcome | The selected Windows updates are installed on the selected node or group of nodes or all
                                          Windows nodes. |

| Note | Before running this command, refer to the recommended guidelines in the Microsoft Security Updates section of the SecurityGuide for CiscoUnified ICM/Contact Center Enterprise at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html Listing of Windows updates available for rollback is not supported. |
|---|---|

| Command | utils patch-manager ms-patches rollback |
|---|---|
| Description | This command is used to roll back a specific Windows update from a specific node or group of
                                          nodes or all Windows nodes. |
| Expected Inputs | Select the node or group of Windows nodes or all Windows nodes on which the rollback needs to be performed. You can also select
                                          all the Windows nodes in the inventory for rollback. Provide the Knowledge Base (KB) number you want to rollback. You are
                                          asked to confirm whether the target nodes need to be rebooted after rollback.Next, you are asked to provide confirmation on
                                          rebooting the node after rollback. |
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

| Command | utils upgrade-manager list |
|---|---|
| Description | This command is used to get a list of upgrade options available for the selected VOS . |
| Expected Inputs | Select a node or group of nodes or all nodes based on the inventory. |
| Expected Outcome | Displays information about available upgrade options for selected VOS or Windows nodes or
                                          group of nodes or all nodes in the inventory. If the selected node or
                                             group of nodes or all nodes are already running the latest software
                                             version, a message is displayed to indicate that. |

| Note | The sub-components sequence dependencies are not validated as part of the upgrade compatibility. Refer to the upgrade guides
                                             of the respective components for the correct sequence. For example, in case of CVP, we have sub-components such as Operations
                                             Console, Unified CVP Reporting Server and Unified CVP Server. These must be upgraded in the required sequence. |
|---|---|

| Command | utils upgrade-manager upgrade |
|---|---|
| Description | This command is used to upgrade VOS or Windows nodes or group of nodes  in the
                                          inventory. |
| Expected Inputs | Select the Windows or VOS node or group of nodes  that you want to
                                          upgrade. From the list of upgrade options available for the
                                             selected node or group of nodes or all nodes, select the appropriate
                                             option and confirm. A compatibility check is then run in the
                                             background. Once the upgrade procedure begins, you can see the
                                             progress details for each of the machines. You can also see the
                                             elapsed time since the procedure started. |
| Expected Outcome | The selected node or group of nodes or all nodes is upgraded. |

| Note | For faster upgrades, the Cloud Connect server downloads locally all the new
                                                   software updates from the Cisco hosted repository at a predefined time. All nodes upgrade to 12.5(2) is not supported. |
|---|---|

| Note | You can check the status of upgrade which is currently in-progress. For more information, see Check Status . |
|---|---|

| Command | utils upgrade-manager switch-forward |
|---|---|
| Description | This command is used to switch forward on target VOS node/cluster from Cloud Connect server. |
| Expected Inputs | Select the VOS node/cluster on which you want to perform the switch forward. You will see the
                                          details of the current active/inactive versions. Confirm to proceed with
                                          the switch forward. A compatibility check is then run in the
                                             background. Once the
                                             switch-forward procedure begins, you can see the progress details
                                             for each of the machines. You can also see the elapsed time since
                                             the procedure started. |
| Expected Outcome | The system restarts and the current version of the system is on a higher version. |

| Note | You can check the status of switch forward which is currently in-progress. For more information, see Check Status . |
|---|---|

| Command | utils upgrade-manager rollback |
|---|---|
| Description | This command is used to roll back an upgrade on VOS or Windows nodes. |
| Expected Inputs | Select the Windows node or VOS node/cluster on which you want to perform the rollback. The
                                          rollback option is listed for the selected node or group of nodes.
                                          Select the appropriate option and confirm. A compatibility check is then
                                          run in the background. If there are components whose versions are not compatible or
                                                   if the components are not onboarded as per the compatibility
                                                   requirements, a list of these components is displayed. Roll
                                                   back the listed components to the required software versions
                                                   and then re-run this command. If the versions of the associated components are compatible
                                                   with the selected node's rollback version, then the rollback
                                                   procedure begins. Once the rollback procedure begins, you can see the progress
                                          details for each of the machines. You can also see the elapsed time
                                          since the procedure started. |
| Expected Outcome | The selected node or group of nodes is rolled back. |

| Note | You can check the status of rollback which is currently in-progress. For more information, see Check Status . |
|---|---|

| Command | utils deployment show in-progress |
|---|---|
| Description | This command is used to check the current status of any patch manager install, patch manager rollback, upgrade manager upgrade,
                                          upgrade manager rollback, switch-forward . It also shows the subsequent progress, if applicable, for each node on which the
                                          procedure is initiated. If there is no procedure in progress, this command gives the last successful/failed procedure status. |
| Expected Inputs | NA |
| Expected Outcome | Shows the current status of the patch manager install, patch manager
                                          rollback, upgrade manager upgrade, upgrade manager rollback,
                                          switch-forward for each node. If there is no patch
                                             manager install, patch manager rollback, upgrade manager upgrade,
                                             upgrade manager rollback, switch-forward, then you see the status of the previous upgrade,
                                             rollback. |

| Command | utils system icm-services start |
|---|---|
| Description | This command is used to start the Unified ICM services from Cloud Connect server. This CLI will present the user with a list
                                          of Unified ICM hosts configured in the inventory, and the admin can select individual or group of Unified ICM hosts. |
| Expected Inputs | User should choose individual or group of Unified ICM hosts from the list. User should give confirmation yes/no to proceed with start of Unified ICM services |
| Expected Outcome | As part of CLI output, there are two kinds of messages which displays
                                          success as shown below: When the Unified ICM services are started successfully from stop state, the message “ Services started ” is displayed. When the Unified ICM services are already up and running, the message “ Services running ” is displayed. |

| Command | utils system onboard update |
|---|---|
| Description | This command is used to update a node/cluster on a Cloud Connect node. |
| Expected Inputs | When run, this command prompts for: Cloud Connect server FQDN Cloud Connect application username and password |
| Expected Outcome | The existing node/cluster is updated in the Cloud Connect node inventory. |

| Command | utils system onboard remove |
|---|---|
| Description | This command is used to remove a node/cluster from a Cloud Connect node. |
| Expected Inputs | When run, this command prompts for: Cloud Connect server FQDN Cloud Connect application username and password |
| Expected Outcome | The node/cluster is successfully removed from the Cloud Connect node inventory. |

| Note | If SSH connection is already established, skip Step 1 in the above procedure. |
|---|---|

| Command | show smtp-host |
|---|---|
| Description | This command is used to get the IP address or hostname of the SMTP server. |
| Expected Inputs | NA |
| Expected Outcome | Shows the configured IP address or host name of the SMTP server. |

| Command | show smtp-from-email |
|---|---|
| Description | This command is used to get the email address from which the emails are triggered. This email address is not monitored and
                                                therefore not used for replying to any emails. |
| Expected Inputs | NA |
| Expected Outcome | Shows the email address from which the emails are triggered. |

| Command | show smtp-use-auth |
|---|---|
| Description | This command is used to know if SMTP authentication is enabled or not. |
| Expected Inputs | NA |
| Expected Outcome | SMTP authentication : <enable/disable> |

| Command | show smtp-user |
|---|---|
| Description | This command is used to show the user name to be used for SMTP server connection. |
| Expected Inputs | NA |
| Expected Outcome | Shows the SMTP username. |

| Command | show smtp-pswd |
|---|---|
| Description | This command is used to know if the SMTP password is set or not. To reset the password, run the set smtp-pswd command. |
| Expected Inputs | NA |
| Expected Outcome | Shows whether the SMTP password is set or not. |

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

| Note | For information on adding deployment type and deployment name in the inventory file, see Add Deployment Type and Deployment Name . |
|---|---|

| Command | utils patch-manager export status |
|---|---|
| Description | This command is used to export the patch level details of a node or a group of nodes in a text file format. |
| Expected Inputs | Select the node(s) and enter the SFTP server details. |
| Expected Outcome | A text file with the current patch levels of the selected nodes is exported to the provided location. A success message is
                                          displayed along with the location where the file is saved. |

| Note | Software is downloaded separately on Cloud Connect publisher and subscriber. |
|---|---|

| Note | If the Windows node (CVP and ICM) version is 12.5, install 12.5 mandatory ES or MR patch before performing this procedure. See System Requirements for details. |
|---|---|

| Note | The authorized_keys extension type is File and you should not modify it. The user must have either domain admin or local administrator privilege. |
|---|---|

| Note | You must copy the Cloud Connect publisher and subscriber public keys into a single authorized_keys file. The publisher and subscriber entries should be in separate lines and should not use any extra space, comma, or any
                                             special characters at the end of the line. |
|---|---|

| Note | For more information on Windows security hardening, see the Windows Server Hardening section in the Security Guide for Cisco Unified ICM/Contact Center Enterprise . |
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