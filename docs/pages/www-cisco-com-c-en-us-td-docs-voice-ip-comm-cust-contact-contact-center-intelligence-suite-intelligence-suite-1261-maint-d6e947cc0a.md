---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-intelligence-suite-intelligence-suite-1261-maint-d6e947cc0a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/intelligence_suite/intelligence_suite_1261/maintain_and_operate/guide/cuic_b_1261-admin-console-user-guide/cuic_m_1261-unrestricted-resource-access.html
retrieved_at: 2026-10-19T10:07:42.664349+00:00
---

Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(1)

# Administration Console User Guide for Cisco Unified Intelligence Center, Release 12.6(1)

Updated: May 14, 2021

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

## Figuras

![login required](https://www.cisco.com/etc/designs/cdc/fw/i/icon_lock_small.png)