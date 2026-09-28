---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-6b1f007d10
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_courtesy-callback-api_1501.html
retrieved_at: 2026-08-21T16:45:49.759014+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Courtesy CallBack API

## Chapter: Courtesy CallBack API

- Courtesy CallBack API

- Courtesy CallBack API

# Courtesy CallBack API

## Courtesy CallBack API

The Courtesy Callback (CCB) feature is available in Unified CVP. Courtesy Callback reduces the time callers have to wait on
                           hold/in queue. The feature allows the system to offer callers who meet certain criteria, for example, callers with the possibility
                           of being in queue for more than X minutes, the option to be called back by the system when the wait time would be considerably
                           shorter.

Courtesy CallBack feature of CVP can be configured through PCCE UI. The configured data persist in AW DB and then synchronized
                           to the CVP Call Servers of the site through the CCB API.

### URL

To associate the Unified CVP Reporting Server. The Unified CVP Reporting Server IP address is saved in AW DB, and synchronized
                              to realtimedb.properties of all the CVP Call Servers present in a site. https://<server>/unifiedconfig/config/ccb/{datacenter}

### Operations

get : Returns the IP address or hostname of the CVP Reporting Server, using the URL: https://<server>/unifiedconfig/config/ccb/{datacenter} .

update : Updates the IP address or hostname of the CVP Reporting Server.

### Parameters

reportingAddress: Required. IP address or hostname of the Cisco Unified CVP Reporting Server in PCCE Inventory. The value
                                    can be null or empty. If the value is not empty, you must provide a valid IPv4 or IPv6 address.

### Example Get Response - CVP Call Server

```
<?xml version="1.0" encoding="UTF-8"?>
<CCB>
<reportingAddress>10.10.10.10</reportingAddress>
</CCB>
```

Following are the REST responses received when the REST API runs to configure the Courtesy CallBack:

Success - Configuration changes persist in AW DB and synchronized with CVP Call Server.

Code: 200

Response: Successfully saved

Partial Success - Configuration changes persist in AW DB, but failed to synchronize with CVP Call Server.

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