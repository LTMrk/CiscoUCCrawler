---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-2bf5de91c0
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_sip-server-group-properties-api_1501.html
retrieved_at: 2026-08-21T16:48:33.288034+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: SIP Server Group Properties API

## Chapter: SIP Server Group Properties API

- SIP Server Group Properties API

- SIP Server Group Properties API

# SIP Server Group Properties API

## SIP Server Group Properties API

The SIP Server group properties provide a heartbeat mechanism that enables the originating endpoint to have the status of
                           the destination endpoint before sending out the SIP request. Whether the destination is unreachable over the network, or is
                           out of service, the originating SIP user agent knows the status through a heartbeat mechanism.

The Server group feature adds a heartbeat mechanism with endpoints for SIP. This feature allows faster failover on call control
                           by eliminating delays due to failed endpoints.

The Up and Down Endpoint Heartbeat Interval is between any two heartbeats; however, it is not between heartbeats to the same
                                       endpoint. The SIP Server Group does not wake up at a specific interval and sends a heartbeat for all elements since this approach
                                       can result in CPU utilization issues. It also takes more resources to track heartbeats for many endpoints. For example, for
                                       3 total elements across all SIP Server Groups, to proactively send a heartbeat to each element at 30000ms (30 seconds) intervals,
                                       you have to set the Endpoint Heartbeat Interval to 10000ms (10 seconds). It is less deterministic for reactive mode since
                                       elements that are currently down can fluctuate so the heartbeat interval fluctuates with it. To turn off pinging when the
                                       element is UP, set the UP interval to zero (reactive pinging). To turn off pinging when the element is down, set the DOWN
                                       interval to zero (proactive pinging). To ping when the element is either UP or DOWN, set both the intervals to greater than
                                       zero (adaptive pinging).

https://<server>/unifiedconfig/config/sipservergroupproperties

### Operations

get : Returns specific SIP server group properties from the database using the URL https://<server>/unifiedconfig/config/sipservergroupproperties/<id> .

update : Updates one SIP server group properties.

### Parameters

serverGroupHeartbeats: Optional. Enable the heartbeat mechanism. The Heartbeat properties are editable only when this parameter
                                    value is true. The default value is false.

serverGroupHBNumTries: Required. The number of failed heartbeats before marking the destination as unreachable.

The default value is 3. Range is 1 to 5.

serverGroupHBTimeout: Required. The amount of time, in milliseconds, before timing out the heartbeat.

The default value is 800 milliseconds. Range is 100 to 3000.

serverGroupUpInterval: Required. The ping interval for heart beating an endpoint (status) that is up.

The default value is 5000 milliseconds. Range is 0 to 3600000

serverGroupDownInterval: Required. The ping interval for heart beating an endpoint (status) that is down.

The default value is 5000 milliseconds. Range is 0 to 3600000

serverGroupHBLocalListenPort: Required. The heartbeat local socket listen port. Responses to heartbeats are sent to this port
                                    on CVP by endpoints.

The default value is 5067. Range is 0 to 65535

serverGroupHBMethod: Required. The heartbeat SIP method.

The default value is OPTIONS. Supported values are OPTIONS and PING

serverGroupHBTransportType: Required. During transportation, Server Group heartbeats are performed with a UDP or TCP socket
                                    connection. If unreachable or overloaded callbacks are invoked in the Server Group, that element is marked as being down for
                                    both UDP and TCP transports. When the element is up again, it is routable for both UDP and TCP.

TLS transport is not supported.

serverGroupOverloadedResponseCodes: Required. The response codes are used to mark an element as overloaded when received. If more than one code is present, it is presented as a comma-delimited list. An OPTIONS message is sent to
                                    an element and if it receives any of those response codes, then this element is marked as overloaded.

The default value is 503,480,600. Maximum length of 128 characters, and accepts the number 0 to 9 and commas (,).

optionsOverrideHost: Required. The contact header hostname to be used for a heartbeat request (SIP OPTIONS). The given value
                                    is added to the name of the contact header of a heartbeat message. Thus, a response to a heartbeat would contain gateway trunk
                                    utilization information.

The default value is cvp.cisco.com. The maximum length of characters is 128.

### Example Get Response

```
<CVP>
<sipServerGroupProperties>   
<serverGroupHeartbeats>true</serverGroupHeartbeats>
<serverGroupHBNumTries>4</serverGroupHBNumTries>
<serverGroupHBTimeout>801</serverGroupHBTimeout>
<serverGroupUpInterval>5001</serverGroupUpInterval> 
<serverGroupDownInterval>5000</serverGroupDownInterval>
<serverGroupHBLocalListenPort>5067</serverGroupHBLocalListenPort>
<serverGroupHBMethod>OPTIONS</serverGroupHBMethod>
<serverGroupHBTransportType>UDP</serverGroupHBTransportType>
<serverGroupOverloadedResponseCodes>200,300</serverGroupOverloadedResponseCodes>  
<optionsOverrideHost>cvp.cisco.com</optionsOverrideHost>   
</sipServerGroupProperties>
</CVP>
```

Following are the REST responses received when the REST API runs to configure the SIP Server group properties:

Success - Configuration changes persist in AW DB and synchronized with respective devices.

Code: 200

Response: Successfully saved

Partial Success - Configuration changes persist in AW DB, but failed to synchronize with one or more devices.

Code: 201

Response: Configuration update failed for one or more devices. (This occurs when the AW DB is updated but Sync with CVP Call
                                    Servers failed.)

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

| Note | The Up and Down Endpoint Heartbeat Interval is between any two heartbeats; however, it is not between heartbeats to the same
                                       endpoint. The SIP Server Group does not wake up at a specific interval and sends a heartbeat for all elements since this approach
                                       can result in CPU utilization issues. It also takes more resources to track heartbeats for many endpoints. For example, for
                                       3 total elements across all SIP Server Groups, to proactively send a heartbeat to each element at 30000ms (30 seconds) intervals,
                                       you have to set the Endpoint Heartbeat Interval to 10000ms (10 seconds). It is less deterministic for reactive mode since
                                       elements that are currently down can fluctuate so the heartbeat interval fluctuates with it. To turn off pinging when the
                                       element is UP, set the UP interval to zero (reactive pinging). To turn off pinging when the element is down, set the DOWN
                                       interval to zero (proactive pinging). To ping when the element is either UP or DOWN, set both the intervals to greater than
                                       zero (adaptive pinging). |
|---|---|

| Note | TLS transport is not supported. |
|---|---|