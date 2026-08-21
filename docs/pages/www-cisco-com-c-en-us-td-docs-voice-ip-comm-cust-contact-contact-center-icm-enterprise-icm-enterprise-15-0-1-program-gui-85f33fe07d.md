---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-icm-enterprise-icm-enterprise-15-0-1-program-gui-85f33fe07d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/icm_enterprise/icm_enterprise_15_0_1/Program/guide/pcce_b_cisco_packaged_cce_developer_reference_release_1501/pcce_m_application-gateway-api_1501.html
retrieved_at: 2026-08-21T16:45:12.340585+00:00
---

Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

# Cisco Packaged Contact Center Enterprise Developer Reference, Release 15.0(1)

Updated: April 9, 2026

Chapter: Application Gateway API

## Chapter: Application Gateway API

- Application Gateway API

- Application                              	 Gateway API

# Application Gateway API

## Application
                        	 Gateway API

Use this API to
                           		create a simple application gateway of the type custom
                              		  gateway . You can have up to 20 application gateways.

### URL

### Operations

create :
                                    				Creates one application gateway and stores it in the database.

delete :
                                    				Deletes one application gateway from the database.

get :
                                    				Retrieves one application gateway from the database, using the URL https://<server>/unifiedconfig/config/applicationgateway/<id>

list :
                                    				Retrieves a list of application gateways, using the URL https://<server>:<serverport>/unifiedconfig/config/applicationgateway/<id>

update :
                                    				Updates one application gateway in the database, using the URL https://<server>:<serverport>/unifiedconfig/config/applicationgateway/<id>

### Parameters

refURL: The
                                    				refURL for the application gateway. See Shared Parameters .

changeStamp:
                                    				See Shared Parameters .

description:
                                    				See Shared Parameters .

encryption:
                                    				Indicates whether requests to the application gateway are encrypted. True or
                                    				false. Default is false.

faultTolerance: If the application gateway is duplexed,
                                    				specifies the fault-tolerance strategy used. Possible values include the
                                    				following:

NONE
                                          					 (default)

DUPLICATE_REQUEST

ALTERNATE_REQUEST

HOT_STANDBY

name:
                                    				Required. An enterprise name for the application gateway.

preferredSide:
                                    				Required. The preferred side of the gateway to use when both sides are
                                    				available. A or B.

side:
                                    				Indicates the side whether A or B.

address: IP
                                    				address or hostname to connect to.

port: port
                                    				number; to be used together with address field.

initializationData: An optional string software passes to the
                                    				host during initialization. This corresponds toconnectionInfofield.

inService:
                                    				Checks the connection availability.

If any of the
                                          			 following fields are present during create or update API, it overrides the
                                          			 global settings.

maxErrors:
                                    				Indicates the number of consecutive errors that cause the router to declare the
                                    				host unavailable. This corresponds to ErrorThreshold column.

heartBeat

interval: Indicates the number of milliseconds the router waits
                                             					 between successful heartbeats.

retry:
                                             					 Limit Number of consecutive unanswered heartbeats after which the router ends
                                             					 the connection. This corresponds to HeartbeatLimit column.

retryTimeout: Indicates the number of milliseconds the router
                                             					 waits before retrying a missed heartbeat. This corresponds to HeartbeatRetry column.

requestTimeout: Indicates the number of milliseconds the router
                                             					 waits for a response to a heartbeat before considering it as a failure. This
                                             					 corresponds to HeartbeatTimeout column.

session:

openTimeout: Indicates the number of milliseconds the router
                                             					 waits for a response to an open or close request. If it receives no response
                                             					 within this time, the router assumes the request failed.

retryTimeout: Indicates the number of milliseconds the router
                                             					 waits before trying to reconnect after a connection terminates or a connection
                                             					 attempt fails. This corresponds to the SessionRetry column.

retryLimit: Indicates the number of times the router tries to
                                             					 establish the connection before it quits. This corresponds to the SessionRetryLimit column.

timeout

abandon:
                                             					 An internal timeout in milliseconds to communicate between the router and the
                                             					 Application Gateway interface process.

late:
                                             					 Indicates the number of milliseconds the router waits for a response before
                                             					 considering it as late. This does not affect router processing. It is for
                                             					 statistical use only.

request:
                                             					 Indicates the number of milliseconds the system waits before timing out a
                                             					 request.

### Search and
                              		  Sort Values

The following
                              		  table shows the parameters that are searched and the parameters that are
                              		  sortable.

Search
                                          						parameters

Sort
                                          						parameters

name

description

name

description

encryption

Only default
                                          			 search is supported.

See Search and Sort .

### Example Create
                              		  Request

```
<applicationGateway>
    <description>application gateway for application1</description>
    <encryption>true</encryption>
    <faultTolerance>ALTERNATE_REQUEST</faultTolerance>
    <name>application gateway for application1</name>
    <preferredSide>A</preferredSide>
    <connections>
        <connection>
            <side>A</side>
            <address>120.22.30.102</address>
            <port>2033</port>
            <initializationData>connect</initializationData>
            <inService>true</inService>
            <maxErrors>10</maxErrors>
            <heartBeat>
                <interval>15000</interval>
                <retryLimit>10</retryLimit>
                <retryTimeout>200</retryTimeout>
                <requestTimeout>300</requestTimeout>
            </heartBeat>
            <session>
                <openTimeout>15000</openTimeout>
                <retryTimeout>60000</retryTimeout>
                <retryLimit>10</retryLimit>
            </session>
            <timeout>
                <abandon>5000</abandon>
                <late>300</late>
                <request>300</request>
            </timeout>
        </connection>
        <connection>
            <side>B</side>
            <address>120.22.30.104</address>
            <port>2034</port>
            <initializationData>connect</initializationData>
            <inService>true</inService>
            <maxErrors>10</maxErrors>
            <heartBeat>
                <interval>15000</interval>
                <retryLimit>10</retryLimit>
                <retryTimeout>200</retryTimeout>
                <requestTimeout>300</requestTimeout>
            </heartBeat>
            <session>
                <openTimeout>15000</openTimeout>
                <retryTimeout>60000</retryTimeout>
                <retryLimit>10</retryLimit>
            </session>
            <timeout>
                <abandon>5000</abandon>
                <late>300</late>
                <request>300</request>
            </timeout>
        <connection>
    </connections>
</applicationGateway>
```

### Example Get
                              		  Response

```
<applicationGateway>
    <refURL>/unifiedconfig/config/applicationgateway/5000</refURL>
    <changeStamp>1</changeStamp>
    <description>application gateway for application1</description>
    <encryption>true</encryption>
    <faultTolerance>ALTERNATE_REQUEST</faultTolerance>
    <name>appGateway1</name>
    <preferredSide>A</preferredSide>
    <connections>
        <connection>
            <side>A</side>
            <address>120.22.30.102</address>
            <port>2033</port>
            <initializationData>connect</initializationData>
            <inService>true</inService>
            <maxErrors>10</maxErrors>
            <heartBeat>
                <interval>15000</interval>
                <retryLimit>10</retryLimit>
                <retryTimeout>200</retryTimeout>
                <requestTimeout>300</requestTimeout>
            </heartBeat>
            <session>
                <openTimeout>15000</openTimeout>
                <retryTimeout>60000</retryTimeout>
                <retryLimit>10</retryLimit>
            </session>
            <timeout>
                <abandon>5000</abandon>
                <late>300</late>
                <request>300</request>
            </timeout>
        </connection>
        <connection>
            <side>B</side>
            <address>120.22.30.104</address>
            <port>2034</port>
            <initializationData>connect</initializationData>
            <inService>true</inService>
            <maxErrors>10</maxErrors>
            <heartBeat>
                <interval>15000</interval>
                <retryLimit>10</retryLimit>
                <retryTimeout>200</retryTimeout>
                <requestTimeout>300</requestTimeout>
            </heartBeat>
            <session>
                <openTimeout>15000</openTimeout>
                <retryTimeout>60000</retryTimeout>
                <retryLimit>10</retryLimit>
            </session>
            <timeout>
                <abandon>5000</abandon>
                <late>300</late>
                <request>300</request>
            </timeout>
        <connection>
    </connections>
</applicationGateway>
```

| Note | If any of the
                                          			 following fields are present during create or update API, it overrides the
                                          			 global settings. |
|---|---|

| Search
                                          						parameters | Sort
                                          						parameters |
|---|---|
| name description | name description encryption |

| Note | Only default
                                          			 search is supported. |
|---|---|