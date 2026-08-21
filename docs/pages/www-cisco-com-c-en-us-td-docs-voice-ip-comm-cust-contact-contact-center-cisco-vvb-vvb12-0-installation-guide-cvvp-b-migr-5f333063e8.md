---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-cisco-vvb-vvb12-0-installation-guide-cvvp-b-migr-5f333063e8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/cisco_vvb/vvb12_0/installation/guide/cvvp_b_migration-guide-1201/cvvp_b_migration-guide-1201_chapter_0101.html
retrieved_at: 2026-08-21T16:28:55.460066+00:00
---

Migration Guide for Cisco Virtualized Voice Browser, Release 12.0(1)

# Migration Guide for Cisco Virtualized Voice Browser, Release 12.0(1)

Updated: January 11, 2019

Chapter: Migration Process

## Chapter: Migration Process

# Migration Process

## Migration
                        	 Process

To migrate from a Cisco-IOS-VB to Cisco-VB, the first step is installation and configuration of Cisco-VVB followed by adding
                           the Cisco-VVB to the CVP deployment. This will require some configuration on CVP OAMP and Egress routing routes.

### Service and
                           	 Dial-Peer Configuration

For
                                    			 comprehensive, standalone and ringtone service, create equivalent application
                                    			 in Cisco-VVB.

For each
                                    			 corresponding dial-peer on Cisco-IOS-VB, add corresponding trigger on the
                                    			 Cisco-VVB.

For SigDigit is
                                    			 defined at dial-peer level in Cisco-IOS-VB, configure SigDigit at corresponding
                                    			 application of the trigger, for example:

```
dial-peer voice 60001 voip
 description CVP VRU LABEL, SIGDIGITS 555XXX
 preference 1
 service bootstrap
 incoming called-number 555.....1111119999T
 voice-class sip rel1xx disable
 dtmf-relay rtp-nte
 codec g711ulaw
 param sigdigits 4
 no vad
```

Service and
                              		Dial-Peer

### Comprehensive
                           	 Service or Application

In a comprehensive
                              		call model administrator needs to add application and set various parameters.

For example:

```
service comprehensive flash:bootstrap.tcl
  paramspace english index 0
  paramspace english language en
  paramspace english location flash
  paramspace english prefix en
  param sigdigits 4
```

Comprehensive
                              		Service

### Standalone Service
                           	 or Application

In a standalone call
                              		model, the administrator has to add application and set various parameters like
                              		VXML application name, primary/secondary server, port and other related.

For example:

```
service standalone flash:CVPSelfService.tcl
  paramspace english language en
  paramspace english index 0
  param CVPPrimaryVXMLServer 10.78.26.38
  paramspace english location flash:
  param CVPSelfService-port 7000
  param CVPSelfService-app AgeIdentification
```

Service standalone

### Ringtone Service
                           	 or Application

For ringtone
                              		service, add application and set various parameters, VXML application name,
                              		primary/secondary server, and port.

For example:

```
service ringtone flash:ringtone.tcl
  paramspace english index 0
  paramspace english language en
  paramspace english location flash
  paramspace english prefix en
```

Ringtone

### MRCP
                           	 Configuration

If ASR and TTS
                                    			 are configured in Cisco-IOS-VB, then add these in the Cisco-VVB for the
                                    			 following scenarios:-

Multiple
                                          				  servers are configured for ASR or TTS, for load balancing, using dial-peer. In
                                          				  this case multiple servers can be configured on Cisco VVB. These will be used
                                          				  in round robin configuration. You cannot set a maximum session limit on
                                          				  CiscoVVB for the configured servers .

IOS-VB has
                                          				  single server and a corresponding backup server configured. You can add
                                          				  multiple servers and these can be used in round-robin basis.

For Cisco VVB
                                    			 the client timeout timers are not configurable. Cisco VVB uses optimized values
                                    			 for the client timeout for connect, disconnect etc.

For Microapps, when the url (rtsp://tts-en-us:4900/synthesizer or rtsp://asr-en-us:4900/recognizer), is processed by Cisco
                                    VVB, only hostname or IP-address in the url is used by Cisco VVB. Hostname is matched to locally configured server and corresponding
                                    port name is used to setup the connection. Depending on MRCP v1 or v2 configured on the system, session is setup to the server.
                                    So practically, you can use MRCP v2 also to for Microapps.

### Call
                           	 Throttling

Cisco VVB throttles
                              		the call to prevent overload.

For maximum calls supported, see VVB virtualization https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/uc_system/virtualization/virtualization-cisco-virtualized-voice-browser.html .

Each OVAs defines the maximum number of calls supported. The maximum
                              		concurrent calls count is aggregated call count of various types of calls in
                              		the system (IVR, ringtone, whisper etc.).

In a deployed VVB,
                              		if the concurrent calls reaches maximum supported calls, any new call requests
                              		received beyond this number will be rejected. Each OVA defines maximum calls
                              		per second (cps) that a specific OVA supports. Any higher call rate beyond this
                              		number will trigger overload (see Solution Design Guide for Cisco Unified
                              		Contact Center Enterprise for details). When migrating Cisco-IOS-VB to Cisco
                              		VVB, this factor should be considered in sizing.

### SIP RAI

If SIP RAI is configured in the Cisco-IOS-VB to send the RAI report to the remote server every interval, then the RAI needs
                                    to be configured for the remote server on Cisco VVB.

If the Remote
                                    			 server is using SIP OPTIONS method to get out the RAI data, then no additional
                                    			 configuration is required in the Cisco VVB. Cisco VVB will report system, cpu,
                                    			 memory, DS0 and DSPs like Cisco-IOS-VB. But given that Cisco VVB does not have
                                    			 DS0, the number of available ports will be reported on this.

DSP data can be ignored.

```
X-cisco-rai : SYSTEM; almost-out-of-resource=false
X-cisco-rai : CPU; almost-out-of-resource=false;total=100%;available=77
X-cisco-rai : MEM; almost-out-of-resource=false;total=100%;available=71
X-cisco-rai : DSO; almost-out-of-resource=false;total=600;available=148
X-cisco-rai : DSP; almost-out-of-resource=false
```

### Adding Cisco-VVB
                           	 to Deployment

Cisco VVB can be added to the deployment using any one of these methods:

Comprehensive
                                    			 deployment model

After Cisco
                                          				  VVB is configured (through Cisco VVB AppAdmin or CVP-OAMP bulk configuration),
                                          				  add the newly configured Cisco VVB to the CVP ‘Dialed Number Pattern’ or ‘SIP
                                          				  Server Group’.

CVP will
                                          				  initiate SIP Heartbeat with the Cisco VVB and if SIP RAI is configured

Standalone
                                    			 deployment model

After the Cisco VVB
                              		is configured (through Cisco VVB AppAdmin or CVP-OAMP bulk configuration), add
                              		the dial-peer in the Ingress-gateway (Cube or PSTN-GW) to point to the Cisco
                              		VVB.

| Note | SigDigit is
                                       		defined as parameter at the service level in Cisco-IOS-VB. |
|---|---|

| Note | Cisco VVB does not use the concept of backup server. |
|---|---|