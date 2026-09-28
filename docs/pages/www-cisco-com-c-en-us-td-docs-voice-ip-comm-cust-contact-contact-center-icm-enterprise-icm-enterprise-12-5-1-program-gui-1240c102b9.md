---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-1240c102b9
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5_chapter_01110.html
retrieved_at: 2026-08-16T20:28:19.205575+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

Updated: February 6, 2020

Chapter: Deployment API

## Chapter: Deployment API

- Deployment API

- Deployment                              	 API

# Deployment API

## Deployment
                        	 API

The Deployment API
                           		is used to view the deployment type of the installation. It is read-only, and
                           		does not require authentication. To change the deployment type, use the
                           		Deployment Type Info API.

### URL

### Parameters

deploymentType: The type of deployment.

supervisorLoginAllowed: Indicates whether the current deployment type allows supervisor login.

### Operations

get : Returns the deployment type of the installation using the URL https://<server>/unifiedconfig/config/deployment .

### Example Get
                              		  Response

```
<deployment>
     <deploymentType>7</deploymentType>
     <supervisorLoginAllowed>true</supervisorLoginAllowed>
</deployment>
```