---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-operation-guide-chcs-b-hcs-smart-licensing-operational-874b1a2e16
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/Operation_Guide/chcs_b_hcs-smart-licensing-operational-guide/chcs_b_hcs-smart-licensing-operational-guide_chapter_01.html
retrieved_at: 2026-09-01T20:56:05.586850+00:00
---

Cisco Hosted Collaboration Solution Smart Licensing Operation Guide, Release 12.5

# Cisco Hosted Collaboration Solution Smart Licensing Operation Guide, Release 12.5

Updated: April 23, 2020

Chapter: Using Smart Licensing

## Chapter: Using Smart Licensing

# Using Smart Licensing

## Enabling Operational License

The Partner must send an email to hcbu-a2q@external.cisco.com requesting to enable the HCS Operational License.

Ensure to include Cisco Account and Cisco Sales in the email for reference.

The Partner uses a single VA (Ordered Virtual Account) to place the order for all the customers in Cisco Commerce (CCW).

These licenses are not used by the Unified Communication Applications

Using HCM-F is mandatory.

A single VA (Operational License Pool) is shared for both Flex Hosted (EA/NU) and HCS Perpetual Licenses.

Cisco deposits operational licenses into this VA. This Virtual Account is used by UC Applications for consumption.

The Partner can avail auto registration features.

## Cisco Smart Software Manager (CSSM)

Cisco Smart Software Manager allows product instances to register and report license consumption.

You can use Cisco Smart Software Manager to:

Manage and track licenses

Move licenses across virtual account

Remove registered product instance

Enable Javascript 1.5 or a later version in your browser.

We recommend using connected mode for the satellite connection.

For details on Cisco Smart Software Manager (CSSM), see https://software.cisco.com/ .

### Initial One Time Setup in CSSM for Smart Licensing

Log in to Cisco Smart Software Manager (CSSM) portal ( https://software.cisco.com ).

Create a Smart Account (if you do not have a smart account) in CSSM, or get access to an existing smart account.

Send an email to smart-operations@cisco.com , requesting API access for your Cisco ID.

The support team provides access to your ID and responds with a confirmation email.

Create a CSSM client application with the CCO ID which stores the client ID and client secret.

The CCO ID used must have a Smart Account User role for the specific Smart Account for HCM-F to manage it.

To create the application, select the OAuth Grant type as Client Credentials Grant . HCM-F uses the Client Credentials Grant type to communicate with CSSM.

To create a new application with client credentials, click on Request API Access from the Cisco API Developer Portal and
                                             select the Client Credentials Grant option.

Login to the Smart Account in CSSM, and create Virtual Accounts, as per your requirement.

The admin does not need to create any product registration token to register the product. HCM- F performs all the token management for product registration.

While assigning the clusters to VA, the export control cannot be set if HCM-F creates the product registration token. To set
                                                         the export control value, you have to manually create the product registration token in CSSM and select the export control
                                                         check-box. For more information about how to register the UC applications that are in mixed mode to the VA in CSSM, see Registering the UC Applications in Mixed Mode to VA in CSSM .

We recommend you to get access to the operational licenses. If you have opted for operational licenses, then add the two virtual
                                             accounts: ordered virtual account (va-hcs-ordered), and operational virtual account (va-hcs-operational). For more information
                                             about operational licenses, see Configuring Operational Licenses .

Register your product with CSSM, using HCM-F.

For more information on how to register UC applications in HCM-F, see Add Cluster Application in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide .

Log in to CCW, select a smart account and virtual account, and order HCS licenses.

Configure Smart Software Licensing alerts in CSSM.

For more information about adding the On-prem local account to CSSM, see Smart Software Manager On-Prem User Guide .

If any of the virtual account has a cluster assigned to it and you need to delete the account, it is required to unassign
                                                         the cluster from that account in HCM-F before you proceed to delete the account from CSSM server.

#### Generating Client Credentials in Smart Accounts and Licensing API

##### Before you begin

To request API access for your Cisco ID, send an email to the support team at smart-operations@cisco.com . The support team takes the necessary steps to provide access to your ID and respond with a confirmation email within 24
                                          hours.

The CCO ID used must have a Smart Account User role for the specific Smart Account, for HCM-F to manage it.

Log in to Smart Accounts and Licensing API .

Click Request API Access .

Click New Application .

Enter these details in the Add application window.

Name: HCM-F instance

Description: API access for HCM-F

Select Client Credentials Grant from the OAuth  Grant Type list

Select automatically register the redirect URIs for AP Notebook and API

HCM-F uses the Client Credentials Grant type to communicate with CSSM.

Click Add .

The application is created and it redirects to the original URL.

Select the application from the drop-down, accept the Terms and Conditions, and click Request API Access

It generates the Client ID and secret.

To get access to the smart account APIs, you must send mail to smart-operations@cisco.com with the CCO ID, smart account domain name, and the application created. Once mail is sent, you have to wait for few days
                                                            to receive a confirmation message.

##### What to do next

From the Smart Accounts and Licensing API website. Click Developer Portal .

Click My Applications and select the Application name that is created for the HCMF instance.

You can view the Client ID and Client Secret.

#### Registering the UC Applications in Mixed Mode to VA in CSSM

##### Before you begin

Create a token in the VA and select export control functionality.

Run a CSSM sync from HCMF.

Ensure that only the manually created token is present in the VA.

Perform cluster assignment.

## Cisco Smart Software Manager On-Prem(Satellite)

Cisco Smart Software Manager on-prem (satellite) is similar to Cisco Smart Software Manager (CSSM). However, instead of being
                           hosted on cisco.com, it is available as an on-premise version.

Cisco Smart Software Manager on-prem (satellite) is used to:

Manage and track licenses of the on-premise users

Support multiple local accounts (multi-tenant)

Scale 10,000 product instances

Connect to Cisco either online or offline

Enable Javascript 1.5 or a later version in your browser. Use Cisco Smart Software Manager satellite 7.2 or later version
                                       to use all the functionalities.

For details on Cisco Smart Software Manager on-prem (satellite), see Smart Licensing .

### Initial One Time Setup in CSSM on-prem for Smart Licensing

You can register the clusters to CSSM by using either the proxy
                                 or the on-prem server.

Pre-requisite for Registering Expressways clusters to
                                 the Cisco Smart Software Manager (CSSM) on-prem server for Smart Licensing

Configure the Expressway clusters with DNS and domain name of the on-prem
                                       Server to adhere to the FQDN requirements of the CSSM On-Prem Server to
                                       on-prem CSSM.

Expressway-E clusters are registered to CSSM via Proxy Mode, if Proxy is set
                                       at the Cluster level.

Expressway-E clusters are registered to CSSM via Direct Mode, if Proxy is set
                                       at Customer Level.

Expressway-C clusters are registered to CSSM via Proxy Mode, if Proxy is set
                                       at either Cluster level or Customer level.

Create a new or existing SSM on-prem local Account and register the account
                                 before using the Smart Licensing functions in the licensing workspace. Until you
                                 complete the registration process, all other Smart Licensing options are not
                                 available. Both network and manual registrations are supported.

For more
                                 information about CSSM on-prem configuration, see Smart Software Manager On-Prem User Guide .

Log in to Smart Software Manager on-prem portal.

Create a Local Account or get access to an existing local account.

For more information about CSSM on-prem configuration, and creating local
                                             account, see Smart Software Manager On-Prem User Guide .

Approve the account using the user name and password.

Click Network , and ensure the hostname which is used in
                                          the registration URL is specified in the SSM On-Prem
                                             Name . Save the configuration.

Click Security , and ensure the hostname which is used in
                                          the registration URL is specified in the Host common
                                             name . Save the configuration.

For CSSM On-Prem version 6, use https:// satellite-server-ip /Transportgateway/services/DeviceRequestHandler as the registration URL.

For CSSM On-Prem version 7, use https://< satellite-server-fqdn >/SmartTransport as the hostname:8443.

For CSSM On-Prem version 8, use https://< satellite-server-fqdn >/SmartTransport as the hostname:8443.

Update the
                                             registration URL in HCMF whenever you upgrade the Satellite Servers.

For example, if the registration url is: https:// hostname /Transportgateway/services/DeviceRequestHandler ,
                                             then the SSM On-Prem Name is hostname and Host common name is same as the CSSM On-Prem
                                             hostname. Example of a token url is: https:// hostname:8443 /backend/oauth/token .

Click Synchronisation , and do a full
                                          synchronization.

Enable the API tool kit and create the client ID and secret for the local
                                          account.

To create a product registration token in SSM on-prem, see Creating Product
                                             Instance Registration Tokens section in the Smart Software Manager On-Prem User Guide .

If any of the virtual account has a cluster assigned to it and you need to delete the account, it is required to unassign
                                                         the cluster from that account in HCM-F before you proceed to delete the account from the CSSM on-prem server.

## Smart Accounts and Virtual Accounts

For details on Cisco Smart Accounts and Virtual Accounts, see https://software.cisco.com/ .

## Smart Licensing Deployment Options

The following options are available for connecting to CSSM and Satellite :

Proxy is the recommended transport mode.

HCS 12.5 release does not support Smart Licensing APIs.

## License Conversion and Migration to Smart Licensing

You can convert Classic, PAK-based licenses (PLM licenses) to a Smart Entitlement (if a Smart License equivalent is available).
                           The license conversion can be performed in the License Registration Portal (LRP) or in Cisco Smart Software Manager (CSSM).
                           You can initiate the process by downloading and installing the Smart Licensing version of the software and registering the
                           device to a Smart Account using a Registration Token. The migration of any entitlements tracked by Cisco, automatically migrates
                           to the Customers Smart Account.

License conversion can be performed either on:

LRP ( License Registration Portal ), go to the PAKs/Tokens tab, select Actions > Convert to Smart Entitlement , or

CSSM ( Cisco Smart Software Manager ), go to the License Conversion tab to convert Classic Licenses to Smart Licenses.

For more information on converting classic licenses to smart licenses, see Migrating classic licenses to smart licenses with active SWSS in Cisco Smart Software Licensing with Cisco Unified Communications Manager 12.0 Solution Overview

## HCS Managed Services

The UC applications and Prime License Manager (PLM) are available on premise. HCM-F does not have connectivity to the on-premise
                           applications.

The change in Cisco Smart Software Manager (CSSM) helps customers migrating from Enterprise to cloud, to use HCS licenses
                           that are Flex Hosted. The Flex Hosted licenses in version 12.x and later work for both on-premise UC (Enterprise mode) and
                           HCS cloud (HCS mode) so it provides an easier migration from on-premise to HCS as there is no need to migrate licenses during
                           the migration phase.

The CSSM accepts the license request from Enterprise UC applications in Enterprise mode and allocates the mapped HCS licenses
                           if corresponding Enterprise licenses are not available. This is called dual parenting.

CSSM follows hierarchy in allocating the licenses. The higher level licences are utilized to fulfill the request for lower
                           level licenses and avoid a shortage of the licenses.The licences are allocated in the following priority, higher to lower-order:

Enterprise (when both Enterprise and HCS licences are available)

HCS Foundation (when the Enterprise licences are all allocated or when there are only HCS licences)

HCS Standard (when the Enterprise licences are all allocated or when there are only HCS licences)

Following is the HCS license mapping for Enterprise licenses:

HCS License

Cisco Unified CM

Cisco Unity Connection

Cisco Emergency Responder

HCS Cisco UCM Foundation License

Basic

Essential

Enhanced

HCS Cisco UCM Standard License

Cisco Unified Workspace Licensing (UWL)

Enhanced plus

HCS Cisco UCM TelePresence Room License

Telepresence Room

HCS Unity Connection Basic License

CUC_BasicMessaging

HCS Unity Connection Standard License

CUC_EnhancedMessaging

HCS Emergency Responder User License

CER_USER

### Migration from On Premise to HCS

Use this procedure to change the license mode for the Unified Communication applications
                              and PLM from enterprise license mode to HCS mode for cluster versions below 12.x  and
                              for versions 12.x and later. Use the ciscocm.HCSMode_v4.cop.sgn file to change the licensing from Enterprise Mode to HCS Mode. Install the cop file on
                              the publisher node of all Cisco Unified CM, Cisco Emergency Responder, and Cisco Unity
                              Connection clusters, and standalone PLM or co-resident PLM. The cop file is available at License Mode Change - Enterprise Mode to HCS Mode .

To change the licensing from HCS Mode to Enterprise Mode, install the ciscocm.EnterpriseMode_v4.cop.sgn file on the publisher node of
                              all Cisco Unified CM, Cisco Emergency Responder, and Cisco Unity Connection clusters,
                              and standalone PLM or co-resident PLM. The cop file is available at License Mode Change: HCS Mode to Enterprise Mode .

For detailed information on the COP files, see these links:

To change from enterprise mode to HCS mode: Readme for License Migration from On-prem to Hosted
                                 Collaboration Solution .

To change from HCS mode to enterprise mode: Readme for License Migration from Hosted
                                 Collaboration Solution to On-prem .

## Smart Versus Traditional Licensing

Traditional (node locked) licensing

Smart (dynamic) licensing

You procure the license and manually install it on the PLM.

Your device requests the licenses that it needs from CSSM.

Node-locked licenses - license is associated with a specific device.

Pooled licenses - Smart accounts are the company account specific that can be used with any compatible device in your company.

No common install base location to view the licenses that are purchased or software usage trends.

Licenses are stored securely on Cisco servers that are accessible 24x7x365.

No easy means to transfer licenses from one device to another.

Licenses can be moved between product instances without a license transfer, which greatly simplifies the reassignment of a
                                       software license as part of the Return Material Authorization (RMA) process.

Limited visibility into all software licenses being used in the network. Licenses are tracked only on per node basis.

Complete view of all Smart Software Licenses used in the network using a consolidated usage report of software licenses and
                                       devices in one easy-to-use portal.

| Step 1 | The Partner must send an email to hcbu-a2q@external.cisco.com requesting to enable the HCS Operational License. Ensure to include Cisco Account and Cisco Sales in the email for reference. |
|---|---|
| Step 2 | The Partner uses a single VA (Ordered Virtual Account) to place the order for all the customers in Cisco Commerce (CCW). These licenses are not used by the Unified Communication Applications |
| Step 3 | Using HCM-F is mandatory. |
| Step 4 | A single VA (Operational License Pool) is shared for both Flex Hosted (EA/NU) and HCS Perpetual Licenses. Cisco deposits operational licenses into this VA. This Virtual Account is used by UC Applications for consumption. |
| Step 5 | The Partner can avail auto registration features. |

| Note | Enable Javascript 1.5 or a later version in your browser. We recommend using connected mode for the satellite connection. |
|---|---|

| Step 1 | Log in to Cisco Smart Software Manager (CSSM) portal ( https://software.cisco.com ). |
|---|---|
| Step 2 | Create a Smart Account (if you do not have a smart account) in CSSM, or get access to an existing smart account. |
| Step 3 | Send an email to smart-operations@cisco.com , requesting API access for your Cisco ID. The support team provides access to your ID and responds with a confirmation email. |
| Step 4 | Create a CSSM client application with the CCO ID which stores the client ID and client secret. Note The CCO ID used must have a Smart Account User role for the specific Smart Account for HCM-F to manage it. To create the application, select the OAuth Grant type as Client Credentials Grant . HCM-F uses the Client Credentials Grant type to communicate with CSSM. To create a new application with client credentials, click on Request API Access from the Cisco API Developer Portal and
                                             select the Client Credentials Grant option. | Note | The CCO ID used must have a Smart Account User role for the specific Smart Account for HCM-F to manage it. To create the application, select the OAuth Grant type as Client Credentials Grant . HCM-F uses the Client Credentials Grant type to communicate with CSSM. |
| Note | The CCO ID used must have a Smart Account User role for the specific Smart Account for HCM-F to manage it. To create the application, select the OAuth Grant type as Client Credentials Grant . HCM-F uses the Client Credentials Grant type to communicate with CSSM. |
| Step 5 | Login to the Smart Account in CSSM, and create Virtual Accounts, as per your requirement. Note The admin does not need to create any product registration token to register the product. HCM- F performs all the token management for product registration. While assigning the clusters to VA, the export control cannot be set if HCM-F creates the product registration token. To set
                                                         the export control value, you have to manually create the product registration token in CSSM and select the export control
                                                         check-box. For more information about how to register the UC applications that are in mixed mode to the VA in CSSM, see Registering the UC Applications in Mixed Mode to VA in CSSM . We recommend you to get access to the operational licenses. If you have opted for operational licenses, then add the two virtual
                                             accounts: ordered virtual account (va-hcs-ordered), and operational virtual account (va-hcs-operational). For more information
                                             about operational licenses, see Configuring Operational Licenses . | Note | The admin does not need to create any product registration token to register the product. HCM- F performs all the token management for product registration. While assigning the clusters to VA, the export control cannot be set if HCM-F creates the product registration token. To set
                                                         the export control value, you have to manually create the product registration token in CSSM and select the export control
                                                         check-box. For more information about how to register the UC applications that are in mixed mode to the VA in CSSM, see Registering the UC Applications in Mixed Mode to VA in CSSM . |
| Note | The admin does not need to create any product registration token to register the product. HCM- F performs all the token management for product registration. While assigning the clusters to VA, the export control cannot be set if HCM-F creates the product registration token. To set
                                                         the export control value, you have to manually create the product registration token in CSSM and select the export control
                                                         check-box. For more information about how to register the UC applications that are in mixed mode to the VA in CSSM, see Registering the UC Applications in Mixed Mode to VA in CSSM . |
| Step 6 | Register your product with CSSM, using HCM-F. For more information on how to register UC applications in HCM-F, see Add Cluster Application in Cisco Hosted Collaboration Mediation Fulfillment Install and Configure Guide . Note Until you register, your product is still in Evaluation Mode. | Note | Until you register, your product is still in Evaluation Mode. |
| Note | Until you register, your product is still in Evaluation Mode. |
| Step 7 | Log in to CCW, select a smart account and virtual account, and order HCS licenses. Note HCS licenses get deposited to the smart account and virtual accounts. | Note | HCS licenses get deposited to the smart account and virtual accounts. |
| Note | HCS licenses get deposited to the smart account and virtual accounts. |
| Step 8 | Configure Smart Software Licensing alerts in CSSM. For more information to configure the alerts, see https://software.cisco.com For more information about adding the On-prem local account to CSSM, see Smart Software Manager On-Prem User Guide . Note If any of the virtual account has a cluster assigned to it and you need to delete the account, it is required to unassign
                                                         the cluster from that account in HCM-F before you proceed to delete the account from CSSM server. | Note | If any of the virtual account has a cluster assigned to it and you need to delete the account, it is required to unassign
                                                         the cluster from that account in HCM-F before you proceed to delete the account from CSSM server. |
| Note | If any of the virtual account has a cluster assigned to it and you need to delete the account, it is required to unassign
                                                         the cluster from that account in HCM-F before you proceed to delete the account from CSSM server. |

| Note | The CCO ID used must have a Smart Account User role for the specific Smart Account for HCM-F to manage it. To create the application, select the OAuth Grant type as Client Credentials Grant . HCM-F uses the Client Credentials Grant type to communicate with CSSM. |
|---|---|

| Note | The admin does not need to create any product registration token to register the product. HCM- F performs all the token management for product registration. While assigning the clusters to VA, the export control cannot be set if HCM-F creates the product registration token. To set
                                                         the export control value, you have to manually create the product registration token in CSSM and select the export control
                                                         check-box. For more information about how to register the UC applications that are in mixed mode to the VA in CSSM, see Registering the UC Applications in Mixed Mode to VA in CSSM . |
|---|---|

| Note | Until you register, your product is still in Evaluation Mode. |
|---|---|

| Note | HCS licenses get deposited to the smart account and virtual accounts. |
|---|---|

| Note | If any of the virtual account has a cluster assigned to it and you need to delete the account, it is required to unassign
                                                         the cluster from that account in HCM-F before you proceed to delete the account from CSSM server. |
|---|---|

| Step 1 | Log in to Smart Accounts and Licensing API . |
|---|---|
| Step 2 | Click Request API Access . |
| Step 3 | Click New Application . |
| Step 4 | Enter these details in the Add application window. Name: HCM-F instance Description: API access for HCM-F Select Client Credentials Grant from the OAuth  Grant Type list Select automatically register the redirect URIs for AP Notebook and API HCM-F uses the Client Credentials Grant type to communicate with CSSM. |
| Step 5 | Click Add . The application is created and it redirects to the original URL. |
| Step 6 | Select the application from the drop-down, accept the Terms and Conditions, and click Request API Access It generates the Client ID and secret. Note To get access to the smart account APIs, you must send mail to smart-operations@cisco.com with the CCO ID, smart account domain name, and the application created. Once mail is sent, you have to wait for few days
                                                            to receive a confirmation message. | Note | To get access to the smart account APIs, you must send mail to smart-operations@cisco.com with the CCO ID, smart account domain name, and the application created. Once mail is sent, you have to wait for few days
                                                            to receive a confirmation message. |
| Note | To get access to the smart account APIs, you must send mail to smart-operations@cisco.com with the CCO ID, smart account domain name, and the application created. Once mail is sent, you have to wait for few days
                                                            to receive a confirmation message. |

| Note | To get access to the smart account APIs, you must send mail to smart-operations@cisco.com with the CCO ID, smart account domain name, and the application created. Once mail is sent, you have to wait for few days
                                                            to receive a confirmation message. |
|---|---|

| Step 1 | Create a token in the VA and select export control functionality. |
|---|---|
| Step 2 | Run a CSSM sync from HCMF. |
| Step 3 | Ensure that only the manually created token is present in the VA. |
| Step 4 | Perform cluster assignment. |

| Note | Enable Javascript 1.5 or a later version in your browser. Use Cisco Smart Software Manager satellite 7.2 or later version
                                       to use all the functionalities. |
|---|---|

| Step 1 | Log in to Smart Software Manager on-prem portal. |
|---|---|
| Step 2 | Create a Local Account or get access to an existing local account. For more information about CSSM on-prem configuration, and creating local
                                             account, see Smart Software Manager On-Prem User Guide . |
| Step 3 | Approve the account using the user name and password. |
| Step 4 | Click Network , and ensure the hostname which is used in
                                          the registration URL is specified in the SSM On-Prem
                                             Name . Save the configuration. |
| Step 5 | Click Security , and ensure the hostname which is used in
                                          the registration URL is specified in the Host common
                                             name . Save the configuration. For CSSM On-Prem version 6, use https:// satellite-server-ip /Transportgateway/services/DeviceRequestHandler as the registration URL. For CSSM On-Prem version 7, use https://< satellite-server-fqdn >/SmartTransport as the hostname:8443. For CSSM On-Prem version 8, use https://< satellite-server-fqdn >/SmartTransport as the hostname:8443. Update the
                                             registration URL in HCMF whenever you upgrade the Satellite Servers. For example, if the registration url is: https:// hostname /Transportgateway/services/DeviceRequestHandler ,
                                             then the SSM On-Prem Name is hostname and Host common name is same as the CSSM On-Prem
                                             hostname. Example of a token url is: https:// hostname:8443 /backend/oauth/token . |
| Step 6 | Click Synchronisation , and do a full
                                          synchronization. |
| Step 7 | Enable the API tool kit and create the client ID and secret for the local
                                          account. To create a product registration token in SSM on-prem, see Creating Product
                                             Instance Registration Tokens section in the Smart Software Manager On-Prem User Guide . Note If any of the virtual account has a cluster assigned to it and you need to delete the account, it is required to unassign
                                                         the cluster from that account in HCM-F before you proceed to delete the account from the CSSM on-prem server. | Note | If any of the virtual account has a cluster assigned to it and you need to delete the account, it is required to unassign
                                                         the cluster from that account in HCM-F before you proceed to delete the account from the CSSM on-prem server. |
| Note | If any of the virtual account has a cluster assigned to it and you need to delete the account, it is required to unassign
                                                         the cluster from that account in HCM-F before you proceed to delete the account from the CSSM on-prem server. |

| Note | If any of the virtual account has a cluster assigned to it and you need to delete the account, it is required to unassign
                                                         the cluster from that account in HCM-F before you proceed to delete the account from the CSSM on-prem server. |
|---|---|

| Note | Proxy is the recommended transport mode. |
|---|---|

| HCS License | Enterprise Licenses |
|---|---|
| Cisco Unified CM | Cisco Unity Connection | Cisco Emergency Responder |
| HCS Cisco UCM Foundation License | Basic Essential Enhanced |  |  |
| HCS Cisco UCM Standard License | Cisco Unified Workspace Licensing (UWL) Enhanced plus |  |  |
| HCS Cisco UCM TelePresence Room License | Telepresence Room |  |  |
| HCS Unity Connection Basic License |  | CUC_BasicMessaging |  |
| HCS Unity Connection Standard License |  | CUC_EnhancedMessaging |  |
| HCS Emergency Responder User License |  |  | CER_USER |

| Traditional (node locked) licensing | Smart (dynamic) licensing |
|---|---|
| You procure the license and manually install it on the PLM. | Your device requests the licenses that it needs from CSSM. |
| Node-locked licenses - license is associated with a specific device. | Pooled licenses - Smart accounts are the company account specific that can be used with any compatible device in your company. |
| No common install base location to view the licenses that are purchased or software usage trends. | Licenses are stored securely on Cisco servers that are accessible 24x7x365. |
| No easy means to transfer licenses from one device to another. | Licenses can be moved between product instances without a license transfer, which greatly simplifies the reassignment of a
                                       software license as part of the Return Material Authorization (RMA) process. |
| Limited visibility into all software licenses being used in the network. Licenses are tracked only on per node basis. | Complete view of all Smart Software Licenses used in the network using a consolidated usage report of software licenses and
                                       devices in one easy-to-use portal. |