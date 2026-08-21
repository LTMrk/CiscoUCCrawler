---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-6-2-configuration-guide-pcce-b-admi-3aca3db0aa
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_6_2/configuration/guide/pcce_b_admin_configuration_guide_12_6_2/pcce_b_admin_configuration_guide_12_5_2_chapter_010010.html
retrieved_at: 2026-08-21T12:16:39.813265+00:00
---

Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.6(2)

# Cisco Packaged Contact Center Enterprise Administration and Configuration Guide, Release 12.6(2)

Updated: December 3, 2025

Chapter: Security Certificates

## Chapter: Security Certificates

# Security Certificates

To download certificates, refer to the respective browser documentation for
                                       instructions.

Procedure for enabling ECDSA certificates, refer to the topic Enabling ECDSA for
                                       Unified CCE Solution at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

## CA Certificates

Import CA Certificates to Target Server

Links

Import WSM CA Certificate into CVP

Import CA Certificate into AW Machines

See Enterprise Chat and Email Installation and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/series.html

Obtain and Upload a CA Certificate

Deploy Certificate in Browsers

Import CA Certificate into AW Machines

CA-Signed Certificate

Import CA Certificate into AW Machines

See Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html

Obtain and Upload Third-party CA Certificate

Import CA Certificate into AW Machines

From the IdS server, generate and download a Certificate Signing Requests (CSR).

Obtain Root and Application certificates from the third-party vendor.

Upload the appropriate certificates to the IdS server.

For more information, see https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-configuration-examples-list.html . Ensure to perform the instructions in IdS server.

Obtain and Upload Third-party CA Certificate

Import CA Certificate into AW Machines

See Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html

Obtain and Upload Third-party CA Certificate

Import CA Certificate into AW Machines

PG

CUCM Publisher

CA-Signed Certificate

VOS components

Import VOS CA Certificate into PG

Logger

AW

Rogger

CVP

Import CA Certificate into Cisco Unified CVP

### Generate CSR

Step 1

Log in to Windows and choose Control Panel > Administrative Tools > Internet Information Services (IIS) Manager .

Step 2

In the Connections pane, click the server name.

Step 3

In the IIS area, double-click Server Certificates .

Step 4

In the Actions pane, click Create Certificate Request .

Step 5

In the Request Certificate dialog box, do the following:

Specify the required information in the displayed fields and click Next .

In the Cryptographic service provider drop-down list, leave the default setting.

From the Bit length drop-down list, select 2048.

Step 6

Specify a file name for the certificate request and click Finish .

### Create Trusted CA-Signed Server or Application Certificate

You can create CA-signed certificate in any one of the following ways:

Create certificate internally. Do the following:

Set up Microsoft Certificate Server for Windows Server

Open the CA server certificate page ( https://<CA-server-address>/certsrv ).

Copy the Certificate Request content in the Base-64-encoded certificate request box.

From the Certificate Template drop-down list, choose Web Server.

Click Submit .

Choose Base 64 encoded .

Click Download certificate and save it to the desired destination folder.

Select the Encoding method as Base 64 .

Click Download CA Certificate and save it to the desired destination folder.

Import the Root CA and Intermediate Authority certificates into Windows trust store of every component. For more information
                                          on how to import CA certificates into Windows trust store, see Microsoft documentation.

Import the Root CA and Intermediate Authority certificates into Java keystore of every component. For more information, see Import CA Certificate into AW Machines .

Obtain certificate from a trusted Certificate Authority (CA). Do the following:

Send the CSR to a trusted Certificate Authority (CA) for sign-off.

Obtain the CA-signed application certificate, Root CA certificate, and Intermediate Authority certificate (if any).

Import the Root CA and Intermediate Authority certificates into Windows trust store of every component. For more information
                                          on how to import CA certificates into Windows trust store, see Microsoft documentation.

Import the Root CA and Intermediate Authority certificates into Java keystore of every component. For more information, see Import CA Certificate into AW Machines .

### Produce
                           	 Certificate Internally

#### Set up Microsoft Certificate Server for Windows Server

This procedure assumes that your deployment includes a Windows Server Active Directory server. Perform the following steps
                                    to add the Active Directory Certificate Services role on the Windows Server domain controller.

##### Before you begin

Before you begin, Microsoft .Net Framework must be installed. See Windows Server documentation for instructions.

Step 1

In Windows, open the Server Manager .

Step 2

In the Quick Start window, click Add Roles and Features .

Step 3

In the Set Installation Type tab, select Role-based or feature-based installation , and then click Next .

Step 4

In the Server Selection tab, select the destination server then click Next .

Step 5

In the Server Roles tab, check the Active Directory Certificate Services box, and then click the Add Features button in the pop-up window.

Step 6

In the Features and AD CS tabs, click Next to accept default values.

Step 7

In the Role Services tab, verify that Certification Authority , Certification Authority Web Enrollment , Certificate Enrollment Web Service , and Certificate Enrollment Policy Web Service boxes are box is checked, and then click Next .

Step 8

In the Confirmation tab, click Install .

Step 9

After the installation is complete, click the Configure Active Directory Certificate Service on the destination server link.

Step 10

Verify that the credentials are correct (for the domain Administrator user), and then click Next .

Step 11

In the Role Services tab, check the Certification Authority , Certification Authority Web Enrollment , Certificate Enrollment Web Service , and Certificate Enrollment Policy Web Service boxes box , and then click Next .

Step 12

In the Setup Type tab, select Enterprise CA , and then click Next .

Step 13

In the CA Type tab, select Root CA , and then click Next .

Step 14

In the Private Key , Cryptography , CA Name , Validity Period , and Certificate Database tabs, click Next to accept default values.

Step 15

In the following tabs, leave the default values, and click Next .

CA for CES

Authentication Type for CES

Service Account for CES

Authentication Type for CEP

Step 16

Review the information in the Confirmation tab, and then click Configure .

### Upload and Bind CA-Signed Certificate

#### Upload CA-Signed Certificate to IIS Manager

##### Before you begin

Step 1

Log in to Windows and choose Control Panel > Administrative Tools > Internet Information Services (IIS) Manager .

Step 2

In the Connections pane, click the server name.

Step 3

In the IIS area, double-click Server Certificates .

Step 4

In the Actions pane, click Complete Certificate Request .

Step 5

In the Complete Certificate Request dialog box, complete the following fields:

In the File name containing the certification authority's response field, click the … button.

Browse to the location where signed certificate is stored and then click Open .

In the Friendly name field, enter the FQDN of the server.

Step 6

Click OK to upload the certificate.

#### Bind CA-Signed Certificate to IIS Manager

##### Bind CCE Web Applications

Step 1

Log in to Windows and choose Control Panel > Administrative Tools > Internet Information Services (IIS) Manager .

Step 2

In the Connections pane, choose <server_name> > Sites > Default Web Site .

Step 3

In the Actions pane, click Bindings... .

Step 4

Click the type https with port 443, and then click Edit... .

Step 5

From the SSL certificate drop-down list, select the uploaded signed Certificate Request.

Step 6

Click OK .

Step 7

Navigate to Start > Run > services.msc and restart the IIS Admin Service.

##### Bind Diagnostic Framework Service

Step 1

Open the command prompt.

Step 2

Navigate to the Diagnostic Portico home folder using:

cd <ICM install directory>:\icm\serviceability\diagnostics\bin

Step 3

Remove the current certificate binding to the Diagnostic Portico tool using:

DiagFwCertMgr /task:UnbindCert

Step 4

Open the signed certificate and copy the hash content (without spaces) of the Thumbprint field. Run the following command:

DiagFwCertMgr /task:BindCertFromStore /certhash:<hash_value>

Step 5

Validate if the certificate binding was successful using:

DiagFwCertMgr /task:ValidateCertBinding

DiagFwCertMgr uses port 7890 by default.

Step 6

Restart the Diagnostic Framework service by running the following command:

sc stop "diagfwsvc"

sc start "diagfwsvc"

### Import WSM CA Certificate into CVP

Step 1

Enter the keystore password. To identify the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 2

Remove the existing certificate by running %CVP_HOME%\jre\bin\keytool.exe -delete -alias wsm_certificate -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS .

Step 3

Generate a new key pair for the alias with selected key size by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias wsm_certificate
                                             -v -validity <duration in days> -keysize 2048 -keyalg RSA .

```
Enter keystore password: <enter the keystore password>
What is your first and last name?
 [Unknown]: <specify the FQDN of the CVP server. For example: cvp1a.example.com >
What is the name of your organizational unit?
 [Unknown]: <specify OU> E.g. CCBU
What is the name of your organization?
 [Unknown]: <specify the name of the org> E.g. CISCO
What is the name of your City or Locality?
 [Unknown]: <specify the name of the city/locality>  E.g. BLR
What is the name of your State or Province?
 [Unknown]: <specify the name of the state/province>  E.g. KAR
What is the two-letter country code for this unit?
 [Unknown]: <specify two-letter Country code>  E.g. IN
Specify ‘yes’ for the inputs.
```

The default duration for validity is 90 days.

Step 4

Generate the CSR certificate for the alias by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias wsm_certificate
                                             -file %CVP_HOME%\conf\security\wsm.csr and save it to a file (for example, wsm.csr ) .

To ensure compatibility with RFC 5280-compliant browsers, each certificate must include Subject Alternative Name (SAN). This
                                                         can be accomplished by using the -ext parameter with SAN when generating the Certificate Signing Request (CSR). The -ext parameter
                                                         allows a user to define certificate extensions. The SAN can contain multiple comma separated values including fully qualified
                                                         domain name (FQDN) of the server as well as localhost.

Supported SAN formats include:

ip:192.168.0.1

dns:myserver.mydomain.com

email:name@mydomain.com

For example:

Step 5

Enter the keystore password when prompted.

Step 6

Download wsm.csr from CVP %CVP_HOME%\conf\security\ and sign it from CA.

Step 7

Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\

Step 8

Install the root CA certificate by initially running the import root command %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                             root -file %CVP_HOME%\conf\security\<filename_of_root_cer> and then followed by running the import intermediate command %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                             intermediate_ca -file %CVP_HOME%\conf\security\<filename_of_intermediate_cer>

Step 9

Enter the keystore password when prompted.

Step 10

Install the signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -trustcacerts -alias
                                                wsm_certificate -file %CVP_HOME%\conf\security\<filename_of_wsm_CA_cer> .

Step 11

Enter the keystore password when prompted.

Step 12

Restart the Cisco CVP WebServicesManager service.

### CA-Signed Certificate

To configure TLS and SRTP, see Security Guide for Cisco Unified Communications Manager 11.6 available at https://www.cisco.com/c/en/us/support/unified-communications/unified-communications-manager-callmanager/products-maintenance-guides-list.html

Step 1

Enter the following command in the CLI to set the CUCM in the mixed mode, and to register the endpoints in the encrypted mode:

```
admin: utils ctl set-cluster mixed-mode This operation will set the cluster to Mixed mode.  Auto-registration is enabled on at least one CM node. Do you want to continue? (y/n): y Moving Cluster to Mixed Mode
Cluster set to Mixed Mode
You must reset all phones to ensure they received the updated CTL file. 
You must restart Cisco CTIManager services on all the nodes in the cluster that have the service activated.
admin:
```

Step 2

Choose CUCM Admin Page > System > Enterprise Parameters . Check if Cluster Security Mode is set to 1.

Step 3

Set the minimum TLS version command from the CLI:

```
admin: set tls client min-version 1.2 **WARNING** If you are lowering the TLS version it can lead to security issues **WARNING**

Do you really want to continue (yes/no)? y Run this command in the other nodes of the cluster.

Restart the system using the command 'utils system restart' for the changes to take effect

Command successful
admin: set tls ser admin: set tls server mi admin: set tls server min-version? Syntax:
set tls server min-version

admin: set tls server min-version 1.2 **WARNING** If you are lowering the TLS version it can lead to security issues **WARNING**

Do you really want to continue (yes/no)? y Run this command in the other nodes of the cluster.

Restart the system using the command 'utils system restart' for the changes to take effect

Command successful
admin:
```

Step 4

Create an
                                          			 encrypted phone profile and the SIP trunk profile. Associate them with the
                                          			 phone and CUCM SIP trunk.

Step 5

Go to System > Security > SIP Trunk Security Profile and create a new SIP trunk security profile.

Step 6

On CUCM SIP Trunk, check the SRTP Allowed check box.

Step 7

From SIP Trunk Security Profile drop-down list, choose TLS Secure Profile .

Step 8

Restart the TFTP and Cisco CallManager services on all the nodes in the cluster that run these services.

Step 9

Upload the root certificate generated from the CA to CUCM against CUCM-trust.

Step 10

Generate the CSR against CallManager and select the key-length as 2048.

Step 11

Sign the certificate on a CA https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/118731-configure-san-00.html .

Step 12

Click Upload
                                             				Certificate on CUCM by selecting the certificate name as CallManager .

On successful
                                             				completion, CUCM displays the description as Certificate
                                                				  signed by <CA hostname> .

Step 13

Restart TFTP
                                          			 and Cisco CallManager services on all the nodes in the cluster that run these
                                          			 services.

### Import CA Certificate into AW Machines

### SUMMARY STEPS

- Log in to the AW-HDS-DDS Server.

- Run the following command:

- Copy the Root or intermediate certificates to a location in AW Machine.

- Remove the existing certificate by running the following command:

- Enter the truststore password when prompted.

- At the AW machine terminal, run the following command:

- Enter the truststore password when prompted.

- Go to Services and restart Apache Tomcat.

### DETAILED STEPS

Step 1

Log in to the AW-HDS-DDS Server.

Step 2

Run the following command:

```
cd %CCE_JAVA_HOME%\bin
```

Step 3

Copy the Root or intermediate certificates to a location in AW Machine.

Step 4

Remove the existing certificate by running the following command:

```
keytool.exe -delete -alias <AW FQDN> -keystore <ICM install directory>\ssl\cacerts
```

Step 5

Enter the truststore password when prompted.

The default truststore password is changeit .

To change the truststore password, see Change Java Truststore Password .

Step 6

At the AW machine terminal, run the following command:

```
cd %CCE_JAVA_HOME%\bin
```

```
keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> <AW FQDN> -keystore <ICM install directory>\ssl\cacerts
```

Step 7

Enter the truststore password when prompted.

Step 8

Go to Services and restart Apache Tomcat.

For more information, refer to Custom Truststore to Store Component
                                                            Certificate section.

### Import VOS CA Certificate into PG

#### Before you begin

This procedure explains how to import CA certificates that signed a VOS component certificate to a PG server.

### SUMMARY STEPS

- Copy the CA certificate to a location in the PG server.

- Run the following command as an administrator at the target server (machine terminal):

- Enter the truststore password when prompted. The default truststore password is changeit .

- Go to Services and restart Apache Tomcat.

### DETAILED STEPS

Step 1

Copy the CA certificate to a location in the PG server.

Step 2

Run the following command as an administrator at the target server (machine terminal):

Important

```
cd % CCE_JAVA_HOME %\bin
```

```
keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> -keystore <ICM install directory>\ssl\cacerts
```

Step 3

Enter the truststore password when prompted. The default truststore password is changeit .

To change the truststore password, see Change Java Truststore Password .

Step 4

Go to Services and restart Apache Tomcat.

### Import CA Certificate into Rogger/Logger

### SUMMARY STEPS

- Log in to the Logger/Rogger Server.

- Run the following command:

- Copy the Root or intermediate certificates to a location in Logger/Rogger VMs.

- Remove the existing certificate by executing:

- Enter the truststore password changeit when prompted.

- At the Logger/Rogger machine terminal, run the following command:

- Enter the truststore password when prompted.

- Go to Services and restart Apache Tomcat.

### DETAILED STEPS

Step 1

Log in to the Logger/Rogger Server.

Step 2

Run the following command:

Important

```
cd % CCE_JAVA_HOME %\bin
```

Step 3

Copy the Root or intermediate certificates to a location in Logger/Rogger VMs.

Step 4

Remove the existing certificate by executing:

```
keytool.exe -delete -alias <alias name>  -keystore <ICM install directory>\ssl\cacerts <ICM install directory>\ssl\cacerts
```

Step 5

Enter the truststore password changeit when prompted.

Step 6

At the Logger/Rogger machine terminal, run the following command:

```
cd % CCE_JAVA_HOME %\bin
```

```
keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> -keystore <ICM install directory>\ssl\cacerts <ICM install directory>\ssl\cacerts
```

Step 7

Enter the truststore password when prompted.

Step 8

Go to Services and restart Apache Tomcat.

### Import CA Certificate into Cisco Unified CVP

Follow the steps below to Import AW Certificate for RSA or ECDSA certificate at CVP and Unified CCE component.

### SUMMARY STEPS

- Download Packaged CCE webadmin CA certificate to %CVP_HOME%\conf\security\ .

- Import the certificate to the CVP Call Server keystore - %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                    AW_cert -file %CVP_HOME%\conf\security\<AW certificate> .

### DETAILED STEPS

Step 1

Download Packaged CCE webadmin CA certificate to %CVP_HOME%\conf\security\ .

Step 2

Import the certificate to the CVP Call Server keystore - %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                             AW_cert -file %CVP_HOME%\conf\security\<AW certificate> .

## Self-signed Certificates

The following table lists components from which self-signed certificates are generated and components into which self-signed
                           certificates are imported.

Import Self-signed Certificates to Target Server

Generate Self-signed Certificates from Source Component Server

Links

AW Machines

Unified CCE Components (Router, Logger 1 , Rogger 2 , PGs, AWs, and HDS

Import Unified CCE Component Certificates

Import Diagnostic Framework Portico Certificate into AWMachines

Customer Voice Portal (CVP) Call Server/CVP Reporting Server

Email and Chat (ECE)

Cisco Finesse Primary and Secondary

Cisco Unified Communications Manager (CUCM) Publisher and Subscriber

Virtualized Voice Browser (VVB)

Cisco Unified Intelligence Center (CUIC) Publisher and Subscriber

Cisco Identity Service (IdS) Publisher and Subscriber

Cloud Connect Publisher and Subscriber

Customer Collaboration Platform

Live Data Publisher and Subscriber

CUCM Publisher

Logger

AW

Import Unified CCE Component Certificates

Rogger

CVP

### Generate Certificate on CVP Call Server

Step 1

http://acrsrv-app-prd-01:8080/ Export the Call Server certificate by
                                          running. %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore
                                             %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                             callserver_certificate -file
                                             %CVP_HOME%\conf\security\<callserver_certificate>

Step 2

Enter the keystore password when prompted.

Step 3

Restart the Call Server service to load the new certificates.

### Import Certificate into ICM

Step 1

Copy the self-signed CVP Call Server certificate downloaded from CVP to the ICM box (PG) .

Step 2

Open the command prompt and go to c:\icm\bin .

Step 3

Type CiscoCertUtil.exe /install
                                             <callserver_certificate> .

Repeat the procedure for multiple PIMs and for Side A and Side B.

### Generate Certificate on ICM Server

#### Before you begin

Step 1

Log into the ICM (PG) box. Go to the command prompt and type CiscoCertUtil.exe /generatecert .

```
C:\icm\bin>ciscocertutil.exe /generatecert SSL config path = C:\icm\ssl\cfg\openssl.cfg
SYSTEM command is C:\icm\ssl\bin\openssl.exe req -x509 -newkey rsa:2048 -days 7300 -nodes -subj /CN=PG-SIDEA.pcce.com -out
C:\icm\ssl\certs\host.pem -keyout C:\icm\ssl\keys\host.key
Generating a RSA private key
..................
....
writing new private key to 'C:\icm\ssl\keys\host.key
```

Step 2

Cycle VRU PG.

### Import ICM  Certificate into CVP Call Server

Step 1

Log into the CVP Call Server box. Create a folder and copy host.pem to c:\IcmCertificate .

Step 2

From the command prompt, run %CVP_HOME%\jre\bin\keytool.exe -import -v -alias icm_certificate -storetype JCEKS -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore
                                             -file c:\IcmCertificate\host.pem .

Step 3

Enter the keystore password when prompted. Click Yes .

Step 4

Restart the Callserver service to load the new certificates.

Repeat the procedure if you have multiple Call Servers.

### Import AW Certificate into Cisco Unified CVP Servers

Follow the steps below to Import AW Certificate for RSA or ECDSA certificate at
                                             CVP and Unified CCE component.

Step 1

Download Packaged CCE webadmin self-signed certificate to %CVP_HOME%\conf\security\ .

Step 2

Import the certificate to the CVP Call Server keystore - %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                             AW_cert -file %CVP_HOME%\conf\security\<AW certificate> .

### Self-signed Certificates

#### Import Unified CCE Component Certificates

Important

The certificate CommonName (CN) must match the Fully Qualified Domain Name (FQDN) provided for the Unified CCE components
                                                in the Packaged Unified CCE Inventory.

### SUMMARY STEPS

- Log in to the required Unified CCE component server.

- From the browser ( https://<FQDN of the Unified CCE component server> ), download the certificate.

- Copy the certificate to a location in the target server.

- Run the following command at the target server (machine terminal):

- Enter the truststore password when prompted.

- Go to Services and restart Apache Tomcat on target servers.

### DETAILED STEPS

Step 1

Log in to the required Unified CCE component server.

Step 2

From the browser ( https://<FQDN of the Unified CCE component server> ), download the certificate.

If you want to regenerate RSA a certificate instead of using the existing certificate, run the following commands:

From the Cisco Unified CCE Tools folder, launch the SSL Encryption Utility .

Go to the Certificate Administration tab and click Uninstall .

Click Yes to confirm uninstallation of certificate.

A message is displayed upon successful uninstallation of the certificate.

Click Install to generate a new certificate.

If you wan to regenerate ECDSA certificate, run the following command from console sslutil -crtecdsabind .

Step 3

Copy the certificate to a location in the target server.

Step 4

Run the following command at the target server (machine terminal):

```
cd %CCE_JAVA_HOME%\bin
```

```
keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> -keystore <ICM install dir>\ssl\cacerts
```

Step 5

Enter the truststore password when prompted.

The default truststore password is changeit .

To change the truststore password, see Change Java Truststore Password .

Step 6

Go to Services and restart Apache Tomcat on target servers.

#### Import Diagnostic Framework Portico Certificate into AW Machines

Follow the steps below to Import Diagnostic Framework Portico Certificate for RSA or ECDSA

### SUMMARY STEPS

- Log in to the CCE component server.

- From the Unified CCE Tools, open the Diagnostic Framework Portico.

- Download the self-signed certificate from the browser.

- Copy the certificate to a location in AW Machine.

- Run the following command at the AW machine terminal:

- Enter the truststore password when prompted.

- Go to Services and restart Apache Tomcat.

### DETAILED STEPS

Step 1

Log in to the CCE component server.

Step 2

From the Unified CCE Tools, open the Diagnostic Framework Portico.

Step 3

Download the self-signed certificate from the browser.

Step 4

Copy the certificate to a location in AW Machine.

Step 5

Run the following command at the AW machine terminal:

```
cd %CCE_JAVA_HOME%\bin
```

```
keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> <FQDN of the CCE component Server> -keystore <ICM install dir>\ssl\cacerts
```

The alias name of the CCE component server must be different from the alias name given while creating the CCE component server's
                                                            self-signed certificate.

Step 6

Enter the truststore password when prompted.

The default truststore password is changeit .

To change the truststore password, see Change Java Truststore Password .

Step 7

Go to Services and restart Apache Tomcat.

#### Import ECE Web Server Certificate into AW Machines

If you do not have a CA certificate, you must import a self-signed certificate from the ECE web server to all AW machines . This will enable you to launch the ECE gadget in the Unified CCE Administration.

### SUMMARY STEPS

- From the ECE Web Server ( https://<ECE Web Server> ), download the certificate, and save the file to your desktop.

- Copy the certificate to a location in AW Machine.

- Run the following command at the AW machine terminal:

- Enter the truststore password when prompted.

- Go to Services and restart Apache Tomcat .

### DETAILED STEPS

Step 1

From the ECE Web Server ( https://<ECE Web Server> ), download the certificate, and save the file to your desktop.

Step 2

Copy the certificate to a location in AW Machine.

Step 3

Run the following command at the AW machine terminal:

```
cd %CCE_JAVA_HOME%\bin
```

```
keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> <FQDN of ECE Web Server> -keystore <ICM install dir>\ssl\cacerts
```

Step 4

Enter the truststore password when prompted.

The default truststore password is changeit .

To change the truststore password, see Change Java Truststore Password .

Step 5

Go to Services and restart Apache Tomcat .

#### Generate Self-signed WSM Certificate for CVP

This procedure is applicable if you don't have the CA certificate.

When you install CVP Call Server or Reporting Server , you must import the Web Service Manager (WSM) self-signed certificate into all AW machines. This will eliminate any browser
                                    warnings and establish HTTPS connection between CVP Call Server or Reporting Server and AW machine. Use Keytool to generate a Self-Signed Certificate.

Important

The certificate CommonName (CN) must match the Fully Qualified Domain Name (FQDN) provided for the CVP Call Server or Reporting Server in the Packaged CCE Inventory.

### SUMMARY STEPS

- Log into the CVP Call Server or Reporting Server .

- Delete the wsm certificate from the CVP keystore:

- Enter the keystore password when prompted. To identify the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

- Generate the self-signed certificate:

- Enter the key password for wsm certificate. Leave it blank to use the default keystore password.

- Restart the CVP Call Server or Reporting Server .

- Download the self-signed certificate from the browser ( https://FQDN of the CVP Server:8111/cvp-dp/rest/DiagnosticPortal/GetProductVersion ).

- Backup the cacerts files from both ICM and OpenJDK paths. You can copy them in a location in AW machine.

- Open a command window as Administrator to import CVP call server certificates into ICM and OpenJDK paths.

- Restart the AW machine.

### DETAILED STEPS

Step 1

Log into the CVP Call Server or Reporting Server .

Step 2

Delete the wsm certificate from the CVP keystore:

```
%CVP_HOME%\jre\bin\keytool.exe -delete -alias wsm_certificate -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS
```

Step 3

Enter the keystore password when prompted. To identify the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 4

Generate the self-signed certificate:

```
%CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias wsm_certificate -v -validity <duration in days> -keysize 2048 -keyalg RSA
```

The default duration for validity is 90 days.

```
Enter keystore password: <enter the keystore password>
What is your first and last name?.
 [Unknown]: <Specify the FQDN of the CVP server. For example: cvp-1a.example.com>
What is the name of your organizational unit?
 [Unknown]: <specify OU> E.g. CCBU
What is the name of your organization?
 [Unknown]: <specify the name of the org> E.g. CISCO
What is the name of your City or Locality?
 [Unknown]: <specify the name of the city/locality>  E.g. BLR
What is the name of your State or Province?
 [Unknown]: <specify the name of the state/province>  E.g. KAR
What is the two-letter country code for this unit?
 [Unknown]: <specify two-letter Country code>  E.g. IN
Specify ‘yes’ for the inputs.
```

Step 5

Enter the key password for wsm certificate. Leave it blank to use the default keystore password.

Step 6

Restart the CVP Call Server or Reporting Server .

Step 7

Download the self-signed certificate from the browser ( https://FQDN of the CVP Server:8111/cvp-dp/rest/DiagnosticPortal/GetProductVersion ).

Step 8

Backup the cacerts files from both ICM and OpenJDK paths. You can copy them in a location in AW machine.

ICM path: <ICM install directory>\ssl\

OpenJDK path: %CCE_JAVA_HOME%\lib\security\cacerts

Step 9

Open a command window as Administrator to import CVP call server certificates into ICM and OpenJDK paths.

Run the following commands:

```
cd %CCE_JAVA_HOME%\bin
keytool.exe –keystore <ICM install directory>\ssl\cacerts -trustcacerts -import -file <path where the CVP Call Server cert is> -alias CVPfqdn_wsm -storepass changeit
keytool.exe –keystore %CCE_JAVA_HOME%\lib\security\cacerts -trustcacerts -import -file <path where the CVP Call Server cert is> -alias CVPfqdn_wsm -storepass changeit
```

Step 10

Restart the AW machine.

### Import VOS Components Certificate

Important

The certificate CommonName (CN) must match the Fully Qualified Domain Name (FQDN) provided for the respective component servers
                                             in the Packaged CCE Inventory.

Follow the same steps while you import certificate for VOS component for RSA or
                                             ECDSA certificate .

### SUMMARY STEPS

- Sign in to the Cisco Unified Operating System Administration on the source component server using the URL ( https://<FQDN of the Component server>:8443/cmplatform 3 ).

- From the Security menu, select Certificate Management .

- Click Find .

- Do one of the following:

- Download the self-signed certificate that contains hostname of the primary server.

- Copy the certificate to a location in the target server.

- Run the following command as an administrator at the target server (machine terminal):

- Enter the truststore password when prompted.

- Go to Services and restart Apache Tomcat.

### DETAILED STEPS

Step 1

Sign in to the Cisco Unified Operating System Administration on the source component server using the URL ( https://<FQDN of the Component server>:8443/cmplatform 3 ).

Step 2

From the Security menu, select Certificate Management .

Step 3

Click Find .

Step 4

Do one of the following:

If the tomcat certificate for your server is not on the list, click Generate Self-signed . When the certificate generation is complete, reboot your server.

If the tomcat certificate for your server is on the list, click the certificate to select it. (Ensure that the certificate
                                                   you select includes the hostname for the server.)

For ECDSA interface download .pem from tomcat-trust
                                                            certificate with common name suffic with
                                                            -EC . In case of CTI interface connection with Finesse, use tomcat certificate .

Step 5

Download the self-signed certificate that contains hostname of the primary server.

Step 6

Copy the certificate to a location in the target server.

Step 7

Run the following command as an administrator at the target server (machine terminal):

```
cd %CCE_JAVA_HOME%\bin
```

```
keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> <FQDN of component Server> -keystore <ICM install directory>\ssl\cacerts
```

Step 8

Enter the truststore password when prompted.

The default truststore password is changeit .

To change the truststore password, see Change Java Truststore Password .

Step 9

Go to Services and restart Apache Tomcat.

| Note | To download certificates, refer to the respective browser documentation for
                                       instructions. |
|---|---|

| Note | Procedure for enabling ECDSA certificates, refer to the topic Enabling ECDSA for
                                       Unified CCE Solution at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
|---|---|

| Import CA Certificates to Target Server | Generate CA Certificates for the Source Component Server | Links |
|---|---|---|
| AW Machines | Unified CCE Components (Router, Logger1, Rogger2, PGs, AWs, and HDS |  |
| Customer Voice Portal (CVP) Call Server/CVP Reporting Server | Import WSM CA Certificate into CVP Import CA Certificate into AW Machines |
| Email and Chat (ECE) | See Enterprise Chat and Email Installation and Configuration Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/cisco-enterprise-chat-email/series.html |
| Cisco Finesse Primary and Secondary | Obtain and Upload a CA Certificate Deploy Certificate in Browsers Import CA Certificate into AW Machines |
| Cisco Unified Communications Manager (CUCM) Publisher and Subscriber | CA-Signed Certificate Import CA Certificate into AW Machines |
| Virtualized Voice Browser (VVB) | See Configuration Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-installation-and-configuration-guides-list.html |
| Cisco Unified Intelligence Center (CUIC) Publisher and Subscriber | Obtain and Upload Third-party CA Certificate Import CA Certificate into AW Machines |
| Cisco Identity Service (IdS) Publisher and Subscriber | From the IdS server, generate and download a Certificate Signing Requests (CSR). Obtain Root and Application certificates from the third-party vendor. Upload the appropriate certificates to the IdS server. For more information, see https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-configuration-examples-list.html . Ensure to perform the instructions in IdS server. |
| Cloud Connect Publisher and Subscriber | Obtain and Upload Third-party CA Certificate Import CA Certificate into AW Machines |
| Customer Collaboration Platform | See Security Guide for Cisco Unified ICM/Contact Center Enterprise at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-and-configuration-guides-list.html |
| Live Data Publisher and Subscriber | Obtain and Upload Third-party CA Certificate Import CA Certificate into AW Machines |
| PG | CUCM Publisher | CA-Signed Certificate |
| VOS components | Import VOS CA Certificate into PG |
| Logger | AW |  |
| Rogger |
| CVP | Import CA Certificate into Cisco Unified CVP |

| Step 1 | Log in to Windows and choose Control Panel > Administrative Tools > Internet Information Services (IIS) Manager . |
|---|---|
| Step 2 | In the Connections pane, click the server name. The server Home pane appears. |
| Step 3 | In the IIS area, double-click Server Certificates . |
| Step 4 | In the Actions pane, click Create Certificate Request . |
| Step 5 | In the Request Certificate dialog box, do the following: Specify the required information in the displayed fields and click Next . In the Cryptographic service provider drop-down list, leave the default setting. From the Bit length drop-down list, select 2048. |
| Step 6 | Specify a file name for the certificate request and click Finish . |

| Step 1 | In Windows, open the Server Manager . |
|---|---|
| Step 2 | In the Quick Start window, click Add Roles and Features . |
| Step 3 | In the Set Installation Type tab, select Role-based or feature-based installation , and then click Next . |
| Step 4 | In the Server Selection tab, select the destination server then click Next . |
| Step 5 | In the Server Roles tab, check the Active Directory Certificate Services box, and then click the Add Features button in the pop-up window. |
| Step 6 | In the Features and AD CS tabs, click Next to accept default values. |
| Step 7 | In the Role Services tab, verify that Certification Authority , Certification Authority Web Enrollment , Certificate Enrollment Web Service , and Certificate Enrollment Policy Web Service boxes are box is checked, and then click Next . |
| Step 8 | In the Confirmation tab, click Install . |
| Step 9 | After the installation is complete, click the Configure Active Directory Certificate Service on the destination server link. |
| Step 10 | Verify that the credentials are correct (for the domain Administrator user), and then click Next . |
| Step 11 | In the Role Services tab, check the Certification Authority , Certification Authority Web Enrollment , Certificate Enrollment Web Service , and Certificate Enrollment Policy Web Service boxes box , and then click Next . |
| Step 12 | In the Setup Type tab, select Enterprise CA , and then click Next . |
| Step 13 | In the CA Type tab, select Root CA , and then click Next . |
| Step 14 | In the Private Key , Cryptography , CA Name , Validity Period , and Certificate Database tabs, click Next to accept default values. |
| Step 15 | In the following tabs, leave the default values, and click Next . CA for CES Authentication Type for CES Service Account for CES Authentication Type for CEP |
| Step 16 | Review the information in the Confirmation tab, and then click Configure . |

| Step 1 | Log in to Windows and choose Control Panel > Administrative Tools > Internet Information Services (IIS) Manager . |
|---|---|
| Step 2 | In the Connections pane, click the server name. |
| Step 3 | In the IIS area, double-click Server Certificates . |
| Step 4 | In the Actions pane, click Complete Certificate Request . |
| Step 5 | In the Complete Certificate Request dialog box, complete the following fields: In the File name containing the certification authority's response field, click the … button. Browse to the location where signed certificate is stored and then click Open . In the Friendly name field, enter the FQDN of the server. |
| Step 6 | Click OK to upload the certificate. If the certificate upload is successful, the certificate appears in the Server Certificates pane. |

| Step 1 | Log in to Windows and choose Control Panel > Administrative Tools > Internet Information Services (IIS) Manager . |
|---|---|
| Step 2 | In the Connections pane, choose <server_name> > Sites > Default Web Site . |
| Step 3 | In the Actions pane, click Bindings... . |
| Step 4 | Click the type https with port 443, and then click Edit... . |
| Step 5 | From the SSL certificate drop-down list, select the uploaded signed Certificate Request. |
| Step 6 | Click OK . |
| Step 7 | Navigate to Start > Run > services.msc and restart the IIS Admin Service. If IIS is restarted successfully, certificate error warnings do not appear when the application is launched. |

| Step 1 | Open the command prompt. |
|---|---|
| Step 2 | Navigate to the Diagnostic Portico home folder using: cd <ICM install directory>:\icm\serviceability\diagnostics\bin |
| Step 3 | Remove the current certificate binding to the Diagnostic Portico tool using: DiagFwCertMgr /task:UnbindCert |
| Step 4 | Open the signed certificate and copy the hash content (without spaces) of the Thumbprint field. Run the following command: DiagFwCertMgr /task:BindCertFromStore /certhash:<hash_value> If certificate binding is successful, it displays "The certificate binding is VALID" message. |
| Step 5 | Validate if the certificate binding was successful using: DiagFwCertMgr /task:ValidateCertBinding Note DiagFwCertMgr uses port 7890 by default. If certificate binding is successful, it displays "The certificate binding is VALID" message. | Note | DiagFwCertMgr uses port 7890 by default. |
| Note | DiagFwCertMgr uses port 7890 by default. |
| Step 6 | Restart the Diagnostic Framework service by running the following command: sc stop "diagfwsvc" sc start "diagfwsvc" If Diagnostic Framework restarts successfully, certificate error warnings do not appear when the application is launched. |

| Note | DiagFwCertMgr uses port 7890 by default. |
|---|---|

| Step 1 | Enter the keystore password. To identify the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
|---|---|
| Step 2 | Remove the existing certificate by running %CVP_HOME%\jre\bin\keytool.exe -delete -alias wsm_certificate -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS . |
| Step 3 | Generate a new key pair for the alias with selected key size by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias wsm_certificate
                                             -v -validity <duration in days> -keysize 2048 -keyalg RSA . Enter keystore password: <enter the keystore password>
What is your first and last name?
 [Unknown]: <specify the FQDN of the CVP server. For example: cvp1a.example.com >
What is the name of your organizational unit?
 [Unknown]: <specify OU> E.g. CCBU
What is the name of your organization?
 [Unknown]: <specify the name of the org> E.g. CISCO
What is the name of your City or Locality?
 [Unknown]: <specify the name of the city/locality>  E.g. BLR
What is the name of your State or Province?
 [Unknown]: <specify the name of the state/province>  E.g. KAR
What is the two-letter country code for this unit?
 [Unknown]: <specify two-letter Country code>  E.g. IN
Specify ‘yes’ for the inputs. Note The default duration for validity is 90 days. | Note | The default duration for validity is 90 days. |
| Note | The default duration for validity is 90 days. |
| Step 4 | Generate the CSR certificate for the alias by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias wsm_certificate
                                             -file %CVP_HOME%\conf\security\wsm.csr and save it to a file (for example, wsm.csr ) . Note To ensure compatibility with RFC 5280-compliant browsers, each certificate must include Subject Alternative Name (SAN). This
                                                         can be accomplished by using the -ext parameter with SAN when generating the Certificate Signing Request (CSR). The -ext parameter
                                                         allows a user to define certificate extensions. The SAN can contain multiple comma separated values including fully qualified
                                                         domain name (FQDN) of the server as well as localhost. Supported SAN formats include: ip:192.168.0.1 dns:myserver.mydomain.com email:name@mydomain.com For example: -ext san=dns:mycvp.mydomain.com,dns:localhost | Note | To ensure compatibility with RFC 5280-compliant browsers, each certificate must include Subject Alternative Name (SAN). This
                                                         can be accomplished by using the -ext parameter with SAN when generating the Certificate Signing Request (CSR). The -ext parameter
                                                         allows a user to define certificate extensions. The SAN can contain multiple comma separated values including fully qualified
                                                         domain name (FQDN) of the server as well as localhost. Supported SAN formats include: ip:192.168.0.1 dns:myserver.mydomain.com email:name@mydomain.com For example: -ext san=dns:mycvp.mydomain.com,dns:localhost |
| Note | To ensure compatibility with RFC 5280-compliant browsers, each certificate must include Subject Alternative Name (SAN). This
                                                         can be accomplished by using the -ext parameter with SAN when generating the Certificate Signing Request (CSR). The -ext parameter
                                                         allows a user to define certificate extensions. The SAN can contain multiple comma separated values including fully qualified
                                                         domain name (FQDN) of the server as well as localhost. Supported SAN formats include: ip:192.168.0.1 dns:myserver.mydomain.com email:name@mydomain.com For example: -ext san=dns:mycvp.mydomain.com,dns:localhost |
| Step 5 | Enter the keystore password when prompted. |
| Step 6 | Download wsm.csr from CVP %CVP_HOME%\conf\security\ and sign it from CA. |
| Step 7 | Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\ |
| Step 8 | Install the root CA certificate by initially running the import root command %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                             root -file %CVP_HOME%\conf\security\<filename_of_root_cer> and then followed by running the import intermediate command %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                             intermediate_ca -file %CVP_HOME%\conf\security\<filename_of_intermediate_cer> |
| Step 9 | Enter the keystore password when prompted. |
| Step 10 | Install the signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -trustcacerts -alias
                                                wsm_certificate -file %CVP_HOME%\conf\security\<filename_of_wsm_CA_cer> . |
| Step 11 | Enter the keystore password when prompted. |
| Step 12 | Restart the Cisco CVP WebServicesManager service. |

| Note | The default duration for validity is 90 days. |
|---|---|

| Note | To ensure compatibility with RFC 5280-compliant browsers, each certificate must include Subject Alternative Name (SAN). This
                                                         can be accomplished by using the -ext parameter with SAN when generating the Certificate Signing Request (CSR). The -ext parameter
                                                         allows a user to define certificate extensions. The SAN can contain multiple comma separated values including fully qualified
                                                         domain name (FQDN) of the server as well as localhost. Supported SAN formats include: ip:192.168.0.1 dns:myserver.mydomain.com email:name@mydomain.com For example: -ext san=dns:mycvp.mydomain.com,dns:localhost |
|---|---|

| Step 1 | Enter the following command in the CLI to set the CUCM in the mixed mode, and to register the endpoints in the encrypted mode: admin: utils ctl set-cluster mixed-mode This operation will set the cluster to Mixed mode.  Auto-registration is enabled on at least one CM node. Do you want to continue? (y/n): y Moving Cluster to Mixed Mode
Cluster set to Mixed Mode
You must reset all phones to ensure they received the updated CTL file. 
You must restart Cisco CTIManager services on all the nodes in the cluster that have the service activated.
admin: |
|---|---|
| Step 2 | Choose CUCM Admin Page > System > Enterprise Parameters . Check if Cluster Security Mode is set to 1. |
| Step 3 | Set the minimum TLS version command from the CLI: admin: set tls client min-version 1.2 **WARNING** If you are lowering the TLS version it can lead to security issues **WARNING**

Do you really want to continue (yes/no)? y Run this command in the other nodes of the cluster.

Restart the system using the command 'utils system restart' for the changes to take effect

Command successful
admin: set tls ser admin: set tls server mi admin: set tls server min-version? Syntax:
set tls server min-version

admin: set tls server min-version 1.2 **WARNING** If you are lowering the TLS version it can lead to security issues **WARNING**

Do you really want to continue (yes/no)? y Run this command in the other nodes of the cluster.

Restart the system using the command 'utils system restart' for the changes to take effect

Command successful
admin: |
| Step 4 | Create an
                                          			 encrypted phone profile and the SIP trunk profile. Associate them with the
                                          			 phone and CUCM SIP trunk. |
| Step 5 | Go to System > Security > SIP Trunk Security Profile and create a new SIP trunk security profile. |
| Step 6 | On CUCM SIP Trunk, check the SRTP Allowed check box. |
| Step 7 | From SIP Trunk Security Profile drop-down list, choose TLS Secure Profile . |
| Step 8 | Restart the TFTP and Cisco CallManager services on all the nodes in the cluster that run these services. |
| Step 9 | Upload the root certificate generated from the CA to CUCM against CUCM-trust. |
| Step 10 | Generate the CSR against CallManager and select the key-length as 2048. |
| Step 11 | Sign the certificate on a CA https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-callmanager/118731-configure-san-00.html . |
| Step 12 | Click Upload
                                             				Certificate on CUCM by selecting the certificate name as CallManager . On successful
                                             				completion, CUCM displays the description as Certificate
                                                				  signed by <CA hostname> . |
| Step 13 | Restart TFTP
                                          			 and Cisco CallManager services on all the nodes in the cluster that run these
                                          			 services. |

| Step 1 | Log in to the AW-HDS-DDS Server. |
|---|---|
| Step 2 | Run the following command: cd %CCE_JAVA_HOME%\bin |
| Step 3 | Copy the Root or intermediate certificates to a location in AW Machine. |
| Step 4 | Remove the existing certificate by running the following command: keytool.exe -delete -alias <AW FQDN> -keystore <ICM install directory>\ssl\cacerts |
| Step 5 | Enter the truststore password when prompted. The default truststore password is changeit . Note To change the truststore password, see Change Java Truststore Password . | Note | To change the truststore password, see Change Java Truststore Password . |
| Note | To change the truststore password, see Change Java Truststore Password . |
| Step 6 | At the AW machine terminal, run the following command: cd %CCE_JAVA_HOME%\bin keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> <AW FQDN> -keystore <ICM install directory>\ssl\cacerts |
| Step 7 | Enter the truststore password when prompted. |
| Step 8 | Go to Services and restart Apache Tomcat. Note For more information, refer to Custom Truststore to Store Component
                                                            Certificate section. | Note | For more information, refer to Custom Truststore to Store Component
                                                            Certificate section. |
| Note | For more information, refer to Custom Truststore to Store Component
                                                            Certificate section. |

| Note | To change the truststore password, see Change Java Truststore Password . |
|---|---|

| Note | For more information, refer to Custom Truststore to Store Component
                                                            Certificate section. |
|---|---|

| Step 1 | Copy the CA certificate to a location in the PG server. |
|---|---|
| Step 2 | Run the following command as an administrator at the target server (machine terminal): Important If you are not employing the 12.5(1a) installer or not having ES55 (mandatory OpenJDK ES), then use JAVA_HOME instead of CCE_JAVA_HOME. cd % CCE_JAVA_HOME %\bin keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> -keystore <ICM install directory>\ssl\cacerts | Important | If you are not employing the 12.5(1a) installer or not having ES55 (mandatory OpenJDK ES), then use JAVA_HOME instead of CCE_JAVA_HOME. |
| Important | If you are not employing the 12.5(1a) installer or not having ES55 (mandatory OpenJDK ES), then use JAVA_HOME instead of CCE_JAVA_HOME. |
| Step 3 | Enter the truststore password when prompted. The default truststore password is changeit . Note To change the truststore password, see Change Java Truststore Password . | Note | To change the truststore password, see Change Java Truststore Password . |
| Note | To change the truststore password, see Change Java Truststore Password . |
| Step 4 | Go to Services and restart Apache Tomcat. |

| Important | If you are not employing the 12.5(1a) installer or not having ES55 (mandatory OpenJDK ES), then use JAVA_HOME instead of CCE_JAVA_HOME. |
|---|---|

| Note | To change the truststore password, see Change Java Truststore Password . |
|---|---|

| Step 1 | Log in to the Logger/Rogger Server. |
|---|---|
| Step 2 | Run the following command: Important If you are not employing the 12.5(1a) installer or not having ES55 (mandatory OpenJDK ES), then use JAVA_HOME instead of CCE_JAVA_HOME. cd % CCE_JAVA_HOME %\bin | Important | If you are not employing the 12.5(1a) installer or not having ES55 (mandatory OpenJDK ES), then use JAVA_HOME instead of CCE_JAVA_HOME. |
| Important | If you are not employing the 12.5(1a) installer or not having ES55 (mandatory OpenJDK ES), then use JAVA_HOME instead of CCE_JAVA_HOME. |
| Step 3 | Copy the Root or intermediate certificates to a location in Logger/Rogger VMs. |
| Step 4 | Remove the existing certificate by executing: keytool.exe -delete -alias <alias name>  -keystore <ICM install directory>\ssl\cacerts <ICM install directory>\ssl\cacerts |
| Step 5 | Enter the truststore password changeit when prompted. |
| Step 6 | At the Logger/Rogger machine terminal, run the following command: cd % CCE_JAVA_HOME %\bin keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> -keystore <ICM install directory>\ssl\cacerts <ICM install directory>\ssl\cacerts |
| Step 7 | Enter the truststore password when prompted. |
| Step 8 | Go to Services and restart Apache Tomcat. |

| Important | If you are not employing the 12.5(1a) installer or not having ES55 (mandatory OpenJDK ES), then use JAVA_HOME instead of CCE_JAVA_HOME. |
|---|---|

| Note | Follow the steps below to Import AW Certificate for RSA or ECDSA certificate at CVP and Unified CCE component. |
|---|---|

| Step 1 | Download Packaged CCE webadmin CA certificate to %CVP_HOME%\conf\security\ . |
|---|---|
| Step 2 | Import the certificate to the CVP Call Server keystore - %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                             AW_cert -file %CVP_HOME%\conf\security\<AW certificate> . |

| Note | To establish a secure communication, run the commands (given in the links below) in the Command Prompt as an Administrator
                                    (right click over the Command Prompt and select Run as administrator ). |
|---|---|

| Import Self-signed Certificates to Target Server | Generate Self-signed Certificates from Source Component Server | Links |
|---|---|---|
| AW Machines | Unified CCE Components (Router, Logger 1 , Rogger 2 , PGs, AWs, and HDS | Import Unified CCE Component Certificates Import Diagnostic Framework Portico Certificate into AWMachines |
| Customer Voice Portal (CVP) Call Server/CVP Reporting Server | Generate Self-signed WSM Certificate for CVP |
| Email and Chat (ECE) | Import ECE Web Server Certificate into AW Machines |
| Cisco Finesse Primary and Secondary | Import VOS Components Certificate |
| Cisco Unified Communications Manager (CUCM) Publisher and Subscriber |
| Virtualized Voice Browser (VVB) |
| Cisco Unified Intelligence Center (CUIC) Publisher and Subscriber |
| Cisco Identity Service (IdS) Publisher and Subscriber |
| Cloud Connect Publisher and Subscriber |
| Customer Collaboration Platform |
| Live Data Publisher and Subscriber |
| PG | CUCM Publisher | Import VOS Components Certificate |
| Logger | AW | Import Unified CCE Component Certificates |
| Rogger |
| CVP | Import AW Certificate into Cisco Unified CVP Servers |

| Step 1 | http://acrsrv-app-prd-01:8080/ Export the Call Server certificate by
                                          running. %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore
                                             %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                             callserver_certificate -file
                                             %CVP_HOME%\conf\security\<callserver_certificate> |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Restart the Call Server service to load the new certificates. |

| Step 1 | Copy the self-signed CVP Call Server certificate downloaded from CVP to the ICM box (PG) . |
|---|---|
| Step 2 | Open the command prompt and go to c:\icm\bin . |
| Step 3 | Type CiscoCertUtil.exe /install
                                             <callserver_certificate> . This imports the certificate to the Trusted Root Certification Authorities. Note Repeat the procedure for multiple PIMs and for Side A and Side B. | Note | Repeat the procedure for multiple PIMs and for Side A and Side B. |
| Note | Repeat the procedure for multiple PIMs and for Side A and Side B. |

| Note | Repeat the procedure for multiple PIMs and for Side A and Side B. |
|---|---|

| Step 1 | Log into the ICM (PG) box. Go to the command prompt and type CiscoCertUtil.exe /generatecert . C:\icm\bin>ciscocertutil.exe /generatecert SSL config path = C:\icm\ssl\cfg\openssl.cfg
SYSTEM command is C:\icm\ssl\bin\openssl.exe req -x509 -newkey rsa:2048 -days 7300 -nodes -subj /CN=PG-SIDEA.pcce.com -out
C:\icm\ssl\certs\host.pem -keyout C:\icm\ssl\keys\host.key
Generating a RSA private key
..................
....
writing new private key to 'C:\icm\ssl\keys\host.key The client certificate and key are generated and stored as host.csr and host.key in C:\icm\ssl\certs folder. |
|---|---|
| Step 2 | Cycle VRU PG. |

| Step 1 | Log into the CVP Call Server box. Create a folder and copy host.pem to c:\IcmCertificate . |
|---|---|
| Step 2 | From the command prompt, run %CVP_HOME%\jre\bin\keytool.exe -import -v -alias icm_certificate -storetype JCEKS -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore
                                             -file c:\IcmCertificate\host.pem . |
| Step 3 | Enter the keystore password when prompted. Click Yes . |
| Step 4 | Restart the Callserver service to load the new certificates. Note Repeat the procedure if you have multiple Call Servers. | Note | Repeat the procedure if you have multiple Call Servers. |
| Note | Repeat the procedure if you have multiple Call Servers. |

| Note | Repeat the procedure if you have multiple Call Servers. |
|---|---|

| Note | Follow the steps below to Import AW Certificate for RSA or ECDSA certificate at
                                             CVP and Unified CCE component. |
|---|---|

| Step 1 | Download Packaged CCE webadmin self-signed certificate to %CVP_HOME%\conf\security\ . |
|---|---|
| Step 2 | Import the certificate to the CVP Call Server keystore - %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                             AW_cert -file %CVP_HOME%\conf\security\<AW certificate> . |

| Important | The certificate CommonName (CN) must match the Fully Qualified Domain Name (FQDN) provided for the Unified CCE components
                                                in the Packaged Unified CCE Inventory. |
|---|---|

| Step 1 | Log in to the required Unified CCE component server. |
|---|---|
| Step 2 | From the browser ( https://<FQDN of the Unified CCE component server> ), download the certificate. If you want to regenerate RSA a certificate instead of using the existing certificate, run the following commands: From the Cisco Unified CCE Tools folder, launch the SSL Encryption Utility . Go to the Certificate Administration tab and click Uninstall . Click Yes to confirm uninstallation of certificate. A message is displayed upon successful uninstallation of the certificate. Click Install to generate a new certificate. If you wan to regenerate ECDSA certificate, run the following command from console sslutil -crtecdsabind . |
| Step 3 | Copy the certificate to a location in the target server. |
| Step 4 | Run the following command at the target server (machine terminal): cd %CCE_JAVA_HOME%\bin keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> -keystore <ICM install dir>\ssl\cacerts |
| Step 5 | Enter the truststore password when prompted. The default truststore password is changeit . Note To change the truststore password, see Change Java Truststore Password . | Note | To change the truststore password, see Change Java Truststore Password . |
| Note | To change the truststore password, see Change Java Truststore Password . |
| Step 6 | Go to Services and restart Apache Tomcat on target servers. |

| Note | To change the truststore password, see Change Java Truststore Password . |
|---|---|

| Note | Follow the steps below to Import Diagnostic Framework Portico Certificate for RSA or ECDSA |
|---|---|

| Step 1 | Log in to the CCE component server. |
|---|---|
| Step 2 | From the Unified CCE Tools, open the Diagnostic Framework Portico. |
| Step 3 | Download the self-signed certificate from the browser. |
| Step 4 | Copy the certificate to a location in AW Machine. |
| Step 5 | Run the following command at the AW machine terminal: cd %CCE_JAVA_HOME%\bin keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> <FQDN of the CCE component Server> -keystore <ICM install dir>\ssl\cacerts Note The alias name of the CCE component server must be different from the alias name given while creating the CCE component server's
                                                            self-signed certificate. | Note | The alias name of the CCE component server must be different from the alias name given while creating the CCE component server's
                                                            self-signed certificate. |
| Note | The alias name of the CCE component server must be different from the alias name given while creating the CCE component server's
                                                            self-signed certificate. |
| Step 6 | Enter the truststore password when prompted. The default truststore password is changeit . Note To change the truststore password, see Change Java Truststore Password . | Note | To change the truststore password, see Change Java Truststore Password . |
| Note | To change the truststore password, see Change Java Truststore Password . |
| Step 7 | Go to Services and restart Apache Tomcat. |

| Note | The alias name of the CCE component server must be different from the alias name given while creating the CCE component server's
                                                            self-signed certificate. |
|---|---|

| Note | To change the truststore password, see Change Java Truststore Password . |
|---|---|

| Step 1 | From the ECE Web Server ( https://<ECE Web Server> ), download the certificate, and save the file to your desktop. |
|---|---|
| Step 2 | Copy the certificate to a location in AW Machine. |
| Step 3 | Run the following command at the AW machine terminal: cd %CCE_JAVA_HOME%\bin keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> <FQDN of ECE Web Server> -keystore <ICM install dir>\ssl\cacerts |
| Step 4 | Enter the truststore password when prompted. The default truststore password is changeit . Note To change the truststore password, see Change Java Truststore Password . | Note | To change the truststore password, see Change Java Truststore Password . |
| Note | To change the truststore password, see Change Java Truststore Password . |
| Step 5 | Go to Services and restart Apache Tomcat . |

| Note | To change the truststore password, see Change Java Truststore Password . |
|---|---|

| Note | This procedure is applicable if you don't have the CA certificate. |
|---|---|

| Important | The certificate CommonName (CN) must match the Fully Qualified Domain Name (FQDN) provided for the CVP Call Server or Reporting Server in the Packaged CCE Inventory. |
|---|---|

| Step 1 | Log into the CVP Call Server or Reporting Server . |
|---|---|
| Step 2 | Delete the wsm certificate from the CVP keystore: %CVP_HOME%\jre\bin\keytool.exe -delete -alias wsm_certificate -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS |
| Step 3 | Enter the keystore password when prompted. To identify the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
| Step 4 | Generate the self-signed certificate: %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias wsm_certificate -v -validity <duration in days> -keysize 2048 -keyalg RSA Note The default duration for validity is 90 days. Enter keystore password: <enter the keystore password>
What is your first and last name?.
 [Unknown]: <Specify the FQDN of the CVP server. For example: cvp-1a.example.com>
What is the name of your organizational unit?
 [Unknown]: <specify OU> E.g. CCBU
What is the name of your organization?
 [Unknown]: <specify the name of the org> E.g. CISCO
What is the name of your City or Locality?
 [Unknown]: <specify the name of the city/locality>  E.g. BLR
What is the name of your State or Province?
 [Unknown]: <specify the name of the state/province>  E.g. KAR
What is the two-letter country code for this unit?
 [Unknown]: <specify two-letter Country code>  E.g. IN
Specify ‘yes’ for the inputs. | Note | The default duration for validity is 90 days. |
| Note | The default duration for validity is 90 days. |
| Step 5 | Enter the key password for wsm certificate. Leave it blank to use the default keystore password. |
| Step 6 | Restart the CVP Call Server or Reporting Server . |
| Step 7 | Download the self-signed certificate from the browser ( https://FQDN of the CVP Server:8111/cvp-dp/rest/DiagnosticPortal/GetProductVersion ). |
| Step 8 | Backup the cacerts files from both ICM and OpenJDK paths. You can copy them in a location in AW machine. ICM path: <ICM install directory>\ssl\ OpenJDK path: %CCE_JAVA_HOME%\lib\security\cacerts |
| Step 9 | Open a command window as Administrator to import CVP call server certificates into ICM and OpenJDK paths. Run the following commands: cd %CCE_JAVA_HOME%\bin
keytool.exe –keystore <ICM install directory>\ssl\cacerts -trustcacerts -import -file <path where the CVP Call Server cert is> -alias CVPfqdn_wsm -storepass changeit
keytool.exe –keystore %CCE_JAVA_HOME%\lib\security\cacerts -trustcacerts -import -file <path where the CVP Call Server cert is> -alias CVPfqdn_wsm -storepass changeit |
| Step 10 | Restart the AW machine. |

| Note | The default duration for validity is 90 days. |
|---|---|

| Important | The certificate CommonName (CN) must match the Fully Qualified Domain Name (FQDN) provided for the respective component servers
                                             in the Packaged CCE Inventory. |
|---|---|

| Note | Follow the same steps while you import certificate for VOS component for RSA or
                                             ECDSA certificate . |
|---|---|

| Step 1 | Sign in to the Cisco Unified Operating System Administration on the source component server using the URL ( https://<FQDN of the Component server>:8443/cmplatform 3 ). |
|---|---|
| Step 2 | From the Security menu, select Certificate Management . |
| Step 3 | Click Find . |
| Step 4 | Do one of the following: If the tomcat certificate for your server is not on the list, click Generate Self-signed . When the certificate generation is complete, reboot your server. If the tomcat certificate for your server is on the list, click the certificate to select it. (Ensure that the certificate
                                                   you select includes the hostname for the server.) Note For ECDSA interface download .pem from tomcat-trust
                                                            certificate with common name suffic with
                                                            -EC . In case of CTI interface connection with Finesse, use tomcat certificate . | Note | For ECDSA interface download .pem from tomcat-trust
                                                            certificate with common name suffic with
                                                            -EC . In case of CTI interface connection with Finesse, use tomcat certificate . |
| Note | For ECDSA interface download .pem from tomcat-trust
                                                            certificate with common name suffic with
                                                            -EC . In case of CTI interface connection with Finesse, use tomcat certificate . |
| Step 5 | Download the self-signed certificate that contains hostname of the primary server. |
| Step 6 | Copy the certificate to a location in the target server. |
| Step 7 | Run the following command as an administrator at the target server (machine terminal): cd %CCE_JAVA_HOME%\bin keytool.exe -import -file <certificate with fully qualified path> -alias <alias name> <FQDN of component Server> -keystore <ICM install directory>\ssl\cacerts |
| Step 8 | Enter the truststore password when prompted. The default truststore password is changeit . Note To change the truststore password, see Change Java Truststore Password . | Note | To change the truststore password, see Change Java Truststore Password . |
| Note | To change the truststore password, see Change Java Truststore Password . |
| Step 9 | Go to Services and restart Apache Tomcat. |

| Note | For ECDSA interface download .pem from tomcat-trust
                                                            certificate with common name suffic with
                                                            -EC . In case of CTI interface connection with Finesse, use tomcat certificate . |
|---|---|

| Note | To change the truststore password, see Change Java Truststore Password . |
|---|---|