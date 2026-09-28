---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-configurationguid-f1e8ce5357
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/ConfigurationGuideCVP12_6/guide/ccvp_b_1261-configuration-guide-for-cisco-unified-customer-voice-portal/appendix-3.html
retrieved_at: 2026-08-21T06:54:10.129184+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: June 11, 2024

Chapter: New Properties for WXM, VAV, Agent Answers, and Smart Licensing

## Chapter: New Properties for WXM, VAV, Agent Answers, and Smart Licensing

- New Properties for WXM, VAV, Agent Answers, and Smart Licensing

# New Properties for WXM, VAV, Agent Answers, and Smart Licensing

## Webex Experience Management

```
SIP.CloudCherry.SurveyValidityTime = 60000
SIP.CloudConnect.SurveyDispatchEndPointApi = /cherrypoint/surveydispatch
```

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