---
doc_id: developer-cisco-com-site-extension-mobility-help-faq-483a7a5686
source_url: https://developer.cisco.com/site/extension-mobility/help/faq/
retrieved_at: 2026-08-25T21:05:14.424856+00:00
---

# Extension Mobility API FAQs

- Where do I post the XML request to?

- What role is required for an application user to access the API and login other users?

- Which phones cannot be configured with Extension Mobility API?

Where do I post the XML request to?

Post the XML request from your application to https://<server>:8443/emservice/EMServiceServlet where <server> is the CUCM domain name or IP address.

What role is required for an application user to access the API and login other users?

The minimum permissions are:

- Standard EM Authentication Proxy Rights - this grants access to the UCM web services. Note, it does not grant full admin access.

Which phones cannot be configured with Extension Mobility API?

The Extension Mobility APIs can be used on phones that support the Extension Mobility service. You can go to the Unified CM Phone Feature List on Cisco Unified Reporting to lookup the supported features of you phones.

Back to Top

Visit the Extension Mobility API Developer Forums to ask questions and interact with other developers.

Forums

## Bug Search Tool

Use the Bug Search Tool to find information about software issues.

Search Bugs