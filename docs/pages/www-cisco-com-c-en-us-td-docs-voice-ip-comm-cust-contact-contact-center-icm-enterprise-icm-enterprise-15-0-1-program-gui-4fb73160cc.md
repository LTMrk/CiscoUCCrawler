---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-4fb73160cc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_instance-api_1501.html
retrieved_at: 2026-08-21T16:46:56.432836+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Instance API

## Chapter: Instance API

- Instance API

- Instance                              	 API

# Instance API

## Instance
                        	 API

The Instance API is used during a Packaged CCE installation to select
                           		the name of the facility and instance for the deployment.

### URL

### Operations

create :
                                    				Creates one instance. Only one instance can be created.

delete :
                                    				Deletes one instance.

get :
                                    				Returns one instance, using the URL https://<server ip
                                       				  address>/unifiedconfig/config/instance/1 .

list :
                                    				Retrieves the instance from the database.

update :
                                    				Updates one instance.

The user performing the operation must be in the setup group for the
                                          			 instance Organizational Unit that is specified.

### Parameters

refURL: The refURL of the instance. See Shared Parameters .

facilityName: Name of an existing facility Organizational Unit in Active Directory.

instanceName: Name of an existing instance Organizational Unit in Active Directory.

### Example Get Response

```
<instance>
   <refURL>/unifiedconfig/config/instance/1</refURL>
   <facilityName>Lab</facilityName>
   <instanceName>pcce</instanceName>
</instance>
```

| Note | The user performing the operation must be in the setup group for the
                                          			 instance Organizational Unit that is specified. |
|---|---|