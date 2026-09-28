---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-program-gui-7bdbfef3c6
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/program/guide/ucce_b_cisco-ucce_developer_guide-12-6-2-/ucce_m_deployment_api-12_6_1.html
retrieved_at: 2026-08-16T20:20:18.436176+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

Updated: August 21, 2023

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