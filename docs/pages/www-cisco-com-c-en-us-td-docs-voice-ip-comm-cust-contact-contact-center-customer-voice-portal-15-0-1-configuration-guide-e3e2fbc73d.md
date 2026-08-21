---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-configuration-guide-e3e2fbc73d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/configuration/guide/ccvp_b_150-configuration-guide-for-cisco-unified-customer-voice-portal/appendix-1.html
retrieved_at: 2026-08-21T03:00:07.691730+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: March 5, 2025

Chapter: FIPS Update

## Chapter: FIPS Update

- FIPS Update

# FIPS Update

You can run the new batch file fips.bat located in the %CVP_HOME%/bin/FipsConfig folder with the argument true to enable many FIPS 140-2 like settings in the product. However, the product is not yet certified to be FIPS 140-2 compliant.
                        The changes leverage FIPS-compliant libraries (FOM) of BouncyCastle. These changes are applied to the security provider list
                        in the JRE, keystore format, ciphers supported, algorithms used, etc.