---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-user-guide-ccvp-b-b1203bdac1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/user/guide/ccvp_b_1261-user-guide-for-cisco-unified-cvp-vxml-server-and-call-studio/ccvp_b_1251-user-guide-for-cisco-unified-cvp-vxml-server-and-cisco-unified-call-studio-release-1251_chapter_0111.html
retrieved_at: 2026-08-21T17:42:02.290810+00:00
---

User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio Release 12.6(1)

# User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio Release 12.6(1)

Updated: May 14, 2021

Chapter: Web Service
	 Integration

## Chapter: Web Service
	 Integration

# Web Service
                     	 Integration

## SOAP
                        	 Service

### Web Services Element

Web services are a common way for any kind of application to communicate with externally hosted servers to retrieve information
                              or send notification events in a standard manner. Voice applications that access a web service can use the Web Services element.

Web Services Element —A special action element used to interface with a web service.

The Web Services element is an action element so it has the same features as the action element: it does not affect the call
                              flow and has a single exit state. The Web Services element, however, has a more complex configuration than a standard action
                              element. Call Studio renders this configuration with its own special interface.

One unique feature of the Web Services element is its ability to configure itself at design time. This is done by loading
                              a Web Services Description Language (WSDL) file. A WSDL file is an XML file that defines the operations supported by the web
                              services server. It is necessary in order to define the inputs required by the service that must be entered by the designer
                              and the outputs returned by the service that can then be stored for use later in the application.

For much more detailed information about how to use the Web Services element, refer to the Call Studio online help.

## Rest
                        	 Service

### Rest_Client
                           	 Element

Cisco Unified Call Studio 11.x and above includes the Rest_Client element. The Rest_Client element provides a flexible interface
                              in order to interact with REST endpoints. The communication between the REST client and server is made completely secure using
                              two-way Secure Sockets Layer (SSL). The Rest_Client element permits users to send GET, POST, PUT, or DELETE requests to application
                              servers.

### Ignore Certificate Validation

REST uses the
                              		boolean flag Ignore Certificate
                                 		  Validation to validate the certificate. The flag can be set to True or False . If the flag is set to False , the client checks for a valid server
                              		certificate in its keystore. If the certificate is not found, an error message
                              		appears.

Call Studio in
                                       			 debug mode: C:\Cisco\CallStudio\eclipse\jre\lib\security\cacerts

Call Studio in
                                       			 VXML Server: C:\Cisco\CVP\jre\lib\security\cacerts

Before you
                                          		  validate, ensure that the required certificate is in the respective keystore.

### Import Certificate in Call Studio for Debug Mode

Step 1

Copy the REST server certificate file manually to the call studio machine.

Step 2

From the
                                          			 command prompt, navigate to C:\Cisco\CallStudio\eclipse\jre\bin .

Step 3

Run the
                                          			 following command to import the server certificate to the client keystore:

The certificate is imported to the client keystore with the default alias name mykey and password changeit

Step 4

Run the
                                          			 following command to check whether the certificate is imported.

### Import Certificate
                           	 in VXML Server

Step 1

Copy the REST server certificate file manually to VXML server.

Step 2

From the command prompt, navigate to %CVP_HOME%\jre\bin .

Step 3

Run the following command to import the server certificate to the client keystore:

Step 4

Step 5

Run the following command to check whether the certificate is imported.

Step 6

Restart the VXML Server after importing the certificate.

### Create One-Way
                           	 Communication Between VXML and REST Server

One-way secure
                                 		  communication imports the REST Server Certificate Authority (CA) certificate
                                 		  into the VXML server trust store, if CA is not available by default.

Perform the
                                 		  following steps to import the REST Server CA certificate into the VXML server:

Step 1

Use the Java
                                          			 key tool to export the CA certificate from the REST Server.

Step 2

Copy the
                                          			 exported CA certificate file from the REST Server to the VXML Server.

For example :
                                             				<RESTServer_ca_cert>

Step 3

From the
                                          			 command prompt, run the following command to import the REST Server CA
                                          			 certificate into the VXML truststore:

File path to
                                             				VXML truststore: %CVP_HOME%\jre\lib\security\cacerts . The default
                                             				password is changeit .

For a self-
                                                         				  signed certificate, export the ca_cert from the REST Server and the self-signed
                                                         				  certificate. Then, import this self-signed certificate in the VXML Server trust
                                                         				  store.

Step 4

Restart the
                                          			 Cisco Unified CVP VXML Server service running in VXML Server.

Do not
                                                         				  import a server certificate signed with a standard CA to the VXML Server trust
                                                         				  store, as it contains standard CA details.

### Create Two-Way
                           	 Communication Between VXML and REST Server

Two-Way secure
                                 		  communication between VXML and REST Server involves importing the VXML Server
                                 		  CA certificate into the REST Server trust store.

Perform the
                                 		  following steps to import the VXML Server CA certificate on the REST Server:

Step 1

Retrieve the keystore password from the security.properties file on the VXML Server. Filepath %CVP_HOME%\conf\security.properties

Step 2

Use the Java key tool to find the certificate and export the VXML Server CA certificate from the keystore.

File path to root: %CVP_HOME%\conf\security\.ormKeystore .

Use the list flag to check your keystore entries by running the following command:

%CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore

%CVP_HOME%\conf\security\.ormKeystore -list

Run the following command to export the VXML Server certificate:

%CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.ormKeystore -storetype JCEKS -alias vxml_root_certificate
                                                -file %CVP_HOME%\conf\security\<root>

Step 3

Copy the
                                          			 exported certificate file from the managed Cisco Unified CVP VXML Server to the
                                          			 REST Server.

Step 4

Use the
                                          			 following Java key tool command to import the certificate into the REST Server
                                          			 truststore

For a
                                                               						self-signed certificate, export the ca_cert from the VXML Server and import the
                                                               						ca_cert to the REST Server truststore.

For a
                                                               						VXML standard trusted CA, do not import the CA certificate on the REST Server
                                                               						truststore.

### XPath
                           	 Expression

Cisco Unified Call Studio includes a new utility that allows you to use
                              		XPath expressions in JavaScript to return values from the XML. You can specify
                              		an XPath expression in the element setting. If the REST response is an XML,
                              		then the nodes which are returned are available as element data. Based on the
                              		XML result from the GET method, you can add XPath expression to get the value
                              		of a specific row.

For example, consider the following XML you get when you query WSM SNMP
                              		public:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>	
<results>
    <communities>
        <community>
            <name>Hello</name>
            <snmpversion>V1</snmpversion>
            <acceptfromanyhost>true</acceptfromanyhost>
            <accessprivilege>readWrite</accessprivilege>
            <servers>
                <server>IP address</server>
            </servers>
        </community>
    </communities>
    <pageinfo>
        <resultsPerPage>25</resultsPerPage>
        <startIndex>0</startIndex>
        <totalResults>1</totalResults>
    </pageinfo>
</results>
```

To get the value from one specific row, use the following XPath
                              		expression: /results/communities/community/snmpversion .

The output of the expression is V1 .

If you use the following XPath
                              		expression: /results/communities/community/name .

The output of the expression is Hello .

### JSONPath
                           	 Expression

Cisco Unified Call Studio includes a new utility that allows you to specify a JSONPath expression in the element setting.
                              The nodes which are returned are available as element data if the REST response is a JSON.

```
{"results": {
	"communities": {
		"community": {
			"name": "Hello",
			"snmpversion": "V1",
			"acceptfromanyhost": true,
			"accessprivilege": "readWrite",
			"servers": {
			"server": "IP address"}
			}
		},
"pageinfo": {
"resultsPerPage": 25,
"startIndex": 0,
"totalResults": 1
}
}
}
```

To get the value from one specific row, use the following XPath expression: $.results.communities.community.snmpversion

The output of the expression is V1 .

If you use the following XPath expression: $.results.communities.community.name

The output of the expression is Hello .

| Note | Before you
                                          		  validate, ensure that the required certificate is in the respective keystore. |
|---|---|

| Step 1 | Copy the REST server certificate file manually to the call studio machine. |
|---|---|
| Step 2 | From the
                                          			 command prompt, navigate to C:\Cisco\CallStudio\eclipse\jre\bin . |
| Step 3 | Run the
                                          			 following command to import the server certificate to the client keystore: keytool.exe -importcert -file <path to REST server certificate> -keystore c:\Cisco\CallStudio\eclipse\jre\lib\security\cacerts Enter the keystore password. The default password is changeit . The certificate is imported to the client keystore with the default alias name mykey and password changeit |
| Step 4 | Run the
                                          			 following command to check whether the certificate is imported. keytool.exe -list
                                             				-keystore c:\Cisco\CallStudio\eclipse\jre\lib\security\cacerts. |

| Step 1 | Copy the REST server certificate file manually to VXML server. |
|---|---|
| Step 2 | From the command prompt, navigate to %CVP_HOME%\jre\bin . |
| Step 3 | Run the following command to import the server certificate to the client keystore: keytool.exe -importcert -trustcacerts -file <path to REST server certificate> -alias <unique alias name> -keystore %CVP_HOME%\jre\lib\security\cacerts Enter the keystore password. The default password is changeit . |
| Step 4 |  |
| Step 5 | Run the following command to check whether the certificate is imported. keytool.exe -list -keystore %CVP_HOME%\jre\lib\security\cacerts |
| Step 6 | Restart the VXML Server after importing the certificate. |

| Step 1 | Use the Java
                                          			 key tool to export the CA certificate from the REST Server. |
|---|---|
| Step 2 | Copy the
                                          			 exported CA certificate file from the REST Server to the VXML Server. For example :
                                             				<RESTServer_ca_cert> |
| Step 3 | From the
                                          			 command prompt, run the following command to import the REST Server CA
                                          			 certificate into the VXML truststore: ..\..\bin\keytool
                                             				-importcert -keystore <path to the VXML Truststore> -alias <alias
                                             				name> -file <Path to RESTServer_ca_cert> File path to
                                             				VXML truststore: %CVP_HOME%\jre\lib\security\cacerts . The default
                                             				password is changeit . Note For a self-
                                                         				  signed certificate, export the ca_cert from the REST Server and the self-signed
                                                         				  certificate. Then, import this self-signed certificate in the VXML Server trust
                                                         				  store. | Note | For a self-
                                                         				  signed certificate, export the ca_cert from the REST Server and the self-signed
                                                         				  certificate. Then, import this self-signed certificate in the VXML Server trust
                                                         				  store. |
| Note | For a self-
                                                         				  signed certificate, export the ca_cert from the REST Server and the self-signed
                                                         				  certificate. Then, import this self-signed certificate in the VXML Server trust
                                                         				  store. |
| Step 4 | Restart the
                                          			 Cisco Unified CVP VXML Server service running in VXML Server. Note Do not
                                                         				  import a server certificate signed with a standard CA to the VXML Server trust
                                                         				  store, as it contains standard CA details. | Note | Do not
                                                         				  import a server certificate signed with a standard CA to the VXML Server trust
                                                         				  store, as it contains standard CA details. |
| Note | Do not
                                                         				  import a server certificate signed with a standard CA to the VXML Server trust
                                                         				  store, as it contains standard CA details. |

| Note | For a self-
                                                         				  signed certificate, export the ca_cert from the REST Server and the self-signed
                                                         				  certificate. Then, import this self-signed certificate in the VXML Server trust
                                                         				  store. |
|---|---|

| Note | Do not
                                                         				  import a server certificate signed with a standard CA to the VXML Server trust
                                                         				  store, as it contains standard CA details. |
|---|---|

| Step 1 | Retrieve the keystore password from the security.properties file on the VXML Server. Filepath %CVP_HOME%\conf\security.properties |
|---|---|
| Step 2 | Use the Java key tool to find the certificate and export the VXML Server CA certificate from the keystore. File path to root: %CVP_HOME%\conf\security\.ormKeystore . Use the list flag to check your keystore entries by running the following command: %CVP_HOME%\jre\bin\keytool.exe -storetype JCEKS -keystore %CVP_HOME%\conf\security\.ormKeystore -list Run the following command to export the VXML Server certificate: %CVP_HOME%\jre\bin\keytool.exe -export -v -keystore %CVP_HOME%\conf\security\.ormKeystore -storetype JCEKS -alias vxml_root_certificate
                                                -file %CVP_HOME%\conf\security\<root> |
| Step 3 | Copy the
                                          			 exported certificate file from the managed Cisco Unified CVP VXML Server to the
                                          			 REST Server. |
| Step 4 | Use the
                                          			 following Java key tool command to import the certificate into the REST Server
                                          			 truststore keytool -import -trustcacerts -keystore <Path to REST server Truststore> -alias <Alias_name> vxml_root_certificate -file <path
                                             to VXMLca_cert_file > Note For a
                                                               						self-signed certificate, export the ca_cert from the VXML Server and import the
                                                               						ca_cert to the REST Server truststore. For a
                                                               						VXML standard trusted CA, do not import the CA certificate on the REST Server
                                                               						truststore. | Note | For a
                                                               						self-signed certificate, export the ca_cert from the VXML Server and import the
                                                               						ca_cert to the REST Server truststore. For a
                                                               						VXML standard trusted CA, do not import the CA certificate on the REST Server
                                                               						truststore. |
| Note | For a
                                                               						self-signed certificate, export the ca_cert from the VXML Server and import the
                                                               						ca_cert to the REST Server truststore. For a
                                                               						VXML standard trusted CA, do not import the CA certificate on the REST Server
                                                               						truststore. |

| Note | For a
                                                               						self-signed certificate, export the ca_cert from the VXML Server and import the
                                                               						ca_cert to the REST Server truststore. For a
                                                               						VXML standard trusted CA, do not import the CA certificate on the REST Server
                                                               						truststore. |
|---|---|