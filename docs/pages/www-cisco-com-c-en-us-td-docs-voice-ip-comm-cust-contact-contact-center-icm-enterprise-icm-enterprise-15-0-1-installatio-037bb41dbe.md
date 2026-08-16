---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-installatio-037bb41dbe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/installation/guide/ucce_b_stagingguide_release_15_0_1/ucce_m_1261_local-machine-authorizations.html
retrieved_at: 2026-08-16T19:59:00.425651+00:00
---

Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 15.0(1)

# Staging Guide for Cisco Unified ICM/Contact Center Enterprise, Release 15.0(1)

Updated: March 24, 2025

Chapter: Local Machine Authorizations

## Chapter: Local Machine Authorizations

# Local Machine Authorizations

Unified CCE supports local authorization that does not involve any Domain security groups for user permissions. All the permissions
                        and privileges are handled by the security groups on the local machines.

## UcceService Group

This security group is created during the installation or upgrade process, in the local machines. The UcceService group applies to Fresh Installations as well as all upgrades including Technology Refresh and other supported upgrade paths
                           from an earlier releases.

The UcceService group is used to provide permissions and privileges to the service accounts associated with the Logger and Distributor services.
                           For a new installation, the domain service accounts for the Logger and Distributor services must be added to this group. All
                           the permissions required for the service accounts are configured for the UcceService group.

## UcceConfig Group

The UcceConfig group is created during the fresh installation in all local machines. For upgrades, this group already exists in local machines.
                           The UcceConfig group is required only for Distributor machines.

The UcceConfig group is used to provide local authorization with the necessary permissions and privileges to the Unified CCE configuration
                           users.

The permissions for registries and local folders must be configured manually. For steps to configure the permissions, see
                           the Configuration Guide for Cisco Unified ICM/Contact Center Enterprise .

## Local Administrators Group

Setup users are domain users with local administrator permissions and can run the UCCE installer, Websetup, and Peripheral
                           Gateway Setup tools.

To make a domain user a setup user, you have to manually add the domain user to the Local Administrators Group. This enables
                           the domain user to perform the UCCE setup operations such as, running the Websetup and Peripheral Gateway Setup tools.

Domain Administrators can perform UCCE setup operations such as, running the Websetup and Peripheral Gateway Setup tools.

| Note | Domain Administrators can perform UCCE setup operations such as, running the Websetup and Peripheral Gateway Setup tools. |
|---|---|