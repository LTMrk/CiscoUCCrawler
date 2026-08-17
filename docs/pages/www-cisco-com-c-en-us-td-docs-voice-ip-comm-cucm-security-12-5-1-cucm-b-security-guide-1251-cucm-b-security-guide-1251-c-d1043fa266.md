---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-security-12-5-1-cucm-b-security-guide-1251-cucm-b-security-guide-1251-c-d1043fa266
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/12_5_1/cucm_b_security-guide-1251/cucm_b_security-guide-1251_chapter_0100001.html
retrieved_at: 2026-08-17T03:58:48.876206+00:00
---

Security Guide for Cisco Unified Communications Manager, Release 12.5(1)

# Security Guide for Cisco Unified Communications Manager, Release 12.5(1)

Updated: February 24, 2025

Chapter: FIPS 140-2 Mode Setup

## Chapter: FIPS 140-2 Mode Setup

- FIPS 140-2 Mode Setup

- FIPS Mode Not Supported in Some 12.x Versions

# FIPS 140-2 Mode Setup

This chapter provides information about FIPS 140-2 mode setup.

## FIPS Mode Not Supported in Some 12.x Versions

FIPS mode is supported with 12.5(1)SU1. However, FIPS mode is not supported with Releases 12.0(x) and 12.5(1) of Cisco Unified Communications Manager and the IM and Presence Service . If you are upgrading from an earlier release with FIPS mode, Enhanced Security Mode, or Common Criteria Mode enabled, you
                              must disable them prior to the upgrade to these releases, or upgrade to 12.5(1)SU1 instead. TFTP and other services will not
                              work in 12.0(x) or 12.5(1) with FIPS mode enabled.