---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-installatio-a29761dc32
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/installation/guide/ucce_b_install_upgrade_guide_1262/ucce_b_12_6_1-install_upgrade_guide_chapter_01010.html
retrieved_at: 2026-08-16T20:00:05.404786+00:00
---

Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Installation and Upgrade Guide, Release 12.6(2)

Updated: April 28, 2023

Chapter: Upgrade from a Standalone Deployment to a Coresident Deployment

## Chapter: Upgrade from a Standalone Deployment to a Coresident Deployment

# Upgrade from a Standalone Deployment to a Coresident Deployment

## Set Deployment Type in Unified CCE Administration Configuration

Perform the following steps to set the deployment:

Step 1

On Administration & Data Server open the Unified CCE Tools folder.

Step 2

Go to Administration Tools > CCE Web Administration.

Step 3

Log in as a Config security group member in the user@domain .

Step 4

Double-click Unified CCE Administration .

Step 5

Go to Infrastructure Settings > Deployment Settings .

Step 6

On the Deployment Type page, select UCCE: 2000 Agents Rogger deployment from the drop-down list and then click Next .

### What to do next

## Install Publisher/Primary Nodes of VOS-Based Contact Center Applications

### Before you begin

DNS Configuration is mandatory for installation of Cisco Unified Communications Manager, Cisco Unified Intelligence Center,
                                    Cisco Finesse and Cisco Identity Service (IdS). To configure DNS, add the VMs to the forward and reverse lookups of the DNS.

Step 1

Create a
                                       			 virtual machine for your VOS-based contact center application using the OVA.

Step 2

Mount the ISO
                                       			 image for the software to the virtual machine.

Step 3

Select the virtual machine, power it on, and open the console.

Step 4

Follow the
                                       			 Install wizard, making selections as follows:

In the Disk Found screen, click OK to begin the verification of the media integrity.

In the Success screen, select OK .

In the Product Deployment Selection screen:

For
                                                      						  the Progger (Lab only) or 2000 agent reference design, choose the coresident
                                                      						  deployment option Cisco Unified Intelligence Center with Live Data and
                                                         							 IdS , and then select OK . The Cisco Unified Intelligence Center with Live Data and
                                                         							 IdS option installs Cisco Unified Intelligence Center with Live
                                                      						  Data and Cisco Identity Service (IdS) on the same server.

For
                                                      						  all other deployments, select one of the standalone install options. For
                                                      						  example, select Cisco Unified Intelligence Center , Live Data , or Cisco Identity Service (IdS) . Then select OK .

In the Proceed with Install screen, select Yes .

In the Platform Installation Wizard screen, select Proceed .

In the Apply Patch screen, select No .

In the Basic Install screen, select Continue .

In the Timezone Configuration screen, use the down arrow to
                                             				  choose the local time zone that most closely matches where your server is
                                             				  located. Select OK .

For
                                                            						Live Data servers, use the same timezone for all the nodes.

In the Auto Negotiation Configuration screen, select Continue .

In the MTU Configuration screen, select No to keep the default setting for Maximum
                                             				  Transmission Units.

In the DHCP Configuration screen, select No .

In the Static Network Configuration screen, enter static
                                             				  configuration values. Select OK .

In the DNS Client Configuration screen, click Yes to enable DNS client.

Enter your DNS client configuration. Select OK .

In the Administrator Login Configuration screen, enter the
                                             				  Platform administration username. Enter and confirm the password for the
                                             				  administrator. Select OK .

In the Certificate Information screen, enter data to create
                                             				  your Certificate Signing Request: Organization, Unit, Location, State, and
                                             				  Country. Select OK .

In the First Node Configuration screen, select Yes .

In the Network Time Protocol Client Configuration screen,
                                             				  enter a valid NTP server IP address and select OK .

In the Security Configuration screen, enter the security
                                             				  password and select OK .

In the SMTP Host Configuration screen, select No .

In the Application User Configuration screen, enter the
                                             				  application username. Enter, and confirm the application user password. Select OK .

In the Platform Configuration Confirmation screen, select OK . The installation begins and runs unattended.

There is a reboot in the middle of the installation.

The installation ends at a sign-in prompt.

Step 5

Unmount the
                                       			 ISO image.

## Install Subscribers/Secondary Nodes of VOS-Based Contact Center Applications

This task is required for installation of the subscriber/secondary nodes of the three VOS-based contact center applications:
                                          Cisco Finesse, Cisco Unified Communications Manager, and Cisco Unified Intelligence Center.

### Before you begin

DNS Configuration is mandatory for installation of Cisco Unified Communications Manager, Cisco Unified Intelligence Center,
                              and Cisco Finesse. To configure DNS, add the VMs to the forward and reverse lookups of the DNS.

Before you install the subscriber/secondary nodes, you must install the publisher/primary nodes and configure the clusters.

Step 1

Create a virtual machine for your VOS-based contact center application using the OVA.

Step 2

Mount the ISO image for the software to the virtual machine.

Step 3

Select the virtual machine and power it on, and open the console.

Step 4

Follow the Install wizard, making selections as follows:

In the Disk Found screen, click OK to begin the verification of the media integrity.

In the Success screen, select OK .

In the Product Deployment Selection screen:

For the Progger (Lab only) or 2000 agent reference design, choose the coresident deployment option Cisco Unified Intelligence Center with Live Data and IdS , and then select OK . The Cisco Unified Intelligence Center with Live Data and IdS option installs Cisco Unified Intelligence Center, Live Data, and Cisco Identity Service (IdS) on the same server.

For all other deployments, select one of the standalone install options. For example, select Cisco Unified Intelligence Center , Live Data , or Cisco Identity Service (IdS) . Then select OK .

Step 5

Follow the Install wizard, making selections as follows:

In the Proceed with Install screen, select Yes .

In the Platform Installation Wizard screen, select Proceed .

In the Apply Patch screen, select No .

In the Basic Install screen, select Continue .

In the Timezone Configuration screen, use the down arrow to choose the local time zone that most closely matches where your server is located. Select OK .

For Live Data servers, use the same timezone for all the nodes.

In the Auto Negotiation Configuration screen, select Continue .

In the MTU Configuration screen, select No to keep the default setting for Maximum Transmission Units.

In the DHCP Configuration screen, select No .

In the Static Network Configuration screen, enter static configuration values. Select OK .

In the DNS Client Configuration screen, click Yes to enable DNS client.

In the Administrator Login Configuration screen, enter the Platform administration username. Enter and confirm the password for the administrator. Select OK .

In the Certificate Information screen, enter data to create your Certificate Signing Request: Organization, Unit, Location, State, and Country. Select OK .

In the First Node Configuration screen, select No .

In the warning screen, select OK .

In the Network Connectivity Test Configuration screen, select No .

In the First Node Access Configuration screen, enter the host name and IP address of the first node. Enter and confirm the security password. Select OK .

In the SMTP Host Configuration screen, select No .

In the Platform Configuration Confirmation screen, select OK . The installation begins and runs unattended.

There is a reboot in the middle of the installation.

The installation ends at a sign-in prompt.

Step 6

Unmount the ISO image.

## Set Up the System Inventory

Step 1

In Unified CCE Administration, navigate to Infrastructure Settings > Inventory .

Step 2

Add the new machine to the System Inventory:

Click New .

The Add Machine popup window opens.

From the Type drop-down menu, select the following machine type:

CUIC_LD_IdS Publisher, for the coresident Unified Intelligence Center, Live Data, and Identity Service machine available in
                                                the 2000 agent reference design.

In the Address field, enter the FQDN or IP address of the machine.

Enter the machine's Administration credentials.

Click Save .

The machine and its related Subscriber or Secondary machine are added to the System Inventory.

## Configure Live Data with AW

This command tells
                              		  Live Data how to access the primary AW DB and the secondary AW DB. The command
                              		  also automatically tests the connection from Live Data to the primary or
                              		  secondary AW, checks to see if the configured user has appropriate AW DB
                              		  access, and reports the results.

You can use the
                              		  optional skip-test parameter if you do not want the test performed. When you include the skip-test parameter, no checking
                              		  is done to see if the configured user has appropriate AW DB access, and no
                              		  results are reported.

You do not need to configure the AW DB on both the Publisher and the Subscriber.  The configuration is replicated between
                                          the Publisher and the Subscriber.

### Before you begin

Before you can configure Live Data, you must first configure
                              		  a SQL user (with special permissions) to work with Live Data, as
                              		  described in Configure SQL User Account .

The SQL administrative user with read and write permissions must then run the following SQL queries for the SQL user configured to work with Live Data.

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

Run the following command to configure Live Data with the primary AW DB. The command automatically tests the connection from
                                       Live Data, checks the user permission, and displays results.

(The skip-test parameter is optional; include it only if you do not want the test performed).

set live-data aw-access primary addr port db user [skip-test]

Step 3

Run the
                                       			 following command to configure Live Data with the secondary AW DB. The command
                                       			 automatically tests the connection from Live Data, checks the user permission,
                                       			 and displays results.

(The skip-test parameter is optional; include it only if you do not want the test performed).

(The skip-test parameter is optional; include it only if you do not want the test performed).

show live-data aw-access [skip-test]

## Configure Live Data Unified Intelligence Center Data Sources

This command tells
                              		  Unified Intelligence Center how to access Live Data.

Step 1

Log in to your
                                       			 Live Data server.

Step 2

Run the
                                       			 following command to configure your Live Data Unified Intelligence Center data
                                       			 sources:

set live-data cuic-datasource cuic-addr cuic-port cuic-user

## Restart Live Data

After you complete the configuration procedures for the AW and the Unified Intelligence Center data source, restart the Live
                              Data system to enable the changes.

Access the Live Data CLI and run the following command:

| Step 1 | On Administration & Data Server open the Unified CCE Tools folder. |
|---|---|
| Step 2 | Go to Administration Tools > CCE Web Administration. |
| Step 3 | Log in as a Config security group member in the user@domain . |
| Step 4 | Double-click Unified CCE Administration . |
| Step 5 | Go to Infrastructure Settings > Deployment Settings . |
| Step 6 | On the Deployment Type page, select UCCE: 2000 Agents Rogger deployment from the drop-down list and then click Next . Note Whenever you change the deployment type, you need to restart the Apache Tomcat on Logger and AWs. | Note | Whenever you change the deployment type, you need to restart the Apache Tomcat on Logger and AWs. |
| Note | Whenever you change the deployment type, you need to restart the Apache Tomcat on Logger and AWs. |

| Note | Whenever you change the deployment type, you need to restart the Apache Tomcat on Logger and AWs. |
|---|---|

| Step 1 | Create a
                                       			 virtual machine for your VOS-based contact center application using the OVA. |
|---|---|
| Step 2 | Mount the ISO
                                       			 image for the software to the virtual machine. |
| Step 3 | Select the virtual machine, power it on, and open the console. |
| Step 4 | Follow the
                                       			 Install wizard, making selections as follows: In the Disk Found screen, click OK to begin the verification of the media integrity. In the Success screen, select OK . In the Product Deployment Selection screen: For
                                                      						  the Progger (Lab only) or 2000 agent reference design, choose the coresident
                                                      						  deployment option Cisco Unified Intelligence Center with Live Data and
                                                         							 IdS , and then select OK . The Cisco Unified Intelligence Center with Live Data and
                                                         							 IdS option installs Cisco Unified Intelligence Center with Live
                                                      						  Data and Cisco Identity Service (IdS) on the same server. For
                                                      						  all other deployments, select one of the standalone install options. For
                                                      						  example, select Cisco Unified Intelligence Center , Live Data , or Cisco Identity Service (IdS) . Then select OK . In the Proceed with Install screen, select Yes . In the Platform Installation Wizard screen, select Proceed . In the Apply Patch screen, select No . In the Basic Install screen, select Continue . In the Timezone Configuration screen, use the down arrow to
                                             				  choose the local time zone that most closely matches where your server is
                                             				  located. Select OK . Note For
                                                            						Live Data servers, use the same timezone for all the nodes. In the Auto Negotiation Configuration screen, select Continue . In the MTU Configuration screen, select No to keep the default setting for Maximum
                                             				  Transmission Units. In the DHCP Configuration screen, select No . In the Static Network Configuration screen, enter static
                                             				  configuration values. Select OK . In the DNS Client Configuration screen, click Yes to enable DNS client. Enter your DNS client configuration. Select OK . In the Administrator Login Configuration screen, enter the
                                             				  Platform administration username. Enter and confirm the password for the
                                             				  administrator. Select OK . In the Certificate Information screen, enter data to create
                                             				  your Certificate Signing Request: Organization, Unit, Location, State, and
                                             				  Country. Select OK . In the First Node Configuration screen, select Yes . In the Network Time Protocol Client Configuration screen,
                                             				  enter a valid NTP server IP address and select OK . In the Security Configuration screen, enter the security
                                             				  password and select OK . In the SMTP Host Configuration screen, select No . In the Application User Configuration screen, enter the
                                             				  application username. Enter, and confirm the application user password. Select OK . In the Platform Configuration Confirmation screen, select OK . The installation begins and runs unattended. There is a reboot in the middle of the installation. The installation ends at a sign-in prompt. | Note | For
                                                            						Live Data servers, use the same timezone for all the nodes. |
| Note | For
                                                            						Live Data servers, use the same timezone for all the nodes. |
| Step 5 | Unmount the
                                       			 ISO image. |

| Note | For
                                                            						Live Data servers, use the same timezone for all the nodes. |
|---|---|

| Note | This task is required for installation of the subscriber/secondary nodes of the three VOS-based contact center applications:
                                          Cisco Finesse, Cisco Unified Communications Manager, and Cisco Unified Intelligence Center. |
|---|---|

| Step 1 | Create a virtual machine for your VOS-based contact center application using the OVA. |
|---|---|
| Step 2 | Mount the ISO image for the software to the virtual machine. |
| Step 3 | Select the virtual machine and power it on, and open the console. |
| Step 4 | Follow the Install wizard, making selections as follows: In the Disk Found screen, click OK to begin the verification of the media integrity. In the Success screen, select OK . In the Product Deployment Selection screen: For the Progger (Lab only) or 2000 agent reference design, choose the coresident deployment option Cisco Unified Intelligence Center with Live Data and IdS , and then select OK . The Cisco Unified Intelligence Center with Live Data and IdS option installs Cisco Unified Intelligence Center, Live Data, and Cisco Identity Service (IdS) on the same server. For all other deployments, select one of the standalone install options. For example, select Cisco Unified Intelligence Center , Live Data , or Cisco Identity Service (IdS) . Then select OK . |
| Step 5 | Follow the Install wizard, making selections as follows: In the Proceed with Install screen, select Yes . In the Platform Installation Wizard screen, select Proceed . In the Apply Patch screen, select No . In the Basic Install screen, select Continue . In the Timezone Configuration screen, use the down arrow to choose the local time zone that most closely matches where your server is located. Select OK . Note For Live Data servers, use the same timezone for all the nodes. In the Auto Negotiation Configuration screen, select Continue . In the MTU Configuration screen, select No to keep the default setting for Maximum Transmission Units. In the DHCP Configuration screen, select No . In the Static Network Configuration screen, enter static configuration values. Select OK . In the DNS Client Configuration screen, click Yes to enable DNS client. In the Administrator Login Configuration screen, enter the Platform administration username. Enter and confirm the password for the administrator. Select OK . In the Certificate Information screen, enter data to create your Certificate Signing Request: Organization, Unit, Location, State, and Country. Select OK . In the First Node Configuration screen, select No . In the warning screen, select OK . In the Network Connectivity Test Configuration screen, select No . In the First Node Access Configuration screen, enter the host name and IP address of the first node. Enter and confirm the security password. Select OK . In the SMTP Host Configuration screen, select No . In the Platform Configuration Confirmation screen, select OK . The installation begins and runs unattended. There is a reboot in the middle of the installation. The installation ends at a sign-in prompt. | Note | For Live Data servers, use the same timezone for all the nodes. |
| Note | For Live Data servers, use the same timezone for all the nodes. |
| Step 6 | Unmount the ISO image. |

| Note | For Live Data servers, use the same timezone for all the nodes. |
|---|---|

| Step 1 | In Unified CCE Administration, navigate to Infrastructure Settings > Inventory . |
|---|---|
| Step 2 | Add the new machine to the System Inventory: Click New . The Add Machine popup window opens. From the Type drop-down menu, select the following machine type: CUIC_LD_IdS Publisher, for the coresident Unified Intelligence Center, Live Data, and Identity Service machine available in
                                                the 2000 agent reference design. In the Address field, enter the FQDN or IP address of the machine. Enter the machine's Administration credentials. Click Save . The machine and its related Subscriber or Secondary machine are added to the System Inventory. |

| Note | You do not need to configure the AW DB on both the Publisher and the Subscriber.  The configuration is replicated between
                                          the Publisher and the Subscriber. |
|---|---|

| Step 1 | Log in to your
                                       			 Live Data server. |
|---|---|
| Step 2 | Run the following command to configure Live Data with the primary AW DB. The command automatically tests the connection from
                                       Live Data, checks the user permission, and displays results. (The skip-test parameter is optional; include it only if you do not want the test performed). set live-data aw-access primary addr port db user [skip-test] |
| Step 3 | Run the
                                       			 following command to configure Live Data with the secondary AW DB. The command
                                       			 automatically tests the connection from Live Data, checks the user permission,
                                       			 and displays results. (The skip-test parameter is optional; include it only if you do not want the test performed). (The skip-test parameter is optional; include it only if you do not want the test performed). show live-data aw-access [skip-test] |

| Step 1 | Log in to your
                                       			 Live Data server. |
|---|---|
| Step 2 | Run the
                                       			 following command to configure your Live Data Unified Intelligence Center data
                                       			 sources: set live-data cuic-datasource cuic-addr cuic-port cuic-user |

| Access the Live Data CLI and run the following command: utils system restart |
|---|