---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-administrat-6e9458da4f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/administration/guide/ucce_b_150_administration-guide-for-cisco-unified-contact-center-enterprise/ucce_m_150_smart-licensing.html
retrieved_at: 2026-08-16T20:43:43.757955+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise Release, 15.0(1)

# Administration Guide for Cisco Unified Contact Center Enterprise Release, 15.0(1)

Updated: July 31, 2026

Chapter: Smart Licensing

## Chapter: Smart Licensing

# Smart Licensing

## Smart Licensing Test

Cisco Smart Software Licensing is a flexible software licensing model that streamlines the way you activate and manage Cisco
                              software licenses across your organization. Smart Licenses provide greater insight into software license ownership and consumption,
                              so that you know what you own and how the licenses are being used. The solution allows you to easily track the status of your
                              license and software usage trends. It pools the license entitlements in a single account and allows you to move licenses freely
                              across virtual accounts. Smart Licensing is enabled across most of the Cisco products and managed by a direct cloud-based
                              or mediated deployment model.

Smart Licensing registers the Product Instance, reports license usage, and obtains the necessary authorization from Cisco Smart Software Manager (Cisco SSM) or Cisco Smart Software Manager On-Prem (Cisco SSM On-Prem) .

You can use Smart Licensing to:

View license usage and count.

View the status of each license type and the product instance.

View the product licenses available on Cisco SSM or Cisco SSM On-Prem.

Register or deregister the Product Instance, renew license authorization and license registration.

View the product version of the active agents.

### Smart Licensing Capabilities

Smart Licensing works in conjunction with Cisco Smart Software Manager ( Cisco SSM ) to intelligently manage product licenses by providing real-time visibility of license status and usage. You can use this
                              data to make better purchase decisions, based on your consumption. Smart Licensing establishes a pool of software licenses
                              or entitlements in Cisco Smart Account.

The Smart Account provides a central location where you can view, store, and manage your licenses, across the organization.
                              You can get access to your software licenses, hardware, and subscriptions through your Smart Account. Smart Accounts are required
                              to access and manage Smart License-enabled products.

Creating a Smart Account is easy and takes less than five minutes. Create a Smart Account on software.cisco.com.

### Documentation Resources

For

Go to...

Smart Licensing Prerequisites

Prerequisites for Smart Licensing

Understanding the License Consumption Calculation

License Consumption Calculation

Migration to Smart Licensing

Migrate to Smart Licensing

Best Practices

Best Practices

### Prerequisites for Smart Licensing

The following are the prerequisites for configuring Smart Licensing:

Smart Licensing Enrollment

Set up Smart and Virtual accounts. For more information, see https://software.cisco.com/#module/SmartLicensing .

Adoption of License Integration Strategy

Decide how you want to connect your product instance to Smart Licensing servers:

On-Cloud: Configure  to connect to Cisco SSM On-Prem

On-Premise:

Deploy the Cisco SSM On-Prem . For instructions on how to do this, see https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager-satellite.html .

Configure  to connect to Cisco SSM On-Prem .

For more information, see Smart License Deployments .

Import the Rogger A certificate into the AW machines

Export Logger/Rogger A certificate and save it by using the url https:<Logger/Roggerhostname>:443

Import the certificate in AW by using the following command:

```
cd %CCE_JAVA_HOME%\bin
```

```
-import keytool.exe <ICM install directory>\ssl\cacerts -file <filepath>.cer -alias <alias>
```

Enter the truststore password when prompted.

Enter 'Yes' when prompted to trust the certificate.

Restart the Tomcat service.

### Smart License Deployments

Direct - Cisco Smart Software Manager ( Cisco SSM )

Cisco Smart Software Manager On-Prem ( Cisco SSM On-Prem )

#### Direct - Cisco Smart Software Manager ( Cisco SSM )

The Cisco SSM is a cloud-based service that handles your system licensing. The Product Instance can connect either directly to Cisco SSM or through a proxy server.

Cisco SSM allows you to:

Create, manage, or view virtual accounts.

Manage and track the licenses.

Move licenses across the virtual accounts.

Create and manage Product Instance Registration Tokens.

For more information about Cisco SSM , go to https://software.cisco.com .

#### Cisco Smart Software Manager On-Prem ( Cisco SSM On-Prem )

Cisco SSM On-Prem is an on-premises component that can handle your licensing needs. When you choose this option,  registers and reports license
                                 consumption to the Cisco SSM On-Prem , which synchronizes its database regularly with Cisco SSM that is hosted on cisco.com.

You can use the Cisco SSM On-Prem in either Connected or Disconnected mode, depending on whether the Cisco SSM On-Prem can connect directly to cisco.com.

Unified CCE 15.0(1) supports the latest on-prem version of Cisco SSM version 9 release 202410 or 9.x.

The <OnpremCSSM> value must match with the SSM Tomcat Certificate Common Name or Subject Alternative Name. In the above URL,
                                             replace <OnpremCSSM> with FQDN or IP, based on the SSM Tomcat Certificate.

Connected —Use when there is connectivity to cisco.com directly from the Cisco SSM On-Prem . Smart account synchronization occurs automatically.

Disconnected —Use when there is no connectivity to cisco.com from the Cisco SSM On-Prem . Cisco SSM On-Prem must synchronize with Cisco SSM manually to reflect the latest license entitlements.

For more information on Cisco SSM On-Prem , see https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager.html .

#### Configure Transport URL for Cisco Smart Software Manager On-Prem with Smart Transport URL

Use the following Smart Transport URL in Cisco SSM On-Prem:

```
https://<FQDN of OnpremCSSM>/SmartTransport
```

Certificate Exchange for TLS/Secured Communication

Import the TLS certificate into the security trust store located at c:\<ICM install directory>\ssl\cacerts . By default, the Cisco SSM On-Prem or Satellite server uses the Cisco Root CA for the TLS certificate. However, this may
                                 differ if the SSM On-Prem is configured to use certificates issued by your own CA.

To import Cisco Root CA into the security trust store, do the following:

Download the onprem.zip file from the following URL:

https://software.cisco.com/download/home/268439622/type/280840583/release/15.0(1)

Extract the certificate from the ZIP file and save it to a directory.

Run the following keytool command for the Smart Transport URL to import the certificate:

```
cd %CCE_JAVA_HOME%\bin
keytool.exe –keystore <ICM install directory>\ssl\cacerts -trustcacerts -import -file <path where the Root, or Intermediate certificate are stored> -alias <Root_name of your CA or Intermediate_name of your CA> -storepass changeit
keytool.exe –keystore %CCE_JAVA_HOME%\lib\security\cacerts -trustcacerts -import -file <path where the Root, or Intermediate certificate are stored> -alias <Root_name of your CA or Intermediate_name of your CA> -storepass changeit
```

Import the downloaded certificate to the Cisco SSM On-Prem.

For more information, see Cisco Smart Software Manager On-Prem User Guide .

#### Configure Transport URL for Cisco SSM On-Prem with Smart Call-Home URL

Use the following Smart Call-Home URL in Cisco SSM On-Prem:

https://<OnpremCSSM>/Transportgateway/services/DeviceRequestHandler

## Smart Licensing Task Flow

Complete these tasks to set up smart licensing for .

Steps

Action

Description

Step 1

Create your Smart Account

Use the Smart Account to organize licenses according to your needs. To create a Smart Account, go to http://software.cisco.com

After the Smart Account is created, Cisco SSM creates a default Virtual Account for this Smart Account. You can use the default account or create other Virtual Accounts.

Step 2

Obtain the Product Instance Registration Token

Generate a product instance registration token for your virtual account.

For more information, see Obtain the Product Instance Registration Token .

Step 3

Configure Transport Settings for Smart Licensing

Configure the transport settings through which  connects to the Cisco SSM or Cisco SSM On-Prem .

For more information, see Configure Transport Settings for Smart Licensing .

Step 4

Select the License Type

Select the License Type before registering the product instance.

For more information, see License Types .

Step 5

Register with Cisco SSM

You can register  with Cisco SSM or Cisco SSM On-Prem .

For more information, see Register with Cisco Smart Software Manager .

After performing the above steps, wait for 10-15 minutes for the correct status to get reflected in the UI. There is no need
                                       to restart the services.

### Obtain the Product Instance Registration Token

Obtain the product instance registration token from Cisco SSM or Cisco SSM On-Prem to register the product instance. Generate the registration token with or without enabling the Export-Controlled functionality.

The Allow export-controlled functionality on the products that are registered with this token check box does not appear for Smart Accounts that are not permitted to use the Export-Controlled functionality.

Step 1

Log in to your smart account in either Cisco SSM or Cisco SSM On-Prem .

Step 2

Navigate to the virtual account with which you want to associate the product instance.

Step 3

Generate the Product Instance Registration Token.

Select the Allow export-controlled functionality on the products registered with this token check box to turn on the Export-Controlled functionality for a product instance you want in this smart account. When you
                                                               select this check box and accept the terms, you enable higher levels of encryption for products that are registered with this
                                                               registration token. By default, this check box is selected.

Use this option only if you are compliant with the Export-Controlled functionality.

Step 4

Copy the generated token. This token is required when registering Smart Licensing with Cisco SSM .

### Configure transport settings for smart licensing

Configure the connection mode between  and Cisco SSM .

Step 1

Select one of the following transport methods:

Smart Call Home (Deprecated)

Smart Transport

With the deprecation of Smart Call Home , it is recommended that you select Smart Transport as the transport mode to fully leverage the features and functionalities that Smart Licensing offers.

Step 2

Select the connection mode to Cisco SSM:

Direct (Product communicates directly with Cisco's licensing servers)

Smart Call Home URL : "https://tools.cisco.com/its/service/oddce/services/DDCEService"

Smart Transport URL : "https://smartreceiver.cisco.com/licservice/license"

This is the default option. The configured URL is displayed.

Transport gateway (Proxy Gateway via Transport Gateway or Cisco Smart Software Manager)

URL: Enter the appropriate URL.

HTTP/HTTPS proxy (Send data via an intermediate HTTP or HTTPS proxy)

Enter appropriate Host Name and Port .

Step 3

Click Save to save the settings.

### Select License Type

Smart Licensing offers two types of license—Flex and Perpetual and it also provides two different usage modes—Production and
                                 Non-Production.

Flex —Flex license is a recurring subscription of Standard and Premium license. These subscriptions are renewed periodically, for
                                       example 1, 3, or 5 years.

Perpetual —Perpetual license is a permanent and one-time payment license that offers a Premium license.

Production —Production mode is when the licenses are used on live systems to handle actual production traffic. Yes

Non-Production —Non-production mode is used for labs, testing and/or staging areas, and not for live systems handling actual end-consumer
                                       traffic.

If you select the incorrect license type, the product instance is placed in the Out-of-Compliance state. If this issue is
                                             unresolved, the product instance is placed in the Enforcement state where the system operations are impacted.

If you select the Deployment Type as Unified CCE Rogger/Logger , the system automatically updates to Perpetual even when the License Type is configured as Flex .

Step 1

Click License Type .

Step 2

Select the License Type and the Usage Mode corresponding to what you have purchased before registering the product instance.

The following table lists the license types and licenses offered as part of Unified CCE and Packaged CCE Smart Licensing:

License Type

Licenses

Flex Production

Unified CCE and Packaged CCE:

Standard Agent

Premium Agent

Dialer Ports

Server License

Perpetual Production

Unified CCE and Packaged CCE:

Premium Agent

Dialer Ports

Server License

Unified CCE:

Regular Agent

Third-party IVR licenses

Server License

Perpetual Non-Production

Regular Agent

Premium Agent

Dialer Ports

Server License

Step 3

Click Save .

### Register with Cisco Smart Software Manager

The product instance has 90 days of evaluation period, within which, the registration must be completed. Else, the product
                                 instance gets into the enforcement state.

Register your product instance with Cisco SSM or Cisco SSM On-Prem to exit the Evaluation or Enforcement state.

After you register the product instance, you cannot change the license type. To change the license type, deregister the product
                                             instance.

After you register the product instance, you can change the Transport Mode type from Smart Call Home to Smart Transport and vice-versa. You must make the changes from the Transport Settings page and save it.

Step 1

In , navigate to Overview > Infrastructure Settings > License Management.

Step 2

Click Register .

Before you register the product instance, ensure to select the License Type and the communication mechanism in Transport Settings .

Step 3

In the Smart Software Licensing Product Registration dialog box, paste the product instance registration token that you generated from Cisco SSM or Cisco SSM On-Prem .

Step 4

Click Register to complete the registration process.

After registration, the Smart Licensing Status displays the following details.

Smart License Status

Description

On Unsuccessful Registration

Registration Status

Unregistered

License Authorization Status

Evaluation

Export-Controlled Functionality

Not Allowed

On Successful Registration

Registration Status

Registered (Date and time of registration)

The date and time indicate the server's time zone.

License Authorization Status

Authorized (Date and time of authorization)

The date and time indicate the server's time zone.

Export-Controlled Functionality

Not Allowed

Smart Account

The name of the smart account

Virtual Account

The name of the virtual account

Product Instance Name

The name of the product instance

Serial Number

The serial number of the product instance

Entitlements are a set of privileges customers and partners receive when purchasing a Cisco service agreement. Using Smart
                                             Licensing, you can view the License consumption summary for the entitlements of different license types. The License consumption
                                             summary displays the License Name, Usage Count, and Status against each entitlement name.

You can update or purchase entitlements on the Cisco Commerce website. For more information, see https://apps.cisco.com/Commerce/ .

### Registration, Authorization, and Entitlement Status

#### Registration Status

This table explains the  registration status for Smart Licensing in the  Administration portal:

Status

Description

Unregistered

Product is unregistered.

Registered

Product is registered. Registration is automatically renewed every six months.

Registration Expired

Product registration has expired because the ID Certificate issued by Cisco SSM is not renewed for more than 12 months.

#### Authorization Status

This table describes the possible  authorization status for Smart Licensing in the  Administration portal:

Status

Description

Evaluation state

Product is not registered with Cisco.

Evaluation Expired

Product evaluation period has expired.

Authorized

Product is in authorized or in compliance state. Authorization is renewed every 30 days.

Authorization Expired

Product authorization has expired. This usually happens when the product has not communicated with Cisco for 90 days. It is
                                             in an overage period for 90 days before enforcing restrictions.

Out-of-Compliance

Product is in out-of-compliance state because of insufficient licenses. It is in an overage period for 90 days before enforcing
                                             restrictions.

Unauthorized

Product is unauthorized.

No License in Use

No Licenses are in use.

#### License Entitlement Status

This table describes the possible  instance license entitlement status for Smart Licensing in the  Administration portal:

Status

Status Description

Authorization Expired

Product authorization has expired, when the product has not communicated with Cisco for 90 days.

Not Authorized

Product instance is not authorized.

Evaluation state

Product is not registered with Cisco.

Evaluation Expired

Product evaluation period has expired.

In Compliance

Product is in authorized or in compliance state. Authorization is renewed every 30 days.

ReservedInCompliance

Entitlement is in compliance with the installed reservation authorization code.

Out-of-Compliance

Product is in out-of-compliance state because of insufficient licenses. It is in an overage period for 90 days before enforcing
                                          restrictions.

Not Applicable

Entitlement is not applicable.

Invalid

Error condition state.

Invalid Tag

Entitlement tag is invalid.

No License in Use

Entitlement is not in use.

Waiting

Waiting for an entitlement request's response from Cisco SSM or Cisco SSM On-Prem .

Disabled

Product instance is deactivated or disabled.

### Out-Of-Compliance and Enforcement Rules

#### Out-of-Compliance

The Product Instance reports license usage to Cisco SSM every 15 minutes. If your license consumption exceeds the entitlements for five consecutive reporting intervals, the Product
                                 Instance is transitioned to the Out-of-Compliance state by CSSM. The Out-of-Compliance period is for 90 days, within which
                                 you need to purchase the additional licenses. If you fail to take corrective action within the 90 days period, the Product
                                 Instance is pushed to the Enforcement state.

All CVPs in a virtual account share the licenses from a pool. If the license consumption exceeds than those available in the
                                 pool, all CVPs in the virtual account follow the Out-of-Compliance and Enforcement rules.

#### Enforcement

The Product Instance is in the Enforcement state in the following scenarios:

Out-of-Compliance expiry : When the Out-of-Compliance period of 90 days has expired.

Purchase new licenses to exit the Enforcement state.

Authorization expiry : When the Product Instance has not communicated with Cisco SSM or Cisco SSM On-Prem for 90 days and has not automatically renewed the entitlement authorizations.

Renew the license authorizations to exit the authorization expiry state.

Evaluation expiry : When the license evaluation period of 90 days has expired and the Product Instance is not registered with Cisco SSM .

Register the Product Instance with Cisco SSM to exit the Evaluation expiry state.

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

Out of Compliance —Product Instance reports license usage to Cisco SSM every 15 minutes . If your license consumption is more than the entitlements for five consecutive reporting intervals, the Product Instance is
                                          transitioned to the Out of Compliance state by CSSM.

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

A pictorial representation of different license states is as follows:

## Notifications and Alerts

The system maintains real-time status of license usage after Product Instances are registered and activated. Administrators
                           are notified through alerts, event logs, and emails on the status of licenses in the Smart and Virtual Accounts. Pay attention
                           to system alerts and banners to get regular information on compliance status and take necessary action.

Following are some of the notification methods:

Banner Notifications

System Alerts

Banner Notifications

The banner displays the aggregate license compliance status on the  Administration portal. The banner is displayed only when
                                 any of the product instances in the deployment is in the Evaluation, Out-of-Compliance, or Enforcement state.

The License Compliance report displays the license status of product instances in the deployment. The reporting hierarchy is Enforcement, Out-of-Compliance,
                                 and Evaluation. This means that if any of the product instances in the deployment is in the Enforcement state, the banner
                                 displays Enforcement state as the overall status. Click the Learn More option to view the consolidated License Compliance report .

When licenses are consumed in a Non-Production System, a banner message, "You are using a Non-Production System”, is displayed.

System Alerts

Smart Licensing related system alerts, which get auto-corrected, are displayed in  Administration portal when:

Smart License state is not initialized

Smart Agent is not enabled

Serial number is not generated

In the above conditions, a red system alert is displayed in the Alerts button on the  Administration portal. The red circle against the name of the machine in the inventory indicates the identified
                           issue and the immediate action needed. After the issue is resolved, a green circle against the name of the machine indicates
                           the system is running fine, for example, when the Smart Agent is enabled or Smart License state is initialized.

## License Consumption Calculation

The system reports peak license usage to Cisco SSM every 15 minutes . If in five consecutive reports you are seen to have consumed more licenses than you are authorized to, the Product Instance is pushed to the Out-of-Compliance
                           state. The Out-of-Compliance period is for 90 days, within which you need to purchase additional licenses. If you do not take
                           corrective action within the 90 days period, the Product Instance is pushed to the Enforcement state in which, some of the
                           operations are impacted.

Log in to Cisco SSM to view the detailed license consumption. Cisco SSM reports purchased quantity, in-use quantity, and balance licenses. At a quick glance, you can decide if the consumption of
                           your licenses are in deficit or surplus, based on which you can make the right decision on the number of licenses that are
                           required.

### License Computation Scenario 1

License purchased: 100 licenses

If Cisco SSM registers consecutive five instances of license over usage, the Product Instance transitions to Out-of-Compliance.
                              Thereafter, the Product Instance reports Locked usage quantity (130 in the above scenario) until the deficit licenses (130-100=30)
                              are purchased. The Locked usage is the highest number of license usage (130) in the Out-of-Compliance state. The Product Instance
                              will not report the actual license usage when the Product Instance is in the Out-of-Compliance state.

Purchase additional licenses from the Cisco Commerce website (CCW) to exit the Out-of-Compliance state.

Reported Usage column in the License Management page displays the locked usage quantity. However, the actual license usage is available in the License Consumption report of CUIC.

### License Computation Scenario 2

If Cisco SSM reports only two consecutive instances of license over usage within a one-hour window, the Product Instance will not transition
                              to Out-of-Compliance. For example:

License Purchased: 100 licenses

In the example, the Product Instance is back to In-compliance state after two instances of overage. The next time the Product
                              Instance goes Out-of-Compliance, the count will be 1 of 5. So, you get 45 min (after the first Out-of-Compliance notification
                              from Cisco SSM ) to bring back the consumption within the acceptable range to stay in the In-compliance state.

To know about the agent license that is consumed by the Standard and Premium licenses, see the Cisco Collaboration Flex Plan Contact Center Data Sheet at https://www.cisco.com/c/en/us/products/collateral/unified-communications/cisco-collaboration-flex-plan/datasheet-c78-741220.html

### License Consumption: Premium vs. Standard Agents

Smart Licensing provides insight into the software license consumption, offering clarity on what you own and how it is being
                              used. License consumption for an agent is determined based on the features, roles configured, and the agent's login status
                              on the Cisco Finesse desktop. For example, when an agent signs in to Cisco Finesse and handles task injected through Webex
                              Connect or Enterprise Chat and Email, the system consumes a Premium license.

When agents log into non-voice or digital channel MRDs using non-Cisco third party applications, the system consumes only
                                          a Standard  license.

License consumption is computed periodically. The aggregated data for all logged-in agents is stored in the Unified CCE database and sent to Cisco SSM or Cisco SSM On-Prem at fixed intervals.

Cisco Smart Licensing reflects the actual usage of Premium and Standard agent usage based on features and roles configured
                              as per the Cisco Collaboration Flex 3.0 Licensing Plan. For more information about the list of entitled features consumed
                              by the Standard and Premium agent, see the Cisco Collaboration Flex 3.0 Contact Center Data Sheet at https://www.cisco.com/c/en/us/products/collateral/customer-collaboration/collab-flex-3-contact-center-ds.html#PackagedContactCenterEnterprisePCCE .

The premium license is specifically consumed during the following scenarios:

When an agent assigned the supervisor role logs into the Cisco Finesse desktop.

When an agent logs into the Cisco Finesse desktop and handles Outbound Predictive or Progressive campaign calls.

When an agent signs in and handles digital channel tasks using Enterprise Chat and Email or Webex Connect.

For more information about the number of Standard vs Premium Agents logged into the CCE system in a given reporting interval
                              or the instantaneous value in real time, see the System_Capacity_Interval and System_Capacity_Real_Time topics in Database Schema Handbook for Cisco Unified Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-technical-reference-list.html .

## New Deployments

For new deployments, buy the licenses on Cisco Commerce website at http://www.cisco.com/c/en/us/products/abt_sw.html . Begin to use the product by using the licenses from your Smart Account.

## Migrate to Smart Licensing

### PAK-Based Migration

Migrate to Smart Licensing for fulfilled, partially fulfilled, and unfulfilled PAKs, and its only applicable to Unified CVP.

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

#### Using Cisco SSM

Convert PAKs to equivalent Smart Licenses.

Go to the Convert PAKs tab.

Assigned PAKs are listed on the Cisco SSM portal.

Click Convert to Smart License in the Actions column.

Select SKUs and Quantity to Convert and click Next .

Classic Licenses which are partially converted will need new Classic License file for managing the remaining Classic Licenses.

Once converted to Smart Entitlement, the old classic licenses will be invalidated. Converted Smart Licenses are added into
                                       the Smart Account and the Virtual Account.

### Device-Based Conversion

Use the device-based Smart Licensing to convert the Classic licenses to smart entitlements and its only applicable to Unified
                              CVP.

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

#### Using Cisco SSM

Assigned Devices show up on the Cisco SSM Portal. The Cisco SSM portal is refreshed every hour. If the assigned device is
                                 not visible in Cisco SSM, please recheck after an hour.

Go to Convert Licenses tab and click the License Conversion wizard.

Select the Product family and provide the device UUID.

Select the SKU and Quantity to Convert .

Classic Licenses which are partially converted will need new License file for managing the remaining Classic Licenses.

Review, Confirm and click Submit.

When the conversion is complete and smart licenses are active, the classic licenses are invalidated.

## License Management

Smart Licensing can be managed by using Cisco SSM and .

Cisco SSM — Cisco SSM enables you to manage all your Cisco smart software licenses from a centralized website. With Cisco SSM , you organize and view your licenses in groups called virtual accounts (collections of licenses and product instances).

You can access Cisco SSM from https://software.cisco.com , by clicking the Smart Software Licensing link under the License menu.

## Smart Licensing Tasks

After you successfully register Smart Licensing, you can perform the following tasks as per the requirement:

Renew Authorization —The license authorization is renewed automatically every 30 days. Use this option to manually renew the authorization.

Renew Registration —The initial registration is valid for one year. Registration is automatically renewed every six months. Use this option to
                                    manually renew the registration.

Reregister —Use this option to forcefully register the product instance again.

Deregister —Use this option to release all the licenses from the current virtual account.

Renew Authorization and Renew Registration are automated tasks that take place at regular intervals. If there is a failure
                              in the automated process, you can manually renew authorization and registration.

You have to Deregister and Reregister manually.

### Renew Authorization

The license authorization is renewed automatically every 30 days. The authorization status expires after 90 days if the product
                                 is not connected to Cisco SSM or Cisco SSM On-Prem .

Use this procedure to manually renew the License Authorization Status for all the licenses listed in the License Type.

Step 1

In , navigate to Overview > Infrastructure Settings > License Management.

Step 2

Click Action > Renew Authorization .

This process takes a few seconds to renew the authorization and close the window.

### Renew Registration

Use this procedure to manually renew your certificates.

The initial registration is valid for one year. Renewal of registration is automatically done every six months, provided the
                                 product is connected to Cisco SSM or Cisco SSM On-Prem .

Step 1

In , navigate to Overview > Infrastructure Settings > License Management .

Step 2

Click Action > Renew Registration .

This process takes a few seconds to renew the authorization and close the window.

### Reregister License

Product can migrate to a different virtual account when reregistering with the token from a new virtual account.

Step 1

In , navigate to Overview > Infrastructure Settings > License Management.

Step 2

Click Action > Reregister .

Step 3

In the Smart Software Licensing Product Registration dialog box, paste the copied or saved Registration Token Key that you generated using the Cisco SSM or Cisco SSM On-Prem in the Product Instance Registration Token text box.

Step 4

Click Reregister to complete the reregistration process.

Step 5

Close the window.

### Deregister License

If  is unable to connect to Cisco SSM or Cisco SSM On-Prem , and the product is deregistered, then a confirmation message notifies you to remove the product manually from Cisco SSM or Cisco SSM On-Prem to free up licenses.

After deregistering, the product reverts to the Evaluation state if the evaluation period is not expired. All the license
                                             entitlements that are used for the product are immediately released to the virtual account and are available for other product
                                             instances to use them.

Step 1

In , navigate to Overview > Infrastructure Settings > License Management .

Step 2

Click Action > Deregister .

Step 3

On the Confirm Deregistration dialog box, click Yes to deregister.

## Best Practices

Some of the best practices for Smart Licensing are:

Before purchasing your licenses, run the License Consumption report on the existing system to understand the consumption pattern
                                 to make the right purchase decisions on the license requirement.

Configure Admin email address in Cisco SSM to receive notifications and alerts from Cisco SSM .

## Specific License Reservation

Devices (product instances of Unified CCE ) that register with Smart Licensing have to share the license information with Cisco Smart Software Manager ( Cisco SSM ) at regular intervals. Your deployments that cannot periodically share license utilization data with Cisco SSM or due to regulatory reasons can use the Specific License Reservation feature. Cisco offers license reservation as an on-request configuration for such product instances.

You can reserve licenses (including add-on licenses) for your product instance on Cisco SSM . Specific License Reservation is enabled through the option License Management in the Unified CCE Administration Console.

The reserved licenses require no renewal or reauthorization unless there is a license usage change on the device. License
                                       reservation provides limited functionality to certain Smart Licensing features such as transfer of licenses between products,
                                       license usage, and asset management.

The Specific License Reservation (SLR) feature does not offer the following benefits that are available as part of the Smart
                                       Licensing feature:

Dynamic movement of license consumption between products

Real-time license usage visibility and asset management

Simplified product registration

## System Setting for Unified CCE Deployment

The system can support a defined call capacity based on the deployment model. Exceeding the supported rate of incoming calls
                              degrades performance and can result in late calls, dropped calls, delivery of new incoming calls, the time out of requests,
                              and potential system failures. (Call transfers are permitted.)

The System Information tool enforces limits to protect against overloading the system and establishes continuous monitoring
                              of the incoming call rate according to the configured settings.

To configure miscellaneous call settings. Navigate to Unified CCE Administration > Call Settings > Miscellaneous page.

To view the Miscellaneous page, the signed in user must have System Information enabled in the Feature control set.

For more information on creating a Feature Control Set, see Feature Control at Configuration Guide for Cisco Unified CCE Enterprise

Enter values on this tool to define system-level settings for congestion control.

Treatment Mode

This field shows the treatment mode that is currently in place. You can make a selection from the drop-down menu options to
                                          indicate how congestion is to be handled and how the caller is to be treated. The first three options send the call to an
                                          external VRU. The last two options terminate the call.

Treat call with DN Default Label

Treat call with Routing client default label

Treat call with System default label

Terminate with Dialog Fail/RouteEnd

Release Message to the Routing client

If you select Treat call with DN Default Label, or Treat call with Routing client default label, you see this message: The target call treatment system should be outside of the CCE system . This means that the call will be sent to an external VRU for VRU treatment.

System Default Label

This field is required when Treat call with System default label is the selection for Congestion Treatment Mode. Enter a label
                                          for the system default. This field allows a maximum of 32 characters.

Maximum Calls Per Second

This field displays the current value for maximum calls per second for the deployment. If this field has been set to a number
                                          other than the default, click the X to restore the deployment type default.

Congestion Control Enabled

Check this check box to enable congestion control and make all other fields editable.

Extended Event Detail

Check this check box to enable extended agent event detail.

The extended agent event detail capabilities are supported only for 36000 agent deployment.

Session Inactivity Timer

To set the inactivity timer for the active session, enter the value in minutes. The minimum is 15 minutes and the maximum
                                          is 1440 minutes. The default is 30 minutes. When you relogin, the system automatically deletes the inactivity timer value
                                          that you had set for the previous session.

## Product Version Reporting to Cisco SSM

Smart Licensing reports license entitlements to Cisco SSM. Additionally, the product's version details are also sent to Cisco
                           SSM. The version reporting functionality is enabled by default. You can access Cisco SSM from https://software.cisco.com , by clicking the Smart Software Licensing link under the License menu to find the entitlement details.

To prevent the smart agent from reporting the product's version details, create a registry value named DisableSmartLicenseVersionReporting with the type REG_SZ in the following path:

HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\SystemSettings

If this registry value is set to true , the version details will not be reported to the Cisco SSM.

### Customers Also Viewed

- Configure Webex AI Agent for CCE

| For | Go to... |
|---|---|
| Smart Licensing Prerequisites | Prerequisites for Smart Licensing |
| Understanding the License Consumption Calculation | License Consumption Calculation |
| Migration to Smart Licensing | Migrate to Smart Licensing |
|  |  |
| Best Practices | Best Practices |

| Note | Unified CCE 15.0(1) supports the latest on-prem version of Cisco SSM version 9 release 202410 or 9.x. |
|---|---|

| Note | The <OnpremCSSM> value must match with the SSM Tomcat Certificate Common Name or Subject Alternative Name. In the above URL,
                                             replace <OnpremCSSM> with FQDN or IP, based on the SSM Tomcat Certificate. |
|---|---|

| Steps | Action | Description |
|---|---|---|
| Step 1 | Create your Smart Account | Use the Smart Account to organize licenses according to your needs. To create a Smart Account, go to http://software.cisco.com After the Smart Account is created, Cisco SSM creates a default Virtual Account for this Smart Account. You can use the default account or create other Virtual Accounts. |
| Step 2 | Obtain the Product Instance Registration Token | Generate a product instance registration token for your virtual account. For more information, see Obtain the Product Instance Registration Token . |
| Step 3 | Configure Transport Settings for Smart Licensing | Configure the transport settings through which  connects to the Cisco SSM or Cisco SSM On-Prem . For more information, see Configure Transport Settings for Smart Licensing . |
| Step 4 | Select the License Type | Select the License Type before registering the product instance. For more information, see License Types . |
| Step 5 | Register with Cisco SSM | You can register  with Cisco SSM or Cisco SSM On-Prem . For more information, see Register with Cisco Smart Software Manager . |

| Note | After performing the above steps, wait for 10-15 minutes for the correct status to get reflected in the UI. There is no need
                                       to restart the services. |
|---|---|

| Note | The Allow export-controlled functionality on the products that are registered with this token check box does not appear for Smart Accounts that are not permitted to use the Export-Controlled functionality. |
|---|---|

| Step 1 | Log in to your smart account in either Cisco SSM or Cisco SSM On-Prem . |
|---|---|
| Step 2 | Navigate to the virtual account with which you want to associate the product instance. |
| Step 3 | Generate the Product Instance Registration Token. Note Select the Allow export-controlled functionality on the products registered with this token check box to turn on the Export-Controlled functionality for a product instance you want in this smart account. When you
                                                               select this check box and accept the terms, you enable higher levels of encryption for products that are registered with this
                                                               registration token. By default, this check box is selected. Use this option only if you are compliant with the Export-Controlled functionality. | Note | Select the Allow export-controlled functionality on the products registered with this token check box to turn on the Export-Controlled functionality for a product instance you want in this smart account. When you
                                                               select this check box and accept the terms, you enable higher levels of encryption for products that are registered with this
                                                               registration token. By default, this check box is selected. Use this option only if you are compliant with the Export-Controlled functionality. |
| Note | Select the Allow export-controlled functionality on the products registered with this token check box to turn on the Export-Controlled functionality for a product instance you want in this smart account. When you
                                                               select this check box and accept the terms, you enable higher levels of encryption for products that are registered with this
                                                               registration token. By default, this check box is selected. Use this option only if you are compliant with the Export-Controlled functionality. |
| Step 4 | Copy the generated token. This token is required when registering Smart Licensing with Cisco SSM . |

| Note | Select the Allow export-controlled functionality on the products registered with this token check box to turn on the Export-Controlled functionality for a product instance you want in this smart account. When you
                                                               select this check box and accept the terms, you enable higher levels of encryption for products that are registered with this
                                                               registration token. By default, this check box is selected. Use this option only if you are compliant with the Export-Controlled functionality. |
|---|---|

| Step 1 | Select one of the following transport methods: Smart Call Home (Deprecated) Smart Transport Note With the deprecation of Smart Call Home , it is recommended that you select Smart Transport as the transport mode to fully leverage the features and functionalities that Smart Licensing offers. | Note | With the deprecation of Smart Call Home , it is recommended that you select Smart Transport as the transport mode to fully leverage the features and functionalities that Smart Licensing offers. |
|---|---|---|---|
| Note | With the deprecation of Smart Call Home , it is recommended that you select Smart Transport as the transport mode to fully leverage the features and functionalities that Smart Licensing offers. |
| Step 2 | Select the connection mode to Cisco SSM: Direct (Product communicates directly with Cisco's licensing servers) Smart Call Home URL : "https://tools.cisco.com/its/service/oddce/services/DDCEService" Smart Transport URL : "https://smartreceiver.cisco.com/licservice/license" This is the default option. The configured URL is displayed. Transport gateway (Proxy Gateway via Transport Gateway or Cisco Smart Software Manager) URL: Enter the appropriate URL. HTTP/HTTPS proxy (Send data via an intermediate HTTP or HTTPS proxy) Enter appropriate Host Name and Port . |
| Step 3 | Click Save to save the settings. Figure 1. Transport Settings |

| Note | With the deprecation of Smart Call Home , it is recommended that you select Smart Transport as the transport mode to fully leverage the features and functionalities that Smart Licensing offers. |
|---|---|

| Note | If you select the incorrect license type, the product instance is placed in the Out-of-Compliance state. If this issue is
                                             unresolved, the product instance is placed in the Enforcement state where the system operations are impacted. |
|---|---|

| Note | If you select the Deployment Type as Unified CCE Rogger/Logger , the system automatically updates to Perpetual even when the License Type is configured as Flex . |
|---|---|

| Step 1 | Click License Type . The Select License Type page is displayed. |
|---|---|
| Step 2 | Select the License Type and the Usage Mode corresponding to what you have purchased before registering the product instance. The following table lists the license types and licenses offered as part of Unified CCE and Packaged CCE Smart Licensing: License Type Licenses Flex Production Unified CCE and Packaged CCE: Standard Agent Premium Agent Dialer Ports Server License Perpetual Production Unified CCE and Packaged CCE: Premium Agent Dialer Ports Server License Unified CCE: Regular Agent Third-party IVR licenses Server License Perpetual Non-Production Regular Agent Premium Agent Dialer Ports Server License | License Type | Licenses | Flex Production | Unified CCE and Packaged CCE: Standard Agent Premium Agent Dialer Ports Server License | Perpetual Production | Unified CCE and Packaged CCE: Premium Agent Dialer Ports Server License Unified CCE: Regular Agent Third-party IVR licenses Server License | Perpetual Non-Production | Regular Agent Premium Agent Dialer Ports Server License |
| License Type | Licenses |
| Flex Production | Unified CCE and Packaged CCE: Standard Agent Premium Agent Dialer Ports Server License |
| Perpetual Production | Unified CCE and Packaged CCE: Premium Agent Dialer Ports Server License Unified CCE: Regular Agent Third-party IVR licenses Server License |
| Perpetual Non-Production | Regular Agent Premium Agent Dialer Ports Server License |
| Step 3 | Click Save . |

| License Type | Licenses |
|---|---|
| Flex Production | Unified CCE and Packaged CCE: Standard Agent Premium Agent Dialer Ports Server License |
| Perpetual Production | Unified CCE and Packaged CCE: Premium Agent Dialer Ports Server License Unified CCE: Regular Agent Third-party IVR licenses Server License |
| Perpetual Non-Production | Regular Agent Premium Agent Dialer Ports Server License |

| Note | After you register the product instance, you cannot change the license type. To change the license type, deregister the product
                                             instance. |
|---|---|

| Note | After you register the product instance, you can change the Transport Mode type from Smart Call Home to Smart Transport and vice-versa. You must make the changes from the Transport Settings page and save it. |
|---|---|

| Step 1 | In , navigate to Overview > Infrastructure Settings > License Management. |
|---|---|
| Step 2 | Click Register . Note Before you register the product instance, ensure to select the License Type and the communication mechanism in Transport Settings . | Note | Before you register the product instance, ensure to select the License Type and the communication mechanism in Transport Settings . |
| Note | Before you register the product instance, ensure to select the License Type and the communication mechanism in Transport Settings . |
| Step 3 | In the Smart Software Licensing Product Registration dialog box, paste the product instance registration token that you generated from Cisco SSM or Cisco SSM On-Prem . |
| Step 4 | Click Register to complete the registration process. After registration, the Smart Licensing Status displays the following details. Table 2. Smart Licensing Status Smart License Status Description On Unsuccessful Registration Registration Status Unregistered License Authorization Status Evaluation Export-Controlled Functionality Not Allowed On Successful Registration Registration Status Registered (Date and time of registration) Note The date and time indicate the server's time zone. License Authorization Status Authorized (Date and time of authorization) Note The date and time indicate the server's time zone. Export-Controlled Functionality Not Allowed Smart Account The name of the smart account Virtual Account The name of the virtual account Product Instance Name The name of the product instance Serial Number The serial number of the product instance Entitlements are a set of privileges customers and partners receive when purchasing a Cisco service agreement. Using Smart
                                             Licensing, you can view the License consumption summary for the entitlements of different license types. The License consumption
                                             summary displays the License Name, Usage Count, and Status against each entitlement name. You can update or purchase entitlements on the Cisco Commerce website. For more information, see https://apps.cisco.com/Commerce/ . | Smart License Status | Description | On Unsuccessful Registration | Registration Status | Unregistered | License Authorization Status | Evaluation | Export-Controlled Functionality | Not Allowed | On Successful Registration | Registration Status | Registered (Date and time of registration) Note The date and time indicate the server's time zone. | Note | The date and time indicate the server's time zone. | License Authorization Status | Authorized (Date and time of authorization) Note The date and time indicate the server's time zone. | Note | The date and time indicate the server's time zone. | Export-Controlled Functionality | Not Allowed | Smart Account | The name of the smart account | Virtual Account | The name of the virtual account | Product Instance Name | The name of the product instance | Serial Number | The serial number of the product instance |
| Smart License Status | Description |
| On Unsuccessful Registration |
| Registration Status | Unregistered |
| License Authorization Status | Evaluation |
| Export-Controlled Functionality | Not Allowed |
| On Successful Registration |
| Registration Status | Registered (Date and time of registration) Note The date and time indicate the server's time zone. | Note | The date and time indicate the server's time zone. |
| Note | The date and time indicate the server's time zone. |
| License Authorization Status | Authorized (Date and time of authorization) Note The date and time indicate the server's time zone. | Note | The date and time indicate the server's time zone. |
| Note | The date and time indicate the server's time zone. |
| Export-Controlled Functionality | Not Allowed |
| Smart Account | The name of the smart account |
| Virtual Account | The name of the virtual account |
| Product Instance Name | The name of the product instance |
| Serial Number | The serial number of the product instance |

| Note | Before you register the product instance, ensure to select the License Type and the communication mechanism in Transport Settings . |
|---|---|

| Smart License Status | Description |
|---|---|
| On Unsuccessful Registration |
| Registration Status | Unregistered |
| License Authorization Status | Evaluation |
| Export-Controlled Functionality | Not Allowed |
| On Successful Registration |
| Registration Status | Registered (Date and time of registration) Note The date and time indicate the server's time zone. | Note | The date and time indicate the server's time zone. |
| Note | The date and time indicate the server's time zone. |
| License Authorization Status | Authorized (Date and time of authorization) Note The date and time indicate the server's time zone. | Note | The date and time indicate the server's time zone. |
| Note | The date and time indicate the server's time zone. |
| Export-Controlled Functionality | Not Allowed |
| Smart Account | The name of the smart account |
| Virtual Account | The name of the virtual account |
| Product Instance Name | The name of the product instance |
| Serial Number | The serial number of the product instance |

| Note | The date and time indicate the server's time zone. |
|---|---|

| Note | The date and time indicate the server's time zone. |
|---|---|

| Status | Description |
|---|---|
| Unregistered | Product is unregistered. |
| Registered | Product is registered. Registration is automatically renewed every six months. |
| Registration Expired | Product registration has expired because the ID Certificate issued by Cisco SSM is not renewed for more than 12 months. |

| Status | Description |
|---|---|
| Evaluation state | Product is not registered with Cisco. |
| Evaluation Expired | Product evaluation period has expired. |
| Authorized | Product is in authorized or in compliance state. Authorization is renewed every 30 days. |
| Authorization Expired | Product authorization has expired. This usually happens when the product has not communicated with Cisco for 90 days. It is
                                             in an overage period for 90 days before enforcing restrictions. |
| Out-of-Compliance | Product is in out-of-compliance state because of insufficient licenses. It is in an overage period for 90 days before enforcing
                                             restrictions. |
| Unauthorized | Product is unauthorized. |
| No License in Use | No Licenses are in use. |

| Status | Status Description |
|---|---|
| Authorization Expired | Product authorization has expired, when the product has not communicated with Cisco for 90 days. |
| Not Authorized | Product instance is not authorized. |
| Evaluation state | Product is not registered with Cisco. |
| Evaluation Expired | Product evaluation period has expired. |
| In Compliance | Product is in authorized or in compliance state. Authorization is renewed every 30 days. |
| ReservedInCompliance | Entitlement is in compliance with the installed reservation authorization code. |
| Out-of-Compliance | Product is in out-of-compliance state because of insufficient licenses. It is in an overage period for 90 days before enforcing
                                          restrictions. |
| Not Applicable | Entitlement is not applicable. |
| Invalid | Error condition state. |
| Invalid Tag | Entitlement tag is invalid. |
| No License in Use | Entitlement is not in use. |
| Waiting | Waiting for an entitlement request's response from Cisco SSM or Cisco SSM On-Prem . |
| Disabled | Product instance is deactivated or disabled. |

| Note | To know about the agent license that is consumed by the Standard and Premium licenses, see the Cisco Collaboration Flex Plan Contact Center Data Sheet at https://www.cisco.com/c/en/us/products/collateral/unified-communications/cisco-collaboration-flex-plan/datasheet-c78-741220.html |
|---|---|

| Note | When agents log into non-voice or digital channel MRDs using non-Cisco third party applications, the system consumes only
                                          a Standard  license. |
|---|---|

| Note | The premium license is specifically consumed during the following scenarios: When an agent assigned the supervisor role logs into the Cisco Finesse desktop. When an agent logs into the Cisco Finesse desktop and handles Outbound Predictive or Progressive campaign calls. When an agent signs in and handles digital channel tasks using Enterprise Chat and Email or Webex Connect. |
|---|---|

| Note | Classic Licenses that are partially converted will need new Classic License file for managing the remaining Classic Licenses. |
|---|---|

| Note | You have to Deregister and Reregister manually. |
|---|---|

| Step 1 | In , navigate to Overview > Infrastructure Settings > License Management. |
|---|---|
| Step 2 | Click Action > Renew Authorization . This process takes a few seconds to renew the authorization and close the window. |

| Step 1 | In , navigate to Overview > Infrastructure Settings > License Management . |
|---|---|
| Step 2 | Click Action > Renew Registration . This process takes a few seconds to renew the authorization and close the window. |

| Note | Product can migrate to a different virtual account when reregistering with the token from a new virtual account. |
|---|---|

| Step 1 | In , navigate to Overview > Infrastructure Settings > License Management. |
|---|---|
| Step 2 | Click Action > Reregister . |
| Step 3 | In the Smart Software Licensing Product Registration dialog box, paste the copied or saved Registration Token Key that you generated using the Cisco SSM or Cisco SSM On-Prem in the Product Instance Registration Token text box. |
| Step 4 | Click Reregister to complete the reregistration process. |
| Step 5 | Close the window. |

| Note | If  is unable to connect to Cisco SSM or Cisco SSM On-Prem , and the product is deregistered, then a confirmation message notifies you to remove the product manually from Cisco SSM or Cisco SSM On-Prem to free up licenses. |
|---|---|

| Note | After deregistering, the product reverts to the Evaluation state if the evaluation period is not expired. All the license
                                             entitlements that are used for the product are immediately released to the virtual account and are available for other product
                                             instances to use them. |
|---|---|

| Step 1 | In , navigate to Overview > Infrastructure Settings > License Management . |
|---|---|
| Step 2 | Click Action > Deregister . |
| Step 3 | On the Confirm Deregistration dialog box, click Yes to deregister. |

| Note | The reserved licenses require no renewal or reauthorization unless there is a license usage change on the device. License
                                       reservation provides limited functionality to certain Smart Licensing features such as transfer of licenses between products,
                                       license usage, and asset management. The Specific License Reservation (SLR) feature does not offer the following benefits that are available as part of the Smart
                                       Licensing feature: Dynamic movement of license consumption between products Real-time license usage visibility and asset management Simplified product registration |
|---|---|

| Note | To view the Miscellaneous page, the signed in user must have System Information enabled in the Feature control set. |
|---|---|

| Field | Description |
|---|---|
| Treatment Mode | This field shows the treatment mode that is currently in place. You can make a selection from the drop-down menu options to
                                          indicate how congestion is to be handled and how the caller is to be treated. The first three options send the call to an
                                          external VRU. The last two options terminate the call. Treat call with DN Default Label Treat call with Routing client default label Treat call with System default label Terminate with Dialog Fail/RouteEnd Release Message to the Routing client If you select Treat call with DN Default Label, or Treat call with Routing client default label, you see this message: The target call treatment system should be outside of the CCE system . This means that the call will be sent to an external VRU for VRU treatment. |
| System Default Label | This field is required when Treat call with System default label is the selection for Congestion Treatment Mode. Enter a label
                                          for the system default. This field allows a maximum of 32 characters. |
| Maximum Calls Per Second | This field displays the current value for maximum calls per second for the deployment. If this field has been set to a number
                                          other than the default, click the X to restore the deployment type default. |
| Congestion Control Enabled | Check this check box to enable congestion control and make all other fields editable. |
| Extended Event Detail | Check this check box to enable extended agent event detail. Note The extended agent event detail capabilities are supported only for 36000 agent deployment. | Note | The extended agent event detail capabilities are supported only for 36000 agent deployment. |
| Note | The extended agent event detail capabilities are supported only for 36000 agent deployment. |
| Session Inactivity Timer | To set the inactivity timer for the active session, enter the value in minutes. The minimum is 15 minutes and the maximum
                                          is 1440 minutes. The default is 30 minutes. When you relogin, the system automatically deletes the inactivity timer value
                                          that you had set for the previous session. |

| Note | The extended agent event detail capabilities are supported only for 36000 agent deployment. |
|---|---|

| Note | To prevent the smart agent from reporting the product's version details, create a registry value named DisableSmartLicenseVersionReporting with the type REG_SZ in the following path: HKEY_LOCAL_MACHINE\SOFTWARE\Cisco Systems, Inc.\ICM\SystemSettings If this registry value is set to true , the version details will not be reported to the Cisco SSM. |
|---|---|