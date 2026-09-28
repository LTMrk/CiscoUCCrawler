---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-10-5-cjab-bk-d6497e98-00-deployment-installation-guide-ciscojabber-cj-b0376d1e1b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/10_5/CJAB_BK_D6497E98_00_deployment-installation-guide-ciscojabber/CJAB_BK_D6497E98_00_deployment-installation-guide-ciscojabber_chapter_01100.html
retrieved_at: 2026-08-21T05:10:32.329359+00:00
---

Deployment and Installation Guide for Cisco Jabber, Release 10.5

# Deployment and Installation Guide for Cisco Jabber, Release 10.5

Updated: September 5, 2014

Chapter: Set Up Certificate Validation

## Chapter: Set Up Certificate Validation

# Set Up Certificate Validation

## About Certificate
                        	 Validation

Cisco
                                 			 Jabber uses certificate validation to establish secure connections
                              		  with servers.

When attempting to
                              		  establish secure connections, servers present Cisco Jabber with certificates.

Cisco Jabber for
                              		  Mac validates those certificates against certificates in the Keychain.

If the client
                              		  cannot validate a certificate, it prompts the user to confirm if they want to
                              		  accept the certificate.

In Expressway for Mobile and
                                 				  Remote Access deployment, when using an online
                              		  certificate status protocol (OCSP) or online certificate revocation lists (CRL)
                              		  to obtain the revocation status of the certificates, the Cisco Jabber client expects a response time of less
                              		  than 5 seconds. Connections will fail if the response time is greater than the
                              		  expected 5 seconds.

### On-Premises Servers

Review which certificates on-premises servers present to the client and the tasks involved in getting those certificates signed.

#### Required
                              	 Certificates for On-Premises Servers

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

Cisco Webex Meetings Server

HTTP ( Tomcat )

Cisco VCS Expressway

Cisco Expressway-E

Server certificate (used for HTTP, XMPP, and SIP call signaling)

##### Important
                                    		  Notes

Security
                                             				Assertion Markup Language (SAML) single sign-on (SSO) and the Identity Provider
                                             				(IdP) require an X.509 certificate.

You should apply the most recent Service Update (SU) for Cisco Unified Communications Manager IM and Presence
                                                				  Service before you begin the certificate signing process.

The required
                                             				certificates apply to all server versions.

Each cluster
                                             				node, subscriber, and publisher, runs a Tomcat service and can present the client with an HTTP certificate.

You should
                                             				plan to sign the certificates for each node in the cluster.

To secure SIP signaling between the client and Cisco Unified
                                                				  Communications Manager , you should use Certification Authority Proxy Function (CAPF) enrollment.

#### Get Certificates
                              	 Signed by Certificate Authority

Public CA —  
                                             			 A
                                             				  third-party company verifies the server identity and issues a trusted
                                             				  certificate.

Private CA 
                                             			 — You create
                                             				  and manage a local CA and issue trusted certificates.

The signing
                                    		  process varies for each server and can vary between server versions. It is
                                    		  beyond the scope of this document to provide detailed steps for every version
                                    		  of each server. You should consult the appropriate server documentation for
                                    		  detailed instructions on how to get certificates signed by a CA. However, the
                                    		  following steps provide a high-level overview of the procedure:

Generate a
                                             			 Certificate Signing Request (CSR) on each server that can present a certificate
                                             			 to the client.

Submit each
                                             			 CSR to the CA.

If the process your company uses means you must wait for the CSRs
                                                				to be sent back to you before you can apply them, then you may wish to
                                                				configure your services now while you wait for the CSRs. Then you can apply the
                                                				certificates after the service configuration is complete, prior to deployment.

Upload the
                                             			 certificates that the CA issues to each server.

##### Certificate
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

A trusted
                                             				authority has issued the certificate.

The identity
                                             				of the server that presents the certificate matches the identity of the server
                                             				specified in the certificate.

Public CAs
                                                   				generally require a fully qualified domain name (FQDN) as the server identity,
                                                   				not an IP address.

##### Identifier
                                    		  Fields

SubjectAltName\OtherName\xmppAddr

SubjectAltName\OtherName\srvName

SubjectAltName\dnsNames

Subject CN

SubjectAltName\dnsNames

Subject CN

The Subject
                                                      				CN field can contain a wildcard ( * ) as the
                                                   			 leftmost character, for example, *.cisco.com .

##### Prevent
                                    		  Identity Mismatch

If users attempt
                                    		  to connect to a server with an IP address or hostname, and the server
                                    		  certificate identifies the server with an FQDN, the client cannot identify the
                                    		  server as trusted and prompts the user.

If your server
                                    		  certificates identify the servers with FQDNs, you should plan to specify each
                                    		  server name as FQDN in many places on your servers. For more information, see Prevent Identity Mismatch section in Troubleshooting TechNotes .

##### Provide XMPP
                                 	 Domain to Clients

This task is not required if you are using Cisco Unified
                                       		  Communications Manager IM and Presence Service version 10.0 or later.

The client
                                       		  identifies XMPP certificates using the XMPP domain, rather than
                                       		  the FQDN. The XMPP certificates must contain the XMPP domain in an
                                       		  identifier field.

When the client
                                       		  attempts to connect to the presence server, the presence server provides the
                                       		  XMPP domain to the client. The client can then validate the identity of the
                                       		  presence server against the XMPP certificate.

Complete the
                                       		  following steps to ensure the presence server provides the XMPP domain to the
                                       		  client:

Open the
                                                			 administration interface for your presence server, as follows:

- Cisco Unified
                                                      				  Communications Manager IM and Presence Service — Open the Cisco
                                                      				  Unified CM IM and Presence Administration interface.

- Cisco Unified Presence —
                                                   				Open the Cisco
                                                      				  Unified Presence Administration interface.

Select System > Security > Settings .

Locate the XMPP
                                                   				Certificate Settings section.

Specify the
                                                			 presence server domain in the following field: Domain
                                                   				name for XMPP Server-to-Server Certificate Subject Alternative
                                                   				Name .

Select the
                                                			 following checkbox: Use
                                                   				Domain Name for XMPP Certificate Subject Alternative Name .

Click Save .

#### Deploy Certificates on Client Computers

Every server
                                    		  certificate should have an associated certificate in the Keychain on the client
                                    		  computers. Cisco Jabber validates the certificates that the servers present
                                    		  against the certificates in the Keychain.

If root
                                                			 certificates are not present in the Keychain, Cisco Jabber prompts users to accept certificates
                                                			 from each server in your environment.

Always
                                             				  trust server
                                                					 name — The client
                                             					 saves the certificate to the Keychain.

Continue — The client
                                             					 will connect, but when the user restarts the client they are prompted to accept
                                             					 the certificate again.

Does not save the
                                                      						certificate.

Does not connect to the
                                                      						server.

Prevent the
                                    		  warning dialogs by downloading the certificates from the Cisco Unified OS
                                       		  Administration interface. Complete the following steps to deploy self-signed
                                    		  certificates to the user.

For each
                                             			 Cisco node, download the corresponding "tomcat-trust" certificate from the Cisco Unified OS Administration interface. Select Security > Certificate
                                                   				  Management .

Concatenate
                                             			 the certificates into a single file with the extension .pem (for
                                             			 example, "companyABCcertificates.pem" ).

Send the file
                                             			 to your Cisco Jabber users and ask them to double-click it. Doing so launches
                                             			 the Keychain Access application and imports the certificates.

### Certificate
                           	 Requirements for Cloud-Based Servers

Central
                                          				Authentication Service (CAS)

WLAN
                                          				Authentication and Privacy Infrastructure (WAPI)

Cisco
                                                   				  WebEx certificates are signed by a public certificate authority (CA). Cisco Jabber validates these certificates to establish secure connections with cloud-based
                                                			 services.

VeriSign
                                          				Class 3 Public Primary Certification Authority—G5 (stored in the Trusted Root
                                          				Certificate Authority)

VeriSign
                                          				Class 3 Secure Server CA—G3 (stored in the Intermediate Certificate Authority)

The same set of
                                 		  certificates are applicable for Cisco Jabber for Android, iPhone and iPad.

The certificate
                                 		  that is stored in the Intermediate Certificate Authority validates the Cisco WebEx Messenger server identity.

For Cisco Jabber for
                                    				  Windows 9.7.2 or later, you can find more information and installation instructions for
                                 		  the root certificate at http://www.identrust.co.uk/certificates/trustid/install-nes36.html .

For Cisco Jabber for Mac 9.6.1 or later and iOS, you can find more information for the root certificate
                                 		  on the Apple support website at https://support.apple.com .

#### Update Profile
                              	 Photo URLs

In cloud-based deployments, Cisco Webex assigns unique URLs to profile photos when you add or import users. When Cisco Jabber resolves contact information, it retrieves the profile photo from Cisco Webex at the URL where the photo is hosted.

A fully qualified domain name (FQDN) that contains the Cisco Webex domain — The client can validate the web server that is hosting the profile photo against the Cisco Webex certificate.

An IP address — The client cannot validate the web server that is hosting the profile photo against the Cisco Webex certificate. In this case, the client prompts users to accept certificates whenever they look up contacts with an IP address
                                             in their profile photo URLs.

We recommend that you update all profile photo URLs that contain an IP address as the server name. Replace the IP address
                                                         with the FQDN that contains the Cisco Webex domain to ensure that the client does not prompt users to accept certificates.

When you
                                                         				  update a photo, the photo can take up to 24 hours to refresh in the client.

The following steps describe how to update profile photo URLs. Refer to the appropriate Cisco Webex documentation for detailed instructions.

Export user contact data in CSV file format with the Cisco Webex Administration Tool.

In the userProfilePhotoURL field, replace IP addresses with the Cisco Webex domain.

Save the CSV
                                             			 file.

Import the CSV file with the Cisco Webex Administration Tool.

| Server | Certificate |
|---|---|
| Cisco Unified Communications Manager IM and Presence
                                                      				  Service | HTTP ( Tomcat ) XMPP |
| Cisco Unified
                                                      				  Communications Manager | HTTP ( Tomcat ) and CallManager certificate (secure SIP call signaling for secure phone) |
| Cisco Unity Connection | HTTP ( Tomcat ) |
| Cisco Webex Meetings Server | HTTP ( Tomcat ) |
| Cisco VCS Expressway Cisco Expressway-E | Server certificate (used for HTTP, XMPP, and SIP call signaling) |

| Step 1 | Generate a
                                             			 Certificate Signing Request (CSR) on each server that can present a certificate
                                             			 to the client. |
|---|---|
| Step 2 | Submit each
                                             			 CSR to the CA. If the process your company uses means you must wait for the CSRs
                                                				to be sent back to you before you can apply them, then you may wish to
                                                				configure your services now while you wait for the CSRs. Then you can apply the
                                                				certificates after the service configuration is complete, prior to deployment. |
| Step 3 | Upload the
                                             			 certificates that the CA issues to each server. |

| Note | Public CAs
                                                   				generally require a fully qualified domain name (FQDN) as the server identity,
                                                   				not an IP address. |
|---|---|

| Tip | The Subject
                                                      				CN field can contain a wildcard ( * ) as the
                                                   			 leftmost character, for example, *.cisco.com . |
|---|---|

| Step 1 | Open the
                                                			 administration interface for your presence server, as follows: Cisco Unified
                                                      				  Communications Manager IM and Presence Service — Open the Cisco
                                                      				  Unified CM IM and Presence Administration interface. Cisco Unified Presence —
                                                   				Open the Cisco
                                                      				  Unified Presence Administration interface. |
|---|---|
| Step 2 | Select System > Security > Settings . |
| Step 3 | Locate the XMPP
                                                   				Certificate Settings section. |
| Step 4 | Specify the
                                                			 presence server domain in the following field: Domain
                                                   				name for XMPP Server-to-Server Certificate Subject Alternative
                                                   				Name . |
| Step 5 | Select the
                                                			 following checkbox: Use
                                                   				Domain Name for XMPP Certificate Subject Alternative Name . |
| Step 6 | Click Save . |

| Important | If root
                                                			 certificates are not present in the Keychain, Cisco Jabber prompts users to accept certificates
                                                			 from each server in your environment. |
|---|---|

| Step 1 | For each
                                             			 Cisco node, download the corresponding "tomcat-trust" certificate from the Cisco Unified OS Administration interface. Select Security > Certificate
                                                   				  Management . |
|---|---|
| Step 2 | Concatenate
                                             			 the certificates into a single file with the extension .pem (for
                                             			 example, "companyABCcertificates.pem" ). |
| Step 3 | Send the file
                                             			 to your Cisco Jabber users and ask them to double-click it. Doing so launches
                                             			 the Keychain Access application and imports the certificates. Note The operating
                                                         				system requires that the user enter the Mac OS X administration password for
                                                         				each certificate that is being imported. | Note | The operating
                                                         				system requires that the user enter the Mac OS X administration password for
                                                         				each certificate that is being imported. |
| Note | The operating
                                                         				system requires that the user enter the Mac OS X administration password for
                                                         				each certificate that is being imported. |

| Note | The operating
                                                         				system requires that the user enter the Mac OS X administration password for
                                                         				each certificate that is being imported. |
|---|---|

| Important | Cisco
                                                   				  WebEx certificates are signed by a public certificate authority (CA). Cisco Jabber validates these certificates to establish secure connections with cloud-based
                                                			 services. |
|---|---|

| Important | We recommend that you update all profile photo URLs that contain an IP address as the server name. Replace the IP address
                                                         with the FQDN that contains the Cisco Webex domain to ensure that the client does not prompt users to accept certificates. When you
                                                         				  update a photo, the photo can take up to 24 hours to refresh in the client. |
|---|---|

| Step 1 | Export user contact data in CSV file format with the Cisco Webex Administration Tool. |
|---|---|
| Step 2 | In the userProfilePhotoURL field, replace IP addresses with the Cisco Webex domain. |
| Step 3 | Save the CSV
                                             			 file. |
| Step 4 | Import the CSV file with the Cisco Webex Administration Tool. |