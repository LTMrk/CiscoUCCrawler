---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-voi-cub-sip-dyn-refer-handling-html-f6634c8b89
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_voi-cub-sip-dyn-refer-handling.html
retrieved_at: 2026-08-16T15:48:43.776031+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Dynamic REFER Handling

## Chapter: Dynamic REFER Handling

# Dynamic REFER Handling

## Dynamic Refer
                        	 Handling

When a dial-peer match occurs, Cisco Unified Border Element (CUBE) passes the REFER message from an in leg to an out leg. Also, the host part of the Refer-to header is modified with the IP
                           address.

The Dynamic REFER handling feature provides configurations to pass across or consume the REFER message. When an endpoint invokes
                           a supplementary service such as a call transfer, the endpoint generates and sends an in-dialog REFER request towards the CUBE . If the REFER message is consumed, an INVITE is sent towards refer-to dial-peer

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature
                                          				  Information

REFER Consume
                                          				  (Enhancements)

Baseline Fuctionality

Refer Delay Disconnect

Cisco IOS XE Bengaluru 17.6.1a

Delay disconnect message on transferor leg for REFER transaction.

## Prerequisites

Transcoding configuration is required on the CUBE for midcall transcoder insertion, deletion, or modification during call transfers.

## Restrictions

Only Session
                                    				Initiation Protocol (SIP)-to-SIP call transfers are supported.

Call escalation
                                    				and de-escalation are not supported.

Video
                                    				transcoding is not supported.

Session
                                    				Description Protocol (SDP) pass-through is not supported.

In REFER consume
                                    				scenario, if TCL script is enabled, then supplementary-service
                                          					 media-renegotiate command should not be configured.

## Configure REFER Passthrough with Unmodified Refer-To

This task configures the passthrough of REFER message from the in leg to the out leg on a dial-peer match. A REFER is sent
                              toward inbound dial peer. This task also ensures that the host part of the Refer-to header is unmodified and not changed to
                              the IP address during passthrough.

Dataplane session will not be deleted for REFER passthrough scenarios, after receiving REFER message. For Cisco IOS XE Bengaluru 17.6.1a and later, configure refer-delay-disconnect <secs> , to override this functionality.

supplementary service refer

Results

yes

REFER is passed through from the in leg to the out leg.

no

INVITE is sent toward refer-to dial-peer.

This configuration in this task can be overridden by the refer consume command. Refer to the Configuring REFER Consumption task for more information.

### SUMMARY STEPS

- enable

- configure terminal

- Configure REFER
                              			 passthrough:

- supplementary-service sip refer in global VoIP
                                 				configuration mode.

- supplementary-service sip refer in dial-peer
                                 				configuration mode.

- (Optional) Configure
                              			 unmodified Refer-to:

- referto-passing in Global VoIP SIP configuration mode.

- voice-class sip referto-passing [ system ] in dial-peer configuration mode.

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables
                                          				privileged EXEC mode.

Enter your
                                                					 password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

Configure REFER
                                       			 passthrough:

- supplementary-service sip refer in global VoIP
                                          				configuration mode.

- supplementary-service sip refer in dial-peer
                                          				configuration mode.

### Example:

```
Device(config)# voice service voip 
Device(conf-voi-serv)# supplementary-service sip refer
```

### Example:

```
Device(config)# dial-peer voice 22 voip
Device(config-dial-peer)# supplementary-service sip refer
```

Step 4

(Optional) Configure
                                       			 unmodified Refer-to:

- referto-passing in Global VoIP SIP configuration mode.

- voice-class sip referto-passing [ system ] in dial-peer configuration mode.

### Example:

```
Device(config)# voice service voip 
Device(conf-voi-serv)# sip
Device(conf-serv-sip)# referto-passing
```

### Example:

```
Device(config)# dial-peer voice 22 voip
Device(config-dial-peer)# voice-class sip referto-passing
```

Step 5

end

Exits to
                                          				privileged EXEC mode.

## REFER Handling - Delayed Disconnect

With the current default behaviour of CUBE REFER handling, CUBE disconnects the call on a transferor leg with BYE message, after REFER transaction is successful. Also, CUBE unbridges the media path between transferee and transferor during REFER pass through scenario. This causes the interoperability
                              issues with other third party vendor products wherein the Call Transfer is unsuccessful. To fix this interoperability issues, refer-delay-discconnect command is configured.

### SUMMARY STEPS

- enable

- configure terminal

- Configure refer-delay-disconnect:

- refer-delay-disconnect <1-5> delay value (in seconds) in global VoIP, dial-peer, and tenant configuration modes.

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables privileged EXEC mode.

Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

Configure refer-delay-disconnect:

- refer-delay-disconnect <1-5> delay value (in seconds) in global VoIP, dial-peer, and tenant configuration modes.

### Example:

```
Device(config)# voice service voip 
Device(conf-voi-serv)#sip 
Device(conf-serv-sip)#refer-delay-disconnect 3
```

### Example:

```
Device(config)# dial-peer voice 22 voip
Device(config-dial-peer)# voice-class sip refer-delay-disconnect 3
```

### Example:

```
Device(config)# voice class tenant 10
Device(config-class)# refer-delay-disconnect 3
```

## Configure REFER Consumption

This task configures
                              		  the consumption of REFER message on a dial-peer match. An INVITE is sent
                              		  towards the Refer-to dial peer.

supplementary service refer

refer consume

Results

yes

no

REFER is
                                          					 sent towards inbound dial-peer

yes

yes

INVITE is
                                          					 sent towards refer-to dial-peer

no

no

INVITE is
                                          					 sent towards refer-to dial-peer

no

yes

INVITE is
                                          					 sent towards refer-to dial-peer

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of the
                              			 following:

- no supplementary-service sip refer in global VoIP
                                 				configuration mode.

- no supplementary-service sip refer in dial-peer
                                 				configuration mode.

- refer consume in global VoIP
                              			 configuration mode.

- (Optional) supplementary-service
                                    				  media-renegotiate in global VoIP configuration mode.

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables
                                          				privileged EXEC mode.

Enter your
                                                					 password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

Enter one of the
                                       			 following:

- no supplementary-service sip refer in global VoIP
                                          				configuration mode.

- no supplementary-service sip refer in dial-peer
                                          				configuration mode.

### Example:

```
Device(config)# voice service voip 
Device(conf-voi-serv)# no supplementary-service sip refer
```

### Example:

```
Device(config)# dial-peer voice 22 voip
Device(config-dial-peer)# no supplementary-service sip refer
```

Step 4

refer consume in global VoIP
                                       			 configuration mode.

### Example:

```
Device(config)# dial-peer voice 22 voip
Device(config-dial-peer)# refer consume
```

Step 5

(Optional) supplementary-service
                                             				  media-renegotiate in global VoIP configuration mode.

### Example:

```
Device(config)# voice service voip 
Device(conf-voi-serv)# supplementary-service media-renegotiate
```

Step 6

end

Exits to
                                          				privileged EXEC mode.

## Troubleshooting Tips

Use any of the
                           		following debug commands:

debug ccsip all

debug voip ccapi inout

debug sccp messages

debug voip application supplementary-service

debug voip application state

debug voip application media negotiation

| Feature Name | Releases | Feature
                                          				  Information |
|---|---|---|
| REFER Consume
                                          				  (Enhancements) | Baseline Fuctionality | REFER Consume (Enhancements) provides additional configurations to conditionally forward the REFER message. |
| Refer Delay Disconnect | Cisco IOS XE Bengaluru 17.6.1a | Delay disconnect message on transferor leg for REFER transaction. |

| Note | Dataplane session will not be deleted for REFER passthrough scenarios, after receiving REFER message. For Cisco IOS XE Bengaluru 17.6.1a and later, configure refer-delay-disconnect <secs> , to override this functionality. |
|---|---|

| supplementary service refer | Results |
|---|---|
| yes | REFER is passed through from the in leg to the out leg. |
| no | INVITE is sent toward refer-to dial-peer. |

| Note | This configuration in this task can be overridden by the refer consume command. Refer to the Configuring REFER Consumption task for more information. |
|---|---|

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter your
                                                					 password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | Configure REFER
                                       			 passthrough: supplementary-service sip refer in global VoIP
                                          				configuration mode. supplementary-service sip refer in dial-peer
                                          				configuration mode. Example: In Global
                                       			 VoIP configuration mode: Device(config)# voice service voip 
Device(conf-voi-serv)# supplementary-service sip refer Example: In dial-peer
                                       			 configuration mode: Device(config)# dial-peer voice 22 voip
Device(config-dial-peer)# supplementary-service sip refer | Configures REFER passthrough. A REFER is sent toward the inbound dial peer. |
| Step 4 | (Optional) Configure
                                       			 unmodified Refer-to: referto-passing in Global VoIP SIP configuration mode. voice-class sip referto-passing [ system ] in dial-peer configuration mode. Example: In Global
                                       			 VoIP configuration mode: Device(config)# voice service voip 
Device(conf-voi-serv)# sip
Device(conf-serv-sip)# referto-passing Example: In
                                       			 dial-peer configuration mode: Device(config)# dial-peer voice 22 voip
Device(config-dial-peer)# voice-class sip referto-passing | (Optional) Ensures that the refer-to header is unmodified and not changed to the IP address during passthrough. |
| Step 5 | end | Exits to
                                          				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | Configure refer-delay-disconnect: refer-delay-disconnect <1-5> delay value (in seconds) in global VoIP, dial-peer, and tenant configuration modes. Example: In Global VoIP configuration mode: Device(config)# voice service voip 
Device(conf-voi-serv)#sip 
Device(conf-serv-sip)#refer-delay-disconnect 3 Example: In dial-peer configuration mode: Device(config)# dial-peer voice 22 voip
Device(config-dial-peer)# voice-class sip refer-delay-disconnect 3 Example: In tenant configuration mode: Device(config)# voice class tenant 10
Device(config-class)# refer-delay-disconnect 3 | Configures refer-delay-disconnect. Now, CUBE delays the disconnect message (sending BYE) on the transferor leg for the configured timeout. |

| supplementary service refer | refer consume | Results |
|---|---|---|
| yes | no | REFER is
                                          					 sent towards inbound dial-peer |
| yes | yes | INVITE is
                                          					 sent towards refer-to dial-peer |
| no | no | INVITE is
                                          					 sent towards refer-to dial-peer |
| no | yes | INVITE is
                                          					 sent towards refer-to dial-peer |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter your
                                                					 password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | Enter one of the
                                       			 following: no supplementary-service sip refer in global VoIP
                                          				configuration mode. no supplementary-service sip refer in dial-peer
                                          				configuration mode. Example: In global
                                       			 VoIP configuration mode: Device(config)# voice service voip 
Device(conf-voi-serv)# no supplementary-service sip refer Example: In dial-peer
                                       			 configuration mode: Device(config)# dial-peer voice 22 voip
Device(config-dial-peer)# no supplementary-service sip refer | Configures REFER consumption. An INVITE is sent towards the
                                       			 Refer-to dial peer. |
| Step 4 | refer consume in global VoIP
                                       			 configuration mode. Example: In
                                       			 dial-peer configuration mode: Device(config)# dial-peer voice 22 voip
Device(config-dial-peer)# refer consume | Configures REFER consumption. |
| Step 5 | (Optional) supplementary-service
                                             				  media-renegotiate in global VoIP configuration mode. Example: In global
                                       			 VoIP configuration mode: Device(config)# voice service voip 
Device(conf-voi-serv)# supplementary-service media-renegotiate | (Optional) Enables
                                       			 end-to-end media renegotiation during the call transfer in REFER consumption
                                       			 mode. |
| Step 6 | end | Exits to
                                          				privileged EXEC mode. |