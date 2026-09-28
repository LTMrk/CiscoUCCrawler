---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su2-maintain-and-operate-guid-ceccb45e36
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su2/maintain_and_operate/guide/uccx_b_1251su2_admin-and-operations-guide/uccx_b_12_5_2admin-and-operations-guide_chapter_010001.html
retrieved_at: 2026-08-16T21:36:48.728704+00:00
---

Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU2

# Cisco Unified Contact Center Express Administration and Operations Guide, Release 12.5(1) SU2

Updated: April 11, 2022

Chapter: Subsystems Menu

## Chapter: Subsystems Menu

# Subsystems Menu

## Unified CM Telephony Menu

The Unified CCX system uses the Unified CM Telephony subsystem of
                              		  the Unified CCX Engine to send and receive call-related messages from the Unified CM Computer Telephony
                              		  Interface (CTI) Manager.

To access the Unified CM Telephony Configuration
                              		  web pages, choose Subsystems > Cisco Unified CM Telephony from the Unified CCXAdministration menu
                              		  bar.

The Unified CM Telephony Configuration
                              		  menu contains the following submenu options:

Unified CM Telephony
                                       				  Provider —Choose this option to enter Unified CM Telephony provider
                                    				information.

Unified CM Telephony Call
                                       				  Control Group Configuration —Choose this option to configure CTI port groups
                                    				for applications.

Unified CM Telephony
                                       				  Trigger Configuration —Choose this option to configure Unified CM Telephony triggers
                                    				for applications.

Data Synchronization —Choose this option to check and
                                    				synchronize data components like Unified CM Telephony Users (JTAPI Application
                                    				Users), Unified CCX Triggers/Route points, and Call Control Groups between
                                    				Unified CCX and Unified CM.

Cisco JTAPI Resync —Choose this option to resynchronize
                                    				Cisco JTAPI Client versions.

Advanced Settings —Choose this option to configure advanced
                                    				settings for the Cisco Unified CM Telephony client.

### Unified CM Telephony Provider Configuration

To access this configuration area, choose Subsystems > Cisco Unified
                                       				CM Telephony > Provider from the
                                 		  Unified CCX Administration menu bar. The Cisco Unified CM Telephony Provider
                                 		  web page opens.

Use the Unified CM Telephony Provider
                                 		  Configuration web page to view and modify the primary and secondary location of
                                 		  your Unified CM Telephony provider, and
                                 		  user prefix.

### Unified CM Telephony Call Control Group Configuration

Choose Subsystems > Cisco Unified CM Telephony > Call Control Group from the Unified CCXAdministration menu bar to access the Unified CM Telephony
                                 		  Call Control Group list web page. Use the Unified CM Telephony Call Control
                                 		  Group Configuration web pages to display, add, modify, and delete information
                                 		  about the call control group.

To add a new Unified CM Telephony Call Control
                                 		  Group, click 
                                 		  the Add New icon or button on the Unified CM Telephony Call Control
                                 		  Group Configuration web page.

To modify an existing Unified CM Telephony Call Control
                                 		  Group, click any hyperlink within the Ports List table entry; the Cisco Unified CM Telephony Call Control
                                 		  Group Configuration web page opens.

### Unified CM
                           	 Telephony Triggers Configuration

Choose Subsystems > Cisco Unified CM
                                       				Telephony > Triggers from the Cisco Unified CCX
                                 		  Administration menu bar to configure Unified CM Telephony Triggers.

The Cisco Unified CM Telephony Trigger Configuration web page opens where you can view, add, modify,
                                 		  and delete Unified CM Telephony triggers. To add a Unified CM Telephony trigger, click the Add
                                    			 New icon or button. The Cisco Unified CM Telephony Trigger Configuration web page opens.

Use of two(2) wildcard CTI Route Points that overlap with each
                                             			 other is not supported. For example, Route Point 1: 123XXXX and Route Point 2:
                                             			 1234XXX overlap with one another and is not supported.

However, a wildcard CTI Route point can overlap with a full DID
                                             			 (best match pattern) that doesn't contain a wildcard. For example, Route Point
                                             			 1: 123XXXX and Route Point 2: 1234567 is supported.

### Synchronize Unified CM Telephony Data

You can configure the telephony data synchronization through a new web page called Cisco Unified CM Telephony Data Synchronization.

The data synchronization process ensures that
                                 				the data components such as Unified CM Telephony Users (JTAPI Application Users),
                                 				Unified CCX Triggers/Route points, Call Control Groups between Unified CCX and
                                 				Unified CM, and SRTP are synchronized without any inconsistency.

The Data Check option displays if the selected data
                                 				components are synchronized between Unified CCX and Unified CM. If you find any
                                 				inconsistency, use the Data Resync option to rectify the
                                 				issue.

To check and synchronize the JTAPI data components between Cisco Unified CM and Cisco Unified CCX, perform the following steps:

Caution

It is important that you plan to perform this task during off peak
                                             			 hours to avoid hampering routine contact center operations.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > Cisco
                                                				  Unified CM Telephony > Data
                                                				  Synchronization .

The Cisco Unified CM Telephony Data Synchronization page appears.

Step 2

Choose the desired components by selecting the corresponding check box:

Call Control Group(s)

Trigger(s)

CM Telephony User(s)

SRTP

Step 3

Click Data Check or Data Resync .
                                          					When you click Data Check or Data
                                             						Resync , a confirmation message dialog box appears prompting you
                                          					to either proceed or cancel. Click OK to continue.

After you click OK in the confirmation message for Data Check or
                                                         							Data Resync, you are not allowed to cancel the process.

Step 4

The Cisco Unified CM Telephony Data Synchronization web page continues to
                                          					update until the Data Check or Data Resync process is complete. On completion of
                                          					the Data Check or Data Resync process, the result is displayed in the same web
                                          					page in a tree structure. The result for each selected component is displayed in
                                          					collapsed format with a tick mark if no mismatch is found. Click the arrow that
                                          					is next to each selected component to expand and view the detailed results.

If any mismatch is found in the elements of the selected component, the
                                             						results for those components are displayed automatically in an expanded
                                             						format.

If you had multiple device pools (for Call Control Groups) in
                                                               									your older versions of Unified CCX setup, performing Data Resync
                                                               									after an upgrade merges all multiple device pools to a single
                                                               									default device pool. However, you can manually assign a
                                                               									different device pool to the Call Control Group if the default
                                                               									device pool is not the intended one.

When you select SRTP and click Data Check ,

The status of secure JTAPI configuration for subsystems JTAPI and RmCm is displayed
                                                                     											under sections CM Telephony and RmCm respectively.

In a HA setup, the status of devices and device profiles that are associated with the
                                                                     											primary RmCm user and the system-generated RmCm user is
                                                                     											displayed under subsections RmCm
                                                                        												Devices and RmCm Device
                                                                        												Profiles respectively.

When you select SRTP and click Data
                                                                  									Resync ,

The secure JTAPI configuration for subsystems JTAPI and
                                                                     											RmCm are re-synchronized as per Unified CCX SRTP
                                                                     											configuration and the status is displayed in the
                                                                     											respective subsections.

In a HA setup, if devices and device profiles do not match between the primary RmCm
                                                                     											user and system-generated RmCm user, the
                                                                     											system-generated RmCm user is synchronized with the
                                                                     											devices and device profiles that are configured for
                                                                     											primary RmCm user.

### Unified CM Telephony Cisco JTAPI Resync

Choose Subsystems > Cisco Unified
                                       				CM Telephony > Cisco JTAPI Resync from the Cisco Unified CCX Administration menu bar to resynchronize the JTAPI
                                 		  client version on the Unified CCX with the JTAPI version on the Unified CM. You
                                 		  can view the status of Cisco JTAPI client resynchronization in this web page.

If the Unified CCX detects a mismatch, the system downloads
                                 		  and installs the compatible or JTAPI client required installer version.
                                 		  Restart the Unified CCX Engine to view these configuration changes.

The JTAPI client update happens only on the local node and
                                 		  not on the second node in case of High Availability deployment.

### Unified CM Telephony Advanced Settings

Choose Subsystems > Cisco Unified
                                       				CM Telephony > Advanced Settings from the Cisco Unified CCX Administration menu bar to configure advanced
                                 		  settings for the Unified CM Telephony Client.

Use the Unified CM Telephony Advanced
                                 		  Settings web page to update the following information:

Periodic Wakeup Interval (seconds): Select the check box before
                                       				Enable Periodic Wakeup prior to updating the existing value in this field.

Queue Size Threshold: Select the check box before Enable Queue Stats prior to updating the
                                       				existing value in this field.

CTI Request Timeout (sec)

Provider Open Request Timeout (sec)

Provider Retry Interval (sec)

Server Heartbeat Interval (sec)

Route Select Timeout (ms)

Post Condition Timeout

Use Progress As Disconnect

Click 
                                 		  the Update icon that displays in the toolbar in the
                                 		  upper left corner of the window or the Update button that displays at the bottom of the
                                 		  window to save the changes. Restart the Unified CCX Engine to view these
                                 		  configuration changes.

In case of High Availability deployment, the changes are
                                 		  propagated to the second node. If the second node cannot be contacted, an alert
                                 		  message indicating that the update has failed on the remote node is displayed.

## RmCm Menu

Use the
                              		  RmCm Configuration web page to configure skills groups, resources, resource
                              		  groups, Contact Service Queues (CSQs), and RM (Resource Manager) Unified CM
                              		  Telephony providers. To access the Unified CCX Configuration web page, choose Subsystems > RmCm from the Unified
                              		  CCXAdministration menu bar.

The RmCm
                              		  menu contains the following submenu options:

Skills —Click this submenu to create skills.

Resources —Click this submenu to assign a resource group and skills to agents.

Resource Groups —Click this submenu to create resource groups.

Contact Services Queues (CSQs) —Click this submenu to configure CSQs.

RmCm Provider —Click this submenu to configure the RM (Resource Manager) Unified CM Telephony provider for the RmCm subsystem.

Assign Skills —Click this submenu to assign skills and a resource group to agents in bulk.

Agent Based Routing Settings —Click this submenu to send a call to a specific agent, rather than to any agent available in a CSQ.

Teams —Click this submenu to create or associate teams with various agents, CSQs, and supervisors.

### Skill Configuration

Use the Skills page to add, modify, or delete skill.

Choose Subsystems > RmCm > Skills from the Unified CCXAdministration menu bar to access the Skills summary web
                                 		  page.

#### Add New Skill

Use the Skill Configuration area to add a new skill name.

Click 
                                             			 the Add New icon that displays in the toolbar in
                                             			 the upper left corner of the window or the Add New button that displays at the bottom of
                                             			 the window to access the Skill Configuration area.

#### Modify Skills

Click the required skill in the Skill name column on the
                                    		  Skill Configuration web page to access the Skill Configuration area.

Click 
                                             			 the Open Printable Report of this Skill
                                                				Configuration icon to view a list of the resources associated with
                                             			 that skill.

### Resources
                           	 Configuration

Use the Resources
                                 		  Configuration area to assign a resource group, to assign skills to a resource,
                                 		  and to assign an alias to the agent. When the agent is on chat, the alias of
                                 		  the agent is displayed to the customer.

To
                                 		  access this configuration area, choose Subsystems > RmCm > Resources from the Unified
                                 		  CCXAdministration menu bar. The main area of the Resources area of the Unified
                                 		  CCX Configuration web page contains a list of resources (if configured).

Click the Open Resources Summary Report icon to open the Resources Summary Report in a new window. For each resource, this report lists the resource groups associated
                                 with the resource, the Unified CCX extension of the resource, and the number of CSQs and team to which the resource is assigned.

#### Modify Resource

Use the Resource Configuration area to modify resource
                                    		  configuration.

To access the Resource Configuration area, click any of the
                                    		  required resource in the Resource area of the Unified CCX Configuration summary
                                    		  web page.

Click 
                                             		  the Open Printable Report of this Resource
                                                			 Configuration icon to open a Resource Report for the agent. The
                                             		  Resource Report lists each agent resource ID, resource name, Unified CCX
                                             		  extension, resource group, automatic available status, skills, CSQs, and team.

### Resource Group Configuration

Use the Resource Group Configuration web page to display and
                                 		  modify the names of existing resource groups and to add new resource groups.

Choose Subsystems > RmCm > Resource
                                       				Groups from the Unified CCXAdministration menu bar
                                 		  to access the Resource Groups web page.

#### Add New Resource Group

Use the Resource Configuration area to enter resource group
                                    		  name in the Resource Group Name field.

Add a new Resource Groups by clicking Add New icon or button in the Resource Group
                                             		  area of the Unified CCX Configuration web page.

#### Modify Existing Resource Groups

Use the Resource Modification page to change or update the
                                    		  resource group name into the Resource Group Name field.

Modify an existing Resource Group by clicking the required
                                    		  resource group in the Resource Groups area. In the Resource Group Configuration
                                    		  area, change the Resource Group and update.

Click 
                                             		  the Open Printable Report of this Resource Group
                                                			 Configuration icon to view a list of the available resources for
                                             		  this resource group.

### Contact Service Queues Configuration

Use the Contact Service Queues area of the Unified CCX Configuration web page to display existing CSQs, delete a CSQ, and
                                 add a new CSQ.

To access the Contact Service Queues area, choose Subsystems > RmCm > Contact Service Queues from the Unified CCXAdministration menu.

When all the CSQs assigned to the teams associated to the Supervisor are deleted, the Advanced Supervisor Capability of Queue
                                             Management is removed for the Supervisor.

#### Add a CSQ

Use the Contact Service Queues Configuration area to add a
                                    		  new CSQ.

To access the Contact Service Queues Configuration area,
                                    		  click 
                                    		  the Add New icon or button in the Contact Service
                                    		  Queues area of the Unified CCX Configuration web page.

To open the Contact Service Queue Report for the required
                                    		  CSQ, click 
                                    		  the Open Printable Report of this CSQ Configuration icon from the Contact Service Queues Configuration area.

### RmCm Provider Configuration

Use the RmCm Provider area of the Unified CCX Configuration
                                 		  web page to identify the Unified CM Telephony user for the
                                 		  Resource Manager.

Choose Subsystems > RmCm > RmCm
                                       				Provider from the Unified CCXAdministration menu bar
                                 		  to access the RmCm Provider web page.

### Skills Configuration Assignment

Use the Assign Skills area of the Unified CCX Configuration
                                 		  web page to modify an existing resource group and skill configuration or to
                                 		  assign new resource groups and skills to all or selected agents.

Choose Subsystems > RmCm > Assign
                                       				Skills from the Unified CCXAdministration menu bar
                                 		  to access this configuration area.

This web page also contains the following icons and buttons:

Add Skill —to add new skills or resource groups to all or
                                       				selected agents.

Remove Skill —to remove skills of all or selected agents.

#### Add Skills

When you click 
                                    		  the Add Skill button in the Assign Skills area of
                                    		  the Unified CCX Configuration web page, the Add Skill area opens. Use the Add
                                    		  Skill area to add a resource group and skills to the selected agents.

#### Remove Skills

When you click 
                                    		  the Remove Skill button in the Assign Skills area of
                                    		  the Unified CCX Configuration web page, the Remove Skill area opens. Use the
                                    		  Remove Skill area to remove skills of all or selected agents.

### Agent Based Routing Settings Configuration

Use the Agent Based Routing Settings area of the Unified CCX
                                 		  Configuration web page to configure Automatic Work and Wrapup Time.

Choose Subsystems > RmCm > Agent
                                       				Based Routing Settings from the Unified
                                 		  CCXAdministration menu bar to access this configuration area.

### Teams Configuration

Use the Teams area of the Unified CCX Configuration web page
                                 		  to create or associate teams with various agents, CSQs, and supervisors.

Choose Subsystems > RmCm > Teams from the Unified CCXAdministration menu bar to access this configuration area.

#### Assign Supervisor Privilege to a User

Step 1

From the Unified CCX Administration menu, choose Tools > User Management > User View .

The User Configuration page displays the list of all users.

Step 2

Click the user to whom you want to assign supervisor capability.

The User Configuration page displays information about that user. In the Capabilities section, the left pane displays the
                                                list of assigned capabilities and the right pane displays the list of capabilities.

Step 3

Using the left arrow, assign Supervisor capability.

Step 4

Click Update to save your changes.

Agents, who have logged in must logout and login again to use supervisor specific features.

For agents with chat or email skill, who have logged in, it may take maximum of 30 mins to reflect the change.

#### Create Teams

Use the Teams area of the RmCm Configuration web page to create or associate teams with various agents, CSQs, and supervisors.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Teams .

Step 2

Click Add New icon that displays in the tool bar in the upper left corner of the window or the Add New button at the bottom of the window.

The Team Configuration page appears.

Step 3

Enter the Team Name .

Step 4

Select the Primary Supervisor from the drop-down list.

Step 5

(Optional) Select the secondary supervisor name from the Available Supervisors list and use the arrow icon to move it into the Secondary Supervisors list.

Step 6

(Optional) To add an agent to this team, select an agent name in the Available Resources list and use the arrow icon to move it into the Assigned Resources list.

Step 7

(Optional) Select the CSQ name in the Available CSQs list and use the arrow icon to move it into the Assigned CSQs list to add the CSQ to this team.

Step 8

In the Team Settings section, specify the following information:

Parameter Name

Parameter Value

Global Settings

Change Agent State to Not Ready when Agent Busy on Non ACD Line

Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                            lines are used for Incoming or Outgoing calls. The options are:

Enable—Enables the state change of the agent in the team.

Disable (default)—Disables any state change of the agent in the team.

Allow team settings to override global settings—A check box to override the global settings. The global settings is available
                                                                  at System > System Parameters > Agent Settings .

When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes.

When you click OK, the team level settings override the global settings.

Displays the global settings.

Auto Answer

Enables the incoming calls to be auto answered. The options are:

Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent.

Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent.

Disable (Default)—Auto answer is not enabled.

To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01.

This functionality is applicable only for the agents and not for the supervisors of the team.

Step 9

Click Save to apply changes or Cancel to exit.

#### Modify Teams

Use the Teams area to modify the supervisors, agents, CSQs, or auto answer configuration on an existing Team.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Teams .

Step 2

Click a name in the Team Name column.

The Team Configuration page appears.

Step 3

Select the Primary Supervisor from the drop-down list.

Step 4

(Optional) Select the secondary supervisor name from the Available Supervisors list and use the arrow icon to move it into the Secondary Supervisors list.

To remove the secondary supervisor name from this team, select the supervisor name in the Secondary Supervisors list and use the arrow icon to move it into the Available Supervisors list. This supervisor now belongs to the default team.

Step 5

(Optional) Select an agent name in the Available Resources list and use the arrow icon to move it into the Assigned Resources list to add an agent to this team.

To remove an agent from this team, select an agent name in the Assigned Resources list and use the arrow icon to move it into the Available Resources list. This agent now belongs to the default team.

Step 6

(Optional) Select the CSQ name in the Available CSQs list and use the arrow icon to move it into the Assigned CSQs list to add the CSQ to this team.

To remove a CSQ from this team, select a CSQ name in the Assigned CSQs list and use the arrow icon to move it into the Available CSQs list. This CSQ now belongs to the default team.

Step 7

In the Team Settings section, specify the following information:

Parameter Name

Parameter Value

Global Settings

Change Agent State to Not Ready when Agent Busy on Non ACD Line

Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                            lines are used for Incoming or Outgoing calls. The options are:

Enable—Enables the state change of the agent in the team.

Disable (default)—Disables any state change of the agent in the team.

Allow team settings to override global settings—A check box to override the global settings. The global settings are available
                                                                  at System > System Parameters > Agent Settings .

When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes.

When you click OK, the team level settings override the global settings.

Displays the global settings.

Auto Answer

Enables the incoming calls to be automatically answered. The options are:

Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent.

Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent.

Disable (Default)—Auto answer is not enabled.

To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01.

Step 8

Click Save or Update to apply changes, Cancel to exit or Delete to delete this team.

#### Delete a Team

Use the Teams area of the RmCm Configuration web page to
                                    		  delete an existing Team.

Step 1

From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Teams .

The Teams web page opens.

Step 2

Click 
                                             			 the Delete icon beside the Team Name icon you want to
                                             			 delete.

The system prompts you to confirm the delete.

Step 3

Click OK .

## Chat and Email Menu Options

Important

The Chat option is available with Premium license package when Cisco Finesse is not activated.

The Chat and Email option is available with Premium license package when you activate Cisco Finesse.

The Chat and Email menu contains the following sub menu options:

Customer Collaboration Platform Configuration —Choose this option to configure the Customer Collaboration Platform parameters. This page also displays the overall health of Customer Collaboration Platform .

Mail Server Configuration —Choose this option to configure the mail server. This page is available on the Unified CCX node with a premium license.

Contact Service Queues —Choose this option to configure chat and Email CSQs. You can configure the email CSQs on the Unified CCX node with a premium
                                    license.

Predefined Responses —Choose this option to define the chat and email predefined responses that are available in the Manage Chat and Email gadget
                                    on the Finesse Agent Desktop.

Channel Parameters —Choose this option to configure channel parameters.

Chat Widget —Choose this option to configure and manage chat widgets.

Teams —Choose this option to configure teams.

### Customer Collaboration Platform Configuration

Use the CCP Configuration web page to configure Cisco Customer Collaboration Platform . You must configure information only on this web page to enable the chat and email features.

Cisco Unified CCX does not support custom configuration changes on the chat and email campaigns or feeds from the Customer Collaboration Platform administration page.

This option is available only with the Unified CCX Premium license package. The email feature support for Unified CCX depends
                                 on the Customer Collaboration Platform version. For information about feature compatibility, see the Unified CCX Compatibility related information, located at: https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html .

Any configuration change using Customer Collaboration Platform Administration interface is not supported.

On a high availability setup, after the Add to Cluster operation is successful, the following message is displayed:

In case of HA, configure the CCP on secondary node after adding to cluster in the secondary node.

Every time you navigate to this page, the state of feeds, campaigns, and notifications rules are validated for chat and email,
                                 the connectivity to the email server is checked, and the web page shows the appropriate status. Icons are used as visual indicators
                                 to display the status of each service. Hover the cursor over the icon to display a tool tip that explains the reason for the
                                 current state. As part of validation, Unified CCX checks the following:

CCP XMPP Service

Unified CCX checks the connectivity with the Customer Collaboration Platform XMPP service. If the XMPP service is down, the following message is displayed:

CCP XMPP service is not accessible. Check the logs for more details.

Unified CCX checks the connectivity with the Customer Collaboration Platform runtime service. If the runtime service is down, the following message is displayed:

CCP runtime service is not accessible. Check the logs for more details.

CCP Tomcat Service

Unified CCX checks the connectivity with the Customer Collaboration Platform Tomcat service. If the Tomcat service is down, the following message is displayed:

Unable to communicate to the CCP on the IP address(Hostname) provided. Please verify whether CCP is running on this IP address(Hostname)
                                          or check the network connection and make sure that CCP is reachable from CCX.

CCP Status

Feeds

Unified CCX validates the status of the intended chat and email feeds in Customer Collaboration Platform .

—All the feeds are operating as usual in Customer Collaboration Platform .

—One or more feeds mismatches with Customer Collaboration Platform .

—All the feeds are missing in Customer Collaboration Platform .

Campaigns

Unified CCX validates the status of the intended chat and email campaigns in Customer Collaboration Platform .

—All the campaigns are operating as usual in Customer Collaboration Platform .

—One or more campaigns mismatches with Customer Collaboration Platform .

—All the campaigns are missing in Customer Collaboration Platform .

Notifications

Unified CCX validates the status of the intended chat and email notifications in Customer Collaboration Platform .

—All the notifications are operating as usual in Customer Collaboration Platform .

—One or more notifications mismatches with Customer Collaboration Platform . This status icon also appears after configuration, when no chat and email contact is injected yet. The status will change
                                                   to normal after successful injection of chat and email contact.

—All the notifications are missing in Customer Collaboration Platform .

Email Cache

Unified CCX checks and alerts the user about the email cache.

—Email cache is operating as usual.

—Unable to cache emails. No new emails will be fetched.

Not Applicable — Customer Collaboration Platform version is not compatible.

Email Server

Unified CCX checks the connectivity with the email server.

—Email server is operating as usual.

Not Configured —Channel provider is not configured.

Not Applicable —The following are the reasons for the current state:

Cisco Finesse is not active.

Email CSQ is not configured.

Customer Collaboration Platform version is incompatible with the Email feature.

—Unable to reach the email server.

CCP Chat Gateway

This indicates the status of the Customer Collaboration Platform Chat Gateway and the Channel that is integrated.

CCP Chat Gateway

—The gateway is operating as usual and is configured with a channel.

—The gateway is not in an operating state as it is either Unreachable or configurations are incorrect.

Not Configured —The gateway is not configured and no channels are configured.

Not Applicable —The following are the reasons for the current state:

Cisco Finesse is not active.

Customer Collaboration Platform version is incompatible or is not configured.

Facebook Messenger Integration —This indicates whether the channel is enabled. It also indicates the last failure recorded in the channel. This helps to
                                                   determine any intermittent or permanent errors.

Step 1

From the Unified CCX Administration menu bar, choose Subsystems > Chat and Email > CCP Configuration as applicable.

The Configuration web page appears.

You must perform the following actions:

In the Unified CCX, upload Customer Collaboration Platform certificate to the Unified CCX Tomcat trust store using the Cisco Unified OS Administration interface. You can also use the set cert import trust tomcat CLI.

In the Customer Collaboration Platform, upload Unified CCX certificate to the Customer Collaboration Platform Tomcat trust
                                                               store using the Cisco Unified OS Administration interface.

Unified CCX and Customer Collaboration Platform servers must have DNS entries. Customer Collaboration Platform must be accessible to Unified CCX by hostname. If the entries are not valid, an error is displayed.

Step 2

Specify the following fields for Customer Collaboration Platform :

Field

Description

IP Address / Host Name

IP address or fully qualified domain name of the Customer Collaboration Platform server. For example, 192.168.1.5 or host.example.com.

User Name

Username of the Customer Collaboration Platform administrator.

Password

Password of the Customer Collaboration Platform administrator.

When the Customer Collaboration Platform application password is reset, ensure that the new password is first updated in Unified CCX and then reset the password in Customer Collaboration Platform . This prevents the account getting locked due to the authentication attempts from Unified CCX with old password.

Step 3

Click Save to save the changes.

After saving a valid Customer Collaboration Platform configuration, you cannot change the IP Address / Host Name details. If you want to change the configuration, delete the existing configuration and create a new one.

If you see an error message, click Save to re-create feeds, campaigns, and notifications for chat and email in Customer Collaboration Platform .

When Unified CCX hostname is changed or when a new Unified CCX node is added, the Customer Collaboration Platform Configurations must be saved again. This enables the change to take effect to re-create all the notifications for email and
                                                               chat in Customer Collaboration Platform .

#### Delete Customer Collaboration Platform Configuration

Important

Ensure that the Customer Collaboration Platform configuration delete operation is performed during maintenance window.

Ensure that the Customer Collaboration Platform configuration hostname is deleted manually from Desktop Layout in Cisco Finesse Administration.

Step 1

On the Customer Collaboration Platform Configuration page, click Delete . A confirmation dialog box appears.

Step 2

Click OK to delete the Customer Collaboration Platform configuration.

This deletes the Customer Collaboration Platform configuration data from the Unified CCX configuration database. In addition, it deletes the configurations such as Feeds,
                                                Campaigns, Notifications, and Webhooks (that were created by Unified CCX) from the Customer Collaboration Platform application.

If you select Delete all Associated Chat and Email CSQs check box in the confirmation dialog box, all the chat and email CSQs are also deleted from the Unified CCX configuration
                                                            database.

Step 3

Restart the Unified CCX engine on both the nodes.

Step 4

Click Cancel to cancel this operation.

##### What to do next

Access Customer Collaboration Platform application: By default, access to Customer Collaboration Platform administration user interface is restricted. Administrator can provide access by using the allowed list of client's IP addresses
                                    and revoke by removing the client's IP from the allowed list. For any modification for permitlist to take effect, Cisco Tomcat
                                    must be restarted.

Permitlist administrator user interface: Use the utils permitlist admin_ui add command to use the allowed list the client's IP address, with which you want to access the Customer Collaboration Platform application. For example: admin:utils permitlist admin_ui add 10.XXX.XX.XX .

Delete Campaign: In the Customer Collaboration Platform application, select the Configuration tab. Select the checkbox to the left of one or more campaign names and click Delete . Click OK in the confirmation window to confirm the deletion of the selected campaigns.

Delete Feeds: In the Customer Collaboration Platform application, select the Configuration tab. Select the checkbox to the left of one or more feed names and click Delete . Click OK in the confirmation window to confirm the deletion of the selected feeds.

Delete Notifications: In the Customer Collaboration Platform application, select the Administration tab. Select the checkbox to the left of one or more notification names and click Delete . Click OK in the confirmation window to confirm the deletion of the selected notifications.

#### Reinject Email
                              	 Contacts

Emails may be parked in Customer Collaboration Platform due to component failures or if the email server is down or not reachable. You can ensure that these emails are attended
                                    to when the services are restored by reinjecting the email contacts.

The latest 200 unread or reserved, social email contacts across the email CSQs are reinjected.

To reinject the email contacts back to Unified CCX, click Subsystems > Chat and Email CCP Configuration > Reinject .

The CCP Configuration web page is reloaded, but the configuration is not updated.

#### Chat
                              	 Transcripts

You can search and retrieve stored chat transcripts. You can search by username (chat.agentName) and alias (chat.agentNickname).
                                 For more information on how to perform a default search or a field-specific search, see the "Search" section of the Cisco Customer Collaboration Platform User Guide or the Customer Collaboration Platform interface online help.

For information on how to change chat storage space and calculate the disk space that you need to store data for a specific
                                 duration, see the online help that is available for the Customer Collaboration Platform interface or see the Cisco Customer Collaboration Platform User Guide , located at:

https://www.cisco.com/en/US/products/sw/custcosw/ps1846/tsd_products_support_series_home.html

### Mail Server
                           	 Configuration

Use the Mail Server Configuration web page to configure the mail server.

#### Before you begin

Create accounts and email addresses that must be used for CSQ creation.

Local Exchange Server

Run the commands set-service msExchangeIMAP4 -startuptype automatic , and start-service msExchangeIMAP4 on Microsoft Exchange to set the Microsoft Exchange IMAP4 service to start automatically.

Run the command set-service msExchangeIMAP4BE -startuptype automatic , and run start-service msExchangeIMAP4BE command (for Microsoft Exchange 2013) on Microsoft Exchange to set the Microsoft Exchange IMAP4 Back End service to start
                                             automatically.

Gmail

Two types of authentication, Basic and OAuth 2.0 are available for Gmail. OAuth 2.0 is more secure.

You can select the authentication type while configuring a CSQ.

To use OAuth, you have to create a service account in the Google Cloud server. While creating a service account, you must
                                             download the JSON file that has the Private Key details, which must be uploaded while configuring a Contact Service Queue
                                             (CSQ). For more information on creating a service account, see https://developers.google.com/identity/protocols/oauth2/service-account .

To authorize a service account for accessing emails, ensure that " https://mail.google.com/ " is entered in API Scopes .

Microsoft Office 365

OAuth 2.0 authentication is used to read emails and Basic authentication is used to send emails.

Create the Azure application for OAuth 2.0 for authentication, and get the Tenant ID, Client ID, and Client secret from the Azure application. For more information
                                             on creating the Azure application see https://docs.microsoft.com/en-us/exchange/client-developer/legacy-protocols/how-to-authenticate-an-imap-pop-smtp-application-by-using-oauth#use-client-credentials-grant-flow-to-authenticate-imap-and-pop-connections .

Create the service principal for the Azure application. The service principal must have "FullAccess" (access rights) of the
                                             mailbox to read the email.

Step 1

From the
                                          			 Unified CCX Administration menu bar, choose Subsystems > Chat and
                                                				  Email > Mail Server Configuration .

Step 2

Complete or
                                          			 modify the following fields for the mail server:

Field

Description

Mail
                                                         							 Server Settings

Mail
                                                         							 Server

Choose the mail server that is required to be configured from the listed options:

MS Exchange Server / Office 365

Gmail

Unified CCX must be connected to a dedicated mail server. Ensure that the email account is not shared.

IMAP
                                                         							 Folder Structure

Sent
                                                         							 Items Folder Name

The name of the sent items folder of the respective mail server that is configured.

Incoming (Secure IMAP)

Host
                                                         							 Name

Fully qualified domain name (FQDN) of the incoming (IMAP)
                                                         							 server. Do not enter the IP address.

Port Number

Port
                                                         							 number that is used to connect to the IMAP server.

The
                                                         							 default port number is 993.

Outgoing (Secure SMTP)

Host Name

FQDN of the outgoing (SMTP) server. Do not enter the IP address.

Port
                                                         							 Number

Port number that is used to connect to the SMTP server.

The
                                                         							 default port number is 587.

Proxy Settings

HTTP

Choose the Enable or Disable radio button to use HTTP proxy for Mail Server connectivity. By default the Disable option is selected and Enable option is disabled. To enable HTTP , configure Http in Proxy Parameters section of System Parameters page.

SOCKS

Choose the Enable or Disable radio button to use socks proxy for Mail Server connectivity. By default the Disable option is selected and Enable option is disabled. To enable SOCKS , configure SOCKS Proxy in System Parameters page.

Description

Description of the mail server.

Step 3

Click Update to save the changes.

### Contact Service
                           	 Queues

#### Before you begin

Microsoft Office 365 option is available from 12.5(1)SU2 ES03 onwards.

To change the Microsoft Office 365 authentication from Basic to OAuth 2.0 , update the mail server selection to Microsoft Office 365, and then edit the email CSQ where the OAuth details must be filled.

You must create a skill before creating a CSQ. For information about creating a skill, see Skill Configuration section in the Cisco Unified Contact Center Express Administration and Operations Guide .

Before creating an email CSQ, you must have configured the mail server.

Step 1

From the Unified CCX Administration menu bar, choose Subsystems > Chat and Email > Contact Service Queues as applicable.

The Contact Service Queues (CSQs) web page opens and displays the information for existing chat and email CSQs if any.

Step 2

To add a new chat or email CSQ, click the Add New icon that appears in the toolbar in the upper left corner of the window or the Add New button that appears at the bottom of the window.

The Contact Service Queue Configuration web page opens.

Step 3

Specify the
                                          			 following fields:

Field Name

Description

CSQ
                                                         							 Name

Name
                                                         							 for the CSQ.

Resource Selection Criteria

Resource selection criteria chosen for the chat CSQ.

Longest Available —Selects the agent who has been in the Available state for the longest amount of time.

Most Skilled —Used for expert agent chat distribution. Selects the agent with the highest total competency level. The total competency
                                                               level is determined by adding the agent's competency levels for each assigned skill that is also assigned to the CSQ.

Example 1: If Agent1 is assigned Skill1(5), Skill2(6), and Skill3(7) and CSQ1 specifies Skill1(min=1) and Skill3(min=1), the
                                                                     total competency level for Agent1 for CSQ1 is 12.

Example 2: If Agent1 is assigned Skill1(5) and Skill2(6), and Skill3(7) and CSQ1 specifies Skill1(min=1), only, the total
                                                                     competency level for Agent1 for CSQ1 is 5.

To change the competence level for an already configured agent, change the agent skill level and save the CSQ.

If two agents score equal in the primary selection criteria, the agent who was updated first will be assigned to the incoming
                                                                           chat until the maximum chats threshold is reached.

Field
                                                         						  Name

Description

CSQ
                                                         						  Type

Choose
                                                         						  Chat.

Field
                                                         						  Name

Description

CSQ
                                                         						  Type

Choose
                                                         						  Email.

You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed:

```
Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs.
```

Mail
                                                         						  Server

Fully
                                                         						  Qualified Domain Name (FQDN) of email server. This field displays the mail
                                                         						  server that you configured.

Authentication Type

The type of authentication that is used to access the configured email account.

Basic is used to access both types of email, Office 365 and Gmail by using username and password. By default, this option is selected.

OAuth is used to access Gmail by using the OAuth Private Key file that is downloaded from the Gmail mail server. Supports OAuth
                                                         2.0 protocol.

This field is displayed only when you have configured Gmail mail server.

Email
                                                         						  username

The
                                                         						  email address to which emails are sent or retrieved.

Email password

Password for the email account.

This field is mandatory when the email server type is Microsoft Office 365 or Microsoft Exchange.

This field is optional when the email server type is Gmail.

Private Key

The JSON file that contains the OAuth Private Key, which is generated while creating Service Account in Google Cloud server.
                                                         Click Upload to select the file.

This field is displayed only when Authentication Type is OAuth .

Tenant ID

This is the Azure cloud tenant ID.

This field is displayed when Microsoft Office 365 is selected as the email server.

Client ID

This is the Azure cloud application client ID.

This field is displayed when Microsoft Office 365 is selected as the email server.

Client secret

This is the Azure cloud application client secret.

This field is displayed when Microsoft Office 365 is selected as the email server.

Inbox Folder Name

The
                                                         						  folder from which emails will be fetched and queued for the Contact Service
                                                         						  Queue.

Default value = Inbox folder of the selected mail server type

If you change the Inbox folder name, which is already in use, the emails that are downloaded and cached by Customer Collaboration Platform are made available to agents. The remaining emails in the folder are ignored.

Sent
                                                         						  Items Folder Name

The folder to which Customer Collaboration Platform will move the response email to, when it is sent.

Test Configuration

This checks the following:

Connectivity from Customer Collaboration Platform to the configured mail server by using the user credentials that is specified in the Contact Service Queue (CSQ) configuration.

Presence of and permissions to the Inbox, Drafts, Outbox, and Sent Items folder for the user, that is specified in the CSQ
                                                               configuration.

Poll
                                                         						  Interval (Seconds)

Frequency in seconds to fetch emails from the server.

Default value = 180, Range = 60 to 3600

Snapshot Age (Minutes)

Specify the time in minutes from when the emails are to be
                                                         						  fetched.

Default value = 120, Range = 60 to 43200

For
                                                         						  example, if you specify 120 minutes, this field fetches the emails from the
                                                         						  last two hours.

Step 4

Click Next .

The Skill
                                             				Association for CSQ area opens with the newly assigned CSQ name.

You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed:

```
Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs.
```

Step 5

From the
                                          			 Available Skills list, choose the skill that you want to associate with the CSQ
                                          			 by clicking it. To choose more than one skill, press the Ctrl key
                                          			 and click the skills that you want to associate with the CSQ.

Step 6

Click Add .

The chosen
                                             				skill and the minimum competence level for that skill are displayed in the
                                             				right pane under the heading Selected.

To delete
                                                         				  the skill from the Skills Required list, click the Delete icon next to Minimum Competence .

Step 7

Specify a
                                          			 minimum competence level for the skill assigned to the CSQ.

Step 8

To view the
                                          			 associated resources, click Show
                                             				Resources .

Step 9

Click Save to save the changes for the CSQ.

The newly
                                             				added CSQ appears in the List of CSQs .

You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed:

```
Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs.
```

You can sort
                                             				the CSQs by title by clicking the CSQ Name header and by type by clicking the CSQ Type header.

Step 10

To view the printable report and associated resources, click the CSQ for which you want to view the report and the associated
                                          resources and then click Open Printable Report .

To delete a CSQ, click the CSQ that you want to delete and then click Delete . A warning dialog box appears, asking you to confirm the deletion. To delete, click OK .

Caution

Deletion of the chat CSQ affects the associated chat web forms. After deleting, modify the corresponding chat web form configurations
                                                         and generate the HTML code.

### Predefined
                           	 Responses

To access the predefined
                              		responses, choose Subsystems > Chat > Predefined
                                    			 Responses OR Subsystems > Chat and
                                    			 Email > Predefined Responses as applicable.

Use the Predefined Responses page to configure and manage chat and email predefined responses. You can add a maximum of 500 chat and email predefined
                              responses in total. These predefined responses are available in the Manage Chat and Email gadget on the Cisco Finesse Desktop.

You can configure the
                              		responses to be available either to all the agents or only to the agents that
                              		are associated with specific CSQs.

#### Predefined
                              	 Responses

Using this web
                                    		  page, you can add, modify, and delete predefined responses.

You can add a
                                    		  maximum of 500 chat and email predefined responses in total.

To modify an existing predefined response, click the Title header for the predefined response that you want to modify. To
                                                delete an existing predefined response, click the Delete icon for the predefined response that you want to delete.

Step 1

From the
                                             			 Unified CCX Administration menu bar, choose Subsystems > Chat > Predefined
                                                   				  Responses OR Subsystems > Chat and
                                                   				  Email > Predefined Responses as applicable.

The Predefined Responses web page opens, displaying the
                                                				information for existing responses, if any.

Step 2

Click the Add
                                                				New icon that is displayed in the toolbar in the upper left corner
                                             			 of the window or the Add
                                                				New button that is displayed at the bottom of the window to create
                                             			 a new response.

The Predefined Response Configuration web page opens.

Step 3

Specify the
                                             			 following information:

Field

Description

Title

Unique identifier of the predefined response.

The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (|) are not
                                                                        allowed.

Type

Types of media.

Response Description

Description for the predefined response.

Rich Text Editor is available to create an HTML-based email predefined response.

Use the supported tags as provided in the Rich Text Editor for formatting purpose.

Plain Text Editor is available to create a chat predefined response.

The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (|) are not
                                                                        allowed in Plain Text Editor for Chat Predefines Response.

The maximum characters limit for predefined response for chat and email is 1500.

In case of email, rich text is supported and includes the HTML tag characters for representing rich text.

Tags

Choose a tag for the predefined response.

Global for all CSQs : The predefined response is available to all the agents that are associated with all the CSQs.

Customize (Maximum 10 CSQs) : The predefined response is available only to the agents that are associated with the selected CSQs.

If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them.

Predefined responses can be used only for emails sent in HTML format and not plain text.

Step 4

Click Save .

The newly
                                                				added predefined response appears with the assigned tags in the List of
                                                   				  Predefined Responses .

You can sort
                                                				the predefined responses by title by clicking the Title header and by type by
                                                				clicking the Type header.

### Wrap-Up
                           	 Reasons

To access the
                              		Wrap-Up Reasons, choose Subsystems > Chat and Email > Wrap-Up Reasons .

Use the Wrap-Up
                                 		  Reasons page to configure and manage Wrap-Up categories and reasons
                              		for chat and email Contact Service Queues (CSQs). Use the Ellipsis (...) to
                              		view all the Wrap-Up Reasons that are added for each Wrap-Up category.

#### Wrap-Up
                              	 Reasons

Using this web
                                    		  page, you can add, modify, and delete the Wrap-Up Reasons.

You can add a
                                    		  maximum of 25 Wrap-Up categories. If you exceed the maximum number of
                                    		  categories, the Add
                                       			 New button is disabled.

Step 1

From the
                                             			 Unified CCX Administration menu bar, choose Subsystems > Chat and Email > Wrap-Up Reasons .

Step 2

Click the Add
                                                				New icon or the Add
                                                				New button that is displayed in the toolbar in the upper left
                                             			 corner of the window.

The Wrap-Up Reasons web page opens.

Step 3

Specify the
                                             			 following information:

Field

Description

Category

Specify the name for the Wrap-Up category. Allows up to 40 characters.

Wrap-Up Reasons

Enter the Wrap-Up Reasons for the specified category. Allows up to 40 characters. Click the Add button to add up to 25 Wrap-Up Reasons for each category.

Tags

Choose a tag for the Wrap-Up category.

You can associate a maximum of 10 Wrap-Up categories to a CSQ.

Global for all CSQs : The Wrap-Up reason is available to all the agents that are associated with all the CSQs.

Customize : The Wrap-Up reason is available only to the agents that are associated with the selected CSQs.

If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them.

Step 4

Click Save .

The newly
                                                				added Wrap-Up category appears with the assigned tags in the List of
                                                   				  Wrap-Up Reasons .

When you
                                                            				  reskill or modify a category, the logged in agents can apply Wrap-Up Reasons
                                                            				  from the updated list of categories for the new non-voice contacts only.

### Email
                           	 Signatures

To access the email
                              		signatures, choose Subsystems > Chat and
                                    			 Email > Email Signatures .

#### Email Signature
                              	 Configuration

Using this web
                                    		  page, you can add, modify, and delete email signatures.

To modify an existing email signature, click the Title header for the email signature that you want to modify. To delete an
                                                existing email signature, click the Delete icon for the email signature that you want to delete.

Step 1

From the
                                             			 Unified CCX Administration menu bar, choose Subsystems > Chat and
                                                   				  Email > Email Signatures .

The Email
                                                   				  Signature web page opens, displaying the list of existing email
                                                				signatures that are configured, if any.

Step 2

Click the Add
                                                				New icon that is displayed in the toolbar in the upper left corner
                                             			 of the window or the Add
                                                				New button that is displayed at the bottom of the window to create
                                             			 a new email signature.

The Email
                                                   				  Signature Configuration web page opens.

Step 3

Specify the
                                             			 following information:

Field

Description

Name

Unique name of the email signature.

The name can have a maximum of 100 characters.

Content

The email signature content.

The email signature can have a maximum of 1500 characters. You may format the text of the email signature content, add images,
                                                                        add URL to the email signature, and add the Agent alias information.

The Agent alias variable appears by default when any new email signature is created. If it is removed from the email signature
                                                                        it can be reinserted at the cursor location in the email signature by clicking on the Agent alias variable icon.

When there is no alias configured for an agent, the Agent ID is presented in the email signature by default.

Tags

Choose a tag for the email signature.

Global for all CSQs : The email signature is available to all the agents that are associated with all the CSQs.

Customize (Maximum 10 CSQs) : The email signature is available only to the agents that are associated with the selected CSQs.

If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them.

Only one (1) email signature can be tagged as Global for all CSQs.

A CSQ can be tagged with only one (1) email signature.

When an email is responded by an agent of a particular CSQ, the system will check if there is any email signature tagged
                                                                        for that CSQ. The different scenarios are:

If there is an email signature tagged to a CSQ, that will be appended in the email response.

If there is no CSQ specific email signature, the global signature is appended in the email response.

If there is no global email signature and no customized email signature tagged to the CSQ then there will be no email signature
                                                                              appended in the email response.

Step 4

Click Save .

The newly
                                                				added email signature appears with the assigned tags in the List of
                                                   				  Email Signatures .

You can sort
                                                				the email signatures by title by clicking the Title header and by type by
                                                				clicking the Type header.

### Channel
                           	 Parameters

Use the Channel
                                 		  Parameters web page to configure channel parameters.

Step 1

From the
                                          			 Unified CCX Administration menu bar, choose Subsystems > Chat > Channel
                                                				  Parameters OR Subsystems > Chat and
                                                				  Email > Channel Parameters as applicable.

The
                                             				Channel Parameters Configuration web page opens.

Step 2

Use this web
                                          			 page to specify or modify the following fields for channel parameters:

Field

Description

No
                                                         							 Answer Timeout (Seconds)

The
                                                         							 time for an agent to respond to the chat request after which, the chat request
                                                         							 is routed back to the chat queue and for the chat toaster to fade out.

This
                                                         							 is applicable for the Group Chat request also. However when the chat is not
                                                         							 accepted, the chat request is not routed back to the chat queue.

When you use Chrome or Firefox, the browser overrides the chat toaster
                                                                     								notification to fade out in 20 seconds, even if it is configured to a higher
                                                                     								value.

Join
                                                         							 Timeout (Minutes)

The
                                                         							 time after which the customer initiates a chat and, if an agent is not joined,
                                                         							 the customer gets a message as per the configuration in the Chat Web Form Configuration page. But an agent can
                                                         							 still join the chat after this timeout. The default timeout is one minute and
                                                         							 the maximum timeout value allowed is 60 minutes.

Inactivity Timeout (Minutes)

The
                                                         							 customer inactivity time after which, the system ends the chat. This timeout is
                                                         							 on the customer side only.

The
                                                         							 agent gets a message "You are alone in the chat room. Click End to close the chat
                                                            								interface." .

The
                                                         							 customer gets a message "Warning: the server connection was lost due to an inactivity
                                                            								timeout or connection failure." .

Inactivity timeout may also apply to contacts in queue that have
                                                         							 not yet been accepted by agents. This scenario occurs only when the Join
                                                         							 Timeout value is greater than the Inactivity Timeout value.

The customer then gets a message "Sorry, the chat service is currently not available. Please try
                                                            								again later."

Offer Chat Contact When On Voice Call

Click Yes if agents are allowed to handle a chat session during
                                                         							 a voice call.

This setting takes effect when the agent ends the current voice call.

Chats are presented to agents even when they go off-hook or busy in a Non ICD call.

Offer Voice Call When On Chat

Click Yes if agents are allowed to handle a voice call during a
                                                         							 chat session.

This setting takes effect when the agent receives a new incoming chat.

Direct/Consult Transfer to an IPCC extension is an exception. Even if agents are busy on a chat they would still get calls
                                                                     that are transferred to their extension directly.

Maximum Number Of Chat Sessions Per Agent

Number of chat sessions (ranging from 1 to 5) that an agent is allowed to
                                                         							 handle.

This includes the group chat sessions also.

This option is available only if Finesse service is activated. For Cisco Finesse Desktop, the value is set to 1.

Maximum Number Of Email Sessions Per Agent

Number of Email sessions (ranging from 1 to 5) that an agent is allowed to
                                                         							 handle.

Sticky Email Timeout (Hours)

Specify the amount of time for which an email message waits in a
                                                         							 specific agent CSQ.

Sticky email routing (Last-agent email routing) is a mechanism
                                                         							 to route an email message to the agent who handled the last leg of the email
                                                         							 conversation.

When
                                                         							 an email message, which is part of an ongoing conversation, comes in and the
                                                         							 agent who handled the last leg of the conversation is not available, then the
                                                         							 email does not wait indefinitely in that agent queue. After the configured time
                                                         							 expires, the email message is placed on the intended CSQ to be handled by any
                                                         							 available agent.

Last-agent email routing is not available if the customer changes the subject line of the email message.

Default = 4 hours, Range = 1 to 120 hours.

Step 3

Click Save to save the changes for the channel parameters.

If any of
                                                         				  the above parameters are changed during the call center operation, the updated
                                                         				  values are not applied to the existing contacts in the system. The changed
                                                         				  parameters will affect only the new contacts coming into the system.

### Chat
                           	 Widgets

Use the Chat Widgets section to configure the Bubble Chat widget and generate HTML code snippet that can be hosted on the customer website.

The Bubble Chat interface supports accessibility for the visually challenged. To use this feature, users must configure Job
                              Access With Speech (JAWS) and enable Accessibility mode in their system. When users navigate across UI elements by using the
                              keyboard, the screen reader announces the focused elements such as fields, buttons, icons, and the incoming messages.

Website developers must localize the accessibility messages of Bubble Chat to ensure that the announcements are in the appropriate
                                          language.

To access the Chat Widgets page, choose Subsystems > Chat and Email > Chat Widgets .

#### Chat Widgets Page

The Chat Widgets page lists the following information and options for each chat widget:

Field

Description

Name

Name of the chat widget.

Description

A brief description.

Post Chat Rating

Whether post chat rating is available for the chat.

Post chat rating can be configured for only bubble chat.

Code

Option to generate the web form code for the configured chat widget.

Delete

Option to delete the chat widget.

#### Chat Widget Configuration

You can add, modify, and delete chat widgets. You can select any one of the following calendars:

24 Hours X 7 Days

Custom Calendar, which has been configured by using the Calendar Management in Finesse desktop.

To modify an existing chat widget, click the chat widget name.

To delete an existing chat widget, click the delete icon. Ensure that the widget is removed from the customer website before
                                                   deleting the widget.

You can configure or modify the Bubble Chat widget.

##### Bubble Chat Widget

Step 1

From the Unified CCX Administration menu bar, choose Subsystems > Chat and Email > Chat Widgets .

The Chat Widgets web page opens, displaying the information for existing chat widgets.

During the widget configuration, live preview of the widget is possible.

Step 2

Click the Add New icon or the Add New button.

The Bubble Chat Configuration web page opens. The administrator can configure the messages and labels in any language.

Step 3

In the Widget Details area, specify the following information:

Field

Description

Name

Unique name of the chat widget.

Description

Chat widget description.

Step 4

Click Next .

Step 5

Specify the following information:

Field

Description

Font Family

Typeface

Font family used for the text in the Chat Web Form and chat window.

The default font family is Helvetica. You can change the font family by either selecting from the drop-down or entering a
                                                                        new name. If the selected font family is not available in the system where from the AppAdmin page is accessed, it will display
                                                                        an alert message. When you enter a new name, ensure that the correct spelling (case sensitive) is used. The system does not
                                                                        indicate if you enter an invalid name. Ensure that you use commonly available fonts so as to make it easy for the customers
                                                                        to view the information. Before proceeding, the administrator should ensure that the selected font family is applied on the
                                                                        Chat Web Form preview.

Chat Title

Text

Title text displayed on the Chat Web Form and Chat Bubble.

Text Color

Color of the title text.

Button

Text

Text displayed on the button of the Chat Web Form.

Color

Color of the button.

Text Color

Color of the text displayed on the button.

Message Color

Background color of the agent message in the chat window.

Text Color

Color of the agent message text.

Step 6

Click Next .

Step 7

Specify the following information:

Field

Description

Enable Post Chat Rating

If this checkbox is checked, post-chat rating will be available for the chat.

The Post Chat Rating column in the Chat Widgets page indicates whether post chat rating is available for a chat.

Label

Text asking the user to rate the chat experience.

Button Text

Text displayed on the button that is used to submit the rating.

Step 8

Click Next .

Step 9

In the User Form Fields area, specify the following information:

From Available Fields , select the desired fields and move it to Selected Fields .

To create new fields in addition to the list of available fields, click Add Custom Field , enter the name of the new custom field in the pop-up window and click OK . The new custom field appears in the list of Selected Fields .

Step 10

In the Add problem Statement CSQ mapping area, specify the following information:

In Problem Statement Caption , enter the label for the problem statement field.

Enter the problem statement for the Chat Web Form and map the problem statement with an existing chat CSQ from the CSQ List drop-down list.

To add more problem statements and associate them with a chat CSQ, click Add More . Click the delete icon for a problem statement to delete that problem statement.

Step 11

Click Next . The Chat Messages area appears.

Step 12

Specify the following information:

Field

Description

Initialization Messages

Widget Wait Message

Join Time-out Message

In Progress Messages

Text for Text Typing Box

Agent Joined Message

Agent Left Message

End Messages

Close Chat Confirmation Pop-up message

In the Negative Response and Positive Response text boxes, enter the text to be displayed on the pop-up window buttons that allows the user to either accept or reject the
                                                            chat closure.

Close Chat and Download Transcript Confirmation Pop-up Message

In the Negative Response and Positive Response text boxes, enter the text appears on the pop-up window buttons that allows the user to either accept or reject the transcript
                                                            download.

By default, the enableTranscriptDownload attribute is set to True in the generated chat widget HTML code snippet.

Error Messages

System Error Message

Message displayed to the customer when the chat service is not available to handle chat requests.

Connectivity Error Message

Message displayed to the customer when the chat is disconnected due to inactivity timeout or connection failure.

Step 13

Click Next . The Service Hours page appears.

Step 14

In Service Hours area, select one of the following options to configure the business hours.

Default (24 hours x 7 days)- Select this option if the contact center works 24 hours and 7 days in a week.

Select Calendar- Select this option to configure the business hours. Calendar drop-down is enabled for this selection.

Step 15

Select the desired calendar from the drop-down list and click the View link to preview the calendar details such as Business Hours , Custom Business Days , and Holidays .

Step 16

In the Messages area, specifiy the following:

Holiday

Message displayed on the bubble chat widget to inform the customer during a holiday.

Off Hours

Message displayed on the bubble chat widget to inform the customer during non-working hours.

Label

Heading text displayed on the bubble chat widget to inform the customer for the business hours details.

Step 17

In the Label for Days of Week area, specify a label for each day of the week.

Step 18

Click Finish .

Step 19

Click Save Code to File to save the generated code. Click Back to Chat Widgets to go to the main Chat Widgets page.

You can also generate the code from the main Chat Widgets page by clicking on the Code icon against the chat widget name. The generated code appears on a pop-up window. To save this code, click Save Code to File .

##### Integration of Chat Code into Customer Website

When you complete a chat widget configuration by clicking the Finish button, the code for the configured chat widget is generated. You can save this generated code by clicking Save Code to File . The code is saved in an HTML file. You can also generate the code from the main Chat Widgets page by clicking on the Code icon against the chat widget name.

For bubble chat, copy  or download the  HTML code snippet and insert it into the desired webpage of the customer's website.
                                    Use the function provided in the HTML code snippet as the event handler for an event such as “click”, etc., and use this event
                                    in an element, such as <button>, <a>, <p> etc. Invoking this event using the element will initiate the chat conversation.
                                    An example is shown in the HTML code snippet. If changes are made to the widget after deployment, there is no need to redeploy
                                    the HTML code snippet. The updated information is automatically fetched based on the widget ID and dynamically reflected for
                                    the next conversation.

In cases where the website is comprises more than one page, ongoing chats might get disconnected when the user navigates from
                                                one page to another.

###### Disable Bubble Chat Transcript Download

To disable the download option for Bubble Chat Transcript, you must set the enableTranscriptDownload attribute to False and then redeploy the HTML code snippet in customer website.

To change the attribute, download the generated widget code snippet, set the enableTranscriptDownload attribute to False, and save. Redeploy the chat widget HTML code snippet in customer website.

###### Localize Accessibility Messages

You can localize most of the messages by using Unified CCX Administration. However, some of the accessibility messages that
                                          are read by the screen reader on Bubble Chat interface have to be localized in the HTML code snippet. Download the generated
                                          chat widget HTML code snippet, and update the following strings:

```
//Please change the following accessibility messages to the required language:
var accesibilityMessageForCloseButton = 'close';
var accesibilityMessageForMinimizeButton = 'minimize';
var accesibilityMessageForRestoreButton = 'restore';
var accesibilityMessageToIndicateAgentTyping = 'Agent is typing';
var accesibilityMessageToIndicateMessageFromAgent = 'message from';
var accesibilityMessageToIndicateCustomerSentMessage = 'Sent message from';
var accesibilityMessageToSelectRating = 'Please press 1 to 5 key with 1 being lowest and 5 being highest';
```

Save and redeploy the chat widget HTML code snippet in customer website.

Customer must have configured JAWS and enabled Accessibility mode in their system to experience the accessibility feature.

### Chat - Facebook Messenger

#### Before you begin

Business entity must have a public Facebook page for their business.

The endpoints like, Cisco Customer Collaboration Platform or a reverse proxy, must have valid Certificate Authority signed SSL certificates as they are exposed publicly to the Internet.

A new Facebook App is created on the Messenger platform. For more information about creation of the Facebook App and Messenger
                                       setup see, https://developers.facebook.com/docs/messenger-platform .

Step 1

From the Unified CCX Administration menu bar, choose Subsystems > Chat and Email > Chat - Facebook Messenger .

Step 2

In Configure Token from Facebook , enter the Facebook Page Access Token . This access token is generated on the Facebook App page when the Facebook App is created.

Step 3

In HTTP Proxy , enable HTTP Proxy and provide valid values for the HTTP Proxy .

Step 4

Click Validate to ensure that the token is valid using HTTP Proxy (if provided).

Step 5

In Problem Statements and CSQ Mapping , enter Problem Statement Caption .

Step 6

Enter problem statement and select CSQ from the dropdown list. Click Add More to add problem statements and CSQs.

You can add a maximum number of three (3) problem statements.

Step 7

In Chat Messages , you can edit the existing messages as per your business requirement. The following table describes the messages that a Facebook
                                          Messenger user would see:

Section

Field

Description

Initialization Messages

Welcome Message

This message welcomes the user when a chat session is initiated. The user can select a problem statement from the list.

In Progress Messages

Wait Message

This message informs the user to wait until an agent joins the chat.

Join Timeout Message

This message informs the user to continue to wait or try again later.

End Messages

End Message

This message informs the user that the chat session has ended.

No Agent Available

This message informs the user that no agent is available.

Unsupported Content Message

This message informs the user that any attachments other than text formats are not supported.

Unknown Error

This message informs the user about any unknown internal error.

Inactivity Timeout Message

This message informs the user that the chat session has ended due to inactivity.

Step 8

In Post Chat Rating , you can enable Post Chat Rating so that customer can rate the chat experience on a scale of 1 (worst) to 5 (best). You can
                                          edit the existing messages as per your business requirement. The following table describes the messages that the Facebook
                                          Messenger user would see:

Section

Field

Description

Post Chat Rating

Rating Offer Message

This message informs the user that the chat experience can be rated. The user can select one of the ratings from 1 (worst)
                                                         to 5 (best).

Rating Completed Message

This message informs the user that the rating was sucessfully submitted.

Step 9

In Webhooks Update in Facebook , ensure that the Facebook Verification token and configured Callback URL are updated in the Facebook App.

If you have modified tokens, restart Customer Collaboration Platform Chat Gateway Service for the changes to take effect.

Step 10

In Enable Integration , check or uncheck the check box to enable or disable the integration of Facebook Messenger with Unified CCX respectively.

Step 11

Click Save to save settings.

### Teams

Choose Subsystems > Chat > Teams OR Subsystems > Chat and
                                       				Email > Teams as applicable from the Unified
                                 		  CCXAdministration menu bar to access this configuration area.

The team
                                             			 configuration for chat is the same as it is for voice.

## Outbound
                        	 Menu

Use the Outbound
                              		  Configuration web page or REST API to provision outbound dialing functionality
                              		  feature.

### General Configuration

Choose Subsystems > Outbound > General from the Cisco Unified CCX Administration menu bar to access the General
                                 		  Configuration web page.

Use this web page to add or modify Outbound dialing
                                 		  preferences.

### Campaign
                           	 Configuration

Choose Subsystems > Outbound > Campaigns from the Cisco Unified CCX
                                 		  Administration menu bar to access the Campaigns web page. You can create and
                                 		  schedule a campaign, modify the settings that apply to a campaign, and import a
                                 		  list of contacts (in bulk using a comma-separated plain text file with .txt or
                                 		  .csv extension) into the Unified CCX database for each campaign using this web
                                 		  page.

From the Direct Preview Campaign Configuration page, you
                                 		  can also create a schedule to automatically import contacts from a remote
                                 		  server using the Import Contacts option.

The Campaigns web page displays the following status in the Automatic Import column in the Campaigns List table for the listed campaigns:

Not Configured —Automatic Import of contacts is not configured.

Enable —Automatic Import of contacts is configured and Automatic Schedule is enabled.

Disable —Automatic Import of contacts is configured but Automatic Schedule is disabled.

You can
                                 		  define any one of the following two types for a campaign:

Agent-based -
                                       				If you select this campaign type, all the outbound calls will be handled by the
                                       				available agents.

IVR-based - In
                                       				this campaign type, the outbound calls will be handled by the IVR scripts.

#### Add New
                              	 Campaigns

To configure the properties
                                    		  for direct preview, progressive and predictive agent-based campaigns, for
                                    		  campaign name and description, callback settings, skill group selection, time
                                    		  range, dialing options, retry settings, and the dial settings, click Add
                                       			 New icon or button in the Campaigns web page.

#### Import
                              	 Contacts

To
                                    		  import contacts for a selected campaign, click the hyperlink for the required
                                    		  campaign under the Name column and click Import
                                       			 Contacts . This will open the Import Contacts window through which
                                    		  you can import contacts.

The Open
                                       			 Printable Report for this Campaign Configuration icon provides the
                                    		  information for the selected campaign in addition to call-specific information,
                                    		  which varies depending on the selected dialer type for outbound. Few of them
                                    		  are:

- Campaign Name

- Enabled - Yes or No

- Description

- Start Time of the campaign

- End Time of the campaign

- Contact Records Cache Size

- Remaining Contacts

#### Delete
                              	 Contacts

To
                                    		  ensure that a contact does not get called again for subsequent campaigns, you
                                    		  must delete the contact from all campaigns to which it belongs.

Click Delete
                                       			 All Contacts icon or button in the Campaign Configuration web page
                                    		  to delete all contacts of a particular campaign. Once you click Delete
                                       			 All Contacts , you will see a dialog box with the message "This campaign
                                       			 will be disabled and all its contacts will be permanently deleted.
                                       			 Continue?" with OK and Cancel buttons.

If you click OK , the Outbound subsystem checks whether the
                                    		  contacts are used in an active Outbound campaign. If the contacts are used as
                                    		  part of an active Outbound campaign, you will see the following alert message
                                    		  in the status bar at the top of the Campaign Configuration web page: "Campaign is active. Cannot remove contacts from an active campaign.
                                       			 Disable the campaign and try again." In such cases, disable the campaign
                                    		  first and then try deleting all contacts. Click Cancel if you do not want to delete all contacts
                                    		  for the specific campaign.

### Area Code Management

Use this page to manually add new area codes, update
                                 		  existing area codes, and to add international area codes.

#### Add New Area Code

The Area Codes Management page allows you to find, add,
                                    		  delete, and modify the mapping of area codes and time zones. The dialer uses
                                    		  the area code of a contact phone number to determine the time zone of the
                                    		  contact calling area.

### Configure SIP
                           	 Gateway

You can
                                 		  use the SIP Gateway Configuration web page to add or modify the parameters that
                                 		  enable the Outbound subsystem of Unified CCX to communicate with the SIP
                                 		  gateway. You can also update the parameters specific to Call Progress Analysis
                                 		  functionality of the gateway using this web page.

Call
                                 		  Progress Analysis is a feature of the SIP gateway by which it determines
                                 		  whether the outcome of a call is an answering machine, live voice, fax, or beep
                                 		  tone and so on. The SIP gateway performs call progressive analysis of the call
                                 		  and informs the outcome of the call to Unified CCX.

It is mandatory to configure the SIP Gateway used by the Outbound
                                             			 subsystem to place calls in case of IVR-based and agent-based progressive and
                                             			 predictive Outbound campaigns.

Follow
                                 		  this procedure to configure the SIP gateway parameters through Unified CCX
                                 		  Administration web interface:

Step 1

From the
                                          			 Unified CCXAdministration menu bar, choose Subsystems > Outbound > SIP Gateway
                                                				  Configuration .

The SIP
                                             				Gateway Configuration web page opens.

Step 2

Click Update to save the configuration changes.

The new SIP
                                             				gateway configuration is added to the Unified CCX system.

Step 3

Click Cancel to restore the default settings.

#### SIP Gateway
                              	 Configuration Web Page

The SIP Gateway
                                    		  Configuration web page.

Field

Description

Gateway Configuration

Gateway
                                                						Hostname/IP Address

The
                                                						HostName or IP Address of the SIP Gateway in the Unified CCX server, which will
                                                						be used by the Outbound subsystem to place calls for the predictive or
                                                						progressive campaigns.

Gateway Port

Destination port used by Unified CCX to communicate with SIP gateway. The default value is 5060.

Local CCX Port

Destination port to be used by SIP gateway to communicate with Unified CCX.

You cannot edit this field. Default value is as follows:

Fresh install: 5065

Upgrade: Previously configured value. If not configured, 5065 is displayed.

If you have configured a value other than 5065, you can restore to the default value by using the Restore Default button.

Local User Agent

This read-only field provides a description of the owner for this connection. The default value is Cisco-UCCX.

Transport(TCP/UDP)

The
                                                						protocol required to send SIP messages. You can select any one of the following
                                                						protocols:

TCP
                                                      							 - Transport Control Protocol or

UDP
                                                      							 - User Datagram Protocol

The
                                                						default value is UDP.

Call Progress Analysis
                                                   						  Configuration (displays the parameter name, parameter value, and suggested
                                                   						  value for the following fields)

Minimum
                                                						Silence Period (10-1000)

The
                                                						amount of time that the signal must be silent after speech detection to declare
                                                						a live voice (in milliseconds).

Default
                                                						= 375 milliseconds, Range = 10-1000 milliseconds

Analysis
                                                						Period (1000 - 10000)

Maximum
                                                						amount of time (from the moment the system first detects the speech) during
                                                						which analysis will be performed on the input audio.

Default
                                                						= 2500 milliseconds, Range = 1000-10000 milliseconds

Maximum
                                                						Time Analysis (1000-10000)

The
                                                						amount of time to wait when it is difficult for the dialer to determine voice
                                                						or answering machine.

Default
                                                						= 3000 milliseconds, Range = 1000-10000 milliseconds

Minimum
                                                						Valid Speech Time (50-500)

Amount of time that
                                                						the signal must be active before being declared speech. Anything less is
                                                						considered as a glitch.

Default
                                                						= 112 milliseconds, Range = 50-500 milliseconds

Maximum
                                                						Term Tone Analysis (1000-60000)

This is
                                                						the amount of time the gateway will look for a terminating beep once an
                                                						answering machine has been detected.

Default
                                                						= 15000 milliseconds, Range = 1000-60000 milliseconds

#### Dial Peer
                              	 Configuration for Outbound

Dial peer
                                 		configuration is required to transfer the outbound calls to the IVR ports and
                                 		agents in case of progressive and predictive outbound campaigns. The dial peer
                                 		maps to the CUCM trigger for IVR-based campaigns and to the agent extension for
                                 		agent-based campaigns.

When you configure
                                 		voice-network dial peers, the key commands that you must configure are the destination-pattern and session-target commands.

##### IVR

For IVR-based
                                    		  progressive and predictive campaigns, the destination-pattern command specifies the Unified CM
                                    		  Telephony Trigger associated with the IVR campaign. The session-target command specifies a destination address for
                                    		  the voice-network peer.

##### Agent

For agent-based
                                    		  progressive and predictive campaigns, the destination-pattern command specifies the agent extension.
                                    		  The session-target command specifies a destination address for
                                    		  the voice-network peer.

For Extend and Connect, the destination-pattern must specify the destination address of the CTI Remote Device (CTIRD). See the Cisco Unified TAPI Developers Guide for Cisco Unified Communications Manager at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/prod_installation_guides_list.html for more information on CTIRD.

##### Disable
                                    		  Hunting for Agent-Based Outbound Calls

When the agent
                                    		  does not answer a live voice call within the time limit configured for Outbound
                                    		  Call Timeout in General Configuration web page, then the call has to be
                                    		  dropped. If hunting is not disabled on the gateway, the call is not dropped and
                                    		  is forwarded to the agent extension.

The gateway
                                    		  receives a 403 forbidden error message and hunts for the "preference 2
                                       			 dial peer." The gateway forwards the call to the agent extension using the " preference 2
                                       			 dial peer." Hence, the call is seen on the agent desktop and the state of
                                    		  the agent is changed to Ready or Not Ready depending on the option selected for
                                    		  the Agent State after Ring No Answer field in System Parameters Configuration
                                    		  web page.

To disable hunting
                                    		  for the gateway, use no voice
                                       			 hunt 57 command (57 maps to 403 forbidden in SIP).

##### Translation of
                                    		  Phone Numbers

Unified CCX does not support the translation or modification of the phone number that it uses to dial out outbound calls.
                                    Any "voice translation rules" configured in the gateway that modifies the phone number are not supported. If the phone number is translated, then those
                                    calls are not treated as IVR or agent-based outbound calls. Any such calls cannot have all the functionality and capabilities
                                    of a normal IVR or agent-based outbound calls.

You can use either of the below two supported methods to modify a dialed number in the gateway:

To remove the initial digits of the phone number use forward-digits or digit-strip in the dial peer configuration.

To add a prefix to the phone number use prefix in the dial peer configuration.

## Database Menu

The Unified CCX system uses the Database subsystem of the
                              		  Unified CCX Engine to communicate with database servers, to obtain information
                              		  that can be relayed to callers or to make application decisions. The Database
                              		  subsystem enables the Unified CCX applications to obtain information from data
                              		  sources, which are databases configured to communicate with the Unified CCX
                              		  system.

The Database menu contains the following options, which are
                              		  explained below:

Datasource

Parameters

Drivers

### DataSource

Use the DataSources web page to add a new data source,
                                 		  display, modify, or delete existing datasources.

Choose Subsystems > Database > DataSource from the Cisco Unified CCX Administration menu bar to access the DataSources
                                 		  web page.

#### New DataSource

Follow this procedure from the DataSources web page to add a new DataSource:

Click 
                                             		  the Add New icon that displays in the toolbar in
                                             		  the upper left corner of the window or the button that displays at the bottom
                                             		  of the window to add a new data source.

The DataSource Configuration web page opens.

### Add New Database
                           	 Parameter

To add a
                                 		  new database parameter:

Choose Subsystems > Database > Parameter from the Unified CCX
                                          			 Administration menu bar.

The Parameters
                                             				web page displays. See Poll Database Connectivity to know more about how to update
                                             				parameter-related fields.

### Driver

Use the Driver List web page to upload new drivers, or to view and delete existing drivers.

### Add New Database
                           	 Driver

Follow
                                 		  this procedure to add a new jdbc driver:

Step 1

From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > Database > Drivers .

The Driver List web page opens up displaying a list of uploaded driver class filenames along with a Delete icon.

Step 2

Click the Add
                                             				New icon that displays in the toolbar in the upper left corner of
                                          			 the window or the Add
                                             				New button that displays at the bottom of the window to add a new
                                          			 driver class name.

The Driver
                                             				Management web page opens.

Step 3

Specify a valid
                                          			 JDBC driver jar file in the Driver File field or click Browse to locate the driver file.

The driver file
                                             				is validated before uploading.

Step 4

Choose the
                                          			 supported class name for the new driver from the Driver Class Name drop-down
                                          			 list box.

Step 5

Click Upload to save the new driver to the database.

Tip

For details on the compatible Enterprise database server version see, https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . Ensure that a valid JDBC driver version is used that is compatible with the Enterprise database server.

Contact your database vendor to know the appropriate JDBC driver versions that is compatible with your Enterprise database
                                                               server.

While uploading com.ibm.db2.jcc.DB2Driver, if your IBM DB2 deployment also requires a license Jar to be in the application's
                                                               classpath, upload the license Jar as a Custom Jar File using the procedure detailed in Specify Custom Classpath Entries . Then, restart the Unified CCX Engine on all nodes through the Unified CCX Serviceability.

## HTTP Menu

The Unified CCX system uses the HTTP subsystem of the Unified CCX Engine to add components to the Unified CCX Engine that
                              allow applications to be triggered in response to requests from a variety of web clients, including computers and IP phones.

HTTP/HTTPS triggers are available if your system has a license installed for one of the following Cisco product packages:
                              Unified IP IVR or Unified CCX Premium.

### HTTP Trigger Configuration

Use the HTTP Trigger Configuration web pages to display,
                                 		  add, modify, and delete existing HTTP triggers.

Choose Subsystems > HTTP from the Cisco Unified CCX Administration menu bar to access the HTTP Trigger
                                 		  Configuration web page.

### Add New HTTP Trigger

To add a new HTTP trigger:

Click 
                                          		  the Add New icon or button on the HTTP Trigger
                                          		  Configuration web page to access the HTTP Trigger Configuration web page.

To modify an existing trigger, click any hyperlink within
                                             		  the HTTP Trigger List table; the HTTP Trigger Configuration web page opens.

## eMail Menu

The
                              		  Unified CCX system uses the eMail subsystem of the Unified CCXEngine to
                              		  communicate with your email server and enable your applications to create and
                              		  send email. The email configuration identifies the default email address and
                              		  server to be used for sending email (including e-pages and faxes) and for
                              		  receiving acknowledgments.

Choose Subsystems > eMail from the Cisco Unified CCX
                              		  Administration menu bar to access the eMail Configuration web page. You must
                              		  configure email functionality so that Unified CCX scripts created with the
                              		  email steps will function correctly.

## Cisco Media

Choose Subsystems > Cisco
                                    				Media from the Unified CCXAdministration menu bar to
                              		  access the Cisco Media Termination Dialog Group Configuration web page.

The Unified CCX system uses the Media subsystem of the
                              		  Unified CCX Engine to configure Cisco Media Termination (CMT) dialog groups
                              		  that can be used to handle simple Dual-Tone Multi-Frequency (DTMF) based dialog
                              		  interactions with customers. A dialog group is a pool of dialog channels in
                              		  which each channel is used to perform dialog interactions with a caller.

To modify an existing CMT dialog group, click any hyperlink
                              		  within the trigger's summary table entry; the Cisco Media Termination Dialog
                              		  Group Configuration web page opens.

To add a new CMT dialog group, click the Add New icon or button
                              		  in the Cisco Media Termination Dialog Group Configuration web page. The Cisco
                              		  Media Termination Dialog Group Configuration web page opens.

## MRCP ASR Menu

The Unified CCX system uses the MRCP ASR (Automatic Speech
                              		  Recognition) subsystem to allow navigation through a menu of options by
                              		  speaking instead of pressing keys on a touch-tone telephone.

### MRCP ASR Provider

Choose Subsystems > MRCP
                                       				ASR > MRCP ASR Provider from the
                                 		  Cisco Unified CCX Administration menu bar to configure information about the
                                 		  vendor of your speech server, including the number of licenses, and the grammar
                                 		  type.

To modify an existing ASR Provider information, click any
                                 		  hyperlink within the provider's summary table entry; the ASR Provider
                                 		  Configuration web page opens.

To add a new ASR Provider information, click the Add New icon or button.

### MRCP ASR Servers

Choose Subsystems > MRCP
                                       				ASR > MRCP ASR Servers from the
                                 		  Cisco Unified CCX Administration menu bar to configure your speech server name,
                                 		  port location, and available languages.

You must have a MRCP ASR Provider defined before you can provision a
                                             			 MRCP ASR Server.

To modify an existing ASR Server, click any hyperlink within
                                 		  the server summary table entry; the ASR Server Configuration web page opens.

To add a new ASR Server, click 
                                 		  the Add New icon or button.

### MRCP ASR Dialog Groups

Use the MRCP ASR Dialog Group Configuration web page to
                                 		  display, add, modify, and delete information about MRCP ASR dialog control
                                 		  groups, which enable Unified CCX applications to use speech recognition.

Choose Subsystems > MRCP
                                       				ASR > MRCP ASR Dialog Groups from
                                 		  the Cisco Unified CCX Administration menu bar to configure the MRCP ASR dialog
                                 		  control groups.

You must have a MRCP ASR Provider defined before you can provision a
                                             			 MRCP ASR Group.

To modify an existing MRCP ASR Dialog Group, click any
                                 		  hyperlink within the group summary table entry; the MRCP ASR Dialog Control
                                 		  Group Configuration web page opens.

To add a new MRCP ASR Group, click 
                                 		  the Add New icon or button.

### MRCP TTS
                           	 Menu

The
                                 		  Unified CCX system uses the MRCP (Text-to-Speech) subsystem to convert plain
                                 		  text (UNICODE) into spoken words to provide a user with information or to
                                 		  prompt a user to respond to an action.

#### MRCP TTS
                              	 Providers

Use the
                                    		  MRCP TTS Provider Configuration web pages to display, add, modify, and delete
                                    		  information about your TTS Provider.

Choose Subsystems > MRCP
                                          				TTS > MRCP TTS Provider from the Cisco
                                    		  Unified CCX Administration menu bar to configure information about the vendor
                                    		  of your TTS system.

To
                                    		  modify an existing MRCP TTS Provider, click any hyperlink within the provider
                                    		  summary table entry; the MRCP TTS Provider Configuration web page opens.

#### MRCP TTS Servers

Use the MRCP TTS Server Configuration web page to display,
                                    		  add, modify, and delete the text-to-speech server name, port location, and
                                    		  available language.

To modify an existing MRCP TTS Server, click any hyperlink
                                    		  within the server summary table entry; the MRCP TTS Server Configuration web
                                    		  page opens.

To add a new MRCP TTS Server, click Add New icon or button in the MRCP TTS Server
                                    		  Configuration web page.

##### Related Topic

#### MRCP TTS Default Genders

Use the MRCP TTS Default Genders Configuration web page to
                                    		  display or modify the gender setting for each Locale. You can modify the
                                    		  default gender setting for the Locales specified during TTS Server provisioning
                                    		  using this page. Click the Update icon or button to save the changes.

##### Related Topic

| Note | Use of two(2) wildcard CTI Route Points that overlap with each
                                             			 other is not supported. For example, Route Point 1: 123XXXX and Route Point 2:
                                             			 1234XXX overlap with one another and is not supported. However, a wildcard CTI Route point can overlap with a full DID
                                             			 (best match pattern) that doesn't contain a wildcard. For example, Route Point
                                             			 1: 123XXXX and Route Point 2: 1234567 is supported. |
|---|---|

| Caution | It is important that you plan to perform this task during off peak
                                             			 hours to avoid hampering routine contact center operations. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > Cisco
                                                				  Unified CM Telephony > Data
                                                				  Synchronization . The Cisco Unified CM Telephony Data Synchronization page appears. |
|---|---|
| Step 2 | Choose the desired components by selecting the corresponding check box: Call Control Group(s) Trigger(s) CM Telephony User(s) SRTP |
| Step 3 | Click Data Check or Data Resync .
                                          					When you click Data Check or Data
                                             						Resync , a confirmation message dialog box appears prompting you
                                          					to either proceed or cancel. Click OK to continue. Note After you click OK in the confirmation message for Data Check or
                                                         							Data Resync, you are not allowed to cancel the process. | Note | After you click OK in the confirmation message for Data Check or
                                                         							Data Resync, you are not allowed to cancel the process. |
| Note | After you click OK in the confirmation message for Data Check or
                                                         							Data Resync, you are not allowed to cancel the process. |
| Step 4 | The Cisco Unified CM Telephony Data Synchronization web page continues to
                                          					update until the Data Check or Data Resync process is complete. On completion of
                                          					the Data Check or Data Resync process, the result is displayed in the same web
                                          					page in a tree structure. The result for each selected component is displayed in
                                          					collapsed format with a tick mark if no mismatch is found. Click the arrow that
                                          					is next to each selected component to expand and view the detailed results. If any mismatch is found in the elements of the selected component, the
                                             						results for those components are displayed automatically in an expanded
                                             						format. Note If you had multiple device pools (for Call Control Groups) in
                                                               									your older versions of Unified CCX setup, performing Data Resync
                                                               									after an upgrade merges all multiple device pools to a single
                                                               									default device pool. However, you can manually assign a
                                                               									different device pool to the Call Control Group if the default
                                                               									device pool is not the intended one. When you select SRTP and click Data Check , The status of secure JTAPI configuration for subsystems JTAPI and RmCm is displayed
                                                                     											under sections CM Telephony and RmCm respectively. In a HA setup, the status of devices and device profiles that are associated with the
                                                                     											primary RmCm user and the system-generated RmCm user is
                                                                     											displayed under subsections RmCm
                                                                        												Devices and RmCm Device
                                                                        												Profiles respectively. When you select SRTP and click Data
                                                                  									Resync , The secure JTAPI configuration for subsystems JTAPI and
                                                                     											RmCm are re-synchronized as per Unified CCX SRTP
                                                                     											configuration and the status is displayed in the
                                                                     											respective subsections. In a HA setup, if devices and device profiles do not match between the primary RmCm
                                                                     											user and system-generated RmCm user, the
                                                                     											system-generated RmCm user is synchronized with the
                                                                     											devices and device profiles that are configured for
                                                                     											primary RmCm user. | Note | If you had multiple device pools (for Call Control Groups) in
                                                               									your older versions of Unified CCX setup, performing Data Resync
                                                               									after an upgrade merges all multiple device pools to a single
                                                               									default device pool. However, you can manually assign a
                                                               									different device pool to the Call Control Group if the default
                                                               									device pool is not the intended one. When you select SRTP and click Data Check , The status of secure JTAPI configuration for subsystems JTAPI and RmCm is displayed
                                                                     											under sections CM Telephony and RmCm respectively. In a HA setup, the status of devices and device profiles that are associated with the
                                                                     											primary RmCm user and the system-generated RmCm user is
                                                                     											displayed under subsections RmCm
                                                                        												Devices and RmCm Device
                                                                        												Profiles respectively. When you select SRTP and click Data
                                                                  									Resync , The secure JTAPI configuration for subsystems JTAPI and
                                                                     											RmCm are re-synchronized as per Unified CCX SRTP
                                                                     											configuration and the status is displayed in the
                                                                     											respective subsections. In a HA setup, if devices and device profiles do not match between the primary RmCm
                                                                     											user and system-generated RmCm user, the
                                                                     											system-generated RmCm user is synchronized with the
                                                                     											devices and device profiles that are configured for
                                                                     											primary RmCm user. |
| Note | If you had multiple device pools (for Call Control Groups) in
                                                               									your older versions of Unified CCX setup, performing Data Resync
                                                               									after an upgrade merges all multiple device pools to a single
                                                               									default device pool. However, you can manually assign a
                                                               									different device pool to the Call Control Group if the default
                                                               									device pool is not the intended one. When you select SRTP and click Data Check , The status of secure JTAPI configuration for subsystems JTAPI and RmCm is displayed
                                                                     											under sections CM Telephony and RmCm respectively. In a HA setup, the status of devices and device profiles that are associated with the
                                                                     											primary RmCm user and the system-generated RmCm user is
                                                                     											displayed under subsections RmCm
                                                                        												Devices and RmCm Device
                                                                        												Profiles respectively. When you select SRTP and click Data
                                                                  									Resync , The secure JTAPI configuration for subsystems JTAPI and
                                                                     											RmCm are re-synchronized as per Unified CCX SRTP
                                                                     											configuration and the status is displayed in the
                                                                     											respective subsections. In a HA setup, if devices and device profiles do not match between the primary RmCm
                                                                     											user and system-generated RmCm user, the
                                                                     											system-generated RmCm user is synchronized with the
                                                                     											devices and device profiles that are configured for
                                                                     											primary RmCm user. |

| Note | After you click OK in the confirmation message for Data Check or
                                                         							Data Resync, you are not allowed to cancel the process. |
|---|---|

| Note | If you had multiple device pools (for Call Control Groups) in
                                                               									your older versions of Unified CCX setup, performing Data Resync
                                                               									after an upgrade merges all multiple device pools to a single
                                                               									default device pool. However, you can manually assign a
                                                               									different device pool to the Call Control Group if the default
                                                               									device pool is not the intended one. When you select SRTP and click Data Check , The status of secure JTAPI configuration for subsystems JTAPI and RmCm is displayed
                                                                     											under sections CM Telephony and RmCm respectively. In a HA setup, the status of devices and device profiles that are associated with the
                                                                     											primary RmCm user and the system-generated RmCm user is
                                                                     											displayed under subsections RmCm
                                                                        												Devices and RmCm Device
                                                                        												Profiles respectively. When you select SRTP and click Data
                                                                  									Resync , The secure JTAPI configuration for subsystems JTAPI and
                                                                     											RmCm are re-synchronized as per Unified CCX SRTP
                                                                     											configuration and the status is displayed in the
                                                                     											respective subsections. In a HA setup, if devices and device profiles do not match between the primary RmCm
                                                                     											user and system-generated RmCm user, the
                                                                     											system-generated RmCm user is synchronized with the
                                                                     											devices and device profiles that are configured for
                                                                     											primary RmCm user. |
|---|---|

| Click 
                                             			 the Add New icon that displays in the toolbar in
                                             			 the upper left corner of the window or the Add New button that displays at the bottom of
                                             			 the window to access the Skill Configuration area. |
|---|

| Click 
                                             			 the Open Printable Report of this Skill
                                                				Configuration icon to view a list of the resources associated with
                                             			 that skill. |
|---|

| Click 
                                             		  the Open Printable Report of this Resource
                                                			 Configuration icon to open a Resource Report for the agent. The
                                             		  Resource Report lists each agent resource ID, resource name, Unified CCX
                                             		  extension, resource group, automatic available status, skills, CSQs, and team. |
|---|

| Add a new Resource Groups by clicking Add New icon or button in the Resource Group
                                             		  area of the Unified CCX Configuration web page. |
|---|

| Click 
                                             		  the Open Printable Report of this Resource Group
                                                			 Configuration icon to view a list of the available resources for
                                             		  this resource group. |
|---|

| Note | When all the CSQs assigned to the teams associated to the Supervisor are deleted, the Advanced Supervisor Capability of Queue
                                             Management is removed for the Supervisor. |
|---|---|

| Step 1 | From the Unified CCX Administration menu, choose Tools > User Management > User View . The User Configuration page displays the list of all users. |
|---|---|
| Step 2 | Click the user to whom you want to assign supervisor capability. The User Configuration page displays information about that user. In the Capabilities section, the left pane displays the
                                                list of assigned capabilities and the right pane displays the list of capabilities. |
| Step 3 | Using the left arrow, assign Supervisor capability. |
| Step 4 | Click Update to save your changes. |

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Teams . |
|---|---|
| Step 2 | Click Add New icon that displays in the tool bar in the upper left corner of the window or the Add New button at the bottom of the window. The Team Configuration page appears. |
| Step 3 | Enter the Team Name . |
| Step 4 | Select the Primary Supervisor from the drop-down list. |
| Step 5 | (Optional) Select the secondary supervisor name from the Available Supervisors list and use the arrow icon to move it into the Secondary Supervisors list. |
| Step 6 | (Optional) To add an agent to this team, select an agent name in the Available Resources list and use the arrow icon to move it into the Assigned Resources list. |
| Step 7 | (Optional) Select the CSQ name in the Available CSQs list and use the arrow icon to move it into the Assigned CSQs list to add the CSQ to this team. |
| Step 8 | In the Team Settings section, specify the following information: Parameter Name Parameter Value Global Settings Change Agent State to Not Ready when Agent Busy on Non ACD Line Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                            lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings is available
                                                                  at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. Displays the global settings. Auto Answer Enables the incoming calls to be auto answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. Note To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. This functionality is applicable only for the agents and not for the supervisors of the team. | Parameter Name | Parameter Value | Global Settings | Change Agent State to Not Ready when Agent Busy on Non ACD Line | Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                            lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings is available
                                                                  at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Displays the global settings. | Auto Answer | Enables the incoming calls to be auto answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. |  | Note | To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. This functionality is applicable only for the agents and not for the supervisors of the team. |
| Parameter Name | Parameter Value | Global Settings |
| Change Agent State to Not Ready when Agent Busy on Non ACD Line | Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                            lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings is available
                                                                  at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Displays the global settings. |
| Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. |
| Auto Answer | Enables the incoming calls to be auto answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. |  |
| Note | To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. This functionality is applicable only for the agents and not for the supervisors of the team. |
| Step 9 | Click Save to apply changes or Cancel to exit. |

| Parameter Name | Parameter Value | Global Settings |
|---|---|---|
| Change Agent State to Not Ready when Agent Busy on Non ACD Line | Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                            lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings is available
                                                                  at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Displays the global settings. |
| Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. |
| Auto Answer | Enables the incoming calls to be auto answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. |  |

| Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. |
|---|---|

| Note | To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. This functionality is applicable only for the agents and not for the supervisors of the team. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Teams . |
|---|---|
| Step 2 | Click a name in the Team Name column. The Team Configuration page appears. |
| Step 3 | Select the Primary Supervisor from the drop-down list. |
| Step 4 | (Optional) Select the secondary supervisor name from the Available Supervisors list and use the arrow icon to move it into the Secondary Supervisors list. To remove the secondary supervisor name from this team, select the supervisor name in the Secondary Supervisors list and use the arrow icon to move it into the Available Supervisors list. This supervisor now belongs to the default team. |
| Step 5 | (Optional) Select an agent name in the Available Resources list and use the arrow icon to move it into the Assigned Resources list to add an agent to this team. To remove an agent from this team, select an agent name in the Assigned Resources list and use the arrow icon to move it into the Available Resources list. This agent now belongs to the default team. |
| Step 6 | (Optional) Select the CSQ name in the Available CSQs list and use the arrow icon to move it into the Assigned CSQs list to add the CSQ to this team. To remove a CSQ from this team, select a CSQ name in the Assigned CSQs list and use the arrow icon to move it into the Available CSQs list. This CSQ now belongs to the default team. |
| Step 7 | In the Team Settings section, specify the following information: Parameter Name Parameter Value Global Settings Change Agent State to Not Ready when Agent Busy on Non ACD Line Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                            lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings are available
                                                                  at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. Displays the global settings. Auto Answer Enables the incoming calls to be automatically answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. Note To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. | Parameter Name | Parameter Value | Global Settings | Change Agent State to Not Ready when Agent Busy on Non ACD Line | Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                            lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings are available
                                                                  at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Displays the global settings. | Auto Answer | Enables the incoming calls to be automatically answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. |  | Note | To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. |
| Parameter Name | Parameter Value | Global Settings |
| Change Agent State to Not Ready when Agent Busy on Non ACD Line | Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                            lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings are available
                                                                  at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Displays the global settings. |
| Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. |
| Auto Answer | Enables the incoming calls to be automatically answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. |  |
| Note | To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. |
| Step 8 | Click Save or Update to apply changes, Cancel to exit or Delete to delete this team. |

| Parameter Name | Parameter Value | Global Settings |
|---|---|---|
| Change Agent State to Not Ready when Agent Busy on Non ACD Line | Radio button that enables the agent state to change from the Ready state to the Not Ready state when the monitored Non ACD
                                                            lines are used for Incoming or Outgoing calls. The options are: Enable—Enables the state change of the agent in the team. Disable (default)—Disables any state change of the agent in the team. Allow team settings to override global settings—A check box to override the global settings. The global settings are available
                                                                  at System > System Parameters > Agent Settings . Note When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. | Displays the global settings. |
| Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. |
| Auto Answer | Enables the incoming calls to be automatically answered. The options are: Enable with Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. A zip tone plays to alert the agent. Enable without Zip tone—For agents, belonging to the team, all the incoming calls to the IPCC extension is auto answered provided
                                                                  the agent is in the Ready state in the Cisco Finesse desktop. The zip tone does not play to alert the agent. Disable (Default)—Auto answer is not enabled. |  |

| Note | When you select the check box, a popup message reminds you that your team settings are different from the global settings.
                                                                        Click OK to proceed or Cancel to discard the changes. When you click OK, the team level settings override the global settings. |
|---|---|

| Note | To configure Change Agent State to Not Ready when Agent Busy on Non ACD Line at a team level, you must install UCCX 12.5(1) SU1 ES01. |
|---|---|

| Step 1 | From the Unified CCXAdministration menu bar, choose Subsystems > RmCm > Teams . The Teams web page opens. |
|---|---|
| Step 2 | Click 
                                             			 the Delete icon beside the Team Name icon you want to
                                             			 delete. The system prompts you to confirm the delete. |
| Step 3 | Click OK . |

| Important | The Chat option is available with Premium license package when Cisco Finesse is not activated. The Chat and Email option is available with Premium license package when you activate Cisco Finesse. |
|---|---|

| Note | On a high availability setup, after the Add to Cluster operation is successful, the following message is displayed: In case of HA, configure the CCP on secondary node after adding to cluster in the secondary node. |
|---|---|

| Step 1 | From the Unified CCX Administration menu bar, choose Subsystems > Chat and Email > CCP Configuration as applicable. The Configuration web page appears. Note You must perform the following actions: In the Unified CCX, upload Customer Collaboration Platform certificate to the Unified CCX Tomcat trust store using the Cisco Unified OS Administration interface. You can also use the set cert import trust tomcat CLI. In the Customer Collaboration Platform, upload Unified CCX certificate to the Customer Collaboration Platform Tomcat trust
                                                               store using the Cisco Unified OS Administration interface. Unified CCX and Customer Collaboration Platform servers must have DNS entries. Customer Collaboration Platform must be accessible to Unified CCX by hostname. If the entries are not valid, an error is displayed. | Note | You must perform the following actions: In the Unified CCX, upload Customer Collaboration Platform certificate to the Unified CCX Tomcat trust store using the Cisco Unified OS Administration interface. You can also use the set cert import trust tomcat CLI. In the Customer Collaboration Platform, upload Unified CCX certificate to the Customer Collaboration Platform Tomcat trust
                                                               store using the Cisco Unified OS Administration interface. Unified CCX and Customer Collaboration Platform servers must have DNS entries. Customer Collaboration Platform must be accessible to Unified CCX by hostname. If the entries are not valid, an error is displayed. |
|---|---|---|---|
| Note | You must perform the following actions: In the Unified CCX, upload Customer Collaboration Platform certificate to the Unified CCX Tomcat trust store using the Cisco Unified OS Administration interface. You can also use the set cert import trust tomcat CLI. In the Customer Collaboration Platform, upload Unified CCX certificate to the Customer Collaboration Platform Tomcat trust
                                                               store using the Cisco Unified OS Administration interface. Unified CCX and Customer Collaboration Platform servers must have DNS entries. Customer Collaboration Platform must be accessible to Unified CCX by hostname. If the entries are not valid, an error is displayed. |
| Step 2 | Specify the following fields for Customer Collaboration Platform : Field Description IP Address / Host Name IP address or fully qualified domain name of the Customer Collaboration Platform server. For example, 192.168.1.5 or host.example.com. User Name Username of the Customer Collaboration Platform administrator. Password Password of the Customer Collaboration Platform administrator. Note When the Customer Collaboration Platform application password is reset, ensure that the new password is first updated in Unified CCX and then reset the password in Customer Collaboration Platform . This prevents the account getting locked due to the authentication attempts from Unified CCX with old password. | Field | Description | IP Address / Host Name | IP address or fully qualified domain name of the Customer Collaboration Platform server. For example, 192.168.1.5 or host.example.com. | User Name | Username of the Customer Collaboration Platform administrator. | Password | Password of the Customer Collaboration Platform administrator. | Note | When the Customer Collaboration Platform application password is reset, ensure that the new password is first updated in Unified CCX and then reset the password in Customer Collaboration Platform . This prevents the account getting locked due to the authentication attempts from Unified CCX with old password. |
| Field | Description |
| IP Address / Host Name | IP address or fully qualified domain name of the Customer Collaboration Platform server. For example, 192.168.1.5 or host.example.com. |
| User Name | Username of the Customer Collaboration Platform administrator. |
| Password | Password of the Customer Collaboration Platform administrator. |
| Note | When the Customer Collaboration Platform application password is reset, ensure that the new password is first updated in Unified CCX and then reset the password in Customer Collaboration Platform . This prevents the account getting locked due to the authentication attempts from Unified CCX with old password. |
| Step 3 | Click Save to save the changes. Note After saving a valid Customer Collaboration Platform configuration, you cannot change the IP Address / Host Name details. If you want to change the configuration, delete the existing configuration and create a new one. If you see an error message, click Save to re-create feeds, campaigns, and notifications for chat and email in Customer Collaboration Platform . When Unified CCX hostname is changed or when a new Unified CCX node is added, the Customer Collaboration Platform Configurations must be saved again. This enables the change to take effect to re-create all the notifications for email and
                                                               chat in Customer Collaboration Platform . | Note | After saving a valid Customer Collaboration Platform configuration, you cannot change the IP Address / Host Name details. If you want to change the configuration, delete the existing configuration and create a new one. If you see an error message, click Save to re-create feeds, campaigns, and notifications for chat and email in Customer Collaboration Platform . When Unified CCX hostname is changed or when a new Unified CCX node is added, the Customer Collaboration Platform Configurations must be saved again. This enables the change to take effect to re-create all the notifications for email and
                                                               chat in Customer Collaboration Platform . |
| Note | After saving a valid Customer Collaboration Platform configuration, you cannot change the IP Address / Host Name details. If you want to change the configuration, delete the existing configuration and create a new one. If you see an error message, click Save to re-create feeds, campaigns, and notifications for chat and email in Customer Collaboration Platform . When Unified CCX hostname is changed or when a new Unified CCX node is added, the Customer Collaboration Platform Configurations must be saved again. This enables the change to take effect to re-create all the notifications for email and
                                                               chat in Customer Collaboration Platform . |

| Note | You must perform the following actions: In the Unified CCX, upload Customer Collaboration Platform certificate to the Unified CCX Tomcat trust store using the Cisco Unified OS Administration interface. You can also use the set cert import trust tomcat CLI. In the Customer Collaboration Platform, upload Unified CCX certificate to the Customer Collaboration Platform Tomcat trust
                                                               store using the Cisco Unified OS Administration interface. Unified CCX and Customer Collaboration Platform servers must have DNS entries. Customer Collaboration Platform must be accessible to Unified CCX by hostname. If the entries are not valid, an error is displayed. |
|---|---|

| Field | Description |
|---|---|
| IP Address / Host Name | IP address or fully qualified domain name of the Customer Collaboration Platform server. For example, 192.168.1.5 or host.example.com. |
| User Name | Username of the Customer Collaboration Platform administrator. |
| Password | Password of the Customer Collaboration Platform administrator. |

| Note | When the Customer Collaboration Platform application password is reset, ensure that the new password is first updated in Unified CCX and then reset the password in Customer Collaboration Platform . This prevents the account getting locked due to the authentication attempts from Unified CCX with old password. |
|---|---|

| Note | After saving a valid Customer Collaboration Platform configuration, you cannot change the IP Address / Host Name details. If you want to change the configuration, delete the existing configuration and create a new one. If you see an error message, click Save to re-create feeds, campaigns, and notifications for chat and email in Customer Collaboration Platform . When Unified CCX hostname is changed or when a new Unified CCX node is added, the Customer Collaboration Platform Configurations must be saved again. This enables the change to take effect to re-create all the notifications for email and
                                                               chat in Customer Collaboration Platform . |
|---|---|

| Important | Ensure that the Customer Collaboration Platform configuration delete operation is performed during maintenance window. Ensure that the Customer Collaboration Platform configuration hostname is deleted manually from Desktop Layout in Cisco Finesse Administration. |
|---|---|

| Step 1 | On the Customer Collaboration Platform Configuration page, click Delete . A confirmation dialog box appears. |
|---|---|
| Step 2 | Click OK to delete the Customer Collaboration Platform configuration. This deletes the Customer Collaboration Platform configuration data from the Unified CCX configuration database. In addition, it deletes the configurations such as Feeds,
                                                Campaigns, Notifications, and Webhooks (that were created by Unified CCX) from the Customer Collaboration Platform application. Note If you select Delete all Associated Chat and Email CSQs check box in the confirmation dialog box, all the chat and email CSQs are also deleted from the Unified CCX configuration
                                                            database. Result: When the Customer Collaboration Platform configuration is deleted from both Unified CCX and Customer Collaboration Platform application, the following message is displayed: CCP configuration has been deleted successfully. However, due to connectivity issues, if the Customer Collaboration Platform configuration is deleted in Unified CCX but not deleted in Customer Collaboration Platform application, the following message is displayed: CCP configuration has been deleted successfully from UCCX. Ensure that the related configurations are deleted manually from
                                                the the CCP application as well. | Note | If you select Delete all Associated Chat and Email CSQs check box in the confirmation dialog box, all the chat and email CSQs are also deleted from the Unified CCX configuration
                                                            database. |
| Note | If you select Delete all Associated Chat and Email CSQs check box in the confirmation dialog box, all the chat and email CSQs are also deleted from the Unified CCX configuration
                                                            database. |
| Step 3 | Restart the Unified CCX engine on both the nodes. |
| Step 4 | Click Cancel to cancel this operation. |

| Note | If you select Delete all Associated Chat and Email CSQs check box in the confirmation dialog box, all the chat and email CSQs are also deleted from the Unified CCX configuration
                                                            database. |
|---|---|

| Note | The latest 200 unread or reserved, social email contacts across the email CSQs are reinjected. |
|---|---|

| To reinject the email contacts back to Unified CCX, click Subsystems > Chat and Email CCP Configuration > Reinject . Note The CCP Configuration web page is reloaded, but the configuration is not updated. | Note | The CCP Configuration web page is reloaded, but the configuration is not updated. |
|---|---|---|
| Note | The CCP Configuration web page is reloaded, but the configuration is not updated. |

| Note | The CCP Configuration web page is reloaded, but the configuration is not updated. |
|---|---|

| Note | Microsoft Office 365 option is available from 12.5(1)SU2 ES03 onwards. |
|---|---|

| Step 1 | From the
                                          			 Unified CCX Administration menu bar, choose Subsystems > Chat and
                                                				  Email > Mail Server Configuration . The Mail
                                             				Server Configuration web page opens. |
|---|---|
| Step 2 | Complete or
                                          			 modify the following fields for the mail server: Field Description Mail
                                                         							 Server Settings Mail
                                                         							 Server Choose the mail server that is required to be configured from the listed options: MS Exchange Server / Office 365 Gmail Note You must not perform any automatic or manual operations on the emails from the mail server. For example, create rules, move
                                                                  the emails manually to a different location, delete emails from the mail server, and so on. Unified CCX must be connected to a dedicated mail server. Ensure that the email account is not shared. IMAP
                                                         							 Folder Structure Sent
                                                         							 Items Folder Name The name of the sent items folder of the respective mail server that is configured. Note All the listed mail servers have the default folder names prepopulated for all the IMAP folders in English locale. These folder
                                                                  names can be edited and can have custom values. Incoming (Secure IMAP) Host
                                                         							 Name Fully qualified domain name (FQDN) of the incoming (IMAP)
                                                         							 server. Do not enter the IP address. Port Number Port
                                                         							 number that is used to connect to the IMAP server. The
                                                         							 default port number is 993. Outgoing (Secure SMTP) Host Name FQDN of the outgoing (SMTP) server. Do not enter the IP address. Port
                                                         							 Number Port number that is used to connect to the SMTP server. The
                                                         							 default port number is 587. Proxy Settings HTTP Choose the Enable or Disable radio button to use HTTP proxy for Mail Server connectivity. By default the Disable option is selected and Enable option is disabled. To enable HTTP , configure Http in Proxy Parameters section of System Parameters page. Note If Customer Collaboration Platform is able to access internet directly, HTTP proxy configuration is not required. Else, HTTP
                                                                  proxy configuration is required to invoke cloud services of mail servers (Gmail) to get the OAuth token. The OAuth token is
                                                                  used in SMTP/IMAP operations. SOCKS Choose the Enable or Disable radio button to use socks proxy for Mail Server connectivity. By default the Disable option is selected and Enable option is disabled. To enable SOCKS , configure SOCKS Proxy in System Parameters page. Description Description of the mail server. | Field | Description | Mail
                                                         							 Server Settings | Mail
                                                         							 Server | Choose the mail server that is required to be configured from the listed options: MS Exchange Server / Office 365 Gmail Note You must not perform any automatic or manual operations on the emails from the mail server. For example, create rules, move
                                                                  the emails manually to a different location, delete emails from the mail server, and so on. Unified CCX must be connected to a dedicated mail server. Ensure that the email account is not shared. | Note | You must not perform any automatic or manual operations on the emails from the mail server. For example, create rules, move
                                                                  the emails manually to a different location, delete emails from the mail server, and so on. Unified CCX must be connected to a dedicated mail server. Ensure that the email account is not shared. | IMAP
                                                         							 Folder Structure | Sent
                                                         							 Items Folder Name | The name of the sent items folder of the respective mail server that is configured. Note All the listed mail servers have the default folder names prepopulated for all the IMAP folders in English locale. These folder
                                                                  names can be edited and can have custom values. | Note | All the listed mail servers have the default folder names prepopulated for all the IMAP folders in English locale. These folder
                                                                  names can be edited and can have custom values. | Incoming (Secure IMAP) | Host
                                                         							 Name | Fully qualified domain name (FQDN) of the incoming (IMAP)
                                                         							 server. Do not enter the IP address. | Port Number | Port
                                                         							 number that is used to connect to the IMAP server. The
                                                         							 default port number is 993. | Outgoing (Secure SMTP) | Host Name | FQDN of the outgoing (SMTP) server. Do not enter the IP address. | Port
                                                         							 Number | Port number that is used to connect to the SMTP server. The
                                                         							 default port number is 587. | Proxy Settings | HTTP | Choose the Enable or Disable radio button to use HTTP proxy for Mail Server connectivity. By default the Disable option is selected and Enable option is disabled. To enable HTTP , configure Http in Proxy Parameters section of System Parameters page. Note If Customer Collaboration Platform is able to access internet directly, HTTP proxy configuration is not required. Else, HTTP
                                                                  proxy configuration is required to invoke cloud services of mail servers (Gmail) to get the OAuth token. The OAuth token is
                                                                  used in SMTP/IMAP operations. | Note | If Customer Collaboration Platform is able to access internet directly, HTTP proxy configuration is not required. Else, HTTP
                                                                  proxy configuration is required to invoke cloud services of mail servers (Gmail) to get the OAuth token. The OAuth token is
                                                                  used in SMTP/IMAP operations. | SOCKS | Choose the Enable or Disable radio button to use socks proxy for Mail Server connectivity. By default the Disable option is selected and Enable option is disabled. To enable SOCKS , configure SOCKS Proxy in System Parameters page. | Description | Description of the mail server. |
| Field | Description |
| Mail
                                                         							 Server Settings |
| Mail
                                                         							 Server | Choose the mail server that is required to be configured from the listed options: MS Exchange Server / Office 365 Gmail Note You must not perform any automatic or manual operations on the emails from the mail server. For example, create rules, move
                                                                  the emails manually to a different location, delete emails from the mail server, and so on. Unified CCX must be connected to a dedicated mail server. Ensure that the email account is not shared. | Note | You must not perform any automatic or manual operations on the emails from the mail server. For example, create rules, move
                                                                  the emails manually to a different location, delete emails from the mail server, and so on. Unified CCX must be connected to a dedicated mail server. Ensure that the email account is not shared. |
| Note | You must not perform any automatic or manual operations on the emails from the mail server. For example, create rules, move
                                                                  the emails manually to a different location, delete emails from the mail server, and so on. Unified CCX must be connected to a dedicated mail server. Ensure that the email account is not shared. |
| IMAP
                                                         							 Folder Structure |
| Sent
                                                         							 Items Folder Name | The name of the sent items folder of the respective mail server that is configured. Note All the listed mail servers have the default folder names prepopulated for all the IMAP folders in English locale. These folder
                                                                  names can be edited and can have custom values. | Note | All the listed mail servers have the default folder names prepopulated for all the IMAP folders in English locale. These folder
                                                                  names can be edited and can have custom values. |
| Note | All the listed mail servers have the default folder names prepopulated for all the IMAP folders in English locale. These folder
                                                                  names can be edited and can have custom values. |
| Incoming (Secure IMAP) |
| Host
                                                         							 Name | Fully qualified domain name (FQDN) of the incoming (IMAP)
                                                         							 server. Do not enter the IP address. |
| Port Number | Port
                                                         							 number that is used to connect to the IMAP server. The
                                                         							 default port number is 993. |
| Outgoing (Secure SMTP) |
| Host Name | FQDN of the outgoing (SMTP) server. Do not enter the IP address. |
| Port
                                                         							 Number | Port number that is used to connect to the SMTP server. The
                                                         							 default port number is 587. |
| Proxy Settings |
| HTTP | Choose the Enable or Disable radio button to use HTTP proxy for Mail Server connectivity. By default the Disable option is selected and Enable option is disabled. To enable HTTP , configure Http in Proxy Parameters section of System Parameters page. Note If Customer Collaboration Platform is able to access internet directly, HTTP proxy configuration is not required. Else, HTTP
                                                                  proxy configuration is required to invoke cloud services of mail servers (Gmail) to get the OAuth token. The OAuth token is
                                                                  used in SMTP/IMAP operations. | Note | If Customer Collaboration Platform is able to access internet directly, HTTP proxy configuration is not required. Else, HTTP
                                                                  proxy configuration is required to invoke cloud services of mail servers (Gmail) to get the OAuth token. The OAuth token is
                                                                  used in SMTP/IMAP operations. |
| Note | If Customer Collaboration Platform is able to access internet directly, HTTP proxy configuration is not required. Else, HTTP
                                                                  proxy configuration is required to invoke cloud services of mail servers (Gmail) to get the OAuth token. The OAuth token is
                                                                  used in SMTP/IMAP operations. |
| SOCKS | Choose the Enable or Disable radio button to use socks proxy for Mail Server connectivity. By default the Disable option is selected and Enable option is disabled. To enable SOCKS , configure SOCKS Proxy in System Parameters page. |
| Description | Description of the mail server. |
| Step 3 | Click Update to save the changes. |

| Field | Description |
|---|---|
| Mail
                                                         							 Server Settings |
| Mail
                                                         							 Server | Choose the mail server that is required to be configured from the listed options: MS Exchange Server / Office 365 Gmail Note You must not perform any automatic or manual operations on the emails from the mail server. For example, create rules, move
                                                                  the emails manually to a different location, delete emails from the mail server, and so on. Unified CCX must be connected to a dedicated mail server. Ensure that the email account is not shared. | Note | You must not perform any automatic or manual operations on the emails from the mail server. For example, create rules, move
                                                                  the emails manually to a different location, delete emails from the mail server, and so on. Unified CCX must be connected to a dedicated mail server. Ensure that the email account is not shared. |
| Note | You must not perform any automatic or manual operations on the emails from the mail server. For example, create rules, move
                                                                  the emails manually to a different location, delete emails from the mail server, and so on. Unified CCX must be connected to a dedicated mail server. Ensure that the email account is not shared. |
| IMAP
                                                         							 Folder Structure |
| Sent
                                                         							 Items Folder Name | The name of the sent items folder of the respective mail server that is configured. Note All the listed mail servers have the default folder names prepopulated for all the IMAP folders in English locale. These folder
                                                                  names can be edited and can have custom values. | Note | All the listed mail servers have the default folder names prepopulated for all the IMAP folders in English locale. These folder
                                                                  names can be edited and can have custom values. |
| Note | All the listed mail servers have the default folder names prepopulated for all the IMAP folders in English locale. These folder
                                                                  names can be edited and can have custom values. |
| Incoming (Secure IMAP) |
| Host
                                                         							 Name | Fully qualified domain name (FQDN) of the incoming (IMAP)
                                                         							 server. Do not enter the IP address. |
| Port Number | Port
                                                         							 number that is used to connect to the IMAP server. The
                                                         							 default port number is 993. |
| Outgoing (Secure SMTP) |
| Host Name | FQDN of the outgoing (SMTP) server. Do not enter the IP address. |
| Port
                                                         							 Number | Port number that is used to connect to the SMTP server. The
                                                         							 default port number is 587. |
| Proxy Settings |
| HTTP | Choose the Enable or Disable radio button to use HTTP proxy for Mail Server connectivity. By default the Disable option is selected and Enable option is disabled. To enable HTTP , configure Http in Proxy Parameters section of System Parameters page. Note If Customer Collaboration Platform is able to access internet directly, HTTP proxy configuration is not required. Else, HTTP
                                                                  proxy configuration is required to invoke cloud services of mail servers (Gmail) to get the OAuth token. The OAuth token is
                                                                  used in SMTP/IMAP operations. | Note | If Customer Collaboration Platform is able to access internet directly, HTTP proxy configuration is not required. Else, HTTP
                                                                  proxy configuration is required to invoke cloud services of mail servers (Gmail) to get the OAuth token. The OAuth token is
                                                                  used in SMTP/IMAP operations. |
| Note | If Customer Collaboration Platform is able to access internet directly, HTTP proxy configuration is not required. Else, HTTP
                                                                  proxy configuration is required to invoke cloud services of mail servers (Gmail) to get the OAuth token. The OAuth token is
                                                                  used in SMTP/IMAP operations. |
| SOCKS | Choose the Enable or Disable radio button to use socks proxy for Mail Server connectivity. By default the Disable option is selected and Enable option is disabled. To enable SOCKS , configure SOCKS Proxy in System Parameters page. |
| Description | Description of the mail server. |

| Note | You must not perform any automatic or manual operations on the emails from the mail server. For example, create rules, move
                                                                  the emails manually to a different location, delete emails from the mail server, and so on. Unified CCX must be connected to a dedicated mail server. Ensure that the email account is not shared. |
|---|---|

| Note | All the listed mail servers have the default folder names prepopulated for all the IMAP folders in English locale. These folder
                                                                  names can be edited and can have custom values. |
|---|---|

| Note | If Customer Collaboration Platform is able to access internet directly, HTTP proxy configuration is not required. Else, HTTP
                                                                  proxy configuration is required to invoke cloud services of mail servers (Gmail) to get the OAuth token. The OAuth token is
                                                                  used in SMTP/IMAP operations. |
|---|---|

| Note | Microsoft Office 365 option is available from 12.5(1)SU2 ES03 onwards. To change the Microsoft Office 365 authentication from Basic to OAuth 2.0 , update the mail server selection to Microsoft Office 365, and then edit the email CSQ where the OAuth details must be filled. |
|---|---|

| Step 1 | From the Unified CCX Administration menu bar, choose Subsystems > Chat and Email > Contact Service Queues as applicable. The Contact Service Queues (CSQs) web page opens and displays the information for existing chat and email CSQs if any. |
|---|---|
| Step 2 | To add a new chat or email CSQ, click the Add New icon that appears in the toolbar in the upper left corner of the window or the Add New button that appears at the bottom of the window. The Contact Service Queue Configuration web page opens. |
| Step 3 | Specify the
                                          			 following fields: Field Name Description CSQ
                                                         							 Name Name
                                                         							 for the CSQ. Resource Selection Criteria Resource selection criteria chosen for the chat CSQ. Longest Available —Selects the agent who has been in the Available state for the longest amount of time. Most Skilled —Used for expert agent chat distribution. Selects the agent with the highest total competency level. The total competency
                                                               level is determined by adding the agent's competency levels for each assigned skill that is also assigned to the CSQ. Example 1: If Agent1 is assigned Skill1(5), Skill2(6), and Skill3(7) and CSQ1 specifies Skill1(min=1) and Skill3(min=1), the
                                                                     total competency level for Agent1 for CSQ1 is 12. Example 2: If Agent1 is assigned Skill1(5) and Skill2(6), and Skill3(7) and CSQ1 specifies Skill1(min=1), only, the total
                                                                     competency level for Agent1 for CSQ1 is 5. Note To change the competence level for an already configured agent, change the agent skill level and save the CSQ. If two agents score equal in the primary selection criteria, the agent who was updated first will be assigned to the incoming
                                                                           chat until the maximum chats threshold is reached. Table 1. CSQ
                                                   				Type—Chat Field
                                                         						  Name Description CSQ
                                                         						  Type Choose
                                                         						  Chat. Table 2. CSQ
                                                   				Type—Email Field
                                                         						  Name Description CSQ
                                                         						  Type Choose
                                                         						  Email. Note You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. Mail
                                                         						  Server Fully
                                                         						  Qualified Domain Name (FQDN) of email server. This field displays the mail
                                                         						  server that you configured. Authentication Type The type of authentication that is used to access the configured email account. Basic is used to access both types of email, Office 365 and Gmail by using username and password. By default, this option is selected. OAuth is used to access Gmail by using the OAuth Private Key file that is downloaded from the Gmail mail server. Supports OAuth
                                                         2.0 protocol. Note This field is displayed only when you have configured Gmail mail server. Email
                                                         						  username The
                                                         						  email address to which emails are sent or retrieved. Email password Password for the email account. Note This field is mandatory when the email server type is Microsoft Office 365 or Microsoft Exchange. This field is optional when the email server type is Gmail. Private Key The JSON file that contains the OAuth Private Key, which is generated while creating Service Account in Google Cloud server.
                                                         Click Upload to select the file. Note This field is displayed only when Authentication Type is OAuth . Tenant ID This is the Azure cloud tenant ID. Note This field is displayed when Microsoft Office 365 is selected as the email server. Client ID This is the Azure cloud application client ID. Note This field is displayed when Microsoft Office 365 is selected as the email server. Client secret This is the Azure cloud application client secret. Note This field is displayed when Microsoft Office 365 is selected as the email server. Note Tenant ID, Client ID, and Client secret are available from 12.5(1)SU2 ES03 onwards. Inbox Folder Name The
                                                         						  folder from which emails will be fetched and queued for the Contact Service
                                                         						  Queue. Default value = Inbox folder of the selected mail server type Note If you change the Inbox folder name, which is already in use, the emails that are downloaded and cached by Customer Collaboration Platform are made available to agents. The remaining emails in the folder are ignored. Sent
                                                         						  Items Folder Name The folder to which Customer Collaboration Platform will move the response email to, when it is sent. Test Configuration This checks the following: Connectivity from Customer Collaboration Platform to the configured mail server by using the user credentials that is specified in the Contact Service Queue (CSQ) configuration. Presence of and permissions to the Inbox, Drafts, Outbox, and Sent Items folder for the user, that is specified in the CSQ
                                                               configuration. Poll
                                                         						  Interval (Seconds) Frequency in seconds to fetch emails from the server. Default value = 180, Range = 60 to 3600 Snapshot Age (Minutes) Specify the time in minutes from when the emails are to be
                                                         						  fetched. Default value = 120, Range = 60 to 43200 For
                                                         						  example, if you specify 120 minutes, this field fetches the emails from the
                                                         						  last two hours. | Field Name | Description | CSQ
                                                         							 Name | Name
                                                         							 for the CSQ. | Resource Selection Criteria | Resource selection criteria chosen for the chat CSQ. Longest Available —Selects the agent who has been in the Available state for the longest amount of time. Most Skilled —Used for expert agent chat distribution. Selects the agent with the highest total competency level. The total competency
                                                               level is determined by adding the agent's competency levels for each assigned skill that is also assigned to the CSQ. Example 1: If Agent1 is assigned Skill1(5), Skill2(6), and Skill3(7) and CSQ1 specifies Skill1(min=1) and Skill3(min=1), the
                                                                     total competency level for Agent1 for CSQ1 is 12. Example 2: If Agent1 is assigned Skill1(5) and Skill2(6), and Skill3(7) and CSQ1 specifies Skill1(min=1), only, the total
                                                                     competency level for Agent1 for CSQ1 is 5. Note To change the competence level for an already configured agent, change the agent skill level and save the CSQ. If two agents score equal in the primary selection criteria, the agent who was updated first will be assigned to the incoming
                                                                           chat until the maximum chats threshold is reached. | Note | To change the competence level for an already configured agent, change the agent skill level and save the CSQ. If two agents score equal in the primary selection criteria, the agent who was updated first will be assigned to the incoming
                                                                           chat until the maximum chats threshold is reached. | Field
                                                         						  Name | Description | CSQ
                                                         						  Type | Choose
                                                         						  Chat. | Field
                                                         						  Name | Description | CSQ
                                                         						  Type | Choose
                                                         						  Email. Note You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. | Note | You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. | Mail
                                                         						  Server | Fully
                                                         						  Qualified Domain Name (FQDN) of email server. This field displays the mail
                                                         						  server that you configured. | Authentication Type | The type of authentication that is used to access the configured email account. Basic is used to access both types of email, Office 365 and Gmail by using username and password. By default, this option is selected. OAuth is used to access Gmail by using the OAuth Private Key file that is downloaded from the Gmail mail server. Supports OAuth
                                                         2.0 protocol. Note This field is displayed only when you have configured Gmail mail server. | Note | This field is displayed only when you have configured Gmail mail server. | Email
                                                         						  username | The
                                                         						  email address to which emails are sent or retrieved. | Email password | Password for the email account. Note This field is mandatory when the email server type is Microsoft Office 365 or Microsoft Exchange. This field is optional when the email server type is Gmail. | Note | This field is mandatory when the email server type is Microsoft Office 365 or Microsoft Exchange. This field is optional when the email server type is Gmail. | Private Key | The JSON file that contains the OAuth Private Key, which is generated while creating Service Account in Google Cloud server.
                                                         Click Upload to select the file. Note This field is displayed only when Authentication Type is OAuth . | Note | This field is displayed only when Authentication Type is OAuth . | Tenant ID | This is the Azure cloud tenant ID. Note This field is displayed when Microsoft Office 365 is selected as the email server. | Note | This field is displayed when Microsoft Office 365 is selected as the email server. | Client ID | This is the Azure cloud application client ID. Note This field is displayed when Microsoft Office 365 is selected as the email server. | Note | This field is displayed when Microsoft Office 365 is selected as the email server. | Client secret | This is the Azure cloud application client secret. Note This field is displayed when Microsoft Office 365 is selected as the email server. | Note | This field is displayed when Microsoft Office 365 is selected as the email server. | Note Tenant ID, Client ID, and Client secret are available from 12.5(1)SU2 ES03 onwards. | Note | Tenant ID, Client ID, and Client secret are available from 12.5(1)SU2 ES03 onwards. | Inbox Folder Name | The
                                                         						  folder from which emails will be fetched and queued for the Contact Service
                                                         						  Queue. Default value = Inbox folder of the selected mail server type Note If you change the Inbox folder name, which is already in use, the emails that are downloaded and cached by Customer Collaboration Platform are made available to agents. The remaining emails in the folder are ignored. | Note | If you change the Inbox folder name, which is already in use, the emails that are downloaded and cached by Customer Collaboration Platform are made available to agents. The remaining emails in the folder are ignored. | Sent
                                                         						  Items Folder Name | The folder to which Customer Collaboration Platform will move the response email to, when it is sent. | Test Configuration | This checks the following: Connectivity from Customer Collaboration Platform to the configured mail server by using the user credentials that is specified in the Contact Service Queue (CSQ) configuration. Presence of and permissions to the Inbox, Drafts, Outbox, and Sent Items folder for the user, that is specified in the CSQ
                                                               configuration. | Poll
                                                         						  Interval (Seconds) | Frequency in seconds to fetch emails from the server. Default value = 180, Range = 60 to 3600 | Snapshot Age (Minutes) | Specify the time in minutes from when the emails are to be
                                                         						  fetched. Default value = 120, Range = 60 to 43200 For
                                                         						  example, if you specify 120 minutes, this field fetches the emails from the
                                                         						  last two hours. |
| Field Name | Description |
| CSQ
                                                         							 Name | Name
                                                         							 for the CSQ. |
| Resource Selection Criteria | Resource selection criteria chosen for the chat CSQ. Longest Available —Selects the agent who has been in the Available state for the longest amount of time. Most Skilled —Used for expert agent chat distribution. Selects the agent with the highest total competency level. The total competency
                                                               level is determined by adding the agent's competency levels for each assigned skill that is also assigned to the CSQ. Example 1: If Agent1 is assigned Skill1(5), Skill2(6), and Skill3(7) and CSQ1 specifies Skill1(min=1) and Skill3(min=1), the
                                                                     total competency level for Agent1 for CSQ1 is 12. Example 2: If Agent1 is assigned Skill1(5) and Skill2(6), and Skill3(7) and CSQ1 specifies Skill1(min=1), only, the total
                                                                     competency level for Agent1 for CSQ1 is 5. Note To change the competence level for an already configured agent, change the agent skill level and save the CSQ. If two agents score equal in the primary selection criteria, the agent who was updated first will be assigned to the incoming
                                                                           chat until the maximum chats threshold is reached. | Note | To change the competence level for an already configured agent, change the agent skill level and save the CSQ. If two agents score equal in the primary selection criteria, the agent who was updated first will be assigned to the incoming
                                                                           chat until the maximum chats threshold is reached. |
| Note | To change the competence level for an already configured agent, change the agent skill level and save the CSQ. If two agents score equal in the primary selection criteria, the agent who was updated first will be assigned to the incoming
                                                                           chat until the maximum chats threshold is reached. |
| Field
                                                         						  Name | Description |
| CSQ
                                                         						  Type | Choose
                                                         						  Chat. |
| Field
                                                         						  Name | Description |
| CSQ
                                                         						  Type | Choose
                                                         						  Email. Note You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. | Note | You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. |
| Note | You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. |
| Mail
                                                         						  Server | Fully
                                                         						  Qualified Domain Name (FQDN) of email server. This field displays the mail
                                                         						  server that you configured. |
| Authentication Type | The type of authentication that is used to access the configured email account. Basic is used to access both types of email, Office 365 and Gmail by using username and password. By default, this option is selected. OAuth is used to access Gmail by using the OAuth Private Key file that is downloaded from the Gmail mail server. Supports OAuth
                                                         2.0 protocol. Note This field is displayed only when you have configured Gmail mail server. | Note | This field is displayed only when you have configured Gmail mail server. |
| Note | This field is displayed only when you have configured Gmail mail server. |
| Email
                                                         						  username | The
                                                         						  email address to which emails are sent or retrieved. |
| Email password | Password for the email account. Note This field is mandatory when the email server type is Microsoft Office 365 or Microsoft Exchange. This field is optional when the email server type is Gmail. | Note | This field is mandatory when the email server type is Microsoft Office 365 or Microsoft Exchange. This field is optional when the email server type is Gmail. |
| Note | This field is mandatory when the email server type is Microsoft Office 365 or Microsoft Exchange. This field is optional when the email server type is Gmail. |
| Private Key | The JSON file that contains the OAuth Private Key, which is generated while creating Service Account in Google Cloud server.
                                                         Click Upload to select the file. Note This field is displayed only when Authentication Type is OAuth . | Note | This field is displayed only when Authentication Type is OAuth . |
| Note | This field is displayed only when Authentication Type is OAuth . |
| Tenant ID | This is the Azure cloud tenant ID. Note This field is displayed when Microsoft Office 365 is selected as the email server. | Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
| Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
| Client ID | This is the Azure cloud application client ID. Note This field is displayed when Microsoft Office 365 is selected as the email server. | Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
| Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
| Client secret | This is the Azure cloud application client secret. Note This field is displayed when Microsoft Office 365 is selected as the email server. | Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
| Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
| Note Tenant ID, Client ID, and Client secret are available from 12.5(1)SU2 ES03 onwards. | Note | Tenant ID, Client ID, and Client secret are available from 12.5(1)SU2 ES03 onwards. |
| Note | Tenant ID, Client ID, and Client secret are available from 12.5(1)SU2 ES03 onwards. |
| Inbox Folder Name | The
                                                         						  folder from which emails will be fetched and queued for the Contact Service
                                                         						  Queue. Default value = Inbox folder of the selected mail server type Note If you change the Inbox folder name, which is already in use, the emails that are downloaded and cached by Customer Collaboration Platform are made available to agents. The remaining emails in the folder are ignored. | Note | If you change the Inbox folder name, which is already in use, the emails that are downloaded and cached by Customer Collaboration Platform are made available to agents. The remaining emails in the folder are ignored. |
| Note | If you change the Inbox folder name, which is already in use, the emails that are downloaded and cached by Customer Collaboration Platform are made available to agents. The remaining emails in the folder are ignored. |
| Sent
                                                         						  Items Folder Name | The folder to which Customer Collaboration Platform will move the response email to, when it is sent. |
| Test Configuration | This checks the following: Connectivity from Customer Collaboration Platform to the configured mail server by using the user credentials that is specified in the Contact Service Queue (CSQ) configuration. Presence of and permissions to the Inbox, Drafts, Outbox, and Sent Items folder for the user, that is specified in the CSQ
                                                               configuration. |
| Poll
                                                         						  Interval (Seconds) | Frequency in seconds to fetch emails from the server. Default value = 180, Range = 60 to 3600 |
| Snapshot Age (Minutes) | Specify the time in minutes from when the emails are to be
                                                         						  fetched. Default value = 120, Range = 60 to 43200 For
                                                         						  example, if you specify 120 minutes, this field fetches the emails from the
                                                         						  last two hours. |
| Step 4 | Click Next . The Skill
                                             				Association for CSQ area opens with the newly assigned CSQ name. Note You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. | Note | You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. |
| Note | You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. |
| Step 5 | From the
                                          			 Available Skills list, choose the skill that you want to associate with the CSQ
                                          			 by clicking it. To choose more than one skill, press the Ctrl key
                                          			 and click the skills that you want to associate with the CSQ. |
| Step 6 | Click Add . The chosen
                                             				skill and the minimum competence level for that skill are displayed in the
                                             				right pane under the heading Selected. Note To delete
                                                         				  the skill from the Skills Required list, click the Delete icon next to Minimum Competence . | Note | To delete
                                                         				  the skill from the Skills Required list, click the Delete icon next to Minimum Competence . |
| Note | To delete
                                                         				  the skill from the Skills Required list, click the Delete icon next to Minimum Competence . |
| Step 7 | Specify a
                                          			 minimum competence level for the skill assigned to the CSQ. |
| Step 8 | To view the
                                          			 associated resources, click Show
                                             				Resources . |
| Step 9 | Click Save to save the changes for the CSQ. The newly
                                             				added CSQ appears in the List of CSQs . Note You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. You can sort
                                             				the CSQs by title by clicking the CSQ Name header and by type by clicking the CSQ Type header. | Note | You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. |
| Note | You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. |
| Step 10 | To view the printable report and associated resources, click the CSQ for which you want to view the report and the associated
                                          resources and then click Open Printable Report . Note To delete a CSQ, click the CSQ that you want to delete and then click Delete . A warning dialog box appears, asking you to confirm the deletion. To delete, click OK . Caution Deletion of the chat CSQ affects the associated chat web forms. After deleting, modify the corresponding chat web form configurations
                                                         and generate the HTML code. | Note | To delete a CSQ, click the CSQ that you want to delete and then click Delete . A warning dialog box appears, asking you to confirm the deletion. To delete, click OK . | Caution | Deletion of the chat CSQ affects the associated chat web forms. After deleting, modify the corresponding chat web form configurations
                                                         and generate the HTML code. |
| Note | To delete a CSQ, click the CSQ that you want to delete and then click Delete . A warning dialog box appears, asking you to confirm the deletion. To delete, click OK . |
| Caution | Deletion of the chat CSQ affects the associated chat web forms. After deleting, modify the corresponding chat web form configurations
                                                         and generate the HTML code. |

| Field Name | Description |
|---|---|
| CSQ
                                                         							 Name | Name
                                                         							 for the CSQ. |
| Resource Selection Criteria | Resource selection criteria chosen for the chat CSQ. Longest Available —Selects the agent who has been in the Available state for the longest amount of time. Most Skilled —Used for expert agent chat distribution. Selects the agent with the highest total competency level. The total competency
                                                               level is determined by adding the agent's competency levels for each assigned skill that is also assigned to the CSQ. Example 1: If Agent1 is assigned Skill1(5), Skill2(6), and Skill3(7) and CSQ1 specifies Skill1(min=1) and Skill3(min=1), the
                                                                     total competency level for Agent1 for CSQ1 is 12. Example 2: If Agent1 is assigned Skill1(5) and Skill2(6), and Skill3(7) and CSQ1 specifies Skill1(min=1), only, the total
                                                                     competency level for Agent1 for CSQ1 is 5. Note To change the competence level for an already configured agent, change the agent skill level and save the CSQ. If two agents score equal in the primary selection criteria, the agent who was updated first will be assigned to the incoming
                                                                           chat until the maximum chats threshold is reached. | Note | To change the competence level for an already configured agent, change the agent skill level and save the CSQ. If two agents score equal in the primary selection criteria, the agent who was updated first will be assigned to the incoming
                                                                           chat until the maximum chats threshold is reached. |
| Note | To change the competence level for an already configured agent, change the agent skill level and save the CSQ. If two agents score equal in the primary selection criteria, the agent who was updated first will be assigned to the incoming
                                                                           chat until the maximum chats threshold is reached. |

| Note | To change the competence level for an already configured agent, change the agent skill level and save the CSQ. If two agents score equal in the primary selection criteria, the agent who was updated first will be assigned to the incoming
                                                                           chat until the maximum chats threshold is reached. |
|---|---|

| Field
                                                         						  Name | Description |
|---|---|
| CSQ
                                                         						  Type | Choose
                                                         						  Chat. |

| Field
                                                         						  Name | Description |
|---|---|
| CSQ
                                                         						  Type | Choose
                                                         						  Email. Note You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. | Note | You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. |
| Note | You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. |
| Mail
                                                         						  Server | Fully
                                                         						  Qualified Domain Name (FQDN) of email server. This field displays the mail
                                                         						  server that you configured. |
| Authentication Type | The type of authentication that is used to access the configured email account. Basic is used to access both types of email, Office 365 and Gmail by using username and password. By default, this option is selected. OAuth is used to access Gmail by using the OAuth Private Key file that is downloaded from the Gmail mail server. Supports OAuth
                                                         2.0 protocol. Note This field is displayed only when you have configured Gmail mail server. | Note | This field is displayed only when you have configured Gmail mail server. |
| Note | This field is displayed only when you have configured Gmail mail server. |
| Email
                                                         						  username | The
                                                         						  email address to which emails are sent or retrieved. |
| Email password | Password for the email account. Note This field is mandatory when the email server type is Microsoft Office 365 or Microsoft Exchange. This field is optional when the email server type is Gmail. | Note | This field is mandatory when the email server type is Microsoft Office 365 or Microsoft Exchange. This field is optional when the email server type is Gmail. |
| Note | This field is mandatory when the email server type is Microsoft Office 365 or Microsoft Exchange. This field is optional when the email server type is Gmail. |
| Private Key | The JSON file that contains the OAuth Private Key, which is generated while creating Service Account in Google Cloud server.
                                                         Click Upload to select the file. Note This field is displayed only when Authentication Type is OAuth . | Note | This field is displayed only when Authentication Type is OAuth . |
| Note | This field is displayed only when Authentication Type is OAuth . |
| Tenant ID | This is the Azure cloud tenant ID. Note This field is displayed when Microsoft Office 365 is selected as the email server. | Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
| Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
| Client ID | This is the Azure cloud application client ID. Note This field is displayed when Microsoft Office 365 is selected as the email server. | Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
| Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
| Client secret | This is the Azure cloud application client secret. Note This field is displayed when Microsoft Office 365 is selected as the email server. | Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
| Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
| Note Tenant ID, Client ID, and Client secret are available from 12.5(1)SU2 ES03 onwards. | Note | Tenant ID, Client ID, and Client secret are available from 12.5(1)SU2 ES03 onwards. |
| Note | Tenant ID, Client ID, and Client secret are available from 12.5(1)SU2 ES03 onwards. |
| Inbox Folder Name | The
                                                         						  folder from which emails will be fetched and queued for the Contact Service
                                                         						  Queue. Default value = Inbox folder of the selected mail server type Note If you change the Inbox folder name, which is already in use, the emails that are downloaded and cached by Customer Collaboration Platform are made available to agents. The remaining emails in the folder are ignored. | Note | If you change the Inbox folder name, which is already in use, the emails that are downloaded and cached by Customer Collaboration Platform are made available to agents. The remaining emails in the folder are ignored. |
| Note | If you change the Inbox folder name, which is already in use, the emails that are downloaded and cached by Customer Collaboration Platform are made available to agents. The remaining emails in the folder are ignored. |
| Sent
                                                         						  Items Folder Name | The folder to which Customer Collaboration Platform will move the response email to, when it is sent. |
| Test Configuration | This checks the following: Connectivity from Customer Collaboration Platform to the configured mail server by using the user credentials that is specified in the Contact Service Queue (CSQ) configuration. Presence of and permissions to the Inbox, Drafts, Outbox, and Sent Items folder for the user, that is specified in the CSQ
                                                               configuration. |
| Poll
                                                         						  Interval (Seconds) | Frequency in seconds to fetch emails from the server. Default value = 180, Range = 60 to 3600 |
| Snapshot Age (Minutes) | Specify the time in minutes from when the emails are to be
                                                         						  fetched. Default value = 120, Range = 60 to 43200 For
                                                         						  example, if you specify 120 minutes, this field fetches the emails from the
                                                         						  last two hours. |

| Note | You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. |
|---|---|

| Note | This field is displayed only when you have configured Gmail mail server. |
|---|---|

| Note | This field is mandatory when the email server type is Microsoft Office 365 or Microsoft Exchange. This field is optional when the email server type is Gmail. |
|---|---|

| Note | This field is displayed only when Authentication Type is OAuth . |
|---|---|

| Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
|---|---|

| Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
|---|---|

| Note | This field is displayed when Microsoft Office 365 is selected as the email server. |
|---|---|

| Note | Tenant ID, Client ID, and Client secret are available from 12.5(1)SU2 ES03 onwards. |
|---|---|

| Note | If you change the Inbox folder name, which is already in use, the emails that are downloaded and cached by Customer Collaboration Platform are made available to agents. The remaining emails in the folder are ignored. |
|---|---|

| Note | You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. |
|---|---|

| Note | To delete
                                                         				  the skill from the Skills Required list, click the Delete icon next to Minimum Competence . |
|---|---|

| Note | You can create up to 100 email CSQs. If you exceed the limit, the following error is displayed: Cisco Unified CCX supports a maximum of 100 Email CSQs. Exceeded maximum limit for Email CSQs. |
|---|---|

| Note | To delete a CSQ, click the CSQ that you want to delete and then click Delete . A warning dialog box appears, asking you to confirm the deletion. To delete, click OK . |
|---|---|

| Caution | Deletion of the chat CSQ affects the associated chat web forms. After deleting, modify the corresponding chat web form configurations
                                                         and generate the HTML code. |
|---|---|

| Note | To modify an existing predefined response, click the Title header for the predefined response that you want to modify. To
                                                delete an existing predefined response, click the Delete icon for the predefined response that you want to delete. |
|---|---|

| Step 1 | From the
                                             			 Unified CCX Administration menu bar, choose Subsystems > Chat > Predefined
                                                   				  Responses OR Subsystems > Chat and
                                                   				  Email > Predefined Responses as applicable. The Predefined Responses web page opens, displaying the
                                                				information for existing responses, if any. |
|---|---|
| Step 2 | Click the Add
                                                				New icon that is displayed in the toolbar in the upper left corner
                                             			 of the window or the Add
                                                				New button that is displayed at the bottom of the window to create
                                             			 a new response. The Predefined Response Configuration web page opens. |
| Step 3 | Specify the
                                             			 following information: Field Description Title Unique identifier of the predefined response. Note The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed. Type Types of media. Response Description Description for the predefined response. Rich Text Editor is available to create an HTML-based email predefined response. Use the supported tags as provided in the Rich Text Editor for formatting purpose. Plain Text Editor is available to create a chat predefined response. Note The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed in Plain Text Editor for Chat Predefines Response. The maximum characters limit for predefined response for chat and email is 1500. In case of email, rich text is supported and includes the HTML tag characters for representing rich text. Tags Choose a tag for the predefined response. Global for all CSQs : The predefined response is available to all the agents that are associated with all the CSQs. Customize (Maximum 10 CSQs) : The predefined response is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. Note Predefined responses can be used only for emails sent in HTML format and not plain text. | Field | Description | Title | Unique identifier of the predefined response. Note The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed. | Note | The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed. | Type | Types of media. | Response Description | Description for the predefined response. Rich Text Editor is available to create an HTML-based email predefined response. Use the supported tags as provided in the Rich Text Editor for formatting purpose. Plain Text Editor is available to create a chat predefined response. Note The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed in Plain Text Editor for Chat Predefines Response. The maximum characters limit for predefined response for chat and email is 1500. In case of email, rich text is supported and includes the HTML tag characters for representing rich text. | Note | The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed in Plain Text Editor for Chat Predefines Response. The maximum characters limit for predefined response for chat and email is 1500. In case of email, rich text is supported and includes the HTML tag characters for representing rich text. | Tags | Choose a tag for the predefined response. Global for all CSQs : The predefined response is available to all the agents that are associated with all the CSQs. Customize (Maximum 10 CSQs) : The predefined response is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. Note Predefined responses can be used only for emails sent in HTML format and not plain text. | Note | Predefined responses can be used only for emails sent in HTML format and not plain text. |
| Field | Description |
| Title | Unique identifier of the predefined response. Note The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed. | Note | The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed. |
| Note | The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed. |
| Type | Types of media. |
| Response Description | Description for the predefined response. Rich Text Editor is available to create an HTML-based email predefined response. Use the supported tags as provided in the Rich Text Editor for formatting purpose. Plain Text Editor is available to create a chat predefined response. Note The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed in Plain Text Editor for Chat Predefines Response. The maximum characters limit for predefined response for chat and email is 1500. In case of email, rich text is supported and includes the HTML tag characters for representing rich text. | Note | The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed in Plain Text Editor for Chat Predefines Response. The maximum characters limit for predefined response for chat and email is 1500. In case of email, rich text is supported and includes the HTML tag characters for representing rich text. |
| Note | The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed in Plain Text Editor for Chat Predefines Response. The maximum characters limit for predefined response for chat and email is 1500. In case of email, rich text is supported and includes the HTML tag characters for representing rich text. |
| Tags | Choose a tag for the predefined response. Global for all CSQs : The predefined response is available to all the agents that are associated with all the CSQs. Customize (Maximum 10 CSQs) : The predefined response is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. Note Predefined responses can be used only for emails sent in HTML format and not plain text. | Note | Predefined responses can be used only for emails sent in HTML format and not plain text. |
| Note | Predefined responses can be used only for emails sent in HTML format and not plain text. |
| Step 4 | Click Save . The newly
                                                				added predefined response appears with the assigned tags in the List of
                                                   				  Predefined Responses . You can sort
                                                				the predefined responses by title by clicking the Title header and by type by
                                                				clicking the Type header. |

| Field | Description |
|---|---|
| Title | Unique identifier of the predefined response. Note The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed. | Note | The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed. |
| Note | The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed. |
| Type | Types of media. |
| Response Description | Description for the predefined response. Rich Text Editor is available to create an HTML-based email predefined response. Use the supported tags as provided in the Rich Text Editor for formatting purpose. Plain Text Editor is available to create a chat predefined response. Note The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed in Plain Text Editor for Chat Predefines Response. The maximum characters limit for predefined response for chat and email is 1500. In case of email, rich text is supported and includes the HTML tag characters for representing rich text. | Note | The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed in Plain Text Editor for Chat Predefines Response. The maximum characters limit for predefined response for chat and email is 1500. In case of email, rich text is supported and includes the HTML tag characters for representing rich text. |
| Note | The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed in Plain Text Editor for Chat Predefines Response. The maximum characters limit for predefined response for chat and email is 1500. In case of email, rich text is supported and includes the HTML tag characters for representing rich text. |
| Tags | Choose a tag for the predefined response. Global for all CSQs : The predefined response is available to all the agents that are associated with all the CSQs. Customize (Maximum 10 CSQs) : The predefined response is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. Note Predefined responses can be used only for emails sent in HTML format and not plain text. | Note | Predefined responses can be used only for emails sent in HTML format and not plain text. |
| Note | Predefined responses can be used only for emails sent in HTML format and not plain text. |

| Note | The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed. |
|---|---|---|

| Note | The special characters angle brackets (< >), parentheses ( ( ) ), double quotation marks (" "), and pipe symbol (\|) are not
                                                                        allowed in Plain Text Editor for Chat Predefines Response. The maximum characters limit for predefined response for chat and email is 1500. In case of email, rich text is supported and includes the HTML tag characters for representing rich text. |
|---|---|---|

| Note | Predefined responses can be used only for emails sent in HTML format and not plain text. |
|---|---|

| Step 1 | From the
                                             			 Unified CCX Administration menu bar, choose Subsystems > Chat and Email > Wrap-Up Reasons . The Wrap-Up
                                                				Reasons web page opens, displaying the information for existing
                                             			 Wrap-Up Reasons, if any. |
|---|---|
| Step 2 | Click the Add
                                                				New icon or the Add
                                                				New button that is displayed in the toolbar in the upper left
                                             			 corner of the window. The Wrap-Up Reasons web page opens. |
| Step 3 | Specify the
                                             			 following information: Field Description Category Specify the name for the Wrap-Up category. Allows up to 40 characters. Wrap-Up Reasons Enter the Wrap-Up Reasons for the specified category. Allows up to 40 characters. Click the Add button to add up to 25 Wrap-Up Reasons for each category. Tags Choose a tag for the Wrap-Up category. Note You can associate a maximum of 10 Wrap-Up categories to a CSQ. Global for all CSQs : The Wrap-Up reason is available to all the agents that are associated with all the CSQs. Customize : The Wrap-Up reason is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. | Field | Description | Category | Specify the name for the Wrap-Up category. Allows up to 40 characters. | Wrap-Up Reasons | Enter the Wrap-Up Reasons for the specified category. Allows up to 40 characters. Click the Add button to add up to 25 Wrap-Up Reasons for each category. | Tags | Choose a tag for the Wrap-Up category. Note You can associate a maximum of 10 Wrap-Up categories to a CSQ. Global for all CSQs : The Wrap-Up reason is available to all the agents that are associated with all the CSQs. Customize : The Wrap-Up reason is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. | Note | You can associate a maximum of 10 Wrap-Up categories to a CSQ. Global for all CSQs : The Wrap-Up reason is available to all the agents that are associated with all the CSQs. Customize : The Wrap-Up reason is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. |
| Field | Description |
| Category | Specify the name for the Wrap-Up category. Allows up to 40 characters. |
| Wrap-Up Reasons | Enter the Wrap-Up Reasons for the specified category. Allows up to 40 characters. Click the Add button to add up to 25 Wrap-Up Reasons for each category. |
| Tags | Choose a tag for the Wrap-Up category. Note You can associate a maximum of 10 Wrap-Up categories to a CSQ. Global for all CSQs : The Wrap-Up reason is available to all the agents that are associated with all the CSQs. Customize : The Wrap-Up reason is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. | Note | You can associate a maximum of 10 Wrap-Up categories to a CSQ. Global for all CSQs : The Wrap-Up reason is available to all the agents that are associated with all the CSQs. Customize : The Wrap-Up reason is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. |
| Note | You can associate a maximum of 10 Wrap-Up categories to a CSQ. Global for all CSQs : The Wrap-Up reason is available to all the agents that are associated with all the CSQs. Customize : The Wrap-Up reason is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. |
| Step 4 | Click Save . The newly
                                                				added Wrap-Up category appears with the assigned tags in the List of
                                                   				  Wrap-Up Reasons . Note When you
                                                            				  reskill or modify a category, the logged in agents can apply Wrap-Up Reasons
                                                            				  from the updated list of categories for the new non-voice contacts only. | Note | When you
                                                            				  reskill or modify a category, the logged in agents can apply Wrap-Up Reasons
                                                            				  from the updated list of categories for the new non-voice contacts only. |
| Note | When you
                                                            				  reskill or modify a category, the logged in agents can apply Wrap-Up Reasons
                                                            				  from the updated list of categories for the new non-voice contacts only. |

| Field | Description |
|---|---|
| Category | Specify the name for the Wrap-Up category. Allows up to 40 characters. |
| Wrap-Up Reasons | Enter the Wrap-Up Reasons for the specified category. Allows up to 40 characters. Click the Add button to add up to 25 Wrap-Up Reasons for each category. |
| Tags | Choose a tag for the Wrap-Up category. Note You can associate a maximum of 10 Wrap-Up categories to a CSQ. Global for all CSQs : The Wrap-Up reason is available to all the agents that are associated with all the CSQs. Customize : The Wrap-Up reason is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. | Note | You can associate a maximum of 10 Wrap-Up categories to a CSQ. Global for all CSQs : The Wrap-Up reason is available to all the agents that are associated with all the CSQs. Customize : The Wrap-Up reason is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. |
| Note | You can associate a maximum of 10 Wrap-Up categories to a CSQ. Global for all CSQs : The Wrap-Up reason is available to all the agents that are associated with all the CSQs. Customize : The Wrap-Up reason is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. |

| Note | You can associate a maximum of 10 Wrap-Up categories to a CSQ. Global for all CSQs : The Wrap-Up reason is available to all the agents that are associated with all the CSQs. Customize : The Wrap-Up reason is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. |
|---|---|

| Note | When you
                                                            				  reskill or modify a category, the logged in agents can apply Wrap-Up Reasons
                                                            				  from the updated list of categories for the new non-voice contacts only. |
|---|---|

| Note | To modify an existing email signature, click the Title header for the email signature that you want to modify. To delete an
                                                existing email signature, click the Delete icon for the email signature that you want to delete. |
|---|---|

| Step 1 | From the
                                             			 Unified CCX Administration menu bar, choose Subsystems > Chat and
                                                   				  Email > Email Signatures . The Email
                                                   				  Signature web page opens, displaying the list of existing email
                                                				signatures that are configured, if any. |
|---|---|
| Step 2 | Click the Add
                                                				New icon that is displayed in the toolbar in the upper left corner
                                             			 of the window or the Add
                                                				New button that is displayed at the bottom of the window to create
                                             			 a new email signature. The Email
                                                   				  Signature Configuration web page opens. |
| Step 3 | Specify the
                                             			 following information: Field Description Name Unique name of the email signature. Note The name can have a maximum of 100 characters. Content The email signature content. Note The email signature can have a maximum of 1500 characters. You may format the text of the email signature content, add images,
                                                                        add URL to the email signature, and add the Agent alias information. The Agent alias variable appears by default when any new email signature is created. If it is removed from the email signature
                                                                        it can be reinserted at the cursor location in the email signature by clicking on the Agent alias variable icon. When there is no alias configured for an agent, the Agent ID is presented in the email signature by default. Tags Choose a tag for the email signature. Global for all CSQs : The email signature is available to all the agents that are associated with all the CSQs. Customize (Maximum 10 CSQs) : The email signature is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. Note Only one (1) email signature can be tagged as Global for all CSQs. A CSQ can be tagged with only one (1) email signature. When an email is responded by an agent of a particular CSQ, the system will check if there is any email signature tagged
                                                                        for that CSQ. The different scenarios are: If there is an email signature tagged to a CSQ, that will be appended in the email response. If there is no CSQ specific email signature, the global signature is appended in the email response. If there is no global email signature and no customized email signature tagged to the CSQ then there will be no email signature
                                                                              appended in the email response. | Field | Description | Name | Unique name of the email signature. Note The name can have a maximum of 100 characters. | Note | The name can have a maximum of 100 characters. | Content | The email signature content. Note The email signature can have a maximum of 1500 characters. You may format the text of the email signature content, add images,
                                                                        add URL to the email signature, and add the Agent alias information. The Agent alias variable appears by default when any new email signature is created. If it is removed from the email signature
                                                                        it can be reinserted at the cursor location in the email signature by clicking on the Agent alias variable icon. When there is no alias configured for an agent, the Agent ID is presented in the email signature by default. | Note | The email signature can have a maximum of 1500 characters. You may format the text of the email signature content, add images,
                                                                        add URL to the email signature, and add the Agent alias information. The Agent alias variable appears by default when any new email signature is created. If it is removed from the email signature
                                                                        it can be reinserted at the cursor location in the email signature by clicking on the Agent alias variable icon. When there is no alias configured for an agent, the Agent ID is presented in the email signature by default. | Tags | Choose a tag for the email signature. Global for all CSQs : The email signature is available to all the agents that are associated with all the CSQs. Customize (Maximum 10 CSQs) : The email signature is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. Note Only one (1) email signature can be tagged as Global for all CSQs. A CSQ can be tagged with only one (1) email signature. When an email is responded by an agent of a particular CSQ, the system will check if there is any email signature tagged
                                                                        for that CSQ. The different scenarios are: If there is an email signature tagged to a CSQ, that will be appended in the email response. If there is no CSQ specific email signature, the global signature is appended in the email response. If there is no global email signature and no customized email signature tagged to the CSQ then there will be no email signature
                                                                              appended in the email response. | Note | Only one (1) email signature can be tagged as Global for all CSQs. A CSQ can be tagged with only one (1) email signature. When an email is responded by an agent of a particular CSQ, the system will check if there is any email signature tagged
                                                                        for that CSQ. The different scenarios are: If there is an email signature tagged to a CSQ, that will be appended in the email response. If there is no CSQ specific email signature, the global signature is appended in the email response. If there is no global email signature and no customized email signature tagged to the CSQ then there will be no email signature
                                                                              appended in the email response. |
| Field | Description |
| Name | Unique name of the email signature. Note The name can have a maximum of 100 characters. | Note | The name can have a maximum of 100 characters. |
| Note | The name can have a maximum of 100 characters. |
| Content | The email signature content. Note The email signature can have a maximum of 1500 characters. You may format the text of the email signature content, add images,
                                                                        add URL to the email signature, and add the Agent alias information. The Agent alias variable appears by default when any new email signature is created. If it is removed from the email signature
                                                                        it can be reinserted at the cursor location in the email signature by clicking on the Agent alias variable icon. When there is no alias configured for an agent, the Agent ID is presented in the email signature by default. | Note | The email signature can have a maximum of 1500 characters. You may format the text of the email signature content, add images,
                                                                        add URL to the email signature, and add the Agent alias information. The Agent alias variable appears by default when any new email signature is created. If it is removed from the email signature
                                                                        it can be reinserted at the cursor location in the email signature by clicking on the Agent alias variable icon. When there is no alias configured for an agent, the Agent ID is presented in the email signature by default. |
| Note | The email signature can have a maximum of 1500 characters. You may format the text of the email signature content, add images,
                                                                        add URL to the email signature, and add the Agent alias information. The Agent alias variable appears by default when any new email signature is created. If it is removed from the email signature
                                                                        it can be reinserted at the cursor location in the email signature by clicking on the Agent alias variable icon. When there is no alias configured for an agent, the Agent ID is presented in the email signature by default. |
| Tags | Choose a tag for the email signature. Global for all CSQs : The email signature is available to all the agents that are associated with all the CSQs. Customize (Maximum 10 CSQs) : The email signature is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. Note Only one (1) email signature can be tagged as Global for all CSQs. A CSQ can be tagged with only one (1) email signature. When an email is responded by an agent of a particular CSQ, the system will check if there is any email signature tagged
                                                                        for that CSQ. The different scenarios are: If there is an email signature tagged to a CSQ, that will be appended in the email response. If there is no CSQ specific email signature, the global signature is appended in the email response. If there is no global email signature and no customized email signature tagged to the CSQ then there will be no email signature
                                                                              appended in the email response. | Note | Only one (1) email signature can be tagged as Global for all CSQs. A CSQ can be tagged with only one (1) email signature. When an email is responded by an agent of a particular CSQ, the system will check if there is any email signature tagged
                                                                        for that CSQ. The different scenarios are: If there is an email signature tagged to a CSQ, that will be appended in the email response. If there is no CSQ specific email signature, the global signature is appended in the email response. If there is no global email signature and no customized email signature tagged to the CSQ then there will be no email signature
                                                                              appended in the email response. |
| Note | Only one (1) email signature can be tagged as Global for all CSQs. A CSQ can be tagged with only one (1) email signature. When an email is responded by an agent of a particular CSQ, the system will check if there is any email signature tagged
                                                                        for that CSQ. The different scenarios are: If there is an email signature tagged to a CSQ, that will be appended in the email response. If there is no CSQ specific email signature, the global signature is appended in the email response. If there is no global email signature and no customized email signature tagged to the CSQ then there will be no email signature
                                                                              appended in the email response. |
| Step 4 | Click Save . The newly
                                                				added email signature appears with the assigned tags in the List of
                                                   				  Email Signatures . You can sort
                                                				the email signatures by title by clicking the Title header and by type by
                                                				clicking the Type header. |

| Field | Description |
|---|---|
| Name | Unique name of the email signature. Note The name can have a maximum of 100 characters. | Note | The name can have a maximum of 100 characters. |
| Note | The name can have a maximum of 100 characters. |
| Content | The email signature content. Note The email signature can have a maximum of 1500 characters. You may format the text of the email signature content, add images,
                                                                        add URL to the email signature, and add the Agent alias information. The Agent alias variable appears by default when any new email signature is created. If it is removed from the email signature
                                                                        it can be reinserted at the cursor location in the email signature by clicking on the Agent alias variable icon. When there is no alias configured for an agent, the Agent ID is presented in the email signature by default. | Note | The email signature can have a maximum of 1500 characters. You may format the text of the email signature content, add images,
                                                                        add URL to the email signature, and add the Agent alias information. The Agent alias variable appears by default when any new email signature is created. If it is removed from the email signature
                                                                        it can be reinserted at the cursor location in the email signature by clicking on the Agent alias variable icon. When there is no alias configured for an agent, the Agent ID is presented in the email signature by default. |
| Note | The email signature can have a maximum of 1500 characters. You may format the text of the email signature content, add images,
                                                                        add URL to the email signature, and add the Agent alias information. The Agent alias variable appears by default when any new email signature is created. If it is removed from the email signature
                                                                        it can be reinserted at the cursor location in the email signature by clicking on the Agent alias variable icon. When there is no alias configured for an agent, the Agent ID is presented in the email signature by default. |
| Tags | Choose a tag for the email signature. Global for all CSQs : The email signature is available to all the agents that are associated with all the CSQs. Customize (Maximum 10 CSQs) : The email signature is available only to the agents that are associated with the selected CSQs. If you choose this option, select the CSQs from the Available CSQs pane, and then click the left arrow to assign them. Note Only one (1) email signature can be tagged as Global for all CSQs. A CSQ can be tagged with only one (1) email signature. When an email is responded by an agent of a particular CSQ, the system will check if there is any email signature tagged
                                                                        for that CSQ. The different scenarios are: If there is an email signature tagged to a CSQ, that will be appended in the email response. If there is no CSQ specific email signature, the global signature is appended in the email response. If there is no global email signature and no customized email signature tagged to the CSQ then there will be no email signature
                                                                              appended in the email response. | Note | Only one (1) email signature can be tagged as Global for all CSQs. A CSQ can be tagged with only one (1) email signature. When an email is responded by an agent of a particular CSQ, the system will check if there is any email signature tagged
                                                                        for that CSQ. The different scenarios are: If there is an email signature tagged to a CSQ, that will be appended in the email response. If there is no CSQ specific email signature, the global signature is appended in the email response. If there is no global email signature and no customized email signature tagged to the CSQ then there will be no email signature
                                                                              appended in the email response. |
| Note | Only one (1) email signature can be tagged as Global for all CSQs. A CSQ can be tagged with only one (1) email signature. When an email is responded by an agent of a particular CSQ, the system will check if there is any email signature tagged
                                                                        for that CSQ. The different scenarios are: If there is an email signature tagged to a CSQ, that will be appended in the email response. If there is no CSQ specific email signature, the global signature is appended in the email response. If there is no global email signature and no customized email signature tagged to the CSQ then there will be no email signature
                                                                              appended in the email response. |

| Note | The name can have a maximum of 100 characters. |
|---|---|

| Note | The email signature can have a maximum of 1500 characters. You may format the text of the email signature content, add images,
                                                                        add URL to the email signature, and add the Agent alias information. The Agent alias variable appears by default when any new email signature is created. If it is removed from the email signature
                                                                        it can be reinserted at the cursor location in the email signature by clicking on the Agent alias variable icon. When there is no alias configured for an agent, the Agent ID is presented in the email signature by default. |
|---|---|

| Note | Only one (1) email signature can be tagged as Global for all CSQs. A CSQ can be tagged with only one (1) email signature. When an email is responded by an agent of a particular CSQ, the system will check if there is any email signature tagged
                                                                        for that CSQ. The different scenarios are: If there is an email signature tagged to a CSQ, that will be appended in the email response. If there is no CSQ specific email signature, the global signature is appended in the email response. If there is no global email signature and no customized email signature tagged to the CSQ then there will be no email signature
                                                                              appended in the email response. |
|---|---|

| Step 1 | From the
                                          			 Unified CCX Administration menu bar, choose Subsystems > Chat > Channel
                                                				  Parameters OR Subsystems > Chat and
                                                				  Email > Channel Parameters as applicable. The
                                             				Channel Parameters Configuration web page opens. |
|---|---|
| Step 2 | Use this web
                                          			 page to specify or modify the following fields for channel parameters: Field Description No
                                                         							 Answer Timeout (Seconds) The
                                                         							 time for an agent to respond to the chat request after which, the chat request
                                                         							 is routed back to the chat queue and for the chat toaster to fade out. This
                                                         							 is applicable for the Group Chat request also. However when the chat is not
                                                         							 accepted, the chat request is not routed back to the chat queue. Note When you use Chrome or Firefox, the browser overrides the chat toaster
                                                                     								notification to fade out in 20 seconds, even if it is configured to a higher
                                                                     								value. Join
                                                         							 Timeout (Minutes) The
                                                         							 time after which the customer initiates a chat and, if an agent is not joined,
                                                         							 the customer gets a message as per the configuration in the Chat Web Form Configuration page. But an agent can
                                                         							 still join the chat after this timeout. The default timeout is one minute and
                                                         							 the maximum timeout value allowed is 60 minutes. Inactivity Timeout (Minutes) The
                                                         							 customer inactivity time after which, the system ends the chat. This timeout is
                                                         							 on the customer side only. The
                                                         							 agent gets a message "You are alone in the chat room. Click End to close the chat
                                                            								interface." . The
                                                         							 customer gets a message "Warning: the server connection was lost due to an inactivity
                                                            								timeout or connection failure." . Inactivity timeout may also apply to contacts in queue that have
                                                         							 not yet been accepted by agents. This scenario occurs only when the Join
                                                         							 Timeout value is greater than the Inactivity Timeout value. The customer then gets a message "Sorry, the chat service is currently not available. Please try
                                                            								again later." Offer Chat Contact When On Voice Call Click Yes if agents are allowed to handle a chat session during
                                                         							 a voice call. Note This setting takes effect when the agent ends the current voice call. Chats are presented to agents even when they go off-hook or busy in a Non ICD call. Offer Voice Call When On Chat Click Yes if agents are allowed to handle a voice call during a
                                                         							 chat session. Note This setting takes effect when the agent receives a new incoming chat. Direct/Consult Transfer to an IPCC extension is an exception. Even if agents are busy on a chat they would still get calls
                                                                     that are transferred to their extension directly. Maximum Number Of Chat Sessions Per Agent Number of chat sessions (ranging from 1 to 5) that an agent is allowed to
                                                         							 handle. This includes the group chat sessions also. Note This option is available only if Finesse service is activated. For Cisco Finesse Desktop, the value is set to 1. Maximum Number Of Email Sessions Per Agent Number of Email sessions (ranging from 1 to 5) that an agent is allowed to
                                                         							 handle. Sticky Email Timeout (Hours) Specify the amount of time for which an email message waits in a
                                                         							 specific agent CSQ. Sticky email routing (Last-agent email routing) is a mechanism
                                                         							 to route an email message to the agent who handled the last leg of the email
                                                         							 conversation. When
                                                         							 an email message, which is part of an ongoing conversation, comes in and the
                                                         							 agent who handled the last leg of the conversation is not available, then the
                                                         							 email does not wait indefinitely in that agent queue. After the configured time
                                                         							 expires, the email message is placed on the intended CSQ to be handled by any
                                                         							 available agent. Note Last-agent email routing is not available if the customer changes the subject line of the email message. Default = 4 hours, Range = 1 to 120 hours. | Field | Description | No
                                                         							 Answer Timeout (Seconds) | The
                                                         							 time for an agent to respond to the chat request after which, the chat request
                                                         							 is routed back to the chat queue and for the chat toaster to fade out. This
                                                         							 is applicable for the Group Chat request also. However when the chat is not
                                                         							 accepted, the chat request is not routed back to the chat queue. Note When you use Chrome or Firefox, the browser overrides the chat toaster
                                                                     								notification to fade out in 20 seconds, even if it is configured to a higher
                                                                     								value. | Note | When you use Chrome or Firefox, the browser overrides the chat toaster
                                                                     								notification to fade out in 20 seconds, even if it is configured to a higher
                                                                     								value. | Join
                                                         							 Timeout (Minutes) | The
                                                         							 time after which the customer initiates a chat and, if an agent is not joined,
                                                         							 the customer gets a message as per the configuration in the Chat Web Form Configuration page. But an agent can
                                                         							 still join the chat after this timeout. The default timeout is one minute and
                                                         							 the maximum timeout value allowed is 60 minutes. | Inactivity Timeout (Minutes) | The
                                                         							 customer inactivity time after which, the system ends the chat. This timeout is
                                                         							 on the customer side only. The
                                                         							 agent gets a message "You are alone in the chat room. Click End to close the chat
                                                            								interface." . The
                                                         							 customer gets a message "Warning: the server connection was lost due to an inactivity
                                                            								timeout or connection failure." . Inactivity timeout may also apply to contacts in queue that have
                                                         							 not yet been accepted by agents. This scenario occurs only when the Join
                                                         							 Timeout value is greater than the Inactivity Timeout value. The customer then gets a message "Sorry, the chat service is currently not available. Please try
                                                            								again later." | Offer Chat Contact When On Voice Call | Click Yes if agents are allowed to handle a chat session during
                                                         							 a voice call. Note This setting takes effect when the agent ends the current voice call. Chats are presented to agents even when they go off-hook or busy in a Non ICD call. | Note | This setting takes effect when the agent ends the current voice call. Chats are presented to agents even when they go off-hook or busy in a Non ICD call. | Offer Voice Call When On Chat | Click Yes if agents are allowed to handle a voice call during a
                                                         							 chat session. Note This setting takes effect when the agent receives a new incoming chat. Direct/Consult Transfer to an IPCC extension is an exception. Even if agents are busy on a chat they would still get calls
                                                                     that are transferred to their extension directly. | Note | This setting takes effect when the agent receives a new incoming chat. Direct/Consult Transfer to an IPCC extension is an exception. Even if agents are busy on a chat they would still get calls
                                                                     that are transferred to their extension directly. | Maximum Number Of Chat Sessions Per Agent | Number of chat sessions (ranging from 1 to 5) that an agent is allowed to
                                                         							 handle. This includes the group chat sessions also. Note This option is available only if Finesse service is activated. For Cisco Finesse Desktop, the value is set to 1. | Note | This option is available only if Finesse service is activated. For Cisco Finesse Desktop, the value is set to 1. | Maximum Number Of Email Sessions Per Agent | Number of Email sessions (ranging from 1 to 5) that an agent is allowed to
                                                         							 handle. | Sticky Email Timeout (Hours) | Specify the amount of time for which an email message waits in a
                                                         							 specific agent CSQ. Sticky email routing (Last-agent email routing) is a mechanism
                                                         							 to route an email message to the agent who handled the last leg of the email
                                                         							 conversation. When
                                                         							 an email message, which is part of an ongoing conversation, comes in and the
                                                         							 agent who handled the last leg of the conversation is not available, then the
                                                         							 email does not wait indefinitely in that agent queue. After the configured time
                                                         							 expires, the email message is placed on the intended CSQ to be handled by any
                                                         							 available agent. Note Last-agent email routing is not available if the customer changes the subject line of the email message. Default = 4 hours, Range = 1 to 120 hours. | Note | Last-agent email routing is not available if the customer changes the subject line of the email message. |
| Field | Description |
| No
                                                         							 Answer Timeout (Seconds) | The
                                                         							 time for an agent to respond to the chat request after which, the chat request
                                                         							 is routed back to the chat queue and for the chat toaster to fade out. This
                                                         							 is applicable for the Group Chat request also. However when the chat is not
                                                         							 accepted, the chat request is not routed back to the chat queue. Note When you use Chrome or Firefox, the browser overrides the chat toaster
                                                                     								notification to fade out in 20 seconds, even if it is configured to a higher
                                                                     								value. | Note | When you use Chrome or Firefox, the browser overrides the chat toaster
                                                                     								notification to fade out in 20 seconds, even if it is configured to a higher
                                                                     								value. |
| Note | When you use Chrome or Firefox, the browser overrides the chat toaster
                                                                     								notification to fade out in 20 seconds, even if it is configured to a higher
                                                                     								value. |
| Join
                                                         							 Timeout (Minutes) | The
                                                         							 time after which the customer initiates a chat and, if an agent is not joined,
                                                         							 the customer gets a message as per the configuration in the Chat Web Form Configuration page. But an agent can
                                                         							 still join the chat after this timeout. The default timeout is one minute and
                                                         							 the maximum timeout value allowed is 60 minutes. |
| Inactivity Timeout (Minutes) | The
                                                         							 customer inactivity time after which, the system ends the chat. This timeout is
                                                         							 on the customer side only. The
                                                         							 agent gets a message "You are alone in the chat room. Click End to close the chat
                                                            								interface." . The
                                                         							 customer gets a message "Warning: the server connection was lost due to an inactivity
                                                            								timeout or connection failure." . Inactivity timeout may also apply to contacts in queue that have
                                                         							 not yet been accepted by agents. This scenario occurs only when the Join
                                                         							 Timeout value is greater than the Inactivity Timeout value. The customer then gets a message "Sorry, the chat service is currently not available. Please try
                                                            								again later." |
| Offer Chat Contact When On Voice Call | Click Yes if agents are allowed to handle a chat session during
                                                         							 a voice call. Note This setting takes effect when the agent ends the current voice call. Chats are presented to agents even when they go off-hook or busy in a Non ICD call. | Note | This setting takes effect when the agent ends the current voice call. Chats are presented to agents even when they go off-hook or busy in a Non ICD call. |
| Note | This setting takes effect when the agent ends the current voice call. Chats are presented to agents even when they go off-hook or busy in a Non ICD call. |
| Offer Voice Call When On Chat | Click Yes if agents are allowed to handle a voice call during a
                                                         							 chat session. Note This setting takes effect when the agent receives a new incoming chat. Direct/Consult Transfer to an IPCC extension is an exception. Even if agents are busy on a chat they would still get calls
                                                                     that are transferred to their extension directly. | Note | This setting takes effect when the agent receives a new incoming chat. Direct/Consult Transfer to an IPCC extension is an exception. Even if agents are busy on a chat they would still get calls
                                                                     that are transferred to their extension directly. |
| Note | This setting takes effect when the agent receives a new incoming chat. Direct/Consult Transfer to an IPCC extension is an exception. Even if agents are busy on a chat they would still get calls
                                                                     that are transferred to their extension directly. |
| Maximum Number Of Chat Sessions Per Agent | Number of chat sessions (ranging from 1 to 5) that an agent is allowed to
                                                         							 handle. This includes the group chat sessions also. Note This option is available only if Finesse service is activated. For Cisco Finesse Desktop, the value is set to 1. | Note | This option is available only if Finesse service is activated. For Cisco Finesse Desktop, the value is set to 1. |
| Note | This option is available only if Finesse service is activated. For Cisco Finesse Desktop, the value is set to 1. |
| Maximum Number Of Email Sessions Per Agent | Number of Email sessions (ranging from 1 to 5) that an agent is allowed to
                                                         							 handle. |
| Sticky Email Timeout (Hours) | Specify the amount of time for which an email message waits in a
                                                         							 specific agent CSQ. Sticky email routing (Last-agent email routing) is a mechanism
                                                         							 to route an email message to the agent who handled the last leg of the email
                                                         							 conversation. When
                                                         							 an email message, which is part of an ongoing conversation, comes in and the
                                                         							 agent who handled the last leg of the conversation is not available, then the
                                                         							 email does not wait indefinitely in that agent queue. After the configured time
                                                         							 expires, the email message is placed on the intended CSQ to be handled by any
                                                         							 available agent. Note Last-agent email routing is not available if the customer changes the subject line of the email message. Default = 4 hours, Range = 1 to 120 hours. | Note | Last-agent email routing is not available if the customer changes the subject line of the email message. |
| Note | Last-agent email routing is not available if the customer changes the subject line of the email message. |
| Step 3 | Click Save to save the changes for the channel parameters. Note If any of
                                                         				  the above parameters are changed during the call center operation, the updated
                                                         				  values are not applied to the existing contacts in the system. The changed
                                                         				  parameters will affect only the new contacts coming into the system. | Note | If any of
                                                         				  the above parameters are changed during the call center operation, the updated
                                                         				  values are not applied to the existing contacts in the system. The changed
                                                         				  parameters will affect only the new contacts coming into the system. |
| Note | If any of
                                                         				  the above parameters are changed during the call center operation, the updated
                                                         				  values are not applied to the existing contacts in the system. The changed
                                                         				  parameters will affect only the new contacts coming into the system. |

| Field | Description |
|---|---|
| No
                                                         							 Answer Timeout (Seconds) | The
                                                         							 time for an agent to respond to the chat request after which, the chat request
                                                         							 is routed back to the chat queue and for the chat toaster to fade out. This
                                                         							 is applicable for the Group Chat request also. However when the chat is not
                                                         							 accepted, the chat request is not routed back to the chat queue. Note When you use Chrome or Firefox, the browser overrides the chat toaster
                                                                     								notification to fade out in 20 seconds, even if it is configured to a higher
                                                                     								value. | Note | When you use Chrome or Firefox, the browser overrides the chat toaster
                                                                     								notification to fade out in 20 seconds, even if it is configured to a higher
                                                                     								value. |
| Note | When you use Chrome or Firefox, the browser overrides the chat toaster
                                                                     								notification to fade out in 20 seconds, even if it is configured to a higher
                                                                     								value. |
| Join
                                                         							 Timeout (Minutes) | The
                                                         							 time after which the customer initiates a chat and, if an agent is not joined,
                                                         							 the customer gets a message as per the configuration in the Chat Web Form Configuration page. But an agent can
                                                         							 still join the chat after this timeout. The default timeout is one minute and
                                                         							 the maximum timeout value allowed is 60 minutes. |
| Inactivity Timeout (Minutes) | The
                                                         							 customer inactivity time after which, the system ends the chat. This timeout is
                                                         							 on the customer side only. The
                                                         							 agent gets a message "You are alone in the chat room. Click End to close the chat
                                                            								interface." . The
                                                         							 customer gets a message "Warning: the server connection was lost due to an inactivity
                                                            								timeout or connection failure." . Inactivity timeout may also apply to contacts in queue that have
                                                         							 not yet been accepted by agents. This scenario occurs only when the Join
                                                         							 Timeout value is greater than the Inactivity Timeout value. The customer then gets a message "Sorry, the chat service is currently not available. Please try
                                                            								again later." |
| Offer Chat Contact When On Voice Call | Click Yes if agents are allowed to handle a chat session during
                                                         							 a voice call. Note This setting takes effect when the agent ends the current voice call. Chats are presented to agents even when they go off-hook or busy in a Non ICD call. | Note | This setting takes effect when the agent ends the current voice call. Chats are presented to agents even when they go off-hook or busy in a Non ICD call. |
| Note | This setting takes effect when the agent ends the current voice call. Chats are presented to agents even when they go off-hook or busy in a Non ICD call. |
| Offer Voice Call When On Chat | Click Yes if agents are allowed to handle a voice call during a
                                                         							 chat session. Note This setting takes effect when the agent receives a new incoming chat. Direct/Consult Transfer to an IPCC extension is an exception. Even if agents are busy on a chat they would still get calls
                                                                     that are transferred to their extension directly. | Note | This setting takes effect when the agent receives a new incoming chat. Direct/Consult Transfer to an IPCC extension is an exception. Even if agents are busy on a chat they would still get calls
                                                                     that are transferred to their extension directly. |
| Note | This setting takes effect when the agent receives a new incoming chat. Direct/Consult Transfer to an IPCC extension is an exception. Even if agents are busy on a chat they would still get calls
                                                                     that are transferred to their extension directly. |
| Maximum Number Of Chat Sessions Per Agent | Number of chat sessions (ranging from 1 to 5) that an agent is allowed to
                                                         							 handle. This includes the group chat sessions also. Note This option is available only if Finesse service is activated. For Cisco Finesse Desktop, the value is set to 1. | Note | This option is available only if Finesse service is activated. For Cisco Finesse Desktop, the value is set to 1. |
| Note | This option is available only if Finesse service is activated. For Cisco Finesse Desktop, the value is set to 1. |
| Maximum Number Of Email Sessions Per Agent | Number of Email sessions (ranging from 1 to 5) that an agent is allowed to
                                                         							 handle. |
| Sticky Email Timeout (Hours) | Specify the amount of time for which an email message waits in a
                                                         							 specific agent CSQ. Sticky email routing (Last-agent email routing) is a mechanism
                                                         							 to route an email message to the agent who handled the last leg of the email
                                                         							 conversation. When
                                                         							 an email message, which is part of an ongoing conversation, comes in and the
                                                         							 agent who handled the last leg of the conversation is not available, then the
                                                         							 email does not wait indefinitely in that agent queue. After the configured time
                                                         							 expires, the email message is placed on the intended CSQ to be handled by any
                                                         							 available agent. Note Last-agent email routing is not available if the customer changes the subject line of the email message. Default = 4 hours, Range = 1 to 120 hours. | Note | Last-agent email routing is not available if the customer changes the subject line of the email message. |
| Note | Last-agent email routing is not available if the customer changes the subject line of the email message. |

| Note | When you use Chrome or Firefox, the browser overrides the chat toaster
                                                                     								notification to fade out in 20 seconds, even if it is configured to a higher
                                                                     								value. |
|---|---|

| Note | This setting takes effect when the agent ends the current voice call. Chats are presented to agents even when they go off-hook or busy in a Non ICD call. |
|---|---|

| Note | This setting takes effect when the agent receives a new incoming chat. Direct/Consult Transfer to an IPCC extension is an exception. Even if agents are busy on a chat they would still get calls
                                                                     that are transferred to their extension directly. |
|---|---|

| Note | This option is available only if Finesse service is activated. For Cisco Finesse Desktop, the value is set to 1. |
|---|---|

| Note | Last-agent email routing is not available if the customer changes the subject line of the email message. |
|---|---|

| Note | If any of
                                                         				  the above parameters are changed during the call center operation, the updated
                                                         				  values are not applied to the existing contacts in the system. The changed
                                                         				  parameters will affect only the new contacts coming into the system. |
|---|---|

| Note | Website developers must localize the accessibility messages of Bubble Chat to ensure that the announcements are in the appropriate
                                          language. |
|---|---|

| Field | Description |
|---|---|
| Name | Name of the chat widget. |
| Description | A brief description. |
| Post Chat Rating | Whether post chat rating is available for the chat. Note Post chat rating can be configured for only bubble chat. | Note | Post chat rating can be configured for only bubble chat. |
| Note | Post chat rating can be configured for only bubble chat. |
| Code | Option to generate the web form code for the configured chat widget. |
| Delete | Option to delete the chat widget. |

| Note | Post chat rating can be configured for only bubble chat. |
|---|---|

| Note | To modify an existing chat widget, click the chat widget name. To delete an existing chat widget, click the delete icon. Ensure that the widget is removed from the customer website before
                                                   deleting the widget. |
|---|---|

| Step 1 | From the Unified CCX Administration menu bar, choose Subsystems > Chat and Email > Chat Widgets . The Chat Widgets web page opens, displaying the information for existing chat widgets. Note During the widget configuration, live preview of the widget is possible. | Note | During the widget configuration, live preview of the widget is possible. |
|---|---|---|---|
| Note | During the widget configuration, live preview of the widget is possible. |
| Step 2 | Click the Add New icon or the Add New button. The Bubble Chat Configuration web page opens. The administrator can configure the messages and labels in any language. |
| Step 3 | In the Widget Details area, specify the following information: Field Description Name Unique name of the chat widget. Description Chat widget description. | Field | Description | Name | Unique name of the chat widget. | Description | Chat widget description. |
| Field | Description |
| Name | Unique name of the chat widget. |
| Description | Chat widget description. |
| Step 4 | Click Next . The Attributes - Branding and Identity area appears. |
| Step 5 | Specify the following information: Section Field Description Font Family Typeface Font family used for the text in the Chat Web Form and chat window. Note The default font family is Helvetica. You can change the font family by either selecting from the drop-down or entering a
                                                                        new name. If the selected font family is not available in the system where from the AppAdmin page is accessed, it will display
                                                                        an alert message. When you enter a new name, ensure that the correct spelling (case sensitive) is used. The system does not
                                                                        indicate if you enter an invalid name. Ensure that you use commonly available fonts so as to make it easy for the customers
                                                                        to view the information. Before proceeding, the administrator should ensure that the selected font family is applied on the
                                                                        Chat Web Form preview. Chat Title Text Title text displayed on the Chat Web Form and Chat Bubble. Text Color Color of the title text. Button Text Text displayed on the button of the Chat Web Form. Color Color of the button. Text Color Color of the text displayed on the button. Agent Message Message Color Background color of the agent message in the chat window. Text Color Color of the agent message text. Note As you specify the attributes, the Preview area dynamically displays the preview of the Chat Web Form and chat window based on your specifications. | Section | Field | Description | Font Family | Typeface | Font family used for the text in the Chat Web Form and chat window. Note The default font family is Helvetica. You can change the font family by either selecting from the drop-down or entering a
                                                                        new name. If the selected font family is not available in the system where from the AppAdmin page is accessed, it will display
                                                                        an alert message. When you enter a new name, ensure that the correct spelling (case sensitive) is used. The system does not
                                                                        indicate if you enter an invalid name. Ensure that you use commonly available fonts so as to make it easy for the customers
                                                                        to view the information. Before proceeding, the administrator should ensure that the selected font family is applied on the
                                                                        Chat Web Form preview. | Note | The default font family is Helvetica. You can change the font family by either selecting from the drop-down or entering a
                                                                        new name. If the selected font family is not available in the system where from the AppAdmin page is accessed, it will display
                                                                        an alert message. When you enter a new name, ensure that the correct spelling (case sensitive) is used. The system does not
                                                                        indicate if you enter an invalid name. Ensure that you use commonly available fonts so as to make it easy for the customers
                                                                        to view the information. Before proceeding, the administrator should ensure that the selected font family is applied on the
                                                                        Chat Web Form preview. | Chat Title | Text | Title text displayed on the Chat Web Form and Chat Bubble. |  | Text Color | Color of the title text. | Button | Text | Text displayed on the button of the Chat Web Form. |  | Color | Color of the button. |  | Text Color | Color of the text displayed on the button. | Agent Message | Message Color | Background color of the agent message in the chat window. |  | Text Color | Color of the agent message text. | Note | As you specify the attributes, the Preview area dynamically displays the preview of the Chat Web Form and chat window based on your specifications. |
| Section | Field | Description |
| Font Family | Typeface | Font family used for the text in the Chat Web Form and chat window. Note The default font family is Helvetica. You can change the font family by either selecting from the drop-down or entering a
                                                                        new name. If the selected font family is not available in the system where from the AppAdmin page is accessed, it will display
                                                                        an alert message. When you enter a new name, ensure that the correct spelling (case sensitive) is used. The system does not
                                                                        indicate if you enter an invalid name. Ensure that you use commonly available fonts so as to make it easy for the customers
                                                                        to view the information. Before proceeding, the administrator should ensure that the selected font family is applied on the
                                                                        Chat Web Form preview. | Note | The default font family is Helvetica. You can change the font family by either selecting from the drop-down or entering a
                                                                        new name. If the selected font family is not available in the system where from the AppAdmin page is accessed, it will display
                                                                        an alert message. When you enter a new name, ensure that the correct spelling (case sensitive) is used. The system does not
                                                                        indicate if you enter an invalid name. Ensure that you use commonly available fonts so as to make it easy for the customers
                                                                        to view the information. Before proceeding, the administrator should ensure that the selected font family is applied on the
                                                                        Chat Web Form preview. |
| Note | The default font family is Helvetica. You can change the font family by either selecting from the drop-down or entering a
                                                                        new name. If the selected font family is not available in the system where from the AppAdmin page is accessed, it will display
                                                                        an alert message. When you enter a new name, ensure that the correct spelling (case sensitive) is used. The system does not
                                                                        indicate if you enter an invalid name. Ensure that you use commonly available fonts so as to make it easy for the customers
                                                                        to view the information. Before proceeding, the administrator should ensure that the selected font family is applied on the
                                                                        Chat Web Form preview. |
| Chat Title | Text | Title text displayed on the Chat Web Form and Chat Bubble. |
|  | Text Color | Color of the title text. |
| Button | Text | Text displayed on the button of the Chat Web Form. |
|  | Color | Color of the button. |
|  | Text Color | Color of the text displayed on the button. |
| Agent Message | Message Color | Background color of the agent message in the chat window. |
|  | Text Color | Color of the agent message text. |
| Note | As you specify the attributes, the Preview area dynamically displays the preview of the Chat Web Form and chat window based on your specifications. |
| Step 6 | Click Next . The Attributes - Post Chat Rating areas open. |
| Step 7 | Specify the following information: Field Description Enable Post Chat Rating If this checkbox is checked, post-chat rating will be available for the chat. The Post Chat Rating column in the Chat Widgets page indicates whether post chat rating is available for a chat. Label Text asking the user to rate the chat experience. Button Text Text displayed on the button that is used to submit the rating. Note The Preview area dynamically displays the preview of the rating window based on the information specified. | Field | Description | Enable Post Chat Rating | If this checkbox is checked, post-chat rating will be available for the chat. The Post Chat Rating column in the Chat Widgets page indicates whether post chat rating is available for a chat. | Label | Text asking the user to rate the chat experience. | Button Text | Text displayed on the button that is used to submit the rating. | Note | The Preview area dynamically displays the preview of the rating window based on the information specified. |
| Field | Description |
| Enable Post Chat Rating | If this checkbox is checked, post-chat rating will be available for the chat. The Post Chat Rating column in the Chat Widgets page indicates whether post chat rating is available for a chat. |
| Label | Text asking the user to rate the chat experience. |
| Button Text | Text displayed on the button that is used to submit the rating. |
| Note | The Preview area dynamically displays the preview of the rating window based on the information specified. |
| Step 8 | Click Next . The User Form Fields and Problem Statements and CSQ Mapping areas open. |
| Step 9 | In the User Form Fields area, specify the following information: From Available Fields , select the desired fields and move it to Selected Fields . To create new fields in addition to the list of available fields, click Add Custom Field , enter the name of the new custom field in the pop-up window and click OK . The new custom field appears in the list of Selected Fields . |
| Step 10 | In the Add problem Statement CSQ mapping area, specify the following information: In Problem Statement Caption , enter the label for the problem statement field. Enter the problem statement for the Chat Web Form and map the problem statement with an existing chat CSQ from the CSQ List drop-down list. To add more problem statements and associate them with a chat CSQ, click Add More . Click the delete icon for a problem statement to delete that problem statement. |
| Step 11 | Click Next . The Chat Messages area appears. |
| Step 12 | Specify the following information: Section Field Description Initialization Messages Widget Wait Message Message displayed to the customer when the customer submits the chat form and waits for an agent to join. Join Time-out Message Message displayed on the chat window to inform the customer that no agent is available currently. In Progress Messages Text for Text Typing Box Text directing the customer to enter a message. This text appears in the text box of the chat window where the customer enters
                                                         messages to be sent. Agent Joined Message Message displayed on the chat window to inform the customer that an agent has joined. This message has the Agent Alias or
                                                         Agent ID. Two text boxes are available to enter text to be displayed before and after the Agent Alias or Agent ID. Agent Left Message Message displayed on the chat window to inform the customer that the agent has left. This message will have the Agent Alias
                                                         or Agent ID. Two text boxes are available to enter text to be displayed before and after the Agent Alias or Agent ID. End Messages Close Chat Confirmation Pop-up message Message displayed on the pop-up window to confirm if the customer wants to close the chat. In the Negative Response and Positive Response text boxes, enter the text to be displayed on the pop-up window buttons that allows the user to either accept or reject the
                                                            chat closure. Close Chat and Download Transcript Confirmation Pop-up Message Message displayed on the pop-up window to inform the customer that the chat has ended and the chat transcript is ready for
                                                         download. In the Negative Response and Positive Response text boxes, enter the text appears on the pop-up window buttons that allows the user to either accept or reject the transcript
                                                            download. Note By default, the enableTranscriptDownload attribute is set to True in the generated chat widget HTML code snippet. Error Messages System Error Message Message displayed to the customer when the chat service is not available to handle chat requests. Connectivity Error Message Message displayed to the customer when the chat is disconnected due to inactivity timeout or connection failure. | Section | Field | Description | Initialization Messages | Widget Wait Message | Message displayed to the customer when the customer submits the chat form and waits for an agent to join. |  | Join Time-out Message | Message displayed on the chat window to inform the customer that no agent is available currently. | In Progress Messages | Text for Text Typing Box | Text directing the customer to enter a message. This text appears in the text box of the chat window where the customer enters
                                                         messages to be sent. |  | Agent Joined Message | Message displayed on the chat window to inform the customer that an agent has joined. This message has the Agent Alias or
                                                         Agent ID. Two text boxes are available to enter text to be displayed before and after the Agent Alias or Agent ID. |  | Agent Left Message | Message displayed on the chat window to inform the customer that the agent has left. This message will have the Agent Alias
                                                         or Agent ID. Two text boxes are available to enter text to be displayed before and after the Agent Alias or Agent ID. | End Messages | Close Chat Confirmation Pop-up message | Message displayed on the pop-up window to confirm if the customer wants to close the chat. In the Negative Response and Positive Response text boxes, enter the text to be displayed on the pop-up window buttons that allows the user to either accept or reject the
                                                            chat closure. |  | Close Chat and Download Transcript Confirmation Pop-up Message | Message displayed on the pop-up window to inform the customer that the chat has ended and the chat transcript is ready for
                                                         download. In the Negative Response and Positive Response text boxes, enter the text appears on the pop-up window buttons that allows the user to either accept or reject the transcript
                                                            download. Note By default, the enableTranscriptDownload attribute is set to True in the generated chat widget HTML code snippet. | Note | By default, the enableTranscriptDownload attribute is set to True in the generated chat widget HTML code snippet. | Error Messages | System Error Message | Message displayed to the customer when the chat service is not available to handle chat requests. |  | Connectivity Error Message | Message displayed to the customer when the chat is disconnected due to inactivity timeout or connection failure. |
| Section | Field | Description |
| Initialization Messages | Widget Wait Message | Message displayed to the customer when the customer submits the chat form and waits for an agent to join. |
|  | Join Time-out Message | Message displayed on the chat window to inform the customer that no agent is available currently. |
| In Progress Messages | Text for Text Typing Box | Text directing the customer to enter a message. This text appears in the text box of the chat window where the customer enters
                                                         messages to be sent. |
|  | Agent Joined Message | Message displayed on the chat window to inform the customer that an agent has joined. This message has the Agent Alias or
                                                         Agent ID. Two text boxes are available to enter text to be displayed before and after the Agent Alias or Agent ID. |
|  | Agent Left Message | Message displayed on the chat window to inform the customer that the agent has left. This message will have the Agent Alias
                                                         or Agent ID. Two text boxes are available to enter text to be displayed before and after the Agent Alias or Agent ID. |
| End Messages | Close Chat Confirmation Pop-up message | Message displayed on the pop-up window to confirm if the customer wants to close the chat. In the Negative Response and Positive Response text boxes, enter the text to be displayed on the pop-up window buttons that allows the user to either accept or reject the
                                                            chat closure. |
|  | Close Chat and Download Transcript Confirmation Pop-up Message | Message displayed on the pop-up window to inform the customer that the chat has ended and the chat transcript is ready for
                                                         download. In the Negative Response and Positive Response text boxes, enter the text appears on the pop-up window buttons that allows the user to either accept or reject the transcript
                                                            download. Note By default, the enableTranscriptDownload attribute is set to True in the generated chat widget HTML code snippet. | Note | By default, the enableTranscriptDownload attribute is set to True in the generated chat widget HTML code snippet. |
| Note | By default, the enableTranscriptDownload attribute is set to True in the generated chat widget HTML code snippet. |
| Error Messages | System Error Message | Message displayed to the customer when the chat service is not available to handle chat requests. |
|  | Connectivity Error Message | Message displayed to the customer when the chat is disconnected due to inactivity timeout or connection failure. |
| Step 13 | Click Next . The Service Hours page appears. |
| Step 14 | In Service Hours area, select one of the following options to configure the business hours. Default (24 hours x 7 days)- Select this option if the contact center works 24 hours and 7 days in a week. Select Calendar- Select this option to configure the business hours. Calendar drop-down is enabled for this selection. |
| Step 15 | Select the desired calendar from the drop-down list and click the View link to preview the calendar details such as Business Hours , Custom Business Days , and Holidays . |
| Step 16 | In the Messages area, specifiy the following: |

| Note | During the widget configuration, live preview of the widget is possible. |
|---|---|

| Field | Description |
|---|---|
| Name | Unique name of the chat widget. |
| Description | Chat widget description. |

| Section | Field | Description |
|---|---|---|
| Font Family | Typeface | Font family used for the text in the Chat Web Form and chat window. Note The default font family is Helvetica. You can change the font family by either selecting from the drop-down or entering a
                                                                        new name. If the selected font family is not available in the system where from the AppAdmin page is accessed, it will display
                                                                        an alert message. When you enter a new name, ensure that the correct spelling (case sensitive) is used. The system does not
                                                                        indicate if you enter an invalid name. Ensure that you use commonly available fonts so as to make it easy for the customers
                                                                        to view the information. Before proceeding, the administrator should ensure that the selected font family is applied on the
                                                                        Chat Web Form preview. | Note | The default font family is Helvetica. You can change the font family by either selecting from the drop-down or entering a
                                                                        new name. If the selected font family is not available in the system where from the AppAdmin page is accessed, it will display
                                                                        an alert message. When you enter a new name, ensure that the correct spelling (case sensitive) is used. The system does not
                                                                        indicate if you enter an invalid name. Ensure that you use commonly available fonts so as to make it easy for the customers
                                                                        to view the information. Before proceeding, the administrator should ensure that the selected font family is applied on the
                                                                        Chat Web Form preview. |
| Note | The default font family is Helvetica. You can change the font family by either selecting from the drop-down or entering a
                                                                        new name. If the selected font family is not available in the system where from the AppAdmin page is accessed, it will display
                                                                        an alert message. When you enter a new name, ensure that the correct spelling (case sensitive) is used. The system does not
                                                                        indicate if you enter an invalid name. Ensure that you use commonly available fonts so as to make it easy for the customers
                                                                        to view the information. Before proceeding, the administrator should ensure that the selected font family is applied on the
                                                                        Chat Web Form preview. |
| Chat Title | Text | Title text displayed on the Chat Web Form and Chat Bubble. |
|  | Text Color | Color of the title text. |
| Button | Text | Text displayed on the button of the Chat Web Form. |
|  | Color | Color of the button. |
|  | Text Color | Color of the text displayed on the button. |
| Agent Message | Message Color | Background color of the agent message in the chat window. |
|  | Text Color | Color of the agent message text. |

| Note | The default font family is Helvetica. You can change the font family by either selecting from the drop-down or entering a
                                                                        new name. If the selected font family is not available in the system where from the AppAdmin page is accessed, it will display
                                                                        an alert message. When you enter a new name, ensure that the correct spelling (case sensitive) is used. The system does not
                                                                        indicate if you enter an invalid name. Ensure that you use commonly available fonts so as to make it easy for the customers
                                                                        to view the information. Before proceeding, the administrator should ensure that the selected font family is applied on the
                                                                        Chat Web Form preview. |
|---|---|

| Note | As you specify the attributes, the Preview area dynamically displays the preview of the Chat Web Form and chat window based on your specifications. |
|---|---|

| Field | Description |
|---|---|
| Enable Post Chat Rating | If this checkbox is checked, post-chat rating will be available for the chat. The Post Chat Rating column in the Chat Widgets page indicates whether post chat rating is available for a chat. |
| Label | Text asking the user to rate the chat experience. |
| Button Text | Text displayed on the button that is used to submit the rating. |

| Note | The Preview area dynamically displays the preview of the rating window based on the information specified. |
|---|---|

| Section | Field | Description |
|---|---|---|
| Initialization Messages | Widget Wait Message | Message displayed to the customer when the customer submits the chat form and waits for an agent to join. |
|  | Join Time-out Message | Message displayed on the chat window to inform the customer that no agent is available currently. |
| In Progress Messages | Text for Text Typing Box | Text directing the customer to enter a message. This text appears in the text box of the chat window where the customer enters
                                                         messages to be sent. |
|  | Agent Joined Message | Message displayed on the chat window to inform the customer that an agent has joined. This message has the Agent Alias or
                                                         Agent ID. Two text boxes are available to enter text to be displayed before and after the Agent Alias or Agent ID. |
|  | Agent Left Message | Message displayed on the chat window to inform the customer that the agent has left. This message will have the Agent Alias
                                                         or Agent ID. Two text boxes are available to enter text to be displayed before and after the Agent Alias or Agent ID. |
| End Messages | Close Chat Confirmation Pop-up message | Message displayed on the pop-up window to confirm if the customer wants to close the chat. In the Negative Response and Positive Response text boxes, enter the text to be displayed on the pop-up window buttons that allows the user to either accept or reject the
                                                            chat closure. |
|  | Close Chat and Download Transcript Confirmation Pop-up Message | Message displayed on the pop-up window to inform the customer that the chat has ended and the chat transcript is ready for
                                                         download. In the Negative Response and Positive Response text boxes, enter the text appears on the pop-up window buttons that allows the user to either accept or reject the transcript
                                                            download. Note By default, the enableTranscriptDownload attribute is set to True in the generated chat widget HTML code snippet. | Note | By default, the enableTranscriptDownload attribute is set to True in the generated chat widget HTML code snippet. |
| Note | By default, the enableTranscriptDownload attribute is set to True in the generated chat widget HTML code snippet. |
| Error Messages | System Error Message | Message displayed to the customer when the chat service is not available to handle chat requests. |
|  | Connectivity Error Message | Message displayed to the customer when the chat is disconnected due to inactivity timeout or connection failure. |

| Note | By default, the enableTranscriptDownload attribute is set to True in the generated chat widget HTML code snippet. |
|---|---|

| Field | Description |
|---|---|
| Holiday | Message displayed on the bubble chat widget to inform the customer during a holiday. |
| Off Hours | Message displayed on the bubble chat widget to inform the customer during non-working hours. |
| Label | Heading text displayed on the bubble chat widget to inform the customer for the business hours details. |

| Step 17 | In the Label for Days of Week area, specify a label for each day of the week. |
|---|---|
| Step 18 | Click Finish . The code for the Chat Web Form is generated and appears onscreen. Note The Chat Web Form that is generated uses JavaScript. You must access this Chat Web Form from a JavaScript enabled browser. | Note | The Chat Web Form that is generated uses JavaScript. You must access this Chat Web Form from a JavaScript enabled browser. |
| Note | The Chat Web Form that is generated uses JavaScript. You must access this Chat Web Form from a JavaScript enabled browser. |
| Step 19 | Click Save Code to File to save the generated code. Click Back to Chat Widgets to go to the main Chat Widgets page. Note You can also generate the code from the main Chat Widgets page by clicking on the Code icon against the chat widget name. The generated code appears on a pop-up window. To save this code, click Save Code to File . | Note | You can also generate the code from the main Chat Widgets page by clicking on the Code icon against the chat widget name. The generated code appears on a pop-up window. To save this code, click Save Code to File . |
| Note | You can also generate the code from the main Chat Widgets page by clicking on the Code icon against the chat widget name. The generated code appears on a pop-up window. To save this code, click Save Code to File . |

| Note | The Chat Web Form that is generated uses JavaScript. You must access this Chat Web Form from a JavaScript enabled browser. |
|---|---|

| Note | You can also generate the code from the main Chat Widgets page by clicking on the Code icon against the chat widget name. The generated code appears on a pop-up window. To save this code, click Save Code to File . |
|---|---|

| Note | In cases where the website is comprises more than one page, ongoing chats might get disconnected when the user navigates from
                                                one page to another. |
|---|---|

| Note | Customer must have configured JAWS and enabled Accessibility mode in their system to experience the accessibility feature. |
|---|---|

| Step 1 | From the Unified CCX Administration menu bar, choose Subsystems > Chat and Email > Chat - Facebook Messenger . |
|---|---|
| Step 2 | In Configure Token from Facebook , enter the Facebook Page Access Token . This access token is generated on the Facebook App page when the Facebook App is created. |
| Step 3 | In HTTP Proxy , enable HTTP Proxy and provide valid values for the HTTP Proxy . |
| Step 4 | Click Validate to ensure that the token is valid using HTTP Proxy (if provided). |
| Step 5 | In Problem Statements and CSQ Mapping , enter Problem Statement Caption . |
| Step 6 | Enter problem statement and select CSQ from the dropdown list. Click Add More to add problem statements and CSQs. You can add a maximum number of three (3) problem statements. |
| Step 7 | In Chat Messages , you can edit the existing messages as per your business requirement. The following table describes the messages that a Facebook
                                          Messenger user would see: Section Field Description Initialization Messages Welcome Message This message welcomes the user when a chat session is initiated. The user can select a problem statement from the list. In Progress Messages Wait Message This message informs the user to wait until an agent joins the chat. Join Timeout Message This message informs the user to continue to wait or try again later. End Messages End Message This message informs the user that the chat session has ended. No Agent Available This message informs the user that no agent is available. Error Messages Unsupported Content Message This message informs the user that any attachments other than text formats are not supported. Unknown Error This message informs the user about any unknown internal error. Inactivity Timeout Message This message informs the user that the chat session has ended due to inactivity. | Section | Field | Description | Initialization Messages | Welcome Message | This message welcomes the user when a chat session is initiated. The user can select a problem statement from the list. | In Progress Messages | Wait Message | This message informs the user to wait until an agent joins the chat. | Join Timeout Message | This message informs the user to continue to wait or try again later. | End Messages | End Message | This message informs the user that the chat session has ended. | No Agent Available | This message informs the user that no agent is available. | Error Messages | Unsupported Content Message | This message informs the user that any attachments other than text formats are not supported. | Unknown Error | This message informs the user about any unknown internal error. | Inactivity Timeout Message | This message informs the user that the chat session has ended due to inactivity. |
| Section | Field | Description |
| Initialization Messages | Welcome Message | This message welcomes the user when a chat session is initiated. The user can select a problem statement from the list. |
| In Progress Messages | Wait Message | This message informs the user to wait until an agent joins the chat. |
| Join Timeout Message | This message informs the user to continue to wait or try again later. |
| End Messages | End Message | This message informs the user that the chat session has ended. |
| No Agent Available | This message informs the user that no agent is available. |
| Error Messages | Unsupported Content Message | This message informs the user that any attachments other than text formats are not supported. |
| Unknown Error | This message informs the user about any unknown internal error. |
| Inactivity Timeout Message | This message informs the user that the chat session has ended due to inactivity. |
| Step 8 | In Post Chat Rating , you can enable Post Chat Rating so that customer can rate the chat experience on a scale of 1 (worst) to 5 (best). You can
                                          edit the existing messages as per your business requirement. The following table describes the messages that the Facebook
                                          Messenger user would see: Section Field Description Post Chat Rating Rating Offer Message This message informs the user that the chat experience can be rated. The user can select one of the ratings from 1 (worst)
                                                         to 5 (best). Rating Completed Message This message informs the user that the rating was sucessfully submitted. | Section | Field | Description | Post Chat Rating | Rating Offer Message | This message informs the user that the chat experience can be rated. The user can select one of the ratings from 1 (worst)
                                                         to 5 (best). | Rating Completed Message | This message informs the user that the rating was sucessfully submitted. |
| Section | Field | Description |
| Post Chat Rating | Rating Offer Message | This message informs the user that the chat experience can be rated. The user can select one of the ratings from 1 (worst)
                                                         to 5 (best). |
| Rating Completed Message | This message informs the user that the rating was sucessfully submitted. |
| Step 9 | In Webhooks Update in Facebook , ensure that the Facebook Verification token and configured Callback URL are updated in the Facebook App. Note If you have modified tokens, restart Customer Collaboration Platform Chat Gateway Service for the changes to take effect. | Note | If you have modified tokens, restart Customer Collaboration Platform Chat Gateway Service for the changes to take effect. |
| Note | If you have modified tokens, restart Customer Collaboration Platform Chat Gateway Service for the changes to take effect. |
| Step 10 | In Enable Integration , check or uncheck the check box to enable or disable the integration of Facebook Messenger with Unified CCX respectively. |
| Step 11 | Click Save to save settings. |

| Section | Field | Description |
|---|---|---|
| Initialization Messages | Welcome Message | This message welcomes the user when a chat session is initiated. The user can select a problem statement from the list. |
| In Progress Messages | Wait Message | This message informs the user to wait until an agent joins the chat. |
| Join Timeout Message | This message informs the user to continue to wait or try again later. |
| End Messages | End Message | This message informs the user that the chat session has ended. |
| No Agent Available | This message informs the user that no agent is available. |
| Error Messages | Unsupported Content Message | This message informs the user that any attachments other than text formats are not supported. |
| Unknown Error | This message informs the user about any unknown internal error. |
| Inactivity Timeout Message | This message informs the user that the chat session has ended due to inactivity. |

| Section | Field | Description |
|---|---|---|
| Post Chat Rating | Rating Offer Message | This message informs the user that the chat experience can be rated. The user can select one of the ratings from 1 (worst)
                                                         to 5 (best). |
| Rating Completed Message | This message informs the user that the rating was sucessfully submitted. |

| Note | If you have modified tokens, restart Customer Collaboration Platform Chat Gateway Service for the changes to take effect. |
|---|---|

| Note | The team
                                             			 configuration for chat is the same as it is for voice. |
|---|---|

| Note | It is mandatory to configure the SIP Gateway used by the Outbound
                                             			 subsystem to place calls in case of IVR-based and agent-based progressive and
                                             			 predictive Outbound campaigns. |
|---|---|

| Step 1 | From the
                                          			 Unified CCXAdministration menu bar, choose Subsystems > Outbound > SIP Gateway
                                                				  Configuration . The SIP
                                             				Gateway Configuration web page opens. |
|---|---|
| Step 2 | Click Update to save the configuration changes. The new SIP
                                             				gateway configuration is added to the Unified CCX system. |
| Step 3 | Click Cancel to restore the default settings. |

| Field | Description |
|---|---|
| Gateway Configuration |
| Gateway
                                                						Hostname/IP Address | The
                                                						HostName or IP Address of the SIP Gateway in the Unified CCX server, which will
                                                						be used by the Outbound subsystem to place calls for the predictive or
                                                						progressive campaigns. |
| Gateway Port | Destination port used by Unified CCX to communicate with SIP gateway. The default value is 5060. |
| Local CCX Port | Destination port to be used by SIP gateway to communicate with Unified CCX. You cannot edit this field. Default value is as follows: Fresh install: 5065 Upgrade: Previously configured value. If not configured, 5065 is displayed. If you have configured a value other than 5065, you can restore to the default value by using the Restore Default button. |
| Local User Agent | This read-only field provides a description of the owner for this connection. The default value is Cisco-UCCX. |
| Transport(TCP/UDP) | The
                                                						protocol required to send SIP messages. You can select any one of the following
                                                						protocols: TCP
                                                      							 - Transport Control Protocol or UDP
                                                      							 - User Datagram Protocol The
                                                						default value is UDP. |
| Call Progress Analysis
                                                   						  Configuration (displays the parameter name, parameter value, and suggested
                                                   						  value for the following fields) |
| Minimum
                                                						Silence Period (10-1000) | The
                                                						amount of time that the signal must be silent after speech detection to declare
                                                						a live voice (in milliseconds). Default
                                                						= 375 milliseconds, Range = 10-1000 milliseconds |
| Analysis
                                                						Period (1000 - 10000) | Maximum
                                                						amount of time (from the moment the system first detects the speech) during
                                                						which analysis will be performed on the input audio. Default
                                                						= 2500 milliseconds, Range = 1000-10000 milliseconds |
| Maximum
                                                						Time Analysis (1000-10000) | The
                                                						amount of time to wait when it is difficult for the dialer to determine voice
                                                						or answering machine. Default
                                                						= 3000 milliseconds, Range = 1000-10000 milliseconds |
| Minimum
                                                						Valid Speech Time (50-500) | Amount of time that
                                                						the signal must be active before being declared speech. Anything less is
                                                						considered as a glitch. Default
                                                						= 112 milliseconds, Range = 50-500 milliseconds |
| Maximum
                                                						Term Tone Analysis (1000-60000) | This is
                                                						the amount of time the gateway will look for a terminating beep once an
                                                						answering machine has been detected. Default
                                                						= 15000 milliseconds, Range = 1000-60000 milliseconds |

| Note | This is a global configuration to restrict the gateway from hunting for all 403 forbidden error messages. |
|---|---|

| Note | You can use either of the below two supported methods to modify a dialed number in the gateway: To remove the initial digits of the phone number use forward-digits or digit-strip in the dial peer configuration. To add a prefix to the phone number use prefix in the dial peer configuration. |
|---|---|

| Click 
                                             		  the Add New icon that displays in the toolbar in
                                             		  the upper left corner of the window or the button that displays at the bottom
                                             		  of the window to add a new data source. The DataSource Configuration web page opens. |
|---|

| Choose Subsystems > Database > Parameter from the Unified CCX
                                          			 Administration menu bar. The Parameters
                                             				web page displays. See Poll Database Connectivity to know more about how to update
                                             				parameter-related fields. |
|---|

| Step 1 | From the Unified
                                          			 CCXAdministration menu bar, choose Subsystems > Database > Drivers . The Driver List web page opens up displaying a list of uploaded driver class filenames along with a Delete icon. |
|---|---|
| Step 2 | Click the Add
                                             				New icon that displays in the toolbar in the upper left corner of
                                          			 the window or the Add
                                             				New button that displays at the bottom of the window to add a new
                                          			 driver class name. The Driver
                                             				Management web page opens. |
| Step 3 | Specify a valid
                                          			 JDBC driver jar file in the Driver File field or click Browse to locate the driver file. The driver file
                                             				is validated before uploading. |
| Step 4 | Choose the
                                          			 supported class name for the new driver from the Driver Class Name drop-down
                                          			 list box. |
| Step 5 | Click Upload to save the new driver to the database. Tip For details on the compatible Enterprise database server version see, https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . Ensure that a valid JDBC driver version is used that is compatible with the Enterprise database server. Contact your database vendor to know the appropriate JDBC driver versions that is compatible with your Enterprise database
                                                               server. While uploading com.ibm.db2.jcc.DB2Driver, if your IBM DB2 deployment also requires a license Jar to be in the application's
                                                               classpath, upload the license Jar as a Custom Jar File using the procedure detailed in Specify Custom Classpath Entries . Then, restart the Unified CCX Engine on all nodes through the Unified CCX Serviceability. | Tip | For details on the compatible Enterprise database server version see, https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . Ensure that a valid JDBC driver version is used that is compatible with the Enterprise database server. Contact your database vendor to know the appropriate JDBC driver versions that is compatible with your Enterprise database
                                                               server. While uploading com.ibm.db2.jcc.DB2Driver, if your IBM DB2 deployment also requires a license Jar to be in the application's
                                                               classpath, upload the license Jar as a Custom Jar File using the procedure detailed in Specify Custom Classpath Entries . Then, restart the Unified CCX Engine on all nodes through the Unified CCX Serviceability. |
| Tip | For details on the compatible Enterprise database server version see, https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . Ensure that a valid JDBC driver version is used that is compatible with the Enterprise database server. Contact your database vendor to know the appropriate JDBC driver versions that is compatible with your Enterprise database
                                                               server. While uploading com.ibm.db2.jcc.DB2Driver, if your IBM DB2 deployment also requires a license Jar to be in the application's
                                                               classpath, upload the license Jar as a Custom Jar File using the procedure detailed in Specify Custom Classpath Entries . Then, restart the Unified CCX Engine on all nodes through the Unified CCX Serviceability. |

| Tip | For details on the compatible Enterprise database server version see, https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-device-support-tables-list.html . Ensure that a valid JDBC driver version is used that is compatible with the Enterprise database server. Contact your database vendor to know the appropriate JDBC driver versions that is compatible with your Enterprise database
                                                               server. While uploading com.ibm.db2.jcc.DB2Driver, if your IBM DB2 deployment also requires a license Jar to be in the application's
                                                               classpath, upload the license Jar as a Custom Jar File using the procedure detailed in Specify Custom Classpath Entries . Then, restart the Unified CCX Engine on all nodes through the Unified CCX Serviceability. |
|---|---|

| Click 
                                          		  the Add New icon or button on the HTTP Trigger
                                          		  Configuration web page to access the HTTP Trigger Configuration web page. To modify an existing trigger, click any hyperlink within
                                             		  the HTTP Trigger List table; the HTTP Trigger Configuration web page opens. |
|---|

| Note | You must have a MRCP ASR Provider defined before you can provision a
                                             			 MRCP ASR Server. |
|---|---|

| Note | You must have a MRCP ASR Provider defined before you can provision a
                                             			 MRCP ASR Group. |
|---|---|