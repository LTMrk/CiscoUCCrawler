---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-program-gui-f8df7c4ae2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/program/guide/ucce_b_cisco-ucce_developer_guide-12-6-2-/ucce_m_ad_domain_api-12_6_1.html
retrieved_at: 2026-08-16T20:19:15.287682+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

Updated: August 21, 2023

Chapter: Active Directory Domain API

## Chapter: Active Directory Domain API

- Active Directory Domain API

- Active Directory                              	 Domain API

# Active Directory Domain API

## Active Directory
                        	 Domain API

Use the Active
                           		Directory Domain API to list the active directory domains currently defined in
                           		your call center environment. It is read-only, and does not require
                           		authentication.

### URL

### Operations

list :
                                    				Retrieves a list of active directory domains.

### Parameters

name: The name
                                    				of the domain.

systemDomain:
                                    				Indicates if the system is a member of this domain. Values are true/false.

### Example List Response

```
<results>
  <activeDirectoryDomains>
    <activeDirectoryDomain>
       <name>boston.com</name> <systemDomain>true</systemDomain> </activeDirectoryDomain>
    <activeDirectoryDomain>
       <name>cisco.com</name> <systemDomain>false</systemDomain> </activeDirectoryDomain>
  </activeDirectoryDomains>
</results>
```