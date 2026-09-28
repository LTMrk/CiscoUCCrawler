---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-jabber-12-8-cjab-b-deploy-jabber-on-premises-128-cjab-b-deploy-jabber-on-pre-45383eb116
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/jabber/12_8/cjab_b_deploy-jabber-on-premises-128/cjab_b_deploy-jabber-on-premises-128_chapter_01110.html
retrieved_at: 2026-08-21T05:20:49.728560+00:00
---

On-Premises Deployment for Cisco Jabber 12.8

# On-Premises Deployment for Cisco Jabber 12.8

Updated: April 1, 2024

Chapter: Configure Certificate Validation

## Chapter: Configure Certificate Validation

# Configure Certificate Validation

## Configure
                        	 Certificates for an On-Premises Deployment

Certificates are
                              		  required for each service to which the Jabber clients connect.

Step 1

If you have
                                       			 Cisco Unified Presence or Cisco Unified Communications Manager IM and Presence
                                       			 Service, download the applicable HTTP (tomcat) and XMPP certificates.

For more
                                          				information, see the Security
                                             				  Configuration on IM and Presence Service chapter in Configuration and
                                             				  Administration of IM and Presence Service on Cisco Unified Communications
                                             				  Manager .

Step 2

Download the
                                       			 HTTPS (tomcat) certificate for Cisco Unified Communications Manager and Cisco
                                       			 Unity Connection.

For more
                                          				information, see the Cisco
                                             				  Unified Communications Manager Security Guide and the Cisco
                                             				  Unified Communications Operating System Administration Guide found here .

Step 3

Download the HTTP (tomcat) for Webex Meetings Server.

For more information, see the Cisco Webex Meetings Server Administration Guide found here .

Step 4

If you plan to
                                       			 configure remote access, download the Cisco VCS Expressway and Cisco
                                       			 Expressway-E Server certificate. The Server certificate is used for both HTTP
                                       			 and XMPP.

For more
                                          				information, see Configuring Certificates on
                                             				  Cisco VCS Expressway .

Step 5

Generate a
                                       			 Certificate Signing Request (CSR).

Step 6

Upload the
                                       			 certificate to the service.

If you use a
                                          				multiserver SAN, you only need to upload a certificate to the service once per
                                          				cluster per tomcat certificate and once per cluster per XMPP certificate. If
                                          				you do not use a multiserver SAN, then you must upload the certificate to the
                                          				service for every Cisco Unified Communications Manager node.

Step 7

Deploy CA Certificates to Clients

To ensure that
                                          				certificate validation occurs without users receiving a prompt to accept or
                                          				decline certificates, deploy certificates to the local certificate store of the
                                          				clients.

## Deploy CA
                        	 Certificates to Clients

To ensure that
                              		  certificate validation occurs without users receiving a prompt to accept or
                              		  decline certificates, deploy certificates to the local certificate store of the
                              		  endpoint clients.

If you use a
                              		  well-known public CA, then the CA certificate may already exist on the client
                              		  certificate store or keychain. If so, you need not deploy CA certificates to
                              		  the clients.

If your deployment size
                                             				  is

Then
                                             				  we recommend

To a large number of local
                                             				  machines

That you use a certificate deployment tool, such as Group Policy
                                             				  or a certificate deployment management application.

To a smaller number of
                                             				  local machines

That you manually deploy the CA certificates.

### Manually Deploy CA
                           	 Certificates to Cisco Jabber for Windows Clients

Step 1

Make the CA
                                          			 certificate available to the Cisco Jabber for Windows client machine.

Step 2

From the
                                          			 Windows machine, open the certificate file.

Step 3

Install the
                                          			 certificate and then select Next .

Step 4

Select Place all certificates in the following store , then
                                          			 select Browse .

Step 5

Select the
                                          			 Trusted Root Certification Authorities store.

#### What to do next

Verify that the
                                 		  certificate is installed in the correct certificate store by opening the
                                 		  Windows Certificate Manager tool. Browse to Trusted Root Certification
                                       				Authorites > Certificates . The CA root certificate
                                 		  is listed in the certificate store.

### Manually Deploy CA
                           	 Certificates to Cisco Jabber for Mac Clients

Step 1

Make the CA
                                          			 certificate available to the Cisco Jabber for Mac client machine.

Step 2

From the Mac
                                          			 machine, open the certificate file.

Step 3

Add to the
                                          			 login keychain for the current user only, then select Add .

#### What to do next

Verify that the
                                 		  certificate is installed in the correct keychain by opening the Keychain Access
                                 		  Tool and selecting Certificates. The CA root certificate is listed in the
                                 		  keychain.

### Manually Deploy CA
                           	 Certificates to Mobile Clients

To deploy the
                                 			 CA certificates to an iOS client, you need a certificate deployment
                                 			 management application. You can email the CA certificate to users, or make the
                                 			 certificates available on a web server for users to access. Users can download
                                 			 and install the certificate using the certificate deployment management tool.

However,  Jabber for Android does not have a certificate management tool, you must use the following procedure.

Step 1

Download the CA certificate to the device.

Step 2

Tap the device Settings > Security > Install from device storage and follow the instructions.

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | If you have
                                       			 Cisco Unified Presence or Cisco Unified Communications Manager IM and Presence
                                       			 Service, download the applicable HTTP (tomcat) and XMPP certificates. | For more
                                          				information, see the Security
                                             				  Configuration on IM and Presence Service chapter in Configuration and
                                             				  Administration of IM and Presence Service on Cisco Unified Communications
                                             				  Manager . |
| Step 2 | Download the
                                       			 HTTPS (tomcat) certificate for Cisco Unified Communications Manager and Cisco
                                       			 Unity Connection. | For more
                                          				information, see the Cisco
                                             				  Unified Communications Manager Security Guide and the Cisco
                                             				  Unified Communications Operating System Administration Guide found here . |
| Step 3 | Download the HTTP (tomcat) for Webex Meetings Server. | For more information, see the Cisco Webex Meetings Server Administration Guide found here . |
| Step 4 | If you plan to
                                       			 configure remote access, download the Cisco VCS Expressway and Cisco
                                       			 Expressway-E Server certificate. The Server certificate is used for both HTTP
                                       			 and XMPP. | For more
                                          				information, see Configuring Certificates on
                                             				  Cisco VCS Expressway . |
| Step 5 | Generate a
                                       			 Certificate Signing Request (CSR). |  |
| Step 6 | Upload the
                                       			 certificate to the service. | If you use a
                                          				multiserver SAN, you only need to upload a certificate to the service once per
                                          				cluster per tomcat certificate and once per cluster per XMPP certificate. If
                                          				you do not use a multiserver SAN, then you must upload the certificate to the
                                          				service for every Cisco Unified Communications Manager node. |
| Step 7 | Deploy CA Certificates to Clients | To ensure that
                                          				certificate validation occurs without users receiving a prompt to accept or
                                          				decline certificates, deploy certificates to the local certificate store of the
                                          				clients. |

| If your deployment size
                                             				  is | Then
                                             				  we recommend |
|---|---|
| To a large number of local
                                             				  machines | That you use a certificate deployment tool, such as Group Policy
                                             				  or a certificate deployment management application. |
| To a smaller number of
                                             				  local machines | That you manually deploy the CA certificates. |

| Step 1 | Make the CA
                                          			 certificate available to the Cisco Jabber for Windows client machine. |
|---|---|
| Step 2 | From the
                                          			 Windows machine, open the certificate file. |
| Step 3 | Install the
                                          			 certificate and then select Next . |
| Step 4 | Select Place all certificates in the following store , then
                                          			 select Browse . |
| Step 5 | Select the
                                          			 Trusted Root Certification Authorities store. When
                                          			 you finish the wizard, a message is displayed to verify successful certificate
                                          			 import. |

| Step 1 | Make the CA
                                          			 certificate available to the Cisco Jabber for Mac client machine. |
|---|---|
| Step 2 | From the Mac
                                          			 machine, open the certificate file. |
| Step 3 | Add to the
                                          			 login keychain for the current user only, then select Add . |

| Step 1 | Download the CA certificate to the device. |
|---|---|
| Step 2 | Tap the device Settings > Security > Install from device storage and follow the instructions. |