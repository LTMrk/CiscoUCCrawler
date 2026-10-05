---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb-15-0-1-adminconfig-guide-ccvb-b-15-f5bcada2ac
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb_15_0_1/adminconfig/guide/ccvb_b_150_cisco-virtualized-voice-browser-administration-and-configuration-guide/appendix-1.html
retrieved_at: 2026-10-05T11:29:11.386142+00:00
---

Cisco Virtualized Voice Browser Administration and Configuration Guide, Release 15.0(1)

# Cisco Virtualized Voice Browser Administration and Configuration Guide, Release 15.0(1)

Updated: December 12, 2025

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

## Figuras

![Back to Top](https://www.cisco.com/etc/designs/cdc/fw/i/responsive/Default-bTop-36.svg)

![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)