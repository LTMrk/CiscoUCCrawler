---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-fd52357247
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_uninitialize-api_1501.html
retrieved_at: 2026-08-21T16:48:58.185121+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Uninitialize API

## Chapter: Uninitialize API

- Uninitialize API

- Uninitialize                              	 API

# Uninitialize API

## Uninitialize
                        	 API

Use this API to roll
                           		back the changes made by the Initialization API to the system only if an
                           		initialization task is in the FAILED state.

- Start reversion process of
                              		  initialization tasks which are in a state of SUCCEEDED or FAILED.

- Check the initialization
                              		  status of the system using Initialization API.

### URL

### Operations

list :
                                    				Lists information about the system uninitialization status.

update :
                                    				Starts a system uninitialization.

### Parameters

initializationStatus: The name of the startup task.

state: The
                                    				state of the task. Values include PROCESSING, FAILED, FAILED_NEEDS_RETRY, or
                                    				SUCCEEDED.

Tasks in the FAILED_NEEDS_RETRY state do not require roll-back
                                    				using the Uninitialize API.

### Example GET
                              		  Response

```
<results>
    <state>SUCCEEDED</state>
    <initializationStatuses>
        <initializationStatus><state>SUCCEEDED</state><name>SetProcessingStateTask</name>
        </initializationStatus>
        <initializationStatus><state>SUCCEEDED</state><name>SqlUserTask_sideA</name>
        </initializationStatus>
        <initializationStatus><state>SUCCEEDED</state><name>SqlUserTask_sideB</name>
        </initializationStatus>
        <initializationStatus><state>SUCCEEDED</state><name>DatabaseTask_sideA</name>
        </initializationStatus>
        <initializationStatus><state>SUCCEEDED</state><name>JtapiClientTask_sideA</name>
        </initializationStatus>
        <initializationStatus><state>SUCCEEDED</state><name>InstanceTask</name>
        </initializationStatus>
        <initializationStatus><state>SUCCEEDED</state><name>PGUserTask</name>
        </initializationStatus>
        <initializationStatus><state>SUCCEEDED</state><name>DatabaseTask_sideB</name>
        </initializationStatus>
        <initializationStatus><state>SUCCEEDED</state><name>JtapiClientTask_sideB</name>
        </initializationStatus>
    </initializationStatuses>
</results>
```