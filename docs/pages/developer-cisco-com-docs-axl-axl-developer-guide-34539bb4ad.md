---
doc_id: developer-cisco-com-docs-axl-axl-developer-guide-34539bb4ad
source_url: https://developer.cisco.com/docs/axl/axl-developer-guide/
retrieved_at: 2026-09-27T15:05:05.905631+00:00
---

# Overview

Administrative XML (AXL) is a powerful provisioning API to extend Cisco Unified Communications Manager (Unified CM). It can help businesses leverage their services to users by automating everyday communications configuration tasks. The AXL API provides a mechanism for programmers to make several types of changes to the Cisco Unified CM Database using XML and the SOAP interface.

Note: this guide covers AXL for CUCM versions 11.5 - 15.  For earlier guides, see Archived References

AXL is a provisioning and configuration API, not a real-time API. Beware that an attempt to make too many AXL requests in quick succession could be throttled. See Data Throttling and Performance .

Examples of AXL operations include:

- add data

- apply data

- get data

- list data

- lockPhone

- remove data

- reset devices

- restart devices

- update data

- wipePhone

AXL API methods, known as requests, use a combination of HTTPS and SOAP. Users perform requests by sending XML data to the Unified CM Publisher server. If the request completes successfully, the system returns the appropriate AXL response. All responses are named the same as associated requests, except the word Response is appended. For example, the XML response returned from an addPhone request is named addPhoneResponse .

Developers must have knowledge or experience in the following areas:

- TCP/IP Protocol

- Hypertext Transport Protocol, specifically HTTPS

- Socket programming

- XML

- SOAP

Users of the AXL API must have a firm grasp of XML syntax and schema, which is used to define AXL requests, responses, and errors.

For more information about XML schema, refer to https://www.w3.org/TR/xmlschema-0/ .

For more information about XML syntax/grammar, refer to https://www.w3.org/TR/rdf-syntax-grammar/ .

The AXL service is enabled by default on all nodes (Publisher and Subscribers.) It is recommended that developers always access AXL on the Publisher.

Caution The AXL API allows you to modify the CUCM system configuration database. Be careful not to delete or change objects unintentionally.

## AXL Compliance

The Unified CM AXL implementation complies with XML Schema 1.0

The Unified CM AXL implementation also complies with SOAP 1.1 and HTTPS 1.1 as defined by the World Wide Web Consortium https://www.w3.org/ . The AXL API runs as an independent service and can only be accessed via HTTPS.

## Cisco Product Security Overview

This product contains cryptographic features and is subject to United States and local country laws governing import, export, transfer, and use.

Note: Delivery of Cisco cryptographic products does not imply third-party authority to import, export, distribute, or use encryption. Importers, exporters, distributors, and users are responsible for compliance with U.S. and local country laws. By using this product you agree to comply with applicable laws and regulations. If you are unable to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at: https://www.cisco.com/wwl/export/crypto/tool/stqrg.html . If you need further assistance, contact us by sending e-mail to export@cisco.com .

# Development Guidelines

## Recommendations for Developers

The following are recommendations for developers to reduce the number and extent of updates.

- For a feature invocation involving two or more independent transactions, the events or messages may be interleaved.

- In such cases, events related to the second transaction may precede messages related to the first.

- Events or messages may be delayed due to situations beyond control of the interface, for example network or transport failures.

- Applications should be able to recover from out-of-order events or messages, even when the order is required for protocol operation.

- Developers must avoid unnecessary dependence on the order of elements to interpret information. The order of elements within the interface event or message may change, within the constraints of the protocol specification.

- Developers must disregard or provide generic treatments for any unknown elements or unknown values of known elements encountered. New interface events, methods, responses, headers, parameters, attributes, other elements, or new values of existing elements may be introduced.

- Previous interface events, methods, responses, headers, parameters, attributes, and other elements will remain and maintain their previous stated meaning and behavior in every way possible. They will remain consistent even when defects with them need to be corrected.

- Applications must never be dependent on interface behavior resulting from defects. That is, not consistent with the published interface specifications. Application behavior might change when a defect is fixed.

- Remove deprecated methods, handlers, events, responses, headers, parameters, attributes, or other elements from applications as soon as possible to avoid issues when those deprecated items are removed from Cisco Unified CM.

- Application developers must be aware that not all new features or new supported devices will be forward compatible. New features and devices (for example, phones) may require application modifications to work properly.

# New and Changed Information

This section provides New and Changed Information for the Unified CM AXL Interface:

For a complete list of the AXL APIs and the versions of Cisco Unified Communications Manager in which they appear see the Operations by Release Matrix .

## New and Changed Information for Unified CM Release 15

### Notes:

- No API changes made for Unified CM Release 15

## New and Changed Information for Unified CM Release 14

### Notes:

XSI namespace attribute location for Nil elements

Prior to CUCM v14, if multiple elements in a response were nil (null), XMLSchemaInstance namespace attributes were added to each nil individual element

Old Behaviour

xml

```
< sshUserId xsi: nil = " true " uuid = " " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " /> < sshPwd xsi: nil = " true " uuid = " " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " />
```

In v14+, if any element in an AXL response body is nil, an XMLSchemaInstance namespace attribute will appear only in the parent/top-level AXL response name element:

xml

```
< ns: getPhoneResponse xmlns: ns = " http://www.cisco.com/AXL/API/12.0 " xmlns: xsi = " http://www.w3.org/2001/XMLSchema-instance " > < sshUserId uuid = " " /> < sshPwd uuid = " " /> </ ns: getPhoneResponse >
```

Both representations are valid and logically/semantically equivalent per SOAP v1.1; however applications with hard-coded/inflexible response parsing may behave differently.

## New and Changed Information for Unified CM Release 12.5(1)

### New APIs

### Changed APIs

## New and Changed Information for Unified CM Release 12.0(1)

## New APIs

## Changed APIs

## New and Changed Information for Unified CM Release 11.5(1)

### New Features:

AXL Read-Only Role

The AXL user can now be assigned a read-only role, allowing the application to read (but not add/update/remove) AXL data.  Refer to AXL Authentication for more details.

User Rank access control support

CUCM can be configured by the administrator to control the ability of users, including AXL API users, to access or update certain CUCM data, via the User Rank feature.  The CUCM user account used by an application to authenticate to AXL is also subject to the access control restrictions of the User Rank feature, which may affect certain types of AXL requests.  See User Rank Interactions for more details.

11.5 schema added

### New APIs

### Changed APIs

## New and Changed Information for Unified CM Release 11.0(1)

- 11.0 schema added

### New APIs

### Changed APIs

## New and Changed Information for Unified CM Release 10.5(1)

- 10.5 schema added

### New APIs

### Changed APIs

## AXL Versioning Policy for Unified CM Release 10.5(1)

The versioning mechanism supports three major releases of schemas to provide additional upgrade flexibility. For example, Unified CM release 10 supports AXL schemas 8.x, 9.x, and 10.x, while the 7.x schema is no longer available. Each major and minor release will include a new schema. Maintenance releases never include new schemas. Old schemas will be deprecated in the first release of each new major version, for example Release 7.0(1). Read the details here .

## Change Notification Feature for Unified CM Release 10.5(1)

Administrative XML (AXL) Clients depend on Cisco Unified CM data to work correctly. The AXL Change Notification Feature (CNF) is designed to help keep AXL applications informed when dependent data changes occur. Learn how to add Change Notification to your application here .

## New Operations and Features for Unified CM Release 10.5(1)

### Apply, Reset, and Restart API Operations

Note: Reset operations should be used with extreme caution, especially when applied to device pools, where large numbers of users can be impacted. Resetting a device makes it unavailable to the user until the operation is completed, since it interrupts service and shuts down the device or service entirely. Applying changes to device pools or several concurrent users simultaneously should only be managed at scheduled maintenance periods.

### getOptionsList

getOptionsList allows interrogation of devices to determine valid options for that device. SipProfileOptions , TransPatternOptions , LineOptions , PhoneOptions , and DeviceProfileOptions were provided as additional tools to help developers solve performance issues.

### wipePhone

wipePhone allows Cisco's newer Android-based devices like the Cisco DX650 to be remotely reset to factory defaults, removing user specific settings and data. This API is typically used when device ownership changes or when device access is compromised.

# Versioning

Applications can make AXL requests specifying any one of several AXL schema versions offered by the AXL service in any given CUCM release. Use of AXL versioning enables developers to support multiple Unified CM releases and maintain backward compatibility after customer upgrades.

Applications can specify the specific schema version they wish to use by including a version number in the SOAPAction header value and in the AXL XML namespace URI in the body of the request:

Header : SOAPAction: "CUCM:DB ver=14.0 getCCMVersion" Body : xmlns:ns="http://www.cisco.com/AXL/API/14.0"

Both should be included, and must indicate the same version, for example:

Example HTTP Request Specifying schema version 14.0

xml

```
POST https://sjds-cucm14.cisco.com:8443/axl/ HTTP/1.1
Content-Type: text/xml;charset=UTF-8
SOAPAction: "CUCM:DB ver=14.0 getCCMVersion"
Content-Length: 295
Authorization: Basic QaW5pcvcjpjaXNjb3BzZHQ= < soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: ns = " http://www.cisco.com/AXL/API/14.0 " > < soapenv: Header /> < soapenv: Body > < ns: getCCMVersion > < processNodeName > </ processNodeName > </ ns: getCCMVersion > </ soapenv: Body > </ soapenv: Envelope >
```

If the application does not wish to specify any particular schema version for a request, it can omit the SOAPAction header and include the special version 1.0 in the AXL XML namespace URI.  In this case, CUCM will attempt to apply the lowest version supported by the CUCM release:

Example Requesting the Default/Oldest Version

xml

```
POST https://sjds-cucm14.cisco.com:8443/axl/ HTTP/1.1
Content-Type: text/xml;charset=UTF-8
Content-Length: 295
Authorization: Basic QaW5pcvcjpjaXNjb3BzZHQ= < soapenv: Envelope xmlns: soapenv = " http://schemas.xmlsoap.org/soap/envelope/ " xmlns: ns = " http://www.cisco.com/AXL/API/1.0 " > < soapenv: Header /> < soapenv: Body > < ns: getCCMVersion > < processNodeName > </ processNodeName > </ ns: getCCMVersion > </ soapenv: Body > </ soapenv: Envelope >
```

In the example above, if the request is sent to CUCM v14, AXL schema version 11.0 would be applied.

Schema Version Requested vs. Version Applied

1 12.5(1)SU3/11.5(1)SU10 schemas were modified to include new headset configuration objects.

## Backward Compatibility Best Practices

Applications should always specify the desired schema version in the SOAPAction header and AXL XML namespace URI to ensure the expected schema is applied (see Versioning ).

If applications omit a SOAPAction header and specify AXL XML namespace URI version 1.0 , the oldest schema version available will be applied.

Applications should avoid using <executeSQLQuery> and <executeSQLUpdate> when feasible, as these requests manipulate the CUCM database directly (via SQL) - this bypasses the AXL database abstraction layer provided by other (non-SQL) AXL requests.  As the underlying CUCM database structure may change without notice in any CUCM release, applications should take care to validate <executeSQLQuery> / <executeSQLUpdate> response data, be prepared to handle unexpected request errors, and test against all ( N.N.N ) CUCM releases.

New schema versions will be added in each CUCM major and minor release ( N.N.n ).

Maintenance/Service Releases ( N.N.N ) are not expected to include new schema versions.

Applications should plan to implement support as soon as possible for the latest schema versions available in CUCM major releases ( N.n.n ).

Old schema versions will be supported for two major CUCM releases ( N-2 ).

Old schema versions will be removed only in major releases ( N.n.n ).

All old ( N-3 ) schema versions will be removed in major CUCM releases.  For example:

- CUCM 12.0(1) : supports schema versions: 12.0 / 11.x / 10.x ; schema versions 9.x and older were removed.

- CUCM 12.5(1) : supports schema versions: 12.x / 11.x / 10.x / 9.x ; no schema versions were removed.

Note: CUCM version numbering skipped version 13.x entirely.

# AXL HTTP Request Basics

To make an AXL request, an application sends XML data - formatted according to the AXL schema - to the CUCM via HTTP POST :

Request Details

Requests must be transmitted securely, using HTTPS 1.1/TLS 1.3+

By default, the AXL web service encrypts SSL communication using a self-signed public key certificate (see the Certificates in the Security Guide for Cisco Unified Communications Manager ).  Applications should be prepared to import/trust the AXL certificate (or disable certificate checking).

Requests are sent using the HTTP POST method.

The Content-Type header should be text/xml

The Accept header should be text/xml

The SOAPAction header should contain the desired AXL version string (see Versioning ).

The request body should be UTF-8 encoded.

All requests should be sent to the CUCM cluster Publisher, via the AXL base URL:

Code Snippet

```
https://{cucm_hostname}:8443/axl/
```

Note: the base URL trailing ' / ' is required

# 'Hello World' Sample Application

To get familiar with using AXL, let's try configuring and running a basic Java application.

Prerequisite: you will need to have a Java Development Kit (JDK) installed.  This project was tested with OpenJDK 11 .

As a first step, to keep everything in one place you will likely want to create a new, empty directory for storing/running the various sample project files.

For example, from a terminal:

Code Snippet

```
mkdir axlsample
cd axlsample
```

## Downloading the AXL Certificate

Before making AXL requests, applications need to be prepared to make a secure SSL HTTPS connection to the AXL web service.   If CUCM is using self-signed/admin-installed public key certificates to encrypt its SSL traffic, applications will likely need to download/install/import the CUCM tomcat certifcate into their system in order to successfully establish connection.

Note: applications should always implement SSL client-side server certificate checking in production.

For this project, which will be using the HttpUrlConnection object from the Java Standard Library to send and receive XML over HTTP, we need to download the AXL certificate from CUCM and import it into a local Java TrustStore file:

In the CUCM admin web pages, navigate to Cisco Unified OS Administration -> Security -> Certificate Management

Then find and download the tomcat certificate, in PEM format:

Make sure to download the file into your sample project directory.

## Importing the AXL Certificate

Java provides the keytool command for importing certificates into an encrypted TrustStore file , for use by java.net SSL applications:

From a terminal window in your project directory, run the following command:

Code Snippet

```
$JAVA_HOME/bin/keytool -keystore cacerts -alias tomcatcert -import -file tomcat.pem
```

Note: if $JAVA_HOME is not set, you can replace it with the full path to your Java installation.

Specify the password as: changeit

Then accept/complete the rest of the dialog.

This should result in a new file named cacerts in your project directory.

## Running the Sample Application

The Java code for the sample is shown below:

hello_world.java

java

```
public class helloworld { public static void main ( String [ ] args ) throws java . io . IOException { // String containing the AXL request XML.  White space is for readability; ignored by AXL String request = "<soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:ns='http://www.cisco.com/AXL/API/14.0'>" + "<soapenv:Header/>" + "  <soapenv:Body>" + "    <ns:getCCMVersion>" + "      <processNodeName></processNodeName>" + "    </ns:getCCMVersion>" + "  </soapenv:Body>" + "</soapenv:Envelope>" ; java . net . URL axlUrl = new java . net . URL ( "https://cucm.abc.inc:8443/axl/" ) ; // SSL security prerequisite step: Import CUCM AXL Tomcat CA certificate into file 'cacerts' // Set system SSL truststore to 'cacerts'; 'changeit' as the password: System . setProperty ( "javax.net.ssl.trustStore" , "cacerts" ) ; System . setProperty ( "javax.net.ssl.trustStorePassword" , "changeit" ) ; java . net . HttpURLConnection connection = ( java . net . HttpURLConnection ) axlUrl . openConnection ( ) ; // Create a connection object connection . setConnectTimeout ( 20000 ) ; // Configure and read timeouts (in ms) connection . setReadTimeout ( 20000 ) ; connection . setDoOutput ( true ) ; // Enable URLConnection for outbound requests connection . setRequestMethod ( "POST" ) ; // User HTTP POST // Set HTTP Headers connection . setRequestProperty ( "Accept" , "text/xml" ) ; connection . setRequestProperty ( "Content-Type" , "text/xml" ) ; connection . setRequestProperty ( "SOAPAction" , "CUCM:DB ver=14.0 getCCMVersion" ) ; // Request 14.0 AXL version // Basic Auth encode the AXL user credentials connection . setRequestProperty ( "Authorization" , "Basic " + java . util . Base64 . getEncoder ( ) . encodeToString ( ( "Administrator" + ":" + "password" ) . getBytes ( java . nio . charset . StandardCharsets . UTF_8 ) ) ) ; java . io . OutputStream outputStream = connection . getOutputStream ( ) ; // Make the TCP/SSL connection outputStream . write ( request . getBytes ( "UTF-8" ) ) ; // Encode/send data/close connection outputStream . flush ( ) ; outputStream . close ( ) ; java . io . InputStream inputStream = connection . getInputStream ( ) ; // Setup response stream byte [ ] res = new byte [ 2048 ] ; // Create 2048 byte buffer array int i = 0 ; StringBuilder response = new StringBuilder ( ) ; // Allows easy concatenation of strings while ( ( i = inputStream . read ( res ) ) != - 1 ) { response . append ( new String ( res , 0 , i ) ) ; } // Read until done (-1) inputStream . close ( ) ; System . out . println ( response . toString ( ) ) ; } }
```

Create a new file named hello_world.java in  your project directory and copy/paste in the code.  (Don't foget to save the file).

From the terminal, use the Java compiler compile the hello_world.java source file:

Code Snippet

```
javac hello_world.java
```

Finally, you can run the compiled program:

Code Snippet

```
java hello_world
```

# Authentication

Refer to AXL Authentication .

# Handling AXL Unique IDs

Most objects used in AXL requests or in the CUCM SQL database have a unique identification value in the form of a UUID .  Many AXL requests can use an object's name or UUID when specifying the object.  This identifier may be referred to as a UUID, PKID or primary key and is composed of a sequence of letters, dashes and numbers:

Code Snippet

```
F889E5C4-B277-4FE8-9749-932BC27D2401
```

In general, AXL responses will display/accept UUIDs surrounded by braces and using alpha characters in uppercase:

xml

```
< ldapAuthentication uuid = " {A8D94FF0-4627-EECC-0D8D-E2EE69123B32} " >
```

However, in the CUCM SQL database itself, primary key values are stored without braces and using lowercase alpha characters.  As a result, when manipulating objects using <executeSqlQuery> and <executeSqlUpdate> , be sure to convert any UUIDs sent in the SQL statements to lowercase (remove braces,) and be prepared to handle bare lowercase UUIDs in responses:

<executeSqlQuery> request snippet:

xml

```
< sql > select dnorpattern, description from numplan where pkid = "f056d852-7cb9-f197-cf7d-6fc34719d26c" </ sql >
```

<executeSqlQuery> response snippet:

xml

```
< return > < row > < name > DS-CUC115 </ name > < pkid > d90b6466-1721-3bf2-d2f4-ca8eaac8e6f7 </ pkid > </ row > < row > < name > testLineGroup </ name > < pkid > a6ed4f3c-885f-971f-3c98-e20c2e1f4dc4 </ pkid > </ row > </ return >
```

Note: AXL requests (other than <executeSqlQuery> / <executeSqlUpdate> ) will accept UUIDs in either upper or lowercase, and with or without braces.

# Data Throttling and Performance

The developer can make powerful modifications of the Unified CM System database using the AXL API. Caution should always be observed during implementation since every API call impacts the system. Requesting large amounts of data or performing multiple write operations may trigger the interface throttle to return an exception. The throttle protects system resources to ensure calls are processed before XML requests.

AXL acts as a provisioning and configuration API, not as a real-time API.

The AXL interface provides developers with two ways of accessing database objects:

- Standard methods which provide backward compatibility between releases, such as GetUser

- Direct access through the ExecuteSQLQuery and ExecuteSQLUpdate methods, which do not provide backward compatibility.

The AXL service dynamically throttles write requests (add, update, and remove requests, and ExecuteSQLUpdate ) based on the current size of the Unified CM database transaction queue. Note that the Unified CM database transaction queue can contain pending updates arising from recent administrative actions, bulk administration tasks, and other AXL applications. If the database transaction queue is too large, AXL may reject new write requests with a 503: Service Unavailable error message. In such cases, applications may retry rejected requests. However, retries should be attempted after a reasonable delay, for example several seconds.

Read requests are also dynamically throttled based on the size of the data set to be returned. Large queries issued using the List <object> and ExecuteSQLQuery methods that result in a data set greater than 8 MB will return Query request too large. Total rows matched: <Matched Rows>. Suggested row fetch: less than <Number of Rows> .

Cisco recommends developers using the ExecuteSQLQuery method follow these guidelines:

- Applications should break up all SQL queries so that the data returned is always less than 8 MB

- Use the Unified CM Data Dictionary to help determine the maximum allowable size of any field in the database

- ASCII characters are stored as 1-byte

- i18n characters (UTF-8) are stored as 3-bytes

- DB has a mix of ASCII and UTF-8 characters

- While Unified CM is processing a large query, concurrent queries should not result in data sets larger than 2 MB

- Applications should wait to receive a response before issuing subsequent queries

- Applications should not submit duplicate queries

Note: Because AXL is not a real-time API, the auto-logout function of Extension Mobility (EM) does not work when the user is logged in or out of EM via the AXL interface.

Below are some example request and response pairs that show what to expect in different throttling scenarios.

Scenario 1 An AXL query request that tries to fetch more than 8 MB of data.

Request:

xml

```
< soapenv: Envelope xmlns: soapenv = " https://schemas.xmlsoap.org/soap/envelope/ " xmlns: ns = " https://www.cisco.com/AXL/API/10.0 " > < soapenv: Header /> < soapenv: Body > < ns: executeSQLQuery sequence = " ? " > < sql > select * from enduser, device </ sql > </ ns: executeSQLQuery > </ soapenv: Body > </ soapenv: Envelope >
```

Response:

xml

```
< soapenv: Envelope xmlns: soapenv = " https://schemas.xmlsoap.org/soap/envelope/ " > < soapenv: Body > < soapenv: Fault > < faultcode > soapenv:Server </ faultcode > < faultstring > Query request too large. Total rows matched: 2816 rows. Suggestive Row Fetch: less than 844 rows </ faultstring > < detail > < axlError > < axlcode > -1 </ axlcode > < axlmessage > Query request too large. Total rows matched: 2816 rows. Suggestive Row Fetch: less than 844 rows </ axlmessage > < request > executeSQLQuery </ request > </ axlError > </ detail > </ soapenv: Fault > </ soapenv: Body > </ soapenv: Envelope >
```

Scenario 2 Too many concurrent ExecuteSQLQuery requests.

Request:

xml

```
< soapenv: Envelope xmlns: soapenv = " https://schemas.xmlsoap.org/soap/envelope/ " xmlns: ns = " https://www.cisco.com/AXL/API/10.0 " > < soapenv: Header /> < soapenv: Body > < ns: executeSQLQuery sequence = " ? " > < sql > select first 999 * from device, enduser </ sql > </ ns: executeSQLQuery > </ soapenv: Body > </ soapenv: Envelope >
```

Response:

xml

```
< soapenv: Envelope xmlns: soapenv = " https://schemas.xmlsoap.org/soap/envelope/ " > < soapenv: Body > < soapenv: Fault > < faultcode > soapenv:Server </ faultcode > < faultstring > Maximum AXL Memory Allocation Consumed. Please retry once requests in progress have completed </ faultstring > < detail > < axlError > < axlcode > -1 </ axlcode > < axlmessage > Maximum AXL Memory Allocation Consumed. Please retry once requests in progress have completed </ axlmessage > < request > executeSQLQuery </ request > </ axlError > </ detail > </ soapenv: Fault > </ soapenv: Body > </ soapenv: Envelope >
```

## Using JSESSIONIDSSO to Improve Performance

One way to streamline the performance of multiple sequential AXL operations is to reuse the JSESSIONIDSSO cookie returned with the first request. This allows you to use a single HTTP session (via HTTP 1.1 persistent connection) for making multiple AXL requests.

Here’s how it works: when you perform an AXL SOAP operation, it returns a JSESSIONIDSSO cookie in the response header. For example:

http

```
Set-Cookie : JSESSIONIDSSO=3D63989808D8A7FE32BE0D8BA; path=/; domain=.ds-ucm115-1.cisco.com; Secure; HttpOnly; Expires=Tue, 19 Jan 2038 03:14:07 GMT;
```

In order to continue to use the same authentication session with AXL (instead of creating a new session for each subsequent request,) you should return the same JSESSIONIDSSO cookie with subsequent requests, via the Cookie header (note, omit the Authentication header when using a JSESSIONSSO cookie.)  As you continue using the same JSESSIONIDSSO, AXL will continue to use the same internal session, thus reducing the stress on CUCM when compared to creating new AXL sessions with every request.

http

```
Cookie : JSESSIONIDSSO=3D63989808D8A7FE32BE0D8BA; path=/; domain=.ds-ucm115-1.cisco.com; Secure; HttpOnly; Expires=Tue, 19 Jan 2038 03:14:07 GMT;
```

Note: You can re-use the AXL authentication session via JSESSIONIDSSO either within the same HTTP persistent connection session, or in separate HTTP connections/requests

The JSESSIONIDSSO has a default timeout of 30 minutes in AXL, but the timeout clock only starts ticking when the connection is idle. You could theoretically continue to use the same JSESSIONIDSSO indefinitely, or at least until you stop performing requests with that particular JSESSIONIDSSO for 30 minutes. If your JSESSIONIDSSO-based connection is idle for more than 30 minutes (i.e. you get an HTTP 404 response status code), make a new request without specifying a JSESSIONIDSSO while including the Authentication header with credentials. This request should return a new JSESSIONIDSSO.

## Re-Using HTTP Connections

Applications performaning multiple AXL requests should also implement HTTP 1.1 persistent connections with the AXL service.  This will maintain and re-use the HTTP connection between app and AXL, which will make subsequent requests faster, and reduce memory/CPU and network object pressure for CUCM.

# Data Change Notification

## Overview

Administrative XML (AXL) clients may be dependent upon up-to-date Unified Cisco CM data to function properly. While apps can periodically request updated data from CUCM via AXL in a pull/polling model, the AXL Change Notification Feature (CNF) is designed to help keep AXL applications informed when CUCM data changes via a more push/notification-type mechanism. This section is intended to show AXL Developers how to add change notification functionality to their applications. Change notification features are applicable to Cisco Unified CM 10.0 and above.

## How It Works

AXL will record changes for objects exposed within the AXL interface into an internal tracking cache. CUCM database changes are 'transformed', as they occur, from the raw table/column update data to their corresponding AXL object names, and a summary of the type of change (for example, add, update, remove) is then stored in the cache. The AXL client can then periodically retrieve the list of change summaries by calling the listChange interface which returns all of the changes in the cache.

If an application is interested in the full details of a particular change, it may be necessary to perform the corresponding <getXXX> request on the specific changed object.  For example, if a change response indicates a change type of phone and action of u the application may want to perform a <getPhone> request to ensure it has the latest, complete details for the device in question.

## Details

### Sample First Request

The first time the client calls the listChange API, AXL returns all of the change notifications in the cache. AXL clients interested in changes for a specific set of objects should always specify the objectList . Use of the objectList tailors the response and reduces the overall load on the Publisher. There is no limit to the number of objects which can be specified in the objectList . If the objectList is not specified, AXL will return the list of changes for all objects in the cache.

xml

```
< soapenv: Envelope xmlns: soapenv = " https://schemas.xmlsoap.org/soap/envelope/ " xmlns: ns = " https://www.cisco.com/AXL/API/10.0 " > < soapenv: Header /> < soapenv: Body > < ns: listChange > < objectList > < object > Phone </ object > < object > User </ object > </ objectList > </ ns: listChange > </ soapenv: Body > </ soapenv: Envelope >
```

### Sample First Response

The sample response shows AXL returned changes 1 to 10,000. The client is expected to ask for change 10,001 the next time it makes a request. Additionally, the queueID must also be submitted. queueID helps the client detect if changes may have been lost between sync intervals. Note that changes 2-10,000 are not shown in this example.

Each time a client calls listChange , the response contains two sections. The first section is called queueInfo which contains: firstChangeID , lastChangeID , nextStartChangeID , and queueID . The second section identifies the change.

xml

```
< queueInfo > < firstChangeId > 154 </ firstChangeId > < lastChangeId > 10000 </ lastChangeId > < nextStartChangeId > 10001 </ nextStartChangeId > < queueId > 093249823498 </ queueId > </ queueInfo > < changes > < change type = ' physicalLocation ' > uuid='8h58f047-7b40-4547-a8c2-fc5b2b668b7f'> < id > 1 </ id > < action > u </ action > < doGet > false </ doGet > < changedTags > < changedTag name = ' description ' > A__V3.Dx.3 w_p6. </ changedTag > </ changedTags > </ change > </ changes >
```

#### Queue Info tags

- firstChangeId The first (or oldest) change available in the cache

- lastChangeId The last (or newest) change available in the cache

- nextStartChangeId The next change record ID clients should specify in subsequent listChange requests

- queueId A unique cache identifier which changes every time the AXL service is restarted

#### Change Type tags

- changes Indicates what changed

- id The change identifier AXL assigned

- action Indicates the type change: u is update, a is add, r is remove

- doGet Boolean which indicates when the client should perform a Get operation for the object, typically because the object is new or when multiple attributes of the object were changed.

- changedTags Indicates the details of the change

#### Sample Subsequent Request

The first time the client calls the listChange API, the startChangeId is not included. However, every subsequent listChange request should include both a startChangeID and queueID . The nextStartChangeId value received in the first response should be submitted as the startChangeId in subsequent requests. Additionally, the queueId received in the first response must also be included to help the client detect if changes may have been lost between sync intervals. Anytime the AXL service is restarted, a new queueID is generated.

xml

```
< soapenv: Envelope xmlns: soapenv = " https://schemas.xmlsoap.org/soap/envelope/ " xmlns: ns = " https://www.cisco.com/AXL/API/10.0 " > < soapenv: Header /> < soapenv: Body > < ns: listChange > < startChangeId queueId = ' 093249823498 ' > 10001 </ startChangeId > < objectList > (optional) < object > Phone </ object > < object > User </ object > </ objectList > </ ns: listChange > </ soapenv: Body > </ soapenv: Envelope >
```

#### Sample Subsequent Response

The sample response shows AXL returned changes from 10,001 to 20,000 for queueID 093249823498. The client should ask for change 20,001 with the same queueID the next time it makes a request. Note that changes 10,005-20,000 are not shown in this example.

The <doGet> tag indicates when the client needs to perform a get <object> operation, typically when the object is newly added or when too many attributes for the object changed. In this example the client should perform a getPhone request for uuid='4c48f047-7b40-4547-a8c2-fc5b2b668bda'.

Note: There may be multiple results for the same object. In this example the PhysicalLocation attribute for phone with uuid='8h58f047-7b40-4547-a8c2-fc5b2b668b7f' was updated, then removed.

xml

```
< soapenv: Envelope xmlns: soapenv = " https://schemas.xmlsoap.org/soap/envelope/ " xmlns: ns = " https://www.cisco.com/AXL/API/10.0 " > < soapenv: Body > < ns: listChangeResponse > < queueInfo > < firstChangeId > 10001 </ firstChangeId > < lastChangeId > 20000 </ lastChangeId > < nextStartChangeId > 20001 </ nextStartChangeId > < queueId > 093249823498 </ queueId > </ queueInfo > < changes > < change type = ' Phone ' uuid = ' 4c48f047-7b40-4547-a8c2-fc5b2b668bda ' > < id > 10001 </ id > < action > a </ action > < doGet > true </ doGet > </ change > < change type = ' PhysicalLocation ' uuid = ' 8h58f047-7b40-4547-a8c2-fc5b2b668b7f ' > < id > 10002 </ id > < action > u </ action > < doGet > false </ doGet > < changedTags > < changedTag name = ' description ' > A__V3.Dx.3 w_p6. </ changedTag > </ changedTags > </ change > < change type = ' PhysicalLocation ' uuid = ' 8h58f047-7b40-4547-a8c2-fc5b2b668b7f ' > < id > 10003 </ id > < action > r </ action > < doGet > false </ doGet > </ change > < change type = ' Phone ' uuid = ' 8g48f047-7b40-4547-a8c2-fc5b2b668b8d ' > < id > 10004 </ id > < action > u </ action > < doGet > false </ doGet > < changedTags > < changedTag name = ' name ' > SEP00000001 </ changedTag > < changedTag name = ' description ' > A__V.x.3 w_p6. </ changedTag > < changedTag name = ' versionStamp ' > 815abf2-1c0e-4 </ changedTag > </ changedTags > </ change > </ changes > </ ns: listChangeResponse > </ soapenv: Body > </ soapenv: Envelope >
```

### Pagination Example

The client should always ask for the nextStartChangeId whether or not the request was paged, so the client doesn't really need to detect if the request was paged. If lastChangeId is greater than or equal to nextStartChangeId , then the request was paged. The client can immediately request the nextStartChangeId .

xml

```
< queueInfo > < firstChangeId > 100 </ firstChangeId > < lastChangeId > 10000 </ lastChangeId > < nextStartChangeId > 1001 </ nextStartChangeId > < queueId > 093249823498 </ queueId > </ queueInfo >
```

### Polling Interval

The new AXL CNF has no restrictions on polling intervals. Requests are still subject to existing AXL throttles which limit each response to 8MB and all concurrent responses to 16MB.

The change queue cache is stored in memory and is limited to 100,000 changes. The cache can fill quickly depending on the types of changes performed. For example, if an XSI (IP Phone) Service has been configured for 10,000 phones and the service is deleted, the cache will include one entry representing the deletion of the service plus 10,000 phone updates indicating the service was removed from each device.

For a typical cluster, Cisco recommends AXL clients request listChange every 1-15 minutes. On a very busy system, AXL clients should request changes often (between 1-5 minutes) to ensure all changes are communicated while still in the cache. If the client waits too long and the changeID requested is no longer in the queue, AXL will return an error.

### Error Conditions

listChange requests which fail will return a HTTP 500 Internal Server Error status code response, along with an explanatory <faultstring> element.  See the example below of an error response where an invalid queueId was provided:

xml

```
HTTP/1.1 500 Internal Server Error
Content-Type: text/xml;charset=UTF-8 <?xml version="1.0" encoding="UTF-8"?> < soapenv: Envelope xmlns: soapenv = " https://schemas.xmlsoap.org/soap/envelope/ " xmlns: ns = " https://www.cisco.com/AXL/API/11.5 " > < soapenv: Body > < soapenv: Fault > < faultcode > soapenv:Server </ faultcode > < faultstring > The queueId value does not match the server. This indicates that it is either incorrect or the server restarted and a full sync is needed. </ faultstring > < detail > < ns2: axlError xmlns: ns2 = " https://www.cisco.com/AXL/API/11.5 " > < axlcode > 5007 </ axlcode > < axlmessage > The queueId value does not match the server. This indicates that it is either incorrect or the server restarted and a full sync is needed. </ axlmessage > < request > listChange </ request > </ ns2: axlError > </ detail > </ soapenv: Fault > </ soapenv: Body > </ soapenv: Envelope >
```

# User Rank Interactions

## Overview

Cisco Unified CM can be configured by the administrator to control the ability of users, including AXL API users, to access or update certain CUCM data, via the User Rank feature.  The administrator may create and assign User Rank values to individual end-users, application-users, or user-groups, then restrict only certain User Ranks from updating specific CUCM data types.  These User Ranks can be created and assigned with values ranging from 1-10, with 1 being the 'default' rank which has the highest level of access.

Note: User Rank is a feature that first appears in CUCM v11.5(1)SU1.  More details can be found in the Documentation Supplement for Cisco Unified Communications Manager and IM and Presence Service, Release 11.5(1)SU1 and System Configuration Guide for Cisco Unified Communications Manager for releases later than v11.5(1).

The CUCM user account used by an application to authenticate to AXL is also subject to the access control restrictions of the User Rank feature, which may affect certain types of AXL requests.

## Interaction Scenarios

If the administrator has configured a User Rank for the AXL user that is higher than 1 (non-default), for example a Rank of 2-10, keep in mind the following possible interactions when performing operations on the controlled object types of End Users, Application Users, User Groups, and LDAP Directories:

- Add requests will result in the new object having the same User Rank as the AXL user.

- Remove requests will fail if the User Rank of the AXL user is greater than the User Rank of the target object.

- Update requests which attempt to modify the User Group(s) associated to an object will fail if the User Rank of the AXL user is greater than the User Rank of the target object.

- executeSqlUpdate operations which attempt to modify database fields related to User Rank, or User Group Association, are only allowed if the AXL User Rank is 1, the 'default' value.

## Compatibility Notes

Upon upgrade to v11.5(1)SU1, User Rank of all objects and users will default to 1, which means no restrictions due to the User Rank Feature will occur.  This should mean all AXL users and applications will be unaffected by the User Rank feature unless the CUCM administrator intentionally increases the User Rank of the AXL user or target controlled objects.

However, as of CUCM v11.5(1)SU1, User Rank is not exposed by any requests or elements in the AXL schema. Exposing User Rank is planned for a later release.  As a result, applications may have difficulty ascertaining the User Rank of the AXL user itself or the User Rank of objects on which operations are to be performed, making it hard to avoid attempting restricted operations.  Applications should be prepared to sanely handle requests which fail due to User Rank restrictions, see Error Messages .

Note, it is possible to read the User Rank value of controlled objects via SQL, using the executeSqlQuery request.  See the Cisco Unified Communications Manager Data Dictionary for details on the tables and fields of the CUCM configuration database.

## Error Messages

Requests which fail due to User Rank access restrictions will return a HTTP 500 Internal Server Error status code response with an explanatory <faultstring> element.  See the example on the right of a error response where an AXL user having a User Rank of 3 attempts a <removeUser> operation on an end user having User Rank of 1:

xml

```
HTTP/1.1 500 Internal Server Error
Content-Type: text/xml;charset=UTF-8 < soapenv: Envelope xmlns: soapenv = " https://schemas.xmlsoap.org/soap/envelope/ " > < soapenv: Body > < soapenv: Fault > < faultcode > soapenv:Server </ faultcode > < faultstring > You do not have the privilege to remove this End User as you have lower User Rank </ faultstring > < detail > < axlError > < axlcode > 5003 </ axlcode > < axlmessage > You do not have the privilege to remove this End User as you have lower User Rank </ axlmessage > < request > removeUser </ request > </ axlError > </ detail > </ soapenv: Fault > </ soapenv: Body > </ soapenv: Envelope >
```

Next

| API | Changed Tags | Added Tags |
|---|---|---|
| getTransportSettings |  | proxyAuthenticationEnabled - proxyUserName - proxyPassword |
| doUpdateTransportSettings |  | enableProxyAuthentication - proxyUserName - proxyPassword |
| addUserProfileProvision |  | allowPhoneReassign |
| getUserProfileProvision |  | allowPhoneReassign |
| updateUserProfileProvision |  | allowPhoneReassign |
| listUserProfileProvision |  | allowPhoneReassign |
| listUser |  | customerName |
| addUser |  | associatedHeadsets |
| updateUser |  | associatedHeadsets - addAssociatedHeadsets - removeAssociatedHeadsets |
| getUser |  | associatedHeadsets |

| API | Operation | Added Tags |
|---|---|---|
| ExpresswayCConfiguration | Add Get List Update Remove | HostNameOrIP description X509SubjectNameorSubjectAlternateName |
| Customer | Add Get List Update Remove | name createTime lastAuditTime |
| PhoneActivationCode | Add List Remove | activationCode activationCodeExpiry phoneName phoneDescription phoneModel enableActivationId userId |
| DeviceDefaults | Get List Update | Model Protocol LoadInformation InactiveLoadInformation DevicePoolName PhoneButtonTemplate VersionStamp PreferActCodeOverAutoReg |
| MraServiceDomain | Add Get List Update Remove | name isDefault serviceDomains |
| CiscoCloudOnboarding | List Update | voucherExists enablePushNotifications enableHttpProxy httpProxyAddress proxyUsername proxyPassword enableTrustCACertificate allowAnalyticsCollection enableTroubleshooting alarmSendEncryptedData orgId alarmPushIntervalSecs alarmEncryptKey serviceAddress onboardingRegistrationStatus email partnerEmail orgName customerOneTimePassword alarmSeverity alarmPushNowToggle enableGDSCommunication mraActivationDomain errorStatus |

| API | Changed Tags | Added Tags |
|---|---|---|
| SipProfile |  | externalPresentationInfo - isAnonymous - presentationInfo externalPresentationNumber externalPresentationName |
| CallManager |  | ports/sipPorts - sipOAuthPort - sipOAuthMRAPort |
| DevicePool |  | mraServiceDomain |
| User | Removed from listUserRes presenceGroupName selfService ldapDirectoryName enableUserToHostConferenceNow attendeesAccessCode | customerName |
| ApplicationUserCapfProfile | keySize default value changed |  |
| EndUserCapfProfile | keySize default value changed |  |
| PhoneSecurityProfile |  | EnableOAuthAuthentication |
| Line |  | callingIdPresentationWhenDiverted externalPresentationInfo - isAnonymous - presentationInfo externalPresentationNumber externalPresentationName |
| Phone | ecKeySize default value removed | enableActivationID activationIDStatus mraServiceDomain allowMraMode |
| AudioCodecPreferenceList | codecNames maxOccurs changed to 31 |  |
| SipTrunk | Removed from listSipTrunkRes presenceGroupName | externalPresentationInfo - isAnonymous - presentationInfo externalPresentationNumber externalPresentationName useOrigCallingPartyPresOnDivert |
| ServiceProfile |  | jabberClientConfigurationProfileInfo |
| UserProfileProvision |  | allowProvisionEMMaxLoginTime |
| LicensedUser | Removed from listLicensedUserRes emEnabled |  |

| API | Operation |
|---|---|
| VG224 | resetVG224 restartVG224 |
| Gateway | retartGateway |
| EnterpriseParameters | applyEnterpriseParameters resetEnterpriseParameters restartEnterpriseParameters |
| UcService | applyUcService resetUcService restartUcService |
| SmartLicensing | doSmartLicenseRegister doSmartLicenseReRegister doSmartLicenseDeRegister |

| API | Operation | Added Tags |
|---|---|---|
| User | get list add update | ipccRoutePartition Removed tags accountType authenticationType |
| Srst | get list add update | ipv6Address |
| PhoneNtp | get list add update | ipv6Address |
| UserProfileProvision | get add update | enableMra mraPolicy_Desktop mraPolicy_Mobile |
| UniversalLineTemplate | get add update | noAnswerRingDuration |
| RemoteDestination | get | ctiRemoteDeviceLineAssociations - pattern - routePartitionName - uuid - index |
| SipProfile | get add update | allowRRAndRSBandwidthModifier |
| SipTrunk | get add update | service parameterLabel originatingParameterValue terminatingParameterValue outboundUriRoutingInstructions |
| H323Trunk | get add update | rdnTransformationCssName useDevicePoolRdnTransformCss |
| GatewayEndpointDigitalAccessBri | get add update | unattendedPort enableDatalinkOnFirstCall |
| GatewayEndpointDigitalAccessT1 | get add update | calledPartyUnknownPrefix calledPartyUnknownStripDigits calledPartyUnknownTransformationCssName useDevicePoolCalledCssUnkn |

| API | Operation | Added Tags |
|---|---|---|
| EnterpriseParameters | doEnterpriseParametersReset |  |
| ServiceParameters | doServiceParametersReset | processNodeName service |
| InfrastructureDevice | add update get list remove | name ipv4Address bssidWithMask wapLocation isActive |
| RegistrationDynamic | get list | device lastKnownIpAddress lastKnownUcm lastKnownConfigVersion locationDetails endpointConnection portOrSsid lastSeen |
| WirelessAccessPointControllers | add update get list remove | name description snmpVersion snmpUserIdOrCommunityString snmpAuthenticationProtocol snmpAuthenticationPassword snmpPrivacyProtocol snmpPrivacyPassword syncNow resyncInterval nextSyncTime scheduleUnit |
| LdapSearch | update get | enableDirectorySearch distinguishedName password userSearchBase1 userSearchBase2 userSearchBase3 ldapFilterForUser enableRecursiveSearch primary seconday tertiary |

| API | Operation | Added Tags |
|---|---|---|
| SipProfile | add update get | connectCallBeforePlayingAnnouncement faxInvite enableExternalQoS |
| MohAudioSource | update get | isExternalSource |
| CredentialPolicy | add update get list | minCharsToChange |
| User | add update get | pwdResetHackCount zeroHop |
| H323Trunk | add update get | connectCallBeforePlayingAnnouncement |
| H323Gateway | add update get | connectCallBeforePlayingAnnouncement |
| UniversalDeviceTemplate | add update get | certificateOperation |
| HttpProfile | add update get | username password requestTimeout retryCount |
| IlsConfig | update | enableUsePassword |
| LocalRouteGroup | update | uuid |
| PhoneButtonTemplate | get | isFixedFeature |
| PhoneTypeDisplayInstance | get | trunkType |

| API | Operation | Added Tags |
|---|---|---|
| LicensedUser | list | userId firstName lastName snrEnabled deviceCount licenseType licenseUsed |
| UnassignedDevice | list | name description deviceType licenseType extension |
| UpdateLicenseUsage | doUpdateLicenseUsage |  |
| HttpProfile | add update get remove | name uuid webServiceRootUri |
| InteractiveVoiceResponse | update get list | name uuid description devicePoolName locationName useTrustedRelayPoint serverName |
| ConferenceNow | add update get list remove | uuid conferenceNowNumber routePartitionName description maxWaitTimeForHost MohAudioSourceId |
| ElinGroup | add update get list remove | name uuid description elinNumbers - elinNumber -- pattern -- partition |
| SecureConfig | update get | name uuid value |

| API | Operation | Added Tags |
|---|---|---|
| ConferenceBridge | add update get | allowCFBControlOfCallSecurityIcon |
| RemoteDestination | add update get | ringSchedule - member/ -- startTime -- endTime -- startDay -- endDay -- accessListName |
| SipProfile | add update get | startVideoPort stopVideoPort dscpForAudioCalls dscpForVideoCalls dscpForAudioPortionOfVideoCalls dscpForTelePresenceCalls dscpForAudioPortionOfTelePresenceCalls |
| User | add update get | enableUserToHostConferenceNow attendeesAccessCode |
| FeatureGroupTemplate | add update get | enableUserToHostConferenceNow |
| DevicePool | add update get | elinGroup |
| Phone | add update get | elinGroup |
| H323Phone | add update get | elinGroup |
| GatewayEndpointAnalogAccess | add update get | elinGroup |
| TransPattern | add update get | isEmergencyServiceNumber |
| RoutePattern | add update get | isEmergencyServiceNumber |
| LdapDirectory | add update get | synchronize ldapFilterForGroups |
| ApplicationUserCapfProfile | add update get list | keyOrder ecKeySize |
| EndUserCapfProfile | add update get list | keyOrder ecKeySize |
| PhoneSecurityProfile | add update get list | keyOrder ecKeySize |
| UniversalDeviceTemplate | add update get list | keyOrder ecKeySize |

| API | Operation | Added Tags |
|---|---|---|
| LicensedUser | get | name uuid returnedTags |

| API | Changed Tags | added Tags |
|---|---|---|
| SipProfile | earlyOfferSupportForVoiceCall | earlyOfferSuppVoiceCall |

| Version String | 15.0 | 14.0 | 12.5 | 12.0 | 11.5 | 11.0 | 10.0 | 9.1 | 9.0 | 1.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| CUCM 15 | 15 schema applied | 14 schema applied | 12.5(1) schema applied 1 | 12.0 schema applied |  |  |  |  |  | 12.0 schema applied |
| CUCM 14 |  | 14 schema applied | 12.5(1) schema applied 1 | 12.0 schema applied | 11.5(1) schema applied 1 | 11.0 schema applied |  |  |  | 11.0 schema applied |
| CUCM 12.5(1) |  |  | 12.5(1) schema applied 1 | 12.0 schema applied | 11.5(1) schema applied 1 | 11.0 schema applied | 10.0 schema applied |  |  | 10.0 schema applied |
| CUCM 12.0(1) |  |  |  | 12.0 schema applied | 11.5(1) schema applied 1 | 11.0 schema applied | 10.0 schema applied |  |  | 10.0 schema applied |
| CUCM 11.5(1) |  |  |  |  | 11.5(1) schema applied 1 | 11.0 schema applied | 10.0 schema applied | 9.1 schema applied | 9.0 schema applied | 9.0 schema applied |
| CUCM 11.0(1) |  |  |  |  |  | 11.0 schema applied | 10.0 schema applied | 9.1 schema applied | 9.0 schema applied | 9.0 schema applied |
| CUCM 10.5(1) |  |  |  |  |  |  | 10.0 schema applied | 9.1 schema applied | 9.0 schema applied | 8.0 schema applied |
| CUCM 10.0(1) |  |  |  |  |  |  | 10.0 schema applied | 9.1 schema applied | 9.0 schema applied | 8.0 schema applied |
| CUCM 9.1(1) |  |  |  |  |  |  |  | 9.1 schema applied | 9.0 schema applied | 7.1 schema applied |
| CUCM 9.0(1) |  |  |  |  |  |  |  |  | 9.0 schema applied | 7.1 schema applied |

## Figuras

![Downlaod Certificate](https://pubhub.devnetcloud.com/media/axl/docs/axl-developer-guide/images/certificate_download.png#developer.cisco.com)