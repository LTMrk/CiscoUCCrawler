---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-exchange-integration-15-cup0-b-ms-outlook-calendar-integrat-a6f9027fc9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/exchange_integration/15/cup0_b_ms-outlook-calendar-integration-15/cup0_b_ms-outlook-calender-integration-1251_chapter_0110.html
retrieved_at: 2026-08-16T16:15:29.309364+00:00
---

Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 15 and SUs

# Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 15 and SUs

Updated: March 18, 2026

Chapter: Configure Calendar Integration in IM and Presence Service

## Chapter: Configure Calendar Integration in IM and Presence Service

# Configure Calendar Integration in IM and Presence Service

## Calendar Integration Overview

### Microsoft Exchange for Calendar Integration

The Microsoft Exchange Calendar Integration feature in IM and Presence Service enables seamless synchronization between users
                              Microsoft Exchange calendars and their presence status in Cisco collaboration clients (such as Cisco Jabber). This integration
                              allows users availability status to automatically reflect their calendar appointments, providing real-time presence information
                              to colleagues across the organization.

Validation and support is performed using the major versions of Microsoft Exchange Server. It is expected that all other cumulative
                              updates of these major versions remain compatible. For example, when we mention Exchange 2016, it indicates that the IM and
                              Presence service supports all Cumulative Updates (CU) released under Exchange 2016.

### Microsoft Office 365 for Calendar Integration

IM and Presence Service pulls user calendar information from the Office 365-hosted Microsoft Outlook and displays it as a
                              part of an IM and Presence user's presence status.

A single IM and Presence Service server instance supports up to 7,500 presence status updates during simultaneous calendar
                              appointments.

## IM and Presence Calendar Integration Task Flow

Complete these tasks on the IM and Presence Service to set up calendar integration with Microsoft Outlook for either of the
                              following Microsoft deployments:

An on-premise Microsoft Exchange Server

A hosted Microsoft Office 365 Server

Step 1

Upload Microsoft Certificates to IM and Presence Service

Download the Microsoft certificates that will be required for integration with the IM and Presence Service.

Step 2

Configure a Presence Gateway

On the IM and Presence server, configure the Exchange server or Office 365 server as a Presence Gateway.

Step 3

Office 365 Configuration for Authentication

(Office 365 only) Use this procedure to configure the Presence Gateway Authentication Type, which is currently OAuth.

Step 4

Configure Pull Interval for Office 365 Integration

(Office 365 only) Configure the interval schedule by which the IM and Presence Service pulls calendar information from Office
                                          365. The default value is 60 minutes.

Step 5

Configure Calendar Out of Office Information

(Optional) Configure the Out of Office information to display the "Out of Office" status. This setting is applicable for all
                                          the users that have the calendaring service enabled or not. The default value is 'Do not display Out of Office availability.'

Step 6

Configure Service Parameters for Exchange Integration

(Exchange only) Configure optional service parameters that outline the calendar sync interaction with the Microsoft Exchange
                                          Server.

Step 7

Restart the Cisco Presence Engine

If you edited any service parameters, restart the Cisco Presence Engine service.

Step 8

Enable calendaring for users using one of the following procedures:

- Enable Calendaring During Initial LDAP Synchronization

- Enable Calendar Integrations by Bulk

- Enable Calendar Integration for a User

Select the procedure that fits your needs:

If you have not yet completed an LDAP sync, enable calendaring via the LDAP sync.

Otherwise, use the Bulk Administration Tool to configure calendaring for many users.

Or enable the feature on a user by user basis.

### Upload Microsoft Certificates to IM and Presence Service

For the IM and Presence Service and the Office 365 deployment to communicate, you must install the Microsoft certificates
                                 on the IM and Presence Service.

Step 1

Download an Office 365 root certificate, and intermediate certificate:

- The following site lists all of the root and intermediate certificates that Office 365 supports: https://support.office.com/en-us/article/office-365-certificate-chains-0c03e6b3-e73f-4316-9e2b-bf4091ae96bb

Step 2

Upload all certificates to the cup-trust and tomcat-trust stores on the IM and Presence Service.

For additional details on certificates with the IM and Presence Service, refer to the "Security Configuration on IM and Presence
                                             Service" chapter of the Configuration and Administration Guide for IM and Presence Service .

#### What to do next

IM and Presence Calendar Integration Task Flow

### Configure a Presence Gateway

Use this procedure to configure a Presence Gateway to set up calendar integration with Microsoft Outlook. You can assign either
                                 a Microsoft Exchange Server or a Microsoft Office 365 server as the Presence Gateway.

Step 1

From Cisco Unified CM IM and Presence Administration, choose Presence > Gateways .

Step 2

Click Add New .

Step 3

From the Presence Gateway Type field, choose one of the following options:

Select Exchange - - EWS Server , if you are integrating with an on-premise Exchange server.

Select Office 365 Server , if you are integrating with a hosted Office 365 server.

If you choose Office 365 Server , then by default the Authentication Type is selected as OAuth .

The fields Application (client) ID , Directory (tenant) ID , and Client Secret are applicable only for Office 365 Server.

The values Application (client) ID , Directory (tenant) ID , and Client Secret must match the values configured in the Office 365 Server.

Step 4

In the Description field, enter a description that helps you to distinguish the presence gateway instance.

Step 5

In the Presence Gateway field, enter the fully qualified domain name or IP address of the Presence Gateway server. This value must match the server
                                          address that is displayed in the Subject Common Name (CN) or Subject Alternate Name field of the server certificate.

Step 6

In the Account Name field, enter the account name to access the server.

Step 7

Enter the password that the account uses to access the server in both the Account Password and Confirm Password fields.

Step 8

In the Presence Gateway Port field, enter the port used to connect to calendaring service. The default port is 443.

Step 9

(Office 365 only) In the HTTP/HTTPS Proxy URL field, assign HTTP/HTTPS Proxy server details, if the Presence Gateway Type is Office 365 Server and IM and Presence Service doesn’t have access to Office 365 Server.

Step 10

(Office 365 only) In the HTTP/HTTPS Proxy Username field, enter the user name to access the HTTP/HTTPS proxy server.

Step 11

(Office 365 only) In the HTTP/HTTPS Proxy Password field, enter the password for the user name provided for HTTP/HTTPS proxy server.

The configuration options in steps 12 and 13 are available starting with Release 15SU2.

Step 12

(Office 365 only) In the AD Authentication Endpoint field, the default URL is https://login.microsoftonline.com . In case you want to enter a customized URL, click the edit icon.

Step 13

(Office 365 only) In the Resource URI field, the default URL is https://outlook.office365.com . For Release 15SU4 and later, the default URL is https://graph.microsoft.com . In case you want to enter a customized URL, click the edit icon.

Step 14

Click Save .

For more information on setting the limits on the TLS version which will be used for establishing the secure HTTP connection,
                                                         see the Security Guide for Cisco Unified Communications Manager .

### Office 365 Configuration for Authentication

Use this procedure to configure the Presence Gateway Authentication Type, which is currently OAuth.

Step 1

Log in to Microsoft Azure portal: https://portal.azure.com .

Step 2

Register the new Application and fetch Application (client) ID and Directory (tenant) ID by following the steps available at: https://docs.microsoft.com/en-gb/azure/active-directory/develop/quickstart-register-app#register-a-new-application-using-the-azure-portal .

Step 3

To create the Client Secret , under Manage , click Certificates & Secrets > New Client Secret . And, obtain the client secret value.

If you select Presence Gateway Type as Office 365 Server, use the same values to configure the Application (client) ID , Directory (tenant) ID , and Client Secret fields in the IM and Presence Service during Presence Gateway setup.

Step 4

Click Manage > API Permissions > Add a permission , and choose Office 365 Exchange Online under APIs my organization uses .

Step 5

To add an application permission, select Application permissions > Permission ,  check the Calendars.ReadBasic.All check box, and click Add permissions .

To retrieve Out of Office information, grant the MailBoxSettings.Read permission.

Step 6

To grant admin consent, click Manage > API permissions .

Step 7

Under Grant consent , click Grant admin consent for "registered Azure Active Directory" and choose Yes .

Step 8

Check if there is a green tick mark against Status column for the allocated permissions.

### Configure Pull Interval for Office 365 Integration

Use this procedure to configure the interval period following which the IM and Presence Service pulls calendar information
                                 from Office 365.

#### Before you begin

Office 365 Configuration for Authentication

Step 1

From Cisco Unified CM IM and Presence Administration, choose System > Service Parameters .

Step 2

From the Server drop-down, choose the IM and Presence publisher node.

Step 3

From the Service drop-down, choose Cisco Presence Engine .

Step 4

Configure an interval, in minutes for the Office 365 Calendar Information Pull Interval service parameter. The default is 60 minutes.

Step 5

Click Save .

### Configure Calendar Out of Office Information

#### Before you begin

Office 365 Configuration for Authentication

Step 1

From Cisco Unified CM IM and Presence Administration, choose System > Service Parameters .

Step 2

From the Server drop-down, choose the IM and Presence publisher node.

Step 3

From the Service drop-down, choose Cisco Presence Engine .

Step 4

In the Calendar Out of Office information service parameter, select Display Out of Office availability to update the user's availability status in the Cisco Jabber client to "Out of Office" whenever the user sets their status
                                          to "Out of Office" on the Microsoft Office 365 or Exchange server.

Step 5

Click Save .

### Configure Service Parameters for Exchange Integration

Use this optional procedure to configure optional service parameters for Outlook calendar integration with a Microsoft Exchange
                                 server. The default values may be sufficient for many parameters.

Step 1

From Cisco Unified CM IM and Presence Administration, choose System > Service Parameters .

Step 2

From the Server drop-down, choose the IM and Presence publisher node.

Step 3

From the Service drop-down, choose Cisco Presence Engine .

Step 4

Under Calendaring Configuration , configure values for the following parameters:

Service Parameter

Description

Microsoft Exchange Notification Port

The port number that the Presence Engine will listen on for incoming notifications from the Exchange server. UDP is used for
                                                         WebDav and TCP is used for EWS (Exchange Web Services). Possible values are 1024-65535 with a default value of 50020.

Calendar Spread (seconds)

This parameter specifies the range of duration in seconds. Each user will be assigned an offset duration by a hash. The duration
                                                         will determine the number of seconds after the top-of-minute that meeting transitions will be sent. The duration can be shortened
                                                         for smaller numbers of users (approx. users / 100 = seconds). It is used for WebDav and EWS (Exchange Web Services). The range
                                                         of values is 0-59 with a default value of 50 seconds.

Exchange Timeout (seconds)

This parameter specifies the duration, in seconds, before a request made to an Exchange server times out. This change requires
                                                         a restart of the Cisco Presence Engine. The range of possible values is 1-20 with a default value of 3 seconds.

Exchange Queue

This parameter specifies the maximum length of the Exchange request queue. If a request is made and the queue length is exceeded,
                                                         the request will fail and a recovery procedure will be initiated. This change requires a restart of the Cisco Presence Engine.
                                                         Possible values are 1-5000 with a default value of 2200.

Exchange Threads

This parameter specifies the number of threads that are used to service Exchange requests. You can increase this value if
                                                         there are a large number of users (for example, 5000) or if some Exchange transactions take longer than 3 seconds. If calendar
                                                         integration is disabled, set this parameter to 1. This change requires a restart of the Cisco Presence Engine. Possible values
                                                         are 1-100 with a default value of 60.

EWS Status Frequency (minutes)

This parameter specifies how often notification messages are sent from the Exchange server when EWS (Exchange Web Services)
                                                         is used. The duration is in minutes. Possible values are 10-1440 with a default value of 60.

FIPS Mode Exchange Server Authentication

This parameter specifies the type of authentication that the Presence Engine uses to establish a connection with the Exchange
                                                         Server. When set to "Auto," the Presence Engine negotiates NTLMv2 first and falls back to Basic Authentication only if NTLMv2
                                                         negotiation fails. NTLMv1 is not negotiated in FIPS mode. When set to "Basic Only," the Presence Engine always uses Basic
                                                         Authentication, even if the Exchange Server is configured to allow both NTLM and Basic. This parameter applies only in FIPS
                                                         mode. Changing this parameter requires you to restart the Cisco Presence Engine. The default value is Auto.

Step 5

Click Save .

#### What to do next

Restart the Cisco Presence Engine

### Restart the Cisco Presence Engine

If you changed the values for any of the Calendaring Configuration service parameters, restart the Cisco Presence Engine service.

Step 1

From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services .

Step 2

From the Server drop-down, choose the IM and Presence server and click Go .

Step 3

Under IM and Presence Services , select Cisco Presence Engine and click Restart .

#### What to do next

Enable calendaring for IM and Presence Service users. To enable the feature for a large number of users at once, you can use
                                 an LDAP sync if  users are synced from an external LDAP directory, or the Bulk Administration Tool for non-LDAP users. Otherwise,
                                 you can enable the feature for users on an individual basis.

Enable Calendaring During Initial LDAP Synchronization

Enable Calendar Integrations by Bulk

Enable Calendar Integration for a User

### Enable Calendaring During Initial LDAP Synchronization

Complete these tasks to enable calendaring before the initial LDAP directory sync. Enable the calendaring feature during the
                                 initial LDAP synchronization process to automatically provision calendaring services for all users as they are imported from
                                 the LDAP directory. This setting must be configured prior to performing the initial synchronization.

Step 1

Add Calendar Integration to a Feature Group Template

Assign calendaring to a feature group template.

Step 2

Add Feature Group Template to LDAP Sync

Assign your calendaring-enabled feature group template to an LDAP directory sync and complete a sync.

#### Add Calendar Integration to a Feature Group Template

Use this procedure to assign Microsoft Outlook calendaring integration to a feature group template.  You can use the template
                                    to configure Outlook calendar integration for all users synchronized from an LDAP directory

You can only add or edit feature group template settings for an LDAP directory that has not yet been synced. If the directory
                                                is already synced, use Enable Calendar Integrations by Bulk instead.

Step 1

From Cisco Unified CM Administration, choose User Management > User Phone/Add > Feature Group Template .

Step 2

Complete one of the following steps:

- Click Add New to create a new template.

- Click Find and select an existing template

Step 3

Check the Enable User for Unified CM IM and Presence check box

Step 4

Check the Include meeting information in Presence check box

Step 5

Complete the remaining fields in the Feature Group Template configuration window. For help with the fields and their settings, see the online help.

Step 6

Click Save .

##### What to do next

Add Feature Group Template to LDAP Sync

#### Add Feature Group Template to LDAP Sync

Use this procedure to assign the calendaring-enabled feature group template that you just created to an LDAP Directory sync.
                                    This will allow you to enable Outlook calendar integration for all users synced from this LDAP Directory.

You can only add a feature group template to an LDAP directory that has not yet been synced. If the directory is already synced,
                                                use Enable Calendar Integrations by Bulk instead.

##### Before you begin

Add Calendar Integration to a Feature Group Template

Step 1

From Cisco Unified CM Administration choose System > LDAP > LDAP Directory .

Step 2

Click Find and select an existing LDAP
                                             Directory.

Step 3

From the Feature Group Template drop-down menu,
                                             select the calendaring-enabled feature group template that you
                                             created in the previous task.

Step 4

Complete the remaining fields in the LDAP
                                                Directory window. For help with the fields and their settings, see the online help.

Step 5

Click Save .

Step 6

Click Perform Full Sync Now .

### Enable Calendar Integrations by Bulk

Use Bulk Administration to enable calendar integration for a large number of users in a single operation.

Enabling Calendar Integration via the Bulk Administration tool consumes significant system resources. This operation may affect
                                             system performance and user experience. We recommend that you schedule this operation during off-business hours to minimize
                                             disruption and maintain optimal system performance.

Step 1

On a Cisco
                                             				Unified Communications Manager node, log in to the Cisco Unified CM
                                             			 Administration user interface.

Step 2

Enabling
                                          			 calendar integrations in bulk can be performed from the following windows:

Bulk
                                                      						Administration > Users > Insert Users .

Bulk
                                                      						Administration > Users > Update Users > Query .

Bulk
                                                      						Administration > Users > Update Users > Custom
                                                      						File .

For information on the different types of update options, refer to the Bulk Administration Guide for Cisco Unified Communications Manager .

Step 3

For all end users for whom you want to enable calendar integration, make sure that the following end user configuration options
                                          are checked:

- Enable User for Unified CM IM and Presence

- Include meeting information in Presence

Step 4

If you are updating from a csv file, in the
                                          			 appropriate Users area, choose a File Name.

Step 5

Click Run
                                             				Immediately or Run
                                             				Later .

Step 6

Click Submit .

### Enable Calendar Integration for a User

Use this procedure to enable calendar integration for an IM and Presence Service user.

Step 1

Log in to
                                          			 the Cisco Unified CM Administration user interface.

Step 2

Choose User
                                                				  Management > End User .

Step 3

Click Find and select an end user.

Step 4

Check the Enable User for Unified CM IM and Presence check box.

Step 5

Check the Include meeting information in presence check box.

Step 6

Click Save .

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Upload Microsoft Certificates to IM and Presence Service | Download the Microsoft certificates that will be required for integration with the IM and Presence Service. |
| Step 2 | Configure a Presence Gateway | On the IM and Presence server, configure the Exchange server or Office 365 server as a Presence Gateway. |
| Step 3 | Office 365 Configuration for Authentication | (Office 365 only) Use this procedure to configure the Presence Gateway Authentication Type, which is currently OAuth. |
| Step 4 | Configure Pull Interval for Office 365 Integration | (Office 365 only) Configure the interval schedule by which the IM and Presence Service pulls calendar information from Office
                                          365. The default value is 60 minutes. |
| Step 5 | Configure Calendar Out of Office Information | (Optional) Configure the Out of Office information to display the "Out of Office" status. This setting is applicable for all
                                          the users that have the calendaring service enabled or not. The default value is 'Do not display Out of Office availability.' |
| Step 6 | Configure Service Parameters for Exchange Integration | (Exchange only) Configure optional service parameters that outline the calendar sync interaction with the Microsoft Exchange
                                          Server. |
| Step 7 | Restart the Cisco Presence Engine | If you edited any service parameters, restart the Cisco Presence Engine service. |
| Step 8 | Enable calendaring for users using one of the following procedures: Enable Calendaring During Initial LDAP Synchronization Enable Calendar Integrations by Bulk Enable Calendar Integration for a User | Select the procedure that fits your needs: If you have not yet completed an LDAP sync, enable calendaring via the LDAP sync. Otherwise, use the Bulk Administration Tool to configure calendaring for many users. Or enable the feature on a user by user basis. |

| Step 1 | Download an Office 365 root certificate, and intermediate certificate: The following site lists all of the root and intermediate certificates that Office 365 supports: https://support.office.com/en-us/article/office-365-certificate-chains-0c03e6b3-e73f-4316-9e2b-bf4091ae96bb |
|---|---|
| Step 2 | Upload all certificates to the cup-trust and tomcat-trust stores on the IM and Presence Service. |

| Note | For additional details on certificates with the IM and Presence Service, refer to the "Security Configuration on IM and Presence
                                             Service" chapter of the Configuration and Administration Guide for IM and Presence Service . |
|---|---|

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose Presence > Gateways . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | From the Presence Gateway Type field, choose one of the following options: Select Exchange - - EWS Server , if you are integrating with an on-premise Exchange server. Select Office 365 Server , if you are integrating with a hosted Office 365 server. If you choose Office 365 Server , then by default the Authentication Type is selected as OAuth . Note The fields Application (client) ID , Directory (tenant) ID , and Client Secret are applicable only for Office 365 Server. The values Application (client) ID , Directory (tenant) ID , and Client Secret must match the values configured in the Office 365 Server. | Note | The fields Application (client) ID , Directory (tenant) ID , and Client Secret are applicable only for Office 365 Server. |
| Note | The fields Application (client) ID , Directory (tenant) ID , and Client Secret are applicable only for Office 365 Server. |
| Step 4 | In the Description field, enter a description that helps you to distinguish the presence gateway instance. |
| Step 5 | In the Presence Gateway field, enter the fully qualified domain name or IP address of the Presence Gateway server. This value must match the server
                                          address that is displayed in the Subject Common Name (CN) or Subject Alternate Name field of the server certificate. |
| Step 6 | In the Account Name field, enter the account name to access the server. |
| Step 7 | Enter the password that the account uses to access the server in both the Account Password and Confirm Password fields. |
| Step 8 | In the Presence Gateway Port field, enter the port used to connect to calendaring service. The default port is 443. |
| Step 9 | (Office 365 only) In the HTTP/HTTPS Proxy URL field, assign HTTP/HTTPS Proxy server details, if the Presence Gateway Type is Office 365 Server and IM and Presence Service doesn’t have access to Office 365 Server. |
| Step 10 | (Office 365 only) In the HTTP/HTTPS Proxy Username field, enter the user name to access the HTTP/HTTPS proxy server. |
| Step 11 | (Office 365 only) In the HTTP/HTTPS Proxy Password field, enter the password for the user name provided for HTTP/HTTPS proxy server. Note The configuration options in steps 12 and 13 are available starting with Release 15SU2. | Note | The configuration options in steps 12 and 13 are available starting with Release 15SU2. |
| Note | The configuration options in steps 12 and 13 are available starting with Release 15SU2. |
| Step 12 | (Office 365 only) In the AD Authentication Endpoint field, the default URL is https://login.microsoftonline.com . In case you want to enter a customized URL, click the edit icon. |
| Step 13 | (Office 365 only) In the Resource URI field, the default URL is https://outlook.office365.com . For Release 15SU4 and later, the default URL is https://graph.microsoft.com . In case you want to enter a customized URL, click the edit icon. |
| Step 14 | Click Save . Note For more information on setting the limits on the TLS version which will be used for establishing the secure HTTP connection,
                                                         see the Security Guide for Cisco Unified Communications Manager . | Note | For more information on setting the limits on the TLS version which will be used for establishing the secure HTTP connection,
                                                         see the Security Guide for Cisco Unified Communications Manager . |
| Note | For more information on setting the limits on the TLS version which will be used for establishing the secure HTTP connection,
                                                         see the Security Guide for Cisco Unified Communications Manager . |

| Note | The fields Application (client) ID , Directory (tenant) ID , and Client Secret are applicable only for Office 365 Server. |
|---|---|

| Note | The configuration options in steps 12 and 13 are available starting with Release 15SU2. |
|---|---|

| Note | For more information on setting the limits on the TLS version which will be used for establishing the secure HTTP connection,
                                                         see the Security Guide for Cisco Unified Communications Manager . |
|---|---|

| Step 1 | Log in to Microsoft Azure portal: https://portal.azure.com . |
|---|---|
| Step 2 | Register the new Application and fetch Application (client) ID and Directory (tenant) ID by following the steps available at: https://docs.microsoft.com/en-gb/azure/active-directory/develop/quickstart-register-app#register-a-new-application-using-the-azure-portal . |
| Step 3 | To create the Client Secret , under Manage , click Certificates & Secrets > New Client Secret . And, obtain the client secret value. Note If you select Presence Gateway Type as Office 365 Server, use the same values to configure the Application (client) ID , Directory (tenant) ID , and Client Secret fields in the IM and Presence Service during Presence Gateway setup. | Note | If you select Presence Gateway Type as Office 365 Server, use the same values to configure the Application (client) ID , Directory (tenant) ID , and Client Secret fields in the IM and Presence Service during Presence Gateway setup. |
| Note | If you select Presence Gateway Type as Office 365 Server, use the same values to configure the Application (client) ID , Directory (tenant) ID , and Client Secret fields in the IM and Presence Service during Presence Gateway setup. |
| Step 4 | Click Manage > API Permissions > Add a permission , and choose Office 365 Exchange Online under APIs my organization uses . |
| Step 5 | To add an application permission, select Application permissions > Permission ,  check the Calendars.ReadBasic.All check box, and click Add permissions . Note To retrieve Out of Office information, grant the MailBoxSettings.Read permission. | Note | To retrieve Out of Office information, grant the MailBoxSettings.Read permission. |
| Note | To retrieve Out of Office information, grant the MailBoxSettings.Read permission. |
| Step 6 | To grant admin consent, click Manage > API permissions . |
| Step 7 | Under Grant consent , click Grant admin consent for "registered Azure Active Directory" and choose Yes . |
| Step 8 | Check if there is a green tick mark against Status column for the allocated permissions. |

| Note | If you select Presence Gateway Type as Office 365 Server, use the same values to configure the Application (client) ID , Directory (tenant) ID , and Client Secret fields in the IM and Presence Service during Presence Gateway setup. |
|---|---|

| Note | To retrieve Out of Office information, grant the MailBoxSettings.Read permission. |
|---|---|

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down, choose the IM and Presence publisher node. |
| Step 3 | From the Service drop-down, choose Cisco Presence Engine . |
| Step 4 | Configure an interval, in minutes for the Office 365 Calendar Information Pull Interval service parameter. The default is 60 minutes. |
| Step 5 | Click Save . |

| Note | The IM and Presence Service pulls information from Office 365 at scheduled intervals as specified by the Office 365 Calendar Information Pull Interval service parameter (default value is 60 minutes). However, there is no mechanism for pushing information from Office 365 to
                                          the IM and Presence Service. As a result, if a non-scheduled Presence update occurs in Office 365 between scheduled pulls
                                          (for example, an ad hoc meeting), the results do not register with the IM and Presence Service until after the next scheduled
                                          pull. |
|---|---|

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down, choose the IM and Presence publisher node. |
| Step 3 | From the Service drop-down, choose Cisco Presence Engine . |
| Step 4 | In the Calendar Out of Office information service parameter, select Display Out of Office availability to update the user's availability status in the Cisco Jabber client to "Out of Office" whenever the user sets their status
                                          to "Out of Office" on the Microsoft Office 365 or Exchange server. |
| Step 5 | Click Save . |

| Step 1 | From Cisco Unified CM IM and Presence Administration, choose System > Service Parameters . |
|---|---|
| Step 2 | From the Server drop-down, choose the IM and Presence publisher node. |
| Step 3 | From the Service drop-down, choose Cisco Presence Engine . |
| Step 4 | Under Calendaring Configuration , configure values for the following parameters: Table 1. Service Parameters for Exchange Integration Service Parameter Description Microsoft Exchange Notification Port The port number that the Presence Engine will listen on for incoming notifications from the Exchange server. UDP is used for
                                                         WebDav and TCP is used for EWS (Exchange Web Services). Possible values are 1024-65535 with a default value of 50020. Calendar Spread (seconds) This parameter specifies the range of duration in seconds. Each user will be assigned an offset duration by a hash. The duration
                                                         will determine the number of seconds after the top-of-minute that meeting transitions will be sent. The duration can be shortened
                                                         for smaller numbers of users (approx. users / 100 = seconds). It is used for WebDav and EWS (Exchange Web Services). The range
                                                         of values is 0-59 with a default value of 50 seconds. Exchange Timeout (seconds) This parameter specifies the duration, in seconds, before a request made to an Exchange server times out. This change requires
                                                         a restart of the Cisco Presence Engine. The range of possible values is 1-20 with a default value of 3 seconds. Exchange Queue This parameter specifies the maximum length of the Exchange request queue. If a request is made and the queue length is exceeded,
                                                         the request will fail and a recovery procedure will be initiated. This change requires a restart of the Cisco Presence Engine.
                                                         Possible values are 1-5000 with a default value of 2200. Exchange Threads This parameter specifies the number of threads that are used to service Exchange requests. You can increase this value if
                                                         there are a large number of users (for example, 5000) or if some Exchange transactions take longer than 3 seconds. If calendar
                                                         integration is disabled, set this parameter to 1. This change requires a restart of the Cisco Presence Engine. Possible values
                                                         are 1-100 with a default value of 60. EWS Status Frequency (minutes) This parameter specifies how often notification messages are sent from the Exchange server when EWS (Exchange Web Services)
                                                         is used. The duration is in minutes. Possible values are 10-1440 with a default value of 60. FIPS Mode Exchange Server Authentication This parameter specifies the type of authentication that the Presence Engine uses to establish a connection with the Exchange
                                                         Server. When set to "Auto," the Presence Engine negotiates NTLMv2 first and falls back to Basic Authentication only if NTLMv2
                                                         negotiation fails. NTLMv1 is not negotiated in FIPS mode. When set to "Basic Only," the Presence Engine always uses Basic
                                                         Authentication, even if the Exchange Server is configured to allow both NTLM and Basic. This parameter applies only in FIPS
                                                         mode. Changing this parameter requires you to restart the Cisco Presence Engine. The default value is Auto. | Service Parameter | Description | Microsoft Exchange Notification Port | The port number that the Presence Engine will listen on for incoming notifications from the Exchange server. UDP is used for
                                                         WebDav and TCP is used for EWS (Exchange Web Services). Possible values are 1024-65535 with a default value of 50020. | Calendar Spread (seconds) | This parameter specifies the range of duration in seconds. Each user will be assigned an offset duration by a hash. The duration
                                                         will determine the number of seconds after the top-of-minute that meeting transitions will be sent. The duration can be shortened
                                                         for smaller numbers of users (approx. users / 100 = seconds). It is used for WebDav and EWS (Exchange Web Services). The range
                                                         of values is 0-59 with a default value of 50 seconds. | Exchange Timeout (seconds) | This parameter specifies the duration, in seconds, before a request made to an Exchange server times out. This change requires
                                                         a restart of the Cisco Presence Engine. The range of possible values is 1-20 with a default value of 3 seconds. | Exchange Queue | This parameter specifies the maximum length of the Exchange request queue. If a request is made and the queue length is exceeded,
                                                         the request will fail and a recovery procedure will be initiated. This change requires a restart of the Cisco Presence Engine.
                                                         Possible values are 1-5000 with a default value of 2200. | Exchange Threads | This parameter specifies the number of threads that are used to service Exchange requests. You can increase this value if
                                                         there are a large number of users (for example, 5000) or if some Exchange transactions take longer than 3 seconds. If calendar
                                                         integration is disabled, set this parameter to 1. This change requires a restart of the Cisco Presence Engine. Possible values
                                                         are 1-100 with a default value of 60. | EWS Status Frequency (minutes) | This parameter specifies how often notification messages are sent from the Exchange server when EWS (Exchange Web Services)
                                                         is used. The duration is in minutes. Possible values are 10-1440 with a default value of 60. | FIPS Mode Exchange Server Authentication | This parameter specifies the type of authentication that the Presence Engine uses to establish a connection with the Exchange
                                                         Server. When set to "Auto," the Presence Engine negotiates NTLMv2 first and falls back to Basic Authentication only if NTLMv2
                                                         negotiation fails. NTLMv1 is not negotiated in FIPS mode. When set to "Basic Only," the Presence Engine always uses Basic
                                                         Authentication, even if the Exchange Server is configured to allow both NTLM and Basic. This parameter applies only in FIPS
                                                         mode. Changing this parameter requires you to restart the Cisco Presence Engine. The default value is Auto. |
| Service Parameter | Description |
| Microsoft Exchange Notification Port | The port number that the Presence Engine will listen on for incoming notifications from the Exchange server. UDP is used for
                                                         WebDav and TCP is used for EWS (Exchange Web Services). Possible values are 1024-65535 with a default value of 50020. |
| Calendar Spread (seconds) | This parameter specifies the range of duration in seconds. Each user will be assigned an offset duration by a hash. The duration
                                                         will determine the number of seconds after the top-of-minute that meeting transitions will be sent. The duration can be shortened
                                                         for smaller numbers of users (approx. users / 100 = seconds). It is used for WebDav and EWS (Exchange Web Services). The range
                                                         of values is 0-59 with a default value of 50 seconds. |
| Exchange Timeout (seconds) | This parameter specifies the duration, in seconds, before a request made to an Exchange server times out. This change requires
                                                         a restart of the Cisco Presence Engine. The range of possible values is 1-20 with a default value of 3 seconds. |
| Exchange Queue | This parameter specifies the maximum length of the Exchange request queue. If a request is made and the queue length is exceeded,
                                                         the request will fail and a recovery procedure will be initiated. This change requires a restart of the Cisco Presence Engine.
                                                         Possible values are 1-5000 with a default value of 2200. |
| Exchange Threads | This parameter specifies the number of threads that are used to service Exchange requests. You can increase this value if
                                                         there are a large number of users (for example, 5000) or if some Exchange transactions take longer than 3 seconds. If calendar
                                                         integration is disabled, set this parameter to 1. This change requires a restart of the Cisco Presence Engine. Possible values
                                                         are 1-100 with a default value of 60. |
| EWS Status Frequency (minutes) | This parameter specifies how often notification messages are sent from the Exchange server when EWS (Exchange Web Services)
                                                         is used. The duration is in minutes. Possible values are 10-1440 with a default value of 60. |
| FIPS Mode Exchange Server Authentication | This parameter specifies the type of authentication that the Presence Engine uses to establish a connection with the Exchange
                                                         Server. When set to "Auto," the Presence Engine negotiates NTLMv2 first and falls back to Basic Authentication only if NTLMv2
                                                         negotiation fails. NTLMv1 is not negotiated in FIPS mode. When set to "Basic Only," the Presence Engine always uses Basic
                                                         Authentication, even if the Exchange Server is configured to allow both NTLM and Basic. This parameter applies only in FIPS
                                                         mode. Changing this parameter requires you to restart the Cisco Presence Engine. The default value is Auto. |
| Step 5 | Click Save . |

| Service Parameter | Description |
|---|---|
| Microsoft Exchange Notification Port | The port number that the Presence Engine will listen on for incoming notifications from the Exchange server. UDP is used for
                                                         WebDav and TCP is used for EWS (Exchange Web Services). Possible values are 1024-65535 with a default value of 50020. |
| Calendar Spread (seconds) | This parameter specifies the range of duration in seconds. Each user will be assigned an offset duration by a hash. The duration
                                                         will determine the number of seconds after the top-of-minute that meeting transitions will be sent. The duration can be shortened
                                                         for smaller numbers of users (approx. users / 100 = seconds). It is used for WebDav and EWS (Exchange Web Services). The range
                                                         of values is 0-59 with a default value of 50 seconds. |
| Exchange Timeout (seconds) | This parameter specifies the duration, in seconds, before a request made to an Exchange server times out. This change requires
                                                         a restart of the Cisco Presence Engine. The range of possible values is 1-20 with a default value of 3 seconds. |
| Exchange Queue | This parameter specifies the maximum length of the Exchange request queue. If a request is made and the queue length is exceeded,
                                                         the request will fail and a recovery procedure will be initiated. This change requires a restart of the Cisco Presence Engine.
                                                         Possible values are 1-5000 with a default value of 2200. |
| Exchange Threads | This parameter specifies the number of threads that are used to service Exchange requests. You can increase this value if
                                                         there are a large number of users (for example, 5000) or if some Exchange transactions take longer than 3 seconds. If calendar
                                                         integration is disabled, set this parameter to 1. This change requires a restart of the Cisco Presence Engine. Possible values
                                                         are 1-100 with a default value of 60. |
| EWS Status Frequency (minutes) | This parameter specifies how often notification messages are sent from the Exchange server when EWS (Exchange Web Services)
                                                         is used. The duration is in minutes. Possible values are 10-1440 with a default value of 60. |
| FIPS Mode Exchange Server Authentication | This parameter specifies the type of authentication that the Presence Engine uses to establish a connection with the Exchange
                                                         Server. When set to "Auto," the Presence Engine negotiates NTLMv2 first and falls back to Basic Authentication only if NTLMv2
                                                         negotiation fails. NTLMv1 is not negotiated in FIPS mode. When set to "Basic Only," the Presence Engine always uses Basic
                                                         Authentication, even if the Exchange Server is configured to allow both NTLM and Basic. This parameter applies only in FIPS
                                                         mode. Changing this parameter requires you to restart the Cisco Presence Engine. The default value is Auto. |

| Step 1 | From Cisco Unified IM and Presence Serviceability, choose Tools > Control Center - Feature Services . |
|---|---|
| Step 2 | From the Server drop-down, choose the IM and Presence server and click Go . |
| Step 3 | Under IM and Presence Services , select Cisco Presence Engine and click Restart . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add Calendar Integration to a Feature Group Template | Assign calendaring to a feature group template. |
| Step 2 | Add Feature Group Template to LDAP Sync | Assign your calendaring-enabled feature group template to an LDAP directory sync and complete a sync. |

| Note | You can only add or edit feature group template settings for an LDAP directory that has not yet been synced. If the directory
                                                is already synced, use Enable Calendar Integrations by Bulk instead. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose User Management > User Phone/Add > Feature Group Template . |
|---|---|
| Step 2 | Complete one of the following steps: Click Add New to create a new template. Click Find and select an existing template |
| Step 3 | Check the Enable User for Unified CM IM and Presence check box |
| Step 4 | Check the Include meeting information in Presence check box |
| Step 5 | Complete the remaining fields in the Feature Group Template configuration window. For help with the fields and their settings, see the online help. |
| Step 6 | Click Save . |

| Note | You can only add a feature group template to an LDAP directory that has not yet been synced. If the directory is already synced,
                                                use Enable Calendar Integrations by Bulk instead. |
|---|---|

| Step 1 | From Cisco Unified CM Administration choose System > LDAP > LDAP Directory . |
|---|---|
| Step 2 | Click Find and select an existing LDAP
                                             Directory. |
| Step 3 | From the Feature Group Template drop-down menu,
                                             select the calendaring-enabled feature group template that you
                                             created in the previous task. |
| Step 4 | Complete the remaining fields in the LDAP
                                                Directory window. For help with the fields and their settings, see the online help. |
| Step 5 | Click Save . |
| Step 6 | Click Perform Full Sync Now . |

| Note | Enabling Calendar Integration via the Bulk Administration tool consumes significant system resources. This operation may affect
                                             system performance and user experience. We recommend that you schedule this operation during off-business hours to minimize
                                             disruption and maintain optimal system performance. |
|---|---|

| Step 1 | On a Cisco
                                             				Unified Communications Manager node, log in to the Cisco Unified CM
                                             			 Administration user interface. |
|---|---|
| Step 2 | Enabling
                                          			 calendar integrations in bulk can be performed from the following windows: Bulk
                                                      						Administration > Users > Insert Users . Bulk
                                                      						Administration > Users > Update Users > Query . Bulk
                                                      						Administration > Users > Update Users > Custom
                                                      						File . Note For information on the different types of update options, refer to the Bulk Administration Guide for Cisco Unified Communications Manager . | Note | For information on the different types of update options, refer to the Bulk Administration Guide for Cisco Unified Communications Manager . |
| Note | For information on the different types of update options, refer to the Bulk Administration Guide for Cisco Unified Communications Manager . |
| Step 3 | For all end users for whom you want to enable calendar integration, make sure that the following end user configuration options
                                          are checked: Enable User for Unified CM IM and Presence Include meeting information in Presence |
| Step 4 | If you are updating from a csv file, in the
                                          			 appropriate Users area, choose a File Name. Note Click View
                                                         				  Sample File for the correct file format. | Note | Click View
                                                         				  Sample File for the correct file format. |
| Note | Click View
                                                         				  Sample File for the correct file format. |
| Step 5 | Click Run
                                             				Immediately or Run
                                             				Later . |
| Step 6 | Click Submit . |

| Note | For information on the different types of update options, refer to the Bulk Administration Guide for Cisco Unified Communications Manager . |
|---|---|

| Note | Click View
                                                         				  Sample File for the correct file format. |
|---|---|

| Step 1 | Log in to
                                          			 the Cisco Unified CM Administration user interface. |
|---|---|
| Step 2 | Choose User
                                                				  Management > End User . |
| Step 3 | Click Find and select an end user. |
| Step 4 | Check the Enable User for Unified CM IM and Presence check box. |
| Step 5 | Check the Include meeting information in presence check box. |
| Step 6 | Click Save . |