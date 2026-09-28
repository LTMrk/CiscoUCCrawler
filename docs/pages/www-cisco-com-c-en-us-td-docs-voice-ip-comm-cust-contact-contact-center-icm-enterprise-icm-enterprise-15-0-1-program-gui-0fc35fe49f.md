---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-0fc35fe49f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_routing-type-api_1501.html
retrieved_at: 2026-08-21T16:48:03.876157+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Routing Type API

## Chapter: Routing Type API

- Routing Type API

- Routing Type                              	 API

# Routing Type API

## Routing Type
                        	 API

Use the Routing Type API to retrieve the list of routing types in the solution, including whether each routing type allows
                           dialed number creation. This API is read-only.

### URL

### Operations

list :
                                    				Returns routing type information for all data centers .

get :
                                    				Returns routing type information for a specific remote data center using the
                                    				URL https://<server>/unifiedconfig/config/routingtype?datacenter=<DatacenterName>

### Parameters

type: Indicates the value of this routing type (see Dialed Number API ).

state: Indicates the state of the routing type:

UNKNOWN: Indicates that the system cannot determine the state of the routing type due to inventory or status errors.

UNUSED: Indicates that the routing type has not been used in Peripheral Gateway Setup.

MISCONFIGURED: Indicates that the routing type is used in Peripheral Gateway Setup, but either the Application Host Name associated
                                          with this routing type has not yet been added to the inventory, or there are status rule violations for the configuration.

OK: The routing type is configured correctly and dialed numbers can be created on this routing type (see Dialed Number API ).

machineType: For routing types 4, 5, 6, and 8 indicates the type of machine in the inventory that is used for this routing type. Potential machine types include EXTERNAL_SOCIAL_MINER
                                    , EXTERNAL_ECE , EXTERNAL_THIRD_PARTY_MULTICHANNEL and CLOUD_CONNECTOR_PUB .

datacenter:
                                    				Indicates the datacenter to which the routing type is associated.

CLOUD_CONNECTOR_PUB refers to Digital Routing service.

### Example Get
                              		  Response

```
<results>
    <routingTypes>
      <routingType>
        <type>1</type>
        <state>OK</state>
      </routingType>
      <routingType>
        <type>2</type>
        <state>OK</state>
      </routingType>
      <routingType>
        <type>3</type>
        <state>OK</state>
      </routingType>
      <routingType>
        <type>4</type>
        <machineType> EXTERNAL_ECE </machineType>
        <state>OK</state>
      </routingType>
      <routingType>
        <type>5</type>
        <state>MISCONFIGURED</state>
      </routingType>
      <routingType>
        <type>6</type>
        <machineType>EXTERNAL_THIRD_PARTY_MULTICHANNEL</machineType>
        <state>OK</state>
      </routingType>
      <routingType>
     <type>7</type>
     <state>UNKNOWN</state>
     </routingType>
     <routingType>
     <type>8</type>
     <machineType>CLOUD_CONNECTOR_PUB</machineType>
     <state>OK</state>
     </routingType>
<routingType>
    <type>9</type>
    <state>OK</state>
 </routingType>
     </routingTypes> <datacenterRoutingTypes>
      <datacenterRoutingType>
        <datacenter>
          <refURL>/unifiedconfig/config/datacenter/5000</refURL>
          <name>boston</name>
        </datacenter>
        <routingTypes>
          <routingType>
            <type>1</type>
            <state>OK</state>
          </routingType>
          ...
          ...
        </routingTypes>
      </datacenterRoutingType>
      ...
      ...
    </datacenterRoutingTypes> </results>
```

| Note | CLOUD_CONNECTOR_PUB refers to Digital Routing service. |
|---|---|