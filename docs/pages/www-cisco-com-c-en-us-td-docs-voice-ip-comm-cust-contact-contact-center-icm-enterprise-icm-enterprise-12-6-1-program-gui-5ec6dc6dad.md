---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-1-program-gui-5ec6dc6dad
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_1/program/guide/ucce_b_cisco-ucce_developer_guide-12_6_1/ucce_b_cisco-ucce_developer_guide-12_6_1_chapter_010.html
retrieved_at: 2026-08-16T20:21:37.497023+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(1)

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