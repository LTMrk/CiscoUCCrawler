---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-hcs-12-5-hcs-solution-operation-guide-chcs-b-hcs-smart-licensing-operational-25daf7711b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/hcs/12_5/HCS_Solution/Operation_Guide/chcs_b_hcs-smart-licensing-operational-guide/chcs_b_hcs-smart-licensing-operational-guide_chapter_0101.html
retrieved_at: 2026-09-01T20:56:22.696852+00:00
---

Cisco Hosted Collaboration Solution Smart Licensing Operation Guide, Release 12.5

# Cisco Hosted Collaboration Solution Smart Licensing Operation Guide, Release 12.5

Updated: April 23, 2020

Chapter: Troubleshooting Smart Licensing

## Chapter: Troubleshooting Smart Licensing

- Troubleshooting Smart Licensing

- Troubleshooting Smart Licensing

- Smart Licensing Error Code and Message Mapping

# Troubleshooting Smart Licensing

## Troubleshooting Smart Licensing

The HCM-F Smart Licensing operations like Smart Account Sync, Cluster Assignment/Unassignment creates jobs, that can be viewed
                              In HCM-F GUI under Infrastructure Manager > Administration > Jobs .

In case of failure, the Job Staus Info column shows the error codes with the corresponding messages and recommendations as listed the following table.

### CSSM API Errors

Error Code

Error Message

Recommendation

CSSM1001

CSSM API encountered an Unknown Error

Check HLM Logs (Detailed) for more details

CSSM1002

Unsupported HTTP Method

Check HLM Logs (Detailed) for more details

CSSM1003

CSSM API encountered an Internal Error

Check HLM Logs (Detailed) for more details

CSSM1004

CSSM API is unable to send request

Check HLM Logs (Detailed) for more details

CSSM1005

CSSM Server refused connection

If Proxy is configured, verify network connectivity between HCM-F and Proxy Server

CSSM1006

CSSM API Unknown Host Error

If Proxy is configured, verify Proxy hostname is correct and DNS resolution of CSSM/Proxy/Authentication GW(Transport Mode
                                          Setting)

CSSM1007

CSSM API Socket Timeout Error

If Proxy is configured, verify network connectivity between HCM-F and Proxy Server

CSSM1008

CSSM API No Route To Host Error

If Proxy is configured, verify network connectivity between HCM-F and Proxy Server

CSSM1009

CSSM client creation failed due to invalid Transport Mode

Check HLM Logs (Detailed) for more details

CSSM1010

CSSM client creation failed due to Unknown Error

Check HLM Logs (Detailed) for more details

CSSM1011

CSSM API Authentication Failed Error

Reconfigure client ID and Secret, and perform Smart Account Sync

CSSM1012

CSSM client unable to parse the response

Check HLM Logs (Detailed) for more details

CSSM1013

CSSM client unable to map JSON response

Check HLM Logs (Detailed) for more details

CSSM1014

CSSM client unable to read response due to IO error

Check HLM Logs (Detailed) for more details

CSSM1015

Client credentials may not have access to Smart Account or Domain Name is incorrect

Check if the Client Id and Secret have access to Smart Account and the Domain name is Correct

CSSM1016

CSSM client unable to process response

Check HLM Logs (Detailed) for more details

CSSM1017

CSSM client unable to process JSON response

Check HLM Logs (Detailed) for more details

CSSM1018

CSSM client config validation failed

Check HLM Logs (Detailed) for more details

CSSM1019

Given Smart Account ID does not exist

Check HLM Logs (Detailed) for more details

CSSM1020

CSSM server responded with errors

Check HLM Logs (Detailed) for more details

### Cisco Application Adaptor (CAA) Errors

Error Code

Error Message

Recommendation

CAA1001

Service encountered an unknown error

Verify App specific adapter Service is running Scan CAA logs for errors and restart service if necessary.

CAA1002

Service encountered an SDR error

Verify Cisco CDM Database is running Scan App specific adapter logs for errors.

CAA1003

CAA is unable to find application instance in SDR

Verify Application is configured Scan CAA logs for errors.

CAA1004

No admin credentials configured for application

Verify admin credentials are configured.

CAA1005

CAA does not support this equipment type

Scan CAA logs for errors.

CAA1006

CAA is unable to read the application name from SDR

Verify Cisco CDM Database is running Scan CAA logs for errors.

CAA1007

No service provider address configured for application

Verify service provider address is configured for the application.

CAA1008

No platform credentials configured for the application

Verify if platform credentials are configured.

CAA1009

No Cluster version configured for the application

Verify if cluster version is configured.

CAA1010

No Request Hanlder Mapping found in json

Verify if request handler exist for message type app type and cluster version.

CAA1011

Error occurred in SSH connection

Check if app details platform credentials are correct and session timeout is sufficient.

CAA1012

Invalid Response type provided

Check response type.

CAA1014

Unable to generate CSR for the given certificate type Provide correct certificate type

Check logs for more details.

CAA1015

Certificate import failed due to CSR public key and Certificate public key doesn't match

Verify whether the certificate and CSR has the same algorithm and key.

CAA1016

Certificate import failed due to CSR SAN and Certificate SAN doesn't match

Verify CSR SAN and Certificate SAN.

CAA1017

Error occurred as CSR does not exist in the App

Generate CSR before proceeding with this action.

CAA1018

CA certificate is not available in the trust-store

Upload a CA certificate in trust store.

CAA1019

Error in CA certificate

Upload a CA certificate in trust store.

CAA1020

Error occurred while reading the certificate

Provide a valid CA Certificate.

CAA1021

Certificate is not in PEM format

Provide a valid Certificate.

CAA1022

Invalid certificate file provided

Provide a valid Certificate.

CAA1023

Error occurred as CSR does not exist in the App

Generate CSR before proceeding with this action.

CAA1024

Error occured as CLI Response Parser is not configured

Configure Parser for CLI command.

CAA1025

Invalid certificate type found

Check if the certificate type is valid.

CAA1026

Certificate Upload failed

Check if the certificate is valid and UC App is provisioned with right version Refer logs for more details.

CAA1027

Certificate operation is not successful Internal error occurred

Check the logs for more details.

CAA1028

Failed to get the REST API client

Verify application is running the supported version.

CAA1029

Error occurred during REST API call to Expressway

Verify credentials are correct and REST service is up on Expressway.

CAA1030

Current version of Expressway is not supported

Use the supported versions of Expressway.

CAA1031

Error occurred as invalid certificate was

Uploaded to Expressway. Verify the CA certificate is available in the trust and uploaded CA signed certificate is valid.

CAA1032

Error occurred as CSR already exist in Expressway

Delete the existing CSR.

CAA1033

Error occurred in CSR generation in Expressway as invalid data was passed fo CSR

Verify the data provided to generate CSR.

CAA1034

No Response Hanlder Mapping found in json

Verify if response handler exist for message type app type and cluster version.

CAA1035

Invalid admin credentials

Verify the user name and password.

CAA1036

CAA encountered an unknown error from the application

Verify the following entities - Cisco AXL Web Service (Cisco
                                          Unified CM) is active Publisher Admin/Platform credentials and
                                          Network address HCMF) are correct.

CAA1037

CAA encountered error while parsing xml

Make sure the UCApps are returning proper responses.

CAA1038

CAA is unable to determine the application Version

Verify Cisco AXL Web Service Cisco Unified CM) is running on
                                          application. Verify application admin credentials and network
                                          address.

CAA1039

API executed by non admin user

Verify the user name and password for admin credentials.

CAA1040

Invalid Proxy details

Verify the Proxy Hostname and Proxy port configured in Transport Mode Setting.

CAA1041

Edit Transport Settings operation is not allowed since product is in Registered state

Sync Smart Account with CSSM and assign cluster to Virtual Account.

CAA1042

Product may already deregistered

Sync Smart Account with with CSSM.

CAA1043

Internal Error occurred while communicating with Unity Connection

Verify the Cisco Smart License Manager and Tomcat service is running in Unity Connection.

CAA1044

Unsupported message received by CAA service

Scan CAA logs for errors.

CAA1045

CAA does not support the application version

Verify if correct cluster version is configured in HCMF.

CAA1046

CAA cannot connect to application

Verify Cisco AXL Web Service is running on Cisco Unified CM
                                          application Publisher's admin/platform credentials and network
                                          address are correct and network connectivity from HCM-F is
                                          established.

CAA1048

Product Registration Token is either invalid or has been expired

Perform Smart Account Sync with CSSM.

CAA1049

Product is in subscriber Node

CAA1050

Exception occurred while performing product operation

Scan CAA logs for errors.

CAA1051

CAA is unable to add community string on application

Verify application admin credentials and network address are correct. Verify community string does not already exist.

CAA1052

CAA is unable to update community string on application

Verify application admin credentials and network address. Verify community string is present.

CAA1053

CAA is unable to delete community string on application

Verify application admin credentials and network address. Verify community string exists.

CAA1054

CAA is unable to add SNMP V3 user on application

Verify application admin credentials and network address. Verify SNMP V3 user does not already exist.

CAA1055

CAA is unable to update SNMP V3 user on application

Verify application admin credentials and network address. Verify SNMP V3 user exists.

CAA1056

CAA is unable to delete SNMP V3 user on application

Verify application admin credentials and network address. Verify SNMP V3 user is present.

CAA1057

CAA is unable to restart application SNMP Master Agent

Verify network connection between HCM-F and application. Verify application platform credentials and network address.

CAA1058

CAA is unable to add Remote Syslog configuration on application

Verify application admin credentials and network address.

CAA1059

CAA is unable to update Remote Syslog configuration on application

Verify application admin credentials and network address.

CAA1060

CAA is unable to add Billing Application Server configuration on application

Verify SFTP Credentials and the directory /home/smuser/ exists on billing server. Verify network connection between application
                                          and billing server.

CAA1061

CAA is unable to update Billing Application Server configuration on application

Verify SFTP Credentials and the directory /home/smuser/ exists on billing server. Verify network connection between application
                                          and billing server.

CAA1062

CAA is unable to remove Billing Application Server configuration on application

Verify application ADMIN credentials and network address. Verify BAS config exists on application.

CAA1063

CAA cannot connect to application platform CLI

Verify platform credentials are configured and network connectivity between HCM-F and application.

CAA1064

CAA is unable to restart application Host Resources Agent

Verify network connection between HCM-F and application. Verify application platform credentials and network address.

CAA1065

Unsupported message received from CAA

Scan CAA logs for errors.

CAA1066

No CUOM is configured for application

Verify CUOM is configured for the application.

CAA1067

No service provider address is configured for CUOM

Verify service provider address is configured for CUOM.

CAA1068

Unable to get process node list from Cisco Unified CM

Verify name in Cisco Unified CM System > Server) matches the
                                          hostname or IP configured in HCM-F for Service Provider or
                                          Application Space Address.

CAA1069

No HTTP credentials configured for application

Verify if HTTP credentials are configured.

CAA1070

No SFTP credentials configured

Verify if SFTP credentials are configured for billing application server.

CAA1071

No SFTP network address configured

Verify if SFTP network address is configured for billing application server.

CAA1072

CAA is unable to find the specified phone device on the application

Verify phone device exists on application.

CAA1073

CAA is unable to find the specified user on the application

Verify end user exists in the application.

CAA1074

Failed to get the web-security details from the UC App

Verify if the web-security data is available on the UC App.

CAA1075

Error occured during RIS call

Check if RIS service is up.

CAA1076

Error occured during CCS call

Check if CC service is up.

CAA1077

Error occurred during PAWS call

Check if PAWS service is up.

CAA1078

Error occurred during command execution on CLI

Verify if the command syntax is correct.

CAA1079

Set Transport Mode failed due Invalid format of on-prem Registration url

Please provide the valid on-prem url.

CAA1080

No Clustering Configuration Found in Expressway

Configure proper clustering Expressway.

CAA1081

Registration with Smart Agent failed

Verify the Proxy connection and the Cisco Unified CM
                                          connectivity with CSSM. Check  CAA/HLM Logs for more
                                          details.

CAA1082

DeRegistration with Smart Agent failed

Verify the Proxy connection and the Cisco Unified CM
                                          connectivity with CSSM or the product is already unregistered
                                          with CSSM. Check CAA/HLM Logs for more details.

CAA1083

Update transport settings failed

Verify the Proxy connection and the Cisco Unified CM
                                          connectivity with CSSM or the product is already registered with
                                          CSSM. Check CAA/HLM Logs for more details.

CAA1084

Error occurred in SSH connection

Check if platform credentials are correct and session timeout is sufficient.

### Smart Licensing Cluster Operation Errors

Error Code

Error Message

Recommendation

SLMCT1001

Virtual Account is not valid

Check if the given Virtual Account is correct

SLMCT1002

Exception occurred while License Mode change

Check if UC application is up and its platform service is running. Check HLM Logs for more details

SLMCT1003

Cluster License Mode did not change successfully

Check HLM Logs for more details

SLMCT1004

Cluster License Mode Change - JMS timeout occurred

Check if Provisioning Adapter Service is up. Check Logs for more details

SLMCT1005

Cluster License Mode Change - JMS timeout occurred

Check if CAA Service is up. Check Logs for more details

SLMCT1006

Cluster is of unsupported Version

Provide a valid cluster

SLMCT1007

Cluster is already assigned

Perform Smart Account sync with CSSM

SLMCT1008

Cluster doesn't have an application

Assign an application to the Cluster

SLMCT1011

Cluster is already unassigned

Perform Smart Account Sync with CSSM

SLMCT1012

Cluster doesn't have publisher node

Assign a publisher node to cluster

SLMCT1013

Cluster application doesn't have platform credentials

Configure platform credentials for cluster application

SLMCT1014

Cluster application doesn't have admin credentials

Configure admin credentials for cluster application

SLMCT1015

Cluste is of unsupported Type

Supported cluster type are Cisco Unified CM, Cisco Unity
                                          Connection and Cisco Emergency Responder

SLMCT1016

Reset Cluster License Mode - did not change successfully

Check HLM Logs for more details

SLMCT1017

Exception occurred while Reset Cluster License Mode

Check if UC Application is up and its platform service is
                                          running. Check HLM Logs for more details

SLMCT1018

Cluster License Mode Change - JMS timeout occurred

Check if Provisioning Adapter Service is up. Check Logs for more details

SLMCT1019

Cluster License Mode Change - JMS timeout occurred

Check if CAA Service is Up. Check Logs for more details

### Smart Licensing General Errors

Error Code

Error Message

Recommendation

SLM1001

Smart Licensing Product Registration request failed due to exception

Check HLM Logs (Detailed) for more details

SLM1002

Smart Licensing Product Registration failed due to JMS timeout

Check if the CAA CUCM Service is started

SLM1003

Smart Licensing Get Transport Mode request failed due to exception

Check HLM Logs (Detailed) for more details

SLM1005

Smart Licensing Update Transport Mode request failed due to exception

Check if the UCapp and its services are up. Check logs for exception details

SLM1007

Smart Licensing Cluster Operation - Cluster does't have admin credentials

Check if admin credentials are configured for cluster application

SLM1008

Smart Licensing Cluster Operation - Cluster does't have platform credentials

Check if platform credentials are configured for cluster application

SLM1009

Smart Licensing Cluster Operation - Cluster don't have a publisher node

Check if cluster has publisher node

SLM1010

Smart Licensing Get Product Token - Unable to generate or retrieve product token for the Virtual Account

Check HLM Logs (Detailed) for more details

SLM1011

Smart Licensing Product DeRegistration failed due to JMS timeout

Check if the CAA CUCM Service is started

SLM1012

Smart Licensing Change License Mode - Cluster HostName/IP is not configured

Check if publisher network address is configured

SLM1013

Smart Licensing Change License Mode request failed while get/update transport mode due to exception

Check UCapps platform service is up or Publishers IP/Hostname and platform credentials are valid

SLM1014

Smart Licensing Change License Mode - Virtual Account is not associated with any License Mode

Check if Virtual Account is associated with License Mode

SLM1015

Smart Licensing Sync - an unknown error occured

Check HLM Logs (Detailed) for more details

SLM1016

Smart Licensing Sync - unable to fetch Smart Account details from SDR

Verify Cisco CDM Database is running. Check HLM Logs (Detailed) for more details

SLM1018

Smart Licensing Change Transport Mode failed due to JMS timeout

Check if the CAA CUCM Adapter is started.

SLM1021

Smart Licensing Product DeRegistration failed due to JMS timeout

Check if the CAA CER Service is started

SLM1023

Smart Licensing Change Transport Mode failed due to JMS timeout

Check if the CAA CER Adapter is started

SLM1024

Smart Licensing Change Transport Mode failed due to JMS timeout

Check if the CAA CUCXN Adapter is started

SLM1025

Smart Licensing Request Failed due to Invalid Cluster Exception

Check HLM Logs (Detailed) for more details

### UC Applications API Errors

Error Code

Error Message

Recommendation

UCAPI1001

Updating Cisco Unified CM Billing Server info failed

N/A

UCAPI1002

Updating Cisco Unified CM Remote Syslog info failed

N/A

UCAPI1003

Updating Cisco Unified CM SNMP info failed

N/A

UCAPI1004

Validation of Cisco Unified CM AXL Connection failed

Check AXL services and Platform services are up in Cisco Unified
                                          CM

UCAPI1005

Accessing Cisco Unified CM AXL SOAP Port failed

Check AXL services and Platform services are up in Cisco Unified
                                          CM

UCAPI1006

Initialization failed

N/A

UCAPI1007

Software Error

N/A

UCAPI1008

Unknown Failure

N/A

UCAPI1009

Connection Timeout

N/A

UCAPI1010

Registration with Smart Agent failed

Verify the Proxy connection and the Cisco Unified CM connectivity
                                          with CSSM. Check CAA/HLM Logs for more details.

UCAPI1011

DeRegistration with Smart Agent failed

Verify the Proxy connection and the Cisco Unified CM connectivity
                                          with CSSM or the product is already unregistered with CSSM.
                                          Check CAA/HLM Logs for more details.

UCAPI1012

Update transport settings failed

Verify the Proxy connection and the Cisco Unified CM connectivity
                                          with CSSM or the product is already unregistered with CSSM.
                                          Check CAA/HLM Logs for more details.

## Smart Licensing Error Code and Message Mapping

REST API

Response

Code

Message

Recommended Action

transportsettings

405

METHOD_NOT_ALLOWED

Edit Transport Settings operation is not allowed since product is in either Registered state or is a Subscriber node

Derigister your product instance and run it from correct node (Publisher only)

transportsettings

500

INTERNAL_SERVER_ERROR

Failed to apply the Transport Settings

Try to run command again with correct information and privilege. If this issue persists, please contact Cisco Technical Support

transportsettings

400

INVALID_PARAMETER

Please enter a valid Transport Mode within the range (0 - 2)

400

INVALID_PARAMETER

Please enter a valid Transport Gateway URL

400

INVALID_PARAMETER

Please provide valid HTTP/HTTPS Proxy IP Address and/or HTTP/HTTPS Proxy Port

400

INVALID_PARAMETER

Please enter a valid HTTP/HTTPS Proxy IP Address

400

INVALID_PARAMETER

Please enter a valid HTTP/HTTPS Proxy Port within the range (1 - 65535)

deregister

405

METHOD_NOT_ALLOWED

Deregistration is not allowed since product is in either unregistered state or is a Subscriber node

Check License status and Node information and take action accordingly

deregister

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to an unknown error

Check Register status, if its deregister, remove product instance manually from CSSM.

EvtSlmCucDeregistrationFailure

SmartLicensingDeregistrationFailure

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to invalid trust chain pool

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to a communication timeout.

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to communication send error

register

400

INVALID_PARAMETER

The Product Instance Registration Token you have entered is either invalid or has been expired. Ensure that you have pasted
                                          the entire token and that the token has not expired

EvtSlmCucRegistrationFailure

SmartLicensingRegistrationFailure

register

405

METHOD_NOT_ALLOWED

Smart Software Licensing operations are not allowed from Subscriber, licenses for this system are managed by Publisher

405

METHOD_NOT_ALLOWED

Product is already registered on CSSM. To Re-register it use 'force' flag

register

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to an unknown error

Check the network connectivity with CSSM. For further troubleshooting, check the CuSlmSvr diagnostic logs. Retry Product Registration.
                                          If this issue persists, contact Cisco Technical Support.

EvtSlmCucRegistrationFailure

SmartLicensingRegistrationFailure

500

INTERNAL_SERVER_ERROR

The Product Instance was unable to register with Smart Software Licensing

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to invalid trust chain pool

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to a communication timeout.

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to communication send error

500

INTERNAL_SERVER_ERROR

Smart License Server is not running. Start Smart License Manager Server from CUCA Serviceability Page

renewID

405

METHOD_NOT_ALLOWED

Renewal of ID is not allowed since product is in either unregistered state or is a Subscriber node

renewID

500

INTERNAL_SERVER_ERROR

Smart License Server is not running. Start Smart License Manager Server from CUCA Serviceability Page

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to a communication timeout

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to an unknown error

Check the network connectivity with CSSM. For further troubleshooting, check the CuSlmSvr diagnostic logs. Retry Renew Registration.
                                          If this issue persists, contact Cisco Technical Support.

EvtSlmCucRenewRegistrationFailure

SmartLicensingRenewRegistrationFailure

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to invalid trust chain pool

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to communication send error

renewAuth

405

METHOD_NOT_ALLOWED

Renewal of Authorization is not allowed since product is in either unregistered state or is a Subscriber node

renewAuth

500

INTERNAL_SERVER_ERROR

Smart License Server is not running. Start Smart License Manager Server from CUCA Serviceability Page

Check the network connectivity with CSSM. For further troubleshooting, check the CuSlmSvr diagnostic logs. Retry Renew Authorization.
                                          If this issue persists, contact Cisco Technical Support.

EvtSlmCucRenewAuthFailure

SmartLicensingRenewAuthFailure

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to a communication timeout

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to an unknown error

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to invalid trust chain pool

500

INTERNAL_SERVER_ERROR

The requested operation was not successful due to communication send error

licensedetails

500

INTERNAL_SERVER_ERROR

Unable to fetch license count from database

All APIs

401

NOT_AUTHORIZED

User is not authorized to perform this operation

Use correct priviledge to run commands

AuthenticationFailed

| Error Code | Error Message | Recommendation |
|---|---|---|
| CSSM1001 | CSSM API encountered an Unknown Error | Check HLM Logs (Detailed) for more details |
| CSSM1002 | Unsupported HTTP Method | Check HLM Logs (Detailed) for more details |
| CSSM1003 | CSSM API encountered an Internal Error | Check HLM Logs (Detailed) for more details |
| CSSM1004 | CSSM API is unable to send request | Check HLM Logs (Detailed) for more details |
| CSSM1005 | CSSM Server refused connection | If Proxy is configured, verify network connectivity between HCM-F and Proxy Server |
| CSSM1006 | CSSM API Unknown Host Error | If Proxy is configured, verify Proxy hostname is correct and DNS resolution of CSSM/Proxy/Authentication GW(Transport Mode
                                          Setting) |
| CSSM1007 | CSSM API Socket Timeout Error | If Proxy is configured, verify network connectivity between HCM-F and Proxy Server |
| CSSM1008 | CSSM API No Route To Host Error | If Proxy is configured, verify network connectivity between HCM-F and Proxy Server |
| CSSM1009 | CSSM client creation failed due to invalid Transport Mode | Check HLM Logs (Detailed) for more details |
| CSSM1010 | CSSM client creation failed due to Unknown Error | Check HLM Logs (Detailed) for more details |
| CSSM1011 | CSSM API Authentication Failed Error | Reconfigure client ID and Secret, and perform Smart Account Sync |
| CSSM1012 | CSSM client unable to parse the response | Check HLM Logs (Detailed) for more details |
| CSSM1013 | CSSM client unable to map JSON response | Check HLM Logs (Detailed) for more details |
| CSSM1014 | CSSM client unable to read response due to IO error | Check HLM Logs (Detailed) for more details |
| CSSM1015 | Client credentials may not have access to Smart Account or Domain Name is incorrect | Check if the Client Id and Secret have access to Smart Account and the Domain name is Correct |
| CSSM1016 | CSSM client unable to process response | Check HLM Logs (Detailed) for more details |
| CSSM1017 | CSSM client unable to process JSON response | Check HLM Logs (Detailed) for more details |
| CSSM1018 | CSSM client config validation failed | Check HLM Logs (Detailed) for more details |
| CSSM1019 | Given Smart Account ID does not exist | Check HLM Logs (Detailed) for more details |
| CSSM1020 | CSSM server responded with errors | Check HLM Logs (Detailed) for more details |

| Error Code | Error Message | Recommendation |
|---|---|---|
| CAA1001 | Service encountered an unknown error | Verify App specific adapter Service is running Scan CAA logs for errors and restart service if necessary. |
| CAA1002 | Service encountered an SDR error | Verify Cisco CDM Database is running Scan App specific adapter logs for errors. |
| CAA1003 | CAA is unable to find application instance in SDR | Verify Application is configured Scan CAA logs for errors. |
| CAA1004 | No admin credentials configured for application | Verify admin credentials are configured. |
| CAA1005 | CAA does not support this equipment type | Scan CAA logs for errors. |
| CAA1006 | CAA is unable to read the application name from SDR | Verify Cisco CDM Database is running Scan CAA logs for errors. |
| CAA1007 | No service provider address configured for application | Verify service provider address is configured for the application. |
| CAA1008 | No platform credentials configured for the application | Verify if platform credentials are configured. |
| CAA1009 | No Cluster version configured for the application | Verify if cluster version is configured. |
| CAA1010 | No Request Hanlder Mapping found in json | Verify if request handler exist for message type app type and cluster version. |
| CAA1011 | Error occurred in SSH connection | Check if app details platform credentials are correct and session timeout is sufficient. |
| CAA1012 | Invalid Response type provided | Check response type. |
| CAA1014 | Unable to generate CSR for the given certificate type Provide correct certificate type | Check logs for more details. |
| CAA1015 | Certificate import failed due to CSR public key and Certificate public key doesn't match | Verify whether the certificate and CSR has the same algorithm and key. |
| CAA1016 | Certificate import failed due to CSR SAN and Certificate SAN doesn't match | Verify CSR SAN and Certificate SAN. |
| CAA1017 | Error occurred as CSR does not exist in the App | Generate CSR before proceeding with this action. |
| CAA1018 | CA certificate is not available in the trust-store | Upload a CA certificate in trust store. |
| CAA1019 | Error in CA certificate | Upload a CA certificate in trust store. |
| CAA1020 | Error occurred while reading the certificate | Provide a valid CA Certificate. |
| CAA1021 | Certificate is not in PEM format | Provide a valid Certificate. |
| CAA1022 | Invalid certificate file provided | Provide a valid Certificate. |
| CAA1023 | Error occurred as CSR does not exist in the App | Generate CSR before proceeding with this action. |
| CAA1024 | Error occured as CLI Response Parser is not configured | Configure Parser for CLI command. |
| CAA1025 | Invalid certificate type found | Check if the certificate type is valid. |
| CAA1026 | Certificate Upload failed | Check if the certificate is valid and UC App is provisioned with right version Refer logs for more details. |
| CAA1027 | Certificate operation is not successful Internal error occurred | Check the logs for more details. |
| CAA1028 | Failed to get the REST API client | Verify application is running the supported version. |
| CAA1029 | Error occurred during REST API call to Expressway | Verify credentials are correct and REST service is up on Expressway. |
| CAA1030 | Current version of Expressway is not supported | Use the supported versions of Expressway. |
| CAA1031 | Error occurred as invalid certificate was | Uploaded to Expressway. Verify the CA certificate is available in the trust and uploaded CA signed certificate is valid. |
| CAA1032 | Error occurred as CSR already exist in Expressway | Delete the existing CSR. |
| CAA1033 | Error occurred in CSR generation in Expressway as invalid data was passed fo CSR | Verify the data provided to generate CSR. |
| CAA1034 | No Response Hanlder Mapping found in json | Verify if response handler exist for message type app type and cluster version. |
| CAA1035 | Invalid admin credentials | Verify the user name and password. |
| CAA1036 | CAA encountered an unknown error from the application | Verify the following entities - Cisco AXL Web Service (Cisco
                                          Unified CM) is active Publisher Admin/Platform credentials and
                                          Network address HCMF) are correct. |
| CAA1037 | CAA encountered error while parsing xml | Make sure the UCApps are returning proper responses. |
| CAA1038 | CAA is unable to determine the application Version | Verify Cisco AXL Web Service Cisco Unified CM) is running on
                                          application. Verify application admin credentials and network
                                          address. |
| CAA1039 | API executed by non admin user | Verify the user name and password for admin credentials. |
| CAA1040 | Invalid Proxy details | Verify the Proxy Hostname and Proxy port configured in Transport Mode Setting. |
| CAA1041 | Edit Transport Settings operation is not allowed since product is in Registered state | Sync Smart Account with CSSM and assign cluster to Virtual Account. |
| CAA1042 | Product may already deregistered | Sync Smart Account with with CSSM. |
| CAA1043 | Internal Error occurred while communicating with Unity Connection | Verify the Cisco Smart License Manager and Tomcat service is running in Unity Connection. |
| CAA1044 | Unsupported message received by CAA service | Scan CAA logs for errors. |
| CAA1045 | CAA does not support the application version | Verify if correct cluster version is configured in HCMF. |
| CAA1046 | CAA cannot connect to application | Verify Cisco AXL Web Service is running on Cisco Unified CM
                                          application Publisher's admin/platform credentials and network
                                          address are correct and network connectivity from HCM-F is
                                          established. |
| CAA1048 | Product Registration Token is either invalid or has been expired | Perform Smart Account Sync with CSSM. |
| CAA1049 | Product is in subscriber Node |  |
| CAA1050 | Exception occurred while performing product operation | Scan CAA logs for errors. |
| CAA1051 | CAA is unable to add community string on application | Verify application admin credentials and network address are correct. Verify community string does not already exist. |
| CAA1052 | CAA is unable to update community string on application | Verify application admin credentials and network address. Verify community string is present. |
| CAA1053 | CAA is unable to delete community string on application | Verify application admin credentials and network address. Verify community string exists. |
| CAA1054 | CAA is unable to add SNMP V3 user on application | Verify application admin credentials and network address. Verify SNMP V3 user does not already exist. |
| CAA1055 | CAA is unable to update SNMP V3 user on application | Verify application admin credentials and network address. Verify SNMP V3 user exists. |
| CAA1056 | CAA is unable to delete SNMP V3 user on application | Verify application admin credentials and network address. Verify SNMP V3 user is present. |
| CAA1057 | CAA is unable to restart application SNMP Master Agent | Verify network connection between HCM-F and application. Verify application platform credentials and network address. |
| CAA1058 | CAA is unable to add Remote Syslog configuration on application | Verify application admin credentials and network address. |
| CAA1059 | CAA is unable to update Remote Syslog configuration on application | Verify application admin credentials and network address. |
| CAA1060 | CAA is unable to add Billing Application Server configuration on application | Verify SFTP Credentials and the directory /home/smuser/ exists on billing server. Verify network connection between application
                                          and billing server. |
| CAA1061 | CAA is unable to update Billing Application Server configuration on application | Verify SFTP Credentials and the directory /home/smuser/ exists on billing server. Verify network connection between application
                                          and billing server. |
| CAA1062 | CAA is unable to remove Billing Application Server configuration on application | Verify application ADMIN credentials and network address. Verify BAS config exists on application. |
| CAA1063 | CAA cannot connect to application platform CLI | Verify platform credentials are configured and network connectivity between HCM-F and application. |
| CAA1064 | CAA is unable to restart application Host Resources Agent | Verify network connection between HCM-F and application. Verify application platform credentials and network address. |
| CAA1065 | Unsupported message received from CAA | Scan CAA logs for errors. |
| CAA1066 | No CUOM is configured for application | Verify CUOM is configured for the application. |
| CAA1067 | No service provider address is configured for CUOM | Verify service provider address is configured for CUOM. |
| CAA1068 | Unable to get process node list from Cisco Unified CM | Verify name in Cisco Unified CM System > Server) matches the
                                          hostname or IP configured in HCM-F for Service Provider or
                                          Application Space Address. |
| CAA1069 | No HTTP credentials configured for application | Verify if HTTP credentials are configured. |
| CAA1070 | No SFTP credentials configured | Verify if SFTP credentials are configured for billing application server. |
| CAA1071 | No SFTP network address configured | Verify if SFTP network address is configured for billing application server. |
| CAA1072 | CAA is unable to find the specified phone device on the application | Verify phone device exists on application. |
| CAA1073 | CAA is unable to find the specified user on the application | Verify end user exists in the application. |
| CAA1074 | Failed to get the web-security details from the UC App | Verify if the web-security data is available on the UC App. |
| CAA1075 | Error occured during RIS call | Check if RIS service is up. |
| CAA1076 | Error occured during CCS call | Check if CC service is up. |
| CAA1077 | Error occurred during PAWS call | Check if PAWS service is up. |
| CAA1078 | Error occurred during command execution on CLI | Verify if the command syntax is correct. |
| CAA1079 | Set Transport Mode failed due Invalid format of on-prem Registration url | Please provide the valid on-prem url. |
| CAA1080 | No Clustering Configuration Found in Expressway | Configure proper clustering Expressway. |
| CAA1081 | Registration with Smart Agent failed | Verify the Proxy connection and the Cisco Unified CM
                                          connectivity with CSSM. Check  CAA/HLM Logs for more
                                          details. |
| CAA1082 | DeRegistration with Smart Agent failed | Verify the Proxy connection and the Cisco Unified CM
                                          connectivity with CSSM or the product is already unregistered
                                          with CSSM. Check CAA/HLM Logs for more details. |
| CAA1083 | Update transport settings failed | Verify the Proxy connection and the Cisco Unified CM
                                          connectivity with CSSM or the product is already registered with
                                          CSSM. Check CAA/HLM Logs for more details. |
| CAA1084 | Error occurred in SSH connection | Check if platform credentials are correct and session timeout is sufficient. |

| Error Code | Error Message | Recommendation |
|---|---|---|
| SLMCT1001 | Virtual Account is not valid | Check if the given Virtual Account is correct |
| SLMCT1002 | Exception occurred while License Mode change | Check if UC application is up and its platform service is running. Check HLM Logs for more details |
| SLMCT1003 | Cluster License Mode did not change successfully | Check HLM Logs for more details |
| SLMCT1004 | Cluster License Mode Change - JMS timeout occurred | Check if Provisioning Adapter Service is up. Check Logs for more details |
| SLMCT1005 | Cluster License Mode Change - JMS timeout occurred | Check if CAA Service is up. Check Logs for more details |
| SLMCT1006 | Cluster is of unsupported Version | Provide a valid cluster |
| SLMCT1007 | Cluster is already assigned | Perform Smart Account sync with CSSM |
| SLMCT1008 | Cluster doesn't have an application | Assign an application to the Cluster |
| SLMCT1011 | Cluster is already unassigned | Perform Smart Account Sync with CSSM |
| SLMCT1012 | Cluster doesn't have publisher node | Assign a publisher node to cluster |
| SLMCT1013 | Cluster application doesn't have platform credentials | Configure platform credentials for cluster application |
| SLMCT1014 | Cluster application doesn't have admin credentials | Configure admin credentials for cluster application |
| SLMCT1015 | Cluste is of unsupported Type | Supported cluster type are Cisco Unified CM, Cisco Unity
                                          Connection and Cisco Emergency Responder |
| SLMCT1016 | Reset Cluster License Mode - did not change successfully | Check HLM Logs for more details |
| SLMCT1017 | Exception occurred while Reset Cluster License Mode | Check if UC Application is up and its platform service is
                                          running. Check HLM Logs for more details |
| SLMCT1018 | Cluster License Mode Change - JMS timeout occurred | Check if Provisioning Adapter Service is up. Check Logs for more details |
| SLMCT1019 | Cluster License Mode Change - JMS timeout occurred | Check if CAA Service is Up. Check Logs for more details |

| Error Code | Error Message | Recommendation |
|---|---|---|
| SLM1001 | Smart Licensing Product Registration request failed due to exception | Check HLM Logs (Detailed) for more details |
| SLM1002 | Smart Licensing Product Registration failed due to JMS timeout | Check if the CAA CUCM Service is started |
| SLM1003 | Smart Licensing Get Transport Mode request failed due to exception | Check HLM Logs (Detailed) for more details |
| SLM1005 | Smart Licensing Update Transport Mode request failed due to exception | Check if the UCapp and its services are up. Check logs for exception details |
| SLM1007 | Smart Licensing Cluster Operation - Cluster does't have admin credentials | Check if admin credentials are configured for cluster application |
| SLM1008 | Smart Licensing Cluster Operation - Cluster does't have platform credentials | Check if platform credentials are configured for cluster application |
| SLM1009 | Smart Licensing Cluster Operation - Cluster don't have a publisher node | Check if cluster has publisher node |
| SLM1010 | Smart Licensing Get Product Token - Unable to generate or retrieve product token for the Virtual Account | Check HLM Logs (Detailed) for more details |
| SLM1011 | Smart Licensing Product DeRegistration failed due to JMS timeout | Check if the CAA CUCM Service is started |
| SLM1012 | Smart Licensing Change License Mode - Cluster HostName/IP is not configured | Check if publisher network address is configured |
| SLM1013 | Smart Licensing Change License Mode request failed while get/update transport mode due to exception | Check UCapps platform service is up or Publishers IP/Hostname and platform credentials are valid |
| SLM1014 | Smart Licensing Change License Mode - Virtual Account is not associated with any License Mode | Check if Virtual Account is associated with License Mode |
| SLM1015 | Smart Licensing Sync - an unknown error occured | Check HLM Logs (Detailed) for more details |
| SLM1016 | Smart Licensing Sync - unable to fetch Smart Account details from SDR | Verify Cisco CDM Database is running. Check HLM Logs (Detailed) for more details |
| SLM1018 | Smart Licensing Change Transport Mode failed due to JMS timeout | Check if the CAA CUCM Adapter is started. |
| SLM1021 | Smart Licensing Product DeRegistration failed due to JMS timeout | Check if the CAA CER Service is started |
| SLM1023 | Smart Licensing Change Transport Mode failed due to JMS timeout | Check if the CAA CER Adapter is started |
| SLM1024 | Smart Licensing Change Transport Mode failed due to JMS timeout | Check if the CAA CUCXN Adapter is started |
| SLM1025 | Smart Licensing Request Failed due to Invalid Cluster Exception | Check HLM Logs (Detailed) for more details |

| Error Code | Error Message | Recommendation |
|---|---|---|
| UCAPI1001 | Updating Cisco Unified CM Billing Server info failed | N/A |
| UCAPI1002 | Updating Cisco Unified CM Remote Syslog info failed | N/A |
| UCAPI1003 | Updating Cisco Unified CM SNMP info failed | N/A |
| UCAPI1004 | Validation of Cisco Unified CM AXL Connection failed | Check AXL services and Platform services are up in Cisco Unified
                                          CM |
| UCAPI1005 | Accessing Cisco Unified CM AXL SOAP Port failed | Check AXL services and Platform services are up in Cisco Unified
                                          CM |
| UCAPI1006 | Initialization failed | N/A |
| UCAPI1007 | Software Error | N/A |
| UCAPI1008 | Unknown Failure | N/A |
| UCAPI1009 | Connection Timeout | N/A |
| UCAPI1010 | Registration with Smart Agent failed | Verify the Proxy connection and the Cisco Unified CM connectivity
                                          with CSSM. Check CAA/HLM Logs for more details. |
| UCAPI1011 | DeRegistration with Smart Agent failed | Verify the Proxy connection and the Cisco Unified CM connectivity
                                          with CSSM or the product is already unregistered with CSSM.
                                          Check CAA/HLM Logs for more details. |
| UCAPI1012 | Update transport settings failed | Verify the Proxy connection and the Cisco Unified CM connectivity
                                          with CSSM or the product is already unregistered with CSSM.
                                          Check CAA/HLM Logs for more details. |

| REST API | Response | Code | Message | Recommended Action |
|---|---|---|---|---|
| transportsettings | 405 | METHOD_NOT_ALLOWED | Edit Transport Settings operation is not allowed since product is in either Registered state or is a Subscriber node | Derigister your product instance and run it from correct node (Publisher only) |
| transportsettings | 500 | INTERNAL_SERVER_ERROR | Failed to apply the Transport Settings | Try to run command again with correct information and privilege. If this issue persists, please contact Cisco Technical Support |
| transportsettings | 400 | INVALID_PARAMETER | Please enter a valid Transport Mode within the range (0 - 2) |  |
| 400 | INVALID_PARAMETER | Please enter a valid Transport Gateway URL |  |
| 400 | INVALID_PARAMETER | Please provide valid HTTP/HTTPS Proxy IP Address and/or HTTP/HTTPS Proxy Port |  |
| 400 | INVALID_PARAMETER | Please enter a valid HTTP/HTTPS Proxy IP Address |  |
| 400 | INVALID_PARAMETER | Please enter a valid HTTP/HTTPS Proxy Port within the range (1 - 65535) |  |
| deregister | 405 | METHOD_NOT_ALLOWED | Deregistration is not allowed since product is in either unregistered state or is a Subscriber node | Check License status and Node information and take action accordingly |
| deregister | 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to an unknown error | Check Register status, if its deregister, remove product instance manually from CSSM. EvtSlmCucDeregistrationFailure SmartLicensingDeregistrationFailure |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to invalid trust chain pool |  |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to a communication timeout. |  |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to communication send error |  |
| register | 400 | INVALID_PARAMETER | The Product Instance Registration Token you have entered is either invalid or has been expired. Ensure that you have pasted
                                          the entire token and that the token has not expired | EvtSlmCucRegistrationFailure SmartLicensingRegistrationFailure |
| register | 405 | METHOD_NOT_ALLOWED | Smart Software Licensing operations are not allowed from Subscriber, licenses for this system are managed by Publisher |  |
| 405 | METHOD_NOT_ALLOWED | Product is already registered on CSSM. To Re-register it use 'force' flag |  |
| register | 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to an unknown error | Check the network connectivity with CSSM. For further troubleshooting, check the CuSlmSvr diagnostic logs. Retry Product Registration.
                                          If this issue persists, contact Cisco Technical Support. EvtSlmCucRegistrationFailure SmartLicensingRegistrationFailure |
| 500 | INTERNAL_SERVER_ERROR | The Product Instance was unable to register with Smart Software Licensing |  |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to invalid trust chain pool |  |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to a communication timeout. |  |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to communication send error |  |
| 500 | INTERNAL_SERVER_ERROR | Smart License Server is not running. Start Smart License Manager Server from CUCA Serviceability Page |  |
| renewID | 405 | METHOD_NOT_ALLOWED | Renewal of ID is not allowed since product is in either unregistered state or is a Subscriber node |  |
| renewID | 500 | INTERNAL_SERVER_ERROR | Smart License Server is not running. Start Smart License Manager Server from CUCA Serviceability Page |  |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to a communication timeout |  |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to an unknown error | Check the network connectivity with CSSM. For further troubleshooting, check the CuSlmSvr diagnostic logs. Retry Renew Registration.
                                          If this issue persists, contact Cisco Technical Support. EvtSlmCucRenewRegistrationFailure SmartLicensingRenewRegistrationFailure |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to invalid trust chain pool |  |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to communication send error |  |
| renewAuth | 405 | METHOD_NOT_ALLOWED | Renewal of Authorization is not allowed since product is in either unregistered state or is a Subscriber node |  |
| renewAuth | 500 | INTERNAL_SERVER_ERROR | Smart License Server is not running. Start Smart License Manager Server from CUCA Serviceability Page | Check the network connectivity with CSSM. For further troubleshooting, check the CuSlmSvr diagnostic logs. Retry Renew Authorization.
                                          If this issue persists, contact Cisco Technical Support. EvtSlmCucRenewAuthFailure SmartLicensingRenewAuthFailure |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to a communication timeout |  |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to an unknown error |  |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to invalid trust chain pool |  |
| 500 | INTERNAL_SERVER_ERROR | The requested operation was not successful due to communication send error |  |
| licensedetails | 500 | INTERNAL_SERVER_ERROR | Unable to fetch license count from database |  |
| All APIs | 401 | NOT_AUTHORIZED | User is not authorized to perform this operation | Use correct priviledge to run commands AuthenticationFailed |