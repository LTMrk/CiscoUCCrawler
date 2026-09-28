---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-reference-guide-c-a7f2bdb7fc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/reference/guide/ccvp_b_1251-element-specification-guide-cvp/cvp-esguide-subflow-return.html
retrieved_at: 2026-08-21T17:30:57.919574+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

Updated: January 31, 2020

Chapter: Subflow Return

## Chapter: Subflow Return

- Subflow Return

- Subflow                              	 Return

# Subflow Return

## Subflow
                        	 Return

The Subflow Return element is the exit point for the subflow processing. The Subflow Return element returns the call flow control back to the Call Subflow element. Subflow Return element has no exit state as it is
                           the last element in the subflow processing. The Subflow Return element is used to returned data configured to a calling application. Subflow Return Element uses a data model to save its
                           configuration which is implemented in the SubflowReturnConfig class. The Element configuration view displays the configuration of Subflow Return element implemented in SubflowReturnDataPage class which extends BaseConfigPage class. The Subflow Return Data is available in the Element Configuration view. Subflow Call element allows to accept multiple
                           return values of different types from a subflow.