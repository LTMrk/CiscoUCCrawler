---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-dab255f8f1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_deployment-_type_-api_1501.html
retrieved_at: 2026-08-21T16:46:23.222306+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Deployment Type API

## Chapter: Deployment Type API

- Deployment Type API

- Deployment Type                              	 Info API

# Deployment Type API

## Deployment Type
                        	 Info API

Use the Deployment
                           		Type Info API to view or edit the current system deployment type.

### URL

### Operations

get :
                                    				Returns the current deployment type and the results of the capacity and system
                                    				validation tests, using the URL https://<server>/unifiedconfig/config/deploymenttypeinfo .

update :
                                    				Sets the specified deployment type if the system validation check, capacity
                                    				check, and VM Validation for that deployment type pass and are required.

### Parameters

changeStamp:
                                    				See Shared Parameters .

vmHosts:
                                    				vmHost information, including name, address, username, and password parameters
                                    				of Side A and Side B. Only required when switching to Packaged CCE, to allow
                                    				access to the ESX servers for VM validation.

permissionInfo: See Permissions .

systemValidationStatus: See Serviceability API .

capacityInfo:
                                    				See Serviceability API .

vmLayoutType:
                                    				Represents the current deployment type and hardware.

vmValidationLogURL: The URL to download a file about VM layout validation.

deploymentType: The type of deployment. The following types are
                                    				supported:

0: No
                                          					 deployment type specified. Initial type set at installation. Once set to
                                          					 another deployment type, you cannot switch back to 0.

2: Contact
                                          					 Director

6: UCCE:
                                          					 12000 Agents Router/Logger

7: Packaged CCE: 2000 Agents

9: UCCE:
                                          					 4000 Agents Rogger

10:
                                          					 Packaged CCE: Lab Mode

13: UCCE:
                                          					 Progger (Lab Only)

16: UCCE: 2000 Agents

17: Packaged CCE: 4000 Agents

18: Packaged CCE: 12000 Agents

19: UCCE: 24000 Agents Router/Logger

targetDeploymentType: Indicates which deployment type is being
                                    				initialized.

hardwareLayoutType: Indicates the hardware layout types - Tested Reference
                                    				Configuration (TRC) or Specification based hardware (SPEC). This is an optional
                                    				parameter. If the hardware type is not specified, the system takes TRC by
                                    				default.

### Example Get
                              		  Response

```
<deploymentTypeInfo>
  <changeStamp>59</changeStamp>
  <deploymentType>7</deploymentType> <vmLayoutType>PCCE_C240M3_Full</vmLayoutType> <vmHosts>
    <vmHost>
      <name>sideA</name>
      <address>10.86.141.10</address>
      <userName>root</userName>
    </vmHost>
    <vmHost>
      <name>sideB</name>
      <address>10.86.141.29</address>
      <userName>root</userName>
      <password>pwexample</password>
    </vmHost>
  </vmHosts>
</deploymentTypeInfo>
```