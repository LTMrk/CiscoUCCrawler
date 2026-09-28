---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-d92498253c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_initialize-api_1501.html
retrieved_at: 2026-08-21T16:46:52.644429+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Initialize API

## Chapter: Initialize API

- Initialize API

- Initialize                              	 API

# Initialize API

## Initialize
                        	 API

The initialize API serves as an entry point for Packaged CCE system setup. It allows you to:

Start setup tasks for system configuration.

Check the initialization status of the system.

### URL

### Operations

list :
                                    				Lists information about the system initialization status.

update :
                                    				Starts a system initialization.

### Parameters

name: The name
                                    				of the startup task.

state: The
                                    				state of the task. Values are:

NOT_STARTED

PROCESSING

FAILED_NEEDS_RETRY: Occurs when an initialization task that does
                                          					 not require uninitialization fails. Correct the errors then invoke the
                                          					 Initialize API again.

FAILED:
                                          					 Occurs when a task that requires uninitialization fails. Correct the errors,
                                          					 and then invoke the Uninitialize API. After a successful uninitialization, the
                                          					 initialization request can be made again.

SUCCEEDED

### Example Get
                              		  Response

```
<results>
   <state>FAILED</state>
   <initializationStatuses>
      <initializationStatus>
         <state>NOT_STARTED</state>
         <name>JtapiClientTask</name>
      </initializationStatus>
      <initializationStatus>
         <state>FAILED</state>
         <name>PGUserTask</name>
         <apiErrors>
             <apiError>
                 <errorType>errorConnectAXL</errorType>
                 <errorMessage>There is no UCM AXL service defined yet</errorMessage>
             </apiError>
          </apiErrors>
      </initializationStatus>
   </initializationStatuses>
</results>
```