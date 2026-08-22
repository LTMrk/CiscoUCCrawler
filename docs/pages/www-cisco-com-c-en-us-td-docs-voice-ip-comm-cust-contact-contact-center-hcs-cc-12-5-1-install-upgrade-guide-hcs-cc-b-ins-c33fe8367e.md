---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-hcs-cc-12-5-1-install-upgrade-guide-hcs-cc-b-ins-c33fe8367e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/hcs-cc/12_5_1/Install_Upgrade_Guide/hcs-cc_b_installing-and-upgrading-guide_12_5/hcs-cc_b_installing-and-upgrading-guide-for_chapter_0101.html
retrieved_at: 2026-08-22T00:12:28.809827+00:00
---

Installing and Upgrading Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5(1) and 12.5(2)

# Installing and Upgrading Guide for Cisco Hosted Collaboration Solution for Contact Center, Release 12.5(1) and 12.5(2)

Updated: July 26, 2022

Chapter: Upgrade

## Chapter: Upgrade

# Upgrade

## Overview of the Upgrade Workflow

The upgrade process is evaluated by the HCS for
                           CC deployment type you plan to upgrade. Follow the section in the table to plan for your
                           upgrade from 12.0 to 12.5 (x).

Current Deployment Type

Target Deployment Type

Upgrade Process

HCS for CC 500

HCS for CC 2000

Migration CC Upgrade

HCS for CC 1000

HCS for CC 2000

Migration CC Upgrade

HCS for CC 4000

HCS for CC 4000

Standard CC Upgrade

HCS for CC 12000

HCS for CC 12000

Standard CC Upgrade

All upgrades from 12.0 to 12.5(x) are Standard CC upgrades.

The Small Contact Center (SCC) deployment uses the HCS for CC 4000 deployment type and follows same upgrade process.

Perform the Cisco HCS for Contact Center upgrade in the same sequence as the upgrade and validation steps are described in
                           this document.

For more information, see Cisco Hosted Collaboration Solution Documentation , https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-hcs/tsd-products-support-series-home.html

The following upgrade paths are supported:

Upgrade from 12.0(x) to 12.5(1) is supported in this
                           release. Use EDMT during this upgrade process.

Upgrade from 12.5(1) to 12.5(x) is supported in
                           this release.

## Upgrading
                        	 Management Components

### Upgrade
                           	 HCM-F

#### Before you begin

Before upgrading a
                                 		  Cisco HCM-F application node, perform the following tasks.

Create a valid
                                       				DRF backup of your HCM-F.

From the
                                       				command-line interface on the application node, run show
                                          				  hcs cluster nodes to verify that the node is at the pre-upgrade
                                       				version.

Obtain the
                                       				upgrade media for upgrading the HCM-F platform: upgrade disk or a downloaded
                                       				executable file.

Step 1

If you
                                          			 downloaded the executable file from Cisco.com, perform one of the following
                                          			 steps.

Copy
                                                         						  the upgrade file to a temporary folder on a local hard drive.

Open
                                                         						  an SFTP client and connect to the HCM-F server using your adminsftp user ID and
                                                         						  password.

Run
                                                         						  the cd upgrade command to navigate to the upgrade folder.

Run
                                                         						  the put [upgrade file name] command to transfer the file.

Copy
                                                            						  the upgrade ISO to a data store that is accessible by your virtual machine.

Attach
                                                            						  the ISO image to the CD/DVD drive of the virtual machine.

Put the
                                                   					 upgrade file on an FTP or SFTP server that is accessible by the virtual machine
                                                   					 that you are upgrading.

Step 2

Copy the
                                          			 contents of the upgrade disk or downloaded files to the virtual machine that
                                          			 you are upgrading.

Step 3

On the virtual
                                          			 machine that you are upgrading, log in to the HCM-F command-line interface and
                                          			 run the utils
                                             				system upgrade initiate command.

Step 4

Choose the
                                          			 source from which you want to upgrade.

Remote
                                                   					 file system via SFTP

Remote
                                                   					 file system via FTP

Local
                                                   					 DVD/CD

Local
                                                   					 Upload Directory

Step 5

Follow system
                                          			 prompts for the upgrade option you chose.

Step 6

If you did not
                                          			 choose to automatically switch versions, run the utils
                                             				system switch-version command. Enter yes to reboot the server and switch to the new
                                          			 software version.

Step 7

From the HCM-F
                                          			 command-line interface, run the show
                                             				version active command to verify that the software version is the
                                          			 upgraded version.

Step 8

If you
                                          			 performed step 6, run the utils
                                             				service list command to view services. Then run utils
                                             				service start [service name] to restart any services that were
                                          			 stopped before the upgrade.

### Validate the HCM-F
                           	 Upgrade

Perform the following steps to validate the upgrade of Cisco HCM-F.

Step 1

Verify that no error logs
                                          			 were created during or after the upgrade.

Step 2

Run the show version active command to verify that the
                                          			 active version is the upgraded version.

Step 3

Run the utils service list command to verify that all
                                          			 services are running as they were before the upgrade.

Step 4

Sign in to the administration interface and click the About link to verify that the interface
                                          			 displays the upgraded version.

Step 5

Verify that all synchronization is successful for Service
                                          			 Provider, Data Center, vCenter, Customer, and UCS Manager.

Step 6

Verify that Hosted License Manager does not contain post-upgrade
                                          			 errors. Also verify that licenses are assigned to the proper customers.

Step 7

Depending on which you used for the upgrade, ensure that Platform
                                          			 Manager or Prime Collaboration Deployment is running.

Step 8

Verify that Service Inventory is running.

### Upgrade
                           	 UCDM

Step 1

Create a
                                          			 backup using the platform command-line interface. You can back up the cluster
                                          			 or back up each node individually.

Step 2

Turn off any
                                          			 scheduled imports.

Step 3

Check for
                                          			 running imports. Either wait for them to complete or cancel them.

Step 4

Upgrade multinode environment. See, Upgrade a Multinode Environment section in Cisco Hosted Collaboration Solution Upgrade and Migration Guide https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-hcs/tsd-products-support-series-home.html

### Validate the
                           	 Unified CDM Upgrade

Take the following
                                 		  steps to validate the upgrade of Unified CDM in a multinode or standalone
                                 		  environment.

Step 1

Sign in to the
                                          			 user interface as hcsadmin, and click About > Extended
                                                				  Version to verify the upgrade.

Step 2

Reactivate the
                                          			 scheduled imports that you turned off before upgrading.

Step 3

Use the
                                          			 command-line interface on the primary node to run the cluster
                                             				status command.

Step 4

Attempt to
                                          			 associate a phone with a user:

In Unified
                                                				  CDM, navigate to Subscriber
                                                      						Management > Phone and add a phone.

Add a line
                                                				  to the phone.

Navigate
                                                				  to Subscriber
                                                      						Management > Agent Line and identify the new phone
                                                				  as an agent line.

In Unified
                                                				  CM, navigate to User
                                                      						Management > Application User and verify that the
                                                				  new phone is associated with pguser.

### Upgrade Prime
                           	 Collaboration Assurance

Cisco supports the upgrade to Cisco Prime Collaboration Assurance 11.6 or later version.

To upgrade Prime Collaboration Assurance, follow the steps in the "Overview of Data Migration Assistant" topic in the Cisco Prime Collaboration Assurance and Analytics Install and Upgrade Guide : https://www.cisco.com/c/en/us/support/cloud-systems-management/prime-collaboration/products-installation-guides-list.html .

### Validate the
                           	 Upgrade of Prime Collaboration Assurance

Take the following
                                 		  steps to validate the upgrade of Prime Collaboration Assurance.

Validation
                                 		  consists of adding a Contact Center customer component and verifying that the
                                 		  component is in Managed state. In this example, we add the Customer Voice
                                 		  Portal component.

Step 1

Sign in to HCM-F as an administrator.

Step 2

Add a cluster.

Navigate
                                                				  to Cluster
                                                      						Management > Cluster and click Add New .

Enter the
                                                				  cluster name.

Select the
                                                				  customer associated with the cluster.

Select CC as the cluster type.

Select the
                                                				  cluster application version.

In the Application Monitoring the Cluster field, select the
                                                				  hostname of the Prime Collaboration Assurance instance.

Click Save .

Step 3

Add the
                                          			 Customer Voice Portal component.

Navigate
                                                				  to Application
                                                      						Management > Cluster Application .

In the
                                                				  General Information section, complete the following steps:

Click Add New .

In the Application Type field, select CVP .

Provide the hostname for the Customer Voice Portal component.

Select
                                                         						  the appropriate cluster.

Click Save .

In the
                                                				  Credentials section, complete the following steps:

Click Add New .

In the Credential Type field, select SNMP_V2 .

Provide the community string for the Customer Voice Portal
                                                         						  component.

Select
                                                         						  the Read Only access type.

Click Save .

Click Add New .

In the Credential Type field, select ADMIN .

Provide the administrator credentials. For Customer Voice
                                                         						  Portal, the User ID is wsmadmin. Use the password that is configured for the
                                                         						  OAMP web interface.

Select
                                                         						  the Read Only access type.

Click Save .

In the
                                                				  Network Addresses section, complete the following steps:

Click Add New .

In
                                                         						  the Network Space field, select Application Space .

Provide the IPv4 address and the hostname.

Click Save .

Click Add New .

In
                                                         						  the Network Space field, select Service Provider Space .

Provide the NAT IPv4 address and the hostname.

Click Save .

Step 4

Navigate to the Current Inventory (Inventory > Inventory Management) page.

### Upgrade Unified
                           	 CCDM

To upgrade Cisco Unified Contact Center Domain Manager, follow the installation steps in the Installation and Configuration Guide for Cisco Unified Contact Center Domain Manager : https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-contact-center/products-installation-guides-list.html .

### Validate the
                           	 Unified CCDM Upgrade

Take the following
                                 		  steps to verify the upgrade of Unified CCDM.

Verification Task

Success
                                             						Criteria

Provisioning Tests for
                                                						  Unified CCE

Log in
                                             						to the side A web server (portal). Create a Skill Group to test the
                                             						provisioning from the side A web server. Run this test for each configured
                                             						Unified CCE instance.

You can
                                             						successfully create the Skill Group, and it is visible on side A, and on side B
                                             						if applicable.

Log in
                                             						to the side A web server (Portal). Create an Agent to test the provisioning
                                             						from the side A web server. Run this test for each configured Unified CCE
                                             						instance.

You can
                                             						successfully create an Agent, and it is visible on side A, and on side B if
                                             						applicable.

Create a
                                             						Skill Group on the Administrative Workstation using the Cisco Skill Group
                                             						Explorer tool. After a few minutes, verify that the Skill Group was imported
                                             						into Unified CCDM.

The
                                             						Skill Group is visible on side A, and on side B if applicable.

Replication Tests for
                                                						  Dual-Sided Deployments

Log in
                                             						to the side B web server (Portal). Create a Skill Group to test Unified CCE
                                             						provisioning from the side B web server. Run this test for each configured
                                             						Unified CCE instance.

You can
                                             						successfully create the Skill Group, and it is visible on side A.

Create a
                                             						Skill Group on the Administrative Workstation using the Cisco Skill Group
                                             						Explorer tool. After a few minutes, verify that the Skill Group was imported
                                             						into Unified CCDM.

The
                                             						Skill Group is visible on side A and on side B.

Log in
                                             						to the side B web server (Portal). Create an IP phone to test Unified CM
                                             						provisioning from the side B web server.

The IP
                                             						phone is visible on side A and on side B.

## Standard CC Upgrade

### Upgrading Unified Customer Voice Portal Components

#### Upgrade the
                              	 Unified Customer Voice Portal

Follow these steps
                                    		  to upgrade Cisco Unified Customer Voice Portal.

Step 1

Back up the
                                             			 Unified CVP Operations Console configuration.

Step 2

Install the
                                             			 upgrade software.

#### Validate the
                              	 Customer Voice Portal Upgrade

Follow these steps
                                    		  to validate the upgrade of Cisco Unified Customer Voice Portal.

Step 1

Log in to the
                                             			 Operations Console.

Step 2

Validate the
                                             			 version of each component.

Step 3

Verify that
                                             			 all services are running.

Step 4

Make a test
                                             			 inbound PSTN call to an agent.

### Upgrading Gateway Components

#### Upgrade Gateway
                              	 Components

Follow the steps to
                                    		  upgrade Cisco Unified Border Element (SP Edition), Cisco Unified Border Element
                                    		  (Enterprise Edition), or a virtual peripheral gateway (vPGW). For more
                                    		  information, see the following topics and guides:

Step 1

Back up all
                                             			 the gateways.

Step 2

Use the
                                             			 gateway consoles to back up component configurations.

Step 3

Upgrade the
                                             			 gateways.

#### Upgrading the
                              	 Cisco ASR 1000 Series Router for Cisco Unified Border Element (SP
                              	 Edition)

Cisco Unified Border Element (SP Edition) is used as a demarcation between the Cisco HCS network and an outside network,
                                 		such as IMS, PSTN, or other SIP network. The ASR 1000 Series router is
                                 		connected to the aggregation switches at the aggregation layer.

To upgrade this component, follow the procedures in the Cisco ASR 1000 Series Aggregation Services Routers Software Configuration Guide : https://www.cisco.com/c/en/us/support/routers/asr-1000-series-aggregation-services-routers/products-installation-and-configuration-guides-list.html .

When you have a redundant Cisco Unified Border Element (SP Edition) deployed, upgrade the component using the procedures in Cisco Unified Border Element (SP Edition) Configuration Guide: Unified Model : https://www.cisco.com/c/en/us/support/routers/asr-1000-series-aggregation-services-routers/products-installation-and-configuration-guides-list.html .

To upgrade the ROMmon image on a Cisco ASR 1000 Series router, see the Cisco ASR 1000 Series Routers ROMmon Upgrade Guide : https://www.cisco.com/c/en/us/support/routers/asr-1000-series-aggregation-services-routers/products-maintenance-guides-list.html .

#### Upgrade the IOS on
                              	 the Cisco ASR 1006 for Cisco Unified Border Element (SP Edition)

Use this procedure
                                    		  to upgrade Cisco Unified Border Element (SP Edition) ASR 1006 from version IOS
                                    		  15.3(3)S to IOS 15.3(3)S4.

##### Before you begin

- Ensure Cisco Unified Border
                                          			 Element (SP Edition) is configured for inter-chassis redundancy, with one Cisco
                                          			 ASR 1006 Aggregation Service Router in the Active state and the other in the
                                          			 Standby state.

Save the
                                             				current configuration and download the software image to the boot flash of both
                                             				of the ASR 1006 devices. It takes about 15 minutes.

Step 1

Enter the CLI
                                             			 command show
                                                				redundancy application group <RG Group Id> to determine which
                                             			 Session Border Controller (SBC) is Active. The Primary SBC is the Active
                                             			 chassis and the Secondary SBC is the Standby chassis.

Step 2

Download the
                                             			 new software version to the Primary and Secondary SBCs.

Step 3

On the
                                             			 Secondary SBC, enter the CLI command boot
                                                				system bootflash: <new image> to change the boot variable to
                                             			 point to the new image.

Step 4

On the Primary SBC, perform an SBC sync from configuration mode. Enter the sbc configuration by running the CLI command sbc <name of SBC> and then run the CLI command sync .

Step 5

On the
                                             			 Secondary SBC, enter the CLI command write
                                                				memory to save the running configuration.

Step 6

On the
                                             			 Primary SBC, enter the CLI command redundancy > application redundancy > group # >
                                                				shutdown to shut down the redundancy group.

Step 7

On the
                                             			 Primary SBC, change the boot variable to point to new software image and save
                                             			 the running configuration.

Step 8

Reload the
                                             			 Primary chassis for upgrade and wait for this SBC to come up with upgraded
                                             			 version.

Step 9

On the Secondary SBC, shut down the redundancy and immediately run the CLI command no shutdown of the redundancy group on the Primary SBC. Keep the duration between shutting down the redundancy group in the Secondary
                                             SBC and the no shutdown command in the Primary box as minimal as possible.

Step 10

Save the
                                             			 running configuration in the Primary SBC.

Step 11

Reload the
                                             			 Secondary chassis for upgrade. When prompted to save the configuration before
                                             			 proceeding with the reload, enter “No” so that after the upgrade the Secondary
                                             			 SBC comes up in Standby mode.

#### Validate the
                              	 Upgrade of Gateway Components

This section describes the steps to verify the upgrade of Cisco Unified Border Element (SP Edition), Metaswitch Perimeta Session Border Controller, Cisco Unified Border Element (Enterprise
                                       Edition), or a virtual peripheral gateway (vPGW) .

Step 1

Use Telnet or
                                             			 SSH to access the gateways and verify the version you upgraded to.

Step 2

Make an
                                             			 inbound call to an agent and verify the prompts. You can run the debug
                                                				voip dial peer command to ensure that the inbound call uses the
                                             			 correct dial peer.

### Upgrading the Unified Component

#### Upgrading the Unified Component

Follow the steps
                                    		  to upgrade the Cisco Unified Contact Center Enterprise Central Controller.

Unless otherwise indicated, the following steps reference topics in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Step 1

Upgrade the
                                             			 Administration and Data server that is connected to Side A.

Step 2

Perform the Database Performance Enhancement.

For more information, see the Database Performance Enhancement section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

Step 3

Bring the Side
                                             			 A logger and call router into service.

Step 4

Upgrade Cisco
                                             			 Unified Intelligence Center reporting templates.

Step 5

Upgrade the
                                             			 Unified CCE Administration Client.

Step 6

Upgrade the gateways.

Step 7

Upgrade the Outbound Option Dialer.

Step 8

Upgrade the CTI server.

##### What to do next

To establish secure connection between a client and a server, use one of the following security certificates:

CA certificates

Self-signed certificates

For more information, see Certificates for CCE Web Administration section in the Cisco Hosted Collaboration Solution for Contact Center Configuration Guide at https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-contact-center/products-installation-and-configuration-guides-list.html .

### Upgrading Reporting Components

#### Upgrade Cisco
                              	 Unified Intelligence Center

To upgrade Cisco Unified Intelligence Center, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center : https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html .

#### Validate the
                              	 Upgrade of Unified Intelligence Center

Take the following steps to validate the upgrade of Cisco Unified
                                    		  Intelligence Center.

Step 1

Open the Unified OS
                                             			 Administration web page at the following URL, where [server-name] is the
                                             			 hostname or IP address of the node: https://[server-name]/cmplatform .

Step 2

Sign in with administrator credentials.

Step 3

Navigate to Settings > Version and verify the software version on the active and inactive partitions.

### Upgrading Desktop Components

#### Upgrade
                              	 Finesse

To upgrade Cisco Finesse, see the Cisco Finesse Installation and Upgrade Guide : https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-installation-guides-list.html .

ES42 provides the ability to
                                                					connect a maximum of two versions of Finesse to the same PG during the upgrade
                                                					or migration process to facilitate the migration of agentsand supervisors to the
                                                					new Finesse version. However, this mode of operation isnot supported for
                                                					production use beyond the upgrade or migration phase.

#### Validate the
                              	 Finesse Upgrade

Take the following
                                    		  steps to validate the upgrade of Cisco Finesse.

Step 1

Ensure that
                                             			 the version of Finesse is the version you upgraded to. From the command line
                                             			 interface, you can run the show status command to verify the version.

Step 2

In the Finesse
                                             			 console, verify that all services are up.

Step 3

Log in to an
                                             			 agent and run desktop-initiated tests such as Call Hold, Transfer, and
                                             			 Conference.

#### Upgrade Desktop
                              	 Clients

(Optional). To upgrade CTI OS Agent and Supervisor desktops, see the CTI OS System Manager Guide for Cisco Unified ICM/Contact Center Enterprise : https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

#### Validate the
                              	 Upgrade of Desktop Clients

Take the following
                                    		  steps to validate the upgrade of CTI OS Agent and Supervisor desktops.

Step 1

Validate the
                                             			 version of each desktop.

Step 2

Sign in to an
                                             			 agent and run desktop-initiated tests such as Call Hold, Transfer, and
                                             			 Conference.

### Upgrading Call-Processing Components

#### Upgrading Cisco
                              	 Virtualized Voice Browser Components

##### Upgrade Cisco
                                 	 Virtualized Voice Browser

To upgrade the Cisco Virtualized Voice Browser, follow the steps in the "Cisco Virtualized Voice Browser Upgrade" chapter
                                    in the Installation and Upgrade Guide for Cisco Virtualized Voice Browser Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/products-installation-guides-list.html

##### Validate the Cisco
                                 	 Virtualized Voice Browser Upgrade

Follow these steps to validate the upgrade of Cisco Virtualized Voice
                                       		  Browser portal.

Step 1

Log into Cisco Virtualized
                                                			 Voice Browser portal.

Step 2

Check the existing configuration.

#### Upgrade Cisco
                              	 Unified Communications Manager

Take the following
                                    		  steps to upgrade Cisco Unified Communications Manager.

Step 1

Upgrade Cisco
                                             			 Unified CM.

Step 2

Uninstall and
                                             			 then reinstall the JTAPI client on the Cisco Unified CM peripheral gateway.

#### Validate the
                              	 Upgrade of Cisco Unified Communications Manager

Take the following
                                    		  steps to validate the upgrade of Cisco Unified Communications Manager.

Step 1

In Cisco Unified CDM, add an IP phone. For more information, see the Cisco Hosted Collaboration Solution End-User Provisioning Guide : https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-hcs/tsd-products-support-series-home.html .

Step 2

In Cisco
                                             			 Unified CM, verify that the phone was added.

| Current Deployment Type | Target Deployment Type | Upgrade Process |
|---|---|---|
| HCS for CC 500 | HCS for CC 2000 | Migration CC Upgrade |
| HCS for CC 1000 | HCS for CC 2000 | Migration CC Upgrade |
| HCS for CC 4000 | HCS for CC 4000 | Standard CC Upgrade |
| HCS for CC 12000 | HCS for CC 12000 | Standard CC Upgrade |

| Note | All upgrades from 12.0 to 12.5(x) are Standard CC upgrades. The Small Contact Center (SCC) deployment uses the HCS for CC 4000 deployment type and follows same upgrade process. |
|---|---|

| Step 1 | If you
                                          			 downloaded the executable file from Cisco.com, perform one of the following
                                          			 steps. Prepare to upgrade from a
                                                				  local folder. Copy
                                                         						  the upgrade file to a temporary folder on a local hard drive. Open
                                                         						  an SFTP client and connect to the HCM-F server using your adminsftp user ID and
                                                         						  password. Run
                                                         						  the cd upgrade command to navigate to the upgrade folder. Run
                                                         						  the put [upgrade file name] command to transfer the file. Prepare to
                                                   					 load an ISO file. Copy
                                                            						  the upgrade ISO to a data store that is accessible by your virtual machine. Attach
                                                            						  the ISO image to the CD/DVD drive of the virtual machine. Put the
                                                   					 upgrade file on an FTP or SFTP server that is accessible by the virtual machine
                                                   					 that you are upgrading. |
|---|---|
| Step 2 | Copy the
                                          			 contents of the upgrade disk or downloaded files to the virtual machine that
                                          			 you are upgrading. Ensure
                                          			 that the upgrade filename begins with 'HCS.' |
| Step 3 | On the virtual
                                          			 machine that you are upgrading, log in to the HCM-F command-line interface and
                                          			 run the utils
                                             				system upgrade initiate command. |
| Step 4 | Choose the
                                          			 source from which you want to upgrade. Remote
                                                   					 file system via SFTP Remote
                                                   					 file system via FTP Local
                                                   					 DVD/CD Local
                                                   					 Upload Directory |
| Step 5 | Follow system
                                          			 prompts for the upgrade option you chose. The
                                          			 system prompts you when the upgrade is complete. |
| Step 6 | If you did not
                                          			 choose to automatically switch versions, run the utils
                                             				system switch-version command. Enter yes to reboot the server and switch to the new
                                          			 software version. |
| Step 7 | From the HCM-F
                                          			 command-line interface, run the show
                                             				version active command to verify that the software version is the
                                          			 upgraded version. |
| Step 8 | If you
                                          			 performed step 6, run the utils
                                             				service list command to view services. Then run utils
                                             				service start [service name] to restart any services that were
                                          			 stopped before the upgrade. |

| Step 1 | Verify that no error logs
                                          			 were created during or after the upgrade. |
|---|---|
| Step 2 | Run the show version active command to verify that the
                                          			 active version is the upgraded version. |
| Step 3 | Run the utils service list command to verify that all
                                          			 services are running as they were before the upgrade. |
| Step 4 | Sign in to the administration interface and click the About link to verify that the interface
                                          			 displays the upgraded version. |
| Step 5 | Verify that all synchronization is successful for Service
                                          			 Provider, Data Center, vCenter, Customer, and UCS Manager. |
| Step 6 | Verify that Hosted License Manager does not contain post-upgrade
                                          			 errors. Also verify that licenses are assigned to the proper customers. |
| Step 7 | Depending on which you used for the upgrade, ensure that Platform
                                          			 Manager or Prime Collaboration Deployment is running. |
| Step 8 | Verify that Service Inventory is running. |

| Step 1 | Create a
                                          			 backup using the platform command-line interface. You can back up the cluster
                                          			 or back up each node individually. |
|---|---|
| Step 2 | Turn off any
                                          			 scheduled imports. |
| Step 3 | Check for
                                          			 running imports. Either wait for them to complete or cancel them. |
| Step 4 | Upgrade multinode environment. See, Upgrade a Multinode Environment section in Cisco Hosted Collaboration Solution Upgrade and Migration Guide https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-hcs/tsd-products-support-series-home.html |

| Step 1 | Sign in to the
                                          			 user interface as hcsadmin, and click About > Extended
                                                				  Version to verify the upgrade. |
|---|---|
| Step 2 | Reactivate the
                                          			 scheduled imports that you turned off before upgrading. |
| Step 3 | Use the
                                          			 command-line interface on the primary node to run the cluster
                                             				status command. The
                                          			 command returns a list of clusters and their status. |
| Step 4 | Attempt to
                                          			 associate a phone with a user: In Unified
                                                				  CDM, navigate to Subscriber
                                                      						Management > Phone and add a phone. Add a line
                                                				  to the phone. Navigate
                                                				  to Subscriber
                                                      						Management > Agent Line and identify the new phone
                                                				  as an agent line. In Unified
                                                				  CM, navigate to User
                                                      						Management > Application User and verify that the
                                                				  new phone is associated with pguser. |

| Note | For downloading the Prime Collaboration patch, refer to the Dowload Software page. Navigate to Products > Cloud and System Management > Collaboration and Unified Communications Management > Prime Collaboration . |
|---|---|

| Step 1 | Sign in to HCM-F as an administrator. |
|---|---|
| Step 2 | Add a cluster. Navigate
                                                				  to Cluster
                                                      						Management > Cluster and click Add New . Enter the
                                                				  cluster name. Select the
                                                				  customer associated with the cluster. Select CC as the cluster type. Select the
                                                				  cluster application version. In the Application Monitoring the Cluster field, select the
                                                				  hostname of the Prime Collaboration Assurance instance. Click Save . |
| Step 3 | Add the
                                          			 Customer Voice Portal component. Navigate
                                                				  to Application
                                                      						Management > Cluster Application . In the
                                                				  General Information section, complete the following steps: Click Add New . In the Application Type field, select CVP . Provide the hostname for the Customer Voice Portal component. Select
                                                         						  the appropriate cluster. Click Save . In the
                                                				  Credentials section, complete the following steps: Click Add New . In the Credential Type field, select SNMP_V2 . Provide the community string for the Customer Voice Portal
                                                         						  component. Select
                                                         						  the Read Only access type. Click Save . Click Add New . In the Credential Type field, select ADMIN . Provide the administrator credentials. For Customer Voice
                                                         						  Portal, the User ID is wsmadmin. Use the password that is configured for the
                                                         						  OAMP web interface. Select
                                                         						  the Read Only access type. Click Save . In the
                                                				  Network Addresses section, complete the following steps: Click Add New . In
                                                         						  the Network Space field, select Application Space . Provide the IPv4 address and the hostname. Click Save . Click Add New . In
                                                         						  the Network Space field, select Service Provider Space . Provide the NAT IPv4 address and the hostname. Click Save . |
| Step 4 | Navigate to the Current Inventory (Inventory > Inventory Management) page. The State column shows the Customer Voice Portal as Managed . |

| Verification Task | Success
                                             						Criteria |
|---|---|
| Provisioning Tests for
                                                						  Unified CCE |  |
| Log in
                                             						to the side A web server (portal). Create a Skill Group to test the
                                             						provisioning from the side A web server. Run this test for each configured
                                             						Unified CCE instance. | You can
                                             						successfully create the Skill Group, and it is visible on side A, and on side B
                                             						if applicable. |
| Log in
                                             						to the side A web server (Portal). Create an Agent to test the provisioning
                                             						from the side A web server. Run this test for each configured Unified CCE
                                             						instance. | You can
                                             						successfully create an Agent, and it is visible on side A, and on side B if
                                             						applicable. |
| Create a
                                             						Skill Group on the Administrative Workstation using the Cisco Skill Group
                                             						Explorer tool. After a few minutes, verify that the Skill Group was imported
                                             						into Unified CCDM. | The
                                             						Skill Group is visible on side A, and on side B if applicable. |
| Replication Tests for
                                                						  Dual-Sided Deployments |  |
| Log in
                                             						to the side B web server (Portal). Create a Skill Group to test Unified CCE
                                             						provisioning from the side B web server. Run this test for each configured
                                             						Unified CCE instance. | You can
                                             						successfully create the Skill Group, and it is visible on side A. |
| Create a
                                             						Skill Group on the Administrative Workstation using the Cisco Skill Group
                                             						Explorer tool. After a few minutes, verify that the Skill Group was imported
                                             						into Unified CCDM. | The
                                             						Skill Group is visible on side A and on side B. |
| Log in
                                             						to the side B web server (Portal). Create an IP phone to test Unified CM
                                             						provisioning from the side B web server. | The IP
                                             						phone is visible on side A and on side B. |

| Step 1 | Back up the
                                             			 Unified CVP Operations Console configuration. |
|---|---|
| Step 2 | Install the
                                             			 upgrade software. For more information, see the "Unified CVP Upgrade" chapter in the Installation and Upgrade Guide for Cisco Unified Customer Voice Portal : https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-guides-list.html . |

| Step 1 | Log in to the
                                             			 Operations Console. |
|---|---|
| Step 2 | Validate the
                                             			 version of each component. |
| Step 3 | Verify that
                                             			 all services are running. |
| Step 4 | Make a test
                                             			 inbound PSTN call to an agent. |

| Step 1 | Back up all
                                             			 the gateways. |
|---|---|
| Step 2 | Use the
                                             			 gateway consoles to back up component configurations. |
| Step 3 | Upgrade the
                                             			 gateways. |

| Step 1 | Enter the CLI
                                             			 command show
                                                				redundancy application group <RG Group Id> to determine which
                                             			 Session Border Controller (SBC) is Active. The Primary SBC is the Active
                                             			 chassis and the Secondary SBC is the Standby chassis. |
|---|---|
| Step 2 | Download the
                                             			 new software version to the Primary and Secondary SBCs. |
| Step 3 | On the
                                             			 Secondary SBC, enter the CLI command boot
                                                				system bootflash: <new image> to change the boot variable to
                                             			 point to the new image. |
| Step 4 | On the Primary SBC, perform an SBC sync from configuration mode. Enter the sbc configuration by running the CLI command sbc <name of SBC> and then run the CLI command sync . |
| Step 5 | On the
                                             			 Secondary SBC, enter the CLI command write
                                                				memory to save the running configuration. |
| Step 6 | On the
                                             			 Primary SBC, enter the CLI command redundancy > application redundancy > group # >
                                                				shutdown to shut down the redundancy group. The
                                             			 Secondary SBC immediately becomes the Active Cisco Unified Border Element and
                                             			 all active calls are preserved. There is no service outage when the switchover
                                             			 of the Active SBC takes place. |
| Step 7 | On the
                                             			 Primary SBC, change the boot variable to point to new software image and save
                                             			 the running configuration. |
| Step 8 | Reload the
                                             			 Primary chassis for upgrade and wait for this SBC to come up with upgraded
                                             			 version. It can
                                             			 take 10 to 12 minutes after the box is reloaded before the SBC reinitializes
                                             			 with the upgraded version. |
| Step 9 | On the Secondary SBC, shut down the redundancy and immediately run the CLI command no shutdown of the redundancy group on the Primary SBC. Keep the duration between shutting down the redundancy group in the Secondary
                                             SBC and the no shutdown command in the Primary box as minimal as possible. This step causes a service outage of approximately 4 minutes. The Primary box becomes the Active Cisco Unified Border Element
                                             (SP Edition) with upgraded software and starts servicing the calls. |
| Step 10 | Save the
                                             			 running configuration in the Primary SBC. |
| Step 11 | Reload the
                                             			 Secondary chassis for upgrade. When prompted to save the configuration before
                                             			 proceeding with the reload, enter “No” so that after the upgrade the Secondary
                                             			 SBC comes up in Standby mode. |

| Step 1 | Use Telnet or
                                             			 SSH to access the gateways and verify the version you upgraded to. |
|---|---|
| Step 2 | Make an
                                             			 inbound call to an agent and verify the prompts. You can run the debug
                                                				voip dial peer command to ensure that the inbound call uses the
                                             			 correct dial peer. |

| Step 1 | Upgrade the
                                             			 Administration and Data server that is connected to Side A. For
                                             			 more information, see the "Migrate HDS Database and Upgrade the Unified CCE
                                             			 Administration & Data Server" topic. |
|---|---|
| Step 2 | Perform the Database Performance Enhancement. For more information, see the Database Performance Enhancement section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| Step 3 | Bring the Side
                                             			 A logger and call router into service. For
                                             			 more information, see the "Bring Upgraded Side A into Service" topic. |
| Step 4 | Upgrade Cisco
                                             			 Unified Intelligence Center reporting templates. For more information, see the Installation and Upgrade Guide for Cisco Unified Intelligence Center at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-intelligence-center/products-installation-guides-list.html . |
| Step 5 | Upgrade the
                                             			 Unified CCE Administration Client. For more information, see the "Upgrade Unified CCE Administration Client" topic. |
| Step 6 | Upgrade the gateways. For more information, see the "Upgrade Peripheral Gateways" section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide : https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| Step 7 | Upgrade the Outbound Option Dialer. For more information, see the "Upgrade Outbound Option Dialer" section in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide : https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |
| Step 8 | Upgrade the CTI server. For more information, see the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide : https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html |

| Step 1 | Open the Unified OS
                                             			 Administration web page at the following URL, where [server-name] is the
                                             			 hostname or IP address of the node: https://[server-name]/cmplatform . |
|---|---|
| Step 2 | Sign in with administrator credentials. |
| Step 3 | Navigate to Settings > Version and verify the software version on the active and inactive partitions. |

| Note | ES42 provides the ability to
                                                					connect a maximum of two versions of Finesse to the same PG during the upgrade
                                                					or migration process to facilitate the migration of agentsand supervisors to the
                                                					new Finesse version. However, this mode of operation isnot supported for
                                                					production use beyond the upgrade or migration phase. |
|---|---|

| Step 1 | Ensure that
                                             			 the version of Finesse is the version you upgraded to. From the command line
                                             			 interface, you can run the show status command to verify the version. |
|---|---|
| Step 2 | In the Finesse
                                             			 console, verify that all services are up. |
| Step 3 | Log in to an
                                             			 agent and run desktop-initiated tests such as Call Hold, Transfer, and
                                             			 Conference. |

| Step 1 | Validate the
                                             			 version of each desktop. |
|---|---|
| Step 2 | Sign in to an
                                             			 agent and run desktop-initiated tests such as Call Hold, Transfer, and
                                             			 Conference. |

| Step 1 | Log into Cisco Virtualized
                                                			 Voice Browser portal. |
|---|---|
| Step 2 | Check the existing configuration. |

| Step 1 | Upgrade Cisco
                                             			 Unified CM. For more information, see the Upgrade Guide for Cisco Unified Communications Manager : https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-installation-guides-list.html . |
|---|---|
| Step 2 | Uninstall and
                                             			 then reinstall the JTAPI client on the Cisco Unified CM peripheral gateway. For more information, see the "Upgrade Cisco JTAPI Client on the Unified Communications Manager PG" topic in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide : https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |

| Step 1 | In Cisco Unified CDM, add an IP phone. For more information, see the Cisco Hosted Collaboration Solution End-User Provisioning Guide : https://www.cisco.com/c/en/us/support/unified-communications/hosted-collaboration-solution-hcs/tsd-products-support-series-home.html . |
|---|---|
| Step 2 | In Cisco
                                             			 Unified CM, verify that the phone was added. |