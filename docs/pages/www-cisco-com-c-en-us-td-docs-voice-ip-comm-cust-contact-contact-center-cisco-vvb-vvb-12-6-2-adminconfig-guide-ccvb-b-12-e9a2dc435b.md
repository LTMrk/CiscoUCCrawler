---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-12-6-2-adminconfig-guide-ccvb-b-12-e9a2dc435b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb_12_6_2/adminconfig/guide/ccvb_b_1262-ciscovvb-administrationconfiguration-guide/appendix-1.html
retrieved_at: 2026-08-21T16:29:25.714042+00:00
---

Cisco Virtualized Voice Browser Administration and Configuration Guide, Release 12.6(2)

# Cisco Virtualized Voice Browser Administration and Configuration Guide, Release 12.6(2)

Updated: April 28, 2023

Chapter: FIPS Update

## Chapter: FIPS Update

- FIPS Update

# FIPS Update

You can run the new CLI command utils fips enable to enable many FIPS 140-2 like settings in the product. However, this is not certified yet to be compliant. Changes leverage
                        FIPS-compliant libraries of BCFIPS and include them to the security provider list in the JRE, keystore format, ciphers supported,
                        algorithms used, etc.

If AppDynamics monitoring is enabled, disable it before enabling FIPS mode.

| Note | If AppDynamics monitoring is enabled, disable it before enabling FIPS mode. |
|---|---|