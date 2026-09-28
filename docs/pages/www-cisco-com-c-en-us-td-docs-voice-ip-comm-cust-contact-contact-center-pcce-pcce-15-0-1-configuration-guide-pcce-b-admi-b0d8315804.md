---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-configuration-guide-pcce-b-admi-b0d8315804
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/configuration/guide/pcce_b_admin-and-config-guide-15_0_1/pcce_m_post-installation-configuration_15_0.html
retrieved_at: 2026-08-25T01:21:33.774715+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Post Installation Configuration

## Chapter: Post Installation Configuration

# Post Installation Configuration

## CCEDataProtect Tool

The CCEDataProtect tool is used to encrypt and decrypt sensitive information in SQLLogin registry key located at HKEY_LOCAL_MACHINE\SOFTWARE\Cisco.System,INC.\ICM\<instancename>\RouterA\Router\CurrentVersion\Configuration\Database . The CallRouter uses the external database lookup value in SQLLogin registry to authenticate and access the remote database.

You must specify the following value in the CCEDataProtect Tool on the CallRouter for SQLLogin registry key:

If you are using a custom SQL Server port for external database, you must specify the following value in the CCEDataProtect
                              tool on the CallRouter for the SQLLogin registry key:

Use a comma as the delimiter to separate data for separate databases.

The following example shows login credentials for two external databases:

The following example shows login credentials for two external databases when using a custom SQL Server port:

Important

The SQLLogin key does not support passwords that contains the following characters:

'/', '\', '=', '(', ')', or ','

Only the administrator, domain user with administrator rights, or a local administrator can run the CCE DataProtect Tool,
                                             using <Install Directory>:\icm\bin\CCEDataProtectTool.exe.

You must run the CCEDataProtect Tool on every server where DBLookup functionality is used.

DBLookup password must contain only ASCII characters.

Following are the features supported with the CCEDataProtect Tool:

DBLookUp - view and edit External DBLookUp SQLLogin registry value.

DBLookUp supports the following options:

Decrypt and View - to view the encrypted password stored in the SQLLogin registry as clear text.

Edit and Encrypt - to configure the registry with encrypted value for first time or edit the existing encrypted value stored in the registry. Only password containing ASCII characters are supported for encryption.

Help - information about the DBLookUp options.

Exit - to return to the initial menu.

Rekey - use this functionality with the Common Ground upgrade to re-encrypt the encrypted values based on upgraded software version.
                                 For Technology Refresh upgrade, you must reconfigure the value in the destination machine using the Edit and Encrypt option. It is recommended to use the Rekey option to secure the sensitive information.

Important

Rekey option will be supported in the future releases only.

Help - information about the CCEDataProtect Tool options.

Exit - to exit the CCEDataProtect Tool.

### Configure External DBLookUp Registry Value using CCEDataProtect Tool

Perform this procedure to configure the External DBLookUp registry value using the CCEDataProtect Tool. For more information about CCEDataProtect Tool, see CCEDataProtect Tool .

Step 1

Run the CCEDataProtect Tool located at <Install Directory>:\icm\bin\CCEDataProtectTool.exe , on every server where DBLookup operations are set up.

Step 2

In the Main menu, press 1 to select DBLookUp , and press Enter .

Step 3

Enter a valid Instance Name for which this option is configured.

You can run only one instance of CCEDataProtect Tool at a time.

Step 4

Press 2 to select Edit and Encrypt , and press Enter .

The tool displays the current encrypted value stored in the registry as clear text, if it is already configured.

Enter a new Registry Value at the system prompt, and press Enter .

The maximum limit for the External DBLookUp registry entry is 2048 characters.

If you press Enter without entering any value, the system removes the encrypted value stored in the registry. You can use this option to remove
                                                               the encrypted entry.

When the system displays the message: Are you sure you want to Edit the Registry Details [Y/N] , press Y and then press Enter .

The system updates the Registry with an encrypted value and the system prompts the message: Registry Updated with Encrypted Data Successfully .

Step 5

Press 1 to select Decrypt and View , to verify the encrypted password.

CCEDataProtect Tool generates the following logs in the C:\temp folder.

CCEDataProtectTool.log - captures the tool usage by the administrator.

CCEDataProtectTool_audit.log - captures the audit details of the tool usage.

## Packaged CCE 2000 Agents Deployment

Follow this sequence to configure components for Packaged CCE 2000 Agents deployment.

Sequence

Task

1

Generate CSR and upload CA Certificates

Or

Generate and import Self-signed Certificates

2

Configure CCE Component

3

Configure Cisco Unified Customer Voice Portal

4

If Media Server is external, Configure Media Server

5

Configure Cisco Unified Communications Manager

6

Configure Cisco Unified Intelligence Center

7

Configure Cisco Finesse

8

Configure Cisco Identity Service

9

Configure Cisco Unified Customer Voice Portal Reporting Server (optional)

10

Configure VVB (optional)

11

Configure Cisco IOS Enterprise Voice Gateway

12

Configure IPv6

13

Configure Enterprise Chat and Email (ECE) (optional)

Email and Chat

### Configure CCE Component

Follow this sequence to configure the core CCE components.

Sequence

Task

1

Configure SQL Server for CCE Components

2

Set up Organizational Units

3

Initialize the Packaged CCE 2000 Agents Deployment Type

4

Add PIMs to the Media Routing Peripheral Gateway (optional)

5

Cisco SNMP Setup (optional)

6

Modify Logger

#### Configure SQL Server
                              	 for CCE Components

The following procedure must be done in Logger, Rogger, and AW Machines.

Step 1

Open Microsoft SQL Server Management Studio .

Step 2

Log in.

Step 3

Expand Security and then Logins .

Step 4

If the
                                             			 BUILTIN\Administrators group is not listed:

Right-click Logins and select New Login .

Click Search and then Locations to locate BUILTIN in the domain tree.

Type Administrators and click Check Name and then OK .

Double-click BUILTIN\Administrators .

Choose Server Roles .

Ensure
                                                   				  that public and sysadmin are both checked.

## Set up Organizational Units

### Add a Domain

Step 1

Log in with a Domain Administrator privilege.

Step 2

Open the Domain Manager Tool from Unified CCE Tools
                                          					shortcut on your desktop.

Step 3

Click Select . under Domains .

Step 4

You can add domains through the Select Domains dialog
                                          					box, or you can add a domain manually if the target domain cannot be detected
                                          					automatically.

To add domains by using the controls in the Select Domains dialog box:

In the left pane under Choose domains, select one or more domains.

Click Add to add the selected domains, or click Add All to add all the domains.

To add a domain manually:

In the field under Enter domain name, enter the fully qualified domain
                                                							name to add.

Click Add .

Click OK .

### Add Organizational
                           	 Units

Use the Domain
                                 		  Manager tool to create the Cisco root Organizational Unit (OU) for a domain,
                                 		  and then create the facility and instance OUs.

The system
                                 		  software always uses the root OU named Cisco_ICM. You can place the Cisco_ICM
                                 		  OU at any level within the domain where the Unified ICM Central Controller is
                                 		  installed. The system software components locate the root OU by searching for
                                 		  this name.

The user who
                                 		  creates the Cisco Root OU automatically becomes a member of the Setup Security
                                 		  Group for the Cisco Root OU. In effect, this user is granted privileges to all
                                 		  Unified CCE tasks in the domain.

Step 1

Log in with a domain administrator privilege and open the Domain Manager Tool from Unified CCE Tools shortcut on the desktop.

Step 2

Choose the
                                          			 domain.

Step 3

If this OU is the first instance, then perform the following steps to add the Cisco_ICM root:

Under
                                                				  Cisco root, click Add .

Select the
                                                				  OU under which you want to create the Cisco root OU, then click OK .

When you
                                                   					 return to the Domain Manager dialog box, the Cisco root OU appears either at
                                                   					 the domain root or under the OU you selected. You can now add the facility.

Step 4

Add the
                                          			 facility OU:

Select the
                                                				  Cisco Root OU under which you want to create the facility OU.

In the
                                                				  right pane, under Facility, click Add .

Enter the
                                                				  name for the Facility, and click OK .

Step 5

Add the
                                          			 instance OU:

Navigate
                                                				  to and select the facility OU under which you want to create the instance OU.

In the
                                                				  right pane, under Instance, click Add .

Enter the
                                                				  instance name and click OK .

Step 6

Click Close .

### Add Users to Security Groups

To add a domain user to a security group, use this procedure. The user is then granted the user privileges to the functions
                                 that are controlled by that security group.

Step 1

Open the Domain Manager tool and select the Security Group ( Config or Setup ) you want to add a user to.

Step 2

Under Security group, click Members .

Step 3

Under Users, click Add .

Step 4

Select the domain of the user you want to add.

Step 5

(Optional) In the Optional Filter field, choose to further filter by the Name or  User Logon Name, apply the search condition, and enter the search value.

Step 6

Click Search .

Step 7

Select the member you want to add to the Security Group from the search results.

Step 8

Click OK .

### Add Users to Local Administrators Group

You can add a domain group to local Administrators group of the server to provide users in domain group administrative permission
                                             on the server, provided the users are immediate members of the domain group.

Step 1

Click Server Manager > Tools > Computer Management .

Step 2

Select Local Users and Groups .

Step 3

Double-click Groups .

Step 4

Right-click Administrators . Select Properties .

Step 5

Click Add and enter the user name or domain group name in the Edit the Object names to select check box.

Step 6

Select Check Names to validate the names.

Step 7

After the name is successfully validated, click OK .

Step 8

Click Apply and OK in the Properties dialog box.

Step 9

Close the Computer Management and Server Manager windows.

## Initialize the Packaged CCE 2000 Agents Deployment Type

When you sign into Unified CCE Administration for the first time, you are prompted to enter information and credentials for
                              the components in your deployment. Packaged CCE uses this information to configure the components and build the System Inventory.

If you are in the process of upgrading from an earlier release, Packaged CCE prompts you only for missing information and
                              credentials; you may not need to perform each step.

Once a Packaged CCE deployment is initialized, you cannot switch to another Packaged CCE deployment type, including Packaged
                                          Lab Mode. However, you can switch to a Unified CCE deployment type.

Important

Packaged CCE 2000 Agents deployments on Nutanix are supported only after Release 15.0(1)SU2/ES202607 or a later Engineering
                                          Special is installed. The initialization workflow depends on the Engineering Special installed. Before the ES, use the VMware
                                          VM Host workflow. After 15.0(1) SU2/ES202607 or a later Engineering Special is installed, initialize a VMware-based or Nutanix-based
                                          deployment by importing the Packaged CCE 2000 Agents inventory file.

Once a Packaged CCE deployment is initialized, you cannot switch to a different Packaged CCE deployment type. However, you
                                 can switch to a Unified CCE deployment type. After this deployment switching, you must ensure to follow the below listed important
                                 considerations:

Component

Important Considerations

Unified CCE

Retains any existing departments and their associations. Allows you to maintain associations within the same department.

Any new department created thereafter will be considered Global.

Finesse

Disables the automatic synchronization of Reason Labels and Teams, and enables the Reasons gadget within Finesse Administration.

Unified Intelligence Center

Disables the automatic creation of supervisor accounts and team collections in Unified Intelligence Center enables AW database
                                             synchronization.

Unified Unified CVP

Virtualized Voice Browser

OAMP needs to be newly built, and all Unified CVP and Cisco VVB configurations need to be manually set up from the beginning.

Step 1

Sign into Unified CCE Administration using the Active Directory username ( user@domain ) and password ( https://< IP Address >/cceadmin , where <IP Address> is the address of the Side A Unified CCE AW-HDS-DDS ).

Step 2

On the Deployment Type page , select a Deployment Type and an Instance from the respective drop-down lists. Be a member of the Setup security group for the instance you select. Click Next .

Step 3

Complete the substep that applies to the Engineering Special installed in your deployment.

For VMware and Nutanix deployments with 15.0(1) SU2/ES202607 or a later ES installed, complete the following actions:

On the Configure your deployment page, click Download Template to download the Packaged CCE 2000 Agent inventory template.

Fill out and save the template to your computer.

For more information on completing the template, see Inventory Content File .

Click Content File to upload the completed file.

Click Next .

The VM Host and Credentials pages are not displayed after 15.0(1) SU2/ES202607 or a later ES is installed.

For VMware deployments running a version earlier than 15.0(1) SU2/ES202607, complete the following steps.

On the VM Host page, enter the IP address, Username, and Password for the VMware hosts for Side A and Side B.

The VMware hosts are the two servers on which ESXi is installed. The username and password fields are the host login names
                                                      and passwords configured in ESXi.

Considerations :

User Credentials and Permissions :

If you do not want to use the "root" user credentials. You can create user with the Read and Reboot permissions on the hosts. To enable these permissions in the VMware Host Client, set the following in Manage Permissions .

Anonymous , View , and Read in Root > System (enabled by default).

Reset in Root > VirtualMachine > Interact

If you update the ESXi root password in Packaged CCE 2000 agent deployment, be sure to reinitialize the deployment in the
                                                                  Inventory page.

Validation

The system validates the hardware specifications of the VMware host and verifies if the VMs are configured as per the reference
                                                            design. If the validation is successful, click Next to open the Credentials page. See the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html for hardware specifications.

If the validation fails, click Update Hosts to go back to the VM Hosts page and edit the values. Click Retry to run the validation with existing values.

Datastores :

Datastores used by Cisco VMs should not be shared or used by other third-party VMs.

Core Components :

Packaged CCE core components include:

Unified CCE Rogger

Unified CCE AW/HDS/DDS

Unified CCE PG

Unified CVP Server

Finesse

Unified Intelligence Center Publisher (with coresident Live Data and Cisco IdS)

VM annotations are used to identify Packaged CCE core component VMs. Do not change the default annotations of any of the core
                                                                  component VMs. The following terms are reserved for core component annotations: Cisco, Finesse, Unified Intelligence Center,
                                                                  and Unified CVP. Do not use these reserved terms in the annotations of any of the noncore component VMs.

Core components must be on-box, all other components have to be added as external machines. For more information, see the Add External Machines topic in the Packaged CCE Administration and Configuration Guide, Release 11.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html

All other non-core components are required to be added as an external machine in the Packaged CCE Inventory.

On the Credentials page, enter the specified information for each component in your deployment. After entering information for a component,
                                                      click Next .

The system validates the credentials that you entered before prompting you for the next component's information.

Unified CM

Either:

The Unified CM Publisher for an on-box Unified Communications Manager deployment.

The Unified CM Publisher Name and IP address for an external Unified Communications Manager deployment.

Only a single Unified CM cluster can be integrated to a single site of Packaged CCE deployment.

AXL username and password.

Unified CVP

Unified CVP Server (Side A) Windows Administration Username and Password.

Unified CVP Server (Side B) Windows Administration Username and Password.

Unified CCE AW-HDS-DDS

Unified CCE Diagnostic Framework Portico domain, username, and password.

These credentials must be of a domain user who is a local administrator on all the CCE servers and valid on all Unified CCE
                                                                  components in your deployment (the Side A and Side B Unified CCE Roggers, PGs, and AW-HDS-DDSs).

Every time the Active Directory credentials are updated, the credentials configured here must be updated as well.

Unified Intelligence Center

Unified Intelligence Center Administration application username and password.

Identity Service Administration username and password.

Finesse

Finesse Administration username and password.

Unified CVP Reporting

Unified CVP Reporting Server Windows Administration Username and Password used during server installation.

Step 4

On the Settings page, select the following:

Select the codec used for Mobile Agent calls from the Mobile Agent Codec drop-down menu. The codec you select must match the codec specified on the voice gateways.

If you have an external Unified Communications Manager, select the Unified CM Subscribers to which the Side A and Side B
                                                Unified CCE PGs connect from the Side A Connection and Side B Connection drop-down menus.

Enter the username and password for an existing Active Directory user in the same domain as the Packaged CCE servers. This
                                                account will be added to the Service group.

Click Next .

See Automated Initialization Tasks for Components for more information.

Step 5

After the automated initialization tasks complete, click Done .

If one of the automated initialization tasks fails, correct the errors and then click Retry .

If the retry is successful, the automated initialization continues.

For some task failures, all completed tasks must be reverted before the task can be retried. You see a message informing you
                                          that the system needs to be reverted to a clean state.

Click OK , and then after the system is in a clean state, click Start Over .

After ES202607 or a later Engineering Special is installed, VM host validation alerts are not generated.

### What to do next

After you have configured the deployment, you can specify system-level settings. For example, you can enter labels for Unified
                              Communications Manager, Unified CVP, and outbound calls. See Miscellaneous .

### Automated Initialization Tasks for Components

Packaged CCE
                              	performs the following tasks during initialization.

Unified CCE Rogger

Creates the Logger.

Creates the Logger database, data size of 130GB and the log
                                                		size of 3GB.

Creates the Router.

Unified CCE PG

Downloads JTAPI from the Unified Communications Manager, and
                                                		installs it on the Unified CCE PG.

Creates the CUCM Peripheral Gateway (PG) with the CUCM PIM.

Creates the Media Routing PG (MR PG).

Creates the VRU PG with two VRU PIMs.

Creates the CTI Server.

Unified CCE AW-HDS-DDS

Creates the AW-HDS-DDS.

Creates the AW database, data size of 1.4GB and log size of 100MB.

Creates the historical database, data size of 450GB and log size of 3GB

Creates the Cisco Unified Intelligence Center SQL user account
                                                			that is used for Unified Intelligence Center data sources.

Creates the Cisco Finesse SQL user account that is used for
                                                			Cisco Finesse data sources.

Outbound

Creates the Outbound database, data size of 1.4GB and log size of 100MB.

Unified
                                          			Communications Manager

Creates the Application User that is used to configure the
                                                				Unified CCE PG.

Unified
                                          			Customer Voice Portal

Configures the Unified CVP Call Server.

Configures the Unified CVP VXML Server.

Configures the Unified CVP Media Server.

Unified CVP Reporting Server

Initializes the Unified CVP Reporting Server.

Unified
                                          			Intelligence Center

Updates the historical and real-time data sources.

Disables the AW database synchronization

Cisco Finesse

Configures the CTI Server settings.

Configures the connection to the AW database.

Disables the Reasons gadget in Finesse Administration.

### System Inventory for Packaged CCE 2000 Agents Deployment

After the ES 15.0(1) SU2/ES202607 patch is applied, for Nutanix-based and VMware-based deployments, the system does not support
                                             auto-discovery. Inventory management for these environments is handled exclusively through the CSV import process (For more
                                             information, see Initialize the Packaged CCE 2000 Agents Deployment Type ). Periodic inventory validation is turned off for both VMware and Nutanix platforms.

The System Inventory is a visual display of the machines in your deployment, including: Virtual Machine Hosts (ESXi servers),
                                 Virtual Machines (VMs) on Side A, VMs on Side B, External Machines, Gateways, and Cisco Virtualized Voice Browsers (VVB).
                                 You can access the System Inventory after you have completed the change to a Packaged CCE deployment.

Access the System Inventory by navigating to Unified CCE Administration > Infrastructure > Inventory .

For more details about the Packaged CCE requirements, see the Server Status pop-up window, see Monitor Server Status Rules for Packaged CCE 2000 Agents Deployment .

Location

This column indicates that the VMs are either on OnBox Side A , OnBox Side B , or OffBox ( External Machine ).

All VMs on Side A are indicated as OnBox Side A in the Location column.

The System Inventory displays read-only information for the following VMs:

Unified CCE Rogger

Unified CCE PG

Unified CM Subscriber 1 (if on-box)

To edit the following VMs, click on the respective rows:

If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory.

Unified CCE AW-HDS-DDS —Diagnostic Framework Service Domain, Username, and Password.

Unified CM Publisher (if on-box)—AXL Username and Password. These are the credentials for connecting to the Unified CM Publisher.

CUIC-LD-IdS Publisher —Username and Password for Unified Intelligence Center Administration. Username and Password for Identity Service Administration.

Unified CVP Server — Unified CVP Server Windows credentials. Configure FTP.

For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine .

Finesse Primary —Username and Password for Cisco Finesse Administration.

You can launch the administration tool for these VMs by clicking the VM arrow icon:

CUIC-LD-IdS Publisher

Unified CM Publisher

You can perform the full synchronization or differential synchronization of the configurations of various components. For
                                             more information on the machines that support data synchronization, see Device Out of Sync Alerts .

Click on the Statistics icon to launch statistics for the following VMs:

Unified CVP

Unified CVP Reporting

For more information, see Unified CVP Statistics and Unified CVP Reporting Statistics .

All VMs on Side B are indicated as OnBox Side B in the Location column.

The System Inventory displays read-only information for the following VMs:

Unified CCE Rogger

Unified CCE PG

Unified CCE AW-HDS-DDS

Unified CM Subscriber 2 (if on-box)

CUIC-LD-IdS Subscriber

Finesse Secondary

ECE Data Server

To update the VM, click the row corresponding to it. The details of the VM appear for you to make updates.

If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory.

Unified CVP - Unified CVP Server Windows credentials. Configure FTP .

For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine .

Unified CVP Reporting - Cisco Unified CVP Reporting Server Windows credentials.

If the CVP Reporting server VM is re-imaged or re-installed, you need to initialize the CVP Reporting server.

To initialize the CVP Reporting Server , click the Initialize icon and then click Yes to confirm.

Initialization removes existing call server association and Courtesy Callback configuration.

To re-associate call servers with the CVP Reporting server, navigate to Overview > Infrastructure Settings > Device Configuration > Device Configuration .

To reconfigure Courtesy Callback, navigate to Overview > Features > Courtesy Callback .

You can perform the full synchronization or differential synchronization of the configurations of various components. For
                                             more information on the machines that support data synchronization, see Device Out of Sync Alerts .

Click on the Statistics icon to launch statistics for the following VMs:

Unified CVP

Unified CVP Reporting

For more information, see Unified CVP Statistics and Unified CVP Reporting Statistics .

External Machines

The Location column for every External Machine in the deployment is displayed as OffBox , and can include any of the following:

HDS

Unified CM Publisher

Unified CM Subscriber

SocialMiner

ECE Data Server (refers to ECE Data Server VM for 400 agents and Services Server VM for ECE 1500 agents)

If ECE is installed in an HA deployment mode, add only one ECE Data Server in the Unified CCE Administration for 2000 agent
                                                               deployment model.

ECE Web Server

3rd Party Multichannel

Unified CVP Reporting

MediaSense

Cisco Contact Center SIP Proxy

Virtualized Voice Browser

Gateway

Cloud Connect Publisher

When you add or delete the Cloud Connect Publisher, for the change to take effect logout and login to the machine.

Media Server

Unified CM Subscriber machines are dedicated to the contact center. When you configure an external Unified CM Publisher, its
                                                               Unified CM Subscribers are added to the System Inventory automatically.

Version information displayed for ECE Data Server is fetched from ECE Web Server.

When you configure Cloud Connect Publisher, its Cloud Connect Subscribers are added to the System Inventory automatically.

The external HDS and external Unified CM Subscribers are auto detected. You do not need to add or delete them.

To add or update the external machines, see Add External Machines .

You can perform the full synchronization or differential synchronization of the configurations of various components. For
                                             more information on the machines that support data synchronization, see Device Out of Sync Alerts .

If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory.

If you edit the Unified CM Publisher, the Unified CM Subscribers associated with the publisher are updated automatically.
                                                         You cannot edit Unified CM Subscribers from the System Inventory.

If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                         You cannot edit Cloud Connect Subscribers from the System Inventory.

To associate the external HDS with a default Cisco Identity Service (IdS) for single sign-on:

Click the external HDS row.

The corresponding machine details page appears and you can modify the machine details.

Click the Search icon next to Default Identity Service .

Enter the machine name for the Cisco IdS in the Search field or choose the Cisco IdS from the list.

Click Save .

To delete , click the x on the machine. Confirm the deletion.

You can open the administration tool for these external machines by clicking the arrow icon in the machine box:

Unified CM Publisher

SocialMiner

MediaSense

To navigate to the Cisco Webex login page, click the Register link.

Principal VVB is used to configure the Customer Virtual Assistant feature.

Only one of the VVB machines across sites can be set as a Principal VVB and you cannot delete this machine.

First added the VVB machine into the Inventory is set as the Principal VVB by default. In the Upgrade scenario, one of the
                                                               configured VVBs is set as a Principal VVB.

A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports the Customer Virtual Assistant feature.
                                                               To set a VVB as a Principal VVB, see Edit External Machines .

#### Monitor Server Status Rules for Packaged CCE 2000 Agents Deployment

The System Health and VM server status categories apply only to VMware-based Packaged CCE 2000 Agents deployments before CCE15.0(1) SU2/ES202607 is
                                                installed. After the ES is installed, these VMware host and VM validation rules do not apply to VMware-based or Nutanix-based
                                                Packaged CCE 2000 Agent deployments.

In Packaged CCE 2000 Agents deployment, the Inventory displays the total number of alerts for machines with validation rules.
                                    Click the alert count to open the Server Status popup window, which lists all of the rules for that machine and indicates which have warnings and errors. Rules are grouped
                                    by these categories:

Configuration

Rules
                                                					for installation and configuration of a component.

These
                                                					rules identify problems with mismatched configuration between components,
                                                					missing services, and incorrectly configured services.

Unified CCE Rogger: The trace level must be set to normal to ensure performance.

Unified CVP: The names of the SIP Server Groups on CVP containing Communications Manager addresses must match the Communications Manager
                                                Cluster Fully Qualified Domain Name.

Cloud Connect: The Cloud Connect Publisher must be configured with the supported cloud services.

Operations

Rules
                                                					for the runtime status of a component.

These
                                                					rules identify services and processes that cannot be reached, are not running,
                                                					or are not in the expected state.

Unified CCE Rogger: The central controller agent process (ccagent.exe) must be in service for both PGs.

Cloud Connect: Type is either Publisher or Subscriber.

System Health

Metrics to monitor the CPU, memory, and disk usage of a component's Virtual Machine (VM) as reported by ESXi over the last
                                                10 minutes. The memory and CPU usage may differ slightly from system tools reported by the VM itself. For VM Hosts, these
                                                metrics also include datastore performance information.

For VM Hosts under M5 Tested Reference Configuration / Specification Based Configuration, these metrics include CPU reservation,
                                                CPU oversubscription, memory reservation and datastore utilization information.

All: Memory usage as reported by ESXi - 17%

For VM Hosts under M5 Tested Reference Configuration / Specification Based Configuration:

Maximum CPU Reservation - 65%

Maximum CPU Oversubscription - 200%

Maximum Memory Reservation - 80%

Maximum Storage Usage per Datastore - 80%

VM

VM requirements for a component.

All: VMware Tools must be up to date

System Validation

Rules for Unified CCE database and configuration settings.

These rules identify whether the configuration of objects in your deployment match the requirements and limits for Packaged
                                                Contact Center Enterprise.

The System Validation category is available only for the Side A Unified CCE AW-HDS-DDS.

Side A Unified CCE AW-HDS-DDS: Agent Desk Settings: Ring No Answer Times must not be set.

Side A Unified CCE AW-HDS-DDS: Application Gateway

Side A Unified CCE AW-HDS-DDS: Application Instance: Up to 12 Application Instances can be defined.

#### VM Validation

This section applies only to VMware-based Packaged CCE 2000 Agents deployments before release 15.0(1) SU2/ES202607 is installed.
                                             After the ES is installed, VM validation is not supported for VMware-based or Nutanix-based Packaged CCE 2000 Agents deployments.

The validation for the Packaged CCE: CCE-PAC-M1 deployment type makes the following checks to ensure hardware compliance and
                                 conformance with the Cisco-provided OVA files.

For Hosts:

Vendor

BIOS

ESXi version

Minimum number of CPU cores

Minimum memory

Data store size

For VMs:

Number of virtual CPU cores

Number of configured networks

Virtual network card driver (except for Unified CM and Unified Intelligence Center)

VM is powered on

CPU reservation

Exact memory

Exact disk size

Exact number of disks

VMware tools

#### Configure Cisco Unified Contact Center Enterprise PG

The following table outlines the configuration task for Media Routing Peripheral Gateway for the Packaged CCE 2000 Agents
                                 deployment.

Configuration Task

Add PIMs to the Media Routing Peripheral Gateway (optional)

### Cisco SNMP Setup

#### Add Cisco SNMP Agent Management Snap-In

You can configure Cisco SNMP Agent Management settings using
                                    		  a Windows Management Console snap-in.

Complete the following procedure to add the snap-in and
                                    		  change Cisco SNMP Management settings.

Step 1

From the Start menu, enter mmc.exe /32 .

Step 2

From the Console, choose File > Add or Remove Snap-ins .

Step 3

In the Add or Remove Snap-ins dialog box, choose Cisco SNMP Agent Management from the list of available snap-ins. Click Add .

Step 4

In the Selected snap-ins pane, double-click Cisco SNMP Agent Management .

Step 5

In the Extentions for Cisco SNMP Agent Management dialog box, select Always enable all available extentions . Click OK .

Step 6

In the Add/Remove Snap-in window, click OK . The Cisco SNMP Agent Management Snap-in
                                             			 is now loaded into the console.

#### Save Cisco SNMP Agent Management Snap-In View

After you load the Cisco SNMP Agent Management MMC snap-in,
                                    		  you can save the console view to a file with a .MSC file extension. You can
                                    		  launch the file directly from Administrative Tools.

Complete the following procedure to save the Cisco SNMP
                                    		  Agent Management snap-in view.

Step 1

Choose File > Save .

Step 2

In the Filename field, enter Cisco SNMP Agent Management .

Step 3

In the Save As type field, choose a file name to map to the
                                             			 administrative tools such as Microsoft Management Console Files(*.msc) .

Step 4

Click Save .

#### Set Up Community Names for SNMP V1 and V2c

If you use SNMP v1 or v2c you must configure a community
                                    		  name so that Network Management Systems (NMSs) can access the data your server
                                    		  provides. Use  SNMP community names to authenticate data exchange of SNMP
                                    		  information. An NMS can exchange SNMP information only with servers that use
                                    		  the same community name.

Complete the following procedure to configure the community
                                    		  name for SNMP v1 and v2c.

##### Before you begin

Ensure Cisco SNMP is added and saved using the procedures Add Cisco SNMP Agent Management Snap-In and Save Cisco SNMP Agent Management Snap-In View .

Step 1

Choose Start > All
                                                   				  Programs > Administrative tools > Cisco
                                                   				  SNMP Agent Management .

Step 2

Right-click Cisco SNMP Agent Management and choose Run as administrator .

Step 3

The Cisco SNMP Agent Management screen lists some of the
                                             			 configurations that require SNMP for traps and system logs.

Step 4

Right-click Community Names (SNMP v1/v2c) and choose Properties .

Step 5

In the Community Names (SNMP v1/v2c) Properties dialog box, click Add New Community .

Step 6

In the Community Name field, enter a community name.

Step 7

In the Host Address List, enter the host IP address.

Step 8

Click Apply and click OK .

#### Set Up SNMP User Names for SNMP V3

If you use SNMP v3 you must configure a user name so that
                                    		  NMSs can access the data your server provides.

Complete the following procedure to configure a user name for SNMP v3.

##### Before you begin

Ensure Cisco SNMP is added and saved using the procedures Add Cisco SNMP Agent Management Snap-In and Save Cisco SNMP Agent Management Snap-In View .

Step 1

From the Console Root, choose Cisco SNMP Agent
                                                   				  Management > User Names (SNMP
                                                   				  v3) > Properties .

Step 2

Click Add New User .

Step 3

In the User Name field, enter a username.

Step 4

Click Save .

Step 5

The username appears in the Configured Users pane at the top of
                                             			 the dialog box.

Step 6

Click Apply and click OK .

#### Set Up SNMP Trap Destinations

You can configure SNMP Trap Destinations for SNMP v1, SNMP
                                    		  v2c, and SNMP v3. A Trap is a notification that the SNMP agent uses to inform
                                    		  the NMS of a certain event.

Complete the following procedure to configure the trap destinations.

##### Before you begin

Ensure Cisco SNMP is added and saved using the procedures Add Cisco SNMP Agent Management Snap-In and Save Cisco SNMP Agent Management Snap-In View .

Step 1

From the Console Root, choose Cisco SNMP Agent
                                                   				  Management > Trap Destinations > Properties .

Step 2

Click Add Trap Entity .

Step 3

Click the SNMP version that your NMS uses.

Step 4

In the Trap Entity Name field, enter a name for the trap entity.

Step 5

Choose the User Name/Community Name that you want to associate
                                             			 with this trap. This list is auto-populated with existing configured
                                             			 users/community names.

Step 6

Enter one or more IP addresses in the IP Address entry field.
                                             			 Click Insert to define the destinations for the
                                             			 traps.

Step 7

Click Apply and click Save to save the new trap destination.

The trap entity name appears in the Trap Entities section at the
                                                			 top of the dialog box.

Step 8

Click OK .

#### Set Up SNMP Syslog Destinations

You can configure Syslog destinations for SNMP from the
                                    		  Cisco SNMP Agent Management Snap-in.

Complete the following procedure to configure Syslog
                                    		  destinations.

Step 1

From the Console Root, choose Cisco SNMP Agent
                                                   				  Management > Syslog
                                                   				  Destinations > Properties .

Step 2

Choose an Instance from the list box.

Step 3

Check Enable Feed .

Step 4

Enter an IP address or host name in the Collector Address field.

Step 5

Click Save .

Step 6

Click OK and restart the logger.

## Modify Logger

To modify the logger, do the following:

This procedure is applicable only after a technology refresh and if you have enabled Outbound Option High Availability

Step 1

Open the Web Setup tool.

Step 2

Choose Component Management > Loggers .

Step 3

Select the required Logger that you want to configure.

Step 4

Click Edit .

Step 5

Click Next twice.

Step 6

Enter the Active Directory Account Name that the opposite side Logger runs under or a security group which includes that account.

While using Outbound Option High Availability, if you want to change the Logger Public Interface or Active Directory Account Name , you must disable Outbound Option High Availability using logger setup. Only after disabling Outbound Option HA, change the Logger Public Interfaces or Active Directory Account Name , then re-enable Outbound Option High Availability to update the new Logger Public Interface or Active Directory Account Name .

Step 7

Click Next .

Step 8

Review the Summary page, and click Finish .

For more information, see the Configure the Logger for Outbound Option topic in the Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/series.html .

## Restart Tomcat on SideB Administration and Data Server

Step 1

Log in to the Side B AW-HDS-DDS Server.

Step 2

Go to Services and restart Apache Tomcat.

## Configure Cisco Unified Customer Voice Portal

The CVP configurations are site specific. Side A and Side B configurations per site must be the same.

Configuration Tasks

To secure communication between Call Server and ICM, see Secure Flow Communication .

For more information about securing CVP communication, see Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

To change the default settings, see CVP Server Services Setup

Configure Media Server

Configure SNMP

### Secure Flow Communication

#### CA-signed Certificates

##### Generate CA Certificate on CVP Call Server

Log in to the Call Server. Retrieve the keystore password from the security.properties file.

At the command prompt, enter more %CVP_HOME%\conf\security.properties .

Security.keystorePW = <Returns the keystore password>

Enter the keystore password when prompted.

Step 1

Remove the existing certificate by running the following command:

%CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -delete -alias callserver_certificate

Step 2

Enter the keystore password when prompted.

Step 3

Generate a new key pair for the alias with the selected key size by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias callserver_certificate
                                                   -v -keysize 2048 -keyalg RSA .

```
Enter keystore password: <enter the keystore password>
What is your first and last name?
 [Unknown]: < Specify the FQDN of the CVP server. Example: cisco-cvp-211@example.com >
What is the name of your organizational unit?
 [Unknown]: <specify OU> E.g. CCBU
What is the name of your organization?
 [Unknown]: <specify the name of the org> E.g. CISCO
What is the name of your City or Locality?
 [Unknown]: <specify the name of the city/locality>  E.g. BLR
What is the name of your State or Province?
 [Unknown]: <specify the name of the state/province>  E.g. KAR
What is the two-letter country code for this unit?
 [Unknown]: <specify two-letter Country code>  E.g. IN

Specify ‘yes’ for the inputs.
```

Step 4

Generate the CSR certificate for the alias by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias callserver_certificate
                                                   -file %CVP_HOME%\conf\security\callserver.csr and save it to a file (for example, callserver.csr).

Step 5

Enter the keystore password when prompted.

Step 6

Download the callserver.csr from %CVP_HOME%\conf\security\ and sign it from CA.

Step 7

Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\ .

Step 8

Install the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                   root -file %CVP_HOME%\conf\security\<filename_of_root_cert> .

Step 9

Enter the keystore password when prompted.

Step 10

Install the signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                   callserver_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert> .

##### Import Root CA Certificate into ICM

Step 1

Copy the root CA certificate to the ICM (PG) box.

Step 2

Open the command prompt and go to c:\cisco\icm\bin .

Step 3

Type CiscoCertUtil.exe /install rootCA.pem .

##### Generate CA Certificate on ICM

Step 1

Navigate to C:\icm\ssl\keys and remove the old ‘host.key’(if available).

Step 2

Log into the ICM (PG) box. Go to the command prompt and type CiscoCertUtil.exe /generateCSR .

```
C:\icm\bin>CiscoCertUtil.exe /generateCSR SSL config path = C:\icm\ssl\cfg\openssl.cfg
SYSTEM command is C:\icm\ssl\bin\openssl.exe req -new -key C:\icm\ssl\keys\host.key -out C:\icm\ssl\certs\host.csr Generating a 2048 bit RSA private key
.............................
.......
writing new private key to 'C:\icm\ssl\keys\host.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:IN
State or Province Name (full name) [Some-State]:KA
Locality Name (eg, city) []:BLR
Organization Name (eg, company) [Internet Widgits Pty Ltd]:cisco
Organizational Unit Name (eg, section) []:ccbu
Common Name (e.g. server FQDN or YOUR name) []:abc.com
Email Address []:radmohan@cisco.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:*****
An optional company name []:cisco
```

The client certificate and key are generated and stored as host.csr and host.key in C:\icm\ssl\certs and C:\icm\ssl\keys folders respectively.

To generate ECDSA CSR with default P384 curve, use ciscocertutil.exe /generateCSR /curve command. For
                                                               more details refer to the topic CiscoCertUtil Utility at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

Step 3

Sign it from a CA. Follow the procedure Import Root CA Certificate into ICM .

Remove the existing host.pem (if any) from C:\icm\ssl\certs .

Save host.cer (CA-signed) as host.pem in C:\icm\ssl\certs .

Step 4

From the command prompt, run C:\icm\bin>CiscoCertUtil.exe /install
                                                   c:\icm\ssl\certs\host.pem .

Step 5

Cycle VRU PG.

#### Self-signed Certificates

The following table lists components from which self-signed certificates are generated and components into which self-signed
                                 certificates are imported.

Import Self-signed Certificates to Target Server

Generate Self-signed Certificates from Source Component Server

Links

AW Machines

Unified CCE Components (Router, Logger 1 , Rogger 2 , PGs, AWs, and HDS

Import Unified CCE Component Certificates

Import Diagnostic Framework Portico Certificate into AWMachines

Customer Voice Portal (CVP) Call Server/CVP Reporting Server

Email and Chat (ECE)

Cisco Finesse Primary and Secondary

Cisco Unified Communications Manager (CUCM) Publisher and Subscriber

Virtualized Voice Browser (VVB)

Cisco Unified Intelligence Center (CUIC) Publisher and Subscriber

Cisco Identity Service (IdS) Publisher and Subscriber

Cloud Connect Publisher and Subscriber

Customer Collaboration Platform

Live Data Publisher and Subscriber

Finesse

AWDB

Import and Export SSC of Finesse to Administration and Data Server

Import and Export SSC of Administration and Data Server to Finesse

PG

Import and Export Self-Signed Certificate of PG to Finesse

Import and Export self-signed certificate of Cisco Finesse to PG

Cloud Connect

Export Cloud Connect Certificate

Import Cloud Connect Certificate

CUCM Publisher

Logger

AW

Import Unified CCE Component Certificates

Rogger

CVP

##### Generate Certificate on CVP Call Server

Step 1

http://acrsrv-app-prd-01:8080/ Export the Call Server certificate by
                                                running. %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore
                                                   %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                   callserver_certificate -file
                                                   %CVP_HOME%\conf\security\<callserver_certificate>

Step 2

Enter the keystore password when prompted.

Step 3

Restart the Call Server service to load the new certificates.

##### Import Certificate into ICM

Step 1

Copy the self-signed CVP Call Server certificate downloaded from CVP to the ICM box (PG) .

Step 2

Open the command prompt and go to c:\icm\bin .

Step 3

Type CiscoCertUtil.exe /install
                                                   <callserver_certificate> .

Repeat the procedure for multiple PIMs and for Side A and Side B.

##### Generate Certificate on ICM Server

###### Before you begin

Step 1

Log into the ICM (PG) box. Go to the command prompt and type CiscoCertUtil.exe /generatecert .

```
C:\icm\bin>ciscocertutil.exe /generatecert SSL config path = C:\icm\ssl\cfg\openssl.cfg
SYSTEM command is C:\icm\ssl\bin\openssl.exe req -x509 -newkey rsa:2048 -days 7300 -nodes -subj /CN=PG-SIDEA.pcce.com -out
C:\icm\ssl\certs\host.pem -keyout C:\icm\ssl\keys\host.key
Generating a RSA private key
..................
....
writing new private key to 'C:\icm\ssl\keys\host.key
```

Step 2

Cycle VRU PG.

##### Import ICM  Certificate into CVP Call Server

Step 1

Log into the CVP Call Server box. Create a folder and copy host.pem to c:\IcmCertificate .

Step 2

From the command prompt, run %CVP_HOME%\jre\bin\keytool.exe -import -v -alias icm_certificate -storetype JCEKS -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore
                                                   -file c:\IcmCertificate\host.pem .

Step 3

Enter the keystore password when prompted. Click Yes .

Step 4

Restart the Callserver service to load the new certificates.

Repeat the procedure if you have multiple Call Servers.

### Configure Cisco Unified Communications Manager

The following table outlines the Cisco Unified Communications Manager configuration tasks for Packaged CCE 2000 Agents deployment.

Configuration Tasks

Configure Fully Qualified Domain Name

Configure Cisco Unified Communications Manager Groups

Configure Conference Bridges

Configure Media Termination Points

Transcoder Configuration in Unified CM and IOS Gateway

Configure Media Resource Groups

Configure and Associate Media Resource Group List

Configure CTI Route Point

Configure Ingress Gateways for Locations-based Call Admission Control

Add a SIP Profile in Unified CM

Configure Trunk

Configure Route Group

Configure Route List

Configure Route Pattern

#### Configure Fully Qualified Domain Name

Step 1

Open Cisco Unified Communications Manager and log in.

Step 2

Navigate to System > Enterprise Parameters .

Step 3

Fill in Clusterwide Domain Configuration > Cluster Fully Qualified Domain Name with the Fully Qualified Domain Name of your cluster.

The Cluster Fully Qualified Domain Name is the name of the Unified Communications Manager Server Group defined in Unified
                                                            CVP.

Step 4

Click Save .

#### Configure Cisco Unified Communications Manager Groups

Step 1

Select  Cisco Unified CM Administrator from the Navigation menu and click Go .

Step 2

Select System > Cisco Unified CM Group .

Step 3

Click Find . Then click Default .

Step 4

Move the two subscribers from the Available panel to the Selected panel.

Step 5

Click Save .

Step 6

Click Reset .

Step 7

On the Device Reset popup, click Reset .

Step 8

Click Close .

#### Configure Conference
                              	 Bridges

Step 1

Select Media
                                                   				  Resources > Conference bridge .

Step 2

Click Add
                                                				New .

Step 3

Select
                                             			 Conference Bridge Type of Cisco
                                                				IOS Conference Bridge .

Step 4

In the Conference Bridge name field, enter a unique
                                             			 identifier for the conference bridge name that matches the configuration on the
                                             			 gateway.

```
# Add a SCCP group for each of the hardware resource types
sccp ccm group 1
associate ccm 1 priority 1
associate profile 2 register gw70mtp
associate profile 1 register gw70conf
associate profile 3 register gw70xcode
```

Step 5

Select a Device
                                             			 Pool.

Step 6

Click Save .

Step 7

Click Apply
                                                				Config .

#### Configure Media
                              	 Termination Points

Step 1

Select Media
                                                   				  Resources > Media Termination Point .

Step 2

Click Add
                                                				New .

Step 3

In the Media
                                             			 Termination Point Name field, enter a unique identifier for the media
                                             			 termination that coincides with the configuration on the gateway.

```
# Add a SCCP group for each of the hardware resource types
sccp ccm group 1
associate ccm 1 priority 1
associate profile 2 register gw70mtp
associate profile 1 register gw70conf
associate profile 3 register gw70xcode
```

Step 4

Select a Device
                                             			 Pool.

Step 5

Click Save .

Step 6

Click Apply
                                                				Config .

## Transcoder Configuration in Unified CM and IOS Gateway

A transcoder is
                              		required for multicodec scenarios to convert a stream from a G.711 codec to a G.729 codec.

For more information about transcoder configuration in Unified Communications Manager and gateway, see the section "Configure
                              Transcoders and Media Termination Points" in the System Configuration Guide for Cisco Unified Communications Manager at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-and-configuration-guides-list.html .

### Configure
                           	 Transcoders

Step 1

In Unified
                                          			 Communications Manager Administration, select Media
                                             				Resources > Transcoder.

Step 2

Click Add
                                             				New .

Step 3

For Transcoder
                                          			 Type, select Cisco IOS enhanced media termination point .

Step 4

In the Device
                                             				Name field, enter a unique identifier for the transcoder name that
                                          			 coincides with the configuration on the gateway.

In the following example, this is gw70xcode.

```
# Add a SCCP group for each of the hardware resource types
sccp ccm group 1
associate ccm 1 priority 1
associate profile 2 register gw70mtp
associate profile 1 register gw70conf
associate profile 3 register gw70xcode
```

Step 5

In the Device Pool field, select the appropriate device pool.

Step 6

Click Save .

Step 7

Click Apply
                                             				Config .

### Configure the CVP Call Server Dial Peers in Ingress Gateway

The Ingress Gateway to
                              		Unified CVP outbound dial peer configuration uses the IPv4 address of
                              		Unified CVP as the session target.

## Configure Media
                        	 Resource Groups

Step 1

Select Media
                                             				  Resources > Media Resource Group .

Step 2

Add a Media
                                       			 Resource Group for Conference Bridges.

Click Add
                                                					 New .

Enter a
                                             				  Name.

From the
                                             				  Available list, select all the Cisco IOS conference bridge resources configured
                                             				  for each ingress/VXML combination gateway in the deployment and add them to the
                                             				  group.

Click Save .

Step 3

Add a Media
                                       			 Resource Group for Media Termination Point.

Click Add
                                                					 New .

Enter a
                                             				  Name.

From the
                                             				  Available list, select all the hardware media termination points configured and
                                             				  add them to the group.

Click Save .

Step 4

Add a Media
                                       			 Resource Group for Transcoder.

Click Add
                                                					 New .

Enter a
                                             				  Name.

From the
                                             				  Available list, select all the transcoders configured and add them to the
                                             				  group.

Click Save .

Step 5

Click Save.

## Configure and Associate Media Resource Group List

Step 1

Select Media Resources > Media
                                             				  Resource Group List .

Step 2

Click Add New and enter a Name.

Step 3

Add a Media Resource Group list and associate all of the media
                                       			 resource groups. Click Save .

Step 4

Select System > Device
                                             				  Pool . Click Find . Select the appropriate device pool.

Step 5

From the Media Resource Group List drop-down list, choose the
                                       			 media resource group list added in Step 2.

Step 6

Click Save . Click Reset .

## Configure CTI
                        	 Route Point

Step 1

In Cisco
                                       			 Unified CM Administration, select Device > CTI Route
                                             				  Point .

Step 2

Click Add
                                          				New .

Step 3

Set a device
                                       			 name; for example, PCCEInternalDNs .

Step 4

For Device
                                       			 Pool, select Default .

Step 5

Select a Media
                                       			 Resource Group List from the list.

Step 6

Click Save.

Step 7

Click on Line
                                       			 [1] to configure the directory number associated with this route point.

This
                                          				directory number will be a pattern that is intended to match any of the
                                          				internal Dialed Numbers you configure in Packaged CCE for internally routed
                                          				calls. (For instance, for Transfers and Conferences).

Important

Define a
                                                      				  pattern that is flexible enough to match all your internal dialed numbers yet
                                                      				  restrictive enough not to inadvertently intercept calls intended for other
                                                      				  Route Patterns you may have defined for other parts of your dial plan. Use a
                                                      				  unique prefix for internal calls. For example, if you have internal dialed
                                                      				  numbers 1230000 and 1231111, then an appropriate line number to enter for the
                                                      				  cti route point would be 123XXXX.

Step 8

Select User
                                             				  Management > Application User .

Step 9

Select pguser created during Packaged CCE automated initialization.

Step 10

Select the CTI
                                       			 Route Point from the list of Available Devices , and add it to the list of Controlled Devices .

Step 11

Click Save.

## Configure Ingress
                        	 Gateways for Locations-based Call Admission Control

Locations-based
                              		  call admission control (CAC) is used in the Unified CCE branch-office call flow
                              		  model (also known as the Centralized Model). This means that all servers
                              		  (Unified CVP, Unified CCE, Unified Communications Manager, and SIP Proxy
                              		  server) are centralized in one or two data centers, and each branch office.

Configure Unified Communications Manager to use the Ingress gateway
                              		  instead of Unified CVP as the originating location of the call. This
                              		  configuration ensures that CAC can be properly adjusted based on the locations
                              		  of the calling endpoint and the phone.

Important

Do not define
                                          			 Unified CVP as a gateway device in Unified Communications Manager.

In Cisco Unified CM Administration, define the Ingress gateways as
                                       			 gateway devices. Assign the correct location to the devices.

## Add a SIP Profile
                        	 in Unified CM

This option allows
                              		  a dual-stack SIP trunk to offer both IPv4 and IPv6 media. 
                              		Perform this procedure for IPv6-enabled deployments only.

Step 1

From Cisco
                                          				Unified CM Administration , choose Device > Device
                                             				  Settings > SIP Profile .

Step 2

Click Add
                                          				New and enter the name of the SIP profile.

Step 3

Check the Enable
                                          				ANAT check box on the SIP Profile.

Step 4

Save your
                                       			 changes.

## Configure
                        	 Trunk

There are two Unified CVP Servers and each must be associated with a SIP trunk in Unified Communications Manager. The following
                              procedure explains how to configure the SIP trunks, each targeting a different Unified CVP Server.

Actual site topology may necessitate the use of alternate SIP trunk plans, which are supported as long as both Unified CVP
                              Servers are targeted by the configured SIP trunks.

Step 1

In Unified Cisco
                                       			 CM Administration, select Device > Trunk.

Step 2

Click Add
                                          				New .

Step 3

From the Trunk
                                       			 Type drop-down list, choose SIP
                                          				Trunk , and then click Next .

Step 4

Enter the
                                       			 following in the Device
                                          				Information section:

In the Device Name field, enter a name for the SIP trunk, for example, sipTrunkCVPA .

In the Device Pool drop-down list, select the device pool
                                             				  that the customer has defined.

Select a
                                             				  Media Resource Group List from the list.

Make sure
                                             				  that the Media Termination Point Required check box is not
                                             				  checked.

Step 5

Scroll down to
                                       			 the SIP
                                          				Information section:

In Row 1 of
                                             				  the Destination table, enter the IP address of a CVP server.
                                             				  Accept the default destination port of 5060.

In the SIP Trunk
                                                					 Security Profile drop-down list, select Non Secure SIP Trunk Profile .

In the SIP Profile drop-down list, select Standard SIP Profile .

If you are using an IPv6-enabled deployment, use the SIP Profile created in Add a SIP Profile in Unified CM .

In the DTMF
                                                					 Signaling Method drop-down list, select RFC 2833 .

Step 6

Click Save .

Step 7

Click Reset .

Step 8

Repeat for all
                                       			 the remaining Unified CVP servers in the deployment.

## Configure Route
                        	 Group

Complete the
                              		  following procedure to create a route group.

Step 1

In Unified
                                       			 Communications Manager, select Call
                                             				  Routing > Route Hunt > Route
                                             				  Group .

Step 2

Click Add
                                          				New .

Step 3

Enter a name
                                       			 for the route group; for example, CVP Route Group .

Step 4

Using the Add
                                       			 to Route Group button, add all CVP Trunks as Selected Devices.

Step 5

Click Save .

## Configure Route
                        	 List

Complete the
                              		  following procedure to add a route list to the route group.

Step 1

In Unified
                                       			 Communications Manager, select Call
                                             				  Routing > Route Hunt > Route
                                             				  List .

Step 2

Click Add
                                          				New .

Step 3

Enter a name
                                       			 for the route list; for example, CVP Route List .

Step 4

Select a Cisco
                                       			 Unified Communications Manager Group.

Step 5

Add the route
                                       			 group you created.

Step 6

Click Save .

## Configure Route
                        	 Pattern

Complete the
                              		  following procedure to add a route pattern to the route list.

Step 1

In Unified
                                       			 Communications Manager, select Call
                                             				  Routing > Route Hunt > Route
                                             				  Pattern .

Step 2

Click Add
                                          				New .

Step 3

Enter a route
                                       			 pattern of 8881111000XXXX .

Step 4

Select the
                                       			 route list that you created.

Step 5

Keep all
                                       			 defaults in all panels

Step 6

Click Save .

Step 7

Click OK at the message about the Forced Authorization Code. You
                                       			 do not want a Forced Authorization Code.

## Configure Cisco Unified Intelligence Center

Follow this sequence to configure the Cisco Unified Intelligence Center for Packaged CCE 2000 Agents deployment

Sequence

Task

1

Download Report Bundles

2

Import Reports

3

Configure Unified Intelligence Center Administration

### Configure Unified Intelligence Center Data Sources for External HDS

Perform this procedure only if your deployment includes an external HDS and you wish to have a longer retention period.

#### Before you begin

Configure the Unified Intelligence Center SQL user for the External HDS databases before configuring the data sources (applicable for 4000 Agents and 12000 Agents). For more information, refer the Configure Unified Intelligence Center SQL User Account on the External HDS section in the
                                    Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html

Step 1

Sign in to Unified Intelligence Center with your Cisco Intelligence Center administrator account (https://<hostname/ IP address
                                          of CUIC Publisher>:8444/cuicui).

Step 2

Select Configure > Data Sources .

Step 3

Click Data
                                             				Sources in the left panel.

Step 4

Select the UCCE Historical data source. Click Edit .

In the Datasource Host field, enter the IP Address of the external HDS server.

In the Port field, enter the AW SQL server port number. The default is 1433 .

In the Database Name field, enter {instance}_awdb .

Leave the Instance field blank.

Select the Timezone .

In the Database User ID , enter the user name that you configured for the Cisco Unified Intelligence Center SQL Server user account.

Enter and confirm the SQL Server User password .

Select the Charset based on the collation of SQL Server installation.

Click Test Connection .

Click Save .

Step 5

Click the Secondary tab to configure Unified CCE Historical
                                          			 Data Source.

Check the Failover
                                                   					 Enabled checkbox.

In the Datasource Host field, enter the IP address of the second external HDS server.

In the Port field, enter 1433 .

In the Database Name field, enter {instance}_awdb .

Complete
                                                				  other fields as in the Primary tab.

Click Test
                                                   					 Connection .

Click Save .

Step 6

Repeat this procedure for the UCCE Realtime datasource for 4000 or 12000 Agents deployment .

The Database Name for the Realtime Data Source is {instance}_awdb .

### Download Report
                           	 Bundles

The following Cisco Unified Intelligence Center report bundles are available as downloads from Cisco.com https://software.cisco.com/download/type.html?mdfid=282163829&catid=null . Click the Intelligence Center Reports link to view all available report bundles:

Realtime and
                                       				Historical Transitional templates - Introductory templates designed for new
                                       				users. These templates are simplified versions of the All Fields templates, and
                                       				are similar to templates available in other contact center solutions.

Realtime and
                                       				Historical All Fields templates - Templates that provide data from all fields
                                       				in a database. These templates are most useful as a basis for creating custom
                                       				report templates.

Live Data
                                       				templates - Templates that provide up to the moment data for contact center
                                       				activity.

Realtime and
                                       				Historical Outbound templates - Templates for reporting on Outbound Option
                                       				activity. Import these templates if your deployment includes Outbound Option.

Realtime and Historical SocialMiner templates - Templates for reporting on SocialMiner activity. Import these templates if your deployment includes SocialMiner .

Cisco Unified
                                       				Intelligence Center Admin Security templates - Templates to report on Cisco
                                       				Unified Intelligence Server audit trails, permissions, and template ownership.

Some of the templates in these bundles are not applicable in Cisco Packaged CCE deployment. See the Cisco Packaged Contact Center Enterprise Reporting User Guide at https://www.cisco.com/en/US/products/ps12586/tsd_products_support_series_home.html for more information about the templates used in Packaged CCE deployments.

Additionally, sample custom report templates are available from Cisco DevNet ( https://developer.cisco.com/site/reporting/documentation/ ) and include templates for:

Enterprise Chat and Email

Cisco Unified Customer Voice Portal (Unified CVP)

When downloading report template bundles, select bundles for the
                                 		  version of software deployed in your contact center.

### Import Reports

You can import the Unified Intelligence Center report, which is in either .xml or .zip file format.

The imported report retrieves data for the following entities:

Report

Report Definition

Value Lists

Views

Thresholds

Drilldowns

Template Help

Each report template help folder has a size limit of 3 MB. If the folder size exceeds this limit, the system does not load
                                                         the help content.

You cannot import Report Filters and Collections.

You cannot use the same names for the custom Value List, Report, or Report Definition that exist in the stock report templates.
                                                         If the same names are used, it leads to the stock report template import failure.

To import reports, perform the following steps:

Step 1

In the left navigation pane, choose Reports .

Step 2

In the Reports listing page, click Import .

Step 3

Click Browse to select the file (.xml or .zip format) to be imported.

The maximum file size for the .zip file format is 60 MB and for .xml file format is 3 MB.

Step 4

Select the required file and click Open .

Step 5

Select the file location from the Save to Folder list to save the file.

Step 6

Click Upload .

Step 7

Select a Data Source for the Report Definition only if the Report Definition for the report being imported is not defined
                                          in the Unified Intelligence Center.

Step 8

Select a Data Source for the Value List that is defined in the Report Definition.

Selection of a Data Source for the Value List is mandatory:

If the Value List does not use the same Data Source as the Report Definition.

For Real Time Streaming Report Definitions.

Step 9

Select the files to import or overwrite.

Overwrite—If the report being imported exists in the Unified Intelligence Center.

Import—If the report being imported is the new set of report files.

Step 10

Click Import .

If the system does not have report definitions, new report definitions are created in Report Definitions > Imported Report Definitions folder.

Importing a report to a different version of Unified Intelligence Center is not supported. However, when you upgrade Unified
                                                               Intelligence Center, report templates continue to work in the upgraded version.

Importing manually edited XMLs is not supported.

### Configure Unified
                           	 Intelligence Center Administration

Step 1

Sign in to the Cisco Unified Intelligence Center Administration Console ( https:// <hostname> :8443/oamp ) .

Step 2

Configure the Active Directory card under Cluster Configuration .

Enter the Host Address for the Primary Active Directory Server.

Leave the default value for Port.

Complete the Manager Distinguished Name fields.

Enter and confirm the password with which the Manager accesses the domain controller.

For User Search Base, specify the Distinguished Name or Organization Unit of the domain you want to search .

For Attribute for User ID, select the required option.

If the Windows domain name and the NETBIOS names are different, do the following: in the Cisco Unified Intelligence Center Administration
                                                                  										Console , under Active Directory Settings , in the
                                                               									field Attribute for User ID , ensure to select sAMAccountName , and add the NETBIOS value to
                                                               									set it as default value.

Add at least one domain for the UserName Identifier. Do not type the @ sign before the domain name.

Set a domain as the default.

Click Test Connection .

Click Save .

For more details, see the online help.

Step 3

Configure syslog
                                          			 for all devices.

Choose Logs and Traces .

For each
                                                				  host address:

Select the associated
                                                         						servers and click the arrow to expand.

Select the server name.

In the Syslog Settings pane, configure the Primary and Backup Host. Click Save .

Step 4

Configure SNMP
                                          			 for all devices, if used.

Select Tools > Network SNMP .

Navigate to
                                                				  SNMP and for each server add the following:

V1/V2c Community Strings.

Notification Destination.

## Configure Cisco Finesse

Follow this sequence to configure the Cisco Finesse for Packaged CCE 2000 Agents deployment

Sequence

Task

1

Configure Contact Center Agents and Routing for Live Data Reports

2

Live Data Reports

3

Securing connection between CTI Server and Finesse

### Configure Contact
                           	 Center Agents and Routing for Live Data Reports

In order to test the Live Data reports in the Finesse desktops, configure the following in Unified CCE Administration ( https:// <Side A/B Unified CCE AW-HDS-DDS IP address> /cceadmin):

Agents

Skill groups or
                                    			 precision queues

Call types

Dialed numbers

Network VRU
                                    			 scripts

Routing scripts

Routing scripts are configured in Script Editor, which you can open from Unified CCE Administration Tools.

## Live Data Reports

Cisco Unified
                              		  Intelligence Center provides Live Data real-time reports that you can add to
                              		  the Finesse desktop.

### Add Live Data
                           	 Reports to Finesse

The following
                                 		  sections describe how to add the Live Data reports to the Finesse desktop. The
                                 		  procedure that you follow depends on several factors, described in the
                                 		  following table.

When to
                                             						use

Add Live
                                             						Data reports to default desktop layout

Use this
                                             						procedure if you want to add Live Data reports to the Finesse desktop after a
                                             						fresh installation or after an upgrade if you have not customized the default
                                             						desktop layout.

Add Live
                                             						Data reports to custom desktop layout

Use this
                                             						procedure if you have customized the Finesse desktop layout.

Add Live
                                             						Data reports to team layout

Use this
                                             						procedure if you want to add Live Data reports to the desktop layout for
                                             						specific teams only.

#### Add Live Data
                              	 Reports to Default Desktop Layout

The Finesse
                                    		  default layout XML contains commented XML code for the Live Data report gadgets
                                    		  available for the Finesse desktop. The gadgets are divided into two categories:
                                    		  HTTPS version of Live Data gadgets and HTTP version of Live Data gadgets.

This procedure
                                    		  explains how to add the Live Data report gadgets to the default desktop layout.
                                    		  Use this procedure after a fresh installation of Finesse. If you upgraded
                                    		  Finesse but do not have a custom desktop layout, click Restore
                                       			 Default Layout on the Manage Desktop Layout gadget and then follow
                                    		  the steps in this procedure. Note that line breaks and spaces that appear in
                                    		  the example text are provided only for readability and must not be included in
                                    		  the actual code.

Step 1

In Unified CCE Administration , navigate to Desktop > Resources .

Step 2

Click the Desktop Layout tab.

Step 3

Remove the
                                             			 comment characters (<!-- and -->) from each report that you want to add
                                             			 to the desktop layout. Make sure you choose the reports that match the method
                                             			 your agents use to access the Finesse desktop (HTTP or HTTPS).

Step 4

Replace
                                             			 my-cuic-server with the fully qualified domain name of your Cisco Unified
                                             			 Intelligence Center Server.

Step 5

Optionally, change the gadget height.

##### Example:

The height specified in the Live Data gadget URLs is 310 pixels. If you want to change the height, change the gadgetHeight
                                                parameter in the URL to the desired value. For example, if you want the gadget height to be 400 pixels, change the code as
                                                follows, replacing 310 with 400:

```
<gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp?
        gadgetHeight=400&viewId_1=99E6C8E210000141000000D80A0006C4&
        filterId_1=agent.id=CL%20teamName&viewId_2=9AB7848B10000141000001C50A0006C4&
        filterId_2=agent.id=CL%20teamName
        </gadget>
```

To maintain the optimal display of the gadget with scroll bars, set the value for the gadget height to a minimum of 200 pixels.
                                                If the report does not require scroll bars, for example a one-row report, you can set a smaller gadget height (for example,
                                                100 pixels). If you do not specify anything for the gadget height (if you remove the 310 from the URL), it defaults to 170
                                                pixels.

Step 6

Click Save .

#### Add Live Data
                              	 Reports to Custom Desktop Layout

The Finesse
                                    		  default layout XML contains commented XML code for the Live Data report gadgets
                                    		  available for the Finesse desktop. The gadgets are divided into two categories:
                                    		  HTTPS version of Live Data gadgets and HTTP version of Live Data gadgets.

This procedure
                                    		  explains how to add the Live Data report gadgets to a custom desktop layout.
                                    		  Note that line breaks and spaces that appear in the example text are provided
                                    		  only for readability and must not be included in the actual code.

Step 1

In Unified CCE Administration , navigate to Desktop > Resources .

Step 2

Click the Desktop Layout tab.

Step 3

Click Finesse Default Layout XML to show the default
                                             			 layout XML.

Step 4

Copy the XML code for the report you want to add from the Finesse
                                             			 default layout XML.

##### Example:

To add the Agent Report for HTTPS, copy the following:

```
<gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp?
        gadgetHeight=310&viewId_1=99E6C8E210000141000000D80A0006C4&
        filterId_1=agent.id=CL%20teamName&
        viewId_2=9AB7848B10000141000001C50A0006C4&
        filterId_2=agent.id=CL%20teamName
</gadget>
```

Step 5

Paste the XML within the tab tags where you want it to appear.

##### Example:

To add the report to the home tab of the agent desktop:

```
<layout>
  <role>Agent</role>
  <page>
    <gadget>/desktop/gadgets/CallControl.jsp</gadget>
  </page>
  <tabs>
    <tab>
      <id>home</id>
      <label>finesse.container.tabs.agent.homeLabel</label>
      <gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp?
              gadgetHeight=310&viewId_1=99E6C8E210000141000000D80A0006C4&
              filterId_1=agent.id=CL%20teamName&
              viewId_2=9AB7848B10000141000001C50A0006C4&
              filterId_2=agent.id=CL%20teamName
      </gadget> 
    </tab>
    <tab>
      <id>manageCall</id>
      <label>finesse.container.tabs.agent.manageCallLabel</label>
    </tab>
  </tabs>
</layout>
```

Step 6

Replace
                                             			 my-cuic-server with the fully qualified domain name of your Cisco Unified
                                             			 Intelligence Center Server.

Step 7

Optionally, change the gadget height.

##### Example:

The height specified in the Live Data gadget URLs is 310 pixels. If you want to change the height, change the gadgetHeight
                                                parameter in the URL to the desired value. For example, if you want the gadget height to be 400 pixels, change the code as
                                                follows:

```
<gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp?
        gadgetHeight=400&viewId_1=99E6C8E210000141000000D80A0006C4&
        filterId_1=agent.id=CL%20teamName&viewId_2=9AB7848B10000141000001C50A0006C4&
        filterId_2=agent.id=CL%20teamName
        </gadget>
```

To maintain the optimal display of the gadget with scroll bars, set the value for the gadget height to a minimum of 200 pixels.
                                                If the report does not require scroll bars, for example a one-row report, you can set a smaller gadget height (for example,
                                                100 pixels). If you do not specify anything for the gadget height (if you remove the 310 from the URL), it defaults to 170
                                                pixels.

Step 8

Click Save .

After you
                                                            				  add a gadget, sign in to the Finesse desktop and make sure it appears the way
                                                            				  you want. If you use a report with a large number of rows, you may want to
                                                            				  adjust the gadget height or the screen resolution on the computer used to
                                                            				  access the desktop to make the report easier to read or make more rows appear
                                                            				  on the screen without needing to scroll down.

Agents who
                                                            				  are signed in when you change the desktop layout must sign out and sign back in
                                                            				  to see the change on their desktops.

## Configure Cisco
                        	 Unified Customer Voice Portal Reporting Server

Follow this sequence to configure the Cisco Unified Customer Voice Portal Reporting Server for Packaged CCE deployment

The Unified CVP Reporting VM is required for customers who use Courtesy Callback and who want to run Unified CVP call and
                                          application reports.

### Obtain Cisco Unified
                           	 Customer Voice Portal Report Templates

To import Unified
                                 		  CVP report templates complete the following:

Step 1

On the Unified
                                          			 CVP Reporting Server, click Start .

Step 2

In the search
                                          			 box, type %CVP_HOME%\CVP_Reporting_Templates and press Enter .

Step 3

Compress the reports into a zip folder and copy it to the system from which you will run Unified Intelligence Center Administration.

### Create Data Source
                           	 for Cisco Unified CVP Report Data

Perform the following procedure to create a data source.

Step 1

Log in to the Unified Intelligence Center at https:// <hostname/ IP address of CUIC Publisher> :8444/cuicui .

Step 2

Select the Data Sources drawer to open the Data Sources page.

Step 3

Click New to open New Data Source page.

Step 4

Complete fields
                                          			 on this page as follows:

Field

Value

Name

Enter
                                                         							 the name of this data source.

Report Designers and Report Definition Designers do not have access to the Data
                                                         							 Sources page but can see the list of Data Sources when they create custom
                                                         							 reports. To benefit those users, give a new Data Source a meaningful name.

Description

Enter
                                                         							 a description for this data source.

Data Source Type

Choose Informix .

Host Settings

Database Host

Enter the IP address or hostname for the Unified CVP Reporting server.

Port

Enter
                                                         							 the port number. Typically, the port is 1526.

You
                                                         							 may have to open this port in the CVP Reporting Server firewall (Windows
                                                         							 Firewall > Advanced Settings > Inbound rules > new rule).

Database Name

Enter the name of the reporting database on the Unified CVP reporting server. The database name can be cvp_data or callback .

Instance

Specify the instance name of the desired database. By default, this is cvp.

Timezone

Choose
                                                         							 the correct time zone for the data stored in the database. In locations that
                                                         							 change from Standard Time to Daylight Savings Time, this time zone is updated
                                                         							 automatically.

Authentication Settings

Database User ID

Enter the user ID of the Reporting User  to access the Unified CVP reporting database.

(The
                                                         							 cvp_dbuser account is created automatically during Unified CVP Reporting server
                                                         							 installation.)

Password and Confirm
                                                            								Password

Enter and confirm the password for the database user.

Charset

Choose UTF-8.

Default Permissions

View or edit the permissions for this datasource for My Group and for the All
                                                         							 Users group.

Max Pool Size

Select the maximum pool size.

Value ranges from 5-200. The default Max Pool Size value is 100 and is common for both the primary and secondary data source
                                                         tabs.

Step 5

Click Test
                                             				Connection .

If the status
                                             				is not Online, review the error message to determine the cause and edit the
                                             				data source accordingly.

Step 6

Click Save to close the Add Data Source window.

The new data
                                             				source appears on the Data Sources list.

### Import Unified CVP Report Templates in Unified Intelligence Center

You can import a report (XML) and the associated template help file (ZIP format) into Cisco Unified Intelligence Center.

Step 1

Launch the Unified Intelligence Center web application at https://<Hostname/IP Address of CUIC Publisher>:8444/cuic

Step 2

From the left navigation pane, click Reports .

Step 3

On the Reports toolbar, click New > Import .

Step 4

Navigate to the folder where you want to import the report.

If you are importing a stock report bundle from Cisco.com, it must be placed at the Reports folder level.

Step 5

Click Import Report .

Step 6

In the File Name (XML or ZIP file) field, click Choose File .

Step 7

Browse to and select the XML or the compressed report file, and click Open .

Step 8

From the Data source for ReportDefinition drop-down list, select a data source used by the report definition.

This field appears only if the Report Definition for the report being imported is not currently defined in Unified Intelligence
                                                         Center.

Step 9

From the Data Source for ValueList drop-down list, select the data source used by the value lists defined in the report definition.

You have to select a data source for the value list only if it does not use the same data source as the Report Definition.
                                                         For Report Definitions of Real Time Streaming, it is mandatory to select a data source for the Value Lists.

Step 10

In the Save To field, browse to the folder where you want to place the imported report. Use the arrow keys to expand the folders.

Step 11

Click Import .

## Configure VVB

If you have configured VXML Gateway, it is not mandatory to configure Virtualized Voice Browser (VVB). You may configure either
                                             VVB or VXML Gateway, or configure both.

The Cisco VVB configurations are site specific. All the VVBs in a site must have the same configurations.

To configure Cisco VVB for all deployments:

Add VVB as an external machine. For more information, see Add External Machines .

Change the default configuration (Optional). For more information, see Cisco Virtualized Voice Browser (VVB) Setup .

Configure SNMP (Optional). For more information, see Configure SNMP .

## Configure Cisco IOS Enterprise Voice Gateway

Tasks to configure the Cisco IOS Enterprise Voice Gateway for Packaged CCE deployment

Task

Common Configuration for the Ingress Gateway and VXML Gateway

Configure Ingress Gateway

Confiugre VXML Gateway (optional)

Configure Codec for Ingress and VXML Gateways

### About Ingress and VXML Gateway Configuration

Complete the following procedures to configure the Ingress Gateway and VXML Gateway. Instructions are applicable to both TDM
                              and Cisco Unified Border Element (CUBE) Voice gateways, unless otherwise noted.

You can add all Gateways as an external machine. For more information, see Add External Machines .

Complete all configuration steps in enable > configuration terminal mode.

### Common
                           	 Configuration for the Ingress Gateway and VXML Gateway

```
logging buffered 2000000 debugging
no logging console	
service timestamps debug datetime msec localtime
ip routing
ip cef	
ip source-route	
interface GigabitEthernet0/0
     ip route-cache same-interface
     duplex auto
     speed auto
     no keepalive
     no cdp enable

voice service voip
          ip address trusted list
          ipv4 0.0.0.0 0.0.0.0 # OR an explicit Source IP Address Trust List
     allow-connections sip to sip
    	signaling forward unconditional
```

### Configure Ingress
                           	 Gateway

Step 1

Configure
                                          			 global settings.

```
voice service voip
	 allow-connections sip to sip
	signaling forward unconditional
	# If this gateway is being licensed as a Cisco UBE the following lines are also required
 mode border-element
 ip address trusted list
  ipv4 0.0.0.0 0.0.0.0               # Or an explicit Source IP Address Trust List
sip
		rel1xx disable
		header-passing
		options-ping 60
  midcall-signaling passthru
```

Step 2

Configure
                                          			 voice codec preference:

```
voice class codec 1
     codec preference 1 g711ulaw
     codec preference 2 g711alaw
     codec preference 3 g729r8
```

Step 3

Configure
                                          			 default services:

To download and transfer the survivability.tcl file to the Ingress Gateway, see File Transfer to Gateway .

```
#Default Services
application
     service survivability flash:survivability.tcl
```

Step 4

Configure
                                          			 gateway and sip-ua timers:

```
gateway
	media-inactivity-criteria all
	timer receive-rtp 1200

sip-ua
	retry invite 2
	retry bye 1
	timers expires 60000
	timers connect 1000
	reason-header override
```

Step 5

Configure
                                          			 POTS dial-peers:

```
# Configure Unified CVP survivability
dial-peer voice 1 pots
     description CVP TDM dial-peer
     service survivability
     incoming called-number .T
     direct-inward-dial
```

This is required for TDM gateways only.

Step 6

Configure the
                                          			 switch leg:

```
#Configure the Switch leg where
# preference is used to distinguish between sides.
# max-conn is used prevent overloading of Unifed CVP
# options-keepalive is used to handle failover
# Note: the example below is for gateways located on the A-side of a geographically
#distributed deployment
# Note: Ensure that you configure switch dial-peers for each Unified CVP server.

dial-peer voice 70021 voip
     description Used for Switch leg SIP Direct
     preference 1
     max-conn 225
     destination-pattern xxxx...... #Customer specific destination pattern
     session protocol sipv2
     session target ipv4:###.###.###.###     #IP Address for Unified CVP, SideA
     session transport tcp
     voice-class codec 1
     voice-class sip options-keepalive up-interval 12 down-interval 65 retry 2
     dtmf-relay rtp-nte
     no vad

dial-peer voice 70022 voip
     description Used for Switch leg SIP Direct
     preference 2
     max-conn 225
     destination-pattern xxxx...... #Customer specific destination pattern
     session protocol sipv2
     session target ipv4:###.###.###.###    #IP Address for Unified CVP, SideB
     session transport tcp
     voice-class codec 1
     voice-class sip options-keepalive up-interval 12 down-interval 65 retry 2
     dtmf-relay rtp-nte
     no vad
```

Step 7

Configure the
                                          			 hardware resources (transcoder, conference bridge, and MTP):

This
                                                         				  configuration section is unnecessary for virtual CUBE or CSR 1000v Gateways.
                                                         				  They do not have physical DSP resources.

```
#For gateways with physical DSP resources, configure Hardware resources using 
#Unified Communications Domain Manager. # Configure the voice-cards share the DSP resources located in Slot0
voice-card 0
     dspfarm
     dsp services dspfarm
voice-card 1
     dspfarm
     dsp services dspfarm
voice-card 2
     dspfarm
     dsp services dspfarm
voice-card 3
     dspfarm
     dsp services dspfarm
voice-card 4
     dspfarm	
     dsp services dspfarm

# Point to the contact center call manager
sccp local GigabitEthernet0/0
     sccp ccm ###.###.###.### identifier 1 priority 1 version 7.0 # Cisco Unified CM sub 1
     sccp ccm ###.###.###.### identifier 2 priority 2 version 7.0 # Cisco Unifed CM sub 2

# Add a SCCP group for each of the hardware resource types
sccp ccm group 1
     associate ccm 1 priority 1
     associate profile 2 register < gatewayname mtp>
     associate profile 1 register < gatewayname conf>
     associate profile 3 register < gatewayname xcode>

# Configure DSPFarms for Conference, MTP and Transcoder

dspfarm profile 1 conference
     codec g711ulaw
     codec g711alaw
     codec g729r8
     maximum sessions 24
     associate application SCCP

dspfarm profile 2 mtp
     codec g711ulaw
     codec g711alaw
     codec g729r8
     maximum sessions software 500
     associate application SCCP

dspfarm profile 3 transcode universal
     codec g711ulaw
     codec g711alaw
     codec g729r8
     maximum sessions 52
     associate application SCCP
```

Step 8

Optional,
                                          			 configure the SIP Trunking:

```
# Configure the resources to be monitored
voice class resource-group 1
     resource cpu 1-min-avg threshold high 80 low 60
     resource ds0
     resource dsp
     resource mem total-mem
     periodic-report interval 30

# Configure one rai target for each CVP Server
sip-ua
     rai target ipv4:###.###.###.### resource-group1 # CVPA
     rai target ipv4:###.###.###.### resource-group1 # CVPB
     permit hostname dns:%Requires manual replacement - ServerGroup Name defined in CVP.System.SIP Server Groups%
```

Step 9

Configure
                                          			 incoming PSTN SIP trunk dial peer:

```
dial-peer voice 70000 voip
     description Incoming Call From PSTN SIP Trunk
     service survivability 
     incoming called-number xxxx……    # Customer specific incoming called-number pattern
     voice-class sip rel1xx disable
     dtmf-relay rtp-nte 
     session protocol sipv2
     voice-class codec 1
     no vad
```

This is required for CUBE only.

### File Transfer to Gateway

Step 1

Download the required .tcl files from %CVP_HOME%\GWDownloads folder.

Step 2

Transfer the .tcl files to the flash memory of the Gateway using FTP.

## Configure Codec for Ingress and VXML Gateways

### Configure Ingress
                           	 Gateway

Step 1

Add the voice
                                          			 class codec 1 to set the codec preference in dial-peer:

#### Example:

```
voice class codec 1
     codec preference 1 g729r8
     codec preference 2 g711alaw
     codec preference 3 g711ulaw
```

```
dial-peer voice 70021 voip
     description Used for Switch leg SIP Direct
     preference 1
     max-conn 225 
     destination-pattern xxxx...... # Customer specific destination
     session protocol sipv2
     session target ipv4:###.###.###.### # IP Address for Unified CVP
     session transport tcp
     voice class codec 1
     voice-class sip options-keepalive up-interval 12 down-interval 65 retry 2
     dtmf-relay rtp-nte
     no vad
```

Step 2

Modify the
                                          			 dial-peer to specify the codec explicitly for a dial-peer:

```
dial-peer voice 9 voip 
     description For Outbound Call for Customer
     destination-pattern <Customer Phone Number Pattern>
     session protocol sipv2
     session target ipv4:<Customer SIP Cloud IP Address>
     session transport tcp
     voice-class sip rel1xx supported "100rel"
     voice-class sip options-keepalive up-interval 12 down-interval 65 retry 2
     dtmf-relay rtp-nte
     codec g711alaw
     no vad

dial-peer voice 10 voip 
     description ***To CUCM Agent Extension For Outbound***
     destination-pattern <Agent Extension Pattern to CUCM>
     session protocol sipv2
     session target ipv4:<CUCM IP Address>
     voice-class sip rel1xx supported "100rel"
     dtmf-relay rtp-nte
     codec g711alaw
```

### Configure VXML
                           	 Gateway

Modify the
                                          			 following dial-peer to specify the codec explicitly for a dial-peer:

```
dial-peer voice 919191 voip
     description Unified CVP SIP ringtone dial-peer
     service ringtone
     incoming called-number 9191T
     voice-class sip rel1xx disable
     dtmf-relay rtp-nte
     codec g711alaw
     no vad

dial-peer voice 929292 voip
     description CVP SIP error dial-peer
     service cvperror
     incoming called-number 9292T
     voice-class sip rel1xx disable
     dtmf-relay rtp-nte
     codec g711alaw
     no vad

dial-peer voice 7777 voip
     description Used for VRU leg #Configure VXML leg where the incoming called
     service bootstrap
     incoming called-number 7777T
     dtmf-relay rtp-nte
     codec g711alaw
     no vad
```

## Configure IPv6

Tasks to configure IPv6 for Packaged CCE deployment

Task

Set Up IPv6 for VOS-Based Contact Center Applications

Configure NAT64 for IPv6-Enabled Deployment

Configure IPv6 on Unified CVP Call Server

Configure Gateways to Support IPv6

Configure IPv6 on Unified Communications Manager

### IPv6 Configuration

Packaged CCE can support IPv6 connections for agent and supervisor Finesse desktops and phones. An IPv6-enabled  deployment
                              can use either all IPv6 endpoints or a mix of IPv4 and IPv6 endpoints. Servers that communicate with these endpoints can accept
                              both IPv4 and IPv6 connections. Communication between servers continues to use IPv4 connections.

This chapter contains the configuration procedures that you perform for IPv6-enabled deployments.

## Set Up IPv6 for
                        	 VOS-Based Contact Center Applications

By default, only IPv4 is enabled for Unified Communications Manager, Cisco Finesse, and Unified Intelligence Center.

If you choose to
                           		enable IPv6 on these applications, you must enable it on both the
                           		publisher/primary nodes and subscriber/secondary nodes for those applications.

You can use Cisco
                           		Unified Operating System Administration or the CLI to enable IPv6.

See the Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html for more information about IPv6 support in Packaged CCE deployments.

### Set Up IPv6 Using
                           	 Cisco Unified Operating System Administration

Step 1

Sign into
                                          			 Cisco Unified Operating System Administration on the Publisher/Primary node:.

Unified
                                                   					 Communications Manager and Unified Intelligence Center: https:// <host or IP address of the Publisher or Primary
                                                         						  node> /cmplatform

Finesse: https:// FQDN of the Primary node :8443/cmplatform

Step 2

Navigate to Settings > IP > Ethernet
                                                				  IPv6 .

Step 3

Check
                                          			 the Enable
                                             				IPv6 check box.

Step 4

Enter values
                                          			 for IPv6Address , Prefix
                                             				Length , and Default Gateway .

Step 5

Check the Update with
                                             				Reboot check box.

Step 6

Click Save .

Step 7

Repeat this
                                          			 procedure on the subscriber/secondary node.

### Set Up IPv6 for
                           	 VOS-Based Applications Using the CLI

Step 1

Access the CLI on the VOS server.

Step 2

To enable or disable IPv6, enter:

Step 3

Set the IPv6 address and prefix length:

#### Example:

Step 4

Set the default gateway:

Step 5

Restart the system for the changes to take effect.

Step 6

To display the IPv6 settings, enter:

## Configure NAT64
                        	 for IPv6-Enabled Deployment

NAT64 allows communication between IPv6 and IPv4 networks. For IPv6-enabled deployments, you must set up NAT64 so that supervisors
                              on an IPv6 network can access Unified CCE Administration web tools on an IPv4 network. You can use either Stateful and Stateless
                              NAT64.

NAT64 is NOT supported on M train IOS. T train is required.

For more information, see the Compatibility Matrix for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html .

The following example network diagram and interface configuration demonstrates Stateful NAT64 translation between an IPv6
                              network and an IPv4 network.

```
interface GigabitEthernet0/0
description ipv4-only interface
 ip address 10.10.10.81 255.255.255.128
 duplex auto
 speed auto
 nat64 enable
 no mop enabled

interface GigabitEthernet0/1
description ipv6-only interface
 no ip address
 duplex auto
 speed auto
 nat64 enable
 ipv6 address 2001::1/64
 ipv6 enable

ipv6 unicast-routing
ipv6 cef
!
nat64 prefix stateful 3001::/96
nat64 v4 pool POOL1 10.10.10.129 10.10.10.250
nat64 v6v4 list V6ACL1 pool POOL1 overload
ipv6 router rip RIPv6
!
ipv6 router rip RIP

!
ipv6 access-list V6ACL1
 permit ipv6 2001::/64 any
```

### Configure DNS for IPv6

To meet the requirement that Unified CCE Administration
                                 		  be accessed by FQDN, a Forward lookup AAAA record for the Unified CCE AW-HDS-DDS servers  and any External HDS servers
                                 must be created in DNS.

The steps in this
                                 		  procedure are for a Windows DNS server.

Step 1

In Windows,
                                          			 navigate to Administrative Tools > DNS . This opens the DNS
                                          			 Manager.

Step 2

In the Forward
                                          			 lookup zone, navigate to your deployment's domain name.

Step 3

Right-click
                                          			 the domain name and select New
                                             				Host (A or AAAA) .

Step 4

In the New
                                          			 Host dialog box, enter the computer name and IP address of the Unified CCE AW-HDS-DDS servers and any External HDS  servers.
                                          Click Add Host .

#### Determine IPv6
                              	 Translation of IPv4 Address for DNS Entry

You can determine the IPv6 address needed for the AAAA DNS record by running a ping command on any Windows machine using mixed
                                 notation. Type “ping -6” followed by your IPv6 Nat64 Prefix, two colons, and then the IPv4 address.

In the ping
                                 		response, the IPv4 address is converted to the hexadecimal equivalent. Use this
                                 		address in your static AAAA record.

Optionally, DNS64
                                             		  can be used in place of static DNS entries. Use of DNS64 helps facilitate
                                             		  translation between IPv6 and IPv4 networks by synthesizing AAAA resource
                                             		  records from A resource records.

## Configure IPv6 on
                        	 Unified CVP Call Server

For IPv6-enabled
                              		  deployments, you must add an IPv6 address to your Unified CVP Call Server's
                              		  existing network interface.

Perform this procedure only if you have an IPv6-enabled
                              		  environment.

Step 1

On the
                                       			 Unified CVP Call Server, navigate to Control
                                             				  Panel > Network and Sharing .

Step 2

Click Ethernet .

Step 3

From the Ethernet Status window, select Properties .

Step 4

Check the Internet Protocol Version 6 (TCP/IPv6) check box,
                                       			 and choose Properties .

Step 5

Choose Use
                                          				the following IPv6 address radio button.

Step 6

Enter values
                                       			 in the IPv6
                                          				address , Subnet
                                          				prefix length , and Default gateway fields.

Step 7

Click OK and restart Windows when prompted.

## Configure Gateways to Support IPv6

For IPv6-enabled deployments, you must configure your Ingress and VXML gateways to enable IPv6 addressing.

### Configure an
                           	 Interface to Support IPv6 Protocol Stack

This procedure applies to the Ingress.

Configure the following on the Gateway:

```
>Enable
>configure terminal
>interface type number
>ipv6 address{ ipv6-address / prefix-length | prefix-name sub-bits / prefix-length}
>ipv6 enable
```

### Enable ANAT in
                           	 Ingress Gateway

Configure the following on the Gateway:

```
>conf t
>voice service voip
>SIP
>ANAT
>bind control source-interface GigabitEthernet0/2
>bind media source-interface GigabitEthernet0/2
```

### Enable Dual Stack
                           	 in the Ingress Gateway

Configure the following on the Gateway:

```
>conf t
>sip-ua
>protocol mode dual-stack preference ipv6
```

## Configure IPv6 on
                        	 Unified Communications Manager

### Cluster-Wide
                           	 Configuration in Unified CM Administration

Perform the
                                 		  following procedure to set IPv6 as the addressing mode preference for media and
                                 		  signaling cluster-wide.

Step 1

From Cisco
                                             				Unified CM Administration , choose System > Enterprise Parameters > IPv6 Configuration Modes to configure
                                          			 the cluster-wide IPv6 settings for each Unified Communications Manager server.

Step 2

From the Enable
                                             				IPv6 drop-down list, choose True .

Step 3

From the IP
                                             				Addressing Mode Preference for Media drop-down list, choose IPv6 .

Step 4

From the IP
                                             				Addressing Mode Preference for Signaling drop-down list, choose IPv6 .

Step 5

From the Allow
                                             				Auto-configuration for Phones drop-down list, choose Off .

Step 6

Save your
                                          			 changes.

### Transcoding

In an IPv6-enabled environment, a transcoder is required for the following scenarios:

An agent logged in to an IPv6 endpoint needs to send or receive transfers from an agent logged in to an IPv4 endpoint.

An agent logged in to an IPv6 endpoint needs to connect to a
                                       			 VXML Gateway for self service.

### Add a Common
                           	 Device Configuration Profile in Unified Communications Manager

In an IPv6-enabled environment, you may have both IPv4 and IPv6 devices.

Perform the
                                 		  following procedure  to add an IPv4, IPv6, or dual stack common device configuration
                                 		  profile in Unified Communications Manager.

Step 1

From Cisco
                                             				Unified CM Administration , choose Device > Device Settings > Common Device Configuration .

Step 2

Click Add
                                             				New and enter the name of the new common device configuration
                                          			 profile.

Step 3

From the IP
                                             				Addressing Mode drop-down list:

- To add an IPv6 common device configuration profile in Unified Communications Manager, choose IPv6
                                                				only .

- To add an IPv4 common device configuration profile in Unified Communications Manager, choose IPv4 only .

- To add a dual stack common device configuration profile in Unified Communications Manager, choose IPv4 and IPv6 . Then choose IPv4 from the IP Addressing Mode Preference for Signaling drop-down list.

Step 4

Save your
                                          			 changes.

### Associate the
                           	 Common Device Configuration Profile with Gateway Trunk

Perform the
                                 		  following procedure to associate the common device configuration profile
                                 		  with the Gateway trunk. 
                                 		This procedure applies to the Ingress Gateway.

Step 1

From Cisco
                                             				Unified CM Administration , choose Device > Trunk .

Step 2

Click Find .

Step 3

From the Common
                                             				Device Configuration drop-down list:

- To associate the IPv6 common device configuration profile with the Gateway trunk, choose the IPv6 common device configuration
                                             profile.

- To
                                             						associate the IPv4 common device configuration profile with the Gateway trunk,
                                             						choose the IPv4 common device configuration profile.

Unified
                                                         						CM gateway trunk supports only an IPv4 or IPv6 trunk. You cannot associate a
                                                         						dual stack common device configuration profile to a Unified CM gateway trunk.

Step 4

Enter the IPv6
                                          			 address in the Destination Address IPv6 field.

Unified CM
                                                         				  to Gateway trunk supports only standard SIP Profile and does not support ANAT
                                                         				  enabled dual-stack SIP trunk.

Step 5

Save your
                                          			 changes.

### Associate the
                           	 Common Device Configuration Profile with an IPv4 or IPv6 Phone

Step 1

From Cisco
                                             				Unified CM Administration , choose Device > Phone .

Step 2

Click Find .

Step 3

From the Common
                                             				Device Configuration drop-down list: choose the IPv6 common device
                                          			 configuration profile.

- To associate the IPv6 common device configuration profile to an IPv6 phone, choose the IPv6 common device configuration profile.

- To associate the IPv4 common device configuration profile to an IPv4 phone, choose the IPv4 common device configuration profle.

Step 4

Save your
                                          			 changes.

### Associate a SIP
                           	 Profile in Unified CM

In an IPv6-enabled deployment, you must associate a SIP profile with the trunk you configured for Unified CVP.

Step 1

From Cisco
                                             				Unified CM Administration , choose Device > Trunk .

Step 2

Click Find . Choose the trunk profile that you want to
                                          			 view.

Step 3

From the SIP
                                             				Profile drop-down list, choose the SIP Profile you created.

For more information on how to create a SIP Profile, see

Step 4

Save your
                                          			 change.

### Associate the Dual
                           	 Stack Common Device Configuration Profile with SIP Trunk

Step 1

From Cisco
                                             				Unified CM Administration , choose Device > Trunk .

Step 2

Click Find . Choose the trunk profile that you want to
                                          			 view.

Step 3

From the Common
                                             				Device Configuration drop-down list, choose the Dual Stack Common
                                          			 Device Configuration Profile.

For more
                                                         				  information on how to add a Dual Stack Common Device Configuration Profile, see Add a Common Device Configuration Profile in Unified Communications Manager .

Step 4

Save your
                                          			 change.

## Packaged CCE 4000 Agents Deployment

Follow this sequence to configure components for Packaged CCE 4000 Agents deployment.

Sequence

Task

1

Generate CSR and upload CA Certificates

Or

Generate and import Self-signed Certificates

2

Configure CCE Component

3

Configure Cisco Unified Customer Voice Portal

4

If Media Server is external, Configure Media Server

5

Configure Cisco Unified Communications Manager

6

Configure Cisco Unified Intelligence Center

7

Configure Cisco Finesse

8

Configure Live Data

9

Configure Cisco Identity Service

10

Configure Cisco Unified Customer Voice Portal Reporting Server (optional)

11

Configure VVB (optional)

12

Configure Cisco IOS Enterprise Voice Gateway

13

Configure IPv6

14

Configure Enterprise Chat and Email (ECE) (optional)

Email and Chat

### Configure CCE Component

Follow this sequence to configure components for Packaged CCE 4000 Agents deployment.

Sequence

Task

1

Configure SQL Server for CCE Components

2

Set up Organizational Units

3

Configure Rogger

4

Configure AW-HDS-DDS

5

Start Unified CCE Services

6

If you have PG VMs installed, Add Unified CCE Instance on all PG VMs

7

Configure Packaged CCE Deployment Type

8

Configure Cisco Unified Contact Center Enterprise PG

9

For configuration using Configuration Manager, see Packaged CCE 4000 and 12000 Agent Supported Tools

#### Configure Rogger

Follow this sequence to configure Rogger for Packaged CCE 4000 Agents deployment.

Sequence

Task

1

Add Unified CCE Instance

2

Create Logger Database

3

To use Outbound Option, see Create Outbound Option Database

4

Add Logger Component to Instance

5

Add Router Component to Instance

6

Cisco SNMP Setup (optional)

##### Create Logger
                                 	 Database

Perform this procedure on the Side A and Side B Logger/Rogger VM.

Step 1

From Unified CCE Tools, open the ICMDBA tool, and click Yes at any warnings that display.

Step 2

Navigate to Server > Instances .

Step 3

Right-click
                                                			 the instance name and choose Create to create the logger database.

Step 4

In the Select
                                                			 Component dialog box, choose the logger you are working on (Logger A or Logger
                                                			 B). Click OK .

Step 5

At the prompt, "SQL Server
                                                   				is not configured properly. Do you want to configure it now?" , click Yes .

Step 6

On the
                                                			 Configure page, in the SQL Server Configurations pane check Memory
                                                   				(MB) and Recovery Interval . Click OK .

Step 7

On the Stop
                                                			 Server page, click Yes to stop the services.

Step 8

In the Select
                                                			 Logger Type dialog box, choose Enterprise . Click OK to open the Create Database dialog box.

Step 9

Create the
                                                			 Logger database and log as follows:

In the DB Type field, choose the Side (A or B).

In the region field, choose your region.

In the Create Database dialog box, click Add to open the Add Device dialog box.

Click Data .

Choose the drive on which you want to create the database, for example, the E drive.

For the Size field, consider whether to choose the default (which is 1.4GB, a fairly minimal size) or calculate a value appropriate for
                                                      your deployment by using the Database Size Estimator Tool. If you calculate the value, enter it here.

You can use the Database Size Estimator Tool only after the database is created.

Click OK to return to the Create Database dialog box.

Click Add again.

In the Add Device dialog box, click Log .

Choose the drive where you created the database.

In the Size field, choose the default setting or, if you have calculated an appropriate size for your deployment, enter that value.

Click OK to return to the Create Database dialog box.

Step 10

In the Create
                                                			 Database dialog box, click Create , then click Start .

Step 11

When you see
                                                			 the successful creation message, click OK and then Close .

##### Create Outbound
                                 	 Option Database

Outbound Option
                                       		  uses its own SQL database on the Logger. Perform the following procedure on the
                                       		  Side A Logger only.

Step 1

Open the
                                                			 ICMDBA tool and click Yes to any warnings.

Step 2

Navigate to Servers > <Logger Server> > Instances > <Unified CCE
                                                      				  instance> > LoggerA . Right-click the instance name
                                                			 and select Database > Create .

Step 3

On the Stop
                                                			 Server message, click Yes to stop the services.

Step 4

In the Create
                                                			 Database dialog box, click Add to open the Add Device dialog box.

Step 5

Click Data , and choose the drive on which you want to create the database, for example, the E drive. In the database size field, you
                                                can choose to retain the default value or enter a required value.

Step 6

Click OK to return to the Create Database dialog box.

Step 7

In the Add Device dialog box, click Log . Choose the desired drive. Retain the default value in the log size field and click OK to return to the Create Database dialog box.

Step 8

In the Create
                                                			 Database dialog box, click Create , and then click Start . When you see the successful creation message,
                                                			 click OK and then click Close .

For more information about configuring Outbound Options, see the Outbound Option Guide for Unified Contact Center Enterprise guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html

##### Add Logger
                                 	 Component to Instance

Perform
                                       		  this procedure on the Side A and Side B Loggers.

Step 1

Open the Web
                                                			 Setup tool.

Step 2

Choose Component Management > Loggers . Click Add , and then choose the instance.

Step 3

On the
                                                			 Deployment page, select the Logger (A or B). Click Duplexed , and then click Next .

Step 4

On the Central Controller Connectivity page, enter the host names for Sides A and B for the Router Private Interface and Logger Private Interface . Enter the SQL port for Side A and B in the Logger SQL Port section. Then, click Next .

The default SQL port is 1433. If the SQL server is configured with custom port, provide the custom port.

Step 5

Check Enable Historical/Detail Data Replication .

Step 6

On the
                                                			 Additional Options page, click Display Database Purge Configuration Steps .

Step 7

Click the Enable Outbound Option check box.

If this Logger is being added for a Rogger server, where there are two IP addresses that are configured on the public Network
                                                               Interface Card (for IP-based prioritization), uncheck "Register this connection's addresses in DNS" for the private ethernet
                                                               card. In addition, ensure that there is only one A-record entry in the DNS server corresponding to the host name of the server,
                                                               which maps to the general priority IP address. This is necessary for processes like the campaign manager and replication running
                                                               as part of the Logger service, to listen on the right interface IP address for client connections.

Step 8

If you enable High Availability, enter the Active Directory Account Name that the opposite side logger runs under or a security group that includes that account. For example, if you are running
                                                Websetup on the logger on Side A, enter the name of the Active Directory account (or security group) that is run on Side B
                                                logger.

Step 9

Select the Syslog box to enable the Syslog event feed process (cw2kfeed.exe).

Step 10

Click Next .

Step 11

On the Data
                                                			 Retention page, modify the Database Retention Configuration table:

For these
                                                      				  tables, set the retention period to 40 days:

Application_Event

Event

Network_Event

Route_Call_Detail

Route_Call_Variable

Termination_Call_Detail

Termination_Call_Variable

Accept the
                                                      				  default settings for all other tables. If your contact center requires access
                                                      				  to any of that data for a longer period, enter an appropriate value.

Step 12

Click Next .

Step 13

On the Data
                                                			 Purge page, configure purges for a day of the week and a time when there is low
                                                			 demand on the system.

Step 14

Accept the
                                                			 default Automatic Purge at Percent Full .

Step 15

Click Next .

Step 16

Check the following check box on the Logger Security page to configure secure communication between CCE core components:

Logger and Router: Enable secure connection between Logger and Router

Logger and its peers: Enable secure data recovery between Logger and Logger

Logger and AW-HDS-DDS: Enable secure data replication between Logger and AW-HDS-DDS and Enable secure-only connection

Campaign Manager process and the Dialer: Enable secure connection between Campaign Manager and Dialer and Enable secure-only connection

To allow both secure and non-secure replication processes to connect to AW-HDS, uncheck the Enable secure-only connection checkbox. This runs the Logger replication process in mixed mode.

To permit both secure and non-secure Dialer processes to connect, uncheck the Enable secure-only connection checkbox. This runs the Campaign Manager process in mixed mode.

Step 17

Click Next .

Step 18

Click Finish .

##### Add Router
                                 	 Component to Instance

Perform this procedure for Side A and Side B Routers.

To fulfill the virtual memory requirement for Router in 48000 deployment, you must configure the Router service on both Side
                                                   A and Side B to launch the Router process (router.exe) as a 64-bit application. To change your Router process build architecture
                                                   from 32-bit to 64-bit, install 12.6(2) ES4 and perform the steps mentioned in the Readme file on the Software Downloads page.
                                                   You must deploy 12.6(2) ES25 for logger.

Step 1

In the Web
                                                			 Setup tool, select Component Management > Routers .

Step 2

Click Add .

Step 3

On the Deployment page, choose the current instance.

Step 4

In the Deployment dialog, select the appropriate side.

Step 5

Click Duplexed , and then click Next .

Step 6

In the Router Connectivity dialog, configure the Private Interface and Public Interfaces. Click Next .

For the address input fields, use Fully Qualified Domain Names instead of IP addresses.

When there are two IP addresses configured on the public Network Interface Card (for IP-based prioritization), manually add
                                                               two A-records on the DNS server. One A-record is for the high priority IP address and the other one is for the general priority
                                                               IP address. The host part of the two DNS entires should be different from the hostname of Windows server. Use the new DNS
                                                               entries to configure the interfaces. This note applies to the Router and to all PG machines.

Step 7

Leave the Enable Peripheral Gateways field blank, and click Next .

Step 8

In the Router Options dialog, the Enable Quality of Service (QoS) is enabled by default. Click Next .

Step 9

In the Router
                                                   				Quality of Service dialog, click Next .

Step 10

To configure secure communication between the Router and CCE core components on Router Security page, check the required check box as given below:

Router and its peer and Logger: Enable secure connection between Router and its Peer and Logger

Router and Peripheral Gateways: Enable secure connection between Router and Peripheral Gateways and Enable secure-only connection

Real Time Server process running in the Router and the Real Time Distributor process running in the AW Distributor: Enable secure connection between Router and AW Distributors and Enable secure-only connection

To allow both secure and non-secure Peripheral Gateways to connect, uncheck the Enable secure-only connection check box. This will run the Router in mixed mode.

To enable both secure and non-secure Real Time Distributor processes to connect, uncheck the Enable secure-only connection check box. This will run the Router (Real Time Server) in mixed mode.

Step 11

In the Summary dialog, make sure that the Router summary is
                                                			 correct, then click Finish .

##### Start Unified CCE Services

The Unified CCE components run as a Windows service on the host computer. You can start, stop, or cycle these services from the Unified CCE Service Control tool on the desktop.

Step 1

On each Unified CCE Server machine, open Unified CCE Service Control .

Step 2

Select each Unified CCE Component in the following sequence and click Start .

Logger A

Router A

Logger B

Router B

Administration & Data Servers

### Configure AW-HDS-DDS

Follow this sequence to configure AW-HDS-DDS for Packaged CCE 4000 Agents deployment.

Sequence

Task

1

Configure SQL Server for CCE Components

2

Add Unified CCE Instance

3

Create HDS Database

4

Add Administration and Data Server Component to Instance

5

Configure ICM Database Lookup (optional)

6

Cisco SNMP Setup (optional)

#### Create HDS Database

Perform this procedure on the Administration & Data Server on which you want to create the HDS database.

Step 1

Open the ICMDBA tool, and click Yes at any warnings that display.

Step 2

Navigate to Servers > Instances .

Step 3

Right-click the instance name and choose Create .

Step 4

In the Select Component dialog box, choose Administration & Data Server . Click OK .

Step 5

At the prompt "SQL Server is not configured properly. Do you want to configure it now?" , click Yes .

Step 6

On the Configure dialog box, click OK .

Step 7

On the Select AW Type dialog box, choose Enterprise . Click OK to open the Create Database dialog box.

Step 8

Create the HDS database as follows:

From the DB Type drop-down list, choose HDS .

Click Add .

On the Add Device dialog box, select Data .

From the Available Drives list, choose the drive on which you want to install the database.

In the Size field, you can leave the default value or enter an appropriate size for your deployment.

You can use the Database Size Estimator Tool to calculate the appropriate size for your deployment.

Click OK to return to the Create Database dialog box.

Click Add .

On the Add Device dialog box, select Log .

From the Available Drives list, choose the drive on which you created the database.

In the Size field, you can leave the default value or enter an appropriate size for your deployment.

Click OK to return to the Create Database dialog box.

Step 9

On the Create Database dialog box, click Create and then click Start .

Step 10

When you see the successful creation message, click OK and then click Close .

#### Add Administration and Data Server Component to Instance

## Configure Packaged CCE  Deployment Type

When you configure the Packaged CCE 4000 Agents and 12000 Agents deployment types, you must add a main site. A main or remote
                           site can have zero or more peripheral sets associated with it. Peripheral set is a collection of all components (like Finesse,
                           CVP, and so on) that are dependent on peripheral gateway (including the peripheral gateway itself). For information on how
                           to add peripheral sets, see Add and Maintain Peripheral Set .

You can add a remote site even with a single VVB. This is helpful in getting control over the traffic, and keeping it local
                           to the same data center.

For example, PSTN delivers SIP trunk to both the Data Centers (DCs). You must retain the traffic local to each DC. If the
                           traffic is delivered to DC1, select the VVB and Nuance Speech Server (NSS) from DC1. If the traffic is delivered to DC2, select
                           the VVB and NSS from DC2. This is achieved by adding a remote site only with VVB. From the VVB, NSS points to the SPOG.

### Add and Maintain Main Site in 4000 Agents or 12000 Agents Deployment Type

Step 1

Navigate to the Unified CCE Administration > Overview > Infrastructure Settings > Deployment Settings .

Step 2

Click the gear icon in the Deployment Type .

Step 3

Select the deployment type as Packaged CCE: 4000 Agents or Packaged CCE: 12000 Agents from the drop-down list.

Step 4

Use the Download Template to get the CSV template for the selected deployment type.

Step 5

Fill the particulars in the file and save it.

Column

Description

Required?

Permissible Values

name

Unique identifier for the machine

Yes

Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         underscore (_), or hyphen (-).

machineType

MachineType Enum name

Yes

Mandatory machines are:

CCE_ROGGER (applicable for 4000 Agents deployment)

CCE_ROUTER (applicable for 12000 Agents deployment)

CCE_LOGGER (applicable for 12000 Agents deployment)

CCE_AW

CUIC_PUBLISHER

CUIC_SUBSCRIBER

LIVE_DATA

IDS_PUBLISHER

IDS_SUBSCRIBER

Optional machines:

CCE_PG

CVP

FINESSE_PRIMARY

FINESSE_SECONDARY

CM_PUBLISHER

CM_SUBSCRIBER

HDS

ECE (refers to ECE Data Server VM for ECE 400 agents and Services Server VM for ECE 1500 agents)

ECE_WEB_SERVER

CVP_REPORTING

GATEWAYS

CVVB

CCCSP

SOCIAL_MINER

THIRD_PARTY_

MULTICHANNEL

MEDIA_SERVER

THIRD_PARTY_GATEWAY

publicAddress

Public address

Yes

Valid IP address or hostname

connectionInfo

Connection information of the machine

Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CCCSP , GATEWAY and LIVE_DATA

Enter the username and password in the following format:

```
userName=<user>&password=<password>
```

For more information on the credentials of each component, see Table 1 .

ConnectionInfo is optional if you are configuring FTP for CVP (Media Server) .

```
userName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber>
```

Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D".

Semicolon (;) delimits the Windows Administration credentials from FTP credentials.

privateAddress

Private address

Required for ROGGER, ROUTER, LOGGER, and PG

Valid IP address or hostname

peripheralSetName

Peripheral set name

Required for PG, CUCM, Finesse, CVP

Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         or an underscore (_).

side

Side information

Yes

sideA

sideB

Step 6

Upload the file and click Next .

Step 7

Wait for validation to be completed.

During the validation, tasks are performed depending on the components defined in the CSV template. For more information about
                                             the tasks, see the Automated Initialization Tasks for 4000 and 12000 Agent Deployments topic.

If any of the performed tasks fails, then all the tasks are reverted.

If validation fails, then click Back to fix the issues in the file and upload the file again, else click Done .

#### Automated Initialization Tasks for 4000 and 12000 Agent Deployments

Packaged CCE performs the following tasks during initialization.

Component

Automated Initialization Tasks

Other Dependent Components

Unified CCE PG

Creates the Agent Peripheral Gateway (PG) and PIMs

Cisco Unified Communications Manager (CUCM) and Cisco Finesse

Creates the Media Routing PG (MR PG), without PIMs

None

Creates the VRU PG and PIMs

Unified Customer Voice Portal

Creates the routing client for each peripheral

Depending on your call flow requirements, create Network VRU labels in the Label list option using the Configuration Manager Tool.

Network VRU Type 10 and Type 2 must be created in the Network VRU Explorer  using Configuration Manager Tool. For more information, see the online help in Configuration Manager Tool .

None

Unified Customer Voice Portal

Configures the Unified CVP Call Server components

Configures the Unified CVP VXML Server components

Configures the Unified CVP Media Server components

None

Unified CVP Reporting Server

Configures the Unified CVP Reporting Server components (not applicable for peripheral set)

None

Live Data

Redeploys Lives data

CUCM and Cisco Finesse

## System Inventory for Packaged CCE 4000 Agents and 12000 Agents Deployment

You can access the Inventory after you have completed the change to a Packaged CCE deployment.

Access the Inventory by navigating to the Unified CCE Administration > Infrastructure > Inventory .

System Inventory contents are updated when you select or change the deployment type and after regular system scans. If a system
                              scan detects VMs that do not conform to Packaged CCE requirements, the Configure your deployment pop-up window opens automatically, detailing the errors. You can access the Inventory again after you have corrected the
                              errors and completed the Configure your deployment popup window.

For more details on Server Status rules, see the Monitor Server Status Rules for Packaged CCE 4000 and 12000 Agents Deployments .

Once a Packaged CCE deployment is initialized, you cannot switch to another Packaged CCE deployment type, including Packaged
                                          Lab Mode. However, you can switch to a Unified CCE deployment type.

Set the Principal AW

Only one AW machine can be Principal AW at a time.

Specifying the Principal AW is required. The first SideA AW machine in the CSV file is the principal AW.

The Principal AW is used by the following features:

File Transfer

Context Service Registration

SSO Registration and Enablement

Differential Sync

You can change the Principal AW by selecting a different AW in the Inventory. Set the AW on which you make most of your configuration
                                          changes as the Principal AW.

To set the Principal AW:

Click the AW to open the Edit CCE AW window.

Check the PrincipalAW check box.

Unified CCE Diagnostic Framework Service domain, username, and password. These credentials must be of a domain user who is
                                                a member of the Config security group for the instance, and valid on all Unified CCE components in your deployment (the Side
                                                A and Side B Unified CCE Roggers, PGs, and AW-HDS-DDSs). Make sure that the Unified CCE Diagnostic Framework Service on each
                                                Unified CCE server is running.

Every time the Active Directory credentials are updated, the credentials configured here must be updated as well.

Click Save .

Set the Principal VVB

Only one of the VVB machines can be a Principal VVB.

Principal VVB is used to configure the Customer Virtual Assistant feature.

First added VVB machine into the Inventory is set as the Principal VVB by default. In Upgrade scenario, one of the configured
                                          VVBs is set as a Principal VVB.

To set a VVB as a Principal VVB, do the following:

Click the VVB to open the Edit VVB window.

Check the Principal check box.

Click Save .

View Statistics

Unified CVP and CVP Reporting Server

You can launch statistics by hovering over the following VMs and clicking the Statistics icon:

Unified CVP

Unified CVP Reporting

For more information, see Unified CVP Statistics and Unified CVP Reporting Statistics .

If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                          system inventory.

### Add Unified CCE
                           	 Instance

Step 1

Open the Unified CCE Web Setup tool from shortcut on your desktop.

Step 2

Sign in as a
                                          			 domain user with local administrator rights.

Step 3

Click Instance Management , and then click Add .

Step 4

On the Add
                                             			 Instance page, from the drop-down list, choose the customer Facility and Instance .

Step 5

Enter an
                                          			 instance number.

The same
                                             				instance name can occur more than once in a domain, so the instance number
                                             				provides the uniqueness. The instance number must be between 0 and 24. The
                                             				instance number must match for the same instance across your entire deployment.
                                             				For an Enterprise (single instance) deployment, select 0 unless there are
                                             				reasons to select another value.

Step 6

For Logger and Administrator & Data server, enter the custom SQL server port to the Local SQL Server Port field.

The default SQL port is 1433. If the SQL server is configured with custom port, provide the custom port.

Step 7

Click Save .

### Monitor Server Status Rules for Packaged CCE 4000 and 12000 Agents Deployments

Green, if the machine is reachable.

Red, if the machine is not reachable.

If any machine in the Inventory is updated, it can take approximately three minutes for the status to appear.

## Configure Cisco Unified Contact Center Enterprise PG

Repeat the following tasks each time you add the Peripheral Set to the Main Site or Remote Site. See the section "Add and
                                       Maintain Peripheral Set" for information on Peripheral Set.

Configuration Tasks

If the Peripheral Set contains CUCM PG:

Install Cisco JTAPI Client on PG

Install Cisco JTAPI Client on PG

Set up CTI Server

If the peripheral set contains VRU PG, manually restart the CVP Servers.

## Install Cisco JTAPI Client on PG

After setting up the Cisco Unified Communications Manager (CUCM) PG, you must install the Cisco JTAPI client. PG uses Cisco
                              JTAPI to communicate with CUCM. Install the Cisco JTAPI client from CUCM Administration.

Continue with the steps provided in this
                                          					section if you are installing the JTAPI client for CUCM version earlier than
                                          					Release 12.5.

To install the JTAPI client for CUCM, Release 12.5 and above, see Install Cisco JTAPI Client on PG .

### Before you begin

Before you install the JTAPI client, ensure that the previous version is uninstalled.

Step 1

Open a browser
                                       			 window on the PG machine.

Step 2

Enter the URL for the Unified Communications Manager Administration utility: http://< Unified Communications Manager machine name> /ccmadmin.

Step 3

Enter the username and password that you created while installing and
                                       					configuring the Unified Communications Manager.

Step 4

Choose Application > Plugins . Click Find .

Step 5

Click the link next to Download Cisco JTAPI for
                                          					Windows .We recommend you to download the 64 bit version. However, if
                                       					you have already downloaded the 32 bit version, you can proceed to step 7.

Download the JTAPI plugin file.

Step 6

Choose Save and save the plugin file to a location of your choice.

Step 7

Open the
                                       			 installer.

Step 8

In the Security Warning box, click Yes to install.

Step 9

Choose Next or Continue through the remaining Setup screens. Accept the default installation path.

Step 10

When prompted for the TFTP Server IP address, enter the CUCM IP address.

Step 11

Click Finish .

Step 12

Reboot the
                                       			 machine.

### Install Cisco JTAPI Client on PG

Complete the following procedure only if you are installing JTAPI client to connect to Cisco Unified Communications Manager,
                                 Release 14.0 and above.

#### Before you begin

Before you install the JTAPI client, ensure that the previous version is uninstalled.

Step 1

Open a browser
                                          			 window on the PG machine.

Step 2

Enter the URL for the Unified Communications Manager Administration utility: http://< Unified Communications Manager machine name> /ccmadmin.

Step 3

Enter the username and password that you created while installing and
                                          					configuring the Unified Communications Manager.

Step 4

Choose Application > Plugins . Click Find .

Step 5

Click the link next to Download Cisco JTAPI Client for
                                                Windows 64 bit or Download Cisco JTAPI Client for
                                                Windows 32 bit.

Download the JTAPI plugin file.

Step 6

Choose Save and save the plugin file to a location of your choice.

Step 7

Unzip the JTAPI plugin zip file to the default location or a location of your
                                          choice.

There are two folders in the unzipped folder CiscoJTAPIx64 and CiscoJTAPIx32 .

Step 8

Run the install64.bat file in the CiscoJTAPIx64 folder or run the install32.bat file in the CiscoJTAPIx32 folder.

The default install path for JTAPI client is C:\Program Files\Cisco\JTAPITools .

Step 9

To accept the default installation path, click Enter and
                                          proceed.

Follow the instructions. Click Enter whenever necessary as
                                             per the instructions.

The JTAPI client installation completes at the default location. The
                                             following message is displayed:

```
Installation Complete.
```

Step 10

Reboot the machine.

#### What to do next

The default location, where the JTAPI client is installed, also contains the uninstall64.bat and uninstall32.bat file. Use this file to uninstall this
                                             version of the client, if necessary.

## Set up CTI Server

Use the PG Setup tool to set up a CTI Server.

### Add CTI Server
                           	 Component

Step 1

Open Peripheral Gateway Setup tool from Unified CCE Tools on the desktop.

Step 2

Click Add in the Instance Components section.

The ICM
                                             				Component Selection dialog box opens.

Step 3

Click CTI
                                             				Server , and click OK .

The CTI Server
                                             				Properties dialog box opens.

### Set CTI Server Properties

Step 1

In the CTI
                                          		  Server Properties dialog box, check Production mode and Auto start at system startup unless your Unified CCE support provider tells you otherwise. These settings set the
                                          			 CTI Server Service startup type to Automatic, so the CTI Server starts
                                          			 automatically when the machine starts up.

Step 2

Check the Duplexed CTI Server option if you are
                                          			 configuring redundant CTI Server machines.

Step 3

In the CG Node Properties section, the numeric portion of the CG
                                          			 node ID must match the PG node ID (for example, CG
                                          			 1 and PG 1).

Step 4

The ICM system ID is the Device Management
                                          			 Protocol (DMP) number of the PG associated with the CTI Gateway. Generally this
                                          			 number is the number associated with the CG ID in step 3.

Step 5

If the CTI Server you add is duplexed, specify which Side you are setting up: Side A or Side B. If
                                          			 the CTI Server is simplex, choose Side A.

Step 6

Click Next .

The CTI Server Component Properties dialog box opens.

### Set CTI Server
                           	 Component Properties

Secured and Non-Secured Connection (Mixed-mode) : Allows secured and non-secured connection between the CTI Server and the CTI clients.

Secured-Only Connection : Allows secured connection between the CTI Server and the CTI clients.

Important

To enable secured connection between the components, ensure to complete the security certificate management process.

For more information, see the chapter Certificate Management for Secured Connections in Security Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html .

In the CTI Server Component Properties dialog box, setup automatically displays the default Secured Connection Port and the Non-Secured Connection Port values. Use these values or change them to the required port numbers. CTI clients use these ports to connect to the CTI Server.

If you have multiple CTI servers running on a single machine, each CTI server must use a different port number set for Secured connection and Mixed-mode connection .

Step 1

Select the appropriate connection type.

For Secured Connection , check the Enable Secure-Only Mode check box.

This option disables the Non-Secured Connection Port field.

For Mixed-mode connection , ensure that the Enable Secure-Only Mode check box is unchecked.

This is the default connection mode.

Step 2

To ensure that an agent is logged in to the client before the client receives events from the CTI Server, check the Agent Login Required for Client Events check box. This ensures that the clients are prevented from accessing data for other agents.

Step 3

Click Next .

The CTI Server
                                             				Network Interface Properties dialog box opens.

### Set CTI Server Network Interface Properties

Step 1

In the CTI Server Network Interface Properties dialog box, in the PG public interfaces section, enter the public network
                                          			 addresses for the PGs associated with the CTI Server.

Step 2

In the CG private interfaces section, enter the private network
                                          			 addresses of the CTI Server.

Step 3

In the CG visible interfaces section, enter the public network addresses of the CTI Server.

Step 4

Click Next .

The Check Setup Information window opens.

### Complete CTI Server Setup

Step 1

In the Check Setup Information window, ensure that the settings
                                          			 displayed are as you intended. If you want to modify any settings before
                                          			 proceeding, use the Back button.

Step 2

When the settings are correct, click Next .

Step 3

The final screen displays and asks whether you want to start the Node Manager now.

Step 4

Click Finish to exit setup (and optionally start the
                                          			 Node Manager).

If you choose to start it, the Node Manager automatically starts
                                             				the other Unified CCE processes on the CTI Server.

## Configure Cisco Unified Customer Voice Portal

The following table outlines the Cisco Unified Customer Voice Portal (CVP) configuration tasks for Packaged 4000 Agents deployment
                           or 12000 Agents deployment.

The CVP configurations are site specific. Side A and Side B configurations per site must be the same.

Configuration Tasks

To secure communication between Call Server and ICM, see Secure Flow Communication .

For more information about securing CVP communication, see Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

CVP Server Services Setup

Configure Media Server

Configure SNMP

### Configure SNMP

Step 1

Log in to the CVP server using Administrator credentials.

Step 2

Navigate to C:\Cisco\CVP\conf\SNMPD.CNF .

Step 3

Complete the following parameters to do the SNMP configuration:

Ensure to enter the parameter values in a single line, without a break.

Parameter

Description

Format

Configure the SNMP agent that runs on the Unified CVP device to use the V1/V2 SNMP protocol to communicate with an SNMP management
                                                         station; add and delete SNMP V1/V2c community strings and associate community strings with the device.

```
snmpCommunityEntry <snmpCommunityIndex> 
<snmpCommunityName> <snmpCommunitySecurityName> 
<snmpCommunityContextEngineID> <snmpCommunityContextName> 
<snmpCommunityTransportTag> <snmpCommunityStorageType>
```

Example:

```
snmpCommunityEntry v2ccvp cvp cvp localSnmpID - - readOnly
```

Configure authentication group for V1/V2C SNMP protocol.

```
vacmSecurityToGroupEntry  <vacmSecurityModel> 
<vacmSecurityName> <vacmGroupName> 
<vacmSecurityToGroupStorageType>
```

Example:

```
vacmSecurityToGroupEntry  snmpv2c cvp 
v2cNoAuthNoPrivGroup nonVolatile
```

Configure the SNMP agent that runs on the Unified CVP device to use the V1/V2 SNMP protocol to communicate with an SNMP management
                                                         station; configure a destination to receive SNMP notifications from an SNMP management station.

```
snmpNotifyEntry <snmpNotifyName> 
<snmpNotifyTag> <snmpNotifyType> <snmpNotifyStorageType>
```

Example:

```
snmpNotifyEntry Descvp Descvp-TrapTag trap readOnly
```

Configure the SNMP agent that runs on the Unified CVP device to use the V3 SNMP protocol to communicate with an SNMP management
                                                         station; add and delete SNMP users and set their access privileges and associate SNMP users with devices.

```
usmUserEntry <usmUserEngineID> 
<usmUserName> <usmUserAuthProtocol> <usmUserPrivProtocol> <usmUserStorageType> 
<usmTargetTag> <AuthKey> <PrivKey>
```

Example:

```
usmUserEntry  localSnmpID < username > usmHMACMD5AuthProtocol usmNoPrivProtocol \
readOnly - password -
```

Ensure that the password is enclosed within "-" as shown in the example. Otherwise, the entry will be discarded and left unencrypted.

Configure the SNMP agent that runs on the Unified CVP device to use the V3 SNMP protocol to communicate with an SNMP management
                                                         station; configure a destination to receive SNMP notifications from an SNMP management station.

```
snmpNotifyEntry <snmpNotifyName> <snmpNotifyTag> 
<snmpNotifyType> <snmpNotifyStorageType>
```

Example:

```
snmpNotifyEntry Descvp Descvp-TrapTag trap readOnly
```

Configure the MIB2 System Group system location settings, and associate the MIB2 System Group with devices.

```
<octetString>
```

Example:

```
MIBLoc
```

Configure the MIB2 System Group system contact and associate the MIB2 System Group with devices.

```
<octetString>
```

For example:

```
MIBContact
```

Configure SNMP trap receiver target IP.

```
snmpTargetAddrEntry  <snmpTargetAddrName> 
<snmpTargetAddrTDomain> <snmpTargetAddrTAddress> 
<snmpTargetAddrTimeout> <snmpTargetAddrRetryCount> 
<snmpTargetAddrTagList> <snmpTargetAddrParams> 
<snmpTargetAddrStorageType> <snmpTargetAddrTMask> 
<snmpTargetAddrMMS>
```

Example:

```
snmpTargetAddrEntry  targetDesV2-Addr1 
snmpUDPDomain 10.100.10.100:0 0 0 \ targetDesV2-TrapTag 
targetDesV2-TrapParams readOnly 255.255.255.255:0 2048
```

Configure the parameters to be used while sending notifications.

```
snmpTargetParamsEntry  <snmpTargetParamsName> 
<snmpTargetParamsMPModel> <snmpTargetParamsSecurityModel> 
<snmpTargetParamsSecurityName> <snmpTargetParamsSecurityLevel> 
<snmpTargetParamsStorageType>
```

Example:

```
snmpTargetParamsEntry  params1 0 
snmpv1 principal noAuthNoPriv 
nonVolatile
```

Step 4

Save the changes.

Step 5

Go to Services and restart Cisco CVP SNMP Management .

## Configure Cisco Unified Communications Manager

The following table outlines the Cisco Unified Communications Manager configuration tasks for Packaged CCE 4000 Agents deployment
                           or 12000 Agents deployment.

.

Task

Set Up Application User

Configure Fully Qualified Domain Name

Configure Cisco Unified Communications Manager Groups

Set Up Device Pool

Configure Conference Bridges

Configure Media Termination Points

Transcoder Configuration in Unified CM and IOS Gateway

Configure Media Resource Groups

Configure and Associate Media Resource Group List

Configure CTI Route Point

Configure Ingress Gateways for Locations-based Call Admission Control

Add a SIP Profile in Unified CM

Configure Trunk

Configure Route Group

Configure Route List

Configure Route Pattern

Configure a Law Codec

Configure SNMP

Configure Agent Desk Settings

### Set Up Device Pool

Complete
                                 		  the following procedure to configure a device pool.

Step 1

Choose System > device
                                                				  pool .

Step 2

Click Add
                                             				new .

Step 3

Provide an
                                          			 appropriate device pool name in Device Pool
                                             				Name .

Step 4

Select a
                                          			 corresponding Call manager group in Cisco Unified
                                             				Communications Manager group .

Step 5

Select appropriate Date/Time Group and Region .

Step 6

Select an
                                          			 appropriate Media resource group list in Media Resource
                                             				Group List.

Step 7

Click Save .

### Set Up Application
                           	 User

Step 1

In Unified Communications Manager, Choose User Management > Application User .

Step 2

In the
                                          			 Application User Configuration window, click Add
                                             				New .

Step 3

Enter the User ID that is set in the Peripheral Gateway Setup.

The <site>_<peripheralsetname>_pguser is set on the PIM when the Peripheral Set is created.

Step 4

Enter a password of your choice, using only ASCII characters .

To change the JTAPI password on the CUCM configuration page:

Open the peripheral Gateway Setup in PG Machine.

Edit the CUCM PG.

Set the same password for the user as previously set in Step 4.

Step 5

Add the application user to the Standard CTI Enabled Group and Role:

Click Add to Access Control Group .

Select the Standard CTI Enabled group.

Select the Standard CTI
                                                   				Allow Control of Phones supporting Connected Xfer and conf group.

Select the Standard CTI
                                                   				Allow Control of Phones supporting Rollover Mode group.

Click Add Selected .

Click Save .

Step 6

Associate the
                                          			 CTI route points and the phones with the application user.

Step 7

Click Save .

### Configure A-Law Codec

Complete the following procedure to configure Unified Communications Manager .

Step 1

Click the System .

Step 2

Select Service Parameters .

Step 3

Select a Server.

Step 4

Select the service as Cisco Call Manager(Active) .

Step 5

Under Clusterwide Parameters (system-location and region), ensure the following:

G.711 A-law Codec Enabled is Enabled .

G7.11 mu-law Codec Enabled to Disabled .

Step 6

Click Save .

### Configure
                           	 SNMP

Step 1

Log in to the Cisco Unified Serviceability (https://hostname of primary server :8443 /ccmservice) using administrator credentials.

Step 2

Select SNMP > V1/V2c > Community
                                                				  String .

Step 3

From Server drop-down list, select the server for
                                          			 which you want to configure a community string and click Find .

Step 4

Click Add
                                             				New to add new community string.

Enter Community String .

#### Example:

In Host IP Addresses Information field, choose Accept SNMP Packets from any host .

From Access Privilages drop-down list, select ReadWriteNotify option.

Check Apply to All Nodes check box to apply community
                                                				  string to all nodes in the cluster.

Click OK .

Click Save .

Click OK .

Step 5

Select SNMP > V1/V2c > Notification
                                                				  Destination .

Step 6

From Server drop-down list, select the server for
                                          			 which you want to configure a notification destination and click Find .

Step 7

Click Add
                                             				New button to add new notification destination.

From Host IP Addresses drop-down list, select Add New .

In Host IP Address field, enter the Prime
                                                				  Collaboration server IP address .

In the Port Number field, enter the notification receiving
                                                				  port number.

In SNMP Version Information field, select the SNMP
                                                				  Version V2C.

In Notification Type Information field; from Notification Type drop-down list, select Trap .

In Community String Information field; from Community String drop-down list, select Community
                                                				  String created in Step 4 from the drop-down list.

Check the Apply to All Nodes check box to apply community
                                                				  string to all nodes.

Click OK .

Click Insert .

Click OK .

### Configure Agent Desk
                           	 Settings

Step 1

From the AW server, open Configuration Manager, choose Configure ICM > Enterprise > Agent Desk Settings > Agent Desk Settings List . The Agent Desk Settings List dialog box opens.

Step 2

Click Retrieve and then Click Add .

Step 3

Fill in the
                                          			 Attributes tab information:

Name . Enter a
                                             				name for the agent desk settings that is unique within the enterprise.

Ring No Answer
                                                				  Time . Enter the number of seconds (between 1 and 120) that a call
                                             				may ring at the agent's station. If you are deploying the Unified CVP, make
                                             				sure this number is less than the number set for the No Answer Timeout for
                                             				Router Requery that you set in the Unified CVP.

If you configure
                                             				this timer, you do not need to configure the Unified Communications Manager
                                             				Call Forward on No Answer for agent extensions in the Unified Communications
                                             				Manager, unless you want them to be used when the agent is not logged in. If
                                             				you set the Unified Communications Manager Call Forward No Answer time, enter a
                                             				value at least 3 seconds higher than the Ring No Answer Time on each Unified
                                             				Communications Manager node.

Ring no answer dialed
                                                				  number . Enter the Unified CCE DN associated with the routing script
                                             				that you want to use to reroute a call that an agent has not answered. If you
                                             				are deploying the Unified CVP, leave this field blank.

Logout non-activity
                                                				  Time . Enter the number of seconds (between 10 and 7200) in which
                                             				the agent can remain in Not Ready state before Unified CCE automatically logs
                                             				out the agent.

Work Mode on
                                                				  Incoming . Select whether wrap-up is required following an incoming
                                             				call. Select an option from the drop-down list.

Work Mode on
                                                				  Outgoing . Select whether wrap-up is required following an outgoing
                                             				call. Select an option from the drop-down list.

Wrap Up Time . Enter the amount of time, in seconds, allocated to an agent to wrap up a call.

Assist Call
                                                				  Method . Select whether Unified CCE creates a consultative call or a
                                             				blind conference call for a supervisor assistance request.

Emergency Alert
                                                				  Method . Select whether the Unified CCE creates a consultative call
                                             				or a blind conference call for an emergency call request.

Blind
                                             				conference is not supported if the call may queue on a VRU.

Description .
                                             				Enter additional optional information about the agent desk settings.

Step 4

Use the
                                          			 following boxes to select or de-select miscellaneous settings:

Auto-answer .
                                             				Indicates whether calls to the agent are automatically answered. The agent is
                                             				not required to take any action to answer the call. If a second call comes in
                                             				while a call is in progress, the call is not automatically answered. This is
                                             				the same behavior as with Unified Communications Manager.

If you enable
                                             				auto-answer, you must also configure the agent phone in Unified Communications
                                             				Manager to turn the speakerphone or headset (or both) to ON. If you turn only the
                                             				headset to ON, the agent must also turn the phone headset button to ON.

In a multi-line
                                             				enabled environment with auto-answer selected, if you are on a call on your
                                             				non-ACD line, the call will not auto-answer. However, if you turn on Unified Communications Manager Auto
                                             				Answer, the call will answer.

Idle Reason
                                                				  Required . Indicates whether an agent is required to enter a reason
                                             				before entering the Idle state.

Logout Reason
                                                				  Required . Indicates whether an agent is required to enter a reason
                                             				before logging out.

Auto Record on
                                                				  Emergency . Indicates in a record request is automatically sent when
                                             				an emergency call request starts.

Cisco Unified Mobile
                                                				  Agent (check box). Enables the Unified Mobile Agent feature so that
                                             				the agent can log in remotely and take calls from any phone. For more
                                             				information about the Unified Mobile Agent, see the Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/products_feature_guides_list.html .

Step 5

Click Save and then click Close .

## Configure Cisco Unified Intelligence Center

Follow this sequence to configure the Cisco Unified Intelligence Center for Packaged CCE 4000 and 12000 Agents deployment

Sequence

Task

2

Configure Unified Intelligence Center Data Sources for External HDS

3

Download Report Bundles

4

Import Reports

5

Configure Unified Intelligence Center Administration

## Configure Cisco Finesse

Follow this sequence to configure the Cisco Finesse for Packaged CCE 4000 Agents deployment or 12000 Agents deployment

Sequence

Task

1

Navigate to Infrastructure Settings > Device Configuration > Finesse to configure, and then select the Site and Peripheral Set of the Finesse server.

Configure Contact Center Enterprise Administration and Data Server Settings

Configure Contact Center Enterprise CTI Server Settings

2

Configure Contact Center Agents and Routing for Live Data Reports

3

Restart the Cisco Tomcat Service

4

Live Data Reports

5

Configure SNMP

### Restart the Cisco
                           	 Tomcat Service

Step 1

Enter utils
                                             				service stop Cisco Tomcat command, to stop the Cisco Tomcat service.

Step 2

Enter utils
                                             				service start Cisco Tomcat command, to start the Cisco Tomcat service.

### Configure Cisco Finesse Administration

Obtain and Upload a CA Certificate

Deploy Certificate in Browsers

Accept security certificates

#### Obtain and Upload
                              	 a CA Certificate

This procedure
                                                			 applies only if you are using HTTPS.

This procedure
                                                			 is optional. If you are using HTTPS, you can choose to obtain and upload a CA
                                                			 certificate or you can choose to use the self-signed certificate provided with
                                                			 Cisco Finesse.

To open Cisco Unified Operating System Administration, enter the following URL in your browser: https://FQDN of primary Finesse server:8443/cmplatform .

Sign in using the
                                    		  username and password for the application user account created during Cisco
                                    		  Finesse installation.

Step 1

Generate a CSR
                                             			 as follows.

Select Security > Certificate Management > Generate
                                                      					 CSR .

From the
                                                   				  certificate name drop-down list, select tomcat .

Click Generate CSR .

Step 2

Download the
                                             			 CSR.

Select Security > Certificate Management > Download
                                                      					 CSR .

From the
                                                   				  certificate name drop-down list, select tomcat .

Click Download CSR .

Step 3

Use the CSR to
                                             			 obtain the signed application certificate and the CA root certificate from the
                                             			 Certificate Authority.

Step 4

When you
                                             			 receive the certificates, select Security > Certificate Management > Upload
                                                				Certificate .

Step 5

Upload the
                                             			 root certificate.

Choose tomcat-trust from Certificate Name drop-down list.

Click Browse and open the root certificate file, in Upload File field.

Click Upload File .

Step 6

Upload the
                                             			 application certificate.

Choose tomcat from Certificate Name drop-down list.

Enter the
                                                   				  name of the CA root certificate in the Root Certificate field.

Click Browse and open the root certificate file, in Upload File field.

Click Upload File .

Step 7

After the
                                             			 upload is complete, sign out from Cisco Finesse.

Step 8

Access the CLI
                                             			 on the primary Cisco Finesse server.

Step 9

Enter utils
                                                				service restart Cisco Finesse Notification Service command to
                                             			 restart the Cisco Finesse Notification service.

Step 10

Enter utils
                                                				service restart Cisco Tomcat command to restart the Cisco Tomcat
                                             			 service.

Step 11

Upload the
                                             			 root certificate and application certificate to the secondary Cisco Finesse
                                             			 server.

Enter the following URL in browser: https://FQDN of secondary Finesse server:8433/cmplatform , to open Cisco Unified Operating System Administration for the secondary server.

Step 12

Access the CLI
                                             			 on the secondary Cisco Finesse server and restart the Cisco Finesse
                                             			 Notification Service and the Cisco Tomcat Service.

## Deploy Certificate in Browsers

### Download CA
                           	 certificate

This procedure
                                 		  assumes that you are using the Windows Certificate Services. Perform the
                                 		  following steps to retrieve the root CA certificate from the certificate
                                 		  authority. After you retrieve the root certificate, each user must install it
                                 		  in the browser used to access Finesse.

Step 1

On the Windows
                                          			 domain controller, run the CLI command certutil -ca.cert ca_name .cer, in which ca_name is the name of your certificate.

Step 2

Save the file.
                                          			 Note where you saved the file so you can retrieve it later.

### Set Up CA
                           	 Certificate for Firefox Browser

Every Firefox user
                                 		  in the system must perform the following steps once to accept the certificate.

To avoid
                                             			 certificate warnings, each user must use the fully-qualified domain name (FQDN)
                                             			 of the Finesse server to access the desktop.

Step 1

From the
                                          			 Firefox browser menu, select Options .

Step 2

Click Advanced .

Step 3

Click the Certificates tab.

Step 4

Click View
                                             				Certificates .

Step 5

Click Authorities .

Step 6

Click Import and browse to the ca_name .cer file (in which ca_name is the name of your certificate).

Step 7

Check the Validate Identical Certificates check box.

Step 8

Restart the browser for certificate installation to take effect.

### Deploy Root Certificate for Browsers

In environments where group policies are enforced via the Active Directory domain, the root certificate can be added automatically
                                 to each user's browser . Adding the certificate automatically simplifies user requirements for configuration.

To avoid
                                             			 certificate warnings, each user must use the fully-qualified domain name (FQDN)
                                             			 of the Finesse server to access the desktop.

Step 1

On the Windows
                                          			 domain controller, navigate to Administrative
                                                				  Tools > Group Policy Management .

Users who have strict Group Policy defined on the Finesse Agent Desktop are required to disable Cross Document Messaging from Group Policy Management to ensure proper functioning of Finesse on browser .

Step 2

Right-click
                                          			 Default Domain Policy and select Edit .

Step 3

In the Group
                                          			 Policy Management Console, go to Computer
                                                				  Configuration > Policies > Window
                                                				  Settings > Security Settings > Public Key
                                                				  Policies .

Step 4

Right-click
                                          			 Trusted Root Certification Authorities and select Import .

Step 5

Import the ca_name .cer file.

Step 6

Go to Computer
                                                				  Configuration > Policies > Windows
                                                				  Settings > Security Settings > Public Key
                                                				  Policies > Certificate Services Client -
                                                				  Auto-Enrollment .

Step 7

From the
                                          			 Configuration Model list, select Enabled .

Step 8

Sign in as a user on a computer that is part of the domain and open browser .

Step 9

If the user
                                          			 does not have the certificate, run the command gpupdate.exe /target:computer /force on the user's
                                          			 computer.

### Set Up CA Certificate for Chrome and Edge Chromium (Microsoft Edge) Browsers

Step 1

In the browser, go to Settings .

Step 2

In the Chrome browser, select Advanced Settings > Privacy and Security , click Manage
                                             Certificates .

Step 3

In the
                                          Microsoft Edge browser, select Privacy, search,
                                             and services . Under Security , click Manage Certificates .

Step 4

Click Trusted Root Certification Authorities tab.

Step 5

Click Import and browse to the ca_name .cer file.

Step 6

Restart the browser for the certificate to install.

### Accept security certificates

Ensure that the pop-ups are enabled for the Finesse desktop.

If you receive a certificate expiry notification, it means that the validity of your CA certificate is about to expire. You
                                 can delete the certificate after expiry. If you use any CA to sign your certificates, you must upload the new certificates
                                 to ensure that your system remains operational. It isn’t required to upload certain CA certificates that come with the platform
                                 and can be deleted when they expire. This update is available from release 12.5(1) SU1 onwards.

After you enter the Finesse desktop URL in your browser, the procedure to add a certificate is as follows:

#### Install certificates on Windows operating system:

The procedure to add a certificate varies for each browser. The procedure for each
                                 browser is as follows:

Firefox

On the Your connection is not secure page, click Advanced > Add Exception .

Ensure that the Permanently store this exception box is checked.

Click Confirm Security Exception .

On the Finesse sign in page, enter your agent ID or username, password, and extension, and click Sign In .

In the SSL Certificate Not Accepted dialog box, click
                                       the certificate link. A browser tab opens for the certificate that you must
                                       accept.

On the browser tab, click I Understand the Risks > Add Exception . Ensure that the Permanently store this exception box is
                                       checked.

Click Confirm Security Exception . The browser tab closes after you accept the certificate and the accepted certificate link is removed from the SSL Certificate Not Accepted dialog box. Close the browser tab if it doesn’t automatically close.

Repeat the preceding steps for all the certificate links. After you accept all the
                                 certificates, the sign-in process is complete.

Chrome and Edge Chromium (Microsoft Edge)

A page appears that states your connection isn’t private. To open the Finesse sign in page,

In Chrome, click Advanced > Proceed to
                                          <Hostname> (unsafe) .

In Microsoft Edge, click Advanced > Continue to <Hostname> (unsafe) .

Enter your agent ID or username, password, and extension, and then click Sign In .

In the SSL Certificate Not Accepted dialog box, click
                                       the certificate link. A browser tab opens for the certificate that you must
                                       accept.

On the browser tab,

In Chrome, click Advanced > Proceed to
                                          <Hostname> (unsafe) .

In Microsoft Edge, click Advanced > Continue to <Hostname> (unsafe) .

The browser tab closes after you accept the certificate and the accepted certificate link is removed from the SSL Certificate Not Accepted dialog box. Close the browser tab if it doesn’t automatically close.

If you click the certificate link and don’t accept it, the certificate link stays enabled in the SSL Certificate Not Accepted dialog box. The certificate error appears every time you sign in. The procedure to permanently accept the certificate is
                                                   as follows.

Click on the certificate error that appears in the address bar and then,

In Chrome, select Certificate (Invalid) .

In Microsoft Edge, select Certificate (not valid) .

The Certificate dialog box appears.

In the Details tab, click Copy to
                                          File . The Certificate Export Wizard appears.

Click Next .

Keep the default selection DER encoded binary X.509
                                          (.CER) and click Next .

Click Browse and select the folder in which you want to save the certificate, enter a recognizable filename and click Save .

Browse to the folder where you’ve saved the certificate ( .cer file), right-click on the file, and click Install Certificate . The Certificate Import Wizard appears.

Keep the default selection Current User and click Next .

Select Place all certificates in the following store and click Browse . The Select Certificate
                                          Store dialog box appears.

Select Trusted Root Certification Authorities and
                                       click OK .

Click Next and then click Finish . A Security Warning dialog box appears that asks if you want to install the certificate.

Click Yes . A Certificate Import dialog box that states the import was successful appears.

Close the browser and sign in to Finesse. The security error doesn’t appear in the address bar.

#### Install certificates on macOS:

The procedure to download a certificate varies for each browser. The procedure for
                                 each browser is as follows:

Chrome and Edge Chromium (Microsoft Edge)

A warning page appears which states that your connection isn’t private. To open the Finesse Console sign in page.

In Chrome, click Advanced > Proceed to
                                          <Hostname> (unsafe) .

In Microsoft Edge, click Advanced > Continue to <Hostname> (unsafe) .

Click on the certificate error that appears in the address bar and then,

In Chrome, select Certificate (Invalid) .

In Microsoft Edge, select Certificate (Not Valid) .

A certificate dialog box appears with the certificate details.

Drag the Certificate icon to the desktop.

Double-click the certificate. The Keychain Access application
                                       opens.

In the right pane of the Keychains dialog, browse to the certificate, right-click on the certificate, and select Get Info from the options that are listed. A dialog appears with more information about the certificate.

Expand Trust . From the When using this
                                          certificate drop-down, select Always
                                          Trust .

Close the dialog box that has more information about the certificate. A
                                       confirmation dialog box appears.

Authenticate the modification of Keychains by providing a password.

The certificate is now trusted, and the certificate error doesn’t appear on the address bar.

Firefox

In your Firefox browser enter the Finesse desktop URL . A warning page appears which states that there’s a security risk.

Click Advanced and then click the View Certificate link. The Certificate Viewer dialog box appears.

Click Details and then click Export . Save the certificate ( .crt file)
                                       in a local folder.

If the .crt file option isn’t available, select the .der option to save the certificate.

From the menu, select Firefox > Preferences . The Preferences page is displayed.

In the left pane, select Privacy & Security .

Scroll to the Certificates section and click View Certificates ... . The Certificate
                                          Manager window is displayed.

Click Import and select the certificate.

The certificate is now authorized, and the certificate error doesn’t appear on the address bar.

## Configure Live Data

Sequence

Task

1

2

Configure Live Data Machine Services

3

Configure Live Data for Unified Intelligence Center Data Sources

4

Configure Cross Origin Resource Sharing (CORS) for Live Data

5

Restart Live Data

6

Set Up Certificates for Live Data

7

Configure SNMP

### Configure Live
                           	 Data with AW

Configure Live Data with AW to access the primary AW DB and the secondary AW DB. The command also automatically tests the
                                 connection from Live Data to the primary or secondary AW, checks to see if you (as the configured user) have appropriate AW
                                 DB access, and reports the results.

You can use the optional skip-test parameter if you do not want to perform the test. When you include the skip-test parameter,
                                 the command does not check if you (as the configured user) have appropriate AW DB access and does not report results.

You do not need to configure the AW DB on both the Publisher and the Subscriber.  The configuration is replicated between
                                             the Publisher and Subscriber.

#### Before you begin

Before you can configure Live Data, you must first configure a SQL user (with special permissions) to work with Live Data.

The SQL administrative user "sa" or a user with sysadmin privileges must then run the following SQL queries on the primary system database for the SQL user who is configured to work with Live
                                 Data:

```
USE master
GO
GRANT CONTROL ON CERTIFICATE :: UCCESymmetricKeyCertificate TO " <user> "
GRANT VIEW DEFINITION ON SYMMETRIC KEY :: UCCESymmetricKey TO " <user> "
```

Step 1

Log in to your
                                          			 Live Data server.

Step 2

Run the
                                          			 following command to configure Live Data with the primary AW DB. The command
                                          			 automatically tests the connection from Live Data, checks the user permission,
                                          			 and displays results.

The skip-test parameter is optional. Include it only if you do not want to perform the test.

set live-data aw-access primary addr port db user pwd [skip-test]

Step 3

Run the
                                          			 following command to configure Live Data with the secondary AW DB. The command
                                          			 automatically tests the connection from Live Data, checks the user permission,
                                          			 and displays results.

The skip-test parameter is optional. Include it only if you do not want to perform the test.

set live-data aw-access secondary addr port db user pwd [skip-test]

The skip-test parameter is optional. Include it only if you do not want to perform the test.

show live-data aw-access [skip-test]

### Configure SQL User
                           	 Account

Step 1

Launch Microsoft SQL Server Management Studio  on the Unified CCE Administration Client workstation .

Step 2

Navigate to Security > Logins , right-click Logins and select New
                                             				Logins .

Use these steps to create login accounts for the Cisco Unified Intelligence Center reporting data sources and for Finesse connectivity to the AW Database on the Cisco Finesse Administration page.

Step 3

On the General
                                          			 Screen:

Enter the
                                                				  Login Name.

Select SQL Server authentication .

Enter and
                                                				  confirm the password.

Uncheck Enforce password policy .

Step 4

In the Server Roles page, check the following check boxes:

public

securityadmin

serveradmin

setupadmin

sysadmin

Step 5

On the User
                                          			 Mapping page, do the following:

Check the Real-time database and Historical database check boxes.

In Database role memberships pane, check the following check boxes:

db_datareader

db_datawriter

db_ddladmin

db_owner

db_securityadmin

public

Step 6

Click OK .

#### What to do next

Ensure that you configure SQL User Account on both the primary and secondary AW databases.

### Configure Live
                           	 Data Machine Services

This command tells
                                 		  the AW where your Live Data machine services are located.

Whenever you run set live-data machine-services , be sure to also run set live-data cuic-datasource to reconfigure the Live Data data sources for the Unified Intelligence Center. See Configure Live Data for Unified Intelligence Center Data Sources .

If you are using any certificates that are unapproved by Cisco or self-signed certificate, ensure to import the AWDB certificate
                                                   into the Live Data server before you run set live-data machine-services .

Step 1

Log in to your
                                          			 Live Data server.

Step 2

Run the
                                          			 following command to configure the Live Data machine services:

set live-data machine-services awdb-user awdb-pwd

Use the user@domain format to specify the AW database domain user with write-access permission. The domain is a fully qualified domain name (FQDN),
                                             and the username is a user principal name. You must be authorized to change Unified CCE configuration.

The Router and Peripheral Gateway (PG) TIP and TOS connection information is automatically populated for Unified CCE deployments
                                                               that support Live Data.

Cisco Unified Communications Manager (CUCM) PG is supported for Live Data.

Once you have updated the host name of Live Data Server, you need to re-run the below set of commands, otherwise new host
                                                         name will not be accepted.

set live-data machine-services awdb-user awdb-pwd

set live-data cuic-datasource cuic-addr cuic-port cuic-user cuic-pwd

Verify that the show machine-services display changed hostname.

It is necessary for you to re-run the set of commands, otherwise Live data machine services will not be updated with the
                                                         new host name.

### Configure Live Data for Unified Intelligence Center Data Sources

This command tells
                                 		  Unified Intelligence Center how to access Live Data.

If you are using any certificates that are unapproved by Cisco, ensure to import the CUIC certificate into the Live Data server
                                             before you run set live-data machine-services .

Step 1

Log in to your
                                          			 Live Data server.

Step 2

Run the
                                          			 following command to configure your Live Data Unified Intelligence Center data
                                          			 sources:

set live-data cuic-datasource cuic-addr cuic-port cuic-user cuic-pwd

### Configure Cross Origin Resource Sharing (CORS) for Live Data

Live Data CORS commands allow you to configure CORS and hence allow web applications running on different origins to communicate
                              with Live Data and CUIC.

For Unified Intelligence Centre gadgets (Live Data) to load in Cisco Finesse, ensure to:

Enable CORS using utils cuic cors enable and utils live-data cors enable commands.

Set the Finesse host URL in utils cuic cors allowed_origin add URLs and utils live-data cors allowed_origin add URLs commands.

Examples:

https://<finesse-FQDN>

https://<finesse-FQDN>:port

### Restart Live Data

After you complete the configuration procedures for the AW, the Live Data Machine Services, and the Unified Intelligence Center
                                 data source, restart the Live Data system to enable the changes.

Access the Live Data CLI and run the following command:

Whenever a new peripheral gateway that supports Live Data gets deployed and started, its feed will not be available to Live
                                                         Data server automatically. Restart the Live Data server to start the feed from the newly deployed Peripheral Gateway.

### Set Up Certificates for Live Data

For secure Cisco Finesse, Cisco Unified Intelligence Center, and Live Data server-to-server communication, perform any of
                              the following:

Use the self-signed certificates provided with Live Data.

When using self-signed certificates, agents must accept the Live Data certificates in the Finesse desktop when they sign in
                                                before they can use the Live Data gadget.

Produce a Certification Authority (CA) certificate internally.

Obtain and install a Certification Authority (CA) certificate from a third-party vendor.

For complete information, see Certificate for Live Data .

For complete information

### Configure
                           	 SNMP

Step 1

Log in to the Cisco Unified Serviceability (https://hostname of primary server :8443 /ccmservice) using administrator credentials.

Step 2

Select SNMP > V1/V2c > Community
                                                				  String .

Step 3

From Server drop-down list, select the server for
                                          			 which you want to configure a community string and click Find .

Step 4

Click Add
                                             				New to add new community string.

Enter Community String .

#### Example:

In Host IP Addresses Information field, choose Accept SNMP Packets from any host .

From Access Privilages drop-down list, select ReadWriteNotify option.

Check Apply to All Nodes check box to apply community
                                                				  string to all nodes in the cluster.

Click OK .

Click Save .

Click OK .

Step 5

Select SNMP > V1/V2c > Notification
                                                				  Destination .

Step 6

From Server drop-down list, select the server for
                                          			 which you want to configure a notification destination and click Find .

Step 7

Click Add
                                             				New button to add new notification destination.

From Host IP Addresses drop-down list, select Add New .

In Host IP Address field, enter the Prime
                                                				  Collaboration server IP address .

In the Port Number field, enter the notification receiving
                                                				  port number.

In SNMP Version Information field, select the SNMP
                                                				  Version V2C.

In Notification Type Information field; from Notification Type drop-down list, select Trap .

In Community String Information field; from Community String drop-down list, select Community
                                                				  String created in Step 4 from the drop-down list.

Check the Apply to All Nodes check box to apply community
                                                				  string to all nodes.

Click OK .

Click Insert .

Click OK .

## Packaged CCE 12000 Agents Deployment

Follow this sequence to configure components for Packaged CCE 12000 Agents deployment.

Sequence

Task

1

Generate CSR and upload CA Certificates

Or

Generate and import Self-signed Certificates

2

Configure CCE Component

3

Configure Cisco Unified Customer Voice Portal

4

If Media Server is external, Configure Media Server

5

Configure Cisco Unified Communications Manager

6

Configure Cisco Unified Intelligence Center

7

Configure Cisco Finesse

8

Configure Live Data

9

Configure Cisco Identity Service

10

Configure Cisco Unified Customer Voice Portal Reporting Server (optional)

11

Configure VVB (optional)

12

Configure Cisco IOS Enterprise Voice Gateway

13

Configure IPv6

14

Configure Enterprise Chat and Email (ECE) (optional)

Email and Chat

### Configure CCE Component

Follow this sequence to configure components for Packaged CCE 12000 Agents deployment.

Sequence

Task

1

Configure SQL Server for CCE Components

2

Set up Organizational Units

3

Configure Logger

4

Configure Router

5

Configure AW-HDS

6

Configure HDS-DDS

7

Start Unified CCE Services

8

If you have PG VMs installed , Add Unified CCE Instance on all PG VMs

9

Configure Packaged CCE Deployment Type

10

Configure Cisco Unified Contact Center Enterprise PG

11

For configuration using Configuration Manager, see Packaged CCE 4000 and 12000 Agent Supported Tools

#### Configure Logger

Follow this sequence to configure Logger for Packaged CCE 12000 Agents deployment.

Sequence

Task

1

Add Unified CCE Instance

2

Create Logger Database

3

To use Outbound Option, see Create Outbound Option Database

4

Add Logger Component to Instance

5

Cisco SNMP Setup (optional)

#### Configure Router

Follow this sequence to configure Router for Packaged CCE 12000 Agents deployment.

Sequence

Task

1

Add Unified CCE Instance

2

Add Router Component to Instance

3

Cisco SNMP Setup (optional)

#### Configure HDS-DDS

Follow this sequence to configure HDS-DDS for Packaged CCE 12000 Agents deployment.

Sequence

Task

1

Configure SQL Server for CCE Components

2

Add Unified CCE Instance

3

Create HDS Database

4

Add Administration and Data Server Component to Instance

5

Cisco SNMP Setup (optional)

### Configure AW-HDS

Follow this sequence to configure AW-HDS for Packaged CCE 12000 Agents deployment.

Sequence

Task

1

Configure SQL Server for CCE Components

2

Add Unified CCE Instance

3

Create HDS Database

4

Add Administration and Data Server Component to Instance

5

Configure ICM Database Lookup (optional)

6

Cisco SNMP Setup (optional)

#### Configure ICM Database Lookup

You can use Database Lookup Explorer tool in Configuration Manager to view, define, delete, or edit script table from an external
                                    database.

Complete the following procedure to configure ICM Database Lookup.

Step 1

Launch the Unified CCE Web Setup tool.

Step 2

In the Router Options window, select Enable Database Routing .

Step 3

Configure Database Lookup explorer:

Click Start > All programs > Cisco Unified CCE Tools > Administration Tools > Configuration Manager .

Open Tools > Explorer Tools > Database Lookup Explorer.

Configure Script Table and Script Table Column as shown in the following example:

Script Table:

Name: AccountInfo

Side A: \\dblookup1\DBLookup.AccountInfo

Side B: <Update Side B of database here>

Description: <Provide description here>

dblookup1 is external database server name, DBLookup is external database name, and AccountInfo is the table name.

Script Table Column:

Column name: AccountNo

Description: <Provide description here>

Step 4

Use the CCEDataProtect Tool to configure the registry settings in Unified CCE . For more information, see Configure External DBLookUp Registry Value using CCEDataProtect Tool

Step 5

Create the ICM script with the database lookup node with the respective table and lookup value.

The following figure shows AccountInfo as the table name and Call.CallingLineID as the lookup value.

## Packaged CCE Lab Only Deployments

Packaged CCE Lab Mode allows you to install Packaged CCE for demonstration and lab use. You can use all the features in a
                           limited capacity without the need to install a full Packaged CCE deployment on supported hardware. If you exceed the capacity
                           limit of an attribute, you are alerted with error messages that are displayed in Unified CCE Administration .

For procedures to configure and manage contact center operations using the Unified CCE Administration web-based tool, see Packaged CCE Administration .

The following Unified CCE Administration features are not initially available when you change into the Packaged CCE Lab deployment:

System Inventory, available on the Inventory page

Log Collection

Live Data

Single sign-on

### Packaged CCE Lab Only Deployment Components

Packaged CCE Lab Mode allows you to install Packaged CCE for demonstration and lab use. You can use all the features in a
                              limited capacity without the need to install a full Packaged CCE deployment on supported hardware. If you exceed the capacity
                              limit of an attribute, you are alerted with error messages that are displayed in the Unified CCE Administration interface.

Before you begin : If you do not have a CA certificate, import self-signed certificates for the external machines. For more information, see Self-signed Certificates .

Packaged CCE Lab Only deployments can be configured as simplex systems or duplex systems only in 2000 Agents deployment. In
                              a simplex system, all components are installed on Side A and there is no Side B. In a duplex system, components are installed
                              on Side A and Side B.

#### Simplex
                              	 Mode

The Lab Only simplex deployment must consist of the following components:

1 Unified CCE Rogger

1 Unified CCE AW-HDS-DDS

Unified CCE PG

Cisco Unified CVP Server

Cisco Unified CM, functioning as a combined Publisher and Subscriber

1 Cisco Unified Intelligence Center, functioning as a combined Publisher and Subscriber

Cisco Finesse, functioning as both a Publisher and Subscriber

Gateways

SocialMiner

Cisco MediaSense

Cisco Enterprise Chat and
                                             						Email

Third-Party Multichannel

In the System Inventory, the status rules that apply to machines outside of the Packaged Contact Center Enterprise Simplex
                                                   Lab Only deployment returns a blocked status. Status rules which require ESXi host return a blocked status.

Cisco Virtualized Voice Browser

Cisco Unified video address Proxy

Gateways

MediaSense

You can add MediaSense only for the main site.

Cisco Unified CVP Reporting

Adding a Cisco Unified Customer Voice Portal Reporting Server with Inventory CSV is not supported. You can also add it as
                                                   an external server after a successful initialization of inventory.

Cisco Enterprise Chat and Email

Third-Party Multichannel

Media Server

You can add the SocialMiner as an external machine only in the main site.

For more information about the configuration limits for external machines, see the Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html .

#### Duplex
                              	 Mode

The Lab Only duplex
                                 		mode consists of the following components.

In Lab Mode,
                                             		  Packaged CCE does not validate the ESXi host.

##### Side A

Side A must have
                                    		  the following:

1 Unified CCE
                                          				Rogger

1 Unified CCE
                                          				AW-HDS-DDS

1 Unified CCE
                                          				PG

1 Cisco
                                          				Unified CVP Server

1 Unified
                                          				Communications Manager Publisher

1 Unified
                                          				Communications Manager Subscriber

1 Unified
                                          				Intelligence Center Publisher

1 Finesse
                                          				Primary

##### Side B

Side B must have
                                    		  the following:

1 Unified CCE
                                          				Rogger

1 Unified CCE
                                          				AW-HDS-DDS

1 Unified CCE
                                          				PG

1 Cisco
                                          				Unified CVP Server

1 Unified
                                          				Communications Manager Subscriber

1 Unified
                                          				Intelligence Center Subscriber

1 Finesse
                                          				Secondary

##### External

The Lab Only duplex mode can have the following external machines:

Gateways

Cisco Virtualized Voice Browsers

Cisco Contact Center SIP Proxy

SocialMiner

Enterprise Chat and Email

Unified CVP Reporting

MediaSense

Third-Party Multichannel

Media Server

Status rules
                                                			 which require ESXi host returns a status of blocked.

For remote site, you can add the following external machines:

Cisco Unified CVP Reporting

Cisco Enterprise Chat and Email

Third-Party Multichannel

Media Server

SocialMiner can be added as an external machine only in the main site.

For more information on the configuration limits for external machines, see the Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html .

### Initialize the Packaged CCE Lab Mode Deployment

When you sign into
                                 		  Unified CCE Administration for the first time, you are prompted to supply
                                 		  information and credentials for the components in your deployment. Packaged CCE
                                 		  uses this information to configure the components and build the System
                                 		  Inventory.

Once a Packaged CCE deployment is initialized, you cannot switch to another Packaged CCE deployment type, including Packaged
                                             Lab Mode. However, you can switch to a Unified CCE deployment type.

Step 1

On the Inventory page, select Packaged CCE: Lab Mode from the Deployment Type drop-down list, then select an instance from the Instance drop-down list that has been created using Domain Manager. Click Next .

Step 2

Select one of the following options from the Template drop-down list:

Simplex Inventory for Simplex Lab Mode deployment

Duplex Inventory for Duplex Lab Mode deployment

Click Download to download the Inventory Content File Template. Fill out and save the template to your computer. In the required Content File field, browse to the content file you have completed. The content file is validated before the inventory is created. Click Next .

For more information on completing the Inventory Content File Template, see Inventory Content File .

Step 3

On the Settings page do the following:

Select the codec used for Mobile Agent calls from the Mobile Agent Codec drop-down list. The Side A Connection and Side B Connection drop-down lists are
                                                   					 disabled in Lab Only deployment.

For the Automatically create service accounts check box, either:

Leave the check box checked if you want automated initialization to create the service accounts in Active Directory.

These accounts will be created and added to the Service group.

Uncheck the check box if you want to use an existing Active Directory account. Enter the username and password for an existing
                                                         Active Directory user in the same domain as the Packaged CCE servers.

This
                                                         						  account will be added to the Service group.

Click Next .

Step 4

After the automated initialization tasks complete, click Done .

If one of the automated initialization tasks fails, correct the errors and then click Retry .

If the retry is successful, the automated initialization continues.

For some task failures, all completed tasks must be reverted before the task can be retried. You see a message informing you
                                             that the system needs to be reverted to a clean state.

Click OK , and then after the system is in a clean state, click Start Over .

You should restart the Unified CVP Server.

After you initiate Simplex or Duplex Lab Mode deployment, you can also add the following external machines for the main site
                                             on the Inventory page:

Unified CM Publisher

Unified CVP Reporting Server

Contact Center SIP Proxy

Virtualized Voice Browser

Gateway

SocialMiner

MediaSense

Enterprise Chat and Email

Third-party Multichannel

Media Server

Cloud Connect Publisher

To add, edit or delete the external machines on the main site, see System Inventory for Packaged CCE 2000 Agents Deployment .

### Enable system inventory, log collection, and live data using the inventory content file

To use the following Unified CCE Administration features for demonstration purposes, you must provide Packaged CCE with information
                                 and credentials for the systems in your deployment:

System Inventory (available under Inventory page )

Log Collection

Live Data

Single Sign-on

You provide this information using the Inventory Content
                                 File.

If you’re configuring the Packaged CCE Lab Only deployment in Unified CCE Administration as part of the installation process,
                                 you’re prompted to complete and upload the Inventory Content File.

If you switch into the Packaged CCE Lab Only deployment from a different deployment, you complete and upload the Content Inventory
                                 file in Unified CCE Administration from the Bulk Import tool.

In Lab only duplex deployments, the Live Data datasource is created only on the publisher node.

To complete and upload the Content Inventory file in Bulk Import :

Step 1

In the Unified CCE Web Administration click the Bulk Import card on the Overview page . Download the Inventory content file template.

Step 2

Open the file in Microsoft Excel and populate the content file fields as described in the Inventory Content file.

Step 3

Save your changes.

Step 4

Create a new bulk job in Bulk Jobs . In the Content File field, select the inventory content file you created and click Save .

#### Inventory Content
                              	 File

The Inventory
                                    		  content file template contains the following fields:

If a username and/or password contains the "=" or "&" characters, use the encoded value of "%3D" or "%26" respectively.

Field

Description

operation

The
                                                						default is CREATE; do not change the operation.

name

Do not
                                                						change the machine name.

This
                                                            						  field applies only to duplex mode.

machineType

Do not
                                                						change the machine type.

publicAddress

Enter the public IP address or hostname for each machine.

publicAddressServices

CCE_ROGGER - Do not change this field.

CCE_PG - This field specifies services that are
                                                						required for the Unified CCE PG. If the Logical Controller ID for the UCM PG is
                                                						not the default of 5000, change the pairing value for the TIP_PG and TIP_PG_TOS
                                                						services to match the Logical Controller ID. (The Logical Controller ID can be
                                                						found on the Peripheral Gateways tab of System > Information.)

CCE_AW -

This field specifies credentials for the Diagnostic Framework for Unified CCE. Replace user@domain.com and password with credentials
                                                of a domain user who is a member of the Config security group for the instance. The credentials must be valid on all Unified
                                                CCE machines in your deployment.

Every time the Active Directory credentials are updated, the credentials configured here must be updated as well.

CVP - Unified CVP Server Windows credentials

CM_PUBLISHER - This field specifies AXL credentials. Replace user and password with the correct credentials.

CUIC_PUBLISHER - This field specifies the services
                                                						for Unified Intelligence Center. For the Administration credentials and Cisco
                                                						Identity Service credentials, replace user and password with the correct
                                                						credentials. For all other services, do not change the default values.

FINESSE - This field specifies Finesse
                                                						Administration credentials. Replace user and password with the correct
                                                						credentials.

privateAddress

Enter the private IP address or hostname for the CCE_PG and CCE_ROGGER . Leave this field blank for all other machines.

side

Enter
                                                						sideA or sideB.

### Customers Also Viewed

- Implement CA-Signed Certificates in a CCE 12.6 Solution

| Important | The SQLLogin key does not support passwords that contains the following characters: '/', '\', '=', '(', ')', or ',' |
|---|---|

| Note | Only the administrator, domain user with administrator rights, or a local administrator can run the CCE DataProtect Tool,
                                             using <Install Directory>:\icm\bin\CCEDataProtectTool.exe. You must run the CCEDataProtect Tool on every server where DBLookup functionality is used. DBLookup password must contain only ASCII characters. |
|---|---|

| Important | Rekey option will be supported in the future releases only. |
|---|---|

| Step 1 | Run the CCEDataProtect Tool located at <Install Directory>:\icm\bin\CCEDataProtectTool.exe , on every server where DBLookup operations are set up. |
|---|---|
| Step 2 | In the Main menu, press 1 to select DBLookUp , and press Enter . |
| Step 3 | Enter a valid Instance Name for which this option is configured. Note You can run only one instance of CCEDataProtect Tool at a time. | Note | You can run only one instance of CCEDataProtect Tool at a time. |
| Note | You can run only one instance of CCEDataProtect Tool at a time. |
| Step 4 | Press 2 to select Edit and Encrypt , and press Enter . The tool displays the current encrypted value stored in the registry as clear text, if it is already configured. Enter a new Registry Value at the system prompt, and press Enter . Note The maximum limit for the External DBLookUp registry entry is 2048 characters. If you press Enter without entering any value, the system removes the encrypted value stored in the registry. You can use this option to remove
                                                               the encrypted entry. When the system displays the message: Are you sure you want to Edit the Registry Details [Y/N] , press Y and then press Enter . The system updates the Registry with an encrypted value and the system prompts the message: Registry Updated with Encrypted Data Successfully . | Note | The maximum limit for the External DBLookUp registry entry is 2048 characters. If you press Enter without entering any value, the system removes the encrypted value stored in the registry. You can use this option to remove
                                                               the encrypted entry. |
| Note | The maximum limit for the External DBLookUp registry entry is 2048 characters. If you press Enter without entering any value, the system removes the encrypted value stored in the registry. You can use this option to remove
                                                               the encrypted entry. |
| Step 5 | Press 1 to select Decrypt and View , to verify the encrypted password. Note CCEDataProtect Tool generates the following logs in the C:\temp folder. CCEDataProtectTool.log - captures the tool usage by the administrator. CCEDataProtectTool_audit.log - captures the audit details of the tool usage. | Note | CCEDataProtect Tool generates the following logs in the C:\temp folder. CCEDataProtectTool.log - captures the tool usage by the administrator. CCEDataProtectTool_audit.log - captures the audit details of the tool usage. |
| Note | CCEDataProtect Tool generates the following logs in the C:\temp folder. CCEDataProtectTool.log - captures the tool usage by the administrator. CCEDataProtectTool_audit.log - captures the audit details of the tool usage. |

| Note | You can run only one instance of CCEDataProtect Tool at a time. |
|---|---|

| Note | The maximum limit for the External DBLookUp registry entry is 2048 characters. If you press Enter without entering any value, the system removes the encrypted value stored in the registry. You can use this option to remove
                                                               the encrypted entry. |
|---|---|

| Note | CCEDataProtect Tool generates the following logs in the C:\temp folder. CCEDataProtectTool.log - captures the tool usage by the administrator. CCEDataProtectTool_audit.log - captures the audit details of the tool usage. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Generate CSR and upload CA Certificates Or Generate and import Self-signed Certificates |
| 2 | Configure CCE Component |
| 3 | Configure Cisco Unified Customer Voice Portal |
| 4 | If Media Server is external, Configure Media Server |
| 5 | Configure Cisco Unified Communications Manager |
| 6 | Configure Cisco Unified Intelligence Center |
| 7 | Configure Cisco Finesse |
| 8 | Configure Cisco Identity Service |
| 9 | Configure Cisco Unified Customer Voice Portal Reporting Server (optional) |
| 10 | Configure VVB (optional) |
| 11 | Configure Cisco IOS Enterprise Voice Gateway |
| 12 | Configure IPv6 |
| 13 | Configure Enterprise Chat and Email (ECE) (optional) Email and Chat |

| Sequence | Task |
|---|---|
| 1 | Configure SQL Server for CCE Components |
| 2 | Set up Organizational Units |
| 3 | Initialize the Packaged CCE 2000 Agents Deployment Type |
| 4 | Add PIMs to the Media Routing Peripheral Gateway (optional) |
| 5 | Cisco SNMP Setup (optional) |
| 6 | Modify Logger |

| Step 1 | Open Microsoft SQL Server Management Studio . |
|---|---|
| Step 2 | Log in. |
| Step 3 | Expand Security and then Logins . |
| Step 4 | If the
                                             			 BUILTIN\Administrators group is not listed: Right-click Logins and select New Login . Click Search and then Locations to locate BUILTIN in the domain tree. Type Administrators and click Check Name and then OK . Double-click BUILTIN\Administrators . Choose Server Roles . Ensure
                                                   				  that public and sysadmin are both checked. |

| Step 1 | Log in with a Domain Administrator privilege. |
|---|---|
| Step 2 | Open the Domain Manager Tool from Unified CCE Tools
                                          					shortcut on your desktop. |
| Step 3 | Click Select . under Domains . |
| Step 4 | You can add domains through the Select Domains dialog
                                          					box, or you can add a domain manually if the target domain cannot be detected
                                          					automatically. To add domains by using the controls in the Select Domains dialog box: In the left pane under Choose domains, select one or more domains. Click Add to add the selected domains, or click Add All to add all the domains. To add a domain manually: In the field under Enter domain name, enter the fully qualified domain
                                                							name to add. Click Add . Click OK . |

| Step 1 | Log in with a domain administrator privilege and open the Domain Manager Tool from Unified CCE Tools shortcut on the desktop. |
|---|---|
| Step 2 | Choose the
                                          			 domain. |
| Step 3 | If this OU is the first instance, then perform the following steps to add the Cisco_ICM root: Under
                                                				  Cisco root, click Add . Select the
                                                				  OU under which you want to create the Cisco root OU, then click OK . When you
                                                   					 return to the Domain Manager dialog box, the Cisco root OU appears either at
                                                   					 the domain root or under the OU you selected. You can now add the facility. |
| Step 4 | Add the
                                          			 facility OU: Select the
                                                				  Cisco Root OU under which you want to create the facility OU. In the
                                                				  right pane, under Facility, click Add . Enter the
                                                				  name for the Facility, and click OK . |
| Step 5 | Add the
                                          			 instance OU: Navigate
                                                				  to and select the facility OU under which you want to create the instance OU. In the
                                                				  right pane, under Instance, click Add . Enter the
                                                				  instance name and click OK . |
| Step 6 | Click Close . |

| Step 1 | Open the Domain Manager tool and select the Security Group ( Config or Setup ) you want to add a user to. |
|---|---|
| Step 2 | Under Security group, click Members . |
| Step 3 | Under Users, click Add . |
| Step 4 | Select the domain of the user you want to add. |
| Step 5 | (Optional) In the Optional Filter field, choose to further filter by the Name or  User Logon Name, apply the search condition, and enter the search value. |
| Step 6 | Click Search . |
| Step 7 | Select the member you want to add to the Security Group from the search results. |
| Step 8 | Click OK . |

| Note | You can add a domain group to local Administrators group of the server to provide users in domain group administrative permission
                                             on the server, provided the users are immediate members of the domain group. |
|---|---|

| Step 1 | Click Server Manager > Tools > Computer Management . |
|---|---|
| Step 2 | Select Local Users and Groups . |
| Step 3 | Double-click Groups . |
| Step 4 | Right-click Administrators . Select Properties . |
| Step 5 | Click Add and enter the user name or domain group name in the Edit the Object names to select check box. |
| Step 6 | Select Check Names to validate the names. |
| Step 7 | After the name is successfully validated, click OK . |
| Step 8 | Click Apply and OK in the Properties dialog box. |
| Step 9 | Close the Computer Management and Server Manager windows. |

| Note | Once a Packaged CCE deployment is initialized, you cannot switch to another Packaged CCE deployment type, including Packaged
                                          Lab Mode. However, you can switch to a Unified CCE deployment type. |
|---|---|

| Important | Packaged CCE 2000 Agents deployments on Nutanix are supported only after Release 15.0(1)SU2/ES202607 or a later Engineering
                                          Special is installed. The initialization workflow depends on the Engineering Special installed. Before the ES, use the VMware
                                          VM Host workflow. After 15.0(1) SU2/ES202607 or a later Engineering Special is installed, initialize a VMware-based or Nutanix-based
                                          deployment by importing the Packaged CCE 2000 Agents inventory file. |
|---|---|

| Component | Important Considerations |
|---|---|
| Unified CCE | Retains any existing departments and their associations. Allows you to maintain associations within the same department. Any new department created thereafter will be considered Global. |
| Finesse | Disables the automatic synchronization of Reason Labels and Teams, and enables the Reasons gadget within Finesse Administration. |
| Unified Intelligence Center | Disables the automatic creation of supervisor accounts and team collections in Unified Intelligence Center enables AW database
                                             synchronization. |
| Unified Unified CVP Virtualized Voice Browser | OAMP needs to be newly built, and all Unified CVP and Cisco VVB configurations need to be manually set up from the beginning. |

| Step 1 | Sign into Unified CCE Administration using the Active Directory username ( user@domain ) and password ( https://< IP Address >/cceadmin , where <IP Address> is the address of the Side A Unified CCE AW-HDS-DDS ). The Configure your deployment popup window opens automatically. |
|---|---|
| Step 2 | On the Deployment Type page , select a Deployment Type and an Instance from the respective drop-down lists. Be a member of the Setup security group for the instance you select. Click Next . |
| Step 3 | Complete the substep that applies to the Engineering Special installed in your deployment. For VMware and Nutanix deployments with 15.0(1) SU2/ES202607 or a later ES installed, complete the following actions: On the Configure your deployment page, click Download Template to download the Packaged CCE 2000 Agent inventory template. Fill out and save the template to your computer. For more information on completing the template, see Inventory Content File . Click Content File to upload the completed file. Click Next . Note The VM Host and Credentials pages are not displayed after 15.0(1) SU2/ES202607 or a later ES is installed. For VMware deployments running a version earlier than 15.0(1) SU2/ES202607, complete the following steps. On the VM Host page, enter the IP address, Username, and Password for the VMware hosts for Side A and Side B. The VMware hosts are the two servers on which ESXi is installed. The username and password fields are the host login names
                                                      and passwords configured in ESXi. Considerations : User Credentials and Permissions : If you do not want to use the "root" user credentials. You can create user with the Read and Reboot permissions on the hosts. To enable these permissions in the VMware Host Client, set the following in Manage Permissions . Anonymous , View , and Read in Root > System (enabled by default). Reset in Root > VirtualMachine > Interact If you update the ESXi root password in Packaged CCE 2000 agent deployment, be sure to reinitialize the deployment in the
                                                                  Inventory page. Validation The system validates the hardware specifications of the VMware host and verifies if the VMs are configured as per the reference
                                                            design. If the validation is successful, click Next to open the Credentials page. See the Virtualization for Cisco Packaged CCE at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html for hardware specifications. If the validation fails, click Update Hosts to go back to the VM Hosts page and edit the values. Click Retry to run the validation with existing values. Datastores : Datastores used by Cisco VMs should not be shared or used by other third-party VMs. Core Components : Packaged CCE core components include: Unified CCE Rogger Unified CCE AW/HDS/DDS Unified CCE PG Unified CVP Server Finesse Unified Intelligence Center Publisher (with coresident Live Data and Cisco IdS) VM annotations are used to identify Packaged CCE core component VMs. Do not change the default annotations of any of the core
                                                                  component VMs. The following terms are reserved for core component annotations: Cisco, Finesse, Unified Intelligence Center,
                                                                  and Unified CVP. Do not use these reserved terms in the annotations of any of the noncore component VMs. Core components must be on-box, all other components have to be added as external machines. For more information, see the Add External Machines topic in the Packaged CCE Administration and Configuration Guide, Release 11.6(1) at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html All other non-core components are required to be added as an external machine in the Packaged CCE Inventory. On the Credentials page, enter the specified information for each component in your deployment. After entering information for a component,
                                                      click Next . The system validates the credentials that you entered before prompting you for the next component's information. Component Information Required Unified CM Either: The Unified CM Publisher for an on-box Unified Communications Manager deployment. The Unified CM Publisher Name and IP address for an external Unified Communications Manager deployment. Note Only a single Unified CM cluster can be integrated to a single site of Packaged CCE deployment. AXL username and password. Unified CVP Unified CVP Server (Side A) Windows Administration Username and Password. Unified CVP Server (Side B) Windows Administration Username and Password. Unified CCE AW-HDS-DDS Unified CCE Diagnostic Framework Portico domain, username, and password. These credentials must be of a domain user who is a local administrator on all the CCE servers and valid on all Unified CCE
                                                                  components in your deployment (the Side A and Side B Unified CCE Roggers, PGs, and AW-HDS-DDSs). Note Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. Unified Intelligence Center Unified Intelligence Center Administration application username and password. Identity Service Administration username and password. Finesse Finesse Administration username and password. Unified CVP Reporting Unified CVP Reporting Server Windows Administration Username and Password used during server installation. | Note | The VM Host and Credentials pages are not displayed after 15.0(1) SU2/ES202607 or a later ES is installed. | Component | Information Required | Unified CM | Either: The Unified CM Publisher for an on-box Unified Communications Manager deployment. The Unified CM Publisher Name and IP address for an external Unified Communications Manager deployment. Note Only a single Unified CM cluster can be integrated to a single site of Packaged CCE deployment. AXL username and password. | Note | Only a single Unified CM cluster can be integrated to a single site of Packaged CCE deployment. | Unified CVP | Unified CVP Server (Side A) Windows Administration Username and Password. Unified CVP Server (Side B) Windows Administration Username and Password. | Unified CCE AW-HDS-DDS | Unified CCE Diagnostic Framework Portico domain, username, and password. These credentials must be of a domain user who is a local administrator on all the CCE servers and valid on all Unified CCE
                                                                  components in your deployment (the Side A and Side B Unified CCE Roggers, PGs, and AW-HDS-DDSs). Note Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. | Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. | Unified Intelligence Center | Unified Intelligence Center Administration application username and password. Identity Service Administration username and password. | Finesse | Finesse Administration username and password. | Unified CVP Reporting | Unified CVP Reporting Server Windows Administration Username and Password used during server installation. |
| Note | The VM Host and Credentials pages are not displayed after 15.0(1) SU2/ES202607 or a later ES is installed. |
| Component | Information Required |
| Unified CM | Either: The Unified CM Publisher for an on-box Unified Communications Manager deployment. The Unified CM Publisher Name and IP address for an external Unified Communications Manager deployment. Note Only a single Unified CM cluster can be integrated to a single site of Packaged CCE deployment. AXL username and password. | Note | Only a single Unified CM cluster can be integrated to a single site of Packaged CCE deployment. |
| Note | Only a single Unified CM cluster can be integrated to a single site of Packaged CCE deployment. |
| Unified CVP | Unified CVP Server (Side A) Windows Administration Username and Password. Unified CVP Server (Side B) Windows Administration Username and Password. |
| Unified CCE AW-HDS-DDS | Unified CCE Diagnostic Framework Portico domain, username, and password. These credentials must be of a domain user who is a local administrator on all the CCE servers and valid on all Unified CCE
                                                                  components in your deployment (the Side A and Side B Unified CCE Roggers, PGs, and AW-HDS-DDSs). Note Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. | Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
| Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
| Unified Intelligence Center | Unified Intelligence Center Administration application username and password. Identity Service Administration username and password. |
| Finesse | Finesse Administration username and password. |
| Unified CVP Reporting | Unified CVP Reporting Server Windows Administration Username and Password used during server installation. |
| Step 4 | On the Settings page, select the following: Select the codec used for Mobile Agent calls from the Mobile Agent Codec drop-down menu. The codec you select must match the codec specified on the voice gateways. If you have an external Unified Communications Manager, select the Unified CM Subscribers to which the Side A and Side B
                                                Unified CCE PGs connect from the Side A Connection and Side B Connection drop-down menus. Enter the username and password for an existing Active Directory user in the same domain as the Packaged CCE servers. This
                                                account will be added to the Service group. Click Next . The deployment is initialized. The Details dialog box displays the status of the automated initialization tasks. See Automated Initialization Tasks for Components for more information. |
| Step 5 | After the automated initialization tasks complete, click Done . If one of the automated initialization tasks fails, correct the errors and then click Retry . If the retry is successful, the automated initialization continues. For some task failures, all completed tasks must be reverted before the task can be retried. You see a message informing you
                                          that the system needs to be reverted to a clean state. Click OK , and then after the system is in a clean state, click Start Over . |

| Note | The VM Host and Credentials pages are not displayed after 15.0(1) SU2/ES202607 or a later ES is installed. |
|---|---|

| Component | Information Required |
|---|---|
| Unified CM | Either: The Unified CM Publisher for an on-box Unified Communications Manager deployment. The Unified CM Publisher Name and IP address for an external Unified Communications Manager deployment. Note Only a single Unified CM cluster can be integrated to a single site of Packaged CCE deployment. AXL username and password. | Note | Only a single Unified CM cluster can be integrated to a single site of Packaged CCE deployment. |
| Note | Only a single Unified CM cluster can be integrated to a single site of Packaged CCE deployment. |
| Unified CVP | Unified CVP Server (Side A) Windows Administration Username and Password. Unified CVP Server (Side B) Windows Administration Username and Password. |
| Unified CCE AW-HDS-DDS | Unified CCE Diagnostic Framework Portico domain, username, and password. These credentials must be of a domain user who is a local administrator on all the CCE servers and valid on all Unified CCE
                                                                  components in your deployment (the Side A and Side B Unified CCE Roggers, PGs, and AW-HDS-DDSs). Note Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. | Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
| Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
| Unified Intelligence Center | Unified Intelligence Center Administration application username and password. Identity Service Administration username and password. |
| Finesse | Finesse Administration username and password. |
| Unified CVP Reporting | Unified CVP Reporting Server Windows Administration Username and Password used during server installation. |

| Note | Only a single Unified CM cluster can be integrated to a single site of Packaged CCE deployment. |
|---|---|

| Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
|---|---|

| Note | After ES202607 or a later Engineering Special is installed, VM host validation alerts are not generated. |
|---|---|

| Component | Automated Initialization
                                       	Tasks |
|---|---|
| Unified CCE Rogger | Creates the Logger. Creates the Logger database, data size of 130GB and the log
                                                		size of 3GB. Creates the Router. |
| Unified CCE PG | Downloads JTAPI from the Unified Communications Manager, and
                                                		installs it on the Unified CCE PG. Creates the CUCM Peripheral Gateway (PG) with the CUCM PIM. Creates the Media Routing PG (MR PG). Creates the VRU PG with two VRU PIMs. Creates the CTI Server. |
| Unified CCE AW-HDS-DDS | Creates the AW-HDS-DDS. Creates the AW database, data size of 1.4GB and log size of 100MB. Creates the historical database, data size of 450GB and log size of 3GB Creates the Cisco Unified Intelligence Center SQL user account
                                                			that is used for Unified Intelligence Center data sources. Creates the Cisco Finesse SQL user account that is used for
                                                			Cisco Finesse data sources. |
| Outbound | Creates the Outbound database, data size of 1.4GB and log size of 100MB. |
| Unified
                                          			Communications Manager | Creates the Application User that is used to configure the
                                                				Unified CCE PG. |
| Unified
                                          			Customer Voice Portal | Configures the Unified CVP Call Server. Configures the Unified CVP VXML Server. Configures the Unified CVP Media Server. |
| Unified CVP Reporting Server | Initializes the Unified CVP Reporting Server. |
| Unified
                                          			Intelligence Center | Updates the historical and real-time data sources. Disables the AW database synchronization |
| Cisco Finesse | Configures the CTI Server settings. Configures the connection to the AW database. Disables the Reasons gadget in Finesse Administration. |

| Note | After the ES 15.0(1) SU2/ES202607 patch is applied, for Nutanix-based and VMware-based deployments, the system does not support
                                             auto-discovery. Inventory management for these environments is handled exclusively through the CSV import process (For more
                                             information, see Initialize the Packaged CCE 2000 Agents Deployment Type ). Periodic inventory validation is turned off for both VMware and Nutanix platforms. |
|---|---|

| Item | Notes | Actions |
|---|---|---|
| Location | This column indicates that the VMs are either on OnBox Side A , OnBox Side B , or OffBox ( External Machine ). |  |
| Side A | All VMs on Side A are indicated as OnBox Side A in the Location column. . | The System Inventory displays read-only information for the following VMs: Unified CCE Rogger Unified CCE PG Unified CM Subscriber 1 (if on-box) To edit the following VMs, click on the respective rows: Note If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory. Unified CCE AW-HDS-DDS —Diagnostic Framework Service Domain, Username, and Password. Unified CM Publisher (if on-box)—AXL Username and Password. These are the credentials for connecting to the Unified CM Publisher. CUIC-LD-IdS Publisher —Username and Password for Unified Intelligence Center Administration. Username and Password for Identity Service Administration. Unified CVP Server — Unified CVP Server Windows credentials. Configure FTP. For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Finesse Primary —Username and Password for Cisco Finesse Administration. You can launch the administration tool for these VMs by clicking the VM arrow icon: CUIC-LD-IdS Publisher Unified CM Publisher You can perform the full synchronization or differential synchronization of the configurations of various components. For
                                             more information on the machines that support data synchronization, see Device Out of Sync Alerts . Click on the Statistics icon to launch statistics for the following VMs: Unified CVP Unified CVP Reporting For more information, see Unified CVP Statistics and Unified CVP Reporting Statistics . | Note | If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory. |
| Note | If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory. |
| Side B | All VMs on Side B are indicated as OnBox Side B in the Location column. | The System Inventory displays read-only information for the following VMs: Unified CCE Rogger Unified CCE PG Unified CCE AW-HDS-DDS Unified CM Subscriber 2 (if on-box) CUIC-LD-IdS Subscriber Finesse Secondary ECE Data Server To update the VM, click the row corresponding to it. The details of the VM appear for you to make updates. Note If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory. Unified CVP - Unified CVP Server Windows credentials. Configure FTP . For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Unified CVP Reporting - Cisco Unified CVP Reporting Server Windows credentials. If the CVP Reporting server VM is re-imaged or re-installed, you need to initialize the CVP Reporting server. To initialize the CVP Reporting Server , click the Initialize icon and then click Yes to confirm. Note Initialization removes existing call server association and Courtesy Callback configuration. To re-associate call servers with the CVP Reporting server, navigate to Overview > Infrastructure Settings > Device Configuration > Device Configuration . To reconfigure Courtesy Callback, navigate to Overview > Features > Courtesy Callback . You can perform the full synchronization or differential synchronization of the configurations of various components. For
                                             more information on the machines that support data synchronization, see Device Out of Sync Alerts . Click on the Statistics icon to launch statistics for the following VMs: Unified CVP Unified CVP Reporting For more information, see Unified CVP Statistics and Unified CVP Reporting Statistics . | Note | If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory. | Note | Initialization removes existing call server association and Courtesy Callback configuration. To re-associate call servers with the CVP Reporting server, navigate to Overview > Infrastructure Settings > Device Configuration > Device Configuration . To reconfigure Courtesy Callback, navigate to Overview > Features > Courtesy Callback . |
| Note | If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory. |
| Note | Initialization removes existing call server association and Courtesy Callback configuration. To re-associate call servers with the CVP Reporting server, navigate to Overview > Infrastructure Settings > Device Configuration > Device Configuration . To reconfigure Courtesy Callback, navigate to Overview > Features > Courtesy Callback . |
| External Machines | The Location column for every External Machine in the deployment is displayed as OffBox , and can include any of the following: HDS Unified CM Publisher Unified CM Subscriber SocialMiner ECE Data Server (refers to ECE Data Server VM for 400 agents and Services Server VM for ECE 1500 agents) Note If ECE is installed in an HA deployment mode, add only one ECE Data Server in the Unified CCE Administration for 2000 agent
                                                               deployment model. ECE Web Server 3rd Party Multichannel Unified CVP Reporting MediaSense Cisco Contact Center SIP Proxy Virtualized Voice Browser Gateway Cloud Connect Publisher Note When you add or delete the Cloud Connect Publisher, for the change to take effect logout and login to the machine. Media Server Note Unified CM Subscriber machines are dedicated to the contact center. When you configure an external Unified CM Publisher, its
                                                               Unified CM Subscribers are added to the System Inventory automatically. Version information displayed for ECE Data Server is fetched from ECE Web Server. When you configure Cloud Connect Publisher, its Cloud Connect Subscribers are added to the System Inventory automatically. | Note | If ECE is installed in an HA deployment mode, add only one ECE Data Server in the Unified CCE Administration for 2000 agent
                                                               deployment model. | Note | When you add or delete the Cloud Connect Publisher, for the change to take effect logout and login to the machine. | Note | Unified CM Subscriber machines are dedicated to the contact center. When you configure an external Unified CM Publisher, its
                                                               Unified CM Subscribers are added to the System Inventory automatically. Version information displayed for ECE Data Server is fetched from ECE Web Server. When you configure Cloud Connect Publisher, its Cloud Connect Subscribers are added to the System Inventory automatically. | The external HDS and external Unified CM Subscribers are auto detected. You do not need to add or delete them. To add or update the external machines, see Add External Machines . You can perform the full synchronization or differential synchronization of the configurations of various components. For
                                             more information on the machines that support data synchronization, see Device Out of Sync Alerts . Note If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory. Note If you edit the Unified CM Publisher, the Unified CM Subscribers associated with the publisher are updated automatically.
                                                         You cannot edit Unified CM Subscribers from the System Inventory. Note If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                         You cannot edit Cloud Connect Subscribers from the System Inventory. To associate the external HDS with a default Cisco Identity Service (IdS) for single sign-on: Click the external HDS row. The corresponding machine details page appears and you can modify the machine details. Click the Search icon next to Default Identity Service . Enter the machine name for the Cisco IdS in the Search field or choose the Cisco IdS from the list. Click Save . To delete , click the x on the machine. Confirm the deletion. You can open the administration tool for these external machines by clicking the arrow icon in the machine box: Unified CM Publisher SocialMiner MediaSense Note To navigate to the Cisco Webex login page, click the Register link. | Note | If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory. | Note | If you edit the Unified CM Publisher, the Unified CM Subscribers associated with the publisher are updated automatically.
                                                         You cannot edit Unified CM Subscribers from the System Inventory. | Note | If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                         You cannot edit Cloud Connect Subscribers from the System Inventory. | Note | To navigate to the Cisco Webex login page, click the Register link. |
| Note | If ECE is installed in an HA deployment mode, add only one ECE Data Server in the Unified CCE Administration for 2000 agent
                                                               deployment model. |
| Note | When you add or delete the Cloud Connect Publisher, for the change to take effect logout and login to the machine. |
| Note | Unified CM Subscriber machines are dedicated to the contact center. When you configure an external Unified CM Publisher, its
                                                               Unified CM Subscribers are added to the System Inventory automatically. Version information displayed for ECE Data Server is fetched from ECE Web Server. When you configure Cloud Connect Publisher, its Cloud Connect Subscribers are added to the System Inventory automatically. |
| Note | If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory. |
| Note | If you edit the Unified CM Publisher, the Unified CM Subscribers associated with the publisher are updated automatically.
                                                         You cannot edit Unified CM Subscribers from the System Inventory. |
| Note | If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                         You cannot edit Cloud Connect Subscribers from the System Inventory. |
| Note | To navigate to the Cisco Webex login page, click the Register link. |
| Note Principal VVB is used to configure the Customer Virtual Assistant feature. Only one of the VVB machines across sites can be set as a Principal VVB and you cannot delete this machine. First added the VVB machine into the Inventory is set as the Principal VVB by default. In the Upgrade scenario, one of the
                                                               configured VVBs is set as a Principal VVB. A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports the Customer Virtual Assistant feature.
                                                               To set a VVB as a Principal VVB, see Edit External Machines . | Note | Principal VVB is used to configure the Customer Virtual Assistant feature. Only one of the VVB machines across sites can be set as a Principal VVB and you cannot delete this machine. First added the VVB machine into the Inventory is set as the Principal VVB by default. In the Upgrade scenario, one of the
                                                               configured VVBs is set as a Principal VVB. A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports the Customer Virtual Assistant feature.
                                                               To set a VVB as a Principal VVB, see Edit External Machines . |
| Note | Principal VVB is used to configure the Customer Virtual Assistant feature. Only one of the VVB machines across sites can be set as a Principal VVB and you cannot delete this machine. First added the VVB machine into the Inventory is set as the Principal VVB by default. In the Upgrade scenario, one of the
                                                               configured VVBs is set as a Principal VVB. A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports the Customer Virtual Assistant feature.
                                                               To set a VVB as a Principal VVB, see Edit External Machines . |

| Note | If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory. |
|---|---|

| Note | If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory. |
|---|---|

| Note | Initialization removes existing call server association and Courtesy Callback configuration. To re-associate call servers with the CVP Reporting server, navigate to Overview > Infrastructure Settings > Device Configuration > Device Configuration . To reconfigure Courtesy Callback, navigate to Overview > Features > Courtesy Callback . |
|---|---|

| Note | If ECE is installed in an HA deployment mode, add only one ECE Data Server in the Unified CCE Administration for 2000 agent
                                                               deployment model. |
|---|---|

| Note | When you add or delete the Cloud Connect Publisher, for the change to take effect logout and login to the machine. |
|---|---|

| Note | Unified CM Subscriber machines are dedicated to the contact center. When you configure an external Unified CM Publisher, its
                                                               Unified CM Subscribers are added to the System Inventory automatically. Version information displayed for ECE Data Server is fetched from ECE Web Server. When you configure Cloud Connect Publisher, its Cloud Connect Subscribers are added to the System Inventory automatically. |
|---|---|

| Note | If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                                         system inventory. |
|---|---|

| Note | If you edit the Unified CM Publisher, the Unified CM Subscribers associated with the publisher are updated automatically.
                                                         You cannot edit Unified CM Subscribers from the System Inventory. |
|---|---|

| Note | If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                         You cannot edit Cloud Connect Subscribers from the System Inventory. |
|---|---|

| Note | To navigate to the Cisco Webex login page, click the Register link. |
|---|---|

| Note | Principal VVB is used to configure the Customer Virtual Assistant feature. Only one of the VVB machines across sites can be set as a Principal VVB and you cannot delete this machine. First added the VVB machine into the Inventory is set as the Principal VVB by default. In the Upgrade scenario, one of the
                                                               configured VVBs is set as a Principal VVB. A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports the Customer Virtual Assistant feature.
                                                               To set a VVB as a Principal VVB, see Edit External Machines . |
|---|---|

| Note | The System Health and VM server status categories apply only to VMware-based Packaged CCE 2000 Agents deployments before CCE15.0(1) SU2/ES202607 is
                                                installed. After the ES is installed, these VMware host and VM validation rules do not apply to VMware-based or Nutanix-based
                                                Packaged CCE 2000 Agent deployments. |
|---|---|

| Server Status Category | Description | Example Rules |
|---|---|---|
| Configuration | Rules
                                                					for installation and configuration of a component. These
                                                					rules identify problems with mismatched configuration between components,
                                                					missing services, and incorrectly configured services. | Unified CCE Rogger: The trace level must be set to normal to ensure performance. Unified CVP: The names of the SIP Server Groups on CVP containing Communications Manager addresses must match the Communications Manager
                                                Cluster Fully Qualified Domain Name. Cloud Connect: The Cloud Connect Publisher must be configured with the supported cloud services. |
| Operations | Rules
                                                					for the runtime status of a component. These
                                                					rules identify services and processes that cannot be reached, are not running,
                                                					or are not in the expected state. | Unified CCE Rogger: The central controller agent process (ccagent.exe) must be in service for both PGs. Cloud Connect: Type is either Publisher or Subscriber. |
| System Health | Metrics to monitor the CPU, memory, and disk usage of a component's Virtual Machine (VM) as reported by ESXi over the last
                                                10 minutes. The memory and CPU usage may differ slightly from system tools reported by the VM itself. For VM Hosts, these
                                                metrics also include datastore performance information. For VM Hosts under M5 Tested Reference Configuration / Specification Based Configuration, these metrics include CPU reservation,
                                                CPU oversubscription, memory reservation and datastore utilization information. | All: Memory usage as reported by ESXi - 17% For VM Hosts under M5 Tested Reference Configuration / Specification Based Configuration: Maximum CPU Reservation - 65% Maximum CPU Oversubscription - 200% Maximum Memory Reservation - 80% Maximum Storage Usage per Datastore - 80% |
| VM | VM requirements for a component. | All: VMware Tools must be up to date |
| System Validation | Rules for Unified CCE database and configuration settings. These rules identify whether the configuration of objects in your deployment match the requirements and limits for Packaged
                                                Contact Center Enterprise. Note The System Validation category is available only for the Side A Unified CCE AW-HDS-DDS. | Note | The System Validation category is available only for the Side A Unified CCE AW-HDS-DDS. | Side A Unified CCE AW-HDS-DDS: Agent Desk Settings: Ring No Answer Times must not be set. Side A Unified CCE AW-HDS-DDS: Application Gateway Side A Unified CCE AW-HDS-DDS: Application Instance: Up to 12 Application Instances can be defined. |
| Note | The System Validation category is available only for the Side A Unified CCE AW-HDS-DDS. |

| Note | The System Validation category is available only for the Side A Unified CCE AW-HDS-DDS. |
|---|---|

| Note | This section applies only to VMware-based Packaged CCE 2000 Agents deployments before release 15.0(1) SU2/ES202607 is installed.
                                             After the ES is installed, VM validation is not supported for VMware-based or Nutanix-based Packaged CCE 2000 Agents deployments. |
|---|---|

| Configuration Task |
|---|
| Add PIMs to the Media Routing Peripheral Gateway (optional) |

| Step 1 | From the Start menu, enter mmc.exe /32 . |
|---|---|
| Step 2 | From the Console, choose File > Add or Remove Snap-ins . |
| Step 3 | In the Add or Remove Snap-ins dialog box, choose Cisco SNMP Agent Management from the list of available snap-ins. Click Add . |
| Step 4 | In the Selected snap-ins pane, double-click Cisco SNMP Agent Management . |
| Step 5 | In the Extentions for Cisco SNMP Agent Management dialog box, select Always enable all available extentions . Click OK . |
| Step 6 | In the Add/Remove Snap-in window, click OK . The Cisco SNMP Agent Management Snap-in
                                             			 is now loaded into the console. |

| Step 1 | Choose File > Save . |
|---|---|
| Step 2 | In the Filename field, enter Cisco SNMP Agent Management . |
| Step 3 | In the Save As type field, choose a file name to map to the
                                             			 administrative tools such as Microsoft Management Console Files(*.msc) . |
| Step 4 | Click Save . |

| Step 1 | Choose Start > All
                                                   				  Programs > Administrative tools > Cisco
                                                   				  SNMP Agent Management . |
|---|---|
| Step 2 | Right-click Cisco SNMP Agent Management and choose Run as administrator . |
| Step 3 | The Cisco SNMP Agent Management screen lists some of the
                                             			 configurations that require SNMP for traps and system logs. |
| Step 4 | Right-click Community Names (SNMP v1/v2c) and choose Properties . |
| Step 5 | In the Community Names (SNMP v1/v2c) Properties dialog box, click Add New Community . |
| Step 6 | In the Community Name field, enter a community name. |
| Step 7 | In the Host Address List, enter the host IP address. |
| Step 8 | Click Apply and click OK . |

| Step 1 | From the Console Root, choose Cisco SNMP Agent
                                                   				  Management > User Names (SNMP
                                                   				  v3) > Properties . |
|---|---|
| Step 2 | Click Add New User . |
| Step 3 | In the User Name field, enter a username. |
| Step 4 | Click Save . |
| Step 5 | The username appears in the Configured Users pane at the top of
                                             			 the dialog box. |
| Step 6 | Click Apply and click OK . |

| Step 1 | From the Console Root, choose Cisco SNMP Agent
                                                   				  Management > Trap Destinations > Properties . |
|---|---|
| Step 2 | Click Add Trap Entity . |
| Step 3 | Click the SNMP version that your NMS uses. |
| Step 4 | In the Trap Entity Name field, enter a name for the trap entity. |
| Step 5 | Choose the User Name/Community Name that you want to associate
                                             			 with this trap. This list is auto-populated with existing configured
                                             			 users/community names. |
| Step 6 | Enter one or more IP addresses in the IP Address entry field.
                                             			 Click Insert to define the destinations for the
                                             			 traps. |
| Step 7 | Click Apply and click Save to save the new trap destination. The trap entity name appears in the Trap Entities section at the
                                                			 top of the dialog box. |
| Step 8 | Click OK . |

| Step 1 | From the Console Root, choose Cisco SNMP Agent
                                                   				  Management > Syslog
                                                   				  Destinations > Properties . |
|---|---|
| Step 2 | Choose an Instance from the list box. |
| Step 3 | Check Enable Feed . |
| Step 4 | Enter an IP address or host name in the Collector Address field. |
| Step 5 | Click Save . |
| Step 6 | Click OK and restart the logger. |

| Note | This procedure is applicable only after a technology refresh and if you have enabled Outbound Option High Availability |
|---|---|

| Step 1 | Open the Web Setup tool. |
|---|---|
| Step 2 | Choose Component Management > Loggers . |
| Step 3 | Select the required Logger that you want to configure. |
| Step 4 | Click Edit . |
| Step 5 | Click Next twice. |
| Step 6 | Enter the Active Directory Account Name that the opposite side Logger runs under or a security group which includes that account. Note While using Outbound Option High Availability, if you want to change the Logger Public Interface or Active Directory Account Name , you must disable Outbound Option High Availability using logger setup. Only after disabling Outbound Option HA, change the Logger Public Interfaces or Active Directory Account Name , then re-enable Outbound Option High Availability to update the new Logger Public Interface or Active Directory Account Name . | Note | While using Outbound Option High Availability, if you want to change the Logger Public Interface or Active Directory Account Name , you must disable Outbound Option High Availability using logger setup. Only after disabling Outbound Option HA, change the Logger Public Interfaces or Active Directory Account Name , then re-enable Outbound Option High Availability to update the new Logger Public Interface or Active Directory Account Name . |
| Note | While using Outbound Option High Availability, if you want to change the Logger Public Interface or Active Directory Account Name , you must disable Outbound Option High Availability using logger setup. Only after disabling Outbound Option HA, change the Logger Public Interfaces or Active Directory Account Name , then re-enable Outbound Option High Availability to update the new Logger Public Interface or Active Directory Account Name . |
| Step 7 | Click Next . |
| Step 8 | Review the Summary page, and click Finish . For more information, see the Configure the Logger for Outbound Option topic in the Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/series.html . |

| Note | While using Outbound Option High Availability, if you want to change the Logger Public Interface or Active Directory Account Name , you must disable Outbound Option High Availability using logger setup. Only after disabling Outbound Option HA, change the Logger Public Interfaces or Active Directory Account Name , then re-enable Outbound Option High Availability to update the new Logger Public Interface or Active Directory Account Name . |
|---|---|

| Step 1 | Log in to the Side B AW-HDS-DDS Server. |
|---|---|
| Step 2 | Go to Services and restart Apache Tomcat. |

| Note | The CVP configurations are site specific. Side A and Side B configurations per site must be the same. |
|---|---|

| Configuration Tasks |
|---|
| To secure communication between Call Server and ICM, see Secure Flow Communication . For more information about securing CVP communication, see Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| To change the default settings, see CVP Server Services Setup |
| Configure Media Server |
| Configure SNMP |

| Note | At the command prompt, enter more %CVP_HOME%\conf\security.properties . Security.keystorePW = <Returns the keystore password> Enter the keystore password when prompted. |
|---|---|

| Step 1 | Remove the existing certificate by running the following command: %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -delete -alias callserver_certificate |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Generate a new key pair for the alias with the selected key size by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias callserver_certificate
                                                   -v -keysize 2048 -keyalg RSA . Enter keystore password: <enter the keystore password>
What is your first and last name?
 [Unknown]: < Specify the FQDN of the CVP server. Example: cisco-cvp-211@example.com >
What is the name of your organizational unit?
 [Unknown]: <specify OU> E.g. CCBU
What is the name of your organization?
 [Unknown]: <specify the name of the org> E.g. CISCO
What is the name of your City or Locality?
 [Unknown]: <specify the name of the city/locality>  E.g. BLR
What is the name of your State or Province?
 [Unknown]: <specify the name of the state/province>  E.g. KAR
What is the two-letter country code for this unit?
 [Unknown]: <specify two-letter Country code>  E.g. IN

Specify ‘yes’ for the inputs. |
| Step 4 | Generate the CSR certificate for the alias by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias callserver_certificate
                                                   -file %CVP_HOME%\conf\security\callserver.csr and save it to a file (for example, callserver.csr). |
| Step 5 | Enter the keystore password when prompted. |
| Step 6 | Download the callserver.csr from %CVP_HOME%\conf\security\ and sign it from CA. |
| Step 7 | Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\ . |
| Step 8 | Install the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                   root -file %CVP_HOME%\conf\security\<filename_of_root_cert> . |
| Step 9 | Enter the keystore password when prompted. |
| Step 10 | Install the signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                   callserver_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert> . |

| Step 1 | Copy the root CA certificate to the ICM (PG) box. |
|---|---|
| Step 2 | Open the command prompt and go to c:\cisco\icm\bin . |
| Step 3 | Type CiscoCertUtil.exe /install rootCA.pem . This imports the certificate to the Trusted Root Certification
                                                Authorities. |

| Step 1 | Navigate to C:\icm\ssl\keys and remove the old ‘host.key’(if available). |
|---|---|
| Step 2 | Log into the ICM (PG) box. Go to the command prompt and type CiscoCertUtil.exe /generateCSR . C:\icm\bin>CiscoCertUtil.exe /generateCSR SSL config path = C:\icm\ssl\cfg\openssl.cfg
SYSTEM command is C:\icm\ssl\bin\openssl.exe req -new -key C:\icm\ssl\keys\host.key -out C:\icm\ssl\certs\host.csr Generating a 2048 bit RSA private key
.............................
.......
writing new private key to 'C:\icm\ssl\keys\host.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:IN
State or Province Name (full name) [Some-State]:KA
Locality Name (eg, city) []:BLR
Organization Name (eg, company) [Internet Widgits Pty Ltd]:cisco
Organizational Unit Name (eg, section) []:ccbu
Common Name (e.g. server FQDN or YOUR name) []:abc.com
Email Address []:radmohan@cisco.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:*****
An optional company name []:cisco The client certificate and key are generated and stored as host.csr and host.key in C:\icm\ssl\certs and C:\icm\ssl\keys folders respectively. Note To generate ECDSA CSR with default P384 curve, use ciscocertutil.exe /generateCSR /curve command. For
                                                               more details refer to the topic CiscoCertUtil Utility at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html | Note | To generate ECDSA CSR with default P384 curve, use ciscocertutil.exe /generateCSR /curve command. For
                                                               more details refer to the topic CiscoCertUtil Utility at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
| Note | To generate ECDSA CSR with default P384 curve, use ciscocertutil.exe /generateCSR /curve command. For
                                                               more details refer to the topic CiscoCertUtil Utility at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
| Step 3 | Sign it from a CA. Follow the procedure Import Root CA Certificate into ICM . Note Remove the existing host.pem (if any) from C:\icm\ssl\certs . Save host.cer (CA-signed) as host.pem in C:\icm\ssl\certs . | Note | Remove the existing host.pem (if any) from C:\icm\ssl\certs . Save host.cer (CA-signed) as host.pem in C:\icm\ssl\certs . |
| Note | Remove the existing host.pem (if any) from C:\icm\ssl\certs . Save host.cer (CA-signed) as host.pem in C:\icm\ssl\certs . |
| Step 4 | From the command prompt, run C:\icm\bin>CiscoCertUtil.exe /install
                                                   c:\icm\ssl\certs\host.pem . |
| Step 5 | Cycle VRU PG. |

| Note | To generate ECDSA CSR with default P384 curve, use ciscocertutil.exe /generateCSR /curve command. For
                                                               more details refer to the topic CiscoCertUtil Utility at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
|---|---|

| Note | Remove the existing host.pem (if any) from C:\icm\ssl\certs . Save host.cer (CA-signed) as host.pem in C:\icm\ssl\certs . |
|---|---|

| Note | To establish a secure communication, run the commands (given in the links below) in the Command Prompt as an Administrator
                                          (right click over the Command Prompt and select Run as administrator ). |
|---|---|

| Import Self-signed Certificates to Target Server | Generate Self-signed Certificates from Source Component Server | Links |
|---|---|---|
| AW Machines | Unified CCE Components (Router, Logger 1 , Rogger 2 , PGs, AWs, and HDS | Import Unified CCE Component Certificates Import Diagnostic Framework Portico Certificate into AWMachines |
| Customer Voice Portal (CVP) Call Server/CVP Reporting Server | Generate Self-signed WSM Certificate for CVP |
| Email and Chat (ECE) | Import ECE Web Server Certificate into AW Machines |
| Cisco Finesse Primary and Secondary | Import VOS Components Certificate |
| Cisco Unified Communications Manager (CUCM) Publisher and Subscriber |
| Virtualized Voice Browser (VVB) |
| Cisco Unified Intelligence Center (CUIC) Publisher and Subscriber |
| Cisco Identity Service (IdS) Publisher and Subscriber |
| Cloud Connect Publisher and Subscriber |
| Customer Collaboration Platform |
| Live Data Publisher and Subscriber |
| Finesse | AWDB | Import and Export SSC of Finesse to Administration and Data Server Import and Export SSC of Administration and Data Server to Finesse |
| PG | Import and Export Self-Signed Certificate of PG to Finesse Import and Export self-signed certificate of Cisco Finesse to PG |
| Cloud Connect | Export Cloud Connect Certificate Import Cloud Connect Certificate |
| PG | CUCM Publisher | Import VOS Components Certificate |
| Logger | AW | Import Unified CCE Component Certificates |
| Rogger |
| CVP | Import AW Certificate into Cisco Unified CVP Servers |

| Step 1 | http://acrsrv-app-prd-01:8080/ Export the Call Server certificate by
                                                running. %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore
                                                   %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                   callserver_certificate -file
                                                   %CVP_HOME%\conf\security\<callserver_certificate> |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Restart the Call Server service to load the new certificates. |

| Step 1 | Copy the self-signed CVP Call Server certificate downloaded from CVP to the ICM box (PG) . |
|---|---|
| Step 2 | Open the command prompt and go to c:\icm\bin . |
| Step 3 | Type CiscoCertUtil.exe /install
                                                   <callserver_certificate> . This imports the certificate to the Trusted Root Certification Authorities. Note Repeat the procedure for multiple PIMs and for Side A and Side B. | Note | Repeat the procedure for multiple PIMs and for Side A and Side B. |
| Note | Repeat the procedure for multiple PIMs and for Side A and Side B. |

| Note | Repeat the procedure for multiple PIMs and for Side A and Side B. |
|---|---|

| Step 1 | Log into the ICM (PG) box. Go to the command prompt and type CiscoCertUtil.exe /generatecert . C:\icm\bin>ciscocertutil.exe /generatecert SSL config path = C:\icm\ssl\cfg\openssl.cfg
SYSTEM command is C:\icm\ssl\bin\openssl.exe req -x509 -newkey rsa:2048 -days 7300 -nodes -subj /CN=PG-SIDEA.pcce.com -out
C:\icm\ssl\certs\host.pem -keyout C:\icm\ssl\keys\host.key
Generating a RSA private key
..................
....
writing new private key to 'C:\icm\ssl\keys\host.key The client certificate and key are generated and stored as host.csr and host.key in C:\icm\ssl\certs folder. |
|---|---|
| Step 2 | Cycle VRU PG. |

| Step 1 | Log into the CVP Call Server box. Create a folder and copy host.pem to c:\IcmCertificate . |
|---|---|
| Step 2 | From the command prompt, run %CVP_HOME%\jre\bin\keytool.exe -import -v -alias icm_certificate -storetype JCEKS -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore
                                                   -file c:\IcmCertificate\host.pem . |
| Step 3 | Enter the keystore password when prompted. Click Yes . |
| Step 4 | Restart the Callserver service to load the new certificates. Note Repeat the procedure if you have multiple Call Servers. | Note | Repeat the procedure if you have multiple Call Servers. |
| Note | Repeat the procedure if you have multiple Call Servers. |

| Note | Repeat the procedure if you have multiple Call Servers. |
|---|---|

| Configuration Tasks |
|---|
| Configure Fully Qualified Domain Name |
| Configure Cisco Unified Communications Manager Groups |
| Configure Conference Bridges |
| Configure Media Termination Points |
| Transcoder Configuration in Unified CM and IOS Gateway |
| Configure Media Resource Groups |
| Configure and Associate Media Resource Group List |
| Configure CTI Route Point |
| Configure Ingress Gateways for Locations-based Call Admission Control |
| Add a SIP Profile in Unified CM |
| Configure Trunk |
| Configure Route Group |
| Configure Route List |
| Configure Route Pattern |

| Step 1 | Open Cisco Unified Communications Manager and log in. |
|---|---|
| Step 2 | Navigate to System > Enterprise Parameters . |
| Step 3 | Fill in Clusterwide Domain Configuration > Cluster Fully Qualified Domain Name with the Fully Qualified Domain Name of your cluster. Note The Cluster Fully Qualified Domain Name is the name of the Unified Communications Manager Server Group defined in Unified
                                                            CVP. | Note | The Cluster Fully Qualified Domain Name is the name of the Unified Communications Manager Server Group defined in Unified
                                                            CVP. |
| Note | The Cluster Fully Qualified Domain Name is the name of the Unified Communications Manager Server Group defined in Unified
                                                            CVP. |
| Step 4 | Click Save . |

| Note | The Cluster Fully Qualified Domain Name is the name of the Unified Communications Manager Server Group defined in Unified
                                                            CVP. |
|---|---|

| Step 1 | Select  Cisco Unified CM Administrator from the Navigation menu and click Go . |
|---|---|
| Step 2 | Select System > Cisco Unified CM Group . |
| Step 3 | Click Find . Then click Default . |
| Step 4 | Move the two subscribers from the Available panel to the Selected panel. |
| Step 5 | Click Save . |
| Step 6 | Click Reset . |
| Step 7 | On the Device Reset popup, click Reset . |
| Step 8 | Click Close . |

| Step 1 | Select Media
                                                   				  Resources > Conference bridge . |
|---|---|
| Step 2 | Click Add
                                                				New . |
| Step 3 | Select
                                             			 Conference Bridge Type of Cisco
                                                				IOS Conference Bridge . |
| Step 4 | In the Conference Bridge name field, enter a unique
                                             			 identifier for the conference bridge name that matches the configuration on the
                                             			 gateway. In the example,
                                                				this is gw70conf. # Add a SCCP group for each of the hardware resource types
sccp ccm group 1
associate ccm 1 priority 1
associate profile 2 register gw70mtp
associate profile 1 register gw70conf
associate profile 3 register gw70xcode |
| Step 5 | Select a Device
                                             			 Pool. |
| Step 6 | Click Save . |
| Step 7 | Click Apply
                                                				Config . |

| Step 1 | Select Media
                                                   				  Resources > Media Termination Point . |
|---|---|
| Step 2 | Click Add
                                                				New . |
| Step 3 | In the Media
                                             			 Termination Point Name field, enter a unique identifier for the media
                                             			 termination that coincides with the configuration on the gateway. In the example,
                                                				this is gw70mtp. # Add a SCCP group for each of the hardware resource types
sccp ccm group 1
associate ccm 1 priority 1
associate profile 2 register gw70mtp
associate profile 1 register gw70conf
associate profile 3 register gw70xcode |
| Step 4 | Select a Device
                                             			 Pool. |
| Step 5 | Click Save . |
| Step 6 | Click Apply
                                                				Config . |

| Step 1 | In Unified
                                          			 Communications Manager Administration, select Media
                                             				Resources > Transcoder. |
|---|---|
| Step 2 | Click Add
                                             				New . |
| Step 3 | For Transcoder
                                          			 Type, select Cisco IOS enhanced media termination point . |
| Step 4 | In the Device
                                             				Name field, enter a unique identifier for the transcoder name that
                                          			 coincides with the configuration on the gateway. In the following example, this is gw70xcode. # Add a SCCP group for each of the hardware resource types
sccp ccm group 1
associate ccm 1 priority 1
associate profile 2 register gw70mtp
associate profile 1 register gw70conf
associate profile 3 register gw70xcode |
| Step 5 | In the Device Pool field, select the appropriate device pool. |
| Step 6 | Click Save . |
| Step 7 | Click Apply
                                             				Config . |

| Step 1 | Select Media
                                             				  Resources > Media Resource Group . |
|---|---|
| Step 2 | Add a Media
                                       			 Resource Group for Conference Bridges. Click Add
                                                					 New . Enter a
                                             				  Name. From the
                                             				  Available list, select all the Cisco IOS conference bridge resources configured
                                             				  for each ingress/VXML combination gateway in the deployment and add them to the
                                             				  group. Click Save . |
| Step 3 | Add a Media
                                       			 Resource Group for Media Termination Point. Click Add
                                                					 New . Enter a
                                             				  Name. From the
                                             				  Available list, select all the hardware media termination points configured and
                                             				  add them to the group. Click Save . |
| Step 4 | Add a Media
                                       			 Resource Group for Transcoder. Click Add
                                                					 New . Enter a
                                             				  Name. From the
                                             				  Available list, select all the transcoders configured and add them to the
                                             				  group. Click Save . |
| Step 5 | Click Save. |

| Step 1 | Select Media Resources > Media
                                             				  Resource Group List . |
|---|---|
| Step 2 | Click Add New and enter a Name. |
| Step 3 | Add a Media Resource Group list and associate all of the media
                                       			 resource groups. Click Save . |
| Step 4 | Select System > Device
                                             				  Pool . Click Find . Select the appropriate device pool. |
| Step 5 | From the Media Resource Group List drop-down list, choose the
                                       			 media resource group list added in Step 2. |
| Step 6 | Click Save . Click Reset . |

| Step 1 | In Cisco
                                       			 Unified CM Administration, select Device > CTI Route
                                             				  Point . |
|---|---|
| Step 2 | Click Add
                                          				New . |
| Step 3 | Set a device
                                       			 name; for example, PCCEInternalDNs . |
| Step 4 | For Device
                                       			 Pool, select Default . |
| Step 5 | Select a Media
                                       			 Resource Group List from the list. |
| Step 6 | Click Save. |
| Step 7 | Click on Line
                                       			 [1] to configure the directory number associated with this route point. This
                                          				directory number will be a pattern that is intended to match any of the
                                          				internal Dialed Numbers you configure in Packaged CCE for internally routed
                                          				calls. (For instance, for Transfers and Conferences). Important Define a
                                                      				  pattern that is flexible enough to match all your internal dialed numbers yet
                                                      				  restrictive enough not to inadvertently intercept calls intended for other
                                                      				  Route Patterns you may have defined for other parts of your dial plan. Use a
                                                      				  unique prefix for internal calls. For example, if you have internal dialed
                                                      				  numbers 1230000 and 1231111, then an appropriate line number to enter for the
                                                      				  cti route point would be 123XXXX. | Important | Define a
                                                      				  pattern that is flexible enough to match all your internal dialed numbers yet
                                                      				  restrictive enough not to inadvertently intercept calls intended for other
                                                      				  Route Patterns you may have defined for other parts of your dial plan. Use a
                                                      				  unique prefix for internal calls. For example, if you have internal dialed
                                                      				  numbers 1230000 and 1231111, then an appropriate line number to enter for the
                                                      				  cti route point would be 123XXXX. |
| Important | Define a
                                                      				  pattern that is flexible enough to match all your internal dialed numbers yet
                                                      				  restrictive enough not to inadvertently intercept calls intended for other
                                                      				  Route Patterns you may have defined for other parts of your dial plan. Use a
                                                      				  unique prefix for internal calls. For example, if you have internal dialed
                                                      				  numbers 1230000 and 1231111, then an appropriate line number to enter for the
                                                      				  cti route point would be 123XXXX. |
| Step 8 | Select User
                                             				  Management > Application User . |
| Step 9 | Select pguser created during Packaged CCE automated initialization. |
| Step 10 | Select the CTI
                                       			 Route Point from the list of Available Devices , and add it to the list of Controlled Devices . |
| Step 11 | Click Save. |

| Important | Define a
                                                      				  pattern that is flexible enough to match all your internal dialed numbers yet
                                                      				  restrictive enough not to inadvertently intercept calls intended for other
                                                      				  Route Patterns you may have defined for other parts of your dial plan. Use a
                                                      				  unique prefix for internal calls. For example, if you have internal dialed
                                                      				  numbers 1230000 and 1231111, then an appropriate line number to enter for the
                                                      				  cti route point would be 123XXXX. |
|---|---|

| Important | Do not define
                                          			 Unified CVP as a gateway device in Unified Communications Manager. |
|---|---|

| In Cisco Unified CM Administration, define the Ingress gateways as
                                       			 gateway devices. Assign the correct location to the devices. |
|---|

| Step 1 | From Cisco
                                          				Unified CM Administration , choose Device > Device
                                             				  Settings > SIP Profile . |
|---|---|
| Step 2 | Click Add
                                          				New and enter the name of the SIP profile. |
| Step 3 | Check the Enable
                                          				ANAT check box on the SIP Profile. |
| Step 4 | Save your
                                       			 changes. |

| Step 1 | In Unified Cisco
                                       			 CM Administration, select Device > Trunk. |
|---|---|
| Step 2 | Click Add
                                          				New . |
| Step 3 | From the Trunk
                                       			 Type drop-down list, choose SIP
                                          				Trunk , and then click Next . |
| Step 4 | Enter the
                                       			 following in the Device
                                          				Information section: In the Device Name field, enter a name for the SIP trunk, for example, sipTrunkCVPA . In the Device Pool drop-down list, select the device pool
                                             				  that the customer has defined. Select a
                                             				  Media Resource Group List from the list. Make sure
                                             				  that the Media Termination Point Required check box is not
                                             				  checked. |
| Step 5 | Scroll down to
                                       			 the SIP
                                          				Information section: In Row 1 of
                                             				  the Destination table, enter the IP address of a CVP server.
                                             				  Accept the default destination port of 5060. In the SIP Trunk
                                                					 Security Profile drop-down list, select Non Secure SIP Trunk Profile . In the SIP Profile drop-down list, select Standard SIP Profile . Note If you are using an IPv6-enabled deployment, use the SIP Profile created in Add a SIP Profile in Unified CM . In the DTMF
                                                					 Signaling Method drop-down list, select RFC 2833 . | Note | If you are using an IPv6-enabled deployment, use the SIP Profile created in Add a SIP Profile in Unified CM . |
| Note | If you are using an IPv6-enabled deployment, use the SIP Profile created in Add a SIP Profile in Unified CM . |
| Step 6 | Click Save . |
| Step 7 | Click Reset . |
| Step 8 | Repeat for all
                                       			 the remaining Unified CVP servers in the deployment. |

| Note | If you are using an IPv6-enabled deployment, use the SIP Profile created in Add a SIP Profile in Unified CM . |
|---|---|

| Step 1 | In Unified
                                       			 Communications Manager, select Call
                                             				  Routing > Route Hunt > Route
                                             				  Group . |
|---|---|
| Step 2 | Click Add
                                          				New . |
| Step 3 | Enter a name
                                       			 for the route group; for example, CVP Route Group . |
| Step 4 | Using the Add
                                       			 to Route Group button, add all CVP Trunks as Selected Devices. |
| Step 5 | Click Save . |

| Step 1 | In Unified
                                       			 Communications Manager, select Call
                                             				  Routing > Route Hunt > Route
                                             				  List . |
|---|---|
| Step 2 | Click Add
                                          				New . |
| Step 3 | Enter a name
                                       			 for the route list; for example, CVP Route List . |
| Step 4 | Select a Cisco
                                       			 Unified Communications Manager Group. |
| Step 5 | Add the route
                                       			 group you created. |
| Step 6 | Click Save . |

| Step 1 | In Unified
                                       			 Communications Manager, select Call
                                             				  Routing > Route Hunt > Route
                                             				  Pattern . |
|---|---|
| Step 2 | Click Add
                                          				New . |
| Step 3 | Enter a route
                                       			 pattern of 8881111000XXXX . |
| Step 4 | Select the
                                       			 route list that you created. |
| Step 5 | Keep all
                                       			 defaults in all panels |
| Step 6 | Click Save . |
| Step 7 | Click OK at the message about the Forced Authorization Code. You
                                       			 do not want a Forced Authorization Code. |

| Sequence | Task |
|---|---|
| 1 | Download Report Bundles |
| 2 | Import Reports |
| 3 | Configure Unified Intelligence Center Administration |

| Step 1 | Sign in to Unified Intelligence Center with your Cisco Intelligence Center administrator account (https://<hostname/ IP address
                                          of CUIC Publisher>:8444/cuicui). |
|---|---|
| Step 2 | Select Configure > Data Sources . |
| Step 3 | Click Data
                                             				Sources in the left panel. |
| Step 4 | Select the UCCE Historical data source. Click Edit . In the Datasource Host field, enter the IP Address of the external HDS server. In the Port field, enter the AW SQL server port number. The default is 1433 . In the Database Name field, enter {instance}_awdb . Leave the Instance field blank. Select the Timezone . In the Database User ID , enter the user name that you configured for the Cisco Unified Intelligence Center SQL Server user account. Enter and confirm the SQL Server User password . Select the Charset based on the collation of SQL Server installation. Click Test Connection . Click Save . |
| Step 5 | Click the Secondary tab to configure Unified CCE Historical
                                          			 Data Source. Check the Failover
                                                   					 Enabled checkbox. In the Datasource Host field, enter the IP address of the second external HDS server. In the Port field, enter 1433 . In the Database Name field, enter {instance}_awdb . Complete
                                                				  other fields as in the Primary tab. Click Test
                                                   					 Connection . Click Save . |
| Step 6 | Repeat this procedure for the UCCE Realtime datasource for 4000 or 12000 Agents deployment . The Database Name for the Realtime Data Source is {instance}_awdb . |

| Note | Each report template help folder has a size limit of 3 MB. If the folder size exceeds this limit, the system does not load
                                                         the help content. You cannot import Report Filters and Collections. You cannot use the same names for the custom Value List, Report, or Report Definition that exist in the stock report templates.
                                                         If the same names are used, it leads to the stock report template import failure. |
|---|---|

| Step 1 | In the left navigation pane, choose Reports . |
|---|---|
| Step 2 | In the Reports listing page, click Import . |
| Step 3 | Click Browse to select the file (.xml or .zip format) to be imported. Note The maximum file size for the .zip file format is 60 MB and for .xml file format is 3 MB. | Note | The maximum file size for the .zip file format is 60 MB and for .xml file format is 3 MB. |
| Note | The maximum file size for the .zip file format is 60 MB and for .xml file format is 3 MB. |
| Step 4 | Select the required file and click Open . |
| Step 5 | Select the file location from the Save to Folder list to save the file. |
| Step 6 | Click Upload . Once the file is successfully uploaded, the table gets populated with the corresponding report template, current available
                                          version, and incoming version of the files being imported. |
| Step 7 | Select a Data Source for the Report Definition only if the Report Definition for the report being imported is not defined
                                          in the Unified Intelligence Center. |
| Step 8 | Select a Data Source for the Value List that is defined in the Report Definition. Note Selection of a Data Source for the Value List is mandatory: If the Value List does not use the same Data Source as the Report Definition. For Real Time Streaming Report Definitions. | Note | Selection of a Data Source for the Value List is mandatory: If the Value List does not use the same Data Source as the Report Definition. For Real Time Streaming Report Definitions. |
| Note | Selection of a Data Source for the Value List is mandatory: If the Value List does not use the same Data Source as the Report Definition. For Real Time Streaming Report Definitions. |
| Step 9 | Select the files to import or overwrite. Overwrite—If the report being imported exists in the Unified Intelligence Center. Import—If the report being imported is the new set of report files. |
| Step 10 | Click Import . Note If the system does not have report definitions, new report definitions are created in Report Definitions > Imported Report Definitions folder. Importing a report to a different version of Unified Intelligence Center is not supported. However, when you upgrade Unified
                                                               Intelligence Center, report templates continue to work in the upgraded version. Importing manually edited XMLs is not supported. | Note | If the system does not have report definitions, new report definitions are created in Report Definitions > Imported Report Definitions folder. Importing a report to a different version of Unified Intelligence Center is not supported. However, when you upgrade Unified
                                                               Intelligence Center, report templates continue to work in the upgraded version. Importing manually edited XMLs is not supported. |
| Note | If the system does not have report definitions, new report definitions are created in Report Definitions > Imported Report Definitions folder. Importing a report to a different version of Unified Intelligence Center is not supported. However, when you upgrade Unified
                                                               Intelligence Center, report templates continue to work in the upgraded version. Importing manually edited XMLs is not supported. |

| Note | The maximum file size for the .zip file format is 60 MB and for .xml file format is 3 MB. |
|---|---|

| Note | Selection of a Data Source for the Value List is mandatory: If the Value List does not use the same Data Source as the Report Definition. For Real Time Streaming Report Definitions. |
|---|---|

| Note | If the system does not have report definitions, new report definitions are created in Report Definitions > Imported Report Definitions folder. Importing a report to a different version of Unified Intelligence Center is not supported. However, when you upgrade Unified
                                                               Intelligence Center, report templates continue to work in the upgraded version. Importing manually edited XMLs is not supported. |
|---|---|

| Step 1 | Sign in to the Cisco Unified Intelligence Center Administration Console ( https:// <hostname> :8443/oamp ) . |
|---|---|
| Step 2 | Configure the Active Directory card under Cluster Configuration . Enter the Host Address for the Primary Active Directory Server. Leave the default value for Port. Complete the Manager Distinguished Name fields. Enter and confirm the password with which the Manager accesses the domain controller. For User Search Base, specify the Distinguished Name or Organization Unit of the domain you want to search . For Attribute for User ID, select the required option. Note If the Windows domain name and the NETBIOS names are different, do the following: in the Cisco Unified Intelligence Center Administration
                                                                  										Console , under Active Directory Settings , in the
                                                               									field Attribute for User ID , ensure to select sAMAccountName , and add the NETBIOS value to
                                                               									set it as default value. Add at least one domain for the UserName Identifier. Do not type the @ sign before the domain name. Set a domain as the default. Click Test Connection . Click Save . Note For more details, see the online help. | Note | If the Windows domain name and the NETBIOS names are different, do the following: in the Cisco Unified Intelligence Center Administration
                                                                  										Console , under Active Directory Settings , in the
                                                               									field Attribute for User ID , ensure to select sAMAccountName , and add the NETBIOS value to
                                                               									set it as default value. | Note | For more details, see the online help. |
| Note | If the Windows domain name and the NETBIOS names are different, do the following: in the Cisco Unified Intelligence Center Administration
                                                                  										Console , under Active Directory Settings , in the
                                                               									field Attribute for User ID , ensure to select sAMAccountName , and add the NETBIOS value to
                                                               									set it as default value. |
| Note | For more details, see the online help. |
| Step 3 | Configure syslog
                                          			 for all devices. Choose Logs and Traces . For each
                                                				  host address: Select the associated
                                                         						servers and click the arrow to expand. Select the server name. In the Syslog Settings pane, configure the Primary and Backup Host. Click Save . |
| Step 4 | Configure SNMP
                                          			 for all devices, if used. Select Tools > Network SNMP . Navigate to
                                                				  SNMP and for each server add the following: V1/V2c Community Strings. Notification Destination. |

| Note | If the Windows domain name and the NETBIOS names are different, do the following: in the Cisco Unified Intelligence Center Administration
                                                                  										Console , under Active Directory Settings , in the
                                                               									field Attribute for User ID , ensure to select sAMAccountName , and add the NETBIOS value to
                                                               									set it as default value. |
|---|---|

| Note | For more details, see the online help. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Configure Contact Center Agents and Routing for Live Data Reports |
| 2 | Live Data Reports |
| 3 | Securing connection between CTI Server and Finesse |

| Note | Routing scripts are configured in Script Editor, which you can open from Unified CCE Administration Tools. |
|---|---|

| Procedure | When to
                                             						use |
|---|---|
| Add Live
                                             						Data reports to default desktop layout | Use this
                                             						procedure if you want to add Live Data reports to the Finesse desktop after a
                                             						fresh installation or after an upgrade if you have not customized the default
                                             						desktop layout. |
| Add Live
                                             						Data reports to custom desktop layout | Use this
                                             						procedure if you have customized the Finesse desktop layout. |
| Add Live
                                             						Data reports to team layout | Use this
                                             						procedure if you want to add Live Data reports to the desktop layout for
                                             						specific teams only. |

| Step 1 | In Unified CCE Administration , navigate to Desktop > Resources . |
|---|---|
| Step 2 | Click the Desktop Layout tab. |
| Step 3 | Remove the
                                             			 comment characters (<!-- and -->) from each report that you want to add
                                             			 to the desktop layout. Make sure you choose the reports that match the method
                                             			 your agents use to access the Finesse desktop (HTTP or HTTPS). |
| Step 4 | Replace
                                             			 my-cuic-server with the fully qualified domain name of your Cisco Unified
                                             			 Intelligence Center Server. |
| Step 5 | Optionally, change the gadget height. Example: The height specified in the Live Data gadget URLs is 310 pixels. If you want to change the height, change the gadgetHeight
                                                parameter in the URL to the desired value. For example, if you want the gadget height to be 400 pixels, change the code as
                                                follows, replacing 310 with 400: <gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp?
        gadgetHeight=400&viewId_1=99E6C8E210000141000000D80A0006C4&
        filterId_1=agent.id=CL%20teamName&viewId_2=9AB7848B10000141000001C50A0006C4&
        filterId_2=agent.id=CL%20teamName
        </gadget> To maintain the optimal display of the gadget with scroll bars, set the value for the gadget height to a minimum of 200 pixels.
                                                If the report does not require scroll bars, for example a one-row report, you can set a smaller gadget height (for example,
                                                100 pixels). If you do not specify anything for the gadget height (if you remove the 310 from the URL), it defaults to 170
                                                pixels. |
| Step 6 | Click Save . |

| Step 1 | In Unified CCE Administration , navigate to Desktop > Resources . |
|---|---|
| Step 2 | Click the Desktop Layout tab. |
| Step 3 | Click Finesse Default Layout XML to show the default
                                             			 layout XML. |
| Step 4 | Copy the XML code for the report you want to add from the Finesse
                                             			 default layout XML. Example: To add the Agent Report for HTTPS, copy the following: <gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp?
        gadgetHeight=310&viewId_1=99E6C8E210000141000000D80A0006C4&
        filterId_1=agent.id=CL%20teamName&
        viewId_2=9AB7848B10000141000001C50A0006C4&
        filterId_2=agent.id=CL%20teamName
</gadget> |
| Step 5 | Paste the XML within the tab tags where you want it to appear. Example: To add the report to the home tab of the agent desktop: <layout>
  <role>Agent</role>
  <page>
    <gadget>/desktop/gadgets/CallControl.jsp</gadget>
  </page>
  <tabs>
    <tab>
      <id>home</id>
      <label>finesse.container.tabs.agent.homeLabel</label>
      <gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp?
              gadgetHeight=310&viewId_1=99E6C8E210000141000000D80A0006C4&
              filterId_1=agent.id=CL%20teamName&
              viewId_2=9AB7848B10000141000001C50A0006C4&
              filterId_2=agent.id=CL%20teamName
      </gadget> 
    </tab>
    <tab>
      <id>manageCall</id>
      <label>finesse.container.tabs.agent.manageCallLabel</label>
    </tab>
  </tabs>
</layout> |
| Step 6 | Replace
                                             			 my-cuic-server with the fully qualified domain name of your Cisco Unified
                                             			 Intelligence Center Server. |
| Step 7 | Optionally, change the gadget height. Example: The height specified in the Live Data gadget URLs is 310 pixels. If you want to change the height, change the gadgetHeight
                                                parameter in the URL to the desired value. For example, if you want the gadget height to be 400 pixels, change the code as
                                                follows: <gadget>https://my-cuic-server:8444/cuic/gadget/LiveData/LiveDataGadget.jsp?
        gadgetHeight=400&viewId_1=99E6C8E210000141000000D80A0006C4&
        filterId_1=agent.id=CL%20teamName&viewId_2=9AB7848B10000141000001C50A0006C4&
        filterId_2=agent.id=CL%20teamName
        </gadget> To maintain the optimal display of the gadget with scroll bars, set the value for the gadget height to a minimum of 200 pixels.
                                                If the report does not require scroll bars, for example a one-row report, you can set a smaller gadget height (for example,
                                                100 pixels). If you do not specify anything for the gadget height (if you remove the 310 from the URL), it defaults to 170
                                                pixels. |
| Step 8 | Click Save . Note After you
                                                            				  add a gadget, sign in to the Finesse desktop and make sure it appears the way
                                                            				  you want. If you use a report with a large number of rows, you may want to
                                                            				  adjust the gadget height or the screen resolution on the computer used to
                                                            				  access the desktop to make the report easier to read or make more rows appear
                                                            				  on the screen without needing to scroll down. Agents who
                                                            				  are signed in when you change the desktop layout must sign out and sign back in
                                                            				  to see the change on their desktops. | Note | After you
                                                            				  add a gadget, sign in to the Finesse desktop and make sure it appears the way
                                                            				  you want. If you use a report with a large number of rows, you may want to
                                                            				  adjust the gadget height or the screen resolution on the computer used to
                                                            				  access the desktop to make the report easier to read or make more rows appear
                                                            				  on the screen without needing to scroll down. Agents who
                                                            				  are signed in when you change the desktop layout must sign out and sign back in
                                                            				  to see the change on their desktops. |
| Note | After you
                                                            				  add a gadget, sign in to the Finesse desktop and make sure it appears the way
                                                            				  you want. If you use a report with a large number of rows, you may want to
                                                            				  adjust the gadget height or the screen resolution on the computer used to
                                                            				  access the desktop to make the report easier to read or make more rows appear
                                                            				  on the screen without needing to scroll down. Agents who
                                                            				  are signed in when you change the desktop layout must sign out and sign back in
                                                            				  to see the change on their desktops. |

| Note | After you
                                                            				  add a gadget, sign in to the Finesse desktop and make sure it appears the way
                                                            				  you want. If you use a report with a large number of rows, you may want to
                                                            				  adjust the gadget height or the screen resolution on the computer used to
                                                            				  access the desktop to make the report easier to read or make more rows appear
                                                            				  on the screen without needing to scroll down. Agents who
                                                            				  are signed in when you change the desktop layout must sign out and sign back in
                                                            				  to see the change on their desktops. |
|---|---|

| Note | The Unified CVP Reporting VM is required for customers who use Courtesy Callback and who want to run Unified CVP call and
                                          application reports. |
|---|---|

| Step 1 | On the Unified
                                          			 CVP Reporting Server, click Start . |
|---|---|
| Step 2 | In the search
                                          			 box, type %CVP_HOME%\CVP_Reporting_Templates and press Enter . |
| Step 3 | Compress the reports into a zip folder and copy it to the system from which you will run Unified Intelligence Center Administration. |

| Step 1 | Log in to the Unified Intelligence Center at https:// <hostname/ IP address of CUIC Publisher> :8444/cuicui . |
|---|---|
| Step 2 | Select the Data Sources drawer to open the Data Sources page. |
| Step 3 | Click New to open New Data Source page. |
| Step 4 | Complete fields
                                          			 on this page as follows: Field Value Name Enter
                                                         							 the name of this data source. Report Designers and Report Definition Designers do not have access to the Data
                                                         							 Sources page but can see the list of Data Sources when they create custom
                                                         							 reports. To benefit those users, give a new Data Source a meaningful name. Description Enter
                                                         							 a description for this data source. Data Source Type Choose Informix . Note Type is disabled in Edit mode. Host Settings Database Host Enter the IP address or hostname for the Unified CVP Reporting server. Port Enter
                                                         							 the port number. Typically, the port is 1526. You
                                                         							 may have to open this port in the CVP Reporting Server firewall (Windows
                                                         							 Firewall > Advanced Settings > Inbound rules > new rule). Database Name Enter the name of the reporting database on the Unified CVP reporting server. The database name can be cvp_data or callback . Instance Specify the instance name of the desired database. By default, this is cvp. Timezone Choose
                                                         							 the correct time zone for the data stored in the database. In locations that
                                                         							 change from Standard Time to Daylight Savings Time, this time zone is updated
                                                         							 automatically. Note Set CVP datasource timezone configuration to UTC on CUIC. Authentication Settings Database User ID Enter the user ID of the Reporting User  to access the Unified CVP reporting database. (The
                                                         							 cvp_dbuser account is created automatically during Unified CVP Reporting server
                                                         							 installation.) Password and Confirm
                                                            								Password Enter and confirm the password for the database user. Charset Choose UTF-8. Default Permissions View or edit the permissions for this datasource for My Group and for the All
                                                         							 Users group. Max Pool Size Select the maximum pool size. Value ranges from 5-200. The default Max Pool Size value is 100 and is common for both the primary and secondary data source
                                                         tabs. | Field | Value | Name | Enter
                                                         							 the name of this data source. Report Designers and Report Definition Designers do not have access to the Data
                                                         							 Sources page but can see the list of Data Sources when they create custom
                                                         							 reports. To benefit those users, give a new Data Source a meaningful name. | Description | Enter
                                                         							 a description for this data source. | Data Source Type | Choose Informix . Note Type is disabled in Edit mode. | Note | Type is disabled in Edit mode. | Host Settings | Database Host | Enter the IP address or hostname for the Unified CVP Reporting server. | Port | Enter
                                                         							 the port number. Typically, the port is 1526. You
                                                         							 may have to open this port in the CVP Reporting Server firewall (Windows
                                                         							 Firewall > Advanced Settings > Inbound rules > new rule). | Database Name | Enter the name of the reporting database on the Unified CVP reporting server. The database name can be cvp_data or callback . | Instance | Specify the instance name of the desired database. By default, this is cvp. | Timezone | Choose
                                                         							 the correct time zone for the data stored in the database. In locations that
                                                         							 change from Standard Time to Daylight Savings Time, this time zone is updated
                                                         							 automatically. Note Set CVP datasource timezone configuration to UTC on CUIC. | Note | Set CVP datasource timezone configuration to UTC on CUIC. | Authentication Settings | Database User ID | Enter the user ID of the Reporting User  to access the Unified CVP reporting database. (The
                                                         							 cvp_dbuser account is created automatically during Unified CVP Reporting server
                                                         							 installation.) | Password and Confirm
                                                            								Password | Enter and confirm the password for the database user. | Charset | Choose UTF-8. | Default Permissions | View or edit the permissions for this datasource for My Group and for the All
                                                         							 Users group. | Max Pool Size | Select the maximum pool size. Value ranges from 5-200. The default Max Pool Size value is 100 and is common for both the primary and secondary data source
                                                         tabs. |
| Field | Value |
| Name | Enter
                                                         							 the name of this data source. Report Designers and Report Definition Designers do not have access to the Data
                                                         							 Sources page but can see the list of Data Sources when they create custom
                                                         							 reports. To benefit those users, give a new Data Source a meaningful name. |
| Description | Enter
                                                         							 a description for this data source. |
| Data Source Type | Choose Informix . Note Type is disabled in Edit mode. | Note | Type is disabled in Edit mode. |
| Note | Type is disabled in Edit mode. |
| Host Settings |
| Database Host | Enter the IP address or hostname for the Unified CVP Reporting server. |
| Port | Enter
                                                         							 the port number. Typically, the port is 1526. You
                                                         							 may have to open this port in the CVP Reporting Server firewall (Windows
                                                         							 Firewall > Advanced Settings > Inbound rules > new rule). |
| Database Name | Enter the name of the reporting database on the Unified CVP reporting server. The database name can be cvp_data or callback . |
| Instance | Specify the instance name of the desired database. By default, this is cvp. |
| Timezone | Choose
                                                         							 the correct time zone for the data stored in the database. In locations that
                                                         							 change from Standard Time to Daylight Savings Time, this time zone is updated
                                                         							 automatically. Note Set CVP datasource timezone configuration to UTC on CUIC. | Note | Set CVP datasource timezone configuration to UTC on CUIC. |
| Note | Set CVP datasource timezone configuration to UTC on CUIC. |
| Authentication Settings |
| Database User ID | Enter the user ID of the Reporting User  to access the Unified CVP reporting database. (The
                                                         							 cvp_dbuser account is created automatically during Unified CVP Reporting server
                                                         							 installation.) |
| Password and Confirm
                                                            								Password | Enter and confirm the password for the database user. |
| Charset | Choose UTF-8. |
| Default Permissions | View or edit the permissions for this datasource for My Group and for the All
                                                         							 Users group. |
| Max Pool Size | Select the maximum pool size. Value ranges from 5-200. The default Max Pool Size value is 100 and is common for both the primary and secondary data source
                                                         tabs. |
| Step 5 | Click Test
                                             				Connection . If the status
                                             				is not Online, review the error message to determine the cause and edit the
                                             				data source accordingly. |
| Step 6 | Click Save to close the Add Data Source window. The new data
                                             				source appears on the Data Sources list. |

| Field | Value |
|---|---|
| Name | Enter
                                                         							 the name of this data source. Report Designers and Report Definition Designers do not have access to the Data
                                                         							 Sources page but can see the list of Data Sources when they create custom
                                                         							 reports. To benefit those users, give a new Data Source a meaningful name. |
| Description | Enter
                                                         							 a description for this data source. |
| Data Source Type | Choose Informix . Note Type is disabled in Edit mode. | Note | Type is disabled in Edit mode. |
| Note | Type is disabled in Edit mode. |
| Host Settings |
| Database Host | Enter the IP address or hostname for the Unified CVP Reporting server. |
| Port | Enter
                                                         							 the port number. Typically, the port is 1526. You
                                                         							 may have to open this port in the CVP Reporting Server firewall (Windows
                                                         							 Firewall > Advanced Settings > Inbound rules > new rule). |
| Database Name | Enter the name of the reporting database on the Unified CVP reporting server. The database name can be cvp_data or callback . |
| Instance | Specify the instance name of the desired database. By default, this is cvp. |
| Timezone | Choose
                                                         							 the correct time zone for the data stored in the database. In locations that
                                                         							 change from Standard Time to Daylight Savings Time, this time zone is updated
                                                         							 automatically. Note Set CVP datasource timezone configuration to UTC on CUIC. | Note | Set CVP datasource timezone configuration to UTC on CUIC. |
| Note | Set CVP datasource timezone configuration to UTC on CUIC. |
| Authentication Settings |
| Database User ID | Enter the user ID of the Reporting User  to access the Unified CVP reporting database. (The
                                                         							 cvp_dbuser account is created automatically during Unified CVP Reporting server
                                                         							 installation.) |
| Password and Confirm
                                                            								Password | Enter and confirm the password for the database user. |
| Charset | Choose UTF-8. |
| Default Permissions | View or edit the permissions for this datasource for My Group and for the All
                                                         							 Users group. |
| Max Pool Size | Select the maximum pool size. Value ranges from 5-200. The default Max Pool Size value is 100 and is common for both the primary and secondary data source
                                                         tabs. |

| Note | Type is disabled in Edit mode. |
|---|---|

| Note | Set CVP datasource timezone configuration to UTC on CUIC. |
|---|---|

| Step 1 | Launch the Unified Intelligence Center web application at https://<Hostname/IP Address of CUIC Publisher>:8444/cuic |
|---|---|
| Step 2 | From the left navigation pane, click Reports . |
| Step 3 | On the Reports toolbar, click New > Import . You will be redirected to the legacy interface. |
| Step 4 | Navigate to the folder where you want to import the report. Note If you are importing a stock report bundle from Cisco.com, it must be placed at the Reports folder level. | Note | If you are importing a stock report bundle from Cisco.com, it must be placed at the Reports folder level. |
| Note | If you are importing a stock report bundle from Cisco.com, it must be placed at the Reports folder level. |
| Step 5 | Click Import Report . |
| Step 6 | In the File Name (XML or ZIP file) field, click Choose File . |
| Step 7 | Browse to and select the XML or the compressed report file, and click Open . |
| Step 8 | From the Data source for ReportDefinition drop-down list, select a data source used by the report definition. Note This field appears only if the Report Definition for the report being imported is not currently defined in Unified Intelligence
                                                         Center. | Note | This field appears only if the Report Definition for the report being imported is not currently defined in Unified Intelligence
                                                         Center. |
| Note | This field appears only if the Report Definition for the report being imported is not currently defined in Unified Intelligence
                                                         Center. |
| Step 9 | From the Data Source for ValueList drop-down list, select the data source used by the value lists defined in the report definition. Note You have to select a data source for the value list only if it does not use the same data source as the Report Definition.
                                                         For Report Definitions of Real Time Streaming, it is mandatory to select a data source for the Value Lists. | Note | You have to select a data source for the value list only if it does not use the same data source as the Report Definition.
                                                         For Report Definitions of Real Time Streaming, it is mandatory to select a data source for the Value Lists. |
| Note | You have to select a data source for the value list only if it does not use the same data source as the Report Definition.
                                                         For Report Definitions of Real Time Streaming, it is mandatory to select a data source for the Value Lists. |
| Step 10 | In the Save To field, browse to the folder where you want to place the imported report. Use the arrow keys to expand the folders. |
| Step 11 | Click Import . |

| Note | If you are importing a stock report bundle from Cisco.com, it must be placed at the Reports folder level. |
|---|---|

| Note | This field appears only if the Report Definition for the report being imported is not currently defined in Unified Intelligence
                                                         Center. |
|---|---|

| Note | You have to select a data source for the value list only if it does not use the same data source as the Report Definition.
                                                         For Report Definitions of Real Time Streaming, it is mandatory to select a data source for the Value Lists. |
|---|---|

| Note | Importing a report to a different version of Unified Intelligence Center is not supported. However, when you upgrade Unified
                                          Intelligence Center, report templates continue to work in the upgraded version. |
|---|---|

| Note | If you have configured VXML Gateway, it is not mandatory to configure Virtualized Voice Browser (VVB). You may configure either
                                             VVB or VXML Gateway, or configure both. The Cisco VVB configurations are site specific. All the VVBs in a site must have the same configurations. |
|---|---|

| Task |
|---|
| Common Configuration for the Ingress Gateway and VXML Gateway |
| Configure Ingress Gateway |
| Confiugre VXML Gateway (optional) |
| Configure Codec for Ingress and VXML Gateways |

| Note | Complete all configuration steps in enable > configuration terminal mode. |
|---|---|

| Step 1 | Configure
                                          			 global settings. voice service voip
	 allow-connections sip to sip
	signaling forward unconditional
	# If this gateway is being licensed as a Cisco UBE the following lines are also required
 mode border-element
 ip address trusted list
  ipv4 0.0.0.0 0.0.0.0               # Or an explicit Source IP Address Trust List
sip
		rel1xx disable
		header-passing
		options-ping 60
  midcall-signaling passthru |
|---|---|
| Step 2 | Configure
                                          			 voice codec preference: voice class codec 1
     codec preference 1 g711ulaw
     codec preference 2 g711alaw
     codec preference 3 g729r8 |
| Step 3 | Configure
                                          			 default services: To download and transfer the survivability.tcl file to the Ingress Gateway, see File Transfer to Gateway . #Default Services
application
     service survivability flash:survivability.tcl |
| Step 4 | Configure
                                          			 gateway and sip-ua timers: gateway
	media-inactivity-criteria all
	timer receive-rtp 1200

sip-ua
	retry invite 2
	retry bye 1
	timers expires 60000
	timers connect 1000
	reason-header override |
| Step 5 | Configure
                                          			 POTS dial-peers: # Configure Unified CVP survivability
dial-peer voice 1 pots
     description CVP TDM dial-peer
     service survivability
     incoming called-number .T
     direct-inward-dial Note This is required for TDM gateways only. | Note | This is required for TDM gateways only. |
| Note | This is required for TDM gateways only. |
| Step 6 | Configure the
                                          			 switch leg: #Configure the Switch leg where
# preference is used to distinguish between sides.
# max-conn is used prevent overloading of Unifed CVP
# options-keepalive is used to handle failover
# Note: the example below is for gateways located on the A-side of a geographically
#distributed deployment
# Note: Ensure that you configure switch dial-peers for each Unified CVP server.

dial-peer voice 70021 voip
     description Used for Switch leg SIP Direct
     preference 1
     max-conn 225
     destination-pattern xxxx...... #Customer specific destination pattern
     session protocol sipv2
     session target ipv4:###.###.###.###     #IP Address for Unified CVP, SideA
     session transport tcp
     voice-class codec 1
     voice-class sip options-keepalive up-interval 12 down-interval 65 retry 2
     dtmf-relay rtp-nte
     no vad

dial-peer voice 70022 voip
     description Used for Switch leg SIP Direct
     preference 2
     max-conn 225
     destination-pattern xxxx...... #Customer specific destination pattern
     session protocol sipv2
     session target ipv4:###.###.###.###    #IP Address for Unified CVP, SideB
     session transport tcp
     voice-class codec 1
     voice-class sip options-keepalive up-interval 12 down-interval 65 retry 2
     dtmf-relay rtp-nte
     no vad |
| Step 7 | Configure the
                                          			 hardware resources (transcoder, conference bridge, and MTP): Note This
                                                         				  configuration section is unnecessary for virtual CUBE or CSR 1000v Gateways.
                                                         				  They do not have physical DSP resources. #For gateways with physical DSP resources, configure Hardware resources using 
#Unified Communications Domain Manager. # Configure the voice-cards share the DSP resources located in Slot0
voice-card 0
     dspfarm
     dsp services dspfarm
voice-card 1
     dspfarm
     dsp services dspfarm
voice-card 2
     dspfarm
     dsp services dspfarm
voice-card 3
     dspfarm
     dsp services dspfarm
voice-card 4
     dspfarm	
     dsp services dspfarm

# Point to the contact center call manager
sccp local GigabitEthernet0/0
     sccp ccm ###.###.###.### identifier 1 priority 1 version 7.0 # Cisco Unified CM sub 1
     sccp ccm ###.###.###.### identifier 2 priority 2 version 7.0 # Cisco Unifed CM sub 2

# Add a SCCP group for each of the hardware resource types
sccp ccm group 1
     associate ccm 1 priority 1
     associate profile 2 register < gatewayname mtp>
     associate profile 1 register < gatewayname conf>
     associate profile 3 register < gatewayname xcode>

# Configure DSPFarms for Conference, MTP and Transcoder

dspfarm profile 1 conference
     codec g711ulaw
     codec g711alaw
     codec g729r8
     maximum sessions 24
     associate application SCCP

dspfarm profile 2 mtp
     codec g711ulaw
     codec g711alaw
     codec g729r8
     maximum sessions software 500
     associate application SCCP

dspfarm profile 3 transcode universal
     codec g711ulaw
     codec g711alaw
     codec g729r8
     maximum sessions 52
     associate application SCCP | Note | This
                                                         				  configuration section is unnecessary for virtual CUBE or CSR 1000v Gateways.
                                                         				  They do not have physical DSP resources. |
| Note | This
                                                         				  configuration section is unnecessary for virtual CUBE or CSR 1000v Gateways.
                                                         				  They do not have physical DSP resources. |
| Step 8 | Optional,
                                          			 configure the SIP Trunking: # Configure the resources to be monitored
voice class resource-group 1
     resource cpu 1-min-avg threshold high 80 low 60
     resource ds0
     resource dsp
     resource mem total-mem
     periodic-report interval 30

# Configure one rai target for each CVP Server
sip-ua
     rai target ipv4:###.###.###.### resource-group1 # CVPA
     rai target ipv4:###.###.###.### resource-group1 # CVPB
     permit hostname dns:%Requires manual replacement - ServerGroup Name defined in CVP.System.SIP Server Groups% |
| Step 9 | Configure
                                          			 incoming PSTN SIP trunk dial peer: dial-peer voice 70000 voip
     description Incoming Call From PSTN SIP Trunk
     service survivability 
     incoming called-number xxxx……    # Customer specific incoming called-number pattern
     voice-class sip rel1xx disable
     dtmf-relay rtp-nte 
     session protocol sipv2
     voice-class codec 1
     no vad Note This is required for CUBE only. | Note | This is required for CUBE only. |
| Note | This is required for CUBE only. |

| Note | This is required for TDM gateways only. |
|---|---|

| Note | This
                                                         				  configuration section is unnecessary for virtual CUBE or CSR 1000v Gateways.
                                                         				  They do not have physical DSP resources. |
|---|---|

| Note | This is required for CUBE only. |
|---|---|

| Step 1 | Download the required .tcl files from %CVP_HOME%\GWDownloads folder. |
|---|---|
| Step 2 | Transfer the .tcl files to the flash memory of the Gateway using FTP. |

| Step 1 | Add the voice
                                          			 class codec 1 to set the codec preference in dial-peer: Example: voice class codec 1
     codec preference 1 g729r8
     codec preference 2 g711alaw
     codec preference 3 g711ulaw dial-peer voice 70021 voip
     description Used for Switch leg SIP Direct
     preference 1
     max-conn 225 
     destination-pattern xxxx...... # Customer specific destination
     session protocol sipv2
     session target ipv4:###.###.###.### # IP Address for Unified CVP
     session transport tcp
     voice class codec 1
     voice-class sip options-keepalive up-interval 12 down-interval 65 retry 2
     dtmf-relay rtp-nte
     no vad |
|---|---|
| Step 2 | Modify the
                                          			 dial-peer to specify the codec explicitly for a dial-peer: dial-peer voice 9 voip 
     description For Outbound Call for Customer
     destination-pattern <Customer Phone Number Pattern>
     session protocol sipv2
     session target ipv4:<Customer SIP Cloud IP Address>
     session transport tcp
     voice-class sip rel1xx supported "100rel"
     voice-class sip options-keepalive up-interval 12 down-interval 65 retry 2
     dtmf-relay rtp-nte
     codec g711alaw
     no vad

dial-peer voice 10 voip 
     description ***To CUCM Agent Extension For Outbound***
     destination-pattern <Agent Extension Pattern to CUCM>
     session protocol sipv2
     session target ipv4:<CUCM IP Address>
     voice-class sip rel1xx supported "100rel"
     dtmf-relay rtp-nte
     codec g711alaw |

| Modify the
                                          			 following dial-peer to specify the codec explicitly for a dial-peer: dial-peer voice 919191 voip
     description Unified CVP SIP ringtone dial-peer
     service ringtone
     incoming called-number 9191T
     voice-class sip rel1xx disable
     dtmf-relay rtp-nte
     codec g711alaw
     no vad

dial-peer voice 929292 voip
     description CVP SIP error dial-peer
     service cvperror
     incoming called-number 9292T
     voice-class sip rel1xx disable
     dtmf-relay rtp-nte
     codec g711alaw
     no vad

dial-peer voice 7777 voip
     description Used for VRU leg #Configure VXML leg where the incoming called
     service bootstrap
     incoming called-number 7777T
     dtmf-relay rtp-nte
     codec g711alaw
     no vad |
|---|

| Task |
|---|
| Set Up IPv6 for VOS-Based Contact Center Applications |
| Configure NAT64 for IPv6-Enabled Deployment |
| Configure IPv6 on Unified CVP Call Server |
| Configure Gateways to Support IPv6 |
| Configure IPv6 on Unified Communications Manager |

| Step 1 | Sign into
                                          			 Cisco Unified Operating System Administration on the Publisher/Primary node:. Unified
                                                   					 Communications Manager and Unified Intelligence Center: https:// <host or IP address of the Publisher or Primary
                                                         						  node> /cmplatform Finesse: https:// FQDN of the Primary node :8443/cmplatform |
|---|---|
| Step 2 | Navigate to Settings > IP > Ethernet
                                                				  IPv6 . |
| Step 3 | Check
                                          			 the Enable
                                             				IPv6 check box. |
| Step 4 | Enter values
                                          			 for IPv6Address , Prefix
                                             				Length , and Default Gateway . |
| Step 5 | Check the Update with
                                             				Reboot check box. |
| Step 6 | Click Save . The
                                          			 server restarts. |
| Step 7 | Repeat this
                                          			 procedure on the subscriber/secondary node. |

| Step 1 | Access the CLI on the VOS server. |
|---|---|
| Step 2 | To enable or disable IPv6, enter: set network ipv6 service {enable \| disable} |
| Step 3 | Set the IPv6 address and prefix length: set network ipv6 static_address addr mask Example: set network ipv6 static_address 2001:db8:2::a 64 |
| Step 4 | Set the default gateway: set network ipv6 gateway addr |
| Step 5 | Restart the system for the changes to take effect. utils system restart |
| Step 6 | To display the IPv6 settings, enter: show network ipv6 settings |

| Note | NAT64 is NOT supported on M train IOS. T train is required. For more information, see the Compatibility Matrix for Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html . |
|---|---|

| Step 1 | In Windows,
                                          			 navigate to Administrative Tools > DNS . This opens the DNS
                                          			 Manager. |
|---|---|
| Step 2 | In the Forward
                                          			 lookup zone, navigate to your deployment's domain name. |
| Step 3 | Right-click
                                          			 the domain name and select New
                                             				Host (A or AAAA) . |
| Step 4 | In the New
                                          			 Host dialog box, enter the computer name and IP address of the Unified CCE AW-HDS-DDS servers and any External HDS  servers.
                                          Click Add Host . |

| Note | Optionally, DNS64
                                             		  can be used in place of static DNS entries. Use of DNS64 helps facilitate
                                             		  translation between IPv6 and IPv4 networks by synthesizing AAAA resource
                                             		  records from A resource records. |
|---|---|

| Step 1 | On the
                                       			 Unified CVP Call Server, navigate to Control
                                             				  Panel > Network and Sharing . |
|---|---|
| Step 2 | Click Ethernet . |
| Step 3 | From the Ethernet Status window, select Properties . |
| Step 4 | Check the Internet Protocol Version 6 (TCP/IPv6) check box,
                                       			 and choose Properties . |
| Step 5 | Choose Use
                                          				the following IPv6 address radio button. |
| Step 6 | Enter values
                                       			 in the IPv6
                                          				address , Subnet
                                          				prefix length , and Default gateway fields. |
| Step 7 | Click OK and restart Windows when prompted. |

| Configure the following on the Gateway: >Enable
>configure terminal
>interface type number
>ipv6 address{ ipv6-address / prefix-length \| prefix-name sub-bits / prefix-length}
>ipv6 enable |
|---|---|

| Configure the following on the Gateway: >conf t
>voice service voip
>SIP
>ANAT
>bind control source-interface GigabitEthernet0/2
>bind media source-interface GigabitEthernet0/2 |
|---|

| Configure the following on the Gateway: >conf t
>sip-ua
>protocol mode dual-stack preference ipv6 |
|---|

| Step 1 | From Cisco
                                             				Unified CM Administration , choose System > Enterprise Parameters > IPv6 Configuration Modes to configure
                                          			 the cluster-wide IPv6 settings for each Unified Communications Manager server. |
|---|---|
| Step 2 | From the Enable
                                             				IPv6 drop-down list, choose True . |
| Step 3 | From the IP
                                             				Addressing Mode Preference for Media drop-down list, choose IPv6 . |
| Step 4 | From the IP
                                             				Addressing Mode Preference for Signaling drop-down list, choose IPv6 . |
| Step 5 | From the Allow
                                             				Auto-configuration for Phones drop-down list, choose Off . |
| Step 6 | Save your
                                          			 changes. |

| Step 1 | From Cisco
                                             				Unified CM Administration , choose Device > Device Settings > Common Device Configuration . |
|---|---|
| Step 2 | Click Add
                                             				New and enter the name of the new common device configuration
                                          			 profile. |
| Step 3 | From the IP
                                             				Addressing Mode drop-down list: To add an IPv6 common device configuration profile in Unified Communications Manager, choose IPv6
                                                				only . To add an IPv4 common device configuration profile in Unified Communications Manager, choose IPv4 only . To add a dual stack common device configuration profile in Unified Communications Manager, choose IPv4 and IPv6 . Then choose IPv4 from the IP Addressing Mode Preference for Signaling drop-down list. |
| Step 4 | Save your
                                          			 changes. |

| Step 1 | From Cisco
                                             				Unified CM Administration , choose Device > Trunk . |
|---|---|
| Step 2 | Click Find . Choose
                                          			 the trunk profile that you want to view. |
| Step 3 | From the Common
                                             				Device Configuration drop-down list: To associate the IPv6 common device configuration profile with the Gateway trunk, choose the IPv6 common device configuration
                                             profile. To
                                             						associate the IPv4 common device configuration profile with the Gateway trunk,
                                             						choose the IPv4 common device configuration profile. Note Unified
                                                         						CM gateway trunk supports only an IPv4 or IPv6 trunk. You cannot associate a
                                                         						dual stack common device configuration profile to a Unified CM gateway trunk. | Note | Unified
                                                         						CM gateway trunk supports only an IPv4 or IPv6 trunk. You cannot associate a
                                                         						dual stack common device configuration profile to a Unified CM gateway trunk. |
| Note | Unified
                                                         						CM gateway trunk supports only an IPv4 or IPv6 trunk. You cannot associate a
                                                         						dual stack common device configuration profile to a Unified CM gateway trunk. |
| Step 4 | Enter the IPv6
                                          			 address in the Destination Address IPv6 field. Note Unified CM
                                                         				  to Gateway trunk supports only standard SIP Profile and does not support ANAT
                                                         				  enabled dual-stack SIP trunk. | Note | Unified CM
                                                         				  to Gateway trunk supports only standard SIP Profile and does not support ANAT
                                                         				  enabled dual-stack SIP trunk. |
| Note | Unified CM
                                                         				  to Gateway trunk supports only standard SIP Profile and does not support ANAT
                                                         				  enabled dual-stack SIP trunk. |
| Step 5 | Save your
                                          			 changes. |

| Note | Unified
                                                         						CM gateway trunk supports only an IPv4 or IPv6 trunk. You cannot associate a
                                                         						dual stack common device configuration profile to a Unified CM gateway trunk. |
|---|---|

| Note | Unified CM
                                                         				  to Gateway trunk supports only standard SIP Profile and does not support ANAT
                                                         				  enabled dual-stack SIP trunk. |
|---|---|

| Step 1 | From Cisco
                                             				Unified CM Administration , choose Device > Phone . |
|---|---|
| Step 2 | Click Find . Choose
                                          			 the trunk profile that you want to view. |
| Step 3 | From the Common
                                             				Device Configuration drop-down list: choose the IPv6 common device
                                          			 configuration profile. To associate the IPv6 common device configuration profile to an IPv6 phone, choose the IPv6 common device configuration profile. To associate the IPv4 common device configuration profile to an IPv4 phone, choose the IPv4 common device configuration profle. |
| Step 4 | Save your
                                          			 changes. |

| Step 1 | From Cisco
                                             				Unified CM Administration , choose Device > Trunk . |
|---|---|
| Step 2 | Click Find . Choose the trunk profile that you want to
                                          			 view. |
| Step 3 | From the SIP
                                             				Profile drop-down list, choose the SIP Profile you created. Note For more information on how to create a SIP Profile, see Add a SIP Profile in Unified CM section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide
                                                         at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . | Note | For more information on how to create a SIP Profile, see Add a SIP Profile in Unified CM section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide
                                                         at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
| Note | For more information on how to create a SIP Profile, see Add a SIP Profile in Unified CM section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide
                                                         at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
| Step 4 | Save your
                                          			 change. |

| Note | For more information on how to create a SIP Profile, see Add a SIP Profile in Unified CM section in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide
                                                         at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html . |
|---|---|

| Step 1 | From Cisco
                                             				Unified CM Administration , choose Device > Trunk . |
|---|---|
| Step 2 | Click Find . Choose the trunk profile that you want to
                                          			 view. |
| Step 3 | From the Common
                                             				Device Configuration drop-down list, choose the Dual Stack Common
                                          			 Device Configuration Profile. Note For more
                                                         				  information on how to add a Dual Stack Common Device Configuration Profile, see Add a Common Device Configuration Profile in Unified Communications Manager . | Note | For more
                                                         				  information on how to add a Dual Stack Common Device Configuration Profile, see Add a Common Device Configuration Profile in Unified Communications Manager . |
| Note | For more
                                                         				  information on how to add a Dual Stack Common Device Configuration Profile, see Add a Common Device Configuration Profile in Unified Communications Manager . |
| Step 4 | Save your
                                          			 change. |

| Note | For more
                                                         				  information on how to add a Dual Stack Common Device Configuration Profile, see Add a Common Device Configuration Profile in Unified Communications Manager . |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Generate CSR and upload CA Certificates Or Generate and import Self-signed Certificates |
| 2 | Configure CCE Component |
| 3 | Configure Cisco Unified Customer Voice Portal |
| 4 | If Media Server is external, Configure Media Server |
| 5 | Configure Cisco Unified Communications Manager |
| 6 | Configure Cisco Unified Intelligence Center |
| 7 | Configure Cisco Finesse |
| 8 | Configure Live Data |
| 9 | Configure Cisco Identity Service |
| 10 | Configure Cisco Unified Customer Voice Portal Reporting Server (optional) |
| 11 | Configure VVB (optional) |
| 12 | Configure Cisco IOS Enterprise Voice Gateway |
| 13 | Configure IPv6 |
| 14 | Configure Enterprise Chat and Email (ECE) (optional) Email and Chat |

| Sequence | Task |
|---|---|
| 1 | Configure SQL Server for CCE Components |
| 2 | Set up Organizational Units |
| 3 | Configure Rogger |
| 4 | Configure AW-HDS-DDS |
| 5 | Start Unified CCE Services |
| 6 | If you have PG VMs installed, Add Unified CCE Instance on all PG VMs |
| 7 | Configure Packaged CCE Deployment Type |
| 8 | Configure Cisco Unified Contact Center Enterprise PG |
| 9 | For configuration using Configuration Manager, see Packaged CCE 4000 and 12000 Agent Supported Tools |

| Sequence | Task |
|---|---|
| 1 | Add Unified CCE Instance |
| 2 | Create Logger Database |
| 3 | To use Outbound Option, see Create Outbound Option Database |
| 4 | Add Logger Component to Instance |
| 5 | Add Router Component to Instance |
| 6 | Cisco SNMP Setup (optional) |

| Step 1 | From Unified CCE Tools, open the ICMDBA tool, and click Yes at any warnings that display. |
|---|---|
| Step 2 | Navigate to Server > Instances . |
| Step 3 | Right-click
                                                			 the instance name and choose Create to create the logger database. |
| Step 4 | In the Select
                                                			 Component dialog box, choose the logger you are working on (Logger A or Logger
                                                			 B). Click OK . |
| Step 5 | At the prompt, "SQL Server
                                                   				is not configured properly. Do you want to configure it now?" , click Yes . |
| Step 6 | On the
                                                			 Configure page, in the SQL Server Configurations pane check Memory
                                                   				(MB) and Recovery Interval . Click OK . |
| Step 7 | On the Stop
                                                			 Server page, click Yes to stop the services. |
| Step 8 | In the Select
                                                			 Logger Type dialog box, choose Enterprise . Click OK to open the Create Database dialog box. |
| Step 9 | Create the
                                                			 Logger database and log as follows: In the DB Type field, choose the Side (A or B). In the region field, choose your region. In the Create Database dialog box, click Add to open the Add Device dialog box. Click Data . Choose the drive on which you want to create the database, for example, the E drive. For the Size field, consider whether to choose the default (which is 1.4GB, a fairly minimal size) or calculate a value appropriate for
                                                      your deployment by using the Database Size Estimator Tool. If you calculate the value, enter it here. Note You can use the Database Size Estimator Tool only after the database is created. Click OK to return to the Create Database dialog box. Click Add again. In the Add Device dialog box, click Log . Choose the drive where you created the database. In the Size field, choose the default setting or, if you have calculated an appropriate size for your deployment, enter that value. Click OK to return to the Create Database dialog box. | Note | You can use the Database Size Estimator Tool only after the database is created. |
| Note | You can use the Database Size Estimator Tool only after the database is created. |
| Step 10 | In the Create
                                                			 Database dialog box, click Create , then click Start . |
| Step 11 | When you see
                                                			 the successful creation message, click OK and then Close . |

| Note | You can use the Database Size Estimator Tool only after the database is created. |
|---|---|

| Step 1 | Open the
                                                			 ICMDBA tool and click Yes to any warnings. |
|---|---|
| Step 2 | Navigate to Servers > <Logger Server> > Instances > <Unified CCE
                                                      				  instance> > LoggerA . Right-click the instance name
                                                			 and select Database > Create . |
| Step 3 | On the Stop
                                                			 Server message, click Yes to stop the services. |
| Step 4 | In the Create
                                                			 Database dialog box, click Add to open the Add Device dialog box. |
| Step 5 | Click Data , and choose the drive on which you want to create the database, for example, the E drive. In the database size field, you
                                                can choose to retain the default value or enter a required value. |
| Step 6 | Click OK to return to the Create Database dialog box. |
| Step 7 | In the Add Device dialog box, click Log . Choose the desired drive. Retain the default value in the log size field and click OK to return to the Create Database dialog box. |
| Step 8 | In the Create
                                                			 Database dialog box, click Create , and then click Start . When you see the successful creation message,
                                                			 click OK and then click Close . For more information about configuring Outbound Options, see the Outbound Option Guide for Unified Contact Center Enterprise guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-user-guide-list.html |

| Step 1 | Open the Web
                                                			 Setup tool. |
|---|---|
| Step 2 | Choose Component Management > Loggers . Click Add , and then choose the instance. |
| Step 3 | On the
                                                			 Deployment page, select the Logger (A or B). Click Duplexed , and then click Next . |
| Step 4 | On the Central Controller Connectivity page, enter the host names for Sides A and B for the Router Private Interface and Logger Private Interface . Enter the SQL port for Side A and B in the Logger SQL Port section. Then, click Next . Note The default SQL port is 1433. If the SQL server is configured with custom port, provide the custom port. | Note | The default SQL port is 1433. If the SQL server is configured with custom port, provide the custom port. |
| Note | The default SQL port is 1433. If the SQL server is configured with custom port, provide the custom port. |
| Step 5 | Check Enable Historical/Detail Data Replication . |
| Step 6 | On the
                                                			 Additional Options page, click Display Database Purge Configuration Steps . |
| Step 7 | Click the Enable Outbound Option check box. Note If this Logger is being added for a Rogger server, where there are two IP addresses that are configured on the public Network
                                                               Interface Card (for IP-based prioritization), uncheck "Register this connection's addresses in DNS" for the private ethernet
                                                               card. In addition, ensure that there is only one A-record entry in the DNS server corresponding to the host name of the server,
                                                               which maps to the general priority IP address. This is necessary for processes like the campaign manager and replication running
                                                               as part of the Logger service, to listen on the right interface IP address for client connections. | Note | If this Logger is being added for a Rogger server, where there are two IP addresses that are configured on the public Network
                                                               Interface Card (for IP-based prioritization), uncheck "Register this connection's addresses in DNS" for the private ethernet
                                                               card. In addition, ensure that there is only one A-record entry in the DNS server corresponding to the host name of the server,
                                                               which maps to the general priority IP address. This is necessary for processes like the campaign manager and replication running
                                                               as part of the Logger service, to listen on the right interface IP address for client connections. |
| Note | If this Logger is being added for a Rogger server, where there are two IP addresses that are configured on the public Network
                                                               Interface Card (for IP-based prioritization), uncheck "Register this connection's addresses in DNS" for the private ethernet
                                                               card. In addition, ensure that there is only one A-record entry in the DNS server corresponding to the host name of the server,
                                                               which maps to the general priority IP address. This is necessary for processes like the campaign manager and replication running
                                                               as part of the Logger service, to listen on the right interface IP address for client connections. |
| Step 8 | If you enable High Availability, enter the Active Directory Account Name that the opposite side logger runs under or a security group that includes that account. For example, if you are running
                                                Websetup on the logger on Side A, enter the name of the Active Directory account (or security group) that is run on Side B
                                                logger. |
| Step 9 | Select the Syslog box to enable the Syslog event feed process (cw2kfeed.exe). Note The event feed is processed and sent to the Syslog collector only if the Syslog collector is configured. For more information
                                                            about the Syslog event feed process, see the Serviceability Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . | Note | The event feed is processed and sent to the Syslog collector only if the Syslog collector is configured. For more information
                                                            about the Syslog event feed process, see the Serviceability Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
| Note | The event feed is processed and sent to the Syslog collector only if the Syslog collector is configured. For more information
                                                            about the Syslog event feed process, see the Serviceability Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
| Step 10 | Click Next . |
| Step 11 | On the Data
                                                			 Retention page, modify the Database Retention Configuration table: For these
                                                      				  tables, set the retention period to 40 days: Application_Event Event Network_Event Route_Call_Detail Route_Call_Variable Termination_Call_Detail Termination_Call_Variable Accept the
                                                      				  default settings for all other tables. If your contact center requires access
                                                      				  to any of that data for a longer period, enter an appropriate value. |
| Step 12 | Click Next . |
| Step 13 | On the Data
                                                			 Purge page, configure purges for a day of the week and a time when there is low
                                                			 demand on the system. |
| Step 14 | Accept the
                                                			 default Automatic Purge at Percent Full . |
| Step 15 | Click Next . |
| Step 16 | Check the following check box on the Logger Security page to configure secure communication between CCE core components: Logger and Router: Enable secure connection between Logger and Router Logger and its peers: Enable secure data recovery between Logger and Logger Logger and AW-HDS-DDS: Enable secure data replication between Logger and AW-HDS-DDS and Enable secure-only connection Campaign Manager process and the Dialer: Enable secure connection between Campaign Manager and Dialer and Enable secure-only connection To allow both secure and non-secure replication processes to connect to AW-HDS, uncheck the Enable secure-only connection checkbox. This runs the Logger replication process in mixed mode. To permit both secure and non-secure Dialer processes to connect, uncheck the Enable secure-only connection checkbox. This runs the Campaign Manager process in mixed mode. |
| Step 17 | Click Next . |
| Step 18 | Click Finish . |

| Note | The default SQL port is 1433. If the SQL server is configured with custom port, provide the custom port. |
|---|---|

| Note | If this Logger is being added for a Rogger server, where there are two IP addresses that are configured on the public Network
                                                               Interface Card (for IP-based prioritization), uncheck "Register this connection's addresses in DNS" for the private ethernet
                                                               card. In addition, ensure that there is only one A-record entry in the DNS server corresponding to the host name of the server,
                                                               which maps to the general priority IP address. This is necessary for processes like the campaign manager and replication running
                                                               as part of the Logger service, to listen on the right interface IP address for client connections. |
|---|---|

| Note | The event feed is processed and sent to the Syslog collector only if the Syslog collector is configured. For more information
                                                            about the Syslog event feed process, see the Serviceability Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
|---|---|

| Note | To fulfill the virtual memory requirement for Router in 48000 deployment, you must configure the Router service on both Side
                                                   A and Side B to launch the Router process (router.exe) as a 64-bit application. To change your Router process build architecture
                                                   from 32-bit to 64-bit, install 12.6(2) ES4 and perform the steps mentioned in the Readme file on the Software Downloads page.
                                                   You must deploy 12.6(2) ES25 for logger. |
|---|---|

| Step 1 | In the Web
                                                			 Setup tool, select Component Management > Routers . |
|---|---|
| Step 2 | Click Add . |
| Step 3 | On the Deployment page, choose the current instance. |
| Step 4 | In the Deployment dialog, select the appropriate side. |
| Step 5 | Click Duplexed , and then click Next . |
| Step 6 | In the Router Connectivity dialog, configure the Private Interface and Public Interfaces. Click Next . Note For the address input fields, use Fully Qualified Domain Names instead of IP addresses. When there are two IP addresses configured on the public Network Interface Card (for IP-based prioritization), manually add
                                                               two A-records on the DNS server. One A-record is for the high priority IP address and the other one is for the general priority
                                                               IP address. The host part of the two DNS entires should be different from the hostname of Windows server. Use the new DNS
                                                               entries to configure the interfaces. This note applies to the Router and to all PG machines. | Note | For the address input fields, use Fully Qualified Domain Names instead of IP addresses. When there are two IP addresses configured on the public Network Interface Card (for IP-based prioritization), manually add
                                                               two A-records on the DNS server. One A-record is for the high priority IP address and the other one is for the general priority
                                                               IP address. The host part of the two DNS entires should be different from the hostname of Windows server. Use the new DNS
                                                               entries to configure the interfaces. This note applies to the Router and to all PG machines. |
| Note | For the address input fields, use Fully Qualified Domain Names instead of IP addresses. When there are two IP addresses configured on the public Network Interface Card (for IP-based prioritization), manually add
                                                               two A-records on the DNS server. One A-record is for the high priority IP address and the other one is for the general priority
                                                               IP address. The host part of the two DNS entires should be different from the hostname of Windows server. Use the new DNS
                                                               entries to configure the interfaces. This note applies to the Router and to all PG machines. |
| Step 7 | Leave the Enable Peripheral Gateways field blank, and click Next . |
| Step 8 | In the Router Options dialog, the Enable Quality of Service (QoS) is enabled by default. Click Next . On the Router Quality of Service page, you see preconfigured values for the Router QoS for the Private Network. These values
                                                only appear if you selected a Side A Router. You can change the values in the DSCP fields if necessary. Keep QoS enabled for all Unified CCE Private network traffic. For most deployments, disable QoS for the public network traffic.
                                                For more details, refer to the appropriate section in the Solution Design Guide for Cisco Packaged Contact Center Enterprise , at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html . |
| Step 9 | In the Router
                                                   				Quality of Service dialog, click Next . |
| Step 10 | To configure secure communication between the Router and CCE core components on Router Security page, check the required check box as given below: Router and its peer and Logger: Enable secure connection between Router and its Peer and Logger Router and Peripheral Gateways: Enable secure connection between Router and Peripheral Gateways and Enable secure-only connection Real Time Server process running in the Router and the Real Time Distributor process running in the AW Distributor: Enable secure connection between Router and AW Distributors and Enable secure-only connection To allow both secure and non-secure Peripheral Gateways to connect, uncheck the Enable secure-only connection check box. This will run the Router in mixed mode. To enable both secure and non-secure Real Time Distributor processes to connect, uncheck the Enable secure-only connection check box. This will run the Router (Real Time Server) in mixed mode. |
| Step 11 | In the Summary dialog, make sure that the Router summary is
                                                			 correct, then click Finish . |

| Note | For the address input fields, use Fully Qualified Domain Names instead of IP addresses. When there are two IP addresses configured on the public Network Interface Card (for IP-based prioritization), manually add
                                                               two A-records on the DNS server. One A-record is for the high priority IP address and the other one is for the general priority
                                                               IP address. The host part of the two DNS entires should be different from the hostname of Windows server. Use the new DNS
                                                               entries to configure the interfaces. This note applies to the Router and to all PG machines. |
|---|---|

| Note | This procedure is required for activating Unified CCE services. However, you must postpone this task until you install Unified CCE components in all virtual machines given in the deployment model. |
|---|---|

| Step 1 | On each Unified CCE Server machine, open Unified CCE Service Control . |
|---|---|
| Step 2 | Select each Unified CCE Component in the following sequence and click Start . Logger A Router A Logger B Router B Administration & Data Servers |

| Sequence | Task |
|---|---|
| 1 | Configure SQL Server for CCE Components |
| 2 | Add Unified CCE Instance |
| 3 | Create HDS Database |
| 4 | Add Administration and Data Server Component to Instance |
| 5 | Configure ICM Database Lookup (optional) |
| 6 | Cisco SNMP Setup (optional) |

| Step 1 | Open the ICMDBA tool, and click Yes at any warnings that display. |
|---|---|
| Step 2 | Navigate to Servers > Instances . |
| Step 3 | Right-click the instance name and choose Create . |
| Step 4 | In the Select Component dialog box, choose Administration & Data Server . Click OK . |
| Step 5 | At the prompt "SQL Server is not configured properly. Do you want to configure it now?" , click Yes . |
| Step 6 | On the Configure dialog box, click OK . |
| Step 7 | On the Select AW Type dialog box, choose Enterprise . Click OK to open the Create Database dialog box. |
| Step 8 | Create the HDS database as follows: From the DB Type drop-down list, choose HDS . Click Add . On the Add Device dialog box, select Data . From the Available Drives list, choose the drive on which you want to install the database. In the Size field, you can leave the default value or enter an appropriate size for your deployment. Note You can use the Database Size Estimator Tool to calculate the appropriate size for your deployment. Click OK to return to the Create Database dialog box. Click Add . On the Add Device dialog box, select Log . From the Available Drives list, choose the drive on which you created the database. In the Size field, you can leave the default value or enter an appropriate size for your deployment. Click OK to return to the Create Database dialog box. | Note | You can use the Database Size Estimator Tool to calculate the appropriate size for your deployment. |
| Note | You can use the Database Size Estimator Tool to calculate the appropriate size for your deployment. |
| Step 9 | On the Create Database dialog box, click Create and then click Start . |
| Step 10 | When you see the successful creation message, click OK and then click Close . |

| Note | You can use the Database Size Estimator Tool to calculate the appropriate size for your deployment. |
|---|---|

| Step 1 | Navigate to the Unified CCE Administration > Overview > Infrastructure Settings > Deployment Settings . |
|---|---|
| Step 2 | Click the gear icon in the Deployment Type . The Configure your deployment wizard opens. |
| Step 3 | Select the deployment type as Packaged CCE: 4000 Agents or Packaged CCE: 12000 Agents from the drop-down list. |
| Step 4 | Use the Download Template to get the CSV template for the selected deployment type. |
| Step 5 | Fill the particulars in the file and save it. Table 2. CSV Template Details Column Description Required? Permissible Values name Unique identifier for the machine Yes Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         underscore (_), or hyphen (-). machineType MachineType Enum name Yes Mandatory machines are: CCE_ROGGER (applicable for 4000 Agents deployment) CCE_ROUTER (applicable for 12000 Agents deployment) CCE_LOGGER (applicable for 12000 Agents deployment) CCE_AW CUIC_PUBLISHER CUIC_SUBSCRIBER LIVE_DATA IDS_PUBLISHER IDS_SUBSCRIBER Optional machines: CCE_PG CVP FINESSE_PRIMARY FINESSE_SECONDARY CM_PUBLISHER CM_SUBSCRIBER HDS ECE (refers to ECE Data Server VM for ECE 400 agents and Services Server VM for ECE 1500 agents) ECE_WEB_SERVER CVP_REPORTING GATEWAYS CVVB CCCSP SOCIAL_MINER THIRD_PARTY_ MULTICHANNEL MEDIA_SERVER THIRD_PARTY_GATEWAY publicAddress Public address Yes Valid IP address or hostname connectionInfo Connection information of the machine Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CCCSP , GATEWAY and LIVE_DATA Enter the username and password in the following format: userName=<user>&password=<password> For more information on the credentials of each component, see Table 1 . ConnectionInfo is optional if you are configuring FTP for CVP (Media Server) . Append the FTP attributes to the username and password in the following format: userName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. privateAddress Private address Required for ROGGER, ROUTER, LOGGER, and PG Valid IP address or hostname peripheralSetName Peripheral set name Required for PG, CUCM, Finesse, CVP Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         or an underscore (_). side Side information Yes sideA sideB | Column | Description | Required? | Permissible Values | name | Unique identifier for the machine | Yes | Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         underscore (_), or hyphen (-). | machineType | MachineType Enum name | Yes | Mandatory machines are: CCE_ROGGER (applicable for 4000 Agents deployment) CCE_ROUTER (applicable for 12000 Agents deployment) CCE_LOGGER (applicable for 12000 Agents deployment) CCE_AW CUIC_PUBLISHER CUIC_SUBSCRIBER LIVE_DATA IDS_PUBLISHER IDS_SUBSCRIBER Optional machines: CCE_PG CVP FINESSE_PRIMARY FINESSE_SECONDARY CM_PUBLISHER CM_SUBSCRIBER HDS ECE (refers to ECE Data Server VM for ECE 400 agents and Services Server VM for ECE 1500 agents) ECE_WEB_SERVER CVP_REPORTING GATEWAYS CVVB CCCSP SOCIAL_MINER THIRD_PARTY_ MULTICHANNEL MEDIA_SERVER THIRD_PARTY_GATEWAY | publicAddress | Public address | Yes | Valid IP address or hostname | connectionInfo | Connection information of the machine | Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CCCSP , GATEWAY and LIVE_DATA | Enter the username and password in the following format: userName=<user>&password=<password> For more information on the credentials of each component, see Table 1 . ConnectionInfo is optional if you are configuring FTP for CVP (Media Server) . Append the FTP attributes to the username and password in the following format: userName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. | Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. | privateAddress | Private address | Required for ROGGER, ROUTER, LOGGER, and PG | Valid IP address or hostname | peripheralSetName | Peripheral set name | Required for PG, CUCM, Finesse, CVP | Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         or an underscore (_). | side | Side information | Yes | sideA sideB |
| Column | Description | Required? | Permissible Values |
| name | Unique identifier for the machine | Yes | Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         underscore (_), or hyphen (-). |
| machineType | MachineType Enum name | Yes | Mandatory machines are: CCE_ROGGER (applicable for 4000 Agents deployment) CCE_ROUTER (applicable for 12000 Agents deployment) CCE_LOGGER (applicable for 12000 Agents deployment) CCE_AW CUIC_PUBLISHER CUIC_SUBSCRIBER LIVE_DATA IDS_PUBLISHER IDS_SUBSCRIBER Optional machines: CCE_PG CVP FINESSE_PRIMARY FINESSE_SECONDARY CM_PUBLISHER CM_SUBSCRIBER HDS ECE (refers to ECE Data Server VM for ECE 400 agents and Services Server VM for ECE 1500 agents) ECE_WEB_SERVER CVP_REPORTING GATEWAYS CVVB CCCSP SOCIAL_MINER THIRD_PARTY_ MULTICHANNEL MEDIA_SERVER THIRD_PARTY_GATEWAY |
| publicAddress | Public address | Yes | Valid IP address or hostname |
| connectionInfo | Connection information of the machine | Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CCCSP , GATEWAY and LIVE_DATA | Enter the username and password in the following format: userName=<user>&password=<password> For more information on the credentials of each component, see Table 1 . ConnectionInfo is optional if you are configuring FTP for CVP (Media Server) . Append the FTP attributes to the username and password in the following format: userName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. | Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| privateAddress | Private address | Required for ROGGER, ROUTER, LOGGER, and PG | Valid IP address or hostname |
| peripheralSetName | Peripheral set name | Required for PG, CUCM, Finesse, CVP | Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         or an underscore (_). |
| side | Side information | Yes | sideA sideB |
| Step 6 | Upload the file and click Next . |
| Step 7 | Wait for validation to be completed. During the validation, tasks are performed depending on the components defined in the CSV template. For more information about
                                             the tasks, see the Automated Initialization Tasks for 4000 and 12000 Agent Deployments topic. Note If any of the performed tasks fails, then all the tasks are reverted. If validation fails, then click Back to fix the issues in the file and upload the file again, else click Done . The main site that is thus created is added to the Inventory page. | Note | If any of the performed tasks fails, then all the tasks are reverted. |
| Note | If any of the performed tasks fails, then all the tasks are reverted. |

| Column | Description | Required? | Permissible Values |
|---|---|---|---|
| name | Unique identifier for the machine | Yes | Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         underscore (_), or hyphen (-). |
| machineType | MachineType Enum name | Yes | Mandatory machines are: CCE_ROGGER (applicable for 4000 Agents deployment) CCE_ROUTER (applicable for 12000 Agents deployment) CCE_LOGGER (applicable for 12000 Agents deployment) CCE_AW CUIC_PUBLISHER CUIC_SUBSCRIBER LIVE_DATA IDS_PUBLISHER IDS_SUBSCRIBER Optional machines: CCE_PG CVP FINESSE_PRIMARY FINESSE_SECONDARY CM_PUBLISHER CM_SUBSCRIBER HDS ECE (refers to ECE Data Server VM for ECE 400 agents and Services Server VM for ECE 1500 agents) ECE_WEB_SERVER CVP_REPORTING GATEWAYS CVVB CCCSP SOCIAL_MINER THIRD_PARTY_ MULTICHANNEL MEDIA_SERVER THIRD_PARTY_GATEWAY |
| publicAddress | Public address | Yes | Valid IP address or hostname |
| connectionInfo | Connection information of the machine | Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CCCSP , GATEWAY and LIVE_DATA | Enter the username and password in the following format: userName=<user>&password=<password> For more information on the credentials of each component, see Table 1 . ConnectionInfo is optional if you are configuring FTP for CVP (Media Server) . Append the FTP attributes to the username and password in the following format: userName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. | Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| privateAddress | Private address | Required for ROGGER, ROUTER, LOGGER, and PG | Valid IP address or hostname |
| peripheralSetName | Peripheral set name | Required for PG, CUCM, Finesse, CVP | Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         or an underscore (_). |
| side | Side information | Yes | sideA sideB |

| Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
|---|---|

| Note | If any of the performed tasks fails, then all the tasks are reverted. |
|---|---|

| Component | Automated Initialization Tasks | Other Dependent Components |
|---|---|---|
| Unified CCE PG | Creates the Agent Peripheral Gateway (PG) and PIMs | Cisco Unified Communications Manager (CUCM) and Cisco Finesse |
| Creates the Media Routing PG (MR PG), without PIMs | None |
| Creates the VRU PG and PIMs | Unified Customer Voice Portal |
| Creates the routing client for each peripheral Note Depending on your call flow requirements, create Network VRU labels in the Label list option using the Configuration Manager Tool. Network VRU Type 10 and Type 2 must be created in the Network VRU Explorer  using Configuration Manager Tool. For more information, see the online help in Configuration Manager Tool . | Note | Depending on your call flow requirements, create Network VRU labels in the Label list option using the Configuration Manager Tool. Network VRU Type 10 and Type 2 must be created in the Network VRU Explorer  using Configuration Manager Tool. For more information, see the online help in Configuration Manager Tool . | None |
| Note | Depending on your call flow requirements, create Network VRU labels in the Label list option using the Configuration Manager Tool. Network VRU Type 10 and Type 2 must be created in the Network VRU Explorer  using Configuration Manager Tool. For more information, see the online help in Configuration Manager Tool . |
| Unified Customer Voice Portal | Configures the Unified CVP Call Server components Configures the Unified CVP VXML Server components Configures the Unified CVP Media Server components | None |
| Unified CVP Reporting Server | Configures the Unified CVP Reporting Server components (not applicable for peripheral set) | None |
| Live Data | Redeploys Lives data | CUCM and Cisco Finesse |

| Note | Depending on your call flow requirements, create Network VRU labels in the Label list option using the Configuration Manager Tool. Network VRU Type 10 and Type 2 must be created in the Network VRU Explorer  using Configuration Manager Tool. For more information, see the online help in Configuration Manager Tool . |
|---|---|

| Note | Once a Packaged CCE deployment is initialized, you cannot switch to another Packaged CCE deployment type, including Packaged
                                          Lab Mode. However, you can switch to a Unified CCE deployment type. |
|---|---|

| Item | Notes | Actions |
|---|---|---|
| Set the Principal AW | Only one AW machine can be Principal AW at a time. | Specifying the Principal AW is required. The first SideA AW machine in the CSV file is the principal AW. The Principal AW (Admin Workstation) is responsible for managing background tasks that are run periodically to sync configuration
                                          with other solution components, such as SSO management, Smart Licensing, etc. The Principal AW is used by the following features: File Transfer Context Service Registration SSO Registration and Enablement Differential Sync You can change the Principal AW by selecting a different AW in the Inventory. Set the AW on which you make most of your configuration
                                          changes as the Principal AW. To set the Principal AW: Click the AW to open the Edit CCE AW window. Check the PrincipalAW check box. Unified CCE Diagnostic Framework Service domain, username, and password. These credentials must be of a domain user who is
                                                a member of the Config security group for the instance, and valid on all Unified CCE components in your deployment (the Side
                                                A and Side B Unified CCE Roggers, PGs, and AW-HDS-DDSs). Make sure that the Unified CCE Diagnostic Framework Service on each
                                                Unified CCE server is running. Note Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. Click Save . | Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
| Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
| Set the Principal VVB | Only one of the VVB machines can be a Principal VVB. | Principal VVB is used to configure the Customer Virtual Assistant feature. First added VVB machine into the Inventory is set as the Principal VVB by default. In Upgrade scenario, one of the configured
                                          VVBs is set as a Principal VVB. A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports Customer Virtual Assistant feature. To set a VVB as a Principal VVB, do the following: Click the VVB to open the Edit VVB window. Check the Principal check box. Click Save . |
| View Statistics | Unified CVP and CVP Reporting Server | You can launch statistics by hovering over the following VMs and clicking the Statistics icon: Unified CVP Unified CVP Reporting For more information, see Unified CVP Statistics and Unified CVP Reporting Statistics . |

| Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
|---|---|

| Note | If you change the password of any of the Packaged CCE components, you must update the password in the respective VM in the
                                          system inventory. |
|---|---|

| Step 1 | Open the Unified CCE Web Setup tool from shortcut on your desktop. |
|---|---|
| Step 2 | Sign in as a
                                          			 domain user with local administrator rights. |
| Step 3 | Click Instance Management , and then click Add . |
| Step 4 | On the Add
                                             			 Instance page, from the drop-down list, choose the customer Facility and Instance . |
| Step 5 | Enter an
                                          			 instance number. The same
                                             				instance name can occur more than once in a domain, so the instance number
                                             				provides the uniqueness. The instance number must be between 0 and 24. The
                                             				instance number must match for the same instance across your entire deployment.
                                             				For an Enterprise (single instance) deployment, select 0 unless there are
                                             				reasons to select another value. |
| Step 6 | For Logger and Administrator & Data server, enter the custom SQL server port to the Local SQL Server Port field. The default SQL port is 1433. If the SQL server is configured with custom port, provide the custom port. |
| Step 7 | Click Save . Note These steps of adding instance must be repeated on each Windows Server VM that hosts the Unified ICM component(s). | Note | These steps of adding instance must be repeated on each Windows Server VM that hosts the Unified ICM component(s). |
| Note | These steps of adding instance must be repeated on each Windows Server VM that hosts the Unified ICM component(s). |

| Note | These steps of adding instance must be repeated on each Windows Server VM that hosts the Unified ICM component(s). |
|---|---|

| Note | If any machine in the Inventory is updated, it can take approximately three minutes for the status to appear. |
|---|---|

| Note | Repeat the following tasks each time you add the Peripheral Set to the Main Site or Remote Site. See the section "Add and
                                       Maintain Peripheral Set" for information on Peripheral Set. |
|---|---|

| Configuration Tasks |
|---|
| If the Peripheral Set contains CUCM PG: Install Cisco JTAPI Client on PG Install Cisco JTAPI Client on PG Set up CTI Server |
| If the peripheral set contains VRU PG, manually restart the CVP Servers. |
| If the peripheral set contains MR PG, Add PIMs to the Media Routing Peripheral Gateway |

| Note | Continue with the steps provided in this
                                          					section if you are installing the JTAPI client for CUCM version earlier than
                                          					Release 12.5. To install the JTAPI client for CUCM, Release 12.5 and above, see Install Cisco JTAPI Client on PG . |
|---|---|

| Step 1 | Open a browser
                                       			 window on the PG machine. |
|---|---|
| Step 2 | Enter the URL for the Unified Communications Manager Administration utility: http://< Unified Communications Manager machine name> /ccmadmin. |
| Step 3 | Enter the username and password that you created while installing and
                                       					configuring the Unified Communications Manager. |
| Step 4 | Choose Application > Plugins . Click Find . |
| Step 5 | Click the link next to Download Cisco JTAPI for
                                          					Windows .We recommend you to download the 64 bit version. However, if
                                       					you have already downloaded the 32 bit version, you can proceed to step 7. Download the JTAPI plugin file. |
| Step 6 | Choose Save and save the plugin file to a location of your choice. |
| Step 7 | Open the
                                       			 installer. |
| Step 8 | In the Security Warning box, click Yes to install. |
| Step 9 | Choose Next or Continue through the remaining Setup screens. Accept the default installation path. |
| Step 10 | When prompted for the TFTP Server IP address, enter the CUCM IP address. |
| Step 11 | Click Finish . |
| Step 12 | Reboot the
                                       			 machine. |

| Step 1 | Open a browser
                                          			 window on the PG machine. |
|---|---|
| Step 2 | Enter the URL for the Unified Communications Manager Administration utility: http://< Unified Communications Manager machine name> /ccmadmin. |
| Step 3 | Enter the username and password that you created while installing and
                                          					configuring the Unified Communications Manager. |
| Step 4 | Choose Application > Plugins . Click Find . |
| Step 5 | Click the link next to Download Cisco JTAPI Client for
                                                Windows 64 bit or Download Cisco JTAPI Client for
                                                Windows 32 bit. Download the JTAPI plugin file. |
| Step 6 | Choose Save and save the plugin file to a location of your choice. |
| Step 7 | Unzip the JTAPI plugin zip file to the default location or a location of your
                                          choice. There are two folders in the unzipped folder CiscoJTAPIx64 and CiscoJTAPIx32 . |
| Step 8 | Run the install64.bat file in the CiscoJTAPIx64 folder or run the install32.bat file in the CiscoJTAPIx32 folder. The default install path for JTAPI client is C:\Program Files\Cisco\JTAPITools . |
| Step 9 | To accept the default installation path, click Enter and
                                          proceed. Follow the instructions. Click Enter whenever necessary as
                                             per the instructions. The JTAPI client installation completes at the default location. The
                                             following message is displayed: Installation Complete. |
| Step 10 | Reboot the machine. |

| Note | The default location, where the JTAPI client is installed, also contains the uninstall64.bat and uninstall32.bat file. Use this file to uninstall this
                                             version of the client, if necessary. |
|---|---|

| Step 1 | Open Peripheral Gateway Setup tool from Unified CCE Tools on the desktop. |
|---|---|
| Step 2 | Click Add in the Instance Components section. The ICM
                                             				Component Selection dialog box opens. |
| Step 3 | Click CTI
                                             				Server , and click OK . The CTI Server
                                             				Properties dialog box opens. |

| Step 1 | In the CTI
                                          		  Server Properties dialog box, check Production mode and Auto start at system startup unless your Unified CCE support provider tells you otherwise. These settings set the
                                          			 CTI Server Service startup type to Automatic, so the CTI Server starts
                                          			 automatically when the machine starts up. |
|---|---|
| Step 2 | Check the Duplexed CTI Server option if you are
                                          			 configuring redundant CTI Server machines. |
| Step 3 | In the CG Node Properties section, the numeric portion of the CG
                                          			 node ID must match the PG node ID (for example, CG
                                          			 1 and PG 1). |
| Step 4 | The ICM system ID is the Device Management
                                          			 Protocol (DMP) number of the PG associated with the CTI Gateway. Generally this
                                          			 number is the number associated with the CG ID in step 3. |
| Step 5 | If the CTI Server you add is duplexed, specify which Side you are setting up: Side A or Side B. If
                                          			 the CTI Server is simplex, choose Side A. |
| Step 6 | Click Next . The CTI Server Component Properties dialog box opens. |

| Important | Non-Secured only mode is not supported. |
|---|---|

| Note | To enable secured connection between the components, ensure to complete the security certificate management process. For more information, see the chapter Certificate Management for Secured Connections in Security Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html . |
|---|---|

| Step 1 | Select the appropriate connection type. For Secured Connection , check the Enable Secure-Only Mode check box. This option disables the Non-Secured Connection Port field. For Mixed-mode connection , ensure that the Enable Secure-Only Mode check box is unchecked. This is the default connection mode. |
|---|---|
| Step 2 | To ensure that an agent is logged in to the client before the client receives events from the CTI Server, check the Agent Login Required for Client Events check box. This ensures that the clients are prevented from accessing data for other agents. |
| Step 3 | Click Next . The CTI Server
                                             				Network Interface Properties dialog box opens. |

| Step 1 | In the CTI Server Network Interface Properties dialog box, in the PG public interfaces section, enter the public network
                                          			 addresses for the PGs associated with the CTI Server. |
|---|---|
| Step 2 | In the CG private interfaces section, enter the private network
                                          			 addresses of the CTI Server. |
| Step 3 | In the CG visible interfaces section, enter the public network addresses of the CTI Server. |
| Step 4 | Click Next . The Check Setup Information window opens. |

| Step 1 | In the Check Setup Information window, ensure that the settings
                                          			 displayed are as you intended. If you want to modify any settings before
                                          			 proceeding, use the Back button. |
|---|---|
| Step 2 | When the settings are correct, click Next . |
| Step 3 | The final screen displays and asks whether you want to start the Node Manager now. |
| Step 4 | Click Finish to exit setup (and optionally start the
                                          			 Node Manager). If you choose to start it, the Node Manager automatically starts
                                             				the other Unified CCE processes on the CTI Server. |

| Note | The CVP configurations are site specific. Side A and Side B configurations per site must be the same. |
|---|---|

| Configuration Tasks |
|---|
| To secure communication between Call Server and ICM, see Secure Flow Communication . For more information about securing CVP communication, see Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| CVP Server Services Setup |
| Configure Media Server |
| Configure SNMP |

| Step 1 | Log in to the CVP server using Administrator credentials. |
|---|---|
| Step 2 | Navigate to C:\Cisco\CVP\conf\SNMPD.CNF . |
| Step 3 | Complete the following parameters to do the SNMP configuration: Note Ensure to enter the parameter values in a single line, without a break. Table 4. SNMP configuration parameters Parameter Description Format snmpCommunityEntry Configure the SNMP agent that runs on the Unified CVP device to use the V1/V2 SNMP protocol to communicate with an SNMP management
                                                         station; add and delete SNMP V1/V2c community strings and associate community strings with the device. snmpCommunityEntry <snmpCommunityIndex> 
<snmpCommunityName> <snmpCommunitySecurityName> 
<snmpCommunityContextEngineID> <snmpCommunityContextName> 
<snmpCommunityTransportTag> <snmpCommunityStorageType> Example: snmpCommunityEntry v2ccvp cvp cvp localSnmpID - - readOnly vacmSecurityToGroupEntry Configure authentication group for V1/V2C SNMP protocol. vacmSecurityToGroupEntry  <vacmSecurityModel> 
<vacmSecurityName> <vacmGroupName> 
<vacmSecurityToGroupStorageType> Example: vacmSecurityToGroupEntry  snmpv2c cvp 
v2cNoAuthNoPrivGroup nonVolatile snmpNotifyEntry Configure the SNMP agent that runs on the Unified CVP device to use the V1/V2 SNMP protocol to communicate with an SNMP management
                                                         station; configure a destination to receive SNMP notifications from an SNMP management station. snmpNotifyEntry <snmpNotifyName> 
<snmpNotifyTag> <snmpNotifyType> <snmpNotifyStorageType> Example: snmpNotifyEntry Descvp Descvp-TrapTag trap readOnly usmUserEntry Configure the SNMP agent that runs on the Unified CVP device to use the V3 SNMP protocol to communicate with an SNMP management
                                                         station; add and delete SNMP users and set their access privileges and associate SNMP users with devices. usmUserEntry <usmUserEngineID> 
<usmUserName> <usmUserAuthProtocol> <usmUserPrivProtocol> <usmUserStorageType> 
<usmTargetTag> <AuthKey> <PrivKey> Example: usmUserEntry  localSnmpID < username > usmHMACMD5AuthProtocol usmNoPrivProtocol \
readOnly - password - Note Ensure that the password is enclosed within "-" as shown in the example. Otherwise, the entry will be discarded and left unencrypted. snmpNotifyEntry Configure the SNMP agent that runs on the Unified CVP device to use the V3 SNMP protocol to communicate with an SNMP management
                                                         station; configure a destination to receive SNMP notifications from an SNMP management station. snmpNotifyEntry <snmpNotifyName> <snmpNotifyTag> 
<snmpNotifyType> <snmpNotifyStorageType> Example: snmpNotifyEntry Descvp Descvp-TrapTag trap readOnly sysLocation Configure the MIB2 System Group system location settings, and associate the MIB2 System Group with devices. <octetString> Example: MIBLoc sysContact Configure the MIB2 System Group system contact and associate the MIB2 System Group with devices. <octetString> For example: MIBContact snmpTargetAddrEntry Configure SNMP trap receiver target IP. snmpTargetAddrEntry  <snmpTargetAddrName> 
<snmpTargetAddrTDomain> <snmpTargetAddrTAddress> 
<snmpTargetAddrTimeout> <snmpTargetAddrRetryCount> 
<snmpTargetAddrTagList> <snmpTargetAddrParams> 
<snmpTargetAddrStorageType> <snmpTargetAddrTMask> 
<snmpTargetAddrMMS> Example: snmpTargetAddrEntry  targetDesV2-Addr1 
snmpUDPDomain 10.100.10.100:0 0 0 \ targetDesV2-TrapTag 
targetDesV2-TrapParams readOnly 255.255.255.255:0 2048 snmpTargetParamsEntry Configure the parameters to be used while sending notifications. snmpTargetParamsEntry  <snmpTargetParamsName> 
<snmpTargetParamsMPModel> <snmpTargetParamsSecurityModel> 
<snmpTargetParamsSecurityName> <snmpTargetParamsSecurityLevel> 
<snmpTargetParamsStorageType> Example: snmpTargetParamsEntry  params1 0 
snmpv1 principal noAuthNoPriv 
nonVolatile | Note | Ensure to enter the parameter values in a single line, without a break. | Parameter | Description | Format | snmpCommunityEntry | Configure the SNMP agent that runs on the Unified CVP device to use the V1/V2 SNMP protocol to communicate with an SNMP management
                                                         station; add and delete SNMP V1/V2c community strings and associate community strings with the device. | snmpCommunityEntry <snmpCommunityIndex> 
<snmpCommunityName> <snmpCommunitySecurityName> 
<snmpCommunityContextEngineID> <snmpCommunityContextName> 
<snmpCommunityTransportTag> <snmpCommunityStorageType> Example: snmpCommunityEntry v2ccvp cvp cvp localSnmpID - - readOnly | vacmSecurityToGroupEntry | Configure authentication group for V1/V2C SNMP protocol. | vacmSecurityToGroupEntry  <vacmSecurityModel> 
<vacmSecurityName> <vacmGroupName> 
<vacmSecurityToGroupStorageType> Example: vacmSecurityToGroupEntry  snmpv2c cvp 
v2cNoAuthNoPrivGroup nonVolatile | snmpNotifyEntry | Configure the SNMP agent that runs on the Unified CVP device to use the V1/V2 SNMP protocol to communicate with an SNMP management
                                                         station; configure a destination to receive SNMP notifications from an SNMP management station. | snmpNotifyEntry <snmpNotifyName> 
<snmpNotifyTag> <snmpNotifyType> <snmpNotifyStorageType> Example: snmpNotifyEntry Descvp Descvp-TrapTag trap readOnly | usmUserEntry | Configure the SNMP agent that runs on the Unified CVP device to use the V3 SNMP protocol to communicate with an SNMP management
                                                         station; add and delete SNMP users and set their access privileges and associate SNMP users with devices. | usmUserEntry <usmUserEngineID> 
<usmUserName> <usmUserAuthProtocol> <usmUserPrivProtocol> <usmUserStorageType> 
<usmTargetTag> <AuthKey> <PrivKey> Example: usmUserEntry  localSnmpID < username > usmHMACMD5AuthProtocol usmNoPrivProtocol \
readOnly - password - Note Ensure that the password is enclosed within "-" as shown in the example. Otherwise, the entry will be discarded and left unencrypted. | Note | Ensure that the password is enclosed within "-" as shown in the example. Otherwise, the entry will be discarded and left unencrypted. | snmpNotifyEntry | Configure the SNMP agent that runs on the Unified CVP device to use the V3 SNMP protocol to communicate with an SNMP management
                                                         station; configure a destination to receive SNMP notifications from an SNMP management station. | snmpNotifyEntry <snmpNotifyName> <snmpNotifyTag> 
<snmpNotifyType> <snmpNotifyStorageType> Example: snmpNotifyEntry Descvp Descvp-TrapTag trap readOnly | sysLocation | Configure the MIB2 System Group system location settings, and associate the MIB2 System Group with devices. | <octetString> Example: MIBLoc | sysContact | Configure the MIB2 System Group system contact and associate the MIB2 System Group with devices. | <octetString> For example: MIBContact | snmpTargetAddrEntry | Configure SNMP trap receiver target IP. | snmpTargetAddrEntry  <snmpTargetAddrName> 
<snmpTargetAddrTDomain> <snmpTargetAddrTAddress> 
<snmpTargetAddrTimeout> <snmpTargetAddrRetryCount> 
<snmpTargetAddrTagList> <snmpTargetAddrParams> 
<snmpTargetAddrStorageType> <snmpTargetAddrTMask> 
<snmpTargetAddrMMS> Example: snmpTargetAddrEntry  targetDesV2-Addr1 
snmpUDPDomain 10.100.10.100:0 0 0 \ targetDesV2-TrapTag 
targetDesV2-TrapParams readOnly 255.255.255.255:0 2048 | snmpTargetParamsEntry | Configure the parameters to be used while sending notifications. | snmpTargetParamsEntry  <snmpTargetParamsName> 
<snmpTargetParamsMPModel> <snmpTargetParamsSecurityModel> 
<snmpTargetParamsSecurityName> <snmpTargetParamsSecurityLevel> 
<snmpTargetParamsStorageType> Example: snmpTargetParamsEntry  params1 0 
snmpv1 principal noAuthNoPriv 
nonVolatile |
| Note | Ensure to enter the parameter values in a single line, without a break. |
| Parameter | Description | Format |
| snmpCommunityEntry | Configure the SNMP agent that runs on the Unified CVP device to use the V1/V2 SNMP protocol to communicate with an SNMP management
                                                         station; add and delete SNMP V1/V2c community strings and associate community strings with the device. | snmpCommunityEntry <snmpCommunityIndex> 
<snmpCommunityName> <snmpCommunitySecurityName> 
<snmpCommunityContextEngineID> <snmpCommunityContextName> 
<snmpCommunityTransportTag> <snmpCommunityStorageType> Example: snmpCommunityEntry v2ccvp cvp cvp localSnmpID - - readOnly |
| vacmSecurityToGroupEntry | Configure authentication group for V1/V2C SNMP protocol. | vacmSecurityToGroupEntry  <vacmSecurityModel> 
<vacmSecurityName> <vacmGroupName> 
<vacmSecurityToGroupStorageType> Example: vacmSecurityToGroupEntry  snmpv2c cvp 
v2cNoAuthNoPrivGroup nonVolatile |
| snmpNotifyEntry | Configure the SNMP agent that runs on the Unified CVP device to use the V1/V2 SNMP protocol to communicate with an SNMP management
                                                         station; configure a destination to receive SNMP notifications from an SNMP management station. | snmpNotifyEntry <snmpNotifyName> 
<snmpNotifyTag> <snmpNotifyType> <snmpNotifyStorageType> Example: snmpNotifyEntry Descvp Descvp-TrapTag trap readOnly |
| usmUserEntry | Configure the SNMP agent that runs on the Unified CVP device to use the V3 SNMP protocol to communicate with an SNMP management
                                                         station; add and delete SNMP users and set their access privileges and associate SNMP users with devices. | usmUserEntry <usmUserEngineID> 
<usmUserName> <usmUserAuthProtocol> <usmUserPrivProtocol> <usmUserStorageType> 
<usmTargetTag> <AuthKey> <PrivKey> Example: usmUserEntry  localSnmpID < username > usmHMACMD5AuthProtocol usmNoPrivProtocol \
readOnly - password - Note Ensure that the password is enclosed within "-" as shown in the example. Otherwise, the entry will be discarded and left unencrypted. | Note | Ensure that the password is enclosed within "-" as shown in the example. Otherwise, the entry will be discarded and left unencrypted. |
| Note | Ensure that the password is enclosed within "-" as shown in the example. Otherwise, the entry will be discarded and left unencrypted. |
| snmpNotifyEntry | Configure the SNMP agent that runs on the Unified CVP device to use the V3 SNMP protocol to communicate with an SNMP management
                                                         station; configure a destination to receive SNMP notifications from an SNMP management station. | snmpNotifyEntry <snmpNotifyName> <snmpNotifyTag> 
<snmpNotifyType> <snmpNotifyStorageType> Example: snmpNotifyEntry Descvp Descvp-TrapTag trap readOnly |
| sysLocation | Configure the MIB2 System Group system location settings, and associate the MIB2 System Group with devices. | <octetString> Example: MIBLoc |
| sysContact | Configure the MIB2 System Group system contact and associate the MIB2 System Group with devices. | <octetString> For example: MIBContact |
| snmpTargetAddrEntry | Configure SNMP trap receiver target IP. | snmpTargetAddrEntry  <snmpTargetAddrName> 
<snmpTargetAddrTDomain> <snmpTargetAddrTAddress> 
<snmpTargetAddrTimeout> <snmpTargetAddrRetryCount> 
<snmpTargetAddrTagList> <snmpTargetAddrParams> 
<snmpTargetAddrStorageType> <snmpTargetAddrTMask> 
<snmpTargetAddrMMS> Example: snmpTargetAddrEntry  targetDesV2-Addr1 
snmpUDPDomain 10.100.10.100:0 0 0 \ targetDesV2-TrapTag 
targetDesV2-TrapParams readOnly 255.255.255.255:0 2048 |
| snmpTargetParamsEntry | Configure the parameters to be used while sending notifications. | snmpTargetParamsEntry  <snmpTargetParamsName> 
<snmpTargetParamsMPModel> <snmpTargetParamsSecurityModel> 
<snmpTargetParamsSecurityName> <snmpTargetParamsSecurityLevel> 
<snmpTargetParamsStorageType> Example: snmpTargetParamsEntry  params1 0 
snmpv1 principal noAuthNoPriv 
nonVolatile |
| Step 4 | Save the changes. |
| Step 5 | Go to Services and restart Cisco CVP SNMP Management . |

| Note | Ensure to enter the parameter values in a single line, without a break. |
|---|---|

| Parameter | Description | Format |
|---|---|---|
| snmpCommunityEntry | Configure the SNMP agent that runs on the Unified CVP device to use the V1/V2 SNMP protocol to communicate with an SNMP management
                                                         station; add and delete SNMP V1/V2c community strings and associate community strings with the device. | snmpCommunityEntry <snmpCommunityIndex> 
<snmpCommunityName> <snmpCommunitySecurityName> 
<snmpCommunityContextEngineID> <snmpCommunityContextName> 
<snmpCommunityTransportTag> <snmpCommunityStorageType> Example: snmpCommunityEntry v2ccvp cvp cvp localSnmpID - - readOnly |
| vacmSecurityToGroupEntry | Configure authentication group for V1/V2C SNMP protocol. | vacmSecurityToGroupEntry  <vacmSecurityModel> 
<vacmSecurityName> <vacmGroupName> 
<vacmSecurityToGroupStorageType> Example: vacmSecurityToGroupEntry  snmpv2c cvp 
v2cNoAuthNoPrivGroup nonVolatile |
| snmpNotifyEntry | Configure the SNMP agent that runs on the Unified CVP device to use the V1/V2 SNMP protocol to communicate with an SNMP management
                                                         station; configure a destination to receive SNMP notifications from an SNMP management station. | snmpNotifyEntry <snmpNotifyName> 
<snmpNotifyTag> <snmpNotifyType> <snmpNotifyStorageType> Example: snmpNotifyEntry Descvp Descvp-TrapTag trap readOnly |
| usmUserEntry | Configure the SNMP agent that runs on the Unified CVP device to use the V3 SNMP protocol to communicate with an SNMP management
                                                         station; add and delete SNMP users and set their access privileges and associate SNMP users with devices. | usmUserEntry <usmUserEngineID> 
<usmUserName> <usmUserAuthProtocol> <usmUserPrivProtocol> <usmUserStorageType> 
<usmTargetTag> <AuthKey> <PrivKey> Example: usmUserEntry  localSnmpID < username > usmHMACMD5AuthProtocol usmNoPrivProtocol \
readOnly - password - Note Ensure that the password is enclosed within "-" as shown in the example. Otherwise, the entry will be discarded and left unencrypted. | Note | Ensure that the password is enclosed within "-" as shown in the example. Otherwise, the entry will be discarded and left unencrypted. |
| Note | Ensure that the password is enclosed within "-" as shown in the example. Otherwise, the entry will be discarded and left unencrypted. |
| snmpNotifyEntry | Configure the SNMP agent that runs on the Unified CVP device to use the V3 SNMP protocol to communicate with an SNMP management
                                                         station; configure a destination to receive SNMP notifications from an SNMP management station. | snmpNotifyEntry <snmpNotifyName> <snmpNotifyTag> 
<snmpNotifyType> <snmpNotifyStorageType> Example: snmpNotifyEntry Descvp Descvp-TrapTag trap readOnly |
| sysLocation | Configure the MIB2 System Group system location settings, and associate the MIB2 System Group with devices. | <octetString> Example: MIBLoc |
| sysContact | Configure the MIB2 System Group system contact and associate the MIB2 System Group with devices. | <octetString> For example: MIBContact |
| snmpTargetAddrEntry | Configure SNMP trap receiver target IP. | snmpTargetAddrEntry  <snmpTargetAddrName> 
<snmpTargetAddrTDomain> <snmpTargetAddrTAddress> 
<snmpTargetAddrTimeout> <snmpTargetAddrRetryCount> 
<snmpTargetAddrTagList> <snmpTargetAddrParams> 
<snmpTargetAddrStorageType> <snmpTargetAddrTMask> 
<snmpTargetAddrMMS> Example: snmpTargetAddrEntry  targetDesV2-Addr1 
snmpUDPDomain 10.100.10.100:0 0 0 \ targetDesV2-TrapTag 
targetDesV2-TrapParams readOnly 255.255.255.255:0 2048 |
| snmpTargetParamsEntry | Configure the parameters to be used while sending notifications. | snmpTargetParamsEntry  <snmpTargetParamsName> 
<snmpTargetParamsMPModel> <snmpTargetParamsSecurityModel> 
<snmpTargetParamsSecurityName> <snmpTargetParamsSecurityLevel> 
<snmpTargetParamsStorageType> Example: snmpTargetParamsEntry  params1 0 
snmpv1 principal noAuthNoPriv 
nonVolatile |

| Note | Ensure that the password is enclosed within "-" as shown in the example. Otherwise, the entry will be discarded and left unencrypted. |
|---|---|

| Task |
|---|
| Set Up Application User |
| Configure Fully Qualified Domain Name |
| Configure Cisco Unified Communications Manager Groups |
| Set Up Device Pool |
| Configure Conference Bridges |
| Configure Media Termination Points |
| Transcoder Configuration in Unified CM and IOS Gateway |
| Configure Media Resource Groups |
| Configure and Associate Media Resource Group List |
| Configure CTI Route Point |
| Configure Ingress Gateways for Locations-based Call Admission Control |
| Add a SIP Profile in Unified CM |
| Configure Trunk |
| Configure Route Group |
| Configure Route List |
| Configure Route Pattern |
| Configure a Law Codec |
| Configure SNMP |
| Configure Agent Desk Settings |

| Step 1 | Choose System > device
                                                				  pool . |
|---|---|
| Step 2 | Click Add
                                             				new . |
| Step 3 | Provide an
                                          			 appropriate device pool name in Device Pool
                                             				Name . |
| Step 4 | Select a
                                          			 corresponding Call manager group in Cisco Unified
                                             				Communications Manager group . |
| Step 5 | Select appropriate Date/Time Group and Region . |
| Step 6 | Select an
                                          			 appropriate Media resource group list in Media Resource
                                             				Group List. |
| Step 7 | Click Save . |

| Step 1 | In Unified Communications Manager, Choose User Management > Application User . |
|---|---|
| Step 2 | In the
                                          			 Application User Configuration window, click Add
                                             				New . |
| Step 3 | Enter the User ID that is set in the Peripheral Gateway Setup. Note The <site>_<peripheralsetname>_pguser is set on the PIM when the Peripheral Set is created. | Note | The <site>_<peripheralsetname>_pguser is set on the PIM when the Peripheral Set is created. |
| Note | The <site>_<peripheralsetname>_pguser is set on the PIM when the Peripheral Set is created. |
| Step 4 | Enter a password of your choice, using only ASCII characters . Note To change the JTAPI password on the CUCM configuration page: Open the peripheral Gateway Setup in PG Machine. Edit the CUCM PG. Set the same password for the user as previously set in Step 4. | Note | To change the JTAPI password on the CUCM configuration page: Open the peripheral Gateway Setup in PG Machine. Edit the CUCM PG. Set the same password for the user as previously set in Step 4. |
| Note | To change the JTAPI password on the CUCM configuration page: Open the peripheral Gateway Setup in PG Machine. Edit the CUCM PG. Set the same password for the user as previously set in Step 4. |
| Step 5 | Add the application user to the Standard CTI Enabled Group and Role: Click Add to Access Control Group . Select the Standard CTI Enabled group. Select the Standard CTI
                                                   				Allow Control of Phones supporting Connected Xfer and conf group. Select the Standard CTI
                                                   				Allow Control of Phones supporting Rollover Mode group. Click Add Selected . Click Save . |
| Step 6 | Associate the
                                          			 CTI route points and the phones with the application user. |
| Step 7 | Click Save . |

| Note | The <site>_<peripheralsetname>_pguser is set on the PIM when the Peripheral Set is created. |
|---|---|

| Note | To change the JTAPI password on the CUCM configuration page: Open the peripheral Gateway Setup in PG Machine. Edit the CUCM PG. Set the same password for the user as previously set in Step 4. |
|---|---|

| Step 1 | Click the System . |
|---|---|
| Step 2 | Select Service Parameters . |
| Step 3 | Select a Server. |
| Step 4 | Select the service as Cisco Call Manager(Active) . |
| Step 5 | Under Clusterwide Parameters (system-location and region), ensure the following: G.711 A-law Codec Enabled is Enabled . G7.11 mu-law Codec Enabled to Disabled . |
| Step 6 | Click Save . |

| Step 1 | Log in to the Cisco Unified Serviceability (https://hostname of primary server :8443 /ccmservice) using administrator credentials. |
|---|---|
| Step 2 | Select SNMP > V1/V2c > Community
                                                				  String . |
| Step 3 | From Server drop-down list, select the server for
                                          			 which you want to configure a community string and click Find . |
| Step 4 | Click Add
                                             				New to add new community string. Enter Community String . Example: public. In Host IP Addresses Information field, choose Accept SNMP Packets from any host . From Access Privilages drop-down list, select ReadWriteNotify option. Check Apply to All Nodes check box to apply community
                                                				  string to all nodes in the cluster. Information message will be displayed. Click OK . Click Save . A message is displayed, that indicates that changes will not take effect until you restart the SNMP primary agent. To continue
                                                the configuration without restarting the SNMP primary agent, click Cancel . To restart the SNMP primary agent service, click OK . Click OK . |
| Step 5 | Select SNMP > V1/V2c > Notification
                                                				  Destination . |
| Step 6 | From Server drop-down list, select the server for
                                          			 which you want to configure a notification destination and click Find . |
| Step 7 | Click Add
                                             				New button to add new notification destination. From Host IP Addresses drop-down list, select Add New . In Host IP Address field, enter the Prime
                                                				  Collaboration server IP address . In the Port Number field, enter the notification receiving
                                                				  port number. Note Default
                                                            					 port number is 162. In SNMP Version Information field, select the SNMP
                                                				  Version V2C. In Notification Type Information field; from Notification Type drop-down list, select Trap . In Community String Information field; from Community String drop-down list, select Community
                                                				  String created in Step 4 from the drop-down list. Check the Apply to All Nodes check box to apply community
                                                				  string to all nodes. Information message will be displayed. Click OK . Click Insert . A message is displayed, that indicates that changes will not take effect until you restart the SNMP primary agent. To continue
                                                the configuration without restarting the SNMP primary agent, click Cancel . To restart the SNMP primary agent service, click OK . Click OK . | Note | Default
                                                            					 port number is 162. |
| Note | Default
                                                            					 port number is 162. |

| Note | Default
                                                            					 port number is 162. |
|---|---|

| Step 1 | From the AW server, open Configuration Manager, choose Configure ICM > Enterprise > Agent Desk Settings > Agent Desk Settings List . The Agent Desk Settings List dialog box opens. |
|---|---|
| Step 2 | Click Retrieve and then Click Add . |
| Step 3 | Fill in the
                                          			 Attributes tab information: Name . Enter a
                                             				name for the agent desk settings that is unique within the enterprise. Ring No Answer
                                                				  Time . Enter the number of seconds (between 1 and 120) that a call
                                             				may ring at the agent's station. If you are deploying the Unified CVP, make
                                             				sure this number is less than the number set for the No Answer Timeout for
                                             				Router Requery that you set in the Unified CVP. If you configure
                                             				this timer, you do not need to configure the Unified Communications Manager
                                             				Call Forward on No Answer for agent extensions in the Unified Communications
                                             				Manager, unless you want them to be used when the agent is not logged in. If
                                             				you set the Unified Communications Manager Call Forward No Answer time, enter a
                                             				value at least 3 seconds higher than the Ring No Answer Time on each Unified
                                             				Communications Manager node. Ring no answer dialed
                                                				  number . Enter the Unified CCE DN associated with the routing script
                                             				that you want to use to reroute a call that an agent has not answered. If you
                                             				are deploying the Unified CVP, leave this field blank. Logout non-activity
                                                				  Time . Enter the number of seconds (between 10 and 7200) in which
                                             				the agent can remain in Not Ready state before Unified CCE automatically logs
                                             				out the agent. Work Mode on
                                                				  Incoming . Select whether wrap-up is required following an incoming
                                             				call. Select an option from the drop-down list. Work Mode on
                                                				  Outgoing . Select whether wrap-up is required following an outgoing
                                             				call. Select an option from the drop-down list. Wrap Up Time . Enter the amount of time, in seconds, allocated to an agent to wrap up a call. Assist Call
                                                				  Method . Select whether Unified CCE creates a consultative call or a
                                             				blind conference call for a supervisor assistance request. Emergency Alert
                                                				  Method . Select whether the Unified CCE creates a consultative call
                                             				or a blind conference call for an emergency call request. Blind
                                             				conference is not supported if the call may queue on a VRU. Description .
                                             				Enter additional optional information about the agent desk settings. |
| Step 4 | Use the
                                          			 following boxes to select or de-select miscellaneous settings: Auto-answer .
                                             				Indicates whether calls to the agent are automatically answered. The agent is
                                             				not required to take any action to answer the call. If a second call comes in
                                             				while a call is in progress, the call is not automatically answered. This is
                                             				the same behavior as with Unified Communications Manager. If you enable
                                             				auto-answer, you must also configure the agent phone in Unified Communications
                                             				Manager to turn the speakerphone or headset (or both) to ON. If you turn only the
                                             				headset to ON, the agent must also turn the phone headset button to ON. In a multi-line
                                             				enabled environment with auto-answer selected, if you are on a call on your
                                             				non-ACD line, the call will not auto-answer. However, if you turn on Unified Communications Manager Auto
                                             				Answer, the call will answer. Idle Reason
                                                				  Required . Indicates whether an agent is required to enter a reason
                                             				before entering the Idle state. Logout Reason
                                                				  Required . Indicates whether an agent is required to enter a reason
                                             				before logging out. Auto Record on
                                                				  Emergency . Indicates in a record request is automatically sent when
                                             				an emergency call request starts. Cisco Unified Mobile
                                                				  Agent (check box). Enables the Unified Mobile Agent feature so that
                                             				the agent can log in remotely and take calls from any phone. For more
                                             				information about the Unified Mobile Agent, see the Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/en/US/products/sw/custcosw/ps1844/products_feature_guides_list.html . |
| Step 5 | Click Save and then click Close . Note For any change, you perform in the Agent Desk Settings to take effect, log out and then log in to the Finesse Agent Desktop. | Note | For any change, you perform in the Agent Desk Settings to take effect, log out and then log in to the Finesse Agent Desktop. |
| Note | For any change, you perform in the Agent Desk Settings to take effect, log out and then log in to the Finesse Agent Desktop. |

| Note | For any change, you perform in the Agent Desk Settings to take effect, log out and then log in to the Finesse Agent Desktop. |
|---|---|

| Sequence | Task |
|---|---|
| 2 | Configure Unified Intelligence Center Data Sources for External HDS |
| 3 | Download Report Bundles |
| 4 | Import Reports |
| 5 | Configure Unified Intelligence Center Administration |

| Sequence | Task |
|---|---|
| 1 | Navigate to Infrastructure Settings > Device Configuration > Finesse to configure, and then select the Site and Peripheral Set of the Finesse server. Configure Contact Center Enterprise Administration and Data Server Settings Configure Contact Center Enterprise CTI Server Settings |
| 2 | Configure Contact Center Agents and Routing for Live Data Reports |
| 3 | Restart the Cisco Tomcat Service |
| 4 | Live Data Reports |
| 5 | Configure SNMP |

| Step 1 | Enter utils
                                             				service stop Cisco Tomcat command, to stop the Cisco Tomcat service. |
|---|---|
| Step 2 | Enter utils
                                             				service start Cisco Tomcat command, to start the Cisco Tomcat service. |

| Note | This procedure
                                                			 applies only if you are using HTTPS. This procedure
                                                			 is optional. If you are using HTTPS, you can choose to obtain and upload a CA
                                                			 certificate or you can choose to use the self-signed certificate provided with
                                                			 Cisco Finesse. |
|---|---|

| Step 1 | Generate a CSR
                                             			 as follows. Select Security > Certificate Management > Generate
                                                      					 CSR . From the
                                                   				  certificate name drop-down list, select tomcat . Click Generate CSR . |
|---|---|
| Step 2 | Download the
                                             			 CSR. Select Security > Certificate Management > Download
                                                      					 CSR . From the
                                                   				  certificate name drop-down list, select tomcat . Click Download CSR . |
| Step 3 | Use the CSR to
                                             			 obtain the signed application certificate and the CA root certificate from the
                                             			 Certificate Authority. |
| Step 4 | When you
                                             			 receive the certificates, select Security > Certificate Management > Upload
                                                				Certificate . |
| Step 5 | Upload the
                                             			 root certificate. Choose tomcat-trust from Certificate Name drop-down list. Click Browse and open the root certificate file, in Upload File field. Click Upload File . |
| Step 6 | Upload the
                                             			 application certificate. Choose tomcat from Certificate Name drop-down list. Enter the
                                                   				  name of the CA root certificate in the Root Certificate field. Click Browse and open the root certificate file, in Upload File field. Click Upload File . |
| Step 7 | After the
                                             			 upload is complete, sign out from Cisco Finesse. |
| Step 8 | Access the CLI
                                             			 on the primary Cisco Finesse server. |
| Step 9 | Enter utils
                                                				service restart Cisco Finesse Notification Service command to
                                             			 restart the Cisco Finesse Notification service. |
| Step 10 | Enter utils
                                                				service restart Cisco Tomcat command to restart the Cisco Tomcat
                                             			 service. |
| Step 11 | Upload the
                                             			 root certificate and application certificate to the secondary Cisco Finesse
                                             			 server. Note Enter the following URL in browser: https://FQDN of secondary Finesse server:8433/cmplatform , to open Cisco Unified Operating System Administration for the secondary server. | Note | Enter the following URL in browser: https://FQDN of secondary Finesse server:8433/cmplatform , to open Cisco Unified Operating System Administration for the secondary server. |
| Note | Enter the following URL in browser: https://FQDN of secondary Finesse server:8433/cmplatform , to open Cisco Unified Operating System Administration for the secondary server. |
| Step 12 | Access the CLI
                                             			 on the secondary Cisco Finesse server and restart the Cisco Finesse
                                             			 Notification Service and the Cisco Tomcat Service. |

| Note | Enter the following URL in browser: https://FQDN of secondary Finesse server:8433/cmplatform , to open Cisco Unified Operating System Administration for the secondary server. |
|---|---|

| Step 1 | On the Windows
                                          			 domain controller, run the CLI command certutil -ca.cert ca_name .cer, in which ca_name is the name of your certificate. |
|---|---|
| Step 2 | Save the file.
                                          			 Note where you saved the file so you can retrieve it later. |

| Note | To avoid
                                             			 certificate warnings, each user must use the fully-qualified domain name (FQDN)
                                             			 of the Finesse server to access the desktop. |
|---|---|

| Step 1 | From the
                                          			 Firefox browser menu, select Options . |
|---|---|
| Step 2 | Click Advanced . |
| Step 3 | Click the Certificates tab. |
| Step 4 | Click View
                                             				Certificates . |
| Step 5 | Click Authorities . |
| Step 6 | Click Import and browse to the ca_name .cer file (in which ca_name is the name of your certificate). |
| Step 7 | Check the Validate Identical Certificates check box. |
| Step 8 | Restart the browser for certificate installation to take effect. |

| Note | To avoid
                                             			 certificate warnings, each user must use the fully-qualified domain name (FQDN)
                                             			 of the Finesse server to access the desktop. |
|---|---|

| Step 1 | On the Windows
                                          			 domain controller, navigate to Administrative
                                                				  Tools > Group Policy Management . Note Users who have strict Group Policy defined on the Finesse Agent Desktop are required to disable Cross Document Messaging from Group Policy Management to ensure proper functioning of Finesse on browser . | Note | Users who have strict Group Policy defined on the Finesse Agent Desktop are required to disable Cross Document Messaging from Group Policy Management to ensure proper functioning of Finesse on browser . |
|---|---|---|---|
| Note | Users who have strict Group Policy defined on the Finesse Agent Desktop are required to disable Cross Document Messaging from Group Policy Management to ensure proper functioning of Finesse on browser . |
| Step 2 | Right-click
                                          			 Default Domain Policy and select Edit . |
| Step 3 | In the Group
                                          			 Policy Management Console, go to Computer
                                                				  Configuration > Policies > Window
                                                				  Settings > Security Settings > Public Key
                                                				  Policies . |
| Step 4 | Right-click
                                          			 Trusted Root Certification Authorities and select Import . |
| Step 5 | Import the ca_name .cer file. |
| Step 6 | Go to Computer
                                                				  Configuration > Policies > Windows
                                                				  Settings > Security Settings > Public Key
                                                				  Policies > Certificate Services Client -
                                                				  Auto-Enrollment . |
| Step 7 | From the
                                          			 Configuration Model list, select Enabled . |
| Step 8 | Sign in as a user on a computer that is part of the domain and open browser . |
| Step 9 | If the user
                                          			 does not have the certificate, run the command gpupdate.exe /target:computer /force on the user's
                                          			 computer. |

| Note | Users who have strict Group Policy defined on the Finesse Agent Desktop are required to disable Cross Document Messaging from Group Policy Management to ensure proper functioning of Finesse on browser . |
|---|---|

| Step 1 | In the browser, go to Settings . |
|---|---|
| Step 2 | In the Chrome browser, select Advanced Settings > Privacy and Security , click Manage
                                             Certificates . |
| Step 3 | In the
                                          Microsoft Edge browser, select Privacy, search,
                                             and services . Under Security , click Manage Certificates . |
| Step 4 | Click Trusted Root Certification Authorities tab. |
| Step 5 | Click Import and browse to the ca_name .cer file. In the Trusted Root Certification Authorities tab, ensure that the new certificate appears in the
                                          list. |
| Step 6 | Restart the browser for the certificate to install. |

| Note | Ensure that the Permanently store this exception box is checked. |
|---|---|

| Note | If you click the certificate link and don’t accept it, the certificate link stays enabled in the SSL Certificate Not Accepted dialog box. The certificate error appears every time you sign in. The procedure to permanently accept the certificate is
                                                   as follows. |
|---|---|

| Note | If the .crt file option isn’t available, select the .der option to save the certificate. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Configure Live Data with AW |
| 2 | Configure Live Data Machine Services |
| 3 | Configure Live Data for Unified Intelligence Center Data Sources |
| 4 | Configure Cross Origin Resource Sharing (CORS) for Live Data |
| 5 | Restart Live Data |
| 6 | Set Up Certificates for Live Data |
| 7 | Configure SNMP |

| Note | You do not need to configure the AW DB on both the Publisher and the Subscriber.  The configuration is replicated between
                                             the Publisher and Subscriber. |
|---|---|

| Step 1 | Log in to your
                                          			 Live Data server. |
|---|---|
| Step 2 | Run the
                                          			 following command to configure Live Data with the primary AW DB. The command
                                          			 automatically tests the connection from Live Data, checks the user permission,
                                          			 and displays results. The skip-test parameter is optional. Include it only if you do not want to perform the test. set live-data aw-access primary addr port db user pwd [skip-test] |
| Step 3 | Run the
                                          			 following command to configure Live Data with the secondary AW DB. The command
                                          			 automatically tests the connection from Live Data, checks the user permission,
                                          			 and displays results. The skip-test parameter is optional. Include it only if you do not want to perform the test. set live-data aw-access secondary addr port db user pwd [skip-test] You can also optionally run the following command at
                                          			 any time to show and test the AW configuration that you set from Live Data to
                                          			 the primary and secondary AW DBs. The skip-test parameter is optional. Include it only if you do not want to perform the test. show live-data aw-access [skip-test] |

| Step 1 | Launch Microsoft SQL Server Management Studio  on the Unified CCE Administration Client workstation . |
|---|---|
| Step 2 | Navigate to Security > Logins , right-click Logins and select New
                                             				Logins . Use these steps to create login accounts for the Cisco Unified Intelligence Center reporting data sources and for Finesse connectivity to the AW Database on the Cisco Finesse Administration page. |
| Step 3 | On the General
                                          			 Screen: Enter the
                                                				  Login Name. Select SQL Server authentication . Enter and
                                                				  confirm the password. Uncheck Enforce password policy . |
| Step 4 | In the Server Roles page, check the following check boxes: public securityadmin serveradmin setupadmin sysadmin |
| Step 5 | On the User
                                          			 Mapping page, do the following: Check the Real-time database and Historical database check boxes. In Database role memberships pane, check the following check boxes: db_datareader db_datawriter db_ddladmin db_owner db_securityadmin public Note For an SQL user configured to work with Live Data, check the master database check box and the db_datareader and db_datawriter
                                                            check boxes (in Database role memberships pane). | Note | For an SQL user configured to work with Live Data, check the master database check box and the db_datareader and db_datawriter
                                                            check boxes (in Database role memberships pane). |
| Note | For an SQL user configured to work with Live Data, check the master database check box and the db_datareader and db_datawriter
                                                            check boxes (in Database role memberships pane). |
| Step 6 | Click OK . |

| Note | For an SQL user configured to work with Live Data, check the master database check box and the db_datareader and db_datawriter
                                                            check boxes (in Database role memberships pane). |
|---|---|

| Note | Ensure that you configure SQL User Account on both the primary and secondary AW databases. |
|---|---|

| Note | Whenever you run set live-data machine-services , be sure to also run set live-data cuic-datasource to reconfigure the Live Data data sources for the Unified Intelligence Center. See Configure Live Data for Unified Intelligence Center Data Sources . If you are using any certificates that are unapproved by Cisco or self-signed certificate, ensure to import the AWDB certificate
                                                   into the Live Data server before you run set live-data machine-services . |
|---|---|

| Step 1 | Log in to your
                                          			 Live Data server. |
|---|---|
| Step 2 | Run the
                                          			 following command to configure the Live Data machine services: set live-data machine-services awdb-user awdb-pwd Use the user@domain format to specify the AW database domain user with write-access permission. The domain is a fully qualified domain name (FQDN),
                                             and the username is a user principal name. You must be authorized to change Unified CCE configuration. Note The Router and Peripheral Gateway (PG) TIP and TOS connection information is automatically populated for Unified CCE deployments
                                                               that support Live Data. Cisco Unified Communications Manager (CUCM) PG is supported for Live Data. Note Once you have updated the host name of Live Data Server, you need to re-run the below set of commands, otherwise new host
                                                         name will not be accepted. set live-data machine-services awdb-user awdb-pwd set live-data cuic-datasource cuic-addr cuic-port cuic-user cuic-pwd Verify that the show machine-services display changed hostname. It is necessary for you to re-run the set of commands, otherwise Live data machine services will not be updated with the
                                                         new host name. | Note | The Router and Peripheral Gateway (PG) TIP and TOS connection information is automatically populated for Unified CCE deployments
                                                               that support Live Data. Cisco Unified Communications Manager (CUCM) PG is supported for Live Data. | Note | Once you have updated the host name of Live Data Server, you need to re-run the below set of commands, otherwise new host
                                                         name will not be accepted. set live-data machine-services awdb-user awdb-pwd set live-data cuic-datasource cuic-addr cuic-port cuic-user cuic-pwd Verify that the show machine-services display changed hostname. It is necessary for you to re-run the set of commands, otherwise Live data machine services will not be updated with the
                                                         new host name. |
| Note | The Router and Peripheral Gateway (PG) TIP and TOS connection information is automatically populated for Unified CCE deployments
                                                               that support Live Data. Cisco Unified Communications Manager (CUCM) PG is supported for Live Data. |
| Note | Once you have updated the host name of Live Data Server, you need to re-run the below set of commands, otherwise new host
                                                         name will not be accepted. set live-data machine-services awdb-user awdb-pwd set live-data cuic-datasource cuic-addr cuic-port cuic-user cuic-pwd Verify that the show machine-services display changed hostname. It is necessary for you to re-run the set of commands, otherwise Live data machine services will not be updated with the
                                                         new host name. |

| Note | The Router and Peripheral Gateway (PG) TIP and TOS connection information is automatically populated for Unified CCE deployments
                                                               that support Live Data. Cisco Unified Communications Manager (CUCM) PG is supported for Live Data. |
|---|---|

| Note | Once you have updated the host name of Live Data Server, you need to re-run the below set of commands, otherwise new host
                                                         name will not be accepted. set live-data machine-services awdb-user awdb-pwd set live-data cuic-datasource cuic-addr cuic-port cuic-user cuic-pwd Verify that the show machine-services display changed hostname. It is necessary for you to re-run the set of commands, otherwise Live data machine services will not be updated with the
                                                         new host name. |
|---|---|

| Note | If you are using any certificates that are unapproved by Cisco, ensure to import the CUIC certificate into the Live Data server
                                             before you run set live-data machine-services . |
|---|---|

| Step 1 | Log in to your
                                          			 Live Data server. |
|---|---|
| Step 2 | Run the
                                          			 following command to configure your Live Data Unified Intelligence Center data
                                          			 sources: set live-data cuic-datasource cuic-addr cuic-port cuic-user cuic-pwd |

| Access the Live Data CLI and run the following command: utils system restart Note Whenever a new peripheral gateway that supports Live Data gets deployed and started, its feed will not be available to Live
                                                         Data server automatically. Restart the Live Data server to start the feed from the newly deployed Peripheral Gateway. | Note | Whenever a new peripheral gateway that supports Live Data gets deployed and started, its feed will not be available to Live
                                                         Data server automatically. Restart the Live Data server to start the feed from the newly deployed Peripheral Gateway. |
|---|---|---|
| Note | Whenever a new peripheral gateway that supports Live Data gets deployed and started, its feed will not be available to Live
                                                         Data server automatically. Restart the Live Data server to start the feed from the newly deployed Peripheral Gateway. |

| Note | Whenever a new peripheral gateway that supports Live Data gets deployed and started, its feed will not be available to Live
                                                         Data server automatically. Restart the Live Data server to start the feed from the newly deployed Peripheral Gateway. |
|---|---|

| Note | When using self-signed certificates, agents must accept the Live Data certificates in the Finesse desktop when they sign in
                                                before they can use the Live Data gadget. |
|---|---|

| Step 1 | Log in to the Cisco Unified Serviceability (https://hostname of primary server :8443 /ccmservice) using administrator credentials. |
|---|---|
| Step 2 | Select SNMP > V1/V2c > Community
                                                				  String . |
| Step 3 | From Server drop-down list, select the server for
                                          			 which you want to configure a community string and click Find . |
| Step 4 | Click Add
                                             				New to add new community string. Enter Community String . Example: public. In Host IP Addresses Information field, choose Accept SNMP Packets from any host . From Access Privilages drop-down list, select ReadWriteNotify option. Check Apply to All Nodes check box to apply community
                                                				  string to all nodes in the cluster. Information message will be displayed. Click OK . Click Save . A message is displayed, that indicates that changes will not take effect until you restart the SNMP primary agent. To continue
                                                the configuration without restarting the SNMP primary agent, click Cancel . To restart the SNMP primary agent service, click OK . Click OK . |
| Step 5 | Select SNMP > V1/V2c > Notification
                                                				  Destination . |
| Step 6 | From Server drop-down list, select the server for
                                          			 which you want to configure a notification destination and click Find . |
| Step 7 | Click Add
                                             				New button to add new notification destination. From Host IP Addresses drop-down list, select Add New . In Host IP Address field, enter the Prime
                                                				  Collaboration server IP address . In the Port Number field, enter the notification receiving
                                                				  port number. Note Default
                                                            					 port number is 162. In SNMP Version Information field, select the SNMP
                                                				  Version V2C. In Notification Type Information field; from Notification Type drop-down list, select Trap . In Community String Information field; from Community String drop-down list, select Community
                                                				  String created in Step 4 from the drop-down list. Check the Apply to All Nodes check box to apply community
                                                				  string to all nodes. Information message will be displayed. Click OK . Click Insert . A message is displayed, that indicates that changes will not take effect until you restart the SNMP primary agent. To continue
                                                the configuration without restarting the SNMP primary agent, click Cancel . To restart the SNMP primary agent service, click OK . Click OK . | Note | Default
                                                            					 port number is 162. |
| Note | Default
                                                            					 port number is 162. |

| Note | Default
                                                            					 port number is 162. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Generate CSR and upload CA Certificates Or Generate and import Self-signed Certificates |
| 2 | Configure CCE Component |
| 3 | Configure Cisco Unified Customer Voice Portal |
| 4 | If Media Server is external, Configure Media Server |
| 5 | Configure Cisco Unified Communications Manager |
| 6 | Configure Cisco Unified Intelligence Center |
| 7 | Configure Cisco Finesse |
| 8 | Configure Live Data |
| 9 | Configure Cisco Identity Service |
| 10 | Configure Cisco Unified Customer Voice Portal Reporting Server (optional) |
| 11 | Configure VVB (optional) |
| 12 | Configure Cisco IOS Enterprise Voice Gateway |
| 13 | Configure IPv6 |
| 14 | Configure Enterprise Chat and Email (ECE) (optional) Email and Chat |

| Sequence | Task |
|---|---|
| 1 | Configure SQL Server for CCE Components |
| 2 | Set up Organizational Units |
| 3 | Configure Logger |
| 4 | Configure Router |
| 5 | Configure AW-HDS |
| 6 | Configure HDS-DDS |
| 7 | Start Unified CCE Services |
| 8 | If you have PG VMs installed , Add Unified CCE Instance on all PG VMs |
| 9 | Configure Packaged CCE Deployment Type |
| 10 | Configure Cisco Unified Contact Center Enterprise PG |
| 11 | For configuration using Configuration Manager, see Packaged CCE 4000 and 12000 Agent Supported Tools |

| Sequence | Task |
|---|---|
| 1 | Add Unified CCE Instance |
| 2 | Create Logger Database |
| 3 | To use Outbound Option, see Create Outbound Option Database |
| 4 | Add Logger Component to Instance |
| 5 | Cisco SNMP Setup (optional) |

| Sequence | Task |
|---|---|
| 1 | Add Unified CCE Instance |
| 2 | Add Router Component to Instance |
| 3 | Cisco SNMP Setup (optional) |

| Sequence | Task |
|---|---|
| 1 | Configure SQL Server for CCE Components |
| 2 | Add Unified CCE Instance |
| 3 | Create HDS Database |
| 4 | Add Administration and Data Server Component to Instance |
| 5 | Cisco SNMP Setup (optional) |

| Sequence | Task |
|---|---|
| 1 | Configure SQL Server for CCE Components |
| 2 | Add Unified CCE Instance |
| 3 | Create HDS Database |
| 4 | Add Administration and Data Server Component to Instance |
| 5 | Configure ICM Database Lookup (optional) |
| 6 | Cisco SNMP Setup (optional) |

| Step 1 | Launch the Unified CCE Web Setup tool. |
|---|---|
| Step 2 | In the Router Options window, select Enable Database Routing . |
| Step 3 | Configure Database Lookup explorer: Click Start > All programs > Cisco Unified CCE Tools > Administration Tools > Configuration Manager . Open Tools > Explorer Tools > Database Lookup Explorer. Configure Script Table and Script Table Column as shown in the following example: Script Table: Name: AccountInfo Side A: \\dblookup1\DBLookup.AccountInfo Side B: <Update Side B of database here> Description: <Provide description here> dblookup1 is external database server name, DBLookup is external database name, and AccountInfo is the table name. Script Table Column: Column name: AccountNo Description: <Provide description here> |
| Step 4 | Use the CCEDataProtect Tool to configure the registry settings in Unified CCE . For more information, see Configure External DBLookUp Registry Value using CCEDataProtect Tool |
| Step 5 | Create the ICM script with the database lookup node with the respective table and lookup value. The following figure shows AccountInfo as the table name and Call.CallingLineID as the lookup value. Figure 3. Example ICM Database Look Up |

| Note | In the System Inventory, the status rules that apply to machines outside of the Packaged Contact Center Enterprise Simplex
                                                   Lab Only deployment returns a blocked status. Status rules which require ESXi host return a blocked status. |
|---|---|

| Note | You can add MediaSense only for the main site. |
|---|---|

| Note | Adding a Cisco Unified Customer Voice Portal Reporting Server with Inventory CSV is not supported. You can also add it as
                                                   an external server after a successful initialization of inventory. |
|---|---|

| Note | You can add the SocialMiner as an external machine only in the main site. |
|---|---|

| Note | In Lab Mode,
                                             		  Packaged CCE does not validate the ESXi host. |
|---|---|

| Note | Status rules
                                                			 which require ESXi host returns a status of blocked. |
|---|---|

| Note | SocialMiner can be added as an external machine only in the main site. |
|---|---|

| Note | Once a Packaged CCE deployment is initialized, you cannot switch to another Packaged CCE deployment type, including Packaged
                                             Lab Mode. However, you can switch to a Unified CCE deployment type. |
|---|---|

| Step 1 | On the Inventory page, select Packaged CCE: Lab Mode from the Deployment Type drop-down list, then select an instance from the Instance drop-down list that has been created using Domain Manager. Click Next . |
|---|---|
| Step 2 | Select one of the following options from the Template drop-down list: Simplex Inventory for Simplex Lab Mode deployment Duplex Inventory for Duplex Lab Mode deployment Click Download to download the Inventory Content File Template. Fill out and save the template to your computer. In the required Content File field, browse to the content file you have completed. The content file is validated before the inventory is created. Click Next . For more information on completing the Inventory Content File Template, see Inventory Content File . |
| Step 3 | On the Settings page do the following: Select the codec used for Mobile Agent calls from the Mobile Agent Codec drop-down list. The Side A Connection and Side B Connection drop-down lists are
                                                   					 disabled in Lab Only deployment. For the Automatically create service accounts check box, either: Leave the check box checked if you want automated initialization to create the service accounts in Active Directory. These accounts will be created and added to the Service group. Uncheck the check box if you want to use an existing Active Directory account. Enter the username and password for an existing
                                                         Active Directory user in the same domain as the Packaged CCE servers. This
                                                         						  account will be added to the Service group. Click Next . The
                                          			 deployment is initialized. The Details dialog box displays the status of the
                                          			 automated initialization tasks. |
| Step 4 | After the automated initialization tasks complete, click Done . If one of the automated initialization tasks fails, correct the errors and then click Retry . If the retry is successful, the automated initialization continues. For some task failures, all completed tasks must be reverted before the task can be retried. You see a message informing you
                                             that the system needs to be reverted to a clean state. Click OK , and then after the system is in a clean state, click Start Over . Note You should restart the Unified CVP Server. After you initiate Simplex or Duplex Lab Mode deployment, you can also add the following external machines for the main site
                                             on the Inventory page: Unified CM Publisher Unified CVP Reporting Server Contact Center SIP Proxy Virtualized Voice Browser Gateway SocialMiner MediaSense Enterprise Chat and Email Third-party Multichannel Media Server Cloud Connect Publisher To add, edit or delete the external machines on the main site, see System Inventory for Packaged CCE 2000 Agents Deployment . | Note | You should restart the Unified CVP Server. |
| Note | You should restart the Unified CVP Server. |

| Note | You should restart the Unified CVP Server. |
|---|---|

| Note | In Lab only duplex deployments, the Live Data datasource is created only on the publisher node. |
|---|---|

| Step 1 | In the Unified CCE Web Administration click the Bulk Import card on the Overview page . Download the Inventory content file template. |
|---|---|
| Step 2 | Open the file in Microsoft Excel and populate the content file fields as described in the Inventory Content file. |
| Step 3 | Save your changes. |
| Step 4 | Create a new bulk job in Bulk Jobs . In the Content File field, select the inventory content file you created and click Save . |

| Note | If a username and/or password contains the "=" or "&" characters, use the encoded value of "%3D" or "%26" respectively. |
|---|---|

| Field | Description |
|---|---|
| operation | The
                                                						default is CREATE; do not change the operation. |
| name | Do not
                                                						change the machine name. Note This
                                                            						  field applies only to duplex mode. | Note | This
                                                            						  field applies only to duplex mode. |
| Note | This
                                                            						  field applies only to duplex mode. |
| machineType | Do not
                                                						change the machine type. |
| publicAddress | Enter the public IP address or hostname for each machine. |
| publicAddressServices | CCE_ROGGER - Do not change this field. CCE_PG - This field specifies services that are
                                                						required for the Unified CCE PG. If the Logical Controller ID for the UCM PG is
                                                						not the default of 5000, change the pairing value for the TIP_PG and TIP_PG_TOS
                                                						services to match the Logical Controller ID. (The Logical Controller ID can be
                                                						found on the Peripheral Gateways tab of System > Information.) CCE_AW - This field specifies credentials for the Diagnostic Framework for Unified CCE. Replace user@domain.com and password with credentials
                                                of a domain user who is a member of the Config security group for the instance. The credentials must be valid on all Unified
                                                CCE machines in your deployment. Note Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. CVP - Unified CVP Server Windows credentials CM_PUBLISHER - This field specifies AXL credentials. Replace user and password with the correct credentials. CUIC_PUBLISHER - This field specifies the services
                                                						for Unified Intelligence Center. For the Administration credentials and Cisco
                                                						Identity Service credentials, replace user and password with the correct
                                                						credentials. For all other services, do not change the default values. FINESSE - This field specifies Finesse
                                                						Administration credentials. Replace user and password with the correct
                                                						credentials. | Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
| Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
| privateAddress | Enter the private IP address or hostname for the CCE_PG and CCE_ROGGER . Leave this field blank for all other machines. |
| side | Enter
                                                						sideA or sideB. |

| Note | This
                                                            						  field applies only to duplex mode. |
|---|---|

| Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
|---|---|