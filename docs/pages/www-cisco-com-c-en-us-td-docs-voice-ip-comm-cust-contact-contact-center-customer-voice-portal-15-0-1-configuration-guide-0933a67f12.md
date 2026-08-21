---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-configuration-guide-0933a67f12
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/configuration/guide/ccvp_b_150-configuration-guide-for-cisco-unified-customer-voice-portal/unified_cvp_security.html
retrieved_at: 2026-08-21T02:59:25.606982+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: March 5, 2025

Chapter: Unified CVP
	 Security

## Chapter: Unified CVP
	 Security

# Unified CVP
                     	 Security

This chapter describes security considerations for Unified CVP call flow model deployments.

This release supports only TLS 1.2. For more information, see Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/tsd-products-support-series-home.html .

To configure TLS Cipher on CVP server , see TLS Cipher Configuration .

As per security guidelines, limit the validity of the generated or the requested SSL certificates to 2-3 years or shorter.

If you are testing with the self-signed TLS certificates that are generated as a part of the installation, ensure that you
                                          map the CN/SANs on the certificate to the corresponding IP through DNS or hosts file entries.

For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Ensure that the common name of the certificate matches the Fully Qualified Domain Name (FQDN) or hostname of the machine.

## Secure JMX Communication between CVP Components

You can secure JMX communication by:

Exchanging the
                                 			 self-signed certificates between the components.

Signing the
                                 			 certificates by a Certificate Authority.

### Self-Signed Certificates

#### On Call Server or VXML Server or Reporting Server

Step 1

Import the certificate to the callserver keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                wsm_oamp_certificate -file %CVP_HOME%\conf\security\<oamp_security.cer> .

Step 2

Enter the keystore password when prompted.

Step 3

Restart the Operation Console Server and the Call Server.

#### On OAMP

Log in to the Operations Console Server. Retrieve the keystore password from the security.properties file.

At the command prompt, enter more %CVP_HOME%\conf\security.properties .

Security.keystorePW = <Returns the keystore password>

Enter the keystore password when prompted.

Step 1

Export the OAMP certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\<oamp_security.cer> .

Step 2

Enter the keystore password when prompted.

Step 3

Copy the WSM certificate you exported from the Call Server/VXML Server/Reporting Server to %CVP_HOME%\conf\security\ and import the certificate to the callserver key store by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                oamp_wsm_certificate -file %CVP_HOME%\conf\security\<wsm_security.cer> .

Step 4

Enter the keystore password when prompted.

#### On Call Server or VXML Server or Reporting Server

Log in to the Call Server or VXML Server or Reporting Server. Retrieve the keystore password from the security.properties file.

At the command prompt, enter more %CVP_HOME%\conf\security.properties .

Security.keystorePW = <Returns the keystore password>

Enter the keystore password when prompted.

Step 1

Export the WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias wsm_certificate
                                                -file %CVP_HOME%\conf\security\<wsm_security.cer> .

Step 2

Enter the keystore password when prompted.

Step 3

Copy the OAMP certificate exported from the OAMP to %CVP_HOME%\conf\security\ and import the certificate to the callserver keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                wsm_oamp_certificate -file %CVP_HOME%\conf\security\<oamp_security.cer> .

Step 4

Enter the keystore password when prompted.

Step 5

Import the WSM certificate into the call server keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                vxml_wsm_certificate -file %CVP_HOME%\conf\security\<wsm_security.cer> .

Step 6

Enter the keystore password when prompted.

Repeat the preceding steps for the Call Server, VXML Server, and Reporting Server.

To enable Courtesy Callback feature in the secure mode, you must exchange the Call Server and Reporting Server certificates
                                                and place the certificates in %CVP_HOME%\conf\security\.keystore of each server.

#### On Call Server or VXML Server or Reporting Server

Log in to the CVP/Reporting Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 1

Export the following certificates:

WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias wsm_certificate
                                                      -file %CVP_HOME%\conf\security\wsm_security.cer

Call Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias callserver_certificate
                                                      -file %CVP_HOME%\conf\security\callserver_security.cer

VXML Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias vxml_certificate
                                                      -file %CVP_HOME%\conf\security\vxml_security.cer

VXML certificate is not applicable for Reporting Server.

Step 2

Enter the keystore password when prompted.

Step 3

Copy all the generated certificates from the %CVP_HOME%\conf\security\ folder of the Call/VXML/Reporting Server machine to the %CVP_HOME%\conf\security\ folder on the OAMP machine.

Step 4

On the OAMP machine, export the OAMP Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\oamp_security.cer

Step 5

Enter the keystore password when prompted.

Step 6

Copy the generated OAMP Server certificate from the %CVP_HOME%\conf\security\ folder of the OAMP machine to the %CVP_HOME%\conf\security\ folder of the CVP/Reporting Server machine.

Step 7

On the CVP/Reporting Server machine, import the OAMP Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                oamp_certificate -file %CVP_HOME%\conf\security\oamp_security.cer

Step 8

Enter the keystore password when prompted.

Step 9

Trust this certificate? [no]: yes

Step 10

Configure WSM in CVP:

Go to c:\cisco\cvp\conf\jmx_wsm.conf

Add or update the file as shown and save it:

```
javax.net.debug = all
com.sun.management.jmxremote.ssl.need.client.auth= false com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=2099
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=3000 javax.net.ssl.keyStore= C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword= <keystore_password>
```

Step 11

Run the regedit command.

Append the following to the file at: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\Webservices Manager\Parameters\Java

The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore

```
Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
Djavax.net.ssl.trustStorePassword=<keystore_password> 
Djavax.net.ssl.trustStoreType=JCEKS
```

Step 12

Configure JMX of callserver in CVP.

Go to c:\cisco\cvp\conf\jmx_callserver.conf .

Update the file as shown and save the file:

```
com.sun.management.jmxremote.ssl.need.client.auth= false com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=2098
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=2097 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore_password>
```

Step 13

Configure JMX of VXMLServer in CVP.

Go to c:\cisco\cvp\conf\jmx_vxml.conf .

Edit the file as shown and save the file:

```
com.sun.management.jmxremote.ssl.need.client.auth= false com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=9696
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=9697 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore_password>
```

Step 14

Run the regedit command.

Append the following to the file at: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\VXML\Parameters\Java

The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore

```
Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
Djavax.net.ssl.trustStorePassword=<keystore_password> 
Djavax.net.ssl.trustStoreType=JCEKS
```

Step 15

Restart the Operation Console Server and the Call Server machines.

#### On OAMP

Log in to the Operations Console Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 1

Import the following certificates:

WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                      oamp_wsm_certificate -file %CVP_HOME%\conf\security\wsm_security.cer

Call Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                      oamp_callserver_certificate -file %CVP_HOME%\conf\security\callserver_security.cer

VXML Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                      oamp_vxml_certificate -file %CVP_HOME%\conf\security\vxml_security.cer

Step 2

Enter the keystore password when prompted.

Step 3

Trust this certificate? [no]: yes

Step 4

Restart OAMP service.

Step 5

Log into OAMP. To enable secure communication between OAMP and Call Server or VXML Server or Reporting Server, navigate to Device Management > Call Server . Check the Enable secure communication with the Ops console check box. Save and deploy both Call Server and VXML Server.

### CA-Signed Certificates

#### On OAMP

Log in to the Operations Console Server. Retrieve the keystore password from the security.properties file.

At the command prompt, enter more %CVP_HOME%\conf\security.properties

Security.keystorePW = <Returns the keystore password>

Enter the keystore password when prompted.

Step 1

Generate CSR on OAMP by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\oamp.csr

Step 2

Enter the keystore password when prompted.

Step 3

Sign the certificate on a CA.

Step 4

Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\

Step 5

Import the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                root -file %CVP_HOME%\conf\security\<filename_of_root_cert>

Step 6

Enter the keystore password when prompted.

Step 7

Import the CA-signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                oamp_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert>

Step 8

Run the regedit command:

Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\OPSConsoleServer\Parameters\Java\Options

The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                            that the required trust certificates are imported into the appropriate keystore

```
-Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore
-Djavax.net.ssl.trustStorePassword=<keystore_password>
-Djavax.net.ssl.trustStoreType=JCEKS
```

#### On Call Server/VXML Server/Reporting Server/WSM Server

Log in to the Call Server or VXML Server or Reporting Server or WSM Server. Retrieve the keystore password from the security.properties file.

At the command prompt, enter more %CVP_HOME%\conf\security.properties

Security.keystorePW = <Returns the keystore password>

Enter the keystore password when prompted.

Step 1

Generate CSR on Call Server by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias callserver_certificate
                                                -file %CVP_HOME%\conf\security\callserver.csr

Step 2

Repeat Step 1 for VXML Server, Reporting Server, and WSM Server.

Step 3

Sign the certificate on a CA.

Step 4

Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\

Step 5

Import the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                root -file %CVP_HOME%\conf\security\<filename_of_root_cert>

Step 6

Enter the keystore password when prompted.

Step 7

Import the CA-signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                callserver_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert>

Step 8

Repeat Step 7 for VXML Server, Reporting Server, and WSM Server.

Step 9

Configure WSM in CVP:

Go to c:/cisco/cvp/conf/jmx_wsm.conf

Add or update the file as shown and save it:

```
javax.net.debug = all
com.sun.management.jmxremote.ssl.need.client.auth = true com.sun.management.jmxremote.authenticate = false
com.sun.management.jmxremote.port = 2099
com.sun.management.jmxremote.ssl = true com.sun.management.jmxremote.rmi.port = 3000 javax.net.ssl.keyStore= C:/Cisco/CVP/conf/security/.keystore
javax.net.ssl.keyStorePassword= <keystore_password>
```

Step 10

Configure JMX of callserver in CVP:

Go to c:/cisco/cvp/conf/jmx_callserver.conf

Update the file as shown and save the file:

```
com.sun.management.jmxremote.ssl.need.client.auth = true com.sun.management.jmxremote.authenticate = false
com.sun.management.jmxremote.port = 2098
com.sun.management.jmxremote.ssl = true com.sun.management.jmxremote.rmi.port = 2097 javax.net.ssl.keyStore= C:/Cisco/CVP/conf/security/.keystore
javax.net.ssl.keyStorePassword= <keystore_password>
```

Run the regedit command.

Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\WebServicesManager\Parameters\Java\Options.

Append the following to the file:

The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore

```
-Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
-Djavax.net.ssl.trustStorePassword=<keystore_password> 
-Djavax.net.ssl.trustStoreType=JCEKS
```

Step 11

Configure JMX of VXMLServer in CVP:

Go to c:/cisco/cvp/conf/jmx_vxml.conf

Edit the file as shown and save the file:

```
com.sun.management.jmxremote.ssl.need.client.auth = true com.sun.management.jmxremote.authenticate = false
com.sun.management.jmxremote.port = 9696
com.sun.management.jmxremote.ssl = true com.sun.management.jmxremote.rmi.port = 9697 javax.net.ssl.keyStore = C:/Cisco/CVP/conf/security/.keystore
javax.net.ssl.keyStorePassword = <keystore_password>
```

Step 12

Restart the Operation Console Server and the CVP server.

To enable Courtesy Callback feature in the secure mode, add the CA root certificate to Tomcat truststore .keystore in %CVP_HOME%\jre\bin>keytool.exe -keystore%CVP_HOME%\conf\\security\.keystore -storepass changeit -importcert -file %CVP_HOME%\conf\security\CA_Root.cer

Step 13

Repeat the steps for Call Server, VXML Server, and Reporting Server.

## Secure JMX Communication between OAMP and Call Server using Mutual Authentication

You can secure JMX communication by:

Exchanging the CA-signed certificates between the components.

Signing the certificates by a Certificate Authority.

### Self-Signed Certificates

#### On Call Server or VXML Server or Reporting Server

Step 1

Import the certificate to the callserver keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                wsm_oamp_certificate -file %CVP_HOME%\conf\security\<oamp_security.cer> .

Step 2

Enter the keystore password when prompted.

Step 3

Restart the Operation Console Server and the Call Server.

#### On OAMP

Log in to the Operations Console Server. Retrieve the keystore password from the security.properties file.

At the command prompt, enter more %CVP_HOME%\conf\security.properties .

Security.keystorePW = <Returns the keystore password>

Enter the keystore password when prompted.

Step 1

Export the OAMP certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\<oamp_security.cer> .

Step 2

Enter the keystore password when prompted.

Step 3

Copy the WSM certificate you exported from the Call Server/VXML Server/Reporting Server to %CVP_HOME%\conf\security\ and import the certificate to the callserver key store by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                oamp_wsm_certificate -file %CVP_HOME%\conf\security\<wsm_security.cer> .

Step 4

Enter the keystore password when prompted.

#### On Call Server or VXML Server or Reporting Server

Log in to the Call Server or VXML Server or Reporting Server. Retrieve the keystore password from the security.properties file.

At the command prompt, enter more %CVP_HOME%\conf\security.properties .

Security.keystorePW = <Returns the keystore password>

Enter the keystore password when prompted.

Step 1

Export the WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias wsm_certificate
                                                -file %CVP_HOME%\conf\security\<wsm_security.cer> .

Step 2

Enter the keystore password when prompted.

Step 3

Copy the OAMP certificate exported from the OAMP to %CVP_HOME%\conf\security\ and import the certificate to the callserver keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                wsm_oamp_certificate -file %CVP_HOME%\conf\security\<oamp_security.cer> .

Step 4

Enter the keystore password when prompted.

Step 5

Import the WSM certificate into the call server keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                vxml_wsm_certificate -file %CVP_HOME%\conf\security\<wsm_security.cer> .

Step 6

Enter the keystore password when prompted.

Repeat the preceding steps for the Call Server, VXML Server, and Reporting Server.

To enable Courtesy Callback feature in the secure mode, you must exchange the Call Server and Reporting Server certificates
                                                and place the certificates in %CVP_HOME%\conf\security\.keystore of each server.

#### On Call Server or VXML Server or Reporting Server

Log in to the CVP/Reporting Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 1

Export the following certificates:

WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias wsm_certificate
                                                      -file %CVP_HOME%\conf\security\wsm_security.cer

Call Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias callserver_certificate
                                                      -file %CVP_HOME%\conf\security\callserver_security.cer

VXML Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias vxml_certificate
                                                      -file %CVP_HOME%\conf\security\vxml_security.cer

VXML certificate is not applicable for Reporting Server.

Step 2

Enter the keystore password when prompted.

Step 3

Copy all the generated certificates from the %CVP_HOME%\conf\security\ folder of the Call/VXML/Reporting Server machine to the %CVP_HOME%\conf\security\ folder on the OAMP machine.

Step 4

On the OAMP machine, export the OAMP Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\oamp_security.cer

Step 5

Enter the keystore password when prompted.

Step 6

Copy the generated OAMP Server certificate from the %CVP_HOME%\conf\security\ folder of the OAMP machine to the %CVP_HOME%\conf\security\ folder of the CVP/Reporting Server machine.

Step 7

On the CVP/Reporting Server machine, import the OAMP Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                oamp_certificate -file %CVP_HOME%\conf\security\oamp_security.cer

Step 8

Enter the keystore password when prompted.

Step 9

Trust this certificate? [no]: yes

Step 10

Configure WSM in CVP:

Go to c:\cisco\cvp\conf\jmx_wsm.conf

Add or update the file as shown and save it:

```
javax.net.debug = all
com.sun.management.jmxremote.ssl.need.client.auth= false com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=2099
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=3000 javax.net.ssl.keyStore= C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword= <keystore_password>
```

Step 11

Run the regedit command.

Append the following to the file at: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\Webservices Manager\Parameters\Java

The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore

```
Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
Djavax.net.ssl.trustStorePassword=<keystore_password> 
Djavax.net.ssl.trustStoreType=JCEKS
```

Step 12

Configure JMX of callserver in CVP.

Go to c:\cisco\cvp\conf\jmx_callserver.conf .

Update the file as shown and save the file:

```
com.sun.management.jmxremote.ssl.need.client.auth= false com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=2098
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=2097 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore_password>
```

Step 13

Configure JMX of VXMLServer in CVP.

Go to c:\cisco\cvp\conf\jmx_vxml.conf .

Edit the file as shown and save the file:

```
com.sun.management.jmxremote.ssl.need.client.auth= false com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=9696
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=9697 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore_password>
```

Step 14

Run the regedit command.

Append the following to the file at: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\VXML\Parameters\Java

The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore

```
Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
Djavax.net.ssl.trustStorePassword=<keystore_password> 
Djavax.net.ssl.trustStoreType=JCEKS
```

Step 15

Restart the Operation Console Server and the Call Server machines.

#### On OAMP

Log in to the Operations Console Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 1

Import the following certificates:

WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                      oamp_wsm_certificate -file %CVP_HOME%\conf\security\wsm_security.cer

Call Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                      oamp_callserver_certificate -file %CVP_HOME%\conf\security\callserver_security.cer

VXML Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                      oamp_vxml_certificate -file %CVP_HOME%\conf\security\vxml_security.cer

Step 2

Enter the keystore password when prompted.

Step 3

Trust this certificate? [no]: yes

Step 4

Restart OAMP service.

Step 5

Log into OAMP. To enable secure communication between OAMP and Call Server or VXML Server or Reporting Server, navigate to Device Management > Call Server . Check the Enable secure communication with the Ops console check box. Save and deploy both Call Server and VXML Server.

### Generate CA-Signed Certificate for WSM Service in Call Server/VXML Server/Reporting Server

Log into the Call Server or VXML Server or Reporting Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 1

Go to %CVP_HOME%\conf\security and delete the WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -delete -alias wsm_certificate . Enter the keystore password when prompted.

Step 2

Repeat Step 1 for Call Server certificate ( callserver_certificate ) and VXML Server certificate ( vxml_certificate ) on the CVP Server and Call Server Certificate ( callserver_certificate ) on the Reporting Server.

Step 3

Generate a CA-signed certificate for WSM server by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias wsm_certificate
                                                -v -keysize 2048 -keyalg RSA .

Enter the keystore password when prompted.

Enter the details at the prompts and type Yes to confirm.

Note the CN name for future reference.

Step 4

Generate the certificate request for the alias by running the following command and saving it to a file (for example, wsm.csr ): %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias wsm_certificate
                                                -file %CVP_HOME%\conf\security\wsm.csr .

Enter the keystore password when prompted.

Step 5

Get the certificate signed by a CA. Use the procedure to create a CA-signed certificate with the CA authority and ensure to
                                          use a Client-Server Certificate Authentication template when the CA generate the signed certificate.

Step 6

Download the signed certificate, the root and intermediate certificate of the CA authority.

Step 7

Copy the root, intermediate, and the CA-signed WSM  to %CVP_HOME%\conf\security\ .

Step 8

Import the root certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                root -file %CVP_HOME%\conf\security\<filename_of_root_cer> .

Enter the keystore password when prompted.

At Trust this certificate prompt, type Yes .

Step 9

Import the intermediate certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                intermediate -file %CVP_HOME%\conf\security\<filename_of_intermediate_cer> .

Enter the keystore password when prompted.

At Trust this certificate prompt, type Yes .

Step 10

Import the CA-signed WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                wsm_certificate -file %CVP_HOME%\conf\security\<filename_of_your_signed_cert_from_CA> .

Enter the keystore password when prompted.

Step 11

Repeat Step 3 to 10 (root and intermediate certificates do not need to be imported twice), for Call Server and VXML Server certificates on the
                                          CVP Server and Call Server certificate on the Reporting Server.

Step 12

Configure WSM in CVP Server and CVP Reporting Server :

Go to c:\cisco\cvp\conf\jmx_wsm.conf

```
javax.net.debug = all
com.sun.management.jmxremote.ssl.need.client.auth= true com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=2099
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=3000 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore_password >
javax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
javax.net.ssl.trustStorePassword=<keystore_password >
javax.net.ssl.trustStoreType=JCEKS
```

Run the regedit command.

Append the following to the file at HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\WebServicesManager\Parameters\Java :

The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore

```
Append this to the file at HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\WebServicesManager\Parameters\Java:

-Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
-Djavax.net.ssl.trustStorePassword=<keystore_password> 
-Djavax.net.ssl.trustStoreType=JCEKS
```

Step 13

Configure JMX of callserver in CVP Server and CVP Reporting Server :

Go to c:\cisco\cvp\conf\jmx_callserver.conf

Update the file as shown and save the file:

```
com.sun.management.jmxremote.ssl.need.client.auth= true com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=2098
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=2097 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore password>
javax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
javax.net.ssl.trustStorePassword=<keystore_password >
javax.net.ssl.trustStoreType=JCEKS
```

Step 14

Configure JMX of VXMLServer in CVP server:

Go to c:\cisco\cvp\conf\jmx_vxml.conf

Edit the file as shown and save the file:

```
com.sun.management.jmxremote.ssl.need.client.auth= true com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=9696
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=9697 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore password>
```

Run the regedit command.

Append the following to the file at HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\VXMLServer\Parameters\Java :

The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore

```
Append theese to the file at HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\VXMLServer\Parameters\Java:

-Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
-Djavax.net.ssl.trustStorePassword=<keystore_password> 
-Djavax.net.ssl.trustStoreType=JCEKS
```

Restart WSM service, Call Server and VXML Server services on CVP server and WSM Service and Call Server service on Reporting
                                                Server.

When secure communication is enabled with JMX, it forces the keystore to be %CVP_HOME%\conf\security\.keystore , instead of %CVP_HOME%\jre\lib\security\cacerts .

Therefore, the certificates from %CVP_HOME%\jre\lib\security\cacerts should be imported to %CVP_HOME%\conf\security\.keystore .

### Generate CA-Signed Client Certificate for WSM

Log in to the CVP or Reporting Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 1

Go to %CVP_HOME%\conf\security and generate a CA-signed certificate for client authentication with callserver by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias <CN of CVP
                                                Server or Reporting Server WSM certificate> -v -keysize 2048 -keyalg RSA

Enter the keystore password when prompted.

Enter the details at the prompts and type Yes to confirm.

The alias will be the same as the CN used for generating WSM certificate.

Step 2

Generate the certificate request for the alias by running the following command and saving it to a file (for example, jmx_client.csr ): %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias <CN of CVP Server
                                                or Reporting Server WSM certificate> -file %CVP_HOME%\conf\security\jmx_client.csr

Enter the keystore password when prompted.

Verify that the CSR was generated successfully by running dir jmx_client.csr

Step 3

Sign the JMX Client Certificate on a CA.

Use the procedure to create a CA-signed certificate with the CA authority. Download the CA-signed JMX Client certificate (Root
                                                         and intermediate certificates are not required since they were downloaded and imported previously).

Step 4

Copy the CA-signed JMX Client certificate to %CVP_HOME%\conf\security\ .

Step 5

Import the CA-signed JMX Client certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                <CN of CVP Server or Reporting Server WSM certificate> -file %CVP_HOME%\conf\security\<filename of CA-signed JMX Client certificate>

Enter the keystore password when prompted.

Step 6

Restart Cisco CVP Call Server, VXML Server, and WSM services.

Repeat the same procedure for Reporting Server, if any.

### Generate CA-Signed Client Certificate for OAMP (to be done on OAMP)

Step 1

Go to %CVP_HOME%\conf\security and generate a CA-signed certificate for client authentication with callserver WSM by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias <CN of CVP
                                             Server or CVP Reporting Server WSM certificate> -v -keysize 2048 -keyalg RSA .

Enter the keystore password when prompted.

Enter the details at the prompts and type Yes to confirm.

The alias will be the same as the CN of the Call Server or the VXML Server.

Ensure that you enter the details of the OAMP server while creating the certificate.

Step 2

Generate the certificate request for the alias by running the following command and saving it to a file (for example, jmx.csr): %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias <CN of CVP Server
                                             or CVP Reporting Server WSM certificate> -file %CVP_HOME%\conf\security\jmx.csr .

Enter the keystore password when prompted.

Step 3

Sign the certificate on a CA.

Follow the procedure to create a CA-signed certificate using the CA authority. Download the certificate and the root certificate
                                                         of the CA authority.

Step 4

Copy the root certificate and CA-signed JMX Client certificate to %CVP_HOME%\conf\security\ .

Step 5

Import the root certificate of the CA by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                             root -file %CVP_HOME%\conf\security\<filename_of_root_cert> .

Enter the keystore password when prompted.

At Trust this certificate prompt, type Yes .

Step 6

Import the CA-signed JMX Client certificate of CVP Server and CVP Reporting Server by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                             <CN of CVP Server or CVP Reporting Server WSM certificate> -file %CVP_HOME%\conf\security\<filename_of_your_signed_cert_from_CA> .

Enter the keystore password when prompted.

Step 7

Restart OAMP service.

Step 8

Log into OAMP. To enable secure communication between OAMP and Call Server or VXML Server, navigate to Device Management > Call Server or Device Management > VXML Server . Check the Enable secure communication with the Ops console check box. Save and deploy both Call Server and VXML Server.

Step 9

Run the regedit command.

Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\OPSConsoleServer\Parameters\Java .

Append the following to the file sand save it:

The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore

```
Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore
Djavax.net.ssl.trustStorePassword=<keystore_password>
Djavax.net.ssl.trustStoreType=JCEKS
```

After securing the ports for JMX, JConsole can be accessed only after performing the defined steps for JConsole listed in
                                                         the OpenJDK docs.

After securing the ports for JMX, JConsole can be accessed only after performing the defined steps for JConsole listed in
                                                         the Oracle docs.

Step 10

Restart the OAMP service.

### [Optional] Blocking JConsole Login to OAMP

This section is needed if you want to block JConsole login to OAMP.

OAMP will stop the JMX communication with the following procedure but OAMP to Call Server/VXML Server / Reporting Server/WSM
                                             will continue to work.

Step 1

Go to c:\cisco\cvp\conf\jmx_oamp.conf .

```
javax.net.debug = all
com.sun.management.jmxremote.ssl.need.client.auth = true com.sun.management.jmxremote.authenticate = false
com.sun.management.jmxremote.port = 10001
com.sun.management.jmxremote.ssl = true
#com.sun.management.jmxremote.ssl.config.file=
com.sun.management.jmxremote.rmi.port = 10000
```

Step 2

Restart the OpsConsoleServer service.

Step 3

Go to c:\cisco\cvp\conf\jmx_wsm.conf .

```
javax.net.debug = all
com.sun.management.jmxremote.ssl.need.client.auth = true com.sun.management.jmxremote.authenticate = false
com.sun.management.jmxremote.port = 2099
com.sun.management.jmxremote.ssl = true
#com.sun.management.jmxremote.ssl.config.file=
com.sun.management.jmxremote.rmi.port = 3000
javax.net.ssl.keyStore= C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword= <keystore_password>
```

Step 4

Restart the WSM service.

With the aforesaid steps, unsecure JConsole login to OAMP will stop from remote machines but JConsole will continue to work
                                 from the OAMP host.

### Securing System CLI

To run the System CLI command on Cisco CVP CallServer, perform the following steps:

Step 1

Import the root CA certificate in the JRE keystore:

Run the %CVP_HOME%\jre\bin\keytool.exe -keystore %CVP_HOME%\jre\lib\security\cacerts -import -v -trustcacerts -alias root -file %CVP_HOME%\conf\security\<filename_of_root_cert> command.

Enter the keystore password when prompted.

The default keystore password is changeit .

Type Yes when the Trust this certificate prompt appears.

Step 2

Restart the Cisco CVP CallServer service.

## Secure SIP Communication between Call Server and Cisco VVB

You can secure SIP communication by:

Exchanging the
                                 			 self-signed certificates between the components.

Signing the
                                 			 certificates by a Certificate Authority.

To support AES 256 bit encryption-based ciphers (for example, TLS_RSA_WITH_AES_256_CBC_SHA256), JRE version in the Unified
                                             CVP server needs to be upgraded to Java 1.8u275.

If you are using SHA1 after upgrading the JRE version, then edit C:\Cisco\CVP\jre\lib\security\java.security file to remove the SHA1 jdkCA & usage TLSServer parameter from jdk.certpath.disabledAlgorithms configuration.

### Self-Signed
                           	 Certificates

When the Unified CVP Call Server, Media Server, and Unified CVP VXML Server are co-resident on the same server and use self-signed
                                          certificates, you can use a single self-signed certificate for all these services. This simplifies the certificate management
                                          process and ensures secure communication within the co-resident environment.

#### On Call
                              	 Server

Log in to the Call Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 1

Export the Call Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias callserver_certificate
                                                -file %CVP_HOME%\conf\security\<callserver_certificate.cer> .

Step 2

Enter the keystore password when prompted.

Step 3

Copy the VVB self-signed certificate to %CVP_HOME%\conf\security\ and import the certificate to the callserver keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                vb_cert -file %CVP_HOME%\conf\security\<vvb certificate> .

See Step 5 of the On Cisco VVB section to download a VVB certificate.

Step 4

Enter the keystore password when prompted.

Step 5

Use the list flag to check your keystore entries by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -list .

#### On Cisco
                              	 VVB

Step 1

Copy the CVP CallServer self-signed certificate downloaded from CVP and upload it to VVB against tomcat-trust.

Step 2

Go to OS Admin > Security > Certificate Management > Upload certificate/certificate chain .

Step 3

In Certificate Purpose , select tomcat-trust .

Step 4

Select the self-signed certificate of the Call Server and click Upload .

Step 5

Download the self-signed certificate of the VVB.

Step 6

Go to OS Admin > Security > Certificate Management .

Step 7

In the Certificate column, find the certificate named tomcat .

Step 8

Select the self-signed tomcat certificate and click Download .

Step 9

After the new certificate is uploaded, restart the node(s) using the CLI command utils system restart .

Step 10

Go to Cisco VVB Administration > System Parameters > TLS .

Step 11

Check TLS as Enable .

Step 12

Select the supported TLS version and click Update .

Step 13

Restart Cisco VVB Engine from the VVB Serviceability page.

### CA-Signed Certificate

#### On Call
                              	 Server

Log in to the Call Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Attention

Repeat this procedure if you have multiple Call Servers.

#### On Cisco
                              	 VVB

Step 1

To generate the CSR certificate on VVB, open the administration page. From the Navigation drop-down list, choose Cisco Unified OS Administration and click Go .

Step 2

Go to Security > Certificate Management > Generate CSR Generate Certificate signing Request . Create the CSR against tomcat with the key-length as 2048.

Step 3

To download the generated CSR, click Download CSR . After the Generate Certificate signing Request dialog opens, click Download CSR .

Step 4

Open the certificate in Notepad, copy the contents and sign the certificate with CA.

Step 5

Upload the root certificate generated from the CA into VVB against tomcat-trust:

Go to Security > Certificate Management > Generate CSR > Upload certificate/certificate chain .

Choose tomcat-trust from the drop-down list.

Click Browse and select the certificate.

Click Upload to upload the root certificate of the Certificate Authority.

Step 6

Upload the signed certificate into VVB against tomcat.

Go to Security > Certificate Management > Upload certificate/certificate chain .

Choose tomcat from the drop-down list.

Click Browse and select the certificate.

Click Upload .

Step 7

Restart the Tomcat service and the VVB engine.

For the configuration steps, see the Manage System Parameters section.

## Secure HTTP Communication between VXML Server and Cisco VVB

You can secure HTTP communication by:

Exchanging the self-signed certificates between the VXML Server and VVB.

Signing the
                                 			 certificates by a Certificate Authority.

### Self-Signed
                           	 Certificate

#### On VXML
                              	 Server

Log in to the VXML Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 1

Export the VXML SERVER certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias vxml_certificate
                                                -file %CVP_HOME%\conf\security\<vxml_certificate.cer> .

Step 2

Enter the keystore password when prompted.

Step 3

Copy the Cisco VVB self-signed certificate to %CVP_HOME%\conf\security\ and import the certificate to the callserver keystore by running keystore.%CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS
                                                -alias vb_cert -file %CVP_HOME%\conf\security\<vvb certificate> .

See Step 5 of the following Section, On Cisco VVB to download a VVB certificate.

Step 4

Enter the keystore password when prompted.

Step 5

Use the list flag to check your keystore entries by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -list .

#### On Cisco
                              	 VVB

Step 1

Copy the VXML Server self-signed certificate downloaded from CVP and upload it to VVB against tomcat-trust.

Step 2

Go to OS Admin > Security > Certificate Management > Upload certificate/certificate chain .

Step 3

In Certificate Purpose , select tomcat-trust .

Step 4

Select the self-signed certificate of the VXML Server and click Upload .

Step 5

Download the self-signed certificate of the VVB.

Step 6

Go to OS Admin > Security > Certificate Management .

Step 7

In the Certificate column, select the tomcat certificate.

Step 8

Select the tomcat certificate and click Download .

Step 9

After the new certificate uploads, restart the Cisco Tomcat service.

Step 10

Go to Cisco VVB Administration > System Parameters > TLS .

Step 11

Check the TLS check box as Enable .

Step 12

Select the supported TLS version and click Update .

Step 13

Restart the Cisco VVB Engine from the VVB Serviceability page.

To enable secured connection in Application Management from the Cisco VVB UI, see Cisco Virtualized Voice Browser Administration and Configuration Guide available at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html .

### CA-Signed Certificate

#### On VXML
                              	 Server

Log in to the VXML Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 1

Remove the existing certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -delete -alias vxml_certificate .

Step 2

Generate a new key pair for the alias with selected key size by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias vxml_certificate
                                                -v -keysize 2048 -keyalg RSA .

```
Enter keystore password: <enter the keystore password>
What is your first and last name?
 [Unknown]: <specify the CVP host name appended with "VXML_Server"> E.g cisco-cvp-211_VXML_Server
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

Step 3

Generate the CSR certificate for the alias by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias vxml_certificate
                                                -file %CVP_HOME%\conf\security\vxmlserver.csr and save it to a file (for example, oamp.csr) .

Step 4

Enter the
                                             			 keystore password when prompted.

Step 5

Download the vxmserver.csr from CVP %CVP_HOME%\conf\security\ and sign it from CA.

Step 6

Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\

Step 7

Install the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                root -file %CVP_HOME%\conf\security\<filename_of_root_cert> .

Step 8

Enter the
                                             			 keystore password when prompted.

Step 9

Install the signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                vxml_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert> .

Step 10

Enter the
                                             			 keystore password when prompted.

Step 11

Restart the
                                             			 VXML Server.

#### On Cisco
                              	 VVB

Step 1

Upload the root certificate generated from the CA into VVB against tomcat-trust. Go to OS Admin > Security > Certificate Management > Upload certificate/certificate chain , select tomcat-trust and upload the root certificate of the Certificate Authority.

If you use the same root certificate that was used in the Call Server configuration as described in Section, Secure Communication
                                                            between Call Server and Cisco VVB and the certificate is already imported, then you can skip this step.

Step 2

Generate the CSR against tomcat with the key-length as 2048.

Step 3

Open the certificate in Notepad. Copy the contents and sign the certificate with CA.

Step 4

Restart the Tomcat service and the VVB engine.

To enable secure communications on the VXML Server, see Unified CVP VXML Server Setup Administration Guide for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html .

To enable secure communications on the VXML Server (standalone), see Unified CVP VXML Server (Standalone) Setup Administration Guide for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html .

## Secure HTTPS Communication between Media Server and Cisco VVB

This section describes how to import certificate from IIS MediaServer to Cisco VVB and how to import IIS CA-signed certificate.

Step 1

Enter https://<mediaserver>:443/ in the address bar of the web browser.

Step 2

In the Security Alert dialog box, click View Certificate .

Step 3

Click the Details tab

Step 4

Click Copy to File .

Step 5

In the Certificate Export Wizard dialog box, click Base-64 encoded X.509 (.CER) , and then click Next .

Step 6

In the File to the Export dialog box, specify a file name, and then click Next .

Step 7

Click Finish .

Step 8

Click OK and close the Security Alert dialog box.

Step 9

Copy the CVP MediaServer self-signed certificate downloaded from the CVP and upload into VVB against tomcat-trust .

Step 10

Go to OS Admin > Security > Certificate Management > Upload certificate/certificate chain > In Certificate Purpose* select tomcat-trust , choose the self-signed certificate of the Call Server and press Upload button.

Step 11

Restart Cisco VVB Engine.

## Secure HTTP Communication between OAMP Server and Cisco VVB

### Self-Signed Certificate

Step 1

Sign in to Cisco Unified OS Administration on the VVB server (https://<FQDN of VVB server>/cmplatform).

Step 2

Go to Security > Certificate Management .

Step 3

Click Find .

Step 4

Perform one of the following steps.

- If the tomcat certificate for your server is not on the list, click Generate Self-signed . When the certificate is generated, reboot your server.

Ensure that the certificate you select includes the hostname for the server.

Step 5

Click Download .PEM File and save the file to your desktop.

Step 6

Copy the certificate to %CVP_HOME%\conf\security\ in OAMP Server.

Step 7

Run the following command to import the certificate to the CVP Call Server keystore.

%CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                VVB_cert -file %CVP_HOME%\conf\security\<VVB certificate.pem>

Log in to the Call Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 8

Go to Services and restart Cisco CVP OPSConsoleServer .

### CA-Signed Certificate

#### On OAMP Server

Step 1

Log in to the OAMP Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 2

Remove the existing certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -delete -alias oamp_certificate .

Step 3

Generate a new key pair for the alias with selected key size by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias oamp_certificate
                                                -v -keysize 2048 -keyalg RSA .

```
Enter keystore password: <enter the keystore password>
What is your first and last name?
 [Unknown]: <specify the CVP host name appended with "OAMP_Server"> E.g cisco-cvp-211_OAMP_Server
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

Step 4

Generate the CSR certificate for the alias by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\oampserver.csr and save it to a file (for example, oamp.csr ) .

Step 5

Enter the keystore password when prompted.

Step 6

Download oamp.csr from CVP %CVP_HOME%\conf\security\ and sign it from CA.

Step 7

Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\

Step 8

Install the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                root -file %CVP_HOME%\conf\security\<filename_of_root_cert> .

Step 9

Enter the keystore password when prompted.

Step 10

Install the signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                oamp_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert> .

Step 11

Enter the keystore password when prompted.

Step 12

Restart the Cisco CVP OpsConsoleServer service.

#### On Cisco VVB

Step 1

To generate the CSR certificate on VVB, open the administration page. From the Navigation drop-down list, choose Cisco Unified OS Administration and click Go .

Step 2

Go to Security > Certificate Management > Generate CSR Generate Certificate signing Request . Create the CSR against tomcat with the key-length as 2048.

Step 3

To download the generated CSR, click Download CSR . After the Generate Certificate signing Request dialog opens, click Download CSR .

Step 4

Open the certificate in Notepad, copy the contents and sign the certificate with CA.

Step 5

Upload the root certificate generated from the CA into VVB against tomcat-trust:

Go to Security > Certificate Management > Generate CSR > Upload certificate/certificate chain .

Choose tomcat-trust from the drop-down list.

Click Browse and select the certificate.

Click Upload to upload the root certificate of the Certificate Authority.

Step 6

Upload the signed certificate into VVB against tomcat.

Go to Security > Certificate Management > Upload certificate/certificate chain .

Choose tomcat from the drop-down list.

Click Browse and select the certificate.

Click Upload .

Step 7

Restart the Tomcat service and the VVB engine.

## Secure HTTP Communication between VXML Server and Dialogflow

Step 1

Log in to VXML Server.

Step 2

Run the regedit command.

Step 3

Go to HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Apache Software Foundation\Procrun 2.0\VXMLServer\Parameters\Java\Options .

Step 4

Append the following lines to the file:

```
-Dhttps.proxyHost=<Your proxy IP/Host>
-Dhttps.proxyPort=80
```

```
-Dhttps.proxyUser=<username>
-Dhttps.proxyPassword=<password>
```

Step 5

Restart service Cisco CVP VXMLServer .

## Secure HTTP Communication between OAMP Server and Call Server

### Self-Signed Certificate

Step 1

Log in to the CVP Server . For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 2

Run the following command to export the WSM certificate.

%CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias wsm_certificate
                                                -file %CVP_HOME%\conf\security\{CVPServerName}_wsm.cer>

Step 3

Enter the keystore password when prompted.

Step 4

Copy the certificate to %CVP_HOME%\conf\security\ in OAMP Server.

Step 5

Log in to the OAMP Server .

For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 6

Run the following command to import the certificate to the OAMP Server:

%CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                {CVPServername}_wsm -file %CVP_HOME%\conf\security\{CVPServername}_wsm.cer>

For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 7

Enter the keystore password when prompted.

Step 8

Repeat all the steps for all the Cisco Unified CVP Servers in the deployment.

Step 9

Go to Services and restart Cisco CVP OPSConsoleServer and CVP WebServices on CVP OAMP Server .

Step 10

Download the OAMP WSM certificate (OAMP_wsm) from https://<oampserverip>:8111 on the Cisco Unified CVP Server to %CVP_HOME%\conf\security\

Step 11

Run the following command to import the certificate to the Cisco Unified CVP Server:

%CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                oamp_wsm -file %CVP_HOME%\conf\security\oamp_wsm.cer>

Step 12

Enter the keystore password when prompted.

Step 13

Repeat all the steps for all the Cisco Unified CVP Servers in the deployment.

Step 14

Go to Services and restart Cisco Web Services , Cisco VXML Service , and Cisco Call Service on each Cisco Unified CVP Server.

### CA-Signed Certificate

#### On OAMP Server

Step 1

Log in to the OAMP Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 2

Remove the existing certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -delete -alias oamp_certificate .

Step 3

Generate a new key pair for the alias with selected key size by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias oamp_certificate
                                                -v -keysize 2048 -keyalg RSA .

```
Enter keystore password: <enter the keystore password>
What is your first and last name?
 [Unknown]: <specify the CVP host name appended with "OAMP_Server"> E.g cisco-cvp-211_OAMP_Server
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

Step 4

Generate the CSR certificate for the alias by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\oampserver.csr and save it to a file (for example, oamp.csr ) .

Step 5

Enter the keystore password when prompted.

Step 6

Download oamp.csr from CVP %CVP_HOME%\conf\security\ and sign it from CA.

Step 7

Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\

Step 8

Install the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                root -file %CVP_HOME%\conf\security\<filename_of_root_cert> .

Step 9

Enter the keystore password when prompted.

Step 10

Install the signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                oamp_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert> .

Step 11

Enter the keystore password when prompted.

Step 12

Restart the Cisco CVP OpsConsoleServer service.

#### On Call Server

Step 1

Log in to the Call Server and retrieve the keystore password from the security.properties file.

At the command prompt, enter the following command:

more %CVP_HOME%\conf\security.properties .

Security.keystorePW = <Returns the keystore password>

Enter the keystore password when prompted.

Step 2

Log in to the Call Server or Reporting Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 3

Remove the existing WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -delete -alias wsm_certificate .

Step 4

Remove the existing Call Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security.keystore -delete -alias callserver_certificate .

Step 5

Generate a new key pair for the alias with selected key size by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias wsm_certificate
                                                -v -validity <duration in days> -keysize 2048 -keyalg RSA .

```
Enter keystore password: <enter the keystore password>
What is your first and last name?
 [Unknown]: <specify the CVP hostname or FQDN, appended with "wsm"> E.g cisco-cvp-211_wsm >
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

When a certificate is generated to be used in PCCE SPOG, provide the FQDN of the host without appending _wsm.

The default duration for validity is 90 days.

Step 6

Generate the CSR certificate for the alias by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias wsm_certificate
                                                -file %CVP_HOME%\conf\security\wsm.csr and save it to a file (for example, wsm.csr ) .

Step 7

Enter the keystore password when prompted.

Step 8

Download wsm.csr from CVP %CVP_HOME%\conf\security\ and sign it from CA.

Step 9

Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\

Step 10

Install the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -validity <duration
                                                in days> -trustcacerts -alias root -file %CVP_HOME%\conf\security\<filename_of_root_cert> .

Step 11

Enter the keystore password when prompted.

Step 12

Install the signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -validity <duration
                                                   in days> -trustcacerts -alias wsm_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert> .

Step 13

Enter the keystore password when prompted.

Step 14

Restart the Cisco CVP WebServicesManager service.

## Configure Cloud Connect

### Before you begin

Import the certificate from the Call Server to the Operations Console server. For details on how to do this, see Secure HTTPS Communication between OAMP Server and Call Server section in Configuration Guide for Cisco Unified Customer Voice Portal .

Import the Cloud Connect certificate to the Call Server. For details on how to do this, see Import the Cloud Connect Certificate .

Ensure Unified CVP hostname is DNS resolvable from OAMP Server.

Restart the CVP OPSConsoleServer service.

Step 1

To open the Operations Console, enter https://<FQDN>:9443/noamp in the web-browser, where FQDN is the fully qualified domain name of the machine on which Operations Console is installed.

Step 2

Navigate to Integration > Cloud Connect .

Step 3

From the Device drop-down list, select the CVP device.

Step 4

In the Publisher IP Address / Hostname text box, enter the FQDN / IP address of the publisher.

Step 5

In the Subscriber IP Address / Hostname text box, enter the FQDN / IP address of the subscriber.

Step 6

In the User Name text box, enter the username.

Step 7

In the Password text box, enter the password.

Step 8

Click Save .

Step 9

Restart the Cisco CVP Call Server.

## Import the Cloud Connect Certificate

Ensure that you import both the Cloud Connect Publisher and Subscriber certificates to all the CVP call servers.

Step 1

To export the Cloud Connect certificates:

Enter the following URL to access the Cisco Unified Communications Operating System Administration page.

```
https://<FQDN of CloudConnect:8443/cmplatform
```

Navigate to Security > Certificate Management and find the Cloud Connect publisher and subscriber certificates in one of your tomcat-trust folders.

Select the certificates and click Download .PEM File to save the certificates to a local folder.

Step 2

Copy the Cloud Connect certificates into the call server folder at c:\cisco\cvp\conf\security .

Step 3

Open the Command Prompt as an administrator.

Step 4

Enter the following command in the keystore to import the Cloud Connect certificate to the call server.

```
c:\Cisco\CVP\jre\bin\keytool.exe -import -keystore .keystore -storetype JCEKS -trustcacerts 
   -alias <cloud connect publisher or cloud connect subscriber> –file <filepath>
```

Step 5

Enter the keystore password when prompted. To retrieve the keystore password, do the following:

Go to %CVP_HOME%\bin . Generate the keystore password by running the DecryptKeystoreUtil.bat file.

Step 6

Restart the CVP call server.

Step 7

Repeat steps 1 through 6 for all the CVP call servers.

For more details on how to obtain a third-party CA certificate for Cloud Connect, see the Obtain and Upload Third-party CA Certificate topic in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html .

## Import VRU PG Certificate

Follow this procedure to import the VRU PG (RSA or ECDSA folder as required) certificates to CVP call servers:

Step 1

Log in to the CVP Call Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 2

Copy the VRU PG certificate to the CVP call server folder at %CVP_HOME%\conf\security\ .

Step 3

Open the Command Prompt as an administrator.

Step 4

Enter the following command in the keystore to import the VRU PG certificate to the callserver keystore:

%CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                             <VRU_PG_Certificate> -file <filepath>

Step 5

Enter the keystore password when prompted.

Step 6

Restart the CVP call server.

## Secure Communication on CUCM

You can secure communication on CUCM by:

Exchanging the self-signed certificates.

Signing the certificates by a Certificate Authority.

### Self-Signed Certificate

Step 1

Log in to the CUCM OS Administration page.

Step 2

Go to Security > Certificate Management .

Step 3

Click Generate Self-signed .

Step 4

On the pop-up window, click Generate button.

Step 5

Restart Tomcat from CUCM CLI by running utils service restart Cisco Tomcat .

Tomcat will take a few minutes to stop and then start. If you access the CUCM UI during this time, you may receive a 404 error.

Step 6

When the CUCM UI is available, open the CUCM OS Administration page.

Step 7

Go to Security > Certificate Management .

Step 8

Click Find and identify the Self-signed certificate generated by the system.

Step 9

Click the CallManager Certificate name.

Step 10

In the dialog box, click Download .

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

Upload the root certificate generated from the CA to CUCM against CUCM-trust.

Step 13

Click Upload
                                             				Certificate on CUCM by selecting the certificate name as CallManager .

On successful
                                             				completion, CUCM displays the description as Certificate
                                                				  signed by <CA hostname> .

Step 14

Restart TFTP
                                          			 and Cisco CallManager services on all the nodes in the cluster that run these
                                          			 services.

## Secure Communication between Ingress Gateway and Call Server

You can secure communication between the Ingress Gateway and the Call Server by:

Exchanging the self-signed certificates.

Signing the certificates by a Certificate Authority.

### Self-Signed Certificate

To secure SIP connection between Cisco Ingress Gateway and Call Server, import the Call Server certificate on the IOS device
                                 during the device configuration.

Step 1

Open the certificate that was exported in Step 1 .

Step 2

Click View Certificate .

Step 3

Click the Details tab.

Step 4

Click Copy to File .

Step 5

Click Base-64 encoded X.509 (.CER) , and then click Next .

Step 6

Specify a file name in the File to the Export dialog box, and then click Next .

Step 7

Click Finish . A message indicates that the export was successful.

Step 8

Click OK and close the Security Alert dialog box.

Step 9

Open the certificate in Notepad.

Step 10

Access the IOS ingress GW in the privileged EXEC mode.

Step 11

Access the global configuration mode by entering the configuration terminal.

Step 12

Import the CVP CallServer Certificate to Cisco IOS Gateway by entering the following commands:

```
crypto pki trustpoint <Call Server trust point name>
enrollment terminal

exit
```

Step 13

Open the exported Call Server certificate in Notepad and copy the certificate information that appears between the -BEGIN
                                          CERTIFICATE and END CERTIFICATE tags to the IOS device.

Step 14

Enter the following command:

```
crypto pki auth <Call Server  trust point name>
```

Step 15

Paste the certificate from Notepad and end with a blank line or the word quit on a line by itself.

Step 16

To generate the self-signed certificate of the Gateway, first generate 2048-bit RSA keys:

```
crypto key generatersageneral-keys Label <Your Ingress GW trustpointname> modulus 2048
```

Step 17

Configure a trustpoint:

```
crypto pkitrustpoint<Your Ingress GW trustpointname>
enrollment selfsigned
fqdn none
subject-name CN=SIP-GW
rsakeypair <Your Ingress GW trustpoint name>

Router(config)# crypto pkienroll<Your Ingress GW trustpointname> % The fully-qualified domain name will not be included in the certificate
% Include the router serial number in the subject name? [yes/no]: no
% Include an IP address in the subject name? [no]: no
Generate Self Signed Router Certificate? [yes/no]: yes
Router Self Signed Certificate successfully created
```

Step 18

View the certificate in PEM format, and copy the Self-signed CA certificate (output starting from “----BEGIN” to “CERTIFICATE----“)
                                          to a file named ingress_gw.pem .

```
Router(config)# crypto pki export <Your Ingress GW trustpoint name> pem terminal % Self-signed CA certificate:
-----BEGIN CERTIFICATE-----
MIIB6zCCAVSgAwIBAgIBAjANBgkqhkiG9w0BAQUFADARMQ8wDQYDVQQDEwZTSVAt
R1cwHhcNMTcwOTI2MTQ1MTE2WhcNMjAwMTAxMDAwMDAwWjARMQ8wDQYDVQQDEwZT
SVAtR1cwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAKdSDxIj8T6UaYxgujMk
9B2d5dq3Ni8s1e4yfsSB1lbJ/AQk+aLDfE3/BeVkeXEjRCohhnZcEnMV4DdOPxj7
9MWzoJgxkMj7X3I6ijaL2Oll2iQuBcjiqYtAUPlxB3VTjqLMbxG30fb7xLCDTuo5
s07TLsE1AbxrbrH62Za/C0e5AgMBAAGjUzBRMA8GA1UdEwEB/wQFMAMBAf8wHwYD
VR0jBBgwFoAU+tJphvbvgc7yE6uqIh7VlgTrtPswHQYDVR0OBBYEFPrSaYb274HO
8hOrqiIe1ZYE67T7MA0GCSqGSIb3DQEBBQUAA4GBADRaW93OqErMEgRGWJJVLlbs
n8XnSbiw1k8KeY/AzgxBoBJtc0FKs4L0XUOEc6eHUKCHoks1FDV211MMlzPe7MAc
vDd7EV/abx2UdFSL9jjm/YzIleVUj8b0T3qNSfOqDtV5CyCjPichNa2eCR1bTmGx
o3HqLeEl/+66L/l74nlT
-----END CERTIFICATE-----

% General Purpose Certificate:
-----BEGIN CERTIFICATE-----
MIIB6zCCAVSgAwIBAgIBAjANBgkqhkiG9w0BAQUFADARMQ8wDQYDVQQDEwZTSVAt
R1cwHhcNMTcwOTI2MTQ1MTE2WhcNMjAwMTAxMDAwMDAwWjARMQ8wDQYDVQQDEwZT
SVAtR1cwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAKdSDxIj8T6UaYxgujMk
9B2d5dq3Ni8s1e4yfsSB1lbJ/AQk+aLDfE3/BeVkeXEjRCohhnZcEnMV4DdOPxj7
9MWzoJgxkMj7X3I6ijaL2Oll2iQuBcjiqYtAUPlxB3VTjqLMbxG30fb7xLCDTuo5
s07TLsE1AbxrbrH62Za/C0e5AgMBAAGjUzBRMA8GA1UdEwEB/wQFMAMBAf8wHwYD
VR0jBBgwFoAU+tJphvbvgc7yE6uqIh7VlgTrtPswHQYDVR0OBBYEFPrSaYb274HO
8hOrqiIe1ZYE67T7MA0GCSqGSIb3DQEBBQUAA4GBADRaW93OqErMEgRGWJJVLlbs
n8XnSbiw1k8KeY/AzgxBoBJtc0FKs4L0XUOEc6eHUKCHoks1FDV211MMlzPe7MAc
vDd7EV/abx2UdFSL9jjm/YzIleVUj8b0T3qNSfOqDtV5CyCjPichNa2eCR1bTmGx
o3HqLeEl/+66L/l74nlT
-----END CERTIFICATE-----
```

Step 19

Test your certificate.

```
show crypto pkicertificates
```

Step 20

To configure TLS version on the Gateway:

```
router# configure terminal router(config)# sip-ua router(config-sip-ua)# transport tcp tls <version> v1.2 Enable TLS Version 1.2

Note: SIP TLS version 1.2 is available in Cisco IOS Software Release 15.6(1)T and higher.
```

Step 21

To check if the TLS version is negotiated:

```
router# show sip-ua connections tcp tls detail
```

Step 22

To enable SRTP on the incoming/outgoing dial-peer, specify SRTP:

```
router# configure terminal router(config)# dial-peer voice 100 voip router(config-dial-peer)# srtp Note: This command is supported in Cisco IOS Software Release 15.6(1)T and higher.
```

Step 23

Configure the SIP stack in Cisco IOS GW to use the self-signed certificate of the router to establish a SIP TLS connection
                                          from/to the CVP Call Server.

```
router# configure terminal router(config)# sip-ua router(config-sip-ua)# crypto signaling remote-addr <peer IP address> <peer subnet mask> trustpoint <Your Ingress GW trustpoint name> strict-cipher Example: 
sip-ua 
 crypto signaling remote-addr 10.48.54.89 255.255.255.255 trustpoint VG-SIP-1 strict-cipher
```

Step 24

Configure an outbound VoIP dial-peer to route calls to the CVP Call Server.

```
session target ipv4:<Call Server IP address>:5061
 session transport tcp tls

Example:
dial-peer voice 3 voip
 destination-pattern 82...
 session protocol sipv2
 session target ipv4:10.48.54.89:5061
 session transport tcp tls
 dtmf-relay rtp-nte
 codec g711ulaw
```

Step 25

To import GW or CUSP certificate into the CVP Call Server:

Copy the Ingress GW/ CUSP self-signed certificate to %CVP_HOME%\conf\security\ and import the certificate to the callserverkeystore. %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetypeJCEKS -alias gw_cert
                                                   -file %CVP_HOME%\conf\security\<ingress GW\CUSP certificate name>

Enter the keystore password when prompted.

A message appears on the screen: Trust this certificate? [no]: Enter yes .

Use the list flag to check your keystore entries by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -list

Step 26

To change the supported TLS version from the OAMP UI, see Administration Guide for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html .

Step 27

Restart the Call Server.

### CA-Signed Certificate

For the configuration steps, see the latest Cisco Unified Border Element Configuration Guide available at https://www.cisco.com/c/en/us/support/unified-communications/unified-border-element/products-installation-and-configuration-guides-list.html .

#### Before you begin

To configure SIP TLS and SRTP on the gateway, apply a security-k9 license on the gateway.

Time sync all the nodes (CVP, VVB, Gateway) with an NTP server.

Step 1

Create a 2048-bit RSA key.

```
Router(config)# crypto key generate rsa general-keys Label <name of the key pair> modulus 2048 Generates 2048 bit RSA key pair.
```

Step 2

Create a trustpoint. A trustpoint represents a trusted CA.

```
Example: Router(config)# crypto pki trustpoint ms-ca-name Creates the trustpoint.

Router(config-pki-trustpoint)# enrollment terminal Specifies cut and paste enrollment with this trustpoint.

Router(config-pki-trustpoint)# subject-name CN=sslvpn.mydomain.com,OU=SSLVPN,O=My Company Name,C=US,ST=Florida Defines x.500 distinguished name.

Router(config-pki-trustpoint)# rsakeypair keypairname Specifies key pair generated previously

Router(config-pki-trustpoint)# fqdn sslvpn.mydomain.com Specifies subject alternative name (DNS:).

Router(config-pki-trustpoint)# exit
```

Step 3

Create a CSR (Certificate Request) to give to the MS Certificate Server.

```
Example: Router(config)# crypto pki enroll ms-ca-name % Start certificate enrollment ..
% The subject name in the certificate will include: CN=Webvpn.cisco.com % The subject name in the certificate will include: webvpn.cisco.com % Include the router serial number in the subject name? [yes/no]: no % Include an IP address in the subject name? [no]: no Display Certificate Request to terminal? [yes/no]: yes ! Displays the PKCS#10 enrollment request to the terminal.
! You will need to copy this from the terminal to a text
! file or web text field to submit to the 3rd party CA.

Certificate Request follows:
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Redisplay enrollment request? [yes/no]: no Router(config)#
```

Step 4

Sign the CSR with the root CA.

Step 5

Install the root certificate.

```
Router(config)# crypto pki authenticate ms-ca-name Enter the base 64 encoded CA certificate.
End with a blank line or the word "quit" on a line by itself

-----BEGIN CERTIFICATE-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

-----END CERTIFICATE-----
quit

Certificate has the following attributes:
Fingerprint MD5: D5DF85B7 9A5287D1 8CD50F90 232DB534
Fingerprint SHA1: 7C4656C3 061F7F4C 0D67B319 A855F60E BC11FC44
% Do you accept this certificate? [yes/no]: y Trustpoint CA certificate accepted.
```

Step 6

Install the signed certificate for the gateway:

```
Router(config)# crypto pki import ms-ca-name certificate Enter the base 64 encoded certificate.
End with a blank line or the word "quit" on a line by itself

-----BEGIN CERTIFICATE-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

-----END CERTIFICATE-----
quit
% Router Certificate successfully imported
```

Step 7

Test your certificate.

```
show crypto pki certificates
```

To configure TLS version on the gateway:

```
router#
router# config terminal router(config)# sip-ua router(config-sip-ua)# transport tcp tls <version> v1.2  Enable TLS Version 1.2
```

To check if the TLS version is negotiated:

```
router# show sip-ua connections tcp tls detail
```

To enable SRTP on the incoming/outgoing dial-peer, specify srtp:

```
router# configure terminal router(config)# dial-peer voice 100 voip router(config-dial-peer)# srtp
```

Step 8

Associate the created trustpoint in Step 2 with sip-ua.

```
router# configure terminal router(config)# sip-ua router(config-sip-ua)# crypto signaling remote-addr <peer IP address> 
<peer subnet mask> trustpoint <trust point name created in step2>
```

Installing CVP Call/VXML Servers enables IIS (for media server functionality), which opens port 443 by default for TLS connections.
                                                         This port allows TLSv1.0 and TLSv1.1 connections. To close these connections, change the Enabled value to 0 by selecting the Decimal option in the following registry keys:

TLSv1.0: HKEY-LOCAL-MACHINE \SYSTEM\CurrentControlSet\Control\SecurityProviders\

SCHANNEL\Protocols\TLS1.0\Server\Enabled

TLSv1.1: HKEY-LOCAL-MACHINE\ SYSTEM\CurrentControlSet\Control\SecurityProviders\

SCHANNEL\Protocols\TLS1.1\Server\Enabled

This disables ports 443 and 3389 for TLSv1.0 and TLSv1.1 server-side connections. While Windows 8 and Windows Server 2012
                                                         remote desktop clients work by default, Windows 7 and Windows Server 2008 remote desktop clients cannot connect to these servers
                                                         for the RDP port (3389). To re-enable this port, install the patch available at https://support.microsoft.com/en-us/help/3080079/update-to-add-rds-

support-for-tls-1-1-and-tls-1-2-in-windows-7-or-wind .

## Secure Communication on CUSP

You can secure communication on CUSP by:

Exchanging the self-signed certificates between the components.

Signing the certificates by a Certificate Authority.

### Self-Signed Certificate

For the configuration steps, see the latest CLI Configuration Guide for Cisco Unified SIP Proxy https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cusp/rel9_0/cli_configuration/cusp_cli_config/configuration.html#72360 .

### CA-Signed Certificate

Step 1

Create an RSA keypair in CUSP . From the CUSP foundation, enter the config mode and create the keypair:

Example

```
democusp48# conf terminal democusp48(config)# crypto key generate rsa label cusp48-ca modulus 1024 default Key generation in progress. Please wait...
The label name for the key is cusp48-ca
```

Step 2

Generate CSR signed by CA by running democusp48(config)# crypto key certreq label <key-label> url ftp:

An FTP or HTTP server is required to export the CSR. Make sure the label in the command matches the label used to create the
                                             rsa private key.

Example

```
democusp48(config)# crypto key certreq label cusp48-ca url ftp: Address or name of remote host? 10.64.82.176
Username (ENTER if none)? test 
Password (not shown)?  
Destination path? /cusp48-ca.csr Uploading CSR file succeed 
democusp48(config)#
```

Step 3

Import the CA server root certificate into CUSP by running: crypto key import trustcacert label <rootCA-label> terminal .

Example

```
democusp48(config)# crypto key import trustcacert label rootCA terminal Enter certificate...
End with a blank line or "quit" on a line by itself
-----BEGIN CERTIFICATE----- MIIEdTCCA12gAwIBAgIQaO1+pgDsy5lNqtF3E
epB4TANBgkqhkiG9w0BAQUFADBC MRMwEQYKCZImiZPyLGQBGRYDY29tMRcwFQYK
CZImiZPyLGQBGRYHQVJUR1NPTDES MBAGA1UEAxMJU0lQUEhPTklYMB4XDTA3MDc
xMzExNTAyMVoXDTEyMDcxMzExNTgz MVowQjETMBEGCgmSJomT8ixkARkWA2NvbT
EXMBUGCgmSJomT8ixkARkWB0FSVEdT T0wxEjAQBgNVBAMTCVNJUFBIT05JWDCCA
SIwDQYJKoZIhvcNAQEBBQADggEPADCC AQoCggEBAKbepxqDVZ5uWUVMWx8VaHVG
geg4CgDbzCz8Na0XqI/0aR9lImgx1Jnf ZD0nP1QvgUFSZ2m6Ee/pr2SkJ5kJSZo
zSmz2Ge4sKjZZbgQHmljWv1DswVDw0nyV F71ULTaNpsh81JVF5t2lqm75UnkW4x
P5qQn/rgfXv/Xse9964kiZhZYjtt2Ixt2V3imhh1i228YTihnTY5c3L0vD30v8dH
newsaCKd/XU+czw8feWguXXCTovvXHIbFeHvLCk9FLDoV8n9PAIHWZRPnt+HQjsD
s+jaB3F9MPVYXYElpmWrpEPHUPNZG4LsFi 6tQtiRP2UANUkXZ9fvGZMXHCZOZJi
FUCAwEAAaOCAWUwggFhMAsGA1UdDwQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA
1UdDgQWBBR39nCk+FjRuAbWEof5na/+Sf58STCCAQ4GA1UdHwSCAQUwggEBMIH+o
IH7oIH4hoG4bGRhcDovLy9DTj1TSVBQSE9O SVgsQ049U0lQUEhPTklYLUlORElB
LENOPUNEUCxDTj1QdWJsaWMlMjBLZXklMjBT ZXJ2aWNlcyxDTj1TZXJ2aWNlcyx
DTj1Db25maWd1cmF0aW9uLERDPUFSVEdTT0ws REM9Y29tP2NlcnRpZmljYXRlUm
V2b2NhdGlvbkxpc3Q/YmFzZT9vYmplY3RDbGFz cz1jUkxEaXN0cmlidXRpb25Qb
2ludIY7aHR0cDovL3NpcHBob25peC1pbmRpYS5h cnRnc29sLmNvbS9DZXJ0RW5y
b2xsL1NJUFBIT05JWC5jcmwwEAYJKwYBBAGCNxUB BAMCAQAwDQYJKoZIhvcNAQE
FBQADggEBAHua4/pwvSZ48MNnZKdsW9hvuTV4jwtGErgc16bOR0Z1urRFIFr2NCP
yzZboTb+ZllkQPDMRPBoBwOVr7BciVyoTo7AKFheqYm9asXL18A6XpK/WqLjlCcX
rdzF8ot0o+dK05sd9ZG7hRckRhFPwwj5Z7z0Vsd/jcO51QjpS4rzMZZXK2FnRvng
d5xmp4U+yJtPyr8g4DyAP2/UeSKe0SEYoTV5x5FpdyF4veZneB7+ZfFntWFf4xwi
obf+UvW47W6pCj5nGLMBzOiaxeQ8pre+yjipL2ucWK4ynOfKzz4XlkfktITDSogQ
A1AS1quQVbKTKk+qLGD6Ml2P0LrcKQkk= 
-----END CERTIFICATE----- 
Certificate info
*******************************************
Owner: CN=cvpvb-GDESINGHROOTCA-CA, DC=cvpvb, DC=cisco, DC=com
Issuer: CN=cvpvb-GDESINGHROOTCA-CA, DC=cvpvb, DC=cisco, DC=com
Certificate fingerprint (MD5): 41:A2:31:9D:97:AF:A8:CA:60:FC:46:95:82:DE:78:03
Do you want to continue to import this certificate, additional validation will be perfom? [y/n]: y 
democusp48(config)#
```

Step 4

Import the signed certificate into CUSP by running crypto key import cer label <key-label> url terminal .

Example

```
democusp48(config)# crypto key import cer label cusp48-ca terminal Enter certificate...
End with a blank line or "quit" on a line by itself
-----BEGIN CERTIFICATE----- MIIFITCCBAmgAwIBAgIKGI1fqgAAAAAAEDAN
BgkqhkiG9w0BAQUFADBCMRMwEQYK CZImiZPyLGQBGRYDY29tMRcwFQYKCZImiZ
PyLGQBGRYHQVJUR1NPTDESMBAGA1UE AxMJU0lQUEhPTklYMB4XDTA4MTIwOTA5M
DExOVoXDTA5MTIwOTA5MTExOVowYTEL MAkGA1UEBhMCJycxCzAJBgNVBAgTAicn
MQswCQYDVQQHEwInJzELMAkGA1UEChMC JycxCzAJBgNVBAsTAicnMR4wHAYDVQQ
DExVTT0xURVNUQ0MuYXJ0Z3NvbC5jb20w gZ8wDQYJKoZIhvcNAQEBBQADgY0AMI
GJAoGBAOZz88nK51bJYjWgvuv4Wx1CGxTN YWGyNg+vDyQgKBXlL7b1CqBx1Yjl4
eetO4LiKkW/y4jSv3nCxCAdOrMvVF5lxFmY baMlR1R/qMCLzAMvmsWlH6VY4rcf
FGkjed3zCcI6BJ6fG9H9dt1J+47iM7SdZYz/ NrEqDnrpoHaUxdzlAgMBAAGjggJ
8MIICeDAdBgNVHQ4EFgQUYXLxMfiZJP29UZ3w Mpj0e79sk4EwHwYDVR0jBBgwFo
AUd/ZwpPhY0bgG1hKH+Z2v/kn+fEkwggEOBgNV HR8EggEFMIIBATCB/qCB+6CB+
IaBuGxkYXA6Ly8vQ049U0lQUEhPTklYLENOPVNJ UFBIT05JWC1JTkRJQSxDTj1D
RFAsQ049UHVibGljJTIwS2V5JTIwU2VydmljZXMs Q049U2VydmljZXMsQ049Q29
uZmlndXJhdGlvbixEQz1BUlRHU09MLERDPWNvbT9j ZXJ0aWZpY2F0ZVJldm9jYX
Rpb25MaXN0P2Jhc2U/b2JqZWN0Q2xhc3M9Y1JMRGlz dHJpYnV0aW9uUG9pbnSGO
2h0dHA6Ly9zaXBwaG9uaXgtaW5kaWEuYXJ0Z3NvbC5j b20vQ2VydEVucm9sbC9T
SVBQSE9OSVguY3JsMIIBIgYIKwYBBQUHAQEEggEUMIIB EDCBqAYIKwYBBQUHMAK
GgZtsZGFwOi8vL0NOPVNJUFBIT05JWCxDTj1BSUEsQ049 UHVibGljJTIwS2V5JT
IwU2VydmljZXMsQ049U2VydmljZXMsQ049Q29uZmlndXJh dGlvbixEQz1BUlRHU
09MLERDPWNvbT9jQUNlcnRpZmljYXRlP2Jhc2U/b2JqZWN0 Q2xhc3M9Y2VydGlm
aWNhdGlvbkF1dGhvcml0eTBjBggrBgEFBQcwAoZXaHR0cDov L3NpcHBob25peC1
pbmRpYS5hcnRnc29sLmNvbS9DZXJ0RW5yb2xsL1NJUFBIT05J WC1JTkRJQS5BUl
RHU09MLmNvbV9TSVBQSE9OSVguY3J0MA0GCSqGSIb3DQEBBQUA A4IBAQAXm0MPu
eXcMYxQhVlPR/Yaxw0n2epeNRwsPP31Pr9Ak3SYSzhoMRVadJ3z K2gt4qiVV8wL
tzTO2o70JXKx+0keZdOX/DQQndxBkiBKqdJ2Qvipv8Z8k3pza3lN jANnYw6FL3/
Yvh+vWCLygEHfrUfKj/7H8GaXQVapj2mDs79/zgoSyIlo+STmwFWT GQy6iFO+pv
vMcyfjjv2dsuwt1Ml0nlict0LtkIKnRGLqnkA6sJo1P6kE+WK7n3P2 yho/Lg98q
vWl+1FRC18DrkUhpNiKXsP1ld9TcJGrdJP9zG7lI5Mf3Q/2NIAx2JZd ZVAsXZMN
smOsOrgXzkcU/xU3BXkX -----END CERTIFICATE-----  Import succeeded 
democusp48(config)#exit 
democusp48#
```

Step 5

You can list the certificates by running show crypto key all .

Example

```
democusp48# sh crypto key all
Label name: rootca
Entry type: Trusted Certificate Entry
Creation date: Sat Jul 01 14:13:14 GMT+05:30 2017
Owner: CN=cvpvb-GDESINGHROOTCA-CA, DC=cvpvb, DC=cisco, DC=com
Issuer: CN=cvpvb-GDESINGHROOTCA-CA, DC=cvpvb, DC=cisco, DC=com
Valid from: Wed Mar 22 14:23:10 GMT+05:30 2017 until: Tue Mar 22 14:33:09 GMT+0
5:30 2022
Certificate fingerprint (MD5): 41:A2:31:9D:97:AF:A8:CA:60:FC:46:95:82:DE:78:03

Label name: cusp48-ca
Entry type: Key Entry
Creation date: Tue Jul 04 10:47:40 GMT+05:30 2017
Owner: CN=democusp48.cvpvb.cisco.com, OU='', O='', L='', ST='', C=''
Issuer: CN=cvpvb-GDESINGHROOTCA-CA, DC=cvpvb, DC=cisco, DC=com
SubjectAltName: DNS:democusp48.cvpvb.cisco.com
Valid from: Tue Jul 04 10:41:56 GMT+05:30 2017 until: Thu Jul 04 10:41:56 GMT+0
5:30 2019
Certificate fingerprint (MD5): 91:ED:83:CA:3B:37:16:E8:AB:07:EA:85:04:1A:D1:05
```

Add the Domain Name System (DNS) of the component with which the secure communication is established under SIP Stack > TLS Trusted Peers in CCCSP.

## Configurable HTTP Security Headers

### Tomcat Level Configuration

You can configure standard HTTP(S) security headers like Strict-Transport-Security, X-XSS-Protection, X-FRAME-OPTIONS, X-Content-Type-Options
                              in CVP to protect from typical attack vectors like MITM (Man-In-The-Middle) attacks, XSS (Cross-Site Scripting), Clickjacking,
                              and MIME-sniffing.

You can configure any of the standard HTTP(S) security headers to include with every response at a blanket level for all apps
                              via the Tomcat-level web.xml file in the $CATALINA_HOME/conf folder. For more information, refer https://tomcat.apache.org/tomcat-9.0-doc/config/filter.html#HTTP_Header_Security_Filter

Cisco Customer Voice Portal ships with these headers enabled with standard recommended values pre-configured by default in
                              all its Tomcat instances; Ops Console Server, Web Service Manager, VXML Server; as follows.

```
<filter>
    <filter-name>httpHeaderSecurity</filter-name>
    <filter-class>org.apache.catalina.filters.HttpHeaderSecurityFilter</filter-class>
    <async-supported>true</async-supported>
	<init-param>
		<param-name>hstsEnabled</param-name>
		<param-value>true</param-value>
	</init-param>
	<init-param>
		<param-name>hstsMaxAgeSeconds</param-name>
		<param-value>31536000</param-value>
	</init-param>
	<init-param>
		<param-name>hstsIncludeSubDomains</param-name>
		<param-value>true</param-value>
	</init-param>
	<init-param>
		<param-name>antiClickJackingEnabled</param-name>
		<param-value>true</param-value>
	</init-param>
	<init-param>
		<param-name>antiClickJackingOption</param-name>
		<param-value>SAMEORIGIN</param-value>
	</init-param>
	<init-param>
		<param-name>blockContentTypeSniffingEnabled</param-name>
		<param-value>true</param-value>
	</init-param>
	<init-param>
		<param-name>xssProtectionEnabled</param-name>
		<param-value>true</param-value>
	</init-param> 
</filter>
```

By default, HSTS is disabled in the VXML Server Tomcat instance because using HTTPS impacts the performance. You can enable
                                          it by uncommenting the documented section of the Tomcat instance’s web.xml.

Test the HTTP and HTTPS connectors, and make sure that you can access your web application via both connectors before you
                                       proceed.

Edit the <tomcat_root_dir>/conf/web.xml file (where, <tomcat_root_dir> is the base directory of Tomcat, for example: C:/Cisco/CVP/OPSConsoleServer/Tomcat ) and add the following in the <web-app> container element:

This configuration can be done at the container level (recommended) or application level, as per your preference. For application
                                                   level, add it to the web.xml file in the WEB-INF folder of the web application. For example: C:\Cisco\CVP\OPSConsoleServer\Tomcat\webapps\oamp\WEB-INF\web.xml

Restart the web application server (or Tomcat).

The above configuration declares that the entire web application is for HTTPS only, and the container intercepts HTTP requests
                                                   and redirect them to the equivalent https:// URL.

### Application Level Configuration

You can enable application-level filters at application-level web.xml in the $CATALINA_HOME/webapps/<app_name>/WEB-INF folder. You can use the filters to override the configuration made in Tomcat container level web.xml or to set some application-specific
                              behaviours.

Tomcat instances in CVP are shipped with an application-level filter to enable the Content-Security-Policy header for XSS
                              protection. They are pre-configured with following standard values:

The application-level filter internally checks the HTML/JS encoding.

Another application-level filter in OAMP allows customization of X-Frame-Options value if required.

```
<filter>
    <filter-name>XSSFilter</filter-name>
    <filter-class>com.cisco.cvp.filter.XSSFilterCommon</filter-class>
    <init-param>
        <param-name>mode</param-name>
        <param-value>frame-ancestors 'self'; default-src 'self'; script-src * 'unsafe-inline' 'unsafe-eval'; style-src * 'unsafe-inline'; img-src * data: 'unsafe-inline'; font-src * data:;</param-value>
    </init-param>
</filter>
```

You can customize the param-value as per your security preferences/standards/deployment. If param-value is left blank, the
                              default value is used.

For more information, refer https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy

## XSS Protection - Query Parameter Validation

As part of measures to protect CVP from XSS (Cross-Site Scripting) attacks, the following Tomcat filter helps to validate/sanitize
                           all query parameters in REST/HTTP(S) requests in a standard, generic, and configurable manner.

The Parameter Validation Filter (PVF) provided by OWASP (Open Web Application Security Project) is available for web applications
                           hosted on Web Services Manager.

The filter definition for each web application is present in the WEB-INF/web.xml file, and the filter's configuration file is WEB-INF/xml/pvf.xml .

For more information on how the filter can be customized or enabled/disabled as required per web application, see https://www.owasp.org/index.php/Parameter_Validation_Filter .

## Configuration for Ghostcat Vulnerability

To fix the Apache Tomcat AJP Local File Inclusion vulnerability (Ghostcat), configuration changes need to be done in OAMP
                           and VXML server.

### OAMP

Step 1

Go to C:\Cisco\CVP\OPSConsoleServer\Tomcat\conf\server.xml .

Step 2

Update the following line as highlighted and save the file:

```
Connector enableLookups="false" port="9009" protocol="AJP/1.3" redirectPort="9443" address="127.0.0.1"
```

Step 3

Go to C:\Cisco\CVP\wsm\Server\Tomcat\conf\server.xml .

Step 4

Update the following line as highlighted and save the file:

```
Connector port="8101" protocol="AJP/1.3" redirectPort="8443" address="127.0.0.1"
```

Step 5

Restart the Web Services Manager and Operations Console services.

### VXML Server

Step 1

Go to C:\Cisco\CVP\VXMLServer\Tomcat\conf\server.xml .

Step 2

Update the following line as highlighted and save the file:

```
Connector enableLookups="false" port="7009" protocol="AJP/1.3" redirectPort="7443" address="127.0.0.1"
```

Step 3

Go to C:\Cisco\CVP\wsm\Server\Tomcat\conf\server.xml .

Step 4

Update the following line as highlighted and save the file:

```
Connector port="8101" protocol="AJP/1.3" redirectPort="8443" address="127.0.0.1"
```

Step 5

Restart the Web Services Manager and VXML services.

## Generate CVP ECDSA Certificate with OpenSSL

Elliptic Curve Digital Signature Algorithm (ECDSA) is a variant of Digital Signature Algorithm which can be enabled in CVP
                              and VVB.

CVP supports either ECDSA or RSA. RSA will continue to be used as the default cryptography algorithm. However, based on the
                              requirements we can enable and disable ECDSA.

For disabling ECDSA, you have to delete the existing ECDSA aliases and generate RSA certificates again.

Use the CVP keystore password when prompted for Export Password , Destination Keystore Password or Source Keystore Password .

### Before you begin

Follow the below steps before you generate the ECDSA Certificate with OpenSSL.

Step 1

Install the latest ES patch from https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/ES_MR/ES/ccvp_b_ccvp-eng-es-spl.html .

Step 2

Update OpenJDK to the the latest version (17.0.1 or higher) . For detailed steps, see Java Runtime Environment Minor Update .

Step 3

Go to C:\Cisco\CVP\conf\security and take a backup of the existing .keystore file.

Step 4

For enabling ECDSA, add the ciphers through OAMP. Go to OAMP > Device Management > Unified CVP Call Server . Select the Call Server. Go to SIP > Advanced Configurations > Security Proprieties . Add the following ciphers here:

TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384

TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256

Step 5

Add the above ciphers in the sip.properties file in the C:/cisco/CVP/conf folder of OAMP server and Reporting server.

Example

### Example

### Self-Signed Certificates

Follow this procedure to generate self-signed ECDSA certificates for Call server, VXML server, WSM server, and OAMP server
                              to be used in CVP.

#### On Call Server

Step 1

Log into the Call Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 2

Download OpenSSL (64 bit) and install on your CVP machine.

Step 3

Add OpenSSL bin path to the Windows environment path variable.

Example: path=C:\Program Files\OpenSSL-Win64\bin

Step 4

Go to C:\Cisco\CVP\conf\security .

Step 5

From the command prompt, run the following commands to generate the private keys for Call server, VXML server, and WSM server
                                             respectively:

Call server:

```
openssl ecparam -name prime256v1 -genkey -noout -out callserver-private-key.pem
```

VXML server:

```
openssl ecparam -name prime256v1 -genkey -noout -out vxml-private-key.pem
```

WSM server:

```
openssl ecparam -name prime256v1 -genkey -noout -out wsm-private-key.pem
```

Step 6

Run the following commands to generate the self-signed certificates for Call server, VXML server, and WSM server:

Call server:

```
openssl req -new -key callserver-private-key.pem  -x509 -nodes -days 365
 -out callserver-cert.pem
```

VXML server:

```
openssl req -new -key vxml-private-key.pem  -x509 -nodes -days 365
 -out vxml-cert.pem
```

WSM server:

```
openssl req -new -key wsm-private-key.pem  -x509 -nodes -days 365
 -out wsm-cert.pem
```

Step 7

Enter the values for the following fields when prompted:

```
Country Name (2 letter code) []:<>
State or Province Name (full name) []:<>
Locality Name (eg, city) []:<>
Organization Name (eg, company) []:<>
Organizational Unit Name (eg, section) []:<>
Common Name (eg, server FQDN or your name) []:.
Email Address []:.
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:.
```

Some fields ( Common Name , Email Address , A challenge password , and An optional company name ) can be left blank by entering a period (.). The certificate is generated after all the details are entered.

Step 8

Run the following commands to append the keys and certificates in one file:

```
cat callserver-private-key.pem callserver-cert.pem > callserver-certificate-private.pem
cat vxml-private-key.pem vxml-cert.pem > vxml-certificate-private.pem
cat wsm-private-key.pem wsm-cert.pem > wsm-certificate-private.pem
```

Step 9

Run the following commands to export the certificates to the Call server:

```
openssl pkcs12 -export -inkey callserver-private-key.pem -in callserver-certificate-private.pem -out cert_callserver.p12 -name callserver_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

```
openssl pkcs12 -export -inkey vxml-private-key.pem -in vxml-certificate-private.pem -out cert_vxml.p12 -name vxml_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

```
openssl pkcs12 -export -inkey wsm-private-key.pem -in wsm-certificate-private.pem -out cert_wsm.p12 -name wsm_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

Step 10

Go to c:\cisco\cvp\conf\security and run the following commands to delete the existing RSA certificates for Call server, VXML server, and WSM servers:

```
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias callserver-certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias vxml_certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias wsm_certificate -storepass <CVP keystore password>
```

Step 11

Run the following commands to import the ECDSA certificates to the keystore:

```
c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_callserver.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias callserver_certificate
Importing keystore cert_callserver.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_vxml.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias vxml_certificate
Importing keystore cert_vxml.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_wsm.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias wsm_certificate
Importing keystore cert_wsm.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]
```

Step 12

Restart the Call server, VXML server, and WSM services from Windows services.

Step 13

In new browser tabs, type the following and check the certificates:

```
https://<callserver ip>:8443
https://<vxmlserver ip>:7443
https://<wsm ip>:8111
```

##### What to do next

Generate ECDSA certificates on the OAMP server.

#### On OAMP Server

Step 1

Log into the OAMP Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 2

Install OpenSSL (64 bit) on your machine.

Step 3

Add OpenSSL bin path to the Windows environment path variable.

Example: path=C:\Program Files\OpenSSL-Win64\bin

Step 4

Go to C:\Cisco\CVP\conf\security .

Step 5

From the command prompt, run the following commands to generate the private keys for the OAMP server and WSM server respectively:

OAMP server:

```
openssl ecparam -name prime256v1 -genkey -noout -out oamp-private-key.pem
```

WSM server:

```
openssl ecparam -name prime256v1 -genkey -noout -out wsm-private-key.pem
```

Step 6

Run the following commands to generate the self-signed certificates for OAMP server and WSM server:

OAMP server:

```
openssl req -new -key oamp-private-key.pem  -x509 -nodes -days 365 -out oamp-cert.pem
```

WSM server:

```
openssl req -new -key wsm-private-key.pem  -x509 -nodes -days 365 -out wsm-cert.pem
```

Step 7

Enter the values for the following fields when prompted:

```
Country Name (2 letter code) []:<>
State or Province Name (full name) []:<>
Locality Name (eg, city) []:<>
Organization Name (eg, company) []:<>
Organizational Unit Name (eg, section) []:<>
Common Name (eg, server FQDN or your name) []:.
Email Address []:.
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:.
```

Some fields ( Common Name , Email Address , A challenge password , and An optional company name ) can be left blank by entering a period (.). The certificate is generated after all the details are entered.

Step 8

Run the following commands to append the keys and certificates in one file:

```
cat oamp-private-key.pem oamp-cert.pem > oamp-certificate-private.pem
cat wsm-private-key.pem wsm-cert.pem > wsm-certificate-private.pem
```

Step 9

Run the following commands to export the certificates to the OAMP server:

```
openssl pkcs12 -export -inkey oamp-private-key.pem -in oamp-certificate-private.pem -out cert_oamp.p12 -name oamp_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

```
openssl pkcs12 -export -inkey wsm-private-key.pem -in wsm-certificate-private.pem -out cert_wsm.p12 -name wsm_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

Step 10

Go to c:\cisco\cvp\conf\security and run the following commands to delete the existing RSA certificates for OAMP server and WSM server:

```
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias oamp_certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias wsm_certificate -storepass <CVP keystore password>
```

Step 11

Run the following commands to import the ECDSA certificates to the keystore:

```
c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_oamp.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias oamp_certificate
Importing keystore cert_oamp.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_wsm.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias wsm_certificate
Importing keystore cert_wsm.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]
```

Step 12

Restart the OAMP and WSM servers from Windows services.

Step 13

In new browser tabs, type the following and check the certificates:

```
https://<wsm ip>:8111
https://<oamp ip>:9443
```

##### What to do next

Generate ECDSA certificates on the Reporting server.

#### On Reporting Server

Step 1

Log into the Reporting Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 2

Install OpenSSL (64 bit) on your machine.

Step 3

Add OpenSSL bin path to the Windows environment path variable.

Example: path=C:\Program Files\OpenSSL-Win64\bin

Step 4

Go to C:\Cisco\CVP\conf\security .

Step 5

From the command prompt, run the following commands to generate the private keys for the Call server and WSM server:

Call server:

```
openssl ecparam -name prime256v1 -genkey -noout -out callserver-private-key.pem
```

WSM server:

```
openssl ecparam -name prime256v1 -genkey -noout -out wsm-private-key.pem
```

Step 6

Run the following commands to generate the self-signed certificates for Call server and WSM server:

Call server:

```
openssl req -new -key callserver-private-key.pem  -x509 -nodes -days 365 -out callserver-cert.pem
```

WSM server:

```
openssl req -new -key wsm-private-key.pem  -x509 -nodes -days 365 -out wsm-cert.pem
```

Step 7

Enter the values for the following fields when prompted:

```
Country Name (2 letter code) []:<>
State or Province Name (full name) []:<>
Locality Name (eg, city) []:<>
Organization Name (eg, company) []:<>
Organizational Unit Name (eg, section) []:<>
Common Name (eg, server FQDN or your name) []:.
Email Address []:.
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:.
```

Some fields ( Common Name , Email Address , A challenge password , and An optional company name ) can be left blank by entering a period (.). The certificate is generated after all the details are entered.

Step 8

Run the following commands to append the keys and certificates in one file:

```
cat callserver-private-key.pem callserver-cert.pem > callserver-certificate-private.pem
cat wsm-private-key.pem wsm-cert.pem > wsm-certificate-private.pem
```

Step 9

Run the following commands to export the certificates to the Reporting server:

```
openssl pkcs12 -export -inkey callserver-private-key.pem -in callserver-certificate-private.pem -out callserver-cert.p12 -name callserver_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

```
openssl pkcs12 -export -inkey wsm-private-key.pem -in wsm-certificate-private.pem -out cert_wsm.p12 -name wsm_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

Step 10

Go to c:\cisco\cvp\conf\security and run the following commands to delete the existing RSA certificates for the Call server and WSM server:

```
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias callserver-certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias wsm_certificate -storepass <CVP keystore password>
```

Step 11

Run the following commands to import the ECDSA certificates to the keystore:

```
c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore callserver-cert.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias callserver_certificate
Importing keystore callserver-cert.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_wsm.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias wsm_certificate
Importing keystore cert_wsm.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]
```

Step 12

Restart the Call server and WSM server from Windows services.

Step 13

In new browser tabs, type the following and check the certificates:

```
https://<callserver ip>:8443
https://<wsm ip>:8111
```

### CA-Signed Certificates

Follow this procedure to generate CA-signed ECDSA certificates for Call server, VXML server, WSM server, and OAMP server to
                              be used in CVP.

#### On Call Server

Step 1

Log into the Call Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 2

Download OpenSSL (64 bit) and install on your CVP machine.

Step 3

Add OpenSSL bin path to the Windows environment path variable.

Example: path=C:\Program Files\OpenSSL-Win64\bin

Step 4

Go to C:\Cisco\CVP\conf\security .

Step 5

From the command prompt, run the following commands to generate the private keys and the CSRs (for Call server, VXML server,
                                             and WSM server) respectively:

Call server:

```
openssl ecparam -name prime256v1 -genkey -noout -out callserver-private-key.pem
openssl req -new -key callserver-private-key.pem -out callserver-cert.csr -days 360
```

VXML server:

```
openssl ecparam -name prime256v1 -genkey -noout -out vxml-private-key.pem
openssl req -new -key vxml-private-key.pem -out vxml-cert.csr -days 360
```

WSM server:

```
openssl ecparam -name prime256v1 -genkey -noout -out wsm-private-key.pem
openssl req -new -key wsm-private-key.pem -out wsm-cert.csr -days 360
```

Step 6

Enter the values for the following fields when prompted:

```
Country Name (2 letter code) []:<>
State or Province Name (full name) []:<>
Locality Name (eg, city) []:<>
Organization Name (eg, company) []:<>
Organizational Unit Name (eg, section) []:<>
Common Name (eg, server FQDN or your name) []:.
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:.
```

This information is incorporated in your certificate request. Some fields ( Common Name , Email Address , A challenge password , and An optional company name ) can be left blank by entering a period (.). The certificate is generated after all the details are entered.

Step 7

Run the following commands to see the certificate requests:

```
openssl cat callserver-cert.csr
openssl cat vxml-cert.csr
openssl cat wsm-cert.csr
```

The encoded certificate request details are displayed.

```
-----BEGIN CERTIFICATE REQUEST-----
MIIBCjCBsQIBADBPMQswCQYDVQQGEwJJTjESMBAGA1UECAwJS0FSTkFUQUtBMQ0w
CwYDVQQHDARCR0xSMQ4wDAYDVQQKDAVDaXNjbzENMAsGA1UECwwEQ0NCVTBZMBMG
ByqGSM49AgEGCCqGSM49AwEHA0IABP3MPDdzf56f+9uuv6e0f7mqVuVOeM4JVaq0
B0Fx6PtKPiby3K85A36F16Ueh81Br5DUueMfnexlwl4RdIbiMn+gADAKBggqhkjO
PQQDAgNIADBFAiEA/z4mjLovTAWUzIHKm3yO5N//At9SBNoJnB8Uz5loRVUCIArL
FjU79myKyC90iJqWyL7b8xPqGrhk4pdNdGaOP/0j
-----END CERTIFICATE REQUEST-----
```

Step 8

Request for the CA-signed certificates:

Submit the callserver-cert.csr , vxml-cert.csr , and wsm-cert.csr to your CA (who can provide signed ECDSA certificates).

Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity.

CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format.

Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client.

Wait for the CA's reply.

Rename the certificate files received from the CA to callserver-cert.pem , vxml-cert.pem , and wsm-cert.pem respectively.

Step 9

From the command prompt, run the following commands to append the keys and certificates in one file:

```
cat callserver-private-key.pem callserver-cert.pem > callserver-certificate-private.pem
cat vxml-private-key.pem vxml-cert.pem > vxml-certificate-private.pem
cat wsm-private-key.pem wsm-cert.pem > wsm-certificate-private.pem
```

Step 10

Run the following commands to export the certificates to the Call server:

```
openssl pkcs12 -export -inkey callserver-private-key.pem -in callserver-certificate-private.pem -out cert_callserver.p12 -name callserver_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

```
openssl pkcs12 -export -inkey vxml-private-key.pem -in vxml-certificate-private.pem -out cert_vxml.p12 -name vxml_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

```
openssl pkcs12 -export -inkey wsm-private-key.pem -in wsm-certificate-private.pem -out cert_wsm.p12 -name wsm_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

Step 11

Go to c:\cisco\cvp\conf\security and run the following commands to delete the existing RSA certificates for Call server, VXML server, and WSM servers:

```
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias callserver-certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias vxml_certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias wsm_certificate -storepass <CVP keystore password>
```

Step 12

Go to c:\cisco\cvp\conf\security and import the root certificate to the keystore:

```
c:\cisco\CVP\jre\bin\keytool.exe -keystore .keystore -storetype JCEKS -import -alias root -trustcacerts -file <filename_of_root_cert>
```

Also, import the intermediate certificates shared by the CA to the keystore.

Step 13

Run the following commands to import the ECDSA certificates to the keystore:

```
c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_callserver.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias callserver_certificate
Importing keystore cert_callserver.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_vxml.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias vxml_certificate
Importing keystore cert_vxml.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_wsm.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias wsm_certificate
Importing keystore cert_wsm.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]
```

Step 14

Restart the Call server, VXML server, and WSM services from Windows services.

Step 15

In new browser tabs, type the following and check the certificates:

```
https://<callserver ip>:8443
https://<vxmlserver ip>:7443
https://<wsm ip>:8111
```

##### What to do next

Generate ECDSA certificates on the OAMP server.

#### On OAMP Server

Step 1

Log into the OAMP Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 2

Download OpenSSL (64 bit) and install on your machine.

Step 3

Add OpenSSL bin path to the Windows environment path variable.

Example: path=C:\Program Files\OpenSSL-Win64\bin

Step 4

Go to C:\Cisco\CVP\conf\security .

Step 5

From the command prompt, run the following commands to generate the private keys and the CSRs (for the OAMP server and WSM
                                             server) respectively:

OAMP server:

```
openssl ecparam -name prime256v1 -genkey -noout -out oamp-private-key.pem
openssl req -new -key oamp-private-key.pem -out oamp-cert.csr -days 360
```

WSM server:

```
openssl ecparam -name prime256v1 -genkey -noout -out wsm-private-key.pem
openssl req -new -key wsm-private-key.pem -out wsm-cert.csr -days 360
```

Step 6

Enter the values for the following fields when prompted:

```
Country Name (2 letter code) []:<>
State or Province Name (full name) []:<>
Locality Name (eg, city) []:<>
Organization Name (eg, company) []:<>
Organizational Unit Name (eg, section) []:<>
Common Name (eg, server FQDN or your name) []:.
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:.
```

This information is incorporated in your certificate request. Some fields ( Common Name , Email Address , A challenge password , and An optional company name ) can be left blank by entering a period (.). The certificate is generated after all the details are entered.

Step 7

Run the following commands to see the certificate requests:

```
openssl cat oamp-cert.csr
openssl cat wsm-cert.csr
```

The encoded certificate request details are displayed.

Step 8

Request for the CA-signed certificates:

Submit the oamp-cert.csr and wsm-cert.csr files to your CA (who can provide signed ECDSA certificates).

Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity.

CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format.

Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client.

Wait for the CA's reply.

Rename the certificate files received from the CA to oamp-cert.pem and wsm-cert.pem respectively.

Step 9

From the command prompt, run the following commands to append the keys and certificates in one file:

```
cat oamp-private-key.pem oamp-cert.pem > oamp-certificate-private.pem
cat wsm-private-key.pem wsm-cert.pem > wsm-certificate-private.pem
```

Step 10

Run the following commands to export the certificates to the OAMP server:

```
openssl pkcs12 -export -inkey oamp-private-key.pem -in oamp-certificate-private.pem -out cert_oamp.p12 -name oamp_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

```
openssl pkcs12 -export -inkey wsm-private-key.pem -in wsm-certificate-private.pem -out cert_wsm.p12 -name wsm_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

Step 11

Go to c:\cisco\cvp\conf\security and run the following commands to delete the existing RSA certificates for OAMP server and WSM server:

```
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias oamp_certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias wsm_certificate -storepass <CVP keystore password>
```

Step 12

Go to c:\cisco\cvp\conf\security and import the root certificate to the keystore:

```
c:\cisco\CVP\jre\bin\keytool.exe -keystore .keystore -storetype JCEKS -import -alias root -trustcacerts -file <filename_of_root_cert>
```

Also, import the intermediate certificates shared by the CA to the keystore.

Step 13

Run the following commands to import the ECDSA certificates to the keystore:

```
c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_oamp.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias oamp_certificate
Importing keystore cert_oamp.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_wsm.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias wsm_certificate
Importing keystore cert_wsm.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]
```

Step 14

Restart the OAMP and WSM servers from Windows services.

Step 15

In new browser tabs, type the following and check the certificates:

```
https://<wsm ip>:8111
https://<oamp ip>:9443
```

##### What to do next

Generate ECDSA certificates on the Reporting server.

#### On Reporting Server

Step 1

Log into the Reporting Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file.

Step 2

Download OpenSSL (64 bit) and install on your machine.

Step 3

Add OpenSSL bin path to the Windows environment path variable.

Example: path=C:\Program Files\OpenSSL-Win64\bin

Step 4

Go to C:\Cisco\CVP\conf\security .

Step 5

From the command prompt, run the following commands to generate the private keys and the CSRs for the Call server and WSM
                                             server:

Call server:

```
openssl ecparam -name prime256v1 -genkey -noout -out callserver-private-key.pem
openssl req -new -key callserver-private-key.pem -out callserver-cert.csr -days 360
```

WSM server:

```
openssl ecparam -name prime256v1 -genkey -noout -out wsm-private-key.pem
openssl req -new -key wsm-private-key.pem -out wsm-cert.csr -days 360
```

Step 6

Enter the values for the following fields when prompted:

```
Country Name (2 letter code) []:<>
State or Province Name (full name) []:<>
Locality Name (eg, city) []:<>
Organization Name (eg, company) []:<>
Organizational Unit Name (eg, section) []:<>
Common Name (eg, server FQDN or your name) []:.
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:.
```

This information is incorporated in your certificate request. Some fields ( Common Name , Email Address , A challenge password , and An optional company name ) can be left blank by entering a period (.). The certificate is generated after all the details are entered.

Step 7

Run the following commands to see the certificate requests:

```
openssl cat callserver-cert.csr
openssl cat wsm-cert.csr
```

The encoded certificate request details are displayed.

Step 8

Request for the CA-signed certificates:

Submit the callserver-cert.csr and wsm-cert.csr files to your CA (who can provide signed ECDSA certificates).

Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity.

CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format.

Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client.

Wait for the CA's reply.

Rename the certificate files received from the CA to callserver-cert.pem and wsm-cert.pem respectively.

Step 9

From the command prompt, run the following commands to append the keys and certificates in one file:

```
cat callserver-private-key.pem callserver-cert.pem > callserver-certificate-private.pem
cat wsm-private-key.pem wsm-cert.pem > wsm-certificate-private.pem
```

Step 10

Run the following commands to export the certificates to the Reporting server:

```
openssl pkcs12 -export -inkey callserver-private-key.pem -in callserver-certificate-private.pem -out callserver-cert.p12 -name callserver_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

```
openssl pkcs12 -export -inkey wsm-private-key.pem -in wsm-certificate-private.pem -out cert_wsm.p12 -name wsm_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password>
```

Step 11

Go to c:\cisco\cvp\conf\security and run the following commands to delete the existing RSA certificates for the Reporting server and WSM server:

```
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias callserver-certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias wsm_certificate -storepass <CVP keystore password>
```

Step 12

Go to c:\cisco\cvp\conf\security and import the root certificate to the keystore:

```
c:\cisco\CVP\jre\bin\keytool.exe -keystore .keystore -storetype JCEKS -import -alias root -trustcacerts -file <filename_of_root_cert>
```

Also, import the intermediate certificates shared by the CA to the keystore.

Step 13

Run the following commands to import the ECDSA certificates to the keystore:

```
c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore callserver-cert.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias callserver_certificate
Importing keystore callserver-cert.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_wsm.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias wsm_certificate
Importing keystore cert_wsm.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]
```

Step 14

Restart the Reporting and WSM servers from Windows services.

Step 15

In new browser tabs, type the following and check the certificates:

```
https://<callserver ip>:8443
https://<wsm ip>:8111
```

## Upgrading to OpenJDK JRE

A new CVP 15.0(1) base installer is available with OpenJDK JRE (17.0.13) as the supporting Java run time for the Unified CVP
                           application. It is an upgrade to the preceding 12.5(1) or 12.6(2) installer, except that in the 12.5(1) or 12.6(2) base installer,
                           the Java runtime environment is installed on the Unified CVP virtual machines (VMs).

Its predecessor, the 12.x installer, employs Oracle JRE.

To verify the base installer version, go to Control Panel > Programs > Programs and Features > Cisco CVP <version> .

For migrating Unified CVP 15.0(1) to OpenJDK, see Upgrading to OpenJDK JRE .

| Note | This release supports only TLS 1.2. For more information, see Contact Center Enterprise Solution Compatibility Matrix at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/tsd-products-support-series-home.html . To configure TLS Cipher on CVP server , see TLS Cipher Configuration . As per security guidelines, limit the validity of the generated or the requested SSL certificates to 2-3 years or shorter. If you are testing with the self-signed TLS certificates that are generated as a part of the installation, ensure that you
                                          map the CN/SANs on the certificate to the corresponding IP through DNS or hosts file entries. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. Ensure that the common name of the certificate matches the Fully Qualified Domain Name (FQDN) or hostname of the machine. |
|---|---|

| Step 1 | Import the certificate to the callserver keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                wsm_oamp_certificate -file %CVP_HOME%\conf\security\<oamp_security.cer> . |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Restart the Operation Console Server and the Call Server. |

| Note | At the command prompt, enter more %CVP_HOME%\conf\security.properties . Security.keystorePW = <Returns the keystore password> Enter the keystore password when prompted. |
|---|---|

| Step 1 | Export the OAMP certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\<oamp_security.cer> . |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Copy the WSM certificate you exported from the Call Server/VXML Server/Reporting Server to %CVP_HOME%\conf\security\ and import the certificate to the callserver key store by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                oamp_wsm_certificate -file %CVP_HOME%\conf\security\<wsm_security.cer> . |
| Step 4 | Enter the keystore password when prompted. |

| Note | At the command prompt, enter more %CVP_HOME%\conf\security.properties . Security.keystorePW = <Returns the keystore password> Enter the keystore password when prompted. |
|---|---|

| Step 1 | Export the WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias wsm_certificate
                                                -file %CVP_HOME%\conf\security\<wsm_security.cer> . |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Copy the OAMP certificate exported from the OAMP to %CVP_HOME%\conf\security\ and import the certificate to the callserver keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                wsm_oamp_certificate -file %CVP_HOME%\conf\security\<oamp_security.cer> . |
| Step 4 | Enter the keystore password when prompted. |
| Step 5 | Import the WSM certificate into the call server keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                vxml_wsm_certificate -file %CVP_HOME%\conf\security\<wsm_security.cer> . |
| Step 6 | Enter the keystore password when prompted. Note Repeat the preceding steps for the Call Server, VXML Server, and Reporting Server. | Note | Repeat the preceding steps for the Call Server, VXML Server, and Reporting Server. |
| Note | Repeat the preceding steps for the Call Server, VXML Server, and Reporting Server. |

| Note | Repeat the preceding steps for the Call Server, VXML Server, and Reporting Server. |
|---|---|

| Note | To enable Courtesy Callback feature in the secure mode, you must exchange the Call Server and Reporting Server certificates
                                                and place the certificates in %CVP_HOME%\conf\security\.keystore of each server. |
|---|---|

| Step 1 | Export the following certificates: WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias wsm_certificate
                                                      -file %CVP_HOME%\conf\security\wsm_security.cer Call Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias callserver_certificate
                                                      -file %CVP_HOME%\conf\security\callserver_security.cer VXML Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias vxml_certificate
                                                      -file %CVP_HOME%\conf\security\vxml_security.cer Note VXML certificate is not applicable for Reporting Server. | Note | VXML certificate is not applicable for Reporting Server. |
|---|---|---|---|
| Note | VXML certificate is not applicable for Reporting Server. |
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Copy all the generated certificates from the %CVP_HOME%\conf\security\ folder of the Call/VXML/Reporting Server machine to the %CVP_HOME%\conf\security\ folder on the OAMP machine. |
| Step 4 | On the OAMP machine, export the OAMP Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\oamp_security.cer |
| Step 5 | Enter the keystore password when prompted. |
| Step 6 | Copy the generated OAMP Server certificate from the %CVP_HOME%\conf\security\ folder of the OAMP machine to the %CVP_HOME%\conf\security\ folder of the CVP/Reporting Server machine. |
| Step 7 | On the CVP/Reporting Server machine, import the OAMP Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                oamp_certificate -file %CVP_HOME%\conf\security\oamp_security.cer |
| Step 8 | Enter the keystore password when prompted. |
| Step 9 | Trust this certificate? [no]: yes |
| Step 10 | Configure WSM in CVP: Go to c:\cisco\cvp\conf\jmx_wsm.conf Add or update the file as shown and save it: javax.net.debug = all
com.sun.management.jmxremote.ssl.need.client.auth= false com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=2099
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=3000 javax.net.ssl.keyStore= C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword= <keystore_password> |
| Step 11 | Run the regedit command. Append the following to the file at: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\Webservices Manager\Parameters\Java Note The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
Djavax.net.ssl.trustStorePassword=<keystore_password> 
Djavax.net.ssl.trustStoreType=JCEKS | Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
| Step 12 | Configure JMX of callserver in CVP. Go to c:\cisco\cvp\conf\jmx_callserver.conf . Update the file as shown and save the file: com.sun.management.jmxremote.ssl.need.client.auth= false com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=2098
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=2097 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore_password> |
| Step 13 | Configure JMX of VXMLServer in CVP. Go to c:\cisco\cvp\conf\jmx_vxml.conf . Edit the file as shown and save the file: com.sun.management.jmxremote.ssl.need.client.auth= false com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=9696
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=9697 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore_password> |
| Step 14 | Run the regedit command. Append the following to the file at: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\VXML\Parameters\Java Note The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
Djavax.net.ssl.trustStorePassword=<keystore_password> 
Djavax.net.ssl.trustStoreType=JCEKS | Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
| Step 15 | Restart the Operation Console Server and the Call Server machines. |

| Note | VXML certificate is not applicable for Reporting Server. |
|---|---|

| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
|---|---|

| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
|---|---|

| Step 1 | Import the following certificates: WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                      oamp_wsm_certificate -file %CVP_HOME%\conf\security\wsm_security.cer Call Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                      oamp_callserver_certificate -file %CVP_HOME%\conf\security\callserver_security.cer VXML Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                      oamp_vxml_certificate -file %CVP_HOME%\conf\security\vxml_security.cer |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Trust this certificate? [no]: yes |
| Step 4 | Restart OAMP service. |
| Step 5 | Log into OAMP. To enable secure communication between OAMP and Call Server or VXML Server or Reporting Server, navigate to Device Management > Call Server . Check the Enable secure communication with the Ops console check box. Save and deploy both Call Server and VXML Server. |

| Note | At the command prompt, enter more %CVP_HOME%\conf\security.properties Security.keystorePW = <Returns the keystore password> Enter the keystore password when prompted. |
|---|---|

| Step 1 | Generate CSR on OAMP by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\oamp.csr |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Sign the certificate on a CA. |
| Step 4 | Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\ |
| Step 5 | Import the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                root -file %CVP_HOME%\conf\security\<filename_of_root_cert> |
| Step 6 | Enter the keystore password when prompted. |
| Step 7 | Import the CA-signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                oamp_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert> |
| Step 8 | Run the regedit command: Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\OPSConsoleServer\Parameters\Java\Options Note The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                            that the required trust certificates are imported into the appropriate keystore Append the following to the file: -Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore
-Djavax.net.ssl.trustStorePassword=<keystore_password>
-Djavax.net.ssl.trustStoreType=JCEKS | Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                            that the required trust certificates are imported into the appropriate keystore |
| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                            that the required trust certificates are imported into the appropriate keystore |

| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                            that the required trust certificates are imported into the appropriate keystore |
|---|---|

| Note | At the command prompt, enter more %CVP_HOME%\conf\security.properties Security.keystorePW = <Returns the keystore password> Enter the keystore password when prompted. |
|---|---|

| Step 1 | Generate CSR on Call Server by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias callserver_certificate
                                                -file %CVP_HOME%\conf\security\callserver.csr |
|---|---|
| Step 2 | Repeat Step 1 for VXML Server, Reporting Server, and WSM Server. |
| Step 3 | Sign the certificate on a CA. |
| Step 4 | Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\ |
| Step 5 | Import the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                root -file %CVP_HOME%\conf\security\<filename_of_root_cert> |
| Step 6 | Enter the keystore password when prompted. |
| Step 7 | Import the CA-signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                callserver_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert> |
| Step 8 | Repeat Step 7 for VXML Server, Reporting Server, and WSM Server. |
| Step 9 | Configure WSM in CVP: Go to c:/cisco/cvp/conf/jmx_wsm.conf Add or update the file as shown and save it: javax.net.debug = all
com.sun.management.jmxremote.ssl.need.client.auth = true com.sun.management.jmxremote.authenticate = false
com.sun.management.jmxremote.port = 2099
com.sun.management.jmxremote.ssl = true com.sun.management.jmxremote.rmi.port = 3000 javax.net.ssl.keyStore= C:/Cisco/CVP/conf/security/.keystore
javax.net.ssl.keyStorePassword= <keystore_password> |
| Step 10 | Configure JMX of callserver in CVP: Go to c:/cisco/cvp/conf/jmx_callserver.conf Update the file as shown and save the file: com.sun.management.jmxremote.ssl.need.client.auth = true com.sun.management.jmxremote.authenticate = false
com.sun.management.jmxremote.port = 2098
com.sun.management.jmxremote.ssl = true com.sun.management.jmxremote.rmi.port = 2097 javax.net.ssl.keyStore= C:/Cisco/CVP/conf/security/.keystore
javax.net.ssl.keyStorePassword= <keystore_password> Run the regedit command. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\WebServicesManager\Parameters\Java\Options. Append the following to the file: Note The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore -Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
-Djavax.net.ssl.trustStorePassword=<keystore_password> 
-Djavax.net.ssl.trustStoreType=JCEKS | Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
| Step 11 | Configure JMX of VXMLServer in CVP: Go to c:/cisco/cvp/conf/jmx_vxml.conf Edit the file as shown and save the file: com.sun.management.jmxremote.ssl.need.client.auth = true com.sun.management.jmxremote.authenticate = false
com.sun.management.jmxremote.port = 9696
com.sun.management.jmxremote.ssl = true com.sun.management.jmxremote.rmi.port = 9697 javax.net.ssl.keyStore = C:/Cisco/CVP/conf/security/.keystore
javax.net.ssl.keyStorePassword = <keystore_password> |
| Step 12 | Restart the Operation Console Server and the CVP server. Note To enable Courtesy Callback feature in the secure mode, add the CA root certificate to Tomcat truststore .keystore in %CVP_HOME%\jre\bin>keytool.exe -keystore%CVP_HOME%\conf\\security\.keystore -storepass changeit -importcert -file %CVP_HOME%\conf\security\CA_Root.cer | Note | To enable Courtesy Callback feature in the secure mode, add the CA root certificate to Tomcat truststore .keystore in %CVP_HOME%\jre\bin>keytool.exe -keystore%CVP_HOME%\conf\\security\.keystore -storepass changeit -importcert -file %CVP_HOME%\conf\security\CA_Root.cer |
| Note | To enable Courtesy Callback feature in the secure mode, add the CA root certificate to Tomcat truststore .keystore in %CVP_HOME%\jre\bin>keytool.exe -keystore%CVP_HOME%\conf\\security\.keystore -storepass changeit -importcert -file %CVP_HOME%\conf\security\CA_Root.cer |
| Step 13 | Repeat the steps for Call Server, VXML Server, and Reporting Server. |

| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
|---|---|

| Note | To enable Courtesy Callback feature in the secure mode, add the CA root certificate to Tomcat truststore .keystore in %CVP_HOME%\jre\bin>keytool.exe -keystore%CVP_HOME%\conf\\security\.keystore -storepass changeit -importcert -file %CVP_HOME%\conf\security\CA_Root.cer |
|---|---|

| Step 1 | Import the certificate to the callserver keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                wsm_oamp_certificate -file %CVP_HOME%\conf\security\<oamp_security.cer> . |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Restart the Operation Console Server and the Call Server. |

| Note | At the command prompt, enter more %CVP_HOME%\conf\security.properties . Security.keystorePW = <Returns the keystore password> Enter the keystore password when prompted. |
|---|---|

| Step 1 | Export the OAMP certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\<oamp_security.cer> . |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Copy the WSM certificate you exported from the Call Server/VXML Server/Reporting Server to %CVP_HOME%\conf\security\ and import the certificate to the callserver key store by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                oamp_wsm_certificate -file %CVP_HOME%\conf\security\<wsm_security.cer> . |
| Step 4 | Enter the keystore password when prompted. |

| Note | At the command prompt, enter more %CVP_HOME%\conf\security.properties . Security.keystorePW = <Returns the keystore password> Enter the keystore password when prompted. |
|---|---|

| Step 1 | Export the WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias wsm_certificate
                                                -file %CVP_HOME%\conf\security\<wsm_security.cer> . |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Copy the OAMP certificate exported from the OAMP to %CVP_HOME%\conf\security\ and import the certificate to the callserver keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                wsm_oamp_certificate -file %CVP_HOME%\conf\security\<oamp_security.cer> . |
| Step 4 | Enter the keystore password when prompted. |
| Step 5 | Import the WSM certificate into the call server keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                vxml_wsm_certificate -file %CVP_HOME%\conf\security\<wsm_security.cer> . |
| Step 6 | Enter the keystore password when prompted. Note Repeat the preceding steps for the Call Server, VXML Server, and Reporting Server. | Note | Repeat the preceding steps for the Call Server, VXML Server, and Reporting Server. |
| Note | Repeat the preceding steps for the Call Server, VXML Server, and Reporting Server. |

| Note | Repeat the preceding steps for the Call Server, VXML Server, and Reporting Server. |
|---|---|

| Note | To enable Courtesy Callback feature in the secure mode, you must exchange the Call Server and Reporting Server certificates
                                                and place the certificates in %CVP_HOME%\conf\security\.keystore of each server. |
|---|---|

| Step 1 | Export the following certificates: WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias wsm_certificate
                                                      -file %CVP_HOME%\conf\security\wsm_security.cer Call Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias callserver_certificate
                                                      -file %CVP_HOME%\conf\security\callserver_security.cer VXML Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias vxml_certificate
                                                      -file %CVP_HOME%\conf\security\vxml_security.cer Note VXML certificate is not applicable for Reporting Server. | Note | VXML certificate is not applicable for Reporting Server. |
|---|---|---|---|
| Note | VXML certificate is not applicable for Reporting Server. |
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Copy all the generated certificates from the %CVP_HOME%\conf\security\ folder of the Call/VXML/Reporting Server machine to the %CVP_HOME%\conf\security\ folder on the OAMP machine. |
| Step 4 | On the OAMP machine, export the OAMP Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\oamp_security.cer |
| Step 5 | Enter the keystore password when prompted. |
| Step 6 | Copy the generated OAMP Server certificate from the %CVP_HOME%\conf\security\ folder of the OAMP machine to the %CVP_HOME%\conf\security\ folder of the CVP/Reporting Server machine. |
| Step 7 | On the CVP/Reporting Server machine, import the OAMP Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                oamp_certificate -file %CVP_HOME%\conf\security\oamp_security.cer |
| Step 8 | Enter the keystore password when prompted. |
| Step 9 | Trust this certificate? [no]: yes |
| Step 10 | Configure WSM in CVP: Go to c:\cisco\cvp\conf\jmx_wsm.conf Add or update the file as shown and save it: javax.net.debug = all
com.sun.management.jmxremote.ssl.need.client.auth= false com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=2099
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=3000 javax.net.ssl.keyStore= C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword= <keystore_password> |
| Step 11 | Run the regedit command. Append the following to the file at: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\Webservices Manager\Parameters\Java Note The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
Djavax.net.ssl.trustStorePassword=<keystore_password> 
Djavax.net.ssl.trustStoreType=JCEKS | Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
| Step 12 | Configure JMX of callserver in CVP. Go to c:\cisco\cvp\conf\jmx_callserver.conf . Update the file as shown and save the file: com.sun.management.jmxremote.ssl.need.client.auth= false com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=2098
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=2097 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore_password> |
| Step 13 | Configure JMX of VXMLServer in CVP. Go to c:\cisco\cvp\conf\jmx_vxml.conf . Edit the file as shown and save the file: com.sun.management.jmxremote.ssl.need.client.auth= false com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=9696
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=9697 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore_password> |
| Step 14 | Run the regedit command. Append the following to the file at: HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\VXML\Parameters\Java Note The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
Djavax.net.ssl.trustStorePassword=<keystore_password> 
Djavax.net.ssl.trustStoreType=JCEKS | Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
| Step 15 | Restart the Operation Console Server and the Call Server machines. |

| Note | VXML certificate is not applicable for Reporting Server. |
|---|---|

| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
|---|---|

| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                                  that the required trust certificates are imported into the appropriate keystore |
|---|---|

| Step 1 | Import the following certificates: WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                      oamp_wsm_certificate -file %CVP_HOME%\conf\security\wsm_security.cer Call Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                      oamp_callserver_certificate -file %CVP_HOME%\conf\security\callserver_security.cer VXML Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                      oamp_vxml_certificate -file %CVP_HOME%\conf\security\vxml_security.cer |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Trust this certificate? [no]: yes |
| Step 4 | Restart OAMP service. |
| Step 5 | Log into OAMP. To enable secure communication between OAMP and Call Server or VXML Server or Reporting Server, navigate to Device Management > Call Server . Check the Enable secure communication with the Ops console check box. Save and deploy both Call Server and VXML Server. |

| Step 1 | Go to %CVP_HOME%\conf\security and delete the WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -delete -alias wsm_certificate . Enter the keystore password when prompted. |
|---|---|
| Step 2 | Repeat Step 1 for Call Server certificate ( callserver_certificate ) and VXML Server certificate ( vxml_certificate ) on the CVP Server and Call Server Certificate ( callserver_certificate ) on the Reporting Server. |
| Step 3 | Generate a CA-signed certificate for WSM server by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias wsm_certificate
                                                -v -keysize 2048 -keyalg RSA . Enter the keystore password when prompted. Enter the details at the prompts and type Yes to confirm. Note Note the CN name for future reference. | Note | Note the CN name for future reference. |
| Note | Note the CN name for future reference. |
| Step 4 | Generate the certificate request for the alias by running the following command and saving it to a file (for example, wsm.csr ): %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias wsm_certificate
                                                -file %CVP_HOME%\conf\security\wsm.csr . Enter the keystore password when prompted. |
| Step 5 | Get the certificate signed by a CA. Use the procedure to create a CA-signed certificate with the CA authority and ensure to
                                          use a Client-Server Certificate Authentication template when the CA generate the signed certificate. |
| Step 6 | Download the signed certificate, the root and intermediate certificate of the CA authority. |
| Step 7 | Copy the root, intermediate, and the CA-signed WSM  to %CVP_HOME%\conf\security\ . |
| Step 8 | Import the root certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                root -file %CVP_HOME%\conf\security\<filename_of_root_cer> . Enter the keystore password when prompted. At Trust this certificate prompt, type Yes . |
| Step 9 | Import the intermediate certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                intermediate -file %CVP_HOME%\conf\security\<filename_of_intermediate_cer> . Enter the keystore password when prompted. At Trust this certificate prompt, type Yes . |
| Step 10 | Import the CA-signed WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                wsm_certificate -file %CVP_HOME%\conf\security\<filename_of_your_signed_cert_from_CA> . Enter the keystore password when prompted. |
| Step 11 | Repeat Step 3 to 10 (root and intermediate certificates do not need to be imported twice), for Call Server and VXML Server certificates on the
                                          CVP Server and Call Server certificate on the Reporting Server. |
| Step 12 | Configure WSM in CVP Server and CVP Reporting Server : Go to c:\cisco\cvp\conf\jmx_wsm.conf Add or update the file as shown and save it: javax.net.debug = all
com.sun.management.jmxremote.ssl.need.client.auth= true com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=2099
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=3000 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore_password >
javax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
javax.net.ssl.trustStorePassword=<keystore_password >
javax.net.ssl.trustStoreType=JCEKS Run the regedit command. Append the following to the file at HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\WebServicesManager\Parameters\Java : Note The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore Append this to the file at HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\WebServicesManager\Parameters\Java:

-Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
-Djavax.net.ssl.trustStorePassword=<keystore_password> 
-Djavax.net.ssl.trustStoreType=JCEKS | Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore |
| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore |
| Step 13 | Configure JMX of callserver in CVP Server and CVP Reporting Server : Go to c:\cisco\cvp\conf\jmx_callserver.conf Update the file as shown and save the file: com.sun.management.jmxremote.ssl.need.client.auth= true com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=2098
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=2097 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore password>
javax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
javax.net.ssl.trustStorePassword=<keystore_password >
javax.net.ssl.trustStoreType=JCEKS |
| Step 14 | Configure JMX of VXMLServer in CVP server: Go to c:\cisco\cvp\conf\jmx_vxml.conf Edit the file as shown and save the file: com.sun.management.jmxremote.ssl.need.client.auth= true com.sun.management.jmxremote.authenticate=false
com.sun.management.jmxremote.port=9696
com.sun.management.jmxremote.ssl= true com.sun.management.jmxremote.rmi.port=9697 javax.net.ssl.keyStore=C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword=<keystore password> Run the regedit command. Append the following to the file at HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\VXMLServer\Parameters\Java : Note The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore Append theese to the file at HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\VXMLServer\Parameters\Java:

-Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore 
-Djavax.net.ssl.trustStorePassword=<keystore_password> 
-Djavax.net.ssl.trustStoreType=JCEKS Restart WSM service, Call Server and VXML Server services on CVP server and WSM Service and Call Server service on Reporting
                                                Server. Note When secure communication is enabled with JMX, it forces the keystore to be %CVP_HOME%\conf\security\.keystore , instead of %CVP_HOME%\jre\lib\security\cacerts . Therefore, the certificates from %CVP_HOME%\jre\lib\security\cacerts should be imported to %CVP_HOME%\conf\security\.keystore . | Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore | Note | When secure communication is enabled with JMX, it forces the keystore to be %CVP_HOME%\conf\security\.keystore , instead of %CVP_HOME%\jre\lib\security\cacerts . Therefore, the certificates from %CVP_HOME%\jre\lib\security\cacerts should be imported to %CVP_HOME%\conf\security\.keystore . |
| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore |
| Note | When secure communication is enabled with JMX, it forces the keystore to be %CVP_HOME%\conf\security\.keystore , instead of %CVP_HOME%\jre\lib\security\cacerts . Therefore, the certificates from %CVP_HOME%\jre\lib\security\cacerts should be imported to %CVP_HOME%\conf\security\.keystore . |

| Note | Note the CN name for future reference. |
|---|---|

| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore |
|---|---|

| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore |
|---|---|

| Note | When secure communication is enabled with JMX, it forces the keystore to be %CVP_HOME%\conf\security\.keystore , instead of %CVP_HOME%\jre\lib\security\cacerts . Therefore, the certificates from %CVP_HOME%\jre\lib\security\cacerts should be imported to %CVP_HOME%\conf\security\.keystore . |
|---|---|

| Step 1 | Go to %CVP_HOME%\conf\security and generate a CA-signed certificate for client authentication with callserver by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias <CN of CVP
                                                Server or Reporting Server WSM certificate> -v -keysize 2048 -keyalg RSA Enter the keystore password when prompted. Enter the details at the prompts and type Yes to confirm. Note The alias will be the same as the CN used for generating WSM certificate. | Note | The alias will be the same as the CN used for generating WSM certificate. |
|---|---|---|---|
| Note | The alias will be the same as the CN used for generating WSM certificate. |
| Step 2 | Generate the certificate request for the alias by running the following command and saving it to a file (for example, jmx_client.csr ): %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias <CN of CVP Server
                                                or Reporting Server WSM certificate> -file %CVP_HOME%\conf\security\jmx_client.csr Enter the keystore password when prompted. Verify that the CSR was generated successfully by running dir jmx_client.csr |
| Step 3 | Sign the JMX Client Certificate on a CA. Note Use the procedure to create a CA-signed certificate with the CA authority. Download the CA-signed JMX Client certificate (Root
                                                         and intermediate certificates are not required since they were downloaded and imported previously). | Note | Use the procedure to create a CA-signed certificate with the CA authority. Download the CA-signed JMX Client certificate (Root
                                                         and intermediate certificates are not required since they were downloaded and imported previously). |
| Note | Use the procedure to create a CA-signed certificate with the CA authority. Download the CA-signed JMX Client certificate (Root
                                                         and intermediate certificates are not required since they were downloaded and imported previously). |
| Step 4 | Copy the CA-signed JMX Client certificate to %CVP_HOME%\conf\security\ . |
| Step 5 | Import the CA-signed JMX Client certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                <CN of CVP Server or Reporting Server WSM certificate> -file %CVP_HOME%\conf\security\<filename of CA-signed JMX Client certificate> Enter the keystore password when prompted. |
| Step 6 | Restart Cisco CVP Call Server, VXML Server, and WSM services. Note Repeat the same procedure for Reporting Server, if any. | Note | Repeat the same procedure for Reporting Server, if any. |
| Note | Repeat the same procedure for Reporting Server, if any. |

| Note | The alias will be the same as the CN used for generating WSM certificate. |
|---|---|

| Note | Use the procedure to create a CA-signed certificate with the CA authority. Download the CA-signed JMX Client certificate (Root
                                                         and intermediate certificates are not required since they were downloaded and imported previously). |
|---|---|

| Note | Repeat the same procedure for Reporting Server, if any. |
|---|---|

| Step 1 | Go to %CVP_HOME%\conf\security and generate a CA-signed certificate for client authentication with callserver WSM by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias <CN of CVP
                                             Server or CVP Reporting Server WSM certificate> -v -keysize 2048 -keyalg RSA . Enter the keystore password when prompted. Enter the details at the prompts and type Yes to confirm. Note The alias will be the same as the CN of the Call Server or the VXML Server. Note Ensure that you enter the details of the OAMP server while creating the certificate. | Note | The alias will be the same as the CN of the Call Server or the VXML Server. | Note | Ensure that you enter the details of the OAMP server while creating the certificate. |
|---|---|---|---|---|---|
| Note | The alias will be the same as the CN of the Call Server or the VXML Server. |
| Note | Ensure that you enter the details of the OAMP server while creating the certificate. |
| Step 2 | Generate the certificate request for the alias by running the following command and saving it to a file (for example, jmx.csr): %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias <CN of CVP Server
                                             or CVP Reporting Server WSM certificate> -file %CVP_HOME%\conf\security\jmx.csr . Enter the keystore password when prompted. |
| Step 3 | Sign the certificate on a CA. Note Follow the procedure to create a CA-signed certificate using the CA authority. Download the certificate and the root certificate
                                                         of the CA authority. | Note | Follow the procedure to create a CA-signed certificate using the CA authority. Download the certificate and the root certificate
                                                         of the CA authority. |
| Note | Follow the procedure to create a CA-signed certificate using the CA authority. Download the certificate and the root certificate
                                                         of the CA authority. |
| Step 4 | Copy the root certificate and CA-signed JMX Client certificate to %CVP_HOME%\conf\security\ . |
| Step 5 | Import the root certificate of the CA by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                             root -file %CVP_HOME%\conf\security\<filename_of_root_cert> . Enter the keystore password when prompted. At Trust this certificate prompt, type Yes . |
| Step 6 | Import the CA-signed JMX Client certificate of CVP Server and CVP Reporting Server by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                             <CN of CVP Server or CVP Reporting Server WSM certificate> -file %CVP_HOME%\conf\security\<filename_of_your_signed_cert_from_CA> . Enter the keystore password when prompted. |
| Step 7 | Restart OAMP service. |
| Step 8 | Log into OAMP. To enable secure communication between OAMP and Call Server or VXML Server, navigate to Device Management > Call Server or Device Management > VXML Server . Check the Enable secure communication with the Ops console check box. Save and deploy both Call Server and VXML Server. |
| Step 9 | Run the regedit command. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\Procrun 2.0\OPSConsoleServer\Parameters\Java . Append the following to the file sand save it: Note The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore Djavax.net.ssl.trustStore=C:\Cisco\CVP\conf\security\.keystore
Djavax.net.ssl.trustStorePassword=<keystore_password>
Djavax.net.ssl.trustStoreType=JCEKS Note After securing the ports for JMX, JConsole can be accessed only after performing the defined steps for JConsole listed in
                                                         the OpenJDK docs. Note After securing the ports for JMX, JConsole can be accessed only after performing the defined steps for JConsole listed in
                                                         the Oracle docs. | Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore | Note | After securing the ports for JMX, JConsole can be accessed only after performing the defined steps for JConsole listed in
                                                         the OpenJDK docs. | Note | After securing the ports for JMX, JConsole can be accessed only after performing the defined steps for JConsole listed in
                                                         the Oracle docs. |
| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore |
| Note | After securing the ports for JMX, JConsole can be accessed only after performing the defined steps for JConsole listed in
                                                         the OpenJDK docs. |
| Note | After securing the ports for JMX, JConsole can be accessed only after performing the defined steps for JConsole listed in
                                                         the Oracle docs. |
| Step 10 | Restart the OAMP service. |

| Note | The alias will be the same as the CN of the Call Server or the VXML Server. |
|---|---|

| Note | Ensure that you enter the details of the OAMP server while creating the certificate. |
|---|---|

| Note | Follow the procedure to create a CA-signed certificate using the CA authority. Download the certificate and the root certificate
                                                         of the CA authority. |
|---|---|

| Note | The following registry entries are added by default. However, if a custom Java application uses a different keystore, ensure
                                                               that the required trust certificates are imported into the appropriate keystore |
|---|---|

| Note | After securing the ports for JMX, JConsole can be accessed only after performing the defined steps for JConsole listed in
                                                         the OpenJDK docs. |
|---|---|

| Note | After securing the ports for JMX, JConsole can be accessed only after performing the defined steps for JConsole listed in
                                                         the Oracle docs. |
|---|---|

| Note | OAMP will stop the JMX communication with the following procedure but OAMP to Call Server/VXML Server / Reporting Server/WSM
                                             will continue to work. |
|---|---|

| Step 1 | Go to c:\cisco\cvp\conf\jmx_oamp.conf . Add the following to the file and save it: javax.net.debug = all
com.sun.management.jmxremote.ssl.need.client.auth = true com.sun.management.jmxremote.authenticate = false
com.sun.management.jmxremote.port = 10001
com.sun.management.jmxremote.ssl = true
#com.sun.management.jmxremote.ssl.config.file=
com.sun.management.jmxremote.rmi.port = 10000 |
|---|---|
| Step 2 | Restart the OpsConsoleServer service. |
| Step 3 | Go to c:\cisco\cvp\conf\jmx_wsm.conf . Add the following to the file and save it: javax.net.debug = all
com.sun.management.jmxremote.ssl.need.client.auth = true com.sun.management.jmxremote.authenticate = false
com.sun.management.jmxremote.port = 2099
com.sun.management.jmxremote.ssl = true
#com.sun.management.jmxremote.ssl.config.file=
com.sun.management.jmxremote.rmi.port = 3000
javax.net.ssl.keyStore= C:\Cisco\CVP\conf\security\.keystore
javax.net.ssl.keyStorePassword= <keystore_password> |
| Step 4 | Restart the WSM service. |

| Step 1 | Import the root CA certificate in the JRE keystore: Run the %CVP_HOME%\jre\bin\keytool.exe -keystore %CVP_HOME%\jre\lib\security\cacerts -import -v -trustcacerts -alias root -file %CVP_HOME%\conf\security\<filename_of_root_cert> command. Enter the keystore password when prompted. The default keystore password is changeit . Type Yes when the Trust this certificate prompt appears. |
|---|---|
| Step 2 | Restart the Cisco CVP CallServer service. |

| Note | To support AES 256 bit encryption-based ciphers (for example, TLS_RSA_WITH_AES_256_CBC_SHA256), JRE version in the Unified
                                             CVP server needs to be upgraded to Java 1.8u275. If you are using SHA1 after upgrading the JRE version, then edit C:\Cisco\CVP\jre\lib\security\java.security file to remove the SHA1 jdkCA & usage TLSServer parameter from jdk.certpath.disabledAlgorithms configuration. |
|---|---|

| Note | When the Unified CVP Call Server, Media Server, and Unified CVP VXML Server are co-resident on the same server and use self-signed
                                          certificates, you can use a single self-signed certificate for all these services. This simplifies the certificate management
                                          process and ensures secure communication within the co-resident environment. |
|---|---|

| Step 1 | Export the Call Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias callserver_certificate
                                                -file %CVP_HOME%\conf\security\<callserver_certificate.cer> . |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Copy the VVB self-signed certificate to %CVP_HOME%\conf\security\ and import the certificate to the callserver keystore by running %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                vb_cert -file %CVP_HOME%\conf\security\<vvb certificate> . Note See Step 5 of the On Cisco VVB section to download a VVB certificate. | Note | See Step 5 of the On Cisco VVB section to download a VVB certificate. |
| Note | See Step 5 of the On Cisco VVB section to download a VVB certificate. |
| Step 4 | Enter the keystore password when prompted. A message appears on the screen: Trust this certificate? [no]: Enter yes . |
| Step 5 | Use the list flag to check your keystore entries by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -list . |

| Note | See Step 5 of the On Cisco VVB section to download a VVB certificate. |
|---|---|

| Step 1 | Copy the CVP CallServer self-signed certificate downloaded from CVP and upload it to VVB against tomcat-trust. |
|---|---|
| Step 2 | Go to OS Admin > Security > Certificate Management > Upload certificate/certificate chain . |
| Step 3 | In Certificate Purpose , select tomcat-trust . |
| Step 4 | Select the self-signed certificate of the Call Server and click Upload . |
| Step 5 | Download the self-signed certificate of the VVB. |
| Step 6 | Go to OS Admin > Security > Certificate Management . |
| Step 7 | In the Certificate column, find the certificate named tomcat . |
| Step 8 | Select the self-signed tomcat certificate and click Download . |
| Step 9 | After the new certificate is uploaded, restart the node(s) using the CLI command utils system restart . |
| Step 10 | Go to Cisco VVB Administration > System Parameters > TLS . |
| Step 11 | Check TLS as Enable . |
| Step 12 | Select the supported TLS version and click Update . |
| Step 13 | Restart Cisco VVB Engine from the VVB Serviceability page. |

| Attention | Repeat this procedure if you have multiple Call Servers. |
|---|---|

| Step 1 | To generate the CSR certificate on VVB, open the administration page. From the Navigation drop-down list, choose Cisco Unified OS Administration and click Go . |
|---|---|
| Step 2 | Go to Security > Certificate Management > Generate CSR Generate Certificate signing Request . Create the CSR against tomcat with the key-length as 2048. |
| Step 3 | To download the generated CSR, click Download CSR . After the Generate Certificate signing Request dialog opens, click Download CSR . |
| Step 4 | Open the certificate in Notepad, copy the contents and sign the certificate with CA. |
| Step 5 | Upload the root certificate generated from the CA into VVB against tomcat-trust: Go to Security > Certificate Management > Generate CSR > Upload certificate/certificate chain . Choose tomcat-trust from the drop-down list. Click Browse and select the certificate. Click Upload to upload the root certificate of the Certificate Authority. |
| Step 6 | Upload the signed certificate into VVB against tomcat. Go to Security > Certificate Management > Upload certificate/certificate chain . Choose tomcat from the drop-down list. Click Browse and select the certificate. Click Upload . After the certificate is uploaded successfully, VVB displays the certificate signed by <CA hostname>. |
| Step 7 | Restart the Tomcat service and the VVB engine. |

| Step 1 | Export the VXML SERVER certificate by running %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias vxml_certificate
                                                -file %CVP_HOME%\conf\security\<vxml_certificate.cer> . |
|---|---|
| Step 2 | Enter the keystore password when prompted. |
| Step 3 | Copy the Cisco VVB self-signed certificate to %CVP_HOME%\conf\security\ and import the certificate to the callserver keystore by running keystore.%CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS
                                                -alias vb_cert -file %CVP_HOME%\conf\security\<vvb certificate> . Note See Step 5 of the following Section, On Cisco VVB to download a VVB certificate. | Note | See Step 5 of the following Section, On Cisco VVB to download a VVB certificate. |
| Note | See Step 5 of the following Section, On Cisco VVB to download a VVB certificate. |
| Step 4 | Enter the keystore password when prompted. A message appears on the screen: Trust this certificate? [no]: Enter yes . |
| Step 5 | Use the list flag to check your keystore entries by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -list . |

| Note | See Step 5 of the following Section, On Cisco VVB to download a VVB certificate. |
|---|---|

| Step 1 | Copy the VXML Server self-signed certificate downloaded from CVP and upload it to VVB against tomcat-trust. |
|---|---|
| Step 2 | Go to OS Admin > Security > Certificate Management > Upload certificate/certificate chain . |
| Step 3 | In Certificate Purpose , select tomcat-trust . |
| Step 4 | Select the self-signed certificate of the VXML Server and click Upload . |
| Step 5 | Download the self-signed certificate of the VVB. |
| Step 6 | Go to OS Admin > Security > Certificate Management . |
| Step 7 | In the Certificate column, select the tomcat certificate. |
| Step 8 | Select the tomcat certificate and click Download . |
| Step 9 | After the new certificate uploads, restart the Cisco Tomcat service. |
| Step 10 | Go to Cisco VVB Administration > System Parameters > TLS . |
| Step 11 | Check the TLS check box as Enable . |
| Step 12 | Select the supported TLS version and click Update . |
| Step 13 | Restart the Cisco VVB Engine from the VVB Serviceability page. Note To enable secured connection in Application Management from the Cisco VVB UI, see Cisco Virtualized Voice Browser Administration and Configuration Guide available at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html . | Note | To enable secured connection in Application Management from the Cisco VVB UI, see Cisco Virtualized Voice Browser Administration and Configuration Guide available at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html . |
| Note | To enable secured connection in Application Management from the Cisco VVB UI, see Cisco Virtualized Voice Browser Administration and Configuration Guide available at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html . |

| Note | To enable secured connection in Application Management from the Cisco VVB UI, see Cisco Virtualized Voice Browser Administration and Configuration Guide available at https://www.cisco.com/c/en/us/support/customer-collaboration/virtualized-voice-browser/tsd-products-support-series-home.html . |
|---|---|

| Step 1 | Remove the existing certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -delete -alias vxml_certificate . |
|---|---|
| Step 2 | Generate a new key pair for the alias with selected key size by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias vxml_certificate
                                                -v -keysize 2048 -keyalg RSA . Enter keystore password: <enter the keystore password>
What is your first and last name?
 [Unknown]: <specify the CVP host name appended with "VXML_Server"> E.g cisco-cvp-211_VXML_Server
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
Specify ‘yes’ for the inputs. |
| Step 3 | Generate the CSR certificate for the alias by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias vxml_certificate
                                                -file %CVP_HOME%\conf\security\vxmlserver.csr and save it to a file (for example, oamp.csr) . |
| Step 4 | Enter the
                                             			 keystore password when prompted. |
| Step 5 | Download the vxmserver.csr from CVP %CVP_HOME%\conf\security\ and sign it from CA. |
| Step 6 | Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\ |
| Step 7 | Install the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                root -file %CVP_HOME%\conf\security\<filename_of_root_cert> . |
| Step 8 | Enter the
                                             			 keystore password when prompted. |
| Step 9 | Install the signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                vxml_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert> . |
| Step 10 | Enter the
                                             			 keystore password when prompted. |
| Step 11 | Restart the
                                             			 VXML Server. |

| Step 1 | Upload the root certificate generated from the CA into VVB against tomcat-trust. Go to OS Admin > Security > Certificate Management > Upload certificate/certificate chain , select tomcat-trust and upload the root certificate of the Certificate Authority. Note If you use the same root certificate that was used in the Call Server configuration as described in Section, Secure Communication
                                                            between Call Server and Cisco VVB and the certificate is already imported, then you can skip this step. | Note | If you use the same root certificate that was used in the Call Server configuration as described in Section, Secure Communication
                                                            between Call Server and Cisco VVB and the certificate is already imported, then you can skip this step. |
|---|---|---|---|
| Note | If you use the same root certificate that was used in the Call Server configuration as described in Section, Secure Communication
                                                            between Call Server and Cisco VVB and the certificate is already imported, then you can skip this step. |
| Step 2 | Generate the CSR against tomcat with the key-length as 2048. |
| Step 3 | Open the certificate in Notepad. Copy the contents and sign the certificate with CA. |
| Step 4 | Restart the Tomcat service and the VVB engine. |

| Note | If you use the same root certificate that was used in the Call Server configuration as described in Section, Secure Communication
                                                            between Call Server and Cisco VVB and the certificate is already imported, then you can skip this step. |
|---|---|

| Step 1 | Enter https://<mediaserver>:443/ in the address bar of the web browser. |
|---|---|
| Step 2 | In the Security Alert dialog box, click View Certificate . |
| Step 3 | Click the Details tab |
| Step 4 | Click Copy to File . |
| Step 5 | In the Certificate Export Wizard dialog box, click Base-64 encoded X.509 (.CER) , and then click Next . |
| Step 6 | In the File to the Export dialog box, specify a file name, and then click Next . |
| Step 7 | Click Finish . A message indicates that the export was successful. |
| Step 8 | Click OK and close the Security Alert dialog box. |
| Step 9 | Copy the CVP MediaServer self-signed certificate downloaded from the CVP and upload into VVB against tomcat-trust . |
| Step 10 | Go to OS Admin > Security > Certificate Management > Upload certificate/certificate chain > In Certificate Purpose* select tomcat-trust , choose the self-signed certificate of the Call Server and press Upload button. |
| Step 11 | Restart Cisco VVB Engine. |

| Step 1 | Sign in to Cisco Unified OS Administration on the VVB server (https://<FQDN of VVB server>/cmplatform). |
|---|---|
| Step 2 | Go to Security > Certificate Management . |
| Step 3 | Click Find . |
| Step 4 | Perform one of the following steps. If the tomcat certificate for your server is not on the list, click Generate Self-signed . When the certificate is generated, reboot your server. If the tomcat certificate for your server is on the list, click the certificate to select it. Note Ensure that the certificate you select includes the hostname for the server. | Note | Ensure that the certificate you select includes the hostname for the server. |
| Note | Ensure that the certificate you select includes the hostname for the server. |
| Step 5 | Click Download .PEM File and save the file to your desktop. |
| Step 6 | Copy the certificate to %CVP_HOME%\conf\security\ in OAMP Server. |
| Step 7 | Run the following command to import the certificate to the CVP Call Server keystore. %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                VVB_cert -file %CVP_HOME%\conf\security\<VVB certificate.pem> Log in to the Call Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
| Step 8 | Go to Services and restart Cisco CVP OPSConsoleServer . |

| Note | Ensure that the certificate you select includes the hostname for the server. |
|---|---|

| Step 1 | Log in to the OAMP Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
|---|---|
| Step 2 | Remove the existing certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -delete -alias oamp_certificate . |
| Step 3 | Generate a new key pair for the alias with selected key size by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias oamp_certificate
                                                -v -keysize 2048 -keyalg RSA . Enter keystore password: <enter the keystore password>
What is your first and last name?
 [Unknown]: <specify the CVP host name appended with "OAMP_Server"> E.g cisco-cvp-211_OAMP_Server
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
Specify ‘yes’ for the inputs. |
| Step 4 | Generate the CSR certificate for the alias by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\oampserver.csr and save it to a file (for example, oamp.csr ) . |
| Step 5 | Enter the keystore password when prompted. |
| Step 6 | Download oamp.csr from CVP %CVP_HOME%\conf\security\ and sign it from CA. |
| Step 7 | Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\ |
| Step 8 | Install the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                root -file %CVP_HOME%\conf\security\<filename_of_root_cert> . |
| Step 9 | Enter the keystore password when prompted. |
| Step 10 | Install the signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                oamp_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert> . |
| Step 11 | Enter the keystore password when prompted. |
| Step 12 | Restart the Cisco CVP OpsConsoleServer service. |

| Step 1 | To generate the CSR certificate on VVB, open the administration page. From the Navigation drop-down list, choose Cisco Unified OS Administration and click Go . |
|---|---|
| Step 2 | Go to Security > Certificate Management > Generate CSR Generate Certificate signing Request . Create the CSR against tomcat with the key-length as 2048. |
| Step 3 | To download the generated CSR, click Download CSR . After the Generate Certificate signing Request dialog opens, click Download CSR . |
| Step 4 | Open the certificate in Notepad, copy the contents and sign the certificate with CA. |
| Step 5 | Upload the root certificate generated from the CA into VVB against tomcat-trust: Go to Security > Certificate Management > Generate CSR > Upload certificate/certificate chain . Choose tomcat-trust from the drop-down list. Click Browse and select the certificate. Click Upload to upload the root certificate of the Certificate Authority. |
| Step 6 | Upload the signed certificate into VVB against tomcat. Go to Security > Certificate Management > Upload certificate/certificate chain . Choose tomcat from the drop-down list. Click Browse and select the certificate. Click Upload . After the certificate is uploaded successfully, VVB displays the certificate signed by <CA hostname>. |
| Step 7 | Restart the Tomcat service and the VVB engine. |

| Step 1 | Log in to VXML Server. |
|---|---|
| Step 2 | Run the regedit command. |
| Step 3 | Go to HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Apache Software Foundation\Procrun 2.0\VXMLServer\Parameters\Java\Options . |
| Step 4 | Append the following lines to the file: -Dhttps.proxyHost=<Your proxy IP/Host>
-Dhttps.proxyPort=80 Note If proxy requires credentials, add the following: -Dhttps.proxyUser=<username>
-Dhttps.proxyPassword=<password> | Note | If proxy requires credentials, add the following: -Dhttps.proxyUser=<username>
-Dhttps.proxyPassword=<password> |
| Note | If proxy requires credentials, add the following: -Dhttps.proxyUser=<username>
-Dhttps.proxyPassword=<password> |
| Step 5 | Restart service Cisco CVP VXMLServer . |

| Note | If proxy requires credentials, add the following: -Dhttps.proxyUser=<username>
-Dhttps.proxyPassword=<password> |
|---|---|

| Step 1 | Log in to the CVP Server . For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
|---|---|
| Step 2 | Run the following command to export the WSM certificate. %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias wsm_certificate
                                                -file %CVP_HOME%\conf\security\{CVPServerName}_wsm.cer> |
| Step 3 | Enter the keystore password when prompted. |
| Step 4 | Copy the certificate to %CVP_HOME%\conf\security\ in OAMP Server. |
| Step 5 | Log in to the OAMP Server . For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
| Step 6 | Run the following command to import the certificate to the OAMP Server: %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                {CVPServername}_wsm -file %CVP_HOME%\conf\security\{CVPServername}_wsm.cer> For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
| Step 7 | Enter the keystore password when prompted. |
| Step 8 | Repeat all the steps for all the Cisco Unified CVP Servers in the deployment. |
| Step 9 | Go to Services and restart Cisco CVP OPSConsoleServer and CVP WebServices on CVP OAMP Server . |
| Step 10 | Download the OAMP WSM certificate (OAMP_wsm) from https://<oampserverip>:8111 on the Cisco Unified CVP Server to %CVP_HOME%\conf\security\ |
| Step 11 | Run the following command to import the certificate to the Cisco Unified CVP Server: %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                                oamp_wsm -file %CVP_HOME%\conf\security\oamp_wsm.cer> |
| Step 12 | Enter the keystore password when prompted. |
| Step 13 | Repeat all the steps for all the Cisco Unified CVP Servers in the deployment. |
| Step 14 | Go to Services and restart Cisco Web Services , Cisco VXML Service , and Cisco Call Service on each Cisco Unified CVP Server. |

| Step 1 | Log in to the OAMP Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
|---|---|
| Step 2 | Remove the existing certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -delete -alias oamp_certificate . |
| Step 3 | Generate a new key pair for the alias with selected key size by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias oamp_certificate
                                                -v -keysize 2048 -keyalg RSA . Enter keystore password: <enter the keystore password>
What is your first and last name?
 [Unknown]: <specify the CVP host name appended with "OAMP_Server"> E.g cisco-cvp-211_OAMP_Server
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
Specify ‘yes’ for the inputs. |
| Step 4 | Generate the CSR certificate for the alias by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias oamp_certificate
                                                -file %CVP_HOME%\conf\security\oampserver.csr and save it to a file (for example, oamp.csr ) . |
| Step 5 | Enter the keystore password when prompted. |
| Step 6 | Download oamp.csr from CVP %CVP_HOME%\conf\security\ and sign it from CA. |
| Step 7 | Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\ |
| Step 8 | Install the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                root -file %CVP_HOME%\conf\security\<filename_of_root_cert> . |
| Step 9 | Enter the keystore password when prompted. |
| Step 10 | Install the signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -trustcacerts -alias
                                                oamp_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert> . |
| Step 11 | Enter the keystore password when prompted. |
| Step 12 | Restart the Cisco CVP OpsConsoleServer service. |

| Step 1 | Log in to the Call Server and retrieve the keystore password from the security.properties file. Note At the command prompt, enter the following command: more %CVP_HOME%\conf\security.properties . Security.keystorePW = <Returns the keystore password> Enter the keystore password when prompted. | Note | At the command prompt, enter the following command: more %CVP_HOME%\conf\security.properties . Security.keystorePW = <Returns the keystore password> Enter the keystore password when prompted. |
|---|---|---|---|
| Note | At the command prompt, enter the following command: more %CVP_HOME%\conf\security.properties . Security.keystorePW = <Returns the keystore password> Enter the keystore password when prompted. |
| Step 2 | Log in to the Call Server or Reporting Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
| Step 3 | Remove the existing WSM certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -delete -alias wsm_certificate . |
| Step 4 | Remove the existing Call Server certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security.keystore -delete -alias callserver_certificate . |
| Step 5 | Generate a new key pair for the alias with selected key size by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -genkeypair -alias wsm_certificate
                                                -v -validity <duration in days> -keysize 2048 -keyalg RSA . Enter keystore password: <enter the keystore password>
What is your first and last name?
 [Unknown]: <specify the CVP hostname or FQDN, appended with "wsm"> E.g cisco-cvp-211_wsm >
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
Specify ‘yes’ for the inputs. Note When a certificate is generated to be used in PCCE SPOG, provide the FQDN of the host without appending _wsm. The default duration for validity is 90 days. | Note | When a certificate is generated to be used in PCCE SPOG, provide the FQDN of the host without appending _wsm. The default duration for validity is 90 days. |
| Note | When a certificate is generated to be used in PCCE SPOG, provide the FQDN of the host without appending _wsm. The default duration for validity is 90 days. |
| Step 6 | Generate the CSR certificate for the alias by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -certreq -alias wsm_certificate
                                                -file %CVP_HOME%\conf\security\wsm.csr and save it to a file (for example, wsm.csr ) . |
| Step 7 | Enter the keystore password when prompted. |
| Step 8 | Download wsm.csr from CVP %CVP_HOME%\conf\security\ and sign it from CA. |
| Step 9 | Copy the root CA certificate and the CA-signed certificate to %CVP_HOME%\conf\security\ |
| Step 10 | Install the root CA certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -validity <duration
                                                in days> -trustcacerts -alias root -file %CVP_HOME%\conf\security\<filename_of_root_cert> . |
| Step 11 | Enter the keystore password when prompted. |
| Step 12 | Install the signed certificate by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -import -v -validity <duration
                                                   in days> -trustcacerts -alias wsm_certificate -file %CVP_HOME%\conf\security\<filename_of_CA_signed_cert> . |
| Step 13 | Enter the keystore password when prompted. |
| Step 14 | Restart the Cisco CVP WebServicesManager service. |

| Note | At the command prompt, enter the following command: more %CVP_HOME%\conf\security.properties . Security.keystorePW = <Returns the keystore password> Enter the keystore password when prompted. |
|---|---|

| Note | When a certificate is generated to be used in PCCE SPOG, provide the FQDN of the host without appending _wsm. The default duration for validity is 90 days. |
|---|---|

| Step 1 | To open the Operations Console, enter https://<FQDN>:9443/noamp in the web-browser, where FQDN is the fully qualified domain name of the machine on which Operations Console is installed. |
|---|---|
| Step 2 | Navigate to Integration > Cloud Connect . |
| Step 3 | From the Device drop-down list, select the CVP device. |
| Step 4 | In the Publisher IP Address / Hostname text box, enter the FQDN / IP address of the publisher. |
| Step 5 | In the Subscriber IP Address / Hostname text box, enter the FQDN / IP address of the subscriber. |
| Step 6 | In the User Name text box, enter the username. |
| Step 7 | In the Password text box, enter the password. |
| Step 8 | Click Save . |
| Step 9 | Restart the Cisco CVP Call Server. |

| Note | Ensure that you import both the Cloud Connect Publisher and Subscriber certificates to all the CVP call servers. |
|---|---|

| Step 1 | To export the Cloud Connect certificates: Enter the following URL to access the Cisco Unified Communications Operating System Administration page. https://<FQDN of CloudConnect:8443/cmplatform Navigate to Security > Certificate Management and find the Cloud Connect publisher and subscriber certificates in one of your tomcat-trust folders. Select the certificates and click Download .PEM File to save the certificates to a local folder. |
|---|---|
| Step 2 | Copy the Cloud Connect certificates into the call server folder at c:\cisco\cvp\conf\security . |
| Step 3 | Open the Command Prompt as an administrator. |
| Step 4 | Enter the following command in the keystore to import the Cloud Connect certificate to the call server. c:\Cisco\CVP\jre\bin\keytool.exe -import -keystore .keystore -storetype JCEKS -trustcacerts 
   -alias <cloud connect publisher or cloud connect subscriber> –file <filepath> |
| Step 5 | Enter the keystore password when prompted. To retrieve the keystore password, do the following: Go to %CVP_HOME%\bin . Generate the keystore password by running the DecryptKeystoreUtil.bat file. |
| Step 6 | Restart the CVP call server. |
| Step 7 | Repeat steps 1 through 6 for all the CVP call servers. For more details on how to obtain a third-party CA certificate for Cloud Connect, see the Obtain and Upload Third-party CA Certificate topic in the Cisco Unified Contact Center Enterprise Installation and Upgrade Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-installation-guides-list.html . |

| Step 1 | Log in to the CVP Call Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
|---|---|
| Step 2 | Copy the VRU PG certificate to the CVP call server folder at %CVP_HOME%\conf\security\ . |
| Step 3 | Open the Command Prompt as an administrator. |
| Step 4 | Enter the following command in the keystore to import the VRU PG certificate to the callserver keystore: %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetype JCEKS -alias
                                             <VRU_PG_Certificate> -file <filepath> |
| Step 5 | Enter the keystore password when prompted. |
| Step 6 | Restart the CVP call server. |

| Step 1 | Log in to the CUCM OS Administration page. |
|---|---|
| Step 2 | Go to Security > Certificate Management . |
| Step 3 | Click Generate Self-signed . |
| Step 4 | On the pop-up window, click Generate button. |
| Step 5 | Restart Tomcat from CUCM CLI by running utils service restart Cisco Tomcat . Note Tomcat will take a few minutes to stop and then start. If you access the CUCM UI during this time, you may receive a 404 error. | Note | Tomcat will take a few minutes to stop and then start. If you access the CUCM UI during this time, you may receive a 404 error. |
| Note | Tomcat will take a few minutes to stop and then start. If you access the CUCM UI during this time, you may receive a 404 error. |
| Step 6 | When the CUCM UI is available, open the CUCM OS Administration page. |
| Step 7 | Go to Security > Certificate Management . |
| Step 8 | Click Find and identify the Self-signed certificate generated by the system. |
| Step 9 | Click the CallManager Certificate name. |
| Step 10 | In the dialog box, click Download . |

| Note | Tomcat will take a few minutes to stop and then start. If you access the CUCM UI during this time, you may receive a 404 error. |
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
| Step 12 | Upload the root certificate generated from the CA to CUCM against CUCM-trust. |
| Step 13 | Click Upload
                                             				Certificate on CUCM by selecting the certificate name as CallManager . On successful
                                             				completion, CUCM displays the description as Certificate
                                                				  signed by <CA hostname> . |
| Step 14 | Restart TFTP
                                          			 and Cisco CallManager services on all the nodes in the cluster that run these
                                          			 services. |

| Step 1 | Open the certificate that was exported in Step 1 . |
|---|---|
| Step 2 | Click View Certificate . |
| Step 3 | Click the Details tab. |
| Step 4 | Click Copy to File . The Certificate ExportWizard window appears. |
| Step 5 | Click Base-64 encoded X.509 (.CER) , and then click Next . |
| Step 6 | Specify a file name in the File to the Export dialog box, and then click Next . |
| Step 7 | Click Finish . A message indicates that the export was successful. |
| Step 8 | Click OK and close the Security Alert dialog box. |
| Step 9 | Open the certificate in Notepad. |
| Step 10 | Access the IOS ingress GW in the privileged EXEC mode. |
| Step 11 | Access the global configuration mode by entering the configuration terminal. |
| Step 12 | Import the CVP CallServer Certificate to Cisco IOS Gateway by entering the following commands: crypto pki trustpoint <Call Server trust point name>
enrollment terminal

exit |
| Step 13 | Open the exported Call Server certificate in Notepad and copy the certificate information that appears between the -BEGIN
                                          CERTIFICATE and END CERTIFICATE tags to the IOS device. |
| Step 14 | Enter the following command: crypto pki auth <Call Server  trust point name> |
| Step 15 | Paste the certificate from Notepad and end with a blank line or the word quit on a line by itself. |
| Step 16 | To generate the self-signed certificate of the Gateway, first generate 2048-bit RSA keys: crypto key generatersageneral-keys Label <Your Ingress GW trustpointname> modulus 2048 |
| Step 17 | Configure a trustpoint: crypto pkitrustpoint<Your Ingress GW trustpointname>
enrollment selfsigned
fqdn none
subject-name CN=SIP-GW
rsakeypair <Your Ingress GW trustpoint name>

Router(config)# crypto pkienroll<Your Ingress GW trustpointname> % The fully-qualified domain name will not be included in the certificate
% Include the router serial number in the subject name? [yes/no]: no
% Include an IP address in the subject name? [no]: no
Generate Self Signed Router Certificate? [yes/no]: yes
Router Self Signed Certificate successfully created |
| Step 18 | View the certificate in PEM format, and copy the Self-signed CA certificate (output starting from “----BEGIN” to “CERTIFICATE----“)
                                          to a file named ingress_gw.pem . Router(config)# crypto pki export <Your Ingress GW trustpoint name> pem terminal % Self-signed CA certificate:
-----BEGIN CERTIFICATE-----
MIIB6zCCAVSgAwIBAgIBAjANBgkqhkiG9w0BAQUFADARMQ8wDQYDVQQDEwZTSVAt
R1cwHhcNMTcwOTI2MTQ1MTE2WhcNMjAwMTAxMDAwMDAwWjARMQ8wDQYDVQQDEwZT
SVAtR1cwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAKdSDxIj8T6UaYxgujMk
9B2d5dq3Ni8s1e4yfsSB1lbJ/AQk+aLDfE3/BeVkeXEjRCohhnZcEnMV4DdOPxj7
9MWzoJgxkMj7X3I6ijaL2Oll2iQuBcjiqYtAUPlxB3VTjqLMbxG30fb7xLCDTuo5
s07TLsE1AbxrbrH62Za/C0e5AgMBAAGjUzBRMA8GA1UdEwEB/wQFMAMBAf8wHwYD
VR0jBBgwFoAU+tJphvbvgc7yE6uqIh7VlgTrtPswHQYDVR0OBBYEFPrSaYb274HO
8hOrqiIe1ZYE67T7MA0GCSqGSIb3DQEBBQUAA4GBADRaW93OqErMEgRGWJJVLlbs
n8XnSbiw1k8KeY/AzgxBoBJtc0FKs4L0XUOEc6eHUKCHoks1FDV211MMlzPe7MAc
vDd7EV/abx2UdFSL9jjm/YzIleVUj8b0T3qNSfOqDtV5CyCjPichNa2eCR1bTmGx
o3HqLeEl/+66L/l74nlT
-----END CERTIFICATE-----

% General Purpose Certificate:
-----BEGIN CERTIFICATE-----
MIIB6zCCAVSgAwIBAgIBAjANBgkqhkiG9w0BAQUFADARMQ8wDQYDVQQDEwZTSVAt
R1cwHhcNMTcwOTI2MTQ1MTE2WhcNMjAwMTAxMDAwMDAwWjARMQ8wDQYDVQQDEwZT
SVAtR1cwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAKdSDxIj8T6UaYxgujMk
9B2d5dq3Ni8s1e4yfsSB1lbJ/AQk+aLDfE3/BeVkeXEjRCohhnZcEnMV4DdOPxj7
9MWzoJgxkMj7X3I6ijaL2Oll2iQuBcjiqYtAUPlxB3VTjqLMbxG30fb7xLCDTuo5
s07TLsE1AbxrbrH62Za/C0e5AgMBAAGjUzBRMA8GA1UdEwEB/wQFMAMBAf8wHwYD
VR0jBBgwFoAU+tJphvbvgc7yE6uqIh7VlgTrtPswHQYDVR0OBBYEFPrSaYb274HO
8hOrqiIe1ZYE67T7MA0GCSqGSIb3DQEBBQUAA4GBADRaW93OqErMEgRGWJJVLlbs
n8XnSbiw1k8KeY/AzgxBoBJtc0FKs4L0XUOEc6eHUKCHoks1FDV211MMlzPe7MAc
vDd7EV/abx2UdFSL9jjm/YzIleVUj8b0T3qNSfOqDtV5CyCjPichNa2eCR1bTmGx
o3HqLeEl/+66L/l74nlT
-----END CERTIFICATE----- |
| Step 19 | Test your certificate. show crypto pkicertificates |
| Step 20 | To configure TLS version on the Gateway: router# configure terminal router(config)# sip-ua router(config-sip-ua)# transport tcp tls <version> v1.2 Enable TLS Version 1.2

Note: SIP TLS version 1.2 is available in Cisco IOS Software Release 15.6(1)T and higher. |
| Step 21 | To check if the TLS version is negotiated: router# show sip-ua connections tcp tls detail |
| Step 22 | To enable SRTP on the incoming/outgoing dial-peer, specify SRTP: router# configure terminal router(config)# dial-peer voice 100 voip router(config-dial-peer)# srtp Note: This command is supported in Cisco IOS Software Release 15.6(1)T and higher. |
| Step 23 | Configure the SIP stack in Cisco IOS GW to use the self-signed certificate of the router to establish a SIP TLS connection
                                          from/to the CVP Call Server. router# configure terminal router(config)# sip-ua router(config-sip-ua)# crypto signaling remote-addr <peer IP address> <peer subnet mask> trustpoint <Your Ingress GW trustpoint name> strict-cipher Example: 
sip-ua 
 crypto signaling remote-addr 10.48.54.89 255.255.255.255 trustpoint VG-SIP-1 strict-cipher |
| Step 24 | Configure an outbound VoIP dial-peer to route calls to the CVP Call Server. session target ipv4:<Call Server IP address>:5061
 session transport tcp tls

Example:
dial-peer voice 3 voip
 destination-pattern 82...
 session protocol sipv2
 session target ipv4:10.48.54.89:5061
 session transport tcp tls
 dtmf-relay rtp-nte
 codec g711ulaw |
| Step 25 | To import GW or CUSP certificate into the CVP Call Server: Copy the Ingress GW/ CUSP self-signed certificate to %CVP_HOME%\conf\security\ and import the certificate to the callserverkeystore. %CVP_HOME%\jre\bin\keytool.exe -import -trustcacerts -keystore %CVP_HOME%\conf\security\.keystore -storetypeJCEKS -alias gw_cert
                                                   -file %CVP_HOME%\conf\security\<ingress GW\CUSP certificate name> Enter the keystore password when prompted. A message appears on the screen: Trust this certificate? [no]: Enter yes . Use the list flag to check your keystore entries by running %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.keystore -list |
| Step 26 | To change the supported TLS version from the OAMP UI, see Administration Guide for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html . |
| Step 27 | Restart the Call Server. |

| Step 1 | Create a 2048-bit RSA key. Router(config)# crypto key generate rsa general-keys Label <name of the key pair> modulus 2048 Generates 2048 bit RSA key pair. |
|---|---|
| Step 2 | Create a trustpoint. A trustpoint represents a trusted CA. Example: Router(config)# crypto pki trustpoint ms-ca-name Creates the trustpoint.

Router(config-pki-trustpoint)# enrollment terminal Specifies cut and paste enrollment with this trustpoint.

Router(config-pki-trustpoint)# subject-name CN=sslvpn.mydomain.com,OU=SSLVPN,O=My Company Name,C=US,ST=Florida Defines x.500 distinguished name.

Router(config-pki-trustpoint)# rsakeypair keypairname Specifies key pair generated previously

Router(config-pki-trustpoint)# fqdn sslvpn.mydomain.com Specifies subject alternative name (DNS:).

Router(config-pki-trustpoint)# exit |
| Step 3 | Create a CSR (Certificate Request) to give to the MS Certificate Server. Example: Router(config)# crypto pki enroll ms-ca-name % Start certificate enrollment ..
% The subject name in the certificate will include: CN=Webvpn.cisco.com % The subject name in the certificate will include: webvpn.cisco.com % Include the router serial number in the subject name? [yes/no]: no % Include an IP address in the subject name? [no]: no Display Certificate Request to terminal? [yes/no]: yes ! Displays the PKCS#10 enrollment request to the terminal.
! You will need to copy this from the terminal to a text
! file or web text field to submit to the 3rd party CA.

Certificate Request follows:
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Redisplay enrollment request? [yes/no]: no Router(config)# |
| Step 4 | Sign the CSR with the root CA. |
| Step 5 | Install the root certificate. Router(config)# crypto pki authenticate ms-ca-name Enter the base 64 encoded CA certificate.
End with a blank line or the word "quit" on a line by itself

-----BEGIN CERTIFICATE-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

-----END CERTIFICATE-----
quit

Certificate has the following attributes:
Fingerprint MD5: D5DF85B7 9A5287D1 8CD50F90 232DB534
Fingerprint SHA1: 7C4656C3 061F7F4C 0D67B319 A855F60E BC11FC44
% Do you accept this certificate? [yes/no]: y Trustpoint CA certificate accepted. |
| Step 6 | Install the signed certificate for the gateway: Router(config)# crypto pki import ms-ca-name certificate Enter the base 64 encoded certificate.
End with a blank line or the word "quit" on a line by itself

-----BEGIN CERTIFICATE-----
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

-----END CERTIFICATE-----
quit
% Router Certificate successfully imported |
| Step 7 | Test your certificate. show crypto pki certificates Note To configure TLS version on the gateway: router#
router# config terminal router(config)# sip-ua router(config-sip-ua)# transport tcp tls <version> v1.2  Enable TLS Version 1.2 To check if the TLS version is negotiated: router# show sip-ua connections tcp tls detail To enable SRTP on the incoming/outgoing dial-peer, specify srtp: router# configure terminal router(config)# dial-peer voice 100 voip router(config-dial-peer)# srtp | Note | To configure TLS version on the gateway: router#
router# config terminal router(config)# sip-ua router(config-sip-ua)# transport tcp tls <version> v1.2  Enable TLS Version 1.2 To check if the TLS version is negotiated: router# show sip-ua connections tcp tls detail To enable SRTP on the incoming/outgoing dial-peer, specify srtp: router# configure terminal router(config)# dial-peer voice 100 voip router(config-dial-peer)# srtp |
| Note | To configure TLS version on the gateway: router#
router# config terminal router(config)# sip-ua router(config-sip-ua)# transport tcp tls <version> v1.2  Enable TLS Version 1.2 To check if the TLS version is negotiated: router# show sip-ua connections tcp tls detail To enable SRTP on the incoming/outgoing dial-peer, specify srtp: router# configure terminal router(config)# dial-peer voice 100 voip router(config-dial-peer)# srtp |
| Step 8 | Associate the created trustpoint in Step 2 with sip-ua. router# configure terminal router(config)# sip-ua router(config-sip-ua)# crypto signaling remote-addr <peer IP address> 
<peer subnet mask> trustpoint <trust point name created in step2> Note Installing CVP Call/VXML Servers enables IIS (for media server functionality), which opens port 443 by default for TLS connections.
                                                         This port allows TLSv1.0 and TLSv1.1 connections. To close these connections, change the Enabled value to 0 by selecting the Decimal option in the following registry keys: TLSv1.0: HKEY-LOCAL-MACHINE \SYSTEM\CurrentControlSet\Control\SecurityProviders\ SCHANNEL\Protocols\TLS1.0\Server\Enabled TLSv1.1: HKEY-LOCAL-MACHINE\ SYSTEM\CurrentControlSet\Control\SecurityProviders\ SCHANNEL\Protocols\TLS1.1\Server\Enabled This disables ports 443 and 3389 for TLSv1.0 and TLSv1.1 server-side connections. While Windows 8 and Windows Server 2012
                                                         remote desktop clients work by default, Windows 7 and Windows Server 2008 remote desktop clients cannot connect to these servers
                                                         for the RDP port (3389). To re-enable this port, install the patch available at https://support.microsoft.com/en-us/help/3080079/update-to-add-rds- support-for-tls-1-1-and-tls-1-2-in-windows-7-or-wind . | Note | Installing CVP Call/VXML Servers enables IIS (for media server functionality), which opens port 443 by default for TLS connections.
                                                         This port allows TLSv1.0 and TLSv1.1 connections. To close these connections, change the Enabled value to 0 by selecting the Decimal option in the following registry keys: TLSv1.0: HKEY-LOCAL-MACHINE \SYSTEM\CurrentControlSet\Control\SecurityProviders\ SCHANNEL\Protocols\TLS1.0\Server\Enabled TLSv1.1: HKEY-LOCAL-MACHINE\ SYSTEM\CurrentControlSet\Control\SecurityProviders\ SCHANNEL\Protocols\TLS1.1\Server\Enabled This disables ports 443 and 3389 for TLSv1.0 and TLSv1.1 server-side connections. While Windows 8 and Windows Server 2012
                                                         remote desktop clients work by default, Windows 7 and Windows Server 2008 remote desktop clients cannot connect to these servers
                                                         for the RDP port (3389). To re-enable this port, install the patch available at https://support.microsoft.com/en-us/help/3080079/update-to-add-rds- support-for-tls-1-1-and-tls-1-2-in-windows-7-or-wind . |
| Note | Installing CVP Call/VXML Servers enables IIS (for media server functionality), which opens port 443 by default for TLS connections.
                                                         This port allows TLSv1.0 and TLSv1.1 connections. To close these connections, change the Enabled value to 0 by selecting the Decimal option in the following registry keys: TLSv1.0: HKEY-LOCAL-MACHINE \SYSTEM\CurrentControlSet\Control\SecurityProviders\ SCHANNEL\Protocols\TLS1.0\Server\Enabled TLSv1.1: HKEY-LOCAL-MACHINE\ SYSTEM\CurrentControlSet\Control\SecurityProviders\ SCHANNEL\Protocols\TLS1.1\Server\Enabled This disables ports 443 and 3389 for TLSv1.0 and TLSv1.1 server-side connections. While Windows 8 and Windows Server 2012
                                                         remote desktop clients work by default, Windows 7 and Windows Server 2008 remote desktop clients cannot connect to these servers
                                                         for the RDP port (3389). To re-enable this port, install the patch available at https://support.microsoft.com/en-us/help/3080079/update-to-add-rds- support-for-tls-1-1-and-tls-1-2-in-windows-7-or-wind . |

| Note | To configure TLS version on the gateway: router#
router# config terminal router(config)# sip-ua router(config-sip-ua)# transport tcp tls <version> v1.2  Enable TLS Version 1.2 To check if the TLS version is negotiated: router# show sip-ua connections tcp tls detail To enable SRTP on the incoming/outgoing dial-peer, specify srtp: router# configure terminal router(config)# dial-peer voice 100 voip router(config-dial-peer)# srtp |
|---|---|

| Note | Installing CVP Call/VXML Servers enables IIS (for media server functionality), which opens port 443 by default for TLS connections.
                                                         This port allows TLSv1.0 and TLSv1.1 connections. To close these connections, change the Enabled value to 0 by selecting the Decimal option in the following registry keys: TLSv1.0: HKEY-LOCAL-MACHINE \SYSTEM\CurrentControlSet\Control\SecurityProviders\ SCHANNEL\Protocols\TLS1.0\Server\Enabled TLSv1.1: HKEY-LOCAL-MACHINE\ SYSTEM\CurrentControlSet\Control\SecurityProviders\ SCHANNEL\Protocols\TLS1.1\Server\Enabled This disables ports 443 and 3389 for TLSv1.0 and TLSv1.1 server-side connections. While Windows 8 and Windows Server 2012
                                                         remote desktop clients work by default, Windows 7 and Windows Server 2008 remote desktop clients cannot connect to these servers
                                                         for the RDP port (3389). To re-enable this port, install the patch available at https://support.microsoft.com/en-us/help/3080079/update-to-add-rds- support-for-tls-1-1-and-tls-1-2-in-windows-7-or-wind . |
|---|---|

| Step 1 | Create an RSA keypair in CUSP . From the CUSP foundation, enter the config mode and create the keypair: democusp48(config)# crypto key generate rsa label <key-label> modulus 1024 default Example democusp48# conf terminal democusp48(config)# crypto key generate rsa label cusp48-ca modulus 1024 default Key generation in progress. Please wait...
The label name for the key is cusp48-ca |
|---|---|
| Step 2 | Generate CSR signed by CA by running democusp48(config)# crypto key certreq label <key-label> url ftp: An FTP or HTTP server is required to export the CSR. Make sure the label in the command matches the label used to create the
                                             rsa private key. Example democusp48(config)# crypto key certreq label cusp48-ca url ftp: Address or name of remote host? 10.64.82.176
Username (ENTER if none)? test 
Password (not shown)?  
Destination path? /cusp48-ca.csr Uploading CSR file succeed 
democusp48(config)# |
| Step 3 | Import the CA server root certificate into CUSP by running: crypto key import trustcacert label <rootCA-label> terminal . Example democusp48(config)# crypto key import trustcacert label rootCA terminal Enter certificate...
End with a blank line or "quit" on a line by itself
-----BEGIN CERTIFICATE----- MIIEdTCCA12gAwIBAgIQaO1+pgDsy5lNqtF3E
epB4TANBgkqhkiG9w0BAQUFADBC MRMwEQYKCZImiZPyLGQBGRYDY29tMRcwFQYK
CZImiZPyLGQBGRYHQVJUR1NPTDES MBAGA1UEAxMJU0lQUEhPTklYMB4XDTA3MDc
xMzExNTAyMVoXDTEyMDcxMzExNTgz MVowQjETMBEGCgmSJomT8ixkARkWA2NvbT
EXMBUGCgmSJomT8ixkARkWB0FSVEdT T0wxEjAQBgNVBAMTCVNJUFBIT05JWDCCA
SIwDQYJKoZIhvcNAQEBBQADggEPADCC AQoCggEBAKbepxqDVZ5uWUVMWx8VaHVG
geg4CgDbzCz8Na0XqI/0aR9lImgx1Jnf ZD0nP1QvgUFSZ2m6Ee/pr2SkJ5kJSZo
zSmz2Ge4sKjZZbgQHmljWv1DswVDw0nyV F71ULTaNpsh81JVF5t2lqm75UnkW4x
P5qQn/rgfXv/Xse9964kiZhZYjtt2Ixt2V3imhh1i228YTihnTY5c3L0vD30v8dH
newsaCKd/XU+czw8feWguXXCTovvXHIbFeHvLCk9FLDoV8n9PAIHWZRPnt+HQjsD
s+jaB3F9MPVYXYElpmWrpEPHUPNZG4LsFi 6tQtiRP2UANUkXZ9fvGZMXHCZOZJi
FUCAwEAAaOCAWUwggFhMAsGA1UdDwQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA
1UdDgQWBBR39nCk+FjRuAbWEof5na/+Sf58STCCAQ4GA1UdHwSCAQUwggEBMIH+o
IH7oIH4hoG4bGRhcDovLy9DTj1TSVBQSE9O SVgsQ049U0lQUEhPTklYLUlORElB
LENOPUNEUCxDTj1QdWJsaWMlMjBLZXklMjBT ZXJ2aWNlcyxDTj1TZXJ2aWNlcyx
DTj1Db25maWd1cmF0aW9uLERDPUFSVEdTT0ws REM9Y29tP2NlcnRpZmljYXRlUm
V2b2NhdGlvbkxpc3Q/YmFzZT9vYmplY3RDbGFz cz1jUkxEaXN0cmlidXRpb25Qb
2ludIY7aHR0cDovL3NpcHBob25peC1pbmRpYS5h cnRnc29sLmNvbS9DZXJ0RW5y
b2xsL1NJUFBIT05JWC5jcmwwEAYJKwYBBAGCNxUB BAMCAQAwDQYJKoZIhvcNAQE
FBQADggEBAHua4/pwvSZ48MNnZKdsW9hvuTV4jwtGErgc16bOR0Z1urRFIFr2NCP
yzZboTb+ZllkQPDMRPBoBwOVr7BciVyoTo7AKFheqYm9asXL18A6XpK/WqLjlCcX
rdzF8ot0o+dK05sd9ZG7hRckRhFPwwj5Z7z0Vsd/jcO51QjpS4rzMZZXK2FnRvng
d5xmp4U+yJtPyr8g4DyAP2/UeSKe0SEYoTV5x5FpdyF4veZneB7+ZfFntWFf4xwi
obf+UvW47W6pCj5nGLMBzOiaxeQ8pre+yjipL2ucWK4ynOfKzz4XlkfktITDSogQ
A1AS1quQVbKTKk+qLGD6Ml2P0LrcKQkk= 
-----END CERTIFICATE----- 
Certificate info
*******************************************
Owner: CN=cvpvb-GDESINGHROOTCA-CA, DC=cvpvb, DC=cisco, DC=com
Issuer: CN=cvpvb-GDESINGHROOTCA-CA, DC=cvpvb, DC=cisco, DC=com
Certificate fingerprint (MD5): 41:A2:31:9D:97:AF:A8:CA:60:FC:46:95:82:DE:78:03
Do you want to continue to import this certificate, additional validation will be perfom? [y/n]: y 
democusp48(config)# |
| Step 4 | Import the signed certificate into CUSP by running crypto key import cer label <key-label> url terminal . Example democusp48(config)# crypto key import cer label cusp48-ca terminal Enter certificate...
End with a blank line or "quit" on a line by itself
-----BEGIN CERTIFICATE----- MIIFITCCBAmgAwIBAgIKGI1fqgAAAAAAEDAN
BgkqhkiG9w0BAQUFADBCMRMwEQYK CZImiZPyLGQBGRYDY29tMRcwFQYKCZImiZ
PyLGQBGRYHQVJUR1NPTDESMBAGA1UE AxMJU0lQUEhPTklYMB4XDTA4MTIwOTA5M
DExOVoXDTA5MTIwOTA5MTExOVowYTEL MAkGA1UEBhMCJycxCzAJBgNVBAgTAicn
MQswCQYDVQQHEwInJzELMAkGA1UEChMC JycxCzAJBgNVBAsTAicnMR4wHAYDVQQ
DExVTT0xURVNUQ0MuYXJ0Z3NvbC5jb20w gZ8wDQYJKoZIhvcNAQEBBQADgY0AMI
GJAoGBAOZz88nK51bJYjWgvuv4Wx1CGxTN YWGyNg+vDyQgKBXlL7b1CqBx1Yjl4
eetO4LiKkW/y4jSv3nCxCAdOrMvVF5lxFmY baMlR1R/qMCLzAMvmsWlH6VY4rcf
FGkjed3zCcI6BJ6fG9H9dt1J+47iM7SdZYz/ NrEqDnrpoHaUxdzlAgMBAAGjggJ
8MIICeDAdBgNVHQ4EFgQUYXLxMfiZJP29UZ3w Mpj0e79sk4EwHwYDVR0jBBgwFo
AUd/ZwpPhY0bgG1hKH+Z2v/kn+fEkwggEOBgNV HR8EggEFMIIBATCB/qCB+6CB+
IaBuGxkYXA6Ly8vQ049U0lQUEhPTklYLENOPVNJ UFBIT05JWC1JTkRJQSxDTj1D
RFAsQ049UHVibGljJTIwS2V5JTIwU2VydmljZXMs Q049U2VydmljZXMsQ049Q29
uZmlndXJhdGlvbixEQz1BUlRHU09MLERDPWNvbT9j ZXJ0aWZpY2F0ZVJldm9jYX
Rpb25MaXN0P2Jhc2U/b2JqZWN0Q2xhc3M9Y1JMRGlz dHJpYnV0aW9uUG9pbnSGO
2h0dHA6Ly9zaXBwaG9uaXgtaW5kaWEuYXJ0Z3NvbC5j b20vQ2VydEVucm9sbC9T
SVBQSE9OSVguY3JsMIIBIgYIKwYBBQUHAQEEggEUMIIB EDCBqAYIKwYBBQUHMAK
GgZtsZGFwOi8vL0NOPVNJUFBIT05JWCxDTj1BSUEsQ049 UHVibGljJTIwS2V5JT
IwU2VydmljZXMsQ049U2VydmljZXMsQ049Q29uZmlndXJh dGlvbixEQz1BUlRHU
09MLERDPWNvbT9jQUNlcnRpZmljYXRlP2Jhc2U/b2JqZWN0 Q2xhc3M9Y2VydGlm
aWNhdGlvbkF1dGhvcml0eTBjBggrBgEFBQcwAoZXaHR0cDov L3NpcHBob25peC1
pbmRpYS5hcnRnc29sLmNvbS9DZXJ0RW5yb2xsL1NJUFBIT05J WC1JTkRJQS5BUl
RHU09MLmNvbV9TSVBQSE9OSVguY3J0MA0GCSqGSIb3DQEBBQUA A4IBAQAXm0MPu
eXcMYxQhVlPR/Yaxw0n2epeNRwsPP31Pr9Ak3SYSzhoMRVadJ3z K2gt4qiVV8wL
tzTO2o70JXKx+0keZdOX/DQQndxBkiBKqdJ2Qvipv8Z8k3pza3lN jANnYw6FL3/
Yvh+vWCLygEHfrUfKj/7H8GaXQVapj2mDs79/zgoSyIlo+STmwFWT GQy6iFO+pv
vMcyfjjv2dsuwt1Ml0nlict0LtkIKnRGLqnkA6sJo1P6kE+WK7n3P2 yho/Lg98q
vWl+1FRC18DrkUhpNiKXsP1ld9TcJGrdJP9zG7lI5Mf3Q/2NIAx2JZd ZVAsXZMN
smOsOrgXzkcU/xU3BXkX -----END CERTIFICATE-----  Import succeeded 
democusp48(config)#exit 
democusp48# |
| Step 5 | You can list the certificates by running show crypto key all . Example democusp48# sh crypto key all
Label name: rootca
Entry type: Trusted Certificate Entry
Creation date: Sat Jul 01 14:13:14 GMT+05:30 2017
Owner: CN=cvpvb-GDESINGHROOTCA-CA, DC=cvpvb, DC=cisco, DC=com
Issuer: CN=cvpvb-GDESINGHROOTCA-CA, DC=cvpvb, DC=cisco, DC=com
Valid from: Wed Mar 22 14:23:10 GMT+05:30 2017 until: Tue Mar 22 14:33:09 GMT+0
5:30 2022
Certificate fingerprint (MD5): 41:A2:31:9D:97:AF:A8:CA:60:FC:46:95:82:DE:78:03

Label name: cusp48-ca
Entry type: Key Entry
Creation date: Tue Jul 04 10:47:40 GMT+05:30 2017
Owner: CN=democusp48.cvpvb.cisco.com, OU='', O='', L='', ST='', C=''
Issuer: CN=cvpvb-GDESINGHROOTCA-CA, DC=cvpvb, DC=cisco, DC=com
SubjectAltName: DNS:democusp48.cvpvb.cisco.com
Valid from: Tue Jul 04 10:41:56 GMT+05:30 2017 until: Thu Jul 04 10:41:56 GMT+0
5:30 2019
Certificate fingerprint (MD5): 91:ED:83:CA:3B:37:16:E8:AB:07:EA:85:04:1A:D1:05 Note Add the Domain Name System (DNS) of the component with which the secure communication is established under SIP Stack > TLS Trusted Peers in CCCSP. | Note | Add the Domain Name System (DNS) of the component with which the secure communication is established under SIP Stack > TLS Trusted Peers in CCCSP. |
| Note | Add the Domain Name System (DNS) of the component with which the secure communication is established under SIP Stack > TLS Trusted Peers in CCCSP. |

| Note | Add the Domain Name System (DNS) of the component with which the secure communication is established under SIP Stack > TLS Trusted Peers in CCCSP. |
|---|---|

| Note | By default, HSTS is disabled in the VXML Server Tomcat instance because using HTTPS impacts the performance. You can enable
                                          it by uncommenting the documented section of the Tomcat instance’s web.xml. |
|---|---|

| Note | This configuration can be done at the container level (recommended) or application level, as per your preference. For application
                                                   level, add it to the web.xml file in the WEB-INF folder of the web application. For example: C:\Cisco\CVP\OPSConsoleServer\Tomcat\webapps\oamp\WEB-INF\web.xml |
|---|---|

| Note | The above configuration declares that the entire web application is for HTTPS only, and the container intercepts HTTP requests
                                                   and redirect them to the equivalent https:// URL. |
|---|---|

| Step 1 | Go to C:\Cisco\CVP\OPSConsoleServer\Tomcat\conf\server.xml . |
|---|---|
| Step 2 | Update the following line as highlighted and save the file: Connector enableLookups="false" port="9009" protocol="AJP/1.3" redirectPort="9443" address="127.0.0.1" |
| Step 3 | Go to C:\Cisco\CVP\wsm\Server\Tomcat\conf\server.xml . |
| Step 4 | Update the following line as highlighted and save the file: Connector port="8101" protocol="AJP/1.3" redirectPort="8443" address="127.0.0.1" |
| Step 5 | Restart the Web Services Manager and Operations Console services. |

| Step 1 | Go to C:\Cisco\CVP\VXMLServer\Tomcat\conf\server.xml . |
|---|---|
| Step 2 | Update the following line as highlighted and save the file: Connector enableLookups="false" port="7009" protocol="AJP/1.3" redirectPort="7443" address="127.0.0.1" |
| Step 3 | Go to C:\Cisco\CVP\wsm\Server\Tomcat\conf\server.xml . |
| Step 4 | Update the following line as highlighted and save the file: Connector port="8101" protocol="AJP/1.3" redirectPort="8443" address="127.0.0.1" |
| Step 5 | Restart the Web Services Manager and VXML services. |

| Note | Use the CVP keystore password when prompted for Export Password , Destination Keystore Password or Source Keystore Password . |
|---|---|

| Step 1 | Install the latest ES patch from https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/ES_MR/ES/ccvp_b_ccvp-eng-es-spl.html . |
|---|---|
| Step 2 | Update OpenJDK to the the latest version (17.0.1 or higher) . For detailed steps, see Java Runtime Environment Minor Update . |
| Step 3 | Go to C:\Cisco\CVP\conf\security and take a backup of the existing .keystore file. |
| Step 4 | For enabling ECDSA, add the ciphers through OAMP. Go to OAMP > Device Management > Unified CVP Call Server . Select the Call Server. Go to SIP > Advanced Configurations > Security Proprieties . Add the following ciphers here: TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 |
| Step 5 | Add the above ciphers in the sip.properties file in the C:/cisco/CVP/conf folder of OAMP server and Reporting server. Example #Secure ciphers colon(;) seperated e.g TLS_RSA_WITH_AES_128_CBC_SHA SIP.Secure.Ciphers=TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384;TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 |

| Step 1 | Log into the Call Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
|---|---|
| Step 2 | Download OpenSSL (64 bit) and install on your CVP machine. |
| Step 3 | Add OpenSSL bin path to the Windows environment path variable. Example: path=C:\Program Files\OpenSSL-Win64\bin |
| Step 4 | Go to C:\Cisco\CVP\conf\security . |
| Step 5 | From the command prompt, run the following commands to generate the private keys for Call server, VXML server, and WSM server
                                             respectively: Call server: openssl ecparam -name prime256v1 -genkey -noout -out callserver-private-key.pem VXML server: openssl ecparam -name prime256v1 -genkey -noout -out vxml-private-key.pem WSM server: openssl ecparam -name prime256v1 -genkey -noout -out wsm-private-key.pem |
| Step 6 | Run the following commands to generate the self-signed certificates for Call server, VXML server, and WSM server: Call server: openssl req -new -key callserver-private-key.pem  -x509 -nodes -days 365
 -out callserver-cert.pem VXML server: openssl req -new -key vxml-private-key.pem  -x509 -nodes -days 365
 -out vxml-cert.pem WSM server: openssl req -new -key wsm-private-key.pem  -x509 -nodes -days 365
 -out wsm-cert.pem |
| Step 7 | Enter the values for the following fields when prompted: Country Name (2 letter code) []:<>
State or Province Name (full name) []:<>
Locality Name (eg, city) []:<>
Organization Name (eg, company) []:<>
Organizational Unit Name (eg, section) []:<>
Common Name (eg, server FQDN or your name) []:.
Email Address []:.
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:. Some fields ( Common Name , Email Address , A challenge password , and An optional company name ) can be left blank by entering a period (.). The certificate is generated after all the details are entered. |
| Step 8 | Run the following commands to append the keys and certificates in one file: cat callserver-private-key.pem callserver-cert.pem > callserver-certificate-private.pem
cat vxml-private-key.pem vxml-cert.pem > vxml-certificate-private.pem
cat wsm-private-key.pem wsm-cert.pem > wsm-certificate-private.pem |
| Step 9 | Run the following commands to export the certificates to the Call server: openssl pkcs12 -export -inkey callserver-private-key.pem -in callserver-certificate-private.pem -out cert_callserver.p12 -name callserver_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> openssl pkcs12 -export -inkey vxml-private-key.pem -in vxml-certificate-private.pem -out cert_vxml.p12 -name vxml_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> openssl pkcs12 -export -inkey wsm-private-key.pem -in wsm-certificate-private.pem -out cert_wsm.p12 -name wsm_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> |
| Step 10 | Go to c:\cisco\cvp\conf\security and run the following commands to delete the existing RSA certificates for Call server, VXML server, and WSM servers: c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias callserver-certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias vxml_certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias wsm_certificate -storepass <CVP keystore password> |
| Step 11 | Run the following commands to import the ECDSA certificates to the keystore: c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_callserver.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias callserver_certificate
Importing keystore cert_callserver.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_vxml.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias vxml_certificate
Importing keystore cert_vxml.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_wsm.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias wsm_certificate
Importing keystore cert_wsm.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore] |
| Step 12 | Restart the Call server, VXML server, and WSM services from Windows services. |
| Step 13 | In new browser tabs, type the following and check the certificates: https://<callserver ip>:8443
https://<vxmlserver ip>:7443
https://<wsm ip>:8111 |

| Step 1 | Log into the OAMP Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
|---|---|
| Step 2 | Install OpenSSL (64 bit) on your machine. |
| Step 3 | Add OpenSSL bin path to the Windows environment path variable. Example: path=C:\Program Files\OpenSSL-Win64\bin |
| Step 4 | Go to C:\Cisco\CVP\conf\security . |
| Step 5 | From the command prompt, run the following commands to generate the private keys for the OAMP server and WSM server respectively: OAMP server: openssl ecparam -name prime256v1 -genkey -noout -out oamp-private-key.pem WSM server: openssl ecparam -name prime256v1 -genkey -noout -out wsm-private-key.pem |
| Step 6 | Run the following commands to generate the self-signed certificates for OAMP server and WSM server: OAMP server: openssl req -new -key oamp-private-key.pem  -x509 -nodes -days 365 -out oamp-cert.pem WSM server: openssl req -new -key wsm-private-key.pem  -x509 -nodes -days 365 -out wsm-cert.pem |
| Step 7 | Enter the values for the following fields when prompted: Country Name (2 letter code) []:<>
State or Province Name (full name) []:<>
Locality Name (eg, city) []:<>
Organization Name (eg, company) []:<>
Organizational Unit Name (eg, section) []:<>
Common Name (eg, server FQDN or your name) []:.
Email Address []:.
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:. Some fields ( Common Name , Email Address , A challenge password , and An optional company name ) can be left blank by entering a period (.). The certificate is generated after all the details are entered. |
| Step 8 | Run the following commands to append the keys and certificates in one file: cat oamp-private-key.pem oamp-cert.pem > oamp-certificate-private.pem
cat wsm-private-key.pem wsm-cert.pem > wsm-certificate-private.pem |
| Step 9 | Run the following commands to export the certificates to the OAMP server: openssl pkcs12 -export -inkey oamp-private-key.pem -in oamp-certificate-private.pem -out cert_oamp.p12 -name oamp_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> openssl pkcs12 -export -inkey wsm-private-key.pem -in wsm-certificate-private.pem -out cert_wsm.p12 -name wsm_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> |
| Step 10 | Go to c:\cisco\cvp\conf\security and run the following commands to delete the existing RSA certificates for OAMP server and WSM server: c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias oamp_certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias wsm_certificate -storepass <CVP keystore password> |
| Step 11 | Run the following commands to import the ECDSA certificates to the keystore: c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_oamp.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias oamp_certificate
Importing keystore cert_oamp.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_wsm.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias wsm_certificate
Importing keystore cert_wsm.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore] |
| Step 12 | Restart the OAMP and WSM servers from Windows services. |
| Step 13 | In new browser tabs, type the following and check the certificates: https://<wsm ip>:8111
https://<oamp ip>:9443 |

| Step 1 | Log into the Reporting Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
|---|---|
| Step 2 | Install OpenSSL (64 bit) on your machine. |
| Step 3 | Add OpenSSL bin path to the Windows environment path variable. Example: path=C:\Program Files\OpenSSL-Win64\bin |
| Step 4 | Go to C:\Cisco\CVP\conf\security . |
| Step 5 | From the command prompt, run the following commands to generate the private keys for the Call server and WSM server: Call server: openssl ecparam -name prime256v1 -genkey -noout -out callserver-private-key.pem WSM server: openssl ecparam -name prime256v1 -genkey -noout -out wsm-private-key.pem |
| Step 6 | Run the following commands to generate the self-signed certificates for Call server and WSM server: Call server: openssl req -new -key callserver-private-key.pem  -x509 -nodes -days 365 -out callserver-cert.pem WSM server: openssl req -new -key wsm-private-key.pem  -x509 -nodes -days 365 -out wsm-cert.pem |
| Step 7 | Enter the values for the following fields when prompted: Country Name (2 letter code) []:<>
State or Province Name (full name) []:<>
Locality Name (eg, city) []:<>
Organization Name (eg, company) []:<>
Organizational Unit Name (eg, section) []:<>
Common Name (eg, server FQDN or your name) []:.
Email Address []:.
Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:. Some fields ( Common Name , Email Address , A challenge password , and An optional company name ) can be left blank by entering a period (.). The certificate is generated after all the details are entered. |
| Step 8 | Run the following commands to append the keys and certificates in one file: cat callserver-private-key.pem callserver-cert.pem > callserver-certificate-private.pem
cat wsm-private-key.pem wsm-cert.pem > wsm-certificate-private.pem |
| Step 9 | Run the following commands to export the certificates to the Reporting server: openssl pkcs12 -export -inkey callserver-private-key.pem -in callserver-certificate-private.pem -out callserver-cert.p12 -name callserver_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> openssl pkcs12 -export -inkey wsm-private-key.pem -in wsm-certificate-private.pem -out cert_wsm.p12 -name wsm_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> |
| Step 10 | Go to c:\cisco\cvp\conf\security and run the following commands to delete the existing RSA certificates for the Call server and WSM server: c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias callserver-certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias wsm_certificate -storepass <CVP keystore password> |
| Step 11 | Run the following commands to import the ECDSA certificates to the keystore: c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore callserver-cert.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias callserver_certificate
Importing keystore callserver-cert.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_wsm.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias wsm_certificate
Importing keystore cert_wsm.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore] |
| Step 12 | Restart the Call server and WSM server from Windows services. |
| Step 13 | In new browser tabs, type the following and check the certificates: https://<callserver ip>:8443
https://<wsm ip>:8111 |

| Step 1 | Log into the Call Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
|---|---|
| Step 2 | Download OpenSSL (64 bit) and install on your CVP machine. |
| Step 3 | Add OpenSSL bin path to the Windows environment path variable. Example: path=C:\Program Files\OpenSSL-Win64\bin |
| Step 4 | Go to C:\Cisco\CVP\conf\security . |
| Step 5 | From the command prompt, run the following commands to generate the private keys and the CSRs (for Call server, VXML server,
                                             and WSM server) respectively: Call server: openssl ecparam -name prime256v1 -genkey -noout -out callserver-private-key.pem
openssl req -new -key callserver-private-key.pem -out callserver-cert.csr -days 360 VXML server: openssl ecparam -name prime256v1 -genkey -noout -out vxml-private-key.pem
openssl req -new -key vxml-private-key.pem -out vxml-cert.csr -days 360 WSM server: openssl ecparam -name prime256v1 -genkey -noout -out wsm-private-key.pem
openssl req -new -key wsm-private-key.pem -out wsm-cert.csr -days 360 |
| Step 6 | Enter the values for the following fields when prompted: Country Name (2 letter code) []:<>
State or Province Name (full name) []:<>
Locality Name (eg, city) []:<>
Organization Name (eg, company) []:<>
Organizational Unit Name (eg, section) []:<>
Common Name (eg, server FQDN or your name) []:.
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:. This information is incorporated in your certificate request. Some fields ( Common Name , Email Address , A challenge password , and An optional company name ) can be left blank by entering a period (.). The certificate is generated after all the details are entered. |
| Step 7 | Run the following commands to see the certificate requests: openssl cat callserver-cert.csr
openssl cat vxml-cert.csr
openssl cat wsm-cert.csr The encoded certificate request details are displayed. -----BEGIN CERTIFICATE REQUEST-----
MIIBCjCBsQIBADBPMQswCQYDVQQGEwJJTjESMBAGA1UECAwJS0FSTkFUQUtBMQ0w
CwYDVQQHDARCR0xSMQ4wDAYDVQQKDAVDaXNjbzENMAsGA1UECwwEQ0NCVTBZMBMG
ByqGSM49AgEGCCqGSM49AwEHA0IABP3MPDdzf56f+9uuv6e0f7mqVuVOeM4JVaq0
B0Fx6PtKPiby3K85A36F16Ueh81Br5DUueMfnexlwl4RdIbiMn+gADAKBggqhkjO
PQQDAgNIADBFAiEA/z4mjLovTAWUzIHKm3yO5N//At9SBNoJnB8Uz5loRVUCIArL
FjU79myKyC90iJqWyL7b8xPqGrhk4pdNdGaOP/0j
-----END CERTIFICATE REQUEST----- |
| Step 8 | Request for the CA-signed certificates: Submit the callserver-cert.csr , vxml-cert.csr , and wsm-cert.csr to your CA (who can provide signed ECDSA certificates). Note Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity. CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format. Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client. Wait for the CA's reply. Rename the certificate files received from the CA to callserver-cert.pem , vxml-cert.pem , and wsm-cert.pem respectively. | Note | Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity. CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format. Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client. |
| Note | Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity. CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format. Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client. |
| Step 9 | From the command prompt, run the following commands to append the keys and certificates in one file: cat callserver-private-key.pem callserver-cert.pem > callserver-certificate-private.pem
cat vxml-private-key.pem vxml-cert.pem > vxml-certificate-private.pem
cat wsm-private-key.pem wsm-cert.pem > wsm-certificate-private.pem |
| Step 10 | Run the following commands to export the certificates to the Call server: openssl pkcs12 -export -inkey callserver-private-key.pem -in callserver-certificate-private.pem -out cert_callserver.p12 -name callserver_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> openssl pkcs12 -export -inkey vxml-private-key.pem -in vxml-certificate-private.pem -out cert_vxml.p12 -name vxml_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> openssl pkcs12 -export -inkey wsm-private-key.pem -in wsm-certificate-private.pem -out cert_wsm.p12 -name wsm_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> |
| Step 11 | Go to c:\cisco\cvp\conf\security and run the following commands to delete the existing RSA certificates for Call server, VXML server, and WSM servers: c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias callserver-certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias vxml_certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias wsm_certificate -storepass <CVP keystore password> |
| Step 12 | Go to c:\cisco\cvp\conf\security and import the root certificate to the keystore: c:\cisco\CVP\jre\bin\keytool.exe -keystore .keystore -storetype JCEKS -import -alias root -trustcacerts -file <filename_of_root_cert> Note Also, import the intermediate certificates shared by the CA to the keystore. | Note | Also, import the intermediate certificates shared by the CA to the keystore. |
| Note | Also, import the intermediate certificates shared by the CA to the keystore. |
| Step 13 | Run the following commands to import the ECDSA certificates to the keystore: c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_callserver.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias callserver_certificate
Importing keystore cert_callserver.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_vxml.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias vxml_certificate
Importing keystore cert_vxml.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_wsm.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias wsm_certificate
Importing keystore cert_wsm.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore] |
| Step 14 | Restart the Call server, VXML server, and WSM services from Windows services. |
| Step 15 | In new browser tabs, type the following and check the certificates: https://<callserver ip>:8443
https://<vxmlserver ip>:7443
https://<wsm ip>:8111 |

| Note | Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity. CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format. Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client. |
|---|---|

| Note | Also, import the intermediate certificates shared by the CA to the keystore. |
|---|---|

| Step 1 | Log into the OAMP Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
|---|---|
| Step 2 | Download OpenSSL (64 bit) and install on your machine. |
| Step 3 | Add OpenSSL bin path to the Windows environment path variable. Example: path=C:\Program Files\OpenSSL-Win64\bin |
| Step 4 | Go to C:\Cisco\CVP\conf\security . |
| Step 5 | From the command prompt, run the following commands to generate the private keys and the CSRs (for the OAMP server and WSM
                                             server) respectively: OAMP server: openssl ecparam -name prime256v1 -genkey -noout -out oamp-private-key.pem
openssl req -new -key oamp-private-key.pem -out oamp-cert.csr -days 360 WSM server: openssl ecparam -name prime256v1 -genkey -noout -out wsm-private-key.pem
openssl req -new -key wsm-private-key.pem -out wsm-cert.csr -days 360 |
| Step 6 | Enter the values for the following fields when prompted: Country Name (2 letter code) []:<>
State or Province Name (full name) []:<>
Locality Name (eg, city) []:<>
Organization Name (eg, company) []:<>
Organizational Unit Name (eg, section) []:<>
Common Name (eg, server FQDN or your name) []:.
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:. This information is incorporated in your certificate request. Some fields ( Common Name , Email Address , A challenge password , and An optional company name ) can be left blank by entering a period (.). The certificate is generated after all the details are entered. |
| Step 7 | Run the following commands to see the certificate requests: openssl cat oamp-cert.csr
openssl cat wsm-cert.csr The encoded certificate request details are displayed. |
| Step 8 | Request for the CA-signed certificates: Submit the oamp-cert.csr and wsm-cert.csr files to your CA (who can provide signed ECDSA certificates). Note Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity. CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format. Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client. Wait for the CA's reply. Rename the certificate files received from the CA to oamp-cert.pem and wsm-cert.pem respectively. | Note | Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity. CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format. Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client. |
| Note | Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity. CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format. Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client. |
| Step 9 | From the command prompt, run the following commands to append the keys and certificates in one file: cat oamp-private-key.pem oamp-cert.pem > oamp-certificate-private.pem
cat wsm-private-key.pem wsm-cert.pem > wsm-certificate-private.pem |
| Step 10 | Run the following commands to export the certificates to the OAMP server: openssl pkcs12 -export -inkey oamp-private-key.pem -in oamp-certificate-private.pem -out cert_oamp.p12 -name oamp_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> openssl pkcs12 -export -inkey wsm-private-key.pem -in wsm-certificate-private.pem -out cert_wsm.p12 -name wsm_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> |
| Step 11 | Go to c:\cisco\cvp\conf\security and run the following commands to delete the existing RSA certificates for OAMP server and WSM server: c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias oamp_certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias wsm_certificate -storepass <CVP keystore password> |
| Step 12 | Go to c:\cisco\cvp\conf\security and import the root certificate to the keystore: c:\cisco\CVP\jre\bin\keytool.exe -keystore .keystore -storetype JCEKS -import -alias root -trustcacerts -file <filename_of_root_cert> Note Also, import the intermediate certificates shared by the CA to the keystore. | Note | Also, import the intermediate certificates shared by the CA to the keystore. |
| Note | Also, import the intermediate certificates shared by the CA to the keystore. |
| Step 13 | Run the following commands to import the ECDSA certificates to the keystore: c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_oamp.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias oamp_certificate
Importing keystore cert_oamp.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_wsm.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias wsm_certificate
Importing keystore cert_wsm.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore] |
| Step 14 | Restart the OAMP and WSM servers from Windows services. |
| Step 15 | In new browser tabs, type the following and check the certificates: https://<wsm ip>:8111
https://<oamp ip>:9443 |

| Note | Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity. CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format. Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client. |
|---|---|

| Note | Also, import the intermediate certificates shared by the CA to the keystore. |
|---|---|

| Step 1 | Log into the Reporting Server. For generating the keystore password, go to the %CVP_HOME%\bin folder and run the DecryptKeystoreUtil.bat file. |
|---|---|
| Step 2 | Download OpenSSL (64 bit) and install on your machine. |
| Step 3 | Add OpenSSL bin path to the Windows environment path variable. Example: path=C:\Program Files\OpenSSL-Win64\bin |
| Step 4 | Go to C:\Cisco\CVP\conf\security . |
| Step 5 | From the command prompt, run the following commands to generate the private keys and the CSRs for the Call server and WSM
                                             server: Call server: openssl ecparam -name prime256v1 -genkey -noout -out callserver-private-key.pem
openssl req -new -key callserver-private-key.pem -out callserver-cert.csr -days 360 WSM server: openssl ecparam -name prime256v1 -genkey -noout -out wsm-private-key.pem
openssl req -new -key wsm-private-key.pem -out wsm-cert.csr -days 360 |
| Step 6 | Enter the values for the following fields when prompted: Country Name (2 letter code) []:<>
State or Province Name (full name) []:<>
Locality Name (eg, city) []:<>
Organization Name (eg, company) []:<>
Organizational Unit Name (eg, section) []:<>
Common Name (eg, server FQDN or your name) []:.
Email Address []:.

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:.
An optional company name []:. This information is incorporated in your certificate request. Some fields ( Common Name , Email Address , A challenge password , and An optional company name ) can be left blank by entering a period (.). The certificate is generated after all the details are entered. |
| Step 7 | Run the following commands to see the certificate requests: openssl cat callserver-cert.csr
openssl cat wsm-cert.csr The encoded certificate request details are displayed. |
| Step 8 | Request for the CA-signed certificates: Submit the callserver-cert.csr and wsm-cert.csr files to your CA (who can provide signed ECDSA certificates). Note Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity. CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format. Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client. Wait for the CA's reply. Rename the certificate files received from the CA to callserver-cert.pem and wsm-cert.pem respectively. | Note | Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity. CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format. Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client. |
| Note | Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity. CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format. Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client. |
| Step 9 | From the command prompt, run the following commands to append the keys and certificates in one file: cat callserver-private-key.pem callserver-cert.pem > callserver-certificate-private.pem
cat wsm-private-key.pem wsm-cert.pem > wsm-certificate-private.pem |
| Step 10 | Run the following commands to export the certificates to the Reporting server: openssl pkcs12 -export -inkey callserver-private-key.pem -in callserver-certificate-private.pem -out callserver-cert.p12 -name callserver_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> openssl pkcs12 -export -inkey wsm-private-key.pem -in wsm-certificate-private.pem -out cert_wsm.p12 -name wsm_certificate
Enter Export Password:<CVP keystore password>
Verifying - Enter Export Password:<CVP keystore password> |
| Step 11 | Go to c:\cisco\cvp\conf\security and run the following commands to delete the existing RSA certificates for the Reporting server and WSM server: c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias callserver-certificate -storepass <CVP keystore password>
c:\cisco\CVP\jre\bin\keytool.exe -storetype JCEKS -keystore .keystore -delete -alias wsm_certificate -storepass <CVP keystore password> |
| Step 12 | Go to c:\cisco\cvp\conf\security and import the root certificate to the keystore: c:\cisco\CVP\jre\bin\keytool.exe -keystore .keystore -storetype JCEKS -import -alias root -trustcacerts -file <filename_of_root_cert> Note Also, import the intermediate certificates shared by the CA to the keystore. | Note | Also, import the intermediate certificates shared by the CA to the keystore. |
| Note | Also, import the intermediate certificates shared by the CA to the keystore. |
| Step 13 | Run the following commands to import the ECDSA certificates to the keystore: c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore callserver-cert.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias callserver_certificate
Importing keystore callserver-cert.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore]

c:\cisco\CVP\jre\bin\keytool.exe -v -importkeystore -srckeystore cert_wsm.p12 -srcstoretype PKCS12 -destkeystore .keystore -deststoretype JCEKS -alias wsm_certificate
Importing keystore cert_wsm.p12 to .keystore...
Enter destination keystore password:
Enter source keystore password:
[Storing .keystore] |
| Step 14 | Restart the Reporting and WSM servers from Windows services. |
| Step 15 | In new browser tabs, type the following and check the certificates: https://<callserver ip>:8443
https://<wsm ip>:8111 |

| Note | Details may vary from one CA to another. You can submit your request via a website, then the CA contacts you to verify your
                                                                        identity. CAs can send signed files in various formats and filenames. Typically, you receive the CA-signed files in PEM format. Request the CA for the intermediate certificates. One or more intermediate certificates are often, but not always, necessary to complete the chain of trust between
                                                                        your CA and a root CA-trusted client. |
|---|---|

| Note | Also, import the intermediate certificates shared by the CA to the keystore. |
|---|---|

| Note | To verify the base installer version, go to Control Panel > Programs > Programs and Features > Cisco CVP <version> . |
|---|---|