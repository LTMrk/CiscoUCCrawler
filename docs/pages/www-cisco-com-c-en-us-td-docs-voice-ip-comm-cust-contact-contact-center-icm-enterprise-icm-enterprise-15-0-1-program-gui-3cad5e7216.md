---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-3cad5e7216
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_trace_level_api_1501.html
retrieved_at: 2026-08-21T16:48:54.335996+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Trace Level API

## Chapter: Trace Level API

- Trace Level API

- Trace Level                              	 API

# Trace Level API

## Trace Level
                        	 API

Use the Trace Level
                           		API to set the trace levels for the following components:

Unified Contact
                                 			 Center Enterprise (CCE)

Unified Customer
                                 			 Voice Portal (CVP)

Unified
                                 			 Communications Manager (UCM)

### URL

### Operations

list :
                                    				Returns the trace level for each component type.

Query parameters

Summary list: See list .
                                                						  Summary defaults to true on the Trace Level API.

update :
                                    				Sets the trace level for each component type.

### Parameters

component: A
                                    				list of components for which the trace level is set. Includes the following
                                    				parameters:

CCE

CVP

UCM

- NORMAL

- DETAILED

- CUSTOM: Not set by user.
                                             						This level appears when one or more trace levels have been set by an outside
                                             						program, as the component does not match the normal detailed definitions for
                                             						the trace levels.

traceMachines: A collection of trace information about each
                                          					 machine containing the refURL of the machine and a collection of process level
                                          					 trace values. Only available when the summary query parameter is false.

### Example List
                              		  Response

```
<traceLevels>
     <component>
        <type>CCE</type>
        <level>DETAILED</level>
     </component>
     <component>	
        <type>CVP</type>				
        <level>NORMAL</level>
     </component>	
     <component>	
        <type>UCM</type>				
        <level>CUSTOM</level>
     </component>	
</traceLevels>
```