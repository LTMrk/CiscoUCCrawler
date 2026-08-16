---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-f4e427a5cc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5_chapter_01.html
retrieved_at: 2026-08-16T20:25:27.603008+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

Updated: February 6, 2020

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