---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-administrat-d250e704c1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/administration/guide/ucce_b_150_administration-guide-for-cisco-unified-contact-center-enterprise/ucce_m_150_database-administration.html
retrieved_at: 2026-08-16T20:44:39.712354+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise Release, 15.0(1)

# Administration Guide for Cisco Unified Contact Center Enterprise Release, 15.0(1)

Updated: July 31, 2026

Chapter: Database Administration

## Chapter: Database Administration

# Database Administration

## Unified CCE
                        	 Database Administration

When you install a new Logger, you create its central database. Create an HDS database on a real-time Administration & Data
                           Server. When you create a database, you specify the size of its data or log files. The data files must be sufficient for all
                           the data that you expect the database to hold. The size of the central and HDS databases depend on your call center traffic
                           and your data retention requirements.

For more information on how to perform a manual configuration for integrating AWDB with ECE , see the section Integrating ECE with Unified CCE in the Enterprise Chat and Email Installation and Configuration Guide .

The local database
                           		(awdb) contains configuration and real-time data, if the Administration &
                           		Data Server role includes a real-time server. Because the real-time data in the
                           		local database (awdb) are constantly overwritten by new data, the database size
                           		remains fairly constant.

Over time, the size of your enterprise or your call volumes can change significantly. Therefore, you might need to resize
                           the central and HDS databases to meet new requirements. You do not need to resize the local database (awdb). To resize the
                           local database (awdb), use the ICM Database Administration (ICMDBA) tool.

The data in the
                           		central database and HDS database grow as they accumulate historical data and
                           		call detail records. The growth is directly related to the following factors:

Size of the Unified ICM configuration; for example, how many services, skill groups, routes, and trunk groups are configured.

Call rate; that is, how many calls per day the system software is handling.

How long historical data is kept in the database.

The amount of
                           		configuration data directly affects the amount of historical data generated.
                           		The system software generates a new historical record every half hour for each
                           		service, skill group, route, trunk group, and so on, that is configured in the
                           		Unified ICM system.

You size and create
                           		the central and HDS databases after installing the system software. Use the
                           		Database Sizing Estimator applet for estimating the size of these databases,
                           		based on the expected usage.

If your
                           		configuration expands significantly or if you change the retention times for
                           		historical data, you might have to increase the size of the database. This
                           		increase might involve adding more disks to the system.

## Historical
                        	 Data

The system software
                           		initiates a purge process on the Logger once every day. By default, the purge
                           		process runs each night at 12:30 A.M. The purge process deletes records that
                           		are older than a specified number of retain days. When you set up the Logger
                           		using the Web Setup tool, you can modify the default retention time and purge
                           		schedule.

This table lists the default settings for retaining historical data.

Historical
                                       					 tables

Default
                                       					 retention time

Logger_Admin, Import_Rule_History, Persistent

30 days

Recovery

3650 days

All other
                                       					 historical tables

14 days

The following large
                           		historical tables are not purged by the system software but as a scheduled SQL
                           		Server Agent Job:

Agent_Event_Detail

Call_Type_SG_Interval

Dialer_Detail

Network_Event_Detail

Route_Call_Detail

Route_Call_Variable

Termination_Call_Detail

Termination_Call_Variable

Caution

SQL Server Agent
                                       		  Jobs are installed and enabled during the Unified CCE install and upgrade
                                       		  procedure. Do not stop these jobs while the system software is active. If you
                                       		  plan to stop the Logger and Administration & Data Server-hds component
                                       		  services for maintenance for more than a day, manually disable the Microsoft
                                       		  SQL Server jobs using the SQL Server enterprise management tool. Later, after
                                       		  the services are started, re-enable the jobs.

## Database Statistics

Maintaining accurate, up-to-date statistical details is essential to a well-run database environment and contributes to the
                           optimizer's efficient handling of work load. In some SQL Server-based environments, it is not unusual to see users rely on
                           the database itself to maintain statistics by using the Auto Create Statistics and Auto Update Statistics options. Setting
                           these options in an AW environment (with its rapid data turnover) results in a considerable effort being expended in updating
                           statistics. For that reason, users often schedule these options to run during off-peak hours. Because the database in the
                           AW environment is nearly empty during off-peak times,  however, statistics gathered then might not be as helpful as they would
                           be when collected at other, busier times.

Another option to consider for gathering statistics is the creation of a SQL Server Agent job that periodically runs the Microsoft
                           stored procedure sp_updatestats. The sp_updatestats procedure updates statistics as required for all user-defined and internal
                           tables in the current database and can be run on an hourly basis if workload and environment permit.

## Database
                        	 Administration Tool

Unified CCE includes
                           		the ICMDBA tool (icmdba.exe) in the \icm\bin folder. This tool provides a
                           		central utility to administer the Unified ICM databases. Use this tool to:

Create, edit, and delete central databases, local databases, and historical databases

Resize database files

Recreate databases

Import and export Unified ICM configuration data to and from databases

View database properties

In addition to these
                           		tasks, you can start or stop a server and do some limited SQL Server
                           		configuration.

Before using the
                                       		  ICMDBA tool, install the Unified CCE software. See the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide , for information on the Unified
                                       		  CCE installation.

The ICMDBA
                                       		  Import /Export feature works on Unified ICM configuration data only. To import
                                       		  or export Unified ICM historical data, use Microsoft’s SQL Server Database
                                       		  Backup and Database Restore utilities.

You start the ICMDBA
                           		either by double-clicking ICMDBA in the Unified CCE Tools folder or by
                           		selecting Start > Run > ICMDBA .

The main window is a
                           		tree hierarchy displaying the Unified ICM database servers in the current
                           		domain.

If you cannot find
                                       		  the server you want in the main window, you can select any computer on your
                                       		  local network by choosing File > Add
                                             				Computer .

Expanding the server
                           		name displays the Unified ICM instances that have databases on the server.
                           		Expanding the Unified ICM instance displays a specific Unified ICM node or
                           		nodes (Administration & Data Server and Logger) on machines that have
                           		databases for that instance. Expanding the node displays the databases
                           		associated with the node. Expanding the node database displays a list of the
                           		individual tables in the node database. Under databases are the table groups,
                           		and the final level lists the tables in the group.

You can create
                           		databases for instances with or without configured components. When an instance
                           		does not have configured components, database creation occurs under the
                           		instance within a component placeholder on the ICMDBA tree view.

To view the
                           		properties of a table, right-click the desired table in the list and select
                           		Properties from the context menu, or double-click the table in the list.

There are two ways
                           		to access the ICMDBA tool functions:

From the main window, select a node or database from the tree and then select a function from the menu bar menu.

Right-click a node or database to display a context menu.

### Create Database
                           	 with Configured Components

Use the Create
                                 		  function to create a database for an Administration & Data Server or
                                 		  Logger. You can only create one Logger database per side.

Step 1

With the
                                          			 Unified CCE running, for the server and instance, select the node
                                          			 (Administration & Data Server or Logger) where you want to create the
                                          			 database.

Step 2

Select Database > Create from the menu bar (or click the
                                          			 right mouse button and select Create ). The Create
                                             				Database window is displayed.

Step 3

Enter the
                                          			 following information for the database:

- DB Type —Specify
                                             				the type of database: Outbound Option for an outbound dialer, Administration & Database Server for a local
                                             				database (awdb), or Historical Data Server/Detail Data Server (HDS/DDS) for Administration & Data Server machines. For a Logger device, the default database type is
                                             				displayed (Logger side must be selected).

- ICM Type —Specify whether this is a Unified ICM or Unified CCE, or Unified ICMH system.

- Region —Specify
                                             				regional information where applicable.

Step 4

Select Add . This button invokes the Add
                                             				Device window.

Move the database log file to a separate virtual drive. By default, both the log file and database data file are installed
                                                         in \MSSQL\DATA on the virtual drive where you create the database. You can move the log file with SQL Server Management Studio.

By default,
                                                         				  the newly created data file is set to “Automatically Grow,” if it exceeds the
                                                         				  initially specified size. You can modify this setting, and the maximum
                                                         				  file size, with SQL Server Enterprise Manager. 
                                                         				Verify on the Files page in  SQL Server Enterprise Manager that the Autogrowth column shows:

Data files automatically grow in 100-MB increments.

Log files automatically grow in 10% increments.

Step 5

After you
                                          			 complete entering information in the Create Database window, select Create to close the window and create the
                                          			 database.

### Create Database
                           	 Without Configured Components

Use the Create
                                 		  function to create a database for an Administration & Data Server or
                                 		  Logger. You can only create one Logger database per side.

When an instance
                                             			 does not have any configured components, database creation occurs under the
                                             			 instance within a component placeholder.

Step 1

With Unified
                                          			 CCE running, for the server and instance, select the instance where you want to
                                          			 create the database.

Step 2

Select Database > Create from the menu bar (or click the
                                          			 right mouse button and select Create ). The Select
                                             				Component dialog appears.

Step 3

Select the Administration & Data Server , LoggerA , or LoggerB component and select OK .

Step 4

If you select LoggerA or LoggerB, the Select Logger type dialog appears, allowing you to select Enterprise . Select the logger type and select OK .

Step 5

Enter the
                                          			 following information for the database:

- DB Type —Specify
                                             				the type of database: Outbound Option for an outbound dialer, Administration & Database Server for a local
                                             				database (awdb), or Historical Data Server/Detail Data Server (HDS/DDS) for Administration & Data Server machines. For a Logger device, the default database type is
                                             				displayed (Logger side must be selected).

- ICM Type —Specify whether this is a Unified ICM or Unified CCE, or Unified ICMH system.

- Region —Specify
                                             				regional information where applicable.

Step 6

Select Add . This button invokes the Add
                                             				Device window.

Move the database log file to a separate virtual drive. By default, both the log file and database data file are installed
                                                         in \MSSQL\DATA on the virtual drive where you create the database. You can move the log file with SQL Server Management Studio.

By default,
                                                         				  the newly created data file is set to “Automatically Grow,” if it exceeds the
                                                         				  initially specified size. You can modify this setting, and the maximum
                                                         				  file size, with SQL Server Enterprise Manager. 
                                                         				Verify on the Files page in  SQL Server Enterprise Manager that the Autogrowth column shows:

Data files automatically grow in 100-MB increments.

Log files automatically grow in 10% increments.

Step 7

After you have
                                          			 completed entering information in the Create Database window, select Create to close the window and create the database.

### Delete a
                           	 Database

Use the Delete
                                 		  function to delete an Administration & Data Server or Logger database.

When an instance
                                             			 does not have any configured components, component placeholders appear under
                                             			 that instance on the application tree view. If you delete the database, the
                                             			 component placeholders no longer appear.

Step 1

With Unified
                                          			 CCE running, for the server, instance, and node (Administration & Data
                                          			 Server or Logger), select the database that you want to delete.

Step 2

Select Database > Delete from the menu bar.

Step 3

The Delete
                                             				Database prompt appears. Select Yes to delete the database.

Step 4

Verify that you want to delete the database in the message box.

Step 5

Select Close to exit. Check the main window to verify that
                                          			 the database was deleted.

### Expand a
                           	 Database

Use this function
                                 		  to add a new storage file.

ICMDBA allows a
                                             			 database to be expanded a maximum of 49 times (resulting in 50 segments). In
                                             			 the event that you reach this limit, you must either recreate the database or
                                             			 use SQL Enterprise Manager to modify the database.

Step 1

For the
                                          			 server, instance, and node (Administration & Data Server or Logger), select
                                          			 the database that you want to expand.

Step 2

Select Database > Expand from the menu bar (or click the
                                          			 right mouse button and select Expand ). The Expand window appears:

Step 3

Use the window
                                          			 to adjust the size allocation on the database storage device, by completing the
                                          			 following fields:

- Component —Specifies whether the file is a data file
                                             				or log file. Each database must have a file for each type of service.

- Available
                                                				  Drives —Specify the drive on which to create the database.

- Size —Specifies
                                             				the size (in MB) of the storage. The field displays a default size, adjust the
                                             				value as necessary.

Step 4

Select OK to expand the file and exit the screen.

### Recreate a
                           	 Database

Use the Recreate
                                 		  function to recreate a database. The procedure for recreating a database is
                                 		  similar to the procedure for creating a database.

Caution

When you
                                             			 recreate a database, the information currently stored in the database is
                                             			 deleted.

When an instance
                                             			 does not have any configured components, database creation occurs under a
                                             			 component placeholder on the application tree view.

Step 1

For the
                                          			 server, instance, and node (Administration & Data Server or Logger), select
                                          			 the database that you want to recreate.

Step 2

Select Database > Recreate from the menu bar. The Recreate window appears.

Step 3

Enter the
                                          			 database information. See the online help for a description of the fields.

Step 4

Select Create to continue. A message is displayed asking if
                                          			 you are sure you want to recreate the database. Select Yes to continue the operation.

Step 5

The next Recreate Database window appears. Select Start to recreate the database. After the process
                                          			 completes, a message appears indicating the action was successful. Select OK and then select Close to exit.

### View Database
                           	 Properties

The ICMDBA tool
                                 		  allows you to view the properties of specified databases.

Step 1

For the
                                          			 server, instance, and node (Administration & Data Server or Logger), select
                                          			 the database that you want to view.

Step 2

Select Database > Properties from the menu bar (or click
                                          			 the right mouse button and select Properties ). The Properties window appears.

- Instance name

- The database configuration

- The size and percentage
                                                				  used of the files

- Where the data and log
                                                				  files are stored

Step 3

After you
                                          			 finish viewing the database properties, select Close to exit the window.

### View Table
                           	 Properties

ICMDBA also allows
                                 		  you to view the properties of each table in the database.

Step 1

Select and
                                          			 expand the database to display the tables of a database.

Step 2

Double-click
                                          			 the table you want to view. The Table
                                             				Properties window appears.

Step 3

After you
                                          			 finish viewing the table properties, select Close to exit the window.

### Import and Export
                           	 Data

You can use
                                 		  Import/Export functions to move Unified ICM configuration data from one
                                 		  database to another.

The ICMDBA
                                             			 Import/Export feature handles Unified ICM configuration data only. To import or
                                             			 export Unified ICM historical data, use Microsoft’s SQL Server Database Backup
                                             			 and Database Restore utilities.

Step 1

For the
                                          			 server, instance, and node (Administration & Data Server or Logger), select
                                          			 the database from which you want to import or export data.

Step 2

Select Data > Import (or Export) from the menu bar.
                                          			 The Import
                                             				data to (or Export) window appears.

Step 3

Check Lockout Changes , if you want to prevent changes to
                                          			 the database during the import or export operation.

Step 4

Check Truncate Config Message Log , if you want to truncate
                                          			 the Config_Message_Log table in the Logger database.

Truncating
                                                         				  deletes the data and does not export the Config_Message_Log table.

Step 5

Set the Data type for the imported data.

Step 6

Indicate the
                                          			 path for the source/destination of the data.

Step 7

Select Import (or Export) to display the Import (or Export) dialog.

Step 8

Select Start to import (or export) the data. After the
                                          			 process completes, a message appears indicating that the action was successful.
                                          			 Select OK and then select Close to exit. You can select Cancel at any time to end the process.

### Synchronize
                           	 Database Data

Use the Synchronize function to synchronize the configuration data of two Logger databases. This function does not synchronize
                                 the historical data.

Step 1

For the server
                                          			 and instance, select the Logger database to synchronize.

Step 2

Select Data > Synchronize from the menu bar. The Synchronize window appears:

Step 3

Check Lockout Changes , if you want to prevent changes to
                                          			 the database during the synchronize operation.

Step 4

Check Truncate Config Message Log , if you want to truncate
                                          			 the Config_Message_Log table in the Logger database.

Step 5

Select the
                                          			 server name and database for both source and target from the drop down lists.
                                          			 To select a server that is not on the drop down list, select Add and enter the server name in the Add
                                             				Server box:

Step 6

Select Synchronize .

Step 7

A message box
                                          			 appears asking for confirmation. Select OK to continue.

Step 8

The next Synchronize window appears. Select Start to synchronize the data. After the process
                                          			 completes, a message appears indicating that the action was successful. Select OK and then select Close to exit. You can select Cancel at any time to end the process.

### Configure a
                           	 Database Server

ICMDBA allows you
                                 		  to start or stop a server and to do some limited server configuration.

To start or stop a
                                 		  server, select the node from the list and select Server > Start/Stop from the menu bar.

When you use the
                                             			 Configure option, the SQL Server, Administration & Data Server, and Logger
                                             			 restart automatically. However, when you use the Stop option from the Server
                                             			 menu, manually restart the Logger and Administration & Data Server
                                             			 from ICM Service Control.

Step 1

Select the
                                          			 server and select Server > Configure from the menu bar. The Configure window appears.

Step 2

Use this
                                          			 window to modify the following SQL Server parameters:

- User
                                                   					 Connections —Indicates the maximum number of users that can connect
                                                				  to SQL Server at one time.

- Locks —Indicates
                                                				  the maximum number of available locks.

User
                                                               						Connections, Locks, and Open Objects are “dynamically allocated” by SQL Server.
                                                               						Unified ICM does not allow you to change these options, so they are dimmed.

- Open
                                                   					 Databases —Indicates the maximum number of available open databases.

You can
                                                               						configure a specific amount of memory instead of the SQL Server default of
                                                               						“Dynamic.” Specifying a value of 0 sets the Memory setting to “Dynamic.”

- Recovery
                                                   					 Interval —This setting controls checkpoint frequency.

- Max Async
                                                   					 ID —Indicates the maximum number of outstanding asynchronous disk
                                                				  input/output (I/O) requests that the entire server can issue against a file.

Step 3

After you are
                                          			 finished configuring the server, select OK to complete the operation or select Cancel to end the operation without making any
                                          			 changes.

## Increase the size of the disk space for an existing virtual machine

### Before you begin

Plan for a maintenance window to increase the size of the disk space.

Step 1

Power off the VM.

Step 2

Clone the VM or take a snapshot of the powered off VM.

Step 3

Change the size of the disk space, as required. Ensure that the disk format is set to Thick Provision Lazy Zeroed.

Step 4

Power on the VM.

Step 5

On the Windows server, go to Server Manager > File and Storage Services > Volumes > Disks .

Step 6

Modify the disk size and verify the changes.

Step 7

Delete the clone or snapshot of the old VM.

## Database Sizing
                        	 Estimator Tool

The Database Sizing
                           		Estimator tool enables you to perform database sizing tasks.

The Database Sizing
                           		Estimator estimates the storage requirements for a Cisco Unified ICM/CCE logger
                           		or HDS database.  The tool bases the estimate ion information about the configuration of the environment
                           		(for example, the number of agents, skill groups, call types, and so on) and
                           		database retention days. You can supply initial values by loading values from
                           		your local Unified ICM database.

When values are
                           		updated in the Database Sizing Estimator, the application recalculates its
                           		totals. This update enables you to immediately see the affects of each change
                           		as it is made, with the values displayed in a spreadsheet. The tool enables you
                           		to engage in what-if scenarios to see the effects that various changes have on the database sizing requirements.

The Database Sizing
                           		Estimator allows you to save the values as an XML file on your local machine.
                           		At any time, you can load the saved XML file back into the Database Sizing
                           		Estimator, so you can continue revising your estimates.

### Cisco Unified
                              		  ICM/CCE Database Retriever Dialog

The Cisco Unified
                              		  ICM/CCE Database Retriever dialog, which you access from the Database Sizing
                              		  Estimator tool, queries the existing database and registry configuration. The
                              		  Database Sizing Estimator tool then uses this data to provide starting values,
                              		  which you can modify.

To access the Database
                                 			 Retriever dialog, select Load
                                 			 from DB in the Database Sizing Estimator tool on your local
                              		  machine.

Cisco Unified
                                          			 ICM/CCE Database Retriever can retrieve the configuration and retention
                                          			 information from any Unified ICM/CCE system containing a Logger or Historical
                                          			 Data Server (HDS) database. The Database Sizing Estimator can calculate a
                                          			 database size for a newer schema other than the deployment to which the
                                          			 Database Sizing Estimator is connected.

### Start Database
                           	 Sizing Estimator

The following
                                 		  steps describe how to start the Database Sizing Estimator.

For Database
                                             			 Sizing Estimator field-level descriptions, see the online help.

Step 1

Open the
                                          			 Database Sizing Estimator tool by selecting Database > Estimate in the ICMDBA tool.

Step 2

The Cisco
                                          			 Unified ICM/CCE Database Sizing Estimator window appears:

Step 3

The window
                                          			 displays initial default values for all fields. As you change the field values,
                                          			 the database size requirements update automatically. You can load values from a
                                          			 previous version or from the Cisco
                                             				Unified ICM/CCE Database Retriever dialog by selecting Load
                                             				from File to load an external XML data file.

### Estimate Database
                           	 Size

Steps 1–3 in
                                             			 this procedure only apply when using existing databases.

Step 1

Use your
                                          			 existing database as the starting point. Select Load
                                             				from DB in the Database Sizing Estimator main window. The Cisco
                                             				Unified ICM/CCE Database Retriever dialog appears.

Step 2

Select the
                                          			 database you want to use as the starting point for your sizing estimates.

Step 3

Select Retrieve .

Step 4

Modify the
                                          			 database information depending on your scenario. As changes are made, the Database Size Required value changes.

Step 5

Save your work
                                          			 in progress by selecting Save
                                             				to File .

## Administration and Data Server with Historical Data Server Setup

There are two ways to set up a Historical Data Server (HDS) VM:

- The instance is created in
                              		  the domain, but not already added.

- The instance is created in
                              		  the domain and is already added.

### Set Up HDS and Add
                           	 Instance

Step 1

Run the Cisco Unified ICM/Contact Center Enterprise  (if you have not run it already) on the local machine.

Step 2

Run the Web Setup tool for that machine (in a browser, from
                                          			 anywhere). Under Instance Management , select Add and add the instance.

Step 3

Run the ICMDBA tool on the local machine. Create the Historical
                                          			 Data Server/Detail Data Server database.

Step 4

Return to the Web Setup tool. Under Component Management , select Add on the Administration & Data Server
                                          			 list page, then follow the instructions in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .
                                          			 If you did not perform step 3, the Administration & Data Server Add wizard does not allow you to finish this
                                          			 procedure until you create an HDS database.

#### What to do next

Use the Database Sizing Estimator tool to determine the size of the database and then use the ICMDBA tool to create the database.

### Set Up HDS from
                           	 Added Instance

Step 1

Run the Cisco Unified ICM/Contact Center Enterprise Installer (if you have not run it already) on the local machine.

Step 2

In the Web Setup tool, under Component Management , select Add on the Administration & Data Server
                                          			 list page, then follow the instructions in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .
                                          			 If you did not perform step 1, the Administration & Data Server Add wizard does not allow you to finish this
                                          			 procedure until you create an HDS database.

#### What to do next

Use the Database Sizing Estimator tool to determine the size of the
                                 		  database and then use the ICMDBA tool to create the database.

## Database Size
                        	 Monitoring

Regularly
                           		monitor the space used by the central database and transaction logs. You can
                           		monitor database size by viewing the Logger’s per-process log files. The
                           		per-process log files contain information on Logger and database activity, as
                           		this example log file illustrates:

The Logger logs
                           		events and trace messages that show the percentage of space used in the
                           		database. These files are stored in a \logfiles subdirectory in the Logger’s folder (la
                           		or lb). You can view the Logger’s per-process log files by using the Unified
                           		ICM dumplog utility.

When the database
                           		becomes 80 percent full, the Logger logs an EMS warning message to the central
                           		database. The “80 percent full” warning message might also immediately be sent
                           		to your Unified ICM network management station through SNMP or SYSLOG.

See the Serviceability Best
                                          			 Practices Guide for Cisco Unified ICM/Contact Center Enterprise for more
                                       		  information on using the dumplog utility.

If you decide that
                           		you need more database space, contact your Unified ICM support provider.

## System Response
                        	 When Database Nears Capacity

The system software
                           		has automatic checks to prevent the central database from becoming full:

Warning message —When the central database begins to approach its capacity, the system software issues a warning message. By default, this
                                 warning occurs when the database is 80% full, but you can configure this value. Warning messages trigger an event that is
                                 registered in AlarmTracker, which the console window displays in an EMS trace message.

Purge Adjustment —Purge Adjustment automatically deletes the oldest historical data when the database usage exceeds 80% threshold or when the
                                 central or HDS database nears its capacity. However, purge adjustment does not happen immediately. It happens at the default scheduled purge time (00:30 AM), or at the
                                    time that you have specified for the scheduled purge to happen.

By default, purge adjustment occurs when the database is 80% full, but you can specify the percentage when you set up the
                                 Logger.

If the historical databases for the Logger, AW-HDS-DDS, AW-HDS, and HDS-DDS are not adequately sized, the purge adjustment
                                 feature is activated when the database usage exceeds the threshold. Use the Database Sizing Estimator tool to size your database requirements.

The purge adjustment feature affects performance of the Unified CCE system. The high CPU and disk usage due to purge adjustment
                                             could affect component performance including failures.

See the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide for more on purging information from databases.

Emergency/Automatic Purge —By default, the system automatically deletes the oldest historical data from all historical tables when the database exceeds
                                 90% usage capacity.

The automatic purge
                           		ensures that the database can never become full. But, the purge means that you
                           		can lose older historical data.

## Allocation of More
                        	 Database Space

If the central database is growing too large, you can allocate more space. If you require more
                           			space in the central database, back up the primary database before you add more space.
                           			Your Unified CCE support provider might have options for allocating more space.

## Initialize Local
                        	 Database (AWDB)

Usually, you do not need to initialize the local database (awdb), because initialization happens automatically during its
                              creation. If you ever need to initialize the local database after its creation, you can do so.

Step 1

Double-click Initialize Local Database within the Administration
                                       			 Tools folder. The Initialize Local Database main window appears.

Step 2

Select Start to transfer the data. As data is copied, the
                                       			 screen displays the number of rows processed for each table.

Step 3

After the
                                       			 transfer is complete, select Close to exit.

## General Database
                        	 Administration

Because Unified ICM is a mission-critical application that runs 24 hours
                           		a day, the system software takes care of many routine administration tasks
                           		automatically. In general, the system software retains control of most of the
                           		database administration functions in order to keep external interference to a
                           		minimum.

The Unified ICM administrator might perform several optional Unified ICM administration tasks:

- Setting networking options

- Monitoring Logger activity

- Backing up the central
                              		  database

- Restoring the central
                              		  database from a backup

- Comparing databases

- Resynchronizing databases

To conserve system resources, minimize all Unified ICM process windows
                                       		  before configuring your system.

### Built-In
                           	 Administration

The system software
                              		maintains a database on each side of the Central Controller and the local
                              		database (awdb). Each database consists of a group of interrelated tables. As
                              		you add or update data in the database, ensure that logical relationships are
                              		maintained. For example, if you delete a trunk group, do not leave trunks in
                              		the database that reference that trunk group. If you do, the integrity of the
                              		database is broken.

Configuration
                              		Manager prevents you from making certain changes that disrupt the integrity of
                              		the data in the database. However, it cannot prevent all such changes. Usually,
                              		if data integrity in the local database (awdb) is temporarily disrupted, no
                              		major problems occur. However, integrity problems in the central Unified CCE
                              		database could cause errors in system processing.

To protect the
                                          		  integrity of the Unified CCE databases, do not use third-party tools to modify
                                          		  them. These tools do not protect against disruptions of database integrity.
                                          		  (You can use third-party tools to view Unified ICM data.)

When your Unified
                              		CCE support provider installs the Unified CCE system, they perform integrity
                              		checks to make sure that the database is configured correctly. After that, the
                              		system software maintains the integrity of the central database. You do not
                              		need to manually check the integrity of the Unified CCE central database. If
                              		you ever have a problem with data integrity in the central database, the
                              		problem is most likely a software problem that your Unified CCE support
                              		provider needs to address.

Caution

Manual integrity
                                          		  checks of the central database must involve your Unified CCE support provider.
                                          		  Do not run the DBCC CHECKDB procedure on the central database with the Unified
                                          		  CCE system running. This procedure stops the Logger.

### Database Stock Jobs

#### AW-HDS Database Stock Jobs

The following table provides the list of AW-HDS Database Stock Jobs:

PurgeCMsgLog

Daily Purge for Configuration Message Log.

12:30 AM

PurgeRCD

Daily Purge for Route Call Detail.

12:30 AM

PurgeRCV

Daily Purge for Route Call Variable.

12:32 AM

PurgeDD

Daily Purge for Dialer Detail.

12:34 AM

PurgeAED

Daily Purge for Agent Event Detail.

12:36 AM

PurgeNED

Daily Purge for Network Event Detail.

12:38 AM

PurgeCTSGI

Daily Purge for Call Type Skill Group Interval.

12:40 AM

PurgeCTSGHH

Daily Purge for Call Type Skill Group Half Hour.

12:42 AM

PurgeASGI

Daily Purge for Agent Skill Group Interval.

12:44 AM

PurgeTCD

Daily Purge for Termination Call Detail. It also re-organizes indexes and updates statistics.

12:46 AM

PurgeTCV

Daily Purge for Termination Call Variable.

12:48 AM

#### Logger Database Stocks

The following table provides the list of Logger Database Stock Jobs:

PurgeDialingList

Daily Purge for DialingList Table.

12:30 AM

PurgePersonalCallbackListID

Daily Purge for PersonalCallbackListID Table.

12:30 AM

PurgeRCD

Daily Purge for Route Call Detail.

12:30 AM

PurgeRCV

Daily Purge for Route Call Variable.

12:32 AM

PurgeDD

Daily Purge for Dialer Detail.

12:34 AM

PurgeAED

Daily Purge for Agent Event Detail.

12:36 AM

PurgeNED

Daily Purge for Network Event Detail.

12:38 AM

PurgeCTSGI

Daily Purge for Call Type Skill Group Interval.

12:40 AM

PurgeCTSGHH

Daily Purge for Call Type Skill Group Half Hour.

12:42 AM

PurgeASGI

Daily Purge for Agent Skill Group Interval.

12:44 AM

PurgeTCD

Daily Purge for Termination Call Detail. It also re-organizes indexes and updates statistics.

12:46 AM

PurgeTCV

Daily Purge for Termination Call Variable.

12:48 AM

## Check AWDB Data
                        	 Integrity

You can manually check the integrity of data in the local database (AWDB). Configuration Manager provides a Check Integrity
                              option under the Administer menu. Configuration Manager allows you to select the checks that you need to run.

The specific data integrity check procedures are listed in the
                              		  following table:

Description

Null

Targets

Checks for appropriate relationships among peripherals,
                                          					 targets at peripherals (services, skill groups, agents, and translation
                                          					 routes), trunk groups, network targets, announcements, and peripheral targets.

Routes and Numbers

Checks if the ID fields cross-referenced from several tables correspond to the existing records.

Scripts

Checks for valid cross-references among scripts, call types,
                                          					 and dialed numbers.

Enterprise

Checks for valid cross-references among enterprise services
                                          					 and services, and between enterprise skill groups and skill groups. Also
                                          					 performs several other checks on skill groups, trunks, and so on.

Domain Adherence

Checks for valid relationships between agents and skill
                                          					 groups, between skill groups and services, between labels and routing clients,
                                          					 between dialed numbers and routes, and between peripherals and routing clients.

Names

Checks for invalid characters in enterprise names
                                          					 (EnterpriseName field) in various database tables. Enterprise names provide
                                          					 unique character-string names for objects in the Unified ICM configuration.

Miscellaneous

Checks rules for Outbound Option Configuration.

For more information on the specific fields checked by these
                              		  procedures, see the online help for the Configuration Manager tool.

Step 1

Invoke Configuration Manager
                                       			 by double-clicking its icon in the Administration Tools folder.

Step 2

Select Configure
                                             				  ICM > Administration > Integrity
                                             				  Check from the menu bar. The Integrity Check dialog box appears.

Step 3

Select specific checks to run, or select All to perform all the checks.

Step 4

Select Start to perform the checks. If any integrity
                                       			 problems are found, the Configuration Manager displays a message describing the
                                       			 problems.

Step 5

After you perform all the checks you want, select Done to dismiss the Integrity Check dialog box.

## Logger
                        	 Events

You can view recent
                           		Logger activity by viewing the Logger’s per-process log files. Per-process log
                           		files document events for the specific processes running on a computer. These
                           		files are useful in diagnosing problems with processes on the Logger (and on
                           		other nodes in the Unified ICM system).

You can also view
                           		Logger event data in the central database. The Event Management System (EMS)
                           		logs events to the central database. Be especially aware of Error and Warning
                           		events generated by the Logger. For example, the system software logs a Warning
                           		event when the central database becomes 80% full.

See the Serviceability Best
                              		  Practices Guide for Cisco Unified ICM/Contact Center Enterprise for more
                           		information on viewing the per-process log files and central database event
                           		data.

## Database
                        	 Networking Support

You can use the SQL
                           		Server Setup program to specify which network protocols the database manager
                           		supports.

The correct order
                           		and states are:

- Shared Memory —Enabled

- Named Pipes —Enabled

- TCP/IP —Enabled

- VIA —Disabled

See the Staging Guide for Cisco Unified Contact Center Enterprise http://www.cisco.com/en/US/products/sw/custcosw/ps1844/prod_installation_guides_list.html for detailed information about installing SQL Server. For more information about database networking, see the Microsoft documentation
                           for Microsoft SQL Server.

## Database Backup
                        	 and Restore

A database can be
                           		lost or corrupted for several reasons. Because you cannot protect against all
                           		these reasons, you must have a backup strategy in place. This backup strategy
                           		is especially important if you have a nonredundant central database
                           		configuration. However, even for a redundant system, you still need to perform
                           		backups to protect against software problems that corrupt both sides of the
                           		system.

The commonly used
                           		database backup strategies are:

- Regularly scheduled
                              		  database backups

- Mirrored disk
                              		  configurations

- Redundant Array of
                              		  Inexpensive Disks (RAID) configurations

Although the last
                           		two strategies might decrease system performance, they have the advantage of
                           		not requiring manual intervention. However, while these configurations protect
                           		against disk drive failure and bad media, they might not protect against some
                           		software errors.

In a single database
                           		configuration, ensure protection against all types of errors. To protect your
                           		data, regularly back up the central database with the SQL Administrator tool
                           		provided with SQL Server.

When you restore a
                           		database, you can only restore up to the last backup. Any transactions after
                           		that backup are lost. In single database configurations, daily backups are
                           		required to ensure maximum data protection.

You must back up
                                       		  the entire database at each backup interval. The system software does not
                                       		  support the use of transaction log dumps as incremental backups.

For general
                           		information about developing a backup strategy, including the use of mirrored
                           		disks, see Microsoft’s SQL
                              		  Server System Administrator’s Guide . For specific information about
                           		backing up a database using SQL Administrator, see Microsoft’s SQL
                              		  Administrator User’s Guide .

## Database Recovery Models 12 5

When you install an ICM and create Logger, HDS, BA, or AWDB, the ICMDBA tool automatically sets the database recovery model
                           to Simple. The Simple recovery model is required for Unified CCE data recovery mechanism.

For more information, see Microsoft documentation.

## Database
                        	 Comparison

For diagnostic purposes, you can check that two databases have
                           		the same data in a specific table. For example, you can check that
                           		the ICM_Locks table contains the same data on both sides of a Central
                           		Controller. The tool dbdiff.exe performs this type of check. Its syntax
                           		is as follows:

```
dbdiff database1.table@host1 database2.table@host2
```

For example:

```
dbdiff cust1_sideA.ICM_Locks@geoxyzlgra cust1_sideB.ICM_Locks@geoxyzlgrb
```

The batch script diffconfig.bat invokes dbdiff for various tables to automatically compare two
                           		Unified ICM databases. Its syntax is as follows:

```
diffconfig database1 host1 database2 host2
```

For example:

```
diffconfig cust1_sideA geoxyzlgra cust1_sideB geoxyzlgrb
```

## Database
                        	 Resynchronization

You might occasionally need to repair corrupt configuration data on the Logger database on one side of a redundant Unified
                           ICM by copying the configuration data on Logger database from the other side. You can synchronize the configuration data on
                           the databases using either the DOS Command window or the ICM Database Administration (ICMDBA) tool.

The ICMDBA synchronize process involves dropping the targeted side data and copying the data from the source. For example,
                           if you are synchronizing side B data to side A data, the side B data is replaced with the data stored in side A. For more
                           information, see Synchronize Database Data .

Perform these
                                       		  procedures in a maintenance window.

### Synchronize Configuration Data between Loggers from Command Window

Step 1

Stop the Logger for the target database, if that Logger is running.

Step 2

In a DOS
                                          			 Command window on the VM for that Logger, change to the \icm directory.

Step 3

Run the following command: install\syncloggers <Source_logger_server> <Source_logger_database> <Target_logger_server> <Target_logger_database> .

Step 4

When prompted, Type Y to continue, upon which
                                          					configuration of target database will be deleted and synced with source
                                          					database.

#### What to do next

When the command
                                 		  is complete, restart the Logger on the target server.

| Note | For more information on how to perform a manual configuration for integrating AWDB with ECE , see the section Integrating ECE with Unified CCE in the Enterprise Chat and Email Installation and Configuration Guide . |
|---|---|

| Historical
                                       					 tables | Default
                                       					 retention time |
|---|---|
| Logger_Admin, Import_Rule_History, Persistent | 30 days |
| Recovery | 3650 days |
| All other
                                       					 historical tables | 14 days |

| Caution | SQL Server Agent
                                       		  Jobs are installed and enabled during the Unified CCE install and upgrade
                                       		  procedure. Do not stop these jobs while the system software is active. If you
                                       		  plan to stop the Logger and Administration & Data Server-hds component
                                       		  services for maintenance for more than a day, manually disable the Microsoft
                                       		  SQL Server jobs using the SQL Server enterprise management tool. Later, after
                                       		  the services are started, re-enable the jobs. |
|---|---|

| Note | Before using the
                                       		  ICMDBA tool, install the Unified CCE software. See the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide , for information on the Unified
                                       		  CCE installation. |
|---|---|

| Note | The ICMDBA
                                       		  Import /Export feature works on Unified ICM configuration data only. To import
                                       		  or export Unified ICM historical data, use Microsoft’s SQL Server Database
                                       		  Backup and Database Restore utilities. |
|---|---|

| Note | If you cannot find
                                       		  the server you want in the main window, you can select any computer on your
                                       		  local network by choosing File > Add
                                             				Computer . |
|---|---|

| Step 1 | With the
                                          			 Unified CCE running, for the server and instance, select the node
                                          			 (Administration & Data Server or Logger) where you want to create the
                                          			 database. |
|---|---|
| Step 2 | Select Database > Create from the menu bar (or click the
                                          			 right mouse button and select Create ). The Create
                                             				Database window is displayed. |
| Step 3 | Enter the
                                          			 following information for the database: DB Type —Specify
                                             				the type of database: Outbound Option for an outbound dialer, Administration & Database Server for a local
                                             				database (awdb), or Historical Data Server/Detail Data Server (HDS/DDS) for Administration & Data Server machines. For a Logger device, the default database type is
                                             				displayed (Logger side must be selected). ICM Type —Specify whether this is a Unified ICM or Unified CCE, or Unified ICMH system. Region —Specify
                                             				regional information where applicable. |
| Step 4 | Select Add . This button invokes the Add
                                             				Device window. Use this
                                          			 window to create a new data file and a new log file for the selected database.
                                          			 Specify the disk drive letter and size in megabytes for each new file. Note Move the database log file to a separate virtual drive. By default, both the log file and database data file are installed
                                                         in \MSSQL\DATA on the virtual drive where you create the database. You can move the log file with SQL Server Management Studio. Note By default,
                                                         				  the newly created data file is set to “Automatically Grow,” if it exceeds the
                                                         				  initially specified size. You can modify this setting, and the maximum
                                                         				  file size, with SQL Server Enterprise Manager. 
                                                         				Verify on the Files page in  SQL Server Enterprise Manager that the Autogrowth column shows: Data files automatically grow in 100-MB increments. Log files automatically grow in 10% increments. | Note | Move the database log file to a separate virtual drive. By default, both the log file and database data file are installed
                                                         in \MSSQL\DATA on the virtual drive where you create the database. You can move the log file with SQL Server Management Studio. | Note | By default,
                                                         				  the newly created data file is set to “Automatically Grow,” if it exceeds the
                                                         				  initially specified size. You can modify this setting, and the maximum
                                                         				  file size, with SQL Server Enterprise Manager. 
                                                         				Verify on the Files page in  SQL Server Enterprise Manager that the Autogrowth column shows: Data files automatically grow in 100-MB increments. Log files automatically grow in 10% increments. |
| Note | Move the database log file to a separate virtual drive. By default, both the log file and database data file are installed
                                                         in \MSSQL\DATA on the virtual drive where you create the database. You can move the log file with SQL Server Management Studio. |
| Note | By default,
                                                         				  the newly created data file is set to “Automatically Grow,” if it exceeds the
                                                         				  initially specified size. You can modify this setting, and the maximum
                                                         				  file size, with SQL Server Enterprise Manager. 
                                                         				Verify on the Files page in  SQL Server Enterprise Manager that the Autogrowth column shows: Data files automatically grow in 100-MB increments. Log files automatically grow in 10% increments. |
| Step 5 | After you
                                          			 complete entering information in the Create Database window, select Create to close the window and create the
                                          			 database. |

| Note | Move the database log file to a separate virtual drive. By default, both the log file and database data file are installed
                                                         in \MSSQL\DATA on the virtual drive where you create the database. You can move the log file with SQL Server Management Studio. |
|---|---|

| Note | By default,
                                                         				  the newly created data file is set to “Automatically Grow,” if it exceeds the
                                                         				  initially specified size. You can modify this setting, and the maximum
                                                         				  file size, with SQL Server Enterprise Manager. 
                                                         				Verify on the Files page in  SQL Server Enterprise Manager that the Autogrowth column shows: Data files automatically grow in 100-MB increments. Log files automatically grow in 10% increments. |
|---|---|

| Note | When an instance
                                             			 does not have any configured components, database creation occurs under the
                                             			 instance within a component placeholder. |
|---|---|

| Step 1 | With Unified
                                          			 CCE running, for the server and instance, select the instance where you want to
                                          			 create the database. |
|---|---|
| Step 2 | Select Database > Create from the menu bar (or click the
                                          			 right mouse button and select Create ). The Select
                                             				Component dialog appears. |
| Step 3 | Select the Administration & Data Server , LoggerA , or LoggerB component and select OK . |
| Step 4 | If you select LoggerA or LoggerB, the Select Logger type dialog appears, allowing you to select Enterprise . Select the logger type and select OK . The Create Database window appears. |
| Step 5 | Enter the
                                          			 following information for the database: DB Type —Specify
                                             				the type of database: Outbound Option for an outbound dialer, Administration & Database Server for a local
                                             				database (awdb), or Historical Data Server/Detail Data Server (HDS/DDS) for Administration & Data Server machines. For a Logger device, the default database type is
                                             				displayed (Logger side must be selected). ICM Type —Specify whether this is a Unified ICM or Unified CCE, or Unified ICMH system. Region —Specify
                                             				regional information where applicable. |
| Step 6 | Select Add . This button invokes the Add
                                             				Device window. Use this
                                          			 window to create a new data file and a new log file for the selected database.
                                          			 Specify the disk drive letter and size in megabytes for each new file. Note Move the database log file to a separate virtual drive. By default, both the log file and database data file are installed
                                                         in \MSSQL\DATA on the virtual drive where you create the database. You can move the log file with SQL Server Management Studio. Note By default,
                                                         				  the newly created data file is set to “Automatically Grow,” if it exceeds the
                                                         				  initially specified size. You can modify this setting, and the maximum
                                                         				  file size, with SQL Server Enterprise Manager. 
                                                         				Verify on the Files page in  SQL Server Enterprise Manager that the Autogrowth column shows: Data files automatically grow in 100-MB increments. Log files automatically grow in 10% increments. | Note | Move the database log file to a separate virtual drive. By default, both the log file and database data file are installed
                                                         in \MSSQL\DATA on the virtual drive where you create the database. You can move the log file with SQL Server Management Studio. | Note | By default,
                                                         				  the newly created data file is set to “Automatically Grow,” if it exceeds the
                                                         				  initially specified size. You can modify this setting, and the maximum
                                                         				  file size, with SQL Server Enterprise Manager. 
                                                         				Verify on the Files page in  SQL Server Enterprise Manager that the Autogrowth column shows: Data files automatically grow in 100-MB increments. Log files automatically grow in 10% increments. |
| Note | Move the database log file to a separate virtual drive. By default, both the log file and database data file are installed
                                                         in \MSSQL\DATA on the virtual drive where you create the database. You can move the log file with SQL Server Management Studio. |
| Note | By default,
                                                         				  the newly created data file is set to “Automatically Grow,” if it exceeds the
                                                         				  initially specified size. You can modify this setting, and the maximum
                                                         				  file size, with SQL Server Enterprise Manager. 
                                                         				Verify on the Files page in  SQL Server Enterprise Manager that the Autogrowth column shows: Data files automatically grow in 100-MB increments. Log files automatically grow in 10% increments. |
| Step 7 | After you have
                                          			 completed entering information in the Create Database window, select Create to close the window and create the database. |

| Note | Move the database log file to a separate virtual drive. By default, both the log file and database data file are installed
                                                         in \MSSQL\DATA on the virtual drive where you create the database. You can move the log file with SQL Server Management Studio. |
|---|---|

| Note | By default,
                                                         				  the newly created data file is set to “Automatically Grow,” if it exceeds the
                                                         				  initially specified size. You can modify this setting, and the maximum
                                                         				  file size, with SQL Server Enterprise Manager. 
                                                         				Verify on the Files page in  SQL Server Enterprise Manager that the Autogrowth column shows: Data files automatically grow in 100-MB increments. Log files automatically grow in 10% increments. |
|---|---|

| Note | When an instance
                                             			 does not have any configured components, component placeholders appear under
                                             			 that instance on the application tree view. If you delete the database, the
                                             			 component placeholders no longer appear. |
|---|---|

| Step 1 | With Unified
                                          			 CCE running, for the server, instance, and node (Administration & Data
                                          			 Server or Logger), select the database that you want to delete. |
|---|---|
| Step 2 | Select Database > Delete from the menu bar. |
| Step 3 | The Delete
                                             				Database prompt appears. Select Yes to delete the database. |
| Step 4 | Verify that you want to delete the database in the message box. |
| Step 5 | Select Close to exit. Check the main window to verify that
                                          			 the database was deleted. |

| Note | ICMDBA allows a
                                             			 database to be expanded a maximum of 49 times (resulting in 50 segments). In
                                             			 the event that you reach this limit, you must either recreate the database or
                                             			 use SQL Enterprise Manager to modify the database. |
|---|---|

| Step 1 | For the
                                          			 server, instance, and node (Administration & Data Server or Logger), select
                                          			 the database that you want to expand. |
|---|---|
| Step 2 | Select Database > Expand from the menu bar (or click the
                                          			 right mouse button and select Expand ). The Expand window appears: |
| Step 3 | Use the window
                                          			 to adjust the size allocation on the database storage device, by completing the
                                          			 following fields: Component —Specifies whether the file is a data file
                                             				or log file. Each database must have a file for each type of service. Available
                                                				  Drives —Specify the drive on which to create the database. Size —Specifies
                                             				the size (in MB) of the storage. The field displays a default size, adjust the
                                             				value as necessary. |
| Step 4 | Select OK to expand the file and exit the screen. |

| Caution | When you
                                             			 recreate a database, the information currently stored in the database is
                                             			 deleted. |
|---|---|

| Note | When an instance
                                             			 does not have any configured components, database creation occurs under a
                                             			 component placeholder on the application tree view. |
|---|---|

| Step 1 | For the
                                          			 server, instance, and node (Administration & Data Server or Logger), select
                                          			 the database that you want to recreate. |
|---|---|
| Step 2 | Select Database > Recreate from the menu bar. The Recreate window appears. |
| Step 3 | Enter the
                                          			 database information. See the online help for a description of the fields. |
| Step 4 | Select Create to continue. A message is displayed asking if
                                          			 you are sure you want to recreate the database. Select Yes to continue the operation. |
| Step 5 | The next Recreate Database window appears. Select Start to recreate the database. After the process
                                          			 completes, a message appears indicating the action was successful. Select OK and then select Close to exit. |

| Step 1 | For the
                                          			 server, instance, and node (Administration & Data Server or Logger), select
                                          			 the database that you want to view. |
|---|---|
| Step 2 | Select Database > Properties from the menu bar (or click
                                          			 the right mouse button and select Properties ). The Properties window appears. The screen
                                          			 display includes the following information: Instance name The database configuration The size and percentage
                                                				  used of the files Where the data and log
                                                				  files are stored |
| Step 3 | After you
                                          			 finish viewing the database properties, select Close to exit the window. |

| Step 1 | Select and
                                          			 expand the database to display the tables of a database. |
|---|---|
| Step 2 | Double-click
                                          			 the table you want to view. The Table
                                             				Properties window appears. |
| Step 3 | After you
                                          			 finish viewing the table properties, select Close to exit the window. |

| Note | The ICMDBA
                                             			 Import/Export feature handles Unified ICM configuration data only. To import or
                                             			 export Unified ICM historical data, use Microsoft’s SQL Server Database Backup
                                             			 and Database Restore utilities. |
|---|---|

| Step 1 | For the
                                          			 server, instance, and node (Administration & Data Server or Logger), select
                                          			 the database from which you want to import or export data. |
|---|---|
| Step 2 | Select Data > Import (or Export) from the menu bar.
                                          			 The Import
                                             				data to (or Export) window appears. |
| Step 3 | Check Lockout Changes , if you want to prevent changes to
                                          			 the database during the import or export operation. |
| Step 4 | Check Truncate Config Message Log , if you want to truncate
                                          			 the Config_Message_Log table in the Logger database. Note Truncating
                                                         				  deletes the data and does not export the Config_Message_Log table. | Note | Truncating
                                                         				  deletes the data and does not export the Config_Message_Log table. |
| Note | Truncating
                                                         				  deletes the data and does not export the Config_Message_Log table. |
| Step 5 | Set the Data type for the imported data. |
| Step 6 | Indicate the
                                          			 path for the source/destination of the data. |
| Step 7 | Select Import (or Export) to display the Import (or Export) dialog. |
| Step 8 | Select Start to import (or export) the data. After the
                                          			 process completes, a message appears indicating that the action was successful.
                                          			 Select OK and then select Close to exit. You can select Cancel at any time to end the process. |

| Note | Truncating
                                                         				  deletes the data and does not export the Config_Message_Log table. |
|---|---|

| Step 1 | For the server
                                          			 and instance, select the Logger database to synchronize. |
|---|---|
| Step 2 | Select Data > Synchronize from the menu bar. The Synchronize window appears: |
| Step 3 | Check Lockout Changes , if you want to prevent changes to
                                          			 the database during the synchronize operation. |
| Step 4 | Check Truncate Config Message Log , if you want to truncate
                                          			 the Config_Message_Log table in the Logger database. |
| Step 5 | Select the
                                          			 server name and database for both source and target from the drop down lists.
                                          			 To select a server that is not on the drop down list, select Add and enter the server name in the Add
                                             				Server box: |
| Step 6 | Select Synchronize . |
| Step 7 | A message box
                                          			 appears asking for confirmation. Select OK to continue. |
| Step 8 | The next Synchronize window appears. Select Start to synchronize the data. After the process
                                          			 completes, a message appears indicating that the action was successful. Select OK and then select Close to exit. You can select Cancel at any time to end the process. |

| Note | When you use the
                                             			 Configure option, the SQL Server, Administration & Data Server, and Logger
                                             			 restart automatically. However, when you use the Stop option from the Server
                                             			 menu, manually restart the Logger and Administration & Data Server
                                             			 from ICM Service Control. |
|---|---|

| Step 1 | Select the
                                          			 server and select Server > Configure from the menu bar. The Configure window appears. |
|---|---|
| Step 2 | Use this
                                          			 window to modify the following SQL Server parameters: User
                                                   					 Connections —Indicates the maximum number of users that can connect
                                                				  to SQL Server at one time. Locks —Indicates
                                                				  the maximum number of available locks. Open
                                                   					 Objects —Indicates the maximum number of available open objects. Note User
                                                               						Connections, Locks, and Open Objects are “dynamically allocated” by SQL Server.
                                                               						Unified ICM does not allow you to change these options, so they are dimmed. Open
                                                   					 Databases —Indicates the maximum number of available open databases. Memory —Indicates the amount of memory (in megabytes)
                                                				  allocated to SQL Server processing. Note You can
                                                               						configure a specific amount of memory instead of the SQL Server default of
                                                               						“Dynamic.” Specifying a value of 0 sets the Memory setting to “Dynamic.” Recovery
                                                   					 Interval —This setting controls checkpoint frequency. Max Async
                                                   					 ID —Indicates the maximum number of outstanding asynchronous disk
                                                				  input/output (I/O) requests that the entire server can issue against a file. | Note | User
                                                               						Connections, Locks, and Open Objects are “dynamically allocated” by SQL Server.
                                                               						Unified ICM does not allow you to change these options, so they are dimmed. | Note | You can
                                                               						configure a specific amount of memory instead of the SQL Server default of
                                                               						“Dynamic.” Specifying a value of 0 sets the Memory setting to “Dynamic.” |
| Note | User
                                                               						Connections, Locks, and Open Objects are “dynamically allocated” by SQL Server.
                                                               						Unified ICM does not allow you to change these options, so they are dimmed. |
| Note | You can
                                                               						configure a specific amount of memory instead of the SQL Server default of
                                                               						“Dynamic.” Specifying a value of 0 sets the Memory setting to “Dynamic.” |
| Step 3 | After you are
                                          			 finished configuring the server, select OK to complete the operation or select Cancel to end the operation without making any
                                          			 changes. |

| Note | User
                                                               						Connections, Locks, and Open Objects are “dynamically allocated” by SQL Server.
                                                               						Unified ICM does not allow you to change these options, so they are dimmed. |
|---|---|

| Note | You can
                                                               						configure a specific amount of memory instead of the SQL Server default of
                                                               						“Dynamic.” Specifying a value of 0 sets the Memory setting to “Dynamic.” |
|---|---|

| Step 1 | Power off the VM. |
|---|---|
| Step 2 | Clone the VM or take a snapshot of the powered off VM. |
| Step 3 | Change the size of the disk space, as required. Ensure that the disk format is set to Thick Provision Lazy Zeroed. |
| Step 4 | Power on the VM. |
| Step 5 | On the Windows server, go to Server Manager > File and Storage Services > Volumes > Disks . |
| Step 6 | Modify the disk size and verify the changes. |
| Step 7 | Delete the clone or snapshot of the old VM. |

| Note | Cisco Unified
                                          			 ICM/CCE Database Retriever can retrieve the configuration and retention
                                          			 information from any Unified ICM/CCE system containing a Logger or Historical
                                          			 Data Server (HDS) database. The Database Sizing Estimator can calculate a
                                          			 database size for a newer schema other than the deployment to which the
                                          			 Database Sizing Estimator is connected. |
|---|---|

| Note | For Database
                                             			 Sizing Estimator field-level descriptions, see the online help. |
|---|---|

| Step 1 | Open the
                                          			 Database Sizing Estimator tool by selecting Database > Estimate in the ICMDBA tool. |
|---|---|
| Step 2 | The Cisco
                                          			 Unified ICM/CCE Database Sizing Estimator window appears: |
| Step 3 | The window
                                          			 displays initial default values for all fields. As you change the field values,
                                          			 the database size requirements update automatically. You can load values from a
                                          			 previous version or from the Cisco
                                             				Unified ICM/CCE Database Retriever dialog by selecting Load
                                             				from File to load an external XML data file. |

| Note | Steps 1–3 in
                                             			 this procedure only apply when using existing databases. |
|---|---|

| Step 1 | Use your
                                          			 existing database as the starting point. Select Load
                                             				from DB in the Database Sizing Estimator main window. The Cisco
                                             				Unified ICM/CCE Database Retriever dialog appears. |
|---|---|
| Step 2 | Select the
                                          			 database you want to use as the starting point for your sizing estimates. |
| Step 3 | Select Retrieve . The fields in the Database Sizing Estimator main window auto-populate
                                          			 with the information from the selected database. |
| Step 4 | Modify the
                                          			 database information depending on your scenario. As changes are made, the Database Size Required value changes. |
| Step 5 | Save your work
                                          			 in progress by selecting Save
                                             				to File . |

| Step 1 | Run the Cisco Unified ICM/Contact Center Enterprise  (if you have not run it already) on the local machine. |
|---|---|
| Step 2 | Run the Web Setup tool for that machine (in a browser, from
                                          			 anywhere). Under Instance Management , select Add and add the instance. |
| Step 3 | Run the ICMDBA tool on the local machine. Create the Historical
                                          			 Data Server/Detail Data Server database. |
| Step 4 | Return to the Web Setup tool. Under Component Management , select Add on the Administration & Data Server
                                          			 list page, then follow the instructions in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .
                                          			 If you did not perform step 3, the Administration & Data Server Add wizard does not allow you to finish this
                                          			 procedure until you create an HDS database. |

| Step 1 | Run the Cisco Unified ICM/Contact Center Enterprise Installer (if you have not run it already) on the local machine. |
|---|---|
| Step 2 | In the Web Setup tool, under Component Management , select Add on the Administration & Data Server
                                          			 list page, then follow the instructions in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide .
                                          			 If you did not perform step 1, the Administration & Data Server Add wizard does not allow you to finish this
                                          			 procedure until you create an HDS database. |

| Note | See the Serviceability Best
                                          			 Practices Guide for Cisco Unified ICM/Contact Center Enterprise for more
                                       		  information on using the dumplog utility. |
|---|---|

| Note | The purge adjustment feature affects performance of the Unified CCE system. The high CPU and disk usage due to purge adjustment
                                             could affect component performance including failures. |
|---|---|

| Step 1 | Double-click Initialize Local Database within the Administration
                                       			 Tools folder. The Initialize Local Database main window appears. |
|---|---|
| Step 2 | Select Start to transfer the data. As data is copied, the
                                       			 screen displays the number of rows processed for each table. |
| Step 3 | After the
                                       			 transfer is complete, select Close to exit. |

| Note | To conserve system resources, minimize all Unified ICM process windows
                                       		  before configuring your system. |
|---|---|

| Note | To protect the
                                          		  integrity of the Unified CCE databases, do not use third-party tools to modify
                                          		  them. These tools do not protect against disruptions of database integrity.
                                          		  (You can use third-party tools to view Unified ICM data.) |
|---|---|

| Caution | Manual integrity
                                          		  checks of the central database must involve your Unified CCE support provider.
                                          		  Do not run the DBCC CHECKDB procedure on the central database with the Unified
                                          		  CCE system running. This procedure stops the Logger. |
|---|---|

| Name | Description | Schedule |
|---|---|---|
| PurgeCMsgLog | Daily Purge for Configuration Message Log. | 12:30 AM |
| PurgeRCD | Daily Purge for Route Call Detail. | 12:30 AM |
| PurgeRCV | Daily Purge for Route Call Variable. | 12:32 AM |
| PurgeDD | Daily Purge for Dialer Detail. | 12:34 AM |
| PurgeAED | Daily Purge for Agent Event Detail. | 12:36 AM |
| PurgeNED | Daily Purge for Network Event Detail. | 12:38 AM |
| PurgeCTSGI | Daily Purge for Call Type Skill Group Interval. | 12:40 AM |
| PurgeCTSGHH | Daily Purge for Call Type Skill Group Half Hour. | 12:42 AM |
| PurgeASGI | Daily Purge for Agent Skill Group Interval. | 12:44 AM |
| PurgeTCD | Daily Purge for Termination Call Detail. It also re-organizes indexes and updates statistics. | 12:46 AM |
| PurgeTCV | Daily Purge for Termination Call Variable. | 12:48 AM |

| Name | Description | Schedule |
|---|---|---|
| PurgeDialingList | Daily Purge for DialingList Table. | 12:30 AM |
| PurgePersonalCallbackListID | Daily Purge for PersonalCallbackListID Table. | 12:30 AM |
| PurgeRCD | Daily Purge for Route Call Detail. | 12:30 AM |
| PurgeRCV | Daily Purge for Route Call Variable. | 12:32 AM |
| PurgeDD | Daily Purge for Dialer Detail. | 12:34 AM |
| PurgeAED | Daily Purge for Agent Event Detail. | 12:36 AM |
| PurgeNED | Daily Purge for Network Event Detail. | 12:38 AM |
| PurgeCTSGI | Daily Purge for Call Type Skill Group Interval. | 12:40 AM |
| PurgeCTSGHH | Daily Purge for Call Type Skill Group Half Hour. | 12:42 AM |
| PurgeASGI | Daily Purge for Agent Skill Group Interval. | 12:44 AM |
| PurgeTCD | Daily Purge for Termination Call Detail. It also re-organizes indexes and updates statistics. | 12:46 AM |
| PurgeTCV | Daily Purge for Termination Call Variable. | 12:48 AM |

| Procedure | Description |
|---|---|
| Null | Checks the database for the value NULL in fields that must not have the value NULL. Checks if the value of the RoutingClient.PeripheralID
                                       is NULL for the routing clients associated with the NIC. |
| Targets | Checks for appropriate relationships among peripherals,
                                          					 targets at peripherals (services, skill groups, agents, and translation
                                          					 routes), trunk groups, network targets, announcements, and peripheral targets. |
| Routes and Numbers | Checks if the ID fields cross-referenced from several tables correspond to the existing records. |
| Scripts | Checks for valid cross-references among scripts, call types,
                                          					 and dialed numbers. |
| Enterprise | Checks for valid cross-references among enterprise services
                                          					 and services, and between enterprise skill groups and skill groups. Also
                                          					 performs several other checks on skill groups, trunks, and so on. |
| Domain Adherence | Checks for valid relationships between agents and skill
                                          					 groups, between skill groups and services, between labels and routing clients,
                                          					 between dialed numbers and routes, and between peripherals and routing clients. |
| Names | Checks for invalid characters in enterprise names
                                          					 (EnterpriseName field) in various database tables. Enterprise names provide
                                          					 unique character-string names for objects in the Unified ICM configuration. |
| Miscellaneous | Checks rules for Outbound Option Configuration. |

| Step 1 | Invoke Configuration Manager
                                       			 by double-clicking its icon in the Administration Tools folder. |
|---|---|
| Step 2 | Select Configure
                                             				  ICM > Administration > Integrity
                                             				  Check from the menu bar. The Integrity Check dialog box appears. |
| Step 3 | Select specific checks to run, or select All to perform all the checks. |
| Step 4 | Select Start to perform the checks. If any integrity
                                       			 problems are found, the Configuration Manager displays a message describing the
                                       			 problems. |
| Step 5 | After you perform all the checks you want, select Done to dismiss the Integrity Check dialog box. |

| Note | You must back up
                                       		  the entire database at each backup interval. The system software does not
                                       		  support the use of transaction log dumps as incremental backups. |
|---|---|

| Note | Perform these
                                       		  procedures in a maintenance window. |
|---|---|

| Step 1 | Stop the Logger for the target database, if that Logger is running. |
|---|---|
| Step 2 | In a DOS
                                          			 Command window on the VM for that Logger, change to the \icm directory. |
| Step 3 | Run the following command: install\syncloggers <Source_logger_server> <Source_logger_database> <Target_logger_server> <Target_logger_database> . |
| Step 4 | When prompted, Type Y to continue, upon which
                                          					configuration of target database will be deleted and synced with source
                                          					database. |