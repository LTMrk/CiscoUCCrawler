---
doc_id: developer-cisco-com-docs-finesse-cors-support-for-finesse-rest-apis-d5cf726eaa
source_url: https://developer.cisco.com/docs/finesse/cors-support-for-finesse-rest-apis/
retrieved_at: 2026-09-07T14:06:48.229001+00:00
---

# CORS Support for
	 Finesse REST APIs

Cross-Origin Resource Sharing (CORS) is a verification mechanism that uses additional HTTP headers to let a user gain permission to access selected resources from a server on a different origin (domain) than the site currently in use. By default, CORS support is disabled for Cisco Finesse and Cisco Finesse Notification Service. The CORS support can be enabled by the Administrator for specific origins listed in the allowed origin list using CLIs. For more information see, Cisco Finesse Admin guide 12.0(1) located at https://www.cisco.com/c/en/us/support/customer-collaboration/finesse/products-user-guide-list.html . CORS requests that are originating from the allowed origin list will be honored as per CORS RFC.