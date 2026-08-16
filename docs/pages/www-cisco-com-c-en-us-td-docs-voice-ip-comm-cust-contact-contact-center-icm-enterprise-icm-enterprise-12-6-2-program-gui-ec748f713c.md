---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-12-6-2-program-gui-ec748f713c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_12_6_2/program/guide/ucce_b_cisco-ucce_developer_guide-12-6-2-/ucce_m_congestion_control_api-12_6_1.html
retrieved_at: 2026-08-16T20:19:57.233120+00:00
---

Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

# Cisco Unified Contact Center Enterprise Developer Reference, Release 12.6(2)

Updated: August 21, 2023

Chapter: Congestion Control API

## Chapter: Congestion Control API

- Congestion Control API

- Congestion Control                              	 API

# Congestion Control API

## Congestion Control
                        	 API

Congestion control parameters determine how calls are treated
                           		by the system when too many calls are received at one time. Use the Congestion
                           		Control API to list or edit the current congestion control parameters in the
                           		database.

### URL

### Operations

get :
                                    				Returns the congestion control parameters, using the URL https://<server>/unifiedconfig/config/congestioncontrol .

update :
                                    				Updates the congestion control parameters.

### Parameters

deploymentType: The type of deployment.

congestionEnabled: Indicates if congestion control is enabled.
                                    				Value is true/false.

congestionTreatmentMode: Mode to handle congestion. Values are:

1: Dialed
                                          					 Number default label is used for call treatment.

2: Treat
                                          					 call with Routing client default label.

3: Treat
                                          					 call with System default label.

4:
                                          					 Terminate with Dialog Fail/RouteEnd.

5: Release
                                          					 message to the Routing client.

systemDefaultLabel: Default label string to treat the calls
                                    				subjected to congestion control. Only used if congestionTreatmentMode is set to
                                    				3 (Treat call with System default label).

cpsCapacity:
                                    				The maximum number of calls per second allowed.

cpsCapacityDefault: The default value for the cpsCapacity
                                    				parameter for the current deployment type. Read-only.

### Example Get
                              		  Response

```
<congestionControl>
      <deploymentType>0</deploymentType>
      <congestionTreatmentMode>1</congestionTreatmentMode>
      <congestionEnabled>true</congestionEnabled>
      <systemDefaultLabel></systemDefaultLabel>
      <cpsCapacity>100</cpsCapacity>
      <cpsCapacityDefault>150</cpsCapacityDefault>
</congestionControl>
```