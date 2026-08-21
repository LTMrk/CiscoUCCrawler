---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-configurationguid-4cf0a4d987
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/ConfigurationGuideCVP12_6/guide/ccvp_b_1261-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_m_1252-preconfiguration.html
retrieved_at: 2026-08-21T06:52:13.859592+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: June 11, 2024

Chapter: Preconfiguration

## Chapter: Preconfiguration

# Preconfiguration

## Prerequisites for Call Flow Model Configuration

This section describes the configuration procedures and information you need before you select a call flow model
                              and  implement it.

### Design
                           	 Prerequisites

Read the Configuration Guide for
                                                				  Cisco Unified Customer Voice Portal .

Understand
                                       				Cisco Unified Customer Voice Portal (CVP) and the description of call flow
                                       				models.

Analyze the
                                       				design information that is provided in Configuration Guide for
                                                				  Cisco Unified Customer Voice Portal ,
                                       				and then choose a call flow model for your desired Unified CVP implementation.

Create the
                                       				simplified all-in-one-box step-by-step call model examples.

Use the
                                       				troubleshooting information and examples as templates.

## Preconfiguration
                        	 Tasks

Step 1

Have network
                                       			 information. See Network Information .

Step 2

Perform ring
                                       			 no answer settings with SIP. See Ring No Answer Settings with SIP .

Step 3

Install Unified CVP on your computer. For Unified CVP installation, see Installation and Upgrade
                                                				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/en/US/products/sw/custcosw/ps1006/prod_installation_guides_list.html and Unified CVP Installation .

Step 4

Install Cisco
                                       			 Unified Intelligent Contact Management (ICM), Cisco Unified Communications
                                       			 Manager (CM), VXML and ingress gateways.

Step 5

Ensure that you have login credentials for Operations Console and Reporting Server. To sign in to Operations Console and view
                                       its menus, see Operations Console .

Step 6

Route calls
                                       			 through the network to the VRU. See Route Calls Through the Network to the VRU .

Step 7

Configure
                                       			 ethernet switch/server NIC, gateways, and Call Server settings. See Ethernet Switch/Server NIC, Gateways and Call Server Settings .

Step 8

Apply contact
                                       			 center gateway debug settings. Apply Contact Center Gateway Debug Settings .

Step 9

Check the
                                       			 network VRU types. See the Network VRU Types .

Step 10

Refer to the
                                       			 SIP dialed number pattern matching algorithm. See SIP Dialed Number Pattern Matching Algorithm .

Step 11

Default
                                       			 security settings can prevent you from using Operations Console. Check your
                                       			 security policy and, if needed, change the settings to a less restrictive
                                       			 level.

### Network
                           	 Information

To configure
                                 		  Unified CVP components and additional solution CVP components for a call flow
                                 		  model, ensure that you have the following network information:

Understanding
                                       				of which Unified CVP call flow model to implement.

For
                                                   				  information about call flow models, see the Configuration Guide for
                                                            				  Cisco Unified Customer Voice Portal .

Network
                                       				topology for your system, including addresses and names of the solution
                                       				components.

Failover
                                       				strategy for Gateways, Unified CVP components, and Media Servers.

Strategy for
                                       				inbound call routing (that is, dial-peers versus Proxy Server).

Naming
                                       				resolution system for Gateways (DNS versus configured on the Gateway).

Naming
                                       				schemes to be used for Unified Intelligent Contact Management Enterprise (ICME)
                                       				peripheral gateways, peripherals, and routing clients.

If you are
                                       				using a voice response unit (VRU) other than Unified CVP, have information
                                       				about VRU trunk group number and number of trunks.

Know locale
                                       				values to be used for automatic speech recognition (ASR) and text to speech
                                       				(TTS) servers.

Know whether
                                       				one or multiple VRUs, which refers to the dialed number, are to be used for
                                       				each customer.

### Unified CVP
                           	 Installation

Install the Unified CVP software. For the installation procedures of Unified CVP components, see the https://www.cisco.com/en/US/products/sw/custcosw/ps1006/prod_installation_guides_list.html .

Install the
                                       				solution components.

If you are
                                       				using Unified CVP as a Unified ICME queuing platform, ensure that the VRU
                                       				peripheral gateways use service control with Service Control Reporting enabled.
                                       				If you are using it as a self-service platform, disable Service Control
                                       				Reporting. Also, note the VRU Connection Port that is used for each VRU
                                       				peripheral gateways Peripheral Interface Manager (PIM).

For information on IVR-related Service Control reporting and queue reporting, see the https://www.cisco.com/en/US/products/sw/custcosw/ps1844/products_user_guide_list.html and the https://www.cisco.com/en/US/products/sw/custcosw/ps1001/products_user_guide_list.html .

For Unified CVP reporting, see Reporting Guide for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html .

Ensure that
                                       				the NIC cards, voice gateway, and network components have the Ethernet
                                       				interfaces configured with matching speed and duplex settings.

For
                                                         						details about the required Ethernet Switch/Server NIC settings, see Ethernet Switch/Server NIC, Gateways and Call Server Settings .

- For details on design
                                                      					 considerations and guidelines for deploying enterprise network solutions that
                                                      					 includes Unified CVP, see the Configuration Guide for
                                                               				  Cisco Unified Customer Voice Portal .

### Route Calls
                           	 Through the Network to the VRU

Most call flow
                                 		  models involve a step in which the call must be transferred to a VoiceXML
                                 		  gateway. Depending on the specific call flow model in use, one of two
                                 		  techniques is applied to direct that transfer. Both techniques involve one or
                                 		  multiple labels that Unified ICME or Unified Intelligent Contact Management
                                 		  Host (ICMH) provides. Configure these in the other call routing components of
                                 		  the solution to deliver a call to an appropriate VoiceXML gateway. Such labels
                                 		  are part of the overall dialed number plan of the contact center, and must be
                                 		  determined before you configure Unified CVP.

Using
                                             					 Network VRUs of Type 7 or 10

Determine
                                             					 the Network Routing Number. This number is the base for routing calls through
                                             					 the network to the VRU. A correlation ID is appended to this number to transfer
                                             					 calls to a Network VRU through the network.

With a
                                             					 Customer VRU in Unified ICMH environments and for NIC Type 8 call flow models

Determine the translation route pools to use for each VRU.

Determine the labels to be sent to the network to connect the
                                                      						  call to the VRU and the corresponding Dialed Number Identification Service
                                                      						  (DNIS) that is seen by the VRU. For example, the label for the network might be
                                                      						  18008889999 and the DNIS received by the VRU and sent back to Unified ICME to
                                                      						  identify the call might be 9999.

### Ethernet Switch/Server NIC, Gateways and Call Server Settings

Ensure to have the following Ethernet Switch/Server NIC, gateways, and Call Server settings:

Caution

Ethernet Switch Speed

Server/Gateway NIC Speed

Speed/Duplex Setting for Switch
                                             Port

Speed/Duplex Setting for
                                             Server/GW NIC

1000 Mb

1000 Mb

1000/Full

1000/Full

1000 Mb

1000 Mb

Auto/Auto

Auto/Auto

1000 Mb

100 Mb

100 Mb/Full

100 Mb/Full

100 Mb

100 Mb

100 Mb/Full

100 Mb/Full

100 Mb

1000 Mb

100 Mb/Full

100 Mb/Full

#### Call Server and VXML Gateway in Different Subnets

Unified CVP shows one to two seconds delay in the Call Server when VXML gateway bootstraps the call. The delay is caused if the Call Server and VXML gateway are in different subnets.

To avoid the delay:

Step 1

Open the registry of the
                                             			 machine.

Step 2

Navigate to the following path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\<Interface
                                                				GUID.

Step 3

Set TcpAckFrequency parameter to 1.

Step 4

Restart the windows machine.

### Trunk Utilization and Reporting

#### DS0 Trunk
                              	 Information

Through Unified CVP,
                                 		Unified ICM passes the gateway trunk and DS0 information from the arriving SIP
                                 		call.

PSTN gateway trunk
                                 		and DS0 information received at ICM has the following purposes:

Reporting

Routing in the
                                       			 Unified CCE Script Editor where TrunkGroupID and TrunkGroupChannelNum
                                       			 information is available for routing decisions.

Following message is
                                 		used in the examples:

The PSTN trunk group
                                 		data comes from the PSTN Gateway in the SIP INVITE as shown:

```
Via: SIP/2.0/UDP
192.168.1.79:5060;x-route-tag="tgrp:2811-b-000";x-ds0num="ISDN 0/0/0:15
0/0/0:DS1 1:DS0";branch
```

The following logic
                                 		is used in Unified CVP to parse and pass the PSTN trunk group information to
                                 		Unified ICM:

- If tgrp: found TrunkGroupID =value after
                                             				  tgrp: > + < data between ISDN and :DS1 tags >· Using the above
                                          				example: TrunkGroupID
                                             				  = 2811-b-000<space>0/0/0:15 0/0/0.

TrunkGroupID
                                             				  = <I P addr of
                                                					 originating device in Via header > + < data between ISDN and:DS1
                                                					 tags >

Using the
                                             				  above example: TrunkGroupID=192.168.1.79<space>0/0/0:15 0/0/0.

- If found, TrunkGroupChannelNum = < value before the
                                             				  :DS0 >· Using the above example: TrunkGroupChannelNum = 1

TrunkGroupChannelNum = < max int
                                                					 value > to indicate we did not find the DS0 value.

Using the
                                             				  above example: TrunkGroupChannelNum = Integer.MAX_VALUE (2^31 - 1)

#### Trunk Utilization
                              	 Routing and Reporting

Through
                                 		the Trunk Utilization feature, a gateway is used for real-time Unified CVP
                                 		routing and Unified ICM reporting and scripting. A gateway pushes the status of
                                 		memory, DS0, DSP, and CPU to Unified CVP. Because this feature uses a push
                                 		method to send resource data to Unified CVP, resources are monitored more
                                 		closely and failover can occur faster when a device goes down or is out of
                                 		resources.

This feature has the following characteristics:

Each gateway can publish an SIP OPTIONS message with CPU, Memory, DS0, and DSP information to Unified CVP every three minutes
                                       when operation conditions are usual on the gateway.

The push interval is configurable through the Cisco IOS CLI on the gateway.

If a high watermark level is reached, the gateway sends the SIP OPTIONS message immediately with an Out-Of-Service = true indication, and does not send another OPTIONS message until the low watermark level is reached with an Out-Of-Service = false indication.

Up to five Resource Availability Indication (RAI) targets can be set up on the gateway.

Trunk
                                 		Utilization Routing can also be used to update trunk group status in the
                                 		Unified CCE router. A PSTN call (through the ICM script) can query the router
                                 		with a preroute from a NIC to use the available ingress gateway for the post
                                 		route to Unified CVP.

DS0 is the data
                                             		  line that provides utilization information about the number of trunks free on a
                                             		  gateway.

##### Gateway Trunk
                                 	 Utilization with Server Group Pinging Combination

When you combine the Server Group element polling feature with
                                    		the Cisco IOS Gateway trunk utilization feature, your solution has faster failover
                                    		for high availability call signaling.

##### Deployment
                                 	 Considerations

- Configure TDM originating
                                                				gateways for resource allocation indication-targets (RAI-targets) to provide
                                                				status in OPTIONS message to primary and secondary Unified CVP Call Servers,
                                                				for reporting purposes. The data is used for reporting, and not routing so the
                                                				data needs to be sent to Call Servers that have reporting enabled.

- Configure primary and
                                                				secondary CUSP proxy servers with Server Groups pinging to Unified CVP, VXML
                                                				Gateways, and Unified Communications Manager elements.

- Configure Unified CVP with
                                                				Server Group that pings to both primary and secondary CUSP proxies for outbound
                                                				calls.

- Configure TDM originating
                                                				gateways for RAI-targets to provide status in OPTIONS message to primary and
                                                				secondary Call Servers. Unified CVP can handle the messages for both reporting
                                                				and routing purposes. If used for routing, then the gateway must be in a server
                                                				group by itself on Unified CVP.

- Configure Unified CVP with
                                                				Server Groups that pings to Unified CVP, VXML Gateways, and Unified
                                                				Communications Manager elements for outbound calls.

- Configure VXML gateways for
                                                				RAI-targets to provide status in the OPTIONS message to primary and secondary
                                                				Call Servers.

Configure the
                                          			 Unified CVP Call Servers to send the same hostname in the contact header of
                                          			 OPTIONS requests to the gateways. This process enables a single RAI-target to
                                          			 be configured to all Call Servers and is important because the limit is five
                                          			 targets. The parameter to set is called Options Header Override.

See the Cisco IOS documentation for guidelines on the high and low watermark settings.

RAI is not
                                             			 supported on Proxy Servers.

CUSP servers do
                                             			 not handle the RAI header of OPTIONS messages, so they do not mark the status
                                             			 of elements with that information. If VXML Gateways are down, Unified CVP may
                                             			 send the call using the proxy, because the proxy does not handle incoming RAI
                                             			 headers in OPTIONS. It is possible to use a local static route scheme on
                                             			 Unified CVP to send all calls to the proxy except the Voice XML Gateways calls
                                             			 to create a server group for Voice XML Gateways and take advantage of RAI
                                             			 updates for routing.

### Apply Contact Center Gateway Debug Settings

Step 1

Log in to the
                                          gateway.

Step 2

Type enable and type your password to enter the enable mode.

Step 3

Enter the
                                          configure terminal command to enter configuration
                                          mode.

Step 4

Type ivr
                                             contact-center to apply default debug settings.

Step 5

Configure the logging buffer size using set logging
                                             buffer .

#### Example:

The  logging buffer size
                                                         should be  1000000 or more.

Step 6

Exit configuration mode and
                                          return to the enable prompt by pressing Ctrl-Z .

To view the current operating configuration, including the changes you made, enter the show
                                                            running-config command.

Step 7

To save the configuration changes, enter the write running-config
                                          startup-config command at the enable prompt.

#### Example:

```
User Access Verification                            
Password:                            
ccbu-doc-gw4>en                            
Password:                            
ccbu-doc-gw4#config t                            
Enter configuration commands, one per line.  End with CNTL/Z.                            
ccbu-doc-gw4(config)#ivr                            
ccbu-doc-gw4(config)#ivr contact-center                            
ccbu-doc-gw4(config)#^Z                           
ccbu-doc-gw4#show debug                            
....
```

### Network VRU
                           	 Types

In Unified ICME,
                                 		  Network VRU is a configuration database entity. It is accessed using the
                                 		  Network VRU Explorer tool of ICM Configuration Manager. A Network VRU entry
                                 		  contains the following information:

Type: A
                                       				number from 7, 8, and 10, which corresponds to one of the types.

Labels: This is a list
                                       				of labels, which Unified ICME can
                                       				use to transfer a call to the particular Network VRU that is being configured.
                                       				These labels are relevant for Network VRUs of Types 7 and 10. These types use
                                       				the Correlation ID mechanism to transfer calls. Labels for Type 8 are defined
                                       				in the Translation Route Explorer tool of ICM Configuration Manager, and are
                                       				invoked using a Translation Route to VRU node.

Each label
                                       				comprises the following components:

A digit
                                             					 string, which becomes a DNIS that is understood by a SIP Proxy Server, by a
                                             					 static route table, or by gateway dial-peers.

A routing
                                             					 client, also known as a switch leg peripheral. Each peripheral device that can
                                             					 act as a switch leg must have its own label, even if the digit strings are the
                                             					 same in all cases.

Unified ICME
                                 		  introduced Network VRU Type 10, which simplifies the configuration of Network
                                 		  VRU’s for Unified CVP. For most call flow models, a single Type 10 Network VRU
                                 		  can take the place of the Type 3, 5, 7, or 8 Network VRUs, which were
                                 		  associated with the Customer Instance and the Switch and VRU leg peripherals.
                                 		  The VRU-Only call flow models still require Type 8. However, in a specific case
                                 		  Type 7 is required.

Network VRU
                                 		  configuration entries themselves have no value until they are associated with
                                 		  active calls. Following are the three places in Unified ICME where you can
                                 		  perform this association:

Advanced tab
                                       				for a given peripheral in the PG Explorer tool of the ICM Configuration
                                       				Manager.

Customer
                                       				Instance configuration in the ICM Instance Explorer tool of the ICM
                                       				Configuration Manager.

On every VRU
                                       				Script configuration in the Network VRU Script List tool of the ICM
                                       				Configuration Manager.

Depending on the
                                 		  call flow model, use Unified ICME to search either the peripheral or the
                                 		  customer instance to determine how to transfer a call to a VRU. Unified ICME
                                 		  examines the following:

The Network
                                       				VRU and the Network VRU using the Translation Route mechanism. The network VRU
                                       				is associated with the switch leg peripheral when the call first arrives on a
                                       				switch leg and Network VRU is associated with the VRU leg peripheral when the
                                       				call is being transferred.

The Network
                                       				VRU from the System Information tool, when the call is being transferred to the
                                       				VRU using the Correlation ID mechanism. The Network VRU is associated with the
                                       				Customer Instance or the default Network VRU.

The Network VRU, which is associated with the VRU Script every time it encounters a RunExternalScript node in its routing
                                       script. If the call is currently not connected to the designated Network VRU, Unified ICME does not rune the VRU Script.

The previously
                                             			 supported VRU types still work with Unified ICME 7.1(1) and later for existing deployments. However, new installations should
                                             			 use Type 10 and existing deployments should switch to Type 10 on upgrade.

### SIP Dialed Number Pattern Matching Algorithm

Refer to the following points to create dialed
                                 number patterns:

Wildcarded DN patterns can contain "." and "X" in any position to match a single wildcard character.

Small letter "x" cannot be used as a wildcard.

Any of the wildcard characters in the set ">*!T" can match
                                       multiple characters. However, only one wildcard character can be used for trailing values, else they can always match with
                                       remaining characters in the string.

The
                                       highest precedence of pattern matching is an exact match, followed by the most
                                       specific wildcard match. When the number of characters is matched equally by
                                       more than one wildcarded pattern, precedence is given from top to bottom of the
                                       configured DN list.

There is no explicit software limit
                                       on the number of items in the DN pattern list.

## Additional Configuration Instructions

Comprehensive call flows for prerouted calls. See Comprehensive Call Flows for Pre-Routed Calls . 
                                    This
                                    class of call flows is similar to the Unified CVP Comprehensive call flow
                                    models, except that calls are first introduced into
                                    Unified ICME or Unified ICMH using a path
                                    other than through Unified CVP. A Unified ICME routing
                                    script is given the chance to preroute such calls before reaching Unified CVP. After the script transfers the call to Unified
                                    CVP for either
                                    self-service or queuing, the standard Unified CVP Comprehensive call flow
                                    model is used.

Common Unified ICMH Configuration for Unified CVP Switch Leg. See Configure Common Unified ICMH for Unified CVP Switch Leg . It describes Unified ICMH configuration instructions common to Comprehensive Unified ICMH and VRU-Only with NIC routing,
                                    with Correlation ID
                                    call routing call flow models for Unified CVP switch legs.

Common Unified ICMH Configuration: Define Unified CVP ECC Variables . It provides instructions
                                    on how to set up ECC variables that Unified CVP uses to exchange information
                                    with Unified ICMH.

Using the Metadata ECC Variable. See Metadata ECC Variable . It defines the values for the user.microapp.metadata ECC variable.

Common Configuration for Differentiating VRUs (Unified CVPs) Based on Dialed Number. See Common Configuration for Differentiating VRUs Based on Dialed Number . It provides instructions on how to configure
                                    Unified ICME to differentiate the VRUs.

SIP Proxy
                                    Redundancy. See Set Up Ingress Gateway to Use Redundant Proxy Servers and Set Up Call Server with Redundant Proxy Servers .

## Order of Device
                        	 Operations

Based on your
                              		  call flow model, set up the device operations in the following order.

Device
                                          					 Deployment

SIP
                                                						  Proxy Server device (optional)

Unified CVP Call Server device

Unified CVP VXML Server device

Unified CVP Reporting Server device

Other
                                                						  Devices (for example, Gateways and Unified CM)

System
                                          					 Configuration

SIP
                                                						  Server Groups

Dialed
                                                						  Number Pattern

Locations

Courtesy Callback

Miscellaneous

Register with Smart Licensing (required)

Transfer of VXML applications (required)

Bulk
                                                						  transfer of default Gateway files (required)

## Manage Devices

Step 1

Add new Unified CVP device.

Step 2

Configure Unified CVP device.

Step 3

Save and deploy Unified CVP device.

Step 4

Verify that Unified CVP devices are active in Operations Console.

Step 5

Deploy system-level configuration, Dialed Number Pattern, SIP Server Groups, Locations, and Courtesy Callback, and verify
                                       their statuses.

Step 6

Save and deploy the SNMP Configuration.

## Smart Licensing Configurations

Unified CVP Release12.5 uses the following configuration files for Smart Licensing operations.

C:\Cisco\CVP\conf\smartlicense.properties

C:\Cisco\CVP\conf\licensetype.properties

C:\Cisco\CVP\conf\Entitlementmapper.csv

Do not edit, delete, or access these files without contacting Cisco TAC. Any change to these files can cause operational impact.

Handling SocketTimeoutException :

If there is a delay in communication between the OMAP and CVP servers, and the SocketTimeoutException error is seen in the Catalina log, perform the following steps:

In the OAMP server, navigate to the following location: %CVP_HOME%\OPSConsoleServer\Tomcat\webapps\ROOT\WEB-INF\classes

Open the file shindig.properties and edit as follows:

Change shindig.http.client.connection-timeout-ms=5000 to shindig.http.client.connection-timeout-ms=10000 .

Add the read-timeout configuration after the connection-timeout configuration:

Save the shindig.properties file.

Restart the CVP OPS Console service and login to OAMP again.

| Step 1 | Have network
                                       			 information. See Network Information . |
|---|---|
| Step 2 | Perform ring
                                       			 no answer settings with SIP. See Ring No Answer Settings with SIP . |
| Step 3 | Install Unified CVP on your computer. For Unified CVP installation, see Installation and Upgrade
                                                				  Guide for Cisco Unified Customer Voice Portal at https://www.cisco.com/en/US/products/sw/custcosw/ps1006/prod_installation_guides_list.html and Unified CVP Installation . |
| Step 4 | Install Cisco
                                       			 Unified Intelligent Contact Management (ICM), Cisco Unified Communications
                                       			 Manager (CM), VXML and ingress gateways. |
| Step 5 | Ensure that you have login credentials for Operations Console and Reporting Server. To sign in to Operations Console and view
                                       its menus, see Operations Console . |
| Step 6 | Route calls
                                       			 through the network to the VRU. See Route Calls Through the Network to the VRU . |
| Step 7 | Configure
                                       			 ethernet switch/server NIC, gateways, and Call Server settings. See Ethernet Switch/Server NIC, Gateways and Call Server Settings . |
| Step 8 | Apply contact
                                       			 center gateway debug settings. Apply Contact Center Gateway Debug Settings . |
| Step 9 | Check the
                                       			 network VRU types. See the Network VRU Types . |
| Step 10 | Refer to the
                                       			 SIP dialed number pattern matching algorithm. See SIP Dialed Number Pattern Matching Algorithm . |
| Step 11 | Default
                                       			 security settings can prevent you from using Operations Console. Check your
                                       			 security policy and, if needed, change the settings to a less restrictive
                                       			 level. |

| Note | For
                                                   				  information about call flow models, see the Configuration Guide for
                                                            				  Cisco Unified Customer Voice Portal . |
|---|---|

| Note | If all the
                                                				dialed numbers use the same VRU, use the default Network VRU instead of
                                                				configuring multiple Network VRUs. For more information, see Configure Common Unified ICMH for Unified CVP Switch Leg . |
|---|---|

| Note | For information on IVR-related Service Control reporting and queue reporting, see the https://www.cisco.com/en/US/products/sw/custcosw/ps1844/products_user_guide_list.html and the https://www.cisco.com/en/US/products/sw/custcosw/ps1001/products_user_guide_list.html . For Unified CVP reporting, see Reporting Guide for Cisco Unified Customer Voice Portal available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html . |
|---|---|

| Note | For
                                                         						details about the required Ethernet Switch/Server NIC settings, see Ethernet Switch/Server NIC, Gateways and Call Server Settings . For details on design
                                                      					 considerations and guidelines for deploying enterprise network solutions that
                                                      					 includes Unified CVP, see the Configuration Guide for
                                                               				  Cisco Unified Customer Voice Portal . |
|---|---|

| Call Flows | Task |
|---|---|
| Using
                                             					 Network VRUs of Type 7 or 10 | Determine
                                             					 the Network Routing Number. This number is the base for routing calls through
                                             					 the network to the VRU. A correlation ID is appended to this number to transfer
                                             					 calls to a Network VRU through the network. |
| With a
                                             					 Customer VRU in Unified ICMH environments and for NIC Type 8 call flow models | Determine the translation route pools to use for each VRU. Determine the labels to be sent to the network to connect the
                                                      						  call to the VRU and the corresponding Dialed Number Identification Service
                                                      						  (DNIS) that is seen by the VRU. For example, the label for the network might be
                                                      						  18008889999 and the DNIS received by the VRU and sent back to Unified ICME to
                                                      						  identify the call might be 9999. |

| Caution | The Auto option is applicable only  for matched port/NIC at Gigabit Ethernet (1000 Mbps). If you are unsure of
                                          the adjacent station configuration, select 1000/Full on the Gigabit interface. You
                                          can use the Auto option only if both stations supply Gigabit interfaces. |
|---|---|

| Ethernet Switch Speed | Server/Gateway NIC Speed | Speed/Duplex Setting for Switch
                                             Port | Speed/Duplex Setting for
                                             Server/GW NIC |
|---|---|---|---|
| 1000 Mb | 1000 Mb | 1000/Full | 1000/Full |
| 1000 Mb | 1000 Mb | Auto/Auto | Auto/Auto |
| 1000 Mb | 100 Mb | 100 Mb/Full | 100 Mb/Full |
| 100 Mb | 100 Mb | 100 Mb/Full | 100 Mb/Full |
| 100 Mb | 1000 Mb | 100 Mb/Full | 100 Mb/Full |

| Step 1 | Open the registry of the
                                             			 machine. |
|---|---|
| Step 2 | Navigate to the following path: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\<Interface
                                                				GUID. |
| Step 3 | Set TcpAckFrequency parameter to 1. |
| Step 4 | Restart the windows machine. |

| Note | DS0 is the data
                                             		  line that provides utilization information about the number of trunks free on a
                                             		  gateway. |
|---|---|

| Note | See the Cisco IOS documentation for guidelines on the high and low watermark settings. |
|---|---|

| Step 1 | Log in to the
                                          gateway. |
|---|---|
| Step 2 | Type enable and type your password to enter the enable mode. |
| Step 3 | Enter the
                                          configure terminal command to enter configuration
                                          mode. |
| Step 4 | Type ivr
                                             contact-center to apply default debug settings. |
| Step 5 | Configure the logging buffer size using set logging
                                             buffer . Example: set logging buffer
                                             1000000 Note The  logging buffer size
                                                         should be  1000000 or more. | Note | The  logging buffer size
                                                         should be  1000000 or more. |
| Note | The  logging buffer size
                                                         should be  1000000 or more. |
| Step 6 | Exit configuration mode and
                                          return to the enable prompt by pressing Ctrl-Z . Note To view the current operating configuration, including the changes you made, enter the show
                                                            running-config command. | Note | To view the current operating configuration, including the changes you made, enter the show
                                                            running-config command. |
| Note | To view the current operating configuration, including the changes you made, enter the show
                                                            running-config command. |
| Step 7 | To save the configuration changes, enter the write running-config
                                          startup-config command at the enable prompt. Example: User Access Verification                            
Password:                            
ccbu-doc-gw4>en                            
Password:                            
ccbu-doc-gw4#config t                            
Enter configuration commands, one per line.  End with CNTL/Z.                            
ccbu-doc-gw4(config)#ivr                            
ccbu-doc-gw4(config)#ivr contact-center                            
ccbu-doc-gw4(config)#^Z                           
ccbu-doc-gw4#show debug                            
.... |

| Note | The  logging buffer size
                                                         should be  1000000 or more. |
|---|---|

| Note | To view the current operating configuration, including the changes you made, enter the show
                                                            running-config command. |
|---|---|

| Note | The previously
                                             			 supported VRU types still work with Unified ICME 7.1(1) and later for existing deployments. However, new installations should
                                             			 use Type 10 and existing deployments should switch to Type 10 on upgrade. |
|---|---|

| Note | Small letter "x" cannot be used as a wildcard. |
|---|---|

| Device Operations | Settings |
|---|---|
| Device
                                          					 Deployment | SIP
                                                						  Proxy Server device (optional) Unified CVP Call Server device Unified CVP VXML Server device Unified CVP Reporting Server device Other
                                                						  Devices (for example, Gateways and Unified CM) |
| System
                                          					 Configuration | SIP
                                                						  Server Groups Dialed
                                                						  Number Pattern Locations Courtesy Callback |
| Miscellaneous | Register with Smart Licensing (required) Transfer of VXML applications (required) Bulk
                                                						  transfer of default Gateway files (required) |

| Step 1 | Add new Unified CVP device. |
|---|---|
| Step 2 | Configure Unified CVP device. |
| Step 3 | Save and deploy Unified CVP device. |
| Step 4 | Verify that Unified CVP devices are active in Operations Console. |
| Step 5 | Deploy system-level configuration, Dialed Number Pattern, SIP Server Groups, Locations, and Courtesy Callback, and verify
                                       their statuses. |
| Step 6 | Save and deploy the SNMP Configuration. |

| Note | Do not edit, delete, or access these files without contacting Cisco TAC. Any change to these files can cause operational impact. |
|---|---|