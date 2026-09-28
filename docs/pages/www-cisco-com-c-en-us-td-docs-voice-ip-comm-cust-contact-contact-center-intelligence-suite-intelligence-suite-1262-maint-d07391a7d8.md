---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1262-maint-d07391a7d8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1262/maintain_and_operate/guide/cuic_b_1262-admin-console-user-guide/cuic_m_1262-unrestricted-resource-access.html
retrieved_at: 2026-08-21T04:40:42.922765+00:00
---

Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(2)

# Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(2)

Updated: April 28, 2023

Chapter: Unrestricted Resource Access

## Chapter: Unrestricted Resource Access

- Unrestricted Resource Access

- Unrestricted Resource Access

# Unrestricted Resource Access

## Unrestricted Resource Access

Cisco Unified Intelligence Center allows unrestricted access to the following resources and API endpoints:

Resource

Path

JavaScript Files

/cuicui/scripts/*", "/cuicui/js/*", "/gadgets/report/js/*

Style sheets

/cuicui/css/*", "/cuicui/gadgets/report/css/*

Images

/cuicui/images/*

API endpoints to get the information regarding locales supported by Cisco Unified Intelligence Center

/cuicui/api/i18n/*

/cuicui/api/locales/

/cuic/rest/locales/*

API endpoints to check if Cisco Unified Intelligence Center server is online

/cuicui/api/status/*

/cuic/rest/status/*

CORS pre-flight request for all REST API endpoints

/cuic/*"[OPTIONS (http method)]"

API endpoint to retrieve the list of sessions that are active in Cisco Unified Intelligence Center

/cuic/rest/usersessiondetail/*

API endpoint to retrieve the list of drf schedules

/cuic/rest/genericservices/drf/*

| Resource | Path |
|---|---|
| JavaScript Files | /cuicui/scripts/*", "/cuicui/js/*", "/gadgets/report/js/* |
| Style sheets | /cuicui/css/*", "/cuicui/gadgets/report/css/* |
| Images | /cuicui/images/* |
| API endpoints to get the information regarding locales supported by Cisco Unified Intelligence Center | /cuicui/api/i18n/* /cuicui/api/locales/ /cuic/rest/locales/* |
| API endpoints to check if Cisco Unified Intelligence Center server is online | /cuicui/api/status/* /cuic/rest/status/* |
| CORS pre-flight request for all REST API endpoints | /cuic/*"[OPTIONS (http method)]" |
| API endpoint to retrieve the list of sessions that are active in Cisco Unified Intelligence Center | /cuic/rest/usersessiondetail/* |
| API endpoint to retrieve the list of drf schedules | /cuic/rest/genericservices/drf/* |