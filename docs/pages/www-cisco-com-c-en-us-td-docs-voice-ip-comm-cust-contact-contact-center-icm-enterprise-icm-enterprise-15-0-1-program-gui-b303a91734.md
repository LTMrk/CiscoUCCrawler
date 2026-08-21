---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-b303a91734
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_deployment-_api_1501.html
retrieved_at: 2026-08-21T16:46:18.892314+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

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

deploymentType: The type of deployment. See Deployment Type Info API .

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