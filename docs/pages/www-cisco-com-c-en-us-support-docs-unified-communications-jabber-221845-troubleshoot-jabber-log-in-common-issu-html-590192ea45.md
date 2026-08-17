---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-221845-troubleshoot-jabber-log-in-common-issu-html-590192ea45
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/221845-troubleshoot-jabber-log-in-common-issu.html
retrieved_at: 2026-08-17T03:32:10.796462+00:00
---

Troubleshoot Jabber Log in - Common Issues

# Troubleshoot Jabber Log in - Common Issues

### Download Options

Updated: April 4, 2024

Document ID: 221845

Contents

## Contents

## Introduction

This document describes the most common Jabber login issues and how to correct them.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of Cisco Unified Communications Manager (CUCM) and Cisco Jabber.

### Components Used

The information in this document is based on the listed software versions:

- Cisco Unified Communications Manager (CUCM) 14.0.1 SU2

- Domain Name System (DNS)

- Cisco Jabber 14.1.3

- Windows 11

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Common Problems and Solutions

The errors listed in the document are the most common errors seen when a login failure occurs when using Cisco Jabber.

### Untrusted server. No services discovered

Login Error: Untrusted server. No services discovered.

#### CUCM Certificate Failure

The untrusted server error is displayed when the operating system the Jabber client is installed on does not trust the Certificate Authority used to sign the CUCM Tomcat certificate.

Jabber Logs

INFO [0x00002fd0] [tutils\adapters\HttpCertAdapter.cpp(109)] [csf.httpclient] [csf::netutils::adapters::HttpCertAdapter::verifyCertificate] - *-----* Certificate Verification Result: FAILURE

INFO [0x00002fd0] [ls\src\http\BasicHttpClientImpl.cpp(675)] [csf.httpclient] [csf::http::performRequest] - *-----* HTTP response code 0 connect code 0 for request #0 to PII_CED_Exception{https://cucmpub.domain.com:8443/cucm-uds/version }

ERROR [0x00002fd0] [ls\src\http\BasicHttpClientImpl.cpp(568)] [csf.httpclient] [csf::http::executeImpl] - There was an issue performing the call to curl_easy_perform for request #0: CERTIFICATE_VALIDATION_ERROR

Solution

- Upload the self-signed certificate to the user machine as a trusted certificate authority.

- Verify the certificates root Certificate Authority is a trusted root on the operating machine running Cisco Jabber.

### Cannot find your services automatically

Login Error: Cannot find services automatically.

#### DNS SRV Failure

During initial login, Cisco Jabber queries for DNS service records to automatically detect and locate services on the network. If these queries fail the Cisco Jabber login process fails due to services not being identified.

Jabber Logs

WARN [0x00003398] [src\dnsutils\win32\win32DnsUtils.cpp(52)] [csf.dns] [csf::dns::mapFromWindowsDNSResult] - *-----* DNS query PII_CED_Exception{_cisco-uds._tcp.domain.com.} has failed: DNS name does not exist.

WARN [0x00002788] [src\dnsutils\win32\win32DnsUtils.cpp(52)] [csf.dns] [csf::dns::mapFromWindowsDNSResult] - *-----* DNS query PII_CED_Exception{_collab-edge._tls.domain.com.} has failed: DNS name does not exist.

INFO [0x00000c94] [vices\impl\DiscoveryHandlerImpl.cpp(668)] [service-discovery] [CSFUnified::DiscoveryHandlerImpl::evaluateServiceDiscoveryResult] - ServiceDiscoveryHandlerResult return code FAILED_NO_SRV_RECORDS_FOUND

WARN [0x000024a0] [ices\impl\DiscoveryHandlerImpl.cpp(1061)] [service-discovery] [CSFUnified::DiscoveryHandlerImpl::callOnFailedDiscoveryResultOnDispatcherThread] - Discovery Failure -> (id) name :: (1005) ServiceDiscoveryNoSRVRecordsFound

Solution

If logging into Cisco Jabber on the local network or over VPN, verify the operating system running Jabber can successfully query the _cisco-uds._tcp.domain.com DNS SRV record. When logging into Cisco Jabber over Mobile Remote Access (MRA) verify the operating system can successfully query the _collab-edge._tls.domain.com DNS SRV record.

For assistance with configuring the DNS SRV records used by Cisco Jabber please refer to the On-Premise Deployment Guide for Cisco Jabber .

#### Home Cluster Not Found

The NO_HOME_UDS_FOUND error in the Jabber logs indicates the Cisco Jabber was able to discover the DNS service records but failed to find the CUCM home cluster for the Jabber user.

Jabber Logs

INFO [0x000019d0] [cm-config\uds\LocatorUdsResponse.cpp(82)] [csf.config] [csf::ucm90::LocatorUdsResponse::parseResult] - No Home UDS Location found

ERROR [0x000019d0] [\ucm-config\uds\LocatorUdsQuery.cpp(172)] [csf.config] [csf::ucm90::LocatorUdsQuery::run] - Locator UDS request has failed

WARN [0x000019d0] [ces\impl\ucm-config\UdsProvider.cpp(761)] [csf.config] [csf::ucm90::UdsProvider::getLocatorUdsInformation] - LocatorUdsQuery has failed with result: NO_HOME_UDS_FOUND

ERROR [0x000019d0] [es\impl\ucm-config\UdsProvider.cpp(1042)] [csf.config] [csf::ucm90::UdsProvider::convertLocatorUdsResult] - locatorUdsResult=[NO_HOME_UDS_FOUND] ucmConfigResult=[2]

WARN [0x000019d0] [m90configflows\UcmRetrievalFlow.cpp(152)] [service-discovery] [CSFUnified::Ucm90ConfigRetrievalFlow::mapUcm90ResultCodeToServiceDiscoveryResult] - CUCM Result : Failed - User lookup failure.

Solution

Navigate to CUCM Administration > User Management > End User. Select the user and verify they have the "Home Cluster" checkbox enabled in CUCM.

CUCM End User Home Cluster

### Cannot communicate with the server

Login Error: Cannot communicate with the server.

#### DNS Hostname Failure

During login, Cisco Jabber connects to CUCM to retrieve home cluster and configuration information. When connecting to CUCM Cisco Jabber performs DNS A record lookups for the CUCM nodes. If these queries fail the Cisco Jabber login process fails as Jabber is unable to communicate with the CUCM nodes.

Jabber Logs

INFO [0x000028a8] [src\dnsutils\win32\win32DnsUtils.cpp(47)] [csf.dns] [csf::dns::mapFromWindowsDNSResult] - *-----* DNS query PII_CED_Exception{_cisco-uds._tcp.domain.com.} has succeeded.

INFO [0x00002fe4] [ls\src\http\BasicHttpClientImpl.cpp(675)] [csf.httpclient] [csf::http::performRequest] - *-----* HTTP response code 0 connect code 0 for request #0 to PII_CED_Exception{https://cucmpub.domain.com:8443/cucm-uds/version }

ERROR [0x00002fe4] [ls\src\http\BasicHttpClientImpl.cpp(568)] [csf.httpclient] [csf::http::executeImpl] - There was an issue performing the call to curl_easy_perform for request #0: UNRESOLVED_HOST_ERROR

Solution

If logging into Cisco Jabber on the local network or over VPN, verify the operating system can successfully query each CUCM nodes DNS A record. When logging into Cisco Jabber over Mobile Remote Access (MRA) verify the operating system can successfully query the Expressway-E DNS A record.

#### End User Permissions

During Initial login, Cisco Jabber performs a home UDS lookup for the user that is attempting to login. If the login user is not assigned sufficient privileges the login attempt fails.

Jabber Logs

INFO [0x000004c4] [ls\src\http\BasicHttpClientImpl.cpp(675)] [csf.httpclient] [csf::http::performRequest] - *-----* HTTP response code 403 connect code 0 for request #4 to PII_CED_Exception{https://cucmpub.domain.com:8443/[...]}

ERROR [0x000004c4] [\ucm-config\uds\HomeUdsUtilities.cpp(64)] [csf.config] [csf::ucm90::HomeUdsUtilities::convertHttpUtilsResult] - Home Uds query failed responseCode =[403]

DEBUG [0x000004c4] [cm-config\uds\HomeUdsHttpRequest.cpp(27)] [csf.log] [csf::ucm90::HomeUdsHttpRequest::performHttpRequest] - Result of UDS result conversion - UDS Result: HOME_UDS_QUERY_FAILED.

DEBUG [0x000004c4] [ces\impl\ucm-config\UdsProvider.cpp(915)] [csf.config] [csf::ucm90::UdsProvider::doHomeUdsQuery] - Result from Home UDS query: HOME_UDS_QUERY_FAILED

Solution

Navigate to CUCM Administration > User Management > End User. Select the user and verify they have the "Standard CCM End Users" role is assigned to the end user.

CUCM End User Roles

### Your Username or Password is not correct

Login Error: Your username or password is not correct.

#### Authentication Failure

During initial Cisco Jabber login, users must be authenticated to be authorized for services. If authentication fails the Jabber login attempt fails.

Jabber Logs

INFO [0x0000188c] [ls\src\http\BasicHttpClientImpl.cpp(675)] [csf.httpclient] [csf::http::performRequest] - *-----* HTTP response code 401 connect code 0 for request #4 to PII_CED_Exception{https://cucmpub.domain.com:8443/ [...]}

INFO [0x0000188c] [\ucm-config\uds\HomeUdsUtilities.cpp(61)] [csf.config] [csf::ucm90::HomeUdsUtilities::convertHttpUtilsResult] - Authentication failed

DEBUG [0x0000188c] [cm-config\uds\HomeUdsHttpRequest.cpp(27)] [csf.log] [csf::ucm90::HomeUdsHttpRequest::performHttpRequest] - Result of UDS result conversion - UDS Result: HOME_UDS_AUTHENTICATION_FAILED.

ERROR [0x0000188c] [ces\impl\ucm-config\UdsProvider.cpp(996)] [csf.config] [csf::ucm90::UdsProvider::convertHomeUdsResult] - homeUdsResult=[HOME_UDS_AUTHENTICATION_FAILED] ucmConfigResult=[FAILED_TO_AUTHENTICATE_WITH_CALL_MANAGER]

Solution

Verify the Jabber username and password are correct. If username and password is correct verify that the Jabber user can login to the CUCM end user web interface. If login to the CUCM end user web interface fails verify that the authenticating LDAP is reachable from CUCM and the correct user search base is defined.

### Certificate not valid

Login Error: Certificate not valid.

#### SOAP Certificate Failure

During Initial login, Cisco IM and Presence enabled users authenticate with SOAP services on IM&P. If the Cisco IM and Presence tomcat certificate chain is not trusted by the operating system the login attempt fails.

Jabber Logs

INFO [0x00001088] [CupSoapClient\CupSoapClientImpl.cpp(664)] [csf.jwcpp] [CupSoapClientImpl::LoginAsync] - @CupSoapCli: login cup async, server:imppub.domain.com, user:****, ver:14.2.0.58008

INFO [0x0000035c] [upSoapClient\CupSoapClientImpl.cpp(1213)] [csf.jwcpp] [CupSoapClientImpl::getEndpoint] - @CupSoapCli: soap,endpoint:https://imppub.domain.com:8443/EPASSoap/service/v80

INFO [0x00001088] [rx\jwcpp\LoginMgr\LoginCUPState.cpp(311)] [csf.jwcpp] [CLoginCup::OnLoginFailed] - @LoginMgr: #0, CLoginCup::OnLoginFailed errtype: 37345, errcode: 30, hAsync: 1, bEdgeServerFlag: 0, errstring: SOAP 1.2 fault: SOAP-ENV:Sender[no subcode] "SSL_ERROR_SSL error:1416F086:SSL routines:tls_process_server_certificate:certificate verify failed" Detail: SSL_connect error in tcp_connect(), soapFaultString: SSL_ERROR_SSL error:1416F086:SSL routines:tls_process_server_certificate:certificate verify failed, customData: 1

DEBUG [0x0000035c] [mmon\PlatformVerificationHandler.cpp(58)] [csf.cert] [csf::cert::PlatformVerificationHandler::handlePlatformVerificationResultSynchronously] - finalResult: FAILURE

INFO [0x00001088] [s\adapters\imp\components\Login.cpp(129)] [IMPServices] [CSFUnified::IMPStackCap::Login::OnLoginError] - OnLoginError: LERR_CUP_CERT <11>:

Solution

Verify the operating system running Jabber trusts the Cisco IM and Presence tomcat certificate chain.

#### XMPP Certificate Failure

During Initial login, Cisco IM and Presence enabled users connect to XMPP services. If the Cisco IM and Presence XMPP certificate chain is not trusted by the operating system the login attempt fails.

Jabber Logs

INFO [0x000021c4] [\jwcpp\xmppcore\src\clientbase.cpp(1719)] [csf.jwcpp] [gloox::ClientBase::onSend] - @XmppSDK: #0, 62, Send:<starttls xmlns="urn:ietf:params:xml:ns:xmpp-tls" cookie="0"/>

INFO [0x000021c4] [rwerx\jwcpp\xmppcore\src\client.cpp(254)] [csf.jwcpp] [gloox::Client::handleNormalNode] - @XmppSDK: #0, starting TLS handshake...

ERROR [0x000021c4] [x\jwcpp\xmppcore\src\clientbase.cpp(394)] [csf.jwcpp] [gloox::ClientBase::handleHandshakeResult] - @XmppSDK: #0, TLS handshake failed!

INFO [0x000021c4] [jwcpp\xmppcore\patch\TriClient.cpp(1540)] [csf.jwcpp] [gloox::CTriClient::handleLeaveSession] - @XmppSDK: #0, handleLeaveSession, reason:13

INFO [0x000021c4] [s\adapters\imp\components\Login.cpp(129)] [IMPServices] [CSFUnified::IMPStackCap::Login::OnLoginError] - OnLoginError: LERR_JABBER_CERT <15>: Certificate Failure

Solution

Verify the operating system running Jabber trusts the Cisco IM and Presence XMPP certificate chain.

### Revision History

1.0

04-Apr-2024

Initial Release

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 04-Apr-2024 | Initial Release |