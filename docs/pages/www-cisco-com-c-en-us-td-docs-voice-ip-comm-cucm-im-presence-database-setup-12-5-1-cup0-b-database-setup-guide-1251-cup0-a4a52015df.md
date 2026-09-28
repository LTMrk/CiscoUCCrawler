---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-database-setup-12-5-1-cup0-b-database-setup-guide-1251-cup0-a4a52015df
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/database_setup/12_5_1/cup0_b_database-setup-guide-1251/cup0_mp_o4fde461_00_oracle-installation-and-setup.html
retrieved_at: 2026-08-16T16:49:48.207823+00:00
---

Database Setup Guide for the IM and Presence Service, Release 12.5(1)

# Database Setup Guide for the IM and Presence Service, Release 12.5(1)

Updated: January 8, 2025

Chapter: Install Oracle

## Chapter: Install Oracle

- Install Oracle

- Install Oracle                              	 Database

- Create New Database Instance

# Install Oracle

This chapter provides information about installing and setting up
                        		an Oracle database.

## Install Oracle
                        	 Database

### Before you begin

Cisco recommends that an Oracle DBA install the Oracle server.

You need to update the patch for the known Oracle defect: ORA-22275. If this is not done persistent chat rooms will not work
                                    properly.

Read the security recommendations for the Oracle database in your Oracle documentation.

For information on supported versions, see External Database Setup Requirements .

For Oracle version 11 and earlier, you must configure your Oracle database to use UTF8 character encoding.

As of Oracle version 12, you must configure the Oracle database to use AL32UTF8 character encoding, as UTF8 may lead to unexpected
                                    behavior. For example, if you use UTF8 with Oracle 12, chat rooms may be deleted when you restart the Cisco XCP Text Conference
                                    Manager service.

To install the Oracle database, refer to your Oracle documentation.

To create tablespace and a database user, connect to the Oracle database as sysdba:

Step 1

Create
                                       			 tablespace.

Enter
                                             				  the following command:

Replace tablespace_name with the tablespace name.

Replace absolute_path_to_oracle_installation with the absolute path to where Oracle is installed. The entire path, including datafile. dbf, is enclosed in single quotation marks.

Replace database_name with the name of your database folder.

The datafile. dbf must be created in a folder under \oradata\ , in this case the database_name folder.

Replace datafile .dbf with the datafile name you want to create.

Step 2

Create a
                                       			 database user.

CREATE USER user_name IDENTIFIED BY " new_user's_password " DEFAULT
                                                					 TABLESPACE tablespace_name TEMPORARY TABLESPACE "TEMP" QUOTA UNLIMITED ON tablespace_name ACCOUNT
                                                					 UNLOCK;

Replace user_name with the new user's user name.

Replace
                                                					 " new_user's_password " with the new user's password.

Important

Replace tablespace_name with the tablespace name.

Step 3

Grant
                                       			 permissions to the database user.

The following example grants the required permissions and privileges to a database user, which are needed to create or upgrade
                                          the schema:

- GRANT CREATE SESSION TO user_name ;

- GRANT CREATE TABLE TO user_name ;

- GRANT CREATE PROCEDURE TO user_name ;

- GRANT CREATE TRIGGER TO user_name ;

After you have created or upgraded the schema, the following privileges can be revoked if greater access control is required:

- REVOKE CREATE TABLE FROM user_name ;

- REVOKE CREATE PROCEDURE FROM user_name ;

- REVOKE CREATE TRIGGER FROM user_name ;

## Create New Database Instance

Step 1

Enter the command dbca

Step 2

Click Next .

Step 3

Click the Create a Database radio button and then click Next .

Step 4

Click the General Purpose or Transaction Processing radio button and then click Next .

Step 5

Enter a unique Global Database Name on this screen and also a unique Oracle System Identifier (SID) for the database and click Next .

Step 6

Under the Enterprise Manager tab the required settings are enabled by default but you can configure optional backups and
                                       alert notifications. Click Next .

Step 7

The window has two options to set up password authentication for database users, choose one and click Next .

Step 8

The Storage Type drop-down list should be the same as your Oracle Installation. Click  the Use Oracle-Managed Files radio button and  click Next .

Step 9

Leave the default values and click Next .

Step 10

[Optional] Check the check box if you want  to enable Sample Schemas and click Next .

Step 11

Under the Memory tab the default value is for a database instance with 4GB of memory. This can be set higher or lower as needed.

Step 12

Under the Character Sets tab click the Use Unicode radio button and click Next .

Step 13

Leave the default settings as they are and click Next .

Step 14

Check the Create Database check box and click Finish .

Step 15

Once  a new database instance is created, you must temporarily change the ORACLE_SID environment variable (from Step 5) on
                                       your Unix system by running the command:

| Step 1 | Create
                                       			 tablespace. Note The DATAFILE keyword of the CREATE
                                                         					 TABLESPACE command tells Oracle where to put the tablespace's
                                                   				datafile. Enter
                                             				  the following command: CREATE TABLESPACE tablespace_name DATAFILE ' absolute_path_to_oracle_installation \oradata\ database_name \ datafile . dbf' SIZE 100M AUTOEXTEND
                                                   						ON NEXT 1M MAXSIZE UNLIMITED LOGGING EXTENT MANAGEMENT LOCAL SEGMENT SPACE
                                                   						MANAGEMENT AUTO; Replace tablespace_name with the tablespace name. Replace absolute_path_to_oracle_installation with the absolute path to where Oracle is installed. The entire path, including datafile. dbf, is enclosed in single quotation marks. Replace database_name with the name of your database folder. The datafile. dbf must be created in a folder under \oradata\ , in this case the database_name folder. Replace datafile .dbf with the datafile name you want to create. | Note | The DATAFILE keyword of the CREATE
                                                         					 TABLESPACE command tells Oracle where to put the tablespace's
                                                   				datafile. |
|---|---|---|---|
| Note | The DATAFILE keyword of the CREATE
                                                         					 TABLESPACE command tells Oracle where to put the tablespace's
                                                   				datafile. |
| Step 2 | Create a
                                       			 database user. CREATE USER user_name IDENTIFIED BY " new_user's_password " DEFAULT
                                                					 TABLESPACE tablespace_name TEMPORARY TABLESPACE "TEMP" QUOTA UNLIMITED ON tablespace_name ACCOUNT
                                                					 UNLOCK; Replace user_name with the new user's user name. Note The
                                                         					 command CREATE USER user_name without double quotes will default to
                                                         					 upper case and with quotes it will maintain the case Replace
                                                					 " new_user's_password " with the new user's password. Important Enclosing the new_user's_password within double quotation marks makes the
                                                         					 variable case-sensitive. By default SQL identifiers are not case-sensitive. Replace tablespace_name with the tablespace name. | Note | The
                                                         					 command CREATE USER user_name without double quotes will default to
                                                         					 upper case and with quotes it will maintain the case | Important | Enclosing the new_user's_password within double quotation marks makes the
                                                         					 variable case-sensitive. By default SQL identifiers are not case-sensitive. |
| Note | The
                                                         					 command CREATE USER user_name without double quotes will default to
                                                         					 upper case and with quotes it will maintain the case |
| Important | Enclosing the new_user's_password within double quotation marks makes the
                                                         					 variable case-sensitive. By default SQL identifiers are not case-sensitive. |
| Step 3 | Grant
                                       			 permissions to the database user. The following example grants the required permissions and privileges to a database user, which are needed to create or upgrade
                                          the schema: Note Prior to an upgrade, you must ensure that these permissions and privileges are granted, so that all IM and Presence Service
                                                   services continue to operate as normal following the upgrade. GRANT CREATE SESSION TO user_name ; GRANT CREATE TABLE TO user_name ; GRANT CREATE PROCEDURE TO user_name ; GRANT CREATE TRIGGER TO user_name ; After you have created or upgraded the schema, the following privileges can be revoked if greater access control is required: Note Ensure that revoked privileges are granted again before upgrading. REVOKE CREATE TABLE FROM user_name ; REVOKE CREATE PROCEDURE FROM user_name ; REVOKE CREATE TRIGGER FROM user_name ; Note IM and Presence Service only requires the CREATE SESSION privilege for regular operation. | Note | Prior to an upgrade, you must ensure that these permissions and privileges are granted, so that all IM and Presence Service
                                                   services continue to operate as normal following the upgrade. | Note | Ensure that revoked privileges are granted again before upgrading. | Note | IM and Presence Service only requires the CREATE SESSION privilege for regular operation. |
| Note | Prior to an upgrade, you must ensure that these permissions and privileges are granted, so that all IM and Presence Service
                                                   services continue to operate as normal following the upgrade. |
| Note | Ensure that revoked privileges are granted again before upgrading. |
| Note | IM and Presence Service only requires the CREATE SESSION privilege for regular operation. |

| Note | The DATAFILE keyword of the CREATE
                                                         					 TABLESPACE command tells Oracle where to put the tablespace's
                                                   				datafile. |
|---|---|

| Note | The
                                                         					 command CREATE USER user_name without double quotes will default to
                                                         					 upper case and with quotes it will maintain the case |
|---|---|

| Important | Enclosing the new_user's_password within double quotation marks makes the
                                                         					 variable case-sensitive. By default SQL identifiers are not case-sensitive. |
|---|---|

| Note | Prior to an upgrade, you must ensure that these permissions and privileges are granted, so that all IM and Presence Service
                                                   services continue to operate as normal following the upgrade. |
|---|---|

| Note | Ensure that revoked privileges are granted again before upgrading. |
|---|---|

| Note | IM and Presence Service only requires the CREATE SESSION privilege for regular operation. |
|---|---|

| Step 1 | Enter the command dbca The Database Configuration Assistant wizard opens. |
|---|---|
| Step 2 | Click Next . The Operations window appears. |
| Step 3 | Click the Create a Database radio button and then click Next . The Database Templates window appears. |
| Step 4 | Click the General Purpose or Transaction Processing radio button and then click Next . The Database Identification window appears. |
| Step 5 | Enter a unique Global Database Name on this screen and also a unique Oracle System Identifier (SID) for the database and click Next . Note Take note of the SID because it is needed in Step 15. The Management Options window appears. | Note | Take note of the SID because it is needed in Step 15. |
| Note | Take note of the SID because it is needed in Step 15. |
| Step 6 | Under the Enterprise Manager tab the required settings are enabled by default but you can configure optional backups and
                                       alert notifications. Click Next . The Database Credentials window appears. |
| Step 7 | The window has two options to set up password authentication for database users, choose one and click Next . The Database File Locations window appears. |
| Step 8 | The Storage Type drop-down list should be the same as your Oracle Installation. Click  the Use Oracle-Managed Files radio button and  click Next . Note This creates the new database instance in the same folder  as your other database instances. The Recovery Configuration window appears. | Note | This creates the new database instance in the same folder  as your other database instances. |
| Note | This creates the new database instance in the same folder  as your other database instances. |
| Step 9 | Leave the default values and click Next . The Database Content window appears. |
| Step 10 | [Optional] Check the check box if you want  to enable Sample Schemas and click Next . The Initialization Parameters window appears. |
| Step 11 | Under the Memory tab the default value is for a database instance with 4GB of memory. This can be set higher or lower as needed. Note The amount of memory used should not be configured too high as this starves other database instances of memory. | Note | The amount of memory used should not be configured too high as this starves other database instances of memory. |
| Note | The amount of memory used should not be configured too high as this starves other database instances of memory. |
| Step 12 | Under the Character Sets tab click the Use Unicode radio button and click Next . The Database Storage window appears. |
| Step 13 | Leave the default settings as they are and click Next . The Create Options window appears. |
| Step 14 | Check the Create Database check box and click Finish . |
| Step 15 | Once  a new database instance is created, you must temporarily change the ORACLE_SID environment variable (from Step 5) on
                                       your Unix system by running the command: export ORACLE_SID= new_oracle_db_instance_sid . This will change the SID so when you login using sqlplus, it will use the new instance and not the old one; you can then
                                       repeat the steps in Install Oracle Database . |

| Note | Take note of the SID because it is needed in Step 15. |
|---|---|

| Note | This creates the new database instance in the same folder  as your other database instances. |
|---|---|

| Note | The amount of memory used should not be configured too high as this starves other database instances of memory. |
|---|---|