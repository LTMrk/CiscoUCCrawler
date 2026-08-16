---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-configurati-fbc4850858
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_serviceability-guide-for-cisco-unified-icm-contact-center-enterprise-release-15-0/cce_serviceability_and_monitoring_using_appdynamics.html
retrieved_at: 2026-08-16T14:37:40.154866+00:00
---

Serviceability Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Serviceability Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: CCE Serviceability and Monitoring using AppDynamics

## Chapter: CCE Serviceability and Monitoring using AppDynamics

# CCE Serviceability and Monitoring using AppDynamics

## Overview

For the Cisco Contact Center Enterprise solution, it is important to have continuous and seamless monitoring of the deployed
                           solution and automated alerting when anomalies are detected. AppDynamics provides a solution for application and platform
                           performance monitoring that helps achieve the following:

Platform, application, and end user monitoring (EUM) through dashboards and metrics.

Automated alerting mechanism in case of anomaly detection.

For ordering and setting up the AppDynamics SaaS controller, license key, and Beacon URL, please contact appd_ucce_sales@cisco.com .

Note

In Unified CCE 15.0(x), the AppDynamics Agents are not included by default. When you upgrade from Unified CCE 12.6(x), any
                                       existing AppDynamics Agents are removed. To install the AppDynamics Agents on 15.0(x) for the first time, or to upgrade, or
                                       to downgrade the installed AppDynamics Agents, see the section Install, Upgrade, or Downgrade AppDynamics Agents . The AppDynamics Agents install, upgrade or downgrade are supported on Cloud Connect 15.0(1) ES202511, 15.0(1) SU1, and all
                                          subsequent releases.

For AppDynamics, CCE supports SaaS and On-Prem controller (version 21.4.10-24683) over secure connection only.

## Supported Applications

All CCE solution components are supported except ECE, Customer Collaboration Platform (CCP), and Cloud Connect server. Here
                           is a table depicting what is instrumented in each component and monitored:

Note

End-user monitoring is supported for Finesse.

Finesse-Desktop

Finesse-Notification

LiveData-ActiveMQ

LiveData-SocketIO

Speech-Server

VVB-Engine

ReportingServer

WebServicesManager

CallServer

VXMLServer

WebServicesManager

Note

LiveData-Worker JVM App Agent is disabled by default. You can enable it using the set live-data appd-monitoring enable CLI. For more information on the CLI, see the Live Data CLI Commands section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .

## Prerequisites

### Application Group and Agent Licenses

Before the applications can be configured for performance monitoring, ensure that an AppDynamics application group is created
                              and the required number of agent licenses are procured and allocated. An access key is generated for the application group.
                              This access key is required later during the configuration procedure.

For details on how to acquire agent licenses, please contact appd_ucce_sales@cisco.com . If your AppDynamics agents are prior to 25.4.0 version, refer to Getting Started , else refer to Agent License Considerations .

Note

For end user monitoring on Finesse, you must procure AppDynamics ENUM license.

### Cloud Connect

The CLI commands described in this chapter must be run from the Cloud Connect server. The nodes on which performance monitoring
                              is to be enabled must be part of the Cloud Connect server orchestration inventory.

To install and configure Cloud Connect, refer to the Install Cloud Connect section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Refer to the following table for the required ES and COPs to be installed on different versions of the component VM:

Component

ES/COP 15.0(1)

ES/COP 12.6(2)

Cloud Connect

ES202511 and above

Cisco Unified Intelligence Center

Appdynamics Agent upgrade/downgrade - ucos.appdAgentsDeployCLI.1501.cop.sha512

Appdynamics Controller Certificate Management - ucos.appdAgentsCertImportCLI.1501.cop.sha512

ucos.appdAgentsCertImportCLI.1262.cop.sgn.

Live Data

Cisco Identity Service

Cisco Virtualized Voice Browser

Finesse

Unified ICM

No Mandatory ES is required.

Unified CVP

Note

CCE 15.0(1) SU1 and subsequent versions do not require mandatory Engineering Specials (ES) for AppDynamics.

AppDynamics performance monitoring is supported in the following deployment types:

UCCE-2000-Agents

UCCE-4000-Agents

UCCE-12000-Agents

UCCE-24000-Agents

PCCE-2000-Agents

PCCE-4000-Agents

PCCE-12000-Agents

For information about how to onboard nodes to Cloud Connect server, refer to the Orchestration Deployment Task Flow section in the Unified CCE or Packaged CCE Install and Upgrade Guide .

### CCE Solution Components

The CCE solution components existing in domain should have a unique FQDN. The components
                              existing in a workgroup should have a unique hostname to register with AppDynamics
                              controller for performance monitoring.

## Install, Upgrade, or Downgrade AppDynamics Agents

To download AppDynamics Agents, go to https://download.appdynamics.com , select the Agent type, operating system (Windows or Linux), and the required version.

To download the DotNetAgentExtensionManager developed by Cisco DevNet, go to https://developer.cisco.com/codeexchange/github/repo/Appdynamics/DotNetAgentExtensionManager and go to the GitHub link and select the Publish folder.

Note

Before you download the DotNetAgentExtensionManager, refer to the note mentioned in the link Import AppDynamics Agents

Supported AppDynamics Agents

Machine Agent

Supported for both Windows and VOS components.

For VOS components: Versions 25.10.0 and above (zip format with JRE included) are supported.

For Windows: Any version is supported.

Example:

For Windows: Machine Agent Bundle - 64-bit Windows (zip)

For VOS components: Machine Agent Bundle - 64-bit Linux (zip)

Java Agent

Supported for both Windows and VOS components.

Use the Java Agent for JDK8+ JVM (zip)

RPM format is currently not supported.

.NET Agents

Supported for Windows only. Any 64-bit version in MSI format is supported.

DotNetAgentExtensionManager

Supported for Windows only. Latest available version 1.5.2 (zip) is supported.

Note

Ensure you import the Machine Agent, Java Agent, and .NET Agent (importing .NET Agent Extension is optional) separately for
                                             Windows, and import the Machine Agent and Java Agent separately for the Linux (VOS) components.

The AppDynamics Agent is specific to Windows or Linux (VOS) platforms and is not exclusive to the CCE component.

AppDynamics agents deployed on CCE 15.0(1) or later are preserved during upgrades to subsequent versions, including Service
                                             Updates (SU).

To enable performance monitoring on the components, first import AppDynamics Agents into Cloud Connect and update the agents
                                             on each respective component. For more information, refer to the sections: Import AppDynamics Agents and Update AppDynamics Agents .

AppDynamics Agent Import , Update , and View Update Status operations can be performed only from the Cloud Connect publisher node.

### Import AppDynamics Agents

To import the AppDynamics Agents (Machine Agents, Java Agents, .NET Agent, and DotNetAgentExtensionManager) from an SFTP server
                                 to the Cloud Connect server, run the utils app-monitoring agents-import command on the Cloud Connect publisher.

For more information on supported AppDynamics Agents versions and instructions on how to download the Agents from AppDynamics,
                                 see section Install, Upgrade, or Downgrade AppDynamics Agents .

Note

Only one version of each Windows/Linux (VOS)-specific agent type (such as the Machine Agent, Java Agent, .NET Agent or DotNetAgentExtensionManager)
                                                   is imported into the Cloud Connect publisher at any given time. When you import a new version of an agent, the previously
                                                   imported version of that same agent type is automatically removed from the Cloud Connect publisher.

Although the Java Agent is operating system-agnostic, you must import it separately for both Windows and Linux (VOS) platforms.

The Import CLI validates the digital signature of all imported agents. However, the DotNetAgentExtensionManager, used for
                                                   Windows Event Viewer Monitoring, developed by Cisco DevNet (Developer Community) does not include a digital signature, and
                                                   therefore its signature is not validated during import. Exercise caution and fully understand the potential risks of using
                                                   an extension that is not digitally signed.

Command

utils app-monitoring agents-import

Description

Use this command to import the AppDynamics Agents from an SFTP server to the Cloud Connect publisher.

Expected Inputs

SFTP server details

AppDynamics Windows or Linux Agents

Machine Agent, App Server Agent, .NET Agent, or DotNetAgentExtensionManager

Agent file name

Expected Outputs

Validates that the SFTP server has selected the Agent or extension and imports it to the Cloud Connect publisher. This CLI
                                             command replaces any previously imported Agents or extensions.

### Update AppDynamics Agents

To update (install, upgrade, or downgrade) AppDynamics Agents on respective Windows and VOS components, run the utils app-monitoring agents-version update command on the Cloud Connect publisher. This update command uses the Agents that were imported using the utils app-monitoring agents-import command. This command replaces the existing agents in the target system.

Command

utils app-monitoring agents-version update

Description

Run this command on the Cloud Connect publisher to update (install, upgrade, or downgrade) the AppDynamics Agents and supported
                                             extensions on Windows or VOS components in the deployment.

Expected Inputs

Select the nodes on which the AppDynamics Agents need to be updated.

Expected Outcome

The update (install, upgrade, or downgrade) of the AppDynamics Agents or extensions is initiated.

Note

Updating AppDynamics Agents on the target system is permitted only when AppDynamics monitoring is disabled and the target
                                                   system is running version 15.0(1) or later.

To check the status of agent or extension updates (including installation, upgrade, or downgrade), run the following command: utils app-monitoring agents-version-update status .

The DotNetAgentExtensionManager is an optional .NET Agent extension used for Windows Event Viewer Monitoring on ICM core components.

During the initial installation, both the .NET Agent and the DotNetAgentExtensionManager can be imported and installed together.
                                                   If you choose to skip the optional DotNetAgentExtensionManager during the initial installation, you can install it later,
                                                   provided that the .NET Agent is already installed on the ICM core components where you want to add the extension.

AppDynamics monitoring can be enabled without the optional Windows Event Viewer Monitoring. However, to enable Windows Event
                                                   Viewer Monitoring, you must install the DotNetAgentExtensionManager extension for the .NET Agent.

When updating AppDynamics agents for the first time on CCE 15.0(1) SU1 VOS systems, an automatic certificate import to agent
                                                   trust store occurs, which may extend the deployment time by approximately 5 to 7 minutes. You can verify the progress of the
                                                   deployment by running the utils app-monitoring agents-version-update status command.

### View AppDynamics Agents Update Status

To view the AppDynamics Agents or extensions update (install, upgrade or downgrade) status on Windows or VOS components, use utils app-monitoring agents-version-update status command on the Cloud Connect publisher.

Command

utils app-monitoring agents-version-update status

Description

Use this command on the Cloud Connect publisher to view the update (install, upgrade, or downgrade) status of the AppDynamics
                                             Agents initiated using update CLI.

Expected Inputs

None.

Expected Outcome

Displays whether the AppDynamics Agents are successfully updated. If the update fails, the CLI displays the failure details
                                             and provides a reference to the log file.

Note

The CLI displays the status of the most recently initiated update operation for AppDynamics Agents.

If the update is successful, you receive a confirmation message.

If the update fails or is not initiated, the CLI displays the relevant details and provides a reference to the log file. The
                                                         CLI shows only the status of the last update operation, not a consolidated summary of all updates.

Note

When updating AppDynamics agents for the first time on CCE 15.0(1) SU1 VOS systems, an automatic certificate import to agent
                                             trust store occurs, which may extend the deployment time by approximately 5 to 7 minutes.

If the following message appears, allow the operation to complete:

Certificate import for Agent(s) is in progress. AppDynamics Agent(s) deployment may take a few extra minutes to complete.

### AppDynamics Agents Controller Certificate Management

You can import the AppDynamics Controller certificate into the trust stores of Machine Agents and App Server Agents on their
                                 respective VOS components. To import or display the certificates, use the appropriate CLI commands on each VOS component.

Note

- Updated SaaS Controller certificates are automatically imported into the Machine Agent and App Server Agent trust stores.
                                                   This process occurs as part of the agent update for VOS 15.0(1) SU1 and later, or by applying the ucos.appdAgentsCertImportCLI.1501.cop.sha512 COP file on VOS 15.0(1) systems.

Ensure you install AppDynamics Agents before you run the CLI commands related to AppDynamics Controller certificate management.
                                                   For more information, refer to the section Install, Upgrade, or Downgrade AppDynamics Agents .

Ensure you run the CLI commands related to AppDynamics Controller certificate management separately on both the publisher
                                                   and subscriber nodes.

#### Importing AppDynamics Controller Certificates into Agents Trust Store on VOS Nodes

To import the private or public CA certificate of the AppDynamics Controller into the trust stores of the AppDynamics Machine
                                 Agent and AppDynamics App Server Agent on VOS-based components, run the

Command

utils app-monitoring controller-certificate import

Description

Use this command to import private or public CA certificate chains into AppDynamics Machine Agent and App Server Agent trust
                                             stores of the VOS-based components from an SFTP server location. Ensure that you run this command on the respective VOS-based
                                             components.

Expected Inputs

SFTP server

SFTP user

SFTP user's password

SFTP directory

Certificate file name

Expected Outputs

#### Displaying Certificates in the Machine Agent Trust Store on VOS Nodes

To display the certificates in the AppDynamics Machine Agent trust store for VOS-based components, run the utils app-monitoring display machine-agent-trust-store-certs command.

Command

utils app-monitoring display machine-agent-trust-store-certs

Description

Use this command to view the certificate aliases in the AppDynamics Machine Agent trust store of the VOS-based components.
                                             Ensure that you run this command on the respective VOS-based components.

Expected Inputs

Expected Outputs

List the certificate aliases available in the AppDynamics Machine Agent trust store. If an error occurs, the CLI displays
                                             the failure details and provides a reference to the log file for more information.

#### Displaying Certificates in the App Server Agent Trust Store on VOS Nodes

To display the certificates in the AppDynamics App Server Agent trust store for VOS-based components, run the utils app-monitoring display appserver-agent-trust-store-certs command.

Command

utils app-monitoring display appserver-agent-trust-store-certs

Description

Use this command to view the certificate aliases in the AppDynamics App Server Agent trust store of the VOS-based components.
                                             Ensure that you run this command on the respective VOS-based components.

Expected Inputs

Expected Outputs

## Performance Monitoring

In order to monitor the performance of CCE applications, platforms, and end-user-facing application such as Finesse desktop
                           using AppDynamics, an administrator must configure and enable performance monitoring on the target node.

Note

Parallel execution of same or different CLI for AppDynamics on Cloud Connect server is not allowed.

### Enable Performance Monitoring

To enable performance monitoring on Windows or VOS nodes, run the utils app-monitoring enable command. You can select a single node or a group of nodes from either Cloud Connect publisher or subscriber to enable performance
                              monitoring. Ensure that the number of selected nodes doesn't exceed 10. Provide the details for configuring these nodes for
                              monitoring. Deployment Name configured in Orchestration inventory is used as the application name in AppDynamics. For more
                              information, see the Add Deployment Type and Deployment Name section in the Orchestration chapter of Unified CCE or Packaged CCE Install and Upgrade Guide .

Performance monitoring is enabled only after restarting the target node. If you choose not to restart the servers immediately,
                              manually restart them later for the changes to take effect.

All the supported AppDynamics agents on the target nodes are enabled for monitoring; the administrator can’t control the enable
                              or disable of a specific AppDynamics agent on the target node.

Note

You can also use this command to update any existing configuration details on selected nodes.

The AppDynamics CLI operation is allowed only if the required AppDynamics agents are deployed on the target node. If AppDynamics
                                                agents are not deployed, the CLI operation is rejected with details displayed on the console.

The AppDynamics CLI operation is not allowed when the agent update is in progress on the target node.

Note

Controller Host: The hostname/URL of the AppDynamics Controller. Agents may connect directly to the Controller or through a proxy.

Controller Port: The port on which the AppDynamics Controller listens for agent traffic.

Account Name: The name of the account listed in the AppDynamics Controller A single tenant Controller has two accounts: a default account
                                                name and an internal system account. For most connections, use the default account name.

Account Access Key: A unique key associated with the AppDynamics Controller account. This is used as the API token by agents to authenticate/authorize
                                                themselves with the Controller.

Beacon URL: The service endpoint where JavaScript agents will connect for sending the end user monitoring metrics.

Beacon Access Key: The access key used by JavaScript agents for authenticating or authorizing themselves with the Beacon server. This is different
                                                from the Account Access Key mentioned above.

Proxy Host: Proxy server IP/hostname via which the AppDynamics controller is connected.

Proxy Port: Proxy port for connecting to the proxy server.

Username: Username of the AppDynamics controller account.

Password: Password of the AppDynamics controller account.

Note

Username and Password are used for enabling Windows Event monitoring on ICM nodes. The administrator has an option to confirm
                                                      on whether AppDynamics Windows Event monitoring must be enabled or not, when the ICM node is selected for enabling AppDynamics.
                                                      AppDynamics Windows Event monitoring can be enabled only when the DotNetAgentExtensionManager is installed. The Username and
                                                      Password will be requested only when the administrator confirms to enable Windows Event Monitoring on ICM nodes.

Note

Proxy Host and Proxy Port will be requested only when the administrator confirms to use proxy for application monitoring.
                                                      Using proxy for application monitoring is optional.

Note

Beacon URL and Beacon Access Key used for end-user monitoring are applicable only for Finesse node. For more information on
                                                      how to generate a Beacon Access Key, refer to the Generate a Beacon Access Key section below:

Note

The DotNetAgentExtensionManager is an optional .NET Agent extension used for Windows Event Viewer Monitoring on ICM core components.

During the initial installation, both the .NET Agent and the DotNetAgentExtensionManager can be imported and installed together.
                                                If you choose to skip the optional DotNetAgentExtensionManager during the initial installation, you can install it later,
                                                provided that the .NET Agent is already installed on the ICM core components where you want to add the extension.

AppDynamics monitoring can be enabled without the optional Windows Event Viewer Monitoring. However, to enable Windows Event
                                                Viewer Monitoring, you must install the DotNetAgentExtensionManager extension for the .NET Agent.

If AppDynamics agents fail to connect to the controller following agent installation, refer the AppDynamics Agents Controller Certificate Management section of the CCE 15.0(1)  Serviceability Guide to import the necessary certificates into the VOS node agent trust store.

Note

If performance monitoring is already enabled, and if you want to add or delete the component in Unified ICM, then follow the
                                          below steps to update the performance counters for monitoring.

Disable application performance monitoring using the utils app-monitoring disable command.

Add or delete the component in the Unified ICM.

Enable application performance monitoring using the utils app-monitoring enable command.

When application performance monitoring is enabled, the system specific and CCE-specific performance counters are enabled
                              by default. You can add more counters for deployment by editing the .NET Agent config file . If your AppDynamics agents are prior to 25.4.0 version, refer to Manage Windows Performance Metrics , else refer to Machine Agent Element . If you are adding more counters, ensure that you don't exceed 200 counters on a virtual machine. Manually added counters will
                              be reset to the default value if you disable or enable application performance monitoring. The counters added to the monitoring
                              list includes all the installed CCE services including the disabled services. Hence, delete the disabled CCE services from
                              the server if they are not required.

Note

Performance monitoring starts on VOS components approximately 15 to 20 minutes after reboot. During this period, performance
                                          monitoring status for the target node in utils app-monitoring status CLI will be shown as Disabled.

#### Generate or Retrieve Beacon Access Key and URLs

Generate Beacon Access Key

Perform the following steps to generate the Beacon Access Key:

Log in to AppDynamics controller.

Click User Experience tab.

Click Add App in Browser Apps tab.

Select Create an application using the Getting Started Wizard , and press OK . The Set Browser Application section appears.

Enter the application name in the Set Browser Application section. Click Continue . The Beacon Access Key will be generated.

The Send and Verify a Test Page operation will be initiated, and it might take up to two minutes to complete. Once the activity
                                       is completed, the message, Beacon Sent and Data Received & Page Created is displayed with a tick mark.

Then, the message, You have successfully verified the configuration is displayed with a tick mark in the Instrument your own web pages section. Click Continue , and click Save in the next page.

Click on the User Experience tab to verify if the browser application has been created with the newly generated Beacon access key.

Retrieve Beacon Access Key and URLs

If you already have a Beacon Access Key and Browser application for Finesse on AppDynamics Controller, you need not generate
                                 a new key to retrieve the URLs. Instead, use the existing Browser App in the AppDynamics Controller and retrieve the HTTPS
                                 URL values from its Browser RUM instrumentation configuration.

To retrieve the URLs for an existing Browser App:

Log in to AppDynamics Controller.

Click User Experience tab.

On the Browser Apps tab, open the Browser Apps tab that is configured for Finesse.

In the left navigation pane, click Configuration .

On the Configuration page, click Configure JavaScript Agent .

In the JavaScript instrumentation snippet, copy the below values:

config.adrumExtUrlHttps and config.beaconUrlHttps for HTTPS values

config.appKey for beacon access key details

Note

Use only the HTTPS values. Regenerate the Beacon Access Key only if the existing Browser App or key is no longer available,
                                             or if you must move Finesse monitoring to a new Browser App. If you generate a new key, update the AppDynamics monitoring
                                             configuration with the new Beacon URL and Beacon Access Key.

### Update Performance Monitoring Configuration

To update the configuration details for performance monitoring, run the app-monitoring enable command. You must restart the servers for the changes to take effect. For details on the command, see Enable Performance Monitoring .

### Disable Performance Monitoring

To disable performance monitoring on Windows and VOS nodes, run the app-monitoring disable command. Performance monitoring will be disabled after restart of target node. The configurations will, however, be retained. The administrator will not be allowed to disable any specific AppDynamics agent on the target node. All supported AppDynamics
                                 agents will be disabled by default.

Note

The AppDynamics CLI operation is allowed only if the required AppDynamics agents are deployed and monitoring is enabled on
                                          the target node. If AppDynamics agents are not deployed, the CLI operation is rejected with details displayed on the console.

### Check Status of Performance Monitoring

To check whether performance monitoring is enabled, disabled, or just configured but not enabled, on selected Windows or VOS
                              nodes, run the utils app-monitoring status command.

Note

The AppDynamics CLI operation is allowed only if the required AppDynamics agents are deployed on the target node. If AppDynamics
                                          agents are not deployed, the CLI operation is rejected with details displayed on the console.

Proxy enabled status

Windows Event monitoring enabled status for ICM nodes

If an update is made to the existing configuration and the node is restarted, then the status shows the updated configuration
                                                as current configuration used by AppDynamics performance monitoring.

If an update is made to the existing configuration and the node is not restarted, then the status shows both the current configuration
                                                used by AppDynamics performance monitoring as well as the to-be-applied configuration which will be applied post restart.

### Test Connection with AppDynamics Controller

To test whether the configured Windows and VOS nodes are able to connect to the AppDynamics controller, run the utils app-monitoring test-connection command.

Note

The AppDynamics CLI operation is allowed only if the required AppDynamics agents are deployed on the target node. If AppDynamics
                                          agents are not deployed, the CLI operation is rejected with details displayed on the console.

### Configure Thresholds and Alerts for Monitoring

We recommend using the templates delivered for configuring threshold and alerts on the
                              AppDynamics controller.

The Cisco-delivered templates can be imported on the application. . For details on managing templetes, if your AppDynamics agents are prior to 25.4.0 version, see Configure and Manage Alerting Templates , else see Configure and Manage Alerting Templates . For downloading templates, see Unified Contact Center Enterprise 15.0(1) Software Download.

Once the template is imported, you have to replace the default email address
                                    (support@cisco.com) with a valid email address for alert notification.

Adding at least one valid email address is mandatory. However, you can add
                                    multiple email addresses.

Threshold for alerts is enabled by default as part of Cisco-delivered
                                    template.

Note

You can also view, create, overwrite, delete, export, apply and disable the template on the application. For details on managing templates, if your AppDynamics agents are prior to 25.4.0 version, see Configure and Manage Alerting Templates , else see Configure and Manage Alerting Templates .

### Configure JMX Monitoring and Alerting Templates for Finesse Desktop

We recommend using the following templates to configure JMX Monitoring for Finesse
                              Desktop.

Finesse_JMX_Metrics_Configuration.xml

Finesse_JMX_Metrics_AlertingTemplate.json

Follow these steps to import the templates to the respective application:

Navigate to the respective application on the AppDynamics controller.

Select Tiers & Nodes section menu.

From the Finesse-Desktop tier, select the Finesse node.

Select the JMX tab.

Click the Configure JMX Metrics icon.

Click the Import icon.

Click the Choose File button.

Select the Finesse_JMX_Metrics_Configuration.xml file.

Click the Import button. The FinesseMetrics List is
                                    displayed if the import succeeds.

Import Finesse_JMX_Metrics_AlertingTemplate.json . See Configure Thresholds and Alerts for Monitoring for more information on importing the alerting
                                    template.

## Dashboards

Dashboards are used to display the health of the system in a graphical manner on the AppDynamics
                           controller. Data such as CPU and memory usage are collected from the system at platform
                           level. Data such as health status of Java agents and .NET agents are collected from the
                           system at application level. Administrators can build custom dashboards with various
                           widgets to visualize the data from individual systems as well as all the systems in the
                           deployment. These dashboards can be imported or exported when deploying new CCE
                           tenants.

For more information on Dashboards, If your AppDynamics agents are prior to 25.4.0 version, see Custom Dashboards , else see Dasboards and Reports .

### Create Dashboards Using Templates

Administrators can create new dashboards or edit the dashboard template (JSON file) provided by
                              us. This edited template file can then be imported to the AppDynamics Controller via the Dashboards & Reports tab.

For downloading template, see AppDynamics Template

Edit the following strings in the template:

"name" - Provide an appropriate name, which is displayed as the dashboard name in
                                    the Controller. For example, "Arihant - 2K Dashboard".

"applicationName" - Update this with the corresponding application name for which
                                    you want to create a dashboard.

Note

"entityName" - Set the name of the system that is monitored.

If the "entityType" is set to "APPLICATION_COMPONENT_NODE", update this string with the corresponding AW component node name.
                                          For example, "UCCEAWHDS121A".

Once the template file is edited and imported, the dashboard will display the
                                    performance and health status of the system.

Note

If the "entityType" is set to "APPLICATION_COMPONENT", then do not
                                                      make any changes to the "entityName".

If the "entityType" is set to "BUSINESS_TRANSACTION", do not make any
                                                      changes to the "scopingEntityName".

There are no changes required in these cases as the type of entity is
                                                      a tier-name, which is common to all the nodes in an application.

### End User Monitoring

End user monitoring is available for the Finesse desktop application. It provides various browser-based metrics, such as the
                              most frequently used browser, the most commonly used browser version, etc. It can provide geographical location of a Finesse
                              agent desktop. The AppDynamics agents in the browser sends the metrics to the AppDynamics Controller. You can view these metrics
                              in the User Experience tab of the AppDynamics Controller application.

Starting with Cisco Finesse 15.0(1) SU1, you can enable end-user monitoring only by updating your Content Security Policy
                                 (CSP) settings.

To update your CSP settings:

Retrieve the config.adrumExtUrlHttps and config.beaconUrlHttps URLs from the instrumentation script that is generated during the beacon access key generation process. For more details,
                                       see Generate Beacon Access Key .

Add the retrieved URLs to the default-src directive using the Finesse CLI. For more details, see default-src in Supported Content Security Policy Directives section in Cisco Finesse Administration Guide, Release 15.0(1)

When you run the app-monitoring enable command to enable performance monitoring for Finesse, end user monitoring is also enabled. There is no additional step required.
                              The Beacon URL and the Beacon Access Key that you provided when running the command are saved in the Finesse server. The network
                              connectivity between the Finesse Agent desktop browser and the Beacon host, however, must be available. The Beacon host must
                              be on the allowed list in the proxy server.

If your AppDynamics agents are prior to 25.4.0 version, see End User Monitoring , else see End User Monitoring .

### View Metrics

Once the monitoring is enabled on the VOS and Windows nodes, the AppDynamics agents start
                              sending out performance metrics to the AppDynamics controller. These monitored metrics,
                              also known as counters, are shipped from the Windows machines as performance counters,
                              and from the respective JVMs of the VOS machines as JMX counters. These metrics can be
                              viewed on the AppDynamics Controller interface and later utilized for setting
                              thresholds, alerts, etc.

#### JMX Counter Thresholds

Cisco Finesse provides important JMX counters with associated threshold values that
                                 can be used to monitor the health of Finesse. The following tables list the JMX
                                 counters with corresponding threshold values at the login phase and steady
                                 phase.

Note

The JMX counter IntervalLoginOperations with the JMX object
                                             name com.cisco.ccbu:category=LoginStats,component0=LoginStats-webservices will be used to determine the total number of logins.

If the number of logins that happened in the last 15 seconds is greater than 5,
                                             then it is login phase. Else it is steady phase. Respective threshold will be
                                             used dynamically based on the number of logins.

Description

JMX Object Name

Threshold at Login Phase

ThreadCount

The number of threads running at the current moment.

java.lang:type = Threading

400

PeakThreadCount

The maximum number of threads run at the same time since the JVM was started or the peak was reset.

java.lang:type = Threading

500

currentThreadCount

The number of threads the thread pool currently has (both busy and free).

Catalina:type = ThreadPool, name = "http-apr-127.0.0.1-8082"

120

currentThreadsBusy

The number of threads currently processing requests.

Catalina:type = ThreadPool, name = "http-apr-127.0.0.1-8082"

100

RequestLongestTime

The maximum amount of time taken to complete an API request, in milliseconds.

com.cisco.ccbu:category = WebAppStats, component0 = AggregateWebappStats

4000

processCPULoad

The CPU load in this process.

java.lang:type = OperatingSystem

0.6

NumOfActiveAgentsLoggedIn

The number of agents logged in with XMPP Presence as available in the current side.

com.cisco.ccbu:category = AWSSubsystem, component0 = AWS Statistics Counter

1500

NumOfAgentsLoggedIn

The number of agents and supervisors logged in currently.

com.cisco.ccbu:category = AWSSubsystem, component0 = AWS Statistics Counter

2010

JMX Counter

Description

JMX Object Name

Threshold at Steady Phase

ThreadCount

The number of threads running at the current moment.

java.lang:type = Threading

400

PeakThreadCount

The maximum number of threads run at the same time since the JVM was started or the peak was reset.

java.lang:type = Threading

500

TotalCallsInSystem

The total number of active calls in the system.

com.cisco.ccbu:category = AWSSubsystem, component0 = AWS Statistics Counter

1400

AverageProcessingTime

The average time taken for processing CTI messages, in milliseconds.

com.cisco.ccbu:category = AWSSubsystem, component0 = CTIMesssage Statistics Counter

20 ms

currentThreadCount

The number of threads the thread pool currently has (both busy and free).

Catalina:type = ThreadPool, name = "http-apr-127.0.0.1-8082"

120

currentThreadsBusy

The number of threads currently processing requests.

Catalina:type = ThreadPool, name = "http-apr-127.0.0.1-8082"

20

RunnablesQueued

Runnables (CTI Messages) still queued.

com.cisco.ccbu:category = AWSSubsystem, component0 = CommandDispatcher

20

TasksQueued

The tasks (such as client requests and CTI messages) queued.

com.cisco.ccbu:category = AWSSubsystem, component0 = CommandDispatcher

20

RequestLongestTime

The maximum amount of time taken to complete an API request, in milliseconds.

com.cisco.ccbu:category = WebAppStats, component0 = AggregateWebappStats

4000

processCPULoad

The CPU load in this process.

java.lang:type = OperatingSystem

NumOfAgentsLoggedIn

The number of agents and supervisors logged in currently.

com.cisco.ccbu:category = AWSSubsystem, component0 = AWS Statistics Counter

2010

The following table lists the thresholds for counters related to Openfire processes.

JMX Counter

Description

JMX Object Name

Threshold at Login Phase

ExecutingTaskCount

The number of tasks (messages published to node) that are running currently.

com.cisco.ccbu.finesse.openfire: type = PubSubOrderedExecutorStatistics

60

QueuedTaskCount

The number of tasks in the queue. Messages that are getting published to a node are placed in the queue.

com.cisco.ccbu.finesse.openfire: type = PubSubOrderedExecutorStatistics

10

PeakThreadCount

The maximum number of threads run at the same time since the JVM was started or the peak was reset.

java.lang:type = Threading

300

ThreadCount

The number of threads running at the current moment.

java.lang:type = Threading

300

processCPULoad

The recent CPU usage for the Java Virtual Machine process.

java.lang:type = OperatingSystem

0.6

## Check Logs

AppDynamics-related logs are used by the administrators for troubleshooting the failures
                           that are encountered while enabling or disabling or testing the connectivity for
                           performance monitoring from the Cloud Connect server.

AppDynamics related logs are used while debugging failures such as performance metrics
                           not appearing in the AppDynamics controller. All AppDynamics-related logs are stored in
                           their respective target nodes.

Audit Logs

The Audit trail for AppDynamics administrative operation that is initiated from the AppDynamics CLI on Cloud Connect server
                           captures the user, action, and date/time details of the CLI operation.

command: file get activelog orchestration-audit/audit.log*

CLI Logs

Run the following command on the Cloud Connect node to retrieve AppDynamics CLI logs:

command: file get activelog platform/log/cli*.log

Ansible Logs

Run the following commands on the Cloud Connect node to retrieve AppDynamics related Ansible logs:

Current transaction logs: file get activelog ansible/ansible.log

Historical logs: file get activelog ansible/ansible_history.log

Agent version update logs: ansible_app_monitoring_agent_version_update.log

Agent version update history logs: ansible_app_monitoring_agent_version_update_history.log

AppDynamics Logs (on the target host)

Refer to the following table for information on retrieving the AppDynamics-related Logs
                           on target host:

file get activelog appdynamics/appdynamics.log

file get activelogappdynamics/machineagent/logs

file get activelog appdynamics/appserveragent/logs/<APM Folder Name>

Note

Ensure that you use the exact regular expression to accurately retrieve the details of the nested directory.

file get activelog appdynamics/appdynamics_default_certificate_import.log

file get activelog appdynamics/appdynamics_agents_deploy.log

Note

This log is available only for target nodes and not for Cloud Connect.

```
<Install Directory>:\Cisco\AppDynamics\
log\AppDynamics_Perf_Configuration.log
```

```
<Install Directory>:\Cisco\AppDynamics
\log\AppDynamics_Configuration.log
```

```
<Install Directory>:\Cisco\CVP\
AppDynamics\log\AppDynamics_Configuration.log
```

Note

For ICM and CVP, the install directory location changes based on your system configuration.

APM Name is constructed with "APM Name-VMhostname", and it is always different in case of every component and node.

You can also view the below-mentioned logs using the Real-Time Monitoring Tool (RTMT):

Ansible logs by selecting 'Ansible Controller' as the Cloud Connect service.

Audit logs by selecting 'Orchestration Audit' as the Cloud Connect service.

AppDynamics related logs by selecting 'Cisco APM Service' as the service on the target nodes.

To download RTMT from Cloud Connect or target VOS nodes, use https://<FQDN>:8443/plugins/Cisco RTMT Plugin.zip .

For more information, refer to the Cisco Unified Real-Time Monitoring Tool
                           Administration Guide at: https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

## Things to Know

AppDynamics cannot be enabled on FIPS-enabled deployment. Disable the FIPS mode
                                 before enabling AppDynamics.

You can disable or enable AppDynamics through AppDynamics CLI on Cloud Connect.
                                 If AppDynamics is disabled and re-enabled with a different application name
                                 (taken from the inventory), a new instance is created in the AppDynamics
                                 controller with the new application name. However, the instance with the old
                                 application name exists and should be manually deleted by logging into the
                                 AppDynamics controller. The new application name will be updated in the
                                 configuration on the target node once AppDynamics is re-enabled successfully
                                 with the new application name.

Performance monitoring for ECE, CCP and Cloud Connect is currently not supported.

### Customers Also Viewed

- Configure Webex AI Agent for CCE

### Contact Cisco

- Open a Support Case

- (Requires a Cisco Service Contract )

| Note | In Unified CCE 15.0(x), the AppDynamics Agents are not included by default. When you upgrade from Unified CCE 12.6(x), any
                                       existing AppDynamics Agents are removed. To install the AppDynamics Agents on 15.0(x) for the first time, or to upgrade, or
                                       to downgrade the installed AppDynamics Agents, see the section Install, Upgrade, or Downgrade AppDynamics Agents . The AppDynamics Agents install, upgrade or downgrade are supported on Cloud Connect 15.0(1) ES202511, 15.0(1) SU1, and all
                                          subsequent releases. For AppDynamics, CCE supports SaaS and On-Prem controller (version 21.4.10-24683) over secure connection only. |
|---|---|

| Sl No | Component Name | Machine Agent (Server Visibility) | .NET Agent (For Windows Perfmon Integration) | JVM App Agents |
|---|---|---|---|---|
| 1 | Finesse Note End-user monitoring is supported for Finesse. | Note | End-user monitoring is supported for Finesse. | ✔ | Not Applicable | Finesse-Desktop Finesse-Notification |
| Note | End-user monitoring is supported for Finesse. |
| 2 | CUIC | ✔ | Not Applicable | CUIC-Reporting |
| 3 | LiveData | ✔ | Not Applicable | LiveData-ActiveMQ LiveData-SocketIO |
| 4 | IdS | ✔ | Not Applicable | IdS Tomcat |
| 5 | VVB | ✔ | Not Applicable | Speech-Server VVB-Engine |
| 6 | CVP OAMP | ✔ | Not Applicable | OAMP |
| 7 | CVP ReportingServer | ✔ | Not Applicable | ReportingServer WebServicesManager |
| 8 | CVP Call/VXMLServer | ✔ | Not Applicable | CallServer VXMLServer WebServicesManager |
| 9 | Router | ✔ | ✔ | Not Applicable |
| 10 | Logger | ✔ | ✔ | Not Applicable |
| 11 | PG | ✔ | ✔ | CCEJGW |
| 12 | AW-HDS | ✔ | ✔ | CCEAdmin |
| 13 | AW-HDS-DDS | ✔ | ✔ | CCEAdmin |

| Note | End-user monitoring is supported for Finesse. |
|---|---|

| Note | LiveData-Worker JVM App Agent is disabled by default. You can enable it using the set live-data appd-monitoring enable CLI. For more information on the CLI, see the Live Data CLI Commands section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide . |
|---|---|

| Note | For end user monitoring on Finesse, you must procure AppDynamics ENUM license. |
|---|---|

| Component | ES/COP 15.0(1) | ES/COP 12.6(2) |
|---|---|---|
| Cloud Connect | ES202511 and above |  |
| Cisco Unified Intelligence Center | Appdynamics Agent upgrade/downgrade - ucos.appdAgentsDeployCLI.1501.cop.sha512 Appdynamics Controller Certificate Management - ucos.appdAgentsCertImportCLI.1501.cop.sha512 | ucos.appdAgentsCertImportCLI.1262.cop.sgn. |
| Live Data |
| Cisco Identity Service |
| Cisco Virtualized Voice Browser |
| Finesse |
| Unified ICM | No Mandatory ES is required. |  |
| Unified CVP |  |

| Note | CCE 15.0(1) SU1 and subsequent versions do not require mandatory Engineering Specials (ES) for AppDynamics. |
|---|---|

| Note | Before you download the DotNetAgentExtensionManager, refer to the note mentioned in the link Import AppDynamics Agents |
|---|---|

| Machine Agent | Supported for both Windows and VOS components. For VOS components: Versions 25.10.0 and above (zip format with JRE included) are supported. For Windows: Any version is supported. Example: For Windows: Machine Agent Bundle - 64-bit Windows (zip) For VOS components: Machine Agent Bundle - 64-bit Linux (zip) |
|---|---|
| Java Agent | Supported for both Windows and VOS components. Use the Java Agent for JDK8+ JVM (zip) RPM format is currently not supported. |
| .NET Agents | Supported for Windows only. Any 64-bit version in MSI format is supported. |
| DotNetAgentExtensionManager | Supported for Windows only. Latest available version 1.5.2 (zip) is supported. |

| Note | Ensure you import the Machine Agent, Java Agent, and .NET Agent (importing .NET Agent Extension is optional) separately for
                                             Windows, and import the Machine Agent and Java Agent separately for the Linux (VOS) components. The AppDynamics Agent is specific to Windows or Linux (VOS) platforms and is not exclusive to the CCE component. AppDynamics agents deployed on CCE 15.0(1) or later are preserved during upgrades to subsequent versions, including Service
                                             Updates (SU). To enable performance monitoring on the components, first import AppDynamics Agents into Cloud Connect and update the agents
                                             on each respective component. For more information, refer to the sections: Import AppDynamics Agents and Update AppDynamics Agents . AppDynamics Agent Import , Update , and View Update Status operations can be performed only from the Cloud Connect publisher node. |
|---|---|

| Note | Only one version of each Windows/Linux (VOS)-specific agent type (such as the Machine Agent, Java Agent, .NET Agent or DotNetAgentExtensionManager)
                                                   is imported into the Cloud Connect publisher at any given time. When you import a new version of an agent, the previously
                                                   imported version of that same agent type is automatically removed from the Cloud Connect publisher. Although the Java Agent is operating system-agnostic, you must import it separately for both Windows and Linux (VOS) platforms. The Import CLI validates the digital signature of all imported agents. However, the DotNetAgentExtensionManager, used for
                                                   Windows Event Viewer Monitoring, developed by Cisco DevNet (Developer Community) does not include a digital signature, and
                                                   therefore its signature is not validated during import. Exercise caution and fully understand the potential risks of using
                                                   an extension that is not digitally signed. |
|---|---|

| Command | utils app-monitoring agents-import |
|---|---|
| Description | Use this command to import the AppDynamics Agents from an SFTP server to the Cloud Connect publisher. |
| Expected Inputs | SFTP server details AppDynamics Windows or Linux Agents Machine Agent, App Server Agent, .NET Agent, or DotNetAgentExtensionManager Agent file name |
| Expected Outputs | Validates that the SFTP server has selected the Agent or extension and imports it to the Cloud Connect publisher. This CLI
                                             command replaces any previously imported Agents or extensions. |

| Command | utils app-monitoring agents-version update |
|---|---|
| Description | Run this command on the Cloud Connect publisher to update (install, upgrade, or downgrade) the AppDynamics Agents and supported
                                             extensions on Windows or VOS components in the deployment. |
| Expected Inputs | Select the nodes on which the AppDynamics Agents need to be updated. |
| Expected Outcome | The update (install, upgrade, or downgrade) of the AppDynamics Agents or extensions is initiated. |

| Note | Updating AppDynamics Agents on the target system is permitted only when AppDynamics monitoring is disabled and the target
                                                   system is running version 15.0(1) or later. To check the status of agent or extension updates (including installation, upgrade, or downgrade), run the following command: utils app-monitoring agents-version-update status . The DotNetAgentExtensionManager is an optional .NET Agent extension used for Windows Event Viewer Monitoring on ICM core components. During the initial installation, both the .NET Agent and the DotNetAgentExtensionManager can be imported and installed together.
                                                   If you choose to skip the optional DotNetAgentExtensionManager during the initial installation, you can install it later,
                                                   provided that the .NET Agent is already installed on the ICM core components where you want to add the extension. AppDynamics monitoring can be enabled without the optional Windows Event Viewer Monitoring. However, to enable Windows Event
                                                   Viewer Monitoring, you must install the DotNetAgentExtensionManager extension for the .NET Agent. When updating AppDynamics agents for the first time on CCE 15.0(1) SU1 VOS systems, an automatic certificate import to agent
                                                   trust store occurs, which may extend the deployment time by approximately 5 to 7 minutes. You can verify the progress of the
                                                   deployment by running the utils app-monitoring agents-version-update status command. |
|---|---|

| Command | utils app-monitoring agents-version-update status |
|---|---|
| Description | Use this command on the Cloud Connect publisher to view the update (install, upgrade, or downgrade) status of the AppDynamics
                                             Agents initiated using update CLI. |
| Expected Inputs | None. |
| Expected Outcome | Displays whether the AppDynamics Agents are successfully updated. If the update fails, the CLI displays the failure details
                                             and provides a reference to the log file. Note The CLI displays the status of the most recently initiated update operation for AppDynamics Agents. If the update is successful, you receive a confirmation message. If the update fails or is not initiated, the CLI displays the relevant details and provides a reference to the log file. The
                                                         CLI shows only the status of the last update operation, not a consolidated summary of all updates. | Note | The CLI displays the status of the most recently initiated update operation for AppDynamics Agents. If the update is successful, you receive a confirmation message. If the update fails or is not initiated, the CLI displays the relevant details and provides a reference to the log file. The
                                                         CLI shows only the status of the last update operation, not a consolidated summary of all updates. |
| Note | The CLI displays the status of the most recently initiated update operation for AppDynamics Agents. If the update is successful, you receive a confirmation message. If the update fails or is not initiated, the CLI displays the relevant details and provides a reference to the log file. The
                                                         CLI shows only the status of the last update operation, not a consolidated summary of all updates. |

| Note | The CLI displays the status of the most recently initiated update operation for AppDynamics Agents. If the update is successful, you receive a confirmation message. If the update fails or is not initiated, the CLI displays the relevant details and provides a reference to the log file. The
                                                         CLI shows only the status of the last update operation, not a consolidated summary of all updates. |
|---|---|

| Note | When updating AppDynamics agents for the first time on CCE 15.0(1) SU1 VOS systems, an automatic certificate import to agent
                                             trust store occurs, which may extend the deployment time by approximately 5 to 7 minutes. If the following message appears, allow the operation to complete: Certificate import for Agent(s) is in progress. AppDynamics Agent(s) deployment may take a few extra minutes to complete. |
|---|---|

| Note | Updated SaaS Controller certificates are automatically imported into the Machine Agent and App Server Agent trust stores.
                                                   This process occurs as part of the agent update for VOS 15.0(1) SU1 and later, or by applying the ucos.appdAgentsCertImportCLI.1501.cop.sha512 COP file on VOS 15.0(1) systems. Ensure you install AppDynamics Agents before you run the CLI commands related to AppDynamics Controller certificate management.
                                                   For more information, refer to the section Install, Upgrade, or Downgrade AppDynamics Agents . Ensure you run the CLI commands related to AppDynamics Controller certificate management separately on both the publisher
                                                   and subscriber nodes. |
|---|---|

| Command | utils app-monitoring controller-certificate import |
|---|---|
| Description | Use this command to import private or public CA certificate chains into AppDynamics Machine Agent and App Server Agent trust
                                             stores of the VOS-based components from an SFTP server location. Ensure that you run this command on the respective VOS-based
                                             components. |
| Expected Inputs | SFTP server SFTP user SFTP user's password SFTP directory Certificate file name |
| Expected Outputs | Displays whether the certificates are successfully imported to the AppDynamics Agent trust stores. |

| Command | utils app-monitoring display machine-agent-trust-store-certs |
|---|---|
| Description | Use this command to view the certificate aliases in the AppDynamics Machine Agent trust store of the VOS-based components.
                                             Ensure that you run this command on the respective VOS-based components. |
| Expected Inputs | None |
| Expected Outputs | List the certificate aliases available in the AppDynamics Machine Agent trust store. If an error occurs, the CLI displays
                                             the failure details and provides a reference to the log file for more information. |

| Command | utils app-monitoring display appserver-agent-trust-store-certs |
|---|---|
| Description | Use this command to view the certificate aliases in the AppDynamics App Server Agent trust store of the VOS-based components.
                                             Ensure that you run this command on the respective VOS-based components. |
| Expected Inputs | None |
| Expected Outputs | List the certificate aliases available in the AppDynamics App Server Agent trust store. If an error occurs, the CLI displays
                                          the failure details and provides a reference to the log file for more information. |

| Note | Parallel execution of same or different CLI for AppDynamics on Cloud Connect server is not allowed. |
|---|---|

| Note | You can also use this command to update any existing configuration details on selected nodes. The AppDynamics CLI operation is allowed only if the required AppDynamics agents are deployed on the target node. If AppDynamics
                                                agents are not deployed, the CLI operation is rejected with details displayed on the console. The AppDynamics CLI operation is not allowed when the agent update is in progress on the target node. |
|---|---|

| Command | utils app-monitoring enable |
|---|---|
| Description | This command enables performance monitoring on selected nodes. |
| Expected Inputs | Select the node on which you need to enable performance monitoring and provide the following information: Note You can select a single node or a group of nodes from either Cloud Connect publisher or subscriber to enable performance monitoring.
                                                   Ensure that the number of selected nodes doesn't exceed 10. Controller Host: The hostname/URL of the AppDynamics Controller. Agents may connect directly to the Controller or through a proxy. Controller Port: The port on which the AppDynamics Controller listens for agent traffic. Account Name: The name of the account listed in the AppDynamics Controller A single tenant Controller has two accounts: a default account
                                                name and an internal system account. For most connections, use the default account name. Account Access Key: A unique key associated with the AppDynamics Controller account. This is used as the API token by agents to authenticate/authorize
                                                themselves with the Controller. Beacon URL: The service endpoint where JavaScript agents will connect for sending the end user monitoring metrics. Beacon Access Key: The access key used by JavaScript agents for authenticating or authorizing themselves with the Beacon server. This is different
                                                from the Account Access Key mentioned above. Proxy Host: Proxy server IP/hostname via which the AppDynamics controller is connected. Proxy Port: Proxy port for connecting to the proxy server. Username: Username of the AppDynamics controller account. Password: Password of the AppDynamics controller account. Note Username and Password are used for enabling Windows Event monitoring on ICM nodes. The administrator has an option to confirm
                                                      on whether AppDynamics Windows Event monitoring must be enabled or not, when the ICM node is selected for enabling AppDynamics.
                                                      AppDynamics Windows Event monitoring can be enabled only when the DotNetAgentExtensionManager is installed. The Username and
                                                      Password will be requested only when the administrator confirms to enable Windows Event Monitoring on ICM nodes. Note Proxy Host and Proxy Port will be requested only when the administrator confirms to use proxy for application monitoring.
                                                      Using proxy for application monitoring is optional. Note Beacon URL and Beacon Access Key used for end-user monitoring are applicable only for Finesse node. For more information on
                                                      how to generate a Beacon Access Key, refer to the Generate a Beacon Access Key section below: Confirm to proceed, and select the option to restart. | Note | You can select a single node or a group of nodes from either Cloud Connect publisher or subscriber to enable performance monitoring.
                                                   Ensure that the number of selected nodes doesn't exceed 10. | Note | Username and Password are used for enabling Windows Event monitoring on ICM nodes. The administrator has an option to confirm
                                                      on whether AppDynamics Windows Event monitoring must be enabled or not, when the ICM node is selected for enabling AppDynamics.
                                                      AppDynamics Windows Event monitoring can be enabled only when the DotNetAgentExtensionManager is installed. The Username and
                                                      Password will be requested only when the administrator confirms to enable Windows Event Monitoring on ICM nodes. | Note | Proxy Host and Proxy Port will be requested only when the administrator confirms to use proxy for application monitoring.
                                                      Using proxy for application monitoring is optional. | Note | Beacon URL and Beacon Access Key used for end-user monitoring are applicable only for Finesse node. For more information on
                                                      how to generate a Beacon Access Key, refer to the Generate a Beacon Access Key section below: |
| Note | You can select a single node or a group of nodes from either Cloud Connect publisher or subscriber to enable performance monitoring.
                                                   Ensure that the number of selected nodes doesn't exceed 10. |
| Note | Username and Password are used for enabling Windows Event monitoring on ICM nodes. The administrator has an option to confirm
                                                      on whether AppDynamics Windows Event monitoring must be enabled or not, when the ICM node is selected for enabling AppDynamics.
                                                      AppDynamics Windows Event monitoring can be enabled only when the DotNetAgentExtensionManager is installed. The Username and
                                                      Password will be requested only when the administrator confirms to enable Windows Event Monitoring on ICM nodes. |
| Note | Proxy Host and Proxy Port will be requested only when the administrator confirms to use proxy for application monitoring.
                                                      Using proxy for application monitoring is optional. |
| Note | Beacon URL and Beacon Access Key used for end-user monitoring are applicable only for Finesse node. For more information on
                                                      how to generate a Beacon Access Key, refer to the Generate a Beacon Access Key section below: |
| Expected Outcome | Performance monitoring is configured for all the selected nodes and enabled if restart option is selected as "Yes". Windows Event Monitoring is enabled for ICM nodes based on administrator's confirmation. Proxy is configured for application monitoring based on administrator's confirmation to use proxy for application monitoring. |

| Note | You can select a single node or a group of nodes from either Cloud Connect publisher or subscriber to enable performance monitoring.
                                                   Ensure that the number of selected nodes doesn't exceed 10. |
|---|---|

| Note | Username and Password are used for enabling Windows Event monitoring on ICM nodes. The administrator has an option to confirm
                                                      on whether AppDynamics Windows Event monitoring must be enabled or not, when the ICM node is selected for enabling AppDynamics.
                                                      AppDynamics Windows Event monitoring can be enabled only when the DotNetAgentExtensionManager is installed. The Username and
                                                      Password will be requested only when the administrator confirms to enable Windows Event Monitoring on ICM nodes. |
|---|---|

| Note | Proxy Host and Proxy Port will be requested only when the administrator confirms to use proxy for application monitoring.
                                                      Using proxy for application monitoring is optional. |
|---|---|

| Note | Beacon URL and Beacon Access Key used for end-user monitoring are applicable only for Finesse node. For more information on
                                                      how to generate a Beacon Access Key, refer to the Generate a Beacon Access Key section below: |
|---|---|

| Note | The DotNetAgentExtensionManager is an optional .NET Agent extension used for Windows Event Viewer Monitoring on ICM core components. During the initial installation, both the .NET Agent and the DotNetAgentExtensionManager can be imported and installed together.
                                                If you choose to skip the optional DotNetAgentExtensionManager during the initial installation, you can install it later,
                                                provided that the .NET Agent is already installed on the ICM core components where you want to add the extension. AppDynamics monitoring can be enabled without the optional Windows Event Viewer Monitoring. However, to enable Windows Event
                                                Viewer Monitoring, you must install the DotNetAgentExtensionManager extension for the .NET Agent. If AppDynamics agents fail to connect to the controller following agent installation, refer the AppDynamics Agents Controller Certificate Management section of the CCE 15.0(1)  Serviceability Guide to import the necessary certificates into the VOS node agent trust store. |
|---|---|

| Note | If performance monitoring is already enabled, and if you want to add or delete the component in Unified ICM, then follow the
                                          below steps to update the performance counters for monitoring. Disable application performance monitoring using the utils app-monitoring disable command. Add or delete the component in the Unified ICM. Enable application performance monitoring using the utils app-monitoring enable command. |
|---|---|

| Note | Performance monitoring starts on VOS components approximately 15 to 20 minutes after reboot. During this period, performance
                                          monitoring status for the target node in utils app-monitoring status CLI will be shown as Disabled. |
|---|---|

| Note | Use only the HTTPS values. Regenerate the Beacon Access Key only if the existing Browser App or key is no longer available,
                                             or if you must move Finesse monitoring to a new Browser App. If you generate a new key, update the AppDynamics monitoring
                                             configuration with the new Beacon URL and Beacon Access Key. |
|---|---|

| Note | The AppDynamics CLI operation is allowed only if the required AppDynamics agents are deployed and monitoring is enabled on
                                          the target node. If AppDynamics agents are not deployed, the CLI operation is rejected with details displayed on the console. |
|---|---|

| Command | utils app-monitoring disable |
|---|---|
| Description | This command is used to disable performance monitoring on selected nodes. |
| Expected Inputs | Select the node on which performance monitoring needs to be disabled. Confirm to proceed. |
| Expected Outcome | Performance monitoring is disabled for all the selected nodes. |

| Note | The AppDynamics CLI operation is allowed only if the required AppDynamics agents are deployed on the target node. If AppDynamics
                                          agents are not deployed, the CLI operation is rejected with details displayed on the console. |
|---|---|

| Command | utils app-monitoring status |
|---|---|
| Description | This command is used to check if performance monitoring is enabled on selected nodes. This command also shows the following: Proxy enabled status Windows Event monitoring enabled status for ICM nodes |
| Expected Inputs | Select the node for which you want to check the status, and confirm to proceed. |
| Expected Outcome | Shows whether the configuration details for performance monitoring is enabled, disabled, or updated for the selected nodes: If an update is made to the existing configuration and the node is restarted, then the status shows the updated configuration
                                                as current configuration used by AppDynamics performance monitoring. If an update is made to the existing configuration and the node is not restarted, then the status shows both the current configuration
                                                used by AppDynamics performance monitoring as well as the to-be-applied configuration which will be applied post restart. |

| Note | The AppDynamics CLI operation is allowed only if the required AppDynamics agents are deployed on the target node. If AppDynamics
                                          agents are not deployed, the CLI operation is rejected with details displayed on the console. |
|---|---|

| Command | utils app-monitoring test-connection |
|---|---|
| Description | This command is used to test the connectivity of selected Windows or VOS nodes to the AppDynamics controller. |
| Expected Inputs | Select the nodes for which you want to test the connectivity status. |
| Expected Outcome | Shows whether the selected nodes are able to connect to the AppDynamics controller. |

| Note | You can also view, create, overwrite, delete, export, apply and disable the template on the application. For details on managing templates, if your AppDynamics agents are prior to 25.4.0 version, see Configure and Manage Alerting Templates , else see Configure and Manage Alerting Templates . |
|---|---|

| Note | If WidgetName is "EventListWidget", then don't change the "applicationName". |
|---|---|

| Note | If the "entityType" is set to "APPLICATION_COMPONENT", then do not
                                                      make any changes to the "entityName". If the "entityType" is set to "BUSINESS_TRANSACTION", do not make any
                                                      changes to the "scopingEntityName". There are no changes required in these cases as the type of entity is
                                                      a tier-name, which is common to all the nodes in an application. |
|---|---|

| Note | The JMX counter IntervalLoginOperations with the JMX object
                                             name com.cisco.ccbu:category=LoginStats,component0=LoginStats-webservices will be used to determine the total number of logins. If the number of logins that happened in the last 15 seconds is greater than 5,
                                             then it is login phase. Else it is steady phase. Respective threshold will be
                                             used dynamically based on the number of logins. |
|---|---|

| JMX Counter | Description | JMX Object Name | Threshold at Login Phase |
|---|---|---|---|
| ThreadCount | The number of threads running at the current moment. | java.lang:type = Threading | 400 |
| PeakThreadCount | The maximum number of threads run at the same time since the JVM was started or the peak was reset. | java.lang:type = Threading | 500 |
| currentThreadCount | The number of threads the thread pool currently has (both busy and free). | Catalina:type = ThreadPool, name = "http-apr-127.0.0.1-8082" | 120 |
| currentThreadsBusy | The number of threads currently processing requests. | Catalina:type = ThreadPool, name = "http-apr-127.0.0.1-8082" | 100 |
| RequestLongestTime | The maximum amount of time taken to complete an API request, in milliseconds. | com.cisco.ccbu:category = WebAppStats, component0 = AggregateWebappStats | 4000 |
| processCPULoad | The CPU load in this process. | java.lang:type = OperatingSystem | 0.6 |
| NumOfActiveAgentsLoggedIn | The number of agents logged in with XMPP Presence as available in the current side. | com.cisco.ccbu:category = AWSSubsystem, component0 = AWS Statistics Counter | 1500 |
| NumOfAgentsLoggedIn | The number of agents and supervisors logged in currently. | com.cisco.ccbu:category = AWSSubsystem, component0 = AWS Statistics Counter | 2010 |

| JMX Counter | Description | JMX Object Name | Threshold at Steady Phase |
|---|---|---|---|
| ThreadCount | The number of threads running at the current moment. | java.lang:type = Threading | 400 |
| PeakThreadCount | The maximum number of threads run at the same time since the JVM was started or the peak was reset. | java.lang:type = Threading | 500 |
| TotalCallsInSystem | The total number of active calls in the system. | com.cisco.ccbu:category = AWSSubsystem, component0 = AWS Statistics Counter | 1400 |
| AverageProcessingTime | The average time taken for processing CTI messages, in milliseconds. | com.cisco.ccbu:category = AWSSubsystem, component0 = CTIMesssage Statistics Counter | 20 ms |
| currentThreadCount | The number of threads the thread pool currently has (both busy and free). | Catalina:type = ThreadPool, name = "http-apr-127.0.0.1-8082" | 120 |
| currentThreadsBusy | The number of threads currently processing requests. | Catalina:type = ThreadPool, name = "http-apr-127.0.0.1-8082" | 20 |
| RunnablesQueued | Runnables (CTI Messages) still queued. | com.cisco.ccbu:category = AWSSubsystem, component0 = CommandDispatcher | 20 |
| TasksQueued | The tasks (such as client requests and CTI messages) queued. | com.cisco.ccbu:category = AWSSubsystem, component0 = CommandDispatcher | 20 |
| RequestLongestTime | The maximum amount of time taken to complete an API request, in milliseconds. | com.cisco.ccbu:category = WebAppStats, component0 = AggregateWebappStats | 4000 |
| processCPULoad | The CPU load in this process. | java.lang:type = OperatingSystem | 0.5 |
| NumOfAgentsLoggedIn | The number of agents and supervisors logged in currently. | com.cisco.ccbu:category = AWSSubsystem, component0 = AWS Statistics Counter | 2010 |

| JMX Counter | Description | JMX Object Name | Threshold at Login Phase |
|---|---|---|---|
| ExecutingTaskCount | The number of tasks (messages published to node) that are running currently. | com.cisco.ccbu.finesse.openfire: type = PubSubOrderedExecutorStatistics | 60 |
| QueuedTaskCount | The number of tasks in the queue. Messages that are getting published to a node are placed in the queue. | com.cisco.ccbu.finesse.openfire: type = PubSubOrderedExecutorStatistics | 10 |
| PeakThreadCount | The maximum number of threads run at the same time since the JVM was started or the peak was reset. | java.lang:type = Threading | 300 |
| ThreadCount | The number of threads running at the current moment. | java.lang:type = Threading | 300 |
| processCPULoad | The recent CPU usage for the Java Virtual Machine process. | java.lang:type = OperatingSystem | 0.6 |

| Node | Performance Monitoring Configuration | AppD Configuration |
|---|---|---|
| VOS | NA | file get activelog appdynamics/appdynamics.log file get activelogappdynamics/machineagent/logs file get activelog appdynamics/appserveragent/logs/<APM Folder Name> Note Ensure that you use the exact regular expression to accurately retrieve the details of the nested directory. file get activelog appdynamics/appdynamics_default_certificate_import.log file get activelog appdynamics/appdynamics_agents_deploy.log Note This log is available only for target nodes and not for Cloud Connect. | Note | Ensure that you use the exact regular expression to accurately retrieve the details of the nested directory. | Note | This log is available only for target nodes and not for Cloud Connect. |
| Note | Ensure that you use the exact regular expression to accurately retrieve the details of the nested directory. |
| Note | This log is available only for target nodes and not for Cloud Connect. |
| ICM | <Install Directory>:\Cisco\AppDynamics\
log\AppDynamics_Perf_Configuration.log | <Install Directory>:\Cisco\AppDynamics
\log\AppDynamics_Configuration.log |
| CVP | NA | <Install Directory>:\Cisco\CVP\
AppDynamics\log\AppDynamics_Configuration.log |

| Note | Ensure that you use the exact regular expression to accurately retrieve the details of the nested directory. |
|---|---|

| Note | This log is available only for target nodes and not for Cloud Connect. |
|---|---|

| Note | For ICM and CVP, the install directory location changes based on your system configuration. APM Name is constructed with "APM Name-VMhostname", and it is always different in case of every component and node. |
|---|---|