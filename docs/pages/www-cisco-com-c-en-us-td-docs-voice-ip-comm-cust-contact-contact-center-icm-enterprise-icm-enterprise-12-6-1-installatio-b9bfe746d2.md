---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-installatio-b9bfe746d2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/installation/guide/ucce_b_pre-installation-planning-guide-for-cisco/ucce_m_icm-application-gateway-and-icm.html
retrieved_at: 2026-08-16T20:03:34.005396+00:00
---

Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.6(1)

# Pre-installation Planning Guide for Cisco Unified Intelligent Contact Management, Release 12.6(1)

Updated: May 12, 2021

Chapter: ICM Application
	 Gateway and ICM Gateway SQL planning

## Chapter: ICM Application
	 Gateway and ICM Gateway SQL planning

# ICM Application
                     	 Gateway and ICM Gateway SQL planning

The Unified ICM
                        		Application Gateway and Unified ICM Gateway SQL options allow Unified ICM to
                        		integrate external contact center applications into the Unified CCE. Each of
                        		these options involves some pre-installation planning. For example, you may
                        		need to prepare host systems and databases; review fault tolerance issues; and,
                        		in the case of Unified ICM Gateway SQL, plan for data transfer.

## ICM Application Gateway planning

The Unified ICM Application Gateway option allows the Unified ICM system to interface with any external call center application.
                              Within the Unified ICM software, the Unified ICM Application Gateway feature is implemented as a node in a call routing script.
                              You add a Gateway node to a script to instruct the Unified ICM to run an external application. This allows the script to evaluate
                              responses from an external application. The Unified ICM can then base subsequent routing decisions on the results produced
                              by the application.

A typical
                              Unified ICM Application Gateway application can return a variable to the
                              CallRouter that identifies the caller as having a certain type of account. The
                              script can then use this information to control where and how the call is
                              routed. Optionally, the Unified ICM software can pass the retrieved information
                              to the site that is receiving the call. In this case, certain data such as
                              account numbers, dates, billing phone numbers, and addresses are passed along
                              with the call to an answering resource.

### Host System
                           	 Preparation

To prepare for the
                                 		  Unified ICM Application Gateway option, you must set up the host system to
                                 		  communicate with the Unified ICM system. This involves configuring the host
                                 		  application to listen to a socket on the target Unified ICM machine. You also
                                 		  need to configure a name and port number to connect the host system to the
                                 		  Unified ICM central database. These steps are performed at system installation;
                                 		  however, you can begin preparing the host applications ahead of time.

During system
                                 		  installation, when connectivity between the Unified ICM system and host system
                                 		  is established, you must identify the host system to be queried by entering
                                 		  data in the Application_Gateway table.

### Fault
                           	 Tolerance

You can configure
                                 		  access to a single host application or duplicate host applications. In a single
                                 		  host configuration, configure the same host for both CallRouters (Side A and
                                 		  Side B). The single host method provides no protection against host failures;
                                 		  however, it does protect against connection failures.

In order to achieve
                                 		  a higher level of fault tolerance in an Unified ICM Application Gateway
                                 		  application, you can connect duplicate host applications to the CallRouter. For
                                 		  example, the Side A and Side B CallRouters can each manage a connection to one
                                 		  of the duplicated host applications. Each time a script initiates a request,
                                 		  both CallRouters query their corresponding host. The CallRouters use the
                                 		  response from the host that responds first. This method is highly reliable.
                                 		  Even if a host or a connection fails, all query requests are satisfied.

## ICM Gateway SQL
                        	 Planning

The Unified ICM
                              		  Gateway SQL option allows the CallRouter to query an external Microsoft SQL
                              		  Server database and use the data in call routing.

Before implementing the Gateway SQL and DB Lookup functionality, consider a Unified CVP VXML Application for database lookup
                                          instead. The DB Lookup node will interrupt routing while doing it's queries. The Unified CVP VXML Application will scale well.

If you are going to
                              		  use the Gateway SQL option, you need to review several pre-installation
                              		  planning issues:

Unified ICM
                                    				Gateway SQL requires an additional Database Server hardware platform.

Know the tasks
                                    				involved in setting up the external host database and populating it with the
                                    				data you want to use in call routing.

### Database Server Platform

The Unified ICM Gateway SQL option requires a host database server.
                                 		  Duplex the host database server to maintain Unified ICM fault tolerance. A
                                 		  duplexed Unified ICM Gateway SQL system requires two identical host database
                                 		  server platforms. Each host database server resides on the same LAN segment as
                                 		  its corresponding Unified ICM CallRouter. The following figure shows a duplexed
                                 		  Unified ICM system that has a duplexed Unified ICM Gateway SQL host database
                                 		  server.

### Data
                           	 Transfer

To prepare an
                                 		  Unified ICM system for Unified ICM Gateway SQL, you need to make several
                                 		  decisions:

Decide which data
                                 		  you want to use in the external database. For example, will you be using:

Customer
                                       				records?

Account
                                       				information?

Other types of
                                       				data?

Decide where the
                                 		  data is coming from:

Another
                                       				database?

A flat file?

Other sources?

Make a plan to
                                 		  transfer the data to the external database:

What type of
                                       				media will you use to transfer the data (tape, disk, network)?

Will the
                                       				transferred data be in a certain format (comma-separated values, text file,
                                       				Microsoft SQL Server syntax)?

### Database
                           	 Configuration Overview

For Unified ICM
                                 		  Gateway SQL, you must set up and configure one or more host databases to
                                 		  function with the Unified ICM system.

Configuration
                                 		  considerations include:

Choosing a host
                                       				database server platform. The host database server must have adequate
                                       				processing power and disk space. Cisco can provide you with specifications for
                                       				basic and high-end host database server platforms.

Setting up the
                                       				host database. This includes:

Installing a
                                       				Microsoft SQL Server

Creating a
                                             					 database on the host database server platform

Defining
                                             					 fields and indexes

Setting up
                                             					 permissions and replication

Transferring
                                       				data from a data source. Transfer data to populate the database with the data
                                       				to be used in call routing (for example, you might want to transfer customer
                                       				records to the database).

Configuring the
                                       				Unified ICM system to access the host database. Set up user names and passwords
                                       				that the Unified ICM system can use to access the data in the host database.

Writing test
                                       				scripts to test the Unified ICM Gateway SQL option. Monitor test scripts that
                                       				use the Script Editor DB Lookup node. The monitoring results are captured and
                                       				stored in the Route_Call_Detail table to validate that the Unified ICM Gateway
                                       				SQL feature is functioning.

| Note | Before implementing the Gateway SQL and DB Lookup functionality, consider a Unified CVP VXML Application for database lookup
                                          instead. The DB Lookup node will interrupt routing while doing it's queries. The Unified CVP VXML Application will scale well. |
|---|---|