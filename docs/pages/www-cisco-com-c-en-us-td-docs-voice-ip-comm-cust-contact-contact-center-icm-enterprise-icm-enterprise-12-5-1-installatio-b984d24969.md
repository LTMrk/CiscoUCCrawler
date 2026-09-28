---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-installatio-b984d24969
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/installation/guide/ucce_b_1251-staging-guide/ucce_b_1251-staging-guide_chapter_0101.html
retrieved_at: 2026-08-16T20:08:12.695110+00:00
---

Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

# Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1)

Updated: February 5, 2020

Chapter: Service Account Manager

## Chapter: Service Account Manager

# Service Account Manager

## Service Account Management

The Service Account Manager allows you to use existing AD accounts as Unified ICM/CCE service accounts.

### Other Considerations

#### Permissions

You must have the correct privileges to associate the accounts in the local machine . Typically, a Domain User with local administrator privilaege performs this task.

#### Domain
                              	 Restriction

The following conditions are mandatory when adding or editing a service account using the Service Account Manager Tool or
                                 Websetup:

The service account must be in the same domain as the Unified ICM server.

The UPN (User Principal Name) must be set for the account in the Active Directory.

ensure that the account user login name set for UPN is same as the NETBIOS pre-windows 2000 login name (SAM Account Name).

Special Case : If the distributor service Account and logger service account are different then add the distributor service account in
                                 the logger.

#### Local Group Update Failures

If Service Account Manager fails to add the user in the local administrators group and local UCCE service account group then
                                 add the user to above mentioned groups manually.

#### Logging

The application
                                 		maintains its own log file, when you invoke it as a standalone application. If
                                 		you invoke it through the Web Setup tool, logs write to the Websetup log files
                                 		only.

## Service Account Manager End User Interfaces

The Service Account Manager has two user interfaces:

The Graphical User Interface consisting of the following dialogs boxes:

Main

Edit Service Account

The Command Line Interface

## Service Account
                        	 Manager GUI Dialog Boxes

You can find a shortcut to the application in Windows Start > Programs > Cisco Unified ICM-CCE Tools folder.

The Service Account
                              		  Manager has two dialog boxes:

Main

Edit Service
                                    				Account dialog box.

## Service Account
                        	 Manager – Main Dialog Box

You can use the Service Account Manager as a standalone application for Cisco Unified ICM/CCE Installer.

The Main Service
                              		  Account Manager dialog box is the application's primary interface. It consists
                              		  of the Services Requiring
                                 			 User Logon Accounts section (which contains the Service Name , Service Logon
                                 			 Account Name , Logon Account
                                 			 Health , Password
                                 			 Expiration , State , and Startup fields), the Facility/Instance drop-down; and the Select
                                 			 All , Edit
                                 			 Service Account , Fix Group
                                 			 Membership , Refresh , Close , and Help buttons.

The following table
                              		  provides a description for each field and button in this dialog box.

Field/Button/ Drop-down

Description

Service
                                          						Name

A list of all relevant services. If there are no relevant services on the server, such as a Administration & Data Server,
                                          or Logger; the field displays the message "This instance does not have any service that requires a service account."

Service
                                          						Logon Account Name

Displays
                                          						the service account name for the list of relevant services.

Logon
                                          						Account Health

The
                                          						Service Account Manager has an account health check mechanism. When the
                                          						application starts, it scans all relevant Unified ICM services and flags them
                                          						as indicated below.

Green

Healthy Account: the service account state is active.

Yellow

Password Warning: the password is due to expire in less than 7
                                                      								  days.

Red

Invalid Account : service
                                                      								  has an invalid account associated with it.

Password Expired : service
                                                      								  account password has expired.

Group Membership Missing : service account is missing from the required local security groups.

Account not associated with
                                                         									 service : service account created but not replicated, hence not associated
                                                      								  yet.

Account is locked out in domain : service has a locked out account associated with it.

The
                                          						following messages could appear in the Health column.

Healthy

Only applies to the service account, not the service itself.

The account is a member of the required UcceService local service and local admin groups.

The account has been validated to start a service.

If
                                                      								  the account password is changed outside of the Service Account Manager
                                                      								  application, Healthy would be displayed even though the service might not
                                                      								  actually be healthy because this application cannot detect the change.

Need to create service account

The Service Account Manager must be used to associate a service account for each service.

Account not a member of the UcceService local group

The Service Account Manager then places the account in the required UcceService local service group and local admin group,
                                                      and sets the required permissions.

Account Disabled

In AD, an account can be enabled or disabled. This message indicates that the account is disabled in the domain.

Password Expired

Account is locked out in domain

In AD, an account can be locked out because of domain policies.

Central Controller (sideA ) Domain name is unknown
                                                							 (Administration & Data Server only)

Administration & Data Servers can be in a different domain
                                                      								  than the Central Controller. When Fixed Group is selected, you are queried for the
                                                      								  domain name of the Central Controller if it is different than that of the
                                                      								  Administration & Data Server.

Central Controller (sideA ) Domain is not trusted or trust is
                                                							 not two-way (Administration & Data Server only)

There must be a two-way trust between the Central Controller and
                                                      								  the Administration & Data Server. SAM detects the lack of the trust
                                                      								  relationship and displays this message. SAM might detect this issue, but is
                                                      								  unable to fix it.

Account not a member of LoggerA Domain Service Group
                                                							 (Administration & Data Server only)

If the Administration & Data Server is on a different domain
                                                      								  than the Central Controller, it applies the Administration & Data Server's
                                                      								  Domain Service Group to both itself and the Central Controller.

Central Controller (sideB ) Domain name is unknown
                                                							 (Administration & Data Server only)

Administration & Data Servers can be in a different domain
                                                      								  than the Central Controller. When Fixed Group is selected, you are queried for the domain name
                                                      								  of the Central Controller if it is different than that of the Administration
                                                      								  & Data Server.

Central Controller (sideB ) Domain is not trusted or trust is
                                                							 not two-way (Administration & Data Server only)

There must be a two-way trust between the Central Controller and
                                                      								  the Disributor. SAM detects the lack of the trust relationship and displays
                                                      								  this message. SAM might detect this issue, but is unable to fix it.

Account not a member of LoggerB Domain Service Group
                                                							 (Administration & Data Server only)

If the Administration & Data Server is on a different domain
                                                      								  than the Central Controller, it applies the Administration & Data Server's
                                                      								  Domain Service Group to both itself and the Central Controller.

Account not associated with service

When SAM associates an account with a service it might run into
                                                      								  replication issues. Use Edit and select Associate the account with a service rather than
                                                      								  selecting editing from the beginning.

Service not validated for starting

When SAM validates a service it might run into replication
                                                      								  issues. Use Validate to successfully start the service.

Password About To Expire

Check the Password Expiration option to determine the validity
                                                      								  period of the password. The Service Account Manager can then be used to reset
                                                      								  the password for this pre-existing account.

A
                                          						service has an Invalid Account health state immediately after creation
                                          						because no domain account is assigned to it yet. This is expected behavior.

A service can have a Missing Group Membership problem due to a prior AD related failure. The Service Account Manager is capable of fixing this issue by providing an interface
                                          that re-attempts placing the account in the relevant local  security groups.

Password
                                          						Expiration

Any service with an account password that expires in seven (7)
                                                            								days is yellow flagged by the application.

You own the responsibility to refresh the passwords before they
                                                            								expire. If you do not, the system services fail to function.

State

The
                                          						current state of the service (Stopped, Start/Stop Pending, or Running).

Startup

Displays
                                          						how the service is started (Manual or Automatic).

Facility/Instance

Drop-down displaying the "Facility/Instance" name.

In case
                                          						of multiple instances, the default "Facility/Instance" selected in the drop-down is the last
                                          						instance edited by Setup.

Select a
                                          						specific instance. The Service Account Manager lists all relevant services with
                                          						their account information, account health, password expiration and startup
                                          						state for the selected instance.

If there are no relevant services on the server (such as a Administration & Data Server, or Logger) the Service Account Manager
                                          displays the message: This instance does not have any service that requires a service account.

Select All

Click to
                                          						select all listed services.

Edit Service
                                             						  Account

To fix any account issues, edit one, a few, or all accounts at the same time by selecting them and clicking this button.

When the dialog box appears, the Service Account Manager prompts you to try to use the account recently created, as it keeps
                                          track of it.  The application never stores the password.

Fix Group
                                             						  Membership

Available ONLY if an account with the Group
                                             						  Membership Missing health state is selected.

Refresh

Refreshes all information in the Service Account Manager Main
                                          						dialog box.

Close

Closes
                                          						the Service Account Manager dialog box.

Help

Select
                                          						to access the online help for the Service Account Manager.

## Service Account
                        	 Manager – Edit Service Account dialog box

The Edit Service Account dialog allows you to  use an existing account . From the Edit Service Account dialog, you can also modify the existing user account or password. The status bar at the bottom of the dialog box displays
                              status messages as needed.

The following table provides a description for each field, button, and check box for this dialog box:

Field/Button/check box

Description

Service(s)

Displays
                                          						the name of the service to be edited.

Service
                                          						account(s)

Displays
                                          						the account name for the selected service.

Account
                                          						Domain

Displays
                                          						the server domain. (Read Only)

Password

Enter the password associated with the account name.

Apply

Click to
                                          						apply any changes on this dialog box.

Close

Click to
                                          						close this dialog box.

If the services do not start automatically, you must start it manually using the CCE Service Control Tool.

If the
                                          						Service Account Manager finds that you did not successfully associate a valid
                                          						domain account with a service, it warns you that the service fails to function
                                          						until you use the Service Account Manager to associate a valid domain account
                                          						with the service.

Help

Select to
                                          						access the online help for the Service Account Manager.

## Command Line Interface for Service Account Manager

### Silent Setup for
                           	 Default Service Accounts

Web Setup uses the command line interface to silently associate service accounts.

Setup passes the
                                 		  following three arguments to the Service Account Manager:

/Instance
                                 		  <InstanceName>

The InstanceName
                                       				argument specifies the Unified ICM instance name for which the service is being
                                       				setup.

/Service
                                 		  <ServiceType>

The Service
                                       				argument specifies the type of the service whose account name and password are
                                       				being created.

For example:
                                       				/Service Distributor

Service types to
                                       				use are:

Distributor

LoggerA –
                                             					 Use when on Side A of the logger or for All-In-1 ICM/CCE

LoggerB –
                                             					 Use when on Side B of the logger only

/Log
                                 		  <Path\LogFileName>

The Log argument specifies the log file name and the path where the log is appended. Typically, Web Setup and Cisco Unified
                                       ICM/CCE Installer passes their own log file name to append the logs. The Service Account Manager also maintains its own log
                                       file in the temp folder.

If any one of
                                                   				  the arguments is missing or incorrect, the Service Account Manager returns an
                                                   				  error to Setup.

If Setup needs
                                                   				  to create accounts for more than one service, it invokes the Service Account
                                                   				  Manager multiple times using the command line interface.

/domainUser <Service Account>

The domainUser argument provides the Service Account that needs to be associated with the service.

/domainPassword <Password>

The domainPassword argument provides the Service Account password for the Service Account that needs to be associated with
                                       the service.

## Service Account Manager

### Update Existing
                           	 Account for Single Service

Step 1

Select a single
                                          			 service from Main Service Account Manager dialog box.

Step 2

Click Edit
                                             				Service Account .

The Edit Service
                                             				Account dialog box opens.

Step 3

Enter a
                                          			 password.

Step 4

Click Apply .

The Service Account Manager places the account in required UcceService local group and local admin group, and sets the required
                                             permissions.

### Update existing account for more than one Service

Step 1

Select multiple
                                          			 services or click Select
                                             				All on the Main Service Account Manager dialog box.

Step 2

Click Edit
                                             				Service Account .

The Edit Service
                                             				Account dialog box opens.

Step 3

Enter an account
                                          			 name.

Step 4

Enter a
                                          			 password.

Step 5

Click Apply .

The Service Account Manager then places the account in the required UcceService local group and local admin group, and sets
                                             the required permissions.

### Fix Account Displaying Adverse Health State

Fix Group Membership is only enabled when an account that is in an adverse health state, is selected. The health state is displayed by a message
                                 such as "Group Membership Missing" or "Account not a member of UcceService local group"

Step 1

Select the unhealthy accounts displaying a state such as the "Group Membership Missing" or "Account not a member of UcceService local group" state.

Step 2

Click Fix Group Membership .

Step 3

Click Apply .

The Service Account Manager then places the account in the required UcceService local service group and local admin group, and sets the required permissions.

| Field/Button/ Drop-down | Description |
|---|---|
| Service
                                          						Name | A list of all relevant services. If there are no relevant services on the server, such as a Administration & Data Server,
                                          or Logger; the field displays the message "This instance does not have any service that requires a service account." |
| Service
                                          						Logon Account Name | Displays
                                          						the service account name for the list of relevant services. |
| Logon
                                          						Account Health | The
                                          						Service Account Manager has an account health check mechanism. When the
                                          						application starts, it scans all relevant Unified ICM services and flags them
                                          						as indicated below. Green Healthy Account: the service account state is active. Yellow Password Warning: the password is due to expire in less than 7
                                                      								  days. Red Invalid Account : service
                                                      								  has an invalid account associated with it. Password Expired : service
                                                      								  account password has expired. Group Membership Missing : service account is missing from the required local security groups. Account not associated with
                                                         									 service : service account created but not replicated, hence not associated
                                                      								  yet. Account is locked out in domain : service has a locked out account associated with it. |
| The
                                          						following messages could appear in the Health column. Healthy Only applies to the service account, not the service itself. The account is a member of the required UcceService local service and local admin groups. The account has been validated to start a service. If
                                                      								  the account password is changed outside of the Service Account Manager
                                                      								  application, Healthy would be displayed even though the service might not
                                                      								  actually be healthy because this application cannot detect the change. Need to create service account The Service Account Manager must be used to associate a service account for each service. Account not a member of the UcceService local group The Service Account Manager then places the account in the required UcceService local service group and local admin group,
                                                      and sets the required permissions. Account Disabled In AD, an account can be enabled or disabled. This message indicates that the account is disabled in the domain. Password Expired Account is locked out in domain In AD, an account can be locked out because of domain policies. Central Controller (sideA ) Domain name is unknown
                                                							 (Administration & Data Server only) Administration & Data Servers can be in a different domain
                                                      								  than the Central Controller. When Fixed Group is selected, you are queried for the
                                                      								  domain name of the Central Controller if it is different than that of the
                                                      								  Administration & Data Server. Central Controller (sideA ) Domain is not trusted or trust is
                                                							 not two-way (Administration & Data Server only) There must be a two-way trust between the Central Controller and
                                                      								  the Administration & Data Server. SAM detects the lack of the trust
                                                      								  relationship and displays this message. SAM might detect this issue, but is
                                                      								  unable to fix it. Account not a member of LoggerA Domain Service Group
                                                							 (Administration & Data Server only) If the Administration & Data Server is on a different domain
                                                      								  than the Central Controller, it applies the Administration & Data Server's
                                                      								  Domain Service Group to both itself and the Central Controller. Central Controller (sideB ) Domain name is unknown
                                                							 (Administration & Data Server only) Administration & Data Servers can be in a different domain
                                                      								  than the Central Controller. When Fixed Group is selected, you are queried for the domain name
                                                      								  of the Central Controller if it is different than that of the Administration
                                                      								  & Data Server. Central Controller (sideB ) Domain is not trusted or trust is
                                                							 not two-way (Administration & Data Server only) There must be a two-way trust between the Central Controller and
                                                      								  the Disributor. SAM detects the lack of the trust relationship and displays
                                                      								  this message. SAM might detect this issue, but is unable to fix it. Account not a member of LoggerB Domain Service Group
                                                							 (Administration & Data Server only) If the Administration & Data Server is on a different domain
                                                      								  than the Central Controller, it applies the Administration & Data Server's
                                                      								  Domain Service Group to both itself and the Central Controller. Account not associated with service When SAM associates an account with a service it might run into
                                                      								  replication issues. Use Edit and select Associate the account with a service rather than
                                                      								  selecting editing from the beginning. Service not validated for starting When SAM validates a service it might run into replication
                                                      								  issues. Use Validate to successfully start the service. Password About To Expire Check the Password Expiration option to determine the validity
                                                      								  period of the password. The Service Account Manager can then be used to reset
                                                      								  the password for this pre-existing account. |
| A
                                          						service has an Invalid Account health state immediately after creation
                                          						because no domain account is assigned to it yet. This is expected behavior. A service can have a Missing Group Membership problem due to a prior AD related failure. The Service Account Manager is capable of fixing this issue by providing an interface
                                          that re-attempts placing the account in the relevant local  security groups. Note SAM
                                                   						health reporting might be inaccurate for the period of time while AD
                                                   						replication is in progress. The previous health state might be indicated during
                                                   						this time. | Note | SAM
                                                   						health reporting might be inaccurate for the period of time while AD
                                                   						replication is in progress. The previous health state might be indicated during
                                                   						this time. |
| Note | SAM
                                                   						health reporting might be inaccurate for the period of time while AD
                                                   						replication is in progress. The previous health state might be indicated during
                                                   						this time. |
| Password
                                          						Expiration | Note Any service with an account password that expires in seven (7)
                                                            								days is yellow flagged by the application. You own the responsibility to refresh the passwords before they
                                                            								expire. If you do not, the system services fail to function. | Note | Any service with an account password that expires in seven (7)
                                                            								days is yellow flagged by the application. You own the responsibility to refresh the passwords before they
                                                            								expire. If you do not, the system services fail to function. |
| Note | Any service with an account password that expires in seven (7)
                                                            								days is yellow flagged by the application. You own the responsibility to refresh the passwords before they
                                                            								expire. If you do not, the system services fail to function. |
| State | The
                                          						current state of the service (Stopped, Start/Stop Pending, or Running). |
| Startup | Displays
                                          						how the service is started (Manual or Automatic). |
| Facility/Instance | Drop-down displaying the "Facility/Instance" name. In case
                                          						of multiple instances, the default "Facility/Instance" selected in the drop-down is the last
                                          						instance edited by Setup. Select a
                                          						specific instance. The Service Account Manager lists all relevant services with
                                          						their account information, account health, password expiration and startup
                                          						state for the selected instance. If there are no relevant services on the server (such as a Administration & Data Server, or Logger) the Service Account Manager
                                          displays the message: This instance does not have any service that requires a service account. |
| Select All | Click to
                                          						select all listed services. |
| Edit Service
                                             						  Account | To fix any account issues, edit one, a few, or all accounts at the same time by selecting them and clicking this button. When the dialog box appears, the Service Account Manager prompts you to try to use the account recently created, as it keeps
                                          track of it.  The application never stores the password. |
| Fix Group
                                             						  Membership | Available ONLY if an account with the Group
                                             						  Membership Missing health state is selected. |
| Refresh | Refreshes all information in the Service Account Manager Main
                                          						dialog box. |
| Close | Closes
                                          						the Service Account Manager dialog box. |
| Help | Select
                                          						to access the online help for the Service Account Manager. |

| Note | SAM
                                                   						health reporting might be inaccurate for the period of time while AD
                                                   						replication is in progress. The previous health state might be indicated during
                                                   						this time. |
|---|---|

| Note | Any service with an account password that expires in seven (7)
                                                            								days is yellow flagged by the application. You own the responsibility to refresh the passwords before they
                                                            								expire. If you do not, the system services fail to function. |
|---|---|

| Field/Button/check box | Description |
|---|---|
| Service(s) | Displays
                                          						the name of the service to be edited. |
| Service
                                          						account(s) | Displays
                                          						the account name for the selected service. |
| Account
                                          						Domain | Displays
                                          						the server domain. (Read Only) |
| Password | Enter the password associated with the account name. |
| Apply | Click to
                                          						apply any changes on this dialog box. |
| Close | Click to
                                          						close this dialog box. Whenever this dialog box is closed, the Service Account Manager determines if a valid domain account is associated with the
                                          services or not. If the account is associated, the services must start automatically. Note If the services do not start automatically, you must start it manually using the CCE Service Control Tool. If the
                                          						Service Account Manager finds that you did not successfully associate a valid
                                          						domain account with a service, it warns you that the service fails to function
                                          						until you use the Service Account Manager to associate a valid domain account
                                          						with the service. | Note | If the services do not start automatically, you must start it manually using the CCE Service Control Tool. |
| Note | If the services do not start automatically, you must start it manually using the CCE Service Control Tool. |
| Help | Select to
                                          						access the online help for the Service Account Manager. |

| Note | If the services do not start automatically, you must start it manually using the CCE Service Control Tool. |
|---|---|

| Note | If any one of
                                                   				  the arguments is missing or incorrect, the Service Account Manager returns an
                                                   				  error to Setup. If Setup needs
                                                   				  to create accounts for more than one service, it invokes the Service Account
                                                   				  Manager multiple times using the command line interface. |
|---|---|

| Step 1 | Select a single
                                          			 service from Main Service Account Manager dialog box. |
|---|---|
| Step 2 | Click Edit
                                             				Service Account . The Edit Service
                                             				Account dialog box opens. |
| Step 3 | Enter a
                                          			 password. |
| Step 4 | Click Apply . The Service Account Manager places the account in required UcceService local group and local admin group, and sets the required
                                             permissions. |

| Step 1 | Select multiple
                                          			 services or click Select
                                             				All on the Main Service Account Manager dialog box. |
|---|---|
| Step 2 | Click Edit
                                             				Service Account . The Edit Service
                                             				Account dialog box opens. |
| Step 3 | Enter an account
                                          			 name. |
| Step 4 | Enter a
                                          			 password. |
| Step 5 | Click Apply . The Service Account Manager then places the account in the required UcceService local group and local admin group, and sets
                                             the required permissions. |

| Step 1 | Select the unhealthy accounts displaying a state such as the "Group Membership Missing" or "Account not a member of UcceService local group" state. |
|---|---|
| Step 2 | Click Fix Group Membership . |
| Step 3 | Click Apply . The Service Account Manager then places the account in the required UcceService local service group and local admin group, and sets the required permissions. Note If the Service Account Manager fails to place the accounts in
                                                      				the groups, it provides an appropriate error. | Note | If the Service Account Manager fails to place the accounts in
                                                      				the groups, it provides an appropriate error. |
| Note | If the Service Account Manager fails to place the accounts in
                                                      				the groups, it provides an appropriate error. |

| Note | If the Service Account Manager fails to place the accounts in
                                                      				the groups, it provides an appropriate error. |
|---|---|