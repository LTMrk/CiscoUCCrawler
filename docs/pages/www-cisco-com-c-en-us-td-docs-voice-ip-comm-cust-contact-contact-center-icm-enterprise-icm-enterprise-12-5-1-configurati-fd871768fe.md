---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-configurati-fd871768fe
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/configuration/guide/ucce_b_serviceability-guide-for-cisco-unified12_5/ucce_m_serviceabilityforcloudconnect125.html
retrieved_at: 2026-08-16T14:50:23.054005+00:00
---

Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) and 12.5(2)

# Serviceability Guide for Cisco Unified ICM/Contact Center Enterprise, Release 12.5(1) and 12.5(2)

Updated: July 26, 2022

Chapter: Serviceability for Cloud Connect

## Chapter: Serviceability for Cloud Connect

- Serviceability for Cloud Connect

- Cloud Connect Serviceability

# Serviceability for Cloud Connect

## Cloud Connect Serviceability

Viewing the Internal state of CloudConnectMgmt container :

The below CLI Command will provide the internal status of the Cloud Connect’s CloudConnectMgmt
                           container.

show cloudconnect CloudConnectMgmt status

### Verifying the Cloud Connect Node status

The below status output segment indicates that both the Cloud Connect Node are in service.

```
"cluster": {
        "nodes": [
            {
                "address": "cconnectpub105.stooges.icm",
                "status": "MemberUp",
                "statusSince": 1585645270161,
                "statusUrl": "https://cconnectpub105.stooges.icm:8445/CloudConnectMgmt/status"
            },
            {
                "address": "cconnectsub105.stooges.icm",
                "status": "MemberUp",
                "statusSince": 1585645270161,
                "statusUrl": "https://cconnectsub105.stooges.icm:8445/CloudConnectMgmt/status"
            }
       ]
..
                "name": "DataStreamer",
                "status": "IN_SERVICE",
                "statusSince": 1585643943804,
                "streamer": "STARTED",
                "streamingEnabled": true
  }
```