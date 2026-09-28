---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-7b18a7f9a8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/ucce_b_cisco-unified-contact-center-enterprise-developer-reference-release-15-0/ucce_m_deployment-type-info-api_1501.html
retrieved_at: 2026-08-16T20:17:46.174974+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: December 10, 2025

Chapter: Deployment Type Info API

## Chapter: Deployment Type Info API

- Deployment Type Info API

- Deployment                              	 API

# Deployment Type Info API

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