---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-b351860750
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_pre-installation-planning-guide-for-cisco/ucce_m_icm-platform-planning126.html
retrieved_at: 2026-08-16T20:03:38.333097+00:00
---

Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.6(1)

# Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.6(1)

Updated: May 12, 2021

Chapter: ICM Platform Planning

## Chapter: ICM Platform Planning

# ICM Platform Planning

After you have the system sizing considerations, you can begin to order the appropriate
                        server configuration. First, however, determine how many Unified ICM nodes you need.

The number of servers required in a Unified ICM system depends on the configuration of
                        the central controller, PGs, NICs, and other nodes. For example, a duplexed central
                        controller configuration requires more servers because the CallRouter and Logger are
                        duplicated.

## Number of Servers Required

The following table shows how to determine the number of servers
                              		  required in your system.

The counts of servers in this example are based on an Unified ICM
                              		  configuration that has the following characteristics:

The Unified ICM system has a duplexed, geographically distributed
                                    				central controller (in other words, each central site has a CallRouter and a
                                    				Logger).

One side of the central controller (Central Site 1) is located at
                                    				a call center and consequently has a PG to serve one or more ACDs. The PG is
                                    				duplexed (two servers) for fault tolerance.

This Unified ICM installation has three remote call center sites
                                    				and two Admin sites.

Sites

Node Types

CallRtr

Lgr

Call/Lgr

DB Server

PG

Administration & Data Server with HDS

Central Site 1

1

1

-

-

2

1

Central Site 2

1

1

-

-

-

1

Remote Call Center 1

-----

-----

-----

-----

2

-

Remote Call Center 2

-----

-----

-----

-----

2

-

Remote Call Center 3

-----

-----

-----

-----

2

-

Admin Site 1

-----

-----

-----

-----

-----

1

Admin Site 2

-----

-----

-----

-----

-----

1

Total Nodes:

2

2

8

4

Key:

--------- These servers are not installed at this type of
                                          					 site.

– Not selected as an option in this particular configuration.

## ICM Platform
                        	 Considerations

For information on server configurations and examples of supported server platforms, see Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html .

### Processor Utilization

Required only in ICM Gateway SQL configurations.

As a general rule for all Unified ICM nodes, keep processor
                                 		  utilization below 60 percent of the maximum expected call load on the system.
                                 		  This is needed to smooth out call request "spikes" as well as to allow enough reserve capacity to perform
                                 		  activities such as re-synchronization and background cleanup. Non-ICM software
                                 		  can make up a part of the 60 percent maximum load. The processor utilization
                                 		  figure (60 percent) covers all software running on the platform.

In addition to the utilization requirement, no software on the system
                                 		  can run at a priority equal to or higher than the Unified ICM software for more
                                 		  than 100 milliseconds in uninterrupted bursts. In other words, the Unified ICM
                                 		  software needs to run on the system at least as frequently as once every 100
                                 		  milliseconds. This is usually not a problem unless device drivers or other
                                 		  kernel-level software is installed, or process/thread priorities have changed
                                 		  incorrectly.

### Paging
                           	 Requirements

The most
                                 		  time-critical component of the Unified ICM system, the CallRouter node, must
                                 		  not be delayed due to disk I/O (that is, paging). The only disk I/O that should
                                 		  be occurring on Unified ICM machines is for log file writes and database I/O.
                                 		  The database I/Os occur on Logger and Administration & Data Server
                                 		  machines. The simple rule is to provide enough main memory so that the entire
                                 		  working sets of critical processes remain in memory.

For complete and current information about RAM and other platform requirements, see the Virtualization information https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html .

Make sure the
                                 		  database platforms (Loggers, Administration & Data Servers, and Unified ICM
                                 		  Gateway SQL machines) have enough main memory so that all first level index
                                 		  pages are kept in main memory cache.

### Logger
                           	 Expansion

The Logger platform
                                 		  you order can include a combination of internal and external SCSI hard drives.
                                 		  As your call center enterprise grows, your database requirements typically grow
                                 		  as well. You may have more services, skill groups, and routes in your
                                 		  configuration, and you may route more calls each day. This database growth means more
                                 		  historical data stored in the central database.

When your database
                                 		  requirements change, contact your Unified ICM software support provider to have
                                 		  the storage capacity of the central database increased.

You can allocate
                                 		  more database space after you install your system by:

Remotely adding
                                       				database space (if current disk space allows).

Installing "hot-plugable" disk drives and configuring the disks while the
                                       				system is running.

### Administration and
                           	 Data Server Planning

To allow users to
                                 		  monitor current call center activity, the Unified ICM system forwards real-time
                                 		  data to Administration & Data Servers at selected sites throughout the call
                                 		  center enterprise. The following figure illustrates the real-time architecture
                                 		  of the Unified ICM system.

Real-time call and
                                 		  agent group status data arrives at the central controller from the Peripheral
                                 		  Gateways, which are constantly monitoring activity at each call center. The
                                 		  CallRouter acts as the real-time server. The CallRouter for the other side of
                                 		  the central controller acts as a back-up real-time server.

The CallRouter is
                                 		  responsible for providing real-time data to one or more Administration &
                                 		  Data Servers at each administrator site. Administration Clients at the site
                                 		  receive their real-time data through a connection to a Administration &
                                 		  Data Server. Administration Clients do not have the local database and
                                 		  Administration & Data Server processes are required to receive real-time
                                 		  data directly from the CallRouter.

### Administrator
                           	 Sites

Administration &
                                 		  Data Servers can be located with one or both sides of the central controller,
                                 		  at a call center, or at another site. An administrator site is any site that
                                 		  contains Administration & Data Servers. Each administrator site requires at
                                 		  least one Administration & Data Server. You should use two Administration
                                 		  & Data Servers (as shown in Administration and Data Server Planning ) to provide fault tolerance in the
                                 		  real-time data distribution architecture.

The primary
                                 		  Administration & Data Server maintains an active connection to the
                                 		  real-time server through which it receives real-time data. The secondary
                                 		  Administration & Data Server also maintains connections to the real-time
                                 		  server; however, these connections remain idle until needed (for example, in
                                 		  cases where the primary Administration & Data Server is unavailable for
                                 		  some reason). In sites that have two Administration & Data Servers, the
                                 		  Administration Clients are configured to automatically switch to a secondary
                                 		  Administration & Data Server if the first distributor becomes
                                 		  non-functional for any reason.

### Administration
                           	 Client Requirements

An Administration & Data Server can serve many Administration Clients. See the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html for information about requirements.

## Historical Data
                        	 Servers

Historical data is
                              		  stored both as individual call detail records and also rolled up and stored as
                              		  interval records. An Administration & Data Server with a Historical Data
                              		  Server (HDS) stores historical data that supports reporting queries.
                              		  Administration & Data Servers at the site query historical data from the
                              		  HDS rather than directly from the Logger.

To set up a
                              		  Historical Data Server, you must configure the Logger to perform historical
                              		  data replication. You must also configure the real-time Administration &
                              		  Data Server as an HDS. You can then create an HDS database on the real-time
                              		  distributor.

Information in the
                              		  real-time feed tells each Administration Client where to obtain historical
                              		  data. If the real-time distributor is a Historical Data Server, then it
                              		  instructs its clients to get historical data from it. Otherwise, it instructs
                              		  its clients to get historical data from the Logger.

Each Logger can
                              		  support up to two HDSs. The Administration Server, Real-time and Historical
                              		  Data Server, and Detail Data Server (AW-HDS-DDS) can be enabled only on the
                              		  primary distributor. The AW-HDS-DDS server role is disabled on the secondary
                              		  real-time Administration & Data Server.

### HDS Features

The HDS eliminates the performance impact on the central database from multiple Administration & Data Servers accessing the
                                 central database to generate reports. In systems that have multiple remote Administration & Data Servers, the HDS brings Unified
                                 ICM historical reporting data closer to the user. Each HDS provides a set of database tables. You can set specific times for
                                 retaining data in these tables. These capabilities give you flexibility in setting up reporting capabilities on a site-by-site
                                 basis.

The Historical Data
                                 		  Server also provides:

Greater
                                       				flexibility in leveraging Internet applications.

An open
                                       				interface for data mining and data warehousing applications.

Host for other
                                       				database tables and have them work with the HDS.

Improved
                                       				security and data access capabilities.

See the Contact Center Enterprise Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html for information on HDS requirements.

| Note | All contact center enterprise solutions must now run on virtual machines, they are no longer supported on bare hardware. For
                                 hardware requirements for Unified CCE virtualized systems, see the Solution Design Guide for Cisco Unified Contact Center Enterprise at http://www.cisco.com/en/US/products/sw/custcosw/ps1844/products_implementation_design_guides_list.html and Virtualization for Unified Contact Center Enterprise at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html . |
|---|---|

| Sites | Node Types |
|---|---|
|  | CallRtr | Lgr | Call/Lgr | DB Server | PG | Administration & Data Server with HDS |
| Central Site 1 | 1 | 1 | - | - | 2 | 1 |
| Central Site 2 | 1 | 1 | - | - | - | 1 |
| Remote Call Center 1 | ----- | ----- | ----- | ----- | 2 | - |
| Remote Call Center 2 | ----- | ----- | ----- | ----- | 2 | - |
| Remote Call Center 3 | ----- | ----- | ----- | ----- | 2 | - |
| Admin Site 1 | ----- | ----- | ----- | ----- | ----- | 1 |
| Admin Site 2 | ----- | ----- | ----- | ----- | ----- | 1 |
| Total Nodes: | 2 | 2 |  |  | 8 | 4 |
| Key: | --------- These servers are not installed at this type of
                                          					 site. – Not selected as an option in this particular configuration. |

| Note | Required only in ICM Gateway SQL configurations. |
|---|---|

| Note | For information about data storage in virtualized deployments, see Virtualization for Unified Contact Center Enterprise at http://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-unified-contact-center-enterprise.html . |
|---|---|

| Note | After you install the Unified ICM system, see Administration Guide for
                                             			 Cisco Unified ICM Enterprise for information on how to manage database
                                          		  space. |
|---|---|