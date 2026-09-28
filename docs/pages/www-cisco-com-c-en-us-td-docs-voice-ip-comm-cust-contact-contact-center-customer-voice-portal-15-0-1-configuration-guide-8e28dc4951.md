---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-configuration-guide-8e28dc4951
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/configuration/guide/ccvp_b_150-configuration-guide-for-cisco-unified-customer-voice-portal/appendix-3.html
retrieved_at: 2026-08-21T03:00:16.063594+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: March 5, 2025

Chapter: New Properties for WXM, VAV, Agent Answers, and Smart Licensing

## Chapter: New Properties for WXM, VAV, Agent Answers, and Smart Licensing

- New Properties for VAV, Agent Answers, and Smart Licensing

# New Properties for VAV, Agent Answers, and Smart Licensing

## VAV Onboarding

```
IVR.CcaiOrgUrl = /cloudconnectmgmt/config
IVR.CcaiConfigUrl = cms/api/auxiliary-data/resources/ccai-config
IVR.CcaiCredentialUrl = _config/organization/%s/credentials/%s/access-token
IVR.CcaiCatalogUrl = /u2c/api/v1/user/catalog
IVR.CcaiConfigFlushTimeoutInMinutes = 60
```

## Agent Answers

```
SIP.CloudConnect.AgentAssistAuthTokenApi = /cloudconnectmgmt/token
SIP.CloudConnect.AgentAssistAuthTokenScopes = cjp-ccai:read,cjp-ccai:write
SIP.MediaForking.DestinationUrl = 
SIP.UseSecureMediaForking = true
SIP.MediaForking.DestinationPort = 443
SIP.UseSIPINFOForking = true
SIP.CloudConnect.AgentAssistAuthTokenRefreshRateInPercent = 10
```

## Smart Licensing

```
SL.eventLogPath = C:/Cisco/CVP/logs/WSM
SL.eventLogMaxSize = 1000000
```