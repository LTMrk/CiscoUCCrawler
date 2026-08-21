---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-e0e188c57f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_peripheral-gateway-api_1501.html
retrieved_at: 2026-08-21T16:47:42.783511+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Peripheral Gateway API

## Chapter: Peripheral Gateway API

- Peripheral Gateway API

- Peripheral Gateway                              	 API

# Peripheral Gateway API

## Peripheral Gateway
                        	 API

Use the Peripheral Gateway (PG) API to retrieve peripheral gateway information.

If there are any system validation errors on any configured PGs, API throws 400 error.

### URL

### Operations

list :
                                    				Retrieves a list of peripheral gateways.

get :
                                    				Returns one peripheral gateway using the URL https://<server>/unifiedconfig/config/peripheralgateway/<id> .

### Parameters

refURL: The
                                    				refURL of the peripheral gateway. See Shared Parameters .

name: The name
                                    				of the peripheral gateway. See Shared Parameters .

logicalControllerId: The ID of the logical controller.

peripherals: A collection of peripheral information, including client type, name, peripheralID, routingClientID, and routingType
                                    (see  Dialed Number API for routingType values).

The client
                                          					 type values are:

13:
                                                						  VRU

30:
                                                						  CUCM

42:
                                                						  Generic PG

47:
                                                						  MediaRouting

datacenter: A
                                    				reference to the data center, including the refURL and name.

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

Search
                                          						Parameters

Sort
                                          						Parameters

name

name (Default)

datacenter.name

See Search and Sort .

Advanced
                                 			 search parameters

The Peripheral
                              		  Gateway API has an advanced search for datacenters.

datacenters:
                                       				  (dc1|dc2|dc3...) which returns all peripheral gateways which belong to any
                                    				of the specified data centers. You can specify up to three data centers. The
                                    				data center names are fully matched (case-insensitive, no partial matches).
                                    				Searching for "core" returns all machines in the core data center.

### Example Get
                              		  Response

```
<peripheralGateway xsi:type="peripheralGateway">
     <changeStamp>0</changeStamp>
     <refURL>/unifiedconfig/config/peripheralgateway/5001</refURL>
     <name>MR_PG</name>
     <logicalControllerID>5001</logicalControllerID> <datacenter>
                <name>Berlin</name>
                <refURL>/unifiedconfig/config/datacenter/5000</refURL>
        </datacenter> <peripherals>
         <peripheral>
             <changeStamp>824</changeStamp>
             <clientType>47</clientType>
             <name>Multichannel</name>
             <peripheralID>5005</peripheralID>
             <routingClientID>5005</routingClientID>
             <routingType>3</routingType>
         </peripheral>
         <peripheral>
             <changeStamp>822</changeStamp>
             <clientType>47</clientType>
             <name>Outbound</name>
             <peripheralID>5007</peripheralID>
             <routingClientID>5007</routingClientID>
             <routingType>4</routingType>
         </peripheral>
     </peripherals>
</peripheralGateway>
```

| Note | If there are any system validation errors on any configured PGs, API throws 400 error. |
|---|---|

| Search
                                          						Parameters | Sort
                                          						Parameters |
|---|---|
| name | name (Default) datacenter.name |