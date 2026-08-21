---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-a78d0ffbdf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_location-api_1501.html
retrieved_at: 2026-08-21T16:47:13.130312+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Location API

## Chapter: Location API

- Location API

- Location API

- Location Properties API

# Location API

## Location API

The Location feature is used to route calls locally to the agent available in the branch office, rather than routing calls
                           to central or main office over a WAN link. In Cisco Unified Call Manager (CUCM), locations are created to implement the call
                           admission control. The call admission control helps to regulate audio quality and video availability by limiting the amount
                           of bandwidth that is available for audio and video calls over links between the locations.

The Location API is used to fetch or create new locations, and update the configuration by assigning the Location code and
                           Ingress Gateway.

https://<server>/unifiedconfig/config/location

### Operations

create : Creates a new location.

delete : Permanently deletes one location.

get : Returns one location, using the URL https://<server>/unifiedconfig/config/location/<id> .

list : Retrieves a list of locations.

update : Updates a location.

### Parameters

refURL: Required. The refURL of the location configured in Packaged CCE. See Shared Parameters .

locationName: Required. The name of the location configured in CUCM. See Shared Parameters .

description: Optional. See Shared Parameters .

datacenters: The datacenters of the location. For remote sites, returns a reference to the data center, including the refURL
                                    and name.

locationCode: Required. A unique location code that is prefixed or suffixed to the ICM label for routing the calls to the
                                    gateway.

ucmPrimaryKey: Required. Location Primary Key ID fetched from CUCM that is used by CVP to create unique identifier for the
                                    location.

cucmHostAddress: The IP address of the CUCM Publisher device where locations are configured.

changeStamp: See Shared Parameters .

gateways: Gateway associated with the location. You can add only one gateway to a location.

### Search and Sort Values

The following table shows the parameters that are searched and the parameters that are sortable.

locationName

description

locationName

cucmHostAddress

See Search and Sort .

Advanced search parameters

The Location API also supports advanced search parameters, such as gateway and datacenters.

gateway:<IPaddress/hostname> : Finds the location associated to the specified hostname or IP address of the gateway. The hostname is fully matched (case-insensitive,
                                    no partial matches).

datacenter:<dcName> Returns all locations which belong to the specified data center. You can specify only one data center. The data center name
                                    is fully matched (case-insensitive, no partial matches). Searching for "core" returns all locations in the core data center.

### Example Get Response

```
<location>
        <refUrl>/unifiedconfig/config/location/6000</refurl>
        <locationName>Location1</locationName>
        <description>First Location</description>
        <datacenters>
            <datacenter>
                <name>Core</name>
            </datacenter>
            <datacenter>
                <name>Site1</name>
                <refUrl>/unifiedconfig/config/datacenter/5003</refUrl>
            </datacenter>
            <datacenter>
                <name>Site2</name>
                <refUrl>/unifiedconfig/config/datacenter/5004</refUrl>
            </datacenter>
        </datacenters>
        <locationCode>22</locationCode>
        <ucmPrimaryKey>30</ucmPrimaryKey>
        <cucmHostAddress>10.78.26.78</cucmHostAddress>
        <changeStamp>1</changeStamp>
        <gateways>
            <gateway>
                <address>cce-gw1.cisco.com</address>
                <refUrl>/unifiedconfig/config/datacenter/5005</refUrl>
             </gateway>
             <gateway>
                <address>cce-gw2.cisco.com</address>
                <refUrl>/unifiedconfig/config/datacenter/5006</refUrl>
             </gateway>
        </gateways>
    </location>
```

Following are the REST responses received when the REST API runs to configure the location:

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

## Location Properties API

The Location Properties feature provides options for the placement of the location routing code. The location routing code
                              is configured using the Location API . See Location API .

You can place the routing code at the beginning of the Network VRU label, in the middle of the Network VRU label and the correlation
                              ID, or can choose not to insert the routing code. The Location Properties are the global settings.

https://<server>/unifiedconfig/config/locationproperties

### Operations

get : Returns the location property data, using the URL https://<server>/unifiedconfig/config/locationproperties .

update : Updates a location property data.

### Parameters

locationRoutingCodeInsertOption: Required. Placement of the location routing code. As this is a global setting, any change
                                    in the value applies to all CVP across all datacenter. The following are the key values:

beginning - Location routing code at the beginning of the Network VRU label.

middle - Location routing code between the Network VRU label and the correlation ID. This is the default value.

none - Do not insert the location routing code.

Default value is middle.

### Example Get Response

```
<CVP>
<locationProperties>   
<locationRoutingCodeInsertOption>middle</locationRoutingCodeInsertOption>
</locationProperties>
</CVP>
```

Following are the REST responses received when the REST API runs to configure the location properties data across all sites:

Success - Configuration changes persist in AW DB and synchronized with respective devices.

Code: 200

Response: Successfully saved

Partial Success - Configuration changes persist in AW DB, but failed to synchronize with one or more devices.

Code: 201

Response: Configuration update failed for one or more devices. (This occurs when the AW DB is updated but Sync with CVP Call
                                    Server failed.)

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

| Search parameters | Sort parameters |
|---|---|
| locationName description | locationName cucmHostAddress |