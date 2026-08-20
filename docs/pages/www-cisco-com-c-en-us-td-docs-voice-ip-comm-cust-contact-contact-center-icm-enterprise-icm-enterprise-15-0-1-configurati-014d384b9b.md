---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-configurati-014d384b9b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/configuration/guide/ucce_b_security-guide-for-cisco-unified-icm-contact-center-enterprise-release-15-0/sql_server_hardening.html
retrieved_at: 2026-08-20T18:56:12.740539+00:00
---

Security Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

# Security Guide for Cisco Unified Contact Center Enterprise, Release 15.0(1)

Updated: April 30, 2025

Chapter: SQL Server Hardening

## Chapter: SQL Server Hardening

# SQL Server Hardening

## SQL Server Hardening Considerations

### Top SQL Hardening
                           	 Considerations

Top SQL Hardening considerations:

Do not install SQL Server on an Active Directory Domain Controller.

Install the latest updates for SQL
                                       						Server from Microsoft.

Set a strong password for the sa account before installing ICM.

Always install SQL Server service to run using a least privilege account. Never install SQL Server to run using the built-in
                                       Local System account. Instead, use the Virtual account.

See the Staging Guide for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html for more information.

Enable SQL Server Agent Service and set to Automatic for database maintenance in Unified ICM.

Installing the latest updates for SQL Server from Microsoft might require you to disable
                                                   							the SQL Server Agent service. So before performing the cumulative update
                                                   							installation, reset this service to disabled . When the
                                                   							installation is complete, stop the service and set it back to enabled .

Disable the SQL guest account.

Restrict sysadmin membership to your Unified ICM administrators.

Block TCP port 1433 (default) and UDP port 1434 at the network firewall, unless the Administration & Data Server is not in
                                       the same security zone as the Logger.

Change the recovery actions of the Microsoft SQL Server service to restart after a failure.

Remove all sample databases.

Enable auditing for failed sign-ins.

The following table lists the settings and the corresponding default and supported values for SQL hardening.

Setting Name

Default Value

Supported Value

Scan for Startup Procedures

Disabled |0|

0 or 1 supported. Unified CCE does not require it to be enabled; however, enabling it would not create any problem.

Ad Hoc Distributed Queries

Disabled |0|

0 or 1 supported. 0 is more secure.

### SQL Server Users and Authentication

When creating a user for the SQL server account, create Windows accounts with the least possible privileges for running SQL
                                 server services. Create the accounts during the installation of SQL server.

The local user or the domain user account that is created for the SQL server service account follows the Windows or domain
                                 password policy respectively. Apply a strict password policy on this account. However, don’t set the password to expire. If
                                 the password expires, the SQL server service ceases to function and the Administration, & Data server fails.

Site requirements
                                 		  can govern the password and account settings. Consider minimum settings like
                                 		  the following:

Setting

Value

Enforce
                                             					 Password History

24
                                             					 passwords remembered

Minimum
                                             					 Password Length

12
                                             					 characters

Password
                                             					 Complexity

Enabled

Minimum
                                             					 Password Age

1 day

Account
                                             					 Lockout Duration

15 minutes

Account
                                             					 Lockout Threshold

3 invalid
                                             					 logon attempts

Reset
                                             					 Account Lockout Counter After

15 minutes

During automated SQL server hardening, if the sa password is found blank, a strong password is generated at random to secure
                                 the sa account. You can reset the sa account password after installation by logging on to the SQL server using a Windows Local
                                 Administrator account.

UCCE supports renaming or removal of default built-in MS SQL sa account. If the sa account is used to integrate with UCCE
                                 solution components like Finesse, CUIC or any other third-party integrations, the login credentials have to be reconfigured
                                 with the renamed sa account.

Renaming or removing the sa account has no correlation with SQL Server hardening that happens during installation or upgrade.

## SQL Server Security Considerations

Microsoft SQL server provides granular access control and runs with lower privileges by default. In addition to the security
                              provided by SQL server, CCE provides utility to harden the SQL server further. Details are available in the following sections.

### Automated SQL Server Hardening

The SQL Server Security Automated Hardening utility performs the following:

Enforces Mixed Mode Authentication.

Ensures that the Named Pipe (np) is listed before TCP/IP (tcp) in the SQL Server Client Network Protocol Order.

Disables SQLWriter and SQLBrowser Services.

Forces SQL server user 'sa' password if found blank.

### SQL Server
                           	 Security Hardening Utility

The SQL Server
                                 		  Security Hardening utility allows you to harden or roll back the SQL
                                 		  Server
                                 		  security on Logger and Administration & Data Server/HDS components.
                                 		  The Harden option disables unwanted services and features. If the latest
                                 		  version of the security settings is already applied, then the Harden option
                                 		  does not change anything. The Rollback option allows you to return to the state
                                 		  of SQL services and features that existed before your applying the last
                                 		  hardening.

You can optionally apply the SQL Server
                                 		  Security Hardening as part of Unified CCE installation and
                                 		  upgrade or via the Security Wizard tool. The utility is internally managed by
                                 		  running the Windows PowerShell script ICMSQLSecurity.ps1. You can also apply the hardening by directly running the PowerShell
                                 script.

Run the Security Wizard tool or Windows PowerShell script as an administrator.

#### Utility
                                 		  Location

The utility is
                                 		  located at:

%SYSTEMDRIVE%\CiscoUtils\SQLSecurity

#### HARDEN
                                 		  Command

At the Windows
                                 		  PowerShell command line, enter:

Powershell
                                    			 .\ICMSQLSecurity.ps1 HARDEN

The current SQL
                                             			 Server configuration is backed up to <ICMInstallDrive>:\CiscoUtils\SQLSecurity\icmsqlsecuritybkp.xml before the utility applies the SQL Server hardening.

#### ROLLBACK
                                 		  Command

The ROLLBACK
                                 		  command rolls back to the previous SQL Server configuration, if
                                 		  hardening was applied before.

To roll back to
                                 		  the previous SQL Server configuration, enter the following command:

Powershell
                                    			 .\ICMSQLSecurity.ps1 ROLLBACK

The following
                                             			 settings are required for Unified CCE to function properly. They are not
                                             			 reverted to their original state when automated rollback is performed:

Named Pipe
                                                   				  (np) listed before TCP/IP(tcp) in the SQL Server Client Network Protocol Order.

Mixed mode
                                                   				  authentication.

#### Help for
                                 		  Commands

If you use no
                                 		  argument with the command line, the help appears.

#### Output
                                 		  Log

All output logs
                                 		  are saved in the file:

%SYSTEMDRIVE%\CiscoUtils\SQLSecurity\Logs\ICMSQLSecurity.log

### Manual SQL Server Hardening

Enable both Named Pipes and TCP/IP endpoints during SQL Server setup. Make sure that the Named Pipes endpoint has a higher order of priority than TCP/IP.

Protocol order for Named Pipes and TCP/IP applies only to SQL Server 2019 and not for SQL Server 2022.

The SQL Server Security Hardening utility checks for the availability and order of these endpoints.

Disable access
                                    			 to all unrequired endpoints. For instance, deny connect permission to VIA
                                    			 endpoint for all users/groups who have access to the database.

### Virtual
                           	 Accounts

Virtual Accounts
                              		are preferred over Network or Local Services account for SQL Services because
                              		of the former's higher level of security. Virtual accounts run with the lowest
                              		privileges. The CCE installer adds the Perform Volume Maintenance Tasks
                              		privilege to the SQL account. This privilege is needed to perform
                              		database-related operations, such as creating and expanding the database.

If your corporate
                              		policy does not allow the use of this privilege, you can remove it. However,
                              		performing database-related operations such as creating and expanding the
                              		database takes more time (depending on the size of your database).

## Custom SQL Server Port

Contact Center Enterprise (CCE) now supports configuring a custom SQL Server port for CCE databases, allowing administrators
                           to replace the default port 1433 with a user-defined port to comply with the CIS Microsoft SQL Server Benchmark. This enhancement
                           improves security by protecting the database from attacks targeting the default port.

For more information about the configuration of custom SQL Server port, see the Custom SQL Server Port chapter in Administration Guide for Cisco Unified Contact Center Enterprise .

You must identify which ports are already used in CCE services and select a custom SQL Server port accordingly. For more information
                           about the list of specific ports assigned to various CCE service, see the Port Utilization in Contact Center Enterprise chapter in Port Utilization Guide for Cisco Unified Contact Center Solution Guide .

CCE supports connecting to an external SQL Server configured with a custom SQL Server port for database lookup. For more information,
                           see the following guides:

Database Lookup Authentication section in Contact Categorization chapter in Scripting and Media Routing Guide for Cisco Unified ICM/Contact Center Enterprise .

CCEDataProtect Tool chapter in Administration Guide for Cisco Unified Contact Center Enterprise .

| Note | Installing the latest updates for SQL Server from Microsoft might require you to disable
                                                   							the SQL Server Agent service. So before performing the cumulative update
                                                   							installation, reset this service to disabled . When the
                                                   							installation is complete, stop the service and set it back to enabled . |
|---|---|

| Setting Name | Default Value | Supported Value |
|---|---|---|
| Scan for Startup Procedures | Disabled \|0\| | 0 or 1 supported. Unified CCE does not require it to be enabled; however, enabling it would not create any problem. |
| Ad Hoc Distributed Queries | Disabled \|0\| | 0 or 1 supported. 0 is more secure. |

| Setting | Value |
|---|---|
| Enforce
                                             					 Password History | 24
                                             					 passwords remembered |
| Minimum
                                             					 Password Length | 12
                                             					 characters |
| Password
                                             					 Complexity | Enabled |
| Minimum
                                             					 Password Age | 1 day |
| Account
                                             					 Lockout Duration | 15 minutes |
| Account
                                             					 Lockout Threshold | 3 invalid
                                             					 logon attempts |
| Reset
                                             					 Account Lockout Counter After | 15 minutes |

| Note | Renaming or removing the sa account has no correlation with SQL Server hardening that happens during installation or upgrade. |
|---|---|

| Note | Run the Security Wizard tool or Windows PowerShell script as an administrator. |
|---|---|

| Note | The current SQL
                                             			 Server configuration is backed up to <ICMInstallDrive>:\CiscoUtils\SQLSecurity\icmsqlsecuritybkp.xml before the utility applies the SQL Server hardening. |
|---|---|

| Note | The following
                                             			 settings are required for Unified CCE to function properly. They are not
                                             			 reverted to their original state when automated rollback is performed: Named Pipe
                                                   				  (np) listed before TCP/IP(tcp) in the SQL Server Client Network Protocol Order. Mixed mode
                                                   				  authentication. |
|---|---|

| Note | Protocol order for Named Pipes and TCP/IP applies only to SQL Server 2019 and not for SQL Server 2022. |
|---|---|

| Note | The SQL Server Security Hardening utility checks for the availability and order of these endpoints. |
|---|---|