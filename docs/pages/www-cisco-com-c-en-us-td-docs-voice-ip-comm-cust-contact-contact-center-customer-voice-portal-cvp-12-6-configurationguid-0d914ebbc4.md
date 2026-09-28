---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-configurationguid-0d914ebbc4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/ConfigurationGuideCVP12_6/guide/ccvp_b_1261-configuration-guide-for-cisco-unified-customer-voice-portal/ccvp_m_1261-configure-gateways.html
retrieved_at: 2026-08-21T06:53:00.481995+00:00
---

Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

# Configuration Guide for Cisco Unified Customer Voice Portal, Release 12.6(1)

Updated: June 11, 2024

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

The VXML Gateway hosts the IOS voice browser, the component which interprets VXML pages from either the Unified CVP IVR service or the VXML Server, plays
                                 .wav files and Text-to-Speech (TTS), inputs voice and Dual Tone Multi Frequency (DTMF), and sends results back to the VXML
                                 requestor. It also mediates between Media Servers, Unified CVP VXML Servers, ASR and TTS Servers, and the interactive voice
                                 response (IVR) service.

You can deploy the Ingress Gateway separately from the VXML Gateway , but in most implementations they are the same: one Gateway performs both functions. Gateways are often deployed in farms,
                                 for centralized deployment models. In Branch deployment models, one combined Gateway is usually located at each branch office.

The service configuration parameters for the Call Server host and port are meant for the VRU-Only call flow model for IOS VoiceXML Gateway . These parameters are optional and you can use them to override the IP address or port number of the Call Server that comes
                                 through the SIP app-info header.

```
application
service vru-leg flash:bootstrap.tcl
param cvpserverhost xxx.xxx.xxx.xxx		<IP of primary Call Server>
param cvpserverbackup xxx.xxx.xxx.xxx		<IP of backup Call Server>
param cvpserverport 7000 <TCP Port # of Call Server>
```

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

### Activate Gateway Configuration

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
                        	 Settings for Standalone Call Flow Model

After you
                              		  configure a gateway through Operations Console, configure settings on the
                              		  gateway.

Step 1

All Versions: Transfer
                                       			 the following script, configuration, and .wav files using the Operations
                                       			 Console or through the Unified CVP CD:

CVPSelfService.tcl

CVPSelfServiceBootstrap.vxml

critical_error.wav

Select Bulk
                                                   						Administration > File Transfer > Scripts and
                                                   						Media .

From the Select device type drop-down list, select Gateway .

Select the
                                             				  required file from the Available list, and click the right arrow to move
                                             				  the device to the Selected list.

Click Transfer .

Step 2

All Versions: Perform
                                       			 Steps from the Configure VXML Server Standalone Call Flow Model procedure.

### Example: Gateway Settings for Standalone Call Flow Model

The first part of the following example provides the basic
                                 configuration for setting a VoiceXML Standalone gateway:

Applies a timestamp to debugging and log messages

Turns on logging

Turns off printing to the command
                                       line interface console

Sends RTP packets

Configures ASR/TTS Server

Configures gateway
                                       settings

The last part ( application ) of this example
                                 provides the following information:

Standalone Service settings
                                       for hello_world application on the VXML Server

Service
                                       requirements for configuring self-service call flow models

```
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
!
service internal
logging buffered 99999999 debugging
no logging console
!
ip cef
!
voice rtp send-recv

ip host tts-en-us <IP of TTS or MRCP Server>
ip host asr-en-us <IP of ASR or MRCP Server>

voice class codec 1
codec preference 1 g711ulaw codec preference 2 g729r8 voice service voip
signaling forward unconditional
h323
!
gateway
timer receive-rtcp 6
!
ip rtcp report interval 3000
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

application
service hello_world flash:CVPSelfService.tcl
param CVPPrimaryVXMLServer <ip address>
param CVPBackupVXMLServer <ip address>
param CVPSelfService-port 7000
param CVPSelfService-SSL 0
-OR-
param CVPSelfService-port 7443
param CVPSelfService-SSL 1
param CVPSelfService-app HelloWorld

service CVPSelfService
flash:CVPSelfServiceBootstrap.vxml
!
```

Important

### Example: Dial-Peer for Standalone Call Flow Model with VXML Gateway

The following example provides the configuration for an incoming
                                 Pots and VoIP call for the VXML Server (standalone) call flow
                                 model:

```
dial-peer voice 8 pots                        
 description Example incoming POTS dial-peer calling HelloWorld VXML 

Server app                        
 service hello_world                          
 incoming called-number <your DN pattern here>        
 direct-inward-dial

                            
dial-peer voice 800 voip                            
 description Example incoming VOIP dial-peer calling HelloWorld VXML 

Server app                            
 service hello_world                            
 incoming called-number 800.......                            
 voice-class codec 1                            
 dtmf-relay rtp-nte                            
 no vad                            
!
```

### Example: Dial-Peer for Standalone Call Flow Model with Cisco VVB

The following example provides the configuration for an outbound dial-peer VoIP for the VXML Server (standalone) call flow
                                 model with Cisco VVB:

```
dial-peer voice 8181 voip
description dial-peer to CVVB Selfservice application trigger 
session protocol sipv2
session target ipv4:<destination IP_address for Cisco VVB>
session transport tcp
codec g711ulaw
destination-pattern 1800T
dtmf-relay rtp-nte
no vad
```

1800XXX is the number dialed which is added as a trigger in Cisco VVB for the self-service application.

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

Transfer files to the VXML Gateway using Step 2.

Step 9

Configure the VXML Gateway base settings.

Step 10

Configure the VXML Gateway service settings.

Step 11

If using ASR and TTS Servers, specify IP addresses for those servers for each locale using the applicable name resolution
                                       system for the Gateway (DNS or "ip host" commands).

If ASR and TTS use the same server, the MRCP server might allocate one license for the ASR session and a second license for
                                                      the TTS section. If you are hosting both ASR and TTS on the same speech server, you must select the ASR/TTS use the same MRCP server option in the IVR Service configuration tab in the Operations Console and follow the instructions in the step below.

Do one of the following:

The primary and backup servers must be configured. If using name resolution local to the Gateway (rather than DNS) specify:

ip host asr- <locale> <ASR server for locale>

ip host asr- <locale> -backup <backup ASR server for locale>

ip host tts- <locale> <TTS server for locale>

ip host tts- <locale> -backup <backup TTS server for locale>

Example for English US, use:

ip host asr-en-us 10.86.129.215

Step 12

If you want
                                       			 the ASR and TTS to use the same MRCP server option, you must configure the
                                       			 gateway as follows.

In the
                                             				  IVR Service in the Operations Console, select the ASR/TTS
                                                					 use the same MRCP server option.

Add the
                                             				  following two host names to the gateway configuration:

ip
                                                      						  host asrtts- <locale> <IP Address Of MRCP Server>

ip
                                                      						  host asrtts- <locale> -backup <IP Address Of MRCP
                                                         							 Server>

Where the locale might be something like en-us or es-es,
                                                      						  resulting in asrtts-en-us or asrtts-es-es .

Change
                                             				  the 'ivr asr-server' and 'ivr tts-server' lines as follows for MRCPV1:

ivr
                                                      						  asr-server rtsp://asr-en-server/recognizer

ivr
                                                      						  tts-server rtsp://tts-en-server/synthesizer

Change
                                             				  the 'ivr asr-server' and 'ivr tts-server' lines as follows for MRCPV2:

ivr asr-server sip:asr@10.78.26.103

ivr tts-server sip:tts@10.78.26.103

Step 13

Configure
                                       			 the speech servers to work with Unified CVP.

Caution

The
                                                      				  Operations Console can only manage speech servers installed on Windows , not on Linux. If the speech server is installed on
                                                      				  Linux, the server cannot be managed.

To ensure
                                          				that the speech servers work with Unified CVP, you must make the following
                                          				changes on each speech server as part of configuring the Unified CVP solution.

If you are
                                          				using Nuance SpeechWorks MediaServer (SWMS), the configuration file is
                                          				osserver.cfg. If you are using Nuance Speech Server (NSS), the configuration
                                          				file is NSSserver.cfg.

Make the
                                          				following changes to the Nuance configuration file:

Change: server.resource.2.url VXIString media/speechrecognizer

To: server.resource.2.url VXIString recognizer

Change: server.resource.4.url VXIString media/speechsynthesizer

To: server.resource.4.url VXIString synthesizer

Change: server.mrcp1.resource.3.url VXIString media/speechrecognizer

To: server.mrcp1.resource.3.url VXIString /recognizer

Change: server.mrcp1.resource.2.url VXIString media/speechsynthesizer

To: server.mrcp1.resource.2.url VXIString media/synthesizer

Change: server.mrcp1.transport.port VXIInteger 4900

To: server.mrcp1.transport.port VXIInteger 554

If you are using Nuance Speech Server 5 and Nuance Vocalizer for Network 5, then make changes to the configuration files
                                          for each application. Make the following changes to the Nuance Speech Server 5 configuration file (NSSserver.cfg):

Change: server.mrcp1.resource.3.url VXIString media/speechrecognizer

To: server.mrcp1.resource.3.url VXIString /recognizer

Change: server.mrcp1.resource.2.url VXIString media/speechsynthesizer

To: server.mrcp1.resource.2.url VXIString /synthesizer

Change: server.mrcp1.transport.port VXIInteger 4900

To: server.mrcp1.transport.port VXIInteger 554

Change: server.mrcp1.transport.dtmfPayloadType VXIInteger 96

To: server.mrcp1.transport.dtmfPayloadType VXIInteger 101

Uncomment the
                                                   						following: server.rtp.dtmfTriggerLeading VXIInteger 0

If you
                                                					 are using the Nuance Vocalizer for Network 5 TTS System, the following
                                                					 configuration files will need to be updated:

<install path>\Nuance Vocalizer for Network 5.0\config\ttsrshclient.xml

Change: <ssml_validation>strict</ssml_validation>

To: <ssml_validation>warn</ssml_validation>

<install path>\Nuance Vocalizer for Network 5.0\config\ttssapi.xml

Change: <ssml_validation>strict</ssml_validation>

To: <ssml_validation>warn</ssml_validation>

If you are using Nuance Recognizer 10.0 and Nuance Speech Server 6.2, make the following changes to the Nuance configuration
                                          file (NSSserver.cfg - C:\Program Files (x86)\Nuance\Speech Server\Server\config):

Change: server.mrcp1.resource.3.url VXIString
                                                					 media/speechrecognizer

To: server.mrcp1.resource.3.url VXIString /recognizer

Change: server.mrcp1.resource.2.url VXIString media/speechsynthesizer

To: server.mrcp1.resource.2.url VXIString /synthesizer

Change : server.mrcp1.transport.port VXIInteger 4900

To: server.mrcp1.transport.port VXIInteger 554

Change: server.mrcp1.transport.dtmfPayloadType VXIInteger 96

To: server.mrcp1.transport.dtmfPayloadType VXIInteger

Make the
                                          				following change to the Baseline.xml file C:\Program Files\Nuance\Recognizer\config

Change: <ssml_validation>strict</ssml_validation>

To: <ssml_validation>warn</ssml_validation>.

If you are using Nuance Recognizer 10.5 and Nuance Speech Server 6.5, then refer to the relevant Nuance Speech Suite Install
                                          Guide available at https://network.nuance.com/portal/server.pt/directory/nuance_speech_suite_10_5/16535 .

If you are using Nuance Recognizer 11.0 and Nuance Speech Server 7.0, then refer to the relevant Nuance Speech Suite Install
                                          Guide available at https://network.nuance.com/portal/server.pt/directory/nuance_speech_suite_11_0 .

Step 14

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

For
                                          				detailed instructions about using Unified CM and the CUSP Server, see the Cisco Unified SIP Proxy Server
                                             				  documentation .

Step 15

(Optional) Configure
                                       			 the SIP Proxy
                                          				Server .

From the
                                          				CUSP Server Administration web page ( http://<CUSP server>/admin ):

Configure the SIP static routes to the Unified CVP Call Server(s), Unified CM SIP
                                             				  trunks, and Gateways.

Configure the SIP static routes for intermediary transfers for ring tone, playback dialed numbers, and error playback dialed
                                                numbers.

For failover and load balancing of calls to multiple destinations, configure the CUSP Server static route with priority and
                                                            weight.

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

The
                                                					 Comprehensive call flow model with SIP calls will typically be deployed with
                                                					 dual CUSP Servers for redundancy. In some cases, you might want to purchase a
                                                					 second CUSP Server. Regardless, the default transport for deployment will be
                                                					 UDP. Make sure you always set the AddRecordRoute setting to Off with CUSP Servers.

Configure the SRV records on the DNS server or locally on Unified CVP with an
                                                					 .xml file (local xml configuration avoids the overhead of DNS lookups with each
                                                					 call).

Step 16

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

If you are using a VXML gateway that is not co-located, then configure the following dial-peer to handle the error case:

Example:

```
dial-peer voice 9292 voip
description SIP error dial-peer
session protocol sipv2
session target ipv4:<destination IP_address for the VXML gateway>
session transport tcp
codec g711ulaw
destination-pattern 929292T
dtmf-relay rtp-nte
no vad
```

This may vary depending on the type of deployment.

### Ingress and VoiceXML Gateway Configuration Examples

The first part of the following example provides the basic configuration for setting an Ingress gateway:

Applies a timestamp to debugging and log messages

Turns on logging

Turns off printing to the command line interface console

Sends RTP packets

Configures gateway settings

The last part of this example provides the following:

Allows SIP to play a .wav file that enables caller to hear message from critical_error.wav

Performs survivability

Enables SIP to play ringtone to caller while caller is being transferred to an agent

Logs errors on the gateway when the call fails

Defines requirements for SIP Call Server

CVP solution does not support 100rel. It can be disabled on the dial-peer level or on a global level under the voice service
                                                      VoIP section.

```
service timestamps debug datetime msec localtime
service timestamps log datetime msec localtime
!
service internallogging buffered 99999999 debuggingn
no logging console
!
ip cef
!voice rtp send-recv
!
voice service voip
signaling forward unconditional 
sip 
min-se 360 
header-passing
!voice class codec 1
codec preference 1 g711ulaw codec preference 2 g729r8 !
application
service cvperror flash:cvperror.tcl
! 
service cvp-survivability flash:survivability.tcl
! 
service ringtone flash:ringtone.tcl
! 
service handoff flash:handoff.tcl
!gateway
timer receive-rtcp 4
!
ip rtcp report interval 2000
!sip-ua
retry invite 2
timers expires 60000
sip-server ipv4:<IP of CUSP server or Call Server>:5060
reason-header override
!
```

The first part of the following example provides the basic configuration for setting a VoiceXML gateway:

Applies a timestamp to debugging and log messages

Turns on logging

Turns off printing to the command line interface console

Sends RTP packets

Configures ASR/TTS Server

Configures gateway settings

The last part of this example provides the following:

Initiates the VoiceXML leg

Initiates the switch leg of the call

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
signaling forward unconditional
sip
min-se 360
header-passing
voice class
codec 1 codec preference 1 g711ulaw codec preference 2 g729r8 !
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
param cvpserverss1 1
!
```

The optional param cvpserverss1 1 line enables HTTPS.

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

For
                                                            						failover and load balancing of calls to multiple destinations, configure the
                                                            						CUSP server static route with priority and weight.

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

If a
                                                            						single CUSP Server is used, then SRV record usage is not required.

Configure the SRV records on the DNS server or locally on Unified CVP with a
                                                					 .xml file (local xml configuration avoids the overhead of DNS lookups with each
                                                					 call).

See
                                                            						the Local SRV File Configuration Example for SIP Messaging Redundancy section for details.

The
                                                					 Call Director call flow model with SIP calls will typically be deployed with
                                                					 dual CUSP servers for redundancy. In some cases, you might want to purchase a
                                                					 second CUSP server. Regardless, the default transport for deployment will be
                                                					 UDP; make sure you always disable the record-route in a CUSP server as this
                                                					 advanced feature is not supported in Contact Center deployments.

For the
                                                					 required settings in the Unified CM Publisher configuration, see the Cisco Unified SIP Proxy
                                                   						documentation .

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

## VoiceXML Gateway

The
                           		VoiceXML Gateway parses and renders VoiceXML documents obtained from the
                           		Unified CVP Call Server (from its IVR Service), the UnifiedCVP VXMLServers,
                           		or some other external VoiceXML source. Rendering a VoiceXML document consists
                           		of retrieving and playing prerecorded audio files, collecting and processing
                           		user input, or connecting to an ASR/TTS Server for voice recognition and
                           		dynamic text-to-speech conversion.

For a discussion
                           		of using mixed codecs in CVP deployments, see Mixed G.729 and G.711 Codec Support .
                           		For a discussion of the benefits and drawbacks of each codec, refer to Voice
                           		Traffic section of Solution Design Guide for Cisco Unified Contact Center
                              		  Enterprise .

VoiceXML Gateway must not have a load balanced path because this route on the VoiceXML Gateway will cause a call HTTP Client
                                       Error. If the VoiceXML Gateway has a load balancing route to the CVP Call Server, it may use a different source address to
                                       send HTTP message to the CVP Call Server. CVP would return a 500 Server Error address to send HTTP message to CVP Call Server,
                                       which would cause CVP to return a 500 Server Error message.

In VoiceXML Gateway, it is not possible to bind any specific interface for the HTTP Client side. If VoiceXML Gateway sends
                                       NEW_CALL using one interface and CALL_RESULT using another interface, CVP will return a 500 Server Error. Starting from IOS
                                       version 15.5.3M1, you have the capability to bind the VXML/HTTP traffic to a specific interface.

### Configuration

The
                              		high-availability configuration for VoiceXML Gateways is controlled by the SIP
                              		proxy for SIP, or the Unified CVP Call Server (Call Server). Whether the
                              		VoiceXML Gateways are distributed or centralized also influences how high
                              		availability is achieved.

If a Call
                              		Server is unable to connect to a VoiceXML Gateway, an error is returned to the
                              		ICM script. In the ICM script, the Send to VRU node is separate from the first
                              		Run External script node in order to catch the VoiceXML Gateway connection
                              		error. If an END script node is used off the X-path of the Send to VRU node,
                              		the call is default-routed by survivability on the originating gateway.
                              		(Survivability does not apply in VRU-only models.) A Queue to Skill group node
                              		is effective only if there is an agent available. Otherwise, ICM tries to queue
                              		the caller, and that attempt fails because the Call Server is once again unable
                              		to connect to a VoiceXML Gateway. An END node could then also be used off the
                              		X-path of the Queue to Skill Group node to default-route the call.

VXML Server uses
                                          		  two features that assist with load balancing:

Limiting load
                                                				balancer involvement

Enhanced HTTP
                                                				probes for load balancers

See the configuration options ip_redirect and license_depletion_probe_error in the User Guide for Cisco
                                       				  Unified CVP VXML Server and Cisco Unified Call Studio , available at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-customer-voice-portal/products-user-guide-list.html .

#### Centralized
                              	 VoiceXML Gateways

In this configuration, the VoiceXML Gateways reside in the
                                 		same data center as the Unified CVP Call Server.

#### SIP VoiceXML
                              	 Gateways

If you are
                                 		using SIP static routes on the Unified CVP Call Server, under the SIP Service
                                 		configuration for the Call Server, configure a static route for each Network
                                 		VRU label and gateway. If the VRU label is 5551000, the static route pattern
                                 		would be 5551000>. The > is a wildcard representing one or more digits,
                                 		and it is needed so that the correlation-id appended to the DNIS number can be
                                 		passed to the VoiceXML Gateway correctly.

Other wildcard
                                             		  characters can be used. See the topic Valid Formats
                                                			 for Dialed Numbers in the Ops Console online help for complete wildcard
                                             		  format and precedence information.

In the
                                 		case of both SIP proxy or Unified CVP static routes, the next-hop address of
                                 		the route can be either the IP address of the gateway or a DNS SRV record. If
                                 		you are using an IP address, you must create multiple static routes, one for
                                 		each VoiceXML Gateway. In the case of DNS SRV, only one route for each Network
                                 		VRU label is needed, and the SRV record provides for load balancing and
                                 		redundancy.

#### High-Availability
                              	 Hardware Configuration on Voice Gateways

The
                                 		individual hardware components have the following high-availability options:

Redundant power
                                       			 supplies

Separate
                                       			 components for higher availability

Dedicated
                                       			 components, which have fewer interaction issues

Example
                                    		  1: Separate PSTN Gateway and VoiceXML Gateway

A PSTN
                                 		Gateway and a separate VoiceXML Gateway provide greater availability for a
                                 		combined PSTN and VoiceXML Gateway.

Example
                                    		  2: Duplicate components for higher availability

Two 8-T1 PSTN
                                       			 Gateways provide greater availability than one 16-T1 PSTN Gateway.

Two 96-port
                                       			 UnifiedCVP VXMLServers provide greater availability than one 192-port
                                       			 UnifiedCVP VXMLServer.

Larger designs
                                       			 can use N+1 spares for higher availability.

Example
                                    		  3: Geographic redundancy for higher availability

Geographical redundancy and high availability can be achieved by
                                 		purchasing duplicate hardware for Side A and Side B.

### Distributed
                           	 VoiceXML Gateways

In this
                              		configuration, the gateway that processes the incoming call from the PSTN is
                              		separated from the Unified CVP servers by a low-bandwidth connection such as a
                              		WAN. The VoiceXML Gateway is different from the Ingress Gateway and can be
                              		located at the same site. The configuration keeps the media stream at the same
                              		site and without consuming bandwidth on the WAN and optimizes VoiceXML Gateway
                              		sizing when it is appropriate to separate Ingress and VoiceXML Gateways. In
                              		this case, setTransferLabel and Send to Originator cannot be used because you
                              		do not want the IVR leg of the call to go back to the Ingress Voice Gateway. It
                              		is also impractical to use a SIP Proxy to control the call routing because you
                              		would have to configure separate Network VRUs, Network VRU labels, and
                              		customers in ICM for each remote site. Instead, use SetSigDigits functionality.

With this
                              		method, the Call Server strips the leading significant digits from the incoming
                              		DNIS number. The value that is stripped is saved and prepended when subsequent
                              		transfers for the call occur.

#### SIP VoiceXML
                              	 Gateways

When SIP
                                 		is used, the significant digits are prepended to the DNIS number, and a SIP
                                 		Proxy can be configured to route calls based on those prepended digits. The
                                 		static routes in the SIP Proxy for the VoiceXML Gateway should have the digits
                                 		prepended. Because these prepended digits were originally populated by the
                                 		Ingress Gateway, the SIP Proxy can use them to determine which VoiceXML Gateway
                                 		to use based on the incoming gateway. In this way, calls arriving at a
                                 		particular site can always be sent back to VoiceXML treatment, with the result
                                 		that no WAN bandwidth is used to carry the voice RTP stream. The Unified CVP
                                 		indiscriminately prepends the sigdigits value to all transfers, including those to UnifiedCM. Therefore, when using
                                 		UnifiedCM in this scenario, it is necessary to strip the prepended digits when
                                 		the call arrives, so that the real DNIS number of the phone can be used by
                                 		UnifiedCM to route the call, as illustrated in the following example.

The configurations mentioned below are only applicable to IOS Voice
                                             		  Gateway.

Configuration of Ingress Voice Gateway :

Apply a
                                 		translation rule to the incoming DNIS to prepend the value 3333:

```
translation-rule 99 
       rule 1 8002324444 33338002324444

      dial-peer voice 1000 voip
       translate-outgoing called 99
```

Assuming
                                 		the DNIS number is 8002324444, the final DNIS string routed to Unified CVP is
                                 		33338002324444.

Configuration of Unified CVP SIP service :

To
                                 		configure the SIP service, in the Operations Console, select Call Server >
                                    		  SIP . Many of the settings are in the Advanced Configuration window.

Configuration of IOS VoiceXML
                                    		  Gateway :

Configure
                                 		the Voice XML Gateway to match the DNIS string, including the prepended digits:

```
dial-peer voice 3000 voip 
       incoming-called number 33335551000T
       service bootstrap
       ...
```

Configure
                                 		the Unified CVP bootstrap.tcl application with the sigdigits parameter, indicating how many digits to strip off of the incoming DNIS string:

```
application 
       service bootstrap flash:bootstrap.tcl
       param sigdigits 4
       ...
```

Cisco
                                    		  UnifiedCM configuration (if used) :

Configure
                                 		UnifiedCM to strip the prepended digits, either by using the Significant
                                 		Digits configuration on the SIP Trunk configuration page or by using
                                 		translation patterns.

SIP Proxy
                                    		  configuration :

Define
                                 		static routes on the SIP Proxy, with the prepended digit present, to be sent to
                                 		the appropriate VoiceXML Gateway. Because transfers to agents on a UnifiedCM
                                 		cluster have prepended digits, the static routes for agent phones must also
                                 		contain the prepended digits.

Summary
                                    		  of call routing :

A call arrives
                                       			 at Unified CVP with a DNIS number of 33338002324444.

Unified CVP
                                       			 removes four digits (3333) from the beginning of the DNIS string, leaving
                                       			 8002324444.

The number
                                       			 8002324444 is passed to ICM for call routing.

When it is time
                                       			 to transfer, ICM returns the label 5551000102. Unified CVP prepends 3333,
                                       			 resulting 33335551000102.

The SIP Service
                                       			 then resolves the address using the SIP Proxy or local static routes, and it
                                       			 sends the call to the VoiceXML Gateway.

The VoiceXML
                                       			 Gateway bootstrap.tcl removes 3333, leaving 5551000102 for the destination
                                       			 address.

### Cache
                           	 Types

There are
                              		two types of cache involved in storing media files: the IVR Media Player cache
                              		and the HTTP Client cache.

The HTTP Client
                              		cache is used for storing files that are downloaded from the HTTP server. In
                              		nonstreaming mode, the entire media file is stored inside the HTTP Client
                              		cache. In streaming mode, the first chunk of the media file is stored in the
                              		HTTP Client cache and in the IVR cache, and all subsequent chunks of the file
                              		are saved in the IVR cache only. The HTTP Client cache can store 100 MB of
                              		prompts, while the IVR cache is limited to 32 MB.

Use only
                              		nonstreaming mode, so that the IVR prompt cache is never used and the HTTP
                              		Client cache is the primary cache. In nonstreaming mode, the HTTP Client cache
                              		can also store 100MB of prompts, while the IVR cache is limited to 16MB.

To
                              		configure the HTTP Client cache, use the following Cisco IOS commands:

http client cache memory
                                 		  file 1-10000

The 1–10000 value is
                              		the file size in kilobytes. The default maximum file size is 50KB, but you can
                              		also have a file size up to 600 KB file size. Any file that is larger than the
                              		configured HTTP Client memory file size will not be cached.

http client cache memory
                                 		  pool 0-100000

The 0–100000 value
                              		is the total memory size available for all prompts, expressed in kilobytes. A
                              		value of zero disables HTTP caching. The default memory pool size for the HTTP
                              		Client cache is 10MB. The memory pool size is the total size of all prompts
                              		stored on the media server, which is up to 100MB.

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

| Step 1 | All Versions: Transfer
                                       			 the following script, configuration, and .wav files using the Operations
                                       			 Console or through the Unified CVP CD: CVPSelfService.tcl Note This
                                                            						file contains a gateway configuration example. CVPSelfServiceBootstrap.vxml critical_error.wav Select Bulk
                                                   						Administration > File Transfer > Scripts and
                                                   						Media . From the Select device type drop-down list, select Gateway . Select the
                                             				  required file from the Available list, and click the right arrow to move
                                             				  the device to the Selected list. Click Transfer . Note Ensure
                                                         					 to check the transfer status after you click Transfer , because sometimes transfer may fail. | Note | This
                                                            						file contains a gateway configuration example. | Note | Ensure
                                                         					 to check the transfer status after you click Transfer , because sometimes transfer may fail. |
|---|---|---|---|---|---|
| Note | This
                                                            						file contains a gateway configuration example. |
| Note | Ensure
                                                         					 to check the transfer status after you click Transfer , because sometimes transfer may fail. |
| Step 2 | All Versions: Perform
                                       			 Steps from the Configure VXML Server Standalone Call Flow Model procedure. |

| Note | This
                                                            						file contains a gateway configuration example. |
|---|---|

| Note | Ensure
                                                         					 to check the transfer status after you click Transfer , because sometimes transfer may fail. |
|---|---|

| Note | The optional param CVPSelfService-SSL
                                             1 line enables HTTPS. |
|---|---|

| Important | Calls
                                          may be rejected with a 403 Forbidden response if Toll
                                          Fraud security is not configured correctly. The solution is to add the IP
                                          address as a trusted endpoint, or else disable the IP address trusted list
                                          authentication altogether using the voice
                                             service voip -> "no ip address trusted
                                             authenticate" configuration entry. |
|---|---|

| Note | VXML Server (Standalone) supports an incoming call with
                                          a TDM through a T1 port only. Using an FXS port is not supported. |
|---|---|

| Note | 1800XXX is the number dialed which is added as a trigger in Cisco VVB for the self-service application. |
|---|---|

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
| Step 8 | Transfer files to the VXML Gateway using Step 2. |
| Step 9 | Configure the VXML Gateway base settings. |
| Step 10 | Configure the VXML Gateway service settings. |
| Step 11 | If using ASR and TTS Servers, specify IP addresses for those servers for each locale using the applicable name resolution
                                       system for the Gateway (DNS or "ip host" commands). Note If ASR and TTS use the same server, the MRCP server might allocate one license for the ASR session and a second license for
                                                      the TTS section. If you are hosting both ASR and TTS on the same speech server, you must select the ASR/TTS use the same MRCP server option in the IVR Service configuration tab in the Operations Console and follow the instructions in the step below. Do one of the following: The primary and backup servers must be configured. If using name resolution local to the Gateway (rather than DNS) specify: ip host asr- <locale> <ASR server for locale> ip host asr- <locale> -backup <backup ASR server for locale> ip host tts- <locale> <TTS server for locale> ip host tts- <locale> -backup <backup TTS server for locale> Example for English US, use: ip host asr-en-us 10.86.129.215 | Note | If ASR and TTS use the same server, the MRCP server might allocate one license for the ASR session and a second license for
                                                      the TTS section. If you are hosting both ASR and TTS on the same speech server, you must select the ASR/TTS use the same MRCP server option in the IVR Service configuration tab in the Operations Console and follow the instructions in the step below. |
| Note | If ASR and TTS use the same server, the MRCP server might allocate one license for the ASR session and a second license for
                                                      the TTS section. If you are hosting both ASR and TTS on the same speech server, you must select the ASR/TTS use the same MRCP server option in the IVR Service configuration tab in the Operations Console and follow the instructions in the step below. |
| Step 12 | If you want
                                       			 the ASR and TTS to use the same MRCP server option, you must configure the
                                       			 gateway as follows. In the
                                             				  IVR Service in the Operations Console, select the ASR/TTS
                                                					 use the same MRCP server option. Add the
                                             				  following two host names to the gateway configuration: ip
                                                      						  host asrtts- <locale> <IP Address Of MRCP Server> ip
                                                      						  host asrtts- <locale> -backup <IP Address Of MRCP
                                                         							 Server> Where the locale might be something like en-us or es-es,
                                                      						  resulting in asrtts-en-us or asrtts-es-es . Change
                                             				  the 'ivr asr-server' and 'ivr tts-server' lines as follows for MRCPV1: ivr
                                                      						  asr-server rtsp://asr-en-server/recognizer ivr
                                                      						  tts-server rtsp://tts-en-server/synthesizer Change
                                             				  the 'ivr asr-server' and 'ivr tts-server' lines as follows for MRCPV2: ivr asr-server sip:asr@10.78.26.103 ivr tts-server sip:tts@10.78.26.103 |
| Step 13 | Configure
                                       			 the speech servers to work with Unified CVP. Caution The
                                                      				  Operations Console can only manage speech servers installed on Windows , not on Linux. If the speech server is installed on
                                                      				  Linux, the server cannot be managed. To ensure
                                          				that the speech servers work with Unified CVP, you must make the following
                                          				changes on each speech server as part of configuring the Unified CVP solution. If you are
                                          				using Nuance SpeechWorks MediaServer (SWMS), the configuration file is
                                          				osserver.cfg. If you are using Nuance Speech Server (NSS), the configuration
                                          				file is NSSserver.cfg. Make the
                                          				following changes to the Nuance configuration file: Change: server.resource.2.url VXIString media/speechrecognizer To: server.resource.2.url VXIString recognizer Change: server.resource.4.url VXIString media/speechsynthesizer To: server.resource.4.url VXIString synthesizer Change: server.mrcp1.resource.3.url VXIString media/speechrecognizer To: server.mrcp1.resource.3.url VXIString /recognizer Change: server.mrcp1.resource.2.url VXIString media/speechsynthesizer To: server.mrcp1.resource.2.url VXIString media/synthesizer Change: server.mrcp1.transport.port VXIInteger 4900 To: server.mrcp1.transport.port VXIInteger 554 If you are using Nuance Speech Server 5 and Nuance Vocalizer for Network 5, then make changes to the configuration files
                                          for each application. Make the following changes to the Nuance Speech Server 5 configuration file (NSSserver.cfg): Change: server.mrcp1.resource.3.url VXIString media/speechrecognizer To: server.mrcp1.resource.3.url VXIString /recognizer Change: server.mrcp1.resource.2.url VXIString media/speechsynthesizer To: server.mrcp1.resource.2.url VXIString /synthesizer Change: server.mrcp1.transport.port VXIInteger 4900 To: server.mrcp1.transport.port VXIInteger 554 Change: server.mrcp1.transport.dtmfPayloadType VXIInteger 96 To: server.mrcp1.transport.dtmfPayloadType VXIInteger 101 Uncomment the
                                                   						following: server.rtp.dtmfTriggerLeading VXIInteger 0 If you
                                                					 are using the Nuance Vocalizer for Network 5 TTS System, the following
                                                					 configuration files will need to be updated: <install path>\Nuance Vocalizer for Network 5.0\config\ttsrshclient.xml Change: <ssml_validation>strict</ssml_validation> To: <ssml_validation>warn</ssml_validation> <install path>\Nuance Vocalizer for Network 5.0\config\ttssapi.xml Change: <ssml_validation>strict</ssml_validation> To: <ssml_validation>warn</ssml_validation> If you are using Nuance Recognizer 10.0 and Nuance Speech Server 6.2, make the following changes to the Nuance configuration
                                          file (NSSserver.cfg - C:\Program Files (x86)\Nuance\Speech Server\Server\config): Change: server.mrcp1.resource.3.url VXIString
                                                					 media/speechrecognizer To: server.mrcp1.resource.3.url VXIString /recognizer Change: server.mrcp1.resource.2.url VXIString media/speechsynthesizer To: server.mrcp1.resource.2.url VXIString /synthesizer Change : server.mrcp1.transport.port VXIInteger 4900 To: server.mrcp1.transport.port VXIInteger 554 Change: server.mrcp1.transport.dtmfPayloadType VXIInteger 96 To: server.mrcp1.transport.dtmfPayloadType VXIInteger Make the
                                          				following change to the Baseline.xml file C:\Program Files\Nuance\Recognizer\config Change: <ssml_validation>strict</ssml_validation> To: <ssml_validation>warn</ssml_validation>. If you are using Nuance Recognizer 10.5 and Nuance Speech Server 6.5, then refer to the relevant Nuance Speech Suite Install
                                          Guide available at https://network.nuance.com/portal/server.pt/directory/nuance_speech_suite_10_5/16535 . If you are using Nuance Recognizer 11.0 and Nuance Speech Server 7.0, then refer to the relevant Nuance Speech Suite Install
                                          Guide available at https://network.nuance.com/portal/server.pt/directory/nuance_speech_suite_11_0 . | Caution | The
                                                      				  Operations Console can only manage speech servers installed on Windows , not on Linux. If the speech server is installed on
                                                      				  Linux, the server cannot be managed. |
| Caution | The
                                                      				  Operations Console can only manage speech servers installed on Windows , not on Linux. If the speech server is installed on
                                                      				  Linux, the server cannot be managed. |
| Step 14 | Configure
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
                                                      						  the Cluster fully qualified domain name: FQDN . For
                                          				detailed instructions about using Unified CM and the CUSP Server, see the Cisco Unified SIP Proxy Server
                                             				  documentation . | Note | CVP
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
| Step 15 | (Optional) Configure
                                       			 the SIP Proxy
                                          				Server . From the
                                          				CUSP Server Administration web page ( http://<CUSP server>/admin ): Configure the SIP static routes to the Unified CVP Call Server(s), Unified CM SIP
                                             				  trunks, and Gateways. Configure the SIP static routes for intermediary transfers for ring tone, playback dialed numbers, and error playback dialed
                                                numbers. Note For failover and load balancing of calls to multiple destinations, configure the CUSP Server static route with priority and
                                                            weight. See the SIP Devices Configuration and SIP Dialed Number Pattern Matching Algorithm for detailed information. Configure Access Control Lists for Unified CVP calls. Select Proxy
                                                            								Settings > Incoming ACL . Set
                                                      						  address pattern: all Configure the service parameters. Select Service Parameters , and set the following: Add
                                                      						  record route: off Maximum invite retransmission count: 2 Proxy Domain and Cluster Name: if using DNS SRV, set to the FQDN of your Proxy
                                                      						  Server SRV name. Write
                                             				  down the IP address and host name of the SIP Proxy Server. You need this
                                             				  information when configuring the SIP Proxy Server in Unified CVP. If
                                             				  using redundant SIP Proxy Servers (primary and secondary or load balancing),
                                             				  decide whether to use DNS server lookups for SRV records or non-DNS based local
                                             				  SRV record configuration. The
                                                					 Comprehensive call flow model with SIP calls will typically be deployed with
                                                					 dual CUSP Servers for redundancy. In some cases, you might want to purchase a
                                                					 second CUSP Server. Regardless, the default transport for deployment will be
                                                					 UDP. Make sure you always set the AddRecordRoute setting to Off with CUSP Servers. Configure the SRV records on the DNS server or locally on Unified CVP with an
                                                					 .xml file (local xml configuration avoids the overhead of DNS lookups with each
                                                					 call). | Note | For failover and load balancing of calls to multiple destinations, configure the CUSP Server static route with priority and
                                                            weight. |
| Note | For failover and load balancing of calls to multiple destinations, configure the CUSP Server static route with priority and
                                                            weight. |
| Step 16 | Configure
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
                                                					 are in a Unified ICMH environment and configuring the CICM, then do the following: Do not select the Network Transfer Preferred checkbox Routing client: INCRP NIC Note If you are using a VXML gateway that is not co-located, then configure the following dial-peer to handle the error case: Example: dial-peer voice 9292 voip
description SIP error dial-peer
session protocol sipv2
session target ipv4:<destination IP_address for the VXML gateway>
session transport tcp
codec g711ulaw
destination-pattern 929292T
dtmf-relay rtp-nte
no vad This may vary depending on the type of deployment. | Note | If you are using a VXML gateway that is not co-located, then configure the following dial-peer to handle the error case: Example: dial-peer voice 9292 voip
description SIP error dial-peer
session protocol sipv2
session target ipv4:<destination IP_address for the VXML gateway>
session transport tcp
codec g711ulaw
destination-pattern 929292T
dtmf-relay rtp-nte
no vad This may vary depending on the type of deployment. |
| Note | If you are using a VXML gateway that is not co-located, then configure the following dial-peer to handle the error case: Example: dial-peer voice 9292 voip
description SIP error dial-peer
session protocol sipv2
session target ipv4:<destination IP_address for the VXML gateway>
session transport tcp
codec g711ulaw
destination-pattern 929292T
dtmf-relay rtp-nte
no vad This may vary depending on the type of deployment. |

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

| Note | If ASR and TTS use the same server, the MRCP server might allocate one license for the ASR session and a second license for
                                                      the TTS section. If you are hosting both ASR and TTS on the same speech server, you must select the ASR/TTS use the same MRCP server option in the IVR Service configuration tab in the Operations Console and follow the instructions in the step below. |
|---|---|

| Caution | The
                                                      				  Operations Console can only manage speech servers installed on Windows , not on Linux. If the speech server is installed on
                                                      				  Linux, the server cannot be managed. |
|---|---|

| Note | CVP
                                                            						solution does not support 100rel. On the SIP profile for the Trunk, confirm
                                                            						that SIP Rel1xx Options are disabled. For
                                                            						warm transfers, the call from Agent 1 to Agent 2 does not typically use a SIP
                                                            						Trunk, but you must configure the CTI Route Point for that dialed number on the Unified CM Server and associate that number with your peripheral gateway user (PGUSER) for
                                                            						the JTAPI gateway on the Unified CM peripheral gateway. An alternative is to use the Dialed Number Plan on Unified ICME to
                                                            						bypass the CTI Route Point. |
|---|---|

| Note | For failover and load balancing of calls to multiple destinations, configure the CUSP Server static route with priority and
                                                            weight. |
|---|---|

| Note | If you are using a VXML gateway that is not co-located, then configure the following dial-peer to handle the error case: Example: dial-peer voice 9292 voip
description SIP error dial-peer
session protocol sipv2
session target ipv4:<destination IP_address for the VXML gateway>
session transport tcp
codec g711ulaw
destination-pattern 929292T
dtmf-relay rtp-nte
no vad This may vary depending on the type of deployment. |
|---|---|

| Note | CVP solution does not support 100rel. It can be disabled on the dial-peer level or on a global level under the voice service
                                                      VoIP section. |
|---|---|

| Note | The optional param cvpserverss1 1 line enables HTTPS. |
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
                                                					 playback dialed numbers, and error playback dialed numbers. Note For
                                                            						failover and load balancing of calls to multiple destinations, configure the
                                                            						CUSP server static route with priority and weight. Configure Access Control Lists for Unified CVP calls. Select Proxy
                                                      						  Settings > Incoming ACL . Address
                                                					 pattern: all Configure the service parameters. Select Service Parameters , then set the following: Add
                                                      						  record route: off Maximum invite retransmission count: 2 Proxy Domain and Cluster Name: if using DNS SRV, set to the FQDN of your Proxy
                                                      						  Server SRV name Write
                                             				  down the IP address and host name of the SIP Proxy Server. (You need this
                                             				  information when configuring the SIP Proxy Server in Unified CVP.) If
                                             				  using redundant SIP Proxy Servers (primary and secondary or load balancing),
                                             				  then decide whether to use DNS server lookups for SRV records or non-DNS based
                                             				  local SRV record configuration. Note If a
                                                            						single CUSP Server is used, then SRV record usage is not required. Configure the SRV records on the DNS server or locally on Unified CVP with a
                                                					 .xml file (local xml configuration avoids the overhead of DNS lookups with each
                                                					 call). Note See
                                                            						the Local SRV File Configuration Example for SIP Messaging Redundancy section for details. The
                                                					 Call Director call flow model with SIP calls will typically be deployed with
                                                					 dual CUSP servers for redundancy. In some cases, you might want to purchase a
                                                					 second CUSP server. Regardless, the default transport for deployment will be
                                                					 UDP; make sure you always disable the record-route in a CUSP server as this
                                                					 advanced feature is not supported in Contact Center deployments. For the
                                                					 required settings in the Unified CM Publisher configuration, see the Cisco Unified SIP Proxy
                                                   						documentation . | Note | For
                                                            						failover and load balancing of calls to multiple destinations, configure the
                                                            						CUSP server static route with priority and weight. | Note | If a
                                                            						single CUSP Server is used, then SRV record usage is not required. | Note | See
                                                            						the Local SRV File Configuration Example for SIP Messaging Redundancy section for details. |
| Note | For
                                                            						failover and load balancing of calls to multiple destinations, configure the
                                                            						CUSP server static route with priority and weight. |
| Note | If a
                                                            						single CUSP Server is used, then SRV record usage is not required. |
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

| Note | For
                                                            						failover and load balancing of calls to multiple destinations, configure the
                                                            						CUSP server static route with priority and weight. |
|---|---|

| Note | If a
                                                            						single CUSP Server is used, then SRV record usage is not required. |
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

| Note | VoiceXML Gateway must not have a load balanced path because this route on the VoiceXML Gateway will cause a call HTTP Client
                                       Error. If the VoiceXML Gateway has a load balancing route to the CVP Call Server, it may use a different source address to
                                       send HTTP message to the CVP Call Server. CVP would return a 500 Server Error address to send HTTP message to CVP Call Server,
                                       which would cause CVP to return a 500 Server Error message. In VoiceXML Gateway, it is not possible to bind any specific interface for the HTTP Client side. If VoiceXML Gateway sends
                                       NEW_CALL using one interface and CALL_RESULT using another interface, CVP will return a 500 Server Error. Starting from IOS
                                       version 15.5.3M1, you have the capability to bind the VXML/HTTP traffic to a specific interface. |
|---|---|

| Note | VXML Server uses
                                          		  two features that assist with load balancing: Limiting load
                                                				balancer involvement Enhanced HTTP
                                                				probes for load balancers |
|---|---|

| Note | Other wildcard
                                             		  characters can be used. See the topic Valid Formats
                                                			 for Dialed Numbers in the Ops Console online help for complete wildcard
                                             		  format and precedence information. |
|---|---|

| Note | The configurations mentioned below are only applicable to IOS Voice
                                             		  Gateway. |
|---|---|