---
doc_id: www-cisco-com-c-en-us-td-docs-solutions-cvd-collaboration-hybrid-12x-hybcvd-calendar-html-b9b0476f23
source_url: https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Collaboration/hybrid/12x/hybcvd/calendar.html
retrieved_at: 2026-08-16T18:25:25.232439+00:00
---

Preferred Architecture for Cisco Webex Hybrid Services, CVD

# Preferred Architecture for Cisco Webex Hybrid Services, CVD

Updated: December 21, 2017

Chapter: Cisco Webex Hybrid Calendar Service

## Chapter: Cisco Webex Hybrid Calendar Service

## Cisco Webex Hybrid Calendar Service

Revised: May 31, 2019

Cisco Webex Hybrid Services enable Webex Teams customers to connect on-premises collaboration services to Webex. Synchronizing enterprise calendar services with the Webex Hybrid Calendar Service for the customer's organization provides a seamless integration with improved end-user experience for managing meeting invitations, content, and communications with participants.

## Overview

The Cisco Webex Hybrid Calendar Service high-level architecture, depicted in Figure 3-1 , enables an organization to integrate their corporate Microsoft Exchange calendar services with Webex through the Expressway-C Connector Host. This integration enables pre-meeting and post-meeting communications and file sharing while providing an enhanced user experience with simplified scheduling and joining for meetings.

Figure 3-1 Cisco Webex Hybrid Calendar Service High-Level Architecture

### Prerequisites

Prior to implementing and deploying Webex Hybrid Calendar Service, perform the following requirements:

- Deploy Microsoft Exchange within the organization with full email and calendaring functionality.

- Deploy Webex Hybrid Directory Service with corporate directory user information synchronized to Webex.

- If the on-premises network is behind a firewall, ensure that outbound HTTPS (port 443) access to the Internet is available.

### Core Components

The core components for Webex Hybrid Calendar Service include:

- Cisco Calendar Connector

- Microsoft Exchange

Note Although Webex Hybrid Calendar Service also supports integration to Microsoft Office 365 or G Suite by Google Cloud, these integrations are not discussed or covered in this PA for Webex Hybrid Services. For information about these integrations, refer to the latest version of the Deployment Guide for Cisco Webex Hybrid Calendar Service , available at https://www.cisco.com/c/en/us/support/unified-communications/spark/products-installation-guides-list.html .

### Key Benefits

Webex Hybrid Calendar Service provides the following benefits:

- Automatic synchronization of users' Microsoft Exchange calendars, including meeting information, to Webex.

- Capability for users to automatically add, schedule, and invite others to Webex Teams meetings.

- Ability to run Cisco Calendar Connector co-resident with other connectors (Management and Call) on the Cisco Expressway-C Connector Host for maximum deployment flexibility.

- HTTPS outbound connection from the enterprise to Webex on standard port 443, which is typically allowed by organizations and thus should not require configuration to open ports on the firewall. The organization’s existing HTTP proxy may also be leveraged as required.

## Architecture

Figure 3-2 shows the Webex Hybrid Calendar Service integration to the enterprise calendar. This integration relies on the Cisco Calendar Connectors (residing on the Expressway-C Connector Hosts), which are co-located in the central site with the Microsoft Exchange environment. Cisco Calendar Connector is deployed on two Expressway-C Connector Hosts for redundancy and high availability.

Figure 3-2 Architecture for the Integration of Webex Hybrid Calendar Service with the Enterprise Calendar

Cisco Calendar Connector relies on Microsoft Exchange Web Services (EWS) to pull calendar information from Microsoft Exchange based on the @webex and @meet notations in the calendar invitations. Calendar Connector uses HTTPS to push user information to the organization's calendar service in Webex.

The Calendar Connector service provides the following capabilities for creating calendar meeting invitations:

- Webex Teams meeting and automatic space creation with @meet

With this capability a Webex Teams meeting is scheduled and a Webex Teams space is created when the user generates a meeting invitation from their Microsoft Outlook calendar with the @meet notation.

When the @meet keyword is specified in the location field of the meeting invitation, Calendar Connector and the cloud calendar service create a Webex Teams meeting and a Webex Teams space with a name that matches the invitation subject. All users in the calendar invitation are not only invited to the meeting but they are also added to the Webex Teams space. The meeting information is also contained inside the Webex Teams space.

This facilitates collaboration and allows the meeting organizer and attendees to communicate and share material prior to, during, and even after the meeting. If a calendar invitation includes a distribution list, users on the distribution list will not be added to the Webex Teams space automatically; however, they will receive the meeting invitation.

Note While the previous @spark keyword notation still works today, it will eventually be removed. Therefore, we recommend that organizations begin using the @meet keyword instead.

- Webex Personal Room meeting scheduling with @webex

With this capability a Webex Personal Room meeting is added when the user generates a meeting invitation from their Microsoft Outlook calendar with the @webex notation.

When the @webex keyword is specified in the location field of a Microsoft Outlook calendar invitation, Calendar Connector automatically populates the invitation with the user's Webex Personal Room meeting information.

For more information regarding the Calendar Connector @ keyword , refer to the Calendar Connector Release Notes , available at https://collaborationhelp.cisco.com/ .

Hybrid Calendar Service integration also enables synchronization of users' Microsoft Exchange enterprise calendar with their Webex Teams application calendar and meeting list and sharing of users' out-of-office status from Microsoft Outlook with Cisco Webex.

### Role of Cisco Expressway-C Connector Host

The Cisco Expressway-C Connector Host registers to Webex and hosts various cloud connector micro-services, including the Cisco Calendar Connector. Expressway-C Connector Hosts are deployed within the enterprise boundary and communicate with Webex using HTTPS. Multiple cloud connectors may reside on the same Expressway-C Connector Host.

### Role of Cisco Calendar Connector

Cloud connectors are small pieces of software that enable cloud service integrations. These connectors reside on the Expressway-C Connector Host and are downloaded, installed, and updated from Webex. Administrators manage cloud connectors from the Webex Control Hub web-portal.

The Cisco Calendar Connector serves as the intermediary between the enterprise Microsoft Exchange server or environment and Webex. The Calendar Connector communicates with the Exchange server using Exchange Web Services (EWS) and with Webex using HTTPS. Calendar Connector enables users to add meeting invitations to their Webex Teams application calendar and dynamically create Webex Teams spaces when scheduling meetings using Microsoft Outlook (application or web-based).

### Role of Microsoft Exchange

Microsoft Exchange is the enterprise email and calendaring application. Users maintain and update their calendars as appropriate. Any updates to user calendars are propagated to the Cisco Calendar Connector using EWS and leveraging an impersonation service account to access and pull users' calendar information.

## Deployment Overview

Figure 3-3 shows the high-level steps required for deploying Webex Hybrid Calendar Service. Virtual machines based on the Cisco Expressway-C open virtual appliance (OVA) template are created and deployed in the enterprise data center (step 1). (Alternatively, you can deploy a hardware appliance.) After deploy the virtual machines, from the Webex Control Hub ( https://admin.webex.com ) register the Expressway-C Connector Host to Webex to automatically download cloud connector software (step 2). Next, set up impersonation for the Calendar Connector service user account and a throttling policy on Microsoft Exchange (step 3). On the Expressway-C Connector Host configure the connection to Microsoft Exchange and the Webex integration details, and enable the Calendar Connector service on Expressway-C (step 4). Calendar invitations including the @meet or @webex notation are pushed from Microsoft Exchange using Exchange Web Services (step 4A) and in turn propagated by HTTPS to Webex Hybrid Calendar Service (step 4B). Then provision enterprise users for Webex Hybrid Calendar Service using the Webex Control Hub (step 5).

Figure 3-3 Webex Hybrid Calendar Service Deployment Overview

### High Availability

As shown in Figure 3-4 , two Cisco Expressway-C Connector Hosts are deployed. These connector hosts are Cisco Expressway-C virtual machines (VMs) and are deployed on separate hosts in separate buildings or data centers to provide high availability and redundancy.

Expressway-C Connector Hosts are clustered in an active/active pair, and each host runs the Calendar Connector micro-service. These Calendar Connectors are capable of synchronizing calendar meeting invitations and updates between the user's enterprise calendar and Webex.

Figure 3-4 Webex Hybrid Calendar Service High Availability

In addition to Cisco Calendar Connector and Expressway-C Connector Host high availability considerations, also consider providing redundancy for other aspects of the integration such as the Microsoft Exchange services (EWS), connectivity to Webex (HTTPS), and availability of cloud services.

Microsoft Exchange should be deployed in a redundant fashion and should leverage network load balancing as required. Consult Microsoft product documentation for information on Microsoft Exchange high availability.

Highly available network connectivity to the Internet is also required to ensure that Webex services are reachable from the enterprise. We recommend redundant physical Internet connections, preferably from different providers.

Webex services are highly available because those services and components are deployed across multiple physical data centers on elastic compute platforms.

### Scalability

The primary sizing and scalability considerations for Webex Hybrid Calendar Service are the capacity of the Expressway-C Connector Host and of Microsoft Exchange.

User capacity of the Calendar Connector on the Expressway-C Connector Host depends on the following factors:

- Expressway-C Connector Host size — Small, medium, or large OVA or the Cisco Expressway CE appliance (for example, CE1200).

- Calendar Connector deployment type — Standalone on the connector host or co-resident with other connectors

- Non- connector operations and functions (for example, hybrid calling media and signaling firewall traversal or business-to-business calling) — Co-resident with the Calendar Connector or handled by other Expressway nodes

From the perspective of Microsoft Exchange, the Calendar Connector increases the CPU usage and load on the Exchange servers. The impact on the Exchange environment depends on:

- The size and type of Exchange deployment

- The expected number of @webex and @meet meetings per user per hour

- The number of configured Exchange users

- The size of each user's calendar

Knowing and understanding these aspects for your deployment is important for sizing Webex Hybrid Calendar Service appropriately.

For more information on Webex Hybrid Calendar Service scaling, see the chapter on Sizing Cisco Webex Hybrid Services .

## Webex Hybrid Calendar Service Deployment Process

Webex Hybrid Calendar Service requires the deployment of the Cisco Expressway-C Connector Host, installation of the Calendar Connector, and configuration of Microsoft Exchange and the Cisco Expressway-C Connector Host for calendar integration between the on-premises enterprise calendar service and the organization's Webex calendar service.

Note This section presents high-level guidance for deploying Webex Hybrid Calendar Service. This guidance should be used in conjunction with the detailed instructions provided in the latest version of the Deployment Guide for Cisco Webex Hybrid Calendar Service , available at https://www.cisco.com/c/en/us/support/unified-communications/spark/products-installation-guides-list.html .

The deployment of Webex Hybrid Calendar Service starts with installation of the Cisco Expressway-C Connector Host followed by deployment and initial configuration of Cisco Calendar Connector and the calendar integration. To deploy Webex Hybrid Calendar Service, perform the following tasks in the order listed here:

### 1. Download and deploy the Cisco Expressway-C Connector Host OVA template.

The Cisco Calendar Connectors run on Cisco Expressway-C Connector Hosts. The Cisco Expressway-C Connector Host is simply a regular Expressway-C server enabled for hybrid services. Download the Cisco Expressway OVA template from https://www.cisco.com/ , then deploy the OVA template on two separate VMware hosts. Alternatively, use two Cisco Expressway hardware appliances (for example, the Cisco Expressway CE1200 appliance).

When deploying the OVA template, select the appropriate Expressway deployment configuration size (for example, Medium) based on the size of your deployment. For more information about Expressway-C Connector Host sizing, refer to the Scalability information earlier in this chapter and the chapter on Sizing Cisco Webex Hybrid Services .

Note The large deployment OVA configuration is not supported on Cisco Business Edition 7000.

For information about the specific Cisco Expressway-C and Microsoft Exchange versions supported for Webex Hybrid Calendar Service, refer to the latest version of the Deployment Guide for Cisco Webex Hybrid Calendar Service , available at

https://www.cisco.com/c/en/us/support/unified-communications/spark/products-installation-guides-list.html

Once the virtual machines (VMs) or appliances have been deployed, power on and complete the initial installation wizard to set system account passwords (for example, administrator password), network information (for example, IP address, default gateway, and so forth), and basic services (for example, SSH and web) at each server console.

Next, navigate to the web interface of each Expressway-C server (for example, https://us-expc-connector1/ and https://us-expc-connector2 ), login, and on the subsequent Service Setup Wizard page ensure the series is set to Expressway and the type is set to Expressway-C . Click the box beside Cisco Webex Hybrid Services to enable hybrid services and service connectors, and click Continue to save the service selection and bring up the system Overview page.

Next, create an Expressway cluster of the Expressway-C Connector Hosts. Select one of the Expressway-C servers as the master Expressway-C Connector Host cluster node. Navigate to System > Clustering to assign the Expressway-C Connector Host cluster fully qualified domain name (FQDN) (for example, us-expc-connector1.ent-pa.com), and specify the IP address of this host as the peer 1 or cluster master peer address. This FQDN is used to register the master peer to Webex, and additional cluster peers automatically register once the master registers.

To add the second Expressway -C Connector Host to the cluster, configure the second host’s IP address as the peer 2 address on the System > Clustering page of the primary Expressway-C Connector Host. Then replicate the same System > Clustering page configuration on the second Expressway-C Connector Host.

The Expressway-C Connector Hosts do not require release or feature keys to use Webex Hybrid Services. If you see an alarm regarding a system release key, you can safely acknowledge to remove it from the web interface.

For more information and configuration details on Cisco Expressway clustering, refer to latest version of the Cisco Expressway Cluster Creation and Maintenance Deployment Guide , available at

https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html

### 2. Register the Expressway-C Connector Hosts to Webex using the Webex Control Hub.

To register the Expressway-C Connector Hosts to Webex and begin to use hybrid connectors, log into the Webex Control Hub at https://admin.webex.com using your Webex organization’s administrator credentials. Then perform the configuration tasks and settings shown in Table 3-1 .

Table 3-1 Cisco Expressway-C Connector Host Cloud Registration

Expressway-C Connector Hosts may be assigned to resource groups in Webex to simplify management of multiple Expressway-C Connector hosts and/or clusters, particularly in global and multi-regional deployments.

Navigate to Services > On-Premises Resources ( under the Hybrid Services area) and select All Resources .

Click the settings gear icon next to Expressway and select Create new resource group .

(Refer to the Configuration Settings and Steps column for the configuration value.)

Click Done to save.

Enter the name of the resource group: US Hybrid Services

The Expressway-C Connector Host primary server must be defined in Webex in order to register and access connector software and services.

Navigate to Services > On-Premises Resources (under the Hybrid Services area) and select All Resources .

Click Add Resource . On the following screens, make selections as shown in the Configuration Settings and Steps column, and click Next to save and move to the next screen.

1. Click Expressway to add a resource for Hybrid Calendar and/or Call service.

2. Click Hybrid Calendar Service . 1

3. Enter the FQDN of the master Expressway-C Connector Host cluster node: us-expc-connector1.ent-pa.com

4. Enter the display name for this Expressway-C Connector Host cluster: us-expc-connectors

5. Click Yes, assign now , and select: US Hybrid Services

The final step of adding the Expressway-C Connector Host resource is to complete the cloud registration.

On the final screen of the add resource wizard, click Go to Expressway to launch the web interface of the Expressway-C Connector Host cluster master peer (for example, https://us-expc-connector1.ent-pa.com/).

(Refer to the Configuration Settings and Steps column for the configuration values.)

1. Login with Expressway administrator credentials.

2. Click I want Cisco to manage the Expressway CA certificates required for this trust in order to automatically add the Webex CA certificates to the Expressway-C trust list.

3. Click Register to initiate cloud registration.

4. On redirect to the Webex Control Hub, click Allow to complete the registration.

1. If you plan to deploy Webex Hybrid Call Service, then you may also click Hybrid Call Service to use this connector host resource for Webex Hybrid Call Service as well.

Once registration of the Expressway-C Connector Host to Webex completes, the Management Connector software offers to automatically upgrade itself if required, and then it begins downloading and installing the Calendar Connector software from the cloud onto the Expressway-C Connector Host.

You do not need to register the second Expressway-C Connector Host to Webex; it will automatically register when the master peer registers, and it will automatically upgrade and/or install the same connectors.

### 3. Prepare Microsoft Exchange for Webex Hybrid Calendar Service integration.

After the Expressway-C Connector Host nodes are registered to Webex, the next step is to prepare Microsoft Exchange for the Webex Hybrid Calendar Service integration. Perform the following tasks on Microsoft Exchange in order to set up Webex Hybrid Calendar Service integration:

Add the impersonation role to the service account for the Calendar Connector Service.

Calendar Connector integrates with Microsoft Exchange through an impersonation account. The application impersonation management role in Microsoft Exchange enables applications to impersonate users in an organization in order to perform tasks on behalf of the user. The application impersonation role is configured in Microsoft Exchange.

Navigate to the Microsoft Exchange server and enter the following command in the Exchange Management Shell:

Where <RoleName> is the name of the new role (for example, CalendarConnector) and <UserName> is the name of the service account the impersonation role is being assigned to in the format domain \ name (for example, ENT-PA\CalendarConnectorAcct).

Note The impersonation account does not require administrator permissions, but it must have a mailbox.

Configure a throttling policy and apply it to the impersonation account.

As with any service or application entity that accesses Microsoft Exchange, it is a good idea to configure a throttling policy to ensure that Microsoft Exchange is able to handle the added load of the service account and can continue to operate and respond as normal.

Return to the Exchange Management Shell and enter the following command:

Where <ThrottlePolicy> is the name of the new role (for example, CalendarConnectorPolicy).

Next assign the new throttling policy to the impersonation account with the following command:

Where <ImpersonationAcct> is the name of the service account (for example, CalendarConnectorAcct), and <ThrottlePolicy > is the name of the throttle policy (for example, CalendarConnectorPolicy) created in the previous step.

### 4. Configure the Expressway-C Connector Hosts for Webex Hybrid Calendar Service integration.

With the Expressway-C Connector Hosts registered to Webex and with the Microsoft Exchange environment prepared, the next step is to complete the Webex Hybrid Calendar Service integration configuration.

Return to the Expressway-C Connector Host master peer web interface (for example, https://us-expc-connector1/) and log in with the administrator credentials. Then perform the configuration tasks and settings shown in Table 3-2 .

Note In order to enable TLS verification for the link to Microsoft Exchange (TLS Verfiy Mode = On ), the Expressway-C server host must be able to validate the certificate received from Microsoft Exchange. Prior to proceeding, ensure that the root certificate of the Certificate Authority (CA) that signed the Microsoft Exchange server certificate has been appended to the Expressway-C server trust list. Failure to import the CA root certificate will result in TLS verification failure and prevent connection between Expressway-C and the Microsoft Exchange server. The CA root certificate must be appended to the server trust list for each Expressway-C node in the cluster.

Table 3-2 Cisco Expressway-C Connector Host Configuration Tasks

Create the connection between Expressway-C Connector Host and Microsoft Exchange.

Navigate to Applications > Hybrid Services > Calendar Service > Microsoft Exchange Configuration .

Click New to begin adding Microsoft Exchange configuration information.

(Refer to the Settings and Example Values columns for configuration values.)

Click Add to create the connection.

Service Account Credentials

CalendarConnectorAcct@ent-pa.com (Format: username @ domain )

Display Name

us-exchange-1

Type

Exchange On-Premises

Need Proxy for Configuration

No

(Enter Yes if web proxy is required to reach Microsoft Exchange.)

Enable this Exchange Server

Yes

Authentication Type

NTLM

TLS Verify Mode

On

Autodiscovery

Use Active Directory

Configure additional Active Directory information as required:

- Active Directory Domain (for example, ent-pa.com )

- Query Mode (for example, ldaps )

- LDAP TLS Verify Mode (for example, On )

Add Webex information to facilitate use of Webex personal meeting rooms (PMRs) when using @webex in meeting invitations.

Navigate to Applications > Hybrid Services > Calendar Service > Cisco Webex Configuration .

Click New to begin adding Webex configuration information.

(Refer to the Settings and Example Values columns for configuration values.)

Click Save to complete the configuration.

WebEx Fully Qualified Site Name

ent-pa.webex.com

WebEx account credentials

<account username @ domain / password>

Default Site

Yes

After completing the configuration tasks in Table 3-2 , start the Calendar Connector service to complete the Calendar Connector integration. Navigate to Applications > Hybrid Services > Connector Management and select the Calendar Connector node. Select Enable from the drop-down list, and then click Save to save the configuration. Make sure the Calendar Connector comes up and begins to run (status says Running ).

### 5. Provision enterprise users for Webex Hybrid Calendar Service by using the Webex Control Hub.

After you have enabled and configured Webex Hybrid Calendar Service, you can provision users for the Webex Hybrid Calendar Service. From a web browser, use your Webex organization’s administrator credentials to log into the Webex Control Hub at https://admin.webex.com .

Provision users individually or in bulk for Webex Hybrid Calendar Service by navigating to Users and selecting individual users or by clicking Manage Users to provision groups of users.

To enable large numbers of users in bulk for Webex Hybrid Calendar Service, choose either Export and modify users with a CSV file or Modify all synchronized users . To enable Webex Hybrid Calendar Service for all users, select Modify all synchronized users and click Next . If prompted, acknowledge that users will automatically be sent an email by clicking Next . On the next screen, wait for the system to synchronize the list of users from the latest directory synchronization agreement, and then click Next .

On the subsequent screen, provision all users for Webex Hybrid Calendar Service by selecting Calendar Service and clicking Next to start the update of user accounts. Once the update is complete, users can begin to use Webex Hybrid Calendar Service.

Note Valid licenses are required to add and enable licensed services and features.

| Expressway-C Connector Host Cloud Registration Tasks and Descriptions | Navigation | Configuration Settings and Steps |
|---|---|---|
| Create Expressway Resource Groups. Expressway-C Connector Hosts may be assigned to resource groups in Webex to simplify management of multiple Expressway-C Connector hosts and/or clusters, particularly in global and multi-regional deployments. | Navigate to Services > On-Premises Resources ( under the Hybrid Services area) and select All Resources . Click the settings gear icon next to Expressway and select Create new resource group . (Refer to the Configuration Settings and Steps column for the configuration value.) Click Done to save. | Enter the name of the resource group: US Hybrid Services |
| Add the Expressway-C Connector Host master peer as an Expressway resource. The Expressway-C Connector Host primary server must be defined in Webex in order to register and access connector software and services. | Navigate to Services > On-Premises Resources (under the Hybrid Services area) and select All Resources . Click Add Resource . On the following screens, make selections as shown in the Configuration Settings and Steps column, and click Next to save and move to the next screen. | 1. Click Expressway to add a resource for Hybrid Calendar and/or Call service. 2. Click Hybrid Calendar Service . 1 3. Enter the FQDN of the master Expressway-C Connector Host cluster node: us-expc-connector1.ent-pa.com 4. Enter the display name for this Expressway-C Connector Host cluster: us-expc-connectors 5. Click Yes, assign now , and select: US Hybrid Services |
| Register the Expressway-C Connector Host to Webex. The final step of adding the Expressway-C Connector Host resource is to complete the cloud registration. | On the final screen of the add resource wizard, click Go to Expressway to launch the web interface of the Expressway-C Connector Host cluster master peer (for example, https://us-expc-connector1.ent-pa.com/). (Refer to the Configuration Settings and Steps column for the configuration values.) | 1. Login with Expressway administrator credentials. 2. Click I want Cisco to manage the Expressway CA certificates required for this trust in order to automatically add the Webex CA certificates to the Expressway-C trust list. 3. Click Register to initiate cloud registration. 4. On redirect to the Webex Control Hub, click Allow to complete the registration. |

| 1. If you plan to deploy Webex Hybrid Call Service, then you may also click Hybrid Call Service to use this connector host resource for Webex Hybrid Call Service as well. |
|---|

| Configuration Tasks | Settings | Example Values |
|---|---|---|
| Configure the Microsoft Exchange Connection. Create the connection between Expressway-C Connector Host and Microsoft Exchange. Navigate to Applications > Hybrid Services > Calendar Service > Microsoft Exchange Configuration . Click New to begin adding Microsoft Exchange configuration information. (Refer to the Settings and Example Values columns for configuration values.) Click Add to create the connection. | Service Account Credentials | CalendarConnectorAcct@ent-pa.com (Format: username @ domain ) |
| Display Name | us-exchange-1 |
| Type | Exchange On-Premises |
| Need Proxy for Configuration | No (Enter Yes if web proxy is required to reach Microsoft Exchange.) |
| Enable this Exchange Server | Yes |
| Authentication Type | NTLM |
| TLS Verify Mode | On |
| Autodiscovery | Use Active Directory Configure additional Active Directory information as required: Active Directory Domain (for example, ent-pa.com ) Query Mode (for example, ldaps ) LDAP TLS Verify Mode (for example, On ) |
| Configure Webex Site Settings. Add Webex information to facilitate use of Webex personal meeting rooms (PMRs) when using @webex in meeting invitations. Navigate to Applications > Hybrid Services > Calendar Service > Cisco Webex Configuration . Click New to begin adding Webex configuration information. (Refer to the Settings and Example Values columns for configuration values.) Click Save to complete the configuration. | WebEx Fully Qualified Site Name | ent-pa.webex.com |
| WebEx account credentials | <account username @ domain / password> |
| Default Site | Yes |