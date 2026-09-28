---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-configuration-guide-32ab7f35d5
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/configuration/guide/ccvp_b_1501-configuration-guide-for-cisco-customer-voice-portal-release/gateway_configuration.html
retrieved_at: 2026-08-21T12:06:59.128127+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 15.0(1)

Updated: December 12, 2025

Chapter: Gateway Configuration

## Chapter: Gateway Configuration

# Gateway Configuration

## Configure Gateway

Step 1

Log in to Operations Console and click Device Management > Gateway .

The Find, Add, Delete, Edit Gateways window opens.

Step 2

Click Add New .

To use an existing Gateway as a template for configuring a
                                                      				new Gateway, select a Gateway from the list of available Gateways and click Use As Template and perform Steps 3 to 5.

Step 3

Click  the General tab, enter the field values, and click Save . See General Settings .

Step 4

(Optional) Click  the Device Pool tab, enter the field values, and click Save . See Add or Remove Device From Device Pool .

Step 5

Click Save .

Step 6

(Optional) If the
                                       call control client placed the Correlation ID in a GTD parameter other than
                                       uus.dat, specify the following parameters to configure a gateway to enable incoming UUI to be used
                                       as the Correlation ID.

```
conf t
                            application
                            service <your-cvp-service-name>
                            param use-uui-as-corrid Y (Refer to Note 1)
                            param correlation-gtd-attribute XXX (Refer to Note 2)
                            param correlation-gtd-instance N (Refer to Note 2)
                            param correlation-gtd-field YYY (Refer to Note 2)
                            dial-peer voice 123 pots
                            service <your-cvp-service-name>
```

## Gateway Settings

### General
                           	 Settings

After adding an IOS Gateway, you can run a subset of IOS Gateway commands on the Gateway from the Operations Console.

The Ingress
                                 		  Gateway is the point at which an incoming call enters the Unified CVP solution.
                                 		  It terminates Time Division Multiplexing (TDM) phone lines on one side and
                                 		  implements VoIP on the other side. It also provides for sophisticated call
                                 		  routing capabilities at the command of other Unified solution components. It
                                 		  works with SIP and also supports Media Gateway Control Protocol (MGCP) for use
                                 		  with Unified CM.

The service configuration parameters for the Call Server host and port are meant for the VRU-Only call flow model for IOS VoiceXML Gateway . These parameters are optional and you can use them to override the IP address or port number of the Call Server that comes
                                 through the SIP app-info header.

An Egress Gateway
                                 		  is typically used in Call Director model to provide access to a call center
                                 		  automatic call distributor (ACD) or third-party IVR.

To configure
                                 		  General settings on a Gateway, on the General tab, enter the field values, as listed in
                                 		  the following table:

Field

Description

Default

Value

Restart
                                             					 Required

IP Address

The IP
                                             					 address of a Unified ICM Server

None

Valid IP
                                             					 address

No

Hostname

The name
                                             					 of the Unified ICM Server

None

Valid DNS
                                             					 name. It includes alphanumeric characters and a dash.

No

Description

Additional
                                             					 information of the Unified ICM Server

None

Up to 1024
                                             					 characters

No

Device
                                             					 Admin URL

The URL
                                             					 for the Unified ICM Web configuration application.

None

Valid URL

No

#### Activate Gateway Configuration

Activate the gateway configuration
                                    by entering these commands:

Step 1

call application voice load
                                             CVPSelfService

Step 2

call
                                             application voice load HelloWorld

### Add Gateway to Device Pool

See Device Pool and Add or Remove Device From Device Pool .

## Configure Gateway
                        	 Settings for Comprehensive Call Flow Model

Step 1

Install the
                                       			 IOS image on the Ingress Gateway.

For detailed
                                          				information, see the Cisco IOS
                                             				  documentation .

Step 2

Transfer the
                                       			 following script, configuration, and .wav files to the Ingress gateway through
                                       			 the Operations Console or the Unified CVP product CD:

bootstrap.tcl

handoff.tcl

survivabilty.tcl

bootstrap.vxml

recovery.vxml

ringtone.tcl

cvperror.tcl

ringback.wav

critical_error.wav

Step 3

Configure the
                                       			 Ingress Gateway base settings.

Step 4

Configure the
                                       			 Ingress Gateway service settings.

Step 5

Configure an
                                       			 Ingress Gateway incoming Pots Dial-peer.

Step 6

For SIP without a
                                          				Proxy Server , complete the following steps:

If you
                                             				  are using DNS query with SRV or A types from the gateway, configure the gateway
                                             				  to use DNS.

Also, if
                                                					 you are using DNS query with SRV or A types from the gateway, use CLI as shown
                                                					 below:

Generally, a non-DNS setup is: sip-server ipv4:xx.xx.xxx.xxx:5060 .

```
ip domain name pats.cisco.com
ip name-server 10.86.129.16
sip-ua
sip-server dns:cvp.pats.cisco.com
OR:
ipv4:xx.xx.xxx.xxx:5060
```

Configure
                                             				  the DNS zone file for the separate DNS server that displays how the Service
                                             				  (SRV) records are configured.

SRV with
                                                            						DNS can be used in any of the SIP call flow models, with or without a Proxy
                                                            						server. Standard A type DNS queries can be used as well for the calls, without
                                                            						SRV, but they lose the load balancing and failover capabilities.

See DNS Zone File Configuration for Call Director Call Flow Model .

Step 7

For SIP with a
                                          				Proxy Server , if you are using the DNS Server, you can set your SIP Service
                                       			 as the Host Name (either A or SRV type).

```
ip host cvp4cc2.cisco.com 10.4.33.132
ip host cvp4cc3.cisco.com 10.4.33.133
ip host cvp4cc1.cisco.com 10.4.33.131
```

```
ip host _sip._tcp.cvp.cisco.com srv 50 50 5060 cvp4cc3.cisco.com
ip host _sip._tcp.cvp.cisco.com srv 50 50 5060 cvp4cc2.cisco.com
ip host _sip._tcp.cvp.cisco.com srv 50 50 5060 cvp4cc1.cisco.com
```

```
ip host _sip._udp.cvp.cisco.com srv 50 50 5060 cvp4cc3.cisco.com
ip host _sip._udp.cvp.cisco.com srv 50 50 5060 cvp4cc2.cisco.com
ip host _sip._udp.cvp.cisco.com srv 50 50 5060 cvp4cc1.cisco.com
```

The DNS
                                                      				  Server must be configured with all necessary A type or SRV type records.

See the SIP Devices Configuration and the Operations Console Online Help , Managing devices > Configuring a SIP Proxy Server for details.

Step 8

Configure
                                       			 SIP-Specific Actions.

On the Unified CM server, CCMAdmin Publisher, configure SIP-specific actions :

Create
                                             				  SIP trunks:

If
                                                      						  you are using a SIP Proxy Server, set up a SIP trunk to the SIP Proxy Server.

Add
                                                      						  a SIP Trunk for the Unified CVP Call Server.

Add
                                                      						  a SIP Trunk for each Ingress gateway that will send SIP calls to Unified CVP
                                                      						  that might be routed to Unified CM .

Select Device > Trunk > Add
                                                      						  New and add the following:

Trunk Type: SIP trunk

Device Protocol: SIP

Destination Address: IP address or host name of the SIP Proxy Server (if using
                                                      						  a SIP Proxy Server). If not using a SIP Proxy Server, enter the IP address or
                                                      						  host name of the Unified CVP Call Server.

DTMF Signaling Method: RFC 2833

Do not check the Media Termination Point Required checkbox.

If
                                                      						  you are using UDP as the outgoing transport on Unified CVP, also set the
                                                      						  outgoing transport to UDP on the SIP Trunk Security Profile.

Add
                                             				  route patterns for outbound calls from Unified CM devices using a SIP Trunk to the Unified CVP Call Server. Also, add a route
                                             				  pattern for error DN.

CVP
                                                            						solution does not support 100rel. On the SIP profile for the Trunk, confirm
                                                            						that SIP Rel1xx Options are disabled.

For
                                                            						warm transfers, the call from Agent 1 to Agent 2 does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the Unified CM Server and associate that number with your peripheral gateway user (PGUSER) for
                                                            						the JTAPI gateway on the Unified CM peripheral gateway. An alternative is to use the Dialed Number Plan on Unified ICME to
                                                            						bypass the CTI Route Point.

Select Call
                                                   						Routing > Route/Hunt > Route
                                                   						Pattern > Add New .

Route Pattern: Specify the route pattern; for example: 3xxx for a TDM phone
                                                      						  that dials 9+3xxx and all Unified ICME scripts are set up for 3xxx dialed numbers.

Gateway/Route List: Select the SIP Trunk defined in Step 2.

If you
                                             				  are sending calls to Unified CM using an SRV cluster domain name, configure the cluster domain name.

Select: Enterprise
                                                            								Parameters > Clusterwide Domain Configuration .

Add
                                                      						  the Cluster fully qualified domain name: FQDN .

For detailed instructions about using Unified CM and the CUSP Server, see the CUSP Server documentation .

Step 9

(Optional) Configure
                                       			 the SIP Proxy
                                          				Server .

From the CUSP Server Administration web page ( http://< CUSP server>/admin ):

Configure the SIP static routes to the Unified CVP Call Server(s), Unified CM SIP
                                             				  trunks, and Gateways.

Configure the SIP static routes for intermediary transfers for ring tone, playback dialed numbers, and error playback dialed
                                                numbers.

For failover and load balancing of calls to multiple destinations, configure the CUSP Server static route with priority and weight.

See the SIP Devices Configuration and SIP Dialed Number Pattern Matching Algorithm for detailed information.

Configure Access Control Lists for Unified CVP calls.

Select Proxy
                                                            								Settings > Incoming ACL .

Set
                                                      						  address pattern: all

Configure the service parameters.

Select Service Parameters , and set the following:

Add
                                                      						  record route: off

Maximum invite retransmission count: 2

Proxy Domain and Cluster Name: if using DNS SRV, set to the FQDN of your Proxy
                                                      						  Server SRV name.

Write
                                             				  down the IP address and host name of the SIP Proxy Server. You need this
                                             				  information when configuring the SIP Proxy Server in Unified CVP.

If
                                             				  using redundant SIP Proxy Servers (primary and secondary or load balancing),
                                             				  decide whether to use DNS server lookups for SRV records or non-DNS based local
                                             				  SRV record configuration.

The Comprehensive call flow model with SIP calls will typically be deployed with dual CUSP Servers for redundancy. In some cases, you might want to purchase a second CUSP Server. Regardless, the default transport for deployment will be UDP. Make sure you always set the AddRecordRoute setting to Off with CUSP Servers.

Configure the SRV records on the DNS server or locally on Unified CVP with an
                                                					 .xml file (local xml configuration avoids the overhead of DNS lookups with each
                                                					 call).

Step 10

Configure
                                       			 Peripheral Gateways (PGs).

On the NAM,
                                          				ICM Configuration Manager, PG
                                             				  Explorer tool, configure a peripheral gateway (PG) for the Unified CVP.
                                          				Configure a PG for each Unified CVP Call Server as follows:

In the tree
                                          				view pane, select the applicable PG.

Logical
                                             				  Controller tab:

Client
                                                					 Type: VRU

Name: A
                                                					 name descriptive of this PG

For
                                                					 example: <location>_A for side A of a particular location

Peripheral tab:

Peripheral Name: Descriptive name of this Unified CVP peripheral

For
                                                					 example: <location>_<cvp1> or <dns_name>

Client
                                                					 Type: VRU

Select: Enable Post-routing

Advanced tab:

Select
                                                					 the name of the Unified CVP VRU from the Network VRU field drop-down list.

For
                                                					 example: cvpVRU

Routing
                                             				  Client tab:

Name: By
                                                					 convention, use the same name as the peripheral

Client
                                                					 Type: VRU

If you
                                                					 are in a Unified ICMH environment and configuring the CICM, then do the following:

Do not select the Network Transfer Preferred checkbox

Routing client: INCRP NIC

## Configure Gateway
                        	 Settings for Call Director Call Flow Model

Step 1

Perform
                                       			 Steps 1 to 4 of the Configure Gateway Settings for Comprehensive Call Flow Model procedure.

Step 2

Configure the
                                       			 Ingress Gateway:

Configure
                                             				  the Ingress Gateway dial-peer for the Unified CVP Call Server.

Configure
                                             				  a dial-peer for ringtone and error.

If you
                                             				  are using a Proxy Server, configure your session target in the outbound dial
                                             				  peer to point to the Proxy Server.

If you
                                             				  are using the sip-server global configuration, then configure the sip-server in
                                             				  the sip-ua section to be your Proxy Server and point the session target of the
                                             				  dial-peer to the sip-server global variable.

Make sure
                                                      				  your dial plan includes this information. You will need to see the Dial plan
                                                      				  when you configure the SIP Proxy Server for Unified CVP.

The SIP
                                                      				  Service voip dial peer and the destination pattern on the Ingress Gateway must
                                                      				  match the DNIS in static routes on the SIP Proxy Server or Unified CVP Call
                                                      				  Server.

Step 3

For SIP
                                       			 without a Proxy Server, complete the following steps:

If you
                                             				  are using DNS query with SRV or A types from the gateway, configure the gateway
                                             				  to use DNS.

See the SIP Devices Configuration and Operations Console online help for detailed instructions. If you are using DNS query with SRV or A types from the gateway, use the gateway configuration
                                                CLI as shown below:

Non-DNS
                                                					 Setup:

```
sip-ua
sip-server ipv4:xx.xx.xxx.xxx:5060
!
```

DNS Setup:

```
ip domain name patz.cisco.com
ip name-server 10.10.111.16
!
sip-ua
sip-server dns:cvp.pats.cisco.com
!
```

Configure
                                             				  the DNS zone file for the separate DNS server that displays how the Service
                                             				  (SRV) records are configured.

SRV with
                                                            						DNS can be used in any of the SIP call flow models, with or without a Proxy
                                                            						server. Standard A type DNS queries can be used as well for the calls, without
                                                            						SRV, but they lose the load balancing and failover capabilities.

See the DNS Zone File Configuration for Call Director Call Flow Model for more information.

Step 4

For SIP with
                                       			 a Proxy Server, use one of the following methods:

You can
                                                      				  configure the Gateway statically instead of using DNS.

The following
                                          				example shows how both the A and SRV type records could be configured:

```
ip host cvp4cc2.cisco.com 10.4.33.132
ip host cvp4cc3.cisco.com 10.4.33.133
ip host cvp4cc1.cisco.com 10.4.33.131
```

For SIP/TCP :

```
ip host _sip._tcp.cvp.cisco.com srv 50 50 5060 cvp4cc3.cisco.com
ip host _sip._tcp.cvp.cisco.com srv 50 50 5060 cvp4cc2.cisco.com
ip host _sip._tcp.cvp.cisco.com srv 50 50 5060 cvp4cc1.cisco.com
```

For SIP/UDP :

```
ip host _sip._udp.cvp.cisco.com srv 50 50 5060 cvp4cc3.cisco.com
ip host _sip._udp.cvp.cisco.com srv 50 50 5060 cvp4cc2.cisco.com
ip host _sip._udp.cvp.cisco.com srv 50 50 5060 cvp4cc1.cisco.com
```

The DNS
                                                      				  Server must be configured with all necessary A type or SRV type records.

If you are
                                          				using the DNS Server, you can set your SIP Service as the Host Name (either A
                                          				or SRV type).

Step 5

On the Unified CM server, CCMAdmin Publisher, complete the following SIP-specific actions:

Create SIP
                                             				  trunks.

If
                                                      						  you are using a SIP Proxy Server, set up a SIP trunk to the SIP Proxy Server.

Add a
                                                      						  SIP Trunk for the Unified CVP Call Server.

Add a
                                                      						  SIP Trunk for each Ingress gateway that will send SIP calls to Unified CVP that
                                                      						  might be routed to Unified CM .

To add an
                                                					 SIP trunk, select Device > Trunk > Add
                                                      						  New and use the following parameters:

Trunk
                                                      						  Type: SIP
                                                         							 trunk

Device Protocol: SIP

Destination Address: IP address or host name of the SIP Proxy Server (if using
                                                      						  a SIP Proxy Server). If not using a SIP Proxy Server, enter the IP address or
                                                      						  host name of the Unified CVP Call Server.

DTMF Signaling Method: RFC 2833

Do not check the Media Termination Point Required check box.

If
                                                      						  you are using UDP as the outgoing transport on Unified CVP, also set the
                                                      						  outgoing transport to UDP on the SIP Trunk Security Profile.

Connection to CUSP Server: use 5060 as the default port.

Add
                                             				  route patterns for outbound calls from the Unified CM devices using a SIP Trunk to the Unified CVP Call Server. Also, add a route
                                             				  pattern for error DN.

Select Call
                                                      						  Routing > Route/Hunt > Route
                                                      						  Pattern > Add New

Add the
                                                					 following:

Route Pattern: Specify the route pattern; for example: 3XXX for a TDM phone that dials 9+3xxx and all Unified ICME scripts are set up for 3xxx dialed numbers.

Gateway/Route List: Select the SIP Trunk defined in the previous substep.

For
                                                            						warm transfers, the call from Agent 1 to Agent 2 does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the Unified CM server and associate that number with your peripheral gateway user (PGUSER) for
                                                            						the JTAPI gateway on the Unified CM peripheral gateway. An alternative is to use the Dialed Number Plan on Unified ICME to
                                                            						bypass the CTI Route Point.

If you
                                             				  are sending calls to Unified CM using an SRV cluster domain name, select Enterprise
                                                   						Parameters > Clusterwide Domain Configuration and
                                             				  add the Cluster fully qualified domain name FQDN .

Step 6

(Optionally) Configure the SIP Proxy
                                          				Server .

Configure the SIP static routes to the Unified CVP Call Servers, Unified CM SIP
                                             				  trunks, and Gateways.

Configure the SIP static routes for intermediary transfers for ringtone,
                                                					 playback dialed numbers, and error playback dialed numbers.

For failover and load balancing of calls to multiple destinations, configure the CUSP server static route with priority and weight.

Configure Access Control Lists for Unified CVP calls.

Select Proxy
                                                      						  Settings > Incoming ACL .

Address
                                                					 pattern: all

Configure the service parameters.

Select Service Parameters , then set the following:

Add
                                                      						  record route: off

Maximum invite retransmission count: 2

Proxy Domain and Cluster Name: if using DNS SRV, set to the FQDN of your Proxy
                                                      						  Server SRV name

Write
                                             				  down the IP address and host name of the SIP Proxy Server. (You need this
                                             				  information when configuring the SIP Proxy Server in Unified CVP.)

If
                                             				  using redundant SIP Proxy Servers (primary and secondary or load balancing),
                                             				  then decide whether to use DNS server lookups for SRV records or non-DNS based
                                             				  local SRV record configuration.

If a single CUSP Server is used, then SRV record usage is not required.

Configure the SRV records on the DNS server or locally on Unified CVP with a
                                                					 .xml file (local xml configuration avoids the overhead of DNS lookups with each
                                                					 call).

See
                                                            						the Local SRV File Configuration Example for SIP Messaging Redundancy section for details.

The Call Director call flow model with SIP calls will typically be deployed with dual CUSP servers for redundancy. In some cases, you might want to purchase a second CUSP server. Regardless, the default transport for deployment will be UDP; make sure you always disable the record-route in a CUSP server as this advanced feature is not supported in Contact Center deployments.

For the required settings in the Unified CM Publisher configuration, see Cisco Unified SIP Proxy documentation .

Step 7

Configure
                                       			 the PGs for the switch leg.

On Unified ICME ,
                                          				ICM Configuration Manager, PG
                                             				  Explorer tool:

Configure each peripheral gateway (PG) to be used for the Switch leg. In the tree view pane, select the applicable PG,
                                             				  and set the following:

Logical Controller tab:

Client Type: VRU

Name: A name descriptive of this PG

For example: <location>_A for side A of a particular location

Peripheral tab:

Peripheral Name: A name descriptive of this Unified CVP peripheral

For example: <location>_<cvp1> or <dns_name>

Client Type: VRU

Select the check box: Enable Post-routing

Routing Client tab:

Name: By convention, use the same name as the peripheral.

Client Type: VRU

For
                                                					 more information, see the ICM Configuration Guide for
                                                   						Cisco ICM Enterprise Edition .

Configure a peripheral for each Unified CVP Call Server to be used for a Switch
                                             				  leg connected to each peripheral gateway.

## Configure Gateway Settings for VRU-Only Call Flow Model: Type 8

Step 1

Using the Unified CVP Operations Console or the Unified CVP product CD, transfer the following script, configuration,
                                       and .wav files to the VoiceXML Gateway used for the VRU
                                       leg.
                                       Perform Step 2 of the Configure Gateway Settings for Comprehensive Call Flow Model procedure.

Step 2

Configure
                                       the VXML gateway base settings.

Step 3

Configure
                                       the VXML gateway service settings.

Step 4

Configure the ICM service.

Using the Operations
                                          Console, select Device Management > CVP Call Server > ICM
                                                tab . On each Unified CVP Call Server, configure the ICM Service by specifying the following required
                                          information:

VRU connection port
                                             number.

Set the VRU Connection Port to match
                                                the VRU connection Port defined in ICM Setup for the corresponding VRU
                                                peripheral gateway (PIM).

Maximum Length of DNIS.

Set the maximum
                                                length DNIS to a number which is at least the length of the translation route
                                                DNIS numbers.

Example: if the Gateway dial pattern is 1800******,
                                                the maximum DNIS length is 10.

Call service IDs: New Call and Pre-routed.

Enter the new and pre-routed call service IDs. Configure the ports for
                                                both groups according to the licenses purchased, call profiles, and capacity by
                                                completing the required fields on this tab.

Trunk group IDs: New Call and Pre-routed.

Enter the new and pre-routed call trunk group IDs

Configure the group number for the Pre-routed Call Trunk group. The group
                                                      number must match the trunk group number in the Network Trunk group used for
                                                      the translation route

Configure the number of ports
                                                      according to the licenses purchased and capacity

Configure each of the numbers used for translation routes. (The "New
                                                         Call" group is not used since the calls are being sent to the VRU (Unified CVP)
                                                      after some initial processing by the
                                                      NIC/ Unified ICME )

Dialed numbers used in the translation route.

Add the dialed numbers in the DNIS field.

Check the default values
                                             of the other settings and change, if
                                             desired.

### VoiceXML Gateway Configuration Examples

Applies a timestamp to debugging and log messages

Turns on logging

Turns off printing to the command line interface console

Sends RTP packets

Configures ASR/TTS Server

Configures gateway settings

Initiates the VoiceXML leg

Plays a .wav file that enables caller to hear message from critical_error.wav

Logs errors on the gateway when the call fails

```
service timestamps debug datetime msec
service timestamps log datetime msec
service internal
logging buffered 99999999 debugging
no logging console
ip cef
no ip domain lookup
ip host tts-en-us <IP of TTS or MRCP Server>
ip host asr-en-us <IP of ASR or MRCP Server>
voice rtp send-recv
!
voice service voip
allow-connections h323 to h323
signaling forward unconditional
h323
sip
min-se 360
header-passing
voice class codec 1
codec preference 1 g711ulaw
codec preference 2 g729r8
!
ivr prompt memory 15000
ivr prompt streamed none
ivr asr-server rtsp://asr-en-us/recognizer
ivr tts-server rtsp://tts-en-us/synthesizer
mrcp client timeout connect 10
mrcp client timeout message 10
mrcp client rtpsetup enable
rtsp client timeout connect 10
rtsp client timeout message 10
vxml tree memory 500
http client cache memory file 500
http client connection timeout 60
http client response timeout 30
http client connection idle timeout 10
gateway
timer receive-rtcp 6
!
ip rtcp report interval 3000
application
service new-call flash:bootstrap.vxml
service cvperror flash:cvperror.tcl
service handoff flash:handoff.tcl
```

```
dial-peer voice 777 voip
 description ICM VRU label
 service bootstrap
 voice-class codec 1
 incoming called-number <your sendtovru label pattern here> 
 dtmf-relay rtp-nte
 no vad
 !
```

## Configure Gateway
                        	 Settings for VRU-Only: Type 7

Step 1

Transfer the
                                       			 following script, configuration, and .wav files to the VoiceXML
                                          				Gateway used for the VRU leg, using the Unified CVP Operations Console. Perform Step 2 of the Configure Gateway Settings for Comprehensive Call Flow Model procedure.

Step 2

Configure the
                                       			 VoiceXML gateway base settings.

Step 3

Configure the
                                       			 VoiceXML gateway service settings.

Step 4

Configure the
                                       			 ICM Service for each Call Server.

In the
                                          				Operations Console, select Device
                                                					 Management > CVP Call Server > ICM
                                                					 tab . For each Unified CVP Call Server, configure the ICM
                                             				  Service by specifying the following required information:

VRU
                                             				  connection port number.

Set the
                                                					 VRU Connection Port to match the VRU connection Port defined in ICM Setup for
                                                					 the corresponding VRU peripheral gateway (PIM).

Set the
                                             				  maximum length DNIS to the length of the Network Routing Number.

Example:
                                                					 if the Gateway dial pattern is 1800******, the maximum DNIS length is 10.

Call
                                             				  service IDs: New Call and Pre-routed.

Enter the
                                                					 new and pre-routed call service IDs. Configure the ports for both groups
                                                					 according to the licenses purchased, call profiles, and capacity by completing
                                                					 the required fields on this tab

Trunk
                                             				  group IDs: New Call and Pre-routed.

Enter the
                                                					 new and pre-routed call trunk group IDs. Configure the group number for the
                                                					 Pre-routed Call Trunk group. The group number must match the trunk group number
                                                					 in the Network Trunk group used for the translation route.

Configure
                                                					 the number of ports according to the licenses purchased and capacity. Configure
                                                					 each of the numbers used for translation routes. (The "New
                                                   						Call" group is not used since the calls are being sent to the VRU (Unified
                                                					 CVP) after some initial processing by the NIC/ Unified ICME .)

Check the
                                             				  default values of other settings and change, if desired.

### VoiceXML
                              		  Gateway Configuration: Example Gateway Settings for Type 7

While using ASR/TTS, use a single version of MRCP (v1/v2) instead of using it in mixed mode.

The first part of
                              		  the following example provides the basic configuration for setting a VoiceXML
                              		  gateway:

Applies a
                                    				timestamp to debugging and log messages

Turns on
                                    				logging

Turns off
                                    				printing to the command line interface console

Sends RTP
                                    				packets

Configures
                                    				ASR/TTS Server

Configures
                                    				gateway settings

The last part of
                              		  this example provides the following:

Initiates the
                                    				VoiceXML leg

Plays a .wav
                                    				file that enables caller to hear message from critical_error.wav

Logs errors on
                                    				the gateway when the call fails

```
service timestamps debug datetime msec
service timestamps log datetime msec
service internal
logging buffered 99999999 debugging
no logging console
ip cef
no ip domain lookup
ip host tts-en-us <IP of TTS or MRCP Server>
ip host asr-en-us <IP of ASR or MRCP Server>
voice rtp send-recv
!
voice service voip
 allow-connections h323 to h323
 signaling forward unconditional
 h323
 sip
 min-se 360
 header-passing
voice class codec 1
 codec preference 1 g711ulaw
 codec preference 2 g729r8
!
ivr prompt memory 15000
ivr prompt streamed none
ivr asr-server rtsp://asr-en-us/recognizer
ivr tts-server rtsp://tts-en-us/synthesizer
mrcp client timeout connect 10
mrcp client timeout message 10
mrcp client rtpsetup enable
rtsp client timeout connect 10
rtsp client timeout message 10
vxml tree memory 500
http client cache memory pool 15000
http client cache memory file 500
http client connection timeout 60
http client response timeout 30
http client connection idle timeout 10
gateway
 timer receive-rtcp 6
!
ip rtcp report interval 3000
application
 service new-call flash:bootstrap.vxml
 service cvperror flash:cvperror.tcl
 service handoff flash:handoff.tcl
 service bootstrap flash:bootstrap.tcl
 !
```

The following
                              		  example provides the configuration for an ICM VRU label dial-peer for the Type
                              		  7 Unified CVP VRU-Only call flow model:

```
dial-peer voice 777 voip
 description ICM VRU label
 service bootstrap
 voice-class codec 1
 incoming called-number <your sendtovru label pattern here>
 dtmf-relay rtp-nte
 no vad
 !
```

## Transfer Script and Media File to Gateway

Transfer a single script or media file at a time from the Operations Console.

Step 1

Log in to the Operations Console and from the Device Management menu, select the type of server to
                                       			 which to transfer the script file.

### Example:

To transfer a script or a media
                                          			 file to a Gateway, select Device
                                                				  Management > Gateway ..

The Find, Add, Delete, Edit window lists any servers that have
                                          				been added to the Operations Console.

Step 2

Select a server by clicking the link in its Hostname field or
                                       			 by clicking the radio button preceding it and then clicking Edit .

Step 3

Select File Transfer in the toolbar, and then click Scripts and Media .

The Scripts and Media File Transfer page appears, listing the host
                                          				name and IP address for the selected device. Script and Media files currently
                                          				stored in the Operations Server database are listed in the Select From
                                             				available Script Files drop box.

Step 4

If the script or media file is not listed in the Select From
                                          			 Available Script Files drop box:

Click Select a Script or Media File from Your Local
                                                					 PC .

Enter the file name in the text box or click Browse to search for the script or media
                                             				  file on the local file system.

Step 5

If the script or media file is listed in the Select From
                                          			 Available Script Files drop box, select the script or media file.

Step 6

Click Transfer to send the file to the device.

## Configure Gateway Settings to modify Outgoing SIP Header

In some scenarios a gateway may need to interact with third-party ACDs, which requires modifications to certain SIP headers.

In this example, the SIP Refer-To header in the outgoing SIP REFER message is modified to pass the Application-to-Application
                           information (AAI) as User-to-User information (UUI):

Create SIP-Copylist.

```
voice class sip-copylist 1
 sip-header Refer-To
```

Create SIP-Profile.

```
voice class sip-profiles 1
 request REFER peer-header sip Refer-To copy ";(.*)" u01 
 request REFER sip-header Refer-To modify "Refer-To: (.*)" "Refer-To: <\1;\u01”
```

- Copy-list to be applied under the inbound dial-peer: voice-class sip copy-list 1.

- SIP-profiles to be applied under the outbound dial-peer: voice-class sip profiles 1.

```
Example:
==================================================================================================
1. Example of SIP copy-list:
voice class sip-copylist 2
sip-header Refer-To
 
2. Example of SIP Profile:
voice class sip-profiles 2
request REFER peer-header sip Refer-To copy ";aai=(.*)" u02
request REFER sip-header Refer-To modify "Refer-To: (.*)" "Refer-To: <\1;User-to-User=\u02"
 
3. Example of dial peer:
 
Dial peer to fwd the call to VVB
-----------------------------------------
dial-peer voice 345679 voip
destination-pattern 369852147
session protocol sipv2
session target ipv4:10.78.0.94
session transport tcp
voice-class sip copy-list 2
codec g711ulaw
 
Dial peer to modify the outgoing SIP REFER message
--------------------------------------------------------------------
dial-peer voice 345678 voip
session protocol sipv2
session target sip-server
session transport tcp
incoming called-number 369852147
voice-class sip profiles 2
codec g711ulaw
```

Once the aforesaid configuration is done, the SIP REFER message with the following SIP header:

Refer-To: <sip:1247@72.163.166.103; aai=PD%2C04%3BC8%2C48656c6c6520746865726521%3BFA%2C00001016421311070956 >

is modified to:

Refer-To: <sip:1247@72.163.166.103; User-to-User=PD%2C04%3BC8%2C48656c6c6520746865726521%3BFA%2C00001016421311070956 >

With similar configuration on gateway, other SIP headers can also be modified according to the call flow needs.

| Step 1 | Log in to Operations Console and click Device Management > Gateway . The Find, Add, Delete, Edit Gateways window opens. |
|---|---|
| Step 2 | Click Add New . Note To use an existing Gateway as a template for configuring a
                                                      				new Gateway, select a Gateway from the list of available Gateways and click Use As Template and perform Steps 3 to 5. | Note | To use an existing Gateway as a template for configuring a
                                                      				new Gateway, select a Gateway from the list of available Gateways and click Use As Template and perform Steps 3 to 5. |
| Note | To use an existing Gateway as a template for configuring a
                                                      				new Gateway, select a Gateway from the list of available Gateways and click Use As Template and perform Steps 3 to 5. |
| Step 3 | Click  the General tab, enter the field values, and click Save . See General Settings . |
| Step 4 | (Optional) Click  the Device Pool tab, enter the field values, and click Save . See Add or Remove Device From Device Pool . |
| Step 5 | Click Save . |
| Step 6 | (Optional) If the
                                       call control client placed the Correlation ID in a GTD parameter other than
                                       uus.dat, specify the following parameters to configure a gateway to enable incoming UUI to be used
                                       as the Correlation ID. conf t
                            application
                            service <your-cvp-service-name>
                            param use-uui-as-corrid Y (Refer to Note 1)
                            param correlation-gtd-attribute XXX (Refer to Note 2)
                            param correlation-gtd-instance N (Refer to Note 2)
                            param correlation-gtd-field YYY (Refer to Note 2)
                            dial-peer voice 123 pots
                            service <your-cvp-service-name> |

| Note | To use an existing Gateway as a template for configuring a
                                                      				new Gateway, select a Gateway from the list of available Gateways and click Use As Template and perform Steps 3 to 5. |
|---|---|

| Field | Description | Default | Value | Restart
                                             					 Required |
|---|---|---|---|---|
| IP Address | The IP
                                             					 address of a Unified ICM Server | None | Valid IP
                                             					 address | No |
| Hostname | The name
                                             					 of the Unified ICM Server | None | Valid DNS
                                             					 name. It includes alphanumeric characters and a dash. | No |
| Description | Additional
                                             					 information of the Unified ICM Server | None | Up to 1024
                                             					 characters | No |
| Device
                                             					 Admin URL | The URL
                                             					 for the Unified ICM Web configuration application. | None | Valid URL | No |

| Step 1 | call application voice load
                                             CVPSelfService |
|---|---|
| Step 2 | call
                                             application voice load HelloWorld |

| Step 1 | Install the
                                       			 IOS image on the Ingress Gateway. For detailed
                                          				information, see the Cisco IOS
                                             				  documentation . |
|---|---|
| Step 2 | Transfer the
                                       			 following script, configuration, and .wav files to the Ingress gateway through
                                       			 the Operations Console or the Unified CVP product CD: bootstrap.tcl handoff.tcl survivabilty.tcl bootstrap.vxml recovery.vxml ringtone.tcl cvperror.tcl ringback.wav critical_error.wav |
| Step 3 | Configure the
                                       			 Ingress Gateway base settings. |
| Step 4 | Configure the
                                       			 Ingress Gateway service settings. |
| Step 5 | Configure an
                                       			 Ingress Gateway incoming Pots Dial-peer. |
| Step 6 | For SIP without a
                                          				Proxy Server , complete the following steps: If you
                                             				  are using DNS query with SRV or A types from the gateway, configure the gateway
                                             				  to use DNS. Also, if
                                                					 you are using DNS query with SRV or A types from the gateway, use CLI as shown
                                                					 below: Note Generally, a non-DNS setup is: sip-server ipv4:xx.xx.xxx.xxx:5060 . ip domain name pats.cisco.com
ip name-server 10.86.129.16
sip-ua
sip-server dns:cvp.pats.cisco.com
OR:
ipv4:xx.xx.xxx.xxx:5060 Configure
                                             				  the DNS zone file for the separate DNS server that displays how the Service
                                             				  (SRV) records are configured. Note SRV with
                                                            						DNS can be used in any of the SIP call flow models, with or without a Proxy
                                                            						server. Standard A type DNS queries can be used as well for the calls, without
                                                            						SRV, but they lose the load balancing and failover capabilities. See DNS Zone File Configuration for Call Director Call Flow Model . | Note | Generally, a non-DNS setup is: sip-server ipv4:xx.xx.xxx.xxx:5060 . | Note | SRV with
                                                            						DNS can be used in any of the SIP call flow models, with or without a Proxy
                                                            						server. Standard A type DNS queries can be used as well for the calls, without
                                                            						SRV, but they lose the load balancing and failover capabilities. |
| Note | Generally, a non-DNS setup is: sip-server ipv4:xx.xx.xxx.xxx:5060 . |
| Note | SRV with
                                                            						DNS can be used in any of the SIP call flow models, with or without a Proxy
                                                            						server. Standard A type DNS queries can be used as well for the calls, without
                                                            						SRV, but they lose the load balancing and failover capabilities. |
| Step 7 | For SIP with a
                                          				Proxy Server , if you are using the DNS Server, you can set your SIP Service
                                       			 as the Host Name (either A or SRV type). You can also
                                          				configure the Gateway statically instead of using DNS. The following example
                                          				shows how both the A and SRV type records could be configured: ip host cvp4cc2.cisco.com 10.4.33.132
ip host cvp4cc3.cisco.com 10.4.33.133
ip host cvp4cc1.cisco.com 10.4.33.131 For SIP/TCP: ip host _sip._tcp.cvp.cisco.com srv 50 50 5060 cvp4cc3.cisco.com
ip host _sip._tcp.cvp.cisco.com srv 50 50 5060 cvp4cc2.cisco.com
ip host _sip._tcp.cvp.cisco.com srv 50 50 5060 cvp4cc1.cisco.com For SIP/UDP: ip host _sip._udp.cvp.cisco.com srv 50 50 5060 cvp4cc3.cisco.com
ip host _sip._udp.cvp.cisco.com srv 50 50 5060 cvp4cc2.cisco.com
ip host _sip._udp.cvp.cisco.com srv 50 50 5060 cvp4cc1.cisco.com Note The DNS
                                                      				  Server must be configured with all necessary A type or SRV type records. See the SIP Devices Configuration and the Operations Console Online Help , Managing devices > Configuring a SIP Proxy Server for details. | Note | The DNS
                                                      				  Server must be configured with all necessary A type or SRV type records. |
| Note | The DNS
                                                      				  Server must be configured with all necessary A type or SRV type records. |
| Step 8 | Configure
                                       			 SIP-Specific Actions. On the Unified CM server, CCMAdmin Publisher, configure SIP-specific actions : Create
                                             				  SIP trunks: If
                                                      						  you are using a SIP Proxy Server, set up a SIP trunk to the SIP Proxy Server. Add
                                                      						  a SIP Trunk for the Unified CVP Call Server. Add
                                                      						  a SIP Trunk for each Ingress gateway that will send SIP calls to Unified CVP
                                                      						  that might be routed to Unified CM . Select Device > Trunk > Add
                                                      						  New and add the following: Trunk Type: SIP trunk Device Protocol: SIP Destination Address: IP address or host name of the SIP Proxy Server (if using
                                                      						  a SIP Proxy Server). If not using a SIP Proxy Server, enter the IP address or
                                                      						  host name of the Unified CVP Call Server. DTMF Signaling Method: RFC 2833 Do not check the Media Termination Point Required checkbox. If
                                                      						  you are using UDP as the outgoing transport on Unified CVP, also set the
                                                      						  outgoing transport to UDP on the SIP Trunk Security Profile. Add
                                             				  route patterns for outbound calls from Unified CM devices using a SIP Trunk to the Unified CVP Call Server. Also, add a route
                                             				  pattern for error DN. Note CVP
                                                            						solution does not support 100rel. On the SIP profile for the Trunk, confirm
                                                            						that SIP Rel1xx Options are disabled. For
                                                            						warm transfers, the call from Agent 1 to Agent 2 does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the Unified CM Server and associate that number with your peripheral gateway user (PGUSER) for
                                                            						the JTAPI gateway on the Unified CM peripheral gateway. An alternative is to use the Dialed Number Plan on Unified ICME to
                                                            						bypass the CTI Route Point. Select Call
                                                   						Routing > Route/Hunt > Route
                                                   						Pattern > Add New . Route Pattern: Specify the route pattern; for example: 3xxx for a TDM phone
                                                      						  that dials 9+3xxx and all Unified ICME scripts are set up for 3xxx dialed numbers. Gateway/Route List: Select the SIP Trunk defined in Step 2. If you
                                             				  are sending calls to Unified CM using an SRV cluster domain name, configure the cluster domain name. Select: Enterprise
                                                            								Parameters > Clusterwide Domain Configuration . Add
                                                      						  the Cluster fully qualified domain name: FQDN . For detailed instructions about using Unified CM and the CUSP Server, see the CUSP Server documentation . | Note | CVP
                                                            						solution does not support 100rel. On the SIP profile for the Trunk, confirm
                                                            						that SIP Rel1xx Options are disabled. For
                                                            						warm transfers, the call from Agent 1 to Agent 2 does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the Unified CM Server and associate that number with your peripheral gateway user (PGUSER) for
                                                            						the JTAPI gateway on the Unified CM peripheral gateway. An alternative is to use the Dialed Number Plan on Unified ICME to
                                                            						bypass the CTI Route Point. |
| Note | CVP
                                                            						solution does not support 100rel. On the SIP profile for the Trunk, confirm
                                                            						that SIP Rel1xx Options are disabled. For
                                                            						warm transfers, the call from Agent 1 to Agent 2 does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the Unified CM Server and associate that number with your peripheral gateway user (PGUSER) for
                                                            						the JTAPI gateway on the Unified CM peripheral gateway. An alternative is to use the Dialed Number Plan on Unified ICME to
                                                            						bypass the CTI Route Point. |
| Step 9 | (Optional) Configure
                                       			 the SIP Proxy
                                          				Server . From the CUSP Server Administration web page ( http://< CUSP server>/admin ): Configure the SIP static routes to the Unified CVP Call Server(s), Unified CM SIP
                                             				  trunks, and Gateways. Configure the SIP static routes for intermediary transfers for ring tone, playback dialed numbers, and error playback dialed
                                                numbers. Note For failover and load balancing of calls to multiple destinations, configure the CUSP Server static route with priority and weight. See the SIP Devices Configuration and SIP Dialed Number Pattern Matching Algorithm for detailed information. Configure Access Control Lists for Unified CVP calls. Select Proxy
                                                            								Settings > Incoming ACL . Set
                                                      						  address pattern: all Configure the service parameters. Select Service Parameters , and set the following: Add
                                                      						  record route: off Maximum invite retransmission count: 2 Proxy Domain and Cluster Name: if using DNS SRV, set to the FQDN of your Proxy
                                                      						  Server SRV name. Write
                                             				  down the IP address and host name of the SIP Proxy Server. You need this
                                             				  information when configuring the SIP Proxy Server in Unified CVP. If
                                             				  using redundant SIP Proxy Servers (primary and secondary or load balancing),
                                             				  decide whether to use DNS server lookups for SRV records or non-DNS based local
                                             				  SRV record configuration. The Comprehensive call flow model with SIP calls will typically be deployed with dual CUSP Servers for redundancy. In some cases, you might want to purchase a second CUSP Server. Regardless, the default transport for deployment will be UDP. Make sure you always set the AddRecordRoute setting to Off with CUSP Servers. Configure the SRV records on the DNS server or locally on Unified CVP with an
                                                					 .xml file (local xml configuration avoids the overhead of DNS lookups with each
                                                					 call). | Note | For failover and load balancing of calls to multiple destinations, configure the CUSP Server static route with priority and weight. |
| Note | For failover and load balancing of calls to multiple destinations, configure the CUSP Server static route with priority and weight. |
| Step 10 | Configure
                                       			 Peripheral Gateways (PGs). On the NAM,
                                          				ICM Configuration Manager, PG
                                             				  Explorer tool, configure a peripheral gateway (PG) for the Unified CVP.
                                          				Configure a PG for each Unified CVP Call Server as follows: In the tree
                                          				view pane, select the applicable PG. Logical
                                             				  Controller tab: Client
                                                					 Type: VRU Name: A
                                                					 name descriptive of this PG For
                                                					 example: <location>_A for side A of a particular location Peripheral tab: Peripheral Name: Descriptive name of this Unified CVP peripheral For
                                                					 example: <location>_<cvp1> or <dns_name> Client
                                                					 Type: VRU Select: Enable Post-routing Advanced tab: Select
                                                					 the name of the Unified CVP VRU from the Network VRU field drop-down list. For
                                                					 example: cvpVRU Routing
                                             				  Client tab: Name: By
                                                					 convention, use the same name as the peripheral Client
                                                					 Type: VRU If you
                                                					 are in a Unified ICMH environment and configuring the CICM, then do the following: Do not select the Network Transfer Preferred checkbox Routing client: INCRP NIC |

| Note | Generally, a non-DNS setup is: sip-server ipv4:xx.xx.xxx.xxx:5060 . |
|---|---|

| Note | SRV with
                                                            						DNS can be used in any of the SIP call flow models, with or without a Proxy
                                                            						server. Standard A type DNS queries can be used as well for the calls, without
                                                            						SRV, but they lose the load balancing and failover capabilities. |
|---|---|

| Note | The DNS
                                                      				  Server must be configured with all necessary A type or SRV type records. |
|---|---|

| Note | CVP
                                                            						solution does not support 100rel. On the SIP profile for the Trunk, confirm
                                                            						that SIP Rel1xx Options are disabled. For
                                                            						warm transfers, the call from Agent 1 to Agent 2 does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the Unified CM Server and associate that number with your peripheral gateway user (PGUSER) for
                                                            						the JTAPI gateway on the Unified CM peripheral gateway. An alternative is to use the Dialed Number Plan on Unified ICME to
                                                            						bypass the CTI Route Point. |
|---|---|

| Note | For failover and load balancing of calls to multiple destinations, configure the CUSP Server static route with priority and weight. |
|---|---|

| Step 1 | Perform
                                       			 Steps 1 to 4 of the Configure Gateway Settings for Comprehensive Call Flow Model procedure. |
|---|---|
| Step 2 | Configure the
                                       			 Ingress Gateway: Configure
                                             				  the Ingress Gateway dial-peer for the Unified CVP Call Server. Configure
                                             				  a dial-peer for ringtone and error. If you
                                             				  are using a Proxy Server, configure your session target in the outbound dial
                                             				  peer to point to the Proxy Server. If you
                                             				  are using the sip-server global configuration, then configure the sip-server in
                                             				  the sip-ua section to be your Proxy Server and point the session target of the
                                             				  dial-peer to the sip-server global variable. Note Make sure
                                                      				  your dial plan includes this information. You will need to see the Dial plan
                                                      				  when you configure the SIP Proxy Server for Unified CVP. The SIP
                                                      				  Service voip dial peer and the destination pattern on the Ingress Gateway must
                                                      				  match the DNIS in static routes on the SIP Proxy Server or Unified CVP Call
                                                      				  Server. | Note | Make sure
                                                      				  your dial plan includes this information. You will need to see the Dial plan
                                                      				  when you configure the SIP Proxy Server for Unified CVP. The SIP
                                                      				  Service voip dial peer and the destination pattern on the Ingress Gateway must
                                                      				  match the DNIS in static routes on the SIP Proxy Server or Unified CVP Call
                                                      				  Server. |
| Note | Make sure
                                                      				  your dial plan includes this information. You will need to see the Dial plan
                                                      				  when you configure the SIP Proxy Server for Unified CVP. The SIP
                                                      				  Service voip dial peer and the destination pattern on the Ingress Gateway must
                                                      				  match the DNIS in static routes on the SIP Proxy Server or Unified CVP Call
                                                      				  Server. |
| Step 3 | For SIP
                                       			 without a Proxy Server, complete the following steps: If you
                                             				  are using DNS query with SRV or A types from the gateway, configure the gateway
                                             				  to use DNS. See the SIP Devices Configuration and Operations Console online help for detailed instructions. If you are using DNS query with SRV or A types from the gateway, use the gateway configuration
                                                CLI as shown below: Non-DNS
                                                					 Setup: sip-ua
sip-server ipv4:xx.xx.xxx.xxx:5060
! DNS Setup: ip domain name patz.cisco.com
ip name-server 10.10.111.16
!
sip-ua
sip-server dns:cvp.pats.cisco.com
! Configure
                                             				  the DNS zone file for the separate DNS server that displays how the Service
                                             				  (SRV) records are configured. Note SRV with
                                                            						DNS can be used in any of the SIP call flow models, with or without a Proxy
                                                            						server. Standard A type DNS queries can be used as well for the calls, without
                                                            						SRV, but they lose the load balancing and failover capabilities. See the DNS Zone File Configuration for Call Director Call Flow Model for more information. | Note | SRV with
                                                            						DNS can be used in any of the SIP call flow models, with or without a Proxy
                                                            						server. Standard A type DNS queries can be used as well for the calls, without
                                                            						SRV, but they lose the load balancing and failover capabilities. |
| Note | SRV with
                                                            						DNS can be used in any of the SIP call flow models, with or without a Proxy
                                                            						server. Standard A type DNS queries can be used as well for the calls, without
                                                            						SRV, but they lose the load balancing and failover capabilities. |
| Step 4 | For SIP with
                                       			 a Proxy Server, use one of the following methods: Note You can
                                                      				  configure the Gateway statically instead of using DNS. The following
                                          				example shows how both the A and SRV type records could be configured: ip host cvp4cc2.cisco.com 10.4.33.132
ip host cvp4cc3.cisco.com 10.4.33.133
ip host cvp4cc1.cisco.com 10.4.33.131 For SIP/TCP : ip host _sip._tcp.cvp.cisco.com srv 50 50 5060 cvp4cc3.cisco.com
ip host _sip._tcp.cvp.cisco.com srv 50 50 5060 cvp4cc2.cisco.com
ip host _sip._tcp.cvp.cisco.com srv 50 50 5060 cvp4cc1.cisco.com For SIP/UDP : ip host _sip._udp.cvp.cisco.com srv 50 50 5060 cvp4cc3.cisco.com
ip host _sip._udp.cvp.cisco.com srv 50 50 5060 cvp4cc2.cisco.com
ip host _sip._udp.cvp.cisco.com srv 50 50 5060 cvp4cc1.cisco.com Note The DNS
                                                      				  Server must be configured with all necessary A type or SRV type records. If you are
                                          				using the DNS Server, you can set your SIP Service as the Host Name (either A
                                          				or SRV type). | Note | You can
                                                      				  configure the Gateway statically instead of using DNS. | Note | The DNS
                                                      				  Server must be configured with all necessary A type or SRV type records. |
| Note | You can
                                                      				  configure the Gateway statically instead of using DNS. |
| Note | The DNS
                                                      				  Server must be configured with all necessary A type or SRV type records. |
| Step 5 | On the Unified CM server, CCMAdmin Publisher, complete the following SIP-specific actions: Create SIP
                                             				  trunks. If
                                                      						  you are using a SIP Proxy Server, set up a SIP trunk to the SIP Proxy Server. Add a
                                                      						  SIP Trunk for the Unified CVP Call Server. Add a
                                                      						  SIP Trunk for each Ingress gateway that will send SIP calls to Unified CVP that
                                                      						  might be routed to Unified CM . To add an
                                                					 SIP trunk, select Device > Trunk > Add
                                                      						  New and use the following parameters: Trunk
                                                      						  Type: SIP
                                                         							 trunk Device Protocol: SIP Destination Address: IP address or host name of the SIP Proxy Server (if using
                                                      						  a SIP Proxy Server). If not using a SIP Proxy Server, enter the IP address or
                                                      						  host name of the Unified CVP Call Server. DTMF Signaling Method: RFC 2833 Do not check the Media Termination Point Required check box. If
                                                      						  you are using UDP as the outgoing transport on Unified CVP, also set the
                                                      						  outgoing transport to UDP on the SIP Trunk Security Profile. Connection to CUSP Server: use 5060 as the default port. Add
                                             				  route patterns for outbound calls from the Unified CM devices using a SIP Trunk to the Unified CVP Call Server. Also, add a route
                                             				  pattern for error DN. Select Call
                                                      						  Routing > Route/Hunt > Route
                                                      						  Pattern > Add New Add the
                                                					 following: Route Pattern: Specify the route pattern; for example: 3XXX for a TDM phone that dials 9+3xxx and all Unified ICME scripts are set up for 3xxx dialed numbers. Gateway/Route List: Select the SIP Trunk defined in the previous substep. Note For
                                                            						warm transfers, the call from Agent 1 to Agent 2 does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the Unified CM server and associate that number with your peripheral gateway user (PGUSER) for
                                                            						the JTAPI gateway on the Unified CM peripheral gateway. An alternative is to use the Dialed Number Plan on Unified ICME to
                                                            						bypass the CTI Route Point. If you
                                             				  are sending calls to Unified CM using an SRV cluster domain name, select Enterprise
                                                   						Parameters > Clusterwide Domain Configuration and
                                             				  add the Cluster fully qualified domain name FQDN . | Note | For
                                                            						warm transfers, the call from Agent 1 to Agent 2 does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the Unified CM server and associate that number with your peripheral gateway user (PGUSER) for
                                                            						the JTAPI gateway on the Unified CM peripheral gateway. An alternative is to use the Dialed Number Plan on Unified ICME to
                                                            						bypass the CTI Route Point. |
| Note | For
                                                            						warm transfers, the call from Agent 1 to Agent 2 does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the Unified CM server and associate that number with your peripheral gateway user (PGUSER) for
                                                            						the JTAPI gateway on the Unified CM peripheral gateway. An alternative is to use the Dialed Number Plan on Unified ICME to
                                                            						bypass the CTI Route Point. |
| Step 6 | (Optionally) Configure the SIP Proxy
                                          				Server . Configure the SIP static routes to the Unified CVP Call Servers, Unified CM SIP
                                             				  trunks, and Gateways. Configure the SIP static routes for intermediary transfers for ringtone,
                                                					 playback dialed numbers, and error playback dialed numbers. Note For failover and load balancing of calls to multiple destinations, configure the CUSP server static route with priority and weight. Configure Access Control Lists for Unified CVP calls. Select Proxy
                                                      						  Settings > Incoming ACL . Address
                                                					 pattern: all Configure the service parameters. Select Service Parameters , then set the following: Add
                                                      						  record route: off Maximum invite retransmission count: 2 Proxy Domain and Cluster Name: if using DNS SRV, set to the FQDN of your Proxy
                                                      						  Server SRV name Write
                                             				  down the IP address and host name of the SIP Proxy Server. (You need this
                                             				  information when configuring the SIP Proxy Server in Unified CVP.) If
                                             				  using redundant SIP Proxy Servers (primary and secondary or load balancing),
                                             				  then decide whether to use DNS server lookups for SRV records or non-DNS based
                                             				  local SRV record configuration. Note If a single CUSP Server is used, then SRV record usage is not required. Configure the SRV records on the DNS server or locally on Unified CVP with a
                                                					 .xml file (local xml configuration avoids the overhead of DNS lookups with each
                                                					 call). Note See
                                                            						the Local SRV File Configuration Example for SIP Messaging Redundancy section for details. The Call Director call flow model with SIP calls will typically be deployed with dual CUSP servers for redundancy. In some cases, you might want to purchase a second CUSP server. Regardless, the default transport for deployment will be UDP; make sure you always disable the record-route in a CUSP server as this advanced feature is not supported in Contact Center deployments. For the required settings in the Unified CM Publisher configuration, see Cisco Unified SIP Proxy documentation . | Note | For failover and load balancing of calls to multiple destinations, configure the CUSP server static route with priority and weight. | Note | If a single CUSP Server is used, then SRV record usage is not required. | Note | See
                                                            						the Local SRV File Configuration Example for SIP Messaging Redundancy section for details. |
| Note | For failover and load balancing of calls to multiple destinations, configure the CUSP server static route with priority and weight. |
| Note | If a single CUSP Server is used, then SRV record usage is not required. |
| Note | See
                                                            						the Local SRV File Configuration Example for SIP Messaging Redundancy section for details. |
| Step 7 | Configure
                                       			 the PGs for the switch leg. On Unified ICME ,
                                          				ICM Configuration Manager, PG
                                             				  Explorer tool: Configure each peripheral gateway (PG) to be used for the Switch leg. In the tree view pane, select the applicable PG,
                                             				  and set the following: Logical Controller tab: Client Type: VRU Name: A name descriptive of this PG For example: <location>_A for side A of a particular location Peripheral tab: Peripheral Name: A name descriptive of this Unified CVP peripheral For example: <location>_<cvp1> or <dns_name> Client Type: VRU Select the check box: Enable Post-routing Routing Client tab: Name: By convention, use the same name as the peripheral. Client Type: VRU For
                                                					 more information, see the ICM Configuration Guide for
                                                   						Cisco ICM Enterprise Edition . Configure a peripheral for each Unified CVP Call Server to be used for a Switch
                                             				  leg connected to each peripheral gateway. |

| Note | Make sure
                                                      				  your dial plan includes this information. You will need to see the Dial plan
                                                      				  when you configure the SIP Proxy Server for Unified CVP. The SIP
                                                      				  Service voip dial peer and the destination pattern on the Ingress Gateway must
                                                      				  match the DNIS in static routes on the SIP Proxy Server or Unified CVP Call
                                                      				  Server. |
|---|---|

| Note | SRV with
                                                            						DNS can be used in any of the SIP call flow models, with or without a Proxy
                                                            						server. Standard A type DNS queries can be used as well for the calls, without
                                                            						SRV, but they lose the load balancing and failover capabilities. |
|---|---|

| Note | You can
                                                      				  configure the Gateway statically instead of using DNS. |
|---|---|

| Note | The DNS
                                                      				  Server must be configured with all necessary A type or SRV type records. |
|---|---|

| Note | For
                                                            						warm transfers, the call from Agent 1 to Agent 2 does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the Unified CM server and associate that number with your peripheral gateway user (PGUSER) for
                                                            						the JTAPI gateway on the Unified CM peripheral gateway. An alternative is to use the Dialed Number Plan on Unified ICME to
                                                            						bypass the CTI Route Point. |
|---|---|

| Note | For failover and load balancing of calls to multiple destinations, configure the CUSP server static route with priority and weight. |
|---|---|

| Note | If a single CUSP Server is used, then SRV record usage is not required. |
|---|---|

| Note | See
                                                            						the Local SRV File Configuration Example for SIP Messaging Redundancy section for details. |
|---|---|

| Step 1 | Using the Unified CVP Operations Console or the Unified CVP product CD, transfer the following script, configuration,
                                       and .wav files to the VoiceXML Gateway used for the VRU
                                       leg.
                                       Perform Step 2 of the Configure Gateway Settings for Comprehensive Call Flow Model procedure. |
|---|---|
| Step 2 | Configure
                                       the VXML gateway base settings. |
| Step 3 | Configure
                                       the VXML gateway service settings. |
| Step 4 | Configure the ICM service. Using the Operations
                                          Console, select Device Management > CVP Call Server > ICM
                                                tab . On each Unified CVP Call Server, configure the ICM Service by specifying the following required
                                          information: VRU connection port
                                             number. Set the VRU Connection Port to match
                                                the VRU connection Port defined in ICM Setup for the corresponding VRU
                                                peripheral gateway (PIM). Maximum Length of DNIS. Set the maximum
                                                length DNIS to a number which is at least the length of the translation route
                                                DNIS numbers. Example: if the Gateway dial pattern is 1800******,
                                                the maximum DNIS length is 10. Call service IDs: New Call and Pre-routed. Enter the new and pre-routed call service IDs. Configure the ports for
                                                both groups according to the licenses purchased, call profiles, and capacity by
                                                completing the required fields on this tab. Trunk group IDs: New Call and Pre-routed. Enter the new and pre-routed call trunk group IDs Configure the group number for the Pre-routed Call Trunk group. The group
                                                      number must match the trunk group number in the Network Trunk group used for
                                                      the translation route Configure the number of ports
                                                      according to the licenses purchased and capacity Configure each of the numbers used for translation routes. (The "New
                                                         Call" group is not used since the calls are being sent to the VRU (Unified CVP)
                                                      after some initial processing by the
                                                      NIC/ Unified ICME ) Dialed numbers used in the translation route. Add the dialed numbers in the DNIS field. Check the default values
                                             of the other settings and change, if
                                             desired. |

| Step 1 | Transfer the
                                       			 following script, configuration, and .wav files to the VoiceXML
                                          				Gateway used for the VRU leg, using the Unified CVP Operations Console. Perform Step 2 of the Configure Gateway Settings for Comprehensive Call Flow Model procedure. |
|---|---|
| Step 2 | Configure the
                                       			 VoiceXML gateway base settings. |
| Step 3 | Configure the
                                       			 VoiceXML gateway service settings. |
| Step 4 | Configure the
                                       			 ICM Service for each Call Server. In the
                                          				Operations Console, select Device
                                                					 Management > CVP Call Server > ICM
                                                					 tab . For each Unified CVP Call Server, configure the ICM
                                             				  Service by specifying the following required information: VRU
                                             				  connection port number. Set the
                                                					 VRU Connection Port to match the VRU connection Port defined in ICM Setup for
                                                					 the corresponding VRU peripheral gateway (PIM). Set the
                                             				  maximum length DNIS to the length of the Network Routing Number. Example:
                                                					 if the Gateway dial pattern is 1800******, the maximum DNIS length is 10. Call
                                             				  service IDs: New Call and Pre-routed. Enter the
                                                					 new and pre-routed call service IDs. Configure the ports for both groups
                                                					 according to the licenses purchased, call profiles, and capacity by completing
                                                					 the required fields on this tab Trunk
                                             				  group IDs: New Call and Pre-routed. Enter the
                                                					 new and pre-routed call trunk group IDs. Configure the group number for the
                                                					 Pre-routed Call Trunk group. The group number must match the trunk group number
                                                					 in the Network Trunk group used for the translation route. Configure
                                                					 the number of ports according to the licenses purchased and capacity. Configure
                                                					 each of the numbers used for translation routes. (The "New
                                                   						Call" group is not used since the calls are being sent to the VRU (Unified
                                                					 CVP) after some initial processing by the NIC/ Unified ICME .) Check the
                                             				  default values of other settings and change, if desired. |

| Note | While using ASR/TTS, use a single version of MRCP (v1/v2) instead of using it in mixed mode. |
|---|---|

| Step 1 | Log in to the Operations Console and from the Device Management menu, select the type of server to
                                       			 which to transfer the script file. Example: To transfer a script or a media
                                          			 file to a Gateway, select Device
                                                				  Management > Gateway .. The Find, Add, Delete, Edit window lists any servers that have
                                          				been added to the Operations Console. |
|---|---|
| Step 2 | Select a server by clicking the link in its Hostname field or
                                       			 by clicking the radio button preceding it and then clicking Edit . |
| Step 3 | Select File Transfer in the toolbar, and then click Scripts and Media . The Scripts and Media File Transfer page appears, listing the host
                                          				name and IP address for the selected device. Script and Media files currently
                                          				stored in the Operations Server database are listed in the Select From
                                             				available Script Files drop box. |
| Step 4 | If the script or media file is not listed in the Select From
                                          			 Available Script Files drop box: Click Select a Script or Media File from Your Local
                                                					 PC . Enter the file name in the text box or click Browse to search for the script or media
                                             				  file on the local file system. |
| Step 5 | If the script or media file is listed in the Select From
                                          			 Available Script Files drop box, select the script or media file. |
| Step 6 | Click Transfer to send the file to the device. |