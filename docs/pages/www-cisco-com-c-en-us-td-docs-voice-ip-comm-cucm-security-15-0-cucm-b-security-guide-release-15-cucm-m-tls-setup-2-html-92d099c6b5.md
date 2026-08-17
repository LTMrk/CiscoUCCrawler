---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-security-15-0-cucm-b-security-guide-release-15-cucm-m-tls-setup-2-html-92d099c6b5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/15_0/cucm_b_security-guide-release-15/cucm_m_tls-setup_2.html
retrieved_at: 2026-08-17T00:30:14.653648+00:00
---

Security Guide for Cisco Unified Communications Manager, Release 15 and SUs

# Security Guide for Cisco Unified Communications Manager, Release 15 and SUs

Updated: April 6, 2026

Chapter: TLS 1.3 Setup (From Release 15SU2 Onwards)

## Chapter: TLS 1.3 Setup (From Release 15SU2 Onwards)

# TLS 1.3 Setup (From Release 15SU2 Onwards)

## TLS 1.3 Overview

### Introduction to TLS 1.3

TLS 1.3, as defined in RFC 8446, is the highest version of the Transport Layer Security (TLS) protocol. It aims to improve
                              upon its predecessors, particularly TLS 1.2. TLS 1.3 achieves this by addressing security vulnerabilities, enhancing performance,
                              and streamlining the handshake process.

One of the key improvements in TLS 1.3 is the reduction in handshake latency. It significantly enhances the performance of
                              time-sensitive applications. Moreover, TLS 1.3 also reduces round-trip times (RTT), by further optimizing the connection establishment
                              process. TLS 1.3 has dropped support for older and less secure cryptographic algorithms.

### Key Benefits and Security Improvements

Reduced Handshake Latency —TLS 1.3 minimizes round trips during the handshake process. Hence, it enhances performance, especially for latency-sensitive
                                    applications.

Enhanced Security —TLS 1.3 mandates the use of modern cryptographic algorithms. It includes Elliptic Curve Diffie-Hellman (ECDH) for key exchange
                                    and Authenticated Encryption with Associated Data (AEAD) for data encryption and integrity protection. This strengthens security
                                    against various attacks.

Perfect Forward Secrecy (PFS) —By default, TLS 1.3 ensures that even if long-term keys are compromised, past communications remain secure. Hence, it improves
                                    privacy and security.

Encrypted Handshake Messages —TLS 1.3 encrypts handshake messages to prevent passive eavesdropping attacks and ensures confidentiality.

Support for Stronger Algorithms —TLS 1.3 eliminates support for outdated cryptographic algorithms and cipher suites. It reduces the risk of attacks, such
                                    as downgrade attacks and cryptographic vulnerabilities.

### Differences Between TLS 1.2 and TLS 1.3

Signature Algorithm Usage —TLS 1.3 limits the use of RSA signatures and promotes modern signature algorithms like ECDSA and DSA. However, TLS 1.2 relies
                                    more on RSA signatures.

Cipher Suite Reduction —TLS 1.3 reduces the number of supported cipher suites. It focuses on authenticated encryption algorithms like AES-GCM and
                                    ChaCha20-Poly1305. In comparison, TLS 1.2 supports a broader range of cipher suites, including some less secure options.

Security Enhancements —TLS 1.3 introduces features such as PFS by default and encrypted handshake messages. These features are absent in TLS 1.2.
                                    They enhance overall security and privacy.

Certificate Selection —In TLS 1.2, the server selects the certificate based on the key algorithm in the cipher suite negotiated during the handshake.
                                    However, in TLS 1.3, the server determines the certificate based on the supported signature algorithms advertised by the client.
                                    It ensures smoother compatibility and a more secure communication environment.

### Supported Signature Algorithms

The following signature algorithms are supported in the TLS 1.3 protocol for Unified Communications Manager and IM and Presence
                              Service:

ecdsa_secp256r1_sha256

ecdsa_secp384r1_sha384

ecdsa_secp521r1_sha512

rsa_pss_rsae_sha256

rsa_pss_rsae_sha384

rsa_pss_rsae_sha512

rsa_pkcs1_sha256

rsa_pkcs1_sha384

rsa_pkcs1_sha512

## Install and Upgrade Considerations

For Fresh Install, the minimum supported TLS version is 1.2. Here, the TLS versions 1.0 and 1.1 are disabled by default. Run
                           the set tls min-version command in case you want to configure the minimum TLS version as 1.0 or 1.1.

For upgrade and/or migration scenarios, the supported TLS versions are TLS 1.0, 1.1, 1.2, and 1.3. The minimum TLS version
                           is retained from the previous version after upgrade or migration scenarios.

Migration Considerations

TLS 1.3 uses Signature algorithms to choose between RSA or ECDSA signed certificates and evaluates the certificates offered
                           from the server side before it decides on the certificate type. TLS 1.3 does not have a separate Cipher Management settings
                           page. It relies on the existing Enterprise parameters, HTTP Ciphers, and the TLS Cipher settings.

SIP and other non-HTTP interfaces will not have an exclusive RSA only mode for the TLS Cipher Enterprise Parameters Configuration settings. Hence, these interfaces continue to offer both the signature algorithms. You
                           can control the preference order of RSA. See Configure the TLS 1.3 Certificate Preference Order Parameter for more details.

All HTTP inbound interfaces use HTTP Ciphers in the Enterprise Parameters Configuration page to load the RSA or RSA and ECDSA
                           certificates in its context while opening the port for configured for inbound traffic. HTTP Ciphers is set to 'RSA only' as
                           the default setting. From 15 SU2 onwards, by default, only RSA certificate will be loaded for HTTPs traffic there by limiting
                           TLS 1.3 and/or 1.2 to use only RSA signed certificates.

Prior to Release 15SU2, while using TLS for inbound HTTPS traffic, the Cipher Management settings page takes precedence over
                           the HTTP Cipher Enterprise parameter. Hence, to create an ECDSA only HTTPS traffic, administrators had to configure the Cipher
                           Management page with only the ECDSA Ciphers and keep the HTTP Cipher Settings at its default configuration. Post upgrade,
                           this HTTPS connection sends only RSA certificate along with the EC Ciphers and will be loaded in the HTTPS inbound context
                           leading to mismatch and connection failures.

Direct Standard Upgrades—To overcome this failure during the Direct Standard Upgrades upgrade, it automatically switches the
                                 HTTP Cipher Enterprise parameter to All Supported EC and RSA Ciphers as part of the upgrade if a mismatch is detected. This loads both the RSA and ECDSA certificates.

Fresh install with Data Import—For Fresh install with Data Import migration method, you have to switch the HTTP Cipher Enterprise
                                 Parameter manually prior to upgrading to Release 15 SU2 and above.

## TLS 1.3 Interactions

### TLS 1.3 Certificate Preference

By default, the TLS 1.3 protocol prefers ECDSA over RSA. This preference is defined by the client in the signature algorithms
                              that it advertises.

For inbound connections, the SIP, CTI Manager, SIP Proxy, or XMPP TLS 1.3 interfaces always advertises both the ECDSA and
                              RSA certificates, and the selection is based on the client's preference order.

Most of the deployments use RSA signed certificates. A new enterprise parameter " TLS 1.2 Ciphers Preference Order " is added to maintain backward compatibility for deployments using RSA signed certificates.

For more information, see Configure the TLS 1.3 Certificate Preference Order Parameter .

## TLS 1.3 Configuration

TLS 1.3 is supported by default on all the TLS interfaces of Unified Communications Manager and IM and Presence Service. For
                           more information on the ports affected by TLS 1.3, see Ports Affected by Transport Layer Security Version 1.3 .

If Unified Communications Manager and IM and Presence Service makes a secure connection to a service or application that does
                           not support TLS 1.3, then it automatically falls back to a lower version based on the minimum TLS version configured to support
                           interoperability.

Important

Ensure that both the Unified Communications Manager and IM and Presence Service are on the same release versions.

### Set Minimum TLS Version

You can configure the minimum TLS version for Unified Communications Manager. Before you set the minimum TLS version, make
                                 sure that your network devices and applications both support the minimum TLS version configured.

Important

This note is applicable only for Release 15SU2.

The minimum TLS version does not have any impact on the calendaring service vendor. It will negotiate with the maximum supported
                                             TLS version of the calendaring service. The IM and Presence Service displays an error message when the minimum TLS version
                                             is set to 1.3.

Step 1

Log in to the Command Line Interface .

Step 2

To confirm the existing TLS version, run the show tls min-version CLI command.

Step 3

Run the set tls min-version <minimum> CLI command where <minimum> represents the TLS version.

For example, run set tls min-version 1.3 to set the minimum TLS version to 1.3.

From Release 15SU2 onwards, the minimum TLS version is supported cluster-wide and any change to the Unified Communications
                                                               Manager Publisher node is replicated across all other nodes in the cluster. You must also configure the minimum TLS version
                                                               on IM and Presence Service separately. Perform Step 3 on both the Unified Communications Manager and IM and Presence Service Publisher nodes separately and restart all the nodes
                                                               in the clusters for the changes to take effect.

In Release 15SU2, IM and Presence Service supports TLS 1.3 connections only with the Oracle database. For IM and Presence
                                                               Service connections over TLS with MSSQL database, TLS 1.3 is not supported.

In Release 15SU2, the IM and Presence Service does not support connections with MSSQL database over TLS 1.3. Hence, setting
                                                               the minimum TLS version to 1.3 must be avoided in case of active TLS connections between the IM and Presence Service and MSSQL
                                                               database.

For more information on the supported TLS versions for IM and Presence Service, see the Database Setup Guide for the IM and Presence Service .

### Configure the TLS 1.3 Certificate Preference Order Parameter

Use this procedure to determine how Unified Communications Manager and IM and Presence Service selects RSA or EC certificates
                                 while establishing an inbound connection.

Step 1

From Cisco Unified CM Administration, choose System > Enterprise Parameters .

Step 2

In Security Parameters , configure a value for the TLS 1.3 Certificate Preference Order enterprise parameter.

TLS 1.2 Ciphers Preference Order (Default) —When you select this parameter, Unified Communications Manager and/or IM and Presence Service will select as RSA or EC certificate
                                                based on the TLS 1.2 Ciphers preference order if both the TLS 1.2 and 1.3 protocols are offered by the client. This option
                                                selects only what certificate to be used for TLS 1.3 connections; connections continue to use the TLS 1.3 cipher and signature
                                                algorithm.

TLS 1.3 Signature Algorithm Preference Order —When you select this parameter, Unified Communications Manager and/or IM and Presence will select an RSA or EC certificate
                                                based on the TLS 1.3 Signature Algorithm Preference order if TLS 1.3 protocol is offered by the client. It is highly recommended
                                                to review the certificate requirements of the clients (devices) connecting to Unified Communications Manager and/or IM and
                                                Presence Service and update the necessary certificates in the clients' trust store (including ECDSA), when using this option.

Step 3

Click Save .

Important

## TLS 1.3 Restrictions

Common Criteria Mode —For Release 15SU2, TLS 1.3 protocol is not supported in Common Criteria mode. TLS 1.2 is the only supported TLS protocol
                                 in this mode.

SIP Trunk and Phone Security Profile —If you set the Device Security Mode to Authenticated , the phones will switch to a TLS version lower than 1.3. When the minimum supported TLS version on the Unified CM is set
                                 to 1.3, phones and SIP trunks with the Authenticated Device Security Mode is not supported.

Phones Support —For information on the list of supported features for Cisco Video Phone 8875 and Cisco Desk Phone 9800 Series, see the following:

Release Notes for Cisco Video Phone 8875 on Cisco Unified CM

Release Notes for Cisco Desk Phone 9800 Series

## Ports Affected by Transport Layer Security Version 1.3

### Cisco Unified Communications Manager Ports Affected by Transport Layer Security Version 1.3

The following table lists the Unified Communications Manager Ports Affected By TLS Version 1.3:

Application

Protocol

Destination / Listener

Cisco Unified Communications Manager Operating in Normal mode

Minimum TLS version 1.0

Minimum TLS version 1.1

Minimum TLS version 1.2

Minimum TLS version 1.3

Tomcat

HTTPS

443

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

SCCP - SEC - SIG

Signalling Connection Control Part (SCCP)

2443

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

CTL-SERV

Proprietary

2444

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

Computer Telephony Integration (CTI)

Quick Buffer Encoding (QBE)

2749

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

CAPF-SERV

Transmission Control Protocol (TCP)

3804

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

Intercluster Lookup Service (ILS)

Not applicable

7501

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

Location Bandwidth Manager (LBM)

Not Applicable

9005

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

Administrative XML (AXL)

Simple Object Access Protocol (SOAP)

8443

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

High Available- Proxy (HA-Proxy)

TCP

9443

TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

Local Push Notification Service (LPNS)

Secure web socket (wss)

9560

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

SIP OAuth

TCP

5090/5091 (configurable)

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

SIP-SIG

Session Initiation Protocol (SIP)

5061 (configurable)

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

HA Proxy

TCP

6971, 6972

TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

Cisco Tomcat

HTTPS

8443

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

Trust Verification Service (TVS)

Proprietary

2445

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

### Instant Messaging and Presence Service Ports Affected by Transport Layer Security Version 1.3

The following table lists the IM and Presence Service Ports Affected By Transport Layer Security Version 1.3:

Application

Protocol

Destination/Listener

Instant Messaging & Presence Operating in Normal mode

Minimum TLS version 1.0

Minimum TLS version 1.1

Minimum TLS version 1.2

Minimum TLS version 1.3

Tomcat

HTTPS

443, 8443

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

SIP Proxy

Session Initiation Protocol (SIP)

5061

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

SIP Proxy

Session Initiation Protocol (SIP)

5062

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

SIP Proxy

Session Initiation Protocol (SIP)

8083

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

XCP Connection Manager

TLS

5222

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

Server To Server (S2S)

TLS

5269

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

XCP Router

TLS

7400

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

Managed File Transfer (MFT)

HTTPS

7336

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

Third Party Bosh Client

TLS

5280

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

Oracle External Dabatbase

TLS

1521, 2484

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

MS SQL External Database

TLS

1433

TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.1, TLS 1.2, TLS 1.3

TLS 1.2, TLS 1.3

TLS 1.3

TLS 1.3 is supported only from Release 15SU3 onwards.

| Important | Ensure that both the Unified Communications Manager and IM and Presence Service are on the same release versions. |
|---|---|

| Important | This note is applicable only for Release 15SU2. The minimum TLS version does not have any impact on the calendaring service vendor. It will negotiate with the maximum supported
                                             TLS version of the calendaring service. The IM and Presence Service displays an error message when the minimum TLS version
                                             is set to 1.3. |
|---|---|

| Step 1 | Log in to the Command Line Interface . |
|---|---|
| Step 2 | To confirm the existing TLS version, run the show tls min-version CLI command. |
| Step 3 | Run the set tls min-version <minimum> CLI command where <minimum> represents the TLS version. For example, run set tls min-version 1.3 to set the minimum TLS version to 1.3. Note From Release 15SU2 onwards, the minimum TLS version is supported cluster-wide and any change to the Unified Communications
                                                               Manager Publisher node is replicated across all other nodes in the cluster. You must also configure the minimum TLS version
                                                               on IM and Presence Service separately. Perform Step 3 on both the Unified Communications Manager and IM and Presence Service Publisher nodes separately and restart all the nodes
                                                               in the clusters for the changes to take effect. In Release 15SU2, IM and Presence Service supports TLS 1.3 connections only with the Oracle database. For IM and Presence
                                                               Service connections over TLS with MSSQL database, TLS 1.3 is not supported. In Release 15SU2, the IM and Presence Service does not support connections with MSSQL database over TLS 1.3. Hence, setting
                                                               the minimum TLS version to 1.3 must be avoided in case of active TLS connections between the IM and Presence Service and MSSQL
                                                               database. For more information on the supported TLS versions for IM and Presence Service, see the Database Setup Guide for the IM and Presence Service . | Note | From Release 15SU2 onwards, the minimum TLS version is supported cluster-wide and any change to the Unified Communications
                                                               Manager Publisher node is replicated across all other nodes in the cluster. You must also configure the minimum TLS version
                                                               on IM and Presence Service separately. Perform Step 3 on both the Unified Communications Manager and IM and Presence Service Publisher nodes separately and restart all the nodes
                                                               in the clusters for the changes to take effect. In Release 15SU2, IM and Presence Service supports TLS 1.3 connections only with the Oracle database. For IM and Presence
                                                               Service connections over TLS with MSSQL database, TLS 1.3 is not supported. In Release 15SU2, the IM and Presence Service does not support connections with MSSQL database over TLS 1.3. Hence, setting
                                                               the minimum TLS version to 1.3 must be avoided in case of active TLS connections between the IM and Presence Service and MSSQL
                                                               database. For more information on the supported TLS versions for IM and Presence Service, see the Database Setup Guide for the IM and Presence Service . |
| Note | From Release 15SU2 onwards, the minimum TLS version is supported cluster-wide and any change to the Unified Communications
                                                               Manager Publisher node is replicated across all other nodes in the cluster. You must also configure the minimum TLS version
                                                               on IM and Presence Service separately. Perform Step 3 on both the Unified Communications Manager and IM and Presence Service Publisher nodes separately and restart all the nodes
                                                               in the clusters for the changes to take effect. In Release 15SU2, IM and Presence Service supports TLS 1.3 connections only with the Oracle database. For IM and Presence
                                                               Service connections over TLS with MSSQL database, TLS 1.3 is not supported. In Release 15SU2, the IM and Presence Service does not support connections with MSSQL database over TLS 1.3. Hence, setting
                                                               the minimum TLS version to 1.3 must be avoided in case of active TLS connections between the IM and Presence Service and MSSQL
                                                               database. For more information on the supported TLS versions for IM and Presence Service, see the Database Setup Guide for the IM and Presence Service . |

| Note | From Release 15SU2 onwards, the minimum TLS version is supported cluster-wide and any change to the Unified Communications
                                                               Manager Publisher node is replicated across all other nodes in the cluster. You must also configure the minimum TLS version
                                                               on IM and Presence Service separately. Perform Step 3 on both the Unified Communications Manager and IM and Presence Service Publisher nodes separately and restart all the nodes
                                                               in the clusters for the changes to take effect. In Release 15SU2, IM and Presence Service supports TLS 1.3 connections only with the Oracle database. For IM and Presence
                                                               Service connections over TLS with MSSQL database, TLS 1.3 is not supported. In Release 15SU2, the IM and Presence Service does not support connections with MSSQL database over TLS 1.3. Hence, setting
                                                               the minimum TLS version to 1.3 must be avoided in case of active TLS connections between the IM and Presence Service and MSSQL
                                                               database. For more information on the supported TLS versions for IM and Presence Service, see the Database Setup Guide for the IM and Presence Service . |
|---|---|

| Note | For clients that offer only the TLS 1.3 protocol, Unified Communications Manager and/or IM and Presence Service will select
                                          an RSA or EC certificate based on TLS 1.3 Signature Algorithm Preference Order, regardless of the setting of the TLS 1.3 Certificate
                                          Preference Order parameter. This parameter has no impact on the TLS 1.2 protocol negotiation. |
|---|---|

| Step 1 | From Cisco Unified CM Administration, choose System > Enterprise Parameters . |
|---|---|
| Step 2 | In Security Parameters , configure a value for the TLS 1.3 Certificate Preference Order enterprise parameter. TLS 1.2 Ciphers Preference Order (Default) —When you select this parameter, Unified Communications Manager and/or IM and Presence Service will select as RSA or EC certificate
                                                based on the TLS 1.2 Ciphers preference order if both the TLS 1.2 and 1.3 protocols are offered by the client. This option
                                                selects only what certificate to be used for TLS 1.3 connections; connections continue to use the TLS 1.3 cipher and signature
                                                algorithm. TLS 1.3 Signature Algorithm Preference Order —When you select this parameter, Unified Communications Manager and/or IM and Presence will select an RSA or EC certificate
                                                based on the TLS 1.3 Signature Algorithm Preference order if TLS 1.3 protocol is offered by the client. It is highly recommended
                                                to review the certificate requirements of the clients (devices) connecting to Unified Communications Manager and/or IM and
                                                Presence Service and update the necessary certificates in the clients' trust store (including ECDSA), when using this option. |
| Step 3 | Click Save . Important For the parameter changes to take effect, restart the Cisco CallManager and Cisco CTIManager services on Unified Communications
                                                      Manager. Restart the Cisco Config Agent, Cisco XCP Config Manager, Cisco XCP Router, and Cisco XCP Connection Manager services
                                                      on IM and Presence Service. | Important | For the parameter changes to take effect, restart the Cisco CallManager and Cisco CTIManager services on Unified Communications
                                                      Manager. Restart the Cisco Config Agent, Cisco XCP Config Manager, Cisco XCP Router, and Cisco XCP Connection Manager services
                                                      on IM and Presence Service. |
| Important | For the parameter changes to take effect, restart the Cisco CallManager and Cisco CTIManager services on Unified Communications
                                                      Manager. Restart the Cisco Config Agent, Cisco XCP Config Manager, Cisco XCP Router, and Cisco XCP Connection Manager services
                                                      on IM and Presence Service. |

| Important | For the parameter changes to take effect, restart the Cisco CallManager and Cisco CTIManager services on Unified Communications
                                                      Manager. Restart the Cisco Config Agent, Cisco XCP Config Manager, Cisco XCP Router, and Cisco XCP Connection Manager services
                                                      on IM and Presence Service. |
|---|---|

| Note | If you want to use the Phone Security Profile, consider changing it to use an encrypted mode. |
|---|---|

| Application | Protocol | Destination / Listener | Cisco Unified Communications Manager Operating in Normal mode |
|---|---|---|---|
| Minimum TLS version 1.0 | Minimum TLS version 1.1 | Minimum TLS version 1.2 | Minimum TLS version 1.3 |
| Tomcat | HTTPS | 443 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| SCCP - SEC - SIG | Signalling Connection Control Part (SCCP) | 2443 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| CTL-SERV | Proprietary | 2444 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| Computer Telephony Integration (CTI) | Quick Buffer Encoding (QBE) | 2749 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| CAPF-SERV | Transmission Control Protocol (TCP) | 3804 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| Intercluster Lookup Service (ILS) | Not applicable | 7501 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| Location Bandwidth Manager (LBM) | Not Applicable | 9005 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| Administrative XML (AXL) | Simple Object Access Protocol (SOAP) | 8443 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| High Available- Proxy (HA-Proxy) | TCP | 9443 | TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| Local Push Notification Service (LPNS) | Secure web socket (wss) | 9560 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| SIP OAuth | TCP | 5090/5091 (configurable) | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| SIP-SIG | Session Initiation Protocol (SIP) | 5061 (configurable) | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| HA Proxy | TCP | 6971, 6972 | TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| Cisco Tomcat | HTTPS | 8443 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| Trust Verification Service (TVS) | Proprietary | 2445 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |

| Application | Protocol | Destination/Listener | Instant Messaging & Presence Operating in Normal mode |
|---|---|---|---|
| Minimum TLS version 1.0 | Minimum TLS version 1.1 | Minimum TLS version 1.2 | Minimum TLS version 1.3 |
| Tomcat | HTTPS | 443, 8443 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| SIP Proxy | Session Initiation Protocol (SIP) | 5061 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| SIP Proxy | Session Initiation Protocol (SIP) | 5062 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| SIP Proxy | Session Initiation Protocol (SIP) | 8083 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| XCP Connection Manager | TLS | 5222 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| Server To Server (S2S) | TLS | 5269 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| XCP Router | TLS | 7400 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| Managed File Transfer (MFT) | HTTPS | 7336 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| Third Party Bosh Client | TLS | 5280 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| Oracle External Dabatbase | TLS | 1521, 2484 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 |
| MS SQL External Database | TLS | 1433 | TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.1, TLS 1.2, TLS 1.3 | TLS 1.2, TLS 1.3 | TLS 1.3 Note TLS 1.3 is supported only from Release 15SU3 onwards. | Note | TLS 1.3 is supported only from Release 15SU3 onwards. |
| Note | TLS 1.3 is supported only from Release 15SU3 onwards. |

| Note | TLS 1.3 is supported only from Release 15SU3 onwards. |
|---|---|