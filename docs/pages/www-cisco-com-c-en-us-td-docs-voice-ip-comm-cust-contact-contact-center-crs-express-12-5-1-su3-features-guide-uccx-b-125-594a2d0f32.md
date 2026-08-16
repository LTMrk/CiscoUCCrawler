---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-crs-express-12-5-1-su3-features-guide-uccx-b-125-594a2d0f32
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5_1_su3/features/guide/uccx_b_1251su3_features-guide/uccx_m_1251su2_smart-licensing.html
retrieved_at: 2026-08-16T21:17:28.143964+00:00
---

Cisco Unified Contact Center Express Features Guide, Release 12.5(1) SU3

# Cisco Unified Contact Center Express Features Guide, Release 12.5(1) SU3

Updated: May 7, 2023

Chapter: Smart Licensing

## Chapter: Smart Licensing

# Smart Licensing

## Smart Licensing Overview

Cisco Smart Software Licensing is a flexible software licensing model that streamlines the way you activate and manage Cisco
                              software licenses across your organization. Smart Licenses provide greater insight into software license ownership and consumption,
                              so that you know what you own and how the licenses are being used. The solution allows you to easily track the status of your
                              license and software usage trends. It pools the license entitlements in a single account and allows you to move licenses freely
                              across virtual accounts. Smart Licensing is enabled across most of the Cisco products and managed by a direct cloud-based
                              or mediated deployment model.

Smart Licensing registers the Product Instance, reports license usage, and obtains the necessary authorization from Cisco Smart Software Manager ( Cisco SSM ) or Cisco Smart Software Manager On-Prem ( Cisco SSM On-Prem ) .

You can use Smart Licensing to:

View license usage and count.

View the status of each license type and the product instance.

View the product licenses available on Cisco SSM or Cisco SSM On-Prem .

Register or deregister the Product Instance, renew license authorization and license registration.

Sign in additional agents to Unified CCX up to the maximum limit that is configured in your OVA.

Limit the license consumption up to the purchased quantity or allow the over consumption of the licenses by using Overage
                                    Allowance. For more information on using Overage Allowance, see the Smart License Management section in Cisco Unified Contact Center Express Administration and Operations Guide .

### License Control

Smart Licensing allows you to use more licenses than you have purchased. You will be later asked to deposit the additional
                              licenses in the Smart Account. However, if you want to limit the license usage to the purchased quantity or less, use License Control . With License Control , you can disable Overage Allowance option to restrict the number of agents and ports that can be used in Unified CCX. For different license types, you can restrict
                              the usage of licenses and ports by configuring the following fields:

License Type

Fields

Comments

Perpetual Premium

Agent Seats

Outbound Ports

-

Perpetual Enhanced

Agent Seats

-

Standard Agent Seats

Premium Agent Seats

The type of license (Standard or Premium) consumed by agents is displayed when they log in.

For example, if you have purchased a total of 50 licenses (10 Premium and 40 Standard):

Maximum of 10 Premium agents can sign in, without transitioning to Out of Compliance state .

Maximum of 50 Standard agents can sign in, if none of the Premium agents have signed in, without transitioning to Out of Compliance state .

When 5 Premium agents sign in, you can have maximum of 45 Standard agents sign in, without transitioning to Out of Compliance state .

The total of Standard and Premium agents signed in should be 50, without transitioning to Out of Compliance state .

IP-IVR

IVR Ports

-

For more information about OVA Profiles, see the Server Capacities and Limits section in Solution Design Guide for Cisco Unified Contact Center Express .

License Control is not applicable:

For Non Production Systems License

For Not For Resale License

For License Reservation

## License Management

Smart Licensing can be managed by using Cisco SSM and License Management in Unified CCX Administration portal .

Cisco SSM — Cisco SSM enables you to manage all your Cisco smart software licenses from a centralized website. With Cisco SSM , you organize and view your licenses in groups called virtual accounts (collections of licenses and product instances).

You can access Cisco SSM from https://software.cisco.com , by clicking the Smart Software Licensing link under the License menu.

License Management in Unified CCX Administration portal — Using the License Management option in the Unified CCX Administration portal, you can register or deregister the product instance,
                                 select your license type, set transport settings, or view the licensing consumption summary.

## Smart License Deployments

Direct - Cisco Smart Software Manager ( Cisco SSM )

Cisco Smart Software Manager On-Prem ( Cisco SSM On-Prem )

### Direct - Cisco Smart Software Manager ( Cisco SSM )

The Cisco SSM is a cloud-based service that handles your system licensing. The Product Instance can connect either directly to Cisco SSM or through a proxy server.

Cisco SSM allows you to:

Create, manage, or view virtual accounts.

Manage and track the licenses.

Move licenses across the virtual accounts.

Create and manage Product Instance Registration Tokens.

For more information about Cisco SSM , go to https://software.cisco.com .

### Cisco Smart Software Manager On-Prem ( Cisco SSM On-Prem )

Cisco SSM On-Prem is an on-premises component that can handle your licensing needs. When you choose this option, Unified CCX registers and reports license consumption to the Cisco SSM On-Prem , which synchronizes its database regularly with Cisco SSM that is hosted on cisco.com.

You can use the Cisco SSM On-Prem in either Connected or Disconnected mode, depending on whether the Cisco SSM On-Prem can connect directly to cisco.com.

Configure Transport URL for Cisco SSM On-Prem with Smart Call-Home URL: https://<OnpremCSSM>/Transportgateway/services/DeviceRequestHandler

The <OnpremCSSM> value must match with the SSM Tomcat Certificate Common Name or Subject Alternative Name. In the above URL,
                                          replace <OnpremCSSM> with FQDN or IP, based on the SSM Tomcat Certificate.

Connected —Use when there is connectivity to cisco.com directly from the Cisco SSM On-Prem . Smart account synchronization occurs automatically.

Disconnected —Use when there is no connectivity to cisco.com from the Cisco SSM On-Prem . Cisco SSM On-Prem must synchronize with Cisco SSM manually to reflect the latest license entitlements.

For more information on Cisco SSM On-Prem , see https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager.html .

### New Deployments

For new deployments, buy the licenses on Cisco Commerce website at https://apps.cisco.com . Begin to use the product by using the licenses from your Smart Account.

## License States

Smart Licensing has the following states:

Registration State

Unregistered —Product Instance is unregistered.

Registered —After you purchase the license, you need to register the Product Instance with Cisco SSM . To register with Cisco SSM , generate a registration token from the Cisco SSM portal. Use the registration token to register your Product Instance.

Registration Expired —Product Instance registration has expired because the ID Certificate issued by Cisco SSM is not renewed for more than 12 months. Reregister the Product Instance.

Authorization State

No licenses in use

Evaluation Mode —The Product Instance license has an Evaluation period of 90 days. In the Evaluation period you have unlimited access to the
                                       product with highest set of product capabilities and unlimited number of licenses. You must register the system with Cisco SSM or Cisco SSM On-Prem within 90 days. If the system is not registered before the end of the evaluation period, it will be moved to the Enforcement
                                       state where certain system functions are restricted.

In Compliance —When the license consumption is as per the purchased quantity, the product is compliant.

Evaluation expired —Product Instance evaluation period has expired.

Authorized —Product Instance is in authorized or in compliance state. Authorization is renewed every 30 days.

Out of Compliance —Product Instance reports license usage to Cisco SSM every 8 hours .

If Cisco SSM reports out-of-compliance for the reported value, then the Product Instance is transitioned to Out of Compliance state.

The out-of-compliance period is for 90 days, within which you need to purchase the additional licenses. If you fail to take
                                       corrective action within the 90 days period, the Product Instance is transitioned to the Enforcement state.

Authorization Expired —Product Instance authorization has expired. This usually happens when the product has not communicated with Cisco SSM for more than 90 days. It is in an overage period for 90 days before restrictions are enforced.

Enforcement State

When the 90 day period of Out-of-Compliance, Evaluation Period or Authorization period has expired, the Product Instance is
                                 moved to the Enforcement state in which system operations are impacted for Contact Center components. The Product Instance
                                 is in the Enforcement state in the following scenarios:

Out-of-Compliance expiry —When the out-of-compliance period of 90 days has expired.

Purchase new licenses to exit the Enforcement state.

Authorization expiry —When the Product Instance has not communicated with Cisco SSM or Cisco SSM On-Prem for 90 days and has not automatically renewed the entitlement authorizations.

Renew the license authorizations to exit the Authorization expiry state.

Evaluation expiry —When the license evaluation period of 90 days has expired and the Product Instance is not registered with Cisco SSM .

Register the Product Instance with Cisco SSM to exit the evaluation expiry state.

During the Enforcement mode, synchronization from Unified CM is blocked because of which, any new addition, modification,
                                 or deletion of agents is not synchronized with the Unified CCX system.

A pictorial representation of different license states is as follows:

## Smart Licensing Task Flow

Complete the following tasks to set up licensing after installing Unified CCX 12.5(1). For more information, see Cisco Unified Contact Center Express Admin and Operations Guide .

Steps

Action

Description

Step 1

Obtain the Product Instance Registration Token

Generate a product instance registration token for your virtual account.

For more information, see Obtain the Product Instance Registration Token .

Step 2

Configure Transport Settings for Smart Licensing

Configure the transport settings through which Unified CCX connects to the Smart Licensing service. By default, the Direct connection option is selected, where the product communicates directly with Cisco licensing servers.

Step 3

Register with Cisco SSM

Register Unified CCX with Cisco SSM or Cisco SSM On-Prem .

Complete the following tasks to set up the system licensing after upgrading to Unified CCX 12.5(1) from previous versions.
                              For more information, see Cisco Unified Contact Center Express Admin and Operations Guide .

Steps

Action

Description

Step 1

Migrate to Smart Licensing

From Classic licensing, you can migrate to Smart Licensing. Once you migrate to Smart Licensing, you cannot use Classic Licensing.

If you want to continue using Cisco WFO, you must remain on Classic Licensing as Cisco WFO does not support Smart Licensing.

Step 2

Choose your License Type

The main license types are as follows:

Lab

Production

Select any one of the license types that are listed under these main license types.

Step 3

Configure Transport Settings for Smart Licensing

Configure the transport settings through which Unified CCX connects to the Smart Licensing service. By default, the Direct connection option is selected, where the product communicates directly with Cisco SSM .

Step 4

Register with Cisco SSM

Register with Cisco SSM or Cisco SSM On-Prem .

### Obtain the Product Instance Registration Token

Obtain the product instance registration token from Cisco SSM or Cisco SSM On-Prem to register the product instance. Generate the registration token with or without enabling the Export-Controlled functionality.

The Allow export-controlled functionality on the products that are registered with this token check box does not appear for Smart Accounts that are not permitted to use the Export-Controlled functionality.

Step 1

Log in to your smart account in either Cisco SSM or Cisco SSM On-Prem .

Step 2

Navigate to the virtual account with which you want to associate the product instance.

Step 3

Generate the Product Instance Registration Token.

There is a check box Allow export-controlled functionality on the products registered with this token , which is not applicable for Unified CCX.

Step 4

Copy the generated token. This token is required when registering Smart Licensing with Cisco SSM .

## Smart Licensing Tasks

After you successfully register Smart Licensing, you can perform the following tasks as per the requirement:

Renew Authorization —The license authorization is renewed automatically every 30 days. Use this option to manually renew the authorization.

Renew Registration —The initial registration is valid for one year. Registration is automatically renewed every six months. Use this option to
                                    manually renew the registration.

Reregister —Use this option to forcefully register the product instance again.

Deregister —Use this option to release all the licenses from the current virtual account.

Renew Authorization and Renew Registration are automated tasks that take place at regular intervals. If there is a failure
                              in the automated process, you can manually renew authorization and registration.

For more information, see Smart License Management section in Cisco Unified Contact Center Express Admin and Operations Guide .

## License Consumption Calculation

The system reports peak license usage to Cisco SSM every 8 hours . If  you are seen to have consumed more licenses than you are authorized to, the Product Instance is pushed to the Out-of-Compliance
                           state. The Out-of-Compliance period is for 90 days, within which you need to purchase additional licenses. If you do not take
                           corrective action within the 90 days period, the Product Instance is pushed to the Enforcement state in which, some of the
                           operations are impacted.

Log in to Cisco SSM to view the detailed license consumption. Cisco SSM reports purchased quantity, in-use quantity, and balance licenses. At a quick glance, you can decide if the consumption of
                           your licenses are in deficit or surplus, based on which you can make the right decision on the number of licenses that are
                           required.

## License Computation

Smart Licensing allows you to view the license consumption of your Cisco Unified CCX deployments. License consumption for
                              an agent is computed as per the skills that are configured and login status into Finesse desktop. License consumption is recomputed
                              every 8 hours . The aggregated data for all logged-in agents is sent to Cisco SSM or Cisco SSM On-Prem at fixed time intervals and exists in the Unified CCX database. The license consumption details differ based on the system's
                              license type. The following table lists the various license types, features available for each license type, and data sent
                              to Cisco SSM or Cisco SSM On-Prem .

License Type

Features Available for Agents

Data Stored

Data Reported to Cisco SSM

Perpetual Premium

Inbound Voice, Chat and Email, Outbound Direct Preview, and Outbound Predictive and Progressive.

Number of agents logged in to the system.

Note: All agents are considered as premium agents irrespective of their skill configuration.

Number of Inbound Ports in use.

Number of Outbound Ports and seats in use.

Number of agents logged in to the system.

Number of Outbound Ports in use.

Server license

Perpetual Enhanced

Inbound Voice

Number of agents logged in to the system.

Note : All agents are considered as standard agents.

Number of Inbound Ports in use.

Number of agents logged in to the system.

Server license

Flex

Standard : Inbound Voice and Outbound Direct Preview.

Premium: Inbound Voice, Outbound Direct Preview, Chat and Email, and Outbound Predictive and Progressive.

Number of agents logged in with Standard and Premium licenses during a set time interval.

Number of Inbound Ports in use.

Number of Outbound Ports and seats in use.

Note: If an agent has supervisor capabilities, the agent is using premium feature (applicable for both Standard and Premium). When using Smart License with Flex license type, the Server License Usage reports to 0. The Server or Warm Standby license
                                                   never shows to be a consumed unit; however, it is required to be present.

Number of agents logged in with Standard and Premium licenses during a set time interval.

## Migrate to Smart Licensing

If you have an active SWSS contract, you can migrate your unconsumed PAKs to Smart Licensing on Cisco SSM portal. If you have already consumed your PAK, you can convert your existing licenses on the device to Smart Licensing by
                              using "Device Based Conversion" on LRP tool. First assign the classic PAK to the Smart Account and Virtual Account to move
                              to Smart Licensing.

To migrate from Unified CCX 10.x to Smart Licensing, upgrade to Unified CCX 11.6 and then to Unified CCX 12.5.

There are two types of migration:

PAK-Based Migration

Device-Based Conversion

If the SWSS contract is inactive, repurchase the licenses or move to Flex, and follow the steps to convert classic licenses
                                    to smart licenses.

PUT tool is only for customers who prefer to continue to operate in Classic Licensing mode.

The following table provides the Smart Licensing migration details:

Migration

Description

Fresh Install of 12.5(1)

Place an order on CCW with Smart Account details attached to the order. Licenses get deposited to the Smart Account/Virtual
                                          Account.

Smart Licensing is the only option for new deployments.

Fresh Install of 12.0 and 11.6.x

No change in the ordering and fulfillment process.

Upgrade to 12.5(1)

You get an option to either stay on Classic Licensing or move to Smart Licensing.

Stay on Classic Licensing

With active SWSS contract, upgrade using the PUT tool to receive a PAK, which can be used to generate a Classic Upgrade License.

With SWSS expired, repurchase the licenses or move to Flex and follow the aforementioned step to upgrade to 12.5(1).

Migrate to smart Licensing

Get the 12.5(1) media from Cisco.com with a valid CCO ID.

To upgrade from 10.6, 11.6.x or 12.0 to 12.5(1), use Device Based Conversion (DBC) on LRP (License Registration Portal) to convert licenses on your existing system to Smart Licensing.

Upgrade to 11.6 or 12.0

No change in the upgrade mechanism. Follow the regular upgrade process.

### PAK-Based Migration

Migrate to Smart Licensing for fulfilled, partially fulfilled, and unfulfilled PAKs.

Log in to the Traditional Licensing Portal at https://tools.cisco.com/SWIFT/LicensingUI/Home .

Locate the PAKs that are to be migrated.

Right click and select Assign to Smart Account and Virtual Account .

Select the Smart Account and Virtual Account to which the PAK will be assigned.

Once done, the classic PAKs will show assigned Smart Account.

#### Using LRP

Select the PAK that needs to be converted to smart entitlement.

From the PAK context option, select Convert to Smart Licensing.

Select the SKUs , Quantity to Convert and click on Submit .

Classic Licenses that are partially converted will need new Classic License file for managing the remaining Classic Licenses.

After the licenses are converted to smart entitlements, successful conversion message is shown. The entitlements will be available
                                       on Cisco SSM under selected Smart and Virtual Account.

### Device-Based Conversion

Use the device-based Smart Licensing to convert the Classic licenses to smart entitlements.

#### Using LRP

Login to the Traditional Licensing Portal at https://tools.cisco.com/SWIFT/LicensingUI/Home

Go to Devices tab and then Add Device .

Locate the device to be migrated (filter using the device UUID). Once added, the added device shows up under Devices tab.

Select the device and right click Assign to Smart Account to Smart Account and Virtual Account.

Select the Smart Account and the Virtual Account.

Once done, the table is updated with the Smart Account assigned to the device.

For Classic licenses to be converted to smart entitlements, select the device and select Convert licenses to Smart Licensing option.

Select the SKUs and Quantity to Convert .

Classic Licenses which are partially converted will need new Classic License file for managing the remaining Classic Licenses.

Confirm and click Submit .

Once the licenses are fully converted, the device UUID will be removed from the LRP. Once done, the successful conversion
                                       message is shown. The entitlements will now be available on Cisco SSM under selected Smart and Virtual Account.

## Notifications and Alerts

### Real Time Monitoring Tool (RTMT) Alerts for Unified CCX

Administrators are notified by alerts (on the landing page of Unified CCX Administration and RTMT) and event logs (Sys logs).
                              Administrators are also notified through emails (that are configured in Cisco SSM ) on the status of licenses in the Smart and Virtual Accounts.

Unified CCX uses RTMT client to bring your attention to actions required to effectively manage your smart products and devices.
                              For Smart Licensing, alerts are triggered in the following scenarios:

Renew Authorization—Authorization Failure notification received/timeout

Renew Registration—Renew ID cert failure notification received/timeout

License Computation—Any exception when trying to compute license usage

Entitlement Reporting—Failure to get license type or exception when trying to get entitlements from SDK

System to enter in Out-of-Compliance (OOC)—Current state is OOC but OOC tolerance limit of 45 min is not breached

System to enter in OOC shortly—System is in OOC state for more than 30 min and the OOC tolerance limit of 45 min is not breached.
                                    (System will enter OOC in the next interval of entitlement reporting)

OOC—System in OOC and OOC tolerance limit of 45 min breached

Enforcement Mode—System in enforcement mode

Smart Agent Initialization—Exception when trying to initialize smart agent or Exception when trying to update transport settings
                                    or get entitlement tags

## Best Practices

Some of the best practices for Smart Licensing are:

Before purchasing your licenses, run the License Consumption report on the existing system to understand the consumption pattern
                                 to make the right purchase decisions on the license requirement.

Configure Admin email address in Cisco SSM to receive notifications and alerts from Cisco SSM .

## Specific License Reservation

Devices (Product Instances of Unified CCX) that are registered with Smart Licensing have to share the license information
                              with Cisco Smart Software Manager ( Cisco SSM ) at regular intervals. Customer deployments that cannot periodically share license utilization data with Cisco SSM due to regulatory reasons can use the Specific License Reservation feature. Specific License Reservation is available by default on the smart account.

You can reserve licenses (including add-on licenses) for your product instance on Cisco SSM . Use Unified CCX CLI to enable Specific License Reservation. For more information on the commands, see the Specific License Reservation Commands section in Cisco Unified Contact Center Express Administration and Operations Guide available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-express/products-maintenance-guides-list.html .

You do not have to renew or reauthorize the reserved licenses unless there is a license usage change on the device. License
                                          reservation provides limited functionality to certain Smart Licensing features such as, transfer of licenses between products,
                                          license usage, and asset management.

License Reservation reduces many of the benefits of Smart Licensing including:

Dynamic movement of license consumption between products

Real-time license usage visibility and asset management

Simplified product registration

### License Usage in Specific License Reservation

When an agent signs in, based on the skills that are configured (irrespective of the usage) in the Resource Configuration page in Unified CCX Administration, Standard or Premium license is consumed.

For example, if you have purchased a total of 50 licenses (10 Premium and 40 Standard), the following scenarios are allowed:

A maximum of 10 Premium agents can sign in.

A maximum of 50 Standard agents can sign in, if none of the Premium agents have signed in.

When 5 Premium agents sign in, you can have a maximum of 45 Standard agents sign in. Or when 45 Standard agents sign in, you
                                    can have a maximum of 5 Premium agents sign in.

The total of Standard and Premium agents signed in should be 50.

Over-consumption of licenses is not allowed in Specific License Reservation.

### Enable Specific License Reservation

#### Before you begin

Step 1

Run the license smart reservation enable command to initiate the reservation process.

Step 2

Run the license smart reservation request specific command to get the Reservation Request Code .

Step 3

Log in to Cisco SSM and enter the Reservation Request Code.

Step 4

Select the specific licenses that must be reserved for the product instance.

Step 5

Run the license smart reservation install "<authorization code>" command.

### Modify Specific License Reservation

#### Before you begin

Step 1

Log in to Cisco SSM , update the reserved licenses, and generate a new Authorization Code .

Step 2

Run the license smart reservation install "<authorization code>" command.

Step 3

Use the Confirmation Code in Cisco SSM and update the Specific License Reservation.

### Remove Specific License Reservation

#### Before you begin

Step 1

Run the license smart reservation return command.

Step 2

Use the Reservation Return Code in Cisco SSM .

Step 3

Run the license smart reservation disable command.

Specific License Reservation is removed from the product instance.

| License Type | Fields | Comments |
|---|---|---|
| Perpetual Premium | Agent Seats Outbound Ports | - |
| Perpetual Enhanced | Agent Seats | - |
| Flex | Standard Agent Seats Premium Agent Seats | The type of license (Standard or Premium) consumed by agents is displayed when they log in. For example, if you have purchased a total of 50 licenses (10 Premium and 40 Standard): Maximum of 10 Premium agents can sign in, without transitioning to Out of Compliance state . Maximum of 50 Standard agents can sign in, if none of the Premium agents have signed in, without transitioning to Out of Compliance state . When 5 Premium agents sign in, you can have maximum of 45 Standard agents sign in, without transitioning to Out of Compliance state . The total of Standard and Premium agents signed in should be 50, without transitioning to Out of Compliance state . |
| IP-IVR | IVR Ports | - |

| Note | License Control is not applicable: For Non Production Systems License For Not For Resale License For License Reservation |
|---|---|

| Note | The <OnpremCSSM> value must match with the SSM Tomcat Certificate Common Name or Subject Alternative Name. In the above URL,
                                          replace <OnpremCSSM> with FQDN or IP, based on the SSM Tomcat Certificate. |
|---|---|

| Steps | Action | Description |
|---|---|---|
| Step 1 | Obtain the Product Instance Registration Token | Generate a product instance registration token for your virtual account. For more information, see Obtain the Product Instance Registration Token . |
| Step 2 | Configure Transport Settings for Smart Licensing | Configure the transport settings through which Unified CCX connects to the Smart Licensing service. By default, the Direct connection option is selected, where the product communicates directly with Cisco licensing servers. |
| Step 3 | Register with Cisco SSM | Register Unified CCX with Cisco SSM or Cisco SSM On-Prem . |

| Steps | Action | Description |
|---|---|---|
| Step 1 | Migrate to Smart Licensing | From Classic licensing, you can migrate to Smart Licensing. Once you migrate to Smart Licensing, you cannot use Classic Licensing. If you want to continue using Cisco WFO, you must remain on Classic Licensing as Cisco WFO does not support Smart Licensing. |
| Step 2 | Choose your License Type | The main license types are as follows: Lab Production Select any one of the license types that are listed under these main license types. |
| Step 3 | Configure Transport Settings for Smart Licensing | Configure the transport settings through which Unified CCX connects to the Smart Licensing service. By default, the Direct connection option is selected, where the product communicates directly with Cisco SSM . |
| Step 4 | Register with Cisco SSM | Register with Cisco SSM or Cisco SSM On-Prem . |

| Note | The Allow export-controlled functionality on the products that are registered with this token check box does not appear for Smart Accounts that are not permitted to use the Export-Controlled functionality. |
|---|---|

| Step 1 | Log in to your smart account in either Cisco SSM or Cisco SSM On-Prem . |
|---|---|
| Step 2 | Navigate to the virtual account with which you want to associate the product instance. |
| Step 3 | Generate the Product Instance Registration Token. Note There is a check box Allow export-controlled functionality on the products registered with this token , which is not applicable for Unified CCX. | Note | There is a check box Allow export-controlled functionality on the products registered with this token , which is not applicable for Unified CCX. |
| Note | There is a check box Allow export-controlled functionality on the products registered with this token , which is not applicable for Unified CCX. |
| Step 4 | Copy the generated token. This token is required when registering Smart Licensing with Cisco SSM . |

| Note | There is a check box Allow export-controlled functionality on the products registered with this token , which is not applicable for Unified CCX. |
|---|---|

| License Type | Features Available for Agents | Data Stored | Data Reported to Cisco SSM |
|---|---|---|---|
| Perpetual Premium | Inbound Voice, Chat and Email, Outbound Direct Preview, and Outbound Predictive and Progressive. | Number of agents logged in to the system. Note: All agents are considered as premium agents irrespective of their skill configuration. Number of Inbound Ports in use. Number of Outbound Ports and seats in use. | Number of agents logged in to the system. Number of Outbound Ports in use. Server license |
| Perpetual Enhanced | Inbound Voice | Number of agents logged in to the system. Note : All agents are considered as standard agents. Number of Inbound Ports in use. | Number of agents logged in to the system. Server license |
| Flex | Standard : Inbound Voice and Outbound Direct Preview. Premium: Inbound Voice, Outbound Direct Preview, Chat and Email, and Outbound Predictive and Progressive. | Number of agents logged in with Standard and Premium licenses during a set time interval. Number of Inbound Ports in use. Number of Outbound Ports and seats in use. Note: If an agent has supervisor capabilities, the agent is using premium feature (applicable for both Standard and Premium). When using Smart License with Flex license type, the Server License Usage reports to 0. The Server or Warm Standby license
                                                   never shows to be a consumed unit; however, it is required to be present. | Number of agents logged in with Standard and Premium licenses during a set time interval. |

| Note | PUT tool is only for customers who prefer to continue to operate in Classic Licensing mode. |
|---|---|

| Migration | Description |
|---|---|
| Fresh Install of 12.5(1) | Place an order on CCW with Smart Account details attached to the order. Licenses get deposited to the Smart Account/Virtual
                                          Account. Note Smart Licensing is the only option for new deployments. | Note | Smart Licensing is the only option for new deployments. |
| Note | Smart Licensing is the only option for new deployments. |
| Fresh Install of 12.0 and 11.6.x | No change in the ordering and fulfillment process. |
| Upgrade to 12.5(1) | You get an option to either stay on Classic Licensing or move to Smart Licensing. Stay on Classic Licensing With active SWSS contract, upgrade using the PUT tool to receive a PAK, which can be used to generate a Classic Upgrade License. With SWSS expired, repurchase the licenses or move to Flex and follow the aforementioned step to upgrade to 12.5(1). Migrate to smart Licensing Get the 12.5(1) media from Cisco.com with a valid CCO ID. To upgrade from 10.6, 11.6.x or 12.0 to 12.5(1), use Device Based Conversion (DBC) on LRP (License Registration Portal) to convert licenses on your existing system to Smart Licensing. |
| Upgrade to 11.6 or 12.0 | No change in the upgrade mechanism. Follow the regular upgrade process. |

| Note | Smart Licensing is the only option for new deployments. |
|---|---|

| Note | Classic Licenses that are partially converted will need new Classic License file for managing the remaining Classic Licenses. |
|---|---|

| Note | You do not have to renew or reauthorize the reserved licenses unless there is a license usage change on the device. License
                                          reservation provides limited functionality to certain Smart Licensing features such as, transfer of licenses between products,
                                          license usage, and asset management. License Reservation reduces many of the benefits of Smart Licensing including: Dynamic movement of license consumption between products Real-time license usage visibility and asset management Simplified product registration |
|---|---|

| Note | Over-consumption of licenses is not allowed in Specific License Reservation. |
|---|---|

| Step 1 | Run the license smart reservation enable command to initiate the reservation process. |
|---|---|
| Step 2 | Run the license smart reservation request specific command to get the Reservation Request Code . |
| Step 3 | Log in to Cisco SSM and enter the Reservation Request Code. |
| Step 4 | Select the specific licenses that must be reserved for the product instance. An Authorization Code is generated, which contains a list of entitlement tags and the number of licenses that are reserved for the product instance. |
| Step 5 | Run the license smart reservation install "<authorization code>" command. |

| Step 1 | Log in to Cisco SSM , update the reserved licenses, and generate a new Authorization Code . |
|---|---|
| Step 2 | Run the license smart reservation install "<authorization code>" command. A Confirmation Code is generated. |
| Step 3 | Use the Confirmation Code in Cisco SSM and update the Specific License Reservation. |

| Step 1 | Run the license smart reservation return command. The Reservation Return Code is generated. |
|---|---|
| Step 2 | Use the Reservation Return Code in Cisco SSM . Reserved licenses are returned to the virtual pool. |
| Step 3 | Run the license smart reservation disable command. |