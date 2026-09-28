---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-14-install-upgrade-guide-b-14cuciumg-b-14cuciumg-chapter-0101-htm-30b395fec6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/install_upgrade/guide/b_14cuciumg/b_14cuciumg_chapter_0101.html
retrieved_at: 2026-08-17T02:13:18.396405+00:00
---

Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 14

# Install, Upgrade and Maintenance Guide for Cisco Unity Connection Release 14

Updated: December 2, 2025

Chapter: Managing
	 Licenses

## Chapter: Managing
	 Licenses

# Managing
                     	 Licenses

## Managing
                        	 Licenses

### Overview

Unity Connection supports Cisco Smart Software Licensing which is simple and enhanced way for using various licensed features.Using Cisco Smart Software Licensing, you can manage
                              all the licenses associated with an organization through Cisco Smart Software Manager (CSSM) or Cisco Smart Software Manager satellite . Cisco Smart Software Licensing establishes a pool of licenses or entitlements that can be used across your organization
                              in a flexible and automated manner. This model of licensing provides the visibility of your licenses ownership and consumption.
                              Unity Connection must be registered with the CSSM to use various licensed feature.

Cisco Smart Software
                                 		  Manager enables you to manage all of your Cisco Smart Software Licenses
                              		from one centralized website. You can use Cisco Smart Software Manager to:

- Manage and track licenses

- Move licenses across
                                    		  virtual account

- Remove registered product
                                    		  instance

For more
                              		information about Cisco Smart Software Manager, see https:/​/​software.cisco.com/

Cisco Smart Software
                                 		  Manager satellite is a component of Cisco Smart Software Licensing that
                              		manages product registrations and monitoring of smart license usage for Cisco
                              		products. If you do not want to manage Cisco products directly using Cisco
                              		Smart Software Manager, either for policy or network availability reasons, you
                              		can choose to install the Cisco Smart Software Manager satellite on-premises.
                              		Products register and report license consumption to the Cisco Smart Software
                              		Manager satellite as it does on Cisco Smart Software Manager.

For more information
                              		about the Cisco Smart Software Manager satellite, see http:/​/​www.cisco.com/​web/​ordering/​smart-software-manager/​smart-software-manager-satellite.html .

For more information
                              		on Cisco Smart Software Licensing, see the "Smart Software Licensing Overview"
                              		available at, http://www.cisco.com/web/ordering/smart-software-licensing/index.html

#### Deployment
                              	 Options

To view and manage
                                 		the licenses, Unity Connection must communicate with the Cisco Smart Software
                                 		Manager (CSSM) or Cisco Smart Software Manager satellite.

Following are the
                                 		options to deploy the Cisco Smart Software Licensing in Unity Connection,
                                 		listed in an order from easiest to use to most secure:

Direct Cloud Access : In
                                          			 this option, Unity Connection can directly communicate with CSSM and transfer
                                          			 the usage information over internet. No additional components are required.

- Direct Cloud Access through an HTTPs Proxy : In this option, Unity Connection directly transfers the usage information to CSSM over internet through proxy server.Administrator
                                       also provides an option to authenticate the proxy server for secure communication with CSSM. You can enter username and password
                                       for authentication of proxy server.

Mediated Access through an
                                             				On-Premises Collector – Connected : In this option, Unity Connection
                                          			 communicates with on-prem version of CSSM called Cisco Smart Software Manager
                                          			 satellite. Periodically satellite communicates with CSSM using Cisco network
                                          			 and exchange of license information will be performed to keep the databases in
                                          			 synch.

Mediated Access through an
                                             				On-Premises Collector – Disconnected : This option also uses the satellite
                                          			 that is not connected with Cisco network. For synchronization between satellite
                                          			 and CSSM, you will manually exchange the license information files to keep the
                                          			 database in synch.

To select the
                                 		deployment options, see " Configuring
                                    		  Transport Setting " section.

#### Smart Account and
                              	 Virtual Account

Smart Account is a
                                 		simple and organized way to manage the product licenses and entitlements. Using
                                 		this account, you can register, view, and manage your Cisco Software Licenses
                                 		across your organization.

As per the
                                 		organization requirements, you can create the sub accounts within your Smart
                                 		Account. The sub accounts are known as Virtual Accounts that are collections of
                                 		licenses and product instances. To manage the licenses, you can create multiple
                                 		virtual accounts based on the different organization categories such as
                                 		departments or locations. Virtual Accounts are maintained by Smart Account
                                 		administrators. Licenses can be transferred within virtual accounts as per the
                                 		requirement.

While moving product instance from one virtual account to another, the licenses assosiated with the previous virtual account
                                 are not transferred.

For more information
                                 		on how to create and manage the Smart Account and Virtual Account, see "Cisco
                                 		Smart Accounts" at http://www.cisco.com/web/ordering/smart-software-manager/smart-accounts.html

### Prerequisites for
                           	 Configuring Cisco Smart Software Licensing

To configure the
                              		Cisco Smart Software Licensing in Unity Connection, ensure the following
                              		requirements:

Understand the
                                       			 Unified Communications (UC) licensing structure. For details, see http:/​/​www.cisco.com/​c/​en/​us/​products/​unified-communications/​unified-communications-licensing/​index.html .

- A Smart Account and Virtual
                                    		  Account must be created for Unity Connection. For more information, see " Smart
                                       			 Account and Virtual Account " section.

### Configuring Cisco
                           	 Smart Software Licensing in Unity Connection

By default, the
                              		Cisco Smart Software Licensing is enabled for Cisco Unity Connection. To use
                              		Cisco Smart Software Licensing, Unity Connection must register with CSSM or
                              		satellite. After fresh install, Unity Connection remains in Evaluation Mode
                              		until it is registered with CSSM or satellite. The Evaluation Period of 90 days
                              		are provided once in the entire life cycle of the product. As soon as Unity
                              		Connection consumes licenses, the Evaluation Period starts.

In Evaluation Mode,
                              		you cannot enable the encryption on Unity Connection. It means you are not
                              		allowed to use the security modules in Unity Connection. To enable the
                              		encryption in Unity Connection, you must register the product with CSSM or
                              		satellite using token that allows Export-Controlled Functionality. To enable
                              		the Export Controlled Functionality for the product, see " Token
                                 		  Creation " section.

After successfully
                              		registering the product with CSSM or satellite, run "utils cuc encryption
                              		enable" CLI command to enable the encryption on Unity Connection.

For more information
                              		on the CLI command, see the Command Line Interface Reference Guide for Cisco
                              		Unified Solutions for the latest release, available at http://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

For more information on the encryption in Cisco Unity Connection, see " Cisco Unity Connection- Restricted and Unrestricted Version " chapter of the Security Guide for Cisco Unity Connection Release 14 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/14/security/guide/b_14cucsecx.html .

#### Configuring
                              	 Transport Settings (optional)

To deploy the
                                    		  Cisco Smart Licensing in Unity Connection, you can configure the applicable
                                    		  transport settings. To configure the transport settings in Unity Connection, do
                                    		  the following procedure:

Step 1

In Cisco Unity
                                             			 Connection Administration, expand System Settings and select Licenses.

Step 2

On the
                                             			 Licenses page, select View/Edit link under Transport Settings field. A dialog box appears, on which select the
                                             			 applicable deployment option for the Smart Licensing. ( For more information,
                                             			 see Help > This Page)

Step 3

Select Save.

#### Token
                              	 Creation

You must create a
                                    		  token to register the product with CSSM or satellite.

To create the
                                    		  token, do the following procedure:

Step 1

Log in to
                                             			 your Smart Account in Cisco Smart Software Manager at software.cisco.com or
                                             			 Cisco Smart Software Manager satellite.

Step 2

Select the
                                             			 virtual account that contains the licenses for the product.

Step 3

In the
                                             			 General tab of virtual account, select New Token.

Step 4

In the Create
                                             			 Registration Token dialog box, enter the Description and Expire After
                                             			 information and select Create Token.

Step 5

To allow the
                                             			 Export Controlled Functionality for Unity Connection, check the Allow
                                                				export-controlled functionality on the products registered with this token check box. By checking the check box, you can enable the encryption for the
                                             			 product registered with this Registration Token.

Step 6

Once the token
                                             			 is created, copy the token to register the product.

#### Registering the
                              	 Unity Connection

To register the
                                    		  Unity Connection with CSSM or satellite, do the following procedure:

Step 1

Log in to the
                                             			 Cisco Unity Connection Administration.

Step 2

Expand System
                                             			 Settings and select Licenses.

Step 3

On the
                                             			 Licenses page, select Register button. A dialog box appears, enter the registration token copied from the CSSM
                                             			 or satellite.

Step 4

Select Register .

### Managing Cisco
                           	 Smart Software Licensing

After successful
                              		registration of the Unity connection with CSSM or satellite , you can see the
                              		usage details on the Licenses page of the Cisco Unity Connection
                              		Administration. You can also manage the licenses by performing the various
                              		actions on Cisco Unity Connection Administration.

To perform the
                              		actions, go to Cisco Unity Connection Administration > System Settings >
                              		Licenses. On the Licenses page, select any one of the following from the Action
                              		menu:

- Renew Authorization Now : Using this option, you can manually renew the license authorization for all the licenses. However, the licenses are automatically
                                 authorized in every 6 hours.

- Renew Registration Now :
                                 		  After registering with CSSM or satellite, it provides a registration
                                 		  certificate to identify the product. This certificate is valid for one year.
                                 		  Using this option, you can manually renew the registration of the product.
                                 		  However, the registration of the product is automatically renewed in every six
                                 		  month.

- Deregister : Using this
                                 		  option, you can deregister the product from CSSM or satellite. All license
                                 		  entitlements used for the product are released back to its virtual account.

Reregister : Using this
                                    			 option, you can reregister the product with CSSM or satellite.

### Smart Software
                           	 Licensing Status

Whenever Unity
                              		Connection communicates with the Cisco Smart Software Manager, there is a
                              		transition in the Unity Connection licensing status. The Smart Software
                              		Licensing Status provides an overview of license usage on the product.

The licensing status
                              		of the Unity Connection can be categorized as follows:

- Registration Status

- Authorization Status

#### Registration
                              	 Status

The different
                                 		registration status in a Unity Connection server are:

Unregistered : The
                                          			 registration status of Unity Connection remains Unregistered until it
                                          			 successfully registers with CSSM or satellite.

Registered : Unity
                                          			 Connection is successfully registered with CSSM or satellite.

- Registration Expired :
                                       		  The registration status of Unity Connection changes to the Registration Expired
                                       		  if registration of the product is not renewed within one year. After
                                       		  registration expired, the product goes back to the Evaluation Mode and you can
                                       		  use licenses for the remaining days of the Evaluation Period. When Evaluation
                                       		  Period of the product is expired and the product is still not registered with
                                       		  CSSM or satellite, you can not create or modify the users in Unity Connection.

#### Authorization
                              	 Status

The different
                                 		authorization status in a Unity Connection server are:

- Evaluation Mode : The
                                       		  authorization status of fresh installed Unity Connection is Evaluation Mode
                                       		  until it registers with CSSM or satellite. In this mode, Unity Connection can
                                       		  use licensed feature except SpeechView and SpeechViewPro. The Evaluation Period
                                       		  of 90 days are provided once in the entire life cycle of the product. The
                                       		  Evaluation Period of Unity Connection begins as soon as it starts consuming
                                       		  licenses. After successful registration with CSSM, the Evaluation timer stops.
                                       		  You can further use the remaining Evaluation Period when Unity Connection will
                                       		  go in Unregister or Registration Expired state.

- Evaluation Period
                                          			 Expired : if Unity Connection uses licenses for 90 days without registering
                                       		  with CSSM or satellite, the status of Unity Connection changes to Evaluation
                                       		  Period Expired. In this mode, user creation or modification are not allowed.

- No Licenses in Use : If
                                       		  Unity Connection does not use any licenses, the status changes to No License in
                                       		  Use.

Authorized : In this
                                          			 state, all the licenses used by Unity Connection are authorized.

- Out of Compliance :
                                       		  Unity Connection authorization status changes to Out of Compliance either
                                       		  license usage exceeds the licenses available in the virtual account of the
                                       		  product or it uses the feature licenses that are not available in the virtual
                                       		  account.

- Authorization Expired :
                                       		  Unity Connection Authorization status changes to Authorization Expired if Unity
                                       		  Connection does not communicate with CSSM or satellite within the authorization
                                       		  time period of 90 days.

### License Reservation in Unity Connection

Cisco Unity Connection provide the following license reservation features:

In Specific License Reservation, reserved licenses of a virtual account are moved with the product instance.

This feature is limted to FedRAMP customers. Permanent License Tag can be ordered through Cisco Commerce Workspace and will
                                                be provisioned in the Smart Account and Virtual Account after Cisco approval. For ordering, see Cisco Collaboration Flex Plan 3.0 for FedRAMP Ordering Guide available at https://www.cisco.com/c/en/us/products/collateral/unified-communications/cisco-collaboration-flex-plan/guide-c07-744596.html . After acquiring permanent licenses, customers should operate within the defined limits of license counts which they have
                                                purchased.

#### Configuring Specific License Reservation in Unity Connection

In Specific License Reservation, Unity Connection requires a manual exchange of information with CSSM for product configuration
                                 and authorization. To configure Specific License Reservation and perform its various functions, execute the CLI commands in
                                 the given below sequence:

license smart reservation enable : This command is used to enable the license reservation feature.

license smart reservation request : This command is used to generate reservation request code for Unity Connection.

license smart reservation install "<authorization code>" or license smart reservation install-file : This command is used to install the license reservation authorization-code generated on the CSSM.

You can also perform additional operations by executing the given below CLI commands:

license smart reservation return : This command is used to generate a return code. The return code must be entered into the CSSM to return the licenses to
                                       the virtual account.

license smart reservation cancel : This command is used to cancel the reservation process before the authorization code obtained from CSSM against the product
                                       request code is installed.

license smart reservation return - authorization "<authorization code>" : This command is used to generate a return code using the authorization code specified on the command line. The return code
                                       must be entered into the CSSM to return the licenses to the virtual account.

In case of a cluster, you can execute the CLI commands only on publisher server.

#### Configuring Permanent License Reservation in Unity Connection

In Permanent License Reservation, Unity Connection requires a manual exchange of information with CSSM for product configuration
                                 and authorization. To configure Permanent License Reservation and perform its various functions, execute the CLI commands
                                 in the section Configuring Specific License Reservation in Unity Connection . These CLI commands are used for reserving Permanent License Tag.

Below mentioned CLI is specific to Permanent License Reservation:

license smart reservation set license_count : This CLI command is used to specify or update the license count for the system to operate within, when set for Permanent
                                       License Reservation. License count set doesn't affect compliance status and is for administrator reference only.License count
                                       set can be referred on the License Management screen. Customers will operate within the defined limits of license counts which
                                       they have purchased.

If this CLI is not executed below warning message will be displayed on License Management screen.

"Administrator has not specified the license this system would operate within. Please run the CLI command "license smart reservation
                                       set license_count" and complete the Permanent License Reservation process."

If the customer purchases more licenses in future, administrator can update the purchased license count by running the CLI
                                                   again.

For more information on above CLI commands, see Command Line Interface Reference Guide for Cisco Unified Communications Solutions Release 14 available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-command-reference-list.html .

#### License Reservation Status

When Unity Connection manually exchanges information once with the CSSM, there is a transition in the Unity Connection license
                                 reservation status.

The licensing status for Specific License Reservation and Permanent License Reservation of the Unity Connection can be categorized
                                 as follows:

##### Registration Status

The different registration status for Specific License Reservation and Permanent License Reservation in a Unity Connection
                                    server are:

Unregistered : The registration status of Unity Connection remains Unregistered until the product reservation request code has been generated.

Reservation In Progress : When Unity Connection generates the reservation request code, the licensing status changes to Reservation in Progress.

(Applicable to Specific License Reservation only) Registered - Specific License Reservation : When Unity Connection provides reservation request code to CSSM, CSSM generates an authorization code for the product. After
                                          successfully installing the authorization code on the product, the licensing status changes to Registered - Specific License
                                          Reservation.

(Applicable to Permanent License Resrvation only) Registered - Universal License Reservation : When Unity Connection provides reservation request code to CSSM, CSSM generates an authorization code for the product. After
                                          successfully installing the authorization code on the product, the licensing status changes to Registered - Universal License
                                          Reservation.

##### Authorization Status

Evaluation Mode: Unity Connection remains in Evaluation Mode until the product is not registered with CSSM. In this mode, Unity Connection
                                             can use licenses for 90 days.

Evaluation Period Expired: When Unity Connection uses licenses for 90 days without registering with CSSM, the status of Unity Connection changes to Evaluation
                                             Period Expired.

No License in Use: When Unity Connection does not use any licenses, the status changes to No License in Use.

Authorized - Reserved: When all the reserved licenses used by Unity Connection are authorized, the status changes to Authorized - Reserved.

(Not applicable to Permanent License Reservation) Not Authorized - Reserved: When Unity Connection license usage exceeds the licenses reserved in the virtual account of the product or it uses the feature
                                             licenses that are not reserved in the virtual account, the status changes to Not Authorized - Reserved.

### Enforcement Policy
                           	 on Unity Connection

When Unity Connection goes in either of the below state, it will go in enforcement mode. In this mode, user creation or modification
                                 in the user account, Speech Connect Port creation or modification and other licensing related updates are not allowed in Unity
                                 Connection in enforcement mode. However, existing users can send or receive the voice mails.

Evaluation
                                          				Period Expired

Registration Expired

Authorization Expired

Out of Compliance with 90 days of overage period expired.

For more information on the above states, see " Smart Software Licensing Status " section .

Evaluation Period Expired

Not Authorized - Reserved state with 90 days of overage period expired

For more information on the above states, see" License Reservation Status

In Evaluation Period Expired and Registration Expired states, Unity Connection generates an alarm to disable the encryption
                                 on the product. It is recommended that either you execute the "utils cuc encryption disable" CLI command to disable the encryption
                                 or register the product with CSSM or satellite to further use the security modules of the Unity Connection.

For more
                                 		  information on the CLI command, see the Command Line Interface Reference Guide
                                 		  for Cisco Unified Solutions for the latest release, available at http://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-maintenance-guides-list.html

For more information on the generated alarm, see Alarm Message Definitions for Cisco Unity Connection available at, https://www.cisco.com/c/en/us/support/unified-communications/unity-connection/products-system-message-guides-list.html .

### Licenses in Unity
                           	 Connection Cluster

In a Unity
                              		Connection cluster, both publisher and subscriber server use licenses but only
                              		publisher server is allowed to communicate with CSSM or satellite. Whenever the
                              		publisher server communicates with CSSM or satellite, the licensing status and
                              		usage information are updated on both publisher as well as subscriber server.
                              		In case, when publisher server stops functioning (for example, when it is shut
                              		down for maintenance), the subscriber server can use licenses but the licensing
                              		status remains unchanged. If the publisher server fails to resume its
                              		functioning within 90 days, the user account provisioning is not allowed on
                              		subscriber server.

In case of a
                              		cluster, only publisher server is allowed to perform the following operations:

- Registration

- Renew Authorization

- Renew Registration

- Deregister

- Reregister

After successful
                              		registration of the publisher server with CSSM or satellite, subscriber server
                              		only shows the licensing status and usage details of the product.

### Migrating
                           	 Licenses

Whenever you upgrade Cisco Unity Connection from any earlier releases to 14 and later, all licenses (legacy and PLM-based)
                              must be migrated to Cisco Smart Software Licensing. Customers with an active Cisco Software Support Service contract, can
                              convert PLM-based (pre-12.0 versions) licenses to Cisco Smart Software Licenses through the Cisco Smart Software Manager portal
                              at https://software.cisco.com/#SmartLicensing-LicenseConversion via License Registration Portal (LRP) at https://slexui.cloudapps.cisco.com/SWIFT/LicensingUI/Home . Customers can migrate fulfilled, partially fulfilled, and unfulfilled PAK's or device-based licenses to Cisco Smart Software
                              licenses. For legacy (pre-9.0 versions) licenses, customers must send a license migration request to Cisco Licensing Support
                              available at https://slexui.cloudapps.cisco.com/SWIFT/LicensingUI/html/contact.html . For customers with no service contract in place, upgrade SKU's must be ordered which will fulfill the new Cisco Smart Software
                              licenses to their organization's Cisco Smart Account and respective virtual account. Refer the Cisco Collaboration Ordering
                              Guide at http://www.cisco.com/c/en/us/partners/tools/collaboration-ordering-guides.html .

For more
                              		information on Cisco Smart Software Licensing, please visit http://www.cisco.com/c/en/us/buy/smart-accounts/software-licensing.html .

If HTTPS or Legacy
                              		networking is deployed in the system, you can migrate the licenses of each node
                              		gradually. It will not affect the system functionality.

### Enabling Encryption in Cisco Unity Connection

The Category C customers of Unity Connection can enable the encryption on the restricted version of Cisco Unity Connection
                              with both type of licensing – Cisco Smart Software Licensing and Specific License Reservation. To enable the encryption for
                              export restricted virtual account, you must have CUC Export Restricted Authorization Key (PID: CUC-SL-EXRTKY-K9=) license in the virtual account. In addition, you must perform below configuration to enable the encryption for Category C
                              customers.

Caution

The CUC Export Restricted Authorization Key (CUC-SL-EXRTKY-K9=) license is now End-of-Sale (EOS) .

End-of-Sale Date: August 2, 2020.

End-of-Support Date: August 31, 2025.

This license is no longer available for new purchases. If encryption is required for export-restricted virtual accounts:

1. Customers with existing licenses can continue using them until the End-of-Support date.

2. For new installations or upgrades to Cisco Unity Connection 14 or later, this license is no longer supported.

3. Contact your Cisco representative or reseller to explore alternative licensing options.

Enabling Encryption with Cisco Smart Software Licensing

Do the following procedure to enable the encryption with Cisco Smart Licensing

Register the Unity Connection with CSSM using token created from Category C customer's virtual account.

Unity Connection does not support Cisco Smart Software satellite as deployment option for export restricted virtual account.

Execute Export request CLI license smart export request local CUC_Export_Restricted_Authorization_Key on the registered Unity Connection server to install Export Restricted Authorization Key.

Execute utils cuc encryption enable CLI to enable the encryption on the product and restart the required services mentioned in the CLI output.

You can also perform additional operations by executing the given below CLI commands:

license smart export return local CUC_Export_Restricted_Authorization_Key to return an export restricted feature licenses.

license smart export cancel to cancel the automatic retry of previously failed export request or return from CSSM

For more information on CLI commands, see the applicable version of Command Line Interface Reference Guide for Cisco Unified Communications Solutions available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

Enabling Encryption with Specific License Reservation

To enable the encryption with Specific License Reservation, you must reserve the CUC Export Restricted Authorization Key license in virtual account of Category C customer on CSSM.

For more information on Export Control Functionality, see " Cisco Unity Connection- Restricted and Unrestricted Version " chapter of Security Guide for Cisco Unity Connection Release 15 available at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/15/security/guide/b_15cucsecx.html .

### License Parameters
                           	 for Unity Connection Features

Below table describes the Licence Parameters of Unity Connection feature applicable for Cisco Smart Software Licensing and
                                 Specific License Reservation.

License Parameter

Feature

Description

CUC_BasicMessaging

Total number of voicemail users.

Specifies the maximum number of voice mail users configured in Unity Connection.

CUC_EnhancedMessaging

Total number of enhanced messaging users.

Specifies the maximum number of Unity Connection SRSV users configured on Unity Connection. The Unity Connection SRSV users
                                                are reflected under this tag only when the branch is active. This tag also provides the licenses of Basic Messaging.

CUC_SpeechView

Total number of speech view standard users.

Specifies the maximum number of Speech view Standard users configured in Unity Connection.

CUC_SpeechViewPro

Total number of speech view professional users.

Specifies the maximum number of Speech view Professional users configured in Unity Connection.

CUC_SpeechConnectPort

Total number of speech connect ports.

Specifies the maximum number of simultaneous voice recognition sessions and Text to Speech (TTS) sessions allowed in Unity
                                                Connection.

CUC_SpeechConnectGuestUser 2

Total number of Contacts.

Specifes the maximum number of local contacts, along with VPIM contacts created from Non Unity Connection Server.

Cisco Smart Software Licensing supports license hierarchy, in which higher level licenses are utilized to fulfill the request
                                 for lower level licenses to avoid a shortage of the licenses.

Reserving entitlement tags of higher release on 12.x is not allowed. You can only borrow higher level licenses on 12.x at
                                             CSSM as per license hierarchy.

Following are the licenses included in license hierarchy in an order from higher level to lower level

- Unity Connection Enhanced Messaging User Licenses (12.x)

- Unity Connection Basic Messaging User Licenses (12.x)

| Note | Cisco Smart Software Licensing is only the way to manage the licenses in Unity Connection. |
|---|---|

| Note | In this
                                                      				option, Unity Connection must resolve the CSSM server directly through DNS. |
|---|---|

| Note | License hierarchy is supported only with Cisco Smart Software Manager satellite version 6.0.0 and later. |
|---|---|

| Note | If you upgrade the Unity Connection from any earlier releases to 14, all the licenses(legacy and PLM based) used in Unity
                                          Connection must be migrated to the CSSM for using Cisco Smart Software Licensing. For more information, see " Migrating Licenses " section. |
|---|---|

| Note | If data plane
                                          		  encryption (e.g. SRTP) has been turned on after registration to CSSM or
                                          		  satellite and the product is subsequently deregistered from CSSM or satellite,
                                          		  data plane encryption will continue to be enabled. An alarm will be sent
                                          		  warning the administer to disable data plane encryption when unregistered from
                                          		  CSSM or satellite. Data plane encryption will be disabled after a reboot of the
                                          		  product. Note that this encryption behavior, immediately after deregistration,
                                          		  may change in future versions of the product. |
|---|---|

| Step 1 | In Cisco Unity
                                             			 Connection Administration, expand System Settings and select Licenses. |
|---|---|
| Step 2 | On the
                                             			 Licenses page, select View/Edit link under Transport Settings field. A dialog box appears, on which select the
                                             			 applicable deployment option for the Smart Licensing. ( For more information,
                                             			 see Help > This Page) |
| Step 3 | Select Save. |

| Note | By default, the
                                             		  Direct option is selected. |
|---|---|

| Step 1 | Log in to
                                             			 your Smart Account in Cisco Smart Software Manager at software.cisco.com or
                                             			 Cisco Smart Software Manager satellite. |
|---|---|
| Step 2 | Select the
                                             			 virtual account that contains the licenses for the product. |
| Step 3 | In the
                                             			 General tab of virtual account, select New Token. |
| Step 4 | In the Create
                                             			 Registration Token dialog box, enter the Description and Expire After
                                             			 information and select Create Token. |
| Step 5 | To allow the
                                             			 Export Controlled Functionality for Unity Connection, check the Allow
                                                				export-controlled functionality on the products registered with this token check box. By checking the check box, you can enable the encryption for the
                                             			 product registered with this Registration Token. Note The Smart
                                                         				Account that are entitled to use Export Controlled Functionality can only check
                                                         				the Allow
                                                            				  export-controlled functionality on the products registered with this token check box. | Note | The Smart
                                                         				Account that are entitled to use Export Controlled Functionality can only check
                                                         				the Allow
                                                            				  export-controlled functionality on the products registered with this token check box. |
| Note | The Smart
                                                         				Account that are entitled to use Export Controlled Functionality can only check
                                                         				the Allow
                                                            				  export-controlled functionality on the products registered with this token check box. |
| Step 6 | Once the token
                                             			 is created, copy the token to register the product. |

| Note | The Smart
                                                         				Account that are entitled to use Export Controlled Functionality can only check
                                                         				the Allow
                                                            				  export-controlled functionality on the products registered with this token check box. |
|---|---|

| Step 1 | Log in to the
                                             			 Cisco Unity Connection Administration. |
|---|---|
| Step 2 | Expand System
                                             			 Settings and select Licenses. |
| Step 3 | On the
                                             			 Licenses page, select Register button. A dialog box appears, enter the registration token copied from the CSSM
                                             			 or satellite. |
| Step 4 | Select Register . |

| Note | In Specific License Reservation, reserved licenses of a virtual account are moved with the product instance. |
|---|---|

| Note | This feature is limted to FedRAMP customers. Permanent License Tag can be ordered through Cisco Commerce Workspace and will
                                                be provisioned in the Smart Account and Virtual Account after Cisco approval. For ordering, see Cisco Collaboration Flex Plan 3.0 for FedRAMP Ordering Guide available at https://www.cisco.com/c/en/us/products/collateral/unified-communications/cisco-collaboration-flex-plan/guide-c07-744596.html . After acquiring permanent licenses, customers should operate within the defined limits of license counts which they have
                                                purchased. |
|---|---|

| Note | In case of a cluster, you can execute the CLI commands only on publisher server. |
|---|---|

| Note | If the customer purchases more licenses in future, administrator can update the purchased license count by running the CLI
                                                   again. |
|---|---|

| Note | In case of Specific License Reservation, when Unity Connection goes in either of the below state, it will go in enforcement
                                                mode. Evaluation Period Expired Not Authorized - Reserved state with 90 days of overage period expired For more information on the above states, see" License Reservation Status |
|---|---|

| Note | After upgrading the Unity Connection from any earlier releases to 14, you must register the product with Cisco Smart Software
                                          Manager or Cisco Smart Software Manager satellite. |
|---|---|

| Caution | The CUC Export Restricted Authorization Key (CUC-SL-EXRTKY-K9=) license is now End-of-Sale (EOS) . End-of-Sale Date: August 2, 2020. End-of-Support Date: August 31, 2025. This license is no longer available for new purchases. If encryption is required for export-restricted virtual accounts: 1. Customers with existing licenses can continue using them until the End-of-Support date. 2. For new installations or upgrades to Cisco Unity Connection 14 or later, this license is no longer supported. 3. Contact your Cisco representative or reseller to explore alternative licensing options. |
|---|---|

| Note | Unity Connection does not support Cisco Smart Software satellite as deployment option for export restricted virtual account. |
|---|---|

| License Parameter | Feature | Description |
|---|---|---|
| CUC_BasicMessaging | Total number of voicemail users. | Specifies the maximum number of voice mail users configured in Unity Connection. |
| CUC_EnhancedMessaging | Total number of enhanced messaging users. | Specifies the maximum number of Unity Connection SRSV users configured on Unity Connection. The Unity Connection SRSV users
                                                are reflected under this tag only when the branch is active. This tag also provides the licenses of Basic Messaging. |
| CUC_SpeechView (Not applicable for Specific License Reservation) | Total number of speech view standard users. | Specifies the maximum number of Speech view Standard users configured in Unity Connection. |
| CUC_SpeechViewPro (Not applicable for Specific License Reservation) 1 | Total number of speech view professional users. | Specifies the maximum number of Speech view Professional users configured in Unity Connection. |
| CUC_SpeechConnectPort | Total number of speech connect ports. | Specifies the maximum number of simultaneous voice recognition sessions and Text to Speech (TTS) sessions allowed in Unity
                                                Connection. |
| CUC_SpeechConnectGuestUser 2 | Total number of Contacts. | Specifes the maximum number of local contacts, along with VPIM contacts created from Non Unity Connection Server. |

| Note | Reserving entitlement tags of higher release on 12.x is not allowed. You can only borrow higher level licenses on 12.x at
                                             CSSM as per license hierarchy. |
|---|---|