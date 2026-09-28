---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-admin-12-5-1su3-systemconfig-cucm-b-system-configuration-guide-1251su3--85372a9b2e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/admin/12_5_1SU3/systemConfig/cucm_b_system-configuration-guide-1251su3/cucm_m_smart-software-licensing-rev.html
retrieved_at: 2026-08-16T17:40:45.424393+00:00
---

System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

# System Configuration Guide for Cisco Unified Communications Manager, Release 12.5(1)SU3

Updated: July 31, 2025

Chapter: Smart Software Licensing

## Chapter: Smart Software Licensing

# Smart Software Licensing

## Smart Software Licensing Overview

Cisco Smart Software Licensing is a new way of thinking about licensing. It adds flexibility to your licensing and simplifies
                           it across the enterprise. It also delivers visibility into your license ownership and consumption.

Cisco Smart Software Licensing helps you to procure, deploy, and manage licenses easily where devices self-register and report
                           license consumption, removing the need for product activation keys (PAK). It pools license entitlements in a single account
                           and allows you to move licenses freely through the network, wherever you need them. It is enabled across Cisco products and
                           managed by a direct cloud-based or mediated deployment model.

The Cisco Smart Software Licensing service registers the product instance, reports license usage, and obtains the necessary
                           authorization from Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

You can use Smart Licensing to:

See the license usage and count

See the status of each license type

See the product licenses available on Cisco Smart Software Manager or Cisco Smart Software Manager satellite

Renew License Authorization with Cisco Smart Software Manager or Cisco Smart Software Manager satellite

Renew the License Registration

Deregister with Cisco Smart Software Manager or Cisco Smart Software Manager satellite

The License authorization is valid for 90 days with a renewal at least once in 30 days. The authorization will expire after
                                       90 days if it is not connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

If the Cisco Smart Software Manager satellite option is selected, the satellite must have an internet connection to Cisco
                                       Smart Software Manager for the authorization to occur. The Cisco Smart Software Manager satellite can operate in 2 modes:
                                       Connected Mode in which the connection time is configurable, and Disconnected mode which requires a manual sync.

There are two main deployment options for Smart Licensing:

Cisco Smart Software Manager

Cisco Smart Software Manager satellite

### Cisco Smart Software Manager

The Cisco Smart Software Manager is a cloud-based service that handles your system licensing. Use this option if Unified
                              Communications Manager can connect to cisco.com, either directly or via a proxy server. Cisco Smart Software Manager allows
                              you to:

Manage and track licenses

Move licenses across virtual account

Remove registered product instance

Optionally, if Unified Communications Manager cannot connect directly to Cisco Smart Software Manager, you can deploy a proxy
                              server to manage the connection.

For additional information about Cisco Smart Software Manager, go to https://software.cisco.com .

### Cisco Smart Software Manager Satellite

Cisco Smart Software Manager satellite is an on-premise deployment that can handle your licensing needs if Unified Communications
                              Manager cannot connect to cisco.com directly, either for security or availability reasons. When this option is deployed, Unified
                              Communications Manager registers and report license consumption to the satellite, which synchronizes its database regularly
                              with the backend Cisco Smart Software Manager that is hosted on cisco.com.

The Cisco Smart Software Manager satellite can be deployed in either Connected or Disconnected mode, depending on whether
                              the satellite can connect directly to cisco.com.

Connected—Used when there is connectivity to cisco.com directly from the Smart Software Manager satellite. Smart account synchronization
                                    occurs automatically.

Disconnected—Used when there is no connectivity to cisco.com from the Smart Software Manager satellite. Smart Account synchronization
                                    must be manually uploaded and downloaded.

The Unified CM running in Dual Stack mode supports satellite configured with IPv4 and IPv6 address.

For Cisco Smart Software Manager satellite information and documentation, go to https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager-satellite.html .

### License Types

The following
                                 		licensing types are available to cover your needs:

Cisco
                                       				Unified Workspace Licensing (UWL) provides the most popular bundles of Cisco
                                       				Collaboration applications and services in a cost-effective, simple package. It
                                       				includes soft clients, applications server software, and licensing on a
                                       				per-user basis.

User Connect
                                       				Licensing (UCL) is a per-user based license for individual Cisco Unified
                                       				Communications applications, which includes the applications server software,
                                       				user licensing, and a soft client. Depending on the type of device and number
                                       				of devices that you require, UCL is available in Essential, Basic, Enhanced,
                                       				and Enhanced Plus versions.

For more
                                       				information about these license types and the versions in which they are
                                       				available, see http://www.cisco.com/c/en/us/products/unified-communications/unified-communications-licensing/index.html .

Session Management Edition can be registered to either Cisco Smart Software Manager or Cisco Smart Software Manager satellite.
                                       You can register Session Management Edition using the same processes as for Unified Communications Manager, register to a
                                       virtual account that Cisco Unified Communications Manager is registered or a separate virtual account, and fulfill a minimal
                                       set of licenses requirement.

The SME registered in Specific License Reservation (SLR) requires a minimum set of licenses reserved in CSSM while generating
                                                   an SLR authorization code.

### Product Instance
                           	 Evaluation Mode

Evaluation period is before the product is registered.

## System Licensing Prerequisites

### Planning your System Licensing

Review and understand the
                              			 Unified Communications (UC) licensing structure. For details, see http://www.cisco.com/c/en/us/products/unified-communications/unified-communications-licensing/index.html .

Plan how you are going to connect Unified Communications Manager to the Smart Software Manager service:

Direct connection to Cisco Smart Software Manager on cisco.com—Unified Communications Manager connects directly to the Cisco
                                    Smart Software Manager on cisco.com. With this option, you must configure DNS on Unified Communications Manager that resolves tools.cisco.com for Call Home.

Connection to Smart Software Manager via proxy server—Unified Communications Manager connects to a proxy server, or transport gateway , which connects to the Cisco Smart Software Manager service on cisco.com. DNS is not required on Unified Communications Manager,
                                    but you do need to configure DNS on the proxy server that can resolve tools.cisco.com for Call Home.

Connection to Smart Software Manager via Transport Gateway—Unified Communications Manager connects to a transport gateway,
                                    which connects to the Cisco Smart Software Manager service on cisco.com . DNS is not required on Unified Communications Manager, but you do need to configure DNS on the proxy server that can resolve tools.cisco.com . Smart Transport is not supported for Transport gateway.

Connection to on-premise Cisco Smart Software Manager satellite—Unified Communications Manager connects to an on-premise Smart
                                    Software Manager satellite. DNS is not required on Unified Communications Manager. DNS that can resolve tools.cisco.com for Call Home is required on the satellite server if you are deploying Connected mode. DNS is not required on the satellite
                                    server if you are deploying Disconnected mode.

### Smart Licensing Enrollment

Set
                              		  up Smart and Virtual accounts. For details, see https://software.cisco.com/ .

(Optional) If you want to deploy a Cisco Smart Software Manager satellite, install, and set up the satellite. Refer to documentation,
                              including the Smart Software Manager satellite Installation Guide . You can find documentation at https://www.cisco.com/c/en/us/buy/smart-accounts/software-manager-satellite.html .

## Smart Software
                        	 Licensing Task Flow

Complete these tasks to set up system licensing for Unified Communications Manager.

Step 1

Obtain the Product Instance Registration Token .

Use this
                                          				procedure to generate a product instance registration token for your virtual
                                          				account.

Step 2

Configure Connection to Smart Software Licensing (Applicable Until Release 14SU4 and 15SU2)

Step 3

Register with Cisco Smart Software Manager .

Perform this step to register Unified Communications Manager with Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

### Obtain the Product
                           	 Instance Registration Token

#### Before you begin

Obtain the product
                                 		  instance registration token from Cisco Smart Software Manager or Cisco Smart
                                 		  Software Manager satellite to register the product instance. Tokens can be
                                 		  generated with or without the Export-Controlled functionality feature being
                                 		  enabled.

Step 1

Log in to
                                          			 your smart account in either Cisco Smart Software Manager or your Cisco Smart
                                          			 Software Manager satellite.

Step 2

Navigate to the virtual account with which you want to associate the Unified Communications Manager cluster.

Step 3

Generate a "Product
                                             				Instance Registration Token" .

Select the Allow export-controlled functionality on the products
                                                            					 registered with this token check box to turn on the
                                                         				  Export-Controlled functionality for tokens of a product instance you wish in
                                                         				  this smart account. By checking this check box and accepting the terms, you
                                                         				  enable higher levels of the product encryption for products registered with
                                                         				  this Registration Token. By default, this check box is selected. You can
                                                         				  uncheck this check box if you wish not to allow the Export-Controlled
                                                         				  functionality to be made available for use with this token.

Caution

Use this option only if you are compliant with the
                                                         				  Export-Controlled functionality.

The Allow export-controlled functionality on the products
                                                            					 registered with this token check box is not displayed for the Smart
                                                         				  Accounts that are not permitted to use the Export-Controlled functionality.

Step 4

Copy the token
                                          			 or save it to another location.

For more
                                             				information, see https://software.cisco.com/ .

### Configure Connection to Smart Software Licensing (Applicable Until Release 14SU4 and 15SU2)

Complete this task to connect Unified Communications Manager to the Smart Software Licensing service.

Step 1

From Cisco Unified CM Administration, choose System > Licensing > License
                                                				  Management .

Step 2

From the Smart Software Licensing section, click the View/Edit the Licensing Smart Call Home settings link.

Step 3

Select the method of connecting Unified Communications Manager to the Smart Licensing service:

Direct —Unified Communications Manager connects directly to the Smart Software Manager on cisco.com. This is the default option.
                                                With this option, you must deploy DNS on Unified Communications Manager that can resolve tools.cisco.com .

Transport Gateway —Unified Communications Manager connects to an on-premise Cisco Smart Software Manager satellite or Transport Gateway for
                                                system licensing. In the URL text box, enter the address and port of the Smart Software Manager satellite or Transport Gateway.
                                                For example, fqdn_of_smart_software_manager:port_number . For HTTPS, use port 443.

HTTP/HTTPS Proxy —Unified Communications Manager connects to a proxy server, which connects to the Cisco Smart Software Manager service along
                                                with Transport Gateway also along with satellite on cisco.com. Enter the IP address or hostname of the proxy server along
                                                with the port:

IP Address/Host Name

Port—For HTTPS, use port 443.

Step 4

Check the Do not share my hostname or IP address with Cisco check box to restrict Unified Communications Manager from sharing its IP address and hostname during the Smart Licensing
                                          registration.

Step 5

Click Save .

### Register with
                           	 Cisco Smart Software Manager

Use this procedure
                                 		  to register your product with Cisco Smart Software Manager or Cisco Smart
                                 		  Software Manager satellite. Until you register, your product is still in
                                 		  Evaluation Mode.

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Licensing > License
                                                				  Management .

Step 2

From the Smart
                                             				Software Licensing section, click the Register button.

Step 3

In the Product
                                             				Instance Registration Token section, paste the copied or saved "Registration
                                             				Token Key" that you generated using the Smart Software Manager or Smart
                                          			 Software Manager satellite.

Step 4

Click Register to complete the registration process.

Step 5

Click Close . For more information, see the online help.

Step 6

In the License
                                             				Usage Report section, click Update
                                             				Usage Details to manually update the system license usage
                                          			 information.

Usage information is updated once every 24 hours automatically. For more information, see the online help.

## Additional Tasks with Smart Software Licensing

Step 1

Renew Authorization

Complete this task to manually renew the License Authorization Status for all the license listed under the License Type.

The license authorization is renewed automatically every 30 days. The authorization status will expire after 90 days if it
                                                      is not connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

If the Cisco Smart Software Manager satellite option is selected, the satellite must have an internet connection to Cisco
                                                      Smart Software Manager for the authorization to occur. The Cisco Smart Software Manager satellite can operate in 2 modes:
                                                      Connected Mode in which the connection time is configurable, and Disconnected mode which requires a manual sync.

Step 2

Renew Registration

Complete this task to renew the registration information manually.

The initial registration is valid for one year. Renewal of registration is automatically done every six months provided the
                                                      product is connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

Step 3

Deregister

Complete this task to disconnect the Unified Communications Manager cluster from Cisco Smart Software Manager or Cisco Smart
                                          Software Manager satellite. The product reverts to evaluation mode as long as the evaluation period is not expired. All license
                                          entitlements used for the product are immediately released back to the virtual account and are available for other product
                                          instances to use it.

Step 4

Reregister License with Cisco Smart Software Manager

Complete this task to reregister Unified Communications Manager with Cisco Smart Software Manager or Cisco Smart Software
                                          Manager satellite.

Product may migrate to a different virtual account by reregistering with token from a new virtual account.

### Renew
                           	 Authorization

Use this procedure
                                 		  to manually renew the License Authorization Status for all the licenses listed
                                 		  under the License Type.

The license authorization is renewed automatically every 30 days. The authorization status will expire after 90 days if it
                                             is not connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite.

If the Cisco Smart Software Manager satellite option is selected, the satellite must have an internet connection to Cisco
                                             Smart Software Manager for the authorization to occur. The Cisco Smart Software Manager satellite can operate in 2 modes:
                                             Connected Mode in which the connection time is configurable, and Disconnected mode  which requires a manual sync.

#### Before you begin

The product should
                                 		  be registered with Cisco Smart Software Manager or Cisco Smart Software Manager
                                 		  satellite.

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Licensing > License
                                                				  Management .

Step 2

From the Smart Software Licensing section, click the Actions drop-down list.

Step 3

Choose Renew
                                             				Authorization Now .

Step 4

Click Ok .

Unified Communications Manager sends a request to Cisco Smart Software Manager or Cisco Smart Software Manager satellite to check the "License Authorization Status" and Cisco Smart Software Manager or Cisco Smart Software Manager satellite reports back the status to Unified Communications Manager . For more information, see the online help.

Step 5

In the License
                                             				Usage Report section, click Update
                                             				Usage Details to manually update the system license usage
                                          			 information.

Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help.

### Renew
                           	 Registration

During product
                                 		  registration to Cisco Smart Software Manager or Cisco Smart Software Manager
                                 		  satellite, there is a security association used to identify the product and is
                                 		  anchored by the registration certificate, which has a lifetime of one year
                                 		  (that is, registration period). This is different from the registration token
                                 		  ID expiration, which has the time limit for the token to be active. This
                                 		  registration period is automatically renewed every 6 months. However, if there
                                 		  is an issue, you can manually renew this registration period.

#### Before you begin

The product should
                                 		  be registered with Cisco Smart Software Manager or Cisco Smart Software Manager
                                 		  satellite.

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Licensing > License
                                                				  Management .

Step 2

From the Smart Software Licensing section, click the Actions drop-down list.

Step 3

Choose Renew
                                             				Registration Now .

Step 4

Click Ok .

Unified Communications Manager sends a request to Cisco Smart Software Manager or Cisco Smart Software Manager satellite to check the "Registration Status" and Cisco Smart Software Manager or Cisco Smart Software Manager satellite reports back the status to Unified Communications Manager .

Step 5

In the License
                                             				Usage Report section, click Update
                                             				Usage Details to manually update the system license usage
                                          			 information.

Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help.

### Deregister

Use this procedure to unregister from Cisco Smart Software Manager or Cisco Smart Software Manager satellite and release all
                                 the licenses from the current virtual account. This procedure also disconnects Unified Communications Manager cluster from Cisco Smart Software Manager or Cisco Smart Software Manager satellite. All license entitlements used for the
                                 product are released back to the virtual account and is available for other product instances to use.

If Unified Communications Manager is unable to connect with the Cisco Smart Software Manager or Cisco Smart Software Manager satellite, and the product is
                                             still deregistered, then a warning message is displayed. This message notifies you to remove the product manually from Cisco
                                             Smart Software Manager or Cisco Smart Software Manager satellite to free up licenses.

#### Before you begin

The product should
                                 		  be registered with Cisco Smart Software Manager or Cisco Smart Software Manager
                                 		  satellite.

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Licensing > License
                                                				  Management .

Step 2

From the Smart Software Licensing section, click the Actions drop-down list.

Step 3

Choose Deregister .

Step 4

Click Ok .

Step 5

In the License
                                             				Usage Report section, click Update
                                             				Usage Details to manually update the system license usage
                                          			 information.

Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help.

If the data plane encryption (Unified Communications Manager cluster in mixed-mode) has been enabled after registered with
                                                               Cisco Smart Software Manager or Cisco Smart Software Manager satellite and the product is later deregistered, then mixed-mode
                                                               will continue to be enabled.

An alert named SmartLicenseExportControlNotAllowed is sent
                                                               						to the administrator to set cluster to non-secure mode when the product is
                                                               						deregistered from Cisco Smart Software Manager or Cisco Smart Software Manager
                                                               						satellite. The mixed-mode will continue to be enabled even after the reboot.

This behavior after deregistration, may change in future
                                                               						versions of the product. For more details on setting up CTL Client, see the "Set Up Cisco CTL Client" chapter of the Security Guide for Cisco Unified Communications
                                                                  						  Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-maintenance-guides-list.html .

For more details on Mixed Mode with Tokenless CTL, see the "CUCM Mixed Mode with Tokenless CTL" section at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-tech-notes-list.html .

### Reregister License
                           	 with Cisco Smart Software Manager

Use this procedure
                                 		  to Reregister Cisco
                                    			 Unified Communications Manager with Cisco Smart Software Manager or
                                 		  Cisco Smart Software Manager satellite.

#### Before you begin

Step 1

From Cisco
                                          			 Unified CM Administration, choose System > Licensing > License
                                                				  Management .

Step 2

From the Smart
                                             				Software Licensing section, click the Register button.

Step 3

From the Smart
                                             				Software Licensing section, click the Actions drop—down list.

Step 4

Choose Reregister .

Step 5

Click Ok .

Step 6

In the Product
                                             				Instance Registration Token section, paste the copied or saved "Registration
                                             				Token Key" that you generated using the Cisco Smart Software Manager or
                                          			 Cisco Smart Software Manager satellite.

Step 7

Click Register to complete the registration process.

Step 8

Click Close . For more information, see the online help.

Step 9

In the License
                                             				Usage Report section, click Update
                                             				Usage Details to manually update the system license usage
                                          			 information.

Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help.

## Specific License Reservation

Specific License Reservation is a feature that is used in highly secure networks. It provides a method for customers to deploy
                           a software license on a device (Product Instance - Unified Communications Manager) without communicating usage information.

The user can specify and reserve perpetual or term-based licenses against the Unified Communications Manager product. After
                           authorization code is exchanged, regular product synchronization is not required until there are changes in the reservation.
                           Reserved licenses remain blocked in Cisco Smart Software Manager unless released from the product with a return code.

An update or change in reserved licenses (increase or decrease) can be done on previously reserved licenses in Cisco Smart
                           Software Manager. The new authorization code can be installed on the Product and a confirmation code can be obtained. The
                           new changes remain in transit status unless confirmation code from the product is installed on the Cisco Smart Software Manager.

When licenses are reserved on a Product Instance (Unified Communications Manager), there are two ways to remove the product
                           from the smart account and release all the licenses that are reserved for that Product Instance (Unified Communications Manager):

Product Instance is operational (graceful removal): User can return the Specific License Reservation authorization by creating a Reservation Return code on the Product Instance
                           (which removes the Authorization Code) and then enter the Reservation Return code into Cisco Smart Software Manager.

Product Instance is not operational (failure/RMA or due to destroying the VM/container): User must contact TAC, who can remove the Product Instance from thier smart account.

Customer who is entitled to License reservation feature on their Smart Account can reserve licenses from their virtual account,
                           tie them to a devices UDI and use their device with these reserved licenses in a disconnected mode. The customer reserves
                           specific licenses and counts for a UDI from their virtual account. The following options describe the new functionality and
                           design elements for Specific License Reservation:

license smart reservation enable

license smart reservation disable

license smart reservation request

license smart reservation cancel

update license reservation

license smart reservation install "<authorization-code>"

license smart reservation install-file <url>

license smart reservation return

license smart reservation return-authorization "<authorization-code>"

### Specific License Reservation Task Flow

Complete these tasks to reserve specific licenses for Unified Communications Manager.

#### license smart reservation enable

Use this procedure to enable Specific License Reservation.

##### Before you begin

Unified Communications Manager is unregistered with Cisco Smart Software Manager or satellite.

From Cisco Unified CM Admin Console execute the below CLI command.

license smart reservation enable

#### license smart reservation request

Use this procedure to generate reservation request code generate request code from Unified Communications Manager product.

##### Before you begin

Make sure Unified Communications Manager Registration Status is Reservation in progress, by executing license smart reservation enable .

Step 1

From Cisco Unified CM Admin Console execute license smart reservation request command.

Step 2

Log into CSSM [Cisco Smart Software manager] and enter the reservation request code.

Step 3

Select the licenses that have to be reserved for this device and generate Authorization code.

Step 4

Copy the authorization code to the product instance and execute the license smart reservation install "<authorization-code> " command to install.

#### license smart reservation install "<authorization-code>"

Use this procedure to install license reservation authorization-code generated from Cisco Smart Software Manager.

##### Before you begin

Make Unified Communications Manager Registration Status is Reservation In Progress, by executing commands in below sequence:

license smart reservation enable

license smart reservation request

From Cisco Unified CM Admin Console execute the below CLI command.

license smart reservation install "<authorization-code>"

#### license smart reservation install-file <url>

Use this procedure to install the license reservation authorization-code file generated on the Cisco Smart Software Manager.

##### Before you begin

Make sure Unified Communications Manager registration status is Reservation In Progress, by executing commands in below sequence.:

license smart reservation enable

license smart reservation request

url is mandatory Path to the authorization-code file on SFTP server in below format:

sftp://<HostName/IP>:<port>/<Path to Authorization-Code file>

From Cisco Unified CM Admin Console execute the below CLI command.

license smart reservation install-file <url>

### Additional Tasks with Specific License Reservation

The following additional tasks are available on Unified Communications Manager for Specific License Reservation:

#### license smart reservation disable

Use this procedure to disable specific license reservation.

##### Before you begin

Specific License Reservation is enabled on  Unified Communications Manager

From Cisco Unified CM Admin Console execute the below CLI command.

license smart reservation disable

#### update license reservation

Use this procedure to update the license reservation for your product instance and get a new authorization code.

##### Before you begin

Make sure Unified Communications Manager Registration Status is Registered- Specific License Reservation by executing commands
                                    in below sequence:

license smart reservation enable

license smart reservation request

license smart reservation install "<authorization-code>"

License borrowing from a higher tier does not happen automatically when a Specific License Reservation is enabled on Unified
                                                Communications Manager. License Reservation has to be updated manually to the Unified Communications Manager license consumption/usage.

Step 1

Select Update Reserved Licenses from Actions drop-down list next to the Product Instance that you wish to update reservation
                                             on CSSM.

Step 2

Update the reservation (Add/Remove/Update licenses for this product instance) and generate authorization code.

Step 3

Copy the authorization code to the product instance and execute the license smart reservation install “<authorization-code>” command to install.

Step 4

Confirmation code is generated on the product after the authorization code is successfully installed.

Step 5

Copy the confirmation code to the CSSM and enter to complete the reservation update.

#### license smart reservation cancel

Use this procedure to cancel the reservation process before the authorization code from Cisco Smart Software Manager against
                                    CUCM request code is installed.

##### Before you begin

Make sure Unified Communications Manager Registration Status is Reservation In Progress, by executing commands in below sequence:

license smart reservation enable

license smart reservation request

From Cisco Unified CM Admin Console execute the below CLI command.

license smart reservation cancel

#### license smart reservation return

Use this procedure to generate a return code that must be entered into the Cisco Smart Software Manager to return the licenses
                                    to the virtual account pool and remove the product instance from CSSM.

##### Before you begin

Make sure Unified Communcations Manger Registration Status is Registered- Specific License Reservation by executing commands
                                    in below sequence:

license smart reservation enable

license smart reservation request

license smart reservation install "<authorization-code>"

Step 1

From Cisco Unified CM Admin Console execute the license smart reservation return command.

Step 2

Copy the reservation return code to CSSM and remove the product instance.

#### license smart reservation return-authorization "<authorization-code>"

Use this procedure to generate a return code for the authorization code not installed yet. The return code must be entered
                                    into the Cisco Smart Software Manager to return the licenses to the virtual account pool and remove the product instance from
                                    CSSM.

##### Before you begin

Make sure Unified Communcations Manager Registration Status is Reservation In Progress, by executing commands in below sequence:

license smart reservation enable

license smart reservation request

Step 1

From Cisco Unified CM Admin Console execute the license smart reservation return-authorization "<authorization-code>" command.

Step 2

Copy the reservation return code to CSSM and remove the product instance.

## Version Independent Licensing

Important

This section is applicable from Release 14 onwards.

Unified Communications Manager supports Version Independent User Licenses. The Licenses are annuity-style and issued for the
                           subscription term. You can order these V14 licenses through Flex EA (Enterprise Agreement) or Flex NU (Named User—Professional,
                           Enhanced, Access). For more information, see the Ordering Guide .

Unified Communications Manager continues to use the version 12.X License.

The licenses are managed on CSSM (Cisco Smart Software Manager). For more information, see Smart Software Licensing .

## Smart Licensing Export Compliance

Smart Licensing provides a method that allows user to use export control features. In the connected state, use export control
                           feature using the registration process. In the disconnected state, use export control feature using Smart License Reservation.

This export control feature is a solution for customers with a smart account, for whom Export Restrictions apply. This feature
                           allows the user to request a regulatory Export License that is granted in the Cisco Smart Software Manager or the satellite
                           and enable the export restricted feature on Cisco Unified Communications Manager.

The following options describe the new functionality and design elements for the export control feature:

license smart export request local <exportfeaturename>

license smart export return local <exportfeaturename>

license smart export cancel

### Export Control Task Flow

Complete the following tasks to export control licenses for Cisco Unified Communications Manager.

### license smart export request local <exportfeaturename>

This command allows user with Smart Account for whom Export Restrictions apply, to request a regulatory export license from
                                 Cisco Smart Software Manager or satellite.

The command returns an export authorization key if regulatory export license is available on Cisco Smart Software Manager
                                 or satellite and enable export restricted feature on the product.

#### Before you begin

Cisco Unified Communications Manager is registered with Cisco Smart Software Manager or satellite. Make sure <CUCM Export
                                 Restricted Authorization Key> license is available on Cisco Smart Software Manager.

From Cisco Unified CM Admin Console, execute the following CLI command:

license smart export request local <exportfeaturename>

### license smart export return local <exportfeaturename>

The command allows to return a previously requested export restricted license to Cisco Smart Software Manager or satellite.
                                 The export authorization key for the export restricted feature is removed from the system.

#### Before you begin

Export authorization key is generated for the feature.

From Cisco Unified CM Admin Console, execute the following CLI command:

license smart export return local <exportfeaturename>

### license smart export cancel

This command allows user with Smart Account for whom Export Restrictions apply, to cancel the automatic retry of previously
                                 failed export request or return from Cisco Smart Software Manager or satellite.

#### Before you begin

Cisco Unified Communications Manager is registered with Cisco Smart Software Manager or satellite.

From Cisco Unified CM Admin Console, execute the following CLI command:

license smart export cancel

| Note | The License authorization is valid for 90 days with a renewal at least once in 30 days. The authorization will expire after
                                       90 days if it is not connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite. If the Cisco Smart Software Manager satellite option is selected, the satellite must have an internet connection to Cisco
                                       Smart Software Manager for the authorization to occur. The Cisco Smart Software Manager satellite can operate in 2 modes:
                                       Connected Mode in which the connection time is configurable, and Disconnected mode which requires a manual sync. |
|---|---|

| Note | The Unified CM running in Dual Stack mode supports satellite configured with IPv4 and IPv6 address. |
|---|---|

| Note | The SME registered in Specific License Reservation (SLR) requires a minimum set of licenses reserved in CSSM while generating
                                                   an SLR authorization code. |
|---|---|

| Note | Evaluation period is before the product is registered. |
|---|---|

| Note | You cannot deploy a secure SIP trunk while running with a 90-day evaluation period. To deploy a secure SIP trunk, your system
                                          must have registered to a Smart Software Manager account with the Allow export-controlled functionality product registration token selected. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Obtain the Product Instance Registration Token . | Use this
                                          				procedure to generate a product instance registration token for your virtual
                                          				account. |
| Step 2 | Configure Connection to Smart Software Licensing (Applicable Until Release 14SU4 and 15SU2) | Select transport settings through which Unified Communications Manager connects to the Smart Software Licensing service. The Direct option is selected by default where the product communicates directly with Cisco licensing servers. |
| Step 3 | Register with Cisco Smart Software Manager . | Perform this step to register Unified Communications Manager with Cisco Smart Software Manager or Cisco Smart Software Manager satellite. |

| Step 1 | Log in to
                                          			 your smart account in either Cisco Smart Software Manager or your Cisco Smart
                                          			 Software Manager satellite. |
|---|---|
| Step 2 | Navigate to the virtual account with which you want to associate the Unified Communications Manager cluster. |
| Step 3 | Generate a "Product
                                             				Instance Registration Token" . Note Select the Allow export-controlled functionality on the products
                                                            					 registered with this token check box to turn on the
                                                         				  Export-Controlled functionality for tokens of a product instance you wish in
                                                         				  this smart account. By checking this check box and accepting the terms, you
                                                         				  enable higher levels of the product encryption for products registered with
                                                         				  this Registration Token. By default, this check box is selected. You can
                                                         				  uncheck this check box if you wish not to allow the Export-Controlled
                                                         				  functionality to be made available for use with this token. Caution Use this option only if you are compliant with the
                                                         				  Export-Controlled functionality. Note The Allow export-controlled functionality on the products
                                                            					 registered with this token check box is not displayed for the Smart
                                                         				  Accounts that are not permitted to use the Export-Controlled functionality. | Note | Select the Allow export-controlled functionality on the products
                                                            					 registered with this token check box to turn on the
                                                         				  Export-Controlled functionality for tokens of a product instance you wish in
                                                         				  this smart account. By checking this check box and accepting the terms, you
                                                         				  enable higher levels of the product encryption for products registered with
                                                         				  this Registration Token. By default, this check box is selected. You can
                                                         				  uncheck this check box if you wish not to allow the Export-Controlled
                                                         				  functionality to be made available for use with this token. | Caution | Use this option only if you are compliant with the
                                                         				  Export-Controlled functionality. | Note | The Allow export-controlled functionality on the products
                                                            					 registered with this token check box is not displayed for the Smart
                                                         				  Accounts that are not permitted to use the Export-Controlled functionality. |
| Note | Select the Allow export-controlled functionality on the products
                                                            					 registered with this token check box to turn on the
                                                         				  Export-Controlled functionality for tokens of a product instance you wish in
                                                         				  this smart account. By checking this check box and accepting the terms, you
                                                         				  enable higher levels of the product encryption for products registered with
                                                         				  this Registration Token. By default, this check box is selected. You can
                                                         				  uncheck this check box if you wish not to allow the Export-Controlled
                                                         				  functionality to be made available for use with this token. |
| Caution | Use this option only if you are compliant with the
                                                         				  Export-Controlled functionality. |
| Note | The Allow export-controlled functionality on the products
                                                            					 registered with this token check box is not displayed for the Smart
                                                         				  Accounts that are not permitted to use the Export-Controlled functionality. |
| Step 4 | Copy the token
                                          			 or save it to another location. For more
                                             				information, see https://software.cisco.com/ . |

| Note | Select the Allow export-controlled functionality on the products
                                                            					 registered with this token check box to turn on the
                                                         				  Export-Controlled functionality for tokens of a product instance you wish in
                                                         				  this smart account. By checking this check box and accepting the terms, you
                                                         				  enable higher levels of the product encryption for products registered with
                                                         				  this Registration Token. By default, this check box is selected. You can
                                                         				  uncheck this check box if you wish not to allow the Export-Controlled
                                                         				  functionality to be made available for use with this token. |
|---|---|

| Caution | Use this option only if you are compliant with the
                                                         				  Export-Controlled functionality. |
|---|---|

| Note | The Allow export-controlled functionality on the products
                                                            					 registered with this token check box is not displayed for the Smart
                                                         				  Accounts that are not permitted to use the Export-Controlled functionality. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Licensing > License
                                                				  Management . The License Management window appears. |
|---|---|
| Step 2 | From the Smart Software Licensing section, click the View/Edit the Licensing Smart Call Home settings link. The Transport Settings dialog box appears. |
| Step 3 | Select the method of connecting Unified Communications Manager to the Smart Licensing service: Direct —Unified Communications Manager connects directly to the Smart Software Manager on cisco.com. This is the default option.
                                                With this option, you must deploy DNS on Unified Communications Manager that can resolve tools.cisco.com . Transport Gateway —Unified Communications Manager connects to an on-premise Cisco Smart Software Manager satellite or Transport Gateway for
                                                system licensing. In the URL text box, enter the address and port of the Smart Software Manager satellite or Transport Gateway.
                                                For example, fqdn_of_smart_software_manager:port_number . For HTTPS, use port 443. HTTP/HTTPS Proxy —Unified Communications Manager connects to a proxy server, which connects to the Cisco Smart Software Manager service along
                                                with Transport Gateway also along with satellite on cisco.com. Enter the IP address or hostname of the proxy server along
                                                with the port: IP Address/Host Name Port—For HTTPS, use port 443. |
| Step 4 | Check the Do not share my hostname or IP address with Cisco check box to restrict Unified Communications Manager from sharing its IP address and hostname during the Smart Licensing
                                          registration. |
| Step 5 | Click Save . |

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Licensing > License
                                                				  Management . The License
                                             				Management window appears. |
|---|---|
| Step 2 | From the Smart
                                             				Software Licensing section, click the Register button. The Registration window appears. |
| Step 3 | In the Product
                                             				Instance Registration Token section, paste the copied or saved "Registration
                                             				Token Key" that you generated using the Smart Software Manager or Smart
                                          			 Software Manager satellite. |
| Step 4 | Click Register to complete the registration process. |
| Step 5 | Click Close . For more information, see the online help. |
| Step 6 | In the License
                                             				Usage Report section, click Update
                                             				Usage Details to manually update the system license usage
                                          			 information. Note Usage information is updated once every 24 hours automatically. For more information, see the online help. | Note | Usage information is updated once every 24 hours automatically. For more information, see the online help. |
| Note | Usage information is updated once every 24 hours automatically. For more information, see the online help. |

| Note | Usage information is updated once every 24 hours automatically. For more information, see the online help. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Renew Authorization | Complete this task to manually renew the License Authorization Status for all the license listed under the License Type. Note The license authorization is renewed automatically every 30 days. The authorization status will expire after 90 days if it
                                                      is not connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite. If the Cisco Smart Software Manager satellite option is selected, the satellite must have an internet connection to Cisco
                                                      Smart Software Manager for the authorization to occur. The Cisco Smart Software Manager satellite can operate in 2 modes:
                                                      Connected Mode in which the connection time is configurable, and Disconnected mode which requires a manual sync. | Note | The license authorization is renewed automatically every 30 days. The authorization status will expire after 90 days if it
                                                      is not connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite. If the Cisco Smart Software Manager satellite option is selected, the satellite must have an internet connection to Cisco
                                                      Smart Software Manager for the authorization to occur. The Cisco Smart Software Manager satellite can operate in 2 modes:
                                                      Connected Mode in which the connection time is configurable, and Disconnected mode which requires a manual sync. |
| Note | The license authorization is renewed automatically every 30 days. The authorization status will expire after 90 days if it
                                                      is not connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite. If the Cisco Smart Software Manager satellite option is selected, the satellite must have an internet connection to Cisco
                                                      Smart Software Manager for the authorization to occur. The Cisco Smart Software Manager satellite can operate in 2 modes:
                                                      Connected Mode in which the connection time is configurable, and Disconnected mode which requires a manual sync. |
| Step 2 | Renew Registration | Complete this task to renew the registration information manually. Note The initial registration is valid for one year. Renewal of registration is automatically done every six months provided the
                                                      product is connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite. | Note | The initial registration is valid for one year. Renewal of registration is automatically done every six months provided the
                                                      product is connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite. |
| Note | The initial registration is valid for one year. Renewal of registration is automatically done every six months provided the
                                                      product is connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite. |
| Step 3 | Deregister | Complete this task to disconnect the Unified Communications Manager cluster from Cisco Smart Software Manager or Cisco Smart
                                          Software Manager satellite. The product reverts to evaluation mode as long as the evaluation period is not expired. All license
                                          entitlements used for the product are immediately released back to the virtual account and are available for other product
                                          instances to use it. |
| Step 4 | Reregister License with Cisco Smart Software Manager | Complete this task to reregister Unified Communications Manager with Cisco Smart Software Manager or Cisco Smart Software
                                          Manager satellite. Note Product may migrate to a different virtual account by reregistering with token from a new virtual account. | Note | Product may migrate to a different virtual account by reregistering with token from a new virtual account. |
| Note | Product may migrate to a different virtual account by reregistering with token from a new virtual account. |

| Note | The license authorization is renewed automatically every 30 days. The authorization status will expire after 90 days if it
                                                      is not connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite. If the Cisco Smart Software Manager satellite option is selected, the satellite must have an internet connection to Cisco
                                                      Smart Software Manager for the authorization to occur. The Cisco Smart Software Manager satellite can operate in 2 modes:
                                                      Connected Mode in which the connection time is configurable, and Disconnected mode which requires a manual sync. |
|---|---|

| Note | The initial registration is valid for one year. Renewal of registration is automatically done every six months provided the
                                                      product is connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite. |
|---|---|

| Note | Product may migrate to a different virtual account by reregistering with token from a new virtual account. |
|---|---|

| Note | The license authorization is renewed automatically every 30 days. The authorization status will expire after 90 days if it
                                             is not connected to Cisco Smart Software Manager or Cisco Smart Software Manager satellite. If the Cisco Smart Software Manager satellite option is selected, the satellite must have an internet connection to Cisco
                                             Smart Software Manager for the authorization to occur. The Cisco Smart Software Manager satellite can operate in 2 modes:
                                             Connected Mode in which the connection time is configurable, and Disconnected mode  which requires a manual sync. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Licensing > License
                                                				  Management . The License
                                             				Management window appears. |
|---|---|
| Step 2 | From the Smart Software Licensing section, click the Actions drop-down list. |
| Step 3 | Choose Renew
                                             				Authorization Now . The Renew Authorization window appears. |
| Step 4 | Click Ok . Unified Communications Manager sends a request to Cisco Smart Software Manager or Cisco Smart Software Manager satellite to check the "License Authorization Status" and Cisco Smart Software Manager or Cisco Smart Software Manager satellite reports back the status to Unified Communications Manager . For more information, see the online help. |
| Step 5 | In the License
                                             				Usage Report section, click Update
                                             				Usage Details to manually update the system license usage
                                          			 information. Note Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. | Note | Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. |
| Note | Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. |

| Note | Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Licensing > License
                                                				  Management . The License
                                             				Management window appears. |
|---|---|
| Step 2 | From the Smart Software Licensing section, click the Actions drop-down list. |
| Step 3 | Choose Renew
                                             				Registration Now . The Renew Registration window appears. |
| Step 4 | Click Ok . Unified Communications Manager sends a request to Cisco Smart Software Manager or Cisco Smart Software Manager satellite to check the "Registration Status" and Cisco Smart Software Manager or Cisco Smart Software Manager satellite reports back the status to Unified Communications Manager . |
| Step 5 | In the License
                                             				Usage Report section, click Update
                                             				Usage Details to manually update the system license usage
                                          			 information. Note Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. | Note | Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. |
| Note | Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. |

| Note | Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. |
|---|---|

| Note | If Unified Communications Manager is unable to connect with the Cisco Smart Software Manager or Cisco Smart Software Manager satellite, and the product is
                                             still deregistered, then a warning message is displayed. This message notifies you to remove the product manually from Cisco
                                             Smart Software Manager or Cisco Smart Software Manager satellite to free up licenses. |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Licensing > License
                                                				  Management . The License
                                             				Management window appears. |
|---|---|
| Step 2 | From the Smart Software Licensing section, click the Actions drop-down list. |
| Step 3 | Choose Deregister . The Deregister window appears. |
| Step 4 | Click Ok . |
| Step 5 | In the License
                                             				Usage Report section, click Update
                                             				Usage Details to manually update the system license usage
                                          			 information. Note Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. Note If the data plane encryption (Unified Communications Manager cluster in mixed-mode) has been enabled after registered with
                                                               Cisco Smart Software Manager or Cisco Smart Software Manager satellite and the product is later deregistered, then mixed-mode
                                                               will continue to be enabled. An alert named SmartLicenseExportControlNotAllowed is sent
                                                               						to the administrator to set cluster to non-secure mode when the product is
                                                               						deregistered from Cisco Smart Software Manager or Cisco Smart Software Manager
                                                               						satellite. The mixed-mode will continue to be enabled even after the reboot. This behavior after deregistration, may change in future
                                                               						versions of the product. For more details on setting up CTL Client, see the "Set Up Cisco CTL Client" chapter of the Security Guide for Cisco Unified Communications
                                                                  						  Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-maintenance-guides-list.html . For more details on Mixed Mode with Tokenless CTL, see the "CUCM Mixed Mode with Tokenless CTL" section at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-tech-notes-list.html . | Note | Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. | Note | If the data plane encryption (Unified Communications Manager cluster in mixed-mode) has been enabled after registered with
                                                               Cisco Smart Software Manager or Cisco Smart Software Manager satellite and the product is later deregistered, then mixed-mode
                                                               will continue to be enabled. An alert named SmartLicenseExportControlNotAllowed is sent
                                                               						to the administrator to set cluster to non-secure mode when the product is
                                                               						deregistered from Cisco Smart Software Manager or Cisco Smart Software Manager
                                                               						satellite. The mixed-mode will continue to be enabled even after the reboot. This behavior after deregistration, may change in future
                                                               						versions of the product. For more details on setting up CTL Client, see the "Set Up Cisco CTL Client" chapter of the Security Guide for Cisco Unified Communications
                                                                  						  Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-maintenance-guides-list.html . For more details on Mixed Mode with Tokenless CTL, see the "CUCM Mixed Mode with Tokenless CTL" section at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-tech-notes-list.html . |
| Note | Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. |
| Note | If the data plane encryption (Unified Communications Manager cluster in mixed-mode) has been enabled after registered with
                                                               Cisco Smart Software Manager or Cisco Smart Software Manager satellite and the product is later deregistered, then mixed-mode
                                                               will continue to be enabled. An alert named SmartLicenseExportControlNotAllowed is sent
                                                               						to the administrator to set cluster to non-secure mode when the product is
                                                               						deregistered from Cisco Smart Software Manager or Cisco Smart Software Manager
                                                               						satellite. The mixed-mode will continue to be enabled even after the reboot. This behavior after deregistration, may change in future
                                                               						versions of the product. For more details on setting up CTL Client, see the "Set Up Cisco CTL Client" chapter of the Security Guide for Cisco Unified Communications
                                                                  						  Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-maintenance-guides-list.html . For more details on Mixed Mode with Tokenless CTL, see the "CUCM Mixed Mode with Tokenless CTL" section at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-tech-notes-list.html . |

| Note | Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. |
|---|---|

| Note | If the data plane encryption (Unified Communications Manager cluster in mixed-mode) has been enabled after registered with
                                                               Cisco Smart Software Manager or Cisco Smart Software Manager satellite and the product is later deregistered, then mixed-mode
                                                               will continue to be enabled. An alert named SmartLicenseExportControlNotAllowed is sent
                                                               						to the administrator to set cluster to non-secure mode when the product is
                                                               						deregistered from Cisco Smart Software Manager or Cisco Smart Software Manager
                                                               						satellite. The mixed-mode will continue to be enabled even after the reboot. This behavior after deregistration, may change in future
                                                               						versions of the product. For more details on setting up CTL Client, see the "Set Up Cisco CTL Client" chapter of the Security Guide for Cisco Unified Communications
                                                                  						  Manager at http://www.cisco.com/c/en/us/support/unified-communications/unified-presence/products-maintenance-guides-list.html . For more details on Mixed Mode with Tokenless CTL, see the "CUCM Mixed Mode with Tokenless CTL" section at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-tech-notes-list.html . |
|---|---|

| Step 1 | From Cisco
                                          			 Unified CM Administration, choose System > Licensing > License
                                                				  Management . The License
                                             				Management window appears. |
|---|---|
| Step 2 | From the Smart
                                             				Software Licensing section, click the Register button. The Registration window appears. |
| Step 3 | From the Smart
                                             				Software Licensing section, click the Actions drop—down list. |
| Step 4 | Choose Reregister . The Reregister window appears. |
| Step 5 | Click Ok . |
| Step 6 | In the Product
                                             				Instance Registration Token section, paste the copied or saved "Registration
                                             				Token Key" that you generated using the Cisco Smart Software Manager or
                                          			 Cisco Smart Software Manager satellite. |
| Step 7 | Click Register to complete the registration process. |
| Step 8 | Click Close . For more information, see the online help. |
| Step 9 | In the License
                                             				Usage Report section, click Update
                                             				Usage Details to manually update the system license usage
                                          			 information. Note Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. | Note | Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. |
| Note | Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. |

| Note | Usage information is updated once every 24 hours automatically. For more information on the fields and their configuration
                                                         options, see the system Online Help. |
|---|---|

| Note | User can use only the CLI configuration to enable Specific License Reservation. |
|---|---|

| Note | When Specific License Reservation is enabled on Unified Communications Manager, voucher generation for cloud on-boarding will
                                    is not supported. |
|---|---|

| From Cisco Unified CM Admin Console execute the below CLI command. license smart reservation enable |
|---|

| Step 1 | From Cisco Unified CM Admin Console execute license smart reservation request command. |
|---|---|
| Step 2 | Log into CSSM [Cisco Smart Software manager] and enter the reservation request code. |
| Step 3 | Select the licenses that have to be reserved for this device and generate Authorization code. |
| Step 4 | Copy the authorization code to the product instance and execute the license smart reservation install "<authorization-code> " command to install. |

| From Cisco Unified CM Admin Console execute the below CLI command. license smart reservation install "<authorization-code>" |
|---|

| Note | url is mandatory Path to the authorization-code file on SFTP server in below format: |
|---|---|

| From Cisco Unified CM Admin Console execute the below CLI command. license smart reservation install-file <url> |
|---|

| From Cisco Unified CM Admin Console execute the below CLI command. license smart reservation disable |
|---|

| Note | License borrowing from a higher tier does not happen automatically when a Specific License Reservation is enabled on Unified
                                                Communications Manager. License Reservation has to be updated manually to the Unified Communications Manager license consumption/usage. |
|---|---|

| Step 1 | Select Update Reserved Licenses from Actions drop-down list next to the Product Instance that you wish to update reservation
                                             on CSSM. |
|---|---|
| Step 2 | Update the reservation (Add/Remove/Update licenses for this product instance) and generate authorization code. |
| Step 3 | Copy the authorization code to the product instance and execute the license smart reservation install “<authorization-code>” command to install. |
| Step 4 | Confirmation code is generated on the product after the authorization code is successfully installed. |
| Step 5 | Copy the confirmation code to the CSSM and enter to complete the reservation update. |

| From Cisco Unified CM Admin Console execute the below CLI command. license smart reservation cancel |
|---|

| Step 1 | From Cisco Unified CM Admin Console execute the license smart reservation return command. |
|---|---|
| Step 2 | Copy the reservation return code to CSSM and remove the product instance. |

| Step 1 | From Cisco Unified CM Admin Console execute the license smart reservation return-authorization "<authorization-code>" command. |
|---|---|
| Step 2 | Copy the reservation return code to CSSM and remove the product instance. |

| Important | This section is applicable from Release 14 onwards. |
|---|---|

| From Cisco Unified CM Admin Console, execute the following CLI command: license smart export request local <exportfeaturename> |
|---|

| From Cisco Unified CM Admin Console, execute the following CLI command: license smart export return local <exportfeaturename> |
|---|

| From Cisco Unified CM Admin Console, execute the following CLI command: license smart export cancel |
|---|