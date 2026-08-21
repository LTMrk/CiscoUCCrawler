---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-75873ea2fd
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_facility-api_1501.html
retrieved_at: 2026-08-21T16:46:40.006927+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Facility API

## Chapter: Facility API

- Facility API

- Facility                              	 API

# Facility API

## Facility
                        	 API

Use the Facility API
                           		to retrieve a list of every facility, including associated instances, from the
                           		Active Directory domain. This API is read-only.

### URL

### Operations

list :
                                    				Returns a list of facilities.

### Parameters

facilities: A
                                    				collection of facility items, including a list of each facility's instances.
                                    				Includes a name parameter.

### Example Get
                              		  Response

```
<results>
   <facilities>
      <facility>
         <instances>
            <instance>
               <name>bos01</name>
            </instance>
            <instance>
               <name>pra01</name>
            </instance>
            <instance>
               <name>bos02</name>
            </instance>
         </instances>
         <name>bos</name>
      </facility>
      <facility>
         <instances>
            <instance>
               <name>test</name>
            </instance>
         </instances>
         <name>Cisco_test_fac</name>
      </facility>
   </facilities>
</results>
```