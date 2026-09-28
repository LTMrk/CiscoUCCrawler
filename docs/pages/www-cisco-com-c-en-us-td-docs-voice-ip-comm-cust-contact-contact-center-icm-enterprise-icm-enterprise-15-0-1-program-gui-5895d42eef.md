---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-5895d42eef
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_network-vru-script-api_1501.html
retrieved_at: 2026-08-21T16:47:29.970583+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Network VRU Script API

## Chapter: Network VRU Script API

- Network VRU Script API

- Network VRU Script                              	 API

# Network VRU Script API

## Network VRU Script
                        	 API

Calls may be sent to
                           		a Voice Response Unit (VRU) instead of or before they are sent to an agent. In
                           		the Packaged CCE deployment, the VRU is Customer Voice Portal (Unified CVP).
                           		You must configure network VRU scripts to direct Unified CVP on how to handle
                           		the treatment of individual calls.

Use the Network VRU
                           		Script API to list, create, edit and delete network VRU scripts.

### URL

### Operations

create : Creates one
                                    				network VRU script.

delete : Deletes one
                                    				network VRU script from the database.

get : Returns one
                                    				network VRU script, using the URL https://<server>/unifiedconfig/config/networkvruscript/<id> .

list : Retrieves a
                                    				list of network VRU scripts.

update : Updates one
                                    				network VRU script.

### Parameters

refURL: The
                                    				refURL of the network VRU script. See Shared Parameters .

name: The name
                                    				of the network VRU as seen by CCE. See Shared Parameters .

changeStamp:
                                    				See Shared Parameters .

description:
                                    				See Shared Parameters .

routingType:
                                    				This field is optional and defaults to 1. Options are:

1: Voice.
                                          					 Used by Unified CVP.

2:
                                          					 Multichannel. Used by Email and Web Collaboration.

vruScriptName:
                                    				Required. The name of the script as it is known on the Unified CVP. Maximum
                                    				length of 39 characters allowed.

timeout:
                                    				Number of seconds for the system to wait for a response from the routing client
                                    				after directing it to run the script. Must be an integer that is 1 or higher.
                                    				Default is 180.

configParam:
                                    				Optional string used by Unified CVP to pass additional parameters to the IVR
                                    				Service. Maximum length is 255 characters.

interruptible:
                                    				Indicates whether the script can be interrupted. Values are true/false.

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

- name

- description

- name (default)

- description

- vruScriptName

- timeout

- configParam

- interruptible

See Search and Sort .

### Example Get
                              		  Response

```
<networkVruScript>
    <refURL>/unifiedconfig/networkvruscript/(id)</refURL>
    <routingType>1</routingType>
    <name>test</name>
    <vruScriptName>GS,Server,V</vruScriptName>
    <timeout>180</timeout>
    <configParam>Y</configParam>
    <interruptible>true</interruptible>
    <description>CVP VXML Server script</description>
    <changeStamp>0</changeStamp>
</networkVruScript>
```

| Search parameters | Sort parameters |
|---|---|
| name description | name (default) description vruScriptName timeout configParam interruptible |