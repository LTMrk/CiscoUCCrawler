---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-operation-guide-chcs-b-hcs-smart-licensing-operational-2a696dbb56
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/Operation_Guide/chcs_b_hcs-smart-licensing-operational-guide/chcs_b_hcs-smart-licensing-operational-guide_chapter_010.html
retrieved_at: 2026-09-01T20:56:10.260440+00:00
---

Cisco Hosted Collaboration Solution Smart Licensing Operation Guide, Release 12.5

# Cisco Hosted Collaboration Solution Smart Licensing Operation Guide, Release 12.5

Updated: April 23, 2020

Chapter: Onboard Customer per Cluster

## Chapter: Onboard Customer per Cluster

# Onboard Customer per Cluster

## Provisioning Workflow for Smart Licensing

### Before you begin

Read Cisco Smart Software Manager

Configure CSSM as described in Initial One Time Setup in CSSM for Smart Licensing

Configure Satellite as described in Initial One Time Setup in CSSM on-prem for Smart Licensing

View Smart Account Summary

Configure Smart Account

Virtual Account Summary

Assign and Unassign a cluster to Virtual Account

HCM-F periodically syncs with CSSM and Satellite .

### What to do next

Verify the Status column for the job status in the HCM-F interface. Navigate to ( Infrastructure Manager > Administration > Jobs ) and see the Smart Account in the Job Entity column. If a job fails, hover over the information icon and the Job Details window pops up. Check the status information and recommended action.

### Create a Smart Account

Skip this section if you already have a Smart Account. Otherwise, you can continue to the next step.

Log in to software.cisco.com using your Cisco.com ID (CCO ID).

Select Request a Smart Account under the Administration section.

Follow the steps to create a Smart Account for your organization.

#### Configure Smart Account Access

From the side menu, select Infrastructure Manager > Smart Licensing > Configure Smart Account .

Click Add New .

Complete the fields in the Configure Smart Account
                                                Access page.

Fields

Description

Smart Account Domain Name

Domain name of smart account.

Client ID

ID of the smart account

Client Secret

Secret (password) of the smart account

Smart Account Name

Name of the smart account.

This is an optional field.

Complete the fields in the Configure Smart Account
                                                Access page.

In the Transport Settings enter the following
                                                   fields:

Fields

Description

Transport Mode

Select the transport mode to access CSSM. The
                                                                  options are:

Proxy: Cisco products send usage information
                                                                        through a proxy server.

Satellite: Cisco products are installed on
                                                                        premise and the connectivity to Cisco is online or
                                                                        offline.

Direct: Cisco products send usage information
                                                                        directly.

Configure the transport mode settings as follows:

Fields

Description

Authentication Gateway

Displays the authentication gateway.

CSSM Server

Displays the CSSM server.

Smart Account Domain Name

Domain name of smart account.

Client ID

ID of the smart account

Client Secret

Secret (password) of the smart account

Fields

Description

Proxy Hostname/IP

Enter the proxy hostname or IP address.

When you set the transport mode as proxy, the
                                                                              setting connects the HCM-F to the CSSM through
                                                                              proxy but does not register the customer and
                                                                              cluster with the CSSM.

To register the cluster and customer to the
                                                                              CSSM, add the proxy values at the customer and
                                                                              cluster level to connect to the CSSM through
                                                                              proxy, otherwise it will connect through direct
                                                                              mode, by default.

For more information about setting the proxy at
                                                                  customer and cluster level, see Add
                                                                     Customer , and Add Cluster at Hosted Collaboration Mediation Fulfillment
                                                                     Install and Configure Guide .

Proxy Port

Enter the proxy port.

Authentication Gateway

Displays the authentication gateway.

Enable Proxy Authentication

HCM-F uses the proxy authentication defined at
                                                                  the customer and cluster level to synchronize with
                                                                  CSSM.

Proxy Username- Enter the proxy username.

Proxy Password- Enter the proxy password.

CSSM Server

Displays the CSSM server.

Smart Account Domain Name

Domain name of smart account.

Client ID

ID of the smart account

Client Secret

Secret (password) of the smart account

Fields

Description

Satellite Hostname

Enter the satellite hostname.

Satellite Port

Enter the satellite port.

Registration URL

Enter the registration URL.

Refer to the links below for the registration
                                                                  URLs for their respective satellite versions:

Satellite version 6.3.0 -
                                                                        https://<SATELLITE_IP_ADDRESS>/Transportgateway/services/DeviceRequestHandler

Satellite version 7.2.0 -

HCM-F V12.5SU2 and above -
                                                                              https://<SATELLITE_FQDN>/SmartTransport

below HCM-F V12.5SU2 -
                                                                              https://<SATELLITE_FQDN>/Transportgateway/services/DeviceRequestHandler

Satellite version 8.X -
                                                                        https://<SATELLITE_FQDN>/SmartTransport

Token URL

Enter the Token URL.

Refer to the links below for the Token URLs for
                                                                  their respective satellite versions:

Satellite version 6.3.0 -
                                                                        https://<SATELLITE_IP_ADDRESS>:8443/backend/oauth/token

Satellite version 7.2.0 -
                                                                        https://<SATELLITE_FQDN>:8443/backend/oauth/token

Satellite version 8.X -
                                                                        https://<SATELLITE_FQDN>:8443/backend/oauth/token

Local Account

Domain Name

Domain name of the satellite smart account.

This field is displayed only when you select
                                                                  Satellite as the transport mode.

Client ID

ID of the smart account

Client Secret

Secret (password) of the smart account

If the cluster is already assigned to a virtual account, and you want
                                                      to change the transport mode settings, the cluster has to be
                                                      unassigned from the virtual account, change the transport mode
                                                      settings, and then reassign the clusters to the virtual account.

Enable the Operational Licenses to autoregister the clusters to the specified
                                             virtual account.

For more information about Operational Licenses and Auto Registration of
                                                clusters, see Auto-registration of Clusters Using Direct or Proxy Mode

Click Save .

#### Set Transport Mode

HCM-F and UC application clusters support the following transport modes for license consumption and reporting:

Proxy

Direct

From the side menu, select Infrastructure Manager > Smart Licensing > Transport Mode .

Select the mode from the Transport Mode drop-down list.

If transport mode is Direct, Authentication Gateway and CSSM Server information is displayed by default.

When Smart account is provisioned with client credentials (Client ID and Client Secret) in HCM-F, the HCM-F authenticates
                                                                  with the Cisco Authentication Gateway with client credentials. HCM-F gets the access token from Cisco Authentication Gateway
                                                                  for communicating with CSSM.

If transport mode is Proxy, enter the proxy server and the proxy server port details.

Authentication Gateway and CSSM Server information is displayed by default.

Proxy is the recommended option. Validate that HCMF and UC applications are connected to CSSM through the proxy.

#### View Smart Account
                              Summary

From the side menu, select Infrastructure Manager > Smart Licensing > Smart Account Summary .

The Smart Account Summary page shows the following
                                             information on smart accounts:

Fields

Description

Name

Name of smart account

Domain

Domain name of smart account

Type

Type of smart account

Status

Status of smart account: active or inactive

VA#

Number of virtual account associated with the smart
                                                            account

Last SyncUp

Last sync up time of smart account

Alerts

Shows the alerts

To see the virtual accounts associated with the smart account, click the
                                                            smart account name from the list. The Virtual Accounts page shows the
                                                            list of virtual accounts.

To see the virtual accounts associated with the smart account, click the
                                                            virtual account name from the list. The Virtual Accounts page shows the
                                                            list of virtual accounts.

Click Add New to configure a new smart account.

Click the Smart Account Name to edit the existing Smart Account.

### Create Virtual Account

Login to software.cisco.com using your Cisco.com ID (CCO ID).

Select Manage Smart Account under Administration section

Select the Virtual Accounts tab and then select New Virtual Account... .

Create two Virtual Accounts and name them as:

- VA–HCS-Ordered

- VA–HCS-Operational

Ensure to add the following two users in Cisco HCS Operations Team as Virtual Account User.

alicchan@cisco.com

trgilman@cisco.com

#### Virtual Account Summary

Virtual Account Summary window displays the list of Virtual accounts. Once a virtual account is selected, you can do the following:

Admin can change the license mode for any virtual account.

If no mode was present earlier, then the license mode could be set.

If no cluster is assigned to the VA, then you can change the mode of the VA.

If a cluster is assigned to the VA, then you cannot change the mode of the VA (It requires the clusters to be unassigned from
                                          the VA before changing the VA license mode). In this scenario, the license mode is noneditable. Hover over the tooltip for
                                          the VA to get the information. If the cluster is assigned to the VA, the tooltip states that the mode cannot be changed as
                                          clusters are associated with the VA. Once the clusters are unassigned, you can edit the license mode of VA.

The license mode is not applicable for the virtual account in CSSM. License mode is applicable only on HCM-F. It enables to
                                          identify the mode it should set the UC application.

From the side menu, select Infrastructure Manager > Smart Licensing > Virtual Account Summary .

The Virtual Accounts page shows the list of virtual accounts, and the following information on virtual accounts:

Fields

Description

Name

Name of virtual account

SA Name

Name of smart account

Access Level

Specifies the access level assigned to the virtual account

Clusters #

Number of clusters assigned to the virtual account

Customer#

Name of customers assigned to the virtual account

#### Assign and Unassign a Cluster to Virtual Account

If auto registration is enabled then the partner does not need to manually register or unregister unless they need to register
                                    clusters to different license repositories, such as, one smart account and one satellite server or two or more satellite servers.

From the side menu, select Infrastructure Manager > Smart Licensing > Virtual Account Summary .

From the Virtual Accounts page, click a virtual account name.

From the Edit Virtual Account page, select the license mode from the License Mode dropdown.

Click Assign in the Clusters Assigned to Virtual Account section.

You cannot assign the cluster to the virtual account if the license mode for the virtual account is not set. A warning message
                                                                  is displayed asking to add the license mode for the VA.

You cannot change the license mode of a virtual account if a cluster is assigned to the virtual account. In this scenario,
                                                                  unassign the cluster from the virtual account.

From the Assign Cluster to Virtual Account page, select the cluster by checking the check box.

Only clusters higher than 11.x is displayed here.

Click Assign .

To unassign a cluster from the virtual account, select the cluster by checking the check box from the Clusters Assigned to Virtual Account section, and then click Unassign .

To assign or unassign a cluster from the virtual account, use the filter by customer name to filter the clusters.

View the Cluster Summary page to ensure that all the clusters are registered, and if it fails to register then refer to the recommended action.

### Configuring Operational Licenses

You can use operational license to generate reports in HCM-F for the amount-of-licenses that are ordered by the partner and
                                 the amount-of-licenses that are consumed. If you opt for operational license, then you have to create an operational virtual
                                 account in CSSM where Cisco stores all the licenses that the partner consumes. An ordered virtual account is also created
                                 where the licenses ordered by the partners from CCW are stored and are not used by the UC applications. Operational license
                                 can be opted by both Flex and perpetual license user. If you have opted for operational license, the licenses are stored in
                                 the operational virtual account in CSSM.

You can autoregister the clusters if you opt for operational licenses.

If the clusters are registered in satellite, then HCM-F syncs with CSSM using proxy and gets the details of the satellite
                                             operational licenses.

#### Before you begin

You must have a Smart Account, Local Account, and Virtual Account in CSSM and Satellite.

The operational licenses are stored in operational virtual account (va-hcs-operational).

Set up operational licenses for the clusters.

If the clusters are migrated to version 12.5 and later, the Flex Usage Report displays additional values for true forwarding,
                                       licenses consumed, and compliance check.

Fill this smart sheet http://cs.co/HCSPartnerRequestForm to get access to the Operational
                                          Licenses.

Once you receive a confirmation, create the following virtual accounts in CSSM.

#### Task Flow of Operational License Without Satellite Account

User orders licenses from CCW.

For all users ordered licenses, a virtual account is created in CSSM: va-hcs-ordered .

Fill this smart sheet http://cs.co/HCSPartnerRequestForm to get access to the Operational
                                             Licenses.

For more information on the prerequisites, see Configuring Operational Licenses .

Create an operational virtual account in CSSM, where Cisco deposits all the operational licenses that are to be consumed: va-hcs-operations .

Once you have opted for operational license, autoregistration of clusters is possible while you configure a smart account.

HCM-F queries ordered virtual account for licenses that are deposited per Subscription ID.

HCM-F is preconfigured to map Customer to Subscription ID.

HCM-F queries Cisco Unified Communications applications for the license consumption report.

#### Task Flow of Operational License With Satellite Account

User orders licenses from CCW.

For all users ordered licenses, a virtual account is created in CSSM: va-hcs-ordered .

Fill this smart sheet http://cs.co/HCSPartnerRequestForm to get access to the Operational
                                             Licenses.

For more information on the prerequisites, see Configuring Operational Licenses .

Create an operational virtual account in CSSM, where Cisco deposits all the operational licenses that are to be consumed: va-hcs-operations . User has to move the licenses from operations VA in CSSM to satellite VAs.

Autoregistration feature supports only one Satellite account. For using more than one Satellite, user can use the Satellite
                                                on board functionality that is provided by HCM-F.

HCM-F queries ordered virtual account for licenses that are deposited per Subscription ID.

HCM-F is preconfigured to map Customer to Subscription ID.

HCM-F queries Cisco Unified Communications applications for license consumption report.

### View Cluster Summary

From the side menu, select Infrastructure Manager > Smart Licensing > Cluster Summary .

List of Unified Communication clusters with the version 12.5 and later.

List of Expressway E and C clusters with version X12.6 and later that are configured with Smart licensing mode.

Registration of Expressway clusters in HCM-F is at the cluster level whereas for the other applications registration in HCM-F
                                                               is done by node.

Fields

Description

Name

Name of the cluster

Type

Retrieves the type of cluster such as Unified CM, Unity Connection, CER, Expressway-E, Expressway-C from the HCM-F inventory.

Version

Specifies the Cluster version.

Smart Account

Name of the Smart Account that is associated with the virtual account.

Virtual Account

Virtual Account name that the cluster is associated with.

Status

Displays the status of the clusters, if they are registered, unregistered, partially registered or autoregistered to the virtual
                                                         account. For example, if the cluster is autoregistered, then the status is displayed as Autoregistered.

The information icon provides details about the cluster status, description, and the recommended action.

The cluster status is prioritized as follows:

Multiple Virtual Account Registered -Specifies the clusters that are assigned offline using the Expressway user interface,
                                                               where all the nodes are not registered to the same VA. Partial and mutiple VA applies only to Expressway-E and C clusters.

NOTE: For clusters registered as multiple VA registered, you cannot assign/unassign clusters using the HCM-F application.
                                                               Use the Expressway application to assign the multiple VA registered clusters.

Auto Registration Failed - Auto registration of the cluster fails.

Manual Registration Failed - Manual assignment of cluster fails.

Deregistration Failed - Manual unassignment of the cluster fails.

Deregistered - cluster is unassigned manually.

Partially Registered - cluster is partially assigned when:

All nodes of a cluster are not registered.

If one of the node of the cluster is either registered/unregistered

NOTE: Partially Registered status applies only to Expressway E and C clusters.

Auto Registration Inprogress - auto registration of the cluster is in progress.

Auto Deregistration InProgress - Auto deregistration of cluster is in progress.

Auto Registered - cluster is autoregistered to the virtual account.

Manually Registered - cluster is manually assigned to a virtual account.

Deregistered - clusters are not assigned to any virtual account.

NOTE:

Add all the nodes of the Expressway cluster in HCM-F, to register the cluster. If there is a mismatch in the number of Expressway
                                                         cluster nodes that is configured in HCM-F, then the registration fails.

Job Status

The information icon provides the provisioning status of the cluster.

Hover over the information icon for a cluster in the Job Status column to see the job details of the cluster.

Fields

Description

Job Type

Specifies the provisioning status of the cluster.

Entity Type

Specifies the type of the cluster.

Date/Time Initiated

Specifies the data and time when the job was initiated.

Date/Time Completed

Specifies the data and time when the job completed.

Status

Specifies the overall status of the job.

Entity Name

Specifies the entity name of the cluster.

Description

Details of the job.

Status Information

Status of the job

Recommended Action

Describe the action to resolve the issue.

To modify a cluster, select a cluster from the list, and modify the details in the Cluster Summary page.

For more information about the field details in the Cluster Summary page, see Add Cluster section in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide .

If you apply a filter of Type on the Cluster, then the set of keyword values that are allowed for Expressway clusters in Smart
                                                         licensing mode are: core, edge, expressway,expresswayedge, expressway edge,expresswaycore, and expressway core.

#### Edit Virtual Account

From the side menu, select Infrastructure Manager > Smart Licensing > Virtual Account Summary

Select the virtual account to make changes, the Edit Virtual account window displays.

Field

Description

Name

Name of virtual account

Description

Displays a short description of the account

Smart Account Name

Displays the Smart account name.

Domain Name

License Mode

Specifies the license mode that is associated with the cluster.

Commercial Access Level

Specifies the access level that is assigned to the virtual account

Clusters Assigned- Displays the details of all clusters that are associated with the virtual account. Select unassign, to
                                             unassign a cluster for the account. Click Assign, to add a new cluster to the account.

#### Auto-registration of Clusters Using Direct or Proxy Mode

If you enable autoregistration, HCM-F changes the license modes of the UC Applications to HCS mode. Hence, the publisher node
                                                of the clusters which are in enterprise mode reboots and the license mode is changed to HCS mode.

You can assign the clusters to the virtual account manually, however, from HCS 12.5 SU1 release you can auto-assign the clusters
                                    to the operational virtual account. This procedure enables you to autoregister the clusters to the operational virtual account
                                    using the proxy or direct mode.

Autoregistration of clusters is possible for only one Smart Account. If Operational Licenses are enabled for a smart account, and you try to configure a new smart account or satellite account, the Operational Licenses check-box is disabled.

If you have not opted for Operational Licenses, you cannot autoregister the clusters to the operational virtual account.

Configure the proxy settings at customer or cluster level before enabling auto-registration for Proxy mode. For more information,
                                                see Add Cluster in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide .

Navigate to Infrastructure Manager > Smart Licensing > Smart Account Summary . Click Add New to configure the smart accounts.

Select Opted Operational Licenses to register the clusters to the following virtual accounts:

If the Ordered and Operational VAs are unchanged, a job for auto-registration is not triggered. Only way to trigger the job
                                                                  is to disable and enable the auto-registration again as part of smart account configuration update.

If the ordererd and operational VAs are different and valid, it first triggers de-registration job for unassigning the clusters
                                                                  from the old operational VA and then trigger auto-registration job for assigning to the new operational VA.

Any auto-registered cluster can be manually unassigned and re-assigned to different VA. In such case, that cluster is no longer
                                                                  considered as part of the autoregistration process. If at all the cluster has to be part of the auto-registration, then the
                                                                  smart account should be either updated with first disabling and then enabling auto-registration.

Autoregistration of the clusters is possible if any of the following conditions are met:

When the clusters with version 12.5 is installed, the clusters are automatically autoregistered to the operational virtual
                                                      account.

When the clusters are upgraded to 12.5, and you have opted for operational licenses, you can choose to autoregister the clusters
                                                      to the operational virtual account, otherwise they are manually assigned to the virtual accounts.

While configuring the smart account, if you opt for operational licenses and enable autoregistration, any  existing 12.5 cluster
                                                      version is autoregistered.

Following are the cluster assignment to virtual account scenarious:

If...

Then...

You want one of the cluster to be removed from the autoregistered virtual account

You have to unassign the cluster manually from the autoregistered virtual account, and reassign the cluster manually to the
                                                            specific virtual account.

You want one of the cluster to be reassigned to the autoregistered virtual account

You have to unassign the cluster manually from the specific virtual acount, and reassign the cluster manually to the autoregistered
                                                            virtual account.

Any cluster fails to autoregister to the operational virtual account

You can do the following:

An on-demand or auto sync that happens in every 24 hours registers the cluster to the operational virtual account.

You can also disable the autoregistration option and enable it again as part of Smart Account update.

Select Enable Auto Registration of applications (disable if you are using Satellite) option to autoregister the clusters to the operational virtual account in CSSM, while using the Direct and Proxy as the Transport
                                             Mode. De-select the autoregistration option, if you want to autoregister the clusters using the Satellite as the Transport
                                             Mode.

Autoregistration is automatically triggered when:

If any configuration details are wrong during the Smart Account configuration (For example, Proxy hostname, IP address, and
                                                      so on), update the fileds with the right value, then the autoregistration is automatically triggered.

In case of proxy mode, if right proxy details are provided at cluster or customer level as part of the update, autoregistration
                                                      is automatically triggered.

Any of the operations, such as credential change, network address change to a valid value for a cluster as part of the update
                                                      also triggers autoregistration.

#### Autoregistration of Clusters Using Satellite Mode

##### Before you begin

Enabling autoregistration through satellite mode is allowed only if the Operational License is enabled while configuring the
                                    smart account as part of either the Proxy or Direct mode.

Navigate to Infrastructure Manager > Smart Licensing > Smart Account Summary . Click Add New to configure the smart accounts.

Select Satellite as the Transport Mode.

Operational License options must be enabled while configuring smart accounts by using the Proxy or Direct mode.

Select Enable Auto Registration to register the clusters to the operational virtual account.

When you configure a smart account using Satellite as the Transport Mode, the Enable Auto Registration option is enabled. You can provide an operational virtual account name, and the clusters are auto-assigned to the virtual
                                                account in the satellite server.

### HCM-F 12.5 Upgrade Guidelines

Complete the seps in Initial One Time Setup in CSSM for Smart Licensing topic.

Upgrade HCM-F to 12.5(x).

For more information about upgrading HCM-F, see Upgrade HCM-F in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide .

Set the Transport Mode in HCM-F, navigate to Smart Licensing > Transport Mode .

Provision Smart Account in HCM-F.

Configure the Smart Account or Satellite local account, navigate to Smart Licensing > Configure Smart Accounts . For details, see Cisco Hosted Collaboration Solution Smart Licensing Guide .

Configure the Smart Account, navigate to Smart Licensing > Smart Accounts . Click Add New , to configure smart accounts.

For more information, see Configure Smart Account Access .

Once the Smart Account is configured, HCM-F synchronizes with CSSM and Satellite and retrieves all the Virtual Account details to HCM-F in Virtual Account Summary window ( Smart Licensing > Virtual Account Summary ).

Upgrade the UC applications.

License Conversion and Migration to Smart Licensing

Unassign the UC clusters from PLM before you upgrade UC clusters to 12.5(x). Navigate to License Management > License Management Summary .

Upgrade the UC applications.

To upgrade Unified CM and IM and Presence to 12.5(x), see the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service guide

To upgrade Cisco Unity Connection to 12.5(x), see Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Guide .

To upgrade Cisco Emergency Responder (CER) to 12.5(x), see Cisco Emergency Responder Administration Guide

Register the UC applications to Virtual Account.

Update the Cluster Application Version to 12.5(x). Navigate to Cluster Management > Cluster to verify the version. For details, see Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide

If you are using Unified CDM, ensure the cluster application version is 12.5(x). If the version is less than 12.5(x), update
                                                               the cluster application version to 12.5(x).

If you are registering to CSSM by using the proxy mode, then you must set the proxy parameters at the customer and cluster
                                                   level, otherwise the registration fails. For more information about the proxy parameters at cutomer and cluster level, see Add Customer , and Add Cluster sections in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide .

Assign a cluster manually to a Virtual Account , if you have not opted for auto registration .

Assign the License Mode to HCS for a Virtual Account, navigate to Smart Licensing > Virtual Account Summary .

For details, see Assign and Unassign a Cluster to Virtual Account .

Ensure the licenses are present in the VA in CSSM.

To check that the product instances are populated correctly and licenses are consumed, log in to Cisco Software Central .

### Subscription Mapper

HCM-F pulls all the Subscription IDs from CSSM. You can select the customer for each Subscription ID from the Subscription Mapper page. When the Flex Usage report is generated, HCM-F uses this mapping to corelate the order and usage information and calculates
                                 the Compliance and True Forwarding.

HCM-F identifies the license ordered details per customer and performs the true forwarding calculation and compliance check.
                                       For more information about true forwarding calculation, and compliance check, see Request or Download Flex Usage Report .

You can sort by the End date to identify which all subscriptions are about to expire.

To update your order, you can click the subscription number and connect to CCW with the Subscription ID.

#### Before you begin

Smart Account, virtual account, and satellite account should be configured in HCM-F.

HCM-F retrieves Subscription IDs from all the virtual account in CSSM and satellite.

From the side menu, select Infrastructure Manager > Smart Licensing > Subscription Mapper .

The Subscription Mapper page shows the following information:

Fields

Description

Subscription ID

Displays the subscription IDs that are retrieved while HCM-F performs a sync with CSSM and satellite .

License Details

Displays the number of licenses that are consumed by each subscription ID.

Hover over the i icon to see the license details that has the list of license types.

Start Date

Displays the start date of the license type. This is valid only for Flex licenses.

End Date

Displays the end date of the license type. This is valid only for Flex licenses.

For Perpetual licenses Start Date and End date is not valid.

Customer

Displays the name of the customer to which the Subscription ID is mapped.

License Model

Displays the model of the license. The supported options are:  Perpetual, Named User, Named User + Perpetual, or Enterprise
                                                         Agreement.

If the license model is already mapped, then the same is displayed in the Subscription Mapper page.

If subscription ID is already added, then it is auto-populated.

Existing configurations are retained.

Multiple subscription IDs can be mapped to a single customer.

One subscription ID must be mapped to a single customer.

All perpetual licenses are automatically mapped to the provider.

Perpetual licenses might not have Subscription ID.

#### What to do next

| Step 1 | View Smart Account Summary |
|---|---|
| Step 2 | Configure Smart Account |
| Step 3 | Virtual Account Summary |
| Step 4 | Assign and Unassign a cluster to Virtual Account |

| Note | HCM-F periodically syncs with CSSM and Satellite . |
|---|---|

| Step 1 | Skip this section if you already have a Smart Account. Otherwise, you can continue to the next step. |
|---|---|
| Step 2 | Log in to software.cisco.com using your Cisco.com ID (CCO ID). |
| Step 3 | Select Request a Smart Account under the Administration section. |
| Step 4 | Follow the steps to create a Smart Account for your organization. |

| Step 1 | From the side menu, select Infrastructure Manager > Smart Licensing > Configure Smart Account . |
|---|---|
| Step 2 | Click Add New . |
| Step 3 | Complete the fields in the Configure Smart Account
                                                Access page. Fields Description Smart Account Domain Name Domain name of smart account. Client ID ID of the smart account Client Secret Secret (password) of the smart account Smart Account Name Name of the smart account. This is an optional field. | Fields | Description | Smart Account Domain Name | Domain name of smart account. | Client ID | ID of the smart account | Client Secret | Secret (password) of the smart account | Smart Account Name | Name of the smart account. This is an optional field. |
| Fields | Description |
| Smart Account Domain Name | Domain name of smart account. |
| Client ID | ID of the smart account |
| Client Secret | Secret (password) of the smart account |
| Smart Account Name | Name of the smart account. This is an optional field. |
| Step 4 | Complete the fields in the Configure Smart Account
                                                Access page. In the Transport Settings enter the following
                                                   fields: Table 1. Transport Mode Settings Fields Description Transport Mode Select the transport mode to access CSSM. The
                                                                  options are: Proxy: Cisco products send usage information
                                                                        through a proxy server. Satellite: Cisco products are installed on
                                                                        premise and the connectivity to Cisco is online or
                                                                        offline. Direct: Cisco products send usage information
                                                                        directly. Configure the transport mode settings as follows: Table 2. Direct Transport Mode Settings Fields Description Authentication Gateway Displays the authentication gateway. CSSM Server Displays the CSSM server. Smart Account Domain Name Domain name of smart account. Client ID ID of the smart account Client Secret Secret (password) of the smart account Table 3. Proxy Transport Mode Settings Fields Description Proxy Hostname/IP Enter the proxy hostname or IP address. Note When you set the transport mode as proxy, the
                                                                              setting connects the HCM-F to the CSSM through
                                                                              proxy but does not register the customer and
                                                                              cluster with the CSSM. To register the cluster and customer to the
                                                                              CSSM, add the proxy values at the customer and
                                                                              cluster level to connect to the CSSM through
                                                                              proxy, otherwise it will connect through direct
                                                                              mode, by default. For more information about setting the proxy at
                                                                  customer and cluster level, see Add
                                                                     Customer , and Add Cluster at Hosted Collaboration Mediation Fulfillment
                                                                     Install and Configure Guide . Proxy Port Enter the proxy port. Authentication Gateway Displays the authentication gateway. Enable Proxy Authentication HCM-F uses the proxy authentication defined at
                                                                  the customer and cluster level to synchronize with
                                                                  CSSM. Proxy Username- Enter the proxy username. Proxy Password- Enter the proxy password. CSSM Server Displays the CSSM server. Smart Account Domain Name Domain name of smart account. Client ID ID of the smart account Client Secret Secret (password) of the smart account Table 4. Satellite Transport Mode Settings Fields Description Satellite Hostname Enter the satellite hostname. Satellite Port Enter the satellite port. Registration URL Enter the registration URL. Refer to the links below for the registration
                                                                  URLs for their respective satellite versions: Satellite version 6.3.0 -
                                                                        https://<SATELLITE_IP_ADDRESS>/Transportgateway/services/DeviceRequestHandler Satellite version 7.2.0 - HCM-F V12.5SU2 and above -
                                                                              https://<SATELLITE_FQDN>/SmartTransport below HCM-F V12.5SU2 -
                                                                              https://<SATELLITE_FQDN>/Transportgateway/services/DeviceRequestHandler Satellite version 8.X -
                                                                        https://<SATELLITE_FQDN>/SmartTransport Token URL Enter the Token URL. Refer to the links below for the Token URLs for
                                                                  their respective satellite versions: Satellite version 6.3.0 -
                                                                        https://<SATELLITE_IP_ADDRESS>:8443/backend/oauth/token Satellite version 7.2.0 -
                                                                        https://<SATELLITE_FQDN>:8443/backend/oauth/token Satellite version 8.X -
                                                                        https://<SATELLITE_FQDN>:8443/backend/oauth/token Local Account Domain Name Domain name of the satellite smart account. This field is displayed only when you select
                                                                  Satellite as the transport mode. Client ID ID of the smart account Client Secret Secret (password) of the smart account If the cluster is already assigned to a virtual account, and you want
                                                      to change the transport mode settings, the cluster has to be
                                                      unassigned from the virtual account, change the transport mode
                                                      settings, and then reassign the clusters to the virtual account. | Fields | Description | Transport Mode | Select the transport mode to access CSSM. The
                                                                  options are: Proxy: Cisco products send usage information
                                                                        through a proxy server. Satellite: Cisco products are installed on
                                                                        premise and the connectivity to Cisco is online or
                                                                        offline. Direct: Cisco products send usage information
                                                                        directly. | Fields | Description | Authentication Gateway | Displays the authentication gateway. | CSSM Server | Displays the CSSM server. | Smart Account Domain Name | Domain name of smart account. | Client ID | ID of the smart account | Client Secret | Secret (password) of the smart account | Fields | Description | Proxy Hostname/IP | Enter the proxy hostname or IP address. Note When you set the transport mode as proxy, the
                                                                              setting connects the HCM-F to the CSSM through
                                                                              proxy but does not register the customer and
                                                                              cluster with the CSSM. To register the cluster and customer to the
                                                                              CSSM, add the proxy values at the customer and
                                                                              cluster level to connect to the CSSM through
                                                                              proxy, otherwise it will connect through direct
                                                                              mode, by default. For more information about setting the proxy at
                                                                  customer and cluster level, see Add
                                                                     Customer , and Add Cluster at Hosted Collaboration Mediation Fulfillment
                                                                     Install and Configure Guide . | Note | When you set the transport mode as proxy, the
                                                                              setting connects the HCM-F to the CSSM through
                                                                              proxy but does not register the customer and
                                                                              cluster with the CSSM. To register the cluster and customer to the
                                                                              CSSM, add the proxy values at the customer and
                                                                              cluster level to connect to the CSSM through
                                                                              proxy, otherwise it will connect through direct
                                                                              mode, by default. | Proxy Port | Enter the proxy port. | Authentication Gateway | Displays the authentication gateway. | Enable Proxy Authentication | HCM-F uses the proxy authentication defined at
                                                                  the customer and cluster level to synchronize with
                                                                  CSSM. Proxy Username- Enter the proxy username. Proxy Password- Enter the proxy password. | CSSM Server | Displays the CSSM server. | Smart Account Domain Name | Domain name of smart account. | Client ID | ID of the smart account | Client Secret | Secret (password) of the smart account | Fields | Description | Satellite Hostname | Enter the satellite hostname. | Satellite Port | Enter the satellite port. | Registration URL | Enter the registration URL. Refer to the links below for the registration
                                                                  URLs for their respective satellite versions: Satellite version 6.3.0 -
                                                                        https://<SATELLITE_IP_ADDRESS>/Transportgateway/services/DeviceRequestHandler Satellite version 7.2.0 - HCM-F V12.5SU2 and above -
                                                                              https://<SATELLITE_FQDN>/SmartTransport below HCM-F V12.5SU2 -
                                                                              https://<SATELLITE_FQDN>/Transportgateway/services/DeviceRequestHandler Satellite version 8.X -
                                                                        https://<SATELLITE_FQDN>/SmartTransport | Token URL | Enter the Token URL. Refer to the links below for the Token URLs for
                                                                  their respective satellite versions: Satellite version 6.3.0 -
                                                                        https://<SATELLITE_IP_ADDRESS>:8443/backend/oauth/token Satellite version 7.2.0 -
                                                                        https://<SATELLITE_FQDN>:8443/backend/oauth/token Satellite version 8.X -
                                                                        https://<SATELLITE_FQDN>:8443/backend/oauth/token | Local Account Domain Name | Domain name of the satellite smart account. This field is displayed only when you select
                                                                  Satellite as the transport mode. | Client ID | ID of the smart account | Client Secret | Secret (password) of the smart account |
| Fields | Description |
| Transport Mode | Select the transport mode to access CSSM. The
                                                                  options are: Proxy: Cisco products send usage information
                                                                        through a proxy server. Satellite: Cisco products are installed on
                                                                        premise and the connectivity to Cisco is online or
                                                                        offline. Direct: Cisco products send usage information
                                                                        directly. |
| Fields | Description |
| Authentication Gateway | Displays the authentication gateway. |
| CSSM Server | Displays the CSSM server. |
| Smart Account Domain Name | Domain name of smart account. |
| Client ID | ID of the smart account |
| Client Secret | Secret (password) of the smart account |
| Fields | Description |
| Proxy Hostname/IP | Enter the proxy hostname or IP address. Note When you set the transport mode as proxy, the
                                                                              setting connects the HCM-F to the CSSM through
                                                                              proxy but does not register the customer and
                                                                              cluster with the CSSM. To register the cluster and customer to the
                                                                              CSSM, add the proxy values at the customer and
                                                                              cluster level to connect to the CSSM through
                                                                              proxy, otherwise it will connect through direct
                                                                              mode, by default. For more information about setting the proxy at
                                                                  customer and cluster level, see Add
                                                                     Customer , and Add Cluster at Hosted Collaboration Mediation Fulfillment
                                                                     Install and Configure Guide . | Note | When you set the transport mode as proxy, the
                                                                              setting connects the HCM-F to the CSSM through
                                                                              proxy but does not register the customer and
                                                                              cluster with the CSSM. To register the cluster and customer to the
                                                                              CSSM, add the proxy values at the customer and
                                                                              cluster level to connect to the CSSM through
                                                                              proxy, otherwise it will connect through direct
                                                                              mode, by default. |
| Note | When you set the transport mode as proxy, the
                                                                              setting connects the HCM-F to the CSSM through
                                                                              proxy but does not register the customer and
                                                                              cluster with the CSSM. To register the cluster and customer to the
                                                                              CSSM, add the proxy values at the customer and
                                                                              cluster level to connect to the CSSM through
                                                                              proxy, otherwise it will connect through direct
                                                                              mode, by default. |
| Proxy Port | Enter the proxy port. |
| Authentication Gateway | Displays the authentication gateway. |
| Enable Proxy Authentication | HCM-F uses the proxy authentication defined at
                                                                  the customer and cluster level to synchronize with
                                                                  CSSM. Proxy Username- Enter the proxy username. Proxy Password- Enter the proxy password. |
| CSSM Server | Displays the CSSM server. |
| Smart Account Domain Name | Domain name of smart account. |
| Client ID | ID of the smart account |
| Client Secret | Secret (password) of the smart account |
| Fields | Description |
| Satellite Hostname | Enter the satellite hostname. |
| Satellite Port | Enter the satellite port. |
| Registration URL | Enter the registration URL. Refer to the links below for the registration
                                                                  URLs for their respective satellite versions: Satellite version 6.3.0 -
                                                                        https://<SATELLITE_IP_ADDRESS>/Transportgateway/services/DeviceRequestHandler Satellite version 7.2.0 - HCM-F V12.5SU2 and above -
                                                                              https://<SATELLITE_FQDN>/SmartTransport below HCM-F V12.5SU2 -
                                                                              https://<SATELLITE_FQDN>/Transportgateway/services/DeviceRequestHandler Satellite version 8.X -
                                                                        https://<SATELLITE_FQDN>/SmartTransport |
| Token URL | Enter the Token URL. Refer to the links below for the Token URLs for
                                                                  their respective satellite versions: Satellite version 6.3.0 -
                                                                        https://<SATELLITE_IP_ADDRESS>:8443/backend/oauth/token Satellite version 7.2.0 -
                                                                        https://<SATELLITE_FQDN>:8443/backend/oauth/token Satellite version 8.X -
                                                                        https://<SATELLITE_FQDN>:8443/backend/oauth/token |
| Local Account Domain Name | Domain name of the satellite smart account. This field is displayed only when you select
                                                                  Satellite as the transport mode. |
| Client ID | ID of the smart account |
| Client Secret | Secret (password) of the smart account |
| Step 5 | Enable the Operational Licenses to autoregister the clusters to the specified
                                             virtual account. For more information about Operational Licenses and Auto Registration of
                                                clusters, see Auto-registration of Clusters Using Direct or Proxy Mode |
| Step 6 | Click Save . Note For 12.5 release, HCM-F supports only one smart account. When the smart
                                                         account is added in HCM-F, HCM-F performs a sync with CSSM to pull the Smart
                                                         account and virtual account data. If the number of virtual accounts are high
                                                         it might take more time to sync (approximately 1-2 hours). Note From 12.5SU1 release, HCM-F supports multiple smart accounts with
                                                         different client credentials, and multiple satellite accounts. When the
                                                         smart account is added in HCM-F, HCM-F performs a sync with CSSM and
                                                         satellite to retrieve the Smart account, virtual account, and local account
                                                         data. | Note | For 12.5 release, HCM-F supports only one smart account. When the smart
                                                         account is added in HCM-F, HCM-F performs a sync with CSSM to pull the Smart
                                                         account and virtual account data. If the number of virtual accounts are high
                                                         it might take more time to sync (approximately 1-2 hours). | Note | From 12.5SU1 release, HCM-F supports multiple smart accounts with
                                                         different client credentials, and multiple satellite accounts. When the
                                                         smart account is added in HCM-F, HCM-F performs a sync with CSSM and
                                                         satellite to retrieve the Smart account, virtual account, and local account
                                                         data. |
| Note | For 12.5 release, HCM-F supports only one smart account. When the smart
                                                         account is added in HCM-F, HCM-F performs a sync with CSSM to pull the Smart
                                                         account and virtual account data. If the number of virtual accounts are high
                                                         it might take more time to sync (approximately 1-2 hours). |
| Note | From 12.5SU1 release, HCM-F supports multiple smart accounts with
                                                         different client credentials, and multiple satellite accounts. When the
                                                         smart account is added in HCM-F, HCM-F performs a sync with CSSM and
                                                         satellite to retrieve the Smart account, virtual account, and local account
                                                         data. |

| Fields | Description |
|---|---|
| Smart Account Domain Name | Domain name of smart account. |
| Client ID | ID of the smart account |
| Client Secret | Secret (password) of the smart account |
| Smart Account Name | Name of the smart account. This is an optional field. |

| Fields | Description |
|---|---|
| Transport Mode | Select the transport mode to access CSSM. The
                                                                  options are: Proxy: Cisco products send usage information
                                                                        through a proxy server. Satellite: Cisco products are installed on
                                                                        premise and the connectivity to Cisco is online or
                                                                        offline. Direct: Cisco products send usage information
                                                                        directly. |

| Fields | Description |
|---|---|
| Authentication Gateway | Displays the authentication gateway. |
| CSSM Server | Displays the CSSM server. |
| Smart Account Domain Name | Domain name of smart account. |
| Client ID | ID of the smart account |
| Client Secret | Secret (password) of the smart account |

| Fields | Description |
|---|---|
| Proxy Hostname/IP | Enter the proxy hostname or IP address. Note When you set the transport mode as proxy, the
                                                                              setting connects the HCM-F to the CSSM through
                                                                              proxy but does not register the customer and
                                                                              cluster with the CSSM. To register the cluster and customer to the
                                                                              CSSM, add the proxy values at the customer and
                                                                              cluster level to connect to the CSSM through
                                                                              proxy, otherwise it will connect through direct
                                                                              mode, by default. For more information about setting the proxy at
                                                                  customer and cluster level, see Add
                                                                     Customer , and Add Cluster at Hosted Collaboration Mediation Fulfillment
                                                                     Install and Configure Guide . | Note | When you set the transport mode as proxy, the
                                                                              setting connects the HCM-F to the CSSM through
                                                                              proxy but does not register the customer and
                                                                              cluster with the CSSM. To register the cluster and customer to the
                                                                              CSSM, add the proxy values at the customer and
                                                                              cluster level to connect to the CSSM through
                                                                              proxy, otherwise it will connect through direct
                                                                              mode, by default. |
| Note | When you set the transport mode as proxy, the
                                                                              setting connects the HCM-F to the CSSM through
                                                                              proxy but does not register the customer and
                                                                              cluster with the CSSM. To register the cluster and customer to the
                                                                              CSSM, add the proxy values at the customer and
                                                                              cluster level to connect to the CSSM through
                                                                              proxy, otherwise it will connect through direct
                                                                              mode, by default. |
| Proxy Port | Enter the proxy port. |
| Authentication Gateway | Displays the authentication gateway. |
| Enable Proxy Authentication | HCM-F uses the proxy authentication defined at
                                                                  the customer and cluster level to synchronize with
                                                                  CSSM. Proxy Username- Enter the proxy username. Proxy Password- Enter the proxy password. |
| CSSM Server | Displays the CSSM server. |
| Smart Account Domain Name | Domain name of smart account. |
| Client ID | ID of the smart account |
| Client Secret | Secret (password) of the smart account |

| Note | When you set the transport mode as proxy, the
                                                                              setting connects the HCM-F to the CSSM through
                                                                              proxy but does not register the customer and
                                                                              cluster with the CSSM. To register the cluster and customer to the
                                                                              CSSM, add the proxy values at the customer and
                                                                              cluster level to connect to the CSSM through
                                                                              proxy, otherwise it will connect through direct
                                                                              mode, by default. |
|---|---|

| Fields | Description |
|---|---|
| Satellite Hostname | Enter the satellite hostname. |
| Satellite Port | Enter the satellite port. |
| Registration URL | Enter the registration URL. Refer to the links below for the registration
                                                                  URLs for their respective satellite versions: Satellite version 6.3.0 -
                                                                        https://<SATELLITE_IP_ADDRESS>/Transportgateway/services/DeviceRequestHandler Satellite version 7.2.0 - HCM-F V12.5SU2 and above -
                                                                              https://<SATELLITE_FQDN>/SmartTransport below HCM-F V12.5SU2 -
                                                                              https://<SATELLITE_FQDN>/Transportgateway/services/DeviceRequestHandler Satellite version 8.X -
                                                                        https://<SATELLITE_FQDN>/SmartTransport |
| Token URL | Enter the Token URL. Refer to the links below for the Token URLs for
                                                                  their respective satellite versions: Satellite version 6.3.0 -
                                                                        https://<SATELLITE_IP_ADDRESS>:8443/backend/oauth/token Satellite version 7.2.0 -
                                                                        https://<SATELLITE_FQDN>:8443/backend/oauth/token Satellite version 8.X -
                                                                        https://<SATELLITE_FQDN>:8443/backend/oauth/token |
| Local Account Domain Name | Domain name of the satellite smart account. This field is displayed only when you select
                                                                  Satellite as the transport mode. |
| Client ID | ID of the smart account |
| Client Secret | Secret (password) of the smart account |

| Note | For 12.5 release, HCM-F supports only one smart account. When the smart
                                                         account is added in HCM-F, HCM-F performs a sync with CSSM to pull the Smart
                                                         account and virtual account data. If the number of virtual accounts are high
                                                         it might take more time to sync (approximately 1-2 hours). |
|---|---|

| Note | From 12.5SU1 release, HCM-F supports multiple smart accounts with
                                                         different client credentials, and multiple satellite accounts. When the
                                                         smart account is added in HCM-F, HCM-F performs a sync with CSSM and
                                                         satellite to retrieve the Smart account, virtual account, and local account
                                                         data. |
|---|---|

| Step 1 | From the side menu, select Infrastructure Manager > Smart Licensing > Transport Mode . |
|---|---|
| Step 2 | Select the mode from the Transport Mode drop-down list. Note If transport mode is Direct, Authentication Gateway and CSSM Server information is displayed by default. When Smart account is provisioned with client credentials (Client ID and Client Secret) in HCM-F, the HCM-F authenticates
                                                                  with the Cisco Authentication Gateway with client credentials. HCM-F gets the access token from Cisco Authentication Gateway
                                                                  for communicating with CSSM. If transport mode is Proxy, enter the proxy server and the proxy server port details. Authentication Gateway and CSSM Server information is displayed by default. Note Proxy is the recommended option. Validate that HCMF and UC applications are connected to CSSM through the proxy. | Note | If transport mode is Direct, Authentication Gateway and CSSM Server information is displayed by default. When Smart account is provisioned with client credentials (Client ID and Client Secret) in HCM-F, the HCM-F authenticates
                                                                  with the Cisco Authentication Gateway with client credentials. HCM-F gets the access token from Cisco Authentication Gateway
                                                                  for communicating with CSSM. If transport mode is Proxy, enter the proxy server and the proxy server port details. Authentication Gateway and CSSM Server information is displayed by default. Note Proxy is the recommended option. Validate that HCMF and UC applications are connected to CSSM through the proxy. | Note | Proxy is the recommended option. Validate that HCMF and UC applications are connected to CSSM through the proxy. |
| Note | If transport mode is Direct, Authentication Gateway and CSSM Server information is displayed by default. When Smart account is provisioned with client credentials (Client ID and Client Secret) in HCM-F, the HCM-F authenticates
                                                                  with the Cisco Authentication Gateway with client credentials. HCM-F gets the access token from Cisco Authentication Gateway
                                                                  for communicating with CSSM. If transport mode is Proxy, enter the proxy server and the proxy server port details. Authentication Gateway and CSSM Server information is displayed by default. Note Proxy is the recommended option. Validate that HCMF and UC applications are connected to CSSM through the proxy. | Note | Proxy is the recommended option. Validate that HCMF and UC applications are connected to CSSM through the proxy. |
| Note | Proxy is the recommended option. Validate that HCMF and UC applications are connected to CSSM through the proxy. |

| Note | If transport mode is Direct, Authentication Gateway and CSSM Server information is displayed by default. When Smart account is provisioned with client credentials (Client ID and Client Secret) in HCM-F, the HCM-F authenticates
                                                                  with the Cisco Authentication Gateway with client credentials. HCM-F gets the access token from Cisco Authentication Gateway
                                                                  for communicating with CSSM. If transport mode is Proxy, enter the proxy server and the proxy server port details. Authentication Gateway and CSSM Server information is displayed by default. Note Proxy is the recommended option. Validate that HCMF and UC applications are connected to CSSM through the proxy. | Note | Proxy is the recommended option. Validate that HCMF and UC applications are connected to CSSM through the proxy. |
|---|---|---|---|
| Note | Proxy is the recommended option. Validate that HCMF and UC applications are connected to CSSM through the proxy. |

| Note | Proxy is the recommended option. Validate that HCMF and UC applications are connected to CSSM through the proxy. |
|---|---|

| Step 1 | From the side menu, select Infrastructure Manager > Smart Licensing > Smart Account Summary . |
|---|---|
| Step 2 | The Smart Account Summary page shows the following
                                             information on smart accounts: Fields Description Name Name of smart account Domain Domain name of smart account Type Type of smart account Status Status of smart account: active or inactive VA# Number of virtual account associated with the smart
                                                            account Last SyncUp Last sync up time of smart account Alerts Shows the alerts Note To see the virtual accounts associated with the smart account, click the
                                                            smart account name from the list. The Virtual Accounts page shows the
                                                            list of virtual accounts. Note To see the virtual accounts associated with the smart account, click the
                                                            virtual account name from the list. The Virtual Accounts page shows the
                                                            list of virtual accounts. | Fields | Description | Name | Name of smart account | Domain | Domain name of smart account | Type | Type of smart account | Status | Status of smart account: active or inactive | VA# | Number of virtual account associated with the smart
                                                            account | Last SyncUp | Last sync up time of smart account | Alerts | Shows the alerts | Note | To see the virtual accounts associated with the smart account, click the
                                                            smart account name from the list. The Virtual Accounts page shows the
                                                            list of virtual accounts. | Note | To see the virtual accounts associated with the smart account, click the
                                                            virtual account name from the list. The Virtual Accounts page shows the
                                                            list of virtual accounts. |
| Fields | Description |
| Name | Name of smart account |
| Domain | Domain name of smart account |
| Type | Type of smart account |
| Status | Status of smart account: active or inactive |
| VA# | Number of virtual account associated with the smart
                                                            account |
| Last SyncUp | Last sync up time of smart account |
| Alerts | Shows the alerts |
| Note | To see the virtual accounts associated with the smart account, click the
                                                            smart account name from the list. The Virtual Accounts page shows the
                                                            list of virtual accounts. |
| Note | To see the virtual accounts associated with the smart account, click the
                                                            virtual account name from the list. The Virtual Accounts page shows the
                                                            list of virtual accounts. |
| Step 3 | Click Add New to configure a new smart account. Click the Smart Account Name to edit the existing Smart Account. |

| Fields | Description |
|---|---|
| Name | Name of smart account |
| Domain | Domain name of smart account |
| Type | Type of smart account |
| Status | Status of smart account: active or inactive |
| VA# | Number of virtual account associated with the smart
                                                            account |
| Last SyncUp | Last sync up time of smart account |
| Alerts | Shows the alerts |

| Note | To see the virtual accounts associated with the smart account, click the
                                                            smart account name from the list. The Virtual Accounts page shows the
                                                            list of virtual accounts. |
|---|---|

| Note | To see the virtual accounts associated with the smart account, click the
                                                            virtual account name from the list. The Virtual Accounts page shows the
                                                            list of virtual accounts. |
|---|---|

| Step 1 | Login to software.cisco.com using your Cisco.com ID (CCO ID). |
|---|---|
| Step 2 | Select Manage Smart Account under Administration section |
| Step 3 | Select the Virtual Accounts tab and then select New Virtual Account... . |
| Step 4 | Create two Virtual Accounts and name them as: VA–HCS-Ordered VA–HCS-Operational |
| Step 5 | Ensure to add the following two users in Cisco HCS Operations Team as Virtual Account User. alicchan@cisco.com trgilman@cisco.com |

| Step 1 | From the side menu, select Infrastructure Manager > Smart Licensing > Virtual Account Summary . |
|---|---|
| Step 2 | The Virtual Accounts page shows the list of virtual accounts, and the following information on virtual accounts: Fields Description Name Name of virtual account SA Name Name of smart account Access Level Specifies the access level assigned to the virtual account Clusters # Number of clusters assigned to the virtual account Customer# Name of customers assigned to the virtual account | Fields | Description | Name | Name of virtual account | SA Name | Name of smart account | Access Level | Specifies the access level assigned to the virtual account | Clusters # | Number of clusters assigned to the virtual account | Customer# | Name of customers assigned to the virtual account |
| Fields | Description |
| Name | Name of virtual account |
| SA Name | Name of smart account |
| Access Level | Specifies the access level assigned to the virtual account |
| Clusters # | Number of clusters assigned to the virtual account |
| Customer# | Name of customers assigned to the virtual account |

| Fields | Description |
|---|---|
| Name | Name of virtual account |
| SA Name | Name of smart account |
| Access Level | Specifies the access level assigned to the virtual account |
| Clusters # | Number of clusters assigned to the virtual account |
| Customer# | Name of customers assigned to the virtual account |

| Step 1 | From the side menu, select Infrastructure Manager > Smart Licensing > Virtual Account Summary . |
|---|---|
| Step 2 | From the Virtual Accounts page, click a virtual account name. |
| Step 3 | From the Edit Virtual Account page, select the license mode from the License Mode dropdown. |
| Step 4 | Click Assign in the Clusters Assigned to Virtual Account section. Note You cannot assign the cluster to the virtual account if the license mode for the virtual account is not set. A warning message
                                                                  is displayed asking to add the license mode for the VA. You cannot change the license mode of a virtual account if a cluster is assigned to the virtual account. In this scenario,
                                                                  unassign the cluster from the virtual account. | Note | You cannot assign the cluster to the virtual account if the license mode for the virtual account is not set. A warning message
                                                                  is displayed asking to add the license mode for the VA. You cannot change the license mode of a virtual account if a cluster is assigned to the virtual account. In this scenario,
                                                                  unassign the cluster from the virtual account. |
| Note | You cannot assign the cluster to the virtual account if the license mode for the virtual account is not set. A warning message
                                                                  is displayed asking to add the license mode for the VA. You cannot change the license mode of a virtual account if a cluster is assigned to the virtual account. In this scenario,
                                                                  unassign the cluster from the virtual account. |
| Step 5 | From the Assign Cluster to Virtual Account page, select the cluster by checking the check box. Note Only clusters higher than 11.x is displayed here. | Note | Only clusters higher than 11.x is displayed here. |
| Note | Only clusters higher than 11.x is displayed here. |
| Step 6 | Click Assign . Note To unassign a cluster from the virtual account, select the cluster by checking the check box from the Clusters Assigned to Virtual Account section, and then click Unassign . To assign or unassign a cluster from the virtual account, use the filter by customer name to filter the clusters. | Note | To unassign a cluster from the virtual account, select the cluster by checking the check box from the Clusters Assigned to Virtual Account section, and then click Unassign . To assign or unassign a cluster from the virtual account, use the filter by customer name to filter the clusters. |
| Note | To unassign a cluster from the virtual account, select the cluster by checking the check box from the Clusters Assigned to Virtual Account section, and then click Unassign . To assign or unassign a cluster from the virtual account, use the filter by customer name to filter the clusters. |

| Note | You cannot assign the cluster to the virtual account if the license mode for the virtual account is not set. A warning message
                                                                  is displayed asking to add the license mode for the VA. You cannot change the license mode of a virtual account if a cluster is assigned to the virtual account. In this scenario,
                                                                  unassign the cluster from the virtual account. |
|---|---|

| Note | Only clusters higher than 11.x is displayed here. |
|---|---|

| Note | To unassign a cluster from the virtual account, select the cluster by checking the check box from the Clusters Assigned to Virtual Account section, and then click Unassign . To assign or unassign a cluster from the virtual account, use the filter by customer name to filter the clusters. |
|---|---|

| Note | If the clusters are registered in satellite, then HCM-F syncs with CSSM using proxy and gets the details of the satellite
                                             operational licenses. |
|---|---|

| Step 1 | Fill this smart sheet http://cs.co/HCSPartnerRequestForm to get access to the Operational
                                          Licenses. |
|---|---|
| Step 2 | Once you receive a confirmation, create the following virtual accounts in CSSM. Ordered Virtual Account Displays the name of the virtual account that stores the licenses that the partners order from CCW. We recommend the Ordered
                                                Virtual Account name as va-hcs-ordered. Operational Virtual Account Displays the name of the virtual account that stores the Cisco licenses to be consumed. We recommend the Operational Virtual
                                                Account name as va-hcs-operational. The clusters are registered to this virtual account in CSSM. |

| Step 1 | User orders licenses from CCW. |
|---|---|
| Step 2 | For all users ordered licenses, a virtual account is created in CSSM: va-hcs-ordered . |
| Step 3 | Fill this smart sheet http://cs.co/HCSPartnerRequestForm to get access to the Operational
                                             Licenses. For more information on the prerequisites, see Configuring Operational Licenses . |
| Step 4 | Create an operational virtual account in CSSM, where Cisco deposits all the operational licenses that are to be consumed: va-hcs-operations . Once you have opted for operational license, autoregistration of clusters is possible while you configure a smart account. |
| Step 5 | HCM-F queries ordered virtual account for licenses that are deposited per Subscription ID. HCM-F is preconfigured to map Customer to Subscription ID. |
| Step 6 | HCM-F queries Cisco Unified Communications applications for the license consumption report. A consolidated report is generated with the ordered license details, consumption details, and compliance status. For more
                                             information about the report, see Request or Download Flex Usage Report |

| Step 1 | User orders licenses from CCW. |
|---|---|
| Step 2 | For all users ordered licenses, a virtual account is created in CSSM: va-hcs-ordered . |
| Step 3 | Fill this smart sheet http://cs.co/HCSPartnerRequestForm to get access to the Operational
                                             Licenses. For more information on the prerequisites, see Configuring Operational Licenses . |
| Step 4 | Create an operational virtual account in CSSM, where Cisco deposits all the operational licenses that are to be consumed: va-hcs-operations . User has to move the licenses from operations VA in CSSM to satellite VAs. Autoregistration feature supports only one Satellite account. For using more than one Satellite, user can use the Satellite
                                                on board functionality that is provided by HCM-F. |
| Step 5 | HCM-F queries ordered virtual account for licenses that are deposited per Subscription ID. HCM-F is preconfigured to map Customer to Subscription ID. |
| Step 6 | HCM-F queries Cisco Unified Communications applications for license consumption report. A consolidated report is generated with the ordered license details, consumption details, and compliance status. For more
                                             information about the report, see Request or Download Flex Usage Report |

| Step 1 | From the side menu, select Infrastructure Manager > Smart Licensing > Cluster Summary . The Cluster Summary page displays the following: List of Unified Communication clusters with the version 12.5 and later. List of Expressway E and C clusters with version X12.6 and later that are configured with Smart licensing mode. Note Registration of Expressway clusters in HCM-F is at the cluster level whereas for the other applications registration in HCM-F
                                                               is done by node. Fields Description Name Name of the cluster Type Retrieves the type of cluster such as Unified CM, Unity Connection, CER, Expressway-E, Expressway-C from the HCM-F inventory. Version Specifies the Cluster version. Smart Account Name of the Smart Account that is associated with the virtual account. Virtual Account Virtual Account name that the cluster is associated with. Status Displays the status of the clusters, if they are registered, unregistered, partially registered or autoregistered to the virtual
                                                         account. For example, if the cluster is autoregistered, then the status is displayed as Autoregistered. The information icon provides details about the cluster status, description, and the recommended action. The cluster status is prioritized as follows: Multiple Virtual Account Registered -Specifies the clusters that are assigned offline using the Expressway user interface,
                                                               where all the nodes are not registered to the same VA. Partial and mutiple VA applies only to Expressway-E and C clusters. NOTE: For clusters registered as multiple VA registered, you cannot assign/unassign clusters using the HCM-F application.
                                                               Use the Expressway application to assign the multiple VA registered clusters. Auto Registration Failed - Auto registration of the cluster fails. Manual Registration Failed - Manual assignment of cluster fails. Deregistration Failed - Manual unassignment of the cluster fails. Deregistered - cluster is unassigned manually. Partially Registered - cluster is partially assigned when: All nodes of a cluster are not registered. If one of the node of the cluster is either registered/unregistered NOTE: Partially Registered status applies only to Expressway E and C clusters. Auto Registration Inprogress - auto registration of the cluster is in progress. Auto Deregistration InProgress - Auto deregistration of cluster is in progress. Auto Registered - cluster is autoregistered to the virtual account. Manually Registered - cluster is manually assigned to a virtual account. Deregistered - clusters are not assigned to any virtual account. NOTE: Add all the nodes of the Expressway cluster in HCM-F, to register the cluster. If there is a mismatch in the number of Expressway
                                                         cluster nodes that is configured in HCM-F, then the registration fails. Job Status The information icon provides the provisioning status of the cluster. | Note | Registration of Expressway clusters in HCM-F is at the cluster level whereas for the other applications registration in HCM-F
                                                               is done by node. | Fields | Description | Name | Name of the cluster | Type | Retrieves the type of cluster such as Unified CM, Unity Connection, CER, Expressway-E, Expressway-C from the HCM-F inventory. | Version | Specifies the Cluster version. | Smart Account | Name of the Smart Account that is associated with the virtual account. | Virtual Account | Virtual Account name that the cluster is associated with. | Status | Displays the status of the clusters, if they are registered, unregistered, partially registered or autoregistered to the virtual
                                                         account. For example, if the cluster is autoregistered, then the status is displayed as Autoregistered. The information icon provides details about the cluster status, description, and the recommended action. The cluster status is prioritized as follows: Multiple Virtual Account Registered -Specifies the clusters that are assigned offline using the Expressway user interface,
                                                               where all the nodes are not registered to the same VA. Partial and mutiple VA applies only to Expressway-E and C clusters. NOTE: For clusters registered as multiple VA registered, you cannot assign/unassign clusters using the HCM-F application.
                                                               Use the Expressway application to assign the multiple VA registered clusters. Auto Registration Failed - Auto registration of the cluster fails. Manual Registration Failed - Manual assignment of cluster fails. Deregistration Failed - Manual unassignment of the cluster fails. Deregistered - cluster is unassigned manually. Partially Registered - cluster is partially assigned when: All nodes of a cluster are not registered. If one of the node of the cluster is either registered/unregistered NOTE: Partially Registered status applies only to Expressway E and C clusters. Auto Registration Inprogress - auto registration of the cluster is in progress. Auto Deregistration InProgress - Auto deregistration of cluster is in progress. Auto Registered - cluster is autoregistered to the virtual account. Manually Registered - cluster is manually assigned to a virtual account. Deregistered - clusters are not assigned to any virtual account. NOTE: Add all the nodes of the Expressway cluster in HCM-F, to register the cluster. If there is a mismatch in the number of Expressway
                                                         cluster nodes that is configured in HCM-F, then the registration fails. | Job Status | The information icon provides the provisioning status of the cluster. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Note | Registration of Expressway clusters in HCM-F is at the cluster level whereas for the other applications registration in HCM-F
                                                               is done by node. |
| Fields | Description |
| Name | Name of the cluster |
| Type | Retrieves the type of cluster such as Unified CM, Unity Connection, CER, Expressway-E, Expressway-C from the HCM-F inventory. |
| Version | Specifies the Cluster version. |
| Smart Account | Name of the Smart Account that is associated with the virtual account. |
| Virtual Account | Virtual Account name that the cluster is associated with. |
| Status | Displays the status of the clusters, if they are registered, unregistered, partially registered or autoregistered to the virtual
                                                         account. For example, if the cluster is autoregistered, then the status is displayed as Autoregistered. The information icon provides details about the cluster status, description, and the recommended action. The cluster status is prioritized as follows: Multiple Virtual Account Registered -Specifies the clusters that are assigned offline using the Expressway user interface,
                                                               where all the nodes are not registered to the same VA. Partial and mutiple VA applies only to Expressway-E and C clusters. NOTE: For clusters registered as multiple VA registered, you cannot assign/unassign clusters using the HCM-F application.
                                                               Use the Expressway application to assign the multiple VA registered clusters. Auto Registration Failed - Auto registration of the cluster fails. Manual Registration Failed - Manual assignment of cluster fails. Deregistration Failed - Manual unassignment of the cluster fails. Deregistered - cluster is unassigned manually. Partially Registered - cluster is partially assigned when: All nodes of a cluster are not registered. If one of the node of the cluster is either registered/unregistered NOTE: Partially Registered status applies only to Expressway E and C clusters. Auto Registration Inprogress - auto registration of the cluster is in progress. Auto Deregistration InProgress - Auto deregistration of cluster is in progress. Auto Registered - cluster is autoregistered to the virtual account. Manually Registered - cluster is manually assigned to a virtual account. Deregistered - clusters are not assigned to any virtual account. NOTE: Add all the nodes of the Expressway cluster in HCM-F, to register the cluster. If there is a mismatch in the number of Expressway
                                                         cluster nodes that is configured in HCM-F, then the registration fails. |
| Job Status | The information icon provides the provisioning status of the cluster. |
| Step 2 | Hover over the information icon for a cluster in the Job Status column to see the job details of the cluster. Fields Description Job Type Specifies the provisioning status of the cluster. Entity Type Specifies the type of the cluster. Date/Time Initiated Specifies the data and time when the job was initiated. Date/Time Completed Specifies the data and time when the job completed. Status Specifies the overall status of the job. Entity Name Specifies the entity name of the cluster. Description Details of the job. Status Information Status of the job Recommended Action Describe the action to resolve the issue. | Fields | Description | Job Type | Specifies the provisioning status of the cluster. | Entity Type | Specifies the type of the cluster. | Date/Time Initiated | Specifies the data and time when the job was initiated. | Date/Time Completed | Specifies the data and time when the job completed. | Status | Specifies the overall status of the job. | Entity Name | Specifies the entity name of the cluster. | Description | Details of the job. | Status Information | Status of the job | Recommended Action | Describe the action to resolve the issue. |
| Fields | Description |
| Job Type | Specifies the provisioning status of the cluster. |
| Entity Type | Specifies the type of the cluster. |
| Date/Time Initiated | Specifies the data and time when the job was initiated. |
| Date/Time Completed | Specifies the data and time when the job completed. |
| Status | Specifies the overall status of the job. |
| Entity Name | Specifies the entity name of the cluster. |
| Description | Details of the job. |
| Status Information | Status of the job |
| Recommended Action | Describe the action to resolve the issue. |
| Step 3 | To modify a cluster, select a cluster from the list, and modify the details in the Cluster Summary page. For more information about the field details in the Cluster Summary page, see Add Cluster section in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide . Note If you apply a filter of Type on the Cluster, then the set of keyword values that are allowed for Expressway clusters in Smart
                                                         licensing mode are: core, edge, expressway,expresswayedge, expressway edge,expresswaycore, and expressway core. | Note | If you apply a filter of Type on the Cluster, then the set of keyword values that are allowed for Expressway clusters in Smart
                                                         licensing mode are: core, edge, expressway,expresswayedge, expressway edge,expresswaycore, and expressway core. |
| Note | If you apply a filter of Type on the Cluster, then the set of keyword values that are allowed for Expressway clusters in Smart
                                                         licensing mode are: core, edge, expressway,expresswayedge, expressway edge,expresswaycore, and expressway core. |

| Note | Registration of Expressway clusters in HCM-F is at the cluster level whereas for the other applications registration in HCM-F
                                                               is done by node. |
|---|---|

| Fields | Description |
|---|---|
| Name | Name of the cluster |
| Type | Retrieves the type of cluster such as Unified CM, Unity Connection, CER, Expressway-E, Expressway-C from the HCM-F inventory. |
| Version | Specifies the Cluster version. |
| Smart Account | Name of the Smart Account that is associated with the virtual account. |
| Virtual Account | Virtual Account name that the cluster is associated with. |
| Status | Displays the status of the clusters, if they are registered, unregistered, partially registered or autoregistered to the virtual
                                                         account. For example, if the cluster is autoregistered, then the status is displayed as Autoregistered. The information icon provides details about the cluster status, description, and the recommended action. The cluster status is prioritized as follows: Multiple Virtual Account Registered -Specifies the clusters that are assigned offline using the Expressway user interface,
                                                               where all the nodes are not registered to the same VA. Partial and mutiple VA applies only to Expressway-E and C clusters. NOTE: For clusters registered as multiple VA registered, you cannot assign/unassign clusters using the HCM-F application.
                                                               Use the Expressway application to assign the multiple VA registered clusters. Auto Registration Failed - Auto registration of the cluster fails. Manual Registration Failed - Manual assignment of cluster fails. Deregistration Failed - Manual unassignment of the cluster fails. Deregistered - cluster is unassigned manually. Partially Registered - cluster is partially assigned when: All nodes of a cluster are not registered. If one of the node of the cluster is either registered/unregistered NOTE: Partially Registered status applies only to Expressway E and C clusters. Auto Registration Inprogress - auto registration of the cluster is in progress. Auto Deregistration InProgress - Auto deregistration of cluster is in progress. Auto Registered - cluster is autoregistered to the virtual account. Manually Registered - cluster is manually assigned to a virtual account. Deregistered - clusters are not assigned to any virtual account. NOTE: Add all the nodes of the Expressway cluster in HCM-F, to register the cluster. If there is a mismatch in the number of Expressway
                                                         cluster nodes that is configured in HCM-F, then the registration fails. |
| Job Status | The information icon provides the provisioning status of the cluster. |

| Fields | Description |
|---|---|
| Job Type | Specifies the provisioning status of the cluster. |
| Entity Type | Specifies the type of the cluster. |
| Date/Time Initiated | Specifies the data and time when the job was initiated. |
| Date/Time Completed | Specifies the data and time when the job completed. |
| Status | Specifies the overall status of the job. |
| Entity Name | Specifies the entity name of the cluster. |
| Description | Details of the job. |
| Status Information | Status of the job |
| Recommended Action | Describe the action to resolve the issue. |

| Note | If you apply a filter of Type on the Cluster, then the set of keyword values that are allowed for Expressway clusters in Smart
                                                         licensing mode are: core, edge, expressway,expresswayedge, expressway edge,expresswaycore, and expressway core. |
|---|---|

| Step 1 | From the side menu, select Infrastructure Manager > Smart Licensing > Virtual Account Summary |
|---|---|
| Step 2 | Select the virtual account to make changes, the Edit Virtual account window displays. Field Description Name Name of virtual account Description Displays a short description of the account Smart Account Name Displays the Smart account name. Domain Name Displays the associated domain name of the cluster. License Mode Specifies the license mode that is associated with the cluster. Commercial Access Level Specifies the access level that is assigned to the virtual account | Field | Description | Name | Name of virtual account | Description | Displays a short description of the account | Smart Account Name | Displays the Smart account name. | Domain Name | Displays the associated domain name of the cluster. | License Mode | Specifies the license mode that is associated with the cluster. | Commercial Access Level | Specifies the access level that is assigned to the virtual account |
| Field | Description |
| Name | Name of virtual account |
| Description | Displays a short description of the account |
| Smart Account Name | Displays the Smart account name. |
| Domain Name | Displays the associated domain name of the cluster. |
| License Mode | Specifies the license mode that is associated with the cluster. |
| Commercial Access Level | Specifies the access level that is assigned to the virtual account |
| Step 3 | Clusters Assigned- Displays the details of all clusters that are associated with the virtual account. Select unassign, to
                                             unassign a cluster for the account. Click Assign, to add a new cluster to the account. |

| Field | Description |
|---|---|
| Name | Name of virtual account |
| Description | Displays a short description of the account |
| Smart Account Name | Displays the Smart account name. |
| Domain Name | Displays the associated domain name of the cluster. |
| License Mode | Specifies the license mode that is associated with the cluster. |
| Commercial Access Level | Specifies the access level that is assigned to the virtual account |

| Note | If you enable autoregistration, HCM-F changes the license modes of the UC Applications to HCS mode. Hence, the publisher node
                                                of the clusters which are in enterprise mode reboots and the license mode is changed to HCS mode. |
|---|---|

| Note | Autoregistration of clusters is possible for only one Smart Account. If Operational Licenses are enabled for a smart account, and you try to configure a new smart account or satellite account, the Operational Licenses check-box is disabled. If you have not opted for Operational Licenses, you cannot autoregister the clusters to the operational virtual account. |
|---|---|

| Note | Configure the proxy settings at customer or cluster level before enabling auto-registration for Proxy mode. For more information,
                                                see Add Cluster in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide . |
|---|---|

| Step 1 | Navigate to Infrastructure Manager > Smart Licensing > Smart Account Summary . Click Add New to configure the smart accounts. |
|---|---|
| Step 2 | Select Opted Operational Licenses to register the clusters to the following virtual accounts: Ordered Virtual Account Displays the name of the virtual account that stores the licenses that the partners order from CCW. We recommend the Ordered
                                                   Virtual Account name as va-hcs-ordered. Operational Virtual Account Displays the name of the virtual account that stores the Cisco licenses to be consumed. We recommend the Operational Virtual
                                                   Account name as va-hcs-operational. The clusters are registered to this virtual account in CSSM. Note If the Ordered and Operational VAs are unchanged, a job for auto-registration is not triggered. Only way to trigger the job
                                                                  is to disable and enable the auto-registration again as part of smart account configuration update. If the ordererd and operational VAs are different and valid, it first triggers de-registration job for unassigning the clusters
                                                                  from the old operational VA and then trigger auto-registration job for assigning to the new operational VA. Any auto-registered cluster can be manually unassigned and re-assigned to different VA. In such case, that cluster is no longer
                                                                  considered as part of the autoregistration process. If at all the cluster has to be part of the auto-registration, then the
                                                                  smart account should be either updated with first disabling and then enabling auto-registration. Autoregistration of the clusters is possible if any of the following conditions are met: When the clusters with version 12.5 is installed, the clusters are automatically autoregistered to the operational virtual
                                                      account. When the clusters are upgraded to 12.5, and you have opted for operational licenses, you can choose to autoregister the clusters
                                                      to the operational virtual account, otherwise they are manually assigned to the virtual accounts. While configuring the smart account, if you opt for operational licenses and enable autoregistration, any  existing 12.5 cluster
                                                      version is autoregistered. Following are the cluster assignment to virtual account scenarious: Table 5. Cluster Assignment Scenarios If... Then... You want one of the cluster to be removed from the autoregistered virtual account You have to unassign the cluster manually from the autoregistered virtual account, and reassign the cluster manually to the
                                                            specific virtual account. You want one of the cluster to be reassigned to the autoregistered virtual account You have to unassign the cluster manually from the specific virtual acount, and reassign the cluster manually to the autoregistered
                                                            virtual account. Any cluster fails to autoregister to the operational virtual account You can do the following: An on-demand or auto sync that happens in every 24 hours registers the cluster to the operational virtual account. You can also disable the autoregistration option and enable it again as part of Smart Account update. | Note | If the Ordered and Operational VAs are unchanged, a job for auto-registration is not triggered. Only way to trigger the job
                                                                  is to disable and enable the auto-registration again as part of smart account configuration update. If the ordererd and operational VAs are different and valid, it first triggers de-registration job for unassigning the clusters
                                                                  from the old operational VA and then trigger auto-registration job for assigning to the new operational VA. Any auto-registered cluster can be manually unassigned and re-assigned to different VA. In such case, that cluster is no longer
                                                                  considered as part of the autoregistration process. If at all the cluster has to be part of the auto-registration, then the
                                                                  smart account should be either updated with first disabling and then enabling auto-registration. | If... | Then... | You want one of the cluster to be removed from the autoregistered virtual account | You have to unassign the cluster manually from the autoregistered virtual account, and reassign the cluster manually to the
                                                            specific virtual account. | You want one of the cluster to be reassigned to the autoregistered virtual account | You have to unassign the cluster manually from the specific virtual acount, and reassign the cluster manually to the autoregistered
                                                            virtual account. | Any cluster fails to autoregister to the operational virtual account | You can do the following: An on-demand or auto sync that happens in every 24 hours registers the cluster to the operational virtual account. You can also disable the autoregistration option and enable it again as part of Smart Account update. |
| Note | If the Ordered and Operational VAs are unchanged, a job for auto-registration is not triggered. Only way to trigger the job
                                                                  is to disable and enable the auto-registration again as part of smart account configuration update. If the ordererd and operational VAs are different and valid, it first triggers de-registration job for unassigning the clusters
                                                                  from the old operational VA and then trigger auto-registration job for assigning to the new operational VA. Any auto-registered cluster can be manually unassigned and re-assigned to different VA. In such case, that cluster is no longer
                                                                  considered as part of the autoregistration process. If at all the cluster has to be part of the auto-registration, then the
                                                                  smart account should be either updated with first disabling and then enabling auto-registration. |
| If... | Then... |
| You want one of the cluster to be removed from the autoregistered virtual account | You have to unassign the cluster manually from the autoregistered virtual account, and reassign the cluster manually to the
                                                            specific virtual account. |
| You want one of the cluster to be reassigned to the autoregistered virtual account | You have to unassign the cluster manually from the specific virtual acount, and reassign the cluster manually to the autoregistered
                                                            virtual account. |
| Any cluster fails to autoregister to the operational virtual account | You can do the following: An on-demand or auto sync that happens in every 24 hours registers the cluster to the operational virtual account. You can also disable the autoregistration option and enable it again as part of Smart Account update. |
| Step 3 | Select Enable Auto Registration of applications (disable if you are using Satellite) option to autoregister the clusters to the operational virtual account in CSSM, while using the Direct and Proxy as the Transport
                                             Mode. De-select the autoregistration option, if you want to autoregister the clusters using the Satellite as the Transport
                                             Mode. Autoregistration is automatically triggered when: If any configuration details are wrong during the Smart Account configuration (For example, Proxy hostname, IP address, and
                                                      so on), update the fileds with the right value, then the autoregistration is automatically triggered. In case of proxy mode, if right proxy details are provided at cluster or customer level as part of the update, autoregistration
                                                      is automatically triggered. Any of the operations, such as credential change, network address change to a valid value for a cluster as part of the update
                                                      also triggers autoregistration. |

| Note | If the Ordered and Operational VAs are unchanged, a job for auto-registration is not triggered. Only way to trigger the job
                                                                  is to disable and enable the auto-registration again as part of smart account configuration update. If the ordererd and operational VAs are different and valid, it first triggers de-registration job for unassigning the clusters
                                                                  from the old operational VA and then trigger auto-registration job for assigning to the new operational VA. Any auto-registered cluster can be manually unassigned and re-assigned to different VA. In such case, that cluster is no longer
                                                                  considered as part of the autoregistration process. If at all the cluster has to be part of the auto-registration, then the
                                                                  smart account should be either updated with first disabling and then enabling auto-registration. |
|---|---|

| If... | Then... |
|---|---|
| You want one of the cluster to be removed from the autoregistered virtual account | You have to unassign the cluster manually from the autoregistered virtual account, and reassign the cluster manually to the
                                                            specific virtual account. |
| You want one of the cluster to be reassigned to the autoregistered virtual account | You have to unassign the cluster manually from the specific virtual acount, and reassign the cluster manually to the autoregistered
                                                            virtual account. |
| Any cluster fails to autoregister to the operational virtual account | You can do the following: An on-demand or auto sync that happens in every 24 hours registers the cluster to the operational virtual account. You can also disable the autoregistration option and enable it again as part of Smart Account update. |

| Step 1 | Navigate to Infrastructure Manager > Smart Licensing > Smart Account Summary . Click Add New to configure the smart accounts. |
|---|---|
| Step 2 | Select Satellite as the Transport Mode. Note Operational License options must be enabled while configuring smart accounts by using the Proxy or Direct mode. | Note | Operational License options must be enabled while configuring smart accounts by using the Proxy or Direct mode. |
| Note | Operational License options must be enabled while configuring smart accounts by using the Proxy or Direct mode. |
| Step 3 | Select Enable Auto Registration to register the clusters to the operational virtual account. When you configure a smart account using Satellite as the Transport Mode, the Enable Auto Registration option is enabled. You can provide an operational virtual account name, and the clusters are auto-assigned to the virtual
                                                account in the satellite server. |

| Note | Operational License options must be enabled while configuring smart accounts by using the Proxy or Direct mode. |
|---|---|

| Step 1 | Complete the seps in Initial One Time Setup in CSSM for Smart Licensing topic. |
|---|---|
| Step 2 | Upgrade HCM-F to 12.5(x). For more information about upgrading HCM-F, see Upgrade HCM-F in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide . Set the Transport Mode in HCM-F, navigate to Smart Licensing > Transport Mode . |
| Step 3 | Provision Smart Account in HCM-F. Configure the Smart Account or Satellite local account, navigate to Smart Licensing > Configure Smart Accounts . For details, see Cisco Hosted Collaboration Solution Smart Licensing Guide . Configure the Smart Account, navigate to Smart Licensing > Smart Accounts . Click Add New , to configure smart accounts. For more information, see Configure Smart Account Access . Note Once the Smart Account is configured, HCM-F synchronizes with CSSM and Satellite and retrieves all the Virtual Account details to HCM-F in Virtual Account Summary window ( Smart Licensing > Virtual Account Summary ). | Note | Once the Smart Account is configured, HCM-F synchronizes with CSSM and Satellite and retrieves all the Virtual Account details to HCM-F in Virtual Account Summary window ( Smart Licensing > Virtual Account Summary ). |
| Note | Once the Smart Account is configured, HCM-F synchronizes with CSSM and Satellite and retrieves all the Virtual Account details to HCM-F in Virtual Account Summary window ( Smart Licensing > Virtual Account Summary ). |
| Step 4 | Upgrade the UC applications. License Conversion and Migration to Smart Licensing Unassign the UC clusters from PLM before you upgrade UC clusters to 12.5(x). Navigate to License Management > License Management Summary . Upgrade the UC applications. To upgrade Unified CM and IM and Presence to 12.5(x), see the Upgrade and Migration Guide for Cisco Unified Communications Manager and the IM and Presence Service guide To upgrade Cisco Unity Connection to 12.5(x), see Install, Upgrade, and Maintenance Guide for Cisco Unity Connection Guide . To upgrade Cisco Emergency Responder (CER) to 12.5(x), see Cisco Emergency Responder Administration Guide |
| Step 5 | Register the UC applications to Virtual Account. Update the Cluster Application Version to 12.5(x). Navigate to Cluster Management > Cluster to verify the version. For details, see Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide Note If you are using Unified CDM, ensure the cluster application version is 12.5(x). If the version is less than 12.5(x), update
                                                               the cluster application version to 12.5(x). If you are registering to CSSM by using the proxy mode, then you must set the proxy parameters at the customer and cluster
                                                   level, otherwise the registration fails. For more information about the proxy parameters at cutomer and cluster level, see Add Customer , and Add Cluster sections in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide . Assign a cluster manually to a Virtual Account , if you have not opted for auto registration . Assign the License Mode to HCS for a Virtual Account, navigate to Smart Licensing > Virtual Account Summary . For details, see Assign and Unassign a Cluster to Virtual Account . Note Ensure the licenses are present in the VA in CSSM. | Note | If you are using Unified CDM, ensure the cluster application version is 12.5(x). If the version is less than 12.5(x), update
                                                               the cluster application version to 12.5(x). | Note | Ensure the licenses are present in the VA in CSSM. |
| Note | If you are using Unified CDM, ensure the cluster application version is 12.5(x). If the version is less than 12.5(x), update
                                                               the cluster application version to 12.5(x). |
| Note | Ensure the licenses are present in the VA in CSSM. |
| Step 6 | To check that the product instances are populated correctly and licenses are consumed, log in to Cisco Software Central . |

| Note | Once the Smart Account is configured, HCM-F synchronizes with CSSM and Satellite and retrieves all the Virtual Account details to HCM-F in Virtual Account Summary window ( Smart Licensing > Virtual Account Summary ). |
|---|---|

| Note | If you are using Unified CDM, ensure the cluster application version is 12.5(x). If the version is less than 12.5(x), update
                                                               the cluster application version to 12.5(x). |
|---|---|

| Note | Ensure the licenses are present in the VA in CSSM. |
|---|---|

| Step 1 | From the side menu, select Infrastructure Manager > Smart Licensing > Subscription Mapper . |
|---|---|
| Step 2 | The Subscription Mapper page shows the following information: Select Subscription ID Select the Subscription ID from the drop-down list. Select Customer ID Select the customer name from the drop-down list to which you want to map the Subscription ID. You must map a customer to the Subscription ID to retrieve order details for the specific customer. Select Licensing Model Select the License model from the drop-down list. Fields Description Subscription ID Displays the subscription IDs that are retrieved while HCM-F performs a sync with CSSM and satellite . License Details Displays the number of licenses that are consumed by each subscription ID. Hover over the i icon to see the license details that has the list of license types. Start Date Displays the start date of the license type. This is valid only for Flex licenses. End Date Displays the end date of the license type. This is valid only for Flex licenses. Note For Perpetual licenses Start Date and End date is not valid. Customer Displays the name of the customer to which the Subscription ID is mapped. License Model Displays the model of the license. The supported options are:  Perpetual, Named User, Named User + Perpetual, or Enterprise
                                                         Agreement. | Fields | Description | Subscription ID | Displays the subscription IDs that are retrieved while HCM-F performs a sync with CSSM and satellite . | License Details | Displays the number of licenses that are consumed by each subscription ID. Hover over the i icon to see the license details that has the list of license types. | Start Date | Displays the start date of the license type. This is valid only for Flex licenses. | End Date | Displays the end date of the license type. This is valid only for Flex licenses. Note For Perpetual licenses Start Date and End date is not valid. | Note | For Perpetual licenses Start Date and End date is not valid. | Customer | Displays the name of the customer to which the Subscription ID is mapped. | License Model | Displays the model of the license. The supported options are:  Perpetual, Named User, Named User + Perpetual, or Enterprise
                                                         Agreement. |
| Fields | Description |
| Subscription ID | Displays the subscription IDs that are retrieved while HCM-F performs a sync with CSSM and satellite . |
| License Details | Displays the number of licenses that are consumed by each subscription ID. Hover over the i icon to see the license details that has the list of license types. |
| Start Date | Displays the start date of the license type. This is valid only for Flex licenses. |
| End Date | Displays the end date of the license type. This is valid only for Flex licenses. Note For Perpetual licenses Start Date and End date is not valid. | Note | For Perpetual licenses Start Date and End date is not valid. |
| Note | For Perpetual licenses Start Date and End date is not valid. |
| Customer | Displays the name of the customer to which the Subscription ID is mapped. |
| License Model | Displays the model of the license. The supported options are:  Perpetual, Named User, Named User + Perpetual, or Enterprise
                                                         Agreement. |

| Fields | Description |
|---|---|
| Subscription ID | Displays the subscription IDs that are retrieved while HCM-F performs a sync with CSSM and satellite . |
| License Details | Displays the number of licenses that are consumed by each subscription ID. Hover over the i icon to see the license details that has the list of license types. |
| Start Date | Displays the start date of the license type. This is valid only for Flex licenses. |
| End Date | Displays the end date of the license type. This is valid only for Flex licenses. Note For Perpetual licenses Start Date and End date is not valid. | Note | For Perpetual licenses Start Date and End date is not valid. |
| Note | For Perpetual licenses Start Date and End date is not valid. |
| Customer | Displays the name of the customer to which the Subscription ID is mapped. |
| License Model | Displays the model of the license. The supported options are:  Perpetual, Named User, Named User + Perpetual, or Enterprise
                                                         Agreement. |

| Note | For Perpetual licenses Start Date and End date is not valid. |
|---|---|

| Note | Perpetual licenses might not have Subscription ID. |
|---|---|