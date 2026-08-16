---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-database-setup-15-cup0-b-database-setup-guide-15-cup0-b-dat-245f408137
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/database_setup/15/cup0_b_database-setup-guide-15/cup0_b_database-setup-guide-1401_chapter_011.html
retrieved_at: 2026-08-16T16:12:57.866518+00:00
---

Database Setup Guide for the IM and Presence Service, Release 15 and SUs

# Database Setup Guide for the IM and Presence Service, Release 15 and SUs

Updated: July 13, 2026

Chapter: Install Microsoft SQL Server

## Chapter: Install Microsoft SQL Server

# Install Microsoft SQL Server

This chapter provides information about installing and setting up
                        Microsoft SQL.

## Encrypted Database Not Supported

The IM and Presence Service supports an encrypted database with Microsoft SQL Server, except in the following cases:

Release 12.0(x)

The IM and Presence Service supports an encrypted compliance database only for the Message Archiver feature.

## Install and Setup
                        	 Microsoft SQL Server

### Before you begin

Read the security recommendations for the Microsoft SQL database in the About Security Recommendations section.

For information on supported versions, see External Database Setup Requirements .

To install the MS SQL Server, refer to your Microsoft documentation.

Connect to the MS SQL Server using Microsoft SQL Server Management Studio .

### Create a New
                           	 Microsoft SQL Server Database

Step 1

Enable SQL server and Windows authentication:

In the left navigation pane, right-click the name of the
                                                				  Microsoft SQL Server, then click properties .

Click Enable SQL Server and Windows Authentication
                                                   					 mode .

Step 2

In the left
                                          			 navigation pane, right-click Databases and click New
                                             				Database .

Step 3

Enter an
                                          			 appropriate name in the Database name field.

Step 4

Click OK . The new name appears in the left navigation pane
                                          			 nested under databases.

### Configure MSSQL Named Instance

Microsoft SQL Server Browser service is responsible for listening on UDP port 1433 for incoming connections to a named instance.
                                 The SQL Server Browser service responds to the client with a dynamically assigned TCP port number, which is used for that
                                 session connection to the named instance.

IM and Presence does not support dynamic port allocation, so you need to configure the Microsoft SQL Server instance to use
                                 a static TCP port.

Use this procedure to statically assign a listening port for a named instance:

Step 1

Log in to the Microsoft server where SQL Server is installed.

Step 2

Select Start > Microsoft SQL Server > SQL Server Configuration.

Step 3

In the SQL Server Configuration Manager, select SQL Server Network Configuration > Protocols for <named_Instance_name> , and then select the TCP\IP protocol name.

Step 4

In the TCP\IP properties for the named instance, select the IP Address tab. The configuration will have several IP configuration sections, such as IP1, IP2, IP3, IP4, IP5, IP6 and IPALL.

Step 5

Perform the following steps for each of the above referenced IP configuration sections:

Remove any configuration in the <TCP Dynamic Ports> field.

Choose a TCP port you want to use for the named instance and update the TCP Port field with the chosen port.

Add a firewall rule for the SQL named instance.

When configuring the external database in IM and Presence, make sure to update the SQL TCP port to the value that is defined
                                                         in the previous steps.

### Create a new Login
                           	 and Database User

Use this procedure
                                 		  to create a new login and Microsoft SQL database user.

Step 1

In the left
                                          			 navigation pane, right-click Security > Login and click New
                                             				Login .

Step 2

Enter an
                                          			 appropriate name in the Login
                                             				name field.

Step 3

Check the SQL
                                             				Server authentication check box.

Step 4

Enter a new
                                          			 password in the Password field and confirm the password in the Confirm password field.

Step 5

Check the Enforce password policy check box.

Ensure that
                                                         				  the Enforce password expiration policy is not checked.
                                                         				  This password is used by IM and Presence Service to connect to the database and
                                                         				  must not expire.

Step 6

Choose the
                                          			 database you want to apply this new user to from the Default database drop-down list.

Step 7

In the left
                                          			 navigation pane of the Login
                                             				- New window, click User
                                             				Mapping .

Step 8

Under the Users
                                             				mapped to this login list, check the database to which you want to
                                          			 add this user.

Step 9

Click User
                                             				Mapping , in the Map column of the Users
                                             				mapped to this pane pane, check the check box of the database you
                                          			 have already created.

Step 10

In Server
                                             				Roles , ensure that only the public role check box is checked.

Step 11

Click OK . In Security > Logins , the new user is created.

### Grant Database
                           	 User Owner Privileges

Use this procedure
                                 		  to grant ownership of a Microsoft SQL database to a database user.

Step 1

In the left
                                          			 navigation pane click Databases , then click on the name of the database
                                          			 that you have created and click Security > Users .

Step 2

Right-click on
                                          			 the name of the database user to who you want to add owner privileges, then
                                          			 click Properties .

Step 3

In the
                                          			 Database User pane, click Membership .

Step 4

In the Role
                                             				Members list, check the db_owner check box.

Step 5

Click OK .

### [Optional]
                           	 Database User Access Restrictions

Use this
                                 		  procedure if you want to remove the database user as the database owner and
                                 		  apply further optional restrictions to the database user on the Microsoft SQL
                                 		  Server database.

Caution

If during an
                                             			 IM and Presence Service upgrade, there is a database schema upgrade, then the
                                             			 database user must have owner privileges for the database.

#### Before you begin

Ensure that you
                                 		  carry out the procedures in the Configure IM and Presence Service for External Database chapter.

Step 1

Create a new
                                          			 database role for executing stored procedures:

In the
                                                				  left navigation pane click Databases , then click the name of the database to
                                                				  which you want to add new database roles.

Right-click Roles , and click New Database Role .

In the Database Role window, click General .

Enter an
                                                				  appropriate name in the Role name field.

Click Securables , then click Search to open the Add Objects window.

Choose
                                                				  the Specific Objects radio button, and click OK .

Click Object Types to open the Select Object Types window.

In the Select Object Types window, check the Stored procedures check box and click OK . Stored procedures is then added to the Select these object types pane.

Click Browse .

In the Browse for Objects window, check the following check
                                                				  boxes:

[dbo][jabber_store_presence]

[dbo][ud_register]

[dbo][ps_get_affiliation]

[dbo][tc_add_message_clear_old]

[dbo][wlc_waitlist_update]

Click OK . The new names appear in the Enter the object names to select pane.

On the Select Objects window, click OK .

From the Database Role window, click the first entry in the
                                                				  list of objects in the Securables list.

In the Explicit list, check the Grant check box for the Execute permission.

Repeat
                                                				  step 13 and 14 for all objects in the Securables list.

Click OK .

A new
                                                   					 database role is created in Security > Roles > Database
                                                         						  Roles .

Step 2

To update
                                          			 the database user's database role membership:

Under Security > Users , right-click on the database
                                                				  user you have created, then click Properties .

In the Database User window, click Membership in the left navigation pane.

In the Role Members pane , uncheck the db_owner check box.

Check
                                                				  the check boxes for db_datareader , db_datawriter , and the database role which you
                                                				  created in step 1.

Step 3

Click OK .

### Default Listener Port  Setup for Microsoft SQL Server

Assign a TCP/IP port number to the SQL Server Database Engine as the default listener port.

Step 1

From the SQL Server Configuration Manager, click SQL Server Network Configuration > Protocols > TCP/IP in the Console .

Step 2

In the TCP/IP Properties dialog box, on the IP Addresses tab, right-click on the IP address that you want to configure and then click Properties .

Step 3

Check the TCP Dynamic Ports dialog box, if it contains the value 0, delete the 0. This prevents the Database Engine from listening on dynamic ports.

Step 4

In the IPn Properties pane, type the port number you want this IP address to listen on in the TCP Port pane.

Step 5

Click OK .

Step 6

Click SQL Server Services in the Console pane.

Step 7

In the Details pane, right-click SQL Server (instance name) and then click Restart , to stop and restart the Microsoft SQL Server.

## Database Migration Required for Upgrades with Microsoft SQL Server

If you have Microsoft SQL Server deployed as an external database with the IM and Presence Service and you are upgrading from 11.5(1), 11.5(1)SU1, or 11.5(1)SU2, you must create a new SQL Server database and migrate
                              to the new database. This is required due to enhanced data type support in this release. If you don't migrate your database,
                              schema verification failure will occur on the existing SQL Server database and services that rely on the external database,
                              such as persistent chat, will not start.

After you upgrade your IM and Presence Service, use this procedure to create a new SQL Server database and migrate data to the new database.

This migration is not required for Oracle or PostgreSQL external databases.

### Before You Begin

The database migration is dependent on the MSSQL_migrate_script.sql script. Contact Cisco TAC to obtain a copy.

Step

Task

Step 1

Create a snapshot of your external Microsoft SQL Server database.

Step 2

Create a new (empty) SQL Server database. For details, see the following chapters in the Database Setup Guide for the IM and Presence Service :

"Microsoft SQL Installation and Setup"—See this chapter for details on how to create your new SQL server database on your
                                                upgraded IM and Presence Service.

"IM and Presence Service External Database Setup"—After your new database is created, refer to this chapter to add the database
                                                as an external database in the IM and Presence Service.

Step 3

Run the System Troubleshooter to confirm that there are no errors with the new database.

From Cisco Unified CM IM and Presence Administration, choose Diagnostics > System Troubleshooter .

Verify that no errors appear in the External Database Troubleshooter section.

Step 4

Restart the Cisco XCP Router on all IM and Presence Service cluster nodes:

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services .

From the Server menu, select an IM and Presence Service node and click Go .

Under IM and Presence Services , select Cisco XCP Router , and click Restart .

Step 5

Turn off services that depend on the external database:

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services .

From the Server menu, select an IM and Presence node and click Go .

Under IM and Presence Services , select the following services:.

Cisco XCP Text Conference Manager

Cisco XCP File Transfer Manager

Cisco XCP Message Archiver

Click Stop .

Step 6

Run the following script to migrate data from the old database to the new database MSSQL_migrate_script.sql .

Contact Cisco TAC to obtain  a copy of this script

Step 7

Run the System Troubleshooter to confirm that there are no errors with the new database.

From Cisco Unified CM IM and Presence Administration, choose Diagnostics > System Troubleshooter .

Verify that no errors appear in the External Database Troubleshooter section.

Step 8

Start the services that you stopped previously.

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services .

From the Server menu, select an IM and Presence node and click Go .

Under IM and Presence Services , select the following services:

Cisco XCP Text Conference Manager

Cisco XCP File Transfer Manager

Cisco XCP Message Archiver

Click Start .

Step 9

Confirm that the external database is running and that all chat rooms are visible from a Cisco Jabber client.  Delete the
                                          old database only after you're confident that the new database is working.

## Upgrade Database Schema from IM and Presence Release 11.5(1) and Above

If you have Microsoft SQL database deployed as an external database with the IM and Presence Service, choose either of the
                              following scenarios to upgrade the database schema.

Scenario

Upgrade from IM and Presence Service 11.5(1), 11.5(1)SU1, or 11.5(1)SU2 release

For more information on how to upgrade your MSSQL database, see the 'Database Migration Required for Upgrades with Microsoft
                                       SQL Server' section in the Database Setup Guide for the IM and Presence Service .

This makes the necessary changes to the column types from TEXT to nvarchar(MAX).

Upgrade from IM and Presence Service 11.5(1)SU3 or later

The MSSQL database connected to the IM and Presence Service Server is upgraded automatically during IM and Presence Service
                                       upgrade. This makes the necessary changes to the column types from nvarchar(4000) to nvarchar(MAX).

If you want to trigger an upgrade manually for any reason, such as to connect to an older database with column type as nvarchar(4000),
                                                   the following actions trigger and upgrade the database by changing the column type to nvarchar(MAX):

Restarting Cisco XCP Config Manager followed by restarting Cisco XCP Router service; or

During schema verification of the external database—when you assign the database to Text Conferencing (TC), Message Archiver
                                                         (MA) or Managed File transfer (MFT) services, and reload the External Database Settings page. (From the Cisco Unified CM IM and Presence Administration user interface, choose Messaging > External Server Setup > External Databases , and then find and select the database to load the External Database Settings page.)

| Note | In compliance with XMPP specifications, the IM and Presence Service node uses UTF8 character encoding. This allows the node
                                       to operate using many languages simultaneously and to display special language characters correctly in the client interface.
                                       If you want to use Microsoft SQL with the node, you must configure it to support UTF8. |
|---|---|

| Step 1 | Enable SQL server and Windows authentication: In the left navigation pane, right-click the name of the
                                                				  Microsoft SQL Server, then click properties . Click Enable SQL Server and Windows Authentication
                                                   					 mode . |
|---|---|
| Step 2 | In the left
                                          			 navigation pane, right-click Databases and click New
                                             				Database . |
| Step 3 | Enter an
                                          			 appropriate name in the Database name field. |
| Step 4 | Click OK . The new name appears in the left navigation pane
                                          			 nested under databases. |

| Step 1 | Log in to the Microsoft server where SQL Server is installed. |
|---|---|
| Step 2 | Select Start > Microsoft SQL Server > SQL Server Configuration. |
| Step 3 | In the SQL Server Configuration Manager, select SQL Server Network Configuration > Protocols for <named_Instance_name> , and then select the TCP\IP protocol name. |
| Step 4 | In the TCP\IP properties for the named instance, select the IP Address tab. The configuration will have several IP configuration sections, such as IP1, IP2, IP3, IP4, IP5, IP6 and IPALL. |
| Step 5 | Perform the following steps for each of the above referenced IP configuration sections: Remove any configuration in the <TCP Dynamic Ports> field. Choose a TCP port you want to use for the named instance and update the TCP Port field with the chosen port. Add a firewall rule for the SQL named instance. Note When configuring the external database in IM and Presence, make sure to update the SQL TCP port to the value that is defined
                                                         in the previous steps. | Note | When configuring the external database in IM and Presence, make sure to update the SQL TCP port to the value that is defined
                                                         in the previous steps. |
| Note | When configuring the external database in IM and Presence, make sure to update the SQL TCP port to the value that is defined
                                                         in the previous steps. |

| Note | When configuring the external database in IM and Presence, make sure to update the SQL TCP port to the value that is defined
                                                         in the previous steps. |
|---|---|

| Step 1 | In the left
                                          			 navigation pane, right-click Security > Login and click New
                                             				Login . |
|---|---|
| Step 2 | Enter an
                                          			 appropriate name in the Login
                                             				name field. |
| Step 3 | Check the SQL
                                             				Server authentication check box. |
| Step 4 | Enter a new
                                          			 password in the Password field and confirm the password in the Confirm password field. |
| Step 5 | Check the Enforce password policy check box. Note Ensure that
                                                         				  the Enforce password expiration policy is not checked.
                                                         				  This password is used by IM and Presence Service to connect to the database and
                                                         				  must not expire. | Note | Ensure that
                                                         				  the Enforce password expiration policy is not checked.
                                                         				  This password is used by IM and Presence Service to connect to the database and
                                                         				  must not expire. |
| Note | Ensure that
                                                         				  the Enforce password expiration policy is not checked.
                                                         				  This password is used by IM and Presence Service to connect to the database and
                                                         				  must not expire. |
| Step 6 | Choose the
                                          			 database you want to apply this new user to from the Default database drop-down list. |
| Step 7 | In the left
                                          			 navigation pane of the Login
                                             				- New window, click User
                                             				Mapping . |
| Step 8 | Under the Users
                                             				mapped to this login list, check the database to which you want to
                                          			 add this user. |
| Step 9 | Click User
                                             				Mapping , in the Map column of the Users
                                             				mapped to this pane pane, check the check box of the database you
                                          			 have already created. |
| Step 10 | In Server
                                             				Roles , ensure that only the public role check box is checked. |
| Step 11 | Click OK . In Security > Logins , the new user is created. |

| Note | Ensure that
                                                         				  the Enforce password expiration policy is not checked.
                                                         				  This password is used by IM and Presence Service to connect to the database and
                                                         				  must not expire. |
|---|---|

| Step 1 | In the left
                                          			 navigation pane click Databases , then click on the name of the database
                                          			 that you have created and click Security > Users . |
|---|---|
| Step 2 | Right-click on
                                          			 the name of the database user to who you want to add owner privileges, then
                                          			 click Properties . |
| Step 3 | In the
                                          			 Database User pane, click Membership . |
| Step 4 | In the Role
                                             				Members list, check the db_owner check box. |
| Step 5 | Click OK . |

| Caution | If during an
                                             			 IM and Presence Service upgrade, there is a database schema upgrade, then the
                                             			 database user must have owner privileges for the database. |
|---|---|

| Step 1 | Create a new
                                          			 database role for executing stored procedures: In the
                                                				  left navigation pane click Databases , then click the name of the database to
                                                				  which you want to add new database roles. Right-click Roles , and click New Database Role . In the Database Role window, click General . Enter an
                                                				  appropriate name in the Role name field. Click Securables , then click Search to open the Add Objects window. Choose
                                                				  the Specific Objects radio button, and click OK . Click Object Types to open the Select Object Types window. In the Select Object Types window, check the Stored procedures check box and click OK . Stored procedures is then added to the Select these object types pane. Click Browse . In the Browse for Objects window, check the following check
                                                				  boxes: [dbo][jabber_store_presence] [dbo][ud_register] [dbo][ps_get_affiliation] [dbo][tc_add_message_clear_old] [dbo][wlc_waitlist_update] Click OK . The new names appear in the Enter the object names to select pane. On the Select Objects window, click OK . From the Database Role window, click the first entry in the
                                                				  list of objects in the Securables list. In the Explicit list, check the Grant check box for the Execute permission. Repeat
                                                				  step 13 and 14 for all objects in the Securables list. Click OK . A new
                                                   					 database role is created in Security > Roles > Database
                                                         						  Roles . |
|---|---|
| Step 2 | To update
                                          			 the database user's database role membership: Under Security > Users , right-click on the database
                                                				  user you have created, then click Properties . In the Database User window, click Membership in the left navigation pane. In the Role Members pane , uncheck the db_owner check box. Check
                                                				  the check boxes for db_datareader , db_datawriter , and the database role which you
                                                				  created in step 1. |
| Step 3 | Click OK . |

| Step 1 | From the SQL Server Configuration Manager, click SQL Server Network Configuration > Protocols > TCP/IP in the Console . |
|---|---|
| Step 2 | In the TCP/IP Properties dialog box, on the IP Addresses tab, right-click on the IP address that you want to configure and then click Properties . |
| Step 3 | Check the TCP Dynamic Ports dialog box, if it contains the value 0, delete the 0. This prevents the Database Engine from listening on dynamic ports. |
| Step 4 | In the IPn Properties pane, type the port number you want this IP address to listen on in the TCP Port pane. |
| Step 5 | Click OK . |
| Step 6 | Click SQL Server Services in the Console pane. |
| Step 7 | In the Details pane, right-click SQL Server (instance name) and then click Restart , to stop and restart the Microsoft SQL Server. |

| Note | This migration is not required for Oracle or PostgreSQL external databases. |
|---|---|

| Step | Task |
|---|---|
| Step 1 | Create a snapshot of your external Microsoft SQL Server database. |
| Step 2 | Create a new (empty) SQL Server database. For details, see the following chapters in the Database Setup Guide for the IM and Presence Service : "Microsoft SQL Installation and Setup"—See this chapter for details on how to create your new SQL server database on your
                                                upgraded IM and Presence Service. "IM and Presence Service External Database Setup"—After your new database is created, refer to this chapter to add the database
                                                as an external database in the IM and Presence Service. |
| Step 3 | Run the System Troubleshooter to confirm that there are no errors with the new database. From Cisco Unified CM IM and Presence Administration, choose Diagnostics > System Troubleshooter . Verify that no errors appear in the External Database Troubleshooter section. |
| Step 4 | Restart the Cisco XCP Router on all IM and Presence Service cluster nodes: From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Network Services . From the Server menu, select an IM and Presence Service node and click Go . Under IM and Presence Services , select Cisco XCP Router , and click Restart . |
| Step 5 | Turn off services that depend on the external database: From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services . From the Server menu, select an IM and Presence node and click Go . Under IM and Presence Services , select the following services:. Cisco XCP Text Conference Manager Cisco XCP File Transfer Manager Cisco XCP Message Archiver Click Stop . |
| Step 6 | Run the following script to migrate data from the old database to the new database MSSQL_migrate_script.sql . Note Contact Cisco TAC to obtain  a copy of this script | Note | Contact Cisco TAC to obtain  a copy of this script |
| Note | Contact Cisco TAC to obtain  a copy of this script |
| Step 7 | Run the System Troubleshooter to confirm that there are no errors with the new database. From Cisco Unified CM IM and Presence Administration, choose Diagnostics > System Troubleshooter . Verify that no errors appear in the External Database Troubleshooter section. |
| Step 8 | Start the services that you stopped previously. From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services . From the Server menu, select an IM and Presence node and click Go . Under IM and Presence Services , select the following services: Cisco XCP Text Conference Manager Cisco XCP File Transfer Manager Cisco XCP Message Archiver Click Start . |
| Step 9 | Confirm that the external database is running and that all chat rooms are visible from a Cisco Jabber client.  Delete the
                                          old database only after you're confident that the new database is working. |

| Note | Contact Cisco TAC to obtain  a copy of this script |
|---|---|

| Scenario | Procedure |
|---|---|
| Upgrade from IM and Presence Service 11.5(1), 11.5(1)SU1, or 11.5(1)SU2 release | For more information on how to upgrade your MSSQL database, see the 'Database Migration Required for Upgrades with Microsoft
                                       SQL Server' section in the Database Setup Guide for the IM and Presence Service . This makes the necessary changes to the column types from TEXT to nvarchar(MAX). |
| Upgrade from IM and Presence Service 11.5(1)SU3 or later | The MSSQL database connected to the IM and Presence Service Server is upgraded automatically during IM and Presence Service
                                       upgrade. This makes the necessary changes to the column types from nvarchar(4000) to nvarchar(MAX). Note If you want to trigger an upgrade manually for any reason, such as to connect to an older database with column type as nvarchar(4000),
                                                   the following actions trigger and upgrade the database by changing the column type to nvarchar(MAX): Restarting Cisco XCP Config Manager followed by restarting Cisco XCP Router service; or During schema verification of the external database—when you assign the database to Text Conferencing (TC), Message Archiver
                                                         (MA) or Managed File transfer (MFT) services, and reload the External Database Settings page. (From the Cisco Unified CM IM and Presence Administration user interface, choose Messaging > External Server Setup > External Databases , and then find and select the database to load the External Database Settings page.) | Note | If you want to trigger an upgrade manually for any reason, such as to connect to an older database with column type as nvarchar(4000),
                                                   the following actions trigger and upgrade the database by changing the column type to nvarchar(MAX): Restarting Cisco XCP Config Manager followed by restarting Cisco XCP Router service; or During schema verification of the external database—when you assign the database to Text Conferencing (TC), Message Archiver
                                                         (MA) or Managed File transfer (MFT) services, and reload the External Database Settings page. (From the Cisco Unified CM IM and Presence Administration user interface, choose Messaging > External Server Setup > External Databases , and then find and select the database to load the External Database Settings page.) |
| Note | If you want to trigger an upgrade manually for any reason, such as to connect to an older database with column type as nvarchar(4000),
                                                   the following actions trigger and upgrade the database by changing the column type to nvarchar(MAX): Restarting Cisco XCP Config Manager followed by restarting Cisco XCP Router service; or During schema verification of the external database—when you assign the database to Text Conferencing (TC), Message Archiver
                                                         (MA) or Managed File transfer (MFT) services, and reload the External Database Settings page. (From the Cisco Unified CM IM and Presence Administration user interface, choose Messaging > External Server Setup > External Databases , and then find and select the database to load the External Database Settings page.) |

| Note | If you want to trigger an upgrade manually for any reason, such as to connect to an older database with column type as nvarchar(4000),
                                                   the following actions trigger and upgrade the database by changing the column type to nvarchar(MAX): Restarting Cisco XCP Config Manager followed by restarting Cisco XCP Router service; or During schema verification of the external database—when you assign the database to Text Conferencing (TC), Message Archiver
                                                         (MA) or Managed File transfer (MFT) services, and reload the External Database Settings page. (From the Cisco Unified CM IM and Presence Administration user interface, choose Messaging > External Server Setup > External Databases , and then find and select the database to load the External Database Settings page.) |
|---|---|