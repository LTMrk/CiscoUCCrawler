---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-im-presence-exchange-integration-15-cup0-b-ms-outlook-calendar-integrat-f2eb8eb6ee
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/im_presence/exchange_integration/15/cup0_b_ms-outlook-calendar-integration-15/cup0_b_ms-outlook-calender-integration-1251_chapter_0100.html
retrieved_at: 2026-08-16T16:15:25.495689+00:00
---

Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 15 and SUs

# Microsoft Outlook Calendar Integration for the IM and Presence Service, Release 15 and SUs

Updated: March 18, 2026

Chapter: Configure Microsoft Exchange

## Chapter: Configure Microsoft Exchange

# Configure Microsoft Exchange

## Microsoft Exchange Configuration for Calendar Integration

If you are deploying an on-premise Microsoft Exchange server, complete the procedures in this chapter to configure your Microsoft
                              Exchange  for calendar integration between the IM and Presence Service and Microsoft Outlook. You can integrate the IM and
                              Presence Service with each of the following Microsoft deployment types:

Microsoft Exchange Deployment

Microsoft Configuration

Microsoft Exchange 2016 or 2019

Microsoft Exchange 2016 and 2019 Configuration Task Flow

Testing is performed using the major versions of Microsoft Exchange Server. It is expected that all other cumulative updates
                                          of these major versions remain compatible. For example, when we mention Exchange 2016, it indicates that the IM and Presence
                                          service supports all Cumulative Updates (CU) released under Exchange 2016.

## Microsoft Exchange 2016 and 2019 Configuration Task Flow

Complete these tasks to configure a Microsoft Exchange 2016 or 2019 deployment for Outlook calendar integration with the
                              IM and Presence Service.

Step 1

Verify Windows Security Settings

Verify your Windows Security Settings for Windows Integrated authentication (NTLM).

Step 2

Set Exchange permissions for your release:

Set Exchange Impersonation Permissions for Specific Users or Groups for Exchange 2016 or 2019

Set the Exchange impersonation permissions for specific users or a group of users.

Step 3

Verify permissions for your release:

Verify Permissions on the Microsoft Exchange 2016 or 2019 Accounts

Verify that the permissions propagate to the mailbox level and that a specified user can access the mailbox and impersonate
                                          the account of another user.

Step 4

Enable Authentication on Exchange 2016 or 2019 Running Windows Server 2016

Basic Authentication, Windows Integrated Authentication, or both must be enabled on the EWS virtual directory (/EWS) for the
                                          Exchange Server.

Step 5

Configure Certificates for Exchange Server Task Flow

Complete this task flow  to configure certificates for a Microsoft Exchange deployment.

### Verify Windows Security Settings

Step 1

On the Windows domain controller and server(s) running Exchange, choose Start > Administrative Tools > Local Security Policy .

Step 2

Navigate to Security Settings > Local Policies > Security Options .

Step 3

Choose Network Security: Minimum session security for NTLM SSP based (including secure RPC) servers .

Step 4

Verify that the Require NTLMv2 session security check box is unchecked.

Step 5

If the Require NTLMv2 session security check box is checked, complete the following steps:

Uncheck the check box Require NTLMv2 session security .

Click OK .

Step 6

To apply the new security settings reboot the Windows domain controller and server(s) running Exchange.

The reboot is only required for servers on which a security policy configuration change was performed.

### Set Exchange Impersonation Permissions for Specific Users or Groups for Exchange 2016 or 2019

Complete the
                                 		  following procedure using the Microsoft Exchange Management Shell (EMS) to set
                                 		  the Exchange impersonation permissions for specific users or a group of users.

These are the commands and settings for Exchange Server 2016 or 2019 .

Step 1

Create the
                                          			 account in Active Directory.

Step 2

Open the EMS
                                          			 for command line entry.

Step 3

Run the New-ManagementRoleAssignment command in the EMS to grant a specified existing domain service account (for example, Ex2016 ) the permission to impersonate other user accounts:

Syntax

New-ManagementRoleAssignment -Name:_suImpersonateRoleAsg -Role:ApplicationImpersonation -User: user @ domain

Example

New-ManagementRoleAssignment -Name:_suImpersonateRoleAsg -Role:ApplicationImpersonation -User: Ex2016 @ contoso.com

Step 4

Run this New-ManagementRoleAssignment command to define the scope to which the impersonation permissions apply. In this example,
                                          the Ex2016 account is granted the permission to impersonate all accounts on a specified Exchange Server.

Syntax

New-ManagementScope -Name:_suImpersonateScope -ServerList: server_name

Example

New-ManagementScope -Name:_suImpersonateScope -ServerList: nw066b-227

Step 5

Run the
                                          			 New-ThrottlingPolicy command to create a new Throttling Policy with the
                                          			 recommended values defined in 
                                          			 the below table:

Syntax

New-ThrottlingPolicy -Name: Policy_Name -EwsMaxConcurrency: 100 -EwsMaxSubscriptions: NULL -EwsCutoffBalance 3000000 -EwsMaxBurst 300000 –EwsRechargeRate 900000

Example

New-ThrottlingPolicy –Name IMP_ThrottlingPolicy -EwsMaxConcurrency 100 -EwsMaxSubscriptions unlimited –EwsCutoffBalance 3000000 -EwsMaxBurst 300000 –EwsRechargeRate 900000

Parameter 1

Recommended Configuration Value — Exchange Server 2016 and 2019

3000000

300000

100

Unlimited

900000

Only available with supported Exchange SP1.

Step 6

Run the
                                          			 Set-ThrottlingPolicyAssociation command to associate the new Throttling Policy
                                          			 with the service account used in Step 2.

Syntax

Set-ThrottlingPolicyAssociation -Identity Username -ThrottlingPolicy Policy_Name

Example

Set-ThrottlingPolicyAssociation -Identity ex2016 -ThrottlingPolicy IMP_ThrottlingPolicy

#### What to do next

Verify Permissions on the Microsoft Exchange 2016 or 2019 Accounts

### Verify Permissions on the Microsoft Exchange 2016 or 2019 Accounts

After you have assigned the permissions to the Exchange 2016 or 2019 account, you must verify that the permissions propagate to mailbox level and that a specified user can access the mailbox
                                 and impersonate the account of another user. It takes some time for the permissions to propagate to mailboxes.

Step 1

On the Active
                                          			 Directory Server, verify that the Impersonation account exists.

Step 2

Open the
                                          			 Exchange Management Shell (EMS) for command line entry.

Step 3

On the
                                          			 Exchange Server verify that the service account has been granted the required
                                          			 Impersonation permissions:

Run this
                                                				  command in the EMS:

Get-ManagementRoleAssignment -Role ApplicationImpersonation

Ensure
                                                				  that the command output indicates role assignments with the Role
                                                				  ApplicationImpersonation for the specified account as follows:

Example Command Output

Name - - - -

Role - - -

Role AssigneeName-

Role AssigneeType-

Assignment Method- - -

Effective
                                                                  								  UserName

_suImpersonate
                                                                  								  RoleAs

Application
                                                                  								  Impersonation

ex2016

User

Direct

ex2016

Step 4

Verify that
                                          			 the management scope that applies to the service account is correct:

Run this
                                                				  command in the EMS:

Get-ManagementScope _suImpersonateScope

Ensure
                                                				  that the command output returns the impersonation account name as follows:

Example Command
                                                         						  Output

Name - - -

Scope RestrictionType

Exclusive

Recipient Root - -

Recipient Filter -

Server Filter- - -

_suImpersonate
                                                                  								  Scope

ServerScope

False

User

Direct

Distinguished
                                                                  								  Name

Step 5

Verify that
                                          			 the ThrottlingPolicy parameters match what is defined in the below table by running this command in the
                                          			 EMS.

Get-ThrottlingPolicy -Identity IMP_ThrottlingPolicy |  Format-List | findstr ^Ews

Parameter 1

Recommended Configuration Value — Exchange Server 2016 and 2019

3000000

300000

100

Unlimited

900000

Step 6

Verify that they ThrottlingPolicy has been associated with the Exchange Account.

Get-ThrottlingPolicyAssociation -Identity ex2016

### Enable Authentication on Exchange 2016 or 2019 Running Windows Server 2016

Step 1

From
                                          			 Administrative Tools, open Internet
                                             				Information Services and choose the server.

Step 2

Choose Web
                                             				Sites .

Step 3

Choose Default
                                             				Web Site .

Step 4

Choose EWS .

Step 5

Under the IIS
                                          			 section, choose Authentication .

Step 6

Verify that the
                                          			 following Authentication methods are enabled:

Anonymous Authentication

Windows Authentication and/or Basic Authentication

Step 7

Use the Enable/Disable link in the Actions column to configure appropriately.

#### What to do next

Configure Certificates for Exchange Server Task Flow

## SAN and Wildcard
                        	 Certificate Support

The IM and Presence
                                 			 Service uses X.509 certificates for secure calendaring integration
                              		  with Microsoft Exchange. The IM and
                                 			 Presence Service supports SAN and wildcard certificates, along with
                              		  standard certificates.

SAN certificates
                              		  allow multiple hostnames and IP addresses to be protected by a single
                              		  certificate, by specifying a list of hostnames, IP addresses, or both in the
                              		  X509v3 Subject Alternative Name field.

Wildcard
                              		  certificates allow a domain and unlimited sub-domains to be represented by
                              		  specifying an asterisk (*) in the domain name. Names may contain the wildcard
                              		  character * which is considered to match any single domain name component. For
                              		  example, *.a.com matches foo.a.com but not bar.foo.a.com.

Wildcards can be
                                          			 placed in the Common Name (CN) field for standard certificates, and in the
                                          			 Subject Alternative Name field for SAN certificates.

## Configure Certificates for Exchange Server Task Flow

Complete these tasks to configure certificates for a Microsoft Exchange deployment.

Step 1

Install the Certificate Authority (CA) on your version of Windows Server:

- Installing a CA on Windows Server 2003

- Installing a CA on Windows Server 2008

Although the Certificate Authority (CA) can run on the Exchange Server, we recommend that you use a different Windows Server
                                          as a CA to provide extended security for third-party certificate exchanges.

Step 2

Generate a CSR for your version of Windows Server:

- Generating a CSR – Running Windows Server 2003

- Generating a CSR – Running Windows Server 2008

You must generate a Certificate Signing Request (CSR) on the IIS Server for Exchange, which is subsequently signed by the
                                          CA Server.

Step 3

Submitting a CSR to the CA Server/Certificate Authority

We recommend that the default SSL certificate, generated for Exchange on IIS, should use the Fully Qualified Domain Name (FQDN)
                                          of the Exchange Server and be signed by a Certificate Authority that the IM and Presence Service trusts. This procedure allows
                                          the CA to sign the CSR from Exchange IIS.

Step 4

Downloading a Signed Certificate

Download a copy of the signed certificate.

Step 5

Upload the signed certificate to your version of Windows Server

- Uploading a Signed Certificate – Running Windows 2003

- Uploading a Signed Certificate – Running Windows 2008

This procedure takes the signed CSR and uploads it onto IIS.

Step 6

Downloading a Root Certificate

Download a root certificate from your CA server.

Step 7

Upload a Root Certificate to the IM and Presence Service Node

Upload the root certificate into the IM and Presence Service.

### Installing a CA on
                           	 Windows Server 2008

Step 1

Choose Start > Administrative
                                                				  Tools > Server Manager .

Step 2

In the console tree, choose Roles .

Step 3

Choose Action > Add
                                                				  Roles .

Step 4

Complete the Add
                                             				Roles wizard:

In the Before You Begin window, ensure that you have
                                                				  completed all prerequisites listed and click Next .

In the Select Server Roles window, check the check box for Active Directory Certificate Services and click Next .

In the Introduction Window window, click Next .

In the Select Role Services window, check these check boxes
                                                				  and click Next .

- Certificate Authority

- Certificate Authority Web
                                                      						Enrollment

- Online Responder

In the Specify Setup Type window, click Standalone .

In the Specify CA Type window, click Root CA .

In the Set
                                                   					 Up Private Key window, click Create a new private key .

In the Configure Cryptography for CA window, choose the
                                                				  default cryptographic service provider.

In the Configure CA Name window, enter a common name to
                                                				  identify the CA.

In the Set
                                                   					 Validity Period window, set the validity period for the certificate
                                                				  generated for the CA.

In the Configure Certificate Database window, choose the
                                                				  default certificate database locations.

In the Confirm Installation Selections window, click Install .

In the Installation Results window, verify that the Installation Succeeded message displays for all components
                                                				  and click Close .

#### What to do next

Generating a CSR – Running Windows Server 2008

### Generating a CSR –
                           	 Running Windows Server 2008

You must
                                 		  generate a Certificate Signing Request (CSR) on the IIS Server for Exchange,
                                 		  which is subsequently signed by the CA Server.

Step 1

From
                                          			 Administrative Tools, open the Internet
                                             				Information Services (IIS) Manager window.

Step 2

Under
                                          			 Connections in the left pane of the IIS Manager, choose the Exchange Server.

Step 3

Double-click Server
                                             				Certificates .

Step 4

Under Actions
                                          			 in the right pane of the IIS Manager, choose Create
                                             				Certificate Request .

Step 5

Complete the Request Certificate wizard:

In the Distinguished Name Properties window, enter the
                                                				  following information:

- In the Common Name field, enter the Exchange Server
                                                      						hostname or IP address.

- In the Organization field, enter your company name

- In the Organizational Unit field, enter the organizational
                                                      						unit that your company belongs to.

Enter your
                                                				  geographic information as follows and click Next .

- City/locality

- State/province

- Country/region

The IIS
                                                               						certificate Common Name that you enter is used to configure the Presence
                                                               						Gateway on the IM and Presence Service , and must be identical to the
                                                               						host (URI or IP address) you are trying to reach.

In the Cryptographic Service Provider Properties window,
                                                				  accept the default Cryptographic service provider, choose 2048 for the bit length, and click Next .

In the Certificate Request File Name window, enter the
                                                				  appropriate filename for the certificate request and click Next .

Make
                                                               						sure that you save the CSR without any extension (.txt) and remember where you
                                                               						save it because you need to be able to find this CSR file later. Only use
                                                               						Notepad to open the file.

In the Request File Summary window, confirm that the
                                                				  information is correct and click Next .

In the Request Certificate Completion window, click Finish .

#### What to do next

Submitting a CSR to the CA Server/Certificate Authority

### Submitting a CSR to
                           	 the CA Server/Certificate Authority

We
                                 		  recommend that the default SSL certificate, generated for Exchange on IIS,
                                 		  should use the Fully Qualified Domain Name (FQDN) of the Exchange Server and be
                                 		  signed by a Certificate Authority that the IM and
                                    			 Presence Service trusts. This procedure allows the CA to sign the CSR
                                 		  from Exchange IIS. Perform the following procedure on your CA Server, and
                                 		  configure the FQDN of the Exchange Server in the:

- Exchange certificate.

- Presence Gateway field of the
                                    			 Exchange Presence Gateway in Cisco Unified CM 
                                       			 IM and
                                       				Presence Administration .

#### Before you begin

Generate a
                                 		  CSR on IIS of the Exchange Server.

Step 1

Copy the
                                          			 certificate request file to your CA Server.

Step 2

Open one of the
                                          			 following URLs:

Windows 2003
                                                   					 or Windows 2008: http:// locall_server /certserv

or

Windows
                                                   					 2003: http://127.0.0.1/certserv

Windows
                                                   					 2008: http://127.0.0.1/certsrv

Step 3

Choose Request
                                             				a certificate .

Step 4

Choose advanced
                                             				certificate request .

Step 5

Choose Submit a
                                             				certificate request by using a base-64-encoded CMC or PKCS #10 file, or submit
                                             				a renewal request by using a base-64-encoded PKCS #7 file .

Step 6

Using a text
                                          			 editor like Notepad, open the CSR that you generated.

Step 7

Copy all
                                          			 information from and including

-----BEGIN CERTIFICATE
                                                				  REQUEST

to and including

END CERTIFICATE
                                                				  REQUEST-----

Step 8

Paste the
                                          			 content of the CSR into the Certificate Request text box.

Step 9

(Optional) By
                                          			 default the Certificate Template drop-down list defaults to the Administrator
                                          			 template, which may or may not produce a valid signed certificate appropriate
                                          			 for server authentication. If you have an enterprise root CA, choose the Web
                                          			 Server certificate template from the Certificate Template drop-down list. The
                                          			 Web Server certificate template may not display, and therefore this step may
                                          			 not apply, if you have already modified your CA configuration.

Step 10

Click Submit .

Step 11

In the Administrative Tools window, choose Start > Administrative
                                                				  Tools > Certification > Authority > CA name > Pending
                                                				  Request to open the Certification Authority window. The Certificate Authority window displays the request you
                                          			 just submitted under Pending Requests.

Step 12

Right click on
                                          			 your request, and complete these actions:

Navigate
                                                   					 to All
                                                      						Tasks .

Choose Issue .

Step 13

Choose Issued
                                             				certificates and verify that your certificate has been issued.

#### What to do next

Downloading a Signed Certificate

### Downloading a Signed
                           	 Certificate

#### Before you begin

[Self-signed Certificates] Submit the Certificate signing request (CSR) to the CA server.

[Third-Party Certificates] Request the CSR from your Certificate Authority.

Step 1

In
                                          			 Administrative Tools, open the Certification Authority. The Certificate Request
                                          			 that you issued displays in the Issued Requests area.

Step 2

Right click the
                                          			 request and choose Open .

Step 3

Choose the Details tab.

Step 4

Choose Copy to
                                             				File .

Step 5

When the Certificate Export wizard displays, click Next .

Step 6

Complete the Certificate Export wizard:

In the Export File Format window, choose Base-64 encoded X.509 and click Next .

In the File
                                                   					 to Export window, enter the location where you want to store the
                                                				  certificate, use cert.cer for the certificate name, and choose c:\cert.cer .

In the Certificate Export Wizard Completion window, review
                                                				  the summary information, verify that the export was successful, then click Finish .

Step 7

Copy or FTP the
                                          			 cert.cer to the computer that you use to administer the IM and
                                             				Presence Service .

#### What to do next

Upload of Signed Certificate onto Exchange IIS

Upload a signed certificate for your server type:

Uploading a Signed Certificate – Running Windows 2003

Uploading a Signed Certificate – Running Windows 2008

### Uploading a Signed
                           	 Certificate – Running Windows 2008

This
                                 		  procedure takes the signed CSR and uploads it onto IIS. To upload the signed
                                 		  certificate, perform the following step on the computer that you use to
                                 		  administer the IM and
                                    			 Presence Service .

#### Before you begin

[Self-signed Certificates] Download the signed certificate.

[Third-party Certificates] Your Certificate Authority provides
                                 		  the signed certificate.

Step 1

From
                                          			 Administrative Tools, open the Internet
                                             				Information Services (IIS) Manager window.

Step 2

Under
                                          			 Connections in the left pane of the IIS Manager, choose the Exchange Server.

Step 3

Double-click Server
                                             				Certificates .

Step 4

Under Actions in
                                          			 the right pane of the IIS Manager, choose Complete
                                             				Certificate Request .

Step 5

In the Specify
                                             				Certificate Authority Response window, complete these actions:

To locate
                                                				  your certificate, choose the ellipsis [...].

Navigate to
                                                				  the correct path and filename.

Enter a
                                                				  user-friendly name for your certificate.

Click Ok . The certificate that you completed displays in
                                                				  the certificate list.

Step 6

In the Internet
                                             				Information Services window, complete the following steps to bind the
                                          			 certificate:

Choose Default Web Site .

Under
                                                				  Actions in the right pane of the IIS Manager, choose Bindings .

Step 7

Complete the
                                          			 following steps in the Site
                                             				Bindings window:

Choose https .

Choose Edit .

Step 8

In the Edit Site
                                             				Binding window, complete the following steps :

Choose the
                                                				  certificate that you just created from the SSL certificate drop-down list. The
                                                				  name that you applied to the certificate displays.

Click Ok .

#### What to do next

Downloading a Root Certificate

### Downloading a Root
                           	 Certificate

#### Before you begin

Upload the
                                 		  Signed Certificate onto Exchange IIS.

Step 1

Log in to your
                                          			 CA Server user interface and open a web browser.

Step 2

Open the URL
                                          			 specific to your Windows platform type:

Windows
                                                				  Server 2008 – https://127.0.0.1/certsrv

Step 3

Choose Download a CA
                                             				certificate, certificate chain, or CRL .

Step 4

For the Encoding
                                          			 Method, choose Base 64 .

Step 5

Click Download CA
                                             				Certificate .

Step 6

Save the
                                          			 certificate, certnew.cer ,
                                          			 to the local disk.

#### Tip

If you do not know
                                 		  the Subject Common Name (CN) of the root certificate, you can use an external
                                 		  certificate management tool to find this information. On a Windows operating
                                 		  system, right-click the certificate file with a .cer extension and open the
                                 		  certificate properties.

#### What to do next

Upload a Root Certificate to the IM and Presence Service Node

### Upload a Root
                           	 Certificate to the IM and Presence Service Node

#### Before you begin

- [Self-signed Certificates]
                                    			 Download the root certificate.

- [Third-party Certificates]
                                    			 Request the root certificate from your Certificate Authority. If you have a
                                    			 third-party CA-signed Exchange server certificate, note that you must upload
                                    			 all CA certificates in the certificate chain to the IM and
                                       				Presence Service as a CiscoUnified Presence Trust certificate
                                    			 (cup-trust).

Step 1

Use the
                                          			 Certificate Import Tool in Cisco Unified CM 
                                             			 IM and
                                             				Presence Administration to upload the certificate:

Upload the certificate via:

Actions

Certificate Import Tool in Cisco Unified CM 
                                                            							 IM and Presence Administration .

The Certificate Import tool simplifies the process of installing
                                                         							 trust certificates on the IM and Presence Service and is the primary method for
                                                         							 certificate exchange. The tool allows you to specify the host and port of the
                                                         							 Exchange server and attempts to download the certificate chain from the server.
                                                         							 Once approved, the tool automatically installs missing certificates.

This
                                                                     								procedure describes one way to access and configure the Certificate Import Tool
                                                                     								in Cisco Unified CM 
                                                                        								IM and Presence Administration . You can also view a
                                                                     								customized version of the Certificate Import Tool in Cisco Unified Presence
                                                                        								Administration when you configure the Exchange Presence Gateway for a specific
                                                                     								type of calendaring integration (Log in to Cisco Unified CM IM and Presence
                                                                        								Administration and choose Presence > Gateways ).

- Log in to the Cisco Unified CM 
                                                               								IM and Presence Administration user interface.

Choose System > Security > Certificate Import
                                                                     										Tool .

Choose IM and Presence(IM/P) Trust as the Certificate Trust
                                                               								  Store where you want to install the certificates. This stores the Presence
                                                               								  Engine trust certificates required for Exchange integration.

Enter one of these values to connect with the Exchange Server:

IP address

Hostname

FQDN

The value that you enter in this Peer Server field must exactly
                                                               								  match the IP address, hostname or FQDN of the Exchange Server.

Enter the port that is used to communicate with the Exchange
                                                               								  Server. This value must match the available port on the Exchange Server.

Click Submit . After the tool finishes, it reports these
                                                               								  states for each test:

Peer Server Reachability Status — indicates whether or not the IM and Presence Service can reach (ping) the Exchange
                                                                     										Server. See Troubleshooting Exchange Server Connection Status .

SSL Connection/Certificate Verification Status — indicates whether
                                                                     										or not the Certificate Import Tool succeeded in downloading certificates from
                                                                     										the specified peer server and whether or not a secure connection has been
                                                                     										established between the IM and Presence Service and the remote server. See Troubleshooting SSL Connection Certificate Status .

Step 2

If the
                                          			 Certificate Import Tool indicates that certificates are missing (typically the
                                          			 CA certificate is missing on Microsoft servers), manually upload the CA certificate(s)
                                          			 using the Cisco
                                             				Unified OS Admin Certificate Management window.

Upload the certificate via:

Actions

Cisco Unified IM and Presence Operating System Administration

If the Exchange Server does not provide the CA certificates
                                                         							 during the SSL/TLS handshake, you cannot use the Certificate Import Tool to
                                                         							 import those certificates. In this case, you must manually import the missing
                                                         							 certificates using the Certificate Management tool in (Log in to Cisco Unified
                                                            							 IM and Presence Operating System Administration . Choose Security > Certificate
                                                               								  Management ).

Copy or FTP the certnew.cer certificate file to the computer that you use to
                                                               								  administer your IM and Presence Service node.

- Log in to the Cisco Unified IM
                                                               								and Presence Operating System Administration user interface.

Choose Security > Certificate
                                                                     										Management .

In the Certificate List window, choose Upload Certificate/Certificate Chain .

Complete these actions when the Upload Certificate/Certificate Chain dialog box
                                                               								  opens:

From the Certificate Name drop-down list, choose cup-trust .

Enter the root certificate name without any extension.

Click Browse and choose certnew.cer .

Click Upload File .

Step 3

Return to the
                                          			 Certificate Import Tool ( Step 1 ) and verify that all status tests
                                          			 succeed.

Step 4

Restart the
                                          			 CiscoPresence Engine and SIP Proxy service after you upload all Exchange trust
                                          			 certificates. Log in to 
                                          			 the Cisco
                                             				Unified IM and Presence Serviceability user interface. Choose Tools > Control Center - Feature Services .

#### Tips

The IM and
                                    			 Presence Service allows you to upload Exchange Server trust
                                 		  certificates with or without a Subject Common Name (CN).

#### What to do next

IM and Presence Calendar Integration Task Flow

| Microsoft Exchange Deployment | Microsoft Configuration |
|---|---|
|  |  |
| Microsoft Exchange 2016 or 2019 | Microsoft Exchange 2016 and 2019 Configuration Task Flow |

| Note | Testing is performed using the major versions of Microsoft Exchange Server. It is expected that all other cumulative updates
                                          of these major versions remain compatible. For example, when we mention Exchange 2016, it indicates that the IM and Presence
                                          service supports all Cumulative Updates (CU) released under Exchange 2016. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Verify Windows Security Settings | Verify your Windows Security Settings for Windows Integrated authentication (NTLM). |
| Step 2 | Set Exchange permissions for your release: | Set Exchange Impersonation Permissions for Specific Users or Groups for Exchange 2016 or 2019 Set the Exchange impersonation permissions for specific users or a group of users. |
| Step 3 | Verify permissions for your release: | Verify Permissions on the Microsoft Exchange 2016 or 2019 Accounts Verify that the permissions propagate to the mailbox level and that a specified user can access the mailbox and impersonate
                                          the account of another user. |
| Step 4 | Enable Authentication on Exchange 2016 or 2019 Running Windows Server 2016 | Basic Authentication, Windows Integrated Authentication, or both must be enabled on the EWS virtual directory (/EWS) for the
                                          Exchange Server. |
| Step 5 | Configure Certificates for Exchange Server Task Flow | Complete this task flow  to configure certificates for a Microsoft Exchange deployment. |

| Step 1 | On the Windows domain controller and server(s) running Exchange, choose Start > Administrative Tools > Local Security Policy . |
|---|---|
| Step 2 | Navigate to Security Settings > Local Policies > Security Options . |
| Step 3 | Choose Network Security: Minimum session security for NTLM SSP based (including secure RPC) servers . |
| Step 4 | Verify that the Require NTLMv2 session security check box is unchecked. |
| Step 5 | If the Require NTLMv2 session security check box is checked, complete the following steps: Uncheck the check box Require NTLMv2 session security . Click OK . |
| Step 6 | To apply the new security settings reboot the Windows domain controller and server(s) running Exchange. Note The reboot is only required for servers on which a security policy configuration change was performed. | Note | The reboot is only required for servers on which a security policy configuration change was performed. |
| Note | The reboot is only required for servers on which a security policy configuration change was performed. |

| Note | The reboot is only required for servers on which a security policy configuration change was performed. |
|---|---|

| Step 1 | Create the
                                          			 account in Active Directory. |
|---|---|
| Step 2 | Open the EMS
                                          			 for command line entry. |
| Step 3 | Run the New-ManagementRoleAssignment command in the EMS to grant a specified existing domain service account (for example, Ex2016 ) the permission to impersonate other user accounts: Syntax New-ManagementRoleAssignment -Name:_suImpersonateRoleAsg -Role:ApplicationImpersonation -User: user @ domain Example New-ManagementRoleAssignment -Name:_suImpersonateRoleAsg -Role:ApplicationImpersonation -User: Ex2016 @ contoso.com |
| Step 4 | Run this New-ManagementRoleAssignment command to define the scope to which the impersonation permissions apply. In this example,
                                          the Ex2016 account is granted the permission to impersonate all accounts on a specified Exchange Server. Syntax New-ManagementScope -Name:_suImpersonateScope -ServerList: server_name Example New-ManagementScope -Name:_suImpersonateScope -ServerList: nw066b-227 |
| Step 5 | Run the
                                          			 New-ThrottlingPolicy command to create a new Throttling Policy with the
                                          			 recommended values defined in 
                                          			 the below table: Syntax New-ThrottlingPolicy -Name: Policy_Name -EwsMaxConcurrency: 100 -EwsMaxSubscriptions: NULL -EwsCutoffBalance 3000000 -EwsMaxBurst 300000 –EwsRechargeRate 900000 Example New-ThrottlingPolicy –Name IMP_ThrottlingPolicy -EwsMaxConcurrency 100 -EwsMaxSubscriptions unlimited –EwsCutoffBalance 3000000 -EwsMaxBurst 300000 –EwsRechargeRate 900000 Table 2. Recommended Throttle Policy Settings on Exchange Server 2016 or 2019 Parameter 1 Recommended Configuration Value — Exchange Server 2016 and 2019 EwsCutoffBalance 3000000 EwsMaxBurst 300000 EwsMaxConcurrency 100 EwsMaxSubscriptions Unlimited EwsRechargeRate 900000 1 These are the only EWS parameters that can be changed in Exchange Server 2016 or 2019. Note Only available with supported Exchange SP1. | Parameter 1 | Recommended Configuration Value — Exchange Server 2016 and 2019 | EwsCutoffBalance | 3000000 | EwsMaxBurst | 300000 | EwsMaxConcurrency | 100 | EwsMaxSubscriptions | Unlimited | EwsRechargeRate | 900000 | 1 These are the only EWS parameters that can be changed in Exchange Server 2016 or 2019. | Note | Only available with supported Exchange SP1. |
| Parameter 1 | Recommended Configuration Value — Exchange Server 2016 and 2019 |
| EwsCutoffBalance | 3000000 |
| EwsMaxBurst | 300000 |
| EwsMaxConcurrency | 100 |
| EwsMaxSubscriptions | Unlimited |
| EwsRechargeRate | 900000 |
| 1 These are the only EWS parameters that can be changed in Exchange Server 2016 or 2019. |
| Note | Only available with supported Exchange SP1. |
| Step 6 | Run the
                                          			 Set-ThrottlingPolicyAssociation command to associate the new Throttling Policy
                                          			 with the service account used in Step 2. Syntax Set-ThrottlingPolicyAssociation -Identity Username -ThrottlingPolicy Policy_Name Example Set-ThrottlingPolicyAssociation -Identity ex2016 -ThrottlingPolicy IMP_ThrottlingPolicy |

| Parameter 1 | Recommended Configuration Value — Exchange Server 2016 and 2019 |
|---|---|
| EwsCutoffBalance | 3000000 |
| EwsMaxBurst | 300000 |
| EwsMaxConcurrency | 100 |
| EwsMaxSubscriptions | Unlimited |
| EwsRechargeRate | 900000 |
| 1 These are the only EWS parameters that can be changed in Exchange Server 2016 or 2019. |

| Note | Only available with supported Exchange SP1. |
|---|---|

| Step 1 | On the Active
                                          			 Directory Server, verify that the Impersonation account exists. |
|---|---|
| Step 2 | Open the
                                          			 Exchange Management Shell (EMS) for command line entry. |
| Step 3 | On the
                                          			 Exchange Server verify that the service account has been granted the required
                                          			 Impersonation permissions: Run this
                                                				  command in the EMS: Get-ManagementRoleAssignment -Role ApplicationImpersonation Ensure
                                                				  that the command output indicates role assignments with the Role
                                                				  ApplicationImpersonation for the specified account as follows: Example Command Output Name - - - - Role - - - Role AssigneeName- Role AssigneeType- Assignment Method- - - Effective
                                                                  								  UserName _suImpersonate
                                                                  								  RoleAs Application
                                                                  								  Impersonation ex2016 User Direct ex2016 | Name - - - - | Role - - - | Role AssigneeName- | Role AssigneeType- | Assignment Method- - - | Effective
                                                                  								  UserName | _suImpersonate
                                                                  								  RoleAs | Application
                                                                  								  Impersonation | ex2016 | User | Direct | ex2016 |
| Name - - - - | Role - - - | Role AssigneeName- | Role AssigneeType- | Assignment Method- - - | Effective
                                                                  								  UserName |
| _suImpersonate
                                                                  								  RoleAs | Application
                                                                  								  Impersonation | ex2016 | User | Direct | ex2016 |
| Step 4 | Verify that
                                          			 the management scope that applies to the service account is correct: Run this
                                                				  command in the EMS: Get-ManagementScope _suImpersonateScope Ensure
                                                				  that the command output returns the impersonation account name as follows: Example Command
                                                         						  Output Name - - - Scope RestrictionType Exclusive Recipient Root - - Recipient Filter - Server Filter- - - _suImpersonate
                                                                  								  Scope ServerScope False User Direct Distinguished
                                                                  								  Name | Name - - - | Scope RestrictionType | Exclusive | Recipient Root - - | Recipient Filter - | Server Filter- - - | _suImpersonate
                                                                  								  Scope | ServerScope | False | User | Direct | Distinguished
                                                                  								  Name |
| Name - - - | Scope RestrictionType | Exclusive | Recipient Root - - | Recipient Filter - | Server Filter- - - |
| _suImpersonate
                                                                  								  Scope | ServerScope | False | User | Direct | Distinguished
                                                                  								  Name |
| Step 5 | Verify that
                                          			 the ThrottlingPolicy parameters match what is defined in the below table by running this command in the
                                          			 EMS. Get-ThrottlingPolicy -Identity IMP_ThrottlingPolicy \|  Format-List \| findstr ^Ews Table 3. Recommended Throttle Policy Settings on Exchange Server 2016 or 2019 Parameter 1 Recommended Configuration Value — Exchange Server 2016 and 2019 EwsCutoffBalance 3000000 EwsMaxBurst 300000 EwsMaxConcurrency 100 EwsMaxSubscriptions Unlimited EwsRechargeRate 900000 1 These are the only EWS parameters that can be changed in Exchange Server 2016 or 2019. | Parameter 1 | Recommended Configuration Value — Exchange Server 2016 and 2019 | EwsCutoffBalance | 3000000 | EwsMaxBurst | 300000 | EwsMaxConcurrency | 100 | EwsMaxSubscriptions | Unlimited | EwsRechargeRate | 900000 | 1 These are the only EWS parameters that can be changed in Exchange Server 2016 or 2019. |
| Parameter 1 | Recommended Configuration Value — Exchange Server 2016 and 2019 |
| EwsCutoffBalance | 3000000 |
| EwsMaxBurst | 300000 |
| EwsMaxConcurrency | 100 |
| EwsMaxSubscriptions | Unlimited |
| EwsRechargeRate | 900000 |
| 1 These are the only EWS parameters that can be changed in Exchange Server 2016 or 2019. |
| Step 6 | Verify that they ThrottlingPolicy has been associated with the Exchange Account. Get-ThrottlingPolicyAssociation -Identity ex2016 |

| Name - - - - | Role - - - | Role AssigneeName- | Role AssigneeType- | Assignment Method- - - | Effective
                                                                  								  UserName |
|---|---|---|---|---|---|
| _suImpersonate
                                                                  								  RoleAs | Application
                                                                  								  Impersonation | ex2016 | User | Direct | ex2016 |

| Name - - - | Scope RestrictionType | Exclusive | Recipient Root - - | Recipient Filter - | Server Filter- - - |
|---|---|---|---|---|---|
| _suImpersonate
                                                                  								  Scope | ServerScope | False | User | Direct | Distinguished
                                                                  								  Name |

| Parameter 1 | Recommended Configuration Value — Exchange Server 2016 and 2019 |
|---|---|
| EwsCutoffBalance | 3000000 |
| EwsMaxBurst | 300000 |
| EwsMaxConcurrency | 100 |
| EwsMaxSubscriptions | Unlimited |
| EwsRechargeRate | 900000 |
| 1 These are the only EWS parameters that can be changed in Exchange Server 2016 or 2019. |

| Step 1 | From
                                          			 Administrative Tools, open Internet
                                             				Information Services and choose the server. |
|---|---|
| Step 2 | Choose Web
                                             				Sites . |
| Step 3 | Choose Default
                                             				Web Site . |
| Step 4 | Choose EWS . |
| Step 5 | Under the IIS
                                          			 section, choose Authentication . |
| Step 6 | Verify that the
                                          			 following Authentication methods are enabled: Anonymous Authentication Windows Authentication and/or Basic Authentication |
| Step 7 | Use the Enable/Disable link in the Actions column to configure appropriately. |

| Note | For SAN
                                       		  certificates, the protected host must be contained in the list of hostnames/IP
                                       		  addresses in the Subject Alternative Name field. When you configure the
                                       		  Presence Gateway, the Presence Gateway field must exactly match the protected
                                       		  host listed in the Subject Alternative Name field. Wildcards can be
                                          			 placed in the Common Name (CN) field for standard certificates, and in the
                                          			 Subject Alternative Name field for SAN certificates. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | Install the Certificate Authority (CA) on your version of Windows Server: Installing a CA on Windows Server 2003 Installing a CA on Windows Server 2008 | Although the Certificate Authority (CA) can run on the Exchange Server, we recommend that you use a different Windows Server
                                          as a CA to provide extended security for third-party certificate exchanges. |
| Step 2 | Generate a CSR for your version of Windows Server: Generating a CSR – Running Windows Server 2003 Generating a CSR – Running Windows Server 2008 | You must generate a Certificate Signing Request (CSR) on the IIS Server for Exchange, which is subsequently signed by the
                                          CA Server. |
| Step 3 | Submitting a CSR to the CA Server/Certificate Authority | We recommend that the default SSL certificate, generated for Exchange on IIS, should use the Fully Qualified Domain Name (FQDN)
                                          of the Exchange Server and be signed by a Certificate Authority that the IM and Presence Service trusts. This procedure allows
                                          the CA to sign the CSR from Exchange IIS. |
| Step 4 | Downloading a Signed Certificate | Download a copy of the signed certificate. |
| Step 5 | Upload the signed certificate to your version of Windows Server Uploading a Signed Certificate – Running Windows 2003 Uploading a Signed Certificate – Running Windows 2008 | This procedure takes the signed CSR and uploads it onto IIS. |
| Step 6 | Downloading a Root Certificate | Download a root certificate from your CA server. |
| Step 7 | Upload a Root Certificate to the IM and Presence Service Node | Upload the root certificate into the IM and Presence Service. |

| Step 1 | Choose Start > Administrative
                                                				  Tools > Server Manager . |
|---|---|
| Step 2 | In the console tree, choose Roles . |
| Step 3 | Choose Action > Add
                                                				  Roles . |
| Step 4 | Complete the Add
                                             				Roles wizard: In the Before You Begin window, ensure that you have
                                                				  completed all prerequisites listed and click Next . In the Select Server Roles window, check the check box for Active Directory Certificate Services and click Next . In the Introduction Window window, click Next . In the Select Role Services window, check these check boxes
                                                				  and click Next . Certificate Authority Certificate Authority Web
                                                      						Enrollment Online Responder In the Specify Setup Type window, click Standalone . In the Specify CA Type window, click Root CA . In the Set
                                                   					 Up Private Key window, click Create a new private key . In the Configure Cryptography for CA window, choose the
                                                				  default cryptographic service provider. In the Configure CA Name window, enter a common name to
                                                				  identify the CA. In the Set
                                                   					 Validity Period window, set the validity period for the certificate
                                                				  generated for the CA. Note The CA
                                                            					 issues valid certificates only up to the expiration date that you specify. In the Configure Certificate Database window, choose the
                                                				  default certificate database locations. In the Confirm Installation Selections window, click Install . In the Installation Results window, verify that the Installation Succeeded message displays for all components
                                                				  and click Close . Note The
                                                            					 Active Directory Certificate Services is now listed as one of the roles on the
                                                            					 Server Manager. | Note | The CA
                                                            					 issues valid certificates only up to the expiration date that you specify. | Note | The
                                                            					 Active Directory Certificate Services is now listed as one of the roles on the
                                                            					 Server Manager. |
| Note | The CA
                                                            					 issues valid certificates only up to the expiration date that you specify. |
| Note | The
                                                            					 Active Directory Certificate Services is now listed as one of the roles on the
                                                            					 Server Manager. |

| Note | The CA
                                                            					 issues valid certificates only up to the expiration date that you specify. |
|---|---|

| Note | The
                                                            					 Active Directory Certificate Services is now listed as one of the roles on the
                                                            					 Server Manager. |
|---|---|

| Step 1 | From
                                          			 Administrative Tools, open the Internet
                                             				Information Services (IIS) Manager window. |
|---|---|
| Step 2 | Under
                                          			 Connections in the left pane of the IIS Manager, choose the Exchange Server. |
| Step 3 | Double-click Server
                                             				Certificates . |
| Step 4 | Under Actions
                                          			 in the right pane of the IIS Manager, choose Create
                                             				Certificate Request . |
| Step 5 | Complete the Request Certificate wizard: In the Distinguished Name Properties window, enter the
                                                				  following information: In the Common Name field, enter the Exchange Server
                                                      						hostname or IP address. In the Organization field, enter your company name In the Organizational Unit field, enter the organizational
                                                      						unit that your company belongs to. Enter your
                                                				  geographic information as follows and click Next . City/locality State/province Country/region Note The IIS
                                                               						certificate Common Name that you enter is used to configure the Presence
                                                               						Gateway on the IM and Presence Service , and must be identical to the
                                                               						host (URI or IP address) you are trying to reach. In the Cryptographic Service Provider Properties window,
                                                				  accept the default Cryptographic service provider, choose 2048 for the bit length, and click Next . In the Certificate Request File Name window, enter the
                                                				  appropriate filename for the certificate request and click Next . Note Make
                                                               						sure that you save the CSR without any extension (.txt) and remember where you
                                                               						save it because you need to be able to find this CSR file later. Only use
                                                               						Notepad to open the file. In the Request File Summary window, confirm that the
                                                				  information is correct and click Next . In the Request Certificate Completion window, click Finish . | Note | The IIS
                                                               						certificate Common Name that you enter is used to configure the Presence
                                                               						Gateway on the IM and Presence Service , and must be identical to the
                                                               						host (URI or IP address) you are trying to reach. | Note | Make
                                                               						sure that you save the CSR without any extension (.txt) and remember where you
                                                               						save it because you need to be able to find this CSR file later. Only use
                                                               						Notepad to open the file. |
| Note | The IIS
                                                               						certificate Common Name that you enter is used to configure the Presence
                                                               						Gateway on the IM and Presence Service , and must be identical to the
                                                               						host (URI or IP address) you are trying to reach. |
| Note | Make
                                                               						sure that you save the CSR without any extension (.txt) and remember where you
                                                               						save it because you need to be able to find this CSR file later. Only use
                                                               						Notepad to open the file. |

| Note | The IIS
                                                               						certificate Common Name that you enter is used to configure the Presence
                                                               						Gateway on the IM and Presence Service , and must be identical to the
                                                               						host (URI or IP address) you are trying to reach. |
|---|---|

| Note | Make
                                                               						sure that you save the CSR without any extension (.txt) and remember where you
                                                               						save it because you need to be able to find this CSR file later. Only use
                                                               						Notepad to open the file. |
|---|---|

| Step 1 | Copy the
                                          			 certificate request file to your CA Server. |
|---|---|
| Step 2 | Open one of the
                                          			 following URLs: Windows 2003
                                                   					 or Windows 2008: http:// locall_server /certserv or Windows
                                                   					 2003: http://127.0.0.1/certserv Windows
                                                   					 2008: http://127.0.0.1/certsrv |
| Step 3 | Choose Request
                                             				a certificate . |
| Step 4 | Choose advanced
                                             				certificate request . |
| Step 5 | Choose Submit a
                                             				certificate request by using a base-64-encoded CMC or PKCS #10 file, or submit
                                             				a renewal request by using a base-64-encoded PKCS #7 file . |
| Step 6 | Using a text
                                          			 editor like Notepad, open the CSR that you generated. |
| Step 7 | Copy all
                                          			 information from and including -----BEGIN CERTIFICATE
                                                				  REQUEST to and including END CERTIFICATE
                                                				  REQUEST----- |
| Step 8 | Paste the
                                          			 content of the CSR into the Certificate Request text box. |
| Step 9 | (Optional) By
                                          			 default the Certificate Template drop-down list defaults to the Administrator
                                          			 template, which may or may not produce a valid signed certificate appropriate
                                          			 for server authentication. If you have an enterprise root CA, choose the Web
                                          			 Server certificate template from the Certificate Template drop-down list. The
                                          			 Web Server certificate template may not display, and therefore this step may
                                          			 not apply, if you have already modified your CA configuration. |
| Step 10 | Click Submit . |
| Step 11 | In the Administrative Tools window, choose Start > Administrative
                                                				  Tools > Certification > Authority > CA name > Pending
                                                				  Request to open the Certification Authority window. The Certificate Authority window displays the request you
                                          			 just submitted under Pending Requests. |
| Step 12 | Right click on
                                          			 your request, and complete these actions: Navigate
                                                   					 to All
                                                      						Tasks . Choose Issue . |
| Step 13 | Choose Issued
                                             				certificates and verify that your certificate has been issued. |

| Step 1 | In
                                          			 Administrative Tools, open the Certification Authority. The Certificate Request
                                          			 that you issued displays in the Issued Requests area. |
|---|---|
| Step 2 | Right click the
                                          			 request and choose Open . |
| Step 3 | Choose the Details tab. |
| Step 4 | Choose Copy to
                                             				File . |
| Step 5 | When the Certificate Export wizard displays, click Next . |
| Step 6 | Complete the Certificate Export wizard: In the Export File Format window, choose Base-64 encoded X.509 and click Next . In the File
                                                   					 to Export window, enter the location where you want to store the
                                                				  certificate, use cert.cer for the certificate name, and choose c:\cert.cer . In the Certificate Export Wizard Completion window, review
                                                				  the summary information, verify that the export was successful, then click Finish . |
| Step 7 | Copy or FTP the
                                          			 cert.cer to the computer that you use to administer the IM and
                                             				Presence Service . |

| Step 1 | From
                                          			 Administrative Tools, open the Internet
                                             				Information Services (IIS) Manager window. |
|---|---|
| Step 2 | Under
                                          			 Connections in the left pane of the IIS Manager, choose the Exchange Server. |
| Step 3 | Double-click Server
                                             				Certificates . |
| Step 4 | Under Actions in
                                          			 the right pane of the IIS Manager, choose Complete
                                             				Certificate Request . |
| Step 5 | In the Specify
                                             				Certificate Authority Response window, complete these actions: To locate
                                                				  your certificate, choose the ellipsis [...]. Navigate to
                                                				  the correct path and filename. Enter a
                                                				  user-friendly name for your certificate. Click Ok . The certificate that you completed displays in
                                                				  the certificate list. |
| Step 6 | In the Internet
                                             				Information Services window, complete the following steps to bind the
                                          			 certificate: Choose Default Web Site . Under
                                                				  Actions in the right pane of the IIS Manager, choose Bindings . |
| Step 7 | Complete the
                                          			 following steps in the Site
                                             				Bindings window: Choose https . Choose Edit . |
| Step 8 | In the Edit Site
                                             				Binding window, complete the following steps : Choose the
                                                				  certificate that you just created from the SSL certificate drop-down list. The
                                                				  name that you applied to the certificate displays. Click Ok . |

| Step 1 | Log in to your
                                          			 CA Server user interface and open a web browser. |
|---|---|
| Step 2 | Open the URL
                                          			 specific to your Windows platform type: Windows
                                                				  Server 2008 – https://127.0.0.1/certsrv |
| Step 3 | Choose Download a CA
                                             				certificate, certificate chain, or CRL . |
| Step 4 | For the Encoding
                                          			 Method, choose Base 64 . |
| Step 5 | Click Download CA
                                             				Certificate . |
| Step 6 | Save the
                                          			 certificate, certnew.cer ,
                                          			 to the local disk. |

| Step 1 | Use the
                                          			 Certificate Import Tool in Cisco Unified CM 
                                             			 IM and
                                             				Presence Administration to upload the certificate: Upload the certificate via: Actions Certificate Import Tool in Cisco Unified CM 
                                                            							 IM and Presence Administration . The Certificate Import tool simplifies the process of installing
                                                         							 trust certificates on the IM and Presence Service and is the primary method for
                                                         							 certificate exchange. The tool allows you to specify the host and port of the
                                                         							 Exchange server and attempts to download the certificate chain from the server.
                                                         							 Once approved, the tool automatically installs missing certificates. Note This
                                                                     								procedure describes one way to access and configure the Certificate Import Tool
                                                                     								in Cisco Unified CM 
                                                                        								IM and Presence Administration . You can also view a
                                                                     								customized version of the Certificate Import Tool in Cisco Unified Presence
                                                                        								Administration when you configure the Exchange Presence Gateway for a specific
                                                                     								type of calendaring integration (Log in to Cisco Unified CM IM and Presence
                                                                        								Administration and choose Presence > Gateways ). Log in to the Cisco Unified CM 
                                                               								IM and Presence Administration user interface. Choose System > Security > Certificate Import
                                                                     										Tool . Choose IM and Presence(IM/P) Trust as the Certificate Trust
                                                               								  Store where you want to install the certificates. This stores the Presence
                                                               								  Engine trust certificates required for Exchange integration. Enter one of these values to connect with the Exchange Server: IP address Hostname FQDN The value that you enter in this Peer Server field must exactly
                                                               								  match the IP address, hostname or FQDN of the Exchange Server. Enter the port that is used to communicate with the Exchange
                                                               								  Server. This value must match the available port on the Exchange Server. Click Submit . After the tool finishes, it reports these
                                                               								  states for each test: Peer Server Reachability Status — indicates whether or not the IM and Presence Service can reach (ping) the Exchange
                                                                     										Server. See Troubleshooting Exchange Server Connection Status . SSL Connection/Certificate Verification Status — indicates whether
                                                                     										or not the Certificate Import Tool succeeded in downloading certificates from
                                                                     										the specified peer server and whether or not a secure connection has been
                                                                     										established between the IM and Presence Service and the remote server. See Troubleshooting SSL Connection Certificate Status . | Upload the certificate via: | Actions | Certificate Import Tool in Cisco Unified CM 
                                                            							 IM and Presence Administration . The Certificate Import tool simplifies the process of installing
                                                         							 trust certificates on the IM and Presence Service and is the primary method for
                                                         							 certificate exchange. The tool allows you to specify the host and port of the
                                                         							 Exchange server and attempts to download the certificate chain from the server.
                                                         							 Once approved, the tool automatically installs missing certificates. Note This
                                                                     								procedure describes one way to access and configure the Certificate Import Tool
                                                                     								in Cisco Unified CM 
                                                                        								IM and Presence Administration . You can also view a
                                                                     								customized version of the Certificate Import Tool in Cisco Unified Presence
                                                                        								Administration when you configure the Exchange Presence Gateway for a specific
                                                                     								type of calendaring integration (Log in to Cisco Unified CM IM and Presence
                                                                        								Administration and choose Presence > Gateways ). | Note | This
                                                                     								procedure describes one way to access and configure the Certificate Import Tool
                                                                     								in Cisco Unified CM 
                                                                        								IM and Presence Administration . You can also view a
                                                                     								customized version of the Certificate Import Tool in Cisco Unified Presence
                                                                        								Administration when you configure the Exchange Presence Gateway for a specific
                                                                     								type of calendaring integration (Log in to Cisco Unified CM IM and Presence
                                                                        								Administration and choose Presence > Gateways ). | Log in to the Cisco Unified CM 
                                                               								IM and Presence Administration user interface. Choose System > Security > Certificate Import
                                                                     										Tool . Choose IM and Presence(IM/P) Trust as the Certificate Trust
                                                               								  Store where you want to install the certificates. This stores the Presence
                                                               								  Engine trust certificates required for Exchange integration. Enter one of these values to connect with the Exchange Server: IP address Hostname FQDN The value that you enter in this Peer Server field must exactly
                                                               								  match the IP address, hostname or FQDN of the Exchange Server. Enter the port that is used to communicate with the Exchange
                                                               								  Server. This value must match the available port on the Exchange Server. Click Submit . After the tool finishes, it reports these
                                                               								  states for each test: Peer Server Reachability Status — indicates whether or not the IM and Presence Service can reach (ping) the Exchange
                                                                     										Server. See Troubleshooting Exchange Server Connection Status . SSL Connection/Certificate Verification Status — indicates whether
                                                                     										or not the Certificate Import Tool succeeded in downloading certificates from
                                                                     										the specified peer server and whether or not a secure connection has been
                                                                     										established between the IM and Presence Service and the remote server. See Troubleshooting SSL Connection Certificate Status . |
|---|---|---|---|---|---|---|---|
| Upload the certificate via: | Actions |
| Certificate Import Tool in Cisco Unified CM 
                                                            							 IM and Presence Administration . The Certificate Import tool simplifies the process of installing
                                                         							 trust certificates on the IM and Presence Service and is the primary method for
                                                         							 certificate exchange. The tool allows you to specify the host and port of the
                                                         							 Exchange server and attempts to download the certificate chain from the server.
                                                         							 Once approved, the tool automatically installs missing certificates. Note This
                                                                     								procedure describes one way to access and configure the Certificate Import Tool
                                                                     								in Cisco Unified CM 
                                                                        								IM and Presence Administration . You can also view a
                                                                     								customized version of the Certificate Import Tool in Cisco Unified Presence
                                                                        								Administration when you configure the Exchange Presence Gateway for a specific
                                                                     								type of calendaring integration (Log in to Cisco Unified CM IM and Presence
                                                                        								Administration and choose Presence > Gateways ). | Note | This
                                                                     								procedure describes one way to access and configure the Certificate Import Tool
                                                                     								in Cisco Unified CM 
                                                                        								IM and Presence Administration . You can also view a
                                                                     								customized version of the Certificate Import Tool in Cisco Unified Presence
                                                                        								Administration when you configure the Exchange Presence Gateway for a specific
                                                                     								type of calendaring integration (Log in to Cisco Unified CM IM and Presence
                                                                        								Administration and choose Presence > Gateways ). | Log in to the Cisco Unified CM 
                                                               								IM and Presence Administration user interface. Choose System > Security > Certificate Import
                                                                     										Tool . Choose IM and Presence(IM/P) Trust as the Certificate Trust
                                                               								  Store where you want to install the certificates. This stores the Presence
                                                               								  Engine trust certificates required for Exchange integration. Enter one of these values to connect with the Exchange Server: IP address Hostname FQDN The value that you enter in this Peer Server field must exactly
                                                               								  match the IP address, hostname or FQDN of the Exchange Server. Enter the port that is used to communicate with the Exchange
                                                               								  Server. This value must match the available port on the Exchange Server. Click Submit . After the tool finishes, it reports these
                                                               								  states for each test: Peer Server Reachability Status — indicates whether or not the IM and Presence Service can reach (ping) the Exchange
                                                                     										Server. See Troubleshooting Exchange Server Connection Status . SSL Connection/Certificate Verification Status — indicates whether
                                                                     										or not the Certificate Import Tool succeeded in downloading certificates from
                                                                     										the specified peer server and whether or not a secure connection has been
                                                                     										established between the IM and Presence Service and the remote server. See Troubleshooting SSL Connection Certificate Status . |
| Note | This
                                                                     								procedure describes one way to access and configure the Certificate Import Tool
                                                                     								in Cisco Unified CM 
                                                                        								IM and Presence Administration . You can also view a
                                                                     								customized version of the Certificate Import Tool in Cisco Unified Presence
                                                                        								Administration when you configure the Exchange Presence Gateway for a specific
                                                                     								type of calendaring integration (Log in to Cisco Unified CM IM and Presence
                                                                        								Administration and choose Presence > Gateways ). |
| Step 2 | If the
                                          			 Certificate Import Tool indicates that certificates are missing (typically the
                                          			 CA certificate is missing on Microsoft servers), manually upload the CA certificate(s)
                                          			 using the Cisco
                                             				Unified OS Admin Certificate Management window. Upload the certificate via: Actions Cisco Unified IM and Presence Operating System Administration If the Exchange Server does not provide the CA certificates
                                                         							 during the SSL/TLS handshake, you cannot use the Certificate Import Tool to
                                                         							 import those certificates. In this case, you must manually import the missing
                                                         							 certificates using the Certificate Management tool in (Log in to Cisco Unified
                                                            							 IM and Presence Operating System Administration . Choose Security > Certificate
                                                               								  Management ). Copy or FTP the certnew.cer certificate file to the computer that you use to
                                                               								  administer your IM and Presence Service node. Log in to the Cisco Unified IM
                                                               								and Presence Operating System Administration user interface. Choose Security > Certificate
                                                                     										Management . In the Certificate List window, choose Upload Certificate/Certificate Chain . Complete these actions when the Upload Certificate/Certificate Chain dialog box
                                                               								  opens: From the Certificate Name drop-down list, choose cup-trust . Enter the root certificate name without any extension. Click Browse and choose certnew.cer . Click Upload File . | Upload the certificate via: | Actions | Cisco Unified IM and Presence Operating System Administration If the Exchange Server does not provide the CA certificates
                                                         							 during the SSL/TLS handshake, you cannot use the Certificate Import Tool to
                                                         							 import those certificates. In this case, you must manually import the missing
                                                         							 certificates using the Certificate Management tool in (Log in to Cisco Unified
                                                            							 IM and Presence Operating System Administration . Choose Security > Certificate
                                                               								  Management ). | Copy or FTP the certnew.cer certificate file to the computer that you use to
                                                               								  administer your IM and Presence Service node. Log in to the Cisco Unified IM
                                                               								and Presence Operating System Administration user interface. Choose Security > Certificate
                                                                     										Management . In the Certificate List window, choose Upload Certificate/Certificate Chain . Complete these actions when the Upload Certificate/Certificate Chain dialog box
                                                               								  opens: From the Certificate Name drop-down list, choose cup-trust . Enter the root certificate name without any extension. Click Browse and choose certnew.cer . Click Upload File . |
| Upload the certificate via: | Actions |
| Cisco Unified IM and Presence Operating System Administration If the Exchange Server does not provide the CA certificates
                                                         							 during the SSL/TLS handshake, you cannot use the Certificate Import Tool to
                                                         							 import those certificates. In this case, you must manually import the missing
                                                         							 certificates using the Certificate Management tool in (Log in to Cisco Unified
                                                            							 IM and Presence Operating System Administration . Choose Security > Certificate
                                                               								  Management ). | Copy or FTP the certnew.cer certificate file to the computer that you use to
                                                               								  administer your IM and Presence Service node. Log in to the Cisco Unified IM
                                                               								and Presence Operating System Administration user interface. Choose Security > Certificate
                                                                     										Management . In the Certificate List window, choose Upload Certificate/Certificate Chain . Complete these actions when the Upload Certificate/Certificate Chain dialog box
                                                               								  opens: From the Certificate Name drop-down list, choose cup-trust . Enter the root certificate name without any extension. Click Browse and choose certnew.cer . Click Upload File . |
| Step 3 | Return to the
                                          			 Certificate Import Tool ( Step 1 ) and verify that all status tests
                                          			 succeed. |
| Step 4 | Restart the
                                          			 CiscoPresence Engine and SIP Proxy service after you upload all Exchange trust
                                          			 certificates. Log in to 
                                          			 the Cisco
                                             				Unified IM and Presence Serviceability user interface. Choose Tools > Control Center - Feature Services . |

| Upload the certificate via: | Actions |
|---|---|
| Certificate Import Tool in Cisco Unified CM 
                                                            							 IM and Presence Administration . The Certificate Import tool simplifies the process of installing
                                                         							 trust certificates on the IM and Presence Service and is the primary method for
                                                         							 certificate exchange. The tool allows you to specify the host and port of the
                                                         							 Exchange server and attempts to download the certificate chain from the server.
                                                         							 Once approved, the tool automatically installs missing certificates. Note This
                                                                     								procedure describes one way to access and configure the Certificate Import Tool
                                                                     								in Cisco Unified CM 
                                                                        								IM and Presence Administration . You can also view a
                                                                     								customized version of the Certificate Import Tool in Cisco Unified Presence
                                                                        								Administration when you configure the Exchange Presence Gateway for a specific
                                                                     								type of calendaring integration (Log in to Cisco Unified CM IM and Presence
                                                                        								Administration and choose Presence > Gateways ). | Note | This
                                                                     								procedure describes one way to access and configure the Certificate Import Tool
                                                                     								in Cisco Unified CM 
                                                                        								IM and Presence Administration . You can also view a
                                                                     								customized version of the Certificate Import Tool in Cisco Unified Presence
                                                                        								Administration when you configure the Exchange Presence Gateway for a specific
                                                                     								type of calendaring integration (Log in to Cisco Unified CM IM and Presence
                                                                        								Administration and choose Presence > Gateways ). | Log in to the Cisco Unified CM 
                                                               								IM and Presence Administration user interface. Choose System > Security > Certificate Import
                                                                     										Tool . Choose IM and Presence(IM/P) Trust as the Certificate Trust
                                                               								  Store where you want to install the certificates. This stores the Presence
                                                               								  Engine trust certificates required for Exchange integration. Enter one of these values to connect with the Exchange Server: IP address Hostname FQDN The value that you enter in this Peer Server field must exactly
                                                               								  match the IP address, hostname or FQDN of the Exchange Server. Enter the port that is used to communicate with the Exchange
                                                               								  Server. This value must match the available port on the Exchange Server. Click Submit . After the tool finishes, it reports these
                                                               								  states for each test: Peer Server Reachability Status — indicates whether or not the IM and Presence Service can reach (ping) the Exchange
                                                                     										Server. See Troubleshooting Exchange Server Connection Status . SSL Connection/Certificate Verification Status — indicates whether
                                                                     										or not the Certificate Import Tool succeeded in downloading certificates from
                                                                     										the specified peer server and whether or not a secure connection has been
                                                                     										established between the IM and Presence Service and the remote server. See Troubleshooting SSL Connection Certificate Status . |
| Note | This
                                                                     								procedure describes one way to access and configure the Certificate Import Tool
                                                                     								in Cisco Unified CM 
                                                                        								IM and Presence Administration . You can also view a
                                                                     								customized version of the Certificate Import Tool in Cisco Unified Presence
                                                                        								Administration when you configure the Exchange Presence Gateway for a specific
                                                                     								type of calendaring integration (Log in to Cisco Unified CM IM and Presence
                                                                        								Administration and choose Presence > Gateways ). |

| Note | This
                                                                     								procedure describes one way to access and configure the Certificate Import Tool
                                                                     								in Cisco Unified CM 
                                                                        								IM and Presence Administration . You can also view a
                                                                     								customized version of the Certificate Import Tool in Cisco Unified Presence
                                                                        								Administration when you configure the Exchange Presence Gateway for a specific
                                                                     								type of calendaring integration (Log in to Cisco Unified CM IM and Presence
                                                                        								Administration and choose Presence > Gateways ). |
|---|---|

| Upload the certificate via: | Actions |
|---|---|
| Cisco Unified IM and Presence Operating System Administration If the Exchange Server does not provide the CA certificates
                                                         							 during the SSL/TLS handshake, you cannot use the Certificate Import Tool to
                                                         							 import those certificates. In this case, you must manually import the missing
                                                         							 certificates using the Certificate Management tool in (Log in to Cisco Unified
                                                            							 IM and Presence Operating System Administration . Choose Security > Certificate
                                                               								  Management ). | Copy or FTP the certnew.cer certificate file to the computer that you use to
                                                               								  administer your IM and Presence Service node. Log in to the Cisco Unified IM
                                                               								and Presence Operating System Administration user interface. Choose Security > Certificate
                                                                     										Management . In the Certificate List window, choose Upload Certificate/Certificate Chain . Complete these actions when the Upload Certificate/Certificate Chain dialog box
                                                               								  opens: From the Certificate Name drop-down list, choose cup-trust . Enter the root certificate name without any extension. Click Browse and choose certnew.cer . Click Upload File . |