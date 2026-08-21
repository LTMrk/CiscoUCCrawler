---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-0d40519495
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_application-gateway-global-settings-api_1501.html
retrieved_at: 2026-08-21T16:45:16.428585+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Application Gateway Global Settings API

## Chapter: Application Gateway Global Settings API

- Application Gateway Global Settings API

- Application                              	 Gateway Global Settings API

# Application Gateway Global Settings API

## Application
                        	 Gateway Global Settings API

Use this API to
                           		retrieve global settings values for application gateway configurations. This is
                           		a read-only API.

### URL

### Operations

list :
                                    				Retrieves a list of values for the global configuration settings for each
                                    				application gateway type. The only supported type is CUSTOM_GATEWAY.

### Parameters

errorThreshold: Specifies the number of consecutive errors after
                                    				which the router declares the Application Gateway host unavailable and tries to
                                    				reconnect.

heartbeat:
                                    				Information about the heartbeat, which includes the following parameters:

interval:
                                          					 The time in milliseconds the router waits between successful heartbeats.

limit: The
                                          					 number of consecutive missed heartbeats after which the router closes the
                                          					 connection and attempts to reconnect.

retry: How
                                          					 long in milliseconds the router waits before retrying a heartbeat after a
                                          					 heartbeat has failed.

timeout:
                                          					 How long in milliseconds the router waits for a response to a heartbeat before
                                          					 considering it a failure.

session:
                                    				Information about the session, which includes the following parameters:

openTimeout: How long in milliseconds the router waits for a
                                          					 response to an open or close request. If it receives no response within this
                                          					 time, the router assumes the request failed.

retry: How
                                          					 long in milliseconds the router waits before trying to reconnect after a
                                          					 connection terminates or a connection attempts fails.

retryLimit: The number of times the router tries to establish
                                          					 the connection before it quits. If this limit is reached, you must restart the
                                          					 connection.

timeout:
                                    				Information about the request, which includes the following parameters:

abandon:
                                          					 An internal timeout in milliseconds for communication between the router and
                                          					 the Application Gateway interface process. If a request exceeds this limit, the
                                          					 router assumes the Application Gateway interface process is off-line.

late: An
                                          					 internal timeout in milliseconds for communication between the router and the
                                          					 Application Gateway interface process. If a request exceeds this limit, the
                                          					 system software considers the request to be late.

request:
                                          					 How long in milliseconds the system software waits before timing out a request.

type: The type
                                    				of application gateway. The only supported type is CUSTOM_GATEWAY.

### Example Get
                              		  Response

```
<applicationGatewayGlobalSettings>
    <applicationGatewayGlobalSetting>
        <connectionParameters>
            <errorThreshold>10</errorThreshold>
            <heartBeat>
                <interval>15000</interval>
                <limit>10</limit>
                <retry>200</retry>
                <timeout>300</timeout>
            </heartBeat>
            <session>
                <openTimeout>15000</openTimeout>
                <retry>60000</retry>
                <retryLimit>10</retryLimit>
            </session>
            <timeout>
                <abandon>5000</abandon>
                <late>300</late>
                <request>300</request>
            </timeout>
        </connectionParameters>
        <type>CUSTOM_GATEWAY</type>
    </applicationGatewayGlobalSetting>
</applicationGatewayGlobalSettings>
```