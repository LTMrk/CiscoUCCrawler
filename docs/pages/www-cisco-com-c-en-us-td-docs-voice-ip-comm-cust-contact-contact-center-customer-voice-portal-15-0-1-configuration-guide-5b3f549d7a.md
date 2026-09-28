---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-configuration-guide-5b3f549d7a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/configuration/guide/ccvp_b_1501-configuration-guide-for-cisco-customer-voice-portal-release/appendix-1.html
retrieved_at: 2026-08-21T12:07:54.644895+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: December 12, 2025

Chapter: FIPS Update

## Chapter: FIPS Update

- FIPS Update

# FIPS Update

You can run the new batch file fips.bat located in the %CVP_HOME%/bin/FipsConfig folder with the argument true to enable many FIPS 140-2 like settings in the product. However, the product is not yet certified to be FIPS 140-2 compliant.
                        The changes leverage FIPS-compliant libraries (FOM) of BouncyCastle. These changes are applied to the security provider list
                        in the JRE, keystore format, ciphers supported, algorithms used, etc.