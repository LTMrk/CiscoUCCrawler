---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-3c2baaf683
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_active-directory-domain-api_1501.html
retrieved_at: 2026-08-21T16:42:37.038924+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Active Directory Domain AP

## Chapter: Active Directory Domain AP

- Active Directory Domain AP

- Active Directory Domain API

# Active Directory Domain AP

## Active Directory Domain API

Use the Active Directory Domain API to list the active directory domains currently defined in your call center environment.
                           It is read-only, and does not require authentication.

### URL

### Operations

list : Retrieves a list of active directory domains.

### Parameters

name: The name of the domain.

### Example List Response

```
<results>
  <activeDirectoryDomains>
    <activeDirectoryDomain>
       <name>boston.com</name>
							
    </activeDirectoryDomain>
    <activeDirectoryDomain>
       <name>cisco.com</name>
							
    </activeDirectoryDomain>
  </activeDirectoryDomains>
</results>
```