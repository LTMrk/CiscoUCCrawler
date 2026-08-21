---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-28de04d2f2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_sip-server-group-api_1501.html
retrieved_at: 2026-08-21T16:48:28.701119+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: SIP Server Group API

## Chapter: SIP Server Group API

- SIP Server Group API

- SIP Server Group API

# SIP Server Group API

## SIP Server Group API

You can add the SIP Server groups to perform SIP dynamic routing by Cisco Unified Customer Voice Portal (CVP).

A Server Group is identified by a Server Group domain name, also known as the Fully Qualified Domain Name (FQDN), and consists
                           of one or more destination addresses (elements).

### URL

### Operations

create : Creates a new SIP server group.

delete : Permanently deletes one SIP server group.

get : Returns specific SIP server groups from the database using the URL https://<server>/unifiedconfig/config/sipservergroup/<id> .

list : Retrieves a list of SIP server groups.

update : Updates one SIP server group.

### Parameters

name: Required. Name of the group (FQDN).

description: See Shared Parameters .

type: Required. Type of group. This parameter accepts string. The value is:

VRU - For Virtualized Voice Browser (VVB), VXML Gateway, and Cisco Contact Center SIP Proxy ( CCCSP ) devices.

Agent - For Cisco Unified Communications Manager (CUCM) and CCCSP devices.

External - For Ingress Gateway and CCCSP devices.

datacenter: Site of the group. This is Null for core site. For remote sites, returns a reference to the data center, including
                                    the refURL and name. This parameter cannot be updated.

defaultGroup: Whether this is the default group. This is read-only.

elements: List the elements in this group. Includes the following parameters:

address: This is the valid hostname or IP address of the server group element.

port: Port number of the element in the server group.

secure port: The listening port for secure connection.

priority: Priority of the element in relation to the other elements in the server group. Specifies whether the server is a
                                          primary or backup server. Primary servers are specified as 1.

weight: Weight of the element in relation to the other elements in the server group. Specifies the frequency with which requests
                                          are sent to servers in that priority group.

You can add devices (elements) from different sites to a SIP Server group.

noOfElements: Number of elements configured for a group. This parameter is used only for get operation.

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

name

description

name

description

See Search and Sort .

Advanced search parameters

The SIP Server Group API also supports advanced search parameters, such as sipServerType, datacenters, and groupElement.

sipServerType : Finds all SIP Server groups that are associated to the specified group type - VRU, Agent, or External.

datacenters:(dc1|dc2|dc3): Returns all routing patterns which belong to any of the specified data centers. You can specify up to three data centers.
                                    The data center names are fully matched (case-insensitive, no partial matches). Searching for "core" returns all routing patterns
                                    in the core data center.

groupElement : Finds the SIP Server group associated with the specified hostname or IP address of the element. The search is case-sensitive
                                    and does not support partial matches.

### Example Get Response

```
<sipServerGroup>
            <refURL>/unifiedconfig/config/sipservergroup/5003</refURL>
            <changeStamp>0</changeStamp>
            <name>pcce.cisco.com</name>
            <type>Agent</type>
            <defaultGroup>false</defaultGroup>
	<datacenter>
                <refURL>/unifiedconfig/config/datacenter/9802</refURL>
                <name>Berlin</name>
            </datacenter>
            <elements>
                <element>
                    <address>CCM-SUB-1B-131</address>
                    <port>5060</port>
                    <priority>10</priority>
                    <refURL>/unifiedconfig/config/machineinventory/9792</refURL>
                    <weight>10</weight>
                </element>
                <element>
                    <address>CCM-SUB-1A-31</address>
                    <port>5060</port>
                    <priority>10</priority>
                    <refURL>/unifiedconfig/config/machineinventory/9786</refURL>
                    <weight>10</weight>
                </element>
            </elements>
            <noOfElements>2</noOfElements>
        </sipServerGroup>
```

Following are the REST responses received when the REST API runs to configure the SIP Server Group:

Success - Configuration changes persist in AW DB and synchronized with respective devices.

Code: 200

Response: Successfully saved

Partial Success - Configuration changes persist in AW DB, but failed to synchronize with one or more devices.

Code: 201

Response: Configuration update failed for one or more devices. (This occurs when the AW DB is updated but Sync with CVP failed.)

Code: 503

Response: The server is currently busy. Please try again later. (This occurs when data synchronization to a device is in progress.)

```
<apiErrors>
<apiError>
<errorMessage>Configuration update failed for one or more devices.</errorMessage>
<errorType>PARTIAL_SUCCESS</errorType>
</apiError>
</apiErrors>
```

Failure - The configuration updates to AW DB is failed.

| Note | You can add devices (elements) from different sites to a SIP Server group. |
|---|---|

| Search parameters | Sort parameters |
|---|---|
| name description | name description |