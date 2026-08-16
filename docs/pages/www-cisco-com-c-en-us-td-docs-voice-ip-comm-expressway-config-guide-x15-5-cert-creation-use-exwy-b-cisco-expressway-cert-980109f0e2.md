---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x15-5-cert-creation-use-exwy-b-cisco-expressway-cert-980109f0e2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X15-5/cert-creation-use/exwy_b_cisco-expressway-certificate-creation-and-use-deployment-guide-x155/exwy_m_server-certificate-requirements-for-unified.html
retrieved_at: 2026-08-16T15:10:01.249749+00:00
---

Cisco Expressway Certificate Creation and Use Deployment Guide (X15.5)

# Cisco Expressway Certificate Creation and Use Deployment Guide (X15.5)

Updated: July 29, 2026

Chapter: Server Certificate Requirements for Unified Communications

## Chapter: Server Certificate Requirements for Unified Communications

# Server Certificate Requirements for Unified Communications

This chapter explains the following:

## Cisco Unified Communications Manager Certificates

Two Cisco Unified Communications Manager certificates are significant for Mobile and Remote Access:

CallManager certificate

tomcat certificate

These certificates are automatically installed on the Cisco Unified Communications Manager and by default they are self-signed
                              and have the same common name (CN).

We recommend using CA-signed certificates. However, if you do use self-signed certificates, the two certificates must have
                              different common names. The Expressway does not allow two self-signed certificates with the same CN. So if the CallManager and tomcat self-signed certificates have the same CN in the Expressway's trusted CA list, the Expressway can only trust one of them.
                              This means that either secure HTTP or secure SIP, between Expressway-C and Cisco Unified Communications Manager, will fail.

Also, when generating tomcat certificate signing requests for any products in the Cisco Collaboration Systems Release 10.5.2,
                              you need to be aware of CSCus47235 . You need to work around this issue to ensure that the FQDNs of the nodes are in the certificates as Subject Alternative
                              Name (SAN) entries. The Expressway X8.5.3 Release Note on the Release Notes page has details of the workarounds.

## IM and Presence Service Certificates

Two IM and Presence Service certificates are significant if you use XMPP:

cup-xmpp certificate

tomcat certificate

We recommend using CA-signed certificates. However, if you do use self-signed certificates, the two certificates must have
                              different common names. The Expressway does not allow two self-signed certificates with the same CN. If the cup-xmpp and tomcat (self-signed) certificates have the same CN, Expressway only trusts one of them, and some TLS attempts between Cisco Expressway-E
                              and IM and Presence Service servers will fail. For more details, see CSCve56019 .

## Expressway CSR Alternative Name Requirements for Unified Communications Features

The Expressway certificate signing request (CSR) tool prompts for and incorporates the relevant Subject Alternative Name (SAN)
                              entries as appropriate for the Unified Communications features that are supported on  Expressway.

The following table shows which CSR alternative name elements apply to which Unified Communications features:

Add these items as subject alternative names

When generating a CSR for these purposes

Mobile and Remote Access

Jabber Guest

XMPP Federation

Business to Business Calls

Unified CM registrations domains (despite their name, these have more in common with service discovery domains than with Unified
                                          CM SIP registration domains)

Required on Expressway-E only

—

—

—

XMPP federation domains

—

—

Required on Expressway-E only

—

IM and Presence chat node aliases

(federated group chat)

—

—

Required

—

Unified CM phone security profile names

Required on Expressway-C only

—

—

—

(Clustered systems only) Expressway Cluster name

Required on Expressway-C only

Required on Expressway-C only

Required on Expressway-C only

—

You may need to produce a new server certificate for the Expressway-C if chat node aliases are added or renamed. Or when IM
                                                and Presence nodes are added or renamed, or new TLS phone security profiles are added.

You must produce a new Expressway-E certificate if new chat node aliases are added to the system, or if the Unified CM or
                                                XMPP federation domains are modified.

You must restart the Expressway for any new uploaded server certificate to take effect.

| Add these items as subject alternative names | When generating a CSR for these purposes |
|---|---|
|  | Mobile and Remote Access | Jabber Guest | XMPP Federation | Business to Business Calls |
| Unified CM registrations domains (despite their name, these have more in common with service discovery domains than with Unified
                                          CM SIP registration domains) | Required on Expressway-E only | — | — | — |
| XMPP federation domains | — | — | Required on Expressway-E only | — |
| IM and Presence chat node aliases (federated group chat) | — | — | Required | — |
| Unified CM phone security profile names | Required on Expressway-C only | — | — | — |
| (Clustered systems only) Expressway Cluster name | Required on Expressway-C only | Required on Expressway-C only | Required on Expressway-C only | — |

| Note | You may need to produce a new server certificate for the Expressway-C if chat node aliases are added or renamed. Or when IM
                                                and Presence nodes are added or renamed, or new TLS phone security profiles are added. You must produce a new Expressway-E certificate if new chat node aliases are added to the system, or if the Unified CM or
                                                XMPP federation domains are modified. You must restart the Expressway for any new uploaded server certificate to take effect. |
|---|---|