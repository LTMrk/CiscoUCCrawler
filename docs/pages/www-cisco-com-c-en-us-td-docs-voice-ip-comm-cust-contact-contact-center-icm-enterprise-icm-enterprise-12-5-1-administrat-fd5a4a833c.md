---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-administrat-fd5a4a833c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/administration/guide/ucce_b_administration-guide-for-cisco-unified12_5/ucce_b_administration-guide-for-cisco-unified12_5_chapter_01111.html
retrieved_at: 2026-08-16T20:47:33.368897+00:00
---

Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)

# Administration Guide for Cisco Unified Contact Center Enterprise, Release 12.5(1)

Updated: February 7, 2019

Chapter: Smart Licensing

## Chapter: Smart Licensing

# Smart Licensing

## Overview

Cisco Smart Software Licensing is a flexible software licensing model that streamlines the way you activate and manage Cisco
                              software licenses across your organization. Smart Licenses provide greater insight into software license ownership and consumption,
                              so that you know what you own and how the licenses are being used. The solution allows you to easily track the status of your
                              license and software usage trends. It pools the license entitlements in a single account and allows you to move licenses freely
                              across virtual accounts. Smart Licensing is enabled across most of the Cisco products and managed by a direct cloud-based
                              or mediated deployment model.

Smart Licensing registers the Product Instance, reports license usage, and obtains the necessary authorization from Cisco Smart Software Manager ( Cisco SSM ) or Cisco Smart Software Manager On-Prem ( Cisco SSM on-Prem ) .

You can use Smart Licensing to:

View license usage and count.

View the status of each license type and the product instance.

View the product licenses available on Cisco SSM or Cisco SSM on-Prem .

Register or deregister the Product Instance, renew license authorization and license registration.

Sign in additional agents to Unified CCX up to the maximum limit that is configured in your OVA.

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

Smart Licensing Tasks in CCE Administration Portal

Smart Licensing Task Flow

Best Practices

Best Practices

### Prerequisites for Smart Licensing

The following are the prerequisites for configuring Smart Licensing:

Smart Licensing Enrollment

Set up Smart and Virtual accounts. For more information, see https://software.cisco.com/#module/SmartLicensing .

Adoption of License Integration Strategy

Decide how you want to connect your product instance to Smart Licensing servers:

On-Cloud: Configure Unified CCE to connect to Cisco SSM.

On-Premise:

Deploy the Cisco SSM On-Prem . For instructions on how to do this, see https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager-satellite.html .

Configure Unified CCE to connect to Cisco SSM On-Prem .

For more information, see Smart License Deployments .

Import the Rogger A certificate into the AW machines

Export Logger/Rogger A certificate and save it by using the url https:<Logger/Roggerhostname>:443

Import the certificate in AW by using the following command:

```
cd %CCE_JAVA_HOME%\bin
```

```
C:\ Program Files (x86)\ Java\jre1.8.0_221 \bin >keytool.exe -keystore Program Files (x86)\ Java\jre1.8.0_221 \ lib\security\cacerts " 
-import -alias <alias name> -file <certicate with fully qualified path>
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

Cisco SSM On-Prem is an on-premises component that can handle your licensing needs. When you choose this option, Unified CCE registers and reports license consumption to the Cisco SSM On-Prem , which synchronizes its database regularly with Cisco SSM that is hosted on cisco.com.

You can use the Cisco SSM On-Prem in either Connected or Disconnected mode, depending on whether the Cisco SSM On-Prem can connect directly to cisco.com.

Configure Transport URL for Cisco SSM On-Prem with Smart Call-Home URL: https://<OnpremCSSM>/Transportgateway/services/DeviceRequestHandler

The <OnpremCSSM> value must match with the SSM Tomcat Certificate Common Name or Subject Alternative Name. In the above URL,
                                             replace <OnpremCSSM> with FQDN or IP, based on the SSM Tomcat Certificate.

Connected —Use when there is connectivity to cisco.com directly from the Cisco SSM On-Prem . Smart account synchronization occurs automatically.

Disconnected —Use when there is no connectivity to cisco.com from the Cisco SSM On-Prem . Cisco SSM On-Prem must synchronize with Cisco SSM manually to reflect the latest license entitlements.

For more information on Cisco SSM On-Prem , see https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager.html .

#### Cisco SSM On-Prem Configuration

Perform these steps to get the correct URL for the customer's environment:

Log in to the On-Prem CSSM GUI with your virtual account.

The URL for the interface is https://<hostname_or_fqdn_of_CSSM>:8443

Click Smart Licensing link and navigate to Inventory > Production Instance Registration Tokens and click Smart Call Home Registration URL . This opens a pop-up window with the URL in it.

Copy and paste this URL in the CCE Smart Transport URL field to create the link.

This link is created using the Cisco SSM On-Prem adminstration configuration and matches with the Cisco Smart Licensing CA
                                       signed certificate .

Contact the Cisco SSM administration team to know the user side URL to generate tokens. Ensure the name used in the CCE Smart Transport URL matches the certificate for the Server. For example; if Cisco SSM is configured with an IP in the admin side then the Smart Call Home URL must use the same IP in the URL. If Cisco SSM is configured with just the hostname then the URL must match the same hostname too.

If the SmartAgent.log shows and error, check the URL to ensure the hostname/IP address matches with the hostname/IP address in the certificate.

## Smart Licensing Task Flow

Complete these tasks to set up smart licensing for Unified CCE .

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

Configure the transport settings through which Unified CCE connects to the Cisco SSM or Cisco SSM On-Prem .

For more information, see Configure Transport Settings for Smart Licensing .

Step 4

Select the License Type

Select the License Type before registering the product instance.

For more information, see License Types .

Step 5

Register with Cisco SSM

You can register Unified CCE with Cisco SSM or Cisco SSM On-Prem .

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

### Configure Transport Settings for Smart Licensing

Configure the connection mode between Unified CCE and Cisco SSM .

Step 1

From Unified CCE Administration, navigate to Overview > Infrastructure Settings > License Management .

Step 2

Click Transport Settings to set the connection method.

Step 3

Select the connection method to Cisco SSM :

Direct — Unified CCE connects directly to Cisco SSM on cisco.com. This is the default option.

Transport Gateway — Unified CCE connects to Cisco SSM On-Prem for smart licensing. Enter the Cisco SSM On-Prem URL.

HTTP/HTTPS Proxy — Unified CCE connects to a proxy server, which connects to Cisco SSM . Enter the Fully Qualified Domain Name (FQDN) of the proxy server along with the port.

Step 4

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

If you select the Deployment Type as ICM Rogger/Logger , the system automatically updates to Perpetual even when the License Type is configured as Flex .

Step 1

From Unified CCE Administration , navigate to Overview > Infrastructure Settings > License Management .

Step 2

Click License Type .

Step 3

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

ICM:

Regular Agent

Avaya PG

Third-party IVR licenses

Server License

Perpetual Non-Production

Regular Agent

Premium Agent

Dialer Ports

Server License

Avaya PG

Step 4

Click Save .

### Register with Cisco Smart Software Manager

The product instance has 90 days of evaluation period, within which, the registration must be completed. Else, the product
                                 instance gets into the enforcement state.

Register your product instance with Cisco SSM or Cisco SSM On-Prem to exit the Evaluation or Enforcement state.

After you register the product instance, you cannot change the license type. To change the license type, deregister the product
                                             instance.

You can register your product instance with Cisco SSM or Cisco SSM On-Prem from any ADS server. After the registration, all the AWs show the same registration status.

Step 1

In Unified CCE Administration , navigate to Overview > Infrastructure Settings > License Management.

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

This table explains the various product registration status for Smart Licensing in the Unified CCE Administration portal:

Status

Description

Unregistered

Product is unregistered.

Registered

Product is registered. Registration is automatically renewed every six months.

Registration Expired

Product registration has expired because the ID Certificate issued by Cisco SSM is not renewed for more than 12 months.

#### Authorization Status

This table describes the possible product authorization status for Smart Licensing in the Unified CCE Administration portal:

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

This table describes the possible product instance license entitlement status for Smart Licensing in the Unified CCE Administration portal:

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

The Product Instance reports license usage to Cisco SSM every 15 minutes. If your license consumption is more than the entitlements for four consecutive reporting intervals, the
                                 Product Instance is pushed to the Out-of-Compliance state. The Out-of-Compliance period is for 90 days, within which you need
                                 to purchase the additional licenses. If you fail to take corrective action within the 90 days period, the Product Instance
                                 is pushed to the Enforcement state.

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

In the Enforcement state, addition of new agents is blocked in Unified CCE .

## License States

Smart Licensing has the following states:

Registration State

Unregistered —Product Instance is unregistered.

Registered —After you purchase the license, you need to register the Product Instance with Cisco SSM . To register with Cisco SSM , generate a registration token from the Cisco SSM portal. Use the registration token to register your Product Instance.

Registration Expired —Product Instance registration has expired because the ID Certificate issued by Cisco SSM is not renewed for more than 12 months. Reregister the Product Instance.

Use SPOG/CCEAdmin > License Management to manually renew your registration.

Authorization State

No licenses in use

Evaluation Mode —The Product Instance license has an Evaluation period of 90 days. In the Evaluation period you have unlimited access to the
                                       product with highest set of product capabilities and unlimited number of licenses. You must register the system with Cisco SSM or Cisco SSM On-Prem within 90 days. If the system is not registered before the end of the evaluation period, it will be moved to the Enforcement
                                       state where certain system functions are restricted.

In Compliance —When the license consumption is as per the purchased quantity, the product is compliant.

Evaluation expired —Product Instance evaluation period has expired.

Authorized —Product Instance is in authorized or in compliance state. Authorization is renewed every 30 days.

Out of Compliance —Product Instance reports license usage to Cisco SSM every 15 minutes . If your license consumption is more than the entitlements for five consecutive reporting intervals, the Product Instance is
                                          transitioned to the Out of Compliance state.

The out-of-compliance period is for 90 days, within which you need to purchase the additional licenses. If you fail to take
                                       corrective action within the 90 days period, the Product Instance is transitioned to the Enforcement state.

Authorization Expired —Product Instance authorization has expired. This usually happens when the product has not communicated with Cisco SSM for more than 90 days. It is in an overage period for 90 days before restrictions are enforced.

Use SPOG/CCEAdmin > License Management to manually renew your authorization.

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

The banner displays the aggregate license compliance status on the Unified CCE Administration portal. The banner is displayed only when any of the product instances in the deployment is in the Evaluation,
                                 Out-of-Compliance, or Enforcement state.

The License Compliance report displays the license status of product instances in the deployment. The reporting hierarchy is Enforcement, Out-of-Compliance,
                                 and Evaluation. This means that if any of the product instances in the deployment is in the Enforcement state, the banner
                                 displays Enforcement state as the overall status. Click the Learn More option to view the consolidated License Compliance report .

When licenses are consumed in a Non-Production System, a banner message, "You are using a Non-Production System”, is displayed.

System Alerts

Smart Licensing related system alerts, which get auto-corrected, are displayed in Unified CCE Administration portal when:

Smart License state is not initialized

Smart Agent is not enabled

Serial number is not generated

In the above conditions, a red system alert is displayed in the Alerts button on the Unified CCE Administration portal. The red circle against the name of the machine in the inventory indicates the identified issue and
                           the immediate action needed. After the issue is resolved, a green circle against the name of the machine indicates the system
                           is running fine, for example, when the Smart Agent is enabled or Smart License state is initialized.

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

## New Deployments

For new deployments, buy the licenses on Cisco Commerce website at https://apps.cisco.com . Begin to use the product by using the licenses from your Smart Account.

## Migrate to Smart Licensing

If you are upgrading to Unified CCE Release 12.5(1), from Unified CCE Release 10.x or above, use self serve capabilities in Cisco SSM to declare the licenses that you own.

## License Management

Smart Licensing can be managed by using Cisco SSM and License Management in Unified CCE Administration portal. .

Cisco SSM — Cisco SSM enables you to manage all your Cisco smart software licenses from a centralized website. With Cisco SSM , you organize and view your licenses in groups called virtual accounts (collections of licenses and product instances).

You can access Cisco SSM from https://software.cisco.com , by clicking the Smart Software Licensing link under the License menu.

License Management in Unified CCE Administration portal — Using the License Management option in the Unified CCE Administration portal, you can register or deregister the product instance,
                                 select your License Type, set transport settings or view the licensing consumption summary.

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

In Unified CCE Administration , navigate to Overview > Infrastructure Settings > License Management.

Step 2

Click Action > Renew Authorization .

This process takes a few seconds to renew the authorization and close the window.

### Renew Registration

Use this procedure to manually renew your certificates.

The initial registration is valid for one year. Renewal of registration is automatically done every six months, provided the
                                 product is connected to Cisco SSM or Cisco SSM On-Prem .

Step 1

In Unified CCE Administration , navigate to Overview > Infrastructure Settings > License Management .

Step 2

Click Action > Renew Registration .

This process takes a few seconds to renew the authorization and close the window.

### Reregister License

Product can migrate to a different virtual account when reregistering with the token from a new virtual account.

Step 1

In Unified CCE Administration , navigate to Overview > Infrastructure Settings > License Management.

Step 2

Click Action > Reregister .

Step 3

In the Smart Software Licensing Product Registration dialog box, paste the copied or saved Registration Token Key that you generated using the Cisco SSM or Cisco SSM On-Prem in the Product Instance Registration Token text box.

Step 4

Click Reregister to complete the reregistration process.

Step 5

Close the window.

### Deregister License

If Unified CCE is unable to connect to Cisco SSM or Cisco SSM on-Prem , and the product is deregistered, then a confirmation message notifies you to remove the product manually from Cisco SSM or Cisco SSM on-Prem to free up licenses.

After deregistering, the product reverts to the Evaluation state if the evaluation period is not expired. All the license
                                             entitlements that are used for the product are immediately released to the virtual account and are available for other product
                                             instances to use it.

Step 1

In Unified CCE Administration , navigate to Overview > Infrastructure Settings > License Management .

Step 2

Click Action > Deregister .

Step 3

On the Confirm Deregistration dialog box, click Yes to deregister.

## Best Practices

Some of the best practices for Smart Licensing are:

Before purchasing your licenses, run the License Consumption report on the existing system to understand the consumption pattern
                                 to make the right purchase decisions on the license requirement.

Configure Admin email address in Cisco SSM to receive notifications and alerts from Cisco SSM .

| For | Go to... |
|---|---|
| Smart Licensing Prerequisites | Prerequisites for Smart Licensing |
| Understanding the License Consumption Calculation | License Consumption Calculation |
| Migration to Smart Licensing | Migrate to Smart Licensing |
| Smart Licensing Tasks in CCE Administration Portal | Smart Licensing Task Flow |
| Best Practices | Best Practices |

| Note | The <OnpremCSSM> value must match with the SSM Tomcat Certificate Common Name or Subject Alternative Name. In the above URL,
                                             replace <OnpremCSSM> with FQDN or IP, based on the SSM Tomcat Certificate. |
|---|---|

| Note | The URL for the interface is https://<hostname_or_fqdn_of_CSSM>:8443 |
|---|---|

| Steps | Action | Description |
|---|---|---|
| Step 1 | Create your Smart Account | Use the Smart Account to organize licenses according to your needs. To create a Smart Account, go to http://software.cisco.com After the Smart Account is created, Cisco SSM creates a default Virtual Account for this Smart Account. You can use the default account or create other Virtual Accounts. |
| Step 2 | Obtain the Product Instance Registration Token | Generate a product instance registration token for your virtual account. For more information, see Obtain the Product Instance Registration Token . |
| Step 3 | Configure Transport Settings for Smart Licensing | Configure the transport settings through which Unified CCE connects to the Cisco SSM or Cisco SSM On-Prem . For more information, see Configure Transport Settings for Smart Licensing . |
| Step 4 | Select the License Type | Select the License Type before registering the product instance. For more information, see License Types . |
| Step 5 | Register with Cisco SSM | You can register Unified CCE with Cisco SSM or Cisco SSM On-Prem . For more information, see Register with Cisco Smart Software Manager . |

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

| Step 1 | From Unified CCE Administration, navigate to Overview > Infrastructure Settings > License Management . |
|---|---|
| Step 2 | Click Transport Settings to set the connection method. |
| Step 3 | Select the connection method to Cisco SSM : Direct — Unified CCE connects directly to Cisco SSM on cisco.com. This is the default option. Transport Gateway — Unified CCE connects to Cisco SSM On-Prem for smart licensing. Enter the Cisco SSM On-Prem URL. HTTP/HTTPS Proxy — Unified CCE connects to a proxy server, which connects to Cisco SSM . Enter the Fully Qualified Domain Name (FQDN) of the proxy server along with the port. Note Proxy servers that require authentication are not supported for this connection method. | Note | Proxy servers that require authentication are not supported for this connection method. |
| Note | Proxy servers that require authentication are not supported for this connection method. |
| Step 4 | Click Save to save the settings. |

| Note | Proxy servers that require authentication are not supported for this connection method. |
|---|---|

| Note | If you select the incorrect license type, the product instance is placed in the Out-of-Compliance state. If this issue is
                                             unresolved, the product instance is placed in the Enforcement state where the system operations are impacted. |
|---|---|

| Note | If you select the Deployment Type as ICM Rogger/Logger , the system automatically updates to Perpetual even when the License Type is configured as Flex . |
|---|---|

| Step 1 | From Unified CCE Administration , navigate to Overview > Infrastructure Settings > License Management . |
|---|---|
| Step 2 | Click License Type . The Select License Type page is displayed. |
| Step 3 | Select the License Type and the Usage Mode corresponding to what you have purchased before registering the product instance. The following table lists the license types and licenses offered as part of Unified CCE and Packaged CCE Smart Licensing: License Type Licenses Flex Production Unified CCE and Packaged CCE: Standard Agent Premium Agent Dialer Ports Server License Perpetual Production Unified CCE and Packaged CCE: Premium Agent Dialer Ports Server License ICM: Regular Agent Avaya PG Third-party IVR licenses Server License Perpetual Non-Production Regular Agent Premium Agent Dialer Ports Server License Avaya PG | License Type | Licenses | Flex Production | Unified CCE and Packaged CCE: Standard Agent Premium Agent Dialer Ports Server License | Perpetual Production | Unified CCE and Packaged CCE: Premium Agent Dialer Ports Server License ICM: Regular Agent Avaya PG Third-party IVR licenses Server License | Perpetual Non-Production | Regular Agent Premium Agent Dialer Ports Server License Avaya PG |
| License Type | Licenses |
| Flex Production | Unified CCE and Packaged CCE: Standard Agent Premium Agent Dialer Ports Server License |
| Perpetual Production | Unified CCE and Packaged CCE: Premium Agent Dialer Ports Server License ICM: Regular Agent Avaya PG Third-party IVR licenses Server License |
| Perpetual Non-Production | Regular Agent Premium Agent Dialer Ports Server License Avaya PG |
| Step 4 | Click Save . |

| License Type | Licenses |
|---|---|
| Flex Production | Unified CCE and Packaged CCE: Standard Agent Premium Agent Dialer Ports Server License |
| Perpetual Production | Unified CCE and Packaged CCE: Premium Agent Dialer Ports Server License ICM: Regular Agent Avaya PG Third-party IVR licenses Server License |
| Perpetual Non-Production | Regular Agent Premium Agent Dialer Ports Server License Avaya PG |

| Note | After you register the product instance, you cannot change the license type. To change the license type, deregister the product
                                             instance. |
|---|---|

| Note | You can register your product instance with Cisco SSM or Cisco SSM On-Prem from any ADS server. After the registration, all the AWs show the same registration status. |
|---|---|

| Step 1 | In Unified CCE Administration , navigate to Overview > Infrastructure Settings > License Management. |
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

| Note | In the Enforcement state, addition of new agents is blocked in Unified CCE . |
|---|---|

| Note | Use SPOG/CCEAdmin > License Management to manually renew your registration. |
|---|---|

| Note | Use SPOG/CCEAdmin > License Management to manually renew your authorization. |
|---|---|

| Note | To know about the agent license that is consumed by the Standard and Premium licenses, see the Cisco Collaboration Flex Plan Contact Center Data Sheet at https://www.cisco.com/c/en/us/products/collateral/unified-communications/cisco-collaboration-flex-plan/datasheet-c78-741220.html |
|---|---|

| Note | You have to Deregister and Reregister manually. |
|---|---|

| Step 1 | In Unified CCE Administration , navigate to Overview > Infrastructure Settings > License Management. |
|---|---|
| Step 2 | Click Action > Renew Authorization . This process takes a few seconds to renew the authorization and close the window. |

| Step 1 | In Unified CCE Administration , navigate to Overview > Infrastructure Settings > License Management . |
|---|---|
| Step 2 | Click Action > Renew Registration . This process takes a few seconds to renew the authorization and close the window. |

| Note | Product can migrate to a different virtual account when reregistering with the token from a new virtual account. |
|---|---|

| Step 1 | In Unified CCE Administration , navigate to Overview > Infrastructure Settings > License Management. |
|---|---|
| Step 2 | Click Action > Reregister . |
| Step 3 | In the Smart Software Licensing Product Registration dialog box, paste the copied or saved Registration Token Key that you generated using the Cisco SSM or Cisco SSM On-Prem in the Product Instance Registration Token text box. |
| Step 4 | Click Reregister to complete the reregistration process. |
| Step 5 | Close the window. |

| Note | If Unified CCE is unable to connect to Cisco SSM or Cisco SSM on-Prem , and the product is deregistered, then a confirmation message notifies you to remove the product manually from Cisco SSM or Cisco SSM on-Prem to free up licenses. |
|---|---|

| Note | After deregistering, the product reverts to the Evaluation state if the evaluation period is not expired. All the license
                                             entitlements that are used for the product are immediately released to the virtual account and are available for other product
                                             instances to use it. |
|---|---|

| Step 1 | In Unified CCE Administration , navigate to Overview > Infrastructure Settings > License Management . |
|---|---|
| Step 2 | Click Action > Deregister . |
| Step 3 | On the Confirm Deregistration dialog box, click Yes to deregister. |