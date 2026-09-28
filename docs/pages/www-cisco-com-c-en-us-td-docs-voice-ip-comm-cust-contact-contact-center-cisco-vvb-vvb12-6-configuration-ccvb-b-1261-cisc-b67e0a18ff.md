---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb12-6-configuration-ccvb-b-1261-cisc-b67e0a18ff
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb12_6/configuration/ccvb_b_1261-ciscovvb-administrationconfiguration-guide/appendix-1.html
retrieved_at: 2026-08-21T16:29:47.591527+00:00
---

Cisco Virtualized Voice Browser Administration and Configuration Guide, Release 12.6(1)

# Cisco Virtualized Voice Browser Administration and Configuration Guide, Release 12.6(1)

Updated: May 14, 2021

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