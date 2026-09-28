---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-configuration-guide-pcce-b-admi-c6fecc0267
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/configuration/guide/pcce_b_admin-and-config-guide_12_5/pcce_b_admin-and-config-guide_12_5_chapter_010110.html
retrieved_at: 2026-08-21T04:43:55.929905+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.5(1)

Updated: June 11, 2024

Chapter: Post Technology Refresh Configurations

## Chapter: Post Technology Refresh Configurations

# Post Technology Refresh Configurations

## Packaged CCE 2000 Agents Deployment

### Single-stage Configurations

Prerequisite:

Upload CA Certificates or import Self-signed Certificates Self-signed Certificates of upgraded components.

The following table outlines the post-upgrade configurations required for components.

If you have changed the IP address or hostname of a component, update the inventory for the respective component. For more
                                                information, see Update Inventory.

If you have rebuilt components, follow the tasks detailed in the following table.

Sequence

Task

1

Update Inventory

2

Configure CCE Components

3

Configure External HDS (optional)

4

Configure Customer Voice Portal

5

Configure Cisco Unified Customer Voice Portal Reporting Server (optional)

6

Configure Cisco IOS Enterprise Voice Gateway

7

Email and Chat (optional)

8

Configure Cisco Finesse

9

Configure Cisco Unified Intelligence Center

10

Configure Cisco Identity Service

11

Configure Cisco Unified Communications Manager

12

Register with Cisco Smart Software Manager

13

Complete Upgrade on the Destination Server

14

Synchronize Source Server to the Destination Server

#### Update Inventory

After you perform a Technology Refresh upgrade, sign in to the Unified CCE Administration of Principal AW on the destination server. On the Inventory page, you can update the IP address or hostname, and choose to rebuild Virtual Machines (VMs) for the upgraded solution components.
                                    For more information, see Update IP Address or Hostname .

While you are updating the Inventory file , ensure to do the following:

If you are upgrading a hardware, update the VMWare ESXi server Side A host details (including HW layout) and Side B host details
                                                            (without HW layout) in the VM_HOST machine type. This update has to be done along with other core machines.

If you are upgrading a hardware from M4 Tested Reference Configuration to M5 Tested Reference Configuration, provide M5TRC as the HW layout. You can move from M3/M4 Tested Reference Configuration to M5 Tested Reference Configuration or Specification
                                                            Based Configuration, but vice versa is not supported.

Update all Core machines with required details before updating Optional machines.

When you update the inventory for Rogger, AW-HDS-DDS, and PG, the Unified CCE services on these components get activated automatically.

Set the isReinstalled value to yes if you are setting up a new VM.

If you wish to use CUCM Publisher from the source server, you can either reuse the existing application user or create a new
                                                            application user. To reuse the existing application user, provide the credentials of this user in the connectionInfo column while updating the CCE_PG . To create a new application user, provide a unique userName and password .

Do not delete any components while the Technology Refresh upgrade is in progress.

A banner appears on the Overview or Inventory page indicating that the Inventory has machines with IP address or hostnames not configured.

A banner appears on the Inventory page when the hardware refresh is in progress, providing an option to sync-all and cutover . It indicates that all AWs and both sides of Rogger, Logger, and Router are configured with correct IP address or hostnames.

#### Configure CCE Components

The following table outlines the configuration tasks required for CCE components in Packaged CCE 2000 Agent deployments.

Sequence

Task

1

Configure SQL Server for CCE Components

2

Configure Cisco SNMP Setup for Rogger (optional)

#### Configure External HDS

The following table outlines the configuration tasks required for External HDS in Packaged CCE deployments.

Sequence

Task

1

Configure SQL Server for CCE Components

2

Cisco SNMP Setup

#### Configure Customer Voice Portal

The CVP configurations are site specific. Side A and Side B configurations per site must be the same.

Configuration Tasks

For CVP security details, see Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Configure SNMP

#### Solution Synchronization and Cutover

##### Synchronize Source Server to the Destination Server

During the staging and testing of the destination systems, the source servers continue to process calls. On the day of the
                                    cutover, the data in the destination servers can be updated with that of the source server, by running the EDMT tool on Logger,
                                    BA, AW, and HDS database on the destination servers.

This updates the database with production server schema version. However, due to the 12.5(1) database schema version being
                                    different from the production server schema version, the updated database is incompatible with 12.5(1). The administrator
                                    would have to manually use upgrade.exe utility to upgrade the database schema before starting the CCE Logger or Distributor
                                    service.

The utility is present in the icm\bin folder, and needs to be run against each of the database that was updated from the production server.

Perform the following steps to use the Upgrade.exe Utility:

<Install Drive>: \icm\bin>upgrade.exe -s <Server Name> -d <Database name> -dt <Database Type> -i <Instance Name> where <Database Type> - can be either " logger " or " hds ", depending on the database that requires the schema to be upgraded.

For Example C:\icm\bin>upgrade -s PRGR-A -d abc_sideA -dt logger -i abc

# - The value as stored in columns Major , CCMinor , and AWMinor of Version table in the CCE database.

Take a backup of Logger and AW-HDS-DDS databases on the destination server before synchronization.

Stop the Router, Logger, AW-HDS, and Apache Tomcat services on the destination servers before running EDMT tool while changing
                                                      over to synchronize.

After each EDMT run, start the Router, Logger, AW-HDS, and Apache Tomcat services and do a manual synchronization on the destination
                                                      server in the inventory. For more information, see Synchronize Components on the Destination Server using Inventory .

To be in sync with configuration details of the source server, EDMT can be run multiple times on the destination server. However,
                                                      after first synchronization, if any of the following configuration changes are done in the CCE Administration on the source
                                                      server, the changes won’t reflect on the destination server in subsequent synchronizations. So, these updates have to be manually
                                                      configured on the destination server.

Cloud Connect integration, Default Media Server settings, Courtesy Callback, SIP Server Group, Route Pattern, and Locations

Addition, modification, or deletion of machines in the inventory

##### Synchronize Components on the Destination Server using Inventory

You can do a full synchronization of all components (using sync-all ) from Principal AW; however it cannot be
                                                   initiated after the cutover is completed.

Step 1

Navigate to Unified CCE Administration > Infrastructure > Inventory .

Step 2

On the banner message, click sync-all .

Step 3

Click Next to confirm initiating full synchronization.

Full synchronization may take several minutes.

Step 4

After the successful initiation of synchronization, click Done .

If initiation of synchronization fails, an error message appears. Click Close to exit and fix the error as required.

##### Complete Upgrade on the Destination Server

Step 1

Navigate to the Unified CCE Administration > Infrastructure > Inventory .

Step 2

On the banner message, click cutover .

Step 3

Click Next to initiate validations for cutover.

If validations are successful, click Next to confirm initiating cutover.

If validations fail, an error message appears. Click the x icon to exit and fix the errors as required.

Step 4

After the successful completion of cutover, click Done .

## Packaged CCE 4000 Agents Deployment

### Single-stage Configurations

Prerequisite:

Upload CA Certificates or import Self-signed Certificates Self-signed Certificates of upgraded components.

The following table outlines the post-upgrade configurations required for components.

If you have changed the IP address or hostname of a component, update the inventory for the respective component. For more
                                                information, see Update IP Address or Hostname .

If you have rebuilt components, follow the tasks detailed in the following table.

Sequence

Task

1

Update Inventory

2

Configure CCE Components

3

Configure External HDS (optional)

4

Configure Cisco Unified Customer Voice Portal

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

Configure Cisco IOS Enterprise Voice Gateway

12

Configure Enterprise Chat and Email (ECE) (optional)

Email and Chat

13

14

Register with Cisco Smart Software Manager

15

Complete Upgrade on the Destination Server

16

Synchronize Source Server to the Destination Server

#### Configure CCE Components

The following table outlines the configuration tasks required for CCE components in Packaged CCE 4000 Agent deployments.

Sequence

Task

1

Configure SQL Server for CCE Components

2

Configure Cisco SNMP Setup for Rogger (optional)

3

Configure Cisco SNMP Setup for AW-HDS-DDS (optional)

#### Configure Cisco Unified Customer Voice Portal

The following table outlines the Cisco Unified Customer Voice Portal (CVP) configuration tasks for Packaged CCE 4000 or 12000
                                 Agent deployments.

The CVP configurations are site specific. Side A and Side B configurations per site must be the same.

Configuration Tasks

For CVP security details, see Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html .

Configure SNMP

#### Configure Customer Collaboration Platform(CCP)

Follow the steps to create new feed for task routing, associate the feed to the
                                    campaigns and configure the CCE for Multichannel Routing Collaboration Platform.

Step 1

Sign in to Unified Customer Collaboration Platform(CCP) with your Customer
                                             Collaboration Platform administrator account (https://<hostname/ IP address
                                             of CCP).

Step 2

In Customer Collaboration Platform, click on the Configuration tab.

Manage Feeds and Manage
                                                   Campaigns screens are displayed.

Step 3

In the left panel, on Manage Feeds screen, click on New and create a new feed.

Step 4

In the right panel of the Manage Campaigns screen, click on New and create a new campaign.

You can create a new campaign and associate the available feed.

From the Administration tab, you can also associate the notificaitons to the
                                                campaign.

Step 5

In the Administration page, select CCE Configuration for
                                                Multichannel Routing .

Provide the details of Media Routing PG for Host Side A and Host Side B, and
                                                enter the port values.  Click Save.

### Multistage Configurations

Prerequisite:

Upload CA Certificates or import Self-Signed Certificates of upgraded components.

The following table outlines the post-upgrade configurations required for each component.

If you have changed the IP address or hostname of a component, update the inventory for the respective component. For more
                                                information, see Update IP Address or Hostname .

If you have rebuilt components, follow the tasks detailed in the following table.

Sequence

Components

Task

1

Cisco Identity Service

Update Core Machines

Configure Cisco Identity Service

2

Configure Enterprise Chat and Email (ECE) (optional)

Update Optional Machines

Email and Chat

3

Cisco Finesse

Update Peripheral Set

Configure Cisco Finesse

4

Cisco Unified Customer Voice Portal (CVP)

Update Peripheral Set

Configure Cisco Unified Customer Voice Portal

Configure Cisco Unified Customer Voice Portal Reporting Server (optional)

5

Cisco Virtualized Voice Browser

Update Optional Machines

6

Cisco IOS Enterprise Voice Gateways

Update Optional Machines

Configure Cisco IOS Enterprise Voice Gateway

7

Cisco Unified Intelligence Center

Update Core Machines

Configure Cisco Unified Intelligence Center

8

CCE Central Controller (CCE_AW, CCE_ROGGER 1 , CCE_ROUTER, CCE_LOGGER 2 )

Update Inventory

Configure CCE Components

9

External HDS (optional)

Update Optional Machines

Configure External HDS

10

Cisco Live Data

Update Core Machines

Configure Live Data

11

Peripheral Gateways

Update Peripheral Set

12

Customer Collaboration Platform

Update Optional Machines

Update IP Address or Hostname

Configure Customer Collaboration Platform(CCP)

13

Cisco Unified Communications Manager

Update Peripheral Set

Configure Cisco Unified Communications Manager

14

Cloud Connect

Update Optional Machines

12

CUSP

13

Third Party Multichannel

14

Not applicable

Register with Cisco Smart Software Manager

15

Complete Upgrade on the Destination Server

16

Synchronize Source Server to the Destination Server

#### Update Inventory

After you perform a Technology Refresh upgrade, sign in to the Unified CCE Administration of Principal AW on the destination
                                    server. On the Inventory page, you can update the IP address or hostname, and choose to rebuild Virtual Machines (VMs) for
                                    the upgraded solution components. For more information, see Update IP Address or Hostname .

While you are updating the Inventory file , ensure to do the following:

Update all Core machines with required details before updating the Peripheral Set or Optional machines.

Set the isReinstalled value to yes if you are setting up a new VM.

In multistage Technology Refresh, during the Central Controller upgrade, EDMT invalidates all the component IP addresses.
                                                So, you must update the inventory for all components after upgrading the Central Controller.

When you update the inventory for Rogger 3 , Router, Logger 4 , AW-HDS-DDS, and PG, the Unified CCE services on these components get activated automatically.

Do not delete any components while the Technology Refresh upgrade is in progress.

A banner appears on the Overview or Inventory page indicating that the inventory has machines with IP address or hostnames not configured.

A banner appears on the Inventory page when the hardware refresh is in progress, providing an option to sync-all and cutover . It indicates that all AWs and both sides of Rogger, Logger, and Router are configured with correct IP address or hostnames.

## Packaged CCE 12000 Agents Deployment

### Single-stage Configurations

Prerequisite:

Upload CA Certificates or import Self-signed Certificates Self-signed Certificates of upgraded components.

The following table outlines the post-upgrade configurations required for components.

If you have changed the IP address or hostname of a component, update the inventory for the respective component. For more
                                                information, see Update IP Address or Hostname .

If you have rebuilt components, follow the tasks detailed in the following table.

Sequence

Task

1

Update Inventory

2

Configure CCE Components

3

Configure External HDS (optional)

4

Configure Cisco Unified Customer Voice Portal

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

Configure Cisco IOS Enterprise Voice Gateway

12

Configure Enterprise Chat and Email (ECE) (optional)

Email and Chat

13

Configure Customer Collaboration Platform(CCP) (optional)

14

Register with Cisco Smart Software Manager

15

Complete Upgrade on the Destination Server

16

Synchronize Source Server to the Destination Server

#### Configure CCE Components

The following table outlines the configuration tasks required for CCE components in Packaged CCE 12000 Agent deployments.

CCE Components

Task

1

Configure SQL Server for CCE Components

2

Configure Cisco SNMP Setup for Logger (optional)

3

Configure Cisco SNMP Setup for Router (optional)

4

Configure Cisco SNMP Setup for HDS-DSS (optional)

5

Configure Cisco SNMP Setup for AW-HDS (optional)

### Multistage Configurations

Prerequisite:

Upload CA Certificates or import Self-signed Certificates Self-signed Certificates of upgraded components.

The following table outlines the post-upgrade configurations required for each component.

If you have changed the IP address or hostname of a component, update the inventory for the respective component. For more
                                                information, see Update IP Address or Hostname .

If you have rebuilt components, follow the tasks detailed in the following table.

Sequence

Components

Task

1

Cisco Identity Service

Update Core Machines

Configure Cisco Identity Service

2

Configure Enterprise Chat and Email (ECE) (optional)

Update Optional Machines

Email and Chat

3

Cisco Finesse

Update Peripheral Set

Configure Cisco Finesse

4

Cisco Unified Customer Voice Portal (CVP)

Update Peripheral Set

Configure Cisco Unified Customer Voice Portal

Configure Cisco Unified Customer Voice Portal Reporting Server (optional)

5

Cisco Virtualized Voice Browser

Update Optional Machines

6

Cisco IOS Enterprise Voice Gateways

Update Optional Machines

Configure Cisco IOS Enterprise Voice Gateway

7

Cisco Unified Intelligence Center

Update Core Machines

Configure Cisco Unified Intelligence Center

8

CCE Central Controller (CCE_AW, CCE_ROGGER 5 , CCE_ROUTER, nd CCE_LOGGER 6 )

Update Inventory

Configure CCE Components

9

External HDS (optional)

Update Optional Machines

Configure External HDS

10

Cisco Live Data

Update Core Machines

Configure Live Data

11

Peripheral Gateways

Update Peripheral Set

12

Customer Collaboration Platform

Update Optional Machines

Update IP Address or Hostname

Configure Customer Collaboration Platform(CCP)

13

Cisco Unified Communications Manager

Update Peripheral Set

Configure Cisco Unified Communications Manager

14

Cloud Connect

Update Optional Machines

12

CUSP

13

Third Party Multichannel

14

Not applicable

Register with Cisco Smart Software Manager

15

Complete Upgrade on the Destination Server

16

Synchronize Source Server to the Destination Server

## Packaged CCE Lab Only Deployments

This section provides information about the post-upgrade configurations required for components in Packaged CCE Lab Only deployments.

Packaged CCE Lab Only deployments can be configured as simplex systems or duplex systems in 2000 Agent deployments. For more
                           information on the required configurations, see Single-stage Configurations .

| Note | If you have changed the IP address or hostname of a component, update the inventory for the respective component. For more
                                                information, see Update Inventory. If you have rebuilt components, follow the tasks detailed in the following table. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Update Inventory |
| 2 | Configure CCE Components |
| 3 | Configure External HDS (optional) |
| 4 | Configure Customer Voice Portal |
| 5 | Configure Cisco Unified Customer Voice Portal Reporting Server (optional) |
| 6 | Configure Cisco IOS Enterprise Voice Gateway |
| 7 | Email and Chat (optional) |
| 8 | Configure Cisco Finesse |
| 9 | Configure Cisco Unified Intelligence Center |
| 10 | Configure Cisco Identity Service |
| 11 | Configure Cisco Unified Communications Manager |
| 12 | Register with Cisco Smart Software Manager |
| 13 | Complete Upgrade on the Destination Server |
| 14 | Synchronize Source Server to the Destination Server |

| Note | While you are updating the Inventory file , ensure to do the following: If you are upgrading a hardware, update the VMWare ESXi server Side A host details (including HW layout) and Side B host details
                                                            (without HW layout) in the VM_HOST machine type. This update has to be done along with other core machines. If you are upgrading a hardware from M4 Tested Reference Configuration to M5 Tested Reference Configuration, provide M5TRC as the HW layout. You can move from M3/M4 Tested Reference Configuration to M5 Tested Reference Configuration or Specification
                                                            Based Configuration, but vice versa is not supported. Update all Core machines with required details before updating Optional machines. When you update the inventory for Rogger, AW-HDS-DDS, and PG, the Unified CCE services on these components get activated automatically. Set the isReinstalled value to yes if you are setting up a new VM. If you wish to use CUCM Publisher from the source server, you can either reuse the existing application user or create a new
                                                            application user. To reuse the existing application user, provide the credentials of this user in the connectionInfo column while updating the CCE_PG . To create a new application user, provide a unique userName and password . Do not delete any components while the Technology Refresh upgrade is in progress. A banner appears on the Overview or Inventory page indicating that the Inventory has machines with IP address or hostnames not configured. A banner appears on the Inventory page when the hardware refresh is in progress, providing an option to sync-all and cutover . It indicates that all AWs and both sides of Rogger, Logger, and Router are configured with correct IP address or hostnames. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Configure SQL Server for CCE Components |
| 2 | Configure Cisco SNMP Setup for Rogger (optional) |

| Sequence | Task |
|---|---|
| 1 | Configure SQL Server for CCE Components |
| 2 | Cisco SNMP Setup |

| Note | The CVP configurations are site specific. Side A and Side B configurations per site must be the same. |
|---|---|

| Configuration Tasks |
|---|
| For CVP security details, see Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Configure SNMP |

| Note | Take a backup of Logger and AW-HDS-DDS databases on the destination server before synchronization. Stop the Router, Logger, AW-HDS, and Apache Tomcat services on the destination servers before running EDMT tool while changing
                                                      over to synchronize. After each EDMT run, start the Router, Logger, AW-HDS, and Apache Tomcat services and do a manual synchronization on the destination
                                                      server in the inventory. For more information, see Synchronize Components on the Destination Server using Inventory . To be in sync with configuration details of the source server, EDMT can be run multiple times on the destination server. However,
                                                      after first synchronization, if any of the following configuration changes are done in the CCE Administration on the source
                                                      server, the changes won’t reflect on the destination server in subsequent synchronizations. So, these updates have to be manually
                                                      configured on the destination server. Cloud Connect integration, Default Media Server settings, Courtesy Callback, SIP Server Group, Route Pattern, and Locations Addition, modification, or deletion of machines in the inventory |
|---|---|

| Note | You can do a full synchronization of all components (using sync-all ) from Principal AW; however it cannot be
                                                   initiated after the cutover is completed. |
|---|---|

| Step 1 | Navigate to Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | On the banner message, click sync-all . |
| Step 3 | Click Next to confirm initiating full synchronization. Full synchronization may take several minutes. |
| Step 4 | After the successful initiation of synchronization, click Done . If initiation of synchronization fails, an error message appears. Click Close to exit and fix the error as required. |

| Step 1 | Navigate to the Unified CCE Administration > Infrastructure > Inventory . |
|---|---|
| Step 2 | On the banner message, click cutover . |
| Step 3 | Click Next to initiate validations for cutover. If validations are successful, click Next to confirm initiating cutover. If validations fail, an error message appears. Click the x icon to exit and fix the errors as required. |
| Step 4 | After the successful completion of cutover, click Done . |

| Note | If you have changed the IP address or hostname of a component, update the inventory for the respective component. For more
                                                information, see Update IP Address or Hostname . If you have rebuilt components, follow the tasks detailed in the following table. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Update Inventory |
| 2 | Configure CCE Components |
| 3 | Configure External HDS (optional) |
| 4 | Configure Cisco Unified Customer Voice Portal |
| 5 | Configure Cisco Unified Communications Manager |
| 6 | Configure Cisco Unified Intelligence Center |
| 7 | Configure Cisco Finesse |
| 8 | Configure Live Data |
| 9 | Configure Cisco Identity Service |
| 10 | Configure Cisco Unified Customer Voice Portal Reporting Server (optional) |
| 11 | Configure Cisco IOS Enterprise Voice Gateway |
| 12 | Configure Enterprise Chat and Email (ECE) (optional) Email and Chat |
| 13 | Configure Customer Collaboration Platform(CCP) (optional) |
| 14 | Register with Cisco Smart Software Manager |
| 15 | Complete Upgrade on the Destination Server |
| 16 | Synchronize Source Server to the Destination Server |

| Sequence | Task |
|---|---|
| 1 | Configure SQL Server for CCE Components |
| 2 | Configure Cisco SNMP Setup for Rogger (optional) |
| 3 | Configure Cisco SNMP Setup for AW-HDS-DDS (optional) |

| Note | The CVP configurations are site specific. Side A and Side B configurations per site must be the same. |
|---|---|

| Configuration Tasks |
|---|
| For CVP security details, see Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html . |
| Configure SNMP |

| Step 1 | Sign in to Unified Customer Collaboration Platform(CCP) with your Customer
                                             Collaboration Platform administrator account (https://<hostname/ IP address
                                             of CCP). |
|---|---|
| Step 2 | In Customer Collaboration Platform, click on the Configuration tab. Manage Feeds and Manage
                                                   Campaigns screens are displayed. |
| Step 3 | In the left panel, on Manage Feeds screen, click on New and create a new feed. |
| Step 4 | In the right panel of the Manage Campaigns screen, click on New and create a new campaign. You can create a new campaign and associate the available feed. From the Administration tab, you can also associate the notificaitons to the
                                                campaign. |
| Step 5 | In the Administration page, select CCE Configuration for
                                                Multichannel Routing . Provide the details of Media Routing PG for Host Side A and Host Side B, and
                                                enter the port values.  Click Save. |

| Note | If you have changed the IP address or hostname of a component, update the inventory for the respective component. For more
                                                information, see Update IP Address or Hostname . If you have rebuilt components, follow the tasks detailed in the following table. |
|---|---|

| Sequence | Components | Task |
|---|---|---|
| 1 | Cisco Identity Service | Update Core Machines Configure Cisco Identity Service |
| 2 | Configure Enterprise Chat and Email (ECE) (optional) | Update Optional Machines Email and Chat |
| 3 | Cisco Finesse | Update Peripheral Set Configure Cisco Finesse |
| 4 | Cisco Unified Customer Voice Portal (CVP) | Update Peripheral Set Configure Cisco Unified Customer Voice Portal Configure Cisco Unified Customer Voice Portal Reporting Server (optional) |
| 5 | Cisco Virtualized Voice Browser | Update Optional Machines |
| 6 | Cisco IOS Enterprise Voice Gateways | Update Optional Machines Configure Cisco IOS Enterprise Voice Gateway |
| 7 | Cisco Unified Intelligence Center | Update Core Machines Configure Cisco Unified Intelligence Center |
| 8 | CCE Central Controller (CCE_AW, CCE_ROGGER 1 , CCE_ROUTER, CCE_LOGGER 2 ) | Update Inventory Configure CCE Components |
| 9 | External HDS (optional) | Update Optional Machines Configure External HDS |
| 10 | Cisco Live Data | Update Core Machines Configure Live Data |
| 11 | Peripheral Gateways | Update Peripheral Set |
| 12 | Customer Collaboration Platform | Update Optional Machines Update IP Address or Hostname Configure Customer Collaboration Platform(CCP) |
| 13 | Cisco Unified Communications Manager | Update Peripheral Set Configure Cisco Unified Communications Manager |
| 14 | Cloud Connect | Update Optional Machines |
| 12 | CUSP |
| 13 | Third Party Multichannel |
| 14 | Not applicable | Register with Cisco Smart Software Manager |
| 15 | Complete Upgrade on the Destination Server |
| 16 | Synchronize Source Server to the Destination Server |

| Note | If you have changed the IP address or hostname of a component, update the inventory for the respective component. For more
                                                information, see Update IP Address or Hostname . If you have rebuilt components, follow the tasks detailed in the following table. |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Update Inventory |
| 2 | Configure CCE Components |
| 3 | Configure External HDS (optional) |
| 4 | Configure Cisco Unified Customer Voice Portal |
| 5 | Configure Cisco Unified Communications Manager |
| 6 | Configure Cisco Unified Intelligence Center |
| 7 | Configure Cisco Finesse |
| 8 | Configure Live Data |
| 9 | Configure Cisco Identity Service |
| 10 | Configure Cisco Unified Customer Voice Portal Reporting Server (optional) |
| 11 | Configure Cisco IOS Enterprise Voice Gateway |
| 12 | Configure Enterprise Chat and Email (ECE) (optional) Email and Chat |
| 13 | Configure Customer Collaboration Platform(CCP) (optional) |
| 14 | Register with Cisco Smart Software Manager |
| 15 | Complete Upgrade on the Destination Server |
| 16 | Synchronize Source Server to the Destination Server |

| CCE Components | Task |
|---|---|
| 1 | Configure SQL Server for CCE Components |
| 2 | Configure Cisco SNMP Setup for Logger (optional) |
| 3 | Configure Cisco SNMP Setup for Router (optional) |
| 4 | Configure Cisco SNMP Setup for HDS-DSS (optional) |
| 5 | Configure Cisco SNMP Setup for AW-HDS (optional) |

| Note | If you have changed the IP address or hostname of a component, update the inventory for the respective component. For more
                                                information, see Update IP Address or Hostname . If you have rebuilt components, follow the tasks detailed in the following table. |
|---|---|

| Sequence | Components | Task |
|---|---|---|
| 1 | Cisco Identity Service | Update Core Machines Configure Cisco Identity Service |
| 2 | Configure Enterprise Chat and Email (ECE) (optional) | Update Optional Machines Email and Chat |
| 3 | Cisco Finesse | Update Peripheral Set Configure Cisco Finesse |
| 4 | Cisco Unified Customer Voice Portal (CVP) | Update Peripheral Set Configure Cisco Unified Customer Voice Portal Configure Cisco Unified Customer Voice Portal Reporting Server (optional) |
| 5 | Cisco Virtualized Voice Browser | Update Optional Machines |
| 6 | Cisco IOS Enterprise Voice Gateways | Update Optional Machines Configure Cisco IOS Enterprise Voice Gateway |
| 7 | Cisco Unified Intelligence Center | Update Core Machines Configure Cisco Unified Intelligence Center |
| 8 | CCE Central Controller (CCE_AW, CCE_ROGGER 5 , CCE_ROUTER, nd CCE_LOGGER 6 ) | Update Inventory Configure CCE Components |
| 9 | External HDS (optional) | Update Optional Machines Configure External HDS |
| 10 | Cisco Live Data | Update Core Machines Configure Live Data |
| 11 | Peripheral Gateways | Update Peripheral Set |
| 12 | Customer Collaboration Platform | Update Optional Machines Update IP Address or Hostname Configure Customer Collaboration Platform(CCP) |
| 13 | Cisco Unified Communications Manager | Update Peripheral Set Configure Cisco Unified Communications Manager |
| 14 | Cloud Connect | Update Optional Machines |
| 12 | CUSP |
| 13 | Third Party Multichannel |
| 14 | Not applicable | Register with Cisco Smart Software Manager |
| 15 | Complete Upgrade on the Destination Server |
| 16 | Synchronize Source Server to the Destination Server |