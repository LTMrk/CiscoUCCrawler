---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-jabber-215572-cisco-jabber-and-sip-oauth-mode-html-a1fdbd8fa3
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/jabber/215572-cisco-jabber-and-sip-oauth-mode.html
retrieved_at: 2026-08-20T22:13:45.623684+00:00
---

Cisco Jabber and SIP OAuth Mode

# Cisco Jabber and SIP OAuth Mode

### Download Options

Updated: February 26, 2021

Document ID: 215572

Contents

## Contents

## Introduction

This document describes configuration and basic troubleshooting steps to implement SIP OAuth mode with Cisco Jabber.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- Jabber softphone registration

- Unified Communications Manager (UCM)

- Mobile and Remote Access (MRA) solution

### Components Used

Minimum software version to support the SIP OAuth mode:

- Cisco UCM 12.5

- Cisco Jabber 12.5

- Cisco Expressway X12.5

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Restriction

When SIP OAuth Mode is enabled, Enable Digest Authentication and TFTP Encrypted Config options are not supported.

## Background Information

### Key Benefits

Securing SIP signaling and media for Cisco Jabber softphone currently involves multiple configuration steps. The most difficult is to install and renew client certificates (LSCs), especially if a Cisco Jabber device is switching between on-premises and off-premises, and keep the certificates inside the CTL file up to date.

SIP OAuth mode allows Cisco Jabber Softphone to use OAuth self-describing tokens instead of client LSC certificate for authentication on secure SIP interface. Supporting OAuth on the UCM SIP interface allows secure signaling and media for Jabber on-premises and MRA deployments without the need for the mixed mode or CAPF operation.

Key benefits of the SIP OAuth mode support for Cisco Jabber:

- Enables always-on encryption without additional admin burden.

- Secure signaling and media for Cisco Jabber without the need of Mixed mode (no CTL updates, certificates maintenance, and so on)

- Challenges with LSC on multiple devices (laptops/mobile devices..)

- CAPF operation required anytime Jabber installed on a new device.

- CAPF operation not supported over MRA.

### Overall Architecture

Cisco Jabber device recognises that the OAuth authentication is enabled on the SIP interface by parsing the CSF configuration file (http://<cucmIP>:6970/<CSF-device-name>.cnf.xml), configuration file example (some lines left out for brevity):

Cisco Jabber reads the sipOAuthMode parameter to determine if SIP OAuth mode is enabled or not. This parameter can assume one of the following values:

- 0 - SIP OAuth is disabled

- 1 - SIP OAuth is enabled

If SIP OAuth mode is enabled , Jabber uses one of these parameters to determine the port for SIP TLS connection - sipOAuthPort for on-premises or sipMRAOAuthPort for MRA based deployments. The example presents the default values - sipOAuthPort 5090 and sipMRAOAuthPort 5091. These values are configurable and can be different on each CUCM node.

If SIP OAuth mode is disabled , Jabber uses legacy non-secure (5060) or secure (5061) ports for SIP registration.

Note : Cisco UCM uses SIP Phone OAuth Port (5090) to listen for SIP line registration from Jabber OnPremise devices over TLS. However, UCM uses SIP Mobile Remote Access Port (default 5091) to listen for SIP line registrations from Jabber over Expressway through mLTS. Both of these ports are configurable. See the configuration section. The CallManager service listens on both sipOAuthPort and sipMRAOAuthPort. However, both ports use the Tomcat certificate and Tomcat-trust for incoming TLS/mTLS connections. Ensure that your Tomcat-trust store is able to verify the Expressway-C certificate for SIP OAuth mode for MRA to function accurately. In situations, when the Tomcat certificate is re-generated, the CallManager process must be restarted on the affected nodes afterward as well. This is needed for the CCM process to load and use new certificates on sipOAuth ports.

This image depicts the registration of Cisco Jabber while on premises :

This image depicts the registration of Cisco Jabber over MRA :

*Expressway-C nodes use AXL API to inform UCM of the CN/SAN in their certificate. UCM uses this information to validate the Exp-C cert when a mutual TLS connection is established.

## Configuration - Jabber On Premises

Note : Ensure that you completed below points before the configuration of the SIP OAuth mode: - MRA is configured and the connection is established between Unified Communication Manager (UCM) and Expressway (applicable only if MRA in use). - UCM is registered to a Smart or Virtual account with allow export-controlled functionality.

### 1. Configure Refresh Logins.

Configure Refresh Logins with OAuth access tokens and refresh tokens for Cisco Jabber clients. From Cisco Unified CM Administration, choose System > Enterprise Parameters .

### 2. Configure OAuth Ports.

Choose System > Cisco Unified CM . This is an optional step. The picture presents the default values. The acceptable configurable range is 1024 to 49151. Repeat the same procedure for each server.

### 3. Enable SIP OAuth Mode.

Use the Publisher's Command Line Interface to enable SIP OAuth mode globally. Run the command: utils sipOAuth-mode enable .

### 4. Restart Cisco CallManager Service.

From Cisco Unified Serviceability , choose Tools > Control Center – Feature Services . Select and restart the Cisco CallManager service on all nodes where the service is active.

### 5. Configure OAuth Support in Security Profile.

From Cisco Unified CM Administration , choose System > Phone Security Profile . Select Enable OAuth Authentication to enable SIP OAuth support for the endpoint.

## Configuration - Jabber over MRA

### Prerequites

Before configuration of the SIP OAuth mode for Jabber over MRA, complete steps 1-4 from the Configuration - Jabber On Premises chapter of this article.

### Step 1. Enable Refresh Login over MRA.

Refresh logins must be enabled on Expressway (also called self-describing tokens) before configuration of the SIP OAuth authentication with Cisco Jabber over MRA. On the Expressway-C , navigate to Configuration > Unified Communications > Configuration and esure that the Authorize by OAuth Token with refresh parameter is set to On.

### Step 2. Refresh the Unified CM Nodes in Expressway-C.

Navigate to Configuration > Unified Communications > Unified CM servers. Discover or refresh the Unified CM nodes in Expressway-C.

Note : A new CEOAuth (TLS) zone is created automatically in Expressway-C. For example, CEOAuth <Unified CM name>. A search rule is created to proxy the SIP requests originating from Jabber over MRA towards the Unified CM node. This zone uses TLS connections irrespective of whether Unified CM is configured with mixed mode. To establish trust, Expressway-C also sends the hostname and Subject Alternative Name (SAN) details to the Unified CM cluster. See the verification part of this article to ensure that proper configuration is in place.

### Step 3. Configure OAuth Support in Security Profile.

From Cisco Unified CM Administration , choose System > Phone Security Profile . Enable OAuth support on the profile which is assigned to Cisco Jabber.

## Verify

### 1. Check if SIP OAuth Mode is Globally Enabled.

Verify the OAuth mode from Cisco Unified CM Administration , choose System > Enterprise Parameters .

Alternatively, use the Admin CLI - Run the command: run sql select paramvalue FROM processconfig WHERE paramname = 'ClusterSIPOAuthMode'

Possible values: 0 - for Disabled (Default), 1 - for Enabled.

### 2. Verify Expressway-C SAN Entries Successfully Pushed to CUCM.

Expressway-C sends the CN/SAN details of its certificate to UCM through AXL. Those details are saved in the expresswaycconfiguration table. This process is invoked each time you discover or refresh the Unified CM nodes in Expressway-C. Those entries are used to establish trust between UCM and Expressway-C. CN/SAN field of Expressway-C certificate is checked against those entries during MTLS connection to the SIP MRA OAuth port (5091 by default). If the verification is unsuccessfull, the MTLS connection fails.

Verify the entries from Cisco Unified CM Administration , choose Device > Expressway-C (available from UCM 12.5.1Su1 onwards)

Alternatively, use the Admin CLI - Run the command: run sql select * from expresswaycconfiguration

### 3. Verify CEOAuth Zone(s) on Expressway-C.

Navigate to Expressway-C > Configuration > Zones > Zones . Ensure that all newly created CEOAuth zones(s) are in the active state.

### 4. Verify CallManager Process Listens on SIP OAuth Ports.

Run the command from the Admin CLI: show open ports regexp 5090 (default SIP OAuth Port)

Run the command from the Admin CLI: show open ports regexp 5091 (default SIP MRA OAuth Port)

## Troubleshoot

### Jabber Log Example (On-Premises)

Log example for on-premises SIP OAuth registration on port 5090 from Jabber log perspective.

## CSF configuration retrieved

2020-03-30 13:03:18,278 DEBUG [0x000012d8] [src\callcontrol\ServicesManager.cpp(993)] [csf.ecc] [csf::ecc::ServicesManager::fetchDeviceConfig] - fetchDeviceConfig() retrieved config for CSFrado

2020-03-30 13:03:18,278 DEBUG [0x000012d8] [rc\callcontrol\ServicesManager.cpp(1003)] [csf.ecc] [csf::ecc::ServicesManager::fetchDeviceConfig] - Device Config: <device  xsi:type="axl:XIPPhone" ctiid="24" uuid="{6154365f-920b-dc71-b6ff-d23f602e94fb}">

<callManager>

<name>10.10.10.1</name>

<description>ccm12pub</description>

<ports>

<ethernetPhonePort>2000</ethernetPhonePort>

<sipPort>5060</sipPort>

<securedSipPort>5061</securedSipPort>

<sipOAuthPort>5090</sipOAuthPort>

<sipMRAOAuthPort>5091</sipMRAOAuthPort>

<mgcpPorts>

…

<sipOAuthMode>1</sipOAuthMode>

## Setting SIP oauth mode to 1

2020-03-30 13:03:18,747 DEBUG [0x00002968] [ig\CertificateVerificationHelper.cpp(35)] [csf.ecc] [csf::ecc::CertificateVerificationHelper::setSipOauthMode] - sip OAuth Mode=1

## Setting OAuth ports (5090 and 5091) for each UCM server

13:03:19,013 INFO  [0x00002484] [\core\ccapp\config\config_parser.c(1491)] [csf.sip-call-control] [config_process_ccm_properties] - ccm0=10.10.10.1 ccm1=10.10.10.2  ccm2= sip_oauth_port_0=5090 sip_oauth_port_1=5090 sip_oauth_port_2=5090 length=0

13:03:19,013 INFO  [0x00002484] [\core\ccapp\config\config_parser.c(1494)] [csf.sip-call-control] [config_process_ccm_properties] - sip_mar_oauth_port_0=5091 sip_mar_oauth_port_1=5091 sip_mar_oauth_port_2=5091

## Open TLS connection to 5090

2020-03-30 13:03:18,528 DEBUG [0x00000e2c] [sipstack\sip_transport_connection.c(431)] [csf.sip-call-control] [sip_create_transport_connection] - [SIP][CONN][0] create TLS connection 10.10.10.10:5061-----10.10.10.1:5090.

## Sending register message

2020-03-30 13:03:19,200 DEBUG [0x00000e2c] [\sipcc\core\sipstack\ccsip_debug.c(1041)] [csf.sip-call-control] [platform_print_sip_msg] - sipio-sent---> REGISTER sip:10.10.10.1 SIP/2.0

Via: SIP/2.0/TLS 10.10.10.10:62162;branch=z9hG4bK00001188

From: <sip:1010@10.10.10.1>;tag=882323451234089000003bdd-00005eff

To: <sip:1010@10.10.10.1>

Call-ID: 88232345-12340017-00001c0b-00000cfa@10.10.10.10

Max-Forwards: 70

Date: Mon, 30 Mar 2020 11:03:19 GMT

CSeq: 2270 REGISTER

User-Agent: Cisco-CSF

Contact: <sip:a8ae9f92-4b07-a0d7-d701-29320aed1e2e@10.10.10.10:62162;transport=tls>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-882323451234>";+u.sip!devicename.ccm.cisco.com="CSFrado";+u.sip!model.ccm.cisco.com="503";video

Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0,X-cisco-xsi-8.5.1,X-cisco-graceful-reg,X-cisco-duplicate-reg

## 407 Proxy Authentication Required

2020-03-30 13:03:19,310 DEBUG [0x00000e2c] [\sipcc\core\sipstack\ccsip_debug.c(1041)] [csf.sip-call-control] [platform_print_sip_msg] - sipio-recv<--- SIP/2.0 407 Proxy Authentication Required

Via: SIP/2.0/TLS 10.10.10.10:62162;branch=z9hG4bK00001188

From: <sip:1010@10.10.10.1>;tag=882323451234089000003bdd-00005eff

To: <sip:1010@10.10.10.1>;tag=441122775

Date: Mon, 30 Mar 2020 11:03:31 GMT

Call-ID: 88232345-12340017-00001c0b-00000cfa@10.10.10.10

Server: Cisco-CUCM12.5

CSeq: 2270 REGISTER

Proxy-Authenticate: Bearer realm="ccmsipline"

Content-Length: 0

## Register with OAuth token included in the Proxy-Authorization header

2020-03-30 13:03:19,310 DEBUG [0x00000e2c] [\sipcc\core\sipstack\ccsip_debug.c(1041)] [csf.sip-call-control] [platform_print_sip_msg] - sipio-sent---> REGISTER sip:10.10.10.1 SIP/2.0
Via: SIP/2.0/TLS 10.10.10.10:62162;branch=z9hG4bK00004a82
From: <sip:1010@10.10.10.1>;tag=882323451234089000003bdd-00005eff
To: <sip:1010@10.10.10.1>
Call-ID: 88232345-12340017-00001c0b-00000cfa@10.10.10.10
Max-Forwards: 70
Date: Mon, 30 Mar 2020 11:03:19 GMT
CSeq: 2271 REGISTER
User-Agent: Cisco-CSF
Contact: <sip:a8ae9f92-4b07-a0d7-d701-29320aed1e2e@10.10.10.10:62162;transport=tls>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-882323451234>";+u.sip!devicename.ccm.cisco.com="CSFrado";+u.sip!model.ccm.cisco.com="503";video
Proxy-Authorization: Bearer token="<long string shorten removed for brevity>"
Supported: replaces,join,sdp-anat,norefersub,resource-priority,extended-refer,X-cisco-callinfo,X-cisco-serviceuri,X-cisco-escapecodes,X-cisco-service-control,X-cisco-srtp-fallback,X-cisco-monrec,X-cisco-config,X-cisco-sis-7.0.0,X-cisco-xsi-8.5.1,X-cisco-graceful-reg,X-cisco-duplicate-reg
Reason: SIP;cause=200;text="cisco-alarm:111 Name=CSFrado ActiveLoad=Jabber_for_Windows-12.8.0.51973 InactiveLoad=Jabber_for_Windows-12.8.0.51973 Last=Application-Requested-Destroy"
Expires: 3600
Content-Type: multipart/mixed; boundary=uniqueBoundary
Mime-Version: 1.0
Content-Length: 1271

# 200 OK for Register

2020-03-30 13:03:19,325 DEBUG [0x00000e2c] [\sipcc\core\sipstack\ccsip_debug.c(1041)] [csf.sip-call-control] [platform_print_sip_msg] - sipio-recv<--- SIP/2.0 200 OK
Via: SIP/2.0/TLS 10.10.10.10:62162;branch=z9hG4bK00004a82
From: <sip:1010@10.10.10.1>;tag=882323451234089000003bdd-00005eff
To: <sip:1010@10.10.10.1>;tag=1915868308
Date: Mon, 30 Mar 2020 11:03:31 GMT
Call-ID: 88232345-12340017-00001c0b-00000cfa@10.10.10.10
Server: Cisco-CUCM12.5
CSeq: 2271 REGISTER
Expires: 120
Contact: <sip:a8ae9f92-4b07-a0d7-d701-29320aed1e2e@10.10.10.10:62162;transport=tls>;+sip.instance="<urn:uuid:00000000-0000-0000-0000-882323451234>";+u.sip!devicename.ccm.cisco.com="CSFrado";+u.sip!model.ccm.cisco.com="503";video;x-cisco-newreg
Supported: X-cisco-srtp-fallback,X-cisco-sis-9.1.0
Content-Type: application/x-c

### Scenario 1 - SIP OAuth Registration port Mismatch

Jabber device on premises in SIP OAuth mode fails to register with UCM. UCM sends 403 for the Register message:

SIP/2.0 403 Forbidden
Via: SIP/2.0/TLS 10.5.10.121:50347;branch=z9hG4bK00005163

From: <sip:2000@UCM2-PUB>;tag=005056867e66010a00006698-00002a32

To: <sip:2000@UCM2-PUB>;tag=1946377502

Date: Fri, 03 Aug 2018 05:00:18 GMT

Call-ID: 00505686-7e660005-0000216b-0000366f@10.5.10.121

Server: Cisco-CUCM12.5

CSeq: 363 REGISTER
Retry-After: 35
Warning: 399 UCM2-PUB "SIP OAuth Registration port Mismatch"
Content-Length: 0

Possible solution: Ensure that the following conditions are met:

- OAuth mode is globally enabled

- Device security profile associated with the device has OAuth support enabled

- Message received on 5090 port over TLS instead of mTLS

### Scenario 2 - Unknown CA from Expressway

Expressway-C is unable to establish the mTLS handshake with UCM on sipMRAOAuthport (default 5091). Expressway-C does not trust the certificate shared by UCM and responds with the Unknown CA message during mTLS setup.

Possible solution: The CallManager service sends its Tomcat certificate during the mTLS handshake. Ensure that your Expressway-C trust the signer of UCM's Tomcat certificate.

### Scenario 3 - Unknown CA from UCM

Expressway-C is unable to establish the mTLS handshake with UCM on sipMRAOAuthport (default 5091). UCM does not trust the certificate shared by Expressway and responds with the Unknown CA message during mTLS setup.

Packet capture from this communication (UCM 10.x.x.198, Expressway-C 10.x.x.182):

Possible solution: UCM uses the Tomcat-trust store to verify incoming certificates during the mTLS handshake on SIP OAuth ports. Ensure that the signer's certificate for Expressway-C is properly uploaded onto the UCM.