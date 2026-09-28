---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-6-cjab-b-planning-guide-for-cisco-jabber-12-6-cjab-b-planning-guid-c370366f70
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_6/cjab_b_planning-guide-for-cisco-jabber-12-6/cjab_b_planning-guide-for-cisco-jabber-12-6_chapter_0111.html
retrieved_at: 2026-08-21T05:15:58.447061+00:00
---

Planning Guide for Cisco Jabber 12.6

# Planning Guide for Cisco Jabber 12.6

Updated: April 2, 2024

Chapter: Security and Certificates

## Chapter: Security and Certificates

# Security and Certificates

## Encryption

### Compliance and Policy Control for File Transfer and Screen Capture

If you send file transfers and
                                 		  screen captures using the 
                                 		  Managed file
                                 			 transfer option on 
                                 		  Cisco Unified
                                 			 Communications Manager IM and Presence 10.5(2) or later, you can send the files to 
                                 		  a compliance server for audit and policy enforcement.

For more information about
                                 		  compliance, see the Instant Messaging Compliance for IM and Presence Service on Cisco
                                    			 Unified Communications Manager guide.

For more information about
                                 		  configuring file transfer and screen capture, see the Cisco Unified Communications Manager IM and Presence Deployment and Installation Guide .

### Instant Message
                           	 Encryption

Cisco Jabber uses Transport Layer Security (TLS) to secure Extensible Messaging and Presence
                                 		  Protocol (XMPP) traffic over the network between the client and server. Cisco Jabber encrypts point to point instant messages.

#### On-Premises
                              	 Encryption

The following table summarizes the details for instant message encryption in on-premises deployments.

Connection

Protocol

Negotiation Certificate

Expected Encryption Algorithm

Client to server

XMPP over TLS v1.2

X.509 public key infrastructure certificate

AES 256 bit

##### Server and
                                    		  Client Negotiation

The following servers negotiate TLS encryption with Cisco Jabber using X.509 public key infrastructure (PKI) certificates
                                    with the following:

Cisco Unified Communications Manager IM and Presence

Cisco Unified Communications Manager

After the server
                                    		  and client negotiate TLS encryption, both the client and server generate and
                                    		  exchange session keys to encrypt instant messaging traffic.

The following table lists the PKI certificate key lengths for Cisco Unified Communications Manager IM and Presence Service.

Version

Key Length

Cisco Unified Communications Manager IM and Presence Service versions 9.0.1 and higher

2048 bit

##### XMPP
                                    		  Encryption

Cisco Unified Communications Manager IM and Presence Service uses 256-bit length session keys that are encrypted with the
                                    AES algorithm to
                                    		  secure instant message traffic between Cisco Jabber and the presence server.

If you require additional security for traffic between server nodes, you can configure XMPP security settings on Cisco Unified
                                    Communications Manager IM and Presence Service. See the following for more information about security settings:

Cisco Unified Communications Manager IM and Presence Service— Security configuration on IM and Presence

##### Instant
                                    		  Message Logging

You can log and
                                    		  archive instant messages for compliance with regulatory guidelines. To log
                                    		  instant messages, you either configure an external database or integrate with a
                                    		  third-party compliance server. Cisco Unified
                                    		  Communications Manager IM and Presence Service does not encrypt instant messages
                                    		  that you log in external databases or in third party compliance servers. You
                                    		  must configure your external database or third party compliance server as
                                    		  appropriate to protect the instant messages that you log.

See the following for more information about compliance:

Cisco Unified Communications Manager IM and Presence Service— Instant Messaging Compliance for IM and Presence Service

For more information about encryption levels and cryptographic algorithms, including symmetric key algorithms such as AES
                                    or public key algorithms such as RSA, see Next Generation Encryption at this link https://www.cisco.com/c/en/us/about/security-center/next-generation-cryptography.html .

For more
                                    		  information about X.509 public key infrastructure certificates, see the Internet
                                       			 X.509 Public Key Infrastructure Certificate and CRL Profile document at this link https://www.ietf.org/rfc/rfc2459.txt .

#### Cloud-Based
                              	 Encryption

The following table summarizes the details for instant message encryption in cloud-based deployments:

Connection

Protocol

Negotiation Certificate

Expected Encryption Algorithm

Client to server

XMPP within TLS

X.509 public key infrastructure certificate

AES 128 bit

Client to client

XMPP within TLS

X.509 public key infrastructure certificate

AES 256 bit

##### Server and
                                    		  Client Negotiation

The following servers negotiate TLS encryption with Cisco Jabber using X.509 public key infrastructure (PKI) certificates with the Webex Messenger service.

After the server
                                    		  and client negotiate TLS encryption, both the client and server generate and
                                    		  exchange session keys to encrypt instant messaging traffic.

##### XMPP
                                    		  Encryption

The Webex Messenger service uses 128-bit session keys that are encrypted with the AES algorithm to secure instant message traffic between Cisco Jabber and the Webex Messenger service.

You can optionally enable 256-bit client-to-client AES encryption to secure the traffic between clients.

##### Instant
                                    		  Message Logging

The Webex Messenger service can log instant messages, but it does not archive those instant messages in an encrypted format. However, the Webex Messenger service uses stringent data center security, including SAE-16 and ISO-27001 audits, to protect the instant messages that
                                    it logs.

The Webex Messenger service cannot log instant messages if you enable AES 256 bit client-to-client encryption.

For more information about encryption levels and cryptographic algorithms, including symmetric key algorithms such as AES
                                    or public key algorithms such as RSA, see Next Generation Encryption at this link https://www.cisco.com/c/en/us/about/security-center/next-generation-cryptography.html .

For more
                                    		  information about X.509 public key infrastructure certificates, see the Internet
                                       			 X.509 Public Key Infrastructure Certificate and CRL Profile document at this link https://www.ietf.org/rfc/rfc2459.txt .

##### Client-to-Client
                                 	 Encryption

By default,
                                       		  instant messaging traffic between the client and the Cisco WebEx Messenger service is secure. You can optionally specify policies in the Cisco
                                          				  WebEx Administration Tool to secure instant messaging traffic between clients.

Support AES Encoding For
                                                   				  IM —Sending clients encrypt instant messages with the AES 256-bit
                                                				algorithm. Receiving clients decrypt instant messages.

Support No Encoding For
                                                   				  IM —Clients can send and receive instant messages to and from other
                                                				clients that do not support encryption.

Policy
                                                      						Combination

Client-to-Client Encryption

When
                                                      						the Remote Client Supports AES Encryption

When
                                                      						the Remote Client Does not Support AES Encryption

Support AES Encoding For IM = false

Support No Encoding For IM = true

No

Cisco Jabber sends unencrypted instant messages.

Cisco Jabber does not negotiate a key exchange. As a result, other clients do not send Cisco Jabber encrypted instant messages.

Cisco Jabber sends and receives unencrypted instant messages.

Support AES Encoding For IM = true

Support No Encoding For IM = true

Yes

Cisco Jabber sends and receives encrypted instant messages.

Cisco Jabber displays an icon to indicate instant messages are encrypted.

Cisco Jabber sends encrypted instant messages.

Cisco Jabber receives unencrypted instant messages.

Support AES Encoding For IM = true

Support No Encoding For IM = false

Yes

Cisco Jabber sends and receives encrypted instant messages.

Cisco Jabber displays an icon to indicate instant messages are encrypted.

Cisco Jabber does not send or receive instant messages to the remote client.

Cisco Jabber displays an error message when users attempt to send instant messages to the
                                                      						remote client.

Cisco Jabber does not support client-to-client encryption with group chats. Cisco Jabber uses client-to-client encryption for point-to-point chats only.

For more
                                       		  information about encryption and Cisco
                                          				  WebEx policies, see About
                                          			 Encryption Levels in the Cisco
                                          				  WebEx documentation.

#### Encryption Icons

Review the icons that the client displays to indicate encryption levels.

##### Lock Icon for Client to Server Encryption

In both on-premises and cloud-based deployments, Cisco Jabber displays the following icon to indicate client to server encryption:

##### Lock Icon for Client to Client Encryption

In cloud-based deployments, Cisco Jabber displays the following icon to indicate client to client encryption:

#### Local Chat
                              	 History

Chat history is retained after participants close the chat window and until participants sign out. If you do not want to retain
                                    chat history after participants close the chat window, set the Disable_IM_History parameter to true. This parameter is available to all clients except IM-only users.

For on-premises deployment of Cisco Jabber for Mac, if you select the Save chat archives to: option in the Chat Preferences window of Cisco Jabber for Mac, chat history is stored locally in the Mac file system and can be searched using Spotlight.

Cisco Jabber does not encrypt archived instant messages when local chat history is enabled.

For desktop clients, you can restrict access to chat history by savings archives to the following directories:

Windows, %USERPROFILE% \AppData\Local\Cisco\Unified Communications\Jabber\CSF\History\ uri .db

Mac: ~/Library/Application Support/Cisco/Unified Communications/Jabber/CSF/History/ uri .db .

## Voice and Video
                        	 Encryption

You can optionally set up secure phone capabilities for all devices.
                              		  Secure phone capabilities provide secure SIP signaling, secure media streams,
                              		  and encrypted device configuration files.

If you enable secure phone capabilities for users, device connections
                              		  to Cisco Unified Communications Manager are secure. However, calls with other
                              		  devices are secure only if both devices have a secure connection.

## PIE ASLR Support

Cisco Jabber for Android, iPhone and iPad supports Position Independent Executable Address Space Layout Randomization (PIE
                              ASLR).

## Federal
                        	 Information Processing Standards

The Federal
                              		  Information Processing Standard (FIPS) 140 is a U.S. and Canadian government
                              		  standard that specifies security requirements for cryptographic modules. These cryptographic modules
                              		  include the set of hardware, software, and firmware that implements approved
                              		  security functions and is contained within the cryptographic boundary.

FIPS requires that
                              		  all encryption, key exchange, digital signatures, and hash and random number
                              		  generation functions used within the client are compliant with the
                              		  FIPS 140.2 requirements for the security of cryptographic modules.

FIPS mode results
                              		  in the client managing certificates more strictly. Users in FIPS mode may see
                              		  certificate errors in the client if a certificate for a service expires and they haven't reentered their credentials.
                              Users also see a
                              		  FIPS icon in their hub window to indicate that the client is running in FIPS mode.

### Enable FIPS for Cisco Jabber for Windows

Cisco Jabber for Windows supports two methods of enabling FIPS:

Operating system enabled—The Windows operating system is in FIPS mode.

Cisco Jabber bootstrap setting—Configure the FIPS_MODE installer switch. Cisco Jabber can be in FIPS mode on an operating
                                    system that is not FIPS enabled. In this scenario, only connections with non-Windows APIs are in FIPS mode.

Platform Mode

Bootstrap Setting

Cisco Jabber Client Setting

FIPS Enabled

FIPS Enabled

FIPS Enabled—Bootstrap setting.

FIPS Enabled

FIPS Disabled

FIPS Disabled—Bootstrap setting.

FIPS Enabled

No setting

FIPS Enabled—Platform setting.

FIPS Disabled

FIPS Enabled

FIPS Enabled—Bootstrap setting.

FIPS Disabled

FIPS Disabled

FIPS Disabled—Bootstrap setting.

FIPS Disabled

No setting

FIPS Disabled—Platform setting.

### Enable FIPS for Cisco Jabber for Mobile Clients

Important

Enabling FIPS removes the users ability to accept untrusted certificates. In this case, some services may not be available
                                                to users. Certificate Trust List (CTL) or ITL file does not apply here. The servers’ certificates must be properly signed,
                                                or the client must be made to trust the servers’ certificates through side-loading.

FIPS enforces TLS1.2, so the older protocols are disabled.

Cisco Jabber for mobile clients don't support Platform Mode.

## Common Criteria

The Common Criteria for Information Technology Security Evaluation comprise a set of international standards that are used
                              to evaluate the security attributes of IT products. You can run Cisco Jabber in a mode that is compliant with the Common Criteria
                              certification requirements. To do this, you must enable it for each of the clients.

To run Jabber in an environment that is enabled with Common Criteria:

Jabber for Windows: Set the CC_MODE installation argument to TRUE.

For Jabber for Android and Jabber for iPhone and iPad: Set the CC_MODE parameter to TRUE in your Enterprise Mobility Management
                                    (EMM).

The RSA key length must be at least 2048 bits. To configure the RSA key length, read about how to Create and Configure Cisco Jabber Devices in the On-Premises Deployment Guide for Cisco Jabber 12.5 .

For more information about how to set up Jabber to run in common criteria mode, read about how to Deploy Cisco Jabber Applications in the On-Premises Deployment Guide for Cisco Jabber 12.5 .

## Secure LDAP

Secure LDAP communication is LDAP over SSL/TLS

LDAPS initiates an LDAP connection over a SSL/TLS connection. It opens the SSL session then begins using the LDAP protocol.
                              This requires a separate port, 636 or Global Catalog port 3269.

## Authenticated UDS Contact Search

Enable authentication for UDS contact searches in Cisco Unified Communications Manager and Cisco Jabber provides credentials
                              to authenticate with UDS for contact searches.

## Certificates

### Certificate
                           	 Validation

#### The
                                 		  Certificate Validation Process

The operating system Cisco Jabber runs on validates server certificates when authenticating to services. When attempting to establish secure connections, the
                                 service presents Cisco Jabber with a certificate. The operating system validates the presented certificate against what is in the client device's local
                                 certificate store. If the certificate is not in the certificate store, the certificate is deemed untrusted and Cisco Jabber prompts the user to accept or decline the certificate.

If the user
                                 		  accepts the certificate, Cisco Jabber connects to the service and saves the certificate in the certificate store or
                                 		  keychain of the device . If the user declines the certificate, Cisco Jabber does not connect to the service and the certificate is not saved to the
                                 		  certificate store or keychain of the device.

If the
                                 		  certificate is in the local certificate store of the device, Cisco Jabber trusts the certificate. Cisco Jabber connects to the service without prompting the user to accept or decline the
                                 		  certificate.

Cisco Jabber can authenticate to several services, depending on what is deployed in the organization. A certificate signing request (CSR)
                                 must be generated for each service. Some public certificate authorities do not accept more than one CSR per fully qualified
                                 domain name (FQDN). Which means that the CSR for each service may need to be sent to separate public certificate authorities.

Ensure that you
                                 		  specify FQDN in the service profile for each service, instead of the IP address
                                 		  or hostname.

#### Signed
                                 		  Certificates

Certificates can be signed by the certificate authority (CA) or self-signed.

CA-signed certificates (Recommended)—Users are not prompted because you are installing the certificate on the devices yourself.
                                       CA-signed certificates can be signed by a Private CA or a Public CA. Many certificates that are signed by a Public CA are
                                       stored in the certificate store or keychain of the device. Devicies using Android 7.0 or later recognize only CA-signed certificates.

Self-signed certificates—Certificates are signed by the services that are presenting the certificates, and users are always
                                       prompted to accept or decline the certificate.

#### Certificate
                                 		  Validation Options

Whether you
                                          				are deploying certificates for on-premises or cloud-based deployments.

What method
                                          				you are using to sign the certificates.

If are you
                                          				deploying CA-signed certificates, whether you are going to use public CA or
                                          				private CA.

Which services
                                          				you need to get certificates for.

### Required
                           	 Certificates for On-Premises Servers

On-premises servers present the following certificates to establish a secure connection with Cisco Jabber :

Server

Certificate

Cisco Unified Communications Manager IM and Presence
                                                				  Service

HTTP ( Tomcat )

XMPP

Cisco Unified
                                                				  Communications Manager

HTTP ( Tomcat ) and CallManager certificate (secure SIP call signaling for secure phone)

Cisco Unity Connection

HTTP ( Tomcat )

Webex Meetings Server

HTTP ( Tomcat )

Cisco VCS Expressway

Cisco Expressway-E

Server certificate (used for HTTP, XMPP, and SIP call signaling)

#### Important
                                 		  Notes

Security Assertion Markup Language (SAML) single sign-on (SSO) and the Identity Provider (IdP) require an X.509 certificate.

You should apply the most recent Service Update (SU) for Cisco Unified Communications Manager IM and Presence
                                          				  Service before you begin the certificate signing process.

The required certificates apply to all server versions.

Each cluster node, subscriber, and publisher, runs a Tomcat service and can present the client with an HTTP certificate.

You should plan to sign the certificates for each node in the cluster.

To secure SIP signaling between the client and Cisco Unified
                                          				  Communications Manager , you should use Certification Authority Proxy Function (CAPF) enrollment.

#### Certificate
                              	 Signing Request Formats and Requirements

Are
                                             				Base64-encoded.

Do not
                                             				contain certain characters, such as @&! , in the Organization , OU , or other fields.

Use specific
                                             				bit lengths in the server's public key.

To prevent issues
                                    		  with your CSRs, you should review the format requirements from the public CA to
                                    		  which you plan to submit the CSRs. You should then ensure that the information
                                    		  you enter when configuring your server conforms to the format that the public
                                    		  CA requires.

One Certificate Per
                                       			 FQDN —Some public CAs sign only one certificate per fully qualified domain
                                    		  name (FQDN).

For example, to sign the HTTP and XMPP certificates for a single Cisco Unified Communications Manager IM and Presence
                                       				  Service node, you might need to submit each CSR to different public CAs.

#### Revocation
                              	 Servers

Cisco Jabber cannot connect to the Cisco Unified Communications Manager servers if the revocation server is not reachable.
                                    Also, if a certificate authority (CA) revokes a certificate, Cisco Jabber does not allow users to connect to that server.

Users are not notified of the following outcomes:

The certificates do not contain revocation information.

The revocation server cannot be reached.

Ensure that the CRL Distribution Point (CDP) field contains an HTTP URL to a certificate revocation list (CRL) on a revocation server.

Ensure that the Authority Information Access (AIA) field contains an HTTP URL for an Online Certificate Status Protocol (OCSP) server.

#### Server Identity in
                              	 Certificates

As part of the signing process, the CA specifies the server identity in the certificate. When the client validates that certificate,
                                    it checks that:

A trusted authority has issued the certificate.

The identity of the server that presents the certificate matches the identity of the server specified in the certificate.

Public CAs generally require a fully qualified domain name (FQDN) as the server identity, not an IP address.

##### Identifier Fields

The client checks the following identifier fields in server certificates for an identity match:

XMPP certificates

SubjectAltName\OtherName\xmppAddr

SubjectAltName\OtherName\srvName

SubjectAltName\dnsNames

Subject CN

HTTP certificates

SubjectAltName\dnsNames

Subject CN

Tip

The Subject CN field can contain a wildcard ( * ) as the leftmost character, for example, *.cisco.com .

##### Prevent
                                    		  Identity Mismatch

If users attempt
                                    		  to connect to a server with an IP address or hostname, and the server
                                    		  certificate identifies the server with an FQDN, the client cannot identify the
                                    		  server as trusted and prompts the user.

If your server
                                    		  certificates identify the servers with FQDNs, you should plan to specify each
                                    		  server name as FQDN in many places on your servers. For more information, see Prevent Identity Mismatch section in Troubleshooting TechNotes .

#### Certificates for
                              	 Multiserver SANs

If you use a multiserver SAN, you only need to upload a certificate to
                                    		  the service once per cluster per tomcat certificate and once per cluster per
                                    		  XMPP certificate. If you do not use a multiserver SAN, then you must upload the
                                    		  certificate to the service for every Cisco Unified Communications Manager node.

### Certificate Validation for Cloud Deployments

Webex Messenger and Webex Meetings Center present the following certificates to the client by default:

CAS

WAPI

Webex certificates are signed by a public Certificate Authority (CA). Cisco Jabber validates these certificates to establish secure
                                          connections with cloud-based services.

Cisco Jabber validates the following XMPP certificates received from Webex Messenger . If these certificates are not included in your operating system, you must provide them.

VeriSign
                                    				Class 3 Public Primary Certification Authority - G5  — This certificate is stored in the Trusted Root
                                    				Certificate Authority

VeriSign Class 3 Secure Server CA - G3 —This certificate validates the Webex Messenger server identity and is stored in the Intermediate Certificate Authority.

AddTrust External CA Root

GoDaddy Class 2 Certification Authority Root Certificate

For more information about root certificates for Cisco Jabber for Windows, see https://www.identrust.co.uk/certificates/trustid/install-nes36.html .

For more information about root certificates for Cisco Jabber for Mac, see https://support.apple.com .

## Server Name Indication Support for Multitenant Hosted Collaboration Solution

Cisco Jabber supports Server Name Indication (SNI) in a Mobile and Remote Access (MRA) deployment with a multitenant Hosted
                              Collaboration Solution.

Cisco Jabber sends the domain information using SNI to Expressway. Expressway looks up the certificate storage to find the
                              certificate that contains the domain information and returns the certificate to Cisco Jabber for validation.

## Antivirus Exclusions

If you deploy antivirus software, include the following folder locations in the antivirus exclusion list:

C:\Users\<User>\AppData\Local\Cisco\Unified Communications\Jabber

C:\Users\<User>\AppData\Roaming\Cisco\Unified Communications\Jabber

C:\ProgramData\Cisco Systems\Cisco Jabber

| Connection | Protocol | Negotiation Certificate | Expected Encryption Algorithm |
|---|---|---|---|
| Client to server | XMPP over TLS v1.2 | X.509 public key infrastructure certificate | AES 256 bit |

| Version | Key Length |
|---|---|
| Cisco Unified Communications Manager IM and Presence Service versions 9.0.1 and higher | 2048 bit |

| Connection | Protocol | Negotiation Certificate | Expected Encryption Algorithm |
|---|---|---|---|
| Client to server | XMPP within TLS | X.509 public key infrastructure certificate | AES 128 bit |
| Client to client | XMPP within TLS | X.509 public key infrastructure certificate | AES 256 bit |

| Policy
                                                      						Combination | Client-to-Client Encryption | When
                                                      						the Remote Client Supports AES Encryption | When
                                                      						the Remote Client Does not Support AES Encryption |
|---|---|---|---|
| Support AES Encoding For IM = false Support No Encoding For IM = true | No | Cisco Jabber sends unencrypted instant messages. Cisco Jabber does not negotiate a key exchange. As a result, other clients do not send Cisco Jabber encrypted instant messages. | Cisco Jabber sends and receives unencrypted instant messages. |
| Support AES Encoding For IM = true Support No Encoding For IM = true | Yes | Cisco Jabber sends and receives encrypted instant messages. Cisco Jabber displays an icon to indicate instant messages are encrypted. | Cisco Jabber sends encrypted instant messages. Cisco Jabber receives unencrypted instant messages. |
| Support AES Encoding For IM = true Support No Encoding For IM = false | Yes | Cisco Jabber sends and receives encrypted instant messages. Cisco Jabber displays an icon to indicate instant messages are encrypted. | Cisco Jabber does not send or receive instant messages to the remote client. Cisco Jabber displays an error message when users attempt to send instant messages to the
                                                      						remote client. |

| Note | Cisco Jabber does not support client-to-client encryption with group chats. Cisco Jabber uses client-to-client encryption for point-to-point chats only. |
|---|---|

| Platform Mode | Bootstrap Setting | Cisco Jabber Client Setting |
|---|---|---|
| FIPS Enabled | FIPS Enabled | FIPS Enabled—Bootstrap setting. |
| FIPS Enabled | FIPS Disabled | FIPS Disabled—Bootstrap setting. |
| FIPS Enabled | No setting | FIPS Enabled—Platform setting. |
| FIPS Disabled | FIPS Enabled | FIPS Enabled—Bootstrap setting. |
| FIPS Disabled | FIPS Disabled | FIPS Disabled—Bootstrap setting. |
| FIPS Disabled | No setting | FIPS Disabled—Platform setting. |

| Note | Jabber Voicemail service only accepts TLS Version TLS 1.2 for HTTPs request https://164.62.224.15/vmrest/version with FIPS enabled during an SSL connection. |
|---|---|

| Important | Enabling FIPS removes the users ability to accept untrusted certificates. In this case, some services may not be available
                                                to users. Certificate Trust List (CTL) or ITL file does not apply here. The servers’ certificates must be properly signed,
                                                or the client must be made to trust the servers’ certificates through side-loading. FIPS enforces TLS1.2, so the older protocols are disabled. Cisco Jabber for mobile clients don't support Platform Mode. |
|---|---|

| Server | Certificate |
|---|---|
| Cisco Unified Communications Manager IM and Presence
                                                				  Service | HTTP ( Tomcat ) XMPP |
| Cisco Unified
                                                				  Communications Manager | HTTP ( Tomcat ) and CallManager certificate (secure SIP call signaling for secure phone) |
| Cisco Unity Connection | HTTP ( Tomcat ) |
| Webex Meetings Server | HTTP ( Tomcat ) |
| Cisco VCS Expressway Cisco Expressway-E | Server certificate (used for HTTP, XMPP, and SIP call signaling) |

| Note | Public CAs generally require a fully qualified domain name (FQDN) as the server identity, not an IP address. |
|---|---|

| Tip | The Subject CN field can contain a wildcard ( * ) as the leftmost character, for example, *.cisco.com . |
|---|---|

| Note | Webex certificates are signed by a public Certificate Authority (CA). Cisco Jabber validates these certificates to establish secure
                                          connections with cloud-based services. |
|---|---|