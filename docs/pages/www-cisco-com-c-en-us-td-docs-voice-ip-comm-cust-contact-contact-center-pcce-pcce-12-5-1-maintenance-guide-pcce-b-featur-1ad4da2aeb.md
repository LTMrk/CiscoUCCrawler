---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-pcce-pcce-12-5-1-maintenance-guide-pcce-b-featur-1ad4da2aeb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/pcce/pcce_12_5_1/maintenance/guide/pcce_b_features_guide_12_5/pcce_b_pcce_features_guide_12_5_chapter_0100.html
retrieved_at: 2026-08-21T04:47:30.591470+00:00
---

Cisco Packaged Contact Center Enterprise Features Guide, Release 12.5(1)

# Cisco Packaged Contact Center Enterprise Features Guide, Release 12.5(1)

Updated: July 29, 2021

Chapter: Application Gateway

## Chapter: Application Gateway

# Application Gateway

## About Application
                        	 Gateways

An application gateway is an optional Packaged CCE feature that allows
                              		  you to invoke an external application from within a script (using a Gateway
                              		  node). You can pass data to the application and receive data in return, which
                              		  you can then examine and use for routing decisions.

Before you can use these nodes in a script, you must first configure
                              		  the gateways.

The application gateway requires connection information to communicate
                              		  with the external application. You perform this task using the Unified CCE
                              		  Administration interface.

## Configuring
                        	 Application Gateways

Configure a
                              		  application gateway for an application you want to access, from within the
                              		  scripts.

Configuration
                              		  information includes data such as:

Type of
                                    				application the gateway interacts with-a non-Packaged CCE application or an
                                    				application on another Packaged CCE system

Form of
                                    				connection the gateway uses-duplex or simplex

Fault
                                    				tolerance strategy for the gateway-described in the following table.

Fault
                                          					 Tolerance Strategy

Description

Duplicate
                                          					 Request

Packaged
                                          					 CCE, both side A and B, connects to separate application gateway hosts. They
                                          					 send simultaneous requests. Each request is sent to both the sides of the
                                          					 gateway. The response that comes back first, is used by both the sides of A and
                                          					 B of ICM.

Alternate
                                          					 Request

Packaged
                                          					 CCE, Side A and Side B connects to separate application gateway hosts. All
                                          					 requests are sent alternatively to A and B.

Hot
                                          					 Standby

Each
                                          					 router manages a connection to a different host. All requests are directed to
                                          					 the designated primary host. If either host (or connection) fails then all
                                          					 requests are directed to the backup host. This results in the loss of some
                                          					 requests on failures.

None

The
                                          					 application gateway is not duplexed.

Once you specify
                              		  the configuration information, you can define the connection information for
                              		  the gateway. For example, the network address of the port, through which the
                              		  system software communicates with the application.

If your Central
                              		  Controller is duplexed, you can define separate connection information for each
                              		  side of the Central Controller. This allows each side to communicate with a
                              		  local copy of the external application.

### Add and Maintain Application Gateways

You can create custom application gateways in Packaged CCE deployment.

Step 1

In Unified
                                          			 CCE Administration, navigate to System > Application
                                                				  Gateway .

Step 2

In Unified CCE Administration, choose Overview > Infrastructure Settings > Application Gateways .

Step 3

To add a new
                                          			 gateway, click New .

Step 4

Enter a name
                                          			 for the new application gateway. Maximum length is 32 characters. Valid
                                          			 characters are alphanumeric, period (.), and underscore (_). The first
                                          			 character must be alphanumeric.

Step 5

Enter a
                                          			 description.

Step 6

Select one of the options from the Encryption drop-down list.

- None : Selected by default. Indicates that the requests are not encrypted.

- Private Key : Indicates that the requests are encrypted using a private key.

- TLS : Indicates that the requests are encrypted using the TLS protocol.

Step 7

Select one of the options from the Connection Type drop-down list.

If you select Duplex , you can enter data in all the subsequent fields.

If you select Simplex A , the Preferred Side is set to Side A , Fault Tolerance is set to None , and the Side B box is disabled.

If you select Simplex B , the Preferred Side is set to Side B , Fault Tolerance is set to None , and the Side A box is disabled.

Step 8

Select a side from the Preferred Side drop-down list.

Step 9

Select one of the options from the Fault Tolerance drop-down list.

- Alternate Request : Each router manages connections with different hosts. The routers take turns to send half the request to the host connected
                                             to Side A and the other half to the host connected to Side B. If one host fails, the entire load is directed to the surviving
                                             host.

- Duplicate Request : Each router manages connections with different hosts. Each time a script initiates a request, both the routers communicate
                                             with their corresponding hosts. The routers process the response from the host that responds first.

- Hot Standby : Each router manages connections with different hosts. All the requests are directed to the designated primary host. If the
                                             host or the connection fails, all the requests are directed to the backup host.

Step 10

Enter the
                                          			 following server details in the Side
                                             				A and Side
                                             				B boxes as applicable:

- In Service : This
                                             				option is enabled by default. If you uncheck the In
                                                				  Service check box, the connection is no more in service and the router does
                                             				not send application gateway requests to that connection.

- Hostname/IP Address : Enter the IP address, hostname of the server, or fully qualified domain name (FQDN).

- Port : Enter the port
                                             				number.

- Initialization Data :
                                             				This information passes to the Application Gateway host at the time of
                                             				initialization.

Step 11

Click Advanced Settings on Side A or Side B to open the respective Advanced Settings dialog box. The following parameters with default values appear:

- Max Errors : Indicates the number of consecutive errors that cause the software to declare the host unavailable.

Request : Indicates the number of milliseconds the Router waits before timing out a request.

Abandon : Indicates the number of milliseconds the Router waits for a response before considering it as late.

Late : An internal timeout in milliseconds to communicate between the Router and the Application Gateway interface process.

Request Timeout : Indicates the number of milliseconds the Router waits for a response to a heartbeat before considering it as a failure.

Retry Timeout : Indicates the number of milliseconds the Router waits before retrying a missed heartbeat.

Retry Limit : Indicates the number of consecutive unanswered heartbeats after which the Router ends the connection.

Interval : Indicates the number of milliseconds the Router waits between successful heartbeats.

Retry Timeout : Indicates the number of milliseconds the Router waits before trying to reconnect after a connection terminates or a connection
                                                      attempt fails.

Retry Limit : Indicates the number of times the Router tries to establish the connection before it quits.

Open Timeout : Indicates the number of milliseconds the Router waits for a response to an open or close request. If it receives no response
                                                      within this time, the Router assumes that the request failed.

Step 12

Edit the
                                          			 advanced settings parameters as applicable and click OK .

Click the Restore Defaults button to restore the default
                                                         				  values.

Step 13

Click Save .

| Fault
                                          					 Tolerance Strategy | Description |
|---|---|
| Duplicate
                                          					 Request | Packaged
                                          					 CCE, both side A and B, connects to separate application gateway hosts. They
                                          					 send simultaneous requests. Each request is sent to both the sides of the
                                          					 gateway. The response that comes back first, is used by both the sides of A and
                                          					 B of ICM. |
| Alternate
                                          					 Request | Packaged
                                          					 CCE, Side A and Side B connects to separate application gateway hosts. All
                                          					 requests are sent alternatively to A and B. |
| Hot
                                          					 Standby | Each
                                          					 router manages a connection to a different host. All requests are directed to
                                          					 the designated primary host. If either host (or connection) fails then all
                                          					 requests are directed to the backup host. This results in the loss of some
                                          					 requests on failures. |
| None | The
                                          					 application gateway is not duplexed. |

| Step 1 | In Unified
                                          			 CCE Administration, navigate to System > Application
                                                				  Gateway . |
|---|---|
| Step 2 | In Unified CCE Administration, choose Overview > Infrastructure Settings > Application Gateways . |
| Step 3 | To add a new
                                          			 gateway, click New . The New
                                             				Application Gateway page displays. |
| Step 4 | Enter a name
                                          			 for the new application gateway. Maximum length is 32 characters. Valid
                                          			 characters are alphanumeric, period (.), and underscore (_). The first
                                          			 character must be alphanumeric. |
| Step 5 | Enter a
                                          			 description. |
| Step 6 | Select one of the options from the Encryption drop-down list. None : Selected by default. Indicates that the requests are not encrypted. Private Key : Indicates that the requests are encrypted using a private key. TLS : Indicates that the requests are encrypted using the TLS protocol. |
| Step 7 | Select one of the options from the Connection Type drop-down list. If you select Duplex , you can enter data in all the subsequent fields. If you select Simplex A , the Preferred Side is set to Side A , Fault Tolerance is set to None , and the Side B box is disabled. If you select Simplex B , the Preferred Side is set to Side B , Fault Tolerance is set to None , and the Side A box is disabled. |
| Step 8 | Select a side from the Preferred Side drop-down list. |
| Step 9 | Select one of the options from the Fault Tolerance drop-down list. Alternate Request : Each router manages connections with different hosts. The routers take turns to send half the request to the host connected
                                             to Side A and the other half to the host connected to Side B. If one host fails, the entire load is directed to the surviving
                                             host. Duplicate Request : Each router manages connections with different hosts. Each time a script initiates a request, both the routers communicate
                                             with their corresponding hosts. The routers process the response from the host that responds first. Hot Standby : Each router manages connections with different hosts. All the requests are directed to the designated primary host. If the
                                             host or the connection fails, all the requests are directed to the backup host. |
| Step 10 | Enter the
                                          			 following server details in the Side
                                             				A and Side
                                             				B boxes as applicable: In Service : This
                                             				option is enabled by default. If you uncheck the In
                                                				  Service check box, the connection is no more in service and the router does
                                             				not send application gateway requests to that connection. Hostname/IP Address : Enter the IP address, hostname of the server, or fully qualified domain name (FQDN). Port : Enter the port
                                             				number. Initialization Data :
                                             				This information passes to the Application Gateway host at the time of
                                             				initialization. |
| Step 11 | Click Advanced Settings on Side A or Side B to open the respective Advanced Settings dialog box. The following parameters with default values appear: Max Errors : Indicates the number of consecutive errors that cause the software to declare the host unavailable. Timeouts Request : Indicates the number of milliseconds the Router waits before timing out a request. Abandon : Indicates the number of milliseconds the Router waits for a response before considering it as late. Late : An internal timeout in milliseconds to communicate between the Router and the Application Gateway interface process. Heartbeats Request Timeout : Indicates the number of milliseconds the Router waits for a response to a heartbeat before considering it as a failure. Retry Timeout : Indicates the number of milliseconds the Router waits before retrying a missed heartbeat. Retry Limit : Indicates the number of consecutive unanswered heartbeats after which the Router ends the connection. Interval : Indicates the number of milliseconds the Router waits between successful heartbeats. Sessions Retry Timeout : Indicates the number of milliseconds the Router waits before trying to reconnect after a connection terminates or a connection
                                                      attempt fails. Retry Limit : Indicates the number of times the Router tries to establish the connection before it quits. Open Timeout : Indicates the number of milliseconds the Router waits for a response to an open or close request. If it receives no response
                                                      within this time, the Router assumes that the request failed. |
| Step 12 | Edit the
                                          			 advanced settings parameters as applicable and click OK . Note Click the Restore Defaults button to restore the default
                                                         				  values. | Note | Click the Restore Defaults button to restore the default
                                                         				  values. |
| Note | Click the Restore Defaults button to restore the default
                                                         				  values. |
| Step 13 | Click Save . |

| Note | Click the Restore Defaults button to restore the default
                                                         				  values. |
|---|---|