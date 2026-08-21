---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-configuration-guide-pcce-b-admi-3cbcde0194
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/configuration/guide/pcce_b_admin-and-config-guide-15_0_1/pcce_m_optional-configurations_15_0.html
retrieved_at: 2026-08-21T16:49:34.806014+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Optional Configurations

## Chapter: Optional Configurations

# Optional Configurations

## Optional Configuration for Packaged CCE 2000 Agents Deployment

To configure optional components for Packaged CCE 2000 Agents deployment.

Task

Add and Maintain Remote Sites for 2000 Agent Deployment

Add and Maintain External Machines

Add PIMs to the Media Routing Peripheral Gateway

Add Multichannel PIM to 2000 Agent Deployment

Configure Email and Chat

Configure Cisco Unified Customer Voice Portal Reporting Server

Configure VVB

### Add and Maintain Remote Sites for 2000 Agent Deployment

You can add new remote sites to the 2000 Agents deployment type. Each remote site added appears as a separate tab. Click the + icon to open the Add Remote Site pop-up window. See Add Remote Site for more information.

#### Add Remote Site

Step 1

Navigate to Unified CCE Administration > Infrastructure > Inventory .

Step 2

Click the + icon to
                                             			 open the Add
                                                				Remote Site page.

Step 3

On the CCE
                                                				PG screen, enter the remote site information in the following fields:

Enter a name for the site . Maximum length is ten characters. Valid characters are alphanumeric, period (.), and underscore (_). The first character
                                                         must be alphanumeric.

You cannot use the system reserved terms like core, main, and site.

Enter the
                                                         					 hostname, IP address, or fully qualified domain name (FQDN) for Side A.

Enter the
                                                         					 hostname, IP address, or fully qualified domain name (FQDN) for Side B.

Select the required peripheral gateway client types. The subsequent screens appear as per the selected options.

If you select Agent , the Unified CM and Finesse screens appear.

If you select VRU , the CVP screen appears.

If you select Multichannel , the Configure screen appears.

The system does not support IP address change. Use the hostname if you foresee a change in IP address. This is applicable
                                                            for all the Hostname/ IP Address fields.

Step 4

Click Next . The subsequent screens appear as per the
                                             			 selected PG client types.

Step 5

On the Unified CM page, you can either select an existing
                                             			 publisher or add a new one. If you select a publisher, the associated
                                             			 subscribers appear and you can select the subscriber details. To add a new
                                             			 publisher,

Select Add a new CM Publisher .

Enter the
                                                   				  Hostname, Username, and Password.

Click Save .

You can
                                                            				  add only one CM Publisher while creating a remote site.

Step 6

On the Subscribers section, select the following connection
                                             			 settings for the agent peripheral:

- Side A Connection

- Side B Connection

- Mobile Agent Codec

Step 7

Click Next .

Step 8

On the Finesse page, enter the Hostname, Username, and
                                             			 Password for the Finesse primary server.

Step 9

Click Next .

Step 10

On the CVP page, enter the Hostname/IP Address, Username, and Password of the Side A and Side B CVP Servers.

Step 11

Click Next .

Unified CCE PG

Agent

Downloads JTAPI from the Unified Communications Manager, and
                                                                  								  installs it on the Unified CCE PG.

Creates the CUCM Peripheral Gateway (PG) with the CUCM PIM.

Creates the CTI Server.

VRU - Creates the VRU
                                                            							 PG with two VRU PIMs.

Multichannel -
                                                            							 Creates the Multichannel PG.

Unified CCE Rogger

Updates the router configuration with the new PGs that are
                                                            							 created as a part of the site .

Unified Communications Manager

Creates the Application User that is used to configure the Agent
                                                                  								  PG.

Finesse

Configures the CTI Server settings.

Configures the connection to the AW database.

Unified Customer Voice Portal

Configures the Unified CVP Call Server components and adds them
                                                                  								  to the Main site Reporting Server.

Configures the Unified CVP VXML Server components.

Configures the Unified CVP Media Server components.

If one of
                                                            				  the automated initialization tasks fail, the system reverts all the completed
                                                            				  tasks.

Step 12

Click Done when all the tasks are complete. If there are
                                             			 configuration errors, you can click Back to edit the previous pages.

Step 13

For the
                                             			 configuration to take effect, do the following:

Restart
                                                      					 the router service.

If you have selected the PG client type as VRU, restart the two newly configured CVP Call Servers .

##### What to do next

For all remote sites configured with Agent PG, you must add the Finesse Self Signed Certificate (if the solution does not
                                                have the CA certificate) to the AW Machine. For more information on how to add Finesse certificate to AW Machine, see the Import VOS Components Certificate Import VOS Components Certificate

#### Reconfigure Remote Site

Step 1

Navigate to Unified CCE Administration > Infrastructure > Inventory .

Step 2

Click the site you want to reconfigure.

Step 3

Click Reconfigure to open the CCE
                                                				PG page.

You can only
                                                            				  add PG client types.

Step 4

Click Next and proceed the same way as you add a new remote site .

#### Delete Remote Site

You can delete a remote site if the following are not associated to the remote site :

Agents

Teams

Dialed Numbers

Skill groups

Routing Pattern

SIP Server Groups

Locations

Script

Dialer

Before deleting a remote site, you must stop all the services and processes running on the Cisco Finesse server of the remote
                                                site manually.

If remote sites has CVPs configured, make sure the following tasks are completed before deleting remote site:

Dissociate CVP Server from CVP Reporting Server.

If a site specific Reporting Server is used in Courtesy Call Back, replace the Reporting Server with another.

Delete all Media Server associations with CVP.

Post deletion of remote site, delete the Packaged CCE ID from the ORM.properties file.

Step 1

Navigate to Unified CCE Administration > Infrastructure > Inventory .

Step 2

Click the remote site you want to delete.

Step 3

Click Delete .

Step 4

Click Yes to confirm.

The delete operation does not remove the remote site objects permanently from the database. If you want to recreate a site
                                                            with same name, you must permanently delete these objects from Configuration Manager > Tools > Miscellaneous Tools > Deleted Objects .

### Add and Maintain External Machines

#### Add External Machines

You can add the following external machines based on PG types configured on :

Agent: None

VRU: Unified CVP Reporting Server, Virtualized Voice Browser, Gateways, Media Server, and Contact Center SIP Proxy

For detailed steps on how to add a Media Server as an external machine, see Add Media Server as External Machine

SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\

Multichannel: Third-Party Multichannel, ECE Data Server (refers to ECE Data Server VM for 400 agents and Services Server VM for ECE 1500 agents), ECE Web Server , and SocialMiner

If you are using any Multichannel applications ( SocialMiner , Enterprise Chat and Email, and Third-Party Multichannel), add them to the System Inventory external machines.

##### Before you begin

If you do not have a CA-signed certificate, import self-signed certificates for the external machines. For more information,
                                    see "Self-signed Certificates" section in Packaged CCE Administration and Configuration Guide .

Step 1

On the Inventory page, select the main site or the remote site tab and click the New button that appears on the top of the grid.

The Add Machine dialog box appears.

Step 2

Choose the machine type from the Type drop-down list.

Step 3

In the Host Name field, enter the hostname, IP address, or fully qualified domain name (FQDN) for the selected machine type.

The system attempts to convert the value you enter to FQDN.

The system does not support IP address change. Use the hostname if you foresee a change in IP address.

Step 4

In the machine's Administration section, enter the administration username and password for the selected machine type.

Step 5

Click Save .

Email and Chat:

In Configuration Manager Tool, application instance and application path are to be created and associated to CUCM PG.

LDAP configuration needs to be done using Single Sign-On (for Partition Administrators) in the ECE Administration Web interface.
                                                                        For more information, see Enterprise Chat and Email Administrator’s Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

Virtualized Voice Browser / Media Gateway: When you add VVB, the system will mark the machine as Out of Sync. Either wait for auto synchronization (which happens every
                                                                  10 mins) or do manual synchronization.

SocialMiner : If you add SocialMiner , the system automatically creates a SocialMiner Task feed for Task Routing, including the associated campaign and Connection to CCE notification.

#### Add Media Server as External Machine

Step 1

In Unified CCE Administration, select Infrastructure Settings > Inventory .

Step 2

Select the main site or the remote site and click the New button that appears on top of the grid.

Step 3

In the Add Machine dialog box, complete the following fields:

Type

From the drop-down list, choose "Media Server".

Host Name/IP Address

Enter the hostname, IP address, or fully qualified domain name (FQDN) for the selected machine type.

The system attempts to convert the value you enter to FQDN.

The system does not support IP address change. Use the hostname if you foresee a change in IP address.

FTP Section

FTP Enabled

Indicates whether a Media Server has FTP enabled.

A Media Server, which has FTP enabled, is automatically populated as a session variable to the VXMLServer. The (default) Agent
                                                            Greeting recording application automatically uses the Media Servers in the inventory that have FTP enabled for the recording.

If Microsoft FTP Service is not enabled in Windows Services Control Panel, then set it to Automatic and start the service.

Anonymous Access

Indicates that this Media Server uses anonymous FTP access. In this case, the user name is specified as anonymous by default.
                                                            The password field is not editable if you chose anonymous access.

Username and Password

These fields apply only if the FTP field is enabled and if the Anonymous Access field is disabled. In this case, enter the
                                                            username and password.

Port

Enter a new port number or use the default port number (21).

Step 4

Click Save .

When a Media Server is added, configurations are propagated to all CVPs across sites.

## Edit Machines

### Edit External Machines

On the Inventory page, select the main site or a remote site and click the required row on the grid. The machine details page appears for
                                    you to edit the following machines:

Machine

Editable Field

Unified CM Publisher

AXL Username and Password

SocialMiner

Administration Username and Password

Enterprise Chat and Email and 3rd Party Multichannel

Web Server: edit partition Administration User name and Password.

Data Server: none

Virtualized Voice Browser / Media Gateway

Administration Username and Password

A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports Customer Virtual Assistant feature.

To set a VVB as a Principal VVB, do the following:

Important

Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB.

Click the VVB row.

The VVB machine details page appears and you can modify the VVB details.

Check the Principal check box.

Select the required mode. This is the required parameter.

For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                               Gateway'.

Enter Administrator username and password.

Click Save .

Cisco Contact Center SIP Proxy

Administration Username and Password

Gateway

Administration Username and Password

Unified CVP Reporting

Windows Administration credentials

Cloud Connect

Administration Username and Password

When a Cloud Connect is updated, configurations are propagated to all CVPs and Finesse across sites.

Media Server

FTP Enabled, Anonymous Access, FTP Credentials, and Port

When a Media Server is updated, configurations are propagated to all CVPs and  across sites.

To delete an external machine on the main site or a remote site, click the x on the machine. Confirm the deletion.

You cannot delete the Virtualized Voice Browser and Cisco Contact Center SIP Proxy external machines if they are associated with a SIP Server Group. To delete these external machines, you must disassociate
                                                   them from the SIP Server Group.

You cannot delete the Gateway external machine if it is associated with Location. To delete this external machine, you must
                                                   disassociate the Gateway from the Location.

If you delete the Unified CM Publisher, the Unified CM Subscribers are also deleted automatically, and the Configure Deployment
                                                   pop-up window opens. Enter the name, IP address, AXL username, and AXL password for the Unified CM Publisher in your deployment.

When a Media Server is deleted, configurations are propogated to all CVPs across sites.

## Update IP Address or Hostname

On the Inventory page, System and Config Administrators can update the IP address or hostname of the following machines.

Core machines

Optional machines

IP address/hostname change or rebuild can only be done from Side A AW machine. The AW machine credentials are shared with
                                             all CCE machines. Ensure that the Side A AW user is part of the local Administrators group on all CCE machines.

If you have rebuilt a CCE_ROGGER or a CCE_AW, do not create a service account manually. Side A AW user account will be used
                                             as a service account for Logger and distributor services.

While updating the inventory for routers in Unified CCE Administration, at least one side of the router needs to be running
                                             successfully if both the sides were rebuilt. If not, you must manually add the router on one side through the web setup.

After updating the hostname in the virtual machine, regenerate and update CA or self-signed certificate on the machine. This
                                             should be done before updating the hostname in the inventory.

Task

Core Machines in Main Site

CCE_AW, CCE_ROGGER, CCE_PG, CVP, CM_PUBLISHER, CUIC_PUBLISHER (CUIC-LD-IDS coresident), CUIC_SUBSCRIBER, FINESSE, and VM_HOST

Update Core Machines

Core Machines in Remote Site

CCE_PG, CVP, CM_PUBLISHER 1 , CM_SUBSCRIBER, and FINESSE_PRIMARY

Optional Machines

Update Optional Machines

CVVB, CVP_REPORTING, MEDIA_SERVER, GATEWAY, EXTERNAL_HDS, CUSTOMER_COLLABORATION_PLATFORM, CCCSP , THIRD_PARTY_MULTICHANNEL, ECE, ECE_WEB_SERVER, CLOUD_CONNECT_PUB, and CLOUD_CONNECT_SUB

### Update Core Machines

In Main site: CCE_AW, CCE_ROGGER, CCE_PG, CVP, CM_PUBLISHER, CUIC_PUBLISHER (CUIC-LD-IDS co-resident), CUIC_SUBSCRIBER, FINESSE,
                                 and VM_HOST

In Remote site: CCE_PG, CVP, CM_PUBLISHER 2 , CM_SUBSCRIBER, and FINESSE_PRIMARY

After updating the IP address or hostname in the Inventory for CVP, restart the CVP device.

If you have changed the hostname of CCE_ROGGER in the virtual machine, restart the Apache Tomcat service on Side A AW. This
                                                   should be done before updating the inventory with new hostname for CCE_ROGGER.

References to VM_HOST in this topic apply only to VMware-based Packaged CCE 2000 Agents deployments before the 15.0(1) SU2/ES202607
                                                   ES is installed. References to VM_HOST remain in the CSV file even after the ES is applied; however, this field is no longer
                                                   validated.

#### Before you begin

Disable auto discovery in the virtual machine. For more information, see Auto Discovery .

Step 1

Navigate to the Unified CCE Administration > Infrastructure > Inventory .

Step 2

Choose Update > Core Machines .

Step 3

Click the Download Present Inventory File icon to get the Inventory File.

Step 4

Fill particulars in the Inventory File and save it. For more information, see Inventory Content File

Step 5

Click the Upload Updated Inventory File icon to import the updated file.

Step 6

Click Next to start the inventory update process and see the progress of tasks.

If the upload is successful, a green circle appears against each task.

If the upload is unsuccessful, fix the errors that are shown and repeat steps 5 and 6.

Step 7

Click Done .

### Update Optional Machines

CVVB, CVP_REPORTING, MEDIA_SERVER, GATEWAY, EXTERNAL_HDS, CUSTOMER_COLLABORATION_PLATFORM, CCCSP , THIRD_PARTY_MULTICHANNEL, ECE, ECE_WEB_SERVER, CLOUD_CONNECT_PUB, CLOUD_CONNECT_SUB and THIRD_PARTY_GATEWAY .

After updating the IP address or hostname in the inventory for CVP Reporting Server, restart this device.

#### Before you begin

Step 1

Navigate to the Unified CCE Administration > Infrastructure > Inventory .

Step 2

Choose Update > Optional Machines .

Step 3

Click the Download Present Inventory File icon to get the Inventory File.

Step 4

Fill particulars in the Inventory File and save it. For more information, see

Step 5

Click the Upload Updated Inventory File icon to import the updated file.

Step 6

Click Next to start the inventory update process and see the progress of tasks.

If the upload is successful, a green circle appears against each task.

If the upload is unsuccessful, fix the errors shown, and repeat steps 5 and 6.

Step 7

Click Done .

### Auto Discovery

During Technology Refresh upgrade, auto discovery is disabled by default till all the core components are updated.

After CCE 15.0(1) SU2/ES202607 or a later ES is installed, auto discovery is not supported for Packaged CCE 2000 Agents deployments
                                             on VMware-based or Nutanix-based deployments. Update the inventory manually by importing the Packaged CCE 2000 Agents inventory
                                             CSV file. For more details, see Step 3 (b) in Initialize the Packaged CCE 2000 Agents Deployment Type

Step 1

Navigate to the Unified CCE Administration > Infrastructure > Inventory .

Step 2

Choose Update > Auto Discovery .

Step 3

If Auto Discovery Status is Enabled, click Disable to disable auto discovery.

Step 4

If Auto Discovery Status is Disabled, click Enable to enable auto discovery.

If you don't enable auto discovery, it gets enabled automatically after three days of disabling.

Step 5

Click Done .

### Update IP Address or Hostname

On the Inventory page, System and Config Administrators can update the IP address or hostname of the following machines.

Core machines

Optional machines

IP address/hostname change or rebuild can only be done from Side A AW machine. The AW machine credentials are shared with
                                                all CCE machines. Ensure that the Side A AW user is part of the local Administrators group on all CCE machines.

If you have rebuilt a CCE_ROGGER or a CCE_AW, do not create a service account manually. Side A AW user account will be used
                                                as a service account for Logger and distributor services.

While updating the inventory for routers in Unified CCE Administration, at least one side of the router needs to be running
                                                successfully if both the sides were rebuilt. If not, you must manually add the router on one side through the web setup.

After updating the hostname in the virtual machine, regenerate and update CA or self-signed certificate on the machine. This
                                                should be done before updating the hostname in the inventory.

References to VM_HOST in this topic apply only to VMware-based Packaged CCE 2000 Agents deployments before the 15.0(1) SU2/ES202607
                                                ES is installed. References to VM_HOST remain in the CSV file even after the ES is applied; however, this field is no longer
                                                validated.

Task

Core Machines in Main Site

CCE_AW, CCE_ROGGER, CCE_PG, CVP, CM_PUBLISHER, CUIC_PUBLISHER (CUIC-LD-IDS coresident), CUIC_SUBSCRIBER, FINESSE, and VM_HOST

Update Core Machines

Core Machines in Remote Site

CCE_PG, CVP, CM_PUBLISHER 3 , CM_SUBSCRIBER, and FINESSE_PRIMARY

Optional Machines

Update Optional Machines

CVVB, CVP_REPORTING, MEDIA_SERVER, GATEWAY, EXTERNAL_HDS, CUSTOMER_COLLABORATION_PLATFORM, CCCSP , THIRD_PARTY_MULTICHANNEL, ECE, ECE_WEB_SERVER, CLOUD_CONNECT_PUB, and CLOUD_CONNECT_SUB

## Add PIMs to the
                        	 Media Routing Peripheral Gateway

The Media Routing
                           		Peripheral Gateway (MR PG) is created during automated initialization.

Creating PIMs for the MR PG is optional. You can create the following PIMs on the Media Routing Peripheral Gateway:

Outbound PIM

Multichannel PIM for SocialMiner

Multichannel PIM for Enterprise Chat and Email (ECE)

Multichannel PIM for a third-party multichannel application

Multichannel PIM for Digital Routing

To create Dialed
                           		Numbers associated with the Multichannel PIMs, first do the following:

Create the PIM using Peripheral Gateway Setup.

Add an external machine in the Solution Inventory using the Unified CCE Administration System. Navigate to Overview > Infrastructure > Inventory .

If ECE Data Server is deployed on box, you do not need to create a Dialed Number associated with the PIM.

Refer to the Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/en/US/products/ps12586/prod_maintenance_guides_list.html for directions on adding the Outbound PIM and the Multichannel PIMs.

Refer to the Enterprise Chat and Email Installation Guide (for Packaged Contact Center Enterprise) at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html .

### Add Multichannel PIM to 2000 Agent Deployment

Caution

Before performing the step to enable the secured connection between the components, ensure that the security certificate management
                                             process is completed.

Step 1

In the Peripheral Gateway Component Properties window, click Add .

Step 2

From the Client Type drop-down list, select Media Routing .

Step 3

From the Available PIMS list, select MR PIM1 , then click OK .

Step 4

In the Configuration dialog box, check the Enabled check box.

Step 5

In the Peripheral name field, enter the peripheral name.

Step 6

In the Peripheral ID field, enter the logical controller ID of the Unified CCE component you are adding. The following are the names by which
                                          the Unified CCE components are represented in the database. Refer Peripheral Gateway page in CCE Admin to get the peripheral ID of the corresponding PIM.

Name of Outbound is Outbound

Name of ECE is Multichannel

Name of CCP is Multichannel2

Name of THIRD_PARTY_MULTICHANNEL is MutliChannel3

Name of Digital Routing is DigitalRouting

#### Example:

Step 7

In the Application Hostname (1) field, enter the hostname or the IP address of the ECE services server.

Step 8

In the Application connection port (1) field, enter the port number.

Use the port number that is on the ECE services server that PIM uses to communicate with the application. The default port is 38001.

Step 9

In the Application Hostname (2) field, leave the field blank.

Step 10

In the Application connection port (2) field, leave the field blank.

Step 11

In the Heartbeat interval (sec) field, enter 5 .

Step 12

In the Reconnect interval (sec) field, enter 10 .

Step 13

Check the Enable Secured Connection option.

This establishes a secured connection between the MR PIM and the application server.

Ensure that you provide the correct information in the application hostname(1) and Application Connection Port(1) fields.

Step 14

Click OK .

## Configure Email and Chat

Step 1

Configure LDAP in the ECE Administration Web Interface.

For more information, see Single Sign-On (for Partition Administrators) in the Enterprise Chat and Email Administrator’s Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html .

Step 2

Accept the certificate in the Unified CCE Administration . Do the following:

Enter https://<fqdn of ecewebserver> in the address bar of the web browser.

Accept the certificate.

Reload the Unified CCE Administration page.

## Optional Configuration for Packaged CCE 4000/12000 Agents Deployment

To configure optional components for Packaged CCE 4000 or 12000 Agents deployment.

Task

Remote Site

Machines

Peripheral Set

Add PIMs to the Media Routing Peripheral Gateway

Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment

Configure Email and Chat

Configure Cisco Unified Customer Voice Portal Reporting Server

Configure VVB

Packaged CCE 4000 and 12000 Agent Supported Tools

ICM-to-ICM Gateway Configurations

### Remote Site

A remote site must have at least one peripheral set. Each remote site added appears as a separate tab.

#### Add and Maintain Remote Site for 4000/12000 Agent Deployment

Step 1

Navigate to the Unified CCE Administration > Infrastructure > Inventory .

Step 2

Click the + icon to add a remote site.

Step 3

Enter the remote site name.

Step 4

Click Download Template .

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

CVP

FINESSE_PRIMARY

FINESSE_SECONDARY

CM_PUBLISHER

CM_SUBSCRIBER

CCE_PG

Optional machines:

ECE (refers to ECE Data Server VM for 400 agents and Services Server VM for ECE 1500 agents)

ECE_WEB_SERVER

CVP_REPORTING

GATEWAY

CVVB

CCCSP

THIRD_PARTY_

MULTICHANNEL

MEDIA_SERVER

publicAddress

Public address

Yes

Valid IP address or hostname

connectionInfo

Connection information of the machine

Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, CCCSP , GATEWAY

Enter the username and password in the following format:

ConnectionInfo is optional if you are configuring FTP for CVP (Media Server).

Append the FTP attributes to the username and password in the following format: UserName=<user>&password=<password>; ftpEnabled=<true or false> &ftpUserName=<ftp_username> &ftpPassword=<ftp_password> &ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine .

Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D".

Semicolon (;) delimits the Windows Administration credentials from FTP credentials.

For CVVB, append the mode to the username and password in the following format:

```
info:userName=<user>&password=<password>&mode=<mode>
```

Enter one of the following expected value for mode:

VVB: For Virtualised Voice Browser

MGW: For Media Gateway

VVB_MGW: For both Virtualised Voice Browser and Media Gateway

privateAddress

Private address

Required for CCE_PG

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

Wait for validation to be completed and click Done .

During the validation, tasks are performed depending on the components defined in the CSV template.

If validation fails, then click Back to fix the issues in the file and upload it again.

Agent PG and PIMs are created only when Finesse and CUCM are
                                                                  present.

Multichannel PGs are created. For adding PIMs, see the section "Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment".

VRU PG and PIMs are created only when CVP is present.

Only one peripheral set must be created at a time.

Live Data Configuration Services, TIP_PG and TIP_PG_TOS will be
                                                                  added in Machine_Service table only for Agent PG.

#### Delete Remote Site

##### Before you begin

Delete all the SIP server groups, routing patters, and locations associated with the remote site.

Delete the peripheral sets associated with the remote site.

Disassociate CVP Reporting Server from CVP Server and courtesy callback.

Step 1

Navigate to Unified CCE Administration > Infrastructure > Inventory .

Step 2

Select the remote site you want to delete and click Delete > Current Site .

### Machines

You can configure machines for the main sites and remotes sites in the 4000 Agents and 12000 Agents deployment type.

#### Add and Maintain Machines

##### Before you begin

Step 1

Navigate to the Unified CCE Administration > Infrastructure > Inventory .

Step 2

Go to Import > Device to add a machine.

Step 3

Click Download Template .

Step 4

Fill the particulars in the file and save it.

Column

Description

Required?

Permissible Values

name

Unique identifier for the machine

Yes

Name must start with an alphabet. Maximum length is limited to 128 characters.

Valid characters are a-z, A-Z, 0-9, dot (.), underscore (_), or hyphen (-).

machineType

MachineType Enum name

Yes

Mandatory machines are:

AW

HDS

ECE (refers to ECE Data Server VM for ECE 400 agents and Services Server VM for ECE 1500 agents)

ECE_WEB_SERVER

CVP

CVP_REPORTING

CM_PUBLISHER

CM_SUBSCRIBER

FINESSE

FINESSE_PRIMARY

FINESSE_SECONDARY

GATEWAY

CVVB

CCCSP

SOCIAL_MINER

THIRD_PARTY_MULTICHANNEL

MEDIA_SERVER

CLOUD CONNECT PUBLISHER

THIRD_PARTY_GATEWAY

You can add Cloud Connect Publisher only in the main site.

HDS, AW, CUIC_SUBSCRIBER are only applicable for the main site.

Add FINESSE and CM together.

SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\

publicAddress

Public address

Yes

Valid IP address or hostname

connectionInfo

Connection information of the machine

Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, EXTERNAL_HDS , GATEWAY, CCCSP , and CLOUD CONNECT PUBLISHER

If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                                        You cannot edit Cloud Connect Subscribers from the System Inventory.

Enter the username and password in the following format:

```
userName=<user>&password=<password>
```

For more information on the credentials of each component, see .

ConnectionInfo is optional if you are configuring FTP for CVP (Media Server).

```
UserName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber>
```

Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D".

Semicolon (;) delimits the Windows Administration credentials from FTP credentials.

For CVVB, append the mode to the username and password in the following format:

```
info:userName=<user>&password=<password>&mode=<mode>
```

Enter one of the following expected value for mode:

VVB: For Virtualised Voice Browser

MGW: For Media Gateway

VVB_MGW: For both Virtualised Voice Browser and Media Gateway

privateAddress

Private address

Required for CCE_PG

Valid IP address or hostname

peripheralSetName

Peripheral set name

Required for CUCM, Finesse, CVP

Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            or an underscore (_).

side

Side information

Yes

sideA

sideB

Step 5

Upload the file and click Next .

Step 6

Wait for validation to be completed and click Done .

During the validation, tasks are performed depending on the components defined in the CSV template. For more information about
                                                the tasks, see the Automated Initialization Tasks for 4000 and 12000 Agent Deployments topic.

If validation fails, then click Back to fix the issues in the file and upload it again.

### Edit Machines

#### Edit Machines

You can edit the credentials of any machine using this procedure.

Step 1

On the Inventory page, click the main site or a remote site to edit the following machines:

Machine

Editable Field

AW

Diagnostic Framework Service Domain, Username, and Password

You can also set a Principal AW machine in 4000 and 12000 Agent deployments.

The credentials must be the same for all CCE machines.

Live Data

Administration Username and Password

Finesse

Administration Username and Password

SocialMiner

Administration Username and Password

ECE Web Server

Application Instance, Partition Administration Username, and Password

Virtualized Voice Browser / Media Gateway

Administration Username and Password

A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports Customer Virtual Assistant feature.

To set a VVB as a Principal VVB, do the following:

Important

Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB.

Click the VVB to open the Edit VVB window.

Check the Principal check box.

Select the required mode. This is the required field.

For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                                              Gateway'.

Click Save .

Cisco Contact Center SIP Proxy

Administration Username and Password

CUIC Publisher

Administration Username and Password

CVP

Windows Administration Username and Password , FTP Enabled, Anonymous Access, FTP Credentials, and Port

When a CVP (which acts as a Media Server) is updated, Media Server configurations are propagated to all other CVPs across
                                                                        sites.

Gateway

Administration Username and Password

CVP Reporting

Windows Administration Username and Password

The Deploy check box initializes the CVP Reporting Server configuration. Initialization removes the existing call server association
                                                            and Courtesy Callback configuration.

To reassociate the call servers with the CVP Reporting server, see Configure Unified CVP Reporting Server .

To reconfigure Courtesy Callback, see Courtesy Callback .

IDS Publisher

Administration Username and Password

Media Server

FTP Enabled, Anonymous Access, FTP Credentials, and Port

When a Media Server is updated, configurations are propagated to all CVPs across sites.

Unified CM Publisher

AXL Username and Password

Cloud Connect Publisher

Administration Username and Password

When a Cloud Connect Publisher is updated,configurations are propagated to all CVPs and Finesse across sites.

External HDS

Diagnostic Framework Service Domain, Username, and Password

Step 2

Edit the credentials.

If successful, you can see the message on the Inventory page; else, fix the errors that are shown before clicking Save .

## Update IP Address or Hostname

On the Inventory page, System and Config Administrators can update the IP address or hostname of the following machines:

Core machines

Peripheral Set machines

Optional machines

IP address/hostname change or rebuild can only be done from Principal AW machine. Ensure that the Principal AW user is part
                                             of the local Administrators group on all CCE machines.

If you have rebuilt a CCE_ROGGER or a CCE_AW, do not create a service account manually. Side A AW user account will be used
                                             as a service account for Logger and distributor services.

After updating the hostname in the virtual machine, upload the CA certificates or import the self-signed certificates into
                                             the machine. This should be done before updating the hostname in the inventory.

Task

Core Machines

CCE_AW, CCE_ROGGER 4 , CCE_ROUTER 5 , CCE_LOGGER 6 , CUIC_PUBLISHER, CUIC_SUBSCRIBER, IDS_PUBLISHER, IDS_SUBSCRIBER, and LIVE_DATA

Update Core Machines

Peripheral Set Machines

CCE_PG, CM_PUBLISHER, CM_SUBSCRIBER, FINESSE_PRIMARY, FINESSE_SECONDARY, and CVP

Update Peripheral Set

Optional Machines

CVVB, CVP_REPORTING, MEDIA_SERVER, GATEWAY, EXTERNAL_HDS, CUSTOMER_COLLABORATION_PLATFORM, CCCSP , THIRD_PARTY_MULTICHANNEL, ECE, ECE_WEB_SERVER, CLOUD_CONNECT_PUB, and CLOUD_CONNECT_SUB

Update Optional Machines

After updating the IP address or hostname in the Inventory for CVP, restart the CVP device.

### Update Core Machines

CCE_AW, CCE_ROGGER, CCE_ROUTER, CCE_LOGGER, CUIC_PUBLISHER, CUIC_SUBSCRIBER, IDS_PUBLISHER, IDS_SUBSCRIBER, and LIVE_DATA

If you have changed the hostname of CCE_ROGGER or CCE_ROUTER in the respective virtual machines, restart the Apache Tomcat
                                             service on Principal AW. This should be done before updating the inventory with new hostname for these machines.

Step 1

Navigate to the Unified CCE Administration > Infrastructure > Inventory .

Step 2

Choose Update > Core Machines .

Step 3

Click the Download Present Inventory File icon to get the Inventory File.

Step 4

Fill particulars in the Inventory File and save it. For more information, see Inventory File .

Step 5

Click the Upload Updated Inventory File icon to import the updated file.

Step 6

Click Next to start the inventory update process and see the progress of tasks.

If the upload is successful, a green circle appears against each task.

If the upload is unsuccessful, fix the errors shown, and repeat steps 5 and 6.

Step 7

Click Done .

### Update Optional Machines

CVVB, CVP_REPORTING, MEDIA_SERVER, GATEWAY, EXTERNAL_HDS, CUSTOMER_COLLABORATION_PLATFORM, CCCSP , THIRD_PARTY_MULTICHANNEL, ECE, ECE_WEB_SERVER, CLOUD_CONNECT_PUB, CLOUD_CONNECT_SUB and THIRD_PARTY_GATEWAY .

Before updating the IP address or hostname for Cloud Connect Subscriber, disable auto discovery in the virtual machine. For
                                                   more information, see Auto Discovery .

After updating the IP address or hostname in the inventory for CVP Reporting Server, restart this device.

Step 1

Navigate to the Unified CCE Administration > Infrastructure > Inventory .

Step 2

Choose Update > Optional Machines .

Step 3

Click the Download Present Inventory File icon to get the Inventory File.

Step 4

Fill particulars in the Inventory File and save it. For more information, see Inventory File .

Step 5

Click the Upload Updated Inventory File icon to import the updated file.

Step 6

Click Next to start the inventory update process and see the progress of tasks.

If the upload is successful, a green circle appears against each task.

If the upload is unsuccessful, fix the errors shown, and repeat steps 5 and 6.

Step 7

Click Done .

### Inventory File

The Inventory File in Packaged CCE 4000 and 12000 Agent deployments contain the following fields.

While updating the inventory file, ensure to refer to the Machine Dependencies .

If you are updating hostname for any of the following machines, restart Apache Tomcat service on all CCE_AW machines after
                                                the inventory update:

CCE_AW

FINESSE

EXTERNAL_HDS

CUIC

Column

Description

Required for upload?

Editable in downloaded inventory file?

Permissible Values

name

Unique identifier for the machine

Yes

No

machine Type

Machine Type

Yes

No

Core machines are:

CCE_AW, CCE_ROGGER 7 , CCE_ROUTER 8 , CCE_LOGGER 9 , CUIC_PUBLISHER, CUIC_SUBSCRIBER, IDS_PUBLISHER, IDS_SUBSCRIBER, and LIVE_DATA

Peripheral set machines are:

CCE_PG, CM_PUBLISHER, CM_SUBSCRIBER, FINESSE_PRIMARY, FINESSE_SECONDARY, and CVP

Optional machines are:

CVVB, CVP_REPORTING, MEDIA_SERVER, GATEWAY, EXTERNAL_HDS, CUSTOMER_COLLABORATION_PLATFORM, CCCSP , THIRD_PARTY_MULTICHANNEL, ECE, ECE_WEB_SERVER, CLOUD_CONNECT_PUB, and CLOUD_CONNECT_SUB

public Address

Public address

Yes

No

IP address or hostname of machines present in the inventory

private Address

Private address

Required for CCE_PG, CCE_ROGGER, CCE_ROUTER, and CCE_LOGGER

No

IP address or hostname of machines present in the inventory

side

Side information

Yes

No

sideA

sideB

connection Info

Connection information of the machine

Required for CCE_AW, CCE_PG (Side A) CM_PUBLISHER, CUIC_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, CCCSP , GATEWAY, IDS_PUBLISHER, LIVE_DATA, EXTERNAL_HDS, CLOUD CONNECT PUBLISHER, CVVB, MEDIA_SERVER, CUSTOMER_ COLLABORATION_ PLATFORM

ConnectionInfo is mandatory for the machines even if:

There is no IP address or hostname change.

The isReinstalled value is set to No .

Yes (only username and password are editable)

Enter the username and password in the following format:

```
userName=<user>&password=<password>
```

Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL-encoded values "%26" or "%3D".

For information on the credentials of machines, see Table 1 .

For CCE_PG update, provide the userName and password of CUCM application user.

If you change the CUCM application user, update the inventory for both Side A and Side B CCE_PGs and set the isReinstalled value to yes . This makes sure that both sides of the PG machines have the same application user.

For CVVB, append the mode to the username and password in the following format:

```
info:userName=<user>&password=<password>&mode=<mode>
```

Enter one of the following expected value for mode:

VVB: For Virtualised Voice Browser

MGW: For Media Gateway

VVB_MGW: For both Virtualised Voice Browser and Media Gateway

newpublic Address

new Public address

Yes

Yes

For IP address change: provide the new IP address

For IP address and hostname change: provide the new IP address. The new hostname is auto detected and updated in the inventory.

For hostname change: provide the new IP address same as the old IP address. The new hostname is auto detected and updated
                                          in the inventory.

newprivate Address

new Private address

Required for CCE_ROUTER, CCE_LOGGER, CCE_ROGGER,CCE_PG

Yes

is Reinstalled

is Reinstalled

Yes

Yes

Supported values are:

Yes : if you are setting up a new virtual machine

No : if you are using the existing virtual machine

### Machine Dependencies

Each row in the table below specifies machines types that are dependent on each other. So, whenever you update a machine,
                                             ensure to provide other dependent machine types from the same row.

Dependent Machine Types

CCE_AW (include all AWs), CCE_ROGGER 10 , CCE_LOGGER, and CCE_ROUTER 11

CCE_PG, CM_PUBLISHER 12 , CM_SUBSCRIBER, FINESSE_PRIMARY, and FINESSE_SECONDARY

CCE_PG and CVP (include all CVPs in the peripheral set)

ECE and ECE_WEB_SERVER

Provide both publisher and subscriber details of a machine together. For example: CUIC_PUBLISHER and CUIC_SUBSCRIBER.

Provide Side A and Side B details of a machine together. For example: CVP Side A and CVP Side B.

If you are updating the IP address/hostname or rebuilding a CCE_PG, provide details of all PG client types (configured in
                                                the system), and dependent machine types in the inventory file. For example: If VRU and Multichannel PGs are configured in
                                                the system, provide side A and side B details for both the PGs and all CVP machines.

If only MR PG is configured in the system, provide side A and side B details of this PG in the inventory file.

## Delete Machine

CCE_AW

HDS

CVP_REPORTING

CUIC_SUBSCRIBER

CCCSP

GATEWAY

CVVB

EXTERNAL_THIRD_PARTY_MULTICHANNEL

DC_EXTERNAL_THIRD_PARTY_MULTICHANNEL

MEDIA_SERVER

CLOUD CONNECT PUBLISHER

THIRD_PARTY_GATEWAY

When a Cloud Connect Publisher is deleted, the corresponding Cloud Connect Subscriber is also deleted.

You cannot delete the Principal VVB.

For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                Gateway'.

When a Media Server is deleted, configurations are propagated to all CVPs across sites.

Step 1

To delete a machine individually, select that particular row and click Delete (X) icon at the end of the row.

Step 2

Click Yes .

## Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment

Caution

Before performing the step to enable the secured connection between the components, ensure that the security certificate management
                                          process is completed.

Step 1

In the Peripheral Gateway Component Properties window, click Add .

Step 2

From the Client Type drop-down list, select Media Routing .

Step 3

From the Available PIMS list, select MR PIM1 , then click OK .

Step 4

In the Configuration dialog box, check the Enabled check box.

Step 5

In the Peripheral name field, enter the peripheral name.

Step 6

In the Peripheral ID field, enter the logical controller ID of the Unified CCE component you are adding. The following are the names by which
                                       the Unified CCE components are represented in the database. Refer PG explorer tool using Configuration Manager to get the
                                       Peripheral ID of the corresponding PIM.

Name of Outbound is Outbound

Name of ECE is MR1

Name of CCP is MR2

Name of THIRD_PARTY_MULTICHANNEL is MR3

Name of Digital Routing is MR4

### Example:

Step 7

In the Application Hostname (1) field, enter the hostname or the IP address of ECE services server.

Step 8

In the Application connection port (1) field, enter the port number.

Use the port number that is on the ECE services server that PIM uses to communicate with the application. The default port is 38001.

Step 9

In the Application Hostname (2) field, leave the field blank.

Step 10

In the Application connection port (2) field, leave the field blank.

Step 11

In the Heartbeat interval (sec) field, enter 5 .

Step 12

In the Reconnect interval (sec) field, enter 10 .

Step 13

Check the Enable Secured Connection option.

This establishes a secured connection between the MR PIM and the application server.

Ensure that you provide the correct information in the Application Hostname(1) and Application Connection Port(1) fields.

Step 14

Click OK .

## Peripheral Set

Peripheral set is a collection of all components that are dependent on the peripheral gateway (including the peripheral gateway
                           itself).

For example, Cisco Finesse, CVP. A main or remote site can have zero or more peripheral sets that are associated with it.

You can add a remote site even with a single VVB. This is helpful in getting control over the traffic, and keeping it local
                           to the same data center.

For example, PSTN delivers SIP trunk to both the Data Centers (DCs). You must retain the traffic local to each DC. If the
                           traffic is delivered to DC1, select the VVB and Nuance Speech Server (NSS) from DC1. If the traffic is delivered to DC2, select
                           the VVB and NSS from DC2. This is achieved by adding a remote site only with VVB. From the VVB, NSS points to the SPOG.

### Add and Maintain Peripheral Set

Step 1

Navigate to the Unified CCE Administration > Infrastructure > Inventory .

Step 2

Go to Import > Peripheral Set to add a peripheral set.

Step 3

Click Download Template .

Step 4

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

Mandatory machine is CCE_PG. Optional machines are:

CVP

FINESSE_PRIMARY

FINESSE_SECONDARY

CM_PUBLISHER

CM_SUBSCRIBER

MEDIA_SERVER

publicAddress

Public address

Yes

Valid IP address or hostname

connectionInfo

Connection information of the machine

Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, CCCSP , GATEWAY and LIVE_DATA

Enter the username and password in the following format:

```
userName=<user>&password=<password>
```

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

For CVVB, append the mode to the username and password in the following format:

```
info:userName=<user>&password=<password>&mode=<mode>
```

Enter one of the following expected value for mode:

VVB: For Virtualised Voice Browser

MGW: For Media Gateway

VVB_MGW: For both Virtualised Voice Browser and Media Gateway

privateAddress

Private address

Optional

Valid IP address or hostname

peripheralSetName

Peripheral set name

Required for PG, CUCM, Finesse, CVP

Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         or an underscore (_).

Name must be unique. It cannot be reused even after that peripheral set is deleted.

side

Side information

Yes

sideA

sideB

Step 5

Upload the file and click Next .

Step 6

Wait for validation to be completed and click Done .

During the validation, tasks are performed depending on the components defined in the CSV template.

If validation fails, then click Back to fix the issues in the file and upload it again.

Agent PG and PIMs are created only when Finesse and CUCM are
                                                               present.

Multichannel PGs are created. For adding PIMs, see the section "Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment".

VRU PG and PIMs are created only when CVP is present.

Only one peripheral set must be created at a time.

Live Data Configuration Services, TIP_PG and TIP_PG_TOS will be
                                                               added in Machine_Service table only for Agent PG.

#### What to do next

### Update Peripheral Set

CCE_PG, CM_PUBLISHER, CM_SUBSCRIBER, FINESSE_PRIMARY, FINESSE_SECONDARY, and CVP

After updating the IP address or hostname in the Inventory for CVP, restart the CVP device.

Step 1

Navigate to the Unified CCE Administration > Infrastructure > Inventory .

Step 2

Go to Import > Device > Add Machine to add a machine to a peripheral set.

Step 3

Click Download Template .

Step 4

Fill the particulars in the .csv template file and save it in the local folder. For more information, see Add and Maintain Peripheral Set .

Step 5

Upload the .csv template file and click Next .

Step 6

Click Done .

### Delete Peripheral Set

#### Before you begin

To delete a peripheral set, you must delete:

agents, skill groups, teams, and dialed numbers associated with it.

all Media Server associations with CVP.

Step 1

Navigate to Unified CCE Administration > Infrastructure > Inventory .

Step 2

Select the peripheral set from main or remote site that you want to delete and click Delete > Peripheral Set .

Step 3

Select a peripheral set from the Peripheral Set drop-down list.

Step 4

Click Delete .

Step 5

Click Back to delete another peripheral set. Else, click Done to return to the Inventory page.

## ICM-to-ICM Gateway Configurations

The following table outlines the ICM-to-ICM Gateway configuration tasks in Packaged CCE 4000 and 12000 Agent deployments.

Sequence

ICM-to-ICM Gateway Configuration Tasks

For more information, see ICM to ICM Gateway User Guide for Unified CCE at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

Remote ICM type application gateway global settings

### Remote ICM type application gateway global settings

The configuration for Remote ICM Type Application Gateway can be performed by using Configuration Manager > List Tools > Application Gateway List > .

Following are the Remote ICM type Application Gateway global settings.

Name

Value

Abandon Timeout.

5000

ApplicationGatewayType

1

DateTimeStamp

NULL

ChangeStamp

0

ErrorThreshold

10

HeartbeatLimit

2

HeartbeatRetry

200

HeartbeatTimeout

300

HeartbeatInterval

15000

ID

2

LateTimeout

400

LinkTestThreshold

2

OpenTimeout

500

RequestTimeout

500

SessionRetry

30000

SessionRetryLimit

0

## Optional Configuration for Packaged CCE Lab deployment

### Remote Sites in
                           	 Lab Mode

You can create remote sites in lab mode deployment. If you initiate your lab mode in simplex, you can create remote sites
                                 only with Side A machines.

Before you begin : If you do not have a CA-signed certificate, import self-signed certificates for all components. For more information, see "Self-signed Certificates" section in Packaged CCE Administration and Configuration Guide .

To add a remote site in lab mode deployment, see Add and Maintain Remote Sites for 2000 Agent Deployment .

When you configure the simplex or duplex lab mode deployment, you can also add the following external machines for a remote
                                 site:

Unified CM Publisher

Unified CVP Reporting Server

Contact Center SIP Proxy

Virtualized Voice Browser

Gateway

MediaSense

Enterprise Chat and Email

Third-party Multichannel

Media Server

You can add SocialMiner , MediaSense and Cloud Connect only in the main site.

To add, edit or delete the external machines on the remote site, see Add External Machines and Edit External Machines sections .

For more information on the configuration limits for external machines, see the Solution Design Guide for Cisco Packaged Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-technical-reference-list.html .

### Customers Also Viewed

- Implement CA-Signed Certificates in a CCE 12.6 Solution

| Task |
|---|
| Add and Maintain Remote Sites for 2000 Agent Deployment |
| Add and Maintain External Machines |
| Add PIMs to the Media Routing Peripheral Gateway |
| Add Multichannel PIM to 2000 Agent Deployment |
| Configure Email and Chat |
| Configure Cisco Unified Customer Voice Portal Reporting Server |
| Configure VVB |

| Step 1 | Navigate to Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Click the + icon to
                                             			 open the Add
                                                				Remote Site page. |
| Step 3 | On the CCE
                                                				PG screen, enter the remote site information in the following fields: Field Description Name Enter a name for the site . Maximum length is ten characters. Valid characters are alphanumeric, period (.), and underscore (_). The first character
                                                         must be alphanumeric. Note You cannot use the system reserved terms like core, main, and site. Side A PG Hostname/ IP Address Enter the
                                                         					 hostname, IP address, or fully qualified domain name (FQDN) for Side A. Side B PG Hostname/ IP Address Enter the
                                                         					 hostname, IP address, or fully qualified domain name (FQDN) for Side B. Select PG Client Types to Configure Select the required peripheral gateway client types. The subsequent screens appear as per the selected options. If you select Agent , the Unified CM and Finesse screens appear. If you select VRU , the CVP screen appears. If you select Multichannel , the Configure screen appears. Note The system does not support IP address change. Use the hostname if you foresee a change in IP address. This is applicable
                                                            for all the Hostname/ IP Address fields. | Field | Description | Name | Enter a name for the site . Maximum length is ten characters. Valid characters are alphanumeric, period (.), and underscore (_). The first character
                                                         must be alphanumeric. Note You cannot use the system reserved terms like core, main, and site. | Note | You cannot use the system reserved terms like core, main, and site. | Side A PG Hostname/ IP Address | Enter the
                                                         					 hostname, IP address, or fully qualified domain name (FQDN) for Side A. | Side B PG Hostname/ IP Address | Enter the
                                                         					 hostname, IP address, or fully qualified domain name (FQDN) for Side B. | Select PG Client Types to Configure | Select the required peripheral gateway client types. The subsequent screens appear as per the selected options. If you select Agent , the Unified CM and Finesse screens appear. If you select VRU , the CVP screen appears. If you select Multichannel , the Configure screen appears. | Note | The system does not support IP address change. Use the hostname if you foresee a change in IP address. This is applicable
                                                            for all the Hostname/ IP Address fields. |
| Field | Description |
| Name | Enter a name for the site . Maximum length is ten characters. Valid characters are alphanumeric, period (.), and underscore (_). The first character
                                                         must be alphanumeric. Note You cannot use the system reserved terms like core, main, and site. | Note | You cannot use the system reserved terms like core, main, and site. |
| Note | You cannot use the system reserved terms like core, main, and site. |
| Side A PG Hostname/ IP Address | Enter the
                                                         					 hostname, IP address, or fully qualified domain name (FQDN) for Side A. |
| Side B PG Hostname/ IP Address | Enter the
                                                         					 hostname, IP address, or fully qualified domain name (FQDN) for Side B. |
| Select PG Client Types to Configure | Select the required peripheral gateway client types. The subsequent screens appear as per the selected options. If you select Agent , the Unified CM and Finesse screens appear. If you select VRU , the CVP screen appears. If you select Multichannel , the Configure screen appears. |
| Note | The system does not support IP address change. Use the hostname if you foresee a change in IP address. This is applicable
                                                            for all the Hostname/ IP Address fields. |
| Step 4 | Click Next . The subsequent screens appear as per the
                                             			 selected PG client types. |
| Step 5 | On the Unified CM page, you can either select an existing
                                             			 publisher or add a new one. If you select a publisher, the associated
                                             			 subscribers appear and you can select the subscriber details. To add a new
                                             			 publisher, Select Add a new CM Publisher . Enter the
                                                   				  Hostname, Username, and Password. Click Save . Note You can
                                                            				  add only one CM Publisher while creating a remote site. | Note | You can
                                                            				  add only one CM Publisher while creating a remote site. |
| Note | You can
                                                            				  add only one CM Publisher while creating a remote site. |
| Step 6 | On the Subscribers section, select the following connection
                                             			 settings for the agent peripheral: Side A Connection Side B Connection Mobile Agent Codec |
| Step 7 | Click Next . |
| Step 8 | On the Finesse page, enter the Hostname, Username, and
                                             			 Password for the Finesse primary server. |
| Step 9 | Click Next . |
| Step 10 | On the CVP page, enter the Hostname/IP Address, Username, and Password of the Side A and Side B CVP Servers. |
| Step 11 | Click Next . The
                                             			 system performs the following Configuration tasks. Component Automated Configuration Tasks Unified CCE PG Agent Downloads JTAPI from the Unified Communications Manager, and
                                                                  								  installs it on the Unified CCE PG. Creates the CUCM Peripheral Gateway (PG) with the CUCM PIM. Creates the CTI Server. VRU - Creates the VRU
                                                            							 PG with two VRU PIMs. Multichannel -
                                                            							 Creates the Multichannel PG. Unified CCE Rogger Updates the router configuration with the new PGs that are
                                                            							 created as a part of the site . Unified Communications Manager Creates the Application User that is used to configure the Agent
                                                                  								  PG. Finesse Configures the CTI Server settings. Configures the connection to the AW database. Unified Customer Voice Portal Configures the Unified CVP Call Server components and adds them
                                                                  								  to the Main site Reporting Server. Configures the Unified CVP VXML Server components. Configures the Unified CVP Media Server components. Note If one of
                                                            				  the automated initialization tasks fail, the system reverts all the completed
                                                            				  tasks. | Component | Automated Configuration Tasks | Unified CCE PG | Agent Downloads JTAPI from the Unified Communications Manager, and
                                                                  								  installs it on the Unified CCE PG. Creates the CUCM Peripheral Gateway (PG) with the CUCM PIM. Creates the CTI Server. VRU - Creates the VRU
                                                            							 PG with two VRU PIMs. Multichannel -
                                                            							 Creates the Multichannel PG. | Unified CCE Rogger | Updates the router configuration with the new PGs that are
                                                            							 created as a part of the site . | Unified Communications Manager | Creates the Application User that is used to configure the Agent
                                                                  								  PG. | Finesse | Configures the CTI Server settings. Configures the connection to the AW database. | Unified Customer Voice Portal | Configures the Unified CVP Call Server components and adds them
                                                                  								  to the Main site Reporting Server. Configures the Unified CVP VXML Server components. Configures the Unified CVP Media Server components. | Note | If one of
                                                            				  the automated initialization tasks fail, the system reverts all the completed
                                                            				  tasks. |
| Component | Automated Configuration Tasks |
| Unified CCE PG | Agent Downloads JTAPI from the Unified Communications Manager, and
                                                                  								  installs it on the Unified CCE PG. Creates the CUCM Peripheral Gateway (PG) with the CUCM PIM. Creates the CTI Server. VRU - Creates the VRU
                                                            							 PG with two VRU PIMs. Multichannel -
                                                            							 Creates the Multichannel PG. |
| Unified CCE Rogger | Updates the router configuration with the new PGs that are
                                                            							 created as a part of the site . |
| Unified Communications Manager | Creates the Application User that is used to configure the Agent
                                                                  								  PG. |
| Finesse | Configures the CTI Server settings. Configures the connection to the AW database. |
| Unified Customer Voice Portal | Configures the Unified CVP Call Server components and adds them
                                                                  								  to the Main site Reporting Server. Configures the Unified CVP VXML Server components. Configures the Unified CVP Media Server components. |
| Note | If one of
                                                            				  the automated initialization tasks fail, the system reverts all the completed
                                                            				  tasks. |
| Step 12 | Click Done when all the tasks are complete. If there are
                                             			 configuration errors, you can click Back to edit the previous pages. |
| Step 13 | For the
                                             			 configuration to take effect, do the following: Restart
                                                      					 the router service. If you have selected the PG client type as VRU, restart the two newly configured CVP Call Servers . |

| Field | Description |
|---|---|
| Name | Enter a name for the site . Maximum length is ten characters. Valid characters are alphanumeric, period (.), and underscore (_). The first character
                                                         must be alphanumeric. Note You cannot use the system reserved terms like core, main, and site. | Note | You cannot use the system reserved terms like core, main, and site. |
| Note | You cannot use the system reserved terms like core, main, and site. |
| Side A PG Hostname/ IP Address | Enter the
                                                         					 hostname, IP address, or fully qualified domain name (FQDN) for Side A. |
| Side B PG Hostname/ IP Address | Enter the
                                                         					 hostname, IP address, or fully qualified domain name (FQDN) for Side B. |
| Select PG Client Types to Configure | Select the required peripheral gateway client types. The subsequent screens appear as per the selected options. If you select Agent , the Unified CM and Finesse screens appear. If you select VRU , the CVP screen appears. If you select Multichannel , the Configure screen appears. |

| Note | You cannot use the system reserved terms like core, main, and site. |
|---|---|

| Note | The system does not support IP address change. Use the hostname if you foresee a change in IP address. This is applicable
                                                            for all the Hostname/ IP Address fields. |
|---|---|

| Note | You can
                                                            				  add only one CM Publisher while creating a remote site. |
|---|---|

| Component | Automated Configuration Tasks |
|---|---|
| Unified CCE PG | Agent Downloads JTAPI from the Unified Communications Manager, and
                                                                  								  installs it on the Unified CCE PG. Creates the CUCM Peripheral Gateway (PG) with the CUCM PIM. Creates the CTI Server. VRU - Creates the VRU
                                                            							 PG with two VRU PIMs. Multichannel -
                                                            							 Creates the Multichannel PG. |
| Unified CCE Rogger | Updates the router configuration with the new PGs that are
                                                            							 created as a part of the site . |
| Unified Communications Manager | Creates the Application User that is used to configure the Agent
                                                                  								  PG. |
| Finesse | Configures the CTI Server settings. Configures the connection to the AW database. |
| Unified Customer Voice Portal | Configures the Unified CVP Call Server components and adds them
                                                                  								  to the Main site Reporting Server. Configures the Unified CVP VXML Server components. Configures the Unified CVP Media Server components. |

| Note | If one of
                                                            				  the automated initialization tasks fail, the system reverts all the completed
                                                            				  tasks. |
|---|---|

| Note | For all remote sites configured with Agent PG, you must add the Finesse Self Signed Certificate (if the solution does not
                                                have the CA certificate) to the AW Machine. For more information on how to add Finesse certificate to AW Machine, see the Import VOS Components Certificate Import VOS Components Certificate |
|---|---|

| Step 1 | Navigate to Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Click the site you want to reconfigure. |
| Step 3 | Click Reconfigure to open the CCE
                                                				PG page. Note You can only
                                                            				  add PG client types. | Note | You can only
                                                            				  add PG client types. |
| Note | You can only
                                                            				  add PG client types. |
| Step 4 | Click Next and proceed the same way as you add a new remote site . Refer to Add Remote Site for more information. |

| Note | You can only
                                                            				  add PG client types. |
|---|---|

| Note | Before deleting a remote site, you must stop all the services and processes running on the Cisco Finesse server of the remote
                                                site manually. |
|---|---|

| Note | Post deletion of remote site, delete the Packaged CCE ID from the ORM.properties file. |
|---|---|

| Step 1 | Navigate to Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Click the remote site you want to delete. |
| Step 3 | Click Delete . A
                                             			 message appears asking if you are sure to delete the remote site . |
| Step 4 | Click Yes to confirm. The remote site disappears from the Inventory page. Note The delete operation does not remove the remote site objects permanently from the database. If you want to recreate a site
                                                            with same name, you must permanently delete these objects from Configuration Manager > Tools > Miscellaneous Tools > Deleted Objects . | Note | The delete operation does not remove the remote site objects permanently from the database. If you want to recreate a site
                                                            with same name, you must permanently delete these objects from Configuration Manager > Tools > Miscellaneous Tools > Deleted Objects . |
| Note | The delete operation does not remove the remote site objects permanently from the database. If you want to recreate a site
                                                            with same name, you must permanently delete these objects from Configuration Manager > Tools > Miscellaneous Tools > Deleted Objects . |

| Note | The delete operation does not remove the remote site objects permanently from the database. If you want to recreate a site
                                                            with same name, you must permanently delete these objects from Configuration Manager > Tools > Miscellaneous Tools > Deleted Objects . |
|---|---|

| Note | For detailed steps on how to add a Media Server as an external machine, see Add Media Server as External Machine |
|---|---|

| Note | SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ |
|---|---|

| Step 1 | On the Inventory page, select the main site or the remote site tab and click the New button that appears on the top of the grid. The Add Machine dialog box appears. |
|---|---|
| Step 2 | Choose the machine type from the Type drop-down list. |
| Step 3 | In the Host Name field, enter the hostname, IP address, or fully qualified domain name (FQDN) for the selected machine type. Note The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. | Note | The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. |
| Note | The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. |
| Step 4 | In the machine's Administration section, enter the administration username and password for the selected machine type. |
| Step 5 | Click Save . Note Email and Chat: In Configuration Manager Tool, application instance and application path are to be created and associated to CUCM PG. LDAP configuration needs to be done using Single Sign-On (for Partition Administrators) in the ECE Administration Web interface.
                                                                        For more information, see Enterprise Chat and Email Administrator’s Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html . Virtualized Voice Browser / Media Gateway: When you add VVB, the system will mark the machine as Out of Sync. Either wait for auto synchronization (which happens every
                                                                  10 mins) or do manual synchronization. SocialMiner : If you add SocialMiner , the system automatically creates a SocialMiner Task feed for Task Routing, including the associated campaign and Connection to CCE notification. | Note | Email and Chat: In Configuration Manager Tool, application instance and application path are to be created and associated to CUCM PG. LDAP configuration needs to be done using Single Sign-On (for Partition Administrators) in the ECE Administration Web interface.
                                                                        For more information, see Enterprise Chat and Email Administrator’s Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html . Virtualized Voice Browser / Media Gateway: When you add VVB, the system will mark the machine as Out of Sync. Either wait for auto synchronization (which happens every
                                                                  10 mins) or do manual synchronization. SocialMiner : If you add SocialMiner , the system automatically creates a SocialMiner Task feed for Task Routing, including the associated campaign and Connection to CCE notification. |
| Note | Email and Chat: In Configuration Manager Tool, application instance and application path are to be created and associated to CUCM PG. LDAP configuration needs to be done using Single Sign-On (for Partition Administrators) in the ECE Administration Web interface.
                                                                        For more information, see Enterprise Chat and Email Administrator’s Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html . Virtualized Voice Browser / Media Gateway: When you add VVB, the system will mark the machine as Out of Sync. Either wait for auto synchronization (which happens every
                                                                  10 mins) or do manual synchronization. SocialMiner : If you add SocialMiner , the system automatically creates a SocialMiner Task feed for Task Routing, including the associated campaign and Connection to CCE notification. |

| Note | The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. |
|---|---|

| Note | Email and Chat: In Configuration Manager Tool, application instance and application path are to be created and associated to CUCM PG. LDAP configuration needs to be done using Single Sign-On (for Partition Administrators) in the ECE Administration Web interface.
                                                                        For more information, see Enterprise Chat and Email Administrator’s Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html . Virtualized Voice Browser / Media Gateway: When you add VVB, the system will mark the machine as Out of Sync. Either wait for auto synchronization (which happens every
                                                                  10 mins) or do manual synchronization. SocialMiner : If you add SocialMiner , the system automatically creates a SocialMiner Task feed for Task Routing, including the associated campaign and Connection to CCE notification. |
|---|---|

| Step 1 | In Unified CCE Administration, select Infrastructure Settings > Inventory . |
|---|---|
| Step 2 | Select the main site or the remote site and click the New button that appears on top of the grid. The Add Machine dialog box appears. |
| Step 3 | In the Add Machine dialog box, complete the following fields: Field Required? Description Type Yes From the drop-down list, choose "Media Server". Host Name/IP Address Yes Enter the hostname, IP address, or fully qualified domain name (FQDN) for the selected machine type. Note The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. FTP Section Configure FTP during off-peak hours. Do not do the configuration during heavy call load. FTP Enabled No Indicates whether a Media Server has FTP enabled. A Media Server, which has FTP enabled, is automatically populated as a session variable to the VXMLServer. The (default) Agent
                                                            Greeting recording application automatically uses the Media Servers in the inventory that have FTP enabled for the recording. If Microsoft FTP Service is not enabled in Windows Services Control Panel, then set it to Automatic and start the service. Anonymous Access No Indicates that this Media Server uses anonymous FTP access. In this case, the user name is specified as anonymous by default.
                                                            The password field is not editable if you chose anonymous access. Username and Password No These fields apply only if the FTP field is enabled and if the Anonymous Access field is disabled. In this case, enter the
                                                            username and password. Port Yes Enter a new port number or use the default port number (21). | Field | Required? | Description | Type | Yes | From the drop-down list, choose "Media Server". | Host Name/IP Address | Yes | Enter the hostname, IP address, or fully qualified domain name (FQDN) for the selected machine type. Note The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. | Note | The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. | FTP Section |  | Configure FTP during off-peak hours. Do not do the configuration during heavy call load. | FTP Enabled | No | Indicates whether a Media Server has FTP enabled. A Media Server, which has FTP enabled, is automatically populated as a session variable to the VXMLServer. The (default) Agent
                                                            Greeting recording application automatically uses the Media Servers in the inventory that have FTP enabled for the recording. If Microsoft FTP Service is not enabled in Windows Services Control Panel, then set it to Automatic and start the service. | Anonymous Access | No | Indicates that this Media Server uses anonymous FTP access. In this case, the user name is specified as anonymous by default.
                                                            The password field is not editable if you chose anonymous access. | Username and Password | No | These fields apply only if the FTP field is enabled and if the Anonymous Access field is disabled. In this case, enter the
                                                            username and password. | Port | Yes | Enter a new port number or use the default port number (21). |
| Field | Required? | Description |
| Type | Yes | From the drop-down list, choose "Media Server". |
| Host Name/IP Address | Yes | Enter the hostname, IP address, or fully qualified domain name (FQDN) for the selected machine type. Note The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. | Note | The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. |
| Note | The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. |
| FTP Section |  | Configure FTP during off-peak hours. Do not do the configuration during heavy call load. |
| FTP Enabled | No | Indicates whether a Media Server has FTP enabled. A Media Server, which has FTP enabled, is automatically populated as a session variable to the VXMLServer. The (default) Agent
                                                            Greeting recording application automatically uses the Media Servers in the inventory that have FTP enabled for the recording. If Microsoft FTP Service is not enabled in Windows Services Control Panel, then set it to Automatic and start the service. |
| Anonymous Access | No | Indicates that this Media Server uses anonymous FTP access. In this case, the user name is specified as anonymous by default.
                                                            The password field is not editable if you chose anonymous access. |
| Username and Password | No | These fields apply only if the FTP field is enabled and if the Anonymous Access field is disabled. In this case, enter the
                                                            username and password. |
| Port | Yes | Enter a new port number or use the default port number (21). |
| Step 4 | Click Save . Note When a Media Server is added, configurations are propagated to all CVPs across sites. | Note | When a Media Server is added, configurations are propagated to all CVPs across sites. |
| Note | When a Media Server is added, configurations are propagated to all CVPs across sites. |

| Field | Required? | Description |
|---|---|---|
| Type | Yes | From the drop-down list, choose "Media Server". |
| Host Name/IP Address | Yes | Enter the hostname, IP address, or fully qualified domain name (FQDN) for the selected machine type. Note The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. | Note | The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. |
| Note | The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. |
| FTP Section |  | Configure FTP during off-peak hours. Do not do the configuration during heavy call load. |
| FTP Enabled | No | Indicates whether a Media Server has FTP enabled. A Media Server, which has FTP enabled, is automatically populated as a session variable to the VXMLServer. The (default) Agent
                                                            Greeting recording application automatically uses the Media Servers in the inventory that have FTP enabled for the recording. If Microsoft FTP Service is not enabled in Windows Services Control Panel, then set it to Automatic and start the service. |
| Anonymous Access | No | Indicates that this Media Server uses anonymous FTP access. In this case, the user name is specified as anonymous by default.
                                                            The password field is not editable if you chose anonymous access. |
| Username and Password | No | These fields apply only if the FTP field is enabled and if the Anonymous Access field is disabled. In this case, enter the
                                                            username and password. |
| Port | Yes | Enter a new port number or use the default port number (21). |

| Note | The system attempts to convert the value you enter to FQDN. The system does not support IP address change. Use the hostname if you foresee a change in IP address. |
|---|---|

| Note | When a Media Server is added, configurations are propagated to all CVPs across sites. |
|---|---|

| Machine | Editable Field |
|---|---|
| Unified CM Publisher | AXL Username and Password |
| SocialMiner | Administration Username and Password |
| Enterprise Chat and Email and 3rd Party Multichannel | Web Server: edit partition Administration User name and Password. Data Server: none |
| Virtualized Voice Browser / Media Gateway | Administration Username and Password A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports Customer Virtual Assistant feature. To set a VVB as a Principal VVB, do the following: Important Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. Click the VVB row. The VVB machine details page appears and you can modify the VVB details. Check the Principal check box. Select the required mode. This is the required parameter. Note For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                               Gateway'. Enter Administrator username and password. Click Save . | Important | Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. | Note | For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                               Gateway'. |
| Important | Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. |
| Note | For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                               Gateway'. |
| Cisco Contact Center SIP Proxy | Administration Username and Password |
| Gateway | Administration Username and Password |
| Unified CVP Reporting | Windows Administration credentials |
| Cloud Connect | Administration Username and Password Note When a Cloud Connect is updated, configurations are propagated to all CVPs and Finesse across sites. | Note | When a Cloud Connect is updated, configurations are propagated to all CVPs and Finesse across sites. |
| Note | When a Cloud Connect is updated, configurations are propagated to all CVPs and Finesse across sites. |
| Media Server | FTP Enabled, Anonymous Access, FTP Credentials, and Port Note When a Media Server is updated, configurations are propagated to all CVPs and  across sites. | Note | When a Media Server is updated, configurations are propagated to all CVPs and  across sites. |
| Note | When a Media Server is updated, configurations are propagated to all CVPs and  across sites. |

| Important | Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. |
|---|---|

| Note | For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                               Gateway'. |
|---|---|

| Note | When a Cloud Connect is updated, configurations are propagated to all CVPs and Finesse across sites. |
|---|---|

| Note | When a Media Server is updated, configurations are propagated to all CVPs and  across sites. |
|---|---|

| Note | You cannot delete the Virtualized Voice Browser and Cisco Contact Center SIP Proxy external machines if they are associated with a SIP Server Group. To delete these external machines, you must disassociate
                                                   them from the SIP Server Group. You cannot delete the Gateway external machine if it is associated with Location. To delete this external machine, you must
                                                   disassociate the Gateway from the Location. If you delete the Unified CM Publisher, the Unified CM Subscribers are also deleted automatically, and the Configure Deployment
                                                   pop-up window opens. Enter the name, IP address, AXL username, and AXL password for the Unified CM Publisher in your deployment. When a Media Server is deleted, configurations are propogated to all CVPs across sites. |
|---|---|

| Note | IP address/hostname change or rebuild can only be done from Side A AW machine. The AW machine credentials are shared with
                                             all CCE machines. Ensure that the Side A AW user is part of the local Administrators group on all CCE machines. If you have rebuilt a CCE_ROGGER or a CCE_AW, do not create a service account manually. Side A AW user account will be used
                                             as a service account for Logger and distributor services. While updating the inventory for routers in Unified CCE Administration, at least one side of the router needs to be running
                                             successfully if both the sides were rebuilt. If not, you must manually add the router on one side through the web setup. After updating the hostname in the virtual machine, regenerate and update CA or self-signed certificate on the machine. This
                                             should be done before updating the hostname in the inventory. |
|---|---|

| Machines | Task |
|---|---|
| Core Machines in Main Site CCE_AW, CCE_ROGGER, CCE_PG, CVP, CM_PUBLISHER, CUIC_PUBLISHER (CUIC-LD-IDS coresident), CUIC_SUBSCRIBER, FINESSE, and VM_HOST | Update Core Machines Note After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. | Note | After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. |
| Note | After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. |
| Core Machines in Remote Site CCE_PG, CVP, CM_PUBLISHER 1 , CM_SUBSCRIBER, and FINESSE_PRIMARY |
| Optional Machines | Update Optional Machines |
| CVVB, CVP_REPORTING, MEDIA_SERVER, GATEWAY, EXTERNAL_HDS, CUSTOMER_COLLABORATION_PLATFORM, CCCSP , THIRD_PARTY_MULTICHANNEL, ECE, ECE_WEB_SERVER, CLOUD_CONNECT_PUB, and CLOUD_CONNECT_SUB |

| Note | After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. |
|---|---|

| Note | After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. If you have changed the hostname of CCE_ROGGER in the virtual machine, restart the Apache Tomcat service on Side A AW. This
                                                   should be done before updating the inventory with new hostname for CCE_ROGGER. References to VM_HOST in this topic apply only to VMware-based Packaged CCE 2000 Agents deployments before the 15.0(1) SU2/ES202607
                                                   ES is installed. References to VM_HOST remain in the CSV file even after the ES is applied; however, this field is no longer
                                                   validated. |
|---|---|

| Step 1 | Navigate to the Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Choose Update > Core Machines . |
| Step 3 | Click the Download Present Inventory File icon to get the Inventory File. |
| Step 4 | Fill particulars in the Inventory File and save it. For more information, see Inventory Content File |
| Step 5 | Click the Upload Updated Inventory File icon to import the updated file. |
| Step 6 | Click Next to start the inventory update process and see the progress of tasks. If the upload is successful, a green circle appears against each task. If the upload is unsuccessful, fix the errors that are shown and repeat steps 5 and 6. |
| Step 7 | Click Done . |

| Note | After updating the IP address or hostname in the inventory for CVP Reporting Server, restart this device. |
|---|---|

| Step 1 | Navigate to the Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Choose Update > Optional Machines . |
| Step 3 | Click the Download Present Inventory File icon to get the Inventory File. |
| Step 4 | Fill particulars in the Inventory File and save it. For more information, see |
| Step 5 | Click the Upload Updated Inventory File icon to import the updated file. |
| Step 6 | Click Next to start the inventory update process and see the progress of tasks. If the upload is successful, a green circle appears against each task. If the upload is unsuccessful, fix the errors shown, and repeat steps 5 and 6. |
| Step 7 | Click Done . |

| Note | During Technology Refresh upgrade, auto discovery is disabled by default till all the core components are updated. |
|---|---|

| Note | After CCE 15.0(1) SU2/ES202607 or a later ES is installed, auto discovery is not supported for Packaged CCE 2000 Agents deployments
                                             on VMware-based or Nutanix-based deployments. Update the inventory manually by importing the Packaged CCE 2000 Agents inventory
                                             CSV file. For more details, see Step 3 (b) in Initialize the Packaged CCE 2000 Agents Deployment Type |
|---|---|

| Step 1 | Navigate to the Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Choose Update > Auto Discovery . |
| Step 3 | If Auto Discovery Status is Enabled, click Disable to disable auto discovery. |
| Step 4 | If Auto Discovery Status is Disabled, click Enable to enable auto discovery. Note If you don't enable auto discovery, it gets enabled automatically after three days of disabling. | Note | If you don't enable auto discovery, it gets enabled automatically after three days of disabling. |
| Note | If you don't enable auto discovery, it gets enabled automatically after three days of disabling. |
| Step 5 | Click Done . |

| Note | If you don't enable auto discovery, it gets enabled automatically after three days of disabling. |
|---|---|

| Note | IP address/hostname change or rebuild can only be done from Side A AW machine. The AW machine credentials are shared with
                                                all CCE machines. Ensure that the Side A AW user is part of the local Administrators group on all CCE machines. If you have rebuilt a CCE_ROGGER or a CCE_AW, do not create a service account manually. Side A AW user account will be used
                                                as a service account for Logger and distributor services. While updating the inventory for routers in Unified CCE Administration, at least one side of the router needs to be running
                                                successfully if both the sides were rebuilt. If not, you must manually add the router on one side through the web setup. After updating the hostname in the virtual machine, regenerate and update CA or self-signed certificate on the machine. This
                                                should be done before updating the hostname in the inventory. References to VM_HOST in this topic apply only to VMware-based Packaged CCE 2000 Agents deployments before the 15.0(1) SU2/ES202607
                                                ES is installed. References to VM_HOST remain in the CSV file even after the ES is applied; however, this field is no longer
                                                validated. |
|---|---|

| Machines | Task |
|---|---|
| Core Machines in Main Site CCE_AW, CCE_ROGGER, CCE_PG, CVP, CM_PUBLISHER, CUIC_PUBLISHER (CUIC-LD-IDS coresident), CUIC_SUBSCRIBER, FINESSE, and VM_HOST | Update Core Machines Note After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. | Note | After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. |
| Note | After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. |
| Core Machines in Remote Site CCE_PG, CVP, CM_PUBLISHER 3 , CM_SUBSCRIBER, and FINESSE_PRIMARY |
| Optional Machines | Update Optional Machines |
| CVVB, CVP_REPORTING, MEDIA_SERVER, GATEWAY, EXTERNAL_HDS, CUSTOMER_COLLABORATION_PLATFORM, CCCSP , THIRD_PARTY_MULTICHANNEL, ECE, ECE_WEB_SERVER, CLOUD_CONNECT_PUB, and CLOUD_CONNECT_SUB |

| Note | After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. |
|---|---|

| Note | If ECE Data Server is deployed on box, you do not need to create a Dialed Number associated with the PIM. |
|---|---|

| Note | Refer to the Cisco Packaged Contact Center Enterprise Features Guide at https://www.cisco.com/en/US/products/ps12586/prod_maintenance_guides_list.html for directions on adding the Outbound PIM and the Multichannel PIMs. Refer to the Enterprise Chat and Email Installation Guide (for Packaged Contact Center Enterprise) at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-installation-guides-list.html . |
|---|---|

| Caution | Before performing the step to enable the secured connection between the components, ensure that the security certificate management
                                             process is completed. |
|---|---|

| Step 1 | In the Peripheral Gateway Component Properties window, click Add . |
|---|---|
| Step 2 | From the Client Type drop-down list, select Media Routing . |
| Step 3 | From the Available PIMS list, select MR PIM1 , then click OK . |
| Step 4 | In the Configuration dialog box, check the Enabled check box. |
| Step 5 | In the Peripheral name field, enter the peripheral name. |
| Step 6 | In the Peripheral ID field, enter the logical controller ID of the Unified CCE component you are adding. The following are the names by which
                                          the Unified CCE components are represented in the database. Refer Peripheral Gateway page in CCE Admin to get the peripheral ID of the corresponding PIM. Name of Outbound is Outbound Name of ECE is Multichannel Name of CCP is Multichannel2 Name of THIRD_PARTY_MULTICHANNEL is MutliChannel3 Name of Digital Routing is DigitalRouting Example: If you are adding ECE, find the component of the name Multichannel in the database. Enter the logical controller ID of that component in the Peripheral ID field. |
| Step 7 | In the Application Hostname (1) field, enter the hostname or the IP address of the ECE services server. |
| Step 8 | In the Application connection port (1) field, enter the port number. Note Use the port number that is on the ECE services server that PIM uses to communicate with the application. The default port is 38001. | Note | Use the port number that is on the ECE services server that PIM uses to communicate with the application. The default port is 38001. |
| Note | Use the port number that is on the ECE services server that PIM uses to communicate with the application. The default port is 38001. |
| Step 9 | In the Application Hostname (2) field, leave the field blank. |
| Step 10 | In the Application connection port (2) field, leave the field blank. |
| Step 11 | In the Heartbeat interval (sec) field, enter 5 . |
| Step 12 | In the Reconnect interval (sec) field, enter 10 . |
| Step 13 | Check the Enable Secured Connection option. This establishes a secured connection between the MR PIM and the application server. Ensure that you provide the correct information in the application hostname(1) and Application Connection Port(1) fields. |
| Step 14 | Click OK . |

| Note | Use the port number that is on the ECE services server that PIM uses to communicate with the application. The default port is 38001. |
|---|---|

| Step 1 | Configure LDAP in the ECE Administration Web Interface. For more information, see Single Sign-On (for Partition Administrators) in the Enterprise Chat and Email Administrator’s Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/products-maintenance-guides-list.html . |
|---|---|
| Step 2 | Accept the certificate in the Unified CCE Administration . Do the following: Enter https://<fqdn of ecewebserver> in the address bar of the web browser. Accept the certificate. Reload the Unified CCE Administration page. |

| Task |
|---|
| Remote Site |
| Machines |
| Peripheral Set |
| Add PIMs to the Media Routing Peripheral Gateway |
| Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment |
| Configure Email and Chat |
| Configure Cisco Unified Customer Voice Portal Reporting Server |
| Configure VVB |
| Packaged CCE 4000 and 12000 Agent Supported Tools |
| ICM-to-ICM Gateway Configurations |

| Step 1 | Navigate to the Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Click the + icon to add a remote site. |
| Step 3 | Enter the remote site name. |
| Step 4 | Click Download Template . |
| Step 5 | Fill the particulars in the file and save it. Table 1. CSV Template Details Column Description Required? Permissible Values name Unique identifier for the machine Yes Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            underscore (_), or hyphen (-). machineType MachineType Enum name Yes Mandatory machines are: CVP FINESSE_PRIMARY FINESSE_SECONDARY CM_PUBLISHER CM_SUBSCRIBER CCE_PG Optional machines: ECE (refers to ECE Data Server VM for 400 agents and Services Server VM for ECE 1500 agents) ECE_WEB_SERVER CVP_REPORTING GATEWAY CVVB CCCSP THIRD_PARTY_ MULTICHANNEL MEDIA_SERVER publicAddress Public address Yes Valid IP address or hostname connectionInfo Connection information of the machine Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, CCCSP , GATEWAY Enter the username and password in the following format: userName=<user>&password=<password> ConnectionInfo is optional if you are configuring FTP for CVP (Media Server). Append the FTP attributes to the username and password in the following format: UserName=<user>&password=<password>; ftpEnabled=<true or false> &ftpUserName=<ftp_username> &ftpPassword=<ftp_password> &ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway privateAddress Private address Required for CCE_PG Valid IP address or hostname peripheralSetName Peripheral set name Required for PG, CUCM, Finesse, CVP Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            or an underscore (_). side Side information Yes sideA sideB | Column | Description | Required? | Permissible Values | name | Unique identifier for the machine | Yes | Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            underscore (_), or hyphen (-). | machineType | MachineType Enum name | Yes | Mandatory machines are: CVP FINESSE_PRIMARY FINESSE_SECONDARY CM_PUBLISHER CM_SUBSCRIBER CCE_PG Optional machines: ECE (refers to ECE Data Server VM for 400 agents and Services Server VM for ECE 1500 agents) ECE_WEB_SERVER CVP_REPORTING GATEWAY CVVB CCCSP THIRD_PARTY_ MULTICHANNEL MEDIA_SERVER | publicAddress | Public address | Yes | Valid IP address or hostname | connectionInfo | Connection information of the machine | Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, CCCSP , GATEWAY | Enter the username and password in the following format: userName=<user>&password=<password> ConnectionInfo is optional if you are configuring FTP for CVP (Media Server). Append the FTP attributes to the username and password in the following format: UserName=<user>&password=<password>; ftpEnabled=<true or false> &ftpUserName=<ftp_username> &ftpPassword=<ftp_password> &ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway | Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. | privateAddress | Private address | Required for CCE_PG | Valid IP address or hostname | peripheralSetName | Peripheral set name | Required for PG, CUCM, Finesse, CVP | Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            or an underscore (_). | side | Side information | Yes | sideA sideB |
| Column | Description | Required? | Permissible Values |
| name | Unique identifier for the machine | Yes | Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            underscore (_), or hyphen (-). |
| machineType | MachineType Enum name | Yes | Mandatory machines are: CVP FINESSE_PRIMARY FINESSE_SECONDARY CM_PUBLISHER CM_SUBSCRIBER CCE_PG Optional machines: ECE (refers to ECE Data Server VM for 400 agents and Services Server VM for ECE 1500 agents) ECE_WEB_SERVER CVP_REPORTING GATEWAY CVVB CCCSP THIRD_PARTY_ MULTICHANNEL MEDIA_SERVER |
| publicAddress | Public address | Yes | Valid IP address or hostname |
| connectionInfo | Connection information of the machine | Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, CCCSP , GATEWAY | Enter the username and password in the following format: userName=<user>&password=<password> ConnectionInfo is optional if you are configuring FTP for CVP (Media Server). Append the FTP attributes to the username and password in the following format: UserName=<user>&password=<password>; ftpEnabled=<true or false> &ftpUserName=<ftp_username> &ftpPassword=<ftp_password> &ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway | Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| privateAddress | Private address | Required for CCE_PG | Valid IP address or hostname |
| peripheralSetName | Peripheral set name | Required for PG, CUCM, Finesse, CVP | Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            or an underscore (_). |
| side | Side information | Yes | sideA sideB |
| Step 6 | Upload the file and click Next . |
| Step 7 | Wait for validation to be completed and click Done . During the validation, tasks are performed depending on the components defined in the CSV template. If validation fails, then click Back to fix the issues in the file and upload it again. The remote site that is created appears as a tab on the Inventory page. Note Agent PG and PIMs are created only when Finesse and CUCM are
                                                                  present. Multichannel PGs are created. For adding PIMs, see the section "Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment". VRU PG and PIMs are created only when CVP is present. Only one peripheral set must be created at a time. Live Data Configuration Services, TIP_PG and TIP_PG_TOS will be
                                                                  added in Machine_Service table only for Agent PG. | Note | Agent PG and PIMs are created only when Finesse and CUCM are
                                                                  present. Multichannel PGs are created. For adding PIMs, see the section "Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment". VRU PG and PIMs are created only when CVP is present. Only one peripheral set must be created at a time. Live Data Configuration Services, TIP_PG and TIP_PG_TOS will be
                                                                  added in Machine_Service table only for Agent PG. |
| Note | Agent PG and PIMs are created only when Finesse and CUCM are
                                                                  present. Multichannel PGs are created. For adding PIMs, see the section "Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment". VRU PG and PIMs are created only when CVP is present. Only one peripheral set must be created at a time. Live Data Configuration Services, TIP_PG and TIP_PG_TOS will be
                                                                  added in Machine_Service table only for Agent PG. |

| Column | Description | Required? | Permissible Values |
|---|---|---|---|
| name | Unique identifier for the machine | Yes | Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            underscore (_), or hyphen (-). |
| machineType | MachineType Enum name | Yes | Mandatory machines are: CVP FINESSE_PRIMARY FINESSE_SECONDARY CM_PUBLISHER CM_SUBSCRIBER CCE_PG Optional machines: ECE (refers to ECE Data Server VM for 400 agents and Services Server VM for ECE 1500 agents) ECE_WEB_SERVER CVP_REPORTING GATEWAY CVVB CCCSP THIRD_PARTY_ MULTICHANNEL MEDIA_SERVER |
| publicAddress | Public address | Yes | Valid IP address or hostname |
| connectionInfo | Connection information of the machine | Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, CCCSP , GATEWAY | Enter the username and password in the following format: userName=<user>&password=<password> ConnectionInfo is optional if you are configuring FTP for CVP (Media Server). Append the FTP attributes to the username and password in the following format: UserName=<user>&password=<password>; ftpEnabled=<true or false> &ftpUserName=<ftp_username> &ftpPassword=<ftp_password> &ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway | Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| privateAddress | Private address | Required for CCE_PG | Valid IP address or hostname |
| peripheralSetName | Peripheral set name | Required for PG, CUCM, Finesse, CVP | Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            or an underscore (_). |
| side | Side information | Yes | sideA sideB |

| Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
|---|---|

| Note | Agent PG and PIMs are created only when Finesse and CUCM are
                                                                  present. Multichannel PGs are created. For adding PIMs, see the section "Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment". VRU PG and PIMs are created only when CVP is present. Only one peripheral set must be created at a time. Live Data Configuration Services, TIP_PG and TIP_PG_TOS will be
                                                                  added in Machine_Service table only for Agent PG. |
|---|---|

| Step 1 | Navigate to Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Select the remote site you want to delete and click Delete > Current Site . The remote site is deleted from the inventory. |

| Step 1 | Navigate to the Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Go to Import > Device to add a machine. |
| Step 3 | Click Download Template . |
| Step 4 | Fill the particulars in the file and save it. Table 2. CSV Template Details Column Description Required? Permissible Values name Unique identifier for the machine Yes Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.), underscore (_), or hyphen (-). machineType MachineType Enum name Yes Mandatory machines are: AW HDS ECE (refers to ECE Data Server VM for ECE 400 agents and Services Server VM for ECE 1500 agents) ECE_WEB_SERVER CVP CVP_REPORTING CM_PUBLISHER CM_SUBSCRIBER FINESSE FINESSE_PRIMARY FINESSE_SECONDARY GATEWAY CVVB CCCSP SOCIAL_MINER THIRD_PARTY_MULTICHANNEL MEDIA_SERVER CLOUD CONNECT PUBLISHER THIRD_PARTY_GATEWAY Note You can add Cloud Connect Publisher only in the main site. Note HDS, AW, CUIC_SUBSCRIBER are only applicable for the main site. Add FINESSE and CM together. SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ publicAddress Public address Yes Valid IP address or hostname connectionInfo Connection information of the machine Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, EXTERNAL_HDS , GATEWAY, CCCSP , and CLOUD CONNECT PUBLISHER Note If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                                        You cannot edit Cloud Connect Subscribers from the System Inventory. Enter the username and password in the following format: userName=<user>&password=<password> For more information on the credentials of each component, see . ConnectionInfo is optional if you are configuring FTP for CVP (Media Server). Append the FTP attributes to the username and password in the following format: UserName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway privateAddress Private address Required for CCE_PG Valid IP address or hostname peripheralSetName Peripheral set name Required for CUCM, Finesse, CVP Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            or an underscore (_). side Side information Yes sideA sideB | Column | Description | Required? | Permissible Values | name | Unique identifier for the machine | Yes | Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.), underscore (_), or hyphen (-). | machineType | MachineType Enum name | Yes | Mandatory machines are: AW HDS ECE (refers to ECE Data Server VM for ECE 400 agents and Services Server VM for ECE 1500 agents) ECE_WEB_SERVER CVP CVP_REPORTING CM_PUBLISHER CM_SUBSCRIBER FINESSE FINESSE_PRIMARY FINESSE_SECONDARY GATEWAY CVVB CCCSP SOCIAL_MINER THIRD_PARTY_MULTICHANNEL MEDIA_SERVER CLOUD CONNECT PUBLISHER THIRD_PARTY_GATEWAY Note You can add Cloud Connect Publisher only in the main site. Note HDS, AW, CUIC_SUBSCRIBER are only applicable for the main site. Add FINESSE and CM together. SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ | Note | You can add Cloud Connect Publisher only in the main site. | Note | HDS, AW, CUIC_SUBSCRIBER are only applicable for the main site. Add FINESSE and CM together. SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ | publicAddress | Public address | Yes | Valid IP address or hostname | connectionInfo | Connection information of the machine | Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, EXTERNAL_HDS , GATEWAY, CCCSP , and CLOUD CONNECT PUBLISHER Note If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                                        You cannot edit Cloud Connect Subscribers from the System Inventory. | Note | If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                                        You cannot edit Cloud Connect Subscribers from the System Inventory. | Enter the username and password in the following format: userName=<user>&password=<password> For more information on the credentials of each component, see . ConnectionInfo is optional if you are configuring FTP for CVP (Media Server). Append the FTP attributes to the username and password in the following format: UserName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway | Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. | privateAddress | Private address | Required for CCE_PG | Valid IP address or hostname | peripheralSetName | Peripheral set name | Required for CUCM, Finesse, CVP | Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            or an underscore (_). | side | Side information | Yes | sideA sideB |
| Column | Description | Required? | Permissible Values |
| name | Unique identifier for the machine | Yes | Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.), underscore (_), or hyphen (-). |
| machineType | MachineType Enum name | Yes | Mandatory machines are: AW HDS ECE (refers to ECE Data Server VM for ECE 400 agents and Services Server VM for ECE 1500 agents) ECE_WEB_SERVER CVP CVP_REPORTING CM_PUBLISHER CM_SUBSCRIBER FINESSE FINESSE_PRIMARY FINESSE_SECONDARY GATEWAY CVVB CCCSP SOCIAL_MINER THIRD_PARTY_MULTICHANNEL MEDIA_SERVER CLOUD CONNECT PUBLISHER THIRD_PARTY_GATEWAY Note You can add Cloud Connect Publisher only in the main site. Note HDS, AW, CUIC_SUBSCRIBER are only applicable for the main site. Add FINESSE and CM together. SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ | Note | You can add Cloud Connect Publisher only in the main site. | Note | HDS, AW, CUIC_SUBSCRIBER are only applicable for the main site. Add FINESSE and CM together. SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ |
| Note | You can add Cloud Connect Publisher only in the main site. |
| Note | HDS, AW, CUIC_SUBSCRIBER are only applicable for the main site. Add FINESSE and CM together. SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ |
| publicAddress | Public address | Yes | Valid IP address or hostname |
| connectionInfo | Connection information of the machine | Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, EXTERNAL_HDS , GATEWAY, CCCSP , and CLOUD CONNECT PUBLISHER Note If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                                        You cannot edit Cloud Connect Subscribers from the System Inventory. | Note | If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                                        You cannot edit Cloud Connect Subscribers from the System Inventory. | Enter the username and password in the following format: userName=<user>&password=<password> For more information on the credentials of each component, see . ConnectionInfo is optional if you are configuring FTP for CVP (Media Server). Append the FTP attributes to the username and password in the following format: UserName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway | Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| Note | If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                                        You cannot edit Cloud Connect Subscribers from the System Inventory. |
| Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| privateAddress | Private address | Required for CCE_PG | Valid IP address or hostname |
| peripheralSetName | Peripheral set name | Required for CUCM, Finesse, CVP | Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            or an underscore (_). |
| side | Side information | Yes | sideA sideB |
| Step 5 | Upload the file and click Next . |
| Step 6 | Wait for validation to be completed and click Done . During the validation, tasks are performed depending on the components defined in the CSV template. For more information about
                                                the tasks, see the Automated Initialization Tasks for 4000 and 12000 Agent Deployments topic. If validation fails, then click Back to fix the issues in the file and upload it again. |

| Column | Description | Required? | Permissible Values |
|---|---|---|---|
| name | Unique identifier for the machine | Yes | Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.), underscore (_), or hyphen (-). |
| machineType | MachineType Enum name | Yes | Mandatory machines are: AW HDS ECE (refers to ECE Data Server VM for ECE 400 agents and Services Server VM for ECE 1500 agents) ECE_WEB_SERVER CVP CVP_REPORTING CM_PUBLISHER CM_SUBSCRIBER FINESSE FINESSE_PRIMARY FINESSE_SECONDARY GATEWAY CVVB CCCSP SOCIAL_MINER THIRD_PARTY_MULTICHANNEL MEDIA_SERVER CLOUD CONNECT PUBLISHER THIRD_PARTY_GATEWAY Note You can add Cloud Connect Publisher only in the main site. Note HDS, AW, CUIC_SUBSCRIBER are only applicable for the main site. Add FINESSE and CM together. SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ | Note | You can add Cloud Connect Publisher only in the main site. | Note | HDS, AW, CUIC_SUBSCRIBER are only applicable for the main site. Add FINESSE and CM together. SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ |
| Note | You can add Cloud Connect Publisher only in the main site. |
| Note | HDS, AW, CUIC_SUBSCRIBER are only applicable for the main site. Add FINESSE and CM together. SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ |
| publicAddress | Public address | Yes | Valid IP address or hostname |
| connectionInfo | Connection information of the machine | Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, EXTERNAL_HDS , GATEWAY, CCCSP , and CLOUD CONNECT PUBLISHER Note If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                                        You cannot edit Cloud Connect Subscribers from the System Inventory. | Note | If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                                        You cannot edit Cloud Connect Subscribers from the System Inventory. | Enter the username and password in the following format: userName=<user>&password=<password> For more information on the credentials of each component, see . ConnectionInfo is optional if you are configuring FTP for CVP (Media Server). Append the FTP attributes to the username and password in the following format: UserName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway | Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| Note | If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                                        You cannot edit Cloud Connect Subscribers from the System Inventory. |
| Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| privateAddress | Private address | Required for CCE_PG | Valid IP address or hostname |
| peripheralSetName | Peripheral set name | Required for CUCM, Finesse, CVP | Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                            or an underscore (_). |
| side | Side information | Yes | sideA sideB |

| Note | You can add Cloud Connect Publisher only in the main site. |
|---|---|

| Note | HDS, AW, CUIC_SUBSCRIBER are only applicable for the main site. Add FINESSE and CM together. SSH algorithm hmac-sha2-256-etm@openssh.com must be added to ClientMacAlgorithms in the AW registry for Cisco IOS Gateway communication: Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Cisco Systems, Inc.\ICM\Cisco SSH Configuration\ |
|---|---|

| Note | If you edit the Cloud Connect Publisher, the Cloud Connect Subscribers associated with the publisher are updated automatically.
                                                                        You cannot edit Cloud Connect Subscribers from the System Inventory. |
|---|---|

| Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
|---|---|

| Step 1 | On the Inventory page, click the main site or a remote site to edit the following machines: Table 3. Machine Credentials Machine Editable Field AW Diagnostic Framework Service Domain, Username, and Password You can also set a Principal AW machine in 4000 and 12000 Agent deployments. The credentials must be the same for all CCE machines. Live Data Administration Username and Password Finesse Administration Username and Password SocialMiner Administration Username and Password ECE Web Server Application Instance, Partition Administration Username, and Password Virtualized Voice Browser / Media Gateway Administration Username and Password A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports Customer Virtual Assistant feature. To set a VVB as a Principal VVB, do the following: Important Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. Click the VVB to open the Edit VVB window. Check the Principal check box. Select the required mode. This is the required field. Note For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                                              Gateway'. Click Save . Cisco Contact Center SIP Proxy Administration Username and Password CUIC Publisher Administration Username and Password CVP Windows Administration Username and Password , FTP Enabled, Anonymous Access, FTP Credentials, and Port Note When a CVP (which acts as a Media Server) is updated, Media Server configurations are propagated to all other CVPs across
                                                                        sites. Gateway Administration Username and Password CVP Reporting Windows Administration Username and Password The Deploy check box initializes the CVP Reporting Server configuration. Initialization removes the existing call server association
                                                            and Courtesy Callback configuration. To reassociate the call servers with the CVP Reporting server, see Configure Unified CVP Reporting Server . To reconfigure Courtesy Callback, see Courtesy Callback . IDS Publisher Administration Username and Password Media Server FTP Enabled, Anonymous Access, FTP Credentials, and Port Note When a Media Server is updated, configurations are propagated to all CVPs across sites. Unified CM Publisher AXL Username and Password Cloud Connect Publisher Administration Username and Password Note When a Cloud Connect Publisher is updated,configurations are propagated to all CVPs and Finesse across sites. External HDS Diagnostic Framework Service Domain, Username, and Password | Machine | Editable Field | AW | Diagnostic Framework Service Domain, Username, and Password You can also set a Principal AW machine in 4000 and 12000 Agent deployments. The credentials must be the same for all CCE machines. | Live Data | Administration Username and Password | Finesse | Administration Username and Password | SocialMiner | Administration Username and Password | ECE Web Server | Application Instance, Partition Administration Username, and Password | Virtualized Voice Browser / Media Gateway | Administration Username and Password A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports Customer Virtual Assistant feature. To set a VVB as a Principal VVB, do the following: Important Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. Click the VVB to open the Edit VVB window. Check the Principal check box. Select the required mode. This is the required field. Note For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                                              Gateway'. Click Save . | Important | Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. | Note | For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                                              Gateway'. | Cisco Contact Center SIP Proxy | Administration Username and Password | CUIC Publisher | Administration Username and Password | CVP | Windows Administration Username and Password , FTP Enabled, Anonymous Access, FTP Credentials, and Port Note When a CVP (which acts as a Media Server) is updated, Media Server configurations are propagated to all other CVPs across
                                                                        sites. | Note | When a CVP (which acts as a Media Server) is updated, Media Server configurations are propagated to all other CVPs across
                                                                        sites. | Gateway | Administration Username and Password | CVP Reporting | Windows Administration Username and Password The Deploy check box initializes the CVP Reporting Server configuration. Initialization removes the existing call server association
                                                            and Courtesy Callback configuration. To reassociate the call servers with the CVP Reporting server, see Configure Unified CVP Reporting Server . To reconfigure Courtesy Callback, see Courtesy Callback . | IDS Publisher | Administration Username and Password | Media Server | FTP Enabled, Anonymous Access, FTP Credentials, and Port Note When a Media Server is updated, configurations are propagated to all CVPs across sites. | Note | When a Media Server is updated, configurations are propagated to all CVPs across sites. | Unified CM Publisher | AXL Username and Password | Cloud Connect Publisher | Administration Username and Password Note When a Cloud Connect Publisher is updated,configurations are propagated to all CVPs and Finesse across sites. | Note | When a Cloud Connect Publisher is updated,configurations are propagated to all CVPs and Finesse across sites. | External HDS | Diagnostic Framework Service Domain, Username, and Password |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Machine | Editable Field |
| AW | Diagnostic Framework Service Domain, Username, and Password You can also set a Principal AW machine in 4000 and 12000 Agent deployments. The credentials must be the same for all CCE machines. |
| Live Data | Administration Username and Password |
| Finesse | Administration Username and Password |
| SocialMiner | Administration Username and Password |
| ECE Web Server | Application Instance, Partition Administration Username, and Password |
| Virtualized Voice Browser / Media Gateway | Administration Username and Password A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports Customer Virtual Assistant feature. To set a VVB as a Principal VVB, do the following: Important Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. Click the VVB to open the Edit VVB window. Check the Principal check box. Select the required mode. This is the required field. Note For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                                              Gateway'. Click Save . | Important | Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. | Note | For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                                              Gateway'. |
| Important | Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. |
| Note | For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                                              Gateway'. |
| Cisco Contact Center SIP Proxy | Administration Username and Password |
| CUIC Publisher | Administration Username and Password |
| CVP | Windows Administration Username and Password , FTP Enabled, Anonymous Access, FTP Credentials, and Port Note When a CVP (which acts as a Media Server) is updated, Media Server configurations are propagated to all other CVPs across
                                                                        sites. | Note | When a CVP (which acts as a Media Server) is updated, Media Server configurations are propagated to all other CVPs across
                                                                        sites. |
| Note | When a CVP (which acts as a Media Server) is updated, Media Server configurations are propagated to all other CVPs across
                                                                        sites. |
| Gateway | Administration Username and Password |
| CVP Reporting | Windows Administration Username and Password The Deploy check box initializes the CVP Reporting Server configuration. Initialization removes the existing call server association
                                                            and Courtesy Callback configuration. To reassociate the call servers with the CVP Reporting server, see Configure Unified CVP Reporting Server . To reconfigure Courtesy Callback, see Courtesy Callback . |
| IDS Publisher | Administration Username and Password |
| Media Server | FTP Enabled, Anonymous Access, FTP Credentials, and Port Note When a Media Server is updated, configurations are propagated to all CVPs across sites. | Note | When a Media Server is updated, configurations are propagated to all CVPs across sites. |
| Note | When a Media Server is updated, configurations are propagated to all CVPs across sites. |
| Unified CM Publisher | AXL Username and Password |
| Cloud Connect Publisher | Administration Username and Password Note When a Cloud Connect Publisher is updated,configurations are propagated to all CVPs and Finesse across sites. | Note | When a Cloud Connect Publisher is updated,configurations are propagated to all CVPs and Finesse across sites. |
| Note | When a Cloud Connect Publisher is updated,configurations are propagated to all CVPs and Finesse across sites. |
| External HDS | Diagnostic Framework Service Domain, Username, and Password |
| Step 2 | Edit the credentials. If successful, you can see the message on the Inventory page; else, fix the errors that are shown before clicking Save . |

| Machine | Editable Field |
|---|---|
| AW | Diagnostic Framework Service Domain, Username, and Password You can also set a Principal AW machine in 4000 and 12000 Agent deployments. The credentials must be the same for all CCE machines. |
| Live Data | Administration Username and Password |
| Finesse | Administration Username and Password |
| SocialMiner | Administration Username and Password |
| ECE Web Server | Application Instance, Partition Administration Username, and Password |
| Virtualized Voice Browser / Media Gateway | Administration Username and Password A VVB can be set as a Principal VVB provided its Sync Status is "In Sync" and it supports Customer Virtual Assistant feature. To set a VVB as a Principal VVB, do the following: Important Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. Click the VVB to open the Edit VVB window. Check the Principal check box. Select the required mode. This is the required field. Note For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                                              Gateway'. Click Save . | Important | Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. | Note | For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                                              Gateway'. |
| Important | Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. |
| Note | For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                                              Gateway'. |
| Cisco Contact Center SIP Proxy | Administration Username and Password |
| CUIC Publisher | Administration Username and Password |
| CVP | Windows Administration Username and Password , FTP Enabled, Anonymous Access, FTP Credentials, and Port Note When a CVP (which acts as a Media Server) is updated, Media Server configurations are propagated to all other CVPs across
                                                                        sites. | Note | When a CVP (which acts as a Media Server) is updated, Media Server configurations are propagated to all other CVPs across
                                                                        sites. |
| Note | When a CVP (which acts as a Media Server) is updated, Media Server configurations are propagated to all other CVPs across
                                                                        sites. |
| Gateway | Administration Username and Password |
| CVP Reporting | Windows Administration Username and Password The Deploy check box initializes the CVP Reporting Server configuration. Initialization removes the existing call server association
                                                            and Courtesy Callback configuration. To reassociate the call servers with the CVP Reporting server, see Configure Unified CVP Reporting Server . To reconfigure Courtesy Callback, see Courtesy Callback . |
| IDS Publisher | Administration Username and Password |
| Media Server | FTP Enabled, Anonymous Access, FTP Credentials, and Port Note When a Media Server is updated, configurations are propagated to all CVPs across sites. | Note | When a Media Server is updated, configurations are propagated to all CVPs across sites. |
| Note | When a Media Server is updated, configurations are propagated to all CVPs across sites. |
| Unified CM Publisher | AXL Username and Password |
| Cloud Connect Publisher | Administration Username and Password Note When a Cloud Connect Publisher is updated,configurations are propagated to all CVPs and Finesse across sites. | Note | When a Cloud Connect Publisher is updated,configurations are propagated to all CVPs and Finesse across sites. |
| Note | When a Cloud Connect Publisher is updated,configurations are propagated to all CVPs and Finesse across sites. |
| External HDS | Diagnostic Framework Service Domain, Username, and Password |

| Important | Do not perform any Customer Virtual Assistant configurations while setting a different VVB as a Principal VVB. |
|---|---|

| Note | For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                                              Gateway'. |
|---|---|

| Note | When a CVP (which acts as a Media Server) is updated, Media Server configurations are propagated to all other CVPs across
                                                                        sites. |
|---|---|

| Note | When a Media Server is updated, configurations are propagated to all CVPs across sites. |
|---|---|

| Note | When a Cloud Connect Publisher is updated,configurations are propagated to all CVPs and Finesse across sites. |
|---|---|

| Note | IP address/hostname change or rebuild can only be done from Principal AW machine. Ensure that the Principal AW user is part
                                             of the local Administrators group on all CCE machines. If you have rebuilt a CCE_ROGGER or a CCE_AW, do not create a service account manually. Side A AW user account will be used
                                             as a service account for Logger and distributor services. After updating the hostname in the virtual machine, upload the CA certificates or import the self-signed certificates into
                                             the machine. This should be done before updating the hostname in the inventory. |
|---|---|

| Machines | Task |
|---|---|
| Core Machines CCE_AW, CCE_ROGGER 4 , CCE_ROUTER 5 , CCE_LOGGER 6 , CUIC_PUBLISHER, CUIC_SUBSCRIBER, IDS_PUBLISHER, IDS_SUBSCRIBER, and LIVE_DATA | Update Core Machines |
| Peripheral Set Machines CCE_PG, CM_PUBLISHER, CM_SUBSCRIBER, FINESSE_PRIMARY, FINESSE_SECONDARY, and CVP | Update Peripheral Set |
| Optional Machines CVVB, CVP_REPORTING, MEDIA_SERVER, GATEWAY, EXTERNAL_HDS, CUSTOMER_COLLABORATION_PLATFORM, CCCSP , THIRD_PARTY_MULTICHANNEL, ECE, ECE_WEB_SERVER, CLOUD_CONNECT_PUB, and CLOUD_CONNECT_SUB | Update Optional Machines Note After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. | Note | After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. |
| Note | After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. |

| Note | After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. |
|---|---|

| Note | If you have changed the hostname of CCE_ROGGER or CCE_ROUTER in the respective virtual machines, restart the Apache Tomcat
                                             service on Principal AW. This should be done before updating the inventory with new hostname for these machines. |
|---|---|

| Step 1 | Navigate to the Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Choose Update > Core Machines . |
| Step 3 | Click the Download Present Inventory File icon to get the Inventory File. |
| Step 4 | Fill particulars in the Inventory File and save it. For more information, see Inventory File . |
| Step 5 | Click the Upload Updated Inventory File icon to import the updated file. |
| Step 6 | Click Next to start the inventory update process and see the progress of tasks. If the upload is successful, a green circle appears against each task. If the upload is unsuccessful, fix the errors shown, and repeat steps 5 and 6. |
| Step 7 | Click Done . |

| Note | Before updating the IP address or hostname for Cloud Connect Subscriber, disable auto discovery in the virtual machine. For
                                                   more information, see Auto Discovery . After updating the IP address or hostname in the inventory for CVP Reporting Server, restart this device. |
|---|---|

| Step 1 | Navigate to the Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Choose Update > Optional Machines . |
| Step 3 | Click the Download Present Inventory File icon to get the Inventory File. |
| Step 4 | Fill particulars in the Inventory File and save it. For more information, see Inventory File . |
| Step 5 | Click the Upload Updated Inventory File icon to import the updated file. |
| Step 6 | Click Next to start the inventory update process and see the progress of tasks. If the upload is successful, a green circle appears against each task. If the upload is unsuccessful, fix the errors shown, and repeat steps 5 and 6. |
| Step 7 | Click Done . |

| Note | While updating the inventory file, ensure to refer to the Machine Dependencies . If you are updating hostname for any of the following machines, restart Apache Tomcat service on all CCE_AW machines after
                                                the inventory update: CCE_AW FINESSE EXTERNAL_HDS CUIC |
|---|---|

| Column | Description | Required for upload? | Editable in downloaded inventory file? | Permissible Values |
|---|---|---|---|---|
| name | Unique identifier for the machine | Yes | No |  |
| machine Type | Machine Type | Yes | No | Core machines are: CCE_AW, CCE_ROGGER 7 , CCE_ROUTER 8 , CCE_LOGGER 9 , CUIC_PUBLISHER, CUIC_SUBSCRIBER, IDS_PUBLISHER, IDS_SUBSCRIBER, and LIVE_DATA Peripheral set machines are: CCE_PG, CM_PUBLISHER, CM_SUBSCRIBER, FINESSE_PRIMARY, FINESSE_SECONDARY, and CVP Optional machines are: CVVB, CVP_REPORTING, MEDIA_SERVER, GATEWAY, EXTERNAL_HDS, CUSTOMER_COLLABORATION_PLATFORM, CCCSP , THIRD_PARTY_MULTICHANNEL, ECE, ECE_WEB_SERVER, CLOUD_CONNECT_PUB, and CLOUD_CONNECT_SUB |
| public Address | Public address | Yes | No | IP address or hostname of machines present in the inventory |
| private Address | Private address | Required for CCE_PG, CCE_ROGGER, CCE_ROUTER, and CCE_LOGGER | No | IP address or hostname of machines present in the inventory |
| side | Side information | Yes | No | sideA sideB |
| connection Info | Connection information of the machine | Required for CCE_AW, CCE_PG (Side A) CM_PUBLISHER, CUIC_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, CCCSP , GATEWAY, IDS_PUBLISHER, LIVE_DATA, EXTERNAL_HDS, CLOUD CONNECT PUBLISHER, CVVB, MEDIA_SERVER, CUSTOMER_ COLLABORATION_ PLATFORM ConnectionInfo is mandatory for the machines even if: There is no IP address or hostname change. The isReinstalled value is set to No . | Yes (only username and password are editable) | Enter the username and password in the following format: userName=<user>&password=<password> Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL-encoded values "%26" or "%3D". For information on the credentials of machines, see Table 1 . For CCE_PG update, provide the userName and password of CUCM application user. Note If you change the CUCM application user, update the inventory for both Side A and Side B CCE_PGs and set the isReinstalled value to yes . This makes sure that both sides of the PG machines have the same application user. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway | Note | If you change the CUCM application user, update the inventory for both Side A and Side B CCE_PGs and set the isReinstalled value to yes . This makes sure that both sides of the PG machines have the same application user. |
| Note | If you change the CUCM application user, update the inventory for both Side A and Side B CCE_PGs and set the isReinstalled value to yes . This makes sure that both sides of the PG machines have the same application user. |
| newpublic Address | new Public address | Yes | Yes | For IP address change: provide the new IP address For IP address and hostname change: provide the new IP address. The new hostname is auto detected and updated in the inventory. For hostname change: provide the new IP address same as the old IP address. The new hostname is auto detected and updated
                                          in the inventory. |
| newprivate Address | new Private address | Required for CCE_ROUTER, CCE_LOGGER, CCE_ROGGER,CCE_PG | Yes |
| is Reinstalled | is Reinstalled | Yes | Yes | Supported values are: Yes : if you are setting up a new virtual machine No : if you are using the existing virtual machine |

| Note | If you change the CUCM application user, update the inventory for both Side A and Side B CCE_PGs and set the isReinstalled value to yes . This makes sure that both sides of the PG machines have the same application user. |
|---|---|

| Note | Each row in the table below specifies machines types that are dependent on each other. So, whenever you update a machine,
                                             ensure to provide other dependent machine types from the same row. |
|---|---|

| Dependent Machine Types |
|---|
| CCE_AW (include all AWs), CCE_ROGGER 10 , CCE_LOGGER, and CCE_ROUTER 11 |
| CCE_PG, CM_PUBLISHER 12 , CM_SUBSCRIBER, FINESSE_PRIMARY, and FINESSE_SECONDARY |
| CCE_PG and CVP (include all CVPs in the peripheral set) |
| ECE and ECE_WEB_SERVER |

| Note | Provide both publisher and subscriber details of a machine together. For example: CUIC_PUBLISHER and CUIC_SUBSCRIBER. Provide Side A and Side B details of a machine together. For example: CVP Side A and CVP Side B. If you are updating the IP address/hostname or rebuilding a CCE_PG, provide details of all PG client types (configured in
                                                the system), and dependent machine types in the inventory file. For example: If VRU and Multichannel PGs are configured in
                                                the system, provide side A and side B details for both the PGs and all CVP machines. If only MR PG is configured in the system, provide side A and side B details of this PG in the inventory file. |
|---|---|

| Note | When a Cloud Connect Publisher is deleted, the corresponding Cloud Connect Subscriber is also deleted. You cannot delete the Principal VVB. For the Prinicipal VVB, the mode must be either 'Virtualized Voice Browser' only or both 'Virtualized Voice Browser and Media
                                                Gateway'. When a Media Server is deleted, configurations are propagated to all CVPs across sites. |
|---|---|

| Step 1 | To delete a machine individually, select that particular row and click Delete (X) icon at the end of the row. |
|---|---|
| Step 2 | Click Yes . If the deletion is successful, then a message is displayed that the machine was deleted successfully. If the deletion fails,
                                       then check the error message and resolve the issue before attempting to delete again. |

| Caution | Before performing the step to enable the secured connection between the components, ensure that the security certificate management
                                          process is completed. |
|---|---|

| Step 1 | In the Peripheral Gateway Component Properties window, click Add . |
|---|---|
| Step 2 | From the Client Type drop-down list, select Media Routing . |
| Step 3 | From the Available PIMS list, select MR PIM1 , then click OK . |
| Step 4 | In the Configuration dialog box, check the Enabled check box. |
| Step 5 | In the Peripheral name field, enter the peripheral name. |
| Step 6 | In the Peripheral ID field, enter the logical controller ID of the Unified CCE component you are adding. The following are the names by which
                                       the Unified CCE components are represented in the database. Refer PG explorer tool using Configuration Manager to get the
                                       Peripheral ID of the corresponding PIM. Name of Outbound is Outbound Name of ECE is MR1 Name of CCP is MR2 Name of THIRD_PARTY_MULTICHANNEL is MR3 Name of Digital Routing is MR4 Example: If you are adding ECE, find the component of the name MR1 in the database. Enter the logical controller ID of that component in the Peripheral ID field. |
| Step 7 | In the Application Hostname (1) field, enter the hostname or the IP address of ECE services server. |
| Step 8 | In the Application connection port (1) field, enter the port number. Note Use the port number that is on the ECE services server that PIM uses to communicate with the application. The default port is 38001. | Note | Use the port number that is on the ECE services server that PIM uses to communicate with the application. The default port is 38001. |
| Note | Use the port number that is on the ECE services server that PIM uses to communicate with the application. The default port is 38001. |
| Step 9 | In the Application Hostname (2) field, leave the field blank. |
| Step 10 | In the Application connection port (2) field, leave the field blank. |
| Step 11 | In the Heartbeat interval (sec) field, enter 5 . |
| Step 12 | In the Reconnect interval (sec) field, enter 10 . |
| Step 13 | Check the Enable Secured Connection option. This establishes a secured connection between the MR PIM and the application server. Ensure that you provide the correct information in the Application Hostname(1) and Application Connection Port(1) fields. |
| Step 14 | Click OK . |

| Note | Use the port number that is on the ECE services server that PIM uses to communicate with the application. The default port is 38001. |
|---|---|

| Step 1 | Navigate to the Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Go to Import > Peripheral Set to add a peripheral set. The New Peripheral Set wizard opens. |
| Step 3 | Click Download Template . |
| Step 4 | Fill the particulars in the file and save it. Table 5. CSV Template Details Column Description Required? Permissible Values name Unique identifier for the machine Yes Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         underscore (_), or hyphen (-). machineType MachineType Enum name Yes Mandatory machine is CCE_PG. Optional machines are: CVP FINESSE_PRIMARY FINESSE_SECONDARY CM_PUBLISHER CM_SUBSCRIBER MEDIA_SERVER publicAddress Public address Yes Valid IP address or hostname connectionInfo Connection information of the machine Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, CCCSP , GATEWAY and LIVE_DATA Enter the username and password in the following format: userName=<user>&password=<password> ConnectionInfo is optional if you are configuring FTP for CVP (Media Server) . Append the FTP attributes to the username and password in the following format: userName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway privateAddress Private address Optional Valid IP address or hostname peripheralSetName Peripheral set name Required for PG, CUCM, Finesse, CVP Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         or an underscore (_). Note Name must be unique. It cannot be reused even after that peripheral set is deleted. side Side information Yes sideA sideB | Column | Description | Required? | Permissible Values | name | Unique identifier for the machine | Yes | Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         underscore (_), or hyphen (-). | machineType | MachineType Enum name | Yes | Mandatory machine is CCE_PG. Optional machines are: CVP FINESSE_PRIMARY FINESSE_SECONDARY CM_PUBLISHER CM_SUBSCRIBER MEDIA_SERVER | publicAddress | Public address | Yes | Valid IP address or hostname | connectionInfo | Connection information of the machine | Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, CCCSP , GATEWAY and LIVE_DATA | Enter the username and password in the following format: userName=<user>&password=<password> ConnectionInfo is optional if you are configuring FTP for CVP (Media Server) . Append the FTP attributes to the username and password in the following format: userName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway | Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. | privateAddress | Private address | Optional | Valid IP address or hostname | peripheralSetName | Peripheral set name | Required for PG, CUCM, Finesse, CVP | Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         or an underscore (_). Note Name must be unique. It cannot be reused even after that peripheral set is deleted. | Note | Name must be unique. It cannot be reused even after that peripheral set is deleted. | side | Side information | Yes | sideA sideB |
| Column | Description | Required? | Permissible Values |
| name | Unique identifier for the machine | Yes | Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         underscore (_), or hyphen (-). |
| machineType | MachineType Enum name | Yes | Mandatory machine is CCE_PG. Optional machines are: CVP FINESSE_PRIMARY FINESSE_SECONDARY CM_PUBLISHER CM_SUBSCRIBER MEDIA_SERVER |
| publicAddress | Public address | Yes | Valid IP address or hostname |
| connectionInfo | Connection information of the machine | Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, CCCSP , GATEWAY and LIVE_DATA | Enter the username and password in the following format: userName=<user>&password=<password> ConnectionInfo is optional if you are configuring FTP for CVP (Media Server) . Append the FTP attributes to the username and password in the following format: userName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway | Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| privateAddress | Private address | Optional | Valid IP address or hostname |
| peripheralSetName | Peripheral set name | Required for PG, CUCM, Finesse, CVP | Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         or an underscore (_). Note Name must be unique. It cannot be reused even after that peripheral set is deleted. | Note | Name must be unique. It cannot be reused even after that peripheral set is deleted. |
| Note | Name must be unique. It cannot be reused even after that peripheral set is deleted. |
| side | Side information | Yes | sideA sideB |
| Step 5 | Upload the file and click Next . |
| Step 6 | Wait for validation to be completed and click Done . During the validation, tasks are performed depending on the components defined in the CSV template. If validation fails, then click Back to fix the issues in the file and upload it again. Note Agent PG and PIMs are created only when Finesse and CUCM are
                                                               present. Multichannel PGs are created. For adding PIMs, see the section "Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment". VRU PG and PIMs are created only when CVP is present. Only one peripheral set must be created at a time. Live Data Configuration Services, TIP_PG and TIP_PG_TOS will be
                                                               added in Machine_Service table only for Agent PG. | Note | Agent PG and PIMs are created only when Finesse and CUCM are
                                                               present. Multichannel PGs are created. For adding PIMs, see the section "Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment". VRU PG and PIMs are created only when CVP is present. Only one peripheral set must be created at a time. Live Data Configuration Services, TIP_PG and TIP_PG_TOS will be
                                                               added in Machine_Service table only for Agent PG. |
| Note | Agent PG and PIMs are created only when Finesse and CUCM are
                                                               present. Multichannel PGs are created. For adding PIMs, see the section "Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment". VRU PG and PIMs are created only when CVP is present. Only one peripheral set must be created at a time. Live Data Configuration Services, TIP_PG and TIP_PG_TOS will be
                                                               added in Machine_Service table only for Agent PG. |

| Column | Description | Required? | Permissible Values |
|---|---|---|---|
| name | Unique identifier for the machine | Yes | Name must start with an alphabet. Maximum length is limited to 128 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         underscore (_), or hyphen (-). |
| machineType | MachineType Enum name | Yes | Mandatory machine is CCE_PG. Optional machines are: CVP FINESSE_PRIMARY FINESSE_SECONDARY CM_PUBLISHER CM_SUBSCRIBER MEDIA_SERVER |
| publicAddress | Public address | Yes | Valid IP address or hostname |
| connectionInfo | Connection information of the machine | Required for CM_PUBLISHER, FINESSE_PRIMARY, ECE_WEB_SERVER, CVP, CVP_REPORTING, CVVB, CCCSP , GATEWAY and LIVE_DATA | Enter the username and password in the following format: userName=<user>&password=<password> ConnectionInfo is optional if you are configuring FTP for CVP (Media Server) . Append the FTP attributes to the username and password in the following format: userName=<user>&password=<password>;
ftpEnabled=<true or false>
&ftpUserName=<ftp_username>
&ftpPassword=<ftp_password>
&ftpPort=<ftp_portnumber> For more information on the FTP attributes, see FTP Section in the Add Media Server as External Machine . Note Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. For CVVB, append the mode to the username and password in the following format: info:userName=<user>&password=<password>&mode=<mode> Enter one of the following expected value for mode: VVB: For Virtualised Voice Browser MGW: For Media Gateway VVB_MGW: For both Virtualised Voice Browser and Media Gateway | Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
| privateAddress | Private address | Optional | Valid IP address or hostname |
| peripheralSetName | Peripheral set name | Required for PG, CUCM, Finesse, CVP | Name can start with an alphabet. Maximum length is limited to 10 characters. Valid characters are a-z, A-Z, 0-9, dot (.),
                                                         or an underscore (_). Note Name must be unique. It cannot be reused even after that peripheral set is deleted. | Note | Name must be unique. It cannot be reused even after that peripheral set is deleted. |
| Note | Name must be unique. It cannot be reused even after that peripheral set is deleted. |
| side | Side information | Yes | sideA sideB |

| Note | Replace Ampersand (&) or equal sign (=) in usernames or passwords with their respective URL encoded values "%26" or "%3D". Semicolon (;) delimits the Windows Administration credentials from FTP credentials. |
|---|---|

| Note | Name must be unique. It cannot be reused even after that peripheral set is deleted. |
|---|---|

| Note | Agent PG and PIMs are created only when Finesse and CUCM are
                                                               present. Multichannel PGs are created. For adding PIMs, see the section "Add Multichannel PIM to Packaged CCE 4000/12000 Agents Deployment". VRU PG and PIMs are created only when CVP is present. Only one peripheral set must be created at a time. Live Data Configuration Services, TIP_PG and TIP_PG_TOS will be
                                                               added in Machine_Service table only for Agent PG. |
|---|---|

| Note | After updating the IP address or hostname in the Inventory for CVP, restart the CVP device. |
|---|---|

| Step 1 | Navigate to the Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Go to Import > Device > Add Machine to add a machine to a peripheral set. The Add Machine wizard is displayed. |
| Step 3 | Click Download Template . The .csv template is downloaded. |
| Step 4 | Fill the particulars in the .csv template file and save it in the local folder. For more information, see Add and Maintain Peripheral Set . |
| Step 5 | Upload the .csv template file and click Next . |
| Step 6 | Click Done . |

| Step 1 | Navigate to Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | Select the peripheral set from main or remote site that you want to delete and click Delete > Peripheral Set . The Delete Peripheral Set from <site name> popup window appears. |
| Step 3 | Select a peripheral set from the Peripheral Set drop-down list. |
| Step 4 | Click Delete . |
| Step 5 | Click Back to delete another peripheral set. Else, click Done to return to the Inventory page. |

| Sequence | ICM-to-ICM Gateway Configuration Tasks |
|---|---|
| 1 | Configure ICM-to-ICM Gateway For more information, see ICM to ICM Gateway User Guide for Unified CCE at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
| 2 | Remote ICM type application gateway global settings |

| Name | Value |
|---|---|
| Abandon Timeout. | 5000 |
| ApplicationGatewayType | 1 |
| DateTimeStamp | NULL |
| ChangeStamp | 0 |
| ErrorThreshold | 10 |
| HeartbeatLimit | 2 |
| HeartbeatRetry | 200 |
| HeartbeatTimeout | 300 |
| HeartbeatInterval | 15000 |
| ID | 2 |
| LateTimeout | 400 |
| LinkTestThreshold | 2 |
| OpenTimeout | 500 |
| RequestTimeout | 500 |
| SessionRetry | 30000 |
| SessionRetryLimit | 0 |

| Note | You can add SocialMiner , MediaSense and Cloud Connect only in the main site. |
|---|---|