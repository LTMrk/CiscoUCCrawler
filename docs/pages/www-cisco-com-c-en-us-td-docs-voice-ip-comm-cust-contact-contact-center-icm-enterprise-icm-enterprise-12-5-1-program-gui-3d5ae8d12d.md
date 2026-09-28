---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-5-1-program-gui-3d5ae8d12d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_5_1/program/guide/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5/ucce_b_cisco-unified-contact-center-enterprise_developer_guide_12_5_chapter_01111.html
retrieved_at: 2026-08-16T20:28:23.538098+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.5(1)

Updated: February 6, 2020

Chapter: Deployment Type Info API

## Chapter: Deployment Type Info API

- Deployment Type Info API

- Deployment Type                              	 Info API

# Deployment Type Info API

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

systemValidationStatus: A collection of validationRules that
                                    				show the potential errors regarding system configuration. Each rule contains
                                    				the following parameters:

name: The
                                          					 name of the rule.

isValid:
                                          					 Indicates if the rule is passing. Values are true/false.

min:
                                          					 The minimum number of items required to match for this rule.

max: The
                                          					 maximum number of items required to match for this rule.

actual:
                                          					 The current number of items configured that match this rule.

capacityInfo:
                                    				A collection of capacityRules indicating if the capacity limits are valid. Each
                                    				rule contains the following parameters:

name:
                                          					 The name of the capacity rule.

max: The
                                          					 maximum number of items allowed for the rule.

actual:
                                          					 The current number of items configured for the rule.

vmValidationLogURL: The URL to download a file about VM layout validation.

deploymentType: The type of deployment. The following types are
                                    				supported:

0: No
                                          					 deployment type specified. Initial type set at installation. Once set to
                                          					 another deployment type, you cannot switch back to 0.

1: NAM
                                          					 (Deprecated)

2: Contact
                                          					 Director

3: NAM
                                          					 Rogger (Deprecated)

4: ICM
                                          					 Router/Logger

5: UCCE:
                                          					 8000 Agents Router/Logger

6: UCCE:
                                          					 12000 Agents Router/Logger

7: Packaged CCE: 2000 Agents

8: ICM
                                          					 Rogger

9: UCCE:
                                          					 4000 Agents Rogger

10:
                                          					 Packaged CCE: Lab Mode

11:
                                          					 HCS-CC: 2000 Agents

12:
                                          					 HCS-CC: 500 Agents (Deprecated)

13: UCCE:
                                          					 Progger (Lab Only)

14:
                                          					 HCS-CC: 4000 Agents

15:
                                          					 HCS-CC: 12000 Agents

16: UCCE: 2000 Agents

17: Packaged CCE: 4000 Agents

18: Packaged CCE: 12000 Agents

19: UCCE: 24000 Agents Router/Logger

20: HCS-CC: 24000 Agents

You can only use Live Data on deployment types UCCE: 2000 Agents, UCCE: 4000 Agents Rogger, UCCE: 8000 Agents Router/Logger, UCCE: 12000 Agents Router/Logger, UCCE: 24000 Agents Router/Logger, HCS-CC: 2000 Agents, HCS-CC: 4000 Agents, HCS-CC: 12000 Agents, HCS-CC: 24000 Agents, Packaged CCE: 2000 Agents, Packaged CCE: 4000 Agents, Packaged CCE: 12000 Agents, and Packaged CCE: Lab Mode.

### Example Get
                              		  Response

```
<deploymentTypeInfo>
  <changeStamp>59</changeStamp>
  <deploymentType>7</deploymentType>
  
  <vmHosts>
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

| Note | You can only use Live Data on deployment types UCCE: 2000 Agents, UCCE: 4000 Agents Rogger, UCCE: 8000 Agents Router/Logger, UCCE: 12000 Agents Router/Logger, UCCE: 24000 Agents Router/Logger, HCS-CC: 2000 Agents, HCS-CC: 4000 Agents, HCS-CC: 12000 Agents, HCS-CC: 24000 Agents, Packaged CCE: 2000 Agents, Packaged CCE: 4000 Agents, Packaged CCE: 12000 Agents, and Packaged CCE: Lab Mode. |
|---|---|