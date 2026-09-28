---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-maintenance-guide-pcce-b-featur-190d5a4fb5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/maintenance/guide/pcce_b_features_guide_12_5/pcce_b_pcce_features_guide_12_5_chapter_01100.html
retrieved_at: 2026-08-21T04:48:03.959793+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 12.5(1)

Updated: July 29, 2021

Chapter: Single Sign-On

## Chapter: Single Sign-On

# Single Sign-On

## Single
                        	 Sign-On

Single sign-on (SSO) is an authentication and authorization process. (Authentication proves that you are the user you say
                              that you are, and authorization verifies that you are allowed to do what you want to do.) SSO allows you to sign in to one
                              application and then securely access other authorized applications without a prompt to resupply user credentials. SSO permits
                              Cisco supervisors or agents to sign on only once with a username and password. Supervisors and agents gain access to all of
                              their Cisco browser-based applications and services within a single browser instance. By using SSO, Cisco administrators can
                              manage all users from a common user directory and enforce password policies for all users consistently.

Before enabling SSO in Packaged CCE, ensure to sign in to the Cisco Unified Intelligence Center OAMP interface and perform the Unified CCE User Integration
                                          operation (Cluster Configuration > UCCE User Integration) once manually to import the Supervisors with the required roles.

This is only applicable for Unified CCE deployment.

SSO is an optional feature whose implementation requires you to enable the HTTPS protocol across the enterprise solution.

You can implement single sign-on in one of these modes:

SSO - Enable all agents and supervisors in the deployment for SSO.

Hybrid - Enable agents and supervisors selectively in the deployment for SSO. Hybrid mode allows you to phase in the migration of agents from a non-SSO deployment to an SSO
                                    deployment and enable SSO for local PGs. Hybrid mode is useful if you have third-party applications that don't support SSO,
                                    and some agents and supervisors must be SSO-disabled to sign in to those applications.

Non-SSO - Continue to use existing Active Directory-based and local authentication, without SSO.

SSO uses Security Assertion Markup Language (SAML) to exchange authentication and authorization details between an identity
                              provider (IdP) and an identity service (IdS). The IdP authenticates based on user credentials, and the IdS provides authorization
                              between the IdP and applications. The IdP issues SAML assertions, which are packages of security information transferred from
                              the IdP to the service provider for user authentication. Each assertion is an XML document that contains trusted statements
                              about a subject including, for example, username and privileges. SAML assertions are digitally signed to ensure their authenticity.

The IdS generates an authentication request (also known as a SAML request) and directs it to the IdP. SAML does not specify
                              the method of authentication at the IdP. It may use a username and password or other form of authentication, including multi-factor
                              authentication. A directory service such as LDAP or AD that allows you to sign in with a username and a password is a typical
                              source of authentication tokens at an IdP.

### Prerequisites

The Identity Provider must support Security Assertion Markup Language (SAML) 2.0. See the Compatibility Matrix for your solution at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-device-support-tables-list.html for details.

### Contact Center Enterprise Reference Design Support for Single Sign-On

Packaged CCE supports single sign-on for these reference designs:

2000 Agents

4000 Agents

12000 Agents

### Coresidency of Cisco Identity Service by Reference Design

Reference Design

Packaged
                                             						CCE Solution

2000 Agent

Cisco IdS is coresident with Unified Intelligence Center and Live Data on a single VM.

4000 Agent

Standalone Cisco IdS VM

12000 Agent

Standalone Cisco IdS VM

### Single Sign-On Support and Limitations

Note the following points that are related to SSO support:

To support SSO, enable the HTTPS protocol across the enterprise solution.

SSO supports agents and supervisors only. SSO support is not available for administrators in this release.

SSO supports multiple domains with federated trusts.

SSO supports only contact center enterprise peripherals.

SSO support is available for Agents and Supervisors that are registered to remote or main site PG in global deployments.

Note the following limitations that are related to SSO support:

SSO support is not available for third-party Automatic Call Distributors (ACDs).

The SSO feature does not support Cisco Finesse IP Phone Agent (FIPPA).

The SSO feature does not support Cisco Finesse Desktop Chat.

### Allowed Operations by Node Type

The Cisco IdS cluster contains a publisher and a subscriber node. A publisher node can perform any configuration and access token operations.
                              The operations that a subscriber node can perform depends on whether the publisher is connected to the cluster.

This table lists which operations each type of node can perform.

Operation

Allowed on Publisher

Allowed on Subscriber

Upload IdP metadata

Always

Never

Download SAML SP metadata

Always

Never

Regenerate SAML Certificate

Always

Never

Regenerate Token Encryption/Signing Key

Always

Never

Update AuthCode/Token Expiry

Always

Only when publisher is connected

Enable/Disable Token Encryption

Always

Only when publisher is connected

Add/Update/Delete Cisco IdS client configuration

Always

Only when publisher is connected

View Cisco IdS client configuration

Always

Always

View Cisco IdS status

Always

Always

Set Troubleshooting Log Level

Always

Always

Set Remote Syslog server

Always

Always

### Single Sign-On Log Out

For a complete logout from all applications, sign out of the applications and close the browser window. In a Windows desktop,
                              log out of the Windows account. In a Mac desktop, quit the browser application.

Users enabled for single sign-on are at risk of having their accounts misused by others if the browser is not closed completely.
                                          If the browser is left open, a different user can access the application from the browser page without entering credentials.

## Single Sign-On
                        	 Flow

Single sign-on (SSO) configuration by an administrator follows this
                              		  flow:

Step 1

Install the appropriate release of Packaged CCE. For more information, see Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html

Step 2

Install the Cisco Identity Service (Cisco IdS). For more information, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html

For Packaged CCE deployments, the Cisco IdS is installed as a service on the Unified Intelligence Center VMs.

Step 3

Install and configure the Identity Provider (IdP).

Step 4

Configure System Inventory.

Step 5

Configure the Cisco IdS.

Step 6

Register and test SSO-compatible components with the Cisco IdS.

Step 7

Choose the SSO mode.

Step 8

Enable multiple users at once for SSO by using the SSO migration tool, or enable users one at time by using the configuration
                                       tools.

## Configure an
                        	 Identity Provider (IdP)

To support SSO for
                           		the contact center solution, configure an Identity Provider (IdP) that is
                           		compliant with the Security Assertion Markup Language 2.0 (SAML v2) Oasis
                           		standard. The IdP stores user profiles and provides authentication services to
                           		the contact center solution.

For a current list of supported Identity Provider products and versions, see the Contact Center Enterprise Compatibility Matrix .

This section
                           		provides sample configuration information for Microsoft AD FS.

Follow this sequence
                           		of tasks to configure the Identity Provider.

Sequence

Task

1

Install and Configure Active Directory Federation Services

2

Set Authentication Type. See Authentication Types .

3

4

Enable Signed SAML Assertions

5

Optionally Customize the AD FS Sign-In Page in Windows Server to Allow User ID

### Install and
                           	 Configure Active Directory Federation Services

Follow Microsoft instructions and guidelines to install Microsoft Active Directory Federation Services (AD FS).

For example, see Active
                                 		  Directory Federation Services Overview at https://technet.microsoft.com/en-us/library/hh831502(v=ws.11).aspx

Cisco IdS does not support AD FS Automatic Certificate Rollover. If the AD FS certificate gets rolled over, then re-establish
                                          the trust relationship between the IdS and AD FS.

The Secure Hash Algorithm (SHA) used for signature verification between:

IdP and Cisco IdS: SHA-1, SHA-256

Cisco IdS and the application browsers: SHA-256

#### Configure SAML Certificate Secure Hash Algorithm from SHA-1 to SHA-256

This procedure is useful for upgrades from version 11.x where the only Secure Hash Algorithm supported was SHA-1.

.

Perform this procedure after the upgrade has completed successfully.

Step 1

From browser in AD FS Server, login to Cisco IdS admin interface https://<Cisco IdS server address>:8553/idsadmin .

Step 2

Click Settings .

Step 3

Click Security tab.

Step 4

Click Keys and Certificates .

After this step, Single Sign On will stop working until you complete Step 8.

Step 5

Regenerate SAML Certificate with SHA-256 Secure Hash Algorithm. In the SAML Certificate section, change Secure Hash algorithm
                                             dropdown menu to SHA-256 and then click Regenerate button

Step 6

Download new metadata file. Click on IdS Trust tab and then click download button.

Step 7

Change Secure Hash Algorithm in AD FS Relaying Party Trust configuration. In AD FS server, open AD FS Management. Go to ADFS -> Trust Relationships -> Relying Party Trusts , right click on existing Relying Party Trust for Cisco IdS and then click on Properties. In the Advanced Tab, change the
                                             Secure Hash Algorithm to SHA-256. Click Apply .

Step 8

Update Relying party trust on AD FS. From AD FS Server, run the following Powershell command:

```
Update-AdfsRelyingPartyTrust -MetadataFile <path to Step 6 new MetaData File> -TargetName
        <Relying Party Trust Display Name>
```

#### Authentication
                              	 Types

Cisco Identity Service supports form-based authentication and Kerberos windows authentication of the Identity Provider.

For information on enabling form-based authentication in ADFS, see Microsoft documentation:

For ADFS 3.0 see https://blogs.msdn.microsoft.com/josrod/2014/10/15/enabled-forms-based-authentication-in-adfs-3-0/

For Kerberos authentication to work, ensure to disable the form-based authentication.

#### Integrate Cisco
                              	 IdS to the Shared Management AD FS

Step 1

In AD FS, be
                                             			 sure that the default Authentication Type is set to Forms. (Cisco Identity
                                             			 Service requires the Identity Provider to provide form-based authentication.)
                                             			 See the Microsoft AD FS documentation for details.

Step 2

In AD FS
                                             			 server, open AD
                                                				FS Management .

Step 3

Right-click AD
                                                				FS -> Trust Relationships -> Relying Party Trust .

Step 4

From the
                                             			 menu, choose Add
                                                				Relying Party Trust to launch the Add
                                                				Relying Party Trust Wizard .

Step 5

In the Select Data Source step, choose the option Import data about the relying party from a file .

Step 6

Browse to the sp.xml file that you downloaded from Cisco Identity
                                             			 Server and complete the import to establish the relying party trust.

Step 7

Select the
                                             			 step Specify Display Name , and add a significant name you
                                             			 can use to identify the Relying Party Trust.

Step 8

For AD FS in Windows Server, select the option I do not want to configure multi-factor authentication settings for the relying party at this time in the Step Configure Multi-factor Authentication Now .

Step 9

In the Step
                                             			 Choose Issuance Authorization Rules, select the option Permit all users to access this relying party and
                                             			 click Next .

Step 10

Click Next again to finish adding the relying party.

Step 11

Right-click
                                             			 on the Relying Party Trust and click Properties . Select the Identifiers tab.

Step 12

On the Identifiers tab, configure the following:

Description

Display name

The unique name of the identifier.

Relying party identifier

FQDN of the publisher node of Cisco Identity Server from which you downloaded the Cisco IdS metadata file.

FQDN of the subscriber node of Cisco Identity Server.

Step 13

Still in Properties , select the Advanced tab.

Step 14

Select secure hash algorithm as SHA-1 and then click OK .

A
                                                                  						claim rule with the following custom claims, as AttributeStatements, in the
                                                                  						assertion:

uid - Identifies the authenticated user in the claim
                                                                        							 sent to the applications.

user_principal - Identifies the authentication realm
                                                                        							 of the user in the assertion sent to Cisco Identity Service.

A
                                                                  						second claim rule that is a NameID custom claim rule specifying the fully
                                                                  						qualified domain name of the AD FS server and the Cisco IdS server.

Follow the
                                                				steps to configure these rules.

Step 15

In Relying Party Trusts , right-click on the Relying
                                             			 Party Trust you created, and click Edit
                                                				Claim Rules .

Step 16

Follow these
                                             			 steps to add a rule with Send
                                                				LDAP Attributes as Claims as the Claim rule template.

In the Issuance Transform Rules tab, click Add Rule .

In the
                                                   				  Step Choose Rule Type , select the claim rule template Send LDAP Attributes as Claims and click Next .

In the Configure Claim Rule step, in the Claim rule name field, enter NameID .

Set the Attribute store drop-down to Active Directory .

Set the
                                                   				  table Mapping of LDAP attributes to outgoing claim types to the appropriate LDAP Attributes and the corresponding Outgoing Claim Type for the type of user identifier
                                                   				  you are using:

When
                                                            						  the identifier is stored as a SAM-Account-Name attribute:

Select an LDAP Attribute of SAM-Account-Name , and set the corresponding Outgoing Claim Type to uid (lowercase).

Select a second LDAP Attribute of User-Principal-Name and set the corresponding Outgoing Claim Type to user_principal (lowercase).

When
                                                            						  the identifier is a UPN:

Select an LDAP Attribute of User-Principal-Name , and set the corresponding Outgoing Claim Type to uid (lowercase).

Select a second LDAP Attribute of User-Principal-Name and set the corresponding Outgoing Claim Type to user_principal (lowercase).

The
                                                                  						SAM-Account-Name or UPN choice is based on the User ID configured in the AW.

Step 17

Follow
                                             			 these steps to add a second rule with the template custom claim
                                                				rule .

Select Add Rule on the Edit Claim Rules window.

Select Send Claims Using Custom Rule .

Set the
                                                   				  name of rule to the fully qualified domain name (FQDN) of the Cisco
                                                   				  Identity Server publisher (primary) node.

Add the
                                                   				  following rule text:

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"] =>
 issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier",
 Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType,
 Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] =
 "urn:oasis:names:tc:SAML:2.0:nameid-format:transient",
 Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/namequalifier"] =
 "http:// <AD FS Server FQDN> /adfs/services/trust",
 Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/spnamequalifier"] =
 " <fully qualified domain name of Cisco IdS> ");
```

Edit the
                                                   				  script as follows:

Replace <ADFS Server FQDN> to match exactly (including
                                                            						  case) the ADFS server FQDN (fully qualified domain name.)

Replace <Cisco IdS server FQDN> to match exactly
                                                            						  (including case) the Cisco Identity Server FQDN.

Step 18

Click OK .

#### Enable Signed SAML
                              	 Assertions

Enable Signed SAML Assertions for the Relying Party Trust (Cisco
                                    		  Identity Service).

Step 1

Click Start and type powershell in the Search field to display the Windows Powershell icon.

Step 2

Right-click on the Windows Powershell program icon and select Run as administrator

All PowerShell commands in this procedure must be run in Administrator mode.

Step 3

Run the command, Set-ADFSRelyingPartyTrust -TargetName <Relying Party Trust Display Name> -SamlResponseSignature "MessageAndAssertion" .

Set <Relying Party Trust Display Name> to exactly match (including case) the Identifier tab of the Relying Party Trust properties.

For example:

Step 4

Navigate back to the Cisco Identity Service Management window.

Step 5

Click Settings .

Step 6

On the Download SAML SP Metadata and Upload IdP Metadata windows, click Next as you have already established trust relationship
                                             between IdP and IdS.

Step 7

On the AD FS authentication window, provide the login credentials.

Step 8

On successful SSO setup, the message "SSO Configuration is tested successfully" is displayed.

If you receive the error message "An error occurred", ensure that the claim you created on the AD FS is enabled.

If you receive the error message "IdP configuration error: SAML processing failed", ensure that the rule has the correct names
                                                            for Ids and AD FS.

#### Optionally Customize the AD FS Sign-In Page in Windows Server to Allow User ID

By default, the sign-in page presented to SSO users by AD FS in Windows Server requires a username that is a UPN. Usually
                                    this is an email format, for example, user@cisco.com. If your contact center solution is in a single domain, you can modify
                                    the sign-in page to allow your users to provide a simple User ID that does not include a domain name as part of the user name.

There are several methods you can use to customize the AD FS sign-in page. Look in the Microsoft AD FS in Windows Server documentation
                                    for details and procedures to configure alternate login IDs and customize the AD FS sign-in pages.

The following procedure is an example of one solution.

Step 1

In the AD FS Relying Party Trust , change the NameID claim rule to map the chosen LDAP attribute to uid .

Step 2

Click the Windows Start control and type powershell in the Search field to display the Windows Powershell icon.

Step 3

Right-click on the Windows Powershell program icon and select Run as administrator

All PowerShell commands in this procedure must be run in Administrator mode.

Step 4

To allow sign-ins to AD FS using the sAMAccountName, run the following Powershell command:

Set-AdfsClaimsProviderTrust -TargetIdentifier "AD AUTHORITY" -AlternateLoginID sAMAccountName -LookupForests myDomain.com

In the LookupForests parameter, replace myDomain.com with the forest DNS that your users belong to.

Step 5

Run the following commands to export a theme:

mkdir C:\themeExport-AdfsWebTheme –Name default –DirectoryPath c:\theme

Step 6

Edit onload.js in C:\theme\script and add the following code at the bottom of the file. This code changes the theme so that the AD FS sign-in page does not
                                             require a domain name or an ampersand, "@", in the username.

```
// Update the placeholder text to not include the domain
var userNameInput = document.getElementById("userNameInput");
if (userNameInput) {
 userNameInput.setAttribute("placeholder", "Username");
}
```

```
// Override submitLoginRequest to not have the "@" check
Login.submitLoginRequest = function () {
 var u = new InputUtil();
 var e = new LoginErrors();
 var userName = document.getElementById(Login.userNameInput);
 var password = document.getElementById(Login.passwordInput);
 if (!userName.value) {
  u.setError(userName, e.userNameFormatError);
  return false;
 }
 if (!password.value) {
  u.setError(password, e.passwordEmpty);
  return false;
 }
 document.forms['loginForm'].submit();
 return false;
};
```

Step 7

In Windows PowerShell, run the following commands to update the theme and make it active:

Set-AdfsWebTheme -TargetName custom -AdditionalFileResource @{Uri=’/adfs/portal/script/onload.js’;path="c:\theme\script\onload.js"}

Set-AdfsWebConfig -ActiveThemeName custom

## Set the Principal AW for Single Sign On

This procedure is applicable only for Packaged CCE 4K or 12K agent reference design.

During deployment, the first SideA AW machine in the CSV file is the Principal AW.

The Principal AW (Admin Workstation) is responsible for managing background tasks that are run periodically to sync configuration
                                 with other solution components, such as SSO management, Smart Licensing, etc.

After deployment, you can change the Principal AW by selecting a different AW on the Inventory page. Set the AW on which you
                              make most of your configuration changes as the Principal AW.

Step 1

In Unified CCE Administration, choose Inventory to open the Inventory page.

Step 2

Set the Principal AW:

Click the AW that you want to be the Principal AW.

You can only specify one Principal AW for each Unified CCE system.

Check the PrincipalAW check box.

Enter the Unified CCE Diagnostic Framework Service domain, username, and password.

The credential must be of a domain user who is a member of the local administrator group if the ADSecurityGroupUpdate registry key in AW is zero. If the ADSecurityGroupUpdate registry key is set to 1, then the user must be available in the Config security group under the instance OU. These credentials
                                                must be valid on all CCE components in your deployment (routers, PGs, AWs, and so on).

Every time the Active Directory credentials are updated, the credentials configured here must be updated as well.

Click Save .

## Set Up the External HDS for Single Sign-On

If you have an external HDS in 2000 Agent deployments, manually associate it with a default Cisco IdS by performing the following
                              instructions.

Step 1

In Unified CCE Administration , click Infrastructure > Inventory to open the Inventory page.

Step 2

Click the pencil icon for the External HDS to open the edit machine popup window.

Step 3

Click the Search icon next to Default Identity Service .

Step 4

Enter the machine name for the Cisco IdS in the Search field or choose the Cisco IdS from the list.

Step 5

Click Save .

## Configure the Cisco Identity Service

The Cisco Identity Service (Cisco IdS) provides authorization between the Identity Provider (IdP) and applications.

When you configure the Cisco IdS, you set up a metadata exchange between the Cisco IdS and the IdP. This exchange establishes
                              a trust relationship that then allows applications to use the Cisco IdS for single sign-on. You establish the trust relationship
                              by downloading a metadata file from the Cisco IdS and uploading it to the IdP. You can then select settings that are related
                              to security, identify clients of the Cisco IdS service, and set log levels. If desired, enable Syslog format.

In Packaged CCE 4000 or 12000 Agent deployments:

Unified CCE AW, Unified Intelligence Center, Finesse, and external HDS gets automatically associated with a default Cisco
                                                Identity Service (Cisco IdS).

Make sure that the Principal AW is configured, and is functional before using the Single Sign-On tool in the Unified CCE Administration.
                                                Also, add the SSO-capable machines to the Inventory.

In Packaged CCE 2000 Agent deployments, you must manually associate an external HDS with a default Cisco Identity Service
                                          (Cisco IdS). For more information, see Set Up the External HDS for Single Sign-On .

Step 1

In the Unified CCE Administration, choose Overview > Infrastructure Settings > Device Configuration > Identity Service .

Use a log in name in the format username@FQDN to log in to the Unified CCE Administration.

Step 2

Click Identity Service Nodes .

Step 3

Click Identity Service Settings .

Step 4

Click Security .

Step 5

Click Tokens .

Refresh Token Expiry -- Refresh token is used to get new Access tokens. This parameter specifies the duration after which the Refresh token expires.
                                                The default value is 10 hours. The minimum value is 2 hours. The maximum is 24 hours.

Authorization Code Expiry -- Authorization code is used to get Access tokens from Cisco IdS. This parameter specifies the duration after which the
                                                Authorization code expires. The default value is 1 minute, which is also the minimum. The maximum is 10 minutes.

Access Token Expiry -- Access token contains security credentials used to authorize clients for accessing resource server. This parameter specifies
                                                the duration after which the Access token expires. The default value is 60 minutes. The minimum value is 5 minutes. The maximum
                                                is 120 minutes.

Step 6

Set the Encrypt Token (optional); the default setting is On . Use this configuration to secure the tokens as Cisco IdS issues tokens in both plain text or encrypted formats.

Step 7

Click Save .

Step 8

Click Keys and Certificates .

Regenerate the Encryption/Signature key by clicking Regenerate . A message appears to say that the Token Registration is successful and advises you to restart the system to complete the
                                                configuration. An Administrator regenerates the Encryption/Signature key when it is exposed or compromised.

Regenerate the SAML Certificate by clicking Regenerate . A message appears to say that the SAML certificate regeneration is successful. SAML certificate is regenerated when it expires
                                                or when IdS relying party trust configuration on IdP is deleted.

Establish the trust relationship again whenever the Encryption keys or SAML certificates are regenerated.

Step 9

Click Save .

Step 10

Click Identity Service Clients .

Step 11

To add a client on the Identity Service Clients tab:

Click New .

Enter the name of client.

Enter the Redirect URL. To add more than one URL, click the plus icon.

Click Add (or click Clear and then click the X to close the page without adding the client).

Step 12

To edit or delete a client, highlight the client row and click the ellipses under Actions . Then:

Click Edit to edit the client's name, ID, or redirect URL. On the Edit Client page, make changes and click Save (or click Clear and then click the X to close the page without saving edits).

Click Delete to delete the client.

Step 13

Click Identity Service Settings .

Step 14

Click Troubleshooting to perform some optional troubleshooting.

Step 15

From the Log Level drop-down list, set the local log level by choosing Error , Warning , Info (the default), Debug , or Trace .

Step 16

To receive errors in Syslog format, enter the name of the Remote Syslog Server in the Host (Optional) field.

Step 17

Click Save .

Register components with the Cisco IdS.

Enable (or disable) SSO for the entire deployment.

If SSO is enabled in the deployment, then import all the IdS server nodes certificate into Cisco Finesse, CUIC, and LiveData
                                             component trust store.

## Register Components and Set Single Sign-On Mode

If you add any SSO-compatible machines to the System Inventory after you 
                              register components with the Cisco IdS, those machines are registered automatically.

### Before you begin

Configure the Cisco Identity Service (Cisco IdS).

Disable popup blockers. It enables viewing all test results correctly.

If you are using Internet Explorer, verify that:

It is not in the Compatibility Mode.

You are using the fully qualified domain name of AW to access the CCE Administration (for example, https://<FQDN>/cceadmin ).

Step 1

In the Unified CCE Administration, navigate to Features > Single Sign-On Overview > Infrastructure Settings > Device Configuration > Identity Service .

Step 2

Click the Register button to register all SSO-compatible components with the Cisco IdS.

The component status table displays the registration status of each component.

If a component fails to register, correct the error and click Retry .

Step 3

Click the Test button. When the new browser tab opens, you may be prompted to accept a certificate. In order for the page to load, accept
                                       any certificates. Then, when presented with a log in dialog, log in as a user with SSO credentials.

The test process verifies that each component has been configured correctly to reach the Identity Provider, and that the Cisco
                                          IdS successfully generates access tokens. Each component that you are setting up for SSO is tested.

The component status table displays the status of testing each component.

If a test is unsuccessful, correct the error, and then click Test again.

Test results are not saved. If you refresh the page, run the test again before enabling SSO.

Step 4

Select the SSO mode  for the system from the Set Mode drop-down menu:

Non-SSO: This mode disables SSO for all agents and supervisors. Users log in using existing Active Directory-based local authentication.

Hybrid: This mode allows you to enable agents and supervisors selectively for SSO.

SSO: This mode enables SSO for all agents and supervisors.

The component status table displays the status of setting the SSO mode on  each component.

If the SSO mode fails to be set on a component, correct the error,  and then select the mode again.

## Single Sign-On and the Agent Tool

When the global SSO-enabled setting is Hybrid, you can use the Unified CCE Administration Agent Tool to enable  agents individually
                           for single sign-on.

In the tool, check the Single Sign-On check box to require a selected  agent to sign in with SSO authentication. For supervisors and for agents with single sign-on
                           (SSO) enabled, the username is the user's Active Directory or SSO account username.

The check box is disabled when the global SSO mode is set to SSO or non-SSO.

To update agent records in bulk, use the Bulk Jobs Agent content file.

## Migration Considerations Before Enabling Single Sign-On

### Administrator User and Single Sign-On in Unified Intelligence Center

During installation, Cisco Unified Intelligence Center creates an administrator user. This user is not enabled for SSO, as
                              the user is known only to Unified Intelligence Center.

When you enable SSO, this administrator user is no longer able to log in to the Unified Intelligence Center and perform administrative
                              tasks. These tasks include configuring datasources and setting permissions for other users, for example. To avoid this situation,
                              perform the following steps before enabling SSO.

Create a new SSO user who has the same roles and permissions as those of the administrator user.

Log in to the CLI.

utils cuic user make-admin username

in which the user name is the complete name of the new user, including the authenticator prefix as shown on the Unified Intelligence
                              Center User List page.

The command, when performed, provides all the roles to the new user and copies all permissions from the administrator user
                              to this new user.

The administrator's group memberships are not copied to the new user by this CLI command and must be manually updated. The
                                                new user, now a Security Administrator, can set up the group memberships.

For any entity (for example, reports or report definitions), if this new user’s permissions provide higher privileges than
                                                the administrator, the privileges are left intact. The privileges are not overwritten by this CLI command.

### Browser Settings and Single Sign-On

If you have enabled single sign-on and are using Internet Explorer, Chrome, Edge Chromium (Microsoft Edge), or Firefox, verify that the browser options are set as shown in the following table. These settings specify that you do not
                              want a new session of the browser to reopen tabs from a previous session. No changes are required for Internet Explorer.

Browser

Browser options to verify when using SSO

Internet Explorer

Open Internet Explorer.

Click the Tools (Alt+X) icon, and then click Internet options .

In the General tab, click Tabs .

From the When a new tab is opened, open: drop-down list, verify that the Your first home page option is selected.

Chrome

Open Chrome.

Click the Customize and control Google Chrome icon.

Click Settings .

In the On startup section of the Settings page, verify that the Open the New Tab page option is selected.

Edge Chromium (Microsoft Edge)

Open Microsoft Edge.

Click the Settings and more (Alt+F) (...) icon.

Click Settings .

On the Settings page, click On startup , and verify that the Open a new tab radio button is selected.

Firefox

Open Firefox.

Click the Open menu icon.

Click Options .

In the Startup section of the General page, verify that either the home page or a blank page is chosen in the When Firefox starts drop-down list.

## Migrate Agents and
                        	 Supervisors to Single Sign-On Accounts

If you are enabling SSO in an existing deployment, you can set the SSO
                              		  state to hybrid to support a mix of SSO and non-SSO users. In hybrid mode, you
                              		  can enable agents and supervisors selectively for SSO making it possible for
                              		  you to transition your system to SSO in phases.

Use the procedures in this section to migrate groups of agents and
                              		  supervisors to SSO accounts using the SSO Migration content file in the Unified
                              		  CCE Administration Bulk Jobs tool. You use the Administration Bulk Jobs tool to
                              		  download a content file containing records for agents and supervisors who have
                              		  not migrated to SSO accounts. You modify the content file locally to specify
                              		  SSO usernames for the existing agents and supervisors. Using the Administration
                              		  Bulk Jobs tool again, you upload the content file to update the agents and
                              		  supervisors usernames; the users are also automatically enabled for SSO.

If you do not want to migrate a user, delete the row for that user.

Important

While the Finesse agent is logged in, changing the login name
                                          			 prevents the agent from answering or placing calls. In this situation, the
                                          			 agent can still change between ready and not_ready state. This affects all active agents,
                                          			 independent of whether SSO is enabled or disabled. Should you need to modify a
                                          			 login name, do so only after the corresponding agent is logged out. Note too
                                          			 that SSO migration (moving a non-SSO agent to be SSO-enabled, by either hybrid
                                          			 mode or global SSO mode) should not be done when the agent is logged in.

Step 1

In Unified CCE Administration, navigate to Overview > Bulk Import .

Step 2

Download the SSO Migration bulk job content file.

Click Templates.

The Download Templates popup window opens.

Click the Download icon for the SSO Migration
                                             				  template.

Click OK to close the Download Templates popup window.

Step 3

Enter the SSO usernames in the SSO Migration content file.

Open the template in Microsoft Excel. Update the newUserName field for the agents and
                                             				  supervisors whom you want to migrate to SSO accounts.

The content file for the SSO migration bulk job contains these
                                                					 fields:

Field

Required?

Description

userName

Yes

The user's non-SSO username.

firstName

No

The user's first name.

lastName

No

The user's last name.

newUserName

No

The user's new SSO username. Enter up to 255 ASCII
                                                            								  characters.

If you want to enable a user for SSO, but keep the
                                                            								  current username, leave newUserName blank, or copy the value of userName into newUserName .

Save the populated file locally.

Step 4

Create a bulk job to update the usernames in the database.

Click New to open the New Bulk Job window.

Enter an optional Description for the job.

In the Content File field, browse to the SSO
                                             				  Migration content file you completed.

The content file is validated before the bulk job is created.

Click Save .

The new bulk job appears in the list of bulk jobs. Optionally,
                                                					 click the bulk job to review the details and status for the bulk job. You can
                                                					 also download the log file for a bulk job.

When the bulk
                                                					 job completes, the agents and supervisors are enabled for SSO and their
                                                					 usernames are updated. You can open an individual user's record in the Agent
                                                					 tool in Unified CCE Administration to see the changes.

### What to do next

After all of the agents and supervisors in your deployment are
                              		  migrated to SSO accounts, you can enable SSO globally in your deployment.

## Globally Disable Single Sign-On

Important

You must assign new passwords for agents (using the Unified CCE Administration Agent tool) when you disable the agents for SSO.

If you change a Cisco Unified Intelligence Center supervisor who was created as SSO-enabled to non-SSO, a new, non-SSO user
                                                      account is created for the supervisor after the next user synchronization. The older, SSO-enabled supervisor account (in the
                                                      format SSO\<loginname>) still exists in Cisco Unified Intelligence Center, however, and you must delete it. You must reconfigure
                                                      the new, non-SSO supervisor user account (that matches the supervisor's SAM account name in Active Directory) in Cisco Unified
                                                      Intelligence Center Administration Console to set up the supervisor's reports and permissions.

Step 1

If the system is in SSO mode, change the SSO mode to Hybrid in the Unified CCE Administration Single Sign-On tool.

Step 2

Disable agents for SSO, and assign the agents new passwords.  This step allows the agents to sign into Finesse.

In Unified CCE Administration, you can update individual agent records using the Agent tool, or update records in bulk using the Bulk Jobs
                                          Agent content file.

Step 3

Disable supervisors for SSO. This step allows the supervisors to sign in to Unified CCE Administration to reskill agents.

In Unified CCE Administration, you can update individual supervisor records using the Agent tool, or update records in bulk using the Bulk
                                          Jobs Agent content file.

Step 4

After you have updated all of the agent and supervisor records, change the SSO mode to Non-SSO .

## Related
                        	 Documentation

Refer to the
                              		  following documents and other resources for more details about single sign-on.

See this
                                          						information

Located
                                          						here

For
                                          						these details

Solution Design Guide for Cisco Packaged Contact Center Enterprise

Design
                                          						considerations and guidelines for deploying the Cisco Packaged CCE system.

Virtualization for Cisco Packaged CCE

Information about deploying Packaged CCE (including single
                                          						sign-on) on VMware.

Release Notes for Cisco Packaged Contact Center Enterprise Solution

New
                                          						features and changes for this release of the Packaged CCE solution.

Contact Center Enterprise Compatibility Matrix

Packaged
                                          						CCE requirements.

Unified
                                          						CCE Administration Single Sign-On Tool

Online
                                          						help

Changes
                                          						to support single sign-on.

System
                                          						Inventory Tool

This
                                          						guide.

Information related to adding SSO-compatible components to the
                                          						inventory.

| Note | Before enabling SSO in Packaged CCE, ensure to sign in to the Cisco Unified Intelligence Center OAMP interface and perform the Unified CCE User Integration
                                          operation (Cluster Configuration > UCCE User Integration) once manually to import the Supervisors with the required roles. This is only applicable for Unified CCE deployment. |
|---|---|

| Reference Design | Packaged
                                             						CCE Solution |
|---|---|
| 2000 Agent | Cisco IdS is coresident with Unified Intelligence Center and Live Data on a single VM. |
| 4000 Agent | Standalone Cisco IdS VM |
| 12000 Agent | Standalone Cisco IdS VM |

| Operation | Allowed on Publisher | Allowed on Subscriber |
|---|---|---|
| Upload IdP metadata | Always | Never |
| Download SAML SP metadata | Always | Never |
| Regenerate SAML Certificate | Always | Never |
| Regenerate Token Encryption/Signing Key | Always | Never |
| Update AuthCode/Token Expiry | Always | Only when publisher is connected |
| Enable/Disable Token Encryption | Always | Only when publisher is connected |
| Add/Update/Delete Cisco IdS client configuration | Always | Only when publisher is connected |
| View Cisco IdS client configuration | Always | Always |
| View Cisco IdS status | Always | Always |
| Set Troubleshooting Log Level | Always | Always |
| Set Remote Syslog server | Always | Always |

| Note | Users enabled for single sign-on are at risk of having their accounts misused by others if the browser is not closed completely.
                                          If the browser is left open, a different user can access the application from the browser page without entering credentials. |
|---|---|

| Step 1 | Install the appropriate release of Packaged CCE. For more information, see Cisco Packaged Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-installation-guides-list.html |
|---|---|
| Step 2 | Install the Cisco Identity Service (Cisco IdS). For more information, see Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html For Packaged CCE deployments, the Cisco IdS is installed as a service on the Unified Intelligence Center VMs. |
| Step 3 | Install and configure the Identity Provider (IdP). |
| Step 4 | Configure System Inventory. |
| Step 5 | Configure the Cisco IdS. |
| Step 6 | Register and test SSO-compatible components with the Cisco IdS. |
| Step 7 | Choose the SSO mode. |
| Step 8 | Enable multiple users at once for SSO by using the SSO migration tool, or enable users one at time by using the configuration
                                       tools. |

| Note | For a current list of supported Identity Provider products and versions, see the Contact Center Enterprise Compatibility Matrix . |
|---|---|

| Sequence | Task |
|---|---|
| 1 | Install and Configure Active Directory Federation Services |
| 2 | Set Authentication Type. See Authentication Types . |
| 3 | Configure an Identity Provider (IdP) |
| 4 | Enable Signed SAML Assertions |
| 5 | Optionally Customize the AD FS Sign-In Page in Windows Server to Allow User ID |

| Note | Cisco IdS does not support AD FS Automatic Certificate Rollover. If the AD FS certificate gets rolled over, then re-establish
                                          the trust relationship between the IdS and AD FS. |
|---|---|

| Note | The Secure Hash Algorithm (SHA) used for signature verification between: IdP and Cisco IdS: SHA-1, SHA-256 Cisco IdS and the application browsers: SHA-256 |
|---|---|

| Step 1 | From browser in AD FS Server, login to Cisco IdS admin interface https://<Cisco IdS server address>:8553/idsadmin . |
|---|---|
| Step 2 | Click Settings . |
| Step 3 | Click Security tab. |
| Step 4 | Click Keys and Certificates . Note After this step, Single Sign On will stop working until you complete Step 8. | Note | After this step, Single Sign On will stop working until you complete Step 8. |
| Note | After this step, Single Sign On will stop working until you complete Step 8. |
| Step 5 | Regenerate SAML Certificate with SHA-256 Secure Hash Algorithm. In the SAML Certificate section, change Secure Hash algorithm
                                             dropdown menu to SHA-256 and then click Regenerate button |
| Step 6 | Download new metadata file. Click on IdS Trust tab and then click download button. |
| Step 7 | Change Secure Hash Algorithm in AD FS Relaying Party Trust configuration. In AD FS server, open AD FS Management. Go to ADFS -> Trust Relationships -> Relying Party Trusts , right click on existing Relying Party Trust for Cisco IdS and then click on Properties. In the Advanced Tab, change the
                                             Secure Hash Algorithm to SHA-256. Click Apply . |
| Step 8 | Update Relying party trust on AD FS. From AD FS Server, run the following Powershell command: Update-AdfsRelyingPartyTrust -MetadataFile <path to Step 6 new MetaData File> -TargetName
        <Relying Party Trust Display Name> |

| Note | After this step, Single Sign On will stop working until you complete Step 8. |
|---|---|

| Step 1 | In AD FS, be
                                             			 sure that the default Authentication Type is set to Forms. (Cisco Identity
                                             			 Service requires the Identity Provider to provide form-based authentication.)
                                             			 See the Microsoft AD FS documentation for details. |
|---|---|
| Step 2 | In AD FS
                                             			 server, open AD
                                                				FS Management . |
| Step 3 | Right-click AD
                                                				FS -> Trust Relationships -> Relying Party Trust . |
| Step 4 | From the
                                             			 menu, choose Add
                                                				Relying Party Trust to launch the Add
                                                				Relying Party Trust Wizard . |
| Step 5 | In the Select Data Source step, choose the option Import data about the relying party from a file . |
| Step 6 | Browse to the sp.xml file that you downloaded from Cisco Identity
                                             			 Server and complete the import to establish the relying party trust. |
| Step 7 | Select the
                                             			 step Specify Display Name , and add a significant name you
                                             			 can use to identify the Relying Party Trust. |
| Step 8 | For AD FS in Windows Server, select the option I do not want to configure multi-factor authentication settings for the relying party at this time in the Step Configure Multi-factor Authentication Now . |
| Step 9 | In the Step
                                             			 Choose Issuance Authorization Rules, select the option Permit all users to access this relying party and
                                             			 click Next . |
| Step 10 | Click Next again to finish adding the relying party. |
| Step 11 | Right-click
                                             			 on the Relying Party Trust and click Properties . Select the Identifiers tab. |
| Step 12 | On the Identifiers tab, configure the following: Field Description Display name The unique name of the identifier. Relying party identifier FQDN of the publisher node of Cisco Identity Server from which you downloaded the Cisco IdS metadata file. FQDN of the subscriber node of Cisco Identity Server. | Field | Description | Display name | The unique name of the identifier. | Relying party identifier | FQDN of the publisher node of Cisco Identity Server from which you downloaded the Cisco IdS metadata file. | FQDN of the subscriber node of Cisco Identity Server. |
| Field | Description |
| Display name | The unique name of the identifier. |
| Relying party identifier | FQDN of the publisher node of Cisco Identity Server from which you downloaded the Cisco IdS metadata file. |
| FQDN of the subscriber node of Cisco Identity Server. |
| Step 13 | Still in Properties , select the Advanced tab. |
| Step 14 | Select secure hash algorithm as SHA-1 and then click OK . Note In the
                                                         				following steps, you configure two claim rules to specify the claims that are
                                                         				sent from AD FS to Cisco Identity Service as part of a successful SAML
                                                         				assertion: A
                                                                  						claim rule with the following custom claims, as AttributeStatements, in the
                                                                  						assertion: uid - Identifies the authenticated user in the claim
                                                                        							 sent to the applications. user_principal - Identifies the authentication realm
                                                                        							 of the user in the assertion sent to Cisco Identity Service. A
                                                                  						second claim rule that is a NameID custom claim rule specifying the fully
                                                                  						qualified domain name of the AD FS server and the Cisco IdS server. Follow the
                                                				steps to configure these rules. | Note | In the
                                                         				following steps, you configure two claim rules to specify the claims that are
                                                         				sent from AD FS to Cisco Identity Service as part of a successful SAML
                                                         				assertion: A
                                                                  						claim rule with the following custom claims, as AttributeStatements, in the
                                                                  						assertion: uid - Identifies the authenticated user in the claim
                                                                        							 sent to the applications. user_principal - Identifies the authentication realm
                                                                        							 of the user in the assertion sent to Cisco Identity Service. A
                                                                  						second claim rule that is a NameID custom claim rule specifying the fully
                                                                  						qualified domain name of the AD FS server and the Cisco IdS server. |
| Note | In the
                                                         				following steps, you configure two claim rules to specify the claims that are
                                                         				sent from AD FS to Cisco Identity Service as part of a successful SAML
                                                         				assertion: A
                                                                  						claim rule with the following custom claims, as AttributeStatements, in the
                                                                  						assertion: uid - Identifies the authenticated user in the claim
                                                                        							 sent to the applications. user_principal - Identifies the authentication realm
                                                                        							 of the user in the assertion sent to Cisco Identity Service. A
                                                                  						second claim rule that is a NameID custom claim rule specifying the fully
                                                                  						qualified domain name of the AD FS server and the Cisco IdS server. |
| Step 15 | In Relying Party Trusts , right-click on the Relying
                                             			 Party Trust you created, and click Edit
                                                				Claim Rules . |
| Step 16 | Follow these
                                             			 steps to add a rule with Send
                                                				LDAP Attributes as Claims as the Claim rule template. In the Issuance Transform Rules tab, click Add Rule . In the
                                                   				  Step Choose Rule Type , select the claim rule template Send LDAP Attributes as Claims and click Next . In the Configure Claim Rule step, in the Claim rule name field, enter NameID . Set the Attribute store drop-down to Active Directory . Set the
                                                   				  table Mapping of LDAP attributes to outgoing claim types to the appropriate LDAP Attributes and the corresponding Outgoing Claim Type for the type of user identifier
                                                   				  you are using: When
                                                            						  the identifier is stored as a SAM-Account-Name attribute: Select an LDAP Attribute of SAM-Account-Name , and set the corresponding Outgoing Claim Type to uid (lowercase). Select a second LDAP Attribute of User-Principal-Name and set the corresponding Outgoing Claim Type to user_principal (lowercase). When
                                                            						  the identifier is a UPN: Select an LDAP Attribute of User-Principal-Name , and set the corresponding Outgoing Claim Type to uid (lowercase). Select a second LDAP Attribute of User-Principal-Name and set the corresponding Outgoing Claim Type to user_principal (lowercase). Note The
                                                                  						SAM-Account-Name or UPN choice is based on the User ID configured in the AW. | Note | The
                                                                  						SAM-Account-Name or UPN choice is based on the User ID configured in the AW. |
| Note | The
                                                                  						SAM-Account-Name or UPN choice is based on the User ID configured in the AW. |
| Step 17 | Follow
                                             			 these steps to add a second rule with the template custom claim
                                                				rule . Select Add Rule on the Edit Claim Rules window. Select Send Claims Using Custom Rule . Set the
                                                   				  name of rule to the fully qualified domain name (FQDN) of the Cisco
                                                   				  Identity Server publisher (primary) node. Add the
                                                   				  following rule text: c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"] =>
 issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier",
 Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType,
 Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] =
 "urn:oasis:names:tc:SAML:2.0:nameid-format:transient",
 Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/namequalifier"] =
 "http:// <AD FS Server FQDN> /adfs/services/trust",
 Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/spnamequalifier"] =
 " <fully qualified domain name of Cisco IdS> "); Edit the
                                                   				  script as follows: Replace <ADFS Server FQDN> to match exactly (including
                                                            						  case) the ADFS server FQDN (fully qualified domain name.) Replace <Cisco IdS server FQDN> to match exactly
                                                            						  (including case) the Cisco Identity Server FQDN. |
| Step 18 | Click OK . |

| Field | Description |
|---|---|
| Display name | The unique name of the identifier. |
| Relying party identifier | FQDN of the publisher node of Cisco Identity Server from which you downloaded the Cisco IdS metadata file. |
| FQDN of the subscriber node of Cisco Identity Server. |

| Note | In the
                                                         				following steps, you configure two claim rules to specify the claims that are
                                                         				sent from AD FS to Cisco Identity Service as part of a successful SAML
                                                         				assertion: A
                                                                  						claim rule with the following custom claims, as AttributeStatements, in the
                                                                  						assertion: uid - Identifies the authenticated user in the claim
                                                                        							 sent to the applications. user_principal - Identifies the authentication realm
                                                                        							 of the user in the assertion sent to Cisco Identity Service. A
                                                                  						second claim rule that is a NameID custom claim rule specifying the fully
                                                                  						qualified domain name of the AD FS server and the Cisco IdS server. |
|---|---|

| Note | The
                                                                  						SAM-Account-Name or UPN choice is based on the User ID configured in the AW. |
|---|---|

| Step 1 | Click Start and type powershell in the Search field to display the Windows Powershell icon. |
|---|---|
| Step 2 | Right-click on the Windows Powershell program icon and select Run as administrator Note All PowerShell commands in this procedure must be run in Administrator mode. | Note | All PowerShell commands in this procedure must be run in Administrator mode. |
| Note | All PowerShell commands in this procedure must be run in Administrator mode. |
| Step 3 | Run the command, Set-ADFSRelyingPartyTrust -TargetName <Relying Party Trust Display Name> -SamlResponseSignature "MessageAndAssertion" . Note Set <Relying Party Trust Display Name> to exactly match (including case) the Identifier tab of the Relying Party Trust properties. For example: Set-ADFSRelyingPartyTrust -TargetName CUICPub.PCCERCDN.cisco.com -SamlResponseSignature "MessageAndAssertion". | Note | Set <Relying Party Trust Display Name> to exactly match (including case) the Identifier tab of the Relying Party Trust properties. |
| Note | Set <Relying Party Trust Display Name> to exactly match (including case) the Identifier tab of the Relying Party Trust properties. |
| Step 4 | Navigate back to the Cisco Identity Service Management window. |
| Step 5 | Click Settings . By default IdS Trust tab is displayed. |
| Step 6 | On the Download SAML SP Metadata and Upload IdP Metadata windows, click Next as you have already established trust relationship
                                             between IdP and IdS. |
| Step 7 | On the AD FS authentication window, provide the login credentials. |
| Step 8 | On successful SSO setup, the message "SSO Configuration is tested successfully" is displayed. Note If you receive the error message "An error occurred", ensure that the claim you created on the AD FS is enabled. If you receive the error message "IdP configuration error: SAML processing failed", ensure that the rule has the correct names
                                                            for Ids and AD FS. | Note | If you receive the error message "An error occurred", ensure that the claim you created on the AD FS is enabled. If you receive the error message "IdP configuration error: SAML processing failed", ensure that the rule has the correct names
                                                            for Ids and AD FS. |
| Note | If you receive the error message "An error occurred", ensure that the claim you created on the AD FS is enabled. If you receive the error message "IdP configuration error: SAML processing failed", ensure that the rule has the correct names
                                                            for Ids and AD FS. |

| Note | All PowerShell commands in this procedure must be run in Administrator mode. |
|---|---|

| Note | Set <Relying Party Trust Display Name> to exactly match (including case) the Identifier tab of the Relying Party Trust properties. |
|---|---|

| Note | If you receive the error message "An error occurred", ensure that the claim you created on the AD FS is enabled. If you receive the error message "IdP configuration error: SAML processing failed", ensure that the rule has the correct names
                                                            for Ids and AD FS. |
|---|---|

| Step 1 | In the AD FS Relying Party Trust , change the NameID claim rule to map the chosen LDAP attribute to uid . |
|---|---|
| Step 2 | Click the Windows Start control and type powershell in the Search field to display the Windows Powershell icon. |
| Step 3 | Right-click on the Windows Powershell program icon and select Run as administrator All PowerShell commands in this procedure must be run in Administrator mode. |
| Step 4 | To allow sign-ins to AD FS using the sAMAccountName, run the following Powershell command: Set-AdfsClaimsProviderTrust -TargetIdentifier "AD AUTHORITY" -AlternateLoginID sAMAccountName -LookupForests myDomain.com In the LookupForests parameter, replace myDomain.com with the forest DNS that your users belong to. |
| Step 5 | Run the following commands to export a theme: mkdir C:\themeExport-AdfsWebTheme –Name default –DirectoryPath c:\theme |
| Step 6 | Edit onload.js in C:\theme\script and add the following code at the bottom of the file. This code changes the theme so that the AD FS sign-in page does not
                                             require a domain name or an ampersand, "@", in the username. // Update the placeholder text to not include the domain
var userNameInput = document.getElementById("userNameInput");
if (userNameInput) {
 userNameInput.setAttribute("placeholder", "Username");
} // Override submitLoginRequest to not have the "@" check
Login.submitLoginRequest = function () {
 var u = new InputUtil();
 var e = new LoginErrors();
 var userName = document.getElementById(Login.userNameInput);
 var password = document.getElementById(Login.passwordInput);
 if (!userName.value) {
  u.setError(userName, e.userNameFormatError);
  return false;
 }
 if (!password.value) {
  u.setError(password, e.passwordEmpty);
  return false;
 }
 document.forms['loginForm'].submit();
 return false;
}; |
| Step 7 | In Windows PowerShell, run the following commands to update the theme and make it active: Set-AdfsWebTheme -TargetName custom -AdditionalFileResource @{Uri=’/adfs/portal/script/onload.js’;path="c:\theme\script\onload.js"} Set-AdfsWebConfig -ActiveThemeName custom |

| Note | This procedure is applicable only for Packaged CCE 4K or 12K agent reference design. |
|---|---|

| Step 1 | In Unified CCE Administration, choose Inventory to open the Inventory page. |
|---|---|
| Step 2 | Set the Principal AW: Click the AW that you want to be the Principal AW. Note You can only specify one Principal AW for each Unified CCE system. The Edit CCE AW window opens. Check the PrincipalAW check box. Enter the Unified CCE Diagnostic Framework Service domain, username, and password. The credential must be of a domain user who is a member of the local administrator group if the ADSecurityGroupUpdate registry key in AW is zero. If the ADSecurityGroupUpdate registry key is set to 1, then the user must be available in the Config security group under the instance OU. These credentials
                                                must be valid on all CCE components in your deployment (routers, PGs, AWs, and so on). Note Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. Click Save . | Note | You can only specify one Principal AW for each Unified CCE system. | Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
| Note | You can only specify one Principal AW for each Unified CCE system. |
| Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |

| Note | You can only specify one Principal AW for each Unified CCE system. |
|---|---|

| Note | Every time the Active Directory credentials are updated, the credentials configured here must be updated as well. |
|---|---|

| Step 1 | In Unified CCE Administration , click Infrastructure > Inventory to open the Inventory page. |
|---|---|
| Step 2 | Click the pencil icon for the External HDS to open the edit machine popup window. |
| Step 3 | Click the Search icon next to Default Identity Service . The Select Identity Service popup window opens. |
| Step 4 | Enter the machine name for the Cisco IdS in the Search field or choose the Cisco IdS from the list. |
| Step 5 | Click Save . |

| Note | In Packaged CCE 4000 or 12000 Agent deployments: Unified CCE AW, Unified Intelligence Center, Finesse, and external HDS gets automatically associated with a default Cisco
                                                Identity Service (Cisco IdS). Make sure that the Principal AW is configured, and is functional before using the Single Sign-On tool in the Unified CCE Administration.
                                                Also, add the SSO-capable machines to the Inventory. In Packaged CCE 2000 Agent deployments, you must manually associate an external HDS with a default Cisco Identity Service
                                          (Cisco IdS). For more information, see Set Up the External HDS for Single Sign-On . |
|---|---|

| Step 1 | In the Unified CCE Administration, choose Overview > Infrastructure Settings > Device Configuration > Identity Service . Note Use a log in name in the format username@FQDN to log in to the Unified CCE Administration. The Identity Service Nodes , Identity Service Settings , and Identity Service Clients tabs appear. | Note | Use a log in name in the format username@FQDN to log in to the Unified CCE Administration. |
|---|---|---|---|
| Note | Use a log in name in the format username@FQDN to log in to the Unified CCE Administration. |
| Step 2 | Click Identity Service Nodes . You can view the overall Node level and identify which nodes are in service. You can also view the SAML Certificate Expiry details for each node, indicating when the certificate is due to expire. The node Status options are Not Configured , In Service , Partial Service , and Out of Service . Click a status to see more information. The star to the right of one of the Node names identifies the node that is the primary
                                       publisher. |
| Step 3 | Click Identity Service Settings . |
| Step 4 | Click Security . |
| Step 5 | Click Tokens . Enter the duration for the following settings: Refresh Token Expiry -- Refresh token is used to get new Access tokens. This parameter specifies the duration after which the Refresh token expires.
                                                The default value is 10 hours. The minimum value is 2 hours. The maximum is 24 hours. Authorization Code Expiry -- Authorization code is used to get Access tokens from Cisco IdS. This parameter specifies the duration after which the
                                                Authorization code expires. The default value is 1 minute, which is also the minimum. The maximum is 10 minutes. Access Token Expiry -- Access token contains security credentials used to authorize clients for accessing resource server. This parameter specifies
                                                the duration after which the Access token expires. The default value is 60 minutes. The minimum value is 5 minutes. The maximum
                                                is 120 minutes. |
| Step 6 | Set the Encrypt Token (optional); the default setting is On . Use this configuration to secure the tokens as Cisco IdS issues tokens in both plain text or encrypted formats. |
| Step 7 | Click Save . |
| Step 8 | Click Keys and Certificates . The Generate Keys and SAML Certificate page opens and allows you to: Regenerate the Encryption/Signature key by clicking Regenerate . A message appears to say that the Token Registration is successful and advises you to restart the system to complete the
                                                configuration. An Administrator regenerates the Encryption/Signature key when it is exposed or compromised. Regenerate the SAML Certificate by clicking Regenerate . A message appears to say that the SAML certificate regeneration is successful. SAML certificate is regenerated when it expires
                                                or when IdS relying party trust configuration on IdP is deleted. Note Establish the trust relationship again whenever the Encryption keys or SAML certificates are regenerated. | Note | Establish the trust relationship again whenever the Encryption keys or SAML certificates are regenerated. |
| Note | Establish the trust relationship again whenever the Encryption keys or SAML certificates are regenerated. |
| Step 9 | Click Save . |
| Step 10 | Click Identity Service Clients . On the Identity Service Clients tab, you can view the existing Cisco IdS clients, with the client name, client ID, and a redirect URL. To search for a particular
                                       client, click the Search icon above the list of names and type the name of client. |
| Step 11 | To add a client on the Identity Service Clients tab: Click New . Enter the name of client. Enter the Redirect URL. To add more than one URL, click the plus icon. Click Add (or click Clear and then click the X to close the page without adding the client). |
| Step 12 | To edit or delete a client, highlight the client row and click the ellipses under Actions . Then: Click Edit to edit the client's name, ID, or redirect URL. On the Edit Client page, make changes and click Save (or click Clear and then click the X to close the page without saving edits). Click Delete to delete the client. |
| Step 13 | Click Identity Service Settings . |
| Step 14 | Click Troubleshooting to perform some optional troubleshooting. |
| Step 15 | From the Log Level drop-down list, set the local log level by choosing Error , Warning , Info (the default), Debug , or Trace . |
| Step 16 | To receive errors in Syslog format, enter the name of the Remote Syslog Server in the Host (Optional) field. |
| Step 17 | Click Save . |

| Note | Use a log in name in the format username@FQDN to log in to the Unified CCE Administration. |
|---|---|

| Note | Establish the trust relationship again whenever the Encryption keys or SAML certificates are regenerated. |
|---|---|

| Note | If SSO is enabled in the deployment, then import all the IdS server nodes certificate into Cisco Finesse, CUIC, and LiveData
                                             component trust store. |
|---|---|

| Step 1 | In the Unified CCE Administration, navigate to Features > Single Sign-On Overview > Infrastructure Settings > Device Configuration > Identity Service . |
|---|---|
| Step 2 | Click the Register button to register all SSO-compatible components with the Cisco IdS. The component status table displays the registration status of each component. If a component fails to register, correct the error and click Retry . |
| Step 3 | Click the Test button. When the new browser tab opens, you may be prompted to accept a certificate. In order for the page to load, accept
                                       any certificates. Then, when presented with a log in dialog, log in as a user with SSO credentials. The test process verifies that each component has been configured correctly to reach the Identity Provider, and that the Cisco
                                          IdS successfully generates access tokens. Each component that you are setting up for SSO is tested. The component status table displays the status of testing each component. If a test is unsuccessful, correct the error, and then click Test again. Test results are not saved. If you refresh the page, run the test again before enabling SSO. |
| Step 4 | Select the SSO mode  for the system from the Set Mode drop-down menu: Non-SSO: This mode disables SSO for all agents and supervisors. Users log in using existing Active Directory-based local authentication. Hybrid: This mode allows you to enable agents and supervisors selectively for SSO. SSO: This mode enables SSO for all agents and supervisors. The component status table displays the status of setting the SSO mode on  each component. If the SSO mode fails to be set on a component, correct the error,  and then select the mode again. |

| Note | The check box is disabled when the global SSO mode is set to SSO or non-SSO. |
|---|---|

| Note | The administrator's group memberships are not copied to the new user by this CLI command and must be manually updated. The
                                                new user, now a Security Administrator, can set up the group memberships. For any entity (for example, reports or report definitions), if this new user’s permissions provide higher privileges than
                                                the administrator, the privileges are left intact. The privileges are not overwritten by this CLI command. |
|---|---|

| Browser | Browser options to verify when using SSO |
|---|---|
| Internet Explorer | Open Internet Explorer. Click the Tools (Alt+X) icon, and then click Internet options . In the General tab, click Tabs . From the When a new tab is opened, open: drop-down list, verify that the Your first home page option is selected. |
| Chrome | Open Chrome. Click the Customize and control Google Chrome icon. Click Settings . In the On startup section of the Settings page, verify that the Open the New Tab page option is selected. |
| Edge Chromium (Microsoft Edge) | Open Microsoft Edge. Click the Settings and more (Alt+F) (...) icon. Click Settings . On the Settings page, click On startup , and verify that the Open a new tab radio button is selected. |
| Firefox | Open Firefox. Click the Open menu icon. Click Options . In the Startup section of the General page, verify that either the home page or a blank page is chosen in the When Firefox starts drop-down list. |

| Important | While the Finesse agent is logged in, changing the login name
                                          			 prevents the agent from answering or placing calls. In this situation, the
                                          			 agent can still change between ready and not_ready state. This affects all active agents,
                                          			 independent of whether SSO is enabled or disabled. Should you need to modify a
                                          			 login name, do so only after the corresponding agent is logged out. Note too
                                          			 that SSO migration (moving a non-SSO agent to be SSO-enabled, by either hybrid
                                          			 mode or global SSO mode) should not be done when the agent is logged in. |
|---|---|

| Step 1 | In Unified CCE Administration, navigate to Overview > Bulk Import . |
|---|---|
| Step 2 | Download the SSO Migration bulk job content file. Click Templates. The Download Templates popup window opens. Click the Download icon for the SSO Migration
                                             				  template. Click OK to close the Download Templates popup window. |
| Step 3 | Enter the SSO usernames in the SSO Migration content file. Open the template in Microsoft Excel. Update the newUserName field for the agents and
                                             				  supervisors whom you want to migrate to SSO accounts. The content file for the SSO migration bulk job contains these
                                                					 fields: Field Required? Description userName Yes The user's non-SSO username. firstName No The user's first name. lastName No The user's last name. newUserName No The user's new SSO username. Enter up to 255 ASCII
                                                            								  characters. If you want to enable a user for SSO, but keep the
                                                            								  current username, leave newUserName blank, or copy the value of userName into newUserName . Save the populated file locally. | Field | Required? | Description | userName | Yes | The user's non-SSO username. | firstName | No | The user's first name. | lastName | No | The user's last name. | newUserName | No | The user's new SSO username. Enter up to 255 ASCII
                                                            								  characters. If you want to enable a user for SSO, but keep the
                                                            								  current username, leave newUserName blank, or copy the value of userName into newUserName . |
| Field | Required? | Description |
| userName | Yes | The user's non-SSO username. |
| firstName | No | The user's first name. |
| lastName | No | The user's last name. |
| newUserName | No | The user's new SSO username. Enter up to 255 ASCII
                                                            								  characters. If you want to enable a user for SSO, but keep the
                                                            								  current username, leave newUserName blank, or copy the value of userName into newUserName . |
| Step 4 | Create a bulk job to update the usernames in the database. Click New to open the New Bulk Job window. Enter an optional Description for the job. In the Content File field, browse to the SSO
                                             				  Migration content file you completed. The content file is validated before the bulk job is created. Click Save . The new bulk job appears in the list of bulk jobs. Optionally,
                                                					 click the bulk job to review the details and status for the bulk job. You can
                                                					 also download the log file for a bulk job. When the bulk
                                                					 job completes, the agents and supervisors are enabled for SSO and their
                                                					 usernames are updated. You can open an individual user's record in the Agent
                                                					 tool in Unified CCE Administration to see the changes. |

| Field | Required? | Description |
|---|---|---|
| userName | Yes | The user's non-SSO username. |
| firstName | No | The user's first name. |
| lastName | No | The user's last name. |
| newUserName | No | The user's new SSO username. Enter up to 255 ASCII
                                                            								  characters. If you want to enable a user for SSO, but keep the
                                                            								  current username, leave newUserName blank, or copy the value of userName into newUserName . |

| Important | If you later want to migrate agents or supervisors from SSO-enabled to non-SSO: You must assign new passwords for agents (using the Unified CCE Administration Agent tool) when you disable the agents for SSO. If you change a Cisco Unified Intelligence Center supervisor who was created as SSO-enabled to non-SSO, a new, non-SSO user
                                                      account is created for the supervisor after the next user synchronization. The older, SSO-enabled supervisor account (in the
                                                      format SSO\<loginname>) still exists in Cisco Unified Intelligence Center, however, and you must delete it. You must reconfigure
                                                      the new, non-SSO supervisor user account (that matches the supervisor's SAM account name in Active Directory) in Cisco Unified
                                                      Intelligence Center Administration Console to set up the supervisor's reports and permissions. |
|---|---|

| Step 1 | If the system is in SSO mode, change the SSO mode to Hybrid in the Unified CCE Administration Single Sign-On tool. |
|---|---|
| Step 2 | Disable agents for SSO, and assign the agents new passwords.  This step allows the agents to sign into Finesse. In Unified CCE Administration, you can update individual agent records using the Agent tool, or update records in bulk using the Bulk Jobs
                                          Agent content file. |
| Step 3 | Disable supervisors for SSO. This step allows the supervisors to sign in to Unified CCE Administration to reskill agents. In Unified CCE Administration, you can update individual supervisor records using the Agent tool, or update records in bulk using the Bulk
                                          Jobs Agent content file. |
| Step 4 | After you have updated all of the agent and supervisor records, change the SSO mode to Non-SSO . |

| See this
                                          						information | Located
                                          						here | For
                                          						these details |
|---|---|---|
| Solution Design Guide for Cisco Packaged Contact Center Enterprise | https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/tsd-products-support-series-home.html | Design
                                          						considerations and guidelines for deploying the Cisco Packaged CCE system. |
| Virtualization for Cisco Packaged CCE | https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/uc_system/virtualization/pcce_virt_index.html | Information about deploying Packaged CCE (including single
                                          						sign-on) on VMware. |
| Release Notes for Cisco Packaged Contact Center Enterprise Solution | https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-release-notes-list.html | New
                                          						features and changes for this release of the Packaged CCE solution. |
| Contact Center Enterprise Compatibility Matrix | https://www.cisco.com/c/en/us/support/customer-collaboration/packaged-contact-center-enterprise/products-device-support-tables-list.html | Packaged
                                          						CCE requirements. |
| Unified
                                          						CCE Administration Single Sign-On Tool | Online
                                          						help | Changes
                                          						to support single sign-on. |
| System
                                          						Inventory Tool | This
                                          						guide. | Information related to adding SSO-compatible components to the
                                          						inventory. |