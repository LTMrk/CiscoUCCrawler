---
doc_id: help-webex-com-en-us-article-n5wdm6c-device-integration-guide-for-webex-for-cisco-broadworks-5ff8c53979
source_url: https://help.webex.com/en-us/article/n5wdm6c/Device-Integration-Guide-for-Webex-for-Cisco-BroadWorks
retrieved_at: 2026-09-01T17:21:17.216903+00:00
---

### Device Onboarding Overview

This chapter describes how to onboard devices to Webex for Cisco BroadWorks. This chapter covers the following use cases:

Onboard new Webex Room OS devices (using activation codes)

Onboard new MPP devices

Add Webex capability to existing MPP devices

We recommended that you deploy this feature on Release Independent ADP servers. However, XSP also supports this feature. If you're using XSP, then where this document refers to "ADP", you can substitute "XSP", unless the text specifies ADP only.

This feature supports both Personal and Workspace devices.

### Room OS Onboarding

Webex for Cisco BroadWorks supports activation code onboarding for both shared and workspace Room OS devices.

#### Device Onboarding with Activation Codes

Device Onboarding with activation codes provides a simple and secure way to onboard Room OS devices. An activation code is a 16-digit one-time system-generated passcode that a user must input on a device to onboard the device. The activation code is securely linked to the intended user account and assures that only the intended user onboards a device linked to the same account. After the user enters the correct code, the device connects to both Webex and BroadWorks, completes registration, downloads its configuration file, and is ready to use.

The following Room OS devices support onboarding with activation codes:

Webex Board Series (Room OS)

Webex Desk Series (Room OS)

Webex Room Series (Room OS)

#### Onboarding Process for Room OS

The following process shows what happens when a Room OS device onboards using activation codes:

The partner administrator provisions the primary user and device in BroadWorks and then generates the activation code in BroadWorks.

An email that contains the device activation code is sent to the device owner.

The device owner starts the device.

The device prompts the device owner to enter the activation code.

The device owner enters the activation code on the device.

The device onboards to BroadWorks and Webex using the following subprocess:

The Room OS device sends an activation request to Webex services. The activation code gets validated by GDS and if the code is correct, the device onboards to Webex. Webex returns a machine token to the device.

The device sends an activation request to the BroadWorks DM along with the machine token and MAC address.

BroadWorks authorizes and onboards the device.

The device sends a request to the BroadWorks DM for an updated config. The machine token is included for authorization.

BroadWorks authorizes the token, locates the updated config file, and returns an updated configuration file.

Room OS will attempt to locate a NAPTR record for the domain specified in the configuration file as it expects to find an SRV entry for _sip._tls.<domain_in_config> if no NAPTR record is present then RoomOS will then try and look for an SRV record followed by an A record respectively.

The SRV record must be _sip._tls. as roomOS will only support TLS for transport and SRTP for media.

The device registers and is ready to use.

The following diagram provides a simplified overview of the onboarding process.

For detailed information on Room OS onboarding, including more detailed flow diagrams, see the feature description Cisco BroadWorks Enhancements for Webex-Aware Device Onboarding .

#### Device Authentication (via OAuth Bearer Tokens)

Device authentication for Room OS devices requires that you enable Cisco OAuth Bearer Tokens on BroadWorks. During onboarding, the bearer token gets passed via the Activate Authorization header and serves to identify the device. The IdP validates the bearer token and returns the UUID (a machine UUID for workspace devices or user UUID for personal devices) as bearer subject. BroadWorks saves the UUID as the device name in the Network Server.

#### Room OS Prerequisites

##### Minimum Room OS Version

Room OS 10.13 minimum

##### BroadWorks Patch Requirements

This feature is supported as of version 2021.11 of the Release Independent (RI) ADP server with no patch requirements.

For non-RI servers, you must have installed the following patches (from patch groups ap381367, ap381951, ap382198) in order to use the feature. Install the patches that apply to your release:

For R22:

AP.as.22.0.1123.ap381367

AP.as.22.0.1123.ap382236

AP.nfm.22.0.1123.ap381367

AP.ns.22.0.1123.ap381367

AP.platform.22.0.1123.ap381367

AP.platform.22.0.1123.ap382198

AP.ps.22.0.1123.ap381367

AP.xsp.22.0.1123.ap381367

AP.xsp.22.0.1123.ap382198

For R23:

AP.as.23.0.1075.ap381367

AP.as.23.0.1075.ap382236

AP.ns.23.0.1075.ap381367

AP.platform.23.0.1075.ap382198

AP.platform.23.0.1075.ap381367

AP.xsp.23.0.1075.ap381367

AP.xsp.23.0.1075.ap382198

AP.ps.23.0.1075.ap381367

For R24:

AP.as.24.0.944.ap381367

AP.as.24.0.944.ap381951

AP.as.24.0.944.ap382236

##### BroadWorks Platform Requirements

This feature is available on:

R22: available on XSP only

R23: available on XSP or ADP (Release Independent)

R24: available on ADP (Release Independent)

##### BroadWorks Configuration Requirements

To implement this solution, the Flowthrough provisioning must be configured to allow Broadworks to provision devices to Webex.

While configuring the Flowthrough provisioning, it’s not mandatory to use flowthrough provisioning to provision users i.e., you can continue to use your existing provisioning methods (API, Trusted/Untrusted Email, User self, etc.) to provision users. See "Provisioning Requirements" in the Webex for Cisco BroadWorks Solution Guide .

Make sure that the Integrated IM+P service is enabled on BroadWorks and points to the BroadWorks Provisioning Bridge.

The Provisioning Bridge URL was assigned when the Customer Template was applied to the organization. This should have been completed during your initial Webex for Cisco BroadWorks setup. To find the existing URL in Partner Hub, see Configure Application Server with Provisioning Service URL in the Webex for Cisco BroadWorks Solution Guide .

If you have multiple partner organizations, you require a dedicated Device Management Service (DMS) instance per partner.

##### Prerequisites for Activation Code Onboarding with Room OS

Make sure that the following is set:

Deploy the Device Activation Service on BroadWorks. For details, see Cisco BroadWorks Secure Onboarding Using Activation Codes .

Verify that the DAS URL setting for the BroadWorks cluster is set to the
                        Device Management Services (DMS) URL. To view the current DAS URL setting in
                        Partner Hub, go to Settings > BroadWorks Calling > View Clusters and select the appropriate cluster. The URL appears under Interface settings .

If there are many customers (>50) in the BroadWorks cluster, the
                                ability to add the DAS URL is not supported. In such instances, it
                                is recommended to contact a Cisco TAC support engineer for
                                assistance.

The following BroadWorks features must be activated on the AS:

101377 Enhancements for Webex and MPP device onboarding

25088 Support Handsets for DECT Devices

24104 Support Multicell Chaining for DECT devices

20077 Device Management Enhancements

19559 Visual Device Management Enhancements

02283 Device Profile Type Customization Enhancements

For example, run the following command to enable 101377. Change the feature number when activating the other features: AS_CLI/System/ActivatableFeature> activate 101377

If all the listed patches are installed and an activatable feature is not listed for your particular AS release, it is because it is already included in your AS base release and does not require activation.

Run the following CLI command on the Network Server:

NS_CLI/System/DeviceManagement> asLocationLookupEnabled true

Make sure that the CA that signs your SBC certificate is listed in the Room OS Trust List. You can view the Room OS trust list from the Device Web Portal . On the portal, select Security > Collaboration Edge to view the list of CAs.

#### RoomOS Onboarding Flow

The RoomOS device is a Webex Aware Session Initiation Protocol (SIP)-based video device that uses SIP to communicate with Cisco BroadWorks for call control. Webex Aware RoomOS devices provide a rich Webex Meeting experience and BroadWorks telephony features.

This guide describes the specific configuration items that are important for use with BroadWorks. For more information on the purpose and use of all configuration items on the RoomOS devices, see Cisco RoomOS Devices Administration Guide .

Complete the following tasks to configure your system to support device onboarding with activation codes for the following Webex RoomOS devices:

Webex Board Series

Webex Desk Series

Webex Room Series

Configure Services for Room OS

Configure BroadWorks support for RoomOS devices.

Provision Room OS Devices

Provision the new device on BroadWorks.

Request Activation Code

In the Device Profile, request an activation code. The code will be emailed to the primary user automatically.

##### Configure Services for Room OS

Raise a Service Request with your onboarding agent or with Cisco TAC to provision Cisco OAuth for your Cisco Identity Provider Federation account. Title your service request "ADP AuthService Configuration".

If you already obtained Cisco OAuth Identity Provider credentials using one of the flows in this document, there’s no need to create a new request. However, if you obtained Cisco OAuth credentials using a flow that is not in this document, complete a new service request to update your credentials.

Cisco gives you an OAuth client ID, a client secret, and a refresh token that is valid for 60 days. If the token expires before you use it with your ADP, you can raise another request.

Enable OAuth by using this CLI command:

ADP_CLI/Applications/BroadworksDms/AccessControl/Authentication/OAuth> set enable true

Make sure that the OAuth scope includes broadworks-connector-user (the scope is enabled by default). Run this command to check your scopes:

ADP_CLI/Applications/BroadworksDms/AccessControl/Authentication/OAuth/Scopes> get

Configure the Cisco Identity Provider parameters using the below CLI commands.

ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider> set enabled false

set clientId <clientId> —see service request response for ID.

set clientSecret <clientSecret> —see service request response for secret.

set issuerName <URL> —see following table for URL.

set issuerUrl <URL> —see following table for URL.

set tokenInfoUrl <IdPProxy_URL> —see following tables for URL.

set ciResponseBodyMaxSizeInBytes 65536

US-A

https://idbroker.webex.com/idb

EU

https://idbroker-eu.webex.com/idb

US-B

https://idbroker-b-us.webex.com/idb

CA

https://idbroker-ca.webex.com/idb

SG

https://idbroker-sg.webex.com/idb

IN

https://idbroker-in.webex.com/idb

AE

https://idbroker-ae.webex.com/idb

AU

https://idbroker-au.webex.com/idb

If you don't know your CI Cluster , you can obtain the information from the Customer details in Help Desk view of Control Hub.

ACHM

https://broadworks-idp-proxy-a.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate

AFRA

https://broadworks-idp-proxy-k.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate

AORE

https://broadworks-idp-proxy-r.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate

ADXB

https://broadworks-idp-proxy-d.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate

ASYD

https://broadworks-idp-proxy-m.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate

If you don't know your Teams Cluster , you can obtain the information from the Customer details in the Help Desk view of Control Hub.

For testing, you can verify that the tokenInfoURL is valid by replacing the " idp/authenticate " portion of the URL with " ping ".

Configure Identity Providers for Cisco Federation using the following commands:

ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Partners> add FederationPartner refreshToken

New Password: <token from service request>

Re-type New Password: <token from service request>

...Done

ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Partners> get

Partner Name Refresh Token

==================================

FederationPartner ********

1 entry found.

ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Federation>

set flsUrl https://cifls.webex.com/federation

set refreshPeriodInMinutes 60

set partnerName FederationPartner

The refresh token is now under the CiscoIdentityProvider/Partners context and the partnerName from the CiscoIdentityProvider/Federation context needs to match the partner added in the CiscoIdentityProvider/Partners context.

If you are running an ADP RI load older than 2022.10, an R23 XSP without patch AP.xsp.23.0.1075.ap383838, or an R22 XSP, then:

You do not need to set a partner under 'System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Federation>'

The refresh token must be set under: System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Federation>

Clear all existing scopes within the following three contexts under ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/...

Scopes

Admin/RolesAllowed

Admin/ScopesAllowed

For each context, run a get to obtain the existing scopes and then delete them. For example:

```
ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Scopes> get
   delete <name_of_scope_1>
   delete <name_of_scope_2>
```

```
ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Admin/RolesAllowed> get
   delete <name_of_scope_1>
   delete <name_of_scope_2>
```

```
ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Admin/ScopesAllowed> get
   delete <name_of_scope_1>
   delete <name_of_scope_2>
```

##### Provision Room OS Devices

On BroadWorks CommPilot, check the Identity/Device Profile Type configuration to see if the device type exists for this Room OS device. If the device type does not exist on BroadWorks, import the device type into BroadWorks using a DTAF file that you download from cisco.com.

After you import the device type, make sure that the following settings exist within the Identity/Device Profile Type configuration:

Check the Allow Activation Code Onboarding check box

Check the Send Activation Code Request Through Messaging Server check box.

Set Authentication Mode to Bearer .

Validate that the Device Profile File has the SIP settings that you want to use. In the Identity/Device Profile Type File make sure that Authentication Mode is Bearer .

Create a Device Profile with the settings for your new device. In the Identity/Device Profile Add/Modify page, leave the MAC address field empty.

Configure the Primary User. On the Users Add page, check or uncheck the isPlace according to whether you intend the device to be personal or for a shared workspace.

Checked—Workspace device

Unchecked—Personal device

Shared workspace devices also require you to assign a primary user. You can assign the primary user that you want.

Complete the option that corresponds to the device type and provisioning method that you want to use:

- Device is for shared workspace—Use the Provision a BroadWorks Workspace API to complete provisioning for the workspace device.

- Device is personal; you want to provision using public APIs—Use the Provision BroadWorks Subscribers API to complete provisioning for the primary user.

- Device is personal; you want users to use self-activate—Forward the User Activation Portal URL to the user. The user must validate their email address to complete provisioning.

- Device is personal; you want to use flowthrough provisioning—Go to step 7.

If the device is for personal use, and you want to use flowthrough provisioning, then for the primary user, assign the Integrated IM+P service. On the User > Profile page, add the IM+P service:

From the Profile page, click Assign Services .

In the list of Available Services , select Integrated IM&P and use the arrow to move the item to the User Services box.

Click OK .

Click Profile .

Trusted email flow only. Add the user E-mail address. This setting serves as the IM&P email for flowthrough provisioning to Webex for Cisco BroadWorks. This is not required if you are using the untrusted email flow.

The Customer Template on Webex must be configured with settings for flowthrough provisioning with trusted emails or untrusted emails. For details, see the Webex for Cisco BroadWorks Solution Guide .

What to do next

##### Request Activation Code

In the Identity/Device Profile page, search for and open the device profile for your new device.

Click the Device Activation tab.

Click Request activation code .

What to do next

Provide the device to the user. After the user plugs in the device, they are required to enter the activation code that was sent in the email. This will onboard the device to Webex for Cisco BroadWorks.

### MPP Onboarding to Webex

This section describes the onboarding of either new or existing MPP devices to Webex for Cisco BroadWorks. Note that 'existing' refers to an MPP device that exists on BroadWorks, but which does not have Webex capability.

#### MPP Device Onboarding (New Devices)

During onboarding, the administrator updates BroadWorks with support for MPP, upgrades the device firmware and provisions the device on BroadWorks to complete onboarding.

The following diagram provides an overview of the onboarding process after the activation code that the user enters is validated.

#### MPP Device Onboarding (Existing Devices)

For existing MPP devices, where the device exists already on BroadWorks, but is not onboarded to Webex, update BroadWorks and the device firmware to support MPP to Webex onboarding. After the updates, the device onboards to Webex automatically.

#### More Information

For more information on MPP device onboarding to Webex, refer to the feature description Cisco BroadWorks DMS Enhancements for Webex Enabling MPP Devices .

#### MPP Device Prerequisites

##### Minimum MPP Version

MPP firmware 11.3.7 minimum

##### BroadWorks Patch Requirements

This feature is supported as of version 2021.11 of the Release Independent (RI) ADP server with no patch requirements.

For non-RI servers, you must have installed the following patches (from patch groups ap381367, ap381951, ap382198) in order to use the feature. Install the patches that apply to your release:

For R22:

AP.as.22.0.1123.ap381367

AP.as.22.0.1123.ap382236

AP.nfm.22.0.1123.ap381367

AP.ns.22.0.1123.ap381367

AP.platform.22.0.1123.ap381367

AP.platform.22.0.1123.ap382198

AP.ps.22.0.1123.ap381367

AP.xsp.22.0.1123.ap381367

AP.xsp.22.0.1123.ap382198

For R23:

AP.as.23.0.1075.ap381367

AP.as.23.0.1075.ap382236

AP.ns.23.0.1075.ap381367

AP.platform.23.0.1075.ap382198

AP.platform.23.0.1075.ap381367

AP.xsp.23.0.1075.ap381367

AP.xsp.23.0.1075.ap382198

AP.ps.23.0.1075.ap381367

For R24:

AP.as.24.0.944.ap381367

AP.as.24.0.944.ap381951

AP.as.24.0.944.ap382236

##### BroadWorks Platform Requirements

This feature is available on:

R22: available on XSP only

R23: available on XSP or ADP (Release Independent)

R24: available on ADP (Release Independent)

##### BroadWorks Configuration Requirements

To implement this solution, the Flowthrough provisioning must be configured to allow Broadworks to provision devices to Webex.

While configuring the Flowthrough provisioning, it’s not mandatory to use flowthrough provisioning to provision users i.e., you can continue to use your existing provisioning methods (API, Trusted/Untrusted Email, User self, etc.) to provision users. See "Provisioning Requirements" in the Webex for Cisco BroadWorks Solution Guide .

Make sure that the Integrated IM+P service is enabled on BroadWorks and points to the BroadWorks Provisioning Bridge.

The Provisioning Bridge URL was assigned when the Customer Template was applied to the organization. This should have been completed during your initial Webex for Cisco BroadWorks setup. To find the existing URL in Partner Hub, see Configure Application Server with Provisioning Service URL in the Webex for Cisco BroadWorks Solution Guide .

If you have multiple partner organizations, you require a dedicated Device Management Service (DMS) instance per partner.

##### Certificates and Firewalls

Make sure that you have configured the following:

Certificate Requirements—MPP devices use mTLS authentication using the device certificate. The device MAC address, which the certificate provides, authenticates the device. Download the required certificates for your MPP device from https://www.cisco.com/security/pki/ .

Cisco Root CA 2048 (crca2048) - PEM

Cisco Root CA 2099 (crca2099) - PEM

Cisco Root CA M1 (crcam1) - PEM

Cisco Root CA M2 (crcam2) - CER

Cisco Manufacturing CA (cmca) - PEM

Cisco Manufacturing CA (cmca2) - PEM

Cisco Manufacturing CA III (cmca3) - PEM

Upload your certificates to establish trust on the ADP or firewall. For example, if you’re uploading to the ADP, use this command:

ADP_CLI/Interface/Http/SSLCommonSettings/ClientAuthentication/Trusts/updateTrust> <certificate_filename>

Firewall requirements—If ADP is behind a firewall, your firewall must be configured with a rule to extract the MAC address from the device certificate and place it in an Authentication header that is then forwarded to the ADP. For example, the identity pattern .*([0-9a-fA-F]{12}).* can be used to extract the MAC address, which can then be placed in a header that uses a descriptive name (for example, macaddress ).

If ADP is not behind a firewall, the preceding requirement doesn’t exist.

##### Feature Activation

Activate the following BroadWorks features on the AS:

101377 Enhancements for Webex and MPP device onboarding

25088 Support Handsets for DECT Devices

23775 Remote Reset for MPP Devices

24104 Support Multicell Chaining for DECT devices

20077 Device Management Enhancements

19559 Visual Device Management Enhancements

02283 Device Profile Type Customization Enhancements

For example, run the following command to enable 101377.Change the feature number when activating the other features: AS_CLI/System/ActivatableFeature> activate 101377

If all the listed patches are installed and an activatable feature is not listed for your particular AS release, it is because it is already included in your AS base release and does not require activation.

Run the following CLI on the Network Server:

NS_CLI/System/DeviceManagement> asLocationLookupEnabled true

##### Activation Code Requirements

Optional. Activation codes are not mandatory for MPP device onboarding. Howver, if you want to use activation codes, see Request Activation Code for MPP for additional requirements that are specific to activation codes with MPP.

#### MPP Device Onboarding Flow

If you’re adding Webex capability to an MPP device that exists on BroadWorks already, complete steps 1 and 2 only.

Configure Services for MPP

(New or existing MPP devices). Configure system support for MPP on Webex for Cisco BroadWorks.

Upgrade MPP Device Firmware

(Existing MPP devices). For any existing MPP devices for which you want to add Webex capability, upgrade to the latest device firmware.

Provision MPP Device

(New MPP devices only). If the device doesn’t exist on BroadWorks, provision the device and primary user on BroadWorks.

Request Activation Code for MPP

(Optional). If you want to use activation codes to onboard MPP devices, request an activation code.

##### Configure Services for MPP

Update your BroadWorks system settings to support MPP devices (new or existing) on
                Webex for Cisco BroadWorks. Complete this step only once. You don’t need to repeat
                this procedure for each MPP device.

Before you begin

If the ADP is behind a firewall, your firewall must be configured with a rule to extract the MAC address from the device certificate and place it in an Authentication header that is then forwarded to the ADP. For example, the identity pattern .*([0-9a-fA-F]{12}).* can be used to extract the MAC address, which can then be placed in a header that uses a descriptive name (for example, macaddress ).

Refer to your firewall documentation for help with the configurations.

Raise a Service Request with your onboarding agent or with Cisco TAC to provision Cisco OAuth for your Cisco Identity Provider Federation account. Use "ADP AuthService Configuration" to title your request.

Cisco gives you an OAuth client ID, a client secret, and a refresh token that is valid for 60 days. If the token expires before you use it with your ADP, you can raise another request.

If you already obtained Cisco OAuth Identity Provider credentials using one of the flows in this document, there’s no need to create a new request. However, if you obtained Cisco OAuth credentials using a flow that is not in this document, complete a new service request to update your credentials.

Configure the Cisco Identity Provider parameters by running the following CLI commands.

ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider> set enabled false

set clientId <clientId> —see service request response for ID.

set clientSecret <clientSecret> —see service request response for secret.

set issuerName <URL> —see following table for URL.

set issuerUrl <URL> —see following table for URL.

set ciResponseBodyMaxSizeInBytes 65536

US-A

https://idbroker.webex.com/idb

EU

https://idbroker-eu.webex.com/idb

US-B

https://idbroker-b-us.webex.com/idb

CA

https://idbroker-ca.webex.com/idb

SG

https://idbroker-sg.webex.com/idb

IN

https://idbroker-in.webex.com/idb

AE

https://idbroker-ae.webex.com/idb

AU

https://idbroker-au.webex.com/idb

If you don't know your CI Cluster , you can obtain the information from the Customer details in Help Desk view of Control Hub.

Set the url of the DM Bridge using the below CLI command. The DM Bridge URL is different for each  Teams Cluster (which you pulled in Step 2).

```
ADP_CLI/Applications/BroadworksDms/DeviceActivation/DMBridge> set
url = <url_of_DM_Bridge>
scope = dm-bridge:device_auth
```

If Teams Cluster is...

Set DM_Bridge URL to...

ACHM

dm-bridge-a.wbx2.com

AORE

dm-bridge-r.wbx2.com

AFRA

dm-bridge-k.wbx2.com

ADXB

dm-bridge-d.wbx2.com

ASYD

dm-bridge-m.wbx2.com

Enable MAC address extraction and authentication using either the Authentication header or Authentication certificate. For security reasons, we recommend that you use one of the options only:

Authentication header—If the ADP is behind a firewall, use the CLI on
                                the ADP to enable MAC address extraction for the Authentication
                                header. This configuration gives the ADP the ability to recognize
                                the MAC address from the Authentication header.  For example:

ADP_CLI/Applications/BroadworksDms/AccessControl/Authentication/Headers> set enable true

ADP_CLI/Applications/BroadworksDms/AccessControl/Authentication/Headers> set identityPattern "macaddress:.*([0-9a-fA-F]{12}).*"

In this example, macaddress is an assigned name
                                    with .*([0-9a-fA-F]{12}).* representing the
                                    pattern that gets assigned to the header. If you call the header
                                    something other than macaddress , adjust your
                                    CLI accordingly.

Authentication certificate—If ADP is not behind a firewall, authentication occurs between the device and ADP directly. Use the below CLI commands to enable MAC address extraction on the device certificate for authentication:

ADP_CLI/Applications/BroadworksDms/AccessControl/Authentication/Certificates> set enable true

ADP_CLI/Applications/BroadworksDms/AccessControl/Authentication/Certificates> set identityPattern ".*([0-9a-fA-F]{12}).*"

##### Upgrade MPP Device Firmware

Before you begin

Upgrade the device firmware to the latest version to ensure that tha the MPP device supports Webex capability.

For more information on firmware upgrades, refer to the Release Notes for your phone model firmware release.

What to do next

Existing MPP devices—After the upgrade, the device onboards to Webex automatically. The user can start using Webex services on the device.

New MPP devices—Provision the new MPP device on BroadWorks.

##### Provision MPP Device

On BroadWorks CommPilot, check the Identity/Device Profile Type configuration to see if the device type exists for this MPP device. If the device type doesn’t exist on BroadWorks, import the device type into BroadWorks using a DTAF file that is downloaded from cisco.com.

On BroadWorks CommPilot, open the Identity/Device Profile Type and check the Allow Activation Code Onboarding check box.

Create an Identity/Device Profile Type File with the SIP settings that you want to use.

Create an Identity/Device Profile with settings for your new device. In the MAC address field, enter the device MAC address.

If you are using activation codes to onboard MPP devices, leave the MAC address field empty.

Configure the Primary User. On the Users Add page, set the isPlace check box according to whether the device is personal or for a shared workspace:

Checked—Workspace device

Unchecked—Personal device

Complete the option that corresponds to the device type and provisioning method that you want to use:

- Device is for shared workspace—Use the Provision a BroadWorks Workspace API to complete provisioning for the workspace device.

- Device is personal; you want to provision using public APIs—Use the Provision BroadWorks Subscribers API to complete provisioning for the primary user.

- Device is personal; you want users to use self-activate—Forward the User Activation Portal URL to the user. The user must validate their email address to complete provisioning.

- Device is personal; you want to use flowthrough provisioning—Go to step 7.

If the device is for personal use, and you want to use flowthrough provisioning, then for the primary user, assign the Integrated IM+P service. On the User > Profile page, add the IM+P service:

From the Profile page, click Assign Services .

In the list of Available Services , select Integrated IM&P and use the arrow to move the item to the User Services box.

Click OK .

Click Profile .

Trusted email flow only. Add the user E-mail address. This setting serves as the IM&P email for flowthrough provisioning to Webex for Cisco BroadWorks. This is not required if you are using the untrusted email flow.

The Customer Template on Webex must be configured with settings for flowthrough provisioning with trusted emails or untrusted emails. For details, see the Webex for Cisco BroadWorks Solution Guide .

What to do next

##### Request Activation Code for MPP

(Optional) Webex for Cisco BroadWorks does not require activation codes to onboard new MPP devices. However, if you do decide to use activation codes, complete the Request Activation Code procedure to request an activation code for a new device.

###### Prerequisites for Using Activation Codes with MPP Devices

If you are using activation code onboarding for MPP devices, make sure that your system meets the following activation code-specific requirements.

Device Activation Service —Complete the following requirements to enable the Device Activation Service:

Deploy the Device Activation Service on BroadWorks. For details, see Cisco BroadWorks Secure Onboarding Using Activation Codes .

Point the Device Activation Service (DAS) to Device Management Services (DMS) on BroadWorks AS using the following CLI command:

AS_CLI/Interface/DAS> set url <url_of_DMS>

Verify that the DAS URL setting for the BroadWorks cluster is set to the
                        Device Management Services (DMS) URL. To view the current DAS URL setting in
                        Partner Hub, go to Settings > BroadWorks Calling > View Clusters and select the appropriate cluster. The URL appears under Interface settings .

If there are many customers (>50) in the BroadWorks cluster, the
                                ability to add the DAS URL is not supported. In such instances, it
                                is recommended to contact a Cisco TAC support engineer for
                                assistance.

Cisco Global Discovery Services (GDS) —GDS is required in order to provision the activation code. Enable GDS on BroadWorks by completing both of the below steps:

Create a service request to provision your GDS account. Cisco provides you with the client ID, client secret, refresh token and GDS domain.

After your GDS account is provisioned, enable GDS on the ADP using the following CLI:

```
ADP_CLI/Applications/BroadworksDms/DeviceActivation/IdentityProviders/Cisco> get
  set gdsDomain <gds_domain_from service request> e.g. https://activation.webex.com
  set clientId <id_from_service_request>
  clientSecret <secret_from_service_request>
  refreshToken <token_from_service_request>
```

In addition to the above activation code-specific prerequisites, your system must meet the general MPP prerequisites in MPP Device Prerequisites .

###### Request Activation Code

Complete the following steps to request an activation code for a new MPP device.

In the Identity/Device Profile page, search for and open the device profile for your new device.

Click the Device Activation tab.

Click Request activation code .

The system generates the activation code and emails the code to the primary user. The user must enter the code on the device to complete onboarding.

| 1 | Configure Services for Room OS Configure BroadWorks support for RoomOS devices. |
|---|---|
| 2 | Provision Room OS Devices Provision the new device on BroadWorks. |
| 3 | Request Activation Code In the Device Profile, request an activation code. The code will be emailed to the primary user automatically. |

| 1 | Raise a Service Request with your onboarding agent or with Cisco TAC to provision Cisco OAuth for your Cisco Identity Provider Federation account. Title your service request "ADP AuthService Configuration". If you already obtained Cisco OAuth Identity Provider credentials using one of the flows in this document, there’s no need to create a new request. However, if you obtained Cisco OAuth credentials using a flow that is not in this document, complete a new service request to update your credentials. Cisco gives you an OAuth client ID, a client secret, and a refresh token that is valid for 60 days. If the token expires before you use it with your ADP, you can raise another request. |
|---|---|
| 2 | Enable OAuth by using this CLI command: ADP_CLI/Applications/BroadworksDms/AccessControl/Authentication/OAuth> set enable true |
| 3 | Make sure that the OAuth scope includes broadworks-connector-user (the scope is enabled by default). Run this command to check your scopes: ADP_CLI/Applications/BroadworksDms/AccessControl/Authentication/OAuth/Scopes> get |
| 4 | Configure the Cisco Identity Provider parameters using the below CLI commands. ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider> set enabled false set clientId <clientId> —see service request response for ID. set clientSecret <clientSecret> —see service request response for secret. set issuerName <URL> —see following table for URL. set issuerUrl <URL> —see following table for URL. set tokenInfoUrl <IdPProxy_URL> —see following tables for URL. set ciResponseBodyMaxSizeInBytes 65536 Table 1. Set issuerName and issuerURL If CI Cluster is... Set issuerName and issuerURL to... US-A https://idbroker.webex.com/idb EU https://idbroker-eu.webex.com/idb US-B https://idbroker-b-us.webex.com/idb CA https://idbroker-ca.webex.com/idb SG https://idbroker-sg.webex.com/idb IN https://idbroker-in.webex.com/idb AE https://idbroker-ae.webex.com/idb AU https://idbroker-au.webex.com/idb If you don't know your CI Cluster , you can obtain the information from the Customer details in Help Desk view of Control Hub. Table 2. Set tokenInfoURL If Teams Cluster is... Set tokenInfoURL to...(IdP Proxy URL) ACHM https://broadworks-idp-proxy-a.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate AFRA https://broadworks-idp-proxy-k.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate AORE https://broadworks-idp-proxy-r.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate ADXB https://broadworks-idp-proxy-d.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate ASYD https://broadworks-idp-proxy-m.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate If you don't know your Teams Cluster , you can obtain the information from the Customer details in the Help Desk view of Control Hub. For testing, you can verify that the tokenInfoURL is valid by replacing the " idp/authenticate " portion of the URL with " ping ". | If CI Cluster is... | Set issuerName and issuerURL to... | US-A | https://idbroker.webex.com/idb | EU | https://idbroker-eu.webex.com/idb | US-B | https://idbroker-b-us.webex.com/idb | CA | https://idbroker-ca.webex.com/idb | SG | https://idbroker-sg.webex.com/idb | IN | https://idbroker-in.webex.com/idb | AE | https://idbroker-ae.webex.com/idb | AU | https://idbroker-au.webex.com/idb | If you don't know your CI Cluster , you can obtain the information from the Customer details in Help Desk view of Control Hub. | If Teams Cluster is... | Set tokenInfoURL to...(IdP Proxy URL) | ACHM | https://broadworks-idp-proxy-a.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate | AFRA | https://broadworks-idp-proxy-k.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate | AORE | https://broadworks-idp-proxy-r.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate | ADXB | https://broadworks-idp-proxy-d.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate | ASYD | https://broadworks-idp-proxy-m.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate | If you don't know your Teams Cluster , you can obtain the information from the Customer details in the Help Desk view of Control Hub. For testing, you can verify that the tokenInfoURL is valid by replacing the " idp/authenticate " portion of the URL with " ping ". |
| If CI Cluster is... | Set issuerName and issuerURL to... |
| US-A | https://idbroker.webex.com/idb |
| EU | https://idbroker-eu.webex.com/idb |
| US-B | https://idbroker-b-us.webex.com/idb |
| CA | https://idbroker-ca.webex.com/idb |
| SG | https://idbroker-sg.webex.com/idb |
| IN | https://idbroker-in.webex.com/idb |
| AE | https://idbroker-ae.webex.com/idb |
| AU | https://idbroker-au.webex.com/idb |
| If you don't know your CI Cluster , you can obtain the information from the Customer details in Help Desk view of Control Hub. |
| If Teams Cluster is... | Set tokenInfoURL to...(IdP Proxy URL) |
| ACHM | https://broadworks-idp-proxy-a.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| AFRA | https://broadworks-idp-proxy-k.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| AORE | https://broadworks-idp-proxy-r.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| ADXB | https://broadworks-idp-proxy-d.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| ASYD | https://broadworks-idp-proxy-m.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| If you don't know your Teams Cluster , you can obtain the information from the Customer details in the Help Desk view of Control Hub. For testing, you can verify that the tokenInfoURL is valid by replacing the " idp/authenticate " portion of the URL with " ping ". |
| 5 | Configure Identity Providers for Cisco Federation using the following commands: ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Partners> add FederationPartner refreshToken New Password: <token from service request> Re-type New Password: <token from service request> ...Done ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Partners> get Partner Name Refresh Token ================================== FederationPartner ******** 1 entry found. ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Federation> set flsUrl https://cifls.webex.com/federation set refreshPeriodInMinutes 60 set partnerName FederationPartner The refresh token is now under the CiscoIdentityProvider/Partners context and the partnerName from the CiscoIdentityProvider/Federation context needs to match the partner added in the CiscoIdentityProvider/Partners context. If you are running an ADP RI load older than 2022.10, an R23 XSP without patch AP.xsp.23.0.1075.ap383838, or an R22 XSP, then: You do not need to set a partner under 'System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Federation>' The refresh token must be set under: System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Federation> |
| 6 | Clear all existing scopes within the following three contexts under ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/... Scopes Admin/RolesAllowed Admin/ScopesAllowed For each context, run a get to obtain the existing scopes and then delete them. For example: ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Scopes> get
   delete <name_of_scope_1>
   delete <name_of_scope_2> ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Admin/RolesAllowed> get
   delete <name_of_scope_1>
   delete <name_of_scope_2> ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider/Admin/ScopesAllowed> get
   delete <name_of_scope_1>
   delete <name_of_scope_2> |

| If CI Cluster is... | Set issuerName and issuerURL to... |
|---|---|
| US-A | https://idbroker.webex.com/idb |
| EU | https://idbroker-eu.webex.com/idb |
| US-B | https://idbroker-b-us.webex.com/idb |
| CA | https://idbroker-ca.webex.com/idb |
| SG | https://idbroker-sg.webex.com/idb |
| IN | https://idbroker-in.webex.com/idb |
| AE | https://idbroker-ae.webex.com/idb |
| AU | https://idbroker-au.webex.com/idb |
| If you don't know your CI Cluster , you can obtain the information from the Customer details in Help Desk view of Control Hub. |

| If Teams Cluster is... | Set tokenInfoURL to...(IdP Proxy URL) |
|---|---|
| ACHM | https://broadworks-idp-proxy-a.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| AFRA | https://broadworks-idp-proxy-k.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| AORE | https://broadworks-idp-proxy-r.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| ADXB | https://broadworks-idp-proxy-d.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| ASYD | https://broadworks-idp-proxy-m.wbx2.com/broadworks-idp-proxy/api/v1/idp/authenticate |
| If you don't know your Teams Cluster , you can obtain the information from the Customer details in the Help Desk view of Control Hub. For testing, you can verify that the tokenInfoURL is valid by replacing the " idp/authenticate " portion of the URL with " ping ". |

| 1 | On BroadWorks CommPilot, check the Identity/Device Profile Type configuration to see if the device type exists for this Room OS device. If the device type does not exist on BroadWorks, import the device type into BroadWorks using a DTAF file that you download from cisco.com. |
|---|---|
| 2 | After you import the device type, make sure that the following settings exist within the Identity/Device Profile Type configuration: Check the Allow Activation Code Onboarding check box Check the Send Activation Code Request Through Messaging Server check box. Set Authentication Mode to Bearer . |
| 3 | Validate that the Device Profile File has the SIP settings that you want to use. In the Identity/Device Profile Type File make sure that Authentication Mode is Bearer . |
| 4 | Create a Device Profile with the settings for your new device. In the Identity/Device Profile Add/Modify page, leave the MAC address field empty. |
| 5 | Configure the Primary User. On the Users Add page, check or uncheck the isPlace according to whether you intend the device to be personal or for a shared workspace. Checked—Workspace device Unchecked—Personal device Shared workspace devices also require you to assign a primary user. You can assign the primary user that you want. |
| 6 | Complete the option that corresponds to the device type and provisioning method that you want to use: Device is for shared workspace—Use the Provision a BroadWorks Workspace API to complete provisioning for the workspace device. Device is personal; you want to provision using public APIs—Use the Provision BroadWorks Subscribers API to complete provisioning for the primary user. Device is personal; you want users to use self-activate—Forward the User Activation Portal URL to the user. The user must validate their email address to complete provisioning. Device is personal; you want to use flowthrough provisioning—Go to step 7. |
| 7 | If the device is for personal use, and you want to use flowthrough provisioning, then for the primary user, assign the Integrated IM+P service. On the User > Profile page, add the IM+P service: From the Profile page, click Assign Services . In the list of Available Services , select Integrated IM&P and use the arrow to move the item to the User Services box. Click OK . Click Profile . Trusted email flow only. Add the user E-mail address. This setting serves as the IM&P email for flowthrough provisioning to Webex for Cisco BroadWorks. This is not required if you are using the untrusted email flow. The Customer Template on Webex must be configured with settings for flowthrough provisioning with trusted emails or untrusted emails. For details, see the Webex for Cisco BroadWorks Solution Guide . |

| 1 | In the Identity/Device Profile page, search for and open the device profile for your new device. |
|---|---|
| 2 | Click the Device Activation tab. |
| 3 | Click Request activation code . |

| 1 | Configure Services for MPP (New or existing MPP devices). Configure system support for MPP on Webex for Cisco BroadWorks. |
|---|---|
| 2 | Upgrade MPP Device Firmware (Existing MPP devices). For any existing MPP devices for which you want to add Webex capability, upgrade to the latest device firmware. |
| 3 | Provision MPP Device (New MPP devices only). If the device doesn’t exist on BroadWorks, provision the device and primary user on BroadWorks. |
| 4 | Request Activation Code for MPP (Optional). If you want to use activation codes to onboard MPP devices, request an activation code. |

| 1 | Raise a Service Request with your onboarding agent or with Cisco TAC to provision Cisco OAuth for your Cisco Identity Provider Federation account. Use "ADP AuthService Configuration" to title your request. Cisco gives you an OAuth client ID, a client secret, and a refresh token that is valid for 60 days. If the token expires before you use it with your ADP, you can raise another request. If you already obtained Cisco OAuth Identity Provider credentials using one of the flows in this document, there’s no need to create a new request. However, if you obtained Cisco OAuth credentials using a flow that is not in this document, complete a new service request to update your credentials. |
|---|---|
| 2 | Configure the Cisco Identity Provider parameters by running the following CLI commands. ADP_CLI/System/CommunicationUtility/DefaultSettings/ExternalAuthentication/CiscoIdentityProvider> set enabled false set clientId <clientId> —see service request response for ID. set clientSecret <clientSecret> —see service request response for secret. set issuerName <URL> —see following table for URL. set issuerUrl <URL> —see following table for URL. set ciResponseBodyMaxSizeInBytes 65536 Table 3. Set issuerName and issuerURL If CI Cluster is... Set issuerName and issuerURL to... US-A https://idbroker.webex.com/idb EU https://idbroker-eu.webex.com/idb US-B https://idbroker-b-us.webex.com/idb CA https://idbroker-ca.webex.com/idb SG https://idbroker-sg.webex.com/idb IN https://idbroker-in.webex.com/idb AE https://idbroker-ae.webex.com/idb AU https://idbroker-au.webex.com/idb If you don't know your CI Cluster , you can obtain the information from the Customer details in Help Desk view of Control Hub. | If CI Cluster is... | Set issuerName and issuerURL to... | US-A | https://idbroker.webex.com/idb | EU | https://idbroker-eu.webex.com/idb | US-B | https://idbroker-b-us.webex.com/idb | CA | https://idbroker-ca.webex.com/idb | SG | https://idbroker-sg.webex.com/idb | IN | https://idbroker-in.webex.com/idb | AE | https://idbroker-ae.webex.com/idb | AU | https://idbroker-au.webex.com/idb | If you don't know your CI Cluster , you can obtain the information from the Customer details in Help Desk view of Control Hub. |
| If CI Cluster is... | Set issuerName and issuerURL to... |
| US-A | https://idbroker.webex.com/idb |
| EU | https://idbroker-eu.webex.com/idb |
| US-B | https://idbroker-b-us.webex.com/idb |
| CA | https://idbroker-ca.webex.com/idb |
| SG | https://idbroker-sg.webex.com/idb |
| IN | https://idbroker-in.webex.com/idb |
| AE | https://idbroker-ae.webex.com/idb |
| AU | https://idbroker-au.webex.com/idb |
| If you don't know your CI Cluster , you can obtain the information from the Customer details in Help Desk view of Control Hub. |
| 3 | Set the url of the DM Bridge using the below CLI command. The DM Bridge URL is different for each  Teams Cluster (which you pulled in Step 2). ADP_CLI/Applications/BroadworksDms/DeviceActivation/DMBridge> set
url = <url_of_DM_Bridge>
scope = dm-bridge:device_auth Table 4. DM_Bridge URL If Teams Cluster is... Set DM_Bridge URL to... ACHM dm-bridge-a.wbx2.com AORE dm-bridge-r.wbx2.com AFRA dm-bridge-k.wbx2.com ADXB dm-bridge-d.wbx2.com ASYD dm-bridge-m.wbx2.com | If Teams Cluster is... | Set DM_Bridge URL to... | ACHM | dm-bridge-a.wbx2.com | AORE | dm-bridge-r.wbx2.com | AFRA | dm-bridge-k.wbx2.com | ADXB | dm-bridge-d.wbx2.com | ASYD | dm-bridge-m.wbx2.com |
| If Teams Cluster is... | Set DM_Bridge URL to... |
| ACHM | dm-bridge-a.wbx2.com |
| AORE | dm-bridge-r.wbx2.com |
| AFRA | dm-bridge-k.wbx2.com |
| ADXB | dm-bridge-d.wbx2.com |
| ASYD | dm-bridge-m.wbx2.com |
| 4 | Enable MAC address extraction and authentication using either the Authentication header or Authentication certificate. For security reasons, we recommend that you use one of the options only: Authentication header—If the ADP is behind a firewall, use the CLI on
                                the ADP to enable MAC address extraction for the Authentication
                                header. This configuration gives the ADP the ability to recognize
                                the MAC address from the Authentication header.  For example: ADP_CLI/Applications/BroadworksDms/AccessControl/Authentication/Headers> set enable true ADP_CLI/Applications/BroadworksDms/AccessControl/Authentication/Headers> set identityPattern "macaddress:.*([0-9a-fA-F]{12}).*" In this example, macaddress is an assigned name
                                    with .*([0-9a-fA-F]{12}).* representing the
                                    pattern that gets assigned to the header. If you call the header
                                    something other than macaddress , adjust your
                                    CLI accordingly. Authentication certificate—If ADP is not behind a firewall, authentication occurs between the device and ADP directly. Use the below CLI commands to enable MAC address extraction on the device certificate for authentication: ADP_CLI/Applications/BroadworksDms/AccessControl/Authentication/Certificates> set enable true ADP_CLI/Applications/BroadworksDms/AccessControl/Authentication/Certificates> set identityPattern ".*([0-9a-fA-F]{12}).*" |

| If CI Cluster is... | Set issuerName and issuerURL to... |
|---|---|
| US-A | https://idbroker.webex.com/idb |
| EU | https://idbroker-eu.webex.com/idb |
| US-B | https://idbroker-b-us.webex.com/idb |
| CA | https://idbroker-ca.webex.com/idb |
| SG | https://idbroker-sg.webex.com/idb |
| IN | https://idbroker-in.webex.com/idb |
| AE | https://idbroker-ae.webex.com/idb |
| AU | https://idbroker-au.webex.com/idb |
| If you don't know your CI Cluster , you can obtain the information from the Customer details in Help Desk view of Control Hub. |

| If Teams Cluster is... | Set DM_Bridge URL to... |
|---|---|
| ACHM | dm-bridge-a.wbx2.com |
| AORE | dm-bridge-r.wbx2.com |
| AFRA | dm-bridge-k.wbx2.com |
| ADXB | dm-bridge-d.wbx2.com |
| ASYD | dm-bridge-m.wbx2.com |

| Upgrade the device firmware to the latest version to ensure that tha the MPP device supports Webex capability. For more information on firmware upgrades, refer to the Release Notes for your phone model firmware release. |
|---|

| 1 | On BroadWorks CommPilot, check the Identity/Device Profile Type configuration to see if the device type exists for this MPP device. If the device type doesn’t exist on BroadWorks, import the device type into BroadWorks using a DTAF file that is downloaded from cisco.com. |
|---|---|
| 2 | On BroadWorks CommPilot, open the Identity/Device Profile Type and check the Allow Activation Code Onboarding check box. |
| 3 | Create an Identity/Device Profile Type File with the SIP settings that you want to use. |
| 4 | Create an Identity/Device Profile with settings for your new device. In the MAC address field, enter the device MAC address. If you are using activation codes to onboard MPP devices, leave the MAC address field empty. |
| 5 | Configure the Primary User. On the Users Add page, set the isPlace check box according to whether the device is personal or for a shared workspace: Checked—Workspace device Unchecked—Personal device |
| 6 | Complete the option that corresponds to the device type and provisioning method that you want to use: Device is for shared workspace—Use the Provision a BroadWorks Workspace API to complete provisioning for the workspace device. Device is personal; you want to provision using public APIs—Use the Provision BroadWorks Subscribers API to complete provisioning for the primary user. Device is personal; you want users to use self-activate—Forward the User Activation Portal URL to the user. The user must validate their email address to complete provisioning. Device is personal; you want to use flowthrough provisioning—Go to step 7. |
| 7 | If the device is for personal use, and you want to use flowthrough provisioning, then for the primary user, assign the Integrated IM+P service. On the User > Profile page, add the IM+P service: From the Profile page, click Assign Services . In the list of Available Services , select Integrated IM&P and use the arrow to move the item to the User Services box. Click OK . Click Profile . Trusted email flow only. Add the user E-mail address. This setting serves as the IM&P email for flowthrough provisioning to Webex for Cisco BroadWorks. This is not required if you are using the untrusted email flow. The Customer Template on Webex must be configured with settings for flowthrough provisioning with trusted emails or untrusted emails. For details, see the Webex for Cisco BroadWorks Solution Guide . |