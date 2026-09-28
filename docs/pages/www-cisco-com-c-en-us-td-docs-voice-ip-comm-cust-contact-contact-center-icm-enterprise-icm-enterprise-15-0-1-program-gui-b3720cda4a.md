---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-b3720cda4a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_active-directory-domain-api_1501.html
retrieved_at: 2026-08-16T20:14:32.736613+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

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