---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-5-cert-creation-use-exwy-b-cisco-expressway-cert-eba69cb74b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-5/cert-creation-use/exwy_b_cisco-expressway-certificate-creation-and-use-deployment-guide-x155/exwy_m_managing-expressway-certificates.html
retrieved_at: 2026-08-16T15:10:04.951796+00:00
---

Cisco Expressway Certificate Creation and Use Deployment Guide (X15.5)

# Cisco Expressway Certificate Creation and Use Deployment Guide (X15.5)

Updated: July 29, 2026

Chapter: Managing Expressway Certificates

## Chapter: Managing Expressway Certificates

# Managing Expressway Certificates

## Managing Expressway Certificates

From Cisco Expressway X15.5 release, Expressway uses two distinct certificate roles for TLS:

Server Certificate — The system presents this to connecting clients to authenticate its identity.

Client Certificate — The system presents this to servers upon connection to verify its identity as a client.

For more information, see the following sections.

Managing the Expressway Server Certificate

Managing the Expressway Client Certificate

### Managing the Expressway Server Certificate

#### Expressway-C Server Certificate Requirements

The Expressway-C server certificate must include the elements listed below in its list of Subject Alternative Names (SAN).

Unified CM phone security profile names : The names of the Phone Security Profiles in Unified CM are configured for encrypted Transport Line Signaling (TLS) and are used for devices requiring remote access.
                                       Use the Fully Qualified Domain Name (FQDN) format and separate multiple entries with commas.

It is essential to generate Certificate Signing Request (CSR) for the new node while adding a new Expressway-C node to an
                                       existing cluster of Expressway-C. It is mandated to put secure profile names as they are on CUCM, if secure registration of
                                       Mobile and Remote Access (MRA) client is needed over MRA. CSR creation on the new node will fail if "Unified CM phone security profile names" are just names or hostnames on CUCM device security profiles. This will force Administrators to change the value of "Unified CM phone security profile names" on CUCM under the Secure Phone Profile page.

From X12.6, it is mandated that the Unified CM phone security profile name must be a Fully Qualified Domain Name (FQDN). It
                                       cannot be just any name or hostname or a value.

For example, jabbersecureprofile.domain.com , DX80SecureProfile.domain.com

The FQDN can comprise multiple levels. Each level's name can only contain letters, digits and hyphens, with each level separated
                                                   by a period (dot). A level name cannot start or end with a hyphen, and the final level name must start with a letter.

Having the secure phone profiles as alternative names means that Unified CM can communicate via Transport Line Signaling (TLS)
                                       with the Expressway-C when it is forwarding messages from devices that use those profiles.

IM and Presence chat node aliases (federated group chat): the Chat Node Aliases (e.g. chatroom1.example.com) that are configured on the IM and Presence servers. These are required only for Unified Communications
                                       XMPP federation deployments that intend to support group chat over TLS with federated contacts.

The Expressway-C automatically includes the chat node aliases in the CSR, providing it has discovered a set of IM&P servers.

We recommend that you use DNS format for the chat node aliases when generating the CSR. You must include the same chat node
                                 aliases in the Expressway-E server certificate's alternative names.

#### Expressway-E Server Certificate Requirements

The Expressway-E server certificate must include the elements listed below in its list of subject alternative names (SAN).
                                 If the Expressway-E is also known by other FQDNs, all of the aliases must be included in the server certificate SAN.

Unified CM registrations domains: all of the domains which are configured on the Expressway-C for Unified CM registrations. Required for secure communications
                                       between endpoint devices and Expressway-E.

The Unified CM registration domains used in the Expressway configuration and Expressway-E certificate, are used by Mobile
                                       and Remote Access clients to lookup the _collab-edge DNS SRV record during service discovery. They enable MRA registrations on Unified CM, and are primarily for service discovery.

These service discovery domains may or may not match the SIP registration domains. It depends on the deployment, and they
                                       do not have to match. One example is a deployment that uses a .local or similar private domain with Unified CM on the internal
                                       network, and public domain names for the Expressway-E FQDN and service discovery. In this case, you need to include the public
                                       domain names in the Expressway-E certificate as SANs. There is no need to include the private domain names used on Unified
                                       CM. You only need to list the edge domain as a SAN.

Select the DNS format and manually specify the required FQDNs. Separate the FQDNs by commas if you need multiple domains. You may select CollabEdgeDNS format instead, which simply adds the prefix collab-edge. to the domain that you enter. This format is recommended if you
                                       do not want to include your top level domain as a SAN (see example in following screenshot).

XMPP federation domains: the domains used for point-to-point XMPP federation. These are configured on the IM&P servers and should also be configured
                                       on the Expressway-C as domains for XMPP federation.

Select the DNS format and manually specify the required FQDNs. Separate the FQDNs by commas if you need multiple domains. Do not use the XMPPAddress format as it may not be supported by your CA, and may be discontinued in future versions of the Expressway software.

IM and Presence chat node aliases (federated group chat): the same set of Chat Node Aliases as entered on the Expressway-C's certificate. They are only required for voice and presence deployments which will support
                                       group chat over TLS with federated contacts.

You can copy the list of chat node aliases from the equivalent Generate CSR page on the Expressway-C.

### Managing the Expressway Client Certificate

This section covers client certificates, including how to view, upload, reset, and generate a Certificate Signing Request
                                 (CSR). It also explains the new option introduced as part of the Cisco Expressway X15.5 release to copy a server certificate directly to a client certificate.

For more information, see Managing Security > Managing the Expressway Client Certificate .in the Cisco Expressway Administrator Guide .

| Note | The FQDN can comprise multiple levels. Each level's name can only contain letters, digits and hyphens, with each level separated
                                                   by a period (dot). A level name cannot start or end with a hyphen, and the final level name must start with a letter. |
|---|---|