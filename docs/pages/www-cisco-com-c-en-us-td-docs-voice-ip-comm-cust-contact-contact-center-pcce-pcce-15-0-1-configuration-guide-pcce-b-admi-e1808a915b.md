---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-15-0-1-configuration-guide-pcce-b-admi-e1808a915b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_15_0_1/configuration/guide/pcce_b_admin-and-config-guide-15_0_1/pcce-m-custom-sql-server-port.html
retrieved_at: 2026-08-21T16:50:00.123346+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 15.0(1)

Updated: July 31, 2026

Chapter: Custom SQL Server Port

## Chapter: Custom SQL Server Port

- Custom SQL Server Port

- Configuring Custom SQL Server Port

- Configuring Custom SQL Server Port During Packaged CCE 2000 Agents Fresh Install

# Custom SQL Server Port

## Configuring Custom SQL Server Port

Pre-requisites:

Install the following ES or later cummulative ES releases based on the respective components:

15.0(1) ES202607 for Logger and Rogger

15.0(1) SU2 for Cisco Finesse

15.0(1) SU2 for Cisco Cloud Connect (for Digital Channels)

15.0(1) SU2 for Cisco Unified Intelligence Center

15.0(1) ES202607 for Enterprise Chat and Email (ECE) and Contact Center Management Portal (CCMP)

Download the ' SQL Port Update ' utility from CCO at https://software.cisco.com/download/home/268439622/type/284420243/release/15.0(1) . Extract the package on the ICM nodes (for example C:\SQLPortUpdate ); it contains the ' SQLPortUpdate.exe ' and ' Config.psd1 ' files.

Right click the ' Config.psd1 ' file and click Edit .

Update the ' Config.psd1 ' file with the following information:

FQDN of the Logger/Rogger Side A and Side B

FQDN of Administration & Data Servers

FQDN of Administration Client

You must have the Administrator user privilege to run this 'SQLPortUpdate.exe' file.

If Administration Client is installed on a Windows Client OS (e.g. Windows 11), you must enable remote registry service manually
                                             on that machine. If this is not possible for any reason, you must run the ' SQLPortUpdate.exe ' file manually on those machine(s).

Run the ' SQLPortUpdate.exe ' file on Windows PowerShell with the ' -setup ' parameter on Logger/Rogger Side A to create required registries with the default port 1433 for all components specified
                                 in ' Config.psd1 '.

For example:

To configure and manage custom SQL Server port for Logger/Rogger, Administration & Data Servers, do the following:

### Step 1. Configure Custom SQL Port for Logger/Rogger Side A

Initiate maintenance mode on Logger/Rogger Side A.

For more information about bringing the Packaged CCE components to maintenance mode, see the Invoking Maintenance Mode topic in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Once the Logger/Rogger Side A services are stopped, now stop the SQL Server, SQL Server Agent, and Tomcat services.

Change the service start up type from Automatic to Manual if it is not set to Manual for all the above services.

Open the SQL Server Configuration Manager, navigate to SQL Server Network Configuration > Protocols for MSSQLSERVER > TCP/IP . The TCP/IP Properties dialog box appears.

Click the IP Addresses tab and go to IPAll section, specify the custom SQL server port.

Click Ok .

Run the 'SQLPortUpdate.exe' file on Windows PowerShell with the '-configure' parameter and follow the instructions to update
                                    custom port.

Revert the service type to Automatic only if it was changed to manual in Step 2 of this topic.

Reboot and start the Logger/Rogger Side A.

### Step 2. Configure Custom SQL Server Port for Primary Administration & Data Servers (Side A for Packaged CCE 2000 Agent Deployment)

The custom SQL server port change made to the Primary Administration & Data Servers impacts the Cisco Finesse, CUIC, Live
                              Data, and Administration Client.

Only for Packaged CCE 2000 agent deployment, consider Primary as Side A and Secondary as Side B.

Initiate maintenance mode on Primary Administration & Data Servers.

Now the Secondary Administration & Data Servers will handle the traffic of Cisco Finesse, CUIC, Live Data, and Administration
                                    Client.

Once the Distributor service is stopped, now stop the SQL Server, SQL Server Agent, and Tomcat services.

Change the service start up type from Automatic to Manual if it is not set to Manual for all the above services.

Open the SQL Server Configuration Manager, navigate to SQL Server Network Configuration > Protocols for MSSQLSERVER > TCP/IP .

The TCP/IP Properties dialog box appears.

Click the IP Addresses tab and go to IPAll section, specify the custom SQL server port.

Click Ok

Run the 'SQLPortUpdate.exe' file on Windows PowerShell with the '-configure' parameter and follow the instructions to update
                                    required custom SQL port registries.

Revert the service type to Automatic only if it is changed to manual in Step 2 of this topic.

Reboot and start the Primary Administration & Data Servers.

Update Primary Administration & Data Servers custom SQL port details to all the dependent Packaged CCE components.

Cisco Finesse Publisher

Open the Cisco Finesse Administrator Console.

In the Contact Center Enterprise Administration & Data Server Settings section, specify the custom SQL server port to the Primary Database Port and Secondary Database Port fields.

Perform Cisco Finesse maintenance mode.

For more information, see the Perform Routine Maintenance chapter in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

This will move all agents to subscriber.

Restart Finesse Tomcat.

Cisco Finesse Subscriber :

Initiate Cisco Finesse maintenance mode.

For more information about maintenance mode, see the Perform Routine Maintenance chapter in Cisco Finesse Administration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-maintenance-guides-list.html .

This will move all agents to Publisher.

Restart Finesse Tomcat.

Live Data (LD) Publisher

For non-Packaged CCE 2000 agent deployment, on the Publisher LD, update the Primary AW access information section with the custom SQL server port.

Changes made to Publisher LD, automatically gets synchronized to Subscriber LD.

CUIC Publisher

For non-Packaged CCE 2000 agent deployment, navigate to the Unified Intelligence Center Administration Console and click Configure .

Select Data Sources .

For all the data source configured with CCE database, update only the Primary Administration & Data Servers port in CUIC data
                                                source configuration.

Cloud Connect : The custom SQL Server port for the Primary Administration and Data Servers is updated automatically in the Digital Routing
                                          service container.

Enterprise Chat and Email (ECE) : For more information, see the SQL Always-On Configuration chapter in the Enterprise Chat and Email Installation and Configuration Guide, Release 15.0 .

Contact Center Management Portal (CCMP) : For more information, see the Update SQL Server Port chapter in the Installation and Configuration Guide for Cisco Unified Contact Center Management Portal, Release 15(202607) .

### Step 3. Configure Custom SQL Server Port for Logger/Rogger Side B

To configure custom SQL server port for Logger/Rogger Side B, do the following:

Initiate maintenance mode on Logger/Rogger Side B.

For more information about bringing the Packaged CCE components to maintenance mode, see the Invoking Maintenance Mode topic in the Cisco Packaged Contact Center Enterprise Administration and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-maintenance-guides-list.html .

Once the Logger/Rogger Side B services are stopped, now stop the SQL Server, SQL Server Agent, and Tomcat services.

Change the service start up type from Automatic to Manual if it is not set to Manual for all the above services.

Open the SQL Server Configuration Manager, navigate to SQL Server Network Configuration > Protocols for MSSQLSERVER > TCP/IP . The TCP/IP Properties dialog box appears.

Click the IP Addresses tab and go to IPAll section, specify the custom SQL server port.

Click Ok

Run the 'SQLPortUpdate.exe' file on Windows PowerShell with the '-configure' parameter and follow the instructions to update
                                    custom port.

Revert the service type to Automatic only if it was changed to manual in Step 2 of this topic.

Reboot and start the Logger/Rogger Side B.

### Step 4. Configure Custom SQL Server Port for Primary Administration & Data Servers (Side B for Packaged CCE 2000 Agent Deployment)

The custom SQL server port change made to the Secondary Administration & Data Servers impacts the Cisco Finesse, CUIC, Live
                              Data, and Administration Client.

Only for Packaged CCE 2000 agent deployment, consider Primary as Side A and Secondary as Side B.

Initiate maintenance mode on Secondary Administration & Data Servers.

Now the Primary Administration & Data Servers will handle the traffic of Cisco Finesse, CUIC, Live Data, and Administration
                                    Client.

Once the Distributor service is stopped, now stop the SQL Server, SQL Server Agent, and Tomcat services.

Change the service start up type from Automatic to Manual if it is not set to Manual for all the above services.

Open the SQL Server Configuration Manager, navigate to SQL Server Network Configuration > Protocols for MSSQLSERVER > TCP/IP .

The TCP/IP Properties dialog box appears.

Click the IP Addresses tab and go to IPAll section, specify the custom SQL server port.

Click Ok

Run the 'SQLPortUpdate.exe' file on Windows PowerShell with the '-configure' parameter and follow the instructions to update
                                    required custom SQL port registries.

Revert the service type to Automatic only if it is changed to manual in Step 2 of this topic.

Reboot and start the Secondary Administration & Data Servers.

Update Secondary Administration & Data Servers custom SQL port details to all the dependent Packaged CCE components.

Live Data (LD) Publisher

For non-Packaged CCE 2000 agent deployment, on the Publisher LD, update the Secondary AW access information section with the custom SQL server port.

Changes made to Publisher LD, automatically gets synchronized to Subscriber LD.

CUIC Publisher

For non-Packaged CCE 2000 agent deployment, navigate to the Unified Intelligence Center Administration Console and click Configure .

Select Data Sources .

For all the data source configured with CCE database, update only the Secondary Administration & Data Servers port in CUIC
                                                data source configuration.

Cloud Connect : The custom SQL Server port for the Primary Administration and Data Servers is updated automatically in the Digital Routing
                                          service container.

Enterprise Chat and Email (ECE) : For more information, see the SQL Always-On Configuration chapter in the Enterprise Chat and Email Installation and Configuration Guide, Release 15.0 .

Contact Center Management Portal (CCMP) : For more information, see the Update SQL Server Port Chapter in the Installation and Configuration Guide for Cisco Unified Contact Center Management Portal, Release 15(202607) .

## Configuring Custom SQL Server Port During Packaged CCE 2000 Agents Fresh Install

The Packaged CCE 2000 Agents deployment fresh installation workflow supports both default (1433) and non-default SQL Server
                              ports. For a deployment that uses the default SQL Server port, no additional configuration is required because the installer
                              uses port 1433 by default.

During a Packaged CCE 2000 Agents fresh install, configure custom SQL Server ports by specifying them in the pcce2k_Inventory_Custom.csv inventory file. The CSV format includes an optional SQL Server configuration entry that allows you to specify the SQL Server
                              port for each applicable VM, such as Rogger A, Rogger B, AW1, and AW2. If no port value is provided, the system assumes port 1433 .

Other than the CSV inventory update, the overall fresh install workflow remains unchanged. After the pcce2k_Inventory_Custom.csv inventory file is uploaded and validated, you can continue with the remaining installation steps.

### Before you begin

Install the 15.0(1) ES202607 installer or later cumulative ES release for the Packaged CCE 2000 Agents deployment.

Verify that you can log in as a member of the Config security group.

Identity whether the deployment uses the default SQL Server port or custom SQL Server ports.

Record the SQL Server port values for each applicable Virtual Machine (VM).

Populate the pcce2k_Inventory_Custom.csv inventory file with the SQL Server port information for each applicable VM.

Step 1

On the Administration & Data Server desktop, open the Unified CCE Tools folder and navigate to Administration Tools > CCE Web Administration .

Step 2

Log in as a Config security group member in the format user@domain .

Step 3

Navigate to Unified CCE Administration > Overview > Infrastructure Settings > Deployment Type .

Step 4

Click Configure your deployment .

Step 5

On the Deployment page, perform the following:

Select Packaged CCE 2000 Agents from the Deployment drop-down list.

Select the required instance from the drop-down list.

Click Next .

Step 6

On the Inventory page, perform the following:

Click Download template to download the inventory template pcce2k_Inventory_Custom.csv file.

Populate all required VM details in the pcce2k_Inventory_Custom.csv file.

Provide VM details in the corresponding fields such as operation, name, machineType, publicAddress, publicAddressServices,
                                                privateAddress, and other required values.

The type=SQL_SERVER&port=<non-default port> parameter of publicAddressServices field denotes the port number of the SQL Server used by the VM. If this parameter is not specified for a VM, the default
                                                SQL port 1433 is used to connect to the SQL service of that VM.

To specify custom SQL port in the CSV file, add type=SQL_SERVER&port=<non-default port> . For example: type=SQL_SERVER&port=1534

Enter the custom SQL port for all CCE VMs, such as Rogger A or Rogger B and AW1 or AW2, that have SQL Server running on a
                                                custom port.

In the Content File field, click Choose File to import the CSV file from your local folder.

Click Next .

If the validation fails, verify the VM parameters and field values, and then retry the validation process.

Step 7

On the Settings page, perform the following:

Select the required values from the drop-down list for each Rogger and Service Account field.

Click Next .

Step 8

On the Initialize page, the fresh install task is triggered.

Step 9

Click Next to deploy Packaged CCE 2000 Agents.

The Packaged CCE 2000 Agents deployment Fresh Install workflow applies the SQL Server port values that you provided in the pcce2k_Inventory_Custom.csv file.

For standard deployments, the installer continues to use SQL Server port 1433 . For deployments that use custom SQL Server ports, each applicable component uses the configured non-default port values
                              provided in the Packaged CCE 2000 Agents deployment pcce2k_Inventory_Custom.csv file.

| Note | You must have the Administrator user privilege to run this 'SQLPortUpdate.exe' file. If Administration Client is installed on a Windows Client OS (e.g. Windows 11), you must enable remote registry service manually
                                             on that machine. If this is not possible for any reason, you must run the ' SQLPortUpdate.exe ' file manually on those machine(s). |
|---|---|

| Note | Only for Packaged CCE 2000 agent deployment, consider Primary as Side A and Secondary as Side B. |
|---|---|

| Note | Changes made to Publisher LD, automatically gets synchronized to Subscriber LD. |
|---|---|

| Note | Changes made to Publisher CUIC, automatically gets synchronized to Subscriber CUIC. |
|---|---|

| Note | Only for Packaged CCE 2000 agent deployment, consider Primary as Side A and Secondary as Side B. |
|---|---|

| Note | Changes made to Publisher LD, automatically gets synchronized to Subscriber LD. |
|---|---|

| Note | Changes made to Publisher CUIC, automatically gets synchronized to Subscriber CUIC. |
|---|---|

| Step 1 | On the Administration & Data Server desktop, open the Unified CCE Tools folder and navigate to Administration Tools > CCE Web Administration . |
|---|---|
| Step 2 | Log in as a Config security group member in the format user@domain . |
| Step 3 | Navigate to Unified CCE Administration > Overview > Infrastructure Settings > Deployment Type . |
| Step 4 | Click Configure your deployment . The Configure your deployment wizard appears. |
| Step 5 | On the Deployment page, perform the following: Select Packaged CCE 2000 Agents from the Deployment drop-down list. Select the required instance from the drop-down list. Click Next . |
| Step 6 | On the Inventory page, perform the following: Click Download template to download the inventory template pcce2k_Inventory_Custom.csv file. Populate all required VM details in the pcce2k_Inventory_Custom.csv file. Provide VM details in the corresponding fields such as operation, name, machineType, publicAddress, publicAddressServices,
                                                privateAddress, and other required values. The type=SQL_SERVER&port=<non-default port> parameter of publicAddressServices field denotes the port number of the SQL Server used by the VM. If this parameter is not specified for a VM, the default
                                                SQL port 1433 is used to connect to the SQL service of that VM. To specify custom SQL port in the CSV file, add type=SQL_SERVER&port=<non-default port> . For example: type=SQL_SERVER&port=1534 Enter the custom SQL port for all CCE VMs, such as Rogger A or Rogger B and AW1 or AW2, that have SQL Server running on a
                                                custom port. In the Content File field, click Choose File to import the CSV file from your local folder. Click Next . The system validates the CSV file. After successful validation, the system automatically navigates to the Settings page. If the validation fails, verify the VM parameters and field values, and then retry the validation process. |
| Step 7 | On the Settings page, perform the following: Select the required values from the drop-down list for each Rogger and Service Account field. Click Next . |
| Step 8 | On the Initialize page, the fresh install task is triggered. |
| Step 9 | Click Next to deploy Packaged CCE 2000 Agents. |