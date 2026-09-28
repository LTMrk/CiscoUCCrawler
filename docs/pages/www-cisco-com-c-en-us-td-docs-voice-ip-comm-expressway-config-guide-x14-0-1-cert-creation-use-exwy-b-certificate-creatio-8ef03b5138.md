---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-expressway-config-guide-x14-0-1-cert-creation-use-exwy-b-certificate-creatio-8ef03b5138
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/config_guide/X14-0-1/cert_creation_use/exwy_b_certificate-creation-and-use-deployment-guide-x1401/exwy_b_certificate-creation-use-deployment-guide_chapter_01000.html
retrieved_at: 2026-08-16T15:24:29.827955+00:00
---

Cisco Expressway Certificate Creation and Use Deployment Guide (X14.0.1)

# Cisco Expressway Certificate Creation and Use Deployment Guide (X14.0.1)

Updated: July 1, 2021

Chapter: Troubleshooting

## Chapter: Troubleshooting

# Troubleshooting

## SIP TLS Negotiation Failures on Neighbor and Traversal Zones

If TLS verify mode is enabled, the neighbor system's FQDN or IP address, as specified in the Peer address field of the zone’s configuration, is used to verify against the certificate holder’s name in the X.509 certificate presented
                           by that system. (The name must be in the SAN attribute of the certificate.) The certificate itself must also be valid and
                           signed by a trusted certificate authority.

So when certificates have been generated with peer or cluster FQDNs, ensure that the zone's Peer address fields are configured with FQDNs rather than IP addresses.

## Certificates with Key Length of 8192 Bits

SIP TLS zones may fail to become active if certificates use a key length of 8192 bits. We recommend using certificates with
                           a key length of 4096 bits.

## Service Failures when Using Mobile and Remote Access

Unified Communications mobile and remote access services can fail due to certificate errors if you upload a private key file
                           that does not contain a trailing newline character.

Ensure that the private key file contains a trailing newline character.

## Issues with SSH Failures and Unsupported OIDs

If you experience unknown ssh failures such as ssh tunnels failing to establish, please verify there are no unknown OIDs in
                           the certificate. This can be done by checking that there are no undecoded numerical entries in the CN of the Issuer & Subject
                           fields (from the GUI: Maintenance > Security > Server Certificate > Show(decoded) or from the console: 'openssl x509 –text –noout –in /tandberg/persistent/certs/server.pem’)

Invalid

subject=CN=blahdeblah,OU=IT

Security,O=BigBang,L=Washington,ST=District of

Columbia,C=US,1.3.6.1.4.1.6449.1.2.1.5.1 = #060C2B06010401B2310102010501

Valid

subject=CN=blahdeblah,OU=IT

Security,O=BigBang,L=Washington,ST=District of

Columbia,C=US,jurisdictionOfIncorporationLocalityName=Dover