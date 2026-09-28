---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-release-gui-34c9a13d84
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/release/guide/rcct_b_cce-solutions-rns-12-6-2/rcct_m_introduction-12-6-2.html
retrieved_at: 2026-08-16T19:37:16.069072+00:00
---

Release Notes for Cisco Contact Center Enterprise Solutions, Release 12.6(2)

# Release Notes for Cisco Contact Center Enterprise Solutions, Release 12.6(2)

Updated: February 27, 2026

Chapter: Introduction

## Chapter: Introduction

# Introduction

## Release Notes for Contact Center Enterprise Solutions

These release notes describe new and updated features and other changes for Release 12.6(2) of the following contact center solutions and their components:

Cisco Unified Contact Center Enterprise

Cisco Packaged Contact Center Enterprise

Information in this document applies to the contact center solutions listed above, except where otherwise noted.

## Cisco Security
                        	 Advisories

The Cisco Product Security Incident Response Team (PSIRT) is a dedicated, global team that manages the receipt, investigation,
                              and public reporting of security vulnerability information that relates to Cisco products and networks.

For information on
                              		  existing security issues, see Cisco
                                 			 Security Advisories, Responses, and Alerts at https://tools.cisco.com/security/center/publicationListing.x .

## Contact Center Enterprise Software Release Delivery Model

Cisco introduces a new software release delivery model for Contact Center Enterprise products. Contact Center Enterprise issues
                           two types of releases:

Long Term Release (LTR)

Dynamic Release (DR)

We recommend the LTR delivery model if you prefer infrequent upgrade cycles over faster adoption of new features. This model
                           includes support for bug fixes through engineering specials.

We recommend the DR delivery model if you want faster feature adoption. With this model, both new feature and bug fixes are
                           delivered through engineering specials and maintenance releases. This model also offers simplified patch upgrades through
                           automated notification, orchestrated patch application, and minimal downtime.

For more information about the new delivery models, see the product bulletin Cisco's Contact Center Enterprise Software Release and Sustaining Lifecycle .

Release 12.6 is a dynamic release and will follow the sustaining process as outlined in this product bulletin.

## Multi-server SAN Certificates

Multi-server Subject Alternate Name (SAN) certificates are supported by the following solution components: Cisco Finesse,
                           Cisco Unified Intelligence Center (CUIC), Live Data, IdS, and Cisco Virtualized Voice Browser (VVB).

For more information, see Configuration of CA-Signed Multi-Server Subject Alternate Name in CVOS Systems .

## Important Notes

SSO Deployments upgrading to 12.6(2) should ensure that Reverse Proxy Installer (for VPN-Less deployments) 12.6(2) ES02 or
                                 later, followed by IdS 12.6(2) ES02 or later, is installed before upgrading any of the components like Cisco Finesse/CUIC
                                 to 12.6.(2).

For 2K Co-Res Deployment model, CUIC, LD and CCE (Router, logger and AW) should be upgraded to in the same maintenance window.