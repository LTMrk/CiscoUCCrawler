---
doc_id: help-webex-com-en-us-article-jja499-19d95f9c08
source_url: https://help.webex.com/en-us/article/jja499
retrieved_at: 2026-09-07T10:36:45.837919+00:00
---

Important items for Hybrid Services deployments

This section provides added context about key configuration items that relate to Hybrid Services.

These points are crucial if you want to successfully deploy Hybrid Calling for Webex devices. We've highlighted these items in particular for the following
                reasons:

We want to explain them, so that you understand their role in a hybrid deployment and feel reassured.

They are mandatory prerequisites that ensure a secure deployment between our cloud and your on-premises environment.

They should be treated as pre-day zero activities: they can take a bit longer to complete than typical configuration in a user interface, so allow a timeframe to get these items sorted.

After these items are addressed in your environment, the rest of your Hybrid Services configuration will go smoothly.

TCP port 5062 on the internet firewall

The Expressway-C and Expressway-E
                                                  pair deployment allows calls to and from
                                                the Internet using firewall traversal
                                                  technologies . This deployment is what
                                                securely takes your on-premises call control and
                                                ties it in to Webex.

The Expressway-C and Expressway-E don't require any inbound
                                                port to be opened in the demilitarized zone (DMZ)
                                                firewall because of the firewall traversal
                                                architecture. But TCP SIP signaling ports and UDP
                                                media ports must be opened inbound on the Internet
                                                firewall to let incoming calls come through. You
                                                must allow time to have the appropriate port opened
                                                on your enterprise firewall.

The firewall traversal architecture is shown in the following
                                                  diagram:

For example, for inbound business-to-business (B2B) calls
                                                using SIP protocol, TCP ports 5060 and 5061 (5061 is
                                                used for SIP TLS) must be opened on the external
                                                firewall, together with UDP media ports used for
                                                services such as voice, video, content sharing, dual
                                                video, and so on. Which media ports to open depends
                                                on the number of concurrent calls and the number of
                                                services.

You can configure the SIP listening port on Expressway to be
                                                any value between 1024 to 65534. At the same time,
                                                this value and the protocol type must be advertised
                                                in the public DNS SRV records, and that same value
                                                must be opened on the Internet firewall.

Though the standard for SIP TCP is 5060 and for SIP TLS 5061,
                                                nothing prevents use of different ports, as the
                                                following example shows.

In this example, we assume that port 5062 is
                                                  used for inbound SIP TLS calls.

The DNS SRV record for a cluster of two
                                                  Expressway servers looks like this:

priority = 10

weight = 10

port = 5062

svr hostname = us-expe1.example.com

priority = 10

weight = 10

port = 5062

svr hostname = us-expe2.example.com

These records mean that calls are directed to us-expe1.example.com and us-expe2.example.com with equal load
                                                  sharing (priority and weight) using TLS as the
                                                  transport type and 5062 as the listening port
                                                  number.

A device that is external to the network (on the Internet)
                                                and that makes a SIP call to a user of the corporate
                                                domain (user1@example.com) must query the DNS to
                                                understand which transport type to use, the port
                                                number, how to load-share the traffic, and which SIP
                                                servers to send the call to.

If the DNS entry includes _sips._tcp , the entry
                                                specifies SIP TLS.

TLS is a client-server protocol and, in the most common
                                                implementations, uses certificates for
                                                authentication. In a business-to-business call
                                                scenario, the TLS client is the calling device, and
                                                the TLS server is the called device. With TLS, the
                                                client checks the certificate of the server, and if
                                                the certificate check fails, it disconnects the
                                                call. The client doesn't need a certificate.

TLS handshake is shown in the following diagram:

However, the TLS specification states that the server can
                                                also check the client certificate by sending a
                                                Certificate Request message to the client during TLS
                                                handshake protocol. This message is helpful on a
                                                server-to-server connection, such as on call that is
                                                established between Expressway-E and the Webex cloud. This concept is called TLS with mutual
                                                authentication and is required when integrating with
                                                  Webex.

Both the calling and called parties check the certificate of
                                                the other peer, as the following diagram shows:

The cloud checks the Expressway identity, and Expressway
                                                checks the cloud identity. For example, if the cloud
                                                identity in the certificate (CN or SAN) doesn't
                                                match what's configured on Expressway, the
                                                connection is dropped.

If mutual authentication is turned on, Expressway-E always
                                                requests the client certificate. As a result, Mobile
                                                and Remote Access (MRA) won't work, because in most
                                                cases certificates are not deployed on Jabber
                                                clients. In a business-to-business scenario, if the
                                                calling entity is not able to provide a certificate,
                                                the call is disconnected.

We recommend that you use a value other than 5061 for TLS
                                                with mutual authentication, such as port 5062. Webex Hybrid Services use the same SIP TLS record used
                                                for B2B. In the case of port 5061, some other
                                                services that cannot provide a TLS client
                                                certificate won't work.

If an existing record is already used for
                                                business-to-business communications, we recommend
                                                specifying a subdomain of the corporate domain as
                                                the SIP destination in Control Hub, and consequently
                                                a public DNS SRV record, as follows:

```
Service and protocol: _sips._tcp.mtls.example.com 
Priority: 1 
Weight: 10 
Port number: 5062 
Target: us-expe1.example.com
```

### Business-to-Business, Mobile and Remote Access and Webex traffic on the same Expressway pair

Business-to-business (B2B) and Mobile and Remote Access (MRA)
                                                calls use port 5061 for SIP TLS, and Webex traffic uses port 5062 for SIP TLS with mutual
                                                authentication.

Why the cloud checks domain ownership

The domain ownership check is part of identity verification. Domain verification is a security measure and identity check that the Webex cloud implements to prove that you are who you say you are.

The identity check is performed in two stages:

Domain ownership check. This step involves three types of domains and is a one-time verification check:

Email domain

Expressway-E DNS domain

Directory URI domain

Expressway-E DNS name ownership check. This step is performed through the implementation of TLS with mutual authentication and involves the use of public certificates on both the cloud and the Expressway. Unlike the domain identity check, this step is performed during any call made to and received from the cloud.

### The importance of the domain ownership check

The Webex cloud performs the domain ownership check to enforce security. Identity theft is one possible threat if this check is not performed.

The following story details what might happen if a domain ownership check is not performed.

A company with DNS domain set to "hacker.com" buys Webex Hybrid Services. Another company, with its own domain set to "example.com", is also using
    hybrid services. One of the general managers of the company Example.com is named Jane Roe and
    has the directory URI jane.roe@example.com.

The administrator of Hacker.com company sets one of her directory URIs to jane.roe@example.com and the email address to jane.roe@hacker.com. She can do that because the cloud doesn't check the SIP URI domain in this example.

Next, she signs in to Webex App with jane.roe@hacker.com. Because she owns the domain, the verification email is read and
    answered, and she can sign in. Finally, she makes a call to a colleague, John Doe, by dialing
    john.doe@example.com from her Webex App. John is sitting in his office and sees a call on his video device coming from
    jane.roe@example.com; that is the directory URI associated with that email account.

"She's abroad," he thinks. "She might need something important." He answers the phone, and the fake Jane Roe asks for important documents. She explains that her device is broken, and because she is travelling, she asks him to send the documents to her private email address, jane.roe@hacker.com. This way, the company realizes only after Jane Roe gets back to the office that important information was leaked outside of the company.

The company Example.com has many ways to protect against fraudulent calls coming from the Internet, but one of the responsibilities of the Webex cloud is to make sure that the identity of anyone calling from Webex is correct and not falsified.

To check the identity, Webex requires that the company proves that it owns the domains used in Hybrid Calling. If it
    doesn't, Hybrid Services won't work.

To ensure this ownership, the two domain verification steps are required:

Prove that the company owns the email domain, Expressway-E domain, Directory URI domain.

All those domains must be routable and known by public DNS servers.

To prove the ownership, the DNS administrator must enter a DNS Text record (TXT). A TXT record is a type of resource record in the DNS used to provide the ability to associate some arbitrary and unformatted text with a host or other name.

The DNS administrator must enter that TXT record in the zone whose ownership must be proved. After that step, the Webex cloud performs a TXT record query for that domain.

If the TXT query is successful and the result matches the token that was generated from the Webex cloud, the domain is verified.

As an example, the administrator must prove that she owns the domain "example.com", if she wants Webex Hybrid Services to work on her domain.

Through https://admin.webex.com , she starts the verification process by creating a TXT record to match the token that the Webex cloud generated:

The DNS administrator then creates a TXT record for this domain with the value set to 123456789abcdef123456789abcdef123456789abcdef123456789abcdef , as in the following example:

At this point, the cloud can verify that the TXT record for the domain example.com matches the token.

The cloud performs a TXT DNS lookup:

Because the TXT value matches the token value, this match proves that the administrator added the TXT record for her own domain to the public DNS, and that she owns the domain.

Expressway-E DNS Name ownership check.

The cloud must check that the Expressway-E has a confirmed identity from one of the certificate authorities that the cloud trusts. The Expressway-E administrator must request a public certificate for his Expressway-E to one of those certificate authorities. To issue the certificate, the certificate authority performs an identity verification process, based on a domain validation check (for domain validated certificates) or organization validation check (for organization validated certificates).

Calls to and from the cloud depend on the certificate that was issued to the Expressway-E. If the certificate is not valid, the call is dropped.

Supported certificate authorities

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
                configured for the DNS zone on Expressway ("callservice.webex.com"). The certificate authority releases a certificate only after an identity check.
                The ownership of the callservice.webex.com domain must be proved to get a certificate signed. Because we (Cisco) own that
                domain, the DNS name "callservice.webex.com" is direct proof that the remote peer is truly Webex.

Supported certificate authorities for Webex

Exchange Impersonation Account

calendar connector integrates Webex with Microsoft Exchange 2013, 2016, 2019 or Office 365 through an impersonation account. The application impersonation management role in Exchange enables applications to impersonate users in an organization to perform tasks on behalf of the user. The application impersonation role must be configured in Exchange and is used in the calendar connector as part of the Exchange configuration on the Expressway-C interface.

The Exchange impersonation account is Microsoft's recommended method for this task . Expressway-C administrators don't need to know the password, because the value can be entered in the Expressway-C interface by an Exchange administrator. The password isn't clearly shown, even if the Expressway-C administrator has root access to the Expressway-C box. The password is stored encrypted using the same credential encryption mechanism as other passwords on the Expressway-C.

For additional security, follow the steps in the Deployment Guide for Cisco Webex Hybrid Calendar Service to enable TLS in order to secure EWS connections on the wire.

For additional security, follow the steps in Deploy Expressway Calendar Connector for Microsoft Exchange to enable TLS in order to secure EWS connections on the wire.