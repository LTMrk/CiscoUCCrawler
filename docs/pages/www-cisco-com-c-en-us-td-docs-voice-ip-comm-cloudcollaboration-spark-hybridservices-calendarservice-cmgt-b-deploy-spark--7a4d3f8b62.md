---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cloudcollaboration-spark-hybridservices-calendarservice-cmgt-b-deploy-spark--7a4d3f8b62
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cloudCollaboration/spark/hybridservices/calendarservice/cmgt_b_deploy-spark-hybrid-calendar-service/cmgt_b_deploy-spark-hybrid-calendar-service_appendix_01100.html
retrieved_at: 2026-08-20T23:54:18.665893+00:00
---

Deployment guide for Hybrid Calendar

# Deployment guide for Hybrid Calendar

Updated: October 17, 2023

Chapter: Important items for Hybrid Services deployments

## Chapter: Important items for Hybrid Services deployments

# Important items for Hybrid Services deployments

## Important items for Hybrid Services deployments

This section provides added context about key configuration items that relate to Hybrid Services .

These points are crucial if you want to successfully deploy Hybrid Calling for Webex devices. We've highlighted these items in particular for the following
                              reasons:

We want to explain them, so that you understand their role in a hybrid deployment and feel reassured.

They are mandatory prerequisites that ensure a secure deployment between our cloud and your on-premises environment.

They should be treated as pre-day zero activities: they can take a bit longer to complete than typical configuration in a
                                    user interface, so allow a timeframe to get these items sorted.

After these items are addressed in your environment, the rest of your Hybrid Services configuration will go smoothly.

## Supported certificate authorities

The Webex Device Connector must communicate with Webex in order for Hybrid Calling to work.

Webex Device Connector is deployed in the internal network, and the way it communicates with the cloud
                              is through an outbound HTTPS connection—the same type that is used for any browser
                              that connects to a web server.

Communication to the Webex cloud uses TLS. Webex Device Connector is the TLS client, and the Webex cloud is the TLS server. As such, Webex Device Connector checks the server certificate.

The certificate authority signs a server certificate using its own private key.
                              Anyone with the public key can decode that signature and prove that the same
                              certificate authority signed that certificate.

If Webex Device Connector has to validate the certificate provided by the cloud, it must use the public key
                              of the certificate authority that signed that certificate to decode the signature. A
                              public key is contained in the certificate of the certificate authority. To
                              establish trust with the certificate authorities used by the cloud, the list of
                              certificates of these trusted certificate authorities must be in the Webex Device Connector trust store.

When communicating with devices, the tool uses trusted certificates that you provide.
                              Currently the way to do that is by placing them in [home
                                 folder]/.devicestool/certs .

A list of certificate authority certificates is also required for the Expressway-E in
                              the traversal pair. Expressway-E communicates with the Webex cloud using SIP with TLS, enforced by mutual authentication. Expressway-E trusts
                              calls coming from and going to the cloud, only if the CN or SAN of the certificate
                              presented by the cloud during TLS connection setup matches the subject name
                              configured for the DNS zone on Expressway (" callservice.webex.com "). The certificate authority releases a certificate only after an identity check.
                              The ownership of the callservice.webex.com domain must be proved to get a certificate signed. Because we (Cisco) own that
                              domain, the DNS name " callservice.webex.com " is direct proof that the remote peer is truly Webex .

## Exchange Impersonation Account

calendar connector integrates Webex with Microsoft Exchange 2013, 2016, 2019 or Office 365 through an impersonation account. The application impersonation management
                              role in Exchange enables applications to impersonate users in an organization to perform tasks on behalf of the user. The
                              application impersonation role must be configured in Exchange and is used in the calendar connector as part of the Exchange configuration on the Expressway-C interface.

The Exchange impersonation account is Microsoft's recommended method for this task . Expressway-C administrators don't need to know the password, because the value can be entered in the Expressway-C interface by an Exchange administrator. The password isn't clearly shown, even if the Expressway-C administrator has root access to the Expressway-C box. The password is stored encrypted using the same credential encryption mechanism as other passwords on the Expressway-C .

For additional security, follow the steps in Deploy Expressway calendar connector for Microsoft Exchange to enable TLS in order to secure EWS connections on the wire.