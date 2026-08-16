---
doc_id: www-cisco-com-c-en-us-td-docs-ios-xml-ios-voice-cube-ios-xe-config-ios-xe-book-m-media-path-html-8b6945150f
source_url: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/voice/cube/ios-xe/config/ios-xe-book/m_media-path.html
retrieved_at: 2026-08-16T15:45:08.859917+00:00
---

Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

# Cisco Unified Border Element Configuration Guide - Cisco IOS XE 17.6 Onwards

Updated: April 25, 2026

Chapter: Media Path

## Chapter: Media Path

# Media Path

## Overview

The Media Path settings determine the path taken by media after a call is established by CUBE .

H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications.

You can configure the media path in the following modes:

- Media flow-through: where media and signaling packets terminate and originate on CUBE . As CUBE is an active participant of the call, this mode is recommended when connected outside an enterprise (untrusted endpoints). Figure 1. Media Flow-Through Mode

Media flow-around: where signaling packets terminate and originate on CUBE , but media flows directly between endpoints. As media bypasses CUBE , this mode is recommended when connected within an enterprise (trusted endpoints).

Media antitrombone: where CUBE is allowed to detect and avoid loops that are created by call transfers or call forwards. Loops are restricted to the SIP
                                 signaling path and removed from the RTP media path.

The user agent may initiate call forwards and call transfers that are sent towards CUBE as a new SIP INVITE dialog. CUBE considers the original call and the forwarded call as separate unrelated calls. Media antitromboning allows CUBE to detect the relation between the calls and resolve the media loop by sending SDP packets back to the sender.

The figure below illustrates how media is needlessly looped over the WAN when loops are not detected.

The figure below illustrates how CUBE detects and avoids the loop with the antitromboning feature.

SDP Pass–Through: CUBE is configured to pass SDP information transparently, so that both the remote ends can negotiate media independently. SDP
                                 pass-through is addressed in two modes:

Flow-through— CUBE plays no role in media negotiation, it terminates and reoriginates the RTP packets irrespective of the content type that
                                       is negotiated by both the ends. This supports address hiding and NAT traversal.

Flow-around— CUBE neither plays a part in media negotiation, nor does it terminate and reoriginate media. Media negotiation and media exchange
                                       is end-to-end.

For more information, refer to the “Configurable Pass-through of SIP INVITE Parameters” section in the Cisco Unified Border Element SIP Support Configuration Guide .

Restrictions for Media Anti-Tromboning

Anti-Tromboning is possible for secure (SRTP) calls only when SDP passthrough is enabled.

Anti-Tromboning is not possible if one call leg is media flow-through and the other call leg is Media Flow-Around. Similarly,
                                 antitromboning is not possible if one call leg is configured for  Session Description Protocol (SDP) passthrough.

### Feature Information

The following table provides release information about the feature or features described in this module. This table lists
                                 only the software release that introduced support for a given feature in a given software release train. Unless noted otherwise,
                                 subsequent releases of that software release train also support that feature.

Feature Name

Releases

Feature Information

Configuring Media Path

The following commands were introduced by this feature: media-flow around, media flow-through, media
                                                						anti-trombone .

## Configure Media Flow-Through

### SUMMARY STEPS

- enable

- configure terminal

- Use one of the following commands to configure media flow-through:

- media flow-through in dial-peer configuration mode

- media flow-through in global VoIP configuration mode

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables privileged EXEC mode. Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global configuration mode.

Step 3

Use one of the following commands to configure media flow-through:

- media flow-through in dial-peer configuration mode

- media flow-through in global VoIP configuration mode

### Example:

```
! Applying flow-through to one dial peer only
Device (config) dial-peer voice 10 voip Device (config-dial-peer) media flow-through Device (config-dial-peer) end
```

### Example:

```
! Applying flow-through globally
Device(config)# voice service voip Device(config-voi-serv)# media flow-through Device(config-voi-serv)# end
```

Ensures that all media traffic passes through CUBE .

Step 4

end

Exits to privileged EXEC mode.

## Configure Media Flow-Around

### SUMMARY STEPS

- enable

- configure terminal

- Use one of the
                              			 following commands to configure media flow-around:

- media flow-around in dial-peer configuration mode

- media flow-around in global VoIP configuration mode

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables
                                          				privileged EXEC mode. Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

Use one of the
                                       			 following commands to configure media flow-around:

- media flow-around in dial-peer configuration mode

- media flow-around in global VoIP configuration mode

### Example:

```
! Applying flow-around to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# media flow-around Device (config-dial-peer)# end
```

### Example:

```
! Applying flow-around globally
Device(config)# voice service voip Device(config-voi-serv)# media flow-around Device(config-voi-serv)# end
```

Allows media packets to flow directly between endpoints.

Step 4

end

Exits to
                                          				privileged EXEC mode.

## Configure Media Anti-Tromboning

### Before you begin

Configure mode border-element command under voice service voip , global VoIP configuration mode.

### SUMMARY STEPS

- enable

- configure terminal

- Enter one of the following commands to configure media antitromboning:

- media anti-trombone in dial-peer configuration mode

- media anti-trombone in global VoIP configuration mode

- end

### DETAILED STEPS

Step 1

enable

### Example:

```
Device> enable
```

Enables
                                          				privileged EXEC mode. Enter your password if prompted.

Step 2

configure terminal

### Example:

```
Device# configure terminal
```

Enters global
                                          				configuration mode.

Step 3

Enter one of the following commands to configure media antitromboning:

- media anti-trombone in dial-peer configuration mode

- media anti-trombone in global VoIP configuration mode

### Example:

```
! Applying anti-trombone to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# media anti-trombone Device (config-dial-peer)# end
```

### Example:

```
! Applying anti-trombone globally
Device(config)# voice service voip Device(config-voi-serv)# media anti-trombone Device(config-voi-serv)# end
```

Enables media anti-trombone for all calls.

Step 4

end

Exits to
                                          				privileged EXEC mode.

| Note | H.323 protocol is no longer supported from Cisco IOS XE Bengaluru 17.6.1a onwards. Consider using SIP for multimedia applications. |
|---|---|

| Feature Name | Releases | Feature Information |
|---|---|---|
| Configuring Media Path | Baseline functionality | The following commands were introduced by this feature: media-flow around, media flow-through, media
                                                						anti-trombone . |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global configuration mode. |
| Step 3 | Use one of the following commands to configure media flow-through: media flow-through in dial-peer configuration mode media flow-through in global VoIP configuration mode Example: In dial-peer configuration mode ! Applying flow-through to one dial peer only
Device (config) dial-peer voice 10 voip Device (config-dial-peer) media flow-through Device (config-dial-peer) end Example: In global VoIP SIP mode ! Applying flow-through globally
Device(config)# voice service voip Device(config-voi-serv)# media flow-through Device(config-voi-serv)# end | Ensures that all media traffic passes through CUBE . |
| Step 4 | end | Exits to privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | Use one of the
                                       			 following commands to configure media flow-around: media flow-around in dial-peer configuration mode media flow-around in global VoIP configuration mode Example: In dial-peer configuration mode ! Applying flow-around to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# media flow-around Device (config-dial-peer)# end Example: In global VoIP SIP mode ! Applying flow-around globally
Device(config)# voice service voip Device(config-voi-serv)# media flow-around Device(config-voi-serv)# end | Allows media packets to flow directly between endpoints. |
| Step 4 | end | Exits to
                                          				privileged EXEC mode. |

|  | Command or Action | Purpose |
|---|---|---|
| Step 1 | enable Example: Device> enable | Enables
                                          				privileged EXEC mode. Enter your password if prompted. |
| Step 2 | configure terminal Example: Device# configure terminal | Enters global
                                          				configuration mode. |
| Step 3 | Enter one of the following commands to configure media antitromboning: media anti-trombone in dial-peer configuration mode media anti-trombone in global VoIP configuration mode Example: In dial-peer configuration mode ! Applying anti-trombone to one dial peer only
Device (config)# dial-peer voice 10 voip Device (config-dial-peer)# media anti-trombone Device (config-dial-peer)# end Example: In global VoIP SIP mode ! Applying anti-trombone globally
Device(config)# voice service voip Device(config-voi-serv)# media anti-trombone Device(config-voi-serv)# end | Enables media anti-trombone for all calls. |
| Step 4 | end | Exits to
                                          				privileged EXEC mode. |