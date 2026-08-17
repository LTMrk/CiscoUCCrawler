---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-connection-12x-quick-start-guide-b-12xcucqssamlsso-html-b4f8d03520
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/quick_start/guide/b_12xcucqssamlsso.html
retrieved_at: 2026-08-17T02:28:15.426896+00:00
---

Quick Start Guide for SAML SSO Access

# Quick Start Guide for SAML SSO Access

### Download Options

Updated: January 24, 2019

# Cisco Unity Connection SAML SSO

## Introduction

Cisco Unity
                  		Connection supports the single sign-on feature that allows users to log in once
                  		and gain access to Unity Connection web applications, such as Cisco Unity
                  		Connection Administration and Cisco Personal Communications Assistant.

Starting with
                  		release 12.0(1), Unity Connection supports the single sign-on feature on the
                  		platform applications such as Cisco Unified Communications OS Administration
                  		and Disaster Recovery System. Unity Connection provides a user to have single
                  		sign-on access with Unity Connection subscriber web interfaces and across the
                  		administrative web applications on the following Unified Communication
                  		Applications:

The SAML SSO feature
                  		is based on open industry standard protocol SAML (Security Assertion Markup
                  		Language). For more information on SAML protocol, see the Understanding
                     		  SAML Protocol , section.

Single Sign-On
                           		using SAML can now be enabled using only graphical user interface (GUI) as
                           		enabling the features through command line interface (CLI) is no longer
                           		supported.

SAML SSO supports
                  		both LDAP and non-LDAP users to gain single sign-on access. LDAP users are the
                  		users integrated to Active Directory. Non-LDAP users are the users that reside
                  		locally on Unity Connection server.

With Unity Connection 12.5(1) and later, SAML SSO also supports local AD-mapped users to gain single sign-on access. Local
                  AD-mapped users are the users that are present in AD as well as locally on Unity Connection server with same alias.

The LDAP users and local AD-mapped users are allowed to login with a username and password that authenticates on Identity Provider. For more information on
                        Identity Provider, see the Understanding Service Provider and Identity Provider , section.

The non-LDAP users with administrator rights login to Cisco Unity Connection Administration using Recovery URL. Recovery URL provides
                        alternate access to the administrative, platform and serviceability web applications via username and password. A non-LDAP
                        user can access the following web applications on Unity Connection using Recovery URL:

Unity Connection Administration

Cisco Unity Connection Serviceability

Cisco Unified Serviceability

Cisco Unified Communications OS Administration

Disaster Recovery System

## Understanding
               	 Service Provider and Identity Provider

Service Provider (SP) is a protected entity on Unity Connection
                  		that provides the web applications. A Service Provider relies on a trusted
                  		Identity Provider (IdP) or Security Token Service (STS) for authentication and
                  		authorization.

Identity Provider is an online service or website that
                  		authenticates users by means of security tokens. It authenticates the end user
                  		and returns a SAML Assertion. SAML Assertion shows either a Yes (authenticated)
                  		or No (authentication failed) response.

A user must authenticate his or her user credentials on Identity
                  		Provider to gain access to the requested web application. If the authentication
                  		gets rejected at any point, the user do not gain access to any of the requested
                  		web applications. If the authentication is accepted, then the user is allowed
                  		to gain single sign-on access to the requested web application.

For information on the currently supported Identity Providers, see SAML-Based SSO Solution chapter of SAML SSO Deployment Guide for Cisco Unified Communications Applications , Release 12.0(1) available at

https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html .

The definitions of Service Provider and Identity Provider further help
                  		to understand the SAML protocol mechanism.

## Understanding SAML
               	 Protocol

Security Assertion Markup Language (SAML) is an XML based open standard
                  		data format for exchanging data. It is an authentication protocol used by
                  		Service Providers to authenticate a user. The security authentication
                  		information is passed between an Identity Provider and Service Provider.

SAML is an open standard that enables clients to authenticate against
                  		any SAML enabled Collaboration (or Unified Communication) service regardless of
                  		the client platform.

All Cisco Unified Communication web interfaces (e.g. CUCM or Unity Connection) use SAML 2.0 protocol in SAML SSO feature.
                  To authenticate the LDAP user and local AD-mapped user, Unity Connection delegates an authentication request to the Identity
                  Provider. This authentication request generated by the Unity Connection is SAML Request.

The Identity Provider authenticates and returns a SAML Assertion. SAML
                  		Assertion shows either Yes (authenticated) or No (authentication failed).

Single SAML SSO mechanism:

SAML 2.0 protocol is a building block that helps to enable single
                  		sign-on access across collaboration services and also helps to enable
                  		federation between collaboration services and customer's Identity Provider.

Once SSO has been enabled on Unity Connection server, a .xml file named,
                  		SPMetadata<hostname of Unity Connection>.xml is generated by Unity
                  		Connection that acts as a Service Provider metadata. The SAML SP metadata must
                  		be exported from SAML Service Provider (on Unity Connection) and then import it
                  		to Identity Provider (ADFS).

The administrator must export SAML metadata from Cisco Unity Connection
                  		Administration and import that metadata on Identity Provider. The administrator
                  		must also export SAML metadata from Identity Provider and import that metadata
                  		on Cisco Unity Connection Administration. This is a two way handshake process
                  		between the Service Provider (that resides on Unity Connection) and Identity
                  		Provider that is essential for SAML Authentication.

The SAML metadata contains the following information:

- URL information for Identity Provider
                     		  and Service Provider.

- Service Provider Assertion
                     		  Consumer Service (ACS) URLs that instructs Identity Provider where to POST
                     		  assertions.

- Certificate information for
                     		  Identity Provider and Service Provider.

The exchange of SAML metadata builds a trust relationship between
                  		Identity Provider and Service Provider. Identity Provider issues SAML assertion
                  		and Identity Provider digitally signs it. On receiving the SAML assertion,
                  		Service Provider validates the assertion, using Identity Provider certificate
                  		information that guarantees that assertion was issued by Identity Provider.

When single sign-on login fails (e.g. If Identity Provider or Active
                  		Directory is inactive), Recovery URL provides alternate access to
                  		administrative and serviceability web applications via username and password.

## SSO Mode

SAML SSO can be
                  		configured in either of the following modes depending upon the requirements:

Cluster wide: The
                        			 Cluster wide SSO mode allows users to import data using only one SAML SP
                        			 metadata file of either publisher or subscriber per cluster. This SSO mode is
                        			 selected by default in following scenarios:

- In case of fresh Unity
                           				Connection installation.

In case
                              				  Unity Connection is upgraded from a previously SSO disabled release to 12.0(1)
                              				  and later release.

Per node: The Per node SSO mode allows users to import data using separate
                        			 SAML SP metadata file for each node in a cluster. This SSO mode is selected by
                        			 default when Unity Connection is upgraded from a previously SSO enabled release
                        			 to 12.0(1) and later release.

Toggling the
                                    				SSO mode is not applicable while SAML SSO is enabled. The SAML SSO must be
                                    				disabled to toggle from Cluster wide mode to Per node mode and vice-versa.

For more
                  		information about micro traces, see "Troubleshooting Cisco Unity Connection"
                  		chapter of Troubleshooting
                     		  Guide for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg/b_12xcuctsg_chapter_0101.html

For more information
                  		about SAML SSO Access, see "Troubleshooting SAML SSO Access" chapter of Troubleshooting
                     		  Guide for Cisco Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg/b_12xcuctsg_chapter_011011.html

## Prerequisites for
               	 Enabling SAML SSO

To configure the
                  		SAML SSO feature, you must ensure the following requirements to be in place:

- Unity Connection 10.0(1)
                     		  and later release on both the servers in the cluster.

- Install Identity Provider
                     		  on Microsoft Windows 2008 with SP2 platform. You must configure Identity
                     		  Provider on the same domain as Unity Connection server.

- Make sure that the clocks
                     		  on Unity Connection and Identity Provider (chosen for SAML SSO) synchronize
                     		  with each other.

- When enabling SSO mode from
                     		  Cisco Unity Connection Administration, make sure you have at least one LDAP
                     		  user with administrator rights in Unity Connection to Run SSO Test for SAML
                     		  SSO.

- Assign the system
                     		  administrator role to the user accounts to allow them to access Unity
                     		  Connection administrative and serviceability web applications.

- When enabling Cluster wide
                     		  SSO mode, make sure that RSA based Multi-server Tomcat certificate are
                     		  uploaded.

for more information
                  		on certificates, see the Security chapter of
                  		Cisco Unified Communications Operating System Administration Guide for Cisco
                  		Unity Connection Release 12.x at https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/os_administration/b_12xcucosagx.html

Once the above
                  		requirements are met, the Unity Connection server is ready to be configured for
                  		SAML SSO feature.

## Configuring SAML
               	 SSO

This section outlines the key steps and/or instructions that must be
                  		followed for Unity Connection specific configuration. However, if you are
                  		configuring SAML SSO feature for the first time, it is strongly recommended to
                  		follow the detailed instructions given below:

### Configuring
                  	 Identity Provider

You must configure one of the
                     		following Identity Providers before configuring SAML SSO in Unity Connection:

#### Configuring ADFS Server 3.0,4.0,5.0

If you Select AD
                           		  FS as the Identity Provider for SAML SSO:

### SUMMARY STEPS

- Add role and
                           			 features in Server Manager and select FINISH when the installation is complete.

- Select Tools
                           			 in Server Manager and select ADFS
                              				management .

- From the let
                           			 side pane, Select Relaying Party
                              				Trusts from Trust
                              				relationships Folder .

- From the Actions window in the right side pane:

- From Edit Claim
                              				Rules window Click Add Rule . Add Transform
                              				Claim Rule Wizard window is displayed.

- From the Claim rule
                              				template drop-down field, select Send LDAP
                              				Attribute as Claims . Click Next .

- Provide Claim Rule
                              				Name .

- From the Attribute
                              				store drop-down, select Active
                              				Directory .

- Select SAM-Account-Name from the LDAP Attribute drop-down field and type uid in Outgoing Claim
                              				Type field. Click Finish .

- Edit Rule Claim window is displayed, Click Add
                              				Rule . Add Transform
                              				Claim Rule Wizard window is displayed.

- From the Claim rule
                              				template drop-down field, select Send Claims
                              				Using a Custom Rule . Click Next .

- Provide Claim Rule
                              				Name .

- In Custom Rule box. Provide custom rule, the syntax for the custom claim rule
                           			 is:

- Select Finish and Apply followed by OK .

### DETAILED STEPS

Add role and
                                    			 features in Server Manager and select FINISH when the installation is complete.

Select Tools
                                    			 in Server Manager and select ADFS
                                       				management .

From the let
                                    			 side pane, Select Relaying Party
                                       				Trusts from Trust
                                       				relationships Folder .

From the Actions window in the right side pane:

- Select Add
                                             					 Relying Party trust option .

- Add Relying party Trust
                                          				  wizard window is displayed.

- Click Start .

- Select Import
                                             					 data about the relying party from the file option and browse the file. Click Next .

- For importing data Online,
                                          				  select Import
                                             					 data about the relying party published online or on a local network option
                                          				  and provide the URL of the file.

- Provide relaying party
                                          				  trust name in the Display
                                             					 name field. Click Next .

- Select option I do not want to configure
                                             					 multi-factor authentication settings for this relying party trust at this
                                             					 time . Click Next .

- Select Permit all
                                             					 users to access this relying party (Selected by default). Click Next .

- Select Open the Edit Claim
                                          				  Rules dialogue for this relying party trust when the wizard closes. Click Close .

- Edit Claim Rules window
                                          				  for your relying part trust is displayed.

From Edit Claim
                                       				Rules window Click Add Rule . Add Transform
                                       				Claim Rule Wizard window is displayed.

From the Claim rule
                                       				template drop-down field, select Send LDAP
                                       				Attribute as Claims . Click Next .

Provide Claim Rule
                                       				Name .

From the Attribute
                                       				store drop-down, select Active
                                       				Directory .

Select SAM-Account-Name from the LDAP Attribute drop-down field and type uid in Outgoing Claim
                                       				Type field. Click Finish .

Edit Rule Claim window is displayed, Click Add
                                       				Rule . Add Transform
                                       				Claim Rule Wizard window is displayed.

From the Claim rule
                                       				template drop-down field, select Send Claims
                                       				Using a Custom Rule . Click Next .

Provide Claim Rule
                                       				Name .

In Custom Rule box. Provide custom rule, the syntax for the custom claim rule
                                    			 is:

```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]
 => issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] = "urn:oasis:names:tc:SAML:2.0:nameid-format:transient", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/namequalifier"] = "http://<ADFS_FQDN>/adfs/com/adfs/service/trust", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/spnamequalifier"] = "<UC_Node_FQDN>");
```

Select Finish and Apply followed by OK .

#### Configuring
                     	 OpenAM

If you select OpenAM Server as
                           		  the Identity Provider for SAML SSO:

### SUMMARY STEPS

- To configure policies on
                           			 OpenAM server, you must log in to OpenAM and select the Access Control tab.
                           			 Click the Top Level Realm option, select the Policies tab, and then create a new policy.
                           			 Follow the steps as given in the Cisco white paper, https://supportforums.cisco.com/document/55391/cucmssowhitepaperedcs-911568pdf ,
                           			 for creating a new policy. While following the instructions given in the white
                           			 paper, make sure to create policies with the below mentioned Unity
                           			 Connection-specific information:

- Configure a Windows Desktop SSO login module instance. Follow the
                           			 instructions for configuring Windows Desktop as given in the Cisco white paper, https://supportforums.cisco.com/document/55391/cucmssowhitepaperedcs-911568pdf

- Configure a J2EE Agent Profile for Policy Agent 3.0. Follow the
                           			 instructions to create a new J2EE agent as given in the Cisco white paper, https://supportforums.cisco.com/document/55391/cucmssowhitepaperedcs-911568pdf with the below mentioned Unity Connection-specific settings:

### DETAILED STEPS

To configure policies on
                                    			 OpenAM server, you must log in to OpenAM and select the Access Control tab.
                                    			 Click the Top Level Realm option, select the Policies tab, and then create a new policy.
                                    			 Follow the steps as given in the Cisco white paper, https://supportforums.cisco.com/document/55391/cucmssowhitepaperedcs-911568pdf ,
                                    			 for creating a new policy. While following the instructions given in the white
                                    			 paper, make sure to create policies with the below mentioned Unity
                                    			 Connection-specific information:

- Each rule should
                                                						be of the URL Policy Agent service type.

- Make sure to check
                                                						the GET and POST check box for each rule.

```
https://<fqdn>:8443/*
https://<fqdn>:8443/*?*
https://<fqdn>/*
https://<fqdn>/*?*
http://<fqdn>/*
http://<fqdn>/*?*
```

- Make sure that the Subject Type field is Authenticated Users .

Do not check the Exclusive check box

- Mention the Condition type as Active Session Time and specify a condition name.

- Configure active
                                                						session timeout as 120 minutes and select No for the Terminate Session option.

Configure a Windows Desktop SSO login module instance. Follow the
                                    			 instructions for configuring Windows Desktop as given in the Cisco white paper, https://supportforums.cisco.com/document/55391/cucmssowhitepaperedcs-911568pdf

Configure a J2EE Agent Profile for Policy Agent 3.0. Follow the
                                    			 instructions to create a new J2EE agent as given in the Cisco white paper, https://supportforums.cisco.com/document/55391/cucmssowhitepaperedcs-911568pdf with the below mentioned Unity Connection-specific settings:

- The name mentioned as
                                          				  agent profile name is the name that you need to enter when enabling SSO on the
                                          				  Unity Connection server, when it prompts as: “ Enter the name of the profile
                                             					 configured for this policy agent ”.

- The agent password
                                          				  entered here is the password that is entered on the Unity Connection server
                                          				  when it prompts as: “ Enter the password of the profile name ”.

```
–/cuadmin/WEB-INF/pages/logon.jsp
–/cuservice/WEB-INF/pages/logon.jsp
–/ciscopca/WEB-INF/pages/logon.jsp
–/inbox/WEB-INF/pages/logon.jsp
–/ccmservice/WEB-INF/pages/logon.jsp
–/vmrest/WEB-INF/pages/logon.jsp
```

```
–/inbox/gadgets/msg/msg-gadget.xml
```

In addition to above Unity Connection-specific configuration,
                                       				ensure the following points:

- Import users from LDAP
                                          				  to Unity Connection. Users must be configured with the appropriate roles to log
                                          				  in to Cisco Unity Connection Administration, or Cisco Unity Connection
                                          				  Serviceability.

- Upload the OpenAM
                                          				  certificate into Unity Connection as described in the Configuring SSO on Cisco Unified Communications Manager 8.6 section of the Cisco white paper, https://supportforums.cisco.com/document/55391/cucmssowhitepaperedcs-911568pdf .

#### Configuring Ping
                     	 Federate Server

If you select Ping Federate
                           		  Server as the Identity Provider for SAML SSO:

### SUMMARY STEPS

- Install JDK. Download JDK
                           			 from the given location: http://www.oracle.com/technetwork/java/javase/downloads/index.html .

- Set the JAVA_HOME environment variable to the JDK installation
                           			 directory path and add the /bin directory to the PATH variable for your
                           			 platform.

- Download Ping federate.zip file and lic file.

- Unzip the Ping Federate file.

- Save the license key file in the directory:

- sRun the Ping Federate as service.

- Access the PingFederate administrative console:

- Login to Ping Federate.

- Change your password on the Change Password screen and select Save .

- Configure server. Browse to Welcome page and select Next .

- Accept the lic file and select Next .

- Select Single-user Administration and select Next .

- Add System Info details as below and select Next .

- Select Next on Runtime Notifications .

- Select Next on Runtime Reporting .

- Enable Account Management details as below:

- Select Next. Select Save on Summary page.

### DETAILED STEPS

Install JDK. Download JDK
                                    			 from the given location: http://www.oracle.com/technetwork/java/javase/downloads/index.html .

Set the JAVA_HOME environment variable to the JDK installation
                                    			 directory path and add the /bin directory to the PATH variable for your
                                    			 platform.

MyComputer> Properties> Advanced> Environment
                                       				variables> Path

C:\WINDOWS\java;C:\Program Files\Java\jdk1.7.0_21\bin

Download Ping federate.zip file and lic file.

Unzip the Ping Federate file.

Save the license key file in the directory:

<pf_install>/pingfederate/server/default/conf

sRun the Ping Federate as service.

run install-service.bat from the directory:

<pf_install>\pingfederate\sbin\win-x86-32

Access the PingFederate administrative console:

https://<IP >:9999/pingfederate/app

Login to Ping Federate.

Username: Administrator

Password: 2Federate

Change your password on the Change Password screen and select Save .

Configure server. Browse to Welcome page and select Next .

Accept the lic file and select Next .

Select Single-user Administration and select Next .

Add System Info details as below and select Next .

Select Next on Runtime Notifications .

Select Next on Runtime Reporting .

Enable Account Management details as below:

- Select Roles and
                                          				  Protocols.

- Provide the Base URL and Realm . Base URL is the IP address of Ping Federate server.

Select Next. Select Save on Summary page.

##### Configuring SP
                        	 Connection

### SUMMARY STEPS

- Select Create New under SP Connections and select Next . Select the Browser SSO option and select Next .

- Browse sp.xml file and select Next .

- After importing the sp.xml file successfully, select Next .

- Configure Base URL as https://<server name>:8443 . Select Next .

- Select Configure Browser SSO and select Next .

- Select SP-Initiated SSO . Select Next . Specify the Assertion Lifetime and select Next .

- Select Assertion Creation . Select Transient and make sure Include attributes in addition to the transient identifier check box is checked.

- Select snap shot details under Attribute Contract .

- Select Map New Adapter Instance . Select Next .

- Select LDAP under Adapter Instance . Select Next .

### DETAILED STEPS

Select Create New under SP Connections and select Next . Select the Browser SSO option and select Next .

Browse sp.xml file and select Next .

sp.xml file is downloaded from Cisco Unified CM

After importing the sp.xml file successfully, select Next .

Configure Base URL as https://<server name>:8443 . Select Next .

Select Configure Browser SSO and select Next .

Select SP-Initiated SSO . Select Next . Specify the Assertion Lifetime and select Next .

Select Assertion Creation . Select Transient and make sure Include attributes in addition to the transient identifier check box is checked.

Select snap shot details under Attribute Contract .

Select Map New Adapter Instance . Select Next .

Select LDAP under Adapter Instance . Select Next .

#### Configuring Oracle
                     	 Identity Provider Server

If you select Oracle Identity
                           		  Provider Server as the Identity Provider for SAML SSO:

### SUMMARY STEPS

- Login to Oracle Enterprise
                           			 Manager where Oracle Identity Federation has been installed as a component.

- Under Identity and Access in the drop down, select Oracle Identity Federation .

- Under Oracle Identity Federation drop down, select Federations .

- Select Federations . In the Federations window, select Add New Federations . In this case the Metadata file is
                           			 imported from Cisco Unified CM. After the Metadata has been loaded, the Cisco
                           			 Unified CM hostname is displayed under Federations .

- Select the Cisco Unified CM node and select Edit . From Edit , select Attribute Mappings and Filters . Check the Enable Attributes
                              				in Single Sign-On (SSO) check box.

- Check the following check boxes:

- Under Name Mappings , select Add to add new attributes, “User Attribute Name” uid and “Assertion Attribute Name” uid. The Send with SSO Assertion check box should be checked.

- Another attribute to be added as email are “User Attribute Name” mail and “Assertion Attribute Name” email. The “Send with SSO Assertion” check box should be checked.

- Select OK and exit out after saving the configuration.

### DETAILED STEPS

Login to Oracle Enterprise
                                    			 Manager where Oracle Identity Federation has been installed as a component.

Under Identity and Access in the drop down, select Oracle Identity Federation .

Under Oracle Identity Federation drop down, select Federations .

Select Federations . In the Federations window, select Add New Federations . In this case the Metadata file is
                                    			 imported from Cisco Unified CM. After the Metadata has been loaded, the Cisco
                                    			 Unified CM hostname is displayed under Federations .

Select the Cisco Unified CM node and select Edit . From Edit , select Attribute Mappings and Filters . Check the Enable Attributes
                                       				in Single Sign-On (SSO) check box.

Check the following check boxes:

- Unspecified

- Email Address

- Persistent
                                             					 Identifier

- Transient/One-Time
                                             					 Identifier

Apply the above changes with the Apply button on the window and
                                       				then select Attribute Mappings and Filters that opens up a new window.

Under Name Mappings , select Add to add new attributes, “User Attribute Name” uid and “Assertion Attribute Name” uid. The Send with SSO Assertion check box should be checked.

Another attribute to be added as email are “User Attribute Name” mail and “Assertion Attribute Name” email. The “Send with SSO Assertion” check box should be checked.

Select OK and exit out after saving the configuration.

##### Generating and Importing Metadata into Cisco Unified CM

Navigate to Oracle Identity Federation drop down, select Administration and select Security and Trust .

### SUMMARY STEPS

- From the Security and Trust Window, generate Metadata xml with
                              				the option Provider Type as Identity Provider and Protocol as SAML 2.0.

- Import the Metadata into the CUCM.

### DETAILED STEPS

From the Security and Trust Window, generate Metadata xml with
                                       				the option Provider Type as Identity Provider and Protocol as SAML 2.0.

Import the Metadata into the CUCM.

### Configuring
                  	 F5-BIG-IP 11.6.0

If you select F5-BIG-IP 11.6.0 as
                        		  the Identity Provider for SAML SSO:

### SUMMARY STEPS

- Login to F5-BIG-IP server
                        			 with admin credentials.

- Do the following steps for LDAP configuration:

- Navigate to Access Policy and select Access Profiles .

- Navigate to Access Policy> SAML > BIG-IP as IDP and select External SP Connector .

### DETAILED STEPS

Login to F5-BIG-IP server
                                 			 with admin credentials.

Do the following steps for LDAP configuration:

- Navigate to Access Policy > AAA servers and select LDAP .

- Click Create .

- Enter any suitable
                                       				  name in Name .

- Enter direct in Server Connection .

- Enter IP of AD in Server Address .

- Enter domain name of
                                       				  Active Directory in Case Search DN .

- EnterAdministrator@samlsso.cisco.com
                                       				  in Admin DN .

- Enter password of
                                       				  Active Directory in Password for AD .

- Click Finished .

Navigate to Access Policy and select Access Profiles .

- Select any one of the
                                       				  profiles and click Edit .

- Select LDAP Auth .

- Navigate to Server and
                                       				  select the server which is configured in
                                       				  <<<<<<<<<<<Step
                                       				  2>>>>>>>>>.

- Navigate to Search DN and select the domain name of configured Active Directory.

- Click Save .

- Select Apply Access Policy .

- Click Close .

Navigate to Access Policy> SAML > BIG-IP as IDP and select External SP Connector .

Metadata of Connection is the Metadata exported from the
                                                   					 Connection. On Cisco Unity Connection Administration, navigate to SAML Single Sign On and select Export All Metadata . Save the sp.xls file on your
                                                   					 system.

- Browse and select the
                                       				  sp.xls file exported from Cisco Unity Connection Administration.

- Enter Service Provider
                                       				  Name and click OK .

- Select profile name
                                       				  created in previous step and Click Edit .

- Select Security Settings and check the “assertion must be signed” check box.

- Click OK .

- Navigate to Local Idp Services and select Create .

- Under General Settings Tab, provide any Name in Idp Service
                                       				  Name.

- Enter the virtual
                                       				  server id in Idp Entity Id . (Example - https://10.77.47.51)

- Go to Assertion Settings and select Assertion Subject Value <%{session.logon.last.username}>

- Go to Security Settings and select <Common/default.crt> in This device’s Public Certificate .

- Click OK .

- From the list select
                                       				  profile created in above step and click Bind/Unbind SP Connectors and select Common/<profile name>

### Configuring SAML
                  	 SSO

To configure SAML SSO feature on
                        		  server, you must perform the following steps:

### SUMMARY STEPS

- Sign in to Cisco Unity
                        			 Connection Administration and select System Settings .

- On the SAML Single Sign-On page, select either of the following in
                        			 the SSO Mode field:

- Select the Enable SAML SSO option. When you select this option, a wizard opens as Web server connections will be restarted , select Continue .

- To initiate the IdP Metadata import, navigate to Identity Provider (IdP) Metadata Trust File and select the Browse to upload the IdP metadata option from your system.
                        			 Then select the Import IdP Metadata option. Follow the link below to download IdP metadata trust file
                        			 for ADFS:

- If the import of metadata is successful, a success message Import
                        			 succeeded for all servers appears on the screen. Select Next to continue the
                        			 wizard.

- For SAML metadata exchange, select the Download Trust Metadata Fileset option.

- The wizard continues and a window appears for user login to IdP.
                        			 Enter the credentials for the LDAP user with administrator role that was
                        			 automatically populated in the previous window.

### DETAILED STEPS

Sign in to Cisco Unity
                                 			 Connection Administration and select System Settings .

The cluster status is not affected while enabling or disabling
                                             				the SAML SSO feature. SAML SSO cannot be enabled from publisher server if
                                             				subscriber server is inactive or vice versa. SAML SSO cannot be enabled from
                                             				publisher server if subscriber server is inactive or vice versa.

On the SAML Single Sign-On page, select either of the following in
                                 			 the SSO Mode field:

- Per node: To upload the server metadata of a single node.

- Cluster wide: To upload the server metadata for both the nodes in a
                                       				  cluster.

Select the Enable SAML SSO option. When you select this option, a wizard opens as Web server connections will be restarted , select Continue .

When enabling SAML SSO from Unity Connection, make sure you have
                                 			 at least one Unity Connection LDAP user with administrator right.

To initiate the IdP Metadata import, navigate to Identity Provider (IdP) Metadata Trust File and select the Browse to upload the IdP metadata option from your system.
                                 			 Then select the Import IdP Metadata option. Follow the link below to download IdP metadata trust file
                                 			 for ADFS:

```
<https://localhost/FederationMetadata/2007-06/FederationMetadata.xml>
```

If the import of metadata is successful, a success message Import
                                 			 succeeded for all servers appears on the screen. Select Next to continue the
                                 			 wizard.

For SAML metadata exchange, select the Download Trust Metadata Fileset option.

If the Trust Metadata has not been imported then
                                             				a warning message prompts on the screen as The server metadata file must be installed on the IdP before
                                                				  this test is run .

Select Next and a window appears for valid administrator IDs that
                                    				automatically populates the LDAP user with administrator rights into that
                                    				window. If you find the LDAP user with administrator rights automatically
                                    				populated in the above window, then select Run Test to continue.

The wizard continues and a window appears for user login to IdP.
                                 			 Enter the credentials for the LDAP user with administrator role that was
                                 			 automatically populated in the previous window.

This enables the SAML SSO feature completely. Select Finish to
                                    				complete the configuration wizard.

During enable or disable of SAML SSO on Unity Connection,
                                             				Tomcat services get restarted automatically. User must wait for 10 to 12
                                             				minutes approximately to get the web applications initialized properly.

## Access to Web
               	 Applications Using SAML SSO

SAML SSO allows a LDAP user and a local AD-mapped user to login to client applications using username and password that authenticates
                     on Identity Provider. A user sign-in to any of the supported web applications on Unified Communication products (after enabling
                     the SAML SSO feature) also gains access to the following web applications on Unity Connection (apart from Cisco Unified Communications
                     Manager and Cisco Unified CM IM/Presence):

Unity Connection users

Web applications

LDAP users with administrator rights

- Unity Unity
                                    						  Connection Administration

- Cisco Unity
                                    						  Connection Serviceability

- Cisco Unified
                                    						  Serviceability

- Cisco Personal
                                    						  Communications Assistant

- Web Inbox

- Mini Web
                                    						  Inbox(desktop version)

LDAP users without administrator rights

- Cisco Personal
                                    						  Communications Assistant

- Web Inbox

- Mini Web
                                    						  Inbox(desktop version)

To access Web Inbox and Mini Web Inbox, you must have a user with
                              		  mailbox. Also navigate to Unity Connection Administration> Class of Service> Licensed
                                 			 features and make sure that Allow Users to Use the Web Inbox, Messaging Inbox and RSS Feeds check box is checked.

The non-LDAP users with administrator role can login to Cisco Unity
                     		  Connection Administration using Recovery URL. The Recovery URL option is
                     		  present in Unity Connection product deployment selection window just below the
                     		  Cisco Unity Connection option. When SSO login fails (if Identity Provider or
                     		  Active Directory is inactive), Recovery URL provides alternate access to the
                     		  administrative and serviceability web applications via username and password.

## Access to Platform
               	 Applications Using SAML SSO

- Enable SAML SSO for Unity
                           			 Connection. It automatically enables SAML SSO for OS admin and DRS pages

- Create a platform user with
                           			 the same name as LDAP user and try login to OS Admin page

Steps to create a Platform
                        			 User through CLI command

Create a
                              			 platform user using the "set account
                                 				name <username>" command.

In CLI execution, enter the privilege level 0.

Enter Yes for
                              			 the "Allow this User to login to SAML SSO-enabled system through Recovery URL ?
                              			 (Yes / No)" prompt.

Enter the UID value
                              			 for the platform user for the " Please enter the Unique Identifier(UID) value
                              			 for this user" prompt.

The UID
                                          				value must be same as of LDAP user name.

Enter the
                              			 password of the user.

Once the
                              			 account is created successfully, login to cli through this user and reset the
                              			 user password.

The password
                              			 of the platform user must be same as of the LDAP user.

On Unity
                              			 Connection login page, navigate to Cisco Unified
                                 				Communications OS Administration . A window appears for user login to IdP.
                              			 Enter the credentials for the platform user.

## Running CLI
               	 Commands in Unity Connection

SAML SSO feature
                  		introduced the following commands in addition to the above three commands:

- utils sso enable

- utils sso disable

- utils sso status

- utils sso recovery-url
                     		  enable

- utils sso recovery-url
                     		  disable

- set samltrace level
                     		  <trace level>

- show samltrace level

- set account
                     		  ssorecoveryurlaccess

- set account ssouidvalue

This command
                        			 when executed returns an informational text message that prompts that the
                        			 administrator can enable SSO feature only from graphical user interface (GUI).
                        			 Both OpenAM SSO and SAML SSO cannot be enabled from CLI interface

This command
                        			 disables (both OpenAM based or SAML based) SSO mode. Within a cluster, the
                        			 command needs to be executed on both the nodes. You may also disable the SSO
                        			 from graphical user interface (GUI) by selecting the Disable option under the
                        			 specific SSO mode.

When SSO is
                                    				disabled from graphical user interface (GUI) of Unity Connection, it disables
                                    				the SSO mode on both nodes in case of cluster.

This command
                        			 shows the SSO status, enabled or disabled, on each node. This command is
                        			 executed on each node individually.

This command
                        			 enables the Recovery URL SSO mode. It also verifies that this URL is working
                        			 successfully. Within a cluster, the command needs to be executed on both the
                        			 nodes.

This command
                        			 disables the Recovery URL SSO mode on that Connection node.

This command
                        			 enables the specified traces to locate the following information:

- error

- warning

- debug

- fatal

- info

This command
                        			 displays the logs selected for SAML SSO.

This command enables or disables the recovery url access for the
                        			 platform user. If disabled, the platform user will not be able to login through
                        			 the Recovery URL.

This command updates the UID value of a platform user.

## Troubleshooting
               	 SAML SSO

SAML SSO allows a
                  		user to have single sign-on access to web applications until a web browser is
                  		active. Ensure that you have taken care of all the requirements and checklist
                  		while enabling the SAML SSO mode. However, for any SAML SSO related issues, see Troubleshooting
                     		  Guide for Cisco Unity Connection Release 12.x , available at

https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/connection/12x/troubleshooting/guide/b_12xcuctsg.html

### This Document Applies to These Products

- Unity Connection Version 12.x

| Note | Single Sign-On
                           		using SAML can now be enabled using only graphical user interface (GUI) as
                           		enabling the features through command line interface (CLI) is no longer
                           		supported. |
|---|---|

| Note | Toggling the
                                    				SSO mode is not applicable while SAML SSO is enabled. The SAML SSO must be
                                    				disabled to toggle from Cluster wide mode to Per node mode and vice-versa. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Add role and
                                    			 features in Server Manager and select FINISH when the installation is complete. |  |
| Step 2 | Select Tools
                                    			 in Server Manager and select ADFS
                                       				management . |  |
| Step 3 | From the let
                                    			 side pane, Select Relaying Party
                                       				Trusts from Trust
                                       				relationships Folder . |  |
| Step 4 | From the Actions window in the right side pane: | Select Add
                                             					 Relying Party trust option . Add Relying party Trust
                                          				  wizard window is displayed. Click Start . Select Import
                                             					 data about the relying party from the file option and browse the file. Click Next . For importing data Online,
                                          				  select Import
                                             					 data about the relying party published online or on a local network option
                                          				  and provide the URL of the file. Provide relaying party
                                          				  trust name in the Display
                                             					 name field. Click Next . Select option I do not want to configure
                                             					 multi-factor authentication settings for this relying party trust at this
                                             					 time . Click Next . Select Permit all
                                             					 users to access this relying party (Selected by default). Click Next . Select Open the Edit Claim
                                          				  Rules dialogue for this relying party trust when the wizard closes. Click Close . Edit Claim Rules window
                                          				  for your relying part trust is displayed. |
| Step 5 | From Edit Claim
                                       				Rules window Click Add Rule . Add Transform
                                       				Claim Rule Wizard window is displayed. |  |
| Step 6 | From the Claim rule
                                       				template drop-down field, select Send LDAP
                                       				Attribute as Claims . Click Next . |  |
| Step 7 | Provide Claim Rule
                                       				Name . |  |
| Step 8 | From the Attribute
                                       				store drop-down, select Active
                                       				Directory . |  |
| Step 9 | Select SAM-Account-Name from the LDAP Attribute drop-down field and type uid in Outgoing Claim
                                       				Type field. Click Finish . |  |
| Step 10 | Edit Rule Claim window is displayed, Click Add
                                       				Rule . Add Transform
                                       				Claim Rule Wizard window is displayed. |  |
| Step 11 | From the Claim rule
                                       				template drop-down field, select Send Claims
                                       				Using a Custom Rule . Click Next . |  |
| Step 12 | Provide Claim Rule
                                       				Name . |  |
| Step 13 | In Custom Rule box. Provide custom rule, the syntax for the custom claim rule
                                    			 is: | c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"]
 => issue(Type = "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/nameidentifier", Issuer = c.Issuer, OriginalIssuer = c.OriginalIssuer, Value = c.Value, ValueType = c.ValueType, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/format"] = "urn:oasis:names:tc:SAML:2.0:nameid-format:transient", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/namequalifier"] = "http://<ADFS_FQDN>/adfs/com/adfs/service/trust", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/spnamequalifier"] = "<UC_Node_FQDN>"); |
| Step 14 | Select Finish and Apply followed by OK . |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | To configure policies on
                                    			 OpenAM server, you must log in to OpenAM and select the Access Control tab.
                                    			 Click the Top Level Realm option, select the Policies tab, and then create a new policy.
                                    			 Follow the steps as given in the Cisco white paper, https://supportforums.cisco.com/document/55391/cucmssowhitepaperedcs-911568pdf ,
                                    			 for creating a new policy. While following the instructions given in the white
                                    			 paper, make sure to create policies with the below mentioned Unity
                                    			 Connection-specific information: | Ensure the following
                                          				  points while adding rules to the policy: Each rule should
                                                						be of the URL Policy Agent service type. Make sure to check
                                                						the GET and POST check box for each rule. Create a rule for
                                                						each of the following resources, where 'fqdn' is the fully qualified domain
                                                						name of your Unity Connection server: https://<fqdn>:8443/*
https://<fqdn>:8443/*?*
https://<fqdn>/*
https://<fqdn>/*?*
http://<fqdn>/*
http://<fqdn>/*?* Ensure the following
                                          				  points while adding a subject to the policy: Make sure that the Subject Type field is Authenticated Users . Specify a subject
                                                						name. Do not check the Exclusive check box Ensure the following
                                          				  points while adding a condition to the policy: Mention the Condition type as Active Session Time and specify a condition name. Configure active
                                                						session timeout as 120 minutes and select No for the Terminate Session option. |
| Step 2 | Configure a Windows Desktop SSO login module instance. Follow the
                                    			 instructions for configuring Windows Desktop as given in the Cisco white paper, https://supportforums.cisco.com/document/55391/cucmssowhitepaperedcs-911568pdf |  |
| Step 3 | Configure a J2EE Agent Profile for Policy Agent 3.0. Follow the
                                    			 instructions to create a new J2EE agent as given in the Cisco white paper, https://supportforums.cisco.com/document/55391/cucmssowhitepaperedcs-911568pdf with the below mentioned Unity Connection-specific settings: | The name mentioned as
                                          				  agent profile name is the name that you need to enter when enabling SSO on the
                                          				  Unity Connection server, when it prompts as: “ Enter the name of the profile
                                             					 configured for this policy agent ”. The agent password
                                          				  entered here is the password that is entered on the Unity Connection server
                                          				  when it prompts as: “ Enter the password of the profile name ”. Make sure to add the
                                          				  following URIs to the Login Form URI section on the Application tab: –/cuadmin/WEB-INF/pages/logon.jsp
–/cuservice/WEB-INF/pages/logon.jsp
–/ciscopca/WEB-INF/pages/logon.jsp
–/inbox/WEB-INF/pages/logon.jsp
–/ccmservice/WEB-INF/pages/logon.jsp
–/vmrest/WEB-INF/pages/logon.jsp Under the Application
                                          				  tab, add the following URI in the Not Enforced URI Processing session: –/inbox/gadgets/msg/msg-gadget.xml In addition to above Unity Connection-specific configuration,
                                       				ensure the following points: Import users from LDAP
                                          				  to Unity Connection. Users must be configured with the appropriate roles to log
                                          				  in to Cisco Unity Connection Administration, or Cisco Unity Connection
                                          				  Serviceability. Upload the OpenAM
                                          				  certificate into Unity Connection as described in the Configuring SSO on Cisco Unified Communications Manager 8.6 section of the Cisco white paper, https://supportforums.cisco.com/document/55391/cucmssowhitepaperedcs-911568pdf . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Install JDK. Download JDK
                                    			 from the given location: http://www.oracle.com/technetwork/java/javase/downloads/index.html . |  |
| Step 2 | Set the JAVA_HOME environment variable to the JDK installation
                                    			 directory path and add the /bin directory to the PATH variable for your
                                    			 platform. | MyComputer> Properties> Advanced> Environment
                                       				variables> Path C:\WINDOWS\java;C:\Program Files\Java\jdk1.7.0_21\bin |
| Step 3 | Download Ping federate.zip file and lic file. |  |
| Step 4 | Unzip the Ping Federate file. |  |
| Step 5 | Save the license key file in the directory: | <pf_install>/pingfederate/server/default/conf |
| Step 6 | sRun the Ping Federate as service. | run install-service.bat from the directory: <pf_install>\pingfederate\sbin\win-x86-32 |
| Step 7 | Access the PingFederate administrative console: | https://<IP >:9999/pingfederate/app |
| Step 8 | Login to Ping Federate. | Username: Administrator Password: 2Federate |
| Step 9 | Change your password on the Change Password screen and select Save . |  |
| Step 10 | Configure server. Browse to Welcome page and select Next . |  |
| Step 11 | Accept the lic file and select Next . |  |
| Step 12 | Select Single-user Administration and select Next . |  |
| Step 13 | Add System Info details as below and select Next . |  |
| Step 14 | Select Next on Runtime Notifications . |  |
| Step 15 | Select Next on Runtime Reporting . |  |
| Step 16 | Enable Account Management details as below: | Select Roles and
                                          				  Protocols. Provide the Base URL and Realm . Base URL is the IP address of Ping Federate server. |
| Step 17 | Select Next. Select Save on Summary page. |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Select Create New under SP Connections and select Next . Select the Browser SSO option and select Next . |  |
| Step 2 | Browse sp.xml file and select Next . | Note sp.xml file is downloaded from Cisco Unified CM | Note | sp.xml file is downloaded from Cisco Unified CM |
| Note | sp.xml file is downloaded from Cisco Unified CM |
| Step 3 | After importing the sp.xml file successfully, select Next . |  |
| Step 4 | Configure Base URL as https://<server name>:8443 . Select Next . |  |
| Step 5 | Select Configure Browser SSO and select Next . |  |
| Step 6 | Select SP-Initiated SSO . Select Next . Specify the Assertion Lifetime and select Next . |  |
| Step 7 | Select Assertion Creation . Select Transient and make sure Include attributes in addition to the transient identifier check box is checked. |  |
| Step 8 | Select snap shot details under Attribute Contract . |  |
| Step 9 | Select Map New Adapter Instance . Select Next . |  |
| Step 10 | Select LDAP under Adapter Instance . Select Next . |  |

| Note | sp.xml file is downloaded from Cisco Unified CM |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Login to Oracle Enterprise
                                    			 Manager where Oracle Identity Federation has been installed as a component. |  |
| Step 2 | Under Identity and Access in the drop down, select Oracle Identity Federation . |  |
| Step 3 | Under Oracle Identity Federation drop down, select Federations . |  |
| Step 4 | Select Federations . In the Federations window, select Add New Federations . In this case the Metadata file is
                                    			 imported from Cisco Unified CM. After the Metadata has been loaded, the Cisco
                                    			 Unified CM hostname is displayed under Federations . |  |
| Step 5 | Select the Cisco Unified CM node and select Edit . From Edit , select Attribute Mappings and Filters . Check the Enable Attributes
                                       				in Single Sign-On (SSO) check box. |  |
| Step 6 | Check the following check boxes: | Unspecified Email Address Persistent
                                             					 Identifier Transient/One-Time
                                             					 Identifier Apply the above changes with the Apply button on the window and
                                       				then select Attribute Mappings and Filters that opens up a new window. |
| Step 7 | Under Name Mappings , select Add to add new attributes, “User Attribute Name” uid and “Assertion Attribute Name” uid. The Send with SSO Assertion check box should be checked. |  |
| Step 8 | Another attribute to be added as email are “User Attribute Name” mail and “Assertion Attribute Name” email. The “Send with SSO Assertion” check box should be checked. |  |
| Step 9 | Select OK and exit out after saving the configuration. |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | From the Security and Trust Window, generate Metadata xml with
                                       				the option Provider Type as Identity Provider and Protocol as SAML 2.0. |  |
| Step 2 | Import the Metadata into the CUCM. |  |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Login to F5-BIG-IP server
                                 			 with admin credentials. |  |
| Step 2 | Do the following steps for LDAP configuration: | Navigate to Access Policy > AAA servers and select LDAP . Click Create . Enter any suitable
                                       				  name in Name . Enter direct in Server Connection . Enter IP of AD in Server Address . Enter domain name of
                                       				  Active Directory in Case Search DN . EnterAdministrator@samlsso.cisco.com
                                       				  in Admin DN . Enter password of
                                       				  Active Directory in Password for AD . Click Finished . |
| Step 3 | Navigate to Access Policy and select Access Profiles . | Select any one of the
                                       				  profiles and click Edit . Select LDAP Auth . Navigate to Server and
                                       				  select the server which is configured in
                                       				  <<<<<<<<<<<Step
                                       				  2>>>>>>>>>. Navigate to Search DN and select the domain name of configured Active Directory. Click Save . Select Apply Access Policy . Click Close . |
| Step 4 | Navigate to Access Policy> SAML > BIG-IP as IDP and select External SP Connector . | Navigate to Create and select From Metadata . Note Metadata of Connection is the Metadata exported from the
                                                   					 Connection. On Cisco Unity Connection Administration, navigate to SAML Single Sign On and select Export All Metadata . Save the sp.xls file on your
                                                   					 system. Browse and select the
                                       				  sp.xls file exported from Cisco Unity Connection Administration. Enter Service Provider
                                       				  Name and click OK . Select profile name
                                       				  created in previous step and Click Edit . Select Security Settings and check the “assertion must be signed” check box. Click OK . Navigate to Local Idp Services and select Create . Under General Settings Tab, provide any Name in Idp Service
                                       				  Name. Enter the virtual
                                       				  server id in Idp Entity Id . (Example - https://10.77.47.51) Go to Assertion Settings and select Assertion Subject Value <%{session.logon.last.username}> Go to Security Settings and select <Common/default.crt> in This device’s Public Certificate . Click OK . From the list select
                                       				  profile created in above step and click Bind/Unbind SP Connectors and select Common/<profile name> | Note | Metadata of Connection is the Metadata exported from the
                                                   					 Connection. On Cisco Unity Connection Administration, navigate to SAML Single Sign On and select Export All Metadata . Save the sp.xls file on your
                                                   					 system. |
| Note | Metadata of Connection is the Metadata exported from the
                                                   					 Connection. On Cisco Unity Connection Administration, navigate to SAML Single Sign On and select Export All Metadata . Save the sp.xls file on your
                                                   					 system. |

| Note | Metadata of Connection is the Metadata exported from the
                                                   					 Connection. On Cisco Unity Connection Administration, navigate to SAML Single Sign On and select Export All Metadata . Save the sp.xls file on your
                                                   					 system. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Sign in to Cisco Unity
                                 			 Connection Administration and select System Settings . | Note The cluster status is not affected while enabling or disabling
                                             				the SAML SSO feature. SAML SSO cannot be enabled from publisher server if
                                             				subscriber server is inactive or vice versa. SAML SSO cannot be enabled from
                                             				publisher server if subscriber server is inactive or vice versa. | Note | The cluster status is not affected while enabling or disabling
                                             				the SAML SSO feature. SAML SSO cannot be enabled from publisher server if
                                             				subscriber server is inactive or vice versa. SAML SSO cannot be enabled from
                                             				publisher server if subscriber server is inactive or vice versa. |
| Note | The cluster status is not affected while enabling or disabling
                                             				the SAML SSO feature. SAML SSO cannot be enabled from publisher server if
                                             				subscriber server is inactive or vice versa. SAML SSO cannot be enabled from
                                             				publisher server if subscriber server is inactive or vice versa. |
| Step 2 | On the SAML Single Sign-On page, select either of the following in
                                 			 the SSO Mode field: | Per node: To upload the server metadata of a single node. Cluster wide: To upload the server metadata for both the nodes in a
                                       				  cluster. |
| Step 3 | Select the Enable SAML SSO option. When you select this option, a wizard opens as Web server connections will be restarted , select Continue . | When enabling SAML SSO from Unity Connection, make sure you have
                                 			 at least one Unity Connection LDAP user with administrator right. |
| Step 4 | To initiate the IdP Metadata import, navigate to Identity Provider (IdP) Metadata Trust File and select the Browse to upload the IdP metadata option from your system.
                                 			 Then select the Import IdP Metadata option. Follow the link below to download IdP metadata trust file
                                 			 for ADFS: | <https://localhost/FederationMetadata/2007-06/FederationMetadata.xml> |
| Step 5 | If the import of metadata is successful, a success message Import
                                 			 succeeded for all servers appears on the screen. Select Next to continue the
                                 			 wizard. |  |
| Step 6 | For SAML metadata exchange, select the Download Trust Metadata Fileset option. | Caution If the Trust Metadata has not been imported then
                                             				a warning message prompts on the screen as The server metadata file must be installed on the IdP before
                                                				  this test is run . Select Next and a window appears for valid administrator IDs that
                                    				automatically populates the LDAP user with administrator rights into that
                                    				window. If you find the LDAP user with administrator rights automatically
                                    				populated in the above window, then select Run Test to continue. | Caution | If the Trust Metadata has not been imported then
                                             				a warning message prompts on the screen as The server metadata file must be installed on the IdP before
                                                				  this test is run . |
| Caution | If the Trust Metadata has not been imported then
                                             				a warning message prompts on the screen as The server metadata file must be installed on the IdP before
                                                				  this test is run . |
| Step 7 | The wizard continues and a window appears for user login to IdP.
                                 			 Enter the credentials for the LDAP user with administrator role that was
                                 			 automatically populated in the previous window. | This enables the SAML SSO feature completely. Select Finish to
                                    				complete the configuration wizard. Note During enable or disable of SAML SSO on Unity Connection,
                                             				Tomcat services get restarted automatically. User must wait for 10 to 12
                                             				minutes approximately to get the web applications initialized properly. | Note | During enable or disable of SAML SSO on Unity Connection,
                                             				Tomcat services get restarted automatically. User must wait for 10 to 12
                                             				minutes approximately to get the web applications initialized properly. |
| Note | During enable or disable of SAML SSO on Unity Connection,
                                             				Tomcat services get restarted automatically. User must wait for 10 to 12
                                             				minutes approximately to get the web applications initialized properly. |

| Note | The cluster status is not affected while enabling or disabling
                                             				the SAML SSO feature. SAML SSO cannot be enabled from publisher server if
                                             				subscriber server is inactive or vice versa. SAML SSO cannot be enabled from
                                             				publisher server if subscriber server is inactive or vice versa. |
|---|---|

| Caution | If the Trust Metadata has not been imported then
                                             				a warning message prompts on the screen as The server metadata file must be installed on the IdP before
                                                				  this test is run . |
|---|---|

| Note | During enable or disable of SAML SSO on Unity Connection,
                                             				Tomcat services get restarted automatically. User must wait for 10 to 12
                                             				minutes approximately to get the web applications initialized properly. |
|---|---|

| Unity Connection users | Web applications |
|---|---|
| LDAP users with administrator rights | Unity Unity
                                    						  Connection Administration Cisco Unity
                                    						  Connection Serviceability Cisco Unified
                                    						  Serviceability Cisco Personal
                                    						  Communications Assistant Web Inbox Mini Web
                                    						  Inbox(desktop version) |
| LDAP users without administrator rights | Cisco Personal
                                    						  Communications Assistant Web Inbox Mini Web
                                    						  Inbox(desktop version) |

| Note | To access Web Inbox and Mini Web Inbox, you must have a user with
                              		  mailbox. Also navigate to Unity Connection Administration> Class of Service> Licensed
                                 			 features and make sure that Allow Users to Use the Web Inbox, Messaging Inbox and RSS Feeds check box is checked. |
|---|---|

| Step 1 | Create a
                              			 platform user using the "set account
                                 				name <username>" command. In CLI execution, enter the privilege level 0. |
|---|---|
| Step 2 | Enter Yes for
                              			 the "Allow this User to login to SAML SSO-enabled system through Recovery URL ?
                              			 (Yes / No)" prompt. |
| Step 3 | Enter the UID value
                              			 for the platform user for the " Please enter the Unique Identifier(UID) value
                              			 for this user" prompt. Note The UID
                                          				value must be same as of LDAP user name. | Note | The UID
                                          				value must be same as of LDAP user name. |
| Note | The UID
                                          				value must be same as of LDAP user name. |
| Step 4 | Enter the
                              			 password of the user. |
| Step 5 | Once the
                              			 account is created successfully, login to cli through this user and reset the
                              			 user password. The password
                              			 of the platform user must be same as of the LDAP user. |
| Step 6 | On Unity
                              			 Connection login page, navigate to Cisco Unified
                                 				Communications OS Administration . A window appears for user login to IdP.
                              			 Enter the credentials for the platform user. |

| Note | The UID
                                          				value must be same as of LDAP user name. |
|---|---|

| Note | When SSO is
                                    				disabled from graphical user interface (GUI) of Unity Connection, it disables
                                    				the SSO mode on both nodes in case of cluster. |
|---|---|