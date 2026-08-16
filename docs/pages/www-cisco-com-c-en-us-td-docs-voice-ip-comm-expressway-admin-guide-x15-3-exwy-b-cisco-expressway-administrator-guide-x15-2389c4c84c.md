---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-admin-guide-x15-3-exwy-b-cisco-expressway-administrator-guide-x15-2389c4c84c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X15-3/exwy_b_cisco-expressway-administrator-guide-x153/exwy_m_smart-licensing.html
retrieved_at: 2026-08-16T22:28:06.360188+00:00
---

Cisco Expressway Administrator Guide (X15.3)

# Cisco Expressway Administrator Guide (X15.3)

Updated: August 5, 2025

Chapter: Smart Licensing

## Chapter: Smart Licensing

# Smart Licensing

## About Smart Licensing

Cisco Expressway X14.2 only supports Smart Licensing and is capped at 2500 encrypted signaling sessions to endpoints. It also includes changes in the
                                       trafficserver behavior (bug ID CSCwc69661 refers) that can lead to MRA failures - see here . For detailed information, see the Cisco Expressway and Cisco TelePresence Video Communication Server Release Note (x14.2) and Cisco Expressway Administrator Guide (X14.2) before upgrading to X14.2 .

Cisco Smart Software Licensing is a new way to think about licensing. From X14.2 release, Smart Licensing is typically managed
                           with the cloud-based Cisco Smart Software Manager (CSSM). Alternatively, deployments that need an on premises approach can
                           use the Smart Software Manager On-Prem product (formerly known as "Smart Software Manager satellite" ). Basically it is a cloud-based, software license management solution. It simplifies the licensing experience across the
                           enterprise and makes it easier to purchase, deploy, enables you to automate time-consuming, manual licensing tasks. The solution
                           allows you to easily track the status of your license and software usage trends. It provides visibility into license ownership
                           and consumption through a single, simple user interface.

You place an order on Cisco Commerce and the order is associated with the smart account, this information is populated on
                           Smart Software Manager, which resides on cisco.com. Now you have a complete view on what you have ordered and purchased.

You can use Smart Licensing to:

See the license usage and count.

See the status of each license type.

See the product licenses available on Cisco Smart Software Manager or  Smart Software Manager On-Prem.

Renew License Authorization with Cisco Smart Software Manager or Smart Software Manager On-Prem.

Renew Registration

Deregister with Cisco Smart Software Manager or Smart Software Manager On-Prem.

Reregister License with Cisco Smart Software Manager

Important

Product Activation Keys (PAK) Licensing (Option Keys) are removed from version X14.2.

Smart License is default and the only licensing mode for Expressway-C and Expressway-E.

We recommend you to enable Smart License before upgrading Expressway to version X14.2. This will help while reverting to a
                                             previous image.

You are not allowed to add the Microsoft Interoperability (MS Interop) key from version X14.2. This functionality is available
                                             only in cases where you have the MS Interop options before upgrade. But once on X14.2, you cannot add MS Interop key.

Once Smart Licensing is turned ON, you do not have an option for reverting to Cisco VCS through Service Select .

Once Smart Licensing is turned ON, you cannot disable it and revert to legacy licensing. There is no option available to revert
                                             it to Cisco VCS (except for a Factory Reset ), either.

For Cisco VCS, legacy/option key license mode remains the only licensing mode.

When Cisco VCS is converted to Expressway Series X14.2, Smart License mode is turned ON automatically.

Smart Licensing is FIPS compliant. For more information, see Prerequisites for Configuring FIPS140-2 Cryptographic Mode.

In Smart License mode, the functionality is enabled by default and hence they are not needed or supported and may not be
                                             converted in the License Registration Portal .

This product has Smart Licensing enabled (through CLI and GUI), is registered to CSSM, and reports license consumption to CSSM. Two models exist to report the usage:

Direct Model - Use this model in networks where devices can communicate directly to the Internet or can connect to the Internet via a HTTPS
                                 proxy. Communication to Cisco.com is through HTTPS, therefore all traffic is encrypted during transport. If the traffic is
                                 sent through a HTTPS proxy, all communications between devices and Cisco.com are channeled through a centralized location
                                 if additional inspection or security policies have to be applied.

Mediated Deployment Model - Use this model in networks where devices cannot connect to the Internet and therefore cannot reach Cisco.com. This deployment
                                 model requires installing a CSSM satellite virtual machine on your premises which all internal hosts can reach. The on-premise
                                 satellite can be deployed in a connected mode that synchronizes with CSSM. The synchronization with cisco.com can be either
                                 monthly, weekly, or can be deployed in a totally disconnected configuration requiring manual file uploads and downloads to
                                 keep the satellite in sync. It is recommended to sync at least every 30 days.

### Factory Reset

The following are a few changes to the way Factory Reset works for Expressway Devices.

Cisco VCS Factory Reset is unchanged .

Flag Removed : Flag ` -o ` (saving of the option keys) is removed from the Expressway factory reset.

To reset the unit to factory default settings, at the command prompt, execute the following command.

Use the chosen flags (if you have any) when you perform a factory reset or you will be prompted with the following list if
                                                   you do not give any flags in the command.

factory-reset [list of flags]

```
*************************************************************
Warning! This operation resets the unit to factory default settings!
*************************************************************

To cancel operation before final confirmation press Ctrl+C
Keep brand and type of the device [YES/NO]? yes
Keep smart licensing settings [YES/NO]? no
Keep FIPS 140 configuration [YES/NO]? no
Keep IP configuration [YES/NO]? yes
Keep dedicated management interface configuration [YES/NO]? yes
Keep ssh keys [YES/NO]? yes
Keep server certificate, associated key and CA trust store [YES/NO]? yes
Keep root and admin passwords [YES/NO]? yes
Save log files [YES/NO]? yes

Are you sure you want to continue [YES/NO]? yes
```

New Flags Added : Two new flags ` -v ` (device brand and type) and ` -t ` (Smart License configuration settings) are added.

' -v ' flag: When the factory reset is triggered and the ` -v ` flag is chosen, the device prompts you to save the brand and box type of their device (where brand is Expressway Series
                                             or Cisco VCS and type is Expressway-E or Expressway-C).

Condition :

Choice is "No" : The default values are Expressway-C and Cisco VCS.

' -t ' flag: When the factory reset is triggered and the ` -t ` flag is chosen, the device prompts you to save the Smart Licensing configuration.

Conditions :

Choice is "No" : The Smart Licensing is reverted to 'Direct' if the device is still an Expressway.

Choice is "Yes" : The Smart Licensing configuration and registration (if it exists) is preserved.

In this case, after factory reset the device will go offline until the DNS settings are configured. This means, you will see
                                                   two different alarms indicating the Smart License registration and authentication are not working. These alarms will clear
                                                   when the device goes back online.

For more information on alarms (Alarm IDs - 30042 and 30044), see Alarms Reference .

The new factory reset is FIPS compliant.

At the command prompt, execute the following command:

# factory-reset --help - Lists all the available options.

#### Restrictions for Smart Licensing

You are not allowed to add the Microsoft Interoperability (MS Interop) Option Key from version X14.2. This functionality is
                                 available only in cases where you have the MS Interop Option Key before upgrade from Cisco VCS to Expressway Series. But once
                                 on X14.2, you cannot add MS Interop Option Key.

After Factory Reset, if the MS Interop option key is on the device, it will be preserved.

### How Smart Licensing Works

Cisco Smart Software Licensing (Smart Licensing) is a new approach to licensing which is enabled across multiple Cisco products.
                                 It simplifies licensing and makes license ownership and consumption clearer. Devices self-register and report license consumption,
                                 which removes the need to use option keys (Product Activation Keys). License entitlements are pooled in a single account that
                                 can be used across Expressways or across different clusters of Expressways. You can use a license on any compatible device
                                 owned by your company and move them around to meet the needs of your organization.

You use Smart Licensing to register/deregister Expressway with the Cisco Smart Software Manager (CSSM) or the Cisco Smart
                                 Software Manager On-Prem to view/monitor smart license usage, count/manage licenses, know the status per license type, and
                                 renew license authorizations.  CSSM is hosted on the Cisco Software Manager and allows product instances to register and report license consumption to it.

There are two main deployment options for Smart Licensing:

Cisco Smart Software Manager

Cisco Smart Software Manager  On-premises

#### Cisco Smart Software Manager

The Cisco Smart Software Manager is a cloud-based service that handles your system licensing. It enables you to manage all
                                 of your Cisco Smart software licenses from one centralized website. With Cisco Smart Software Manager, you can organize and
                                 view your licenses in groups called virtual accounts (collections of licenses and product instances). The Cisco Smart Software
                                 Manager allows you to:

Create, manage, track, or view virtual accounts

Create and manage Product Instance Registration Tokens

Transfer licenses across virtual account or view licenses

Transfer, remove, or view product instances

Remove registered product instance

Run reports against your virtual accounts

View overall account information

To access or for additional information about Cisco Smart Software Manager, go to https://software.cisco.com .

#### On-premises option - using Smart Software Manager On-Prem

If you do not want to manage Cisco products directly using Cisco Smart Software Manager, either for policy or network availability
                                 reasons, you can instead use Smart Software Manager On-Prem. This is an on-premises component of Cisco Smart Licensing and
                                 products register and report license consumption to it in the same way as with Cisco Smart Software Manager.

Smart Software Manager On-Prem can be deployed in either Connected or Disconnected mode, depending on whether the satellite
                                 can connect directly to cisco.com.

Connected . Used when there is direct connectivity to cisco.com. Smart account synchronization occurs automatically.

Disconnected . Used when there is no direct connectivity to cisco.com. Smart Account synchronization must be manually uploaded and downloaded.

#### More information

For detailed product information about the Cisco Smart Software Manager, see Cisco Smart Software Manager . Or for information about the on-prem manager, see Smart Software Manager On-Prem .

### Creating a Smart Account

Navigate to the Cisco Software Central web page:

https://software.cisco.com/

The Cisco Software Central page is displayed.

You need a Smart Account to use Smart Licensing.

### Requesting License Reservation for Your Smart Account

Complete the following steps to request license reservation to your Smart Account in Cisco Smart Software Manager:

Go to Support Case Manager .

Click OPEN NEW CASE .

Select Software Licensing .

The licensing team will contact you to start the process or for any additional information.

## Before You Enable Smart Licensing

This section has some caveats to be aware of  before you implement Smart Licensing on Expressway.

Caution

After Smart Licensing is enabled, the only way to revert to PAK-based licensing (or to convert an Expressway system to a Cisco
                                          VCS system) is with a factory reset. Because a factory reset reinstalls the software image and resets the Expressway configuration
                                          to the default, we strongly advise you to backup the Expressway data before you enable Smart Licensing.

### Product Instance Evaluation Mode

After enabling Smart Licensing on Expressway allows only a 90-day Evaluation period. During the evaluation period, Expressway
                              does allow cluster-related configuration. After the evaluation period, if Expressway is not registered with either CSSM or
                              Smart Software Manager On-Prem, the product moves to Unauthorized state. In the Unauthorised state, the  Expressway does not
                              allow cluster-related configuration changes, nor does it allow local device registrations (SIP/H323).

After Smart Licensing is enabled, you cannot use option keys on the Expressway. So, if you want to use any Expressway functions
                              that still require option keys, use PAK-based licensing.

We recommend you to set up Smart and Virtual accounts before you review the general Expressway licensing information in Call Types and Licensing . For details, see Cisco Smart Accounts .

## Smart Licensing Settings

This section describes how to use the Smart Licensing settings in the Expressway web interface to do the following:

Enable Smart Licensing.

Register and deregister the Expressway with CSSM or Smart Software Manager On-Prem.

Manually renew the registration and license authorization.

View system license usage information as it is reported to CSSM or Smart Software Manager On-Prem. (Licenses are assigned
                                    to your organization's Smart Account and are not locked to a device.)

This section describes the web interface. For information about CLI commands for Smart Licensing, see the Command Reference section of this guide.

Field

Description

Smart licensing mode

Enables Smart Licensing on this Expressway product instance. Before you select this option, review the Smart Licensing Settings section.

It is always recommended to take a configuration backup in order to avoid any partial or complete configuration lost scenario.

Transport settings

Determines how this Expressway product instance communicates with CSSM to send and receive usage information.

Caution

If the Expressway product instance is already registered, you must first deregister it if you want to change transport settings
                                                      from Direct (CSSM) to On-Prem, or the other way round.

Choose Transport settings under licensing page, as per your smart licensing deployment model.

Transport settings

Direct : Expressway sends usage information directly over the internet and no additional components are needed. This is the default
                                          setting.

To use the Direct option, you must configure DNS settings on Expressway so that it can resolve cisco.com .

If you choose not to configure the domain and DNS on Expressway, you can instead select Smart Software Manager On-Prem or
                                          proxy server. If you choose not to use the DNS server in your deployment and not to connect to the internet, you can select
                                          the Smart Software Manager On-Prem with manual synchronization in disconnected mode.

Smart Software Manager On-Prem : Expressway sends usage information to an on-premise CSSM. Periodic information exchange keeps the databases in sync between
                                          Smart Software Manager On-Prem and CSSM.

In the URL field, be sure to enter the exact Smart Transport URL of Smart Software Manager On-Prem . Enter the protocol and FQDN of the satellite server prefixed to " SmartTransport " . This is an example of a valid transport URL: https://example.com/SmartTransport

For more information about installing or configuring Smart Software Manager On-Prem, see https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager.html .

Proxy Server : Optionally you can use this setting to have Expressway send usage information over the internet through a proxy server.
                                          Enter the following details:

Proxy address IPv4 address or FQDN of the proxy server.

Port Port on which the proxy server is listening for requests.

Username Username for authorizing requests at the proxy server.

Password Password for authenticating the authorized user.

Do not share my hostname or IP address with Cisco

Check this check box if the hostname and IP address of this Expressway product instance must not be exchanged with CSSM or
                                          Cisco Smart Software Manager On-Prem

Additional operations

The Additional operations drop-down list is activated after a successful registration.

Renew authorization now : Perform this operation if automatic authorization status renewal fails due to network connectivity issues with CSSM.

Renew registration now : Perform this operation if automatic registration renewal fails due to network connectivity issues with CSSM.

Deregister : The product reverts to Unregistered mode. All license entitlements used for the product are released immediately to the
                                                virtual account and are available for other product instances to use it. If the evaluation period has not expired, the product
                                                reverts to evaluation mode.

Product Instance Registration token

Enter the Product Instance Registration token that you generated from CSSM or Smart Software Manager On-Prem to register the
                                          product.

Reregister this product instance if it is already registered

Check this check box to reregister this Expressway product instance to a different virtual account.

Register

Click Register to register the Expressway with CSSM or Smart Software Manager On-Prem. (Changes to Reregister after successful registration.)

Licensing status

Registration status

Displays the registration status of this Expressway product instance:

Registered : Product is registered.

Unregistered : Product is not registered.

Unregistered : Registration Expired : Registration has expired for this product.

Unregistered : Registration Pending : Registration is in progress.

Unregistered : Registration Failed : Product registration failed because the token is invalid or expired.

License authorization status

Displays the license authorization status of this Expressway product instance.

Authorized : Product is authorized and in compliance state.

Authorization Expired : Authorization has expired. This usually happens if the product has not communicated with Cisco for 90 continuous days.

Out-of-compliance : Status for this product is out-of-compliance, due to insufficient licenses.

No Licenses in Use : No licenses are being consumed by the product.

Evaluation Mode : Product is in evaluation mode and not yet registered with Cisco.

Evaluation Expired : Evaluation period has expired.

Not Applicable : Product is unable to determine the current registration status.

Smart account

Displays information about the customer's Smart Account with Cisco. The Smart Account is created from the Request Smart Account option under the Administration section of Cisco Software Central .

Virtual account

A self-defined element to reflect the company organization. Licenses and Product instances can be distributed across virtual
                                          accounts. Created and maintained by an administrator on CSSM or Smart Software Manager On-Prem. The administrator needs full
                                          visibility to company assets.

Export-Controlled Functionality

Displays one of the following states:

Allowed : Export-controlled functionality is enabled in the token with which this product was registered.

Not Allowed : Export-controlled functionality is not enabled in the token with which this product was registered.

The Allow export-controlled functionality on the products registered with this token check box is not displayed for Smart Accounts that are not allowed to use Export-Controlled functionality.

License usage

Update usage details

License usage provides summary and detailed information on system license usage as it's reported to CSSM or Smart Software
                                          Manager On-Prem. The information is auto-updated every 6 hours.

Optionally you can manually update the usage details by clicking Update usage details . However, this is a resource intensive operation and we don't recommend using it frequently. It may take upwards of a minute
                                          depending on the size of the system.

Within a cluster if 1 node consumes more than the installed licenses then only the number of installed licenses will be reported.

For example, In a 2 node cluster, if each node has 10 licenses then 1 node can consume a maximum of 20 licenses. In that case,
                                          it will be reporting only the installed number of licenses that is, 10 licenses instead of 20 licenses.

For more information, see "Resource usage" section of the   "Overview" page in the Cisco Expressway Web User Interface .

License type

Lists the license types - Rich Media Session or Room/Desktop Registrations.

Current usage

Shows current license usage by license type. If a license type is not in use (being consumed) it is not displayed here.

Status

Displays the status of each license type.

Authorization Expired : Authorized period has expired.

Evaluation Mode : The agent is using the evaluation period for this entitlement.

Evaluation Expired : Evaluation period has expired.

Authorized : In compliance (authorized).

Invalid : Error condition state.

Invalid-tag : The entitlement tag is invalid.

Not Authorized : Enforcement mode is not applicable.

Out of compliance : Out of compliance.

Waiting : The initial state after an entitlement request while waiting for the authorization request response.

## Configure Smart Licensing

This section describes the tasks required to configure Smart Licensing.

### Before You Start

Review the cautions and other information in Before you Enable Smart Licensing .

The following additional configuration caveats apply:

The only supported transport protocol is HTTPS between Expressway and CSSM / Smart Software Manager On-Prem.

If a communication issue occurs with the registration server when you register the Expressway product instance, the registration
                                       fails with this message: The last attempt to renew smart software licensing registration is in progress because of the following reason: HTTP Server
                                          Error 200: Operation timed out .

The product instance reattempts to register at 15-minute intervals. Refresh the page on your browser after each reattempt,
                                       to check current registration status. If the communication issue is resolved during the reattempts, the product will be registered.
                                       If the product is not registered after multiple reattempts, verify if there is any communication issue with the registration
                                       server and manually reregister the product instance.

When you restore a system, the Smart Licensing settings that are restored depends on whether you restore the backup onto the
                                       same system or on a different system.

If you restore on the same system, the registration settings are restored on the restored system.

If you restore on a different system, you must register the product again with a registration key.

If you are configuring Smart Software Manager On-Prem, be sure to enter the exact URL of the Smart Transport component (details
                                       and an example are provided in Smart Licensing Settings ).

### Process Summary

Task 1: Obtain the Product Instance Registration Token

Task 2: Configure Transport Settings on Expressway

Task 3: Register with Cisco Smart Software Manager

### Obtain the Product Instance Registration Token

Step 1

Log in to your smart account in CSSM or Smart Software Manager On-Prem.

Step 2

Navigate to the virtual account that you want to associate with the Expressway.

Step 3

Generate a Product Instance Registration Token.

Step 4

Select the Allow export-controlled functionality on the products registered with this token check box to enable export-controlled functionality on the products registered with this token.

Caution

Use this option only if you are compliant with the export-controlled functionality.

By checking this check box and accepting the terms, you enable higher levels of product encryption for products registered
                                             with this Registration Token. By default, this check box is selected. You can uncheck this check box to disallow Export-Controlled
                                             functionality on a product.

The Allow export-controlled functionality on the products registered with this token check box is not displayed for Smart Accounts that are not permitted to use the Export-Controlled functionality.

Step 5

Copy the token or save it to another location.

### Configure Transport Settings on Expressway

Step 1

In the Expressway web interface, go to Maintenance > Smart licensing .

Step 2

Navigate to Transport settings and select one of the following transport options:

Direct Expressway sends usage information directly over the internet and no additional components are needed. This is the default.

Smart Software Manager On-Prem Expressway sends usage information to an on-premise CSSM.

Proxy Server Expressway sends usage information over the internet through a proxy server.

Details about the transport settings are provided in Smart Licensing Settings . Remember that if the Expressway product instance is already registered, you must first deregister it if you want to change
                                             transport settings from Direct (CSSM) to On-Prem, or the other way round.

Step 3

If the hostname and IP address of this product instance must not be exchanged with CSSM or Cisco Smart Software Manager On-Prem,
                                          check the setting Do not share my hostname or IP address with Cisco .

Step 4

Click Save .

### Register with Cisco Smart Software Manager

Step 1

In the Expressway web interface, go to Maintenance > Smart licensing .

Step 2

In the Registration section, paste the Product Instance Registration Token that you previously generated using CSSM or Smart Software Manager
                                          On-Prem.

Step 3

Click Register to complete the registration process. (After successful registration the button changes to Reregister .)

Step 4

In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system.

The configuration for Smart Licensing is now complete.

The following section describes how to manage Smart Licensing registrations and authorizations, including what to do if the
                                             Expressway hostname is changed in future, or if you decide to permanently shut it down.

### Important Configuration Information for Smart Licensing

Caution

After Smart Licensing is set to On you cannot reset to Off using the web interface. To go back to PAK-based licensing (or to change the system to a VCS) requires a factory reset. For
                                             detailed information on Factory Reset , see the chapter Smart Licensing , section Factory Reset in Cisco Expressway Administrator Guide (X14.2) . Because the reset will reinstall the software image and reset the Expressway configuration to the default, we strongly advise
                                             you to backup the Expressway data before you enable Smart Licensing.

After Smart Licensing is enabled, you cannot use option keys on the Expressway.

```
The last attempt to renew smart software licensing registration is in progress because of the 
following reason: HTTP Server Error 200: Operation timed out.
```

The product instance reattempts to register at 15-minute intervals. Refresh the page on your browser after each reattempt,
                                       to check current registration status. If the communication issue is resolved during the reattempts, the product will be registered.
                                       If the product is not registered after multiple reattempts, verify if there is any communication issue with the registration
                                       server and manually reregister the product instance.

When you restore a system, the Smart Licensing settings that are restored depends on whether you restore the backup onto the
                                       same system or on a different system.

If you restore on the same system, Smart Licensing will be enabled and the registration settings are restored on the restored
                                             system.

If you restore on a different system, Smart Licensing will be enabled on the restored system but you must register the product
                                             again with a registration key.

#### More details

For detailed product information about the Cisco Smart Software Manager, see Cisco Smart Software Manager . Or for information about the On-Prem Manager, see Smart Software Manager On-Prem .

For more information about how to configure Smart Licensing, see the chapter on Smart Licensing in Cisco Expressway Administrator Guide (X14.2) .

## Manage Smart Licensing Registrations and Authorizations

This section describes Smart Licensing operations, including:

Renew Authorization : Use to manually renew the License authorization status for all the licenses listed under the License type. The license authorization
                                    is renewed automatically every 30 days. The authorization status will expire after 90 days if it is not connected to CSSM
                                    or Smart Software Manager On-Prem.

Renew Registration : Use to renew the registration information manually. The initial registration is valid for one year. Renewal of registration
                                    is automatically done every six months provided the product is connected to CSSM or Smart Software Manager On-Prem.

Deregister : Use to disconnect the Expressway from CSSM or Smart Software Manager On-Prem. The product reverts to evaluation mode as
                                    long as the evaluation period is not expired. All license entitlements used for the product are immediately released back
                                    to the virtual account and are available for other product instances to use it.

Reregister License with Cisco Smart Software Manager : Use to reregister Expressway with CSSM or Smart Software Manager On-Prem. The product may migrate to a different virtual
                                    account by reregistering with a token from a new virtual account.

### Important Caveat

Smart Licensing Registration is a per-node operation. This means that a cluster of two or more peers requires every peer to
                              register with Smart Licensing.

### Renew Authorization

Use this procedure to manually renew the License authorization status for all the licenses listed under the License type . This process assumes that the product is registered with CSSM or Smart Software Manager On-Prem.

Step 1

In the Expressway web interface, go to Maintenance > Smart licensing .

Step 2

In the Action section, from the Additional operations drop-down list, choose Renew authorization now .

Step 3

Click Save .

Expressway sends a request to Cisco Smart Software Manager or Smart Software Manager On-Prem to check the "License Authorization Status" and Cisco Smart Software Manager or Smart Software Manager On-Prem reports back the status to Cisco Expressway.

Step 4

In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system.

### Renew Registration

During product registration to Cisco Smart Software Manager or Smart Software Manager On-Prem, a security association is used
                                 to identify the product and is anchored by the registration certificate, which has a lifetime of one year (the registration
                                 period). This is different from the registration token ID expiration, which has the time limit for the token to be active.
                                 This registration period is automatically renewed every 6 months. However, if there is an issue, you can manually renew this
                                 registration period.

This process assumes that the product is registered with CSSM or Smart Software Manager On-Prem.

Step 1

In the Expressway web interface, go to Maintenance > Smart licensing .

Step 2

In the Action section, from the Additional operations drop-down list, choose Renew registration now .

Step 3

Click Save .

Expressway sends a request to CSSM or Smart Software Manager On-Prem to check the "Registration Status" and CSSM / Smart Software Manager On-Prem reports the status to Cisco Unified Communications Manager.

Step 4

In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system.

### Deregister

Use this procedure to unregister an Expressway from CSSM or Smart Software Manager On-Prem and release all the licenses from
                                 the current virtual account. This procedure also disconnects the Expressway from CSSM / Smart Software Manager On-Prem. All
                                 license entitlements used for the product are released back to the virtual account and are available for other product instances
                                 to use.

If Expressway is unable to connect with CSSM or Smart Software Manager On-Prem, and the product is still deregistered, a warning
                                 message displays. The message notifies you to remove the product manually from CSSM / Smart Software Manager On-Prem to free
                                 up licenses.

Step 1

In the Expressway web interface, go to Maintenance > Smart licensing .

Step 2

In the Action section, from the Additional operations drop-down list, choose Deregister .

Step 3

Click Save .

Step 4

In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system.

### Reregister with Cisco Smart Software Manager

Use this procedure to reregister the Expressway with CSSM or Smart Software Manager On-Prem. You need the Product Instance
                                 Registration Token (see Manage Smart Licensing Registrations and Authorizations ).

Step 1

From the web interface, choose Maintenance > Smart licensing .

Step 2

In the Registration section, paste the "Registration Token Key" that you generated using the CSSM or Smart Software Manager On-Prem.

Step 3

Click Reregister to complete the reregistration process.

Step 4

In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system.

### How to Register a Change to the Expressway Hostname

If the Expressway hostname is changed, to reflect the change in CSSM, go to the Expressway Smart Licensing web page and click " Renew Registration Now " .

### Deregister First if Expressway is Permanently Shutdown

We recommend that if you plan to shutdown an Expressway machine permanently, you first deregister the product instance from
                                 the Expressway Smart Licensing web page. This is to avoid leaving unused product instances in CSSM.

In case you forget to do so, there is an alternate approach to remove the Expressway product instance from the CSSM portal.

This step is not needed for restarts or temporary shutdowns.

## About Cisco Smart License Reservation and Its Types

Cisco Smart License Reservation is meant to reserve licenses and install them on the device. This process enables you to generate
                              a unique reservation code from your Cisco device, which is then used to reserve a license type and quantity from your Cisco
                              Smart Account’s inventory.

The following are the license reservation types:

Permanent License Reservation (PLR): All licenses are reserved.

Specific License Reservation (SLR): Only specific licenses are reserved.

The following processes are common for both Permanent License Reservation (PLR) and Specific License Reservation (SLR).

### Reserving a New Smart License

Section Purpose: This section outlines the procedure to reserve a new smart license for use.

The user can specify and reserve licenses against the product. For more information, see Requesting License Reservation for Your Smart Account . After the authorization code is exchanged, regular product synchronization is not required until there are changes in the
                              reservation. Reserved licenses remain blocked in the Cisco Smart Software Manager unless released from the product with a
                              return code.

### Updating a Smart License Reservation

Use the Cisco Smart Software Manager to update or change reserved licenses (increase or decrease). You can install a new authorization
                              code on the Product and obtain a confirmation code. The new changes remain in transit status unless confirmation code from
                              the product is installed on the Cisco Smart Software Manager.

### Removing the Product Instance from CSSM

You can remove the product from the smart account and release all the licenses that are reserved for that Product Instance
                              (Expressway) when licenses are reserved on a Product Instance (Expressway).

Product Instance is operational (graceful removal): Users can create a Reservation Return Code on the Product Instance (which removes the Authorization Code) using the Cisco
                              Smart Software Manager and return the Specific License Reservation Authorization.

User can use only the CLI configuration to enable Permanent License Reservation and Specific License Reservation.

### Functionality

Customers entitled to License reservation feature on their Smart Account can reserve licenses from their virtual account,
                              tie them to a devices Unique Device Identifier (UDI) and use their device with these reserved licenses in a disconnected mode.
                              The customer reserves specific licenses and counts the UDI from their virtual account.

### CLI Commands for PLR and SLR

The table lists a set of CLI commands applicable for PLR and SLR.

#### Prerequisites

Enable smart licensing before executing the reservation commands.

Select the appropriate PLR or SLR licenses using the CLI commands before running the smart licensing commands.

CLI Command

Description

xconfiguration License Smart ReservationEnable:  On

Enables license reservation feature.

xcommand License Smart Reservation Request

Prints the "Reservation Request Code" . Paste this into the portal to start the reservation process.

xcommand License Smart Reservation Install "<authorization code>"

Enters the "Reservation Authorization Code" into the device to complete the process.

xcommand License Smart Reservation Return

Prints the "Reservation Return Code" . Paste this into the portal to return licenses and delete the product instance.

This uses the previously installed authorization code.

xcommand License Smart Reservation ReturnAuthorization <auth code>

Prints the "Reservation Return Code" . Paste this into the portal to return licenses and delete the product instance.

Uses the authorization code from the command line.

Note: An extra authorization is not necessary for smart license reservation return authorization code.

xcommand License Smart Reservation Cancel

Cancels a reservation that is in progress and allows entitlement changes.

### Permanent License Reservation

Permanent License Reservation (PLR) is a part of Cisco smart licensing solution. Smart Licensing needs a smart account. The
                                 product must connect to the Cisco Smart Software Management (CSSM) or Smart Software Manage (SSM On-Prem) in order to reactivate
                                 and report the most recent license status. You will use Cisco Permanent License Reservation or PLR license if you have extremely
                                 secured inner networks with restricted internet access.

You can apply Permanent licenses over evaluation licenses, and also apply it incrementally (that is, you can have multiple
                                 permanent licenses, and so on). Its capabilities are designed for highly secure environments, where communication with outside
                                 environment is impossible.

#### How does PLR Licenses Work?

Permanent License Reservation is a permanent solution for highly secure network architecture where all outbound connections
                                 are limited. PLR license allows you to register all product instances along with unlimited features (along with all entitlements
                                 on Expressway till the physical capacity of the Expressway box) and permanently (no renewal needed) using a reservation code.
                                 This solution is similar to traditional PAK licenses and is mostly available for Cisco Secure product lines. Furthermore,
                                 PLR licenses counts as an easy-to-use and intuitive solution which can be applied easily on different devices. In addition,
                                 you can provide a single authorization code to permanently enable all features or eliminate various features and expiration
                                 dates.

#### How to Apply PLR Licenses?

There are a few Command Line Interface (CLI) commands. These commands can generate a reservation code. You can use the reservation
                                 code to receive a unique authorization code. Entering this Authorization Code in CLI will permanently activate all features.

#### Task Flow

You can use a set of commands through the Command Line Interface (CLI) to call the Smart Agent and obtain the required information.
                                 You can paste this information on the Cisco Smart Software Manager (CSSM) portal.

This reservation is also called Online-Offline mode. You must be online to register and use the reservation. First, deregister
                                 yourself if you have already registered to enable reservation and start the process.

Complete these tasks to reserve permanent licenses for Expressway.

##### Enable Reservation

Use this procedure to enable Permanent License Reservation.

Reservation is disabled by default. You must enable it.

###### Before you begin

Expressway is unregistered with Cisco Smart Software Manager or On-Prem.

From Expressway Admin Console, execute the command.

```
xconfiguration License Smart ReservationEnable: On

OK
```

Now you can start the process.

###### What to do next

For information on the procedure to generate reservation request code from the Expressway product, see the steps on Reservation Request Code .

##### Reservation Request Code

Use this procedure to generate reservation request code from the Expressway product.

###### Before you begin

```
xconfiguration License Smart ReservationEnable: On
```

Step 1

Execute the following command from the Expressway Admin Console.

```
xcommand License Smart Reservation Request
<code is generated>
```

Invoke this command to obtain the code from Smart Agent Reservation Request. After the code is generated, copy the code and
                                                   paste it into the CSSM portal ( Smart Software Licensing page).

This will start the process and generate the authorization code in CSSM.

Step 2

Log into Cisco Smart Software Manager (CSSM) from https://software.cisco.com/#. .

Use the Cisco provided username and password to Log in to the Cisco SSM portal.

Click Inventory > Licenses tab > License Reservation... .

This displays the Smart License Reservation window.

The is the default tab.

In the Reservation Request Code field, paste the reservation request code that is generated from Expressway.

Click Next .

This displays the tab.

Choose Expressway PLR without Export Control from Licenses to Reserve .

Click Next .

This displays the tab.

Click Generate Authorization Code .

The code is generated in the Authorization Code field.

Copy the code and navigate to the Expressway Admin Console.

###### What to do next

For information on the procedure to install license reservation authorization code generated from Cisco Smart Software Manager,
                                       see the steps on Install License Reservation Authorization Code from CSSM .

##### Install License Reservation Authorization Code from CSSM

Use this procedure to install license reservation authorization code generated from Cisco Smart Software Manager.

###### Before you begin

Execute these commands in sequence:

xconfiguration License Smart ReservationEnable

xcommand License Smart Reservation Request

Step 1

Execute the command from the Expressway Admin Console:

```
xcommand License Smart Reservation Install <authorization code>
```

Remember

In the command, paste the <authorization code> copied from the CSSM portal.

Execute this command to install the code and all licenses. In the Permanent Reservation License, you do not choose anything
                                                   but will install the entire package. This completes the process of Reservation.

Step 2

Navigate to Cisco Smart Software Manager (CSSM) portal.

From the tab, click Close .

###### What to do next

For information on the procedure to generate a return code, see the steps on Return Reservation Code .

##### Return Reservation Code

Use this procedure to generate a return code. You must enter this code into the Cisco Smart Software Manager (CSSM) to return
                                       the licenses to the virtual account pool and remove the product instance from CSSM.

###### Before you begin

Execute the following commands in sequence:

xconfiguration License Smart ReservationEnable

xcommand License Smart Reservation Request

xcommand License Smart Reservation Install <authorization code>

Step 1

From Expressway Admin Console, execute the command.

```
xcommand License Smart Reservation Return
```

This generates a return code. Copy the code and paste it in the CSSM portal in order to return the previously installed permanent
                                                   licenses.

Step 2

Navigate to the Cisco Smart Software Manager (CSSM) portal, Smart Software Licensing page, follow the path: Click Inventory > Product Instances tab.

This displays the available list of product instances.

Step 3

Locate an appropriate product instance where the licenses are installed. Optionally, you can enter a name or product type
                                                string in the search tab to locate the product instance or Time and Date stamp or Serial Number of the machine.

Step 4

Click the Actions drop-down list from the Actions column. and choose Remove

Result: This displays the Remove Product Instance popup window.

Step 5

Paste the reservation return code in the Reservation Return Code field.

Step 6

Click Remove Product Instance .

This removes the reservation information and makes the license available in the virtual account.

###### What to do next

For information on the procedure to cancel the reservation process, see the steps on Cancel the Reservation Process .

##### Cancel the Reservation Process

Use this procedure to cancel the reservation process before the authorization code from Cisco Smart Software Manager (CSSM)
                                       against Expressway request code is installed.

###### Before you begin

Execute the following commands in sequence:

xconfiguration License Smart ReservationEnable

xcommand License Smart Reservation Request

Step 1

Execute the command from Expressway Admin Console:

```
xcommand License Smart Reservation Request
```

Step 2

Copy the request code.

Step 3

Navigate to Cisco Smart Software Manager (CSSM) portal.

Step 4

Click Inventory > Licenses > License Reservation... .

This displays the Smart License Reservation window.

The is the default tab.

Step 5

In the Reservation Request Code field, paste the request code that is generated from Product Instance - Expressway.

Step 6

Click Next to generate the Authorization Code.

This displays the tab.

Step 7

Choose Expressway PLR without Export Control from Licenses to Reserve .

Step 8

Click Next .

This displays the tab.

Step 9

Click Generate Authorization Code .

This generates code in the Authorization Code field.

Remember

Now, do not install the authorization code since you are canceling the reservation.

Step 10

Navigate to the Expressway Admin Console and execute this command:

```
xcommand License Smart Reservation Cancel

OK
```

Step 11

Navigate to Cisco Smart Software Manager (CSSM) portal, copy the <authorization code> that is generated.

###### What to do next

For information on the procedure to generate a return code for the authorization code you have not yet installed, see the
                                       steps on Generate a Return Code for the Authorization Code to complete the process.

##### Generate a Return Code for the Authorization Code

Use this procedure to generate a return code for the authorization code you have not yet installed. Enter the return code
                                       into the Cisco Smart Software Manager to return the licenses to the virtual account pool and remove the product instance from
                                       CSSM.

###### Before you begin

Execute the following commands in sequence:

xconfiguration License Smart ReservationEnable

xcommand License Smart Reservation Request

Step 1

Navigate to the Expressway Admin Console and execute the command:

```
xcommand License Smart Reservation ReturnAuthorization <auth code>
                           (paste the authorization code from CSSM)
```

<Reservation Return Code> is generated.

In order to complete the process, copy the <generated reservation return code> from the Expressway Admin Console.

Step 2

Navigate to the Cisco Smart Software Manager (CSSM) portal.

Step 3

Click Inventory > Product Instances tab from the Smart Software Licensing page.

The displays the list of available product instances.

Step 4

Locate an appropriate product instance where the licenses are installed. Optionally, you can enter a name or product type
                                                string in the search tab to locate the product instance or Time and Date stamp or Serial Number of the machine.

Step 5

Click Actions drop-down list from the Actions column and choose Remove .

Result: This displays the Remove Product Instance popup window.

Step 6

Paste the reservation return code in the Reservation Return Code field.

Step 7

Click Remove Product Instance .

Step 8

From the tab, click Close .

### Specific License Reservation

Specific License Reservation is a feature that is used in highly secure networks. It provides a method for customers to deploy
                                 a software license on a device (Product Instance - Expressway) without communicating usage information.

#### Task Flow

##### Enable Reservation

Use this procedure to enable Specific License Reservation.

Reservation is disabled by default. You must enable it.

###### Before you begin

Expressway is unregistered with Cisco Smart Software Manager or On-Prem.

Execute this command from the Expressway Admin Console.

```
xconfiguration License Smart ReservationEnable: On

OK
```

Now you can start the process.

###### What to do next

For information on the procedure to generate reservation request code from the Expressway product, see the steps on Reservation Request Code .

##### Reservation Request Code

Use this procedure to generate reservation request code from the Expressway product.

###### Before you begin

```
xconfiguration License Smart ReservationEnable: On
```

Step 1

Execute the following command from the Expressway Admin Console.

```
xcommand License Smart Reservation Request
<request code is generated>
```

Invoke this command to obtain the code from the Smart Agent Reservation Request. After the code is generated, copy the code
                                                   and paste it into the CSSM portal ( Smart Software Licensing page).

This will start the process and generate the authorization code in CSSM.

Step 2

Log into Cisco Smart Software Manager (CSSM) from https://software.cisco.com/#. .

Use the Cisco provided username and password to log in to the Cisco SSM portal.

Click Inventory > Licenses tab > License Reservation... .

This displays the Smart License Reservation window.

The is the default tab.

In the Reservation Request Code field, paste the reservation request code that is generated from Expressway.

Click Next .

This displays the tab.

Choose Reserve a specific license from Licenses to Reserve .

In the Quantity to Reserve field, enter the numeral adjacent to the required license.

Information

Here you can choose the number of licenses and the type of license to reserve. You can choose between version 12 and version
                                                                     14 that Expressway uses to communicate with both the versions of UCM. The Expressway Advanced Account Security Entitlement
                                                                     is linked with Export Control. Make sure that you do not choose 0 in the quality to reserve field. Choosing 0 will not allow
                                                                     enabling Export Control.

Click Next .

This displays the tab.

Click Generate Authorization Code .

The code is generated in the Authorization Code field.

This authorization code is slightly different from the code generated in Permanent License Reservation.

Copy the code and navigate to the Expressway Admin Console.

Step 3

Navigate to the Expressway Admin Console.

###### What to do next

For information on the procedure to install license reservation authorization code generated from Cisco Smart Software Manager,
                                       see the steps on Install License Reservation Authorization Code from CSSM .

##### Install License Reservation Authorization Code from CSSM

Use this procedure to install license reservation authorization code generated from Cisco Smart Software Manager.

###### Before you begin

Execute the following commands in sequence:

xconfiguration License Smart ReservationEnable

xcommand License Smart Reservation Request

Step 1

Execute the command from the Expressway Admin Console.

```
xcommand License Smart Reservation Install "<authorization code>"
```

Information

This is an XML file. Make sure you insert the code within double quotes.

Remember

In the Expressway Admin Console, paste the "<authorization code>" that is copied from the CSSM portal.

Result: This displays the message that the installation is successful. Along with this message, a confirmation code is also generated
                                                   on the product after the authorization code is successfully installed.

This is different from Permanent License Reservation (PLR). This confirmation code is used whenever you must update the licenses.

Step 2

Navigate to the Cisco Smart Software Manager (CSSM) portal.

###### What to do next

For information on the procedure to update the license reservation for your product instance and get a new authorization code,
                                       see the steps on Update License Reservation .

##### Update License Reservation

Use this procedure to update the license reservation for your product instance and get a new authorization code.

###### Before you begin

Execute the following command:

xconfiguration License Smart ReservationEnable

xcommand License Smart Reservation Request

xcommand License Smart Reservation Install "<authorization code>"

Step 1

Follow the path, click Inventory > Product Instances tab from the Cisco Smart Software Manager (CSSM)  portal.

The displays the list of available product instances.

Step 2

Locate an appropriate product instance where the licenses are installed. Optionally, you can enter a name or product type
                                                string in the search tab to locate the product instance or Time and Date stamp or Serial Number of the machine.

Step 3

Click the Actions drop-down list from the Actions column and choose Update Reserved Licenses .

This displays the Update License Reservation window.

The tab and is selected by default.

Step 4

Select Reserve a specific license from Licenses to Reserve ..

You can view the previously reserved licenses and modify them.

Step 5

In the Quantity to Reserve field adjacent the corresponding license, enter/modify the number of licenses you want to reserve.

Step 6

Click Next .

This displays the tab. You can review the license reservation information.

Step 7

Click Generate Authorization Code .

The code is generated in the Authorization Code field.

Step 8

After generating the authorization code, click Copy to Clipboard to copy the authorization, or Download as File to download the file and save it to the Flash drive or the TFTP server.

Step 9

Navigate to the Expressway Admin Console and paste the code in the command:

```
xcommand License Smart Reservation Install "<authorization code>"
```

Information

This is an XML file. Make sure you insert the code within double quotes.

Remember

In the Expressway Admin Console, paste the "<authorization code>" that is copied from the CSSM portal.

Result: The installation is successful message appears. Along with the message, a confirmation code is also generated on the product
                                                   after the authorization code is successfully installed.

Step 10

Copy the <Confirmation Code>.

Step 11

Navigate to the Cisco Smart Software Manager (CSSM) portal to complete the process of updating the licenses.

Step 12

Click Enter Confirmation Code .

This displays the Enter Confirmation Code window.

Step 13

Paste the confirmation code in the Reservation Confirmation Code field.

Step 14

Click OK .

A message that the licenses are successfully reserved appears. Thus the licenses are updated.

###### What to do next

For information on the procedure to generate a return code, see the steps on Return Reservation Code .

##### Return Reservation Code

Use this procedure to generate a return code that must be entered into the Cisco Smart Software Manager to return the licenses
                                       to the virtual account pool and remove the product instance from CSSM.

###### Before you begin

Execute the following command:

xconfiguration License Smart ReservationEnable

xcommand License Smart Reservation Request

xcommand License Smart Reservation Install "<authorization code>"

Step 1

Execute this command from the Expressway Admin Console.

```
xcommand License Smart Reservation Return
```

This command is executed after successful installation.

This generates a <Return Code>. Copy the return code and paste it in the CSSM portal.

Step 2

Navigate to the Cisco Smart Software Manager (CSSM) portal, Smart Software Licensing page, follow the path, click Inventory > Product Instances tab.

The displays the list of available product instances.

Step 3

Locate an appropriate product instance where the licenses are installed. Optionally, you can enter a name or product type
                                                string in the search tab to locate the product instance or Time and Date stamp or Serial Number of the machine.

Step 4

Click the Actions drop-down list from the Actions column and choose Remove .

Result: This displays the Remove Product Instance popup window.

Step 5

Paste the reservation return code in the Reservation Return Code field.

Step 6

Click Remove Product Instance .

A message that the Product Instance was successfully removed appears.

Step 7

From the tab, click Close .

###### What to do next

For information on the procedure to cancel the reservation process, see the steps on Cancel the Reservation Process .

##### Cancel the Reservation Process

Use this procedure to cancel the reservation process before the authorization code from Cisco Smart Software Manager (CSSM)
                                       against Expressway request code is installed.

###### Before you begin

Execute the following commands in sequence:

xconfiguration License Smart ReservationEnable

xcommand License Smart Reservation Request

Step 1

Execute the command from Expressway Admin Console.

```
xcommand License Smart Reservation Request
```

Step 2

Copy the request code.

Step 3

Navigate to Cisco Smart Software Manager (CSSM) portal.

Step 4

Click Inventory > Licenses > License Reservation... .

This displays the Smart License Reservation window.

The is the default tab.

Step 5

In the Reservation Request Code field, paste the request code that is generated from Product Instance - Expressway.

Step 6

Click Next to generate the Authorization Code.

This displays the tab.

Step 7

Choose Reserve a specific license from Licenses to Reserve .

Step 8

Click Next .

This displays the tab.

Step 9

Click Generate Authorization Code .

This generates code in the Authorization Code field.

Remember

Now, do not install the authorization code since you are canceling the reservation.

Step 10

Navigate to the Expressway Admin Console and execute this command:

```
xcommand License Smart Reservation Cancel

OK
```

Step 11

Navigate to Cisco Smart Software Manager (CSSM) portal, copy the <authorization code> that is generated.

###### What to do next

For information on the procedure to generate a return code for the authorization code you have not yet installed, see the
                                       steps on Generate a Return Code for the Authorization Code to complete the process.

##### Generate a Return Code for the Authorization Code

Use this procedure to generate a return code for the authorization code you have not yet installed. Enter the return code
                                       into the Cisco Smart Software Manager to return the licenses to the virtual account pool and remove the product instance from
                                       CSSM.

###### Before you begin

Execute the following commands in sequence:

xconfiguration License Smart ReservationEnable

xcommand License Smart Reservation Request

Step 1

Navigate to the Expressway Admin Console and execute the command:

```
xcommand License Smart Reservation ReturnAuthorization "<auth code>"
                           (paste the authorization code from CSSM)
```

<Reservation Return Code> is generated.

Information

This is an XML file. Make sure you insert the code within double quotes.

In order to complete the process, copy the <generated reservation return code> from the Expressway Admin Console.

Step 2

Navigate to the Cisco Smart Software Manager (CSSM) portal.

Step 3

Click Inventory > Product Instances tab from the Smart Software Licensing page.

The displays the list of available product instances.

Step 4

Locate an appropriate product instance where the licenses are installed. Optionally, you can enter a name or product type
                                                string in the search tab to locate the product instance or Time and Date stamp or Serial Number of the machine.

Step 5

Click Actions drop-down list from the Actions column and choose Remove .

Result: This displays the Remove Product Instance popup window.

Step 6

Paste the reservation return code in the Reservation Return Code field.

Step 7

Click Remove Product Instance .

Step 8

From the tab, click Close .

### Additional Information

Make sure that Smart Licensing is enabled and Expressway is in Specific License Reservation (SLR) mode.

#### Sharing of Licenses Across Nodes in a Cluster

Consider Node 1 and Node 2 where,

Node 1 : 10 Desk Registrations + 10 Rich Media Session (RMS)

Node 2 : 10 Desk Registrations + 10 RMS

Explanation : 10 RMS licenses are consumed when there are 10 Business to Business (B2B) calls made from Node 1.

A cluster license is shared among all the nodes. For example, Node 1 has 10 licenses, if 11th endpoint tries to register then
                                 the Node automatically borrows 1 license from other nodes.

Information: The license is borrowed only if there are no available RMS licenses in Node 1.

This behavior is similar to PAK-based licenses.

#### Reporting of the License Consumption to Smart Agent

The license consumption is reported to the Smart Agent over pre-configured intervals.

Within a cluster if 1 node consumes more than the installed licenses then only the number of installed licenses will be reported.

For example, In a 2 node cluster, if each node has 10 licenses then 1 node can consume a maximum of 20 licenses. In that case,
                                 it will be reporting only the installed number of licenses that is, 10 licenses instead of 20 licenses.

### Limitation

Make sure that Smart Licensing is enabled and Expressway is in Specific License Reservation (SLR) mode.

#### Hard Enforce Entitlement for SLR/Expiry of Smart License Reservation Licenses

After the license expires, there is no impact on the registration of calling functionalities of the Expressway device until
                                 it is restarted.

After the Expressway device is restarted, if the license has expired, the respective functionality will stop and an alarm
                                 is triggered.

The functionality associated with license expiry does stop immediately since the device triggers a notification only upon
                                 restart.

## Smart Licensing Export Compliance

The Export Limit of 2500 registrations/calls/sessions is On by default for all customers. This means that now every customer will not be able to create more than 2500 encrypted connections.

Advanced Account Security is not available.

From X14.2, FIPS140-2 Cryptographic Mode is available.

FIPS140-2 mode is only available on Cisoc Video Communication Server (VCS) with the Advanced Security option key and Expressway Select , not Expressway (Export Control Restricted version).

Encrypted signaling sessions to endpoints’ is capped at 2500.

### Export Control Alarms

The Export Control approaching alarm and approached alarm are raised once calls and registration capacity have reached 90%
                                 and 100% of the export control limit, respectively.

Export Control limit is ideally set to a count of 2500 (Calls+Registrations). This applies to both Smart Licensing Connected and Reservation mode(s).

For more information, see " Alarms Reference ".

### Additional Information

The following are the values used for Export Control.

#### Lower Watermark for Export Control

In Export Control, a lower watermark is introduced to update if the export control limit is reached or not. The lower watermark
                                 is a 1% value of the current export control limit (~2500).

This is to avoid call(s) to change notification when there is a frequent change in the resource usage value.

For example, if the export control limit is reached (~2500). Consequently, a few calls and registrations are dropped. In the
                                 current scenario, it is considered that the export limit is reached only when calls or registrations drop until 25 (1% of
                                 2500). New Registrations or Calls are allowed only when the resource usage value is below 2475. This is to avoid call(s) to
                                 change notification between 100% to 99% range.

#### Export Control Limit When WebRTC  is Enabled

When WebRTC is enabled on either Cisco Expressway-C or Cisco Expressway-E, the Export Control limit value is set to 2244,
                                 since the maximum WebRTC connections allowed on the Expressway C or E is 256.

When the WebRTC value is disabled, the Export Control limit is set back to 2500.

#### Restore Process in Smart Licensing Model

You can backup settings on one Expressway and restore it to a different Expressway. For example, You can use this feature
                                 when the original system has failed. Before restoring, install the option keys assigned in the original system to the new
                                 system.

If you are using the Smart Licensing model, re-apply the token (in case there are multiple users) or assign a new token before
                                 restoring the backup file.

#### VCS Behavior

The 2500 Limit is applicable to VCS also. But the requirement to go over the limit with crypto key is not available. From
                                 X14.2, VCS always will be within the limit and there is no crypto key to go above the 2500 limit.

## Limitations

### Product License Registration - Issue with Converting to Smart Licensing

This item applies if you want to convert existing Expressway licenses (RMS, Desktop, or Room) to Smart Licensing entitlements.
                              In this case do not use the option in the Cisco Product License Registration portal to partially convert just some of the
                              licenses. Due to a known issue, if you opt to convert only some licenses, the system automatically forfeits/removes the remaining
                              licenses as well. So the licenses that are not converted are also removed, and a licensing case will be required to retrieve
                              them.

To avoid this happening, please ensure that the Quantity to Convert field is the same value as the Quantity Available field; this is the default when you open the page.

### Smart Licensing not Available With Features that Use Option Keys (including HSM)

The following Expressway features are enabled by option keys. Because option keys are incompatible with Smart Licensing, if
                              you need these features, you must use PAK-based licensing and not Smart Licensing:

Advanced account security

HSM (Hardware Security Module)

Microsoft Interoperability

### Expressway Reporting "Unknown CA" for Smart Licensing Through Proxy Server with Intercept Mode

The Expressway does NOT initiate connections with a proxy or a smart licensing server. A smart licensing agent component initiates
                              these connections. The smart licensing agent validates certificates using its trust store list. Users cannot change this list. Therefore, the device rejects connections to any proxy server presenting a CA signed
                              certificate other than the "QuoVadis Root CA 2" with an "Unknown CA" error.

### Expressway Reporting "Unknown CA" for ACME Service Through Proxy Server with Intercept Mode

The Expressway does NOT support accessing ACME service (Automated Certificate Management Environment) through a proxy with
                              Intercept mode enabled .

| Note | Cisco Expressway X14.2 only supports Smart Licensing and is capped at 2500 encrypted signaling sessions to endpoints. It also includes changes in the
                                       trafficserver behavior (bug ID CSCwc69661 refers) that can lead to MRA failures - see here . For detailed information, see the Cisco Expressway and Cisco TelePresence Video Communication Server Release Note (x14.2) and Cisco Expressway Administrator Guide (X14.2) before upgrading to X14.2 . |
|---|---|

| Important | Product Activation Keys (PAK) Licensing (Option Keys) are removed from version X14.2. Smart License is default and the only licensing mode for Expressway-C and Expressway-E. We recommend you to enable Smart License before upgrading Expressway to version X14.2. This will help while reverting to a
                                             previous image. You are not allowed to add the Microsoft Interoperability (MS Interop) key from version X14.2. This functionality is available
                                             only in cases where you have the MS Interop options before upgrade. But once on X14.2, you cannot add MS Interop key. Once Smart Licensing is turned ON, you do not have an option for reverting to Cisco VCS through Service Select . Once Smart Licensing is turned ON, you cannot disable it and revert to legacy licensing. There is no option available to revert
                                             it to Cisco VCS (except for a Factory Reset ), either. For Cisco VCS, legacy/option key license mode remains the only licensing mode. When Cisco VCS is converted to Expressway Series X14.2, Smart License mode is turned ON automatically. Smart Licensing is FIPS compliant. For more information, see Prerequisites for Configuring FIPS140-2 Cryptographic Mode. In Smart License mode, the functionality is enabled by default and hence they are not needed or supported and may not be
                                             converted in the License Registration Portal . |
|---|---|

| Note | Use the chosen flags (if you have any) when you perform a factory reset or you will be prompted with the following list if
                                                   you do not give any flags in the command. |
|---|---|

| Note | After Factory Reset, if the MS Interop option key is on the device, it will be preserved. |
|---|---|

| Navigate to the Cisco Software Central web page: https://software.cisco.com/ The Cisco Software Central page is displayed. Note You need a Smart Account to use Smart Licensing. | Note | You need a Smart Account to use Smart Licensing. |
|---|---|---|
| Note | You need a Smart Account to use Smart Licensing. |

| Note | You need a Smart Account to use Smart Licensing. |
|---|---|

| Caution | After Smart Licensing is enabled, the only way to revert to PAK-based licensing (or to convert an Expressway system to a Cisco
                                          VCS system) is with a factory reset. Because a factory reset reinstalls the software image and resets the Expressway configuration
                                          to the default, we strongly advise you to backup the Expressway data before you enable Smart Licensing. |
|---|---|

| Note | This section describes the web interface. For information about CLI commands for Smart Licensing, see the Command Reference section of this guide. |
|---|---|

| Field | Description |
|---|---|
| Smart licensing mode | Enables Smart Licensing on this Expressway product instance. Before you select this option, review the Smart Licensing Settings section. Note It is always recommended to take a configuration backup in order to avoid any partial or complete configuration lost scenario. | Note | It is always recommended to take a configuration backup in order to avoid any partial or complete configuration lost scenario. |
| Note | It is always recommended to take a configuration backup in order to avoid any partial or complete configuration lost scenario. |
| Transport settings | Determines how this Expressway product instance communicates with CSSM to send and receive usage information. Caution If the Expressway product instance is already registered, you must first deregister it if you want to change transport settings
                                                      from Direct (CSSM) to On-Prem, or the other way round. Choose Transport settings under licensing page, as per your smart licensing deployment model. | Caution | If the Expressway product instance is already registered, you must first deregister it if you want to change transport settings
                                                      from Direct (CSSM) to On-Prem, or the other way round. |
| Caution | If the Expressway product instance is already registered, you must first deregister it if you want to change transport settings
                                                      from Direct (CSSM) to On-Prem, or the other way round. |
| Transport settings | Direct : Expressway sends usage information directly over the internet and no additional components are needed. This is the default
                                          setting. To use the Direct option, you must configure DNS settings on Expressway so that it can resolve cisco.com . If you choose not to configure the domain and DNS on Expressway, you can instead select Smart Software Manager On-Prem or
                                          proxy server. If you choose not to use the DNS server in your deployment and not to connect to the internet, you can select
                                          the Smart Software Manager On-Prem with manual synchronization in disconnected mode. Smart Software Manager On-Prem : Expressway sends usage information to an on-premise CSSM. Periodic information exchange keeps the databases in sync between
                                          Smart Software Manager On-Prem and CSSM. In the URL field, be sure to enter the exact Smart Transport URL of Smart Software Manager On-Prem . Enter the protocol and FQDN of the satellite server prefixed to " SmartTransport " . This is an example of a valid transport URL: https://example.com/SmartTransport For more information about installing or configuring Smart Software Manager On-Prem, see https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager.html . Proxy Server : Optionally you can use this setting to have Expressway send usage information over the internet through a proxy server.
                                          Enter the following details: Proxy address IPv4 address or FQDN of the proxy server. Port Port on which the proxy server is listening for requests. Username Username for authorizing requests at the proxy server. Password Password for authenticating the authorized user. |
| Do not share my hostname or IP address with Cisco | Check this check box if the hostname and IP address of this Expressway product instance must not be exchanged with CSSM or
                                          Cisco Smart Software Manager On-Prem |
| Additional operations | The Additional operations drop-down list is activated after a successful registration. Renew authorization now : Perform this operation if automatic authorization status renewal fails due to network connectivity issues with CSSM. Renew registration now : Perform this operation if automatic registration renewal fails due to network connectivity issues with CSSM. Deregister : The product reverts to Unregistered mode. All license entitlements used for the product are released immediately to the
                                                virtual account and are available for other product instances to use it. If the evaluation period has not expired, the product
                                                reverts to evaluation mode. |
| Product Instance Registration token | Enter the Product Instance Registration token that you generated from CSSM or Smart Software Manager On-Prem to register the
                                          product. |
| Reregister this product instance if it is already registered | Check this check box to reregister this Expressway product instance to a different virtual account. |
| Register | Click Register to register the Expressway with CSSM or Smart Software Manager On-Prem. (Changes to Reregister after successful registration.) |
| Licensing status |
| Registration status | Displays the registration status of this Expressway product instance: Registered : Product is registered. Unregistered : Product is not registered. Unregistered : Registration Expired : Registration has expired for this product. Unregistered : Registration Pending : Registration is in progress. Unregistered : Registration Failed : Product registration failed because the token is invalid or expired. |
| License authorization status | Displays the license authorization status of this Expressway product instance. Authorized : Product is authorized and in compliance state. Authorization Expired : Authorization has expired. This usually happens if the product has not communicated with Cisco for 90 continuous days. Out-of-compliance : Status for this product is out-of-compliance, due to insufficient licenses. No Licenses in Use : No licenses are being consumed by the product. Evaluation Mode : Product is in evaluation mode and not yet registered with Cisco. Evaluation Expired : Evaluation period has expired. Not Applicable : Product is unable to determine the current registration status. |
| Smart account | Displays information about the customer's Smart Account with Cisco. The Smart Account is created from the Request Smart Account option under the Administration section of Cisco Software Central . |
| Virtual account | A self-defined element to reflect the company organization. Licenses and Product instances can be distributed across virtual
                                          accounts. Created and maintained by an administrator on CSSM or Smart Software Manager On-Prem. The administrator needs full
                                          visibility to company assets. |
| Export-Controlled Functionality | Displays one of the following states: Allowed : Export-controlled functionality is enabled in the token with which this product was registered. Not Allowed : Export-controlled functionality is not enabled in the token with which this product was registered. The Allow export-controlled functionality on the products registered with this token check box is not displayed for Smart Accounts that are not allowed to use Export-Controlled functionality. |
| License usage |
| Update usage details | License usage provides summary and detailed information on system license usage as it's reported to CSSM or Smart Software
                                          Manager On-Prem. The information is auto-updated every 6 hours. Optionally you can manually update the usage details by clicking Update usage details . However, this is a resource intensive operation and we don't recommend using it frequently. It may take upwards of a minute
                                          depending on the size of the system. Within a cluster if 1 node consumes more than the installed licenses then only the number of installed licenses will be reported. For example, In a 2 node cluster, if each node has 10 licenses then 1 node can consume a maximum of 20 licenses. In that case,
                                          it will be reporting only the installed number of licenses that is, 10 licenses instead of 20 licenses. Note For more information, see "Resource usage" section of the   "Overview" page in the Cisco Expressway Web User Interface . | Note | For more information, see "Resource usage" section of the   "Overview" page in the Cisco Expressway Web User Interface . |
| Note | For more information, see "Resource usage" section of the   "Overview" page in the Cisco Expressway Web User Interface . |
| License type | Lists the license types - Rich Media Session or Room/Desktop Registrations. |
| Current usage | Shows current license usage by license type. If a license type is not in use (being consumed) it is not displayed here. |
| Status | Displays the status of each license type. Authorization Expired : Authorized period has expired. Evaluation Mode : The agent is using the evaluation period for this entitlement. Evaluation Expired : Evaluation period has expired. Authorized : In compliance (authorized). Invalid : Error condition state. Invalid-tag : The entitlement tag is invalid. Not Authorized : Enforcement mode is not applicable. Out of compliance : Out of compliance. Waiting : The initial state after an entitlement request while waiting for the authorization request response. |

| Note | It is always recommended to take a configuration backup in order to avoid any partial or complete configuration lost scenario. |
|---|---|

| Caution | If the Expressway product instance is already registered, you must first deregister it if you want to change transport settings
                                                      from Direct (CSSM) to On-Prem, or the other way round. |
|---|---|

| Note | For more information, see "Resource usage" section of the   "Overview" page in the Cisco Expressway Web User Interface . |
|---|---|

| Step 1 | Log in to your smart account in CSSM or Smart Software Manager On-Prem. |
|---|---|
| Step 2 | Navigate to the virtual account that you want to associate with the Expressway. |
| Step 3 | Generate a Product Instance Registration Token. |
| Step 4 | Select the Allow export-controlled functionality on the products registered with this token check box to enable export-controlled functionality on the products registered with this token. Caution Use this option only if you are compliant with the export-controlled functionality. By checking this check box and accepting the terms, you enable higher levels of product encryption for products registered
                                             with this Registration Token. By default, this check box is selected. You can uncheck this check box to disallow Export-Controlled
                                             functionality on a product. The Allow export-controlled functionality on the products registered with this token check box is not displayed for Smart Accounts that are not permitted to use the Export-Controlled functionality. | Caution | Use this option only if you are compliant with the export-controlled functionality. |
| Caution | Use this option only if you are compliant with the export-controlled functionality. |
| Step 5 | Copy the token or save it to another location. |

| Caution | Use this option only if you are compliant with the export-controlled functionality. |
|---|---|

| Step 1 | In the Expressway web interface, go to Maintenance > Smart licensing . |
|---|---|
| Step 2 | Navigate to Transport settings and select one of the following transport options: Direct Expressway sends usage information directly over the internet and no additional components are needed. This is the default. Smart Software Manager On-Prem Expressway sends usage information to an on-premise CSSM. Proxy Server Expressway sends usage information over the internet through a proxy server. Details about the transport settings are provided in Smart Licensing Settings . Remember that if the Expressway product instance is already registered, you must first deregister it if you want to change
                                             transport settings from Direct (CSSM) to On-Prem, or the other way round. |
| Step 3 | If the hostname and IP address of this product instance must not be exchanged with CSSM or Cisco Smart Software Manager On-Prem,
                                          check the setting Do not share my hostname or IP address with Cisco . |
| Step 4 | Click Save . |

| Step 1 | In the Expressway web interface, go to Maintenance > Smart licensing . |
|---|---|
| Step 2 | In the Registration section, paste the Product Instance Registration Token that you previously generated using CSSM or Smart Software Manager
                                          On-Prem. |
| Step 3 | Click Register to complete the registration process. (After successful registration the button changes to Reregister .) |
| Step 4 | In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system. The configuration for Smart Licensing is now complete. The following section describes how to manage Smart Licensing registrations and authorizations, including what to do if the
                                             Expressway hostname is changed in future, or if you decide to permanently shut it down. |

| Caution | After Smart Licensing is set to On you cannot reset to Off using the web interface. To go back to PAK-based licensing (or to change the system to a VCS) requires a factory reset. For
                                             detailed information on Factory Reset , see the chapter Smart Licensing , section Factory Reset in Cisco Expressway Administrator Guide (X14.2) . Because the reset will reinstall the software image and reset the Expressway configuration to the default, we strongly advise
                                             you to backup the Expressway data before you enable Smart Licensing. |
|---|---|

| Step 1 | In the Expressway web interface, go to Maintenance > Smart licensing . |
|---|---|
| Step 2 | In the Action section, from the Additional operations drop-down list, choose Renew authorization now . |
| Step 3 | Click Save . Expressway sends a request to Cisco Smart Software Manager or Smart Software Manager On-Prem to check the "License Authorization Status" and Cisco Smart Software Manager or Smart Software Manager On-Prem reports back the status to Cisco Expressway. |
| Step 4 | In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system. |

| Step 1 | In the Expressway web interface, go to Maintenance > Smart licensing . |
|---|---|
| Step 2 | In the Action section, from the Additional operations drop-down list, choose Renew registration now . |
| Step 3 | Click Save . Expressway sends a request to CSSM or Smart Software Manager On-Prem to check the "Registration Status" and CSSM / Smart Software Manager On-Prem reports the status to Cisco Unified Communications Manager. |
| Step 4 | In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system. |

| Step 1 | In the Expressway web interface, go to Maintenance > Smart licensing . |
|---|---|
| Step 2 | In the Action section, from the Additional operations drop-down list, choose Deregister . |
| Step 3 | Click Save . |
| Step 4 | In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system. |

| Step 1 | From the web interface, choose Maintenance > Smart licensing . The Smart licensing window appears. |
|---|---|
| Step 2 | In the Registration section, paste the "Registration Token Key" that you generated using the CSSM or Smart Software Manager On-Prem. |
| Step 3 | Click Reregister to complete the reregistration process. |
| Step 4 | In the License usage section, click Update usage details to manually update the system license usage information. This is resource-intensive and may take a few minutes depending
                                          on the size of the system. |

| Note | The following processes are common for both Permanent License Reservation (PLR) and Specific License Reservation (SLR). |
|---|---|

| Note | User can use only the CLI configuration to enable Permanent License Reservation and Specific License Reservation. |
|---|---|

| CLI Command | Description |
|---|---|
| xconfiguration License Smart ReservationEnable:  On | Enables license reservation feature. |
| xcommand License Smart Reservation Request | Prints the "Reservation Request Code" . Paste this into the portal to start the reservation process. |
| xcommand License Smart Reservation Install "<authorization code>" | Enters the "Reservation Authorization Code" into the device to complete the process. |
| xcommand License Smart Reservation Return | Prints the "Reservation Return Code" . Paste this into the portal to return licenses and delete the product instance. This uses the previously installed authorization code. |
| xcommand License Smart Reservation ReturnAuthorization <auth code> | Prints the "Reservation Return Code" . Paste this into the portal to return licenses and delete the product instance. Uses the authorization code from the command line. Note: An extra authorization is not necessary for smart license reservation return authorization code. |
| xcommand License Smart Reservation Cancel | Cancels a reservation that is in progress and allows entitlement changes. |

| Note | Reservation is disabled by default. You must enable it. |
|---|---|

| From Expressway Admin Console, execute the command. xconfiguration License Smart ReservationEnable: On

OK Now you can start the process. |
|---|

| Step 1 | Execute the following command from the Expressway Admin Console. xcommand License Smart Reservation Request
<code is generated> Invoke this command to obtain the code from Smart Agent Reservation Request. After the code is generated, copy the code and
                                                   paste it into the CSSM portal ( Smart Software Licensing page). This will start the process and generate the authorization code in CSSM. |
|---|---|
| Step 2 | Log into Cisco Smart Software Manager (CSSM) from https://software.cisco.com/#. . Use the Cisco provided username and password to Log in to the Cisco SSM portal. Click Inventory > Licenses tab > License Reservation... . This displays the Smart License Reservation window. The is the default tab. In the Reservation Request Code field, paste the reservation request code that is generated from Expressway. Click Next . This displays the tab. Choose Expressway PLR without Export Control from Licenses to Reserve . Click Next . This displays the tab. Click Generate Authorization Code . The code is generated in the Authorization Code field. Copy the code and navigate to the Expressway Admin Console. |

| Step 1 | Execute the command from the Expressway Admin Console: xcommand License Smart Reservation Install <authorization code> Remember In the command, paste the <authorization code> copied from the CSSM portal. Execute this command to install the code and all licenses. In the Permanent Reservation License, you do not choose anything
                                                   but will install the entire package. This completes the process of Reservation. Result: A message appears that the installation is successful after all the steps are completed. | Remember | In the command, paste the <authorization code> copied from the CSSM portal. |
|---|---|---|---|
| Remember | In the command, paste the <authorization code> copied from the CSSM portal. |
| Step 2 | Navigate to Cisco Smart Software Manager (CSSM) portal. From the tab, click Close . |

| Remember | In the command, paste the <authorization code> copied from the CSSM portal. |
|---|---|

| Step 1 | From Expressway Admin Console, execute the command. xcommand License Smart Reservation Return This generates a return code. Copy the code and paste it in the CSSM portal in order to return the previously installed permanent
                                                   licenses. |
|---|---|
| Step 2 | Navigate to the Cisco Smart Software Manager (CSSM) portal, Smart Software Licensing page, follow the path: Click Inventory > Product Instances tab. This displays the available list of product instances. |
| Step 3 | Locate an appropriate product instance where the licenses are installed. Optionally, you can enter a name or product type
                                                string in the search tab to locate the product instance or Time and Date stamp or Serial Number of the machine. |
| Step 4 | Click the Actions drop-down list from the Actions column. and choose Remove Result: This displays the Remove Product Instance popup window. |
| Step 5 | Paste the reservation return code in the Reservation Return Code field. |
| Step 6 | Click Remove Product Instance . Result: A message that the Product Instance was successfully removed appears. This removes the reservation information and makes the license available in the virtual account. |

| Step 1 | Execute the command from Expressway Admin Console: xcommand License Smart Reservation Request Result: <Reservation Request Code> is generated. |
|---|---|
| Step 2 | Copy the request code. |
| Step 3 | Navigate to Cisco Smart Software Manager (CSSM) portal. |
| Step 4 | Click Inventory > Licenses > License Reservation... . This displays the Smart License Reservation window. The is the default tab. |
| Step 5 | In the Reservation Request Code field, paste the request code that is generated from Product Instance - Expressway. |
| Step 6 | Click Next to generate the Authorization Code. This displays the tab. |
| Step 7 | Choose Expressway PLR without Export Control from Licenses to Reserve . |
| Step 8 | Click Next . This displays the tab. |
| Step 9 | Click Generate Authorization Code . This generates code in the Authorization Code field. Remember Now, do not install the authorization code since you are canceling the reservation. | Remember | Now, do not install the authorization code since you are canceling the reservation. |
| Remember | Now, do not install the authorization code since you are canceling the reservation. |
| Step 10 | Navigate to the Expressway Admin Console and execute this command: xcommand License Smart Reservation Cancel

OK |
| Step 11 | Navigate to Cisco Smart Software Manager (CSSM) portal, copy the <authorization code> that is generated. |

| Remember | Now, do not install the authorization code since you are canceling the reservation. |
|---|---|

| Step 1 | Navigate to the Expressway Admin Console and execute the command: xcommand License Smart Reservation ReturnAuthorization <auth code>
                           (paste the authorization code from CSSM) <Reservation Return Code> is generated. In order to complete the process, copy the <generated reservation return code> from the Expressway Admin Console. |
|---|---|
| Step 2 | Navigate to the Cisco Smart Software Manager (CSSM) portal. |
| Step 3 | Click Inventory > Product Instances tab from the Smart Software Licensing page. The displays the list of available product instances. |
| Step 4 | Locate an appropriate product instance where the licenses are installed. Optionally, you can enter a name or product type
                                                string in the search tab to locate the product instance or Time and Date stamp or Serial Number of the machine. |
| Step 5 | Click Actions drop-down list from the Actions column and choose Remove . Result: This displays the Remove Product Instance popup window. |
| Step 6 | Paste the reservation return code in the Reservation Return Code field. |
| Step 7 | Click Remove Product Instance . Result: A message that the Product Instance was successfully removed appears. |
| Step 8 | From the tab, click Close . Result: This completes the process. |

| Note | Reservation is disabled by default. You must enable it. |
|---|---|

| Execute this command from the Expressway Admin Console. xconfiguration License Smart ReservationEnable: On

OK Now you can start the process. |
|---|

| Step 1 | Execute the following command from the Expressway Admin Console. xcommand License Smart Reservation Request
<request code is generated> Invoke this command to obtain the code from the Smart Agent Reservation Request. After the code is generated, copy the code
                                                   and paste it into the CSSM portal ( Smart Software Licensing page). This will start the process and generate the authorization code in CSSM. |
|---|---|
| Step 2 | Log into Cisco Smart Software Manager (CSSM) from https://software.cisco.com/#. . Use the Cisco provided username and password to log in to the Cisco SSM portal. Click Inventory > Licenses tab > License Reservation... . This displays the Smart License Reservation window. The is the default tab. In the Reservation Request Code field, paste the reservation request code that is generated from Expressway. Click Next . This displays the tab. Choose Reserve a specific license from Licenses to Reserve . In the Quantity to Reserve field, enter the numeral adjacent to the required license. Information Here you can choose the number of licenses and the type of license to reserve. You can choose between version 12 and version
                                                                     14 that Expressway uses to communicate with both the versions of UCM. The Expressway Advanced Account Security Entitlement
                                                                     is linked with Export Control. Make sure that you do not choose 0 in the quality to reserve field. Choosing 0 will not allow
                                                                     enabling Export Control. Click Next . This displays the tab. Click Generate Authorization Code . The code is generated in the Authorization Code field. Note This authorization code is slightly different from the code generated in Permanent License Reservation. Copy the code and navigate to the Expressway Admin Console. | Information | Here you can choose the number of licenses and the type of license to reserve. You can choose between version 12 and version
                                                                     14 that Expressway uses to communicate with both the versions of UCM. The Expressway Advanced Account Security Entitlement
                                                                     is linked with Export Control. Make sure that you do not choose 0 in the quality to reserve field. Choosing 0 will not allow
                                                                     enabling Export Control. | Note | This authorization code is slightly different from the code generated in Permanent License Reservation. |
| Information | Here you can choose the number of licenses and the type of license to reserve. You can choose between version 12 and version
                                                                     14 that Expressway uses to communicate with both the versions of UCM. The Expressway Advanced Account Security Entitlement
                                                                     is linked with Export Control. Make sure that you do not choose 0 in the quality to reserve field. Choosing 0 will not allow
                                                                     enabling Export Control. |
| Note | This authorization code is slightly different from the code generated in Permanent License Reservation. |
| Step 3 | Navigate to the Expressway Admin Console. |

| Information | Here you can choose the number of licenses and the type of license to reserve. You can choose between version 12 and version
                                                                     14 that Expressway uses to communicate with both the versions of UCM. The Expressway Advanced Account Security Entitlement
                                                                     is linked with Export Control. Make sure that you do not choose 0 in the quality to reserve field. Choosing 0 will not allow
                                                                     enabling Export Control. |
|---|---|

| Note | This authorization code is slightly different from the code generated in Permanent License Reservation. |
|---|---|

| Step 1 | Execute the command from the Expressway Admin Console. xcommand License Smart Reservation Install "<authorization code>" Information This is an XML file. Make sure you insert the code within double quotes. Remember In the Expressway Admin Console, paste the "<authorization code>" that is copied from the CSSM portal. Result: This displays the message that the installation is successful. Along with this message, a confirmation code is also generated
                                                   on the product after the authorization code is successfully installed. Note This is different from Permanent License Reservation (PLR). This confirmation code is used whenever you must update the licenses. | Information | This is an XML file. Make sure you insert the code within double quotes. | Remember | In the Expressway Admin Console, paste the "<authorization code>" that is copied from the CSSM portal. | Note | This is different from Permanent License Reservation (PLR). This confirmation code is used whenever you must update the licenses. |
|---|---|---|---|---|---|---|---|
| Information | This is an XML file. Make sure you insert the code within double quotes. |
| Remember | In the Expressway Admin Console, paste the "<authorization code>" that is copied from the CSSM portal. |
| Note | This is different from Permanent License Reservation (PLR). This confirmation code is used whenever you must update the licenses. |
| Step 2 | Navigate to the Cisco Smart Software Manager (CSSM) portal. |

| Information | This is an XML file. Make sure you insert the code within double quotes. |
|---|---|

| Remember | In the Expressway Admin Console, paste the "<authorization code>" that is copied from the CSSM portal. |
|---|---|

| Note | This is different from Permanent License Reservation (PLR). This confirmation code is used whenever you must update the licenses. |
|---|---|

| Step 1 | Follow the path, click Inventory > Product Instances tab from the Cisco Smart Software Manager (CSSM)  portal. The displays the list of available product instances. |
|---|---|
| Step 2 | Locate an appropriate product instance where the licenses are installed. Optionally, you can enter a name or product type
                                                string in the search tab to locate the product instance or Time and Date stamp or Serial Number of the machine. |
| Step 3 | Click the Actions drop-down list from the Actions column and choose Update Reserved Licenses . This displays the Update License Reservation window. The tab and is selected by default. |
| Step 4 | Select Reserve a specific license from Licenses to Reserve .. You can view the previously reserved licenses and modify them. |
| Step 5 | In the Quantity to Reserve field adjacent the corresponding license, enter/modify the number of licenses you want to reserve. |
| Step 6 | Click Next . This displays the tab. You can review the license reservation information. |
| Step 7 | Click Generate Authorization Code . The code is generated in the Authorization Code field. |
| Step 8 | After generating the authorization code, click Copy to Clipboard to copy the authorization, or Download as File to download the file and save it to the Flash drive or the TFTP server. |
| Step 9 | Navigate to the Expressway Admin Console and paste the code in the command: xcommand License Smart Reservation Install "<authorization code>" Information This is an XML file. Make sure you insert the code within double quotes. Remember In the Expressway Admin Console, paste the "<authorization code>" that is copied from the CSSM portal. Result: The installation is successful message appears. Along with the message, a confirmation code is also generated on the product
                                                   after the authorization code is successfully installed. | Information | This is an XML file. Make sure you insert the code within double quotes. | Remember | In the Expressway Admin Console, paste the "<authorization code>" that is copied from the CSSM portal. |
| Information | This is an XML file. Make sure you insert the code within double quotes. |
| Remember | In the Expressway Admin Console, paste the "<authorization code>" that is copied from the CSSM portal. |
| Step 10 | Copy the <Confirmation Code>. |
| Step 11 | Navigate to the Cisco Smart Software Manager (CSSM) portal to complete the process of updating the licenses. |
| Step 12 | Click Enter Confirmation Code . This displays the Enter Confirmation Code window. |
| Step 13 | Paste the confirmation code in the Reservation Confirmation Code field. |
| Step 14 | Click OK . A message that the licenses are successfully reserved appears. Thus the licenses are updated. |

| Information | This is an XML file. Make sure you insert the code within double quotes. |
|---|---|

| Remember | In the Expressway Admin Console, paste the "<authorization code>" that is copied from the CSSM portal. |
|---|---|

| Step 1 | Execute this command from the Expressway Admin Console. xcommand License Smart Reservation Return This command is executed after successful installation. This generates a <Return Code>. Copy the return code and paste it in the CSSM portal. |
|---|---|
| Step 2 | Navigate to the Cisco Smart Software Manager (CSSM) portal, Smart Software Licensing page, follow the path, click Inventory > Product Instances tab. The displays the list of available product instances. |
| Step 3 | Locate an appropriate product instance where the licenses are installed. Optionally, you can enter a name or product type
                                                string in the search tab to locate the product instance or Time and Date stamp or Serial Number of the machine. |
| Step 4 | Click the Actions drop-down list from the Actions column and choose Remove . Result: This displays the Remove Product Instance popup window. |
| Step 5 | Paste the reservation return code in the Reservation Return Code field. |
| Step 6 | Click Remove Product Instance . A message that the Product Instance was successfully removed appears. |
| Step 7 | From the tab, click Close . |

| Step 1 | Execute the command from Expressway Admin Console. xcommand License Smart Reservation Request Result: <Reservation Request Code> is generated> |
|---|---|
| Step 2 | Copy the request code. |
| Step 3 | Navigate to Cisco Smart Software Manager (CSSM) portal. |
| Step 4 | Click Inventory > Licenses > License Reservation... . This displays the Smart License Reservation window. The is the default tab. |
| Step 5 | In the Reservation Request Code field, paste the request code that is generated from Product Instance - Expressway. |
| Step 6 | Click Next to generate the Authorization Code. This displays the tab. |
| Step 7 | Choose Reserve a specific license from Licenses to Reserve . |
| Step 8 | Click Next . This displays the tab. |
| Step 9 | Click Generate Authorization Code . This generates code in the Authorization Code field. Remember Now, do not install the authorization code since you are canceling the reservation. | Remember | Now, do not install the authorization code since you are canceling the reservation. |
| Remember | Now, do not install the authorization code since you are canceling the reservation. |
| Step 10 | Navigate to the Expressway Admin Console and execute this command: xcommand License Smart Reservation Cancel

OK |
| Step 11 | Navigate to Cisco Smart Software Manager (CSSM) portal, copy the <authorization code> that is generated. |

| Remember | Now, do not install the authorization code since you are canceling the reservation. |
|---|---|

| Step 1 | Navigate to the Expressway Admin Console and execute the command: xcommand License Smart Reservation ReturnAuthorization "<auth code>"
                           (paste the authorization code from CSSM) <Reservation Return Code> is generated. Information This is an XML file. Make sure you insert the code within double quotes. In order to complete the process, copy the <generated reservation return code> from the Expressway Admin Console. | Information | This is an XML file. Make sure you insert the code within double quotes. |
|---|---|---|---|
| Information | This is an XML file. Make sure you insert the code within double quotes. |
| Step 2 | Navigate to the Cisco Smart Software Manager (CSSM) portal. |
| Step 3 | Click Inventory > Product Instances tab from the Smart Software Licensing page. The displays the list of available product instances. |
| Step 4 | Locate an appropriate product instance where the licenses are installed. Optionally, you can enter a name or product type
                                                string in the search tab to locate the product instance or Time and Date stamp or Serial Number of the machine. |
| Step 5 | Click Actions drop-down list from the Actions column and choose Remove . Result: This displays the Remove Product Instance popup window. |
| Step 6 | Paste the reservation return code in the Reservation Return Code field. |
| Step 7 | Click Remove Product Instance . Result: A message that the Product Instance was successfully removed appears. |
| Step 8 | From the tab, click Close . Result: This completes the process. |

| Information | This is an XML file. Make sure you insert the code within double quotes. |
|---|---|

| Note | Make sure that Smart Licensing is enabled and Expressway is in Specific License Reservation (SLR) mode. |
|---|---|

| Note | This behavior is similar to PAK-based licenses. |
|---|---|

| Note | Make sure that Smart Licensing is enabled and Expressway is in Specific License Reservation (SLR) mode. |
|---|---|

| Note | The Export Limit of 2500 registrations/calls/sessions is On by default for all customers. This means that now every customer will not be able to create more than 2500 encrypted connections. Advanced Account Security is not available. From X14.2, FIPS140-2 Cryptographic Mode is available. FIPS140-2 mode is only available on Cisoc Video Communication Server (VCS) with the Advanced Security option key and Expressway Select , not Expressway (Export Control Restricted version). Encrypted signaling sessions to endpoints’ is capped at 2500. |
|---|---|