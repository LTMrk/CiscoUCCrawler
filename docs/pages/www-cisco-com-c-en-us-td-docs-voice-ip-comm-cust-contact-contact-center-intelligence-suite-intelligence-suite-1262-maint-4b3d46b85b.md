---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1262-maint-4b3d46b85b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1262/maintain_and_operate/guide/cuic_b_1262-admin-console-user-guide/cuic_m_1262-user-interface.html
retrieved_at: 2026-08-21T04:39:58.827529+00:00
---

Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(2)

# Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(2)

Updated: April 28, 2023

Chapter: User Interface

## Chapter: User Interface

# User Interface

## Administration
                        	 Console

Unified Intelligence Center is installed on a Cisco Unified Operating
                           		System platform as a cluster with a maximum of eight nodes: one Controller node
                           		and up to seven Member nodes.

The Controller node is mandatory and provides both the Administration
                           		and the Unified Intelligence Center Reporting web applications. A cluster can
                           		consist of the Controller node only.

Member nodes are optional and have the Unified Intelligence Center
                           		Reporting application only. (Unified Intelligence Center Administration is not
                           		available on a Member node.)

The Administration console manages all components in a unified
                           		deployment and also provides links to:

Cisco Unified Serviceability and SNMP

Disaster Recovery System

Real Time Monitoring Tool (RTMT)

## Access
                        	 Administration Console

This initial Super User can then create other Super Users in the Admin Users page. For more information, see Manage All Super Users .

Step 1

Direct your browser to the URL https://<HOST ADDRESS>/oamp where HOST ADDRESS is the IP Address or Hostname of your server.

Step 2

Sign in using
                                       			 your Super User (system application user) ID and password. A successful sign-in
                                       			 launches the OAMP application.

### What to do next

The session timeout for inactivity is thirty minutes. It is
                              				not configurable.

See also: Users in the Administration Console .

## Home Page

The Home page appears by default after a successful sign-in.

To

Do this

Display the values for a function

Click a menu in the left navigation pane.

Open the Unified Intelligence Center reporting interface on a member node

Open a new browser window and enter this URL: https://<HOST ADDRESS>:8444/ where HOST ADDRESS is the IP Address or Hostname of your server.

Verify your signed on identity

This shows as protected text after Signed on as .

Displays Administrator on the top-right corner of your screen.

Sign Out

Click Administrator > Sign Out on the top-right corner of your screen.

Return to this Home page

Click Home in the left navigation pane.

## Users in the Administration Console

There are three user accounts that have access to the Administration console:

Super Users

System Application User

System Administration User

### Super Users

This user role is defined in the Administration console. It is the only user role for Administration.

The initial and default Super User is the System Application User who is configured during installation.

The initial Super User (the System Application User) can sign in to the Unified Intelligence Center Reporting console and
                              has all User Roles and full permissions for all drawers in Unified Intelligence Center Reporting. Those credentials cannot be removed from the initial Super User.

Additional Super Users who are added in the Administration Console can also sign in to Unified Intelligence Center Reporting
                              and are considered to be IMS users. They have limited Login User role only, until the Unified Intelligence Center Reporting
                              security administrator gives them additional roles and flags them as Active users.

Local users can log in using their IMS username and password. After logging in for the first time, the users are listed on
                              the User List Page. The username is not case sensitive, but the password is case sensitive.

### System Application
                           	 User

This user role is defined during installation. Although it is possible
                              		to define unique application user names and passwords during the installation
                              		of each node, you must use the same credentials for all installations.

The application user defined during the installation of the Controller is the only System Application User recognized by
                              		Unified Intelligence Center.

This user has full rights to all functions in the Administration and
                              		Unified Intelligence Center Reporting applications, as described below:

Can log in to the Administration application and becomes the initial
                                    			 Super User for Administration.

Can create additional Super Users in the Administration
                                    			 application.

Can log in to Unified Intelligence Center and has full rights to all
                                    			 functions in Unified Intelligence Center.

Is the initial Security Administrator user in the Unified
                                    			 Intelligence Center Reporting application.

Can create additional Security Administrator users in the Unified
                                    			 Intelligence Center Reporting application.

Cannot have any role taken away from them.

Cannot take any role away from himself.

This user can log in to the Reporting application and is the initial
                                    			 System user.

### System
                           	 Administration User

The System
                              		Administrator account User ID and password are configured at installation for
                              		each node. You must enter the same user name and password for all nodes.

The System
                              		Administrator for the Controller can
                              		access:

The Cisco Systems
                                    			 tools on the Navigation drop-down menu in the Administration console: Disaster
                                    			 Recovery System, Cisco Unified Serviceability, and Cisco Unified OS
                                    			 Administration interfaces.

The CLI for the
                                    			 Controller.

The System
                              		Administrator has no access to functions in the Unified Intelligence Center
                              		Reporting application.

| Note | When you log in to the Admin Console site and you do not have any scheduled backup configured and enabled, Unified Intelligence
                                       Center returns the message "No active backup schedule is available. Set up a new schedule now." Unified Intelligence Center displays this message only for the administrator. |
|---|---|

| Step 1 | Direct your browser to the URL https://<HOST ADDRESS>/oamp where HOST ADDRESS is the IP Address or Hostname of your server. |
|---|---|
| Step 2 | Sign in using
                                       			 your Super User (system application user) ID and password. A successful sign-in
                                       			 launches the OAMP application. |

| To | Do this |
|---|---|
| Display the values for a function | Click a menu in the left navigation pane. |
| Open the Unified Intelligence Center reporting interface on a member node | Open a new browser window and enter this URL: https://<HOST ADDRESS>:8444/ where HOST ADDRESS is the IP Address or Hostname of your server. |
| Verify your signed on identity | This shows as protected text after Signed on as . Displays Administrator on the top-right corner of your screen. |
| Sign Out | Click Administrator > Sign Out on the top-right corner of your screen. |
| Return to this Home page | Click Home in the left navigation pane. |

| Note | If you configure
                                       		unique System Administrator credentials for Member nodes, use those credentials
                                       		to access the CLI for those Member servers. |
|---|---|