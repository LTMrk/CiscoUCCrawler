---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cucm-security-12-5-1su2-cucm-b-security-guide-1251su2-cucm-b-security-guide--0609bfa04d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cucm/security/12_5_1SU2/cucm_b_security-guide-1251SU2/cucm_b_security-guide-1251SU2_chapter_011101.html
retrieved_at: 2026-08-21T08:39:58.963490+00:00
---

Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

# Security Guide for Cisco Unified Communications Manager, Release 12.5(1)SU2

Updated: March 22, 2024

Chapter: Certificate Monitoring Overview

## Chapter: Certificate Monitoring Overview

- Certificate Monitoring Overview

- Certificate Monitoring Configuration

# Certificate Monitoring Overview

Administrators must be able to track and renew certificates when Unified Communications Manager and IM and Presence Service services contain automated systems. Certificate Monitoring helps administrators know the certificate status on an ongoing
                           basis and email you when a certificate is approaching expiration.

## Certificate Monitoring Configuration

The Cisco Certificate Expiry Monitor network service must be running. By default, this service is enabled, but you can confirm
                              if the service is running in Cisco Unified Serviceability application by choosing Tools > Control Center - Network Services and verifying that the Cisco Certificate Expiry Monitor Service status is Running .

Step 1

From the Cisco Unified OS Administration, Choose Security > Certificate Monitor

Step 2

Enter or choose the configuration details.

Step 3

Click Save to save the configuration.

By default, the certificate monitor service runs once every 24 hours. When you restart the certificate monitor service, it
                                                      starts the service and then calculates the next schedule to run only after 24 hours. The interval doesn't change even when
                                                      the certificate is close to the expiry date of seven days. It runs every one hour when the certificate either has expired
                                                      or is going to expire in one day.

| Step 1 | From the Cisco Unified OS Administration, Choose Security > Certificate Monitor |
|---|---|
| Step 2 | Enter or choose the configuration details. |
| Step 3 | Click Save to save the configuration. Note By default, the certificate monitor service runs once every 24 hours. When you restart the certificate monitor service, it
                                                      starts the service and then calculates the next schedule to run only after 24 hours. The interval doesn't change even when
                                                      the certificate is close to the expiry date of seven days. It runs every one hour when the certificate either has expired
                                                      or is going to expire in one day. | Note | By default, the certificate monitor service runs once every 24 hours. When you restart the certificate monitor service, it
                                                      starts the service and then calculates the next schedule to run only after 24 hours. The interval doesn't change even when
                                                      the certificate is close to the expiry date of seven days. It runs every one hour when the certificate either has expired
                                                      or is going to expire in one day. |
| Note | By default, the certificate monitor service runs once every 24 hours. When you restart the certificate monitor service, it
                                                      starts the service and then calculates the next schedule to run only after 24 hours. The interval doesn't change even when
                                                      the certificate is close to the expiry date of seven days. It runs every one hour when the certificate either has expired
                                                      or is going to expire in one day. |

| Note | By default, the certificate monitor service runs once every 24 hours. When you restart the certificate monitor service, it
                                                      starts the service and then calculates the next schedule to run only after 24 hours. The interval doesn't change even when
                                                      the certificate is close to the expiry date of seven days. It runs every one hour when the certificate either has expired
                                                      or is going to expire in one day. |
|---|---|