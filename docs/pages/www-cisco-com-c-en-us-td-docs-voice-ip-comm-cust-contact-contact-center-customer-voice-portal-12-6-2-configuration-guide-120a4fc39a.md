---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-configuration-guide-120a4fc39a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/configuration/guide/ccvp_b_1262-configuration-guide-for-cisco-unified-customer-voice-portal/appendix-2.html
retrieved_at: 2026-08-21T11:58:59.893417+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(2)

Updated: April 28, 2023

Chapter: Internal REST API Endpoints

## Chapter: Internal REST API Endpoints

- Internal REST API Endpoints

# Internal REST API Endpoints

Following authenticated REST API endpoints are exposed for internal invocation from within the solution. These REST API endpoints
                        are listed for information purposes only, and not intended for external consumption currently. If you have a valid use case
                        to know more, please get in touch with the product team.

```
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/sipservergroup
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/sipservergroup/properties
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/location
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/location/properties
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/dialednumber
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/routepattern
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/cvpconfig
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/cloudconnectconfig
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/callserver/associatereporting
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/reporting/associatecallservers
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/reporting/deploy
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/reporting/undeploy
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/callserver/deassociatereporting
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/vxmlapplications
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/cvpconfig/properties
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/stats
https://<CVP_HOSTNAME_OR_IP>:8111/cvp-orm/rest/smartlicense/smartlicenseinfo
```